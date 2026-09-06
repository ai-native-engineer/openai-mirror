<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/groups-and-provisioning -->

群組可用來組織 ChatGPT 工作區中的人員，並可獲指派自訂角色。群組成員資格不能取代席位分配，也不會自行授予工作區功能權限、凌駕本機執行階段政策，或提供 Platform API 或已連線系統的存取權。

如需完整的控制模型，請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

## 比較成員資格來源

請使用群組管理有共同存取需求的人員，例如試行計畫參與者、工作區操作人員，或需要使用相同受支援功能的成員。

### 為共同存取需求建立群組

工作區擁有者與管理員可以建立及管理群組。若對象人數較少或僅需暫時使用，可建立手動管理的群組；若成員資格應以目錄為準，則可從身分識別提供者同步既有群組。

每個群組都有唯一作準的成員資格來源：

| 群組類型                | 成員資格來源                   | 適用情況                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| 手動管理          | ChatGPT 工作區管理    | 群組規模較小、僅供暫時使用，或未透過目錄同步管理             |
| 由身分識別提供者管理 | 您的身分識別提供者（透過 SCIM） | 成員資格應依循組織目錄與成員移除流程 |

手動管理的群組與由身分識別提供者管理的群組可以並存。對於同步群組，身分識別提供者是成員資格來源；後續的佈建更新可能覆寫工作區端的變更。SCIM 目前的運作方式、支援的屬性及設定步驟，應以說明中心的資訊為準。

## 瞭解存取界線

群組成員資格本身不會授予工作區功能權限。

### 將群組連結至適當的權限

工作區擁有者可以將自訂角色指派給群組，或在支援此功能的情況下直接
指派給成員。請檢查所有適用的角色：只要任何角色明確將某項權限設為 **關閉** ，
就會拒絕授予該權限，即使其他角色授予該權限也一樣。成員的席位類型
與產品使用資格仍然適用。

SCIM 會佈建工作區成員資格與群組指派，但不會授予 GitHub、Google Drive、Slack 或其他已連線系統中的權限，也不會取代本機執行階段要求或 Platform API 的組織存取權。

工作區 RBAC 和本機執行階段要求屬於兩套獨立的控制系統。
群組可能同時與兩者相關，但請勿根據工作區群組順序，推斷受管理要求的比對
或優先順序規則。請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)，瞭解文件記載的
設定傳遞與本機優先順序規則。

## 依照現行設定程序操作

工作區管理的詳細資訊可能會變更。如需目前的 UI 操作步驟、可用性與限制，請參考以下來源：

- [管理成員、席位類型、角色與存取權](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [管理群組](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [SCIM 整合常見問題](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [管理工作區設定](https://help.openai.com/en/articles/8411955)

### 確認成員加入、異動與離開時的存取狀態

- **新加入的成員：** 確認成員已接受所有待處理的工作區邀請，並
  獲得預期的席位、群組成員資格、權限與
  受支援的功能。
- **異動的成員：** 更新作準的成員資格來源，並確認成員
  在所有適用角色下的實際生效權限。
- **離開的成員：** 透過身分識別提供者移除由 SCIM 管理的成員的存取權，
  並確認該成員已無法存取工作區。
  如果只從工作區移除該成員，
  後續同步可能會恢復其存取權。

## 相關文件

- [使用者生命週期管理](/zh-Hant/codex/enterprise/user-lifecycle)
- [身分驗證](/zh-Hant/codex/auth)
- [角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
- [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)
- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
