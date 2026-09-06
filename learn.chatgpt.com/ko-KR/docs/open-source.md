<!-- source: https://learn.chatgpt.com/ko-KR/docs/open-source -->

OpenAI는 Codex의 핵심 부분을 오픈 소스로 개발합니다. 이 작업은 GitHub에서 진행되므로 진행 상황을 확인하고, 이슈를 보고하고, 개선에 기여할 수 있습니다.

널리 사용되는 오픈 소스 프로젝트를 유지 관리하고 있거나 중요한 프로젝트를 이끄는 메인테이너를 추천하려는 경우, [Codex for OSS 프로그램에 지원하여](/community/codex-for-oss) API 크레딧, Codex가 포함된 ChatGPT Pro, Codex Security에 대한 선별적 이용 권한을 받을 수도 있습니다.

## 오픈 소스 구성 요소

| 구성 요소                     | 찾을 수 있는 곳                                                                                             | 비고                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Codex CLI                     | [openai/codex](https://github.com/openai/codex)                                                           | Codex 오픈 소스 개발의 중심 레포지토리      |
| Codex SDK                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | SDK 소스는 Codex 레포지토리에 있습니다                      |
| Codex Security CLI            | [openai/codex-security](https://github.com/openai/codex-security)                                         | 보안 취약점을 찾아 검증하는 CLI |
| Codex Security TypeScript SDK | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | Codex Security 스캔을 실행하는 TypeScript SDK         |
| Codex App Server              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | App Server 소스는 Codex 레포지토리에 있습니다               |
| 스킬                        | [openai/skills](https://github.com/openai/skills)                                                         | ChatGPT와 Codex를 확장하는 재사용 가능한 스킬           |
| 플러그인                       | [openai/plugins](https://github.com/openai/plugins)                                                       | ChatGPT와 Codex를 확장하는 재사용 가능한 플러그인                  |
| IDE 확장                 | -                                                                                                         | 오픈 소스가 아님                                         |
| Codex Cloud                   | -                                                                                                         | 오픈 소스가 아님                                         |
| 범용 클라우드 환경   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Codex Cloud에서 사용하는 기본 환경                    |

## 이슈 보고 및 기능 요청 경로

버그를 보고하거나 기능을 요청할 때는 해당 GitHub 레포지토리를 사용하세요:

- Codex 버그 보고 및 기능 요청: [openai/codex/issues](https://github.com/openai/codex/issues)
- Codex Security CLI와 TypeScript SDK의 버그 보고 및 기능 요청: [openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- 토론 포럼: [openai/codex/discussions](https://github.com/openai/codex/discussions)

이슈를 제출할 때는 사용 중인 구성 요소(CLI, SDK, IDE 확장, Codex Cloud 또는 Codex Security)와 가능하면 해당 버전을 포함하세요.
