<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/target-prioritization -->

## 利用技能

[Life Science Research 插件](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
为每个证据维度提供了相应技能：

- 人类遗传学和 GWAS：`gwas-catalog-skill`、`opentargets-skill`、`gnomad-graphql-skill`
- 队列重复验证和 PheWAS：`finngen-phewas-skill`、`ukb-topmed-phewas-skill`、`biobankjapan-phewas-skill`、`tpmi-phewas-skill`
- 靶点与疾病的关联证据及疾病背景：`opentargets-skill`、`efo-ontology-skill`
- 临床和监管先例：`clinicaltrials-skill`、`opentargets-skill`、`chembl-skill`、`pharmgkb-skill`
- 文献和公共数据集背景：`ncbi-entrez-skill`、`ncbi-pmc-skill`、`biorxiv-skill`、`ncbi-datasets-skill`、`biostudies-arrayexpress-skill`
- 表达和组织/细胞类型背景：`human-protein-atlas-skill`、`gtex-eqtl-skill`、`cellxgene-skill`、`bgee-skill`

您可以明确指定要使用的技能，也可以让 ChatGPT 决定何时使用它们。

## 分步指南

1. 先提出一个具体的比较问题，并明确列出希望 ChatGPT 涵盖的靶点、疾病和证据维度。
2. 调用 `Life Science Research` 插件，并让 ChatGPT 使用子智能体并行分析各证据维度，确保每类证据都在明确限定的范围内处理。
3. 让 ChatGPT 按固定的 1–5 分制为每个证据维度评分，并将该疾病的直接证据与相近表型的证据分开。
4. 在同一聊天中审查已保存的原始载荷、按证据维度和靶点汇总的评分表，以及综合排名。
