<!-- source: https://learn.chatgpt.com/zh-Hant/docs/github-action -->

使用 Codex GitHub Action (`openai/codex-action@v1`)，即可在 CI/CD 作業中執行 Codex、套用修補程式，或從 GitHub Actions 工作流程發布審查意見。
此 Action 會安裝 Codex CLI，在您提供 API 金鑰時啟動 Responses API Proxy，並以您指定的權限執行 `codex exec`。

若有以下需求，請使用此 Action：

- 無須自行管理 CLI，即可自動取得 Codex 對 Pull Request 或版本資訊的回饋。
- 將由 Codex 執行的品質檢查納入 CI 管線，以把關變更。
- 從工作流程檔案執行可重複的 Codex 任務（程式碼審查、版本發布準備、遷移作業）。

如需 CI 範例，請參閱 [非互動模式](/zh-Hant/codex/non-interactive-mode)；原始碼請見 [openai/codex-action 程式碼庫](https://github.com/openai/codex-action)。

## 先決條件

- 將 OpenAI 金鑰儲存為 GitHub 機密資訊（例如 `OPENAI_API_KEY`），並在工作流程中參照該機密資訊。
- 在 Linux 或 macOS 執行器上執行此作業。若使用 Windows，請設定 `safety-strategy: unsafe`。
- 請先簽出程式碼，再叫用此 Action，讓 Codex 能讀取程式碼庫內容。
- 決定要執行哪些提示詞。您可以透過 `prompt` 提供內嵌文字，或使用 `prompt-file` 指向已提交至程式碼庫的檔案。

## 範例工作流程

下方範例工作流程會審查新的 Pull Request、擷取 Codex 的回應，並將回應發布至該 PR。

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

將 `.github/codex/prompts/review.md` 替換為您自己的提示詞檔案，或使用 `prompt` 輸入來提供內嵌文字。此範例也會將 Codex 的最終訊息寫入 `codex-output.md`，供稍後檢查或上傳為成品。

## 設定 `codex exec`

透過設定對應至 `codex exec` 選項的 Action 輸入，即可微調 Codex 的執行方式：

- `prompt` 或 `prompt-file`（擇一）：提供內嵌指示，或提供程式碼庫中含有任務內容的 Markdown 或文字檔案路徑。建議將提示詞儲存在 `.github/codex/prompts/`。
- `codex-args`：額外的 CLI 旗標。請提供 JSON 陣列（例如 `["--ephemeral"]`）或 Shell 字串（`--profile ci`），以設定工作階段、設定檔或 MCP 設定。
- `model` 和 `effort`：選擇所需的 Codex 智慧體組態；留空即可使用預設值。
- `sandbox`：請依 Codex 執行期間所需的權限，選擇相符的沙盒模式（`workspace-write`、`read-only`、`danger-full-access`）。
- `output-file`：將 Codex 的最終訊息儲存至磁碟，供後續步驟上傳或進行差異比對。
- `codex-version`：鎖定特定 CLI 版本。留空則使用最新發布的版本。
- `codex-home`：指定共用的 Codex 主目錄，以便跨步驟重複使用組態檔或 MCP 設定。

## 管理權限

除非您加以限制，否則 Codex 在 GitHub 託管的執行器上擁有廣泛的存取權。請使用以下輸入控制其可存取的範圍：

- `safety-strategy`（預設為 `drop-sudo`）會在執行 Codex 前移除 `sudo`。這項操作在該作業中無法復原，並可保護記憶體中的機密資訊。在 Windows 上，您必須設定 `safety-strategy: unsafe`。
- `unprivileged-user` 會搭配使用 `safety-strategy: unprivileged-user` 和 `codex-user`，讓 Codex 以指定帳戶執行。請確保該使用者可讀寫程式碼庫的簽出目錄（如需修正擁有權，請參閱 [`unprivileged-user` 範例](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml)）。
- `read-only` 可防止 Codex 變更檔案或使用網路，但 Codex 仍會以提升的權限執行。請勿只依賴 `read-only` 來保護機密資訊。
- `sandbox` 會限制 Codex 本身對檔案系統和網路的存取。請選擇在仍可完成任務的前提下，限制最嚴格的選項。
- `allow-users` 和 `allow-bots` 可限制哪些人能觸發工作流程。預設只有具備寫入權限的使用者可執行此 Action；請明確列出其他受信任帳戶，或將欄位留空以沿用預設行為。

## 擷取輸出

此 Action 會透過 `final-message` 輸出提供 Codex 的最後一則訊息。您可以將其對應至作業輸出（如上所示），或在後續步驟中直接處理。如果您想從執行器收集完整記錄，請將 `output-file` 與成品上傳功能搭配使用。需要結構化資料時，請將 `--output-schema` 透過 `codex-args` 傳入，以強制採用 JSON 結構。

## 安全性檢查清單

- 限制可啟動工作流程的使用者。應優先採用受信任的事件或明確核准，而不是允許所有人針對您的程式碼庫執行 Codex。
- 清理來自 Pull Request、提交訊息或議題內文的提示詞輸入，以避免提示注入。將內容提供給 Codex 前，請先審查其中的 HTML 註解或隱藏文字。
- 若要保護您的 `OPENAI_API_KEY`，請將 `safety-strategy` 維持為 `drop-sudo`，或改用非特權使用者執行 Codex。切勿讓此 Action 在多租戶執行器上處於 `unsafe` 模式。
- 請將 Codex 安排為作業的最後一個步驟，以免後續步驟繼承任何非預期的狀態變更。
- 若您懷疑 Proxy 記錄或 Action 輸出洩露了機密內容，請立即輪替金鑰。

## 疑難排解

- **您同時設定了 prompt 和 prompt-file**：移除重複的輸入，確保只提供一個來源。
- **responses-api-proxy 未寫入伺服器資訊**：確認 API 金鑰已提供且有效；只有在您提供 `openai-api-key` 時，Proxy 才會啟動。
- **預期會移除 `sudo`，但 `sudo` 仍可成功執行**：確認先前沒有任何步驟還原 `sudo`，且執行器作業系統為 Linux 或 macOS。請以全新作業重新執行。
- **使用 `drop-sudo` 後發生權限錯誤**：請在此 Action 執行前授予寫入權限（例如使用 `chmod -R g+rwX "$GITHUB_WORKSPACE"` 或採用 unprivileged-user 模式）。
- **未經授權的觸發遭到封鎖**：如果您需要允許預設具備寫入權限的協作者以外的服務帳戶，請調整 `allow-users` 或 `allow-bots` 輸入。
