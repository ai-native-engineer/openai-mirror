<!-- source: https://learn.chatgpt.com/zh-Hans/docs/custom-prompts -->

自定义提示已弃用。请使用 [技能](/zh-Hans/codex/build-skills) 创建 Codex 可显式或隐式调用的可复用
  指令。

自定义提示（已弃用）可让您将 Markdown 文件转换为可复用提示，并在 Codex CLI 和 Codex IDE 扩展中以斜杠命令的形式调用这些提示。

自定义提示需要显式调用，并存放在您本地的 Codex 主目录中（例如 `~/.codex`），因此不会通过您的代码仓库共享。如果您想共享某个提示（或希望 Codex 隐式调用它），请 [使用技能](/zh-Hans/codex/build-skills)。

1. 创建提示目录：

   ```bash
   mkdir -p ~/.codex/prompts

2. 创建 `~/.codex/prompts/draftpr.md` 并写入可复用指令：

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. 重启 Codex，使其加载新提示（重启您的 CLI 会话；如果您正在使用 IDE 扩展，还需重新加载该扩展）。

预期结果：在斜杠命令菜单中输入 `/prompts:draftpr` 后，您的自定义命令会连同前置元数据中的描述一起显示，并提示文件和 PR 标题均为可选项。

## 添加元数据和参数

下一次启动会话时，Codex 会读取提示元数据并解析占位符。

- **描述：** 显示在弹出窗口中的命令名称下方。请在 YAML 前置元数据中将其设为 `description:`。
- **参数提示：** 使用 `argument-hint: KEY=<value>` 指明预期参数。
- **位置占位符：** `$1` 到 `$9` 会依次展开为您在命令后提供的、以空格分隔的参数。`$ARGUMENTS` 包含所有这些参数。
- **命名占位符：** 使用 `$FILE` 或 `$TICKET_ID` 之类的全大写名称，并以 `KEY=value` 的形式提供值。对于包含空格的值，请用引号括起来（例如 `FOCUS="loading state"`）。
- **美元符号字面量：** 写入 `$$` 可在展开后的提示中输出一个 `$`。

编辑提示文件后，请重启 Codex 或新建聊天以加载更新。Codex 会忽略提示目录中的非 Markdown 文件。

## 调用和管理自定义命令

1. 在 Codex（CLI 或 IDE 扩展）中，输入 `/` 以打开斜杠命令菜单。
2. 输入 `prompts:` 或提示名称，例如 `/prompts:draftpr`。
3. 提供所需参数：

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. 按 Enter 键发送展开后的指令（不需要某个参数时，可将其省略）。

预期结果：Codex 会展开 `draftpr.md` 的内容，将占位符替换为您提供的参数，然后将结果作为消息发送。

您可以通过编辑或删除 `~/.codex/prompts/` 下的文件来管理提示。Codex 只会扫描该文件夹顶层的 Markdown 文件，因此请将每个自定义提示直接放在 `~/.codex/prompts/` 下，而不是放在子目录中。
