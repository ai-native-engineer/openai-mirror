<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/plugin/code-changes -->

对 Git 管理的单个变更集运行安全审查，以发现安全回归问题。
Codex 会审查每个已更改的源代码类文件，以及直接支持该文件的代码。
审查不会扩大为对整个代码仓库的全面审计。

若要扫描整个代码仓库而非特定更改，请参阅[运行安全
扫描](/zh-Hans/codex/security/plugin/scans)。

## 手动运行审查

在桌面应用中，打开 **安全**，选择 **扫描**，再选择 **+ 扫描**。
选择代码仓库，然后选择 **更改**。您可以审查未提交的更改、
单个提交，或基准修订版本和目标修订版本。 **深度扫描** 不适用于
更改扫描。

您还可以在对话中让 Codex 审查未提交的更改：

```text
Use $codex-security:security-diff-scan to review my current uncommitted changes for security regressions.

对于提交范围或分支范围，必要时请同时指定两个修订版本：

```text
Use $codex-security:security-diff-scan to review the changes from origin/main to HEAD for security regressions. Focus on authentication, authorization, input handling, filesystem access, network requests, and secrets.

如果 Pull Request 的基准修订版本和目标修订版本在本地检出中均可用，
您也可以指定该 Pull Request。

## 在设置中确认更改

1. 选择 **更改**。
2. 确认已检出的代码仓库、当前分支和最新提交。
3. 在 **待审查的更改**中，选择以下内容：
   - `Uncommitted changes`，用于当前工作树。
   - 最新提交，用于审查单个提交。
   - 基准修订版本和目标修订版本，用于审查分支或 Pull Request 范围。
4. 确认摘要描述的是您打算审查的更改。
5. 选择 **开始扫描**。

Codex 不会检出其他分支，也不会切换选定的工作树。如果
所需修订版本在本地不可用，请在审查前获取该版本，或者
提供本地可用的基准修订版本和目标修订版本。

## 处理发现项

审查结果后，[修复并验证已接受的
发现项](/zh-Hans/codex/security/plugin/fix-findings)，或[导出并跟踪
发现项](/zh-Hans/codex/security/plugin/export-findings)。

## 在 CI/CD 中自动执行审查

如果您可以使用测试版独立 CLI，请参阅[在 CI 中
运行 Codex Security](/zh-Hans/codex/security/cli/ci)，了解结构化 JSON、严重程度策略和 SARIF
上传。请继续阅读本节，了解如何通过
`codex exec` 调用已安装的插件技能。

当运行器能够以非交互方式调用 Codex CLI 时，请在 CI 中运行 `$codex-security:security-diff-scan`。
首先，请在不暴露扫描凭据的情况下
安装 CLI：

```bash
npm install --global @openai/codex

在 CLI 中安装 Codex Security 插件：

```bash
codex plugin add codex-security@openai-curated

该安装命令使用公开的 Codex CLI 插件市场。
请先查看[插件更新日志](/zh-Hans/codex/security/plugin/changelog)，再在 CI 中
依赖特定插件版本或功能。

接下来，请将 CI 机密存储中的 OpenAI API 密钥作为
`CODEX_SECURITY_API_KEY` 提供。仅向扫描过程提供该凭据：

```bash
CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
  --sandbox workspace-write \
  "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

可写沙盒允许扫描创建临时工件。提示
仍要求 Codex 保持已检出的源代码不变。

扫描会将输出写入
`$TMPDIR/codex-security-scans/<repository>/<scan-id>/`：

| 文件                 | 内容                                                                                                                                                  |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `report.md`          | 查看完整扫描目录的主要可读入口。                                                                                              |
| `findings/<slug>/`   | 按需提供详细的漏洞报告及配套的概念验证文件。                                                                     |
| `hardening/`         | 按需提供结构性加固指南及配套方案。                                                                                   |
| `findings.json`      | 包含稳定标识符、严重程度、置信度、源代码位置和修复措施的发现项。将这些发现项提供给经批准的内部安全工作流或下游工具。 |
| `scan-manifest.json` | 密封的扫描回执，包含审查目标、修订版本和工件哈希。                                                                             |
| `coverage.json`      | 已审查和暂缓审查的范围、排除项以及覆盖完整性。                                                                                    |

[`findings.json` 模式](https://github.com/openai/plugins/blob/main/plugins/codex-security/schemas/findings.schema.json)
定义了完整结构。该模式包含以下字段：

| 字段                     | 类型   | 说明                                                            |
| ------------------------- | ------ | ---------------------------------------------------------------------- |
| `documentType`            | 字符串 | 将文档标识为 `codex-security.findings`。                  |
| `schemaVersion`           | 字符串 | 标识发现项模式的版本。                                |
| `scanId`                  | 字符串 | 标识生成这些发现项的扫描。                        |
| `findings`                | 数组  | 包含零个或多个发现项对象。                                 |
| `findings[].findingId`    | 字符串 | 根据发现项指纹派生的稳定发现项标识符。        |
| `findings[].occurrenceId` | 字符串 | 标识该发现项在特定扫描中的本次出现。          |
| `findings[].ruleId`       | 字符串 | 标识漏洞家族。                                   |
| `findings[].identity`     | 对象 | 包含语义锚点和可选的同级实例标识符。 |
| `findings[].fingerprints` | 对象 | 包含指纹算法和主指纹。            |
| `findings[].title`        | 字符串 | 提供简短的发现项标题。                                      |
| `findings[].summary`      | 字符串 | 概述漏洞及其影响。                           |
| `findings[].severity`     | 对象 | 包含严重性级别和可选的评分详情。              |
| `findings[].confidence`   | 对象 | 包含置信度级别和判断依据。                           |
| `findings[].taxonomy`     | 对象 | 包含漏洞类别和 CWE 标识符。               |
| `findings[].locations`    | 数组  | 列出受影响的文件、行号和位置角色。                |
| `findings[].remediation`  | 字符串 | 说明建议的修复方法。                                         |
| `findings[].provenance`   | 对象 | 标明发现项的来源。                                  |

例如，以下命令会为每个发现项打印一行以制表符分隔的数据：

```bash
jq -r '
  .findings[] |
  [.findingId, .severity.level, .confidence.level, .locations[0].path, .locations[0].startLine, .title] |
  @tsv
' findings.json

这些示例假定使用受信任的 Linux 运行器，其中安装了 Node.js 和 `npm`、Git、Python
3、`jq` 以及相应提供商的命令行工具。`npm` 的全局软件包前缀
必须可写。

请选择与您的 CI 提供商对应的示例：

扫描结果可能包含敏感的漏洞详情。请确保构件
不公开，并仅在审查发布对象、内容和
所需审批后发布发现项。

  <div slot="github">

```yaml
name: Codex Security review

on:
  pull_request:

jobs:
  security-review:
    if: github.event.pull_request.head.repo.full_name == github.repository
    runs-on: ubuntu-latest
    permissions:
      contents: read
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Install Codex Security
        env:
          CODEX_HOME: ${{ runner.temp }}/codex-home
        run: |
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated

      - name: Review code changes
        env:
          CODEX_SECURITY_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_HOME: ${{ runner.temp }}/codex-home
          TMPDIR: ${{ runner.temp }}/codex-security
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_REVISION: ${{ github.event.pull_request.head.sha }}
        run: |
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_REVISION")"
          CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
            --sandbox workspace-write \
            "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."

      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: codex-security-review
          path: ${{ runner.temp }}/codex-security/codex-security-scans

  </div>

  <div slot="gitlab">

创建启用掩码的 `CODEX_SECURITY_API_KEY` CI/CD 变量，并在分享发现项前以非公开方式审查扫描
构件。

```yaml
codex-security-review:
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
  variables:
    GIT_DEPTH: "0"
  script:
    - |
      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
      CODEX_API_KEY="$codex_security_api_key" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
  after_script:
    - |
      unset CODEX_SECURITY_API_KEY
      scan_root="/tmp/codex-security-$CI_JOB_ID/codex-security-scans"
      if [ -d "$scan_root" ]; then
        tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
      fi
  artifacts:
    when: always
    paths:
      - codex-security-artifacts.tar.gz

  </div>

  <div slot="azure">

```yaml
trigger: none

pool:
  vmImage: ubuntu-latest

steps:
  - checkout: self
    fetchDepth: 0

  - bash: |
      set -euo pipefail

      npm install --global @openai/codex
      codex plugin add codex-security@openai-curated
    displayName: Install Codex Security

  - bash: |
      set -euo pipefail

      CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
        --sandbox workspace-write \
        "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
    displayName: Review code changes
    condition: and(succeeded(), ne(variables['System.PullRequest.IsFork'], 'True'))
    env:
      CODEX_SECURITY_API_KEY: $(CODEX_SECURITY_API_KEY)

  - publish: $(Agent.TempDirectory)/codex-security/codex-security-scans
    artifact: codex-security-review
    condition: always()

请为 Azure Repos 配置 **生成验证** 分支策略，以便针对 Pull Request 运行
流水线。

  </div>

  <div slot="jenkins">

```groovy
pipeline {
  agent { label 'linux' }
  stages {
    stage('Codex Security review') {
      when {
        allOf {
          changeRequest()
          expression { !env.CHANGE_FORK?.trim() }
        }
      }
      steps {
        sh '''#!/usr/bin/env bash
          set -euo pipefail

          mkdir -p "$TMPDIR"
          git fetch --no-tags origin "$CHANGE_TARGET"
          target="$(git rev-parse FETCH_HEAD)"
          git fetch --no-tags origin "$CHANGE_BRANCH"
          git rev-parse FETCH_HEAD > "$TMPDIR/head"
          git merge-base "$target" "$(cat "$TMPDIR/head")" > "$TMPDIR/base"
          npm install --global @openai/codex
          codex plugin add codex-security@openai-curated
        '''
        withCredentials([string(credentialsId: 'codex-security-api-key', variable: 'CODEX_SECURITY_API_KEY')]) {
          sh '''#!/usr/bin/env bash
            set +x
            set -euo pipefail

            CODEX_API_KEY="$CODEX_SECURITY_API_KEY" codex exec \
              --sandbox workspace-write \
              "Use \$codex-security:security-diff-scan to review changes from $BASE_REVISION to $HEAD_REVISION for security regressions. Do not modify the checkout."
          '''
        }
      }
      post {
        always {
          sh '''#!/usr/bin/env bash
            set -euo pipefail
            scan_root="/tmp/codex-security-$BUILD_TAG/codex-security-scans"
            if [ -d "$scan_root" ]; then
              tar -czf codex-security-artifacts.tar.gz -C "$scan_root" .
            fi
          '''
          archiveArtifacts artifacts: 'codex-security-artifacts.tar.gz', allowEmptyArchive: true
        }
      }
    }
  }
}

  </div>

这些示例会跳过来自派生代码仓库的 Pull Request。仅可基于
受保护的流水线定义运行需要凭证的作业，并且只能为受信任且可接触扫描
凭证的贡献者运行此类作业。请归档 `codex-security-scans`，将结构化发现项、
清单、覆盖范围和 `report.md` 一并保存，并包含任何已请求的
`findings/` 或 `hardening/` 输出。初期请将结果仅作为参考，并审查
覆盖范围和运行时间，再将该作业设为必需检查项。

有关 API 密钥处理和沙盒控制，请参阅[非交互
模式](/zh-Hans/codex/non-interactive-mode)。如果您的组织允许使用 [Codex
GitHub Action](/zh-Hans/codex/github-action)，它可以在运行时安装 CLI，但
您仍须先安装插件，并将该 GitHub Action 的 `codex-home`
输入指向同一个 `CODEX_HOME`。
