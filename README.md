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

An unofficial, searchable Markdown archive of OpenAI public materials: articles, Academy resources, official documentation and research sites, YouTube transcripts, and OpenAI-hosted PDFs.

> [!WARNING]
> This repository is not created or operated by OpenAI. OpenAI retains the copyright to the archived material. Check the official source for current, authoritative information.

## Archive

| Path | Material |
|---|---|
| [`openai.com/`](openai.com/) | News, research, policy, and product pages |
| [`developers.openai.com/`](developers.openai.com/) | API, cookbook, and Codex documentation |
| [`help.openai.com/`](help.openai.com/) | Help Center articles |
| [`model-spec.openai.com/`](model-spec.openai.com/) | Model Spec |
| [`learn.chatgpt.com/`](learn.chatgpt.com/), [`deploymentsafety.openai.com/`](deploymentsafety.openai.com/) | ChatGPT Learn and deployment safety documentation |
| [`alignment.openai.com/`](alignment.openai.com/), [`spinningup.openai.com/`](spinningup.openai.com/) | Alignment Research and Spinning Up |
| [`progress.openai.com`](progress.openai.com.md), [`devday.openai.com`](devday.openai.com.md), [`trust.openai.com`](trust.openai.com.md) | Progress, DevDay, and the public Trust Center overview |
| [`academy.openai.com/`](academy.openai.com/) | Academy resources, events, and video transcripts |
| [`openaifoundation.org/`](openaifoundation.org/), [`openai.fund/`](openai.fund/) | Foundation and Startup Fund pages |
| [`youtube.com/openai/`](youtube.com/openai/) | One transcript or caption-status stub per video |
| OpenAI-owned file hosts | PDFs linked from archived pages |

The tree follows source URLs as `<host>/<path>.md`. Crawled pages include a `<!-- source: <url> -->` header; YouTube transcripts keep the source URL in YAML frontmatter.

## Use

Browse on GitHub, search locally with `rg`, or clone the archive:

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
cd openai-mirror
rg -i -n -C 2 --glob '*.md' 'harness engineering|agent harness'
rg -l -i --glob '*.md' 'reasoning models|test-time compute'
rg --files | rg -i 'harness|reasoning'
```

The first command shows matching Markdown with line numbers and surrounding context. The second lists matching documents, and the third searches file paths. Most archived text is English, so start with English terms and synonyms.

`rg` cannot search compressed PDF contents directly. To search Markdown and every PDF text layer together, install `pdftotext` (Poppler; `brew install poppler` on macOS) and run:

```bash
./search-archive.sh 'harness engineering|agent harness'
```

PDF result line numbers refer to extracted text, not PDF page numbers.

## Coverage

The archive is regenerated in place and keeps only the latest crawl. Git preserves earlier revisions.

- JavaScript-only content and collapsed interactive API tables may be incomplete.
- Videos without accessible captions are kept as short stubs or omitted.
- External publications and files over GitHub's size limit remain source links.
- Product apps, community content, demos, and status pages are outside the archive scope.

## Updates and contributions

Archived pages are generated files. Report missing or broken pages with an issue instead of editing their contents. Maintainers should update [`.agents/skills/openai-mirror/`](.agents/skills/openai-mirror/) and regenerate the affected domains.

## Copyright

No license is granted for the archived material. Copyright holders may request removal by opening an issue.
