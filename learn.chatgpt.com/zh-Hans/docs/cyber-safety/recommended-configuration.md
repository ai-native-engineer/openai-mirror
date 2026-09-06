<!-- source: https://learn.chatgpt.com/zh-Hans/docs/cyber-safety/recommended-configuration -->

适用于网络安全工作流程的安全控制措施取决于所用模型、模型可以执行的操作、可以访问的系统，以及相关数据的敏感程度。

对于大多数 Daybreak Blue 工作流，您所在组织现有的安全实践，例如访问控制、凭据保护和敏感操作审查，可能已经足够。

Daybreak Red 工作流、自主安全测试，以及涉及生产系统、敏感数据或外部工具的活动，可能需要更严格的安全防护措施。以下建议主要面向这些风险较高的场景。

  您有责任评估具体工作流程的风险，并
实施适当的安全控制措施。模型安全防护措施和
Trusted Access 无法取代您所在组织自身的安全、监控和
监督实践。

Trusted Access 管理经批准的模型访问权限，但不会配置您的环境，也不会强制执行获批系统和操作的范围限制。您的团队必须设置适当的隔离、权限、审查、监控和人工监督控制措施。应假设模型、其工具以及每个已连接的系统都可能遭到入侵，并据此配置环境，确保即使发生入侵，它们仍无法访问未经授权的系统、泄露凭据、禁用安全防护措施，或在工作结束后继续驻留。

## 隔离环境

在专用实验室或沙盒中开展进攻性安全工作。开始时不要开放不受限制的互联网访问，也不要允许访问敏感生产系统、企业网络、无关工作负载或主机管理接口。除非获批工作明确需要并授权，否则不得让模型接触机密和凭据、获得持久访问权限，或对系统进行持久性更改。

对于风险较高或防护措施有所减少的工作，每次尝试都应使用全新且严格隔离的环境。分别隔离计算资源、存储、网络和身份，并在结束后销毁该环境，不要重置或重复使用。

在开始风险较高的工作前，测试文件系统和网络边界。测试应涵盖每台可访问的主机、每个已连接的工具、受委派的智能体和下游服务。即使模型或审查者批准了某项操作，也要保持主机环境隔离。

## 定义并强制执行已批准的边界

在模型开始运行前，记录此次工作已获批的系统、工具、操作和时间限制。应包括：

- 获批的目标系统、主机和环境。
- 排除在外的系统，包括生产系统和无关基础设施。
- 获批的工具和已连接服务。
- 获批和禁止的操作。
- 获批的开始和结束时间，以及数据处理要求。
- 漏洞披露、补丁审批以及与维护者的协调。
- 停止条件，以及需要明确人工审批的操作。

将这些已批准的边界作为任务上下文提供给智能体。仅靠文档无法强制执行这些边界：在可行的情况下，采用独立的文件系统、网络、身份和工具控制措施，使未经授权的操作无法执行。

使用 Codex [权限配置方案](/zh-Hans/codex/permissions)建立最小权限边界。任务不需要进行更改时，请选择 `:read-only`；工作需要编辑工作空间时，请扩展 `:workspace`。例如：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

`network_proxy` 功能会强制执行获批的域名限制。如果未启用该功能，
`network.enabled = true` 会允许直接访问网络，而实验室允许列表
不会限制目标地址。网页搜索、应用、连接器、MCP 服务器、
浏览器活动和 Codex 云端分别采用独立的控制措施；请限制或关闭
已批准的工作流程不需要的每项功能。

将 `lab.example.com` 替换为获批目标。限定范围的文件系统扫描旨在避免搜索 Linux、WSL 和 Windows 上的整个工作空间；如果敏感文件位于更深层级，请增加扫描深度，或使用精确的拒绝访问路径。不要将权限配置方案与旧版 `sandbox_mode` 设置结合使用；请遵循[权限配置方案的配置指南](/zh-Hans/codex/permissions#define-and-select-a-profile)。

如果获批的实验室主机解析到私有地址，即使该主机位于允许列表中，Codex 默认也会阻止访问。只有在私有网络工作获得明确批准时，才可设置 `allow_local_binding = true`，并应严格限制目标允许列表的范围，查阅[本地和私有网络指南](/zh-Hans/codex/permissions#local-and-private-networks)。您也可以将获批的确切私有 IP 地址加入允许列表。

默认阻止对开放互联网和生产网络的访问。如果确需外部访问，请通过具有独立强制执行机制的网关或代理转发，并配置严格限定的允许列表、请求检查和日志记录。对于通过软件包管理器、Webhook、URL 获取服务、重定向、云 API 和已连接工具建立的间接连接，也应施加同样的限制。在运行前加载依赖项，或使用管理员批准的依赖项。

## 保护凭据和敏感数据

不要在提示、代码仓库、环境变量、共享文件系统或模型可访问的日志中存放可重复使用的 API 密钥、云端凭据、密码和服务账户 Token。需要身份验证时，请使用单独的凭据代理或网关，在不向模型暴露凭据的情况下，提供仅适用于确切目标和允许操作的短期凭据。

仅提供获批任务所需的数据。移除不必要的敏感信息，阻止访问云端元数据和凭据端点，并将模型生成的文件视为不受信任的内容。

网络安全工作流应避免使用 `:danger-full-access` 和 `--yolo`。完全访问权限会移除自动审查所依赖的可强制执行沙盒边界。采用托管配置的组织可以排除 `:danger-full-access` 和 `--yolo`、限制允许使用的审批策略，并通过[企业托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-automatic-review-policy)要求进行自动审查。

在为获批的安全模型启用 **完全访问权限** 前，ChatGPT 桌面应用会显示针对该模型的危险操作警告。该警告建议改用 **为我审批** ，并链接到[审查者策略配置](/zh-Hans/codex/sandboxing/auto-review#configuration)。此警告不会恢复沙盒边界，也不会覆盖组织策略。

防护机制可为受控的网络安全工作流程增加基于策略的审查，但无法取代环境隔离、最小权限、明确定义的边界、监控或人工监督。

## 审查 Codex 的敏感操作

[自动审查](/zh-Hans/codex/sandboxing/auto-review)会在拟议操作执行前，将符合条件的沙盒边界审批请求转交给单独的审查者。审查者会考虑拟议操作、限定范围的任务上下文和适用策略，然后允许或拒绝该请求。组织可以根据获批目标、禁止的操作和必须进行人工审查的条件定制该策略。

对于影响生产环境、外部系统、敏感数据、权限提升、持久访问或不可逆更改的操作，必须获得明确的人工审批。将嵌入网站、代码仓库、文档和工具输出中的指令视为不受信任的内容；这些指令不能扩大授权范围，也不能覆盖访问控制。

在 ChatGPT 桌面应用中选择获批的 Daybreak 模型时，如果您的账户可以使用 **为我审批** 模式，且组织策略允许，权限控件会自动切换到该模式。使用桌面应用的 `/model` 命令时也是如此。如果该模式不可用，当前权限模式将保持不变。选择模型绝不会覆盖通过托管配置实施的组织要求。

要运行自动审查，请确保以下三项控制措施均已到位：

1. 使用交互式审批策略，例如 `approval_policy = "on-request"`。
2. 设置 `approvals_reviewer = "auto_review"`。
3. 保留可强制执行的沙盒边界或权限配置方案边界。

发送到网络允许列表中目标的请求仍处于网络边界内，不会自动触发自动审查。即使敏感命令的目标位于允许列表中，如需审查该命令，请创建明确的[命令规则](/zh-Hans/codex/agent-configuration/rules)，并将其保存在 `~/.codex/rules/` 下：

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

添加规则后重启 Codex。配置 `approvals_reviewer = "auto_review"` 后，匹配的命令会在执行前交由审查者处理。为每条敏感命令添加相应的提示规则，或使用 `approval_mode = "prompt"` 配置单个[MCP 工具](/zh-Hans/codex/extend/mcp)。需要由人员做出决策的操作仍须获得明确的人工审批。

自动审查不会检查沙盒内已经允许的常规操作。使用 `approval_policy = "never"` 或完全访问权限时，敏感操作可能不会生成可供审查的审批请求。自动审查可能出错，也无法取代隔离、明确定义的边界、监控或明确的人工监督。

如需了解限定范围的策略和组织范围内的强制执行，请参阅[配置经授权的网络安全工作流程](/zh-Hans/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement)。

## 独立监控并在故障时默认拒绝

记录模型请求、工具调用、网络活动、凭据使用情况和与安全相关的更改。将日志和监控系统置于模型控制的环境之外。出现未经授权的目标、意外网络请求、凭据泄露、策略更改、日志缺失或试图绕过安全防护措施的情况时，应发出警报。

确保策略执行、凭据代理、审查系统和紧急关闭控制机制独立于智能体。如果关键控制措施或监控系统发生故障，请停止工作流程。

## 为自定义智能体工作流添加防护机制

如果您使用 Responses API、Agents SDK 或其他执行框架进行构建，请在工具执行边界添加审查。执行前，根据已批准的系统、操作和时间限制检查拟议的敏感操作；将有歧义或高风险的操作交由人员处理；强制执行独立的文件系统和网络限制；保留审计日志；如果审查者或策略不可用，则默认拒绝执行。

Codex 自动审查不会自动保护自定义工具或外部执行框架。请参照[防护机制和人工审查](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)中的 Agents SDK 实现模式，并参考[开源审查者策略](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。

Codex 产品侧的沙盒机制和审查与[API 网络安全检查](/api/docs/guides/safety-checks/cybersecurity)相互独立。API 安全防护措施可能返回 `cyber_policy` 错误，而按用户分别设置的 `safety_identifier` 值有助于限制安全防护操作的影响范围。

## 清理并验证结果

工作结束后，撤销临时凭据、终止后台进程、移除持久访问权限，并销毁风险较高的环境。确认不存在残留的回调、暴露的产物、共享状态或跨运行访问，并确保不同用户、会话和评估彼此隔离。

在采取行动前验证发现结果，遵循协调披露实践，并确保相关人员对修复和更改负责。

## 开始之前

开始前，请确认已批准的系统和操作、适当的模型、隔离环境、最小权限、受限的网络访问、受保护的凭据、操作审查、独立监控、紧急停止机制和清理计划均已就绪。模型安全防护措施、隔离、限定范围的权限、操作审查、监控和人工监督相辅相成；其中任何一项都不应成为唯一的控制措施。
