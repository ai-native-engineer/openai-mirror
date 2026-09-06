<!-- source: https://learn.chatgpt.com/zh-Hans/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 选择模型

在 ChatGPT 桌面应用中，使用编辑器下方的模型和推理控件选择可用模型，并调整其推理强度。

提高推理强度有助于改善复杂任务的处理结果，但会花费更长时间并使用更多 Token。请先使用默认强度，在任务需要更深入的规划或分析时再提高强度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式
不局限于单个智能体运行。它使用
[子智能体](/codex/agent-configuration/subagents)加快复杂工作的处理速度，
因此适合规模较大、可拆分给多个子智能体处理的任务。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 选择模型

这些建议适用于 **ChatGPT Work** 网页版。使用
编辑器下方的模型和推理控件选择可用模型，
并调整其推理强度。

提高推理强度有助于改善复杂任务的处理结果，但会花费更长时间并使用更多 Token。请先使用默认强度，在任务需要更深入的规划或分析时再提高强度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式
不局限于单个智能体运行。它使用
[子智能体](/codex/agent-configuration/subagents)加快复杂工作的处理速度，
因此适合规模较大、可拆分给多个子智能体处理的任务。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## 选择模型

在交互式 CLI 会话中，使用 `/model` 切换模型或调整
推理强度。启动 Codex 时，您也可以通过
`--model` 或其别名 `-m` 选择模型：

该选项也适用于非交互式运行。例如：

提高推理强度可以改善复杂任务的处理效果，但耗时更长，
也会使用更多 Token。请先使用默认推理强度，
在任务需要更深入的规划或分析时再提高强度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式
不局限于单个智能体独立运行。它使用
[子智能体](/codex/agent-configuration/subagents)加快复杂工作的处理速度，
因此适合规模较大且可拆分给多个子智能体的任务。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## 选择模型

使用编辑器下方的模型切换器选择可用模型和
推理强度。

提高推理强度可以改善复杂任务的处理效果，但耗时更长，
也会使用更多 Token。请先使用默认推理强度，
在任务需要更深入的规划或分析时再提高强度。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> 模式
不局限于单个智能体独立运行。它使用
[子智能体](/codex/agent-configuration/subagents)加快复杂工作的处理速度，
因此适合规模较大且可拆分给多个子智能体的任务。

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## 推荐模型

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

可用性取决于推出进度、您的登录方式和所用客户端。
有关套餐访问权限和用量，请参阅[定价](/zh-Hans/codex/pricing)；
有关企业访问权限，请参阅[工作空间模型可用性](/zh-Hans/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)。

  请先使用您账户可用的默认能力设置。
向**更智能** 方向调整可获得更深入的推理，向 **更快** 方向调整则可更快地完成工作，同时降低成本。
  如果您想使用 `gpt-5.6-luna`，或选择特定模型、推理强度
  或速度，请打开 **高级** 选项。

选择器示意图展示的是 GPT-5.6 控件。对于符合条件的 Pro、Business（$100）和企业账户，随着 Astra 的推出，能力选项会更新为 Terra 轻度、Sol 轻度、Sol 中、Astra 轻度、Astra 中和 Astra 极高。选项可能因套餐和推出阶段而异。

### 实验性上下文管理

在支持此功能的 Codex 客户端上，使用 ChatGPT Plus 或 Pro 登录的用户可以主动启用实验性上下文管理。Astra 会跨上下文窗口保留笔记，并可搜索同一任务中较早的消息和工具结果。此实验功能默认关闭，推出时不支持使用 Business、企业账户或 API 密钥登录的用户。

要启用此功能，请在您的 `config.toml` 中设置 `features.context_management.experimental_mode = true`，
然后开始一项新任务。有关此设置，请参阅[配置参考](/zh-Hans/codex/config-file/config-reference)；
有关文件位置，请参阅[配置基础](/zh-Hans/codex/config-file/config-basic)。
工作空间要求仍然适用。

<a id="choosing-sol-terra-and-luna"></a>

## 如何选择 Astra、Sol、Terra 和 Luna

当任务涉及多个步骤和工具，
并且需要最强的能力时，请选择 **Astra** 。 **Sol** 适合需要深入分析和精心打磨的工作， **Terra** 适合日常工作，
 **Luna** 适合需求明确、可重复执行的任务。

### 各模型的优势

- **Astra，适合最困难的端到端工作。** 对于涵盖代码、应用和研究，
  且需要持续推理和判断的完整工作流，请选择 Astra。
  请向它提供资料来源、模板、约束条件和检查标准，
  明确什么样的结果才有用。Astra 更擅长提出有针对性的问题并采纳您的指导，
  同时始终兼顾原始目标和约束条件。
- **Sol，适合复杂、开放式的工作。** 对于需求不明确、难以处理或价值较高，
  且需要更多分析、判断或打磨的任务，请选择 Sol，例如
  复杂的代码变更、深度研究或精心打磨的文档。对于范围较小的任务，
  请明确完成标准，让工作保持聚焦。
- **Terra，务实的全能之选。** 如果日常工作需要强大的推理和工具使用能力，
  但不需要 Sol 那样的深度，请选择 Terra。
  对于您之前交给 GPT-5.5 的工作，可以先从 Terra 开始。
- **Luna，适合需求明确、可重复执行的任务。** 当您对理想结果已有明确预期，
  并需要大批量处理特定任务时，请选择 Luna，例如提取、
  分类、转换和生成结构化摘要。

### 选择推理强度

使用能得到所需结果的最低推理强度。对于需要更多规划、分析或检查的任务，请提高推理强度。

- ChatGPT 桌面应用、网页版 ChatGPT Work 和 IDE 扩展中的**轻度** ，或 CLI 中的 **低** ，
  适合可快速完成、范围明确的任务。
- **中** 可兼顾速度与深度，适合需要更多规划的任务。
- **高** 和 **极高** 适合涉及多个步骤、多个信息源，
  或需要权衡取舍的复杂工作。

GPT-5.5 与 GPT-5.6 的推理强度没有精确的对应关系。请先用较低设置尝试一项熟悉的任务，再根据结果调整。

### 何时使用 Max 或 Ultra

**Max** 让所选模型有更多时间针对单项任务进行推理。
对于最困难的问题，如果深度比速度或用量更重要，请使用 Max。
如果选项中未显示 Max，您需要在应用设置中启用它。

**Ultra** 使用[子智能体](/zh-Hans/codex/agent-configuration/subagents)并行处理
复杂任务的不同部分。如果您能将工作合理拆分为多个子任务，
请选择 Ultra。大多数任务不需要 Max 或 Ultra。

如果桌面应用的模型滑块中没有 Ultra，请前往
**设置** \> **配置**，然后开启 **在模型选择器滑块中显示 Ultra**。

## 其他模型

当您使用 ChatGPT 登录时，Codex 搭配上述推荐模型的效果最佳。

  <strong>
    GPT-5.4 和 GPT-5.4 mini 于 2026 年 8 月 31 日在 Codex 中停用。
  </strong>{" "}
  如果您使用 ChatGPT 登录，请在已保存的配置、自定义智能体和计划任务中，将 `gpt-5.4` 替换为 `gpt-5.6-terra`，并
将 `gpt-5.4-mini` 替换为 `gpt-5.6-luna`。
  OpenAI API 和使用您自己的 API 密钥进行身份验证的 Codex
  不受影响。

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

您也可以让 Codex 使用任何支持 [Chat Completions](https://platform.openai.com/docs/api-reference/chat) 或 [Responses API](https://platform.openai.com/docs/api-reference/responses) 的模型和提供商，以满足您的具体使用需求。

  对 Chat Completions API 的支持已弃用，并将在未来的 Codex 版本中移除。

## 已弃用的 Codex 模型

通过 ChatGPT 登录 Codex 时，`gpt-5.4` 和 `gpt-5.4-mini` 模型
于 2026 年 8 月 31 日停用。请在工作空间默认设置、已保存的模型设置、
托管配置、自定义智能体和计划任务中，
将 `gpt-5.4` 替换为 `gpt-5.6-terra`，将 `gpt-5.4-mini` 替换为 `gpt-5.6-luna`。

通过 ChatGPT 登录 Codex 时，`gpt-5.2` 和 `gpt-5.3-codex` 模型已弃用。
请更新仍引用这些模型的脚本、配置文件和
`codex exec --model` 命令。

OpenAI API 以及使用您自己的 API 密钥进行身份验证的 Codex
不受 GPT-5.4 停用的影响。有关当前可用的 API 模型，请参阅
[API 模型页面](/api/docs/models)。

## 配置默认本地模型

ChatGPT 桌面应用、Codex CLI 和 IDE 扩展使用同一个 `config.toml`
[配置文件](/zh-Hans/codex/config-file/config-basic)。要指定模型，请在配置文件中添加
`model` 条目。如果您未指定模型，
ChatGPT 桌面应用、Codex CLI 或 IDE 扩展将使用推荐模型。

## 为云端聊天选择模型

目前，您无法更改 Codex 云端聊天的默认模型。
