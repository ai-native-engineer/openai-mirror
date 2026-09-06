<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/apps-and-connectors -->

外掛程式將可重複使用的工作流程封裝在一起，可包含技能，
以及連接其他工具的應用程式。ChatGPT 和 Codex 在支援的介面上
共用同一個公開外掛程式目錄，而管理員則決定工作區可使用哪些外掛程式。
進一步瞭解[外掛程式](/zh-Hant/codex/plugins)、
[技能](/zh-Hant/codex/skills-and-plugins)及
[應用程式與連接器](https://help.openai.com/en/articles/11487775)。

成員只有在其角色可使用該外掛程式和應用程式，且擁有已連線服務的存取權時，才能使用由連接器支援的能力。

外掛程式可用於網頁版、桌面版及行動版 ChatGPT 的對話與 Work，也可用於 ChatGPT 桌面版應用程式中的 Codex，並可透過 Codex CLI 外掛程式瀏覽器使用。IDE 擴充功能不支援外掛程式。

如需瞭解這些控制措施如何與工作區角色及權限搭配運作，請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

## 瞭解能力的控制層級

外掛程式可能涉及下列控制層級：

| 層級                   | 控制內容                                                           | 管理位置                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 可用性            | 使用者是否可使用外掛程式套件                           | 支援的網頁版與桌面版介面使用[工作區設定](https://chatgpt.com/admin/settings)；CLI 使用 CLI 外掛程式瀏覽器 |
| 隨附技能         | 已安裝的外掛程式提供哪些可重複使用的指示                 | 外掛程式套件與[技能控制措施](/zh-Hant/codex/enterprise/skills)                                                               |
| App 存取權              | 使用者是否可使用由連接器支援的能力                          | [工作區應用程式](https://chatgpt.com/admin/ca)與[權限與角色](https://chatgpt.com/admin/settings)                    |
| 動作與權限 | 使用者可執行哪些動作，以及 ChatGPT 何時會在使用連接器前詢問使用者 | [工作區應用程式](https://chatgpt.com/admin/ca)中連接器的「動作控制」與「App 權限」                            |
| 服務授權   | 經身分驗證的身分可存取哪些外部資料及執行哪些動作        | 已連線的服務及其身分識別提供者                                                                                 |
| 執行階段權限     | 智慧體取得資料或工具後可執行的操作                        | 目前所用介面的執行階段、沙盒與核准控制措施                                                              |

運用這些層級，分兩個步驟導入：先開放適當的外掛程式，再設定各工作流程所需的能力與權限。

## 步驟 1：開放使用外掛程式

在支援的網頁版與桌面版介面中，工作區外掛程式控制措施會決定
哪些角色可使用或安裝外掛程式。Codex CLI 則透過自己的
外掛程式瀏覽器進行安裝。請參閱
[建置外掛程式](https://developers.openai.com/plugins/build/plugins)，瞭解
封裝與發佈方式。

若要從 GitHub 匯入工作區外掛程式並保持最新狀態，請參閱
[外掛程式管理](/zh-Hant/codex/enterprise/plugin-management)。

### 匯出公開目錄以供審查

符合資格的 ChatGPT Enterprise 工作區擁有者和管理員，可以下載一份列出其工作區可用公開外掛程式的 CSV 檔案。變更外掛程式的可用性前，請使用匯出資料審查外掛程式、應用程式和技能的中繼資料。

1. 開啟[管理 \> 外掛程式](https://chatgpt.com/admin/plugins)。
2. 選取 **公開**。
3. 選取頁首的下載圖示（**匯出 CSV**）。

下載檔案的檔名為 `public-plugins-security-review.csv`，內容包括：

- 外掛程式中繼資料：`Plugin Name`、`Plugin Description`、`Date Added (UTC)`、
`OpenAI Verified`、`Developer Name` 和 `Version`。
- App 中繼資料：`App Name(s)` 和 `App Description(s)`。
- 對話技能中繼資料：`Skill Name(s)` 和 `Skill Description(s)`。

若外掛程式包含多個應用程式或技能，對應的值會以分號分隔。匯出內容使用的公開目錄快照最多可能是 48 小時前的版本，僅包含目前工作區可查看的公開外掛程式，不包含為該工作區建立的外掛程式。FedRAMP 工作區無法使用此匯出功能。

## 步驟 2：管理能力

  在 ChatGPT 中開放使用應用程式或外掛程式，並不會授予已連線服務中的檔案與紀錄存取權，或動作執行權限。進行疑難排解或擴大存取權前，請先檢查成員的工作區角色與經核准的動作設定，再確認經身分驗證的帳戶或共用連線在已連線服務中具備預期權限。

ChatGPT 與 Codex 的外掛程式可包含連接器，用於在外部系統中搜尋、擷取、同步資料或執行動作。外掛程式的可用性與授予各連接器的存取權及動作權限，屬於彼此獨立的控制措施。

透過
[工作區應用程式](https://chatgpt.com/admin/ca)與
[權限與角色](https://chatgpt.com/admin/settings)管理由連接器支援的能力。可用的控制措施
讓管理員能夠：

- 啟用應用程式或連接器，並依工作區角色指派存取權。
- 針對支援「動作控制」的連接器，允許唯讀動作或一組經核准的自訂動作，並設定工作區如何處理新增的動作。
- 設定「App 權限」，決定 ChatGPT 何時會在使用應用程式前詢問使用者。
- 將存取限制在各已連線服務及已通過身分驗證的使用者所授予的範圍與權限內。

如需最新的可用性資訊與操作程序，請參閱
[應用程式中的管理員控制措施、安全性與合規性](https://help.openai.com/en/articles/11509118)。

<a id="choose-a-starting-set-of-apps"></a>

## 精選初期導入的外掛程式

從能滿足明確業務需求的外掛程式著手。針對每個外掛程式，決定要開放所有人使用、僅限特定角色或試行群組使用，或要求進一步審查。

針對每項已連線服務，記錄業務負責人、允許存取的資料、經核准的讀取或寫入動作、身分驗證方式，以及負責支援或移除事宜的聯絡人。

啟用寫入動作或發佈新的連線能力前，請確認其角色適用範圍，並使用在已連線服務中僅具有預定權限的帳戶進行測試。

若要大規模導入，請從團隊每天使用的類別著手，例如電子郵件、
行事曆以及檔案或文件系統。透過
[外掛程式目錄](https://chatgpt.com/apps)，確認外掛程式在支援的 ChatGPT 與 Codex 介面上目前的可用性
及能力。

不論初期選擇哪些外掛程式，都先從讀取動作開始。啟用寫入動作前，請確認外掛程式負責人、審查連接器的授權範圍與服務權限、確認資料存取權，並記錄外部影響及復原方式。

## 瞭解資料流與安全性

當 ChatGPT 使用外掛程式隨附的應用程式或連接器時，會向已連線服務傳送要求，並依照經身分驗證的使用者在該服務中的權限，傳回允許存取的資料或動作結果。

ChatGPT 以兩種方式處理已連線應用程式的資料：

- **未同步：** ChatGPT 會暫時處理來自對話與深度研究的資料，
  不會為其建立索引。
- **已同步：** ChatGPT 會預先為選定的已連線內容建立索引。您可以在
  應用程式的外掛程式頁面查看其是否支援同步。

模式設定會改變 ChatGPT 為已連線內容建立索引的方式，但不會取代一般對話保留控制措施。使用應用程式的 ChatGPT 對話仍可透過 Compliance API 取得。

OpenAI 的應用程式指南說明了傳輸中與靜態資料加密、個別使用者授權、角色與動作控制，以及針對使用應用程式的對話所設的網路存取限制。指南也說明，Business、Enterprise 和 Edu 客戶透過應用程式存取的資訊不會用於訓練模型。當請求到達已連線的服務時，該服務的權限範圍、資料保留、資料駐留及其他政策也同樣適用。

請參閱[應用程式安全性與合規性](https://help.openai.com/en/articles/11509118)
及[具備同步功能的應用程式](https://help.openai.com/en/articles/10847137)，瞭解最新的
資料處理詳情。如需瞭解 ChatGPT 桌面應用程式、
Codex CLI 或 IDE 擴充功能中的 MCP 伺服器本機設定，請參閱
[Codex MCP 組態](/zh-Hant/codex/extend/mcp)。

## 使用最新流程與參考資料

- [應用程式的管理員控制項、安全性與合規性](https://help.openai.com/en/articles/11509118)
- [ChatGPT 中的應用程式](https://help.openai.com/en/articles/11487775)
- [具備同步功能的應用程式](https://help.openai.com/en/articles/10847137)
- [管理工作區設定](https://help.openai.com/en/articles/8411955)
- [外掛程式](/zh-Hant/codex/plugins)
- [技能與外掛程式](/zh-Hant/codex/skills-and-plugins)
- [建置外掛程式](https://developers.openai.com/plugins/build/plugins)
- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
