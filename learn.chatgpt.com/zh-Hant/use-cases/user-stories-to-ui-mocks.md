<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/user-stories-to-ui-mocks -->

## 簡介

產品團隊經常從各種來源收集意見回饋，例如 Slack 討論串、Linear 議題、Google Drive 文件或試算表，以及客戶通話筆記。有時，他們已有清楚的使用者故事，可以說明想解決的問題；有時，相關上下文則包含在這些來源中。

ChatGPT 可以彙整這些上下文，並據此為能解決該問題的功能製作 UI 模擬稿。確認方向後，Codex 就能在產品中實作這項功能。

## 建立視覺基準

如果已有清楚的使用者故事，可以直接以此為起點。否則，可以先與 ChatGPT 討論，從不同來源收集上下文，再將其彙整成使用者故事。

接著，可以請 ChatGPT 使用圖像生成功能，產生幾個不同方向的模擬稿。這些模擬稿應保留產品的資訊架構，並符合設計系統的限制。

如有幫助，可以提供目前 UI 的螢幕截圖或 Figma 檔案作為參考。

持續調整，直到你對模擬稿感到滿意為止。變更範圍界定得越清楚，Codex 就越可能產生可直接實作的模擬稿。

## 從模擬稿到原型

請使用你希望 Codex 實作的最終模擬稿圖片。選取 Codex、開始新對話，並重新附加該圖片，不要直接接續原本的 ChatGPT 對話。接著，請 Codex 實作這份模擬稿——如果你正在建置網頁應用程式，也可以選擇使用 [Build Web Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)——將它轉化為可運作的原型：
