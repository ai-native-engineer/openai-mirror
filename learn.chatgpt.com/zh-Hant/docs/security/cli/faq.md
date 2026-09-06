<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli/faq -->

查看有關從終端掃描程式碼庫及管理
安全性發現項目的常見問題解答。如需安裝並執行第一次掃描，請先
參閱 [CLI 快速入門](/zh-Hant/codex/security/cli)。

## 程式碼庫掃描

### 誰可以使用 CLI

`@openai/codex-security` 套件已公開提供。

執行掃描需要 Codex Security 存取權。為獲得最佳結果，請使用通過
[Trusted Access for Cyber](https://chatgpt.com/cyber) 驗證的帳戶。

### 為什麼登入後掃描仍會使用 API 金鑰

當環境包含 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 時，沒有互動式終端的掃描
以及 JSON 和 JSONL 掃描，預設會使用環境中的
API 金鑰，即使已成功透過 ChatGPT 或存取 Token 登入也一樣。
如果也能使用 ChatGPT 登入，具有文字輸出的互動式掃描
會要求您選擇。試執行不會顯示提示或載入認證資料。

若要在掃描中使用已儲存的認證資料，請明確選取：

```bash
npx @openai/codex-security scan . --auth chatgpt

若要強制使用來自 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 的 API 金鑰：

```bash
npx @openai/codex-security scan . --auth api-key

若要讓已儲存的認證資料自動成為預設值，請執行
`unset OPENAI_API_KEY CODEX_API_KEY`。如需了解所有支援的身分驗證模式，
請參閱 [CLI 參考資料](/zh-Hant/codex/security/cli/reference#select-scan-authentication)。

### 批次程式碼庫掃描如何運作

使用 GitHub CLI 登入：

```bash
gh auth login

探索並選取 GitHub 帳戶或組織中的程式碼庫：

```bash
npx @openai/codex-security bulk-scan

若已備妥清單，請提供程式碼庫 CSV 檔案與輸出目錄：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

請參閱 [執行批次安全性掃描](/zh-Hant/codex/security/cli/bulk-scans)，以了解 GitHub
程式碼庫探索、CSV 格式、掃描活動結果及可用選項。

### 中斷的批次掃描可以繼續執行嗎

可以。使用原本的 CSV 和輸出目錄，再次執行相同的批次掃描指令。
Codex Security 會略過已完成掃描的程式碼庫。

加入 `--max-attempts 3`，以便在程式碼庫或掃描發生暫時性錯誤時重試：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

已完成的掃描若涵蓋範圍為 `partial` 或 `unknown`，會保留結果，
並使掃描活動以結束代碼 `2` 結束。即使使用
`--max-attempts`，也不會重試該掃描。

### 掃描如何使用架構與安全性政策

若要傳入架構文件、威脅模型或安全性政策，請使用
`--knowledge-base`：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security 會將這些文件作為目前掃描的上下文。若要了解
支援的檔案類型與目錄處理方式，請參閱 [新增安全性
上下文](/zh-Hant/codex/security/cli/reference#add-security-context)。

## 發現項目與涵蓋範圍

### 團隊可在哪裡找到先前的掃描結果

列出程式碼庫已儲存的掃描：

```bash
npx @openai/codex-security scans list /path/to/repository

使用結果中的掃描 ID，查看該掃描的發現項目：

```bash
npx @openai/codex-security scans show SCAN_ID

每次完成的掃描都會將報告、發現項目、涵蓋範圍及相關
成品一併儲存。如需完整結構，請參閱 [掃描
成品](/zh-Hant/codex/security/cli/reference#scan-artifacts)。

若要檢查已儲存的掃描與工作程序事件，請執行 `scans logs SCAN_ID`。這些紀錄
未經遮蔽，可能包含原始碼或認證資料。

### 如果 CLI 無法儲存掃描歷程，該怎麼辦

Codex Security 會將掃描歷程儲存在工作台資料庫中。如果預設的
狀態目錄無法寫入，請選擇位於
程式碼庫外的私有目錄：

```bash

### 掃描如何區分新發現項目與已知發現項目

列出程式碼庫所有掃描中尚未解決的發現項目：

```bash
npx @openai/codex-security findings list /path/to/repository

清單會標示最新掃描確認的發現項目，以及先前尚未解決、
但此次掃描未確認的發現項目。

比較這兩次掃描的發現項目：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較時，系統會依根本原因自動比對發現項目，重複使用已儲存的
比對結果，並辨識新增、持續存在、重新開啟、已解決和狀態不明的
發現項目。只有在後一次掃描涵蓋原始目標與受影響路徑，且沒有
涵蓋缺口時，發現項目才會被視為已解決。

### 誤判回饋如何運作

檢查已儲存的掃描，找出發現項目實例 ID：

```bash
npx @openai/codex-security scans show SCAN_ID

記錄該發現項目不適用的原因：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

日後對相同程式碼庫執行掃描時，系統會將該說明納入上下文。這些掃描
仍會獨立檢查目前的原始碼、控制措施與可達性。將發現項目
標記為不適用，不會讓系統略過任何規則、路徑或漏洞類別。

如需指令詳細資訊，請參閱 [發現項目
參考資料](/zh-Hant/codex/security/cli/reference#codex-security-findings)。

### 為什麼重複執行掃描會傳回不同的發現項目

即使使用相同的掃描組態，AI 輔助掃描的結果仍可能有所不同。請先
重新執行基準掃描：

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

重新執行掃描時，系統會沿用原始掃描組態，且必須使用相同的外掛程式
版本。如果已安裝的外掛程式有所變更，指令就會停止執行。

比較基準掃描與新掃描：

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

若缺少上下文可能導致差異，請提供共用的架構與安全性指引。
比對功能可以辨識多次執行中實質相同的發現項目，
但無法讓掃描結果具有確定性。請直接重新檢查任何在新掃描中
未出現的重要發現項目。

### 團隊如何確認修正已生效

套用修正後，重新執行原始掃描：

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

比較原始發現項目與新掃描：

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

確認新掃描涵蓋原始目標與受影響路徑，且沒有
涵蓋缺口。接著，請針對目前簽出的程式碼直接重新檢查原始
發現項目：

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

僅憑發現項目未出現或掃描比較，無法證明修正已生效。

### 涵蓋範圍不完整代表什麼

涵蓋範圍可以是 `complete`、`partial` 或 `unknown`。請檢查 `coverage.json`
中的排除路徑、延後檢查的範圍及待釐清問題，再將
掃描結果視為已進行審查的證據。

涵蓋範圍為部分或未知的掃描會傳回結束代碼 `2`，即使沒有
嚴重性政策也一樣。這類掃描仍會保留所有可用的發現項目與涵蓋範圍。後續
掃描若未涵蓋先前發現項目的原始路徑，就無法
證明該發現項目已不存在。

## 自動化與成本

### 深度掃描的時間限制如何運作

開始深度掃描時，設定工作程序的執行期限：

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

預設為 `96` 小時。可使用任何不超過 `96` 的正數，
包括小數。期限到達時，Codex Security 會停止尚未完成的工作程序，
保留已完成的標準掃描結果，並將其彙整至最終報告。如果
沒有任何工作程序完成原始碼審查，報告會記錄部分涵蓋範圍，
CLI 會傳回結束代碼 `2`。

如需讓設定持續生效，或用於批次掃描活動，請將 `max_time_hours` 設定在
`[deep_scan]` 底下，詳見 [深度掃描
組態](/zh-Hant/codex/security/cli/reference#configure-deep-scans)。

### 掃描成本限制如何運作

開始掃描前，以 USD 設定預估成本上限：

```bash
npx @openai/codex-security scan . --max-cost 5

此限制只是預估值，並非硬性支出上限。已在進行中的
請求完成時，費用可能超過此限制。如果深度掃描在 Codex Security
彙整已完成工作程序的結果之後達到限制，CLI 會儲存已完成、但涵蓋範圍為部分的
報告，並以結束代碼 `2` 結束。否則，系統會保留
任何可用的部分輸出。

### 掃描可以檢查提交和 Pull Request 嗎

安裝提交前的安全性檢查，涵蓋已暫存和未暫存的變更：

```bash
npx @openai/codex-security install-hook

針對 Pull Request 檢查，掃描已提交的變更並設定嚴重性
門檻：

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

完整掃描發現嚴重性達到或超過所選等級的問題時，會傳回結束代碼 `1`。
請參閱[在 CI 中執行掃描](/zh-Hant/codex/security/cli/ci)，瞭解
完整的 GitHub Actions 工作流程、成品處理和 SARIF 匯出。

### 其他應用程式可以直接執行掃描嗎

可以。使用 [TypeScript SDK](/zh-Hant/codex/security/sdk)，即可在應用程式或開發工具中啟動掃描、選擇
目標、檢查發現的問題和涵蓋範圍、追蹤進度，
並套用成本控制。
