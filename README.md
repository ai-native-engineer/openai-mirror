<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/openai-logo-dark.svg">
    <img src="assets/openai-logo.svg" alt="OpenAI" height="46">
  </picture>
</p>

<p align="center"><b>English</b> | <a href="README.ko.md">한국어</a></p>

# openai-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/openai-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/openai-mirror)

> Unofficial markdown archive of **OpenAI public materials** - news, research, OpenAI Academy, developer docs, the Model Spec, the OpenAI YouTube channel, and linked PDF documents (system cards, research papers).

Collected as a reference source for talks and study, kept public so anyone can read.

> [!WARNING]
> **Unofficial archive. Not created or operated by OpenAI.** All content is copyright **OpenAI**; this repository only mirrors published text as markdown for personal reference. Always check the official sources below for the latest and most accurate information.

## Contents

Mostly text, as of the crawl snapshot. No image or video files (videos are transcribed from captions), but PDF documents linked from pages (system cards, research papers, policy docs) are mirrored as their original `.pdf` files. Crawled Markdown pages keep a `<!-- source: <url> -->` header; YouTube channel pages store the source URL in YAML frontmatter.

| Path | Content |
|---|---|
| `openai.com/` | News, research, index articles, policies, global affairs, product pages |
| `developers.openai.com/` | API reference, guides, cookbook, and the full **Codex** docs under `/codex` (CLI reference, config, hooks, MCP, subagents, sandboxing, IDE, SDK, enterprise, use cases) |
| `academy.openai.com/` | OpenAI Academy blogs / resources / events + video transcripts |
| `help.openai.com/` | Help Center articles |
| `model-spec.openai.com/` | OpenAI Model Spec (full text) |
| `openaifoundation.org/` | OpenAI Foundation |
| `openai.fund/` | OpenAI Startup Fund |
| `youtube.com/openai/` | OpenAI YouTube channel - one transcript per available video |
| `cdn.openai.com/`, `d2xo500swnpgl1.cloudfront.net/`, `openaiassets.blob.core.windows.net/` | PDF documents linked from pages (system cards, research papers, policy docs, Academy one-pagers), kept as original files |

Academy video lessons under `academy.openai.com/public/videos/` are transcribed from Vimeo auto-generated captions, with a visible **Watch on Vimeo** link above each transcript.

The **OpenAI YouTube channel** is mirrored under `youtube.com/openai/` - one Markdown transcript per video, enumerated with `yt-dlp` and transcribed from each video's captions (videos with no captions are kept as a short stub).

**Known limitation:** API reference pages under `developers.openai.com/api/` render their parameter tables via JavaScript, so the mirror keeps each endpoint's prose and overview but not the fully expanded interactive tables.

**Known coverage gaps:** JS-rendered pages with no server-side text, Academy videos with no exposed caption source, thin club/listing pages, and collapsed interactive API/Codex tables are not fully represented. Capturing those would need a different rendering path; this mirror keeps the Cloudflare-compatible sitemap and server-rendered workflow.

## How it's generated

Crawled by an automated, sitemap-driven pipeline (no API keys). Both `openai.com` and `developers.openai.com` sit behind a Cloudflare bot challenge, so URLs come from each site's `sitemap.xml` and bodies are fetched with a Chrome browser fingerprint (`curl_cffi`) that passes the challenge without a captcha or headless browser; the pages are server-rendered, so the HTML already contains the text. Academy video lessons are transcribed from their Vimeo captions, and the OpenAI YouTube channel is enumerated with `yt-dlp` and transcribed from each video's captions. See `AGENTS.md` for regeneration details.

## Sources

- https://openai.com (news, research, index, policies)
- https://developers.openai.com (API, cookbook, Codex)
- https://academy.openai.com (OpenAI Academy)
- https://help.openai.com (Help Center)
- https://model-spec.openai.com (Model Spec)
- https://openaifoundation.org , https://openai.fund
- https://www.youtube.com/@OpenAI (YouTube channel)

## Usage

Browse any folder on GitHub, or clone the full archive:

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
```

The tree mirrors the source URLs (`<host>/<path>.md`), so a file's location maps directly to its original page.

## Out of scope

Product apps and operational / user-generated content are excluded: chatgpt.com, sora (product apps), openai.fm (demo), community.openai.com (user forum), status.openai.com (status page). External PDFs cited on OpenAI pages (arxiv, conference proceedings, government / academic sources) are not mirrored, as they are not OpenAI publications. One OpenAI PDF (the DALL-E 3 System Card, 144 MB) exceeds GitHub's file-size limit and is left to its source link.

## Updating

Re-crawled and overwritten by the `openai-mirror` skill. Only the latest mirror is kept; change history is preserved by git (`git log` / `git diff`). No dated snapshot folders are accumulated.

## Contributing

This archive is generated automatically, so files are not hand-edited - please don't open PRs that change document content (they'd be overwritten on the next sync). Instead:

- Found a broken or missing page? Open an issue.
- Are you the copyright holder requesting removal? Open an issue; the material will be taken down.

## License

No open-source license is granted - all archived text is copyright OpenAI. This repository is a study / reference mirror, and content is removed on the copyright holder's request.
