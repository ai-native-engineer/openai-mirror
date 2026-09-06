<!-- source: https://learn.chatgpt.com/zh-Hans/docs/long-running-work -->

对于可能需要多个步骤的工作，请向 ChatGPT 明确说明预期结果、约束条件，
以及完成标准。将相关工作保留在同一聊天中，
以便 ChatGPT 使用相同的上下文确定下一步，
并判断工作何时完成。

在 ChatGPT 桌面应用中输入 `/goal`，启动目标模式。ChatGPT 工作期间，您可以通过进度栏
暂停、恢复、编辑或清除目标。

对于在 ChatGPT 网页版中托管的长时间运行工作，请使用 ChatGPT Work，
并在提示词中直接说明预期结果、约束条件和审查标准。

继续在同一个网页聊天中添加上下文、调整约束条件，或
请求状态更新。当独立任务可以
并行运行时，请使用不同的聊天，并避免向两个任务授予对同一已连接源的写入权限。
对于相关工作，请将聊天和源文件归入同一个
[项目](/zh-Hans/codex/projects)。

在 Codex CLI 交互式会话中输入 `/goal`，启动目标模式。继续
在同一会话中调整工作方向，或请求状态更新。

在 IDE 扩展的聊天中输入 `/goal`，为已打开的
工作空间启动目标模式。任务运行期间，请继续在同一聊天中调整任务方向。

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## 启动目标

在 ChatGPT 桌面应用、Codex CLI 或 IDE 扩展中输入 `/goal`。
目标文本既是首条提示词，也是
任务的完成标准。

如果预期结果仍不明确，请先使用 `/plan`。让 ChatGPT 通过提问了解您的需求，
明确约束条件，并将结果转化为包含可衡量成功
标准的目标。然后使用 `/goal` 启动完善后的目标。

## 明确完成标准

编写一个让 ChatGPT 能够自行验证进度的目标。在适用的情况下，
请包含以下三项内容：

| 目标要素     | 应包含的内容                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **预期结果**      | 描述您想要的结果，而不只是 ChatGPT 应执行的操作。   |
| **约束条件**  | 说明所需工具、边界、兼容性要求或应避免的方法。 |
| **验证** | 添加可证明工作已完成的测试、衡量指标或审查标准。  |

例如：

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## 调整运行中的目标

在 ChatGPT 桌面应用中，目标进度栏显示在编辑器上方。您可以使用它来
暂停或恢复工作、编辑目标，或清除目标。目标运行期间，您也可以发送后续消息，
以添加上下文或调整约束条件。

如果您想在不中断主聊天的情况下了解状态摘要或获取说明，
请使用侧边聊天。在预计连接中断之前，请先暂停
目标；准备好让 ChatGPT 继续时，再恢复目标。

<a id="steer-a-running-task"></a>

## 调整运行中的工作

继续在同一聊天中添加上下文、调整约束条件，或请求
状态摘要。如果另一项任务可以
独立运行，请另开一个聊天。

## 调整运行中的目标

在同一交互式会话中发送后续消息，以添加上下文或
调整约束条件。如果您希望 Codex 在继续之前总结
进度，请请求状态摘要。

## 调整运行中的目标

继续在同一个 IDE 聊天中添加上下文、调整约束条件，或请求
状态摘要。目标运行期间，请确保工作空间保持可用。

启动目标不会赋予 ChatGPT 更广泛的访问权限。ChatGPT 仍受相同的
[沙盒和审批策略](/zh-Hans/codex/sandboxing)约束，并在
需要做出决策时暂停。通过[自动审批
审查](/zh-Hans/codex/sandboxing/auto-review)，独立的审查者可以
在不扩大这些边界的情况下评估符合条件的请求。

## 并行运行目标

每个聊天都保留各自的上下文、消息、结果和目标。您可以让多个聊天
并行运行，但应避免两个聊天修改相同的文件。请使用
[工作树](/zh-Hans/codex/environments/git-worktrees)，为并行的编程聊天提供独立的
代码检出目录。

进行本地工作时，请在设置中开启 **运行时防止睡眠** ，让 Mac
保持唤醒。通过[宠物](/zh-Hans/codex/pets?surface=app)或[系统
通知](/zh-Hans/codex/notifications?surface=app)，了解聊天何时需要您输入内容，
或何时已可供审查。

## 相关文档

- [项目和聊天](/zh-Hans/codex/projects)
- [目标模式和提示词](/zh-Hans/codex/prompting#goal-mode)
- [Git 工作树](/zh-Hans/codex/environments/git-worktrees)

## 相关文档

- [项目和聊天](/zh-Hans/codex/projects)
- [计划任务](/zh-Hans/codex/automations)
- [沙盒和权限](/zh-Hans/codex/sandboxing)
