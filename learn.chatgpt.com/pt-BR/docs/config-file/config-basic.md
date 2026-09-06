<!-- source: https://learn.chatgpt.com/pt-BR/docs/config-file/config-basic -->

O Codex lê informações de configuração em mais de um local. Seus valores padrão pessoais ficam em `~/.codex/config.toml`, e você pode adicionar substituições específicas do projeto com arquivos `.codex/config.toml`. Por segurança, o Codex só carrega as camadas `.codex/` do projeto quando você confia nele.

## Arquivo de configuração do Codex

O Codex armazena a configuração no nível do usuário em `~/.codex/config.toml`. Para limitar as configurações a um projeto ou subpasta específicos, adicione um arquivo `.codex/config.toml` ao repositório.

Para abrir o arquivo de configuração na extensão do Codex para IDE, selecione o ícone de engrenagem no canto superior direito e, em seguida, selecione **Configurações do Codex \> Abrir config.toml**.

A CLI e a extensão para IDE compartilham as mesmas camadas de configuração. Você pode usar essas camadas para:

- Definir o modelo e o provedor padrão.
- Configurar [políticas de aprovação e configurações do Sandbox](/pt-BR/codex/agent-approvals-security#sandbox-and-approvals).
- Configurar [servidores MCP](/pt-BR/codex/extend/mcp).

## Precedência da configuração

O Codex determina os valores nesta ordem (da maior para a menor precedência):

1. Flags da CLI e substituições com `--config`
2. Arquivos de configuração do projeto: `.codex/config.toml`, ordenados da raiz do projeto até o diretório de trabalho atual (o mais próximo prevalece; somente projetos confiáveis)
3. Arquivos de [perfil](/pt-BR/codex/config-file/config-advanced#profiles) selecionados com `--profile profile-name` (`~/.codex/profile-name.config.toml`)
4. Configuração do usuário: `~/.codex/config.toml`
5. Configuração do sistema (se houver): `/etc/codex/config.toml` no Unix
6. Valores padrão integrados

Use essa precedência para definir valores padrão compartilhados em `config.toml` e manter os [arquivos de perfil](/pt-BR/codex/config-file/config-advanced#profiles) limitados aos valores que diferem.

Se você marcar um projeto como não confiável, o Codex ignorará as camadas `.codex/` específicas do projeto, incluindo a configuração, os ganchos e as regras locais do projeto. As configurações do usuário e do sistema continuarão sendo carregadas, incluindo ganchos e regras do usuário e globais.

Para substituições pontuais por meio de `-c`/`--config` (incluindo as regras de uso de aspas no TOML), consulte [Configuração avançada](/pt-BR/codex/config-file/config-advanced#one-off-overrides-from-the-cli).

  Em máquinas gerenciadas, sua organização também pode impor restrições por meio de
`requirements.toml` (por exemplo, não permitindo `approval_policy = "never"` ou
`sandbox_mode = "danger-full-access"`). Consulte [Configuração
  gerenciada](/pt-BR/codex/enterprise/managed-configuration) e [Requisitos impostos
  pelo administrador](/pt-BR/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml).

## Opções comuns de configuração

Estas são algumas das opções alteradas com mais frequência:

#### Modelo padrão

Escolha o modelo que o Codex usa por padrão na CLI e na IDE.

#### Solicitações de aprovação

Controle quando o Codex pausa para pedir aprovação antes de executar os comandos gerados.

```toml
approval_policy = "on-request"

Para entender as diferenças de comportamento entre `untrusted`, `on-request` e `never`, consulte [Executar sem solicitações de aprovação](/pt-BR/codex/agent-approvals-security#run-without-approval-prompts) e [Combinações comuns de Sandbox e aprovação](/pt-BR/codex/agent-approvals-security#common-sandbox-and-approval-combinations).

#### Nível do Sandbox

Ajuste o nível de acesso do Codex ao sistema de arquivos e à rede durante a execução de comandos.

```toml
sandbox_mode = "workspace-write"

Para saber como cada modo se comporta (incluindo os caminhos protegidos `.git`/`.codex` e as configurações padrão de rede), consulte [Sandbox e aprovações](/pt-BR/codex/agent-approvals-security#sandbox-and-approvals), [Caminhos protegidos em diretórios raiz com permissão de escrita](/pt-BR/codex/agent-approvals-security#protected-paths-in-writable-roots) e [Acesso à rede](/pt-BR/codex/agent-approvals-security#network-access).

#### Perfis de permissão

O Codex também oferece suporte a perfis de permissão nomeados para políticas reutilizáveis de acesso ao sistema de arquivos e
à rede. Os perfis integrados são `:read-only`, `:workspace` e
`:danger-full-access`. Os perfis personalizados usam tabelas `[permissions.<name>]` e um
valor correspondente em `default_permissions`. Consulte [Permissões](/pt-BR/codex/permissions).

#### Modo de Sandbox do Windows

Ao executar o Codex nativamente no Windows, defina o modo de Sandbox nativo como `elevated` na tabela `windows`. Use `unelevated` somente se você não tiver permissões de administrador ou se a configuração com privilégios elevados falhar.

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### Modo de Pesquisa na Web

O Codex ativa a Pesquisa na Web por padrão em chats locais e fornece resultados de um cache de pesquisa na Web. O cache é um índice de resultados da Web mantido pela OpenAI, portanto o modo em cache retorna resultados pré-indexados em vez de buscar páginas em tempo real. Isso reduz a exposição à injeção de prompt por conteúdo arbitrário obtido em tempo real, mas você ainda deve tratar os resultados da Web como não confiáveis. Se você estiver usando `--yolo` ou outra [configuração de Sandbox com acesso completo](/pt-BR/codex/agent-approvals-security#common-sandbox-and-approval-combinations), a Pesquisa na Web usará resultados em tempo real por padrão. Escolha um modo com `web_search`:

- `"cached"` (padrão) fornece resultados do cache de pesquisa na Web.
- `"indexed"` permite acesso externo à Web somente quando o índice de pesquisa autoriza a solicitação.
- `"live"` busca os dados mais recentes da Web (equivale a `--search`).
- `"disabled"` desativa a ferramenta de Pesquisa na Web.

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### Esforço de raciocínio

Ajuste o nível de esforço de raciocínio aplicado pelo modelo, quando houver suporte.

```toml
model_reasoning_effort = "high"

#### Estilo de comunicação

Defina um estilo de comunicação padrão para os modelos compatíveis.

```toml
personality = "friendly" # or "pragmatic" or "none"

Você pode substituir essa configuração depois, durante uma sessão ativa, com `/personality` ou por thread/turno ao usar as APIs do App Server.

#### Mapa de teclas da TUI

Personalize os atalhos do terminal em `tui.keymap`. Determinadas ações do editor recorrem às associações correspondentes de `tui.keymap.global`; quando houver suporte, as associações específicas do contexto terão precedência. Uma lista vazia remove a associação da ação.

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### Ambiente de comandos

Controle quais variáveis do ambiente o Codex encaminha aos comandos que ele inicia. Use
filtros por chave para manter apenas as variáveis necessárias:

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

O valor padrão de `ignore_default_excludes` é `true`, o que desativa a filtragem automática
de nomes de variáveis que contenham `KEY`, `SECRET` ou `TOKEN`. Defina essa opção como `false`
quando quiser usar essa filtragem automática. Para saber mais sobre regras de exclusão, precedência e
configuração legada, consulte [Política do ambiente
do shell](/pt-BR/codex/config-file/config-advanced#shell-environment-policy).

#### Diretório de logs

Altere o local onde o Codex grava os arquivos de log locais. Definir `log_dir` explicitamente também
ativa o log opcional da TUI em texto simples, `codex-tui.log`, nesse diretório.

```toml
log_dir = "/absolute/path/to/codex-logs"

Em execuções pontuais, você também pode defini-lo pela CLI:

```bash
codex -c log_dir=./.codex-log

## Flags de recursos

Use a tabela `[features]` em `config.toml` para ativar ou desativar recursos opcionais e experimentais.

### Flags de recursos comuns

| Chave                  |        Padrão        | Maturidade     | Descrição                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | Estável       | Ativar integrações com aplicativos (conectores)                                                      |
| `goals`              |         true          | Estável       | Ativar a persistência de metas e a continuação automática                                        |
| `hooks`              |         true          | Estável       | Ativar ganchos de ciclo de vida definidos em `hooks.json` ou diretamente em `[hooks]`. Consulte [Ganchos](/pt-BR/codex/hooks). |
| `fast_mode`          |         true          | Estável       | Ativar a seleção do modo Fast e o uso de `service_tier = "fast"`                          |
| `memories`           |         false         | Experimental | Ativar [Memórias](/pt-BR/codex/customization/memories)                                         |
| `multi_agent`        |         true          | Estável       | Ativar ferramentas de colaboração entre subagentes                                                      |
| `personality`        |         true          | Estável       | Ativar controles de seleção de personalidade                                                    |
| `remote_plugin`      |         true          | Estável       | Ativar o catálogo remoto de plug-ins                                                         |
| `shell_snapshot`     |         true          | Estável       | Salvar uma cópia do estado do ambiente do shell para acelerar a execução repetida de comandos                            |
| `shell_tool`         |         true          | Estável       | Ativar a ferramenta `shell` padrão                                                          |
| `unified_exec`       | `true`, exceto no Windows | Estável       | Usar a ferramenta exec unificada baseada em PTY                                                     |
| `web_search`         |         true          | Obsoleto   | Opção legada; prefira a configuração `web_search` no nível superior                                 |
| `web_search_cached`  |         false         | Obsoleto   | Opção legada que, na ausência de um valor definido, equivale a `web_search = "cached"`                            |
| `web_search_request` |         false         | Obsoleto   | Opção legada que, na ausência de um valor definido, equivale a `web_search = "live"`                              |

  Esta tabela lista sinalizadores comuns voltados ao usuário, mas não inclui todos os recursos internos ou
  em desenvolvimento. A coluna Maturidade usa rótulos como
  Experimental, Beta e Estável. Consulte [Maturidade
  dos recursos](/pt-BR/codex/feature-maturity) para saber como interpretar esses rótulos.

Omita as chaves de recursos para manter os valores padrão.

Para configurar ganchos de ciclo de vida, consulte [Ganchos](/pt-BR/codex/hooks).

### Ativar recursos

- No arquivo `config.toml`, adicione `feature_name = true` à seção `[features]`.
- Na CLI, execute `codex --enable feature_name`.
- Para ativar mais de um recurso, execute `codex --enable feature_a --enable feature_b`.
- Para desativar um recurso, defina a chave como `false` no arquivo `config.toml`.
