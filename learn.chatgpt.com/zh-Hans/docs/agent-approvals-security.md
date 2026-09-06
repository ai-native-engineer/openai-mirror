<!-- source: https://learn.chatgpt.com/zh-Hans/docs/agent-approvals-security -->

Codex 可帮助保护您的代码和数据，并降低滥用风险。

  本页介绍如何安全运行 Codex，包括沙盒、审批
  和网络访问。如果您想了解用于
  扫描已连接 GitHub 代码仓库的产品 Codex Security，请参阅 [Codex Security](/zh-Hans/codex/security)。

默认情况下，智能体在关闭网络访问的状态下运行。在本地，Codex 使用由操作系统强制执行的沙盒来限制可访问的范围（通常仅限当前工作空间），并通过审批策略决定何时必须在操作前暂停并向您请求审批。

如需大致了解 ChatGPT 桌面应用、
Codex CLI 和 IDE 扩展中的沙盒工作原理，请参阅[沙盒](/zh-Hans/codex/sandboxing)。
如需更全面地了解企业安全，请参阅 [Codex 安全白皮书](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)。

## 沙盒与审批

Codex 的安全控制由两层相互配合的机制构成：

- **沙盒模式**：Codex 执行模型生成的命令时，在技术上能够执行哪些操作，例如可写入哪些位置以及能否访问网络。
- **审批策略**：Codex 在执行哪些操作之前必须向您请求审批，例如离开沙盒、访问网络或运行不在受信任集合中的命令。

Codex 会根据运行位置使用不同的沙盒模式：

- **Codex 云端**：在由 OpenAI 管理的隔离容器中运行，无法访问您的主机系统或无关数据。它采用两阶段运行时模型：设置阶段先于智能体阶段运行，可以访问网络以安装指定的依赖项；随后，智能体阶段默认离线运行，除非您为该环境启用互联网访问。为云端环境配置的机密信息仅在设置阶段可用，并会在智能体阶段开始前移除。
- **Codex CLI / IDE 扩展**：由操作系统级机制强制执行沙盒策略。默认设置包括禁止网络访问，并将写入权限限制在当前工作空间内。您可以根据风险承受能力配置沙盒、审批策略和网络设置。

使用 `Auto` 预设时（例如 `--sandbox workspace-write --ask-for-approval on-request`），Codex 可以自动读取文件、进行编辑，并在工作目录中运行命令。

编辑工作空间之外的文件，或运行需要网络访问的命令时，Codex 会请求审批。如果您只想聊天或制定计划而不进行更改，请使用 `/permissions` 命令切换到 `read-only`（只读）模式。

对于声明会产生副作用的应用（连接器）工具调用，即使相关操作不是 Shell 命令或文件更改，Codex 也可以请求审批。如果应用/MCP 工具声明了破坏性标注，破坏性工具调用始终需要审批；但如果该工具同时声明了读取标注，则优先采用读取标注。

## 安全监控与暂停的任务

GPT-6 Astra 在 Codex 和 ChatGPT Work 中包含安全监控功能。监控异步运行，检测到模型可能存在不安全行为时，可以暂停任务。暂停可能在触发它的活动发生之后才生效；监控不能替代沙盒、权限控制或对结果的审查。

如果任务暂停，请阅读通知，并在有检测结果时审查这些结果。只有确认任务可以安全继续后，才应恢复。如果通知表明任务已结束，或未提供恢复选项，您就无法从该界面恢复任务。

| 使用界面与数据控制                                                                               | 检测结果与任务恢复                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 支持查看检测结果和恢复任务流程，且未启用此处所列数据控制的 Codex 和 ChatGPT Work 客户端 | 恢复任务前，请审查检测结果。                      |
| Codex CLI 和移动端                                                                                    | 无法查看完整检测结果或恢复任务。任务将结束。 |
| 零数据保留、调整后的滥用监控，或美国以外的数据存储驻留                        | 无法查看完整检测结果或恢复任务。任务将结束。 |

安全监控评估任务执行期间的模型行为。
[自动审批审查](/zh-Hans/codex/sandboxing/auto-review)则针对本就需要审批的单项操作，
在执行前进行评估。即使某项操作通过了自动审批审查，
其所属任务仍可能随后被监控暂停。

## 网络访问 

对于 Codex 云端，请参阅[智能体互联网访问](/zh-Hans/codex/cloud/internet-access)，了解如何启用完整的互联网访问权限或域名允许列表。

对于 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展，默认的 `workspace-write` 沙盒模式会关闭网络访问，除非您在配置中将其启用：

```toml
[sandbox_workspace_write]
network_access = true

### 网络隔离

网络访问通过目标地址规则进行控制，这些规则适用于脚本、
程序和命令派生的子进程。如果命令的网络访问权限
已经启用，请开启 `network_proxy` 功能，将相关流量
限制在您配置的网络策略范围内。
仅添加域名规则不会自动启用代理。

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

对于一次性 CLI 会话，如果只需控制开关，请使用布尔值简写形式；如果还需设置策略选项，请使用表形式：

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

该功能会改变已启用网络访问的管控方式，但本身不会授予
网络访问权限。请将 `sandbox_workspace_write.network_access` 与
`workspace-write` 配置配合使用，以决定命令是否拥有网络访问权限：

- 网络关闭 + `network_proxy` 开启：网络保持关闭，此功能不起作用。
- 网络开启 + `network_proxy` 关闭：网络保持开启，
  可不受限制地直接进行出站访问。
- 网络开启 + `network_proxy` 开启：网络保持开启，
  出站流量受已配置的网络策略限制。

代理功能也适用于[权限配置方案](/zh-Hans/codex/permissions#network-permissions)。
配置方案中的 `network.enabled = true` 会授予命令网络访问权限，
而 `features.network_proxy = true` 则会启用
该配置方案中域名规则的强制执行：

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

如果在此示例中省略代理功能，命令将可直接访问网络，
且 `api.openai.com` 允许规则不会限制其访问目标。

管理员管理的 `experimental_network` 要求与用户端功能开关彼此独立。
即使未启用 `features.network_proxy`，
也可以通过这些要求配置并启动沙盒网络；
但如果当前沙盒关闭网络访问，它们不会开启网络访问。请参阅[托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-network-access-requirements)，
了解管理员端 `requirements.toml` 的配置结构。

#### 网络策略

域名规则以允许列表为基础：

- 精确主机规则仅匹配该主机本身。
- `*.example.com` 可匹配 `api.example.com` 等子域名，
但不匹配 `example.com`。
- `**.example.com` 同时匹配根域名和子域名。
- 全局 `*` 允许规则可匹配任何未被拒绝的公网主机。请将 `*` 视为广泛的网络访问权限，
  并尽可能优先使用限定范围的规则。
- `deny` 始终优先于 `allow`，而全局 `*` 仅适用于允许规则。

#### 本地和专用网络目标地址

默认情况下，`allow_local_binding = false` 会阻止访问回环地址、链路本地地址
和专用网络地址：

- 特定例外：当命令需要访问单个本地目标时，
  请添加针对精确本地 IP 字面量或 `localhost` 的允许规则。
- 更广泛的访问：只有当您确实希望扩大本地/专用网络的访问范围时，
  才应设置 `allow_local_binding = true`。
- 通配符：通配符规则不视为显式的本地例外。
- 解析后的地址：解析到本地/专用 IP 地址的主机名，即使匹配允许列表，仍会被阻止。

#### DNS 重绑定防护

在允许访问某个主机名之前，Codex 会尽可能执行 DNS 和 IP 分类检查：

- 查询失败或超时时，访问将被阻止。
- 解析到非公网地址的主机名会被阻止。
- 该检查能够降低 DNS 重绑定风险，但无法完全消除。要彻底防止重绑定，需要将解析后的 IP 地址一直固定到传输层。

如果威胁范围包括恶意 DNS，还应在更底层实施出站控制。

#### 危险设置

以下两项设置会主动扩大信任边界：

- `dangerously_allow_non_loopback_proxy = true` 可能会使代理侦听器
  暴露在回环地址之外。
- `dangerously_allow_all_unix_sockets = true` 会绕过 Unix 套接字允许列表。

请仅在严格受控的环境中使用这些设置。启用 Unix 套接字代理后，即使请求绑定到非回环地址，监听器也仍仅绑定到回环地址，因此沙盒网络不会成为远程访问本地守护进程的桥梁。

`network_proxy` 默认关闭。启用后的行为如下：

| 设置                                | 默认值 | 行为                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | 仅当命令的网络访问已开启时，才启动沙盒网络。                                                                                                           |
| `domains`                              | 未设置   | 采用允许列表机制，因此在您添加 `allow` 规则之前，不允许访问任何外部目标。支持精确主机匹配、限定范围的通配符以及全局 `*` 允许规则；`deny` 始终优先。 |
| `unix_sockets`                         | 未设置   | 在您添加明确的 `allow` 规则之前，不允许访问任何 Unix 套接字目标。                                                                                                         |
| `allow_local_binding`                  | `false` | 阻止访问本地和私有网络目标，除非您添加包含确切本地 IP 字面量或 `localhost` 的允许规则，或明确启用更广泛的本地或私有网络访问。                |
| `enable_socks5`                        | `true`  | 在策略允许时提供 SOCKS5 支持。                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | 当 SOCKS5 可用时，允许通过 SOCKS5 传输 UDP。                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | 允许沙盒网络使用环境中配置的上游代理。                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | 除非您有意将监听端点暴露到 localhost 之外，否则它们始终绑定到回环地址。                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | 除非您有意绕过该防护，否则 Unix 套接字访问始终受允许列表控制。                                                                                              |

### 命令网络代理之外的流量

网络代理会过滤在本地命令沙盒中运行的脚本、程序和子进程。它不会过滤网页搜索、应用或连接器工具调用、MCP 服务器连接、浏览器或计算机使用活动、Codex 云端任务，以及客户端的模型和身份验证请求。这些功能使用独立的服务连接、功能设置、工作空间策略或环境控制。

浏览器工具在访问某个源之前，会单独检查托管的网络拒绝规则和排他性允许列表。
浏览器源策略可进一步限制站点访问、
上传、下载和开发者工具。请参阅
[托管浏览器控制](/zh-Hans/codex/enterprise/managed-configuration#control-browser-and-computer-use)。

对于托管用户，请将命令网络策略与以下控制措施结合使用：
`allowed_web_search_modes`、已获批准的 `mcp_servers`，以及针对应用、插件、浏览器或计算机使用的
功能要求。请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)。

您还可以控制[网页搜索工具](https://platform.openai.com/docs/guides/tools-web-search)，而无需向启动的命令授予完整网络访问权限。Codex 默认通过网页搜索缓存获取结果。该缓存是 OpenAI 维护的网页搜索结果索引，因此缓存模式会返回预先编入索引的结果，而不会获取实时网页。这可以降低任意实时内容带来的提示注入风险，但您仍应将网页搜索结果视为不受信任的内容。如果您使用 `--yolo` 或其他[完全访问权限沙盒设置](#common-sandbox-and-approval-combinations)，网页搜索默认会返回实时结果。使用 `--search` 或设置 `web_search = "live"` 可允许实时浏览；也可以将其设为 `"disabled"` 以关闭该工具：

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

当外部网页访问应受搜索索引限制时，请设置 `web_search = "indexed"`。
在 Codex 中启用网络访问或网页搜索时请务必谨慎。
提示注入可能导致智能体获取并遵循不受信任的指令。

## 默认设置与建议

- 启动时，Codex 会检测文件夹是否纳入版本控制，并给出以下建议：
  - 已纳入版本控制的文件夹：`Auto`（工作空间可写 + 按需审批）
  - 未纳入版本控制的文件夹：`read-only`
- 根据您的设置，Codex 也可能以 `read-only` 模式启动，直到您明确将工作目录设为可信（例如，通过初始设置提示或 `/permissions`）。
- 工作空间包括当前目录以及 `/tmp` 等临时目录。使用 `/status` 命令可查看工作空间包含哪些目录。
- 要接受默认设置，请运行 `codex`。
- 您可以明确设置这些选项：
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### 可写根目录中的受保护路径

在默认的 `workspace-write` 沙盒策略中，可写根目录仍包含受保护路径：

- 无论 `<writable_root>/.git` 是目录还是文件，都会受到只读保护。
- 如果 `<writable_root>/.git` 是指针文件（`gitdir: ...`），解析后的 Git 目录路径也会受到只读保护。
- 当 `<writable_root>/.agents` 以目录形式存在时，会受到只读保护。
- 当 `<writable_root>/.codex` 以目录形式存在时，会受到只读保护。
- 此保护以递归方式应用，因此这些路径下的所有内容均为只读。

### 运行时不显示审批提示

您可以使用 `--ask-for-approval never` 或其简写形式 `-a never` 禁用审批提示。

此选项适用于所有 `--sandbox` 模式，因此您仍可控制 Codex 的自主程度。Codex 会在您设定的限制范围内尽力执行。

如果您需要 Codex 在不显示审批提示的情况下读取文件、进行编辑并运行可访问网络的命令，请使用 `--sandbox danger-full-access`（或 `--dangerously-bypass-approvals-and-sandbox` 标志）。执行此操作前请务必谨慎。

作为折中方案，`approval_policy = { granular = { ... } }` 可让特定类别的审批提示保持交互式，同时自动拒绝其他类别。细粒度策略涵盖沙盒审批、execpolicy-rule 提示、MCP 提示、`request_permissions` 提示以及技能脚本审批。

### 审批请求自动审查

默认情况下，审批请求会转交给您：

```toml
approvals_reviewer = "user"

审批请求自动审查适用于交互式审批，例如
`approval_policy = "on-request"` 或细粒度审批策略。设置
`approvals_reviewer = "auto_review"` 后，符合条件的审批请求会在 Codex 执行相应请求之前
先交由审查智能体处理：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

有关审查器的完整生命周期、触发条件、配置优先级
和失败处理方式，请参阅
[自动审查](/zh-Hans/codex/sandboxing/auto-review)。

审查器仅评估原本就需要审批的操作，例如沙盒权限提升、
被阻止的网络请求、`request_permissions` 提示，或
会产生副作用的应用工具调用和 MCP 工具调用。沙盒内的操作
无需额外审查即可继续执行。

审查器策略会检查数据外泄、凭据探测、持续削弱安全防护的行为以及破坏性操作。在策略允许的情况下，低风险和中等风险操作可以继续执行。该策略会拒绝严重风险操作。高风险操作需要获得充分的用户授权，并且不能匹配任何拒绝规则。如果提示构建、审查会话或解析失败，系统会默认拒绝执行。超时情况会单独显示，但相应操作仍不会执行。

[默认审查器策略](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
位于开源 Codex 代码仓库中。企业可以使用托管要求中的 `guardian_policy_config`
替换其中的租户专属部分。
也支持本地 `[auto_review].policy` 策略文本，但托管要求
具有更高优先级。有关设置详情，请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-automatic-review-policy)。

在 ChatGPT 桌面应用中，这些审查会显示为自动审查条目，状态包括“审查中”“已批准”“已拒绝”“已中止”或“已超时”。其中还可能包含所审查请求的风险级别和用户授权评估。

自动审查会额外调用模型，因此可能增加 Codex 用量。管理员
可以使用 `allowed_approvals_reviewers` 对其进行限制。

### 常见的沙盒与审批组合

| 用途                                                            | 标志/配置                                                                                                                      | 效果                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 自动（预设）                                                     | _无需指定标志_ ，或使用 `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex 可以在工作空间中读取文件、进行编辑和运行命令。若要编辑工作空间之外的内容或访问网络，Codex 需要获得审批。 |
| 安全的只读浏览                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex 可以读取文件并回答问题。若要进行编辑、运行命令或访问网络，Codex 需要获得审批。                               |
| 只读非交互式运行（CI）                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex 只能读取文件；绝不会请求审批。                                                                                              |
| 自动编辑，但运行不受信任的命令前需请求审批 | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex 可以读取和编辑文件，但在运行不受信任的命令之前会请求审批。                                                           |
| 自动审核模式                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` 或 `approvals_reviewer = "auto_review"` | 沙盒边界与标准的按请求审批模式相同，但符合条件的审批请求由自动审查处理，不会呈现给用户。  |
| 危险的完全访问权限                                             | `--dangerously-bypass-approvals-and-sandbox`（别名：`--yolo`）                                                                      |  无沙盒；无需审批 _（不推荐）_                                                                               |

对于非交互式运行，请使用 `codex exec --sandbox workspace-write`；Codex 仍保留旧的 `codex exec --full-auto` 调用方式作为已弃用的兼容途径，并会输出警告。

使用 `--ask-for-approval untrusted` 时，Codex 只会自动执行已知安全的读取操作。可能改变状态或触发外部执行路径的命令（例如破坏性的 Git 操作，或使用 Git 输出标志、配置覆盖标志的命令）需要审批。

#### 在 `config.toml` 中配置

有关更完整的配置工作流程，请参阅[基础配置](/zh-Hans/codex/config-file/config-basic)、[高级配置](/zh-Hans/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)和[配置参考资料](/zh-Hans/codex/config-file/config-reference)。

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

您也可以将预设保存为[配置方案文件](/zh-Hans/codex/config-file/config-advanced#profiles)，然后使用 `codex --profile profile-name` 选择：

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### 在本地测试沙盒

要了解命令在 Codex 沙盒中运行时的行为，请使用以下 Codex CLI 命令：

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

`sandbox` 命令也可以通过 `codex debug` 使用，各平台的辅助命令也有别名，例如 `codex sandbox seatbelt` 和 `codex sandbox landlock`。

## 操作系统级沙盒

Codex 会根据您使用的操作系统，以不同方式实施沙盒隔离：

- **macOS** 使用 Seatbelt 策略，并通过 `sandbox-exec` 配合与您所选 `--sandbox` 模式对应的配置方案（`-p`）运行命令。当受限读取访问启用平台默认设置时，Codex 会追加经过筛选的 macOS 平台策略，而不是全面放行 `/System`，以保持常用工具的兼容性。
- **Linux** 默认结合使用 `bwrap` 和 `seccomp`。
- 在 **Windows** 上，通过[适用于 Linux 的 Windows 子系统 2（WSL2）](/zh-Hans/codex/windows/wsl)运行时，Codex 采用 Linux 沙盒实现。Codex `0.114` 及之前的版本支持 WSL1；从 `0.115` 开始，Linux 沙盒改用 `bwrap`，因此不再支持 WSL1。在 Windows 上原生运行时，Codex 使用 [Windows 沙盒](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)实现。

如果您在 Windows 上使用 Codex IDE 扩展，该扩展直接支持 WSL2。请在 VS Code 中进行以下设置，确保只要 WSL2 可用，智能体就始终在其中运行：

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

这可确保即使主机操作系统是 Windows，IDE 扩展在处理命令、审批和文件系统访问时，也会沿用 Linux 沙盒语义。有关详情，请参阅 [WSL 指南](/zh-Hans/codex/windows/wsl)。

在 Windows 上原生运行时，请在 `config.toml` 中配置原生沙盒模式：

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

有关详情，请参阅 [Windows 设置指南](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)。

在 Docker 等容器化环境中运行 Linux 时，如果主机或容器配置阻止 Codex 所需的命名空间操作、setuid `bwrap` 操作或 `seccomp` 操作，沙盒可能无法正常工作。

在这种情况下，请先配置 Docker 容器以提供所需的隔离，再在容器内使用 `--sandbox danger-full-access`（或 `--dangerously-bypass-approvals-and-sandbox` 标志）运行 `codex`。

### 在 Dev Containers 中运行 Codex

如果您的主机无法直接运行 Linux 沙盒，或者您的组织已将容器化开发作为标准，请通过 Dev Containers 运行 Codex，并由 Docker 提供外层隔离边界。此方式适用于 Visual Studio Code Dev Containers 及兼容工具。

请将 [Codex 安全开发容器示例](https://github.com/openai/codex/tree/main/.devcontainer)作为参考实现。该示例会安装 Codex、常用开发工具和 `bubblewrap`，并设置基于防火墙的出站访问控制。

  开发容器能提供有效防护，
  但无法阻止所有攻击。如果您在容器内使用 `--sandbox danger-full-access` 或
`--dangerously-bypass-approvals-and-sandbox` 运行 Codex，
  恶意项目可能会外传开发容器内可访问的任何内容，包括
  Codex 凭据。请仅对受信任的代码仓库使用此模式，
  并像监控其他高权限环境一样监控 Codex 的活动。

该参考实现包括：

- 已安装 Codex 和常用开发工具的 Ubuntu 24.04 基础镜像；
- 基于允许列表的出站访问防火墙配置方案；
- 用于在容器中重新打开工作空间的 VS Code 设置及推荐扩展程序；
- 用于命令历史记录和 Codex 配置的持久化挂载；
- `bubblewrap`，以便在容器授予所需能力时，Codex 仍可使用其 Linux 沙盒。

试用方法：

1. 安装 Visual Studio Code 和 [Dev Containers 扩展程序](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)。
2. 将 Codex 示例中的 `.devcontainer` 配置复制到您的代码仓库中，或直接从 Codex 代码仓库开始。
3. 在 VS Code 中运行 **Dev Containers: Open Folder in Container...** ，然后选择 `.devcontainer/devcontainer.secure.json`。
4. 容器启动后，打开终端并运行 `codex`。

您也可以通过 CLI 启动容器：

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

该示例主要包含三个部分：

- `.devcontainer/devcontainer.secure.json` 用于控制容器设置、能力、挂载、环境变量及 VS Code 扩展程序。
- `.devcontainer/Dockerfile.secure` 用于定义基于 Ubuntu 的镜像和安装的工具。
- `.devcontainer/init-firewall.sh` 用于应用出站网络策略。

该参考防火墙在设计上仅作为起点。如果您依赖域名允许列表实现隔离，请根据自身环境实施 DNS 重绑定防护和 DNS 刷新防护，例如依据 TTL 进行刷新，或采用可感知 DNS 的防火墙。

在容器内，请选择以下模式之一：

- 如果 Dev Container 配置方案授予了 `bwrap` 创建内层沙盒所需的能力，请保持启用 Codex 的 Linux 沙盒。
- 如果您希望将容器作为安全边界，请在容器内使用 `--sandbox danger-full-access` 运行 Codex，使 Codex 不再尝试创建第二层沙盒。

## 版本控制

配合版本控制工作流程使用 Codex 效果最佳：

- 请在功能分支上工作，并在委派任务前确保 `git status` 显示工作区干净。这样更容易隔离和还原 Codex 生成的补丁。
- 优先采用基于补丁的工作流（例如 `git diff`/`git apply`），而不是直接编辑受跟踪的文件。请频繁提交，以便按较小粒度回滚。
- 请像处理其他 PR 一样对待 Codex 提出的建议：进行针对性验证、审查差异，并在提交信息中记录决策，以供审计。

## 监控与遥测

Codex 支持用户主动启用基于 OpenTelemetry（OTel）的监控，帮助团队在不削弱本地默认安全设置的情况下审计使用情况、调查问题并满足合规要求。遥测默认关闭；请在配置中明确启用。

### 概览

- Codex 默认关闭 OTel 导出，以保持本地运行的独立性。
- 启用后，Codex 会发出结构化日志事件，涵盖聊天、API 请求、SSE/WebSocket 流活动、用户提示（默认隐去内容）、工具审批决策和工具结果。
- Codex 会使用 `service.name`（发起方）、CLI 版本和环境标签标记导出的事件，以区分开发、预发布和生产环境的流量。

### 启用 OTel（需主动启用）

在 Codex 配置中添加 `[otel]` 配置块（配置文件通常为 `~/.codex/config.toml`），并选择导出器以及是否记录提示文本。

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` 会保持插桩处于启用状态，但不会向任何位置发送数据。
- 要将事件发送到您自己的收集器，请从以下选项中选择一个：

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Codex 批量处理事件，并在关闭时发送所有缓存的事件。Codex 仅导出其 OTel 模块生成的遥测数据。

### 事件类别

典型事件类型包括：

- `codex.conversation_starts`（模型、推理设置、沙盒/审批策略）
- `codex.api_request`（尝试信息、状态/是否成功、耗时和错误详情）
- `codex.sse_event`（流事件类型、成功/失败、耗时，以及 `response.completed` 中的 Token 数量）
- `codex.websocket_request` 和 `codex.websocket_event`（请求耗时，以及每条消息的类型、是否成功和错误信息）
- `codex.user_prompt`（长度；除非明确启用内容记录，否则内容会被隐去）
- `codex.tool_decision`（批准/拒绝，来源：配置或用户）
- `codex.tool_result`（耗时、是否成功、输出片段）

相关 OTel 指标以计数器和耗时直方图配对的形式提供，包括 `codex.api_request`、`codex.sse_event`、`codex.websocket.request`、`codex.websocket.event` 和 `codex.tool.call`（以及对应的 `.duration_ms` 度量工具）。

有关完整的事件目录和配置参考资料，请参阅 [GitHub 上的 Codex 配置文档](https://github.com/openai/codex/blob/main/docs/config.md#otel)。

### 安全与隐私指南

- 除非策略明确允许存储提示内容，否则请保持 `log_user_prompt = false`。提示可能包含源代码和敏感数据。
- 仅将遥测数据发送到您控制的收集器；根据您的合规要求实施数据保留限制和访问控制。
- 请将工具参数和输出视为敏感信息。条件允许时，优先在收集器或 SIEM 中进行脱敏处理。
- 如果您不希望 Codex 在 `CODEX_HOME` 下保存会话记录，请检查本地数据保留设置（例如 `history.persistence` / `history.max_bytes`）。请参阅[高级配置](/zh-Hans/codex/config-file/config-advanced#history-persistence)和[配置参考资料](/zh-Hans/codex/config-file/config-reference)。
- 如果您在关闭网络访问的情况下运行 CLI，OTel 导出将无法连接到您的收集器。要导出数据，请在 `workspace-write` 模式下允许对 OTel 端点的网络访问，或从 Codex 云端导出，并确保收集器域名位于您的批准列表中。
- 请定期审查事件，检查审批或沙盒的变更以及意外的工具执行。

OTel 是可选功能，旨在补充而非取代上述沙盒和审批防护。

## 托管配置

企业管理员可以在[托管配置](/zh-Hans/codex/enterprise/managed-configuration)中为其工作空间配置 Codex 安全设置。有关设置和策略详情，请参阅该页面。
