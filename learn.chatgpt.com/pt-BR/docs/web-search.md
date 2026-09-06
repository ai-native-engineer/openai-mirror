<!-- source: https://learn.chatgpt.com/pt-BR/docs/web-search -->

O ChatGPT inclui uma ferramenta própria de pesquisa na Web. Trate todos os resultados da Web como
entradas não confiáveis.

No aplicativo do ChatGPT para desktop, peça informações atualizadas em um chat. O ChatGPT registra
a atividade de pesquisa junto com as outras chamadas de ferramentas na transcrição.

No ChatGPT na Web, peça informações atualizadas ou fontes. Os resultados da pesquisa e
as citações aparecem no chat quando o ChatGPT usa a pesquisa na Web. As configurações do
workspace podem limitar a disponibilidade da pesquisa.

Na CLI, use `--search` para obter resultados em tempo real em uma única execução:

```bash
codex --search "Summarize the latest release notes for this dependency"

As pesquisas aparecem como itens `web_search` na transcrição interativa e na saída de
`codex exec --json`.

Na extensão para IDE, peça ao Codex que pesquise enquanto trabalha no editor. A
extensão usa o modo de pesquisa do host do Codex ao qual está conectada. A atividade de pesquisa aparece
na transcrição do chat.

## Configurar a pesquisa na Web para uso local

Nos chats locais do Codex, a pesquisa em cache é ativada por padrão. O modo em cache usa
um índice mantido pela OpenAI em vez de buscar páginas arbitrárias em tempo real, o que
reduz — mas não elimina — o risco de injeção de prompt.

A pesquisa na Web é uma ferramenta hospedada, separada do acesso à rede dos comandos locais executados em ambiente isolado.
Ela não usa o proxy de rede nem a lista de domínios permitidos do perfil de permissões e
pode continuar disponível quando o acesso dos comandos à rede está desativado. Configure
a pesquisa com `web_search`, `tools.web_search.allowed_domains` e a configuração gerenciada
`allowed_web_search_modes`, conforme necessário. Os filtros de domínios de pesquisa não restringem
o tráfego de comandos locais, aplicativos, conectores ou servidores MCP.

Use a pesquisa em tempo real quando sua tarefa depender das informações mais recentes. Defina
`web_search = "live"` no arquivo `config.toml`. Defina `web_search = "disabled"` para desativar
a ferramenta. O modo `"indexed"` permite acesso externo à Web somente quando o
índice de pesquisa autoriza a solicitação. Quando o Codex é executado com acesso completo, a pesquisa na Web
usa resultados em tempo real por padrão. Consulte [Configuração básica](/pt-BR/codex/config-file/config-basic)
para ver os locais dos arquivos de configuração e a ordem de precedência.

### Pesquisar com um provedor de modelos personalizado

Um provedor de modelos personalizado pode optar pela pesquisa independente na Web quando oferecer suporte
a um endpoint de pesquisa compatível:

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

Para provedores personalizados, o padrão é `supports_standalone_web_search = false`.
A pesquisa independente na Web ainda está em desenvolvimento e fica desativada por padrão.
Definir essa capacidade do provedor não habilita o recurso: o provedor,
o modelo selecionado e o ambiente de execução também precisam oferecer suporte à pesquisa independente. As restrições do workspace e da
pesquisa gerenciada continuam valendo.

Para conferir os limites de rede aplicáveis aos ambientes de nuvem do Codex, consulte [Acesso
à Internet](/pt-BR/codex/cloud/internet-access).
