<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/github-code-reviews -->

## 使用方法

首先，将 Codex 代码审查添加到您的 GitHub 组织或代码仓库。
如需了解详情，请参阅 [GitHub 中的 Codex 代码审查](/zh-Hans/codex/third-party/github)。

您可以设置 Codex 自动审查每个 Pull Request，也可以在 Pull Request 评论中使用 `@codex review` 请求审查。

如果 Codex 标记出回归或潜在问题，您可以在 Pull Request 中发表评论，并使用后续提示让它修复问题，例如 `@codex fix it`。

这将启动一个新的云端聊天，用于修复该问题并更新 Pull Request。

## 制定审查指南

若要自定义 Codex 的审查内容，请将 `## Code Review Rules` 部分添加到距离这些规则所适用的代码最近的
`AGENTS.md` 中。例如：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

将适用于整个代码仓库的规则放在根目录下的 `AGENTS.md` 中，并将针对特定服务的规则
放在子目录中的文件里。规则应保持简洁，说明要标记的行为以及任何
安全处理方式或例外情况，并将格式检查和 lint 检查交给 CI。请参阅
[自定义 Codex 的审查内容](/zh-Hans/codex/third-party/github#customize-what-codex-reviews)
以了解设置方法和规则编写指南。
