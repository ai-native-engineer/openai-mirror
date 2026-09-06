<!-- source: https://learn.chatgpt.com/zh-Hans/use-cases/build-an-ai-tour-guide -->

## 简介

学习某些工作流程时，如果有人告诉您该去哪里、选择什么，就会更容易。使用 Codex 构建操作引导，在用户亲自执行操作时，引导他们使用您的 Web 应用。

通过用于访问应用控件、状态和文档的 WebMCP 工具，Codex 可以根据用户看到的内容选择下一步指令。尚未连接服务的用户与已经完成设置的用户，需要从不同的步骤开始。

## 使用方法

1. 在 Codex 中打开您应用的代码仓库，选择一个要提供引导的工作流程，例如连接服务或添加文件夹。
2. 提供相关文档，并描述操作引导应处理哪些初始状态。
3. 运行本页的入门提示，添加引导目标、UI 状态工具，以及访问应用指令的能力。
4. 在 Codex 能够调用您应用的 WebMCP 工具的浏览器环境中测试该流程。请 Codex 为您提供引导，然后亲自完成每个步骤。

首次操作引导的范围不宜过大。添加更多工作流之前，先验证它能否引导用户从开始设置一直到完成整个流程。

## 示例：在 Runme 中添加 Google Drive 文件夹

在 <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a> 中，用户可以编辑笔记本，并通过文件浏览器添加 Google Drive 文件夹和浏览文件。操作引导帮助新用户找到这些控件并学会操作流程。

要进一步了解 Runme，您可以阅读《<a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">在 OpenAI 使用 Codex 自动完成重复性工作</a>》。

观看 Codex 如何高亮显示 Runme 的控件并解释其用途。下方截图展示的是另一套专门用于添加 Google Drive 文件夹的操作引导。

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    您的浏览器不支持视频标签。
  </video>
</figure>

Google Drive 操作引导从一个请求开始：

### 连接 Google Drive

Codex 会检查是否已连接 Google Drive。如果尚未连接，Codex 会高亮显示 **连接 Google Drive** ，并请用户选择该控件，然后完成连接。

![Codex 高亮显示 Runme 中的“连接 Google Drive”，并说明如何开始。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### 打开文件浏览器

连接完成后，Codex 会引导用户打开文件浏览器。下一步指令会根据更新后的应用状态给出。

![Codex 高亮显示用于打开 Runme 文件浏览器的控件。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### 添加文件夹

用户展开工具栏后，Codex 会高亮显示用于添加 Google Drive 文件夹的控件。用户始终掌控交互过程，也会知道下次在哪里找到该控件。

![Codex 高亮显示 Runme 中用于添加 Google Drive 文件夹的控件。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## 为 Codex 提供引导用户所需的上下文

Runme 的实现提供三类上下文：引导目标、应用状态和文档。以下工具名称来自 Runme；请根据您应用的情况实现具有相同作用的工具。

### 让 Codex 找到控件

为引导目标设置稳定且具有明确语义的 `data-tour-id` 值，并为每个目标提供标签和描述。Runme 通过三个 WebMCP 工具提供对这些控件的访问：

- `listTargets` 列出已注册的目标及其 ID、标签和描述。
- `showTourStep({ target, title?, message, placement? })` 高亮显示目标并展示说明。
- `dismiss` 取消高亮显示。

这样，Codex 就能识别控件并解释其用途，而不必替用户执行相应操作。

### 读取状态并等待用户操作

Runme 将引导相关的状态保存在 React 之外，并通过控制器对外提供。其 `getUiSnapshot` 工具提供当前 UI 状态，包括登录状态。`waitForUiChange(...)` 让 Codex 能够等待变化，例如用户选择高亮显示的控件。

让 Codex 在每次交互后重新读取状态。推进引导流程应以应用中实际发生的情况为依据，而不是看 Codex 是否已经展示过指令。

### 随应用提供指令

Runme 将 Markdown 文档与应用一同打包，并通过 WebMCP 提供访问：

- `readInstructionsForAIAgents` 说明 Codex 应如何与应用及其工具交互。
- `listDocumentation()` 列出可用页面及其描述。
- `getDocumentation({ name })` 以 Markdown 格式返回所选页面。

引导指令和工具可以随应用一同发布，无需为操作引导另外提供 Codex 插件。

## 审查操作引导

从不同的初始状态尝试同一个请求。检查操作引导是否会跳过已完成的设置步骤、等待用户操作，并在 UI 变化时更新引导内容。

还要测试步骤被取消、控件尚未显示的情况。Codex 应说明缺少什么，或选择可行的下一步操作。它不应仅因高亮显示了某个按钮，就声称操作已成功。

让身份验证、权限检查和用户操作继续沿用应用的现有流程。操作引导应在不绕过这些控制措施的前提下，帮助用户理解界面。

## 后续建议

第一个流程正常运行后，请在同一聊天中继续：

- “在 Google Drive 已连接且文件浏览器已关闭的情况下，测试此导览。”
- “处理用户取消某个步骤后又请求继续导览的情况。”
- “为 \[next workflow\] 添加导览，复用现有的导览目标和状态工具。”
