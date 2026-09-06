<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/managed-configuration -->

托管配置用于控制 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中所涵盖功能的受支持本地运行时行为。不同客户端及版本支持的要求可能有所不同。托管配置不会授予 ChatGPT 工作空间访问权限、分配席位，也不会取代工作空间基于角色的访问控制 (RBAC)。有关工作空间功能的访问权限，请参阅[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)；有关本地运行时策略，请参阅本页。

企业管理员可以通过以下两种方式控制受支持的本地客户端行为：

- **要求**：由管理员强制执行、用户无法覆盖的约束。
- **托管默认值**：受支持的客户端启动时应用的初始值。用户仍可在运行期间更改设置；客户端会在下次启动时重新应用托管默认值。

## 管理员强制执行的要求（requirements.toml）

要求会约束安全敏感设置，包括审批策略、审批审查者、自动审查策略、沙盒模式、权限配置方案、网页搜索模式、托管钩子、用户可启用的 MCP 服务器，以及用户可添加、从中安装插件或刷新的用户自配插件市场来源。解析配置（例如来自 `config.toml`、[配置方案文件](/zh-Hans/codex/config-file/config-advanced#profiles)或 CLI 配置覆盖项的配置）时，如果某个值与强制执行的规则冲突，本地客户端会回退到兼容值并通知用户。如果您配置了 `mcp_servers` 允许列表，只有当 MCP 服务器的名称和身份都与获准条目匹配时，客户端才会启用该服务器；否则会将其禁用。

要求还可以通过 `requirements.toml` 中的 `[features]` 表约束[功能标志](/zh-Hans/codex/config-file/config-basic/#feature-flags)。请注意，功能并非都涉及安全，但企业可以根据需要固定其值。未指定的键不受约束。

对于 Codex 0.138.0 或更高版本，请优先使用[权限配置方案](/zh-Hans/codex/permissions)，
并搭配 `allowed_permission_profiles` 和托管的 `default_permissions`。
`allowed_sandbox_modes` 仅适用于仍在配置
`sandbox_mode` 的旧版部署。

有关确切的键列表，请参阅[配置参考资料中的 `requirements.toml` 部分](/zh-Hans/codex/config-file/config-reference#requirementstoml)。

### 位置和优先级

每个受支持的本地客户端都会按优先级从低到高组合各项要求：

1. 系统 `requirements.toml`（在 Unix 系统上为 `/etc/codex/requirements.toml`，
   包括 Linux 和 macOS；
   在 Windows 上为 `%ProgramData%\OpenAI\Codex\requirements.toml`）。
2. 通过云端配置包下发的企业托管要求。
3. 本地客户端重新解释为要求的旧版 `managed_config.toml` 字段。
4. 通过
`com.openai.codex:requirements_toml_base64` 下发的 macOS 托管偏好设置（MDM）。

优先级较高的配置层会覆盖
优先级较低的配置层中的普通标量值和列表值。表按键合并，
而规则、钩子和文件系统限制等要求则根据具体字段采用不同的组合方式。请查阅
[`requirements.toml` 参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)
了解当前模式，不要假定所有字段
都以相同方式合并。

为了保持向后兼容，受支持的本地客户端会将旧版
`approval_policy`、`approvals_reviewer` 和 `sandbox_mode` 字段重新解释为要求。
此转换会在必要时添加兼容性选项；
如需明确指定允许列表，请使用 `requirements.toml`。

### 云端托管要求

当用户使用受支持套餐的 ChatGPT 账户登录时，受支持的本地客户端
可以接收与工作空间关联、由管理员强制执行的要求。
这是下发与 `requirements.toml` 兼容的策略的渠道。
它不会授予工作空间访问权限，也不会取代工作空间 RBAC。

打开[托管配置](https://chatgpt.com/codex/settings/managed-configs)，
创建并分配云端托管要求。例如，此策略会限制
审批和沙盒选项，并在受支持的 Shell 入口点运行前
显示提示：

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

请确认每个托管客户端版本都支持您选择的键，并在分配给整个组织之前，先让一小组用户测试该策略。请查阅配置参考资料了解当前模式，并通过管理界面了解当前的分配行为。

服务会选择适用于当前登录身份的
企业托管要求层。本地客户端会将这些配置层与
[位置和优先级](#locations-and-precedence)中所述的其他要求来源一起评估。
请通过当前的管理界面在工作空间端
创建和分配要求。请勿依赖复制的群组匹配算法；
这一行为由管理服务负责，可以独立于
本地要求格式进行调整。

有关支持的键和示例，请参阅
[requirements.toml 示例](#example-requirementstoml)以及
[`requirements.toml` 参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)。

#### 本地客户端如何应用云端托管要求

当用户启动受支持的本地客户端，并使用受支持套餐的 ChatGPT 账户登录时，客户端会先检查是否存在有效且身份匹配的缓存条目。如果没有有效条目，客户端会获取适用的配置包并按需重试，成功后写入带签名的缓存条目。如果请求失败或超时，且没有可用的有效缓存，云端配置包加载将返回错误，而不会在缺少云端托管要求层的情况下静默启动。

完成缓存解析后，客户端会将云端要求与上述其他要求层组合。后台刷新可以更新缓存，供后续启动时使用；但不会替换当前进程中已经加载的要求。

### 确认管理员和员工的使用体验

为每项托管策略指定负责人，记录应接收该策略的用户或群组，并记录对文件系统、网络、审批或权限配置方案施加任何限制的业务原因。

在扩大部署范围之前，请与具有代表性的用户一起测试一个获准的工作流程，以及一个明确设置为不允许的工作流程。请在受支持的客户端中验证实际生效的设置，不要认为仅凭工作空间角色或群组就能实施本地限制。

### requirements.toml 示例

本示例会阻止 `--ask-for-approval never` 和 `--sandbox danger-full-access`（包括 `--yolo`）：

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### 禁用应用快照

要为托管用户禁用应用快照，请设置顶层 `allow_appshots` 要求：

```toml
allow_appshots = false

在应用快照可用的情况下，`allow_appshots = false` 会将其禁用。
如果您省略该键，相关要求不会限制应用快照，
仍适用常规产品可用性检查。App Server 客户端
通过 `configRequirements/read` 读取实际生效的要求时，会以
`allowAppshots` 的形式接收相同限制；如果 `allowAppshots` 被省略或值为 `null`，
则不会禁用应用快照。

### 禁用设备远程控制

要为托管用户禁用[设备远程控制](/zh-Hans/codex/remote-connections#pick-up-work-from-another-device)，
请设置顶层 `allow_remote_control` 要求：

```toml
allow_remote_control = false

在支持设备远程控制的情况下，`allow_remote_control = false` 会将其禁用。
如果您省略该键，相关要求不会限制设备远程控制，
仍适用常规产品可用性检查。
此要求不会禁用 SSH 远程连接。

### 控制可用的权限配置方案

使用 `allowed_permission_profiles` 控制用户可以选择哪些内置和自定义
[权限配置方案](/zh-Hans/codex/permissions)。
它相当于权限配置方案层面的 `allowed_sandbox_modes`；
请根据用户选择权限的方式使用相应的允许列表。

权限配置方案允许列表要求使用 Codex 0.138.0 或更高版本。
Codex 0.137.0 及更早版本会忽略 `allowed_permission_profiles` 和托管的
`default_permissions`。

仅当所有托管客户端都运行支持相关功能的版本后，才可使用以下权限配置方案示例。在所有客户端升级完成前，请勿部署托管的自定义配置方案。

如果该表存在，它就是获准配置方案的完整列表。
设为 `true` 的配置方案会被允许；省略或设为 `false` 的配置方案会被拒绝，
未来 Codex 版本新增的内置配置方案也不例外。

#### 允许标准配置方案

此策略允许只读访问和工作空间访问，但不允许完全访问权限：

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### 添加遵循最小权限原则的托管默认值

管理员可以在同一要求来源中定义自定义配置方案。
请使用组织专属的配置方案名称，
避免与用户已加载配置中的名称冲突。自定义名称不能以 `:` 开头，
也不能使用保留名称 `filesystem`。

请勿向运行 Codex 0.137.0 或更早版本的客户端部署托管的自定义配置方案。这些客户端能够识别配置方案表，但无法识别用于选择该配置方案的托管默认值。

例如：

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### 仅允许企业定义的配置方案

如果用户应当只能选择管理员定义的配置方案，请省略所有内置配置方案：

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

自定义配置方案可以扩展 `:workspace`，
即便用户无法直接选择内置的 `:workspace` 配置方案。

#### 禁用其他来源允许的配置方案

权限允许列表按配置方案名称合并。
由于云端要求的优先级高于系统要求，因此云端要求可以使用 `false`
禁用系统文件允许的配置方案。

云端要求：

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

系统要求：

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

请将 `default_permissions` 明确设置为获准的配置方案。如果省略该设置，
本地运行时仅在 `:workspace` 和
`:read-only` 都被明确允许时，才会默认使用 `:workspace`。如果 `allowed_permission_profiles` 不存在，
托管要求不会限制用户可以选择的配置方案名称。
每个条目都必须指定内置配置方案，或在
已加载的配置或要求来源中定义的自定义配置方案。
请在托管要求中定义自定义配置方案，以便集中控制其行为。

### 按主机覆盖沙盒要求

如果同一项托管策略需要在不同主机上应用不同的沙盒要求，
请使用 `[[remote_sandbox_config]]`。例如，您可以为笔记本电脑保留更严格的默认设置，
同时允许匹配的开发机或 CI 运行器写入工作空间。
目前，特定于主机的条目只会覆盖 `allowed_sandbox_modes`：

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

本地运行时会尽可能解析主机名，
并将每个 `hostname_patterns` 条目与解析结果进行比较。如果完全限定域名可用，
则优先使用该域名；否则回退到本地主机名。匹配不区分大小写；
`*` 匹配任意字符序列，`?` 匹配单个字符。

同一要求来源中，第一个匹配的 `[[remote_sandbox_config]]` 条目优先生效。
如果没有条目匹配，本地运行时会保留顶层的
`allowed_sandbox_modes`。主机名匹配仅用于选择策略；
请勿将其视为设备已通过身份验证的证明。

您还可以约束网页搜索模式：

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` 仅允许 `"disabled"`。
例如，`allowed_web_search_modes = ["cached"]` 即使在 `danger-full-access` 会话中也会阻止实时网页搜索。

### 配置网络访问要求

  `[experimental_network]` 属于实验性功能，后续可能发生变化。请勿在尚未针对用户使用的
  本地客户端版本和操作系统进行验证的情况下，
  在企业部署中大范围启用这些要求。目前对 Windows 的支持
  仍然有限；除非您已在自己的环境中完成测试，否则请避免将此策略
  应用于 Windows 用户。

如果管理员需要集中定义网络访问要求，请使用 `requirements.toml` 中的 `[experimental_network]`。
这些要求独立于用户的 `features.network_proxy` 开关：
即使未启用该功能标志，也可以配置沙盒网络，
但如果当前沙盒禁用了联网，这些要求不会授予命令网络访问权限。
请设置
`experimental_network.enabled = true` 以启用托管代理；
仅配置域名规则不会使代理生效。

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

仅当您同时在 `[experimental_network.domains]` 中定义了
由管理员管理的 `"allow"` 条目，
并希望只允许这些规则生效时，才使用 `experimental_network.managed_allowed_domains_only = true`。
如果将其设为 `true`，却没有配置托管允许规则，则用户添加的域名允许规则将不再生效。
请勿将规范的 `domains` 映射与旧版
`allowed_domains` 或 `denied_domains` 列表混用。

`*.example.com` 仅匹配子域名。`**.example.com` 匹配根域名
及其子域名。匹配的拒绝规则优先于允许规则。

域名语法、本地或私有目标地址规则、拒绝规则优先于允许规则的行为
以及 DNS 重绑定限制，均与
[智能体审批与安全](/zh-Hans/codex/agent-approvals-security#network-isolation)中所述的沙盒联网行为一致。

代理会路由在沙盒内运行的本地命令的网络流量。浏览器工具在访问某个源之前，也会检查托管网络拒绝规则和排他性允许列表；这是单独的策略检查，并不是通过命令代理路由浏览器流量。代理不会过滤网页搜索、应用和连接器、MCP 服务器、原生应用流量、Codex 服务请求或 Codex 云端流量。请使用各功能对应的控制措施：

- 使用 `allowed_web_search_modes` 限制网页搜索。
- 使用 `features.apps = false` 禁用应用和连接器集成，并在受支持的情况下
使用 `features.plugins = false` 禁用插件。
- 使用托管的 `mcp_servers` 批准列表限制 MCP 服务器。
- 使用 `browser_use`、`in_app_browser` 和
`computer_use` 等功能要求，限制浏览器和计算机使用能力。
- 在云端环境设置中配置 Codex 云端的网络访问。

命令域名允许列表不能替代这些针对特定功能的控制措施。

### 控制浏览器和计算机使用

使用 `requirements.toml` 中的 `[browser_use]` 和 `[computer_use]` 表，
限制受支持的桌面客户端。请在部署环境中的客户端版本
和操作系统上验证该策略。配置允许规则并不会
安装插件、授予操作系统权限，
也不会批准仍需审查的操作。

对于浏览器访问，请配置源策略。源包含协议、
主机和可选的端口，例如 `https://example.com` 或
`https://*.example.com:8443`。请勿包含路径、查询字符串或片段。
与命令网络域名规则不同，浏览器源规则会区分 HTTP 和 HTTPS，
并匹配端口。

此示例将浏览器访问限制为已批准的站点，并禁止向该站点上传内容或对其进行完整的 Chrome DevTools Protocol（CDP）访问：

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

匹配的源规则会逐字段确定最终取值。匹配的拒绝规则优先；除此之外，匹配规则未指定的字段由默认源策略提供。本地配置可以增加限制，但不能放宽托管拒绝规则。网络拒绝规则和排他性托管网络允许列表仍然适用。

设置 `browser_use.disable_auto_review = true` 可禁用对浏览器操作的自动审批审查，
也可以在源策略中设置 `auto_review = "deny"`，
对该源限制此功能。这控制的是审批处理方式，
不会禁用模型安全监控。

对于原生应用，请设置默认访问策略，并指定允许使用的应用。例如，以下 macOS 策略允许使用计算器，并禁止保存审批结果：

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Windows 策略可以通过
`computer_use.windows.aumids` 识别打包应用，或通过
`computer_use.windows.exes` 识别可执行文件。可执行文件规则必须包含 `publisher_name`、
`product_name` 和 `access`；`binary_name` 为可选项。请使用应用经过验证的
身份信息，而非仅使用其显示名称。

请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)
了解完整字段，并参阅[锁定使用限制](#restrict-locked-computer-use)
了解受管理的 macOS 设备的相关限制。

### 固定功能标志

您还可以为接收托管 `requirements.toml` 的用户
固定[功能标志](/zh-Hans/codex/config-file/config-basic/#feature-flags)：

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

对于运行时功能，请使用 `config.toml` 的 `[features]` 表中的规范功能键。
本地运行时会规范化已识别的功能，使其符合这些固定设置，
并拒绝向 `config.toml` 或配置方案文件中的功能设置
写入与之冲突的值。

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` 会禁用内置浏览器面板。
- 在受支持的情况下，`in_app_updates = false` 会在重启时
  禁用 ChatGPT 桌面应用自身的更新程序。此设置不会影响外部软件包部署，也不会
  延长对旧版应用的支持。有关设置和部署的指导，请参阅
[管理应用更新](/zh-Hans/codex/enterprise/manage-app-updates)。
- `browser_use = false` 会禁用浏览器中的计算机使用功能，并使 Browser Agent 不可用。
- `browser_use_full_cdp_access = false` 会禁用本地运行时的完整 CDP 访问权限，
  包括浏览器开发者模式，并阻止 ChatGPT 桌面应用
  启用相应设置。
- `browser_use_external = false` 会禁用外部浏览器功能。
- `computer_use = false` 会禁用计算机使用、录制与重放，以及相关的
  安装或设置流程。

如果您省略这些键，策略将允许相关功能，但其可用性仍取决于客户端、平台以及功能的正常发布进度。

### 限制锁定状态下的计算机使用

要阻止用户在受管理的 Mac 上启用[锁定使用](/zh-Hans/codex/computer-use#locked-use)，
请添加以下要求：

```toml
[computer_use]
allow_locked_computer_use = false

此要求会移除用于启用锁定使用的控件。如果锁定使用已启用，此要求不会将其关闭。如果您省略此要求，产品的正常可用性和用户的本地设置仍然适用。

### 配置自动审查策略

使用 `allowed_approvals_reviewers` 强制或允许自动审查。
将其设为 `["auto_review"]` 可强制自动审查；如果允许用户选择手动审批，
则应包含 `"user"`。

设置 `guardian_policy_config`，以替换自动审查策略中
针对特定租户的部分。本地运行时仍会使用内置的审查器
模板和输出约定。托管的 `guardian_policy_config`
优先于本地 `[auto_review].policy`。

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### 强制执行禁止读取要求

管理员可以使用
`[permissions.filesystem]` 禁止读取精确路径或与 glob 模式匹配的路径。用户无法通过本地
配置放宽这些要求。

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

存在禁止读取要求时，本地运行时会拒绝完全访问权限，
并将本地执行限制在只读沙盒或工作空间沙盒内，
以便强制执行这些要求。在原生 Windows 上，托管的 `deny_read` 适用于直接操作文件的工具；
shell 子进程的读取操作不适用此沙盒规则。

### 通过要求强制执行托管钩子

管理员也可以直接在 `requirements.toml` 中定义托管生命周期钩子。
使用 `[hooks]` 配置钩子本身，并将 `managed_dir` 指向
您的 MDM 或端点管理工具用于安装所引用脚本
的目录。

要对已在本地关闭钩子的用户也强制执行托管钩子，请固定
`[features].hooks = true`，并同时配置 `[hooks]`。要跳过用户、项目、会话
和插件钩子，同时仍允许托管钩子，请设置
`allow_managed_hooks_only = true`。

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

注意事项：

- 本地运行时会强制执行 `requirements.toml` 中的钩子配置，
  但不会分发 `managed_dir` 中的脚本。
- 请通过您的 MDM 或设备管理解决方案分发这些脚本。
- 托管钩子命令应引用已配置的托管目录下脚本的绝对路径。
- `allow_managed_hooks_only = true` 会跳过用户、项目、会话和
  插件来源的钩子，但仍会加载 `requirements.toml` 及其他
  托管配置层中的钩子。

### 通过要求强制执行命令规则

管理员还可以使用 `requirements.toml`
中的 `[rules]` 表强制执行限制性命令规则。这些规则会与常规 `.rules` 文件合并，
且仍以限制最严格的判定结果为准。

与 `.rules` 不同，要求中的规则必须指定 `decision`，且该判定值
必须为 `"prompt"` 或 `"forbidden"`（不能是 `"allow"`）。

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

要限制本地客户端可以启用的 MCP 服务器，请添加 `mcp_servers` 批准列表。
对于 stdio 服务器，按 `command` 匹配；
对于支持流式传输的 HTTP 服务器，按 `url` 匹配：

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

`identity.command` 的字符串形式仅匹配已配置的 `command`，
不会检查 `args`、`cwd`、`env` 或 `env_vars`。

要约束完整的 stdio 调用，请匹配可执行文件和每个位置参数：

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

可执行文件、参数数量和参数顺序都必须匹配。参数与 URL 规则
支持 `exact`、`prefix` 以及针对完整值的 `regex` 匹配。
结构化命令规则仍不会检查 `cwd`、`env` 或 `env_vars`。
插件附带的 MCP 服务器在
`plugins.<plugin>.mcp_servers.<server>` 下使用相同的标识结构。

如果 `mcp_servers` 存在但为空，本地客户端会禁用所有 MCP 服务器。

### 控制插件可用性

要在受支持的本地客户端中关闭插件，请在 `requirements.toml` 中将 `features.plugins` 设置为
`false`：

```toml
features.plugins = false

用户使用 API 密钥登录 Codex 时，此设置同样适用。请参阅
[`features.plugins`
参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)，了解
受支持的配置。

### 限制插件市场来源

要限制对用户配置的市场来源执行的操作，请设置
`restrict_to_allowed_sources = true`，并定义一条或多条来源规则：

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Git 规则会匹配规范化后的代码仓库 URL，并在指定
`ref` 时对其进行精确匹配。主机模式是与小写 Git 主机名匹配的正则表达式；
使用 `^` 和 `$` 可匹配整个主机名。本地规则要求使用
规范化的绝对路径。请参阅 [`requirements.toml` 参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)，
了解完整的配置模式和合并行为。

对于用户配置的来源，凡是与规则不匹配的添加市场、安装插件或刷新已配置 Git 市场的操作，都会被这些要求拒绝。由 Codex 管理的 OpenAI 市场在其来源和保留名称匹配时仍可用。这些要求不会在运行时过滤已配置的用户市场或其中的插件。

这些来源限制仅适用于支持插件市场操作的本地客户端：桌面应用中的 ChatGPT 和 Codex，以及 Codex CLI。它们不控制网页版或移动端 ChatGPT 中的插件使用，也不会为 IDE 扩展添加插件。

## 托管默认值（`managed_config.toml`）

托管默认值决定受支持的本地客户端启动时使用的配置。
启动时，它们会覆盖用户本地的 `config.toml` 以及通过 CLI `--config`
指定的所有覆盖项。用户仍可在当前运行期间更改这些设置，
下次客户端启动时会再次应用托管默认值。

如果托管默认值、macOS MDM 配置文件或已保存的配置为通过 ChatGPT 登录的用户固定使用 `gpt-5.4`
或 `gpt-5.4-mini`，请在 2026 年 8 月 31 日之前更新。将 `gpt-5.4` 替换为 `gpt-5.6-terra`，并将 `gpt-5.4-mini` 替换为
`gpt-5.6-luna`。OpenAI API 和使用您自己的 API 密钥进行身份验证的 Codex
不受影响。请参阅[工作空间模型
可用性](/zh-Hans/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement)。

请确保您的托管默认值符合要求；本地运行时会拒绝不允许的值。

### 优先级与分层

本地运行时按以下顺序组合出最终生效的配置（上层覆盖下层）：

- 托管偏好设置（macOS MDM；优先级最高）
- `managed_config.toml`（系统/托管文件）
- `config.toml`（用户的基础配置）

CLI `--config key=value` 覆盖项会应用于基础配置，但托管层会覆盖这些设置。这意味着，即使您提供本地标志，每次运行也都会从托管默认值开始。

云端托管要求影响的是要求层，而非托管默认值。有关优先级，请参阅上文的“管理员强制执行的要求”部分。

### 位置

- Linux/macOS（Unix）：`/etc/codex/managed_config.toml`
- Windows/非 Unix：`~/.codex/managed_config.toml`

如果该文件不存在，本地运行时会跳过托管层。

### macOS 托管偏好设置（MDM）

在 macOS 上，管理员可以推送设备配置文件，在以下位置提供经 base64 编码的 TOML 有效负载：

- 偏好设置域：`com.openai.codex`
- 键：
  - `config_toml_base64`（托管默认值）
  - `requirements_toml_base64`（要求）

本地运行时将这些“托管偏好设置”有效负载解析为 TOML。
对于托管默认值（`config_toml_base64`），托管偏好设置的优先级最高。
对于要求（`requirements_toml_base64`），优先级遵循
上文所述的云端托管要求顺序。
要求配置中的同一 `[features]` 表也适用于 `requirements_toml_base64`；
其中同样应使用规范的功能键。

### MDM 设置工作流程

本地运行时支持标准的 macOS MDM 有效负载，因此您可以
使用 `Jamf Pro`、`Fleet` 或 `Kandji` 等工具分发设置。
轻量级部署流程如下：

1. 编写托管有效负载的 TOML 内容，并使用 `base64` 对其编码（不换行）。
2. 在您的 MDM 配置文件中，将该字符串写入 `com.openai.codex` 域下的 `config_toml_base64`（托管默认值）或 `requirements_toml_base64`（要求）键。
3. 推送该配置文件，然后请用户重启受支持的本地客户端，并确认启动配置摘要显示托管值。
4. 撤销或更改策略时，请更新托管有效负载；客户端会在下次启动时读取更新后的偏好设置。

避免在有效负载中嵌入机密信息或频繁变化的动态值。请将托管 TOML 与其他 MDM 设置一样纳入变更控制。

### managed\_config.toml 示例

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### 推荐的防护措施

- 对于大多数用户，优先使用 `workspace-write` 并启用审批；仅对受控容器启用完全访问权限。
- 除非您的安全审查允许使用收集器或访问工作流所需的域名，否则请保留 `network_access = false` 设置。
- 使用托管配置固定 OTel 设置（导出器、环境），但除非您的策略明确允许存储提示内容，否则请保留 `log_user_prompt = false` 设置。
- 定期审计本地 `config.toml` 与托管策略之间的差异，以发现配置漂移；托管层的优先级应高于本地标志和文件。
