"""OpenAI Academy(academy.openai.com) 전체 추출 — 로그인 불필요.

academy.openai.com은 curl_cffi(impersonate=chrome)로 CF·게이팅 없이 /public/ 콘텐츠가 받힌다.
- 텍스트(blogs/resources/collections/events/podcasts): <main>/body -> markdown.
- 영상(videos): 페이지 HTML의 vimeo id -> player config -> 자동생성 자막 .vtt -> 전사 markdown.
  (영상 페이지 UI는 'Sign in to continue'로 게이팅되지만 vimeo id는 HTML에 있고 vimeo config는 공개라 자막을 받는다.)
  자막이 없는 영상도 `<!-- vimeo: ID | track: none -->` 마커로 provenance를 남긴다.

URL은 academy sitemap(인덱스 + 자식 + 일부 중첩)에서 수집. 출력 <out>/academy.openai.com/<path>.md (증분).
crawl-mirror.save/dest/find_boilerplate 재사용. 실행 결과는 <out>/_mirror-state/ manifest에 남는다.

실행: python3 academy-extract.py <out_dir> [--include videos,blogs,resources] [--exclude events] [--force]
      [--limit N] [--concurrency N] [--urls FILE] [--retry-unresolved] [--retries N] [--retry-backoff S]
"""

import argparse, importlib.util, os, re, sys
from urllib.parse import urlsplit
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
SITEMAP = "https://academy.openai.com/sitemap.xml"
REFERER = "https://academy.openai.com/"
IMPERSONATE = "chrome"
MIN_LEN = 150
# player/video, manage/videos, progressive_redirect/playback, <user>/download 형식을 모두 잡는다(8/2026 이후 페이지는 뒤쪽 형식).
VIMEO_RE = re.compile(
    r"vimeo\.com/(?:video/|manage/videos/|progressive_redirect/playback/|[\w-]+/download/)?(\d{6,})"
)
YOUTUBE_RE = re.compile(r"(?:youtu\.be/|youtube(?:-nocookie)?\.com/(?:watch\?v=|embed/|live/|shorts/))([A-Za-z0-9_-]{11})")

spec = importlib.util.spec_from_file_location("cm", CM_PATH)
cm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cm)


class TransientError(RuntimeError):
    """Vimeo 429/5xx 같은 일시 오류. fetch 전체를 재시도하게 흘린다."""


def get(url, **kw):
    return requests.get(url, impersonate=IMPERSONATE, timeout=40, **kw)


def sitemap_urls(policy, manifest):
    """인덱스 -> 자식 sitemap -> URL. loc이 또 sitemap.xml이면 한 번 더 펼친다. 실패한 sitemap은 열거 오류로 남긴다."""
    seen, urls = set(), set()

    def fetch(sm):
        r = get(sm)
        return ms.Result(
            sm,
            body=r.text,
            status=r.status_code,
            retry_after=ms.parse_retry_after(r.headers.get("retry-after")),
        )

    def expand(sm):
        if sm in seen:
            return
        seen.add(sm)
        res = policy.run(fetch, sm)
        if res.status != 200 or res.error:
            print(f"  sitemap ERR {sm}: {res.kind} {res.error}", flush=True)
            manifest.enum_error(sm, f"{res.kind} {res.error}".strip(), "academy")
            return
        for l in re.findall(r"<loc>(.*?)</loc>", res.body):
            if l.endswith("sitemap.xml"):
                expand(l)
            else:
                urls.add(l)

    expand(SITEMAP)
    return urls


def existing_video_urls(out):
    """Keep previously discovered club videos in the incremental discovery set."""
    base = os.path.join(out, "academy.openai.com")
    urls = set()
    if not os.path.isdir(base):
        return urls
    for current, _, files in os.walk(base):
        for name in files:
            if not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(current, name), base).replace(
                os.sep, "/"
            )
            if rel.startswith("public/") and "/videos/" in rel:
                urls.add("https://academy.openai.com/" + rel[:-3])
    return urls


def seg(url):
    parts = [x for x in urlsplit(url).path.split("/") if x]
    return (
        parts[1]
        if len(parts) >= 2 and parts[0] == "public"
        else (parts[0] if parts else "")
    )


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


def _vimeo_get(url):
    r = get(url, headers={"Referer": REFERER})
    if r.status_code == 429 or r.status_code >= 500:
        raise TransientError(f"vimeo status={r.status_code} {url}")
    return r


def video_md(url, html):
    """영상 페이지 -> (markdown, 전사 여부). 자막이 없으면 provenance 마커만 돌려준다."""
    ids = list(dict.fromkeys(VIMEO_RE.findall(html)))
    first = None
    for vid in ids:
        r = _vimeo_get(f"https://player.vimeo.com/video/{vid}/config")
        if r.status_code != 200:
            continue  # 비공개/삭제 영상
        cfg = r.json()
        title = cfg.get("video", {}).get("title") or url.rstrip("/").split("/")[-1]
        first = first or (vid, title)
        tracks = cfg.get("request", {}).get("text_tracks") or []
        en = next(
            (t for t in tracks if t["lang"].startswith("en")),
            tracks[0] if tracks else None,
        )
        if not en:
            continue
        track = _vimeo_get(
            "https://player.vimeo.com" + en["url"]
            if en["url"].startswith("/")
            else en["url"]
        )
        txt = vtt_to_text(track.text) if track.status_code == 200 else ""
        if len(txt) < 100:
            continue
        return (
            f"# {title}\n\n<!-- vimeo: {vid} | track: {en.get('label')} -->\n\n{txt}",
            True,
        )
    if ids:  # 자막이 없거나 config가 비공개여도 HTML의 Vimeo ID로 provenance를 남긴다.
        vid = first[0] if first else ids[0]
        return (
            f"<!-- vimeo: {vid} | track: none -->\n\n[▶ Watch on Vimeo](https://vimeo.com/{vid})",
            False,
        )
    yt = list(dict.fromkeys(YOUTUBE_RE.findall(html)))
    if yt:  # YouTube 호스팅 Academy 영상. 자막은 inline-transcripts.py가 _yt-cache에서 붙인다.
        return (
            f"<!-- youtube: {yt[0]} | track: none -->\n\nhttps://www.youtube.com/watch?v={yt[0]}",
            False,
        )
    return "", False


def raw(url):
    r = get(url)
    res = ms.Result(url, body=r.text, status=r.status_code,
                    retry_after=ms.parse_retry_after(r.headers.get("retry-after")))
    res.final_url = r.url
    return res


def fetch_one(url):
    # 영상 여부를 URL 경로(`/public/videos/`)로만 가르면 club 영상(`/public/clubs/*/videos/*`)·
    # event replay·resource 링크 영상이 텍스트로 새 자막을 잃는다. HTML에 vimeo 링크가 있으면 전사한다.
    r = get(url)
    res = ms.Result(
        url,
        status=r.status_code,
        retry_after=ms.parse_retry_after(r.headers.get("retry-after")),
        canonical=ms.canonical_of(r.text) if r.status_code != 200 else "",
    )
    if r.status_code != 200:
        return res
    is_video_path = (
        "/videos/" in url
    )  # /public/videos/* 와 /public/clubs/*/videos/* 모두
    if is_video_path or VIMEO_RE.search(r.text):  # YouTube 링크만 있는 글은 영상 페이지로 보지 않는다.
        v, transcribed = video_md(
            url, r.text
        )  # spartan: 페이지에 vimeo 여럿이면 첫 영상만 전사
        if transcribed:
            if (
                not is_video_path
            ):  # events/resources 하이브리드: 텍스트 본문 + 영상 자막
                body = html_to_md(r.text)
                if body and len(body) >= MIN_LEN:
                    res.body = f"{body}\n\n{v}"
                    return res
            res.body = v
            return res
        if v:  # 자막 없는 영상: 텍스트 본문 + provenance 마커
            body = html_to_md(r.text)
            res.body = f"{body}\n\n{v}" if len(body) >= MIN_LEN else ""
            res.thin_reason = "" if res.body else f"자막 없는 영상, 본문 {len(body)}자"
            return res
        if is_video_path:
            res.thin_reason = "영상 경로지만 Vimeo/YouTube id 없음"
            return res
    res.body = html_to_md(r.text)
    return res


def read_urls(fp):
    with open(fp, encoding="utf-8") as f:
        return {ln.strip() for ln in f if ln.strip() and not ln.startswith("#")}


def self_test():
    # 8/2026 이후 Academy 페이지가 쓰는 Vimeo URL 형식을 모두 잡아야 provenance가 남는다.
    assert VIMEO_RE.findall(
        '"videoUrl":"https://vimeo.com/manage/videos/1109871723/cc15131a68" '
        "https://player.vimeo.com/progressive_redirect/playback/1185285074/rendition/1080p/file.mp4 "
        "https://vimeo.com/openai/download/1215584300/7387cc5953 https://player.vimeo.com/video/1226039347"
    ) == ["1109871723", "1185285074", "1215584300", "1226039347"]
    assert YOUTUBE_RE.findall('"videoUrl":"https://www.youtube.com/watch?v=gKyEzP_jhZc"') == ["gKyEzP_jhZc"]
    assert vtt_to_text("WEBVTT\n\n1\n00:00.000 --> 00:01.000\nhello\n\n2\n00:01.000 --> 00:02.000\nhello\nworld") == "hello world"
    ms.self_test()


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument(
        "--include",
        default="",
        help="포함 유형 csv (videos,blogs,resources,collections,events,podcasts)",
    )
    ap.add_argument("--exclude", default="")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument(
        "--urls",
        default="",
        help="이 파일의 URL만 다시 수집(기존 파일도 덮어씀, 부분 실행)",
    )
    ap.add_argument(
        "--retry-unresolved",
        action="store_true",
        help="직전 manifest에서 unresolved인 URL만 다시 수집(부분 실행)",
    )
    ap.add_argument("--verify-stale", action="store_true",
                    help="발견 집합 밖 기존 생성물의 원본을 확인해 moved/gone/live로 manifest에 기록(삭제하지 않음)")
    ms.add_retry_args(ap, retries=6, backoff=5.0, max_wait=120.0, min_interval=1.5)
    a = ap.parse_args()
    inc = set(s for s in a.include.split(",") if s)
    exc = set(s for s in a.exclude.split(",") if s)
    policy = ms.policy_from(a)
    manifest = ms.Manifest(a.out, "academy", sys.argv[1:], a.state_dir)
    state_dir = a.state_dir or os.path.join(a.out, ms.STATE_DIR)

    targeted = bool(a.urls or a.retry_unresolved)
    print("academy sitemap 수집 중...", flush=True)
    listed = sitemap_urls(policy, manifest)
    urls = set(listed) | ms.live_seeds(state_dir, "academy")
    if not inc or "videos" in inc:
        recovered = existing_video_urls(a.out) - urls
        if recovered:
            urls |= recovered
            print(f"기존 영상 링크 복구: +{len(recovered)}", flush=True)
    slugs = ms.slug_index(urls)
    if targeted:
        picked = read_urls(a.urls) if a.urls else set()
        if a.retry_unresolved:
            st = ms.load_surface(state_dir, "academy") or {}
            picked |= {
                u
                for u, r in st.get("urls", {}).items()
                if r["status"] in ("unresolved", "pending")
            }
        urls = picked
    else:
        if inc:
            urls = {
                u
                for u in urls
                if seg(u) in inc or ("videos" in inc and "/videos/" in urlsplit(u).path)
            }
        if exc:
            urls = {u for u in urls if seg(u) not in exc}
    manifest.discover(urls)
    known = set(urls)
    if not (targeted or a.force):
        have = {u for u in urls if os.path.exists(cm.dest(a.out, u)[0])}
        manifest.existing(have)
        urls -= have
    urls = sorted(urls)
    if a.limit:
        urls = urls[: a.limit]
    if not (inc or exc or a.limit or targeted):
        manifest.complete.add("academy")
    print(
        f"추출 대상: {len(urls)} (concurrency={a.concurrency}, retries={a.retries})",
        flush=True,
    )

    results = (
        ms.collect(urls, fetch_one, policy, a.concurrency, slugs, every=25)
        if urls
        else []
    )
    pages = ms.candidate_pages(results, MIN_LEN, listed)

    # boilerplate 제거: 순수 영상 전사만 제외(공통 라인 없음). 하이브리드(텍스트+자막)는 포함해 nav를 제거하되,
    # 자막 라인은 고유라 strip_boilerplate에서 살아남는다. 순수 영상 = vimeo 마커 앞 텍스트가 제목뿐(짧음).
    def pure_video(m):
        return "<!-- vimeo:" in m and len(m.split("<!-- vimeo:", 1)[0]) < 200

    text_pages = {u: m for u, m in pages.items() if not pure_video(m)}
    sample = list(text_pages.values())
    if text_pages and len(sample) < 20:
        # --urls 같은 소량 실행은 공통 nav를 판별할 표본이 모자란다. 저장하지 않는 표본 페이지로 보충한다.
        def page_text(u):
            r = get(u)
            return ms.Result(u, body=html_to_md(r.text) if r.status_code == 200 else "", status=r.status_code)

        for kind in (True, False):  # 영상 페이지와 일반 페이지의 chrome이 달라 양쪽에서 뽑는다.
            pool = sorted(u for u in listed if ("/videos/" in u) == kind and u not in text_pages)
            for u in pool[:: max(1, len(pool) // 8)][:8]:
                extra = policy.run(page_text, u)
                if extra.status == 200 and len(extra.body) >= MIN_LEN:
                    sample.append(extra.body)
    if len(sample) >= 5:
        boiler = cm.find_boilerplate(sample, 0.4)
        if boiler:
            for u in text_pages:
                pages[u] = cm.strip_boilerplate(pages[u], boiler)
            print(f"boilerplate: {len(boiler)} lines removed", flush=True)
    pages, dropped = ms.keep_pages(pages, MIN_LEN, cm.strip_chrome)
    for u, m in pages.items():
        cm.save(a.out, u, m, False)
    ms.record_results(manifest, results, pages, dropped, MIN_LEN)
    print(f"저장: {len(pages)} / 미저장: {len(results) - len(pages)}", flush=True)
    if a.verify_stale and "academy" in manifest.complete:
        ms.verify_stale(manifest, a.out, "academy", known, raw, policy, a.concurrency)
    unresolved = manifest.report()
    print(f"manifest: {manifest.write()}", flush=True)
    if unresolved:
        raise SystemExit(
            f"Academy unresolved {unresolved}개: 재시도 소진 또는 확정되지 않은 404"
        )


if __name__ == "__main__":
    main()
