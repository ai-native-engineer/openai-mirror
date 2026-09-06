<!-- source: https://learn.chatgpt.com/pt-BR/docs/agent-configuration/subagents -->

O ChatGPT Work e o Codex podem executar fluxos de trabalho com subagentes, iniciando agentes especializados
em paralelo e reunindo seus resultados em uma única resposta. Isso pode ser especialmente
útil em tarefas complexas que permitem amplo paralelismo, como explorar uma base de código
ou implementar um plano de várias etapas para um recurso.

Nos clientes locais do Codex, você também pode definir agentes personalizados com diferentes
configurações de modelo e instruções para diferentes tarefas.

## Disponibilidade

O ChatGPT Work disponibiliza fluxos de trabalho e atividades de subagentes para contas qualificadas.

<a id="custom-agents"></a>

As versões atuais do Codex habilitam por padrão os fluxos de trabalho com subagentes. A atividade dos subagentes
aparece no aplicativo do ChatGPT para desktop, na Codex CLI e na extensão para IDE.

Como cada subagente usa o modelo e as ferramentas de forma independente, os fluxos de trabalho
com subagentes consomem mais tokens do que execuções comparáveis com um único agente.

No ChatGPT Work, peça ao ChatGPT para delegar tarefas independentes a subagentes. Os
agentes são executados no ambiente hospedado do ChatGPT, e o chat mostra suas
atividades e seus resultados. Na maioria dos níveis de inteligência, solicite a delegação
explicitamente. Com Ultra, o ChatGPT pode delegar tarefas de forma proativa quando agentes em
paralelo puderem melhorar significativamente a velocidade ou a qualidade.

Em um chat do aplicativo, peça ao Codex para delegar partes independentes do trabalho a
subagentes. As versões locais atuais do Codex fazem essa delegação quando você solicita diretamente ou quando
instruções aplicáveis de `AGENTS.md` ou de habilidades solicitam isso. O aplicativo exibe cada
conversa de subagente para que você possa inspecionar seu trabalho e o resumo retornado ao
chat principal.

Em uma sessão interativa da CLI, peça ao Codex para usar subagentes. O Codex também pode seguir
instruções aplicáveis de `AGENTS.md` ou de habilidades que solicitem a delegação. Use
`/agent` para inspecionar e alternar entre conversas de agentes durante a execução. A conversa
principal reúne os resultados dos subagentes na resposta final.

Em um chat da IDE, peça ao Codex para delegar partes independentes do trabalho a subagentes.
O Codex também pode seguir instruções aplicáveis de `AGENTS.md` ou de habilidades que solicitem
a delegação. Quando a interface de agentes em segundo plano estiver disponível, os subagentes ativos aparecem
acima do editor. Expanda o painel para ver o status deles, interromper todos os subagentes
ativos ou abrir a conversa de um subagente específico.

## Por que os fluxos de trabalho com subagentes são úteis

Mesmo com grandes janelas de contexto, os modelos têm limites. Se você sobrecarregar o chat principal (no qual define requisitos, restrições e decisões) com resultados intermediários cheios de ruído, como anotações de exploração, logs de testes, rastreamentos de pilha e saídas de comandos, a sessão pode se tornar menos confiável com o tempo.

Isso costuma ser descrito como:

- **Poluição do contexto**: informações úteis ficam ocultas em meio a resultados intermediários cheios de ruído.
- **Degradação do contexto**: o desempenho piora à medida que o chat se enche de detalhes menos relevantes.

Para saber mais, consulte o artigo da Chroma sobre [degradação do contexto](https://research.trychroma.com/context-rot).

Os fluxos de trabalho com subagentes ajudam a tirar da conversa principal as tarefas que geram ruído:

- Mantenha o **agente principal** concentrado nos requisitos, nas decisões e nos resultados finais.
- Execute **subagentes** especializados em paralelo para exploração, testes ou análise de logs.
- Retorne **resumos** dos subagentes em vez de resultados intermediários brutos.

Esses fluxos também podem economizar tempo quando o trabalho pode ser executado de forma independente e em paralelo,
além de facilitar tarefas de maior porte ao dividi-las em partes de escopo
delimitado. Por exemplo, o Codex pode dividir a análise de um documento com milhões de
tokens em problemas menores e retornar uma síntese das conclusões à conversa
principal.

Como ponto de partida, use agentes em paralelo para tarefas que exigem muita leitura, como
exploração, testes, triagem e elaboração de resumos. Tenha mais cuidado com fluxos de trabalho paralelos
que exigem muita escrita, pois agentes editando código ao mesmo tempo podem gerar
conflitos e aumentar o esforço de coordenação.

## Termos principais

O Codex usa alguns termos relacionados nos fluxos de trabalho com subagentes:

- **Fluxo de trabalho com subagentes**: um fluxo de trabalho em que o Codex executa agentes em paralelo e combina seus resultados.
- **Subagente**: um agente que o Codex inicia para realizar uma tarefa específica por delegação.
- **Conversa do agente**: a conversa em que um subagente realiza seu trabalho. Os clientes compatíveis permitem abrir essas conversas para inspecionar o progresso ou os resultados.

## Como acionar fluxos de trabalho com subagentes

Na maioria dos níveis de inteligência, solicite diretamente o uso de subagentes ou de agentes trabalhando em
paralelo. Ultra habilita a delegação proativa, permitindo que o ChatGPT delegue tarefas independentes
adequadas sem uma solicitação adicional.

Solicite diretamente o uso de subagentes ou de agentes trabalhando em paralelo. O Codex também pode delegar quando
instruções aplicáveis do projeto ou de habilidades solicitarem isso.

Na prática, acionar manualmente significa usar instruções diretas, como
"inicie dois agentes", "delegue este trabalho em paralelo" ou "use um agente por
item". Os fluxos de trabalho com subagentes consomem mais tokens do que execuções comparáveis com um único agente
porque cada subagente usa o modelo e as ferramentas de forma independente.

Um bom prompt para subagentes deve explicar como dividir o trabalho, se o Codex
deve aguardar todos os agentes antes de continuar e qual resumo ou resultado deve
retornar.

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## Escolha de modelos e raciocínio

Agentes diferentes precisam de configurações diferentes de modelo e raciocínio.

No ChatGPT Work, escolha um modelo e um nível de inteligência no editor.
Os níveis de inteligência disponíveis podem incluir **Leve**, **Médio**, **Alto**,
**Extra alto** e **Max**, dependendo do modelo selecionado. **Ultra** está
disponível apenas para contas qualificadas e modelos compatíveis. Esse nível usa raciocínio
máximo e permite que o ChatGPT delegue proativamente tarefas adequadas a subagentes.

Nos outros níveis de inteligência, solicite explicitamente subagentes quando quiser delegar o trabalho
em paralelo.

Se você não configurar um modelo de subagente nem `model_reasoning_effort`, o
subagente herdará o modelo e o esforço de raciocínio do agente pai. Se uma solicitação explícita
de criação de agente ou um valor padrão de `[agents]` selecionar um modelo sem um
esforço de raciocínio explícito ou configurado, o subagente usará o esforço de raciocínio padrão
desse modelo. Para equilibrar inteligência, velocidade e preço em cada tarefa,
solicite no prompt um modelo ou um esforço de raciocínio específico,
configure os valores padrão de `[agents]` em `config.toml` ou defina `model` e
`model_reasoning_effort` diretamente no arquivo do agente personalizado.
Por exemplo, use <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> em varreduras rápidas ou uma configuração de <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> com maior esforço para tarefas que exigem mais raciocínio.

  Para a maioria das tarefas no Codex, comece com{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>. Use{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> quando quiser
  uma opção mais rápida e econômica para tarefas mais leves de subagentes.

### Escolha do modelo

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**: Comece por aqui para agentes com tarefas exigentes. É a opção mais eficaz para trabalhos ambíguos e com várias etapas que exigem planejamento, uso de ferramentas, validação e execução até o fim em um contexto mais amplo.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**: Use para agentes que priorizam velocidade e eficiência em vez de profundidade, como em exploração, varreduras que exigem muita leitura, revisão de arquivos grandes ou processamento de documentos de apoio. Funciona bem para agentes executados em paralelo que retornam resultados sintetizados ao agente principal.
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**: Use para agentes rápidos e de escopo delimitado que lidam com tarefas bem definidas, repetíveis ou de grande volume.

### Esforço de raciocínio (`model_reasoning_effort`)

- **`ultra`**: Use para o raciocínio mais profundo quando o modelo selecionado oferecer suporte
  a esse nível.
- **`max`** e **`xhigh`**: Use para tarefas que exigem raciocínio especialmente intenso quando o
  modelo selecionado oferecer suporte a esses níveis.
- **`high`**: Use quando um agente precisar acompanhar uma lógica complexa, verificar suposições ou analisar casos extremos (por exemplo, agentes de revisão ou especializados em segurança).
- **`medium`**: Uma configuração padrão equilibrada para a maioria dos agentes.
- **`low`**: Use quando a tarefa for simples e a velocidade for o mais importante.

Um esforço de raciocínio maior aumenta o tempo de resposta e o uso de tokens, mas pode melhorar a qualidade em trabalhos complexos. Para mais detalhes, consulte [Modelos](/pt-BR/codex/models), [Configuração básica](/pt-BR/codex/config-file/config-basic) e [Referência de configuração](/pt-BR/codex/config-file/config-reference).

## Orquestração e controles de conversas

O ChatGPT ou o Codex gerencia a orquestração entre os agentes, incluindo a criação de novos
subagentes, o encaminhamento de instruções complementares, a espera pelos resultados e o encerramento de
conversas de agentes.

Quando vários agentes estão em execução, o Codex aguarda até que todos os resultados solicitados estejam
disponíveis e então retorna uma resposta consolidada.

Na maioria dos níveis de inteligência, o ChatGPT inicia agentes após uma solicitação direta. Com
Ultra, o ChatGPT também pode delegar proativamente quando o trabalho em paralelo for útil.

As versões locais atuais do Codex iniciam agentes após uma solicitação direta ou uma instrução aplicável
do projeto ou de uma habilidade.

Para ver isso em ação, experimente o seguinte prompt no seu projeto:

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## Gerenciamento de subagentes

Abra **Subagentes** para ver as listas somente leitura **Ativos** e **Concluídos** . Selecione um
subagente concluído para inspecionar seus detalhes e seu resultado. A barra lateral da Web informa
a atividade dos subagentes, mas não oferece controles para interromper ou orientar um
subagente específico.

- Abra uma conversa de subagente pela atividade exibida na conversa principal para inspecionar
seu trabalho.
- Peça diretamente ao Codex para orientar um subagente em execução, interrompê-lo ou fechar conversas
de subagentes concluídos.

  

  

- Use `/agent` na CLI para alternar entre threads de agentes ativas e inspecionar a thread em andamento.
- Peça diretamente ao Codex para orientar um subagente em execução, interrompê-lo ou fechar threads de agentes concluídas.

- Quando o painel de agentes em segundo plano estiver disponível, expanda-o para verificar o status,
interromper subagentes ativos ou abrir a thread de um subagente.
- Peça diretamente ao Codex para orientar um subagente em execução, interrompê-lo ou fechar threads
concluídas de subagentes.

## Aprovações e controles de Sandbox

Os subagentes herdam sua política de Sandbox atual.

O ChatGPT Work executa subagentes em seu ambiente hospedado e não disponibiliza um
Sandbox local do Codex nem um controle do modo de aprovação. Os subagentes usam as ferramentas disponíveis
no chat que os originou. As permissões de sites e conectores continuam sendo
específicas de cada ferramenta.

Os subagentes herdam o modo de permissão selecionado abaixo do editor. Escolha o
modo de permissão para o turno do agente pai antes de pedir ao Codex para delegar o trabalho.

Em sessões interativas da CLI, solicitações de aprovação podem surgir de threads inativas de agentes
mesmo enquanto você visualiza a thread principal. O painel sobreposto de aprovação
mostra o rótulo da thread de origem, e você pode pressionar `o` para abrir essa thread antes de
aprovar, rejeitar ou responder à solicitação.

Em fluxos não interativos ou quando uma execução não consegue apresentar uma nova solicitação de aprovação, uma
ação que exige nova aprovação falha, e o Codex retorna o erro ao fluxo de trabalho
que a originou.

O Codex também reaplica as substituições de configuração em vigor no turno do agente pai ao iniciar um
agente filho. Isso inclui as opções de Sandbox e aprovação definidas de forma interativa durante
a sessão, como alterações em `/permissions` ou o uso de `--yolo`, mesmo que o arquivo
do agente personalizado selecionado defina padrões diferentes.

Os subagentes herdam o modo de permissão selecionado abaixo do editor. Escolha
o modo de permissão para o turno do agente pai antes de pedir ao Codex para delegar o trabalho.

Você também pode substituir a configuração de Sandbox de [agentes personalizados](#custom-agents) específicos, por exemplo, configurando explicitamente um deles para trabalhar em modo somente leitura.

## Agentes personalizados

O Codex inclui agentes integrados:

- `default`: agente de uso geral usado como alternativa.
- `worker`: agente focado na execução de implementações e correções.
- `explorer`: agente de exploração da base de código, com uso intensivo de leitura.

Para definir seus próprios agentes personalizados, adicione arquivos TOML independentes em
`~/.codex/agents/` para agentes pessoais ou em `.codex/agents/` para agentes com escopo de
projeto.

Cada arquivo define um agente personalizado. O Codex carrega esses arquivos como camadas de configuração
para as sessões iniciadas, permitindo que os agentes personalizados substituam as mesmas configurações disponíveis em
uma sessão normal do Codex. Isso pode parecer mais complexo do que um manifesto dedicado ao agente,
e o formato pode evoluir conforme a criação e o compartilhamento amadurecem.

Cada arquivo independente de agente personalizado deve definir:

- `name`
- `description`
- `developer_instructions`

Se um arquivo de agente personalizado definir `model` ou `model_reasoning_effort`, o valor no
arquivo terá precedência. Antes de aplicar o arquivo, o Codex determina cada configuração
a partir de um valor explícito de inicialização, seguido do padrão correspondente em `[agents]` e,
por fim, do valor do agente pai. Se uma solicitação explícita de inicialização ou um padrão em `[agents]`
selecionar um modelo e nenhum deles fornecer um esforço de raciocínio, o Codex usará
o esforço padrão desse modelo. Um arquivo de agente personalizado que defina apenas `model`
preserva esse esforço determinado anteriormente. Defina também `model_reasoning_effort` no
arquivo se o modelo selecionado não oferecer suporte a esse esforço ou se você quiser um
esforço diferente. Outras configurações da sessão, como `sandbox_mode`, `mcp_servers`
e `skills.config`, são herdadas do agente pai quando o arquivo do agente personalizado
as omite.

### Configurações globais

As configurações globais de subagentes continuam em `[agents]` na sua [configuração](/pt-BR/codex/config-file/config-basic#configuration-precedence).

| Campo                                       | Tipo    | Obrigatório | Finalidade                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | booleano |    Não    | Ative ou desative as ferramentas multiagente.                                |
| `agents.max_concurrent_threads_per_session` | número  |    Não    | Limite o número de threads de agentes iniciados que podem ficar abertas simultaneamente, sem contar a principal. |
| `agents.default_subagent_model`             | string  |    Não    | Defina o modelo padrão para os agentes iniciados.                           |
| `agents.default_subagent_reasoning_effort`  | string  |    Não    | Defina o esforço de raciocínio padrão para os agentes iniciados.                |
| `agents.interrupt_message`                  | booleano |    Não    | Registre uma mensagem visível para o modelo quando o turno de um agente for interrompido.   |

**Observações:**

- `agents.enabled` usa `true` por padrão. Defina como `false` para desativar as ferramentas multiagente.
- Se você não definir `agents.max_concurrent_threads_per_session`, o Codex escolherá o padrão. As configurações existentes podem continuar usando `agents.max_threads` como um alias legado.
- Valores explícitos de inicialização têm precedência sobre `agents.default_subagent_model` e `agents.default_subagent_reasoning_effort`.
- `agents.interrupt_message` usa `true` por padrão. Defina como `false` para omitir do contexto do agente a mensagem de interrupção visível para o modelo.
- Se o nome de um agente personalizado corresponder ao de um agente integrado, como `explorer`, o agente personalizado terá precedência.

### Esquema do arquivo de agente personalizado

| Campo                    | Tipo   | Obrigatório | Finalidade                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | string |   Sim    | Nome do agente que o Codex usa para iniciá-lo ou se referir a ele. |
| `description`            | string |   Sim    | Orientação para o usuário sobre quando o Codex deve usar esse agente.     |
| `developer_instructions` | string |   Sim    | Instruções principais que definem o comportamento do agente.             |

Você também pode incluir outras chaves compatíveis de `config.toml` em um arquivo de agente personalizado, como `model`, `model_reasoning_effort`, `sandbox_mode`, `mcp_servers` e `skills.config`.

O Codex identifica o agente personalizado pelo campo `name`. Usar o mesmo nome para o arquivo e
o agente é a convenção mais simples, mas o campo `name` é a referência
definitiva.

### Exemplos de agentes personalizados

Os melhores agentes personalizados têm escopo delimitado e diretrizes bem definidas. Atribua a cada agente uma função clara, um
conjunto de ferramentas adequado a ela e instruções que o impeçam de assumir
tarefas fora do escopo.

#### Exemplo 1: revisão de PR

Esse padrão divide a revisão entre três agentes personalizados, cada um com um foco específico:

- `pr_explorer` mapeia a base de código e reúne evidências.
- `reviewer` identifica riscos relacionados à correção do código, à segurança e aos testes.
- `docs_researcher` consulta a documentação do framework ou da API por meio de um servidor MCP dedicado.

Configuração do projeto (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`:

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

`.codex/agents/reviewer.toml`:

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

`.codex/agents/docs-researcher.toml`:

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

Essa configuração funciona bem com prompts como:

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### Exemplo 2: depuração de integração de frontend

Esse padrão é útil para regressões de interface, fluxos instáveis no navegador ou bugs de integração que abrangem tanto o código do aplicativo quanto o produto em execução.

Configuração do projeto (`.codex/config.toml`):

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`:

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

`.codex/agents/browser-debugger.toml`:

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

`.codex/agents/ui-fixer.toml`:

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

Essa configuração funciona bem com prompts como:

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
