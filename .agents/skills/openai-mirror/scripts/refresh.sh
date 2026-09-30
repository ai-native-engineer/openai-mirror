#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: refresh.sh [--check] [--force] [--refetch] [--render-only] [--prune-stale] [--self-test]"
}

# bash 3.2 (macOS) treats empty-array expansion as unbound under `set -u`; keep $force a plain word.
force=
self_test=false
check_only=false
refetch=
render_only=
prune_stale=
for arg in "$@"; do
  case "$arg" in
    --check) check_only=true ;;
    --force) force=--force ;;
    --refetch) refetch=--refetch ;;
    --render-only) render_only=--render-only ;;
    --prune-stale) prune_stale=--prune-stale ;;
    --self-test) self_test=true ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo="$(git -C "$script_dir" rev-parse --show-toplevel)"
skill_dir="$(cd "$script_dir/.." && pwd -P)"
crawl_dir="${CRAWL_SKILL_DIR:-$HOME/.agents/skills/shared/crawl}/scripts"
python="${OPENAI_MIRROR_PYTHON:-$HOME/.local/share/uv/tools/crawl4ai/bin/python}"

if [[ ! -x "$python" ]]; then
  python="$(command -v python3 || true)"
fi
[[ -n "$python" ]] || { echo "python3 not found" >&2; exit 1; }

local_required=("$skill_dir/SKILL.md" "$repo/AGENTS.md" "$skill_dir/scripts/verify-publish.py")
for file in "${local_required[@]}"; do
  [[ -f "$file" ]] || { echo "local dependency not found: $file" >&2; exit 1; }
done

if $self_test; then
  "$python" "$skill_dir/scripts/crawl-site.py" --self-test >/dev/null
  "$python" "$skill_dir/scripts/docs-extract.py" --self-test >/dev/null
  "$python" "$skill_dir/scripts/academy-extract.py" --self-test >/dev/null
  python3 "$skill_dir/scripts/mirror_state.py" --self-test >/dev/null
  python3 "$skill_dir/scripts/archive-state.py" --self-test >/dev/null
  python3 "$skill_dir/scripts/verify-publish.py" --self-test >/dev/null
  python3 "$crawl_dir/youtube-channels.py" --self-test >/dev/null
  # 수집기 호출부와 같은 전개를 태운다. 빈 값이 set -u에서 죽거나 --force가 빠지면 여기서 걸린다.
  probe=; set -- . $probe
  [[ "$#" -eq 1 ]] || { echo "self-test: 기본 실행에 인자가 붙었다" >&2; exit 1; }
  probe=--force; set -- . $probe
  [[ "$#" -eq 2 && "$2" == --force ]] || { echo "self-test: --force가 전달되지 않았다" >&2; exit 1; }
  probe=--refetch; set -- . $probe
  [[ "$#" -eq 2 && "$2" == --refetch ]] || { echo "self-test: --refetch가 전달되지 않았다" >&2; exit 1; }
  echo "self-test ok"
  exit 0
fi

required=(crawl-mirror.py youtube-channels.py youtube-transcripts.sh inline-transcripts.py render-video-refs.py split-markdown.py pdf-mirror.py)
for file in "${required[@]}"; do
  [[ -f "$crawl_dir/$file" ]] || { echo "crawl skill dependency not found: $crawl_dir/$file" >&2; exit 1; }
done

command -v yt-dlp >/dev/null || { echo "yt-dlp not found" >&2; exit 1; }

if ! "$python" -c 'import bs4, curl_cffi, markdownify' 2>/dev/null; then
  $check_only && { echo "Python packages missing: bs4, curl_cffi, or markdownify" >&2; exit 1; }
  command -v uv >/dev/null || { echo "missing Python packages and uv is unavailable" >&2; exit 1; }
  uv pip install --python "$python" beautifulsoup4 curl_cffi markdownify
fi

if $check_only; then
  echo "OK: repository $repo"
  echo "OK: skill $skill_dir"
  echo "OK: Python $python"
  echo "OK: shared crawl scripts $crawl_dir"
  exit 0
fi

export CRAWL_MIRROR_PATH="$crawl_dir/crawl-mirror.py"
export CRAWL_SKILL_DIR="$(cd "$crawl_dir/.." && pwd -P)"
cd "$repo"

# 수집기는 unresolved URL이 남으면 non-zero로 끝난다. 한 표면의 실패가 다른 표면 갱신과 감사를 막지 않도록
# 끝까지 진행하고, 실패한 단계를 모아 마지막에 non-zero로 끝낸다.
failed=
step() {
  local name="$1"; shift
  if ! "$@"; then
    echo "FAILED: $name" >&2
    failed="$failed $name"
  fi
}

step crawl-site "$python" "$skill_dir/scripts/crawl-site.py" . $force
step academy "$python" "$skill_dir/scripts/academy-extract.py" . $force
step docs "$python" "$skill_dir/scripts/docs-extract.py" . $force $prune_stale
# shared 스크립트의 --prune-stale은 목록 없이 지운다. 삭제는 archive-state.py가 목록을 출력한 뒤 수행한다.
step youtube-channels python3 "$crawl_dir/youtube-channels.py" . openai:UCXZCJLdBC09xxGZ6gcdrc6A $force $refetch $render_only
step youtube-transcripts bash "$crawl_dir/youtube-transcripts.sh" . --exclude 'academy.openai.com/**'
step inline-transcripts python3 "$crawl_dir/inline-transcripts.py" .
step render-video-refs python3 "$crawl_dir/render-video-refs.py" .
step split-markdown python3 "$crawl_dir/split-markdown.py" . --limit 786432
step pdf-mirror python3 "$crawl_dir/pdf-mirror.py" . \
  --oversize-dir _pdf-cache \
  --host openai.com \
  --host d2xo500swnpgl1.cloudfront.net \
  --host openaiassets.blob.core.windows.net \
  --host files.oaiusercontent.com \
  --host downloads.ctfassets.net \
  --host openaifoundation.org \
  --host openai.fund
step archive-state python3 "$skill_dir/scripts/archive-state.py" . all $prune_stale
step verify-publish python3 "$skill_dir/scripts/verify-publish.py" .
step tree-audit python3 "$skill_dir/scripts/verify-publish.py" . --tree-audit

if [[ -n "$failed" ]]; then
  echo "refresh 미완료: 실패 단계${failed}. _mirror-state/runs/ 의 최신 manifest에서 unresolved URL을 확인한다." >&2
  exit 1
fi
echo "refresh ok: 모든 표면 unresolved=0"
