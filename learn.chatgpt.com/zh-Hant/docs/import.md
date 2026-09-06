<!-- source: https://learn.chatgpt.com/zh-Hant/docs/import -->

透過匯入流程，將其他智慧體的指示、設定、技能、外掛程式、專案
和近期工作匯入 ChatGPT 桌面版應用程式或 Codex CLI。
桌面版應用程式可從 **Claude Code**、<strong>Claude Cowork</strong>
或 **Cursor** 匯入；Codex CLI 則可從 **Claude Code** 或 **Cursor** 匯入。

桌面版應用程式會直接匯入受支援的項目，並協助你為
需要授權的已匯入外掛程式或連線完成設定。你也可以透過
自動更新，讓匯入的工作保持同步。

匯入作業不會變更或刪除你現有的智慧體設定。

  

## 開始匯入

### 在桌面版應用程式中匯入

1. 在 ChatGPT 桌面版應用程式中，開啟 **設定 \> 匯入**。如果 **匯入** 尚未
   顯示為設定區段，請開啟 **一般** ，然後尋找 **匯入其他
   智慧體設定**。
2. 選取 **匯入**。
3. 選擇要從中匯入的智慧體，然後選取 **繼續**。
4. 在 **選取要匯入的項目** 畫面中，選擇要匯入的內容，然後選取 **繼續**。
5. 匯入完成後，開啟已匯入的專案或對話，即可繼續工作。

### 讓匯入的工作保持同步

在 ChatGPT 桌面版應用程式中，開啟 **設定 \> 匯入** ，然後啟用自動
更新，讓匯入的工作與原始智慧體保持同步。你也可以
在同一個設定區段中檢視匯入紀錄。

### 在 Codex CLI 中匯入

1. 啟動本機 Codex CLI 工作階段，然後輸入 `/import`。
2. 選擇 **Claude Code** 或 **Cursor**。
3. 選取要匯入的受支援設定、專案檔案，
以及近期對話。
4. 審查匯入的組態，然後在 Codex 中繼續工作。

Codex CLI 最多可匯入過去 30 天內的 50 個對話。`/import` 指令
無法在任務執行期間、遠端工作階段中，或連線
至本機 app-server 常駐程式時使用。請參閱 [CLI 斜線
指令](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import)。

  

## 匯入的運作方式

匯入流程會同時檢查你的使用者層級設定和現有專案。
使用者層級設定來自你電腦上的檔案；專案層級設定則
來自所選程式碼庫和資料夾中的檔案。

匯入時，ChatGPT 會：

1. 偵測受支援的設定和近期工作。
2. 匯入你選取的項目。
3. 保留你現有的智慧體設定，不做任何變更。
4. 檢查已匯入的外掛程式或連線是否仍需設定。
5. 需要完成設定時，顯示狀態卡片。

## ChatGPT 可匯入的內容

| 匯入項目                     | 目的地                                             |
| --------------------------------- | ------------------------------------------------------- |
| 指示檔案                 | [`AGENTS.md`](/zh-Hant/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/zh-Hant/codex/config-file/config-basic)        |
| 技能                            | [技能](/zh-Hant/codex/build-skills)                           |
| 外掛程式                           | 外掛程式                                                 |
| 現有專案資料夾          | 使用相同資料夾的專案                         |
| 來自 Claude Code 的專案記憶 | [記憶](/zh-Hant/codex/customization/memories)               |
| 過去 30 天內的對話       | ChatGPT 對話                                           |
| MCP 伺服器組態          | [Codex MCP 組態](/zh-Hant/codex/extend/mcp)            |
| 掛勾                             | [Codex 掛勾](/zh-Hant/codex/hooks)                             |
| 斜線指令                    | [技能](/zh-Hant/codex/build-skills)                           |
| 子代理程式                         | [Codex 子代理程式](/zh-Hant/codex/agent-configuration/subagents) |

## 匯入後完成設定

匯入完成後，應用程式會在左下角顯示狀態卡片。
如果已匯入的外掛程式或連線仍需設定，卡片會特別標示。

當應用程式標示某個項目需要處理時，請選取 **完成** ，並依照
提示完成設定。

## 匯入後應審查的項目

使用匯入的設定前，請先審查，尤其注意以下項目：

- 已匯入技能和智慧體中的工具限制或權限。
- 使用自訂身分驗證、標頭、環境變數或傳輸方式的 MCP 伺服器
設定。你可能需要重新登入。
- 匯入後行為可能有所不同的掛勾。
- 需要手動完成後續作業的外掛程式、市集或其他設定。
- 依賴引數、Shell
插值或檔案路徑預留位置的提示詞範本或指令式提示詞。

## 匯入後

匯入完成後，請開啟其中一個已匯入的專案，並繼續
進行作業。請參閱 [使用 ChatGPT](/zh-Hant/codex/use-chatgpt)，瞭解如何開始
下一項任務。
