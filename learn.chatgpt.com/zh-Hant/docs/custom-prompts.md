<!-- source: https://learn.chatgpt.com/zh-Hant/docs/custom-prompts -->

自訂提示詞已棄用。請使用 [技能](/zh-Hant/codex/build-skills) 建立可重複使用的
  指示，供 Codex 明確或隱含叫用。

自訂提示詞（已棄用）可將 Markdown 檔案轉換為可重複使用的提示詞，並讓您在 Codex CLI 和 Codex IDE 擴充功能中都能以斜線指令叫用。

自訂提示詞需要明確叫用，且存放在本機 Codex 主目錄中（例如 `~/.codex`），因此不會透過您的程式碼庫共用。若要共用提示詞（或讓 Codex 隱含叫用），請 [使用技能](/zh-Hant/codex/build-skills)。

1. 建立提示詞目錄：

   ```bash
   mkdir -p ~/.codex/prompts

2. 建立 `~/.codex/prompts/draftpr.md`，並在其中加入可重複使用的指引：

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. 重新啟動 Codex，讓它載入新的提示詞（請重新啟動 CLI 工作階段；若正在使用 IDE 擴充功能，也請重新載入該擴充功能）。

預期結果：在斜線指令選單中輸入 `/prompts:draftpr` 後，系統會顯示您的自訂指令及前置中繼資料中的說明，並提示檔案與 PR 標題均為選填。

## 新增中繼資料和引數

Codex 會在下次工作階段啟動時讀取提示詞中繼資料並解析預留位置。

- **說明：** 會顯示在彈出式視窗的指令名稱下方。請在 YAML 前置中繼資料中以 `description:` 設定。
- **引數提示：** 使用 `argument-hint: KEY=<value>` 說明預期的參數。
- **位置型預留位置：** `$1` 至 `$9` 會展開為您在指令後輸入、以空格分隔的對應引數。`$ARGUMENTS` 則包含所有這些引數。
- **具名預留位置：** 使用 `$FILE` 或 `$TICKET_ID` 這類大寫名稱，並以 `KEY=value` 的格式提供值。請為含有空格的值加上引號（例如 `FOCUS="loading state"`）。
- **常值美元符號：** 寫入 `$$`，即可在展開後的提示詞中輸出一個 `$`。

編輯提示詞檔案後，請重新啟動 Codex 或開啟新對話，以載入更新內容。Codex 會忽略提示詞目錄中的非 Markdown 檔案。

## 叫用與管理自訂指令

1. 在 Codex（CLI 或 IDE 擴充功能）中輸入 `/` 以開啟斜線指令選單。
2. 輸入 `prompts:` 或提示詞名稱，例如 `/prompts:draftpr`。
3. 提供必要的引數：

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. 按下 Enter 以傳送展開後的指示（不需要其中任一引數時，可省略該引數）。

預期結果：Codex 會展開 `draftpr.md` 的內容，將預留位置替換為您提供的引數，然後以訊息形式傳送結果。

若要管理提示詞，請編輯或刪除 `~/.codex/prompts/` 下的檔案。Codex 只會掃描該資料夾最上層的 Markdown 檔案，因此每個自訂提示詞都應直接放在 `~/.codex/prompts/` 下，而非子目錄中。
