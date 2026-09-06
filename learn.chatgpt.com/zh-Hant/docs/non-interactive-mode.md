<!-- source: https://learn.chatgpt.com/zh-Hant/docs/non-interactive-mode -->

非互動模式可讓你透過指令碼執行 Codex，例如在持續整合（CI）作業中執行，而無須開啟互動式 TUI。
請使用 `codex exec` 呼叫此模式。

如需各旗標的詳細資訊，請參閱 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)。

## 何時使用 `codex exec`

若想讓 Codex 執行下列操作，請使用 `codex exec`：

- 作為管線的一部分執行，例如 CI、合併前檢查或排程作業。
- 產生可透過管線傳送給其他工具的輸出，例如產生版本說明或摘要。
- 自然融入 CLI 工作流程，將指令輸出串接至 Codex，再將 Codex 的輸出傳送給其他工具。
- 使用明確且預先設定的沙盒與核准設定執行。

## 基本用法

將任務提示詞作為單一引數傳入：

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

在 `codex exec` 執行期間，Codex 會將進度串流至 `stderr`，並只將智慧體的最終訊息輸出至 `stdout`。因此可以輕鬆重新導向最終結果，或透過管線傳送至其他工具：

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

若不想將工作階段執行記錄檔保存在磁碟上，請使用 `--ephemeral`：

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

若透過管線傳入 stdin，且同時提供提示詞引數，Codex 會將提示詞視為指示，並將管線傳入的內容視為額外上下文。

如此一來，即可透過單一指令產生輸入，並直接傳送給 Codex：

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

如需更進階的 stdin 管線傳送模式，請參閱[進階 stdin 管線傳送](#advanced-stdin-piping)。

## 權限與安全性

根據預設，`codex exec` 會在唯讀沙盒中執行。進行自動化時，請設定工作流程所需的最低必要權限：

- 允許編輯：`codex exec --sandbox workspace-write "<task>"`
- 允許更廣泛的存取權：`codex exec --sandbox danger-full-access "<task>"`

只能在受控環境中使用 `danger-full-access`，例如隔離的 CI 執行器或容器。

Codex 保留 `codex exec --full-auto` 作為已棄用的相容性旗標，並會輸出警告。新指令碼應優先使用明確的 `--sandbox workspace-write` 旗標。

若執行時不需要載入 `$CODEX_HOME/config.toml`，請使用 `--ignore-user-config`；若需要在受控自動化環境中略過使用者和專案的 execpolicy `.rules` 檔案，請使用 `--ignore-rules`。

如果為已啟用的 MCP 伺服器設定 `required = true`，但伺服器初始化失敗，`codex exec` 會回報錯誤並結束，而不會在缺少該伺服器的情況下繼續執行。

## 讓輸出可供機器讀取

若要在指令碼中處理 Codex 輸出，請使用 JSON Lines 輸出：

```bash
codex exec --json "summarize the repo structure" | jq

啟用 `--json` 後，`stdout` 會成為 JSON Lines（JSONL）串流，讓你擷取 Codex 在執行期間發出的每個事件。事件類型包括 `thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*` 和 `error`。

項目類型包括智慧體訊息、推理、指令執行、檔案變更、MCP 工具呼叫、網頁搜尋及計畫更新。

JSON 串流範例，每一行都是一個 JSON 物件：

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

若只需要最終訊息，請使用 `-o <path>`/`--output-last-message <path>` 將其寫入檔案。這會將最終訊息寫入檔案，同時仍輸出至 `stdout`，詳情請參閱 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)。

## 使用結構描述建立結構化輸出

如果後續步驟需要結構化資料，請使用 `--output-schema` 要求最終回應符合 JSON Schema。
這適用於需要穩定欄位的自動化工作流程，例如作業摘要、風險報告或發行版本中繼資料。

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

使用結構描述執行 Codex，並將最終 JSON 回應寫入磁碟：

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

最終輸出範例（stdout）：

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## 在自動化環境中進行身分驗證

`codex exec` 預設會沿用已儲存的 CLI 身分驗證。在 CI 中，通常會明確提供認證資訊：

如果受信任的雲端或 CI 執行環境已取得短效工作負載
Token，請使用
[工作負載身分聯合](/zh-Hant/codex/enterprise/workload-identity)
，而不是儲存 OpenAI 認證資訊。

### 使用 API 金鑰進行身分驗證

在 GitHub Actions 中，請使用 [Codex GitHub Action](/zh-Hant/codex/github-action)，而不是自行安裝 CLI 並完成身分驗證。此 Action 會安裝 Codex、啟動 Responses API 代理伺服器，並採用可設定的安全策略執行 Codex，藉此降低 API 金鑰暴露的風險。

在會簽出或執行程式碼庫所控制之程式碼的工作流程中，請勿將 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 設為作業層級的環境變數。同一作業中的建置指令碼、測試、依賴項生命週期掛勾，或遭入侵的 Action，都可能讀取這些環境變數。

對於其他自動化環境，請只為需要該金鑰的 Codex 呼叫設定 `CODEX_API_KEY`，
並確保同一
程序環境中不會執行不受信任的程式碼。

若要在單次執行中使用不同的 API 金鑰，請直接在指令中設定 `CODEX_API_KEY`：

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

`CODEX_API_KEY` 可搭配 `codex exec`、`codex review`、TypeScript
SDK 及 `codex exec-server --remote` 使用。

如果需要使用 Codex 使用者帳戶而非 API 金鑰執行 CI/CD 作業，請閱讀本節。
適用對象包括在受信任的執行器上使用由 ChatGPT 管理的 Codex 存取權的企業團隊，
以及需要採用 ChatGPT/Codex 速率限制，而非 API 金鑰用量的使用者。

API 金鑰較容易佈建和輪替，
因此適合作為自動化的預設選項。只有明確需要以自己的
Codex 帳戶身分執行時，才應採用這種方式。

請將 `~/.codex/auth.json` 視同密碼保護，因為其中包含存取權杖。切勿
提交此檔案、將其貼到工單中，或在對話中分享。

請勿將此工作流程用於公開或開放原始碼程式碼庫。如果 `codex login`
無法在執行器上使用，請透過安全儲存空間預先提供 `auth.json`，接著在執行器上執行
Codex，讓 Codex 就地更新該檔案，並保留更新後的檔案
供後續執行使用。

請參閱[在 CI/CD 中維護 Codex 帳戶身分驗證（進階）](/codex/auth/ci-cd-auth)。

## 繼續非互動式工作階段

如果需要繼續先前的執行作業，例如兩階段管線，請使用 `resume` 子指令：

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

也可以使用 `codex exec resume <SESSION_ID>` 指定特定的工作階段 ID。

## 必須使用 Git 程式碼庫

為避免破壞性變更，Codex 要求指令必須在 Git 程式碼庫內執行。如果確定環境安全，可使用 `codex exec --skip-git-repo-check` 略過這項檢查。

## 常見自動化模式

### 範例：在 GitHub Actions 中自動修正 CI 失敗問題

在 GitHub Actions 工作流程中，請使用 [`openai/codex-action`](https://github.com/openai/codex-action)，而不要自行安裝 Codex 並將 API 金鑰傳給 Shell 步驟。此 Action 會為 OpenAI API 金鑰啟動安全的代理伺服器。

當 CI 工作流程失敗時，可使用 Codex 自動提出修正建議。模式如下：

1. 當主要 CI 工作流程因錯誤結束時，觸發後續工作流程。
2. 僅使用程式碼庫唯讀權限，簽出導致失敗的提交。
3. 在執行 Codex 前先執行設定指令，且不要讓這些步驟接觸 OpenAI API 金鑰。
4. 執行 Codex GitHub Action。
5. 將 Codex 的本機變更儲存為修補程式成品。
6. 在另一個獨立作業中，套用修補程式並建立 Pull Request。

下方的 Codex 作業僅具備 `contents: read` 權限。Codex 執行完畢後，只會將差異序列化為成品。`open_pr` 作業會取得程式碼庫寫入權限，但不會取得 `OPENAI_API_KEY`。

此範例以 Node.js 專案為前提。請依您的技術堆疊調整設定和測試指令。

如需更深入的安全性檢查清單，請參閱 [Codex GitHub Action 安全性指引](https://github.com/openai/codex-action/blob/main/docs/security.md)。

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## 進階 stdin 管線傳遞

當另一項指令為 Codex 產生輸入內容時，請根據指示的來源選擇 stdin 模式。如果您已確定指示內容，並想將管線輸出作為上下文傳入，請使用 prompt-plus-stdin。如果 stdin 應作為完整提示詞，請使用 `codex exec -`。

### 使用 prompt-plus-stdin

當另一項指令已產生您希望 Codex 檢查的資料時，prompt-plus-stdin 十分實用。在此模式中，您自行撰寫指示，再將輸出透過管線傳入作為上下文，因此非常適合以指令輸出、記錄和產生的資料為核心的 CLI 工作流程。

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### 彙整記錄內容

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### 檢查 TLS 或 HTTP 問題

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### 準備可直接貼到 Slack 的更新內容

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### 根據 CI 記錄草擬 Pull Request 留言

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### 將 stdin 作為提示詞時，使用 `codex exec -`

如果省略提示詞引數，Codex 會從 stdin 讀取提示詞。若要明確強制採用此行為，請使用 `codex exec -`。

當另一項指令或指令碼動態產生完整提示詞時，`-` 哨兵值十分實用。這種方式適用於將提示詞儲存在檔案中、使用 shell 指令碼組合提示詞，或先將即時指令輸出與指示結合，再把完整提示詞交給 Codex。

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
