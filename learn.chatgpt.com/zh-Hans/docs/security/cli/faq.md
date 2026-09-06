<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli/faq -->

查阅有关扫描代码仓库以及在终端中管理
安全发现的常见问题解答。若要安装并执行首次扫描，请先
参阅 [CLI 快速入门](/zh-Hans/codex/security/cli)。

## 代码仓库扫描

### 谁可以使用 CLI

`@openai/codex-security` 软件包是公开的。

运行扫描需要 Codex Security 访问权限。为获得最佳结果，请使用
已通过 [Trusted Access for Cyber](https://chatgpt.com/cyber) 验证的账户。

### 为何登录后扫描仍会使用 API 密钥

如果您的环境中设置了 `OPENAI_API_KEY` 或 `CODEX_API_KEY`，无交互式终端的扫描
以及 JSON 和 JSONL 扫描会默认使用环境中的
API 密钥，即使您已通过 ChatGPT 或访问令牌成功登录也是如此。
对于输出文本的交互式扫描，如果也可以使用 ChatGPT 登录，
系统会提示您选择要使用的凭据。试运行不会提示您选择，也不会加载凭据。

若要使用已存储的凭据进行扫描，请明确选择相应凭据：

```bash
npx @openai/codex-security scan . --auth chatgpt

若要强制使用来自 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 的 API 密钥：

```bash
npx @openai/codex-security scan . --auth api-key

若要默认自动使用您已存储的凭据，请运行
`unset OPENAI_API_KEY CODEX_API_KEY`。如需了解所有受支持的身份验证模式，
请参阅 [CLI 参考资料](/zh-Hans/codex/security/cli/reference#select-scan-authentication)。

### 如何批量扫描代码仓库

使用 GitHub CLI 登录：

```bash
gh auth login

查找并选择 GitHub 账户或组织中的代码仓库：

```bash
npx @openai/codex-security bulk-scan

如果已有准备好的列表，请提供代码仓库 CSV 文件和输出目录：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

请参阅[运行批量安全扫描](/zh-Hans/codex/security/cli/bulk-scans)，了解 GitHub
代码仓库查找、CSV 格式、批量扫描任务结果和可用选项。

### 中断的批量扫描能否恢复

可以。使用原始 CSV 文件和输出目录运行相同的批量扫描命令。
Codex Security 会跳过已完成的代码仓库。

添加 `--max-attempts 3`，以重试代码仓库或扫描过程中出现的临时错误：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

覆盖范围为 `partial` 或 `unknown` 的已完成扫描会保留结果，并
使批量扫描任务以退出代码 `2` 结束。即使设置了
`--max-attempts`，也不会重试此类扫描。

### 扫描如何使用架构和安全策略

若要传入架构文档、威胁模型或安全策略，请使用
`--knowledge-base`：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security 将这些文档用作当前扫描的上下文。有关
支持的文件类型和目录处理方式，请参阅[添加安全
上下文](/zh-Hans/codex/security/cli/reference#add-security-context)。

## 安全发现和覆盖范围

### 团队可以在哪里找到以前的扫描结果

列出为您的代码仓库保存的扫描：

```bash
npx @openai/codex-security scans list /path/to/repository

使用结果中的扫描 ID 检查其安全发现：

```bash
npx @openai/codex-security scans show SCAN_ID

每次已完成的扫描都会将报告、安全发现、覆盖范围及相关
产物保存在一起。完整布局请参阅[扫描
产物](/zh-Hans/codex/security/cli/reference#scan-artifacts)。

若要检查已保存的扫描事件和工作进程事件，请运行 `scans logs SCAN_ID`。这些日志
未经脱敏，可能包含源代码或凭据。

### 如果 CLI 无法保存扫描历史记录，该怎么办

Codex Security 将扫描历史记录保存在工作台数据库中。如果默认
状态目录不可写，请选择代码仓库外部的
私有目录：

```bash

### 扫描如何区分新增与已知的安全发现

列出某个代码仓库所有扫描中尚未解决的安全发现：

```bash
npx @openai/codex-security findings list /path/to/repository

该列表会标识最新扫描确认的安全发现，以及更早发现但此次扫描未确认的
未解决安全发现。

比较两次扫描中的安全发现：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比较过程会按根本原因自动匹配安全发现，复用已保存的
匹配结果，并识别新增、持续存在、重新开启、已解决及状态未知的
安全发现。仅当后一次扫描覆盖其原始目标和受影响路径，且没有覆盖
缺口时，相应安全发现才会被视为已解决。

### 误报反馈机制如何运作

检查已保存的扫描，查找出现记录 ID：

```bash
npx @openai/codex-security scans show SCAN_ID

记录相应安全发现不适用的原因：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

后续对同一代码仓库的扫描会将该说明作为上下文。这些扫描
仍会独立检查当前源代码、控制措施和可达性。将某项安全发现
标记为不适用，不会屏蔽任何规则、路径或漏洞类别。

有关命令详情，请参阅[安全发现
参考资料](/zh-Hans/codex/security/cli/reference#codex-security-findings)。

### 为什么重复扫描会返回不同的安全发现

即使扫描配置相同，AI 辅助扫描的结果也可能有所不同。请先
重新运行基准扫描：

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

重新运行会保留原始扫描配置，并要求使用相同版本的插件。
如果已安装的插件发生变化，命令会停止执行。

将基准扫描与新扫描进行比较：

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

如果上下文缺失可能导致结果差异，请提供共享的架构和
安全指导。匹配功能可以识别不同扫描中本质相同的
安全发现，但无法保证每次扫描结果相同。对于任何不再出现的
重要安全发现，请直接重新检查。

### 团队如何确认修复是否生效

应用修复后，重新运行原始扫描：

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

将原始安全发现与新扫描进行比较：

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

确认新扫描覆盖原始目标和受影响路径，且不存在
覆盖缺口。然后针对当前检出的代码，直接重新检查原始
安全发现：

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

仅凭某项安全发现不再出现或扫描比较结果，无法证明修复已生效。

### 覆盖范围不完整意味着什么

覆盖范围可以是 `complete`、`partial` 或 `unknown`。请检查 `coverage.json`，
了解已排除的路径、暂缓检查的区域和未决问题，再将
扫描视为已完成审查的证据。

覆盖范围为部分或未知的扫描会返回退出代码 `2`，即使没有设置
严重性策略也是如此。这些扫描仍会保留所有可用的安全发现和覆盖范围。
如果后续扫描未覆盖先前安全发现的原始路径，就无法
确认该安全发现已经不存在。

## 自动化和成本

### 深度扫描的时间限制如何运作

启动深度扫描时，为工作进程设置截止时间：

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

默认时限为 `96` 小时。您可以设置不超过 `96` 的任意正数，
包括小数。截止时间到达后，Codex Security 会停止尚未完成的工作进程，
保留已完成的标准扫描结果，并将其汇总到最终报告中。如果
没有任何工作进程完成源代码审查，报告将记录部分覆盖，
CLI 会返回退出代码 `2`。

对于持久化设置或批量扫描任务，请将 `max_time_hours` 设置在
`[deep_scan]` 下，详见[深度扫描
配置](/zh-Hans/codex/security/cli/reference#configure-deep-scans)。

### 扫描成本限制如何运作

在开始扫描前设置以美元计的预估成本上限：

```bash
npx @openai/codex-security scan . --max-cost 5

该限制是预估值，并非硬性支出上限。已在处理中的请求
完成时，费用可能超过该限制。如果 Codex Security 汇总已完成的
工作进程结果后，深度扫描达到该限制，CLI 会保存标记为部分覆盖的
已完成报告，并以退出代码 `2` 结束。否则，它会保留
所有可用的部分输出。

### 扫描能否检查提交和 Pull Request

为已暂存和未暂存的更改安装提交前安全检查：

```bash
npx @openai/codex-security install-hook

对于 Pull Request 检查，请扫描已提交的更改并设置严重性阈值：

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

完整扫描发现严重性达到或超过所选级别的问题时，将返回退出代码 `1`。
请参阅[在 CI 中运行扫描](/zh-Hans/codex/security/cli/ci)，了解
完整的 GitHub Actions 工作流程、产物处理和 SARIF 导出。

### 其他应用能否直接运行扫描

可以。您可以使用 [TypeScript SDK](/zh-Hans/codex/security/sdk)，在应用或开发者工具中启动扫描、选择
目标、检查发现的问题和覆盖情况、跟踪进度，
并实施成本控制。
