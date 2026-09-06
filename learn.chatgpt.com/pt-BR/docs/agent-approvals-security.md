<!-- source: https://learn.chatgpt.com/pt-BR/docs/agent-approvals-security -->

O Codex ajuda a proteger seu código e seus dados e reduz o risco de uso indevido.

  Esta página explica como operar o Codex com segurança, incluindo ambiente isolado, aprovações
  e acesso à rede. Se você procura o Codex Security, o produto para
  verificar repositórios conectados do GitHub, consulte [Codex Security](/pt-BR/codex/security).

Por padrão, o agente é executado com o acesso à rede desativado. Localmente, o Codex usa um sandbox imposto pelo sistema operacional que limita o que ele pode acessar (geralmente, o workspace atual), além de uma política de aprovação que determina quando ele deve parar e solicitar sua aprovação antes de agir.

Para uma explicação geral de como o ambiente isolado funciona no aplicativo do ChatGPT para desktop,
na Codex CLI e na extensão para IDE, consulte [ambiente isolado](/pt-BR/codex/sandboxing).
Para uma visão mais ampla da segurança empresarial, consulte o [white paper de segurança do Codex](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click).

## Sandbox e aprovações

Os controles de segurança do Codex são compostos por duas camadas que funcionam em conjunto:

- **Modo de sandbox**: o que o Codex pode fazer tecnicamente (por exemplo, onde pode gravar e se pode acessar a rede) ao executar comandos gerados pelo modelo.
- **Política de aprovação**: quando o Codex deve solicitar sua aprovação antes de executar uma ação (por exemplo, sair do sandbox, usar a rede ou executar comandos que não fazem parte de um conjunto confiável).

O Codex usa diferentes modos de sandbox dependendo de onde é executado:

- **Codex Cloud**: é executado em contêineres isolados gerenciados pela OpenAI, impedindo o acesso ao seu sistema host ou a dados não relacionados. Usa um modelo de execução em duas fases: a configuração é executada antes da fase do agente e pode acessar a rede para instalar as dependências especificadas; depois, a fase do agente é executada offline por padrão, a menos que você habilite o acesso à internet para esse ambiente. Os segredos configurados para ambientes de nuvem ficam disponíveis apenas durante a configuração e são removidos antes do início da fase do agente.
- **Codex CLI / extensão para IDE**: mecanismos no nível do sistema operacional aplicam as políticas de sandbox. Por padrão, não há acesso à rede, e as permissões de gravação são limitadas ao workspace ativo. Você pode configurar o sandbox, a política de aprovação e a rede de acordo com sua tolerância a riscos.

Na predefinição `Auto` (por exemplo, `--sandbox workspace-write --ask-for-approval on-request`), o Codex pode ler arquivos, fazer edições e executar comandos automaticamente no diretório de trabalho.

O Codex solicita aprovação para editar arquivos fora do workspace ou executar comandos que exijam acesso à rede. Se quiser conversar ou planejar sem fazer alterações, mude para o modo `read-only` com o comando `/permissions`.

O Codex também pode solicitar aprovação para chamadas de ferramentas de aplicativos (conectores) que declarem efeitos colaterais, mesmo quando a ação não for um comando de shell nem uma alteração de arquivo. Chamadas destrutivas de ferramentas de aplicativos/MCP sempre exigem aprovação quando a ferramenta declara uma anotação destrutiva, exceto quando também declara uma anotação de leitura, que tem prioridade.

## Monitoramento de segurança e tarefas pausadas

O GPT-6 Astra inclui monitoramento de segurança no Codex e no ChatGPT Work. O monitoramento
é executado de forma assíncrona e pode pausar uma tarefa se detectar um comportamento potencialmente inseguro do modelo.
A pausa pode ocorrer depois da atividade que a desencadeou; o monitoramento
não substitui o ambiente isolado, as permissões nem a revisão do resultado.

Se uma tarefa for pausada, leia o aviso e revise os resultados da análise, quando disponíveis. Retome
somente após verificar que a tarefa pode continuar com segurança. Se o aviso informar que a
tarefa foi encerrada ou não oferecer uma opção para retomá-la, não será possível retomá-la por essa
interface.

| Interface e controles de dados                                                                               | Resultados da análise e retomada                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Clientes do Codex e do ChatGPT Work com o fluxo de resultados da análise e retomada, sem os controles de dados listados aqui | Revise os resultados da análise antes de retomar.                      |
| Codex CLI e dispositivos móveis                                                                                    | Os resultados completos da análise e a retomada não estão disponíveis. A tarefa é encerrada. |
| Zero retenção de dados, Monitoramento de abuso modificado ou residência de armazenamento de dados fora dos EUA                        | Os resultados completos da análise e a retomada não estão disponíveis. A tarefa é encerrada. |

O monitoramento de segurança avalia o comportamento do modelo durante uma tarefa.
A [revisão automática de aprovações](/pt-BR/codex/sandboxing/auto-review) avalia ações individuais que
já exigem aprovação, antes de serem executadas. Uma ação aprovada pela
revisão automática de aprovações ainda pode fazer parte de uma tarefa que o monitoramento venha a pausar.

## Acesso à rede 

Para o Codex Cloud, consulte [acesso do agente à internet](/pt-BR/codex/cloud/internet-access) para habilitar o acesso completo à internet ou uma lista de domínios permitidos.

No aplicativo do ChatGPT para desktop, na Codex CLI ou na extensão para IDE, o modo de sandbox padrão `workspace-write` mantém o acesso à rede desativado, a menos que você o habilite na configuração:

```toml
[sandbox_workspace_write]
network_access = true

### Isolamento de rede

O acesso à rede é controlado por regras de destino aplicadas a scripts,
programas e subprocessos iniciados por comandos. Quando o acesso dos comandos à rede já estiver
ativado, habilite o recurso `network_proxy` para limitar esse tráfego
à política de rede configurada. A inclusão de regras de domínio não habilita o
proxy por si só.

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

Para uma sessão pontual da CLI, use a forma booleana abreviada quando precisar apenas de
ativar ou desativar o recurso e a forma de tabela quando também configurar opções de política:

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

O recurso altera a forma como o acesso à rede é controlado quando está habilitado; não concede
acesso à rede por si só. Use `sandbox_workspace_write.network_access` com a configuração
`workspace-write` para definir se os comandos terão acesso à rede:

- Rede desativada + `network_proxy` ativado: a rede permanece desativada, e o recurso não tem efeito.
- Rede ativada + `network_proxy` desativado: a rede permanece ativada, com acesso direto
  e irrestrito de saída.
- Rede ativada + `network_proxy` ativado: a rede permanece ativada, e o tráfego de saída fica
  restrito pela política de rede configurada.

O recurso de proxy também se aplica aos [perfis de permissões](/pt-BR/codex/permissions#network-permissions).
A configuração `network.enabled = true` em um perfil concede acesso à rede aos comandos, enquanto
`features.network_proxy = true` ativa a aplicação das regras de domínio
desse perfil:

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

Se você omitir o recurso de proxy neste exemplo, os comandos terão acesso direto à
rede, e a regra de permissão para `api.openai.com` não restringirá seus destinos.

Os requisitos `experimental_network` gerenciados por administradores são independentes do controle
de ativação do recurso pelo usuário. Eles podem configurar e iniciar a rede em sandbox sem
`features.network_proxy`, mas não ativam o acesso à rede quando o
sandbox ativo o mantém desativado. Consulte [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration#configure-network-access-requirements)
para ver o formato de `requirements.toml` usado pelo administrador.

#### Política de rede

As regras de domínio têm como base uma lista de permissões:

- Hosts especificados de forma exata correspondem apenas a si mesmos.
- `*.example.com` corresponde a subdomínios como `api.example.com`, mas não a
`example.com`.
- `**.example.com` corresponde tanto ao domínio raiz quanto aos subdomínios.
- Uma regra global de permissão `*` corresponde a qualquer host público que não esteja bloqueado. Considere `*`
  como acesso amplo à rede e prefira regras de escopo delimitado sempre que possível.
- `deny` sempre prevalece sobre `allow`, e o `*` global só é válido para regras de permissão.

#### Destinos locais e privados

Por padrão, `allow_local_binding = false` bloqueia destinos de loopback, link-local e
privados:

- Exceções específicas: adicione um literal exato de IP local ou uma regra de permissão para `localhost`
  quando um comando precisar acessar um destino local específico.
- Acesso mais amplo: defina `allow_local_binding = true` somente quando quiser deliberadamente
  ampliar o acesso a destinos locais ou privados.
- Curingas: regras com curingas não contam como exceções locais explícitas.
- Endereços resolvidos: nomes de host resolvidos para IPs locais ou privados permanecem bloqueados
mesmo que correspondam à lista de permissões.

#### Proteções contra rebinding de DNS

Antes de permitir um nome de host, o Codex realiza, na medida do possível, uma verificação de DNS
e da classificação de IP:

- Consultas que falham ou excedem o tempo limite são bloqueadas.
- Nomes de host resolvidos para endereços não públicos são bloqueados.
- A verificação reduz o risco de rebinding de DNS, mas não o elimina. Evitar o
rebinding por completo exigiria manter os IPs resolvidos fixos até a camada de
transporte.

Se o escopo incluir DNS hostil, aplique também controles de saída em uma camada inferior.

#### Configurações perigosas

Duas configurações ampliam deliberadamente o limite de confiança:

- `dangerously_allow_non_loopback_proxy = true` pode expor os pontos de escuta do proxy além do
  loopback.
- `dangerously_allow_all_unix_sockets = true` ignora a lista de permissões de sockets Unix.

Use essas configurações apenas em ambientes rigorosamente controlados. Quando o proxy de sockets Unix está
habilitado, os endpoints de escuta permanecem restritos ao loopback, mesmo que tenha sido solicitada uma vinculação fora dele,
para que a rede do sandbox não se torne uma ponte remota para daemons locais.

`network_proxy` fica desativado por padrão. Ao habilitá-lo:

| Configuração                                | Padrão | Comportamento                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | Inicia a rede do sandbox somente quando o acesso dos comandos à rede já está habilitado.                                                                                                           |
| `domains`                              | não definido   | Usa uma lista de permissões, portanto, nenhum destino externo é permitido até que você adicione regras `allow`. Aceita hosts exatos, curingas com escopo delimitado e regras de permissão globais com `*`; `deny` sempre tem precedência. |
| `unix_sockets`                         | não definido   | Nenhum destino de socket Unix é permitido até que você adicione regras `allow` explícitas.                                                                                                         |
| `allow_local_binding`                  | `false` | Bloqueia destinos locais e de redes privadas, a menos que você adicione uma regra de permissão para um endereço IP local literal exato ou para `localhost`, ou habilite explicitamente um acesso mais amplo a destinos locais e privados.                |
| `enable_socks5`                        | `true`  | Disponibiliza suporte a SOCKS5 quando a política permite.                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | Permite UDP via SOCKS5 quando SOCKS5 está disponível.                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | Permite que a rede do sandbox respeite um proxy upstream configurado no ambiente.                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | Mantém os endpoints de escuta no loopback, a menos que você os exponha intencionalmente fora de localhost.                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | Mantém o acesso a sockets Unix baseado em uma lista de permissões, a menos que você ignore essa proteção intencionalmente.                                                                                              |

### Tráfego fora do proxy de rede dos comandos

O proxy de rede filtra scripts, programas e processos filhos executados
no sandbox local de comandos. Ele não filtra a pesquisa na Web, chamadas de ferramentas de aplicativos ou
conectores, conexões com servidores MCP, atividades do navegador ou do Uso do computador,
tarefas do Codex Cloud nem solicitações de modelo e autenticação do cliente. Esses
recursos usam conexões de serviço separadas, configurações de recursos, políticas do workspace
ou controles do ambiente.

As ferramentas do navegador verificam separadamente os bloqueios de rede gerenciados e as listas de permissões exclusivas
antes de acessar uma origem. As políticas de origem do navegador podem restringir ainda mais o acesso a sites,
uploads, downloads e ferramentas de desenvolvedor. Consulte
[controles gerenciados do navegador](/pt-BR/codex/enterprise/managed-configuration#control-browser-and-computer-use).

Para usuários gerenciados, combine a política de rede dos comandos com controles como
`allowed_web_search_modes`, `mcp_servers` aprovados e requisitos de recursos
para aplicativos, plug-ins, navegadores ou Uso do computador. Consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration).

Você também pode controlar a [ferramenta de pesquisa na Web](https://platform.openai.com/docs/guides/tools-web-search) sem conceder acesso completo à rede aos comandos iniciados. Por padrão, o Codex usa um cache de pesquisa na Web para acessar os resultados. Esse cache é um índice de resultados da Web mantido pela OpenAI, portanto, o modo em cache retorna resultados pré-indexados em vez de buscar páginas em tempo real. Isso reduz a exposição à injeção de prompt proveniente de conteúdo arbitrário em tempo real, mas você ainda deve tratar os resultados da Web como não confiáveis. Se estiver usando `--yolo` ou outra [configuração de sandbox com acesso completo](#common-sandbox-and-approval-combinations), a pesquisa na Web usará resultados em tempo real por padrão. Use `--search` ou defina `web_search = "live"` para permitir a navegação em tempo real, ou defina a configuração como `"disabled"` para desativar a ferramenta:

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

Defina `web_search = "indexed"` quando o acesso externo à Web precisar ser controlado pelo
índice de pesquisa. Tenha cuidado ao habilitar o acesso à rede ou a pesquisa na Web no Codex.
A injeção de prompt pode levar o agente a buscar e seguir instruções não confiáveis.

## Configurações padrão e recomendações

- Ao iniciar, o Codex detecta se a pasta está sob controle de versão e recomenda:
  - Pastas sob controle de versão: `Auto` (gravação no workspace + aprovações sob solicitação)
  - Pastas sem controle de versão: `read-only`
- Dependendo da sua configuração, o Codex também pode iniciar em `read-only` até que você indique explicitamente que confia no diretório de trabalho (por exemplo, por meio de um prompt de configuração inicial ou de `/permissions`).
- O workspace inclui o diretório atual e diretórios temporários como `/tmp`. Use o comando `/status` para ver quais diretórios fazem parte do workspace.
- Para aceitar as configurações padrão, execute `codex`.
- Você pode definir essas opções explicitamente:
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### Caminhos protegidos em raízes graváveis

Na política padrão de sandbox `workspace-write`, as raízes graváveis ainda incluem caminhos protegidos:

- `<writable_root>/.git` é protegido como somente leitura, seja um diretório ou um arquivo.
- Se `<writable_root>/.git` for um arquivo de ponteiro (`gitdir: ...`), o caminho resolvido do diretório Git também será protegido como somente leitura.
- `<writable_root>/.agents` é protegido como somente leitura quando existe como diretório.
- `<writable_root>/.codex` é protegido como somente leitura quando existe como diretório.
- A proteção é recursiva, portanto, tudo dentro desses caminhos é somente leitura.

### Executar sem prompts de aprovação

Você pode desativar os prompts de aprovação com `--ask-for-approval never` ou `-a never` (forma abreviada).

Essa opção funciona com todos os modos `--sandbox`, portanto, você continua controlando o nível de autonomia do Codex. O Codex faz o possível dentro das restrições definidas por você.

Se precisar que o Codex leia arquivos, faça edições e execute comandos com acesso à rede sem prompts de aprovação, use `--sandbox danger-full-access` (ou a flag `--dangerously-bypass-approvals-and-sandbox`). Tenha cautela antes de fazer isso.

Como opção intermediária, `approval_policy = { granular = { ... } }` permite manter categorias específicas de prompts de aprovação interativas enquanto rejeita automaticamente as demais. A política granular abrange aprovações do sandbox, prompts de execpolicy-rule, prompts do MCP, prompts de `request_permissions` e aprovações de scripts de habilidades.

### Revisões automáticas de aprovações

Por padrão, as solicitações de aprovação são encaminhadas a você:

```toml
approvals_reviewer = "user"

As revisões automáticas de aprovações se aplicam quando as aprovações são interativas, como
`approval_policy = "on-request"` ou uma política de aprovação granular. Defina
`approvals_reviewer = "auto_review"` para encaminhar as solicitações de aprovação elegíveis
a um agente revisor antes de o Codex executar a solicitação:

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

Para conhecer todo o ciclo de vida do revisor, as condições de acionamento, a precedência da configuração
e o comportamento em caso de falha, consulte
[Revisão automática](/pt-BR/codex/sandboxing/auto-review).

O revisor avalia apenas ações que já exigem aprovação, como ampliações das permissões do sandbox,
solicitações de rede bloqueadas, prompts de `request_permissions` ou
chamadas de ferramentas de aplicativos e do MCP com efeitos colaterais. As ações que permanecem dentro do sandbox
prosseguem sem uma etapa adicional de revisão.

A política do revisor verifica a exfiltração de dados, a sondagem de credenciais, o enfraquecimento
persistente da segurança e ações destrutivas. Ações de risco baixo e médio
podem prosseguir quando a política permite. A política nega ações de risco crítico.
Ações de alto risco exigem autorização suficiente do usuário e nenhuma regra de negação aplicável.
Falhas na criação do prompt, na sessão de revisão e na análise sintática resultam em bloqueio por padrão. Os tempos limite são
informados separadamente, mas a ação continua sem ser executada.

A [política padrão do revisor](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
está no repositório de código aberto do Codex. Empresas podem substituir a seção
específica do locatário por `guardian_policy_config` nos requisitos gerenciados.
Também é possível usar um texto local em `[auto_review].policy`, mas os requisitos gerenciados
têm precedência. Para mais detalhes sobre a configuração, consulte
[Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration#configure-automatic-review-policy).

No aplicativo do ChatGPT para desktop, essas revisões aparecem como itens de revisão automática com status
como Em revisão, Aprovada, Negada, Interrompida ou Tempo esgotado. Também podem
incluir um nível de risco e uma avaliação da autorização do usuário para a solicitação
analisada.

A revisão automática usa chamadas adicionais ao modelo, portanto, pode aumentar o uso do Codex. Os administradores
podem limitá-la com `allowed_approvals_reviewers`.

### Combinações comuns de sandbox e aprovação

| Objetivo                                                            | Flags / configuração                                                                                                                      | Efeito                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Auto (predefinição)                                                     | _nenhuma flag necessária_ ou `--sandbox workspace-write --ask-for-approval on-request`                                                      | O Codex pode ler arquivos, fazer edições e executar comandos no workspace. O Codex exige aprovação para editar fora do workspace ou acessar a rede. |
| Navegação segura em modo somente leitura                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | O Codex pode ler arquivos e responder a perguntas. O Codex exige aprovação para fazer edições, executar comandos ou acessar a rede.                               |
| Somente leitura não interativa (CI)                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | O Codex só pode ler arquivos; nunca solicita aprovação.                                                                                              |
| Editar automaticamente, mas pedir aprovação para executar comandos não confiáveis | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | O Codex pode ler e editar arquivos, mas solicita aprovação antes de executar comandos não confiáveis.                                                           |
| Modo de revisão automática                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` ou `approvals_reviewer = "auto_review"` | Mantém os mesmos limites do sandbox do modo padrão de aprovação sob solicitação, mas os pedidos de aprovação elegíveis são avaliados pela Revisão automática em vez de serem apresentados ao usuário.  |
| Acesso completo perigoso                                             | `--dangerously-bypass-approvals-and-sandbox` (alias: `--yolo`)                                                                      |  Sem sandbox; sem aprovações _(não recomendado)_                                                                               |

Para execuções não interativas, use `codex exec --sandbox workspace-write`; o Codex mantém as invocações antigas de `codex exec --full-auto` como uma opção de compatibilidade obsoleta e exibe um aviso.

Com `--ask-for-approval untrusted`, o Codex executa automaticamente apenas operações de leitura reconhecidamente seguras. Comandos que podem alterar o estado ou acionar mecanismos de execução externa (por exemplo, operações destrutivas do Git ou flags do Git que controlam a saída ou substituem configurações) exigem aprovação.

#### Configuração em `config.toml`

Para conhecer o fluxo de configuração mais amplo, consulte [Configuração básica](/pt-BR/codex/config-file/config-basic), [Configuração avançada](/pt-BR/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) e a [Referência de configuração](/pt-BR/codex/config-file/config-reference).

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

Você também pode salvar predefinições como [arquivos de perfil](/pt-BR/codex/config-file/config-advanced#profiles) e selecioná-las com `codex --profile profile-name`:

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### Teste o sandbox localmente

Para ver o que acontece quando um comando é executado no sandbox do Codex, use estes comandos da Codex CLI:

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

O comando `sandbox` também está disponível como `codex debug`, e os utilitários de cada plataforma têm aliases (por exemplo, `codex sandbox seatbelt` e `codex sandbox landlock`).

## Sandbox no nível do sistema operacional

O Codex aplica o sandbox de maneiras diferentes dependendo do sistema operacional:

- O **macOS** usa políticas do Seatbelt e executa comandos com `sandbox-exec`, usando um perfil (`-p`) correspondente ao modo `--sandbox` selecionado. Quando o acesso restrito de leitura habilita as configurações padrão da plataforma, o Codex acrescenta uma política criteriosamente definida para o macOS (em vez de permitir acesso amplo a `/System`) para preservar a compatibilidade com ferramentas comuns.
- O **Linux** usa `bwrap` e `seccomp` por padrão.
- O **Windows** usa a implementação de sandbox do Linux quando executado no [Subsistema do Windows para Linux 2 (WSL2)](/pt-BR/codex/windows/wsl). O WSL1 teve suporte até o Codex `0.114`; a partir da versão `0.115`, o sandbox do Linux passou a usar `bwrap`, portanto o WSL1 deixou de ter suporte. Quando executado nativamente no Windows, o Codex usa uma implementação do [Sandbox do Windows](/pt-BR/codex/windows/windows-sandbox#windows-sandbox).

Se você usa a extensão do Codex para IDE no Windows, ela oferece suporte direto ao WSL2. Defina a configuração a seguir no VS Code para manter o agente dentro do WSL2 sempre que ele estiver disponível:

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

Isso garante que a extensão para IDE herde a semântica do sandbox do Linux para comandos, aprovações e acesso ao sistema de arquivos, mesmo quando o sistema operacional do host for o Windows. Saiba mais no [guia do WSL](/pt-BR/codex/windows/wsl).

Ao executar nativamente no Windows, configure o modo de sandbox nativo em `config.toml`:

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

Consulte o [guia de configuração do Windows](/pt-BR/codex/windows/windows-sandbox#windows-sandbox) para mais detalhes.

Ao executar o Linux em um ambiente em contêineres, como o Docker, o sandbox pode não funcionar se a configuração do host ou do contêiner bloquear as operações de namespace, de `bwrap` com setuid ou de `seccomp` necessárias para o Codex.

Nesse caso, configure o contêiner do Docker para fornecer o isolamento necessário e execute `codex` com `--sandbox danger-full-access` (ou com a flag `--dangerously-bypass-approvals-and-sandbox`) dentro do contêiner.

### Execute o Codex em Dev Containers

Se o host não puder executar diretamente o sandbox do Linux, ou se sua organização já tiver padronizado o desenvolvimento em contêineres, execute o Codex com Dev Containers e deixe que o Docker forneça o limite externo de isolamento. Isso funciona com Visual Studio Code Dev Containers e ferramentas compatíveis.

Use o [exemplo de contêiner de desenvolvimento seguro do Codex](https://github.com/openai/codex/tree/main/.devcontainer) como implementação de referência. O exemplo instala o Codex, ferramentas comuns de desenvolvimento, `bubblewrap` e controles de tráfego de saída baseados em firewall.

  Os contêineres de desenvolvimento oferecem proteção substancial, mas não impedem todos os
  ataques. Se você executar o Codex com `--sandbox danger-full-access` ou
`--dangerously-bypass-approvals-and-sandbox` dentro do contêiner, um projeto malicioso
  poderá exfiltrar qualquer dado disponível no contêiner de desenvolvimento, incluindo
  as credenciais do Codex. Use esse padrão somente com repositórios confiáveis e
  monitore a atividade do Codex como faria em qualquer outro ambiente com privilégios elevados.

A implementação de referência inclui:

- uma imagem base do Ubuntu 24.04 com o Codex e ferramentas comuns de desenvolvimento instalados;
- um perfil de firewall baseado em uma lista de permissões para acesso de saída;
- configurações do VS Code e recomendações de extensões para reabrir o workspace em um contêiner;
- montagens persistentes para o histórico de comandos e a configuração do Codex;
- `bubblewrap`, para que o Codex ainda possa usar seu sandbox do Linux quando o contêiner conceder as capacidades necessárias.

Para experimentar:

1. Instale o Visual Studio Code e a [extensão Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).
2. Copie a configuração `.devcontainer` do exemplo do Codex para seu repositório ou comece diretamente pelo repositório do Codex.
3. No VS Code, execute **Dev Containers: Open Folder in Container...** e selecione `.devcontainer/devcontainer.secure.json`.
4. Depois que o contêiner for iniciado, abra um terminal e execute `codex`.

Você também pode iniciar o contêiner pela CLI:

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

O exemplo tem três componentes principais:

- `.devcontainer/devcontainer.secure.json` controla as configurações, as capacidades e as montagens do contêiner, as variáveis do ambiente e as extensões do VS Code.
- `.devcontainer/Dockerfile.secure` define a imagem baseada no Ubuntu e as ferramentas instaladas.
- `.devcontainer/init-firewall.sh` aplica a política de tráfego de saída da rede.

O firewall de referência foi concebido como um ponto de partida. Se o isolamento depender de uma lista de domínios permitidos, implemente proteções contra rebinding de DNS e para atualizações de DNS adequadas ao seu ambiente, como atualizações que considerem o TTL ou um firewall com reconhecimento de DNS.

Dentro do contêiner, escolha um destes modos:

- Mantenha o sandbox do Linux do Codex habilitado se o perfil do Dev Container conceder as capacidades necessárias para que `bwrap` crie o sandbox interno.
- Se o contêiner for o limite de segurança pretendido, execute o Codex com `--sandbox danger-full-access` dentro dele para que o Codex não tente criar uma segunda camada de sandbox.

## Controle de versão

O Codex funciona melhor com um fluxo de trabalho que usa controle de versão:

- Trabalhe em uma branch de funcionalidade e garanta que `git status` não indique alterações pendentes antes de delegar. Isso facilita isolar e reverter os patches do Codex.
- Prefira fluxos de trabalho baseados em patches (por exemplo, `git diff`/`git apply`) em vez de editar diretamente os arquivos rastreados. Faça commits com frequência para poder reverter as alterações em pequenos incrementos.
- Trate as sugestões do Codex como qualquer outro PR: execute verificações direcionadas, revise os diffs e documente as decisões nas mensagens de commit para fins de auditoria.

## Monitoramento e telemetria

O Codex oferece monitoramento opcional via OpenTelemetry (OTel) para ajudar as equipes a auditar o uso, investigar problemas e atender aos requisitos de conformidade sem enfraquecer as configurações padrão de segurança local. A telemetria está desativada por padrão; habilite-a explicitamente na configuração.

### Visão geral

- Por padrão, o Codex desativa a exportação do OTel para manter as execuções locais autocontidas.
- Quando esse recurso está habilitado, o Codex emite eventos de log estruturados que abrangem chats, solicitações de API, atividade de streams SSE/WebSocket, prompts de usuários (com conteúdo ocultado por padrão), decisões de aprovação de ferramentas e resultados de ferramentas.
- O Codex marca os eventos exportados com `service.name` (origem), a versão da CLI e um rótulo de ambiente para separar o tráfego de desenvolvimento, homologação e produção.

### Habilite o OTel (opcional)

Adicione um bloco `[otel]` à configuração do Codex (normalmente em `~/.codex/config.toml`), escolha um exportador e defina se o texto dos prompts deve ser registrado.

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` mantém a instrumentação ativa, mas não envia dados a nenhum destino.
- Para enviar eventos ao seu próprio coletor, escolha uma destas opções:

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

O Codex agrupa eventos em lotes e envia os eventos pendentes ao encerrar. O Codex exporta apenas a telemetria produzida pelo seu módulo OTel.

### Categorias de eventos

Alguns exemplos de tipos de eventos são:

- `codex.conversation_starts` (modelo, configurações de raciocínio, política de sandbox/aprovação)
- `codex.api_request` (tentativa, status/sucesso, duração e detalhes do erro)
- `codex.sse_event` (tipo de evento do fluxo, sucesso/falha, duração e contagens de tokens em `response.completed`)
- `codex.websocket_request` e `codex.websocket_event` (duração da solicitação e tipo/sucesso/erro por mensagem)
- `codex.user_prompt` (comprimento; conteúdo ocultado, a menos que seu registro seja explicitamente habilitado)
- `codex.tool_decision` (aprovado/negado, origem: configuração ou usuário)
- `codex.tool_result` (duração, sucesso, trecho da saída)

As métricas OTel associadas (pares de contador e histograma de duração) incluem `codex.api_request`, `codex.sse_event`, `codex.websocket.request`, `codex.websocket.event` e `codex.tool.call` (com os instrumentos `.duration_ms` correspondentes).

Para consultar o catálogo completo de eventos e a referência de configuração, veja a [documentação de configuração do Codex no GitHub](https://github.com/openai/codex/blob/main/docs/config.md#otel).

### Orientações de segurança e privacidade

- Mantenha `log_user_prompt = false`, a menos que a política permita explicitamente o armazenamento do conteúdo dos prompts. Os prompts podem incluir código-fonte e dados sensíveis.
- Envie a telemetria somente para coletores sob seu controle; aplique limites de retenção e controles de acesso alinhados aos seus requisitos de conformidade.
- Trate os argumentos e as saídas das ferramentas como dados sensíveis. Sempre que possível, priorize o mascaramento de dados no coletor ou no SIEM.
- Revise as configurações locais de retenção de dados (por exemplo, `history.persistence` / `history.max_bytes`) se não quiser que o Codex salve transcrições de sessões em `CODEX_HOME`. Consulte [Configuração avançada](/pt-BR/codex/config-file/config-advanced#history-persistence) e [Referência de configuração](/pt-BR/codex/config-file/config-reference).
- Se você executar a CLI com o acesso à rede desativado, a exportação do OTel não conseguirá alcançar seu coletor. Para exportar, permita o acesso à rede para o endpoint do OTel no modo `workspace-write` ou exporte pelo Codex Cloud com o domínio do coletor na sua lista de domínios aprovados.
- Revise os eventos periodicamente para identificar alterações nas aprovações ou no sandbox e execuções inesperadas de ferramentas.

O OTel é opcional e foi criado para complementar, não substituir, as proteções de sandbox e aprovação descritas acima.

## Configuração gerenciada

Administradores de empresas podem definir as configurações de segurança do Codex para seu workspace em [Configuração gerenciada](/pt-BR/codex/enterprise/managed-configuration). Consulte essa página para ver detalhes sobre a configuração e as políticas.
