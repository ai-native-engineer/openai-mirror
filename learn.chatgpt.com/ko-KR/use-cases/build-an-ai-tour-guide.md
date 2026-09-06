<!-- source: https://learn.chatgpt.com/ko-KR/use-cases/build-an-ai-tour-guide -->

## 소개

누군가 어디로 이동하고 무엇을 선택해야 하는지 알려 주면 더 쉽게 익힐 수 있는 워크플로우가 있습니다. Codex로 사용자가 직접 조작하면서 웹 앱 사용법을 익힐 수 있도록 안내하는 투어를 만드세요.

앱의 컨트롤, 상태, 문서에 접근할 수 있는 WebMCP 도구가 있으면 Codex가 사용자에게 보이는 화면을 바탕으로 다음 안내를 선택할 수 있습니다. 서비스를 아직 연결하지 않은 사용자와 설정을 이미 마친 사용자는 시작해야 할 단계가 다릅니다.

## 사용 방법

1. Codex에서 앱의 레포지토리를 열고 서비스 연결이나 폴더 추가처럼 안내할 워크플로우 하나를 선택하세요.
2. 관련 문서를 제공하고 투어가 처리해야 할 초기 상태를 설명하세요.
3. 이 페이지의 시작 프롬프트를 실행해 투어 대상, UI 상태 도구, 앱 지침에 접근하는 기능을 추가하세요.
4. Codex가 앱의 WebMCP 도구를 호출할 수 있는 브라우저 환경에서 플로우를 테스트하세요. Codex에 안내를 요청한 다음 각 단계를 직접 수행하세요.

처음 만드는 투어는 범위를 좁게 잡으세요. 다른 워크플로우를 추가하기 전에 설정부터 완료까지 사용자를 안내할 수 있는지 확인하세요.

## 예시: Runme에서 Google Drive 폴더 추가하기

<a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a>에서는 사용자가 노트북을 편집하고, 파일 탐색기를 사용해 Google Drive 폴더를 추가하고 파일을 탐색합니다. 투어는 신규 사용자가 해당 컨트롤을 찾고 플로우를 익히도록 돕습니다.

Runme에 대해 자세히 알아보려면 <a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">OpenAI에서 Codex로 반복 업무 자동화하기</a>를 읽어 보세요.

Codex가 Runme의 컨트롤을 강조 표시하고 각 컨트롤의 용도를 설명하는 모습을 살펴보세요. 아래 스크린샷은 Google Drive 폴더 추가라는 특정 작업에 초점을 맞춘 별도의 투어를 보여 줍니다.

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    브라우저에서 동영상 재생을 지원하지 않습니다.
  </video>
</figure>

Google Drive 투어는 다음 요청으로 시작합니다:

### Google Drive 연결하기

Codex는 Google Drive가 연결되어 있는지 확인합니다. 연결되어 있지 않으면 **Google Drive 연결을** 강조 표시하고, 사용자에게 이를 선택해 연결을 완료하도록 요청합니다.

![Codex가 Runme에서 Google Drive 연결을 강조 표시하고 시작 방법을 설명합니다.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### 파일 탐색기 열기

연결이 완료되면 Codex가 사용자를 파일 탐색기로 안내합니다. 다음 안내는 업데이트된 앱 상태에 맞춰 제공됩니다.

![Codex가 Runme의 파일 탐색기를 여는 컨트롤을 강조 표시합니다.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### 폴더 추가하기

사용자가 도구 모음을 펼치면 Codex가 Google Drive 폴더를 추가하는 컨트롤을 강조 표시합니다. 사용자는 계속 직접 조작하며, 다음에 해당 컨트롤을 어디에서 찾을 수 있는지도 익힙니다.

![Codex가 Runme에서 Google Drive 폴더를 추가하는 컨트롤을 강조 표시합니다.](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## 사용자 안내에 필요한 컨텍스트를 Codex에 제공하기

Runme는 투어 대상, 애플리케이션 상태, 문서라는 세 가지 컨텍스트를 제공하도록 구현되어 있습니다. 아래 도구 이름은 Runme에서 사용하는 이름입니다. 동일한 역할을 앱에 맞게 적용하세요.

### 컨트롤을 찾을 수 있도록 만들기

각 투어 대상에 일관되게 유지되고 의미가 분명한 `data-tour-id` 값을 지정하고, 레이블과 설명을 추가하세요. Runme는 다음 세 가지 WebMCP 도구로 이 컨트롤들을 노출합니다:

- `listTargets` 도구는 등록된 대상과 ID, 레이블, 설명을 나열합니다.
- `showTourStep({ target, title?, message, placement? })` 도구는 대상을 강조 표시하고 설명을 보여 줍니다.
- `dismiss` 도구는 강조 표시를 해제합니다.

이렇게 하면 Codex가 사용자를 대신해 동작을 실행하지 않고도 컨트롤을 식별하고 설명할 수 있습니다.

### 상태를 읽고 사용자가 조작할 때까지 기다리기

Runme는 투어 관련 상태를 React 외부에서 관리하고 컨트롤러로 노출합니다. `getUiSnapshot` 도구는 로그인 상태를 포함한 현재 UI 상태를 제공합니다. Codex는 `waitForUiChange(...)`를 사용해 사용자가 강조 표시된 컨트롤을 선택하는 등의 변화를 기다릴 수 있습니다.

각 조작이 끝날 때마다 상태를 다시 읽도록 Codex에 요청하세요. 투어의 다음 단계로 넘어갈지는 Codex가 안내를 표시했는지가 아니라 앱에서 실제로 어떤 일이 일어났는지를 기준으로 결정해야 합니다.

### 앱과 함께 지침 제공하기

Runme는 애플리케이션에 Markdown 문서를 함께 포함하고 WebMCP로 제공합니다:

- `readInstructionsForAIAgents` 도구는 Codex가 앱과 도구를 어떻게 사용해야 하는지 설명합니다.
- `listDocumentation()` 도구는 사용 가능한 페이지와 각 페이지의 설명을 나열합니다.
- `getDocumentation({ name })` 도구는 선택한 페이지를 Markdown으로 반환합니다.

별도의 투어용 Codex 플러그인 없이도 투어 지침과 도구를 앱에 포함해 배포할 수 있습니다.

## 투어 검토하기

초기 상태를 바꿔 가며 같은 요청을 시도해 보세요. 투어가 이미 완료된 설정은 건너뛰고, 사용자가 조작할 때까지 기다리며, UI가 바뀌면 안내를 업데이트하는지 확인하세요.

단계가 취소되거나 컨트롤이 아직 보이지 않는 경우도 테스트하세요. Codex는 무엇이 빠져 있는지 설명하거나 진행 가능한 다음 단계를 선택해야 합니다. 버튼을 강조 표시했다는 이유만으로 동작이 성공했다고 말해서는 안 됩니다.

인증, 권한 확인, 사용자 동작은 기존 앱 플로우에서 처리하도록 유지하세요. 투어는 이러한 절차를 우회하지 않으면서 사용자가 인터페이스를 이해하도록 도와야 합니다.

## 추천 후속 요청

첫 번째 플로우가 작동하면 같은 채팅에서 이어서 요청하세요:

- "Google Drive가 이미 연결되어 있고 파일 탐색기가 닫혀 있는 상태에서 이 투어를 테스트해 주세요."
- "사용자가 한 단계를 취소한 뒤 투어를 계속해 달라고 요청하는 경우를 처리해 주세요."
- "기존 대상과 상태 도구를 재사용해 \[next workflow\]용 투어를 추가해 주세요."
