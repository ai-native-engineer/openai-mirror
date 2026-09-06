<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/groups-and-provisioning -->

群组用于组织 ChatGPT 工作空间中的人员，并可关联自定义角色。群组成员身份不能替代席位分配，本身不会授予工作空间功能权限，也不会覆盖本地运行时策略或提供对 Platform API 或已连接系统的访问权限。

如需了解完整的控制模型，请参阅
[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)。

## 比较成员来源

为具有共同访问需求的人员使用群组，例如试点用户、工作空间运营人员，或需要使用相同受支持功能的成员。

### 为共同的访问需求创建群组

工作空间所有者和管理员可以创建和管理群组。对于人数较少或临时组建的用户群，请创建手动管理的群组；如果成员名单需要与您的目录保持一致，请从您的身份提供商同步现有群组。

每个群组都有一个权威成员来源：

| 群组类型                | 成员来源                   | 适用情形                                                                  |
| ------------------------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| 手动管理          | ChatGPT 工作空间管理    | 群组规模较小、属于临时群组，或未通过目录同步进行管理             |
| 由身份提供商管理 | 您的身份提供商（通过 SCIM） | 需要根据组织目录和成员移除流程管理成员 |

手动管理的群组与由身份提供商管理的群组可以共存。对于同步的群组，身份提供商是成员来源；后续预配更新可能会覆盖工作空间端的更改。有关 SCIM 当前的行为、支持的属性和设置步骤，请以帮助中心为准。

## 了解访问权限边界

群组成员身份本身并不会授予工作空间功能权限。

### 为群组关联适当的权限

工作空间所有者可以将自定义角色分配给群组，或在支持的情况下直接
分配给成员。请检查所有适用的角色：只要任一角色中某项权限明确设为 **关闭** ，
即使其他角色授予该权限，该权限也会被拒绝。成员仍受席位类型
和产品使用资格的约束。

SCIM 负责预配工作空间成员身份并进行群组分配。它不会授予 GitHub、Google Drive、Slack 或其他已连接系统中的权限，也不能替代本地运行时要求或 Platform API 组织访问权限。

工作空间 RBAC 和本地运行时要求属于相互独立的控制系统。
群组可能与两者都相关，但请勿根据工作空间中的群组顺序推断托管要求的匹配规则
或优先级规则。请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)，了解文档中说明的
配置下发规则和本地优先级规则。

## 按照当前流程进行设置

工作空间管理的具体细节可能会发生变化。请参考以下资源，了解当前的界面操作步骤、可用性和限制：

- [管理成员、席位类型、角色和访问权限](https://help.openai.com/en/articles/8266401-managing-members-seat-types-roles-and-access-in-chatgpt-enterprise)
- [管理群组](https://help.openai.com/en/articles/9083985-group-permissions-in-gpts)
- [SCIM 集成常见问题](https://help.openai.com/en/articles/10011769-openai-platform-scim-integration-faq)
- [管理工作空间设置](https://help.openai.com/en/articles/8411955)

### 核验新加入、发生变动和离开的成员

- **新加入的成员：** 确认该成员已接受所有待处理的工作空间邀请，
  并获得预期的席位、群组成员身份、权限
  和受支持的功能。
- **发生变动的成员：** 更新权威成员来源，并
  核验该成员在所有适用角色下的实际生效权限。
- **离开的成员：** 通过身份提供商撤销受 SCIM 管理的成员的访问权限，
  并确认该成员无法再访问工作空间。
  如果您仅从工作空间中移除该成员，后续同步可能会恢复其
  访问权限。

## 相关文档

- [用户生命周期管理](/zh-Hans/codex/enterprise/user-lifecycle)
- [身份验证](/zh-Hans/codex/auth)
- [角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)
- [托管配置](/zh-Hans/codex/enterprise/managed-configuration)
- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
