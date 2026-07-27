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

OpenAI 공개 자료를 검색하기 쉬운 마크다운으로 보관하는 비공식 아카이브입니다. 기사, Academy 리소스, 공식 문서·연구 사이트, YouTube 전사, OpenAI가 호스팅하는 PDF를 담습니다.

> [!WARNING]
> OpenAI가 만들거나 운영하는 저장소가 아닙니다. 보관된 자료의 저작권은 OpenAI에 있습니다. 최신 공식 정보는 반드시 원문에서 확인하세요.

## 아카이브

| 경로 | 자료 |
|---|---|
| [`openai.com/`](openai.com/) | 뉴스, 연구, 정책, 제품 페이지 |
| [`developers.openai.com/`](developers.openai.com/) | API, cookbook, Codex 문서 |
| [`help.openai.com/`](help.openai.com/) | 도움말 센터 문서 |
| [`model-spec.openai.com/`](model-spec.openai.com/) | Model Spec |
| [`learn.chatgpt.com/`](learn.chatgpt.com/), [`deploymentsafety.openai.com/`](deploymentsafety.openai.com/) | ChatGPT Learn과 배포 안전 문서 |
| [`alignment.openai.com/`](alignment.openai.com/), [`spinningup.openai.com/`](spinningup.openai.com/) | Alignment Research와 Spinning Up |
| [`progress.openai.com`](progress.openai.com.md), [`devday.openai.com`](devday.openai.com.md), [`trust.openai.com`](trust.openai.com.md) | Progress, DevDay, Trust Center 공개 개요 |
| [`academy.openai.com/`](academy.openai.com/) | Academy 리소스, 이벤트, 영상 전사 |
| [`openaifoundation.org/`](openaifoundation.org/), [`openai.fund/`](openai.fund/) | Foundation 및 Startup Fund 페이지 |
| [`youtube.com/openai/`](youtube.com/openai/) | 영상별 전사 또는 자막 상태 stub |
| OpenAI 소유 파일 호스트 | 보관된 페이지가 링크한 PDF |

트리는 원문 URL을 `<host>/<path>.md` 형태로 따릅니다. 크롤한 페이지에는 `<!-- source: <url> -->` 헤더가 있고, YouTube 전사는 YAML frontmatter에 원문 URL을 기록합니다.

## 사용

GitHub에서 바로 읽거나, 로컬에서 `rg`로 검색하거나, 전체 아카이브를 클론할 수 있습니다.

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
cd openai-mirror
rg "reasoning models"
```

선택적으로 [gbrain](https://github.com/garrytan/gbrain)을 이용해 RAG 검색을 할 수 있습니다. 이 클론을 한 번 등록하고 동기화하면 저장소 안 어디서든 질의할 수 있습니다.

```bash
gbrain sources add openai-mirror --path "$PWD" --no-federated
gbrain sync --source openai-mirror --no-pull --no-extract --no-embed
gbrain query "추론 모델은 어떻게 동작하나요?"
```

저장소의 `.gbrain-source` 파일이 질의 범위를 이 아카이브로 자동 제한합니다. 미러를 갱신한 뒤에는 동기화를 다시 실행하세요. 벡터 검색까지 추가하려면 `--no-embed`를 빼세요. 이 경우 아카이브 텍스트가 설정된 임베딩 제공자에게 전송되고 사용료가 발생할 수 있습니다.

## 수집 범위

아카이브는 같은 위치에 다시 생성하며 최신 크롤만 유지합니다. 이전 버전은 Git 이력으로 확인할 수 있습니다.

- JavaScript로만 표시되는 내용과 접힌 API 인터랙티브 표는 일부 누락될 수 있습니다.
- 접근 가능한 자막이 없는 영상은 짧은 stub로 남거나 제외됩니다.
- 외부 발행물과 GitHub 용량 제한을 넘는 파일은 원문 링크만 남깁니다.
- 제품 앱, 커뮤니티 콘텐츠, 데모, 상태 페이지는 수집하지 않습니다.

## 갱신과 기여

보관된 페이지는 생성 파일입니다. 내용을 직접 고치지 말고 누락되거나 깨진 페이지를 이슈로 알려주세요. 관리자는 [`.agents/skills/openai-mirror/`](.agents/skills/openai-mirror/)를 수정한 뒤 해당 도메인을 다시 생성합니다.

## 저작권

보관된 자료에 별도 라이선스를 부여하지 않습니다. 저작권자는 이슈로 삭제를 요청할 수 있습니다.
