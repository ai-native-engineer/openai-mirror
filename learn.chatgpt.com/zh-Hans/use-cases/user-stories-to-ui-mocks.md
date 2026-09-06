<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/user-stories-to-ui-mocks -->

## 简介

产品团队通常会从各种来源收集反馈，例如 Slack 讨论串、Linear 议题、Google Drive 文档或电子表格，以及客户通话笔记。有时，他们已有明确的用户故事来说明想要解决的问题；有时，相关上下文则存在于这些来源中。

ChatGPT 可以汇集这些上下文，并为能够解决该问题的功能生成 UI 设计稿。验证设计方向后，Codex 可以在产品中实现该功能。

## 建立视觉基准

如果您已有明确的用户故事，可以直接从它入手。否则，可以先与 ChatGPT 讨论，从不同来源收集上下文，并将这些信息整合成用户故事。

然后，您可以让 ChatGPT 使用图像生成功能制作几版不同方向的设计稿。这些设计稿应延续产品的信息架构，并遵循设计系统的约束。

如有帮助，您可以提供当前 UI 的屏幕截图或 Figma 文件作为参考。

请反复迭代，直到您对设计稿满意。改动范围界定得越明确，Codex 就越有可能生成可直接实现的设计稿。

## 从设计稿到原型

使用您希望 Codex 实现的最终版设计稿图像。选择 Codex，开始新对话并重新附加该图像，而不要直接继续当前的 ChatGPT 对话。然后，让 Codex 实现该设计稿，将其转化为可运行的原型；如果您要构建 Web 应用，也可以使用 [Build Web Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)：
