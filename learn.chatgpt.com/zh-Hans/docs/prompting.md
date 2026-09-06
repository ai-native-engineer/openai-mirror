<!-- source: https://learn.chatgpt.com/zh-Hans/docs/prompting -->

<a id="prompts"></a>

## 提示词概览

提示词用于告诉 ChatGPT 您想了解、创建或更改什么。提示词
可以是问题、指令或目标。您不需要掌握技术语法，也不必遵循
固定套路。先用自己的话说明需求，查看回复，再通过后续
消息完善结果。

简短的提示词通常就足够了。对于规模更大或更重要的任务，请包含
真正重要的部分：

- **目标：** ChatGPT 应该做什么？
- **上下文：** 哪些信息或资料来源会有所帮助？
- **输出：** 您需要什么格式、篇幅或详细程度？
- **边界：** 哪些内容必须保持不变？ChatGPT 应避免什么，或在采取行动前就哪些事项
  向您确认？

只需包含有帮助的部分。您不必填写每一项，也不必遵循
规定格式。

## 描述您需要的结果

先说明预期结果，而不是详细列出步骤。如果受众或
格式会影响 ChatGPT 应生成的内容，请一并说明。

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

此提示词说明要创建什么以及目标读者是谁。只有当流程
本身很重要时，才需要描述具体流程。否则，请给 ChatGPT 留出空间来搜索、比较
信息并调整方法。

<a id="context"></a>

## 添加有用的上下文

提供可能影响结果的信息。只添加重要的资料来源，
并说明 ChatGPT 应从每个来源获取哪些信息。

- 如果您希望 ChatGPT 总结、比较或转换文档、电子表格、演示文稿或 PDF 文件，
  或[创建文件以供审查](/zh-Hans/codex/artifacts-viewer)，请附上相应文件。
- 如果任务依赖视觉上下文，请添加屏幕截图、图表或其他[图像输入](/zh-Hans/codex/image-inputs)。
  请指出需要关注的区域，
  不要只依赖图像本身。
- 如果答案取决于最新信息，请让 ChatGPT 使用[网页搜索](/zh-Hans/codex/web-search)；
  需要核查结果时，请要求提供信息来源。
- 使用[项目](/zh-Hans/codex/projects)，让相关聊天共享文件、
  资料来源或本地文件夹。

### 使用已连接的数据源

当 ChatGPT 可以访问已连接的数据源时，请说明应在哪里查找以及要查找
什么。您不必描述它应执行的每项搜索。

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

已连接的数据源需要相应的插件，能否使用还可能取决于
您的套餐和工作空间设置。

### 使用插件

插件让 ChatGPT 和 Codex 能够复用指令，并连接 Google Drive、Gmail、Slack 和 GitHub 等工具。
两款产品的公开插件
均来自同一个通用目录。说明您需要的结果，由
当前使用的界面从其可用工具中进行选择。在 ChatGPT 的消息输入框中输入 `@`
即可选择特定插件。

  
    <span slot="icon">
      
    </span>
    在 ChatGPT 和 Codex 中查找、安装和使用插件。
  

### 个性化 ChatGPT

在 **设置 \> 个性化**中，将适用于所有聊天的偏好
设置为自定义指令。仅与当前聊天相关的细节应保留在
提示词中。

  
    <span slot="icon">
      
    </span>
    设置默认个性、自定义指令和其他应用偏好。
  

## 设置边界，避免实际问题

边界是 ChatGPT 为避免增加额外工作
或采取您并不希望的行动而需要遵循的少量指令。如果误改某个细节
会导致结果无法使用，或您希望在相关事项
影响他人之前先行审查，请设置相应边界。

- 请勿更改已批准的日期和预算数字。
- 仅使用所提供的资料来源。遇到信息缺失时，请予以标记，不要猜测。
- 确保建议不超出指定预算。
- 将消息写成草稿，不要发送。

只需关注最重要的一两项边界，无需控制
ChatGPT 的每一步操作。

## 让结果可直接使用

告诉 ChatGPT 您打算如何使用结果，以便它选择合适的
篇幅、详细程度和组织方式。

- 将其整理成一页摘要，供主管在会前快速浏览。将决策和
后续步骤放在最前面。
- 将这些笔记整理成一封跟进电子邮件，
列出各项决策、负责人和截止日期。
- 制作一张清晰的表格，对比计划支出与实际支出，
并突出显示所有超过 10% 的差异。

对于重要工作，请让 ChatGPT 进行最终检查，例如确认每项行动
都有负责人和截止日期，或标出其无法核实的信息。然后，在使用或
分享结果之前，请自行审查。

## 通过后续消息改进结果

您的第一个提示词不必尽善尽美。查看结果，然后提出
您想要的具体修改。

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

您可以补充缺少的资料来源、纠正方向、要求提供其他方案，
或调整详细程度，而无需从头开始。

### 引导和排队

当 Codex 正在工作时，您无需等待当前运行结束，
就可以发送另一条消息：

- **引导** 会将消息添加到当前运行中，可用于调整方向、补充
  遗漏的细节，或分享新信息。
- **排队** 会将消息留待下一次运行处理，适用于需要等到
  当前工作完成后再处理的后续消息。

在 ChatGPT 桌面应用中，可以在
[**设置 \> 常规 \> 后续消息行为**](/zh-Hans/codex/app/settings#general)中选择默认行为。
排队的消息会显示在消息输入框上方，您可以编辑、重新排序、发送或
删除这些消息。该设置还会显示相应快捷键，让您无需更改默认行为，
即可为单条消息采用另一种处理方式。

在 Codex CLI 中，当 Codex 正在工作时，按 <kbd>Enter</kbd> 可引导当前
轮次，按 <kbd>Tab</kbd> 则可将消息排队，留待下一轮处理。详细信息请参阅
[交互式快捷键](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
说明。

## 综合运用各项要素

对于使用已连接数据源的项目更新，一条完整的提示词可以
这样写：

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

此提示词涵盖 **目标**、 **上下文**、 **输出**和 **边界**，并
要求进行最终检查，无需逐一说明每个步骤。

## 使用语音听写

在 ChatGPT 桌面应用中，当消息输入框可见时，按下 <kbd>Ctrl+Shift+D</kbd>
并开始说话。ChatGPT 会将您的语音转录到消息输入框中，
方便您在发送提示词之前查看和编辑。

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## 聊天提示词示例

通过聊天提问、构思、起草内容并做出日常决策。先说明
您想要的结果，仅在细节会影响答案时再补充。

### 了解某个主题

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### 起草和润色文稿

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### 比较选项

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### 制定切实可行的计划

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## 为 ChatGPT Work 编写提示词

使用聊天处理快速问答、简短改写、头脑风暴和简单
草稿。对于需要利用不同资料来源或工具、涉及一系列
步骤、进行更改或产出较大交付成果的任务，请使用 ChatGPT Work。

在 ChatGPT Work 中，说明您需要的成果、提供源材料、明确
受众，并说明您将如何审查工作成果。让 ChatGPT 制定计划、
收集所需信息、创建文件，并在完成前检查这些文件。

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### 高效使用 ChatGPT Work

ChatGPT Work 适用于耗时或重复性任务，也适合制作可重复使用的成品
文件。即使某项任务消耗更多额度，只要能够节省时间、提高
质量或帮助您做出重要决策，仍可能值得执行。

从一项可供您审查的成果开始：

- 仅纳入相关资料来源，并在适当情况下限定日期范围。
- 明确目标受众、输出格式和所需篇幅。
- 区分必须完成的工作与可选的改进或润色。
- 如果处理方法很重要，请要求 ChatGPT 先制定计划。要求 ChatGPT
在发送、发布或更改他人依赖的信息前，先获得您的审批。
- 如果任务开始处理您不再需要的工作，请缩小任务范围或停止任务。

审查初次产出的结果，完善指令，并在该工作流程
行之有效时重复使用。

### 将源材料转化为成品文件

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### 为做出决策开展调研

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### 协调发布工作

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

对于重复性工作，请先在普通聊天中完善提示词。待输出结果
稳定可靠后，[在该聊天中设置计划任务](/zh-Hans/codex/automations#schedule-a-task-inside-a-chat)。
如果每次计划任务运行都应开启
新聊天，请改为创建独立的计划任务。

<a id="use-editor-context"></a>

## 为 Codex 编写提示词

如果您希望 ChatGPT 处理代码、代码库或开发者工具，请使用 Codex。
有效的 Codex 提示词应说明您期望的行为，指出相关代码或
复现步骤，保留重要约束，并说明如何验证
更改。

<a id="goal-mode"></a>

对于多步骤任务，如需 Codex 在编辑前先调查并提出方案，请在 App 编辑器中输入 `/plan`。
当[目标模式](/zh-Hans/codex/long-running-work)
可用时，请在制定计划后使用 `/goal` 设置持续生效的目标。请参阅[App 斜杠
命令](/codex/reference/slash-commands)，
查看当前命令列表。

### 如何阅读这些示例

每个工作流程都包括：

- **适用场景** 以及最合适的 Codex 使用方式（IDE、CLI 或云端）。
- **步骤** ，并附上用户提示词示例。
- **上下文说明**：Codex 可自动看到的内容，以及您应附加的内容。
- **验证**：如何检查输出。

> **注意：** IDE 扩展会自动将您打开的文件纳入上下文。在 CLI 中，请明确指定路径，或通过 `/mention` 和 `@` 路径自动补全功能附加文件。

Codex 在限制文件和网络访问的[沙盒](/zh-Hans/codex/sandboxing)
中运行本地命令。如果任务需要越过该边界，
Codex 会遵循您的审批策略，然后再继续。

### 讲解代码库

当您熟悉新项目、接手一项服务，或尝试理清协议、数据模型或请求流程时，请使用此工作流程。

#### IDE 扩展工作流程（本地探索的最快方式）

1. 打开最相关的文件。
2. 选中您关注的代码（可选，但建议这样做）。
3. 向 Codex 输入提示词：

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

验证：

- 要求 Codex 提供您可以核对的示意图或检查清单：

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### CLI 工作流程（适合需要会话记录和 Shell 命令的场景）

1. 启动交互式会话：

   ```bash
   codex

2. 附加文件（可选）并输入提示词：

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

上下文说明：

- 您可以在编辑器中使用 `@` 插入工作空间中的文件路径，或使用 `/mention` 附加特定文件。

### 修复缺陷

当您遇到可在本地复现的异常行为时，请使用此工作流程。

#### CLI 工作流程（快速迭代复现与验证）

1. 在代码仓库根目录启动 Codex：

   ```bash
   codex

2. 向 Codex 提供复现步骤，以及您怀疑存在问题的文件：

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

上下文说明：

- 由您提供：复现步骤和约束条件（这些内容比概括性描述更重要）。
- 由 Codex 提供：命令输出、发现的调用位置，以及其触发的任何堆栈跟踪。

验证：

- 修复后，Codex 应重新执行复现步骤。
- 如果您有标准检查流水线，请让 Codex 运行该流水线：

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### IDE 扩展工作流程

1. 打开您认为存在缺陷的文件及其最近的调用方。
2. 向 Codex 输入提示词：

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### 编写测试

当您需要明确界定测试的具体范围时，请使用此工作流程。

#### IDE 扩展工作流程（基于选中的代码）

1. 打开包含该函数的文件。
2. 选中定义该函数的代码行。在命令面板中选择“添加到 Codex 对话”，将这些代码行添加到上下文中。
3. 向 Codex 输入提示词：

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

上下文说明：

- 由“添加到 Codex 对话”命令提供：选中的代码行（即“行号”范围）以及已打开的文件。

#### CLI 工作流程（在提示词中说明路径和行号范围）

1. 启动 Codex：

   ```bash
   codex

2. 输入包含函数名称的提示：

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### 根据截图构建原型

当您希望将设计稿、截图或 UI 参考图转换为可运行的原型时，请使用此方法。

#### CLI 工作流程（图像 + 提示）

1. 将截图保存到本地（例如 `./specs/ui.png`）。
2. 运行 Codex：

   ```bash
   codex

3. 将图像文件拖入终端，将其附加到提示中。

4. 接着补充约束条件和结构要求：

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

上下文说明：

- 图像提供了视觉要求，但您仍需明确实现方面的约束条件（框架、路由、组件样式）。
- 请以文字说明图像未展示的行为，例如悬停状态、验证规则或键盘交互。

验证：

- 请 Codex 运行开发服务器（如果允许），并明确告知您应查看的位置：

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### IDE 扩展工作流程（图像 + 现有文件）

1. 在 Codex 聊天中附加图像（拖放或粘贴）。
2. 向 Codex 输入提示：

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### 通过实时更新迭代 UI

如果您希望在 Codex 编辑代码时快速循环执行“设计 → 调整 → 刷新 → 再调整”，请使用此方法。

#### CLI 工作流程（运行 Vite，然后使用简短提示进行迭代）

1. 启动 Codex：

   ```bash
   codex

2. 在单独的终端窗口中启动开发服务器：

   ```bash
   npm run dev

3. 输入提示，让 Codex 进行更改：

   ```text
   Propose 2-3 styling improvements for the landing page.

4. 选择一个方向，然后使用简短、具体的提示进行迭代：

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. 继续提出有针对性的请求：

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

验证：

- Codex 更新代码时，请在浏览器中审查更改。
- 提交您满意的更改，并还原不满意的更改。
- 如果您还原或修改了某项更改，请告知 Codex，以免它在处理下一个提示时覆盖您的修改。

### 将重构任务委派到云端

当您希望基于本地上下文设计方案，然后将耗时较长的实现工作委派给可并行运行的云端聊天时，请使用此方法。

#### 本地规划（IDE）

1. 请确保当前工作已提交，或至少已储藏，以便清晰地比较更改。
2. 请 Codex 制定重构计划。如果您可以使用 `$plan` 技能，请显式调用它：

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. 审查计划并协商调整方案：

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

上下文说明：

- 当 Codex 可以在本地扫描当前代码（入口点、模块边界、依赖关系图线索）时，规划效果最佳。

#### 云端委派（IDE → 云端）

1. 如果您尚未配置，请设置 [Codex 云端环境](/zh-Hans/codex/environments/cloud-environment)。
2. 点击提示编辑器下方的云端图标，然后选择您的云端环境。
3. 输入下一个提示后，Codex 会在云端创建一个新聊天，并沿用现有聊天的上下文，包括计划和任何本地源代码更改。

   ```text
   Implement Milestone 1 from the plan.

4. 审查云端差异，必要时继续迭代。

5. 直接在云端创建 PR，或将更改拉取到本地进行测试并完成收尾工作。

6. 继续迭代计划中的其他里程碑。

委派到云端的任务在隔离环境中运行。除非您为该环境启用互联网访问，
否则智能体阶段的互联网访问将处于关闭状态。详细了解
[云端互联网访问](/zh-Hans/codex/cloud/internet-access)。

### 进行本地代码审查

当您希望在提交或创建 PR 前获得额外的审查意见时，请使用此方法。

#### CLI 工作流程（审查您的工作树）

1. 启动 Codex：

   ```bash
   codex

2. 运行审查命令：

   ```text
   /review

3. 可选：提供自定义指令，指定审查重点：

   ```text
   /review Focus on edge cases and security issues

验证：

- 根据审查反馈修复问题，然后重新运行 `/review`，确认问题已经解决。

### 审查 GitHub Pull Request

当您希望在不将分支拉取到本地的情况下获得审查反馈时，请使用此方法。

使用此功能前，请在您的代码仓库中启用 Codex **代码审查** 。请参阅[代码审查](/zh-Hans/codex/third-party/github)。

#### GitHub 工作流程（评论驱动）

1. 在 GitHub 上打开 Pull Request。
2. 发表评论并提及 Codex，同时明确说明重点关注的方面：

   ```text
   @codex review

3. 可选：提供更明确的指令。

   ```text
   @codex review for security vulnerabilities and security concerns

### 更新文档

当您需要对文档做出准确、清晰的更改时，请使用此方法。

#### IDE 或 CLI 工作流程（本地编辑 + 本地验证）

1. 确定要更改的文档文件，然后在 IDE 中打开它们，或在 IDE 或 CLI 中使用 `@` 提及它们。
2. 向 Codex 输入提示，说明范围和验证要求：

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Codex 起草修改内容后，请审查文档并根据需要反复调整。

验证：

- 阅读渲染后的页面。
