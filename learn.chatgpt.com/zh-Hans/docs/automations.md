<!-- source: https://learn.chatgpt.com/zh-Hans/docs/automations -->

安排定期任务，让它们在后台运行。在网页版和移动版 ChatGPT 中，
符合条件的套餐还支持通过受支持的应用事件触发任务。
您可以在“ **计划任务**”中查看已启用、已暂停和已完成的任务，以及最近的运行记录。您还可以将
计划任务与[技能](/zh-Hans/codex/build-skills)结合使用，完成更复杂的工作。

在 ChatGPT 桌面应用中，计划任务可以处理本地项目，
并在项目目录或隔离的工作树中运行。当计划任务需要本地文件时，请保持计算机开机，
并让应用持续运行。

如果您的工作空间已启用计划任务，您可以在 Web 上通过“聊天”或
ChatGPT Work 创建任务，并在“ **计划任务**”中管理其运行。Web 任务
可以使用已上传的上下文和已连接的工具，但无法直接在
您计算机上的文件夹中工作。

Codex CLI 不提供“计划任务”管理界面。请使用网页版 ChatGPT
或桌面应用创建和管理计划任务。您可以先使用 CLI
准备并测试提示、技能或脚本。

IDE 扩展不提供“计划任务”管理界面。
请使用网页版 ChatGPT 或桌面应用创建和管理计划任务。
您可以先通过 IDE 扩展准备并测试提示、技能
或工作空间更改。

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## 在 Web 上管理计划任务

打开“ **计划任务** ”，查看任务状态和最近的运行记录。如果每次运行都应从保存的提示开始，
请使用独立的计划任务。如果您希望 ChatGPT 返回同一聊天，
并沿用该聊天的现有上下文，
请在该聊天中使用计划任务。

Web 上的计划任务可以使用该聊天中可用的已上传文件、已连接的工具、技能和
插件。它们不会在各次运行之间保留可用的本地文件夹或
工作树。请将长期有效的指令写入任务提示
或附加的技能中，并将所需源材料保存在可访问的
项目、上传内容或已连接的服务中。

安排任务前，请先在常规 Web 聊天中测试其提示。
检查前几次运行，如果结果范围过于宽泛或需要更多上下文，
请调整提示、工具或运行频率。

## 通过应用事件触发任务

如果您使用的套餐符合条件，计划任务可在受支持的 Gmail、Slack 或
GitHub 事件发生时运行。事件触发的任务可在网页版和移动版 ChatGPT 中使用，
但无法在 ChatGPT 桌面应用、Codex CLI 或
IDE 扩展中使用。

请让 ChatGPT 创建任务，然后说明要监测的事件及其发生时
应执行的操作。触发条件决定任务何时运行；已保存的
提示决定每次运行执行的内容。一个任务可以使用多个事件触发条件，
但不能将事件触发条件与定时计划结合使用。

支持的事件触发条件包括：

- **Gmail：** 新收到的邮件，可按发件人或主题筛选。
- **Slack：** 所选频道中的新消息，可按发送者
  筛选，并选择是否包含话题回复。不支持表情回应、消息编辑、消息删除和
  私信。
- **GitHub：** 代码仓库中的 Pull Request 活动。可按 Pull Request、
  作者、标题或标签筛选，并选择任务是在审查、评论、提交更新时触发，
  还是仅在合并时触发。

创建任务前，请先连接应用并完成授权。对于 Slack，请将
`@ChatGPT` 添加到任务监测的每个频道中。对于 GitHub，已连接的应用
必须有权访问相应的代码仓库。

当多个符合条件的事件在短时间内接连到达时，ChatGPT 可能会将它们
合并到一次运行中处理。打开“ **计划任务** ”可查看待处理事件，或选择“ **立即运行**”
来处理这些事件。

能否使用此功能取决于您的套餐和工作空间设置。在受管理的
工作空间中，管理员可以通过“ **允许事件触发的
计划任务** ”权限控制访问。

例如，您可以安排任务来评估遥测错误并提交修复，
或生成有关代码库近期更改的报告。对于需要持续使用相同上下文的工作，
请[在现有聊天中安排任务](#schedule-a-task-inside-a-chat)。

对于项目范围内的计划任务，请保持计算机开机，
并让 ChatGPT 桌面应用持续运行。在任务的预定运行时间，
所选项目必须仍可从磁盘访问。

在 Git 代码仓库中，您可以选择让计划任务在本地
项目中运行，或在新的[工作树](/zh-Hans/codex/environments/git-worktrees)中运行。两种方式都在
后台运行。工作树会将计划任务所做的更改与尚未完成的本地
工作隔离，而在本地项目中运行可能会修改您仍在
处理的文件。在未使用版本控制的项目中，计划任务会直接在
项目目录中运行。

您也可以使用默认的模型和推理强度设置；如果希望更精细地控制计划任务的运行方式，
也可以自行指定这两项设置。

如果计划任务通过 ChatGPT 登录使用 `gpt-5.4` 或 `gpt-5.4-mini`，
请在这些模型于 2026 年 8 月 31 日停用前更新任务。将 `gpt-5.4` 替换为
`gpt-5.6-terra`，并将 `gpt-5.4-mini` 替换为 `gpt-5.6-luna`。

  

计划任务会在无人值守的情况下运行，并使用您的默认沙盒设置。请先授予能让任务成功完成的
最小访问权限，仅在需要时才授予网络访问权限或更广泛的文件
访问权限。[了解沙盒](/zh-Hans/codex/sandboxing)。

## 管理计划任务

在 ChatGPT 桌面应用侧边栏的“ **计划任务** ”中，
您可以查看所有计划任务及其运行记录。

“ **计划任务** ”视图相当于您的收件箱。包含发现结果的计划任务运行记录
会显示在这里；某次运行需要您关注时，会显示未读标记。

  

独立的计划任务会为每次计划运行开启新聊天，并在
“ **计划任务**”中显示结果。如果每次运行都应相互独立，或同一
计划任务需要在一个或多个项目中运行，请使用独立的计划任务。如果需要自定义
运行频率，请使用自定义计划控件。如需设置高级运行计划，请编辑其
RFC 5545 重复规则（RRULE），例如
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0`。

对于 Git 代码仓库，每个计划任务都可以在本地项目中运行，或
在专用的后台[工作树](/zh-Hans/codex/environments/git-worktrees)中运行。如果您希望
将计划任务的更改与尚未完成的本地工作隔离，
请使用工作树。如果您希望计划任务直接在主检出目录中工作，
请使用本地模式，但请注意，它可能会更改您正在编辑的文件。
在未使用版本控制的项目中，计划任务会直接在项目
目录中运行。您可以让同一个计划任务在多个项目中运行。

在 Web 上通过 ChatGPT Work 创建的计划任务，或在桌面应用中通过 ChatGPT Work 或
Codex 创建的计划任务，都可以使用插件。计划任务也可以使用技能。
为了便于维护计划任务并在团队间共享，请使用
[技能](/zh-Hans/codex/build-skills)来定义操作，并提供工具和上下文。
如果工作流程不应依赖自动选择工具，
请在任务提示中选择或调用特定技能。

## 让 ChatGPT 创建或更新计划任务

您可以在 ChatGPT 或 Codex 聊天中创建和更新计划任务。
请说明工作内容、运行时间，以及每次运行应返回
当前聊天还是开启新聊天。ChatGPT 可以起草提示、选择
合适的目标位置，并在任务范围或运行频率
发生变化时更新任务。

例如，您可以让 ChatGPT 在等待部署完成期间，从当前聊天中安排
一次后续跟进；也可以让它创建一个独立的计划任务，定期检查
某个项目。

技能也可以创建或更新计划任务。例如，用于
持续跟进 Pull Request 的技能可以设置一个计划任务，通过
GitHub 插件检查 PR 状态，并根据新的审查反馈进行修复。

## 在聊天中安排任务

如果您希望 ChatGPT 按计划返回某个现有聊天，请在该聊天中安排任务。
计划任务会使用该聊天的现有上下文，
而不是每次都从新提示开始。

聊天中的计划任务可以按分钟间隔运行，用于持续跟进；
如果您需要在特定时间检查，也可以设置每天或每周的
运行计划。

您可以在聊天中安排任务，用于：

- 持续检查长时间运行的操作，直至其完成
- 当您需要定期获取快照，而不是响应某个受支持的应用事件时，按固定频率
检查已连接的来源
- 提醒 ChatGPT 按固定频率继续审查循环
- 运行由技能驱动且使用插件的工作流程，例如检查 PR 状态
并处理新的反馈
- 在不丢失上下文的情况下，继续当前的研究或问题分类聊天

如果每次运行都应相互独立，或
发现结果应在“ **计划任务**”中作为单独运行显示，请使用独立的计划任务。

在聊天中安排任务时，请确保提示能长期适用。提示应说明
ChatGPT 在每次计划运行时应执行的操作、如何判断是否有
重要信息需要报告，以及何时停止或请求您提供信息。

## 测试计划任务

安排任务前，请先在常规聊天中
手动测试提示。这有助于确认：

- 提示清晰，范围设定正确。
- 所选或默认的模型、推理强度和工具均按预期运行。
- 生成的输出便于审查。

任务开始按计划运行后，请审查前几次输出，并根据需要调整
提示或运行频率。

在 ChatGPT 桌面应用中，您可以在计划任务的提示中
使用 `$skill-name` 显式触发某项技能。

## 清理计划任务的工作树

如果您为 Git 代码仓库选择工作树，频繁运行计划任务可能会逐渐创建
大量工作树。请归档不再需要的计划任务运行记录；除非您打算保留相应的工作树，否则不要
固定这些运行记录。

## 权限和安全模型

计划任务会在无人值守的情况下运行，并使用您的默认沙盒设置。

有关这些边界的通俗说明，请参阅
[沙盒概览](/zh-Hans/codex/sandboxing)。有关文件系统和网络规则，
请参阅[权限](/zh-Hans/codex/permissions)。

- 如果您的沙盒模式为 **只读**，工具调用若需要
  修改文件、访问网络或使用您计算机上的应用，就会失败。
  您可以考虑将沙盒设置更改为“工作空间可写”。
- 如果您的沙盒模式为 **workspace-write**，工具调用若需要
  修改工作空间以外的文件、访问网络或使用您计算机上的应用，
  就会失败。您可以通过
  [规则](/zh-Hans/codex/agent-configuration/rules)有选择地将命令加入允许列表，使其能够在沙盒外运行。
- 如果您的沙盒模式为 **完全访问权限**，后台计划任务存在
  较高风险，因为 ChatGPT 可能在不询问您的情况下修改文件、运行命令
  和访问网络。您可以考虑将沙盒设置更改为“工作空间可写”，并
  使用[规则](/zh-Hans/codex/agent-configuration/rules)，有选择地指定智能体
  可以在完全访问权限下运行的命令。

如果您处于受管理的环境中，管理员可以通过
强制要求来限制这些行为。例如，他们可以禁止使用 `approval_policy =
"never"`，或限制允许使用的沙盒模式。请参阅
[管理员强制要求（`requirements.toml`）](/zh-Hans/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

在您的组织策略允许的情况下，计划任务会使用 `approval_policy = "never"`。
如果管理员的要求禁止使用 `approval_policy = "never"`，
计划任务会回退到您所选权限模式的
审批行为。

## 示例

### 自动创建新技能

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### 及时了解您的项目动态

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### 结合计划任务和技能，修复您自己引入的错误

创建一项名为 `$recent-code-bugfix` 的新技能，用于尝试修复您自己的提交引入的错误，并[将其保存在您的个人技能中](/zh-Hans/codex/build-skills#where-to-save-skills)。

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

然后，创建一个新的计划任务：

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.
