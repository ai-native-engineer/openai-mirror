<!-- source: https://learn.chatgpt.com/zh-Hans/docs/webmcp -->

网站工具是 ChatGPT 对
[WebMCP 标准提案](https://webmachinelearning.github.io/webmcp/)的实现。通过 WebMCP，
网站除了提供用户日常使用的界面，
还可以直接向 AI 智能体提供实用操作。您和智能体可以使用同一个实时页面
和已登录会话。

在 ChatGPT 桌面应用的[内置浏览器](/zh-Hans/codex/browser)中，
ChatGPT Work 和 Codex 可以发现并使用可用的网站工具。

  使用网站工具时，请选择 GPT-5.6 Sol 或 GPT-5.6 Terra。GPT-5.6 Luna 目前禁用了 WebMCP。
请将 ChatGPT 桌面应用更新至最新版本。
网站工具在企业或 Edu 工作空间中不可用。
可用性还取决于功能推出进度以及当前页面提供的工具。

## WebMCP 与 MCP 的对比

[模型上下文协议（MCP）](https://modelcontextprotocol.io/docs/learn/architecture)
将 AI 应用连接到本地或远程服务器。其工具可以
独立于打开的网页运行，例如在服务中搜索内容，
或通过 API 管理记录。

[WebMCP](https://github.com/webmachinelearning/webmcp) 让网站能够以一组预定义工具的形式，
向智能体提供其能力。智能体可以在访问网站时
发现这些工具，因此用户无需单独安装 MCP 服务器
或另行建立连接，即可使用这些能力。

当您和智能体需要查看相同内容时，这种方式就很实用，例如
编辑画布或探索仪表板时。
[带有 MCP 服务器的插件](/zh-Hans/codex/build-plugins)可以提供
不依赖已打开页面的集成功能。网站可以同时支持这两种方式。

## 在浏览器中的工作方式

在内置浏览器中打开网站，并让 ChatGPT Work 或 Codex 协助完成任务。
如果页面提供网站工具，智能体就能在您正在浏览的网站中发现并使用相关操作。
例如，文档编辑器可能允许智能体查找某个章节，
或留下评论供您审查。

选择浏览器地址栏中的 **网站工具** ，查看网站
提供的工具。选择 **可用的网站工具** ，查看各个工具的详情。
浏览器会在网站执行请求之前检查每个请求，智能体也可以
查看页面，了解发生了哪些变化。如果有近期活动记录，
请选择 **最近使用** ，打开 **来源** 并审查这些调用。

在此示例中，展开 **可用的网站工具** ，查看
[Margin](https://margin-local-docs.openai.chatgpt.site) 提供的工具。

  

工具归属于提供它们的页面。关闭页面或跳转到其他页面后，
该页面的工具可能会变得不可用。如果没有合适的工具，
智能体可能仍能使用其常规浏览器能力。

## 示例：探索 OpenAI 文档

ChatGPT 学习和 OpenAI 开发者提供网站工具，用于查找和阅读
文档。在编辑器中选择 **在 ChatGPT 中打开** ，即可在桌面应用的
浏览器中打开学习网站，旁边的新聊天中已填入此提示，可直接发送。

智能体可以使用这些工具搜索、读取并打开相关页面：

| 工具                    | 功能                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | 搜索 OpenAI 文档。                                           |
| `lookup_page`           | 通过路径或 URL 读取文档页面。                               |
| `lookup_context`        | 读取当前文档路由和选中的文本。                          |
| `navigate_to_page`      | 在当前文档网站上打开匹配的页面。                 |
| `generate_custom_guide` | 开始生成自定义构建指南或学习指南，并返回其状态和链接。 |

文档智能体会异步生成定制指南。收到指南链接并不意味着生成已完成。

## 安全与用户控制

网站提供的工具定义和结果均为不可信内容。工具的名称或其仅用于读取数据的声明，并不能证明它实际会执行什么操作。网站上的指令不会赋予智能体分享无关信息或执行敏感操作的权限。

在内置浏览器中，每次工具调用都会在执行前接受安全审查。常规的网站访问和确认策略仍然适用，包括发送消息、进行购买、删除数据或更改权限等会产生重要影响的操作。浏览器会将每次调用与其来源页面及工具注册信息关联起来。这些检查可以降低风险，但并不意味着网站或其输出可信。

您可以在 **设置 \> 浏览器 \> 权限**中关闭 **启用站点工具** 。
在分享敏感信息或依赖某项更改之前，
请审查网站、请求执行的操作及其结果。

请通过 OpenAI 的
[安全漏洞赏金计划](https://bugcrowd.com/engagements/openai)报告安全漏洞。对于 AI 安全风险，
请参阅
[AI 安全漏洞赏金计划](https://openai.com/index/safety-bug-bounty/)。请遵循
各计划的适用范围和提交说明。

## 限制

ChatGPT 的内置浏览器目前支持部分 WebMCP API。以下功能尚不受支持：

- **声明式 API：** 通过 HTML 表单属性定义的工具
  无法用作站点工具。
- **iframe 中的工具：** 浏览器不会发现 iframe 内注册的工具，
  包括同源和跨源 iframe 中的工具。

请使用 JavaScript 在顶层页面中注册工具，如
[下一节](#add-webmcp-to-your-website)所示。ChatGPT Work 和 Codex 仍可能
使用常规浏览器功能与表单交互，但这些交互
不属于 WebMCP 工具调用。

WebMCP 规范和 Chrome 开发者指南介绍的 API 范围更广，涵盖了内置浏览器目前尚不支持的功能。

## 为您的网站添加 WebMCP 支持

您可以让 Codex 为您正在开发的 Web 应用或
[站点](/zh-Hans/codex/sites)添加 WebMCP 支持。请说明智能体应该能够执行哪些操作，
并让 Codex 复用应用现有的逻辑和权限。

从您的应用已支持的一项操作开始。例如：

- 让智能体设置日期范围并查看图表底层数据的仪表盘。
- 让智能体查找章节、提出修改建议或留下评论供您审查的文档编辑器。
- 让智能体在您查看地图时比较方案并更新行程的旅行规划工具。

您也可以自行编写代码。在页面的 JavaScript 模块中，检查浏览器是否支持 WebMCP，并注册一个工具。以下只读示例会返回当前页面的标题：

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

兼容的智能体可以发现 `get_page_title` 并获取页面的当前标题。
对于接受参数的工具，请在输入模式中描述这些参数，
并在 `execute` 处理函数中使用它们来调用
应用现有的逻辑。

限制输入范围，说明副作用，并返回足够的信息以验证结果。使用应用现有的身份验证、授权和输入验证机制。为用户以及不支持 WebMCP 的浏览器保留常规界面。

有关 API 详情和示例，请参阅
[WebMCP 规范](https://webmachinelearning.github.io/webmcp/)和
[Chrome 开发者指南](https://developer.chrome.com/docs/ai/webmcp)。
