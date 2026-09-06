<!-- source: https://learn.chatgpt.com/zh-Hans/docs/import -->

使用导入流程，将其他智能体中的指令、设置、技能、插件、项目
和近期工作内容导入 ChatGPT 桌面应用或 Codex CLI。
桌面应用支持从 **Claude Code**、<strong>Claude Cowork</strong>
或 **Cursor** 导入。Codex CLI 支持从 **Claude Code** 或 **Cursor** 导入。

桌面应用可直接导入受支持的内容，并让您完成需要授权的
已导入插件或连接的设置。您还可以通过自动更新，让导入的
工作内容保持同步。

导入不会更改或删除您现有的智能体设置。

  

## 开始导入

### 在桌面应用中导入

1. 在 ChatGPT 桌面应用中，打开 **设置 \> 导入**。如果暂未提供 **导入** 
   设置项，请打开 **常规** ，找到 **导入其他
   智能体设置**。
2. 选择 **导入**。
3. 选择要从中导入的智能体，然后选择 **继续**。
4. 在 **选择要导入的内容** 页面中选择所需内容，然后选择 **继续**。
5. 导入完成后，打开已导入的项目或聊天，继续工作。

### 同步已导入的工作内容

在 ChatGPT 桌面应用中，打开 **设置 \> 导入** 并启用自动
更新，使已导入的工作内容与原智能体保持同步。您还可以
在同一设置页面查看导入历史记录。

### 在 Codex CLI 中导入

1. 启动本地 Codex CLI 会话并输入 `/import`。
2. 选择 **Claude Code** 或 **Cursor**。
3. 选择您要导入的受支持设置、项目文件和
近期聊天。
4. 审查已导入的配置，然后继续在 Codex 中工作。

Codex CLI 最多可导入最近 30 天内的 50 个聊天。`/import` 命令
在任务运行期间、远程会话中，或连接
到本地 app-server 守护进程时不可用。请参阅 [CLI 斜杠
命令](/codex/developer-commands?surface=cli#cli-import-claude-code-or-cursor-setup-with-import)。

  

## 导入的工作原理

导入流程会检查您的用户级设置和现有项目。
用户级设置来自您计算机上的文件。项目级设置则来自您选择的
代码仓库和文件夹中的文件。

导入时，ChatGPT 会：

1. 检测受支持的设置和近期工作内容。
2. 导入您选择的内容。
3. 保持您现有的智能体设置不变。
4. 检查已导入的插件或连接是否仍需完成设置。
5. 在您需要完成设置时显示状态卡片。

## ChatGPT 可以导入的内容

| 导入项                     | 目标位置                                             |
| --------------------------------- | ------------------------------------------------------- |
| 指令文件                 | [`AGENTS.md`](/zh-Hans/codex/agent-configuration/agents-md)     |
| `settings.json`                   | [`config.toml`](/zh-Hans/codex/config-file/config-basic)        |
| 技能                            | [技能](/zh-Hans/codex/build-skills)                           |
| 插件                           | 插件                                                 |
| 现有项目文件夹          | 使用相同文件夹的项目                         |
| 来自 Claude Code 的项目记忆 | [记忆](/zh-Hans/codex/customization/memories)               |
| 最近 30 天内的聊天       | ChatGPT 聊天                                           |
| MCP 服务器配置          | [Codex MCP 配置](/zh-Hans/codex/extend/mcp)            |
| 钩子                             | [Codex 钩子](/zh-Hans/codex/hooks)                             |
| 斜杠命令                    | [技能](/zh-Hans/codex/build-skills)                           |
| 子智能体                         | [Codex 子智能体](/zh-Hans/codex/agent-configuration/subagents) |

## 导入后完成设置

导入完成后，应用会在左下角显示状态卡片。
如果已导入的插件或连接仍需完成设置，卡片会明确指出。

当应用标记出需要处理的内容时，请选择 **完成** ，然后按照
提示完成设置。

## 导入后需审查的内容

在依赖已导入的设置之前，请先审查其内容，尤其注意：

- 已导入的技能和智能体中的工具限制或权限。
- 使用自定义身份验证、标头、环境变量或
传输方式的 MCP 服务器设置。您可能需要重新登录。
- 导入后行为可能有所不同的钩子。
- 需要手动完成后续操作的插件、市场或其他设置。
- 依赖参数、Shell
插值或文件路径占位符的提示模板或命令式提示。

## 导入后

导入完成后，打开您导入的其中一个项目，
继续开展工作。请参阅[使用 ChatGPT](/zh-Hans/codex/use-chatgpt)，了解如何开始
下一项任务。
