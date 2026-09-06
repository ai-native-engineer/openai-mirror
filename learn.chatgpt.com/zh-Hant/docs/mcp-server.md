<!-- source: https://learn.chatgpt.com/zh-Hant/docs/mcp-server -->

# 將 Codex 作為 MCP 伺服器執行

  `codex mcp-server` 已棄用。請改用 [Codex App
  Server](/zh-Hant/codex/app-server)。若要從 Claude Code 呼叫 Codex，請使用
[適用於 Claude Code 的 Codex 外掛程式](https://github.com/openai/codex-plugin-cc)，
  該外掛程式使用 App Server。本頁說明此已棄用指令，供
  現有整合參考。

您可以將 Codex 作為 MCP 伺服器執行，並從其他 MCP 用戶端連線至該伺服器（例如，使用 [OpenAI Agents SDK 的 MCP 整合功能](/api/docs/guides/agents/integrations-observability#mcp)建構的智慧體）。

若要將 Codex 作為 MCP 伺服器啟動，可使用下列指令：

```bash
codex mcp-server
```

您可以使用 [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) 啟動 Codex MCP 伺服器：

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

傳送 `tools/list` 要求，即可查看兩項工具：

**`codex`**：使用下列提示詞與組態覆寫值執行 Codex 工作階段：

| 屬性                 | 型別     | 說明                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** （必填）  | `string` | 用來開始 Codex 對話的初始使用者提示詞。                                                 |
| `approval-policy`        | `string` | 用於模型產生之 Shell 指令的核准政策：`untrusted`、`on-request` 和 `never`。       |
| `base-instructions`      | `string` | 用來取代預設指示的一組指示。                                              |
| `compact-prompt`         | `string` | 壓縮對話時使用的提示詞。                                                            |
| `config`                 | `object` | 用來覆寫 `$CODEX_HOME/config.toml` 中對應值的個別組態設定。                     |
| `cwd`                    | `string` | 工作階段的工作目錄。若為相對路徑，則以伺服器處理程序的目前目錄為基準進行解析。 |
| `developer-instructions` | `string` | 以開發人員角色訊息形式注入的開發人員指示。                                             |
| `model`                  | `string` | 模型名稱的選用覆寫值（例如 `gpt-5.6-terra`）。                                     |
| `sandbox`                | `string` | 沙盒模式：`read-only`、`workspace-write` 或 `danger-full-access`。                                   |

**`codex-reply`**：提供執行緒 ID 與提示詞，以繼續 Codex 工作階段。`codex-reply` 工具接受下列屬性：

| 屬性                      | 型別   | 說明                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** （必填）       | 字串 | 用來繼續 Codex 對話的下一個使用者提示詞。  |
| **`threadId`** （必填）     | 字串 | 要繼續的執行緒 ID。                         |
| `conversationId`（已棄用） | 字串 | `threadId` 的已棄用別名（為維持相容性而保留）。 |

請使用 `tools/call` 回應中由 `structuredContent.threadId` 提供的 `threadId`。核准提示（exec/patch）的 `params` 承載資料中也包含 `threadId`。

回應承載資料範例：

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

請注意，若回應中有 `"structuredContent"`，新式 MCP 用戶端通常只會將其回報為工具呼叫的結果；不過，Codex MCP 伺服器也會回傳 `"content"`，以支援較舊的 MCP 用戶端。

# 建立多智慧體工作流程

Codex CLI 的功能遠不止執行臨時任務。將 CLI 作為 [模型上下文協定](https://modelcontextprotocol.io/)（MCP）伺服器提供服務，並使用 OpenAI Agents SDK 進行編排，就能建立具確定性且可審查的工作流程，從單一智慧體擴充至完整的軟體交付管線。

本指南會逐步說明 [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb) 中展示的同一套工作流程。您將：

- 將 Codex CLI 啟動為長時間執行的 MCP 伺服器，
- 建構目標明確的單一智慧體工作流程，製作可遊玩的瀏覽器遊戲，以及
- 編排具備交接與防護機制的多智慧體團隊，並保留完整的追蹤記錄供您事後審查。

開始前，請確認已具備：

- 本機已安裝 [Codex CLI](/zh-Hant/codex/cli)，可使用 `codex` 指令。
- Python 3.10 以上版本，並已安裝 `pip`。
- 若要執行上述 MCP Inspector 範例，需有 Node.js 18 以上版本。
- 儲存在本機的 OpenAI API 金鑰。您可以在 [OpenAI 儀表板](https://platform.openai.com/account/api-keys)建立或管理金鑰。

為本指南建立工作目錄，並將 API 金鑰新增至 `.env` 檔案：

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## 安裝相依套件

Agents SDK 負責編排 Codex，並處理交接與追蹤記錄。請安裝最新的 SDK 套件：

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  啟用虛擬環境可讓 SDK 相依套件與
系統的其他部分保持隔離。

## 將 Codex CLI 初始化為 MCP 伺服器

首先，將 Codex CLI 轉換為 Agents SDK 可呼叫的 MCP 伺服器。該伺服器提供兩項工具（`codex()` 用來開始對話，`codex-reply()` 用來繼續對話），並讓 Codex 在智慧體的多輪互動期間持續執行。

建立名為 `codex_mcp.py` 的檔案，並加入下列內容：

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

執行一次指令碼，確認 Codex 能成功啟動：

```bash
python codex_mcp.py
```

指令碼會在印出 `Codex MCP server started.` 後結束。在後續章節中，您將在功能更豐富的工作流程中重複使用同一個 MCP 伺服器。

## 建構單一智慧體工作流程

先從範圍明確的範例開始，使用 Codex MCP 完成一款小型瀏覽器遊戲。這個工作流程仰賴兩個智慧體：

1. **遊戲設計師**：撰寫遊戲設計概要。
2. **遊戲開發人員**：呼叫 Codex MCP 來實作遊戲。

使用下列程式碼更新 `codex_mcp.py`。此程式碼保留上述 MCP 伺服器設定，並加入這兩個智慧體。

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

執行指令碼：

```bash
python codex_mcp.py
```

Codex 會讀取設計師撰寫的遊戲概要，建立 `index.html` 檔案，並將完整遊戲寫入磁碟。在瀏覽器中開啟產生的檔案，即可遊玩。每次執行都會產生不同的設計，各有獨特的玩法巧思與精緻細節。

## 擴充為多智慧體工作流程

接著，將單一智慧體的設定轉換為具備協調機制且可追蹤的工作流程。系統會新增以下角色：

- **專案經理**：建立共用需求、協調交接，並落實防護機制。
- **設計師**、 **前端開發人員**、 **伺服器開發人員**和 **測試人員**：各自有針對其職責範圍的指示與專屬輸出資料夾。

建立名為 `multi_agent_workflow.py` 的新檔案：

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

執行指令碼，並查看產生的檔案：

```bash
python multi_agent_workflow.py
ls -R
```

專案經理智慧體會寫入 `REQUIREMENTS.md`、`TEST.md` 和 `AGENT_TASKS.md`，接著協調設計師、前端開發人員、伺服器開發人員和測試人員智慧體之間的交接。每個智慧體都會將職責範圍內的產出寫入自己的資料夾，再將控制權交回專案經理。

## 追蹤工作流程

Codex 會自動記錄追蹤資料，涵蓋每個提示詞、工具呼叫與交接。多智慧體工作流程執行完成後，開啟[追蹤記錄儀表板](https://platform.openai.com/trace)以檢視執行時間軸。

從追蹤記錄的總覽可清楚看出，專案經理如何在繼續執行前驗證交接。按一下個別步驟，即可查看提示詞、Codex MCP 呼叫、寫入的檔案和執行耗時。這些詳細資料可讓你輕鬆稽核每次交接，並瞭解工作流程如何隨著每輪互動演變。
這些追蹤記錄可讓你輕鬆排除工作流程中的問題、稽核智慧體行為，並持續衡量效能，無須額外加入監測機制。
