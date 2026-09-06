<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/target-prioritization -->

## 善用技能

[Life Science Research 外掛程式](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
包含各證據面向所需的技能：

- 人類遺傳學與 GWAS：`gwas-catalog-skill`、`opentargets-skill`、`gnomad-graphql-skill`
- 世代研究重現驗證與 PheWAS：`finngen-phewas-skill`、`ukb-topmed-phewas-skill`、`biobankjapan-phewas-skill`、`tpmi-phewas-skill`
- 標的－疾病證據與疾病脈絡：`opentargets-skill`、`efo-ontology-skill`
- 臨床與法規先例：`clinicaltrials-skill`、`opentargets-skill`、`chembl-skill`、`pharmgkb-skill`
- 文獻與公開資料集脈絡：`ncbi-entrez-skill`、`ncbi-pmc-skill`、`biorxiv-skill`、`ncbi-datasets-skill`、`biostudies-arrayexpress-skill`
- 表現量與組織／細胞類型脈絡：`human-protein-atlas-skill`、`gtex-eqtl-skill`、`cellxgene-skill`、`bgee-skill`

你可以明確指定這些技能，也可以讓 ChatGPT 決定何時使用。

## 逐步指南

1. 先從具體的比較問題開始，並明確列出希望 ChatGPT 涵蓋的標的、疾病與證據面向。
2. 叫用 `Life Science Research` 外掛程式，並要求 ChatGPT 使用子代理程式平行處理各證據面向，以明確限定每類證據的範圍。
3. 要求 ChatGPT 按固定的 1-5 分制為每個證據面向評分，並將疾病的直接證據與相鄰表型分開處理。
4. 在同一個對話中，審查已儲存的原始承載資料、證據面向 × 標的評分表，以及綜整後的排名。
