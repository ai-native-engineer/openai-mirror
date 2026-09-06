<!-- source: https://learn.chatgpt.com/es-419/use-cases/target-prioritization -->

## Aprovecha las habilidades

El [complemento Life Science Research](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
incluye habilidades para cada línea de evidencia:

- Genética humana y GWAS: `gwas-catalog-skill`, `opentargets-skill`, `gnomad-graphql-skill`
- Replicación en cohortes y PheWAS: `finngen-phewas-skill`, `ukb-topmed-phewas-skill`, `biobankjapan-phewas-skill`, `tpmi-phewas-skill`
- Evidencia sobre la relación entre el blanco terapéutico y la enfermedad, y contexto de la enfermedad: `opentargets-skill`, `efo-ontology-skill`
- Precedentes clínicos y regulatorios: `clinicaltrials-skill`, `opentargets-skill`, `chembl-skill`, `pharmgkb-skill`
- Contexto de publicaciones y conjuntos de datos públicos: `ncbi-entrez-skill`, `ncbi-pmc-skill`, `biorxiv-skill`, `ncbi-datasets-skill`, `biostudies-arrayexpress-skill`
- Expresión y contexto del tejido o tipo celular: `human-protein-atlas-skill`, `gtex-eqtl-skill`, `cellxgene-skill`, `bgee-skill`

Usa estas habilidades mencionándolas explícitamente o deja que ChatGPT decida cuándo usarlas.

## Guía paso a paso

1. Comienza con una pregunta concreta de comparación e indica exactamente qué blancos terapéuticos, qué enfermedad y qué líneas de evidencia quieres que ChatGPT abarque.
2. Invoca el complemento `Life Science Research` y pídele a ChatGPT que ejecute las líneas en paralelo con subagentes para mantener bien delimitada cada familia de evidencia.
3. Pídele a ChatGPT que puntúe cada línea en una escala fija del 1 al 5 y mantenga separada la evidencia directa sobre la enfermedad de los fenotipos relacionados.
4. Revisa en el mismo chat las cargas útiles sin procesar guardadas, la tabla de puntuaciones por línea y blanco terapéutico y la clasificación final.
