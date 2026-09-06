<!-- source: https://learn.chatgpt.com/pt-BR/docs/customization/memories -->

Com as Memórias, o ChatGPT e o Codex podem reaproveitar contexto útil de trabalhos anteriores em
trabalhos futuros.
O ChatGPT na Web usa a memória do ChatGPT, enquanto os clientes locais do Codex usam um repositório local
separado para memórias, com controles próprios.

Mantenha as orientações obrigatórias da equipe em `AGENTS.md` ou na documentação versionada. Considere
as memórias uma camada útil para recuperar contexto, não a única fonte das regras que devem
ser sempre aplicadas.

No aplicativo do ChatGPT para desktop, use `/memories` para escolher se um chat pode usar
memórias locais ou contribuir para memórias futuras. Gerencie o recurso em
**Configurações \> Personalização** quando precisar ativá-lo ou desativá-lo.

Gerencie a memória do ChatGPT em **Configurações \> Personalização**. O ChatGPT Work usa
as configurações de memória disponíveis para sua conta e seu workspace; ele não usa
um repositório local de memórias do Codex nem controles locais de memória.

No Codex CLI, use `/memories` em uma sessão interativa para controlar se o
chat atual pode usar memórias locais existentes ou ser usado como entrada para gerar
memórias futuras. Consulte [Configurar memórias locais](#configure-local-memories) se o
comando não estiver disponível.

A extensão para IDE usa o repositório local de memórias do host do Codex ao qual está conectada.
Quando as memórias estiverem ativadas nesse host, use os mesmos controles por chat do Codex CLI.

O [Histórico do computador](/pt-BR/codex/customization/computer-history) é um recurso para desktop disponível no macOS
que transforma as atividades em aplicativos e sites permitidos em memórias e
em uma linha do tempo que o ChatGPT e o Codex podem consultar.

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## Como funcionam as memórias locais do Codex

Depois de ativar as memórias, o Codex pode transformar contexto útil de chats anteriores elegíveis
em arquivos de memória locais. O Codex ignora sessões ativas ou de curta duração,
remove segredos dos campos de memória gerados e atualiza as memórias em
segundo plano, em vez de fazer isso imediatamente ao final de cada chat.

As memórias podem não ser atualizadas assim que um chat termina. O Codex espera até que um
chat fique inativo por tempo suficiente para não resumir um trabalho que ainda está em
andamento.

A geração de memórias também pode deixar de executar uma etapa em segundo plano quando a porcentagem restante do limite de taxa
do Codex estiver abaixo do valor mínimo configurado, para que o Codex não consuma
cota quando você estiver perto de atingir um limite.

## Armazenamento local de memórias

O Codex armazena as memórias no diretório inicial do Codex. Por padrão, esse diretório é
`~/.codex`. Consulte [Locais de configuração e estado](/pt-BR/codex/config-file/config-advanced#config-and-state-locations)
para saber como o Codex usa `CODEX_HOME`.

Os principais arquivos de memória ficam em `~/.codex/memories/` e incluem resumos,
registros persistentes, entradas recentes e evidências de suporte provenientes de chats anteriores.

Trate esses arquivos como estado gerado. Você pode inspecioná-los ao solucionar problemas
ou antes de compartilhar o diretório inicial do Codex, mas não dependa da edição manual deles
como principal forma de controle.

<a id="control-local-memories-per-task"></a>

## Controlar memórias locais por chat

No aplicativo do ChatGPT para desktop e na TUI do Codex, use `/memories` para controlar como as memórias funcionam no
chat atual. As opções por chat permitem decidir se o chat atual
pode usar memórias existentes e se o Codex pode usar esse chat para
gerar memórias futuras.

As opções por chat não alteram suas configurações globais de memória.

## Revisar memórias locais

Não armazene segredos nas memórias. O Codex remove segredos dos campos de memória
gerados, mas você ainda deve revisar os arquivos de memória antes de compartilhar o diretório inicial
do Codex ou os artefatos de memória gerados.

<a id="enable-memories"></a>
<a id="configuration"></a>

## Configurar memórias locais

As memórias locais do Codex ficam desativadas por padrão. No aplicativo do ChatGPT para desktop, abra
**Configurações \> Personalização** e ative a opção **Ativar memórias**.

Na configuração por arquivo, adicione a flag do recurso ao `config.toml`:

```toml
[features]
memories = true

Para saber onde estão os arquivos de configuração e ver a lista completa das configurações relacionadas à memória, consulte
[Configuração básica](/pt-BR/codex/config-file/config-basic) e a [referência de
configuração](/pt-BR/codex/config-file/config-reference).

Entre as configurações específicas de memória mais comuns estão:

- `memories.generate_memories`: controla se chats recém-criados podem ser
  armazenados como entradas para a geração de memórias.
- `memories.use_memories`: controla se o Codex injeta memórias existentes em
  sessões futuras.
- `memories.disable_on_external_context`: quando o valor é `true`, impede que chats que usaram
  contexto externo, como chamadas de ferramentas MCP, Pesquisa na Web ou pesquisa de ferramentas, sejam usados na
  geração de memórias. A chave mais antiga `memories.no_memories_if_mcp_or_web_search`
  continua sendo aceita como alias.
- `memories.min_rate_limit_remaining_percent`: controla a porcentagem mínima restante do
  limite de taxa do Codex necessária para iniciar a geração de memórias.
- `memories.extract_model`: substitui o modelo usado na extração de memórias
  por chat.
- `memories.consolidation_model`: substitui o modelo usado na consolidação global
  de memórias.
