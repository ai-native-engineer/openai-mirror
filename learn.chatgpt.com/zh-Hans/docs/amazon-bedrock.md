<!-- source: https://learn.chatgpt.com/zh-Hans/docs/amazon-bedrock -->

配置本地 ChatGPT Work 和 Codex 界面，以使用通过 Amazon Bedrock 提供的 OpenAI 模型。在此设置中，本地客户端使用 AWS 管理的身份验证和访问控制，将模型请求发送到 Bedrock。

## 工作原理

当您将本地 ChatGPT Work 或 Codex 界面的模型提供商配置为 Amazon Bedrock 时，请求不会经过由 OpenAI 托管的 Responses API。本地客户端将模型请求发送到 Amazon Bedrock，而 Bedrock 为受支持的 OpenAI 模型提供与 OpenAI 兼容的 Responses API 实现。

  身份验证采用 AWS 原生方式。用户使用 Bedrock API 密钥或 AWS
  IAM 凭证进行身份验证；对于此提供商，用户不会使用 ChatGPT 登录或 `OPENAI_API_KEY`
  进行身份验证。

## 开始之前

请确保您具备以下条件：

- 访问 Amazon Bedrock 中受支持的 OpenAI 模型的权限。
- 所选模型可用的 AWS 区域。
- 已为 AWS 账户配置 Amazon Bedrock Mantle 路径的身份验证。

## 配置提供商

将适用于 Amazon Bedrock Mantle 路径的 `amazon-bedrock` 模型提供商添加到
`~/.codex/config.toml`。ChatGPT 桌面应用、Codex CLI、IDE 扩展和
SDK 读取相同的本地配置层。模型为可选配置。
需要时，请明确选择受支持的模型。

```toml
model_provider = "amazon-bedrock"

  本指南介绍受支持的 AWS 商业区域中的 Amazon Bedrock Mantle 路径。本地 ChatGPT Work 和 Codex 界面不支持 AWS GovCloud 区域中的 Bedrock Mantle 端点。

## 身份验证选项

本地 ChatGPT Work 和 Codex 界面支持两种 Bedrock 身份验证方式，并按照以下顺序检查：

1. Bedrock API 密钥。
2. AWS SDK 凭证链。

### 选项 1：Bedrock API 密钥

在本地客户端读取的环境中设置 Bedrock API 密钥。使用 API 密钥进行身份验证时，必须指定区域。

```shell

### 选项 2：AWS SDK 凭证

如果您的组织通过 AWS SDK 凭证链管理 Bedrock 访问权限，请使用这种方式。本地客户端可使用以下标准 AWS SDK 凭证来源：

#### 共享 AWS 配置文件

配置共享的 AWS `config` 和 `credentials` 文件：

```shell
aws configure

#### 环境变量

设置标准 AWS SDK 凭证环境变量：

```shell

#### AWS 管理控制台凭证

使用 AWS 管理控制台凭证登录：

```shell
aws login

#### AWS SSO 或命名配置方案

使用 AWS SSO 登录并选择命名配置方案：

```shell
aws sso login --profile codex-bedrock

#### 联合身份

对于企业 SSO 或 OIDC 联合身份验证，请在本地客户端之外使用
`credential_process` 配置联合身份，并让 AWS SDK
解析凭证。将浏览器登录、Token 交换、缓存和刷新交由
AWS 配置方案中的 `credential_process` 辅助程序处理。

## 桌面应用和 IDE 扩展

桌面应用和 IDE 扩展可能无法继承 shell
中的环境变量。请将所需值写入 `~/.codex/.env`
后重启应用或扩展。

```shell

## 验证设置

- 在 Codex CLI 中，打开 `/status`，确认 Codex 正在使用
`amazon-bedrock` 模型提供商。
- 重启 ChatGPT 桌面应用后，选择 Work 或 Codex 并启动新任务。
- 重启 IDE 扩展后，开始新会话。
- 确认所选模型在已配置的 AWS 区域中可用，并且 AWS 身份有权访问该模型。

## 受支持的模型

请使用准确的模型 ID：

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

模型可用性因 AWS 区域而异。选择模型前，请参阅[各
AWS
区域的模型支持情况](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)。

## 功能可用性

此配置支持本地 ChatGPT Work 和 Codex 工作流。托管的网页版 ChatGPT Work、Codex 云端，以及依赖 OpenAI 托管的云服务、托管工具或云端管理的发现机制的功能，目前均不可用。

  使用 Amazon Bedrock 时无法使用快速模式。快速模式采用优先处理，而 Amazon Bedrock 初始提供的服务仅支持按需推理。

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> 此功能目前仅在特定区域可用。请查阅
    各项功能的文档，详细了解地域限制。
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> 无需 ChatGPT 身份验证的本地插件包和 OpenAI 精选插件
    （包括 Codex Security）均可使用。
    需要 ChatGPT 身份验证、连接器或云端托管共享功能的
    插件不可用。
  </div>

## 故障排除

如果设置失败，请检查以下各项：

- 模型 ID 与受支持的模型完全匹配。
- 您指定了该模型可用的 AWS 区域。
- Bedrock API 密钥或 AWS 凭证有效且未过期。
- AWS 身份有权访问所选 Bedrock 模型。
- `AWS_BEARER_TOKEN_BEDROCK` 未设置为已过期或非预期的密钥。
- 使用桌面应用或 IDE 扩展时，所需环境变量已包含在
  `~/.codex/.env` 中。

## 支持范围

OpenAI 支持团队可协助解决 ChatGPT Work 和 Codex 客户端的设置、
配置、本地 CLI 行为、桌面应用行为、IDE 扩展行为，
以及本地产品体验方面的问题。

如需处理 AWS 凭证、IAM 权限、Bedrock 模型访问权限、配额、账单、
区域可用性、Bedrock 请求失败、AWS 服务日志或 Bedrock
服务行为方面的问题，请联系客户的 AWS 管理员或 AWS 支持团队。
