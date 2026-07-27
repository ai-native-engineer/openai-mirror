"""openai.com 공개 페이지 전체 크롤 (curl_cffi 브라우저 지문 위장 -> 캡챠·브라우저 불필요).

openai.com은 Cloudflare 봇 챌린지 뒤에 있어 일반 헤드리스 브라우저는 캡챠('Just a moment...')에 막힌다.
대신 curl_cffi(impersonate="chrome")로 Chrome의 TLS/JA3 지문을 위장하면 CF를 캡챠 없이 통과한다(실측 200, 풀 본문).
페이지는 Next.js SSR이라 HTML에 본문이 들어있어 브라우저 렌더가 필요 없다(codex 같은 마케팅 페이지도 풀 텍스트).

URL은 sitemap.xml 인덱스에서 받는다. 본문은 <main>을 bs4로 뽑아 markdownify -> 마크다운.
crawl-mirror.save/dest/find_boilerplate를 재사용해 <out>/openai.com/<path>.md 트리로 저장(증분: 기존 .md는 skip).

실행: python3 crawl-site.py <out_dir> [--include seg,seg] [--exclude seg,seg] [--force] [--limit N] [--concurrency N]
"""
import argparse, importlib.util, os, re, sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlsplit, urljoin
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

CM_PATH = os.environ.get(
    "CRAWL_MIRROR_PATH",
    os.path.expanduser("~/.agents/skills/shared/crawl/scripts/crawl-mirror.py"),
)
if not os.path.isfile(CM_PATH):
    raise SystemExit(f"crawl skill dependency not found: {CM_PATH}")
SITEMAP = "https://openai.com/sitemap.xml"
ROOT = "https://openai.com/"
FOUNDATION = "https://openaifoundation.org/"
FUND = "https://openai.fund/"
ALIGNMENT = "https://alignment.openai.com/"
SPINNING_UP = "https://spinningup.openai.com/en/latest/"
PROGRESS = "https://progress.openai.com/"
DEVDAY = "https://devday.openai.com/"
IMPERSONATE = "chrome"
# sitemap에 없는 제품·마케팅 페이지(chatgpt·gpt-5·apps·customer-stories 등)를 잡기 위한 내부 링크 발견 허브
HUBS = [ROOT] + [ROOT.rstrip("/") + p for p in [
    "/chatgpt/", "/business/", "/api/", "/safety/", "/research/", "/stories/", "/news/",
    "/policies/", "/codex/", "/about/", "/gpt-5/", "/sora/", "/apps/", "/agent-platform/",
    "/customer-stories/", "/solutions/", "/index/"]]

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)


def get(url):
    r = requests.get(url, impersonate=IMPERSONATE, timeout=40)
    return r.status_code, r.text


def sitemap_urls():
    """sitemap 인덱스 -> 모든 자식 sitemap -> URL 집합."""
    _, idx = get(SITEMAP)
    children = re.findall(r"<loc>(.*?)</loc>", idx)
    urls = set()
    for c in children:
        try:
            _, t = get(c)
            urls.update(re.findall(r"<loc>(.*?)</loc>", t))
        except Exception as e:
            print(f"  sitemap ERR {c}: {e}", flush=True)
    urls.add(ROOT)
    return urls


def discover_internal():
    """허브 페이지에서 openai.com 내부 링크를 1-depth 수집 (sitemap에 없는 제품·마케팅 페이지 보강)."""
    from urllib.parse import urljoin
    found = set()
    for h in HUBS:
        try:
            _, html = get(h)
            soup = BeautifulSoup(html, "html.parser")
        except Exception:
            continue
        for a in soup.find_all("a", href=True):
            u = urljoin(h, a["href"]).split("#")[0].split("?")[0]
            if urlsplit(u).netloc == "openai.com" and not u.endswith((".xml", ".pdf")):
                found.add(u if u.endswith("/") else u + "/")
    return found


def discover_local(out, host):
    """기존 생성물이 알고 있는 절대 링크를 재사용. 고정 허브가 놓친 깊은 페이지를 다음 증분에서 복구한다."""
    # ponytail: 폐기 링크도 재확인한다. 갱신 시간이 문제가 될 때만 TTL miss cache를 추가한다.
    root = os.path.join(out, host)
    found = set()
    if not os.path.isdir(root):
        return found
    for base, _, files in os.walk(root):
        for name in files:
            if not name.endswith(".md"):
                continue
            with open(os.path.join(base, name), encoding="utf-8", errors="ignore") as f:
                text = f.read()
            for raw in re.findall(r"https?://[^\s<>\"'`)\]]+", text):
                u = raw.rstrip(".,;:!?")
                p = urlsplit(u)
                if u.isascii() and p.netloc == host and not p.query and not p.fragment and not p.path.lower().endswith(
                    (".css", ".gif", ".ico", ".jpg", ".jpeg", ".js", ".json", ".png", ".svg", ".webp", ".xml", ".pdf")
                ):
                    found.add(u)
    return found


def seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return parts[0] if parts else ""


def html_to_md(html):
    """본문 컨테이너(main/article/body 중 텍스트가 가장 많은 것)를 추출해 nav/footer/script 제거 후 markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    cands = [c for c in (soup.find("main"), soup.find("article"), soup.body) if c is not None]
    if not cands:
        return ""
    node = max(cands, key=lambda c: len(c.get_text(strip=True)))
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    return "\n".join(line.rstrip() for line in md(str(node), heading_style="ATX").strip().splitlines())


def fetch_one(url):
    try:
        status, html = get(url)
        if status != 200 or "Just a moment" in html[:5000]:
            return url, "", f"status={status}"
        return url, html_to_md(html), ""
    except Exception as e:
        return url, "", str(e)[:80]


def failure_kind(err):
    if not err:
        return "thin"
    if err.startswith("status="):
        return f"http-{err.removeprefix('status=')}"
    return "network/extract"


def crawl(urls, concurrency):
    pages, fails = {}, []
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {ex.submit(fetch_one, u): u for u in urls}
        done = 0
        for f in as_completed(futs):
            url, mdtext, err = f.result()
            done += 1
            if mdtext and len(mdtext) >= 200:
                pages[url] = mdtext
            else:
                fails.append((url, err))
            if done % 50 == 0:
                print(f"  {done}/{len(urls)} (성공 {len(pages)}, 미저장 {len(fails)})", flush=True)
    return pages, fails


def crawl_sibling(base, dom, concurrency, out, force, depth=1, cap=120):
    """sitemap 없는 형제 사이트: 루트 + 같은 도메인 링크 BFS.
    트랙 A와 같은 증분: 기존 .md는 skip(없으면 재크롤 시 boilerplate 차이로 헛 diff가 생긴다)."""
    links, seen, queue = {base}, set(), [(base, 0)]
    while queue and len(links) < cap:
        current, level = queue.pop(0)
        if current in seen or level >= depth:
            continue
        seen.add(current)
        status, html = get(current)
        if status != 200:
            continue
        for a in BeautifulSoup(html, "html.parser").find_all("a", href=True):
            u = urljoin(current, a["href"]).split("#")[0].split("?")[0]
            p = urlsplit(u)
            if p.netloc == dom and not p.path.lower().endswith((".xml", ".pdf")) and u not in links:
                links.add(u)
                queue.append((u, level + 1))
    links |= discover_local(out, dom)
    links = sorted(links)[:cap]
    if not force:
        links = [l for l in links if not os.path.exists(cm.dest(out, l)[0])]
    pages, _ = crawl(links, concurrency) if links else ({}, [])
    return pages


def main():
    if sys.argv[1:] == ["--self-test"]:
        assert failure_kind("") == "thin"
        assert failure_kind("status=404") == "http-404"
        assert failure_kind("timed out") == "network/extract"
        import tempfile
        d = tempfile.mkdtemp()
        os.makedirs(os.path.join(d, "openai.com"))
        with open(os.path.join(d, "openai.com", "x.md"), "w") as f:
            f.write("[ok](https://openai.com/index/deep/) ![](https://openai.com/x.png) "
                    "[other](https://example.com/x) [bad](https://openai.com/about\u2060)")
        assert discover_local(d, "openai.com") == {"https://openai.com/index/deep/"}
        print("self-test ok")
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--include", default="", help="포함할 첫 세그먼트 csv (예: index,research,news)")
    ap.add_argument("--exclude", default="", help="제외할 첫 세그먼트 csv (예: form,academy)")
    ap.add_argument("--force", action="store_true", help="기존 .md도 다시 크롤")
    ap.add_argument("--limit", type=int, default=0, help="크롤 URL 상한")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--no-discover", action="store_true", help="허브 내부 링크 발견 생략(sitemap만)")
    a = ap.parse_args()

    inc = set(s for s in a.include.split(",") if s)
    exc = set(s for s in a.exclude.split(",") if s)

    print("sitemap 수집 중...", flush=True)
    urls = sitemap_urls()
    if not a.no_discover and not a.limit:
        extra = discover_internal() | discover_local(a.out, "openai.com")
        new = extra - {u if u.endswith("/") else u + "/" for u in urls}
        urls |= extra
        print(f"내부 링크 발견: +{len(new)} (sitemap 외)", flush=True)
    if inc:
        urls = {u for u in urls if seg(u) in inc or u == ROOT}
    if exc:
        urls = {u for u in urls if seg(u) not in exc}
    if not a.force:
        urls = {u for u in urls if not os.path.exists(cm.dest(a.out, u)[0])}
    urls = sorted(urls)
    if a.limit:
        urls = urls[:a.limit]
    print(f"크롤 대상: {len(urls)} (concurrency={a.concurrency})", flush=True)

    pages, fails = ({}, [])
    if urls:
        pages, fails = crawl(urls, a.concurrency)

    if not inc and not a.limit:
        for label, base, dom, depth, cap in [
            ("foundation", FOUNDATION, "openaifoundation.org", 2, 120),
            ("fund", FUND, "openai.fund", 2, 120),
            ("alignment", ALIGNMENT, "alignment.openai.com", 2, 120),
            ("spinning-up", SPINNING_UP, "spinningup.openai.com", 3, 160),
            ("progress", PROGRESS, "progress.openai.com", 1, 20),
            ("devday", DEVDAY, "devday.openai.com", 1, 20),
        ]:
            try:
                sp = crawl_sibling(base, dom, a.concurrency, a.out, a.force, depth, cap)
                pages.update(sp)
                print(f"{label}: {len(sp)} pages", flush=True)
            except Exception as e:
                print(f"{label} ERR: {e}", flush=True)

    if len(pages) >= 5:
        boiler = cm.find_boilerplate(list(pages.values()), 0.4)
        if boiler:
            pages = {u: cm.strip_boilerplate(m, boiler) for u, m in pages.items()}
            print(f"boilerplate: {len(boiler)} lines removed", flush=True)
    for u, m in pages.items():
        cm.save(a.out, u, m, False)
    print(f"저장: {len(pages)} / 미저장: {len(fails)}", flush=True)
    if fails:
        kinds = Counter(failure_kind(err) for _, err in fails)
        print("미저장 분류(재실행 시 자동 재시도): " + " / ".join(
            f"{kind} {count}" for kind, count in sorted(kinds.items())), flush=True)
        for kind in sorted(kinds):
            for u, err in [(u, err) for u, err in fails if failure_kind(err) == kind][:5]:
                print(f"  {kind}: {u} [{err}]", flush=True)


if __name__ == "__main__":
    main()
