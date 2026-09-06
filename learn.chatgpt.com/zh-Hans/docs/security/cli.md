<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli -->

Codex Security 可帮助安全和工程团队发现、确认并修复漏洞。使用其命令行界面（CLI）扫描您拥有或有权评估的代码仓库，持续审查发现结果，并在更改合入前进行检查。

  `@openai/codex-security` 软件包已公开。运行扫描需要 Codex
  Security 访问权限。如需在 Codex 中进行交互式扫描，请先参阅 [Codex
  Security 插件快速入门](/zh-Hans/codex/security/plugin)。对于已连接的 GitHub
  代码仓库，请参阅 [Codex Security 云服务设置](/zh-Hans/codex/security/setup)。

## 检查先决条件

CLI 需要 Node.js 22（22.13.0 或更高版本）、24 或 26。扫描、批量扫描、
导出、扫描历史记录和已保存的发现结果还需要 Python 3.10 或更高版本。
详情请参阅[身份验证和
先决条件](/zh-Hans/codex/security/cli/reference#authentication-and-prerequisites)。

## 设置并验证 CLI

使用 `npx` 运行 CLI，并检查其版本：

```bash
npx @openai/codex-security --version

如需同时查看软件包及其随附插件的版本，请运行：

```bash
npx @openai/codex-security info --json

请参阅 [CLI 和 SDK 发布记录](https://github.com/openai/codex-security/releases)，
了解软件包的变更。

列出可用命令：

```bash
npx @openai/codex-security --help

另请参阅 [CLI 参考资料](/zh-Hans/codex/security/cli/reference)。

## 登录

在本地使用时，请使用您的 ChatGPT 账户登录：

```bash
npx @openai/codex-security login

在远程计算机或无头计算机上，请使用设备身份验证：

```bash
npx @openai/codex-security login --device-auth

对于 CI 和其他自动化工作流，请设置 OpenAI API 密钥：

```bash

有关 AWS 凭据，请参阅 [Amazon Bedrock
设置](/zh-Hans/codex/security/cli/reference#use-amazon-bedrock)。对于 [OpenRouter 或
Fireworks](/zh-Hans/codex/security/cli/reference#use-openrouter-or-fireworks)，请设置
提供商的 API 密钥，并使用 `--provider` 和 `--model` 选择模型。

如果同时设置了 API 密钥，如需使用 ChatGPT 登录，请明确选择该登录方式：

```bash
npx @openai/codex-security scan . --auth chatgpt

如需强制使用环境中的 API 密钥，请选择 API 密钥身份验证：

```bash
npx @openai/codex-security scan . --auth api-key

视您的账户和代码仓库而定，扫描整个代码仓库可能还需要
[Trusted Access for Cyber](https://chatgpt.com/cyber)。

## 准备扫描

请选择您信任并有权评估的代码仓库。扫描使用您
本地操作系统的权限，并且不会暂停等待审批。扫描
进程可能会继承您的环境，因此请在开始前
移除无关凭据。请参阅[本地扫描
权限](/zh-Hans/codex/security/cli/reference#local-scan-permissions)。

请选择代码仓库之外的目录保存扫描结果：

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

如果省略 `--output-dir`，Codex Security 会将结果保存在其专用的持久化
状态目录中。结果可能包含源代码摘录和漏洞详细信息，
因此请选择私有位置并采用适当的保留政策。

如果默认状态目录不可写，请选择所扫描代码仓库之外的可写目录：

```bash

开始扫描前，请检查代码仓库、目标和输出目录：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

试运行会检查本地输入，包括任何 `--knowledge-base` 路径，
但不会启动 Codex、加载凭据，也不会探测插件的 Python
解释器。

## 运行首次扫描

运行标准扫描，并将结果保存在所选目录中：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

交互式终端会显示实时扫描仪表板。添加 `--headless` 后，
将改为显示纯文本进度行。CI 和没有交互式会话的终端
会自动使用纯文本进度显示。

仪表板还会显示实时会话详情，其中可能包含源代码或凭据，因此请在分享前进行审查。

默认情况下，CLI 会将扫描进度和完成摘要写入 stderr，不会将完整扫描结果输出到 stdout。扫描完成后会输出类似以下内容的摘要：

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

相关信息可用时会显示 Token 用量和估算成本。如需以机器可读的 JSON 格式输出完整结果，请明确请求结构化输出：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

扫描默认仅生成报告，因此发现结果仍可供本地
审查。当您准备[在
CI 中运行扫描](/zh-Hans/codex/security/cli/ci)时，可以考虑设置严重性阈值。

## 选择模型和推理强度

扫描默认使用 `gpt-5.6-sol` 模型，推理强度为 `xhigh`。如果任务需要，请选择
其他模型和推理强度：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

支持的推理强度级别包括 `minimal`、`low`、`medium`、`high`、`xhigh`
和 `max`。

## 审查结果

打开 `report.md` 可查看便于阅读的结果。扫描目录还包含
供自动化使用的结构化文件：

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` 记录目标、范围、生成方和已封存的
  工件。
- `findings.json` 记录每项发现结果的严重性、置信度、位置、证据
  和修复措施。
- `coverage.json` 记录已审查区域、排除项、暂缓处理的工作、未决
  问题和覆盖完整性。

覆盖状态可以是 `complete`、`partial` 或 `unknown`。在将扫描视为审查证据之前，请查看所有暂缓审查的区域或
未决问题。
[CLI 参考资料](/zh-Hans/codex/security/cli/reference#scan-artifacts)介绍了
工件和输出的完整约定。

## 审查发现结果并修复问题

完成交互式扫描且有发现结果后，CLI 会提供发现结果浏览器。请审查相关证据，并选择需要修复的问题。您可以在 Codex 桌面应用中找到已保存的任务。

如需不使用浏览器修复高危和严重级别的问题：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

添加 `--create-pr` 以提交经过验证的补丁，并创建 GitHub Pull Request。

您还可以针对已保存的发现结果应用补丁，或导入 Linear 议题。请参阅
[`validate` 和 `patch` 参考资料](/zh-Hans/codex/security/cli/reference#codex-security-validate-and-codex-security-patch)。

## 选择后续扫描方式

当代码仓库包含独立的服务或软件包时，请使用路径扫描：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

审查基准修订版与 `HEAD` 之间已提交的更改：

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

以 `HEAD` 为基准，审查已暂存和未暂存的更改：

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

差异扫描和工作树扫描要求代码仓库参数为 Git 工作树根目录。开始差异扫描前，请先获取所选修订版。

当代码仓库或路径需要更广泛的审查时，请使用深度模式：

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

如需控制工作进程、子智能体和扫描停止时机：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

这些选项需要深度模式，该模式支持代码仓库和路径目标，
但不支持差异扫描或工作树扫描。此处，`--workers` 控制单次扫描中独立的
标准扫描工作进程；`bulk-scan --workers` 控制并发执行的
代码仓库扫描。`--max-time-hours` 接受不超过 `96` 的正数，
小时数可以包含小数。达到时限后，扫描会停止尚未完成的工作进程，
保留已完成的扫描结果，并将其汇总至最终报告中。

## 添加架构和安全上下文

提供架构文档、威胁模型或安全策略作为扫描上下文。这有助于 Codex Security 根据您的系统实际运行方式评估发现结果：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## 添加自定义扫描指令

添加指令，使扫描重点关注您的安全优先事项。使用第二个文件提供后续指令：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

扫描成功完成后，
或扫描覆盖不完整、出现错误后，后续指令都会在同一已通过身份验证的会话中运行。如果后续指令执行失败，CLI
会发出警告并保留已完成的扫描。扫描被取消
或达到成本上限后，后续指令不会运行。这两个选项也适用于
`bulk-scan`；CSV 中的 `prompt` 列可添加针对特定代码仓库的指令。

## 设置扫描预算

使用 `--max-cost` 可在估算的模型成本超过指定限额时停止扫描；该限额
以美元计：

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

正在处理的请求完成时，费用可能略微超过限额。
如果深度扫描在 Codex Security 汇总已完成工作进程的结果后达到限额，
CLI 会保存已完成的报告，将其覆盖状态标记为 `partial`，
并返回退出代码 `2`。如果扫描无法生成完整报告，
任何已有的部分输出都会保留在磁盘上。

## 在每次提交前扫描更改

为您的代码仓库安装 Git pre-commit 安全检查：

```bash
npx @openai/codex-security install-hook

此检查会在每次提交前扫描已暂存和未暂存的更改。
遇到高严重程度的发现项或扫描错误时，检查会阻止提交，
且不会替换现有的 pre-commit 脚本。

## 批量扫描代码仓库

发现代码仓库前，请先登录 GitHub：

```bash
gh auth login

从您的 GitHub 账户或组织中发现并选择代码仓库：

```bash
npx @openai/codex-security bulk-scan

交互式流程会排除已归档的代码仓库和派生仓库。
扫描前，系统会要求您确认所选代码仓库。

要扫描已准备好的代码仓库列表，请提供 CSV 文件和输出目录：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

再次运行相同命令即可恢复已有的批量扫描。Codex Security
会跳过已完成扫描的代码仓库。添加 `--max-attempts 3` 可在
代码仓库或扫描出现临时错误时重试。

如需了解 GitHub 代码仓库发现、CSV 准备、扫描活动结果以及 Docker 设置，请参阅
[运行批量安全扫描](/zh-Hans/codex/security/cli/bulk-scans)。

## 在 Docker 中运行批量扫描

如果您有权访问 Codex Security Docker 镜像，请在 Linux Docker 主机上使用随附的
安全加固版 Compose 配置和安全配置方案。
该主机必须支持创建非特权用户命名空间。请提供代码仓库
CSV 文件，将结果和登录状态保存在持久挂载的目录中，并
通过您的环境或密钥管理器提供凭据：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

容器运行批量扫描时不会显示交互式提示。如果您想以交互方式发现代码仓库，请在
Docker 外部使用 CLI。对于私有
代码仓库，请提供 `GH_TOKEN` 或 `GITHUB_TOKEN`，可通过您的环境或
密钥管理器传入。[登录要求](#sign-in)（包括账户和
代码仓库访问权限）也适用于容器化扫描。

## 重新查看已保存的扫描

列出您的代码仓库已保存的扫描：

```bash
npx @openai/codex-security scans list "$REPOSITORY"

从结果中复制扫描 ID，以查看对应的发现项和配置：

```bash
npx @openai/codex-security scans show SCAN_ID

查看扫描及其工作进程已保存的事件：

```bash
npx @openai/codex-security scans logs SCAN_ID

已保存的日志未经脱敏，可能包含源代码或凭据。
分享前请先审查。

列出代码仓库各次扫描中尚未关闭的发现项：

```bash
npx @openai/codex-security findings list "$REPOSITORY"

如果最新扫描未确认先前的发现项，该发现项仍会保持未关闭状态。

要将已审查的发现项标记为误报，
请说明该发现项为何不适用：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

后续扫描会参考这一说明，但仍会重新检查当前代码。

使用原始配置，针对当前检出的代码运行相同的扫描：

```bash
npx @openai/codex-security scans rerun SCAN_ID

比较两次扫描，找出新增、持续存在、重新打开、已解决或状态未知的
发现项：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比较时会根据根本原因自动匹配发现项，
并复用已保存的匹配结果。

如需了解批量扫描的 CSV 格式、扫描历史记录筛选条件和命令选项，请参阅
[CLI 参考资料](/zh-Hans/codex/security/cli/reference)。

根据您的目标，继续执行相应的工作流程：

- [运行批量安全扫描](/zh-Hans/codex/security/cli/bulk-scans)，以发现 GitHub
  代码仓库或扫描固定的 CSV 清单。
- [阅读 CLI 常见问题](/zh-Hans/codex/security/cli/faq)，了解扫描历史记录、
  误报反馈、覆盖范围和修复验证的相关解答。
- [在 CI 中运行扫描](/zh-Hans/codex/security/cli/ci)，以审查 Pull Request、保留
  结果并设置严重程度策略。
- [查阅 CLI 参考资料](/zh-Hans/codex/security/cli/reference)，了解所有标志、
  输出格式、产物和退出代码。
- [集成 TypeScript SDK](/zh-Hans/codex/security/sdk)，以便通过
  应用程序或开发者工具运行扫描。
