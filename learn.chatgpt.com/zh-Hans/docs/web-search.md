<!-- source: https://learn.chatgpt.com/zh-Hans/docs/web-search -->

ChatGPT 内置第一方网页搜索工具。请将所有网页搜索结果视为
不可信输入。

在 ChatGPT 桌面应用中，您可以在聊天中询问最新信息。ChatGPT 会在对话记录中一并记录
搜索活动和其他工具调用。

在 ChatGPT 网页版中，您可以询问最新信息或要求提供来源。ChatGPT 使用网页搜索时，搜索结果和
引用会显示在聊天中。工作空间
设置可限制搜索功能的可用性。

在 CLI 中，传入 `--search` 即可为单次运行获取实时结果：

```bash
codex --search "Summarize the latest release notes for this dependency"

搜索会以 `web_search` 项的形式显示在交互式会话记录和
`codex exec --json` 输出中。

使用编辑器工作时，您可以在 IDE 扩展中让 Codex 进行搜索。该
扩展会使用所连接的 Codex 主机的搜索模式。聊天记录中会显示
搜索活动。

## 配置本地网页搜索

在本地 Codex 聊天中，Codex 默认启用缓存搜索。缓存模式使用
由 OpenAI 维护的索引，而不是实时获取任意网页，这会
降低提示注入风险，但无法消除这一风险。

网页搜索是托管工具，与沙盒中本地命令的网络访问相互独立。
它不会使用权限配置方案的网络代理或域名允许列表，并且
即使命令的网络访问被禁用，网页搜索仍可能可用。请根据需要通过
`web_search`、`tools.web_search.allowed_domains` 和受管理的
`allowed_web_search_modes` 配置搜索。搜索域名过滤器不会限制
本地命令流量、应用、连接器或 MCP 服务器。

当您的任务依赖最新信息时，请使用实时搜索。请将
`web_search = "live"` 写入 `config.toml`。设置 `web_search = "disabled"` 即可关闭
该工具。`"indexed"` 模式仅在
搜索索引放行请求时才允许访问外部网页。Codex 以完全访问权限运行时，网页搜索
默认返回实时结果。请参阅 [基础配置](/zh-Hans/codex/config-file/config-basic)
以了解配置文件的位置和优先级。

### 使用自定义模型提供商进行搜索

自定义模型提供商支持
兼容的搜索端点时，可以选择接入独立网页搜索：

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

自定义提供商的默认设置为 `supports_standalone_web_search = false`。
独立网页搜索仍在开发中，默认处于关闭状态。
设置这项提供商能力并不会启用该功能：提供商、
所选模型和运行时也必须支持独立搜索。工作空间限制和
受管理的搜索限制仍然适用。

有关适用于 Codex 云端环境的网络边界，请参阅 [互联网
访问](/zh-Hans/codex/cloud/internet-access)。
