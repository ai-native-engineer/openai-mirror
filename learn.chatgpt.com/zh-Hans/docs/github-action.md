<!-- source: https://learn.chatgpt.com/zh-Hans/docs/github-action -->

使用 Codex GitHub Action（`openai/codex-action@v1`）在 CI/CD 作业中运行 Codex、应用补丁，或通过 GitHub Actions 工作流发布审查意见。
此 GitHub Action 会安装 Codex CLI，在您提供 API 密钥时启动 Responses API 代理，并使用您指定的权限运行 `codex exec`。

如需执行以下操作，请使用此 GitHub Action：

- 无需自行管理 CLI，即可让 Codex 自动为 Pull Request 或发布提供反馈。
- 将 Codex 驱动的质量检查纳入 CI 流水线，并据此决定是否允许更改通过。
- 通过工作流文件运行可重复执行的 Codex 任务（代码审查、发布准备、迁移）。

有关 CI 示例，请参阅 [非交互模式](/zh-Hans/codex/non-interactive-mode)，并前往 [openai/codex-action 代码仓库](https://github.com/openai/codex-action)，浏览其中的源代码。

## 前提条件

- 将您的 OpenAI 密钥存储为 GitHub 机密（例如 `OPENAI_API_KEY`），并在工作流中引用它。
- 在 Linux 或 macOS 运行器上运行作业。对于 Windows，请设置 `safety-strategy: unsafe`。
- 请先签出代码，再调用此 GitHub Action，以便 Codex 读取代码仓库内容。
- 确定要运行的提示。您可以通过 `prompt` 提供内联文本，也可以使用 `prompt-file` 指向代码仓库中已提交的文件。

## 示例工作流

下面的示例工作流会审查新的 Pull Request、获取 Codex 的响应，并将其发布到相应 PR 中。

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

将 `.github/codex/prompts/review.md` 替换为您自己的提示文件，或使用 `prompt` 输入来提供内联文本。该示例还会将 Codex 的最终消息写入 `codex-output.md`，以供后续检查或上传为工件。

## 配置 `codex exec`

通过设置与 `codex exec` 选项对应的 GitHub Action 输入，精细调整 Codex 的运行方式：

- `prompt` 或 `prompt-file`（选择其一）：提供内联任务指令，或提供代码仓库中包含任务内容的 Markdown 或文本文件路径。建议将提示存储在 `.github/codex/prompts/` 中。
- `codex-args`：额外的 CLI 标志。请提供 JSON 数组（例如 `["--ephemeral"]`）或 Shell 字符串（`--profile ci`），以配置会话、配置文件或 MCP 设置。
- `model` 和 `effort`：选择您需要的 Codex 智能体配置；留空则使用默认值。
- `sandbox`：根据 Codex 运行期间所需的权限选择合适的沙盒模式（`workspace-write`、`read-only`、`danger-full-access`）。
- `output-file`：将 Codex 的最终消息保存到磁盘，以便后续步骤上传或进行差异比较。
- `codex-version`：锁定特定的 CLI 版本。留空则使用最新发布的版本。
- `codex-home`：如果您想在不同步骤间复用配置文件或 MCP 设置，请指定共享的 Codex 主目录。

## 管理权限

如果您不加限制，Codex 在 GitHub 托管的运行器上拥有广泛的访问权限。请使用以下输入控制其访问范围：

- `safety-strategy`（默认为 `drop-sudo`）会在运行 Codex 前移除 `sudo`。此操作对该作业不可逆，并可保护内存中的机密信息。在 Windows 上，您必须设置 `safety-strategy: unsafe`。
- `unprivileged-user` 会将 `safety-strategy: unprivileged-user` 与 `codex-user` 配合使用，以特定账户运行 Codex。请确保该用户能够读写代码仓库的签出目录（有关修复所有权问题的方法，请参阅 [`unprivileged-user` 示例](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml)）。
- `read-only` 可阻止 Codex 修改文件或使用网络，但 Codex 运行时仍具有提升的权限。不要仅依赖 `read-only` 来保护机密信息。
- `sandbox` 会限制 Codex 本身对文件系统和网络的访问。请选择权限范围最小、但仍能完成任务的选项。
- `allow-users` 和 `allow-bots` 会限制可触发工作流的账户。默认情况下，只有具备写入权限的用户才能运行此 GitHub Action；请明确列出其他受信任账户，或将此字段留空以采用默认行为。

## 捕获输出

此 GitHub Action 会通过 `final-message` 输出提供 Codex 的最后一条消息。您可以将其映射到作业输出（如上所示），也可以在后续步骤中直接处理。如果希望从运行器收集完整的运行记录，可将 `output-file` 与工件上传功能结合使用。需要结构化数据时，请通过 `codex-args` 传入 `--output-schema`，以强制输出符合指定的 JSON 结构。

## 安全检查清单

- 限制可启动工作流的人员。应优先使用受信任的事件或显式审批，而不是允许所有人针对您的代码仓库运行 Codex。
- 对来自 Pull Request、提交消息或议题正文的提示输入进行清理，以避免提示注入。在将 HTML 注释或隐藏文本提供给 Codex 前，请先审查这些内容。
- 通过将 `safety-strategy` 保持为 `drop-sudo`，或让 Codex 以非特权用户身份运行，来保护您的 `OPENAI_API_KEY`。切勿让此 GitHub Action 在多租户运行器上保持 `unsafe` 模式。
- 让 Codex 在作业的最后一个步骤运行，以免后续步骤继承任何非预期的状态更改。
- 如果您怀疑代理日志或 GitHub Action 输出泄露了机密信息，请立即轮换密钥。

## 故障排除

- **您同时设置了 prompt 和 prompt-file**：移除重复的输入，确保只提供一个输入来源。
- **responses-api-proxy 未写入服务器信息**：请确认 API 密钥存在且有效；仅当您提供 `openai-api-key` 时，代理才会启动。
- **原本应移除 `sudo`，但 `sudo` 仍执行成功**：请确保此前没有任何步骤恢复 `sudo`，并且运行器操作系统为 Linux 或 macOS。请使用全新作业重新运行。
- **使用 `drop-sudo` 后出现权限错误**：请在此 GitHub Action 运行前授予写入权限（例如使用 `chmod -R g+rwX "$GITHUB_WORKSPACE"`，或采用 unprivileged-user 模式）。
- **未授权的触发请求被阻止**：如果您需要允许默认具有写入权限的协作者之外的服务账户，请调整 `allow-users` 或 `allow-bots` 输入。
