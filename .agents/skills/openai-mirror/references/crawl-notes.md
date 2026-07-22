# 수집기 구조와 함정

부분 수집, 누락 복구, 생성기 수정에 필요한 비자명한 동작을 정리한다. 전체 갱신은 `scripts/refresh.sh`를 실행한다.

## 실행 환경

- `refresh.sh --check`는 Python 의존성, `yt-dlp`, shared `crawl` 스킬을 확인하고 `refresh.sh`는 전체 트랙을 실행한다.
- 인터프리터는 `OPENAI_MIRROR_PYTHON`, shared crawl 위치는 `CRAWL_SKILL_DIR`로 바꿀 수 있다.
- 개별 수집기의 옵션은 해당 스크립트의 `--help`를 정본으로 삼는다.

## 커버리지

| 표면 | 수집기 | 발견 방식 |
|---|---|---|
| openai.com | `crawl-site.py` | sitemap + 허브 내부 링크 |
| openaifoundation.org / openai.fund | `crawl-site.py` | 같은 도메인 링크 1-depth |
| academy.openai.com | `academy-extract.py` | sitemap + Vimeo 자막 |
| developers.openai.com | `docs-extract.py` | sitemap |
| help.openai.com | `docs-extract.py` | collections/articles BFS |
| model-spec.openai.com | `docs-extract.py` | 루트가 가리키는 최신 문서 |
| OpenAI YouTube | shared `youtube-channels.py` | 채널 전 영상 + 자막 |
| OpenAI 소유 PDF | shared `pdf-mirror.py` | 허용 호스트의 원본 PDF |

## 공개 사이트

- openai.com은 Cloudflare bot challenge 뒤에 있다. headless browser 대신 `curl_cffi`의 Chrome 지문을 사용한다.
- 본문은 SSR HTML의 `<main>`, `<article>`, `<body>` 순으로 추출하고 공통 nav/footer를 제거한다.
- sitemap에 없는 제품/마케팅 페이지는 홈과 허브의 내부 링크로 보강한다.
- `thin`, 404, network/extract 실패는 저장하지 않아 다음 증분 실행에서 다시 확인한다.
- SSR 본문이 없는 폼, 인터랙티브 랜딩, 일부 고객 사례는 계속 thin일 수 있다. 이를 위해 browser 경로를 추가하지 않는다.

## OpenAI Academy

- 경로가 아니라 HTML의 Vimeo 링크로 영상을 감지한다. club 영상, event replay, resource 영상도 같은 흐름으로 처리한다.
- Vimeo config의 영어 자동 자막을 우선하며, 자막이 없는 영상은 미저장 상태가 정상이다.
- event/resource 페이지는 본문과 자막을 한 파일에 저장한다.
- shared `render-video-refs.py`가 Vimeo 링크와 접이식 자막을 렌더하며 재실행해도 중복하지 않는다.

## 공식 문서

- developers.openai.com은 `sitemap-0.xml`, Help Center는 collection/article BFS를 사용한다.
- Model Spec 루트의 meta refresh가 가리키는 최신 HTML을 저장한다.
- developers API의 JavaScript 파라미터 표처럼 SSR에 없는 인터랙티브 내용은 수집하지 못한다.
- platform.openai.com/docs는 developers.openai.com으로 이관되어 별도 수집하지 않는다.

## YouTube와 영상 후처리

- `youtube-channels.py`는 `yt-dlp --flat-playlist`로 전 영상을 열거하고 `_yt-cache/<ID>.md`를 재사용한다.
- 채널 발행물은 `youtube.com/openai/<yymmdd>-<slug>.md`, 인덱스는 `youtube.com/openai.md`다.
- 자막이 없으면 `captions: none` stub과 썸네일만 남긴다.
- `--render-only`는 캐시에서 다시 렌더하고, `--force`는 발행 파일을 다시 렌더하며, `--refetch`는 자막을 다시 받는다.
- 페이지의 YouTube 링크는 `youtube-transcripts.sh`와 `inline-transcripts.py`가 인라인한다. Academy와 채널 발행 트리는 중복 처리를 피한다.

## PDF

- `refresh.sh`의 허용 호스트만 원본 PDF로 미러한다. arxiv, 학회, 정부, 대학 등 외부 인용 PDF는 제외한다.
- PDF는 OCR이나 Markdown 변환을 하지 않고 `%PDF-`와 크기를 검증한다.
- GitHub 한도인 100MB를 넘는 파일은 내려받지 않고 source link만 유지한다.

## 증분과 범위

- 기본 실행은 기존 파일을 건너뛰고 신규/과거 실패분만 수집한다.
- `refresh.sh --force`는 사이트, Academy, 공식 문서 본문을 다시 받고 YouTube 발행 파일을 다시 렌더한다. YouTube 자막 재수집은 `--refetch`가 별도다.
- chatgpt.com, Sora, openai.fm, community.openai.com, status.openai.com은 제품 앱, 데모, 사용자/운영 콘텐츠라 제외한다.
