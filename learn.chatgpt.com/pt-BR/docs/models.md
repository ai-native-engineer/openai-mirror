<!-- source: https://learn.chatgpt.com/pt-BR/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Escolha um modelo

No aplicativo do ChatGPT para desktop, use o controle de modelo e raciocínio abaixo do
editor para escolher um modelo disponível e ajustar seu esforço de raciocínio.

Um esforço de raciocínio maior pode melhorar os resultados em tarefas complexas, mas exige
mais tempo e usa mais tokens. Comece com o esforço padrão e aumente-o quando
a tarefa exigir planejamento ou análise mais aprofundados.

O modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> vai
além de uma execução com um único agente. Ele usa
[subagentes](/codex/agent-configuration/subagents) para acelerar trabalhos complexos,
o que o torna útil para tarefas maiores que podem ser divididas entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Escolha um modelo

Estas recomendações se aplicam ao **ChatGPT Work** na Web. Use o
controle de modelo e raciocínio abaixo do editor para escolher um modelo disponível
e ajustar seu esforço de raciocínio.

Um esforço de raciocínio maior pode melhorar os resultados em tarefas complexas, mas exige
mais tempo e usa mais tokens. Comece com o esforço padrão e aumente-o quando
a tarefa exigir planejamento ou análise mais aprofundados.

O modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> vai
além de uma execução com um único agente. Ele usa
[subagentes](/codex/agent-configuration/subagents) para acelerar trabalhos complexos,
o que o torna útil para tarefas maiores que podem ser divididas entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## Escolha um modelo

Em uma sessão interativa da CLI, use `/model` para trocar de modelo ou ajustar o
esforço de raciocínio. Você também pode escolher um modelo ao iniciar o Codex com
`--model` ou seu alias `-m`:

A mesma opção funciona em execuções não interativas. Por exemplo:

Um esforço maior de raciocínio pode melhorar os resultados em tarefas complexas, mas exige
mais tempo e consome mais tokens. Comece com o esforço padrão e aumente-o quando
a tarefa exigir planejamento ou análise mais aprofundados.

O modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> vai
além de uma execução com um único agente. Ele usa
[subagentes](/codex/agent-configuration/subagents) para acelerar trabalhos complexos,
por isso é útil em tarefas maiores que podem ser divididas entre subagentes.

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## Escolha um modelo

Use o seletor de modelo abaixo do editor para escolher um modelo disponível e
o esforço de raciocínio.

Um esforço maior de raciocínio pode melhorar os resultados em tarefas complexas, mas exige
mais tempo e consome mais tokens. Comece com o esforço padrão e aumente-o quando
a tarefa exigir planejamento ou análise mais aprofundados.

O modo <strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> vai
além de uma execução com um único agente. Ele usa
[subagentes](/codex/agent-configuration/subagents) para acelerar trabalhos complexos,
por isso é útil em tarefas maiores que podem ser divididas entre subagentes.

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## Modelos recomendados

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

A disponibilidade depende da liberação gradual, da sua forma de login e do cliente que você usa.
Consulte os [preços](/pt-BR/codex/pricing) para saber sobre acesso e uso por plano, e a
[disponibilidade de modelos no workspace](/pt-BR/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)
para saber sobre o acesso no Enterprise.

  Comece com a configuração padrão de Potência disponível para sua conta. Mova o controle em direção a
**Mais inteligente** para um raciocínio mais profundo ou a **Mais rápido** para trabalhar com mais rapidez e menor custo.
  Abra **Avançado** quando quiser usar `gpt-5.6-luna` ou escolher um modelo, esforço de
  raciocínio ou velocidade específicos.

As ilustrações do seletor mostram os controles do GPT-5.6. Para contas Pro, Business
($100) e Enterprise elegíveis, a liberação gradual do Astra atualiza as opções de Potência
para Terra Leve, Sol Leve, Sol Médio, Astra Leve, Astra Médio e Astra
Extra alto. As opções podem variar conforme o plano e a etapa da liberação.

### Gerenciamento experimental de contexto

Nos clientes Codex compatíveis, usuários conectados com o ChatGPT Plus ou Pro podem ativar
o gerenciamento experimental de contexto. O Astra mantém anotações entre janelas
de contexto e pode pesquisar mensagens anteriores e resultados de ferramentas da mesma tarefa.
Esse experimento vem desativado por padrão e, no lançamento, não está disponível para contas Business, Enterprise ou
para login com chave de API.

Para ativar, defina `features.context_management.experimental_mode = true` no seu arquivo
`config.toml` e inicie uma nova tarefa. Consulte a [referência de configuração](/pt-BR/codex/config-file/config-reference)
para saber sobre essa opção e os [conceitos básicos de configuração](/pt-BR/codex/config-file/config-basic)
para localizar o arquivo. Os requisitos do workspace continuam se aplicando.

<a id="choosing-sol-terra-and-luna"></a>

## Como escolher entre Astra, Sol, Terra e Luna

Escolha **Astra** quando uma tarefa exigir a maior capacidade ao longo de várias
etapas e ferramentas. **Sol** oferece profundidade e refinamento, **Terra** é adequado para o trabalho do dia a dia
e **Luna** é adequado para tarefas bem definidas e repetíveis.

### Onde cada modelo se destaca

- **Astra, para os trabalhos mais difíceis de ponta a ponta.** Escolha Astra para fluxos de trabalho completos
  que envolvam código, aplicativos e pesquisa e exijam raciocínio e discernimento contínuos.
  Forneça as fontes, os modelos a seguir, as restrições e as verificações que definem um resultado
  útil. Astra é melhor em fazer perguntas específicas e incorporar suas
  orientações sem perder de vista o objetivo e as restrições originais.
- **Sol, para trabalhos complexos e de escopo aberto.** Escolha Sol para tarefas ambíguas, difíceis ou
  de alto valor que exijam mais análise, discernimento ou refinamento, como
  alterações complexas no código, pesquisa aprofundada ou documentos bem-acabados. Para tarefas de escopo mais restrito,
  defina os critérios de conclusão para manter o foco do trabalho.
- **Terra, a opção versátil e pragmática.** Escolha Terra para tarefas cotidianas que
  exijam raciocínio sólido e bom uso de ferramentas, quando você não precisar de toda a profundidade de Sol.
  Terra é um ponto de partida natural para trabalhos que você antes atribuía ao GPT-5.5.
- **Luna, para tarefas bem definidas e repetíveis.** Escolha Luna para tarefas específicas em grande volume
  quando você souber o que caracteriza um bom resultado, como extração,
  classificação, transformação e resumos estruturados.

### Escolha um nível de esforço de raciocínio

Use o menor esforço de raciocínio que produza o resultado de que você precisa. Aumente-o
para tarefas que exijam mais planejamento, análise ou verificação.

- O nível **Leve** no aplicativo do ChatGPT para desktop, no ChatGPT Work na Web e na extensão para IDE, ou **Baixo** na
  CLI, é adequado para tarefas rápidas e com escopo bem delimitado.
- **Médio** equilibra velocidade e profundidade em tarefas que exigem mais planejamento.
- **Alto** e **Extra alto** são adequados para trabalhos difíceis com várias etapas, fontes
  ou decisões que exigem concessões.

Não há correspondência exata entre os níveis de esforço de raciocínio do GPT-5.5 e os do GPT-5.6. Teste uma
tarefa conhecida em um nível mais baixo e ajuste conforme o resultado.

### Saiba quando usar Max ou Ultra

**Max** dá ao modelo selecionado mais tempo para raciocinar sobre uma única tarefa. Use-o
nos problemas mais difíceis, quando a profundidade for mais importante do que a velocidade ou o consumo. Se você
não encontrar Max entre as opções, será preciso ativá-lo nas configurações do aplicativo.

**Ultra** usa [subagentes](/pt-BR/codex/agent-configuration/subagents) para lidar
em paralelo com partes distintas de uma tarefa complexa. Escolha essa opção quando puder dividir o
trabalho em partes que façam sentido. A maioria das tarefas não exige Max nem Ultra.

Se Ultra não aparecer no controle deslizante de modelos do aplicativo para desktop, acesse
**Configurações** \> **Configuração** e ative **Ultra no controle deslizante do seletor de modelos**.

## Outros modelos

Quando você faz login com o ChatGPT, o Codex funciona melhor com os modelos recomendados listados acima.

  <strong>
    GPT-5.4 e GPT-5.4 mini serão retirados do Codex em 31 de agosto de 2026.
  </strong>{" "}
  Se você fizer login com o ChatGPT, substitua `gpt-5.4` por `gpt-5.6-terra` e
`gpt-5.4-mini` por `gpt-5.6-luna` em configurações salvas, agentes personalizados e
  tarefas agendadas. A API da OpenAI e o Codex autenticado com sua própria chave de API
  não são afetados.

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

Você também pode configurar o Codex para usar qualquer modelo e provedor que ofereça suporte à [API Chat Completions](https://platform.openai.com/docs/api-reference/chat) ou à [API Responses](https://platform.openai.com/docs/api-reference/responses), conforme seu caso de uso específico.

  O suporte à API Chat Completions está obsoleto e será removido em
versões futuras do Codex.

## Modelos obsoletos do Codex

Os modelos `gpt-5.4` e `gpt-5.4-mini` deixam de estar disponíveis no Codex com login pelo ChatGPT
em 31 de agosto de 2026. Substitua `gpt-5.4` por `gpt-5.6-terra` e
`gpt-5.4-mini` por `gpt-5.6-luna` nas configurações padrão do workspace, nas configurações salvas de modelos,
nas configurações gerenciadas, nos agentes personalizados e nas tarefas agendadas.

Os modelos `gpt-5.2` e `gpt-5.3-codex` já estão obsoletos no Codex quando
você faz login com o ChatGPT. Atualize scripts, arquivos de configuração e
comandos como `codex exec --model` que ainda fazem referência a esses modelos.

A API da OpenAI e o Codex autenticado com sua própria chave de API não são afetados
pela retirada do GPT-5.4. Para conferir quais modelos estão disponíveis atualmente na API, consulte a
[página de modelos da API](/api/docs/models).

## Configure seu modelo local padrão

O aplicativo do ChatGPT para desktop, a Codex CLI e a extensão para IDE usam o mesmo
[arquivo de configuração](/pt-BR/codex/config-file/config-basic) `config.toml`. Para especificar um modelo, adicione uma entrada
`model` ao arquivo de configuração. Se você não especificar um modelo, o
aplicativo do ChatGPT para desktop, a Codex CLI ou a extensão para IDE usará um modelo recomendado.

## Escolha um modelo para chats na nuvem

Atualmente, não é possível alterar o modelo padrão dos chats do Codex Cloud.
