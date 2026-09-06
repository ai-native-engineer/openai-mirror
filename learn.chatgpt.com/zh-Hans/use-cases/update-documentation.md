<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/update-documentation -->

## 简介

要让文档保持最新，最简单的做法是在源代码发生变更时同步更新，而不是等到几周后。Codex 可以检查有变更的代码、测试、发行说明、关联议题和 Pull Request 上下文，然后根据现有结构起草范围明确的文档更新。

此工作流适用于开发者文档、README 更新、更新日志草稿、迁移说明、运行手册，或其他任何需要跟踪频繁变化行为的内容。

## 使用方法

1. 从需要在文档中说明的变更入手。

   提供相关的分支、Pull Request、提交、议题或文件。如果文档会公开发布，请明确说明不得包含未发布的路线图、客户私密信息和仅限内部使用的上下文。

2. 让 Codex 梳理并确定受影响的文档。

   在起草前，让 Codex 在现有文档中搜索功能名称、配置键、命令、示例和相关术语。

3. 将文档更新控制在必要的最小范围内。

   Codex 应保留当前的页面结构、术语、交叉链接和 frontmatter。如果有针对性地更新一条说明、一个示例或一个章节就足够，则应避免大范围改写。

4. 验证变更。

   让 Codex 运行适合该代码仓库的格式检查和文档检查，然后总结每项面向用户的声明所依据的证据。

## 向 Codex 提供什么

| 来源                               | 作用                                                               |
| ------------------------------------ | -------------------------------------------------------------------------- |
| 发生变更的代码和测试               | 让 Codex 能够分析实际行为，从而起草有针对性的文档更新。 |
| 公开的发行说明或产品文档 | 帮助 Codex 与公开资料中的术语、可用范围和功能状态保持一致。    |
| Pull Request 或议题上下文        | 说明变更的原因，以及哪些面向用户的行为很重要。   |
| 本地文档检查                    | 在文档发布前，为 Codex 提供明确的完成标准。   |

补充公开发行说明等上下文，可帮助 Codex 避免在文档中包含私密信息或尚未公开的更新。

## 让工作流可重复执行

若要为整个代码仓库制定统一约定，请将文档相关要求添加到 [AGENTS.md](/zh-Hans/codex/agent-configuration/agents-md)。例如：

```md
## Documentation

- When user-facing behavior changes, check whether docs, examples, or changelogs need updates.
- Public docs must only include public information or behavior visible in this repo.
- Preserve existing terminology and frontmatter.
- Run the docs formatting and build checks before final handoff.

如果该流程包含更多步骤，请将其转化为一项 [技能](/zh-Hans/codex/build-skills)，让今后的 Codex 任务可以遵循相同的来源检查、起草和验证循环。有关此模式的更多详情，请参阅 [将工作流保存为技能](/zh-Hans/codex/use-cases/reusable-codex-skills)。

您还可以 [从当前聊天中为此工作流创建计划任务](/zh-Hans/codex/automations#schedule-a-task-inside-a-chat)。例如，让 Codex 每周获取近期的 GitHub Pull Request，并让文档保持最新：
