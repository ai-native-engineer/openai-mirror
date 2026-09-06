<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/fix-findings -->

使用 Codex Security，将已接受的安全发现项转化为有针对性且
经过验证的补丁。您可以在安全工作台中操作，也可以通过提示、命令行或 CI/CD 运行修复
工作流。Codex 会验证问题，并在测试安全且可行时添加一项有针对性的回归测试，使其
在修复前失败、修复后通过。它还会检查正常
行为是否仍然有效。如果回归测试不安全或无法实施，Codex 会
记录证据缺口，并改为提供可重复执行的最有力验证
产物。

先从一个已接受的发现项着手，审查建议的补丁和验证
证据。如果该工作流符合您的标准，请在单独的 Codex 任务或 CI/CD 作业中逐一处理其他已接受的
发现项。为每项任务限定范围，可以让相关代码更改和
证据更易于审查。

## 在 UI 中修复发现项

从 **发现项** 中打开一个已接受的发现项，或从 **扫描** 中打开一项已完成的扫描。
审查相关证据，然后使用 **补丁** 生成、审查、应用并验证
一项针对性修复。

1. 生成针对性补丁

   打开该发现项，选择 **补丁** 标签页，然后选择 **生成补丁**。
   Codex 会在可行时验证或复现问题，并生成补丁
   产物，而不会修改所选检出目录。

2. 审查建议的代码差异

   逐一查看所有已更改的源代码、回归测试和验证产物。拒绝
大范围重构、无关的清理，或会削弱其他安全
控制措施的更改。

3. 在本地应用补丁

   只有确认差异可以接受后，才选择 **应用补丁**。Codex 会将
   生成的补丁原样应用到工作树，并记录该状态。继续之前，请审查
   工作树中的差异。

4. 验证修复

   选择 **验证修复**。Codex 会重新运行原始复现程序，或执行当前可用且最有力的
   利用检查。如果回归测试安全且可行，Codex 会
   检查该测试是否在修复前失败、修复后通过。如果该测试
   不安全或无法实施，Codex 会记录证据缺口，并改为提供
   可重复执行的最有力验证产物。它还会检查
   正常行为、相近的绕过方式以及代码仓库中的相关测试。

5. 审慎关闭发现项

   验证不会自动关闭发现项。请审查命令、
结果和仍存在的证据缺口，然后给出准确的原因并关闭发现项，
或保持该发现项为打开状态，以便进一步处理。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    在将生成的安全修复应用到检出目录之前，请先进行审查。
  </figcaption>
</figure>

## 从 CLI 修复发现项

对于来自扫描、工单、安全通告、漏洞披露、
安全评估或内部审查的已接受发现项，请使用 Codex CLI。

请先将 Codex Security 安装到 `CODEX_HOME` 中（`codex exec` 使用该目录），然后再
运行这些命令。全新的 CI 运行器默认不包含市场
插件。

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

请提供已知的源、汇、攻击者输入、影响、预期不变量、
复现程序、受影响的文件和验证命令。Codex 可以检查
代码仓库，以补全缺失的技术细节。在假定
产品策略或预期的安全不变量之前，Codex 应先询问您。

对于自动运行，请检出代码，并确保发现项报告可用，
然后将插件安装到运行器的 `CODEX_HOME` 中。接着启用工作空间
写入权限，并将提示传递给 `codex exec`：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## 在 CI/CD 中扫描并修复发现项

请先将 Codex Security 安装到运行器的 `CODEX_HOME` 中，再调用任一
技能。以下命令使用已安装的插件，但不会安装该插件。

在 CI/CD 中，将变更扫描与修复分开，并要求扫描
不得修改检出目录。将已完成扫描的目录保留为作业
产物，审查发现项，并为每个
已接受的待修复发现项分别启动 Codex 任务或作业。

默认情况下，`codex exec` 使用只读沙盒。运行变更扫描和
修复时都要使用 `--sandbox workspace-write`。扫描需要该权限
来保存临时产物，但提示中仍必须明确要求 `Do not modify
the checkout`。修复也需要相同的权限，才能写入针对性
补丁和验证证据。请参阅 [权限与
安全](/zh-Hans/codex/non-interactive-mode#permissions-and-safety)。

对于每次扫描和每个已接受的发现项：

1. 确定此次变更的基准修订版和头部修订版。
2. 针对该差异运行 `$codex-security:security-diff-scan`，且不要修改
   检出目录。
3. 保留完整的扫描目录，并选择要修复的发现项。
4. 对每个已接受的发现项调用一次 `$codex-security:fix-finding`，并传入
   对应的发现项 ID 以及已完成扫描的目录。
5. 生成一个针对性补丁，并添加一项在修复前
失败、修复后通过的回归测试。如果该测试不安全或无法实施，请记录
证据缺口，并改用可重复执行的最有力验证产物。
6. 验证原始问题和正常行为。分别返回每个补丁、测试
或备用验证产物、验证命令以及任何证据
缺口。

首先，在不修改检出目录的情况下扫描变更：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

然后，修复已完成扫描中的一个已接受发现项：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

对于其余每个
已接受的发现项，请在独立任务或作业中重复运行第二条命令。验证后，请按照您的常规
代码审查和发布流程合并每个补丁。如果要在
修复前将发现项移交给另一个团队，请参阅 [导出或跟踪
发现项](/zh-Hans/codex/security/plugin/export-findings)。
