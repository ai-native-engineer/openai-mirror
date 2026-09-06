<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/workspace-model-availability -->

用户可使用的模型取决于所用的产品界面和登录方式。您的 ChatGPT 工作空间中的模型设置不会自动应用于 ChatGPT 桌面应用中的 Codex、Codex CLI、IDE 扩展、Codex 云端或 OpenAI API。

如需了解完整的管理体系，请参阅
[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)。

## 明确模型访问权限的适用边界

| 产品或身份验证边界                                                         | 模型访问权限取决于                                                                                  | 当前信息来源                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 工作空间                                                                          | 工作空间套餐、成员访问权限、工作空间设置，以及受支持的角色权限                 | [ChatGPT Enterprise 和 ChatGPT Edu 的模型与限制](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| 通过 ChatGPT 登录使用的 ChatGPT 桌面应用中的 Codex、Codex CLI 和 IDE 扩展        | 相应客户端支持的模型，以及已登录的 ChatGPT 身份所拥有的访问权限    | [Codex 模型](/zh-Hans/codex/models)和当前适用的工作空间指南                                                                  |
| Codex 云端                                                                                | 托管式 Codex 工作流支持的模型，以及已登录的 ChatGPT 身份所拥有的访问权限 | [Codex 模型](/zh-Hans/codex/models)和 [Codex 云端](/zh-Hans/codex/cloud)                                                                 |
| 通过 API 密钥进行身份验证的 ChatGPT 桌面应用中的 Codex、Codex CLI 和 IDE 扩展 | 与该密钥关联的 OpenAI API 组织和项目                                       | [身份验证](/zh-Hans/codex/auth)和 [OpenAI API 平台](https://platform.openai.com/docs/overview)                        |

请查阅用户实际使用的产品界面所对应的当前信息来源。不要照搬模型目录，也不要假定 ChatGPT 模型选择器中的设置对 ChatGPT 桌面应用中的 Codex、Codex CLI、IDE 扩展、Codex 云端和 API 平台具有相同作用。

## 为员工设定明确的初始使用体验

邀请试点小组之前，请查看您工作空间的[模型设置](https://help.openai.com/en/articles/8411955)。
工作空间所有者和管理员可以
分别配置聊天的初始默认设置，以及 Work 和 Codex 的初始默认设置。
在支持这些设置的情况下，请为聊天、Work 和本地 Codex 界面选择初始模型、推理级别、速度
以及新建聊天时的行为。

这些选项只是默认设置，不代表访问权限。可用模型仍取决于成员的席位、角色、工作空间身份或 API 身份、强制执行的工作空间要求，以及实际使用的具体产品界面。初始默认设置不能授予不可用模型的访问权限，也不能覆盖上述要求。Codex 云端不支持更改默认模型。

快速模式的可用性取决于工作空间、产品界面，以及
[`requirements.toml`](/zh-Hans/codex/config-file/config-reference#requirementstoml) 中
强制执行的任何 `features.fast_mode` 设置。
该设置可以将托管的本地 Codex 客户端的快速模式固定为开启或关闭；
它不是初始默认设置，也不能覆盖工作空间或产品层面的可用性限制。

## 企业中的 GPT-6 Astra

在初始推出阶段，您的组织必须拥有 Daybreak 访问权限，
管理员才能启用 Astra。在发布后的前两周，
ChatGPT Enterprise 默认关闭 Astra。在符合条件的工作空间中，
管理员可以为用户或群组
启用聊天、Work 和 Codex 中的 Astra。现有的产品使用资格要求仍然适用。请检查您的
[工作空间模型设置](https://help.openai.com/en/articles/8411955)，并
确认试点小组使用的每个客户端上的模型可用性。

启用访问权限和选择初始模型是两个独立的决定。将 Astra 设为默认模型之前，请检查
适用的席位、角色和计费安排。
有关用量限额和计费的指导，请参阅[定价](/zh-Hans/codex/pricing)；
有关暂停以等待审查的任务，请参阅[安全监控](/zh-Hans/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)
中的说明。

使用 API 密钥登录时，Astra 的访问权限取决于与该密钥关联的 API 组织和项目。在 ChatGPT 工作空间中启用 Astra 不会授予 API 访问权限。使用 API 密钥进行抢先体验还需要配置客户端；请向您的 OpenAI 客户团队索取设置说明。仅选择模型或更改本地配置并不能获得访问权限。

## 为 GPT-5.4 退役做好准备

对于使用 ChatGPT 登录的用户，GPT-5.4 和 GPT-5.4 mini 将于 2026 年 8 月 31 日在 Codex 中退役。请在此之前更新受影响的工作空间默认设置、已保存的模型设置、托管配置、自定义智能体和计划任务：

- 将 `gpt-5.4` 替换为 `gpt-5.6-terra`（GPT-5.6 Terra）。
- 将 `gpt-5.4-mini` 替换为 `gpt-5.6-luna`（GPT-5.6 Luna）。

OpenAI API 和使用您自己的 API 密钥进行身份验证的 Codex 均不受影响。
请参阅 [Codex 模型](/zh-Hans/codex/models#deprecated-codex-models)和
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)，
了解迁移详情。

## 区分模型访问权限与运行时权限

模型访问权限决定已通过身份验证的用户能否在受支持的产品界面上使用某个模型。本地权限配置方案和托管要求决定本地运行启动后智能体能够执行哪些操作，例如可以更改哪些文件，或可以访问哪些网络目标。

权限配置方案无法授予模型访问权限。模型访问权限也无法削弱适用于运行过程的沙盒、审批策略、网络控制或源系统权限。

## 排查模型访问权限问题

如果用户无法选择预期的模型：

- 确认产品界面和登录方式。
- 确认 ChatGPT 工作空间，或 API 平台的组织和项目。
- 检查该身份验证边界当前适用的访问控制。
- 检查所选本地客户端或 Codex 云端是否支持该模型。

## 当前信息来源

- [ChatGPT Enterprise 和 ChatGPT Edu 的模型与限制](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [管理工作空间设置](https://help.openai.com/en/articles/8411955)
- [基于角色的访问控制](https://help.openai.com/en/articles/11750701-rbac)
- [Codex 模型](/zh-Hans/codex/models)
- [各套餐的 Codex 功能可用性](/zh-Hans/codex/pricing#feature-availability)
- [身份验证](/zh-Hans/codex/auth)

## 相关文档

- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
- [群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)
- [角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)
- [托管配置](/zh-Hans/codex/enterprise/managed-configuration)
