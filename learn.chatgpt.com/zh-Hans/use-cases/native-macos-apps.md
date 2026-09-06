<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/native-macos-apps -->

## 搭建应用脚手架和构建循环

对于新的 Mac 应用，先让 Codex 选择合适的场景模型：`WindowGroup`、`Window`、`Settings`、`MenuBarExtra` 或 `DocumentGroup`。这样，应用从第一版起就具备桌面原生体验，而不会从 iOS 风格的 `ContentView` 逐步扩展而来。

保持执行循环以 Shell 为先。对于 Xcode 项目，使用 `xcodebuild`。对于以软件包为先的应用，使用 `swift build` 和项目本地的 `script/build_and_run.sh` 包装脚本；该脚本会停止旧进程、构建应用、启动新产物，并可选择提供日志或遥测数据。

如果纯 SwiftPM 应用是 GUI 应用，请将其打包为 `.app` 后再启动，而不要直接运行原始可执行文件。这样可以避免本地验证期间出现 Dock 不显示、应用无法激活或应用包标识缺失等问题。

## 利用技能

当工作开始涉及更多桌面端特性时，请添加 [Build macOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-macos-apps)。该插件涵盖 Shell 优先的构建和调试循环、SwiftPM 应用打包、原生 SwiftUI 场景和窗口模式、AppKit 互操作、统一日志记录、测试问题分类排查，以及签名和公证工作流。

要详细了解如何安装和使用插件及技能，请参阅 [插件文档](/zh-Hans/codex/plugins) 和 [技能文档](/zh-Hans/codex/build-skills)。

## 构建桌面原生 UI

应优先遵循 Mac 惯例，而不是 iOS 导航模式。侧边栏/详细信息布局使用 `NavigationSplitView`，偏好设置使用显式的 `Settings` 场景，可发现的操作使用工具栏和命令，轻量级且随时可用的实用工具则使用菜单栏附加项。

优先使用系统材质、语义颜色和标准控件。仅当产品需要独特的桌面界面时，才添加自定义窗口样式、拖拽区域或 Liquid Glass 界面效果。

如果 SwiftUI 已基本满足需求但仍有不足，请添加尽可能精简的 AppKit 桥接层。适用场景包括打开/存储面板、第一响应者控制、菜单验证、拖放边界行为，以及为某个专用控件封装一个 `NSView`。

## 调试、测试并准备发布

对于运行时行为，让 Codex 在打开窗口、选择侧边栏项、执行菜单命令或后台同步等环节添加一些 `Logger` 事件，然后在应用启动后使用 `log stream` 验证这些事件。

测试失败时，先让 Codex 以最小的有效范围运行 `xcodebuild test` 或 `swift test`，并判断问题属于编译错误、断言失败、崩溃、偶发性失败，还是环境/设置问题。

当工作从本地迭代转向分发时，让 Codex 同时准备 Xcode 手动归档流程，以及基于脚本的归档和公证流程，以便可重复发布。让它使用 `codesign` 和 `plutil` 检查应用包、授权信息和强化运行时；如果您也希望在终端中完成上传，请使用 [App Store Connect CLI](https://asccli.sh/)。

## 示例提示

## 实用技巧

### 明确定义场景

将主窗口、设置窗口、实用工具窗口和菜单栏附加项分别建模为独立的场景根节点，而不是把整个应用藏在一个庞大的视图中。

### 让系统界面元素承担更多工作

在创建自定义侧边栏、工具栏或材质之前，先检查标准 SwiftUI 场景和窗口 API 是否已经能够提供您想要的 Mac 行为。

### 将 AppKit 限定在局部边界

使用 `NSViewRepresentable`、`NSViewControllerRepresentable` 或专用于某项缺失桌面功能的 `NSWindow` 辅助工具，但选择状态和应用状态仍以 SwiftUI 为唯一可信来源。

### 独立于本地构建结果验证签名和公证

本地成功启动并不能证明应用已完成签名或已做好公证准备。保留 Xcode 手动归档流程，以便执行一次性发布检查；添加脚本化归档和公证流程，以便进行可重复的分发；如果任务涉及发布而不仅是本地迭代，请运行 `codesign` 和 `plutil` 检查。
