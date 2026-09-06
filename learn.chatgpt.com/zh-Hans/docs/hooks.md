<!-- source: https://learn.chatgpt.com/zh-Hans/docs/hooks -->

钩子是 Codex 的扩展框架，让您可以在智能体循环中运行脚本或 MCP 工具，实现以下功能：

- 将聊天发送到自定义日志记录/分析引擎
- 扫描您团队的提示词，防止意外粘贴 API 密钥
- 总结聊天，自动创建持久记忆
- 在一轮聊天停止时运行自定义验证检查，以确保符合标准
- 在特定目录中自定义提示词

需要注意的运行时行为：

- 来自多个文件的所有匹配钩子都会运行。
- 同一事件的多个匹配命令钩子会并发启动，因此一个钩子无法阻止另一个匹配钩子启动。
- 非托管钩子必须先经过审查并获得信任，才能运行。

钩子会在对话的不同阶段运行：

| 时机                              | 钩子                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 一轮对话期间                     | `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、`SubagentStop`、`Stop` |
| 您中断正在进行的一轮对话时 | `Interrupt`（不针对子智能体运行）                                                                                   |
| 会话或子智能体启动时 | `SessionStart`、`SubagentStart`                                                                                           |
| 主线程结束时         | `SessionEnd`（不针对子智能体运行）                                                                                  |

## Codex 查找钩子的位置

Codex 会在生效配置层对应的位置查找以下任一形式的钩子：

- `hooks.json`
- `config.toml` 中的内联 `[hooks]` 表

已安装的插件也可以通过插件清单
或默认的 `hooks/hooks.json` 文件附带生命周期配置。有关插件
打包规则，请参阅[构建
插件](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks)。

实际使用中，最实用的四个位置是：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

如果存在多个钩子来源，Codex 会加载所有匹配的钩子。
优先级较高的配置层不会替换较低优先级层中的钩子。
如果同一配置层同时包含 `hooks.json` 和内联 `[hooks]`，Codex 会将二者合并，
并在启动时发出警告。建议每个配置层只使用一种表示形式。

Codex 还可以发现已启用插件附带的钩子。这些钩子会与其他来源的钩子一同加载，并采用与其他非托管钩子相同的信任审查流程。

只有当项目的 `.codex/` 配置层受信任时，才会加载项目本地钩子。
在不受信任的项目中，Codex 仍会从用户和系统各自生效的配置层
加载相应的钩子。

## 审查并信任钩子

Codex 会先列出已配置的钩子，再决定哪些钩子可以运行。非托管钩子运行前，Codex 会要求您审查并信任该钩子的确切定义。Codex 根据钩子的当前哈希值记录信任状态，因此新增或修改过的钩子会被标记为待审查，并在获得信任前被跳过。

在 CLI 中使用 `/hooks` 可检查钩子来源、审查新增或修改过的钩子、
信任钩子，或禁用单个非托管钩子。如果启动时有钩子需要审查，
Codex 会输出一条警告，提示您打开 `/hooks`。

来自系统、MDM、云端或 `requirements.toml` 的托管钩子会被标记为托管，
根据策略获得信任，且无法在用户钩子浏览界面中禁用。

对于已在 Codex 外部核验钩子来源的一次性自动化任务，请传入
`--dangerously-bypass-hook-trust`，即可运行已启用的钩子，
本次调用无须已有的持久化钩子信任记录。

## 配置结构

钩子分为三个层级：

- 钩子事件，例如 `PreToolUse`、`PostToolUse`、`PreCompact`、
`SubagentStart` 或 `Stop`
- 用于确定该事件何时匹配的匹配器组
- 匹配器组匹配成功时运行的一个或多个钩子处理程序

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

注意事项：

- `description` 是 `hooks.json` 文件的可选顶级元数据。
  它不会影响哪些钩子会运行。
- `timeout` 的单位为秒。
- 如果省略 `timeout`，Codex 会将大多数钩子的超时时间设为 `600` 秒。
  - `SessionEnd` 和 `Interrupt` 的默认超时时间为 `1` 秒，最长支持 `3` 秒。
- `statusMessage` 是可选项。
- `additionalContextLimit` 用于设置命令钩子可向模型发送的 `additionalContext` 内容量上限。
  超过此上限后，Codex 会将完整文本保存到磁盘，改为发送较短的预览。
  请参阅[过长的钩子输出](#large-hook-output)。
- `commandWindows` 是仅在 Windows 上生效的可选命令覆盖项。在 TOML 中，请使用
`command_windows` 或 `commandWindows`。
- 将 `async` 设为 `true`，即可[在后台
  运行命令钩子](#run-hooks-in-the-background)。
- 支持 `command` 和 `mcp_tool` 处理程序。`prompt` 和 `agent` 处理程序
  会被解析，但不会运行。
- 命令运行时以会话的 `cwd` 作为工作目录。
- 对于代码仓库本地钩子，建议基于 Git 根目录解析路径，
  而不要使用 `.codex/hooks/...` 之类的相对路径。Codex 可能会从子目录启动，
  基于 Git 根目录的路径可确保钩子位置保持稳定。

`config.toml` 中等效的内联 TOML：

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## MCP 工具钩子

MCP 工具钩子让生命周期事件能够调用已连接的 MCP 服务器上的工具。它会将结构化参数直接发送给工具，并采用与命令钩子相同的信任审查流程和输出约定。

### 配置 MCP 工具钩子

在 Codex 写入或编辑文件后，此钩子会请求 `scanner` MCP 服务器
扫描每个补丁：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| 字段           | 含义                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | 必须为 `mcp_tool`。                                              |
| `server`        | 必填，指定已连接的 MCP 服务器的名称。                |
| `tool`          | 必填，指定该服务器提供的工具的名称。                  |
| `input`         | 可选，包含参数模板的 JSON 对象。默认为 `{}`。    |
| `timeout`       | 可选的实际执行超时时间，单位为秒。默认为 `600`。 |
| `statusMessage` | 可选消息，在钩子运行时显示。                      |

### 根据钩子事件展开参数

使用 `${field.nested}` 从钩子事件中读取以点号分隔的路径所指定的字段。
占据整个值的占位符会保留其 JSON 类型。嵌在较长字符串中的占位符则会呈现为文本。
Codex 会递归展开对象和数组。

对于包含 `{"tool_input":{"file_path":"src/main.rs","count":3}}` 的事件，
以下参数模板：

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

将变为：

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### 执行与生命周期

- 钩子使用现有的 MCP 连接，不会启动服务器或重新连接服务器。
- 当工具返回阻止操作的决定时，钩子可以阻止该操作。错误、服务器缺失和工具不可用都不会阻止操作。
- MCP 工具钩子同步运行，不会请求工具审批，也不会触发其他钩子。
- 超时时间以钩子和服务器两者中较短的为准。等待 MCP 引导式提取响应的时间不计入超时时间。
- `SessionStart` 钩子可能在 MCP 服务器就绪前运行。
  在这种情况下，它们不会阻止会话。
- `SessionEnd` 不支持 MCP 工具钩子。

## 关闭钩子

默认启用钩子。要关闭钩子，请在 `config.toml` 中设置：

```toml
[features]
hooks = false

请使用 `hooks` 作为规范的功能键。`codex_hooks` 仍可作为已弃用的别名使用。
管理员也可以采用同样的方式强制关闭钩子，
即在 `requirements.toml` 中设置 `[features].hooks = false`。

## 来自 `requirements.toml` 的受管理钩子

企业管理的要求配置也可以在 `[hooks]` 下内联定义钩子。
当管理员希望强制实施钩子配置，
同时通过 MDM 或其他设备管理系统分发实际脚本时，这种方式很有用。
要对在本地禁用了钩子的用户也强制启用受管理的钩子，
请在 `requirements.toml` 中配置 `[hooks]` 的同时，强制设置 `[features].hooks = true`。
要忽略用户、项目、会话和插件钩子，同时仍允许管理员管理的钩子运行，
请设置 `allow_managed_hooks_only = true`。

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

受管理钩子的注意事项：

- macOS 和 Linux 使用 `managed_dir`。
- Windows 使用 `windows_managed_dir`。
- Codex 不负责分发 `managed_dir` 中的脚本；
  您必须通过企业工具单独安装和更新这些脚本。
- 受管理的钩子命令应使用脚本的绝对路径，且脚本应位于配置的受管理目录下。
- `allow_managed_hooks_only = true` 会跳过来自用户、项目、会话和插件的钩子，
  但仍会加载来自 `requirements.toml`
  以及其他受管理配置层的受管理钩子。

## 插件附带的钩子

启用插件后，Codex 可以加载该插件的生命周期钩子，同时加载用户钩子、项目钩子和受管理的钩子。

默认情况下，Codex 会在插件根目录中查找 `hooks/hooks.json`。
插件清单可以通过 `.codex-plugin/plugin.json` 中的 `hooks` 条目覆盖这一默认设置。
该清单条目可以是以 `./` 为前缀的路径、
以 `./` 为前缀的路径组成的数组、内联钩子对象，
或内联钩子对象组成的数组。

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

清单中的钩子路径以插件根目录为基准解析，
且必须位于该根目录内。如果清单定义了 `hooks`，Codex 会使用这些清单条目，
而不是默认的 `hooks/hooks.json`。

插件钩子命令会接收以下环境变量：

- `PLUGIN_ROOT` 是 Codex 专用扩展，
  指向已安装插件的根目录。
- `PLUGIN_DATA` 是 Codex 专用扩展，
  指向插件的可写数据目录。
- Codex 还会设置 `CLAUDE_PLUGIN_ROOT` 和 `CLAUDE_PLUGIN_DATA`，
  以兼容现有的插件钩子。

插件钩子使用与其他钩子相同的事件模式。安装或启用插件并不意味着自动信任其钩子；在您审查并信任当前钩子定义之前，Codex 会跳过插件附带的钩子。

## 匹配器模式

`matcher` 字段是一个正则表达式字符串，用于筛选钩子的触发时机。使用 `"*"`、
`""`，或完全省略 `matcher`，
即可匹配所支持事件的每一次触发。

目前只有部分 Codex 事件支持 `matcher`：

| 事件               | `matcher` 筛选的内容 | 备注                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | 工具名称              | 支持范围包括 `Bash`、`apply_patch`\* 和 MCP 工具名称 |
| `PostToolUse`       | 工具名称              | 请参阅[工具覆盖范围](#tool-coverage)                          |
| `PostCompact`       | 压缩触发方式     | 值为 `manual` 或 `auto`                                |
| `PreCompact`        | 压缩触发方式     | 值为 `manual` 或 `auto`                                |
| `PreToolUse`        | 工具名称              | 请参阅[工具覆盖范围](#tool-coverage)                          |
| `SessionEnd`        | 结束原因             | 目前仅为 `other`                                       |
| `SessionStart`      | 启动来源           | 值为 `startup`、`resume`、`clear` 和 `compact`       |
| `SubagentStart`     | 子智能体类型          | 值取决于所启动的子智能体                    |
| `SubagentStop`      | 子智能体类型          | 值取决于停止运行的子智能体                     |
| `UserPromptSubmit`  | 不支持          | 此事件会忽略任何已配置的 `matcher`           |
| `Stop`              | 不支持          | 此事件会忽略任何已配置的 `matcher`           |
| `Interrupt`         | 不支持          | 此事件会忽略任何已配置的 `matcher`           |

\*对于 `apply_patch`，`matcher` 的值也可以使用 `Edit` 或 `Write`。

示例：

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### 工具覆盖范围

`PreToolUse` 和 `PostToolUse` 可观测的调用不限于 shell 和 MCP 调用。
大多数本地函数工具都使用同一钩子路径，因此您可以匹配工具名称、
检查其 JSON 参数，并通过 `PreToolUse` 阻止或改写调用。

| 工具路径                         | `PreToolUse` | `PostToolUse` | 说明                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Shell 命令                    | 是          | 是           | 使用 `Bash` 匹配。                                                                                                         |
| 统一执行（`exec_command`）     | 是          | 是           | 使用 `Bash` 匹配。命令完成时，后续的 `write_stdin` 轮询可传递该原始命令的 `PostToolUse` 事件。 |
| `apply_patch`                     | 是          | 是           | 使用 `apply_patch`、`Edit` 或 `Write` 匹配。                                                                              |
| MCP 工具                         | 是          | 是           | 匹配 MCP 工具名称，例如 `mcp__filesystem__read_file`。                                                           |
| 其他本地函数工具        | 是          | 是           | 匹配函数工具名称，例如 `update_plan`。`spawn_agent` 也匹配 `Agent`。                                 |
| 托管工具，例如 `WebSearch` | 否           | 否            | 这些工具不经过本地函数工具的钩子路径。                                                                       |

`write_stdin` 是现有统一执行会话的传输通道。
对于已通过 `PreToolUse` 的命令，它在发送输入或轮询时，
不会再次运行 `PreToolUse`。

某些专用工具路径可以选择不经过默认的钩子路径。
请将工具钩子视为实用的防护机制，而非完整的强制执行边界。

## 通用输入字段

每个命令钩子都会通过 `stdin` 接收一个 JSON 对象。

以下是您通常会使用的共享字段：

| 字段             | 类型             | 含义                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | 当前 Codex 会话 ID。子智能体钩子使用父会话 ID。 |
| `transcript_path` | `string \| null` | 会话记录文件的路径（如果有）                         |
| `cwd`             | `string`         | 会话的工作目录                                   |
| `hook_event_name` | `string`         | 当前钩子事件名称                                             |
| `model`           | `string`         | Codex 特有扩展。当前使用的模型 Slug                         |

针对单个轮次的钩子会将 `turn_id` 作为 Codex 特有扩展，
列在各自的事件专用表中。

`SessionStart`、`PreToolUse`、`PermissionRequest`、`PostToolUse`、
`UserPromptSubmit`、`SubagentStart`、`SubagentStop`、`Stop` 和 `Interrupt` 还包含
`permission_mode`，用于描述当前权限模式，其值为 `default`、
`acceptEdits`、`plan`、`dontAsk` 或 `bypassPermissions`。

`transcript_path` 指向聊天记录，方便您使用，但
记录格式不是供钩子使用的稳定接口，以后可能会发生变化。

如需完整的传输格式，请参阅[模式](#schemas)。

## 通用输出字段

`SessionStart`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、
`SubagentStop` 和 `Stop` 支持以下通用 JSON 字段。`SubagentStart`
也接受相同结构的 `systemMessage` 和钩子特有上下文，但
`continue: false` 不会停止子智能体：

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| 字段            | 效果                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | 若为 `false`，则将本次钩子运行标记为已停止      |
| `stopReason`     | 记录为停止原因             |
| `systemMessage`  | 在界面或事件流中显示为警告 |
| `suppressOutput` | 目前会解析此字段，但尚未实现其功能            |

退出码为 `0` 且没有输出时，会被视为成功，Codex 会继续执行。

`PreToolUse` 和 `PermissionRequest` 支持 `systemMessage`，但这些事件目前不支持 `continue`、
`stopReason` 和 `suppressOutput`。
如果 `PreToolUse` 钩子返回其中一个不受支持的字段，Codex 会将
本次钩子运行标记为失败，报告错误，并继续执行工具调用。

`PostToolUse` 支持 `systemMessage`、`continue: false` 和 `stopReason`。
Codex 会解析 `suppressOutput`，但此事件目前尚不支持该字段。

### 超长钩子输出

默认情况下，Codex 会将每条模型可见的钩子输出消息限制在大约
2,500 个 Token 以内。如果钩子返回的内容超过此限制，Codex 会将完整文本保存到
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt`，并向模型提供包含文本开头和结尾的预览，
以及保存文件的路径。这种行为称为
**溢写**：Codex 将过长的输出存储在磁盘上，
并用较短的模型可见预览替代它。如果无法写入文件，
模型仍会收到截断后的预览。

  请保持钩子和插件的上下文简洁。多个钩子和插件的上下文
  会叠加，可能降低模型性能。调高 `additionalContextLimit`
  会增加这一风险。请避免将限制设为 `0`，除非钩子会
  严格执行输出上限；否则，
  单个钩子就可能占满整个上下文窗口。

对于任何返回 `additionalContext` 的命令钩子，
请在处理程序上设置 `additionalContextLimit`，
以自定义大致的 Token 数量阈值：

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

省略 `additionalContextLimit` 即可使用默认阈值（`2500` 个 Token）。
设置为正整数可指定其他阈值，设置为 `0` 则会将处理程序的
全部附加上下文直接传给模型。Codex 会独立评估
每个匹配的处理程序。对于无法生成附加上下文的事件，
Codex 会忽略 `additionalContextLimit`，
并报告配置警告。

该设置仅适用于 `additionalContext`。
工具反馈和用于继续执行的提示仍使用默认限制。

由于过长的输出可能会写入磁盘，请避免在钩子输出中返回机密信息或
其他敏感数据。

## 在后台运行钩子

默认情况下，Codex 会等待命令钩子完成，
再继续触发该钩子的操作。将 `async` 设为 `true`，
即可让命令钩子在后台运行，同时让 Codex 继续执行。

### 配置后台钩子

在 `hooks.json` 的命令处理程序中添加 `"async": true`：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

对于 `config.toml` 中的内联钩子，请设置 `async = true`：

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

后台钩子与同步命令钩子使用相同的输入、匹配器、信任审查、超时设置和
[超长输出处理机制](#large-hook-output)。与其他命令钩子一样，
`timeout` 以秒为单位，
默认值为 `600`。`Interrupt` 钩子的默认超时时间为 1 秒，最长为 3 秒，
在后台运行时也不例外。

### 后台钩子的运行方式

后台钩子完成后，Codex 会在对话中的下一个安全时机传递受支持的信息类输出：

- 如果当前有正在进行的轮次，Codex 会等待当前模型请求和工具调用完成，然后将输出提供给该轮次中的下一个模型请求。
- 如果当前没有正在进行的轮次，Codex 会等待下一个用户轮次。后台钩子完成不会触发新轮次。

请使用与同步钩子相同的事件专用 JSON 输出。
Codex 会将 `additionalContext` 添加到模型的上下文中，
并将 `systemMessage` 显示为警告。

  后台钩子无法阻止、批准、重写或以其他方式控制触发它们的操作。如需执行工具策略、做出权限决策、拒绝提示或继续轮次，请使用同步钩子。

### 限制

- 在每个会话中，Codex 最多同时运行八个后台钩子。其余钩子需等待正在运行的某个钩子完成。
- 每次匹配的调用都会独立运行，后台钩子的完成顺序可能与启动顺序不同。
- 会话结束时，Codex 会取消尚未完成的后台钩子，并丢弃尚未传递的输出。
- `SessionEnd` 钩子始终同步运行。

## 钩子

### SessionStart

对于此事件，`matcher` 应用于 `source`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段    | 类型     | 含义                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | 会话启动方式：`startup`、`resume`、`clear` 或 `compact` |

输出到 `stdout` 的纯文本会被添加为额外的开发者上下文。

输出到 `stdout` 的 JSON 支持[通用输出字段](#common-output-fields)以及以下
钩子专用结构：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

该 `additionalContext` 文本会被添加为额外的开发者上下文。

Codex 压缩根会话后，`SessionStart` 钩子若匹配
`source: "compact"`，就会在下一个模型请求前运行。这也适用于
轮次中途发生自动压缩的情况：Codex 会将钩子的
附加上下文传递给紧接着的续接请求，而不会等待
后续用户轮次。如果钩子返回 `continue: false`，Codex 会结束该轮次，
不再发送模型请求。

### SessionEnd

`SessionEnd` 可让您在会话结束时运行命令，例如保存最终笔记
或清理文件。当您归档或
删除仍处于打开状态的对话、Codex 正常关闭，或者对话
连续 30 分钟处于闲置状态且未在任何已连接的客户端中打开时，
它会针对主线程运行。它不会针对子智能体运行。

从当前对话切换到其他界面或调用 `thread/unsubscribe` 不会立即
结束会话，因此也不会立即运行 `SessionEnd`。您的钩子在运行期间
仍可读取会话记录。

对于此事件，`matcher` 用于筛选 `reason`。目前，`reason` 始终为 `other`。
您可以省略 `matcher`，或将其设为 `other`，让钩子在每次 `SessionEnd` 事件发生时运行。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段    | 类型     | 含义                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | 会话结束的原因：`other` |

例如，`SessionEnd` 命令会收到以下内容：

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

`SessionEnd` 钩子始终同步运行，即使 `async` 为 `true` 也是如此。
它们仅起建议作用，因此其输出不会引导 Codex 的行为，也不会让线程保持打开状态。
如果命令超时或因错误退出，Codex 会将其报告为钩子失败。

### SubagentStart

对于此事件，`matcher` 应用于 `agent_type`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段             | 类型     | 含义                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Codex 特有扩展。当前活动的 Codex 轮次 ID |
| `agent_id`        | `string` | 子智能体的标识符                    |
| `agent_type`      | `string` | 子智能体类型或配置方案                       |
| `permission_mode` | `string` | 当前权限模式                        |

输出到 `stdout` 的纯文本会被添加为子智能体的额外开发者上下文。

输出到 `stdout` 的 JSON 支持 `systemMessage` 和以下钩子专用结构：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

该 `additionalContext` 文本会被添加为子智能体的额外开发者上下文。
系统会解析 `continue: false` 以保持兼容性，
但这不会阻止子智能体启动。

### PreToolUse

`PreToolUse` 可拦截 Bash、通过 `apply_patch` 执行的文件编辑、
MCP 工具调用以及其他本地函数工具。有关支持的调用路径和例外情况，请参阅[工具
覆盖范围](#tool-coverage)。

`matcher` 应用于 `tool_name` 和匹配器别名。
对于通过 `apply_patch` 进行的文件编辑，`matcher` 的值可以是 `apply_patch`、`Edit` 或 `Write`；
钩子输入仍会报告 `tool_name: "apply_patch"`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段         | 类型         | 含义                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Codex 特有扩展。当前活动的 Codex 轮次 ID                                                                                   |
| `tool_name`   | `string`     | 钩子使用的规范工具名称，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 这样的 MCP 名称                                     |
| `tool_use_id` | `string`     | 此次调用的工具调用 ID                                                                                                 |
| `tool_input`  | `JSON value` | 工具专用输入。`Bash` 和 `apply_patch` 使用 `tool_input.command`。MCP 工具和其他本地函数工具会发送各自的参数。 |

输出到 `stdout` 的纯文本会被忽略。

写入 `stdout` 的 JSON 可以使用 `systemMessage`。要拒绝受支持的工具调用，请返回
以下钩子专用结构：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex 也接受以下旧版阻止调用格式：

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

您也可以使用退出码 `2`，并将阻止原因写入 `stderr`。

要在不阻止调用的情况下添加模型可见的上下文，请返回
`hookSpecificOutput.additionalContext`：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

要在不阻止调用的情况下重写受支持的工具调用，请返回
`permissionDecision: "allow"`，并附带 `updatedInput`：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

对于 Bash 命令和 `apply_patch`，`updatedInput` 必须包含一个
字符串类型的 `command` 字段。对于 MCP 和其他本地函数工具，`updatedInput` 是
用于替换原参数的对象。返回 `updatedInput` 时，
必须同时返回 `permissionDecision: "allow"`；其他 `updatedInput` 结构
会被报告为错误。

`permissionDecision: "ask"`、旧版 `decision: "approve"`、`continue: false`、
`stopReason` 和 `suppressOutput` 会被解析，但尚不受支持。Codex 会
将此次钩子运行标记为失败、报告错误，并继续执行工具调用。

### PermissionRequest

当 Codex 即将请求审批时，`PermissionRequest` 会运行，例如
请求提升 shell 权限或受管网络审批时。它可以允许请求、
拒绝请求，或不做决定，让常规审批提示照常显示。
不需要审批的命令不会触发此钩子。

`matcher` 用于匹配 `tool_name` 及其匹配别名。当前的规范值
包括 `Bash`、`apply_patch` 和 MCP 工具名称，例如
`mcp__server__tool`；`apply_patch` 也匹配 `Edit` 和 `Write`。

除[通用输入字段](#common-input-fields)外，还包括以下字段：

| 字段                    | 类型             | 含义                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Codex 特有扩展。当前活跃的 Codex 轮次 ID                                                                 |
| `tool_name`              | `string`         | 钩子使用的规范工具名称，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 这样的 MCP 名称                   |
| `tool_input`             | `JSON value`     | 工具专用输入。`Bash` 和 `apply_patch` 使用 `tool_input.command`，MCP 工具则发送所有参数。 |
| `tool_input.description` | `string \| null` | 审批原因的文字说明（如果 Codex 提供）                                                             |

写入 `stdout` 的纯文本会被忽略。

某些工具输入可能包含文字描述，但不能假定所有工具都有
`tool_input.description` 字段。

要批准请求，请返回：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

要拒绝请求，请返回：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

如果多个匹配的钩子返回决策结果，只要有 `deny`，就以其为准。否则，
`allow` 会让请求继续执行，而不显示审批提示。如果没有
匹配的钩子做出决定，Codex 会使用常规审批流程。

请勿返回 `updatedInput`、`updatedPermissions` 或 `interrupt` 来响应
`PermissionRequest`；这些字段是为未来行为预留的，
目前返回它们会导致请求被拒绝。

### PostToolUse

在受支持的工具产生输出后，`PostToolUse` 会运行，支持范围包括 Bash、
`apply_patch`、MCP 工具调用和其他本地函数工具。对于 Bash，
即使命令以非零状态退出，它也会运行。它无法撤销
已运行工具产生的副作用。请参阅[工具覆盖范围](#tool-coverage)，了解
受支持的调用路径及例外情况。

`matcher` 用于匹配 `tool_name` 及其匹配别名。对于通过
`apply_patch` 进行的文件编辑，`matcher` 的值可以是 `apply_patch`、`Edit` 或 `Write`；钩子输入
仍会报告 `tool_name: "apply_patch"`。

除[通用输入字段](#common-input-fields)外，还包括以下字段：

| 字段           | 类型         | 含义                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Codex 特有扩展。当前活跃的 Codex 轮次 ID                                                                                   |
| `tool_name`     | `string`     | 钩子使用的规范工具名称，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 这样的 MCP 名称                                     |
| `tool_use_id`   | `string`     | 本次调用的工具调用 ID                                                                                                 |
| `tool_input`    | `JSON value` | 工具专用输入。`Bash` 和 `apply_patch` 使用 `tool_input.command`。MCP 和其他本地函数工具会发送其参数。 |
| `tool_response` | `JSON value` | 工具专用输出。MCP 工具会发送 MCP 调用结果。其他本地函数工具通常会发送提供给模型的输出。    |

写入 `stdout` 的纯文本会被忽略。

写入 `stdout` 的 JSON 可以使用 `systemMessage` 和以下钩子专用结构：

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

`additionalContext` 中的文本会被添加为额外的开发者上下文。

对于此事件，`decision: "block"` 不会撤销已执行完毕的 Bash 命令。
Codex 会记录反馈，并用该反馈替换工具结果，
然后让模型基于钩子提供的消息继续运行。

您也可以使用退出码 `2`，并将反馈原因写入 `stderr`。

要在命令已经运行后停止对原始工具结果的常规处理，
请返回 `continue: false`。Codex 会将工具结果替换为
您的反馈或停止说明，然后据此继续运行。

`updatedMCPToolOutput` 和 `suppressOutput` 会被解析，但尚不受支持。
Codex 会将此次钩子运行标记为失败、报告错误，并继续按常规方式
处理工具结果。

#### 代码模式中的工具调用

当模型使用代码模式通过 JavaScript 调用工具时，钩子的决策会应用于
该嵌套调用。`PreToolUse` 可以在工具运行前阻止其执行，或重写
其输入。阻止调用的 `PostToolUse` 无法撤销工具的副作用，但
可以阻止原始结果传递给正在运行的脚本。

| 钩子结果                                                      | 代码模式中的表现                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` 阻止调用                                              | 工具调用的 Promise 会在工具运行前被拒绝。                                                         |
| `PreToolUse` 返回 `updatedInput`                              | 工具使用重写后的输入运行，Promise 会以该运行结果兑现。                      |
| `PostToolUse` 返回 `decision: "block"`，或以退出码 `2` 退出 | 工具运行后，该 Promise 会以钩子给出的原因被拒绝。                                          |
| `PostToolUse` 返回 `continue: false`                          | Codex 使用钩子反馈作为模型可见的结果，但不会拒绝嵌套工具调用的 Promise。 |

### PreCompact

`PreCompact` 在 Codex 压缩聊天之前运行。`matcher` 用于匹配
`trigger`，其取值为 `manual` 或 `auto`。

除[通用输入字段](#common-input-fields)外，还包括以下字段：

| 字段     | 类型     | 含义                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 特有扩展。当前活跃的 Codex 轮次 ID |
| `trigger` | `string` | 压缩的触发方式：`manual` 或 `auto`  |

写入 `stdout` 的纯文本会被忽略。

`stdout` 上的 JSON 支持[通用输出字段](#common-output-fields)。
如果匹配的 `PreCompact` 钩子返回 `continue: false`，
Codex 会在压缩前停止。

### PostCompact

`PostCompact` 在 Codex 压缩聊天后运行。`matcher` 应用于
`trigger`，其值为 `manual` 和 `auto`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段     | 类型     | 含义                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 专用扩展。当前活跃的 Codex 轮次 ID |
| `trigger` | `string` | 触发压缩的方式：`manual` 或 `auto`  |

`stdout` 上的纯文本会被忽略。

`stdout` 上的 JSON 支持[通用输出字段](#common-output-fields)。
如果匹配的 `PostCompact` 钩子返回 `continue: false`，
Codex 会在压缩后停止。

### UserPromptSubmit

此事件目前不使用 `matcher`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段     | 类型     | 含义                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 专用扩展。当前活跃的 Codex 轮次 ID |
| `prompt`  | `string` | 即将发送的用户提示            |

`stdout` 上的纯文本会作为额外的开发者上下文添加。

`stdout` 上的 JSON 支持[通用输出字段](#common-output-fields)，以及
以下钩子专用结构：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

该 `additionalContext` 文本会作为额外的开发者上下文添加。

要拦截该提示，请返回：

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

您也可以使用退出代码 `2`，并将拦截原因写入 `stderr`。

### SubagentStop

对于此事件，`matcher` 应用于 `agent_type`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段                    | 类型             | 含义                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Codex 专用扩展。当前活跃的 Codex 轮次 ID  |
| `agent_id`               | `string`         | 子智能体的标识符                     |
| `agent_type`             | `string`         | 子智能体类型或配置方案                        |
| `agent_transcript_path`  | `string \| null` | 子智能体对话记录文件的路径（如有）    |
| `stop_hook_active`       | `boolean`        | 是否已让此子智能体继续运行     |
| `last_assistant_message` | `string \| null` | 子智能体的最新助手消息（如有） |

`SubagentStop` 以退出代码 `0` 退出时，应向 `stdout` 输出 JSON。
此事件不接受纯文本输出。

`stdout` 上的 JSON 支持[通用输出字段](#common-output-fields)。
要让 Codex 继续执行子智能体流程，请返回：

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

您也可以使用退出代码 `2`，并将继续运行的原因写入 `stderr`。

如果任一匹配的 `SubagentStop` 钩子返回 `continue: false`，
该结果会优先于其他匹配的 `SubagentStop` 钩子
做出的继续运行决定。

### Stop

此事件目前不使用 `matcher`。

除[通用输入字段](#common-input-fields)外，还有以下字段：

| 字段                    | 类型             | 含义                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Codex 专用扩展。当前活跃的 Codex 轮次 ID    |
| `stop_hook_active`       | `boolean`        | 此轮次是否已通过 `Stop` 继续运行 |
| `last_assistant_message` | `string \| null` | 最新的助手消息文本（如有）       |

`Stop` 以退出代码 `0` 退出时，应向 `stdout` 输出 JSON。
此事件不接受纯文本输出。

`stdout` 上的 JSON 支持[通用输出字段](#common-output-fields)。
要让 Codex 继续运行，请返回：

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

您也可以使用退出代码 `2`，并将继续运行的原因写入 `stderr`。

对于此事件，`decision: "block"` 不会拒绝该轮次，而是让
Codex 继续运行，并自动创建一条用于继续运行的新提示，
将其作为新的用户提示，提示文本为您提供的 `reason`。

如果任一匹配的 `Stop` 钩子返回 `continue: false`，
该结果会优先于其他匹配的 `Stop` 钩子做出的继续运行决定。

### Interrupt

当您中断主线程中正在运行的轮次时，`Interrupt` 会运行。
您可以用它记录中断，或清理由钩子启动的工作。
它不会针对空闲线程或子智能体运行，且会忽略任何已配置的 `matcher`。

除[通用输入字段](#common-input-fields)外，此事件还包含
`turn_id`（被中断轮次的 ID）和 `permission_mode`。

命令钩子的默认超时时间为 1 秒。
配置的超时时间仅限 1 到 3 秒。
钩子输出无法阻止中断，也无法重新启动该轮次。请以退出代码 `0` 退出，不输出任何内容；
或者返回 JSON，其中可包含 `systemMessage` 来显示警告。
此事件不接受纯文本输出。

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## 模式

  链接指向的 `main` 分支中的模式可能包含当前版本中没有的钩子字段。
  当前版本的行为请以本页为准。

如果您需要当前的确切传输格式，请查看
[Codex GitHub 代码仓库](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated)中生成的模式。
