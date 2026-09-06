<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli/bulk-scans -->

使用 `npx @openai/codex-security bulk-scan` 在一次
扫描活动中审查代码仓库。您可以从个人 GitHub 账户或
组织中发现代码仓库，也可以提供 CSV，将每个代码仓库固定到确切的 Git
修订版本。

  `@openai/codex-security` 软件包已公开。运行扫描需要 Codex Security 访问权限。
  请按照 [CLI 快速入门](/zh-Hans/codex/security/cli) 安装
  CLI 并登录。

## 选择代码仓库来源

| 来源           | 适用场景                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| GitHub 代码仓库发现 | 从您的个人 GitHub 账户或某个组织中以交互方式选择代码仓库。 |
| CSV 清单    | 针对代码仓库的确切修订版本运行可重复执行的自动化扫描活动。                |

两种工作流都会保存进度、保留各代码仓库的结果，并允许您
在中断后恢复扫描活动。

## 发现 GitHub 代码仓库

使用 GitHub CLI 登录：

```bash
gh auth login

启动交互式批量扫描：

```bash
npx @openai/codex-security bulk-scan

CLI 会引导您完成以下步骤：

1. 选择您的个人 GitHub 账户或某个组织。
2. 审查过去 90 天内活跃的代码仓库。
3. 搜索代码仓库列表，然后选择要扫描的代码仓库。
4. 选择用于保存扫描结果的目录。
5. 审查所选代码仓库并确认扫描活动。

发现过程会排除已归档的代码仓库和派生代码仓库。CLI 会记录每个所选代码仓库的
确切默认分支提交，并将其写入
`<output-directory>/repositories.csv`。在您确认
所选内容之前，不会开始任何扫描。

要使用 GitHub Enterprise Server，请先登录您的 GitHub 主机：

```bash
gh auth login --hostname github.example.com

开始发现代码仓库时，请设置 `GH_HOST`：

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

交互式发现需要终端。对于 CI、容器或预先准备的
代码仓库列表，请改用 CSV 清单。

## 创建代码仓库 CSV

创建一个 CSV，其中每个代码仓库及其固定修订版本占一行：

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

CSV 支持以下列：

| 列       | 必填 | 说明                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | 是      | 代码仓库的唯一标识符。请使用字母、数字、句点、连字符或下划线。                      |
| `repository` | 是      | HTTPS URL、SSH URL 或本地代码仓库路径。相对路径以 CSV 文件所在目录为基准解析。               |
| `revision`   | 是      | 包含 40 或 64 个字符的完整 Git 提交 SHA。不支持分支名称、标签和缩短的提交哈希。 |
| `scope`      | 否       | 相对于代码仓库的待扫描目录。省略此值则扫描整个代码仓库。                       |
| `mode`       | 否       | `standard` 或 `deep`。省略此值则使用命令选择的模式。                                   |
| `prompt`     | 否       | 此代码仓库专用的扫描指令。                                                             |

要查找本地代码仓库的完整提交 SHA，请运行：

```bash
git -C /path/to/repository rev-parse HEAD

## 根据 CSV 运行扫描活动

传入 CSV 以及一个位于代码仓库之外的私有输出目录：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` 控制代码仓库扫描的并发数，默认值为 `4`。它
不会设置每次深度扫描中独立的标准扫描工作进程数量；
请通过
[`[deep_scan]`](/zh-Hans/codex/security/cli/reference#configure-deep-scans) 配置这些限制。使用 `--mode
deep` 可为未自行指定 `mode` 的行选择深度扫描。CSV 中的每一行
仍可自行选择扫描模式和代码仓库范围。

设置 `[deep_scan].max_time_hours`，以限制扫描活动中每次深度扫描的
工作进程执行。`--max-time-hours` 标志适用于 `scan`，不适用于 `bulk-scan`。

CLI 会签出每个固定的修订版本，扫描所选目标并记录结果，
然后删除临时签出的代码仓库。只有当扫描覆盖范围完整，
并且所有必需的结果制品均存在时，
该代码仓库才算完成。

## 共享安全上下文和指令

如需为每次扫描添加架构文档、威胁模型或安全策略，请
使用 `--knowledge-base`。如需添加更多文件或目录，请重复指定该标志：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

若要添加共享扫描指令，或在每次扫描后运行后续指令，
请提供提示文件：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

CLI 会将每个代码仓库在 CSV 中的 `prompt` 追加到共享扫描
指令之后。扫描成功、覆盖范围不完整或发生错误后，后续指令
都会在同一个已通过身份验证的会话中运行；但扫描被取消
或达到费用上限时，不会运行后续指令。提示文件路径
以您的当前目录为基准解析。

## 选择模型和推理强度

批量扫描默认使用 `gpt-5.6-sol`，推理强度为 `xhigh`。如需
为 CSV 扫描活动选择其他模型和推理强度：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

这些选项同样适用于交互式代码仓库发现：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

支持的推理强度级别为 `minimal`、`low`、`medium`、`high` 和 `xhigh`。

要使用 OpenRouter 或 Fireworks，请分别设置 `OPENROUTER_API_KEY` 或 `FIREWORKS_API_KEY`，
并指定 `--provider` 和 `--model`。有关凭据和
示例，请参阅 [OpenRouter 或 Fireworks
设置](/zh-Hans/codex/security/cli/reference#use-openrouter-or-fireworks) 或 [Amazon Bedrock
设置](/zh-Hans/codex/security/cli/reference#use-amazon-bedrock)。

## 审查扫描活动结果

输出目录包含已固定的扫描活动、仅追加的结果
台账，以及每个代码仓库和每次尝试各自的制品：

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` 会记录扫描活动中的代码仓库、固定修订版本、范围、扫描
  模式，以及共享或代码仓库专用的指令。
- `results.jsonl` 会记录每次代码仓库扫描尝试、其状态、制品
  目录，以及任何可用的费用或错误详情。
- `report.md` 会为一次代码仓库扫描尝试提供易读报告。
- `findings.json` 和 `coverage.json` 会记录该次尝试的发现结果和
  已审查范围。

如需可移植的扫描结果，请导出一次已完成的代码仓库扫描：

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

结果可能包含源代码摘录和漏洞详情。请确保输出目录保持私有、位于所扫描的代码仓库之外，并遵循适当的保留政策。

## 恢复扫描活动

使用相同的 CSV 和输出目录运行原始命令：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CLI 会恢复未完成的代码仓库扫描，并跳过已完成的扫描。
覆盖范围不完整的扫描不会重试，其结果仍然可用，
命令将以退出代码 `2` 结束。

对于现有输出目录，请勿更改代码仓库清单、扫描指令或后续指令。CLI 会检查已固定的清单，并拒绝其他扫描活动。如果更改了代码仓库、修订版本、范围、扫描模式、共享指令或代码仓库专用指令，请使用新的输出目录。

## 重试出错的代码仓库

使用 `--max-attempts`，在代码仓库发生暂时性的检出或扫描
错误后重试：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

默认情况下，每个代码仓库仅尝试一次。每次尝试都有独立的回执和工件目录。可重试的情况包括检出错误、扫描失败和缺少必需的工件。已完成但覆盖范围不完整的扫描不会重试。

批量扫描使用以下退出代码：

| 退出代码 | 含义                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | 所有代码仓库均已成功完成扫描。                                                                              |
| `2`       | 某个代码仓库未能完成扫描、某次扫描覆盖范围不完整，或命令遇到输入错误或运行时错误。 |
| `130`     | Ctrl-C 中断了扫描活动。                                                                                      |
| `143`     | SIGTERM 终止了扫描活动。                                                                                      |

## 在 Docker 中运行批量扫描

[Codex Security
代码仓库](https://github.com/openai/codex-security)包含经过安全加固的
Compose 配置，可在 Linux Docker 主机上自动执行 CSV 扫描活动。
该主机必须支持非特权用户创建用户命名空间。

请将代码仓库 CSV、扫描结果和登录状态挂载到持久化目录中。
通过环境或密钥管理器提供 OpenAI 凭据。
私有 GitHub 代码仓库所需的 `GH_TOKEN` 或 `GITHUB_TOKEN`
也应通过相同方式提供。

使用已挂载的 CSV 和输出目录运行镜像：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

使用相同的已挂载 CSV 和输出目录恢复扫描活动。对于
GitHub Enterprise Server，请将 `CODEX_SECURITY_GIT_HOST` 设置为您的 GitHub 主机。

有关所有可用标志，请参阅 [bulk-scan
命令参考资料](/zh-Hans/codex/security/cli/reference#codex-security-bulk-scan)。
有关扫描覆盖范围和发现结果的常见问题，请参阅 [CLI
常见问题](/zh-Hans/codex/security/cli/faq)。
