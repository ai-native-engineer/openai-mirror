<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/triage-backlog -->

使用 `$codex-security:triage-finding` 審查現有安全性發現項目，
並以目前的程式碼庫為依據。此工作流程會執行唯讀的靜態
分析：Codex 將每個發現項目視為尚未證實的主張，並檢查程式碼庫中的
證據，而不執行程式碼。

請在 Codex 專案中執行此工作流程；該專案的範圍必須限定於您要
評估的程式碼庫。Codex 必須能夠讀取程式碼庫的原始碼。Jira 和 Linear
連接器可提供發現項目資料，而 GitHub 發現項目則需要經過驗證的
GitHub REST 存取權。這兩者皆不能取代對原始碼的存取權。

實際運作時，Codex 會先查看所引用的程式碼或版本資訊，然後
追蹤主張中受攻擊者控制的來源、相關安全性控制措施、
危險匯點和可到達路徑。它也會檢查產品功能面與信任
邊界、搜尋反證，並記錄證據缺口。接著，Codex 會為
每個發現項目傳回一項判定，並為需要採取行動或進一步
審查的發現項目排序。

這與 `$codex-security:validation` 不同；後者可以建置或執行程式碼，
建立針對性測試或概念驗證，或透過實際介面進行測試，
以重現發現項目所述問題或證明其不成立。使用分級處理來分類現有
待辦清單並排定優先順序。如果執行階段證據可能釐清某個發現項目，
但靜態證據仍不足以判定，請使用驗證。

  待辦清單的分級處理會從現有發現項目開始。若要在程式碼庫中搜尋新的
  漏洞，請[執行安全性掃描](/zh-Hant/codex/security/plugin/scans)。分級處理
  不會修改程式碼庫，也不會實作修正。

## 選擇要進行分級處理的發現項目

您可以提供來自以下來源的單一發現項目或一組發現項目：

| 來源                   | 提供內容                                                                                                                                                                                                                                                                                                                                                                                                                                        | 必要條件                                                                                                                                                                                     |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 貼上或儲存於本機的發現項目 | SARIF 結果、CVE 或 GHSA、安全性公告、掃描器工單、漏洞懸賞報告、Codex Security 發現項目產出物，或以一般語言描述的漏洞主張。                                                                                                                                                                                                                                                                                          | 無須連接器。                                                                                                                                                                           |
| Jira 或 Linear           | 安全性或漏洞議題的確切 URL 或識別碼、Jira JQL，或 Linear 團隊、專案或搜尋詞組。Codex 會在分級處理前擷取所選議題的內容。                                                                                                                                                                                                                                                                            | [透過 Atlassian Rovo 使用 Jira](codex://plugins/plugin_connector_692de805e3ec8191834719067174a384)，或使用 [Linear](codex://plugins/plugin_asdk_app_69a089a326dc8191b32a3f2553f5be2c) 並具備讀取權限。 |
| GitHub                   | 一個程式碼庫，以及一種發現項目來源：程式碼掃描、`Dependabot` 漏洞與惡意軟體、安全性公告與私人漏洞報告，或所有來源。若未指定程式碼庫，Codex 會在可用時使用附加至目前 Codex 專案的 GitHub 程式碼庫。預設 GitHub 來源不包含 GitHub 議題；若要對其進行分級處理，請提供特定議題，或明確要求納入 GitHub 議題。 | 經過驗證的 GitHub REST 存取權，例如 `gh auth token`、`GH_TOKEN` 或 `GITHUB_TOKEN`，且須具備讀取所選程式碼庫和發現項目類型的權限。                                      |

Codex 會依輸入順序為每個提供的發現項目保留一項結果，讓每個
原始發現項目都可追溯。它不會合併或捨棄看起來
重複的發現項目。

## 執行唯讀分級處理

對於貼上的發現項目或本機產出物，可傳送類似以下內容的提示詞：

```text
Use $codex-security:triage-finding to triage these existing security findings against this repository:

[Paste the findings or provide the artifact path.]

對於 Jira 或 Linear 議題，請指定議題集合，並讓來源系統
維持唯讀：

```text
Use $codex-security:triage-finding to import and triage the security findings from [Jira or Linear issue URLs, identifiers, or query] against this repository.
Do not change the source issues.

對於 GitHub 發現項目，請指定程式碼庫和來源：

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from [owner/repository] against this repository.

若要使用附加至目前 Codex 專案的 GitHub 程式碼庫，請只指定
發現項目來源：

```text
Use $codex-security:triage-finding to import and triage [code scanning, Dependabot vulnerabilities and malware, security advisories and private vulnerability reports, or all] from GitHub against this repository. Use the GitHub repository attached to the current Codex project.

工作流程會依以下順序進行：

1. 收集並整理發現項目

   Codex 會擷取任何要求的議題或 GitHub 內容，保留來源
識別碼與參照資訊，並為每項輸入建立一個分級處理項目。它會先建立
完整的項目清單，再指派判定。

2. 確認程式碼庫上下文

   Codex 會在可用時確認目前的程式碼庫與修訂版本。它會讀取
`SECURITY.md`（如有），讓支援的版本、可信任的輸入、產品
   邊界和超出範圍的功能面都能作為評估依據。

3. 檢查靜態證據

   針對每個發現項目，Codex 會追蹤主張中受攻擊者控制的來源、
相關安全性控制措施、有漏洞的匯點、可到達路徑，以及適用的
安全性邊界。它會記錄支持該主張的證據、反駁該
主張的證據，以及證據缺口。

4. 指派判定與排名

   Codex 會為每個發現項目指派判定與可信度，並將
`confirmed` 與 `needs_review` 發現項目分別放入不同佇列，依可利用性排序。

## 審查結果

| 判定          | 含義                                                                                                                                                 |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `confirmed`      | 程式碼庫證據顯示，漏洞路徑在所述先決條件下可到達，且會跨越適用的安全性邊界。                     |
| `not_actionable` | 程式碼庫證據足以排除該主張，例如顯示未受影響的版本、無法到達的路徑、有效的防護措施，或未隨產品提供的功能面。                 |
| `needs_review`   | 程式碼庫證據不足以做出判定，因為必要資訊缺漏或語意不明，或必須視執行階段、環境或政策而定。 |

  可利用性排名使用從 `1` 開始的正整數，並在
  每個判定佇列中各自獨立計算。如此可將修復工作的優先順序與
  尚未解決的審查工作分開。排名 `1` 代表該結果集中可利用性最高的 `confirmed` 發現項目，
  或優先順序最高的 `needs_review` 發現項目。此排名
  不是掃描器的嚴重程度分數，而 `not_actionable` 發現項目不會獲得排名。

請針對每個發現項目審查以下內容：

- 判定與排名的依據
- 支持該主張的證據與反證
- 待解答問題與剩餘的證據缺口
- 受影響的位置與元件
- 產品功能面與來源信任層級
- 建議的後續步驟
- 交接至 [`$codex-security:fix-finding`](/zh-Hant/codex/security/plugin/fix-findings)
  （當發現項目的判定為 `confirmed` 時）

當每個提供的發現項目都有一項結果、Codex 保留
其來源識別碼，且所有不確定之處都已明確列出時，即完成分級處理。Jira、Linear 和其他
待辦清單記錄會維持不變，除非您要求 Codex 在
審查分級處理結果後回寫。

## 後續步驟

- `confirmed`：由人員確認該發現項目應予修復後，請使用
[`$codex-security:fix-finding`](/zh-Hant/codex/security/plugin/fix-findings) 進行修正並
  驗證。分級處理會準備可直接作為提示詞使用的交接內容，但不會
  自動叫用該技能。
- `needs_review`：若執行程式碼能補足證據缺口，請使用
`$codex-security:validation` 執行有限範圍的動態驗證。請傳入
  分級處理結果中的發現項目主張、受影響位置、先決條件、靜態證據與
  證據缺口：

  ```text
  Use $codex-security:validation to dynamically validate finding [triage item ID or source ID] from the backlog triage result. Use the strongest realistic, bounded method, record exactly what was tested, and preserve any remaining proof gaps.

  驗證與分級處理不同，可能會建置或執行程式碼、建立針對性測試或
  概念驗證，或透過實際介面進行測試。請先審查擬執行的指令，
  再予以核准，並持續套用[Codex 核准與安全性
  政策](/zh-Hant/codex/agent-approvals-security)。

- `needs_review`：若發現項目取決於產品政策或部署
  上下文，請先回答列出的待解答問題，再變更程式碼。
- `not_actionable`：請將證據與分級處理記錄保存在一起。Codex 不會
  自動關閉或更新來源工單。
- 若要尋找所提供待辦清單之外的漏洞，請[執行安全性
  掃描](/zh-Hant/codex/security/plugin/scans)。
