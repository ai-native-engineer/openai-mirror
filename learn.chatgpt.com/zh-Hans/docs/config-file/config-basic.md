<!-- source: https://learn.chatgpt.com/zh-Hans/docs/config-file/config-basic -->

Codex 会从多个位置读取配置。您的个人默认设置保存在 `~/.codex/config.toml` 中，您可以通过 `.codex/config.toml` 文件添加项目级覆盖设置。出于安全考虑，Codex 仅在您信任项目时才会加载项目的 `.codex/` 配置层。

## Codex 配置文件

Codex 将用户级配置存储在 `~/.codex/config.toml` 中。要让设置仅对特定项目或子文件夹生效，请在代码仓库中添加 `.codex/config.toml` 文件。

要从 Codex IDE 扩展中打开配置文件，请选择右上角的齿轮图标，然后选择 **Codex 设置 \> 打开 config.toml**。

CLI 和 IDE 扩展共用相同的配置层。您可以通过这些配置层：

- 设置默认模型和提供商。
- 配置[审批策略和沙盒设置](/zh-Hans/codex/agent-approvals-security#sandbox-and-approvals)。
- 配置 [MCP 服务器](/zh-Hans/codex/extend/mcp)。

## 配置优先级

Codex 按以下顺序确定配置值（优先级从高到低）：

1. CLI 标志和 `--config` 覆盖设置
2. 项目配置文件：`.codex/config.toml`，从项目根目录到您当前的工作目录逐级排列（离当前目录最近的文件优先；仅限受信任的项目）
3. 通过 `--profile profile-name` 选择的[配置方案](/zh-Hans/codex/config-file/config-advanced#profiles)文件（`~/.codex/profile-name.config.toml`）
4. 用户配置：`~/.codex/config.toml`
5. 系统配置（如有）：Unix 上的 `/etc/codex/config.toml`
6. 内置默认值

利用上述优先级，在 `config.toml` 中设置共用的默认值，并在[配置方案文件](/zh-Hans/codex/config-file/config-advanced#profiles)中仅设置需要覆盖的值。

如果您将项目标记为不受信任，Codex 会跳过项目级 `.codex/` 配置层，包括项目本地配置、钩子和规则。用户和系统配置仍会加载，包括用户级和全局的钩子与规则。

有关通过 `-c`/`--config` 进行一次性覆盖的说明（包括 TOML 引号规则），请参阅[高级配置](/zh-Hans/codex/config-file/config-advanced#one-off-overrides-from-the-cli)。

  在受管理的计算机上，您的组织还可能通过
`requirements.toml` 强制实施约束（例如，禁止 `approval_policy = "never"` 或
`sandbox_mode = "danger-full-access"`）。请参阅[受管理的
  配置](/zh-Hans/codex/enterprise/managed-configuration)和[管理员强制执行的
  要求](/zh-Hans/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

## 常用配置选项

以下是一些最常修改的选项：

#### 默认模型

选择 Codex 在 CLI 和 IDE 中默认使用的模型。

#### 审批提示

控制 Codex 何时在运行生成的命令前暂停并请求审批。

```toml
approval_policy = "on-request"

有关 `untrusted`、`on-request` 和 `never` 的行为差异，请参阅[不显示审批提示运行](/zh-Hans/codex/agent-approvals-security#run-without-approval-prompts)和[常见沙盒与审批组合](/zh-Hans/codex/agent-approvals-security#common-sandbox-and-approval-combinations)。

#### 沙盒级别

调整 Codex 在执行命令时拥有的文件系统和网络访问权限。

```toml
sandbox_mode = "workspace-write"

有关各模式的具体行为（包括受保护的 `.git`/`.codex` 路径和网络默认设置），请参阅[沙盒与审批](/zh-Hans/codex/agent-approvals-security#sandbox-and-approvals)、[可写根目录中的受保护路径](/zh-Hans/codex/agent-approvals-security#protected-paths-in-writable-roots)和[网络访问](/zh-Hans/codex/agent-approvals-security#network-access)。

#### 权限配置方案

Codex 还支持具名权限配置方案，用于复用文件系统和
网络策略。内置配置方案为 `:read-only`、`:workspace` 和
`:danger-full-access`。自定义配置方案使用 `[permissions.<name>]` 表，以及
与之匹配的 `default_permissions` 值。请参阅[权限](/zh-Hans/codex/permissions)。

#### Windows 沙盒模式

在 Windows 上原生运行 Codex 时，请在 `windows` 表中将原生沙盒模式设置为 `elevated`。仅当您没有管理员权限或提权模式设置失败时，才使用 `unelevated`。

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### 网页搜索模式

Codex 默认为本地聊天启用网页搜索，并从网页搜索缓存中提供结果。该缓存是由 OpenAI 维护的网页结果索引，因此缓存模式会返回预先编入索引的结果，而不是获取实时网页。这可以降低任意实时内容带来的提示注入风险，但您仍应将网页结果视为不可信内容。如果您使用 `--yolo` 或其他[完全访问权限沙盒设置](/zh-Hans/codex/agent-approvals-security#common-sandbox-and-approval-combinations)，网页搜索会默认返回实时结果。请通过 `web_search` 选择模式：

- `"cached"`（默认）从网页搜索缓存中提供结果。
- `"indexed"` 仅在请求受搜索索引管控时才允许访问外部网页。
- `"live"` 从网页获取最新数据（与 `--search` 相同）。
- `"disabled"` 关闭网页搜索工具。

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### 推理强度

在模型支持的情况下，调整其推理强度。

```toml
model_reasoning_effort = "high"

#### 沟通风格

为支持此功能的模型设置默认沟通风格。

```toml
personality = "friendly" # or "pragmatic" or "none"

之后，您可以在当前会话中使用 `/personality` 覆盖此设置；使用 app-server API 时，也可以针对每个线程或轮次覆盖此设置。

#### TUI 键位映射

在 `tui.keymap` 下自定义终端快捷键。部分编辑器操作会回退到匹配的 `tui.keymap.global` 按键绑定；如果支持特定上下文的按键绑定，则优先使用这些绑定。空列表会解除该操作的按键绑定。

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### 命令环境

控制 Codex 将哪些环境变量传递给启动的命令。使用
按键名筛选的规则，仅保留您需要的变量：

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` 默认为 `true`，因此不会自动过滤
名称中包含 `KEY`、`SECRET` 或 `TOKEN` 的变量。若要启用这种自动过滤，请将其设置为 `false`。
有关排除规则、优先级和
旧版配置，请参阅[Shell 环境
策略](/zh-Hans/codex/config-file/config-advanced#shell-environment-policy)。

#### 日志目录

更改 Codex 写入本地日志文件的位置。显式设置 `log_dir` 后，还会
在该目录中启用纯文本 TUI 日志 `codex-tui.log`；这是一项需要用户主动启用的功能。

```toml
log_dir = "/absolute/path/to/codex-logs"

对于一次性运行，您也可以通过 CLI 进行设置：

```bash
codex -c log_dir=./.codex-log

## 功能标志

使用 `config.toml` 中的 `[features]` 表来开启或关闭可选及实验性功能。

### 常用功能标志

| 键                  |        默认值        | 成熟度     | 说明                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | 稳定       | 启用应用（连接器）集成                                                      |
| `goals`              |         true          | 稳定       | 启用持久化目标和自动继续功能                                        |
| `hooks`              |         true          | 稳定       | 启用通过 `hooks.json` 或内联 `[hooks]` 配置的生命周期钩子。请参阅[钩子](/zh-Hans/codex/hooks)。 |
| `fast_mode`          |         true          | 稳定       | 启用快速模式选择功能和 `service_tier = "fast"` 路径                          |
| `memories`           |         false         | 实验性 | 启用[记忆](/zh-Hans/codex/customization/memories)                                         |
| `multi_agent`        |         true          | 稳定       | 启用子智能体协作工具                                                      |
| `personality`        |         true          | 稳定       | 启用个性选择控件                                                    |
| `remote_plugin`      |         true          | 稳定       | 启用远程插件目录                                                         |
| `shell_snapshot`     |         true          | 稳定       | 创建 Shell 环境快照，以加快重复执行命令的速度                            |
| `shell_tool`         |         true          | 稳定       | 启用默认的 `shell` 工具                                                          |
| `unified_exec`       | `true`，Windows 除外 | 稳定       | 使用以 PTY 为后端的统一 exec 工具                                                     |
| `web_search`         |         true          | 已弃用   | 旧版开关；请优先使用顶层 `web_search` 设置                                 |
| `web_search_cached`  |         false         | 已弃用   | 旧版开关；未设置时会映射到 `web_search = "cached"`                            |
| `web_search_request` |         false         | 已弃用   | 旧版开关；未设置时会映射到 `web_search = "live"`                              |

  此表列出了常见的面向用户的功能标志，并未涵盖所有内部或
  尚在开发的功能。“成熟度”列使用的标签包括
  “实验性”、“测试版”和“稳定”。有关这些标签的含义，请参阅[功能
  成熟度](/zh-Hans/codex/feature-maturity)。

省略功能配置键即可保留其默认值。

有关生命周期钩子的配置，请参阅[钩子](/zh-Hans/codex/hooks)。

### 启用功能

- 在 `config.toml` 中，将 `feature_name = true` 添加到 `[features]` 下。
- 在 CLI 中运行 `codex --enable feature_name`。
- 如需启用多个功能，请运行 `codex --enable feature_a --enable feature_b`。
- 如需禁用某项功能，请在 `config.toml` 中将相应键设置为 `false`。
