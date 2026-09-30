# 수집기 구조와 함정

부분 수집, 누락 복구, 생성기 수정에 필요한 비자명한 동작을 정리한다. 전체 갱신은 `scripts/refresh.sh`를 실행한다.

## 실행 환경

- `refresh.sh --check`는 Python 의존성, `yt-dlp`, shared `crawl` 스킬을 확인하는 preflight다. 최신성·coverage·provenance는 `verify-publish.py --tree-audit`로 별도 확인한다.
- 인터프리터는 `OPENAI_MIRROR_PYTHON`, shared crawl 위치는 `CRAWL_SKILL_DIR`로 바꿀 수 있다.
- 개별 수집기의 옵션은 해당 스크립트의 `--help`를 정본으로 삼는다.
- 세 수집기는 `--retries`, `--retry-backoff`, `--retry-max-wait`, `--min-interval`, `--state-dir`를 공통으로 받는다(구현은 `scripts/mirror_state.py`).

## 커버리지

| 표면 | 수집기 | 발견 방식 |
|---|---|---|
| openai.com | `crawl-site.py` | sitemap + 허브/기존 생성물의 내부 링크 |
| Foundation / Fund / Alignment / Spinning Up / Progress / DevDay | `crawl-site.py` | 같은 도메인 링크 BFS |
| academy.openai.com | `academy-extract.py` | sitemap + 기존 영상 경로 + Vimeo 자막 |
| developers.openai.com | `docs-extract.py` | sitemap + 모델 상세 인덱스 + API reference 사이드바 |
| help.openai.com | `docs-extract.py` | collections/articles BFS |
| model-spec.openai.com | `docs-extract.py` | 루트가 가리키는 최신 문서 |
| learn.chatgpt.com / deploymentsafety.openai.com | `docs-extract.py` | sitemap / 상위 시스템 카드 |
| trust.openai.com | `docs-extract.py` | 비로그인 루트 개요 |
| OpenAI YouTube | shared `youtube-channels.py`, 색인 감사 `archive-state.py` | videos + shorts + streams + 자막 |
| OpenAI 소유 PDF | shared `pdf-mirror.py`, coverage 감사 `archive-state.py` | 허용 호스트의 원본 PDF |

## 공개 사이트

- openai.com은 Cloudflare bot challenge 뒤에 있다. headless browser 대신 `curl_cffi`의 Chrome 지문을 사용한다.
- 본문은 SSR HTML의 `<main>`, `<article>`, `<body>` 순으로 추출하고 공통 nav/footer를 제거한다.
- sitemap에 없는 제품/마케팅 페이지는 홈·허브와 기존 생성물의 절대 링크로 보강한다. 허브가 404/410을 재확인하면 URL 누락이 아니라 `HUBS` 정리 신호로 경고만 출력한다.
- thin, 404, 실패 URL은 저장하지 않아 다음 증분 실행에서 다시 확인한다. 판정 규칙은 「상태와 coverage」를 따른다.
- Cloudflare challenge(`Just a moment`) 응답과 `server: cloudflare`의 403은 간헐 차단이라 재시도 대상 오류로 본다.
- 형제 사이트 BFS가 발견 상한에 닿으면 URL을 잘라 버리지 않고 열거 오류(unresolved)로 남긴다.
- SSR 본문이 없는 폼, 인터랙티브 랜딩, 일부 고객 사례는 계속 thin일 수 있다. 이를 위해 browser 경로를 추가하지 않는다.
- 개발자 문서로 이관된 openai.com 경로(`/api/docs*`, `/api/reference*`, `/plugins/*`, `/ads/*` 허브 제외, `/codex/*` 허브 제외)는 크롤 대상에서 빼고 `docs-extract.py` 정본만 따른다.

## OpenAI Academy

- 경로가 아니라 HTML의 Vimeo 링크로 영상을 감지한다. club 영상, event replay, resource 영상도 같은 흐름으로 처리한다.
- Vimeo 링크는 `player.vimeo.com/video/ID`, `vimeo.com/manage/videos/ID/hash`, `progressive_redirect/playback/ID`, `vimeo.com/<user>/download/ID/hash` 형식이 섞여 있다. 앞의 형식만 잡으면 2025-08 이후 페이지가 자막 없이 텍스트로 저장된다.
- Vimeo config의 영어 자동 자막을 우선한다. 자막이 없거나 config가 비공개여도 `<!-- vimeo: ID | track: none -->` 마커와 Vimeo 링크로 provenance를 남긴다.
- 일부 Academy 영상은 YouTube 호스팅(`video.videoUrl`이 youtube.com)이다. 이때는 `<!-- youtube: ID | track: none -->`와 watch URL을 남기고, 자막은 `inline-transcripts.py`가 `_yt-cache`에 있을 때 붙인다.
- `/videos/` 경로 문서는 source 헤더와 vimeo/youtube 마커가 모두 있어야 한다. `verify-publish.py`가 없으면 문제로 보고한다.
- Academy는 분당 요청 수보다 순간 burst에 429를 주고 `Retry-After`를 보내지 않는다. 기본값은 concurrency 3, `--min-interval 1.5`, `--retries 6`, `--retry-backoff 5`, `--retry-max-wait 120`이다(2026-09-30 실측: 1.2초 간격 80회 연속 200, 무간격 concurrency 2는 25회 전후에 429).
- `--urls FILE`은 지정 URL만 덮어써 다시 받고, `--retry-unresolved`는 `_mirror-state/surfaces/academy.json`의 unresolved URL만 다시 받는다. 둘 다 부분 실행이다.
- 소량 실행은 공통 nav 판별 표본이 모자라므로 영상/일반 페이지 각 8개를 저장하지 않는 표본으로 더 받아 boilerplate를 계산한다.
- event/resource 페이지는 본문과 자막을 한 파일에 저장한다.
- shared `render-video-refs.py`가 Vimeo 링크와 접이식 자막을 렌더하며 재실행해도 중복하지 않는다.

## 공식 문서

- developers.openai.com은 `sitemap-0.xml`과 모델 목록의 상세 링크, Help Center는 collection/article BFS를 사용한다. collection 요청이 실패하면 그 아래 article이 발견 집합에서 빠지므로 열거 오류(unresolved)로 남긴다.
- API reference(`/api/reference/**`)는 sitemap에 하나도 없다. overview와 섹션 루트(overview 링크의 첫 경로 조각 + 기존 생성물의 언어 디렉터리)의 사이드바를 모으고, 사이드바가 method만 링크하므로 `resources/`/`subresources/` 뒤의 리소스 페이지를 경로에서 파생한다. CLI 사이드바처럼 일부만 링크하는 트리가 있어 `/api/reference/` 아래 기존 생성물도 발견 집합에 넣는다.
- developers/learn 문서는 가능하면 `path.md` text/markdown 원문을 우선 받고, soft-redirect(`Redirecting from … to …`)면 대상 URL 본문을 원 sitemap 경로에 저장한다.
- Model Spec 루트의 meta refresh가 가리키는 최신 HTML을 저장한다.
- ChatGPT Learn은 sitemap index를 재귀 열거한다. Deployment Safety는 sitemap의 `localhost` origin을 공개 host로 교정한 뒤, 각 섹션이 카드 전체를 반복 렌더하므로 루트와 23개 상위 시스템 카드만 저장한다. 열거에서 빠진 구 생성물은 매 실행 `삭제 후보`로 출력하고 `--prune-stale`일 때만 지운다.
- Trust Center는 비로그인 루트 개요만 저장한다. 상세 자료는 쿼리 기반 포털 UI이고 접근 요청/인증이 필요해 제외한다.
- developers API의 JavaScript 파라미터 표처럼 SSR에 없는 인터랙티브 내용은 수집하지 못한다.
- platform.openai.com/docs는 developers.openai.com으로 이관되어 별도 수집하지 않는다.
- Academy `/public/.../externals/*` 는 클라이언트 전용 셸(본문 SSR 없음)인 경우가 많아 thin skip이 정상이다.

## YouTube와 영상 후처리

- `youtube-channels.py`는 `yt-dlp --flat-playlist`로 videos/shorts/streams 탭을 합쳐 열거하고 `_yt-cache/<ID>.md`를 재사용한다.
- 색인 정합성은 `archive-state.py . youtube`가 양방향으로 비교한다. 색인 대상 파일이 없으면 unresolved, 파일만 있으면 stale 후보(같은 ID 제목 변경 / 채널 열거에서 빠진 비공개·unlisted·삭제 영상)로 `_mirror-state/surfaces/youtube.json`에 남긴다.
- `_yt-cache/`는 gitignored라 새 clone이나 worktree에는 없다. 캐시 없이 실행하면 채널 전 영상의 자막을 다시 받아 429를 부르므로, 다른 체크아웃에서 돌릴 때는 기존 `_yt-cache/`를 먼저 복사한다.
- 채널 발행물은 `youtube.com/openai/<yymmdd>-<slug>.md`, 인덱스는 `youtube.com/openai.md`다.
- 자막이 없으면 `captions: none` stub과 썸네일만 남긴다.
- `--render-only`는 캐시에서 다시 렌더하고, `--force`는 발행 파일을 다시 렌더하며, `--refetch`는 자막을 다시 받는다.
- `refresh.sh`는 `--force`, `--refetch`, `--render-only`만 shared 스크립트에 전달한다. `--prune-stale`는 shared 스크립트가 아니라 `archive-state.py`에 전달되어 삭제할 파일 목록을 출력한 뒤 지운다. 지정하지 않으면 후보 목록만 출력한다.
- 페이지의 YouTube 링크는 `youtube-transcripts.sh`와 `inline-transcripts.py`가 인라인한다. Academy와 채널 발행 트리는 중복 처리를 피한다.

## PDF

- `refresh.sh`의 허용 호스트만 원본 PDF로 미러한다. arxiv, 학회, 정부, 대학 등 외부 인용 PDF는 제외한다.
- PDF는 OCR이나 Markdown 변환을 하지 않고 `%PDF-`와 크기를 검증한다.
- GitHub 한도인 100MB를 넘는 파일은 `_pdf-cache/`에 원본 URL 경로로 내려받고, gitignored 로컬 자료로만 유지한다.
- `archive-state.py . pdf`는 pdf-mirror와 같은 scan/dest 규칙으로 발견 집합을 만들고, 미저장 PDF를 다시 요청해 404/410이 반복되거나 서명 URL이 만료됐으면 gone, 그 밖에는 unresolved로 남긴다. 말줄임표로 축약된 링크는 발견 집합에서 뺀다.

## 증분과 범위

- `split-markdown.py`는 큰 생성 문서를 768KiB 이하의 순서가 보존된 조각으로 나눠 GitHub 렌더 상한을 피한다.
- 기본 실행은 기존 파일을 건너뛰고 신규/과거 실패분만 수집한다.
- `refresh.sh --force`는 사이트, Academy, 공식 문서 본문을 다시 받고 YouTube 발행 파일을 다시 렌더한다. YouTube 자막 재수집은 `--refetch`가 별도다.
- chatgpt.com, Sora, openai.fm, community.openai.com, status.openai.com은 제품 앱, 데모, 사용자/운영 콘텐츠라 제외한다.

## 상태와 coverage

- 수집기는 실행마다 `_mirror-state/runs/<UTC>-<collector>.json`을 새로 남기고(지우지 않음), 표면별 최신 상태를 `_mirror-state/surfaces/<surface>.json`에 병합한다. 전체 범위 실행은 URL 집합을 교체하고, `--include`/`--exclude`/`--only`/`--limit`/`--urls` 같은 부분 실행은 건드린 URL만 갱신한다.
- 각 URL 기록에는 발견 여부, 상태, 저장 여부, HTTP 상태, thin 여부, 시도 횟수, 예외 메시지, 404 판정 근거가 들어간다.
- 상태는 `saved`, `existing`(증분 skip), `thin`(200이지만 본문 미달), `moved`, `gone`, `unresolved`다.
- 429, 5xx, timeout, network/추출 예외는 exponential backoff로 재시도한다. 429는 모든 worker가 함께 쉬고 `Retry-After`가 있으면 따른다.
- 404/410은 바로 삭제로 보지 않는다. canonical 링크, 끝 슬래시 경로 변경, 발견 집합에서 마지막 경로 조각이 같은 URL(하이픈이 있는 두 단어 이상 slug만, 경로가 얕은 순으로 최대 5개. 클럽별 사본이 모두 404이고 전역 경로 하나만 살아 있는 Academy 사례 때문)을 확인해 공개 URL이 있으면 `moved`, 없고 재확인도 404/410이면 `gone`, 그 밖에는 `unresolved`다.
- boilerplate 제거와 정리 후에 본문 길이를 다시 잰다. 비어 버린 문서는 저장하지 않고 `thin`으로 남긴다. 이전 버전이 이런 문서를 빈 본문으로 저장한 적이 있어 기존 파일은 `--tree-audit`의 thin 목록으로 보인다.
- sitemap, 허브, Help collection, 형제 사이트 루트처럼 발견 단계가 실패하면 열거 오류로 기록한다. 발견 집합이 불완전하므로 unresolved에 합산한다.
- unresolved가 하나라도 있으면 수집기는 non-zero로 끝난다. `refresh.sh`는 나머지 단계를 끝까지 실행한 뒤 실패 단계를 모아 non-zero로 끝낸다.
- `verify-publish.py . --tree-audit`는 파일 검사(UTF-8, 빈 파일, source 헤더, YouTube frontmatter, PDF magic bytes, Academy 영상 provenance) 뒤에 표면별 발견/저장/재시도/unresolved/thin/404/stale 표를 출력한다. 표면 manifest가 없거나 부분 실행만 있거나 unresolved가 있으면 non-zero다. stale은 전체 범위 manifest가 있을 때만 센다.
- 세 수집기의 `--verify-stale`은 발견 집합 밖 생성물의 source URL을 다시 요청해 HTTP/soft redirect면 `moved`(대상 기록), 404/410 재확인이면 `gone`, 같은 주소로 200이면 `live`로 판정해 `stale_checked`에 남긴다. 파일은 지우지 않는다. `live`는 sitemap 밖 공개 URL이므로 다음 실행부터 발견 집합에 편입된다. 단 Model Spec(최신판만), Deployment Safety(루트와 상위 카드만), Trust(개요만)는 정책상 일부만 저장하므로 편입하지 않고 stale 후보로 남긴다. 판정이 unresolved면 coverage 미완결이다.
- 2026-09-30 첫 검증 결과: learn 로케일 페이지(`/ko-KR/...`)는 영어 페이지로 redirect(`?translationFallback=`)되고, Help 구 slug는 새 slug로, developers `codex/*`는 learn으로 redirect된다. 이들은 삭제 승인 대상 후보다.

