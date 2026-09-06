<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/native-ios-apps -->

## 建立應用程式與建置迴圈的初始架構

對於全新開發工作，先直接使用提示詞即可。請 Codex 建立一個入門 iOS SwiftUI 應用程式的初始架構，並撰寫小型建置與啟動指令碼，可連接至 `Build` 動作；該動作位於 [本機環境](/zh-Hant/codex/environments/local-environment)。

建置迴圈應以 CLI 為優先。Apple 的 `xcodebuild` 能列出 scheme，並從終端執行建置、測試、封存、`build-for-testing` 與 `test-without-building` 動作，讓 Codex 能持續處於智慧體式迴圈中，無須反覆切換至 Xcode GUI。

如果你想使用更簡潔的專案產生器，也能接受第三方工具，可考慮以 [Tuist](https://tuist.dev/) 作為下一步。它不需使用 GUI 即可產生及建置 Xcode 專案，同時仍可讓 Codex 從終端建置並啟動應用程式。

進入完整的 Xcode 專案後，如果需要更深入的自動化，請使用 [XcodeBuildMCP](https://www.xcodebuildmcp.com/)。到了這個階段，scheme、目標、模擬器控制、螢幕截圖、記錄與 UI 互動都很重要，一般 shell 指令已不足以完成所有工作。

## 善用技能

初次處理時，通常不需要技能或 MCP 伺服器。若工作開始涉及專門領域，或你希望執行流程更確實遵循 SwiftUI 慣例，再加入技能。

- [SwiftUI expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) 是一項功能強大的通用 SwiftUI 技能，已內建許多最佳實務。
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) 是一項全面的 SwiftUI 審查技能，涵蓋現代 API、可維護性、無障礙功能與效能。

- [Liquid Glass expert](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) 可協助 Codex 採用新的 iOS 26 Liquid Glass API，並調校自訂元件，使其符合最新的系統設計。
- 當功能感覺遲緩，或 SwiftUI 檢視更新路徑看起來不太對勁時，[SwiftUI performance](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) 很有幫助。它會掃描常見的 SwiftUI 錯誤，並產生依優先順序排列的報告，指出該修正哪些問題，以及哪些地方的改善幅度最大。
- 當晦澀的錯誤和編譯器警告開始阻礙你想進行的變更時，[Swift concurrency expert](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) 很有幫助。在 GPT-5.6 Terra 上，你可能比較不常需要它；但當 Swift 並行處理的診斷訊息過多而難以判讀時，它仍很實用。
- [SwiftUI view refactor](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) 有助於維持檔案精簡，並提高整個程式碼庫中 SwiftUI 程式碼的一致性。
- 隨著應用程式擴充，[SwiftUI patterns](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) 有助於採用可預期的 `@Observable` 與 `@Environment` 架構模式。

若要進一步瞭解如何安裝及使用技能，請參閱我們的 [技能文件](/zh-Hant/codex/build-skills)。

## 反覆改進

初版能夠運作後，或若你從現有專案開始，即可著手反覆調整 UI 或行為。

在這個階段，請具體說明要變更的內容和方式。

請在提示詞中明確交代這些資訊：告訴 Codex 它正在處理全新的程式碼庫還是現有 Xcode 專案、應用程式必須在哪些 iOS 裝置或部署目標上繼續正常運作，以及你預期採用何種驗證迴圈。

### 提示詞範例

例如，若要為現有應用程式新增功能，可以要求 Codex 進行如下變更：

## 實用技巧

### 從基本做起

對於全新開發工作，先直接使用提示詞即可。請 Codex 建立一個入門 SwiftUI 應用程式的初始架構，並撰寫小型建置與啟動指令碼，可連接至 `Build` 動作；該動作位於 [本機環境](/zh-Hant/codex/environments/local-environment)。初次處理時，通常不需要任何技能或 MCP 伺服器。

### 採用小而可靠的驗證迴圈

每次變更後，要求 Codex 執行範圍最小、但確實能驗證所修改契約的指令。之後再擴大建置範圍。這可讓 Codex 保持快速，又不會誤把完整的應用程式建置當成每次編輯都必須執行的步驟。

### 維持以 CLI 為優先的迭代流程

維持以 CLI 為優先的迭代流程。Apple 的 `xcodebuild` 工具可以列出 scheme，並從終端執行 build、test、archive、`build-for-testing` 和 `test-without-building` 動作，讓 Codex 能持續在智慧體式迭代流程中運作，不必反覆切換至 Xcode 圖形使用者介面。

### 善用 XcodeBuildMCP

只要你已進入完整的 Xcode 專案，且需要更深入的自動化，就使用 XcodeBuildMCP。當工作需要處理 scheme、target、模擬器控制、螢幕截圖、日誌和 UI 互動，單靠一般 shell 指令已不足時，就該採用它。
