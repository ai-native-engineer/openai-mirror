<!-- source: https://learn.chatgpt.com/fr-FR/use-cases/target-prioritization -->

## Tirez parti des Skills

Le [plugin Life Science Research](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
comprend des Skills pour chaque axe d’analyse :

- Génétique humaine et GWAS : `gwas-catalog-skill`, `opentargets-skill`, `gnomad-graphql-skill`
- Réplication dans des cohortes et PheWAS : `finngen-phewas-skill`, `ukb-topmed-phewas-skill`, `biobankjapan-phewas-skill`, `tpmi-phewas-skill`
- Données sur l’association cible-maladie et contexte pathologique : `opentargets-skill`, `efo-ontology-skill`
- Précédents cliniques et réglementaires : `clinicaltrials-skill`, `opentargets-skill`, `chembl-skill`, `pharmgkb-skill`
- Contexte tiré de la littérature et des jeux de données publics : `ncbi-entrez-skill`, `ncbi-pmc-skill`, `biorxiv-skill`, `ncbi-datasets-skill`, `biostudies-arrayexpress-skill`
- Expression et contexte tissulaire/cellulaire : `human-protein-atlas-skill`, `gtex-eqtl-skill`, `cellxgene-skill`, `bgee-skill`

Utilisez ces Skills en les mentionnant explicitement, ou laissez ChatGPT décider quand y recourir.

## Guide étape par étape

1. Commencez par une question comparative concrète et précisez les cibles, la maladie et les axes d’analyse que ChatGPT doit couvrir.
2. Faites appel au plugin `Life Science Research` et demandez à ChatGPT de traiter les axes d’analyse en parallèle à l’aide de Sous-agents afin de maintenir un périmètre bien délimité pour chaque catégorie de données.
3. Demandez à ChatGPT d’attribuer à chaque axe un score sur une échelle fixe de 1 à 5 et de distinguer les données directement liées à la maladie de celles portant sur des phénotypes apparentés.
4. Dans la même discussion, examinez les charges utiles brutes enregistrées, le tableau des scores par axe et par cible, ainsi que le classement de synthèse.
