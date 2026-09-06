<!-- source: https://learn.chatgpt.com/pt-BR/docs/app-server -->

O app-server do Codex é a interface que o Codex usa para dar suporte a clientes com recursos avançados, como a extensão do Codex para VS Code. Use-o quando quiser uma integração profunda com seu próprio produto: autenticação, histórico de conversas, aprovações e transmissão contínua de eventos do agente. A implementação do app-server é de código aberto e está disponível no repositório do Codex no GitHub ([openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)). Consulte a página [Código aberto](/pt-BR/codex/open-source) para ver a lista completa de componentes de código aberto do Codex.

  Se estiver automatizando tarefas ou executando o Codex em CI, use o
<a href="/codex/codex-sdk">SDK do Codex</a> em vez disso.

## Conecte a interface de terminal da CLI

O modo remoto da interface de terminal permite executar o app-server em uma máquina e conectar a
interface de terminal do Codex CLI a partir de outra. Inicie um ponto de escuta WebSocket:

```bash
codex app-server --listen ws://127.0.0.1:4500

Em seguida, conecte a interface de terminal:

```bash
codex --remote ws://127.0.0.1:4500

Para uma conexão não local, configure a autenticação WebSocket e proteja a
conexão com TLS. Armazene o token de portador em uma variável de ambiente e
informe o nome dela em vez de inserir o token na linha de comando:

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

A opção `--remote` aceita endpoints `ws://`, `wss://`, `unix://` e
`unix://PATH`. Use WebSockets sem TLS apenas em localhost ou em uma conexão com
encaminhamento de portas via SSH.

## Conecte um host remoto do modo Código

Por padrão, o app-server inicia um host local do modo Código. Para usar um host remoto
em vez disso, informe sua URL WebSocket segura:

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` controla a conexão de saída do app-server com seu host do
modo Código. Isso não altera `--listen`, que controla como os clientes se conectam ao
app-server. Todas as conversas do mesmo processo do app-server compartilham a conexão
selecionada com o host do modo Código.

Use `wss://` para um host remoto. Use `ws://` somente para uma conexão com localhost ou
encaminhada via SSH. O comando app-server e o transporte WebSocket são
experimentais e não têm suporte para cargas de trabalho em produção.

## Protocolo

Assim como o [MCP](https://modelcontextprotocol.io/), `codex app-server` oferece suporte à comunicação bidirecional por meio de mensagens JSON-RPC 2.0 (com o cabeçalho `"jsonrpc":"2.0"` omitido na transmissão).

Transportes compatíveis:

- `stdio` (`--listen stdio://`, padrão): JSON delimitado por quebras de linha (JSONL).
- `websocket` (`--listen ws://IP:PORT`, experimental e sem suporte): uma
  mensagem JSON-RPC por quadro de texto WebSocket.
- Socket Unix (`--listen unix://` ou `--listen unix://PATH`): conexões WebSocket
  pelo socket de controle padrão do app-server do Codex ou por um caminho personalizado de
  socket Unix, usando a negociação HTTP Upgrade padrão.
- `off` (`--listen off`): não expõe um transporte local.

Ao executar com `--listen ws://IP:PORT`, o mesmo ponto de escuta também atende a verificações básicas de
integridade via HTTP:

- `GET /readyz` retorna `200 OK` assim que o ponto de escuta passa a aceitar novas conexões.
- `GET /healthz` retorna `200 OK` quando o cabeçalho `Origin`
  não está presente na solicitação.
- Solicitações com o cabeçalho `Origin` são rejeitadas com `403 Forbidden`.

O transporte WebSocket é experimental e não tem suporte. Pontos de escuta locais, como
`ws://127.0.0.1:PORT`, são adequados para localhost e para fluxos de trabalho com encaminhamento de portas
via SSH. Durante a implantação gradual, os pontos de escuta WebSocket fora da interface de loopback permitem atualmente
conexões não autenticadas por padrão; portanto, configure a autenticação WebSocket antes de
expor um deles remotamente.

Opções de autenticação WebSocket compatíveis:

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

Para tokens de portador assinados, também é possível definir `--ws-issuer`, `--ws-audience` e
`--ws-max-clock-skew-seconds`. Os clientes apresentam a credencial como
`Authorization: Bearer <token>` durante a negociação inicial do WebSocket, e o app-server
exige autenticação antes da solicitação JSON-RPC `initialize`.

Prefira `--ws-token-file` em vez de passar tokens de portador brutos na linha de comando. Use
`--ws-token-sha256` somente quando o cliente mantiver o token bruto de alta entropia em um
armazenamento local de segredos separado; o hash é apenas um verificador, e os clientes ainda precisam
do token original.

No modo WebSocket, o app-server usa filas de capacidade limitada. Quando a fila de entrada de solicitações está cheia,
o servidor rejeita novas solicitações com o código de erro JSON-RPC `-32001` e a mensagem
`"Server overloaded; retry later."` Os clientes devem tentar novamente com um intervalo de espera que aumente
exponencialmente e inclua uma variação aleatória.

## Esquema de mensagens

As solicitações incluem `method`, `params` e `id`:

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

As respostas repetem o `id`, acompanhado de `result` ou `error`:

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

As notificações omitem o `id` e usam apenas `method` e `params`:

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

Você pode gerar um esquema TypeScript ou um pacote JSON Schema pela CLI. Cada saída é específica da versão do Codex executada, de modo que os artefatos gerados correspondem exatamente a essa versão:

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## Primeiros passos

1. Inicie o servidor com `codex app-server` (transporte stdio padrão),
`codex app-server --listen ws://127.0.0.1:4500` (WebSocket sobre TCP) ou
`codex app-server --listen unix://` (socket Unix padrão).
2. Conecte um cliente pelo transporte selecionado e envie `initialize`, seguido da notificação `initialized`.
3. Inicie uma conversa e um turno e continue lendo as notificações do fluxo de transporte ativo.

Exemplo (Node.js / TypeScript):

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## Primitivas fundamentais

- **Conversa**: Uma conversa entre um usuário e o agente do Codex. As conversas contêm turnos.
- **Turno**: Uma única solicitação do usuário e o trabalho do agente que vem a seguir. Os turnos contêm itens e transmitem atualizações incrementais.
- **Item**: Uma unidade de entrada ou saída (mensagem do usuário, mensagem do agente, execuções de comandos, alteração de arquivo, chamada de ferramenta e outros).

Use as APIs de conversa para criar, listar ou arquivar conversas. Conduza uma conversa com as APIs de turno e transmita o progresso por meio das notificações de turno.

## Visão geral do ciclo de vida

- **Inicialize uma vez por conexão**: Imediatamente após abrir uma conexão de transporte, envie uma solicitação `initialize` com os metadados do seu cliente e depois emita `initialized`. O servidor rejeita qualquer solicitação nessa conexão antes dessa negociação inicial.
- **Inicie (ou retome) uma conversa**: Chame `thread/start` para uma nova conversa, `thread/resume` para continuar uma conversa existente ou `thread/fork` para ramificar o histórico em um novo ID de conversa.
- **Inicie um turno**: Chame `turn/start` com o `threadId` de destino e a entrada do usuário. Os campos opcionais substituem as configurações de modelo, personalidade, `cwd`, política de sandbox e outras.
- **Oriente um turno ativo**: Chame `turn/steer` para acrescentar uma entrada do usuário ao turno em andamento, sem criar um novo turno.
- **Acompanhe o fluxo de eventos**: Após `turn/start`, continue lendo as notificações no stdout: `thread/archived`, `thread/unarchived`, `item/started`, `item/completed`, `item/agentMessage/delta`, o progresso das ferramentas e outras atualizações.
- **Conclua o turno**: O servidor emite `turn/completed` com o status final quando o modelo termina ou após um cancelamento por `turn/interrupt`.

## Inicialização

Os clientes devem enviar uma única solicitação `initialize` por conexão de transporte antes de invocar qualquer outro método nessa conexão e, em seguida, confirmar com uma notificação `initialized`. Solicitações enviadas antes da inicialização recebem um erro `Not initialized`, e chamadas repetidas a `initialize` na mesma conexão retornam `Already initialized`.

O servidor retorna a string de agente de usuário que apresentará aos serviços dos quais depende, além dos valores `platformFamily` e `platformOs`, que descrevem a plataforma de execução de destino. Defina `clientInfo` para identificar sua integração.

`initialize.params.capabilities` também oferece suporte às seguintes capacidades do cliente:

- `optOutNotificationMethods` - nomes exatos dos métodos de notificação que devem ser suprimidos nesta
  conexão. A correspondência é exata (sem curingas nem prefixos); nomes desconhecidos
  são aceitos e ignorados.
- `requestAttestation` - habilita o recebimento da solicitação `attestation/generate`
  iniciada pelo servidor. Hosts de desktop que fornecem atestação aos serviços dos quais dependem respondem com um
  valor opaco `{ "token": "..." }`.
- `mcpServerOpenaiFormElicitation` - permite que os servidores MCP acessados pelo app-server enviem
  a variante de `mcpServer/elicitation/request` com formulário estendido da OpenAI.

**Importante**: Use `clientInfo.name` para identificar seu cliente na Plataforma de logs de conformidade. Se estiver desenvolvendo uma nova integração do Codex para uso empresarial, entre em contato com a OpenAI para que ela seja adicionada a uma lista de clientes conhecidos. Para mais contexto, consulte a [referência de logs do Codex](https://chatgpt.com/public/admin/api-reference#tag/Codex).

Exemplo (da extensão do Codex para VS Code):

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

Exemplo com desativação de notificações:

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## Ativação da API experimental

Alguns métodos e campos do app-server exigem intencionalmente que a capacidade `experimentalApi` esteja habilitada.

- Omita `capabilities` (ou defina `experimentalApi` como `false`) para continuar usando a interface estável da API; nesse caso, o servidor rejeita métodos e campos experimentais.
- Defina `capabilities.experimentalApi` como `true` para habilitar métodos e campos experimentais.

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

Se um cliente enviar um método ou campo experimental sem habilitar os recursos experimentais, o app-server rejeitará a solicitação com:

`<descriptor> requires experimentalApi capability`

## Visão geral da API

- `thread/start` - cria uma nova conversa; emite `thread/started` e inscreve você automaticamente nos eventos de turnos/itens dessa conversa.
- `thread/resume` - reabre uma conversa existente pelo ID para que chamadas posteriores a `turn/start` acrescentem conteúdo a ela.
- `thread/fork` - cria um fork de uma conversa com um novo ID, copiando o histórico armazenado. Passe `lastTurnId` para copiar o histórico até esse turno, inclusive, e omitir os turnos posteriores, ou `ephemeral: true` para criar um fork em memória. Emite `thread/started` para a nova conversa; as conversas retornadas incluem `forkedFromId` quando disponível.
- `thread/read` - lê uma conversa armazenada pelo ID sem retomá-la; defina `includeTurns` para retornar o histórico completo de turnos. Os objetos `thread` retornados incluem o `status` de execução.
- `thread/list` - consulta os logs armazenados das conversas com paginação; oferece suporte à paginação por cursor e aos filtros `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly` e `searchTerm`, além dos filtros experimentais `parentThreadId` ou `ancestorThreadId`. Os objetos `thread` retornados incluem o `status` de execução.
- `thread/turns/list` - experimental; consulta com paginação o histórico de turnos de uma conversa armazenada sem retomá-la. `itemsView` controla se os itens dos turnos são omitidos, resumidos ou carregados integralmente.
- `thread/items/list` - experimental; consulta com paginação os itens persistidos de uma conversa, com a opção de restringir a consulta a um único `turnId`. O armazenamento de conversas em uso deve oferecer suporte à paginação de itens.
- `thread/loaded/list` - lista os IDs das conversas carregadas atualmente na memória.
- `thread/name/set` - define ou atualiza o nome da conversa exibido ao usuário, para uma conversa carregada ou um registro de execução persistido; emite `thread/name/updated`.
- `thread/goal/set` - define a meta de uma conversa; emite `thread/goal/updated`.
- `thread/goal/get` - lê a meta atual de uma conversa.
- `thread/goal/clear` - remove a meta de uma conversa; emite `thread/goal/cleared`.
- `thread/metadata/update` - atualiza parcialmente os metadados da conversa armazenados no SQLite, incluindo os valores persistidos de `gitInfo` e `isPinned`.
- `thread/archive` - move o arquivo de log de uma conversa para o diretório de arquivamento e tenta arquivar os logs das conversas descendentes originadas por ela que ainda não estejam arquivados; retorna `{}` em caso de sucesso e emite `thread/archived` para cada conversa arquivada.
- `thread/delete` - exclui permanentemente uma conversa persistida, ativa ou arquivada, e todas as conversas descendentes originadas por ela; retorna `{}` em caso de sucesso e emite `thread/deleted` para cada conversa excluída.
- `thread/unsubscribe` - cancela a inscrição desta conexão nos eventos de turnos/itens da conversa. Se esta era a última conexão inscrita, o servidor remove a conversa da memória após um período de tolerância sem atividade nem conexões inscritas e emite `thread/closed`.
- `thread/unarchive` - restaura o registro de execução de uma conversa arquivada para o diretório de sessões ativas; retorna o objeto `thread` restaurado e emite `thread/unarchived`.
- `thread/status/changed` - notificação emitida quando o `status` de execução de uma conversa carregada muda.
- `thread/compact/start` - aciona a compactação do histórico de uma conversa; retorna `{}` imediatamente, enquanto o progresso é transmitido por notificações `turn/*` e `item/*`.
- `thread/shellCommand` - executa um comando de shell iniciado pelo usuário e associado a uma conversa. A execução ocorre fora do sandbox, com acesso completo, e não herda a política de sandbox da conversa.
- `thread/backgroundTerminals/clean` - encerra todos os terminais em segundo plano em execução de uma conversa (experimental; requer `capabilities.experimentalApi`).
- `thread/backgroundTerminals/list` - lista os terminais em segundo plano em execução de uma conversa carregada (experimental; requer `capabilities.experimentalApi`).
- `thread/backgroundTerminals/terminate` - encerra um terminal em segundo plano em execução usando o `processId` do app-server (experimental; requer `capabilities.experimentalApi`).
- `thread/rollback` - obsoleto; remove os últimos N turnos do contexto em memória e persiste um marcador de reversão; retorna o objeto `thread` atualizado.
- `turn/start` - adiciona a entrada do usuário ou uma saída avulsa de ferramenta a uma conversa e inicia a geração pelo Codex; responde com o `turn` inicial e transmite eventos. Para `collaborationMode`, `settings.developer_instructions: null` significa "usar as instruções integradas do modo selecionado".
- `thread/inject_items` - acrescenta itens brutos da Responses API ao histórico visível para o modelo de uma conversa carregada, sem iniciar um turno do usuário.
- `turn/steer` - acrescenta a entrada do usuário ao turno ativo em andamento de uma conversa; retorna o `turnId` aceito.
- `turn/interrupt` - solicita o cancelamento de um turno em andamento; em caso de sucesso, retorna `{}`, e o turno termina com `status: "interrupted"`.
- `review/start` - inicia o revisor do Codex para uma conversa; emite os itens `enteredReviewMode` e `exitedReviewMode`.
- `command/exec` - executa um único comando no sandbox do servidor sem iniciar uma conversa nem um turno.
- `command/exec/write` - grava bytes em `stdin` de uma sessão `command/exec` em execução ou fecha `stdin`.
- `command/exec/resize` - redimensiona uma sessão `command/exec` em execução que usa PTY.
- `command/exec/terminate` - encerra uma sessão `command/exec` em execução.
- `command/exec/outputDelta` (notificação) - emitida para blocos de stdout/stderr codificados em base64 de uma sessão `command/exec` com saída transmitida continuamente.
- `process/spawn` - inicia explicitamente uma sessão de processo fora do sandbox do Codex (experimental; requer `capabilities.experimentalApi`).
- `process/writeStdin` - grava bytes em stdin de uma sessão `process/spawn` em execução ou fecha stdin (experimental).
- `process/resizePty` - redimensiona uma sessão de processo em execução que usa PTY (experimental).
- `process/kill` - encerra uma sessão de processo em execução (experimental).
- `process/outputDelta` e `process/exited` (notificações) - emitidas para transmitir continuamente a saída do processo e informar seu status de encerramento (experimental).
- `model/list` - lista os modelos disponíveis (defina `includeHidden: true` para incluir entradas com `hidden: true`), com opções de esforço, um `upgrade` opcional e `inputModalities`.
- `modelProvider/capabilities/read` - lê os limites de capacidade do provedor para combinações de modelo/provedor.
- `experimentalFeature/list` - lista sinalizadores de recursos com metadados do estágio do ciclo de vida e paginação por cursor.
- `experimentalFeature/enablement/set` - atualiza parcialmente as configurações de execução em memória para as chaves de recursos aceitas, como `apps` e `plugins`.
- `environment/info` - experimental; conecta-se a um ambiente de execução configurado e retorna o shell e o diretório de trabalho padrão desse ambiente.
- `permissionProfile/list` - lista os perfis de permissão em beta e indica se os requisitos efetivos permitem usá-los, com paginação por cursor.
- `collaborationMode/list` - lista predefinições do modo de colaboração (experimental, sem paginação).
- `skills/list` - lista habilidades para um ou mais valores de `cwd` (oferece suporte a `forceReload` e ao parâmetro opcional `perCwdExtraUserRoots`).
- `skills/extraRoots/set` - substitui, no nível do processo, os diretórios raiz adicionais usados para descobrir habilidades independentes, sem persisti-los.
- `skills/changed` (notificação) - emitida quando os arquivos locais de habilidades monitorados são alterados.
- `hooks/list` - lista os ganchos de ciclo de vida encontrados para um ou mais valores de `cwd`.
- `marketplace/add` - adiciona um marketplace remoto de plug-ins e o salva na configuração de marketplace do usuário.
- `marketplace/remove` - remove um marketplace configurado e, se existir, o diretório raiz da instalação desse marketplace.
- `marketplace/upgrade` - atualiza um marketplace Git configurado ou todos os marketplaces Git configurados quando o nome do marketplace é omitido.
- `plugin/list` - em desenvolvimento; lista os marketplaces de plug-ins encontrados e o estado dos plug-ins, incluindo metadados das políticas de instalação/autenticação, erros de carregamento de marketplaces, IDs de plug-ins em destaque e metadados de origem de plug-ins locais, baseados em Git, provenientes de registros de pacotes ou remotos. Os resumos podem incluir o valor remoto de `version`, o valor local de `localVersion`, ícones estruturados para os modos claro e escuro e o campo `installPolicySource`, que pode ser `null`, `WORKSPACE_SETTING` ou `IMPLICIT_CANONICAL_APP` nas entradas remotas atuais. Ainda não chame esse método em clientes de produção.
- `plugin/read` - em desenvolvimento; lê um plug-in pelo caminho do marketplace ou pelo nome do marketplace remoto e pelo nome do plug-in, incluindo as habilidades e os aplicativos incluídos no pacote, os nomes de servidores MCP e o `shareUrl` de um plug-in remoto, quando fornecido pelo catálogo remoto. Ainda não chame esse método em clientes de produção.
- `plugin/install` - em desenvolvimento; instala um plug-in a partir do caminho de um marketplace ou do nome de um marketplace remoto. Ainda não chame esse método em clientes de produção.
- `plugin/uninstall` - em desenvolvimento; desinstala um plug-in instalado. Ainda não chame esse método em clientes de produção.
- `plugin/skill/read` - lê sob demanda o Markdown de uma habilidade de um plug-in remoto usando o marketplace remoto, o ID do plug-in e o nome da habilidade.
- `app/installed` - lê o estado de execução dos aplicativos instalados, incluindo se cada aplicativo está efetivamente habilitado e pode ser chamado.
- `app/list` - lista os aplicativos disponíveis (conectores), com paginação e metadados de acesso e habilitação.
- `app/read` - obtém, para IDs específicos de aplicativos, metadados e resumos opcionais de ferramentas usados apenas para exibição.
- `skills/config/write` - habilita ou desabilita habilidades por caminho.
- `mcpServer/oauth/login` - inicia um login OAuth para um servidor MCP configurado; retorna uma URL de autorização e emite `mcpServer/oauthLogin/completed` ao concluir.
- `tool/requestUserInput` - apresenta ao usuário de 1 a 3 perguntas curtas para uma chamada de ferramenta (experimental); as perguntas podem definir `isOther` para oferecer uma opção de resposta livre.
- `mcpServer/elicitation/request` (requisição do servidor) - solicita ao cliente dados estruturados de formulário ou a confirmação de um fluxo via URL solicitado por um servidor MCP.
- `item/permissions/requestApproval` (requisição do servidor) - solicita ao cliente que conceda um subconjunto das permissões de rede ou de sistema de arquivos solicitadas pela ferramenta integrada `request_permissions`.
- `config/mcpServer/reload` - recarrega do disco a configuração do servidor MCP e coloca na fila uma atualização para as conversas carregadas.
- `mcpServerStatus/list` - lista servidores MCP, ferramentas, recursos e status de autenticação (paginação por cursor + limite). Use `detail: "full"` para obter os dados completos ou `detail: "toolsAndAuthOnly"` para omitir os recursos.
- `mcpServer/resource/read` - lê um único recurso MCP por meio de um servidor MCP inicializado.
- `mcpServer/tool/call` - chama uma ferramenta no servidor MCP configurado para uma conversa.
- `mcpServer/startupStatus/updated` (notificação) - é emitida quando o status de inicialização de um servidor MCP configurado muda para uma conversa carregada.
- `windowsSandbox/setupStart` - inicia a configuração do Sandbox do Windows para o modo `elevated` ou `unelevated`; retorna rapidamente e depois emite `windowsSandbox/setupCompleted`.
- `feedback/upload` - envia um relatório de feedback (classificação + motivo/logs opcionais + ID da conversa, além de anexos `extraLogFiles` opcionais).
- `config/read` - busca a configuração efetiva no disco após resolver as camadas de configuração.
- `externalAgentConfig/detect` - detecta artefatos de agentes externos que podem ser migrados usando `includeHome` e, opcionalmente, `cwds`; cada item detectado inclui `cwd` (`null` para o diretório pessoal).
- `externalAgentConfig/import` - aplica os itens selecionados de migração de agentes externos passando explicitamente `migrationItems` com `cwd` (`null` para o diretório pessoal). Os tipos de item aceitos incluem configuração, habilidades, `AGENTS.md`, plug-ins, configuração de servidor MCP, subagentes, ganchos, comandos e sessões; importações não vazias emitem `externalAgentConfig/import/progress` e `externalAgentConfig/import/completed` à medida que o trabalho é concluído. As importações de plug-ins e sessões podem ser concluídas de forma assíncrona.
- `config/value/write` - grava um único par chave/valor de configuração no arquivo `config.toml` do usuário no disco.
- `config/batchWrite` - aplica de forma atômica as alterações de configuração ao arquivo `config.toml` do usuário no disco.
- `configRequirements/read` - busca requisitos em `requirements.toml` e/ou no MDM, incluindo a configuração gerenciada exata, listas de permissões, valores fixados de `featureRequirements` e requisitos de rede (ou `null` se você não tiver configurado nenhum).
- `fs/readFile`, `fs/writeFile`, `fs/createDirectory`, `fs/getMetadata`, `fs/readDirectory`, `fs/remove`, `fs/copy`, `fs/watch`, `fs/unwatch` e `fs/changed` (notificação) - operam em caminhos absolutos do sistema de arquivos por meio da API v2 de sistema de arquivos do app-server.

Os resumos dos plug-ins incluem um campo `source` de tipo união. Os plug-ins locais retornam
`{ "type": "local", "path": ... }`, as entradas de marketplace baseadas em Git retornam
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }`,
as entradas de registros de pacotes retornam
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }` e
as entradas de catálogos remotos retornam `{ "type": "remote" }`. Para entradas de catálogos disponíveis apenas
remotamente, `PluginMarketplaceEntry.path` pode ser `null`; passe
`remoteMarketplaceName` em vez de `marketplacePath` ao ler ou instalar
esses plug-ins.

## Modelos

### Listar modelos (`model/list`)

Chame `model/list` para descobrir os modelos disponíveis e suas capacidades antes de renderizar seletores de modelo ou personalidade.

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

Cada entrada de modelo pode incluir:

- `supportedReasoningEfforts` - opções de esforço de raciocínio aceitas pelo modelo.
- `defaultReasoningEffort` - esforço de raciocínio padrão sugerido para os clientes.
- `upgrade` - ID opcional do modelo recomendado para atualização, usado em prompts de migração nos clientes.
- `upgradeInfo` - metadados opcionais de atualização para prompts de migração nos clientes.
- `hidden` - indica se o modelo fica oculto na lista padrão do seletor.
- `inputModalities` - tipos de entrada aceitos pelo modelo (por exemplo, `text`, `image`).
- `supportsPersonality` - indica se o modelo aceita instruções específicas de personalidade, como `/personality`.
- `isDefault` - indica se o modelo é o padrão recomendado.

Por padrão, `model/list` retorna apenas os modelos visíveis no seletor. Defina `includeHidden: true` se precisar da lista completa e quiser filtrá-la no cliente usando `hidden`.

Quando `inputModalities` não estiver presente (em catálogos de modelos mais antigos), trate-o como `["text", "image"]` para manter a compatibilidade com versões anteriores.

### Listar recursos experimentais (`experimentalFeature/list`)

Use este endpoint para descobrir sinalizadores de recursos com metadados e estágio do ciclo de vida:

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` pode ser `beta`, `underDevelopment`, `stable`, `deprecated` ou `removed`. Para sinalizadores que não estejam em beta, `displayName`, `description` e `announcement` podem ser `null`.

### Inspecionar um ambiente de execução (experimental)

Use `environment/info` para inspecionar um ambiente remoto configurado antes de
começar a trabalhar nele. O método exige `capabilities.experimentalApi = true`.

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` pode ser `null`. Quando presente, é um URI `file:` canônico que usa a
sintaxe de caminho nativa do ambiente. IDs de ambiente desconhecidos e falhas de conexão ou
de protocolo retornam erros de requisição.

## Conversas

- `thread/read` lê uma conversa armazenada sem se inscrever nela; defina `includeTurns` para incluir os turnos.
- `thread/turns/list` é experimental e consulta de forma paginada o histórico de turnos de uma conversa armazenada sem
  retomá-la. Use `itemsView` para escolher se os itens dos turnos serão omitidos,
  resumidos ou carregados por completo.
- `thread/items/list` é experimental e consulta de forma paginada os itens persistidos de uma conversa, com a opção de restringir os resultados a um único turno.
- `thread/list` oferece paginação por cursor e filtragem por `modelProviders`, `sourceKinds`, `archived`, `isPinned`, `cwd`, `useStateDbOnly` e `searchTerm`, além de filtragem experimental por `parentThreadId` ou `ancestorThreadId`.
- `thread/loaded/list` retorna os IDs das conversas que estão atualmente na memória.
- `thread/archive` move o log JSONL persistido da conversa para o diretório de arquivamento e tenta arquivar os logs das conversas descendentes geradas que ainda não estejam arquivados.
- `thread/delete` exclui permanentemente uma conversa persistida, ativa ou arquivada, e as conversas descendentes geradas a partir dela.
- `thread/metadata/update` atualiza os metadados armazenados da conversa, incluindo os valores persistidos de `gitInfo` e `isPinned`.
- `thread/unsubscribe` cancela a inscrição da conexão atual em uma conversa carregada e pode acionar `thread/closed` após um período de tolerância à inatividade.
- `thread/unarchive` restaura o registro de execução de uma conversa arquivada no diretório de sessões ativas.
- `thread/compact/start` aciona a compactação e retorna `{}` imediatamente.
- `thread/rollback` está obsoleto. Ele remove os últimos N turnos do contexto em memória e registra um marcador de reversão no log JSONL persistido da conversa.
- `thread/inject_items` acrescenta itens brutos da Responses API ao histórico visível para o modelo de uma conversa carregada, sem iniciar um turno do usuário.

### Iniciar ou retomar uma conversa

Quando precisar de uma nova conversa com o Codex, inicie uma do zero.

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName` é opcional. Defina-o quando quiser que o app-server identifique as métricas da conversa com o nome do serviço da sua integração.

`thread/start`, `thread/resume` e `thread/fork` retornam
`instructionSources`, um array com os caminhos dos arquivos de instruções carregados. Cada caminho usa
a sintaxe nativa de caminhos absolutos do ambiente de origem, inclusive para ambientes
remotos.

Clientes experimentais podem definir `historyMode` em `thread/start` como `"legacy"`
(o padrão) ou `"paginated"`. A criação de conversas paginadas ainda não tem suporte
e retorna o erro JSON-RPC `-32601`. O app-server pode listar e ler resumos de
registros paginados existentes, mas as leituras do histórico completo, a paginação de turnos e a retomada
retornam erro, sem prosseguir, até que haja suporte ao histórico paginado.

Clientes beta que ativarem `capabilities.experimentalApi` podem passar o ID de um perfil de permissões
nomeado em `permissions`, em vez do campo legado `sandbox`.
Não envie `permissions` e `sandbox` juntos. Use
`permissionProfile/list` com o `cwd` do projeto para descobrir os perfis disponíveis
e verificar se os requisitos gerenciados permitem cada um deles.

`thread.sessionId` identifica a raiz da árvore da sessão atualmente ativa. As conversas raiz
usam o próprio ID da conversa como ID da sessão; as conversas criadas por fork mantêm o ID da sessão
da raiz de origem. Os clientes devem ler o ID da sessão em
`thread.sessionId`, em vez de derivá-lo do ID da conversa.

Para continuar uma sessão armazenada, chame `thread/resume` com o `thread.id` que você registrou anteriormente. O formato da resposta é igual ao de `thread/start`. Você também pode passar as mesmas substituições de configuração aceitas por `thread/start`, como `personality`:

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

Retomar uma conversa, por si só, não atualiza `thread.updatedAt` (nem a data e hora de modificação do arquivo de registro de execução). O carimbo de data/hora é atualizado quando você inicia um turno.

Se você marcar um servidor MCP habilitado como `required` na configuração e a inicialização desse servidor falhar, `thread/start` e `thread/resume` falharão em vez de continuar sem ele.

O campo `dynamicTools` de `thread/start` é experimental (requer `capabilities.experimentalApi = true`). O Codex persiste essas ferramentas dinâmicas nos metadados do registro de execução da conversa e as restaura em `thread/resume` quando você não fornece novas ferramentas dinâmicas.

Se você retomar a conversa com um modelo diferente do que consta no registro de execução, o Codex emite um aviso e aplica uma instrução de troca de modelo uma única vez, no próximo turno.

### Gerenciar a meta de uma conversa

Use `thread/goal/set`, `thread/goal/get` e `thread/goal/clear` para gerenciar o
mesmo estado persistido da meta exibido por `/goal` na TUI.

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

Os objetivos das metas não podem estar vazios e devem ter no máximo 4.000 caracteres. Informar um novo
objetivo substitui a meta e reinicia a contabilização do uso. Informar o objetivo atual
em estado não terminal ou omitir `objective` atualiza o status ou o orçamento de tokens
e preserva o histórico de uso.

Para criar um fork de uma sessão armazenada, chame `thread/fork` com `thread.id`. Isso cria um novo ID de conversa e emite uma notificação `thread/started` para ela. Passe
`lastTurnId` para copiar o histórico até esse turno, inclusive, e omitir os
turnos posteriores:

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

O App Server rejeita um `lastTurnId` referente a um turno em andamento. Se você omitir o campo enquanto a
conversa de origem estiver no meio de um turno, o fork registra um marcador de interrupção em vez de
manter um turno parcial sem marcação.

Passe `ephemeral: true` para criar um fork em memória sem adicioná-lo às listas de
conversas armazenadas:

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

Forks efêmeros de conversas paginadas também exigem `excludeTurns: true`. Esse
campo é experimental e requer `capabilities.experimentalApi = true`.

Quando um título de conversa visível ao usuário é definido, o App Server preenche `thread.name` nas respostas de `thread/list`, `thread/read`, `thread/resume`, `thread/unarchive` e `thread/rollback`. `thread/start` e `thread/fork` podem omitir `name` (ou retornar `null`) até que um título seja definido posteriormente.

### Ler uma conversa armazenada (sem retomá-la)

Use `thread/read` quando quiser obter os dados armazenados de uma conversa sem retomá-la nem assinar seus eventos.

- `includeTurns` - quando definido como `true`, a resposta inclui os turnos da conversa; quando definido como `false` ou omitido, você recebe apenas o resumo da conversa.
- Os objetos `thread` retornados incluem o `status` em tempo de execução (`notLoaded`, `idle`, `systemError` ou `active` com `activeFlags`).

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

Ao contrário de `thread/resume`, `thread/read` não carrega a conversa na memória nem emite `thread/started`.

### Listar os turnos de uma conversa

`thread/turns/list` é experimental. Use-o para percorrer, com paginação, o histórico de turnos de uma conversa armazenada sem retomá-la. Por padrão, os resultados são ordenados do mais recente para o mais antigo, para que os clientes possam buscar turnos mais antigos com `nextCursor`. A resposta também inclui `backwardsCursor`; passe esse valor como `cursor` com `sortDirection: "asc"` para buscar turnos mais recentes que o primeiro item da página obtida anteriormente.

`itemsView` controla a quantidade de dados dos itens dos turnos que a resposta inclui:

- `notLoaded` omite os itens.
- `summary` retorna dados resumidos dos itens e é o padrão quando o campo é omitido.
- `full` retorna os dados completos dos itens.

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list` também é experimental. Ele pagina os itens persistidos sem
retomar a conversa. Passe `turnId` para restringir os resultados a um turno ou omita-o
para paginar os itens de toda a conversa. O armazenamento de conversas em uso deve oferecer suporte à
paginação de itens; caso contrário, o servidor retorna um erro de método não suportado.

### Listar conversas (com paginação e filtros)

`thread/list` permite renderizar uma interface de histórico. Por padrão, os resultados são ordenados por `createdAt`, do mais recente para o mais antigo. Os filtros são aplicados antes da paginação. Passe qualquer combinação de:

- `cursor` - sequência opaca de caracteres de uma resposta anterior; omita esse campo na primeira página.
- `limit` - se não for definido, o servidor usa um tamanho de página razoável por padrão.
- `sortKey` - `created_at` (padrão), `updated_at` ou `recency_at`.
- `sortDirection` - `desc` (padrão) ou `asc`.
- `modelProviders` - restringe os resultados a provedores específicos; se não for definido, for null ou for um vetor vazio, todos os provedores serão incluídos.
- `sourceKinds` - restringe os resultados a origens específicas de conversas. Quando omitido ou definido como `[]`, o servidor usa por padrão apenas origens interativas: `cli` e `vscode`.
- `archived` - quando definido como `true`, lista apenas conversas arquivadas. Quando definido como `false` ou omitido, lista conversas não arquivadas (padrão).
- `isPinned` - quando fornecido, retorna apenas conversas cujo estado de fixação persistido corresponda ao valor fornecido. Omita-o para retornar conversas fixadas e não fixadas.
- `cwd` - restringe os resultados a conversas cujo diretório de trabalho atual da sessão corresponda exatamente a este caminho ou a um dos caminhos de um vetor. Os caminhos relativos são resolvidos a partir do diretório de trabalho do processo do App Server.
- `useStateDbOnly` - quando definido como `true`, retorna resultados do banco de dados de estado sem examinar os registros JSONL das conversas para reparar os metadados. Omita-o ou passe `false` para usar o comportamento padrão de verificação e reparo.
- `searchTerm` - restringe os resultados a conversas cujo título extraído contenha este trecho de texto, com distinção entre maiúsculas e minúsculas.
- `parentThreadId` - restringe os resultados às conversas filhas diretas da conversa pai indicada. Esse filtro é experimental e requer `capabilities.experimentalApi = true`.
- `ancestorThreadId` - restringe os resultados às conversas descendentes criadas a partir da conversa indicada, em qualquer nível de profundidade. Esse filtro é experimental e requer `capabilities.experimentalApi = true`; não o combine com `parentThreadId`.

`sourceKinds` aceita os seguintes valores:

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

Exemplo:

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

Quando `nextCursor` é `null`, você chegou à última página.

### Atualizar os metadados armazenados de uma conversa

Use `thread/metadata/update` para atualizar os metadados armazenados da conversa sem
retomá-la. Defina `isPinned` para fixar ou desafixar a conversa, ou atualize `gitInfo` para alterar
os metadados persistidos do Git. Campos omitidos permanecem inalterados; um `null` explícito remove um
valor armazenado dos metadados do Git.

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### Acompanhar alterações no status de uma conversa

`thread/status/changed` é emitido sempre que o status em tempo de execução de uma conversa carregada muda. O conteúdo da notificação inclui `threadId` e o novo `status`.

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### Listar conversas carregadas

`thread/loaded/list` retorna os IDs das conversas atualmente carregadas na memória.

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### Cancelar a assinatura de uma conversa carregada

`thread/unsubscribe` remove a assinatura da conexão atual para uma conversa. O status da resposta é um dos seguintes:

- `unsubscribed` quando a conexão tinha uma assinatura, que agora foi removida.
- `notSubscribed` quando a conexão não tinha uma assinatura para essa conversa.
- `notLoaded` quando a conversa não está carregada.

Se essa era a última conexão assinante, o servidor mantém a conversa carregada até que ela fique 30 minutos sem assinantes e sem atividade. Quando o período de tolerância termina, o App Server remove a conversa da memória e emite `thread/status/changed` indicando a transição para `notLoaded`, além de `thread/closed`.

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

Se a conversa expirar depois:

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### Arquivar uma conversa

Use `thread/archive` para mover o registro persistido da conversa (armazenado como um arquivo JSONL no disco) para o diretório de sessões arquivadas. Ao arquivar uma conversa, o servidor também tenta arquivar as conversas descendentes criadas a partir dela que ainda não estejam arquivadas.

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

As conversas arquivadas não aparecerão em chamadas futuras a `thread/list`, a menos que você passe `archived: true`. O servidor emite uma notificação `thread/archived` para cada conversa que efetivamente arquiva; se uma conversa descendente criada a partir dela não puder ser arquivada, a solicitação ainda poderá ser concluída com sucesso sem uma notificação de arquivamento para essa descendente.

### Excluir uma conversa

Use `thread/delete` para excluir permanentemente uma conversa persistida ativa ou arquivada
e as conversas descendentes criadas a partir dela. Antes de retornar uma resposta de sucesso, o servidor remove os arquivos de registro de execução existentes e
os metadados associados; arquivos de registro de execução ausentes são considerados
já excluídos. Conversas raiz efêmeras não podem ser excluídas.

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### Desarquivar uma conversa

Use `thread/unarchive` para mover o registro de execução de uma conversa arquivada de volta ao diretório de sessões ativas.

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### Acionar a compactação de uma conversa

Use `thread/compact/start` para acionar manualmente a compactação do histórico de uma conversa. A solicitação retorna imediatamente com `{}`.

O App Server informa o progresso por meio de notificações padrão `turn/*` e `item/*` no mesmo `threadId`, incluindo o ciclo de vida de um item `contextCompaction` (`item/started` seguido de `item/completed`).

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### Executar um comando de shell em uma conversa

Use `thread/shellCommand` para comandos de shell iniciados pelo usuário e associados a uma conversa. A solicitação retorna imediatamente com `{}`, enquanto o progresso é transmitido pelas notificações padrão `turn/*` e `item/*`.

Esta API é executada fora do sandbox, com acesso completo, e não herda a política de sandbox da conversa. Os clientes devem disponibilizá-la somente para comandos iniciados explicitamente pelo usuário.

Se a conversa já tiver um turno ativo, o comando será executado como uma ação auxiliar nesse turno, e sua saída formatada será inserida no fluxo de mensagens do turno. Se a conversa estiver ociosa, o app-server iniciará um turno independente para o comando de shell.

Defina `timeoutMs` para limitar o tempo de execução em milissegundos. Se o campo for omitido ou receber
`null`, será usado o padrão de uma hora. O valor `0` solicita a expiração imediata do tempo limite; valores
negativos são rejeitados. O tempo limite não atrasa a confirmação imediata de recebimento da RPC.

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### Encerrar terminais em segundo plano

Use `thread/backgroundTerminals/clean` para encerrar todos os terminais em segundo plano em execução associados a uma conversa. Este método é experimental e requer `capabilities.experimentalApi = true`.

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

Use `thread/backgroundTerminals/list` para inspecionar os terminais em segundo plano em execução
de uma conversa carregada. A solicitação aceita a paginação padrão com `cursor` e `limit`,
e o `processId` retornado é o ID de processo do app-server. Este
método é experimental e requer `capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

Use `thread/backgroundTerminals/terminate` com esse `processId` para encerrar um
terminal em segundo plano. Este método é experimental e requer
`capabilities.experimentalApi = true`:

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### Reverter turnos recentes

`thread/rollback` está obsoleto e será removido. Ele remove as últimas
`numTurns` entradas do contexto em memória e persiste um marcador de reversão no
log de execução. O `thread` retornado inclui o campo `turns` preenchido após a
reversão.

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## Turnos

O campo `input` aceita uma lista de itens:

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

Você pode substituir as configurações por turno (modelo, nível de esforço, personalidade, `cwd`, política de sandbox, resumo). Quando especificadas, essas configurações passam a ser os valores padrão dos turnos posteriores na mesma conversa. `outputSchema` se aplica somente ao turno atual. Para `sandboxPolicy.type = "externalSandbox"`, defina `networkAccess` como `restricted` ou `enabled`; para `workspaceWrite`, `networkAccess` continua sendo um valor booleano.

Em `turn/start.collaborationMode`, `settings.developer_instructions: null` significa "usar as instruções integradas do modo selecionado", em vez de limpar as instruções do modo.

### Acesso de leitura no sandbox (`ReadOnlyAccess`)

`sandboxPolicy` oferece controles explícitos de acesso de leitura:

- `readOnly`: `access` opcional (`{ "type": "fullAccess" }` por padrão ou acesso restrito a diretórios-raiz).
- `workspaceWrite`: `readOnlyAccess` opcional (`{ "type": "fullAccess" }` por padrão ou acesso restrito a diretórios-raiz).

Estrutura do acesso de leitura restrito:

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

No macOS, `includePlatformDefaults: true` acrescenta uma política Seatbelt padrão da plataforma, selecionada criteriosamente, às sessões com leitura restrita. Isso melhora a compatibilidade das ferramentas sem conceder acesso amplo a todo o `/System`.

Exemplos:

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### Iniciar um turno

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

Para iniciar um turno com a saída de uma ferramenta executada pelo seu cliente, passe `toolOutput`
com um `name` não vazio, um `namespace` opcional e um `output` como string ou
array de itens de conteúdo. Defina `input` como um array vazio; não é possível combinar
`toolOutput` com uma entrada do usuário não vazia.

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

A saída permanece identificada como saída de ferramenta na conversa e aparece como um item
`functionCallOutput` nas notificações e no histórico persistido. Se um turno regular
já estiver ativo, o Codex colocará a saída na fila desse turno.

### Injetar itens em uma conversa

Use `thread/inject_items` para adicionar itens previamente criados da Responses API ao histórico de prompts de uma conversa carregada sem iniciar um turno do usuário. Esses itens são persistidos no registro de execução e incluídos nas solicitações posteriores ao modelo.

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### Direcionar um turno ativo

Use `turn/steer` para adicionar mais entradas do usuário ao turno ativo em andamento.

- Inclua `expectedTurnId`; ele deve corresponder ao ID do turno ativo.
- A solicitação falha se não houver um turno ativo na conversa.
- `turn/steer` não emite uma nova notificação `turn/started`.
- `turn/steer` não aceita substituições de configuração por turno (`model`, `cwd`, `sandboxPolicy` ou `outputSchema`).

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### Iniciar um turno (invocar uma habilidade)

Invoque uma habilidade explicitamente incluindo `$<skill-name>` na entrada de texto e adicionando também um item de entrada `skill`.

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### Interromper um turno

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

Em caso de sucesso, o turno termina com `status: "interrupted"`.

## Revisão

`review/start` executa o revisor do Codex para uma conversa e transmite itens de revisão. Os alvos incluem:

- `uncommittedChanges`
- `baseBranch` (comparação das diferenças em relação a uma branch)
- `commit` (revisar um commit específico)
- `custom` (instruções em formato livre)

Use `delivery: "inline"` (padrão) para executar a revisão na conversa existente ou `delivery: "detached"` para criar uma nova conversa de revisão por meio de um fork.

Exemplo de solicitação/resposta:

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

Para uma revisão separada, use `"delivery": "detached"`. A resposta tem o mesmo formato, mas `reviewThreadId` será o ID da nova conversa de revisão (diferente do `threadId` original). O servidor também emite uma notificação `thread/started` para essa nova conversa antes de iniciar a transmissão do turno de revisão.

O Codex transmite a notificação `turn/started` habitual, seguida de uma notificação `item/started` com um item `enteredReviewMode`:

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

Quando o revisor termina, o servidor emite as notificações `item/started` e `item/completed`, que contêm um item `exitedReviewMode` com o texto final da revisão:

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

Use essa notificação para exibir a saída do revisor no seu cliente.

## Execução de processos

`process/*` é uma API experimental para controle explícito de processos. Ela requer
`capabilities.experimentalApi = true` e é executada fora do sandbox do Codex. Use-a
somente quando seu cliente disponibilizar intencionalmente o controle local de processos sem um
sandbox.

Inicie um processo com `process/spawn` e forneça um `processHandle`; depois, use
esse identificador nas solicitações de stdin, redimensionamento e encerramento. A saída é transmitida pelas notificações
`process/outputDelta`, e a conclusão é informada por
`process/exited`.

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

Use `process/writeStdin` com `deltaBase64`, `closeStdin` ou ambos para enviar
dados de entrada. Use `process/resizePty` para eventos de redimensionamento de PTY e `process/kill` para
encerrar um processo em execução.

## Execução de comandos

`command/exec` executa um único comando (array `argv`) dentro do sandbox do servidor sem criar uma conversa.

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

Use `sandboxPolicy.type = "externalSandbox"` se você já executa o processo do servidor em um sandbox e quer que o Codex deixe de aplicar seu próprio sandbox. No modo de sandbox externo, defina `networkAccess` como `restricted` (padrão) ou `enabled`. Para `readOnly` e `workspaceWrite`, use a mesma estrutura opcional de `access` / `readOnlyAccess` mostrada acima.

Observações:

- O servidor rejeita arrays `command` vazios.
- `sandboxPolicy` aceita a mesma estrutura usada por `turn/start` (por exemplo, `dangerFullAccess`, `readOnly`, `workspaceWrite`, `externalSandbox`).
- Quando omitido, `timeoutMs` usa o valor padrão do servidor.
- Defina `tty: true` para sessões baseadas em PTY e use `processId` quando pretender fazer chamadas posteriores a `command/exec/write`, `command/exec/resize` ou `command/exec/terminate`.
- Defina `streamStdoutStderr: true` para receber notificações `command/exec/outputDelta` enquanto o comando estiver em execução.

### Ler requisitos definidos pelo administrador (`configRequirements/read`)

Use `configRequirements/read` para inspecionar os requisitos em vigor definidos pelo administrador e carregados de `requirements.toml` e/ou do MDM.

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

`result.requirements` é `null` quando nenhum requisito está configurado. Consulte a documentação sobre [`requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml) para ver detalhes das chaves e dos valores aceitos.

### Configuração do sandbox do Windows (`windowsSandbox/setupStart`)

Clientes personalizados para Windows podem iniciar a configuração do sandbox de forma assíncrona, sem bloquear a execução nas verificações de inicialização.

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

O App Server inicia a configuração em segundo plano e depois emite uma notificação de conclusão:

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

Modos:

- `elevated` - execute o fluxo de configuração do Sandbox do Windows com privilégios elevados.
- `unelevated` - execute o fluxo legado de configuração/verificação prévia.

## Sistema de arquivos

As APIs v2 do sistema de arquivos operam com caminhos absolutos. Use `fs/watch` quando um cliente precisar invalidar o estado da interface após a alteração de um arquivo ou diretório.

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

O monitoramento de um arquivo emite `fs/changed` para o caminho desse arquivo, incluindo atualizações decorrentes de operações de substituição ou renomeação.

## Eventos

As notificações de eventos formam o fluxo iniciado pelo servidor para os ciclos de vida das conversas e dos turnos, bem como para os itens contidos neles. Depois de iniciar ou retomar uma conversa, continue lendo o fluxo do transporte ativo para receber as notificações `thread/started`, `thread/archived`, `thread/unarchived`, `thread/closed`, `thread/status/changed`, `turn/*`, `item/*` e `serverRequest/resolved`.

### Desativação de notificações

Os clientes podem suprimir notificações específicas por conexão enviando os nomes exatos dos métodos em `initialize.params.capabilities.optOutNotificationMethods`.

- Somente correspondência exata: `item/agentMessage/delta` suprime apenas esse método.
- Nomes de métodos desconhecidos são ignorados.
- Aplica-se às notificações atuais `thread/*`, `turn/*` e `item/*`, além das notificações v2 relacionadas.
- Não se aplica a solicitações, respostas nem erros.

### Eventos de pesquisa aproximada de arquivos (experimental)

A API de sessão de pesquisa aproximada de arquivos emite notificações para cada consulta:

- `fuzzyFileSearch/sessionUpdated` - `{ sessionId, query, files }` com as correspondências atuais da consulta ativa.
- `fuzzyFileSearch/sessionCompleted` - `{ sessionId }` quando a indexação e a busca de correspondências dessa consulta forem concluídas.

### Eventos de aviso

- `configWarning` - `{ summary, details?, path?, range? }` para problemas recuperáveis
  de configuração ou inicialização.
- `warning` - `{ threadId?, message }` para avisos não fatais em tempo de execução.

### Eventos de configuração do Sandbox do Windows

- `windowsSandbox/setupCompleted` - `{ mode, success, error }` emitido após a conclusão de uma solicitação `windowsSandbox/setupStart`.

### Eventos de turno

- `turn/started` - `{ turn }` com o ID do turno, o campo `items` vazio e `status: "inProgress"`.
- `turn/completed` - `{ turn }`, em que `turn.status` é `completed`, `interrupted` ou `failed`; as falhas incluem `{ error: { message, codexErrorInfo?, additionalDetails? } }`.
- `turn/diff/updated` - `{ threadId, turnId, diff }` com as diferenças mais recentes em formato unificado, agregando todas as alterações de arquivos no turno.
- `turn/plan/updated` - `{ turnId, explanation?, plan }` sempre que o agente compartilha ou altera seu plano; cada entrada de `plan` é `{ step, status }`, com `status` definido como `pending`, `inProgress` ou `completed`.
- `hook/started` e `hook/completed` - `{ threadId, turnId?, run }` quando um gancho síncrono de ciclo de vida é iniciado e quando o resumo final de sua execução fica disponível. Essas notificações não são emitidas para ganchos assíncronos.
- `model/safetyBuffering/updated` - `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }` quando uma resposta passa a ser retida temporariamente em buffer por segurança.
- `model/rerouted` - `{ threadId, turnId, fromModel, toModel, reason }` quando o serviço encaminha uma solicitação para outro modelo.
- `model/verification` - `{ threadId, turnId, verifications }` quando o serviço exige uma verificação adicional da conta.
- `thread/tokenUsage/updated` - atualizações de uso da conversa ativa.

`turn/diff/updated` e `turn/plan/updated` atualmente incluem vetores `items` vazios, mesmo quando os eventos dos itens são transmitidos de forma incremental. Use as notificações `item/*` como referência definitiva para os itens do turno.

### Itens

`ThreadItem` é a união discriminada presente nas respostas dos turnos e nas notificações `item/*`. Os tipos comuns de item incluem:

- `userMessage` - `{id, content}`, em que `content` é uma lista de entradas do usuário (`text`, `image` ou `localImage`).
- `functionCallOutput` - `{id, name, namespace, output}` para uma saída de ferramenta fornecida de forma independente por meio de `turn/start.toolOutput`. `namespace` pode ser `null`.
- `agentMessage` - `{id, text, phase?}` contendo a resposta acumulada do agente. Quando presente, `phase` usa os valores do formato de transmissão da Responses API (`commentary`, `final_answer`).
- `plan` - `{id, text}` contendo o texto do plano proposto no modo planejamento. Considere o item `plan` final de `item/completed` como definitivo.
- `reasoning` - `{id, summary, content}`, em que `summary` contém resumos de raciocínio transmitidos de forma incremental e `content` contém blocos brutos de raciocínio.
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`.
- `fileChange` - `{id, changes, status}` descrevendo as edições propostas; a lista `changes` contém `{path, kind, diff}`.
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`. Para aplicativos MCP confiáveis, `appContext` pode incluir `connectorId`, `linkId`, `resourceUri`, `appName`, `templateId` e o `actionName` estável do conector. Itens persistidos mais antigos podem omitir metadados mais recentes. Use `appContext.resourceUri` em vez do campo obsoleto `mcpAppResourceUri` de nível superior.
- `dynamicToolCall` - `{id, tool, arguments, status, contentItems?, success?, durationMs?}` para chamadas de ferramentas dinâmicas executadas pelo cliente.
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`.
- `webSearch` - `{id, query, action?}` para solicitações de pesquisa na Web feitas pelo agente.
- `imageView` - `{id, path}` emitido quando o agente chama a ferramenta de visualização de imagens.
- `enteredReviewMode` - `{id, review}` enviado quando o revisor inicia a execução.
- `exitedReviewMode` - `{id, review}` emitido quando o revisor conclui a execução.
- `contextCompaction` - `{id}` emitido quando o Codex compacta o histórico da conversa.

Para `webSearch.action`, o campo `type` da ação pode ser `search` (`query?`, `queries?`), `openPage` (`url?`) ou `findInPage` (`url?`, `pattern?`).

O App Server marca a notificação legada `thread/compacted` como obsoleta; use o item `contextCompaction` em seu lugar.

Todos os itens emitem dois eventos de ciclo de vida compartilhados:

- `item/started` - emite o `item` completo quando uma nova unidade de trabalho começa; o `item.id` corresponde ao `itemId` usado pelos deltas.
- `item/completed` - envia o `item` final quando o trabalho termina; considere esse estado como definitivo.

### Deltas de itens

- `item/agentMessage/delta` - acrescenta à mensagem do agente o texto transmitido de forma incremental.
- `item/plan/delta` - transmite de forma incremental o texto do plano proposto. O item `plan` final pode não corresponder exatamente aos deltas concatenados.
- `item/reasoning/summaryTextDelta` - transmite de forma incremental resumos legíveis do raciocínio; `summaryIndex` é incrementado quando uma nova seção do resumo é iniciada.
- `item/reasoning/summaryPartAdded` - marca a separação entre seções do resumo de raciocínio.
- `item/reasoning/textDelta` - transmite de forma incremental o texto bruto do raciocínio (quando o modelo oferece suporte).
- `item/commandExecution/outputDelta` - transmite stdout/stderr de um comando em fluxo; acrescente os deltas na ordem.
- `item/fileChange/outputDelta` - notificação de compatibilidade obsoleta para a saída de texto legada de `apply_patch`. As versões atuais do app-server não a emitem mais; use os itens `fileChange` e `turn/diff/updated`.

## Erros

Se um turno falhar, o servidor emitirá um evento `error` com `{ error: { message, codexErrorInfo?, additionalDetails? } }` e encerrará o turno com `status: "failed"`. Quando um status HTTP do serviço de origem estiver disponível, ele aparecerá em `codexErrorInfo.httpStatusCode`.

Valores comuns de `codexErrorInfo` incluem:

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed` (erros 4xx/5xx do serviço de origem)
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`, `Unauthorized`, `SandboxError`, `InternalServerError`, `Other`

Quando um status HTTP do serviço de origem está disponível, o servidor o encaminha em `httpStatusCode` na variante correspondente de `codexErrorInfo`.

## Aprovações

Dependendo das configurações do Codex definidas pelo usuário, a execução de comandos e as alterações em arquivos podem exigir aprovação. O app-server envia ao cliente uma solicitação JSON-RPC iniciada pelo servidor, e o cliente responde com uma carga útil contendo a decisão.

- Decisões sobre a execução de comandos: `accept`, `acceptForSession`, `decline`, `cancel` ou `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`.
- Decisões sobre alterações em arquivos: `accept`, `acceptForSession`, `decline`, `cancel`.

- As solicitações incluem `threadId` e `turnId`; use-os para limitar o escopo do estado da interface à conversa ativa.
- O servidor retoma ou recusa o trabalho e encerra o item com `item/completed`.

### Aprovações para execução de comandos

Ordem das mensagens:

1. `item/started` mostra o item `commandExecution` pendente com `command`, `cwd` e outros campos.
2. `item/commandExecution/requestApproval` inclui `itemId`, `threadId`, `turnId` e os campos opcionais `reason`, `command`, `cwd`, `commandActions`, `proposedExecpolicyAmendment`, `networkApprovalContext` e `availableDecisions`. Quando `initialize.params.capabilities.experimentalApi = true`, a carga útil também pode incluir o campo experimental `additionalPermissions`, que descreve o acesso ao sandbox solicitado para cada comando. Todos os caminhos do sistema de arquivos em `additionalPermissions` são absolutos no protocolo.
3. O cliente responde com uma das decisões de aprovação da execução de comandos apresentadas acima.
4. `serverRequest/resolved` confirma que a solicitação pendente foi respondida ou removida.
5. `item/completed` retorna o item `commandExecution` final com `status: completed | failed | declined`.

Quando `networkApprovalContext` está presente, o prompt se refere ao acesso gerenciado à rede (não à aprovação geral de um comando do shell). O esquema v2 atual expõe o `host` e o `protocol` de destino; os clientes devem exibir um prompt específico de rede e não presumir que `command` apresente uma prévia de comando do shell compreensível para o usuário.

O Codex agrupa prompts simultâneos de aprovação de rede por destino (`host`, protocolo e porta). Portanto, o app-server pode enviar um único prompt que desbloqueia várias solicitações na fila para o mesmo destino, enquanto portas diferentes no mesmo host são tratadas separadamente.

### Aprovações de alterações em arquivos

Ordem das mensagens:

1. `item/started` emite um item `fileChange` com as alterações propostas em `changes` e com `status: "inProgress"`.
2. `item/fileChange/requestApproval` inclui `itemId`, `threadId`, `turnId` e os campos opcionais `reason` e `grantRoot`.
3. O cliente responde com uma das decisões de aprovação de alterações em arquivos apresentadas acima.
4. `serverRequest/resolved` confirma que a solicitação pendente foi respondida ou removida.
5. `item/completed` retorna o item `fileChange` final com `status: completed | failed | declined`.

### `tool/requestUserInput`

Quando o cliente responde a `item/tool/requestUserInput`, o app-server emite `serverRequest/resolved` com `{ threadId, requestId }`. Se a solicitação pendente for removida pelo início, pela conclusão ou pela interrupção do turno antes que o cliente responda, o servidor emite a mesma notificação para indicar essa remoção.

Os parâmetros da solicitação incluem `autoResolutionMs` como um tempo limite em milissegundos expresso por um número inteiro ou
`null`. Quando esse tempo limite é informado, os clientes host podem resolver o prompt automaticamente após esse
intervalo se o usuário não responder.

### Solicitações de permissão

A ferramenta integrada `request_permissions` envia
`item/permissions/requestApproval` com `threadId`, `turnId`, `itemId`,
`environmentId`, `cwd`, o campo opcional `reason` e as permissões de rede ou do sistema de arquivos
solicitadas. Responda com `permissions` contendo apenas o subconjunto concedido.
Defina `scope` como `"session"` para manter a concessão em turnos posteriores da mesma
sessão; omita esse campo ou use `"turn"` para uma concessão limitada ao turno. As permissões que
não foram solicitadas são ignoradas.

### Solicitações de elicitação de servidores MCP

Um servidor MCP pode interromper um turno com `mcpServer/elicitation/request`. A
solicitação inclui `threadId`, o campo opcional `turnId`, `serverName` e um destes
formatos de solicitação:

- `mode: "form"` ou `mode: "openai/form"`, com `message` e
`requestedSchema`.
- `mode: "url"`, com `message`, `url` e `elicitationId`.

Responda com `action: "accept"` e o `content` solicitado, ou com
`action: "decline"` ou `"cancel"` e `content: null`. Em seguida, o app-server emite
`serverRequest/resolved`. Para receber a variante `openai/form`, habilite-a com
`initialize.params.capabilities.mcpServerOpenaiFormElicitation`.

### Chamadas de ferramentas dinâmicas (experimentais)

O campo `dynamicTools` em `thread/start` e o fluxo correspondente de solicitação ou resposta de `item/tool/call` são APIs experimentais.

Os nomes de ferramentas dinâmicas e de espaços de nomes devem seguir as restrições de nomenclatura da Responses API.
Evite os nomes reservados de espaços de nomes usados pelas ferramentas integradas do Codex.

Quando uma ferramenta dinâmica é invocada durante um turno, o app-server emite:

1. `item/started` com `item.type = "dynamicToolCall"`, `status = "inProgress"`, além de `tool` e `arguments`.
2. `item/tool/call` como uma solicitação do servidor ao cliente.
3. A carga útil da resposta do cliente com os itens de conteúdo retornados.
4. `item/completed` com `item.type = "dynamicToolCall"`, o `status` final e qualquer valor retornado em `contentItems` ou `success`.

### Aprovações de chamadas de ferramentas MCP (aplicativos)

As chamadas de ferramentas de aplicativos (conectores) também podem exigir aprovação. Quando uma chamada de ferramenta de um aplicativo tem efeitos colaterais, o servidor pode solicitar aprovação com `tool/requestUserInput` e opções como **Aceitar**, **Recusar** e **Cancelar**. As anotações que indicam ferramentas destrutivas sempre acionam uma solicitação de aprovação, mesmo quando a ferramenta também apresenta indicações de que requer menos privilégios. Se o usuário recusar ou cancelar, o item `mcpToolCall` relacionado será concluído com um erro, sem executar a ferramenta.

## Habilidades

Invoque uma habilidade incluindo `$<skill-name>` na entrada de texto do usuário. Adicione um item de entrada `skill` (recomendado) para que o servidor injete as instruções completas da habilidade em vez de depender do modelo para resolver o nome.

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

Se você omitir o item `skill`, o modelo ainda analisará o marcador `$<skill-name>` e tentará localizar a habilidade, o que pode aumentar a latência.

Exemplo:

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

Use `skills/list` para buscar as habilidades disponíveis (opcionalmente limitadas a `cwds`, com `forceReload`). Você também pode incluir `perCwdExtraUserRoots` para examinar caminhos absolutos adicionais no escopo `user` para valores específicos de `cwd`. O app-server ignora entradas cujo `cwd` não esteja presente em `cwds`. `skills/list` pode reutilizar um resultado em cache para cada `cwd`; defina `forceReload: true` para atualizar os dados a partir do disco. Quando presentes, o servidor lê `interface` e `dependencies` de `SKILL.json`.

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

O servidor também emite notificações `skills/changed` quando os arquivos locais de habilidades monitorados são alterados. Trate isso como um sinal de invalidação e execute `skills/list` novamente com os parâmetros atuais quando necessário.

Para habilitar ou desabilitar uma habilidade pelo caminho:

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## Apps (conectores)

Use `app/installed` para ler o instantâneo confirmado mais recente do estado de execução dos aplicativos instalados.
Cada resultado inclui o `id` do aplicativo, `runtimeName` (ou `null`), o estado efetivo de
`enabled` e o estado de `callable`. Um aplicativo só pode ser chamado quando a
configuração efetiva o habilita e pelo menos uma ferramenta visível para o modelo atende às políticas
do aplicativo e da ferramenta.

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

Omita `threadId` para usar a configuração global em vez da configuração de uma conversa
carregada. Defina `forceRefresh: true` para atualizar o instantâneo do estado de execução do conector
antes de lê-lo. Quando uma política global ou do workspace bloqueia o acesso a aplicativos,
um aplicativo detectado ainda pode aparecer com `enabled` e `callable` definidos como `false`.

Use `app/list` para buscar os aplicativos disponíveis. Na CLI/TUI, `/apps` é o seletor exibido ao usuário; em clientes personalizados, chame `app/list` diretamente. Cada entrada inclui `isAccessible` (disponível para o usuário) e `isEnabled` (habilitado em `config.toml`), permitindo que os clientes diferenciem instalação/acesso do estado de habilitação local. As entradas de aplicativos também podem incluir os campos opcionais `branding`, `appMetadata` e `labels`.

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

Se você fornecer `threadId`, o controle de ativação de aplicativos (`features.apps`) usará o instantâneo de configuração dessa conversa. Se você omitir esse campo, o app-server usará a configuração global mais recente.

`app/list` retorna depois que os aplicativos acessíveis e os aplicativos do diretório são carregados. Defina `forceRefetch: true` para ignorar os caches de aplicativos e buscar dados atualizados. As entradas de cache só são substituídas quando as atualizações são bem-sucedidas.

O servidor também emite notificações `app/list/updated` sempre que qualquer uma das fontes (aplicativos acessíveis ou aplicativos do diretório) termina de carregar. Cada notificação inclui a lista consolidada de aplicativos mais recente.

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

Use `app/read` quando você já souber os IDs dos aplicativos e precisar dos metadados dos aplicativos em vez
do estado de execução dos aplicativos instalados. Passe no máximo 100 IDs em `appIds`. O servidor mantém apenas
a primeira ocorrência de cada ID repetido e preserva essa ordem em
`apps` e `missingAppIds`. Aplicativos desconhecidos ou inacessíveis são retornados em
`missingAppIds` sem causar falha em toda a solicitação.

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

Defina `includeTools: true` para solicitar resumos públicos de ferramentas apenas para exibição.
A resposta de metadados não inclui o estado de execução dos aplicativos instalados
nem autoriza uma chamada de ferramenta; use `app/installed` para verificar
o estado efetivo de `enabled` e `callable`.

Invoque um aplicativo inserindo `$<app-slug>` no texto de entrada e adicionando um item de entrada `mention` com o caminho `app://<id>` (recomendado).

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### Exemplos de RPC de configuração para ajustes de aplicativos

Use `config/read`, `config/value/write` e `config/batchWrite` para inspecionar ou atualizar os controles de aplicativos em `config.toml`.

Consulte a estrutura da configuração efetiva do aplicativo (incluindo `_default` e substituições por ferramenta):

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer` define o revisor para todos os aplicativos, a menos que um
valor específico de um aplicativo o substitua. Quando ambos são omitidos, o aplicativo herda o
valor de `approvals_reviewer` no nível superior. `apps._default.default_tools_approval_mode`
define o modo de aprovação padrão para ferramentas sem substituição por aplicativo ou
por ferramenta. Os requisitos gerenciados de modo de aprovação prevalecem sobre as
configurações de modo de aprovação das ferramentas.

Atualize uma única configuração de aplicativo:

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

Aplique várias alterações nas configurações de aplicativos de forma atômica:

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### Detectar e importar configurações de agentes externos

Use `externalAgentConfig/detect` para identificar artefatos de agentes externos que podem ser migrados e, em seguida, passe as entradas selecionadas para `externalAgentConfig/import`.

Exemplo de detecção:

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

Exemplo de importação:

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

O parâmetro opcional de importação `source` no nível superior identifica o produto que
gerou os itens de migração selecionados.

O servidor emite `externalAgentConfig/import/progress` à medida que a importação de cada tipo de item é concluída,
e `externalAgentConfig/import/completed` depois que todas as importações síncronas e em segundo plano
forem concluídas. Essas notificações incluem o mesmo `importId` da
resposta e `itemTypeResults` com `successes` e `failures` por tipo.
A notificação de conclusão pode chegar imediatamente após a resposta ou depois que as importações remotas em segundo plano
forem concluídas.

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

Consulte as importações anteriores concluídas:

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

Os valores aceitos para `itemType` são `AGENTS_MD`, `CONFIG`, `SKILLS`, `PLUGINS`,
`MCP_SERVER_CONFIG`, `SUBAGENTS`, `HOOKS`, `COMMANDS` e `SESSIONS`. Para itens
do tipo `PLUGINS`, `details.plugins` lista cada `marketplaceName` e os
`pluginNames` que o Codex pode tentar migrar. A detecção retorna apenas itens que ainda
precisam ser processados. Por exemplo, o Codex ignora a migração de AGENTS quando `AGENTS.md`
já existe e não está vazio, e as importações de habilidades não sobrescrevem diretórios de
habilidades existentes.

Ao detectar plug-ins em `.claude/settings.json`, o Codex lê as fontes de marketplace
configuradas em `extraKnownMarketplaces`. Se `enabledPlugins` contiver
plug-ins de `claude-plugins-official`, mas a fonte do marketplace estiver ausente,
o Codex infere `anthropics/claude-plugins-official` como fonte.

## Endpoints de autenticação

A interface JSON-RPC de autenticação e conta expõe métodos de solicitação e resposta, além de notificações iniciadas pelo servidor (sem `id`). Use esses recursos para determinar o estado da autenticação, iniciar ou cancelar logins, encerrar a sessão, consultar os limites de taxa do ChatGPT e notificar proprietários de workspaces sobre créditos esgotados ou limites de uso.

### Modos de autenticação

O Codex oferece suporte a estes modos de autenticação. `account/updated.authMode` mostra o modo ativo e inclui o `planType` atual do ChatGPT, quando disponível. `account/read` também informa detalhes da conta e do plano.

- **Chave de API (`apikey`)** - o chamador fornece uma chave de API da OpenAI com `type: "apiKey"`, e o Codex a armazena para solicitações à API.
- **Autenticação gerenciada do ChatGPT (`chatgpt`)** - o Codex gerencia o fluxo OAuth do ChatGPT, armazena os tokens de forma persistente e os renova automaticamente. Comece com `type: "chatgpt"` para o fluxo pelo navegador ou `type: "chatgptDeviceCode"` para o fluxo de código do dispositivo.
- **Tokens externos do ChatGPT (`chatgptAuthTokens`)** - modo experimental destinado a aplicativos host que já gerenciam o ciclo de vida da autenticação do usuário no ChatGPT. O aplicativo host fornece diretamente `accessToken`, `chatgptAccountId` e, opcionalmente, `chatgptPlanType`, e deve renovar o token quando solicitado.
- **Amazon Bedrock** - `account/read` identifica as contas do Bedrock como `type: "amazonBedrock"` e indica se as credenciais vêm de uma chave de API do Bedrock gerenciada pelo Codex (`credentialSource: "codexManaged"`) ou da cadeia externa de credenciais da AWS (`credentialSource: "awsManaged"`). `account/updated.authMode` usa `bedrockApiKey` para chaves de API do Bedrock gerenciadas pelo Codex.

### Visão geral da API

- `account/read` - obtém as informações atuais da conta; opcionalmente, renova os tokens.
- `account/login/start` - inicia o login (`apiKey`, `chatgpt`, `chatgptDeviceCode` ou `chatgptAuthTokens`, que é experimental).
- `account/login/completed` (notificação) - emitida quando uma tentativa de login termina (com sucesso ou erro).
- `account/login/cancel` - cancela um login pendente no modo de autenticação gerenciada do ChatGPT, identificado por `loginId`.
- `account/logout` - encerra a sessão; aciona `account/updated`.
- `account/updated` (notificação) - emitida sempre que o modo de autenticação muda (`authMode`: `apikey`, `chatgpt`, `chatgptAuthTokens`, `agentIdentity`, `personalAccessToken`, `bedrockApiKey` ou `null`) e inclui `planType` quando disponível.
- `account/chatgptAuthTokens/refresh` (solicitação do servidor) - solicita novos tokens do ChatGPT gerenciados externamente após um erro de autorização.
- `account/rateLimits/read` - obtém os limites de taxa do ChatGPT.
- `account/rateLimits/updated` (notificação) - emitida sempre que os limites de taxa do ChatGPT de um usuário mudam.
- `account/sendAddCreditsNudgeEmail` - solicita ao ChatGPT que envie um e-mail a um proprietário de workspace sobre créditos esgotados ou um limite de uso atingido.
- `account/rateLimitResetCredit/consume` - consome uma redefinição de limite de taxa obtida, usando um valor de `idempotencyKey` fornecido pelo chamador.
- `account/usage/read` - obtém resumos da atividade de tokens da conta do ChatGPT e agrupamentos diários.
- `account/workspaceMessages/read` - obtém as mensagens ativas do workspace, incluindo títulos de notificações, quando disponíveis.
- `mcpServer/oauthLogin/completed` (notificação) - emitida após a conclusão de um fluxo `mcpServer/oauth/login`; o payload inclui `{ name, threadId, success, error? }`. `threadId` pode ser `null` em fluxos OAuth com escopo de aplicativo ou de plug-ins.
- `mcpServer/startupStatus/updated` (notificação) - emitida quando o status de inicialização de um servidor MCP configurado muda; o payload inclui `{ threadId, name, status, error, failureReason }`. `threadId` é `null` na inicialização com escopo de aplicativo. Se a inicialização falhar, `failureReason: "reauthenticationRequired"` significa que as credenciais OAuth armazenadas expiraram e não puderam ser renovadas; portanto, o cliente deve oferecer a opção de reconectar o servidor.

### 1) Verificar o estado da autenticação

Solicitação:

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

Exemplos de resposta:

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

Observações sobre os campos:

- `refreshToken` (booleano): defina como `true` para forçar a renovação do token no modo de autenticação gerenciada do ChatGPT. No modo de tokens externos (`chatgptAuthTokens`), o app-server ignora esse sinalizador.
- `email` é `null` quando a conta do ChatGPT não tem um endereço de e-mail.
- `requiresOpenaiAuth` reflete o provedor ativo; quando é `false`, o Codex pode ser executado sem credenciais da OpenAI.
- O Amazon Bedrock informa `credentialSource: "codexManaged"` quando usa uma
  chave de API do Bedrock gerenciada pelo Codex. Informa `credentialSource: "awsManaged"`
  para o mecanismo externo de credenciais da AWS. Isso identifica a fonte de credenciais
  selecionada; não valida se a cadeia de credenciais da AWS consegue obter
  credenciais.

### 2) Fazer login com uma chave de API

1. Enviar:

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. Resposta esperada:

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. Notificações:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) Fazer login com o ChatGPT (fluxo pelo navegador)

1. Inicie:

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   Por padrão, um callback bem-sucedido do navegador redireciona para uma página local de confirmação.
   Defina `useHostedLoginSuccessPage: true` para usar a página de confirmação hospedada quando
   não for necessário configurar a organização. Com a página de confirmação hospedada habilitada, `appBrand`
   pode ser `"codex"` ou `"chatgpt"`; se o valor for omitido ou for `null`, o padrão será
`"codex"`.

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. Abra `authUrl` em um navegador; o app-server hospeda o callback local.
3. Aguarde as notificações:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) Fazer login com o ChatGPT (fluxo de código do dispositivo)

Use este fluxo quando o seu cliente controlar o processo de login ou quando o callback do navegador for pouco confiável.

1. Inicie:

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. Mostre `verificationUrl` e `userCode` ao usuário; o frontend é responsável pela experiência do usuário.
3. Aguarde as notificações:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) Fazer login com tokens do ChatGPT gerenciados externamente (`chatgptAuthTokens`)

Use esse modo experimental somente quando um aplicativo host gerenciar o ciclo de autenticação do usuário no ChatGPT e fornecer tokens diretamente. Os clientes devem definir `capabilities.experimentalApi = true` durante `initialize` antes de usar esse tipo de login.

1. Envie:

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. Resposta esperada:

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. Notificações:

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

Quando o servidor recebe um `401 Unauthorized`, ele pode solicitar tokens renovados ao aplicativo host:

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

O servidor repete a solicitação original após receber uma resposta de renovação bem-sucedida. As solicitações atingem o tempo limite após cerca de 10 segundos.

### 4) Cancelar um login no ChatGPT

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) Sair

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) Limites de taxa (ChatGPT)

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

Observações sobre os campos:

- `rateLimits` é a visão de um único grupo de limites, compatível com versões anteriores.
- `rateLimitsByLimitId` (quando presente) é a visão de vários grupos de limites, indexada pelo `limit_id` usado na medição (por exemplo, `codex`).
- `limitId` é o identificador do grupo de limites cujo uso é medido.
- `limitName` é um rótulo opcional do grupo de limites, exibido ao usuário.
- `usedPercent` é o uso atual dentro da janela de cota.
- `windowDurationMins` é a duração da janela de cota.
- `resetsAt` é um carimbo de data/hora Unix (em segundos) da próxima redefinição.
- `planType` é incluído quando o servidor retorna o plano do ChatGPT associado a um grupo de limites.
- `credits` é incluído quando o servidor retorna detalhes dos créditos restantes do workspace.
- `rateLimitReachedType` identifica o estado do limite, conforme classificado pelo servidor, quando um limite é atingido.
- `rateLimitResetCredits` contém a quantidade de redefinições obtidas que estão disponíveis quando o serviço fornece essa informação; caso contrário, é `null`.
- `rateLimitResetCredits.credits` é `null` quando apenas a quantidade é conhecida. Um vetor vazio significa que o serviço buscou os detalhes e não retornou nenhum crédito disponível. O serviço pode limitar o número de linhas de detalhes, por isso `availableCount` é o valor definitivo.
- Cada linha de detalhes inclui um `id` opaco, `resetType`, `status`, `grantedAt`, `expiresAt` (que pode ser `null`), `title` (que pode ser `null`) e `description` (que pode ser `null`).
- Consulte `account/rateLimits/read` após consumir uma redefinição.

### 7) Uso de tokens (ChatGPT)

Use `account/usage/read` para obter os campos de resumo da atividade de tokens do ChatGPT e
os agrupamentos diários opcionais.

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

Observações sobre os campos:

- Os valores de `summary` podem ser `null` quando o serviço não tiver retornado essa métrica.
- `dailyUsageBuckets` pode ser `null`; quando presente, cada agrupamento inclui `startDate` e `tokens`.
- O endpoint exige autenticação baseada nos serviços do Codex. São aceitas as autenticações pelo ChatGPT,
por tokens externos do ChatGPT, por identidade de agente e por token de acesso pessoal;
as autenticações apenas por chave de API e pelo Bedrock não são aceitas.

### 8) Redefinições obtidas para limites de taxa (ChatGPT)

Use `account/rateLimitResetCredit/consume` para consumir uma redefinição obtida.

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

Observações sobre os campos:

- `idempotencyKey` não pode estar vazio. Use um UUID para cada tentativa lógica de resgate e reutilize o mesmo valor ao repetir essa tentativa.
- `creditId` é opcional. Quando fornecido, deve ser um ID opaco não vazio retornado por `account/rateLimits/read`. Quando omitido, o serviço seleciona o próximo crédito disponível.
- `reset` significa que um crédito foi consumido.
- `alreadyRedeemed` significa que o mesmo resgate já foi concluído. Trate esse resultado como um sucesso idempotente e atualize os dados dos limites da conta.
- `nothingToReset` significa que não há nenhuma janela de limite de taxa elegível para redefinição.
- `noCredit` significa que a conta não tem créditos disponíveis de redefinições obtidas.
- Consulte `account/rateLimits/read` após consumir uma redefinição, em vez de inferir as janelas atualizadas com base nessa resposta.

### 9) Notificar um proprietário do workspace sobre um limite

Use `account/sendAddCreditsNudgeEmail` para pedir ao ChatGPT que envie um e-mail a um proprietário do workspace quando os créditos se esgotarem ou um limite de uso for atingido.

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

Use `creditType: "credits"` quando os créditos do workspace se esgotarem ou `creditType: "usage_limit"` quando o limite de uso do workspace for atingido. Se o proprietário já tiver sido notificado recentemente, o status da resposta será `cooldown_active`.

### 10) Mensagens do workspace (ChatGPT)

Use `account/workspaceMessages/read` para obter as mensagens ativas do workspace
atual, incluindo os títulos das notificações quando disponíveis.

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
