<!-- source: https://learn.chatgpt.com/zh-Hans/docs/permissions -->

Beta 版。权限配置方案正在积极开发中，可能会发生变化。

  权限配置方案不能与旧版沙盒设置组合使用。请仅配置
  `default_permissions` 和 `[permissions]`，或者 `sandbox_mode` /
`sandbox_workspace_write` 中的一组，不要同时配置两组。如果 `sandbox_mode` 出现在任一
  已加载的配置文件中，或者您传入 `--sandbox`，或者所选配置方案设置了
`sandbox_mode`，Codex 会使用这些旧版沙盒设置，而不会使用
`default_permissions`。

托管的 `allowed_permission_profiles` 是例外：它会让 Codex 使用
权限配置方案。部署托管的配置方案允许列表之前，请移除
`sandbox_mode` 和 `[sandbox_workspace_write]` 等旧版设置。
对于混合版本的企业部署，您可以保留
托管的 `allowed_sandbox_modes` 要求，作为临时兼容性
约束，直到所有客户端都运行 Codex 0.138.0 或更高版本。

权限配置方案可让您对 Codex 代您运行的本地命令
施加最小权限边界。配置方案是一项命名策略，用于结合文件系统
规则与网络规则：文件系统规则定义命令可读取或写入的内容，网络
规则定义命令可以访问的目标。

  配置方案中的 `network.enabled = true` 允许命令访问网络，但
  不会启动网络代理。要执行配置方案的域名规则，还需在
`config.toml` 中设置 `features.network_proxy = true`，或者使用已启用且
  由管理员托管的 `[experimental_network]` 要求。如果没有运行中的
  代理，配置方案的域名规则不会限制直接网络访问。

通过配置方案，您可以仅向 Codex 授予当前聊天所需的权限，
而无需授予其对您计算机或网络的广泛访问权限。例如，只读配置方案可以
让 Codex 检查项目而不能编辑项目，具备写入权限的配置方案
则可以将编辑范围限制在选定的工作空间根目录内。

macOS、Linux、WSL 和原生
Windows 均支持本地权限配置方案。请参阅[范围和强制执行](#scope-and-enforcement)，了解特定于平台的
详细信息和注意事项。

有关 Codex 云端的网络设置，请参阅[互联网访问](/zh-Hans/codex/cloud/internet-access)。

## 定义并选择配置方案

Codex 内置三种权限配置方案：

- `:read-only` 使本地命令以只读方式执行。
- `:workspace` 允许写入活动工作空间根目录和系统临时目录。
- `:danger-full-access` 会移除本地沙盒限制，
  仅应在您有意授予此类广泛访问权限时使用。

在 `[permissions.<name>]` 下创建命名配置方案，然后将顶层
`default_permissions` 键设置为该配置方案的名称，或上述某个内置配置方案的名称。
在此示例中，`project-edit` 是用户定义的配置方案名称，而不是内置
值。

企业管理员可以通过托管配置
`requirements.toml` 定义配置方案，并限制用户可选择的配置方案。一旦配置了
`allowed_permission_profiles`，未列出的配置方案一律不可使用，
其中包括未列出的内置配置方案，以及未来 Codex 版本中新增的配置方案。请参阅
[控制可用的权限配置方案](/zh-Hans/codex/enterprise/managed-configuration#control-available-permission-profiles)，
了解推荐的托管配置。

自定义配置方案涉及两个相关概念：

- `[permissions.<name>.workspace_roots]` 可添加特定目录，作为该配置方案的
  工作空间根目录。
- `[permissions.<name>.filesystem.":workspace_roots"]` 定义 Codex 在每个实际生效的工作空间根目录中应用的文件系统
  规则，这些根目录包括当前
  会话的运行时工作空间根目录，以及上述由配置方案定义的根目录。

配置方案也使用常规配置分层模型。优先级更高的层可以
在同一配置方案名称下添加或替换条目，而无需重新声明整个
配置方案。

例如，组织级配置和用户级配置可以分别扩展
同一个配置方案：

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

启用 `server` 后，两个工作空间根目录都会纳入生效的
配置方案。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

此配置方案会：

- 读取常用开发者工具所需的最少运行时路径。
- 将相同的工作空间根目录规则应用于当前会话，以及
由配置方案定义的根目录。
- 确保 `.devcontainer/` 等 IDE 相关设置在每个
  根目录下保持只读。
- 通过 glob 规则拒绝访问匹配的环境文件。
- 仅允许按已配置的域名策略访问网络。

在已启用的配置方案中，即使范围更广的
路径可读或可写，范围更窄的拒绝规则仍然有效。例如，配置方案可以使工作空间根目录
可写，同时将匹配的 `.env` 路径设为 `deny`。

## 扩展配置方案

如果配置方案与内置配置方案或其他命名配置方案基本一致，请使用 `extends`。
优先扩展内置配置方案，而不是从头创建，
以沿用基础防护。例如，扩展 `:workspace` 会让
工作空间根目录中的 `.codex` 目录保持只读，除非您明确
覆盖此设置。只需设置一次父配置方案，然后仅添加或覆盖
存在差异的规则。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

此配置方案以 `:workspace` 为基础，继续拒绝访问匹配的 `.env` 文件，并
允许向 `api.openai.com` 发出请求。配置方案可以扩展 `:read-only`、
`:workspace` 或其他命名配置方案，但不能扩展
`:danger-full-access`；Codex 还会拒绝未知的父配置方案和继承
循环。

## 配置规范

| 条目                                                             | 类型/值              | 默认值                 | 详细信息                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | 字符串形式的配置方案名称        | 无                    | 指定 Codex 默认应用的权限配置方案。它必须匹配 `[permissions]` 下的某个配置方案，或 `:workspace` 等内置配置方案。为确保行为可预测，请明确设置该项；只有在明确允许 `:workspace` 和 `:read-only` 时，托管要求才可以省略该项。在这种设置下，除非托管的 `allowed_permission_profiles` 指示 Codex 使用权限配置方案，否则 Codex 会使用旧版沙盒设置。 |
| `[permissions.<name>]`                                            | 表                      | 无                    | 定义一个命名配置方案。`default_permissions` 选择一个配置方案作为默认方案；其他权限配置方案设置也使用该配置方案名称。                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | 字符串                     | 无                    | 为配置方案提供便于理解的说明。配置方案不会通过 `extends` 继承其父配置方案的说明。                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | 字符串形式的配置方案名称        | 无                    | 以另一个命名配置方案，或内置的 `:read-only` 或 `:workspace` 配置方案为基础创建此配置方案。Codex 会拒绝 `:danger-full-access`、未知的父配置方案和继承循环。                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | 表                      | 无                    | 添加由配置方案定义的工作空间根目录，使这些根目录与当前会话的运行时工作空间根目录一同适用 `:workspace_roots` 文件系统规则。                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | 布尔值                    | `false`                 | 当值为 `true` 时，将该路径添加到配置方案的工作空间根目录集合。设为 `false` 的条目不会生效。                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | 表                      | 无                    | 将文件系统路径映射到访问权限值或限定范围的子路径映射。文件系统表缺失或为空时，文件系统访问仍会受到限制，并在启动时发出警告。                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | 数字                     | 无                    | 当 Codex 在沙盒启动前对匹配项创建快照时，此设置会限制 Linux、WSL 和原生 Windows 上拒绝读取 glob 模式的展开范围。值越大，启动扫描工作量可能越大。当需要对无界 `**` 模式进行有界预展开时，请将该值设为至少 `1`。                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`、`write` 或 `deny` | 无                    | 授予对受支持路径的直接访问权限。`deny` 会拒绝访问，其优先级高于匹配范围同样具体的 `write` 或 `read` 条目。Codex 会拒绝当前运行时无法强制执行的直接写入规则。                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`、`write` 或 `deny` | 无                    | 授予对 `<path>` 下级路径的访问权限。使用 `.` 表示基础路径。其他子路径必须是该基础路径下的相对路径，且不能包含 `.` 或 `..` 路径段。                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | 表                      | 无                    | 配置命令的网络访问权限，以及运行中的网络代理所执行的策略。除非由管理员管理的网络要求会启动代理，否则请启用 `features.network_proxy`。                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | 布尔值                    | `false`                 | 为该配置方案中的命令启用网络访问。这不会启动网络代理；如果没有运行中的代理，命令可以直接连接网络，不受域名限制。                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | 表                      | 无                    | 将主机匹配模式映射为 `allow` 或 `deny`。这些规则仅在网络代理运行时生效。如果没有 `allow` 条目，运行中的代理会阻止域名请求；拒绝条目优先于允许条目。                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` 或 `deny`          | 无                    | 支持精确主机名、用于匹配子域名的 `*.example.com`、用于匹配根域名及其子域名的 `**.example.com`，以及仅可用于允许规则的全局通配符 `*`。主机匹配模式会通过去除首尾空白、转换为小写、移除末尾的点号，以及移除简单端口或方括号进行规范化。                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | 表                      | 无                    | 映射 Unix 套接字允许名单的覆盖项。仅用于 Docker 等本地集成。                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` 或 `deny`          | 无                    | 使用 `allow` 将 Unix 套接字的绝对路径加入生效的允许名单，或使用 `deny` 拒绝该路径。被拒绝的条目不会出现在生效的允许名单中。                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | URL 字符串                 | `http://127.0.0.1:3128` | 供 `HTTP_PROXY`、`HTTPS_PROXY`、WebSocket 代理变量和相关工具代理环境变量使用的 HTTP 代理监听器。                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | 布尔值                    | `true`                  | 启用供 `ALL_PROXY` 和 FTP 代理变量使用的 SOCKS5 监听器。                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | URL 字符串                 | `http://127.0.0.1:8081` | SOCKS5 监听器地址。                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | 布尔值                    | `true`                  | 在已启用 SOCKS5 监听器时启用 SOCKS5 UDP 支持。                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | 布尔值                    | `true`                  | 允许网络沙盒代理针对出站请求遵循上游 `HTTP(S)_PROXY` 和 `ALL_PROXY` 设置。                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | 布尔值                    | `false`                 | 设置为 `true` 时，禁用本地和私有网络防护。设置为 `false` 时，必须将 `localhost` 或 `127.0.0.1` 等精确的本地字面值明确加入允许名单，而解析到本地或私有 IP 地址的主机名仍会被阻止。                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | 布尔值                    | `false`                 | 允许代理监听器绑定非环回地址。常规本地开发时请勿设置此项。                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | 布尔值                    | `false`                 | 在支持 Unix 套接字代理的环境中，绕过 Unix 套接字允许名单。这是一种范围很广的本地绕过机制。                                                                                                                                                                                                                                                                                                               |

## 文件系统权限

文件系统条目使用 `read`、`write` 或 `deny`：

| 访问权限  | 含义                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | 允许命令读取该路径下的文件并列出目录。命令不能在其中创建、修改、重命名或删除文件。 |
| `write` | 允许命令读取和修改该路径下的文件；在操作系统允许时，还可创建、重命名和删除文件。  |
| `deny`  | 禁止读取和写入该路径下的内容。使用此值，可从范围更大的 `read` 或 `write` 授权中排除一个禁止访问的子路径。         |

更具体的条目会覆盖范围更广的条目。当两个条目针对
同一路径时，`deny` 的优先级高于 `write`，而 `write` 的优先级
高于 `read`。

这种优先级规则允许配置方案先指定范围较广的工作区域，再从中排除
需要保持不可读的文件或目录：

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

在此示例中，工作空间根目录仍可写入，`.devcontainer/` 仍
可读取但不可写入，而沙盒内运行的命令仍
无法访问匹配的环境文件。

更具体的路径还可以在范围较广的拒绝规则内重新开放范围较窄的子树：

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

支持的路径形式：

| 路径               | 含义                                                                                     | 限定范围的子路径 |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | 文件系统根目录                                                                         | 仅 `.`        |
| `:minimal`         | 常用工具所需的平台和运行时路径                                           | 仅 `.`        |
| `:workspace_roots` | 当前会话的工作空间根目录，以及配置方案定义且已启用的所有工作空间根目录      | 是             |
| `:tmpdir`          | 可用时，`$TMPDIR` 指定的位置                                               | 仅 `.`        |
| `:slash_tmp`       | `/tmp` 文件夹（如果存在）                                                             | 仅 `.`        |
| `/absolute/path`   | 平台绝对路径，例如 macOS/Linux/WSL 上的 `/path`，或原生 Windows 上的 `C:\path` | 是             |
| `~/path`           | 当前用户主目录下的路径                                              | 是             |

在原生 Windows 上，相对于主目录的路径也可以使用反斜杠，例如
`~\work`。

仅当配置方案明确需要广泛的读取权限时，才使用 `:root`：

```toml
[permissions.audit.filesystem]
":root" = "read"

使用 `:workspace_roots` 下的嵌套条目，将访问范围限定为
相对于工作空间根目录的子路径：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

嵌套子路径必须位于其工作空间根目录内。系统会拒绝
`../other-repo` 等父目录遍历。

### 使用精确路径或 glob 模式拒绝读取

对于 Codex 不应读取的文件或子树，请使用 `deny`，即使范围更广的
配置方案规则允许访问附近路径也不例外。精确路径适合位置固定的目标，
例如 `~/.ssh`。如果配置方案需要涵盖一组
在各个代码仓库中具体位置不同的敏感文件，glob 模式更为合适。

当 glob 模式位于 `:workspace_roots` 下时，Codex 会以每个
有效工作空间根目录为基准解析该模式。例如：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

此规则禁止读取匹配的 `.env` 文件，无论其位于运行时工作空间根目录还是
配置方案定义的工作空间根目录下。当您希望保留正常的
工作空间写入权限，同时禁止读取环境文件、生成的机密信息或类似的
凭据文件时，请使用此规则。

`deny` glob 模式可用作拒绝读取规则。`read` 或 `write` glob 模式
在 Linux、WSL 和原生 Windows 沙盒中的可移植性较差，因此应尽可能优先使用
精确路径或 `"docs/**" = "read"` 等子树规则。

在 Linux、WSL 和原生 Windows 上，无界的 `**` 拒绝读取模式可能需要
在沙盒启动前进行有界预展开。使用无界模式时，请设置 `glob_scan_max_depth`，
例如 `"**/*.env" = "deny"`：

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` 必须至少为 `1`。值越大，沙盒启动前的
扫描深度越大，可能增加 Linux、WSL 和原生 Windows 上的启动开销。
如果您不想使用有界展开，可以列举明确的深度，例如
`*.env`、`*/*.env` 和 `*/*/*.env`。

如果同一组规则需要应用于当前会话根目录以外的其他目录，
请向配置方案添加可复用的工作空间根目录：

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

此配置方案生效时，Codex 会将 `:workspace_roots` 规则应用于
当前会话的运行时工作空间根目录，以及每个已启用且由配置方案定义的
工作空间根目录。

在原生 Windows 上，支持将 `D:\work` 等盘符路径和
`\\server\share` 等 UNC 路径用作绝对路径。

## 网络权限

网络访问和网络过滤是相互独立的设置。设置
`permissions.<name>.network.enabled = true`，允许命令访问网络，
并启用 `features.network_proxy` 以强制实施配置方案的域名规则：

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

实际行为取决于这两项设置：

- 网络关闭：无论代理功能是否启用，
命令都无法访问网络。
- 网络开启、代理关闭：命令可以直接、不受限制地访问网络。
权限配置方案中的域名规则不会得到强制实施。
- 网络开启、代理开启：命令通过代理访问网络，
代理会强制实施配置方案中的域名规则。如果启用的代理没有允许访问的域名，
则会阻止访问外部目标。

添加 `[permissions.<name>.network.domains]` 或设置
`permissions.<name>.network.enabled = true`，不会启用
`features.network_proxy`。管理员还可以通过
`[experimental_network]` 配置项在 `requirements.toml` 中启用代理。请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration#configure-network-access-requirements)。

网络沙盒代理启用后，默认绑定到本地监听地址：

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

除非需要与
特定运行时集成，否则请保留这些监听器的默认设置。`dangerously_*` 网络配置键是
专用环境中用于绕过限制的机制，不应在普通本地开发中使用。

### 本地网络和私有网络

网络代理启用后，Codex 默认启用本地网络和私有网络防护机制，
以防范 DNS 重绑定以及意外访问本地服务。
如果需要明确允许访问以字面量指定的本地目标，
请将确切的主机名或 IP 字面量加入允许列表：

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

仅当配置方案必须访问已列入允许列表的主机名，且这些主机名
解析为本地或私有地址时，才设置 `allow_local_binding = true`：

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Unix 套接字

Unix 套接字代理为 Docker 等工具提供绕过本地限制的途径，
请谨慎使用：

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

使用 `deny` 拒绝套接字路径，包括继承的允许条目。被拒绝的
套接字路径不会纳入有效允许列表。

启用 Unix 套接字时，请确保代理监听器始终绑定到环回地址。

## 从旧版沙盒设置迁移

权限配置方案可取代旧版的 `sandbox_mode` 和
`sandbox_workspace_write` 组合，让您通过一个可复用的配置方案同时描述
文件系统和网络行为。每个会话只能使用其中一种机制，不要
同时使用两种。

建议从以下配置开始：

- 对于只读工作流程，请使用内置的 `:read-only` 配置方案，或定义
  只在必要位置授予读取权限的自定义配置方案。
- 如需编辑工作空间，请使用内置的 `:workspace` 配置方案，或定义
  通过 `:workspace_roots` 写入的自定义配置方案，并仅添加工作流程所需的额外
  临时路径或缓存路径。
- 对于不受限制的本地执行，仅当您
  明确需要最宽松的本地访问模式时，才使用 `:danger-full-access`。

配置方案定义会话的本地默认权限状态。组织托管的
要求仍可施加其他限制，用户配置不得
放宽这些限制。请参阅 [托管配置](/zh-Hans/codex/enterprise/managed-configuration)，
了解管理员强制实施的文件系统和网络限制。

## 适用范围与强制实施

权限配置方案用于界定本地沙盒命令的执行边界。
请将其与审批策略配合使用，
并针对网页搜索、连接器、MCP 服务器、内置浏览器、计算机使用
和 Codex 云端分别采取独立的控制措施。

### 配置方案的控制范围

- **本地命令执行：** 权限配置方案用于控制在您计算机上运行的沙盒命令。
  连接器、MCP 服务器、浏览器或
  计算机使用界面、Codex 云端环境设置以及经审批的
  权限提升均采用各自的控制措施。
- **文件系统写入：** 允许写入的配置方案可以产生持久更改。
  请将对脚本、构建步骤、软件包管理器钩子、shell 启动
  文件和共享目录的写入视为敏感操作，因为后续工具或用户可以
  在原始沙盒上下文之外执行这些文件。
- **出站目标：** 只有在网络代理启用时，网络域名规则才会限制沙盒
  命令流量可访问的目标。这些规则不会
  判断允许访问的目标是否可信，通配符允许规则的覆盖范围仍然
  很广。
- **本地服务：** 启用的网络代理默认会阻止访问本地和私有网络
  目标。将 `localhost`、私有 IP 地址或 Unix 套接字加入允许列表，或者设置
`allow_local_binding = true`，都会明确开放对本地服务的访问。

### 网络代理无法控制的范围

网络代理只过滤在沙盒内运行的本地命令产生的流量，
不会将配置方案的域名允许列表应用于以下功能：

- **网页搜索：** 托管搜索工具使用独立的访问设置。请使用
`web_search` 进行控制；对于托管客户端，还可使用 `allowed_web_search_modes`。
  `tools.web_search.allowed_domains` 过滤的是搜索结果，而不是命令的
  网络访问。
- **应用和连接器：** 由连接器提供支持的工具使用各自的服务端
  连接、工作空间权限以及应用或工具设置。
- **MCP 服务器：** 本地和远程 MCP 服务器使用各自的进程或
  传输机制。请通过 `mcp_servers` 配置和托管的服务器
  允许列表进行控制。
- **浏览器和计算机使用：** 浏览器导航和计算机使用操作
  采用各自的功能与审批控制措施。
- **Codex 服务流量：** 模型、身份验证及其他客户端服务
  请求采用客户端独立的 HTTP 和系统代理设置。
- **Codex 云端：** 这些任务使用各自环境的
[互联网访问设置](/zh-Hans/codex/cloud/internet-access)。

如需限制这些功能，请直接配置每项功能。
命令的网络允许列表并不是适用于 Codex 所有操作的全局网络策略。

### 强制实施机制

- 在 macOS 上，Codex 使用 Seatbelt 沙盒配置方案。
如果平台沙盒无法强制实施所选策略，Codex 会拒绝运行命令，
而不会在未使用沙盒的情况下静默执行该命令。
- 在 Linux 和 WSL 上，Codex 使用 [bubblewrap](https://github.com/containers/bubblewrap)
  和 [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)，
  并可使用 Landlock 作为兼容性回退路径。最严格的
  强制实施路径取决于用户命名空间和内核支持；受限的
  容器主机可能迫使系统采用兼容性路径，不受支持的拆分策略
  则会被拒绝。
- 在原生 Windows 上，[`elevated` 沙盒](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)
  的强制实施能力最强，因为它可以使用专用的低权限沙盒用户、
  文件系统权限边界和防火墙规则。`unelevated`
  沙盒是网络隔离能力较弱的回退方案，无法强制实施
  所有读写分离的例外规则，因此系统会拒绝不受支持的策略。如果您需要 Linux 沙盒模型，
  请使用 WSL。

### 操作指南

请选择在确保任务完成的前提下权限范围最小的配置方案，
尤其是在授予写入权限或出站网络访问权限时。
请确保审批策略、机密信息处理方式和允许规则与该访问级别一致。

## 常用配置方案

### 带网络允许列表的只读配置

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### 文件访问仅限工作空间

以下是一个权限配置方案示例：该方案允许 Codex 写入您的工作空间文件夹，同时禁止读取文件系统的其他部分（仅保留由 `:minimal` 确定的有限例外）。

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### 工作空间可写，不可访问网络

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### 工作空间可写，可访问公共网络

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

仅当您有意允许访问公共网络时，才使用全局 `"*"` 允许规则。
拒绝规则可以缩小宽泛的允许列表范围。
