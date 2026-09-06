<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/workload-identity -->

工作负载身份联合可让受信任的自动化流程使用 Codex，而无需存储个人访问 Token 或其他长期有效的 OpenAI 凭据。您的工作负载会提供由您现有的身份提供方签发的短期身份 Token。OpenAI 会验证该 Token，并为您受管理的 ChatGPT 工作空间中的用户或服务账户返回一个短期访问 Token。

对于云平台、
Kubernetes、CI 系统以及其他能够签发 OIDC Token 或
SPIFFE JWT-SVID 的环境中运行的无人值守 Codex 进程，请使用工作负载身份。如需了解共享信任模型和独立的 OpenAI API 流程，
请参阅[工作负载身份概览](/api/docs/guides/workload-identity-federation)。

  Codex 工作负载身份联合目前处于测试阶段，且必须在您的
  工作空间中启用。如需申请使用权限，请联系您的 OpenAI 代表或[OpenAI
  支持团队](https://help.openai.com/en/articles/6614161-how-can-i-contact-support)。

## 开始前的准备

您需要：

- 在 OpenAI 管理门户中管理工作负载身份的权限。
- 一个受管理的 ChatGPT 工作空间。
- 一个已加入该工作空间且成员状态有效的 ChatGPT 用户或服务账户，或者在设置期间创建此类用户或账户的权限。
- 一个 OIDC Token 或 SPIFFE JWT-SVID，并且您清楚其签发方、受众及用于标识身份的声明。
- 能够在绝对路径下的受保护文件中持续更新该 Token 的运行时。
- Codex 0.148.0 或更高版本。
- 已生效的 Codex 身份验证策略，允许采用 ChatGPT 身份验证
  并使用联合规则选定的工作空间。请参阅[强制使用登录
  方式或工作空间](/zh-Hans/codex/auth#enforce-a-login-method-or-workspace)。

OpenAI 不会在 Token 交换过程中创建主体或建立工作空间成员关系。管理员需要在工作负载连接前选择或创建主体。创建由真人使用的用户账户会占用一个工作空间席位，并须遵循该工作空间的成员资格规则。

在原生 Windows 环境中，请使用 **提升权限**的
[Windows 沙盒](/zh-Hans/codex/windows/windows-sandbox)。其他 Windows 沙盒模式
无法阻止模型控制的命令访问身份 Token 文件。

## 获取身份 Token

您的工作负载运行时负责获取并刷新上游身份 Token。Codex 不会代您调用云平台元数据服务或身份提供方客户端库。

| 运行时                          | 推荐的 Token 文件来源                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes、AKS、EKS 或 GKE     | 挂载投射的服务账户 Token，并将 Codex 指向该文件。平台负责轮换该 Token。                                  |
| Microsoft Entra 托管标识 | 运行受信任的主机进程或边车进程，向 Azure IMDS 请求 Token，并在 Token 过期前替换该文件。                |
| AWS 出站身份联合 | 运行受信任的主机进程，调用区域 STS 的 `GetWebIdentityToken`，并在 Token 过期前替换该文件。                   |
| Google Cloud                     | 运行受信任的主机进程，向元数据服务器请求身份 Token，并在 Token 过期前替换该文件。        |
| Oracle Cloud Infrastructure      | 运行受信任的主机进程，使用实例主体请求 IDCS 访问 Token，并在 Token 过期前替换该文件。 |
| GitHub Actions                   | 请求作业的 OIDC Token，将其写入受保护的文件，并在后续交换前请求新的 Token。                    |
| SPIFFE                           | 使用 SPIFFE Workload API 或经批准的辅助程序，将当前有效的 JWT-SVID 写入该文件。                                      |
| 自定义 OIDC 提供方             | 通过签发方的工作负载流程获取 JWT，然后在 JWT 过期前刷新受保护的文件。                            |

请按照相应提供方的指南配置 Token 签发，并检查示例 Token：

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

在本地解码示例 Token，并记录其 `iss`、`aud`、`sub` 及您计划信任的其他
声明。解码不会验证签名。切勿将
生产环境 Token 粘贴到网站上或写入日志。

## 连接工作负载

启动 Codex 前，管理员需要创建提供方和联合规则。

1. 在 OpenAI 管理门户中打开[工作负载身份](https://admin.openai.com/workload-identity)，
   然后选择 **连接工作负载**。
2. 重用已为 Codex 配置的提供方，或创建新的提供方。提供方预设会预填 GitHub Actions、Microsoft Entra ID、Google Cloud、AWS、Kubernetes、SPIFFE 及自定义 OIDC 提供方的常用设置。
3. 选择 **Codex** 和允许该工作负载使用的受管理工作空间。
4. 添加能够识别工作负载且范围尽可能小的条件。可匹配主体、精确声明、CEL 条件或这些条件的组合。添加可接受的受众，以限制规则接受的 Token。所有已配置的匹配器都必须通过。
5. 将规则映射到一名现有的 ChatGPT 用户或一个现有的服务账户，或者在设置期间创建相应账户。
6. 审查提供方、条件、工作空间、主体、作用域及访问
   Token 的有效期。依次选择 **连接工作负载**和 **下载配置**。

下载的文件包含一个非机密的联合规则 ID，以及 Codex 读取身份 Token 的路径。该文件不包含凭据。

如需自动完成设置，请使用[工作负载身份 Admin
API](/api/docs/guides/workload-identity-federation/admin-api)。有关匹配器的
行为和示例，请参阅[联合规则
参考资料](/api/docs/guides/workload-identity-federation/federation-rules)。

## 配置 Codex 进程

启动 Codex 的进程需要以下两个工作负载身份变量：

```bash

`OPENAI_FEDERATION_RULE_ID` 不属于机密，但 Token 文件属于机密。请使用绝对
路径，并将 Token 文件置于专用目录中，例如 `/var/run/secrets/openai.com`；该目录应归
工作负载账户所有，且权限模式应设为 `0700`。只有受信任的主机进程才应写入
该目录。请勿将该目录置于代码仓库或其他
Codex 工具可访问的路径中。避免凭据出现在日志、Shell 历史记录和构建产物中。

### 添加审计归因

当多个运行时实例共享一条联合规则时，您可以在 Token 签发审计事件中识别每个实例。
请将可选的
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` 变量设置为编码为字符串的
JSON 对象：

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

该对象必须包含 `instance_id`，还可以包含 `display_name` 和最多
8 个标签。编码后的对象最大为 1,024 字节。`instance_id` 和
`display_name` 最多为 128 个字符。标签键最多为 64
个字符，标签值最多为 256 个字符。

标识符必须以 ASCII 字母或数字开头。后续字符可以包含
字母、数字、`.`、`_`、`:`、`/`、`@` 和 `-`。标签键支持字母、
数字、`.`、`_` 和 `-`。

OpenAI 将此上下文视为客户端上报的审计归因，而非经验证的工作负载身份。它不会影响身份验证、授权、规则匹配、作用域、速率限制、撤销、功能门控或指标。请勿在其中放置凭据、机密信息、个人数据、提示、模型输出或其他客户内容。

对于有效的上下文，OpenAI 会派生一个稳定的归因 ID，其作用域限定为租户、
提供商、联合规则和 `instance_id`。出于归因目的，访问令牌
包含该 ID，但不包含上下文。令牌签发成功的审计事件
包含该 ID 和规范化后的上下文。如果上下文超出限制或
违反此模式，交换将失败并返回 `invalid_grant`。

Codex 会在进程启动时读取上下文，并且不会将上下文、规则 ID 或令牌文件路径传递给由模型控制的 Shell、钩子或 MCP 服务器。更改上下文后，请重启 Codex。

### 保护和轮换令牌文件

对于托管的 Linux、macOS 和 WSL 部署，请将整个令牌目录添加到
[`permissions.filesystem.deny_read`](/zh-Hans/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
这一托管要求中：

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

这样可以阻止由模型控制的命令读取当前有效的令牌或临时替换令牌，同时 Codex 主机进程仍可使用该令牌进行交换。对于投射令牌卷，请禁止读取整个令牌挂载点，以及位于挂载点外部的所有底层路径或解析后的目标路径。仅依靠文件权限和清理环境变量，无法阻止以同一用户身份运行的其他进程访问凭证。在原生 Windows 上，请使用上述提升权限的沙盒。

对于不投射文件的令牌来源，请让受信任的主机进程将每个替换文件写入受保护的目录，再将其重命名到目标位置。原子重命名可以防止 Codex 读取不完整的令牌。例如，您可以根据提供商的令牌命令调整此由主机管理的刷新脚本。运行脚本前，请预先准备好该目录：

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

请在 Codex 能够控制的任何 Shell 或工具之外运行刷新进程。
在刷新和清理期间，请始终保持拒绝读取设置生效。即使强制停止
导致临时文件残留，该文件也必须保留在禁止读取的
目录中。请勿将工作负载身份设置写入 `config.toml`。

## 验证连接

加载已下载的环境配置，并检查所选的身份验证方式：

```bash
. ./workload-identity-idpm_example.env
codex login status

在 PowerShell 中：

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

检查成功时会输出 `Logged in using workload identity`。这表明
Codex 已通过配置的联合规则完成令牌交换。该命令
不会输出解析得到的工作空间、安全主体或规则。启动工作负载之前，
请在管理门户中确认这些值。如果 Codex 显示其他
身份验证方式，说明两个必需的 WIF 变量未传递给该进程。

如果提供商使用 **防止断言重放** 功能，且断言包含 `jti`
声明，此检查会消耗该 `jti`。请在启动另一个 Codex 进程前，写入包含新
`jti` 的新签发断言。

在同一环境中发起一个简单请求：

```bash
codex exec "Reply with only: workload identity is working"

Codex 会交换上游令牌，并将 OpenAI 访问令牌保存在内存中。
它不会将任何一种凭证写入 `auth.json`、系统密钥环或
`config.toml`。

## 保持令牌有效

请在上游令牌过期前刷新身份令牌文件。Codex 需要新的 OpenAI 访问令牌时，会重新读取该文件。OpenAI 令牌将在上游令牌到期或联合规则设定的有效期届满时失效，以较早者为准，并且其有效期绝不超过一小时。

管理员启用重放保护后，每个上游 JWT 都必须具有
唯一的 `jti`。请在每次交换前写入包含新 `jti` 的新签发断言，
包括长时间运行的进程中的刷新操作。不含
`jti` 的断言不受重放保护。

Codex 在每个主机进程内共享一个内存中的交换会话。该进程内的并发请求会复用有效的 OpenAI 访问令牌，并在其过期时共享一次刷新。不同进程会分别进行交换，因此需要使用提供商允许其使用的断言。

## 凭证优先级

两个必需的工作负载身份变量优先于所有其他凭证来源：

1. 只要 `OPENAI_FEDERATION_RULE_ID` 或
`OPENAI_IDENTITY_TOKEN_FILE` 其中之一存在，Codex 就会选择工作负载身份。
2. 如果只设置了一个必需变量，Codex 会返回错误。它不会回退到 API 密钥、访问令牌或已保存的登录状态。
3. 只设置 `OPENAI_WORKLOAD_IDENTITY_CONTEXT` 时，不会选择工作负载身份。
4. 如果两个必需的 WIF 变量均不存在，Codex 会应用相应使用方式的常规
   凭证规则。对于允许使用 API 密钥进行
   身份验证的使用方式，`CODEX_API_KEY` 在 `codex exec`、
`codex review`、TypeScript SDK 和 `codex exec-server --remote` 中优先生效。其他
   使用方式可以采用 `CODEX_ACCESS_TOKEN` 或已保存的登录状态。

SDK 的 `apiKey` 选项会转换为 `CODEX_API_KEY`；只要存在任一必需的 WIF 变量，
WIF 仍具有优先级。使用 WIF 时，请省略此选项，
避免工作负载携带未使用的长期凭证。

如需不停机迁移现有工作负载，请在其当前凭证仍可用时配置 WIF。启动一个同时设置了两个必需 WIF 变量的新进程；即使旧凭证仍然存在，WIF 也会优先生效。工作负载使用 WIF 成功运行后，请从其运行时及密钥存储中移除旧凭证，然后撤销该凭证。在撤销之前，您可以移除两个必需的 WIF 变量并启动新进程，以完成回滚。

## 支持的 Codex 使用方式

请在运行 Codex 进程的计算机上配置工作负载身份。

| 使用方式                                         | 支持情况和主机边界                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 交互式 `codex`、`resume` 和 `fork`       | 支持。请在已配置的环境中启动 CLI。                                                 |
| `codex exec`、`exec resume` 和 `codex review` | 支持。任一必需的 WIF 变量都会使 WIF 优先生效。                                      |
| TypeScript SDK                                  | 支持。父进程提供必需的 WIF 变量以及可选的归因上下文。 |
| `codex app-server`                              | 支持。请在 app-server 主机上配置 WIF，而不是在远程客户端上配置。                                |
| `codex exec-server --remote`                    | 支持对远程环境注册表进行身份验证。请在 exec-server 主机上配置 WIF。 |
| 本地 exec-server 进程操作            | 不使用 WIF 身份验证。这些操作通过本地 exec-server 协议运行。                         |
| `codex mcp-server`                              | 不支持。                                                                                          |

远程 app-server 和 exec-server 客户端绝不会通过其协议发送上游身份令牌。

## 更改或移除访问权限

对规则的主体、受众、声明、CEL 条件、作用域或令牌有效期所作的更改，适用于新的交换。在更改之前签发的令牌可能会一直有效，直至其有效期结束。

禁用提供商或规则可立即终止访问。禁用后，新的交换会被阻止，并且通过该资源签发的现有 OpenAI 访问令牌会被撤销。归档对访问具有相同的影响，且归档操作无法撤销。更改提供商的信任设置时，也会在新的信任设置生效前撤销已签发的令牌。

## 审计变更

创建、更新或归档提供商及联合规则时，都会生成审计
事件。请参阅[合规 API 和审计事件
指南](/zh-Hans/codex/enterprise/compliance-api)，导出您的工作空间
支持的事件。将这些事件与身份提供商的签发日志关联，并且不要在
任一系统中记录上游断言或 OpenAI 访问令牌。

当进程提供 `OPENAI_WORKLOAD_IDENTITY_CONTEXT` 时，成功的
令牌签发审计事件还会包含上文所述的稳定归因 ID 和
规范化后的上下文。

## 故障排查

| 问题现象                                                               | 检查项                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex 提示工作负载身份配置不完整              | 在同一进程中设置两个必需变量，并使用令牌文件的绝对路径。                               |
| Codex 提示其登录策略不允许使用工作负载身份 | 在生效的策略中允许 ChatGPT 身份验证，并将该规则对应的工作空间纳入其允许的工作空间范围。 |
| Codex 显示其他凭证                                      | 将两个必需的 WIF 变量加载到 Codex 进程中，然后启动新进程并重新运行 `codex login status`。  |
| OpenAI 拒绝工作负载上下文                                       | 检查其 JSON 结构、大小、允许的字符以及字段限制。移除敏感内容或客户内容。            |
| OpenAI 拒绝该令牌                                              | 将 `iss`、`aud`、到期时间、签名密钥和断言有效期与提供商配置进行核对。               |
| 规则不匹配                                               | 确认客户端使用预期的规则 ID，并且所有主体、受众、精确声明和 CEL 检查均已通过。  |
| OpenAI 拒绝该安全主体                                          | 确认用户或服务账户处于活跃状态，且是所选工作空间的活跃成员。                   |
| OpenAI 拒绝重复使用的断言                                   | 获取包含新 `jti` 的新 JWT；请勿使用同一受重放保护的断言重试。                                  |
| 长时间运行的进程停止刷新                               | 确认主机上的刷新进程仍会在 Token 过期前替换 Token 文件。                                  |

有关提供方验证、限制和 CEL 的详细信息，请参阅[联合规则
参考资料](/api/docs/guides/workload-identity-federation/federation-rules)。
