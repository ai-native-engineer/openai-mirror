<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/native-ios-apps -->

## 搭建应用和构建循环

对于全新开发，先直接使用提示词。请 Codex 搭建一个入门级 iOS SwiftUI 应用，并编写一个可接入 `Build` 操作的小型构建和启动脚本；该操作位于 [本地环境](/zh-Hans/codex/environments/local-environment)。

保持构建循环以 CLI 为主。Apple 的 `xcodebuild` 可以列出方案，并从终端执行构建、测试、归档、`build-for-testing` 和 `test-without-building` 操作，让 Codex 留在智能体工作闭环中，而不必频繁切换至 Xcode GUI。

如果您想要更简洁的项目生成工具，并且能够接受第三方工具，那么 [Tuist](https://tuist.dev/) 是很好的下一步选择。它无需 GUI 即可生成和构建 Xcode 项目，同时仍可让 Codex 从终端构建并启动应用。

进入完整的 Xcode 项目并需要更深入的自动化时，请使用 [XcodeBuildMCP](https://www.xcodebuildmcp.com/)。当方案、目标、模拟器控制、屏幕截图、日志和 UI 交互变得非常重要，仅靠普通 Shell 命令已无法满足需求时，正适合使用它。

## 善用技能

首次实现时，通常不需要技能或 MCP 服务器。等任务需要专门能力，或您希望将更完善的 SwiftUI 规范融入执行过程时，再添加技能。

- [SwiftUI 专家](https://github.com/AvdLee/SwiftUI-Agent-Skill) 是一项优秀的通用 SwiftUI 技能，已内置许多最佳实践。
- [SwiftUI Pro](https://github.com/twostraws/SwiftUI-Agent-Skill/blob/main/swiftui-pro/SKILL.md) 是一项覆盖面广的 SwiftUI 审查技能，涵盖现代 API、可维护性、辅助功能和性能。

- [Liquid Glass 专家](https://github.com/Dimillian/Skills/blob/main/swiftui-liquid-glass/SKILL.md) 可帮助 Codex 采用新的 iOS 26 Liquid Glass API，并调整自定义组件，使其符合最新的系统设计。
- [SwiftUI 性能](https://github.com/Dimillian/Skills/blob/main/swiftui-performance-audit/SKILL.md) 适用于功能运行缓慢或 SwiftUI 视图更新路径可疑的情况。它会扫描常见的 SwiftUI 错误，并生成按优先级排列的报告，说明应修复哪些问题，以及哪些修复能带来最大收益。
- [Swift 并发专家](https://github.com/Dimillian/Skills/blob/main/swift-concurrency-expert/SKILL.md) 可在晦涩的错误和编译器警告开始阻碍您进行所需更改时提供帮助。使用 GPT-5.6 Terra 时，您可能不太需要它；但当 Swift 并发诊断信息过多且杂乱时，它仍然很有用。
- [SwiftUI 视图重构](https://github.com/Dimillian/Skills/blob/main/swiftui-view-refactor/SKILL.md) 有助于控制文件大小，并让整个代码仓库中的 SwiftUI 代码更加一致。
- [SwiftUI 模式](https://github.com/Dimillian/Skills/blob/main/swiftui-ui-patterns/SKILL.md) 可帮助您随着应用不断发展，采用可预测的 `@Observable` 和 `@Environment` 架构模式。

如需详细了解如何安装和使用技能，请参阅我们的 [技能文档](/zh-Hans/codex/build-skills)。

## 迭代

初版可用后，或者如果您从现有项目开始，就可以开始迭代 UI 或行为。

在这一步，请明确说明您希望更改什么，以及希望如何更改。

请在提示词中明确交代：Codex 处理的是全新代码仓库还是现有 Xcode 项目，必须继续支持哪些 iOS 设备或部署目标，以及您期望采用哪种验证循环。

### 提示词示例

例如，如果您想向现有应用添加功能，可以让 Codex 进行如下更改：

## 实用技巧

### 从基础开始

对于全新开发，先直接使用提示词。请 Codex 搭建一个入门级 SwiftUI 应用，并编写一个可接入 `Build` 操作的小型构建和启动脚本；该操作位于 [本地环境](/zh-Hans/codex/environments/local-environment)。首次实现时，通常不需要任何技能或 MCP 服务器。

### 使用精简且可靠的验证循环

每次更改后，让 Codex 运行范围最小、但确实能验证此次改动所涉及契约的命令。之后再扩展到更全面的构建。这样既能让 Codex 保持高效，又不会把每次编辑都当成必须完整构建应用。

### 让构建循环以 CLI 为先

让构建循环以 CLI 为先。Apple 的 `xcodebuild` 工具可以在终端中列出方案，并执行构建、测试、归档、`build-for-testing` 和 `test-without-building` 操作，让 Codex 留在智能体循环中，而不必来回切换到 Xcode 图形界面。

### 善用 XcodeBuildMCP

一旦您在完整的 Xcode 项目中工作并需要更深入的自动化，就应使用 XcodeBuildMCP。此时，您会需要处理方案、目标、模拟器控制、截图、日志和 UI 交互，单靠普通的 shell 命令已无法满足所有需求。
