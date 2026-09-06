<!-- source: https://learn.chatgpt.com/zh-Hans/docs/config-file/config-advanced -->

当您需要更精细地控制提供商、策略和集成时，请使用这些选项。如需快速上手，请参阅[基础配置](/zh-Hans/codex/config-file/config-basic)。

如需了解项目指导、可复用能力、自定义斜杠命令、子智能体工作流和集成的相关背景，请参阅[自定义](/zh-Hans/codex/customization/overview)。有关配置键，请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference)。

## 配置方案

配置方案可让您保存命名的配置层，并通过
CLI 在不同方案之间切换。传入 `--profile profile-name` 时，Codex 会先加载
`~/.codex/config.toml`，然后叠加 `~/.codex/profile-name.config.toml`。
配置方案名称可包含字母、数字、连字符和下划线。

请为每个配置方案创建单独的 TOML 文件，并在
配置方案文件中使用顶层配置键；不要将这些键嵌套在 `[profiles.profile-name]` 下。

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

由于配置方案文件的配置层级高于基础用户配置、低于
项目配置和 CLI 配置，因此只需包含与基础
配置不同的值。配置方案文件也可以覆盖 `model_catalog_json`；如果两个文件都设置了该值，Codex 会使用
配置方案文件中的值。

从 Codex 0.134.0 开始，`--profile` 不再读取 `[profiles.profile-name]`
（位于 `config.toml` 中），也不再支持顶层 `profile = "profile-name"`
选择器。请将旧版配置方案设置迁移到
`~/.codex/profile-name.config.toml`，然后删除对应的
`[profiles.profile-name]` 表和 `profile = "profile-name"` 选择器（位于
`config.toml` 中）。

## 通过 CLI 进行单次配置覆盖

除编辑 `~/.codex/config.toml` 外，您还可以通过 CLI 为单次运行覆盖配置：

- 如果存在专用标志，请优先使用，例如 `--model`。
- 需要覆盖任意配置键时，请使用 `-c` / `--config`。

示例：

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

注意事项：

- 配置键可使用点号表示法设置嵌套值，例如 `mcp_servers.context7.enabled=false`。
- `--config` 的值会作为 TOML 解析。如果不确定，请用引号括起该值，以免 shell 按空格将其拆分。
- 如果该值无法解析为 TOML，Codex 会将其视为字符串。

## 配置和状态的存储位置

Codex 将本地状态存储在 `CODEX_HOME` 下，默认位置为 `~/.codex`。

您可能会在其中看到以下常见文件：

- `config.toml`（您的本地配置）
- `auth.json`（如果您使用基于文件的凭据存储），或操作系统的钥匙串或密钥环
- `history.jsonl`（如果已启用历史记录持久化）
- 其他用户级状态，例如日志和缓存

有关身份验证的详细信息，包括凭据存储模式，请参阅[身份验证](/zh-Hans/codex/auth)。有关配置键的完整列表，请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference)。

有关存放在代码仓库或系统路径中的共享默认设置、规则和技能，请参阅[团队配置](/zh-Hans/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config)。

如果您只需将内置 OpenAI 提供商指向 LLM 代理、路由器或已启用数据驻留的项目，请将 `openai_base_url` 设置在 `config.toml` 中，无需定义新的提供商。这样可以更改内置 `openai` 提供商的基础 URL，而无需单独添加 `model_providers.<id>` 条目。

```toml
openai_base_url = "https://us.api.openai.com/v1"

## 项目配置文件（`.codex/config.toml`）

除用户配置外，Codex 还会从代码仓库内的 `.codex/config.toml` 文件读取项目级覆盖配置。Codex 会从项目根目录遍历至您当前的工作目录，并加载沿途找到的每个 `.codex/config.toml`。如果多个文件定义了同一个配置键，则以距离工作目录最近的文件为准。

出于安全考虑，Codex 仅在项目受信任时加载项目级配置文件。如果项目不受信任，Codex 会忽略项目的 `.codex/` 配置层，包括 `.codex/config.toml`、项目本地钩子和项目本地规则。用户层和系统层保持独立，仍会加载。

项目配置中的相对路径，例如 `model_instructions_file`，会以 `.codex/` 文件夹为基准进行解析，该文件夹包含 `config.toml`。

项目配置文件无法覆盖以下设置：重定向凭据、修改
由主机管理的应用请求元数据、更改提供商的身份验证方式、选择配置方案，
或运行本机通知/遥测命令。Codex 会忽略
项目本地 `.codex/config.toml` 中的以下配置键，并在发现这些键时输出启动
警告：`openai_base_url`、`chatgpt_base_url`、
`apps_mcp_product_sku`、`model_provider`、`model_providers`、`notify`、
`profile`、`profiles`、`experimental_realtime_ws_base_url` 和 `otel`。请将
提供商、通知和遥测相关配置键设置在用户级
`~/.codex/config.toml` 中；使用 `--profile profile-name`
和 `~/.codex/profile-name.config.toml` 选择配置方案。

## 钩子

Codex 还可以从 `hooks.json` 文件或内联的
`[hooks]` 表中加载生命周期钩子；这些表位于与生效配置层相邻的 `config.toml` 文件中。

实际使用中，最实用的是以下四个位置：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

仅当项目的 `.codex/` 配置层受信任时，才会加载项目本地钩子。
用户级钩子不受项目信任状态影响。

内联 TOML 钩子使用与 `hooks.json` 相同的事件结构：

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

如果同一配置层同时包含 `hooks.json` 和内联的 `[hooks]`，Codex 会同时加载
两者并发出警告。建议每个配置层只使用一种表示方式。

有关当前的事件列表、输入字段、输出行为和限制，请参阅
[钩子](/zh-Hans/codex/hooks)。

## 智能体角色（`config.toml` 中的 `[agents]`）

有关子智能体角色配置（`config.toml` 中的 `[agents]`），请参阅[子智能体](/zh-Hans/codex/agent-configuration/subagents)。

## 项目根目录检测

Codex 会从工作目录逐级向上查找项目配置，例如 `.codex/` 配置层和 `AGENTS.md`，直到到达项目根目录。

默认情况下，Codex 将包含 `.git` 的目录视为项目根目录。要自定义此行为，请在 `config.toml` 中设置 `project_root_markers`：

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

设置 `project_root_markers = []` 可跳过对父目录的搜索，并将当前工作目录视为项目根目录。

## 自定义模型提供商

模型提供商定义 Codex 连接模型的方式，包括基础 URL、传输 API、身份验证和可选的 HTTP 标头。自定义提供商不能复用以下预留的内置提供商 ID：`openai`、`ollama` 和 `lmstudio`。

定义其他提供商，并将 `model_provider` 指向这些提供商：

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

如果自定义提供商支持独立的网页搜索端点，请在其提供商配置中声明
这一能力：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

该设置对自定义提供商默认为 `false`。独立网页搜索功能仍在
开发中，且默认关闭。即使将提供商的相应能力设为 `true`，
也不会启用该功能：提供商必须支持兼容的端点，
并且所选模型和运行时必须支持独立搜索。已配置的
[`web_search` 模式](/zh-Hans/codex/web-search)和
托管搜索限制仍然适用。

按需添加请求标头：

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

当提供商需要 Codex 从外部凭据辅助程序获取 Bearer Token 时，请使用基于命令的身份验证：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

身份验证命令不接收任何 `stdin` 输入，且必须将 Token 输出到 stdout。Codex 会去除首尾空白字符，将空 Token 视为错误，并按 `refresh_interval_ms` 指定的间隔主动刷新；设置 `refresh_interval_ms = 0` 后，仅在身份验证重试后刷新。不要将 `[model_providers.<id>.auth]` 与 `env_key`、`experimental_bearer_token` 或 `requires_openai_auth` 同时使用。

### Amazon Bedrock 提供商

Codex 内置了 `amazon-bedrock` 模型提供商。请将其直接设为
`model_provider` 的值；与自定义提供商不同，此内置提供商仅支持
嵌套的 AWS 配置方案和区域覆盖设置。

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

如果省略 `profile`，Codex 会使用标准 AWS 凭据链。请将
`region` 设置为用于处理请求的受支持 Bedrock 区域。

有关完整设置流程、身份验证选项、支持的模型及功能
可用性，请参阅[将 ChatGPT Work 和 Codex 与 Amazon
Bedrock 搭配使用](/zh-Hans/codex/amazon-bedrock)。

## OSS 模式（本地提供商）

Codex 可使用 Ollama 或 LM
Studio 等本地“开源”提供商运行，只需传入 `--oss`。如需为单次运行选择提供商，请使用
`--local-provider`；或者将 `oss_provider` 设置为默认提供商。如果两者都未设置，
交互式 CLI 会提示您选择；`codex exec` 会报错退出。

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Azure 提供商与各提供商的调优

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

要更改内置 OpenAI 提供商的基础 URL，请使用 `openai_base_url`；不要创建 `[model_providers.openai]`，因为无法覆盖内置提供商 ID。

## 使用数据驻留的 API 组织

创建时已启用[数据驻留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)的项目可以创建模型提供商，更新 `base_url`，使其使用[正确的前缀](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)。对于启用了数据驻留的 ChatGPT 工作空间，无需自定义提供商；使用 ChatGPT 登录时，Codex 会遵循工作空间的数据驻留设置。

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## 模型推理、输出详细程度和限制

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` 仅适用于使用 Responses API 的提供商。Chat Completions 提供商会忽略此设置。

## 审批策略和沙盒模式

选择审批严格程度（影响 Codex 何时暂停）和沙盒级别（影响文件和网络访问）。

有关编辑 `config.toml` 时需要注意的操作细节，请参阅[常见沙盒与审批组合](/zh-Hans/codex/agent-approvals-security#common-sandbox-and-approval-combinations)、[可写根目录中的受保护路径](/zh-Hans/codex/agent-approvals-security#protected-paths-in-writable-roots)和[网络访问](/zh-Hans/codex/agent-approvals-security#network-access)。

如需了解同时配置文件系统和网络访问权限的测试版权限配置方案，请参阅[权限](/zh-Hans/codex/permissions)。

您还可以使用细粒度审批策略（`approval_policy = { granular = { ... } }`）来允许或自动拒绝各个提示类别。如果您希望某些情况使用常规交互式审批，而其他情况（例如 `request_permissions` 或技能脚本提示）自动拒绝以确保安全，这种策略很有用。

设置 `approvals_reviewer = "auto_review"`，将符合条件的交互式审批
请求交由自动审查处理。此设置更改的是审查者，而非沙盒
边界。

使用 `[auto_review].policy` 指定本地审查者策略指令。托管配置项
`guardian_policy_config` 优先。

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### 命名权限配置方案

如需了解内置配置方案、自定义配置方案语法，以及完整的文件系统与
网络配置模型，请参阅[权限](/zh-Hans/codex/permissions)。

如需完整的键列表和要求约束条件，请参阅
[配置参考](/zh-Hans/codex/config-file/config-reference)和
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)。

  在 workspace-write 模式下，某些环境仍会将 `.git/` 和 `.codex/`
  设为只读，即使工作空间的其余部分可写。因此，
  `git commit` 等命令要在
  沙盒外运行，可能仍需审批。如果您希望 Codex 跳过特定命令（例如，在沙盒外阻止 `git
  commit`），请使用
<a href="/codex/agent-configuration/rules">规则</a>。

彻底禁用沙盒（仅当您的环境已隔离进程时使用）：

```toml
sandbox_mode = "danger-full-access"

## Shell 环境策略

`shell_environment_policy` 控制 Codex 会将哪些环境变量传递给
其启动的命令。使用 `inherit = "none"` 可从空环境开始，或
使用 `inherit = "core"` 继承一组精简的环境变量。添加显式值和键控
过滤器，以避免向所启动的命令传递不必要的机密信息。

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

过滤模式不区分大小写，并支持 `*` 和 `?`。使用 `"exclude"`
移除匹配的变量。当任一模式使用 `"include"` 时，Codex
仅保留与包含模式匹配的变量。包含模式不会恢复那些
已被排除的变量。过滤器键跨
配置层合并时不区分大小写。

`ignore_default_excludes` 默认为 `true`，因此 Codex 不会自动
移除名称中包含 `KEY`、`SECRET` 或 `TOKEN` 的变量。将其设为 `false`
即可在应用显式过滤器之前应用这些自动排除规则。

Codex 先应用自动排除规则，再应用自定义排除规则，随后应用
`set` 中的值，最后应用包含模式允许列表。由于 `set` 在
排除操作之后执行，因此可以恢复被排除的变量。包含模式允许列表
仍可移除这个已恢复的值。

旧版 `exclude` 和 `include_only` 数组在现有
配置中仍受支持。不要在同一配置层中将其中任一数组与
`[shell_environment_policy.filters]` 组合使用；Codex
会拒绝这种组合。

## MCP 服务器

请参阅专门的[MCP 文档](/zh-Hans/codex/extend/mcp)，了解配置详情。

## 可观测性和遥测

启用 OpenTelemetry（OTel）日志导出，以跟踪 Codex 运行（API 请求、SSE/事件、提示、工具审批和结果）。默认处于禁用状态；可通过 `[otel]` 主动启用：

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

选择导出器：

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

如果 `exporter = "none"`，Codex 会记录事件，但不会发送任何内容。导出器会异步批量处理事件，并在关闭时刷新缓冲区。事件元数据包括服务名称、CLI 版本、环境标签、会话 ID、模型、沙盒和审批设置，以及各事件字段（请参阅[配置参考](/zh-Hans/codex/config-file/config-reference)）。

### 发出的事件

Codex 会发出有关运行和工具使用情况的结构化日志事件。代表性的事件类型包括：

- `codex.conversation_starts`（模型、推理设置、沙盒和审批策略）
- `codex.api_request`（尝试、状态、是否成功、持续时间和错误详情）
- `codex.sse_event`（流事件类型、成功与否、持续时间，以及 `response.completed` 事件中的 Token 计数）
- `codex.websocket_request` 和 `codex.websocket_event`（请求持续时间，以及每条消息的类型、成功与否和错误信息）
- `codex.user_prompt`（长度；除非显式启用，否则内容会被隐去）
- `codex.tool_decision`（批准或拒绝，以及结果由配置还是用户决定）
- `codex.tool_result`（持续时间、成功状态、输出片段）

### 发出的 OTel 指标

启用 OTel 指标流水线后，Codex 会针对 API、流和工具活动发出计数器与持续时间直方图。

以下每项指标还包含默认元数据标签：`auth_mode`、`originator`、`session_source`、`model` 和 `app.version`。

| 指标                                | 类型      | 字段              | 说明                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | 计数器   | `status`、`success` | 按 HTTP 状态和成功与否分类的 API 请求数。             |
| `codex.api_request.duration_ms`       | 直方图 | `status`、`success` | API 请求持续时间（毫秒）。                             |
| `codex.sse_event`                     | 计数器   | `kind`、`success`   | 按事件类型和成功与否分类的 SSE 事件数。                |
| `codex.sse_event.duration_ms`         | 直方图 | `kind`、`success`   | SSE 事件处理持续时间（毫秒）。                    |
| `codex.websocket.request`             | 计数器   | `success`           | 按成功与否分类的 WebSocket 请求数。                       |
| `codex.websocket.request.duration_ms` | 直方图 | `success`           | WebSocket 请求持续时间（毫秒）。                       |
| `codex.websocket.event`               | 计数器   | `kind`、`success`   | 按类型和成功与否分类的 WebSocket 消息/事件数。        |
| `codex.websocket.event.duration_ms`   | 直方图 | `kind`、`success`   | WebSocket 消息/事件处理持续时间（毫秒）。      |
| `codex.tool.call`                     | 计数器   | `tool`、`success`   | 按工具名称和成功/失败统计的工具调用次数。           |
| `codex.tool.call.duration_ms`         | 直方图 | `tool`、`success`   | 按工具名称和结果统计的工具执行时长（毫秒）。 |

有关遥测的更多安全和隐私指南，请参阅 [安全](/zh-Hans/codex/agent-approvals-security#monitoring-and-telemetry)。

### 指标

默认情况下，Codex 会定期向 OpenAI 发回少量匿名使用数据和运行状况数据。这有助于发现 Codex 未正常运行的情况，并了解当前正在使用的功能和配置选项，以便 Codex 团队专注于最重要的事项。这些指标不包含任何个人身份信息（PII）。指标收集与 OTel 日志/追踪导出相互独立。

如果您希望在一台计算机上完全停用 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展的指标收集，请在配置中设置分析标志：

```toml
[analytics]
enabled = false

每项指标都包含其自身的字段以及下方的默认上下文字段。

#### 默认上下文字段（适用于每个事件/指标）

- `auth_mode`：`swic` \| `api` \| `unknown`。
- `model`：所用模型的名称。
- `app.version`：Codex 版本。

#### 指标目录

每项指标都包含必填字段以及上方的默认上下文字段。下列指标名称省略了 `codex.` 前缀。
大多数指标名称统一定义在 `codex-rs/otel/src/metrics/names.rs` 中；此外，此处也收录了在该文件之外生成的特定功能指标。
如果某项指标包含 `tool` 字段，它表示所使用的内部工具（例如 `apply_patch` 或 `shell`），不会包含实际的 shell 命令，也不会包含 `codex` 尝试应用的补丁。

#### 运行时和模型传输

| 指标                                          | 类型      | 字段               | 说明                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | 计数器   | `status`、`success`  | 按 HTTP 状态和成功/失败统计的 API 请求数。        |
| `api_request.duration_ms`                       | 直方图 | `status`、`success`  | API 请求时长（毫秒）。                        |
| `sse_event`                                     | 计数器   | `kind`、`success`    | 按事件种类和成功/失败统计的 SSE 事件数。           |
| `sse_event.duration_ms`                         | 直方图 | `kind`、`success`    | SSE 事件处理时长（毫秒）。               |
| `websocket.request`                             | 计数器   | `success`            | 按成功/失败统计的 WebSocket 请求数。                  |
| `websocket.request.duration_ms`                 | 直方图 | `success`            | WebSocket 请求时长（毫秒）。                  |
| `websocket.event`                               | 计数器   | `kind`、`success`    | 按类型和成功/失败统计的 WebSocket 消息/事件数。   |
| `websocket.event.duration_ms`                   | 直方图 | `kind`、`success`    | WebSocket 消息/事件处理时长（毫秒）。 |
| `responses_api_overhead.duration_ms`            | 直方图 |                      | WebSocket 响应中的 Responses API 开销时间。      |
| `responses_api_inference_time.duration_ms`      | 直方图 |                      | WebSocket 响应中的 Responses API 推理时间。     |
| `responses_api_engine_iapi_ttft.duration_ms`    | 直方图 |                      | Responses API 引擎 IAPI 的首 Token 耗时。        |
| `responses_api_engine_service_ttft.duration_ms` | 直方图 |                      | Responses API 引擎服务的首 Token 耗时。     |
| `responses_api_engine_iapi_tbt.duration_ms`     | 直方图 |                      | Responses API 引擎 IAPI 的相邻 Token 间隔时间。         |
| `responses_api_engine_service_tbt.duration_ms`  | 直方图 |                      | Responses API 引擎服务的相邻 Token 间隔时间。      |
| `transport.fallback_to_http`                    | 计数器   | `from_wire_api`      | WebSocket 回退到 HTTP 的次数。                            |
| `remote_models.fetch_update.duration_ms`        | 直方图 |                      | 获取远程模型定义所需的时间。                      |
| `remote_models.load_cache.duration_ms`          | 直方图 |                      | 加载远程模型缓存所需的时间。                         |
| `startup_prewarm.duration_ms`                   | 直方图 | `status`             | 按结果统计的启动预热时长。                         |
| `startup_prewarm.age_at_first_turn_ms`          | 直方图 | `status`             | 首个实际轮次获取启动预热结果时，预热已持续的时长。    |
| `cloud_requirements.fetch.duration_ms`          | 直方图 |                      | 工作空间管理的云端要求获取时长。         |
| `cloud_requirements.fetch_attempt`              | 计数器   | 见说明             | 工作空间管理的云端要求获取尝试次数。         |
| `cloud_requirements.fetch_final`                | 计数器   | 见说明             | 工作空间管理的云端要求的最终获取结果。    |
| `cloud_requirements.load`                       | 计数器   | `trigger`、`outcome` | 工作空间管理的云端要求加载结果。           |

`cloud_requirements.fetch_attempt` 指标包含 `trigger`、`attempt`、`outcome` 和 `status_code` 字段。`cloud_requirements.fetch_final` 指标包含 `trigger`、`outcome`、`reason`、`attempt_count` 和 `status_code` 字段。

#### 轮次与工具活动

| 指标                                 | 类型      | 字段                                                                    | 描述                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | 直方图 |                                                                           | 完整轮次的端到端时长。                                                                                 |
| `turn.ttft.duration_ms`                | 直方图 |                                                                           | 轮次从开始到生成首个 Token 所需的时间。                                                                                  |
| `turn.ttfm.duration_ms`                | 直方图 |                                                                           | 轮次从开始到生成首个模型输出项所需的时间。                                                                      |
| `turn.network_proxy`                   | 计数器   | `active`、`tmp_mem_enabled`                                               | 此轮次中托管网络代理是否处于活动状态。                                                       |
| `turn.memory`                          | 计数器   | `read_allowed`、`feature_enabled`、`config_use_memories`、`has_citations` | 每个轮次的记忆读取可用性和记忆引用使用情况。                                                     |
| `turn.tool.call`                       | 直方图 | `tmp_mem_enabled`                                                         | 该轮次中的工具调用次数。                                                                                |
| `turn.token_usage`                     | 直方图 | `token_type`、`tmp_mem_enabled`                                           | 每个轮次按 Token 类型（`total`、`input`、`cached_input`、`output` 或 `reasoning_output`）统计的 Token 用量。          |
| `tool.call`                            | 计数器   | `tool`、`success`                                                         | 按工具名称和成功或失败状态统计的工具调用次数。                                                          |
| `tool.call.duration_ms`                | 直方图 | `tool`、`success`                                                         | 按工具名称和结果统计的工具执行时长（毫秒）。                                                |
| `tool.unified_exec`                    | 计数器   | `tty`                                                                     | 按 TTY 模式统计的统一 exec 工具调用次数。                                                                             |
| `approval.requested`                   | 计数器   | `tool`、`approved`                                                        | 工具审批请求的结果（`approved`、`approved_with_amendment`、`approved_for_session`、`denied`、`abort`）。 |
| `mcp.call`                             | 计数器   | 见说明                                                                  | MCP 工具调用结果。                                                                                      |
| `mcp.call.duration_ms`                 | 直方图 | 见说明                                                                  | MCP 工具调用时长。                                                                                    |
| `mcp.tools.list.duration_ms`           | 直方图 | `cache`                                                                   | MCP 工具列表获取时长，包括缓存命中或未命中状态。                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | 直方图 |                                                                           | 未命中缓存的 MCP 工具获取时长。                                                                |
| `mcp.tools.cache_write.duration_ms`    | 直方图 |                                                                           | Codex 应用的 MCP 工具缓存写入时长。                                                                    |
| `hooks.run`                            | 计数器   | `hook_name`、`source`、`status`                                           | 按钩子名称、来源和状态统计的钩子运行次数。                                                                 |
| `hooks.run.duration_ms`                | 直方图 | `hook_name`、`source`、`status`                                           | 钩子运行时长，以毫秒为单位。                                                                               |

`mcp.call` 和 `mcp.call.duration_ms` 指标包含 `status`；常规工具调用发出的指标还包含 `tool`，并在可用时包含 `connector_id` 和 `connector_name`。被阻止的 Codex 应用 MCP 调用可能发出 `mcp.call`，其中仅包含 `status`。

#### 线程、任务和功能

| 指标                            | 类型      | 字段                | 描述                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | 计数器   | `feature`、`value`    | 与默认值不同的功能值，每个非默认值生成一行记录。         |
| `status_line`                     | 计数器   |                       | 会话启动时已配置状态行。                                   |
| `model_warning`                   | 计数器   |                       | 已向模型发送警告。                                                       |
| `thread.started`                  | 计数器   | `is_git`              | 创建新线程，并标记工作目录是否位于 Git 代码仓库中。    |
| `conversation.turn.count`         | 计数器   |                       | 每个线程中的用户与助手交互轮次，在线程结束时记录。              |
| `thread.fork`                     | 计数器   | `source`              | 通过派生现有线程创建新线程。                                |
| `thread.rename`                   | 计数器   |                       | 已重命名线程。                                                                  |
| `thread.side`                     | 计数器   | `source`              | 已创建旁支对话。                                                       |
| `thread.skills.enabled_total`     | 直方图 |                       | 新线程启用的技能数量。                                       |
| `thread.skills.kept_total`        | 直方图 |                       | 渲染提示后保留的已启用技能数量。                            |
| `thread.skills.truncated`         | 直方图 |                       | 技能渲染是否截断了已启用技能列表（`1` 或 `0`）。          |
| `task.compact`                    | 计数器   | `type`                | 按类型（`remote` 或 `local`）统计的压缩次数，包括手动压缩和自动压缩。 |
| `task.review`                     | 计数器   |                       | 触发的审查次数。                                                     |
| `task.undo`                       | 计数器   |                       | 触发的撤销操作次数。                                                |
| `task.user_shell`                 | 计数器   |                       | 用户 Shell 操作次数，例如 TUI 中的 `!`。                       |
| `shell_snapshot`                  | 计数器   | 参见注释              | 获取 Shell 快照是否成功。                                       |
| `shell_snapshot.duration_ms`      | 直方图 | `success`             | 获取 Shell 快照所需的时间。                                                   |
| `skill.injected`                  | 计数器   | `status`、`skill`     | 按技能统计的技能注入结果。                                               |
| `plugins.startup_sync`            | 计数器   | `transport`、`status` | 精选插件启动时的同步尝试次数。                                            |
| `plugins.startup_sync.final`      | 计数器   | `transport`、`status` | 精选插件启动时同步的最终结果。                                       |
| `multi_agent.spawn`               | 计数器   | `role`                | 按角色统计的智能体创建次数。                                                            |
| `multi_agent.resume`              | 计数器   |                       | 智能体恢复运行次数。                                                                   |
| `multi_agent.nickname_pool_reset` | 计数器   |                       | 智能体昵称池重置次数。                                                      |

`shell_snapshot` 指标包含 `success`，失败时还包含 `failure_reason`。

#### 记忆和本地状态

| 指标                         | 类型      | 字段                    | 描述                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | 计数器   | `status`                  | 记忆第 1 阶段按状态统计的作业数。                      |
| `memory.phase1.e2e_ms`         | 直方图 |                           | 记忆第 1 阶段的端到端耗时。                   |
| `memory.phase1.output`         | 计数器   |                           | 记忆第 1 阶段写入的输出数。                           |
| `memory.phase1.token_usage`    | 直方图 | `token_type`              | 记忆第 1 阶段按 Token 类型统计的 Token 用量。                 |
| `memory.phase2`                | 计数器   | `status`                  | 记忆第 2 阶段按状态统计的作业数。                      |
| `memory.phase2.e2e_ms`         | 直方图 |                           | 记忆第 2 阶段的端到端耗时。                   |
| `memory.phase2.input`          | 计数器   |                           | 记忆第 2 阶段的输入数。                               |
| `memory.phase2.token_usage`    | 直方图 | `token_type`              | 记忆第 2 阶段按 Token 类型统计的 Token 用量。                 |
| `memories.usage`               | 计数器   | `kind`、`tool`、`success` | 按类型、工具和成功/失败统计的记忆使用情况。          |
| `external_agent_config.detect` | 计数器   | 见注释                  | 按迁移项类型统计的外部智能体配置检测次数。  |
| `external_agent_config.import` | 计数器   | 见注释                  | 按迁移项类型统计的外部智能体配置导入次数。     |
| `db.backfill`                  | 计数器   | `status`                  | 状态数据库初次回填结果（`upserted`、`failed`）。 |
| `db.backfill.duration_ms`      | 直方图 | `status`                  | 状态数据库初次回填的耗时。                |
| `db.error`                     | 计数器   | `stage`                   | 状态数据库操作期间发生的错误。                        |

`external_agent_config.detect` 和 `external_agent_config.import` 指标包含 `migration_type`；技能迁移还包含 `skills_count`。

#### Windows 沙盒

| 指标                                           | 类型      | 字段                                    | 说明                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | 计数器   | `originator`、`mode`                      | Windows 沙盒设置成功次数。                      |
| `windows_sandbox.setup_failure`                  | 计数器   | `originator`、`mode`                      | Windows 沙盒设置失败次数。                       |
| `windows_sandbox.setup_duration_ms`              | 直方图 | `result`、`originator`、`mode`            | Windows 沙盒设置耗时。                       |
| `windows_sandbox.elevated_setup_success`         | 计数器   |                                           | Windows 沙盒提权设置成功次数。             |
| `windows_sandbox.elevated_setup_failure`         | 计数器   | 见注释                                  | Windows 沙盒提权设置失败次数。              |
| `windows_sandbox.elevated_setup_canceled`        | 计数器   | 见注释                                  | 已取消的 Windows 沙盒提权设置尝试次数。     |
| `windows_sandbox.elevated_setup_duration_ms`     | 直方图 | `result`                                  | Windows 沙盒提权设置耗时。              |
| `windows_sandbox.elevated_prompt_shown`          | 计数器   |                                           | 显示沙盒提权设置提示的次数。                  |
| `windows_sandbox.elevated_prompt_accept`         | 计数器   |                                           | 接受沙盒提权设置提示的次数。               |
| `windows_sandbox.elevated_prompt_use_legacy`     | 计数器   |                                           | 用户在提权设置提示中选择旧版沙盒的次数。   |
| `windows_sandbox.elevated_prompt_quit`           | 计数器   |                                           | 用户在提权设置提示中退出的次数。                   |
| `windows_sandbox.fallback_prompt_shown`          | 计数器   |                                           | 显示回退沙盒提示的次数。                        |
| `windows_sandbox.fallback_retry_elevated`        | 计数器   |                                           | 用户通过回退提示重试提权设置的次数。 |
| `windows_sandbox.fallback_use_legacy`            | 计数器   |                                           | 用户通过回退提示选择旧版沙盒的次数。   |
| `windows_sandbox.fallback_prompt_quit`           | 计数器   |                                           | 用户通过回退提示退出的次数。                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | 计数器   | 参见注释                                  | 旧版 Windows 沙盒设置预检失败次数。       |
| `windows_sandbox.setup_elevated_sandbox_command` | 计数器   |                                           | 提权沙盒设置命令的调用次数。               |
| `windows_sandbox.createprocessasuserw_failed`    | 计数器   | `error_code`、`path_kind`、`exe`、`level` | Windows `CreateProcessAsUserW` 失败次数。              |

当 Windows 设置失败的详细信息可用时，提权设置失败指标会包含 `code` 和 `message`；从共享设置路径发出时，还可能包含 `originator`。从共享设置路径发出时，`windows_sandbox.legacy_setup_preflight_failed` 指标会包含 `originator`，但回退提示中的预检失败可能不包含任何字段。

### 反馈控制

默认情况下，本地客户端允许用户通过 `/feedback` 发送反馈。要在一台计算机上的 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中禁用反馈收集，请更新您的配置：

```toml
[feedback]
enabled = false

禁用后，`/feedback` 会显示一条禁用提示，Codex 也会拒绝反馈提交。

### 隐藏或显示推理事件

如果您想减少冗杂的“推理”输出（例如 CI 日志中的此类输出），可以将其隐藏：

```toml
hide_agent_reasoning = true

如果您想在模型输出原始推理内容时将其显示出来：

```toml
show_raw_agent_reasoning = true

仅当您的工作流程可以接受原始推理时，才启用此功能。某些模型或提供商（例如 `gpt-oss`）不会输出原始推理；在这种情况下，此设置不会产生任何可见效果。

## 通知

使用 `notify`，可在 Codex 每次发出受支持的事件时触发外部程序（目前仅支持 `agent-turn-complete`）。它适用于桌面弹出通知、聊天 webhook、CI 更新，以及内置 TUI 通知未涵盖的其他渠道提醒。

```toml
notify = ["python3", "/path/to/notify.py"]

`notify.py` 示例（已截断），用于响应 `agent-turn-complete`：

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

该脚本接收一个 JSON 参数。常见字段包括：

- `type`（当前为 `agent-turn-complete`）
- `thread-id`（会话标识符）
- `turn-id`（轮次标识符）
- `cwd`（工作目录）
- `input-messages`（触发该轮次的用户消息）
- `last-assistant-message`（最后一条助手消息的文本）

将脚本放在磁盘上的某个位置，并将 `notify` 指向该脚本。

#### `notify` 与 `tui.notifications`

- `notify` 会运行一个外部程序（适合用于 webhook、桌面通知程序和 CI 钩子）。
- `tui.notifications` 是 TUI 的内置功能，并可选择按事件类型筛选（例如 `agent-turn-complete` 和 `approval-requested`）。
- `tui.notification_method` 控制 TUI 发出终端通知的方式（`auto`、`osc9` 或 `bel`）。
- `tui.notification_condition` 控制 TUI 通知是仅在
  终端未获得焦点时（`unfocused`）触发，还是始终（`always`）触发。

在 `auto` 模式下，Codex 优先使用 OSC 9 通知（一些终端会将这种终端转义序列解释为桌面通知），否则会回退到 BEL（`\x07`）。

有关确切的键，请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference)。

## 历史记录持久化

默认情况下，Codex 会将本地会话记录保存在 `CODEX_HOME` 下（例如 `~/.codex/history.jsonl`）。要禁用本地历史记录持久化：

```toml
[history]
persistence = "none"

要限制历史记录文件的大小，请设置 `history.max_bytes`。文件超过此上限时，Codex 会丢弃最早的条目并压缩该文件，同时保留最新记录。

```toml
[history]
max_bytes = 104857600 # 100 MiB

## 可点击的引用

如果您使用的终端或编辑器集成支持此功能，Codex 可以将文件引用渲染为可点击的链接。配置 `file_opener` 以选择 Codex 使用的 URI 方案：

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

例如，像 `/home/user/project/main.py:42` 这样的引用可以改写为可点击的 `vscode://file/...:42` 链接。

## 项目指令发现

Codex 会读取 `AGENTS.md`（及相关文件），并在会话的首个轮次中加入有限的项目指导信息。此行为由两个设置项控制：

- `project_doc_max_bytes`：从每个 `AGENTS.md` 文件中读取的数据量
- `project_doc_fallback_filenames`：某一目录层级中缺少 `AGENTS.md` 时要尝试的其他文件名

有关详细步骤，请参阅[使用 AGENTS.md 自定义指令](/zh-Hans/codex/agent-configuration/agents-md)。

## 桌面端

本节中的选项仅适用于 ChatGPT 桌面应用。

### 添加自定义文件处理程序

在用户级 `~/.codex/config.toml` 中，于
`desktop.custom_file_handlers` 下添加条目，即可在 ChatGPT 桌面应用默认不支持的编辑器或内部启动器中
打开文件。每个条目都会向
应用的 **打开方式** 菜单添加一个编辑器选项。当
`command` 是现有的绝对路径，或可通过应用的 `PATH` 解析到时，应用会列出该选项。

以下示例展示了将文件传给处理程序的三种方式：

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

保存 `config.toml`，然后重启 ChatGPT 桌面应用。

处理程序 ID 是 TOML 表头的最后一段。它必须包含
1–64 个字符，以 ASCII 字母或数字开头，其余字符只能是
ASCII 字母、数字、句点、下划线或连字符。应用会为
该 ID 加上 `custom:` 前缀；例如，`company_editor` 会变为
`custom:company_editor`。如果 ID 包含句点，请用引号将其括起，以免 TOML
将其解释为嵌套表。例如：

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

每个处理程序支持以下字段：

| 字段          | 必填 | 说明                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | 是      | 应用中的显示名称。                                                                                                                                                 |
| `icon`         | 是      | 应用内置图标（例如 `apps/vscode.png`）、base64 `data:image/...` URL、`file:` URI 或本地图像的绝对路径。如果来源不受支持，则使用默认的 VS Code 图标。 |
| `command`      | 是      | 用于检测和启动的可执行文件路径或命令名称。                                                                                                                    |
| `args`         | 否       | 插入到 `command` 与文件输入之间的字符串数组。默认为 `[]`。                                                                                            |
| `input`        | 否       | 应用发送文件输入的方式：`path`、`json_argument` 或 `json_stdin`。默认为 `path`。                                                                              |
| `supports_ssh` | 否       | 是否为 SSH 工作空间中的文件提供该处理程序。默认为 `false`。如果处理程序需要远程主机和路径详细信息，请使用 `json_stdin`。                     |

`input` 的值决定 `args` 之后的内容：

- `path` 会将路径作为最后一个参数附加到命令中。
- `json_argument` 会附加一个包含 `target`、`path`、`appPath` 和
`location` 的 JSON 对象。`location` 的值可以是包含从 1 开始计数的 `line` 和
`column` 值的对象，也可以是 `null`。
- `json_stdin` 会将 JSON 对象写入标准输入，而不是添加
  参数。该对象还包含 `hostConfig`、`remoteWorkspaceRoot` 和
`remotePath`；这些字段不适用时为 `null`。

例如，`company_editor` 可在用户打开
特定源代码位置时接收此参数：

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

将自定义处理程序选为首选编辑器后，该选择会以与选择内置编辑器相同的
方式持久保存，包括按项目保存的偏好设置。

## TUI 选项

不带子命令运行 `codex` 会启动交互式终端用户界面（TUI）。Codex 在 `[tui]` 下提供了一些 TUI 专用配置，包括：

- `tui.notifications`：启用或禁用通知（或限制为特定类型）
- `tui.notification_method`：为终端通知选择 `auto`、`osc9` 或 `bel`
- `tui.notification_condition`：选择 `unfocused` 或 `always`，以指定何时
  触发通知
- `tui.animations`：启用或禁用 ASCII 动画和微光效果
- `tui.alternate_screen`：控制备用屏幕的使用（设为 `never` 可保留终端滚动历史记录）
- `tui.show_tooltips`：在欢迎屏幕上显示或隐藏新手引导工具提示

`tui.notification_method` 默认为 `auto`。在 `auto` 模式下，如果终端看似支持 OSC 9 通知（一种终端转义序列，部分终端会将其解析为桌面通知），Codex 会优先使用这类通知；否则回退到 BEL（`\x07`）。

有关完整的配置键列表，请参阅 [配置参考资料](/zh-Hans/codex/config-file/config-reference)。
