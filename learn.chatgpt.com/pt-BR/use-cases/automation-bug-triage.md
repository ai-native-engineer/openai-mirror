<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/automation-bug-triage -->

## Como usar

Peça ao Codex para verificar onde os bugs já aparecem: alertas do Sentry, issues do Linear e do GitHub, verificações de PR, logs de implantação, tickets de suporte e threads do Slack. Comece com uma varredura manual, ajuste o relatório no chat e depois execute a varredura de forma programada.

Use um único chat do Codex para todo o ciclo de triagem:

1. Execute uma varredura sob demanda e obtenha um rascunho da lista.
2. Revise a lista e dê feedback no mesmo chat.
3. A partir desse chat, agende uma tarefa para o trabalho de triagem.
4. Opcional: quando estiver confiante no relatório, peça ao Codex para preparar rascunhos de issues no Linear, atualizações no Slack, comentários no GitHub ou notas de repasse.

Antes de começar, instale os [plug-ins](/pt-BR/codex/plugins) de que o Codex precisa, como Sentry, Slack, Linear ou GitHub. No prompt inicial, substitua a lista de plug-ins entre colchetes por chips reais de plug-ins usando `@`. Em seguida, substitua cada fonte entre colchetes pelo local exato da pesquisa: um projeto ou URL de alerta do Sentry, um canal ou uma thread do Slack, uma equipe, visualização ou consulta do Linear, um repositório, uma consulta de issues ou uma verificação de PR no GitHub, um link de implantação, um arquivo de log, uma fila de suporte ou um painel.

## Fase 1: execute a varredura

Inicie o Codex no repositório responsável pelos bugs quando o contexto local for útil: testes, ferramentas do repositório, verificações de build ou falhas de CI. Você também pode executar a varredura a partir de qualquer repositório se for possível acessar as fontes de bugs por meio de plug-ins, conectores, servidores MCP, links, exportações, logs colados ou anexos.

Execute primeiro o prompt inicial acima. Mantenha apenas os plug-ins e as fontes que fazem parte da sua varredura.

Por exemplo, um prompt preenchido pode indicar os plug-ins e as filas, os canais ou os repositórios específicos que você quer incluir na varredura.

<div class="not-prose mb-12 rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
</div>

## Fase 2: torne o relatório útil

Antes de automatizar, verifique se o relatório é útil o bastante para ser lido todos os dias.

Uma primeira execução útil inclui:

- Bugs de alta relevância ordenados de P0 a P3.
- Relatos duplicados agrupados em um único bug.
- Cada bug inclui evidências com links ou citações curtas.
- As suposições ficam separadas dos fatos observados.
- Cada bug tem uma próxima ação recomendada e curta.

Ajuste o relatório no mesmo chat antes de agendar sua execução. Você pode pedir ao Codex para:

- Verificar mais uma fonte antes de ordenar a lista por prioridade.
- Descartar alertas ruidosos que a equipe já conhece.
- Retornar somente bugs P0 e P1.
- Combinar relatos do Slack, alertas do Sentry e falhas do GitHub quando apontarem para o mesmo bug.
- Mostrar somente o melhor link para cada bug.
- Adicionar evidências suficientes para que outra pessoa consiga reproduzir ou encaminhar a issue.

## Fase 3: automatize

Quando o relatório sob demanda já for útil, permaneça no mesmo chat e [use esse chat para agendar uma tarefa para o trabalho de triagem](/pt-BR/codex/automations#schedule-a-task-inside-a-chat). O Codex pode usar o que você refinou no chat para escrever o prompt recorrente.

**Agende o trabalho de triagem**

## Fase 4: encaminhe as próximas ações

Quando o relatório agendado estiver útil, decida para onde encaminhar o trabalho em seguida. O Codex pode preparar o rascunho de uma atualização no Slack para um canal da equipe, criar issues no Linear para os bugs que você quer acompanhar, escrever comentários no GitHub sobre um PR com falha ou preparar um repasse para quem estiver de plantão.
