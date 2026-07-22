#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: refresh.sh [--force]"
}

force=()
self_test=false
case "${1:-}" in
  "") ;;
  --force) force=(--force) ;;
  --self-test) self_test=true ;;
  -h|--help) usage; exit 0 ;;
  *) usage >&2; exit 2 ;;
esac

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo="$(git -C "$script_dir" rev-parse --show-toplevel)"
skill_dir="$(cd "$script_dir/.." && pwd -P)"
crawl_dir="${CRAWL_SKILL_DIR:-$HOME/.agents/skills/shared/crawl}/scripts"
python="${OPENAI_MIRROR_PYTHON:-$HOME/.local/share/uv/tools/crawl4ai/bin/python}"

if [[ ! -x "$python" ]]; then
  python="$(command -v python3 || true)"
fi
[[ -n "$python" ]] || { echo "python3 not found" >&2; exit 1; }

required=(crawl-mirror.py youtube-channels.py youtube-transcripts.sh inline-transcripts.py render-video-refs.py pdf-mirror.py)
for file in "${required[@]}"; do
  [[ -f "$crawl_dir/$file" ]] || { echo "crawl skill dependency not found: $crawl_dir/$file" >&2; exit 1; }
done

if $self_test; then
  [[ -f "$skill_dir/SKILL.md" && -f "$repo/AGENTS.md" ]]
  echo "self-test ok"
  exit 0
fi

if ! "$python" -c 'import bs4, curl_cffi, markdownify' 2>/dev/null; then
  command -v uv >/dev/null || { echo "missing Python packages and uv is unavailable" >&2; exit 1; }
  uv pip install --python "$python" beautifulsoup4 curl_cffi markdownify
fi

export CRAWL_MIRROR_PATH="$crawl_dir/crawl-mirror.py"
cd "$repo"

"$python" "$skill_dir/scripts/crawl-site.py" . "${force[@]}"
"$python" "$skill_dir/scripts/academy-extract.py" . "${force[@]}"
"$python" "$skill_dir/scripts/docs-extract.py" . "${force[@]}"
python3 "$crawl_dir/youtube-channels.py" . openai:UCXZCJLdBC09xxGZ6gcdrc6A "${force[@]}"
bash "$crawl_dir/youtube-transcripts.sh" . --exclude 'academy.openai.com/**'
python3 "$crawl_dir/inline-transcripts.py" .
python3 "$crawl_dir/render-video-refs.py" .
python3 "$crawl_dir/pdf-mirror.py" . \
  --host openai.com \
  --host d2xo500swnpgl1.cloudfront.net \
  --host openaiassets.blob.core.windows.net \
  --host files.oaiusercontent.com \
  --host downloads.ctfassets.net \
  --host openaifoundation.org \
  --host openai.fund
python3 "$skill_dir/scripts/verify-publish.py" .
