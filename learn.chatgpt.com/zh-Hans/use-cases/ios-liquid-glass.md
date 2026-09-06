<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/ios-liquid-glass -->

## 从 iOS 26 基线开始

首先，将 Liquid Glass 视为一项 iOS 26 和 Xcode 26 迁移项目。使用 iOS 26 SDK 重新构建应用，查看标准 SwiftUI 控件能自动呈现哪些效果，然后再让 Codex 重新设计那些看起来仍然过于扁平、厚重或与系统界面元素脱节的自定义部分。

如果应用仍支持较早的 iOS 版本，请从一开始就明确这项约束。 [Build iOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps) 中的 SwiftUI Liquid Glass 技能应使用 `#available(iOS 26, *)` 为新的 Liquid Glass 专用 API 添加可用性判断，同时保留一条在较旧设备上仍具备良好可读性的回退路径。

## 善用 iOS 插件

如果您希望 Codex 将 SwiftUI UI 变更与基于模拟器的验证结合起来，请使用 [Build iOS Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-ios-apps)。对于 Liquid Glass 迁移，有效的做法是让 Codex 审查一个流程、迁移少量界面区域、在 iOS 26 模拟器上启动迁移后的应用并截取屏幕截图，之后再扩大范围。

该插件内置 SwiftUI Liquid Glass 技能，其中有一组简单的默认原则值得写入您的提示：

- 相比自定义模糊视图，应优先采用原生的 `glassEffect`、`GlassEffectContainer`、玻璃效果按钮样式和 `glassEffectID` 过渡。
- 请在布局和视觉修饰符之后应用 `.glassEffect(...)`，这样材质就会包裹您实际想要的最终形状。
- 当多个界面区域同时出现时，请将相关玻璃元素包裹在 `GlassEffectContainer` 中。
- 仅在真正响应触控的按钮、标签块和控件上使用 `.interactive()`。
- 在整个功能中保持边角形状、着色和间距一致，不要混用仅针对个别位置的玻璃效果样式。
- 为 iOS 26 之前的部署目标保留非玻璃效果回退方案。

如需进一步了解如何安装插件和技能，请参阅我们的 [插件](/zh-Hans/codex/plugins) 和 [技能](/zh-Hans/codex/build-skills) 文档。

## 观看 WWDC 讲座

在让 Codex 重构实际的生产流程之前，以下 WWDC25 讲座是一组很好的参考资料：

- [认识 Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/)
- [了解全新设计系统](https://developer.apple.com/videos/play/wwdc2025/356/)
- [使用全新设计构建 SwiftUI 应用](https://developer.apple.com/videos/play/wwdc2025/323/)
- [使用全新设计构建 UIKit 应用](https://developer.apple.com/videos/play/wwdc2025/284/)
- [SwiftUI 新功能](https://developer.apple.com/videos/play/wwdc2025/256/)

## 先让 Codex 制定迁移方案，再完成一小部分迁移

当 Codex 将“玻璃效果应出现在哪里？”与“现在就编写所有代码”分开处理时，Liquid Glass 迁移会更顺利。先让 Codex 快速审查，再让智能体实现一个可独立完成的迁移部分，并通过模拟器进行验证。

## 实用技巧

### 不要处处使用玻璃效果

Liquid Glass 应在内容上方形成清晰的控件层，而不是把每张卡片都变成发光面板。让 Codex 移除与系统材质冲突的装饰性背景，在最需要保证可读性的区域保留普通内容样式，并仅将着色用于语义强调或主要操作。

### 从一个高频流程开始

标签页根视图、详情屏幕、工作表、搜索界面或新手引导流程，通常比一次性迁移整个应用更适合作为首个迁移目标。这样既更易于审查，也能明确哪些 Liquid Glass 设计决策应转化为可复用的组件模式。

### 有针对性地审查回退行为

如果您的部署目标低于 iOS 26，请让 Codex 同时展示回退实现和 Liquid Glass 版本。此审查步骤可发现意外引入的 API 可用性回归，并避免发布只能在最新模拟器上运行的迁移版本。
