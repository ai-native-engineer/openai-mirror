<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/skills -->

技能是由指示和輔助資源組成、可重複使用的工作流程。
ChatGPT 工作區技能、本文涵蓋的本機功能所使用的檔案系統技能
（這些功能位於 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中），以及
封裝技能的外掛程式，各有獨立的生命週期與存取控制。

如需瞭解完整的管理模型，請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

<a id="distinguish-the-distribution-models"></a>

## 技能分發與管理

| 分發模式      | 用途                                                                                           | 管理界線                                                                       |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| ChatGPT 工作區技能 | 透過受支援的 ChatGPT 工作區功能，共用或安裝已核准的工作流程              | ChatGPT 工作區技能的權限與生命週期控管                                    |
| 本機檔案系統技能  | 從程式碼庫、使用者、管理員或隨附的系統位置載入已安裝的工作流程     | 檔案系統分發、本機用戶端組態與執行階段權限                  |
| 外掛程式                  | 將一項或多項技能與選用的連接器、MCP 伺服器、掛勾及呈現用中繼資料封裝在一起 | 外掛程式的可用性與安裝，以及每項內含功能各自的控管機制 |

ChatGPT 工作區技能分發、本機檔案系統技能安裝，以及
各介面專屬的外掛程式安裝，分別採用不同途徑。移轉技能時，不會
一併移轉 ChatGPT 工作區擁有權、共用設定、角色指派、外掛程式
安裝狀態或連接器授權。

外掛程式可在網頁版、桌面版和行動版 ChatGPT 的對話與 Work 中使用，
也可在 ChatGPT 桌面版應用程式的 Codex 中，以及透過 Codex CLI 外掛程式瀏覽器使用。
IDE 擴充功能不提供這些外掛程式。
上述受支援的介面會從 ChatGPT 與 Codex 共用的單一通用目錄
取得公開外掛程式。

## 控管歸屬

請參閱 [建置技能](/zh-Hant/codex/build-skills)，瞭解檔案系統位置與編寫方式；
[ChatGPT 中的技能](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
則說明目前的工作區操作程序；另請參閱 [建置外掛程式](https://developers.openai.com/plugins/build/plugins)，瞭解
外掛程式的封裝方式。

ChatGPT 工作區的控管機制不會安裝本機檔案系統技能或外掛程式。
檔案系統分發不會授予 ChatGPT 工作區擁有權，也不會指派角色。
外掛程式安裝不會授予連接器、MCP 伺服器或
已連線服務的存取權。設定每項功能時，請使用負責
該功能的控管介面。

## 相關文件

- [技能與外掛程式](/zh-Hant/codex/skills-and-plugins)
- [外掛程式](/zh-Hant/codex/plugins)
- [建置技能](/zh-Hant/codex/build-skills)
- [建置外掛程式](https://developers.openai.com/plugins/build/plugins)
- [管理員部署指南](/zh-Hant/codex/enterprise/admin-setup)
- [外掛程式控管](/zh-Hant/codex/enterprise/apps-and-connectors)
