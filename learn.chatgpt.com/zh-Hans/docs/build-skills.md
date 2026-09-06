<!-- source: https://learn.chatgpt.com/zh-Hans/docs/build-skills -->

使用智能体技能，为 ChatGPT 和 Codex 扩展特定任务所需的能力。
每项技能将指令、资源和可选脚本打包，使任一产品
都能可靠地执行工作流程。技能基于
[开放的智能体技能标准](https://agentskills.io)构建。

技能是编写可复用工作流的格式。插件通过 ChatGPT 和 Codex 共用的
通用插件目录分发可复用技能和连接器。
插件可用于网页版 ChatGPT、桌面端和移动端的聊天与 Work，
也可用于 ChatGPT 桌面应用中的 Codex，或通过 Codex
CLI 使用。请先使用技能设计工作流程本身；如有需要，可将其打包为
[插件](https://developers.openai.com/plugins/build/plugins)，供
其他人安装。

独立技能可在 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中使用。
插件中捆绑的技能还可用于网页版 ChatGPT、桌面端
和移动端的聊天与 Work。

在 ChatGPT 桌面应用中，打开侧边栏中的 **技能** ，即可查看和探索
您在各个项目中创建的技能。

  
    
  

技能采用 **渐进式披露** 机制，高效管理上下文。ChatGPT 与
Codex 首先获取每项技能的名称和描述，决定使用某项技能后，才加载
完整的 `SKILL.md` 指令。

在 Codex 中，初始列表还包含每项技能的文件路径。为避免挤占
提示中的其他内容，该列表最多占用模型上下文窗口的 2%；
如果上下文窗口大小未知，则最多使用 8,000 个字符。若安装了大量
技能，Codex 会优先缩短技能描述；对于规模较大的技能集合，
Codex 可能会省略初始列表中的部分技能，并显示警告。

这项预算仅适用于初始技能列表。Codex 选定某项技能后，仍会读取该技能完整的 SKILL.md 指令。

技能是一个包含 `SKILL.md` 文件的目录，还可包含脚本和参考资料。`SKILL.md` 文件必须包含 `name` 和 `description`。

<a id="how-codex-uses-skills"></a>

## ChatGPT 和 Codex 如何使用技能

ChatGPT 和 Codex 可通过两种方式激活技能：

1. **显式调用：** 直接在您的提示中指定技能。在
   ChatGPT 中，输入 `@` 即可选择技能；在 Codex CLI 或 IDE 扩展中，运行
`/skills` 或输入 `$` 即可引用技能。
2. **隐式调用：** 当您的任务
   与技能的 `description` 相匹配时，ChatGPT 或 Codex 可以选择该技能。

由于隐式匹配取决于 `description`，请编写简洁的描述，
并明确适用范围和边界。将关键使用场景和触发词置于描述开头，
这样即使描述被缩短，主机仍能匹配该技能。

## 创建技能

如果您已熟悉相关工作流程，并且演示比描述更容易，请使用
[录制与重放](/zh-Hans/codex/extend/record-and-replay)。录制器会记录工作流程，
检查各个步骤，并根据
演示内容起草可复用的技能。

如果您希望通过描述来创建技能，请使用内置创建器。
在 ChatGPT Work 中，使用 `@skill-creator` 调用它；在 Codex 中，调用方式如下：

```text
$skill-creator

创建器会询问技能的用途、触发时机，以及它应仅包含指令还是也包含脚本。默认情况下，技能仅包含指令。

您也可以创建一个包含 `SKILL.md` 文件的文件夹，以手动创建技能：

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex 会自动检测技能变更。如果更新未显示，请重启 Codex。

<a id="where-to-save-skills"></a>

## Codex 加载本地技能的位置

Codex 会从代码仓库、用户、管理员和系统位置读取技能。对于代码仓库，Codex 会从您当前的工作目录向上遍历至代码仓库根目录，并扫描各级目录中的 `.agents/skills`。如果两项技能的 `name` 相同，Codex 不会将其合并；两者都可能显示在技能选择器中。

| 技能范围 | 位置                                                                                                  | 建议用途                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> 当前工作目录：您启动 Codex 的位置。                           | 在代码仓库或代码环境中，团队可以提交与特定工作文件夹相关的技能，例如仅适用于某个微服务或模块的技能。                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> 在 Git 代码仓库中启动 Codex 时，当前工作目录（CWD）上一级的文件夹。         | 如果代码仓库包含嵌套文件夹，组织可以在上级文件夹中提交适用于共享区域的技能。                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> 在 Git 代码仓库中启动 Codex 时，该代码仓库最顶层的根文件夹。 | 如果代码仓库包含嵌套文件夹，组织可以提交适用于所有代码仓库用户的技能。这些技能属于根级技能，可供代码仓库内任何子文件夹使用。 |
| `USER`      | `$HOME/.agents/skills` <br /> 提交到用户个人文件夹中的技能。                         | 用于整理与用户相关的技能，适用于该用户可能使用的任何代码仓库。                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> 提交到计算机或容器中共享系统位置的技能。 | 用于 SDK 脚本和自动化，也可用于提交默认的管理员技能，供计算机上的每位用户使用。                                                                                     |
| `SYSTEM`    | 由 OpenAI 随 Codex 捆绑提供。                                                                             | 适用于广大用户的实用技能，例如 skill-creator 和 plan 技能。所有用户启动 Codex 时即可使用。                                                                   |

Codex 支持符号链接形式的技能文件夹，并会在扫描这些位置时跟随符号链接访问其目标。

这些位置用于编写技能和在本地发现技能。如果您希望
在单个代码仓库之外分发可复用技能，或者选择将技能与
连接器捆绑，请使用[插件](https://developers.openai.com/plugins/build/plugins)。

## 使用插件分发技能

直接使用技能文件夹最适合在本地编写技能和构建代码仓库范围的工作流。
如果您希望分发可复用技能、将两项或更多技能捆绑在一起，
或将技能与连接器一同发布，请将它们打包成
[插件](https://developers.openai.com/plugins/build/plugins)。

插件可以包含一项或多项技能，也可以选择将已注册的 MCP 服务器连接、
随附的 MCP 服务器配置以及展示资源
打包在同一个软件包中。

## 安装精选技能以供本地使用

要为您的本地 Codex 环境添加内置技能之外的精选技能，请使用 `$skill-installer`。例如，安装 `$linear` 技能：

```bash
$skill-installer linear

您也可以通过提示让安装器从其他代码仓库下载技能。
Codex 会自动检测新安装的技能；如果某项技能未显示，
请重启 Codex。

这种方式适合本地设置和实验。
如果希望以可复用的方式分发您自己的技能，请优先使用插件。

## 启用或禁用本地 Codex 技能

使用 `[[skills.config]]` 配置项，在 `~/.codex/config.toml` 中禁用技能，而无需将其删除：

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

修改 `~/.codex/config.toml` 后，请重启 Codex。

## 可选元数据

添加 `agents/openai.yaml`，即可配置[ChatGPT 桌面应用](/zh-Hans/codex/app)中的 UI 元数据、设置调用策略并声明工具依赖项，从而让技能使用体验更加流畅。

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation`（默认值：`true`）：设置为 `false` 时，Codex 不会根据用户提示隐式调用该技能；但仍可通过 `$skill` 显式调用。

## 最佳实践

- 让每项技能专注于一项任务。
- 除非需要确定性行为或外部工具，否则应优先使用指令，而非脚本。
- 以祈使句编写操作步骤，并明确输入和输出。
- 结合技能描述测试提示，确认触发行为符合预期。

如需更多示例，请参阅
[GitHub CI 修复](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)、
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf)、
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear)、
[openai/skills](https://github.com/openai/skills)以及
[智能体技能规范](https://agentskills.io/specification)。如需
以可安装形式分发，建议使用[插件](https://developers.openai.com/plugins/build/plugins)。
