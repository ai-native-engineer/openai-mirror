<!-- source: https://learn.chatgpt.com/es-419/docs/mcp-server -->

# Ejecutar Codex como servidor MCP

  `codex mcp-server` está obsoleto. Usa [App Server de
  Codex](/es-419/codex/app-server) en su lugar. Para llamar a Codex desde Claude Code, usa el
[complemento de Codex para Claude Code](https://github.com/openai/codex-plugin-cc),
  que usa App Server. Esta página documenta el comando obsoleto para
  las integraciones existentes.

Puedes ejecutar Codex como servidor MCP y conectarte a él desde otros clientes MCP (por ejemplo, un agente creado con la [integración con MCP de OpenAI Agents SDK](/api/docs/guides/agents/integrations-observability#mcp)).

Para iniciar Codex como servidor MCP, puedes usar el siguiente comando:

```bash
codex mcp-server
```

Puedes iniciar un servidor MCP de Codex con [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector):

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

Envía una solicitud `tools/list` para ver dos herramientas:

**`codex`**: ejecuta una sesión de Codex con el siguiente prompt y los siguientes ajustes que reemplazan la configuración:

| Propiedad                 | Tipo     | Descripción                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (obligatorio)  | `string` | El prompt inicial del usuario para iniciar la conversación de Codex.                                                 |
| `approval-policy`        | `string` | Política de aprobación para los comandos de shell generados por el modelo: `untrusted`, `on-request` y `never`.       |
| `base-instructions`      | `string` | El conjunto de instrucciones que se usará en lugar de las predeterminadas.                                              |
| `compact-prompt`         | `string` | Prompt que se usa al compactar la conversación.                                                            |
| `config`                 | `object` | Ajustes de configuración individuales que reemplazan los definidos en `$CODEX_HOME/config.toml`.                     |
| `cwd`                    | `string` | Directorio de trabajo de la sesión. Si la ruta es relativa, se resuelve con respecto al directorio actual del proceso del servidor. |
| `developer-instructions` | `string` | Instrucciones del desarrollador que se insertan como un mensaje con el rol de desarrollador.                                             |
| `model`                  | `string` | Valor opcional que reemplaza el nombre del modelo (por ejemplo, `gpt-5.6-terra`).                                     |
| `sandbox`                | `string` | Modo de sandbox: `read-only`, `workspace-write` o `danger-full-access`.                                   |

**`codex-reply`**: continúa una sesión de Codex proporcionando el ID del hilo y el prompt. La herramienta `codex-reply` acepta estas propiedades:

| Propiedad                      | Tipo   | Descripción                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (obligatorio)       | string | El siguiente prompt del usuario para continuar la conversación de Codex.  |
| **`threadId`** (obligatorio)     | string | El ID del hilo que se continuará.                         |
| `conversationId` (obsoleto) | string | Alias obsoleto de `threadId` (se conserva por compatibilidad). |

Usa el `threadId` de `structuredContent.threadId` en la respuesta de `tools/call`. Las solicitudes de aprobación (exec/patch) también incluyen `threadId` en su carga útil `params`.

Ejemplo de carga útil de respuesta:

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

Ten en cuenta que, por lo general, los clientes MCP modernos solo reportan `"structuredContent"` como resultado de una llamada a una herramienta, si está presente, aunque el servidor MCP de Codex también devuelve `"content"` para los clientes MCP más antiguos.

# Crear flujos de trabajo con varios agentes

Codex CLI puede hacer mucho más que ejecutar tareas puntuales. Al exponer la CLI como servidor de [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) y orquestarla con OpenAI Agents SDK, puedes crear flujos de trabajo deterministas y revisables que escalan desde un solo agente hasta un proceso completo de entrega de software.

Esta guía explica paso a paso el mismo flujo de trabajo que se muestra en [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb). Vas a:

- iniciar Codex CLI como un servidor MCP de larga duración,
- crear un flujo de trabajo bien delimitado con un solo agente que produzca un juego listo para jugar en el navegador, y
- orquestar un equipo de varios agentes con transferencias de control, medidas de protección y trazas completas que podrás revisar después.

Antes de comenzar, asegúrate de tener:

- una instalación local de [Codex CLI](/es-419/codex/cli) para que el comando `codex` esté disponible.
- Python 3.10+ con `pip`.
- Node.js 18+ si quieres ejecutar el ejemplo anterior de MCP Inspector.
- una clave de API de OpenAI almacenada localmente. Puedes crear o administrar claves en el [panel de OpenAI](https://platform.openai.com/account/api-keys).

Crea un directorio de trabajo para la guía y agrega tu clave de API a un archivo `.env`:

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## Instalar las dependencias

Agents SDK gestiona la orquestación de Codex, las transferencias de control y las trazas. Instala los paquetes más recientes del SDK:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  Activar un entorno virtual mantiene las dependencias del SDK aisladas del
resto del sistema.

## Inicializar Codex CLI como servidor MCP

Comienza por convertir Codex CLI en un servidor MCP que Agents SDK pueda invocar. El servidor expone dos herramientas (`codex()` para iniciar una conversación y `codex-reply()` para continuarla) y mantiene Codex activo durante varios turnos de los agentes.

Crea un archivo llamado `codex_mcp.py` y agrega lo siguiente:

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

Ejecuta el script una vez para verificar que Codex se inicie correctamente:

```bash
python codex_mcp.py
```

El script finaliza después de imprimir `Codex MCP server started.`. En las siguientes secciones, reutilizarás el mismo servidor MCP en flujos de trabajo más completos.

## Crear un flujo de trabajo con un solo agente

Comencemos con un ejemplo acotado que usa Codex MCP para crear un pequeño juego para navegador. El flujo de trabajo se basa en dos agentes:

1. **Diseñador del juego**: redacta una descripción general del juego.
2. **Desarrollador del juego**: implementa el juego mediante llamadas a Codex MCP.

Actualiza `codex_mcp.py` con el siguiente código. Este código conserva la configuración anterior del servidor MCP y agrega ambos agentes.

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

Ejecuta el script:

```bash
python codex_mcp.py
```

Codex leerá el resumen del diseñador, creará un archivo `index.html` y guardará el juego completo en el disco. Abre el archivo generado en un navegador para jugar. Cada ejecución produce un diseño diferente, con variaciones únicas en la jugabilidad y un acabado pulido.

## Ampliar el flujo de trabajo a varios agentes

Ahora convierte la configuración de un solo agente en un flujo de trabajo orquestado y con trazabilidad. El sistema agrega:

- **Gerente de proyecto**: crea requisitos compartidos, coordina las transferencias y aplica medidas de protección.
- **Diseñador**, **Desarrollador de frontend**, **Desarrollador del servidor** y **Responsable de pruebas**: cada uno con instrucciones específicas para su función y carpetas de salida.

Crea un archivo nuevo llamado `multi_agent_workflow.py`:

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

Ejecuta el script y observa los archivos generados:

```bash
python multi_agent_workflow.py
ls -R
```

El agente que actúa como gerente de proyecto escribe `REQUIREMENTS.md`, `TEST.md` y `AGENT_TASKS.md`, y luego coordina las transferencias entre los agentes de diseño, frontend, servidor y pruebas. Cada agente escribe los artefactos correspondientes a su función en su propia carpeta antes de devolver el control al gerente de proyecto.

## Revisar las trazas del flujo de trabajo

Codex registra automáticamente trazas que capturan cada prompt, llamada a herramienta y transferencia. Cuando termine la ejecución con varios agentes, abre el [panel de trazas](https://platform.openai.com/trace) para inspeccionar la cronología de ejecución.

La traza de alto nivel muestra cómo el gerente de proyecto verifica las transferencias antes de continuar. Haz clic en cada paso para ver los prompts, las llamadas a Codex MCP, los archivos que se escribieron y la duración de cada ejecución. Estos detalles facilitan la auditoría de cada transferencia y permiten comprender cómo evolucionó el flujo de trabajo turno a turno.
Estas trazas facilitan la depuración de problemas del flujo de trabajo, la auditoría del comportamiento de los agentes y la medición del rendimiento a lo largo del tiempo sin necesidad de instrumentación adicional.
