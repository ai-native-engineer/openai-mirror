<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/admin-plugin -->

通过本指南，您可以了解管理插件如何支持常见管理工作，为任务做好准备，并在具备所需审批和上下文的情况下，尝试主要使用场景的提示。

## 1. 了解管理插件的用途

管理插件旨在帮助您直接在 ChatGPT Work 中管理设置、权限和控制项。您用日常语言描述目标，插件便会收集所需信息、读取当前状态、解释发现的情况，并引导您执行下一步受支持的操作。

### 管理插件旨在解决的问题

- 将管理请求转化为清晰的工作流程，无需您编写 API 请求。
- 在做出决策或批准更改之前，审查工作空间的当前状态。
- 展示回答所依据的已授权数据源和字段，并说明无法验证的内容。
- 在执行受支持的更改前暂停，等待审查；更改后再次读取记录以确认结果。

该插件在后台使用选定的管理 API 和经批准的已连接数据源。它不会整合所有管理系统、扩大您的权限，也不会让您在 ChatGPT 中执行所有 API 操作。数据所属的系统仍然决定插件可以读取或更改哪些内容。

### 管理 API 旨在解决的问题

管理 API 为软件提供了一种结构化方式，用于请求数据或执行受支持的操作。组织可以使用管理 API 构建内部流程或外部工具。常见示例包括定期报告、对多条记录执行重复操作，以及连接经批准的系统。这些工作流通常需要经过工程、安全和治理审查。

使用本指南无需构建 API 工作流程。本指南的其余部分围绕管理插件展开。ChatGPT 工作空间管理与 OpenAI API 平台管理仍然相互独立，各有相应的权限和身份验证要求。

### 保护凭据隐私

仅使用您组织批准的连接和机密存储系统。切勿将真实的管理 API 密钥粘贴到 ChatGPT、Codex、文档或源文件中。

## 2. 做好使用管理插件的准备

如果您希望用日常语言处理受支持的一次性任务，可以使用管理插件。请描述目标，并提供稳定 ID 或经批准的报告上下文。插件会先展示发现的情况或计划进行的更改，再由您决定是否继续。

插件仅使用针对该任务获得授权的数据源、凭据和操作。它不会整合所有管理系统，也不会扩大您的权限。仍应以原系统中的信息为准。

### 开始之前

1. 找到记录所在的管理区域。
2. 收集所需信息并取得必要的审批。
3. 先提出只读请求。
4. 询问插件使用了哪些数据源和字段，以及哪些内容无法验证。
5. 对于受支持的更改，请先审查计划，再决定是否批准。之后，请插件再次读取记录并确认结果。

确认您的工作空间中可以使用该插件，且您具备所需权限。下方的角色和访问权限使用场景反映了插件当前文档所述的能力范围。插件可以审查角色、功能权限以及用户或群组的角色分配情况。经您确认后，它还可以将现有角色分配给现有群组。

插件无法创建角色、更改角色权限，也无法确认对特定连接器的访问权限。

分析类使用场景需要访问已连接且经批准的数据源。ROI 分析还需要获准使用的业务或工程成果数据；仅有使用记录并不足够。

## 3. 探索管理插件的主要使用场景

选择一个使用场景，将各个占位符替换为已批准请求中的值，然后按顺序执行步骤。除非任务是已获批准且受支持的更改，否则请先提出只读请求。

### 列出工作空间角色

**可尝试的提示**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**步骤**

1. **准备：** 确认工作空间 ID，以及您是否有权查看这些信息。
2. **执行：** 请求以只读方式获取角色列表。
3. **审查：** 检查角色类型、功能访问权限和角色分配情况。
4. **验证：** 在不做更改的情况下调查任何异常情况。

### 审查单个角色

**可尝试的提示**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**步骤**

1. **准备：** 确认角色 ID 和工作空间。
2. **执行：** 请求以只读方式审查角色。
3. **审查：** 检查权限和角色分配情况是否符合该角色的预期用途。
4. **验证：** 记下需要向角色负责人询问的问题。请记住，插件无法创建该角色或编辑其权限。

### 了解用户或群组的访问权限

**可尝试的提示**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**步骤**

1. **准备：** 使用用户或群组的稳定 ID。
2. **执行：** 请插件解释访问权限。
3. **审查：** 检查分配了哪些角色，以及这些角色提供哪些访问权限。记录任何重叠或缺失的权限。
4. **验证：** 如果插件无法查看某些内容，请将其标记为未知，不要猜测。

### 将现有角色分配给群组

**可尝试的提示**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**步骤**

1. **准备：** 确认群组和角色 ID。核对已批准的请求及记录中的审批人。
2. **执行：** 请插件展示当前角色以及将要进行的更改。
3. **审查：** 仅在计划与已批准的请求一致时才予以批准。
4. **验证：** 分配完成后，再次检查群组，确认已按批准的内容添加现有角色。

### 检查连接器通用权限

**可尝试的提示**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**步骤**

1. **准备：** 确认用户 ID，以及您是否有权审查该用户的访问权限。
2. **执行：** 请求检查通用权限。
3. **审查：** 核对已分配的角色，以及回答所依据的权限。
4. **验证：** 仅将此结果用于一般性检查。它不能证明用户有权访问特定连接器或已连接的内容。

### 排查已获批变更的问题

**可尝试的提示**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**步骤**

1. **准备：** 确认已获批的变更记录和预期结果。
2. **执行：** 让插件将请求与工作空间的当前状态进行对比。
3. **审查：** 检查工作空间和角色，然后核实记录的所有者。
4. **验证：** 在决定下一步操作前，以工作空间的当前状态为准。

### 优化成本和模型组合

**可尝试的提示**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**步骤**

1. **准备：** 确认工作空间和日期范围，并确认成本数据涵盖整个期间。检查有哪些获准使用的性能或成效字段可用。
2. **执行：** 请求对比成本和模型。
3. **审查：** 将数据反映的情况与假设、缺失的输入信息及需要权衡的因素区分开。
4. **验证：** 采取行动前，与财务团队和工作流程负责人核实可能节省的成本。

### 了解用量和采用情况

**可尝试的提示**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**步骤**

1. **准备：** 核对工作空间、日期范围和团队映射关系。确保用户级别的报告已获批。
2. **执行：** 请求分析用量和采用情况。
3. **审查：** 检查所请求的字段中有哪些可用。对于缺失的活动数据，予以排除，不要猜测。
4. **验证：** 用量高并不能证明用户采用了高级用法，也不能证明业务价值或个人绩效。

### 衡量业务价值和 ROI

**可尝试的提示**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**步骤**

1. **准备：** 核对工作空间和日期范围，然后确认获准使用的成效数据。审查计算公式和隐私规则。
2. **执行：** 请求进行 ROI 分析。
3. **审查：** 逐一检查所有来源和假设，记录每项局限或缺失的输入信息。
4. **验证：** 仅凭用量无法证明 ROI 或因果关系。与财务团队和业务负责人一同审查结果。

### 评估 Codex ROI

**可尝试的提示**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**步骤**

1. **准备：** 确认工作空间和报告周期。审查团队映射、代码仓库映射和获准使用的基线数据。
2. **执行：** 请求进行 Codex ROI 分析。
3. **审查：** 将观察到的规律与假设区分开。保护用户和代码仓库数据。
4. **验证：** 与工程团队一同审查建议和成效基线。

## 4. 何时可以考虑使用 API 工作流程

一些组织会使用这些 API 构建自己的管理流程或外部工具。这种方式可以支持定时或持续开展的工作，也有助于处理涉及大量记录或需要连接获准使用的内部系统的流程。这种方式独立于管理插件提供的引导式体验。

先明确一项管理任务：确定所需的输入和权限、审查环节、预期结果，以及结果的记录方式。如果您的组织要将其自动化，请让相关工程、安全和治理团队参与，将凭据存放在获准使用的机密存储系统中，并在部署前测试工作流程。

### 相关资源

- [ChatGPT 工作空间管理 API 参考](https://chatgpt.com/public/admin/api-reference)
- [管理边界](/zh-Hans/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [ChatGPT 工作空间分析 API](/zh-Hans/codex/enterprise/analytics-api)
- [ChatGPT 工作空间合规 API](/zh-Hans/codex/enterprise/compliance-api)
