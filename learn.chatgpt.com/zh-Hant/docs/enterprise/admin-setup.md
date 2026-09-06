<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/admin-setup -->

使用本指南規劃 ChatGPT Enterprise 導入作業，涵蓋以下管理範疇：

- 工作區存取權。
- ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中，適用範圍內功能的本機執行階段政策。
- Codex 雲端。
- Platform API 存取權。
- 外掛程式和連接器存取權。
- 已連線系統中的權限。

首次導入時，請依序完成各步驟；若只需調整單一範疇，請參閱對應的連結頁面。

在工作區設定中， **本機 Codex 與 Work** 透過
 **允許成員在本機使用 Codex 和 Work**，統一管理 Codex 和 Work 的本機存取權。部分工作區
則提供獨立的 **本機 Codex** 和 **本機 Work** 區段。在
這種配置下， **允許成員在本機使用 Codex** 控制 Codex，而 **在本機使用
Work** 控制 Work。啟用其中一項不會同時啟用另一項。
這些標籤代表工作區權限，而非獨立的產品或用戶端。
Token 權限和憑證有效期限限制會依工作區而異，顯示在 **存取
Token** 區段或本機存取區段中。
受管理的設定是獨立的政策層，可針對這些用戶端中適用範圍內的功能，
限制其支援的執行階段行為。當行為或可用性有所差異時，
本指南會明確指出個別介面。

請先參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)中的標準對照關係。
如需目前的 ChatGPT 工作區操作程序，請參閱說明中心指引；如需本機與託管執行階段的行為說明，
請參閱連結的開發人員文件。

<a id="enterprise-grade-security-and-privacy"></a>

如需企業安全性、隱私權和執行階段保護的相關資訊，請參閱
[智慧體核准與安全性](/zh-Hant/codex/agent-approvals-security)和
[Codex 安全性白皮書](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)。

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## 步驟 1：指定負責人並選擇導入方案

為導入作業的每個部分指定負責人：

- **工作區存取權：** 成員資格、席次、角色，以及
  支援的工作區功能。
- **本機執行階段政策：** 支援的本機用戶端所需的核准、權限設定檔、檔案系統與
  網路存取權，以及其他要求。
- **Codex 雲端：** 託管環境、程式碼庫連線，以及
  雲端執行階段政策。
- **已連線系統：** 供應商端的應用程式安裝、帳戶和
  權限。
- **報告與合規：** 分析功能存取權、稽核資料匯出，以及
  下游資料處理。

判斷各類使用者需要的是 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中適用範圍內的本機功能、Codex 雲端，還是其中幾項的組合。當工作流程使用 API 金鑰進行身分驗證時，請將 Platform API 存取權視為獨立的組織與專案管理範疇。

## 步驟 2：設定工作區存取權與身分

透過 ChatGPT 工作區的成員資格、席次、群組和支援的 RBAC 權限，讓目標使用者使用支援的工作區功能。請依據目前的工作區指引，驗證本機用戶端和 Codex 雲端的存取權，不要假設同一角色可控制所有介面。內建管理角色應僅授予負責管理工作區的人員。

工作區控制項和標籤會隨時間變更。請參閱以下來源，瞭解目前的操作程序：

- [管理成員、席次類型、角色和存取權](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [設定角色型存取控制](https://help.openai.com/en/articles/11750701-rbac)
- [管理工作區設定](https://help.openai.com/en/articles/8411955)
- [群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
- [使用者生命週期管理](/zh-Hant/codex/enterprise/user-lifecycle)
- [身分驗證](/zh-Hant/codex/auth)

擴大導入範圍之前，請先以具代表性的成員測試登入和功能存取。工作區存取權不會授予已連線服務中的程式碼庫、檔案或動作存取權。

## 步驟 3：設定本機執行階段要求

當使用者在 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中
啟動支援的本機執行作業時，本機要求會限制執行階段行為。請透過支援的雲端、裝置或系統管道
派送 `requirements.toml`。請將
此政策與 ChatGPT 工作區角色和群組分開管理。

請為支援的本機用戶端使用權限設定檔，不要以舊版沙盒模式限制為基礎建立新的部署。例如：

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

若要在所有支援的瀏覽器和桌面功能介面中停用「電腦」功能，請限制這項體驗所涉及的每個公開功能設定鍵：

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

如需權威的設定鍵清單、派送行為、優先順序及更多
範例，請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)和
[`requirements.toml` 參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)。

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## 步驟 4：標準化程式碼庫組態

使用程式碼庫範圍的組態，共用專案預設值、規則和
技能，無須為每位使用者重複設定。請依照功能文件指定的位置，將組態置於
`.codex` 或 `.agents`，並納入版本控制：

| 類型          | 來源                                           | 用途                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| 組態 | [基本設定](/zh-Hant/codex/config-file/config-basic) | 為支援的本機用戶端設定程式碼庫預設值        |
| 規則         | [規則](/zh-Hant/codex/agent-configuration/rules)        | 控制在沙盒外執行時需要核准的指令 |
| 技能        | [建立技能](/zh-Hant/codex/build-skills)              | 讓支援的用戶端可使用程式碼庫工作流程   |

程式碼庫組態可提供預設值和可重複使用的工作流程，但無法授予工作區、模型、Platform API 或已連線系統的存取權。

## 步驟 5：設定 Codex 雲端

Codex 雲端使用託管環境和已連線的來源程式碼庫。請規劃各項管理範疇：

1. 透過支援的工作區控制項，授予目標使用者 Codex 雲端存取權。
2. 安裝並設定支援的來源系統整合。
3. 在來源系統中，將各類使用者的程式碼庫存取權限制在其所需的程式碼庫。
4. 為這些程式碼庫設定雲端環境、機密資料和網際網路存取權。
5. 設定選用的託管工作流程，例如程式碼審查。
6. 以具代表性且具備預定工作區和程式碼庫權限的使用者進行測試。

Codex 雲端會遵循已連線來源系統所提供的
程式碼庫權限和保護措施。工作區存取權不會繞過這些控制項。請參閱
[雲端環境](/zh-Hant/codex/environments/cloud-environment)、
[GitHub 整合](/zh-Hant/codex/third-party/github)和
[智慧體核准與安全性](/zh-Hant/codex/agent-approvals-security)，瞭解 Codex 雲端的
設定和執行階段指引。

## 步驟 6：設定外掛程式和連線功能

請分別審查外掛程式安裝、隨附技能、連接器支援的功能、連接器動作和來源系統授權，並各自做出決定。停用連接器支援的功能，不一定會解除安裝該外掛程式或其隨附技能。

將外掛程式或技能納入導入範圍之前：

1. 確認其來源、負責人、目標使用者和審查日期。
2. 審查隨附的技能、連接器、MCP 伺服器、掛勾，以及各項功能所需的資料與動作。
3. 使用非敏感資料，並以其所需的最低存取權限進行測試。
4. 記錄重新審查與除役作業的負責人。

外掛程式可在網頁版、桌面版和行動版 ChatGPT 的對話與 Work 中使用，也可在 ChatGPT 桌面版應用程式中的 Codex 使用，或透過 Codex CLI 的外掛程式瀏覽器使用。
外掛程式不適用於 IDE 擴充功能。
ChatGPT 與 Codex 共用一個通用的公開外掛程式目錄；工作區控制措施決定成員可存取其中哪些外掛程式。

如需瞭解完整管理模式，請參閱[外掛程式控制措施](/zh-Hant/codex/enterprise/apps-and-connectors)與
[技能控制措施](/zh-Hant/codex/enterprise/skills)。

## 步驟 7：設定治理與可觀測性

根據要解答的問題，選擇適合的報告介面：

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- 使用[工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)進行
  互動式 ChatGPT 工作區分析與 Codex 分析。
- 使用[分析 API](/zh-Hant/codex/enterprise/analytics-api)，透過 Codex 分析 API
  以程式化方式產生彙總報告。
- 使用 [Compliance API](/zh-Hant/codex/enterprise/compliance-api) 取得稽核與
  調查紀錄。
- 若 Codex 活動依所用方案會消耗符合資格的 ChatGPT 工作區
  點數，請使用
  [ChatGPT 使用量限制與支出控制措施](/zh-Hant/codex/enterprise/usage-limits)。

請參閱需經身分驗證才能存取的 API 參考文件，瞭解目前的存取要求、結構描述、欄位、資料保留方式與請求行為。請勿根據本指南中複製的介面規格建置整合。

保護整合邊界：

- 將 API 金鑰和其他整合憑證儲存在組織的機密管理系統中。
- 僅允許經核准的對象存取下游系統與保留的資料。
- 根據匯出的 Compliance API 紀錄的敏感度與組織的保留政策保護這些紀錄，並依現行介面規格測試收集與刪除工作流程。

## 步驟 8：驗證並維護導入作業

使用具代表性的身分，驗證每個適用的邊界：

- ChatGPT 工作區成員資格、席位，以及支援的角色權限。
- ChatGPT 桌面版應用程式、Codex CLI 與 IDE 擴充功能所涵蓋的本機功能，包括登入與實際生效的執行階段要求。
- Codex 雲端的存取權、環境組態與程式碼庫權限。
- 使用 API 金鑰的工作流程所需的平台 API 組織與專案存取權。
- 外掛程式安裝、隨附技能、連接器存取權，以及支援的動作。
- 已連線系統的授權與資料存取權。
- 負責相關作業的管理員對分析與合規功能的存取權。

記錄每項控制措施的負責人與現行程序的資訊來源。這份紀錄可讓管理員在 UI 或政策變更時更新程序，而無須變更管理模式。

完成初次導入後，請審查存取權、已連線的功能、點數使用情況、支援回饋，以及團隊實際使用的工作流程。當這些項目出現變化時，請調整導入範圍與管理員指引。
