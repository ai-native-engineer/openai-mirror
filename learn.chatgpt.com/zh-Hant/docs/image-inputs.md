<!-- source: https://learn.chatgpt.com/zh-Hant/docs/image-inputs -->

當任務需要視覺上下文時（例如錯誤
螢幕截圖、介面設計、架構圖或現有素材），請在提示詞中加入圖像。請說明
ChatGPT 應檢查的內容與你想要的結果；不要只靠圖像
本身來傳達任務內容。

按住 <kbd>Shift</kbd> 鍵，將圖像拖入提示詞撰寫工具，即可將
它納入上下文。你也可以要求 ChatGPT 檢查系統中的圖像，或使用
螢幕截圖工具驗證其他 App 中的工作成果。

在 ChatGPT Web 撰寫工具中附加、貼上或拖入圖像。在提示詞中，
告訴 ChatGPT 要檢查哪些內容，以及你希望從圖像取得什麼結果。

將圖像貼到互動式撰寫工具中，或透過
指令列傳入一個或多個檔案：

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

若有多張圖像，請用逗號分隔各路徑，或重複使用 `--image`。Codex
接受 PNG 和 JPEG 等常見圖像格式。

按住 <kbd>Shift</kbd> 鍵，將圖像拖入提示詞撰寫工具，讓
擴充功能接收這項拖放操作，而不是將它傳給編輯器。

## 配合圖像撰寫提示詞

說明圖像顯示的內容、指出重點區域，並清楚指定所需輸出
與限制條件。若附加多張圖像，請逐一標明，並說明
ChatGPT 應如何比較這些圖像。

例如：

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## 選用合適的圖像功能

若要 ChatGPT 檢查視覺參考資料，請使用圖像輸入。請使用
[圖像生成](/zh-Hant/codex/image-generation)，讓 ChatGPT
建立或編輯圖像。
