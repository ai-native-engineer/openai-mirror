[English](README.md) | **한국어**

# openai-mirror

![status: unofficial mirror](https://img.shields.io/badge/status-unofficial%20mirror-orange)
![last commit](https://img.shields.io/github/last-commit/ai-native-engineer/openai-mirror)
![repo size](https://img.shields.io/github/repo-size/ai-native-engineer/openai-mirror)
![docs ~5.8k](https://img.shields.io/badge/docs-~5.8k-blue)

> **OpenAI 공개 자료**(뉴스, 연구, OpenAI Academy, 개발자 문서, Model Spec)를 마크다운으로 정리한 비공식 아카이브.

강의/자료 제작 시 참고 소스로 모았고, 누구나 읽어볼 수 있게 공개해 둡니다.

> [!WARNING]
> **비공식 아카이브입니다. OpenAI가 만들거나 운영하지 않습니다.** 모든 콘텐츠의 저작권은 **OpenAI**에 있으며, 이 저장소는 원문을 마크다운으로 변환해 보관한 개인 참고용 미러입니다. 최신/정확한 내용은 항상 아래 공식 출처를 확인하세요.

## 무엇이 담겨 있나

크롤 시점(스냅샷) 기준 텍스트 본문만 보관합니다. 이미지/동영상 파일은 포함하지 않습니다(영상은 자막을 텍스트로 전사). 각 파일 상단에는 원문 링크 `<!-- source: <url> -->`가 붙어 있습니다.

| 경로 | 내용 | 문서 수 |
|---|---|---|
| `openai.com/` | 뉴스, 연구, index 기사, 정책, global affairs, 제품 페이지 | 약 1,370 |
| `developers.openai.com/` | API 레퍼런스, 가이드, cookbook, Codex 문서 | 약 3,410 |
| `academy.openai.com/` | OpenAI Academy 블로그 / 리소스 / 이벤트 + 영상 전사(71편) | 약 550 |
| `help.openai.com/` | 헬프센터 article | 약 450 |
| `model-spec.openai.com/` | OpenAI Model Spec 전문 | 1 |
| `openaifoundation.org/` | OpenAI Foundation | 약 10 |
| `openai.fund/` | OpenAI Startup Fund | 약 3 |

`academy.openai.com/public/videos/`의 영상 레슨은 Vimeo 자동생성 자막을 텍스트로 전사해 보관합니다.

## 출처 (Sources)

- https://openai.com (news, research, index, policies)
- https://developers.openai.com (API, cookbook, Codex)
- https://academy.openai.com (OpenAI Academy)
- https://help.openai.com (Help Center)
- https://model-spec.openai.com (Model Spec)
- https://openaifoundation.org , https://openai.fund

## 사용법

GitHub에서 폴더별로 바로 읽거나, 전체를 클론하세요:

```bash
git clone https://github.com/ai-native-engineer/openai-mirror.git
```

트리는 원문 URL 구조(`<host>/<path>.md`)를 그대로 따라가므로, 파일 위치가 곧 원문 페이지 위치입니다.

## 범위 밖

제품 앱과 운영 / 사용자 생성 콘텐츠는 제외합니다: chatgpt.com, sora(제품 앱), openai.fm(데모), community.openai.com(사용자 포럼), status.openai.com(운영 상태).

## 갱신

`openai-mirror` 스킬로 다시 크롤해 최신 미러만 덮어씁니다. 변경 이력은 git이 보존하므로 `git log` / `git diff`로 추적합니다(날짜별 디렉토리를 누적하지 않습니다).

## 기여

이 아카이브는 자동 생성되므로 파일을 손으로 고치지 않습니다 - 문서 내용을 바꾸는 PR은 다음 동기화 때 덮어써지니 보내지 마세요. 대신:

- 깨졌거나 빠진 페이지를 찾으셨나요? 이슈를 열어 주세요.
- 저작권자로서 자료 삭제를 원하시나요? 이슈를 열어 주시면 해당 자료를 내립니다.

## 라이선스 / 저작권

오픈소스 라이선스를 부여하지 않습니다 - 보관된 텍스트의 저작권은 전부 OpenAI에 있습니다. 학습 / 참고 목적의 미러이며, 저작권자의 요청이 있으면 해당 자료를 내립니다.
