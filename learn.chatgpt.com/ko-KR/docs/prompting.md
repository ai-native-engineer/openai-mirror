<!-- source: https://learn.chatgpt.com/ko-KR/docs/prompting -->

<a id="prompts"></a>

## 프롬프팅 개요

프롬프팅은 알고 싶거나 만들거나 변경하려는 내용을 ChatGPT에 전달하는 방법입니다. 프롬프트는 질문이나 지시, 목표가 될 수 있습니다. 전문적인 문법이나 정해진 형식은 필요하지 않습니다. 자신의 말로 시작한 뒤 응답을 검토하고, 후속 메시지를 통해 결과를 다듬어 가세요.

짧은 프롬프트만으로도 충분한 경우가 많습니다. 규모가 크거나 중요한 작업이라면 다음 중 필요한 요소를 포함하세요:

- **목표:** ChatGPT가 무엇을 해야 하나요?
- **컨텍스트:** 어떤 정보나 출처가 도움이 되나요?
- **출력:** 어떤 형식과 분량, 어느 정도의 상세함이 필요한가요?
- **제한 사항:** 변경하지 않아야 할 사항은 무엇인가요? ChatGPT가 피해야 할 일이나 실행 전에
  사용자에게 확인해야 할 사항은 무엇인가요?

도움이 되는 요소만 사용하세요. 모든 항목을 채우거나 정해진 형식을 따를 필요는 없습니다.

## 필요한 결과 설명하기

세부 절차를 나열하기보다 원하는 결과부터 설명하세요. 대상 독자나 형식에 따라 ChatGPT가 만들어야 할 결과물이 달라진다면 이러한 정보도 포함하세요.

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

이 프롬프트는 무엇을 만들고 누가 읽을지를 설명합니다. 과정 자체가 중요하다면 그 과정을 설명하세요. 그렇지 않다면 ChatGPT가 정보를 검색하고 비교하면서 접근 방식을 조정할 수 있도록 여지를 남겨 두세요.

<a id="context"></a>

## 유용한 컨텍스트 추가하기

결과에 영향을 줄 수 있는 정보를 공유하세요. 중요한 출처만 추가하고, ChatGPT가 각 출처에서 무엇을 파악해야 하는지 설명하세요.

- ChatGPT에 자료 요약, 비교, 변환 또는 [검토용 파일 생성](/ko-KR/codex/artifacts-viewer)을 요청할 때는
  문서, 스프레드시트, 프레젠테이션 또는 PDF 파일을 첨부하세요.
- 시각적 컨텍스트가 중요한 작업이라면 스크린샷, 다이어그램 또는 다른 [이미지 입력](/ko-KR/codex/image-inputs)을
  추가하세요. 이미지에만 의존하지 말고 중요한 부분을
  직접 짚어 주세요.
- 답변에 최신 정보가 필요하면 ChatGPT에 [웹 검색](/ko-KR/codex/web-search)을 활용하도록
  요청하고, 결과를 확인해야 한다면 출처도 함께 요청하세요.
- 관련 채팅에서 파일, 출처 또는 로컬 폴더를 공유해야 한다면 [프로젝트](/ko-KR/codex/projects)를
  사용하세요.

### 연결된 소스 사용하기

ChatGPT가 연결된 소스에 접근할 수 있다면 어디에서 무엇을 찾아야 하는지 지정하세요. 필요한 검색을 하나하나 설명할 필요는 없습니다.

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

연결된 소스를 사용하려면 해당 플러그인이 필요하며, 사용 가능 여부는 요금제와 워크스페이스 설정에 따라 달라질 수 있습니다.

### 플러그인 사용하기

플러그인은 ChatGPT와 Codex에 재사용 가능한 지침과 Google Drive, Gmail, Slack, GitHub 등의
도구 연결을 제공합니다. 두 제품 모두 동일한 범용 디렉터리에서 공개
플러그인을 가져옵니다. 필요한 결과를 요청하고 현재 사용 중인 인터페이스가
이용 가능한 도구 중에서 적절한 도구를 선택하도록 하세요. ChatGPT에서는 메시지 입력창에 `@`을
입력해 특정 플러그인을 선택하세요.

  
    <span slot="icon">
      
    </span>
    ChatGPT와 Codex에서 플러그인을 찾고 설치해 사용하세요.
  

### ChatGPT 개인 맞춤 설정

모든 채팅에 적용할 선호 사항은 **설정 \> 개인 맞춤 설정에서**
맞춤형 지침으로 등록하세요. 현재 채팅에만 필요한 세부 정보는
프롬프트에 포함하세요.

  
    <span slot="icon">
      
    </span>
    기본 성격, 맞춤형 지침, 기타 앱 환경설정을 지정하세요.
  

## 실제 문제를 방지하는 제한 사항 설정하기

제한 사항은 ChatGPT가 불필요한 작업을 늘리거나 의도하지 않은 행동을 하지 않도록 하는 몇 가지 지침입니다. 중요한 세부 정보가 잘못 변경되어 결과물을 사용할 수 없게 될 수 있거나, 다른 사람에게 영향을 미치기 전에 내용을 검토하고 싶다면 제한 사항을 추가하세요.

- 승인된 날짜와 예산 수치는 변경하지 마세요.
- 제공된 출처만 사용하세요. 추측하지 말고 누락된 정보를 표시하세요.
- 명시된 예산 범위 내에서만 추천하세요.
- 메시지는 초안만 작성하고 보내지 마세요.

가장 중요한 제한 사항 한두 가지에 집중하세요. ChatGPT가 수행하는 모든 단계를 통제할 필요는 없습니다.

## 결과를 바로 사용할 수 있게 만들기

결과를 어떻게 사용할 예정인지 ChatGPT에 알려 주세요. 그러면 용도에 맞는 분량과 상세 수준, 구성 방식을 선택할 수 있습니다.

- 회의 전에 책임자가 훑어볼 수 있도록 한 페이지로 요약하세요. 결정 사항과 다음 단계를 맨 앞에 배치하세요.
- 이 메모를 바탕으로 결정 사항, 담당자, 기한을 담은 후속 이메일을 작성하세요.
- 계획 지출과 실제 지출을 명확한 표로 비교하고, 차이가 10%를 넘는 항목을 모두 강조하세요.

중요한 작업이라면 ChatGPT에 최종 점검을 요청하세요. 예를 들어 모든 실행 항목에 담당자와 기한이 지정되었는지 확인하거나 검증하지 못한 정보를 표시하도록 할 수 있습니다. 그런 다음 결과를 사용하거나 공유하기 전에 직접 검토하세요.

## 후속 메시지로 결과 개선하기

첫 프롬프트부터 완벽할 필요는 없습니다. 결과를 검토한 다음, 원하는 변경 사항을 구체적으로 요청하세요.

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

처음부터 다시 시작하지 않고도 누락된 출처를 추가하거나, 방향을 바로잡거나, 다른 선택지를 요청하거나, 상세 수준을 변경할 수 있습니다.

### 메시지 즉시 반영 및 대기열 추가

Codex가 이미 작업 중이라면 현재 실행이 끝날 때까지 기다리지 않고 다른 메시지를 보낼 수 있습니다:

- **즉시 반영은** 메시지를 현재 실행에 추가합니다. 방향을 바꾸거나 누락된
  세부 정보를 추가하거나 새 정보를 제공할 때 사용하세요.
- **대기열 추가는** 메시지를 다음 실행을 위해 저장합니다. 현재 작업이
  끝난 뒤 처리해야 하는 후속 요청에 사용하세요.

ChatGPT 데스크톱 앱에서는
[**설정 \> 일반 \> 후속 메시지 동작에서**](/ko-KR/codex/app/settings#general) 기본 동작을 선택하세요.
대기열에 추가한 메시지는 메시지 입력창 위에 표시되며, 편집하거나 순서를 바꾸고
보내거나 삭제할 수 있습니다. 이 설정에서는 기본값을 변경하지 않고 메시지 하나에만 다른
동작을 적용하는 단축키도 확인할 수 있습니다.

Codex CLI에서 Codex가 작업하는 동안 <kbd>Enter</kbd>를 누르면 현재
턴에 메시지가 즉시 반영되고, <kbd>Tab</kbd>을 누르면 다음 턴의 대기열에 추가됩니다. 자세한 내용은
[대화형 단축키](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)를
참고하세요.

## 요소 조합하기

연결된 소스를 활용해 프로젝트 업데이트를 작성하는 경우, 전체 프롬프트는 다음과 같이 구성할 수 있습니다:

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

이 프롬프트는 **목표**, **컨텍스트**, **출력**, **제한 사항을** 모두 다루며,
모든 단계를 일일이 설명하지 않고 최종 점검도 요청합니다.

## 음성 받아쓰기 사용하기

ChatGPT 데스크톱 앱에서 메시지 입력창이 보일 때 <kbd>Ctrl+Shift+D</kbd>를
누른 다음 말하기 시작하세요. ChatGPT가 음성을 텍스트로 변환해 메시지 입력창에 입력하므로
프롬프트를 보내기 전에 검토하고 수정할 수 있습니다.

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## 채팅 프롬프팅 예시

질문, 아이디어 구상, 초안 작성, 일상적인 의사 결정에는 채팅을 사용하세요. 원하는 결과부터 설명하고, 답변에 영향을 줄 때만 세부 정보를 추가하세요.

### 주제 이해하기

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### 글 초안 작성 및 다듬기

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### 선택지 비교하기

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### 실용적인 계획 세우기

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## ChatGPT Work 프롬프팅

빠른 질문, 짧은 문장 수정, 브레인스토밍, 간단한 초안 작성에는 채팅을 사용하세요. 여러 자료나 도구를 활용하거나, 여러 단계를 거치거나, 변경 작업을 수행하거나, 규모가 더 큰 결과물을 만드는 작업에는 ChatGPT Work를 사용하세요.

ChatGPT Work에서는 필요한 결과를 설명하고, 원본 자료를 제공하고, 대상 독자를 명시한 다음 작업을 어떻게 검토할지 설명하세요. ChatGPT에 계획을 세우고 필요한 정보를 수집해 파일을 만든 다음, 작업을 마치기 전에 해당 파일을 확인하도록 요청하세요.

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### ChatGPT Work를 효율적으로 사용하기

ChatGPT Work는 시간이 오래 걸리거나 반복되는 작업, 또는 재사용할 수 있는 완성된 파일을 만드는 데 유용합니다. 크레딧을 더 많이 사용하는 작업이라도 시간을 절약하거나 품질을 높이거나 중요한 결정을 내리는 데 도움이 된다면 충분한 가치가 있습니다.

검토할 수 있는 결과물 하나부터 시작하세요:

- 관련 자료만 포함하고, 필요한 경우 날짜 범위를 제한하세요.
- 대상 독자, 출력 형식, 원하는 길이를 지정하세요.
- 필수 작업과 선택적인 개선 또는 다듬기 작업을 구분하세요.
- 접근 방식이 중요하다면 계획을 요청하세요. ChatGPT가 다른 사람이 의존하는 정보를 전송하거나 게시하거나 변경하기 전에는 반드시 사용자의 승인을 받도록 하세요.
- 더 이상 필요하지 않은 일을 하기 시작하면 작업 범위를 줄이거나 작업을 중지하세요.

첫 번째 결과를 검토하고 지침을 다듬은 다음, 워크플로우가 잘 작동하면 재사용하세요.

### 원본 자료를 완성된 파일로 만들기

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### 의사결정에 필요한 정보 조사하기

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### 출시 조율하기

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

반복 작업은 먼저 일반 채팅에서 프롬프트를 다듬으세요. 결과물을
신뢰할 수 있게 되면 [해당 채팅 안에서 작업을 예약하세요](/ko-KR/codex/automations#schedule-a-task-inside-a-chat).
예약 작업이 실행될 때마다 새 채팅을 시작해야 한다면
독립형 예약 작업을 대신 만드세요.

<a id="use-editor-context"></a>

## Codex 프롬프팅

ChatGPT가 코드, 코드베이스 또는 개발자 도구를 다루도록 하려면 Codex를 사용하세요. 유용한 Codex 프롬프트에는 원하는 동작, 관련 코드 또는 재현 단계, 유지해야 하는 중요한 제약 조건, 변경 사항을 검증하는 방법이 명시되어 있습니다.

<a id="goal-mode"></a>

여러 단계로 이루어진 작업에서 Codex가 코드를 수정하기 전에 조사하고 접근 방식을 제안하도록 하려면 앱 Composer에 `/plan`을
입력하세요. [목표 모드](/ko-KR/codex/long-running-work)를
사용할 수 있다면 계획을 세운 후 `/goal`을 사용해 지속적인 목표를 설정하세요. [앱 슬래시
명령어](/codex/reference/slash-commands)에서
현재 사용할 수 있는 명령어 목록을 확인하세요.

### 예시를 살펴보는 방법

각 워크플로우에는 다음 내용이 포함됩니다:

- **사용 시점과** 가장 적합한 Codex 사용 환경(IDE, CLI 또는 클라우드).
- **진행 단계와** 사용자 프롬프트 예시.
- **컨텍스트 참고 사항**: Codex가 자동으로 확인하는 항목과 사용자가 직접 첨부해야 하는 항목.
- **검증**: 결과물을 확인하는 방법.

> **참고:** IDE 확장은 열어 둔 파일을 컨텍스트에 자동으로 포함합니다. CLI에서는 경로를 명시적으로 언급하거나 `/mention`과 `@` 경로 자동 완성을 사용해 파일을 첨부하세요.

Codex는 파일과 네트워크 접근을 제한하는 [샌드박스](/ko-KR/codex/sandboxing)에서
로컬 명령어를 실행합니다. 작업을 수행하려면 해당 경계를 벗어나야 하는 경우,
Codex는 계속 진행하기 전에 사용자의 승인 정책을 따릅니다.

### 코드베이스 설명하기

온보딩 중이거나 서비스를 인수받았거나 프로토콜, 데이터 모델, 요청 플로우를 이해하려는 경우에 사용하세요.

#### IDE 확장 워크플로우(로컬 탐색에 가장 빠른 방법)

1. 가장 관련성이 높은 파일을 여세요.
2. 관련 코드를 선택하세요(선택 사항이지만 권장합니다).
3. Codex에 프롬프트를 입력하세요:

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

검증:

- 검증할 수 있는 다이어그램이나 체크리스트를 요청하세요:

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### CLI 워크플로우(세션 기록과 셸 명령어가 필요할 때 적합)

1. 대화형 세션을 시작하세요:

   ```bash
   codex

2. 파일을 첨부하고(선택 사항) 프롬프트를 입력하세요:

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

컨텍스트 참고 사항:

- Composer에서 `@`을 사용하면 워크스페이스의 파일 경로를 삽입할 수 있고, `/mention`을 사용하면 특정 파일을 첨부할 수 있습니다.

### 버그 수정하기

로컬에서 재현 가능한 문제가 발생했을 때 사용하세요.

#### CLI 워크플로우(재현과 검증을 빠르게 반복)

1. 레포지토리 루트에서 Codex를 시작하세요:

   ```bash
   codex

2. Codex에 재현 절차와 문제가 의심되는 파일을 제공하세요:

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

컨텍스트 참고 사항:

- 사용자가 제공하는 정보: 재현 단계와 제약 조건(개괄적인 설명보다 더 중요합니다).
- Codex가 제공하는 정보: 명령어 출력, 확인한 호출 지점, 실행 중 발생한 스택 트레이스.

검증:

- Codex는 수정한 후 재현 단계를 다시 실행해야 합니다.
- 표준 검사 파이프라인이 있다면 실행하도록 요청하세요:

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### IDE 확장 워크플로우

1. 버그가 의심되는 파일과 가장 가까운 호출부를 여세요.
2. Codex에 프롬프트를 입력하세요:

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### 테스트 작성하기

테스트할 범위를 정확히 지정하고 싶을 때 사용하세요.

#### IDE 확장 워크플로우(선택 영역 기반)

1. 해당 함수가 있는 파일을 여세요.
2. 함수를 정의하는 줄을 선택하세요. 명령 팔레트에서 "Add to Codex Thread"를 선택해 해당 줄을 컨텍스트에 추가하세요.
3. Codex에 프롬프트를 입력하세요:

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

컨텍스트 참고 사항:

- "Add to Codex Thread" 명령어가 제공하는 항목: 선택한 줄(즉, "줄 번호" 범위)과 열려 있는 파일.

#### CLI 워크플로우(프롬프트에 경로와 줄 범위 명시)

1. Codex를 시작합니다:

   ```bash
   codex

2. 함수 이름을 포함해 프롬프트를 입력합니다:

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### 스크린샷으로 프로토타입 만들기

디자인 목업, 스크린샷 또는 UI 참고 자료를 실제로 작동하는 프로토타입으로 구현하려는 경우 사용합니다.

#### CLI 워크플로우(이미지 + 프롬프트)

1. 스크린샷을 로컬에 저장합니다(예: `./specs/ui.png`).
2. Codex를 실행합니다:

   ```bash
   codex

3. 이미지 파일을 터미널로 드래그하여 프롬프트에 첨부합니다.

4. 제약 조건과 구조를 지정하는 후속 프롬프트를 입력합니다:

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

컨텍스트 참고 사항:

- 이미지는 시각적 요구 사항을 전달하지만 구현 제약 조건(프레임워크, 라우팅, 컴포넌트 스타일)은 별도로 지정해야 합니다.
- 호버 상태, 유효성 검사 규칙, 키보드 상호작용처럼 이미지에 나타나지 않는 동작은 텍스트로 명시합니다.

검증:

- 허용되는 경우 Codex에 개발 서버를 실행하고 확인할 위치를 정확히 알려 달라고 요청합니다:

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### IDE 확장 워크플로우(이미지 + 기존 파일)

1. Codex 채팅에 이미지를 첨부합니다(드래그 앤 드롭 또는 붙여넣기).
2. Codex에 프롬프트를 입력합니다:

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### 실시간 업데이트로 UI를 반복 개선하기

Codex가 코드를 편집하는 동안 “디자인 → 수정 → 새로 고침 → 수정” 과정을 빠르게 반복하려는 경우 사용합니다.

#### CLI 워크플로우(Vite 실행 후 짧은 프롬프트로 반복 개선)

1. Codex를 시작합니다:

   ```bash
   codex

2. 별도의 터미널 창에서 개발 서버를 시작합니다:

   ```bash
   npm run dev

3. Codex에 변경을 요청합니다:

   ```text
   Propose 2-3 styling improvements for the landing page.

4. 방향을 하나 정하고 짧고 구체적인 프롬프트로 반복 개선합니다:

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. 특정 부분에 집중한 요청을 반복합니다:

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

검증:

- Codex가 코드를 업데이트하는 동안 브라우저에서 변경 사항을 확인합니다.
- 마음에 드는 변경 사항은 커밋하고 그렇지 않은 변경 사항은 되돌립니다.
- 편집 내용을 되돌리거나 수정했다면 Codex에 알려 다음 프롬프트를 처리할 때 해당 변경 사항을 덮어쓰지 않도록 합니다.

### 리팩터링을 클라우드에 위임하기

로컬 컨텍스트를 바탕으로 접근 방식을 설계한 다음, 병렬로 실행할 수 있는 클라우드 채팅에 시간이 오래 걸리는 구현 작업을 위임하려는 경우 사용합니다.

#### 로컬 계획 수립(IDE)

1. 변경 사항을 명확히 비교할 수 있도록 현재 작업을 커밋하거나 최소한 스태시해 둡니다.
2. Codex에 리팩터링 계획을 작성하도록 요청합니다. `$plan` 스킬을 사용할 수 있다면 명시적으로 호출합니다:

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. 계획을 검토하고 변경 사항을 조율합니다:

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

컨텍스트 참고 사항:

- Codex가 현재 코드를 로컬에서 살펴보며 진입점, 모듈 경계, 종속성 그래프 관련 단서를 파악할 수 있을 때 계획을 가장 효과적으로 수립할 수 있습니다.

#### 클라우드 위임(IDE → 클라우드)

1. 아직 설정하지 않았다면 [Codex 클라우드 환경](/ko-KR/codex/environments/cloud-environment)을 설정합니다.
2. 프롬프트 입력창 아래의 클라우드 아이콘을 클릭하고 클라우드 환경을 선택합니다.
3. 다음 프롬프트를 입력하면 Codex가 기존 채팅의 컨텍스트(계획 및 로컬 소스 코드 변경 사항 포함)를 이어받는 새 채팅을 클라우드에 만듭니다.

   ```text
   Implement Milestone 1 from the plan.

4. 클라우드 diff를 검토하고 필요하면 수정 작업을 반복합니다.

5. 클라우드에서 바로 PR을 만들거나 변경 사항을 로컬로 가져와 테스트하고 마무리합니다.

6. 계획의 다음 마일스톤도 같은 방식으로 진행합니다.

클라우드에 위임된 작업은 격리된 환경에서 실행됩니다. 환경에서 인터넷 액세스를 활성화하지 않으면
에이전트 단계에서는 인터넷 액세스가 꺼져 있습니다. 자세한 내용은
[클라우드 인터넷 액세스](/ko-KR/codex/cloud/internet-access)를 참조하세요.

### 로컬 코드 검토하기

커밋하거나 PR을 만들기 전에 한 번 더 검토받고 싶은 경우 사용합니다.

#### CLI 워크플로우(작업 트리 검토)

1. Codex를 시작합니다:

   ```bash
   codex

2. 검토 명령어를 실행합니다:

   ```text
   /review

3. 선택 사항: 중점적으로 검토할 부분을 지정하는 맞춤 지침을 제공합니다:

   ```text
   /review Focus on edge cases and security issues

검증:

- 검토 피드백에 따라 수정한 다음 `/review`를 다시 실행하여 문제가 해결되었는지 확인합니다.

### GitHub Pull Request 검토하기

브랜치를 로컬로 가져오지 않고 검토 피드백을 받고 싶은 경우 사용합니다.

이 기능을 사용하려면 먼저 레포지토리에서 Codex **코드 검토를** 사용 설정해야 합니다. [코드 검토](/ko-KR/codex/third-party/github)를 참조하세요.

#### GitHub 워크플로우(댓글 기반)

1. GitHub에서 Pull Request를 엽니다.
2. 중점적으로 검토할 영역을 명시하고 Codex를 태그하는 댓글을 남깁니다:

   ```text
   @codex review

3. 선택 사항: 더 구체적인 지침을 제공합니다.

   ```text
   @codex review for security vulnerabilities and security concerns

### 문서 업데이트하기

정확하고 명확하게 문서를 변경해야 할 때 사용합니다.

#### IDE 또는 CLI 워크플로우(로컬 편집 + 로컬 검증)

1. 변경할 문서 파일을 찾아 IDE에서 열거나 IDE 또는 CLI에서 `@`로 멘션합니다.
2. 작업 범위와 검증 요구 사항을 명시해 Codex에 요청하세요:

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Codex가 변경 사항의 초안을 작성하면 문서를 검토하고 필요에 따라 보완하세요.

검증:

- 렌더링된 페이지를 읽어 보세요.
