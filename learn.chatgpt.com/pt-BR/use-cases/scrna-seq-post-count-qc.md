<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/scrna-seq-post-count-qc -->

## Aproveite as habilidades

O plug-in NGS Analysis inclui:

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

Ao usar o plug-in, o ChatGPT pode usar todas essas habilidades reunidas no pacote.

## Guia passo a passo

1. Indique ao ChatGPT a matriz, os códigos de barras, os genes ou características, o manifesto e os metadados do conjunto de dados que devem ser usados, ou forneça referências exatas aos arquivos.
2. Execute o prompt inicial para que o ChatGPT escolha os limiares de QC com base nas distribuições observadas e registre a justificativa nos artefatos da execução.
3. Abra o índice de visualizações e o notebook ou aplicativo de revisão para examinar as contagens de aprovação ou reprovação no QC, os UMAPs e o nível de confiança das anotações.
4. Continue no mesmo chat para refinar os limiares, fornecer um atlas de referência compatível ou executar novamente após desbloquear a detecção de dupletos.

## Resultados

A execução gera uma interface para revisar as decisões de filtragem, não apenas uma
matriz filtrada. Comece pelos gráficos de justificativa dos limiares e pelo resumo de QC
para ver quantas células cada filtro removeu ou sinalizou e
se os valores de corte selecionados correspondem às distribuições observadas.

![Examine os gráficos de justificativa dos limiares e as contagens de aprovação ou reprovação no QC de uma análise de célula única.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

Depois, examine os UMAPs gerados por rótulo geral e por cluster de Leiden. Essas
visualizações facilitam a identificação de lacunas nas anotações, clusters suspeitos ou
escolhas de limiares que precisam de outra rodada de revisão.

![Examine os gráficos de UMAP por rótulo geral e por cluster de Leiden.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

Por fim, revise as métricas por célula e os resultados da filtragem. O ChatGPT preserva
esta tabela junto com o arquivo `.h5ad` filtrado e os artefatos de visualização, para que você possa
revisar os limiares no mesmo chat sem perder a justificativa da
primeira rodada.

![Abra as métricas de QC por célula e os resultados da filtragem para revisão.](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)
