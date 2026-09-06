<!-- source: https://learn.chatgpt.com/zh-Hans/docs/cli-customization -->

Codex CLI 提供终端专用选项，用于控制交互式会话
的呈现方式，以及您输入命令和提示的方式。

## 语法高亮与主题

终端 UI（TUI）会对 Markdown 围栏代码块和文件
差异进行语法高亮。运行 `/theme` 可打开主题选择器、预览主题，并将您的
选择保存至 `$CODEX_HOME/config.toml` 中的 `tui.theme` 配置项。

若要添加自定义主题，请将 `.tmTheme` 文件放入 `$CODEX_HOME/themes`，然后
在主题选择器中选择该主题。

## Shell 补全

为 Bash、Z shell、Fish 或 PowerShell 生成补全脚本：

```bash
codex completion zsh

从您的 Shell 配置中加载该脚本。对于 Z shell，请添加：

```bash
eval "$(codex completion zsh)"

如果 Z shell 报告 `command not found: compdef`，请先初始化其补全系统，
然后再加载 Codex 补全脚本：

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

重新启动 Shell，输入 `codex`，然后按 <kbd>Tab</kbd> 键，验证补全是否正常。

## 提示编辑器

对于较长的提示，请在编辑器中按 <kbd>Ctrl</kbd>+<kbd>G</kbd>，以打开
由 `VISUAL` 配置的外部编辑器；如果未设置 `VISUAL`，则改用 `EDITOR` 配置的外部编辑器。保存
并关闭外部编辑器，即可将文本返回到编辑器中，然后再发送。

有关交互式键盘操作以及完整的命令和选项列表，请参阅
[命令](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)。
