<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/deep-security-scan -->

## 选择对代码仓库进行深度审查

如果您需要对代码仓库或明确指定的文件夹进行更全面的漏洞审查，
并且能够接受较长的运行时间，请使用深度扫描。Codex Security 插件会
先执行多轮发现扫描，再验证发现项并确定其优先级，
因此此工作流程比常规扫描需要更多时间和资源。

深度扫描可以审查整个代码仓库，也可以审查一个明确指定的软件包或
目录。要审查 Pull Request、提交、分支差异或工作树补丁，
请使用
[$codex-security:security-diff-scan](/zh-Hans/codex/use-cases/scan-code-changes-for-security)。

## 准备开展经授权的扫描

1. 在 Codex 中打开代码仓库，并完成 [Codex Security 插件快速入门](/zh-Hans/codex/security/plugin)。
2. 确认您拥有此代码仓库，或已获授权对其进行评估。
3. 将有关架构、信任边界、安全不变量、发现项判定标准、
   排除项和严重程度的指导写入 `SECURITY.md`。使用嵌套的 `SECURITY.md`
   文件制定目录专属策略。
4. 将支持的构建、测试和验证命令，以及代码仓库的其他
   指令保存在 `AGENTS.md` 中。
5. 运行入门提示，等待扫描完成多轮发现、
验证、攻击路径分析和最终报告等阶段。
6. 审查发现项工作空间、报告和所有证据缺口。如有需要，请索取详细的
漏洞报告或结构性加固指导。

## 修复前审查证据

最终结果应说明受影响的位置、相关行为为何可以
被触发、Codex 执行了哪些验证、仍存在哪些证据缺口，以及
范围明确的修复方向。请将缺少验证证据的发现项
与经过验证的发现项区分开来。

仅针对您已选择并审查过的发现项开始修复。请参阅
[修复积压的漏洞](/zh-Hans/codex/use-cases/remediate-vulnerability-backlog)
，逐一修复发现的问题，并进行有针对性的回归验证。

有关设置、预检、限定范围的目标和运行时长预期，请参阅 [运行深度
安全扫描](/zh-Hans/codex/security/plugin/deep-scans)。
