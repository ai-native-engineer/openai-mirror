<!-- source: https://learn.chatgpt.com/zh-Hans/docs/third-party/github -->

使用 Codex 代码审查，对 GitHub Pull Request 再进行一轮高价值审查。Codex 会审查 Pull Request 差异，遵循您的代码仓库指南，并发布标准的 GitHub 代码审查，重点关注严重问题。安全审查目前以研究预览版提供，可对 Pull Request 中潜在的安全问题进行更深入的审查。

<br />

## 开始前

请确保满足以下条件：

- 已为您要审查的代码仓库设置 [Codex 云端](/zh-Hans/codex/cloud)。
- 能够访问 [Codex 代码审查设置](https://chatgpt.com/codex/settings/code-review)。
- 如果您希望 Codex 遵循代码仓库专用的审查指南，请准备一个 `AGENTS.md` 文件。

## 设置 Codex 代码审查

要配置自动审查，您需要一个已连接的 GitHub 代码仓库，并拥有管理其设置所需的 GitHub 推送权限或管理员权限。

1. 设置 [Codex 云端](/zh-Hans/codex/cloud)。
2. 前往 [Codex 设置](https://chatgpt.com/codex/settings/code-review)。
3. 为您的代码仓库开启 **代码审查** 。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 请求 Codex 审查

1. 在 Pull Request 评论中提及 `@codex review`。
2. 等待 Codex 添加表情回应（👀），并发布审查结果。

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex 会像团队成员一样在 Pull Request 上发布审查结果。在 GitHub 中，Codex 仅标记 P0 和 P1 问题，使审查评论聚焦于高优先级风险。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 启用自动审查

如果您希望 Codex 自动审查每个 Pull Request，请开启
**自动审查** ，该选项位于 [Codex 设置](https://chatgpt.com/codex/settings/code-review)中。
每当有人创建新的待审查 PR 时，Codex 都会发布审查结果，无需
添加 `@codex review` 评论。

## 自定义 Codex 的审查内容

Codex 会在您的代码仓库中查找 `AGENTS.md` 文件，并遵循适用的
代码审查规则。请在最靠近规则适用代码的文件中添加 `## Code Review Rules` 部分。
如有需要，可使用 `###` 标题
对相关检查进行分组。

例如，实验报告服务可以防止曝光后的行为改变比较队列：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

将适用于整个代码仓库的规则写入根目录的 `AGENTS.md`，并将特定服务的规则
写入嵌套文件，例如 `services/experiment_reporting/AGENTS.md`。Codex 会
针对每个已更改的文件，应用根目录的指南和适用范围更具体的指南，因此
无关变更无需包含特定服务的上下文。

先制定两三条简洁的规则，将审查人员经常说明的检查要求纳入其中。实用的规则应满足以下几点：

- **重点关注影响重大且特定于代码仓库的行为。** 说明需要标记的
  兼容性约束、数据边界或不安全的副作用，并解释
  其重要性。
- **说明安全的处理方式或例外情况。** 为 Codex 提供足够的上下文，以区分
  实际问题与预期行为。
- **确保规则范围明确且长期有效。** 优先描述预期结果，而不是可能变化的函数名，
  并将指南放在其适用的代码附近。
- **将机械性检查交给 CI。** 不要将格式检查、lint 检查和其他
  确定性检查写入审查规则。

创建一个有代表性的 Pull Request，并使用 `@codex review` 请求审查。
根据审查发现和反馈完善规则，并缩小或
删除会产生干扰信息的指南。

代码审查规则用于指导 Codex，不能取代测试、分支保护或必需的审批。

如需在单次审查中重点关注某个方面，请在 Pull Request 评论中注明：

`@codex review for issues in the database migration`

## 安全审查

安全审查是一项额外审查，适合希望特别关注 Pull Request 中安全问题的客户。它会分析 Pull Request 差异、相关的代码仓库上下文，以及已配置的威胁模型或安全指南，因此在安全相关风险方面比代码审查更深入。

代码审查在常规审查过程中也能发现安全相关问题，因此您偶尔可能会发现代码审查和安全审查的结果有所重叠。

### 设置安全审查

有关更详细的设置说明和配置选项，请参阅[安全
审查](/zh-Hans/codex/security/security-review)。

1. 设置 [Codex 云端](/zh-Hans/codex/cloud)。
2. 前往 [Codex 设置](https://chatgpt.com/codex/settings/code-review)。
3. 在 **代码仓库偏好设置**中，选择哪些 Pull Request 要接受安全
   审查，以及审查的运行时机。选择 **每次运行代码审查时** ，即可让安全审查
   与代码审查一同运行。

### 请求安全审查

要手动请求安全审查，请向 Pull Request 添加以下评论：

`@codex security review`

审查运行期间，Codex 会添加表情回应，随后直接
在 Pull Request 上发布发现的安全问题。打开关联的 Codex 任务，然后选择 **安全
报告** 标签页，即可查看完整报告。

## 根据审查发现采取行动

Codex 发布审查结果后，您可以在同一 Pull Request 中再留一条评论，让它修复问题：

```md
@codex fix the P1 issue

Codex 会以该 Pull Request 作为上下文发起云端聊天，并在具备相应权限时将修复推送回该分支。

## 让 Codex 执行其他任务

如果您在评论中提及 `@codex`，并附上 `review` 以外的任何内容，Codex 会以您的 Pull Request 作为上下文发起[云端聊天](/zh-Hans/codex/cloud)。

```md
@codex fix the CI failures

## 排查代码审查问题

如果 Codex 没有添加表情回应，或没有发布审查结果：

- 确认已为代码仓库开启 **代码审查** ，该选项位于 [Codex 设置](https://chatgpt.com/codex/settings/code-review)中。
- 确认该 Pull Request 所属的代码仓库已设置 [Codex 云端](/zh-Hans/codex/cloud)。
- 在 Pull Request 评论中使用完全一致的触发词 `@codex review`。
- 对于自动审查，请检查是否已开启 **自动审查** ，并确认
  Pull Request 事件与您的审查触发设置相匹配。
