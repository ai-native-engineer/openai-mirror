<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/governance -->

Codex 活動的治理涵蓋互動式分析、程式化報告、
相關的 ChatGPT 使用量控制項，以及稽核記錄。請依問題
選擇合適的介面；分析資料與合規資料
各有不同用途。

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| 若要                                          | 請先使用                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| 瞭解 ChatGPT 整體的採用情況                      | [工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)              |
| 以互動方式檢視 Codex 的採用與活動情況        | [Codex 分析](#analytics-dashboard)                                   |
| 將彙總的 Codex 報告載入另一個系統     | [Analytics API](/zh-Hant/codex/enterprise/analytics-api)                          |
| 匯出記錄以供稽核或調查               | [Compliance API](/zh-Hant/codex/enterprise/compliance-api)                        |
| 檢視依方案而定的 ChatGPT 工作區點數控制項 | [ChatGPT 使用量限制與支出控制項](/zh-Hant/codex/enterprise/usage-limits) |

## 開啟管理介面

- 開啟 [工作區分析](https://chatgpt.com/admin/usage)，
  即可使用互動式工作區報告功能。[工作區分析指南](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)
  說明目前的角色與檢視畫面。
- 需要依排程透過程式取得報告時，
  請開啟 [Codex Analytics API 參考文件](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)。
- 請開啟 [Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)
  與 [合規平台指南](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)，
  以進行稽核與調查整合。

例如，使用工作區分析快速檢查採用情況，
使用 Analytics API 將彙總的 Codex 報告載入商業智慧系統，
並使用 Compliance API 將可供稽核的記錄
傳送至 SIEM 或電子蒐證工作流程。

## 分析儀表板

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT 提供涵蓋整個工作區的分析，用於掌握整體採用情況與參與度。
Codex 分析則著重於 Codex 活動。兩者都是互動式報告介面，
而非原始稽核記錄。

請參閱 [工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)，比較這兩種分析體驗，
並找到目前由各自負責團隊維護的資料來源。你也可以
直接開啟 [工作區分析](https://chatgpt.com/admin/usage)。請勿
根據儀表板標籤或下載報告中的欄位制定長期報告規格；
這些內容可能會隨產品演進而變更。

## 相關的 ChatGPT 使用量控制項

ChatGPT 工作區使用量控制項與分析功能彼此獨立，也不會
設定功能存取資格。視方案而定，符合條件的 Codex 活動
可能會消耗 ChatGPT 工作區點數；額度用盡時，可能會暫停存取
符合條件的功能。這些控制項不會設定通用的 Codex 限制，也不會管理
Platform API 計費。

請參閱 [ChatGPT 使用量限制與支出控制項](/zh-Hant/codex/enterprise/usage-limits)，
瞭解長期適用的範圍界定，並查閱說明中心目前的參考資料。

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

使用 Analytics API，以程式化方式取得彙總的 Codex 報告。
此 API 適合用於資料倉儲、商業智慧系統，
以及不應依賴互動式儀表板的內部報告。

存取需求、路由、結構描述、
欄位、報告期間與分頁機制，均以 API 參考文件為準。請參閱
[Analytics API](/zh-Hant/codex/enterprise/analytics-api)，查看整合範圍的概念說明，
並取得正式參考文件連結。

## Compliance API

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

安全性、法務與治理工作流程如需可供稽核的記錄，
請使用 Compliance API。它不是用來分析採用情況或生產力的儀表板。

事件涵蓋範圍、結構描述、權限、
篩選條件、保留期間與請求行為，均以 API 參考文件為準。請參閱
[Compliance API](/zh-Hant/codex/enterprise/compliance-api)，查看整合範圍的概念說明，
並取得正式參考文件連結。

<a id="recommended-pattern"></a>

若要安排這些介面的導入順序並進行驗證，請參閱
[管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)。

## 相關文件

- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)
- [Analytics API](/zh-Hant/codex/enterprise/analytics-api)
- [Compliance API](/zh-Hant/codex/enterprise/compliance-api)
