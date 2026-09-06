<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/workspace-analytics -->

使用 ChatGPT 工作區分析，瞭解整個工作區的採用情況。
使用 Codex 分析，取得以 Codex 為主的報告。
使用 Analytics API，以程式方式取得彙總資料；
使用 Compliance API，取得可供稽核的記錄。

這些報告介面不會授予產品存取權，也不會設定執行階段政策。請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
，瞭解管理上的界線。

## 選擇報告介面

| 介面                     | 用途                                                    | 規範依據                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作區分析 | 涵蓋整個工作區採用與參與情況的互動式報告 | [說明中心的工作區分析指南](https://help.openai.com/en/articles/10875114)                               |
| Codex 分析             | 專注於 Codex 採用與活動情況的互動式報告  | 需驗證身分才能存取的 [Codex 分析儀表板](https://admin.openai.com/analytics/codex)                                |
| Analytics API               | 以程式方式取得 Codex 彙總報告                      | [Codex Analytics API 參考文件](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| Compliance API              | 稽核、安全性、法律與調查記錄             | [Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)                                              |

## 審查 ChatGPT 工作區分析

ChatGPT 工作區分析提供互動式檢視，讓你瞭解工作區中受支援功能的採用情況
與參與情況。可用性、角色、儀表板區段、
資料更新時效、隱私權處理方式與匯出格式都可能變更。請參閱
[ChatGPT Enterprise 與 Edu 的工作區分析](https://help.openai.com/en/articles/10875114)
，瞭解目前的涵蓋範圍與操作程序。

請將下載的報告視為可識別身分的組織資料。
遵循組織的存取、儲存與保留政策，
不要假設匯出資料與彙總儀表板
具有相同的隱私權特性。

## 審查 Codex 分析

需驗證身分才能存取的 [Codex 分析儀表板](https://admin.openai.com/analytics/codex)
專注於 Codex 報告。請用它進行互動式探索，不應將它視為穩定的
結構描述規範。儀表板的類別、欄位、篩選條件與匯出格式，都可能
在本頁未更新的情況下變更。

若要自動產生報告，請使用 [Analytics API](/zh-Hant/codex/enterprise/analytics-api)
，並依照其 API 參考文件操作。若要取得可供稽核的記錄，請使用
[Compliance API](/zh-Hant/codex/enterprise/compliance-api)。

## 解讀報告資料

請留意以下界線：

- ChatGPT 工作區分析與 Codex 分析
涵蓋不同的產品範圍。
- 彙總分析與稽核記錄用途不同，
且各有獨立的規範。
- 分析呈現活動情況；
不會授予存取權，也不會變更執行階段權限。
- [ChatGPT 使用限制與支出控管](/zh-Hant/codex/enterprise/usage-limits) 是
  另一項依方案而異的工作區限制。
