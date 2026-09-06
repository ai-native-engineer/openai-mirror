<!-- source: https://learn.chatgpt.com/zh-Hant/docs/app-server -->

Codex app-server 是 Codex 用來支援功能豐富的用戶端（例如 Codex VS Code 擴充功能）的介面。如果您想將身分驗證、對話歷程、核准及智慧體事件串流等功能深度整合至自己的產品，請使用此介面。app-server 實作已在 Codex GitHub 程式碼庫（[openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)）中開源。如需完整的 Codex 開源元件清單，請參閱[開源](/zh-Hant/codex/open-source)頁面。

  若您要自動化作業或在 CI 中執行 Codex，請改用
<a href="/codex/codex-sdk">Codex SDK</a>。

## 連線至 CLI 終端介面

遠端終端介面模式可讓您在一台機器上執行 app-server，
並在另一台機器上透過 Codex CLI 終端介面連線。請啟動 WebSocket 接聽程式：

```bash
codex app-server --listen ws://127.0.0.1:4500

接著連線至終端介面：

```bash
codex --remote ws://127.0.0.1:4500

若為非本機連線，請設定 WebSocket 身分驗證，並使用 TLS 保護連線。
請將 Bearer Token 儲存在環境變數中，並傳入該變數名稱，
不要將 Token 直接放在指令列上：

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

`--remote` 選項接受 `ws://`、`wss://`、`unix://` 和
`unix://PATH` 端點。請僅在 localhost 或
透過 SSH 連接埠轉送的連線中使用未加密的 WebSocket。

## 連線至遠端程式碼模式主機

app-server 預設會啟動本機程式碼模式主機。
若要改用遠端主機，請傳入其安全的 WebSocket URL：

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` 控制從 app-server 連至其程式碼模式主機的對外連線。
它不會變更 `--listen`；後者控制用戶端連線至 app-server 的方式。
同一個 app-server 處理程序中的所有對話串，都會共用
選定的程式碼模式主機連線。

遠端主機請使用 `wss://`。`ws://` 僅適用於 localhost 或
透過 SSH 轉送的連線。app-server 指令和 WebSocket 傳輸方式均屬
實驗性功能，不支援正式環境工作負載。

## 通訊協定

如同 [MCP](https://modelcontextprotocol.io/)，`codex app-server` 支援使用 JSON-RPC 2.0 訊息進行雙向通訊（傳輸時會省略 `"jsonrpc":"2.0"` 標頭）。

支援的傳輸方式：

- `stdio`（`--listen stdio://`，預設）：以換行字元分隔的 JSON（JSONL）。
- `websocket`（`--listen ws://IP:PORT`，實驗性且不受支援）：每個 WebSocket 文字訊框包含一則
  JSON-RPC 訊息。
- Unix 通訊端（`--listen unix://` 或 `--listen unix://PATH`）：透過 Codex 預設的
  app-server 控制通訊端或自訂的 Unix 通訊端路徑建立 WebSocket 連線，
  並使用標準 HTTP Upgrade 交握。
- `off`（`--listen off`）：不提供本機傳輸介面。

使用 `--listen ws://IP:PORT` 執行時，同一個接聽程式也會提供基本的
HTTP 健康狀態探查：

- 接聽程式開始接受新連線後，`GET /readyz` 會傳回 `200 OK`。
- 當要求不包含 `Origin` 標頭時，
  `GET /healthz` 會傳回 `200 OK`。
- 包含 `Origin` 標頭的要求會遭到拒絕，並傳回 `403 Forbidden`。

WebSocket 傳輸方式屬於實驗性功能，且不受支援。
`ws://127.0.0.1:PORT` 這類本機接聽程式適用於 localhost 和
SSH 連接埠轉送工作流程。在功能推出期間，非回送位址的 WebSocket 接聽程式
目前預設允許未經身分驗證的連線，因此請先設定 WebSocket 身分驗證，
再開放遠端存取。

支援的 WebSocket 身分驗證旗標：

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

對於已簽署的 Bearer Token，您也可以設定 `--ws-issuer`、`--ws-audience` 和
`--ws-max-clock-skew-seconds`。用戶端在 WebSocket 交握期間會以
`Authorization: Bearer <token>` 的形式提供憑證，而 app-server
會在 JSON-RPC `initialize` 之前強制執行身分驗證。

請優先使用 `--ws-token-file`，避免在指令列上傳入原始 Bearer Token。
只有在用戶端將原始高熵 Token 儲存於獨立的本機機密儲存區時，才應使用 `--ws-token-sha256`；
雜湊值僅供驗證，用戶端仍需要
原始 Token。

在 WebSocket 模式中，app-server 使用有界佇列。當要求輸入佇列已滿時，
伺服器會以 JSON-RPC 錯誤碼 `-32001` 和訊息
`"Server overloaded; retry later."` 拒絕新要求。用戶端重試時，應讓延遲時間以指數方式增加，
並加入隨機抖動。

## 訊息結構描述

要求包含 `method`、`params` 和 `id`：

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

回應會傳回相同的 `id`，並包含 `result` 或 `error`：

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

通知會省略 `id`，只使用 `method` 和 `params`：

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

您可以透過 CLI 產生 TypeScript 結構描述或 JSON Schema 組合包。每項輸出都對應您執行的 Codex 版本，因此產出的內容會與該版本完全相符：

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## 開始使用

1. 使用 `codex app-server`（預設 stdio 傳輸方式）、
`codex app-server --listen ws://127.0.0.1:4500`（TCP WebSocket）或
`codex app-server --listen unix://`（預設 Unix 通訊端）啟動伺服器。
2. 讓用戶端透過選定的傳輸方式連線，接著傳送 `initialize`，然後傳送 `initialized` 通知。
3. 啟動對話串和輪次，然後持續讀取目前使用的傳輸串流中的通知。

範例（Node.js / TypeScript）：

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

## 核心構成要素

- **對話串**：使用者與 Codex 智慧體之間的對話。對話串包含輪次。
- **輪次**：一項使用者要求，以及智慧體隨後執行的工作。輪次包含項目，並以串流方式提供增量更新。
- **項目**：輸入或輸出的單位，包括使用者訊息、智慧體訊息、指令執行、檔案變更、工具呼叫等。

使用對話串 API 建立、列出或封存對話。使用輪次 API 推進對話，並透過輪次通知以串流方式取得進度。

## 生命週期概覽

- **每個連線僅初始化一次**：開啟傳輸連線後，立即傳送包含用戶端中繼資料的 `initialize` 要求，接著發出 `initialized`。在完成這項交握之前，伺服器會拒絕該連線上的所有要求。
- **啟動或繼續對話串**：若要建立新對話，請呼叫 `thread/start`；若要繼續現有對話，請呼叫 `thread/resume`；若要從歷程分支出具有新 ID 的對話串，請呼叫 `thread/fork`。
- **開始輪次**：呼叫 `turn/start`，並傳入目標 `threadId` 和使用者輸入。選用欄位可覆寫模型、個性、`cwd`、沙盒政策等設定。
- **引導進行中的輪次**：呼叫 `turn/steer`，將使用者輸入附加至目前正在處理的輪次，而不建立新輪次。
- **串流事件**：呼叫 `turn/start` 後，持續讀取 stdout 上的通知：`thread/archived`、`thread/unarchived`、`item/started`、`item/completed`、`item/agentMessage/delta`、工具進度及其他更新。
- **完成輪次**：模型完成處理或透過 `turn/interrupt` 取消後，伺服器會發出包含最終狀態的 `turn/completed`。

## 初始化

在每個傳輸連線上呼叫任何其他方法前，用戶端都必須先傳送一次 `initialize` 要求，再以 `initialized` 通知確認。初始化之前傳送的要求會收到 `Not initialized` 錯誤；在同一連線上重複呼叫 `initialize` 則會傳回 `Already initialized`。

伺服器會傳回它將提供給上游服務的使用者代理字串，以及描述執行目標平台的 `platformFamily` 和 `platformOs` 值。請設定 `clientInfo` 以識別您的整合。

`initialize.params.capabilities` 也支援下列用戶端能力：

- `optOutNotificationMethods`：指定此連線要排除的通知方法完整名稱。
  名稱必須完全相符，不支援萬用字元或前綴比對；
  未知名稱仍可傳入，但會被忽略。
- `requestAttestation`：選擇接收伺服器主動發起的 `attestation/generate` 要求。
  向上游提供證明的桌面主機會傳回
  不透明的 `{ "token": "..." }` 值。
- `mcpServerOpenaiFormElicitation`：允許下游 MCP 伺服器傳送
  OpenAI 擴充表單格式的 `mcpServer/elicitation/request` 變體。

**重要**：請使用 `clientInfo.name`，讓合規紀錄平台識別您的用戶端。如果您正在開發新的 Codex 整合，且預計供企業使用，請聯絡 OpenAI，將其加入已知用戶端清單。如需更多背景資訊，請參閱 [Codex 紀錄參考資料](https://chatgpt.com/public/admin/api-reference#tag/Codex)。

範例（取自 Codex VS Code 擴充功能）：

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

選擇不接收通知的範例：

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

## 選擇啟用實驗性 API

部分 app-server 方法和欄位依設計必須啟用 `experimentalApi` 能力才能使用。

- 省略 `capabilities`，或將 `experimentalApi` 設為 `false`，即可繼續使用穩定的 API 介面；伺服器會拒絕實驗性方法和欄位。
- 將 `capabilities.experimentalApi` 設為 `true`，即可啟用實驗性方法和欄位。

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

如果用戶端未選擇啟用實驗性功能，就傳送實驗性方法或欄位，app-server 會拒絕請求並傳回：

`<descriptor> requires experimentalApi capability`

## API 概覽

- `thread/start` - 建立新的對話串；發出 `thread/started`，並自動為你訂閱該對話串的回合與項目事件。
- `thread/resume` - 依 ID 重新開啟現有對話串，讓後續的 `turn/start` 呼叫將內容附加至該對話串。
- `thread/fork` - 複製已儲存的歷程，建立具有新對話串 ID 的分支。傳入 `lastTurnId` 可複製截至該回合的歷程並省略後續回合，或傳入 `ephemeral: true` 以建立記憶體內的分支。系統會針對新對話串發出 `thread/started`；`forkedFromId` 可用時，傳回的對話串也會包含該欄位。
- `thread/read` - 依 ID 讀取已儲存的對話串，但不恢復該對話串；設定 `includeTurns` 可傳回完整的回合歷程。傳回的 `thread` 物件包含執行階段的 `status`。
- `thread/list` - 分頁瀏覽已儲存的對話串記錄；支援游標式分頁及下列篩選條件：`modelProviders`、`sourceKinds`、`archived`、`isPinned`、`cwd`、`useStateDbOnly`、`searchTerm`，以及實驗性的 `parentThreadId` 或 `ancestorThreadId`。傳回的 `thread` 物件包含執行階段的 `status`。
- `thread/turns/list` - 實驗性功能；在不恢復對話串的情況下，分頁瀏覽已儲存對話串的回合歷程。`itemsView` 控制回合項目要省略、以摘要形式呈現，還是完整載入。
- `thread/items/list` - 實驗性功能；分頁瀏覽已持久保存的對話串項目，並可選擇將範圍限於單一 `turnId`。目前使用的對話串儲存區必須支援項目分頁。
- `thread/loaded/list` - 列出目前已載入記憶體的對話串 ID。
- `thread/name/set` - 針對已載入的對話串或持久保存的執行記錄，設定或更新對話串顯示給使用者的名稱；發出 `thread/name/updated`。
- `thread/goal/set` - 設定對話串的目標；發出 `thread/goal/updated`。
- `thread/goal/get` - 讀取對話串目前的目標。
- `thread/goal/clear` - 清除對話串的目標；發出 `thread/goal/cleared`。
- `thread/metadata/update` - 局部更新儲存在 SQLite 中的對話串中繼資料，包括持久保存的 `gitInfo` 和 `isPinned`。
- `thread/archive` - 將對話串的記錄檔移至封存目錄，並嘗試封存由該對話串衍生且尚未封存的後代對話串記錄檔；成功時傳回 `{}`，並針對每個已封存的對話串發出 `thread/archived`。
- `thread/delete` - 永久刪除已持久保存的作用中或已封存對話串，以及其衍生的所有後代對話串；成功時傳回 `{}`，並針對每個已刪除的對話串發出 `thread/deleted`。
- `thread/unsubscribe` - 取消此連線對對話串回合與項目事件的訂閱。如果這是最後一個訂閱者，伺服器會在對話串無訂閱者且無活動的寬限期過後卸載該對話串，並發出 `thread/closed`。
- `thread/unarchive` - 將已封存的對話串執行記錄還原至作用中工作階段目錄；傳回已還原的 `thread`，並發出 `thread/unarchived`。
- `thread/status/changed` - 已載入對話串的執行階段 `status` 發生變更時發出的通知。
- `thread/compact/start` - 觸發對話串的對話歷程壓縮；立即傳回 `{}`，同時透過 `turn/*` 和 `item/*` 通知以串流方式傳送進度。
- `thread/shellCommand` - 為對話串執行使用者發起的 Shell 指令。此操作在沙盒外執行，具有完整存取權，且不會繼承對話串的沙盒政策。
- `thread/backgroundTerminals/clean` - 停止對話串所有執行中的背景終端（實驗性功能；需要 `capabilities.experimentalApi`）。
- `thread/backgroundTerminals/list` - 列出已載入對話串中執行中的背景終端（實驗性功能；需要 `capabilities.experimentalApi`）。
- `thread/backgroundTerminals/terminate` - 依 app-server 的 `processId` 終止一個執行中的背景終端（實驗性功能；需要 `capabilities.experimentalApi`）。
- `thread/rollback` - 已棄用；從記憶體內的上下文中移除最後 N 個回合，並持久保存復原標記；傳回更新後的 `thread`。
- `turn/start` - 將使用者輸入或獨立的工具輸出新增至對話串，讓 Codex 開始生成內容；傳回初始的 `turn`，並以串流方式傳送事件。對於 `collaborationMode`，`settings.developer_instructions: null` 表示「使用所選模式的內建指示」。
- `thread/inject_items` - 將原始 Responses API 項目附加至已載入對話串中模型可見的歷程，且不啟動使用者回合。
- `turn/steer` - 將使用者輸入附加至對話串目前進行中的回合；傳回已接受的 `turnId`。
- `turn/interrupt` - 要求取消進行中的回合；成功時傳回 `{}`，該回合以 `status: "interrupted"` 結束。
- `review/start` - 為對話串啟動 Codex 審查器；發出 `enteredReviewMode` 和 `exitedReviewMode` 項目。
- `command/exec` - 在伺服器沙盒內執行單一指令，且不啟動對話串或回合。
- `command/exec/write` - 將 `stdin` 位元組寫入執行中的 `command/exec` 工作階段，或關閉 `stdin`。
- `command/exec/resize` - 調整執行中且使用 PTY 的 `command/exec` 工作階段大小。
- `command/exec/terminate` - 停止執行中的 `command/exec` 工作階段。
- `command/exec/outputDelta`（通知）- 串流中的 `command/exec` 工作階段產生以 base64 編碼的 stdout/stderr 資料區塊時發出。
- `process/spawn` - 在 Codex 的沙盒外明確啟動程序工作階段（實驗性功能；需要 `capabilities.experimentalApi`）。
- `process/writeStdin` - 將 stdin 位元組寫入執行中的 `process/spawn` 工作階段，或關閉 stdin（實驗性功能）。
- `process/resizePty` - 調整執行中且使用 PTY 的程序工作階段大小（實驗性功能）。
- `process/kill` - 終止執行中的程序工作階段（實驗性功能）。
- `process/outputDelta` 和 `process/exited`（通知）- 分別用於傳送程序的串流輸出和結束狀態（實驗性功能）。
- `model/list` - 列出可用模型（設定 `includeHidden: true` 可納入符合 `hidden: true` 的項目），包括推理強度選項、選用的 `upgrade` 和 `inputModalities`。
- `modelProvider/capabilities/read` - 讀取各模型與供應商組合所對應的供應商能力範圍。
- `experimentalFeature/list` - 列出功能旗標，包含生命週期階段中繼資料，並支援游標式分頁。
- `experimentalFeature/enablement/set` - 針對 `apps` 和 `plugins` 等受支援的功能設定鍵，局部更新記憶體中的執行階段設定。
- `environment/info` - 實驗性功能；連線至已設定的執行環境，並傳回其 Shell 和預設工作目錄。
- `permissionProfile/list` - 列出測試版的權限設定檔，以及目前生效的要求是否允許使用這些設定檔，並支援游標式分頁。
- `collaborationMode/list` - 列出協作模式預設選項（實驗性功能，不支援分頁）。
- `skills/list` - 列出一或多個 `cwd` 值所對應的技能（支援 `forceReload`，並可選擇提供 `perCwdExtraUserRoots`）。
- `skills/extraRoots/set` - 取代程序層級中用於尋找獨立技能的額外根目錄，且不持久保存這些設定。
- `skills/changed`（通知）- 受監看的本機技能檔案發生變更時發出。
- `hooks/list` - 列出針對一或多個 `cwd` 值找到的生命週期掛勾。
- `marketplace/add` - 新增遠端外掛程式市集，並將其持久保存至使用者的市集設定中。
- `marketplace/remove` - 移除已設定的市集；若有已安裝的市集根目錄，也一併移除。
- `marketplace/upgrade` - 重新整理已設定的 Git 市集；若省略市集名稱，則重新整理所有已設定的 Git 市集。
- `plugin/list` - 開發中；列出已找到的外掛程式市集和外掛程式狀態，包括安裝與身分驗證政策中繼資料、市集載入錯誤、精選外掛程式 ID，以及本機、Git、套件登錄庫或遠端外掛程式來源的中繼資料。摘要可包含遠端的 `version`、本機的 `localVersion`、以結構化資料表示的淺色與深色圖示，以及 `installPolicySource`；對目前的遠端資料列而言，後者可以是 `null`、`WORKSPACE_SETTING` 或 `IMPLICIT_CANONICAL_APP`。目前請勿在生產環境用戶端中呼叫此方法。
- `plugin/read` - 開發中；依市集路徑或遠端市集名稱，搭配外掛程式名稱，讀取單一外掛程式，包括隨附的技能、應用程式和 MCP 伺服器名稱；若遠端目錄有提供，也包括遠端外掛程式的 `shareUrl`。目前請勿在生產環境用戶端中呼叫此方法。
- `plugin/install` - 開發中；使用市集路徑或遠端市集名稱安裝外掛程式。目前請勿在生產環境用戶端中呼叫此方法。
- `plugin/uninstall` - 開發中；解除安裝已安裝的外掛程式。目前請勿在生產環境用戶端中呼叫此方法。
- `plugin/skill/read` - 依遠端市集、外掛程式 ID 與技能名稱，隨需讀取遠端外掛程式技能的 Markdown。
- `app/installed` - 讀取已安裝應用程式的執行階段狀態，包括各應用程式實際生效的啟用狀態與可呼叫狀態。
- `app/list` - 列出可用的應用程式（連接器），支援分頁，並包含可存取與啟用狀態的中繼資料。
- `app/read` - 擷取指定應用程式 ID 的中繼資料，並可選擇取得僅供顯示的工具摘要。
- `skills/config/write` - 依路徑啟用或停用技能。
- `mcpServer/oauth/login` - 為已設定的 MCP 伺服器啟動 OAuth 登入；傳回授權 URL，並在完成時發出 `mcpServer/oauthLogin/completed`。
- `tool/requestUserInput` - 針對工具呼叫向使用者提出 1 至 3 個簡短問題（實驗性）；問題可設定 `isOther`，以提供自由填寫選項。
- `mcpServer/elicitation/request`（伺服器要求） - 要求用戶端提供結構化表單輸入，或確認 MCP 伺服器所要求的 URL 流程。
- `item/permissions/requestApproval`（伺服器要求） - 要求用戶端授予內建 `request_permissions` 工具所要求的部分網路或檔案系統權限。
- `config/mcpServer/reload` - 從磁碟重新載入 MCP 伺服器組態，並將已載入對話串的重新整理作業排入佇列。
- `mcpServerStatus/list` - 列出 MCP 伺服器、工具、資源與身分驗證狀態（使用游標與數量上限進行分頁）。使用 `detail: "full"` 取得完整資料，或使用 `detail: "toolsAndAuthOnly"` 省略資源。
- `mcpServer/resource/read` - 透過已初始化的 MCP 伺服器讀取單一 MCP 資源。
- `mcpServer/tool/call` - 呼叫對話串所設定的 MCP 伺服器上的工具。
- `mcpServer/startupStatus/updated`（通知） - 當已載入對話串所設定的 MCP 伺服器啟動狀態變更時發出。
- `windowsSandbox/setupStart` - 針對 `elevated` 或 `unelevated` 模式啟動 Windows 沙盒設定；此方法會快速傳回，之後再發出 `windowsSandbox/setupCompleted`。
- `feedback/upload` - 提交意見回饋報告（包含分類、選填的原因／日誌、對話 ID，以及選填的 `extraLogFiles` 附件）。
- `config/read` - 解析組態分層後，取得磁碟上實際生效的組態。
- `externalAgentConfig/detect` - 使用 `includeHome` 與選填的 `cwds`，偵測可遷移的外部智慧體產物；每個偵測到的項目都包含 `cwd`（若來自主目錄，則為 `null`）。
- `externalAgentConfig/import` - 傳入明確指定的 `migrationItems`，其中包含 `cwd`（若來自主目錄，則為 `null`），以套用所選的外部智慧體遷移項目。支援的項目類型包括組態、技能、`AGENTS.md`、外掛程式、MCP 伺服器組態、子代理程式、掛勾、指令和工作階段；匯入項目非空時，會隨作業完成發出 `externalAgentConfig/import/progress` 和 `externalAgentConfig/import/completed`。外掛程式和工作階段的匯入可非同步完成。
- `config/value/write` - 將單一組態鍵值對寫入使用者儲存在磁碟上的 `config.toml`。
- `config/batchWrite` - 以原子方式將組態變更套用至使用者儲存在磁碟上的 `config.toml`。
- `configRequirements/read` - 從 `requirements.toml` 和／或 MDM 取得需求，包括受管理的設定之確切內容、允許清單、固定的 `featureRequirements`，以及網路需求（若尚未設定任何需求，則為 `null`）。
- `fs/readFile`、`fs/writeFile`、`fs/createDirectory`、`fs/getMetadata`、`fs/readDirectory`、`fs/remove`、`fs/copy`、`fs/watch`、`fs/unwatch` 和 `fs/changed`（通知） - 透過 app-server v2 檔案系統 API 對檔案系統的絕對路徑執行作業。

外掛程式摘要包含 `source` 聯集型別。本機外掛程式會傳回
`{ "type": "local", "path": ... }`；以 Git 為後端的市集項目會傳回
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`；
套件登錄庫項目會傳回
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }`；
遠端目錄項目則會傳回 `{ "type": "remote" }`。對於僅存在於遠端目錄的項目，
`PluginMarketplaceEntry.path` 可以是 `null`；請傳入
`remoteMarketplaceName` 而非 `marketplacePath`，以讀取或安裝
這些外掛程式。

## 模型

### 列出模型（`model/list`）

請先呼叫 `model/list`，找出可用模型及其能力，再呈現模型或個性選擇器。

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

每個模型項目可包含：

- `supportedReasoningEfforts` - 模型支援的推理強度選項。
- `defaultReasoningEffort` - 建議用戶端採用的預設推理強度。
- `upgrade` - 選填的建議升級模型 ID，供用戶端的遷移提示使用。
- `upgradeInfo` - 選填的升級中繼資料，供用戶端的遷移提示使用。
- `hidden` - 模型是否會在預設選擇器清單中隱藏。
- `inputModalities` - 模型支援的輸入類型（例如 `text`、`image`）。
- `supportsPersonality` - 模型是否支援個性專屬指示，例如 `/personality`。
- `isDefault` - 模型是否為建議的預設選項。

依預設，`model/list` 只會傳回選擇器中可見的模型。若需要完整清單，且希望在用戶端使用 `hidden` 進行篩選，請設定 `includeHidden: true`。

若缺少 `inputModalities`（較舊的模型目錄），請將其視為 `["text", "image"]`，以維持向後相容性。

### 列出實驗性功能（`experimentalFeature/list`）

使用此端點找出功能旗標及其中繼資料和生命週期階段：

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

`stage` 可為 `beta`、`underDevelopment`、`stable`、`deprecated` 或 `removed`。對於非 Beta 階段的旗標，`displayName`、`description` 和 `announcement` 可能是 `null`。

### 檢查執行環境（實驗性）

在已設定的遠端環境開始工作前，請使用 `environment/info` 檢查該環境。
此方法需要 `capabilities.experimentalApi = true`。

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` 可以是 `null`。若有值，則是採用環境原生路徑語法的
正規形式 `file:` URI。遇到未知的環境 ID、連線失敗或
通訊協定失敗時，都會傳回要求錯誤。

## 對話串

- `thread/read` 會讀取已儲存的對話串，但不會訂閱該對話串；設定 `includeTurns` 以包含回合。
- `thread/turns/list` 是實驗性功能，可分頁讀取已儲存對話串的回合歷史記錄，
  而不會恢復該對話串。使用 `itemsView` 選擇省略回合項目、
  僅載入摘要或完整載入項目。
- `thread/items/list` 是實驗性功能，可分頁讀取已持久儲存的對話串項目，並可選擇將結果限制為單一回合。
- `thread/list` 支援游標分頁，並可依 `modelProviders`、`sourceKinds`、`archived`、`isPinned`、`cwd`、`useStateDbOnly`、`searchTerm`，以及實驗性的 `parentThreadId` 或 `ancestorThreadId` 進行篩選。
- `thread/loaded/list` 會傳回目前在記憶體中的對話串 ID。
- `thread/archive` 會將對話串已持久儲存的 JSONL 日誌移至封存目錄，並嘗試封存由其衍生、但尚未封存的後代對話串日誌。
- `thread/delete` 會永久刪除已持久儲存的作用中或已封存對話串，以及由其衍生的後代對話串。
- `thread/metadata/update` 會局部更新已儲存的對話串中繼資料，包括已持久儲存的 `gitInfo` 和 `isPinned`。
- `thread/unsubscribe` 會取消目前連線對已載入對話串的訂閱，並可能在閒置寬限期後觸發 `thread/closed`。
- `thread/unarchive` 會將已封存對話串的執行軌跡還原至作用中的工作階段目錄。
- `thread/compact/start` 會觸發壓縮，並立即傳回 `{}`。
- `thread/rollback` 已棄用。它會從記憶體中的上下文移除最後 N 個回合，並在對話串已持久儲存的 JSONL 日誌中記錄復原標記。
- `thread/inject_items` 會將原始 Responses API 項目附加至已載入對話串中模型可見的歷史記錄，而不會啟動使用者回合。

### 啟動或恢復對話串

需要新的 Codex 對話時，請啟動全新的對話串。

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

`serviceName` 為選填。如果希望 app-server 以整合項目的服務名稱標記對話串層級的指標，請設定此欄位。

`thread/start`、`thread/resume` 和 `thread/fork` 會傳回
`instructionSources`，也就是已載入指示檔案的路徑陣列。各路徑均採用
來源環境原生的絕對路徑語法，
遠端環境也不例外。

實驗性用戶端可在 `thread/start` 中將 `historyMode` 設為 `"legacy"`
（預設值）或 `"paginated"`。目前尚不支援建立分頁對話串，
因此會傳回 JSON-RPC 錯誤 `-32601`。App-server 可列出及讀取
現有分頁記錄的摘要，但在支援分頁歷史記錄之前，讀取完整歷史記錄、回合分頁與恢復操作
一律會遭拒絕。

選擇啟用 `capabilities.experimentalApi` 的 Beta 版用戶端可將具名的
權限設定檔 ID 傳入 `permissions`，以取代舊版 `sandbox` 欄位。
請勿同時傳送 `permissions` 和 `sandbox`。請使用
`permissionProfile/list` 並提供專案的 `cwd`，以找出可用的設定檔，
並確認受管理的需求是否允許使用各設定檔。

`thread.sessionId` 可識別目前作用中工作階段樹狀結構的根節點。根對話串
會以自身的對話串 ID 作為工作階段 ID；分支對話串則保留
其來源根對話串的工作階段 ID。用戶端應從
`thread.sessionId` 讀取工作階段 ID，而非根據對話串 ID 推導。

若要繼續已儲存的工作階段，請呼叫 `thread/resume` 並傳入先前記錄的 `thread.id`。回應結構與 `thread/start` 相同。也可傳入 `thread/start` 支援的相同組態覆寫值，例如 `personality`：

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

僅恢復對話串本身並不會更新 `thread.updatedAt`（或執行軌跡檔案的修改時間）。時間戳記會在啟動回合時更新。

如果在組態中將已啟用的 MCP 伺服器標記為 `required`，而該伺服器初始化失敗，`thread/start` 和 `thread/resume` 也會失敗，而不會略過該伺服器繼續執行。

`thread/start` 的 `dynamicTools` 是實驗性欄位（需要 `capabilities.experimentalApi = true`）。Codex 會將這些動態工具儲存在執行緒執行記錄的中繼資料中；若未提供新的動態工具，則會在 `thread/resume` 時還原這些工具。

如果恢復執行緒時使用的模型與執行記錄中記載的模型不同，Codex 會發出警告，並在下一個回合套用一次性的模型切換指示。

### 管理執行緒目標

使用 `thread/goal/set`、`thread/goal/get` 和 `thread/goal/clear`，即可管理
TUI 中 `/goal` 所呈現的同一份已儲存目標狀態。

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

目標內容不得為空，且不得超過 4,000 個字元。提供新的目標內容
會取代原有目標並重設用量統計。若提供目前尚未進入終止狀態的目標內容，
或省略 `objective`，則會更新狀態或 Token 預算，
並保留用量歷史記錄。

若要從已儲存的工作階段建立分支，請呼叫 `thread/fork` 並傳入 `thread.id`。這會建立新的執行緒 ID，並為其發出 `thread/started` 通知。傳入
`lastTurnId` 可複製截至該回合（含該回合）的歷史記錄，
並省略後續回合：

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App-server 會拒絕指向進行中回合的 `lastTurnId`。如果來源執行緒的回合仍在進行中，
而您省略了此欄位，分支會記錄中斷標記，
而不會保留未標記的不完整回合。

傳入 `ephemeral: true` 可在記憶體中建立分支，
而不會將其加入已儲存的執行緒清單：

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

為採用分頁的執行緒建立暫時性分支時，也必須設定 `excludeTurns: true`。
此欄位屬於實驗性功能，需要 `capabilities.experimentalApi = true`。

設定顯示給使用者的執行緒標題後，app-server 會在 `thread/list`、`thread/read`、`thread/resume`、`thread/unarchive` 和 `thread/rollback` 的回應中填入 `thread.name`。在後續設定標題之前，`thread/start` 和 `thread/fork` 可能會省略 `name`，或傳回 `null`。

### 讀取已儲存的執行緒（不恢復）

如果需要已儲存的執行緒資料，但不想恢復執行緒或訂閱其事件，請使用 `thread/read`。

- `includeTurns`：設為 `true` 時，回應會包含執行緒的回合；設為 `false` 或省略時，只會取得執行緒摘要。
- 傳回的 `thread` 物件包含執行階段的 `status`，可能為 `notLoaded`、`idle`、`systemError`，或搭配 `activeFlags` 的 `active`。

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

與 `thread/resume` 不同，`thread/read` 不會將執行緒載入記憶體，也不會發出 `thread/started`。

### 列出執行緒回合

`thread/turns/list` 屬於實驗性功能，可用於分頁讀取已儲存執行緒的回合歷史記錄，不必恢復執行緒。結果預設由新到舊排序，讓用戶端可以使用 `nextCursor` 擷取較舊的回合。回應也包含 `backwardsCursor`；將其作為 `cursor` 傳入並搭配 `sortDirection: "asc"`，即可擷取比先前取得的頁面中第一個項目更新的回合。

`itemsView` 控制回應中回合項目資料的詳細程度：

- `notLoaded` 會省略項目。
- `summary` 會傳回項目摘要資料，也是未指定此設定時的預設值。
- `full` 會傳回完整的項目資料。

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

`thread/items/list` 也屬於實驗性功能，可分頁讀取已儲存的項目，
不必恢復執行緒。傳入 `turnId` 可將結果限於單一回合；
省略此值則可分頁讀取整個執行緒的項目。目前使用的執行緒儲存區必須支援項目分頁，
否則伺服器會傳回不支援此方法的錯誤。

### 列出執行緒（含分頁和篩選條件）

`thread/list` 可用於呈現歷史記錄 UI。結果預設依 `createdAt` 由新到舊排序，並在分頁前套用篩選條件。您可以任意組合下列參數：

- `cursor`：先前回應中的不透明字串；讀取第一頁時請省略。
- `limit`：如果未設定，伺服器預設會使用合理的每頁筆數。
- `sortKey`：`created_at`（預設）、`updated_at` 或 `recency_at`。
- `sortDirection`：`desc`（預設）或 `asc`。
- `modelProviders`：將結果限於特定提供者；未設定、設為 null 或設為空陣列時，會包含所有提供者。
- `sourceKinds`：將結果限於特定執行緒來源。省略或設為 `[]` 時，伺服器預設只包含互動式來源：`cli` 和 `vscode`。
- `archived`：設為 `true` 時，只列出已封存的執行緒；設為 `false` 或省略時，則列出未封存的執行緒，這也是預設行為。
- `isPinned`：提供此值時，只傳回已儲存的釘選狀態與指定值相符的執行緒。省略時，則同時傳回已釘選和未釘選的執行緒。
- `cwd`：將結果限於工作階段目前工作目錄與此路徑或陣列中任一路徑完全相符的執行緒。相對路徑會以 app-server 程序的工作目錄為基準解析。
- `useStateDbOnly`：設為 `true` 時，會傳回狀態資料庫的結果，不會掃描 JSONL 執行緒記錄檔以修復中繼資料。省略或傳入 `false` 時，則採用預設的掃描並修復行為。
- `searchTerm`：將結果限於擷取出的標題包含此文字片段的執行緒，且區分大小寫。
- `parentThreadId`：將結果限於指定父執行緒的直接子執行緒。此篩選條件屬於實驗性功能，需要 `capabilities.experimentalApi = true`。
- `ancestorThreadId`：將結果限於指定執行緒所衍生的後代執行緒，不限層級深度。此篩選條件屬於實驗性功能，需要 `capabilities.experimentalApi = true`；請勿與 `parentThreadId` 併用。

`sourceKinds` 接受下列值：

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

範例：

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

當 `nextCursor` 為 `null` 時，表示已到達最後一頁。

### 更新已儲存的執行緒中繼資料

使用 `thread/metadata/update` 局部更新已儲存的執行緒中繼資料，
不必恢復執行緒。設定 `isPinned` 可釘選或取消釘選執行緒，更新 `gitInfo` 則可變更
已儲存的 Git 中繼資料。省略的欄位會維持不變；明確指定 `null` 會清除
已儲存的 Git 中繼資料值。

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

### 追蹤執行緒狀態變更

每當已載入執行緒的執行階段狀態變更時，就會發出 `thread/status/changed`。承載資料包含 `threadId` 和新的 `status`。

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### 列出已載入的執行緒

`thread/loaded/list` 會傳回目前已載入記憶體的執行緒 ID。

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### 取消訂閱已載入的執行緒

`thread/unsubscribe` 會移除目前連線對執行緒的訂閱。回應狀態為下列其中一項：

- `unsubscribed` 表示連線原本已訂閱，現在已移除該訂閱。
- `notSubscribed` 表示連線原本未訂閱該執行緒。
- `notLoaded` 表示該執行緒未載入。

如果這是最後一個訂閱者，伺服器仍會維持執行緒的載入狀態，直到連續 30 分鐘沒有訂閱者，也沒有任何執行緒活動。寬限期屆滿後，app-server 會卸載執行緒，並發出表示狀態轉為 `notLoaded` 的 `thread/status/changed` 通知，以及 `thread/closed` 通知。

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

如果該執行緒稍後到期：

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### 封存執行緒

使用 `thread/archive` 將已儲存的執行緒記錄（以 JSONL 檔案形式儲存在磁碟上）移至已封存工作階段的目錄。封存執行緒時，也會嘗試封存其衍生且尚未封存的後代執行緒。

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

已封存的執行緒不會出現在後續的 `thread/list` 呼叫結果中，除非傳入 `archived: true`。伺服器會針對每個實際封存的執行緒發出一則 `thread/archived` 通知；如果無法封存某個衍生的後代執行緒，請求仍可能成功，但不會針對該後代執行緒發出封存通知。

### 刪除執行緒

使用 `thread/delete` 永久刪除已儲存的作用中或已封存執行緒，
以及其衍生的後代執行緒。伺服器會先移除現有的執行記錄檔與
相關中繼資料，再傳回成功結果；不存在的執行記錄檔會視為
已刪除。暫時性的根執行緒無法刪除。

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### 取消封存執行緒

使用 `thread/unarchive` 將已封存執行緒的執行記錄移回作用中工作階段的目錄。

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### 觸發執行緒壓縮

使用 `thread/compact/start` 手動觸發執行緒的歷史記錄壓縮。請求會立即傳回 `{}`。

App-server 會在同一個 `threadId` 上透過標準的 `turn/*` 和 `item/*` 通知回報進度，包括 `contextCompaction` 項目的生命週期（先發出 `item/started`，再發出 `item/completed`）。

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### 執行執行緒的 Shell 指令

使用 `thread/shellCommand` 執行屬於對話串且由使用者發起的 Shell 指令。請求會立即傳回 `{}`，進度則透過標準的 `turn/*` 和 `item/*` 通知串流傳送。

此 API 會以完整存取權在沙盒外執行，且不會繼承對話串的沙盒原則。用戶端應僅針對使用者明確發起的指令提供此 API。

如果對話串已有進行中的回合，指令會作為該回合的輔助動作執行，格式化後的輸出則會注入該回合的訊息串流。如果對話串處於閒置狀態，app-server 會為該 Shell 指令啟動獨立回合。

設定 `timeoutMs` 可限制執行時間，單位為毫秒。省略此欄位或傳入
`null` 時，會使用一小時的預設值。`0` 表示要求立即逾時；
負值會遭到拒絕。逾時設定不會延遲立即傳回的 RPC 確認回應。

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### 清理背景終端

使用 `thread/backgroundTerminals/clean` 停止與對話串相關聯的所有執行中背景終端。此方法為實驗性功能，且需要 `capabilities.experimentalApi = true`。

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

使用 `thread/backgroundTerminals/list` 檢視已載入對話串中執行中的背景終端。
此請求支援標準的 `cursor` 和 `limit` 分頁，
傳回的 `processId` 是 app-server 的處理程序 ID。
此方法為實驗性功能，且需要 `capabilities.experimentalApi = true`：

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

使用 `thread/backgroundTerminals/terminate` 搭配該 `processId`，即可停止一個背景終端。
此方法為實驗性功能，且需要
`capabilities.experimentalApi = true`：

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### 復原最近的回合

`thread/rollback` 已棄用，且日後將移除。它會從記憶體內的上下文移除最後
`numTurns` 個項目，並將復原標記持久儲存至 rollout 紀錄。
傳回的 `thread` 包含 `turns` 欄位，
其中已填入復原後的回合。

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## 回合

`input` 欄位接受項目清單：

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

你可以針對每個回合覆寫組態設定，包括模型、推理強度、個性、`cwd`、沙盒原則和摘要。指定後，這些設定會成為同一對話串後續回合的預設值。`outputSchema` 僅適用於目前回合。對於 `sandboxPolicy.type = "externalSandbox"`，請將 `networkAccess` 設為 `restricted` 或 `enabled`；對於 `workspaceWrite`，`networkAccess` 仍為布林值。

對於 `turn/start.collaborationMode`，`settings.developer_instructions: null` 表示「使用所選模式的內建指示」，而不是清除模式指示。

### 沙盒讀取權限（`ReadOnlyAccess`）

`sandboxPolicy` 支援明確的讀取權限控制：

- `readOnly`：可選擇設定 `access`（預設為 `{ "type": "fullAccess" }`，也可限制為指定的根目錄）。
- `workspaceWrite`：可選擇設定 `readOnlyAccess`（預設為 `{ "type": "fullAccess" }`，也可限制為指定的根目錄）。

受限讀取權限的結構：

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

在 macOS 上，`includePlatformDefaults: true` 會為讀取權限受限的工作階段附加經過篩選的平台預設 Seatbelt 原則。這可改善工具相容性，無須全面開放整個 `/System` 的存取權。

範例：

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

### 啟動回合

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

若要使用用戶端執行工具後的輸出啟動回合，請傳入 `toolOutput`，
其中包含非空的 `name`、選用的 `namespace`，以及 `output` 字串或
內容項目陣列。將 `input` 設為空陣列；
`toolOutput` 不能與非空的使用者輸入一起使用。

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

這份輸出在對話中仍會保留為工具輸出，並在通知和持久儲存的歷程中
以 `functionCallOutput` 項目呈現。如果已有一般回合正在進行，
Codex 會將輸出排入該回合的佇列。

### 將項目注入對話串

使用 `thread/inject_items` 將預先建立的 Responses API 項目附加至已載入對話串的提示詞歷程，而不啟動使用者回合。這些項目會持久儲存至 rollout，並納入後續的模型請求。

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

### 引導進行中的回合

使用 `turn/steer` 將更多使用者輸入附加至目前進行中的回合。

- 請加入 `expectedTurnId`；其值必須與進行中回合的 ID 相符。
- 如果對話串中沒有進行中的回合，請求將失敗。
- `turn/steer` 不會發出新的 `turn/started` 通知。
- `turn/steer` 不接受回合層級的覆寫設定（`model`、`cwd`、`sandboxPolicy` 或 `outputSchema`）。

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### 啟動回合（叫用技能）

若要明確叫用技能，請在文字輸入中加入 `$<skill-name>`，並同時新增一個 `skill` 輸入項目。

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### 中斷回合

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

成功時，回合會以 `status: "interrupted"` 結束。

## 審查

`review/start` 會為對話串執行 Codex 審查器，並串流傳送審查項目。目標包括：

- `uncommittedChanges`
- `baseBranch`（與分支進行差異比對）
- `commit`（審查特定提交）
- `custom`（自由格式指示）

使用 `delivery: "inline"`（預設值）可在現有對話串中執行審查，使用 `delivery: "detached"` 則會分支出新的審查對話串。

請求／回應範例：

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

若要在獨立對話串中執行審查，請使用 `"delivery": "detached"`。回應結構相同，但 `reviewThreadId` 會是新審查對話串的 ID，與原始 `threadId` 不同。伺服器也會先為新對話串發出 `thread/started` 通知，再串流傳送審查回合。

Codex 會如常串流傳送 `turn/started` 通知，接著傳送 `item/started`，其中包含一個 `enteredReviewMode` 項目：

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

審查器完成後，伺服器會發出 `item/started` 和 `item/completed`，其中包含帶有最終審查文字的 `exitedReviewMode` 項目：

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

使用此通知在用戶端中呈現審查器的輸出。

## 處理程序執行

`process/*` 是用於明確控制處理程序的實驗性 API。
它需要 `capabilities.experimentalApi = true`，並在 Codex 的沙盒外執行。
只有在用戶端刻意提供不受沙盒限制的本機處理程序控制功能時，
才應使用此 API。

使用 `process/spawn` 啟動處理程序並提供 `processHandle`，
接著將該控制代碼用於 stdin、調整大小和終止請求。
輸出會透過 `process/outputDelta` 通知串流傳送，
完成狀態則透過 `process/exited` 串流傳送。

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

使用 `process/writeStdin` 搭配 `deltaBase64`、`closeStdin` 或兩者來傳送輸入。
使用 `process/resizePty` 處理 PTY 大小調整事件，並使用 `process/kill`
終止執行中的處理程序。

## 指令執行

`command/exec` 會在伺服器沙盒內執行單一指令（`argv` 陣列），而不建立對話串。

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

如果已將伺服器處理程序置於沙盒中，並希望 Codex 不再強制套用自身的沙盒限制，請使用 `sandboxPolicy.type = "externalSandbox"`。對於外部沙盒模式，請將 `networkAccess` 設為 `restricted`（預設值）或 `enabled`。對於 `readOnly` 和 `workspaceWrite`，請使用上方所示的相同選用結構 `access` / `readOnlyAccess`。

注意事項：

- 伺服器會拒絕空的 `command` 陣列。
- `sandboxPolicy` 接受與 `turn/start` 相同的結構，例如 `dangerFullAccess`、`readOnly`、`workspaceWrite` 和 `externalSandbox`。
- 省略 `timeoutMs` 時，會使用伺服器預設值。
- 對於使用 PTY 的工作階段，請設定 `tty: true`；若預計後續呼叫 `command/exec/write`、`command/exec/resize` 或 `command/exec/terminate`，請使用 `processId`。
- 設定 `streamStdoutStderr: true`，即可在指令執行期間接收 `command/exec/outputDelta` 通知。

### 讀取管理員要求（`configRequirements/read`）

使用 `configRequirements/read` 檢視從 `requirements.toml` 和／或 MDM 載入後實際生效的管理員要求。

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

未設定任何要求時，`result.requirements` 為 `null`。如需支援的鍵和值的詳細資訊，請參閱 [`requirements.toml`](/zh-Hant/codex/config-file/config-reference#requirementstoml) 文件。

### Windows 沙盒設定（`windowsSandbox/setupStart`）

自訂 Windows 用戶端可以非同步觸發沙盒設定，不必在啟動時等待檢查完成。

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

App Server 會在背景啟動設定流程，並在稍後發出完成通知：

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

模式：

- `elevated` - 以提升的權限執行 Windows 沙盒設定流程。
- `unelevated` - 執行舊版設定／預檢流程。

## 檔案系統

v2 檔案系統 API 使用絕對路徑進行操作。當用戶端需要在檔案或目錄變更後使 UI 狀態失效時，請使用 `fs/watch`。

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

監看檔案時，系統會針對該檔案路徑發出 `fs/changed`，包括取代或重新命名操作所產生的更新。

## 事件

事件通知是由伺服器發起的串流，涵蓋對話串生命週期、回合生命週期及其中的項目。啟動或繼續對話串後，請持續讀取作用中的傳輸串流，以接收 `thread/started`、`thread/archived`、`thread/unarchived`、`thread/closed`、`thread/status/changed`、`turn/*`、`item/*` 及 `serverRequest/resolved` 通知。

### 停用通知

用戶端可針對每個連線，在 `initialize.params.capabilities.optOutNotificationMethods` 中傳送確切的方法名稱，以停用特定通知。

- 僅限完全相符：`item/agentMessage/delta` 只會停用該方法的通知。
- 系統會忽略未知的方法名稱。
- 適用於目前的 `thread/*`、`turn/*`、`item/*` 及相關 v2 通知。
- 不適用於請求、回應或錯誤。

### 檔案模糊搜尋事件（實驗性）

檔案模糊搜尋工作階段 API 會針對每個查詢發出通知：

- `fuzzyFileSearch/sessionUpdated` - `{ sessionId, query, files }`，包含作用中查詢目前的相符結果。
- `fuzzyFileSearch/sessionCompleted` - `{ sessionId }`，在該查詢的索引建立與比對完成時發出。

### 警告事件

- `configWarning` - `{ summary, details?, path?, range? }`，用於可復原的
  組態或初始化問題。
- `warning` - `{ threadId?, message }`，用於非致命的執行階段警告。

### Windows 沙盒設定事件

- `windowsSandbox/setupCompleted` - `{ mode, success, error }`，在 `windowsSandbox/setupStart` 請求完成後發出。

### 回合事件

- `turn/started` - `{ turn }`，包含回合 ID、空的 `items`，以及 `status: "inProgress"`。
- `turn/completed` - `{ turn }`，其中 `turn.status` 為 `completed`、`interrupted` 或 `failed`；失敗時會包含 `{ error: { message, codexErrorInfo?, additionalDetails? } }`。
- `turn/diff/updated` - `{ threadId, turnId, diff }`，包含彙整該回合所有檔案變更的最新統一格式差異。
- `turn/plan/updated` - `{ turnId, explanation?, plan }`，每當智慧體分享或變更計畫時發出；每個 `plan` 項目皆為 `{ step, status }`，其 `status` 為 `pending`、`inProgress` 或 `completed`。
- `hook/started` 和 `hook/completed` - `{ threadId, turnId?, run }`，分別在同步生命週期掛勾開始時，以及其最終執行摘要可用時發出。非同步掛勾不會觸發這些通知。
- `model/safetyBuffering/updated` - `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }`，在回應進入暫時的安全緩衝狀態時發出。
- `model/rerouted` - `{ threadId, turnId, fromModel, toModel, reason }`，在服務將請求轉送至另一個模型時發出。
- `model/verification` - `{ threadId, turnId, verifications }`，在服務要求進行額外的帳戶驗證時發出。
- `thread/tokenUsage/updated` - 作用中對話串的用量更新。

即使正在串流傳送項目事件，`turn/diff/updated` 和 `turn/plan/updated` 目前仍包含空的 `items` 陣列。回合項目應以 `item/*` 通知為準。

### 項目

`ThreadItem` 是回合回應與 `item/*` 通知所承載的標記聯集型別。常見的項目類型包括：

- `userMessage` - `{id, content}`，其中 `content` 是使用者輸入的清單（`text`、`image` 或 `localImage`）。
- `functionCallOutput` - `{id, name, namespace, output}`，用於透過 `turn/start.toolOutput` 提供的獨立工具輸出。`namespace` 可為 `null`。
- `agentMessage` - `{id, text, phase?}`，包含累積的智慧體回覆。若有 `phase`，則會使用 Responses API 的傳輸格式值（`commentary`、`final_answer`）。
- `plan` - `{id, text}`，包含規劃模式中擬定的計畫文字。請以 `item/completed` 中最終的 `plan` 項目為準。
- `reasoning` - `{id, summary, content}`，其中 `summary` 包含以串流傳送的推理摘要，`content` 則包含原始推理區塊。
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`。
- `fileChange` - `{id, changes, status}`，描述提議的修改；`changes` 列出 `{path, kind, diff}`。
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`。對於受信任的 MCP 應用程式，`appContext` 可包含 `connectorId`、`linkId`、`resourceUri`、`appName`、`templateId`，以及穩定的連接器動作名稱 `actionName`。較早保存的項目可能不含較新的中繼資料。請使用 `appContext.resourceUri`，取代已棄用的頂層 `mcpAppResourceUri`。
- `dynamicToolCall` - `{id, tool, arguments, status, contentItems?, success?, durationMs?}`，用於由用戶端執行的動態工具呼叫。
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`。
- `webSearch` - `{id, query, action?}`，用於智慧體發出的網頁搜尋請求。
- `imageView` - `{id, path}`，在智慧體呼叫圖像檢視器工具時發出。
- `enteredReviewMode` - `{id, review}`，在審查器開始執行時傳送。
- `exitedReviewMode` - `{id, review}`，在審查器完成執行時發出。
- `contextCompaction` - `{id}`，在 Codex 壓縮對話歷史記錄時發出。

對於 `webSearch.action`，動作的 `type` 可為 `search`（`query?`、`queries?`）、`openPage`（`url?`）或 `findInPage`（`url?`、`pattern?`）。

App Server 已棄用舊版 `thread/compacted` 通知；請改用 `contextCompaction` 項目。

所有項目都會發出兩個共用的生命週期事件：

- `item/started` - 新的工作單元開始時發出完整的 `item`；`item.id` 與增量所使用的 `itemId` 相符。
- `item/completed` - 工作完成後傳送最終的 `item`；應以此狀態為準。

### 項目增量

- `item/agentMessage/delta` - 將串流文字附加至智慧體訊息。
- `item/plan/delta` - 以串流傳送擬定的計畫文字。最終的 `plan` 項目可能與串接後的增量內容不完全相同。
- `item/reasoning/summaryTextDelta` - 以串流傳送可讀的推理摘要；每開始一個新的摘要區段，`summaryIndex` 就會遞增。
- `item/reasoning/summaryPartAdded` - 標示推理摘要區段之間的邊界。
- `item/reasoning/textDelta` - 以串流傳送原始推理文字（模型支援時）。
- `item/commandExecution/outputDelta` - 串流傳送指令的 stdout/stderr；請依序附加增量內容。
- `item/fileChange/outputDelta` - 已棄用的相容性通知，用於舊版 `apply_patch` 的文字輸出。目前的 app-server 版本已不再發出此通知；請改用 `fileChange` 項目和 `turn/diff/updated`。

## 錯誤

若回合失敗，伺服器會發出包含 `{ error: { message, codexErrorInfo?, additionalDetails? } }` 的 `error` 事件，然後以 `status: "failed"` 結束回合。若有上游 HTTP 狀態碼，會顯示在 `codexErrorInfo.httpStatusCode` 中。

常見的 `codexErrorInfo` 值包括：

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed`（上游 4xx/5xx 錯誤）
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`、`Unauthorized`、`SandboxError`、`InternalServerError`、`Other`

若有上游 HTTP 狀態碼，伺服器會透過相應 `codexErrorInfo` 變體的 `httpStatusCode` 欄位轉送該狀態碼。

## 核准

視使用者的 Codex 設定而定，指令執行和檔案變更可能需要核准。app-server 會向用戶端傳送由伺服器發起的 JSON-RPC 要求，用戶端則以包含決策的承載資料回應。

- 指令執行決策：`accept`、`acceptForSession`、`decline`、`cancel` 或 `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`。
- 檔案變更決策：`accept`、`acceptForSession`、`decline`、`cancel`。

- 要求包含 `threadId` 和 `turnId`；請使用這些欄位，將 UI 狀態限定於目前進行中的對話。
- 伺服器會繼續或拒絕執行工作，並以 `item/completed` 結束該項目。

### 指令執行核准

訊息順序：

1. `item/started` 會顯示待處理的 `commandExecution` 項目，其中包含 `command`、`cwd` 和其他欄位。
2. `item/commandExecution/requestApproval` 包含 `itemId`、`threadId`、`turnId`，以及選用的 `reason`、`command`、`cwd`、`commandActions`、`proposedExecpolicyAmendment`、`networkApprovalContext` 和 `availableDecisions`。當 `initialize.params.capabilities.experimentalApi = true` 時，承載資料還可包含實驗性的 `additionalPermissions`，用於說明個別指令所要求的沙盒存取權。`additionalPermissions` 中的所有檔案系統路徑在傳輸時皆為絕對路徑。
3. 用戶端會以上述其中一項指令執行核准決策回應。
4. `serverRequest/resolved` 會確認待處理要求已獲回覆或已清除。
5. `item/completed` 會傳回最終的 `commandExecution` 項目，其中包含 `status: completed | failed | declined`。

若有 `networkApprovalContext`，此提示是針對受管理的網路存取，而不是一般 Shell 指令核准。目前的 v2 結構描述會提供目標 `host` 和 `protocol`；用戶端應顯示網路專用提示，而不應假設 `command` 能提供使用者看得懂的 Shell 指令預覽。

Codex 會依目的地（`host`、通訊協定和連接埠）將並行的網路核准提示分組。因此，app-server 可能只傳送一則提示，就能讓多個排入佇列、目的地相同的要求繼續執行；同一主機上的不同連接埠則會分開處理。

### 檔案變更核准

訊息順序：

1. `item/started` 會發出一個 `fileChange` 項目，其中包含提議的 `changes`，並帶有 `status: "inProgress"`。
2. `item/fileChange/requestApproval` 包含 `itemId`、`threadId`、`turnId`，以及選用的 `reason` 和 `grantRoot`。
3. 用戶端會以上述其中一項檔案變更核准決策回應。
4. `serverRequest/resolved` 會確認待處理要求已獲回覆或已清除。
5. `item/completed` 會傳回最終的 `fileChange` 項目，其中包含 `status: completed | failed | declined`。

### `tool/requestUserInput`

當用戶端回應 `item/tool/requestUserInput` 時，app-server 會發出包含 `{ threadId, requestId }` 的 `serverRequest/resolved`。如果在用戶端回覆前，待處理要求因回合開始、完成或中斷而被清除，伺服器也會針對該清理作業發出相同通知。

要求參數包含 `autoResolutionMs`，其值為以毫秒為單位的整數逾時時間，或
`null`。若有設定逾時時間且使用者未回覆，主機用戶端可在該
等待時間過後自動處理提示。

### 權限要求

內建的 `request_permissions` 工具會傳送
`item/permissions/requestApproval`，其中包含 `threadId`、`turnId`、`itemId`、
`environmentId`、`cwd`、選用的 `reason`，以及要求的網路或檔案系統權限。
請以 `permissions` 回應，其中僅包含已授予的權限子集。
將 `scope` 設為 `"session"` 可保留授權，供同一工作階段的後續回合使用；
省略此欄位或使用 `"turn"`，則授權僅適用於目前回合。
未要求的權限會被忽略。

### MCP 伺服器引導測試要求

MCP 伺服器可透過 `mcpServer/elicitation/request` 中斷回合。
要求包含 `threadId`、選用的 `turnId`、`serverName`，以及
下列其中一種要求格式：

- `mode: "form"` 或 `mode: "openai/form"`，包含 `message` 和
`requestedSchema`。
- `mode: "url"`，包含 `message`、`url` 和 `elicitationId`。

請以 `action: "accept"` 和所要求的 `content` 回應，或改以
`action: "decline"` 或 `"cancel"` 搭配 `content: null` 回應。接著，app-server 會發出
`serverRequest/resolved`。若要接收 `openai/form` 變體，請透過
`initialize.params.capabilities.mcpServerOpenaiFormElicitation` 明確啟用此功能。

### 動態工具呼叫（實驗性）

`thread/start` 中的 `dynamicTools`，以及對應的 `item/tool/call` 要求或回應流程，都是實驗性 API。

動態工具名稱和命名空間名稱必須符合 Responses API 的命名限制。
請避免使用 Codex 內建工具的保留命名空間名稱。

在回合期間叫用動態工具時，app-server 會發出：

1. `item/started`，其中包含 `item.type = "dynamicToolCall"`、`status = "inProgress"`，以及 `tool` 和 `arguments`。
2. `item/tool/call`，作為伺服器要求傳送給用戶端。
3. 用戶端的回應承載資料，內含傳回的內容項目。
4. `item/completed`，其中包含 `item.type = "dynamicToolCall"`、最終的 `status`，以及任何傳回的 `contentItems` 或 `success` 值。

### MCP 工具呼叫核准（應用程式）

應用程式（連接器）的工具呼叫也可能需要核准。當應用程式工具呼叫具有副作用時，伺服器可能透過 `tool/requestUserInput` 要求核准，並提供 **接受**、 **拒絕**和 **取消**等選項。即使工具同時宣告了權限需求較低的提示，標示工具具有破壞性的註解仍一律會觸發核准要求。若使用者拒絕或取消，相關的 `mcpToolCall` 項目會以錯誤結束，而不會執行工具。

## 技能

在使用者文字輸入中加入 `$<skill-name>` 即可叫用技能。建議再加入一個 `skill` 輸入項目，讓伺服器注入完整的技能指示，而不是依賴模型解析名稱。

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

若省略 `skill` 項目，模型仍會剖析 `$<skill-name>` 標記並嘗試找出技能，這可能會增加延遲。

範例：

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

使用 `skills/list` 擷取可用的技能（可使用 `cwds` 限定範圍，並搭配 `forceReload`）。也可以加入 `perCwdExtraUserRoots`，針對特定 `cwd` 值掃描額外的絕對路徑，並將其視為 `user` 範圍。若項目的 `cwd` 不在 `cwds` 中，app-server 會忽略該項目。`skills/list` 可能會重複使用各個 `cwd` 的快取結果；設定 `forceReload: true` 即可從磁碟重新整理。若有 `interface` 和 `dependencies` 欄位，伺服器會從 `SKILL.json` 讀取它們。

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

受監看的本機技能檔案變更時，伺服器也會發出 `skills/changed` 通知。請將此視為資料已失效的訊號，並在需要時以目前的參數重新執行 `skills/list`。

若要依路徑啟用或停用技能：

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## 應用程式（連接器）

使用 `app/installed` 讀取最近一次提交的已安裝應用程式執行階段快照。
每項結果都包含應用程式的 `id`、`runtimeName`（或 `null`）、實際生效的
`enabled` 狀態和 `callable` 狀態。只有在實際生效的組態啟用該應用程式，
且至少有一項模型可見的工具符合
應用程式與工具政策時，才能呼叫該應用程式。

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

省略 `threadId` 即可使用全域組態，而不是已載入執行緒的組態。
設定 `forceRefresh: true` 可在讀取前重新整理連接器的執行階段快照。
若全域或工作區政策封鎖應用程式存取，
系統觀察到的應用程式仍可能出現在結果中，但其 `enabled` 和 `callable` 會設為 `false`。

使用 `app/list` 擷取可用的應用程式。在 CLI/TUI 中，`/apps` 是供使用者操作的選擇器；自訂用戶端則應直接呼叫 `app/list`。每個項目都包含 `isAccessible`（使用者可用）和 `isEnabled`（已在 `config.toml` 中啟用），讓用戶端能區分安裝／存取狀態與本機啟用狀態。應用程式項目還可包含選用的 `branding`、`appMetadata` 和 `labels` 欄位。

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

若提供 `threadId`，系統會使用該執行緒的組態快照，判定應用程式功能（`features.apps`）是否啟用。若省略，app-server 會使用最新的全域組態。

`app/list` 會在可存取的應用程式和目錄中的應用程式都載入後才傳回。設定 `forceRefetch: true` 可略過應用程式快取並擷取最新資料。只有在重新整理成功時，才會取代快取項目。

每當任一來源（可存取的應用程式或目錄中的應用程式）完成載入時，伺服器也會發出 `app/list/updated` 通知。每則通知都包含最新合併的應用程式清單。

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

若已知應用程式 ID，且需要的是應用程式中繼資料，
而非已安裝應用程式的執行階段狀態，請使用 `app/read`。最多可傳入 100 個 `appIds`。
對於重複的 ID，伺服器只保留第一次出現的項目，並在
`apps` 和 `missingAppIds` 中保留此順序。未知或無法存取的應用程式會透過
`missingAppIds` 傳回，不會導致整個要求失敗。

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

設定 `includeTools: true` 即可要求取得僅供顯示的公開工具摘要。
中繼資料回應不包含已安裝應用程式的執行階段狀態，也不會授權
工具呼叫；請使用 `app/installed` 檢查實際生效的 `enabled` 和 `callable`
狀態。

在文字輸入中插入 `$<app-slug>`，即可呼叫應用程式；建議同時新增包含 `app://<id>` 路徑的 `mention` 輸入項目。

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

### 應用程式設定的組態 RPC 範例

使用 `config/read`、`config/value/write` 和 `config/batchWrite`，檢查或更新 `config.toml` 中的應用程式控制設定。

讀取目前生效的應用程式組態結構（包括 `_default` 和各工具的覆寫設定）：

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

`apps._default.approvals_reviewer` 會設定所有應用程式的審查者，
但個別應用程式的設定值可將其覆寫。若兩者皆省略，
應用程式會繼承頂層的 `approvals_reviewer` 值。`apps._default.default_tools_approval_mode`
會為沒有個別應用程式或工具覆寫設定的工具，
設定備援核准模式。受管理的核准模式要求
會覆寫工具的核准模式設定。

更新單一應用程式設定：

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

以原子方式套用多項應用程式修改：

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

### 偵測並匯入外部智慧體組態

使用 `externalAgentConfig/detect` 找出可移轉的外部智慧體產物，再將選取的項目傳給 `externalAgentConfig/import`。

偵測範例：

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

匯入範例：

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

選用的頂層 `source` 匯入參數用來標示
產生所選移轉項目的產品。

各類型項目匯入完成時，伺服器會發出 `externalAgentConfig/import/progress`；
所有同步與背景匯入完成後，則會發出 `externalAgentConfig/import/completed`。
這些通知包含與回應相同的 `importId`，
以及 `itemTypeResults`，其中列出各類型的 `successes` 和 `failures`。
完成通知可能在回應後立即送達，
也可能在背景遠端匯入完成後才送達。

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

讀取先前已完成的匯入：

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

支援的 `itemType` 值包括 `AGENTS_MD`、`CONFIG`、`SKILLS`、`PLUGINS`、
`MCP_SERVER_CONFIG`、`SUBAGENTS`、`HOOKS`、`COMMANDS` 和 `SESSIONS`。針對
`PLUGINS` 項目，`details.plugins` 會列出每個 `marketplaceName`，以及
Codex 可嘗試移轉的 `pluginNames`。偵測結果只會包含
仍需處理的項目。例如，若 `AGENTS.md` 已存在且內容非空，
Codex 會略過 AGENTS 移轉；匯入技能時也不會
覆寫現有的技能目錄。

從 `.claude/settings.json` 偵測外掛程式時，Codex 會從
`extraKnownMarketplaces` 讀取已設定的市集來源。若 `enabledPlugins` 包含
來自 `claude-plugins-official` 的外掛程式，但缺少該市集來源，
Codex 會推定來源為 `anthropics/claude-plugins-official`。

## 身分驗證端點

JSON-RPC 身分驗證／帳戶介面提供請求／回應方法，以及由伺服器發起的通知（不含 `id`）。可使用這些介面判斷身分驗證狀態、開始或取消登入、登出、檢查 ChatGPT 速率限制，並通知工作區擁有者點數耗盡或使用量限制的情況。

### 身分驗證模式

Codex 支援下列身分驗證模式。`account/updated.authMode` 會顯示目前使用的模式，並在可用時包含目前 ChatGPT 的 `planType`。`account/read` 也會回報帳戶與方案詳細資料。

- **API 金鑰（`apikey`）** - 呼叫端會以 `type: "apiKey"` 提供 OpenAI API 金鑰，Codex 則會儲存該金鑰以供 API 請求使用。
- **ChatGPT 受管理模式（`chatgpt`）** - Codex 負責 ChatGPT OAuth 流程，會保存 Token 並自動重新整理。使用 `type: "chatgpt"` 開始瀏覽器流程，或使用 `type: "chatgptDeviceCode"` 開始裝置代碼流程。
- **ChatGPT 外部 Token（`chatgptAuthTokens`）** - 此功能尚在實驗階段，適用於已自行管理使用者 ChatGPT 身分驗證生命週期的主機應用程式。主機應用程式會直接提供 `accessToken`、`chatgptAccountId` 和選用的 `chatgptPlanType`，並且必須在收到要求時重新整理 Token。
- **Amazon Bedrock** - `account/read` 會以 `type: "amazonBedrock"` 回報 Bedrock 帳戶，並指出憑證是來自 Codex 管理的 Bedrock API 金鑰（`credentialSource: "codexManaged"`），還是外部 AWS 憑證鏈（`credentialSource: "awsManaged"`）。對於 Codex 管理的 Bedrock API 金鑰，`account/updated.authMode` 會使用 `bedrockApiKey`。

### API 概覽

- `account/read` - 取得目前的帳戶資訊，並可選擇重新整理 Token。
- `account/login/start` - 開始登入（`apiKey`、`chatgpt`、`chatgptDeviceCode` 或實驗性的 `chatgptAuthTokens`）。
- `account/login/completed`（通知）- 登入嘗試結束時發出，無論成功或發生錯誤。
- `account/login/cancel` - 依 `loginId` 取消尚未完成的 ChatGPT 受管理模式登入。
- `account/logout` - 登出，並觸發 `account/updated`。
- `account/updated`（通知）- 每當身分驗證模式變更時發出（`authMode`：`apikey`、`chatgpt`、`chatgptAuthTokens`、`agentIdentity`、`personalAccessToken`、`bedrockApiKey` 或 `null`），並在可用時包含 `planType`。
- `account/chatgptAuthTokens/refresh`（伺服器請求）- 發生授權錯誤後，要求提供由外部管理的最新 ChatGPT Token。
- `account/rateLimits/read` - 取得 ChatGPT 速率限制。
- `account/rateLimits/updated`（通知）- 每當使用者的 ChatGPT 速率限制變更時發出。
- `account/sendAddCreditsNudgeEmail` - 要求 ChatGPT 傳送電子郵件給工作區擁有者，告知點數已耗盡或已達使用量限制。
- `account/rateLimitResetCredit/consume` - 透過呼叫端提供的 `idempotencyKey` 值，使用一次已獲得的速率限制重設機會。
- `account/usage/read` - 取得 ChatGPT 帳戶的 Token 活動摘要與按日分組的資料。
- `account/workspaceMessages/read` - 取得目前有效的工作區訊息，並在有通知標題時一併取得。
- `mcpServer/oauthLogin/completed`（通知）- 在 `mcpServer/oauth/login` 流程完成後發出；承載資料包含 `{ name, threadId, success, error? }`。針對應用程式層級或外掛程式的 OAuth 流程，`threadId` 可以是 `null`。
- `mcpServer/startupStatus/updated`（通知）- 已設定的 MCP 伺服器啟動狀態變更時發出；承載資料包含 `{ threadId, name, status, error, failureReason }`。若是應用程式層級的啟動，`threadId` 為 `null`。啟動失敗時，`failureReason: "reauthenticationRequired"` 表示已儲存的 OAuth 憑證已過期且無法重新整理，因此用戶端應提供重新連線至伺服器的選項。

### 1) 檢查身分驗證狀態

請求：

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

回應範例：

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

欄位說明：

- `refreshToken`（布林值）：設為 `true` 可在 ChatGPT 受管理模式中強制重新整理 Token。在外部 Token 模式（`chatgptAuthTokens`）中，app-server 會忽略此旗標。
- 當 ChatGPT 帳戶沒有電子郵件地址時，`email` 為 `null`。
- `requiresOpenaiAuth` 反映目前使用的提供者；值為 `false` 時，Codex 可在沒有 OpenAI 憑證的情況下運作。
- Amazon Bedrock 使用由 Codex 管理的 Bedrock API 金鑰時，會回報 `credentialSource: "codexManaged"`。
  若使用外部 AWS 憑證取得途徑，則會回報 `credentialSource: "awsManaged"`。
  這只會標示所選的憑證來源，
  不會驗證 AWS 憑證鏈
  能否取得憑證。

### 2) 使用 API 金鑰登入

1. 傳送：

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. 預期結果：

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. 通知：

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

### 3) 使用 ChatGPT 登入（瀏覽器流程）

1. 開始：

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

   預設情況下，瀏覽器回呼成功後會重新導向本機成功頁面。
   設定 `useHostedLoginSuccessPage: true` 後，若不需要進行組織設定，
   就會使用託管成功頁面。啟用託管成功頁面後，`appBrand`
   可設為 `"codex"` 或 `"chatgpt"`；若省略或設為 `null`，預設值為
`"codex"`。

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. 在瀏覽器中開啟 `authUrl`；本機回呼由 app-server 託管。
3. 等待通知：

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

### 3b) 使用 ChatGPT 登入（裝置代碼流程）

當用戶端負責登入互動流程，或瀏覽器回呼不穩定時，請使用此流程。

1. 開始：

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

2. 向使用者顯示 `verificationUrl` 和 `userCode`；使用者體驗由前端負責。
3. 等待通知：

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

### 3c) 使用由外部管理的 ChatGPT Token 登入（`chatgptAuthTokens`）

僅在主機應用程式負責使用者的 ChatGPT 身分驗證生命週期，並直接提供 Token 時，才使用此實驗性模式。用戶端必須在 `initialize` 期間設定 `capabilities.experimentalApi = true`，才能使用此登入類型。

1. 傳送：

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

2. 預期回應：

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. 通知：

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

當伺服器收到 `401 Unauthorized` 時，可能會向主機應用程式要求更新後的 Token：

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

收到成功的 Token 更新回應後，伺服器會重試原始要求。要求約在 10 秒後逾時。

### 4) 取消 ChatGPT 登入

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) 登出

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) 速率限制（ChatGPT）

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

欄位說明：

- `rateLimits` 是向後相容的單一配額類別檢視。
- `rateLimitsByLimitId`（若存在）是以計量項目的 `limit_id`（例如 `codex`）為索引鍵、涵蓋多個配額類別的檢視。
- `limitId` 是計量配額類別的識別碼。
- `limitName` 是配額類別的選用標籤，供使用者查看。
- `usedPercent` 是配額時段內的目前用量。
- `windowDurationMins` 是配額時段的長度。
- `resetsAt` 是下一次重設時間的 Unix 時間戳記（秒）。
- 伺服器傳回與配額類別相關聯的 ChatGPT 方案時，會一併提供 `planType`。
- 伺服器傳回工作區剩餘點數的詳細資料時，會一併提供 `credits`。
- 達到限制時，`rateLimitReachedType` 會標示伺服器判定的限制狀態類別。
- 服務提供此資訊時，`rateLimitResetCredits` 會包含已獲得且可用的重設次數；否則為 `null`。
- 僅有數量資訊時，`rateLimitResetCredits.credits` 為 `null`。空陣列表示服務已擷取詳細資料，但未傳回任何可用的重設點數。服務可能限制明細列數，因此應以 `availableCount` 為準。
- 每筆明細都包含不透明的 `id`，以及 `resetType`、`status`、`grantedAt`、`expiresAt`（可為 `null`）、`title`（可為 `null`）和 `description`（可為 `null`）。
- 使用一次重設機會後，請呼叫 `account/rateLimits/read`。

### 7) Token 用量（ChatGPT）

使用 `account/usage/read` 擷取 ChatGPT Token 活動的摘要欄位，以及
選用的每日用量分組。

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

欄位說明：

- 服務尚未傳回該指標時，`summary` 的值可能為 `null`。
- `dailyUsageBuckets` 可能為 `null`；若有值，每個分組都包含 `startDate` 和 `tokens`。
- 此端點需要由 Codex 服務支援的身分驗證。可使用 ChatGPT、
外部 ChatGPT Token、智慧體身分或個人存取 Token 進行身分驗證；
但不支援僅使用 API 金鑰或 Bedrock 的身分驗證。

### 8) 已獲得的速率限制重設機會（ChatGPT）

呼叫 `account/rateLimitResetCredit/consume`，使用一次已獲得的重設機會。

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

欄位說明：

- `idempotencyKey` 不得為空。每項獨立的兌換作業都應使用一個 UUID；重試同一項作業時，請沿用相同的值。
- `creditId` 為選用欄位。若提供此值，必須是從 `account/rateLimits/read` 取得且非空的不透明 ID。若省略，服務會選取下一筆可用點數。
- `reset` 表示已使用一筆重設點數。
- `alreadyRedeemed` 表示同一筆兌換先前已完成。請將此結果視為冪等操作成功，並重新整理帳戶限制資訊。
- `nothingToReset` 表示目前沒有符合重設資格的速率限制時段。
- `noCredit` 表示帳戶目前沒有任何已獲得的重設點數可用。
- 使用一次重設機會後，請呼叫 `account/rateLimits/read`，不要根據此回應推斷更新後的速率限制時段。

### 9) 將限制情況通知工作區擁有者

當點數用盡或已達用量限制時，使用 `account/sendAddCreditsNudgeEmail` 要求 ChatGPT 寄送電子郵件給工作區擁有者。

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

工作區點數用盡時，請使用 `creditType: "credits"`；達到工作區用量限制時，則使用 `creditType: "usage_limit"`。若近期已通知過擁有者，回應狀態為 `cooldown_active`。

### 10) 工作區訊息（ChatGPT）

使用 `account/workspaceMessages/read` 擷取目前工作區仍有效的訊息，
若有通知標題也會一併擷取。

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
