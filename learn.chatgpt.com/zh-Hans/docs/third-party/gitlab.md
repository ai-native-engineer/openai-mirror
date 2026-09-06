<!-- source: https://learn.chatgpt.com/zh-Hans/docs/third-party/gitlab -->

使用 Codex 代码审查对 GitLab 合并请求额外进行一轮高价值审查。
Codex 会审查合并请求的代码差异，遵循您代码仓库中的指导规则，
并发布一份侧重严重问题的标准 GitLab 代码审查。

GitLab 支持目前处于 Beta 测试阶段，适用于所有 ChatGPT 套餐。
Codex 集成在 Codex 云端运行。桌面应用中类似 GitHub 的代码仓库操作，
例如 **创建 Pull Request**，不包含在本次 Beta 测试中。

## 开始之前

请确保已具备以下条件：

- 已连接的 GitLab 账户。使用 GitLab.com 时需完成
[标准连接流程](https://help.openai.com/articles/20001486)；
  自托管 GitLab 或 GitLab Dedicated 实例则需完成
[工作空间管理员模板设置](https://help.openai.com/articles/20001487)。
- 可准备一个 `AGENTS.md` 文件，以便让 Codex 遵循代码仓库专属的审查
  指南。

## 设置 Codex 代码审查

### 设置 GitLab 连接和 Codex 审查身份

对于 GitLab.com，请先在 ChatGPT 中
[连接 GitLab](https://help.openai.com/articles/20001486)，再在 Codex 中连接您的 GitLab 账户。
对于自托管 GitLab 或 GitLab Dedicated，每位审查者都应在
[工作空间管理员模板](https://help.openai.com/articles/20001487)
发布后完成连接。

对于自托管 GitLab 或 GitLab Dedicated，请打开 **Codex 云端** → **设置** →
[**连接器**](https://chatgpt.com/codex/cloud/settings/connectors)。
工作空间管理员可以让 Codex 创建服务账户，或保存现有服务账户的个人
访问令牌。

#### 让 Codex 创建账户

在 **Codex 云端** → **设置** → **连接器**中，选择您的
自托管 GitLab 或 GitLab Dedicated 主机所对应的应用 → 选择 **设置服务账户** →
**创建服务账户**。负责完成设置的工作空间管理员必须拥有
GitLab 实例的管理员权限。选择 **选定群组**
或 **仅限选定项目**，然后选择 Codex 应当运行的位置并创建
账户。群组选项会为每个选定群组授予 Developer 权限，
其项目和子群组会继承该权限；项目选项则仅向您选定的具体项目授予
Developer 权限。Codex 将创建
名为 ChatGPT Codex Connector 的实例服务账户，并为其生成具有
`api` 作用域的个人访问令牌。

#### 使用现有账户

在 GitLab 中创建或选择一个服务账户，并仅在 Codex 应当运行的群组或
项目中为其授予 Developer 权限。在 **服务
账户** 页面中，选择该账户 → **管理访问令牌** → **添加新
令牌** ，以
[创建个人访问令牌](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account)。
该令牌须具有 `api` 作用域，且至少在 30 天后到期。返回
Codex，选择 **使用现有服务账户**，粘贴令牌，然后选择
**保存令牌**。令牌保存时会被加密，之后不会再次显示。

#### 管理服务账户令牌

工作空间管理员可以在 **Codex 云端** →
**设置** → **连接器**中管理服务账户。对于由 Codex 创建的账户，管理员可以撤销
当前令牌并生成新令牌。对于现有账户，管理员可以
替换或移除保存在 Codex 中的令牌，并在需要时单独在 GitLab 中将其
撤销。在配置有效令牌之前，Codex 无法响应 GitLab
活动。

### 选择将 GitLab 活动传送给 Codex 的方式

#### 为编程任务或项目专属设置创建项目环境

在 **Codex 云端** → **设置** → **环境**中选择 GitLab 项目，
并在需要 Codex 为该项目编写或执行代码时创建项目环境，
例如编辑文件、提交更改，或将更新推送到
合并请求分支；如果审查依赖项目专属的密钥、
网络访问或设置命令，也需要创建项目环境。

对于 GitLab.com，启用 Codex 审查也需要项目环境。

创建环境时，启用 **允许来自 GitLab 的 Codex 活动**，
以安装项目 webhook，将合并请求、评论和议题
事件传送给 Codex。创建项目 webhook 需要具备 Maintainer 或 Owner
权限、管理员权限，或可管理项目
webhook 的自定义角色。已签名的项目和群组 webhook 要求使用 GitLab 19.0 或更高版本。在
自托管 GitLab 19.0 中，请确认 `webhook_signing_token` 功能标志
已启用；该标志默认启用，并已在 GitLab 19.1 中移除。

#### 为 GitLab 群组内的各项目启用 Codex 审查活动

对于自托管 GitLab 或 GitLab Dedicated，工作空间管理员可以打开 **环境**
→ **GitLab 活动** → **管理群组** ，为整个群组
及其子群组启用 Codex 审查。Codex 将安装覆盖该群组内
所有项目的群组 webhook。已连接的 GitLab 用户必须是该群组的 Owner，而且
群组 webhook 要求使用 GitLab Premium 或 Ultimate，以及 GitLab 19.0 或更高版本。

群组活动可启用代码审查，但不会创建项目环境。
要运行由 GitLab 触发的编程任务，例如编辑文件、运行命令、
提交更改或将更新推送到合并请求，
请创建项目环境。

### 配置代码审查策略

在
[Codex 审查设置](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab)中配置代码审查策略。
选择代码仓库策略：`Review my MRs`、`Review team MRs`、
`Review all MRs` 或 `Follow personal`。然后选择审查运行时机： **MR 打开时**、
**每次推送时**或 **智能触发（实验性）**。代码仓库设置可以
覆盖个人默认设置。

## 请求 Codex 审查

1. 在合并请求评论中提及 `@codex review`。
2. 等待 Codex 作出回应（👀）并发布审查。

Codex 会像团队成员一样，在合并请求中发布 GitLab 讨论和备注。
默认情况下，手动请求的审查可以包含 P0、P1 和
P2 级问题，而自动审查侧重 P0 和 P1 级问题。

## 启用自动审查

若要自动审查符合条件的合并请求，请在 Codex 设置中启用 **自动
审查** ，选择 GitLab 代码仓库策略，并选择
触发条件： **MR 打开时**、 **每次推送时**或 **智能触发（实验性）**。
当合并请求事件符合相应策略和触发条件时，无需发布 `@codex review` 评论，
Codex 就会运行。

必须通过项目 webhook 或上级群组 webhook 启用 GitLab 活动。
对于自托管 GitLab 或 GitLab Dedicated，配置的服务账户还必须
具备向项目回写的权限。如果已配置项目环境，Codex 会使用该环境。
如果上级群组已启用活动，
下级项目将继承相应的覆盖范围。

## 自定义 Codex 的审查内容

Codex 会在您的代码仓库中查找 `AGENTS.md` 文件，并遵循适用的
代码审查规则。请在距离规则所约束代码最近的文件中添加 `## Code Review Rules`
章节。必要时，可以使用 `###` 标题对相关检查项进行
分组。

例如，实验报告服务可以防止曝光后的行为
改变对照队列：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

将适用于整个代码仓库的规则放在根目录的 `AGENTS.md` 中，将特定服务的规则
放在嵌套文件中，例如 `services/experiment_reporting/AGENTS.md`。Codex 会应用
根目录规则，以及适用于各个变更文件的更具体规则，因此不相关的
更改无需附带特定服务的上下文。

先编写两到三条简明规则，概括审查者经常需要说明的检查项。
实用的规则应做到：

- **重点关注影响重大的代码仓库特有行为。** 描述需要标记的
  兼容性约束、数据边界或不安全的副作用，并说明
  其重要性。
- **说明安全做法或例外情况。** 提供充分的上下文，让 Codex 能够区分
  真实问题与预期行为。
- **明确规则适用范围，并保持其长期有效。** 优先描述预期结果，而非可能发生变化的函数名称，
  并将指导规则放在其所约束代码附近。
- **将机械性检查留给 CI。** 不要将格式化、lint 以及其他
  确定性检查纳入审查规则。

发起一个具有代表性的合并请求，并使用 `@codex review` 请求审查。
根据发现的问题和收到的反馈完善规则，并缩小或移除
会产生干扰的指导规则。

代码审查规则用于指导 Codex，不能替代测试、分支保护或
必需的审批。

若需指定一次性的审查重点，请将其添加到合并请求评论中：

`@codex review for issues in the database migration`

## 处理审查发现的问题

要修复审查发现的问题，必须具备 **已配置的项目环境**；群组
活动本身只支持审查，无法运行编程任务。如果项目已配置
环境，您可以在同一合并请求中再发表一条评论，请 Codex
修复问题：

```md
@codex fix the P1 issue

Codex 会以合并请求为上下文开启[云端聊天](/zh-Hans/codex/cloud)，并且
在拥有相应权限时将修复推送回该分支。

## 向 Codex 分配其他任务

其他编程任务同样需要 **已配置的项目环境**；群组
活动本身仅支持审查。如果您在评论中提及 `@codex`，并附上
`review` 之外的任何内容，Codex 就会开启[云端聊天](/zh-Hans/codex/cloud)，并将
您的合并请求作为上下文。

```md
@codex fix the CI failures

## 排查代码审查问题

如果 Codex 没有回应或发布审查：

- 确认已选择正确的 GitLab 应用；如果使用项目专属设置，
请确认项目具有相应的 Codex 云端环境。
- 确认项目或其上级群组已启用活动。在 GitLab 中，查看
**Webhook** →
[**最近事件**](https://docs.gitlab.com/user/project/integrations/webhooks/)，
  并确认合并请求和备注事件投递成功。
- 对于自托管 GitLab 或 GitLab Dedicated，请确认项目或群组 webhook
  已签名、已启用 SSL 验证，并且实例使用 GitLab 19.0 或
  更高版本。对于自托管 GitLab 19.0，请确认 `webhook_signing_token` 功能
  标志已启用；修复发生故障后被自动禁用的钩子。
- 对于自托管 GitLab 或 GitLab Dedicated，请确认现有服务账户的
  个人访问令牌有效，并具有 `api` 作用域。如果服务账户由 Codex
  创建，请确认已在
[Codex 连接器设置](https://chatgpt.com/codex/cloud/settings/connectors)中正确配置该账户，
  且相应项目或群组已启用。
- 对于自托管 GitLab 或 GitLab Dedicated，请确认工作空间服务账户
（而不只是已连接的 GitLab 用户）对项目或上级群组具有 Developer 权限，
以便 Codex 发布审查和表情回应。成员资格可以继承；
活动与服务账户访问权限相互独立。
- 确认已启用 **代码审查** 或 **自动审查** ，并且该 MR 符合
  代码仓库策略和触发条件。
- 使用 `@codex review`。
