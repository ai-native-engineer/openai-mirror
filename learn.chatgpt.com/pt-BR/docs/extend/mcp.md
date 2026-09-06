<!-- source: https://learn.chatgpt.com/pt-BR/docs/extend/mcp -->

O Model Context Protocol (MCP) conecta modelos a ferramentas e contexto. Use-o para
dar ao ChatGPT ou ao Codex acesso à documentação de terceiros ou permitir que eles
interajam com ferramentas de desenvolvimento, como seu navegador ou o Figma.

O ChatGPT na Web pode usar ferramentas remotas baseadas em MCP fornecidas por plug-ins. Os clientes locais do Codex
também podem se conectar diretamente a servidores MCP e compartilhar a mesma configuração.

<a id="supported-mcp-features"></a>

O aplicativo do ChatGPT para desktop, o Codex CLI e a extensão para IDE oferecem suporte a servidores MCP e
compartilham a configuração MCP de um mesmo host do Codex.

Os recursos de servidor descritos abaixo se aplicam aos servidores MCP configurados em um
host do Codex. As ferramentas hospedadas de plug-ins podem ter capacidades diferentes.

## Recursos MCP compatíveis

- **Servidores STDIO**: servidores executados como um processo local (iniciado por um comando).
  - Variáveis do ambiente
- **Servidores Streamable HTTP**: servidores acessados por um endereço.
  - Autenticação por token bearer
  - Autenticação OAuth, incluindo documentos de metadados de ID do cliente (CIMD) e
registro dinâmico de clientes (DCR)
  - Autenticação por sessão do ChatGPT para servidores próprios confiáveis
- **Instruções do servidor**: o Codex lê o campo `instructions` do MCP retornado durante a inicialização e o usa como orientação para todo o servidor, em conjunto com as ferramentas do servidor.

Se você desenvolver ou mantiver um servidor MCP para o Codex, use `instructions` para fluxos de trabalho entre ferramentas, restrições e limites de taxa aplicáveis a todo o servidor. Garanta que os primeiros 512 caracteres façam sentido por conta própria para que as orientações mais importantes estejam disponíveis quando o Codex decidir como usar o servidor.

## Conecte o Codex a um servidor MCP

O Codex armazena a configuração MCP em `config.toml`, junto com outras configurações do Codex. Por padrão, esse arquivo é `~/.codex/config.toml`, mas você também pode limitar o escopo dos servidores MCP a um projeto com `.codex/config.toml` (somente em projetos confiáveis).

O aplicativo do ChatGPT para desktop, o Codex CLI e a extensão para IDE compartilham essa configuração.
Depois de configurar seus servidores MCP, você pode alternar entre esses clientes sem
refazer a configuração.

### Configure no aplicativo do ChatGPT para desktop

1. Abra **Configurações** e selecione **Servidores MCP**.
2. Selecione **Adicionar servidor**.
3. Insira um nome, escolha **STDIO** ou **Streamable HTTP** e informe o
   comando ou a URL do servidor.
4. Salve o servidor e selecione **Reiniciar**.

A lista de servidores mostra quais estão habilitados e quais exigem OAuth. Selecione
**Autenticar** quando um servidor OAuth exigir login. No editor, digite `/mcp`
para ver os servidores conectados.

## Use ferramentas baseadas em MCP no ChatGPT na Web

Em um chat hospedado no ChatGPT Work, instale um [plug-in](/pt-BR/codex/plugins) para usar os
conectores e as ferramentas MCP remotas incluídos nele. Depois da instalação, Chat e Work podem
usar essas ferramentas. Os administradores do workspace podem controlar quais plug-ins e ferramentas
ficam disponíveis.

O ChatGPT na Web não lê os arquivos locais de configuração do Codex nem disponibiliza o menu local
de comandos do Codex. Abra a aba **Plug-ins** para explorar e gerenciar as ferramentas
disponíveis.

### Configure com a CLI

#### Adicione um servidor MCP

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

Por exemplo, para adicionar o Context7 (um servidor MCP gratuito de documentação para desenvolvedores), você pode executar o seguinte comando:

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### Outros comandos da CLI

Execute `codex mcp list` para ver os servidores configurados. Para ver todos os comandos MCP
disponíveis, execute `codex mcp --help`. Para um servidor compatível com OAuth, execute
`codex mcp login <server-name>`.

#### Interface de usuário do terminal (TUI)

Na TUI do `codex`, use `/mcp` para ver seus servidores MCP ativos.

### Configure na extensão para IDE

1. Abra o menu do ícone de engrenagem e selecione **Servidores MCP**.
2. Selecione **Adicionar servidor**.
3. Insira um nome, escolha **STDIO** ou **Streamable HTTP** e informe o
   comando ou a URL do servidor.
4. Salve o servidor e selecione **Reiniciar extensão**.

A lista de servidores MCP mostra quais estão habilitados e quais exigem OAuth.
Selecione **Autenticar** quando um servidor OAuth exigir login.

### Configure com config.toml

Para ter um controle mais detalhado, edite `~/.codex/config.toml` ou um arquivo
`.codex/config.toml` específico de um projeto. Consulte a [referência de configuração](/pt-BR/codex/config-file/config-reference)
para ver uma lista pesquisável com todas as opções MCP compatíveis.

Configure cada servidor MCP com uma tabela `[mcp_servers.<server-name>]` no arquivo de configuração.

<a id="stdio-servers"></a>

#### Servidores STDIO

- `command` (obrigatório): o comando que inicia o servidor.
- `args` (opcional): argumentos a serem passados ao servidor.
- `env` (opcional): variáveis do ambiente a serem definidas para o servidor.
- `env_vars` (opcional): variáveis do ambiente a serem permitidas e encaminhadas.
- `cwd` (opcional): diretório de trabalho a partir do qual o servidor será iniciado.
- `experimental_environment` (opcional): defina como `remote` para iniciar o servidor stdio
  por meio do ambiente de um executor remoto, quando disponível.

`env_vars` pode conter nomes simples de variáveis ou objetos com uma origem:

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

Entradas de texto e entradas com `source = "local"` obtêm os valores do ambiente local do Codex.
Entradas com `source = "remote"` obtêm os valores do ambiente do executor remoto e exigem
a execução remota de servidores MCP via stdio.

<a id="streamable-http-servers"></a>

#### Servidores Streamable HTTP

- `url` (obrigatório): o endereço do servidor.
- `auth` (opcional): autenticação a ser tentada após os tokens bearer configurados e os
  cabeçalhos de autorização. Use `oauth` (o padrão) para as credenciais OAuth do MCP
  armazenadas. Use `chatgpt` para usar a sessão atual do ChatGPT na origem confiável
  do próprio ChatGPT, com as credenciais OAuth armazenadas como alternativa.
- `bearer_token_env_var` (opcional): nome da variável do ambiente que contém um token bearer a ser enviado no cabeçalho `Authorization`.
- `http_headers` (opcional): mapeamento de nomes de cabeçalhos para valores estáticos.
- `env_http_headers` (opcional): mapeamento de nomes de cabeçalhos para nomes de variáveis do ambiente (valores obtidos do ambiente).
- `http_headers_helper` (opcional): comando local que imprime um objeto JSON com
  nomes de cabeçalhos e valores de string, como `{"X-Auth": "temporary-token"}`.
  Compatível com conexões MCP via HTTP feitas a partir do ambiente local; não com
  servidores stdio nem com conexões feitas por meio de um ambiente de execução remota.

O Codex armazena em cache os cabeçalhos fornecidos pelo comando auxiliar para a conexão. Após uma requisição POST para a mesma origem
retornar `401` ou `403`, ele atualiza os cabeçalhos uma vez e só tenta novamente se o
comando auxiliar retornar valores diferentes. Tokens bearer explícitos e credenciais OAuth
têm precedência sobre um cabeçalho `Authorization` fornecido pelo comando auxiliar.
Uma resposta OAuth `403` que indique escopo insuficiente não aciona uma
atualização pelo comando auxiliar.

Se não for possível obter credenciais de nenhuma fonte, o Codex pode se conectar ao servidor sem
autenticação. Execute `codex mcp login <server-name>` separadamente para iniciar um login
OAuth no MCP.

#### Outras opções de configuração

- `startup_timeout_sec` (opcional): tempo limite (em segundos) para o servidor iniciar. Padrão: `10`.
- `tool_timeout_sec` (opcional): tempo limite (em segundos) para o servidor executar uma ferramenta. Padrão: `60`.
- `enabled` (opcional): Defina como `false` para desativar um servidor sem excluí-lo.
- `required` (opcional): Defina como `true` para que a inicialização falhe se este servidor ativado não conseguir iniciar.
- `enabled_tools` (opcional): Lista de ferramentas permitidas.
- `disabled_tools` (opcional): Lista de ferramentas bloqueadas (aplicada após `enabled_tools`).
- `default_tools_approval_mode` (opcional): Comportamento padrão de aprovação das
  ferramentas deste servidor. Os valores aceitos são `auto`, `prompt`, `writes` e
`approve`. O modo `writes` solicita aprovação para ferramentas que não estejam marcadas como somente leitura.
- `tools.<tool>.approval_mode` (opcional): Substituição do comportamento de aprovação por ferramenta.
- `tools.<tool>.output_token_limit` (opcional): Limite de tokens maior que zero para a saída de uma
  ferramenta, antes da margem padrão de 20% para serialização. Substitui o
  limite padrão do modelo para truncar a saída dessa ferramenta.

A configuração de nível superior `mcp_optional_startup_grace_ms` controla por quanto tempo o Codex
aguarda os servidores MCP opcionais ao montar o catálogo inicial de ferramentas. O valor
padrão é `1000` milissegundos. Defina-a como `0` para usar o tempo limite
`startup_timeout_sec` de cada servidor. Servidores obrigatórios continuam usando seus
tempos limite de inicialização.

#### Registro de clientes OAuth e callbacks

Quando o servidor de autorização exigir um cliente OAuth pré-registrado, informe
o ID desse cliente ao adicionar o servidor MCP:

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

O Codex exibe a URL de callback completa para você registrar no seu provedor:

```text
OAuth callback URL: http://127.0.0.1/callback

O Codex salva o callback junto com o ID do cliente em `config.toml` para os próximos
logins:

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

Clientes pré-registrados recém-adicionados só usam um callback estável quando o
servidor de autorização anuncia
`authorization_response_iss_parameter_supported: true` e fornece nos metadados
um `issuer`. Se o suporte ao emissor não for anunciado, o Codex acrescentará um ID de callback
específico do servidor, como em `http://127.0.0.1/callback/XuuuHAzzHOni`. Clientes existentes
sem um callback salvo continuam usando o redirecionamento específico do seu ID de callback.

Durante o login, a seleção do callback depende da configuração OAuth e
dos metadados do servidor de autorização:

| Configuração OAuth                                                | Suporte ao emissor           | Callback usado                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` sem `client_id`                                 | Com suporte                | O callback configurado é usado no registro do cliente.                                                                                           |
| `callback_url` sem `client_id`                                 | Sem suporte              | O callback configurado é usado no registro do cliente com o ID de callback específico do servidor acrescentado ao final.                                             |
| `client_id` e `callback_url`                                     | Com suporte                | O callback configurado é reutilizado; a resposta de autorização deve conter o `iss` correspondente.                                                     |
| `client_id` e uma `callback_url` que termina com o ID de callback correto | Sem suporte              | O callback configurado é reutilizado sem alterações.                                                                                                       |
| `client_id` e uma `callback_url` sem o ID de callback correto   | Sem suporte              | O callback configurado é ignorado. O Codex usa `mcp_oauth_callback_url` ou, se essa opção não estiver definida, `http://127.0.0.1/callback`, com o ID de callback acrescentado ao final. |
| `client_id` sem uma `callback_url` configurada                    | Com ou sem suporte | O Codex usa o callback global ou padrão com o ID de callback específico do servidor acrescentado ao final.                                                           |

O uso dessa alternativa não altera a URL de callback armazenada. O Codex deriva o
ID de callback da URL do servidor MCP, incluindo o caminho e a string de consulta. As mesmas
regras de seleção se aplicam ao login automático e ao explícito.

Defina `mcp_oauth_callback_url` quando precisar de um caminho de callback personalizado ou de uma URL de entrada de um
Devbox remoto. Clientes pré-registrados recém-adicionados usam essa URL sem alterações
quando o provedor oferece suporte à identificação do emissor. Caso contrário, usam a
URL configurada com o ID de callback específico do servidor acrescentado ao final. Sempre registre
o callback exato exibido por `codex mcp add`.

Para callbacks `http://127.0.0.1` sem porta, o Codex omite a porta de escuta da
URL que exibe e armazena e, depois, insere a porta de escuta ativa durante a
autorização. Essa substituição não se aplica a `localhost`, hosts IPv6,
URLs HTTPS ou callbacks que já incluem uma porta. Os servidores de autorização
devem aceitar portas variáveis de loopback, conforme a
[RFC 8252, seção 7.3](https://www.rfc-editor.org/rfc/rfc8252#section-7.3).

Defina `mcp_oauth_callback_port` para escolher uma porta de escuta global fixa ou defina
`mcp_servers.<server-name>.oauth.callback_port` para substituí-la em um servidor específico.
Uma porta explícita na URL de callback não configura o processo de escuta. Para um
callback direto de loopback, use `http://127.0.0.1` sem porta ou configure a mesma
porta explícita na URL de callback e no processo de escuta. Um callback via proxy pode
usar intencionalmente uma porta na URL externa diferente da porta de escuta
local. Para URLs de callback locais, a escuta ocorre na interface local; para URLs de callback não locais,
a escuta ocorre em `0.0.0.0`.

O Codex valida qualquer `iss` retornado antes de trocar o código de autorização. Um
`iss` divergente sempre causa a rejeição da resposta. Quando o suporte ao emissor é anunciado,
a ausência de `iss` também causa a rejeição. Em nenhuma dessas falhas o código é trocado ou outro
callback é usado como alternativa. Uma URL de callback malformada ou o anúncio de suporte ao emissor
sem um emissor nos metadados também resultam em falha fatal. Consulte
[Autenticar usuários](/plugins/build/auth).

Se o servidor MCP anunciar `scopes_supported`, o Codex dará preferência aos
escopos anunciados pelo servidor durante o login OAuth. Caso contrário, usará os
escopos configurados em `config.toml`.

#### Registro de clientes OAuth

O Codex oferece suporte a [documentos de metadados de ID de cliente OAuth (CIMD)](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
e ao registro dinâmico de clientes (DCR). Por padrão, o Codex escolhe automaticamente
CIMD quando o servidor de autorização anuncia
`client_id_metadata_document_supported: true`, inclui `none` em
`token_endpoint_auth_methods_supported` e o callback usa uma URL de
loopback compatível. Caso contrário, o Codex usa DCR quando disponível. Um ID de cliente OAuth
configurado sempre tem precedência e dispensa o registro do cliente.

Para CIMD, o Codex usa um documento de metadados hospedado no ChatGPT e específico do servidor
MCP:

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

O Codex deriva `<callback_id>` da URL do servidor MCP e o inclui na
URI de redirecionamento de loopback, como
`http://127.0.0.1:<port>/callback/<callback_id>`. O documento de metadados registra
a URI de loopback correspondente sem porta. Os servidores de autorização devem aceitar a
porta selecionada no login e verificar se o host e o caminho correspondem exatamente, conforme exigido pela
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3). Hosts,
caminhos ou parâmetros de consulta personalizados para o callback exigem DCR ou um ID de
cliente OAuth configurado.

O suporte a um documento CIMD estável e compartilhado está em desenvolvimento e estará disponível em breve:

```text
https://chatgpt.com/oauth/codex/client.json

O Codex usará o documento estável com o caminho compartilhado `/callback` quando o
servidor de autorização anunciar
`authorization_response_iss_parameter_supported: true`, fornecer um
`issuer` válido nos metadados e incluir um `iss` correspondente nas respostas de
autorização. Servidores sem respostas vinculadas ao emissor continuarão usando o
documento específico do callback.

Para escolher um método de registro para um único login na CLI, use
`--oauth-client-registration`:

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

O valor padrão é `auto`. As opções de registro se aplicam apenas ao login atual e
não são armazenadas em `config.toml`.

#### Exemplos de config.toml

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### Servidores MCP fornecidos por plug-ins

Os plug-ins instalados podem incluir servidores MCP no manifesto do plug-in. Esses
servidores são iniciados pelo plug-in, portanto a configuração do usuário não define o
comando de transporte deles. A configuração do usuário ainda pode controlar se ficam ativados ou desativados e a política de ferramentas
em `plugins.<plugin>.mcp_servers.<server>`.

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

Servidores MCP HTTP fornecidos por plug-ins também podem declarar configurações OAuth em `.mcp.json`.
Os manifestos de plug-ins usam os nomes de campo em camelCase `clientId`, `callbackUrl` e
`callbackPort`:

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

Servidores MCP fornecidos por plug-ins seguem as mesmas regras de seleção de callback dos demais
servidores MCP. Se um plug-in fornecer um `clientId`, seu provedor não oferecer suporte a
callbacks vinculados ao emissor e `callbackUrl` não contiver o ID de callback
específico do servidor, o Codex ignorará essa URL no login e usará `mcp_oauth_callback_url` ou,
se essa opção não estiver definida, `http://127.0.0.1/callback`, com o ID de callback acrescentado ao final. O
valor configurado de `callbackUrl` permanece inalterado.

A configuração `oauth.callbackPort` de um plug-in substitui a configuração global
`mcp_oauth_callback_port`; se nenhuma das duas estiver definida, o Codex escolherá uma porta efêmera.
A porta incluída em `callbackUrl` não determina a porta de escuta. Para um
callback direto de loopback com porta fixa, configure os dois valores para que sejam iguais:

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

No caso de um ponto de entrada remoto ou outro proxy, a porta da URL de callback e a porta de escuta
local podem ser intencionalmente diferentes quando o proxy encaminha as solicitações ao processo de escuta
configurado.

## Exemplos de servidores MCP úteis

A lista de servidores MCP continua crescendo. Veja alguns dos mais comuns:

- [MCP da documentação da OpenAI](/learn/docs-mcp): Pesquise e leia a documentação da OpenAI para desenvolvedores.
- [Context7](https://github.com/upstash/context7): Conecte-se à documentação atualizada para desenvolvedores.
- Figma [Local](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/) e [Remoto](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/): Acesse seus designs do Figma.
- [Playwright](https://www.npmjs.com/package/@playwright/mcp): Controle e inspecione um navegador usando o Playwright.
- [Ferramentas para desenvolvedores do Chrome](https://github.com/ChromeDevTools/chrome-devtools-mcp/): Controle e inspecione o Chrome.
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex): Acesse os logs do Sentry.
- [GitHub](https://github.com/github/github-mcp-server): Gerencie o GitHub além do que o `git` permite (por exemplo, pull requests e issues).
