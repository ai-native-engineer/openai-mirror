<!-- source: https://learn.chatgpt.com/ko-KR/docs/codex-sdk -->

Codex CLI, IDE 확장 또는 Codex 클라우드로 Codex를 사용한다면 프로그래밍 방식으로도 제어할 수 있습니다.

다음과 같은 작업에는 SDK를 사용하세요:

- CI/CD 파이프라인의 일부로 Codex 제어하기
- Codex와 상호작용해 복잡한 엔지니어링 작업을 수행하는 자체 에이전트 만들기
- 내부 도구와 워크플로우에 Codex 통합하기
- 자체 애플리케이션에 Codex 통합하기

CI 작업을 비롯한 코딩 작업을 자동화하려면 Codex SDK를 사용하세요. 인증, 대화 기록, 승인, 스트리밍되는 에이전트 이벤트를 처리하는 맞춤형 클라이언트를 만들려면 [Codex App Server](/ko-KR/codex/app-server)를 사용하세요.

`codex mcp-server`는 사용 중단 예정(deprecated)입니다. 기존 통합을 위한 [MCP 서버 가이드](/ko-KR/codex/mcp-server)는 계속 제공됩니다.

베타 액세스 권한이 있고 구조화된
보안 이슈와 커버리지 정보를 제공하는 레포지토리 또는 변경 사항 스캔이 필요하다면 [Codex Security TypeScript
SDK](/ko-KR/codex/security/sdk)를 사용하세요.

## TypeScript 라이브러리

TypeScript 라이브러리를 사용하면 애플리케이션에서 로컬 Codex 스레드를 시작하거나 계속 실행하거나 재개할 수 있습니다.

이 라이브러리는 서버 측에서 사용하세요. Node.js 18 이상이 필요합니다.

### 설치

시작하려면 `npm`을 사용해 Codex SDK를 설치하세요:

```bash
npm install @openai/codex-sdk

### 사용법

Codex 스레드를 시작하고 프롬프트를 전달해 실행하세요.

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

같은 스레드에서 계속하려면 `run()`을 다시 호출하세요. 스레드 ID를 제공하면 이전 스레드를 재개할 수도 있습니다.

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

자세한 내용은 [TypeScript 레포지토리](https://github.com/openai/codex/tree/main/sdk/typescript)를 확인하세요.

## Python 라이브러리

Python SDK는 JSON-RPC를 통해 로컬 Codex app-server를 제어합니다. Python 3.10 이상이 필요합니다. 배포된 SDK 빌드에는 버전이 고정된 Codex CLI 런타임 종속성이 포함됩니다.

### 설치

SDK를 설치하려면 다음 명령어를 실행하세요:

```bash
pip install openai-codex

배포된 SDK 빌드는 버전이 고정된 런타임을 자동으로 사용합니다. 특정 로컬 Codex 실행 파일을 의도적으로 사용하려는 경우에만 `CodexConfig(codex_bin=...)` 설정을 전달하세요.

Python SDK는 안정 버전으로 제공됩니다. `pip install openai-codex`
명령어는 최신 안정 버전을 설치합니다. 더 새로운 프리릴리스 빌드를 사용하려면 `pip install --pre openai-codex`
명령어를 실행하세요.

### 사용법

Codex를 시작하고 스레드를 만든 다음 프롬프트를 실행하세요:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

애플리케이션이 이미 비동기 방식으로 동작한다면 `AsyncCodex`를 사용하세요:

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### 샌드박스 프리셋

스레드를 만들거나 이후 턴에 적용할 파일 시스템
접근 권한을 변경할 때도 동일한 `Sandbox` 프리셋을 사용하세요:

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

사용 가능한 프리셋은 다음과 같습니다:

- `Sandbox.read_only`: 파일 읽기는 허용하고 쓰기는 허용하지 않습니다.
- `Sandbox.workspace_write`: 파일 읽기를 허용하며, 워크스페이스와 쓰기 허용 루트로 설정된 경로 내에서는 파일 쓰기도 허용합니다.
- `Sandbox.full_access`: 파일 시스템 접근 제한 없이 실행합니다.

`sandbox=` 설정을 생략하면 app-server는 구성된 기본값을 사용합니다.
`run(...)` 또는 `turn(...)`에 전달한 샌드박스는 해당 턴과
같은 스레드의 이후 턴에 적용됩니다.

자세한 내용은 [Python 레포지토리](https://github.com/openai/codex/tree/main/sdk/python)를 확인하세요.
