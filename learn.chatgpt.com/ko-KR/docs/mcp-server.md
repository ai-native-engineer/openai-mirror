<!-- source: https://learn.chatgpt.com/ko-KR/docs/mcp-server -->

# Codex를 MCP 서버로 실행하기

  `codex mcp-server`는 사용 중단 예정(deprecated)입니다. 대신 [Codex
  App Server](/ko-KR/codex/app-server)를 사용하세요. Claude Code에서 Codex를 호출하려면
[Claude Code용 Codex 플러그인](https://github.com/openai/codex-plugin-cc)을 사용하세요.
  이 플러그인은 App Server를 사용합니다. 이 페이지에서는
  기존 통합에 사용되는 사용 중단 예정(deprecated) 명령어를 설명합니다.

Codex를 MCP 서버로 실행하고 다른 MCP 클라이언트(예: [OpenAI Agents SDK MCP 통합](/api/docs/guides/agents/integrations-observability#mcp)으로 만든 에이전트)에서 연결할 수 있습니다.

Codex를 MCP 서버로 시작하려면 다음 명령어를 사용할 수 있습니다:

```bash
codex mcp-server
```

[Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector)로 Codex MCP 서버를 시작할 수 있습니다:

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

`tools/list` 요청을 보내면 다음 두 도구를 확인할 수 있습니다:

**`codex`**: 다음 프롬프트와 구성 재정의 값을 사용해 Codex 세션을 실행합니다:

| 속성                 | 유형     | 설명                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (필수)  | `string` | Codex 대화를 시작하는 첫 사용자 프롬프트입니다.                                                 |
| `approval-policy`        | `string` | 모델이 생성한 셸 명령어에 적용할 승인 정책: `untrusted`, `on-request`, `never`.       |
| `base-instructions`      | `string` | 기본 지침 대신 사용할 지침 모음입니다.                                              |
| `compact-prompt`         | `string` | 대화의 컨텍스트를 압축할 때 사용하는 프롬프트입니다.                                                            |
| `config`                 | `object` | `$CODEX_HOME/config.toml`에 정의된 값을 재정의하는 개별 구성 설정입니다.                     |
| `cwd`                    | `string` | 세션의 작업 디렉터리입니다. 상대 경로는 서버 프로세스의 현재 디렉터리를 기준으로 해석됩니다. |
| `developer-instructions` | `string` | 개발자 역할 메시지로 삽입되는 개발자 지침입니다.                                             |
| `model`                  | `string` | 모델 이름을 재정의하는 선택적 설정입니다(예: `gpt-5.6-terra`).                                     |
| `sandbox`                | `string` | 샌드박스 모드: `read-only`, `workspace-write` 또는 `danger-full-access`.                                   |

**`codex-reply`**: 스레드 ID와 프롬프트를 제공하여 Codex 세션을 이어갑니다. `codex-reply` 도구는 다음 속성을 받습니다:

| 속성                      | 유형   | 설명                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (필수)       | 문자열 | Codex 대화를 이어가기 위한 다음 사용자 프롬프트입니다.  |
| **`threadId`** (필수)     | 문자열 | 이어갈 스레드의 ID입니다.                         |
| `conversationId` (사용 중단 예정(deprecated)) | 문자열 | `threadId`의 별칭으로, 사용 중단 예정(deprecated)이지만 호환성을 위해 유지됩니다. |

`tools/call` 응답의 `structuredContent.threadId`에서 `threadId`를 가져와 사용하세요. 승인 프롬프트(exec/patch)의 `params` 페이로드에도 `threadId`가 포함됩니다.

응답 페이로드 예시:

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

최신 MCP 클라이언트는 `"structuredContent"`가 있으면 일반적으로 이 항목만 도구 호출 결과로 보고합니다. Codex MCP 서버는 이전 MCP 클라이언트와의 호환성을 위해 `"content"`도 반환합니다.

# 다중 에이전트 워크플로우 만들기

Codex CLI는 단발성 작업 실행 외에도 훨씬 다양한 일을 할 수 있습니다. CLI를 [Model Context Protocol](https://modelcontextprotocol.io/)(MCP) 서버로 제공하고 OpenAI Agents SDK로 오케스트레이션하면, 단일 에이전트부터 전체 소프트웨어 제공 파이프라인까지 확장할 수 있는 결정론적이고 검토 가능한 워크플로우를 만들 수 있습니다.

이 가이드에서는 [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb)에 소개된 것과 동일한 워크플로우를 살펴봅니다. 다음을 수행합니다:

- Codex CLI를 장시간 실행되는 MCP 서버로 시작합니다.
- 실제로 플레이할 수 있는 브라우저 게임 제작에 초점을 맞춘 단일 에이전트 워크플로우를 구축합니다.
- 핸드오프와 가드레일을 적용하고 나중에 검토할 수 있는 전체 트레이스를 남기는 다중 에이전트 팀을 오케스트레이션합니다.

시작하기 전에 다음 사항을 준비하세요:

- 로컬에 [Codex CLI](/ko-KR/codex/cli)를 설치하여 `codex` 명령어를 사용할 수 있어야 합니다.
- `pip`이 설치된 Python 3.10 이상이 필요합니다.
- 위의 MCP Inspector 예시를 실행하려면 Node.js 18 이상이 필요합니다.
- 로컬에 저장된 OpenAI API 키가 필요합니다. [OpenAI 대시보드](https://platform.openai.com/account/api-keys)에서 키를 만들거나 관리할 수 있습니다.

이 가이드용 작업 디렉터리를 만들고 API 키를 `.env` 파일에 추가하세요:

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## 종속성 설치하기

Agents SDK는 Codex 오케스트레이션, 핸드오프, 트레이스를 처리합니다. 최신 SDK 패키지를 설치하세요:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  가상 환경을 활성화하면 SDK 종속성이
시스템의 나머지 부분과 분리됩니다.

## Codex CLI를 MCP 서버로 초기화하기

먼저 Agents SDK가 호출할 수 있도록 Codex CLI를 MCP 서버로 설정하세요. 서버는 대화를 시작하는 `codex()`와 대화를 이어가는 `codex-reply()`라는 두 도구를 제공하고, 에이전트가 여러 턴을 진행하는 동안 Codex를 실행 상태로 유지합니다.

`codex_mcp.py` 파일을 만들고 다음 내용을 추가하세요:

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

스크립트를 한 번 실행하여 Codex가 정상적으로 시작되는지 확인하세요:

```bash
python codex_mcp.py
```

스크립트는 `Codex MCP server started.` 메시지를 출력한 후 종료됩니다. 다음 섹션에서는 더 정교한 워크플로우에서 같은 MCP 서버를 재사용합니다.

## 단일 에이전트 워크플로우 구축하기

범위를 좁혀 Codex MCP로 작은 브라우저 게임을 완성하는 예시부터 살펴보겠습니다. 이 워크플로우는 두 에이전트를 사용합니다:

1. **게임 디자이너**: 게임 기획서를 작성합니다.
2. **게임 개발자**: Codex MCP를 호출해 게임을 구현합니다.

다음 코드로 `codex_mcp.py` 파일을 업데이트하세요. 위의 MCP 서버 설정을 유지하면서 두 에이전트를 모두 추가하는 코드입니다.

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

스크립트를 실행하세요:

```bash
python codex_mcp.py
```

Codex는 디자이너의 기획서를 읽고 `index.html` 파일을 생성한 뒤 게임 전체를 디스크에 저장합니다. 생성된 파일을 브라우저에서 열어 게임을 플레이하세요. 실행할 때마다 플레이 방식에 독특한 변화를 더하고 세부 요소까지 다듬은 새로운 디자인이 만들어집니다.

## 멀티 에이전트 워크플로우로 확장

이제 단일 에이전트 구성을 에이전트 간 작업을 조율하고 실행 과정을 추적할 수 있는 워크플로우로 확장하세요. 다음 역할이 추가됩니다:

- **프로젝트 관리자**: 공통 요구 사항을 작성하고 핸드오프를 조율하며 가드레일을 적용합니다.
- **디자이너**, **프런트엔드 개발자**, **서버 개발자**, **테스터**: 각 역할에는 작업 범위를 정한 지침과 출력 폴더가 있습니다.

`multi_agent_workflow.py`라는 새 파일을 만드세요:

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

스크립트를 실행하고 생성되는 파일을 확인하세요:

```bash
python multi_agent_workflow.py
ls -R
```

프로젝트 관리자 에이전트는 `REQUIREMENTS.md`, `TEST.md`, `AGENT_TASKS.md`를 작성한 다음 디자이너, 프런트엔드, 서버, 테스터 에이전트 간의 핸드오프를 조율합니다. 각 에이전트는 자신의 폴더에 담당 범위의 산출물을 작성한 후 프로젝트 관리자에게 제어권을 돌려줍니다.

## 워크플로우 추적

Codex는 모든 프롬프트, 도구 호출, 핸드오프가 담긴 트레이스를 자동으로 기록합니다. 멀티 에이전트 실행이 완료되면 [트레이스 대시보드](https://platform.openai.com/trace)를 열어 실행 타임라인을 확인하세요.

트레이스 개요를 보면 프로젝트 관리자가 다음 단계로 진행하기 전에 핸드오프를 어떻게 검증하는지 알 수 있습니다. 개별 단계를 클릭하면 프롬프트, Codex MCP 호출, 작성된 파일, 실행 시간을 확인할 수 있습니다. 이 세부 정보를 통해 모든 핸드오프를 쉽게 감사하고 턴마다 워크플로우가 어떻게 전개되었는지 파악할 수 있습니다.
이러한 트레이스를 활용하면 추가 계측 없이도 워크플로우의 문제를 쉽게 디버깅하고, 에이전트 동작을 감사하며, 시간에 따른 성능을 측정할 수 있습니다.
