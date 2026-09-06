<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/bulk-rna-seq-fastq-qc -->

## 利用技能

NGS Analysis 插件包括：

- `ngs-analysis-router`
- `ngs-bulk-rnaseq-counts-qc`
- `ngs-runtime-env`

当您使用该插件时，ChatGPT 可以使用其中包含的所有技能。

## 分步指南

1. 为 ChatGPT 指定包含样本表、FASTQ 文件、转录组 FASTA、基因组 FASTA 和 GTF 的目录，或提供各文件的准确路径。
2. 运行入门提示，让 ChatGPT 在执行前验证链特异性、参考文件一致性和工具就绪情况。
3. 在 ChatGPT 中打开生成的 MultiQC 和矩阵产物，审查比对率、重复情况、文库类型一致性和资源就绪情况。
4. 继续在同一聊天中解决阻碍流程的问题、使用更新后的元数据重新运行，或将生成的基因级矩阵交给后续差异表达分析流程。

## 结果

此次运行返回的是经过质控审查的计数结果包，而不是单纯的定量
输出。先查看 MultiQC 报告，找出可能影响
后续解读的警告。在此示例中，ChatGPT 会将 FastQC
序列内容警告与运行摘要一并呈现，以便团队判断
观察到的模式是否符合该文库制备方法的预期。

![结合 bulk RNA-seq 运行摘要审查 FastQC 序列内容警告。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-1.webp)

接下来，审查同一报告中的 Salmon 统计信息。比对率、
文库类型判定和重复信号可用于进行简要的就绪情况
检查，以便在开展差异表达分析前判断是否准备就绪。

![检查生成的 MultiQC 报告中的 Salmon 比对和文库类型统计信息。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-2.webp)

生成的基因级计数矩阵会保存为可复用产物。请在 ChatGPT 中打开它
以确认其中包含预期的样本和特征，然后将其保留
并与运行溯源信息放在一起，以供后续分析使用。

![打开生成的基因级计数矩阵，以进行后续审查。](/codex/use-cases/bulk-rna-seq-fastq-qc-screenshot-3.webp)
