<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/slack-action-triage -->

## Encontre o trabalho escondido no Slack

O Slack costuma ser o ponto de partida de uma solicitação, mas nem sempre contém todo o contexto. Uma pessoa da equipe pode pedir uma resposta por DM, esclarecer a ação necessária em uma thread, compartilhar o link de um documento em um canal e depois resolver a questão sem voltar a mencionar você.

Use este fluxo de trabalho quando quiser que o ChatGPT leia o contexto no Slack, verifique se a solicitação ainda está em aberto e apresente apenas os poucos itens que realmente exigem sua atenção. O objetivo é obter uma fila priorizada de ações: o que exige uma resposta, uma decisão, o contato com alguém, a atualização de um documento ou um repasse.

## Faça a triagem

1. Informe ao ChatGPT um período, uma frente de trabalho, uma pessoa, um canal ou um tópico.
2. Peça que pesquise DMs, DMs em grupo, menções em canais e respostas relevantes em threads.
3. Peça ao ChatGPT que leia as últimas mensagens da thread antes de considerar um item não resolvido.
4. Peça uma fila priorizada por urgência e impacto.
5. Peça ao ChatGPT que prepare um rascunho da resposta, do repasse ou da tarefa de acompanhamento.

Depois de testar e adaptar o fluxo às suas necessidades, você pode [agendar uma tarefa para executar esse trabalho pelo chat](/pt-BR/codex/automations#schedule-a-task-inside-a-chat), pedindo ao ChatGPT que repita o processo conforme uma programação.

## Peça o resultado adequado

Um resultado de triagem útil deve explicar por que cada item continua em aberto. Também deve ignorar solicitações antigas às quais alguém respondeu mais tarde na thread.

Você verá algo parecido com isto:

  <p>
    <strong>Principal item de ação:</strong> Priya está pedindo exemplos concretos
    de clientes, não apenas mais ideias.
  </p>
  <p>
    <strong>Por que é importante:</strong> a atualização do lançamento precisa de pessoas reais que
    a equipe possa contatar esta semana.
  </p>
  <p>
    <strong>Evidência:</strong> a mensagem original no canal pedia casos de uso,
    mas uma resposta posterior na thread diz: "por favor, mande uma DM para mim se tiver leads."
  </p>
  <p>
    <strong>Próxima etapa:</strong> responda indicando dois leads específicos ou diga que você pode ser
    o exemplo, se isso for mais útil.
  </p>

Um bom resultado deixa as diferenças explícitas: uma ideia não é o mesmo que um lead; uma solicitação em aberto não é o mesmo que uma mensagem apenas informativa; e uma solicitação à qual você já respondeu não deve permanecer na fila.

Se houver muito ruído ou poucos itens que exijam ação, ajuste o prompt e, se necessário, informe os canais específicos do Slack nos quais o ChatGPT deve se concentrar.

## Prepare o acompanhamento

Quando a fila estiver como você quer, faça o acompanhamento no mesmo chat. Peça ao ChatGPT que prepare uma resposta ou um repasse com base nas evidências que já coletou:
