<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/roles-and-workspace-permissions -->

不同設定分別管理貴組織 ChatGPT 使用體驗的不同面向。授予某人在一個領域的存取權，不代表該人會自動獲得另一個領域的存取權。請透過本頁瞭解六項控制邊界如何相互配合，再參閱連結中的指南，瞭解目前的設定步驟。

在工作區設定中， **Codex 與 Work 本機** 區段將 Codex 和 Work 的本機
存取權整合至 **允許成員在本機使用 Codex 和 Work**。其他工作區則將
 **Codex 本機** 和 **Work 本機** 分為獨立區段。在這種
配置下， **允許成員在本機使用 Codex** 會授予 Codex 本機存取權，而
**在本機使用 Work** 會授予 Work 本機存取權。啟用其中一項不會
授予另一項的存取權。這些標籤代表工作區權限，而非獨立的
產品或用戶端。Token 權限與憑證有效期限限制
會顯示在 **存取權杖** 區段或本機存取區段中，具體位置
依工作區而定。受管理的設定則是獨立的控制層，用來限制
這些用戶端所涵蓋功能中受支援的執行階段行為。功能
與實際生效的要求可能因用戶端和版本而異。

## 瞭解控制邊界

| 邊界          | 控制的項目                                                                                                                                                                                      | 不控制的項目                                                                          | 目前參考來源                                                                                                                                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作區 | 成員資格、席位、內建管理角色，以及依角色授予的受支援工作區功能存取權                                                                                               | 本機智慧體權限、API 平台組織存取權，或已連線服務中的權限 | [ChatGPT 工作區存取權](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)與 [RBAC](https://help.openai.com/en/articles/11750701-rbac) |
| 本機用戶端     | ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中所涵蓋功能的執行階段行為，包括核准、檔案系統與網路存取、權限設定檔，以及允許使用的整合 | ChatGPT 席位、功能或模型使用資格，或外部資料存取權                         | [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)與[權限](/zh-Hant/codex/permissions)                                                                                                   |
| Codex 雲端       | 使用託管 Codex 工作流程的資格，以及提供給使用者的雲端環境                                                                                                       | 本機執行階段政策，或來源系統授予的程式碼庫權限                    | [雲端環境](/zh-Hant/codex/environments/cloud-environment)                                                                                                                                              |
| API 平台      | 透過 API 驗證身分的工作所涉及的組織與專案成員資格、API 金鑰、模型存取權、用量及帳務                                                                                            | ChatGPT 工作區成員資格、本機用戶端存取權，或 Codex 雲端存取權                         | [API 平台](https://platform.openai.com/docs/overview)                                                                                                                                         |
| 外掛程式           | 外掛程式的可用性與安裝、隨附的技能、連接器存取權，以及受支援的連接器動作                                                                                               | 已連線服務中的授權，或更廣泛的本機與雲端執行階段權限            | [外掛程式控制措施](/zh-Hant/codex/enterprise/apps-and-connectors)                                                                                                                                                 |
| 已連線系統 | 已通過身分驗證的帳戶可在來源系統中存取哪些程式碼庫、檔案與訊息，以及執行哪些動作                                                                                            | ChatGPT 工作區、外掛程式、Codex 雲端或 API 平台的使用資格                              | 已連線服務的管理與存取控制                                                                                                                                               |

每個請求都必須通過所有適用的控制邊界。例如，工作區存取權可以讓使用者使用外掛程式，但已連線服務仍會決定已登入帳戶可以讀取哪些資料。本機權限設定檔可以限制受支援本機用戶端中的執行作業，但無法授予工作區功能或模型的使用資格。

## 指派工作區存取權

ChatGPT 工作區管理會將產品存取權與管理權限分開。

### 瞭解席位、管理員角色與自訂角色之間的差異

席位決定成員可以存取哪些產品介面。依工作區方案而定，可用的席位類型可能包括 ChatGPT 席位和 Codex 席位。

內建工作區角色決定管理權限。 **擁有者** 角色
管理整個工作區的設定； **管理員** 角色管理受支援的營運作業
與群組； **成員** 角色沒有管理權限；
**分析檢視者** 角色則可以存取工作區分析。

自訂角色定義成員可以使用哪些受支援的功能，但不會取代席位或方案的資格要求、授予已連線系統中的權限，或變更本機執行階段要求。

<div class="not-prose my-4 aspect-video overflow-hidden rounded-md bg-gray-900">
  <iframe
    src="https://player.vimeo.com/video/1215495812"
    title="角色型存取控制操作導覽"
    loading="lazy"
    allow="autoplay; fullscreen; picture-in-picture"
    allowFullScreen
    referrerPolicy="strict-origin-when-cross-origin"
    class="h-full w-full border-0"
  ></iframe>
</div>

### 先設定工作區預設值，再依特定需求建立自訂角色

只有工作區擁有者可以設定角色型存取控制 (RBAC) 並建立自訂角色。工作區設定會為適用的權限建立基準。工作區擁有者可以透過群組指派自訂角色；在支援的情況下，也可以直接指派給個別成員。群組可以手動管理或透過 SCIM 同步，而成員可以獲得多個自訂角色。

對於適用的權限， **預設** 會沿用工作區設定， **開啟**
會授予存取權，而 **關閉** 則明確拒絕存取。只要任何適用角色明確設為 **關閉** ，
即使另一個角色授予存取權，仍會阻擋存取。
各項功能可用的權限狀態可能有所不同。

### 審查 Work 本機與 Work 雲端權限

當您的工作區提供 **Work 本機** 和 **Work 雲端**時，請同時檢查
工作區預設值及各個適用的自訂角色。Work 僅供
符合資格的工作區使用，可用的控制措施可能因方案、工作區
設定及推出進度而有所不同。角色無法擴大成員席位
所允許的存取範圍。

**Work 雲端** 控管受支援的 ChatGPT Work 雲端任務。當這些
控制措施彼此獨立時，只有 **Work 本機** 而沒有 **Work 雲端** 權限，成員可以
在 ChatGPT 桌面版應用程式中進行本機作業，但無法啟動雲端任務。
Codex 的本機存取權由 **允許成員在本機使用 Codex** 控制，該設定位於 **Codex
本機**區段。變更 **在本機使用 Work** 不會改變 Codex 本機存取權，也不會
取代本機執行階段要求。

部分工作區則會顯示合併的 **Codex 與 Work 本機** 區段。
在這種配置下， **允許成員在本機使用 Codex 和 Work** 會同時控制這兩項
產品的存取權。

如需瞭解目前的使用資格與設定，請參閱
[ChatGPT Work 與 Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)。

由於可用的席位、角色及權限會隨產品與方案更新而改變，請前往說明中心查看目前的權限清單與設定程序：

- [管理成員、席位類型、角色與存取權](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [設定角色型存取控制](https://help.openai.com/en/articles/11750701-rbac)
- [管理群組](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)

### 控管電腦使用紀錄存取權

[電腦使用紀錄](/zh-Hant/codex/customization/computer-history)在 Business 與企業工作區中
預設為關閉。工作區擁有者
明確授予存取權之前，成員無法啟用此功能。企業工作區擁有者可以
依角色授予存取權：

1. 開啟[**工作區設定 \> 權限與角色**](https://chatgpt.com/admin/settings)。
2. 找到 **電腦使用紀錄** ，並選擇應具有
   存取權的工作區角色。
3. 為該角色開啟 **啟用電腦使用紀錄** 。

這項權限只允許獲指派的成員開啟電腦使用紀錄，不會代替成員開啟這項功能。每位成員都必須透過 macOS 上的 ChatGPT 桌面版應用程式自行選擇啟用，並可選擇要納入哪些應用程式和網站的使用紀錄。未取得必要工作區權限的成員，無法透過本機設定啟用這項功能。

## 套用本機執行階段政策

本機執行階段政策會限制 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中所涵蓋的功能。由雲端管理的要求還取決於受支援的 ChatGPT 登入方式與方案資格。權限設定檔與受管理的要求可限制指令、檔案系統存取、網路存取、核准及其他本機執行階段行為。這些設定不會變更使用者的席位、工作區角色、模型使用資格，或外部系統中的權限。

本機政策允許時，使用者可以選擇內建或自訂的權限設定檔。
管理員可以透過
受支援的受管理設定管道發布預設值與要求。請參閱[權限](/zh-Hant/codex/permissions)，
瞭解設定檔的運作方式；另請參閱[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)，
瞭解要求、傳遞方式與優先順序。

## 相關文件

- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
- [使用者生命週期管理](/zh-Hant/codex/enterprise/user-lifecycle)
- [工作區模型可用性](/zh-Hant/codex/enterprise/workspace-model-availability)
- [存取權杖](/zh-Hant/codex/enterprise/access-tokens)
- [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)
- [身分驗證](/zh-Hant/codex/auth)
