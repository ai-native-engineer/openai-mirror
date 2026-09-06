<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/draft-prds-from-sources -->

## 簡介

在著手開發新產品或功能前，通常會先草擬產品需求文件（PRD），以便就範圍和需求達成共識。多數情況下，撰寫這份 PRD 所需的上下文早已存在於團隊內部系統中，例如 Linear 中的議題、Slack 上的討論，以及 Notion 或 Google Drive 中的草稿等。ChatGPT 可以彙整這些上下文，草擬一份 PRD 供你審查並反覆完善，同時保留清楚、可追溯的來源資訊。

## 選擇來源

首先提供你希望 ChatGPT 使用的來源：Linear 專案、Slack 規劃頻道或討論串，以及 PRD 應引用的任何 Drive 文件、Notion 頁面、會議筆記或本機檔案。
也請清楚列出你預期的 PRD 章節，例如問題、使用者、需求、UX、技術、發布計畫、時程或決策。

1. 當輸出需要是實際的 DOCX 檔案時，請從 `$documents` 著手。
2. 直接指明來源：Linear 專案或里程碑、Slack 頻道或討論串，以及 ChatGPT 應引用的文件或筆記。
3. 向 ChatGPT 提供 PRD 的章節規範。
4. 先審查來源附錄，再審查需求和待解問題。
5. 在同一個對話中補齊缺漏、收斂範圍並準備交接。

<a id="refine-in-the-same-chat"></a>
<a id="refine-in-the-same-task"></a>

## 在同一個對話中持續完善

使用本頁的起始提示詞建立初稿。若有內容缺漏，請讓 ChatGPT 參考缺少的來源，而不是從頭開始。

## 檢查來源是否可追溯

在分享 PRD 前，請 ChatGPT 列出以下內容：來源佐證不足或缺漏的主張、尚未解決的問題，以及它視為已確認的決策。如果來源附錄無法讓這些項目易於查核，請先在同一個對話中繼續完善內容，再匯出或發布任何內容。

### 建議提示詞

**檢查來源是否可追溯**
