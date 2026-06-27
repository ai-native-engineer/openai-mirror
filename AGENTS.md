# AGENTS.md

Guidance for AI agents (Claude Code, Codex, Cursor, etc.) working in this repository.

## What this repo is

A **generated** archive, not a hand-maintained one. Every Markdown file under a `<host>/` directory is crawled from a live OpenAI page and rewritten as Markdown. The first line of each file is a `<!-- source: <url> -->` pointer to the original.

## Do / Don't

- **Do not hand-edit content files.** They are overwritten on the next crawl, so edits are lost. Fix the generator (the `openai-mirror` skill), not the output.
- **Do not add files by hand** under the domain directories. New pages enter only through the crawl.
- Treat the archive as read-only when answering questions: browse and `rg`/grep across it freely.

## Layout

`<host>/<path>.md`, mirroring the original URL tree.

| Directory | Source |
|---|---|
| `openai.com/` | News, research, index articles, policies, global affairs, Codex, API, business |
| `developers.openai.com/` | API reference, guides, cookbook, Codex docs |
| `academy.openai.com/` | OpenAI Academy blogs / resources / events + video transcripts |
| `help.openai.com/` | Help Center |
| `model-spec.openai.com/` | OpenAI Model Spec |
| `openaifoundation.org/`, `openai.fund/` | OpenAI Foundation, Startup Fund |
| `youtube.com/@OpenAI/` | OpenAI YouTube channel - one Markdown transcript per video |
| `cdn.openai.com/`, `d2xo500swnpgl1.cloudfront.net/`, `openaiassets.blob.core.windows.net/` | PDF documents linked from pages, kept as original `.pdf` files (OpenAI-owned hosts only) |

## Conventions

- **Academy video lessons are transcribed** from their Vimeo auto-generated captions and saved as Markdown alongside the other lessons.
- **YouTube transcripts split by purpose.** `youtube.com/@OpenAI/` holds the **committed** OpenAI channel archive (one transcript per video). Loose `youtube.com/<ID>.md` at the directory root is a gitignored cache of transcripts inlined into pages, not committed (`.gitignore` rule: `youtube.com/*.md`).
- **Latest-only.** The newest crawl overwrites in place; there are no dated snapshot folders. History lives in git.
- **Commits:** one logical change per commit. Don't `git add .` blindly - a full crawl touches thousands of files, so stage the domains you actually regenerated. Never `git push --force` or `git reset --hard`.
- **README is bilingual** (`README.md` English, `README.ko.md` Korean). Keep both in sync when you change one.

## Regenerating

Owned by the `openai-mirror` skill (lives outside this repo). Both `openai.com` and `developers.openai.com` sit behind a Cloudflare bot challenge, so URLs come from each site's `sitemap.xml` and bodies are fetched with a Chrome browser fingerprint (`curl_cffi`) that passes the challenge without a captcha or headless browser. Academy video lessons are transcribed from Vimeo captions, and PDF documents linked from pages are mirrored as their original `.pdf` files from OpenAI-owned hosts (text-layer PDFs kept as-is; image-only PDFs get an OCR text layer). The OpenAI YouTube channel is enumerated with `yt-dlp` and each video transcribed from its captions into `youtube.com/@OpenAI/`. Do not reimplement any of this inside the repo.
