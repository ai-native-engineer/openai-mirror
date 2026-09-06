<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/security-review -->

Codex Security 审查目前以研究预览版形式提供。
该功能面向 ChatGPT Enterprise、Business、Edu 和 Pro 客户开放；
不向 Plus 用户开放。在初始推广期内，Codex Security 审查
不消耗 ChatGPT 额度。可能会有使用限制。

Codex Security 审查是一项额外审查，适用于希望
特别关注 Pull Request 中安全问题的客户。

在特定安全风险方面，Codex Security 审查比 [代码
审查](/zh-Hans/codex/third-party/github) 更深入：它会分析
Pull Request 差异、相关代码仓库上下文，以及已配置的威胁模型
或安全指南。代码审查在常规审查中也能识别安全相关问题，
因此二者的发现有时可能重叠。

## 开始之前

要配置自动执行的 Codex Security 审查，您需要：

- 您的工作空间需有 Codex Security 审查研究预览版访问权限
- [Codex 云端](/zh-Hans/codex/cloud) 已完成设置并连接到 GitHub 代码仓库
- 对 GitHub 代码仓库拥有推送或管理员权限

现有的 Codex Security 扫描为可选项。

<a id="configure-security-review"></a>

## 配置 Codex Security 审查

1. 前往 [Codex 设置](https://chatgpt.com/codex/settings/code-review)。
2. 在 **代码仓库偏好设置** 中，选择哪些 Pull Request 接受 Codex
   Security 审查：
   - **遵循个人设置** 允许每位贡献者通过其个人
     Codex Security 审查设置主动启用该功能。
   - **审查所有 PR** 适用于代码仓库中的所有 Pull Request。
   - **审查团队 PR**（如可用）适用于由
     您的 ChatGPT 工作空间成员（而非 GitHub 团队成员）创建的 Pull Request。
3. 选择 Codex Security 审查的运行时机：
   - **创建 PR 时** 会在 Pull Request 创建时独立运行。
   - **每次推送** 会在推送新提交后独立运行。
   - **每次代码审查运行时** 需要启用代码审查，并会同时运行 Codex Security
     审查。

## 添加威胁模型上下文

您可以配置威胁模型，以便为 Codex 提供有关应用的
资产、信任边界、安全假设和代码仓库特有风险的上下文。
如果代码仓库已有 Codex Security 扫描配置，您可以使用
其中的威胁模型。否则，请提供已签入
代码仓库的威胁模型文件路径。如果您未指定来源，Codex 会为
每次审查重新生成威胁模型。

## 设置报告阈值

默认情况下，自动执行的 Codex Security 审查会报告严重性为 **高** 和 **严重**
的发现，而手动请求的审查会报告严重性为 **中**、**高** 和
**严重** 的发现。您可以分别更改自动审查和手动审查的
最低严重性级别，并添加基于路径的覆盖规则。

发布到 Pull Request 的发现会继承该 Pull Request 在 GitHub 上的
可见性。任何能查看该 Pull Request 的人都能查看这些发现，
包括公开代码仓库中的发现，以及工作空间外的贡献者所创建的
Pull Request 中的发现。对于 Pull Request 评论可能广泛可见的代码仓库，
请谨慎选择报告阈值。报告阈值决定 Codex 会向 GitHub 发布
哪些内容；完整的 Codex Security 审查报告仍保留在
Codex 中。

<a id="request-a-security-review"></a>

## 请求 Codex Security 审查

要手动请求 Codex Security 审查，请在 Pull Request 中添加以下评论：

`@codex security review`

审查运行期间，Codex 会添加表情回应，然后将符合您
手动报告阈值的发现直接发布到 Pull Request。打开关联的
Codex 任务，然后选择 **安全报告** 标签页以查看完整报告，
其中包括严重性、攻击路径、支持证据、验证结果和
修复指南。如果没有问题达到报告阈值，Codex 不会
将发现发布到 Pull Request。

## 相关文档

- [使用 Codex 审查 GitHub Pull Request](/zh-Hans/codex/third-party/github) 介绍了代码审查和 GitHub 集成。
- [Codex Security](/zh-Hans/codex/security) 提供产品概览。
- [Codex Security 云服务设置](/zh-Hans/codex/security/setup) 介绍了如何扫描代码仓库和审查发现。
- [改进威胁模型](/zh-Hans/codex/security/threat-model) 介绍了如何调整代码仓库上下文。
