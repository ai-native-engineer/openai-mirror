<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/learn-a-new-concept -->

## Introdução

Aprender um novo conceito com um artigo ou curso denso exige mais do que um simples resumo. O objetivo é construir um modelo mental útil: qual problema ele aborda, o que o método de fato faz, quais evidências o sustentam, de quais premissas depende e quais partes você ainda precisa investigar.

O ChatGPT é útil nesse caso porque pode automatizar a coleta de contexto e representar conceitos complexos em diagramas ou ilustrações úteis. Esse caso de uso também é adequado para [subagentes](/pt-BR/codex/agent-configuration/subagents): um pode ler o artigo para identificar sua estrutura, outro pode reunir o contexto necessário, outro pode examinar figuras e notações, e o agente principal pode conciliar os resultados em um relatório que você poderá revisar mais tarde.

Para este caso de uso, o artefato final deve ser algo que você possa revisar com facilidade: um arquivo Markdown, como `notes/concept-report.md`, ou um documento em outro formato. Em vez de se limitar a uma resposta temporária no chat, ele deve incluir um resumo, um glossário, uma análise passo a passo, diagramas, uma tabela de evidências, limitações e questões em aberto.

## Defina o objetivo de aprendizagem

Comece definindo o conceito e o resultado que você quer obter. Uma pergunta específica torna o relatório mais útil do que um resumo amplo.

Por exemplo:

> Quero entender a ideia principal deste artigo de pesquisa, como o método funciona, por que os experimentos sustentam ou não a alegação e o que devo ler em seguida.

Esse escopo dá ao ChatGPT uma tarefa concreta. Ele deve ensinar o conceito, mas também manter explícitas as incertezas, citar as fontes das alegações e diferenciar o que o artigo afirma da sua própria interpretação.

## Exemplo prático: análise de um artigo de pesquisa

Suponha que você queira estudar um artigo sobre uma arquitetura de modelo que não conhece. Você quer um relatório que permita entender o conceito em uma rápida consulta, sem precisar ler o artigo inteiro.

Um bom resultado poderia ser assim:

- `notes/paper-report.md` com a explicação principal.
- `notes/figures/method-flow.mmd` ou um diagrama Mermaid embutido que represente o método.
- `notes/figures/concept-map.mmd` ou um pequeno SVG que mostre como os conhecimentos prévios necessários se relacionam.
- Uma tabela de evidências que associe as alegações às seções, páginas, figuras ou tabelas do artigo.
- Uma lista de leituras complementares e questões não resolvidas.

A ideia é tornar o processo de aprendizagem mais sistemático e deixar como resultado um artefato duradouro.

## Divida o trabalho entre subagentes

Os subagentes funcionam melhor quando cada um tem uma tarefa bem delimitada e um formato de resposta bem definido. Peça explicitamente ao ChatGPT que os inicie; ele não precisa usar subagentes em todas as tarefas de leitura, mas a exploração em paralelo ajuda quando o artigo é longo ou conceitualmente denso.

Para um artigo de pesquisa, uma divisão prática do trabalho é:

- **Mapa do artigo:** Extraia a formulação do problema, a contribuição, o método, os experimentos, as limitações e os resultados que o artigo afirma ter obtido.
- **Contexto necessário:** Explique os termos fundamentais, os conceitos relacionados e qualquer trabalho anterior cujo conhecimento o artigo pressuponha.
- **Notação e figuras:** Analise passo a passo as equações, os algoritmos, os diagramas, as figuras e as tabelas.
- **Revisor cético:** Verifique se as evidências sustentam as alegações, liste ressalvas e identifique baselines ausentes ou premissas pouco claras.

O agente principal deve aguardar esses subagentes, comparar as respostas e resolver as contradições. Em seguida, o ChatGPT sintetizará os resultados em um relatório coerente.

## Colete contexto adicional de forma deliberada

Quando o artigo pressupuser conhecimentos que você não tem, peça ao ChatGPT para buscar contexto em fontes aprovadas. Isso pode incluir notas locais, uma pasta de bibliografia, artigos vinculados, Pesquisa na Web, caso esteja habilitada, ou uma base de conhecimento conectada.

Se estiver aprendendo sobre um conceito interno, você pode conectar várias fontes com [plug-ins](/pt-BR/codex/plugins) para criar uma base de conhecimento.

Mantenha esta etapa bem delimitada. Diga ao ChatGPT o que deve ser considerado uma fonte confiável e como o relatório final deve usar o contexto externo:

- Defina os termos fundamentais em um glossário.
- Adicione uma breve seção "o que você precisa saber antes".
- Separe os links para leituras complementares das alegações do próprio artigo.
- Sinalize as alegações que vêm de fora do artigo.

## Gere diagramas para o relatório

Os diagramas costumam ser a maneira mais rápida de verificar se você realmente entendeu um conceito. Para um relatório em Markdown, peça ao ChatGPT diagramas que sejam fiéis ao material de origem e fáceis de atualizar.

Boas opções padrão incluem:

- Um mapa conceitual que mostre os conhecimentos prévios necessários e como eles se conectam.
- Um fluxograma do método que mostre entradas, transformações, componentes do modelo e saídas.
- Um mapa dos experimentos que conecte conjuntos de dados, métricas, baselines e alegações apresentadas.
- Um diagrama de limitações que separe premissas, modos de falha e questões em aberto.

Para relatórios cujo formato principal é Markdown, peça um diagrama Mermaid quando o destino for compatível ou, caso contrário, um pequeno arquivo SVG/PNG versionado no repositório. Peça ao ChatGPT que use a habilidade de sistema imagegen, incluída por padrão no ChatGPT, somente quando você precisar de um recurso visual ilustrativo que não precise ser exato ou de algo que não possa ser representado em um diagrama nativo do Markdown.

## Escreva o relatório em Markdown

Peça ao ChatGPT para criar um relatório suficientemente autocontido para que você possa voltar a consultá-lo mais tarde. Uma estrutura útil é:

1. Resumo executivo.
2. O que saber antes da leitura.
3. Termos-chave e notação.
4. Análise passo a passo do artigo.
5. Diagrama do método.
6. Tabela de evidências.
7. O que o artigo não comprova.
8. Questões em aberto e leituras complementares.

O relatório deve incluir referências às fontes sempre que possível. No caso de um PDF, peça referências a páginas, seções, figuras ou tabelas. Se o ChatGPT não conseguir extrair referências exatas às páginas, deve informar isso e usar referências a seções ou títulos.

## Use o relatório como base para um ciclo de estudos

O primeiro relatório é um ponto de partida. Depois de lê-lo, faça perguntas complementares e peça ao ChatGPT que revise o artefato.

Algumas perguntas complementares úteis são:

- Qual parte desse método devo entender primeiro?
- Qual é o exemplo didático mais simples que demonstra a ideia central?
- Qual figura mais contribui para sustentar o argumento do artigo?
- Qual afirmação é a mais fraca ou a menos fundamentada?
- O que devo ler em seguida se quiser implementar isso?

Quando o conceito exigir experimentação, peça ao ChatGPT que adicione um pequeno notebook ou script que recrie uma versão simplificada da ideia. Mantenha um link para esse trabalho exploratório no relatório em Markdown, para que a explicação e o experimento permaneçam juntos.

Exemplo de prompt:

## Habilidades a considerar

Use habilidades somente quando forem adequadas ao artefato que você quer criar:

- `$jupyter-notebook` para exemplos didáticos, gráficos ou reproduções simples que devem ser executáveis.
- `$imagegen` para recursos visuais ilustrativos que não precisam ser diagramas técnicos precisos.
- `$slides` quando quiser transformar o relatório em uma apresentação após concluir a etapa de aprendizagem.

Para a maioria dos relatórios de análise de artigos, é melhor usar por padrão diagramas nativos do Markdown ou arquivos SVG simples em vez de um bitmap gerado. Esses formatos são mais fáceis de comparar, revisar e atualizar à medida que sua compreensão evolui.

## Prompts sugeridos

**Crie primeiro a estrutura do relatório**

**Crie diagramas para explicar o conceito**

**Transforme o relatório em um plano de estudos**
