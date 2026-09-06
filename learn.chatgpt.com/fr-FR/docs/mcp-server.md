<!-- source: https://learn.chatgpt.com/fr-FR/docs/mcp-server -->

# Exécution de Codex en tant que serveur MCP

  La commande `codex mcp-server` est obsolète. Utilisez plutôt l’[App Server
  de Codex](/fr-FR/codex/app-server). Pour appeler Codex depuis Claude Code, utilisez le
[plugin Codex pour Claude Code](https://github.com/openai/codex-plugin-cc),
  qui utilise l’App Server. Cette page documente la commande obsolète pour
  les intégrations existantes.

Vous pouvez exécuter Codex en tant que serveur MCP et vous y connecter depuis d’autres clients MCP (par exemple, un agent créé avec l’[intégration MCP du SDK Agents d’OpenAI](/api/docs/guides/agents/integrations-observability#mcp)).

Pour démarrer Codex en tant que serveur MCP, vous pouvez utiliser la commande suivante :

```bash
codex mcp-server
```

Vous pouvez lancer un serveur MCP Codex avec le [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector) :

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

Envoyez une requête `tools/list` pour afficher deux outils :

**`codex`** : lancez une session Codex avec le prompt et les paramètres de configuration de remplacement suivants :

| Propriété                 | Type     | Description                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (obligatoire)  | `string` | Prompt utilisateur initial permettant de démarrer la conversation Codex.                                                 |
| `approval-policy`        | `string` | Politique d’approbation des commandes shell générées par le modèle : `untrusted`, `on-request` et `never`.       |
| `base-instructions`      | `string` | Ensemble d’instructions à utiliser à la place des instructions par défaut.                                              |
| `compact-prompt`         | `string` | Prompt utilisé pour le compactage de la conversation.                                                            |
| `config`                 | `object` | Paramètres de configuration individuels qui remplacent les paramètres correspondants définis dans `$CODEX_HOME/config.toml`.                     |
| `cwd`                    | `string` | Répertoire de travail de la session. Si son chemin est relatif, il est résolu par rapport au répertoire courant du processus serveur. |
| `developer-instructions` | `string` | Instructions du développeur injectées sous forme de message de rôle développeur.                                             |
| `model`                  | `string` | Remplacement facultatif du nom du modèle (par exemple, `gpt-5.6-terra`).                                     |
| `sandbox`                | `string` | Mode du bac à sable : `read-only`, `workspace-write` ou `danger-full-access`.                                   |

**`codex-reply`** : poursuivez une session Codex en fournissant l’ID du thread et le prompt. L’outil `codex-reply` accepte les propriétés suivantes :

| Propriété                      | Type   | Description                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (obligatoire)       | string | Prompt utilisateur suivant permettant de poursuivre la conversation Codex.  |
| **`threadId`** (obligatoire)     | string | L’ID du thread à poursuivre.                         |
| `conversationId` (obsolète) | string | Alias obsolète de `threadId` (conservé pour assurer la compatibilité). |

Utilisez la valeur `threadId` provenant de `structuredContent.threadId` dans la réponse à `tools/call`. Les demandes d’approbation (exec/patch) incluent également `threadId` dans leur charge utile `params`.

Exemple de charge utile de réponse :

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

Notez que les clients MCP modernes ne renvoient généralement que `"structuredContent"` comme résultat d’un appel d’outil, lorsque ce champ est présent. Le serveur MCP Codex renvoie toutefois également `"content"` pour les clients MCP plus anciens.

# Création de workflows multi-agents

Codex CLI peut faire bien plus qu’exécuter des tâches ponctuelles. En exposant la CLI sous forme de serveur [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) et en l’orchestrant avec le SDK Agents d’OpenAI, vous pouvez créer des workflows déterministes que vous pouvez examiner, allant d’un agent unique à une chaîne complète de livraison logicielle.

Ce guide détaille le workflow présenté dans l’[OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb). Vous allez :

- lancer Codex CLI en tant que serveur MCP s’exécutant en continu,
- créer un workflow mono-agent ciblé qui produit un jeu jouable dans un navigateur, et
- orchestrer une équipe multi-agents avec des transferts entre agents, des garde-fous et des traces complètes que vous pourrez examiner par la suite.

Avant de commencer, vérifiez que vous disposez des éléments suivants :

- Une installation locale de [Codex CLI](/fr-FR/codex/cli), afin que la commande `codex` soit disponible.
- Python 3.10+ avec `pip`.
- Node.js 18+ si vous souhaitez exécuter l’exemple de MCP Inspector ci-dessus.
- Une clé API OpenAI stockée localement. Vous pouvez créer ou gérer vos clés dans le [tableau de bord OpenAI](https://platform.openai.com/account/api-keys).

Créez un répertoire de travail pour ce guide et ajoutez votre clé API dans un fichier `.env` :

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## Installez les dépendances

Le SDK Agents assure l’orchestration de Codex ainsi que la gestion des transferts et des traces. Installez les dernières versions des packages du SDK :

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  L’activation d’un environnement virtuel permet d’isoler les dépendances du SDK du
reste de votre système.

## Initialisez Codex CLI en tant que serveur MCP

Commencez par transformer Codex CLI en serveur MCP que le SDK Agents peut appeler. Le serveur expose deux outils (`codex()` pour démarrer une conversation et `codex-reply()` pour la poursuivre) et maintient Codex en cours d’exécution pendant plusieurs tours d’agent.

Créez un fichier nommé `codex_mcp.py` et ajoutez-y ce qui suit :

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

Exécutez le script une fois pour vérifier que Codex démarre correctement :

```bash
python codex_mcp.py
```

Le script se termine après avoir affiché `Codex MCP server started.`. Dans les sections suivantes, vous réutiliserez le même serveur MCP dans des workflows plus élaborés.

## Créez un workflow mono-agent

Commencez par un exemple ciblé qui utilise Codex MCP pour livrer un petit jeu pour navigateur. Le workflow repose sur deux agents :

1. **Concepteur du jeu** : rédige un brief pour le jeu.
2. **Développeur du jeu** : implémente le jeu en appelant Codex MCP.

Mettez à jour `codex_mcp.py` avec le code suivant. Il conserve la configuration du serveur MCP définie plus haut et ajoute les deux agents.

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

Exécutez le script :

```bash
python codex_mcp.py
```

Codex lira le brief du designer, créera un fichier `index.html` et enregistrera l’intégralité du jeu sur le disque. Ouvrez le fichier généré dans un navigateur pour y jouer. Chaque exécution produit un design différent, avec ses propres variantes de gameplay et ses finitions.

## Passez à un workflow multi-agents

Transformez maintenant la configuration à un seul agent en un workflow orchestré et traçable. Le système ajoute les agents suivants :

- **Chef de projet** : définit les exigences communes, coordonne les transferts et veille au respect des garde-fous.
- **Designer**, **Développeur frontend**, **Développeur serveur** et **Testeur** : chacun dispose d’instructions et de dossiers de sortie propres à son périmètre.

Créez un nouveau fichier nommé `multi_agent_workflow.py` :

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

Exécutez le script et observez les fichiers générés :

```bash
python multi_agent_workflow.py
ls -R
```

L’agent chef de projet rédige `REQUIREMENTS.md`, `TEST.md` et `AGENT_TASKS.md`, puis coordonne les transferts entre les agents designer, développeur frontend, développeur serveur et testeur. Chaque agent produit dans son propre dossier les artefacts relevant de son périmètre avant de rendre le contrôle au chef de projet.

## Consultez les traces du workflow

Codex enregistre automatiquement des traces qui consignent chaque prompt, appel d’outil et transfert. Une fois l’exécution multi-agents terminée, ouvrez le [tableau de bord des traces](https://platform.openai.com/trace) pour examiner la chronologie d’exécution.

La vue d’ensemble de la trace montre comment le chef de projet vérifie les transferts avant de poursuivre. Cliquez sur les différentes étapes pour consulter les prompts, les appels à Codex MCP, les fichiers enregistrés et les durées d’exécution. Ces informations permettent d’auditer facilement chaque transfert et de comprendre comment le workflow a évolué tour après tour.
Ces traces facilitent le débogage des dysfonctionnements du workflow, l’audit du comportement des agents et la mesure des performances au fil du temps, sans instrumentation supplémentaire.
