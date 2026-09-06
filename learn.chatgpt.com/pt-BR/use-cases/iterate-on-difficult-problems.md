<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/iterate-on-difficult-problems -->

## Introdução

Algumas tarefas são fáceis de verificar em uma única tentativa: a compilação é concluída sem erros, os testes passam e pronto. No entanto, alguns problemas de otimização são difíceis de resolver e exigem muitas iterações com um ciclo rigoroso de avaliação. Para saber que direção seguir, o Codex precisa inspecionar a saída atual, atribuir uma pontuação, decidir qual será a próxima alteração e repetir o processo até que o resultado seja realmente bom.

Esse tipo de caso de uso funciona bem com uma interface personalizada que permita inspecionar visualmente o progresso, com o Codex registrando as saídas e os artefatos gerados em cada iteração.
Você pode acompanhar o Codex trabalhando no aplicativo enquanto o artefato de destino, a saída do modelo ou o recurso gerado continua sendo aprimorado.
O essencial é fornecer ao Codex os scripts necessários para gerar as métricas de avaliação e os artefatos a serem inspecionados.

## Comece pelas avaliações

Antes de iniciar a tarefa, defina como o sucesso será medido. Em geral, a melhor configuração combina:

- **Verificações determinísticas:** aspectos que os scripts podem pontuar diretamente, como violações de restrições ou métricas determinísticas calculadas por código
- **Verificações com LLM como avaliador:** pontuações baseadas em uma rubrica de avaliação para qualidades mais difíceis de codificar com precisão, como semelhança, legibilidade, utilidade ou qualidade geral — elas podem usar saídas de texto ou imagem

Se a parte subjetiva for importante, forneça ao Codex um script que possa, por exemplo, usar a [Responses API](/api/reference/resources/responses/methods/create) para chamar um modelo e retornar pontuações estruturadas. A ideia não é substituir as verificações determinísticas, mas complementá-las com um avaliador consistente para a parte que, de outra forma, as pessoas avaliariam visualmente.

O ciclo funciona melhor quando a saída da avaliação está em formato legível por máquina, é salva após cada execução e pode ser facilmente comparada ao longo do tempo.

  **Dica**: Peça ao Codex que gere o script de avaliação para você, descrevendo as
  verificações que deseja executar.

## Defina uma regra de parada para o Codex

Tarefas difíceis muitas vezes perdem o rumo porque o prompt diz “continue melhorando” sem indicar quando parar. Deixe explícita a regra de parada.

Um padrão prático é:

1. Defina uma meta para a pontuação geral.
2. Defina uma meta separada para a média atribuída pelo LLM avaliador.
3. Diga ao Codex para continuar até que as duas fiquem acima do limite, e não apenas uma.

Por exemplo, se a meta for um artefato de alta qualidade, peça ao Codex que continue até que tanto a pontuação geral quanto a média do LLM fiquem acima de 90%. Assim, o estado da tarefa fica claro: o Codex consegue saber se o resultado ainda está abaixo da meta, o que ainda falta e se a alteração mais recente ajudou.

## Mantenha um registro contínuo do ciclo

Tarefas de longa duração são muito mais confiáveis quando o Codex faz anotações sobre o ciclo, em vez de depender apenas do contexto do chat.

Esse registro contínuo deve incluir:

- as melhores pontuações atuais
- o que mudou na última iteração
- o que a avaliação indicou ter melhorado ou piorado
- o que o Codex pretende tentar em seguida

Isso é especialmente importante quando a tarefa é executada por muito tempo. O registro serve como ponto de continuidade quando a tarefa é retomada e como histórico de autoavaliação da execução atual.

## Inspecione o artefato, não apenas os registros

Em algumas tarefas difíceis, o diff do código e a saída das métricas não são suficientes. O Codex deve examinar o artefato que produziu.

Se a saída for visual, como uma imagem gerada, um layout ou um estado renderizado, deixe o Codex inspecionar esse artefato diretamente — por exemplo, quando a saída estiver armazenada no disco como uma imagem — e comparar o resultado atual com o melhor resultado anterior ou com a rubrica definida.

Isso torna o ciclo mais robusto:

- o script de avaliação informa a pontuação
- o artefato mostra o que não foi captado pela pontuação
- a próxima alteração se baseia em ambos

Essa combinação é muito mais eficaz do que alterar o código às cegas entre as execuções.

## Explicite cada iteração

Peça ao Codex para seguir sempre o mesmo ciclo:

1. Execute as avaliações na linha de base atual.
2. Identifique, com base nas pontuações e nos artefatos, o principal modo de falha.
3. Faça uma única alteração direcionada a esse gargalo.
4. Execute as avaliações novamente.
5. Registre as novas pontuações e informe se a alteração ajudou.
6. Continue até atingir os limites.

Essa disciplina é importante. Se cada iteração alterar muitas coisas de uma só vez, o Codex não conseguirá saber qual ideia levou à melhora da pontuação. Se não fizer esse registro, a tarefa se tornará menos confiável e mais difícil de retomar.
