<!-- source: https://learn.chatgpt.com/zh-Hans/docs/non-interactive-mode -->

非交互模式让您无需打开交互式 TUI，即可通过脚本（例如持续集成（CI）作业）运行 Codex。
您可以使用 `codex exec` 调用此模式。

有关各标志的详细信息，请参阅 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)。

## 何时使用 `codex exec`

如果您希望 Codex 执行以下操作，请使用 `codex exec`：

- 作为流水线的一部分运行（CI、合并前检查、计划作业）。
- 生成可通过管道传递给其他工具的输出，例如用于生成发行说明或摘要。
- 自然融入 CLI 工作流，将命令输出传入 Codex，并将 Codex 输出传递给其他工具。
- 使用明确预设的沙盒和审批设置运行。

## 基本用法

将任务提示作为单个参数传入：

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

在 `codex exec` 运行期间，Codex 会将进度流式输出到 `stderr`，并且只将最终的智能体消息打印到 `stdout`。这样可以轻松重定向最终结果，或通过管道传递该结果：

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

如果您不希望将会话运行记录文件持久保存到磁盘，请使用 `--ephemeral`：

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

如果 stdin 通过管道传入，并且您还提供了提示参数，Codex 会将该提示视为指令，并将管道传入的内容视为额外上下文。

这样，您可以使用一条命令生成输入，并将其直接传递给 Codex：

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

有关更高级的 stdin 管道传输模式，请参阅 [高级 stdin 管道传输](#advanced-stdin-piping)。

## 权限和安全

默认情况下，`codex exec` 在只读沙盒中运行。在自动化场景中，请为工作流设置所需的最低权限：

- 允许编辑：`codex exec --sandbox workspace-write "<task>"`
- 允许更广泛的访问权限：`codex exec --sandbox danger-full-access "<task>"`

仅在受控环境中使用 `danger-full-access`，例如隔离的 CI 运行器或容器。

Codex 仍保留 `codex exec --full-auto` 作为已弃用的兼容性标志，并会显示警告。新脚本应优先使用明确的 `--sandbox workspace-write` 标志。

如果某次运行不应加载 `$CODEX_HOME/config.toml`，请使用 `--ignore-user-config`；如果需要在受控的自动化环境中跳过用户和项目的 execpolicy `.rules` 文件，请使用 `--ignore-rules`。

如果您为已启用的 MCP 服务器配置了 `required = true`，而该服务器初始化失败，`codex exec` 会报错并退出，而不会在缺少该服务器的情况下继续运行。

## 使输出可供机器读取

要在脚本中处理 Codex 输出，请使用 JSON Lines 格式输出：

```bash
codex exec --json "summarize the repo structure" | jq

启用 `--json` 后，`stdout` 会变为 JSON Lines（JSONL）流，因此您可以捕获 Codex 运行期间发出的每个事件。事件类型包括 `thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*` 和 `error`。

条目类型包括智能体消息、推理、命令执行、文件更改、MCP 工具调用、网页搜索和计划更新。

JSON 流示例（每行均为一个 JSON 对象）：

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

如果您只需要最终消息，可使用 `-o <path>`/`--output-last-message <path>` 将其写入文件。此操作会将最终消息写入文件，同时仍将其打印到 `stdout`（详情请参阅 [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec)）。

## 使用模式创建结构化输出

如果下游步骤需要结构化数据，请使用 `--output-schema` 请求符合 JSON Schema 的最终响应。
这适用于需要稳定字段的自动化工作流，例如作业摘要、风险报告或发布元数据。

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

使用该模式运行 Codex，并将最终 JSON 响应写入磁盘：

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

最终输出示例（stdout）：

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## 在自动化中进行身份验证

`codex exec` 默认复用已保存的 CLI 身份验证信息。在 CI 中，通常会显式提供凭据：

如果您受信任的云端环境或 CI 运行时已经接收短期有效的工作负载令牌，
请使用
[工作负载身份联合](/zh-Hans/codex/enterprise/workload-identity)，
而不是存储 OpenAI 凭据。

### 使用 API 密钥进行身份验证

对于 GitHub Actions，请使用 [Codex GitHub Action](/zh-Hans/codex/github-action)，而不是自行安装 CLI 并进行身份验证。该 GitHub Action 会安装 Codex、启动 Responses API 代理，并使用可配置的安全策略运行 Codex，从而降低 API 密钥暴露风险。

如果工作流会签出或运行由代码仓库控制的代码，请勿将 `OPENAI_API_KEY` 或 `CODEX_API_KEY` 设置为作业级环境变量。同一作业中的构建脚本、测试、依赖项生命周期钩子或已遭入侵的 GitHub Action 都可以读取这些环境变量。

对于其他自动化环境，请仅设置 `CODEX_API_KEY` 以供需要它的 Codex
调用使用，并确保同一
进程环境中不运行任何不受信任的代码。

要在单次运行中使用不同的 API 密钥，请以内联方式设置 `CODEX_API_KEY`：

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

您可以将 `CODEX_API_KEY` 与 `codex exec`、`codex review`、TypeScript
SDK 以及 `codex exec-server --remote` 搭配使用。

如果您需要使用 Codex 用户账户而非 API 密钥运行 CI/CD 作业，
请阅读本节。例如，在受信任的运行器上使用由 ChatGPT 管理的 Codex 访问权限的企业团队，
或需要采用 ChatGPT/Codex 速率限制而非 API 密钥用量的用户。

API 密钥更易于预配和轮换，因此是自动化场景的合适默认选择。
仅当您明确需要以自己的 Codex 账户身份运行时，
才应采用这种方式。

请像保护密码一样保护 `~/.codex/auth.json`：其中包含访问令牌。切勿
提交该文件、将其粘贴到工单中，或在聊天中分享。

请勿将此工作流用于公开或开源代码仓库。如果运行器无法使用 `codex login`，
请通过安全存储预置 `auth.json`，并在运行器上
运行 Codex，使 Codex 就地刷新该文件，同时在各次运行之间
持久保存更新后的文件。

请参阅 [在 CI/CD 中维护 Codex 账户身份验证（高级）](/codex/auth/ci-cd-auth)。

## 恢复非交互会话

如果您需要继续先前的运行，例如在两阶段流水线中，请使用 `resume` 子命令：

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

您也可以使用 `codex exec resume <SESSION_ID>` 指定具体的会话 ID。

## 需要 Git 代码仓库

Codex 要求命令在 Git 代码仓库内运行，以防止破坏性更改。如果您确定环境安全，可使用 `codex exec --skip-git-repo-check` 跳过此检查。

## 常见自动化模式

### 示例：在 GitHub Actions 中自动修复 CI 失败问题

对于 GitHub Actions 工作流，请使用 [`openai/codex-action`](https://github.com/openai/codex-action)，而不要自行安装 Codex 并将 API 密钥传递给 shell 步骤。该 GitHub Action 会为 OpenAI API 密钥启动安全代理。

当 CI 工作流失败时，您可以使用 Codex 自动提出修复方案。流程如下：

1. 当您的主 CI 工作流因错误而结束时，触发后续工作流。
2. 仅使用代码仓库读取权限，签出导致失败的提交。
3. 在运行 Codex 之前执行设置命令，且不向这些步骤暴露您的 OpenAI API 密钥。
4. 运行 Codex GitHub Action。
5. 将 Codex 的本地更改保存为补丁构件。
6. 在单独的作业中应用补丁并创建 Pull Request。

下面的 Codex 作业仅具有 `contents: read` 权限。Codex 运行完成后，该作业只会将差异序列化为构件。`open_pr` 作业具有代码仓库写入权限，但不会获得 `OPENAI_API_KEY`。

此示例假定使用 Node.js 项目。请根据您的技术栈调整设置和测试命令。

如需更详细的安全检查清单，请参阅 [Codex GitHub Action 安全指南](https://github.com/openai/codex-action/blob/main/docs/security.md)。

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## 高级 stdin 管道传输

当其他命令为 Codex 生成输入时，请根据指令的来源选择 stdin 模式。如果您已经明确指令内容，并希望将通过管道传入的输出用作上下文，请使用 prompt-plus-stdin。如果 stdin 应作为完整提示，请使用 `codex exec -`。

### 使用 prompt-plus-stdin

当其他命令已经生成您希望 Codex 检查的数据时，Prompt-plus-stdin 非常实用。在此模式下，您自行编写指令，并通过管道将输出作为上下文传入，因此非常适合围绕命令输出、日志和生成的数据构建的 CLI 工作流。

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### 汇总日志

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### 排查 TLS 或 HTTP 问题

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### 准备可直接发布到 Slack 的更新

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### 根据 CI 日志起草 Pull Request 评论

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### stdin 用作提示时，使用 `codex exec -`

如果您省略提示参数，Codex 会从 stdin 读取提示。若要显式强制采用这一行为，请使用 `codex exec -`。

当其他命令或脚本动态生成完整提示时，`-` 哨兵标记非常实用。如果您将提示保存在文件中、使用 shell 脚本组装提示，或者先将实时命令输出与指令结合，再将完整提示交给 Codex，就很适合采用这种方式。

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
