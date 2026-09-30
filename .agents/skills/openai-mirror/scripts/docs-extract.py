"""OpenAI 공식 문서 표면 추출 — 로그인·CF 우회 불필요, curl_cffi.

openai.com/academy 외의 공식 문서 표면을 같은 curl_cffi 방식으로 받는다:
- developers.openai.com: sitemap + sitemap에 없는 모델 상세 인덱스.
- help.openai.com: Intercom 헬프센터. sitemap 없음 -> 홈 -> collections -> articles BFS 열거.
- model-spec.openai.com: Model Spec 단일 문서(루트가 날짜별 .html로 링크).
- learn.chatgpt.com / deploymentsafety.openai.com: sitemap.
- trust.openai.com: 비로그인 루트 개요(상세 문서는 인증 포털 UI).

출력 <out>/<host>/<path>.md (증분). crawl-mirror.save/dest/find_boilerplate 재사용.
실행 결과는 <out>/_mirror-state/ manifest에 표면별로 남는다.

실행: python3 docs-extract.py <out_dir> [--only developers,help,model-spec,learn,deployment-safety,trust] [--force]
      [--limit N] [--concurrency N] [--prune-stale] [--retries N] [--retry-backoff S] [--retry-max-wait S]
"""

import argparse, importlib.util, os, re, sys
from urllib.parse import urljoin, urlsplit
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
DEV_SITEMAP = "https://developers.openai.com/sitemap-0.xml"
DEV_MODELS = "https://developers.openai.com/api/docs/models/all"
DEV_REFERENCE = "https://developers.openai.com/api/reference/overview"
REF_CONTAINERS = {"resources", "subresources", "methods"}
HELP_HOME = "https://help.openai.com/en"
HELP_BASE = "https://help.openai.com"
MODELSPEC = "https://model-spec.openai.com/"
LEARN_SITEMAP = "https://learn.chatgpt.com/sitemap-index.xml"
DEPLOYMENT_SITEMAP = "https://deploymentsafety.openai.com/sitemap.xml"
DEPLOYMENT_BASE = "https://deploymentsafety.openai.com"
TRUST = "https://trust.openai.com/"
IMPERSONATE = "chrome"
MIN_LEN = 200
RUN = {"verify_stale": False, "state_dir": ""}  # main에서 채우는 실행 옵션
CURATED = {"model-spec", "deployment-safety", "trust"}  # 최신 문서/상위 카드/개요만 저장하는 표면
DOC_HOSTS = {"developers.openai.com", "learn.chatgpt.com"}

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)


def get(url, **kw):
    return requests.get(url, impersonate=IMPERSONATE, timeout=40, **kw)


def raw(url):
    r = get(url)
    res = ms.Result(
        url,
        body=r.text,
        status=r.status_code,
        retry_after=ms.parse_retry_after(r.headers.get("retry-after")),
    )
    res.final_url = r.url
    return res


def html_to_md(html):
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


def markdown_twin(url):
    """developers/learn 문서는 path.md 로 text/markdown 원문을 제공한다. 실패하면 HTML 경로로 넘어간다."""
    p = urlsplit(url)
    if p.netloc not in DOC_HOSTS:
        return ""
    path = p.path.rstrip("/")
    if not path or path.endswith(".md"):
        return ""
    try:
        r = get(f"{p.scheme}://{p.netloc}{path}.md")
    except Exception:
        return ""
    ct = r.headers.get("content-type", "")
    body = r.text.strip()
    if (
        r.status_code == 200
        and body
        and ("text/markdown" in ct or body.lstrip().startswith("#"))
    ):
        return body
    return ""


def soft_redirect_target(url, body):
    """클라이언트 soft-redirect 페이지: 'Redirecting from `/a` to `/b`'."""
    m = re.search(r"Redirecting from\s+`[^`]+`\s+to\s+`([^`]+)`", body)
    if not m:
        m = re.search(r"Redirecting from\s+\S+\s+to\s+`?(/[^`'\s\]]+)`?", body)
    if not m:
        return ""
    return urljoin(url, m.group(1))


def fetch_one(url, depth=0):
    md_body = markdown_twin(url)
    if len(md_body) >= MIN_LEN:
        return ms.Result(url, body=md_body, status=200)
    r = get(url)
    res = ms.Result(
        url,
        status=r.status_code,
        retry_after=ms.parse_retry_after(r.headers.get("retry-after")),
    )
    if r.status_code != 200:
        res.canonical = ms.canonical_of(r.text)
        return res
    res.body = html_to_md(r.text)
    if len(res.body) < MIN_LEN and depth < 2:
        tgt = soft_redirect_target(url, res.body)
        host = urlsplit(tgt).netloc if tgt else ""
        if tgt and host in {urlsplit(url).netloc} | DOC_HOSTS:
            moved = fetch_one(tgt, depth + 1)
            # sitemap 원 URL 경로에 저장해 증분 재시도를 끝낸다.
            res.body, res.status, res.error = moved.body, moved.status, moved.error
            res.note = f"soft-redirect -> {tgt}"
            if len(res.body) < MIN_LEN:
                res.thin_reason = f"soft-redirect 대상 {tgt} 본문 {len(res.body)}자"
    return res


def crawl_urls(urls, out, conc, policy, manifest, slugs, listed):
    results = (
        ms.collect(urls, fetch_one, policy, conc, slugs, every=100) if urls else []
    )
    pages = ms.candidate_pages(results, MIN_LEN, listed)
    # boilerplate: 표본 200개로 공통 라인 도출 후 전체 strip (대량 셋 비용 절감)
    # native markdown(.md) 본문은 공통 nav 라인이 없어 strip 대상에서 제외한다.
    html_pages = {u: m for u, m in pages.items() if not m.lstrip().startswith("# ")}
    vals = list(html_pages.values())
    if len(vals) >= 5:
        boiler = cm.find_boilerplate(vals[:200], 0.4)
        if boiler:
            for u in html_pages:
                pages[u] = cm.strip_boilerplate(pages[u], boiler)
            print(f"  boilerplate: {len(boiler)} lines removed", flush=True)
    pages, dropped = ms.keep_pages(pages, MIN_LEN, cm.strip_chrome)
    for u, m in pages.items():
        cm.save(out, u, m, False)
    ms.record_results(manifest, results, pages, dropped, MIN_LEN)
    return len(pages), len(results) - len(pages)


def run_surface(label, surface, pages, out, conc, force, limit, policy, manifest):
    """발견 집합 -> manifest 기록 -> 신규/재수집. limit이 없으면 전체 범위 실행으로 표시한다."""
    pages = set(pages)
    if surface not in CURATED:  # 정책상 일부만 고르는 표면은 sitemap 밖 공개 URL을 편입하지 않는다.
        pages |= ms.live_seeds(RUN["state_dir"], surface)
    manifest.discover(pages)
    todo = set(pages)
    if not force:
        have = {u for u in todo if os.path.exists(cm.dest(out, u)[0])}
        manifest.existing(have)
        todo -= have
    todo = sorted(todo)
    if limit:
        todo = todo[:limit]
    else:
        manifest.complete.add(surface)
    print(f"{label} 발견 {len(pages)} / 대상 {len(todo)}", flush=True)
    if todo:
        n, miss = crawl_urls(
            todo, out, conc, policy, manifest, ms.slug_index(pages), pages
        )
        print(f"{label} 저장: {n} / 미저장: {miss}", flush=True)
    if RUN["verify_stale"] and not limit:
        ms.verify_stale(manifest, out, surface, pages, raw, policy, conc,
                        lambda url, body: soft_redirect_target(url, html_to_md(body)),
                        adopt_live=surface not in CURATED)


def replace_origin(loc, origin):
    p = urlsplit(loc)
    return (
        origin.rstrip("/") + p.path
        if origin and p.hostname in {"localhost", "127.0.0.1"}
        else loc
    )


def sitemap_urls(url, policy, manifest, surface, origin=""):
    """Sitemap/index loc을 재귀 열거. Deployment sitemap의 localhost build URL은 공개 origin으로 교정."""
    seen, pages, queue = set(), set(), [url]
    while queue:
        current = queue.pop()
        if current in seen:
            continue
        seen.add(current)
        res = policy.run(raw, current)
        if res.status != 200 or res.error:
            print(f"  sitemap ERR {current}: {res.kind} {res.error}", flush=True)
            manifest.enum_error(current, f"{res.kind} {res.error}".strip(), surface)
            continue
        for loc in re.findall(r"<loc>(.*?)</loc>", res.body):
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
        and urlsplit(urljoin(DEV_MODELS, a["href"])).path.startswith(
            "/api/docs/models/"
        )
    }


def deployment_pages(urls):
    """섹션 URL마다 카드 전체를 반복 렌더하므로 루트 + 상위 시스템 카드만 남긴다."""
    pages = {DEPLOYMENT_BASE + "/"}
    for url in urls:
        parts = [p for p in urlsplit(url).path.split("/") if p]
        if parts:
            pages.add(f"{DEPLOYMENT_BASE}/{parts[0]}/")
    return pages


def reference_links(html, base):
    out = set()
    for x in BeautifulSoup(html, "html.parser").find_all("a", href=True):
        p = urlsplit(urljoin(base, x["href"]))
        if p.netloc == "developers.openai.com" and p.path.startswith("/api/reference/") \
                and not p.query and "__" not in p.path:  # __sdk_schema 같은 쿼리 UI 제외
            out.add(f"https://developers.openai.com{p.path.rstrip('/')}/")
    return out


def reference_ancestors(urls):
    """사이드바는 method leaf만 링크한다. resources/subresources 아래의 리소스 페이지를 경로에서 파생한다."""
    out = set()
    for u in urls:
        parts = [x for x in urlsplit(u).path.split("/") if x]
        for i in range(3, len(parts)):
            if parts[i - 1] in REF_CONTAINERS:
                out.add("https://developers.openai.com/" + "/".join(parts[: i + 1]) + "/")
    return out


def reference_urls(out, policy, manifest):
    """API reference는 sitemap에 없다(2026-09-30 기준 파일 2875개 중 0개 등재).
    overview와 언어 루트 사이드바 + 상위 리소스 경로 + 기존 생성물로 발견한다. CLI 사이드바처럼 일부만 링크하는
    트리가 있어 기존 생성물을 함께 넣고, 사라진 페이지는 --force 재수집의 404 판정으로 걸러진다."""
    ov = policy.run(raw, DEV_REFERENCE)
    if ov.status != 200 or ov.error:
        manifest.enum_error(DEV_REFERENCE, f"{ov.kind} {ov.error}".strip(), "developers")
        return set()
    links = reference_links(ov.body, DEV_REFERENCE)
    base = os.path.join(out, "developers.openai.com", "api", "reference")
    # overview는 언어 중립 resources/*만 링크한다. 언어 루트(python, go, cli ...)는 기존 생성물 디렉터리에서 얻는다.
    sections = {urlsplit(u).path.split("/")[3] for u in links if len(urlsplit(u).path.split("/")) > 4}
    if os.path.isdir(base):
        sections |= {d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d))}
    sections = sorted(sections)
    for sec in sections:
        root = f"https://developers.openai.com/api/reference/{sec}/"
        r = policy.run(raw, root)
        if r.status == 200 and not r.error:
            links |= reference_links(r.body, root)
        elif r.status not in (404, 410):  # 404인 섹션 이름은 루트 페이지가 없는 묶음이다.
            manifest.enum_error(root, f"{r.kind} {r.error}".strip(), "developers")
    links |= reference_ancestors(links)
    for current, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if not d.endswith((".parts", ".assets"))]
        for n in files:
            if n.endswith(".md"):
                rel = os.path.relpath(os.path.join(current, n), out)[:-3]
                links.add(f"https://{rel}/")
    print(f"developers API reference 발견: {len(links)}", flush=True)
    return links


def developers(a, policy, manifest):
    print("developers.openai.com sitemap...", flush=True)
    locs = sitemap_urls(DEV_SITEMAP, policy, manifest, "developers")
    locs |= reference_urls(a.out, policy, manifest)
    models = policy.run(raw, DEV_MODELS)
    if models.status == 200 and not models.error:
        locs |= model_urls(models.body)
    else:
        manifest.enum_error(
            DEV_MODELS, f"{models.kind} {models.error}".strip(), "developers"
        )
    run_surface(
        "developers",
        "developers",
        locs,
        a.out,
        a.concurrency,
        a.force,
        a.limit,
        policy,
        manifest,
    )


def stale_files(out, host, pages):
    desired = {os.path.abspath(cm.dest(out, url)[0]) for url in pages}
    stale = []
    for base, dirs, files in os.walk(os.path.join(out, host)):
        dirs[:] = [d for d in dirs if not d.endswith((".parts", ".assets"))]
        stale.extend(
            os.path.abspath(os.path.join(base, n))
            for n in files
            if n.endswith(".md")
            and os.path.abspath(os.path.join(base, n)) not in desired
        )
    return sorted(stale)


def prune_host(out, host, pages, apply):
    """현재 열거에 없는 구 생성물. 목록은 항상 출력하고 apply일 때만 삭제한다."""
    stale = stale_files(out, host, pages)
    for fp in stale:
        print(
            f"  {'삭제' if apply else '삭제 후보'}: {os.path.relpath(fp, out)}",
            flush=True,
        )
        if apply:
            os.unlink(fp)
    return len(stale)


def help_center(a, policy, manifest):
    print("help.openai.com 열거(BFS)...", flush=True)
    seen, arts = set(), set()
    home = policy.run(raw, HELP_HOME)
    if home.status != 200 or home.error:
        manifest.enum_error(HELP_HOME, f"{home.kind} {home.error}".strip(), "help")
        return
    soup = BeautifulSoup(home.body, "html.parser")
    queue = [
        urljoin(HELP_BASE, x["href"])
        for x in soup.find_all("a", href=True)
        if "/collections/" in x["href"]
    ]
    while queue:
        col = queue.pop()
        if col in seen:
            continue
        seen.add(col)
        res = policy.run(raw, col)
        if res.status != 200 or res.error:
            # collection 하나를 놓치면 그 아래 article 전부가 발견 집합에서 빠진다.
            manifest.enum_error(
                col, f"collection {res.kind} {res.error}".strip(), "help"
            )
            continue
        for x in BeautifulSoup(res.body, "html.parser").find_all("a", href=True):
            h = urljoin(HELP_BASE, x["href"])
            if "/articles/" in h:
                arts.add(h.split("?")[0])
            elif "/collections/" in h and h not in seen:
                queue.append(h)
    print(f"help articles: {len(arts)} (collections {len(seen)})", flush=True)
    run_surface(
        "help", "help", arts, a.out, a.concurrency, a.force, a.limit, policy, manifest
    )


def model_spec(a, policy, manifest):
    print("model-spec.openai.com...", flush=True)
    root = policy.run(raw, MODELSPEC)
    if root.status != 200 or root.error:
        manifest.enum_error(
            MODELSPEC, f"{root.kind} {root.error}".strip(), "model-spec"
        )
        return
    # 루트는 meta refresh로 날짜별 .html을 가리킨다 (예: content="0; url=2025-12-18.html")
    m = re.search(r'url=([^"\'\s>]+\.html)', root.body) or re.search(
        r'href=["\']?([^"\'\s>]+\.html)', root.body
    )
    target = urljoin(MODELSPEC, m.group(1)) if m else MODELSPEC
    run_surface(
        "model-spec", "model-spec", {target}, a.out, 1, a.force, 0, policy, manifest
    )


def self_test():
    assert model_urls(
        '<a href="/api/docs/models/gpt-5">x</a><a href="/api/docs/guides/x">no</a>'
    ) == {"https://developers.openai.com/api/docs/models/gpt-5"}
    assert (
        replace_origin("http://localhost:4321/gpt-5/system-card/", DEPLOYMENT_BASE)
        == "https://deploymentsafety.openai.com/gpt-5/system-card/"
    )
    assert deployment_pages(
        {
            "https://deploymentsafety.openai.com/gpt-5/",
            "https://deploymentsafety.openai.com/gpt-5/agent-evaluations/",
        }
    ) == {DEPLOYMENT_BASE + "/", DEPLOYMENT_BASE + "/gpt-5/"}
    assert (
        soft_redirect_target(
            "https://developers.openai.com/resources/agents/",
            "[Redirecting from `/resources/agents/` to `/learn/agents`](/learn/agents)",
        )
        == "https://developers.openai.com/learn/agents"
    )
    import tempfile

    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, DEPLOYMENT_BASE.split("//")[1], "old"))
    keep = os.path.join(d, "deploymentsafety.openai.com", "gpt-5.md")
    old = os.path.join(d, "deploymentsafety.openai.com", "old", "x.md")
    for fp in (keep, old):
        open(fp, "w").write("x")
    assert (
        prune_host(
            d, "deploymentsafety.openai.com", {DEPLOYMENT_BASE + "/gpt-5/"}, False
        )
        == 1
    )
    assert os.path.exists(old)
    assert reference_ancestors({"https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/methods/list/"}) == {
        "https://developers.openai.com/api/reference/go/resources/beta/",
        "https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/",
        "https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/methods/list/",
    }
    assert reference_links('<a href="/api/reference/go/resources/x/">a</a><a href="/api/reference/go/__sdk_schema?d=1">b</a>',
                           DEV_REFERENCE) == {"https://developers.openai.com/api/reference/go/resources/x/"}
    ms.self_test()


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument(
        "--only",
        default="developers,help,model-spec,learn,deployment-safety,trust",
        help="대상 csv",
    )
    ap.add_argument("--force", action="store_true")
    ap.add_argument(
        "--prune-stale",
        action="store_true",
        help="현재 열거에서 제외된 deploymentsafety 구 생성물 삭제(지정하지 않으면 후보 목록만 출력)",
    )
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=8)
    ap.add_argument("--verify-stale", action="store_true",
                    help="발견 집합 밖 기존 생성물의 원본을 확인해 moved/gone/live로 manifest에 기록(삭제하지 않음)")
    ms.add_retry_args(ap)
    a = ap.parse_args()
    RUN["verify_stale"] = a.verify_stale
    RUN["state_dir"] = a.state_dir or os.path.join(a.out, ms.STATE_DIR)
    only = set(s.strip() for s in a.only.split(",") if s.strip())
    policy = ms.policy_from(a)
    manifest = ms.Manifest(a.out, "docs", sys.argv[1:], a.state_dir)

    if "developers" in only:
        developers(a, policy, manifest)
    if "help" in only:
        help_center(a, policy, manifest)
    if "model-spec" in only:
        model_spec(a, policy, manifest)
    if "learn" in only:
        print("learn.chatgpt.com sitemap...", flush=True)
        run_surface(
            "learn.chatgpt.com",
            "learn",
            sitemap_urls(LEARN_SITEMAP, policy, manifest, "learn"),
            a.out,
            a.concurrency,
            a.force,
            a.limit,
            policy,
            manifest,
        )
    if "deployment-safety" in only:
        print("deploymentsafety.openai.com sitemap...", flush=True)
        pages = deployment_pages(
            sitemap_urls(
                DEPLOYMENT_SITEMAP,
                policy,
                manifest,
                "deployment-safety",
                DEPLOYMENT_BASE,
            )
        )
        run_surface(
            "deploymentsafety.openai.com",
            "deployment-safety",
            pages,
            a.out,
            a.concurrency,
            a.force,
            a.limit,
            policy,
            manifest,
        )
        if not a.limit:
            n = prune_host(a.out, "deploymentsafety.openai.com", pages, a.prune_stale)
            print(
                f"deploymentsafety.openai.com 구 생성물 {'정리' if a.prune_stale else '후보'}: {n}",
                flush=True,
            )
    if "trust" in only:
        run_surface(
            "trust.openai.com", "trust", {TRUST}, a.out, 1, a.force, 0, policy, manifest
        )
    unresolved = manifest.report()
    print(f"manifest: {manifest.write()}", flush=True)
    if unresolved:
        raise SystemExit(
            f"docs unresolved {unresolved}개: 재시도 소진, 열거 실패 또는 확정되지 않은 404"
        )


if __name__ == "__main__":
    main()
