<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/native-macos-apps -->

## 建立應用程式初始架構與建置迴圈

對於新的 Mac 應用程式，先請 Codex 選擇正確的場景模型： `WindowGroup`、`Window`、`Settings`、`MenuBarExtra` 或 `DocumentGroup`。這能讓應用程式從第一次實作起就符合桌面原生體驗，而不是從 `ContentView` 這類 iOS 風格的檢視逐步擴充而成。

讓執行迴圈維持以 shell 為優先。Xcode 專案請使用 `xcodebuild`。以套件為核心的應用程式則使用 `swift build`，並搭配專案內的 `script/build_and_run.sh` 包裝指令碼，以停止舊的處理程序、建置應用程式、啟動新的建置產出物，並可選擇提供日誌或遙測資料。

如果純 SwiftPM 應用程式是 GUI 應用程式，請將它封裝成 `.app` 並以此啟動，而不要直接執行原始可執行檔。這可避免在本機驗證時發生 Dock 不顯示、無法啟用或套件識別資訊缺失等問題。

## 善用技能

當工作內容變得更偏重桌面平台時，請加入 [Build macOS Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)。它涵蓋以 shell 為優先的建置與偵錯迴圈、SwiftPM 應用程式封裝、原生 SwiftUI 場景與視窗模式、AppKit 互通性、統一日誌記錄、測試問題分類，以及簽署與公證工作流程。

若要進一步瞭解如何安裝及使用外掛程式與技能，請參閱 [外掛程式文件](/zh-Hant/codex/plugins) 與 [技能文件](/zh-Hant/codex/build-skills)。

## 建置桌面原生 UI

優先採用 Mac 慣例，而非 iOS 導覽模式。側邊欄與詳細資料配置請使用 `NavigationSplitView`、偏好設定請使用明確定義的 `Settings` 場景、易於發現的操作請使用工具列與指令，輕量且隨時可用的工具則使用選單列附加項目。

優先使用系統材質、語意色彩與標準控制項。只有在產品需要獨特的桌面介面時，才加入自訂視窗樣式、拖曳區域或 Liquid Glass 介面。

如果 SwiftUI 幾乎能滿足需求但仍有不足，請加入範圍盡可能小的 AppKit 橋接層。適合這麼做的場景包括開啟/儲存面板、第一回應者控制、選單驗證、拖放邊界處理，以及為單一特殊控制項包裝 `NSView`。

## 偵錯、測試並準備發布

若要觀察執行階段行為，請 Codex 針對視窗開啟、側邊欄選取、選單指令或背景同步加入幾個 `Logger` 事件，然後在應用程式啟動後使用 `log stream` 驗證這些事件。

對於失敗的測試，讓 Codex 先執行範圍最小但足以診斷問題的 `xcodebuild test` 或 `swift test`，再判斷問題屬於編譯問題、斷言失敗、當機、偶發性失敗，或環境/設定問題。

當工作從本機反覆開發轉向發佈時，請 Codex 同時準備 Xcode 手動封存流程，以及以指令碼執行的封存與公證流程，讓發布作業可重複進行。請它使用 `codesign` 與 `plutil` 檢查應用程式套件、權利設定和強化執行階段；如果也想讓上傳作業留在終端中，則使用 [App Store Connect CLI](https://asccli.sh/)。

## 提示詞範例

## 實用提示

### 明確定義各個場景

將主視窗、設定視窗、工具視窗與選單列附加項目分別建模為獨立的場景根節點，而不要把整個應用程式都藏在單一大型檢視中。

### 多善用系統介面元件

建立自訂側邊欄、工具列或材質之前，先確認標準 SwiftUI 場景與視窗 API 是否已能提供所需的 Mac 行為。

### 將 AppKit 限定在必要的邊界

使用 `NSViewRepresentable`、`NSViewControllerRepresentable` 或專用的 `NSWindow` 輔助工具來補足單一欠缺的桌面功能，但仍應以 SwiftUI 作為選取項目和應用程式狀態的唯一依據。

### 簽署與公證應和本機建置分開驗證

本機成功啟動不代表應用程式已完成簽署或已可送交公證。保留手動 Xcode 封存流程以進行單次發布檢查，並加入指令碼式封存與公證流程以支援可重複的發佈；當任務目標是發布，而不只是本機反覆開發時，請執行 `codesign` 與 `plutil` 檢查。
