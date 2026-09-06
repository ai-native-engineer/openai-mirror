<!-- source: https://learn.chatgpt.com/zh-Hant/docs/codex-sdk -->

如果您透過 Codex CLI、IDE 擴充功能或 Codex 雲端使用 Codex，也可以透過程式控制 Codex。

需要進行下列操作時，請使用 SDK：

- 在 CI/CD 管線中控制 Codex
- 建立自己的智慧體，讓它能與 Codex 互動，以執行複雜的工程任務
- 將 Codex 整合至您自己的內部工具與工作流程
- 將 Codex 整合至您自己的應用程式

使用 Codex SDK 自動執行程式碼編寫任務，包括 CI 中的作業。使用 [Codex app server](/zh-Hant/codex/app-server) 建立自訂用戶端，以處理身分驗證、對話記錄、核准，以及串流傳送的智慧體事件。

`codex mcp-server` 已棄用。現有整合仍可參考 [MCP 伺服器指南](/zh-Hant/codex/mcp-server)。

如果您有測試版存取權，且需要掃描程式碼庫或變更，以取得結構化的
安全性檢查結果與涵蓋範圍，請使用 [Codex Security TypeScript
SDK](/zh-Hant/codex/security/sdk)。

## TypeScript 程式庫

TypeScript 程式庫可讓您的應用程式啟動、延續及恢復本機 Codex 執行緒。

請在伺服器端使用此程式庫；它需要 Node.js 18 或更新版本。

### 安裝

若要開始使用，請使用 `npm` 安裝 Codex SDK：

```bash
npm install @openai/codex-sdk

### 使用方式

使用 Codex 啟動執行緒，並在其中執行您的提示詞。

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

再次呼叫 `run()` 可繼續同一個執行緒；您也可以提供執行緒 ID，以恢復先前的執行緒。

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

如需詳細資訊，請參閱 [TypeScript 程式碼庫](https://github.com/openai/codex/tree/main/sdk/typescript)。

## Python 程式庫

Python SDK 會透過 JSON-RPC 控制本機 Codex app-server。它需要 Python 3.10 或更新版本。已發佈的 SDK 組建包含固定版本的 Codex CLI 執行階段相依套件。

### 安裝

若要安裝 SDK，請執行：

```bash
pip install openai-codex

已發佈的 SDK 組建會自動使用各自固定版本的執行階段。只有在您確實想改用特定的本機 Codex 可執行檔時，才傳入 `CodexConfig(codex_bin=...)`。

Python SDK 已提供穩定版。`pip install openai-codex`
會安裝最新穩定版。使用 `pip install --pre openai-codex` 即可選擇安裝
較新的預發行組建。

### 使用方式

啟動 Codex、建立執行緒，並執行提示詞：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

若您的應用程式已採用非同步處理，請使用 `AsyncCodex`：

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### 沙盒預設設定

請使用相同的 `Sandbox` 預設設定來建立執行緒，或變更後續輪次的
檔案系統存取權：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

可用的預設設定如下：

- `Sandbox.read_only`：可讀取檔案，但不允許寫入。
- `Sandbox.workspace_write`：可讀取檔案，並可在工作區與已設定的可寫入根目錄中寫入。
- `Sandbox.full_access`：執行時不受檔案系統存取限制。

省略 `sandbox=` 時，app-server 會使用已設定的預設值。
傳入 `run(...)` 或 `turn(...)` 的沙盒設定，會套用至該輪次及同一執行緒的
後續輪次。

如需詳細資訊，請參閱 [Python 程式碼庫](https://github.com/openai/codex/tree/main/sdk/python)。
