"""OpenAI Academy(academy.openai.com) 전체 추출 — 로그인 불필요.

academy.openai.com은 curl_cffi(impersonate=chrome)로 CF·게이팅 없이 /public/ 콘텐츠가 받힌다.
- 텍스트(blogs/resources/collections/events/podcasts): <main>/body -> markdown.
- 영상(videos): 페이지 HTML의 vimeo id -> player config -> 자동생성 자막 .vtt -> 전사 markdown.
  (영상 페이지 UI는 'Sign in to continue'로 게이팅되지만 vimeo id는 HTML에 있고 vimeo config는 공개라 자막을 받는다.)

URL은 academy sitemap(인덱스 + 자식 + 일부 중첩)에서 수집. 출력 <out>/academy.openai.com/<path>.md (증분).
crawl-mirror.save/dest/find_boilerplate 재사용.

실행: python3 academy-extract.py <out_dir> [--include videos,blogs,resources] [--exclude events] [--force] [--limit N] [--concurrency N]
"""
import argparse, importlib.util, os, re
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlsplit
from curl_cffi import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

CM_PATH = os.environ.get(
    "CRAWL_MIRROR_PATH",
    os.path.expanduser("~/.agents/skills/shared/crawl/scripts/crawl-mirror.py"),
)
if not os.path.isfile(CM_PATH):
    raise SystemExit(f"crawl skill dependency not found: {CM_PATH}")
SITEMAP = "https://academy.openai.com/sitemap.xml"
REFERER = "https://academy.openai.com/"
IMPERSONATE = "chrome"

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)


def get(url, **kw):
    return requests.get(url, impersonate=IMPERSONATE, timeout=40, **kw)


def sitemap_urls():
    """인덱스 -> 자식 sitemap -> URL. loc이 또 sitemap.xml이면 한 번 더 펼친다."""
    seen, urls = set(), set()

    def expand(sm):
        if sm in seen:
            return
        seen.add(sm)
        try:
            locs = re.findall(r"<loc>(.*?)</loc>", get(sm).text)
        except Exception as e:
            print(f"  sitemap ERR {sm}: {e}", flush=True); return
        for l in locs:
            if l.endswith("sitemap.xml"):
                expand(l)
            else:
                urls.add(l)

    expand(SITEMAP)
    return urls


def seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return parts[1] if len(parts) >= 2 and parts[0] == "public" else (parts[0] if parts else "")


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


def vtt_to_text(vtt):
    out = []
    for ln in vtt.splitlines():
        ln = ln.strip()
        if not ln or ln == "WEBVTT" or "-->" in ln or ln.isdigit():
            continue
        ln = re.sub(r"<[^>]+>", "", ln)
        if not out or out[-1] != ln:
            out.append(ln)
    return " ".join(out)


def video_md(url, html):
    """영상 페이지 -> vimeo 자막 전사 markdown."""
    ids = list(dict.fromkeys(re.findall(r"(?:vimeo\.com/(?:video/)?|player\.vimeo\.com/video/)(\d+)", html)))
    if not ids:
        return ""
    for vid in ids:
        try:
            cfg = get(f"https://player.vimeo.com/video/{vid}/config", headers={"Referer": REFERER}).json()
        except Exception:
            continue
        title = cfg.get("video", {}).get("title") or url.rstrip("/").split("/")[-1]
        tracks = cfg.get("request", {}).get("text_tracks") or []
        en = next((t for t in tracks if t["lang"].startswith("en")), tracks[0] if tracks else None)
        if not en:
            continue
        try:
            txt = vtt_to_text(get("https://player.vimeo.com" + en["url"] if en["url"].startswith("/") else en["url"]).text)
        except Exception:
            continue
        if len(txt) < 100:
            continue
        return f"# {title}\n\n<!-- vimeo: {vid} | track: {en.get('label')} -->\n\n{txt}"
    return ""


def fetch_one(url):
    # 영상 여부를 URL 경로(`/public/videos/`)로만 가르면 club 영상(`/public/clubs/*/videos/*`)·
    # event replay·resource 링크 영상이 텍스트로 새 자막을 잃는다. HTML에 vimeo 링크가 있으면 전사한다.
    try:
        r = get(url)
        if r.status_code != 200:
            return url, "", f"status={r.status_code}"
        is_video_path = "/videos/" in url  # /public/videos/* 와 /public/clubs/*/videos/* 모두
        has_vimeo = bool(re.search(r"vimeo\.com/(?:video/)?\d+", r.text))
        if is_video_path or has_vimeo:
            v = video_md(url, r.text)  # spartan: 페이지에 vimeo 여럿이면 첫 영상만 전사
            if v:
                if not is_video_path:  # events/resources 하이브리드: 텍스트 본문 + 영상 자막
                    body = html_to_md(r.text)
                    if body and len(body) >= 150:
                        return url, f"{body}\n\n{v}", "ok"
                return url, v, "ok"
            # vimeo id 없음/자막 없음/게이팅 -> 텍스트 폴백
        return url, html_to_md(r.text), "thin"
    except Exception as e:
        return url, "", str(e)[:80]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--include", default="", help="포함 유형 csv (videos,blogs,resources,collections,events,podcasts)")
    ap.add_argument("--exclude", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=6)
    a = ap.parse_args()
    inc = set(s for s in a.include.split(",") if s)
    exc = set(s for s in a.exclude.split(",") if s)

    print("academy sitemap 수집 중...", flush=True)
    urls = sitemap_urls()
    if inc:
        urls = {u for u in urls if seg(u) in inc}
    if exc:
        urls = {u for u in urls if seg(u) not in exc}
    if not a.force:
        urls = {u for u in urls if not os.path.exists(cm.dest(a.out, u)[0])}
    urls = sorted(urls)
    if a.limit:
        urls = urls[:a.limit]
    print(f"추출 대상: {len(urls)} (concurrency={a.concurrency})", flush=True)
    if not urls:
        print("대상 없음.", flush=True); return

    pages, fails, done = {}, [], 0
    with ThreadPoolExecutor(max_workers=a.concurrency) as ex:
        futs = {ex.submit(fetch_one, u): u for u in urls}
        for f in as_completed(futs):
            url, body, err = f.result()
            done += 1
            if body and len(body) >= 150:
                pages[url] = body
            else:
                fails.append((url, err))
            if done % 25 == 0:
                print(f"  {done}/{len(urls)} (성공 {len(pages)}, 실패 {len(fails)})", flush=True)

    # boilerplate 제거: 순수 영상 전사만 제외(공통 라인 없음). 하이브리드(텍스트+자막)는 포함해 nav를 제거하되,
    # 자막 라인은 고유라 strip_boilerplate에서 살아남는다. 순수 영상 = vimeo 마커 앞 텍스트가 제목뿐(짧음).
    def pure_video(m):
        return "<!-- vimeo:" in m and len(m.split("<!-- vimeo:", 1)[0]) < 200
    text_pages = {u: m for u, m in pages.items() if not pure_video(m)}
    if len(text_pages) >= 5:
        boiler = cm.find_boilerplate(list(text_pages.values()), 0.4)
        if boiler:
            for u in text_pages:
                pages[u] = cm.strip_boilerplate(pages[u], boiler)
            print(f"boilerplate: {len(boiler)} lines removed", flush=True)
    for u, m in pages.items():
        cm.save(a.out, u, m, False)
    print(f"저장: {len(pages)} / 실패: {len(fails)}", flush=True)
    if fails:
        for u, err in fails[:20]:
            print(f"  {u} [{err}]", flush=True)


if __name__ == "__main__":
    main()
