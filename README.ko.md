<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/openai-logo-dark.svg">
    <img src="assets/openai-logo.svg" alt="OpenAI" height="46">
  </picture>
</p>

<p align="center"><a href="README.md">English</a> | <b>한국어</b></p>

# openai-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/openai-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/openai-mirror)
![docs ~5.9k](https://img.shields.io/badge/docs-~5.9k-blue)

> **OpenAI 공개 자료**(뉴스, 연구, OpenAI Academy, 개발자 문서, Model Spec, OpenAI YouTube 채널, 페이지에 링크된 PDF 문서)를 마크다운으로 정리한 비공식 아카이브.

강의/자료 제작 시 참고 소스로 모았고, 누구나 읽어볼 수 있게 공개해 둡니다.

> [!WARNING]
> **비공식 아카이브입니다. OpenAI가 만들거나 운영하지 않습니다.** 모든 콘텐츠의 저작권은 **OpenAI**에 있으며, 이 저장소는 원문을 마크다운으로 변환해 보관한 개인 참고용 미러입니다. 최신/정확한 내용은 항상 아래 공식 출처를 확인하세요.

## 무엇이 담겨 있나

크롤 시점(스냅샷) 기준 대부분 텍스트 본문입니다. 이미지/동영상 파일은 포함하지 않지만(영상은 자막을 텍스트로 전사), 페이지에 링크된 PDF 문서(system cards, 연구 논문, 정책 문서)는 원본 `.pdf` 파일로 보관합니다. 각 파일 상단에는 원문 링크 `<!-- source: <url> -->`가 붙어 있습니다.

| 경로 | 내용 | 문서 수 |
|---|---|---|
| `openai.com/` | 뉴스, 연구, index 기사, 정책, global affairs, 제품 페이지 | 약 1,370 |
| `developers.openai.com/` | API 레퍼런스, 가이드, cookbook, `/codex` 하위 **Codex** 문서 전체(CLI 레퍼런스, config, hooks, MCP, subagents, sandboxing, IDE, SDK, 엔터프라이즈, use-case 80여 개) | 약 3,410 |
| `academy.openai.com/` | OpenAI Academy 블로그 / 리소스 / 이벤트 + 영상 전사(71편) | 약 550 |
| `help.openai.com/` | 헬프센터 article | 약 450 |
| `model-spec.openai.com/` | OpenAI Model Spec 전문 | 1 |
| `openaifoundation.org/` | OpenAI Foundation | 약 10 |
| `openai.fund/` | OpenAI Startup Fund | 약 3 |
| `youtube.com/@OpenAI/` | OpenAI YouTube 채널 - 영상 1편당 전사 1개 | 약 530 |
| `cdn.openai.com/`, `d2xo500swnpgl1.cloudfront.net/`, `openaiassets.blob.core.windows.net/` | 페이지에 링크된 PDF 문서(system cards, 연구 논문, 정책 문서, Academy 원페이저), 원본 파일로 보관 | PDF 228개 |

`academy.openai.com/public/videos/`의 영상 레슨은 Vimeo 자동생성 자막을 텍스트로 전사하고, 전사 위에 보이는 **Watch on Vimeo** 링크를 답니다.

**OpenAI YouTube 채널**은 `youtube.com/@OpenAI/` 아래에 미러합니다 - `yt-dlp`로 전 영상을 열거하고 각 영상 자막을 텍스트로 전사해 영상 1편당 마크다운 1개로 둡니다(자막이 없는 영상은 짧은 stub로 남깁니다).

**알려진 한계:** `developers.openai.com/api/` 하위 API 레퍼런스 페이지는 파라미터 표를 JavaScript로 렌더해서, 미러는 각 엔드포인트의 산문/개요는 담지만 완전히 펼쳐진 인터랙티브 표는 담지 못합니다.

**알려진 커버리지 갭** (각 sitemap 대조 측정): `openai.com`/`developers.openai.com` 약 98%, `academy.openai.com` 약 90%. 못 담은 것: 서버측 텍스트가 없는 JS 렌더 `openai.com` 페이지 약 23개, 자막 소스가 없는 academy 영상 약 20개, 얇은 academy club/목록 페이지 약 36개. JS로 로드되는 콘텐츠(위 API 표, 일부 Codex 문서의 "Expand to view all" enum 목록)도 펼쳐지지 않습니다. 이들을 담으려면 헤드리스 브라우저가 필요한데, Cloudflare 통과를 위해 쓰지 않습니다.

## 어떻게 만들어지나

sitemap 기반 자동 크롤 파이프라인으로 수집합니다(API 키 없음). `openai.com`과 `developers.openai.com` 모두 Cloudflare 봇 챌린지 뒤에 있어, URL은 각 사이트의 `sitemap.xml`에서 받고 본문은 Chrome 브라우저 지문(`curl_cffi`)으로 캡챠/헤드리스 브라우저 없이 챌린지를 통과해 가져옵니다. 페이지가 SSR이라 HTML에 본문이 들어 있습니다. Academy 영상 레슨은 Vimeo 자막으로 전사하고, OpenAI YouTube 채널은 `yt-dlp`로 전 영상을 열거해 각 영상 자막으로 전사합니다. 재생성 절차는 `AGENTS.md` 참조.

## 출처 (Sources)

- https://openai.com (news, research, index, policies)
- https://developers.openai.com (API, cookbook, Codex)
- https://academy.openai.com (OpenAI Academy)
- https://help.openai.com (Help Center)
- https://model-spec.openai.com (Model Spec)
- https://openaifoundation.org , https://openai.fund
- https://www.youtube.com/@OpenAI (YouTube 채널)

## 사용법

GitHub에서 폴더별로 바로 읽거나, 전체를 클론하세요:

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
```

트리는 원문 URL 구조(`<host>/<path>.md`)를 그대로 따라가므로, 파일 위치가 곧 원문 페이지 위치입니다.

## 범위 밖

제품 앱과 운영 / 사용자 생성 콘텐츠는 제외합니다: chatgpt.com, sora(제품 앱), openai.fm(데모), community.openai.com(사용자 포럼), status.openai.com(운영 상태). OpenAI 페이지에 인용된 외부 PDF(arxiv, 학회 proceedings, 정부 / 학술 출처)는 OpenAI 발행물이 아니라 미러하지 않습니다. OpenAI PDF 1건(DALL-E 3 System Card, 144MB)은 GitHub 파일 크기 제한을 넘어 소스 링크로만 둡니다.

## 갱신

`openai-mirror` 스킬로 다시 크롤해 최신 미러만 덮어씁니다. 변경 이력은 git이 보존하므로 `git log` / `git diff`로 추적합니다(날짜별 디렉토리를 누적하지 않습니다).

## 기여

이 아카이브는 자동 생성되므로 파일을 손으로 고치지 않습니다 - 문서 내용을 바꾸는 PR은 다음 동기화 때 덮어써지니 보내지 마세요. 대신:

- 깨졌거나 빠진 페이지를 찾으셨나요? 이슈를 열어 주세요.
- 저작권자로서 자료 삭제를 원하시나요? 이슈를 열어 주시면 해당 자료를 내립니다.

## 라이선스 / 저작권

오픈소스 라이선스를 부여하지 않습니다 - 보관된 텍스트의 저작권은 전부 OpenAI에 있습니다. 학습 / 참고 목적의 미러이며, 저작권자의 요청이 있으면 해당 자료를 내립니다.
