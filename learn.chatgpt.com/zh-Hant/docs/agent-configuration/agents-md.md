<!-- source: https://learn.chatgpt.com/zh-Hant/docs/agent-configuration/agents-md -->

Codex 在執行任何工作前，會先讀取 `AGENTS.md` 檔案。透過分層套用全域指引與專案專用覆寫，無論開啟哪個程式碼庫，每次開始任務時都能遵循一致的規範。

## Codex 如何尋找指引

Codex 啟動時會建立指示鏈（每次執行建立一次；在 TUI 中，這通常表示每次啟動工作階段時建立一次）。尋找指引時會依照以下優先順序：

1. **全域範圍：** 在您的 Codex 主目錄中（預設為 `~/.codex`，除非您設定 `CODEX_HOME`），如果 `AGENTS.override.md` 存在，Codex 會讀取該檔案；否則，Codex 會讀取 `AGENTS.md`。Codex 在此層級只會使用第一個非空檔案。
2. **專案範圍：** 從專案根目錄（通常是 Git 根目錄）開始，Codex 會沿著目錄向下搜尋到您目前的工作目錄。如果 Codex 找不到專案根目錄，就只會檢查目前的目錄。對路徑上的每個目錄，Codex 會依序檢查 `AGENTS.override.md`、`AGENTS.md`，再檢查 `project_doc_fallback_filenames` 中設定的備用檔名。每個目錄最多只會納入一個檔案。
3. **合併順序：** Codex 會從根目錄開始向下串接檔案，並以空白行分隔。較接近目前目錄的檔案會覆寫先前的指引，因為它們在合併後的提示詞中出現得較晚。

Codex 會略過空檔案；合併後的大小一旦達到由 `project_doc_max_bytes` 定義的上限（預設為 32 KiB），就會停止加入檔案。如需這些設定項目的詳細資訊，請參閱 [專案指示搜尋機制](/zh-Hant/codex/config-file/config-advanced#project-instructions-discovery)。達到上限時，請提高限制，或將指示拆分到巢狀目錄中。

## 建立全域指引

在 Codex 主目錄中建立持續適用的預設設定，讓每個程式碼庫都能繼承您的工作規範。

1. 確認該目錄存在：

   ```bash
   mkdir -p ~/.codex

2. 建立 `~/.codex/AGENTS.md`，並加入可重複使用的偏好設定：

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. 在任意位置執行 Codex，確認它會載入該檔案：

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   預期結果：Codex 會先引用 `~/.codex/AGENTS.md` 中的項目，再提出工作方案。

需要暫時覆寫全域設定但不想刪除基礎檔案時，請使用 `~/.codex/AGENTS.override.md`。移除覆寫檔即可還原共用指引。

## 分層套用專案指示

程式碼庫層級的檔案可讓 Codex 持續掌握專案規範，同時繼承您的全域預設設定。

1. 在程式碼庫根目錄中新增 `AGENTS.md` 檔案，內容涵蓋基本設定：

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. 當特定團隊需要不同規則時，請在巢狀目錄中新增覆寫檔。例如，在 `services/payments/` 中建立 `AGENTS.override.md`：

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. 從 payments 目錄啟動 Codex：

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   預期結果：Codex 會先列出全域檔案，接著是程式碼庫根目錄的 `AGENTS.md`，最後是 payments 覆寫檔。

Codex 搜尋到目前的目錄後就會停止，因此覆寫檔應盡可能放在最接近特定工作內容的目錄中。

以下是新增全域檔案與 payments 專用覆寫檔後的程式碼庫範例：

## 新增程式碼審查規則

若要使用 [GitHub 中的 Codex 程式碼審查](/zh-Hant/codex/third-party/github#customize-what-codex-reviews)，
請在最接近這些規則所適用程式碼的 `AGENTS.md` 中
新增 `## Code Review Rules` 區段。將整個程式碼庫適用的檢查放在根目錄，特定服務的
檢查則放在巢狀檔案中。

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

規則應保持簡潔，說明應標記的行為及任何安全的處理方式或
例外，並將格式與 lint 檢查交由 CI 處理。請參閱 [自訂
Codex 的審查內容](/zh-Hant/codex/third-party/github#customize-what-codex-reviews)，瞭解
設定與規則撰寫指南。

## 自訂備用檔名

若您的程式碼庫已使用不同的檔名（例如 `TEAM_GUIDE.md`），請將該檔名加入備用清單，讓 Codex 將它視為指示檔案。

1. 編輯 Codex 組態：

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. 重新啟動 Codex 或執行新指令，以載入更新後的組態。

目前 Codex 會依下列順序檢查每個目錄：`AGENTS.override.md`、`AGENTS.md`、`TEAM_GUIDE.md`、`.agents.md`。Codex 在尋找指示時會忽略不在此清單中的檔名。較高的位元組上限可讓合併後的指引在截斷前包含更多內容。

設定備用清單後，Codex 會將替代檔案視為指示：

若要使用不同的設定檔（例如專案專用的自動化使用者），請設定 `CODEX_HOME` 環境變數：

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

預期結果：輸出會列出以自訂 `.codex` 目錄為基準的檔案路徑。

## 驗證您的設定

- 在程式碼庫根目錄執行 `codex --ask-for-approval never "Summarize the current instructions."`。Codex 應依優先順序輸出全域與專案檔案中的指引。
- 使用 `codex --cd subdir --ask-for-approval never "Show which instruction files are active."`，確認巢狀覆寫會取代範圍較廣的規則。
- 若要稽核 Codex 載入了哪些指示檔案，請使用 `codex -c log_dir=./.codex-log` 啟用純文字 TUI 日誌，並檢查 `./.codex-log/codex-tui.log`；如果已啟用工作階段記錄，也可以檢查最新的 `session-*.jsonl` 檔案。
- 如果指示看起來不是最新的，請在目標目錄中重新啟動 Codex。Codex 每次執行時（以及每個 TUI 工作階段開始時）都會重建指示鏈，因此無須手動清除快取。

## 排解指示搜尋問題

- **未載入任何內容：** 確認您位於預期的程式碼庫中，且 `codex status` 回報的工作區根目錄符合預期。請確認指示檔案包含內容；Codex 會忽略空檔案。
- **出現非預期的指引：** 在目錄樹較上層或 Codex 主目錄中尋找 `AGENTS.override.md`。重新命名或移除覆寫檔，即可改用一般檔案。
- **Codex 忽略備用檔名：** 確認列在 `project_doc_fallback_filenames` 中的檔名沒有拼字錯誤，然後重新啟動 Codex，讓更新後的組態生效。
- **指示遭到截斷：** 提高 `project_doc_max_bytes` 的值，或將大型檔案拆分到巢狀目錄中，以確保重要指引保持完整。
- **設定檔混淆：** 在啟動 Codex 前執行 `echo $CODEX_HOME`。非預設值會讓 Codex 指向另一個主目錄，而不是您所編輯的主目錄。

## 後續步驟

- 請造訪 [AGENTS.md](https://agents.md) 官方網站以取得更多資訊。
- 請參閱 [向 Codex 提供提示詞](/zh-Hant/codex/prompting)，瞭解適合與持續性指引搭配使用的對話模式。
