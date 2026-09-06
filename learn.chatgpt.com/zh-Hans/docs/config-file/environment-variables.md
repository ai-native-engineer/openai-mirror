<!-- source: https://learn.chatgpt.com/zh-Hans/docs/config-file/environment-variables -->

Codex 使用 `config.toml` 保存持久设置。环境变量可用于
仅在 shell 范围内生效的覆盖设置、自动化机密信息、安装程序行为或诊断。

本页列出 Codex 直接读取的稳定公开环境变量。
不包括内部开发变量、测试变量，或
您通过
[`env_key`](/zh-Hans/codex/config-file/config-advanced#custom-model-providers) 自行指定的提供商专用密钥名称。

## 核心位置

| 变量            | 使用方                                    | 默认值      | 说明                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI、IDE 扩展、app-server、安装程序 | `~/.codex`   | 设置 Codex 状态数据的根目录，包括配置、身份验证、日志、会话、技能和独立软件包元数据。如果您设置此变量，该目录必须已经存在。 |
| `CODEX_SQLITE_HOME` | CLI 和 app-server 的状态数据                   | `CODEX_HOME` | 设置使用 SQLite 保存的状态数据的存储位置。`sqlite_home` 配置选项优先。相对路径基于当前工作目录解析。           |

有关 `CODEX_HOME` 下所存文件的详细信息，请参阅
[配置和状态位置](/zh-Hans/codex/config-file/config-advanced#config-and-state-locations)。

## 安装程序变量

这些变量适用于通过以下地址提供的独立安装脚本：
`https://chatgpt.com/codex/install.sh` 和
`https://chatgpt.com/codex/install.ps1`。

| 变量                | 默认值                                                                              | 说明                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | 将其设置为 `1`、`true` 或 `yes` 可跳过安装程序提示。这些提示会采用默认响应，因此请将此设置用于脚本化安装和更新，而不要用于首次运行设置。 |
| `CODEX_INSTALL_DIR`     | `~/.local/bin`（macOS/Linux）；`%LOCALAPPDATA%\Programs\OpenAI\Codex\bin`（Windows） | 更改用户可见的 `codex` 命令的安装位置。独立软件包缓存仍位于 `CODEX_HOME/packages/standalone` 下。                        |

如需无人值守安装，请在相应的 shell 中设置 `CODEX_NON_INTERACTIVE=1`，并使用该 shell 运行
已下载的安装程序：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## 身份验证和网络

| 变量                           | 使用方                                          | 说明                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec、审查、TypeScript SDK、远程 exec-server | 为非交互式 Codex 进程提供 API 密钥。运行由代码仓库控制的代码时，请以内联方式设置该变量，而不要在整个作业范围内设置。             |
| `CODEX_ACCESS_TOKEN`               | CLI、app-server、受信任的自动化              | 为受信任的自动化提供 ChatGPT 或 Codex 访问令牌。如需持久保存登录状态，请通过管道将令牌传递给 `codex login --with-access-token`。             |
| `OPENAI_FEDERATION_RULE_ID`        | 工作负载身份                                | 选择为工作负载配置的联合规则。                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | 工作负载身份                                | 指向包含当前 OIDC 令牌或 SPIFFE JWT-SVID 的文件的绝对路径。                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | 工作负载身份                                | 可选择提供受限的 JSON 标识符，用于客户端上报的审计归因。不会影响身份验证或授权。         |
| `CODEX_CA_CERTIFICATE`             | HTTPS、登录和 WebSocket 客户端              | 指向 PEM CA 证书包，适用于存在企业 TLS 拦截或私有根证书的环境。其优先级高于 `SSL_CERT_FILE`。 |
| `SSL_CERT_FILE`                    | HTTPS、登录和 WebSocket 客户端              | 未设置 `CODEX_CA_CERTIFICATE` 时使用的备用 PEM CA 证书包路径。                                                                               |

对于提供商 API 密钥，请将
[`env_key`](/zh-Hans/codex/config-file/config-advanced#custom-model-providers) 设置在模型提供商的
配置中。Codex 会读取该配置指定的变量，因此变量
名称本身并不是固定的 Codex 环境变量。

有关自动化机密信息的处理，请参阅
[使用 API 密钥进行身份验证](/zh-Hans/codex/non-interactive-mode#use-api-key-auth)。
有关访问令牌的设置，请参阅[访问令牌](/zh-Hans/codex/enterprise/access-tokens)。
有关工作负载身份的设置，请参阅
[工作负载身份联合](/zh-Hans/codex/enterprise/workload-identity)。

## 诊断

| 变量   | 使用方            | 说明                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI 和 app-server | 控制 Rust 日志过滤和详细程度。除非您设置更详细的值，否则 `codex exec` 默认输出 `error` 级别的消息。 |

`RUST_LOG` 接受 `error`、`warn`、`info`、`debug` 和
`trace` 等值。它还接受更有针对性的 Rust 日志过滤规则，例如
`codex_core=debug,codex_tui=debug`。

交互式 CLI 默认会将诊断信息记录在容量受限的本地存储中，但
纯文本 `codex-tui.log` 文件需要主动启用。请显式设置 `log_dir`，以获取
用于故障排除的纯文本日志：

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

在非交互模式下，`codex exec` 会直接输出消息，而不是将其写入
单独的 TUI 日志文件。
