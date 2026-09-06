<!-- source: https://learn.chatgpt.com/pt-BR/docs/mcp-server -->

# Executar o Codex como servidor MCP

  `codex mcp-server` está obsoleto. Use o [App
  Server do Codex](/pt-BR/codex/app-server) em seu lugar. Para chamar o Codex a partir do Claude Code, use o
[plug-in do Codex para Claude Code](https://github.com/openai/codex-plugin-cc),
  que usa o App Server. Esta página documenta o comando obsoleto para
  integrações existentes.

Você pode executar o Codex como servidor MCP e se conectar a ele a partir de outros clientes MCP (por exemplo, um agente criado com a [integração MCP do SDK de Agentes da OpenAI](/api/docs/guides/agents/integrations-observability#mcp)).

Para iniciar o Codex como servidor MCP, você pode usar o seguinte comando:

```bash
codex mcp-server
```

Você pode iniciar um servidor MCP do Codex com o [Model Context Protocol Inspector](https://modelcontextprotocol.io/legacy/tools/inspector):

```bash
npx @modelcontextprotocol/inspector codex mcp-server
```

Envie uma solicitação `tools/list` para ver duas ferramentas:

**`codex`**: Execute uma sessão do Codex com o seguinte prompt e as seguintes substituições de configuração:

| Propriedade                 | Tipo     | Descrição                                                                                              |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------- |
| **`prompt`** (obrigatório)  | `string` | O prompt inicial do usuário para iniciar a conversa com o Codex.                                                 |
| `approval-policy`        | `string` | Política de aprovação para comandos de shell gerados pelo modelo: `untrusted`, `on-request` e `never`.       |
| `base-instructions`      | `string` | O conjunto de instruções a ser usado no lugar das instruções padrão.                                              |
| `compact-prompt`         | `string` | Prompt usado ao compactar a conversa.                                                            |
| `config`                 | `object` | Configurações individuais que substituem as definidas em `$CODEX_HOME/config.toml`.                     |
| `cwd`                    | `string` | Diretório de trabalho da sessão. Se o caminho for relativo, será resolvido em relação ao diretório atual do processo do servidor. |
| `developer-instructions` | `string` | Instruções do desenvolvedor injetadas como uma mensagem com o papel de desenvolvedor.                                             |
| `model`                  | `string` | Substituição opcional do nome do modelo (por exemplo, `gpt-5.6-terra`).                                     |
| `sandbox`                | `string` | Modo Sandbox: `read-only`, `workspace-write` ou `danger-full-access`.                                   |

**`codex-reply`**: Continue uma sessão do Codex informando o ID da conversa e o prompt. A ferramenta `codex-reply` aceita estas propriedades:

| Propriedade                      | Tipo   | Descrição                                               |
| ----------------------------- | ------ | --------------------------------------------------------- |
| **`prompt`** (obrigatório)       | string | O próximo prompt do usuário para continuar a conversa com o Codex.  |
| **`threadId`** (obrigatório)     | string | O ID da conversa a ser continuada.                         |
| `conversationId` (obsoleto) | string | Nome alternativo obsoleto para `threadId` (mantido por compatibilidade). |

Use o `threadId` de `structuredContent.threadId` na resposta de `tools/call`. As solicitações de aprovação (exec/patch) também incluem `threadId` no conteúdo de `params`.

Exemplo de corpo de resposta:

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

Observe que os clientes MCP modernos geralmente informam apenas `"structuredContent"` como resultado de uma chamada de ferramenta, quando presente, embora o servidor MCP do Codex também retorne `"content"` para atender a clientes MCP mais antigos.

# Criar fluxos de trabalho multiagente

A Codex CLI pode fazer muito mais do que executar tarefas pontuais. Ao expor a CLI como um servidor do [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) e orquestrá-la com o SDK de Agentes da OpenAI, você pode criar fluxos de trabalho determinísticos e passíveis de revisão que vão de um único agente a um pipeline completo de entrega de software.

Este guia apresenta, passo a passo, o mesmo fluxo de trabalho demonstrado no [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/codex/codex_mcp_agents_sdk/building_consistent_workflows_codex_cli_agents_sdk.ipynb). Você vai:

- iniciar a Codex CLI como um servidor MCP de longa duração,
- criar um fluxo de trabalho de escopo definido com um único agente que produza um jogo para navegador pronto para jogar, e
- orquestrar uma equipe multiagente com transferências de controle, proteções e rastreamentos completos que você poderá revisar depois.

Antes de começar, verifique se você tem:

- A [Codex CLI](/pt-BR/codex/cli) instalada localmente para que o comando `codex` esteja disponível.
- Python 3.10+ com `pip`.
- Node.js 18+ se quiser executar o exemplo do MCP Inspector acima.
- Uma chave de API da OpenAI armazenada localmente. Você pode criar ou gerenciar chaves no [painel da OpenAI](https://platform.openai.com/account/api-keys).

Crie um diretório de trabalho para o guia e adicione sua chave de API a um arquivo `.env`:

```bash
mkdir codex-workflows
cd codex-workflows
printf "OPENAI_API_KEY=sk-..." > .env
```

## Instalar dependências

O SDK de Agentes gerencia a orquestração do Codex, as transferências de controle e os rastreamentos. Instale os pacotes mais recentes do SDK:

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade openai openai-agents python-dotenv
```

  Ativar um ambiente virtual mantém as dependências do SDK isoladas do
restante do sistema.

## Inicializar a Codex CLI como servidor MCP

Comece transformando a Codex CLI em um servidor MCP que o SDK de Agentes possa chamar. O servidor disponibiliza duas ferramentas (`codex()` para iniciar uma conversa e `codex-reply()` para continuá-la) e mantém o Codex ativo ao longo de vários turnos dos agentes.

Crie um arquivo chamado `codex_mcp.py` e adicione o seguinte conteúdo:

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

Execute o script uma vez para verificar se o Codex inicia corretamente:

```bash
python codex_mcp.py
```

O script é encerrado após exibir `Codex MCP server started.`. Nas próximas seções, você reutilizará o mesmo servidor MCP em fluxos de trabalho mais elaborados.

## Criar um fluxo de trabalho com um único agente

Vamos começar com um exemplo de escopo delimitado que usa o MCP do Codex para criar um pequeno jogo para navegador. Esse fluxo de trabalho usa dois agentes:

1. **Designer de jogos**: escreve uma descrição breve do jogo.
2. **Desenvolvedor de jogos**: implementa o jogo chamando o MCP do Codex.

Atualize `codex_mcp.py` com o código a seguir. Esse código mantém a configuração do servidor MCP apresentada acima e adiciona os dois agentes.

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

Execute o script:

```bash
python codex_mcp.py
```

O Codex lerá a descrição do designer, criará um arquivo `index.html` e gravará o jogo completo no disco. Abra o arquivo gerado em um navegador para jogar. Cada execução produz um design diferente, com variações únicas na jogabilidade e um acabamento refinado.

## Amplie o fluxo de trabalho para incluir vários agentes

Agora, transforme a configuração com um único agente em um fluxo de trabalho orquestrado e rastreável. O sistema passa a incluir:

- **Gerente de projeto**: cria requisitos compartilhados, coordena as transferências de controle e aplica proteções.
- **Designer**, **Desenvolvedor de frontend**, **Desenvolvedor de servidor** e **Testador**: cada um com instruções de escopo delimitado e pastas de saída.

Crie um novo arquivo chamado `multi_agent_workflow.py`:

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

Execute o script e observe os arquivos gerados:

```bash
python multi_agent_workflow.py
ls -R
```

O agente que atua como gerente de projeto grava `REQUIREMENTS.md`, `TEST.md` e `AGENT_TASKS.md` e, em seguida, coordena as transferências de controle entre os agentes de design, frontend, servidor e testes. Cada agente grava artefatos de escopo delimitado em sua própria pasta antes de devolver o controle ao gerente de projeto.

## Rastreie o fluxo de trabalho

O Codex registra automaticamente rastreamentos que capturam cada prompt, chamada de ferramenta e transferência de controle. Quando a execução multiagente terminar, abra o [painel de rastreamentos](https://platform.openai.com/trace) para inspecionar a linha do tempo da execução.

A visão geral do rastreamento mostra como o gerente de projeto verifica as transferências de controle antes de prosseguir. Clique em cada etapa para ver prompts, chamadas ao Codex MCP, arquivos gravados e tempos de execução. Esses detalhes facilitam a auditoria de cada transferência de controle e a compreensão de como o fluxo de trabalho evoluiu a cada turno.
Esses rastreamentos facilitam a depuração de problemas no fluxo de trabalho, a auditoria do comportamento dos agentes e a medição do desempenho ao longo do tempo, sem exigir instrumentação adicional.
