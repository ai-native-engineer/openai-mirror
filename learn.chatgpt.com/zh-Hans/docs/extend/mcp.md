<!-- source: https://learn.chatgpt.com/zh-Hans/docs/extend/mcp -->

模型上下文协议（MCP）将模型与工具和上下文连接起来。您可以使用该协议，让 ChatGPT 或 Codex 访问第三方文档，或与浏览器、Figma 等开发者工具交互。

ChatGPT 网页版可以使用插件提供的远程 MCP 工具。本地 Codex 客户端也可以直接连接到 MCP 服务器，并共享 MCP 配置。

<a id="supported-mcp-features"></a>

ChatGPT 桌面应用、Codex CLI 和 IDE 扩展均支持 MCP 服务器，并共享同一 Codex 主机上的 MCP 配置。

以下受支持的服务器功能适用于在 Codex 主机上配置的 MCP 服务器。托管的插件工具可能具备不同的能力。

## 支持的 MCP 功能

- **STDIO 服务器**：作为本地进程运行的服务器（通过命令启动）。
  - 环境变量
- **Streamable HTTP 服务器**：通过地址访问的服务器。
  - Bearer Token 身份验证
  - OAuth 身份验证，包括客户端 ID 元数据文档（CIMD）和动态客户端注册（DCR）
  - 适用于受信任第一方服务器的 ChatGPT 会话身份验证
- **服务器指令**：Codex 会读取初始化期间返回的 MCP `instructions` 字段，并将其作为适用于整个服务器的指引，与服务器工具一同使用。

如果您为 Codex 构建或维护 MCP 服务器，请使用 `instructions` 说明适用于整个服务器的跨工具工作流、约束和速率限制。请确保前 512 个字符的内容能够独立理解，以便 Codex 在决定如何使用服务器时获取最重要的指引。

## 将 Codex 连接到 MCP 服务器

Codex 将 MCP 配置与其他 Codex 配置设置一并存储在 `config.toml` 中。默认路径为 `~/.codex/config.toml`，您也可以通过 `.codex/config.toml` 将 MCP 服务器的配置限定在项目范围内（仅限受信任的项目）。

ChatGPT 桌面应用、Codex CLI 和 IDE 扩展共享这一配置。完成 MCP 服务器配置后，您可以在这些客户端之间切换，无需重新设置。

### 在 ChatGPT 桌面应用中配置

1. 打开 **设置**，然后选择 **MCP 服务器**。
2. 选择 **添加服务器**。
3. 输入名称，选择 **STDIO** 或 **Streamable HTTP**，并提供
   服务器的命令或 URL。
4. 保存服务器，然后选择 **重新启动**。

服务器列表会显示哪些服务器已启用，以及哪些需要 OAuth。
OAuth 服务器需要登录时，请选择**身份验证** 。在编辑器中输入 `/mcp`，
即可查看已连接的服务器。

## 在 ChatGPT 网页版中使用基于 MCP 的工具

在托管的 ChatGPT Work 聊天中，安装[插件](/zh-Hans/codex/plugins)即可使用其
随附的连接器和远程 MCP 工具。安装后，聊天和 Work 均可
使用这些工具。工作空间管理员可以控制
哪些插件和工具可供使用。

ChatGPT 网页版不会读取本地 Codex 配置文件，也不会显示本地
Codex 命令菜单。打开 **插件** 标签页，
浏览并管理可用工具。

### 使用 CLI 配置

#### 添加 MCP 服务器

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

例如，要添加 Context7（面向开发者文档的免费 MCP 服务器），您可以运行以下命令：

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### 其他 CLI 命令

运行 `codex mcp list` 可查看已配置的服务器。
要查看所有可用的 MCP 命令，请运行 `codex mcp --help`。对于支持 OAuth 的服务器，请运行
`codex mcp login <server-name>`。

#### 终端用户界面（TUI）

在 `codex` TUI 中，使用 `/mcp` 可查看当前活动的 MCP 服务器。

### 在 IDE 扩展中配置

1. 打开齿轮图标菜单，然后选择 **MCP 服务器**。
2. 选择 **添加服务器**。
3. 输入名称，选择 **STDIO** 或 **Streamable HTTP**，并提供
   服务器的命令或 URL。
4. 保存服务器，然后选择 **重新启动扩展**。

MCP 服务器列表会显示哪些服务器已启用，以及哪些需要 OAuth。
OAuth 服务器需要登录时，请选择 **身份验证** 。

### 使用 config.toml 配置

如需更精细的控制，请编辑 `~/.codex/config.toml` 或项目级的
`.codex/config.toml`。请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference)，
其中列出了所有受支持的 MCP 选项，并支持搜索。

在配置文件中，使用 `[mcp_servers.<server-name>]` 表配置每个 MCP 服务器。

<a id="stdio-servers"></a>

#### STDIO 服务器

- `command`（必需）：用于启动服务器的命令。
- `args`（可选）：要传递给服务器的参数。
- `env`（可选）：要为服务器设置的环境变量。
- `env_vars`（可选）：允许转发的环境变量。
- `cwd`（可选）：启动服务器时使用的工作目录。
- `experimental_environment`（可选）：设为 `remote` 后，若有可用的远程执行器环境，
  将通过该环境启动 stdio 服务器。

`env_vars` 可包含普通变量名或指定了来源的对象：

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

字符串条目以及指定 `source = "local"` 的条目会从 Codex 的本地环境中读取值。
指定 `source = "remote"` 的条目会从远程执行器环境中读取值，并且需要
远程 MCP stdio。

<a id="streamable-http-servers"></a>

#### Streamable HTTP 服务器

- `url`（必需）：服务器地址。
- `auth`（可选）：在尝试已配置的 Bearer Token 和
  授权标头之后尝试的身份验证方式。使用 `oauth`（默认值）可采用已存储的 MCP OAuth
  凭据。使用 `chatgpt` 可对受信任的
  第一方 ChatGPT 源使用当前 ChatGPT 会话，并以已存储的 OAuth 凭据作为后备方案。
- `bearer_token_env_var`（可选）：存放 Bearer Token 的环境变量名称，该 Token 将在 `Authorization` 中发送。
- `http_headers`（可选）：标头名称到静态值的映射。
- `env_http_headers`（可选）：标头名称到环境变量名称的映射（值从环境中获取）。
- `http_headers_helper`（可选）：本地命令，用于输出以
  标头名称为键、字符串为值的 JSON 对象，例如 `{"X-Auth": "temporary-token"}`。
  支持从本地环境建立的 HTTP MCP 连接；不支持
  stdio 服务器或通过远程执行环境建立的连接。

Codex 会为连接缓存辅助程序提供的标头。当同源 POST 请求
返回 `401` 或 `403` 时，Codex 会刷新一次标头，并且仅在
辅助程序返回的值发生变化时重试。显式设置的 Bearer Token 和 OAuth 凭据
优先于辅助程序提供的 `Authorization` 标头。
报告授权范围不足的 OAuth `403` 响应不会
触发辅助程序刷新。

如果无法从任何凭据来源获取凭据，Codex 可以不经
身份验证连接到服务器。请单独运行 `codex mcp login <server-name>`，发起 MCP
OAuth 登录。

#### 其他配置选项

- `startup_timeout_sec`（可选）：服务器启动的超时时间（秒）。默认值：`10`。
- `tool_timeout_sec`（可选）：服务器运行工具的超时时间（秒）。默认值：`60`。
- `enabled`（可选）：设为 `false` 可停用服务器，而不删除它。
- `required`（可选）：设为 `true` 后，如果此已启用的服务器无法初始化，启动就会失败。
- `enabled_tools`（可选）：工具允许列表。
- `disabled_tools`（可选）：工具拒绝列表（在 `enabled_tools` 之后应用）。
- `default_tools_approval_mode`（可选）：此服务器提供的
  工具的默认审批行为。支持的值为 `auto`、`prompt`、`writes` 和
`approve`。`writes` 模式会对未标记为只读的工具请求审批。
- `tools.<tool>.approval_mode`（可选）：针对单个工具的审批行为覆盖设置。
- `tools.<tool>.output_token_limit`（可选）：单个工具输出的 Token 预算，
  必须为正数，且不包含标准的 20% 序列化余量。此设置会覆盖
  模型针对该工具的默认输出截断预算。

顶层设置 `mcp_optional_startup_grace_ms` 控制 Codex 在构建初始工具目录时
等待可选 MCP 服务器的时长。
默认值为 `1000` 毫秒。将其设为 `0`，则改为按各服务器的
`startup_timeout_sec` 等待。必需的服务器仍使用各自的
启动超时时间。

#### OAuth 客户端注册和回调

如果您的授权服务器要求使用预注册的 OAuth 客户端，请在添加 MCP 服务器时提供其客户端 ID：

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex 会显示需要在您的提供商处注册的完整回调 URL：

```text
OAuth callback URL: http://127.0.0.1/callback

Codex 会将回调地址和客户端 ID 一同保存在 `config.toml` 中，供后续
登录使用：

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

新添加的预注册客户端只有在
授权服务器声明
`authorization_response_iss_parameter_supported: true`，并在元数据中提供
`issuer` 时，才会使用稳定的回调地址。如果未声明支持颁发者标识，Codex 会附加服务器专用的
回调 ID，例如 `http://127.0.0.1/callback/XuuuHAzzHOni`。未保存回调地址的现有客户端
会继续使用包含各自回调 ID 的重定向地址。

登录时，回调地址的选择取决于 OAuth 配置和授权服务器元数据：

| OAuth 配置                                                | 颁发者标识支持           | 使用的回调地址                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 已配置 `callback_url`，但未配置 `client_id`                                 | 支持                | 使用配置的回调地址进行客户端注册。                                                                                           |
| 已配置 `callback_url`，但未配置 `client_id`                                 | 不支持              | 在配置的回调地址后附加服务器专用的回调 ID，并用于客户端注册。                                             |
| 已配置 `client_id` 和 `callback_url`                                     | 支持                | 复用配置的回调地址；授权响应必须包含匹配的 `iss`。                                                     |
| 已配置 `client_id`，以及以正确回调 ID 结尾的 `callback_url` | 不支持              | 原样复用配置的回调地址。                                                                                                       |
| 已配置 `client_id`，以及缺少正确回调 ID 的 `callback_url`   | 不支持              | 忽略配置的回调地址。Codex 使用 `mcp_oauth_callback_url`，未设置时则使用 `http://127.0.0.1/callback`，并在地址后附加回调 ID。 |
| 已配置 `client_id`，但未配置 `callback_url`                    | 支持或不支持 | Codex 使用全局配置的回调地址或默认回调地址，并在其后附加服务器专用的回调 ID。                                                           |

此回退行为不会修改已存储的回调 URL。Codex 根据 MCP 服务器 URL（包括其路径和查询字符串）派生回调 ID。自动登录和显式登录适用相同的选择规则。

如果您需要自定义回调路径或远程
Devbox 入口 URL，请设置 `mcp_oauth_callback_url`。新添加的预注册客户端会原样使用该 URL，
前提是其提供商支持颁发者标识。否则，它们会在
配置的 URL 后附加服务器专用的回调 ID。请务必注册
与 `codex mcp add` 显示的内容完全一致的回调地址。

对于不含端口的 `http://127.0.0.1` 回调地址，Codex 会在
显示和存储的 URL 中省略监听端口，并在
授权期间插入当前使用的监听端口。这种替换不适用于 `localhost`、IPv6 主机、
HTTPS URL 或已包含端口的回调地址。授权服务器
必须按照
[RFC 8252 第 7.3 节](https://www.rfc-editor.org/rfc/rfc8252#section-7.3)的要求接受可变的环回端口。

设置 `mcp_oauth_callback_port` 可指定固定的全局监听端口，也可以设置
`mcp_servers.<server-name>.oauth.callback_port` 来为单个服务器覆盖该端口。
在回调 URL 中显式指定端口并不会配置监听器。
直接通过环回地址接收回调时，请使用不含端口的 `http://127.0.0.1`，或为回调 URL 和监听器
显式配置相同的端口。使用代理时，回调的外部 URL 端口可以
按需设置为与本地监听端口不同的值。
本地回调 URL 绑定到本地接口；非本地回调 URL
绑定到 `0.0.0.0`。

Codex 会先验证返回的 `iss`，再进行授权码交换。
如果 `iss` 不匹配，Codex 始终会拒绝该响应。如果已声明支持颁发者标识，
缺少 `iss` 也会导致响应被拒绝。这两种失败情况都不会进行授权码交换，也不会
回退到其他回调地址。回调 URL 格式错误，或声明支持颁发者标识
却未在元数据中提供颁发者，也仍会导致流程直接失败。请参阅
[用户身份验证](/plugins/build/auth)。

如果 MCP 服务器声明了 `scopes_supported`，Codex 会在 OAuth 登录时优先使用
服务器声明的这些作用域。否则，Codex 会回退到
`config.toml` 中配置的作用域。

#### OAuth 客户端注册

Codex 支持 [OAuth 客户端 ID 元数据文档（CIMD）](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
和动态客户端注册（DCR）。默认情况下，Codex 会在以下条件都满足时自动选择
CIMD：授权服务器声明
`client_id_metadata_document_supported: true`、将 `none` 列入
`token_endpoint_auth_methods_supported`，且回调使用受支持的
环回 URL。否则，如果 DCR 可用，Codex 会使用 DCR。已配置的 OAuth 客户端
ID 始终优先，并会跳过客户端注册。

对于 CIMD，Codex 使用由 ChatGPT 托管、专用于相应 MCP 服务器的元数据文档：

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex 根据 MCP 服务器 URL 派生 `<callback_id>`，并将其包含在
环回重定向 URI 中，例如
`http://127.0.0.1:<port>/callback/<callback_id>`。元数据文档会注册
相应的不含端口的环回 URI。授权服务器必须接受
登录时选择的端口，并精确匹配主机和路径，以符合
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3) 的要求。自定义
回调主机、路径或查询参数需要使用 DCR 或已配置的 OAuth
客户端 ID。

对稳定、共享的 CIMD 文档的支持正在开发中，即将推出：

```text
https://chatgpt.com/oauth/codex/client.json

Codex 将使用包含共享 `/callback` 路径的稳定文档，前提是
授权服务器声明
`authorization_response_iss_parameter_supported: true`，在元数据中提供有效的
`issuer`，并在授权响应中包含匹配的 `iss`。
未提供与颁发者绑定的响应的服务器将继续使用
回调专用文档。

如需为单次 CLI 登录选择注册方式，请使用
`--oauth-client-registration`：

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

默认值为 `auto`。所选注册方式仅适用于当前登录，
不会存储在 `config.toml` 中。

#### config.toml 示例

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### 插件提供的 MCP 服务器

已安装的插件可以在插件清单中捆绑 MCP 服务器。
这些服务器由插件启动，因此用户配置不会设置其
传输命令。用户配置仍可在
`plugins.<plugin>.mcp_servers.<server>` 下控制启用或停用状态和工具策略。

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

插件提供的 HTTP MCP 服务器也可以在 `.mcp.json` 中声明 OAuth 设置。
插件清单使用小驼峰式字段名 `clientId`、`callbackUrl` 和
`callbackPort`：

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

插件提供的 MCP 服务器与其他
MCP 服务器遵循相同的回调选择规则。如果插件提供了 `clientId`，其提供商不支持
与颁发者绑定的回调，且 `callbackUrl` 缺少服务器专用的回调
ID，Codex 会在此次登录中忽略该 URL，改用 `mcp_oauth_callback_url`，或在未设置时使用
`http://127.0.0.1/callback`，并在地址后附加回调 ID。
已配置的 `callbackUrl` 保持不变。

插件的 `oauth.callbackPort` 会覆盖全局
`mcp_oauth_callback_port`；如果两者均未设置，Codex 会选择一个临时端口。
`callbackUrl` 中的端口不会决定监听端口。
要通过固定的环回端口直接接收回调，请确保两处配置的端口一致：

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

使用远程入口或其他代理时，只要代理将请求转发到已配置的监听器，就可以按需为回调 URL 和本地监听器设置不同的端口。

## 实用的 MCP 服务器示例

MCP 服务器的数量仍在不断增加。以下是几个常用示例：

- [OpenAI 文档 MCP](/learn/docs-mcp)：搜索并阅读 OpenAI 开发者文档。
- [Context7](https://github.com/upstash/context7)：连接到最新的开发者文档。
- Figma [本地](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)和[远程](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)：访问您的 Figma 设计。
- [Playwright](https://www.npmjs.com/package/@playwright/mcp)：使用 Playwright 控制和检查浏览器。
- [Chrome 开发者工具](https://github.com/ChromeDevTools/chrome-devtools-mcp/)：控制和检查 Chrome。
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex)：访问 Sentry 日志。
- [GitHub](https://github.com/github/github-mcp-server)：管理 `git` 支持范围之外的 GitHub 功能（例如 Pull Request 和议题）。
