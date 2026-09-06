<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/target-prioritization -->

## スキルの活用

[Life Science Research プラグイン](https://github.com/openai/plugins/tree/main/plugins/life-science-research)
には、エビデンス領域ごとのスキルが含まれています：

- ヒト遺伝学と GWAS：`gwas-catalog-skill`、`opentargets-skill`、`gnomad-graphql-skill`
- コホートでの再現検証と PheWAS：`finngen-phewas-skill`、`ukb-topmed-phewas-skill`、`biobankjapan-phewas-skill`、`tpmi-phewas-skill`
- 標的と疾患の関連を示すエビデンスおよび疾患コンテキスト：`opentargets-skill`、`efo-ontology-skill`
- 臨床・規制上の先例：`clinicaltrials-skill`、`opentargets-skill`、`chembl-skill`、`pharmgkb-skill`
- 文献および公開データセットのコンテキスト：`ncbi-entrez-skill`、`ncbi-pmc-skill`、`biorxiv-skill`、`ncbi-datasets-skill`、`biostudies-arrayexpress-skill`
- 発現および組織・細胞種のコンテキスト：`human-protein-atlas-skill`、`gtex-eqtl-skill`、`cellxgene-skill`、`bgee-skill`

これらのスキルは、名前を明示して使用することも、いつ使用するかを ChatGPT に判断させることもできます。

## ステップ別ガイド

1. まず、具体的な比較課題を設定し、ChatGPT に調べてもらう標的、疾患、エビデンス領域を明確に指定します。
2. `Life Science Research` プラグインを呼び出し、各エビデンス群の調査範囲を明確に区切るため、サブエージェントを使って各領域を並列に実行するよう ChatGPT に指示します。
3. ChatGPT に各領域を固定の 1～5 段階で採点し、対象疾患の直接的なエビデンスと関連する表現型のエビデンスを分けて扱うよう指示します。
4. 同じチャット内で、保存した生のペイロード、エビデンス領域別・標的別のスコア表、統合して得られた順位をレビューします。
