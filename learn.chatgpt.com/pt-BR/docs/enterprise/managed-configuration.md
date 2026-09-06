<!-- source: https://learn.chatgpt.com/pt-BR/docs/enterprise/managed-configuration -->

A configuração gerenciada controla o comportamento do ambiente de execução local para as capacidades abrangidas no aplicativo do ChatGPT para desktop, na Codex CLI e na extensão para IDE, conforme o suporte de cada cliente. Os requisitos compatíveis podem variar conforme o cliente e a versão. A configuração gerenciada não concede acesso ao workspace do ChatGPT, não atribui licenças nem substitui o controle de acesso baseado em funções (RBAC) do workspace. Consulte [Funções e permissões do workspace](/pt-BR/codex/enterprise/roles-and-workspace-permissions) para saber sobre o acesso aos recursos do workspace e esta página para saber sobre a política do ambiente de execução local.

Os administradores empresariais podem controlar o comportamento dos clientes locais compatíveis de duas maneiras:

- **Requisitos**: restrições impostas pelos administradores que os usuários não podem substituir.
- **Valores padrão gerenciados**: valores iniciais aplicados quando um cliente compatível é iniciado. Os usuários ainda podem alterar as configurações durante uma execução; o cliente reaplica os valores padrão gerenciados na próxima inicialização.

## Requisitos impostos pelos administradores (requirements.toml)

Os requisitos restringem configurações sensíveis à segurança (política de aprovação, revisor de aprovações, política de revisão automática, modo de sandbox, perfis de permissão, modo de pesquisa na Web, ganchos gerenciados, quais servidores MCP os usuários podem habilitar e quais fontes de marketplace de plug-ins configuradas pelos usuários eles podem adicionar, usar para instalar plug-ins ou atualizar). Ao resolver a configuração (por exemplo, com base em `config.toml`, [arquivos de perfil](/pt-BR/codex/config-file/config-advanced#profiles) ou substituições de configuração da CLI), se um valor entrar em conflito com uma regra imposta, o cliente local usará um valor compatível e notificará o usuário. Se você configurar uma lista de permissões em `mcp_servers`, o cliente só habilitará um servidor MCP quando seu nome e sua identidade corresponderem a uma entrada aprovada; caso contrário, o cliente o desabilitará.

Os requisitos também podem restringir [sinalizadores de recursos](/pt-BR/codex/config-file/config-basic/#feature-flags) por meio da tabela `[features]` em `requirements.toml`. Os recursos nem sempre são sensíveis à segurança, mas as empresas podem fixar valores, se desejarem. As chaves omitidas permanecem sem restrições.

No Codex 0.138.0 ou posterior, prefira [perfis de permissão](/pt-BR/codex/permissions)
com `allowed_permission_profiles` e o valor gerenciado de `default_permissions`. Use
`allowed_sandbox_modes` somente em implantações legadas que ainda configurem
`sandbox_mode`.

Para conferir a lista exata de chaves, consulte a [seção `requirements.toml` na Referência de configuração](/pt-BR/codex/config-file/config-reference#requirementstoml).

### Locais e precedência

Cada cliente local compatível combina os requisitos da menor para a maior precedência:

1. O `requirements.toml` do sistema (`/etc/codex/requirements.toml` em sistemas Unix,
   incluindo Linux e macOS, ou `%ProgramData%\OpenAI\Codex\requirements.toml`
   no Windows).
2. Requisitos gerenciados pela empresa fornecidos no pacote de configuração da nuvem.
3. Campos legados de `managed_config.toml` que o cliente local reinterpreta como requisitos.
4. Preferências gerenciadas do macOS (MDM) fornecidas por meio de
`com.openai.codex:requirements_toml_base64`.

As camadas de maior precedência substituem os valores escalares e de lista comuns das
camadas de menor precedência. As tabelas são mescladas por chave, enquanto requisitos como regras, ganchos e
restrições do sistema de arquivos têm um comportamento de composição específico de cada campo. Consulte a
[referência de `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml)
para verificar o esquema atual, em vez de presumir que todos os campos sejam mesclados da mesma
forma.

Para manter a compatibilidade retroativa, os clientes locais compatíveis reinterpretam os campos legados
`approval_policy`, `approvals_reviewer` e `sandbox_mode` como
requisitos. Essa conversão adiciona opções de compatibilidade quando necessário; use
`requirements.toml` para listas de permissões explícitas.

### Requisitos gerenciados na nuvem

Quando um usuário faz login com o ChatGPT em um plano compatível, os clientes locais compatíveis
podem receber requisitos impostos pelos administradores e associados ao workspace. Esse é
um canal para distribuir políticas compatíveis com `requirements.toml`. Ele não concede
acesso ao workspace nem substitui o RBAC do workspace.

Abra [Configuração gerenciada](https://chatgpt.com/codex/settings/managed-configs)
para criar e atribuir requisitos gerenciados na nuvem. Por exemplo, esta política limita
as opções de aprovação e de sandbox e solicita confirmação antes que um ponto de entrada compatível do shell
seja executado:

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

Confirme se todas as versões dos clientes gerenciados são compatíveis com as chaves selecionadas e
teste a política com um grupo pequeno antes de atribuí-la à organização inteira. Use
a referência de configuração para consultar o esquema atual e a interface de administração
para verificar o comportamento atual das atribuições.

O serviço seleciona as camadas de requisitos gerenciados pela empresa aplicáveis à
identidade autenticada. O cliente local avalia essas camadas juntamente com as demais
fontes de requisitos descritas em [Locais e precedência](#locations-and-precedence).
Use a interface de administração atual para criar e
atribuir requisitos no workspace. Não se baseie em uma cópia do algoritmo de correspondência de grupos; o serviço de administração
controla esse comportamento e pode alterá-lo independentemente do formato dos
requisitos locais.

Para ver as chaves compatíveis e exemplos, consulte
[Exemplo de requirements.toml](#example-requirementstoml) e a
[referência de `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml).

#### Como os clientes locais aplicam requisitos gerenciados na nuvem

Quando um usuário inicia um cliente local compatível e faz login com o ChatGPT em um
plano compatível, o cliente primeiro verifica se há uma entrada de cache válida
que corresponda à identidade. Se nenhuma entrada válida estiver disponível, o cliente busca o pacote aplicável,
faz novas tentativas quando necessário e grava uma entrada de cache assinada se a busca for bem-sucedida. Se a solicitação falhar ou
atingir o tempo limite e não houver cache válido disponível, o carregamento do pacote de configuração da nuvem retorna
um erro, em vez de iniciar silenciosamente sem a camada de requisitos
gerenciados na nuvem.

Após a resolução do cache, o cliente combina os requisitos da nuvem com as
outras camadas de requisitos descritas acima. Uma atualização em segundo plano pode atualizar o
cache para uma inicialização posterior; ela não substitui os requisitos já carregados
no processo atual.

### Confirmar a experiência dos administradores e funcionários

Designe uma pessoa responsável por cada política gerenciada, registre quais usuários ou grupos devem
recebê-la e documente a justificativa de negócio para qualquer restrição de sistema de arquivos, rede,
aprovação ou perfil de permissão.

Antes de ampliar a implantação, teste um fluxo de trabalho aprovado e um fluxo de trabalho intencionalmente
não permitido com um usuário representativo. Verifique as configurações efetivas
no cliente compatível, em vez de presumir que uma função ou um grupo no workspace, por si só,
garante a aplicação da restrição local.

### Exemplo de requirements.toml

Este exemplo bloqueia `--ask-for-approval never` e `--sandbox danger-full-access` (incluindo `--yolo`):

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### Desativar as Capturas do app

Para desativar as Capturas do app para usuários gerenciados, defina o requisito `allow_appshots` no nível superior:

```toml
allow_appshots = false

Onde as Capturas do app estão disponíveis, `allow_appshots = false` as desativa. Se você
omitir a chave, os requisitos não restringirão as Capturas do app, e as verificações normais de
disponibilidade do produto serão aplicadas. Os clientes do App Server que leem os requisitos efetivos
por meio de `configRequirements/read` recebem a mesma restrição no campo
`allowAppshots`; um valor ausente ou `null` em `allowAppshots` não desativa
as Capturas do app.

### Desativar o controle remoto do dispositivo

Para desativar o [controle remoto do dispositivo](/pt-BR/codex/remote-connections#pick-up-work-from-another-device)
para usuários gerenciados, defina o requisito `allow_remote_control` no nível superior:

```toml
allow_remote_control = false

Onde houver suporte ao controle remoto do dispositivo, `allow_remote_control = false`
o desativa. Se você omitir a chave, os requisitos não restringirão o controle remoto do
dispositivo, e as verificações normais de disponibilidade do produto serão aplicadas. Esse requisito não
desativa conexões remotas via SSH.

### Controlar os perfis de permissão disponíveis

Use `allowed_permission_profiles` para controlar quais
[perfis de permissão](/pt-BR/codex/permissions) integrados e personalizados os usuários podem selecionar. Essa é a
opção equivalente a `allowed_sandbox_modes` para perfis de permissão; use a lista de permissões que
corresponda à forma como os usuários selecionam permissões.

As listas de perfis de permissão permitidos exigem o Codex 0.138.0 ou posterior. O Codex 0.137.0 e as
versões anteriores ignoram `allowed_permission_profiles` e o valor gerenciado de
`default_permissions`.

Use os exemplos de perfis de permissão abaixo somente depois que todos os clientes gerenciados estiverem executando uma
versão compatível. Não implante perfis personalizados gerenciados até que a atualização de todos os clientes
esteja concluída.

Quando está presente, a tabela é a lista completa de perfis permitidos. Ela permite
perfis definidos como `true` e bloqueia perfis omitidos ou definidos como `false`, inclusive
perfis integrados adicionados em versões futuras do Codex.

#### Permitir os perfis padrão

Esta política permite acesso somente leitura e acesso ao workspace, mas não acesso completo:

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### Adicionar um valor padrão gerenciado com privilégio mínimo

Os administradores podem definir um perfil personalizado na mesma fonte de requisitos. Use
nomes de perfil específicos da organização que não entrem em conflito com nomes presentes na
configuração carregada dos usuários. Os nomes personalizados não podem começar com `:` nem usar o nome reservado
`filesystem`.

Não implante perfis personalizados gerenciados em clientes que executam o Codex 0.137.0 ou
uma versão anterior. Esses clientes reconhecem a tabela de perfis, mas não o valor padrão gerenciado
que seleciona o perfil.

Por exemplo:

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### Permitir somente perfis definidos pela empresa

Omita todos os perfis integrados quando os usuários só puderem selecionar perfis definidos pelos administradores:

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

O perfil personalizado pode estender `:workspace`, mesmo que os usuários não possam selecionar diretamente o
perfil integrado `:workspace`.

#### Desativar um perfil permitido por outra fonte

As listas de permissões são combinadas pelo nome do perfil. Como os requisitos da nuvem têm
precedência maior do que os requisitos do sistema, os requisitos da nuvem podem usar `false`
para desativar um perfil permitido pelo arquivo do sistema.

Requisitos da nuvem:

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

Requisitos do sistema:

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

Defina `default_permissions` explicitamente como um perfil permitido. Se ele for omitido,
o ambiente de execução local usará `:workspace` como padrão somente quando tanto `:workspace` quanto
`:read-only` estiverem explicitamente permitidos. Quando `allowed_permission_profiles` estiver
ausente, os requisitos gerenciados não restringirão os nomes de perfil que os usuários podem
selecionar. Cada entrada deve indicar um perfil integrado ou um perfil personalizado definido em
uma configuração ou fonte de requisitos carregada. Defina perfis personalizados nos
requisitos gerenciados para controlar o comportamento deles de forma centralizada.

### Substituir os requisitos de sandbox por host

Use `[[remote_sandbox_config]]` quando uma única política gerenciada precisar aplicar requisitos de
sandbox diferentes em hosts diferentes. Por exemplo, você pode manter um padrão mais restritivo
para laptops e permitir gravações no workspace em máquinas de desenvolvimento ou executores de CI que correspondam aos padrões.
Atualmente, as entradas específicas de host substituem somente `allowed_sandbox_modes`:

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

O ambiente de execução local compara cada entrada de `hostname_patterns` com o
nome do host resolvido da melhor forma possível. Ele prioriza o nome de domínio totalmente qualificado quando
disponível e, como alternativa, usa o nome do host local. A correspondência não diferencia maiúsculas de minúsculas;
`*` corresponde a qualquer sequência de caracteres, e `?` corresponde a um caractere.

A primeira entrada de `[[remote_sandbox_config]]` que corresponder prevalece dentro da mesma
fonte de requisitos. Se nenhuma entrada corresponder, o ambiente de execução local manterá o valor de nível superior de
`allowed_sandbox_modes`. A correspondência do nome do host serve apenas para selecionar a política; não
a considere uma comprovação autenticada da identidade do dispositivo.

Você também pode restringir o modo de pesquisa na Web:

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` permite somente `"disabled"`.
Por exemplo, `allowed_web_search_modes = ["cached"]` impede a pesquisa na Web em tempo real mesmo em sessões `danger-full-access`.

### Configurar requisitos de acesso à rede

  `[experimental_network]` é experimental e pode mudar. Não habilite esses
  requisitos de forma ampla em uma implantação empresarial sem validá-los
  nas versões dos clientes locais e nos sistemas operacionais usados pelos usuários. O suporte ao Windows
  ainda é limitado; evite aplicar essa política a usuários do Windows, a menos que
  você a tenha testado no seu ambiente.

Use `[experimental_network]` em `requirements.toml` quando os administradores precisarem
definir centralmente os requisitos de acesso à rede. Esses requisitos são independentes
da opção `features.network_proxy` do usuário: eles podem configurar a rede do sandbox
sem esse sinalizador de recurso, mas não concedem acesso à rede aos comandos
quando o sandbox ativo mantém a rede desativada. Defina
`experimental_network.enabled = true` para ativar o proxy gerenciado; as regras de domínio,
por si só, não ativam o proxy.

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

Use `experimental_network.managed_allowed_domains_only = true` somente quando você
também definir entradas `"allow"` sob controle dos administradores em
`[experimental_network.domains]` e quiser que essas regras sejam exclusivas. Se o valor for
`true` sem regras de permissão gerenciadas, as regras de permissão de domínios adicionadas pelos usuários deixam de
ter efeito. Não combine o mapa canônico `domains` com as listas legadas
`allowed_domains` ou `denied_domains`.

`*.example.com` corresponde apenas a subdomínios. `**.example.com` corresponde ao domínio raiz
e aos seus subdomínios. Uma regra de negação correspondente prevalece sobre uma regra de permissão.

A sintaxe dos domínios, as regras para destinos locais ou privados, a prioridade da negação sobre a permissão
e as limitações de DNS rebinding são as mesmas do comportamento de rede do sandbox
descrito em [Aprovações do agente e segurança](/pt-BR/codex/agent-approvals-security#network-isolation).

O proxy encaminha o tráfego dos comandos locais executados dentro do sandbox. As ferramentas de navegador
também verificam as negações de rede gerenciadas e as listas exclusivas de permissões antes de acessar
uma origem; essa é uma verificação de política separada, que não encaminha o tráfego do navegador pelo
proxy de comandos. O proxy não filtra a pesquisa na Web, aplicativos e conectores, servidores MCP,
tráfego de aplicativos nativos, solicitações ao serviço Codex nem o tráfego do Codex Cloud.
Use os controles específicos de cada recurso:

- Use `allowed_web_search_modes` para restringir a pesquisa na Web.
- Use `features.apps = false` para desativar integrações com aplicativos e conectores e
`features.plugins = false` para desativar plug-ins quando houver suporte.
- Use a lista gerenciada de servidores aprovados em `mcp_servers` para restringir os servidores MCP.
- Use requisitos de recursos como `browser_use`, `in_app_browser` e
`computer_use` para restringir as capacidades do navegador e de Uso do computador.
- Configure o acesso à rede do Codex Cloud nas configurações do respectivo ambiente de nuvem.

Uma lista de domínios permitidos para comandos não substitui esses controles
específicos de cada capacidade.

### Controlar o navegador e o Uso do computador

Use as tabelas `[browser_use]` e `[computer_use]` em `requirements.toml` para
restringir os clientes para desktop compatíveis. Valide a política nas versões dos clientes
e nos sistemas operacionais da sua implantação. Uma regra de permissão configurada não
instala um plug-in, não concede uma permissão do sistema operacional nem aprova uma ação
que ainda exige revisão.

Para o acesso pelo navegador, configure uma política de origem. Uma origem inclui o esquema,
o host e uma porta opcional, como `https://example.com` ou
`https://*.example.com:8443`. Não inclua caminho, consulta ou fragmento. Ao contrário
das regras de domínio para a rede dos comandos, as regras de origem do navegador distinguem HTTP de HTTPS
e verificam a correspondência da porta.

Este exemplo restringe o acesso pelo navegador a um site aprovado e impede uploads
e acesso completo ao Chrome DevTools Protocol (CDP) nesse site:

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

As regras de origem correspondentes são resolvidas por campo. Uma negação correspondente prevalece; caso contrário,
a política de origem padrão fornece os campos que as regras correspondentes não especificam.
A configuração local pode adicionar restrições, mas não pode flexibilizar uma negação gerenciada.
As negações de rede e as listas exclusivas de permissões de rede gerenciadas continuam válidas.

Defina `browser_use.disable_auto_review = true` para desativar a revisão automática de aprovações
para ações do navegador ou defina `auto_review = "deny"` em uma política de origem
para restringi-la nessa origem. Isso controla o tratamento das aprovações; não
desativa o monitoramento de segurança do modelo.

Para aplicativos nativos, defina uma política de acesso padrão e identifique os aplicativos permitidos. Por
exemplo, esta política do macOS permite o uso da Calculadora e impede que aprovações sejam salvas:

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

As políticas do Windows podem identificar aplicativos empacotados com
`computer_use.windows.aumids` ou executáveis com
`computer_use.windows.exes`. As regras para executáveis exigem `publisher_name`,
`product_name` e `access`; `binary_name` é opcional. Use a identidade verificada
do aplicativo, em vez de apenas seu nome de exibição.

Consulte a [referência de configuração](/pt-BR/codex/config-file/config-reference#requirementstoml)
para conhecer todos os campos e as [restrições de uso com o dispositivo bloqueado](#restrict-locked-computer-use)
para dispositivos macOS gerenciados.

### Fixar sinalizadores de recursos

Você também pode fixar [sinalizadores de recursos](/pt-BR/codex/config-file/config-basic/#feature-flags) para usuários
que recebem um arquivo `requirements.toml` gerenciado:

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

Use as chaves canônicas de recursos da tabela `[features]` de `config.toml` para
os recursos do ambiente de execução. O ambiente de execução local normaliza os recursos reconhecidos para respeitar esses
valores fixados e rejeita gravações conflitantes em `config.toml` ou nas configurações de recursos dos arquivos de
perfil.

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` desativa o painel do navegador integrado.
- `in_app_updates = false` desativa o atualizador próprio do aplicativo do ChatGPT para desktop na
  reinicialização, quando houver suporte. Isso não afeta a implantação externa de pacotes nem
  estende o suporte a versões anteriores do aplicativo. Para orientações sobre configuração e implantação, consulte
[Gerenciar atualizações do aplicativo](/pt-BR/codex/enterprise/manage-app-updates).
- `browser_use = false` desativa o Uso do computador em navegadores e a disponibilidade do Agente do navegador.
- `browser_use_full_cdp_access = false` desativa o acesso completo ao CDP no ambiente de execução
  local, inclusive o modo Desenvolvedor do navegador, e impede que o aplicativo do ChatGPT para
  desktop ative a configuração correspondente.
- `browser_use_external = false` desativa o Navegador externo.
- `computer_use = false` desativa o Uso do computador, o recurso Gravar e reproduzir e os fluxos
  relacionados à instalação ou configuração.

Se você omitir essas chaves, a política permitirá os recursos, sujeitos à disponibilidade normal no cliente,
na plataforma e na liberação gradual.

### Restringir o uso do computador com o dispositivo bloqueado

Para impedir que os usuários ativem o [Uso com o dispositivo bloqueado](/pt-BR/codex/computer-use#locked-use)
em um Mac gerenciado, adicione este requisito:

```toml
[computer_use]
allow_locked_computer_use = false

Este requisito remove os controles para ativar o Uso com o dispositivo bloqueado. Ele não
desativa o Uso com o dispositivo bloqueado se o recurso já estiver ativado. Se você omitir esse requisito, a disponibilidade normal do produto
e a configuração local do usuário continuarão válidas.

### Configurar a política de revisão automática

Use `allowed_approvals_reviewers` para exigir ou permitir a revisão automática. Defina o valor
como `["auto_review"]` para exigir a revisão automática ou inclua `"user"` quando os usuários
puderem optar pela aprovação manual.

Defina `guardian_policy_config` para substituir a seção específica do tenant na
política de revisão automática. O ambiente de execução local continua usando o modelo integrado do revisor
e o contrato de saída. A configuração gerenciada `guardian_policy_config` tem precedência
sobre a configuração local `[auto_review].policy`.

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### Aplicar requisitos de negação de leitura

Os administradores podem negar a leitura de caminhos exatos ou correspondentes a padrões glob com
`[permissions.filesystem]`. Os usuários não podem tornar esses requisitos menos restritivos com a
configuração local.

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

Quando há requisitos de negação de leitura, o ambiente de execução local rejeita permissões de acesso completo
e mantém a execução local em um sandbox somente leitura ou com acesso ao workspace para
poder aplicá-los. No Windows nativo, o `deny_read` gerenciado se aplica às ferramentas de acesso direto a
arquivos; as leituras feitas por subprocessos do shell não usam essa regra do sandbox.

### Aplicar ganchos gerenciados definidos nos requisitos

Os administradores também podem definir ganchos de ciclo de vida gerenciados diretamente em `requirements.toml`.
Use `[hooks]` para configurar os próprios ganchos e faça `managed_dir` apontar para o
diretório em que sua ferramenta de MDM ou de gerenciamento de endpoints instala os scripts
referenciados.

Para aplicar ganchos gerenciados até mesmo aos usuários que os desativaram localmente, fixe
`[features].hooks = true` junto com `[hooks]`. Para ignorar ganchos do usuário, do projeto, da sessão
e de plug-ins sem deixar de permitir ganchos gerenciados, defina
`allow_managed_hooks_only = true`.

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

Observações:

- O ambiente de execução local aplica a configuração de ganchos definida em `requirements.toml`,
  mas não distribui os scripts em `managed_dir`.
- Distribua esses scripts com sua solução de MDM ou gerenciamento de dispositivos.
- Os comandos de ganchos gerenciados devem fazer referência a caminhos absolutos dos scripts no
diretório gerenciado configurado.
- `allow_managed_hooks_only = true` ignora ganchos provenientes de fontes do usuário, do projeto, da sessão e de
  plug-ins, mas continua carregando ganchos de `requirements.toml` e de outras camadas de
  configuração gerenciada.

### Aplicar regras de comandos definidas nos requisitos

Os administradores também podem aplicar regras restritivas de comandos definidas em `requirements.toml`
usando uma tabela `[rules]`. Essas regras são mescladas aos arquivos `.rules` comuns, e a
decisão mais restritiva continua prevalecendo.

Ao contrário de `.rules`, as regras definidas nos requisitos devem especificar `decision`, e essa decisão
deve ser `"prompt"` ou `"forbidden"` (não `"allow"`).

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

Para restringir quais servidores MCP um cliente local pode ativar, adicione em `mcp_servers`
uma lista de servidores aprovados. Para servidores stdio, use `command` como critério de correspondência; para servidores HTTP com
streaming, use `url`:

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

A representação em string de `identity.command` corresponde apenas ao `command` configurado. Ela
não inspeciona `args`, `cwd`, `env` nem `env_vars`.

Para restringir uma invocação stdio completa, faça a correspondência do executável e de cada
argumento posicional:

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

O executável, o número de argumentos e a ordem deles devem corresponder. As regras de argumentos e URL
aceitam correspondência por `exact`, por `prefix` e por `regex` aplicada ao valor completo. As regras estruturadas de
comandos continuam sem inspecionar `cwd`, `env` ou `env_vars`. Os servidores MCP incluídos em plug-ins
usam os mesmos formatos de identidade em
`plugins.<plugin>.mcp_servers.<server>`.

Se `mcp_servers` estiver presente, mas vazio, o cliente local desativa todos os servidores MCP.

### Controlar a disponibilidade de plug-ins

Para desativar plug-ins nos clientes locais compatíveis, defina `features.plugins` como
`false` em `requirements.toml`:

```toml
features.plugins = false

Essa configuração também se aplica quando os usuários entram no Codex com uma chave de API. Consulte a
[referência de
`features.plugins`](/pt-BR/codex/config-file/config-reference#requirementstoml) para conhecer a
configuração compatível.

### Restringir as fontes do marketplace de plug-ins

Para restringir operações em fontes do marketplace configuradas pelo usuário, defina
`restrict_to_allowed_sources = true` e crie uma ou mais regras para as fontes:

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

As regras Git comparam a URL normalizada do repositório e, quando presente, uma
`ref` exata. Os padrões de host são expressões regulares comparadas ao host Git
em minúsculas; use `^` e `$` para fazer a correspondência do host inteiro. As regras locais exigem um caminho absoluto e
normalizado. Consulte a [referência de `requirements.toml`](/pt-BR/codex/config-file/config-reference#requirementstoml)
para conhecer o esquema completo e o comportamento de mesclagem.

Esses requisitos rejeitam operações de adição de marketplaces, instalação de plug-ins e
atualização de marketplaces Git configurados que não correspondam às regras para fontes configuradas pelo usuário.
Os marketplaces da OpenAI gerenciados pelo Codex continuam disponíveis quando a fonte e o
nome reservado correspondem. Os requisitos não filtram marketplaces já configurados pelos usuários
nem os respectivos plug-ins durante a execução.

Essas restrições de fontes se aplicam apenas onde um cliente local oferece suporte a operações de marketplace de plug-ins: ChatGPT e Codex no aplicativo para desktop e Codex CLI.
Elas não controlam o uso de plug-ins no ChatGPT na Web ou em dispositivos móveis e não
adicionam plug-ins à extensão para IDE.

## Valores padrão gerenciados (`managed_config.toml`)

Os valores padrão gerenciados definem a configuração inicial de um cliente local compatível. Na
inicialização, eles têm precedência sobre o `config.toml` local do usuário e quaisquer substituições feitas com `--config`
na CLI. Os usuários ainda podem alterar essas configurações durante a execução atual, e os
valores padrão voltam a ser aplicados na próxima vez que o cliente for iniciado.

Se um valor padrão gerenciado, um perfil MDM do macOS ou uma configuração salva fixar `gpt-5.4`
ou `gpt-5.4-mini` para usuários conectados com o ChatGPT, atualize essa configuração antes de 31 de agosto de 2026. Substitua `gpt-5.4` por `gpt-5.6-terra` e `gpt-5.4-mini` por
`gpt-5.6-luna`. A API da OpenAI e o Codex autenticado com sua própria chave de API
não são afetados. Consulte a [disponibilidade de modelos
no workspace](/pt-BR/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement).

Verifique se os valores padrão gerenciados atendem aos seus requisitos; o ambiente de execução local
rejeita valores não permitidos.

### Precedência e camadas

O ambiente de execução local compõe a configuração efetiva nesta ordem (os itens acima
têm precedência sobre os itens abaixo):

- Preferências gerenciadas (MDM do macOS; maior precedência)
- `managed_config.toml` (arquivo do sistema/gerenciado)
- `config.toml` (configuração base do usuário)

As substituições feitas com `--config key=value` na CLI se aplicam à configuração base, mas as camadas gerenciadas têm precedência sobre elas. Isso significa que cada execução começa com os valores padrão gerenciados, mesmo quando você informa flags locais.

Os requisitos gerenciados na nuvem afetam a camada de requisitos (não os valores padrão gerenciados). Para saber a ordem de precedência, consulte a seção anterior sobre requisitos impostos por administradores.

### Locais

- Linux/macOS (Unix): `/etc/codex/managed_config.toml`
- Windows/não Unix: `~/.codex/managed_config.toml`

Se o arquivo não existir, o ambiente de execução local ignora a camada gerenciada.

### Preferências gerenciadas do macOS (MDM)

No macOS, os administradores podem distribuir um perfil de dispositivo que fornece payloads TOML codificados em base64 em:

- Domínio de preferências: `com.openai.codex`
- Chaves:
  - `config_toml_base64` (valores padrão gerenciados)
  - `requirements_toml_base64` (requisitos)

O ambiente de execução local interpreta esses payloads de "preferências gerenciadas" como TOML. Para
os valores padrão gerenciados (`config_toml_base64`), as preferências gerenciadas têm a maior
precedência. Para os requisitos (`requirements_toml_base64`), a precedência segue
a ordem dos requisitos gerenciados na nuvem descrita acima. A mesma
tabela `[features]` da camada de requisitos funciona em `requirements_toml_base64`; use
as chaves canônicas de recursos ali também.

### Fluxo de trabalho de configuração do MDM

O ambiente de execução local respeita os payloads MDM padrão do macOS, permitindo distribuir
configurações com ferramentas como `Jamf Pro`, `Fleet` ou `Kandji`. Uma implantação
simples funciona assim:

1. Crie o payload TOML gerenciado e codifique-o com `base64` (sem quebras de linha).
2. Insira a string no seu perfil MDM, no domínio `com.openai.codex`, em `config_toml_base64` (valores padrão gerenciados) ou `requirements_toml_base64` (requisitos).
3. Distribua o perfil e peça aos usuários que reiniciem o cliente local compatível e
confirmem que o resumo da configuração na inicialização reflete os valores gerenciados.
4. Ao revogar ou alterar a política, atualize o payload gerenciado; o cliente
lerá a preferência atualizada na próxima vez que for iniciado.

Evite incluir segredos ou valores dinâmicos que mudam com frequência no payload. Trate o TOML gerenciado como qualquer outra configuração de MDM sujeita ao controle de alterações.

### Exemplo de managed\_config.toml

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### Medidas de proteção recomendadas

- Prefira `workspace-write` com aprovações para a maioria dos usuários; reserve o acesso completo para contêineres controlados.
- Mantenha `network_access = false`, a menos que sua revisão de segurança permita um coletor ou os domínios necessários para seus fluxos de trabalho.
- Use a configuração gerenciada para fixar as configurações do OTel (exportador, ambiente), mas mantenha `log_user_prompt = false`, a menos que sua política permita explicitamente armazenar o conteúdo dos prompts.
- Audite periodicamente as diferenças entre o `config.toml` local e a política gerenciada para detectar desvios; as camadas gerenciadas devem ter precedência sobre flags e arquivos locais.
