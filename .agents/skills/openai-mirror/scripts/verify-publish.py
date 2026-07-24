#!/usr/bin/env python3
"""OpenAI 미러의 Git 변경분을 발행 전에 검증한다.

실행: python3 verify-publish.py <repo> [--staged] [--allow-deletes]
기본은 unstaged/untracked 변경, --staged는 index를 검사한다. 문제 없으면 exit 0.
"""
import argparse
import os
import subprocess
import sys
import tempfile


ALLOWED_ROOTS = {
    "academy.openai.com",
    "cdn.openai.com",
    "d2xo500swnpgl1.cloudfront.net",
    "developers.openai.com",
    "downloads.ctfassets.net",
    "files.oaiusercontent.com",
    "help.openai.com",
    "model-spec.openai.com",
    "openai.com",
    "openai.fund",
    "openaifoundation.org",
    "openaiassets.blob.core.windows.net",
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


def validate_change(repo, status, path, allow_deletes=False, strict_paths=False):
    issues = []
    root = path.split("/", 1)[0]
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
        with open(fp, encoding="utf-8", errors="replace") as f:
            first = f.readline().rstrip("\n")
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
    print("self-test ok")


def main():
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    ap = argparse.ArgumentParser()
    ap.add_argument("repo")
    ap.add_argument("--staged", action="store_true", help="worktree 대신 Git index 검사")
    ap.add_argument("--allow-deletes", action="store_true", help="전량 재생성처럼 의도된 삭제 허용")
    a = ap.parse_args()
    repo = os.path.abspath(a.repo)
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
