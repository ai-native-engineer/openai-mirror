<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/draft-prds-from-sources -->

## 简介

在着手开发新产品或功能之前，通常会先起草一份产品需求文档（PRD），以便就范围和需求达成一致。大多数情况下，编写这份 PRD 所需的背景信息已经存在于团队的内部系统中，例如 Linear 中的工单、Slack 中的讨论，以及 Notion 或 Google Drive 中的草稿等。ChatGPT 可以汇集这些背景信息并起草一份 PRD，供您审查和反复完善，同时让来源链路清晰可见。

## 选择资料来源

首先确定您希望 ChatGPT 使用的资料来源：Linear 项目、Slack 规划频道或讨论串，以及 PRD 中应引用的所有 Drive 文档、Notion 页面、会议记录或本地文件。
您还应明确列出期望 PRD 包含的章节，例如问题、用户、需求、UX、技术、发布计划、时间线或决策。

1. 当输出结果需要是真正的 DOCX 文件时，请先使用 `$documents`。
2. 直接注明资料来源：Linear 项目或里程碑、Slack 频道或讨论串，以及 ChatGPT 应引用的文档或笔记。
3. 向 ChatGPT 提供 PRD 章节规范。
4. 先审查来源附录，然后审查需求和待解决问题。
5. 在同一聊天中补齐缺漏、收敛范围并准备交接。

<a id="refine-in-the-same-chat"></a>
<a id="refine-in-the-same-task"></a>

## 在同一聊天中完善

使用本页的入门提示生成初稿。如果缺少某些内容，请让 ChatGPT 查阅缺失的资料来源，而不要从头开始。

## 检查来源链路

在分享 PRD 之前，请 ChatGPT 列出来源依据不足或缺失的论断、尚未解决的问题，以及 ChatGPT 视为已确认的决策。如果来源附录不能让您轻松核查这些内容，请继续在同一聊天中完善，然后再导出或发布任何内容。

### 建议提示

**检查来源链路**
