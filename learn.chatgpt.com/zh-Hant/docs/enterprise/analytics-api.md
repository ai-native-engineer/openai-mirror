<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/analytics-api -->

Codex Analytics API 提供 ChatGPT 工作區的
Codex 使用情況與活動彙總指標。

[Codex Analytics API 參考文件](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
是目前存取要求、路由、請求與
回應的結構描述、指標、時間語意及分頁機制的權威依據。

## 何時使用 Analytics API

Analytics API 適用於下列需求：

- 將定期產出 Codex 報表的流程自動化。
- 將彙總的 Codex 指標與組織內部資料結合。
- 建立供經核准對象使用的受控報表層。
- 避免將整合功能與互動式儀表板耦合。

這不是原始稽核記錄介面。
若工作流程需要可供稽核的活動記錄，
請使用 [Compliance API](/zh-Hant/codex/enterprise/compliance-api)。

## 確認管理範圍

Analytics API 的結果範圍限定於 ChatGPT 工作區，但請求須使用
Platform 組織的 API 金鑰進行身分驗證。金鑰所屬組織必須
與工作區所關聯的組織相符。

目前的金鑰佈建、權限範圍要求、路由、結構描述、欄位、
時間語意及分頁行為，皆以 API 參考文件為準。
本頁不再重述這些規範。

## 相關文件

- [工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)
- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [治理](/zh-Hant/codex/enterprise/governance)
- [Compliance API](/zh-Hant/codex/enterprise/compliance-api)
