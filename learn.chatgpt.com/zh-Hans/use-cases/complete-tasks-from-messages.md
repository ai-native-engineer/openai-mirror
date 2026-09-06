<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/complete-tasks-from-messages -->

## 简介

许多消息对话中都隐藏着待办事项：预订晚餐、安排后续沟通、调研可选方案、提交收据，或整理回复所需的信息。计算机使用功能可以读取对话、识别任务，并在相关应用中完成工作。

如果消息中包含具体请求，并且您希望 ChatGPT 不只是总结对话，还能完成后续工作，那么这种方式就很适合。

## 使用方法

1. 安装 [计算机使用插件](/zh-Hans/codex/computer-use)。
2. 请 ChatGPT 审查指定的消息对话或来自指定发件人的消息。
3. 告诉它要执行的操作，并说明它是否应在完成任何事项前暂停。
4. 说明是否要让它在原对话中起草回复。

例如：

- `@Computer Look at my messages from [person]. Check my availability, find 2 dinner options in Hayes Valley, and draft a reply in the same thread. Check in with me before completing booking.`

## 实用技巧

### 要求在执行不可逆操作前暂停

如果任务可能涉及转账、提交订单、确认预订或敲定日程，请让 ChatGPT 在执行最后一步前停下来征求您的确认。

### 确保相关应用已准备就绪

当您已登录相关应用且这些应用可用时，效果最佳。如果任务需要使用“地图”“日历”“备忘录”、预订网站或浏览器会话，请提前准备好这些应用、网站或会话。

### 请注意，对话会被标记为已读

当 ChatGPT 在“信息”中打开对话时，它会像普通用户一样查看对话。请将该对话视为已读。

## 后续建议

如果一项工作从消息开始并在其他地方完成，同样的模式也适用于 Slack、电子邮件等其他收件箱式界面。如果您经常使用这种工作流，请在 [自定义](/zh-Hans/codex/customization/overview) 中添加可复用的偏好或指令，让 ChatGPT 每次都以相同方式处理这类请求。

### 建议提示

**完成消息对话中的一项任务**
