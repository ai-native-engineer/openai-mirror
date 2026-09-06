<!-- source: https://learn.chatgpt.com/pt-BR/docs/permissions -->

Versão beta. Os perfis de permissão estão em desenvolvimento ativo e podem mudar.

  Os perfis de permissão não podem ser combinados com as configurações antigas de sandbox. Configure
  `default_permissions` e `[permissions]`, ou `sandbox_mode` /
`sandbox_workspace_write`, mas não as duas opções. Se `sandbox_mode` aparecer em qualquer
  arquivo de configuração carregado, se você passar `--sandbox` ou se o perfil de configuração selecionado definir
`sandbox_mode`, o Codex usará essas configurações antigas de sandbox em vez de
`default_permissions`.

A configuração gerenciada `allowed_permission_profiles` é a exceção: ela faz o Codex usar
perfis de permissão. Remova configurações antigas, como
`sandbox_mode` e `[sandbox_workspace_write]`, antes de implantar uma lista gerenciada de
perfis permitidos. Em uma implantação empresarial com versões mistas, você pode manter o
requisito gerenciado `allowed_sandbox_modes` como uma restrição temporária de
compatibilidade até que todos os clientes executem o Codex 0.138.0 ou posterior.

Os perfis de permissão permitem aplicar limites de privilégio mínimo aos comandos locais
que o Codex executa em seu nome. Um perfil é uma política nomeada que combina regras do sistema de arquivos,
que definem o que os comandos podem ler ou gravar, com regras de rede, que
definem quais destinos os comandos podem acessar.

  A configuração `network.enabled = true` de um perfil permite que os comandos acessem a rede, mas
  não inicia o proxy de rede. Para aplicar as regras de domínio do perfil, também defina
`features.network_proxy = true` em `config.toml` ou use requisitos ativados de
  `[experimental_network]` gerenciados por um administrador. Sem um proxy
  ativo, as regras de domínio do perfil não restringem o acesso direto à rede.

Use perfis para dar ao Codex acesso suficiente para o chat atual sem conceder
acesso amplo à sua máquina ou rede. Por exemplo, um perfil somente leitura pode
permitir que o Codex inspecione um projeto sem editá-lo, enquanto um perfil com permissão de gravação
pode limitar as edições às raízes selecionadas do workspace.

Há suporte a perfis de permissão locais no macOS, no Linux, no WSL e no
Windows nativo. Consulte [Escopo e aplicação](#scope-and-enforcement) para ver
detalhes e ressalvas específicos de cada plataforma.

Para ver as configurações de rede do Codex Cloud, consulte [Acesso à internet](/pt-BR/codex/cloud/internet-access).

## Definir e selecionar um perfil

O Codex inclui três perfis de permissão integrados:

- `:read-only` mantém a execução de comandos locais no modo somente leitura.
- `:workspace` permite gravar nas raízes ativas do workspace e nos diretórios temporários do sistema.
- `:danger-full-access` remove as restrições do sandbox local e deve ser usado
  somente quando esse acesso amplo for intencional.

Crie um perfil nomeado em `[permissions.<name>]` e defina a chave de nível superior
`default_permissions` como o nome desse perfil ou como um dos perfis integrados acima.
Neste exemplo, `project-edit` é um nome de perfil definido pelo usuário, não um valor
integrado.

Os administradores de empresas podem definir perfis e restringir quais deles
os usuários podem selecionar por meio do `requirements.toml` gerenciado. Quando
`allowed_permission_profiles` estiver presente, os perfis omitidos não serão permitidos,
inclusive perfis integrados omitidos e perfis adicionados em versões futuras do Codex. Consulte
[Controlar os perfis de permissão disponíveis](/pt-BR/codex/enterprise/managed-configuration#control-available-permission-profiles)
para ver a configuração gerenciada recomendada.

Os perfis personalizados usam dois conceitos relacionados:

- `[permissions.<name>.workspace_roots]` adiciona diretórios específicos que devem
  ser considerados raízes do workspace desse perfil.
- `[permissions.<name>.filesystem.":workspace_roots"]` define as regras do sistema de arquivos
  que o Codex aplica dentro de cada raiz efetiva do workspace: as raízes do workspace do ambiente de execução
  da sessão atual, além das raízes definidas pelo perfil acima.

Os perfis também usam o modelo normal de camadas de configuração. As camadas de maior precedência podem
adicionar ou substituir entradas com o mesmo nome de perfil sem redefinir todo o
perfil.

Por exemplo, uma configuração no nível da organização e outra no nível do usuário podem estender
o mesmo perfil de forma independente:

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

Quando `server` está ativo, ambas as raízes do workspace fazem parte do perfil
efetivo.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

Este perfil:

- Lê o conjunto mínimo de caminhos do ambiente de execução de que as ferramentas comuns de desenvolvimento precisam.
- Aplica as mesmas regras às raízes do workspace da sessão atual e às raízes
definidas pelo perfil.
- Mantém as configurações associadas à IDE, como `.devcontainer/`, no modo somente leitura em cada
  raiz.
- Nega o acesso aos arquivos de ambiente correspondentes por meio de uma regra glob.
- Permite acesso à rede somente por meio da política de domínios configurada.

Em um perfil ativo, as regras de negação mais específicas continuam em vigor mesmo quando um caminho mais abrangente
tem permissão de leitura ou gravação. Por exemplo, um perfil pode permitir gravação nas raízes do workspace
e ainda definir um caminho correspondente a `.env` como `deny`.

## Estender um perfil

Use `extends` quando um perfil for quase igual a um perfil integrado ou a outro perfil nomeado.
Prefira estender um perfil integrado em vez de começar do zero para manter
as proteções básicas. Por exemplo, estender `:workspace` mantém
o diretório `.codex` da raiz do workspace no modo somente leitura, a menos que você substitua essa regra
explicitamente. Defina o perfil pai uma única vez e adicione ou substitua apenas as regras que
forem diferentes.

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Este perfil começa com `:workspace`, mantém negado o acesso aos arquivos que correspondem a `.env` e
permite solicitações para `api.openai.com`. Um perfil pode estender `:read-only`,
`:workspace` ou outro perfil nomeado. Ele não pode estender
`:danger-full-access`; o Codex também rejeita perfis pai desconhecidos e ciclos de
herança.

## Especificação da configuração

| Entrada                                                             | Tipo / valores              | Padrão                 | Detalhes                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | Nome do perfil (string)        | Nenhum                    | Especifica o perfil de permissão que o Codex aplica por padrão. Ele deve corresponder a um perfil definido em `[permissions]` ou a um perfil integrado, como `:workspace`. Defina-o explicitamente para garantir um comportamento previsível; os requisitos gerenciados só podem omiti-lo quando `:workspace` e `:read-only` forem explicitamente permitidos. O Codex usa as configurações antigas de sandbox, a menos que a opção gerenciada `allowed_permission_profiles` determine o uso de perfis de permissão nesta configuração. |
| `[permissions.<name>]`                                            | Tabela                      | Nenhum                    | Define um perfil nomeado. `default_permissions` seleciona um perfil como padrão; outras configurações de perfis de permissão também usam o nome do perfil.                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | String                     | Nenhum                    | Fornece uma descrição de fácil leitura para o perfil. Um perfil não herda a descrição do perfil pai por meio de `extends`.                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | Nome do perfil (string)        | Nenhum                    | Baseia este perfil em outro perfil nomeado ou no perfil integrado `:read-only` ou `:workspace`. O Codex rejeita `:danger-full-access`, perfis pai desconhecidos e ciclos de herança.                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | Tabela                      | Nenhum                    | Adiciona raízes do workspace definidas pelo perfil que recebem as regras `:workspace_roots` do sistema de arquivos junto com as raízes do workspace do ambiente de execução da sessão atual.                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | Booleano                    | `false`                 | Adiciona o caminho ao conjunto de raízes do workspace do perfil quando o valor é `true`. As entradas com valor `false` permanecem inativas.                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | Tabela                      | Nenhum                    | Mapeia caminhos do sistema de arquivos para valores de acesso ou mapas de subcaminhos com escopo delimitado. Tabelas do sistema de arquivos ausentes ou vazias mantêm o acesso ao sistema de arquivos restrito e emitem um aviso na inicialização.                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | Número                     | Nenhum                    | Limita a expansão de globs de negação de leitura no Linux, WSL e Windows nativo quando o Codex cria um snapshot das correspondências antes da inicialização do sandbox. Valores maiores podem aumentar o trabalho de varredura na inicialização. Use um valor de pelo menos `1` quando um padrão `**` sem limite exigir uma pré-expansão delimitada.                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`, `write` ou `deny` | Nenhum                    | Concede acesso direto a um caminho compatível. `deny` nega o acesso e prevalece sobre entradas `write` ou `read` igualmente específicas. O Codex rejeita regras diretas de gravação que o ambiente de execução ativo não consegue aplicar.                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`, `write` ou `deny` | Nenhum                    | Concede acesso a um caminho descendente de `<path>`. Use `.` para o caminho base. Os demais subcaminhos devem ser descendentes relativos e não podem conter componentes `.` ou `..`.                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | Tabela                      | Nenhum                    | Configura o acesso dos comandos à rede e a política aplicada por um proxy de rede ativo. Ative `features.network_proxy`, a menos que requisitos de rede gerenciados por um administrador iniciem o proxy.                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | Booleano                    | `false`                 | Ativa o acesso dos comandos do perfil à rede. Não inicia o proxy de rede; sem um proxy ativo, os comandos podem se conectar diretamente, sem restrições de domínio.                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | Tabela                      | Nenhum                    | Mapeia padrões de host para `allow` ou `deny`. As regras só se aplicam quando o proxy de rede está ativo. O proxy ativo bloqueia solicitações a domínios se não houver entradas `allow`, e as entradas de negação têm precedência sobre as de permissão.                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` ou `deny`          | Nenhum                    | Oferece suporte a hosts exatos, `*.example.com` para subdomínios, `**.example.com` para o domínio raiz e seus subdomínios e `*` como curinga global exclusivo para permissões. Os padrões de host são normalizados mediante a remoção de espaços nas extremidades, a conversão para minúsculas e a remoção do ponto final, de indicações simples de porta ou de colchetes.                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | Tabela                      | Nenhum                    | Mapeia substituições na lista de permissões de soquetes Unix. Use apenas para integrações locais, como o Docker.                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` ou `deny`          | Nenhum                    | Adiciona um caminho absoluto de soquete Unix à lista de permissões efetiva com `allow` ou o rejeita com `deny`. As entradas negadas são omitidas da lista de permissões efetiva.                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | String de URL                 | `http://127.0.0.1:3128` | Listener de proxy HTTP usado para `HTTP_PROXY`, `HTTPS_PROXY`, variáveis de proxy de websocket e variáveis de ambiente de proxy das ferramentas relacionadas.                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | Booleano                    | `true`                  | Ativa o listener SOCKS5 usado para `ALL_PROXY` e para variáveis de proxy FTP.                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | String de URL                 | `http://127.0.0.1:8081` | Endereço do listener SOCKS5.                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | Booleano                    | `true`                  | Ativa o suporte a UDP do SOCKS5 quando o listener SOCKS5 está ativado.                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | Booleano                    | `true`                  | Permite que o proxy de rede do ambiente isolado respeite as configurações upstream de `HTTP(S)_PROXY` e `ALL_PROXY` para solicitações de saída.                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | Booleano                    | `false`                 | Desativa a proteção contra acesso a redes locais ou privadas quando definido como `true`. Quando definido como `false`, literais locais exatos, como `localhost` ou `127.0.0.1`, devem estar explicitamente na lista de permissões, e nomes de host que apontam para endereços IP locais ou privados permanecem bloqueados.                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | Booleano                    | `false`                 | Permite vincular listeners de proxy a endereços que não sejam de loopback. Para o desenvolvimento local comum, deixe essa opção sem definir.                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | Booleano                    | `false`                 | Ignora a lista de permissões de soquetes Unix quando há suporte ao uso de proxy para soquetes Unix. Isso cria uma forma ampla de contornar as restrições locais.                                                                                                                                                                                                                                                                                                               |

## Permissões do sistema de arquivos

As entradas do sistema de arquivos usam `read`, `write` ou `deny`:

| Acesso  | Significado                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | Permite que os comandos leiam arquivos e listem diretórios abaixo do caminho. Os comandos não podem criar, modificar, renomear nem excluir arquivos nesse local. |
| `write` | Permite que os comandos leiam e modifiquem arquivos abaixo do caminho, inclusive criando, renomeando e excluindo arquivos quando o sistema operacional permitir.  |
| `deny`  | Nega a leitura e a gravação abaixo do caminho. Use essa opção para delimitar um subcaminho com acesso negado dentro de uma permissão mais ampla de `read` ou `write`.         |

Entradas mais específicas têm precedência sobre entradas mais amplas. Quando duas entradas se aplicam ao
mesmo caminho, `deny` tem precedência sobre `write`, e `write` tem precedência
sobre `read`.

Essa precedência permite que um perfil defina primeiro uma área ampla de trabalho e depois delimite
os arquivos ou diretórios que devem permanecer inacessíveis para leitura:

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

Neste exemplo, a raiz do workspace continua gravável, `.devcontainer/` permanece
acessível apenas para leitura, e os arquivos de ambiente correspondentes ficam
indisponíveis para comandos executados em ambiente isolado.

Um caminho mais específico também pode reabrir o acesso a uma subárvore mais restrita dentro de uma regra de negação mais ampla:

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

Formatos de caminho aceitos:

| Caminho               | Significado                                                                                     | Subcaminhos com escopo delimitado |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | A raiz do sistema de arquivos                                                                         | Somente `.`        |
| `:minimal`         | Caminhos da plataforma e do ambiente de execução necessários para ferramentas comuns                                           | Somente `.`        |
| `:workspace_roots` | As raízes de workspace da sessão atual e quaisquer raízes de workspace definidas no perfil que estejam ativadas      | Sim             |
| `:tmpdir`          | O local indicado por `$TMPDIR`, quando disponível                                               | Somente `.`        |
| `:slash_tmp`       | A pasta `/tmp`, se existir                                                             | Somente `.`        |
| `/absolute/path`   | Um caminho absoluto da plataforma, como `/path` no macOS/Linux/WSL ou `C:\path` no Windows nativo | Sim             |
| `~/path`           | Um caminho dentro do diretório pessoal do usuário atual                                              | Sim             |

No Windows nativo, caminhos relativos ao diretório pessoal também podem usar barras invertidas, como
`~\work`.

Use `:root` somente quando houver a intenção de conceder amplo acesso de leitura ao perfil:

```toml
[permissions.audit.filesystem]
":root" = "read"

Use entradas aninhadas em `:workspace_roots` para delimitar o acesso a subcaminhos
relativos à raiz do workspace:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

Os subcaminhos aninhados devem permanecer dentro da raiz do workspace. A navegação para o diretório pai, como
`../other-repo`, é rejeitada.

### Negar leituras com caminhos exatos ou padrões glob

Use `deny` para arquivos ou subárvores que o Codex não deve ler, mesmo que uma regra
mais ampla do perfil conceda acesso a caminhos próximos. Caminhos exatos funcionam bem para locais estáveis,
como `~/.ssh`. Padrões glob são mais adequados quando o perfil precisa abranger uma
família de arquivos confidenciais cujos locais exatos variam entre repositórios.

Quando um padrão glob está em `:workspace_roots`, o Codex o interpreta em relação a cada
raiz efetiva do workspace. Por exemplo:

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

Essa regra nega a leitura dos arquivos `.env` correspondentes encontrados sob cada raiz do workspace do ambiente de execução ou
definida pelo perfil. Use-a quando quiser manter as operações normais de gravação
no workspace e impedir a leitura de arquivos de ambiente, segredos gerados ou arquivos semelhantes
que contenham credenciais.

Padrões glob com `deny` são compatíveis com regras de negação de leitura. Padrões glob com `read` ou `write`
são menos portáveis nos ambientes isolados do Linux, do WSL e do Windows nativo; por isso, prefira
caminhos exatos ou regras para subárvores, como `"docs/**" = "read"`, sempre que possível.

No Linux, no WSL e no Windows nativo, um padrão `**` sem limite para negação de leitura pode exigir
uma pré-expansão limitada antes da inicialização do Sandbox. Defina `glob_scan_max_depth` quando
usar um padrão sem limite, como `"**/*.env" = "deny"`:

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` deve ser, no mínimo, `1`. Valores mais altos fazem uma verificação mais profunda antes da
inicialização do Sandbox, o que pode aumentar o processamento durante a inicialização no Linux, no WSL e no Windows nativo.
Se preferir não usar a expansão limitada, enumere profundidades explícitas, como
`*.env`, `*/*.env` e `*/*/*.env`.

Adicione raízes de workspace reutilizáveis ao perfil quando as mesmas regras precisarem se aplicar a
outras raízes além da raiz da sessão atual:

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

Quando este perfil está ativo, o Codex aplica as regras de `:workspace_roots` às
raízes de workspace em tempo de execução da sessão atual e a cada raiz
de workspace habilitada definida pelo perfil.

No Windows nativo, caminhos com letra de unidade, como `D:\work`, e caminhos UNC, como
`\\server\share`, são aceitos como caminhos absolutos.

## Permissões de rede

O acesso à rede e a filtragem de rede são configurações separadas. Defina
`permissions.<name>.network.enabled = true` para permitir que os comandos acessem a rede
e habilite `features.network_proxy` para aplicar as regras de domínio do perfil:

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

O comportamento resultante depende das duas configurações:

- Rede desativada: os comandos não podem acessar a rede, independentemente do recurso
de proxy.
- Rede ativada, proxy desativado: os comandos têm acesso direto e irrestrito à
rede. As regras de domínio do perfil de permissão não são aplicadas.
- Rede ativada, proxy ativado: os comandos usam o proxy, que aplica as regras de
domínio do perfil. Se o proxy ativo não tiver domínios permitidos, ele bloqueia
os destinos externos.

Adicionar `[permissions.<name>.network.domains]` ou definir
`permissions.<name>.network.enabled = true` não habilita
`features.network_proxy`. Como alternativa, os administradores podem habilitar o
proxy com `[experimental_network]` em `requirements.toml`. Consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration#configure-network-access-requirements).

Quando está ativo, o proxy de rede do Sandbox vincula-se a listeners locais por padrão:

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

Mantenha essas configurações de listener nos valores padrão, a menos que esteja fazendo uma integração com
um runtime específico. As chaves de rede `dangerously_*` são mecanismos de escape para
ambientes especializados e não devem ser usadas no desenvolvimento local comum.

### Redes locais e privadas

Quando o proxy de rede está ativo, o Codex aplica, por padrão, uma proteção para redes locais
e privadas contra DNS rebinding e o acesso acidental a serviços
locais. Para permitir intencionalmente um destino local literal, adicione à lista de permissões
o host exato ou o endereço IP literal:

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

Defina `allow_local_binding = true` somente quando o perfil precisar acessar nomes de host permitidos
que sejam resolvidos para endereços locais ou privados:

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Sockets Unix

O uso de proxy para sockets Unix é um mecanismo de escape local para ferramentas como o Docker. Use-o
com moderação:

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

Use `deny` para rejeitar um caminho de socket, inclusive uma entrada de permissão herdada. Os caminhos de
socket negados são omitidos da lista de permissões efetiva.

Quando os sockets Unix estiverem habilitados, mantenha os listeners do proxy vinculados a endereços de loopback.

## Migrar das configurações antigas do Sandbox

Os perfis de permissão substituem a antiga combinação de `sandbox_mode` e
`sandbox_workspace_write` quando você precisa de um único perfil reutilizável para definir o comportamento
do sistema de arquivos e da rede. Em uma sessão, use um sistema ou outro, nunca
os dois.

Pontos de partida sugeridos:

- Para um fluxo de trabalho somente leitura, use o perfil integrado `:read-only` ou defina um
  perfil personalizado com acesso de leitura apenas onde necessário.
- Para editar o workspace, use o perfil integrado `:workspace` ou defina um
  perfil personalizado que grave por meio de `:workspace_roots` e adicione apenas os caminhos
  temporários ou de cache adicionais necessários ao fluxo de trabalho.
- Para execução local irrestrita, use `:danger-full-access` somente se você
  pretender usar o modelo de acesso local mais amplo.

Os perfis definem a política local padrão de uma sessão. Requisitos gerenciados pela organização
ainda podem impor restrições que a configuração do usuário não deve
flexibilizar. Consulte [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration)
para conhecer as restrições de sistema de arquivos e rede impostas pelos administradores.

## Escopo e aplicação

Os perfis de permissão definem os limites para a execução local de comandos em ambiente
isolado. Use-os em conjunto com políticas de aprovação e com os controles separados
para pesquisa na Web, conectores, servidores MCP, o navegador integrado, o Uso do computador
e o Codex Cloud.

### O que os perfis controlam

- **Execução local de comandos:** os perfis de permissão controlam os comandos em ambiente isolado
  executados na sua máquina. Conectores, servidores MCP, interfaces de navegador ou de
  Uso do computador, configurações dos ambientes do Codex Cloud e elevações
  aprovadas usam seus próprios controles.
- **Gravações no sistema de arquivos:** um perfil com permissão de gravação pode criar alterações persistentes.
  Trate como sensíveis as gravações em scripts, etapas de build, hooks de gerenciadores de pacotes, arquivos de inicialização do
  shell e diretórios compartilhados, porque outras ferramentas ou usuários podem
  executar esses arquivos posteriormente, fora do contexto original do Sandbox.
- **Destinos de saída:** as regras de domínio de rede restringem o destino do tráfego de comandos em ambiente
  isolado somente enquanto o proxy de rede está ativo. Elas não
  determinam se um destino permitido é confiável, e as regras de permissão com caracteres curinga
  continuam amplas.
- **Serviços locais:** um proxy de rede ativo bloqueia, por padrão, destinos em redes locais e privadas.
  Adicionar `localhost`, endereços IP privados ou sockets Unix à lista de permissões, ou definir
`allow_local_binding = true`, libera explicitamente o acesso a serviços locais.

### O que o proxy de rede não controla

O proxy de rede filtra apenas o tráfego de comandos locais executados no
Sandbox. Ele não aplica a lista de domínios permitidos do perfil a:

- **Pesquisa na Web:** a ferramenta de pesquisa hospedada usa suas próprias configurações de acesso. Use
`web_search` e, em clientes gerenciados, `allowed_web_search_modes` para
  controlá-la. `tools.web_search.allowed_domains` filtra os resultados da pesquisa, não o acesso dos comandos
  à rede.
- **Apps e conectores:** as ferramentas baseadas em conectores usam suas próprias conexões do lado do serviço,
  permissões do workspace e configurações de aplicativos ou ferramentas.
- **Servidores MCP:** servidores MCP locais e remotos usam seu próprio processo ou
  transporte. Controle-os com a configuração `mcp_servers` e com listas gerenciadas
  de servidores permitidos.
- **Navegador e Uso do computador:** a navegação no navegador e as ações de uso do computador
  usam seus próprios controles de recursos e aprovação.
- **Tráfego do serviço Codex:** as solicitações de modelo, autenticação e outros serviços do cliente
  usam as configurações separadas de HTTP e de proxy do sistema do cliente.
- **Codex Cloud:** essas tarefas usam as próprias
[configurações de acesso à internet](/pt-BR/codex/cloud/internet-access) de seus ambientes.

Para limitar essas superfícies, configure cada recurso diretamente. Uma lista de permissões de rede para
comandos não é uma política global de rede aplicável a todas as ações que o Codex pode executar.

### Como funciona a aplicação das regras

- No macOS, o Codex usa perfis de Sandbox do Seatbelt. Se o Sandbox da plataforma não puder
aplicar a política selecionada, o Codex se recusa a executar o comando, em vez
de executá-lo silenciosamente sem isolamento.
- No Linux e no WSL, o Codex usa [bubblewrap](https://github.com/containers/bubblewrap)
  e [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html),
  com o Landlock disponível para alternativas de compatibilidade. O mecanismo de aplicação mais
  rigoroso depende dos namespaces de usuário e do suporte do kernel; hosts de contêiner
  com restrições podem exigir alternativas de compatibilidade, e políticas de acesso segmentado sem suporte
  são recusadas.
- No Windows nativo, o [ambiente isolado `elevated`](/pt-BR/codex/windows/windows-sandbox#windows-sandbox)
  é o que oferece mais proteção, pois pode usar usuários dedicados do Sandbox com privilégios reduzidos,
  limites de permissão do sistema de arquivos e regras de firewall. O ambiente isolado `unelevated`
  é uma alternativa com isolamento de rede mais fraco e não consegue aplicar
  todas as exceções segmentadas de leitura e gravação; por isso, políticas sem suporte são recusadas. Use o WSL
  quando precisar do modelo de Sandbox do Linux.

### Orientações operacionais

Escolha o perfil mais restrito que ainda permita concluir a tarefa, especialmente quando
conceder permissões de gravação ou acesso de saída à rede. Mantenha a política de aprovação, o tratamento de
segredos e as regras de permissão alinhados a esse nível de acesso.

## Perfis comuns

### Somente leitura com lista de permissões de rede

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### Acesso a arquivos limitado ao workspace

Este é um exemplo de perfil de permissão que permite ao Codex gravar nas pastas do seu workspace, mas nega a leitura do restante do sistema de arquivos (com exceções limitadas, conforme determinado por `:minimal`).

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### Gravação no workspace sem rede

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### Gravação no workspace com acesso à Web pública

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

Use a regra global de permissão `"*"` somente quando pretender permitir o acesso à rede
pública. Regras de negação podem restringir uma lista de permissões ampla.
