<!-- source: https://learn.chatgpt.com/pt-BR/docs/hooks -->

Os ganchos são uma estrutura de extensibilidade para o Codex. Eles permitem executar scripts ou ferramentas MCP
durante o ciclo agêntico, possibilitando recursos como:

- Enviar o chat para um sistema personalizado de logs e análise
- Verificar os prompts da sua equipe para impedir que chaves de API sejam coladas por acidente
- Resumir chats para criar memórias persistentes automaticamente
- Executar uma validação personalizada quando um turno do chat terminar, garantindo o cumprimento dos padrões
- Personalizar a criação de prompts quando estiver em um diretório específico

Durante a execução, considere o seguinte:

- Todos os ganchos correspondentes dos diferentes arquivos são executados.
- Vários ganchos de comando que correspondem ao mesmo evento são iniciados simultaneamente,
por isso um gancho não pode impedir que outro gancho correspondente seja iniciado.
- Ganchos não gerenciados precisam ser revisados e marcados como confiáveis antes de serem executados.

Os ganchos são executados em diferentes momentos de uma conversa:

| Quando                              | Ganchos                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Durante um turno                     | `PreToolUse`, `PermissionRequest`, `PostToolUse`, `PreCompact`, `PostCompact`, `UserPromptSubmit`, `SubagentStop`, `Stop` |
| Quando você interrompe um turno ativo | `Interrupt` (não é executado para subagentes)                                                                                   |
| Quando uma sessão ou um subagente inicia | `SessionStart`, `SubagentStart`                                                                                           |
| Quando a conversa principal termina         | `SessionEnd` (não é executado para subagentes)                                                                                  |

## Onde o Codex procura ganchos

O Codex encontra ganchos junto às camadas de configuração ativas em uma destas formas:

- `hooks.json`
- tabelas `[hooks]` definidas diretamente em `config.toml`

Os plug-ins instalados também podem incluir configurações do ciclo de vida por meio do manifesto
do plug-in ou de um arquivo `hooks/hooks.json` padrão. Consulte [Criar
plug-ins](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks) para ver as regras
de empacotamento de plug-ins.

Na prática, estes são os quatro locais mais úteis:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Se houver mais de uma origem de ganchos, o Codex carrega todos os ganchos correspondentes.
As camadas de configuração com maior precedência não substituem os ganchos das camadas de menor precedência.
Se uma única camada contiver tanto `hooks.json` quanto tabelas `[hooks]` definidas diretamente nela, o Codex
mescla as duas formas e exibe um aviso na inicialização. Prefira uma única representação por camada.

O Codex também pode encontrar ganchos incluídos em plug-ins ativados. Esses ganchos são carregados
junto com ganchos de outras origens e seguem o mesmo processo de revisão e atribuição de confiança
que os demais ganchos não gerenciados.

Os ganchos locais do projeto só são carregados quando a camada `.codex/` do projeto é considerada confiável. Em
projetos não confiáveis, o Codex ainda carrega ganchos do usuário e do sistema das respectivas
camadas de configuração ativas.

## Revisar ganchos e marcá-los como confiáveis

O Codex lista os ganchos configurados antes de decidir quais podem ser executados. Antes de executar um
gancho não gerenciado, o Codex exige que você revise a definição exata do gancho e a marque como confiável.
O Codex vincula esse registro de confiança ao hash atual do gancho. Assim, ganchos novos ou alterados
são marcados para revisão e não são executados até serem considerados confiáveis.

Use `/hooks` na CLI para inspecionar as origens dos ganchos, revisar ganchos novos ou alterados,
marcá-los como confiáveis ou desativar ganchos não gerenciados individualmente. Se os ganchos precisarem de revisão na
inicialização, o Codex exibirá um aviso orientando você a abrir `/hooks`.

Ganchos gerenciados provenientes do sistema, do MDM, da nuvem ou de `requirements.toml` são marcados
como gerenciados, considerados confiáveis por política e não podem ser desativados no navegador de ganchos do usuário.

Para uma automação pontual que já valida as origens dos ganchos fora do Codex, passe
`--dangerously-bypass-hook-trust` para executar os ganchos ativados sem exigir
um registro persistente de confiança nos ganchos para essa execução.

## Estrutura da configuração

Os ganchos são organizados em três níveis:

- Um evento de gancho, como `PreToolUse`, `PostToolUse`, `PreCompact`,
`SubagentStart` ou `Stop`
- Um grupo de critérios de correspondência que determina quando esse evento se aplica
- Um ou mais manipuladores de gancho executados quando os critérios do grupo são atendidos

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

Observações:

- `description` é um metadado opcional no nível superior de um arquivo `hooks.json`. Ele
  não altera quais ganchos são executados.
- `timeout` é expresso em segundos.
- Se `timeout` for omitido, o Codex usa `600` segundos para a maioria dos ganchos.
  - `SessionEnd` e `Interrupt` usam `1` segundo por padrão e aceitam até `3` segundos.
- `statusMessage` é opcional.
- `additionalContextLimit` define quanto conteúdo de `additionalContext` um gancho de comando pode
  enviar ao modelo antes de o Codex salvar o texto completo em disco e enviar uma prévia mais curta
  em seu lugar. Consulte [Saída extensa de ganchos](#large-hook-output).
- `commandWindows` permite substituir o comando apenas no Windows e é opcional. Em TOML, use
`command_windows` ou `commandWindows`.
- Defina `async` como `true` para [executar um gancho de comando em
  segundo plano](#run-hooks-in-the-background).
- Há suporte a manipuladores `command` e `mcp_tool`. Os manipuladores `prompt` e `agent`
  são analisados sintaticamente, mas ignorados.
- Os comandos são executados usando o `cwd` da sessão como diretório de trabalho.
- Para ganchos locais do repositório, prefira resolver caminhos a partir da raiz do repositório Git, em vez de usar um
  caminho relativo como `.codex/hooks/...`. O Codex pode ser iniciado em um
  subdiretório, e um caminho baseado na raiz do repositório Git mantém estável a localização do gancho.

Configuração TOML equivalente definida diretamente em `config.toml`:

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## Ganchos de ferramentas MCP

Um gancho de ferramenta MCP permite que um evento do ciclo de vida chame uma ferramenta em um servidor MCP já conectado.
Ele envia argumentos estruturados diretamente à ferramenta e usa o mesmo processo de revisão e atribuição de confiança
e o mesmo contrato de saída de um gancho de comando.

### Configurar um gancho de ferramenta MCP

Este gancho solicita ao servidor MCP `scanner` que verifique cada patch após o Codex gravar ou
editar arquivos:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| Campo           | Significado                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | Deve ser `mcp_tool`.                                              |
| `server`        | Nome obrigatório de um servidor MCP já conectado.                |
| `tool`          | Nome obrigatório de uma ferramenta exposta por esse servidor.                  |
| `input`         | Objeto JSON opcional com modelos de argumentos. O padrão é `{}`.    |
| `timeout`       | Tempo limite opcional de execução ativa, em segundos. O padrão é `600`. |
| `statusMessage` | Mensagem opcional exibida enquanto o gancho é executado.                      |

### Expandir argumentos a partir do evento do gancho

Use `${field.nested}` para ler um campo do evento do gancho usando notação de ponto. Um marcador de posição
que ocupa todo o valor mantém seu tipo JSON. Um marcador de posição dentro de uma string maior
é renderizado como texto. O Codex expande objetos e arrays recursivamente.

Para um evento que contém `{"tool_input":{"file_path":"src/main.rs","count":3}}`,
este modelo de argumentos:

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

torna-se:

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### Execução e ciclo de vida

- Os ganchos usam uma conexão MCP existente. Eles não iniciam nem reconectam servidores.
- Um gancho pode bloquear uma operação quando a ferramenta retorna uma decisão de bloqueio.
Erros, servidores ausentes e ferramentas indisponíveis não bloqueiam a operação.
- Os ganchos de ferramentas MCP são executados de forma síncrona. Eles não solicitam aprovação para usar ferramentas nem acionam
outros ganchos.
- Aplica-se o menor tempo limite entre o gancho e o servidor. O tempo de espera por uma
resposta de elicitação MCP não é contabilizado nesse limite.
- Os ganchos `SessionStart` podem ser executados antes que um servidor MCP esteja pronto. Se isso acontecer,
  eles não bloqueiam a sessão.
- `SessionEnd` não oferece suporte a ganchos de ferramentas MCP.

## Desativar ganchos

Os ganchos são ativados por padrão. Para desativá-los em `config.toml`, defina:

```toml
[features]
hooks = false

Use `hooks` como a chave canônica do recurso. `codex_hooks` ainda funciona como um
nome alternativo obsoleto. Os administradores podem forçar a desativação dos ganchos da mesma forma em
`requirements.toml` com `[features].hooks = false`.

## Ganchos gerenciados de `requirements.toml`

Os requisitos gerenciados pela empresa também podem definir ganchos diretamente em `[hooks]`.
Isso é útil quando os administradores querem impor a configuração dos ganchos e, ao mesmo tempo,
distribuir os scripts por MDM ou outro sistema de gerenciamento de dispositivos.
Para impor ganchos gerenciados mesmo para usuários que desativaram os ganchos localmente, fixe
`[features].hooks = true` em `requirements.toml` junto com `[hooks]`. Para ignorar
ganchos de usuário, projeto, sessão e plug-ins, mas ainda permitir ganchos
gerenciados pelo administrador, defina `allow_managed_hooks_only = true`.

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

Observações sobre ganchos gerenciados:

- `managed_dir` é usado no macOS e no Linux.
- `windows_managed_dir` é usado no Windows.
- O Codex não distribui os scripts em `managed_dir`; as ferramentas da sua empresa
  devem instalá-los e atualizá-los separadamente.
- Os comandos de ganchos gerenciados devem usar caminhos absolutos para scripts dentro do
diretório gerenciado configurado.
- `allow_managed_hooks_only = true` ignora ganchos de usuário, projeto, sessão e
  plug-ins, mas ainda carrega os ganchos gerenciados de `requirements.toml` e de
  outras camadas de configuração gerenciadas.

## Ganchos incluídos em plug-ins

Quando um plug-in é ativado, o Codex pode carregar ganchos de ciclo de vida desse plug-in
junto com ganchos de usuário, de projeto e gerenciados.

Por padrão, o Codex procura `hooks/hooks.json` na raiz do plug-in. O manifesto de um plug-in
pode substituir esse padrão com uma entrada `hooks` em
`.codex-plugin/plugin.json`. A entrada do manifesto pode ser um caminho com o prefixo `./`, um
array de caminhos com o prefixo `./`, um objeto de ganchos definido diretamente no manifesto ou um
array desses objetos.

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

Os caminhos dos ganchos no manifesto são resolvidos em relação à raiz do plug-in e devem permanecer
dentro dessa raiz. Se um manifesto definir `hooks`, o Codex usa essas entradas do manifesto
em vez do arquivo padrão `hooks/hooks.json`.

Os comandos dos ganchos de plug-ins recebem estas variáveis do ambiente:

- `PLUGIN_ROOT` é uma extensão específica do Codex que aponta para a raiz do plug-in
  instalado.
- `PLUGIN_DATA` é uma extensão específica do Codex que aponta para o diretório de dados do plug-in
  com permissão de gravação.
- O Codex também define `CLAUDE_PLUGIN_ROOT` e `CLAUDE_PLUGIN_DATA` para
  manter a compatibilidade com ganchos de plug-ins existentes.

Os ganchos de plug-ins usam o mesmo esquema de eventos que os outros ganchos. Instalar ou ativar um
plug-in não torna seus ganchos automaticamente confiáveis; o Codex ignora os ganchos incluídos no plug-in
até que você revise a definição atual do gancho e a marque como confiável.

## Padrões de correspondência

O campo `matcher` é uma string com uma expressão regular que filtra quando os ganchos são acionados. Use `"*"`,
`""` ou omita completamente `matcher` para corresponder a todas as ocorrências de um
evento com suporte.

Somente alguns eventos atuais do Codex levam `matcher` em conta:

| Evento               | O que `matcher` filtra | Observações                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | nome da ferramenta              | Há suporte para `Bash`, `apply_patch`\* e nomes de ferramentas MCP |
| `PostToolUse`       | nome da ferramenta              | Consulte [Cobertura de ferramentas](#tool-coverage)                          |
| `PostCompact`       | acionador da compactação     | Os valores são `manual` ou `auto`                                |
| `PreCompact`        | acionador da compactação     | Os valores são `manual` ou `auto`                                |
| `PreToolUse`        | nome da ferramenta              | Consulte [Cobertura de ferramentas](#tool-coverage)                          |
| `SessionEnd`        | motivo do encerramento             | No momento, somente `other`                                       |
| `SessionStart`      | origem da inicialização           | Os valores são `startup`, `resume`, `clear` e `compact`       |
| `SubagentStart`     | tipo de subagente          | Os valores dependem do subagente que inicia a execução                    |
| `SubagentStop`      | tipo de subagente          | Os valores dependem do subagente que encerra a execução                     |
| `UserPromptSubmit`  | sem suporte          | Qualquer `matcher` configurado é ignorado neste evento           |
| `Stop`              | sem suporte          | Qualquer `matcher` configurado é ignorado neste evento           |
| `Interrupt`         | sem suporte          | Qualquer `matcher` configurado é ignorado neste evento           |

\*Para `apply_patch`, os valores de `matcher` também podem ser `Edit` ou `Write`.

Exemplos:

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### Cobertura de ferramentas

`PreToolUse` e `PostToolUse` podem monitorar mais do que chamadas de shell e MCP. A maioria das
ferramentas de função locais usa o mesmo caminho de execução dos ganchos, então você pode usar o nome da ferramenta como critério de correspondência,
inspecionar seus argumentos JSON e, no caso de `PreToolUse`, bloquear ou reescrever a chamada.

| Caminho de execução da ferramenta                         | `PreToolUse` | `PostToolUse` | Observações                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Comandos de shell                    | Sim          | Sim           | Use `Bash` como critério de correspondência.                                                                                                         |
| Execução unificada (`exec_command`)     | Sim          | Sim           | Use `Bash` como critério de correspondência. Uma consulta posterior com `write_stdin` pode entregar o evento `PostToolUse` do comando original quando esse comando terminar. |
| `apply_patch`                     | Sim          | Sim           | Use `apply_patch`, `Edit` ou `Write` como critério de correspondência.                                                                              |
| Ferramentas MCP                         | Sim          | Sim           | Use o nome da ferramenta MCP, como `mcp__filesystem__read_file`, como critério de correspondência.                                                           |
| Outras ferramentas de função locais        | Sim          | Sim           | Use o nome da ferramenta de função, como `update_plan`, como critério de correspondência. `spawn_agent` também corresponde a `Agent`.                                 |
| Ferramentas hospedadas, como `WebSearch` | Não           | Não            | Essas ferramentas não usam o caminho de execução dos ganchos das ferramentas de função locais.                                                                       |

`write_stdin` fornece o transporte para uma sessão de execução unificada existente. Ele não executa
`PreToolUse` novamente ao enviar dados de entrada ou consultar um comando que já passou por
`PreToolUse`.

Alguns caminhos especializados de execução de ferramentas podem não usar o caminho padrão dos ganchos. Trate os ganchos
de ferramentas como uma proteção útil, não como uma garantia de que todas as regras serão aplicadas.

## Campos comuns de entrada

Cada gancho de comando recebe um objeto JSON em `stdin`.

Estes são os campos compartilhados que você geralmente usará:

| Campo             | Tipo             | Significado                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | ID da sessão atual do Codex. Os ganchos de subagentes usam o ID da sessão pai. |
| `transcript_path` | `string \| null` | Caminho do arquivo de transcrição da sessão, se houver                         |
| `cwd`             | `string`         | Diretório de trabalho da sessão                                   |
| `hook_event_name` | `string`         | Nome do evento de gancho atual                                             |
| `model`           | `string`         | Extensão específica do Codex. Slug do modelo ativo                         |

Os ganchos com escopo de turno listam `turn_id` como uma extensão específica do Codex nas
tabelas dos respectivos eventos.

`SessionStart`, `PreToolUse`, `PermissionRequest`, `PostToolUse`,
`UserPromptSubmit`, `SubagentStart`, `SubagentStop`, `Stop` e `Interrupt` também incluem
`permission_mode`, que descreve o modo de permissão atual como `default`,
`acceptEdits`, `plan`, `dontAsk` ou `bypassPermissions`.

`transcript_path` aponta para uma transcrição do chat por conveniência, mas o
formato da transcrição não é uma interface estável para ganchos e pode mudar com o tempo.

Se precisar do formato completo dos dados transmitidos, consulte [Esquemas](#schemas).

## Campos comuns de saída

`SessionStart`, `PreCompact`, `PostCompact`, `UserPromptSubmit`,
`SubagentStop` e `Stop` oferecem suporte a estes campos JSON compartilhados. `SubagentStart`
aceita a mesma estrutura para `systemMessage` e para o contexto específico do gancho, mas
`continue: false` não interrompe o subagente:

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| Campo            | Efeito                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | Se for `false`, marca essa execução do gancho como interrompida      |
| `stopReason`     | Registrado como motivo da interrupção             |
| `systemMessage`  | Exibido como aviso na interface ou no fluxo de eventos |
| `suppressOutput` | Analisado sintaticamente, mas ainda não implementado            |

O encerramento com código `0` e sem saída é considerado bem-sucedido, e o Codex continua.

`PreToolUse` e `PermissionRequest` oferecem suporte a `systemMessage`, mas atualmente não há suporte a `continue`,
`stopReason` e `suppressOutput` nesses eventos.
Se um gancho `PreToolUse` retornar um desses campos sem suporte, o Codex marca
essa execução do gancho como malsucedida, informa o erro e prossegue com a chamada da ferramenta.

`PostToolUse` oferece suporte a `systemMessage`, `continue: false` e `stopReason`.
`suppressOutput` é analisado sintaticamente, mas atualmente não há suporte a esse campo nesse evento.

### Saídas extensas de ganchos

Por padrão, o Codex limita cada mensagem de saída de gancho visível ao modelo a aproximadamente
2.500 tokens. Se um gancho retornar mais conteúdo, o Codex salva o texto completo em
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt` e fornece ao modelo uma
prévia com o início e o fim do conteúdo, junto com o caminho do arquivo salvo. Esse comportamento é chamado de
**transferência para disco**: o Codex armazena em disco as saídas acima do limite e as substitui por uma
prévia mais curta, visível ao modelo. Se não for possível gravar o arquivo, o modelo ainda
recebe uma prévia truncada.

  Mantenha conciso o contexto fornecido por ganchos e plug-ins. O contexto de vários ganchos e plug-ins
  se acumula e pode prejudicar o desempenho do modelo. Aumentar `additionalContextLimit`
  eleva esse risco. Evite definir o limite como `0`, a menos que o gancho imponha um
  limite máximo rígido à saída; caso contrário, um único gancho poderá consumir toda a janela de
  contexto.

Para qualquer gancho de comando que retorne `additionalContext`, defina
`additionalContextLimit` no manipulador para personalizar o limite aproximado de
tokens:

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

Omita `additionalContextLimit` para usar o limite padrão de `2500` tokens. Use um
número inteiro positivo para selecionar outro limite ou `0` para repassar todo o contexto adicional do manipulador
diretamente ao modelo. O Codex avalia cada
manipulador correspondente de forma independente. Nos eventos que não podem gerar contexto
adicional, o Codex ignora `additionalContextLimit` e emite um
aviso de configuração.

A configuração se aplica somente a `additionalContext`. O feedback de ferramentas e os prompts de continuação
mantêm o limite padrão.

Como saídas acima do limite podem ser gravadas em disco, evite retornar segredos ou
outros dados sensíveis na saída do gancho.

## Executar ganchos em segundo plano

Por padrão, o Codex aguarda a conclusão de um gancho de comando antes de continuar a
operação que o acionou. Defina `async` como `true` para executar um gancho de comando em
segundo plano enquanto o Codex continua.

### Configure um gancho em segundo plano

Adicione `"async": true` a um manipulador de comando em `hooks.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

Para um gancho definido diretamente em `config.toml`, defina `async = true`:

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

A entrada, o critério de correspondência, a revisão de confiança, o tempo limite e o
[tratamento de saídas grandes](#large-hook-output) são os mesmos nos ganchos em segundo plano e nos ganchos de comando síncronos. Assim como
nos outros ganchos de comando, `timeout` é medido em segundos e tem o valor padrão
`600`. Os ganchos `Interrupt` usam um segundo como padrão e três segundos como limite máximo,
inclusive quando são executados em segundo plano.

### Como os ganchos em segundo plano são executados

Quando um gancho em segundo plano termina, o Codex entrega a saída informativa compatível
no próximo ponto seguro da conversa:

- Se houver um turno ativo, o Codex aguarda a conclusão da solicitação atual ao modelo e das chamadas de ferramentas.
Em seguida, disponibiliza a saída para a próxima solicitação ao modelo nesse
turno.
- Se nenhum turno estiver ativo, o Codex aguarda o próximo turno do usuário. A conclusão de um
gancho em segundo plano não inicia um novo turno.

Use a mesma saída JSON específica do evento que usaria em um gancho síncrono. O Codex adiciona
`additionalContext` ao contexto do modelo e exibe `systemMessage` como um
aviso.

  Os ganchos em segundo plano não podem bloquear, aprovar, reescrever nem controlar de outra forma a
operação que os acionou. Use ganchos síncronos para políticas de ferramentas,
decisões de permissão, rejeição de prompts ou continuação de turnos.

### Limitações

- O Codex executa até oito ganchos em segundo plano simultaneamente por sessão. Os ganchos
adicionais aguardam até que um gancho em execução termine.
- Cada chamada correspondente é executada de forma independente, e os ganchos em segundo plano podem terminar
em uma ordem diferente daquela em que foram iniciados.
- Quando a sessão termina, o Codex cancela os ganchos em segundo plano que ainda não foram concluídos e descarta
a saída que ainda não foi entregue.
- Os ganchos `SessionEnd` sempre são executados de forma síncrona.

## Ganchos

### SessionStart

`matcher` é aplicado a `source` neste evento.

Além dos [campos de entrada comuns](#common-input-fields), há estes campos:

| Campo    | Tipo     | Significado                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | Como a sessão foi iniciada: `startup`, `resume`, `clear` ou `compact` |

O texto simples em `stdout` é adicionado como contexto adicional do desenvolvedor.

O JSON em `stdout` aceita os [campos de saída comuns](#common-output-fields) e esta
estrutura específica do gancho:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

Esse texto de `additionalContext` é adicionado como contexto adicional do desenvolvedor.

Depois que o Codex compacta uma sessão raiz, os ganchos `SessionStart` que correspondem a
`source: "compact"` são executados antes da próxima solicitação ao modelo. Isso também se aplica quando
a compactação automática ocorre no meio de um turno: o Codex entrega o contexto
adicional do gancho à continuação imediata, em vez de aguardar um
turno posterior do usuário. Se o gancho retornar `continue: false`, o Codex encerra o turno
sem enviar outra solicitação ao modelo.

### SessionEnd

`SessionEnd` permite executar um comando quando uma sessão termina, por exemplo, para salvar as
notas finais ou limpar arquivos. Ele é executado para a conversa principal quando você arquiva ou
exclui uma conversa que ainda está aberta, quando o Codex é encerrado normalmente ou depois que uma
conversa fica inativa e não está aberta em nenhum cliente conectado por 30
minutos. Ele não é executado para subagentes.

Sair de uma conversa ou chamar `thread/unsubscribe` não encerra
a sessão imediatamente, por isso `SessionEnd` não é executado de imediato. Seu gancho ainda pode
ler a transcrição da sessão durante a execução.

`matcher` filtra `reason` neste evento. Por enquanto, `reason` é sempre `other`.
Você pode omitir `matcher` ou usar `other` para executar o gancho em todos os eventos `SessionEnd`.

Além dos [campos de entrada comuns](#common-input-fields), há estes campos:

| Campo    | Tipo     | Significado                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | Motivo do encerramento da sessão: `other` |

Por exemplo, um comando `SessionEnd` recebe:

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

Os ganchos `SessionEnd` sempre são executados de forma síncrona, mesmo quando `async` é `true`. Eles
têm caráter apenas informativo, portanto sua saída não orienta o Codex nem mantém a conversa aberta. Se um
comando atingir o tempo limite ou terminar com erro, o Codex relata isso como uma falha do gancho.

### SubagentStart

`matcher` é aplicado a `agent_type` neste evento.

Além dos [campos de entrada comuns](#common-input-fields), há estes campos:

| Campo             | Tipo     | Significado                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Extensão específica do Codex. ID do turno ativo do Codex |
| `agent_id`        | `string` | Identificador do subagente                    |
| `agent_type`      | `string` | Tipo ou perfil do subagente                       |
| `permission_mode` | `string` | Modo de permissão atual                        |

O texto simples em `stdout` é adicionado como contexto adicional do desenvolvedor para o subagente.

O JSON em `stdout` aceita `systemMessage` e esta estrutura específica do gancho:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

Esse texto de `additionalContext` é adicionado como contexto adicional do desenvolvedor para o
subagente. `continue: false` é analisado para fins de compatibilidade, mas não impede que o
subagente seja iniciado.

### PreToolUse

`PreToolUse` pode interceptar Bash, edições de arquivos realizadas por meio de `apply_patch`,
chamadas de ferramentas MCP e outras ferramentas de função locais. Consulte [Cobertura de
ferramentas](#tool-coverage) para ver os caminhos compatíveis e as exceções.

`matcher` é aplicado a `tool_name` e aos nomes alternativos usados na correspondência. Para edições de arquivos por meio de
`apply_patch`, os valores de `matcher` podem ser `apply_patch`, `Edit` ou `Write`; a entrada do gancho
continua informando `tool_name: "apply_patch"`.

Além dos [campos de entrada comuns](#common-input-fields), há estes campos:

| Campo         | Tipo         | Significado                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Extensão específica do Codex. ID do turno ativo do Codex                                                                                   |
| `tool_name`   | `string`     | Nome canônico da ferramenta no gancho, como `Bash`, `apply_patch` ou um nome MCP como `mcp__fs__read`                                     |
| `tool_use_id` | `string`     | ID da chamada de ferramenta para esta invocação                                                                                                 |
| `tool_input`  | `JSON value` | Entrada específica da ferramenta. `Bash` e `apply_patch` usam `tool_input.command`. As ferramentas MCP e outras ferramentas de função locais enviam seus argumentos. |

O texto simples em `stdout` é ignorado.

O JSON em `stdout` pode usar `systemMessage`. Para negar uma chamada de ferramenta compatível, retorne
esta estrutura específica do gancho:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

O Codex também aceita esta estrutura de bloqueio mais antiga:

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

Você também pode usar o código de saída `2` e gravar o motivo do bloqueio em `stderr`.

Para adicionar contexto visível para o modelo sem bloquear a chamada, retorne
`hookSpecificOutput.additionalContext`:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

Para reescrever uma chamada de ferramenta compatível sem bloqueá-la, retorne
`permissionDecision: "allow"` com `updatedInput`:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Para comandos Bash e `apply_patch`, `updatedInput` deve incluir um campo
`command` do tipo string. Para MCP e outras ferramentas de função locais, `updatedInput` é o
objeto de argumentos substituto. Retorne `updatedInput` apenas com
`permissionDecision: "allow"`; outros formatos de `updatedInput` são relatados como
erros.

`permissionDecision: "ask"`, a forma legada `decision: "approve"`, `continue: false`,
`stopReason` e `suppressOutput` são analisados sintaticamente, mas ainda não têm suporte. O Codex marca
a execução do gancho como malsucedida, relata o erro e dá continuidade à chamada de ferramenta.

### PermissionRequest

`PermissionRequest` é executado quando o Codex está prestes a pedir aprovação, como para uma
elevação de permissões no shell ou uma aprovação de acesso à rede gerenciada. Ele pode permitir a solicitação, negá-la
ou se abster de decidir e deixar que o prompt normal de aprovação prossiga.
Ele não é executado para comandos que não precisam de aprovação.

`matcher` é aplicado a `tool_name` e aos nomes alternativos de correspondência. Os valores canônicos atuais
incluem `Bash`, `apply_patch` e nomes de ferramentas MCP, como
`mcp__server__tool`; `apply_patch` também corresponde a `Edit` e `Write`.

Outros campos, além dos [campos de entrada comuns](#common-input-fields):

| Campo                    | Tipo             | Significado                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Extensão específica do Codex. ID do turno ativo do Codex                                                                 |
| `tool_name`              | `string`         | Nome canônico da ferramenta no gancho, como `Bash`, `apply_patch` ou um nome de ferramenta MCP, como `mcp__fs__read`                   |
| `tool_input`             | `JSON value`     | Entrada específica da ferramenta. `Bash` e `apply_patch` usam `tool_input.command`, enquanto as ferramentas MCP enviam todos os argumentos. |
| `tool_input.description` | `string \| null` | Motivo da aprovação em linguagem natural, quando disponível no Codex                                                             |

O texto simples em `stdout` é ignorado.

Algumas entradas de ferramentas podem incluir uma descrição em linguagem natural, mas não presuma que o campo
`tool_input.description` esteja presente em todas as ferramentas.

Para aprovar a solicitação, retorne:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

Para negar a solicitação, retorne:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

Se vários ganchos correspondentes retornarem decisões, qualquer `deny` prevalece. Caso contrário,
`allow` permite que a solicitação prossiga sem exibir o prompt de aprovação. Se nenhum
gancho correspondente decidir, o Codex usa o fluxo normal de aprovação.

Não retorne `updatedInput`, `updatedPermissions` ou `interrupt` para
`PermissionRequest`; esses campos estão reservados para comportamentos futuros e, atualmente,
resultam em bloqueio por segurança.

### PostToolUse

`PostToolUse` é executado depois que as ferramentas compatíveis produzem saída, incluindo Bash,
`apply_patch`, chamadas de ferramentas MCP e outras ferramentas de função locais. No caso do Bash, ele
também é executado após comandos que terminam com status diferente de zero. Ele não pode desfazer os efeitos
colaterais de uma ferramenta que já foi executada. Consulte [Cobertura de ferramentas](#tool-coverage) para ver
os caminhos com suporte e as exceções.

`matcher` é aplicado a `tool_name` e aos nomes alternativos de correspondência. Para edições de arquivos por meio de
`apply_patch`, os valores de `matcher` podem ser `apply_patch`, `Edit` ou `Write`; a entrada do gancho
continua informando `tool_name: "apply_patch"`.

Outros campos, além dos [campos de entrada comuns](#common-input-fields):

| Campo           | Tipo         | Significado                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Extensão específica do Codex. ID do turno ativo do Codex                                                                                   |
| `tool_name`     | `string`     | Nome canônico da ferramenta no gancho, como `Bash`, `apply_patch` ou um nome de ferramenta MCP, como `mcp__fs__read`                                     |
| `tool_use_id`   | `string`     | ID da chamada de ferramenta desta invocação                                                                                                 |
| `tool_input`    | `JSON value` | Entrada específica da ferramenta. `Bash` e `apply_patch` usam `tool_input.command`. As ferramentas MCP e outras ferramentas de função locais enviam seus argumentos. |
| `tool_response` | `JSON value` | Saída específica da ferramenta. As ferramentas MCP enviam o resultado da chamada MCP. Outras ferramentas de função locais normalmente enviam a saída apresentada ao modelo.    |

O texto simples em `stdout` é ignorado.

O JSON em `stdout` pode usar `systemMessage` e esta estrutura específica do gancho:

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

Esse texto de `additionalContext` é adicionado como contexto adicional do desenvolvedor.

Neste evento, `decision: "block"` não desfaz o comando Bash já concluído.
Em vez disso, o Codex registra o feedback, substitui o resultado da ferramenta por esse
feedback e retoma a execução do modelo a partir da mensagem fornecida pelo gancho.

Você também pode usar o código de saída `2` e gravar o motivo do feedback em `stderr`.

Para interromper o processamento normal do resultado original da ferramenta depois que o comando
já tiver sido executado, retorne `continue: false`. O Codex substituirá o resultado da ferramenta pelo
seu feedback ou pelo texto de interrupção e continuará a partir daí.

`updatedMCPToolOutput` e `suppressOutput` são analisados sintaticamente, mas ainda não têm suporte.
O Codex marca a execução do gancho como malsucedida, relata o erro e continua o
processamento normal do resultado da ferramenta.

#### Chamadas de ferramentas no modo de código

Quando um modelo usa o modo de código para chamar uma ferramenta via JavaScript, as decisões dos ganchos se aplicam
a essa chamada aninhada. `PreToolUse` pode impedir a execução da ferramenta ou reescrever
sua entrada. Uma decisão de bloqueio de `PostToolUse` não pode desfazer os efeitos colaterais da ferramenta, mas
pode impedir que o resultado original chegue ao script em execução.

| Resultado do gancho                                                      | O que o modo de código vê                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` bloqueia                                              | A promessa da ferramenta é rejeitada antes da execução da ferramenta.                                                         |
| `PreToolUse` retorna `updatedInput`                              | A ferramenta é executada com a entrada reescrita, e a promessa é resolvida com esse resultado.                      |
| `PostToolUse` retorna `decision: "block"` ou termina com o código de saída `2` | A ferramenta é executada e, em seguida, a promessa é rejeitada com o motivo fornecido pelo gancho.                                          |
| `PostToolUse` retorna `continue: false`                          | O Codex usa o feedback do gancho como resultado visível para o modelo, mas não rejeita a promessa da chamada aninhada à ferramenta. |

### PreCompact

`PreCompact` é executado antes de o Codex compactar o chat. `matcher` é aplicado
a `trigger`, cujos valores são `manual` e `auto`.

Outros campos, além dos [campos de entrada comuns](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensão específica do Codex. ID do turno ativo do Codex |
| `trigger` | `string` | O que acionou a compactação: `manual` ou `auto`  |

O texto simples em `stdout` é ignorado.

O JSON em `stdout` oferece suporte aos [campos comuns de saída](#common-output-fields). Se um
gancho `PreCompact` correspondente retornar `continue: false`, o Codex para antes
da compactação.

### PostCompact

`PostCompact` é executado depois que o Codex compacta o chat. `matcher` é aplicado
a `trigger`, cujos valores são `manual` e `auto`.

Campos além dos [campos comuns de entrada](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensão específica do Codex. ID do turno ativo do Codex |
| `trigger` | `string` | O que acionou a compactação: `manual` ou `auto`  |

O texto simples em `stdout` é ignorado.

O JSON em `stdout` oferece suporte aos [campos comuns de saída](#common-output-fields). Se um
gancho `PostCompact` correspondente retornar `continue: false`, o Codex para após
a compactação.

### UserPromptSubmit

`matcher` não é usado atualmente para este evento.

Campos além dos [campos comuns de entrada](#common-input-fields):

| Campo     | Tipo     | Significado                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Extensão específica do Codex. ID do turno ativo do Codex |
| `prompt`  | `string` | Prompt do usuário que está prestes a ser enviado            |

O texto simples em `stdout` é adicionado como contexto adicional do desenvolvedor.

O JSON em `stdout` oferece suporte aos [campos comuns de saída](#common-output-fields) e
a esta estrutura específica do gancho:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

Esse texto de `additionalContext` é adicionado como contexto adicional do desenvolvedor.

Para bloquear o prompt, retorne:

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

Você também pode usar o código de saída `2` e gravar o motivo do bloqueio em `stderr`.

### SubagentStop

`matcher` é aplicado a `agent_type` neste evento.

Campos além dos [campos comuns de entrada](#common-input-fields):

| Campo                    | Tipo             | Significado                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Extensão específica do Codex. ID do turno ativo do Codex  |
| `agent_id`               | `string`         | Identificador do subagente                     |
| `agent_type`             | `string`         | Tipo ou perfil do subagente                        |
| `agent_transcript_path`  | `string \| null` | Caminho para o arquivo de transcrição do subagente, se houver    |
| `stop_hook_active`       | `boolean`        | Indica se a execução deste subagente já foi retomada     |
| `last_assistant_message` | `string \| null` | Mensagem mais recente do assistente do subagente, se disponível |

`SubagentStop` espera receber JSON em `stdout` ao encerrar com o código `0`. A saída em texto simples é
inválida para este evento.

O JSON em `stdout` oferece suporte aos [campos comuns de saída](#common-output-fields). Para pedir
ao Codex que continue o fluxo do subagente, retorne:

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

Você também pode usar o código de saída `2` e gravar o motivo da continuação em `stderr`.

Se algum gancho `SubagentStop` correspondente retornar `continue: false`, isso terá
precedência sobre as decisões de continuação de outros ganchos `SubagentStop`
correspondentes.

### Stop

`matcher` não é usado atualmente para este evento.

Campos além dos [campos comuns de entrada](#common-input-fields):

| Campo                    | Tipo             | Significado                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Extensão específica do Codex. ID do turno ativo do Codex    |
| `stop_hook_active`       | `boolean`        | Indica se este turno já foi retomado por `Stop` |
| `last_assistant_message` | `string \| null` | Texto da mensagem mais recente do assistente, se disponível       |

`Stop` espera receber JSON em `stdout` ao encerrar com o código `0`. A saída em texto simples é inválida
para este evento.

O JSON em `stdout` oferece suporte aos [campos comuns de saída](#common-output-fields). Para que
o Codex continue, retorne:

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

Você também pode usar o código de saída `2` e gravar o motivo da continuação em `stderr`.

Neste evento, `decision: "block"` não rejeita o turno. Em vez disso, instrui
o Codex a continuar e cria automaticamente um novo prompt de continuação que funciona
como um novo prompt do usuário, usando o valor de `reason` como texto desse prompt.

Se algum gancho `Stop` correspondente retornar `continue: false`, isso terá precedência
sobre as decisões de continuação de outros ganchos `Stop` correspondentes.

### Interrupt

`Interrupt` é executado quando você interrompe um turno ativo na conversa principal. Use-o
para registrar a interrupção ou realizar a limpeza do trabalho iniciado por um gancho. Ele não é executado
para conversas inativas nem para subagentes, e qualquer `matcher` configurado é ignorado.

Além dos [campos comuns de entrada](#common-input-fields), o evento inclui
`turn_id`, o ID do turno interrompido, e `permission_mode`.

Ganchos de comando têm um tempo limite de um segundo por padrão. Os tempos limite configurados ficam
restritos ao intervalo de um a três segundos. A saída do gancho não pode impedir a
interrupção nem reiniciar o turno. Encerre com o código `0` sem gerar saída ou retorne JSON com
um `systemMessage` opcional para exibir um aviso. A saída em texto simples é inválida
para este evento.

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## Esquemas

  Os esquemas da branch `main` indicados nos links podem incluir campos de ganchos que não fazem parte da
  versão atual. Use esta página como referência para o comportamento da versão.

Se precisar do formato de transmissão exato usado atualmente, consulte os esquemas gerados no
[repositório do Codex no GitHub](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated).
