<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/cli/ci -->

在 CI 中运行 Codex Security CLI，审查 Pull Request 或合并请求中的确切更改，保留发现项和覆盖范围信息，并可选择在发现项达到指定严重性时使检查失败。先仅将结果用作参考，审查扫描质量和运行时间，再添加适合您代码仓库的严重性策略。

  安装公开发布的 `@openai/codex-security` 软件包。
  运行扫描仍需要 Codex Security 访问权限。

本指南提供 GitHub Actions 和 GitLab CI/CD 的示例。相同的扫描和导出命令也适用于其他 CI 系统。

## 准备工作流程

将 OpenAI API 密钥存储在您的 CI 提供商的机密存储区中，并命名为
`CODEX_SECURITY_API_KEY`。

将此机密直接映射到扫描步骤的 `OPENAI_API_KEY` 环境变量。
将凭据的使用范围限定为扫描进程，并使用
`--auth api-key` 明确选择该凭据。

仅针对您信任的代码仓库和 Pull Request 运行此工作流程。扫描会使用运行器的本地权限，并且不会暂停等待审批。扫描进程可能会继承作业环境，因此请勿在其中放置无关的 Token 或云端凭据。

运行器需要：

- Node.js 22（22.13.0 或更高版本）、24 或 26。
- Python 3.10 或更高版本。
- 已发布的 `@openai/codex-security` 软件包，需安装在
  代码仓库检出目录之外。
- Pull Request 或合并请求的头部提交和基准提交的历史记录，以便 Git 计算合并基准。

## 添加 GitHub Actions 工作流程

对于私有或内部代码仓库，请先启用
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)，
再上传 SARIF。

创建 `.github/workflows/codex-security.yml`。在检出 Pull Request 之前，
将 `@openai/codex-security` 安装到
`$RUNNER_TEMP/codex-security` 下，使受信任的可执行文件位于
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security`：

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

该工作流程会检出 Pull Request 的头部提交，计算其合并基准，
并扫描这两个修订版本之间已提交的更改。完整的历史记录可确保扫描目标准确。
`persist-credentials: false` 可避免将代码仓库 Token 写入检出目录中的 Git 配置。
在检出前安装 CLI，
并通过其绝对路径运行，可防止由代码仓库控制的可执行文件接触扫描凭据。
`--auth api-key` 会明确选择已限定作用域的 API 密钥。
扫描会将历史记录保存在可写状态目录中，
该目录位于代码仓库之外。

`--json` 会将一个完整的 JSON 文档写入 stdout，因此工作流程可以直接保存该文档。
进度、完成摘要和错误仍写入 stderr。
这不同于 `codex exec --json`，后者会输出 JSON Lines 事件流。

导出步骤会读取已完成并封存的扫描结果，然后写入 SARIF。它不会改动 Codex 运行时和凭据。扫描工件可能包含存在漏洞的源代码片段、证据和修复详情。请选择适合您代码仓库的访问控制措施，并设置较短的保留期限。

## 添加 GitLab CI/CD 流水线

如需在生产工作流程中支持受保护默认分支扫描、需主动启用的定时深度扫描、
独立的 SARIF 策略门禁，以及可选的经过验证的草稿合并请求，
请参阅[在 GitLab CI/CD 中
运行 Codex Security](/zh-Hans/codex/security/cli/ci/gitlab)。

在 GitLab Ultimate 19.2 或更高版本中，GitLab 可以导入
[SARIF 2.1.0 报告](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)。
运行流水线前，请添加一个设为掩码且隐藏的
`CODEX_SECURITY_API_KEY` CI/CD 变量。

以下最简示例将仅执行扫描的 `security` 作业添加到根目录的
`.gitlab-ci.yml` 中。请保留文件中已有的所有阶段和作业。该作业默认扫描合并请求中的更改。
将 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH`
设置为 `"true"`，还可对整个默认分支进行扫描：

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

默认情况下，该作业仅针对同一项目内分支发起的合并请求运行，
因此派生项目的流水线不会获得扫描凭据。
在组、项目或流水线级别将 `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` 设置为 `"true"`，
还可在默认分支上运行标准全量扫描。
全量扫描比差异扫描耗时更长，成本也更高。

`GIT_DEPTH: "0"` 会提供合并请求扫描所需的历史记录，
以便根据 `CI_MERGE_REQUEST_DIFF_BASE_SHA` 和 `CI_COMMIT_SHA` 计算合并基准。

该作业会将 CLI 安装在 `/tmp` 下，
通过绝对路径运行，并且仅向扫描进程提供 API 密钥。
`artifacts: when: always` 会在扫描失败时保留 SARIF 报告，
而 `artifacts:access: maintainer` 会限制对详细扫描结果的访问。

对 `.gitlab-ci.yml` 的更改可能会暴露 CI/CD 变量，
因此请在运行作业前审查流水线更改。如果您
[将 `CODEX_SECURITY_API_KEY` 设为受保护变量](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)，
GitLab 仅会向同一项目中受保护分支之间的合并请求提供该变量，
并且仅在用户有权访问目标分支时才提供。

GitLab 专项指南介绍了如何将这个最简作业扩展为生产工作流程，指南链接见本节开头。

## 选择严重性策略

这两个示例均未指定 `--fail-on-severity`，因此仅生成报告。
当您准备好让发现项影响检查结果时，
请为扫描命令添加阈值：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

支持的阈值为 `critical`、`high`、`medium` 和 `low`。
阈值涵盖当前扫描中严重性达到或超过该级别的发现项。
代码仓库摘要中显示的此前未解决的发现项不会影响该策略。

扫描步骤使用以下退出代码：

| 退出代码  | 含义                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | 扫描已完成且覆盖范围完整，所有已配置的策略均已通过。            |
| `1`   | 已完成的扫描中包含严重性达到或超过阈值的发现项。                        |
| `2`   | CLI 检测到输入错误或运行时错误，或者已完成扫描的覆盖范围不完整。 |
| `130` | Ctrl-C 中断了扫描。                                                            |
| `143` | SIGTERM 终止了扫描。                                                            |

覆盖范围为 `partial` 或 `unknown` 的扫描会返回 `2`，即使未设置严重性策略也是如此。
CLI 仍会写入可用的发现项和覆盖范围信息。
在将检查结果视为定论之前，请审查 `coverage.json` 中延后处理的区域。

## 使用现有结果目录重试

每个 CI 作业都应使用新的运行器目录。
对于持久化或自托管的运行器，请使用 `--archive-existing` 保留之前的结果：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

该命令会归档之前的结果，并从空扫描目录开始。

## 排查 CI 扫描问题

- **未知的 Git 引用或差异不符合预期：** 获取基准提交和头部提交的历史记录，
  计算合并基准，并明确传入这两个修订版本。
- **输出目录受保护或不为空：** 请选择所在 Git 工作树之外的私有目录。
  如果目录中已有结果，
  请使用 `--archive-existing`。
- **缺少凭据：** 请确认受信任的工作流程或流水线可以使用 `CODEX_SECURITY_API_KEY`，
  且该凭据已直接映射到扫描进程的
`OPENAI_API_KEY` 环境变量。
- **扫描历史记录错误：** 请将 `CODEX_SECURITY_STATE_DIR` 设置为
  代码仓库之外的可写目录。
- **Python 设置错误：** 请确认运行器使用 Python 3.10 或更高版本。
- **覆盖范围不完整：** 请审查 `coverage.json`，包括延后检查的范围和未解决的问题，
  然后使用适当的目标或环境重新运行。
- **SARIF 导出错误：** 请确认扫描已完成，且完整的扫描目录可用。
  导出操作会先验证已封存的工件，
  再写入 SARIF。
- **SARIF 上传错误：** 对于 GitHub Actions，请确认您的组织已为代码仓库
  启用 GitHub Code Security，并且工作流程授予了
`actions: read`、`contents: read` 和 `security-events: write` 权限。
  对于 GitLab CI/CD，请确认项目使用 GitLab Ultimate 19.2 或更高版本，
  并且作业通过 `artifacts:reports:sarif` 上传 SARIF 2.1.0 文件。

有关各个命令、标志、工件和输出字段的说明，请参阅 [CLI
参考资料](/zh-Hans/codex/security/cli/reference)。如需基于插件进行交互式 CI 审查，
请参阅[审查代码更改中的安全问题](/zh-Hans/codex/security/plugin/code-changes#automate-reviews-in-cicd)。
