<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/update-documentation -->

## 簡介

在原始碼變更時同步更新文件，而不是幾週後才處理，是讓文件保持最新的最簡單方式。Codex 可以檢查已變更的程式碼、測試、版本資訊、相關議題和 Pull Request 上下文，再草擬符合現有結構且範圍明確的文件更新。

這套工作流程適用於開發人員文件、README 更新、更新日誌草稿、遷移說明、操作手冊，以及其他任何需要持續反映頻繁變動行為的內容。

## 使用方式

1. 先從需要寫入文件的變更著手。

   提供分支、Pull Request、提交、議題或檔案。如果文件會公開發布，請明確指出不得納入尚未發布的產品藍圖、客戶的私人資訊和僅供內部使用的上下文。

2. 請 Codex 找出受影響的文件。

   草擬前，請 Codex 搜尋現有文件中的功能名稱、設定鍵、指令、範例和相關詞彙。

3. 將文件更新限縮在足以達成目的的最小範圍。

   Codex 應保留目前的頁面結構、術語、交叉連結和 frontmatter。如果精準更新附註、範例或章節便已足夠，就應避免大範圍改寫。

4. 驗證變更。

   請 Codex 執行適合該程式碼庫的格式與文件檢查，再摘要說明每項面向使用者的陳述有哪些佐證。

## 要提供給 Codex 的內容

| 來源                               | 為何有幫助                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| 已變更的程式碼和測試               | 可讓 Codex 分析實際行為，進而草擬範圍明確的文件更新。 |
| 公開的版本資訊或產品文件 | 協助 Codex 與公開資訊中的術語、可用範圍和功能狀態保持一致。    |
| Pull Request 或議題的上下文        | 說明變更原因，以及哪些使用者可見的行為需要關注。   |
| 本機文件檢查                    | 讓 Codex 在文件發布前有一套明確的完成標準。   |

加入公開版本資訊等更多上下文，可讓 Codex 避免納入私人內容或尚未公開的更新。

## 建立可重複執行的工作流程

若要建立適用於整個程式碼庫的慣例，請在 [AGENTS.md](/zh-Hant/codex/agent-configuration/agents-md) 中加入文件相關規範。例如：

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

如果流程還有更多步驟，請將它轉換成 [技能](/zh-Hant/codex/build-skills)，讓日後的 Codex 任務都能遵循相同的來源查核、草擬與驗證循環。若要進一步瞭解這種模式，請參閱 [將工作流程儲存為技能](/zh-Hant/codex/use-cases/reusable-codex-skills)。

你也可以 [從目前的對話為此工作流程排程任務](/zh-Hant/codex/automations#schedule-a-task-inside-a-chat)。例如，請 Codex 每週擷取近期的 GitHub Pull Request，讓文件保持最新：
