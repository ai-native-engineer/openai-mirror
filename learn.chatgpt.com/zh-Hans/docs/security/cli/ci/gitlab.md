<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli/ci/gitlab -->

在 GitLab CI/CD 中运行 Codex Security，扫描已提交的变更和受保护的分支，将检测结果发布到 GitLab Security，并可选择通过草稿合并请求提出已验证的修复。

此工作流程将扫描凭据与代码仓库写入权限分离。生成的变更在合并前始终需要人工审查。

先仅扫描并生成报告。只有在检查项目的运行器、检测结果和凭据边界之后，才启用修复。

## 开始之前

您需要：

- 一个 GitLab 项目，配有支持 Codex 沙盒用户命名空间的可信运行器。
- 在 GitLab 项目中具有维护者或所有者角色，以便配置
[项目 CI/CD 变量](https://docs.gitlab.com/ci/variables/)和
  受保护的资源。
- 一个具有 Codex Security 访问权限的 OpenAI API 密钥。使用平台
  API 密钥的组织可[申请 Trusted Access for
  Cyber](https://openai.com/form/enterprise-trusted-access-for-cyber/)。
  使用 ChatGPT 身份验证的个人用户可使用[个人 Trusted Access
  流程](https://chatgpt.com/cyber)。对于某些账户或代码仓库，
  全库扫描需要此访问权限。
- GitLab Ultimate 19.2 或更高版本，用于[导入 SARIF 2.1.0
  报告](https://docs.gitlab.com/user/application_security/detect/sarif/)。
- 完整的 Git 历史记录，以便合并请求作业计算合并基点。

流水线镜像会安装 Node.js 26、Python 3、Git、`rg` 和固定版本的
Codex Security CLI。自动修复还需要现有的回归测试，
以及能够在不持有受保护凭据的情况下
运行由代码仓库控制的命令的运行器。

## 从仅扫描的流水线开始

创建名为
`CODEX_SECURITY_API_KEY` 的 GitLab CI/CD 变量，并启用掩码、隐藏和保护设置。使用具有 Codex Security
访问权限的 OpenAI 平台 API 密钥，并将其环境作用域设为 `codex-security/openai`。请参阅
[限定环境作用域的 CI/CD 变量](https://docs.gitlab.com/ci/environments/#limit-the-environment-scope-of-a-cicd-variable)。

先将这个最小流水线添加到测试项目。它会扫描符合条件的受保护合并请求中已提交的变更，通过成功完成的报告作业发布 SARIF，并在单独的门禁步骤中还原扫描器结果：

```yaml
stages:
  - security_scan
  - security_gate

.codex-security-merge-request:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID && $CI_MERGE_REQUEST_SOURCE_BRANCH_PROTECTED == "true" && $CI_MERGE_REQUEST_TARGET_BRANCH_PROTECTED == "true"'

codex-security:
  extends: .codex-security-merge-request
  stage: security_scan
  image: node:26-bookworm-slim
  environment:
    name: codex-security/openai
    action: access
  variables:
    GIT_DEPTH: "0"
  before_script:
    - npm install --prefix /tmp/codex-security-cli --ignore-scripts --no-audit --no-fund @openai/codex-security@0.1.20
  script:
    - |
      set -eu
      test -n "${CODEX_SECURITY_API_KEY:-}"

      CODEX_SECURITY_BIN="/tmp/codex-security-cli/node_modules/.bin/codex-security"
      RESULTS_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      ARTIFACT_DIR="codex-security-artifacts"
      BASE_REVISION="$(git merge-base \
        "$CI_MERGE_REQUEST_DIFF_BASE_SHA" "$CI_COMMIT_SHA")"
      install -d -m 700 "$RESULTS_DIR" "$ARTIFACT_DIR/results"

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY
      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          --diff "$BASE_REVISION" \
          --head "$CI_COMMIT_SHA" \
          --auth api-key \
          --output-dir "$RESULTS_DIR" \
          --json
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      case "$scan_exit" in
        0|1|2) ;;
        *) exit "$scan_exit" ;;
      esac

      "$CODEX_SECURITY_BIN" export "$RESULTS_DIR" \
        --export-format sarif \
        --source-root "$CI_PROJECT_DIR" \
        --output "$ARTIFACT_DIR/results.sarif"
      test -s "$ARTIFACT_DIR/results.sarif"
      cp -R "$RESULTS_DIR"/. "$ARTIFACT_DIR/results/"
      printf '%s\n' "$scan_exit" > "$ARTIFACT_DIR/scan-exit-code.txt"
      exit 0
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/results.sarif

codex-security-gate:
  extends: .codex-security-merge-request
  stage: security_gate
  image: alpine:3.20
  needs:
    - job: codex-security
      artifacts: true
  script:
    - exit "$(cat codex-security-artifacts/scan-exit-code.txt)"

  

在运行持有机密信息的作业之前，请审查对 `.gitlab-ci.yml` 的每一项变更。
这个最小示例有意省略了全量扫描和修复。

## 采用生产流水线

1. [下载完整的 GitLab 流水线](/codex/security/cli/ci/gitlab.yml)，
   并将其保存为代码仓库根目录下的 `.gitlab-ci.yml`。如果您的代码仓库
   已有流水线，请将示例中的阶段、隐藏模板和
   作业合并到现有文件中。
2. 保留现有的构建、测试和部署阶段。如果项目使用
`workflow: rules`，请确认这些规则允许触发您希望扫描的
   流水线事件。

此示例添加了 `security_scan`、`security_remediation`、`security_publish`
和 `security_gate` 阶段。仅扫描并生成报告只需要
`CODEX_SECURITY_API_KEY`。

默认情况下，扫描作业仅针对同一项目中
受保护分支之间的合并请求运行。设置 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH=true`，即可扫描
向受保护默认分支的推送以及手动触发的流水线。设置
`CODEX_SECURITY_SCHEDULED_DEEP_SCAN=true` 并明确配置时间和成本
预算，即可在受保护的默认分支上启用定时深度扫描。

只有满足以下条件，合并请求流水线才能访问受保护的变量和运行器：

- 您已将同一项目中的源分支和目标分支都设为受保护分支。
- 项目[允许合并请求流水线访问受保护的变量和
  运行器](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)。
- 启动流水线的用户有权向目标分支推送或合并。

派生代码仓库的流水线和未受保护的合并请求不会获得扫描凭据。
在运行持有机密信息的作业之前，请审查对 `.gitlab-ci.yml` 的每一项变更。
对变量启用掩码和隐藏设置，
并不能使不可信的 CI 代码变得安全。

## 运行扫描并审查检测结果

创建符合条件的受保护合并请求，或在受保护的默认分支上运行流水线。在运行付费的全库扫描之前，请先从小范围差异开始。

打开 `codex-security` 作业，确认其产物包含：

- `scan-manifest.json`
- `findings.json`
- `coverage.json`
- `results.sarif`
- `scan-exit-code.txt`

然后打开流水线的 **安全** 选项卡，审查导入警告，并确认
检测结果的标识符、严重程度和源码位置。默认分支扫描
还会创建项目漏洞记录。合并请求的检测结果会显示在
流水线的安全选项卡或合并请求的安全小组件中，但不会创建
项目范围的漏洞记录。

请限制对产物的访问，因为扫描结果可能包含存在漏洞的源码片段、证据和修复详情。

## 选择扫描配置方案

流水线会根据触发条件选择配置方案：

| 触发条件                                        | 目标          | 模式       | 强度  |
| ---------------------------------------------- | --------------- | ---------- | ------- |
| 同一项目内受保护的合并请求           | 已提交的差异  | `standard` | `low`   |
| 受保护默认分支上的推送或手动触发（需主动启用） | 整个代码仓库 | `standard` | `high`  |
| 受保护默认分支上的定时触发（需主动启用）    | 整个代码仓库 | `deep`     | `xhigh` |

合并请求扫描专注于对已提交的变更提供反馈。默认分支扫描审查集成后的代码仓库。定时深度扫描定期提供更广泛的覆盖。完成一次差异扫描只说明扫描了该项变更，并不意味着整个代码仓库没有问题。

此工作流程将 CLI 安装在代码仓库之外，并通过绝对路径运行。试运行预检会使用仅传入该进程的 API 密钥，但不会启动付费扫描，也不会检查 API 身份验证、Codex Security 访问权限、配额或模型可用性。

此工作流程将扫描状态和结果写入工作树之外，并将
`OPENAI_API_KEY` 的作用域限定为扫描进程。CLI 只接收一组精简且明确指定的
环境变量，而不会继承所有 GitLab 变量。对于差异扫描，
此工作流程会计算合并基点，并将扫描绑定到已审查的基准修订版本和
头部修订版本。

此示例将 `@openai/codex-security` 的版本固定为 `0.1.20`。更改固定版本之前，请重新测试身份验证、
产物、SARIF 导入和策略门禁。

## 将报告与策略执行分离

GitLab 从成功完成的报告作业中导入 SARIF。流水线先发布
报告，再通过单独的
`codex-security-gate` 作业还原扫描器的退出状态。

报告作业会接受退出码为 `0` 和 `1` 时的检测结果。对于退出码
`2`，只有当扫描清单证明扫描已完成、覆盖情况
明确为 `partial`，且存在非空的 SARIF 报告时，才会接受。其他运行时、
配置或导出失败仍会阻止流程继续。

最终门禁会保留以下扫描器退出码：

| 退出码 | 含义                                                                     |
| ---- | --------------------------------------------------------------------------- |
| `0`  | 扫描已完成，覆盖完整，并通过了策略检查。            |
| `1`  | 扫描已完成，并发现严重程度达到或超过配置阈值的问题。 |
| `2`  | 扫描覆盖不完整，或发生了输入错误或运行时错误。              |

在您调整部分覆盖的处理方式期间，此示例暂时允许退出码 `2`。
当覆盖不完整必须导致流水线失败时，请取消这项例外。

修复和发布会在最终策略门禁之前运行。即使该门禁随后使流水线失败，仍可针对符合条件的问题生成经过验证的合并请求草稿。

## 启用经验证的修复

自动修复是可选功能，仅在受保护的默认分支流水线中运行。Codex 修复进程和由代码仓库控制的验证命令不会接收 GitLab 项目访问 Token 或运行器注入的凭据。

安全约定包含三部分：由代码仓库控制的命令绝不接收 OpenAI 或 GitLab 凭据；只有发布作业拥有代码仓库写入权限；每项生成的更改在人工审查并合并前都保持草稿状态。

此工作流程会：

1. 要求扫描覆盖完整，并发现严重程度为 `high` 或 `critical` 的
   问题。
2. 确认配置的回归测试在应用补丁前失败。
3. 生成针对性补丁，并拒绝对 CI 文件、凭据文件、二进制文件或其他受保护文件的更改。
4. 在不提供 OpenAI、GitLab、制品仓库、部署或作业 Token 凭据的情况下运行回归测试。
5. 使用 `verify-fix` 返回 `fixed`、`still_vulnerable` 或 `inconclusive`。
   只有当 `verify-fix` 返回 `fixed`，且
   验证过程未更改补丁时，作业才会发布补丁。

设置以下受保护变量以启用修复：

- 将 `CODEX_SECURITY_ENABLE_REMEDIATION` 设为 `true`。
- 将 `CODEX_SECURITY_VERIFICATION_COMMAND` 设为一个现有的回归测试，
  其退出码在修复前为 `1`，修复后为 `0`。
- 您也可以将 `CODEX_SECURITY_SETUP_COMMAND` 设为
  非交互式依赖项设置命令。

请选择验证底层安全不变量的回归测试，而不是针对某个具体实现的测试。对生成的测试更改和源代码更改应采用同样严格的审查标准。

<details>
  <summary>高级：代码仓库命令隔离</summary>

`validate`、`patch` 和 `verify-fix` 命令会接收仅限其进程使用的
`CODEX_API_KEY`。由代码仓库控制的设置和测试命令以
单独的非特权用户身份，在已跟踪源文件的可写副本中运行。
该副本刻意排除了 Git 元数据、子模块内容和
下载的产物。需要 `.git` 或
子模块的设置和测试命令必须在单独设计的不含凭据的作业中运行。

只有归 root 所有的 Codex 步骤才能访问基准检出目录，或 GitLab 的
相邻文件变量目录。副本的纯净环境仅包含
`PATH`、`HOME`、`LANG`、`CI` 和 `CI_PROJECT_DIR`。如果某条命令需要其他
非机密值，请先审查该命令，再将该值加入允许列表。如果您的
运行器无法切换用户，请先将验证移至单独的不含凭据的
作业，再启用修复。

</details>

## 发布合并请求草稿

创建一个 [GitLab 项目访问
Token](https://docs.gitlab.com/user/project/settings/project_access_tokens/#create-a-project-access-token)，
赋予其开发者角色以及 `api` 和 `write_repository` 作用域。将其保存为
受保护、已掩码且已隐藏的变量 `GITLAB_REMEDIATION_TOKEN`，作用域仅限于
`codex-security/publish` 环境。

设置 `CODEX_SECURITY_CREATE_MR=true` 以启用发布。同时将非机密变量
`CODEX_SECURITY_MR_TEST_COMMAND` 设为项目专用的安全回归测试，
每个生成的修复分支都必须通过该测试。请勿将此变量
设为受保护变量，以便生成的不受保护的合并请求可以读取该命令。
发布工作流程会：

- 接收代码仓库写入 Token，但不接收 OpenAI 凭据。
- 创建一个 `codex-security/fix-<finding-hash>` 分支。
- 创建合并请求草稿；如果已有处于打开状态的草稿，则复用该草稿，避免重复创建。
- 在不提供受保护凭据的情况下，以非特权用户身份在仅包含已跟踪文件的副本中运行不受保护的修复分支的回归测试。
- 绝不自动合并生成的更改。

不要用 `CI_JOB_TOKEN` 代替项目访问 Token。它无法执行
所需的合并请求创建操作。合并前请审查建议的补丁、
验证证据以及扫描发现的问题。

## 配置可选变量

仅配置您启用的功能所需的变量：

| 变量                                  | 何时需要                       | 默认值或用途                                          |
| ----------------------------------------- | --------------------------------- | ----------------------------------------------------------- |
| `CODEX_SECURITY_API_KEY`                  | 每次扫描                        | 受保护、已掩码且已隐藏；作用域限定为 `codex-security/openai` |
| `CODEX_SECURITY_VERSION`                  | CLI 升级                       | 版本固定为 `0.1.20`；更改前需重新测试                  |
| `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` | 默认分支全量扫描         | 需主动启用；默认关闭                             |
| `CODEX_SECURITY_SCHEDULED_DEEP_SCAN`      | 定时深度扫描              | 需主动启用；默认关闭                             |
| `CODEX_SECURITY_DEEP_MAX_TIME_HOURS`      | 定时深度扫描              | 必须设置大于 `0` 且小于 `8` 的时间预算     |
| `CODEX_SECURITY_DEEP_MAX_COST`            | 定时深度扫描              | 必须设置大于 `0` 的预估费用限制（美元）      |
| `CODEX_SECURITY_ENABLE_REMEDIATION`       | 补丁生成                  | 需通过受保护变量主动启用；默认关闭                            |
| `CODEX_SECURITY_VERIFICATION_COMMAND`     | 补丁生成                  | 受保护的回归测试                                   |
| `CODEX_SECURITY_SETUP_COMMAND`            | 可选的修复设置        | 受保护的依赖项安装                           |
| `CODEX_SECURITY_REMEDIATION_EFFORT`       | 可选的修复调优       | `high`                                                      |
| `CODEX_SECURITY_MAX_CHANGED_FILES`        | 可选的补丁大小限制         | `8`；允许范围为 `1` 至 `20`                         |
| `CODEX_SECURITY_CREATE_MR`                | 创建合并请求草稿      | 需通过受保护变量主动启用；默认关闭                            |
| `GITLAB_REMEDIATION_TOKEN`                | 创建合并请求草稿      | 具有开发者角色的项目 Token，作用域限定为 `codex-security/publish`  |
| `CODEX_SECURITY_GITLAB_INTERNAL_URL`      | 可选的自托管发布   | 运行器可访问的 GitLab 源站地址                     |
| `CODEX_SECURITY_MR_TEST_COMMAND`          | 发布合并请求草稿    | 必需的项目专用回归测试，不含机密信息       |
| `CODEX_SECURITY_MR_SETUP_COMMAND`         | 可选的修复分支设置 | 不含机密信息的依赖项设置                                 |

GitLab 提供 `CI_*` 变量。流水线管理
`CODEX_SECURITY_BIN`、`CODEX_SECURITY_EFFORT`、`CODEX_SECURITY_MODE`、
`CODEX_SECURITY_STATE_DIR` 和 `CODEX_SECURITY_TARGET`；请勿将它们
配置为项目变量。对于差异扫描，CLI 根据规范化后的基准和头部修订版本
推导出规范的目标标识。

## 调整策略执行方式和成本

使用有针对性的差异扫描为合并请求提供反馈，对默认分支
使用标准代码仓库扫描，并通过定时深度扫描扩大覆盖范围。这两种
全代码仓库扫描配置方案默认均关闭。定时深度扫描还需要设置
`CODEX_SECURITY_DEEP_MAX_TIME_HOURS` 和 `CODEX_SECURITY_DEEP_MAX_COST`；
CLI 的时间预算必须低于作业的 8 小时超时时限。请先收集典型运行的测量数据，
再设置预算。将 `--max-cost` 视为用于控制预估成本的阈值，而非
严格的计费上限。

先从仅生成报告的扫描开始。请在您的团队
审查有代表性的发现项、覆盖范围、成本和运行时间后，再添加 `--fail-on-severity`。请参阅 [在 CI 中运行
Codex Security](/zh-Hans/codex/security/cli/ci)，了解严重性策略和退出码的
详细信息。

作业失败时：

- 扫描产物缺失表明配置或运行器存在问题。
- 如果已有产物但覆盖不完整，需要审查 `coverage.json`。
- 如果 GitLab 中缺少发现项，请检查 SARIF 报告作业
是否成功，以及 GitLab 是否接受了该报告。
- 如果修复被跳过，请检查分支是否受保护、扫描覆盖是否完整、
发现项的严重性、验证命令以及用于启用修复的变量。
- 发布出错时，请检查项目 Token 的角色、权限范围和
环境限制。

有关所有命令、标志和产物的信息，请参阅 [Codex Security CLI
参考资料](/zh-Hans/codex/security/cli/reference)。
