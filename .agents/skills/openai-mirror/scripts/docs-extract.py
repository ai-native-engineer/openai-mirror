"""OpenAI 공식 문서 표면 추출 — 로그인·CF 우회 불필요, curl_cffi.

openai.com/academy 외의 공식 문서 표면을 같은 curl_cffi 방식으로 받는다:
- developers.openai.com: sitemap + sitemap에 없는 모델 상세 인덱스.
- help.openai.com: Intercom 헬프센터. sitemap 없음 -> 홈 -> collections -> articles BFS 열거.
- model-spec.openai.com: Model Spec 단일 문서(루트가 날짜별 .html로 링크).
- learn.chatgpt.com / deploymentsafety.openai.com: sitemap.
- trust.openai.com: 비로그인 루트 개요(상세 문서는 인증 포털 UI).

출력 <out>/<host>/<path>.md (증분). crawl-mirror.save/dest/find_boilerplate 재사용.

실행: python3 docs-extract.py <out_dir> [--only developers,help,model-spec,learn,deployment-safety,trust] [--force] [--limit N] [--concurrency N]
"""
import argparse, importlib.util, os, re, sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin, urlsplit
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

CM_PATH = os.environ.get(
    "CRAWL_MIRROR_PATH",
    os.path.expanduser("~/.agents/skills/shared/crawl/scripts/crawl-mirror.py"),
)
if not os.path.isfile(CM_PATH):
    raise SystemExit(f"crawl skill dependency not found: {CM_PATH}")
DEV_SITEMAP = "https://developers.openai.com/sitemap-0.xml"
DEV_MODELS = "https://developers.openai.com/api/docs/models/all"
HELP_HOME = "https://help.openai.com/en"
HELP_BASE = "https://help.openai.com"
MODELSPEC = "https://model-spec.openai.com/"
LEARN_SITEMAP = "https://learn.chatgpt.com/sitemap-index.xml"
DEPLOYMENT_SITEMAP = "https://deploymentsafety.openai.com/sitemap.xml"
DEPLOYMENT_BASE = "https://deploymentsafety.openai.com"
TRUST = "https://trust.openai.com/"
IMPERSONATE = "chrome"

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)


def get(url, **kw):
    return requests.get(url, impersonate=IMPERSONATE, timeout=40, **kw)


def html_to_md(html):
    soup = BeautifulSoup(html, "html.parser")
    for t in soup(["script", "style", "noscript", "svg"]):
        t.decompose()
    cands = [c for c in (soup.find("main"), soup.find("article"), soup.body) if c is not None]
    if not cands:
        return ""
    node = max(cands, key=lambda c: len(c.get_text(strip=True)))
    for t in node(["nav", "header", "footer", "form"]):
        t.decompose()
    return md(str(node), heading_style="ATX").strip()


def fetch_one(url):
    try:
        r = get(url)
        if r.status_code != 200:
            return url, "", f"status={r.status_code}"
        return url, html_to_md(r.text), "thin"
    except Exception as e:
        return url, "", str(e)[:80]


def crawl_urls(urls, out, concurrency, min_len=200):
    pages, fails, done = {}, [], 0
    with ThreadPoolExecutor(max_workers=concurrency) as ex:
        futs = {ex.submit(fetch_one, u): u for u in urls}
        for f in as_completed(futs):
            url, body, err = f.result()
            done += 1
            if body and len(body) >= min_len:
                pages[url] = body
            else:
                fails.append((url, err))
            if done % 100 == 0:
                print(f"  {done}/{len(urls)} (성공 {len(pages)}, 실패 {len(fails)})", flush=True)
    # boilerplate: 표본 200개로 공통 라인 도출 후 전체 strip (대량 셋 비용 절감)
    vals = list(pages.values())
    if len(vals) >= 5:
        boiler = cm.find_boilerplate(vals[:200], 0.4)
        if boiler:
            pages = {u: cm.strip_boilerplate(m, boiler) for u, m in pages.items()}
            print(f"  boilerplate: {len(boiler)} lines removed", flush=True)
    for u, m in pages.items():
        cm.save(out, u, m, False)
    return len(pages), fails


def to_crawl(urls, out, force, limit):
    urls = sorted(set(urls))
    if not force:
        urls = [u for u in urls if not os.path.exists(cm.dest(out, u)[0])]
    return urls[:limit] if limit else urls


def replace_origin(loc, origin):
    p = urlsplit(loc)
    return origin.rstrip("/") + p.path if origin and p.hostname in {"localhost", "127.0.0.1"} else loc


def sitemap_urls(url, origin=""):
    """Sitemap/index loc을 재귀 열거. Deployment sitemap의 localhost build URL은 공개 origin으로 교정."""
    seen, pages, queue = set(), set(), [url]
    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)
        locs = re.findall(r"<loc>(.*?)</loc>", get(current).text)
        for loc in locs:
            loc = replace_origin(loc, origin)
            if loc.endswith(".xml"):
                queue.append(loc)
            else:
                pages.add(loc)
    return pages


def model_urls(html):
    soup = BeautifulSoup(html, "html.parser")
    return {
        urljoin(DEV_MODELS, a["href"]).split("#")[0].split("?")[0]
        for a in soup.find_all("a", href=True)
        if urlsplit(urljoin(DEV_MODELS, a["href"])).netloc == "developers.openai.com"
        and urlsplit(urljoin(DEV_MODELS, a["href"])).path.startswith("/api/docs/models/")
    }


def developers(out, conc, force, limit):
    print("developers.openai.com sitemap...", flush=True)
    locs = sitemap_urls(DEV_SITEMAP) | model_urls(get(DEV_MODELS).text)
    urls = to_crawl(locs, out, force, limit)
    print(f"developers 대상: {len(urls)}", flush=True)
    if urls:
        n, fails = crawl_urls(urls, out, conc)
        print(f"developers 저장: {n} / 실패: {len(fails)}", flush=True)


def sitemap_site(label, sitemap, out, conc, force, limit, replace_origin=""):
    print(f"{label} sitemap...", flush=True)
    urls = to_crawl(sitemap_urls(sitemap, replace_origin), out, force, limit)
    print(f"{label} 대상: {len(urls)}", flush=True)
    if urls:
        n, fails = crawl_urls(urls, out, conc)
        print(f"{label} 저장: {n} / 실패: {len(fails)}", flush=True)


def single_page(label, url, out, force):
    urls = to_crawl([url], out, force, 0)
    if not urls:
        return
    target, body, err = fetch_one(url)
    if body:
        cm.save(out, target, body, False)
        print(f"{label} 저장: {target}", flush=True)
    else:
        print(f"{label} 실패: {err}", flush=True)


def help_center(out, conc, force, limit):
    print("help.openai.com 열거(BFS)...", flush=True)
    seen, arts, queue = set(), set(), []
    home = BeautifulSoup(get(HELP_HOME).text, "html.parser")
    queue = [urljoin(HELP_BASE, a["href"]) for a in home.find_all("a", href=True) if "/collections/" in a["href"]]
    while queue:
        col = queue.pop()
        if col in seen:
            continue
        seen.add(col)
        try:
            soup = BeautifulSoup(get(col).text, "html.parser")
        except Exception:
            continue
        for a in soup.find_all("a", href=True):
            h = urljoin(HELP_BASE, a["href"])
            if "/articles/" in h:
                arts.add(h.split("?")[0])
            elif "/collections/" in h and h not in seen:
                queue.append(h)
    print(f"help articles: {len(arts)} (collections {len(seen)})", flush=True)
    urls = to_crawl(arts, out, force, limit)
    if urls:
        n, fails = crawl_urls(urls, out, conc)
        print(f"help 저장: {n} / 실패: {len(fails)}", flush=True)


def model_spec(out):
    print("model-spec.openai.com...", flush=True)
    root = get(MODELSPEC)
    # 루트는 meta refresh로 날짜별 .html을 가리킨다 (예: content="0; url=2025-12-18.html")
    m = re.search(r'url=([^"\'\s>]+\.html)', root.text) or re.search(r'href=["\']?([^"\'\s>]+\.html)', root.text)
    target = urljoin(MODELSPEC, m.group(1)) if m else MODELSPEC
    url, body, err = fetch_one(target)
    if body:
        cm.save(out, url, body, False)
        print(f"model-spec 저장: {url}", flush=True)
    else:
        print(f"model-spec 실패: {err}", flush=True)


def main():
    if sys.argv[1:] == ["--self-test"]:
        assert model_urls('<a href="/api/docs/models/gpt-5">x</a><a href="/api/docs/guides/x">no</a>') == {
            "https://developers.openai.com/api/docs/models/gpt-5"
        }
        assert replace_origin("http://localhost:4321/gpt-5/system-card/", DEPLOYMENT_BASE) == \
               "https://deploymentsafety.openai.com/gpt-5/system-card/"
        print("self-test ok")
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--only", default="developers,help,model-spec,learn,deployment-safety,trust", help="대상 csv")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=8)
    a = ap.parse_args()
    only = set(s.strip() for s in a.only.split(",") if s.strip())

    if "developers" in only:
        developers(a.out, a.concurrency, a.force, a.limit)
    if "help" in only:
        help_center(a.out, a.concurrency, a.force, a.limit)
    if "model-spec" in only:
        model_spec(a.out)
    if "learn" in only:
        sitemap_site("learn.chatgpt.com", LEARN_SITEMAP, a.out, a.concurrency, a.force, a.limit)
    if "deployment-safety" in only:
        sitemap_site("deploymentsafety.openai.com", DEPLOYMENT_SITEMAP, a.out, a.concurrency,
                     a.force, a.limit, DEPLOYMENT_BASE)
    if "trust" in only:
        single_page("trust.openai.com", TRUST, a.out, a.force)


if __name__ == "__main__":
    main()
