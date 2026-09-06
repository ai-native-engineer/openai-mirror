<!-- source: https://learn.chatgpt.com/zh-Hans/docs/third-party/linear -->

在 Linear 中使用 Codex，通过议题委派工作。将议题分配给 Codex，或在评论中提及 `@Codex`，Codex 便会创建云端聊天，并回复进度和结果。

付费套餐支持在 Linear 中使用 Codex（请参阅[定价](/zh-Hans/codex/pricing)）。

如果您使用企业套餐，请让您的 ChatGPT 工作空间管理员在[工作空间设置](https://chatgpt.com/admin/settings)中开启 Codex 云端聊天，并在[连接器设置](https://chatgpt.com/admin/ca)中启用 **Codex for Linear** 。

## 设置 Linear 集成

1. 要设置 [Codex 云端聊天](/zh-Hans/codex/cloud)，请在 [Codex](https://chatgpt.com/codex) 中连接 GitHub，并为您希望 Codex 使用的代码仓库创建[环境](/zh-Hans/codex/environments/cloud-environment)。
2. 前往 [Codex 设置](https://chatgpt.com/codex/settings/connectors)，为您的工作空间安装 **Codex for Linear** 。
3. 在 Linear 议题的评论串中提及 `@Codex`，以关联您的 Linear 账户。

## 将工作委派给 Codex

您可以通过以下两种方式委派工作：

### 将议题分配给 Codex

安装集成后，您可以像将议题分配给团队成员一样，将其分配给 Codex。Codex 会开始工作，并在该议题中发布进度更新。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### 在评论中提及 `@Codex`

您也可以在评论串中提及 `@Codex`，以委派工作或提出问题。Codex 回复后，请继续在该评论串中回复，以延续同一聊天。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Codex 开始处理议题后，会[选择工作所用的环境和代码仓库](#how-codex-chooses-an-environment-and-repo)。
若要指定特定代码仓库，请在评论中写明，例如：`@Codex fix this in openai/codex`。

如需跟踪进度：

- 打开议题中的 **活动** ，查看进度更新。
- 打开聊天链接，更详细地了解进展。

Codex 完成后，会发布摘要和已完成聊天的链接，以便您创建 Pull Request。

### Codex 如何选择环境和代码仓库

- Linear 会根据议题上下文推荐代码仓库。Codex 会选择与该建议最匹配的环境。如果请求含义不明确，则会改用您最近使用的环境。
- 聊天会基于该环境代码仓库映射中列出的首个代码仓库的默认分支运行。如需更改默认代码仓库或添加更多代码仓库，请在 Codex 中更新代码仓库映射。
- 如果没有合适的环境或代码仓库，Codex 会在 Linear 中回复说明，指导您先解决问题后再重试。

## 自动将议题分配给 Codex

您可以使用分流规则，自动将议题分配给 Codex：

1. 在 Linear 中，前往 **设置**。
2. 在 **您的团队**下，选择您的团队。
3. 在工作流程设置中，打开 **分流** 并启用此功能。
4. 在 **分流规则**中创建规则，然后依次选择 **委派** \> **Codex** （以及您希望设置的其他属性）。

Linear 会自动将进入分流流程的新议题分配给 Codex。
使用分流规则时，Codex 会使用议题创建者的账户运行聊天。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## 数据使用、隐私和安全

当您提及 `@Codex` 或将议题分配给 Codex 时，Codex 会接收您的议题内容，以理解您的请求并创建聊天。
数据处理遵循 OpenAI 的[隐私政策](https://openai.com/privacy)、[使用条款](https://openai.com/terms/)以及其他适用的[政策](https://openai.com/policies)。
有关安全性的更多信息，请参阅[Codex 安全文档](/zh-Hans/codex/agent-approvals-security)。

Codex 使用的大语言模型可能会出错。请务必审查回答和代码差异。

## 技巧和故障排除

- **未建立连接**：如果 Codex 无法确认您的 Linear 连接，它会在议题中回复用于关联账户的链接。
- **环境选择不符合预期**：在评论串中回复并注明您希望使用的环境（例如：`@Codex please run this in openai/codex`）。
- **处理了错误的代码部分**：请在议题中添加更多上下文，或在提及 `@Codex` 的评论中给出明确指令。
- **更多帮助**：请参阅[OpenAI 帮助中心](https://help.openai.com/)。

<a id="connect-linear-for-local-tasks-mcp"></a>

## 连接 Linear 以在本地工作（MCP）

如果您使用 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展，并希望其在本地访问 Linear 议题，请配置 Linear Model Context Protocol (MCP) 服务器。

如需了解更多信息，请[查看 Linear MCP 文档](https://linear.app/integrations/codex-mcp)。

由于两者共用同一配置，无论您使用 IDE 扩展还是 CLI，MCP 服务器的设置步骤都相同。

### 使用 CLI（推荐）

如果您已安装 CLI，请运行：

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

系统会提示您使用 Linear 账户登录，并将该账户连接到 Codex。

### 手动配置

1. 在您的编辑器中打开 `~/.codex/config.toml`。
2. 添加以下内容：

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. 运行 `codex mcp login linear` 以登录。
