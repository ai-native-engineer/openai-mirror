<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/datasets-and-reports -->

## Introdução

Em essência, a análise de dados usa os dados para orientar decisões. O objetivo não é analisar por analisar, mas produzir um artefato que ajude alguém a agir: um gráfico para a liderança, resultados de um experimento para uma equipe de produto, uma avaliação de modelo para pesquisadores ou um dashboard que oriente as operações diárias.

Uma estrutura útil, popularizada por _R for Data Science_, é um ciclo: importar e organizar os dados e, em seguida, alternar entre transformação, visualização e modelagem para compreendê-los antes de comunicar os resultados.

O ChatGPT Work se encaixa bem nesse fluxo. Ele ajuda a limpar dados, explorar hipóteses, gerar análises e produzir artefatos reproduzíveis. O objetivo não é criar um notebook para uma única ocasião, e sim uma análise que outras pessoas possam revisar, considerar confiável e executar novamente.

## Defina seu caso de uso

Escolha uma pergunta concreta que você queira responder com seus dados. Quanto mais específica ela for, mais fácil será identificar os dados de entrada, as verificações e o resultado adequados.

### Exemplo prático: valores de imóveis próximos à rodovia

Como exemplo, vamos explorar a seguinte pergunta:

> Até que ponto o valor de avaliação das casas próximas à rodovia é mais baixo?

Suponha que um conjunto de dados contenha valores de avaliação ou preços de venda de imóveis, enquanto outro contenha informações de localização, lote ou proximidade à rodovia. O trabalho não se resume a executar um modelo. É preciso garantir a confiabilidade dos dados de entrada, documentar as junções, testar a robustez do resultado e, por fim, produzir um artefato que outra pessoa possa usar.

Você pode anexar arquivos CSV ou pastas de trabalho do Excel, indicar uma planilha aprovada do Google Sheets com `@google-drive` ou usar o aplicativo para desktop quando os dados estiverem armazenados no computador.

<div data-use-case-export-only>

### Exemplo de resultado

Em uma amostra fictícia, o ChatGPT faz a correspondência entre 11 vendas de imóveis e o arquivo de distância até a rodovia e sinaliza uma venda sem uma distância correspondente. As casas a até uma milha da rodovia têm valor médio de **$500,000**, em comparação com **$600,000** para casas a uma distância de duas a cinco milhas da rodovia.

Depois de excluir o imóvel mais caro entre os mais distantes, a diferença ainda é de **$94,000**. O relatório e o gráfico explicam que a amostra é pequena, que a venda sem correspondência foi excluída e que a comparação não estabelece causalidade nem controla fatores como bairro, data da venda, trânsito ou ruído.

</div>

## Importe os dados

Comece anexando os arquivos e pedindo ao ChatGPT para inspecioná-los. Isso ajuda a responder a perguntas básicas, mas importantes:

- Quais formatos de arquivo estão presentes?
- O que cada conjunto de dados parece representar?
- Quais colunas podem corresponder a variáveis-alvo, identificadores, datas, localizações ou medidas?
- Quais são os problemas de qualidade evidentes?

Ainda não peça conclusões. Primeiro, peça um inventário e uma explicação.

## Organize e combine os dados de entrada

A maior parte do trabalho real começa aqui. Você tem dois ou mais conjuntos de dados, a chave primária não está clara e uma mesclagem ingênua pode resultar em perda de dados ou criar duplicatas.

Peça ao ChatGPT para avaliar a mesclagem antes de executá-la:

- Verifique se as chaves candidatas são únicas.
- Meça as taxas de valores nulos e as diferenças de formatação.
- Padronize a formatação quando houver problemas evidentes, como diferenças no uso de maiúsculas e minúsculas, espaços em branco ou formatação de endereços.
- Execute junções de teste e informe as taxas de correspondência.
- Recomende a estratégia de mesclagem mais segura antes de criar o arquivo mesclado final.

Se precisar derivar a melhor chave, como um endereço normalizado, um identificador de lote criado com base em algumas colunas ou uma junção por localização, peça ao ChatGPT que explique as vantagens, as desvantagens e os casos extremos antes de você aceitar a mesclagem.

## Explore os dados com gráficos

Use gráficos para entender os dados antes de escolher um modelo. No exemplo prático, compare as casas próximas à rodovia com as mais distantes, examine valores atípicos, verifique padrões de valores ausentes e confira se o efeito aparente reflete a composição dos bairros, o tamanho das casas ou algum outro fator.

Mantenha cada gráfico relacionado à pergunta original. Salve as comparações úteis para que outra pessoa possa examinar a análise.

## Modele a questão

Nem toda análise precisa de um modelo complexo. Comece com um modelo de referência interpretável.

Para a questão sobre a rodovia, uma primeira abordagem sensata é usar uma regressão ou outro modelo transparente para estimar a relação entre a proximidade da rodovia e o valor dos imóveis, controlando fatores relevantes, como tamanho, idade e localização.

Peça ao ChatGPT que deixe claro:

- As definições da variável-alvo e dos atributos.
- Quais variáveis de controle incluir e por quê.
- Os riscos de vazamento de dados e as exclusões.
- Como escolheu a divisão dos dados, a forma de avaliação ou a estimativa da incerteza.
- O que o resultado significa em linguagem simples.

Se o primeiro modelo tiver baixo desempenho, isso ainda será útil. O resultado ajudará a identificar se o problema está no modelo, nos atributos, na qualidade da junção ou na própria questão.

## Comunique o resultado

A análise só é útil quando outra pessoa consegue usá-la. Peça ao ChatGPT que produza o artefato de que o público precisa:

- Um memorando em Markdown para colaboradores técnicos.
- Uma planilha ou um arquivo CSV para operações subsequentes.
- Um documento formatado ou um PDF para tomadores de decisão.
- Um notebook, painel ou relatório estático para uma análise reutilizável.

Peça que inclua ressalvas. Se a qualidade da junção não for ideal, houver viés de amostragem ou as premissas do modelo forem frágeis, o material final deve deixar isso claro.

## Opcional: configure um ambiente Python

Se o projeto precisar de scripts reutilizáveis ou de um notebook, peça ao ChatGPT para usar o ambiente Python existente ou configurar um ambiente enxuto e reproduzível. Mantenha os arquivos de origem inalterados e salve separadamente a análise, os gráficos e o relatório final. Você não precisa configurar o Python antes de analisar arquivos anexados no ChatGPT Work.

## Prompts sugeridos

**Carregue os conjuntos de dados e explique cada um**

**Verifique a junção antes de unir os dados**

**Crie um primeiro modelo interpretável**

**Prepare os resultados para as partes interessadas**
