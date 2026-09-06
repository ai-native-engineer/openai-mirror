<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/draft-prds-from-sources -->

## Introdução

Antes de trabalhar em um novo produto ou recurso, é comum elaborar um documento de requisitos do produto (PRD) para alinhar o escopo e os requisitos. Na maioria das vezes, o contexto necessário para redigir esse PRD já está disponível nos sistemas internos da equipe: tickets no Linear, discussões no Slack, rascunhos no Notion ou no Google Drive etc. O ChatGPT pode reunir esse contexto e elaborar um PRD que você possa revisar e aprimorar, mantendo clara a rastreabilidade das fontes.

## Escolha as fontes

Comece pelas fontes que você quer que o ChatGPT use: o projeto do Linear, o canal ou a thread de planejamento no Slack e quaisquer documentos do Drive, páginas do Notion, anotações de reuniões ou arquivos locais que devam ser citados no PRD.
Também descreva claramente quais seções você espera no PRD, como problema, usuários, requisitos, UX, aspectos técnicos, plano de lançamento, cronograma ou decisões.

1. Comece com `$documents` quando a saída precisar ser um arquivo DOCX de verdade.
2. Indique as fontes de forma explícita: o projeto ou marco do Linear, o canal ou a thread do Slack e os documentos ou anotações que o ChatGPT deve citar.
3. Defina para o ChatGPT quais seções o PRD deve conter.
4. Revise primeiro o apêndice de fontes e, depois, os requisitos e as perguntas em aberto.
5. Use o mesmo chat para sanar lacunas, delimitar melhor o escopo e preparar o repasse.

<a id="refine-in-the-same-chat"></a>
<a id="refine-in-the-same-task"></a>

## Aprimore o PRD no mesmo chat

Use o prompt inicial desta página para criar o primeiro rascunho. Se faltar algo, indique ao ChatGPT a fonte ausente em vez de começar de novo.

## Verifique a rastreabilidade das fontes

Antes de compartilhar o PRD, peça ao ChatGPT que liste as afirmações com pouco ou nenhum respaldo nas fontes, as perguntas em aberto e as decisões que o ChatGPT considerou confirmadas. Se o apêndice de fontes não permitir auditar esses itens com facilidade, continue ajustando o PRD no mesmo chat antes de exportar ou publicar qualquer coisa.

### Prompt sugerido

**Verifique a rastreabilidade das fontes**
