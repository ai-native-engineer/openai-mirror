<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/scrna-seq-post-count-qc -->

## 利用技能

NGS Analysis 插件包括：

- `ngs-analysis-router`
- `scrna-seq-qc`
- `ngs-scrna-seq`

使用该插件时，ChatGPT 可以使用其中封装的所有技能。

## 分步指南

1. 向 ChatGPT 指明相应的矩阵、条形码、基因或特征、清单和数据集元数据，或提供确切的文件引用。
2. 运行起始提示，让 ChatGPT 根据观察到的分布选择 QC 阈值，并在运行产物中记录依据。
3. 打开可视化索引，以及用于审查的笔记本或应用，检查通过或未通过 QC 的细胞数、UMAP 和注释置信度。
4. 继续在同一聊天中优化阈值、提供匹配的参考图谱，或在排除导致双细胞检测受阻的问题后重新运行。

## 结果

此次运行会生成用于审查筛选决策的界面，而不只是
经过筛选的矩阵。首先查看阈值设定依据图和 QC
摘要，以了解每个筛选条件移除或标记了多少个细胞，并判断
所选阈值是否与观察到的分布相符。

![审查单细胞运行的阈值设定依据图和通过或未通过 QC 的细胞数。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-1.webp)

然后，按粗粒度标签和 Leiden 聚类检查生成的 UMAP。这些
视图有助于识别注释缺口、可疑聚类，或
需要重新审视的阈值选择。

![按粗粒度标签和 Leiden 聚类检查 UMAP 图。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-2.webp)

最后，审查细胞级指标和筛选结果。ChatGPT 会将
此表与经过筛选的 `.h5ad` 文件和可视化产物一并保留，以便您
在同一聊天中调整阈值，同时不会丢失
首次筛选的依据。

![打开细胞级 QC 指标和筛选结果进行审查。](/codex/use-cases/scrna-seq-post-count-qc-screenshot-3.webp)
