<!-- source: https://learn.chatgpt.com/zh-Hans/docs/customization/memories -->

记忆可让 ChatGPT 和 Codex 将先前工作中的有用上下文延续到
后续工作中。
ChatGPT 网页版使用 ChatGPT 记忆，而 Codex 本地客户端使用独立的本地
记忆存储和控制项。

请将团队必须遵循的指导保存在 `AGENTS.md` 或已提交到代码仓库的文档中。应将
记忆视为辅助回顾信息的工具，而不要将其作为必须
始终适用的规则的唯一来源。

在 ChatGPT 桌面应用中，使用 `/memories` 设置聊天能否使用
本地记忆，以及能否为后续记忆提供内容。如需开启或关闭此功能，请前往
**设置 \> 个性化** 进行管理。

在 **设置 \> 个性化**中管理 ChatGPT 记忆。ChatGPT Work 使用
您的账户和工作空间中可用的记忆设置；不会使用
Codex 本地记忆存储或本地记忆控制项。

在 Codex CLI 的交互式会话中，使用 `/memories` 控制当前
聊天能否使用现有本地记忆，以及能否作为生成后续
记忆的输入。如果该命令不可用，请参阅[配置本地记忆](#configure-local-memories)
中的说明。

IDE 扩展使用所连接 Codex 主机的本地记忆存储。
该主机启用记忆后，请使用与 Codex CLI
相同的聊天级控制项。

[计算机使用记录](/zh-Hans/codex/customization/computer-history)是一项 macOS 桌面
功能，可将允许访问的应用和网站中的活动转化为记忆和
时间线，供 ChatGPT 和 Codex 参考。

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## Codex 本地记忆的工作原理

启用记忆后，Codex 可将符合条件的以往
聊天中的有用上下文转换为本地记忆文件。Codex 会跳过仍在进行或持续时间较短的会话，
从生成的记忆字段中隐去机密信息，并在
后台更新记忆，而不是在每次聊天结束时立即更新。

聊天结束后，记忆可能不会立即更新。Codex 会等到
聊天闲置足够长的时间，以免为仍在
进行的工作生成摘要。

当您的 Codex 速率限制剩余百分比低于配置的
阈值时，记忆生成也可能跳过一轮后台处理，以免 Codex 在您接近
限制时消耗额度。

## 本地记忆存储

Codex 将记忆存储在您的 Codex 主目录下，默认位置为
`~/.codex`。有关详细信息，请参阅[配置和状态位置](/zh-Hans/codex/config-file/config-advanced#config-and-state-locations)，了解
Codex 如何使用 `CODEX_HOME`。

主要记忆文件位于 `~/.codex/memories/` 目录下，包含摘要、
持久化条目、近期输入，以及来自以往聊天的佐证。

请将这些文件视为已生成的状态数据。排查故障时
或在共享您的 Codex 主目录之前，您可以检查这些文件，但不要将
手动编辑文件作为主要控制方式。

<a id="control-local-memories-per-task"></a>

## 按聊天分别控制本地记忆

在 ChatGPT 桌面应用和 Codex TUI 中，使用 `/memories` 控制当前聊天的
记忆行为。聊天级选项可让您决定当前
聊天能否使用现有记忆，以及 Codex 能否使用该聊天
生成后续记忆。

聊天级选项不会更改您的全局记忆设置。

## 审查本地记忆

请勿在记忆中存储机密信息。Codex 会从生成的记忆
字段中隐去机密信息，但在共享您的 Codex 主目录
或生成的记忆产物之前，您仍应审查记忆文件。

<a id="enable-memories"></a>
<a id="configuration"></a>

## 配置本地记忆

Codex 本地记忆默认关闭。在 ChatGPT 桌面应用中，打开
**设置 \> 个性化** ，然后开启 **启用记忆**。

如需通过配置文件设置，请将功能标志添加到 `config.toml`：

```toml
[features]
memories = true

有关配置文件的位置和记忆相关设置的完整列表，请参阅
[基础配置](/zh-Hans/codex/config-file/config-basic)以及[配置
参考资料](/zh-Hans/codex/config-file/config-reference)。

常见的记忆相关设置包括：

- `memories.generate_memories`：控制能否将新创建的聊天
  存储为生成记忆的输入。
- `memories.use_memories`：控制 Codex 是否将现有记忆注入
  后续会话。
- `memories.disable_on_external_context`：设为 `true` 时，使用过
  外部上下文（例如 MCP 工具调用、网页搜索或工具搜索）的聊天不会用于
  生成记忆。较旧的 `memories.no_memories_if_mcp_or_web_search` 配置键
  仍可作为别名使用。
- `memories.min_rate_limit_remaining_percent`：控制启动记忆生成前，Codex 速率限制
  需要达到的最低剩余百分比。
- `memories.extract_model`：覆盖为每个聊天提取记忆时使用的
  模型。
- `memories.consolidation_model`：覆盖用于整合全局记忆的
  模型。
