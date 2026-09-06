<!-- source: https://learn.chatgpt.com/zh-Hans/docs/agent-configuration/rules -->

使用规则控制 Codex 可以在沙盒外运行哪些命令。

规则尚处于实验阶段，可能会发生变化。

## 创建规则文件

1. 创建一个 `.rules` 文件，并将它放入生效配置层旁的 `rules/` 文件夹中（例如 `~/.codex/rules/default.rules`）。
2. 添加一条规则。此示例会在允许 `gh pr view` 在沙盒外运行前提示您。

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. 重启 Codex。

Codex 会在启动时扫描每个生效配置层下的 `rules/`，包括[团队配置](/zh-Hans/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config)位置以及位于 `~/.codex/rules/` 的用户层。位于 `<repo>/.codex/rules/` 下的项目本地规则仅在项目的 `.codex/` 层受信任时加载。

当您在 TUI 中将命令添加到允许列表时，Codex 会将其写入位于 `~/.codex/rules/default.rules` 的用户层，以便后续运行时跳过提示。

启用智能审批（默认设置）后，Codex 可能会在权限提升请求期间向您建议一条
`prefix_rule`。接受前，请先对建议的前缀
进行仔细审查。

管理员还可以强制执行限制性的 `prefix_rule` 条目，这些条目来自
[`requirements.toml`](/zh-Hans/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

## 了解规则字段

`prefix_rule()` 支持以下字段：

- `pattern` **（必填）**：用于定义待匹配命令前缀的非空列表。每个元素可以是以下任一种：
  - 字面量字符串（例如 `"pr"`）。
  - 字面量的联合（例如 `["view", "list"]`），用于匹配该参数位置上的多个备选项。
- `decision` **（默认为 `"allow"`）**：规则匹配时采取的操作。多条规则同时匹配时，Codex 会采用限制最严格的处理方式（`forbidden` \> `prompt` \> `allow`）。
  - `allow`：无需提示，直接在沙盒外运行命令。
  - `prompt`：每次匹配的调用前都提示您。
  - `forbidden`：不提示您，直接阻止请求。
- `justification` **（可选）**：一条非空且便于理解的规则理由。Codex 可能会在审批提示或拒绝消息中显示该理由。当您使用 `forbidden` 时，请酌情在理由中提供建议的替代方案（例如，`"Use \`rg\`，而非 \`grep\`。”\`）。
- `match` 和 `not_match` **（默认为 `[]`）**：供 Codex 在加载您的规则时验证的示例。使用这些示例可在规则生效前发现错误。

当 Codex 考虑运行某个命令时，会将该命令的参数列表与 `pattern` 进行比较。在内部实现中，Codex 将该命令视为参数列表（类似于 `execvp(3)` 接收的内容）。

## Shell 包装器和复合命令

有些工具会将多个 Shell 命令封装到一次调用中，例如：

```text
["bash", "-lc", "git add . && rm -rf /"]

由于此类命令可以在一个字符串中隐藏多个操作，Codex 会对 `bash -lc`、`bash -c` 以及它们在 `zsh` / `sh` 中的对应形式进行特殊处理。

### Codex 可以安全拆分脚本时

如果该 Shell 脚本是一条仅由以下内容构成的线性命令链：

- 普通单词（不含变量展开，也不含 `VAR=...`、`$FOO`、`*` 等）
- 由安全运算符（`&&`、`||`、`;` 或 `|`）连接

那么，Codex 会使用 tree-sitter 解析该脚本，并在应用您的规则前将其拆分为单独的命令。

上述脚本会被视为两个独立命令：

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

然后，Codex 会依据您的规则评估每个命令，并采用限制最严格的结果。

即使您已允许 `pattern=["git", "add"]`，Codex 也不会自动允许 `git add . && rm -rf /`，因为其中的 `rm -rf /` 部分会被单独评估，从而阻止整个调用被自动允许。

这样可以防止将危险命令夹带在安全命令中。

### Codex 不拆分脚本时

如果脚本使用更高级的 Shell 功能，例如：

- 重定向（`>`、`>>`、`<`）
- 命令替换（`$(...)`、`...`）
- 环境变量（`FOO=bar`）
- 通配符模式（`*`、`?`）
- 控制流（`if`、`for`、带有赋值的 `&&` 等）

那么，Codex 不会尝试解释或拆分它。

在这些情况下，整个调用会被视为：

```text
["bash", "-lc", "<full script>"]

并且您的规则会应用于该**单次**调用。

采用这种处理方式后，系统会在可以安全拆分脚本时逐命令评估，以保障安全；无法安全拆分时，则采取保守处理。

## 测试规则文件

使用 `codex execpolicy check` 测试您的规则如何应用于某个命令：

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

该命令会输出 JSON，其中显示限制最严格的处理方式和所有匹配规则，包括匹配规则中的所有 `justification` 值。使用多个 `--rules` 标志可合并文件，并添加 `--pretty` 以格式化输出。

## 了解规则语言

`.rules` 文件格式使用 `Starlark`（请参阅[语言规范](https://github.com/bazelbuild/starlark/blob/master/spec.md)）。其语法类似 Python，但专为安全运行而设计：规则引擎运行它时不会产生副作用（例如，不会改动文件系统）。
