<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security -->

Codex Security 是一款应用安全智能体，可帮助安全和
工程团队查找、确认并修复漏洞。您可以在
Codex 中使用它，也可以通过您的终端或 TypeScript SDK 使用它，或将其用于已连接的 GitHub
代码仓库。

如需按明确步骤进行首次本地扫描，请从[Codex Security 插件
快速入门](/zh-Hans/codex/security/plugin)开始。

## 在桌面应用中使用 Codex Security

在 ChatGPT 桌面应用中，打开 ChatGPT 下拉菜单并选择 **Codex**。
安装并启用 Codex Security 插件，即可在侧边栏中打开 **安全** 。
安全工作台会将您的扫描、发现项和代码仓库
集中管理，同时 Codex 会将每次扫描作为一项任务运行。

- 使用 **扫描** 启动扫描、跟踪进度并审查已保存的结果。
- 使用 **发现项** 检查各项已完成扫描中的问题和证据。
- 使用 **代码仓库** 查看代码仓库历史记录和未解决的发现项。

请参阅[使用安全工作台](/zh-Hans/codex/security/plugin/workbench)，了解完整的桌面应用
工作流程。

### 探索插件使用场景

- 对代码仓库或单个指定的文件夹[运行安全扫描](/zh-Hans/codex/security/plugin/scans)。
- 如果您需要更大范围的审查，并且可以等待较长时间完成扫描，请[运行深度安全扫描](/zh-Hans/codex/security/plugin/deep-scans)。
- 在合并 Pull Request 或分支前，请[审查代码更改](/zh-Hans/codex/security/plugin/code-changes)。
- 当您需要审查现有安全发现项时，请[研判积压项](/zh-Hans/codex/security/plugin/triage-backlog)。
- [修复并验证发现项](/zh-Hans/codex/security/plugin/fix-findings)：使用范围受限的补丁处理已获批准的发现项。
- [导出或跟踪发现项](/zh-Hans/codex/security/plugin/export-findings)：将其导出为可移植构件，或发送到需经审批的跟踪目标。
- 根据提供的发现项、披露说明、源代码和 PoCs，[编写漏洞报告](/zh-Hans/codex/security/plugin/vulnerability-reports)。
- 根据扫描结果或其他安全证据[提出安全加固方案](/zh-Hans/codex/security/plugin/security-hardening)。
- 查看 Codex Security 插件的[最新动态](/zh-Hans/codex/security/plugin/changelog)。

  桌面安全工作台和 Codex CLI 均使用 Codex Security 插件。
  Codex Security 云服务通过 Codex 云端扫描已连接的 GitHub 代码仓库。
  有关 Codex 沙盒、审批、网络控制和管理员设置，请参阅
[智能体审批与安全](/zh-Hans/codex/agent-approvals-security)。

## Codex Security CLI 和 SDK

CLI 和 TypeScript SDK 均通过公开的
[`@openai/codex-security`](https://github.com/openai/codex-security) 软件包提供。
使用 `npx` 运行 CLI：

```bash
npx @openai/codex-security --help

运行扫描需要 Codex Security 访问权限。为获得最佳效果，请使用
已通过 [Trusted Access for Cyber](https://chatgpt.com/cyber) 验证的账户。

在不同代码仓库中持续使用与插件相同的扫描器。
CLI 可发现 GitHub 代码仓库、恢复批量扫描、跨扫描跟踪发现项，
并记录误报反馈。您可以添加自己的架构和安全策略，
设置预估费用上限，或在 CI 中及提交前运行检查。
使用 TypeScript SDK 将扫描、进度报告和费用控制功能
集成到应用或开发者工具中。

- [从 CLI 快速入门开始](/zh-Hans/codex/security/cli)，设置 CLI、
  对代码仓库进行预检并运行本地扫描。
- [运行批量安全扫描](/zh-Hans/codex/security/cli/bulk-scans)，发现 GitHub
  代码仓库，或根据 CSV 清单运行可恢复的扫描活动。
- [在 CI 中运行扫描](/zh-Hans/codex/security/cli/ci)，审查 Pull Request 更改、
  保留构件、上传 SARIF 并设置严重程度策略。
- [阅读 CLI 常见问题](/zh-Hans/codex/security/cli/faq)，查找有关扫描历史记录、
  误报反馈、覆盖范围和修复验证的答案。
- [查阅 CLI 参考资料](/zh-Hans/codex/security/cli/reference)，查看支持的
  命令、标志、输出格式、构件和退出代码。
- [集成 TypeScript SDK](/zh-Hans/codex/security/sdk)，通过代码选择目标、
  检查结果、跟踪进度并取消扫描。

## Codex Security 云服务

Codex Security 云服务目前处于研究预览阶段。
它会扫描已连接的 GitHub 代码仓库，查找可能存在的安全问题。

它可帮助团队：

1. **发现潜在漏洞** ：使用代码仓库专属的威胁模型和真实代码上下文。
2. **减少干扰** ：在您审查发现项之前对其进行验证。
3. **推动发现项得到修复** ：提供排序后的结果、证据和建议的补丁方案。

## Codex Security 云服务的工作原理

Codex Security 会逐个提交扫描已连接的代码仓库。
它会基于您的代码仓库构建扫描上下文，结合该上下文检查潜在漏洞，并在展示高置信度问题之前，先在隔离环境中进行验证。

您将获得侧重以下方面的工作流程：

- 代码仓库专属上下文，而非通用特征签名
- 有助于减少误报的验证证据
- 可在 GitHub 中审查的修复建议

## Codex Security 云服务的访问权限和先决条件

Codex Security 云服务通过 Codex 云端与已连接的 GitHub
代码仓库配合使用。如果某个代码仓库不可见，请确认该代码仓库在您的
Codex 云端工作空间中可用，或联系您的 OpenAI 客户团队。

## 相关文档

- [Codex Security 插件快速入门](/zh-Hans/codex/security/plugin)将引导您完成安装和首次本地扫描。
- [安全工作台](/zh-Hans/codex/security/plugin/workbench)介绍桌面应用中已保存的扫描、发现项、代码仓库和扫描活动。
- [Codex Security CLI 快速入门](/zh-Hans/codex/security/cli)将引导您完成设置、预检和首次终端扫描。
- [运行批量安全扫描](/zh-Hans/codex/security/cli/bulk-scans)介绍如何发现 GitHub 代码仓库，并说明 CSV 清单、扫描活动结果和恢复方式。
- [Codex Security CLI 常见问题](/zh-Hans/codex/security/cli/faq)解答有关扫描、发现项、覆盖范围和费用的常见问题。
- [Codex Security TypeScript SDK](/zh-Hans/codex/security/sdk)介绍如何从应用或开发者工具中运行扫描。
- [Codex Security 云服务设置](/zh-Hans/codex/security/setup)详细介绍设置、扫描和发现项审查。
- [安全审查](/zh-Hans/codex/security/security-review)介绍如何对 GitHub Pull Request 进行深入的安全审查。
- [改进威胁模型](/zh-Hans/codex/security/threat-model)介绍如何调整范围、入口点和关键程度假设。
- [Codex Security 云服务常见问题](/zh-Hans/codex/security/faq)涵盖云端产品的常见问题。
