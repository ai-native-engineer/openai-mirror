<!-- source: https://learn.chatgpt.com/zh-Hans/docs/third-party/slack -->

在 Slack 中使用 Codex，从频道和话题串发起编程任务。提及 `@Codex` 并附上提示词，Codex 会创建云端聊天并回复结果。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## 设置 Slack 应用

1. 设置 [Codex 云端聊天](/zh-Hans/codex/cloud)。您需要 Plus、Pro、Business、Enterprise 或 Edu 套餐（请参阅 [ChatGPT 定价](https://chatgpt.com/pricing)）、一个已连接的 GitHub 账户以及至少一个[环境](/zh-Hans/codex/environments/cloud-environment)。
2. 前往 [Codex 设置](https://chatgpt.com/codex/settings/connectors)，为您的工作空间安装 Slack 应用。根据您的 Slack 工作空间政策，安装可能需要管理员审批。
3. 将 `@Codex` 添加到频道。如果尚未添加，Slack 会在您提及时提示您添加。

<a id="start-a-task"></a>

## 开始聊天

1. 在频道或话题串中提及 `@Codex`，并附上您的提示词。Codex 可以参考话题串中之前的消息，因此您通常不必重述上下文。
2. （可选）在提示词中指定环境或代码仓库，例如：`@Codex fix the above in openai/codex`。
3. 等待 Codex 添加表情回应（👀）并回复聊天链接。任务完成后，Codex 会发布结果，并根据您的设置在话题串中发布答案。

### Codex 如何选择环境和代码仓库

- Codex 会检查您有权访问的环境，并选择与您的请求最匹配的环境。如果请求不明确，则会改用您最近使用的环境。
- 聊天会基于该环境的代码仓库映射中列出的第一个代码仓库的默认分支运行。如果您需要使用其他默认代码仓库或添加更多代码仓库，请在 Codex 中更新代码仓库映射。
- 如果没有可用的合适环境或代码仓库，Codex 会在 Slack 中回复并说明如何解决问题；请按说明解决问题后重试。

### 企业数据控制

默认情况下，Codex 会在话题串中回复答案，其中可能包含其运行环境中的信息。
为防止这种情况，企业管理员可以在 [ChatGPT 工作空间设置](https://chatgpt.com/admin/settings)中取消选中 **允许 Codex Slack 应用在任务完成时发布答案** 。管理员关闭答案发布后，Codex 只会回复聊天链接。

### 数据使用、隐私与安全

当您提及 `@Codex` 时，Codex 会接收您的消息和话题串历史记录，以理解您的请求并创建聊天。
数据处理遵循 OpenAI 的[隐私政策](https://openai.com/privacy)、[使用条款](https://openai.com/terms/)及其他适用的[政策](https://openai.com/policies)。
如需进一步了解安全信息，请参阅 Codex 的[安全文档](/zh-Hans/codex/agent-approvals-security)。

Codex 使用的大语言模型可能会出错。请务必审查答案和代码差异。

### 使用技巧与故障排除

- **缺少连接**：如果 Codex 无法确认您的 Slack 或 GitHub 连接，它会回复一个用于重新连接的链接。
- **环境选择不符合预期**：请在话题串中回复您要使用的环境（例如：`Please run this in openai/openai (applied)`），然后再次提及 `@Codex`。
- **较长或复杂的话题串**：请在最新消息中总结关键细节，以免 Codex 遗漏话题串前文中的上下文。
- **在工作空间中发布**：部分企业工作空间会限制发布最终答案。在这种情况下，请打开聊天链接查看进度和结果。
- **更多帮助**：请参阅 [OpenAI 帮助中心](https://help.openai.com/)。
