<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli/reference -->

使用本参考资料查看支持的 `codex-security` 命令、标志、
输出格式和退出行为。如需按照指导进行首次扫描，请先阅读
[CLI 快速入门](/zh-Hans/codex/security/cli)。

  `@openai/codex-security` 软件包已公开。运行扫描需要 Codex
  Security 访问权限。扫描会使用您的本地权限，且不会暂停等待
  审批。开始之前，请查看[本地扫描
  权限](#local-scan-permissions)。

使用 `npx @openai/codex-security` 运行 CLI。

## 命令概览

```text
usage: codex-security [--version] <command> [options]

CLI 提供以下命令：

| 命令                       | 用途                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | 运行 Codex Security 扫描。                            |
| `codex-security install-hook` | 安装 Git 提交前安全扫描。               |
| `codex-security bulk-scan`    | 发现代码仓库并运行可恢复的批量扫描。   |
| `codex-security scans`        | 列出、检查、比较和获取已保存的扫描日志。 |
| `codex-security findings`     | 审查并更新已保存的安全发现。            |
| `codex-security export`       | 将已完成的发现导出为 CSV、JSON 或 SARIF。     |
| `codex-security publish`      | 将已完成扫描的发现发布到 Linear。            |
| `codex-security validate`     | 检查一个或多个候选安全发现。        |
| `codex-security patch`        | 修补一个或多个安全问题。                    |
| `codex-security login`        | 登录、存储凭据或检查登录状态。  |
| `codex-security logout`       | 移除已存储的登录信息。                            |
| `codex-security info`         | 显示 SDK 和捆绑插件的只读元数据。       |

CLI 还提供以下集成命令：

| 命令                      | 用途                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | 生成 Shell 补全脚本。    |
| `codex-security mcp`         | 将 CLI 注册为 MCP 服务器。    |
| `codex-security skills`      | 将 Codex Security 技能同步到智能体。 |

列出所有可用命令：

```bash
npx @openai/codex-security --help

在命令中添加 `--help`，以查看其参数和选项：

```bash
npx @openai/codex-security scan --help

`codex-security --version` 会输出已安装的版本并退出。
`codex-security info --json` 会报告 SDK 和捆绑插件的版本。
这两个命令均不需要 Python。

### 发现命令并连接智能体

输出智能体可读取的命令清单：

```bash
npx @openai/codex-security --llms

以 JSON 格式查看扫描参数模式：

```bash
npx @openai/codex-security scan --schema --format json

为 Bash 生成 Shell 补全：

```bash
npx @openai/codex-security completions bash

对于相应的 Shell，请将 `bash` 替换为 `zsh` 或 `fish`。

扫描结果支持 `--format toon|json|yaml|jsonl` 和 `--full-output`。这里的
框架级 `--format` 与 `--export-format` 不同，后者用于选择
从已完成扫描中导出的工件格式。全局命令帮助
还会列出 `md`，但扫描结果不支持 Markdown 输出。

将 CLI 注册为 MCP 服务器：

```bash
npx @openai/codex-security mcp add

将 Codex Security 技能同步到您的智能体：

```bash
npx @openai/codex-security skills add

MCP 仅提供只读的 `info` 元数据命令。扫描、导出、
身份验证、验证和修补仍只能通过 CLI 执行。

## `codex-security scan`

对代码仓库、所选路径、已提交的更改或
工作树进行扫描。

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

`repository` 默认为当前目录。

### 选择扫描身份验证方式

使用默认选项 `--auth auto` 可自动选择凭据。当同时具备
ChatGPT 登录状态以及 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 时，
采用文本输出的交互式扫描会询问要使用哪种凭据。CI 扫描、JSON 和
JSONL 扫描，以及其他没有交互式终端的扫描会使用
环境 API 密钥。试运行不会发出提示，也不会加载凭据。

若要使用您已存储的凭据，请传入 `--auth chatgpt`：

```bash
npx @openai/codex-security scan . --auth chatgpt

若要使用环境 API 密钥，请传入 `--auth api-key`：

```bash
npx @openai/codex-security scan . --auth api-key

若要默认自动使用已存储的凭据，请运行
`unset OPENAI_API_KEY CODEX_API_KEY`。

### 使用 OpenRouter 或 Fireworks

要选择 OpenRouter，请提供其 API 密钥并明确指定模型：

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

要选择 Fireworks，请提供其 API 密钥并明确指定模型：

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

这两个提供商也都支持 `bulk-scan`。

### 使用 Amazon Bedrock

使用 `--provider amazon-bedrock` 选择 Amazon Bedrock，并通过
`--model` 明确指定 Bedrock 模型：

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

设置 `AWS_REGION`，并使用 `AWS_BEARER_TOKEN_BEDROCK`、标准 AWS
访问密钥、AWS 配置方案、Web 身份、容器凭据或
默认 AWS 凭据链进行身份验证。Bedrock 扫描使用 AWS 凭据，而不使用
`--auth`、ChatGPT 登录信息或 OpenAI API 密钥。`scan` 和 `bulk-scan`
均支持 `--provider`。

### 选择扫描目标

请为每次扫描选择一种目标类型。

| 参数                 | 说明                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | 扫描相对于代码仓库的路径。如需扫描更多路径，请重复使用该标志。         |
| `--diff BASE`            | 扫描从 `BASE` 到 `--head` 的已提交更改。头部修订版本默认为 `HEAD`。    |
| `--head HEAD`            | 设置 `--diff` 的头部修订版本。                                             |
| `--working-tree`         | 以 `--base` 为基准，扫描已暂存和未暂存的更改。基准修订版本默认为 `HEAD`。 |
| `--base BASE`            | 设置 `--working-tree` 的基准修订版本。                                     |
| `--mode {standard,deep}` | 选择扫描模式。默认值为 `standard`。                                |

`--path`、`--diff` 和 `--working-tree` 互斥。`--head`
需要与 `--diff` 一起使用，`--base` 需要与 `--working-tree` 一起使用。深度模式支持
以代码仓库或路径作为扫描目标。

差异扫描和工作树扫描要求代码仓库参数为 Git 工作树的根目录。所选引用必须存在于该检出副本中。

扫描整个代码仓库：

```bash
npx @openai/codex-security scan .

扫描所选路径：

```bash
npx @openai/codex-security scan . --path src --path tests

扫描已提交的更改：

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

扫描已暂存和未暂存的更改：

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

对代码仓库进行更深入的审查：

```bash
npx @openai/codex-security scan . --mode deep

### 配置深度扫描

将以下选项与 `--mode deep` 配合使用，以控制工作进程并发数和运行时间：

| 参数                 | 说明                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | 并发运行的独立标准扫描工作进程数量上限。默认值为 `4`。                |
| `--subagents N`          | 每个工作进程可用的子智能体数量。默认值为 `3`。                                   |
| `--stop-after-no-new N`  | 连续 `N` 次已完成的工作进程扫描均未发现新问题时停止。默认值为 `4`。 |
| `--max-discovery-runs N` | 独立标准扫描的总运行次数上限。默认值为 `40`。                       |
| `--max-time-hours HOURS` | 工作进程执行时间上限，以小时为单位。默认值为 `96`；支持小数。             |

`--subagents` 接受零或正整数。`--max-time-hours` 接受
不大于 `96` 的正数。其余选项要求提供
正整数。这些选项不适用于标准扫描。

例如，使用两个工作进程，最多运行十次，并在 1.5 小时后停止工作进程运行：

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

达到时间限制后，扫描会停止尚未完成的工作进程，保留已完成的
扫描结果，并将其汇总至最终报告。如果没有工作进程完成
源代码审查，扫描会记录部分覆盖，并返回退出码 `2`。

在 `~/.codex/codex-security/config.toml` 中设置持久默认值；或者在
`$CODEX_HOME/codex-security/config.toml` 中设置，前提是已设置 `CODEX_HOME`：

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

命令行选项会覆盖这些默认值。`scan --workers` 控制
单次深度扫描中的独立标准扫描工作进程；`bulk-scan --workers`
控制代码仓库的并发扫描。只能在 TOML 文件中设置 `stop_after_consecutive_errors`；
其默认值为 `3`。

### 添加安全上下文

使用 `--knowledge-base PATH` 提供架构文档、威胁模型
或安全策略。可重复使用该选项，以提供更多文件或目录：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

支持的文档包括 `.md`、`.markdown`、`.txt`、`.pdf` 和 `.docx`
文件。CLI 会递归搜索目录，拒绝符号链接形式的输入路径，
跳过符号链接目录项，并且不会将提取的文档内容
写入已保存的扫描结果。

### 添加扫描指令

要添加扫描指令，请通过
`--scan-prompt-file` 提供文本或 Markdown 文件。使用 `--post-scan-prompt-file`，可在扫描成功、
扫描覆盖范围不完整或出现错误后，在同一已通过身份验证的会话中
运行后续指令：

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

例如，使用扫描提示来重点关注授权边界，并要求
后续指令在扫描目录中写入新的 `post-scan-summary.md`。
如果后续指令执行失败，CLI 会发出警告并保留已完成的扫描。
扫描取消后或达到成本
限制时，不会执行后续指令。

### 设置输出和策略选项

使用这些选项可保留扫描工件、保存先前结果或生成机器可读的结果。

| 参数                   | 说明                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | 将扫描工件写入所在 Git 工作树之外的私有目录。默认写入 Codex Security 的持久状态目录。 |
| `--archive-existing`       | 将现有结果移至 `DIR.previous-<timestamp>-<id>`，并从空的输出目录开始。需要 `--output-dir`。  |
| `--fail-on-severity LEVEL` | 如果已完成的扫描报告了严重性达到或超过 `critical`、`high`、`medium` 或 `low` 的发现项，则返回退出码 `1`。                  |
| `--patch`                  | 在完成扫描后修复并验证所选发现项。                                                                      |
| `--patch-severity LEVEL`   | 修复严重性达到或超过 `critical`、`high`、`medium` 或 `low` 的发现项。默认值为 `low`。                                        |
| `--create-pr`              | 提交已验证的补丁文件，并创建 GitHub Pull Request。需要 `--patch`。                                              |
| `--max-cost USD`           | 当预估模型成本超过指定的美元金额时停止扫描。                                                  |
| `--dry-run`                | 在不启动扫描的情况下，检查代码仓库、目标、知识库、输出目录和 Codex 配置。             |
| `--headless`               | 显示纯文本进度，而不显示交互式扫描仪表板。                                                          |
| `--verbose`                | 将经过脱敏处理的生命周期、身份验证、进度和成本诊断信息输出到 stderr。                                          |
| `--json`                   | 将清单、发现项、覆盖范围、路径和轮次元数据作为单个 JSON 文档输出。                                           |
| `--format FORMAT`          | 以 `toon`、`json`、`yaml` 或 `jsonl` 格式输出完整扫描结果。                                                        |
| `--full-output`            | 使用默认的结构化输出格式打印完整结果。                                                        |

成本限制只是估算值，并非硬性支出上限。正在处理的
请求完成时可能会略微超出限制。如果深度扫描在
Codex Security 汇总已完成工作进程的结果后达到限制，CLI 会封存
可用结果，将覆盖范围标记为 `partial`，并返回退出码 `2`。
否则，会返回 `2`，并将所有可用的部分输出保留在磁盘上。

省略 `--output-dir` 时，结果会持久保存在
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>` 下。`CODEX_HOME`
的默认值为 `~/.codex`。设置 `CODEX_SECURITY_STATE_DIR` 后，结果会改为保存在
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` 下。这些目录可能
包含源代码摘录和漏洞详情，因此请妥善管理其权限
和保留期限。

工作台将扫描历史记录保存在
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3` 中。设置
`CODEX_SECURITY_STATE_DIR` 也会迁移工作台数据库。

输出目录必须位于扫描目录以及包含该目录的任何
Git 工作树之外。扫描时可使用
`--archive-existing` 替换现有结果目录。

要在重复使用输出目录之前保留先前结果：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

扫描默认仅生成报告。添加 `--fail-on-severity`，以在 CI 中评估
严重性策略：

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

试运行会检查包括知识库文档在内的本地输入，但不会加载凭据、启动 Codex，也不会探测插件的 Python 解释器：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### 配置运行时

如需明确指定模型、解释器、插件或 Codex 配置值，请使用运行时选项。

| 参数                                                  | 说明                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | 选择扫描凭据。默认值为 `auto`。                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | 选择推理服务提供商。默认值为 `openai`。                                                  |
| `--model MODEL`                                           | 选择模型。默认值为 `gpt-5.6-sol`。使用 OpenRouter、Fireworks 或 Amazon Bedrock 时必须指定。  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | 选择模型的推理强度。默认值为 `xhigh`。                                             |
| `--plugin-path PATH`                                      | 使用 Codex Security 插件目录或 ZIP 文件覆盖随附插件。                             |
| `--python PATH`                                           | 选择插件运行时使用的 Python 解释器。                                                    |
| `--codex KEY=VALUE`                                       | 覆盖隔离式 Codex 配置中的一个值。值采用 TOML 语法。可重复使用该标志以设置更多值。 |

要在不编写 TOML 的情况下选择其他模型和推理强度：

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

为通过 `--codex` 传递的字符串值加上引号，确保 TOML 解析器接收到
字符串：

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

为当前代码仓库安装 Git pre-commit 安全检查：

```bash
npx @openai/codex-security install-hook

该检查会在每次提交前扫描已暂存和未暂存的更改，并在发现
高严重性发现项或发生扫描错误时阻止提交。它遵循 `core.hooksPath` 设置，并且
不会替换现有的 pre-commit 脚本。您也可以
根据需要设置其他严重性阈值：

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

发现并扫描 GitHub 代码仓库，或根据代码仓库 CSV 文件运行
可恢复的扫描：

有关 GitHub 代码仓库发现、CSV 清单、扫描活动结果
和容器化扫描的完整指南，请参阅[运行批量安全
扫描](/zh-Hans/codex/security/cli/bulk-scans)。

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

不带参数运行 `npx @openai/codex-security bulk-scan`，即可交互式选择
代码仓库。此流程需要登录 GitHub CLI。

如需在交互式发现过程中选择模型和推理强度：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

对于预先准备好的代码仓库列表，请提供 CSV 文件和 `--output-dir`：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CSV 必须包含 `id`、`repository` 和 `revision` 列。修订版本必须是
完整的提交哈希值。可选的 `scope`、`mode` 和 `prompt` 列用于配置
各个代码仓库：

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

使用 `--knowledge-base PATH` 在所有
代码仓库之间共享安全文档。使用 `--scan-prompt-file FILE` 添加共享扫描指令；
CSV 的 `prompt` 列会在共享提示
之后添加代码仓库专用指令。`--post-scan-prompt-file FILE` 会在每次扫描
后执行后续指令，包括覆盖不完整或出现错误的扫描。扫描取消
或达到费用上限时，不会执行后续指令。

`--workers` 限制同时运行的代码仓库扫描数量，默认值为 `4`。`--mode`
的默认值为 `standard`，`--max-attempts` 的默认值为 `1`。设置
`--max-attempts` 可在代码仓库或扫描出错时重试。已经完成但
覆盖不完整的扫描不会重试。其结果仍然可用，并且
命令会返回退出代码 `2`。

再次运行相同的命令，即可从现有输出目录继续执行。CLI
会跳过已完成的扫描，包括覆盖不完整的扫描。

如需开展容器化扫描活动，请参阅[在
Docker 中运行批量扫描](/zh-Hans/codex/security/cli/bulk-scans#run-bulk-scans-in-docker)。

## `codex-security scans`

### 查找已保存的扫描

列出当前目录中已保存的扫描：

```bash
npx @openai/codex-security scans

列出其他代码仓库的扫描：

```bash
npx @openai/codex-security scans list /path/to/repository

查找存储在特定输出目录下的扫描：

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### 检查或重新运行扫描

显示已保存扫描的结果和配置：

```bash
npx @openai/codex-security scans show SCAN_ID

添加 `--show-linked-findings`，以包含之前扫描中发现项的链接。

使用原始配置，针对当前检出目录重新运行扫描：

```bash
npx @openai/codex-security scans rerun SCAN_ID

重新运行扫描时，必须使用原始扫描所记录的插件版本。如果
已安装的版本不同，命令将停止，而不会使用
不同版本的插件运行。

### 查看已保存的扫描日志

读取扫描及其工作进程已保存的完整会话事件。这些日志
未经脱敏，可能包含源代码或凭据，因此请在
共享前审查：

```bash
npx @openai/codex-security scans logs SCAN_ID

添加 `--json`，以适合机器处理的格式获取完整结果。

### 匹配并比较发现项

比较两次扫描，以找出新增、持续存在、重新打开、已解决及状态未知的
发现项：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比较时会自动匹配根本原因相同的发现项，
并复用已保存的匹配结果。如需显式保存匹配结果，请使用 `scans match`：

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

如果后一次扫描覆盖不完整，或未
覆盖发现项的原始位置，则该发现项的状态为未知。将 `--force` 添加到 `match`，即可在需要时
重新计算现有匹配结果。

如需匹配当前代码仓库所有已完成的扫描，包括来自
其他检出目录的扫描：

```bash
npx @openai/codex-security scans match --all

即使使用相同配置重新运行，扫描结果也可能不同。匹配和
比较用于跟踪变化，不能保证结果具有确定性，也不能证明
漏洞已不存在。请使用 `validate`，对照当前代码重新检查对安全至关重要的
发现项。

## `codex-security findings`

列出当前代码仓库各次扫描中未解决的发现项：

```bash
npx @openai/codex-security findings list

传入代码仓库路径，以检查另一个检出目录：

```bash
npx @openai/codex-security findings list /path/to/repository

添加 `--json` 可获得结构化输出。列表会标识在
最新扫描中出现的发现项，以及该次扫描未确认的先前发现项。

请注意，先前的发现项在解决或忽略前始终保持未解决状态（未在最新扫描中
出现，并不能证明相应问题已修复）。

将经审查的发现项记录为误报：

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

检查已保存的扫描，以确定发现项的具体出现记录：

```bash
npx @openai/codex-security scans show SCAN_ID

记录判定为误报的具体原因：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

原因不能为空。Codex Security 会为该
代码仓库保存这项判定，并将其作为上下文提供给后续扫描。每次扫描都会独立
重新检查当前源代码、控制措施和可达性。此前的判定
不会屏蔽规则、路径或漏洞类别。

## `codex-security export`

从已完成且已封存的扫描中导出 CSV、JSON 或 SARIF。导出操作会在写入输出前验证
扫描工件，并且不会改动 Codex 运行时和
凭据。

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` 是已完成扫描的目录。

| 参数                           | 说明                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | 选择导出格式。默认值为 `sarif`。                                           |
| `--output FILE\|-`                 | 将所选格式写入文件或 stdout。默认写入当前目录中的文件。 |
| `--source-root PATH`               | 使用代码仓库的检出目录向 SARIF 添加源代码行指纹。                          |
| `--python PATH`                    | 为随附的导出器选择 Python 解释器。                                     |

`--source-root` 仅可与 `--export-format sarif` 配合使用。JSON 会保留
已封存的发现项文档。CSV 包含可移植的发现项列，但
不包含本地工作台的研判状态。

未指定 `--output` 时，CLI 会在当前工作目录中将 SARIF 写入 `results.sarif`，将 JSON 写入
`findings.json`，并将 CSV 写入 `findings.csv`。
导出内容可能包含源代码摘录和漏洞详情。请在代码仓库
之外运行该命令，或使用 `--output` 指定已扫描
检出目录之外的私有路径。

将 SARIF 写入文件：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

将 SARIF 写入 stdout：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

将发现项导出为 JSON：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

将发现项导出为 CSV：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

将已完成扫描中的每个发现项发布到 Linear：

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` 必须包含已完成且已封存的扫描。在交互式
终端中省略此参数，即可从本地扫描历史记录中选择已完成的扫描。创建议题
还要求相应扫描及其发现项存在于本地扫描历史记录中。
试运行会验证已封存的工件，但不会执行此项持久化检查。

| 参数                             | 说明                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | 发布到 Linear。此参数为必填项。                                                                                                                    |
| `--linear-team TEAM_ID`              | 选择 Linear 团队。省略此参数时使用 `CODEX_SECURITY_LINEAR_TEAM`；两者至少需设置一项。                                                                 |
| `--project PROJECT_ID`               | 选择 Linear 项目。省略此参数时使用 `CODEX_SECURITY_LINEAR_PROJECT`。如果两者均未设置，议题将直接在团队中创建。                          |
| `--linear-api-key KEY`               | 使用 Linear 个人 API 密钥直接发布。省略此参数时使用 `CODEX_SECURITY_LINEAR_API_KEY`。                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | 根据电子邮件地址或 Linear 用户 ID 分配已创建的议题。需要提供 `--linear-api-key` 或 `CODEX_SECURITY_LINEAR_API_KEY`。省略此参数时，议题将保持未分配状态。 |
| `--dry-run`                          | 准备议题载荷，不启动 Codex、不连接 Linear、不创建议题，也不写入发布状态。                                                 |
| `--json`                             | 将结构化发布结果写入 stdout。进度信息仍输出到 stderr。                                                                                      |

  Linear 议题描述和试运行输出可能包含源代码片段
及漏洞详情。请仅向经授权的 Linear 团队或
项目发布，并将保存的输出视为敏感信息。

每次非试运行调用都会尝试为每个发现项创建一个新议题。
再次发布同一次扫描时，不会匹配、更新或复用现有议题。
如果某些发现项发布失败，命令会保留已成功创建的议题，并
返回退出代码 `2`。
使用 `--json` 时，请在重试前审查 `created` 和 `failed` 结果，
以避免创建重复议题。

发布前预览议题载荷：

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### 使用已连接的 Linear 应用发布

如果未提供 Linear API 密钥，该命令会使用您现有的配置和已连接的
Linear 应用启动 Codex。发布前，请先登录并将 Linear 连接到您的
Codex 账户：

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### 使用 Linear API 密钥发布

提供 `--linear-api-key` 或 `CODEX_SECURITY_LINEAR_API_KEY` 后，即可直接通过 Linear API
发布，并且不会启动 Codex。直接发布时，
除非您选择负责人，否则议题将保持未分配状态：

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

命令行参数的值会覆盖对应的环境变量。对于 API
密钥，建议优先使用 `CODEX_SECURITY_LINEAR_API_KEY`，而不是 `--linear-api-key`，因为
命令行参数可能出现在 shell 历史记录和进程列表中。

## `codex-security validate` 和 `codex-security patch`

检查候选发现项是否有效：

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

使用随附的修复技能生成修复方案：

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

每个位置参数都接受文本字面量或文件路径。这些输入以
当前目录为基准。修复完成后，或后续扫描不再报告某个发现项时，请使用 `validate`
重新检查该发现项。仅比较扫描结果无法证明修复
已生效。

使用 `--effort` 为任一命令选择推理强度：

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### 扫描后修复发现项

使用 `scan --patch` 在完整扫描后修复发现项。这需要
`@openai/codex-security` 0.1.15 或更高版本。默认严重程度阈值为
`low`。以下命令选择高危和严重级别的发现项：

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

已验证的发现项与已修复的发现项均不会触发 `--fail-on-severity`。

### 修复已保存的发现项

传入发现项 ID 或发现实例 ID，对其原始代码仓库应用修复；或者从已保存的扫描中
选择发现项：

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` 会选择当前代码仓库最近一次完成的扫描。
处理已保存发现项的命令支持 `--json`；文本字面量和文件输入则不支持。

添加 `--create-pr`，以仅提交经过验证的补丁文件，并通过
GitHub CLI 创建 Pull Request：

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

如果推送或 Pull Request 创建失败，请在同一代码仓库中运行输出的 `patch --resume-pr BRANCH`
命令以重试。

### 修复 Linear 议题

设置 `CODEX_SECURITY_LINEAR_API_KEY` 或 `LINEAR_API_KEY` 以提供个人 API 密钥，
或设置 `LINEAR_ACCESS_TOKEN` 以提供 OAuth Token。建议优先使用环境变量，而不是
`--linear-api-key KEY`，以免密钥出现在 shell 历史记录中。

通过 ID 或 URL 导入议题。重复使用 `--linear-issue` 可选择多个
议题：

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

使用 `--linear-project` 选择某个项目中未解决的议题。添加 `--linear-filter`
可缩小选择范围：

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

除非筛选条件设置了 `state`，否则 CLI 会排除已完成和已取消的议题。
它不会修改 Linear 议题。

## `codex-security login`、`logout` 和 `info`

以交互方式登录：

```bash
npx @openai/codex-security login

在远程或无图形界面的计算机上使用设备身份验证：

```bash
npx @openai/codex-security login --device-auth

检查当前登录状态：

```bash
npx @openai/codex-security login status

移除已保存的登录信息：

```bash
npx @openai/codex-security logout

通过 stdin 传入 API 密钥并保存：

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

保存企业访问 Token：

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

查看 SDK 和随附插件的只读元数据：

```bash
npx @openai/codex-security info --json

当您将 CLI 作为 MCP 服务器提供时，`info` 是唯一可用的命令。
扫描、导出、发布、登录、验证和修复仍只能通过 CLI 执行。

## 读取扫描输出

默认情况下，扫描会将进度、完成摘要和错误发送到 stderr，
而不会将完整扫描结果写入 stdout。使用 `--json`、
`--format` 或 `--full-output`，可将结构化扫描结果发送到 stdout。

交互式终端会显示实时仪表板，列出当前扫描阶段、
已审查文件、活动、Token 使用量和预估费用。CI 和重定向输出
使用纯文本进度。添加 `--headless` 后，可在
交互式终端中使用纯文本进度：

```bash
npx @openai/codex-security scan . --headless

仪表板还会显示实时会话详情。这些信息未经脱敏，可能包含源代码或
凭据。分享前请先审查。

### 详细诊断信息

添加 `--verbose`，将经过脱敏处理的生命周期、身份验证、进度和费用
诊断信息输出到 stderr：

```bash
npx @openai/codex-security scan . --verbose

设置 `CODEX_SECURITY_LOG_LEVEL=debug` 后，无需使用该
标志即可启用相同的诊断功能。`LOG_LEVEL=debug` 也可启用诊断功能，前提是
未设置 `CODEX_SECURITY_LOG_LEVEL`。

### 完成摘要

扫描完成后，会将代码仓库中未解决发现项的数量、按严重程度分类的统计、
覆盖情况、耗时、报告路径和结果目录写入 stderr。如果有相关数据，
还会显示 Token 使用量和预估费用：

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

信息类发现项会计入摘要总数。严重程度策略
仅评估当前扫描中严重程度为 `critical`、`high`、`medium` 和 `low` 的发现项，
不包括代码仓库总数中显示的以往发现项。

### JSON 输出

`scan --json` 会向 stdout 写入一个完整的 JSON 文档。其顶层结构
如下：

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

执行[修复](#patch-findings-after-a-scan)时，JSON 输出还会包含修复
结果以及已创建的 Pull Request（如有）。

进度、完成摘要、归档通知和错误仍会输出到 stderr。
即使严重程度策略
返回退出代码 `1`，或覆盖不完整导致返回退出代码 `2`，已完成的扫描仍会输出完整的 JSON 结果。

  `codex-security scan --json` 会输出一个 JSON 文档。`codex exec --json`
  会输出 JSON Lines 事件流。请使用与您运行的
  命令相匹配的输出格式。

## 扫描工件

扫描完成后，易读报告和结构化工件会保存在一起：

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

这些结构化文件各有不同用途：

| 文件                    | 内容                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | 扫描标识、状态、目标、范围、生成方以及已封存工件的记录。                                                    |
| `findings.json`         | 发现项标识符、严重程度、置信度、分类体系、位置、证据、验证、数据流、可达性和修复方案。 |
| `coverage.json`         | 已审查区域、排除项、延后处理的工作、待解决问题和覆盖完整性。                                        |
| `report.md`             | 易读的扫描报告。                                                                                                           |
| `artifacts/`            | 辅助扫描工件。                                                                                                      |
| `exports/results.sarif` | 扫描期间生成的 SARIF（如有）。                                                                                  |

覆盖完整性有三种取值：

- `complete`：扫描记录显示，所选范围已得到完整覆盖。
- `partial`：扫描记录了延后处理的工作或其他覆盖限制。
- `unknown`：扫描报告显示覆盖完整性未知。

在将覆盖情况用作安全决策依据之前，
请审查延后处理的区域、明确排除项和待解决问题。

## 退出代码和信号

CLI 使用以下退出代码：

| 退出代码  | 条件                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | 扫描已完成、覆盖完整且通过严重性策略；批量扫描或发布完成且无失败项；或者其他命令执行成功。                  |
| `1`   | 已完成的扫描报告了严重程度达到或超过所配置级别的发现项。                                                                                                       |
| `2`   | CLI 检测到输入、运行时或导出错误；扫描覆盖不完整；批量扫描中有代码仓库出现错误；或者发布时有一个或多个发现项发布失败。 |
| `130` | Ctrl-C 中断了扫描或发布。                                                                                                                                     |
| `143` | SIGTERM 终止了扫描或发布。                                                                                                                                     |

任何覆盖状态为 `partial` 或 `unknown` 的扫描都会返回 `2`，即使未设置
严重性策略也是如此。当您请求结构化输出时，已完成的扫描和
部分完成的发布仍会将可用结果写入 stdout。CLI
会在发生中断或运行时
错误后打印部分输出的位置。

## 本地扫描权限

CLI 和 SDK 扫描使用您的本地操作系统权限运行。每次扫描
都使用 `codex_security_scan` 文件系统配置方案，并将 `approvalPolicy` 设置为
`"never"`。该配置方案允许读取本地文件系统，并向
工作空间根目录和所选的扫描状态目录写入内容。扫描不会暂停以
请求交互式审批。

通过 CLI `--codex` 或 SDK `codexOverrides` 提供的设置，包括
`approval_policy`、`sandbox_mode` 和文件系统权限，无法替代
或限制这些扫描控制措施。主机和网络限制仍然适用。

扫描和工作台进程可能继承您的环境，包括无关的 API Token 和云端凭证。请仅扫描您信任且有权评估的代码仓库，并且只提供扫描所需的凭证。

## 身份验证和前提条件

设置 `OPENAI_API_KEY` 或 `CODEX_API_KEY`，通过
`npx @openai/codex-security login` 登录，或使用已存储在文件中的 Codex
登录信息。对于 OpenRouter 或 Fireworks，请设置该提供商的 API 密钥并选择
模型。对于 Amazon Bedrock，请改用 Bedrock API 密钥或标准 AWS
凭证链。

有关凭证选择，请参阅[选择扫描
身份验证方式](#select-scan-authentication)。

在 CI 中，请将 API 密钥的使用范围限定于扫描步骤，并使用受信任的工作流程。

CLI 要求使用 Node.js 22（22.13.0 或更高版本）、24 或 26。扫描、批量扫描、
导出、扫描历史记录和已保存的发现项还要求使用 Python 3.10 或更高版本。
Python 3.10 还需要 `tomli`。将 `--python` 与 `scan`、`bulk-scan` 或
`export` 一起使用，或者为任何基于 Python 的命令设置 `PYTHON`。

继续阅读[CLI 快速入门](/zh-Hans/codex/security/cli)、[批量扫描
指南](/zh-Hans/codex/security/cli/bulk-scans)、[CLI 常见问题](/zh-Hans/codex/security/cli/faq)、[CI
指南](/zh-Hans/codex/security/cli/ci)或[TypeScript SDK 指南](/zh-Hans/codex/security/sdk)。
