<!-- source: https://learn.chatgpt.com/zh-Hans/docs/customization/overview -->

通过自定义，您可以让 Codex 按照团队的工作方式开展工作。

在 Codex 中，自定义由几个协同工作的层组成：

- **项目指南（`AGENTS.md`）**，用于提供长期有效的指令
- **[记忆](/zh-Hans/codex/customization/memories)**，用于保留从以往工作中获得的实用上下文
- **技能**，用于提供可复用的工作流和领域专业知识
- **[MCP](/zh-Hans/codex/extend/mcp)**，用于访问外部工具和共享系统
- **[子智能体](/zh-Hans/codex/agent-configuration/subagents)**，用于将工作委派给专门的子智能体

这些功能相辅相成，并不冲突。`AGENTS.md` 用于塑造行为，记忆
会延续本地上下文，技能可将可重复的流程封装起来，而
[MCP](/zh-Hans/codex/extend/mcp) 会将 Codex 连接到本地工作空间之外的系统。

## AGENTS 指南

`AGENTS.md` 可为 Codex 提供长期有效的项目指南。该指南会随您的代码仓库一同分发，并在智能体开始工作前生效。请保持内容精简。

将它用于您希望 Codex 每次在代码仓库中都遵循的规则，例如：

- 构建和测试命令
- 审查要求
- 代码仓库特有的约定
- 特定目录的指令

如果智能体对您的代码库做出错误假设，请在 `AGENTS.md` 中纠正这些假设，并要求智能体更新 `AGENTS.md`，让修正持续生效。将这一过程作为反馈循环。

**更新 `AGENTS.md`：** 一开始只添加必要的指令。将反复出现的审查反馈整理为明确规则，把指南放在最贴近其适用范围的目录中；当您纠正问题时，要求智能体更新 `AGENTS.md`，让后续会话继承该修正。

### 何时更新 `AGENTS.md`

- **重复出错**：如果智能体反复犯同一个错误，请添加一条规则。
- **读取内容过多**：如果智能体找到了正确的文件，却读取了过多文档，请添加路径指引（应优先读取哪些目录/文件）。
- **反复出现的 PR 反馈**：如果您多次留下相同反馈，请将其整理为明确规则。
- **在 GitHub 中**：在 Pull Request 评论中标记 `@codex` 并提出请求（例如 `@codex add this to AGENTS.md`），将更新任务委派给云端聊天。
- **自动执行漂移检查**：使用 [计划任务](/zh-Hans/codex/automations) 定期运行检查（例如每天一次），找出指南缺漏，并建议应向 `AGENTS.md` 添加哪些内容。

将 `AGENTS.md` 与能够强制执行这些规则的基础设施搭配使用：预提交钩子、代码检查工具和类型检查器能在您看到问题前发现它们，让系统更善于防止同类错误反复发生。

Codex 可以从多个位置加载指南：Codex 主目录中的全局文件（供您作为开发者使用），以及可由团队检入的代码仓库专用文件。文件越接近工作目录，优先级越高。
使用全局文件来设定 Codex 与您沟通的方式（例如审查风格、详细程度和默认设置），并让代码仓库文件专注于团队和代码库规则。

[使用 AGENTS.md 设置自定义指令](/zh-Hans/codex/agent-configuration/agents-md)

## 技能

技能为 Codex 提供可复用的能力，以支持可重复的工作流。
技能通常最适合用来实现可复用的工作流，因为它们支持更丰富的指令、脚本和参考资料，同时还能跨任务复用。
技能会被载入，并对智能体可见（至少其元数据如此），因此 Codex 可以发现技能，并在未被明确调用时自动选择。这样无需一开始就让上下文变得臃肿，也能随时使用内容丰富的工作流。

使用技能文件夹在本地编写并迭代工作流。如果已有适用于该工作流的插件，
请先安装它，以复用经过验证的设置。当
您希望在多个团队间分发自己的工作流，或将其与
连接器捆绑时，请将其打包为 [插件](/zh-Hans/codex/build-plugins)。技能仍是
编写工作流时采用的格式；插件则是可安装的分发单元。

一项技能通常由一个 `SKILL.md` 文件组成，还可包含脚本、参考资料和资源。

技能目录可包含一个 `scripts/` 文件夹，其中存放 Codex 在工作流中调用的 CLI 脚本（例如，用于填充种子数据或运行验证）。当工作流需要外部系统（问题跟踪器、设计工具、文档服务器）时，请将技能与 [MCP](/zh-Hans/codex/extend/mcp) 配合使用。

`SKILL.md` 示例：

```md
---
name: commit
description: Stage and commit changes in semantic groups. Use when the user wants to commit, organize commits, or clean up a branch before pushing.
---

1. Do not run `git add .`. Stage files in logical groups by purpose.
2. Group into separate commits: feat → test → docs → refactor → chore.
3. Write concise commit messages that match the change scope.
4. Keep each commit focused and reviewable.

技能适用于：

- 可重复的工作流（发布步骤、审查流程、文档更新）
- 团队专属的专业知识
- 需要示例、参考资料或辅助脚本的操作流程

技能可以是全局的（位于您的用户目录中，供您作为开发者使用），也可以是代码仓库专用的（检入 `.agents/skills`，供您的团队使用）。如果工作流适用于某个项目，请将该项目的技能放入 `.agents/skills`；如果您希望技能可用于所有代码仓库，请将它放入用户目录。

| 层级  | 全局               | 代码仓库                                           |
| :----- | :------------------- | :--------------------------------------------- |
| AGENTS | `~/.codex/AGENTS.md` | 代码仓库根目录或嵌套目录中的 `AGENTS.md` |
| 技能 | `~/.agents/skills`   | 代码仓库中的 `.agents/skills`                       |

Codex 对技能采用渐进式披露：

- 首先加载用于发现技能的元数据（`name`、`description`）
- 只有选定某项技能后，才会加载 `SKILL.md`
- 仅在需要时读取参考资料或运行脚本

技能可以显式调用；当任务与技能描述匹配时，Codex 也可以自动选择技能。清晰的技能描述可以提高触发的可靠性。

[构建技能](/zh-Hans/codex/build-skills)

## MCP

MCP（模型上下文协议）是将 Codex 连接到外部工具和上下文提供方的标准方式。
它尤其适用于远程托管的系统，例如 Figma、Linear、GitHub，或团队所依赖的内部知识服务。

当 Codex 所需的能力位于本地代码仓库之外时，请使用 MCP；例如，这些能力可能来自问题跟踪器、设计工具、浏览器或共享文档系统。

可以这样理解：

- **主机**：Codex
- **客户端**：Codex 内部的 MCP 连接
- **服务器**：外部工具或上下文提供方

MCP 服务器可以提供：

- **工具**（操作）
- **资源**（可读取的数据）
- **提示**（可复用的提示模板）

这种划分有助于您厘清信任边界和能力边界。有些服务器主要提供上下文，另一些则提供强大的操作能力。

在实践中，MCP 与技能配合使用时往往最有用：

- 技能定义工作流，并指定要使用的 MCP 工具

[模型上下文协议](/zh-Hans/codex/extend/mcp)

## 子智能体

您可以创建角色各异的智能体，并通过提示让它们以不同方式使用工具。例如，一个智能体可以运行特定的测试命令并采用特定配置，另一个智能体则可配备 MCP 服务器，用于获取生产环境日志以进行调试。每个子智能体都会专注于自己的任务，并使用适合该任务的工具。

[子智能体](/zh-Hans/codex/agent-configuration/subagents)

## 技能与 MCP 结合使用

将技能与 MCP 结合起来，就能让各个部分协同运作：技能定义可重复执行的工作流，MCP 则将其连接到外部工具和系统。
如果某项技能依赖 MCP，请在 `agents/openai.yaml` 中声明该依赖项，以便 Codex 自动完成安装和连接配置（请参阅 [构建技能](/zh-Hans/codex/build-skills)）。

## 下一步

按以下顺序构建：

1. [使用 AGENTS.md 设置自定义指令](/zh-Hans/codex/agent-configuration/agents-md) 可让 Codex 遵循您的代码仓库约定。添加预提交钩子和代码检查工具，以强制执行这些规则。
2. 如果已有可复用的工作流，请安装一个 [插件](/zh-Hans/codex/plugins)。否则，请创建一项 [技能](/zh-Hans/codex/build-skills)，并在需要共享时将其打包为插件。
3. [MCP](/zh-Hans/codex/extend/mcp) 适合在工作流需要外部系统（Linear、GitHub、文档服务器、设计工具）时使用。
4. [子智能体](/zh-Hans/codex/agent-configuration/subagents) 适合在您准备好将繁杂或专业性较强的任务委派给子智能体时使用。
