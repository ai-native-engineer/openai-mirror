<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/complete-tasks-from-messages -->

## 簡介

許多訊息對話串其實都藏著待辦事項：預訂晚餐座位、安排後續追蹤、研究各種選項、提交收據，或彙整回覆所需的資訊。電腦可讀取對話串、辨識任務，並在相關應用程式中完成工作。

當訊息包含明確請求，而你希望 ChatGPT 負責後續處理，不只是摘要對話串時，這種做法很適合。

## 使用方式

1. 請安裝 [電腦外掛程式](/zh-Hant/codex/computer-use)。
2. 請 ChatGPT 審查特定訊息對話串，或特定傳送者的訊息。
3. 告訴 ChatGPT 要執行哪項操作，以及是否應在完成任何操作前暫停。
4. 指定 ChatGPT 是否應在原對話串中草擬回覆。

例如：

- `@Computer Look at my messages from [person]. Check my availability, find 2 dinner options in Hayes Valley, and draft a reply in the same thread. Check in with me before completing booking.`

## 實用提示

### 要求在執行無法復原的操作前先暫停

如果任務可能涉及轉帳、送出訂單、確認預訂或敲定行程，請告訴 ChatGPT 在執行最後一步前先停下來詢問你。

### 確認相關應用程式已準備就緒

相關應用程式都已登入且可供使用時，這種做法的效果最佳。如果任務需要使用「地圖」、「行事曆」、「備忘錄」、預訂網站或瀏覽器工作階段，請事先準備好這些項目。

### 請留意對話串會標示為已讀

當 ChatGPT 在「訊息」中開啟對話串時，其行為與一般使用者檢視對話時相同。請將該對話串視為已讀。

## 後續建議

如果工作從一則訊息開始，並在其他地方完成，同樣的模式也適用於 Slack 或電子郵件等其他類似收件匣的介面。如果這套工作流程成為常態，請在 [自訂](/zh-Hant/codex/customization/overview) 中加入可重複使用的偏好設定或指示，讓 ChatGPT 每次都以相同方式處理這類請求。

### 建議的提示詞

**根據訊息對話串完成一項任務**
