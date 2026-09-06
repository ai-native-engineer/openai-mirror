<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/workspace-model-availability -->

使用者可使用的模型取決於產品介面與登入方式。ChatGPT 工作區的模型設定不會自動套用至 ChatGPT 桌面版應用程式中的 Codex、Codex CLI、IDE 擴充功能、Codex 雲端或 OpenAI API。

如需瞭解完整的管理架構，請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

## 釐清模型存取權的適用範圍

| 產品或身分驗證邊界                                                         | 模型存取權取決於                                                                                  | 最新資訊來源                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作區                                                                          | 工作區方案、成員存取權、工作區設定，以及支援的角色權限                 | [ChatGPT Enterprise 與 ChatGPT Edu 的模型與限制](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| ChatGPT 桌面版應用程式中的 Codex、Codex CLI 與 IDE 擴充功能（使用 ChatGPT 登入）        | 該用戶端支援的模型，以及已登入的 ChatGPT 身分所具備的存取權    | [Codex 模型](/zh-Hant/codex/models)與最新的工作區指南                                                                  |
| Codex 雲端                                                                                | 託管式 Codex 工作流程支援的模型，以及已登入的 ChatGPT 身分所具備的存取權 | [Codex 模型](/zh-Hant/codex/models)與 [Codex 雲端](/zh-Hant/codex/cloud)                                                                 |
| ChatGPT 桌面版應用程式中的 Codex、Codex CLI 與 IDE 擴充功能（使用 API 金鑰進行身分驗證） | 與該金鑰相關聯的 OpenAI API 組織及專案                                       | [身分驗證](/zh-Hant/codex/auth)與 [OpenAI API 平台](https://platform.openai.com/docs/overview)                        |

請查閱使用者實際使用的產品介面所對應的最新資訊來源。請勿複製模型目錄，也不要假設 ChatGPT 模型選擇器的設定對 ChatGPT 桌面版應用程式中的 Codex、Codex CLI、IDE 擴充功能、Codex 雲端及 API 平台具有相同效果。

## 為員工設定明確的初始使用體驗

邀請試行群組前，請先檢視工作區的[模型設定](https://help.openai.com/en/articles/8411955)。
工作區擁有者和管理員可以
分別為對話，以及 Work 和 Codex 設定初始預設值。
在支援的情況下，可為對話、Work 和本機 Codex 介面選擇初始模型、推理程度、速度，
以及建立新對話時的行為。

請將這些選項視為預設值，而非權限。可用的模型仍取決於成員的席位、角色、工作區或 API 身分、強制執行的工作區要求，以及其實際使用的產品介面。初始預設值不會授予不可用模型的存取權，也無法覆寫這些要求。Codex 雲端不支援變更預設模型。

快速模式是否可用，取決於工作區、產品介面，
以及 [`requirements.toml`](/zh-Hant/codex/config-file/config-reference#requirementstoml) 中
任何強制套用的 `features.fast_mode` 設定。
此設定可將受管理的本機 Codex 用戶端的快速模式固定為開啟或關閉；
它不是初始預設值，也無法覆寫工作區或產品的可用性限制。

## 企業環境中的 GPT-6 Astra

在初期推出階段，組織必須先取得 Daybreak 存取權，
管理員才能啟用 Astra。推出後的前兩週，
ChatGPT Enterprise 預設關閉 Astra。符合資格的工作區管理員
可以為使用者或群組啟用 Astra，
供其在對話、Work 和 Codex 中使用。現有的產品使用資格要求仍然適用。請檢視
[工作區模型設定](https://help.openai.com/en/articles/8411955)，並
確認試行群組使用的每個用戶端是否皆可使用 Astra。

開放存取權與選擇初始模型是兩項不同的決定。
將 Astra 設為預設模型前，請確認適用的席位、角色及計費安排。
如需使用額度與計費說明，請參閱[定價](/zh-Hant/codex/pricing)；
如需瞭解因等待審查而暫停的任務，請參閱[安全監控](/zh-Hant/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)
的說明。

使用 API 金鑰登入時，Astra 存取權取決於與該金鑰相關聯的 API 組織及專案。在 ChatGPT 工作區中啟用 Astra 並不會授予 API 存取權。使用 API 金鑰搶先體驗 Astra 還需要設定用戶端；請向您的 OpenAI 客戶團隊索取設定說明。單憑選擇模型或變更本機組態，並不會獲得存取權。

## 準備因應 GPT-5.4 退役

2026 年 8 月 31 日，Codex 將停止向使用 ChatGPT 登入的使用者提供 GPT-5.4 與 GPT-5.4 mini。請在此之前更新受影響的工作區預設值、已儲存的模型設定、受管理的設定、自訂智慧體和排程任務：

- 將 `gpt-5.4` 替換為 `gpt-5.6-terra`（GPT-5.6 Terra）。
- 將 `gpt-5.4-mini` 替換為 `gpt-5.6-luna`（GPT-5.6 Luna）。

OpenAI API 以及使用您自己的 API 金鑰進行身分驗證的 Codex 不受影響。
請參閱 [Codex 模型](/zh-Hant/codex/models#deprecated-codex-models)和
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)，
瞭解遷移詳情。

## 區分模型存取權與執行階段權限

模型存取權決定已通過身分驗證的使用者能否在支援的介面上使用某個模型。本機權限設定檔與受管理的要求，則決定智慧體開始在本機執行後可以進行哪些操作，例如可以變更哪些檔案，或可以連線至哪些網路目的地。

權限設定檔無法授予模型存取權。模型存取權也不能放寬執行作業適用的沙盒限制、核准政策、網路控制或來源系統權限。

## 排解模型存取問題

如果使用者無法選取預期的模型：

- 確認產品介面及登入方式。
- 確認 ChatGPT 工作區，或 API 平台的組織及專案。
- 檢視該身分驗證邊界目前的存取控制。
- 檢查所選的本機用戶端或 Codex 雲端是否支援該模型。

## 最新資訊來源

- [ChatGPT Enterprise 與 ChatGPT Edu 的模型與限制](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [管理工作區設定](https://help.openai.com/en/articles/8411955)
- [角色型存取控制](https://help.openai.com/en/articles/11750701-rbac)
- [Codex 模型](/zh-Hant/codex/models)
- [各方案的 Codex 功能可用性](/zh-Hant/codex/pricing#feature-availability)
- [身分驗證](/zh-Hant/codex/auth)

## 相關文件

- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
- [角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
- [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)
