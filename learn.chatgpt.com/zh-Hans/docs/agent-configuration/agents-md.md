<!-- source: https://learn.chatgpt.com/zh-Hans/docs/agent-configuration/agents-md -->

Codex 在执行任何工作前都会读取 `AGENTS.md` 文件。通过分层叠加全局指令和项目专用的覆盖指令，无论您打开哪个代码仓库，您在开始每项任务时对 Codex 行为的预期都能保持一致。

## Codex 如何查找指令

Codex 启动时会构建一条指令链（每次运行仅构建一次；在 TUI 中，这通常意味着每次启动会话时构建一次）。查找过程遵循以下优先顺序：

1. **全局范围：** 在您的 Codex 主目录中（默认为 `~/.codex`，除非您设置了 `CODEX_HOME`），如果 `AGENTS.override.md` 存在，Codex 会读取该文件。否则，Codex 会读取 `AGENTS.md`。在此层级，Codex 只使用按顺序找到的第一个非空文件。
2. **项目范围：** Codex 从项目根目录（通常为 Git 根目录）开始，沿目录树向下逐级检查，直至当前工作目录。如果 Codex 找不到项目根目录，则只检查当前目录。在沿途的每个目录中，它会依次检查 `AGENTS.override.md`、`AGENTS.md`，然后检查 `project_doc_fallback_filenames` 中列出的任意回退文件名。Codex 在每个目录中最多纳入一个文件。
3. **合并顺序：** Codex 从根目录开始向下拼接文件，并用空行分隔。由于更靠近当前目录的文件在合并后的提示词中出现得更晚，因此会覆盖之前的指令。

Codex 会跳过空文件；合并后的大小一旦达到 `project_doc_max_bytes` 定义的上限（默认为 32 KiB），就不再添加文件。有关这些配置项的详细信息，请参阅 [项目指令发现机制](/zh-Hans/codex/config-file/config-advanced#project-instructions-discovery)。达到上限时，请提高该上限，或将指令拆分到嵌套目录中。

## 创建全局指令

在您的 Codex 主目录中创建持久化的默认指令，让每个代码仓库都继承您的工作约定。

1. 确保该目录存在：

   ```bash
   mkdir -p ~/.codex

2. 创建 `~/.codex/AGENTS.md`，并在其中写入可复用的偏好设置：

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. 在任意位置运行 Codex，确认它会加载该文件：

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   预期结果：Codex 会先引用 `~/.codex/AGENTS.md` 中的条目，再提出工作方案。

如果需要临时进行全局覆盖，又不想删除基础文件，请使用 `~/.codex/AGENTS.override.md`。删除此覆盖文件即可恢复共享指令。

## 分层添加项目指令

代码仓库级文件可让 Codex 了解项目规范，同时仍会继承您的全局默认设置。

1. 在代码仓库根目录中添加 `AGENTS.md`，涵盖基本设置：

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. 当特定团队需要不同规则时，请在嵌套目录中添加覆盖文件。例如，在 `services/payments/` 中创建 `AGENTS.override.md`：

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. 从 payments 目录启动 Codex：

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   预期结果：Codex 会先报告全局文件，其次报告代码仓库根目录中的 `AGENTS.md`，最后报告 payments 目录的覆盖文件。

Codex 搜索到当前目录便会停止，因此应尽量将覆盖文件放在最接近相关专项工作的目录中。

以下是添加全局文件和 payments 专用覆盖文件后的代码仓库示例：

## 添加代码审查规则

对于 [GitHub 中的 Codex 代码审查](/zh-Hans/codex/third-party/github#customize-what-codex-reviews)，
请将 `## Code Review Rules` 部分添加到最靠近相关代码的 `AGENTS.md` 中，其中的
规则用于约束这些代码。请将代码仓库范围的检查放在根目录中，并将服务专属的
检查放在嵌套文件中。

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

规则应保持简洁，说明要标记的行为以及安全的处理方式或
例外情况，并将格式和 lint 检查留给 CI。请参阅 [自定义
Codex 的审查内容](/zh-Hans/codex/third-party/github#customize-what-codex-reviews)，了解
设置方法和规则编写指南。

## 自定义回退文件名

如果您的代码仓库已使用其他文件名（例如 `TEAM_GUIDE.md`），请将其添加到回退列表中，以便 Codex 将它视为指令文件。

1. 编辑您的 Codex 配置：

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. 重启 Codex 或运行新命令，以加载更新后的配置。

现在，Codex 会按以下顺序检查每个目录：`AGENTS.override.md`、`AGENTS.md`、`TEAM_GUIDE.md`、`.agents.md`。查找指令时，不在此列表中的文件名会被忽略。提高字节上限后，可以在截断前合并更多指令。

配置好回退列表后，Codex 会将备用文件视为指令：

如果您希望使用另一套配置（例如项目专用自动化用户的配置），请设置 `CODEX_HOME` 环境变量：

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

预期结果：输出会列出相对于自定义 `.codex` 目录的文件。

## 验证您的设置

- 在代码仓库根目录运行 `codex --ask-for-approval never "Summarize the current instructions."`。Codex 应按优先顺序回显全局文件和项目文件中的指令。
- 使用 `codex --cd subdir --ask-for-approval never "Show which instruction files are active."` 确认嵌套目录中的覆盖指令会取代范围更广的规则。
- 要核查 Codex 加载了哪些指令文件，请使用 `codex -c log_dir=./.codex-log` 启用纯文本 TUI 日志并检查 `./.codex-log/codex-tui.log`；如果已启用会话日志记录，也可以检查最新的 `session-*.jsonl` 文件。
- 如果指令看起来未更新，请在目标目录中重启 Codex。Codex 每次运行时（以及每个 TUI 会话开始时）都会重新构建指令链，因此无需手动清除缓存。

## 排查指令查找问题

- **未加载任何内容：** 确认您位于预期的代码仓库中，并且 `codex status` 报告的工作空间根目录符合预期。确保指令文件包含内容；Codex 会忽略空文件。
- **出现了错误的指令：** 请在目录树的上层或您的 Codex 主目录下查找 `AGENTS.override.md`。重命名或删除该覆盖文件，以恢复使用常规文件。
- **Codex 忽略回退文件名：** 请确认在 `project_doc_fallback_filenames` 中列出的名称均无拼写错误，然后重启 Codex，使更新后的配置生效。
- **指令被截断：** 请增大 `project_doc_max_bytes` 的值，或将大型文件拆分到多个嵌套目录中，以确保关键指令保持完整。
- **配置混淆：** 在启动 Codex 前运行 `echo $CODEX_HOME`。如果该值不是默认值，Codex 将使用另一个主目录，而不是您编辑的主目录。

## 后续步骤

- 请访问官方 [AGENTS.md](https://agents.md) 网站，了解更多信息。
- 请查阅 [Codex 提示词](/zh-Hans/codex/prompting)，了解适合与持久化指令搭配使用的对话模式。
