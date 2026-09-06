<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/security-hardening -->

使用 `$codex-security:propose-security-hardening` 将收集的
安全证据转化为结构或架构层面的加固方案。该
工作流程可以分析已完成的 Codex Security 扫描，也可以从提供的
调查发现、披露报告、事件复盘、评估文档和
源代码着手。

结果是一份设计方案集，而不是补丁，也不能证明其能够修复漏洞。
只有在您选择某项方案并明确要求 Codex 实施相应变更后，
Codex 才会修改代码仓库。

## 准备证据

请为该工作流程提供以下内容：

- 一个扫描目录，或一组明确列出的调查发现和报告。
- 目标源代码树，以及相关修订版本或快照（如有）。
- 支持这些调查发现的 PoC、跟踪记录、事件证据
或评估材料。
- 性能、内存、兼容性、可靠性、运维、
交付时间或变更范围方面的约束。

该工作流程利用这些证据识别反复遭到破坏的不变量、分散的控制措施、
高权限关键节点、薄弱的隔离边界，以及反复出现的修复模式。
它也可能得出结论：局部修复比架构变更
更为恰当。

## 运行工作流程

发送类似以下内容的提示：

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## 审查方案集

实用的方案集应满足以下要求：

- 将每项拟议变更与具体的调查发现、源代码
和威胁模型证据关联起来。
- 说明当前设计，以及新设计
应保留的安全不变量。
- 比较不同方案，包括其残余风险、性能、
可靠性、运维、兼容性和迁移成本。
- 仅在有证据支持时才推荐某个方案，
并明确说明相关假设和待解决的问题。
- 提供上线、验证、回滚和实施方面的指导。
- 区分观察到的事实、推断和拟议的设计属性。

选择方案前，请审查相关证据并权衡各项利弊。
架构图或设计建议不能替代对原始调查发现
或已实施修复的验证。

## 使用扫描提供的加固指导

如果标准扫描、深度扫描或变更扫描产生了
可报告的调查发现，您可以请求生成加固方案集。Codex 会将方案集写入 `hardening/hardening.md`，
将结构化分析写入 `hardening/hardening.json`，并将配套提案
或图表写入 `hardening/` 目录。扫描会在 `report.md` 中提供指向该方案集的链接。

请保持整个扫描目录完整，以确保这些链接仍可用。要审查
为该方案集提供依据的各份报告，请参阅[编写漏洞
报告](/zh-Hans/codex/security/plugin/vulnerability-reports)。
