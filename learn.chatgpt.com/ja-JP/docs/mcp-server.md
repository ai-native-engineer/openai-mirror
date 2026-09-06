<!-- source: https://learn.chatgpt.com/ja-JP/docs/mcp-server -->

# Codex を MCP サーバーとして実行

  `codex mcp-server` は非推奨です。代わりに [Codex
  App Server](/ja-JP/codex/app-server) を使用してください。Claude Code から Codex を呼び出すには、
[Claude Code 用 Codex プラグイン](https://github.com/openai/codex-plugin-cc)を使用してください。
  このプラグインは App Server を使用します。このページでは、
  既存の連携向けに非推奨のコマンドを説明します。

Codex を MCP サーバーとして実行し、ほかの MCP クライアントから接続できます（たとえば、[OpenAI Agents SDK の MCP 連携](/api/docs/guides/agents/integrations-observability#mcp)を使って構築したエージェントなど）。

Codex を MCP サーバーとして起動するには、次のコマンドを使用します：

```bash
codex mcp-server
```

[Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) を使って Codex MCP サーバーを起動できます：

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

`tools/list` リクエストを送信すると、次の 2 つのツールを確認できます：

**`codex`**：次のプロンプトと構成の上書き設定を指定して、Codex セッションを実行します：

| プロパティ                 | 型     | 説明                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** （必須）  | `string` | Codex との会話を開始するための最初のユーザープロンプトです。                                                 |
| `approval-policy`        | `string` | モデルが生成したシェルコマンドに対する承認ポリシーです。`untrusted`、`on-request`、`never` を指定できます。       |
| `base-instructions`      | `string` | デフォルトの指示の代わりに使用する一連の指示です。                                              |
| `compact-prompt`         | `string` | 会話のコンパクション時に使用するプロンプトです。                                                            |
| `config`                 | `object` | `$CODEX_HOME/config.toml` の内容を上書きする個別の構成設定です。                     |
| `cwd`                    | `string` | セッションの作業ディレクトリです。相対パスの場合は、サーバープロセスのカレントディレクトリを基準に解決されます。 |
| `developer-instructions` | `string` | developer ロールのメッセージとして挿入される開発者からの指示です。                                             |
| `model`                  | `string` | モデル名を任意で上書きできます（例：`gpt-5.6-terra`）。                                     |
| `sandbox`                | `string` | サンドボックスモードです。`read-only`、`workspace-write`、または `danger-full-access` を指定できます。                                   |

**`codex-reply`**：スレッド ID とプロンプトを指定して Codex セッションを続行します。`codex-reply` ツールは次のプロパティを受け取ります：

| プロパティ                      | 型   | 説明                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** （必須）       | string | Codex との会話を続行するための次のユーザープロンプトです。  |
| **`threadId`** （必須）     | string | 続行するスレッドの ID です。                         |
| `conversationId` （非推奨） | string | `threadId` の非推奨のエイリアスです（互換性維持のため残されています）。 |

`tools/call` レスポンスの `structuredContent.threadId` から `threadId` を取得して使用します。承認プロンプト（exec/patch）の `params` ペイロードにも `threadId` が含まれます。

レスポンスペイロードの例：

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

なお、現在の MCP クライアントでは通常、ツール呼び出しの結果に `"structuredContent"` があれば、それだけが報告されます。ただし、Codex MCP サーバーは古い MCP クライアント向けに `"content"` も返します。

# マルチエージェントワークフローの作成

Codex CLI の用途は、単発のタスク実行だけではありません。CLI を [Model Context Protocol](https://modelcontextprotocol.io/)（MCP）サーバーとして公開し、OpenAI Agents SDK でオーケストレーションすることで、単一のエージェントからソフトウェアデリバリーパイプライン全体にまで拡張できる、決定論的でレビュー可能なワークフローを作成できます。

このガイドでは、[OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb) で紹介されているものと同じワークフローを解説します。具体的には、次のことを行います：

- Codex CLI を長時間稼働する MCP サーバーとして起動
- 実際に遊べるブラウザゲームを作成する、目的を絞った単一エージェントワークフローを構築
- ハンドオフ、ガードレール、後からレビューできる完全なトレースを備えたマルチエージェントチームをオーケストレーション

開始する前に、次のものを用意してください：

- ローカルにインストール済みの [Codex CLI](/ja-JP/codex/cli)（`codex` コマンドが利用できること）
- Python 3.10 以降と `pip`
- 上記の MCP Inspector の例を実行する場合は Node.js 18 以降
- ローカルに保存した OpenAI API キー（[OpenAI ダッシュボード](https://platform.openai.com/account/api-keys)で作成・管理できます）

このガイド用の作業ディレクトリを作成し、API キーを `.env` ファイルに追加します：

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## 依存関係のインストール

Agents SDK は、Codex のオーケストレーション、ハンドオフ、トレースを管理します。最新の SDK パッケージをインストールします：

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  仮想環境を有効にすると、SDK の依存関係をシステムのほかの部分から分離できます。

## Codex CLI を MCP サーバーとして初期化

まず、Codex CLI を Agents SDK から呼び出せる MCP サーバーとして設定します。サーバーは、会話を開始する `codex()` と続行する `codex-reply()` の 2 つのツールを公開し、エージェントの複数のターンにわたって Codex を稼働状態に保ちます。

`codex_mcp.py` という名前のファイルを作成し、次の内容を追加します：

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

スクリプトを一度実行し、Codex が正常に起動することを確認します：

```bash
python codex_mcp.py
```

スクリプトは `Codex MCP server started.` を出力した後、終了します。以降のセクションでは、同じ MCP サーバーをより高度なワークフローで再利用します。

## 単一エージェントワークフローの構築

まずは対象を絞り、Codex MCP で小規模なブラウザゲームを完成させる例を見ていきます。このワークフローでは、2 つのエージェントを使用します：

1. **ゲームデザイナー**：ゲームの概要書を作成します。
2. **ゲーム開発者**：Codex MCP を呼び出してゲームを実装します。

`codex_mcp.py` を次のコードで更新します。このコードは上記の MCP サーバーの設定を維持し、2 つのエージェントを追加します。

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

スクリプトを実行します：

```bash
python codex_mcp.py
```

Codex はデザイナーの企画概要を読み、`index.html` ファイルを作成して、ゲーム全体をディスクに書き込みます。生成されたファイルをブラウザで開くと、ゲームをプレイできます。実行するたびに、遊び方や細部の仕上げに独自の工夫が凝らされた、異なるデザインのゲームが生成されます。

## マルチエージェントワークフローへの拡張

次に、シングルエージェント構成を、複数のエージェントが連携し、実行をトレースできるワークフローへ拡張します。システムに次のエージェントを追加します：

- **プロジェクトマネージャー**：共通要件の作成、ハンドオフの調整、ガードレールの適用
- **デザイナー**、 **フロントエンド開発者**、 **サーバー開発者**、 **テスター**：それぞれに担当範囲に応じた指示と出力フォルダーを設定

新しいファイル `multi_agent_workflow.py` を作成します：

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

スクリプトを実行し、生成されるファイルを確認します：

```bash
python multi_agent_workflow.py
ls -R
```

プロジェクトマネージャーエージェントは `REQUIREMENTS.md`、`TEST.md`、`AGENT_TASKS.md` を作成した後、デザイナー、フロントエンド開発者、サーバー開発者、テスターの各エージェント間のハンドオフを調整します。各エージェントは、それぞれのフォルダーに担当範囲の成果物を書き込んでから、プロジェクトマネージャーに制御を戻します。

## ワークフローのトレース

Codex は、すべてのプロンプト、ツール呼び出し、ハンドオフを含むトレースを自動的に記録します。マルチエージェントでの実行が完了したら、[トレースダッシュボード](https://platform.openai.com/trace)を開いて、実行タイムラインを確認します。

全体のトレースを見ると、プロジェクトマネージャーが次に進む前にハンドオフをどう検証しているかがわかります。各ステップをクリックすると、プロンプト、Codex MCP の呼び出し、書き込まれたファイル、実行時間を確認できます。こうした詳細情報により、すべてのハンドオフを簡単に監査し、ワークフローがターンごとにどう進んだかを把握できます。
これらのトレースがあれば、計測処理を追加しなくても、ワークフローで生じた問題のデバッグ、エージェントの動作の監査、パフォーマンスの継続的な測定を簡単に行えます。
