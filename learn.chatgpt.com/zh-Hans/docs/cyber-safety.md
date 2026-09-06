<!-- source: https://learn.chatgpt.com/zh-Hans/docs/cyber-safety -->

OpenAI Daybreak 帮助获批用户开展经授权的防御性网络安全工作。Daybreak Blue 提供旗舰模型的访问权限；这些模型在经授权的防御性工作流中拒绝请求的情况更少。Daybreak Red 提供经单独审批的专用网络安全模型访问权限，用于更高级的安全研究。

将您的获批模型与受控环境、针对获批系统和操作的明确限制、最小权限以及敏感操作执行前的自动审查机制配套使用。请仅通过获批的身份、工作空间或 API 组织及项目，以及产品端使用该模型。

## 选择合适的模型

对于大多数经授权的防御性工作，请优先使用 **GPT-Daybreak-Blue** 。此模型可让您使用高级能力，且在以下防御性安全工作流中拒绝请求的情况更少：

- 漏洞发现和分类处置。
- 代码安全审查和威胁建模。
- 检测工程和事件响应。
- 在受控环境中进行恶意软件分析。
- 修复和补丁验证。

**GPT-Daybreak-Red** 是一款专用网络安全模型，适用于经单独审批且获得明确授权的工作流，例如受控的漏洞复现、概念验证或漏洞利用验证、渗透测试、红队测试和复杂系统分析。它不是日常安全工作的默认选择，而且访问权限不会自动开通，也并非在所有产品端都可用。

在缺乏明确授权的情况下，这些高级工作流可能看起来像恶意活动。请仅将获批的模型和产品端用于您拥有或已获得明确评估授权的系统，并保持适当的人工监督。

例如：

- **GPT-Daybreak-Blue：** 审查获批的实验室代码仓库是否存在身份验证薄弱环节，根据证据和影响对发现的问题排序，并在不访问外部系统的情况下提出补丁方案。
- **GPT-Daybreak-Red：** 在获批的实验室环境和测试时段内，复现已记录的身份验证缺陷，验证一个最小概念验证方案，并在访问凭据、建立持久化机制或更改生产环境之前停止操作。

## Trusted Access for Cyber

通过 [Trusted Access for Cyber](https://help.openai.com/en/articles/20001258-trusted-access-for-cyber) 申请 **Daybreak 访问权限** 。访问权限取决于您的具体身份或服务、ChatGPT 工作空间或 API 组织及项目、获授权的产品方案和模型，以及允许使用的产品端是否已获批并完成开通配置。

- 个人可通过[个人 Trusted Access 申请表](https://chatgpt.com/cyber)申请访问权限。
- 组织可提交[企业 Trusted Access 申请表](https://openai.com/form/enterprise-trusted-access-for-cyber/)，并与其 OpenAI 代表协调。

提交申请或完成身份验证并不保证获批。

  申请访问权限、验证身份或获准使用 Daybreak Blue，
都不会让您获得 Daybreak Red 或 GPT-Daybreak-Red 的访问权限。
这一专用产品方案需要单独审批和开通配置。

使用企业访问权限时，请仅将获批的工作空间、API 组织或项目用于您所在组织经授权的内部工作。不得将该访问权限扩展至外部用户、第三方客户、面向外部提供的服务、下游产品功能或获批工作范围之外的系统。如果不确定获批的是哪个身份、工作空间、API 组织、项目、模型或产品端，请停止操作并向您的 OpenAI 代表确认。

Trusted Access 不会自动提供[零数据保留](/api/docs/guides/your-data#data-retention-controls-for-abuse-monitoring)。开始之前，请确认您所用的具体 API 组织及相应端点已单独获批的数据保留控制措施。

## 误报

正当的网络安全活动或与网络安全无关的活动仍可能触发安全防护机制。如果安全防护机制阻止、重新路由或限制请求，请检查可用的客户端通知和请求日志。请参阅[常见问题与故障排除](https://help.openai.com/en/articles/20001259)，了解需要收集的信息和后续步骤。如果 `/feedback` 可用，请通过它报告疑似 Codex 误报。有关 API 访问限制和申诉，请遵循 [API 网络安全检查指南](/api/docs/guides/safety-checks/cybersecurity#appeals)。

所有用户仍须遵守[使用政策](https://openai.com/policies/usage-policies/)和[使用条款](https://openai.com/policies/row-terms-of-use/)。

## 配置您的安全工作流程

Trusted Access 管理获批的模型访问权限，但不会配置您的环境、强制执行针对获批系统和操作的限制，也不会审查拟执行的操作。

- [使用推荐配置](/zh-Hans/codex/cyber-safety/recommended-configuration)，以实现隔离、落实最小权限、明确边界，并为敏感操作设置防护机制。
