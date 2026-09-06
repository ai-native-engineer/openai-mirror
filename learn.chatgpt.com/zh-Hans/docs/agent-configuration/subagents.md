<!-- source: https://learn.chatgpt.com/zh-Hans/docs/agent-configuration/subagents -->

ChatGPT Work 和 Codex 可以并行启动专用智能体来运行子智能体工作流，然后将它们的结果汇总到一条响应中。这对于适合高度并行处理的复杂任务尤其有帮助，例如探索代码库或实施包含多个步骤的功能计划。

在本地 Codex 客户端中，您还可以针对不同任务，定义采用不同模型配置和指令的自定义智能体。

## 可用性

ChatGPT Work 向符合条件的账户开放子智能体工作流及其活动信息。

<a id="custom-agents"></a>

当前的 Codex 版本默认启用子智能体工作流。子智能体活动会显示在 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中。

由于每个子智能体都会独立使用模型和工具，子智能体工作流比类似的单智能体运行消耗更多 Token。

在 ChatGPT Work 中，请要求 ChatGPT 将可独立开展的工作委派给子智能体。这些智能体在 ChatGPT 的托管环境中运行，其活动和结果会显示在聊天中。在大多数智能级别下，您需要明确要求进行委派。使用 Ultra 时，如果并行智能体能够显著提高速度或质量，ChatGPT 可以主动委派工作。

请在应用聊天中要求 Codex 将工作中相互独立的部分委派给子智能体。
当前的本地 Codex 版本会在您直接提出要求，
或适用的 `AGENTS.md` 或技能指令要求委派时执行委派。
应用会显示每个子智能体线程，
方便您查看其工作以及返回主聊天的摘要。

请在交互式 CLI 会话中要求 Codex 使用子智能体。
Codex 也可以遵循适用的 `AGENTS.md` 或技能指令中的委派要求。
智能体运行期间，请使用 `/agent` 查看并切换智能体线程。
主线程会汇总子智能体的结果，并纳入最终响应。

请在 IDE 聊天中要求 Codex 将工作中相互独立的部分委派给子智能体。
Codex 也可以遵循适用的 `AGENTS.md` 或技能指令，
按要求执行委派。后台智能体界面可用时，
正在运行的子智能体会显示在编辑器上方。展开面板即可查看其状态，
停止所有正在运行的子智能体，或打开单个子智能体线程。

## 子智能体工作流的优势

即使拥有较大的上下文窗口，模型仍然存在局限。如果您在用于确定需求、约束和决策的主聊天中塞入探索记录、测试日志、堆栈跟踪和命令输出等杂乱的中间结果，随着时间推移，会话的可靠性可能下降。

这种现象通常称为：

- **上下文污染**：有用信息被杂乱的中间输出淹没。
- **上下文腐化**：随着聊天被相关性较低的细节填满，性能逐渐下降。

如需了解背景，请参阅 Chroma 关于[上下文腐化](https://research.trychroma.com/context-rot)的文章。

子智能体工作流将容易产生干扰信息的工作移出主线程，从而带来以下帮助：

- 让 **主智能体** 专注于需求、决策和最终输出。
- 并行运行专用的 **子智能体** ，开展探索、测试或日志分析。
- 让子智能体返回 **摘要** ，而非原始的中间输出。

当各项工作能够独立并行时，子智能体工作流还可以节省时间，并通过将规模较大的任务拆分成范围明确的部分，使其更易处理。例如，Codex 可以将一份包含数百万 Token 的文档分析任务拆成多个较小的问题，并将提炼后的要点返回主线程。

建议先将并行智能体用于探索、测试、问题分流和总结等以读取为主的任务。对于以写入为主的并行工作流，则需更加谨慎，因为多个智能体同时编辑代码可能造成冲突，并增加协调开销。

## 核心术语

Codex 在子智能体工作流中使用以下相关术语：

- **子智能体工作流**：由 Codex 并行运行多个智能体并汇总其结果的工作流。
- **子智能体**：由 Codex 启动并受委派处理特定任务的智能体。
- **智能体线程**：子智能体执行工作的线程。支持该功能的客户端允许您打开这些线程，查看进度或结果。

## 触发子智能体工作流

在大多数智能级别下，请直接要求使用子智能体或让智能体并行工作。Ultra 支持主动委派，因此无需您另行提出要求，ChatGPT 就可以委派适合独立处理的工作。

请直接要求使用子智能体或让智能体并行工作。如果适用的项目或技能指令要求委派，Codex 也可以执行委派。

在实际使用中，手动触发是指使用“启动两个智能体”“并行委派这项工作”或“每个要点使用一个智能体”等直接指令。由于每个子智能体都会独立使用模型和工具，子智能体工作流比类似的单智能体运行消耗更多 Token。

一条好的子智能体提示应说明如何分工、Codex 是否应等待所有智能体完成后再继续，以及应返回何种摘要或输出。

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## 选择模型和推理设置

不同智能体需要不同的模型和推理设置。

在 ChatGPT Work 中，请通过编辑器选择模型和智能级别。
可用的智能级别因所选模型而异，可能包括 **轻度**、 **中**、 **高**、
**极高**和 **Max**。 **Ultra** 仅适用于符合条件的账户和受支持的模型。
它采用最高推理强度，
并允许 ChatGPT 主动将适合的工作委派给子智能体。

在其他智能级别下，如果您希望并行委派工作，请明确要求使用子智能体。

如果您未为子智能体配置模型或 `model_reasoning_effort`，
它会继承父智能体的模型和推理强度。
如果明确的启动请求或 `[agents]` 默认设置指定了模型，
却没有明确指定或配置推理强度，子智能体会使用该模型的默认推理强度。
要针对每项任务平衡智能、速度和价格，
您可以在提示中指定具体模型或推理强度，
在 `config.toml` 中配置 `[agents]` 的默认值，或直接在自定义智能体文件中设置 `model` 和
`model_reasoning_effort`。
例如，使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> 进行快速扫描，或为要求更高的推理任务选用推理强度更高的 <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> 配置。

  对于在 Codex 中执行的大多数任务，建议先使用{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>。如果您希望以更快的速度、更低的成本
处理较轻量的子智能体工作，
  请使用{" "}<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>。

### 模型选择

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**：对于承担复杂任务的智能体，建议优先选用此模型。它最擅长处理目标不够明确、步骤较多，且需要在较大上下文中进行规划、使用工具、验证并持续跟进的工作。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**：适用于优先考虑速度和效率而非深度的智能体，例如执行探索、以读取为主的扫描、大文件审查或辅助文档处理。它很适合用于并行运行并向主智能体返回提炼结果的智能体。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**：适用于运行快速、任务范围较窄的智能体，用来处理目标清晰、可重复或大批量的工作。

### 推理强度（`model_reasoning_effort`）

- **`ultra`**：当所选模型支持该级别时，
  可用于最深入的推理。
- **`max`** 和 **`xhigh`**：当所选模型支持这些级别时，
  可用于要求特别高的推理任务。
- **`high`**：适用于需要梳理复杂逻辑、检验假设或处理边界情况的智能体，例如审查智能体或专注安全的智能体。
- **`medium`**：适合大多数智能体的均衡默认设置。
- **`low`**：适用于任务简单且最注重速度的情况。

更高的推理强度会延长响应时间、增加 Token 消耗，但可能提高复杂工作的质量。详情请参阅[模型](/zh-Hans/codex/models)、[基础配置](/zh-Hans/codex/config-file/config-basic)和[配置参考资料](/zh-Hans/codex/config-file/config-reference)。

## 编排与线程控制

ChatGPT 或 Codex 负责智能体之间的编排，包括启动新的子智能体、转发后续指令、等待结果以及关闭智能体线程。

当多个智能体同时运行时，Codex 会等待所有请求的结果就绪，然后返回汇总后的响应。

在大多数智能级别下，ChatGPT 会在收到直接请求后启动智能体。使用 Ultra 时，如果并行工作有帮助，ChatGPT 也可以主动委派。

当前的本地 Codex 版本会在收到直接请求，或适用的项目或技能指令要求委派时，启动智能体。

要了解实际运行效果，请在您的项目中尝试以下提示：

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## 管理子智能体

打开 **子智能体** ，即可查看只读的 **进行中** 和 **已完成** 列表。
选择已完成的子智能体，即可查看其详细信息和结果。
网页侧边栏会显示子智能体的活动，
但不提供停止单个子智能体或调整其工作方向的控件。

- 通过主线程中显示的活动打开子智能体线程，即可查看其工作。
- 请直接要求 Codex 调整正在运行的子智能体的工作方向、停止其运行，或关闭已完成的子智能体线程。

  

  

- 在 CLI 中使用 `/agent` 切换正在运行的智能体线程，并查看当前进行中的线程。
- 直接要求 Codex 指导正在运行的子智能体、停止其运行，或关闭已完成的智能体线程。

- 后台智能体面板可用时，展开面板即可查看状态、停止正在运行的子智能体，或打开子智能体线程。
- 直接要求 Codex 指导正在运行的子智能体、停止其运行，或关闭已完成的子智能体线程。

## 审批和沙盒控制

子智能体会继承您当前的沙盒策略。

ChatGPT Work 在其托管环境中运行子智能体，不提供本地 Codex 沙盒或审批模式控制选项。子智能体使用父级聊天可用的工具。网站和连接器权限仍由各工具分别控制。

子智能体会继承编辑器下方所选的权限模式。请先为父级轮次选择权限模式，再要求 Codex 委派工作。

在交互式 CLI 会话中，即使您正在查看主线程，
非活动智能体线程也可能发出审批请求。
审批浮层会显示来源线程的标签，您可以按 `o` 打开该线程，
再批准、拒绝或答复该请求。

在非交互式流程中，或运行无法显示新的审批请求时，需要新审批的操作会失败，Codex 会将错误反馈给父级工作流程。

Codex 在启动子智能体时，也会重新应用父级轮次当前生效的运行时覆盖设置。
这些设置包括您在会话中以交互方式选择的沙盒和审批选项，
例如通过 `/permissions` 进行的更改或使用 `--yolo`。
即使所选的自定义智能体文件设置了不同的默认值，这些覆盖设置仍会生效。

子智能体会继承编辑器下方所选的权限模式。请先为父级轮次选择权限模式，再要求 Codex 委派工作。

您还可以覆盖单个[自定义智能体](#custom-agents)的沙盒配置，例如明确指定某个智能体以只读模式运行。

## 自定义智能体

Codex 内置以下智能体：

- `default`：通用后备智能体。
- `worker`：侧重执行的智能体，用于实现和修复。
- `explorer`：以读取为主的代码库探索智能体。

要定义自己的自定义智能体，请添加独立的 TOML 文件：
个人智能体的文件放在 `~/.codex/agents/` 下，
项目级智能体的文件放在 `.codex/agents/` 下。

每个文件定义一个自定义智能体。Codex 会将这些文件作为新启动会话的配置层加载，因此自定义智能体可以覆盖普通 Codex 会话配置中的同类设置。相比专用的智能体清单，这种方式可能显得更繁琐；随着编写和共享方式逐渐成熟，这种格式也可能发生变化。

每个独立的自定义智能体文件都必须定义：

- `name`
- `description`
- `developer_instructions`

如果自定义智能体文件设置了 `model` 或 `model_reasoning_effort`，则以文件中的值为准。
在应用该文件之前，Codex 会按以下优先级确定每项设置的值：
先采用启动时显式指定的值，再采用对应的 `[agents]` 默认值，
最后采用父级的值。如果显式启动请求或 `[agents]` 默认值选择了模型，
而两者均未指定推理强度，
Codex 会使用该模型的默认推理强度。仅设置 `model` 的自定义智能体文件
会保留此前确定的推理强度。如果所选模型不支持该强度，
或者您希望使用其他强度，也应在文件中设置 `model_reasoning_effort`。
其他会话设置，例如 `sandbox_mode`、`mcp_servers`
和 `skills.config`，若未在自定义智能体文件中设置，
则会从父级继承。

### 全局设置

全局子智能体设置仍位于您的[配置](/zh-Hans/codex/config-file/config-basic#configuration-precedence)中的 `[agents]` 下。

| 字段                                       | 类型    | 必填 | 用途                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | 布尔值 |    否    | 启用或禁用多智能体工具。                                |
| `agents.max_concurrent_threads_per_session` | 数值  |    否    | 限制同时打开的已启动智能体线程数量，不包括主线程。 |
| `agents.default_subagent_model`             | 字符串  |    否    | 设置所启动智能体的默认模型。                           |
| `agents.default_subagent_reasoning_effort`  | 字符串  |    否    | 设置所启动智能体的默认推理强度。                |
| `agents.interrupt_message`                  | 布尔值 |    否    | 智能体轮次中断时，记录一条模型可见的消息。   |

**说明：**

- `agents.enabled` 的默认值为 `true`。将其设为 `false` 可禁用多智能体工具。
- 未设置 `agents.max_concurrent_threads_per_session` 时，Codex 会选择默认值。现有配置可以继续使用 `agents.max_threads` 作为旧版别名。
- 启动时显式指定的值会覆盖 `agents.default_subagent_model` 和 `agents.default_subagent_reasoning_effort`。
- `agents.interrupt_message` 的默认值为 `true`。将其设为 `false` 可使智能体的上下文不包含模型可见的中断消息。
- 如果自定义智能体的名称与 `explorer` 等内置智能体相同，则优先使用自定义智能体。

### 自定义智能体文件模式

| 字段                    | 类型   | 必填 | 用途                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | 字符串 |   是    | Codex 启动或提及此智能体时使用的智能体名称。 |
| `description`            | 字符串 |   是    | 面向用户的指引，说明 Codex 应在何时使用此智能体。     |
| `developer_instructions` | 字符串 |   是    | 定义智能体行为的核心指令。             |

您还可以在自定义智能体文件中加入其他受支持的 `config.toml` 键，例如 `model`、`model_reasoning_effort`、`sandbox_mode`、`mcp_servers` 和 `skills.config`。

Codex 通过 `name` 字段识别自定义智能体。最简单的做法是让文件名与
智能体名称一致，但最终应以 `name` 字段
为准。

### 自定义智能体示例

最好的自定义智能体职责专一，做事方式明确。请为每个智能体指定一项清晰的职责，配置与之匹配的可用工具，并提供指令，避免其偏离职责范围、转而处理其他相关工作。

#### 示例 1：PR 审查

此模式将审查工作分配给三个各有侧重的自定义智能体：

- `pr_explorer` 梳理代码库结构并收集证据。
- `reviewer` 排查正确性、安全性和测试方面的风险。
- `docs_researcher` 通过专用 MCP 服务器查阅框架或 API 文档。

项目配置（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`：

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`：

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`：

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

此配置适合以下这类提示：

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### 示例 2：前端集成调试

此模式适用于 UI 回归问题、不稳定的浏览器流程，或同时涉及应用代码和正在运行的产品的集成缺陷。

项目配置（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`：

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`：

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`：

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

此配置适合以下这类提示：

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
