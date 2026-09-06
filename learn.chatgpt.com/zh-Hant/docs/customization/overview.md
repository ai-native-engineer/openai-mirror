<!-- source: https://learn.chatgpt.com/zh-Hant/docs/customization/overview -->

透過自訂，你可以讓 Codex 採用與團隊相同的工作方式。

在 Codex 中，自訂功能由幾個相互配合的層面構成：

- **專案指引（`AGENTS.md`）**，用於提供持續適用的指示
- **[記憶](/zh-Hant/codex/customization/memories)**，用於保留先前工作所累積的實用上下文
- **技能**，提供可重用的工作流程和領域專業知識
- **[MCP](/zh-Hant/codex/extend/mcp)**，用於存取外部工具和共用系統
- **[子代理程式](/zh-Hant/codex/agent-configuration/subagents)**，用於將工作委派給專門的子代理程式

這些項目相輔相成，而非彼此競爭。`AGENTS.md` 用來塑造行為，記憶
會延續本機上下文，技能會封裝可重複執行的流程，而
[MCP](/zh-Hant/codex/extend/mcp) 則將 Codex 連接至本機工作區之外的系統。

## AGENTS 指引

`AGENTS.md` 為 Codex 提供長期適用的專案指引。這些指引會隨你的程式碼庫一同提供，並在智慧體開始工作前套用。檔案內容應保持精簡。

將它用於希望 Codex 每次都在程式碼庫中遵循的規則，例如：

- 建置與測試指令
- 審查要求
- 程式碼庫專屬慣例
- 目錄專屬指示

當智慧體對你的程式碼庫做出錯誤假設時，請在 `AGENTS.md` 中修正這些假設，並要求智慧體更新 `AGENTS.md`，讓這項修正持續有效。將此流程視為回饋循環。

**更新 `AGENTS.md`：** 一開始只加入真正重要的指示。將重複出現的審查回饋寫成規則，把指引放在最接近其適用位置的目錄中；當你修正某個問題時，也請智慧體更新 `AGENTS.md`，讓後續工作階段沿用這項修正。

### 何時更新 `AGENTS.md`

- **重複犯錯**：如果智慧體一再犯相同的錯誤，請新增規則。
- **讀取過多內容**：如果智慧體找到了正確的檔案，卻讀取過多文件，請加入路由指引（指定應優先處理哪些目錄或檔案）。
- **PR 回饋重複出現**：如果你多次留下相同的回饋，請將其寫成規則。
- **在 GitHub 中**：請在 Pull Request 留言中標記 `@codex` 並提出要求（例如 `@codex add this to AGENTS.md`），將這項更新委派給雲端對話處理。
- **將漂移檢查自動化**：使用 [排程任務](/zh-Hant/codex/automations) 定期執行檢查（例如每天一次），找出指引缺漏，並建議應在 `AGENTS.md` 中新增哪些內容。

將 `AGENTS.md` 與可強制執行這些規則的基礎架構搭配使用：pre-commit 掛勾、Linter 和型別檢查器會在你看到問題之前就將其找出，讓系統更善於防止同類錯誤再次發生。

Codex 可從多個位置載入指引：Codex 主目錄中的全域檔案（供你以開發人員身分使用），以及可由團隊提交的程式碼庫專屬檔案。檔案越接近工作目錄，優先順序就越高。
使用全域檔案來調整 Codex 與你溝通的方式（例如審查風格、詳略程度和預設值），並讓程式碼庫檔案聚焦於團隊和程式碼庫規則。

[透過 AGENTS.md 設定自訂指示](/zh-Hant/codex/agent-configuration/agents-md)

## 技能

技能為 Codex 提供可重用的能力，以執行可重複的工作流程。
技能通常最適合可重用的工作流程，因為它支援更豐富的指示、指令碼和參考資料，同時可跨任務重用。
技能會載入並可供智慧體查看（至少可查看其中繼資料），因此 Codex 能探索技能並自行選用。如此既能讓內容豐富的工作流程隨時可用，又不會從一開始就讓上下文過度膨脹。

使用技能資料夾在本機編寫工作流程並反覆調整。如果已有外掛程式
可支援該工作流程，請先安裝它，以重用經過驗證的設定。若要
在團隊間發布自己的工作流程，或將其與
連接器綑綁，請將它封裝成 [外掛程式](/zh-Hant/codex/build-plugins)。技能仍是用來
編寫工作流程的格式；外掛程式則是可安裝的散發形式。

技能通常包含一個 `SKILL.md` 檔案，以及選用的指令碼、參考資料和資產。

技能目錄可包含一個 `scripts/` 資料夾，內含 Codex 在工作流程中呼叫的 CLI 指令碼（例如填入種子資料或執行驗證）。當工作流程需要外部系統（議題追蹤器、設計工具、文件伺服器）時，請將技能與 [MCP](/zh-Hant/codex/extend/mcp) 搭配使用。

範例 `SKILL.md`：

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

技能可用於：

- 可重複執行的工作流程（發布步驟、審查例行作業、文件更新）
- 團隊專屬的專業知識
- 需要範例、參考資料或輔助指令碼的程序

技能可以是全域技能（位於你的使用者目錄中，供你以開發人員身分使用），也可以是程式碼庫專屬技能（存放在 `.agents/skills` 並提交至程式碼庫，供你的團隊使用）。當工作流程適用於該專案時，請將程式碼庫技能放在 `.agents/skills`；若希望技能可用於所有程式碼庫，則放在使用者目錄中。

| 層級  | 全域               | 程式碼庫                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | `AGENTS.md` 位於程式碼庫根目錄或巢狀目錄中 |
| 技能 | `~/.agents/skills`   | `.agents/skills` 位於程式碼庫中                       |

Codex 會對技能採用漸進式揭露：

- 一開始僅使用中繼資料（`name`、`description`）來探索技能
- 只有選定技能後，才會載入 `SKILL.md`
- 只有在需要時，才會讀取參考資料或執行指令碼

你可以明確呼叫技能；當任務符合技能描述時，Codex 也可以自行選用。清楚的技能描述可讓觸發更可靠。

[建立技能](/zh-Hant/codex/build-skills)

## MCP

MCP（模型上下文協定）是將 Codex 連接至外部工具和上下文提供者的標準方式。
它特別適合 Figma、Linear、GitHub 等遠端託管的系統，或團隊所依賴的內部知識服務。

當 Codex 需要本機程式碼庫之外的功能時，請使用 MCP，例如議題追蹤器、設計工具、瀏覽器或共用文件系統。

可以這樣理解：

- **主機**：Codex
- **用戶端**：Codex 內的 MCP 連線
- **伺服器**：外部工具或上下文提供者

MCP 伺服器可提供：

- **工具**（動作）
- **資源**（可讀取的資料）
- **提示詞**（可重複使用的提示詞範本）

這項區分有助於你釐清信任與能力的邊界。有些伺服器主要提供上下文，另一些則提供強大的操作能力。

實務上，MCP 與技能搭配使用時通常最能發揮效用：

- 技能會定義工作流程，並指定要使用的 MCP 工具

[模型上下文協定](/zh-Hant/codex/extend/mcp)

## 子代理程式

你可以建立擔任不同角色的智慧體，並透過提示詞指示它們以不同方式使用工具。例如，一個智慧體可能會執行特定的測試指令並套用特定組態，另一個則可透過 MCP 伺服器擷取正式環境紀錄以進行偵錯。每個子代理程式都會專注於自己的任務，並使用適合該任務的工具。

[子代理程式](/zh-Hant/codex/agent-configuration/subagents)

## 技能與 MCP 搭配使用

技能與 MCP 搭配使用，就能將這一切串聯起來：技能會定義可重複使用的工作流程，MCP 則將這些工作流程連接至外部工具和系統。
若技能依賴 MCP，請在 `agents/openai.yaml` 中宣告這項相依性，讓 Codex 能自動完成安裝與串接（請參閱 [建立技能](/zh-Hant/codex/build-skills)）。

## 下一步

請依下列順序建置：

1. [使用 AGENTS.md 設定自訂指示](/zh-Hant/codex/agent-configuration/agents-md)，讓 Codex 遵循你的程式碼庫慣例。加入提交前掛勾和程式碼檢查工具，以強制執行這些規則。
2. 若已有可重複使用的工作流程，請安裝 [外掛程式](/zh-Hant/codex/plugins)。否則，請建立 [技能](/zh-Hant/codex/build-skills)；若要分享該技能，請將其封裝為外掛程式。
3. 工作流程需要外部系統（Linear、GitHub、文件伺服器、設計工具）時，請使用 [MCP](/zh-Hant/codex/extend/mcp)。
4. 準備好委派會產生大量雜訊或需要專業處理的任務時，請將這些任務委派給 [子代理程式](/zh-Hant/codex/agent-configuration/subagents)。
