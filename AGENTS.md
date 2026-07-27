# AGENTS.md

This repository is a generated, latest-only archive of OpenAI public materials.

## Rules

- Treat host-named Markdown and PDF outputs as read-only. Fix `.agents/skills/openai-mirror/` and regenerate instead of editing or adding generated files.
- Crawled pages use `<!-- source: <url> -->`; YouTube pages use YAML frontmatter. `_yt-cache/` is gitignored.
- Browse the archive freely with `rg` when answering questions.
- Preserve unrelated work, stage only regenerated domains with explicit paths, and keep one logical change per commit.
- Push only with explicit approval. Never force-push or hard-reset.
- Keep `README.md` and `README.ko.md` in sync.

## Search

- Search Markdown content with context: `rg -i -n -C 2 --glob '*.md' 'term|synonym'`.
- List matching documents with `rg -l -i --glob '*.md' 'term|synonym'`; search paths with `rg --files | rg -i 'term'`.
- `rg` does not search PDF contents directly. When PDF coverage matters, run `./search-archive.sh 'term|synonym'`.
- PDF result line numbers refer to extracted text; open the matching PDF to verify its page and surrounding context.
- Most archived text is English, so translate non-English topics and try English synonyms.
