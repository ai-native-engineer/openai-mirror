<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/threat-model -->

了解什么是威胁模型，以及如何通过编辑威胁模型来优化 Codex Security 提供的建议。

## 什么是威胁模型

威胁模型是一份简短的安全摘要，用于说明您的代码仓库如何运作。在 Codex Security 中，您可将其作为 `project overview` 进行编辑，系统会将其用作扫描上下文，供后续扫描、优先级排序和审查使用。

Codex Security 会基于代码生成初稿。如果发现项与预期不符，首先要编辑的就是威胁模型。

一份实用的威胁模型会明确列出：

- 入口点和不受信任的输入
- 信任边界和身份验证方面的假设
- 敏感数据路径或特权操作
- 您的团队希望优先审查的区域

例如：

> 用于账户变更的公共 API。接受 JSON 请求和文件上传。使用内部身份验证服务核验身份，并通过内部服务写入计费变更。重点审查身份验证检查、上传解析和服务间信任边界。

这样能为 Codex Security 的后续扫描和发现项优先级排序提供更好的起点。

## 改进并重新审视威胁模型

如果您想改进结果，请先编辑威胁模型。当发现项未覆盖您关注的区域，或出现在意料之外的位置时，请调整威胁模型。对威胁模型的修改会改变后续扫描的上下文。

  有些用户会将当前威胁模型复制到 Codex 中，并通过聊天对其进行改进，
改进时侧重他们希望更仔细审查的区域，然后将更新后的
版本粘贴回 Web 界面。

### 在哪里编辑

要审查或更新威胁模型，请前往 [Codex Security 扫描](https://chatgpt.com/codex/security/scans)，打开代码仓库，然后点击 **编辑**。

## 相关文档

- [Codex Security 云服务设置](/zh-Hans/codex/security/setup) 涵盖代码仓库设置和发现项审查。
- [Codex Security](/zh-Hans/codex/security) 提供产品概览。
- [Codex Security 云端常见问题](/zh-Hans/codex/security/faq) 涵盖常见的云端问题。
