<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/ios-liquid-glass -->

## 從 iOS 26 基準著手

先將 Liquid Glass 視為 iOS 26 和 Xcode 26 的遷移專案。使用 iOS 26 SDK 重新建置應用程式，檢視標準 SwiftUI 控制項會自動呈現哪些效果，最後才請 Codex 重新設計那些仍顯得過於扁平、厚重，或與系統介面元件格格不入的自訂部分。

如果應用程式仍支援較早的 iOS 版本，請一開始就明確說明這項限制。[Build iOS Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) 中的 SwiftUI Liquid Glass 技能應透過 `#available(iOS 26, *)` 控管新的玻璃效果專用 API，並保留在舊裝置上仍清晰易讀的後備路徑。

## 善用 iOS 外掛程式

如果想讓 Codex 將 SwiftUI UI 變更與模擬器驗證結合，請使用 [Build iOS Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)。進行 Liquid Glass 遷移時，較有效的做法是要求 Codex 先稽核一個流程、遷移少數幾個介面，在 iOS 26 模擬器上啟動成果並擷取螢幕截圖，再擴大範圍。

這個外掛程式內含 SwiftUI Liquid Glass 技能，其中有一組簡單的預設做法，值得納入提示詞：

- 優先使用原生 `glassEffect`、`GlassEffectContainer`、玻璃效果按鈕樣式及 `glassEffectID` 轉場，而不是自訂模糊效果檢視。
- 在配置和視覺修飾器之後套用 `.glassEffect(...)`，讓材質包覆實際想要的最終形狀。
- 當多個介面元素一同出現時，請以 `GlassEffectContainer` 包裹相關的玻璃效果元素。
- 只有按鈕、標籤及確實會回應觸控的控制項才使用 `.interactive()`。
- 整項功能中的圓角形狀、色調與間距應保持一致，不要混用零散的玻璃效果設計。
- 為 iOS 26 之前的部署目標保留非玻璃效果的後備方案。

若要進一步瞭解如何安裝外掛程式和技能，請參閱我們的 [外掛程式](/zh-Hant/codex/plugins) 與 [技能](/zh-Hant/codex/build-skills) 文件。

## 觀看 WWDC 講座

在要求 Codex 重構實際的正式產品流程之前，以下 WWDC25 講座是不錯的參考資料：

- [認識 Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)
- [認識全新設計系統](https://developer.apple.com/videos/play/wwdc2025/356/)
- [使用全新設計建構 SwiftUI App](https://developer.apple.com/videos/play/wwdc2025/323/)
- [使用全新設計建構 UIKit App](https://developer.apple.com/videos/play/wwdc2025/284/)
- [SwiftUI 新功能](https://developer.apple.com/videos/play/wwdc2025/256/)

## 先要求遷移計畫，再實作一個片段

讓 Codex 將「哪裡應該出現玻璃效果？」與「現在就寫出所有程式碼」分開處理，Liquid Glass 遷移通常會更順利。請先要求快速稽核，再讓智慧體實作一個可獨立完成的片段，並以模擬器驗證。

## 實用技巧

### 不要對所有元素套用玻璃效果

Liquid Glass 應在內容上方建立清楚的控制層，而不是把每張卡片都變成發光面板。請 Codex 移除與系統材質衝突的裝飾背景，在易讀性最重要的地方保留無裝飾的內容，並僅在需要語意強調或凸顯主要操作時使用色調。

### 從一個使用頻繁的流程著手

分頁根畫面、詳細資料畫面、面板、搜尋介面或新手引導流程，通常比一次遷移整個應用程式更適合作為第一個目標。這能讓審查更容易，也能釐清哪些 Liquid Glass 設計決策應轉化為可重複使用的元件模式。

### 仔細審查後備行為

如果部署目標低於 iOS 26，請 Codex 同時呈現後備實作與 Liquid Glass 版本。這個審查步驟能找出非預期的 API 可用性迴歸問題，避免發佈只能在最新模擬器上運作的遷移成果。
