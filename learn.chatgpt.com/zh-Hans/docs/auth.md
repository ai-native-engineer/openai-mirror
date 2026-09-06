<!-- source: https://learn.chatgpt.com/zh-Hans/docs/auth -->

## OpenAI 身份验证

<a id="sign-in-with-chatgpt"></a>

使用 OpenAI 模型时，Codex 支持两种登录方式：

- 使用 ChatGPT 登录以获得订阅访问权限
- 使用 API 密钥登录以获得按用量计费的访问权限

ChatGPT 桌面应用、Codex CLI 和 IDE 扩展在本地工作时均支持这两种登录方式。
使用 Codex 云端必须通过 ChatGPT 登录。

您的登录方式还决定适用哪些管理控制措施和数据处理政策。

- 使用 ChatGPT 登录时，Codex 的使用受您的 ChatGPT 工作空间权限、
基于角色的访问控制（RBAC），以及
ChatGPT Enterprise 的数据保留和数据驻留设置约束。
- 使用 API 密钥时，
则适用您所属 API 组织的数据保留和数据共享设置。

对于受管理的工作空间，身份验证只是访问控制的一个层面。工作空间的
成员资格和预配决定谁可以登录，而席位和
工作空间角色决定他们可以使用哪些产品界面和功能。
在 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中本地工作时，
权限配置方案会限制智能体在设备上可执行的操作。请参阅
[群组与预配](/zh-Hans/codex/enterprise/groups-and-provisioning)
和[角色与工作空间权限](/zh-Hans/codex/enterprise/roles-and-workspace-permissions)
，以规划相关控制措施。

### 使用 ChatGPT 登录

在 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中使用 ChatGPT 登录时，登录流程会打开浏览器窗口。登录后，浏览器会将您的凭据返回给 Codex。

### ChatGPT 网页版

打开 [ChatGPT](https://chatgpt.com)，登录并选择您要用于
工作的工作空间。ChatGPT 网页版会在浏览器中保持已通过身份验证的会话。

#### ChatGPT 桌面应用

在未登录界面上，选择 **继续登录**，然后完成
浏览器登录流程。

#### Codex CLI

运行 `codex login`，然后完成浏览器登录流程。这是没有有效会话时采用的默认
身份验证方式。

#### IDE 扩展

在未登录界面上，选择 **使用 ChatGPT 登录**，然后完成
浏览器登录流程。

<a id="sign-in-with-an-api-key"></a>

### 使用 API 密钥登录

您也可以使用 API 密钥登录 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展。请从 [OpenAI 控制面板](https://platform.openai.com/api-keys)获取 API 密钥。

#### ChatGPT 桌面应用

在未登录界面上，选择 **使用其他方式登录**，输入密钥，然后
选择 **继续**。

#### Codex CLI

通过 stdin 将密钥以管道方式传递给 `codex login`：

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### IDE 扩展

在未登录界面上，选择 **使用 API 密钥**，输入密钥，然后选择
**确定**。

OpenAI 会通过您的 OpenAI Platform 账户，按照标准 API 费率对 API 密钥用量计费。请参阅[API 定价页面](https://openai.com/api/pricing/)。

API 密钥身份验证支持本地 Codex 工作流，但部分依赖
ChatGPT 工作空间访问权限或云服务的功能会受限或无法使用。
如需比较不同方案的支持情况，请参阅
[功能可用性](/zh-Hans/codex/pricing#feature-availability)。

在 Codex CLI 和 ChatGPT 桌面应用的 Codex 中，使用 API 密钥进行身份验证
后，可以访问受支持的 OpenAI 精选插件。部分插件
无法使用，因为其连接流程需要目前不受支持的 OAuth
功能。请参阅[使用插件](/zh-Hans/codex/plugins#api-key-availability)。

使用 API 密钥登录时，Codex 按标准 API 定价计费，
而不会使用 ChatGPT 方案中包含的额度。

对于程序化的 Codex CLI 工作流，例如 CI/CD
作业，请使用 API 密钥进行身份验证。请勿在不受信任或公开的环境中暴露 Codex 执行功能。

### 检查身份验证状态或退出登录

打开个人资料菜单，确认当前使用的账户和工作空间。要结束该浏览器中的
ChatGPT 网页版会话，请选择 **退出登录**。

打开个人资料菜单，查看当前账户或 API 密钥状态。选择
**退出登录** 以清除当前凭据。

运行 `codex login status` 查看当前身份验证方式。对于已存储的
身份验证信息，请运行 `codex logout` 清除当前凭据。当
进程选择工作负载身份时，Codex 会拒绝 `codex login` 和
`codex logout`，因为身份验证由进程环境控制。

打开个人资料菜单，查看当前账户或 API 密钥状态。选择
**退出登录** 以清除当前凭据。

### 使用 Codex 访问令牌实现企业自动化

在 ChatGPT Enterprise 工作空间中，管理员可以授予访问令牌权限，
使获准成员能够为受信任、非交互式的 Codex 本地工作流创建 Codex 访问令牌。
当自动化流程需要访问 ChatGPT 工作空间、使用由 ChatGPT 管理的 Codex 权益，
或应用企业工作空间控制措施，
同时无需通过浏览器登录时，请使用访问令牌。

访问令牌适用于受信任的脚本、调度程序和私有 CI 运行器。
对于常规 OpenAI API 调用，请继续使用 Platform API 密钥。

有关设置步骤、权限、轮换和撤销的指导，请参阅
[访问令牌](/zh-Hans/codex/enterprise/access-tokens)。

如果您的云平台、CI 系统或集群已签发短期有效的
工作负载令牌，请使用
[工作负载身份联合](/zh-Hans/codex/enterprise/workload-identity)
，而不要存储 OpenAI 凭据。

如果您的环境已提供 Codex 访问令牌，请通过管道将其传递给 CLI：

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## 保护您的 Codex 云端账户

Codex 云端会直接与您的代码库交互，因此其安全要求高于许多其他 ChatGPT 功能。请启用多重身份验证（MFA）。

如果您使用社交登录提供商（Google、Microsoft、Apple），则无需在 ChatGPT 账户中启用 MFA，但可以通过社交登录提供商进行设置。

有关设置说明，请参阅：

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

如果您通过单点登录（SSO）访问 ChatGPT，您所在组织的 SSO 管理员应强制所有用户启用 MFA。

如果您使用电子邮件和密码登录，则必须先为账户设置 MFA，才能访问 Codex 云端。

如果您的账户支持多种登录方式，且其中一种是电子邮件和密码，那么即使使用其他方式登录，也必须先设置 MFA，才能访问 Codex。

<a id="login-caching"></a>

## 登录信息缓存

使用 ChatGPT 或 API 密钥登录 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展时，您的登录信息会被缓存并重复使用。CLI 和扩展共享同一份缓存的登录信息。如果您从任一端退出登录，下次启动 CLI 或扩展时都需要重新登录。

Codex 会将登录信息缓存在本地明文文件 `~/.codex/auth.json` 中，或缓存在操作系统专用的凭据存储区中。

对于使用 ChatGPT 登录的会话，Codex 会在使用期间自动刷新即将过期的 Token，因此活跃会话通常可以持续，无需再次通过浏览器登录。

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## 凭据存储

使用 `cli_auth_credentials_store` 控制 Codex CLI 存储缓存凭据的位置：

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` 会将凭据存储在 `auth.json` 文件中；该文件位于 `CODEX_HOME` 目录下（默认为 `~/.codex`）。
- `keyring` 会将凭据存储在操作系统的凭据存储区中。
- `auto` 会在操作系统凭据存储区可用时使用该存储区，否则回退到 `auth.json`。

请参阅[配置参考资料](/zh-Hans/codex/config-file/config-reference)，了解完整的
`config.toml` 模式。

  如果使用基于文件的存储，请像保护密码一样保护 `~/.codex/auth.json`，因为它
  包含访问令牌。请勿提交该文件、将其粘贴到工单中或在
  聊天中分享。

## 强制指定登录方式或工作空间

在托管环境中，管理员可以限制用户可采用的身份验证方式：

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

如果当前凭据不符合配置的限制，Codex 会先让用户退出登录，然后退出程序。

这些设置通常通过托管配置应用，而不是由每位用户单独设置。请参阅[托管配置](/zh-Hans/codex/enterprise/managed-configuration)。

## 登录诊断

直接运行 `codex login` 时，会在您配置的日志目录下写入专用的 `codex-login.log` 文件。
需要排查浏览器登录或
设备代码登录故障，或者支持团队要求提供登录专用日志时，请使用该文件。

## 自定义 CA 证书包

如果您的网络使用企业 TLS 代理或私有根 CA，请在登录前将
`CODEX_CA_CERTIFICATE` 设置为 PEM 证书包。未设置
`CODEX_CA_CERTIFICATE` 时，Codex 会回退使用 `SSL_CERT_FILE`。这些自定义 CA 设置同样适用于
登录、常规 HTTPS 请求和
安全 WebSocket 连接。

```shell

codex login

## 在无头设备上登录

使用 Codex CLI 登录 ChatGPT 时，以下情况可能导致基于浏览器的登录界面无法正常使用：

- 您正在远程或无头环境中运行 CLI。
- 您的本地网络配置阻止了 Codex 在您登录后用于将 OAuth Token 返回给 CLI 的 localhost 回调。

在这些情况下，请优先使用设备代码身份验证（测试版）。在交互式登录界面中，选择 **使用设备代码登录**，或直接运行 `codex login --device-auth`。如果设备代码身份验证不适用于您的环境，请使用一种备用方法。

### 首选：设备代码身份验证（测试版）

1. 请在 ChatGPT 安全设置（个人账户）或 ChatGPT 工作空间权限（工作空间管理员）中启用设备代码登录。
2. 在运行 Codex 的终端中，选择以下任一选项：
   - 在交互式登录界面中，选择 **使用设备代码登录**。
   - 运行 `codex login --device-auth`。
3. 在浏览器中打开链接并登录，然后输入一次性代码。

如果您的环境中无法使用设备代码登录，请使用以下
备用方法之一。

### 备用方案：在本地完成身份验证并复制登录缓存

如果您可以在配有浏览器的计算机上完成登录流程，就可以将缓存的凭据复制到无头计算机。

1. 在可以通过浏览器完成登录流程的计算机上，运行 `codex login`。
2. 确认登录缓存文件 `~/.codex/auth.json` 已存在。
3. 将 `~/.codex/auth.json` 复制到无头计算机上的 `~/.codex/auth.json`。

请像保护密码一样保护 `~/.codex/auth.json`：它包含访问令牌。请勿提交该文件、将其粘贴到工单中或在聊天中分享。

如果您的操作系统将凭据存储在凭据存储区中，而不是 `~/.codex/auth.json` 中，此方法可能不适用。有关如何配置基于文件的存储，请参阅
[凭据存储](/zh-Hans/codex/auth#credential-storage)。

通过 SSH 复制到远程计算机：

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

或者使用无需 `scp` 的单行命令：

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

复制到 Docker 容器中：

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

如需了解如何在受信任的 CI/CD 运行器上采用这一模式的进阶做法，请参阅
[在 CI/CD 中维护 Codex 账户身份验证（进阶）](/codex/auth/ci-cd-auth)。
该指南介绍了如何让 Codex 在正常运行期间刷新 `auth.json`，并
保留更新后的文件供下一个作业使用。API 密钥仍是自动化场景中推荐的
默认选择。

### 备用方案：通过 SSH 转发 localhost 回调

如果可以在本地计算机与远程主机之间转发端口，您可以通过隧道转发 Codex 的本地回调服务器（默认为 `localhost:1455`），使用基于浏览器的标准登录流程。

1. 在本地计算机上启动端口转发：

```shell
ssh -L 1455:localhost:1455 user@remote

2. 在该 SSH 会话中运行 `codex login`，然后在本地计算机上访问输出的地址。

## 其他模型提供商

在配置文件中定义[自定义模型提供商](/zh-Hans/codex/config-file/config-advanced#custom-model-providers)时，您可以选择以下任一身份验证方式：

- **OpenAI 身份验证**：设置 `requires_openai_auth = true` 以使用 OpenAI 身份验证。然后，您可以使用 ChatGPT 或 API 密钥登录。这种方式适用于通过 LLM 代理服务器访问 OpenAI 模型。当 `requires_openai_auth = true` 时，Codex 会忽略 `env_key`。
- **环境变量身份验证**：设置 `env_key = "<ENV_VARIABLE_NAME>"`，以使用名为 `<ENV_VARIABLE_NAME>` 的本地环境变量中的提供商专用 API 密钥。
- **无身份验证**：如果未设置 `requires_openai_auth`（或将其设置为 `false`），并且也未设置 `env_key`，Codex 会认为该提供商不需要身份验证。这种方式适用于本地模型。
