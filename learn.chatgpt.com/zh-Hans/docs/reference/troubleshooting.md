<!-- source: https://learn.chatgpt.com/zh-Hans/docs/reference/troubleshooting -->

## 常见问题

### 侧边面板中显示了 Codex 未编辑的文件

如果您的项目位于 Git 代码仓库中，审查面板会根据项目的 Git 状态自动
显示更改，其中也包括并非 Codex
所做的更改。

在审查窗格中，您可以在已暂存的更改与尚未
暂存的更改之间切换，还可将您的分支与 main 进行比较。

如果只想查看 Codex 上一轮产生的更改，请将差异
窗格切换到 **上一轮** 视图。

[进一步了解如何使用审查窗格](/zh-Hans/codex/code-review?surface=app)。

### 从侧边栏移除项目

要从侧边栏移除项目，请将鼠标悬停在项目名称上，点击
三个点，然后选择“移除”。要恢复该项目，请使用
**添加新项目** 按钮（位于 **聊天** 旁边）重新添加，也可以使用

<kbd>Cmd</kbd>+<kbd>O</kbd>。

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### 查找已归档的聊天

您可以在 [设置](codex://settings) 中找到已归档的聊天。取消归档
某个聊天后，它会重新出现在侧边栏中的原始位置。

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### 侧边栏中只显示部分聊天

您可以在侧边栏中根据项目状态筛选聊天。如果有聊天
未显示，请选择 **聊天** 旁边的筛选图标，然后选择
**按时间顺序**。如果仍未看到该聊天，请打开
[设置](codex://settings)，然后查看 **已归档的聊天**。

### 代码无法在工作树中运行

工作树会创建在其他目录中，并默认继承已提交到
Git 的文件。根据您管理项目
依赖项和工具的方式，您可能需要通过
[本地环境](/zh-Hans/codex/environments/local-environment) 在工作树中运行设置脚本，或复制被忽略的设置文件，
具体可使用 [`.worktreeinclude`](/zh-Hans/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees)。
或者，您可以在常规本地项目中签出这些更改。如需了解详情，请参阅
[工作树文档](/zh-Hans/codex/environments/git-worktrees)。

### App 未识别团队成员共享的本地环境

本地环境配置必须位于项目根目录下的 `.codex` 文件夹中。
如果您使用的单体代码仓库包含多个
项目，请确保在包含
`.codex` 文件夹的目录中打开项目。

### Codex 请求访问 Apple Music

根据任务需求，Codex 可能需要浏览文件系统。macOS 上的某些
目录（包括“音乐”“下载”或“桌面”）需要
用户额外审批。如果 Codex 需要读取您的主目录，
macOS 会提示您批准访问这些文件夹。

<a id="automations-create-many-worktrees"></a>

### 计划任务会创建许多工作树

频繁运行的计划任务会随着时间推移创建许多工作树。请归档不再需要的计划
运行；除非您打算保留这些运行的
工作树，否则请勿固定它们。

### 选择错误目标后恢复提示

如果您不小心选择了错误的目标（**本地**、**工作树** 或 **云端**）并开始了聊天，可以取消当前运行，然后在编辑器中按向上箭头键恢复之前的提示。

### 功能可在 Codex CLI 中使用，但无法在 ChatGPT 桌面 App 中使用

ChatGPT 桌面 App 和 Codex CLI 可能使用不同版本的 Codex，因此
功能可能先在其中一端推出。实验性功能也可能
率先在 Codex CLI 中推出。

要查看您系统上的 Codex CLI 版本，请运行：

```bash
codex --version

要查看 ChatGPT 桌面 App 内置的 Codex 版本，请使用
保留的 `Codex.app` 兼容包路径：

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## 反馈和日志

在消息输入框中键入 <kbd>/</kbd>，即可向团队提供反馈。如果
您在现有聊天中发起反馈，可以选择将
现有会话与反馈一并共享。提交反馈后，
您会收到可与团队共享的会话 ID。

要报告问题：

1. 在 Codex GitHub 代码仓库中查找 [现有议题](https://github.com/openai/codex/issues)。
2. [新建 GitHub 议题](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

可在以下位置找到更多日志：

- App 日志（macOS）： `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- 会话记录： `$CODEX_HOME/sessions`（默认： `~/.codex/sessions`）
- 已归档会话： `$CODEX_HOME/archived_sessions`（默认： `~/.codex/archived_sessions`）

如果您要共享日志，请先检查并确认其中不含敏感
信息。

## 卡住状态及恢复方法

如果聊天似乎卡住了：

1. 检查 Codex 是否正在等待审批。
2. 打开终端并运行一条基本命令，例如 `git status`。
3. 使用范围更小、重点更明确的提示开始新对话。

如果您误取消创建工作树并丢失了提示，请在编辑器中按
向上箭头键将其恢复。

## 终端问题

**终端似乎卡住了**

1. 关闭终端面板。
2. 按 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 将其重新打开。
3. 重新运行一条基本命令，例如 `pwd` 或 `git status`。

如果命令的行为与预期不符，请先在终端中确认当前目录和
分支。

如果仍然卡住，请等待当前进行中的聊天全部完成，然后重启 App。

**字体未正确渲染**

Codex 的审查窗格、集成终端以及 App 内显示的其他所有代码均使用同一种字体。您可以在 [设置](codex://settings) 窗格的 **代码字体** 项中配置该字体。
