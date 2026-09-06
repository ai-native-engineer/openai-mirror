<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/macos-sidebar-detail-inspector -->

## 從 Mac 場景模型開始

此使用案例旨在將應用程式構想打造成專為桌面設計的 Mac 應用程式殼層，而不是把觸控優先的堆疊勉強拉伸成桌面版。請 Codex 先選擇場景模型，再以穩定的側邊欄選取狀態、詳細資料區域，以及用於次要控制項或中繼資料的檢查器來設計主視窗。

![Mac 原生側邊欄與詳細資料應用程式殼層，側邊欄中有一個已選取項目，詳細資料窗格則顯示內容](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

當你希望 Codex 套用這種桌面結構，並讓建置/執行迭代以 Shell 為主時，請使用 [Build macOS Apps 外掛程式](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)。其 macOS SwiftUI 模式技能很適合用於場景設計、側邊欄、檢查器、指令、設定，以及在 SwiftUI 尚無法完整實現某項 Mac 特有行為時加入小型 AppKit 橋接層。

## 建構側邊欄、詳細資料窗格和檢查器

若功能需要持續顯示的導覽與穩定的選取項目，應優先使用 `NavigationSplitView`。側邊欄列應維持原生且精簡，側邊欄採用系統背景，並將自訂卡片或密集的中繼資料留給詳細資料窗格或檢查器。

```swift
struct LibraryRootView: View {
  @SceneStorage("LibraryRootView.selection") private var selection: Item.ID?
  @SceneStorage("LibraryRootView.showInspector") private var showInspector = true

  var body: some View {
    NavigationSplitView {
      List(selection: $selection) {
        ForEach(items) { item in
          Label(item.title, systemImage: item.systemImage)
            .tag(item.id)
        }
      }
      .listStyle(.sidebar)
      .navigationTitle("Library")
    } detail: {
      ItemDetailView(selection: selection)
        .inspector(isPresented: $showInspector) {
          ItemInspectorView(selection: selection)
        }
    }
  }
}

如果應用程式需要特殊的分割檢視尺寸、低階視窗協調或自訂回應者鏈行為，請 Codex 保留完整的 SwiftUI 殼層，只為該功能缺口加入所需的最小 AppKit 橋接層。

## 將指令、工具列和快速鍵置於桌面層

Mac 使用者應能從選單列、工具列和鍵盤快速鍵找到重要動作。請 Codex 以相同的應用程式動作為核心，串接場景層級的 `commands`、依上下文變化的選單項目和工具列按鈕，讓桌面使用者不必四處尋找只能透過手勢操作的控制項。

```swift
@main
struct LibraryApp: App {
  var body: some Scene {
    WindowGroup {
      LibraryRootView()
    }
    .commands {
      CommandMenu("Library") {
        Button("New Item") {
          // Create a new item.
        }
        .keyboardShortcut("n")

        Button("Toggle Inspector") {
          // Route this command to the focused window or selected item state.
        }
        .keyboardShortcut("i", modifiers: [.command, .option])
      }
    }

    Settings {
      LibrarySettingsView()
    }
  }
}

當指令應套用至目前的詳細資料項目時，請使用 `FocusedValue`、場景狀態或明確的選取狀態。若同一個快速鍵會在多處註冊，請 Codex 將所有權集中至一處，讓應用程式只有一條明確的指令路徑。

## 將偏好設定放在 `Settings` 中

對應用程式偏好設定，請使用專用的 `Settings` 場景，並透過 `@AppStorage` 長期保存使用者選擇。相較於在主要內容視窗內推入設定畫面，這通常更符合 Mac 的使用方式。

```swift
struct LibrarySettingsView: View {
  @AppStorage("showItemMetadata") private var showItemMetadata = true

  var body: some View {
    TabView {
      Form {
        Toggle("Show Item Metadata", isOn: $showItemMetadata)
      }
      .tabItem { Label("General", systemImage: "gearshape") }
    }
    .frame(width: 460, height: 260)
    .scenePadding()
  }
}

## 先用提示詞描述應用程式概念，再驗證殼層

使用本頁時，最好在提示詞中說明應用程式概念、主要內容物件和主要動作，再要求 Codex 優先依該工作流程建構桌面殼層。請智慧體執行小規模的建置/執行檢查，並摘要說明場景結構、指令串接、狀態所有權，以及任何必須以 AppKit 補足的邊界情況。

## 實用技巧

### 讓側邊欄維持原生樣式

側邊欄列應使用一個圖示、一行標題，最多再加一行簡短的次要文字。將資訊更豐富的卡片、計數器和中繼資料移至詳細資料窗格或檢查器，讓來源清單仍能輕鬆瀏覽。

### 避免將偏好設定藏在主要堆疊中

如果某項使用者偏好會影響整個應用程式，請 Codex 將該控制項放在 `Settings` 中並搭配 `@AppStorage`，再透過應用程式選單提供進入點，而不要另行建立推入式設定畫面。

### 僅用 AppKit 補足特定的桌面功能缺口

如果功能需要開啟/儲存面板、第一回應者控制或自訂 `NSView`，請將 AppKit 限制在 SwiftUI 所擁有的狀態模型外圍，僅補足少量功能，而不要用 AppKit 重寫整個視窗。
