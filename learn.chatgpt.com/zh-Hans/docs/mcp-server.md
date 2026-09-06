<!-- source: https://learn.chatgpt.com/zh-Hans/docs/mcp-server -->

# 将 Codex 作为 MCP 服务器运行

  `codex mcp-server` 已弃用。请改用 [Codex App
  Server](/zh-Hans/codex/app-server)。如需从 Claude Code 调用 Codex，请使用
[适用于 Claude Code 的 Codex 插件](https://github.com/openai/codex-plugin-cc)，
  该插件使用 App Server。本页为
  现有集成提供这条已弃用命令的说明。

您可以将 Codex 作为 MCP 服务器运行，并通过其他 MCP 客户端连接到该服务器（例如，使用 [OpenAI Agents SDK MCP 集成](/api/docs/guides/agents/integrations-observability#mcp)构建的智能体）。

要将 Codex 作为 MCP 服务器启动，您可以使用以下命令：

```bash
codex mcp-server
```

您可以通过 [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) 启动 Codex MCP 服务器：

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

发送 `tools/list` 请求即可查看两个工具：

**`codex`**：使用以下提示和配置覆盖项运行 Codex 会话：

| 属性                 | 类型     | 说明                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** （必需）  | `string` | 用于启动 Codex 对话的初始用户提示。                                                 |
| `approval-policy`        | `string` | 模型生成的 shell 命令的审批策略：`untrusted`、`on-request` 和 `never`。       |
| `base-instructions`      | `string` | 用于替代默认指令的一组指令。                                              |
| `compact-prompt`         | `string` | 压缩对话时使用的提示。                                                            |
| `config`                 | `object` | 用于覆盖 `$CODEX_HOME/config.toml` 中相应设置的单项配置。                     |
| `cwd`                    | `string` | 会话的工作目录。如果是相对路径，则以服务器进程的当前目录为基准进行解析。 |
| `developer-instructions` | `string` | 以开发者角色消息形式注入的开发者指令。                                             |
| `model`                  | `string` | 模型名称的可选覆盖值（例如 `gpt-5.6-terra`）。                                     |
| `sandbox`                | `string` | 沙盒模式：`read-only`、`workspace-write` 或 `danger-full-access`。                                   |

**`codex-reply`**：通过提供线程 ID 和提示继续 Codex 会话。`codex-reply` 工具接受以下属性：

| 属性                      | 类型   | 说明                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** （必需）       | 字符串 | 用于继续 Codex 对话的下一条用户提示。  |
| **`threadId`** （必需）     | 字符串 | 要继续的线程的 ID。                         |
| `conversationId`（已弃用） | 字符串 | `threadId` 的已弃用别名（为保持兼容性而保留）。 |

请使用 `tools/call` 响应中 `structuredContent.threadId` 提供的 `threadId`。审批提示（exec/patch）的 `params` 载荷中也包含 `threadId`。

响应载荷示例：

```json
{
  "structuredContent": {
    "threadId": "019bbb20-bff6-7130-83aa-bf45ab33250e",
    "content": "`ls -lah` (or `ls -alh`) — long listing, includes dotfiles, human-readable sizes."
  },
  "content": [
    {
      "type": "text",
      "text": "`ls -lah` (or `ls -alh`) — long listing, includes dotfiles, human-readable sizes."
    }
  ]
}
```

请注意，如果存在 `"structuredContent"`，较新的 MCP 客户端通常只会将其作为工具调用结果；不过，Codex MCP 服务器也会返回 `"content"`，供较旧的 MCP 客户端使用。

# 创建多智能体工作流

Codex CLI 的用途远不止运行临时任务。通过让 CLI 以 [Model Context Protocol](https://modelcontextprotocol.io/)（MCP）服务器的形式提供服务，并使用 OpenAI Agents SDK 进行编排，您可以创建具有确定性且可供审查的工作流，并将其从单个智能体扩展到完整的软件交付流水线。

本指南将带您完成 [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb) 中展示的同一工作流。您将：

- 将 Codex CLI 作为长时间运行的 MCP 服务器启动；
- 构建一个目标明确的单智能体工作流，生成一款可玩的浏览器游戏；
- 通过任务交接和护栏机制编排多智能体团队，并生成可供您事后审查的完整跟踪记录。

开始前，请确保您具备以下条件：

- 本地已安装 [Codex CLI](/zh-Hans/codex/cli)，且 `codex` 命令可用。
- Python 3.10+，且已安装 `pip`。
- 如果您要运行上述 MCP Inspector 示例，还需要 Node.js 18+。
- 一个保存在本地的 OpenAI API 密钥。您可以在 [OpenAI 控制面板](https://platform.openai.com/account/api-keys) 中创建或管理密钥。

为本指南创建一个工作目录，并将您的 API 密钥添加到 `.env` 文件中：

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## 安装依赖项

Agents SDK 负责对 Codex 进行编排，并处理任务交接和跟踪记录。请安装最新的 SDK 软件包：

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  激活虚拟环境可将 SDK 依赖项与
系统的其余部分隔离。

## 将 Codex CLI 初始化为 MCP 服务器

首先，将 Codex CLI 设为 Agents SDK 可调用的 MCP 服务器。该服务器提供两个工具（`codex()` 用于启动对话，`codex-reply()` 用于继续对话），并让 Codex 在智能体的多轮交互中持续运行。

创建一个名为 `codex_mcp.py` 的文件，并添加以下内容：

```python

from agents import Agent, Runner
from agents.mcp import MCPServerStdio

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={
            "command": "codex",
            "args": ["mcp-server"],
        },
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:
        print("Codex MCP server started.")
        # More logic coming in the next sections.
        return

if __name__ == "__main__":
    asyncio.run(main())
```

运行一次脚本，验证 Codex 能否成功启动：

```bash
python codex_mcp.py
```

脚本输出 `Codex MCP server started.` 后便会退出。在接下来的章节中，您将在更丰富的工作流中复用同一个 MCP 服务器。

## 构建单智能体工作流

我们先从一个范围明确的示例开始，使用 Codex MCP 交付一款小型浏览器游戏。该工作流依赖两个智能体：

1. **游戏设计师**：编写游戏设计概要。
2. **游戏开发者**：通过调用 Codex MCP 实现游戏。

使用以下代码更新 `codex_mcp.py`。这段代码保留了上面的 MCP 服务器设置，并添加了这两个智能体。

```python

from dotenv import load_dotenv

from agents import Agent, Runner, set_default_openai_api
from agents.mcp import MCPServerStdio

load_dotenv(override=True)
set_default_openai_api(os.getenv("OPENAI_API_KEY"))

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={
            "command": "codex",
            "args": ["mcp-server"],
        },
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:
        developer_agent = Agent(
            name="Game Developer",
            instructions=(
                "You are an expert in building simple games using basic html + css + javascript with no dependencies. "
                "Save your work in a file called index.html in the current directory. "
                "Always call codex with \"approval-policy\": \"never\" and \"sandbox\": \"workspace-write\"."
            ),
            mcp_servers=[codex_mcp_server],
        )

        designer_agent = Agent(
            name="Game Designer",
            instructions=(
                "You are an indie game connoisseur. Come up with an idea for a single page html + css + javascript game that a developer could build in about 50 lines of code. "
                "Format your request as a 3 sentence design brief for a game developer and call the Game Developer coder with your idea."
            ),
            model="gpt-5",
            handoffs=[developer_agent],
        )

        await Runner.run(designer_agent, "Implement a fun new game!")

if __name__ == "__main__":
    asyncio.run(main())
```

执行脚本：

```bash
python codex_mcp.py
```

Codex 会阅读设计师的简报，创建 `index.html` 文件，并将完整的游戏写入磁盘。在浏览器中打开生成的文件，即可游玩。每次运行都会生成不同的设计，带来独特的玩法变化和精心打磨的细节。

## 扩展为多智能体工作流程

现在，将单智能体配置扩展为经过编排且可追踪的工作流程。系统会新增以下角色：

- **项目经理**：制定共享需求、协调移交，并强制执行防护规则。
- **设计师**、 **前端开发者**、 **服务端开发者**和 **测试人员**：每个角色都有范围明确的指令和各自的输出文件夹。

新建名为 `multi_agent_workflow.py` 的文件：

```python

from dotenv import load_dotenv

from agents import (
    Agent,
    ModelSettings,
    Runner,
    WebSearchTool,
    set_default_openai_api,
)
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from agents.mcp import MCPServerStdio
from openai.types.shared import Reasoning

load_dotenv(override=True)
set_default_openai_api(os.getenv("OPENAI_API_KEY"))

async def main() -> None:
    async with MCPServerStdio(
        name="Codex CLI",
        params={"command": "codex", "args": ["mcp-server"]},
        client_session_timeout_seconds=360000,
    ) as codex_mcp_server:
        designer_agent = Agent(
            name="Designer",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Designer.\n"
                "Your only source of truth is AGENT_TASKS.md and REQUIREMENTS.md from the Project Manager.\n"
                "Do not assume anything that is not written there.\n\n"
                "You may use the internet for additional guidance or research."
                "Deliverables (write to /design):\n"
                "- design_spec.md – a single page describing the UI/UX layout, main screens, and key visual notes as requested in AGENT_TASKS.md.\n"
                "- wireframe.md – a simple text or ASCII wireframe if specified.\n\n"
                "Keep the output short and implementation-friendly.\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            tools=[WebSearchTool()],
            mcp_servers=[codex_mcp_server],
        )

        frontend_developer_agent = Agent(
            name="Frontend Developer",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Frontend Developer.\n"
                "Read AGENT_TASKS.md and design_spec.md. Implement exactly what is described there.\n\n"
                "Deliverables (write to /frontend):\n"
                "- index.html – main page structure\n"
                "- styles.css or inline styles if specified\n"
                "- main.js or game.js if specified\n\n"
                "Follow the Designer’s DOM structure and any integration points given by the Project Manager.\n"
                "Do not add features or branding beyond the provided documents.\n\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager_agent."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            mcp_servers=[codex_mcp_server],
        )

        backend_developer_agent = Agent(
            name="Backend Developer",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Backend Developer.\n"
                "Read AGENT_TASKS.md and REQUIREMENTS.md. Implement the backend endpoints described there.\n\n"
                "Deliverables (write to /backend):\n"
                "- package.json – include a start script if requested\n"
                "- server.js – implement the API endpoints and logic exactly as specified\n\n"
                "Keep the code as simple and readable as possible. No external database.\n\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager_agent."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            mcp_servers=[codex_mcp_server],
        )

        tester_agent = Agent(
            name="Tester",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                "You are the Tester.\n"
                "Read AGENT_TASKS.md and TEST.md. Verify that the outputs of the other roles meet the acceptance criteria.\n\n"
                "Deliverables (write to /tests):\n"
                "- TEST_PLAN.md – bullet list of manual checks or automated steps as requested\n"
                "- test.sh or a simple automated script if specified\n\n"
                "Keep it minimal and easy to run.\n\n"
                "When complete, handoff to the Project Manager with transfer_to_project_manager."
                "When creating files, call Codex MCP with {\"approval-policy\":\"never\",\"sandbox\":\"workspace-write\"}."
            ),
            model="gpt-5",
            mcp_servers=[codex_mcp_server],
        )

        project_manager_agent = Agent(
            name="Project Manager",
            instructions=(
                f"""{RECOMMENDED_PROMPT_PREFIX}"""
                """
                You are the Project Manager.

                Objective:
                Convert the input task list into three project-root files the team will execute against.

                Deliverables (write in project root):
                - REQUIREMENTS.md: concise summary of product goals, target users, key features, and constraints.
                - TEST.md: tasks with [Owner] tags (Designer, Frontend, Backend, Tester) and clear acceptance criteria.
                - AGENT_TASKS.md: one section per role containing:
                  - Project name
                  - Required deliverables (exact file names and purpose)
                  - Key technical notes and constraints

                Process:
                - Resolve ambiguities with minimal, reasonable assumptions. Be specific so each role can act without guessing.
                - Create files using Codex MCP with {"approval-policy":"never","sandbox":"workspace-write"}.
                - Do not create folders. Only create REQUIREMENTS.md, TEST.md, AGENT_TASKS.md.

                Handoffs (gated by required files):
                1) After the three files above are created, hand off to the Designer with transfer_to_designer_agent and include REQUIREMENTS.md and AGENT_TASKS.md.
                2) Wait for the Designer to produce /design/design_spec.md. Verify that file exists before proceeding.
                3) When design_spec.md exists, hand off in parallel to both:
                   - Frontend Developer with transfer_to_frontend_developer_agent (provide design_spec.md, REQUIREMENTS.md, AGENT_TASKS.md).
                   - Backend Developer with transfer_to_backend_developer_agent (provide REQUIREMENTS.md, AGENT_TASKS.md).
                4) Wait for Frontend to produce /frontend/index.html and Backend to produce /backend/server.js. Verify both files exist.
                5) When both exist, hand off to the Tester with transfer_to_tester_agent and provide all prior artifacts and outputs.
                6) Do not advance to the next handoff until the required files for that step are present. If something is missing, request the owning agent to supply it and re-check.

                PM Responsibilities:
                - Coordinate all roles, track file completion, and enforce the above gating checks.
                - Do NOT respond with status updates. Just handoff to the next agent until the project is complete.
                """
            ),
            model="gpt-5",
            model_settings=ModelSettings(
                reasoning=Reasoning(effort="medium"),
            ),
            handoffs=[designer_agent, frontend_developer_agent, backend_developer_agent, tester_agent],
            mcp_servers=[codex_mcp_server],
        )

        designer_agent.handoffs = [project_manager_agent]
        frontend_developer_agent.handoffs = [project_manager_agent]
        backend_developer_agent.handoffs = [project_manager_agent]
        tester_agent.handoffs = [project_manager_agent]

        task_list = """
Goal: Build a tiny browser game to showcase a multi-agent workflow.

High-level requirements:
- Single-screen game called "Bug Busters".
- Player clicks a moving bug to earn points.
- Game ends after 20 seconds and shows final score.
- Optional: submit score to a simple backend and display a top-10 leaderboard.

Roles:
- Designer: create a one-page UI/UX spec and basic wireframe.
- Frontend Developer: implement the page and game logic.
- Backend Developer: implement a minimal API (GET /health, GET/POST /scores).
- Tester: write a quick test plan and a simple script to verify core routes.

Constraints:
- No external database—memory storage is fine.
- Keep everything readable for beginners; no frameworks required.
- All outputs should be small files saved in clearly named folders.
"""

        result = await Runner.run(project_manager_agent, task_list, max_turns=30)
        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
```

运行脚本并查看生成的文件：

```bash
python multi_agent_workflow.py
ls -R
```

项目经理智能体会编写 `REQUIREMENTS.md`、`TEST.md` 和 `AGENT_TASKS.md`，然后协调设计师、前端开发者、服务端开发者和测试人员智能体之间的移交。每个智能体都会先在自己的文件夹中写入职责范围内的产物，再将控制权交还给项目经理。

## 追踪工作流程

Codex 会自动生成追踪记录，涵盖每条提示、每次工具调用和每次移交。多智能体运行完成后，请打开[追踪仪表板](https://platform.openai.com/trace)，查看执行时间线。

追踪概览会重点展示项目经理如何在继续推进之前验证移交。点击具体步骤，即可查看提示、Codex MCP 调用、写入的文件和执行时长。这些详细信息让您能够轻松审查每次移交，并了解工作流程如何逐轮演进。
通过这些追踪记录，您无需额外插桩，即可轻松排查工作流程中的问题、审查智能体行为，并衡量性能随时间的变化。
