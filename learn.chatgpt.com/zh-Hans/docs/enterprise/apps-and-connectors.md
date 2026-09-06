<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/apps-and-connectors -->

插件将可复用的工作流打包在一起，并可包含技能和连接
其他工具的应用。ChatGPT 和 Codex 在受支持的界面上
使用同一个公开插件目录，而管理员决定哪些插件在其工作空间中可用。
详细了解[插件](/zh-Hans/codex/plugins)、
[技能](/zh-Hans/codex/skills-and-plugins)和
[应用与连接器](https://help.openai.com/en/articles/11487775)。

只有当成员所属角色可以使用相应插件和应用，且该成员有权访问
所连接的服务时，该成员才能使用由连接器提供的能力。

插件可用于网页版、桌面版和移动版 ChatGPT 中的聊天与 Work，
也可用于 ChatGPT 桌面应用中的 Codex，还可通过 Codex CLI 插件浏览器使用。
插件在 IDE 扩展中不可用。

若要了解这些控制如何与工作空间角色和权限配合使用，请参阅
[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)。

## 了解能力控制链

一个插件可能涉及以下控制层级：

| 层级                   | 决定的内容                                                           | 管理位置                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 可用性            | 用户能否使用该插件包                           | 受支持的网页和桌面界面：[工作空间设置](https://chatgpt.com/admin/settings)；CLI：CLI 插件浏览器 |
| 包含的技能         | 已安装的插件提供哪些可复用指令                 | 插件包和[技能控制](/zh-Hans/codex/enterprise/skills)                                                               |
| 应用访问权限              | 用户能否使用由连接器提供的能力                          | [工作空间应用](https://chatgpt.com/admin/ca)和[权限与角色](https://chatgpt.com/admin/settings)                    |
| 操作和权限 | 用户可以执行哪些操作，以及 ChatGPT 在哪些情况下会先询问用户再使用连接器 | [工作空间应用](https://chatgpt.com/admin/ca)中的连接器操作控制和 App 权限                            |
| 服务授权   | 通过身份验证的主体可以访问哪些外部数据、执行哪些操作        | 已连接的服务及其身份提供商                                                                                 |
| 运行时权限     | 智能体获取数据或工具后可以执行哪些操作                        | 当前使用界面的运行时、沙盒和审批控制                                                              |

分两步落实这些控制层级：先让合适的插件可供使用，
再配置每个工作流程所需的能力和权限。

## 第 1 步：使插件可供使用

对于受支持的网页和桌面界面，工作空间插件控制决定
哪些角色可以使用或安装插件。Codex CLI 使用自带的插件浏览器
安装插件。请参阅
[构建插件](https://developers.openai.com/plugins/build/plugins)，了解
打包和分发方式。

若要从 GitHub 导入工作空间插件并使其保持最新，请参阅
[插件管理](/zh-Hans/codex/enterprise/plugin-management)。

### 导出公开目录以供审查

符合条件的 ChatGPT Enterprise 工作空间所有者和管理员可以下载一份 CSV 文件，
其中列出了其工作空间可用的公开插件。在更改插件可用性之前，
请使用导出的文件审查插件、应用和技能的元数据。

1. 打开[管理 \> 插件](https://chatgpt.com/admin/plugins)。
2. 选择 **公开**。
3. 选择页面顶部的下载图标（**导出 CSV**）。

下载文件名为 `public-plugins-security-review.csv`，其中包含：

- 插件元数据：`Plugin Name`、`Plugin Description`、`Date Added (UTC)`、
`OpenAI Verified`、`Developer Name` 和 `Version`。
- 应用元数据：`App Name(s)` 和 `App Description(s)`。
- 聊天技能元数据：`Skill Name(s)` 和 `Skill Description(s)`。

当一个插件包含多个应用或技能时，相应的值以分号分隔。
导出内容基于最多滞后 48 小时的公开目录快照，
仅包含当前工作空间可见的公开插件，
不包含为该工作空间创建的插件。
此导出功能不适用于 FedRAMP 工作空间。

## 第 2 步：管理能力

  让应用或插件在 ChatGPT 中可用，并不会授予对已连接服务中文件、
记录或操作的访问权限。在排查问题或扩大访问范围前，
请检查成员的工作空间角色及已批准的操作设置。
然后确认已通过身份验证的账户或共享连接在该服务中
拥有预期权限。

ChatGPT 和 Codex 中的插件可以包含连接器，用于搜索、检索或同步外部系统的数据，
或对外部系统执行操作。插件可用性与授予各连接器的访问权限和操作权限
由不同的控制项分别管理。

请在
[工作空间应用](https://chatgpt.com/admin/ca)和
[权限与角色](https://chatgpt.com/admin/settings)中管理由连接器提供的能力。可用控制项
允许管理员：

- 启用应用或连接器，并按工作空间角色分配访问权限。
- 对于支持操作控制的连接器，可允许只读操作或已获批准的自定义操作集，
并配置工作空间处理新增操作的方式。
- 设置 App 权限，以确定 ChatGPT 在哪些情况下会先询问用户再使用应用。
- 确保访问仅限于各已连接服务和经身份验证的用户
授予的范围及权限。

有关当前可用性和操作流程，请参阅
[应用中的管理员控制、安全与合规](https://help.openai.com/en/articles/11509118)。

<a id="choose-a-starting-set-of-apps"></a>

## 有针对性地选择首批插件

优先选择能满足明确业务需求的插件。逐一决定是向所有人开放插件，
将其限定在特定角色或试点小组内，
还是要求进一步审查。

针对每项已连接的服务，记录业务负责人、允许访问的数据、已批准的
读取或写入操作、身份验证方式，以及支持或移除事宜的联系人。

在启用写入操作或发布新的服务集成能力之前，请核实其适用的角色范围，
并使用在已连接服务中仅拥有预期权限的账户
进行测试。

如需大范围推广，可从团队日常使用的类别入手，例如电子邮件、
日历以及文件或文档系统。请通过
[插件目录](https://chatgpt.com/apps)确认插件在受支持的 ChatGPT 和 Codex 界面上的当前可用性
及相关能力。

无论首批选择哪些插件，都应先从读取操作开始。在启用写入操作之前，
请明确插件负责人，审查连接器的权限范围及服务权限，
确认数据访问情况，并记录对外部系统的影响及
恢复方案。

## 了解数据流与安全

当 ChatGPT 使用插件中包含的应用或连接器时，会向已连接的服务发出请求，
并返回经过身份验证的用户在该服务中的权限
允许访问的数据或操作结果。

ChatGPT 通过以下两种方式处理已连接应用的数据：

- **未同步：** ChatGPT 临时处理来自聊天和深度研究的数据，
  但不会为其建立索引。
- **已同步：** ChatGPT 预先为选定的已连接内容建立索引。您可以在相应插件的页面上
  查看应用是否支持同步。

模式会改变 ChatGPT 为已连接内容建立索引的方式，但不会取代
常规的聊天保留控制。使用应用的 ChatGPT 对话仍可
通过合规 API 获取。

OpenAI 的应用指南说明了数据传输和存储时的加密、按用户授权、角色和操作控制，以及使用应用的对话所受的网络访问限制。指南还说明，Business、Enterprise 和 Edu 客户通过应用访问的信息不会用于模型训练。当请求到达已连接的服务时，该服务的权限范围、数据保留、数据驻留及其他政策同样适用。

有关最新的数据处理详情，请参阅[应用安全与合规](https://help.openai.com/en/articles/11509118)
和[支持同步的应用](https://help.openai.com/en/articles/10847137)。
对于在 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中
本地配置的 MCP 服务器，请参阅
[Codex MCP 配置](/zh-Hans/codex/extend/mcp)。

## 使用最新操作流程和参考资料

- [应用中的管理员控制、安全与合规](https://help.openai.com/en/articles/11509118)
- [ChatGPT 中的应用](https://help.openai.com/en/articles/11487775)
- [支持同步的应用](https://help.openai.com/en/articles/10847137)
- [管理工作空间设置](https://help.openai.com/en/articles/8411955)
- [插件](/zh-Hans/codex/plugins)
- [技能和插件](/zh-Hans/codex/skills-and-plugins)
- [构建插件](https://developers.openai.com/plugins/build/plugins)
- [管理员上线指南](/zh-Hans/codex/enterprise/admin-setup)
