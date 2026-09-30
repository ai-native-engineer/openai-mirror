#!/usr/bin/env python3
"""OpenAI 미러의 Git 변경분을 발행 전에 검증한다.

실행: python3 verify-publish.py <repo> [--staged] [--allow-deletes]
기본은 unstaged/untracked 변경, --staged는 index를 검사한다. 문제 없으면 exit 0.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mirror_state  # noqa: E402


ALLOWED_ROOTS = {
    "academy.openai.com",
    "alignment.openai.com",
    "cdn.openai.com",
    "d2xo500swnpgl1.cloudfront.net",
    "developers.openai.com",
    "deploymentsafety.openai.com",
    "downloads.ctfassets.net",
    "files.oaiusercontent.com",
    "help.openai.com",
    "learn.chatgpt.com",
    "model-spec.openai.com",
    "openai.com",
    "openai.fund",
    "openaifoundation.org",
    "openaiassets.blob.core.windows.net",
    "progress.openai.com",
    "spinningup.openai.com",
    "devday.openai.com",
    "trust.openai.com",
    "youtube.com",
}
MAX_FILE_BYTES = 100 * 1024 * 1024  # GitHub 단일 파일 제한을 넘기지 않는 발행 게이트.


def git(repo, *args):
    return subprocess.run(
        ["git", "-C", repo, *args], check=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, text=True,
    ).stdout


def worktree_changes(repo):
    # -z를 쓴다. 기본 출력은 공백·비ASCII 경로를 따옴표로 감싸 경로가 실제 파일과 어긋난다.
    out = git(repo, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    fields = out.split("\0")
    changes = []
    i = 0
    while i < len(fields):
        entry = fields[i]
        i += 1
        if len(entry) < 4:
            continue
        status = entry[:2]
        changes.append((status, entry[3:]))
        if "R" in status or "C" in status:
            i += 1  # rename/copy는 원본 경로를 다음 필드로 흘린다.
    return changes


def staged_changes(repo):
    fields = git(repo, "diff", "--cached", "--name-status", "-z").split("\0")
    changes = []
    i = 0
    while i + 1 < len(fields) and fields[i]:
        status = fields[i]
        if status[0] in ("R", "C") and i + 2 < len(fields):
            changes.append((status, fields[i + 2]))  # 대상 경로가 원본 다음에 온다.
            i += 3
        else:
            changes.append((status, fields[i + 1]))
            i += 2
    return changes


ACADEMY_VIDEO = re.compile(r"^academy\.openai\.com/public/(?:.+/)?videos/[^/]+\.md$")
VIDEO_MARKER = re.compile(r"<!--\s*(?:vimeo|youtube):\s*[\w-]+")


def content_issues(path, data):
    """파일 내용 공통 검사: 빈 파일, UTF-8, Academy 영상 provenance."""
    if not data.strip():
        return [f"빈 파일: {path}"]
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        return [f"UTF-8 아님: {path} (byte {e.start})"]
    if ACADEMY_VIDEO.match(path) and not VIDEO_MARKER.search(text):
        return [f"Academy 영상 provenance(vimeo/youtube 마커) 누락: {path}"]
    return []


def validate_change(repo, status, path, allow_deletes=False, strict_paths=False):
    issues = []
    root = path.split("/", 1)[0]
    if "/" not in path and root.endswith(".md"):
        root = root.removesuffix(".md")
    if root not in ALLOWED_ROOTS:
        return [f"예상 도메인 밖 변경: {path}"] if strict_paths else []
    if status.startswith(("R", "C")) or "R" in status or "C" in status:
        return [f"rename/copy는 증분 발행 범위 밖: {path}"]
    if "D" in status:
        return [] if allow_deletes else [f"증분 발행에서 삭제 감지: {path}"]

    fp = os.path.join(repo, path)
    if not os.path.isfile(fp):
        return [f"파일을 찾을 수 없음: {path}"]
    if os.path.getsize(fp) > MAX_FILE_BYTES:
        issues.append(f"100MB 초과: {path}")

    if path.endswith(".pdf"):
        with open(fp, "rb") as f:
            if f.read(5) != b"%PDF-":
                issues.append(f"PDF 매직바이트 불일치: {path}")
    elif path.endswith(".md"):
        with open(fp, "rb") as f:
            data = f.read()
        issues.extend(content_issues(path, data))
        first = data.decode("utf-8", errors="replace").split("\n", 1)[0]
        if path == "youtube.com/openai.md":
            if not first.startswith("# openai"):
                issues.append(f"YouTube 인덱스 헤더 불일치: {path}")
        elif path.startswith("youtube.com/openai/"):
            if first != "---":
                issues.append(f"YouTube frontmatter 누락: {path}")
        elif root == "youtube.com":
            issues.append(f"예상하지 않은 YouTube 발행 경로: {path}")
        elif not first.startswith("<!-- source: https://"):
            issues.append(f"source 헤더 누락: {path}")
    else:
        issues.append(f"지원하지 않는 생성물 확장자: {path}")
    return issues


def validate(repo, changes, allow_deletes=False, strict_paths=False):
    issues = []
    for status, path in changes:
        issues.extend(validate_change(repo, status, path, allow_deletes, strict_paths))
    return issues


def _generated_markdown(repo):
    paths = []
    for name in os.listdir(repo):
        fp = os.path.join(repo, name)
        if os.path.isfile(fp) and name.endswith('.md') and name[:-3] in ALLOWED_ROOTS:
            paths.append(os.path.relpath(fp, repo))
    for root in ALLOWED_ROOTS:
        base = os.path.join(repo, root)
        if not os.path.isdir(base):
            continue
        for current, _, files in os.walk(base):
            paths.extend(os.path.join(root, os.path.relpath(os.path.join(current, f), base)) for f in files if f.endswith('.md'))
    return sorted(paths)


def tree_audit(repo):
    """Audit existing generated output, not only the current Git diff."""
    issues, warnings = [], []
    markdown = _generated_markdown(repo)
    thin = 0
    thin_paths = []
    youtube_pages = set()
    for path in markdown:
        fp = os.path.join(repo, path)
        with open(fp, 'rb') as f:
            data = f.read()
        issues.extend(content_issues(path, data))
        text = data.decode('utf-8', errors='replace')
        lines = text.splitlines()
        first = lines[0] if lines else ''
        if path == 'youtube.com/openai.md':
            if not first.startswith('# openai'):
                issues.append(f'YouTube 인덱스 헤더 불일치: {path}')
            continue
        if path.startswith('youtube.com/openai/'):
            youtube_pages.add(path.removeprefix('youtube.com/'))
            if first != '---':
                issues.append(f'YouTube frontmatter 누락: {path}')
            else:
                header = text.split('\n---', 1)[0]
                required = {'title:', 'channel:', 'url:', 'youtube_id:', 'published:', 'captions:'}
                missing = sorted(k for k in required if k not in header)
                if missing:
                    issues.append(f'YouTube frontmatter 필드 누락: {path} ({", ".join(missing)})')
            continue
        if not first.startswith('<!-- source: https://'):
            issues.append(f'source 헤더 누락: {path}')
        body = '\n'.join(lines[1:]).strip()
        if len(body) < 20:
            thin += 1
            thin_paths.append(path)

    index_fp = os.path.join(repo, 'youtube.com', 'openai.md')
    if os.path.isfile(index_fp):
        index = open(index_fp, encoding='utf-8', errors='replace').read()
        indexed = set(re.findall(r'\]\((openai/[^)]+\.md)\)', index))
        missing_targets = sorted(indexed - youtube_pages)
        stale = sorted(youtube_pages - indexed)
        for path in missing_targets:
            issues.append(f'YouTube 인덱스 대상 파일 없음: youtube.com/{path}')
        if stale:
            warnings.append(f'YouTube 색인에 없는 보존 파일 {len(stale)}개: --prune-stale 검토 필요')
    elif youtube_pages:
        issues.append('YouTube 인덱스 파일 없음: youtube.com/openai.md')

    pdfs = []
    for root in ALLOWED_ROOTS | {'_pdf-cache'}:
        base = os.path.join(repo, root)
        if not os.path.isdir(base):
            continue
        for current, _, files in os.walk(base):
            pdfs.extend(os.path.join(current, f) for f in files if f.endswith('.pdf'))
    for fp in pdfs:
        rel = os.path.relpath(fp, repo)
        with open(fp, 'rb') as f:
            if f.read(5) != b'%PDF-':
                issues.append(f'PDF 매직바이트 불일치: {rel}')
        if not rel.startswith('_pdf-cache' + os.sep) and os.path.getsize(fp) > MAX_FILE_BYTES:
            issues.append(f'100MB 초과: {rel}')
    if thin:
        warnings.append(f'본문이 매우 짧은 생성 문서 {thin}개: thin/client-only 여부 확인 필요')
        warnings.extend(f'  thin: {p}' for p in thin_paths[:20])
    return issues, warnings, {'markdown': len(markdown), 'pdf': len(pdfs), 'thin': thin}


def parsing_self_test():
    root = tempfile.mkdtemp()
    git(root, "init", "-q")
    spaced = "openai.com/index/with space.md"
    os.makedirs(os.path.join(root, "openai.com/index"), exist_ok=True)
    with open(os.path.join(root, spaced), "w") as f:
        f.write("<!-- source: https://openai.com/index/x/ -->\n")
    assert spaced in {p for _, p in worktree_changes(root)}
    git(root, "add", "-A")
    assert spaced in {p for _, p in staged_changes(root)}


def self_test():
    root = tempfile.mkdtemp()
    files = {
        "openai.com/index/x.md": "<!-- source: https://openai.com/index/x/ -->\n",
        "trust.openai.com.md": "<!-- source: https://trust.openai.com/ -->\n",
        "youtube.com/openai.md": "# openai (YouTube)\n",
        "youtube.com/openai/x.md": "---\ntitle: x\n---\n",
        "cdn.openai.com/x.pdf": "%PDF-test",
    }
    for path, body in files.items():
        fp = os.path.join(root, path)
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        mode = "wb" if path.endswith(".pdf") else "w"
        with open(fp, mode) as f:
            f.write(body.encode() if mode == "wb" else body)
    assert not validate(root, [("??", p) for p in files])
    assert not validate_change(root, "??", "README.md")
    assert validate_change(root, "??", "README.md", strict_paths=True)
    assert not validate_change(root, "D ", "README.md")
    assert validate_change(root, "D ", "README.md", strict_paths=True)
    assert validate_change(root, "D ", "openai.com/index/x.md")
    assert not validate_change(root, "D ", "openai.com/index/x.md", allow_deletes=True)
    parsing_self_test()
    audit = tempfile.mkdtemp()
    os.makedirs(os.path.join(audit, 'openai.com', 'index'), exist_ok=True)
    os.makedirs(os.path.join(audit, 'youtube.com', 'openai'), exist_ok=True)
    with open(os.path.join(audit, 'openai.com', 'index', 'x.md'), 'w') as f:
        f.write('<!-- source: https://openai.com/index/x/ -->\n\nLong enough body for the tree audit.\n')
    with open(os.path.join(audit, 'youtube.com', 'openai.md'), 'w') as f:
        f.write('# openai (YouTube)\n\n- [x](openai/x.md)\n')
    with open(os.path.join(audit, 'youtube.com', 'openai', 'x.md'), 'w') as f:
        f.write('---\ntitle: x\nchannel: openai\nurl: https://www.youtube.com/watch?v=x\nyoutube_id: x\npublished: 2026-01-01\ncaptions: none\n---\n\n# x\n\nLong enough body for the tree audit.\n')
    issues, warnings, stats = tree_audit(audit)
    assert not issues and stats['markdown'] == 3 and not warnings
    assert content_issues("academy.openai.com/public/videos/x.md", b"<!-- source: https://a/ -->\n\ntext")
    assert not content_issues("academy.openai.com/public/videos/x.md", b"<!-- source: https://a/ -->\n<!-- vimeo: 123 | track: none -->")
    assert not content_issues("academy.openai.com/public/clubs/c/videos/x.md", b"<!-- youtube: abcDEF12345 | track: none -->")
    assert content_issues("openai.com/x.md", b"\xff\xfe")[0].startswith("UTF-8")
    assert content_issues("openai.com/x.md", b"")[0].startswith("빈 파일")
    _, problems = mirror_state.coverage(audit)
    assert problems  # manifest가 없으면 coverage 완결로 보지 않는다.
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--staged", action="store_true", help="worktree 대신 Git index 검사")
    ap.add_argument("--allow-deletes", action="store_true", help="전량 재생성처럼 의도된 삭제 허용")
    ap.add_argument("--tree-audit", action="store_true",
                    help="기존 생성물 전체와 _mirror-state 기반 URL coverage를 감사")
    ap.add_argument("--skip-coverage", action="store_true",
                    help="--tree-audit에서 coverage 판정을 생략(파일 형식만 검사, 완료 판정에 쓰지 않음)")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
    if a.tree_audit:
        issues, warnings, stats = tree_audit(repo)
        print(f"아카이브 전체 감사: Markdown {stats['markdown']}개 / PDF {stats['pdf']}개 / thin {stats['thin']}개 / 문제 {len(issues)}개")
        for warning in warnings[:30]:
            print(f"  경고: {warning}")
        for issue in issues[:30]:
            print(f"  문제: {issue}")
        if a.skip_coverage:
            return 1 if issues else 0
        rows, problems = mirror_state.coverage(repo)
        mirror_state.print_coverage(rows, problems)
        return 1 if issues or problems else 0
    try:
        changes = staged_changes(repo) if a.staged else worktree_changes(repo)
    except subprocess.CalledProcessError as e:
        print(e.stderr.strip() or "Git 변경분을 읽지 못했습니다.", file=sys.stderr)
        return 2
    issues = validate(repo, changes, a.allow_deletes, strict_paths=a.staged)
    print(f"Git 변경 {len(changes)}개 검사: 문제 {len(issues)}개")
    for issue in issues[:30]:
        print(f"  {issue}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
