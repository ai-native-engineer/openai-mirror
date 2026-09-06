<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/idea-to-proof-of-concept -->

## 从视觉方向入手

GPT Image 2 擅长生成高质量 UI 视觉稿。探索新想法时，您无需从零开始，可以利用图像生成来确定视觉方向。

可以通过两种方式做到这一点：

- 使用 ImageGen 技能反复调整视觉方向。对生成的 UI 方案满意后，您可以要求 Codex 构建与视觉稿一致的原型。在这种情况下，请选择 Codex，开始新对话，并附上您最终要实现的图像，而不是直接在 ChatGPT 对话中继续。Codex 能参考用户附件时，效果会更好。
- 使用插件时，您只需描述自己的想法：插件会为您生成视觉方向并处理后续步骤。

## 使用插件

如果您在开始实现前无需反复调整视觉方向，就可以使用插件并描述自己的想法。

使用 [Build Web Apps 插件](https://github.com/openai/plugins/tree/main/plugins/build-web-apps)
来构建 Web 应用、仪表板、创意网站和侧重前端的工具。其
工作流会引导 Codex 先生成设计，再用代码还原设计，并使用
浏览器将结果与概念方案进行比较。

请使用 [Game Studio 插件](https://github.com/openai/plugins/tree/main/plugins/game-studio)
来构建浏览器游戏的概念验证。该流程应在扩展游戏前明确玩家可执行的
动作、首个可玩循环、引擎、资源工作流、HUD、控制方式，并完成浏览器
测试。

## 迭代工作流

良好的概念验证应聚焦于可快速实现并由团队验证的 MVP。
如果您想确保 MVP 按预期运行，可以使用 Playwright interactive，让 Codex 验证其工作成果。

初版运行起来后，您可以在同一聊天中提出范围明确的更改要求，继续迭代：
