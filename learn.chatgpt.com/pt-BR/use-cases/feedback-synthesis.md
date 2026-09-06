<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/feedback-synthesis -->

## Antes de começar

O feedback sobre o produto pode estar no Slack, em exportações de pesquisas, rastreadores de issues, registros de suporte ou notas de pesquisa. Forneça ao ChatGPT Work as fontes, a área do produto e o intervalo de datas para a análise. Ele pode agrupar problemas recorrentes em uma planilha ou um documento que a equipe possa conferir antes de decidir o que fazer em seguida.

Inicie esse fluxo de trabalho no Work pela Web ou pelo aplicativo para desktop, usando Apps conectados e arquivos na nuvem. Se a fonte estiver no seu computador, primeiro anexe uma exportação local ou use o aplicativo para desktop.

## O que esperar

Veja um exemplo que usa uma exportação de pesquisa, registros de suporte, uma conversa de feedback e notas de pesquisa para uma fila de revisão de solicitações. A primeira análise agrupa os problemas recorrentes; a etapa seguinte divide um tema amplo em duas decisões mais claras.

<div data-use-case-export-only>

A primeira análise identificou três problemas recorrentes ao cruzar uma pesquisa, registros de suporte, uma conversa de feedback e notas de pesquisa:

- **Os conflitos ficam ocultos na fila:** oito menções nas quatro fontes. Exiba o status dos conflitos na lista e diferencie `Ready` de `Needs attention`.
- **A aprovação em massa pode incluir solicitações bloqueadas:** quatro menções nas quatro fontes. Por padrão, não inclua as solicitações bloqueadas ou exiba um aviso antes da aprovação.
- **Os revisores perdem o ponto em que pararam e não conseguem isolar itens de trabalho:** dez menções nas quatro fontes. Preserve o estado da pesquisa e dos filtros e ofereça uma visualização de itens com status `Needs attention`.

Após uma etapa de acompanhamento para separar o último tema, a tabela diferencia **a redefinição da pesquisa e dos filtros ao retornar** da **dificuldade de isolar itens bloqueados e não revisados**. A tabela mantém, junto a cada tema, os usuários afetados, os IDs das evidências, o nível de confiança, as implicações de design, as perguntas em aberto e as ações de acompanhamento. As contagens representam menções recorrentes em uma amostra pequena, não taxas de incidência em todo o produto.

</div>

## Como funciona

1. Informe ao Work as fontes de feedback, a área do produto e o período da análise.
2. Peça ao Work que agrupe o feedback recorrente em temas e mantenha os links ou IDs das evidências junto a cada tema.
3. Crie um documento ou uma planilha do Google com os usuários afetados, o nível de confiança, as perguntas em aberto e a decisão ou ação de acompanhamento necessária.
4. Revise o resumo antes de transformar qualquer tema em uma atualização no Slack ou em um rascunho de issue.

Use o prompt inicial desta página na primeira análise e depois refine qualquer tema que seja amplo demais, não tenha evidências ou misture problemas distintos.

## Transforme um tema revisado no próximo rascunho

Depois que o resumo estiver pronto, peça ao Work que divida um tema amplo, acrescente as evidências ausentes, prepare o rascunho de uma atualização no Slack ou transforme um tema revisado em um rascunho de issue. Especifique o público e a decisão para deixar clara a próxima etapa.

## Mantenha um canal de feedback atualizado

Para um canal do Slack ou uma fila de issues que recebe novos relatos continuamente, peça ao Work para [fazer verificações programadas](/pt-BR/codex/automations#schedule-work-from-a-task). Mantenha os mesmos limites de revisão para evitar que o novo feedback gere uma publicação, uma issue ou uma atribuição sem aprovação.
