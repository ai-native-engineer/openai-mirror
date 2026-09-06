<!-- source: https://learn.chatgpt.com/ko-KR/docs/app-server -->

Codex app-server는 Codex가 리치 클라이언트(예: Codex VS Code 확장 프로그램)를 구동하는 데 사용하는 인터페이스입니다. 자체 제품에 인증, 대화 기록, 승인, 에이전트 이벤트 스트리밍을 긴밀히 통합하려는 경우에 사용하세요. app-server 구현은 Codex GitHub 레포지토리([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server))에서 오픈 소스로 제공됩니다. 오픈 소스 Codex 구성 요소의 전체 목록은 [Open Source](/ko-KR/codex/open-source) 페이지를 참조하세요.

  작업을 자동화하거나 CI에서 Codex를 실행하는 경우에는
<a href="/codex/codex-sdk">Codex SDK</a>를 대신 사용하세요.

## CLI 터미널 UI 연결

원격 터미널 UI 모드를 사용하면 한 머신에서 app-server를 실행하고
다른 머신에서 Codex CLI 터미널 인터페이스로 연결할 수 있습니다. WebSocket 리스너를 시작하세요:

```bash
codex app-server --listen ws://127.0.0.1:4500

그런 다음 터미널 UI를 연결하세요:

```bash
codex --remote ws://127.0.0.1:4500

로컬이 아닌 연결에서는 WebSocket 인증을 구성하고
TLS로 연결을 보호하세요. 베어러 토큰을 환경 변수에 저장하고
명령줄에 토큰을 직접 넣는 대신 환경 변수 이름을 전달하세요:

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

`--remote` 옵션에는 `ws://`, `wss://`, `unix://` 및
`unix://PATH` 엔드포인트를 지정할 수 있습니다. 암호화되지 않은 WebSocket은 로컬호스트나
SSH 포트 포워딩 연결에만 사용하세요.

## 원격 Code Mode 호스트 연결

기본적으로 app-server는 로컬 Code Mode 호스트를 시작합니다.
대신 원격 호스트를 사용하려면 해당 호스트의 보안 WebSocket URL을 전달하세요:

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` 옵션은 app-server에서 Code Mode 호스트로 나가는
연결을 제어합니다. 클라이언트가 app-server에 연결하는 방식을 제어하는
`--listen` 옵션에는 영향을 주지 않습니다. 동일한 app-server 프로세스의 모든 스레드는
선택한 Code Mode 호스트 연결을 공유합니다.

원격 호스트에는 `wss://` 형식을 사용하세요. 로컬호스트 또는
SSH 포워딩 연결에만 `ws://` 형식을 사용하세요. app-server 명령어와 WebSocket 전송은
실험 단계이며 프로덕션 워크로드에는 공식적으로 지원되지 않습니다.

## 프로토콜

[MCP](https://modelcontextprotocol.io/)와 마찬가지로 `codex app-server`에서는 JSON-RPC 2.0 메시지를 사용한 양방향 통신을 지원합니다(전송 시 `"jsonrpc":"2.0"` 헤더는 생략됩니다).

지원되는 전송 방식:

- `stdio`(`--listen stdio://`, 기본값): 줄바꿈으로 구분된 JSON(JSONL).
- `websocket`(`--listen ws://IP:PORT`, 실험 단계이며 공식적으로 지원되지 않음): WebSocket 텍스트 프레임당
  JSON-RPC 메시지 하나.
- Unix 소켓(`--listen unix://` 또는 `--listen unix://PATH`): Codex의 기본 app-server 제어 소켓이나
  사용자 지정 Unix 소켓 경로를 통한 WebSocket 연결입니다.
  표준 HTTP Upgrade 핸드셰이크를 사용합니다.
- `off`(`--listen off`): 로컬 전송 방식을 노출하지 않습니다.

`--listen ws://IP:PORT` 설정으로 실행하면 동일한 리스너가
기본 HTTP 상태 확인 프로브도 제공합니다:

- 리스너가 새 연결을 수락하기 시작하면 `GET /readyz` 요청의 응답은 `200 OK`입니다.
- 요청에 `Origin` 헤더가 없으면 `GET /healthz` 요청의 응답은
  `200 OK`입니다.
- `Origin` 헤더가 있는 요청은 `403 Forbidden` 응답으로 거부됩니다.

WebSocket 전송은 실험 단계이며 공식적으로 지원되지 않습니다.
`ws://127.0.0.1:PORT` 같은 로컬 리스너는 로컬호스트와 SSH 포트 포워딩
워크플로우에 적합합니다. 현재 롤아웃 기간에는 루프백이 아닌 WebSocket 리스너가
기본적으로 인증되지 않은 연결을 허용하므로, 원격으로 노출하기 전에
WebSocket 인증을 구성하세요.

지원되는 WebSocket 인증 플래그:

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

서명된 베어러 토큰을 사용할 때는 `--ws-issuer`, `--ws-audience`,
`--ws-max-clock-skew-seconds`도 설정할 수 있습니다. 클라이언트는 WebSocket 핸드셰이크 중에
`Authorization: Bearer <token>` 형식으로 자격 증명을 제공하며, app-server는 JSON-RPC
`initialize` 요청 전에 반드시 인증을 수행합니다.

명령줄에 베어러 토큰 원문을 전달하기보다는 `--ws-token-file` 사용을 권장합니다.
`--ws-token-sha256` 옵션은 클라이언트가 엔트로피가 높은 토큰의 원문을
별도의 로컬 시크릿 저장소에 보관하는 경우에만 사용하세요. 해시는 검증용일 뿐이며,
클라이언트에는 여전히 원본 토큰이 필요합니다.

WebSocket 모드에서 app-server는 용량이 제한된 큐를 사용합니다. 요청 수신 큐가
가득 차면 서버는 새 요청을 거부하며 JSON-RPC 오류 코드는 `-32001`, 메시지는
`"Server overloaded; retry later."`입니다. 클라이언트는 지수적으로 증가하는 지연과
지터를 적용해 재시도해야 합니다.

## 메시지 스키마

요청에 포함되는 필드는 `method`, `params`, `id`입니다:

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

응답에는 요청과 동일한 `id`와 함께 `result` 또는 `error` 중 하나가 포함됩니다:

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

알림은 `id` 없이 `method`와 `params`만 사용합니다:

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

CLI에서 TypeScript 스키마 또는 JSON Schema 번들을 생성할 수 있습니다. 각 출력은 실행한 Codex 버전에 맞춰 생성되므로, 생성된 아티팩트는 해당 버전과 정확히 일치합니다:

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## 시작하기

1. `codex app-server`(기본 stdio 전송),
`codex app-server --listen ws://127.0.0.1:4500`(TCP WebSocket) 또는
`codex app-server --listen unix://`(기본 Unix 소켓)으로 서버를 시작하세요.
2. 선택한 전송 방식으로 클라이언트를 연결한 다음 `initialize` 요청에 이어 `initialized` 알림을 보내세요.
3. 스레드와 턴을 시작한 다음 활성 전송 스트림에서 계속 알림을 읽으세요.

예시(Node.js / TypeScript):

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## 핵심 구성 요소

- **스레드**: 사용자와 Codex 에이전트 간의 대화입니다. 스레드에는 턴이 포함됩니다.
- **턴**: 하나의 사용자 요청과 그에 이어지는 에이전트 작업입니다. 턴에는 항목이 포함되며 업데이트를 점진적으로 스트리밍합니다.
- **항목**: 입력 또는 출력의 단위입니다(사용자 메시지, 에이전트 메시지, 명령어 실행, 파일 변경, 도구 호출 등).

스레드 API로 대화를 생성하거나 보관하고 대화 목록을 조회하세요. 턴 API로 대화를 진행하고 턴 알림을 통해 진행 상황을 스트리밍하세요.

## 수명 주기 개요

- **연결마다 한 번 초기화**: 전송 연결을 연 직후 클라이언트 메타데이터와 함께 `initialize` 요청을 보내고, 이어서 `initialized` 알림을 전송하세요. 서버는 이 핸드셰이크가 완료되기 전에 해당 연결로 들어오는 모든 요청을 거부합니다.
- **스레드 시작(또는 재개)**: 새 대화를 시작하려면 `thread/start` 메서드를, 기존 대화를 계속하려면 `thread/resume` 메서드를, 기록을 새 스레드 ID로 분기하려면 `thread/fork` 메서드를 호출하세요.
- **턴 시작**: 대상 `threadId` 및 사용자 입력을 지정해 `turn/start` 메서드를 호출하세요. 선택적 필드로 모델, 성격, `cwd`, 샌드박스 정책 등을 재정의할 수 있습니다.
- **활성 턴 조정**: 새 턴을 만들지 않고 현재 진행 중인 턴에 사용자 입력을 추가하려면 `turn/steer` 메서드를 호출하세요.
- **이벤트 스트리밍**: `turn/start` 호출 후 stdout에서 `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, 도구 진행 상황 및 기타 업데이트 알림을 계속 읽으세요.
- **턴 완료**: 모델이 작업을 마치거나 `turn/interrupt` 호출로 턴이 취소되면 서버가 최종 상태를 담은 `turn/completed` 알림을 보냅니다.

## 초기화

클라이언트는 전송 연결마다 다른 메서드를 호출하기 전에 `initialize` 요청을 한 번만 보내고, 이어서 `initialized` 알림으로 이를 확인해야 합니다. 초기화 전에 보낸 요청에는 `Not initialized` 오류가 반환되고, 같은 연결에서 `initialize` 호출을 반복하면 `Already initialized`가 반환됩니다.

서버는 업스트림 서비스에 제공할 사용자 에이전트 문자열과 런타임 대상을 설명하는 `platformFamily` 및 `platformOs` 값을 반환합니다. 통합을 식별할 수 있도록 `clientInfo` 값을 설정하세요.

`initialize.params.capabilities`에서는 다음 클라이언트 기능도 지원합니다:

- `optOutNotificationMethods` - 이 연결에서 수신하지 않을 알림의 정확한 메서드 이름입니다.
  이름은 완전히 일치해야 하며 와일드카드나 접두사 매칭은 지원하지 않습니다.
  알 수 없는 이름도 허용되지만 무시됩니다.
- `requestAttestation` - 서버에서 시작하는 `attestation/generate` 요청을 받도록 설정합니다.
  업스트림 서비스에 증명을 제공하는 데스크톱 호스트는
  불투명한 `{ "token": "..." }` 값으로 응답합니다.
- `mcpServerOpenaiFormElicitation` - 다운스트림 MCP 서버가 `mcpServer/elicitation/request`의
  OpenAI 확장 폼 베리언트를 보내도록 허용합니다.

**중요**: 컴플라이언스 로그 플랫폼에서 클라이언트를 식별하려면 `clientInfo.name` 값을 사용하세요. 엔터프라이즈용 새 Codex 통합을 개발하는 경우 알려진 클라이언트 목록에 추가할 수 있도록 OpenAI에 문의하세요. 자세한 내용은 [Codex 로그 참조 자료](https://chatgpt.com/public/admin/api-reference#tag/Codex)를 확인하세요.

예시(Codex VS Code 확장 프로그램에서 발췌):

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

알림 수신 제외 예시:

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## 실험적 API 사용 설정

일부 app-server 메서드와 필드는 `experimentalApi` 기능을 활성화한 경우에만 사용할 수 있도록 설계되어 있습니다.

- 안정적인 API만 사용하려면 `capabilities`를 생략하거나 `experimentalApi`를 `false`로 설정하세요. 이 경우 서버는 실험적 메서드와 필드를 거부합니다.
- 실험적 메서드와 필드를 활성화하려면 `capabilities.experimentalApi` 값을 `true`로 설정하세요.

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

클라이언트가 실험적 API 사용을 활성화하지 않고 실험적 메서드나 필드를 보내면 app-server는 다음과 같이 거부합니다:

`<descriptor> requires experimentalApi capability`

## API 개요

- `thread/start` - 새 스레드를 생성하고 `thread/started`를 내보내며, 클라이언트가 해당 스레드의 턴/항목 이벤트를 자동으로 구독하도록 설정합니다.
- `thread/resume` - 기존 스레드를 ID로 다시 열어 이후 `turn/start` 호출 시 해당 스레드에 턴을 추가하도록 합니다.
- `thread/fork` - 저장된 기록을 복사해 새 ID의 스레드로 포크합니다. `lastTurnId`를 전달하면 해당 턴까지의 기록을 복사하고 이후 턴은 제외하며, `ephemeral: true`를 전달하면 메모리 내 포크를 생성합니다. 새 스레드에 대해 `thread/started`를 내보내며, 반환된 스레드에는 값이 있는 경우 `forkedFromId`가 포함됩니다.
- `thread/read` - 저장된 스레드를 재개하지 않고 ID로 읽습니다. `includeTurns`를 설정하면 전체 턴 기록을 반환합니다. 반환된 `thread` 객체에는 런타임 `status`가 포함됩니다.
- `thread/list` - 저장된 스레드 로그를 페이지 단위로 조회합니다. 커서 기반 페이지네이션과 `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` 필터 및 실험적 필터인 `parentThreadId` 또는 `ancestorThreadId`를 지원합니다. 반환된 `thread` 객체에는 런타임 `status`가 포함됩니다.
- `thread/turns/list` - 실험적 기능입니다. 저장된 스레드를 재개하지 않고 턴 기록을 페이지 단위로 조회합니다. `itemsView` 값으로 턴 항목을 생략할지, 요약할지, 모두 로드할지 제어합니다.
- `thread/items/list` - 실험적 기능입니다. 영구 저장된 스레드 항목을 페이지 단위로 조회하며, 선택적으로 하나의 `turnId`에 해당하는 항목만 조회할 수 있습니다. 사용 중인 스레드 저장소가 항목 페이지네이션을 지원해야 합니다.
- `thread/loaded/list` - 현재 메모리에 로드된 스레드 ID를 나열합니다.
- `thread/name/set` - 로드된 스레드나 영구 저장된 롤아웃에서 사용자에게 표시되는 스레드 이름을 설정하거나 업데이트하고 `thread/name/updated`를 내보냅니다.
- `thread/goal/set` - 스레드의 목표를 설정하고 `thread/goal/updated`를 내보냅니다.
- `thread/goal/get` - 스레드의 현재 목표를 읽습니다.
- `thread/goal/clear` - 스레드의 목표를 지우고 `thread/goal/cleared`를 내보냅니다.
- `thread/metadata/update` - 영구 저장된 `gitInfo`와 `isPinned`를 포함해 SQLite에 저장된 스레드 메타데이터를 패치합니다.
- `thread/archive` - 스레드의 로그 파일을 보관 디렉터리로 이동하고, 해당 스레드에서 생성된 하위 스레드 중 아직 보관되지 않은 스레드의 로그도 보관하려고 시도합니다. 성공하면 `{}`를 반환하고, 보관된 각 스레드에 대해 `thread/archived`를 내보냅니다.
- `thread/delete` - 영구 저장된 활성 스레드 또는 보관된 스레드와 해당 스레드에서 생성된 모든 하위 스레드를 영구 삭제합니다. 성공하면 `{}`를 반환하고, 삭제된 각 스레드에 대해 `thread/deleted`를 내보냅니다.
- `thread/unsubscribe` - 이 연결의 스레드 턴/항목 이벤트 구독을 해제합니다. 이 연결이 마지막 구독자였다면 서버는 구독자가 없고 활동도 없는 상태가 유예 기간 동안 지속된 후 스레드를 언로드하고 `thread/closed`를 내보냅니다.
- `thread/unarchive` - 보관된 스레드 롤아웃을 활성 세션 디렉터리로 복원합니다. 복원된 `thread`를 반환하고 `thread/unarchived`를 내보냅니다.
- `thread/status/changed` - 로드된 스레드의 런타임 `status`가 변경될 때 내보내는 알림입니다.
- `thread/compact/start` - 스레드의 대화 기록에 대한 컨텍스트 압축을 시작합니다. 즉시 `{}`를 반환하며, 진행 상황은 `turn/*` 및 `item/*` 알림으로 스트리밍됩니다.
- `thread/shellCommand` - 사용자가 요청한 셸 명령어를 해당 스레드에서 실행합니다. 샌드박스 밖에서 전체 권한으로 실행되며 스레드의 샌드박스 정책을 상속하지 않습니다.
- `thread/backgroundTerminals/clean` - 스레드에서 실행 중인 모든 백그라운드 터미널을 중지합니다. 실험적 기능이며 `capabilities.experimentalApi`가 필요합니다.
- `thread/backgroundTerminals/list` - 로드된 스레드에서 실행 중인 백그라운드 터미널을 나열합니다. 실험적 기능이며 `capabilities.experimentalApi`가 필요합니다.
- `thread/backgroundTerminals/terminate` - app-server의 `processId`를 사용해 실행 중인 백그라운드 터미널 하나를 종료합니다. 실험적 기능이며 `capabilities.experimentalApi`가 필요합니다.
- `thread/rollback` - 사용 중단 예정(deprecated)입니다. 메모리 내 컨텍스트에서 마지막 N개 턴을 제거하고 롤백 마커를 영구 저장한 다음, 업데이트된 `thread`를 반환합니다.
- `turn/start` - 스레드에 사용자 입력이나 단독으로 제공된 도구 출력을 추가하고 Codex 응답 생성을 시작합니다. 초기 `turn`을 반환하고 이벤트를 스트리밍합니다. `collaborationMode`에서 `settings.developer_instructions: null` 값은 “선택한 모드의 기본 제공 지침을 사용한다”는 의미입니다.
- `thread/inject_items` - 사용자 턴을 시작하지 않고, 로드된 스레드에서 모델이 볼 수 있는 기록에 원시 Responses API 항목을 추가합니다.
- `turn/steer` - 스레드에서 현재 진행 중인 턴에 사용자 입력을 추가하고, 수락된 `turnId`를 반환합니다.
- `turn/interrupt` - 진행 중인 턴의 취소를 요청합니다. 성공하면 `{}`를 반환하고 턴은 `status: "interrupted"` 상태로 종료됩니다.
- `review/start` - 스레드에 대한 Codex 리뷰어를 실행하고 `enteredReviewMode` 및 `exitedReviewMode` 항목을 내보냅니다.
- `command/exec` - 스레드나 턴을 시작하지 않고 서버 샌드박스에서 단일 명령어를 실행합니다.
- `command/exec/write` - 실행 중인 `command/exec` 세션의 `stdin`에 바이트를 쓰거나 `stdin`을 닫습니다.
- `command/exec/resize` - 실행 중인 PTY 기반 `command/exec` 세션의 크기를 조정합니다.
- `command/exec/terminate` - 실행 중인 `command/exec` 세션을 중지합니다.
- `command/exec/outputDelta` (알림) - 스트리밍 중인 `command/exec` 세션에서 나오는 base64로 인코딩된 stdout/stderr 청크를 전달합니다.
- `process/spawn` - Codex 샌드박스 밖에서 프로세스 세션을 명시적으로 시작합니다. 실험적 기능이며 `capabilities.experimentalApi`가 필요합니다.
- `process/writeStdin` - 실행 중인 `process/spawn` 세션의 stdin에 바이트를 쓰거나 stdin을 닫습니다. 실험적 기능입니다.
- `process/resizePty` - 실행 중인 PTY 기반 프로세스 세션의 크기를 조정합니다. 실험적 기능입니다.
- `process/kill` - 실행 중인 프로세스 세션을 종료합니다. 실험적 기능입니다.
- `process/outputDelta` 및 `process/exited` (알림) - 스트리밍되는 프로세스 출력과 프로세스 종료 상태를 전달합니다. 실험적 기능입니다.
- `model/list` - 사용 가능한 모델을 추론 수준 옵션, 선택적 `upgrade`, `inputModalities`와 함께 나열합니다. `includeHidden: true`를 설정하면 `hidden: true`인 항목도 포함됩니다.
- `modelProvider/capabilities/read` - 모델/제공자 조합별로 제공자가 지원하는 기능 범위를 읽습니다.
- `experimentalFeature/list` - 수명 주기 단계 메타데이터가 포함된 기능 플래그를 나열하며 커서 기반 페이지네이션을 지원합니다.
- `experimentalFeature/enablement/set` - `apps`와 `plugins` 등 지원되는 기능 키의 메모리 내 런타임 설정을 패치합니다.
- `environment/info` - 실험적 기능입니다. 설정된 실행 환경에 연결해 해당 환경의 셸과 기본 작업 디렉터리를 반환합니다.
- `permissionProfile/list` - 베타 권한 프로필과 현재 적용되는 요구 사항에 따른 각 프로필의 허용 여부를 나열합니다. 커서 기반 페이지네이션을 지원합니다.
- `collaborationMode/list` - 협업 모드 프리셋을 나열합니다. 실험적 기능이며 페이지네이션은 지원하지 않습니다.
- `skills/list` - 하나 이상의 `cwd` 값에 대한 스킬을 나열합니다. `forceReload`를 지원하며 `perCwdExtraUserRoots`도 선택적으로 사용할 수 있습니다.
- `skills/extraRoots/set` - 독립형 스킬을 찾는 데 사용하는 프로세스 수준의 추가 루트를 교체하되 영구 저장하지 않습니다.
- `skills/changed` (알림) - 감시 중인 로컬 스킬 파일이 변경될 때 내보냅니다.
- `hooks/list` - 하나 이상의 `cwd` 값을 기준으로 찾은 수명 주기 훅을 나열합니다.
- `marketplace/add` - 원격 플러그인 마켓플레이스를 추가하고 사용자의 마켓플레이스 설정에 영구 저장합니다.
- `marketplace/remove` - 설정된 마켓플레이스를 제거하고, 설치된 마켓플레이스 루트가 있으면 함께 제거합니다.
- `marketplace/upgrade` - 설정된 Git 마켓플레이스를 새로 고칩니다. 마켓플레이스 이름을 생략하면 설정된 모든 Git 마켓플레이스를 새로 고칩니다.
- `plugin/list` - 개발 중입니다. 발견된 플러그인 마켓플레이스와 플러그인 상태를 나열합니다. 여기에는 설치/인증 정책 메타데이터, 마켓플레이스 로드 오류, 추천 플러그인 ID, 로컬, Git, 패키지 레지스트리 또는 원격 플러그인 소스의 메타데이터가 포함됩니다. 요약에는 원격 `version`, 로컬 `localVersion`, 구조화된 라이트/다크 아이콘과 함께 `installPolicySource`도 포함될 수 있습니다. 이 필드는 현재 원격 항목에서 `null`, `WORKSPACE_SETTING` 또는 `IMPLICIT_CANONICAL_APP` 값을 가질 수 있습니다. 아직 프로덕션 클라이언트에서 이 메서드를 호출하지 마세요.
- `plugin/read` - 개발 중입니다. 마켓플레이스 경로 또는 원격 마켓플레이스 이름을 플러그인 이름과 함께 지정해 플러그인 하나를 읽습니다. 함께 제공되는 스킬, 앱, MCP 서버 이름이 포함되며, 원격 카탈로그에서 제공하는 경우 원격 플러그인의 `shareUrl`도 포함됩니다. 아직 프로덕션 클라이언트에서 이 메서드를 호출하지 마세요.
- `plugin/install` - 개발 중입니다. 마켓플레이스 경로나 원격 마켓플레이스 이름을 사용해 플러그인을 설치합니다. 아직 프로덕션 클라이언트에서 이 메서드를 호출하지 마세요.
- `plugin/uninstall` - 개발 중입니다. 설치된 플러그인을 제거합니다. 아직 프로덕션 클라이언트에서 이 메서드를 호출하지 마세요.
- `plugin/skill/read` - 원격 마켓플레이스, 플러그인 ID, 스킬 이름을 지정해 원격 플러그인 스킬의 Markdown을 필요할 때 읽습니다.
- `app/installed` - 설치된 앱의 런타임 상태를 읽습니다. 여기에는 각 앱에 실제로 적용된 활성화 상태와 호출 가능 상태가 포함됩니다.
- `app/list` - 사용 가능한 앱(커넥터)을 나열합니다. 페이지네이션을 지원하며 접근 가능 여부 및 활성화 상태 메타데이터를 포함합니다.
- `app/read` - 특정 앱 ID에 대한 메타데이터를 가져오며, 선택적으로 표시 전용 도구 요약도 가져옵니다.
- `skills/config/write` - 경로를 기준으로 스킬을 활성화하거나 비활성화합니다.
- `mcpServer/oauth/login` - 구성된 MCP 서버의 OAuth 로그인을 시작합니다. 권한 부여 URL을 반환하고 완료되면 `mcpServer/oauthLogin/completed` 알림을 보냅니다.
- `tool/requestUserInput` - 도구 호출을 위해 사용자에게 1~3개의 짧은 질문을 표시합니다(실험적). 질문에 `isOther`를 설정해 자유 입력 옵션을 제공할 수 있습니다.
- `mcpServer/elicitation/request` (서버 요청) - MCP 서버가 요청한 구조화된 양식 입력이나 URL 플로우 확인을 클라이언트에 요청합니다.
- `item/permissions/requestApproval` (서버 요청) - 기본 제공 `request_permissions` 도구가 요청한 네트워크 또는 파일 시스템 권한 중 일부를 부여하도록 클라이언트에 요청합니다.
- `config/mcpServer/reload` - 디스크에서 MCP 서버 구성을 다시 로드하고, 로드된 스레드의 새로 고침 작업을 대기열에 추가합니다.
- `mcpServerStatus/list` - MCP 서버, 도구, 리소스, 인증 상태를 나열합니다(커서 및 개수 제한 기반 페이지네이션). 전체 데이터를 가져오려면 `detail: "full"`로, 리소스를 제외하려면 `detail: "toolsAndAuthOnly"`로 설정하세요.
- `mcpServer/resource/read` - 초기화된 MCP 서버를 통해 MCP 리소스 하나를 읽습니다.
- `mcpServer/tool/call` - 스레드에 구성된 MCP 서버의 도구를 호출합니다.
- `mcpServer/startupStatus/updated` (알림) - 로드된 스레드에 구성된 MCP 서버의 시작 상태가 변경되면 전송됩니다.
- `windowsSandbox/setupStart` - `elevated` 또는 `unelevated` 모드의 Windows 샌드박스 설정을 시작합니다. 빠르게 반환한 뒤 나중에 `windowsSandbox/setupCompleted` 알림을 보냅니다.
- `feedback/upload` - 피드백 보고서를 제출합니다(분류 + 선택적 사유/로그 + 대화 ID, 선택적 `extraLogFiles` 첨부 파일 포함).
- `config/read` - 디스크에 저장된 구성의 계층별 우선순위를 적용해 최종 적용 구성을 가져옵니다.
- `externalAgentConfig/detect` - `includeHome` 및 선택적 `cwds` 매개변수를 사용해 마이그레이션 가능한 외부 에이전트 아티팩트를 감지합니다. 감지된 각 항목에는 `cwd`가 포함되며, 홈 디렉터리의 경우 값은 `null`입니다.
- `externalAgentConfig/import` - `cwd` 값(홈 디렉터리의 경우 `null`)이 포함된 `migrationItems`를 명시적으로 전달해 선택한 외부 에이전트 마이그레이션 항목을 적용합니다. 지원되는 항목 유형에는 구성, 스킬, `AGENTS.md`, 플러그인, MCP 서버 구성, 하위 에이전트, 훅, 명령, 세션이 포함됩니다. 가져올 항목이 있으면 작업 완료 과정에서 `externalAgentConfig/import/progress` 및 `externalAgentConfig/import/completed` 알림을 보냅니다. 플러그인과 세션 가져오기는 비동기적으로 완료될 수 있습니다.
- `config/value/write` - 디스크에 있는 사용자의 `config.toml`에 구성 키/값 하나를 씁니다.
- `config/batchWrite` - 디스크에 있는 사용자의 `config.toml`에 구성 변경 사항을 원자적으로 적용합니다.
- `configRequirements/read` - `requirements.toml` 및/또는 MDM에서 요구 사항을 가져옵니다. 여기에는 정확히 지정된 관리형 구성, 허용 목록, 고정된 `featureRequirements`, 네트워크 요구 사항이 포함됩니다. 설정된 요구 사항이 없으면 `null`을 반환합니다.
- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch` 및 `fs/changed` (알림) - app-server v2 파일 시스템 API를 통해 절대 파일 시스템 경로를 대상으로 작업합니다.

플러그인 요약에는 `source` 유니온 타입이 포함됩니다. 로컬 플러그인은
`{ "type": "local", "path": ... }`, Git 기반 마켓플레이스 항목은
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
패키지 레지스트리 항목은
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }`, 원격 카탈로그 항목은
`{ "type": "remote" }` 값을 반환합니다. 원격 전용 카탈로그 항목의 경우
`PluginMarketplaceEntry.path` 값이 `null`일 수 있습니다. 해당 플러그인을
읽거나 설치할 때는 `marketplacePath` 대신
`remoteMarketplaceName`을 전달하세요.

## 모델

### 모델 목록 조회(`model/list`)

모델 또는 성격 선택기를 렌더링하기 전에 `model/list`를 호출해 사용 가능한 모델과 각 모델의 기능을 확인하세요.

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

각 모델 항목에는 다음이 포함될 수 있습니다:

- `supportedReasoningEfforts` - 모델이 지원하는 추론 수준 옵션입니다.
- `defaultReasoningEffort` - 클라이언트에 권장하는 기본 추론 수준입니다.
- `upgrade` - 클라이언트의 마이그레이션 프롬프트에 사용할 권장 업그레이드 모델 ID입니다(선택 사항).
- `upgradeInfo` - 클라이언트의 마이그레이션 프롬프트에 사용할 업그레이드 메타데이터입니다(선택 사항).
- `hidden` - 기본 선택기 목록에서 모델이 숨겨져 있는지 여부입니다.
- `inputModalities` - 모델이 지원하는 입력 유형입니다(예: `text`, `image`).
- `supportsPersonality` - 모델이 `/personality` 같은 성격별 지침을 지원하는지 여부입니다.
- `isDefault` - 권장 기본 모델인지 여부입니다.

`model/list`는 기본적으로 선택기에 표시되는 모델만 반환합니다. 전체 목록을 가져와 `hidden` 값을 기준으로 클라이언트 측에서 필터링하려면 `includeHidden: true`로 설정하세요.

`inputModalities` 값이 없는 경우(이전 모델 카탈로그) 하위 호환성을 위해 해당 값을 `["text", "image"]`로 간주하세요.

### 실험적 기능 목록 조회(`experimentalFeature/list`)

이 엔드포인트를 사용해 기능 플래그와 해당 메타데이터, 수명 주기 단계를 확인하세요:

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` 값은 `beta`, `underDevelopment`, `stable`, `deprecated`, `removed` 중 하나일 수 있습니다. 베타가 아닌 플래그에서는 `displayName`, `description`, `announcement` 값이 `null`일 수 있습니다.

### 실행 환경 확인(실험적)

구성된 원격 환경에서 작업을 시작하기 전에 `environment/info`로 해당 환경을
확인하세요. 이 메서드에는 `capabilities.experimentalApi = true` 설정이 필요합니다.

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` 값은 `null`일 수 있습니다. 값이 있으면 정규 형식의 `file:` URI이며,
해당 환경 고유의 경로 구문을 사용합니다. 알 수 없는 환경 ID나 연결 실패 또는
프로토콜 오류가 발생하면 요청 오류가 반환됩니다.

## 스레드

- `thread/read`는 저장된 스레드를 구독하지 않고 읽습니다. 턴을 포함하려면 `includeTurns`를 설정하세요.
- `thread/turns/list`는 저장된 스레드를 재개하지 않고 턴 기록을 페이지 단위로 조회하는
  실험적 메서드입니다. `itemsView`로 턴 항목을 생략할지, 요약할지,
  또는 전체를 로드할지 선택하세요.
- `thread/items/list`는 영구 저장된 스레드 항목을 페이지 단위로 조회하는 실험적 메서드입니다. 필요하면 하나의 턴으로 범위를 제한할 수 있습니다.
- `thread/list`는 커서 페이지네이션과 `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly`, `searchTerm` 및 실험적 `parentThreadId` 또는 `ancestorThreadId` 필터링을 지원합니다.
- `thread/loaded/list`는 현재 메모리에 있는 스레드 ID를 반환합니다.
- `thread/archive`는 스레드의 영구 저장된 JSONL 로그를 보관 디렉터리로 옮기고, 이 스레드에서 생성된 하위 스레드 중 아직 보관되지 않은 스레드의 로그도 보관하려고 시도합니다.
- `thread/delete`는 영구 저장된 스레드(활성 또는 보관 상태)와 이 스레드에서 생성된 하위 스레드를 영구 삭제합니다.
- `thread/metadata/update`는 영구 저장된 `gitInfo` 및 `isPinned` 값을 포함한 스레드 메타데이터를 패치합니다.
- `thread/unsubscribe`는 로드된 스레드에 대한 현재 연결의 구독을 해제하며, 비활성 유예 기간이 지나면 `thread/closed` 알림을 보낼 수 있습니다.
- `thread/unarchive`는 보관된 스레드 롤아웃을 활성 세션 디렉터리로 복원합니다.
- `thread/compact/start`는 컨텍스트 압축을 시작하고 즉시 `{}`를 반환합니다.
- `thread/rollback`은 사용 중단 예정(deprecated)입니다. 메모리 내 컨텍스트에서 마지막 N개 턴을 제거하고 스레드의 영구 저장된 JSONL 로그에 롤백 마커를 기록합니다.
- `thread/inject_items`는 사용자 턴을 시작하지 않고, 로드된 스레드에서 모델이 볼 수 있는 기록에 원시 Responses API 항목을 추가합니다.

### 스레드 시작 또는 재개

새 Codex 대화가 필요하면 새 스레드를 시작하세요.

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName`은 선택 사항입니다. app-server가 스레드 수준 메트릭에 연동 서비스의 이름을 태그하도록 하려면 이 값을 설정하세요.

`thread/start`, `thread/resume`, `thread/fork` 메서드는 로드된 지침 파일 경로의 배열인
`instructionSources`를 반환합니다. 각 경로는
원격 환경 여부와 관계없이 해당 경로의 원본 환경에서 사용하는
고유한 절대 경로 구문을 따릅니다.

실험적 기능을 사용하는 클라이언트는 `thread/start`의 `historyMode`를 `"legacy"`(기본값)
또는 `"paginated"`로 설정할 수 있습니다. 페이지네이션 방식의 스레드 생성은 아직 지원되지 않으며
JSON-RPC 오류 `-32601`가 반환됩니다. app-server는 기존 페이지네이션 레코드를 나열하고 요약을 읽을 수 있지만,
전체 기록 읽기, 턴 페이지네이션, 재개 요청은
페이지네이션 기록이 지원될 때까지 거부됩니다.

`capabilities.experimentalApi`를 활성화한 베타 클라이언트는 이름이 지정된
권한 프로필 ID를 기존 `sandbox` 필드 대신 `permissions`에 전달할 수 있습니다.
`permissions`와 `sandbox`는 함께 보내지 마세요.
`permissionProfile/list`에 프로젝트의 `cwd`를 전달하면 사용 가능한 프로필과
관리형 요구 사항에 따라 각 프로필이 허용되는지 확인할 수 있습니다.

`thread.sessionId`는 현재 활성 세션 트리의 루트를 식별합니다. 루트 스레드는
자체 스레드 ID를 세션 ID로 사용하고, 포크된 스레드는 원본 루트의 세션 ID를
유지합니다. 클라이언트는 스레드 ID에서 세션 ID를 추론하지 말고
`thread.sessionId`에서 읽어야 합니다.

저장된 세션을 계속하려면 `thread/resume`을 호출할 때 이전에 기록한 `thread.id`를 전달하세요. 응답 구조는 `thread/start`의 응답과 같습니다. `thread/start`에서 지원하는 구성 재정의 값도 동일하게 전달할 수 있습니다(예: `personality`):

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

스레드를 재개하는 것만으로는 `thread.updatedAt` 값이나 롤아웃 파일의 수정 시간이 업데이트되지 않습니다. 타임스탬프는 턴을 시작할 때 업데이트됩니다.

구성에서 활성화된 MCP 서버를 `required`로 지정했는데 해당 서버가 초기화에 실패하면, `thread/start` 및 `thread/resume` 호출은 해당 서버 없이 계속 진행하지 않고 실패합니다.

`dynamicTools`는 `thread/start`의 실험적 필드로, `capabilities.experimentalApi = true` 설정이 필요합니다. Codex는 이러한 동적 도구를 스레드의 롤아웃 메타데이터에 저장하며, 새 동적 도구를 제공하지 않으면 `thread/resume` 호출 시 복원합니다.

롤아웃에 기록된 모델과 다른 모델로 재개하면 Codex가 경고를 내보내고 다음 턴에 일회성 모델 전환 지침을 적용합니다.

### 스레드 목표 관리

`thread/goal/set`, `thread/goal/get`, `thread/goal/clear`를 사용해
TUI의 `/goal`에 표시되는 것과 동일한 저장된 목표 상태를 관리하세요.

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

목표 내용은 비어 있으면 안 되며 최대 4,000자까지 허용됩니다. 새 목표 내용을
제공하면 기존 목표가 대체되고 사용량 집계가 초기화됩니다. 종료 상태가 아닌 현재 목표의 내용을
다시 제공하거나 `objective`를 생략하면 사용 이력은 유지하면서
상태 또는 토큰 예산을 업데이트합니다.

저장된 세션에서 분기하려면 `thread/fork` 호출에 `thread.id`를 전달하세요. 그러면 새 스레드 ID가 생성되고 해당 스레드에 대한 `thread/started` 알림이 전송됩니다.
`lastTurnId`를 전달하면 지정한 턴까지 포함해 이력을 복사하고
그 이후 턴은 제외합니다:

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App-server는 진행 중인 턴을 가리키는 `lastTurnId`를 거부합니다. 원본 스레드에서
턴이 진행 중일 때 이 필드를 생략하면 포크는 불완전한 턴을 아무 표시 없이
남겨 두는 대신 중단 마커를 기록합니다.

`ephemeral: true`를 전달하면 저장된 스레드 목록에 추가하지 않고
메모리 내에 포크를 생성할 수 있습니다:

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

페이지네이션을 사용하는 스레드의 임시 포크에는 `excludeTurns: true`도 필요합니다.
이 필드는 실험적이며 `capabilities.experimentalApi = true` 설정이 필요합니다.

사용자에게 표시되는 스레드 제목이 설정되면 app-server는 `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive`, `thread/rollback` 응답에 `thread.name` 값을 채웁니다. `thread/start` 및 `thread/fork` 응답에서는 나중에 제목이 설정될 때까지 `name`을 생략하거나 그 값으로 `null`을 반환할 수 있습니다.

### 저장된 스레드 읽기(재개 없이)

저장된 스레드 데이터가 필요하지만 스레드를 재개하거나 해당 이벤트를 구독하지 않으려면 `thread/read`를 사용하세요.

- `includeTurns` - `true`로 설정하면 응답에 스레드의 턴이 포함됩니다. `false`로 설정하거나 생략하면 스레드 요약만 반환됩니다.
- 반환되는 `thread` 객체에는 런타임 `status`가 포함되며, 값은 `notLoaded`, `idle`, `systemError` 또는 `active`(`activeFlags` 포함)입니다.

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

`thread/resume` 호출과 달리 `thread/read`는 스레드를 메모리에 로드하지 않으며 `thread/started` 알림도 전송하지 않습니다.

### 스레드 턴 목록 조회

`thread/turns/list`는 실험적 기능입니다. 스레드를 재개하지 않고 저장된 스레드의 턴 이력을 페이지 단위로 조회할 때 사용하세요. 결과는 기본적으로 최신순으로 정렬되므로 클라이언트는 `nextCursor`로 더 오래된 턴을 가져올 수 있습니다. 응답에는 `backwardsCursor`도 포함됩니다. 이를 `cursor` 값으로 지정하고 `sortDirection: "asc"` 설정을 함께 전달하면 이전 페이지의 첫 번째 항목보다 최신인 턴을 가져올 수 있습니다.

`itemsView`는 응답에 포함할 턴 항목 데이터의 범위를 제어합니다:

- `notLoaded`로 설정하면 항목을 생략합니다.
- `summary`는 요약된 항목 데이터를 반환하며, 필드를 생략할 때 적용되는 기본값입니다.
- `full`은 전체 항목 데이터를 반환합니다.

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list`도 실험적 기능입니다. 스레드를 재개하지 않고
저장된 항목을 페이지 단위로 조회합니다. 한 턴의 항목만 가져오려면 `turnId`를 전달하고,
스레드 전체의 항목을 페이지 단위로 조회하려면 생략하세요. 현재 사용 중인 스레드 저장소가 항목 페이지네이션을
지원해야 하며, 그렇지 않으면 서버는 메서드가 지원되지 않는다는 오류를 반환합니다.

### 스레드 목록 조회(페이지네이션 및 필터)

`thread/list`를 사용하면 이력 UI를 렌더링할 수 있습니다. 결과는 기본적으로 `createdAt` 기준 최신순으로 정렬됩니다. 필터는 페이지네이션 전에 적용됩니다. 다음 옵션을 자유롭게 조합해 전달하세요:

- `cursor` - 이전 응답에서 받은 불투명 문자열입니다. 첫 페이지에서는 생략하세요.
- `limit` - 설정하지 않으면 서버가 적절한 페이지 크기를 기본값으로 사용합니다.
- `sortKey` - `created_at`(기본값), `updated_at` 또는 `recency_at`.
- `sortDirection` - `desc`(기본값) 또는 `asc`.
- `modelProviders` - 결과를 특정 제공자로 제한합니다. 설정하지 않거나 null 또는 빈 배열을 지정하면 모든 제공자가 포함됩니다.
- `sourceKinds` - 결과를 특정 스레드 소스로 제한합니다. 생략하거나 `[]`로 설정하면 서버는 기본적으로 대화형 소스인 `cli`와 `vscode`만 포함합니다.
- `archived` - `true`로 설정하면 보관된 스레드만 조회합니다. `false`로 설정하거나 생략하면 보관되지 않은 스레드를 조회합니다(기본값).
- `isPinned` - 값을 지정하면 저장된 고정 상태가 해당 값과 일치하는 스레드만 반환합니다. 생략하면 고정된 스레드와 고정되지 않은 스레드를 모두 반환합니다.
- `cwd` - 세션의 현재 작업 디렉터리가 지정한 경로 또는 배열에 포함된 경로 중 하나와 정확히 일치하는 스레드로 결과를 제한합니다. 상대 경로는 app-server 프로세스의 작업 디렉터리를 기준으로 해석됩니다.
- `useStateDbOnly` - `true`로 설정하면 메타데이터 복구를 위해 JSONL 스레드 로그를 스캔하지 않고 상태 데이터베이스 결과를 반환합니다. 기본 스캔 및 복구 동작을 사용하려면 생략하거나 `false`를 전달하세요.
- `searchTerm` - 추출된 제목에 지정한 문자열이 포함된 스레드로 결과를 제한합니다. 대소문자를 구분합니다.
- `parentThreadId` - 지정한 부모 스레드의 직계 자식 스레드로 결과를 제한합니다. 이 필터는 실험적이며 `capabilities.experimentalApi = true` 설정이 필요합니다.
- `ancestorThreadId` - 깊이에 관계없이 지정한 스레드에서 생성된 하위 스레드로 결과를 제한합니다. 이 필터는 실험적이며 `capabilities.experimentalApi = true` 설정이 필요합니다. `parentThreadId`와 함께 사용하지 마세요.

`sourceKinds`에는 다음 값을 사용할 수 있습니다:

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

예:

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

`nextCursor`가 `null`이면 마지막 페이지입니다.

### 저장된 스레드 메타데이터 업데이트

`thread/metadata/update`를 사용해 스레드를 재개하지 않고 저장된 스레드 메타데이터를
수정하세요. `isPinned`를 설정하면 스레드를 고정하거나 고정을 해제할 수 있고, `gitInfo`를 업데이트하면
저장된 Git 메타데이터를 변경할 수 있습니다. 생략한 필드는 그대로 유지되며, `null`을 명시하면
저장된 Git 메타데이터 값이 지워집니다.

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### 스레드 상태 변경 추적

`thread/status/changed` 알림은 로드된 스레드의 런타임 상태가 변경될 때마다 전송됩니다. 페이로드에는 `threadId`와 변경된 `status`가 포함됩니다.

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### 로드된 스레드 목록 조회

`thread/loaded/list`는 현재 메모리에 로드된 스레드 ID를 반환합니다.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### 로드된 스레드 구독 해제

`thread/unsubscribe`는 현재 연결의 스레드 구독을 해제합니다. 응답 상태는 다음 중 하나입니다:

- `unsubscribed` - 연결이 구독 중이었고 이번에 구독이 해제된 경우입니다.
- `notSubscribed` - 연결이 해당 스레드를 구독하고 있지 않았던 경우입니다.
- `notLoaded` - 스레드가 로드되지 않은 경우입니다.

이 연결이 마지막 구독자였다면 서버는 구독자가 없고 스레드 활동도 없는 상태가 30분간 지속될 때까지 스레드를 로드된 상태로 유지합니다. 유예 기간이 만료되면 app-server는 스레드를 언로드하고 `notLoaded` 상태로의 전환을 알리는 `thread/status/changed` 알림과 `thread/closed` 알림을 전송합니다.

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

이후 스레드가 만료되면:

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### 스레드 보관

`thread/archive`를 사용해 저장된 스레드 로그(디스크에 저장된 JSONL 파일)를 보관 세션 디렉터리로 이동하세요. 스레드를 보관하면 서버는 해당 스레드에서 생성된 하위 스레드 중 아직 보관되지 않은 스레드도 보관하려고 시도합니다.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

이후 `thread/list` 호출에서 `archived: true`를 전달하지 않으면 보관된 스레드는 결과에 표시되지 않습니다. 서버는 실제로 보관한 각 스레드에 대해 `thread/archived` 알림을 하나씩 전송합니다. 생성된 하위 스레드를 보관할 수 없는 경우에는 해당 하위 스레드의 보관 알림이 없어도 요청이 성공할 수 있습니다.

### 스레드 삭제

`thread/delete`를 사용해 저장된 활성 스레드 또는 보관된 스레드와
해당 스레드에서 생성된 하위 스레드를 영구적으로 삭제하세요. 서버는 성공 응답을 반환하기 전에 기존 롤아웃 파일과
관련 메타데이터를 삭제하며, 존재하지 않는 롤아웃 파일은
이미 삭제된 것으로 처리합니다. 임시 루트 스레드는 삭제할 수 없습니다.

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### 스레드 보관 해제

`thread/unarchive`를 사용해 보관된 스레드 롤아웃을 활성 세션 디렉터리로 다시 이동하세요.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### 스레드 컨텍스트 압축 실행

`thread/compact/start`로 스레드 이력의 컨텍스트 압축을 수동으로 시작하세요. 요청은 즉시 `{}`를 반환합니다.

App-server는 동일한 `threadId`에 대해 표준 `turn/*` 및 `item/*` 알림으로 진행 상황을 전송합니다. 여기에는 `contextCompaction` 항목의 수명 주기(`item/started` 이후 `item/completed`)가 포함됩니다.

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### 스레드 셸 명령어 실행

스레드에 속한 셸 명령어를 사용자가 직접 실행할 때는 `thread/shellCommand`를 사용하세요. 요청은 즉시 `{}`를 반환하며, 진행 상황은 표준 `turn/*` 및 `item/*` 알림으로 스트리밍됩니다.

이 API는 샌드박스 외부에서 전체 권한으로 실행되며 스레드의 샌드박스 정책을 상속하지 않습니다. 클라이언트는 사용자가 명시적으로 실행을 요청한 명령어에만 이 API를 제공해야 합니다.

스레드에 이미 활성 턴이 있으면 명령어는 해당 턴의 보조 작업으로 실행되며, 형식이 지정된 출력이 해당 턴의 메시지 스트림에 삽입됩니다. 스레드가 유휴 상태이면 app-server가 셸 명령어를 위한 별도의 턴을 시작합니다.

`timeoutMs` 값을 설정해 실행 시간을 밀리초 단위로 제한하세요. 생략하거나
`null`을 전달하면 기본값인 1시간이 적용됩니다. `0`을 지정하면 즉시 시간 초과 처리를 요청하며,
음수는 거부됩니다. 시간 초과 설정으로 인해 RPC 수신 확인 응답이 지연되지는 않으며, 이 응답은 즉시 반환됩니다.

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### 백그라운드 터미널 정리

`thread/backgroundTerminals/clean`을 사용해 스레드에 연결되어 실행 중인 백그라운드 터미널을 모두 중지하세요. 이 메서드는 실험적이며 `capabilities.experimentalApi = true` 설정이 필요합니다.

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

`thread/backgroundTerminals/list`를 사용해 로드된 스레드에서 실행 중인 백그라운드 터미널을
확인하세요. 요청은 표준 `cursor` 및 `limit` 기반
페이지네이션을 지원하며, 반환되는 `processId`는 app-server의 프로세스 ID입니다.
이 메서드는 실험적이며 `capabilities.experimentalApi = true` 설정이 필요합니다:

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

`thread/backgroundTerminals/terminate`에 해당 `processId`를 지정해
백그라운드 터미널 하나를 중지하세요. 이 메서드는 실험적이며
`capabilities.experimentalApi = true` 설정이 필요합니다:

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### 최근 턴 롤백

`thread/rollback`은 사용 중단 예정(deprecated)이며 향후 제거됩니다. 메모리 내 컨텍스트에서 마지막
`numTurns`개 항목을 제거하고 롤아웃 로그에 롤백 마커를
저장합니다. 반환되는 `thread`에는 롤백 후의 내용으로 채워진
`turns`가 포함됩니다.

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## 턴

`input` 필드는 항목 목록을 받습니다:

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

턴별로 설정(모델, 추론 강도, 성격, `cwd`, 샌드박스 정책, 요약)을 재정의할 수 있습니다. 지정한 설정은 같은 스레드의 이후 턴에서 기본값으로 사용됩니다. `outputSchema`는 현재 턴에만 적용됩니다. `sandboxPolicy.type = "externalSandbox"`인 경우 `networkAccess` 값을 `restricted` 또는 `enabled`로 설정하세요. `workspaceWrite`에서는 `networkAccess` 값이 불리언으로 유지됩니다.

`turn/start.collaborationMode`에서 `settings.developer_instructions: null` 설정은 모드 지침을 지우는 것이 아니라 “선택한 모드의 기본 제공 지침을 사용한다”는 뜻입니다.

### 샌드박스 읽기 권한(`ReadOnlyAccess`)

`sandboxPolicy`는 읽기 권한을 명시적으로 제어할 수 있도록 지원합니다:

- `readOnly`: 선택 사항인 `access`(기본값은 `{ "type": "fullAccess" }`이며, 접근 가능한 루트를 제한할 수도 있음).
- `workspaceWrite`: 선택 사항인 `readOnlyAccess`(기본값은 `{ "type": "fullAccess" }`이며, 접근 가능한 루트를 제한할 수도 있음).

제한된 읽기 권한의 구조:

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

macOS에서 `includePlatformDefaults: true`를 설정하면 읽기 권한이 제한된 세션에 선별된 플랫폼 기본 Seatbelt 정책이 추가됩니다. 이를 통해 `/System` 전체에 대한 접근을 일괄 허용하지 않고도 도구 호환성을 높일 수 있습니다.

예시:

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### 턴 시작

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

클라이언트에서 실행한 도구의 출력으로 턴을 시작하려면 `toolOutput`에
비어 있지 않은 `name`, 선택 사항인 `namespace`, 문자열이나 콘텐츠 항목 배열 형식의
`output`을 담아 전달하세요. `input`은 빈 배열로 설정하세요.
`toolOutput`은 비어 있지 않은 사용자 입력과 함께 사용할 수 없습니다.

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

이 출력은 대화에서 도구 출력으로 유지되며,
알림과 저장된 기록에는 `functionCallOutput` 항목으로 나타납니다. 이미 일반 턴이
진행 중이라면 Codex는 해당 턴에서 처리하도록 출력을 큐에 넣습니다.

### 스레드에 항목 삽입

`thread/inject_items`를 사용해 사용자 턴을 시작하지 않고 로드된 스레드의 프롬프트 기록에 미리 구성한 Responses API 항목을 추가하세요. 이 항목은 롤아웃에 저장되며 이후 모델 요청에 포함됩니다.

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### 활성 턴 조정

`turn/steer`를 사용해 현재 진행 중인 턴에 사용자 입력을 추가하세요.

- `expectedTurnId`를 포함하세요. 이 값은 활성 턴의 ID와 일치해야 합니다.
- 스레드에 활성 턴이 없으면 요청이 실패합니다.
- `turn/steer`는 새로운 `turn/started` 알림을 내보내지 않습니다.
- `turn/steer`는 턴별 설정 재정의(`model`, `cwd`, `sandboxPolicy` 또는 `outputSchema`)를 허용하지 않습니다.

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### 턴 시작(스킬 호출)

텍스트 입력에 `$<skill-name>`을 포함하고 `skill` 입력 항목도 함께 추가해 스킬을 명시적으로 호출하세요.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### 턴 중단

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

성공하면 턴은 `status: "interrupted"` 상태로 종료됩니다.

## 검토

`review/start`는 스레드에서 Codex 검토기를 실행하고 검토 항목을 스트리밍합니다. 검토 대상에는 다음이 포함됩니다:

- `uncommittedChanges`
- `baseBranch`(브랜치와의 차이 비교)
- `commit`(특정 커밋 검토)
- `custom`(자유 형식 지침)

기존 스레드에서 검토를 실행하려면 기본값인 `delivery: "inline"`을 사용하고, 새 검토 스레드를 포크하려면 `delivery: "detached"`를 사용하세요.

요청/응답 예시:

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

별도 스레드에서 검토하려면 `"delivery": "detached"`를 사용하세요. 응답 구조는 동일하지만 `reviewThreadId`는 새 검토 스레드의 ID로, 원래 `threadId`와 다릅니다. 서버는 검토 턴을 스트리밍하기 전에 해당 새 스레드에 대한 `thread/started` 알림도 내보냅니다.

Codex는 일반적인 `turn/started` 알림을 스트리밍한 다음, `enteredReviewMode` 항목이 포함된 `item/started` 알림을 스트리밍합니다:

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

검토기가 작업을 마치면 서버는 `item/started` 및 `item/completed` 알림을 내보냅니다. 두 알림에는 최종 검토 텍스트가 담긴 `exitedReviewMode` 항목이 포함됩니다:

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

이 알림을 사용해 클라이언트에서 검토기의 출력을 렌더링하세요.

## 프로세스 실행

`process/*` API는 실험적이며 프로세스를 명시적으로 제어합니다.
`capabilities.experimentalApi = true` 설정이 필요하며 Codex의 샌드박스 외부에서 실행됩니다.
클라이언트에서 샌드박스 없이 로컬 프로세스를 제어하는 기능을
의도적으로 제공할 때만 사용하세요.

`process/spawn`으로 프로세스를 시작하고 `processHandle`을 제공한 다음,
해당 핸들을 stdin 입력, 크기 조정 및 종료 요청에 사용하세요. 출력은
`process/outputDelta` 알림으로 스트리밍되며, 완료 정보는
`process/exited`로 스트리밍됩니다.

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

`process/writeStdin`에 `deltaBase64`, `closeStdin` 또는 두 값을 모두 지정해
입력을 전송하세요. PTY 크기 조정 이벤트에는 `process/resizePty`를 사용하고, `process/kill`로
실행 중인 프로세스를 종료하세요.

## 명령어 실행

`command/exec` 호출은 스레드를 생성하지 않고 서버 샌드박스에서 단일 명령어(`argv` 배열)를 실행합니다.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

서버 프로세스에 이미 샌드박스를 적용한 상태에서 Codex의 자체 샌드박스 적용을 생략하려면 `sandboxPolicy.type = "externalSandbox"`를 사용하세요. 외부 샌드박스 모드에서는 `networkAccess` 값을 `restricted`(기본값) 또는 `enabled`로 설정하세요. `readOnly`와 `workspaceWrite`에서는 위에서 설명한 것과 동일한 `access` / `readOnlyAccess` 구조를 선택적으로 사용할 수 있습니다.

참고:

- 서버는 빈 `command` 배열을 거부합니다.
- `sandboxPolicy`에는 `turn/start`에서 사용하는 것과 동일한 구조를 지정할 수 있습니다(예: `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
- `timeoutMs` 값을 생략하면 서버 기본값이 적용됩니다.
- PTY 기반 세션에는 `tty: true`를 설정하고, 나중에 `command/exec/write`, `command/exec/resize` 또는 `command/exec/terminate`를 호출할 예정이라면 `processId`를 사용하세요.
- `streamStdoutStderr: true`를 설정하면 명령어 실행 중에 `command/exec/outputDelta` 알림을 받을 수 있습니다.

### 관리자 요구 사항 조회(`configRequirements/read`)

`configRequirements/read`를 사용해 `requirements.toml` 및/또는 MDM에서 로드되어 실제로 적용되는 관리자 요구 사항을 확인하세요.

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

구성된 요구 사항이 없으면 `result.requirements` 값은 `null`입니다. 지원되는 키와 값에 대한 자세한 내용은 [`requirements.toml`](/ko-KR/codex/config-file/config-reference#requirementstoml) 문서를 참조하세요.

### Windows 샌드박스 설정(`windowsSandbox/setupStart`)

사용자 정의 Windows 클라이언트는 시작 시 점검이 끝날 때까지 기다리지 않고 샌드박스 설정을 비동기적으로 시작할 수 있습니다.

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

App-server는 백그라운드에서 설정을 시작하고 이후 완료 알림을 전송합니다:

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

모드:

- `elevated` - 관리자 권한으로 Windows 샌드박스 설정 절차를 실행합니다.
- `unelevated` - 레거시 설정/사전 점검 절차를 실행합니다.

## 파일 시스템

v2 파일 시스템 API는 절대 경로를 대상으로 작동합니다. 파일이나 디렉터리가 변경된 후 클라이언트에서 UI 상태를 무효화해야 한다면 `fs/watch`를 사용하세요.

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

파일을 감시하면 교체나 이름 변경 작업에 따른 업데이트를 포함해 해당 파일 경로에 대한 `fs/changed` 알림이 전송됩니다.

## 이벤트

이벤트 알림은 스레드와 턴의 수명 주기 및 그 안의 항목을 전달하는 서버 발신 스트림입니다. 스레드를 시작하거나 재개한 후에는 활성 전송 스트림을 계속 읽어 `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*`, `serverRequest/resolved` 알림을 확인하세요.

### 알림 수신 거부

클라이언트는 `initialize.params.capabilities.optOutNotificationMethods`에 정확한 메서드 이름을 전달해 연결별로 특정 알림을 받지 않도록 설정할 수 있습니다.

- 정확히 일치하는 메서드에만 적용됩니다. `item/agentMessage/delta`를 지정하면 해당 메서드의 알림만 차단됩니다.
- 알 수 없는 메서드 이름은 무시됩니다.
- 현재 `thread/*`, `turn/*`, `item/*` 및 관련 v2 알림에 적용됩니다.
- 요청, 응답 또는 오류에는 적용되지 않습니다.

### 퍼지 파일 검색 이벤트(실험적)

퍼지 파일 검색 세션 API는 쿼리별 알림을 전송합니다:

- `fuzzyFileSearch/sessionUpdated` - `{ sessionId, query, files }` 형식이며, 활성 쿼리와 일치하는 현재 결과를 포함합니다.
- `fuzzyFileSearch/sessionCompleted` - 해당 쿼리의 인덱싱과 매칭이 완료되면 `{ sessionId }` 형식으로 전송됩니다.

### 경고 이벤트

- `configWarning` - `{ summary, details?, path?, range? }` 형식으로 전송되며, 복구 가능한
  구성 또는 초기화 문제를 알립니다.
- `warning` - `{ threadId?, message }` 형식으로 전송되며, 치명적이지 않은 런타임 경고를 알립니다.

### Windows 샌드박스 설정 이벤트

- `windowsSandbox/setupCompleted` - `windowsSandbox/setupStart` 요청이 완료되면 `{ mode, success, error }` 형식으로 전송됩니다.

### 턴 이벤트

- `turn/started` - `{ turn }` 형식이며, 턴 ID, 빈 `items`, `status: "inProgress"`를 포함합니다.
- `turn/completed` - `{ turn }` 형식이며, `turn.status` 값은 `completed`, `interrupted`, `failed` 중 하나입니다. 실패하면 `{ error: { message, codexErrorInfo?, additionalDetails? } }`도 포함됩니다.
- `turn/diff/updated` - `{ threadId, turnId, diff }` 형식이며, 턴에서 발생한 모든 파일 변경 사항을 집계한 최신 통합 diff를 포함합니다.
- `turn/plan/updated` - 에이전트가 계획을 공유하거나 변경할 때마다 `{ turnId, explanation?, plan }` 형식으로 전송됩니다. 각 `plan` 항목은 `{ step, status }` 형식이며, `status` 값은 `pending`, `inProgress`, `completed` 중 하나입니다.
- `hook/started` 및 `hook/completed` - 동기식 수명 주기 훅이 시작될 때와 최종 실행 요약이 준비되었을 때 각각 `{ threadId, turnId?, run }` 형식으로 전송됩니다. 비동기식 훅에서는 이러한 알림이 전송되지 않습니다.
- `model/safetyBuffering/updated` - 응답이 안전을 위한 일시적 버퍼링 상태에 들어가면 `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }` 형식으로 전송됩니다.
- `model/rerouted` - 서비스가 요청을 다른 모델로 라우팅할 때 `{ threadId, turnId, fromModel, toModel, reason }` 형식으로 전송됩니다.
- `model/verification` - 서비스에서 추가 계정 확인을 요구할 때 `{ threadId, turnId, verifications }` 형식으로 전송됩니다.
- `thread/tokenUsage/updated` - 활성 스레드의 사용량 업데이트를 전송합니다.

현재 `turn/diff/updated` 및 `turn/plan/updated`에는 항목 이벤트가 스트리밍되는 경우에도 빈 `items` 배열이 포함됩니다. 턴 항목의 기준 데이터로는 `item/*` 알림을 사용하세요.

### 항목

`ThreadItem`은 턴 응답과 `item/*` 알림에 포함되는 태그 유니온 타입입니다. 대표적인 항목 유형은 다음과 같습니다:

- `userMessage` - `{id, content}` 형식이며, `content` 값은 사용자 입력(`text`, `image` 또는 `localImage`) 목록입니다.
- `functionCallOutput` - `turn/start.toolOutput`으로 제공된 독립적인 도구 출력을 담은 `{id, name, namespace, output}` 형식입니다. `namespace` 값은 `null`일 수 있습니다.
- `agentMessage` - 누적된 에이전트 응답을 담은 `{id, text, phase?}` 형식입니다. `phase` 필드가 있으면 Responses API의 전송 형식에 정의된 값(`commentary`, `final_answer`)을 사용합니다.
- `plan` - `{id, text}` 형식이며, 플랜 모드에서 제안된 계획 텍스트를 포함합니다. `item/completed`에서 전달된 최종 `plan` 항목을 기준으로 삼으세요.
- `reasoning` - `{id, summary, content}` 형식이며, `summary`에는 스트리밍된 추론 요약이, `content`에는 원시 추론 블록이 포함됩니다.
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange` - 제안된 수정 내용을 담은 `{id, changes, status}` 형식입니다. `changes`에는 `{path, kind, diff}` 형식의 항목이 나열됩니다.
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`. 신뢰할 수 있는 MCP 앱에서는 `appContext`에 `connectorId`, `linkId`, `resourceUri`, `appName`, `templateId`과 안정적으로 유지되는 커넥터 액션 이름 `actionName`가 포함될 수 있습니다. 이전에 저장된 항목에는 새로 추가된 메타데이터가 없을 수 있습니다. 사용 중단 예정(deprecated)인 최상위 `mcpAppResourceUri` 대신 `appContext.resourceUri`를 사용하세요.
- `dynamicToolCall` - 클라이언트가 실행하는 동적 도구 호출을 나타내는 `{id, tool, arguments, status, contentItems?, success?, durationMs?}` 형식입니다.
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch` - 에이전트가 보낸 웹 검색 요청을 나타내는 `{id, query, action?}` 형식입니다.
- `imageView` - 에이전트가 이미지 뷰어 도구를 호출할 때 `{id, path}` 형식으로 전송됩니다.
- `enteredReviewMode` - 검토 프로세스가 시작될 때 `{id, review}` 형식으로 전송됩니다.
- `exitedReviewMode` - 검토 프로세스가 끝날 때 `{id, review}` 형식으로 전송됩니다.
- `contextCompaction` - Codex가 대화 기록을 압축할 때 `{id}` 형식으로 전송됩니다.

`webSearch.action`에서 액션의 `type` 값은 `search`(`query?`, `queries?`), `openPage`(`url?`), `findInPage`(`url?`, `pattern?`) 중 하나일 수 있습니다.

App Server에서 레거시 `thread/compacted` 알림은 사용 중단 예정(deprecated)입니다. 대신 `contextCompaction` 항목을 사용하세요.

모든 항목은 다음 두 가지 공통 수명 주기 이벤트를 내보냅니다:

- `item/started` - 새 작업 단위가 시작되면 `item` 전체를 내보냅니다. `item.id` 값은 델타에서 사용하는 `itemId` 값과 일치합니다.
- `item/completed` - 작업이 끝나면 최종 `item`을 전송합니다. 이 상태를 기준으로 삼으세요.

### 항목 델타

- `item/agentMessage/delta` - 에이전트 메시지에 스트리밍된 텍스트를 추가합니다.
- `item/plan/delta` - 제안된 계획 텍스트를 스트리밍합니다. 최종 `plan` 항목은 델타를 모두 이어 붙인 결과와 정확히 일치하지 않을 수 있습니다.
- `item/reasoning/summaryTextDelta` - 사람이 읽을 수 있는 추론 요약을 스트리밍합니다. 새 요약 섹션이 시작될 때마다 `summaryIndex` 값이 증가합니다.
- `item/reasoning/summaryPartAdded` - 추론 요약 섹션 사이의 경계를 표시합니다.
- `item/reasoning/textDelta` - 원시 추론 텍스트를 스트리밍합니다(모델에서 지원하는 경우).
- `item/commandExecution/outputDelta` - 명령어의 stdout/stderr를 스트리밍합니다. 델타를 순서대로 추가하세요.
- `item/fileChange/outputDelta` - 레거시 `apply_patch` 텍스트 출력을 위한 사용 중단 예정(deprecated)인 호환성 알림입니다. 현재 app-server 버전에서는 더 이상 이 알림을 내보내지 않습니다. 대신 `fileChange` 항목과 `turn/diff/updated`를 사용하세요.

## 오류

턴이 실패하면 서버는 `{ error: { message, codexErrorInfo?, additionalDetails? } }`를 포함한 `error` 이벤트를 내보낸 뒤 `status: "failed"` 상태로 턴을 종료합니다. 업스트림 HTTP 상태가 있으면 `codexErrorInfo.httpStatusCode`에 표시됩니다.

대표적인 `codexErrorInfo` 값은 다음과 같습니다:

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (업스트림 4xx/5xx 오류)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

업스트림 HTTP 상태가 있으면 서버는 해당 `codexErrorInfo` 베리언트의 `httpStatusCode`에 그 값을 담아 전달합니다.

## 승인

사용자의 Codex 설정에 따라 명령어 실행과 파일 변경에 승인이 필요할 수 있습니다. app-server는 서버 측에서 시작하는 JSON-RPC 요청을 클라이언트에 보내고, 클라이언트는 결정을 담은 페이로드로 응답합니다.

- 명령어 실행 결정: `accept`, `acceptForSession`, `decline`, `cancel` 또는 `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- 파일 변경 결정: `accept`, `acceptForSession`, `decline`, `cancel`.

- 요청에는 `threadId`와 `turnId`가 포함됩니다. 이 값을 사용해 UI 상태의 범위를 활성 대화로 한정하세요.
- 서버는 작업을 재개하거나 거부하고 `item/completed` 알림으로 항목을 종료합니다.

### 명령어 실행 승인

메시지 순서:

1. `item/started`에는 대기 중인 `commandExecution` 항목이 표시되며, 이 항목에는 `command`, `cwd` 등의 필드가 포함됩니다.
2. `item/commandExecution/requestApproval`에는 `itemId`, `threadId`, `turnId` 필드와 선택 사항인 `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext`, `availableDecisions` 필드가 포함됩니다. `initialize.params.capabilities.experimentalApi = true`인 경우 페이로드에 요청된 명령어별 샌드박스 접근 권한을 설명하는 실험적 필드 `additionalPermissions`도 포함될 수 있습니다. 전송되는 `additionalPermissions` 내의 파일 시스템 경로는 모두 절대 경로입니다.
3. 클라이언트는 위의 명령어 실행 승인 결정 중 하나로 응답합니다.
4. `serverRequest/resolved` 알림은 대기 중인 요청에 대한 응답이 완료되었거나 요청이 해제되었음을 알립니다.
5. `item/completed` 알림은 `status: completed | failed | declined` 상태의 최종 `commandExecution` 항목을 반환합니다.

`networkApprovalContext` 값이 있으면 해당 프롬프트는 관리형 네트워크 접근을 위한 것입니다(일반적인 셸 명령어 승인이 아님). 현재 v2 스키마는 대상 `host` 및 `protocol` 정보를 제공합니다. 클라이언트는 네트워크 전용 프롬프트를 렌더링해야 하며, `command`가 사용자에게 의미 있는 셸 명령어 미리보기라고 가정해서는 안 됩니다.

Codex는 동시에 발생하는 네트워크 승인 프롬프트를 대상(`host`, 프로토콜, 포트)별로 그룹화합니다. 따라서 app-server는 같은 대상으로 향하는 대기열의 여러 요청을 한꺼번에 진행시킬 수 있는 프롬프트 하나를 보낼 수 있습니다. 같은 호스트라도 포트가 다르면 별도로 처리합니다.

### 파일 변경 승인

메시지 순서:

1. `item/started` 이벤트는 제안된 `changes`와 `status: "inProgress"` 상태를 포함한 `fileChange` 항목을 내보냅니다.
2. `item/fileChange/requestApproval`에는 `itemId`, `threadId`, `turnId` 필드와 선택 사항인 `reason`, `grantRoot` 필드가 포함됩니다.
3. 클라이언트는 위의 파일 변경 승인 결정 중 하나로 응답합니다.
4. `serverRequest/resolved` 알림은 대기 중인 요청에 대한 응답이 완료되었거나 요청이 해제되었음을 알립니다.
5. `item/completed` 알림은 `status: completed | failed | declined` 상태의 최종 `fileChange` 항목을 반환합니다.

### `tool/requestUserInput`

클라이언트가 `item/tool/requestUserInput`에 응답하면 app-server는 `{ threadId, requestId }`을 포함한 `serverRequest/resolved` 알림을 내보냅니다. 클라이언트가 응답하기 전에 턴 시작, 턴 완료 또는 턴 중단으로 대기 중인 요청이 해제되면 서버는 이 정리 작업에 대해서도 같은 알림을 내보냅니다.

요청 매개변수의 `autoResolutionMs` 값은 정수로 나타낸 밀리초 단위 제한 시간 또는
`null`입니다. 제한 시간이 지정되어 있으면 사용자가 응답하지 않을 때 호스트 클라이언트가
해당 시간이 지난 뒤 프롬프트를 자동으로 처리할 수 있습니다.

### 권한 요청

기본 제공 `request_permissions` 도구는
`item/permissions/requestApproval` 요청을 보냅니다. 요청에는 `threadId`, `turnId`, `itemId`,
`environmentId`, `cwd`, 선택 사항인 `reason`, 요청한 네트워크 또는 파일 시스템
권한이 포함됩니다. 응답의 `permissions`에는 요청된 권한 중 부여한 권한만 포함하세요.
같은 세션의 이후 턴에도 부여한 권한을 유지하려면 `scope` 값을 `"session"`으로 설정하세요.
해당 턴에만 권한을 부여하려면 이 필드를 생략하거나 `"turn"` 값을 사용하세요.
요청하지 않은 권한은 무시됩니다.

### MCP 서버의 유도 요청

MCP 서버는 `mcpServer/elicitation/request` 요청으로 턴을 일시 중단할 수 있습니다.
요청에는 `threadId`, 선택 사항인 `turnId`, `serverName`가 포함되며,
요청 형식은 다음 중 하나입니다:

- `mode: "form"` 또는 `mode: "openai/form"`: `message`와
`requestedSchema`를 포함합니다.
- `mode: "url"`: `message`, `url`, `elicitationId`를 포함합니다.

`action: "accept"` 값과 요청된 `content`로 응답하거나,
`action: "decline"` 또는 `"cancel"` 값과 `content: null`로 응답하세요. 그러면 app-server가
`serverRequest/resolved` 알림을 내보냅니다. `openai/form` 베리언트를 수신하려면
`initialize.params.capabilities.mcpServerOpenaiFormElicitation` 설정으로 옵트인하세요.

### 동적 도구 호출(실험적)

`thread/start`의 `dynamicTools` 필드와 이에 대응하는 `item/tool/call` 요청 또는 응답 플로우는 실험적 API입니다.

동적 도구 이름과 네임스페이스 이름은 Responses API의 명명 규칙을
따라야 합니다. 기본 제공 Codex 도구에서 사용하는 예약된 네임스페이스 이름은 피하세요.

턴 중에 동적 도구가 호출되면 app-server는 다음을 내보냅니다:

1. `item/started`: `item.type = "dynamicToolCall"`, `status = "inProgress"`, `tool`, `arguments`를 포함합니다.
2. `item/tool/call`: 클라이언트에 보내는 서버 요청입니다.
3. 반환된 콘텐츠 항목을 포함한 클라이언트 응답 페이로드.
4. `item/completed`: `item.type = "dynamicToolCall"`, 최종 `status`, 반환된 `contentItems` 또는 `success` 값을 포함합니다.

### MCP 도구 호출 승인(앱)

App(커넥터) 도구 호출에도 승인이 필요할 수 있습니다. 앱 도구 호출에 사이드 이펙트가 있으면 서버는 `tool/requestUserInput` 요청과 **수락**, **거부**, **취소** 등의 옵션으로 승인을 요청할 수 있습니다. 도구에 파괴적 작업을 나타내는 어노테이션이 있으면 더 낮은 권한을 나타내는 힌트가 함께 제공되어도 항상 승인을 요청합니다. 사용자가 거부하거나 취소하면 도구는 실행되지 않고 관련 `mcpToolCall` 항목은 오류와 함께 완료됩니다.

## 스킬

사용자 텍스트 입력에 `$<skill-name>`을 포함해 스킬을 호출하세요. `skill` 입력 항목도 추가하는 것이 좋습니다. 이렇게 하면 모델이 이름으로 스킬을 찾는 데 의존하지 않고 서버가 전체 스킬 지침을 삽입합니다.

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

`skill` 항목을 생략해도 모델은 `$<skill-name>` 마커를 파싱하고 스킬을 찾으려 하므로 지연 시간이 늘어날 수 있습니다.

예:

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

`skills/list`로 사용 가능한 스킬을 조회하세요. 필요하면 `cwds`로 범위를 지정하고 `forceReload` 옵션을 사용할 수 있습니다. `perCwdExtraUserRoots`를 포함하면 특정 `cwd` 값에 대해 추가 절대 경로를 `user` 범위로 스캔할 수도 있습니다. app-server는 `cwd` 값이 `cwds`에 포함되지 않은 항목을 무시합니다. `skills/list`는 `cwd`별로 캐시된 결과를 재사용할 수 있습니다. 디스크에서 새로 읽으려면 `forceReload: true`로 설정하세요. 서버는 `SKILL.json`에 `interface` 및 `dependencies` 값이 있으면 이를 읽습니다.

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

서버는 감시 중인 로컬 스킬 파일이 변경되면 `skills/changed` 알림도 내보냅니다. 이 알림을 무효화 신호로 보고, 필요할 때 현재 매개변수로 `skills/list`를 다시 호출하세요.

경로를 지정해 스킬을 활성화하거나 비활성화하려면:

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## 앱(커넥터)

`app/installed` 호출로 설치된 앱의 가장 최근에 커밋된 런타임 스냅샷을 읽으세요.
각 결과에는 앱 `id`, `runtimeName`(또는 `null`), 실제 적용되는
`enabled` 상태와 `callable` 상태가 포함됩니다. 실제 적용되는 구성에서 앱이
활성화되어 있고, 모델에 표시되는 도구 중 하나 이상이 앱 정책과
도구 정책을 준수할 때만 앱을 호출할 수 있습니다.

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

로드된 스레드의 구성 대신 전역 구성을 사용하려면 `threadId` 필드를 생략하세요.
커넥터 런타임 스냅샷을 읽기 전에 새로 고치려면
`forceRefresh: true`로 설정하세요. 전역 또는 워크스페이스 정책이 앱 접근을 차단해도
감지된 앱은 `enabled` 및 `callable` 값이 `false`인 상태로 표시될 수 있습니다.

`app/list`로 사용 가능한 앱을 조회하세요. CLI/TUI에서는 `/apps`가 사용자용 선택기이며, 사용자 지정 클라이언트에서는 `app/list`를 직접 호출하세요. 각 항목에는 `isAccessible`(사용자의 이용 가능 여부)와 `isEnabled`(`config.toml`에서의 활성화 여부)가 모두 포함되므로 클라이언트에서 설치·접근 상태와 로컬 활성화 상태를 구분할 수 있습니다. 앱 항목에는 선택 사항인 `branding`, `appMetadata`, `labels` 필드도 포함될 수 있습니다.

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

`threadId` 값을 제공하면 앱 기능 제어(`features.apps`)에 해당 스레드의 구성 스냅샷이 사용됩니다. 생략하면 app-server는 최신 전역 구성을 사용합니다.

`app/list` 호출은 접근 가능한 앱과 디렉터리 앱이 모두 로드된 후 반환됩니다. 앱 캐시를 우회해 새 데이터를 가져오려면 `forceRefetch: true`로 설정하세요. 새로 고침에 성공한 경우에만 캐시 항목이 교체됩니다.

서버는 두 소스(접근 가능한 앱, 디렉터리 앱) 중 하나의 로드가 완료될 때마다 `app/list/updated` 알림도 내보냅니다. 각 알림에는 최신 통합 앱 목록이 포함됩니다.

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

앱 ID를 이미 알고 있고 설치된 런타임 상태가 아니라 앱 메타데이터가 필요하면
`app/read`를 사용하세요. `appIds`에는 최대 100개의 ID를 전달하세요.
서버는 ID가 중복되면 처음 나타난 항목만 유지하고,
`apps`와 `missingAppIds` 모두에서 그 순서를 유지합니다. 알 수 없거나 접근할 수 없는 앱은
전체 요청을 실패시키지 않고 `missingAppIds`에 반환됩니다.

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

표시용 공개 도구 요약을 요청하려면 `includeTools: true`로 설정하세요.
메타데이터 응답에는 설치된 앱의 런타임 상태가 포함되지 않으며
도구 호출 권한도 부여하지 않습니다. `app/installed`로 실제 적용되는
`enabled` 및 `callable` 상태를 확인하세요.

앱을 호출하려면 텍스트 입력에 `$<app-slug>`를 넣고, `app://<id>` 경로가 지정된 `mention` 입력 항목을 추가하세요(권장).

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### 앱 설정을 위한 구성 RPC 예제

`config/read`, `config/value/write`, `config/batchWrite`를 사용해 `config.toml`의 앱 제어 설정을 확인하거나 업데이트하세요.

실제로 적용되는 앱 설정 구조(`_default` 및 도구별 재정의 포함)를 조회하세요:

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer`는 앱별 값으로 재정의하지 않는 한
모든 앱의 검토자를 설정합니다. 두 값이 모두 생략되면 앱은
최상위 `approvals_reviewer` 값을 상속합니다. `apps._default.default_tools_approval_mode`는
앱별 또는 도구별 재정의가 없는 도구에 적용할
기본 승인 모드를 설정합니다. 관리형 승인 모드 요구 사항은 도구 승인 모드
설정보다 우선합니다.

앱 설정 하나를 업데이트하세요:

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

여러 앱 설정 변경 사항을 원자적으로 적용하세요:

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### 외부 에이전트 설정 감지 및 가져오기

`externalAgentConfig/detect`를 사용해 마이그레이션할 수 있는 외부 에이전트 아티팩트를 찾은 다음, 선택한 항목을 `externalAgentConfig/import`에 전달하세요.

감지 예:

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

가져오기 예:

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

가져오기 요청의 선택적 최상위 매개변수 `source`는
선택한 마이그레이션 항목을 생성한 제품을 나타냅니다.

서버는 항목 유형별 처리가 완료될 때마다 `externalAgentConfig/import/progress` 알림을 전송하고,
모든 동기 및 백그라운드 가져오기가 완료되면 `externalAgentConfig/import/completed`
알림을 전송합니다. 이 알림에는 응답과 동일한 `importId`와
유형별 `successes` 및 `failures` 정보가 담긴 `itemTypeResults`가 포함됩니다.
완료 알림은 응답 직후 또는 백그라운드 원격 가져오기가
완료된 후 도착할 수 있습니다.

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

이전에 완료된 가져오기 내역을 조회하세요:

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

지원되는 `itemType` 값은 `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
`MCP_SERVER_CONFIG`, `SUBAGENTS`, `HOOKS`, `COMMANDS`, `SESSIONS`입니다.
`PLUGINS` 항목의 `details.plugins`에는 각 `marketplaceName`과 Codex가
마이그레이션을 시도할 수 있는 `pluginNames`가 나열됩니다. 감지 결과에는 아직
처리할 작업이 남아 있는 항목만 포함됩니다. 예를 들어 `AGENTS.md`가
이미 존재하고 비어 있지 않으면 Codex는 AGENTS 마이그레이션을 건너뛰며, 스킬을 가져올 때 기존
스킬 디렉터리를 덮어쓰지 않습니다.

`.claude/settings.json`에서 플러그인을 감지할 때 Codex는
`extraKnownMarketplaces`에서 설정된 마켓플레이스 소스를 읽습니다. `enabledPlugins`에
`claude-plugins-official`의 플러그인이 포함되어 있지만 마켓플레이스 소스가 없으면,
Codex는 `anthropics/claude-plugins-official`을 소스로 추정합니다.

## 인증 엔드포인트

JSON-RPC 인증/계정 인터페이스는 요청/응답 메서드와 서버 발신 알림(`id` 없음)을 제공합니다. 이를 사용해 인증 상태를 확인하고, 로그인을 시작하거나 취소하고, 로그아웃하고, ChatGPT 요청 한도를 조회하며, 크레딧 소진이나 사용 한도에 관해 워크스페이스 소유자에게 알릴 수 있습니다.

### 인증 모드

Codex는 다음 인증 모드를 지원합니다. `account/updated.authMode`는 활성 모드를 나타내며, 제공되는 경우 현재 ChatGPT `planType`도 포함합니다. `account/read`에서도 계정 및 플랜 세부 정보를 제공합니다.

- **API 키(`apikey`)** - 호출자가 `type: "apiKey"`를 지정해 OpenAI API 키를 제공하면 Codex가 해당 키를 저장해 API 요청에 사용합니다.
- **관리형 ChatGPT(`chatgpt`)** - Codex가 ChatGPT OAuth 플로우를 관리하고 토큰을 저장하며 자동으로 갱신합니다. 브라우저 플로우는 `type: "chatgpt"`로, 기기 코드 플로우는 `type: "chatgptDeviceCode"`로 시작하세요.
- **ChatGPT 외부 토큰(`chatgptAuthTokens`)** - 사용자의 ChatGPT 인증 수명 주기를 이미 관리하는 호스트 앱을 위한 실험적 모드입니다. 호스트 앱은 `accessToken`과 `chatgptAccountId`를 직접 제공하고, 선택적으로 `chatgptPlanType`도 제공합니다. 요청을 받으면 토큰을 갱신해야 합니다.
- **Amazon Bedrock** - `account/read`에서는 Bedrock 계정을 `type: "amazonBedrock"` 형식으로 반환하고, 자격 증명의 출처가 Codex에서 관리하는 Bedrock API 키(`credentialSource: "codexManaged"`)인지 외부 AWS 자격 증명 체인(`credentialSource: "awsManaged"`)인지 나타냅니다. `account/updated.authMode`는 Codex에서 관리하는 Bedrock API 키에 `bedrockApiKey`를 사용합니다.

### API 개요

- `account/read` - 현재 계정 정보를 가져오며, 선택적으로 토큰도 갱신합니다.
- `account/login/start` - 로그인을 시작합니다(`apiKey`, `chatgpt`, `chatgptDeviceCode` 또는 실험적 기능인 `chatgptAuthTokens`).
- `account/login/completed` (알림) - 로그인 시도가 성공 또는 오류로 완료되면 전송됩니다.
- `account/login/cancel` - 대기 중인 관리형 ChatGPT 로그인을 `loginId`로 취소합니다.
- `account/logout` - 로그아웃하고 `account/updated` 알림을 발생시킵니다.
- `account/updated` (알림) - 인증 모드가 변경될 때마다 전송됩니다(`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, `agentIdentity`, `personalAccessToken`, `bedrockApiKey` 또는 `null`). 제공되는 경우 `planType`도 포함됩니다.
- `account/chatgptAuthTokens/refresh` (서버 요청) - 권한 부여 오류가 발생한 후 외부에서 관리하는 새 ChatGPT 토큰을 요청합니다.
- `account/rateLimits/read` - ChatGPT 요청 한도를 가져옵니다.
- `account/rateLimits/updated` (알림) - 사용자의 ChatGPT 요청 한도가 변경될 때마다 전송됩니다.
- `account/sendAddCreditsNudgeEmail` - 크레딧이 소진되었거나 사용 한도에 도달했음을 워크스페이스 소유자에게 이메일로 알리도록 ChatGPT에 요청합니다.
- `account/rateLimitResetCredit/consume` - 획득한 요청 한도 재설정 기회를 1회 소진합니다. 이때 호출자가 제공한 `idempotencyKey` 값을 사용합니다.
- `account/usage/read` - ChatGPT 계정의 토큰 활동 요약과 일별 버킷을 가져옵니다.
- `account/workspaceMessages/read` - 활성 상태인 워크스페이스 메시지를 가져오며, 제공되는 경우 알림 제목도 포함합니다.
- `mcpServer/oauthLogin/completed` (알림) - `mcpServer/oauth/login` 플로우가 완료된 후 전송되며, 페이로드에는 `{ name, threadId, success, error? }` 형식의 데이터가 포함됩니다. 앱 범위의 OAuth 플로우나 플러그인 OAuth 플로우에서는 `threadId`가 `null`일 수 있습니다.
- `mcpServer/startupStatus/updated` (알림) - 설정된 MCP 서버의 시작 상태가 변경되면 전송되며, 페이로드에는 `{ threadId, name, status, error, failureReason }` 형식의 데이터가 포함됩니다. 앱 범위에서 시작한 경우 `threadId` 값은 `null`입니다. 시작에 실패했을 때 `failureReason: "reauthenticationRequired"`는 저장된 OAuth 자격 증명이 만료되어 갱신하지 못했다는 의미이므로, 클라이언트는 서버 재연결 옵션을 제공해야 합니다.

### 1) 인증 상태 확인

요청:

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

응답 예:

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

필드 참고 사항:

- `refreshToken` (boolean): 관리형 ChatGPT 모드에서 토큰 갱신을 강제하려면 `true`로 설정하세요. 외부 토큰 모드(`chatgptAuthTokens`)에서는 app-server가 이 플래그를 무시합니다.
- ChatGPT 계정에 이메일 주소가 없으면 `email` 값은 `null`입니다.
- `requiresOpenaiAuth` 값은 현재 사용 중인 공급자를 반영합니다. 값이 `false`이면 OpenAI 자격 증명 없이 Codex를 실행할 수 있습니다.
- Amazon Bedrock은 Codex가 관리하는 Bedrock API 키를 사용하면 `credentialSource: "codexManaged"` 값을
  반환하고, 외부 AWS 자격 증명 경로를 사용하면 `credentialSource: "awsManaged"` 값을
  반환합니다. 이는 선택된 자격 증명 소스를 나타낼 뿐,
  AWS 자격 증명 체인에서 자격 증명을
  찾을 수 있는지는 검증하지 않습니다.

### 2) API 키로 로그인

1. 보내기:

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. 예상 결과:

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. 알림:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) ChatGPT로 로그인(브라우저 플로우)

1. 시작:

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   기본적으로 브라우저 콜백이 성공하면 로컬 성공 페이지로 리디렉션됩니다.
   조직 설정이 필요하지 않은 경우 `useHostedLoginSuccessPage: true`로 설정하면
   호스팅된 성공 페이지를 사용할 수 있습니다. 호스팅된 성공 페이지를 활성화하면 `appBrand`에
   `"codex"` 또는 `"chatgpt"`를 지정할 수 있습니다. 값을 생략하거나 `null`로 설정하면
기본값은 `"codex"`입니다.

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. 브라우저에서 `authUrl`을 여세요. 로컬 콜백은 app-server가 호스팅합니다.
3. 알림을 기다리세요:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) ChatGPT로 로그인(기기 코드 플로우)

클라이언트가 로그인 절차를 직접 관리하거나 브라우저 콜백이 불안정한 경우 이 플로우를 사용하세요.

1. 시작:

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. `verificationUrl`과 `userCode`를 사용자에게 표시하세요. UX는 프런트엔드가 담당합니다.
3. 알림을 기다리세요:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) 외부에서 관리하는 ChatGPT 토큰으로 로그인(`chatgptAuthTokens`)

이 실험적 모드는 호스트 애플리케이션이 사용자의 ChatGPT 인증 수명 주기를 관리하고 토큰을 직접 제공하는 경우에만 사용하세요. 클라이언트는 이 로그인 유형을 사용하기 전에 `initialize`에서 `capabilities.experimentalApi = true`로 설정해야 합니다.

1. 보내기:

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. 예상 응답:

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. 알림:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

서버가 `401 Unauthorized` 응답을 받으면 호스트 앱에 갱신된 토큰을 요청할 수 있습니다:

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

토큰 갱신에 성공했다는 응답을 받으면 서버는 원래 요청을 다시 시도합니다. 요청은 약 10초 후에 시간 초과로 종료됩니다.

### 4) ChatGPT 로그인 취소

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) 로그아웃

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) 요청 한도(ChatGPT)

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

필드 참고 사항:

- `rateLimits`는 이전 버전과 호환되는 단일 버킷 뷰입니다.
- `rateLimitsByLimitId`가 있으면 사용량 측정 대상의 `limit_id`(예: `codex`)를 키로 하는 다중 버킷 뷰를 나타냅니다.
- `limitId`는 사용량 측정 버킷의 식별자입니다.
- `limitName`은 사용자에게 표시할 버킷 레이블이며 선택 사항입니다.
- `usedPercent`는 할당량 적용 기간 내 현재 사용량입니다.
- `windowDurationMins`는 할당량 적용 기간의 길이입니다.
- `resetsAt` 값은 다음 재설정 시각을 나타내는 Unix 타임스탬프(초)입니다.
- `planType`은 서버가 버킷에 연결된 ChatGPT 요금제를 반환할 때 포함됩니다.
- `credits`는 서버가 워크스페이스의 남은 크레딧 세부 정보를 반환할 때 포함됩니다.
- `rateLimitReachedType`은 한도에 도달했을 때 서버가 분류한 한도 상태를 나타냅니다.
- 서비스가 해당 정보를 제공하면 `rateLimitResetCredits`에는 획득한 재설정 기회 중 사용 가능한 횟수가 포함됩니다. 제공하지 않으면 `null`입니다.
- 개수만 확인할 수 있는 경우 `rateLimitResetCredits.credits` 값은 `null`입니다. 빈 배열은 서비스가 세부 정보를 조회한 결과 사용 가능한 크레딧이 없음을 의미합니다. 서비스가 세부 정보 행 수를 제한할 수 있으므로 `availableCount` 값을 기준으로 판단해야 합니다.
- 각 세부 정보 행에는 불투명 식별자인 `id`, `resetType`, `status`, `grantedAt`, `expiresAt`(`null`일 수 있음), `title`(`null`일 수 있음), `description`(`null`일 수 있음)이 포함됩니다.
- 재설정 기회를 사용한 후 `account/rateLimits/read`로 조회하세요.

### 7) 토큰 사용량(ChatGPT)

`account/usage/read`로 ChatGPT 토큰 활동 요약 필드와
선택 사항인 일별 버킷을 조회하세요.

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

필드 참고 사항:

- 서비스가 해당 지표를 반환하지 않은 경우 `summary` 값은 `null`일 수 있습니다.
- `dailyUsageBuckets` 값은 `null`일 수 있습니다. 값이 있으면 각 버킷에 `startDate`와 `tokens`가 포함됩니다.
- 이 엔드포인트에는 Codex 서비스 기반 인증이 필요합니다. ChatGPT 인증,
외부 ChatGPT 토큰 인증, 에이전트 신원 인증, 개인 액세스 토큰 인증은 사용할 수 있지만,
API 키만 사용하는 인증과 Bedrock 인증은 사용할 수 없습니다.

### 8) 획득한 요청 한도 재설정 기회(ChatGPT)

획득한 재설정 기회 1회를 사용하려면 `account/rateLimitResetCredit/consume`을 호출하세요.

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

필드 참고 사항:

- `idempotencyKey` 값은 비워 둘 수 없습니다. 각 논리적 크레딧 사용 시도마다 UUID를 지정하고, 해당 시도를 재시도할 때는 같은 값을 재사용하세요.
- `creditId`는 선택 사항입니다. 지정하는 경우 `account/rateLimits/read`에서 받은 비어 있지 않은 불투명 ID여야 합니다. 생략하면 서비스가 사용 가능한 다음 크레딧을 선택합니다.
- `reset` 값은 크레딧이 사용되었음을 의미합니다.
- `alreadyRedeemed`는 동일한 크레딧 사용 처리가 이미 완료되었음을 의미합니다. 이를 멱등한 성공으로 처리하고 계정 한도 정보를 새로 조회하세요.
- `nothingToReset` 값은 재설정 대상이 되는 요청 한도 적용 기간이 없음을 의미합니다.
- `noCredit` 값은 계정에서 획득한 재설정 크레딧 중 사용 가능한 크레딧이 없음을 의미합니다.
- 재설정 기회를 사용한 후에는 이 응답으로 갱신된 요청 한도 적용 기간을 추정하지 말고 `account/rateLimits/read`로 조회하세요.

### 9) 워크스페이스 소유자에게 한도 알림 보내기

크레딧이 소진되었거나 사용량 한도에 도달했을 때 워크스페이스 소유자에게 이메일을 보내도록 ChatGPT에 요청하려면 `account/sendAddCreditsNudgeEmail`을 사용하세요.

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

워크스페이스 크레딧이 소진된 경우에는 `creditType: "credits"` 값을 사용하고, 워크스페이스 사용량 한도에 도달한 경우에는 `creditType: "usage_limit"` 값을 사용하세요. 소유자에게 최근에 이미 알림을 보냈다면 응답 상태는 `cooldown_active`입니다.

### 10) 워크스페이스 메시지(ChatGPT)

`account/workspaceMessages/read`로 현재 워크스페이스의 활성 메시지를
조회하세요. 알림 제목이 있으면 함께 반환됩니다.

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
