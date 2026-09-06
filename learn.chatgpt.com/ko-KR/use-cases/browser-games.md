<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/browser-games -->

## 소개

게임 개발은 Codex가 코드 생성 이상의 작업을 지원하는 방식을 가장 잘 보여 주는 사례 중 하나입니다. 실제 게임을 만들려면 대개 글로 정리한 콘셉트, 렌더링 레이어, 프런트엔드 셸 구현, 백엔드 상태 관리, 에셋 제작, 지속적인 비주얼 조정이 필요합니다

이 사용 사례에서는 Codex가 먼저 게임이 어떻게 동작해야 하는지 정확히 문서화한 다음, Playwright interactive를 사용해 실제 브라우저에서 게임을 테스트하면서 반복 개선하도록 할 때 가장 효과적입니다.

## 게임 계획부터 시작하기

Codex가 스캐폴딩 작업에 착수하기 전에 게임을 구체적으로 정의하는 `PLAN.md`를 만들도록 요청하세요:

- 플레이어의 목표
- 메인 루프
- 입력 방식과 조작법
- 승리 및 실패 조건
- 진행 방식 또는 난이도
- 비주얼 방향성
- 기술 스택과 호스팅에 대한 전제
- 마일스톤 순서

이 계획이 중요한 이유는 “게임을 만들어라”라는 지시만으로는 너무 모호하기 때문입니다. Codex는 게임의 각 부분을 어떻게 구현할지 파악할 수 있어야 하며, 빌드 과정에서 구현 세부 사항을 자주 참조해야 합니다.

`/plan` 슬래시 명령어를 사용하면 플랜 모드를 활성화할 수 있습니다.
출력 결과를 `PLAN.md` 파일로 저장하세요.

## AGENTS.md로 Codex의 동작 방식 지정하기

Codex가 계획을 따르고 작업 결과를 검증하며 적절한 도구를 사용하게 하려면 다음과 같은 `AGENTS.md`를 정의하세요:

```text
# Game name

Tech Stack:

- NextJS for frontend (hosted on Vercel)
- <insert technology> for rendering
- Fastify for backend, websockets (hosted on <hosting platform>)
- Postgres for database (hosted on <hosting platform>)
- Redis for caching and pub/sub (hosted on <hosting platform>)
- OpenAI for generative AI features

Tips:

- Use build and test commands to verify your work as soon as you complete a feature or task
- Use the PLAN.md file to guide your work when building new features
- Log your work under .logs (create new log files as you see fit) to record your thought process and decisions, and reference them when iterating on features
- Use playwright to test the visual output of your work, and iterate if it doesn't look right or fit the vibe
- Use imagegen to generate visual assets for your work, and every time you generate a collection of assets, save the prompts you used to be able to continue generating more of the same assets later (create files in .prompts)
- Use Context7 MCP to fetch <rendering framework> docs

이렇게 하면 Codex가 장시간 독립적으로 실행되며 필요에 따라 관련 스킬을 사용할 수 있습니다.

## 스킬 활용하기

AGENTS.md 파일에 언급된 스킬을 추가하세요:

- Codex가 필요에 따라 게임용 시각 에셋을 생성할 수 있게 하는 Imagegen
- Codex가 실제 브라우저에서 게임을 테스트할 수 있게 하는 Playwright interactive
- Codex가 최신 OpenAI API 문서를 가져올 수 있게 하는 OpenAI 문서
- 선택 사항으로, 렌더링 프레임워크의 최신 문서를 가져오기 위해 Context7 MCP 서버를 추가할 수도 있습니다

스킬을 추가하는 방법은 [스킬 문서](/ko-KR/codex/build-skills)에서 자세히 알아보세요.

  **팁**: 모든 시각 에셋의 일관성을 유지할 수 있도록 Codex에 이미지 생성 프롬프트를 파일로 저장해 달라고 요청하세요.
  생성하려는 에셋의 스타일을 설명하고,
  Codex가 재사용 가능한 상세 프롬프트를 만들게 하세요.

## Codex에 작업과 반복 개선 맡기기

Codex는 초기 계획을 바탕으로 게임의 첫 번째 버전을 생성합니다.

생성해야 할 이미지 에셋이 많다면 첫 번째 버전을 만드는 데 시간이 걸릴 수 있으며, 때로는 몇 시간이 소요되기도 합니다. Codex는 작업 결과를 테스트하고 실제 브라우저에서 게임을 직접 실행해 볼 수 있으므로 추가 입력 없이도 오랫동안 작업을 계속할 수 있습니다.

계획이 구체적일수록 첫 번째 반복 개선을 마쳤을 때 결과물의 완성도도 높아집니다.

직접 테스트하면서 만족스러운 결과가 나올 때까지 스크린샷을 제공하고 게임플레이 변경이나 시각 에셋 업데이트를 요청하는 방식으로 필요에 따라 반복 개선하세요.
