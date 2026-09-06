<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/macos-sidebar-detail-inspector -->

## 从 Mac 场景模型开始

此用例可将应用构想转化为真正为桌面端打造的 Mac 应用框架，而不是把触控优先的界面堆栈拉伸到桌面端。先让 Codex 选择场景模型，再围绕稳定的边栏选中状态、详情界面以及用于辅助控件或元数据的检查器设计主窗口。

![一个 Mac 原生边栏和详情应用框架，边栏中有一个选中项，详情面板中显示其内容](/images/codex/use-cases/macos-sidebar-detail-inspector.png)

如果您希望 Codex 应用这种桌面结构，并让构建/运行循环以 Shell 为先，请使用 [Build macOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)。其中的 macOS SwiftUI 模式技能非常适合用于场景设计、边栏、检查器、命令和设置；如果仅有某项 Mac 特有行为无法由 SwiftUI 简洁实现，也适合添加少量 AppKit 桥接。

## 构建边栏、详情面板和检查器

如果功能需要持久导航和稳定的选中项，请优先使用 `NavigationSplitView`。边栏中的行应保持原生、轻量，边栏应采用系统背景；自定义卡片或密集元数据只应放在详情面板或检查器中。

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

如果应用需要非常规的分栏尺寸、底层窗口协调或自定义响应者链行为，请让 Codex 保持 SwiftUI 应用框架不变，只针对这一处缺口添加所需的最小 AppKit 桥接。

## 将命令、工具栏和快捷键放在桌面层

Mac 用户应能通过菜单栏、工具栏和键盘快捷键找到重要操作。让 Codex 围绕同一组应用操作接入场景级 `commands`、上下文相关的菜单项和工具栏按钮，这样桌面端用户就不必费力寻找仅支持手势的控件。

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

如果命令应作用于当前显示的详情项，请使用 `FocusedValue`、场景状态或显式选择状态。如果某个快捷键会在多处注册，请让 Codex 统一其所有权，使应用只有一条清晰的命令执行路径。

## 将偏好设置放在 `Settings` 中

对于应用偏好设置，请使用专用 `Settings` 场景，并通过 `@AppStorage` 持久保存需要长期保留的用户选择。这通常比在主内容窗口中推入设置屏幕更符合 Mac 应用习惯。

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

## 先在提示中描述应用构想，再验证应用框架

要充分利用本页，您的提示应明确应用构想、主要内容对象和核心操作，然后让 Codex 先围绕该工作流构建桌面应用框架。让智能体执行一项简单的构建/运行检查，并总结场景结构、命令接入、状态所有权，以及它必须通过 AppKit 桥接处理的任何边缘情况。

## 实用技巧

### 保持边栏采用原生样式

边栏中的每一行仅使用一个图标、一行标题，次要文本最多一行且应简短。将信息更丰富的卡片、计数器和元数据移到详情面板或检查器中，以便快速浏览源列表。

### 不要将设置隐藏在主内容堆栈中

如果某项用户偏好影响整个应用，请让 Codex 将该控件放在 `Settings` 中，使用 `@AppStorage` 持久保存，并通过应用菜单提供入口，而不是再构建一个通过导航推入的设置屏幕。

### 仅用 AppKit 弥补少量桌面端能力缺口

如果该功能需要打开或保存面板、第一响应者控制或自定义 `NSView`，请仅在由 SwiftUI 持有的状态模型外围添加一小层 AppKit 边界，而不要用 AppKit 重写整个窗口。
