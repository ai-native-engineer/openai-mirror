<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/discover-protein-folding-architectures -->

## 探索蛋白质折叠架构假设

当您的蛋白质折叠假设需要进行不止
一轮实现时，请使用 Codex 目标模式。请为 Codex 提供范围明确的科学方向、一个
可运行的基线，以及一个可自动评分的基准。Codex 可以实现
架构分支、跟踪实验、诊断故障，并在您审查证据的同时继续
迭代。

本示例从一个具体问题出发：AlphaFold2 风格模型
如果其主干不仅表示残基和残基对，还显式表示高阶拓扑对象，能否
更高效地学习有用的蛋白质几何
结构？

## 定义范围明确的实验

AlphaFold2 已在 Evoformer 中采用强大的成对推理和三角推理。
其三角形运算可改进边表示，但仍会将结果
写回成对张量。科学家建议测试三角面和四面体单元的持久化
可学习表示能否
在数据有限的环境中提供有用的归纳偏置。

由此产生的公开代码仓库 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)，
添加了稀疏面状态 `F_ijk` 和四面体状态 `U_ijkl`，同时保留
传统的成对表示 `Z_ij`。

```text
MSA representation M
        <-> pair / edge tensor Z_ij
        <-> sparse face tensor F_ijk
        <-> sparse tetra tensor U_ijkl
        -> structure module
        -> recycled geometry
        loops back into the next pass

请从本页的起始提示、一个最小化的 AlphaFold2 风格基线
和公开的 NanoFold 基准开始。该基准为结构生物学实验提供了一个规模小、经过整理、
数据固定且可自动评分的基础
平台。首次实现应保持足够小的规模，以便先通过
有针对性的单元测试和微基准测试进行测试，再启动成本高昂的训练
运行。

## 使用目标模式开展搜索

1. 请提供一个可证伪的高层次科学假设，而不是让模型从零开始构想完整的研究规划。
2. 在 ChatGPT 中使用 GPT-5.5 Pro，将这一方向转化为包含明确约束和消融实验的实施计划。
3. 让 Codex 实现规模最小且可运行的 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold) 基线，然后通过有针对性的单元测试和微基准测试进行验证。
4. 将由此生成的代码仓库交给 Codex 目标模式，并指示它在 NanoFold 基准上对验证 `lDDT-Cα` 进行爬山优化，同时保留实验日志、计划和工件引用。
5. 持续运行目标模式，让它利用基准反馈对架构、训练方案和实验执行框架进行迭代。在本示例中，该循环运行了超过 150 小时。

使用 `PLAN.md` 记录当前策略和后续步骤，使用 `EXPERIMENTS.md` 保存
结构化的结果日志，并使用 `EXPERIMENT_NOTES.md` 记录持续更新的临时笔记。
这些工件使长期搜索可供审计，也为您指导下一轮迭代提供了稳定的
工作基础。

目标模式在这里很有用，因为这种搜索需要反复实现、
测试、跟踪实验、诊断故障，并在基准结果驱动下进行
迭代。缺乏指导的自动研究往往会偏向熟悉的局部改动，
例如调整损失函数、优化器和超参数。由科学家提供的简洁
架构假设为 Codex 划定了更有意义的搜索空间，同时仍
保留了测试、诊断和改进实现的余地。

这一工作流也适合希望评估科学家在环指导如何影响智能体式科学搜索
质量的团队。

## 示例结果

这一工作流的成果是 [SimplexFold](https://github.com/ChrisHayduk/SimplexFold)，
这是一种具有显式高阶单纯形状态的实验性架构。请结合基准日志审查
其拓扑结构，以确认每一轮迭代仍在
检验最初的科学构想。

![1-单纯形、2-单纯形和 3-单纯形蛋白质几何结构的比较。](/codex/use-cases/discover-protein-folding-architectures-simplex.webp)

值得借鉴的并不是 Codex 已自主解决蛋白质折叠问题。该
工作流展示了目标模式如何充当持久的科学工程
循环：科学家提出概念上的关键思路，Codex 则缩短
实现、实验、调试和后续搜索的周期。

应将看似有希望的诊断结果视为实现路径可行的证据，
而不是泛化能力的证明。请定期审查智能体的工作轨迹；
如果它退化为局部超参数调优，请将其重新引导至具有科学意义的架构问题，
并且只有在完成条件匹配的公开验证对比和适当次数的重复实验后，
才能将观察结果上升为结论。

## 资源

- [SimplexFold 代码仓库](https://github.com/ChrisHayduk/SimplexFold)
- [SimplexFold 基准测试计划](https://github.com/ChrisHayduk/SimplexFold/blob/main/BENCHMARK_PLAN.md)
- [NanoFold 竞赛](https://github.com/ChrisHayduk/nanoFold-Competition)
- [NanoFold 竞赛规则](https://github.com/ChrisHayduk/nanoFold-Competition/blob/main/docs/COMPETITION.md)
- [目标模式持续运行超过 150 小时](https://x.com/ChrisHayduk/status/2055757345506877759?s=20)
- [目标模式文章](https://x.com/ChrisHayduk/status/2053807198870880743?s=20)
