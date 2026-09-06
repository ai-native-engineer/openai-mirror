<!-- source: https://learn.chatgpt.com/pt-BR/docs/config-file/config-advanced -->

Use estas opções quando precisar de mais controle sobre provedores, políticas e integrações. Para começar rapidamente, consulte [Configuração básica](/pt-BR/codex/config-file/config-basic).

Para saber mais sobre orientações de projeto, capacidades reutilizáveis, comandos de barra personalizados, fluxos de trabalho de subagentes e integrações, consulte [Personalização](/pt-BR/codex/customization/overview). Para ver as chaves de configuração, consulte [Referência de configuração](/pt-BR/codex/config-file/config-reference).

## Perfis

Os perfis permitem salvar camadas de configuração nomeadas e alternar entre elas pela
CLI. Ao usar `--profile profile-name`, o Codex carrega
`~/.codex/config.toml` e, em seguida, aplica `~/.codex/profile-name.config.toml` sobre essa configuração.
Os nomes dos perfis podem conter letras, números, hífens e sublinhados.

Crie um arquivo TOML separado para cada perfil. Use chaves de configuração de nível superior no
arquivo do perfil; não as aninhe em `[profiles.profile-name]`.

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

Como o arquivo de perfil fica em uma camada acima da configuração-base do usuário e abaixo da
configuração do projeto e da CLI, ele só precisa conter os valores que diferem da
configuração-base. Os arquivos de perfil também podem substituir `model_catalog_json`; quando ambos os arquivos definem essa chave, o Codex usa o
valor do perfil.

A partir do Codex 0.134.0, `--profile` não lê mais `[profiles.profile-name]`
de `config.toml`, e o seletor de nível superior `profile = "profile-name"` não
tem mais suporte. Mova as configurações legadas de perfil para
`~/.codex/profile-name.config.toml`; depois, remova a tabela correspondente
`[profiles.profile-name]` e o seletor `profile = "profile-name"` de
`config.toml`.

## Substituições pontuais pela CLI

Além de editar `~/.codex/config.toml`, você pode substituir configurações em uma única execução pela CLI:

- Prefira flags específicas quando estiverem disponíveis (por exemplo, `--model`).
- Use `-c` / `--config` quando precisar substituir qualquer chave.

Exemplos:

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

Observações:

- As chaves podem usar a notação de ponto para definir valores aninhados (por exemplo, `mcp_servers.context7.enabled=false`).
- Os valores de `--config` são analisados como TOML. Em caso de dúvida, coloque o valor entre aspas para que o shell não o divida nos espaços.
- Se o valor não puder ser analisado como TOML, o Codex o trata como uma string.

## Locais de configuração e estado

O Codex armazena o estado local em `CODEX_HOME` (o padrão é `~/.codex`).

Arquivos comuns que você pode encontrar nesse local:

- `config.toml` (sua configuração local)
- `auth.json` (se você usar o armazenamento de credenciais em arquivo) ou o chaveiro do sistema operacional
- `history.jsonl` (se a persistência do histórico estiver ativada)
- Outros dados de estado específicos do usuário, como logs e caches

Para ver detalhes da autenticação (incluindo os modos de armazenamento de credenciais), consulte [Autenticação](/pt-BR/codex/auth). Para ver a lista completa das chaves de configuração, consulte [Referência de configuração](/pt-BR/codex/config-file/config-reference).

Para ver valores padrão, regras e habilidades compartilhados armazenados em repositórios ou caminhos do sistema, consulte [Configuração da equipe](/pt-BR/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config).

Se você só precisa direcionar o provedor integrado da OpenAI para um proxy de LLM, um roteador ou um projeto com residência de dados ativada, defina `openai_base_url` em `config.toml` em vez de definir um novo provedor. Isso altera a URL base do provedor integrado `openai` sem exigir uma entrada `model_providers.<id>` separada.

```toml
openai_base_url = "https://us.api.openai.com/v1"

## Arquivos de configuração do projeto (`.codex/config.toml`)

Além da configuração do usuário, o Codex lê substituições no escopo do projeto em arquivos `.codex/config.toml` dentro do repositório. O Codex percorre os diretórios desde a raiz do projeto até o diretório de trabalho atual e carrega cada `.codex/config.toml` que encontrar. Se vários arquivos definirem a mesma chave, prevalece o arquivo mais próximo do diretório de trabalho.

Por segurança, o Codex só carrega arquivos de configuração no escopo do projeto quando o projeto é confiável. Se o projeto não for confiável, o Codex ignora as camadas `.codex/` do projeto, incluindo `.codex/config.toml`, hooks locais do projeto e regras locais do projeto. As camadas do usuário e do sistema permanecem separadas e continuam sendo carregadas.

Os caminhos relativos em uma configuração de projeto (por exemplo, `model_instructions_file`) são resolvidos em relação à pasta `.codex/` que contém o arquivo `config.toml`.

Os arquivos de configuração do projeto não podem substituir configurações que redirecionem credenciais, alterem
metadados de solicitações do aplicativo controlados pelo host, mudem a autenticação do provedor, selecionem perfis de configuração
ou executem, na máquina local, comandos de notificação ou telemetria. O Codex ignora as
seguintes chaves no arquivo local do projeto `.codex/config.toml` e exibe um aviso de inicialização
quando as encontra: `openai_base_url`, `chatgpt_base_url`,
`apps_mcp_product_sku`, `model_provider`, `model_providers`, `notify`,
`profile`, `profiles`, `experimental_realtime_ws_base_url` e `otel`. Defina
as chaves de provedor, notificação e telemetria no arquivo
`~/.codex/config.toml` do usuário; selecione perfis de configuração com `--profile profile-name`
e `~/.codex/profile-name.config.toml`.

## Hooks

O Codex também pode carregar hooks de ciclo de vida de arquivos `hooks.json` ou de tabelas
`[hooks]` incluídas em arquivos `config.toml` localizados junto às camadas de configuração ativas.

Na prática, os quatro locais mais úteis são:

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

Os hooks locais do projeto só são carregados quando a camada `.codex/` do projeto é considerada confiável.
Os hooks no nível do usuário não dependem da confiabilidade do projeto.

Os hooks definidos no próprio arquivo TOML usam a mesma estrutura de eventos de `hooks.json`:

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

Se uma camada contiver tanto `hooks.json` quanto uma tabela `[hooks]` incorporada, o Codex carregará
ambos e emitirá um aviso. Prefira uma única representação por camada.

Para ver a lista atual de eventos, os campos de entrada, o comportamento da saída e as limitações, consulte
[Hooks](/pt-BR/codex/hooks).

## Funções de agentes (`[agents]` em `config.toml`)

Para configurar funções de subagentes (`[agents]` em `config.toml`), consulte [Subagentes](/pt-BR/codex/agent-configuration/subagents).

## Detecção da raiz do projeto

O Codex encontra a configuração do projeto (por exemplo, camadas `.codex/` e `AGENTS.md`) subindo na hierarquia a partir do diretório de trabalho até chegar à raiz do projeto.

Por padrão, o Codex considera um diretório que contém `.git` como a raiz do projeto. Para personalizar esse comportamento, defina `project_root_markers` em `config.toml`:

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

Defina `project_root_markers = []` para não pesquisar os diretórios superiores e considerar o diretório de trabalho atual como a raiz do projeto.

## Provedores de modelos personalizados

Um provedor de modelos define como o Codex se conecta a um modelo (URL base, API de comunicação, autenticação e cabeçalhos HTTP opcionais). Os provedores personalizados não podem reutilizar os IDs reservados dos provedores integrados: `openai`, `ollama` e `lmstudio`.

Defina outros provedores e configure `model_provider` para apontar para eles:

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

Se um provedor personalizado oferecer suporte ao endpoint de Pesquisa na Web independente, declare
essa capacidade na configuração do provedor:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

Essa configuração usa `false` por padrão em provedores personalizados. A Pesquisa na Web independente está
em desenvolvimento e desativada por padrão. Definir essa capacidade do provedor como `true`
não ativa a pesquisa: o provedor precisa oferecer suporte a um endpoint compatível,
e o modelo e o ambiente de execução selecionados precisam oferecer suporte à pesquisa independente. O
[modo `web_search`](/pt-BR/codex/web-search) configurado e as
restrições de pesquisa gerenciadas continuam em vigor.

Adicione cabeçalhos de solicitação quando necessário:

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

Use autenticação baseada em comando quando um provedor precisar que o Codex obtenha tokens bearer de um auxiliar externo de credenciais:

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

O comando de autenticação não recebe nenhuma entrada por `stdin` e deve imprimir o token em stdout. O Codex remove os espaços em branco no início e no fim, trata um token vazio como erro e o renova de forma proativa no intervalo definido por `refresh_interval_ms`; defina `refresh_interval_ms = 0` para renová-lo somente após uma nova tentativa de autenticação. Não combine `[model_providers.<id>.auth]` com `env_key`, `experimental_bearer_token` ou `requires_openai_auth`.

### Provedor do Amazon Bedrock

O Codex inclui um provedor de modelos `amazon-bedrock` integrado. Defina-o diretamente como valor de
`model_provider`; ao contrário dos provedores personalizados, esse provedor integrado oferece suporte apenas
às substituições aninhadas de perfil e região da AWS.

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

Se você omitir `profile`, o Codex usa a cadeia de credenciais padrão da AWS. Defina
`region` como a região compatível do Bedrock que deve processar as solicitações.

Para ver o fluxo completo de configuração, as opções de autenticação, os modelos compatíveis e a disponibilidade
dos recursos, consulte [Usar o ChatGPT Work e o Codex com o Amazon
Bedrock](/pt-BR/codex/amazon-bedrock).

## Modo OSS (provedores locais)

O Codex pode ser executado com um provedor local de "código aberto", como Ollama ou LM
Studio, quando você passa `--oss`. Escolha um para uma única execução com
`--local-provider` ou defina `oss_provider` como padrão. Se nenhuma dessas opções estiver definida, a
CLI interativa solicita que você escolha um; o comando `codex exec` termina com erro.

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Provedor do Azure e ajustes específicos por provedor

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

Para alterar a URL base do provedor integrado da OpenAI, use `openai_base_url`; não crie `[model_providers.openai]`, pois não é possível substituir os IDs dos provedores integrados.

## Organizações da API que usam residência de dados

Projetos criados com a [residência de dados](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt) ativada podem criar um provedor de modelos para atualizar `base_url` com o [prefixo correto](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency). Para workspaces do ChatGPT com residência de dados, não é necessário um provedor personalizado; o Codex respeita as configurações de residência do workspace quando você entra com o ChatGPT.

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## Raciocínio do modelo, nível de detalhamento e limites

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` se aplica apenas aos provedores que usam a Responses API. Os provedores de Chat Completions ignoram essa configuração.

## Políticas de aprovação e modos de sandbox

Escolha o grau de rigor das aprovações (isso afeta quando o Codex faz uma pausa) e o nível do sandbox (isso afeta o acesso a arquivos e à rede).

Para ver detalhes operacionais que devem ser considerados ao editar `config.toml`, consulte [Combinações comuns de sandbox e aprovação](/pt-BR/codex/agent-approvals-security#common-sandbox-and-approval-combinations), [Caminhos protegidos em raízes graváveis](/pt-BR/codex/agent-approvals-security#protected-paths-in-writable-roots) e [Acesso à rede](/pt-BR/codex/agent-approvals-security#network-access).

Para conhecer os perfis de permissão em versão beta que configuram em conjunto o acesso ao sistema de arquivos e à rede, consulte [Permissões](/pt-BR/codex/permissions).

Você também pode usar uma política de aprovação granular (`approval_policy = { granular = { ... } }`) para permitir ou rejeitar automaticamente categorias específicas de prompts. Isso é útil quando você quer aprovações interativas normais em alguns casos, mas quer que outros, como `request_permissions` ou prompts de scripts de Habilidades, sejam rejeitados automaticamente por padrão.

Defina `approvals_reviewer = "auto_review"` para encaminhar solicitações interativas de aprovação
elegíveis para a revisão automática. Isso muda o revisor, não o limite que o sandbox
impõe.

Use `[auto_review].policy` para fornecer instruções locais de política ao revisor. A configuração gerenciada
`guardian_policy_config` tem precedência.

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### Perfis de permissão nomeados

Para conhecer os perfis integrados, a sintaxe de perfis personalizados e o modelo completo de configuração do sistema de arquivos e
da rede, consulte [Permissões](/pt-BR/codex/permissions).

Para ver a lista completa de chaves e as restrições dos requisitos, consulte
[Referência de configuração](/pt-BR/codex/config-file/config-reference) e
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

  No modo workspace-write, alguns ambientes mantêm `.git/` e `.codex/`
  no modo somente leitura, mesmo quando é possível gravar no restante do workspace. Por isso,
  comandos como `git commit` talvez ainda precisem de aprovação para serem executados fora do
  sandbox. Se quiser impedir que o Codex execute comandos específicos (por exemplo, para bloquear `git
  commit` fora do sandbox), use as
<a href="/codex/agent-configuration/rules">regras</a>.

Desative totalmente o ambiente isolado (use apenas se seu ambiente já isola processos):

```toml
sandbox_mode = "danger-full-access"

## Política de ambiente do shell

`shell_environment_policy` controla quais variáveis de ambiente o Codex repassa aos
comandos executados. Comece com um ambiente vazio usando `inherit = "none"` ou
herde um conjunto reduzido usando `inherit = "core"`. Adicione valores explícitos e filtros por chave
para evitar repassar segredos desnecessários aos comandos executados.

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

Os padrões de filtro não diferenciam maiúsculas de minúsculas e aceitam `*` e `?`. Use `"exclude"`
para remover variáveis correspondentes. Quando algum padrão usa `"include"`, o Codex mantém
apenas as variáveis que correspondem a um padrão de inclusão. Os padrões de inclusão não restauram variáveis
que já foram excluídas. As chaves de filtro são mescladas sem diferenciar maiúsculas de minúsculas entre as
camadas de configuração.

`ignore_default_excludes` usa `true` como padrão, portanto o Codex não remove automaticamente
nomes de variáveis que contenham `KEY`, `SECRET` ou `TOKEN`. Defina essa opção como `false`
para aplicar essas exclusões automáticas antes dos seus filtros explícitos.

Primeiro, o Codex aplica as exclusões automáticas; depois, as exclusões personalizadas, os valores definidos em
`set` e, por fim, a lista de permissões com padrões de inclusão. Como `set` é aplicado após as
exclusões, ele pode restaurar uma variável excluída. Uma lista de permissões com padrões de inclusão
ainda pode remover esse valor restaurado.

Os arrays antigos `exclude` e `include_only` continuam sendo aceitos em configurações
existentes. Não combine nenhum desses arrays com
`[shell_environment_policy.filters]` na mesma camada de configuração; o Codex
rejeita essa combinação.

## Servidores MCP

Para ver detalhes de configuração, consulte a [documentação dedicada ao MCP](/pt-BR/codex/extend/mcp).

## Observabilidade e telemetria

Ative a exportação de logs do OpenTelemetry (OTel) para acompanhar as execuções do Codex (solicitações à API, SSE/eventos, prompts, aprovações/resultados de ferramentas). Ela fica desativada por padrão; ative-a por meio de `[otel]`:

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

Escolha um exportador:

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Com `exporter = "none"`, o Codex registra eventos, mas não envia nada. Os exportadores agrupam os eventos em lotes de forma assíncrona e enviam os lotes pendentes no encerramento. Os metadados dos eventos incluem o nome do serviço, a versão da CLI, a tag do ambiente, o ID da conversa, o modelo, as configurações de sandbox/aprovação e os campos específicos de cada evento (consulte a [Referência de configuração](/pt-BR/codex/config-file/config-reference)).

### O que é emitido

O Codex emite eventos de log estruturados para execuções e uso de ferramentas. Alguns tipos de evento representativos são:

- `codex.conversation_starts` (modelo, configurações de raciocínio, política de sandbox/aprovação)
- `codex.api_request` (tentativa, status/sucesso, duração e detalhes do erro)
- `codex.sse_event` (tipo de evento de streaming, sucesso/falha, duração e contagens de tokens em `response.completed`)
- `codex.websocket_request` e `codex.websocket_event` (duração da solicitação e tipo/sucesso/erro de cada mensagem)
- `codex.user_prompt` (tamanho; conteúdo ocultado, a menos que seja ativado explicitamente)
- `codex.tool_decision` (aprovação/negação e se a decisão veio da configuração ou do usuário)
- `codex.tool_result` (duração, sucesso, trecho da saída)

### Métricas OTel emitidas

Quando o pipeline de métricas OTel está ativado, o Codex emite contadores e histogramas de duração para atividades de API, streaming e ferramentas.

Cada métrica abaixo também inclui tags padrão de metadados: `auth_mode`, `originator`, `session_source`, `model` e `app.version`.

| Métrica                                | Tipo      | Campos              | Descrição                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | contador   | `status`, `success` | Contagem de solicitações à API por status HTTP e sucesso/falha.             |
| `codex.api_request.duration_ms`       | histograma | `status`, `success` | Duração da solicitação à API em milissegundos.                             |
| `codex.sse_event`                     | contador   | `kind`, `success`   | Contagem de eventos SSE por tipo de evento e sucesso/falha.                |
| `codex.sse_event.duration_ms`         | histograma | `kind`, `success`   | Duração do processamento de eventos SSE em milissegundos.                    |
| `codex.websocket.request`             | contador   | `success`           | Contagem de solicitações WebSocket por sucesso/falha.                       |
| `codex.websocket.request.duration_ms` | histograma | `success`           | Duração das solicitações WebSocket em milissegundos.                       |
| `codex.websocket.event`               | contador   | `kind`, `success`   | Contagem de mensagens/eventos WebSocket por tipo e sucesso/falha.        |
| `codex.websocket.event.duration_ms`   | histograma | `kind`, `success`   | Duração do processamento de mensagens/eventos WebSocket em milissegundos.      |
| `codex.tool.call`                     | contador   | `tool`, `success`   | Contagem de invocações de ferramentas por nome da ferramenta e sucesso/falha.           |
| `codex.tool.call.duration_ms`         | histograma | `tool`, `success`   | Duração da execução da ferramenta em milissegundos, por nome da ferramenta e resultado. |

Para mais orientações sobre segurança e privacidade relacionadas à telemetria, consulte [Segurança](/pt-BR/codex/agent-approvals-security#monitoring-and-telemetry).

### Métricas

Por padrão, o Codex envia periodicamente à OpenAI uma pequena quantidade de dados anônimos sobre uso e integridade. Isso ajuda a detectar quando o Codex não está funcionando corretamente e indica quais recursos e opções de configuração estão sendo usados, para que a equipe do Codex possa se concentrar no que é mais importante. Essas métricas não contêm informações de identificação pessoal (PII). A coleta de métricas é independente da exportação de logs e rastreamentos do OTel.

Se quiser desativar totalmente a coleta de métricas em uma máquina para o aplicativo do ChatGPT para desktop, a Codex CLI e a extensão para IDE, defina a flag de análise na sua configuração:

```toml
[analytics]
enabled = false

Cada métrica inclui seus próprios campos, além dos campos de contexto padrão abaixo.

#### Campos de contexto padrão (aplicáveis a todos os eventos e métricas)

- `auth_mode`: `swic` | `api` | `unknown`.
- `model`: nome do modelo usado.
- `app.version`: versão do Codex.

#### Catálogo de métricas

Cada métrica inclui os campos obrigatórios, além dos campos de contexto padrão acima. Os nomes das métricas abaixo omitem o prefixo `codex.`.
A maioria dos nomes de métricas está centralizada em `codex-rs/otel/src/metrics/names.rs`; as métricas específicas de recursos emitidas fora desse arquivo também estão incluídas aqui.
Se uma métrica incluir o campo `tool`, esse campo representa a ferramenta interna usada (por exemplo, `apply_patch` ou `shell`) e não contém o comando de shell real nem o patch que `codex` está tentando aplicar.

#### Tempo de execução e transporte do modelo

| Métrica                                          | Tipo      | Campos               | Descrição                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | contador   | `status`, `success`  | Contagem de solicitações à API por status HTTP e sucesso/falha.        |
| `api_request.duration_ms`                       | histograma | `status`, `success`  | Duração das solicitações à API em milissegundos.                        |
| `sse_event`                                     | contador   | `kind`, `success`    | Contagem de eventos SSE por tipo de evento e sucesso/falha.           |
| `sse_event.duration_ms`                         | histograma | `kind`, `success`    | Duração do processamento de eventos SSE em milissegundos.               |
| `websocket.request`                             | contador   | `success`            | Contagem de solicitações via WebSocket por sucesso/falha.                  |
| `websocket.request.duration_ms`                 | histograma | `success`            | Duração das solicitações via WebSocket em milissegundos.                  |
| `websocket.event`                               | contador   | `kind`, `success`    | Contagem de mensagens/eventos via WebSocket por tipo e sucesso/falha.   |
| `websocket.event.duration_ms`                   | histograma | `kind`, `success`    | Duração do processamento de mensagens/eventos via WebSocket em milissegundos. |
| `responses_api_overhead.duration_ms`            | histograma |                      | Tempo de sobrecarga da Responses API nas respostas via WebSocket.      |
| `responses_api_inference_time.duration_ms`      | histograma |                      | Tempo de inferência da Responses API nas respostas via WebSocket.     |
| `responses_api_engine_iapi_ttft.duration_ms`    | histograma |                      | Tempo até o primeiro token da IAPI do mecanismo da Responses API.        |
| `responses_api_engine_service_ttft.duration_ms` | histograma |                      | Tempo até o primeiro token do serviço do mecanismo da Responses API.     |
| `responses_api_engine_iapi_tbt.duration_ms`     | histograma |                      | Tempo entre tokens da IAPI do mecanismo da Responses API.         |
| `responses_api_engine_service_tbt.duration_ms`  | histograma |                      | Tempo entre tokens do serviço do mecanismo da Responses API.      |
| `transport.fallback_to_http`                    | contador   | `from_wire_api`      | Contagem de fallbacks de WebSocket para HTTP.                            |
| `remote_models.fetch_update.duration_ms`        | histograma |                      | Tempo para buscar definições de modelos remotos.                      |
| `remote_models.load_cache.duration_ms`          | histograma |                      | Tempo para carregar o cache de modelos remotos.                         |
| `startup_prewarm.duration_ms`                   | histograma | `status`             | Duração do pré-aquecimento na inicialização por resultado.                         |
| `startup_prewarm.age_at_first_turn_ms`          | histograma | `status`             | Tempo decorrido desde o pré-aquecimento da inicialização até sua resolução pelo primeiro turno real.    |
| `cloud_requirements.fetch.duration_ms`          | histograma |                      | Duração da obtenção dos requisitos de nuvem gerenciados pelo workspace.         |
| `cloud_requirements.fetch_attempt`              | contador   | Ver observação             | Tentativas de obtenção dos requisitos de nuvem gerenciados pelo workspace.         |
| `cloud_requirements.fetch_final`                | contador   | Ver observação             | Resultado final da obtenção dos requisitos de nuvem gerenciados pelo workspace.    |
| `cloud_requirements.load`                       | contador   | `trigger`, `outcome` | Resultado do carregamento dos requisitos de nuvem gerenciados pelo workspace.           |

A métrica `cloud_requirements.fetch_attempt` inclui os campos `trigger`, `attempt`, `outcome` e `status_code`. A métrica `cloud_requirements.fetch_final` inclui os campos `trigger`, `outcome`, `reason`, `attempt_count` e `status_code`.

#### Atividade de turnos e ferramentas

| Métrica                                 | Tipo      | Campos                                                                    | Descrição                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | histograma |                                                                           | Tempo de ponta a ponta de um turno completo.                                                                                 |
| `turn.ttft.duration_ms`                | histograma |                                                                           | Tempo até o primeiro token de um turno.                                                                                  |
| `turn.ttfm.duration_ms`                | histograma |                                                                           | Tempo até o primeiro item de saída do modelo em um turno.                                                                      |
| `turn.network_proxy`                   | contador   | `active`, `tmp_mem_enabled`                                               | Se o proxy de rede gerenciado estava ativo durante o turno.                                                       |
| `turn.memory`                          | contador   | `read_allowed`, `feature_enabled`, `config_use_memories`, `has_citations` | Disponibilidade de leitura da memória e uso de citações da memória por turno.                                                     |
| `turn.tool.call`                       | histograma | `tmp_mem_enabled`                                                         | Número de chamadas de ferramentas no turno.                                                                                |
| `turn.token_usage`                     | histograma | `token_type`, `tmp_mem_enabled`                                           | Uso de tokens por turno, por tipo de token (`total`, `input`, `cached_input`, `output` ou `reasoning_output`).          |
| `tool.call`                            | contador   | `tool`, `success`                                                         | Contagem de invocações de ferramentas por nome da ferramenta e sucesso/falha.                                                          |
| `tool.call.duration_ms`                | histograma | `tool`, `success`                                                         | Duração da execução da ferramenta, em milissegundos, por nome da ferramenta e resultado.                                                |
| `tool.unified_exec`                    | contador   | `tty`                                                                     | Chamadas da ferramenta exec unificada por modo TTY.                                                                             |
| `approval.requested`                   | contador   | `tool`, `approved`                                                        | Resultado da solicitação de aprovação da ferramenta (`approved`, `approved_with_amendment`, `approved_for_session`, `denied`, `abort`). |
| `mcp.call`                             | contador   | Ver observação                                                                  | Resultado da invocação de ferramenta MCP.                                                                                      |
| `mcp.call.duration_ms`                 | histograma | Ver observação                                                                  | Duração da invocação de ferramenta MCP.                                                                                    |
| `mcp.tools.list.duration_ms`           | histograma | `cache`                                                                   | Duração da listagem de ferramentas MCP, incluindo o estado de acerto ou falha no cache.                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | histograma |                                                                           | Duração das buscas de ferramentas MCP que não encontram dados no cache.                                                                |
| `mcp.tools.cache_write.duration_ms`    | histograma |                                                                           | Duração das gravações no cache de ferramentas MCP do Codex Apps.                                                                    |
| `hooks.run`                            | contador   | `hook_name`, `source`, `status`                                           | Contagem de execuções de hooks por nome do hook, origem e status.                                                                 |
| `hooks.run.duration_ms`                | histograma | `hook_name`, `source`, `status`                                           | Duração da execução do hook em milissegundos.                                                                               |

As métricas `mcp.call` e `mcp.call.duration_ms` incluem `status`; as emissões normais de chamadas de ferramenta também incluem `tool`, além de `connector_id` e `connector_name` quando disponíveis. Chamadas MCP bloqueadas do Codex Apps podem emitir `mcp.call` apenas com `status`.

#### Threads, tarefas e recursos

| Métrica                            | Tipo      | Campos                | Descrição                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | contador   | `feature`, `value`    | Valores de recursos diferentes dos valores padrão (uma linha é emitida por valor não padrão).         |
| `status_line`                     | contador   |                       | Sessão iniciada com uma linha de status configurada.                                   |
| `model_warning`                   | contador   |                       | Aviso enviado ao modelo.                                                       |
| `thread.started`                  | contador   | `is_git`              | Nova thread criada, com uma tag que indica se o diretório de trabalho está em um repositório Git.    |
| `conversation.turn.count`         | contador   |                       | Turnos de usuário/assistente por thread, registrados ao final da thread.              |
| `thread.fork`                     | contador   | `source`              | Nova thread criada a partir do fork de uma thread existente.                                |
| `thread.rename`                   | contador   |                       | Thread renomeada.                                                                  |
| `thread.side`                     | contador   | `source`              | Conversa paralela criada.                                                       |
| `thread.skills.enabled_total`     | histograma |                       | Número de habilidades ativadas para uma nova thread.                                       |
| `thread.skills.kept_total`        | histograma |                       | Número de habilidades ativadas mantidas após a renderização do prompt.                            |
| `thread.skills.truncated`         | histograma |                       | Indica se a renderização das habilidades truncou a lista de habilidades ativadas (`1` ou `0`).          |
| `task.compact`                    | contador   | `type`                | Número de compactações por tipo (`remote` ou `local`), incluindo as manuais e automáticas. |
| `task.review`                     | contador   |                       | Número de revisões acionadas.                                                     |
| `task.undo`                       | contador   |                       | Número de ações de desfazer acionadas.                                                |
| `task.user_shell`                 | contador   |                       | Número de ações de shell do usuário (por exemplo, `!` na TUI).                       |
| `shell_snapshot`                  | contador   | Consulte a observação              | Indica se a captura de um snapshot do shell foi bem-sucedida.                                       |
| `shell_snapshot.duration_ms`      | histograma | `success`             | Tempo para capturar um snapshot do shell.                                                   |
| `skill.injected`                  | contador   | `status`, `skill`     | Resultados da injeção de habilidades por habilidade.                                               |
| `plugins.startup_sync`            | contador   | `transport`, `status` | Tentativas de sincronização dos plug-ins selecionados durante a inicialização.                                            |
| `plugins.startup_sync.final`      | contador   | `transport`, `status` | Resultado final da sincronização dos plug-ins selecionados durante a inicialização.                                       |
| `multi_agent.spawn`               | contador   | `role`                | Criações de agentes por função.                                                            |
| `multi_agent.resume`              | contador   |                       | Retomadas de agentes.                                                                   |
| `multi_agent.nickname_pool_reset` | contador   |                       | Redefinições do conjunto de apelidos dos agentes.                                                      |

A métrica `shell_snapshot` inclui `success` e, em caso de falha, `failure_reason`.

#### Memória e estado local

| Métrica                         | Tipo      | Campos                    | Descrição                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | contador   | `status`                  | Contagem de tarefas da fase 1 da memória por status.                      |
| `memory.phase1.e2e_ms`         | histograma |                           | Duração de ponta a ponta da fase 1 da memória.                   |
| `memory.phase1.output`         | contador   |                           | Saídas gravadas na fase 1 da memória.                           |
| `memory.phase1.token_usage`    | histograma | `token_type`              | Uso de tokens na fase 1 da memória por tipo de token.                 |
| `memory.phase2`                | contador   | `status`                  | Contagem de tarefas da fase 2 da memória por status.                      |
| `memory.phase2.e2e_ms`         | histograma |                           | Duração de ponta a ponta da fase 2 da memória.                   |
| `memory.phase2.input`          | contador   |                           | Contagem de entradas da fase 2 da memória.                               |
| `memory.phase2.token_usage`    | histograma | `token_type`              | Uso de tokens na fase 2 da memória por tipo de token.                 |
| `memories.usage`               | contador   | `kind`, `tool`, `success` | Uso da memória por tipo, ferramenta e sucesso/falha.          |
| `external_agent_config.detect` | contador   | Consulte a observação                  | Detecções de configurações de agentes externos por tipo de item de migração.  |
| `external_agent_config.import` | contador   | Consulte a observação                  | Importações de configurações de agentes externos por tipo de item de migração.     |
| `db.backfill`                  | contador   | `status`                  | Resultados do preenchimento retroativo inicial do banco de dados de estado (`upserted`, `failed`). |
| `db.backfill.duration_ms`      | histograma | `status`                  | Duração do preenchimento retroativo inicial do banco de dados de estado.                |
| `db.error`                     | contador   | `stage`                   | Erros durante operações no banco de dados de estado.                        |

As métricas `external_agent_config.detect` e `external_agent_config.import` incluem `migration_type`; as migrações de habilidades também incluem `skills_count`.

#### Sandbox do Windows

| Métrica                                           | Tipo      | Campos                                    | Descrição                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | contador   | `originator`, `mode`                      | Configurações bem-sucedidas do Sandbox do Windows.                      |
| `windows_sandbox.setup_failure`                  | contador   | `originator`, `mode`                      | Falhas na configuração do Sandbox do Windows.                       |
| `windows_sandbox.setup_duration_ms`              | histograma | `result`, `originator`, `mode`            | Duração da configuração do Sandbox do Windows.                       |
| `windows_sandbox.elevated_setup_success`         | contador   |                                           | Configurações bem-sucedidas do Sandbox do Windows com privilégios elevados.             |
| `windows_sandbox.elevated_setup_failure`         | contador   | Consulte a observação                                  | Falhas na configuração do Sandbox do Windows com privilégios elevados.              |
| `windows_sandbox.elevated_setup_canceled`        | contador   | Consulte a observação                                  | Tentativas canceladas de configuração do Sandbox do Windows com privilégios elevados.     |
| `windows_sandbox.elevated_setup_duration_ms`     | histograma | `result`                                  | Duração da configuração do Sandbox do Windows com privilégios elevados.              |
| `windows_sandbox.elevated_prompt_shown`          | contador   |                                           | Prompt de configuração do Sandbox com privilégios elevados exibido.                  |
| `windows_sandbox.elevated_prompt_accept`         | contador   |                                           | Prompt de configuração do Sandbox com privilégios elevados aceito.               |
| `windows_sandbox.elevated_prompt_use_legacy`     | contador   |                                           | O usuário escolheu o Sandbox legado no prompt de configuração com privilégios elevados.   |
| `windows_sandbox.elevated_prompt_quit`           | contador   |                                           | O usuário optou por sair no prompt de configuração com privilégios elevados.                   |
| `windows_sandbox.fallback_prompt_shown`          | contador   |                                           | Prompt alternativo do sandbox exibido.                        |
| `windows_sandbox.fallback_retry_elevated`        | contador   |                                           | O usuário tentou novamente a configuração com privilégios elevados a partir do prompt alternativo. |
| `windows_sandbox.fallback_use_legacy`            | contador   |                                           | O usuário escolheu o sandbox legado no prompt alternativo.   |
| `windows_sandbox.fallback_prompt_quit`           | contador   |                                           | O usuário optou por sair no prompt alternativo.                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | contador   | Consulte a observação                                  | Falha na verificação prévia da configuração do sandbox legado do Windows.       |
| `windows_sandbox.setup_elevated_sandbox_command` | contador   |                                           | Comando de configuração do sandbox com privilégios elevados invocado.               |
| `windows_sandbox.createprocessasuserw_failed`    | contador   | `error_code`, `path_kind`, `exe`, `level` | Falhas de `CreateProcessAsUserW` no Windows.              |

As métricas de falha da configuração com privilégios elevados incluem `code` e `message` quando há detalhes disponíveis sobre a falha na configuração do Windows e podem incluir `originator` quando são emitidas pelo fluxo compartilhado de configuração. A métrica `windows_sandbox.legacy_setup_preflight_failed` inclui `originator` quando é emitida pelo fluxo compartilhado de configuração, mas as falhas de verificação prévia originadas no prompt alternativo podem não incluir nenhum campo.

### Controles de feedback

Por padrão, os clientes locais permitem que os usuários enviem feedback por meio de `/feedback`. Para desativar a coleta de feedback no aplicativo do ChatGPT para desktop, no Codex CLI e na extensão para IDE em um computador, atualize sua configuração:

```toml
[feedback]
enabled = false

Quando a coleta está desativada, `/feedback` exibe uma mensagem informando que o feedback está desativado, e o Codex rejeita os envios de feedback.

### Ocultar ou exibir eventos de raciocínio

Se quiser reduzir o ruído gerado pela saída de "raciocínio" (por exemplo, em logs de CI), você pode suprimi-la:

```toml
hide_agent_reasoning = true

Se quiser exibir o conteúdo bruto de raciocínio quando um modelo o emitir:

```toml
show_raw_agent_reasoning = true

Ative o raciocínio bruto somente se isso for aceitável para seu fluxo de trabalho. Alguns modelos/provedores (como `gpt-oss`) não emitem raciocínio bruto; nesse caso, essa configuração não produz nenhum efeito visível.

## Notificações

Use `notify` para acionar um programa externo sempre que o Codex emitir eventos compatíveis (no momento, apenas `agent-turn-complete`). Isso é útil para notificações pop-up na área de trabalho, webhooks de chat, atualizações de CI ou qualquer alerta por canal secundário não contemplado pelas notificações integradas da TUI.

```toml
notify = ["python3", "/path/to/notify.py"]

Exemplo de `notify.py` (truncado) que reage a `agent-turn-complete`:

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

O script recebe um único argumento JSON. Os campos comuns incluem:

- `type` (atualmente `agent-turn-complete`)
- `thread-id` (identificador da sessão)
- `turn-id` (identificador do turno)
- `cwd` (diretório de trabalho)
- `input-messages` (mensagens do usuário que deram origem ao turno)
- `last-assistant-message` (texto da última mensagem do assistente)

Coloque o script em algum local do disco e configure `notify` para apontar para ele.

#### `notify` versus `tui.notifications`

- `notify` executa um programa externo (ideal para webhooks, notificadores da área de trabalho e hooks de CI).
- `tui.notifications` é integrado à TUI e, opcionalmente, pode filtrar por tipo de evento (por exemplo, `agent-turn-complete` e `approval-requested`).
- `tui.notification_method` controla como a TUI emite notificações do terminal (`auto`, `osc9` ou `bel`).
- `tui.notification_condition` controla se as notificações da TUI são disparadas apenas quando
  o terminal está `unfocused` ou em todos os casos (`always`).

No modo `auto`, o Codex prioriza as notificações OSC 9 (uma sequência de escape do terminal que alguns terminais interpretam como uma notificação da área de trabalho) e, caso contrário, recorre a BEL (`\x07`).

Consulte a [Referência de configuração](/pt-BR/codex/config-file/config-reference) para ver as chaves exatas.

## Persistência do histórico

Por padrão, o Codex salva as transcrições das sessões locais em `CODEX_HOME` (por exemplo, `~/.codex/history.jsonl`). Para desativar a persistência do histórico local:

```toml
[history]
persistence = "none"

Para limitar o tamanho do arquivo de histórico, defina `history.max_bytes`. Quando o arquivo excede esse limite, o Codex descarta as entradas mais antigas e compacta o arquivo, mantendo os registros mais recentes.

```toml
[history]
max_bytes = 104857600 # 100 MiB

## Citações clicáveis

Se você usa uma integração de terminal/editor compatível, o Codex pode renderizar citações de arquivos como links clicáveis. Configure `file_opener` para escolher o esquema de URI usado pelo Codex:

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

Exemplo: uma citação como `/home/user/project/main.py:42` pode ser reescrita como um link clicável no formato `vscode://file/...:42`.

## Identificação das instruções do projeto

O Codex lê `AGENTS.md` e arquivos relacionados e inclui uma quantidade limitada de orientações do projeto no primeiro turno de uma sessão. Duas configurações controlam esse funcionamento:

- `project_doc_max_bytes`: quanto conteúdo ler de cada arquivo `AGENTS.md`
- `project_doc_fallback_filenames`: outros nomes de arquivo a verificar quando não houver `AGENTS.md` em determinado nível de diretório

Para ver um passo a passo detalhado, consulte [Instruções personalizadas com AGENTS.md](/pt-BR/codex/agent-configuration/agents-md).

## Desktop

As opções desta seção se aplicam somente ao aplicativo do ChatGPT para desktop.

### Adicionar manipuladores de arquivos personalizados

No arquivo `~/.codex/config.toml` do usuário, adicione entradas em
`desktop.custom_file_handlers` para abrir arquivos em editores ou inicializadores internos
aos quais o aplicativo do ChatGPT para desktop não oferece suporte por padrão. Cada entrada adiciona uma
opção de editor aos menus **Abrir em** do aplicativo. O aplicativo exibe a opção quando
`command` é um caminho absoluto existente ou pode ser encontrado no `PATH` do aplicativo.

O exemplo a seguir mostra três maneiras de passar um arquivo para um manipulador:

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

Salve `config.toml` e reinicie o aplicativo do ChatGPT para desktop.

O ID do manipulador é o último segmento do cabeçalho da tabela TOML. Ele deve ter
de 1 a 64 caracteres, começar com uma letra ou um número ASCII e, no restante, conter
somente letras ASCII, números, pontos, caracteres de sublinhado ou hífens. O aplicativo expõe
o ID com o prefixo `custom:`; por exemplo, `company_editor` se torna
`custom:company_editor`. Coloque entre aspas um ID que contenha um ponto para que o TOML não
o interprete como uma tabela aninhada. Por exemplo:

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

Cada manipulador aceita estes campos:

| Campo          | Obrigatório | Descrição                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | Sim      | Nome de exibição no aplicativo.                                                                                                                                                 |
| `icon`         | Sim      | Ícone de aplicativo incluído no pacote, como `apps/vscode.png`, URL `data:image/...` em base64, URI `file:` ou caminho absoluto para uma imagem local. Se a origem não for compatível, será usado o ícone padrão do VS Code. |
| `command`      | Sim      | Caminho do executável ou nome do comando a ser detectado e iniciado.                                                                                                                    |
| `args`         | Não       | Array de strings inserido entre `command` e a entrada do arquivo. O padrão é `[]`.                                                                                            |
| `input`        | Não       | Como o aplicativo envia a entrada do arquivo: `path`, `json_argument` ou `json_stdin`. O padrão é `path`.                                                                              |
| `supports_ssh` | Não       | Indica se o manipulador deve ser disponibilizado para arquivos em workspaces SSH. O padrão é `false`. Use `json_stdin` quando o manipulador precisar dos detalhes do host remoto e do caminho.                     |

O valor de `input` define o que vem depois de `args`:

- `path` adiciona o caminho como o último argumento do comando.
- `json_argument` adiciona um objeto JSON com os campos `target`, `path`, `appPath` e
`location`. O valor de `location` é um objeto com valores de `line` e
`column` indexados a partir de 1, ou é `null`.
- `json_stdin` grava o objeto JSON na entrada padrão, em vez de adicionar um
  argumento. O objeto também inclui `hostConfig`, `remoteWorkspaceRoot` e
`remotePath`; esses campos são `null` quando não se aplicam.

Por exemplo, `company_editor` pode receber este argumento quando o usuário abre uma
posição específica no código-fonte:

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

Ao selecionar um manipulador personalizado como editor preferencial, a escolha é mantida da mesma
forma que ao selecionar um editor integrado, inclusive nas preferências específicas de cada projeto.

## Opções da TUI

Executar `codex` sem nenhum subcomando inicia a interface de usuário interativa no terminal (TUI). O Codex disponibiliza algumas opções de configuração específicas da TUI em `[tui]`, incluindo:

- `tui.notifications`: ativar/desativar notificações ou restringi-las a tipos específicos
- `tui.notification_method`: escolher `auto`, `osc9` ou `bel` para as notificações do terminal
- `tui.notification_condition`: escolher `unfocused` ou `always` para definir quando
  as notificações são disparadas
- `tui.animations`: ativar/desativar animações ASCII e efeitos de cintilação
- `tui.alternate_screen`: controlar o uso da tela alternativa (defina como `never` para manter o histórico de rolagem do terminal)
- `tui.show_tooltips`: mostrar ou ocultar dicas de introdução na tela de boas-vindas

O padrão de `tui.notification_method` é `auto`. No modo `auto`, o Codex dá preferência a notificações OSC 9 (uma sequência de escape do terminal que alguns terminais interpretam como uma notificação da área de trabalho) quando o terminal parece oferecer suporte a elas; caso contrário, usa BEL (`\x07`) como alternativa.

Consulte a [Referência de configuração](/pt-BR/codex/config-file/config-reference) para ver a lista completa de chaves.
