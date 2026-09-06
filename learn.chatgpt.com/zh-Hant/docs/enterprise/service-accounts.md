<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/service-accounts -->

服務帳戶讓您無須依賴員工帳戶，就能在整個組織中執行無介面的 Codex 工作流程，並擴大運作規模。每個持續整合 (CI) 執行器、排程工作或共用整合都會擁有專屬的 ChatGPT 工作區身分，並具備與人員帳戶相同的群組、角色、存取控制及可稽核性。

只有工作區擁有者和管理員能建立服務帳戶。他們可以授權其他人員或群組管理帳戶、設定外掛程式，或建立存取權杖。

服務帳戶僅適用於隨用隨付方案。

服務帳戶代表工作區中的非人員身分。[個人存取權杖](/zh-Hant/codex/enterprise/access-tokens)則代表建立該權杖的工作區成員。API 平台的專案服務帳戶和 API 金鑰使用獨立的專案存取權限與計費機制。

## 建立及設定服務帳戶

本互動式導覽以 GitHub 為例，說明如何建立帳戶、設定外掛程式、建立權杖，以及指派群組和角色。

1. 在工作區設定中開啟「[服務帳戶](https://chatgpt.com/admin/service-accounts)」。
2. 選取加號（**+**）按鈕，並輸入具描述性的名稱，例如 `release-automation`。
3. 選取「 **建立**」。

## 連接外掛程式

請為服務帳戶本身設定外掛程式。服務帳戶不會繼承建立者的外掛程式或已連接的應用程式。

1. 開啟帳戶的「 **外掛程式** 」區段，然後選取「 **新增外掛程式**」。
2. 選擇外掛程式，並確認其顯示為已設定或已啟用。

「 **設定** 」和「 **管理者** 」角色可以設定外掛程式；「 **使用者** 」角色則不行。

## 建立存取權杖

在服務帳戶的詳細資料頁面建立 Token。此 Token 代表服務帳戶，而非建立 Token 的人員。

1. 開啟帳戶，在「 **存取權杖**」中選取「 **建立 Token** 」。
2. 為 Token 命名，確認「 **Codex** 」範圍，並選擇到期時間。
3. 選取「 **建立** 」，並將 Token 儲存在機密管理工具中。

完整的 Token 只會顯示一次。可選擇的到期時間由工作區政策決定。

## 指派角色與群組

服務帳戶可以和真人工作區成員一樣，獲指派工作區角色並加入群組。請直接指派其存取權；服務帳戶不會繼承建立者的權限。

如要讓人員或群組管理帳戶，請選取「 **分享**」，再選取「 **新增人員或群組**」，並指派角色：

| 共用帳戶角色 | 設定帳戶及其外掛程式 | 建立服務帳戶存取權杖 |
| ------------------- | ------------------------------------- | ------------------------------------ |
| **使用者**            | 否                                    | 是                                  |
| **設定**       | 是                                   | 否                                   |
| **管理者**         | 是                                   | 是                                  |

這些角色適用於管理帳戶的人員，與指派給服務帳戶的工作區角色和群組分開管理。

「**設定** 」和「 **管理者** 」角色可以啟用或停用帳戶。只有工作區擁有者和管理員可以建立、刪除或分享帳戶。操作人員登入自己的 ChatGPT 帳戶來管理共用帳戶。

如要進一步瞭解工作區權限，請參閱[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

## 不登入即可執行 Codex

服務帳戶存取權杖需要 Codex CLI `0.142.0` 或更新版本。設定 `CODEX_ACCESS_TOKEN` 後，即可在不開啟瀏覽器的情況下執行 Codex：

```bash

codex exec --json "Inspect this repository and summarize its current state."

在 CI 中，請透過機密管理工具或執行器機密提供 Token。

如要在受信任的電腦上儲存登入資訊，請透過標準輸入傳遞 Token：

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "Summarize the changes in the current branch."

這會將憑證儲存在本機。在共用或臨時執行器上，請使用 `CODEX_ACCESS_TOKEN`，不要儲存登入資訊。

## 透過 SCIM 佈建服務帳戶

如果工作區支援透過跨網域身分識別管理系統（SCIM）通訊協定佈建服務帳戶，請在身分識別提供者中將 `userType` 設為 `ServiceAccount`：

```json
{
  "schemas": ["urn:ietf:params:scim:schemas:core:2.0:User"],
  "userName": "svc-codex-release@company.example",
  "displayName": "Codex release automation",
  "active": true,
  "userType": "ServiceAccount"
}

將該身分指派給工作區及必要群組，然後進行同步。身分識別提供者負責管理帳戶名稱、群組成員資格和生命週期。由 SCIM 管理的帳戶無法在 ChatGPT 中重新命名或刪除。請參閱[群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)。

## 使用 Admin API 管理服務帳戶

如果你的工作區具有存取權，請使用 ChatGPT Admin API 金鑰管理帳戶、權杖和共用設定。讀取操作需要 `chatgpt.enterprise.service_account.read`；變更操作需要 `chatgpt.enterprise.service_account.write`。服務帳戶權杖無法用於 Admin API 請求的身分驗證。

請查閱 [Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)，瞭解可用的操作和目前的請求路徑。

### 帳戶

| 操作                    | 方法   | 功能說明                               |
| ---------------------------- | -------- | ------------------------------------------ |
| 列出帳戶                | `GET`    | 傳回工作區的服務帳戶         |
| 建立帳戶            | `POST`   | 建立具有指定名稱的服務帳戶            |
| 取得帳戶               | `GET`    | 傳回一個服務帳戶                |
| 啟用或停用帳戶 | `PATCH`  | 更新帳戶的 `enabled` 值      |
| 刪除帳戶            | `DELETE` | 移除帳戶並撤銷其權杖 |

使用 `POST /v1/manage/workspaces/{workspace_id}/service-accounts` 建立帳戶。更新帳戶時僅會變更 `enabled`。

### 權杖

| 操作      | 方法   | 功能說明                         |
| -------------- | -------- | ------------------------------------ |
| 列出權杖    | `GET`    | 傳回帳戶的權杖中繼資料 |
| 建立權杖 | `POST`   | 建立具有限定範圍的存取權杖        |
| 撤銷權杖 | `DELETE` | 永久撤銷一個權杖        |

例如，建立一個 30 天後到期的 Codex 權杖：

```json
{
  "name": "production-release-runner",
  "ttl": 2592000,
  "scopes": ["chatgpt.workspace.feature.allow-codex-local-access.access"]
}

`ttl` 是權杖的有效期間，以秒為單位。若設定有效期限，有效期間必須短於一年，並符合工作區的到期政策。只有建立權杖時，才會傳回完整的 `access_token`。

Admin API 也可列出、新增、更新及移除共用帳戶的存取權限。其角色值為 `manager`、`configurer` 和 `user`；`configurer` 在 ChatGPT 中顯示為「 **設定** 」。

## 保護並管理服務帳戶

- 僅授予工作流程所需的角色、群組、外掛程式和連線。
- 將權杖存放於機密管理工具中，並使用可信任的執行器。
- 請勿將認證資訊寫入記錄檔、對話訊息或原始碼版本控制系統。
- 設定明確的到期時間，並定期審查帳戶的存取權限和活動。
- 若要輪替權杖，請先建立替代權杖、更新工作流程並驗證存取權限，最後在工作區中或透過 Admin API 撤銷舊權杖。
- 立即撤銷已外洩的權杖，並調查帳戶近期的活動。
- 在工作區中或透過 Admin API 停用或刪除未使用的帳戶。這兩種操作都會撤銷所有有效權杖。已停用的帳戶可重新啟用並使用新的權杖；刪除後則無法復原。

執行作業會歸屬於服務帳戶。可用的工作區分析和稽核紀錄也能查明誰建立了權杖或變更了帳戶設定。請在 [Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)中確認涵蓋哪些事件。

## 相關文件

- [身分驗證](/zh-Hant/codex/auth)
- [個人存取權杖](/zh-Hant/codex/enterprise/access-tokens)
- [角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
- [群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
- [治理](/zh-Hant/codex/enterprise/governance)
- [Compliance API 與稽核事件](/zh-Hant/codex/enterprise/compliance-api)
- [非互動模式](/zh-Hant/codex/non-interactive-mode)
