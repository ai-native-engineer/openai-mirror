"""openai.com 공개 페이지 전체 크롤 (curl_cffi 브라우저 지문 위장 -> 캡챠·브라우저 불필요).

openai.com은 Cloudflare 봇 챌린지 뒤에 있어 일반 헤드리스 브라우저는 캡챠('Just a moment...')에 막힌다.
대신 curl_cffi(impersonate="chrome")로 Chrome의 TLS/JA3 지문을 위장하면 CF를 캡챠 없이 통과한다(실측 200, 풀 본문).
페이지는 Next.js SSR이라 HTML에 본문이 들어있어 브라우저 렌더가 필요 없다(codex 같은 마케팅 페이지도 풀 텍스트).

URL은 sitemap.xml 인덱스에서 받는다. 본문은 <main>을 bs4로 뽑아 markdownify -> 마크다운.
crawl-mirror.save/dest/find_boilerplate를 재사용해 <out>/openai.com/<path>.md 트리로 저장(증분: 기존 .md는 skip).
실행 결과(발견·저장·재시도·404 판정)는 <out>/_mirror-state/ manifest에 남는다.

실행: python3 crawl-site.py <out_dir> [--include seg,seg] [--exclude seg,seg] [--force] [--limit N] [--concurrency N]
      [--retries N] [--retry-backoff S] [--retry-max-wait S]
"""

import argparse, importlib.util, os, re, sys
from urllib.parse import urlsplit, urljoin
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mirror_state as ms  # noqa: E402

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
MIN_LEN = 200
# sitemap에 없는 제품·마케팅 페이지(chatgpt·gpt-5·apps·customer-stories 등)를 잡기 위한 내부 링크 발견 허브
HUBS = [ROOT] + [
    ROOT.rstrip("/") + p
    for p in [
        "/chatgpt/",
        "/business/",
        "/api/",
        "/safety/",
        "/research/",
        "/stories/",
        "/news/",
        "/policies/",
        "/codex/",
        "/about/",
        "/gpt-5/",
        "/sora/",
        "/agent-platform/",
        "/customer-stories/",
        "/solutions/",
        "/index/",
    ]
]
SIBLINGS = [  # label, base, domain, BFS depth, 발견 상한(넘치면 열거 오류)
    ("foundation", FOUNDATION, "openaifoundation.org", 2, 400),
    ("fund", FUND, "openai.fund", 2, 400),
    ("alignment", ALIGNMENT, "alignment.openai.com", 2, 400),
    ("spinning-up", SPINNING_UP, "spinningup.openai.com", 3, 400),
    ("progress", PROGRESS, "progress.openai.com", 1, 100),
    ("devday", DEVDAY, "devday.openai.com", 1, 100),
]

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)


def raw(url):
    """HTML 원문. Cloudflare challenge는 재시도 가능한 오류로 돌려준다."""
    r = requests.get(url, impersonate=IMPERSONATE, timeout=40)
    res = ms.Result(
        url,
        body=r.text,
        status=r.status_code,
        retry_after=ms.parse_retry_after(r.headers.get("retry-after")),
    )
    res.final_url = r.url
    if "Just a moment" in r.text[:5000]:
        res.error = f"cloudflare challenge (status={r.status_code})"
    elif r.status_code == 403 and "cloudflare" in r.headers.get("server", "").lower():
        # challenge 문구 없는 403도 간헐 차단이다(2026-09-30: 같은 URL이 403 뒤 재요청에서 404). 재시도 대상으로 둔다.
        res.error = "cloudflare 403"
    return res


def sitemap_urls(policy, manifest):
    """sitemap 인덱스 -> 모든 자식 sitemap -> URL 집합. 실패한 sitemap은 열거 오류로 남긴다."""
    urls = {ROOT}
    idx = policy.run(raw, SITEMAP)
    if idx.status != 200 or idx.error:
        manifest.enum_error(SITEMAP, f"{idx.kind} {idx.error}".strip(), "openai.com")
        return urls
    for c in re.findall(r"<loc>(.*?)</loc>", idx.body):
        res = policy.run(raw, c)
        if res.status != 200 or res.error:
            print(f"  sitemap ERR {c}: {res.kind} {res.error}", flush=True)
            manifest.enum_error(c, f"{res.kind} {res.error}".strip(), "openai.com")
            continue
        urls.update(re.findall(r"<loc>(.*?)</loc>", res.body))
    return urls


def discover_internal(policy, manifest):
    """허브 페이지에서 openai.com 내부 링크를 1-depth 수집 (sitemap에 없는 제품·마케팅 페이지 보강)."""
    found = set()
    for h in HUBS:
        res = policy.run(raw, h)
        if res.status in (404, 410) and not res.error and policy.run(raw, h).status in (404, 410):
            # 허브는 발견 보조 수단이다. 사라진 허브는 URL 누락이 아니라 HUBS 정리 신호다.
            print(f"  경고: 허브 {h}가 {res.status} 재확인. HUBS에서 제거 필요", flush=True)
            continue
        if res.status != 200 or res.error:
            manifest.enum_error(h, f"hub {res.kind} {res.error}".strip(), "openai.com")
            continue
        for a in BeautifulSoup(res.body, "html.parser").find_all("a", href=True):
            u = urljoin(h, a["href"]).split("#")[0].split("?")[0]
            if urlsplit(u).netloc == "openai.com" and not u.endswith((".xml", ".pdf")):
                found.add(u if u.endswith("/") else u + "/")
    return found


PLAIN_PATH = re.compile(r"^[A-Za-z0-9/_.~-]*$")


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
            for raw_url in re.findall(r"https?://[^\s<>\"'`)\]]+", text):
                u = raw_url.rstrip(".,;:!?")
                try:
                    p = urlsplit(u)
                except ValueError:  # 본문 속 깨진 URL(예: `https://host/[x`)은 링크가 아니다.
                    continue
                if (
                    u.isascii()
                    and p.netloc == host
                    and PLAIN_PATH.match(p.path)  # 인용문 꼬리(",2024.Accessed:")나 붙은 두 URL은 링크가 아니다.
                    and not p.query
                    and not p.fragment
                    and not p.path.lower().endswith(
                        (
                            ".css",
                            ".gif",
                            ".ico",
                            ".jpg",
                            ".jpeg",
                            ".js",
                            ".json",
                            ".png",
                            ".svg",
                            ".webp",
                            ".xml",
                            ".pdf",
                        )
                    )
                ):
                    found.add(u)
    return found


def seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return parts[0] if parts else ""


def is_migrated_docs_url(url):
    """openai.com 아래 죽은 개발자 문서 미러. 정본은 developers/learn 쪽 docs-extract가 담당.

    - /api/docs*, /plugins/*: developers.openai.com 으로 이관
    - /ads/* (허브 제외): developers ads 문서
    - /codex/* (허브 /codex/ 제외): developers/learn codex 문서
    마케팅 허브(/codex/, /ads/ 리다이렉트)는 남긴다.
    """
    p = urlsplit(url)
    if p.netloc != "openai.com":
        return False
    path = p.path if p.path.endswith("/") else p.path + "/"
    if path.startswith("/api/docs") or path.startswith("/api/reference"):
        return True
    if path.startswith("/plugins/"):
        return True
    if path.startswith("/ads/") and path != "/ads/":
        return True
    if path.startswith("/codex/") and path != "/codex/":
        return True
    return False


def html_to_md(html):
    """본문 컨테이너(main/article/body 중 텍스트가 가장 많은 것)를 추출해 nav/footer/script 제거 후 markdown."""
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    cands = [
        c for c in (soup.find("main"), soup.find("article"), soup.body) if c is not None
    ]
    if not cands:
        return ""
    node = max(cands, key=lambda c: len(c.get_text(strip=True)))
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    return "\n".join(
        line.rstrip()
        for line in md(str(node), heading_style="ATX").strip().splitlines()
    )


def fetch_one(url):
    res = raw(url)
    html, res.body = res.body, ""
    if res.error:
        return res
    if res.status == 200:
        res.body = html_to_md(html)
    else:
        res.canonical = ms.canonical_of(html)
    return res


def discover_sibling(base, dom, out, depth, cap, policy, manifest):
    """sitemap 없는 형제 사이트: 루트 + 같은 도메인 링크 BFS. 상한을 넘기면 조용히 자르지 않고 열거 오류로 남긴다."""
    links, seen, queue = {base}, set(), [(base, 0)]
    while queue:
        pending = [q for q in queue if q[1] < depth and q[0] not in seen]
        if len(links) >= cap and pending:
            manifest.enum_error(
                base,
                f"BFS 상한 {cap} 도달: 미열거 페이지 {len(pending)}개",
                "openai-sites",
            )
            break
        current, level = queue.pop(0)
        if current in seen or level >= depth:
            continue
        seen.add(current)
        res = policy.run(raw, current)
        if res.status != 200 or res.error:
            if current == base:
                manifest.enum_error(
                    base, f"root {res.kind} {res.error}".strip(), "openai-sites"
                )
            continue  # 하위 페이지 실패는 그 URL의 수집 기록으로 남는다.
        for a in BeautifulSoup(res.body, "html.parser").find_all("a", href=True):
            u = urljoin(current, a["href"]).split("#")[0].split("?")[0]
            p = urlsplit(u)
            if (
                p.netloc == dom
                and not p.path.lower().endswith((".xml", ".pdf"))
                and u not in links
            ):
                links.add(u)
                queue.append((u, level + 1))
    return links | discover_local(out, dom)


def self_test():
    assert is_migrated_docs_url("https://openai.com/api/docs/pricing/")
    assert is_migrated_docs_url("https://openai.com/codex/long-running-work/")
    assert not is_migrated_docs_url("https://openai.com/codex/")
    assert not is_migrated_docs_url("https://openai.com/index/hello/")
    import tempfile

    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "openai.com"))
    with open(os.path.join(d, "openai.com", "x.md"), "w") as f:
        f.write(
            "[ok](https://openai.com/index/deep/) ![](https://openai.com/x.png) "
            "[other](https://example.com/x) [bad](https://openai.com/about\u2060) https://openai.com[broken https://openai.com/index/x/,2024.Accessed:2025 "
            "https://openai.com/updates/a%3A%20bhttps://openai.com/updates/c"
        )
    assert discover_local(d, "openai.com") == {"https://openai.com/index/deep/"}
    ms.self_test()


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument(
        "--include", default="", help="포함할 첫 세그먼트 csv (예: index,research,news)"
    )
    ap.add_argument(
        "--exclude", default="", help="제외할 첫 세그먼트 csv (예: form,academy)"
    )
    ap.add_argument("--force", action="store_true", help="기존 .md도 다시 크롤")
    ap.add_argument("--limit", type=int, default=0, help="크롤 URL 상한")
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument(
        "--no-discover", action="store_true", help="허브 내부 링크 발견 생략(sitemap만)"
    )
    ap.add_argument("--verify-stale", action="store_true",
                    help="발견 집합 밖 기존 생성물의 원본을 확인해 moved/gone/live로 manifest에 기록(삭제하지 않음)")
    ms.add_retry_args(ap)
    a = ap.parse_args()
    state_dir = a.state_dir or os.path.join(a.out, ms.STATE_DIR)
    policy = ms.policy_from(a)
    manifest = ms.Manifest(a.out, "crawl-site", sys.argv[1:], a.state_dir)

    inc = set(s for s in a.include.split(",") if s)
    exc = set(s for s in a.exclude.split(",") if s)

    print("sitemap 수집 중...", flush=True)
    urls = sitemap_urls(policy, manifest)
    listed = set(urls)
    if not a.no_discover and not a.limit:
        extra = discover_internal(policy, manifest) | discover_local(
            a.out, "openai.com"
        )
        new = extra - {u if u.endswith("/") else u + "/" for u in urls}
        urls |= extra | ms.live_seeds(state_dir, "openai.com")
        print(f"내부 링크 발견: +{len(new)} (sitemap 외)", flush=True)
    if inc:
        urls = {u for u in urls if seg(u) in inc or u == ROOT}
    if exc:
        urls = {u for u in urls if seg(u) not in exc}
    migrated = {u for u in urls if is_migrated_docs_url(u)}
    if migrated:
        urls -= migrated
        print(
            f"이관 docs skip: {len(migrated)} (developers/learn 정본 사용)", flush=True
        )
    slugs = ms.slug_index(listed - migrated)
    if not (inc or exc or a.limit or a.no_discover):
        manifest.complete.add("openai.com")
    manifest.discover(urls)
    site_known = set(urls)
    if not a.force:
        have = {u for u in urls if os.path.exists(cm.dest(a.out, u)[0])}
        manifest.existing(have)
        urls -= have
    urls = sorted(urls)
    if a.limit:
        urls = urls[: a.limit]
    print(
        f"크롤 대상: {len(urls)} (concurrency={a.concurrency}, retries={a.retries})",
        flush=True,
    )
    results = (
        ms.collect(urls, fetch_one, policy, a.concurrency, slugs, label="openai.com ")
        if urls
        else []
    )

    sibling_known = set()
    if not inc and not a.limit:
        manifest.complete.add("openai-sites")
        seeds = ms.live_seeds(state_dir, "openai-sites")
        for label, base, dom, depth, cap in SIBLINGS:
            links = discover_sibling(base, dom, a.out, depth, cap, policy, manifest)
            links |= {u for u in seeds if urlsplit(u).netloc == dom}
            sibling_known |= links
            manifest.discover(links)
            todo = set(links)
            if not a.force:
                have = {u for u in todo if os.path.exists(cm.dest(a.out, u)[0])}
                manifest.existing(have)
                todo -= have
            sib = (
                ms.collect(
                    sorted(todo), fetch_one, policy, a.concurrency, ms.slug_index(links)
                )
                if todo
                else []
            )
            results += sib
            print(f"{label}: 발견 {len(links)} / 수집 {len(todo)}", flush=True)
            listed |= links

    pages = ms.candidate_pages(results, MIN_LEN, listed)
    if len(pages) >= 5:
        boiler = cm.find_boilerplate(list(pages.values()), 0.4)
        if boiler:
            pages = {u: cm.strip_boilerplate(m, boiler) for u, m in pages.items()}
            print(f"boilerplate: {len(boiler)} lines removed", flush=True)
    pages, dropped = ms.keep_pages(pages, MIN_LEN, cm.strip_chrome)
    for u, m in pages.items():
        cm.save(a.out, u, m, False)
    ms.record_results(manifest, results, pages, dropped, MIN_LEN)
    print(f"저장: {len(pages)} / 미저장: {len(results) - len(pages)}", flush=True)
    if a.verify_stale:
        if "openai.com" in manifest.complete:
            ms.verify_stale(manifest, a.out, "openai.com", site_known, raw, policy, a.concurrency,
                            adopt_live=lambda u: not is_migrated_docs_url(u))  # 이관 경로는 live여도 편입하지 않는다.
        if "openai-sites" in manifest.complete:
            ms.verify_stale(manifest, a.out, "openai-sites", sibling_known, raw, policy, a.concurrency)
    unresolved = manifest.report()
    print(f"manifest: {manifest.write()}", flush=True)
    if unresolved:
        raise SystemExit(
            f"crawl-site unresolved {unresolved}개: 재시도 소진, 열거 실패 또는 확정되지 않은 404"
        )


if __name__ == "__main__":
    main()
