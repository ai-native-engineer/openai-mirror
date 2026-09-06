<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/cli -->

Codex Security 可協助安全性和工程團隊找出、確認並修正
漏洞。使用其指令列介面 (CLI) 掃描
您擁有或獲准評估的程式碼庫，持續審查發現項目，
並在變更合併前加以檢查。

  `@openai/codex-security` 套件可公開取得。執行掃描必須具備 Codex Security
  存取權。若要在 Codex 中執行互動式掃描，請先參閱 [Codex Security
  外掛程式快速入門](/zh-Hant/codex/security/plugin)。若使用已連線的 GitHub
  程式碼庫，請參閱 [Codex Security 雲端服務設定](/zh-Hant/codex/security/setup)。

## 檢查先決條件

CLI 需要 Node.js 22（22.13.0 或更新版本）、24 或 26。掃描、批次掃描、
匯出、掃描紀錄和已儲存的發現項目也需要 Python 3.10 或更新版本。
如需詳細資訊，請參閱 [身分驗證與
先決條件](/zh-Hant/codex/security/cli/reference#authentication-and-prerequisites)。

## 設定並驗證 CLI

使用 `npx` 執行 CLI，並檢查其版本：

```bash
npx @openai/codex-security --version

若要同時查看套件版本及其隨附外掛程式的版本，請執行：

```bash
npx @openai/codex-security info --json

請參閱 [CLI 和 SDK 版本資訊](https://github.com/openai/codex-security/releases)，
以瞭解套件變更。

列出可用的指令：

```bash
npx @openai/codex-security --help

另請參閱 [CLI 參考資料](/zh-Hant/codex/security/cli/reference)。

## 登入

若在本機使用，請以您的 ChatGPT 帳戶登入：

```bash
npx @openai/codex-security login

在遠端或無頭機器上，請使用裝置身分驗證：

```bash
npx @openai/codex-security login --device-auth

針對 CI 和其他自動化工作流程，請設定 OpenAI API 金鑰：

```bash

如需設定 AWS 憑證，請參閱 [Amazon Bedrock
設定](/zh-Hant/codex/security/cli/reference#use-amazon-bedrock)。若使用 [OpenRouter 或
Fireworks](/zh-Hant/codex/security/cli/reference#use-openrouter-or-fireworks)，請設定
供應商的 API 金鑰，並使用 `--provider` 和 `--model` 選取模型。

若在已設定 API 金鑰的情況下仍要使用 ChatGPT 登入，請明確選取此方式：

```bash
npx @openai/codex-security scan . --auth chatgpt

若要強制使用環境中的 API 金鑰，請選取 API 金鑰身分驗證：

```bash
npx @openai/codex-security scan . --auth api-key

視您的帳戶和程式碼庫而定，掃描整個程式碼庫時可能還
需要 [Trusted Access for Cyber](https://chatgpt.com/cyber)。

## 準備掃描

請選擇您信任且有權評估的程式碼庫。掃描會使用您的
本機作業系統權限，且不會暫停以等待核准。掃描
程序可能會繼承您的環境，因此請在
開始前移除無關的憑證。請參閱 [本機掃描
權限](/zh-Hant/codex/security/cli/reference#local-scan-permissions)。

請在程式碼庫之外選擇一個目錄，以儲存掃描結果：

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

如果省略 `--output-dir`，Codex Security 會將結果儲存在其專用的持久
狀態目錄中。結果可能包含原始碼摘錄和漏洞詳細資料，
因此請選擇私密位置，並採用適當的保留政策。

如果預設狀態目錄不可寫入，請選擇位於受掃描程式碼庫
之外的可寫入目錄：

```bash

開始掃描前，請檢查程式碼庫、目標和輸出目錄：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

試執行會檢查本機輸入，包括所有 `--knowledge-base` 路徑，
但不會啟動 Codex、載入憑證，或探查外掛程式的 Python
解譯器。

## 執行第一次掃描

執行標準掃描，並將結果保留在所選目錄中：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

互動式終端會顯示即時掃描儀表板。加入 `--headless` 可改為顯示
純文字進度行。CI 和沒有互動式工作階段的終端
會自動使用純文字進度。

儀表板也會顯示即時工作階段的詳細資訊。這些資訊可能包含原始碼
或憑證，因此請先審查再分享。

CLI 預設會將掃描進度和完成摘要寫入 stderr。
它不會將完整掃描結果輸出至 stdout。掃描完成時會輸出
如下摘要：

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

Token 使用量和預估費用會在可用時顯示。若要將完整
結果以機器可讀的 JSON 輸出，請明確要求結構化輸出：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

掃描預設僅產生報告，因此發現項目仍可供本機
審查。當您準備好[在 CI 中執行
掃描](/zh-Hant/codex/security/cli/ci)時，可考慮加入嚴重性門檻。

## 選擇模型和推理程度

掃描預設使用 `gpt-5.6-sol` 模型，推理程度為 `xhigh`。如果任務需要，請選取
其他模型和推理程度：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

支援的推理程度包括 `minimal`、`low`、`medium`、`high`、`xhigh` 和
`max`。

## 審查結果

開啟 `report.md` 即可查看易於閱讀的結果。掃描目錄也包含
供自動化使用的結構化檔案：

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` 會記錄目標、範圍、產生者和已密封的
  成品。
- `findings.json` 會記錄每個發現項目的嚴重性、可信度、位置、證據和
  補救措施。
- `coverage.json` 會記錄已審查的範圍、排除項目、延後處理的工作、尚待釐清的
  問題，以及涵蓋範圍的完整性。

涵蓋狀態可為 `complete`、`partial` 或 `unknown`。在將掃描視為審查證據前，請先查看延後處理的區域或
尚待釐清的問題。
[CLI 參考資料](/zh-Hant/codex/security/cli/reference#scan-artifacts)說明
完整的成品與輸出規範。

## 審查發現項目並修補問題

互動式掃描完成並產生發現項目後，CLI 會提供發現項目
瀏覽器。請審查相關證據，並選擇要修正的發現項目。您可在 Codex
桌面 App 中找到已儲存的任務。

若不使用瀏覽器，而要修補高嚴重性和重大嚴重性的發現項目：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

加入 `--create-pr`，即可提交已驗證的修補程式並建立 GitHub Pull Request。

您也可以修補已儲存的發現項目，或匯入 Linear 議題。請參閱
[`validate` 和 `patch` 參考資料](/zh-Hant/codex/security/cli/reference#codex-security-validate-and-codex-security-patch)。

## 選擇下一種掃描方式

若程式碼庫包含彼此獨立的服務或套件，請使用路徑掃描：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

審查基準修訂版本與 `HEAD` 之間已提交的變更：

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

審查相對於 `HEAD` 的已暫存與未暫存變更：

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

執行差異與工作樹掃描時，程式碼庫引數必須指定 Git
工作樹根目錄。開始差異掃描前，請先擷取所選修訂版本。

當程式碼庫或路徑需要更廣泛的審查時，請使用深度模式：

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

若要控制工作程序、子代理程式和掃描停止的時機：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

這些選項需要深度模式；此模式支援程式碼庫和路徑目標，
但不支援差異或工作樹掃描。在此，`--workers` 控制單次掃描中獨立的
標準掃描工作程序；`bulk-scan --workers` 控制同時執行的
程式碼庫掃描。`--max-time-hours` 可設為不超過 `96` 的正數，
包括以小數表示的小時數。達到上限時，掃描會停止尚未完成的工作程序，
保留已完成的掃描結果，並將其彙整至最終報告。

## 新增架構與安全性上下文

請提供架構文件、威脅模型或安全性政策，作為掃描
上下文。這有助於 Codex Security 根據您系統
實際的運作方式評估發現項目：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## 新增自訂掃描指示

新增指示，讓掃描聚焦於您的安全性優先事項。請使用
第二個檔案提供後續指示：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

掃描成功後，或掃描涵蓋範圍不完整或發生錯誤後，
後續指示都會在同一個已完成身分驗證的工作階段中執行。如果後續指示執行失敗，CLI
會發出警告並保留已完成的掃描。掃描遭到
取消或達到費用上限時，則不會執行後續指示。這兩個選項也可搭配
`bulk-scan` 使用；CSV 的 `prompt` 欄位可加入各程式碼庫專用的指示。

## 設定掃描預算

使用 `--max-cost`，可在掃描的預估模型費用超過指定上限
（以 USD 計價）時停止掃描：

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

處理中的請求完成時，費用可能略高於上限。如果深度
掃描在 Codex Security 彙整已完成工作程序的
結果後達到上限，CLI 會儲存已完成的報告，將涵蓋狀態標示為 `partial`，
並傳回結束代碼 `2`。如果掃描無法產生已完成的報告，任何
可用的部分輸出仍會保留在磁碟上。

## 每次提交前掃描變更

為您的程式碼庫安裝 Git pre-commit 安全性檢查：

```bash
npx @openai/codex-security install-hook

這項檢查會在每次提交前掃描已暫存及未暫存的變更；若出現
高嚴重性發現項目或掃描錯誤，便會阻止提交，且不會取代現有的
pre-commit 指令碼。

## 批次掃描程式碼庫

探索程式碼庫前，請先登入 GitHub：

```bash
gh auth login

從您的 GitHub 帳戶或組織中探索並選取程式碼庫：

```bash
npx @openai/codex-security bulk-scan

互動式流程會排除已封存的程式碼庫及分支程式碼庫，並要求您在
掃描前確認所選的程式碼庫。

若要掃描事先準備好的程式碼庫清單，請提供 CSV 檔案和輸出目錄：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

再次執行相同指令，即可繼續先前的批次掃描。Codex Security
會略過已完成的程式碼庫。加入 `--max-attempts 3`，即可在程式碼庫或掃描發生
暫時性錯誤時重試。

如需瞭解如何探索 GitHub 程式碼庫、準備 CSV、查看掃描活動結果及設定 Docker，請參閱
[執行批次安全性掃描](/zh-Hant/codex/security/cli/bulk-scans)。

## 在 Docker 中執行批次掃描

若您擁有 Codex Security Docker 映像檔的存取權，請在 Linux Docker 主機上使用隨附的
安全強化 Compose 組態和安全性設定檔。
主機必須支援建立非特權使用者命名空間。請提供程式碼庫
CSV，將結果和登入狀態儲存在持久性掛載目錄中，並
透過環境或祕密管理工具提供憑證：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

容器執行批次掃描時不會顯示互動式提示。若要以互動方式探索程式碼庫，請在
Docker 之外使用 CLI。若為私有
程式碼庫，請透過環境或祕密管理工具提供 `GH_TOKEN` 或 `GITHUB_TOKEN`。
容器化掃描也必須符合[登入要求](#sign-in)，包括帳戶和
程式碼庫的存取權。

## 重新檢視已儲存的掃描

列出程式碼庫已儲存的掃描：

```bash
npx @openai/codex-security scans list "$REPOSITORY"

從結果中複製掃描 ID，以檢查其發現項目與組態：

```bash
npx @openai/codex-security scans show SCAN_ID

查看掃描及其工作程序的已儲存事件：

```bash
npx @openai/codex-security scans logs SCAN_ID

已儲存的記錄未遮蔽敏感資訊，可能包含原始程式碼或憑證。分享前
請先審查。

列出程式碼庫各次掃描中尚未結案的發現項目：

```bash
npx @openai/codex-security findings list "$REPOSITORY"

即使最新掃描未確認先前的發現項目，該項目仍會維持未結案狀態。

若要將已審查的發現項目標記為誤判，請說明該項目為何
不適用：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

後續掃描會將這項說明納入考量，但仍會重新檢查目前的程式碼。

使用原始組態，針對目前簽出的版本重新執行相同掃描：

```bash
npx @openai/codex-security scans rerun SCAN_ID

比較兩次掃描，找出新增、持續存在、重新開啟、已解決或狀態不明的
發現項目：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較時會依根本原因自動配對發現項目，並沿用已儲存的
配對結果。

如需瞭解批次掃描的 CSV 格式、掃描歷程篩選條件與指令選項，請參閱
[CLI 參考資料](/zh-Hant/codex/security/cli/reference)。

請接著選擇符合您目標的工作流程：

- [執行批次安全性掃描](/zh-Hant/codex/security/cli/bulk-scans)，以探索 GitHub
  程式碼庫，或掃描已釘選的 CSV 清冊。
- [閱讀 CLI 常見問題](/zh-Hant/codex/security/cli/faq)，查看掃描歷程、
  誤判回饋、涵蓋範圍與修正驗證等問題的解答。
- [在 CI 中執行掃描](/zh-Hant/codex/security/cli/ci)，以審查 Pull Request、保留
  結果，並設定嚴重性政策。
- [使用 CLI 參考資料](/zh-Hant/codex/security/cli/reference)，查看所有旗標、
  輸出格式、產出物與結束代碼。
- [整合 TypeScript SDK](/zh-Hant/codex/security/sdk)，以便透過
  應用程式或開發工具執行掃描。
