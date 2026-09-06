<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/admin-setup -->

使用本指南规划 ChatGPT Enterprise 上线，涵盖以下管理边界：

- 工作空间访问权限。
- ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中适用功能的本地运行时策略。
- Codex 云端。
- 平台 API 访问权限。
- 插件和连接器访问权限。
- 已连接系统中的权限。

首次上线时，请按顺序完成这些步骤；若只需调整一个管理边界，请参阅相应的链接页面。

在工作空间设置中， **本地 Codex 和 Work** 将 Codex 和 Work 的本地访问权限
合并到 **允许成员在本地使用 Codex 和 Work**控制项下。部分工作空间
则提供独立的 **本地 Codex** 和 **本地 Work** 部分。在
这种布局中， **允许成员在本地使用 Codex** 控制 Codex，而 **在本地
使用 Work** 控制 Work。启用其中一项不会启用另一项。
这些标签表示工作空间权限，并非独立的产品或客户端。
Token 权限和凭据有效期限制位于 **访问
Token** 部分或本地访问部分，具体取决于工作空间。
托管配置是独立的策略层，可对这些客户端中适用功能的
受支持运行时行为施加限制。当行为或可用性存在差异时，本指南会
明确指出具体适用端。

请先查看
[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)中的权威对应表。
有关当前 ChatGPT 工作空间的操作流程，请参阅帮助中心指南；有关本地和托管运行时行为，
请参阅本文链接的开发者文档。

<a id="enterprise-grade-security-and-privacy"></a>

有关企业安全、隐私和运行时保护，请参阅
[智能体审批与安全](/zh-Hans/codex/agent-approvals-security)以及
[Codex 安全白皮书](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)。

<a id="pre-requisites-determine-owners-and-rollout-strategy"></a>

## 第 1 步：指定负责人并选择上线方案

为上线工作的每个部分指定负责人：

- **工作空间访问权限：** 成员资格、席位、角色及
  受支持的工作空间功能。
- **本地运行时策略：** 审批、权限配置方案、文件系统和
  网络访问权限，以及受支持的本地客户端的其他要求。
- **Codex 云端：** 托管环境、代码仓库连接和
  云端运行时策略。
- **已连接系统：** 提供商端的应用安装、账户和
  权限。
- **报告与合规：** 分析访问权限、审计导出和
  下游数据处理。

确定各类用户群体需要的是 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中适用的本地功能、Codex 云端，还是其中的组合。当工作流使用 API 密钥进行身份验证时，应将平台 API 访问权限视为独立的组织和项目边界。

## 第 2 步：配置工作空间访问权限和身份

使用 ChatGPT 工作空间成员资格、席位、群组和受支持的 RBAC 权限，向目标用户群体开放受支持的工作空间功能。请根据当前工作空间指南核实本地客户端和 Codex 云端访问权限，不要假定同一个角色可以控制所有使用端。内置管理角色应仅授予实际管理工作空间的人员。

工作空间控制项和标签会随时间变化。请参阅以下资料，了解当前操作流程：

- [管理成员、席位类型、角色和访问权限](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [配置基于角色的访问控制](https://help.openai.com/en/articles/11750701-rbac)
- [管理工作空间设置](https://help.openai.com/en/articles/8411955)
- [群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)
- [用户生命周期管理](/zh-Hans/codex/enterprise/user-lifecycle)
- [身份验证](/zh-Hans/codex/auth)

扩大上线范围之前，请让一名具有代表性的成员测试登录和功能访问权限。工作空间访问权限不会授予已连接服务中的代码仓库、文件或操作的访问权限。

## 第 3 步：配置本地运行时要求

当用户在 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中发起受支持的
本地运行时，本地要求会约束运行时行为。请通过受支持的云端、设备或系统渠道分发
`requirements.toml`。请将此策略与 ChatGPT 工作空间的
角色和群组分开管理。

请为受支持的本地客户端使用权限配置方案，不要再围绕旧版沙盒模式限制设计新的部署。例如：

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true

要在受支持的浏览器端和桌面端功能界面中全面禁用计算机使用，请限制该体验涉及的每个公开功能键：

```toml
[features]
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
computer_use = false

有关权威配置键列表、分发行为、优先顺序和更多
示例，请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)和
[`requirements.toml` 参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)。

<a id="team-config"></a>
<a id="step-4-standardize-local-configuration-with-team-config"></a>

## 第 4 步：标准化代码仓库配置

使用代码仓库级配置共享项目默认设置、规则和
技能，无需为每位用户重复设置。请按照相应功能文档指定的位置，将配置提交到
`.codex` 或 `.agents` 中：

| 类型          | 来源                                           | 用途                                                  |
| ------------- | ------------------------------------------------ | ---------------------------------------------------------- |
| 配置 | [基础配置](/zh-Hans/codex/config-file/config-basic) | 为受支持的本地客户端设置代码仓库默认值        |
| 规则         | [规则](/zh-Hans/codex/agent-configuration/rules)        | 控制在沙盒外运行时需要审批的命令 |
| 技能        | [构建技能](/zh-Hans/codex/build-skills)              | 让受支持的客户端可以使用代码仓库工作流   |

代码仓库配置可以提供默认设置和可复用的工作流，但无法授予工作空间、模型、平台 API 或已连接系统的访问权限。

## 第 5 步：配置 Codex 云端

Codex 云端使用托管环境和已连接的源代码仓库。请规划每个管理边界：

1. 通过受支持的工作空间控制项向目标用户群体授予 Codex 云端访问权限。
2. 安装并配置受支持的源系统集成。
3. 在源系统中，将各类用户群体的代码仓库访问范围限制为其所需的代码仓库。
4. 为这些代码仓库配置云端环境、机密信息和互联网访问权限。
5. 配置代码审查等可选的托管工作流。
6. 让一名具备预期工作空间和代码仓库权限的代表性用户进行测试。

Codex 云端遵循已连接源系统提供的
代码仓库权限和保护机制。工作空间访问权限不会绕过这些控制措施。请参阅
[云端环境](/zh-Hans/codex/environments/cloud-environment)、
[GitHub 集成](/zh-Hans/codex/third-party/github)和
[智能体审批与安全](/zh-Hans/codex/agent-approvals-security)，了解 Codex 云端的
设置和运行时指南。

## 第 6 步：配置插件和连接功能

请分别审查插件安装、随附技能、由连接器支持的功能、连接器操作和源系统授权，并独立做出决策。禁用由连接器支持的功能不一定会卸载插件或其随附技能。

将插件或技能纳入上线范围之前：

1. 确认其来源、责任人、目标用户群体和审查日期。
2. 审查随附的技能、连接器、MCP 服务器、钩子，以及每项功能所需的数据和操作。
3. 使用非敏感数据，仅授予其所需的最低访问权限进行测试。
4. 记录复审和停用工作的负责人。

插件可用于网页版、桌面版和移动版 ChatGPT 中的聊天和 Work，以及 ChatGPT 桌面应用中的 Codex，还可通过 Codex CLI 插件浏览器使用。
IDE 扩展中不提供插件。
ChatGPT 和 Codex 共用一个统一的公共插件目录；工作空间控制项决定成员可以访问其中的哪些插件。

有关完整的管控模型，请参阅[插件控制](/zh-Hans/codex/enterprise/apps-and-connectors)和
[技能控制](/zh-Hans/codex/enterprise/skills)。

## 第 7 步：设置治理和可观测性

根据您要解答的问题选择相应的报告方式：

<a id="analytics-api-setup-steps"></a>
<a id="compliance-api-setup-steps"></a>

- 使用[工作空间分析](/zh-Hans/codex/enterprise/workspace-analytics)，以交互方式
  查看 ChatGPT 工作空间分析和 Codex 分析。
- 使用[分析 API](/zh-Hans/codex/enterprise/analytics-api)，通过 Codex 分析 API
  以编程方式生成汇总报告。
- 使用[合规 API](/zh-Hans/codex/enterprise/compliance-api)获取审计和
  调查记录。
- 当因套餐而异的 Codex 活动消耗
  符合条件的 ChatGPT 工作空间额度时，
  请使用[ChatGPT 使用限制和支出控制](/zh-Hans/codex/enterprise/usage-limits)。

请查阅需要身份验证才能访问的 API 参考文档，了解当前的访问要求、模式、字段、数据保留规则和请求行为。不要依据本指南中的接口契约副本构建集成。

保护集成边界：

- 将 API 密钥和其他集成凭据存储在组织的机密管理系统中。
- 仅允许获批的用户群体访问下游系统和保留的数据。
- 根据导出的合规 API 记录的敏感程度以及组织的保留政策保护这些记录，并按照当前接口契约测试收集和删除工作流。

## 第 8 步：验证并维护部署

使用具有代表性的身份验证每个适用的管理边界：

- ChatGPT 工作空间成员资格、席位以及受支持的角色权限。
- ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中所涵盖的本地功能，包括登录和实际生效的运行时要求。
- Codex 云端访问权限、环境配置和代码仓库权限。
- 使用 API 密钥的工作流所需的平台 API 组织和项目访问权限。
- 插件安装、随附技能、连接器访问权限和受支持的操作。
- 已连接系统的授权和数据访问权限。
- 负责相关工作的管理员对分析和合规功能的访问权限。

记录每项控制措施的负责人和现行操作流程的来源。这份记录可帮助管理员在 UI 或策略发生变化时更新操作流程，而无需更改管理模型。

初始部署后，审查访问权限、已连接的功能、额度使用情况、支持反馈以及团队实际使用的工作流。当这些情况发生变化时，调整部署范围和管理员指南。
