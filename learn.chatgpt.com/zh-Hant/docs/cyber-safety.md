<!-- source: https://learn.chatgpt.com/zh-Hant/docs/cyber-safety -->

OpenAI Daybreak 可協助獲核准的使用者執行經授權的防禦性網路安全工作。Daybreak Blue 提供旗艦模型的存取權，並減少經授權的防禦性工作流程遭拒的情況。Daybreak Red 則提供需另行核准的存取權，讓使用者能運用專精於網路安全的模型，進行更進階的安全性研究。

使用獲核准的模型時，請搭配受控環境，明確界定獲核准的系統與動作範圍，採用最小權限，並在執行敏感動作前進行自動審查。請僅以獲核准的身分，透過獲核准的工作區或 API 組織與專案，以及獲核准的產品介面使用該模型。

## 選擇合適的模型

執行大多數經授權的防禦性工作時，請先使用 **GPT-Daybreak-Blue** 。此模型可讓您運用進階能力，而且在處理下列防禦性安全工作流程時，較少發生要求遭拒的情況：

- 漏洞發掘與分級處理。
- 程式碼安全審查與威脅建模。
- 偵測工程與事件應變。
- 受控環境中的惡意軟體分析。
- 修復與修補程式驗證。

**GPT-Daybreak-Red** 是專精於網路安全的模型，供另行核准且獲明確授權的工作流程使用，例如以受控方式重現漏洞、確認概念驗證或漏洞利用是否有效、進行滲透測試與紅隊演練，以及分析複雜系統。此模型並非例行安全性工作的預設選擇；您不會自動取得存取權，而且並非所有產品介面都能使用此模型。

若缺乏明確授權，這些進階工作流程可能看似惡意活動。請僅將獲核准的模型與產品介面用於您所擁有或已獲明確授權評估的系統，並維持適當的人工監督。

例如：

- **GPT-Daybreak-Blue：** 請在不存取外部系統的情況下，審查獲核准的實驗室程式碼庫是否存在身分驗證弱點，依據證據與影響排定發現事項的優先順序，並提出修補程式建議。
- **GPT-Daybreak-Red：** 請在獲核准的實驗室及測試時段內，重現已記錄的身分驗證缺陷，確認最精簡的概念驗證是否有效，並在存取憑證、建立常駐機制或變更正式環境之前停止。

## Trusted Access for Cyber

請透過 [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber) 申請 **Daybreak 存取權** 。存取權取決於是否已針對您的特定身分或服務、ChatGPT 工作區或 API 組織與專案、獲授權的方案與模型，以及允許的產品介面完成核准與佈建。

- 個人可透過 [Trusted Access 個人申請表](https://chatgpt.com/cyber) 申請存取權。
- 組織可提交 [企業 Trusted Access 申請表](https://openai.com/form/enterprise-trusted-access-for-cyber/)，並與其 OpenAI 代表協調。

提交申請或完成身分驗證，並不保證會獲得核准。

  提出申請、完成身分驗證，或獲准使用 Daybreak Blue，
都不會讓您取得 Daybreak Red 或 GPT-Daybreak-Red 的存取權。
這項專用方案必須另行取得核准並完成佈建。

若使用企業存取權，請僅將獲核准的工作區、API 組織或專案用於您所屬組織內部經授權的工作。不得將此存取權延伸至外部使用者、第三方客戶、對外提供的服務、下游產品功能，或獲核准工作範圍以外的系統。若不清楚哪些身分、工作區、API 組織、專案、模型或介面已獲核准，請停止操作並向您的 OpenAI 代表確認。

Trusted Access 不會自動提供 [零資料保留](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring)。開始前，請確認針對該特定 API 組織與適用端點另行核准的各項保留控制措施。

## 誤判

即使是正當的網路安全活動或與網路安全無關的活動，仍可能觸發防護機制。若防護機制封鎖、重新路由或限制某項要求，請檢查可取得的用戶端通知與要求紀錄。請查閱 [常見問題與疑難排解](https://help.openai.com/en/articles/20001259)，瞭解需要收集的詳細資料及後續步驟。若可使用 `/feedback`，請透過此功能回報疑似 Codex 誤判。針對 API 存取限制與申訴，請遵循 [API 網路安全檢查指南](/api/docs/guides/safety-checks/cybersecurity#appeals)。

所有使用者仍須遵守 [使用政策](https://openai.com/policies/usage-policies/) 和 [使用條款](https://openai.com/policies/row-terms-of-use/)。

## 設定您的安全性工作流程

Trusted Access 控管對獲核准模型的存取，但不會設定您的環境、強制執行針對獲核准系統與動作所設的限制，也不會審查擬執行的動作。

- [使用建議組態](/zh-Hant/codex/cyber-safety/recommended-configuration)，以隔離環境、設定最小權限、清楚界定範圍，並為敏感動作設置防護措施。
