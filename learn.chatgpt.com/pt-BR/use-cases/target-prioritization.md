<!-- source: https://learn.chatgpt.com/pt-BR/use-cases/target-prioritization -->

## Aproveite as Habilidades

O [plug-in Life Science Research](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
inclui Habilidades para cada frente de evidência:

- Genética humana e GWAS: `gwas-catalog-skill`, `opentargets-skill`, `gnomad-graphql-skill`
- Replicação em coortes e PheWAS: `finngen-phewas-skill`, `ukb-topmed-phewas-skill`, `biobankjapan-phewas-skill`, `tpmi-phewas-skill`
- Evidências da relação alvo-doença e contexto da doença: `opentargets-skill`, `efo-ontology-skill`
- Precedentes clínicos e regulatórios: `clinicaltrials-skill`, `opentargets-skill`, `chembl-skill`, `pharmgkb-skill`
- Contexto da literatura e de conjuntos de dados públicos: `ncbi-entrez-skill`, `ncbi-pmc-skill`, `biorxiv-skill`, `ncbi-datasets-skill`, `biostudies-arrayexpress-skill`
- Expressão e contexto por tecido/tipo celular: `human-protein-atlas-skill`, `gtex-eqtl-skill`, `cellxgene-skill`, `bgee-skill`

Use essas Habilidades mencionando-as especificamente ou deixe que o ChatGPT decida quando usá-las.

## Guia passo a passo

1. Comece com uma pergunta concreta de comparação e indique exatamente quais alvos, qual doença e quais frentes de evidência você quer que o ChatGPT aborde.
2. Acione o plug-in `Life Science Research` e peça ao ChatGPT que execute as frentes em paralelo com subagentes, para manter delimitado o escopo de cada categoria de evidência.
3. Peça ao ChatGPT que atribua uma pontuação a cada frente em uma escala fixa de 1 a 5 e mantenha as evidências diretas da doença separadas das evidências de fenótipos relacionados.
4. Revise, no mesmo Chat, os payloads brutos salvos, a tabela de pontuações por frente e por alvo e a classificação consolidada.
