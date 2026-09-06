<!-- source: https://learn.chatgpt.com/zh-Hans/docs/sandboxing/auto-review -->

自动审查在沙盒边界使用单独的
审查智能体取代手动审批。Codex 主智能体仍在同一沙盒内运行，并采用
相同的审批策略以及相同的网络和文件系统限制。两者的
区别在于由谁审查符合条件的权限提升请求。

  自动审查仅适用于交互式审批。实际上，这
  意味着使用 `approval_policy = "on-request"`，或使用仍会
  显示相关提示类别的细粒度审批策略。使用 `approval_policy = "never"` 时，
  没有可供审查的请求。

在 ChatGPT 桌面 App 中，选择已获批准的 Daybreak 模型后，
会自动将权限控件切换为**替我审批**，前提是该
模式可用于您的账户且组织策略允许。
使用桌面 App 的 `/model` 命令时也同样如此。如果该模式
不可用，当前权限模式将保持不变。选择模型
绝不会覆盖组织的托管要求。

在为已获批准的安全模型启用**完全访问权限**前，
ChatGPT 桌面 App 会显示针对危险操作的模型专属警告。
该警告建议改用**替我审批**，并链接到
[审查策略配置](#configuration)。该警告不会恢复
沙盒边界，也不会覆盖组织策略。

## 自动审查的工作原理

总体流程如下：

1. 主智能体在 `read-only` 或 `workspace-write` 沙盒模式下运行。
2. 当需要越过沙盒边界时，它会请求审批。
3. 如果 `approvals_reviewer = "auto_review"`，Codex 会将该审批请求
   交给单独的审查智能体，而不是暂停并等待人工处理。
4. 审查智能体判断是否应执行该操作，并返回判断理由。
5. 如果操作获批，执行将继续。如果被拒绝，主
智能体会收到指令，要求其寻找明显更安全的路径，或停止并询问
用户。

自动审查只是更换审查智能体，并不授予权限。它不会扩展
`writable_roots`、启用网络访问权限或削弱对受保护路径的保护。它仅
改变 Codex 处理已需审批操作的方式。

## 触发条件

自动审查会评估原本需要暂停并等待人工处理的审批请求。
这些请求包括：

- 请求提升沙盒权限的 Shell 或 exec 工具调用。
- 被当前沙盒或策略阻止的网络请求。
- 对允许写入的根目录之外文件的编辑。
- 需要根据工具注解
或配置的审批模式进行审批的 MCP 或应用工具调用。
- 通过计算机使用访问新网站或域名。

自动审查不会对沙盒内已获允许的常规操作运行。
如果命令可以在当前 `sandbox_mode` 下运行，或工具调用
符合允许的策略，主智能体会继续执行，无需审查。

计算机使用是另一种情况。计算机使用的 App 审批仍会
直接向用户显示，因此自动审查不会取代这些 App 级提示。

## 自动审查会阻止哪些操作

总体而言，自动审查旨在阻止以下操作：

- 将私密数据、机密信息或凭据发送到不受信任的目的地
- 探查凭据、Token、Cookie 或会话材料
- 大范围或持续削弱安全性
- 具有重大不可逆损害风险的破坏性操作

具体策略位于开源 Codex 代码仓库中的以下文件：
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
和
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
企业可通过 `guardian_policy_config` 自定义该策略，个人用户则可
通过本地 [`[auto_review].policy`](/zh-Hans/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) 自定义。

## 审查智能体看到的内容

审查智能体本身也是 Codex 智能体，但任务范围比主智能体更窄：
判断是否应执行某项特定的越界操作。

审查智能体会看到精简的会话记录以及具体的审批请求。其中
通常包括用户消息、已显示的助手更新、相关工具
调用和工具输出，以及当前提交审批的操作。它
也可以执行只读检查来收集缺失的上下文，但很少这样做。

其中不包括隐藏的助手推理。自动审查看到的是保留的
聊天项和工具证据，而不是私密思维链。

## 拒绝和失败处理

明确拒绝不会被当作普通沙盒错误处理。Codex 会将
审查理由返回给主智能体，并附加一条更严格的指令：

- 不得通过变通方案、间接执行或规避策略
来达成同一结果。
- 只有找到明显更安全的替代方案时才能继续。
- 否则，停止并询问用户。

Codex 还会为每轮应用拒绝熔断器。在当前
开源实现中，自动审查会在连续拒绝 `3` 次，
或累计拒绝达到 `10` 次（基于同一轮内最近 `50`
次审查的滚动窗口）后中断该轮。

任何非拒绝结果都会重置连续拒绝计数器。触发熔断器时，
Codex 会发出警告，并通过中断来终止当前轮，
而不会让智能体循环尝试更多权限提升请求。

超时会与明确拒绝分开显示，并会告知主智能体：
仅凭超时不能证明该操作不安全。

对于被拒绝的操作，还有一条明确的覆盖路径。在当前
开源 TUI 中，运行 `/approve` 打开**自动审查拒绝记录**选择器，然后
选择一项最近被拒绝的操作，并批准对其重试一次。Codex 每项任务最多记录 10 项
最近的拒绝。该审批的范围严格受限：它仅适用于被拒绝的
具体操作，不适用于日后类似的操作；该审批记录仅供在
同一上下文中重试一次；重试仍需经过自动审查。在内部实现中，
Codex 会为该具体操作注入一个限定于开发者作用域的审批标记。
之后，审查智能体会将这项明确的用户覆盖视为上下文，但仍会遵循
策略；如果策略规定用户无权覆盖该类拒绝，它仍可再次
拒绝。

## 配置

有关设置详情，请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-automatic-review-policy)。

默认审查策略位于开源 Codex 代码仓库中：
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
企业可以在托管要求中使用
`guardian_policy_config` 替换其中的租户特定部分。个人用户也可设置
本地
[`[auto_review].policy`](/zh-Hans/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
，将其写入自己的 `config.toml` 中，但托管要求优先：

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

要自定义策略，请先完整复制默认策略文本，再
根据您自身的风险状况逐步调整。

## 配置经授权的网络安全活动

对于经授权的安全工作，应将自动审查与书面的
活动范围及遵循最小权限原则的[权限配置文件](/zh-Hans/codex/permissions)结合使用。
请使用已批准的实验室目标，记录操作和活动时间窗口，并
将生产系统、不相关的主机、凭据和持久性更改
排除在范围之外，除非已明确获得授权。

`[auto_review].policy` 和 `guardian_policy_config` 都会替换您当前的
审查策略。它们不会与模型附带的策略或
组织管理的策略合并。内置的审查指令和响应
格式仍然适用。使用任一示例前，请复制完整的当前
策略，保留所有现有规则，并添加适用于您已获批准工作的规则。
请将大写占位符替换为该完整策略。如果您无法
访问当前策略，请勿覆盖它。

以下本地 `config.toml` 模板会启用审查，并在现有审查策略后添加限定范围的
条件：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

请将示例目标和允许的操作替换为实际获批的范围。
请使用独立的文件系统和网络规则强制执行目标限制；
审查指令不能取代这些边界。

组织可以在托管的 `requirements.toml` 中强制执行相同条件：

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` 控制当前的权限配置文件。
`allowed_sandbox_modes` 还会在仍使用
旧版 `sandbox_mode` 的部署中阻止完全访问权限。

托管的 `guardian_policy_config` 优先于用户的本地
`[auto_review].policy`。请保留 `approval_policy = "on-request"` 或其他
符合条件的交互式审批策略，并维持可强制执行的沙盒边界。
使用 `approval_policy = "never"`、`:danger-full-access` 或 `--yolo` 时，操作
可以在不生成自动审查所需的越界审批请求的情况下执行。

列入允许列表的网络目标本身不会触发审查。请添加
显式的[命令规则](/zh-Hans/codex/agent-configuration/rules)并设置
`decision = "prompt"`，或将敏感 MCP 工具配置为需要审批，
以确保沙盒内必须接受审查的操作仍会交由审查智能体处理。

有关模型访问、活动设置和自定义智能体工作流，请参阅[模型和可信访问](/zh-Hans/codex/cyber-safety)与[推荐
配置](/zh-Hans/codex/cyber-safety/recommended-configuration)。
有关企业设置的优先级和支持的客户端版本，请参阅[托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-automatic-review-policy)。
对于自定义 API 或
Agents SDK 执行框架，请使用[防护措施和人工审查](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)。

## 在不削弱安全性的前提下减少审查量

自动审查在沙盒已涵盖您常用的安全
工作流时效果最佳。如果过多日常操作需要审查，应先修正边界设置，
而不是让审查智能体长期批准大量无谓的权限提升请求。

实际上，效果最显著的改进包括：

- 添加范围受限的
[`writable_roots`](/zh-Hans/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  ，用于您有意使用的临时目录或相邻代码仓库。
- 添加范围严格限定的[前缀规则](/zh-Hans/codex/agent-configuration/rules)。应优先使用精确的命令
  前缀（如 `["cargo", "test"]` 或 `["pnpm", "run", "lint"]`），而不是宽泛的
  模式（如 `["python"]` 或 `["curl"]`）。宽泛的规则往往会使
  自动审查本应守护的边界形同虚设。

自动审查会话记录默认保存在 `~/.codex/sessions` 下，
因此，您可以在更改
策略或权限前，让 Codex 分析其中的过往活动。

## 限制

自动审查可改善长时间运行的智能体任务在默认情况下的运行状态，
但并不能提供确定性的安全保障。

- 它只会评估请求跨越边界的操作。
- 它仍可能出错，尤其是在对抗性或非常规情境下。
- 它应作为良好沙盒设计、监控和
组织专属政策的补充，而不是取代这些措施。

有关研究依据和已发布的评测结果，请参阅
[对齐研究团队关于自动审查的文章](https://alignment.openai.com/auto-review/)。
