<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/update-documentation -->

## 소개

문서는 몇 주 뒤가 아니라 소스 변경과 함께 업데이트할 때 가장 쉽게 최신 상태로 유지할 수 있습니다. Codex는 변경된 코드와 테스트, 릴리스 노트, 연결된 이슈, Pull Request 컨텍스트를 살펴본 다음 기존 구조에 맞춰 범위를 적절히 한정한 문서 업데이트 초안을 작성할 수 있습니다.

개발자 문서, README 업데이트, 변경 로그 초안, 마이그레이션 노트, 런북 등 자주 변경되는 동작을 반영해야 하는 모든 문서에 이 워크플로우를 사용하세요.

## 사용 방법

1. 문서화할 변경 사항부터 시작하세요.

   브랜치, Pull Request, 커밋, 이슈 또는 파일을 공유하세요. 공개 문서라면 아직 공개되지 않은 로드맵, 고객의 비공개 세부 정보 및 내부 전용 컨텍스트를 포함하지 말아야 한다고 명시하세요.

2. 영향받는 문서 범위를 파악하도록 Codex에 요청하세요.

   초안을 작성하기 전에 기능 이름, 설정 키, 명령, 예제 및 관련 용어를 기존 문서에서 검색하도록 하세요.

3. 필요한 최소 범위의 문서만 업데이트하세요.

   Codex는 현재 페이지 구조, 용어, 상호 링크 및 프런트매터를 유지해야 합니다. 구체적인 안내 문구나 예제, 섹션만 업데이트해도 충분하다면 광범위하게 다시 작성하지 않아야 합니다.

4. 변경 사항을 검증하세요.

   레포지토리에 맞는 포맷팅 검사와 문서 검사를 실행하도록 Codex에 요청한 다음, 사용자에게 안내하는 각 내용의 근거를 요약하도록 하세요.

## Codex에 제공할 자료

| 소스                               | 도움이 되는 이유                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| 변경된 코드 및 테스트               | Codex가 실제 동작을 분석해 필요한 부분에 집중한 문서 업데이트 초안을 작성할 수 있게 합니다. |
| 공개 릴리스 노트 또는 제품 문서 | Codex가 공개 문서의 용어, 기능 제공 여부 및 상태를 정확히 반영하는 데 도움이 됩니다.    |
| Pull Request 또는 이슈 컨텍스트        | 변경 이유와 사용자가 접하는 동작 중 중요한 부분을 설명합니다.   |
| 로컬 문서 검사                    | 문서를 게시하기 전에 Codex에 구체적인 완료 기준을 제공합니다.   |

공개 릴리스 노트와 같은 컨텍스트를 추가로 제공하면 Codex가 비공개 컨텍스트나 아직 공개되지 않은 업데이트를 포함하지 않도록 할 수 있습니다.

## 반복 가능한 워크플로우 만들기

레포지토리 전체에 적용할 규칙을 정하려면 문서화 요구 사항을 [AGENTS.md](/ko-KR/codex/agent-configuration/agents-md)에 추가하세요. 예를 들면 다음과 같습니다:

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

프로세스에 단계가 더 많다면 이를 [스킬](/ko-KR/codex/build-skills)로 만들어 향후 Codex 작업에서도 동일한 소스 확인, 초안 작성 및 검증 루프를 따르도록 하세요. 이 패턴에 관한 자세한 내용은 [워크플로우를 스킬로 저장](/ko-KR/codex/use-cases/reusable-codex-skills)에서 확인하세요.

또한 [현재 채팅에서 이 워크플로우의 작업을 예약할 수 있습니다](/ko-KR/codex/automations#schedule-a-task-inside-a-chat). 예를 들어 매주 최근 GitHub Pull Request를 가져와 문서를 최신 상태로 유지하도록 Codex에 요청하세요:
