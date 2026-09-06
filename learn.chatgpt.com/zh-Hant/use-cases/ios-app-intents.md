<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/ios-app-intents -->

## 讓系統看見 App 中合適的部分

App Intents 是讓 iOS App 在自身 UI 之外發揮更多用途最直接的方式之一。不要把 App 當成封閉空間，非得等使用者啟動並四處點選後才能使用；請改用 Codex，將應供捷徑、Siri、Spotlight、小工具、控制項，以及較新的助理驅動系統體驗使用的動作與物件公開出來。

這對目前的可探索性和自動化都很有幫助，也是迎接更由助理驅動之未來的重要準備。若你的 App 已能撰寫、開啟、篩選、導向或摘要有價值的內容，App Intents 就能讓系統以結構化方式要求執行這些功能。

## 先從動作和實體著手，而不是每個畫面

第一次實作 App Intents 時，通常不應「照搬整個 App」。請 Codex 找出：

- 使用者無須瀏覽完整介面就會想觸發的少數動作
- 系統為了正確導向這些動作而需要理解的 App 物件
- 應以特定狀態開啟 App 的工作流程，以及應直接在系統介面完成的工作流程

Apple 的 App Intents 指南很適合用來架構這項工作：定義動作、定義系統所需的實體介面，再讓這些動作可在各種系統體驗中探索並重複使用。最實用的參考資料包括 [讓動作與內容可供探索並廣泛使用](https://developer.apple.com/documentation/appintents/making-actions-and-content-discoverable-and-widely-available)、[建立你的第一個 App Intent](https://developer.apple.com/documentation/appintents/creating-your-first-app-intent)，以及系統體驗範例 [採用 App Intents 以支援系統體驗](https://developer.apple.com/documentation/appintents/adopting-app-intents-to-support-system-experiences)。

## 從系統介面的角度思考，而不只是捷徑

機會不只「新增一個捷徑」這麼簡單。設計完善的 App Intents 介面能讓 App 在多個地方發揮作用：

- 捷徑可讓使用者直接執行動作，或將動作組合成更大型的自動化
- Siri 可讓 App 公開具體有意義的動詞與深層連結，而不只是以一般方式開啟 App
- Spotlight 可讓 App 實體和 App 捷徑成為可供探索的系統進入點
- 小工具、即時動態、控制項，以及其他由意圖驅動的 UI 介面
- 較新的面向助理體驗；相較於沒有固定結構的 UI 流程，系統更容易理解結構化動作和實體

## 遵循實際 App 的模式

App 採用以下結構時，通常效果最好：

- 使用專用的 App Intents target，而不是將意圖型別散落在彼此無關的 App 檔案中
- `AppShortcutsProvider` 項目，用於撰寫貼文或在特定分頁開啟 App 等高價值使用者動作
- 小型 `AppEntity` 型別，用來表示系統需要理解的項目，例如帳號、列表和時間軸篩選器
- 能順暢導回主要 App 場景的意圖處理方式，讓叫用的意圖可開啟正確的撰寫流程，或將 App 切換至正確的分頁

對多數 App，我會要求 Codex 遵循這種模式：先建立精簡、面向系統的動作層，將實體介面控制在精簡範圍，並在意圖需要主要 UI 時，建立可預期的執行階段交接機制，將流程交回 App。

## 請 Codex 設計第一個意圖介面

最有效的提示詞會先向 Codex 提供 App 的核心物件和主要使用者動作，再要求它選擇首版中規模最小但有實用價值的 App Intents 介面，而不是盲目公開所有內容。

## 實用訣竅

### 公開使用者確實想在 App 外觸發的動作

好的首批意圖通常是撰寫、開啟、尋找、篩選、開始、繼續或檢視等動作。若某個動作只有完成冗長的 App 內設定流程後才實用，就可能不適合納入第一輪 App Intents 實作。

### 實體應比模型層精簡

系統通常不需要完整的持久化模型。請 Codex 定義範圍最小的 App 實體介面，同時仍為 Siri、捷徑和 Spotlight 提供足夠的上下文，以正確導向並顯示動作。

### 將其視為助理基礎架構，而不只是捷徑功能

即使第一個版本明顯改善的只有 Shortcuts 或 Siri，真正更深層的效益在於，你的應用程式開始以結構化動作與實體來描述自身功能。相較於功能只編碼在點按操作與檢視階層中的應用程式，這能讓你的應用程式更容易融入未來由系統與 AI 驅動的各種進入點。
