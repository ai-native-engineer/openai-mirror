**English** | [한국어](README.ko.md)

# openai-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/openai-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/openai-mirror)
![docs ~5.8k](https://img.shields.io/badge/docs-~5.8k-blue)

> Unofficial markdown archive of **OpenAI public materials** - news, research, OpenAI Academy, developer docs, and the Model Spec.

Collected as a reference source for talks and study, kept public so anyone can read.

> [!WARNING]
> **Unofficial archive. Not created or operated by OpenAI.** All content is copyright **OpenAI**; this repository only mirrors published text as markdown for personal reference. Always check the official sources below for the latest and most accurate information.

## Contents

Text content only, as of the crawl snapshot. No image or video files (videos are transcribed from captions). Each file keeps a `<!-- source: <url> -->` header linking back to the original page.

| Path | Content | Docs |
|---|---|---|
| `openai.com/` | News, research, index articles, policies, global affairs, product pages | ~1,370 |
| `developers.openai.com/` | API reference, guides, cookbook, Codex docs | ~3,410 |
| `academy.openai.com/` | OpenAI Academy blogs / resources / events + video transcripts (71 videos) | ~550 |
| `help.openai.com/` | Help Center articles | ~450 |
| `model-spec.openai.com/` | OpenAI Model Spec (full text) | 1 |
| `openaifoundation.org/` | OpenAI Foundation | ~10 |
| `openai.fund/` | OpenAI Startup Fund | ~3 |

Academy video lessons under `academy.openai.com/public/videos/` are transcribed from Vimeo auto-generated captions.

## How it's generated

Crawled by an automated, sitemap-driven pipeline (no API keys). Both `openai.com` and `developers.openai.com` sit behind a Cloudflare bot challenge, so URLs come from each site's `sitemap.xml` and bodies are fetched with a Chrome browser fingerprint (`curl_cffi`) that passes the challenge without a captcha or headless browser; the pages are server-rendered, so the HTML already contains the text. Academy video lessons are transcribed from their Vimeo captions. See `AGENTS.md` for regeneration details.

## Sources

- https://openai.com (news, research, index, policies)
- https://developers.openai.com (API, cookbook, Codex)
- https://academy.openai.com (OpenAI Academy)
- https://help.openai.com (Help Center)
- https://model-spec.openai.com (Model Spec)
- https://openaifoundation.org , https://openai.fund

## Usage

Browse any folder on GitHub, or clone the full archive:

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
```

The tree mirrors the source URLs (`<host>/<path>.md`), so a file's location maps directly to its original page.

## Out of scope

Product apps and operational / user-generated content are excluded: chatgpt.com, sora (product apps), openai.fm (demo), community.openai.com (user forum), status.openai.com (status page).

## Updating

Re-crawled and overwritten by the `openai-mirror` skill. Only the latest mirror is kept; change history is preserved by git (`git log` / `git diff`). No dated snapshot folders are accumulated.

## Contributing

This archive is generated automatically, so files are not hand-edited - please don't open PRs that change document content (they'd be overwritten on the next sync). Instead:

- Found a broken or missing page? Open an issue.
- Are you the copyright holder requesting removal? Open an issue; the material will be taken down.

## License

No open-source license is granted - all archived text is copyright OpenAI. This repository is a study / reference mirror, and content is removed on the copyright holder's request.
