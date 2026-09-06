<!-- source: https://learn.chatgpt.com/zh-Hant/docs/build-plugins -->

若要建置或提交外掛程式，請參閱
[developers.openai.com 上的完整建置文件](/plugins)。

<div className="not-prose my-6">
  
    建置並提交外掛程式
  
</div>

本頁提供簡要介紹。外掛程式是可安裝的套件，
可包含技能、MCP 伺服器，或同時包含兩者。MCP 伺服器也可傳回
選用的使用者介面。

ChatGPT 和 Codex 共用同一個通用外掛程式目錄。公開外掛程式只需發布一次，
即可在兩項產品支援的介面中找到同一個上架項目。
開發期間，請先透過本機市集測試套件，
再將其提交至通用目錄。

若要透過 GitHub 在工作區中散布外掛程式，請參閱
[外掛程式管理](/zh-Hant/codex/enterprise/plugin-management)。

若仍在反覆調整一項個人工作流程，請先從技能著手。
若要分享該工作流程、封裝相關技能、連線至外部服務，
或將穩定的能力提供給團隊，請建置外掛程式。

## 使用 `@plugin-creator` 建立外掛程式

最快的設定方式是使用 ChatGPT Work 模式內建的 `@plugin-creator` 技能，
或在 Codex 中使用 `$plugin-creator`。

  
    
  

說明預期成果、要納入的技能或 MCP 伺服器，以及是否需要
在本機市集新增項目以供測試。例如：

```text
@plugin-creator Create a plugin named meeting-follow-up.
Include a skill that turns meeting notes into decisions, owners, and next steps.
Add it to a personal marketplace so I can test it locally.

此技能會建立必要的 `.codex-plugin/plugin.json` 資訊清單、
整理外掛程式資料夾，並可將外掛程式新增至本機市集。

  
    
  

完成後：

1. 審查 `.codex-plugin/plugin.json`。
2. 檢查 `skills/` 中的每項隨附技能。
3. 重新整理 ChatGPT 或 Codex，然後從對應的本機市集來源
安裝外掛程式。
4. 在新對話中，以具代表性的要求測試外掛程式。

如果外掛程式包含 MCP 伺服器，請先建置並測試該伺服器，然後
將已註冊的連線資訊提供給 `@plugin-creator`。請依照完整的
[MCP 伺服器工作流程](https://developers.openai.com/plugins/build/mcp-server)
處理工具、身分驗證、部署和測試。

## 手動建立僅包含技能的外掛程式

最精簡的外掛程式包含一份資訊清單和至少一項技能：

```text
meeting-follow-up/
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── meeting-follow-up/
        └── SKILL.md

建立 `.codex-plugin/plugin.json`：

```json
{
  "name": "meeting-follow-up",
  "version": "1.0.0",
  "description": "Turn meeting notes into decisions and next steps",
  "skills": "./skills/"
}

接著新增 `skills/meeting-follow-up/SKILL.md`：

```md
---
name: meeting-follow-up
description: Extract decisions, owners, and next steps from meeting notes.
---

Review the meeting notes. Return:

1. Decisions
2. Action items with owners
3. Open questions

外掛程式名稱應保持穩定，並採用 kebab case 格式。技能說明應足夠具體，
讓 ChatGPT 和 Codex 能判斷工作流程的適用時機。

使用 `@plugin-creator` 將資料夾新增至本機市集，然後安裝並
測試外掛程式，再與他人分享。

## 繼續參閱建置文件

如需完整的建置文件，請參閱
[外掛程式文件](https://developers.openai.com/plugins/)。內容涵蓋：

- [外掛程式架構](https://developers.openai.com/plugins/concepts/plugins)
- [建置技能](https://developers.openai.com/plugins/build/skills)
- [建置 MCP 伺服器](https://developers.openai.com/plugins/build/mcp-server)
- [新增選用的使用者介面](https://developers.openai.com/plugins/build/chatgpt-ui)
- [封裝外掛程式](https://developers.openai.com/plugins/build/plugins)
- [測試外掛程式](https://developers.openai.com/plugins/deploy/connect-chatgpt)
- [提交與發布](https://developers.openai.com/plugins/deploy/submission)

若要瀏覽、安裝、啟用或移除外掛程式，請參閱[使用
外掛程式](/zh-Hant/codex/plugins)。
