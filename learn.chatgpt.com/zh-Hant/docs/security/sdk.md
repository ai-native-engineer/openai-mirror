<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/sdk -->

使用 Codex Security TypeScript SDK，從您的應用程式或開發工具對程式碼庫與
程式碼變更執行安全性掃描。SDK 會傳回具型別的
發現項目、涵蓋範圍詳細資料及掃描產物路徑。對於執行時間較長的掃描，也
支援預檢、成本上限、進度回呼及取消操作。

SDK 採用 ECMAScript 模組（ESM），並透過 Node.js 22
（22.13.0 或更新版本）、24 或 26 在伺服器端執行。掃描也需要 Python 3.10 或更新版本。
使用 Python 3.10 時，另須安裝 `tomli` 套件。

  Codex Security SDK [已在
  GitHub 上公開提供](https://github.com/openai/codex-security)。執行掃描需要
  Codex Security 存取權。若要使用一般程式碼編寫智慧體，請參閱 [Codex SDK
  指南](/zh-Hant/codex/codex-sdk)。若要使用終端與 CI 工作流程，請參閱 [Codex
  Security CLI 快速入門](/zh-Hant/codex/security/cli)。

## 設定 SDK

安裝 SDK：

```bash
npm install @openai/codex-security

開始掃描前，請設定 `OPENAI_API_KEY` 或 `CODEX_API_KEY`、使用
現有且儲存在檔案中的 Codex 登入狀態，或[設定其他
供應商](#configure-the-runtime-and-credentials)。Amazon Bedrock 使用 AWS
認證資料；OpenRouter 和 Fireworks 則使用各供應商專用的 API 金鑰與
組態。

為獲得最佳結果，請使用已通過 [Trusted Access for
Cyber](https://chatgpt.com/cyber) 驗證的帳戶。登入或提供 API 金鑰並不會
讓帳戶取得 Trusted Access。

## 執行掃描

只掃描您信任且有權評估的程式碼庫。SDK 會以您本機作業系統的權限
執行，且不會暫停等待核准。
掃描程序可能繼承您的環境，因此請在開始前移除無關的
認證資料。請參閱[本機掃描
權限](/zh-Hant/codex/security/cli/reference#local-scan-permissions)。

建立一個 `CodexSecurity` 用戶端、執行標準程式碼庫掃描，並在作業完成後關閉
該用戶端。傳入 `outputDir`，以選擇位於所屬 Git 工作樹之外的私有
結果目錄。

若省略 `outputDir`，Codex Security 會將結果儲存在專屬的持久性
狀態目錄中。結果可能包含原始碼摘錄與漏洞
詳細資料，因此請選擇適當的權限與保留政策。

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run` 會啟動掃描、等待掃描完成、驗證經密封的產物，
並傳回 `ScanResult`。`close` 會釋放隔離的執行階段，且支援
重複呼叫。

## 透過預檢檢查輸入

開始掃描前，使用 `preflight` 檢查程式碼庫、目標、模式、知識庫文件、
輸出位置和 Codex 組態：

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

預檢不會動用 Codex 執行階段或認證資料，也會將外掛程式與 Python 的偵測
留待掃描本身執行。因此，預檢適合在長時間執行
或需要認證資料的作業前，先檢查使用者輸入。

若要預覽現有結果目錄將如何封存，請設定
`archiveExisting: true`：

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

傳回的 `archiveDir` 可預覽封存目錄的命名方式。最終路徑可能
不同，因為 `run` 會自行產生唯一的目的地。若要擷取實際的
封存路徑，請使用 `onOutputArchived`：

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

掃描會先封存先前的結果，再以空白輸出
目錄開始執行。

## 選擇掃描目標

SDK 支援程式碼庫、路徑、已提交差異和工作樹目標。
預設目標是整個程式碼庫。

### 掃描所選路徑

傳入程式碼庫內的路徑陣列：

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

路徑可指向檔案或目錄。SDK 會解析程式碼庫內的每個
路徑並移除重複項目。

### 掃描已提交的變更

使用 `DiffTarget.refs` 掃描兩個本機可用的
Git 修訂版本之間已提交的變更：

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

目標修訂版本預設為 `HEAD`。若為差異目標，程式碼庫引數必須
是 Git 工作樹的根目錄。

### 掃描工作樹

使用 `DiffTarget.workingTree`，以基準
修訂版本為依據，掃描已暫存與未暫存的變更：

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

基準版本預設為 `HEAD`。在開始
差異或工作樹掃描前，請先擷取所選修訂版本。

### 選擇深度模式

若程式碼庫或路徑掃描需要更全面的審查，請設定 `mode: "deep"`：

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

深度模式支援程式碼庫和路徑目標。差異與
工作樹掃描請使用標準模式。選用設定可控制同時執行且彼此獨立的
標準掃描工作程序數量、每個工作程序的子代理程式數量、連續完成但未產生新發現項目的
工作程序掃描次數，以及工作程序執行的總次數與持續時間。這些設定
需要 `mode: "deep"`。

`maxTimeHours` 的預設值為 `96`，可設為不超過 `96` 的正數，
也接受小數小時。到達時限時，Codex Security 會停止尚未完成的
工作程序、保留已完成的掃描結果，並將其彙整成最終
報告。請先審查 `result.coverage.completeness`，再將限時
掃描視為完整涵蓋的證據。

### 新增安全性知識庫

傳入架構文件、威脅模型或安全性政策時，請使用
`knowledgeBasePaths`：

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

SDK 接受檔案或目錄，並會以遞迴方式搜尋目錄。
支援的文件格式為 `.md`、`.markdown`、`.txt`、`.pdf` 和 `.docx`。
SDK 會拒絕連結形式的輸入路徑、略過目錄中的連結項目，而且不會將
擷取出的文件內容納入已儲存的掃描結果。

### 新增掃描與後續指示

使用 `scanPrompt` 指定掃描重點，並使用 `postScanPrompt` 要求後續處理：

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

若後續處理失敗，SDK 仍會保留已完成的掃描，並透過
`onWarning` 回報錯誤。對於遭後續處理變更的任何已完成掃描產物，
SDK 也會加以還原。

### 設定掃描預算

設定 `maxCostUsd`，即可在預估模型成本超過上限時停止掃描。
使用 `onCost` 在掃描執行期間追蹤成本：

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

此限額僅用於預估支出，並非硬性上限，因此進行中的
要求完成時，實際費用可能略高於限額。若深度掃描在
Codex Security 彙整已完成工作程序的結果後達到限額，`run` 會傳回
將 `coverage.completeness` 設為 `"partial"` 的結果，並透過
`onWarning` 回報預算警告。

若掃描無法產生已完成的部分結果，`run` 會擲回
`ScanCostLimitExceededError`，並保留任何可用的輸出。

## 處理掃描結果

`ScanResult` 會提供結構化文件、掃描中繼資料和產物
路徑：

| 屬性             | 內容                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | 經密封的掃描資訊清單，包含目標、範圍、產生者及產物記錄。 |
| `findings`           | 本次掃描的發現項目。請從 `findings.findings` 讀取發現項目物件。     |
| `repositoryFindings` | 如有掃描歷史記錄，則提供程式碼庫歷次掃描中尚未解決的發現項目。             |
| `coverage`           | 已審查的範圍、排除項目、延後處理的工作、未解問題及完整度。    |
| `scanDir`            | 掃描目錄。                                                                |
| `threadId`           | 此掃描的 Codex 執行緒識別碼。                                          |
| `turnResult`         | 回合狀態、回應及可用的用量中繼資料。                               |
| `cost`               | 預估的模型與 Token 成本；若無法取得，則為 `null`。                        |
| `reportPath`         | `report.md` 的路徑。                                                           |
| `manifestPath`       | `scan-manifest.json` 的路徑。                                                  |
| `findingsPath`       | `findings.json` 的路徑。                                                       |
| `coveragePath`       | `coverage.json` 的路徑。                                                       |
| `artifactsDir`       | supporting-artifacts 目錄。                                                |
| `sarifPath`          | 產生的 SARIF 路徑；若沒有 SARIF，則為 `null`。                          |
| `pluginVersion`      | 掃描產生者所記錄的版本。                                         |

若後續掃描必須使用相同的外掛程式，請傳入
`expectedPluginVersion: result.pluginVersion`。如果已安裝的外掛程式版本
不同，SDK 會拒絕該次掃描。

直接使用結構化的發現項目和涵蓋範圍：

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

發現項目可包含 `codeEvidence`、`rootCause`、`validation`、
`attackPath`、`remediationTests` 和 `preventiveControls` 等選填欄位。

針對整個程式碼庫的發現項目，`confirmedInLatestScan` 可區分最新掃描中發現的項目
與先前發現但仍未解決的項目：

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

涵蓋完整度為 `complete`、`partial` 或 `unknown`。在將掃描結果作為
安全性決策的依據之前，請先審查延後審查的範圍、排除項目及
尚待釐清的問題。

`result.toJSON()` 會以單一可直接轉換為 JSON 的物件，傳回資訊清單、程式碼庫與本次掃描的發現項目、
涵蓋範圍、掃描與執行緒識別碼、`reportPath`、`artifactsDir`、
`sarifPath`、成本及輪次中繼資料。

## 追蹤或取消掃描

傳入 `ScanOptions` 回呼，以回報掃描啟動、工作程式進度及
連線重試情形：

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

傳入 `AbortSignal`，以處理來自請求、工作控制器
或逾時的取消操作：

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

掃描中斷時，可能會在 `scanDir` 留下部分輸出。若需要調查結果，請保留該
目錄。

顯示掃描設定進度的應用程式，也可以使用 `ScanOptions` 的
生命週期回呼：

| 回呼                            | 呼叫時機                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | 掃描選取身分驗證方法時。          |
| `onOutputArchived(archiveDir)`      | 現有結果移至封存目錄時。      |
| `onOutputDirReady(scanDir)`         | 私有掃描目錄準備就緒時。                 |
| `onScanStarted()`                   | 掃描設定完成並開始執行時。           |
| `onTrustedAccessStatus(status)`     | 可取得 Trusted Access 狀態時。             |
| `onReconnect(attempt, maxAttempts)` | SDK 重試已中斷連線的掃描串流時。          |
| `onActivity(activity)`              | 指令、工具、推理步驟或訊息更新時。 |
| `onProgress(progress)`              | 掃描階段或已審查的檔案數量變更時。       |
| `onWorkerStatus(status)`            | 工作程式的預檢或分派狀態變更時。         |
| `onSessionEvent(session)`           | 掃描工作階段或工作程式工作階段發出事件時。             |
| `onCost(cost)`                      | 可取得更新後的預估掃描成本時。         |
| `onWarning(warning)`                | 掃描回報警告時。                          |
| `onObserverError(observer, error)`  | 另一個掃描生命週期回呼引發錯誤時。     |

Trusted Access 狀態為 `granted`、`not_granted` 或 `unknown`。缺少存取權或
存取狀態不明時，也會觸發 `onWarning`。

`onSessionEvent` 接收的事件未經遮蔽處理，且可能包含原始
程式碼或憑證。將這些事件傳送至共用紀錄或其他
服務前，請先加以篩選。

## 設定執行階段與憑證

需要特定的外掛程式、解譯器或
Codex 設定時，請傳入執行階段組態：

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` 接受外掛程式目錄或 ZIP 檔。`pythonPath` 用於選取
外掛程式解譯器。`codexOverrides` 會將支援的值合併至隔離的
Codex 組態。掃描預設使用 `gpt-5.6-sol`，並採用
極高推理強度。將 `model` 與 `model_reasoning_effort` 設定於 `codexOverrides` 中，即可使用
不同的模型或推理強度。若要使用 [Amazon
Bedrock](/zh-Hant/codex/security/cli/reference#use-amazon-bedrock)，請
將 `model_provider` 與 `model` 設定於 `codexOverrides` 中。

`codexOverrides` 無法限制掃描對檔案系統的存取，也無法變更其
核准政策。請參閱[本機掃描
權限](/zh-Hant/codex/security/cli/reference#local-scan-permissions)。

若使用 OpenRouter 或 Fireworks，也須提供對應的 API 金鑰，並在
`codexOverrides` 中設定完整的供應商組態。例如，請設定
`OPENROUTER_API_KEY` 並設定 OpenRouter：

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

若使用 Fireworks，請將兩個 `openrouter` 鍵都改為 `fireworks`，將 `name` 設為
`Fireworks AI`，將 `env_key` 設為 `FIREWORKS_API_KEY`，使用
`https://api.fireworks.ai/inference/v1` 作為 `base_url`，並選取 Fireworks
模型。

用戶端也提供支援的身分驗證方法：

| 方法                     | 用途                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | 使用 API 金鑰對隔離的執行階段進行身分驗證。          |
| `loginChatGPT()`           | 啟動瀏覽器登入流程，並傳回登入控制代碼。     |
| `loginChatGPTDeviceCode()` | 啟動裝置代碼登入流程，並傳回登入控制代碼。 |
| `account()`                | 傳回目前的身分驗證狀態。                    |
| `logout()`                 | 清除隔離環境中的身分驗證資訊。                              |

登入控制代碼提供 `waitForInstructions`、`authUrl`、`verificationUrl`、
`userCode`、`wait` 和 `cancel`，讓應用程式能夠顯示並完成
所選的登入流程。SDK 可重複使用儲存於檔案中的 Codex 登入資訊。API 金鑰
適合用於 CI 和伺服器端自動化。

當 API 金鑰和已儲存的登入資訊皆可用時，SDK 預設會使用 API
金鑰。若要改用 ChatGPT 登入，請為掃描選取該方式：

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

設定 `auth: "api-key"`，即可要求使用環境中的 API 金鑰。`preflight` 也接受
相同的 `auth` 選項。

## 處理掃描錯誤

根據應用程式可採取的處理動作，
捕捉對應的匯出錯誤類別：

| 錯誤                            | 含義                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | 掃描需要受支援的憑證。                               |
| `ConfigurationError`             | Codex 組態或覆寫設定不符合要求。                  |
| `InvalidTargetError`             | 程式碼庫、路徑、模式或 Git 目標不符合要求。           |
| `OutputDirectoryError`           | 輸出位置或其權限不符合要求。             |
| `OutputInsideProtectedRootError` | 輸出目錄位於所掃描的程式碼庫或工作樹內。 |
| `PluginPythonUnavailableError`   | 沒有可用的 Python 解譯器。                        |
| `PluginBootstrapError`           | 外掛程式執行階段無法啟動。                                |
| `ScanCostLimitExceededError`     | 掃描超出預估成本上限。                        |
| `IncompleteScanError`            | 掃描在產生所需結果前就已結束。               |
| `ContractValidationError`        | 已完成的掃描傳回結構化契約錯誤。             |
| `ScanInterruptedError`           | 掃描因中斷而停止，且可能留下部分輸出。 |

接著請參閱 [CLI 快速入門](/zh-Hant/codex/security/cli)、[CI
指南](/zh-Hant/codex/security/cli/ci)或 [CLI
參考資料](/zh-Hant/codex/security/cli/reference)。
