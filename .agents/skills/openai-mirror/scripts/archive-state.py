#!/usr/bin/env python3
"""YouTube 색인과 OpenAI 소유 PDF의 coverage 상태를 _mirror-state manifest로 남긴다.

YouTube와 PDF는 shared crawl 스크립트가 생성하므로 수집기 manifest가 없다. 이 스크립트가 생성물을 기준으로
발견/저장/stale을 계산한다.

- youtube: `youtube.com/openai.md` 색인과 `youtube.com/openai/*.md` 파일을 양방향 비교한다.
  색인에 있는데 파일이 없으면 unresolved, 파일만 있으면 stale 후보다. stale은 기본적으로 목록만 출력하고
  `--prune-stale`을 명시했을 때만 삭제한다.
- pdf: 생성 Markdown이 링크한 허용 호스트 PDF(pdf-mirror.py와 같은 scan/dest 규칙)를 발견 집합으로 삼는다.
  미저장 PDF는 네트워크로 재확인해 404/410이 반복되면 gone, 그 밖의 실패는 unresolved로 남긴다.

실행: python3 archive-state.py <repo> [youtube|pdf|all] [--prune-stale] [--retries N] [--retry-backoff S]
"""

import argparse
import importlib.util
import os
import re
import sys
import urllib.error
import urllib.request
from urllib.parse import parse_qs, urlsplit
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mirror_state as ms  # noqa: E402

CRAWL_DIR = os.path.join(
    os.environ.get(
        "CRAWL_SKILL_DIR", os.path.expanduser("~/.agents/skills/shared/crawl")
    ),
    "scripts",
)
PDF_HOSTS = (
    "openai.com",
    "d2xo500swnpgl1.cloudfront.net",
    "openaiassets.blob.core.windows.net",
    "files.oaiusercontent.com",
    "downloads.ctfassets.net",
    "openaifoundation.org",
    "openai.fund",
)
CHANNEL = "openai"


def youtube_state(repo):
    """(index 항목 [(rel, 파일 존재)], stale 후보 [{path, youtube_id, reason}])."""
    pub = os.path.join(repo, "youtube.com")
    index_fp = os.path.join(pub, f"{CHANNEL}.md")
    ddir = os.path.join(pub, CHANNEL)
    files = (
        {f"{CHANNEL}/{n}" for n in os.listdir(ddir) if n.endswith(".md")}
        if os.path.isdir(ddir)
        else set()
    )
    index = open(index_fp, encoding="utf-8").read() if os.path.isfile(index_fp) else ""
    indexed = list(dict.fromkeys(re.findall(rf"\]\(({CHANNEL}/[^)]+\.md)\)", index)))

    def vid(rel):
        with open(os.path.join(pub, rel), encoding="utf-8", errors="replace") as f:
            m = re.search(r"^youtube_id:\s*(\S+)", f.read(1500), re.M)
        return m.group(1) if m else ""

    indexed_ids = {vid(r) for r in indexed if r in files}
    stale = []
    for rel in sorted(files - set(indexed)):
        i = vid(rel)
        reason = (
            "같은 youtube_id가 다른 파일명으로 색인됨(제목 변경)"
            if i in indexed_ids
            else "채널 열거(videos/shorts/streams)에 없음(비공개/unlisted/삭제 추정)"
        )
        stale.append({"path": f"youtube.com/{rel}", "youtube_id": i, "reason": reason})
    return [(r, r in files) for r in indexed], stale


def run_youtube(repo, state_dir, prune):
    entries, stale = youtube_state(repo)
    m = ms.Manifest(
        repo,
        "youtube-index",
        ["youtube"] + (["--prune-stale"] if prune else []),
        state_dir,
    )
    for rel, exists in entries:
        url = f"https://youtube.com/{rel}"  # 발행 파일 기준 식별자. 실제 영상 URL은 frontmatter url.
        if exists:
            m.mark(url, "existing")
        else:
            m.mark(url, "unresolved", note=f"색인 대상 파일 없음: youtube.com/{rel}")
    for rec in m.records.values():
        rec["surface"] = "youtube"
    m.complete.add("youtube")
    for s in stale:
        print(
            f"  {'삭제' if prune else 'stale 후보'}: {s['path']} ({s['youtube_id']}, {s['reason']})",
            flush=True,
        )
        if prune:
            os.unlink(os.path.join(repo, s["path"]))
    run_fp = write_run(
        m, {"stale": [] if prune else stale, "pruned": stale if prune else []}
    )
    print(
        f"youtube: 색인 {len(entries)} / 파일 있음 {sum(e for _, e in entries)} / "
        f"stale {len(stale)}{' (삭제함)' if prune else ''} -> {run_fp}",
        flush=True,
    )
    return sum(not e for _, e in entries)


def write_run(m, extra):
    """Manifest.write와 같은 자리에 쓰되 표면 상태에 stale 목록을 함께 넣는다."""
    run_fp = m.write()
    surface = next(iter(m.complete))
    st = ms.load_surface(m.state_dir, surface) or {}
    ms.merge_surface(
        m.state_dir,
        surface,
        m.collector,
        run_fp,
        list(st.get("urls", {}).values()),
        st.get("enumeration_errors", []),
        True,
        extra,
    )
    return run_fp


def load_pdf_mirror():
    fp = os.path.join(CRAWL_DIR, "pdf-mirror.py")
    if not os.path.isfile(fp):
        raise SystemExit(f"crawl skill dependency not found: {fp}")
    spec = importlib.util.spec_from_file_location("pdf_mirror", fp)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def expired_signature(url):
    se = parse_qs(urlsplit(url).query).get("se", [""])[0]
    try:
        return datetime.strptime(se, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        ) < datetime.now(timezone.utc)
    except ValueError:
        return False


def probe_pdf(url):
    req = urllib.request.Request(
        url, headers={"User-Agent": "Mozilla/5.0", "Range": "bytes=0-7"}
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            head = r.read(8)
            return ms.Result(
                url,
                body=head.decode("latin-1"),
                status=r.status if r.status != 206 else 200,
            )
    except urllib.error.HTTPError as e:
        return ms.Result(
            url,
            status=e.code,
            retry_after=ms.parse_retry_after(e.headers.get("retry-after")),
        )


def run_pdf(repo, state_dir, policy):
    pm = load_pdf_mirror()
    urls = pm.scan(repo, PDF_HOSTS)
    m = ms.Manifest(repo, "pdf", ["pdf"], state_dir)
    invalid = [u for u in urls if pm.invalid_source_url(u)]
    referenced = set()
    for u in urls:
        if u in invalid:
            continue
        fp, cache_fp = pm.dest(repo, u), pm.dest(os.path.join(repo, "_pdf-cache"), u)
        referenced.update({os.path.abspath(fp), os.path.abspath(cache_fp)})
        if os.path.exists(fp) or os.path.exists(cache_fp):
            m.mark(u, "existing")
            continue
        res = policy.run(probe_pdf, u)
        if res.status == 200 and res.body.startswith("%PDF-"):
            m.mark(
                u,
                "unresolved",
                http=200,
                attempts=res.attempts,
                note="원본은 PDF로 응답하지만 미저장: pdf-mirror 재실행 필요",
            )
        elif res.status == 200:
            m.mark(
                u,
                "gone",
                http=200,
                attempts=res.attempts,
                note="비-PDF 응답(업스트림 회수/홈 redirect)",
            )
        elif res.status in (404, 410):
            again = policy.run(probe_pdf, u)
            status = "gone" if again.status in (404, 410) else "unresolved"
            note = f"{res.status} 재확인 {again.status}" + (
                "; 만료된 서명 URL" if expired_signature(u) else ""
            )
            m.mark(
                u,
                status,
                http=res.status,
                attempts=res.attempts + again.attempts,
                note=note,
            )
        elif res.status in (401, 403, 409) and expired_signature(u):
            m.mark(
                u,
                "gone",
                http=res.status,
                attempts=res.attempts,
                note="만료된 서명 URL",
            )
        else:
            m.mark(
                u,
                "unresolved",
                http=res.status,
                error=res.error,
                attempts=res.attempts,
                retried=res.attempts > 1,
            )
    for rec in m.records.values():
        rec["surface"] = "pdf"
    m.complete.add("pdf")
    stale = []
    for host in set(PDF_HOSTS) | {"cdn.openai.com"}:
        for base, _, files in os.walk(os.path.join(repo, host)):
            stale.extend(
                os.path.relpath(os.path.join(base, n), repo)
                for n in files
                if n.endswith(".pdf")
                and os.path.abspath(os.path.join(base, n)) not in referenced
            )
    for p in sorted(stale):
        print(f"  stale 후보(링크하는 문서 없음): {p}", flush=True)
    run_fp = write_run(
        m, {"stale": [{"path": p} for p in sorted(stale)], "invalid_links": invalid}
    )
    unresolved = m.report()
    print(
        f"pdf: 링크 {len(urls)} (축약 URL 제외 {len(invalid)}) / stale {len(stale)} -> {run_fp}",
        flush=True,
    )
    return unresolved


def self_test():
    import tempfile

    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "youtube.com", "openai"))
    page = "---\ntitle: x\nyoutube_id: {}\n---\n"
    for name, vid in (
        ("a.md", "AAAAAAAAAAA"),
        ("a-old.md", "AAAAAAAAAAA"),
        ("gone.md", "BBBBBBBBBBB"),
    ):
        open(os.path.join(d, "youtube.com", "openai", name), "w").write(
            page.format(vid)
        )
    open(os.path.join(d, "youtube.com", "openai.md"), "w").write(
        "# openai (YouTube)\n\n- [a](openai/a.md)\n- [m](openai/missing.md)\n"
    )
    entries, stale = youtube_state(d)
    assert entries == [("openai/a.md", True), ("openai/missing.md", False)]
    assert [s["path"] for s in stale] == [
        "youtube.com/openai/a-old.md",
        "youtube.com/openai/gone.md",
    ]
    assert "제목 변경" in stale[0]["reason"] and "채널 열거" in stale[1]["reason"]
    assert run_youtube(d, "", False) == 1 and os.path.exists(
        os.path.join(d, "youtube.com", "openai", "gone.md")
    )
    rows, _ = ms.coverage(d)
    yt = next(r for r in rows if r["surface"] == "youtube")
    assert (yt["discovered"], yt["saved"], yt["unresolved"], yt["stale"]) == (
        2,
        1,
        1,
        2,
    ), yt
    assert expired_signature(
        "https://files.oaiusercontent.com/f?se=2024-03-11T20%3A29%3A52Z&sp=r"
    )
    assert not expired_signature("https://cdn.openai.com/a.pdf")
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument(
        "target", nargs="?", default="all", choices=["youtube", "pdf", "all"]
    )
    ap.add_argument(
        "--prune-stale",
        action="store_true",
        help="YouTube 색인에 없는 파일을 목록 출력 후 삭제",
    )
    ms.add_retry_args(ap)
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    state_dir = a.state_dir or os.path.join(repo, ms.STATE_DIR)
    bad = 0
    if a.target in ("youtube", "all"):
        bad += run_youtube(repo, state_dir, a.prune_stale)
    if a.target in ("pdf", "all"):
        bad += run_pdf(repo, state_dir, ms.policy_from(a))
    if bad:
        print(f"unresolved {bad}개", file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
