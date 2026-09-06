<!-- source: https://learn.chatgpt.com/de-DE/docs/mcp-server -->

# Codex als MCP-Server ausführen

  `codex mcp-server` ist veraltet. Verwende stattdessen den [Codex
  App Server](/de-DE/codex/app-server). Um Codex aus Claude Code aufzurufen, verwende das
[Codex-Plug-in für Claude Code](https://github.com/openai/codex-plugin-cc),
  das den App Server nutzt. Diese Seite dokumentiert den veralteten Befehl für
  bestehende Integrationen.

Du kannst Codex als MCP-Server ausführen und von anderen MCP-Clients aus eine Verbindung dazu herstellen (zum Beispiel von einem Agenten, der mit der [MCP-Integration des OpenAI Agents SDK](/api/docs/guides/agents/integrations-observability#mcp) entwickelt wurde).

Um Codex als MCP-Server zu starten, kannst du folgenden Befehl verwenden:

```bash
codex mcp-server
```

Einen Codex-MCP-Server kannst du mit dem [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) starten:

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

Sende eine Anfrage vom Typ `tools/list`, um zwei Tools anzuzeigen:

**`codex`**: Führe eine Codex-Sitzung mit dem folgenden Prompt aus und überschreibe dabei die Konfiguration mit den folgenden Einstellungen:

| Eigenschaft                 | Typ     | Beschreibung                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (erforderlich)  | `string` | Der erste Prompt, mit dem du die Codex-Konversation startest.                                                 |
| `approval-policy`        | `string` | Genehmigungsrichtlinie für vom Modell generierte Shell-Befehle: `untrusted`, `on-request` und `never`.       |
| `base-instructions`      | `string` | Die Anweisungen, die anstelle der Standardanweisungen verwendet werden.                                              |
| `compact-prompt`         | `string` | Prompt für die Compaction (Kontextverdichtung) der Konversation.                                                            |
| `config`                 | `object` | Einzelne Konfigurationseinstellungen, die die Werte in `$CODEX_HOME/config.toml` überschreiben.                     |
| `cwd`                    | `string` | Arbeitsverzeichnis für die Sitzung. Relative Pfade werden ausgehend vom aktuellen Verzeichnis des Serverprozesses aufgelöst. |
| `developer-instructions` | `string` | Entwickleranweisungen, die als Nachricht der Entwicklerrolle eingefügt werden.                                             |
| `model`                  | `string` | Optionale Überschreibung des Modellnamens (zum Beispiel `gpt-5.6-terra`).                                     |
| `sandbox`                | `string` | Sandbox-Modus: `read-only`, `workspace-write` oder `danger-full-access`.                                   |

**`codex-reply`**: Setze eine Codex-Sitzung fort, indem du die Thread-ID und einen Prompt angibst. Das Tool `codex-reply` akzeptiert folgende Eigenschaften:

| Eigenschaft                      | Typ   | Beschreibung                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (erforderlich)       | string | Der nächste Prompt, mit dem du die Codex-Konversation fortsetzt.  |
| **`threadId`** (erforderlich)     | string | Die ID des Threads, der fortgesetzt werden soll.                         |
| `conversationId` (veraltet) | string | Veralteter Alias für `threadId` (aus Kompatibilitätsgründen beibehalten). |

Verwende die `threadId` aus `structuredContent.threadId` in der Antwort auf `tools/call`. Genehmigungsanfragen (exec/patch) enthalten außerdem `threadId` in ihrer `params`-Payload.

Beispiel für eine Antwort-Payload:

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

Beachte, dass moderne MCP-Clients als Ergebnis eines Tool-Aufrufs in der Regel nur `"structuredContent"` ausgeben, sofern vorhanden. Der Codex-MCP-Server gibt für ältere MCP-Clients jedoch auch `"content"` zurück.

# Arbeitsabläufe mit mehreren Agenten erstellen

Codex CLI kann weit mehr als Ad-hoc-Aufgaben ausführen. Wenn du die CLI als Server für das [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) bereitstellst und mit dem OpenAI Agents SDK orchestrierst, kannst du deterministische, überprüfbare Arbeitsabläufe erstellen. Diese lassen sich von einem einzelnen Agenten bis zu einer vollständigen Pipeline für die Softwarebereitstellung skalieren.

Diese Anleitung führt dich durch denselben Ablauf, der im [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb) vorgestellt wird. Du wirst:

- Codex CLI als über längere Zeit laufenden MCP-Server starten,
- einen klar abgegrenzten Ablauf mit einem einzelnen Agenten erstellen, der ein spielbares Browserspiel erzeugt, und
- ein Team aus mehreren Agenten mit Übergaben, Schutzmechanismen und vollständigen Traces orchestrieren, die du anschließend überprüfen kannst.

Prüfe vor dem Start, ob die folgenden Voraussetzungen erfüllt sind:

- Eine lokale Installation von [Codex CLI](/de-DE/codex/cli), sodass der Befehl `codex` verfügbar ist.
- Python 3.10+ mit `pip`.
- Node.js 18+, wenn du das obige Beispiel für den MCP Inspector ausführen möchtest.
- Ein lokal gespeicherter OpenAI-API-Schlüssel. Im [OpenAI-Dashboard](https://platform.openai.com/account/api-keys) kannst du Schlüssel erstellen oder verwalten.

Erstelle ein Arbeitsverzeichnis für diese Anleitung und trage deinen API-Schlüssel in eine `.env`-Datei ein:

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## Abhängigkeiten installieren

Das Agents SDK übernimmt die Orchestrierung von Codex einschließlich Übergaben und Traces. Installiere die neuesten SDK-Pakete:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  Wenn du eine virtuelle Umgebung aktivierst, bleiben die SDK-Abhängigkeiten vom
Rest deines Systems getrennt.

## Codex CLI als MCP-Server initialisieren

Richte Codex CLI zunächst als MCP-Server ein, den das Agents SDK aufrufen kann. Der Server stellt zwei Tools bereit (`codex()` zum Starten einer Konversation und `codex-reply()` zum Fortsetzen) und hält Codex über mehrere Interaktionen der Agenten hinweg aktiv.

Erstelle eine Datei namens `codex_mcp.py` und füge Folgendes ein:

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

Führe das Skript einmal aus, um zu prüfen, ob Codex erfolgreich startet:

```bash
python codex_mcp.py
```

Das Skript gibt `Codex MCP server started.` aus und wird anschließend beendet. In den nächsten Abschnitten verwendest du denselben MCP-Server in umfangreicheren Arbeitsabläufen erneut.

## Ablauf mit einem einzelnen Agenten erstellen

Beginnen wir mit einem klar abgegrenzten Beispiel: Mit Codex MCP erstellen wir ein kleines Browserspiel. Der Ablauf nutzt zwei Agenten:

1. **Game Designer**: schreibt ein Briefing für das Spiel.
2. **Game Developer**: ruft Codex MCP auf, um das Spiel zu implementieren.

Aktualisiere `codex_mcp.py` mit dem folgenden Code. Der Code übernimmt das obige Setup des MCP-Servers und fügt beide Agenten hinzu.

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

Führe das Skript aus:

```bash
python codex_mcp.py
```

Codex liest das Briefing des Designer-Agenten, erstellt eine Datei namens `index.html` und speichert das vollständige Spiel auf der Festplatte. Öffne die erzeugte Datei in einem Browser, um das Ergebnis zu spielen. Jeder Durchlauf liefert ein anderes Design mit eigenen spielerischen Besonderheiten und ausgefeilten Details.

## Zu einem Ablauf mit mehreren Agenten erweitern

Erweitere das Setup mit einem einzelnen Agenten nun zu einem orchestrierten, nachvollziehbaren Ablauf. Das System wird dazu um Folgendes ergänzt:

- **Project Manager**: definiert gemeinsame Anforderungen, koordiniert Übergaben und stellt die Einhaltung von Schutzvorgaben sicher.
- **Designer**, **Frontend Developer**, **Server Developer** und **Tester**: jeweils mit klar abgegrenzten Anweisungen und eigenen Ausgabeordnern.

Erstelle eine neue Datei mit dem Namen `multi_agent_workflow.py`:

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

Führe das Skript aus und sieh dir die erzeugten Dateien an:

```bash
python multi_agent_workflow.py
ls -R
```

Der als Project Manager eingesetzte Agent schreibt `REQUIREMENTS.md`, `TEST.md` und `AGENT_TASKS.md` und koordiniert anschließend die Übergaben zwischen den Agenten für Design, Frontend, Server und Tests. Jeder Agent schreibt die Artefakte für seinen Aufgabenbereich in seinen eigenen Ordner, bevor er die Kontrolle an den Project Manager zurückgibt.

## Den Ablauf nachverfolgen

Codex zeichnet automatisch Traces auf, die jeden Prompt, jeden Tool-Aufruf und jede Übergabe erfassen. Öffne nach Abschluss des Durchlaufs mit mehreren Agenten das [Traces-Dashboard](https://platform.openai.com/trace), um den zeitlichen Ablauf der Ausführung zu prüfen.

Die Trace-Übersicht zeigt, wie der Project Manager Übergaben prüft, bevor er fortfährt. Klicke auf einzelne Schritte, um Prompts, Codex-MCP-Aufrufe, geschriebene Dateien und die jeweilige Ausführungsdauer anzuzeigen. Anhand dieser Details kannst du jede Übergabe leicht überprüfen und nachvollziehen, wie sich der Ablauf von Runde zu Runde entwickelt hat.
Mit diesen Traces kannst du Probleme im Ablauf einfach debuggen, das Verhalten der Agenten überprüfen und die Leistung im Zeitverlauf messen, ohne zusätzliche Instrumentierung einrichten zu müssen.
