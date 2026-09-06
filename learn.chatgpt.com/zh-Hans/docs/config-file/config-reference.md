<!-- source: https://learn.chatgpt.com/zh-Hans/docs/config-file/config-reference -->

本页提供可搜索的 Codex 配置文件参考资料。如需了解相关概念和示例，请先阅读[基础配置](/zh-Hans/codex/config-file/config-basic)和[高级配置](/zh-Hans/codex/config-file/config-advanced)。

## `config.toml`

用户级配置位于 `~/.codex/config.toml`。您还可以在 `.codex/config.toml` 文件中添加项目级覆盖项。Codex 仅在您信任项目时加载项目级配置文件。

项目级配置无法覆盖本机的提供商、身份验证、
由主机控制的应用请求元数据、通知、配置方案选择
或遥测路由配置键。若 `openai_base_url`、
`chatgpt_base_url`、`apps_mcp_product_sku`、`model_provider`、
`model_providers`、`notify`、`profile`、`profiles`、
`experimental_realtime_ws_base_url` 和 `otel` 出现在
项目本地的 `.codex/config.toml` 中，Codex 会忽略这些设置；请改为在用户级配置中设置提供商、通知和遥测
配置键。[配置方案文件](/zh-Hans/codex/config-file/config-advanced#profiles)与
`config.toml` 位于同一目录，路径为 `$CODEX_HOME/profile-name.config.toml`；使用
`--profile profile-name` 选择配置方案。

对于沙盒和审批配置键（`approval_policy`、`sandbox_mode` 和 `sandbox_workspace_write.*`），请结合[沙盒与审批](/zh-Hans/codex/agent-approvals-security#sandbox-and-approvals)、[可写根目录中的受保护路径](/zh-Hans/codex/agent-approvals-security#protected-paths-in-writable-roots)以及[网络访问](/zh-Hans/codex/agent-approvals-security#network-access)阅读本参考资料。有关测试版的权限配置方案，请参阅[权限](/zh-Hans/codex/permissions)。

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "要使用的模型（例如 `gpt-5.5`）。",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "供 `/review` 使用的可选模型覆盖项（默认为当前会话模型）。",
    },
    {
      key: "model_provider",
      type: "string",
      description: "来自 `model_providers` 的提供商 ID（默认值：`openai`）。",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "内置 `openai` 模型提供商的基础 URL 覆盖项。",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "当前模型可用的上下文窗口 Token 数。",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "触发历史记录自动压缩的 Token 阈值（未设置时使用模型默认值）。",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "控制自动压缩阈值是按完整的当前上下文计算（`total`，默认值），还是仅按沿用的压缩窗口前缀之后的增长量计算（`body_after_prefix`）。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "启动时加载的 JSON 模型目录的可选路径。所选的 `$CODEX_HOME/profile-name.config.toml` 配置方案文件可以针对相应配置方案覆盖此设置。",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "使用 `--oss` 运行时采用的默认本地提供商（未设置时，默认提示您选择）。",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "控制 Codex 在执行命令前暂停并请求审批的时机。您还可以使用 `approval_policy = { granular = { ... } }`，允许显示或自动拒绝特定类别的提示，同时保留其他提示的交互方式。`on-failure` 已弃用；交互式运行请使用 `on-request`，非交互式运行请使用 `never`。",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "设为 `true` 时，允许显示沙盒权限提升审批提示。",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "设为 `true` 时，允许显示由 execpolicy 的 `prompt` 规则触发的审批提示。",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "设为 `true` 时，允许显示 MCP 引导式提取提示，而不是自动拒绝。",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "设为 `true` 时，允许显示来自 `request_permissions` 工具的提示。",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "设为 `true` 时，允许显示技能脚本审批提示。",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "指定由谁审查 `on-request` 或细粒度审批策略下符合条件的审批提示。默认为 `user`；`auto_review` 使用审查子智能体。此设置不会改变沙盒机制，也不会审查沙盒内已获允许的操作。",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "自动审查所用的本地 Markdown 策略指令。受管理的 `guardian_policy_config` 优先级更高。空值会被忽略。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "允许基于 Shell 的工具采用登录 Shell 语义。默认为 `true`；设为 `false` 时，`login = true` 请求会被拒绝，省略 `login` 时则默认使用非登录 Shell。",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "命令执行期间文件系统和网络访问的沙盒策略。",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "当 `sandbox_mode = \"workspace-write\"` 时的额外可写根目录。",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "允许在 workspace-write 沙盒内进行出站网络访问。",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "在 workspace-write 模式下，将 `$TMPDIR` 排除在可写根目录之外。",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "在 workspace-write 模式下，将 `/tmp` 排除在可写根目录之外。",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Codex 在 Windows 上原生运行时使用的 Windows 专用原生沙盒模式。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "在原生 Windows 上，默认让最终的沙盒子进程在专用桌面上运行。仅当需要兼容旧版 `Winsta0\\\\Default` 行为时，才设为 `false`。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "设为 `false` 可限制对浏览器历史记录的访问。受管理的要求可以强制实施此限制。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "浏览器源的回退限制。支持 `access`、`uploads`、`downloads` 和 `full_cdp_access`，每项均可设为 `allow` 或 `deny`。",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "针对各个源的浏览器限制，字段与 `browser_use.default_origin_policy` 相同。必须包含 HTTP 或 HTTPS 协议方案，可选填端口；不要包含路径、查询参数或片段。本地设置不能放宽受管理的拒绝规则。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "“计算机使用”访问原生应用时的回退策略。特定应用的条目可以提供策略；本地配置不能放宽受管理的限制。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "以捆绑包标识符为键的 macOS 原生应用访问设置。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "以应用程序用户模型 ID（AUMID）为键的已打包 Windows 应用访问设置。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Windows 可执行文件访问规则。每条规则都必须包含 `publisher_name`、`product_name` 和 `access`（`allow` 或 `deny`）；`binary_name` 为可选项。",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "“计算机使用”无需提示即可打开的 Windows 应用的标识符。不在列表中的应用需要审批；请在 ChatGPT 桌面应用的“计算机使用”设置中移除已保存的条目。",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "发送通知时调用的命令；该命令接收来自 Codex 的 JSON 负载。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "启动时检查 Codex 更新（仅当更新集中管理时，才设为 false）。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "允许在所有本地客户端中通过 `/feedback` 提交反馈（默认值：true）。",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "启用或禁用此计算机或配置方案的分析功能。未设置时，采用客户端默认值。",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "预留供将来使用；优先使用 `model_instructions_file` 或 `AGENTS.md`。",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "注入会话的额外开发者指令（可选）。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Codex 写入日志文件的目录；默认为 `$CODEX_HOME/log`。显式设置此项还会在该目录中启用需主动开启的纯文本 TUI 日志 `codex-tui.log`。",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex 存储基于 SQLite 的状态数据库的目录；该数据库用于智能体作业及其他可恢复的运行时状态。",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "历史记录压缩提示的内联覆盖项。",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "用于替换内置指令，而非 `AGENTS.md`。",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "声明支持 `supportsPersonality` 的模型所使用的默认沟通风格；可按线程或轮次覆盖，也可通过 `/personality` 覆盖。",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "新轮次的首选服务层级。请使用 `fast` 或当前模型声明支持的其他层级；`fast` 映射到请求值 `priority`。",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "从文件加载压缩提示的覆盖内容（实验性）。",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "可用技能目录的 Token 预算。默认为模型上下文窗口的 2%。显式设置的值上限为 `10000` 个 Token。",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "存储在 config.toml 中、按技能设置的启用状态覆盖项。",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "包含 `SKILL.md` 的技能文件夹路径。",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "启用或禁用引用的技能。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "按 ID 启用或禁用特定应用或连接器（默认值：true）。",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "所有应用的默认启用状态；各应用可单独覆盖此设置。",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "对设置了 `destructive_hint = true` 的应用工具的默认允许或拒绝设置。",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "对设置了 `open_world_hint = true` 的应用工具的默认允许或拒绝设置。",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "应用工具审批提示的默认审查者；各应用可单独覆盖此设置。省略时，应用会继承顶层 `approvals_reviewer` 的值。",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "未设置按应用或按工具覆盖项时，应用工具的默认审批行为。",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "允许或阻止此应用中声明 `destructive_hint = true` 的工具。",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "允许或阻止此应用中声明 `open_world_hint = true` 的工具。",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "此应用中工具的默认启用状态；如果存在针对单个工具的覆盖设置，则以该设置为准。",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "此应用工具审批请求的审查者。覆盖 `apps._default.approvals_reviewer`。",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此应用中工具的默认审批行为；如果存在针对单个工具的覆盖设置，则以该设置为准。",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "针对单个应用工具（例如 `repos/list`）的启用状态覆盖设置。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "针对单个应用工具的审批行为覆盖设置。",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "允许工具推荐其他可发现的连接器或插件。每个条目使用 `type = \"connector\"` 或 `\"plugin\"`，并包含一个 `id`。",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "禁用对特定可发现连接器或插件的推荐。每个条目使用 `type = \"connector\"` 或 `\"plugin\"`，并包含一个 `id`。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "启用应用（连接器）集成（稳定；默认启用）。应用和连接器的流量不受沙盒命令网络代理或其域名允许列表的控制。",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "启用从 `hooks.json` 或内联 `[hooks]` 配置加载的生命周期钩子。`features.codex_hooks` 是已弃用的别名。",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "启用代码模式功能配置。此功能仍在开发中，默认关闭。",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "代码模式从嵌套代码模式工具指引中排除、且不向执行器公开的工具命名空间。",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "代码模式仅可通过直接工具调用使用的工具命名空间。",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "启用实验性上下文管理（默认关闭）。此功能使用笔记和可搜索的历史记录来保留积累的细节，而非反复将上下文压缩为一份摘要。需要使用 Plus、Pro 或 Pro Lite 套餐的 ChatGPT 账户登录。",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "启用推演预算跟踪。此功能仍在开发中，默认关闭。启用后必须设置 `features.rollout_budget.limit_tokens`。",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "用于推演预算跟踪的 Token 上限，必须为正数。启用推演预算时必填。",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "推演预算提醒之间的 Token 间隔，必须为正数。默认为 `limit_tokens` 的 10%，且至少为 1 个 Token。",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "推演预算核算中采样 Token 的乘数，必须为有限非负数。默认为 `1.0`。",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "推演预算核算中预填充 Token 的乘数，必须为有限非负数。默认为 `1.0`。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "在 `config.toml` 中内联配置的生命周期钩子。采用与 `hooks.json` 相同的事件模式；示例和支持的事件请参阅钩子指南。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "用于 `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit`、`Stop` 或 `Interrupt` 等钩子事件的匹配器组。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "匹配器组的钩子处理程序。支持命令钩子和 MCP 工具钩子；提示钩子和智能体钩子处理程序虽会被解析，但会跳过执行。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "在后台运行命令钩子，不延迟触发该钩子的操作。默认为 `false`；`SessionEnd` 始终同步运行。请参阅[在后台运行钩子](/codex/hooks#run-hooks-in-the-background)。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "每个处理程序用于判定 `additionalContext` 过大的近似 Token 阈值。超过该阈值时，会将其保存到磁盘，并向模型显示较短的预览。默认为 `2500`；`0` 会将完整上下文直接传递给模型。请参阅[大型钩子输出](/codex/hooks#large-hook-output)。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "命令钩子的 Windows 专用命令覆盖设置。也接受 TOML 别名 `command_windows`。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "启用[记忆](/codex/customization/memories)（默认关闭）。",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "构建初始工具目录时，所有可选 MCP 服务器共用的等待时间。默认为 `1000`。设为 `0` 时，则按各服务器的 `startup_timeout_sec` 等待。",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "用于启动 MCP stdio 服务器的命令。",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "传递给 MCP stdio 服务器命令的参数。",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "转发给 MCP stdio 服务器的环境变量。",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "要加入 MCP stdio 服务器允许列表的额外环境变量。字符串条目默认为 `source = \"local\"`；`source = \"remote\"` 仅用于通过执行器运行的远程 stdio。",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "MCP stdio 服务器进程的工作目录。",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "MCP streamable HTTP 服务器的端点。",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "MCP HTTP 服务器的身份验证回退方式，优先级低于已配置的 Bearer Token 和授权标头。`oauth`（默认值）会在可用时使用已存储的 MCP OAuth 凭据。`chatgpt` 会针对受信任的第一方 ChatGPT 源站使用当前 ChatGPT 会话，然后回退到已存储的 OAuth 凭据。若无法从任何来源获取凭据，这两种模式都可在不进行身份验证的情况下连接。",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "预先注册的 OAuth 客户端 ID，用于与此 MCP 服务器进行授权和 Token 交换。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "此服务器专用的 OAuth 回调地址。预先注册的客户端在支持签发者标识，或 URL 已以此服务器专用的回调 ID 结尾时，会复用该地址。否则，Codex 会使用全局或默认回调地址，并在末尾附加该 ID。没有预先注册 ID 的客户端会在客户端注册时使用此回调地址。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "此 MCP 服务器的固定 OAuth 回调监听端口。覆盖 `mcp_oauth_callback_port`。对于 URL 中明确指定了端口的直接回环回调，请将监听端口设为相同的端口。",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "为 MCP HTTP 服务器提供 Bearer Token 的环境变量。",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "随每个 MCP HTTP 请求发送的静态 HTTP 标头。",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "输出包含 HTTP 标头名称和值的 JSON 对象的本地命令。仅支持在本地连接的 HTTP MCP 服务器。显式指定的 Bearer Token 和 OAuth 凭据优先于辅助程序提供的 Authorization 标头。",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "MCP HTTP 服务器使用的 HTTP 标头，其值从环境变量填充。",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "禁用 MCP 服务器，但不移除其配置。",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "设为 true 时，如果此已启用的 MCP 服务器无法初始化，则启动或恢复会失败。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "覆盖 MCP 服务器默认的 10 秒启动超时时间。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "以毫秒为单位的 `startup_timeout_sec` 别名。",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "覆盖 MCP 服务器中每个工具默认的 60 秒超时时间。",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "MCP 服务器所公开工具名称的允许列表。",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "在 `enabled_tools` 之后应用于 MCP 服务器的拒绝列表。",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此服务器上 MCP 工具的默认审批行为；如果存在针对单个工具的覆盖设置，则以该设置为准。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此服务器上单个 MCP 工具的审批行为覆盖设置。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "单个 MCP 工具输出的 Token 预算，尚未计入标准的 20% 序列化余量。覆盖模型针对该工具的默认输出截断预算。",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "对该 MCP 服务器进行身份验证时请求的 OAuth 作用域。",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "MCP 登录时要包含的可选 RFC 8707 OAuth 资源参数。",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "MCP 服务器的实验性运行位置设置。`remote` 会通过远程执行器环境启动 stdio 服务器；尚未实现 streamable HTTP 的远程运行。",
    },
    {
      key: "agents",
      type: "table",
      description:
        "多智能体设置和自定义角色声明。标量设置名称已被保留，不能用作自定义角色名称。",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "启用或禁用多智能体工具（默认值：true）。",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "可同时保持打开状态的已创建智能体线程数上限，不包括主线程。未设置时，由 Codex 选择默认值。",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "`agents.max_concurrent_threads_per_session` 的旧版别名。",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "创建智能体时使用的默认模型。创建时显式指定的模型优先。",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "创建智能体时使用的默认推理强度。创建时显式指定的推理强度优先。",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "智能体轮次中断时，记录一条对模型可见的消息（默认值：true）。",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Codex 在选择并创建此类型的智能体时看到的角色指引。",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "该角色对应的 TOML 配置层路径；相对路径以声明该角色的配置文件所在目录为基准解析。",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "设为 `false` 时，新创建的线程不会被存储为记忆生成的输入。默认为 `true`。",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "设为 `false` 时，Codex 不会将现有记忆注入后续会话。默认为 `true`。",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "为 `true` 时，使用 MCP 工具调用、网页搜索或工具搜索等外部上下文的线程不会用于生成记忆。默认值为 `false`。旧版别名：`memories.no_memories_if_mcp_or_web_search`。",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "为全局整合保留的近期原始记忆的最大数量。默认值为 `256`，上限为 `4096`。",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "记忆自上次使用以来仍可参与整合的最长天数。默认值为 `30`，取值限制在 `0`-`365` 范围内。",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "可用于生成记忆的线程的最长存续时间。默认值为 `30`，取值限制在 `0`-`90` 范围内。",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "每次启动处理的候选运行轨迹的最大数量。默认值为 `16`，上限为 `128`。",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "线程可用于生成记忆之前必须达到的最短空闲时间。默认值为 `6`，取值限制在 `1`-`48` 范围内。",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "开始生成记忆前，Codex 速率限制窗口中所需的最低剩余百分比。默认值为 `25`，取值限制在 `0`-`100` 范围内。",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "用于逐线程提取记忆的可选模型覆盖值。",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "用于全局记忆整合的可选模型覆盖值。",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "使用基于 PTY 的统一 exec 工具（稳定功能；除 Windows 外，默认启用）。",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "为 shell 环境创建快照，以加快重复命令的执行（稳定功能；默认开启）。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "启用多智能体协作工具（`spawn_agent`、`send_input`、`resume_agent`、`wait_agent` 和 `close_agent`）（稳定功能；默认开启）。",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "启用目标持久化和自动继续功能（稳定功能；默认开启）。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "启用远程插件目录（稳定功能；默认开启）。",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "启用个性选择控件（稳定功能；默认开启）。",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "启动沙盒命令的网络代理（实验性功能；默认关闭）。要强制执行权限配置方案中的域名规则，必须启用此功能，除非已启用的管理员托管 `experimental_network` 要求启动了代理。设置 `domains` 等功能级策略选项时，请使用表形式。该代理不会过滤网页搜索、应用、MCP 或其他托管工具。",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "在启用命令网络访问时，启动沙盒命令的网络代理。默认值为 `false`；代理关闭时，不会强制执行权限配置方案中的域名规则。",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "沙盒网络的域名策略。默认未设置，这意味着在添加 `allow` 规则之前，不允许访问任何外部目标。支持精确主机匹配、仅匹配子域名的 `*.example.com`、匹配根域名及其子域名的 `**.example.com`，以及全局 `*` 允许规则；建议优先使用限定范围的规则，因为 `*` 会广泛开放公网出站访问。添加 `deny` 规则可阻止访问相应目标；发生冲突时以 `deny` 为准。",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "沙盒网络的 Unix 套接字策略。默认未设置；请为允许使用的套接字添加 `allow` 条目。",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "允许更广泛地访问本地或私有网络。默认值为 `false`；精确匹配本地 IP 字面量或 `localhost` 的允许规则仍可放行特定本地目标。",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "提供 SOCKS5 支持。默认值为 `true`。",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "允许通过 SOCKS5 使用 UDP。默认值为 `true`。",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "允许通过环境中指定的上游代理进行链式转发。默认值为 `true`。",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允许使用非环回监听地址。默认值为 `false`；启用后，代理监听器可能会向 localhost 以外开放。",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允许访问任意 Unix 套接字目标，而不再仅限允许列表中的目标。默认值为 `false`；请仅在严格受控的环境中使用。",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "沙盒网络的 HTTP 监听器 URL。默认值为 `\"http://127.0.0.1:3128\"`。",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "SOCKS5 监听器 URL。默认值为 `\"http://127.0.0.1:8081\"`。",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "已弃用的旧版开关；请优先使用顶层 `web_search` 设置。",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "已弃用的旧版开关。未设置 `web_search` 时，true 会映射为 `web_search = \"cached\"`。",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "已弃用的旧版开关。未设置 `web_search` 时，true 会映射为 `web_search = \"live\"`。",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "启用用于运行命令的默认 `shell` 工具（稳定功能；默认开启）。",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "在支持的情况下，使用 zstd 压缩流式请求体（稳定功能；默认开启）。",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "允许在技能缺少 MCP 依赖项时发出提示并安装这些依赖项（稳定功能；默认开启）。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "在 TUI 中启用模型目录中的服务层级选择功能，包括在当前模型声明支持时启用快速层级命令（稳定功能；默认开启）。",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "在轮次运行期间阻止计算机进入睡眠状态（实验性功能；默认关闭）。",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "不显示启用开发中功能标志时出现的警告。",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "自定义提供商的定义。内置提供商 ID（`openai`、`ollama` 和 `lmstudio`）为保留项，不能覆盖。",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "自定义模型提供商的显示名称。",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "模型提供商的 API 基础 URL。",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "提供商 API 密钥所在的环境变量。",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "提供商 API 密钥的可选设置说明。",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "直接指定的提供商 Bearer Token（不建议使用；请改用 `env_key`）。",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "该提供商使用 OpenAI 身份验证（默认值为 false）。",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "提供商使用的协议。`responses` 是唯一受支持的值，省略时也默认使用该值。",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "附加到提供商请求的额外查询参数。",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "添加到提供商请求的静态 HTTP 标头。",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "存在相应环境变量时，使用其值填充的 HTTP 标头。",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "向提供商发起 HTTP 请求时的重试次数（默认值：4）。",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "SSE 流中断后的重试次数（默认值：5）。",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "SSE 流的空闲超时时间，单位为毫秒（默认值：300000）。",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "该提供商是否支持 Responses API 的 WebSocket 传输方式。",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "声明支持兼容的独立网页搜索端点（默认值：false）。独立搜索仍在开发中，默认关闭；仅具备提供商兼容性不会启用该功能。",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "自定义提供商通过命令获取 Bearer Token 的配置。请勿与 `env_key`、`experimental_bearer_token` 或 `requires_openai_auth` 结合使用。",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Codex 需要 Bearer Token 时要运行的命令。该命令必须将 Token 输出到 stdout。",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "传递给 Token 获取命令的参数。",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Token 获取命令的最长运行时间，单位为毫秒（默认值：5000）。",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Codex 主动刷新 Token 的间隔，单位为毫秒（默认值：300000）。设置为 `0` 后，仅在身份验证重试后刷新。",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Token 获取命令的工作目录。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "内置 `amazon-bedrock` 提供商使用的 AWS 配置方案名称。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "内置 `amazon-bedrock` 提供商使用的 AWS 区域。",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "调整受支持模型的推理强度（仅限 Responses API；`xhigh` 是否可用取决于模型）。",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "计划模式专用的推理强度覆盖值。未设置时，计划模式使用其内置预设的默认值。",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "选择推理摘要的详细程度，或完全禁用摘要。",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "可选的 GPT-5 Responses API 输出详细程度覆盖值；未设置时，使用选定模型或预设的默认值。",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "强制 Codex 发送或不发送推理元数据。",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "创建子进程时的基本环境继承策略。",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "在运行其他过滤器之前，保留名称中包含 KEY、SECRET 或 TOKEN 的变量（默认：true）。设置为 false 可按敏感信息相关名称自动排除变量。",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "标准的环境变量模式过滤器，不区分大小写。包含条目构成允许列表，无法恢复已排除的值。显式 `set` 值在排除操作之后应用。不要在同一配置层中将这些过滤器与旧版 `exclude` 或 `include_only` 数组混用。",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "旧版环境变量排除模式。新配置请使用 `shell_environment_policy.filters`；不要在同一配置层中混用这两种形式。",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "旧版环境变量模式允许列表。新配置请使用 `shell_environment_policy.filters`；不要在同一配置层中混用这两种形式。",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "在排除操作之后注入的显式环境变量值；包含过滤器仍可移除这些值。",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "创建子进程时使用用户的 shell 配置文件。",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "项目根目录标记文件的文件名列表；用于在父目录中查找项目根目录。",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "构建项目指令时，从 `AGENTS.md` 读取的最大字节数。",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "`AGENTS.md` 缺失时尝试查找的其他文件名。",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "控制 Codex 是否将会话记录保存到 history.jsonl。",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "在历史记录中存储单个工具或函数输出时的 Token 预算。",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "空 `write_stdin` 轮询（后台终端轮询）的最长等待时间，以毫秒为单位。默认值为 `300000`（5 分钟）。取代旧的 `background_terminal_timeout` 键。",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "设置后，通过删除最早的条目，将历史记录文件大小限制在指定字节数以内。",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "用于打开 Codex 输出中引用内容的 URI 方案（默认：`vscode`）。",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "添加到所发出的 OpenTelemetry 事件上的环境标签（默认：`dev`）。",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "选择 OpenTelemetry 导出器并提供端点元数据。",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "选择 OpenTelemetry 跟踪导出器并提供端点元数据。",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "选择 OpenTelemetry 指标导出器（默认为 `statsig`）。",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "选择将原始用户提示随 OpenTelemetry 日志一同导出。",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 日志的导出器端点。",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 导出器使用的协议。",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 导出器请求中包含的静态标头。",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 日志的跟踪导出器端点。",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 跟踪导出器使用的协议。",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 跟踪导出器请求中包含的静态标头。",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 导出器 TLS 使用的 CA 证书路径。",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 导出器 TLS 使用的客户端证书路径。",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 导出器 TLS 使用的客户端私钥路径。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 跟踪导出器 TLS 使用的 CA 证书路径。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 跟踪导出器 TLS 使用的客户端证书路径。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 跟踪导出器 TLS 使用的客户端私钥路径。",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "仅限用户级配置。为 ChatGPT 桌面应用定义额外的**打开方式**目标。有关示例和处理程序 ID 限制，请参阅[添加自定义文件处理程序](/codex/config-file/config-advanced#add-custom-file-handlers)。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "在**打开方式**菜单中显示的名称。必填。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "处理程序图标的内置资源路径、采用 Base64 编码的 `data:image/...` URL、文件 URI 或本地绝对路径。必填；如果图标来源不受支持，则使用默认的 VS Code 图标。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "要检测并启动的可执行文件路径或命令名称。必填。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "插入到命令与文件输入之间的参数（默认：`[]`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "应用向处理程序发送文件输入的方式（默认：`path`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "为 SSH 工作空间中的文件提供该处理程序（默认：`false`）。",
    },
    {
      key: "tui",
      type: "table",
      description:
        "TUI 专用选项，例如启用内嵌桌面通知。",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "启用 TUI 通知；可选择将其限制为特定事件类型。",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "终端通知的发送方式（默认：auto）。",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "控制 TUI 通知是仅在终端失去焦点时触发，还是无论焦点状态如何都触发。默认为 `unfocused`。",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "启用终端动画（欢迎屏幕、微光效果、旋转指示器）（默认：true）。",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "控制 TUI 是否使用备用屏幕（默认：auto；为保留滚动回溯记录，auto 在 Zellij 中不会使用备用屏幕）。",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "恢复或派生会话时使用的工作目录。未设置时，如果您当前的目录与会话中保存的目录不同，Codex 会提示您选择。",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "让编辑器启动时进入 Vim 普通模式，而不是插入模式（默认：false）。您仍可在各个会话中使用 `/vim` 切换。",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "以原始滚动回溯模式启动 TUI，便于在终端中选择并复制文本（默认：false）。您可以使用 `/raw` 或默认的 `alt-r` 按键绑定切换该模式。",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "在 TUI 欢迎屏幕中显示新用户引导提示（默认：true）。",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "TUI 底部状态行中各项标识符的有序列表。`null` 会禁用状态行。",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "终端窗口或标签页标题中各项标识符的有序列表。默认为 `[\"spinner\", \"project\"]`；`null` 会禁用标题更新。",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "语法高亮主题覆盖设置（主题名称采用 kebab-case 格式）。",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "TUI 操作的键盘快捷键绑定。支持的上下文包括 `global`、`chat`、`composer`、`editor`、`vim_normal`、`vim_operator`、`vim_text_object`、`pager`、`list` 和 `approval`。部分编辑器操作会回退到匹配的 `tui.keymap.global` 绑定；如果支持特定上下文的绑定，则优先使用这些绑定。",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "取消该操作在相应键位映射上下文中的绑定。按键名称使用规范化字符串，例如 `ctrl-a`、`shift-enter`、`page-down` 或 `minus`。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "在不更改插件清单的情况下，启用或禁用已安装插件附带的 MCP 服务器。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "插件提供的 MCP 服务器上各工具的默认审批行为。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "插件提供的 MCP 服务器所公开工具的允许列表。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "插件提供的 MCP 服务器的拒绝列表，在 `enabled_tools` 之后应用。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "插件提供的单个 MCP 工具的审批行为覆盖设置。",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "以模型 Slug 为键的内部启动提示状态。",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "在 TUI 和 `codex exec` 输出中隐藏推理事件。",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "当前模型输出原始推理内容时，将其显示出来。",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "禁用 TUI 中的突发粘贴检测。",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "记录是否已确认 Windows 入门引导（仅限 Windows）。",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "覆盖 ChatGPT 登录流程中使用的基础 URL。",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "控制 CLI 缓存凭据的存储位置（auth.json 文件或操作系统钥匙串）。",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "MCP OAuth 凭据的首选存储位置。",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "可选的全局固定端口，用于 MCP OAuth 登录期间的本地 HTTP 回调服务器。服务器专用的 `oauth.callback_port` 优先。如果两者均未设置，Codex 会绑定到操作系统选择的临时端口。",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "可选的 MCP OAuth 登录基础回调 URL，例如 devbox 入口 URL。当授权服务器支持颁发者识别时，新添加的预注册客户端会原样使用此 URL；未保存回调的现有客户端则会附加服务器专用的回调 ID。如果不支持颁发者识别，任何已预注册的 MCP 服务器只要其配置的回调缺少必需的 ID，就会回退到此 URL 并附加该 ID。回调 URL 中的端口不会决定监听端口。",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "用于启用统一执行功能的旧名称；请优先使用 `[features].unified_exec` 或 `codex --enable unified_exec`。",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "可选的网页搜索工具配置。对象形式可设置搜索上下文大小、允许搜索的域名和用户的大致位置。这些搜索域名过滤器独立于沙盒命令的网络域名规则，不会限制连接器或 MCP 服务器。",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "启用本地图像附件工具 `view_image`。",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "网页搜索模式（默认值：`\"cached\"`；cached 使用 OpenAI 维护的索引，不访问外部网页；indexed 仅允许经搜索索引准许的外部访问；如果您使用 `--yolo` 或其他授予完全访问权限的沙盒设置，则默认值为 `\"live\"`）。使用 `\"live\"` 进行不受限制的实时检索，或使用 `\"disabled\"` 移除此工具。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "应用于沙盒工具调用的默认权限配置方案名称。内置配置方案为 `:read-only`、`:workspace` 和 `:danger-full-access`；自定义配置方案名称需要有对应的 `[permissions.<name>]` 表。请勿与 `sandbox_mode` 或 `[sandbox_workspace_write]` 同时使用。",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "此命名配置方案的易读描述。配置方案不会通过 `extends` 继承父配置方案的描述。",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "可选的父配置方案，在此命名配置方案之前应用。可将其设为另一个命名配置方案、`:read-only` 或 `:workspace`；不允许使用 `:danger-full-access`、未定义的父配置方案或循环继承。",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "配置方案定义的工作空间根目录。这些目录与会话的运行时工作空间根目录都适用 `:workspace_roots` 文件系统规则。",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "为 `true` 时，将路径纳入该配置方案的工作空间根目录集合。已禁用的条目仍不生效。",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "命名的文件系统权限配置方案。每个键都是绝对路径或特殊 Token，例如 `:minimal` 或 `:workspace_roots`。",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "在沙盒启动前对匹配结果生成快照的平台上，展开拒绝读取的 glob 模式时所用的最大深度。如果设置此项，其值必须至少为 `1`。",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "为路径、glob 模式或特殊 Token 授予直接访问权限，或将嵌套条目的作用域限定在该根路径下。使用 `\"deny\"` 拒绝读取匹配的路径。",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "相对于每个生效的工作空间根目录设置的文件系统访问权限。使用 `\".\"` 表示根目录本身；对于 `\"**/*.env\"` 等 glob 子路径，可使用 `\"deny\"` 拒绝读取。",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "为此权限配置方案中的命令启用网络访问。此设置不会启动网络代理。如果既未启用 `features.network_proxy`，也未启用管理员管理的网络要求，命令将直接访问网络，且不会强制执行配置方案的域名规则。",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "此权限配置方案启用沙盒网络时使用的 HTTP 监听器 URL。",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "此权限配置方案启用沙盒网络时提供 SOCKS5 支持。",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "此权限配置方案使用的 SOCKS5 代理端点。",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "启用后，允许通过 SOCKS5 监听器传输 UDP。",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "允许沙盒网络通过另一个上游代理进行链式转发。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允许沙盒网络监听器绑定非环回地址。启用后，localhost 以外的主机可能也能访问这些监听器。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允许访问任意 Unix 套接字目标，而不局限于默认的受限集合。仅在严格受控的环境中使用。",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "子进程流量使用的网络代理模式。",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "沙盒命令的域名规则。仅当 `features.network_proxy` 或已启用的管理员管理的网络要求激活代理时，才会强制执行。支持精确匹配的主机、`*.example.com`、`**.example.com` 和全局 `*` 允许规则；`deny` 优先。不限制网页搜索、应用或 MCP 服务器。",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "允许或拒绝精确匹配的主机，或 `*.example.com`、`**.example.com` 等限定范围的通配符模式。",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "沙盒网络的 Unix 套接字允许列表覆盖项。以套接字路径为键；`allow` 添加路径，`deny` 拒绝路径。",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "使用 `allow` 将 Unix 套接字绝对路径添加到生效的允许列表，或使用 `deny` 拒绝该路径。被拒绝的条目不会纳入生效的允许列表。",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "允许沙盒网络更广泛地访问本地网络或私有网络。即使此项保持为 `false`，针对精确本地 IP 字面值或 `localhost` 的允许规则仍可允许访问特定本地目标。",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "将项目或工作树标记为受信任或不受信任（`\"trusted\"` | `\"untrusted\"`）。不受信任的项目会跳过项目范围的 `.codex/` 配置层，包括项目本地的配置、钩子和规则。",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "记录是否已确认完全访问权限警告提示。",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "记录是否已确认有关 Windows 目录对所有用户可写的警告。",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "记录是否已选择不再显示速率限制下的模型切换提醒。",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "记录是否已确认 GPT-5.1 迁移提示。",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "记录是否已确认 gpt-5.1-codex-max 迁移提示。",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "以 old->new 映射的形式记录已确认的模型迁移。",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "将 Codex 限制为只能使用特定的身份验证方式。",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "将 ChatGPT 登录限制在指定标识符对应的工作空间内。",
    },
  ]}
  client:load
/>

您可以在[此处](/codex/config-schema.json)找到 `config.toml` 的最新 JSON 模式。

在 VS Code 或 Cursor 中编辑 `config.toml` 时，如需使用自动补全和诊断功能，您可以安装 [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) 扩展程序，并在 `config.toml` 顶部添加下面这一行：

```toml
#:schema https://developers.openai.com/codex/config-schema.json

注意：请将 `experimental_instructions_file` 重命名为 `model_instructions_file`。Codex 已弃用旧键；请在现有配置中改用新名称。

## `requirements.toml`

`requirements.toml` 是由管理员强制执行的配置文件，用于限制安全敏感设置，且用户无法覆盖这些限制。有关详细说明、文件位置和示例，请参阅[管理员强制执行的要求](/zh-Hans/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

对于 ChatGPT Business 和 ChatGPT Enterprise 用户，Codex 还可以应用从云端获取的要求。
有关优先级的详细信息，请参阅安全页面。

在 `requirements.toml` 中使用 `[features]`，通过与 `config.toml` 相同的规范键名固定运行时功能标志。
要求中也可以包含文档列明的应用专用键，
这些键不属于 `config.toml`。
未指定的键仍不受约束。

部分托管要求会强制使用确切的配置值，而不是允许列表。
用户无法覆盖强制指定的路径、更新偏好设置、登录 Shell 策略、
反馈设置或 Windows 私有桌面设置。

托管权限配置方案允许列表需要 Codex 0.138.0 或更高版本。
Codex 0.137.0 及更早版本会忽略 `allowed_permission_profiles`
和托管的 `default_permissions`。

请将 `allowed_sandbox_modes` 与 `sandbox_mode` 配合使用。
对于采用权限配置方案的部署，
请将 `allowed_permission_profiles` 与托管的 `default_permissions` 配合使用。

`[models.new_thread]` 表提供托管默认值，而非强制设置。
通过专用 CLI 标志或 `--config` 覆盖项显式指定的启动选项具有更高优先级。
显式指定模型或推理强度覆盖项时，会跳过两个托管模型字段；
`service_tier` 独立于这些字段。

浏览器要求涵盖三个独立的操作界面。
`in_app_browser` 控制用户直接打开并使用的浏览器面板。
`browser_use` 控制智能体在浏览器中执行的操作。
`computer_use` 控制智能体在原生桌面应用中执行的操作。

嵌套的浏览器和计算机使用策略值本身不会授予访问权限。
针对特定来源或应用设置的 `allow` 可以覆盖同一策略来源中的回退值，
但常规的功能、审批和其他策略检查仍然适用。
当托管要求和 `config.toml` 同时适用时，
任一方的 `deny` 均优先。

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "强制指定 Codex 存储基于 SQLite 的运行时状态的目录。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "强制指定 Codex 写入本地日志文件的目录。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "强制指定 Codex 启动时使用的 JSON 模型目录。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "强制规定 Codex 启动时是否检查更新。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "强制规定 Shell 工具是否可以启动登录 Shell。",
    },
    {
      key: "feedback",
      type: "table",
      description: "托管反馈设置。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "强制规定用户能否在各 Codex 客户端中提交反馈。",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "`approval_policy` 的允许值（例如 `untrusted`、`on-request`、`never` 和 `granular`）。",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "`approvals_reviewer` 的允许值，例如 `user` 和 `auto_review`。",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "用于自动审查的托管 Markdown 策略指令。其优先级高于本地的 `[auto_review].policy`。空白值将被忽略。",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "允许使用的权限配置方案的完整列表。设为 `true` 的配置方案允许使用。省略或设为 `false` 的配置方案均禁止使用，包括未来版本新增的配置方案。合并多个要求配置来源时，按配置方案名称匹配条目。",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "允许或禁止使用已加载的配置或要求配置来源中定义的内置或自定义权限配置方案。后加载且优先级更高的要求配置来源可以使用 `false`，禁用先前优先级较低的来源所允许的配置方案。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "托管的默认权限配置方案。该配置方案必须在 `allowed_permission_profiles` 中被允许。请显式设置此项，以确保行为可预测；如果省略，只有在 `:workspace` 和 `:read-only` 均被显式允许时，Codex 才会默认使用 `:workspace`。",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "要求 Codex 服务流量使用受支持的数据驻留区域。目前接受 `us`。",
    },
    {
      key: "models",
      type: "table",
      description:
        "新线程的托管模型默认值。这些值优先于用户和项目默认值，但为新线程显式选择的设置可以覆盖它们。",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "启动新的本地线程时应用的默认值。每项模型设置均为可选。",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "新线程的默认模型。通过 `--model` 显式指定的模型，或通过 `--config` 显式指定的模型或推理覆盖设置优先。",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "新线程的默认推理强度。显式指定模型或推理强度覆盖设置时，会跳过这两个托管模型字段。",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "新线程的默认服务层级。显式指定的服务层级覆盖设置优先，且独立于模型字段生效。",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "以配置方案名称为键的管理员定义的权限配置方案。使用与 `config.toml` 相同的配置方案字段。",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "管理员定义的权限配置方案。名称不能以 `:` 开头，不能使用保留名称 `filesystem`，也不能与已加载配置中的配置方案重名。使用与 `config.toml` 相同的配置方案字段；完整的配置方案模式请参阅权限指南。",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "`sandbox_mode` 的允许值。",
    },
    {
      key: "windows",
      type: "table",
      description: "原生 Windows 沙盒要求。",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "`windows.sandbox` 允许使用的原生 Windows 沙盒实现（`elevated` 和 `unelevated`）。列表不能为空。如果两者均被允许且未选择模式，Codex 会优先使用 `elevated`。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "强制设定原生 Windows 沙盒是否在私有桌面上启动其子进程。",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "主机专属沙盒要求。`hostname_patterns` 与解析得到的主机名匹配的第一个条目，会覆盖该要求配置来源中的顶层 `allowed_sandbox_modes`。主机专属条目目前仅覆盖沙盒模式。",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "不区分大小写的主机名模式。支持用 `*` 匹配任意字符序列，用 `?` 匹配单个字符。",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "此主机专属条目匹配时允许使用的沙盒模式。",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "`web_search` 的允许值（`disabled`、`cached`、`indexed`、`live`）。始终允许 `disabled`；空列表实际上只允许 `disabled`。",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "设为 `true` 时，Codex 会跳过用户、项目、会话和插件钩子，但仍允许来自 `requirements.toml` 和其他托管配置层的托管钩子。",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "设为 `false` 可为受管理用户禁用应用快照。如果省略，应用快照不受要求配置限制，并遵循产品正常的可用性规则。",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "设为 `false` 可为受管理用户禁用设备远程控制。如果省略，设备远程控制不受要求配置限制，并遵循产品正常的可用性规则。",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "设为 `false` 可同时禁用智能体驱动的浏览器功能和面向原生应用的计算机使用功能。设为 `true` 或省略此项并不会启用这两项功能；其余功能、策略和审批检查仍然适用。",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "在云端托管的 `requirements.toml` 中设为 `false`，可禁用在工作空间内共享本地构建插件的功能。",
    },
    {
      key: "features",
      type: "table",
      description:
        "固定的功能配置值。运行时功能应使用 `config.toml` 中的规范名称；此处也支持文档中列出的应用专属要求配置键。",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "要求文档中列出的运行时功能或应用功能保持启用或禁用状态。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "将受管理用户的应用集成功能固定为启用或禁用状态。",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false` 可禁用应用内更新。如果省略此要求，更新默认保持启用。",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false`，可禁用由用户直接打开和操控的内置浏览器窗格。",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false`，可禁用智能体驱动的浏览器功能。",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false`，可阻止 Codex 通过 ChatGPT 浏览器扩展程序操作受支持的浏览器，包括现有标签页和已登录的会话。",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false` 可禁用本地运行时对 Chrome DevTools Protocol 的完整访问，包括浏览器开发者模式，并阻止 ChatGPT 桌面应用启用对应设置。如果省略，则遵循产品正常的可用性规则。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "对受管理用户，将规范名称为 `fast_mode` 的功能固定为启用或禁用状态。",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "将受管理用户的 Guardian 审批功能固定为启用或禁用状态。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "将受管理用户的记忆功能固定为启用或禁用状态。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "将受管理用户的多智能体功能固定为启用或禁用状态。",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "将受管理用户的插件功能固定为启用或禁用状态。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "将受管理用户的远程插件目录固定为启用或禁用状态。",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "在 `requirements.toml` 中设为 `false` 可禁用计算机使用、录制与重放以及相关的安装或启用流程。",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "对受管理用户，将随附的工作空间依赖项运行时固定为启用或禁用状态。",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "内置浏览器窗格的要求配置。这些设置不控制智能体驱动的浏览器功能。",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "设为 `false` 可阻止用户将外部浏览器的设置或浏览数据导入内置浏览器。设为 `true` 或省略此项时，只要其他产品检查允许，导入功能就仍然可用。此设置仅可由管理员管理，无法通过 `config.toml` 覆盖。",
    },
    {
      key: "browser_use",
      type: "table",
      description: "智能体驱动的浏览器功能的托管要求配置。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "设为 `false` 可阻止浏览器功能读取浏览器历史记录。设为 `true` 或省略此项时，常规历史记录设置和可用性检查仍然适用。",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "设为 `true` 可跳过浏览器功能的自动审查，改为请求用户审批。设为 `false` 或省略此项时，只要其他设置允许，自动审查就仍然可用。",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "设为 `false` 可阻止浏览器功能创建或采用覆盖所有站点的 `Always allow` 审批，例如允许从任意站点下载。已保存的审批会被忽略，但不会被删除。设为 `true` 或省略此项并不会创建审批。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "如果 `browser_use.origins` 下没有匹配的条目定义某项浏览器设置，则使用此处的回退值。匹配的来源规则会替换该配置来源中的回退值。随后，Codex 会采用托管要求配置和用户配置中更严格的结果。",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "使用 `deny` 可对采用回退规则的来源禁用浏览器功能。被拒绝的来源也会禁止上传、下载、完整的浏览器调试访问和自动审查。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止浏览器功能从采用回退规则的来源下载。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止浏览器功能向采用回退规则的来源上传。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "使用 `deny` 可对采用回退规则的来源禁止完整的 Chrome DevTools Protocol（CDP）访问。`allow` 仅允许继续进行常规的用户主动启用检查和审批检查。",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "使用 `deny` 可对采用回退规则的来源跳过自动审查，改为请求用户审批。设为 `allow` 时，只要其他设置允许，自动审查就仍然可用。",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "设为 `false` 可阻止浏览器功能为采用回退规则的来源保存或采用 `Always allow` 审批。针对当前轮次或线程的审批仍可生效。设为 `true` 时，只要其他条件允许，`Always allow` 就可用，但此设置本身不会创建审批。",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "设置非持久性站点访问审批的有效期：`turn` 将其限制为当前轮次，`thread` 则使其在当前线程的剩余时间内保持有效。`persistent_approval` 单独控制 `Always allow` 是否可用。产品默认值为 `thread`。",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "针对特定来源的浏览器策略。键使用 `<scheme>://<host-pattern>[:<port>]` 格式，协议为 `http` 或 `https`。可使用精确主机名、仅匹配子域名的 `*.example.com`，或匹配根域名及其子域名的 `**.example.com`。其他 `*` 通配符可以跨点号匹配，因此 `region*.example.com` 也匹配 `region.api.example.com`；主机部分为 `*` 时，会匹配该协议下的所有主机。协议和非默认端口会影响匹配；显式指定的默认端口会在规范化时移除。路径、查询参数、内嵌用户名或密码，以及协议或端口中的通配符均无效。在 TOML 中，请用引号括起模式，例如 `[browser_use.origins.\"https://**.example.com\"]`。",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "适用于匹配此模式的来源的策略。如果多个模式匹配，Codex 会对每项能力采用限制最严格的值：`deny` 优先于 `allow`，`false` 优先于 `true`，`turn` 优先于 `thread`。",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "使用 `deny` 可对匹配的来源禁用浏览器功能。拒绝访问也会禁止这些来源上的上传、下载、完整的浏览器调试访问和自动审查。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止浏览器功能从匹配的来源下载。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止浏览器功能向匹配的来源上传。`allow` 仅允许继续进行常规审批和策略检查。",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "使用 `deny` 可对匹配的来源禁止完整的 Chrome DevTools Protocol（CDP）访问。`allow` 仅允许继续进行常规的用户主动启用检查和审批检查。",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "使用 `deny` 可对匹配的来源跳过自动审查，改为请求用户审批。设为 `allow` 时，只要其他设置允许，自动审查就仍然可用。",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "设为 `false` 可阻止浏览器功能为匹配的来源保存或采用 `Always allow` 审批。针对当前轮次或线程的审批仍可生效。设为 `true` 时，只要其他条件允许，`Always allow` 就可用，但此设置本身不会创建审批。",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "设置匹配来源的非持久性站点访问审批的有效期：`turn` 将其限制为当前轮次，`thread` 则使其在当前线程的剩余时间内保持有效。`persistent_approval` 单独控制 `Always allow` 是否可用。",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "适用于智能体在原生桌面应用中执行工作的托管要求配置。托管应用规则和 `config.toml` 应用规则均会强制执行；应用必须获得每个策略来源的允许。",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "设为 `false` 可阻止用户在受管理的 macOS 设备上启用锁定后使用功能。此要求会移除启用控件；如果该功能已启用，则不会将其关闭。省略时，遵循产品的正常可用性设置。",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "设为 `false` 可移除跨会话保存应用审批的选项。当前会话的审批仍然可用。设为 `true` 或省略此项并不代表批准访问应用。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "未匹配任何平台专属规则的原生应用所使用的回退访问策略。`deny` 会阻止访问。`allow` 仅允许继续进行正常的审批和策略检查。产品默认值为 `allow`。",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "适用于 macOS 的计算机使用应用规则。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "将精确的 macOS 捆绑包标识符映射到 `allow` 或 `deny`。匹配的规则会替代同一策略来源中的 `computer_use.default_app_access`。托管要求或用户配置中只要有一方拒绝访问，访问仍会被阻止。",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止访问与该捆绑包标识符精确匹配的应用。`allow` 仅覆盖此策略来源的默认值，仍需其他所有策略来源及正常审批流程允许访问该应用。",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "适用于已打包和未打包 Windows 应用的计算机使用应用规则。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "将已签名的打包应用所注册的精确应用程序用户模型 ID（AUMID）映射到 `allow` 或 `deny`。匹配的规则会替代同一策略来源中的 `computer_use.default_app_access`。",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "使用 `deny` 可阻止访问与该打包应用身份精确匹配的应用。`allow` 仅覆盖此策略来源的默认值，仍需其他所有策略来源及正常审批流程允许访问该应用。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "适用于已签名、未打包的 Windows 可执行文件的规则。规则匹配可执行文件经验证的发布者和已签名的版本信息，而非其路径或当前文件名。匹配的拒绝规则优先于匹配的允许规则。未签名的可执行文件使用 `computer_use.default_app_access`；无法明确验证签名身份的可执行文件会被阻止。",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "必填的精确发布者名称，取自可执行文件的受信任签名证书，采用 Windows X.500 可分辨名称格式。",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "必填的精确 `ProductName`，取自可执行文件已签名的版本信息。",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "可选的 `OriginalFilename`，取自可执行文件已签名的版本信息。匹配不区分大小写。如果匹配发布者和产品的规则要求提供此值，但可执行文件未提供，计算机使用会阻止该可执行文件。",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "必填，用于决定是否允许访问匹配的可执行文件。`deny` 会阻止访问。`allow` 仅覆盖此策略来源的默认值，仍需其他所有策略来源及正常审批流程允许访问该应用。",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "由管理员管理的沙盒内本地命令网络要求，通过 `requirements.toml` 强制执行。启用后，这些要求无需 `features.network_proxy` 即可启动命令网络代理。浏览器工具会单独检查托管的网络拒绝规则和排他性允许列表。这些要求不会将浏览器流量路由到代理，也不控制网页搜索、应用、MCP 服务器、原生应用流量或 Codex 云端网络。",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "启用沙盒网络要求。如果当前沙盒仍禁止命令联网，此设置不会授予网络访问权限。",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "`[experimental_network]` 要求使用的回环 HTTP 监听端口。",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "`[experimental_network]` 要求使用的回环 SOCKS5 监听端口。",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "允许沙盒网络通过环境中配置的上游代理进行链式连接。",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允许 `[experimental_network]` 要求使用非回环监听地址。启用后，localhost 以外的设备也可能访问这些监听器。",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允许访问任意 Unix 套接字目标，而不局限于允许列表。仅应在严格受控的环境中使用。",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "以映射形式定义的沙盒网络管理员域名策略。支持精确主机名、仅匹配子域名的 `*.example.com`、同时匹配根域名和子域名的 `**.example.com`，以及全局 `*` 允许规则；建议使用限定范围的规则，因为 `*` 会广泛开放公网出站访问。发生冲突时，`deny` 优先。请勿与 `experimental_network.allowed_domains` 或 `experimental_network.denied_domains` 同时使用。",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "启用托管网络代理时，适用于沙盒内命令联网的管理员允许规则。这些规则不适用于网页搜索、应用或 MCP 服务器。请勿与 `experimental_network.domains` 同时使用。",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "以列表形式定义的沙盒网络管理员拒绝规则。请勿与 `experimental_network.domains` 同时使用。",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "设为 `true` 时，在沙盒网络要求生效期间，只有管理员管理的允许规则有效；用户添加的允许列表条目会被忽略。即使没有托管的允许规则，用户添加的域名允许规则也不会生效。",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "由管理员管理的沙盒网络 Unix 套接字策略。",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "允许沙盒网络更广泛地访问本地网络或私有网络。即使此项保持为 `false`，精确匹配本地 IP 字面量或 `localhost` 的允许规则仍可允许访问特定本地目标。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "由管理员强制执行的托管生命周期钩子。需要指定托管钩子目录，并使用与 `config.toml` 中内联 `[hooks]` 相同的事件模式。",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "macOS 和 Linux 上存放托管钩子脚本的目录。加载托管钩子前，Codex 会验证该目录使用绝对路径且确实存在。",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Windows 上存放托管钩子脚本的目录。加载托管钩子前，Codex 会验证该目录使用绝对路径且确实存在。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "钩子事件的匹配器组，例如 `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit` 或 `Stop`。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "匹配器组的钩子处理程序。支持命令钩子和 MCP 工具钩子；提示钩子和智能体钩子的处理程序会被解析，但会跳过执行。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "在后台运行命令钩子，不延迟触发该钩子的操作。默认为 `false`；`SessionEnd` 始终同步运行。请参阅[在后台运行钩子](/codex/hooks#run-hooks-in-the-background)。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "每个处理程序的大致 Token 阈值，超过此阈值时会将过大的 `additionalContext` 保存到磁盘，并向模型显示较短的预览。默认为 `2500`；设为 `0` 会将完整上下文直接传给模型。请参阅[较大的钩子输出](/codex/hooks#large-hook-output)。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "仅适用于 Windows 的命令钩子命令覆盖设置。也接受 TOML 别名 `command_windows`。",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "由管理员强制执行的文件系统读取拒绝规则。条目可以是路径或 glob 模式，用户无法通过本地配置放宽这些限制。",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "允许启用的 MCP 服务器列表。只有服务器名称（`<id>`）和身份均匹配时，才能启用该 MCP 服务器。已配置的 MCP 服务器如果不在允许列表中或身份不匹配，都会被禁用。",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "单个 MCP 服务器的身份规则。设置 `command`（stdio）或 `url`（流式 HTTP）之一。",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "通过精确匹配命令字符串来允许 MCP stdio 服务器，或使用匹配器表要求可执行文件精确匹配，并按顺序匹配参数。字符串形式不会检查参数、`cwd`、`env` 或 `env_vars`。",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "stdio 服务器配置的 `command` 必须精确匹配的可执行文件。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "stdio 服务器的有序参数匹配器。配置的参数列表必须与匹配器列表长度相同，且每个位置都必须匹配。命令匹配器不会检查 `cwd`、`env` 或 `env_vars`。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "此参数位置的匹配操作。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "`exact` 或 `prefix` 参数匹配器使用的值。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 参数匹配器使用的正则表达式。该表达式必须有效，并匹配完整的参数值。",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "通过精确匹配 URL 字符串来允许 MCP 流式 HTTP 服务器，或使用 `exact`、`prefix` 或 `regex` 值匹配器表。",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "已配置的 MCP 服务器 URL 的匹配操作。",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "`exact` 或 `prefix` URL 匹配器使用的值。",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 匹配器使用的正则表达式。该表达式必须有效，并匹配完整的 URL 值。",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "以插件标识符为键的插件专属 MCP 服务器允许列表。存在此表时，没有匹配的插件和服务器条目的插件随附服务器会被禁用。",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "某个插件随附的 MCP 服务器的允许列表。插件服务器要求与顶层 `mcp_servers` 要求使用相同的精确身份匹配形式和匹配器形式。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "某个插件随附的 MCP 服务器的身份规则。设置 `command`（stdio）或 `url`（流式 HTTP）之一。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "通过精确匹配命令字符串来允许插件的 stdio MCP 服务器，或使用匹配器表要求可执行文件精确匹配，并按顺序匹配参数。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "插件随附的 stdio 服务器所配置的命令必须精确匹配的可执行文件。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "插件随附的 stdio 服务器的有序参数匹配器。配置的参数列表必须与匹配器列表长度相同，且每个位置都必须匹配。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "此参数位置的匹配操作。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "`exact` 或 `prefix` 参数匹配器使用的值。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 参数匹配器使用的正则表达式。该表达式必须匹配完整的参数值。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "通过精确匹配 URL 字符串来允许插件的流式 HTTP MCP 服务器，或使用 `exact`、`prefix` 或 `regex` 值匹配器表。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "插件随附的 MCP 服务器 URL 的匹配操作。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "`exact` 或 `prefix` URL 匹配器使用的值。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 匹配器使用的正则表达式。该表达式必须匹配完整的 URL 值。",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "针对插件市场来源的管理员要求。规则在 `restrict_to_allowed_sources` 为 `true` 时生效。",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "设为 `true` 时，添加市场、安装插件以及刷新已配置的 Git 市场均要求用户配置的市场来源与 `allowed_sources` 匹配。由 Codex 管理的 OpenAI 市场在其保留来源和名称匹配时仍在允许范围内。此设置不会在运行时筛选已配置的用户市场。",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "允许的市场来源以管理员选定的规则名称为键。不同名称的规则会跨要求配置层累积；同名规则下的字段遵循常规的配置层优先级。",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "一条允许来源的规则。合并要求后，最终的 `source` 值决定 Codex 解析哪些同级字段。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "市场来源的匹配器类型。使用 `git` 匹配单个代码仓库，使用 `host_pattern` 通过正则表达式匹配 Git 主机，或使用 `local` 匹配单个目录。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "当 `source = \"git\"` 时必填的 Git 代码仓库 URL。Codex 会先对配置的 URL 和允许的 URL 进行规范化，再要求代码仓库精确匹配。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "`git` 规则的可选精确 Git 引用。省略时，该规则允许匹配的代码仓库中的任意引用。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "当 `source = \"host_pattern\"` 时必填的正则表达式。Codex 会将其与从 HTTPS、SSH 或 SCP 格式的 Git 来源中解析出的小写主机名进行匹配。使用 `^` 和 `$` 可要求匹配整个主机名。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "当 `source = \"local\"` 时必填的本地市场目录。Codex 要求使用绝对路径，并在规范化后比较路径。",
    },
    {
      key: "apps",
      type: "table",
      description:
        "以应用标识符为键的托管应用要求。这些要求可以禁用应用，或限制单个工具的审批行为。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "设为 `false` 可禁用应用。合并多个要求来源时，禁用应用的要求仍具有约束力。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "为单个应用工具设置托管审批模式。",
    },
    {
      key: "rules",
      type: "table",
      description:
        "由管理员强制执行的命令规则，会与 `.rules` 文件合并。要求中的规则必须具有限制性。",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "强制执行的前缀规则列表。每条规则都必须包含 `pattern` 和 `decision`。",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "以模式 Token 表示的命令前缀。每个 Token 都需设置 `token` 或 `any_of` 中的一项。",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "此位置上的单个字面量 Token。",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "此位置上允许的备选 Token 列表。",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "必填。要求中的规则只能请求审批或禁止，不能直接允许。",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "可选的非空理由，会显示在审批提示或拒绝消息中。",
    },
  ]}
  client:load
/>
