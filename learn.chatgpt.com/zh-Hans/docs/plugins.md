<!-- source: https://learn.chatgpt.com/zh-Hans/docs/plugins -->

## 概览

插件将各种能力整合为 ChatGPT 和 Codex 中可复用的工作流。插件可以包含技能、连接器，或同时包含两者。两款产品共用一个通用插件目录，因此您可以在它们各自支持的界面中找到相同的公开插件。

插件可用于网页版、桌面版和移动版 ChatGPT 中的聊天和 Work，也可用于 ChatGPT 桌面应用中的 Codex。Codex CLI 还为 Codex 环境提供插件浏览器。IDE 扩展不支持插件。

在移动端，您可以在聊天或 Work 中使用您的账户可用的插件。

打开 **插件** 标签页，即可浏览和安装插件。
安装后，您可以在 ChatGPT 的聊天或 Work 中，或在 Codex 中使用插件。
已安装的插件可以为新对话添加技能、连接器和 MCP 工具。

打开 **插件** 标签页，即可浏览和安装插件。
安装后，您可以在聊天或 Work 中使用插件。
插件可能会提示您先连接外部服务，然后才能使用其工具。

在 Codex CLI 中，输入 `/plugins` 即可打开插件浏览器。
从已配置的市场安装插件后，请先开启新会话，
再使用插件随附的技能或工具。

<a id="plugin-directory-in-the-ide-extension"></a>

### 在受支持的界面中使用插件

IDE 扩展不支持插件。如需浏览和安装 Codex 插件，请使用 ChatGPT 桌面应用或 Codex CLI。

例如，您可以通过以下方式扩展 ChatGPT 和 Codex 的能力：

- 安装 Codex Security 插件，扫描已获授权的代码，并核实发现的疑似漏洞。
- 安装 Gmail 插件以使用 Gmail。
- 安装 Google Drive 插件，以便在 Drive、文档、Sheets 和 Slides 中开展工作。
- 安装 Slack 插件，以总结频道内容或起草回复。

插件可以包含以下一个或多个组成部分：

- **技能：** 针对特定类型工作的可复用指令。
  ChatGPT 和 Codex 可以按需加载这些技能，以遵循正确的步骤，
  并为任务使用合适的参考资料或辅助脚本。
- **连接器：** 用于连接 GitHub、Slack 或 Google Drive 等工具，
  让 ChatGPT 和 Codex 能够读取这些工具中的信息并在其中执行操作。
  连接器提供工具，也可以包含自定义 UI。
- **MCP 服务器：** 为 ChatGPT 和 Codex 提供更多工具或共享信息的服务，
  这些工具或信息通常来自您的本地项目之外的系统。
  MCP 服务器也是连接器背后的服务，负责定义工具、强制执行身份验证、
  返回结构化数据，并在外部系统中执行操作。
- **浏览器扩展程序：** 提供插件工作流程
  所需的浏览器能力。
- **钩子：** 在已配置的生命周期节点运行的命令。
  启用插件钩子前，请先审查并确认其可信。
- **计划任务模板：** 可复用的基础模板，
  用于在支持计划任务的场景中创建周期性任务。

您可以通过市场来源发布并分享插件，例如面向项目或团队的
代码仓库市场。请参阅[构建插件](https://developers.openai.com/plugins/build/plugins)，
了解市场设置、打包和分发方面的指导。

如果您正在构建集成，请先参阅
[构建 MCP 服务器](https://developers.openai.com/plugins/build/mcp-server)。
如果插件需要自定义 UI，请参阅
[可选 UI 指南](https://developers.openai.com/plugins/build/chatgpt-ui)。

## 使用和安装插件

<a id="plugin-directory-in-the-codex-app"></a>

### 通用插件目录

ChatGPT 和 Codex 共用同一个公开插件目录。
在网页端或 ChatGPT 桌面应用中，打开 **插件** 标签页即可浏览和安装插件。

  
    
  

插件目录通过以下标签页对插件进行分类：

- **OpenAI：** 由 OpenAI 开发的插件。
- **您的工作空间名称：** 由您的工作空间提供的插件。
- **个人：** 个人市场插件；有相应插件时，会显示 **由我创建** 和
**与我共享** 分区。

您可以通过单独的 **已安装** 一栏查看已安装的插件。

工作空间管理员可以为团队导入并同步 GitHub 市场。请参阅
[插件管理](/zh-Hans/codex/enterprise/plugin-management)，
了解设置和访问要求。

### 安装和使用插件

打开插件目录后：

1. 搜索或浏览插件，然后打开其详情。
2. 选择加号按钮以安装插件。
3. 如果插件需要连接器，请按提示进行连接。有些插件会在安装时要求您进行身份验证，另一些则会等到您首次使用时才提出要求。
4. 安装完成后，开始新对话，并让 ChatGPT 或 Codex 使用该插件。

### 通过“使用 ChatGPT 登录”连接受支持的合作伙伴

**使用 ChatGPT 登录** 正在以测试版形式向受支持的插件和合作伙伴网站逐步推出，
包括 Airtable、GitLab、HubSpot、Notion、Supabase 和 Vercel。
该选项可用时，请在连接插件时选择 **使用 ChatGPT 登录** ，
以创建或关联您在该服务中的账户。

登录时，只会与合作伙伴共享您的姓名、电子邮件地址和头像（如有）。登录不会授予插件访问您数据的权限，也不会自动批准操作。使用该连接前，请另行审查并批准插件请求的权限。

安装插件后，您可以直接在提示输入框中使用它：

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">直接描述任务</p>
    <p class="mt-2 text-sm text-secondary">
      说明您希望获得的结果，例如“总结今天未读的 Gmail 邮件会话”或“从 Google Drive 获取最新发布说明”。
    </p>
    <p class="mt-3 text-sm text-secondary">
      如果您希望 ChatGPT 为任务选择合适的已安装工具，请使用此方式。
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">选择特定插件</p>
    <p class="mt-2 text-sm text-secondary">
      输入 <code>@</code> 即可明确调用插件
      或其随附的某项技能。
    </p>
    <p class="mt-3 text-sm text-secondary">
      如果您希望明确指定 ChatGPT 应使用哪个插件或技能，请使用此方式。
      请参阅<a href="/codex/skills-and-plugins">技能与插件</a>。
    </p>
  </div>
</div>

### 在 Codex 中使用 Apple Messages

所有套餐的用户均可在 macOS 版 ChatGPT 桌面应用中使用 Apple Messages 插件。在 Codex 和 ChatGPT Work 中，该插件可以读取和搜索您 Mac 上的 iMessage、SMS 和 RCS 聊天记录，并通过“信息”应用代您发送消息。它不支持您通过“信息”远程与 ChatGPT 互动，也不适用于普通的 ChatGPT 聊天。

在此版本中，Messages 插件仅包含在 ChatGPT 桌面应用的 Apple Silicon（arm64）版本中。

1. 打开 **插件**，找到并安装 Apple Messages 插件。
2. 开启新的 Codex 或 ChatGPT Work 对话，让它查找、总结、起草或发送消息。
3. 在 ChatGPT 读取“信息”之前，请授予其请求的 macOS 权限。
4. 允许发送之前，请先审查消息及其收件人。

默认情况下，ChatGPT 只有在您批准消息及其收件人后才会发送消息。
选择 **允许一次** ，即可仅批准此次发送。如果您选择
**始终允许向此聊天发送消息**，ChatGPT 此后可向该“信息”聊天发送消息，
无需再次获得发送审批。

对于可能包含不可信或误导性指令的聊天，请保留逐次发送审批。持续有效的审批会让您失去在 ChatGPT 以您的名义发送消息前审查消息的最后机会。只有在您接受这一风险时，才应使用此设置。

要恢复逐次发送审批，请打开 **设置** \> **计算机使用** ，然后选择
 **信息**旁边的**管理** 。在 **始终允许发送**下，
选择该聊天旁边的垃圾桶图标，然后确认 **移除**。
此后，ChatGPT 会在再次向该聊天发送消息前征求您的同意。

**已知问题：** 如果您的任务设为 **完全访问权限** ，或以其他方式禁用了
审批提示，Apple Messages 可能无法显示发送消息所需的
确认提示。请切换为 **请求审批** 或 **代我审批** ，然后重试。

Apple Messages 在您的 Mac 上运行。网页版或移动版 ChatGPT、Codex CLI 以及 IDE 扩展均无法直接使用 Apple Messages。

在受管理的工作空间中，管理员可以通过现有的“计算机使用”控制项禁用 Apple Messages。

<a id="plugin-directory-in-codex-cli"></a>

### Codex CLI 中的插件浏览器

在 Codex CLI 中运行以下命令，打开插件浏览器：

```text
codex
/plugins

  
    
  

CLI 插件浏览器按市场对插件分组。您可以通过市场选项卡
切换来源，打开插件查看详情，安装或卸载
市场中的插件。选中已安装的插件后，按 <kbd>Space</kbd> 键
将其启用或停用。

<a id="api-key-availability"></a>

### 使用 API 密钥时的可用性

如果您[使用 OpenAI API 密钥
登录 Codex](/zh-Hans/codex/auth#sign-in-with-an-api-key)，即可在 Codex CLI 和 ChatGPT 桌面应用中的 Codex 内
浏览、安装和管理受支持的 OpenAI 精选插件。
使用 API 密钥进行身份验证时，部分插件不可用，因为其
连接流程需要不受支持的 OAuth 功能。请在
[平台用量页面](https://platform.openai.com/usage)查看插件用量。

### 权限与数据共享机制

在网页版 ChatGPT 中，聊天和 Work 使用当前对话可用的工作空间权限和工具。连接器仍需单独登录并获得相应的访问权限。

当插件功能通过 Codex 主机运行时，适用该主机的[沙盒和
审批策略](/zh-Hans/codex/agent-approvals-security)。
连接外部服务时，使用该服务自身的身份验证和
访问控制。

- 安装后，当您开始新对话或启动新的 CLI 会话时，即可使用随附的技能。
- 如果插件包含连接器，当前使用的产品可能会在设置过程中或您首次使用这些连接器时，提示您安装或登录相应连接器。
- 如果插件包含 MCP 服务器，您可能需要先进行额外设置或完成身份验证，才能使用这些服务器。
- 当 ChatGPT 通过随附的连接器发送数据时，适用该服务的条款和隐私政策。

### 移除插件

要移除插件，请在受支持的插件浏览器中打开该插件，并在此操作可用时选择
**卸载插件** 。由工作空间安装的插件或
默认插件可能不提供此操作；这些插件由您的工作空间管理员
管理。

卸载插件会从相应的 ChatGPT 或 Codex 环境中移除插件包，但随附的连接器会保持连接，直到您在 ChatGPT 中对其进行管理。

## 构建自己的插件

如果您想创建、测试或分发自己的插件，请参阅
[构建插件](https://developers.openai.com/plugins/build/plugins)。该页面介绍本地脚手架搭建、
手动设置市场、在工作空间中共享插件、插件清单和
打包指南。

如果您的插件包含由服务器支持的功能，请参阅
[构建 MCP 服务器](https://developers.openai.com/plugins/build/mcp-server)。
MCP 工具无需自定义 UI 即可运行；当可视化界面有助于
工作流程时，也可以返回 UI。

当您的插件准备好接受审查时，请参阅
[提交插件](https://developers.openai.com/plugins/deploy/submission)，了解 OpenAI 平台的提交
流程、所需权限、审查材料、MCP 检查和测试用例
要求。

## 插件指南

- [录制与重放](/zh-Hans/codex/extend/record-and-replay)：只需向 ChatGPT 演示一次工作流程，
  即可将其转化为可复用的技能。
- [Codex Security 插件](/zh-Hans/codex/security/plugin)：扫描已获授权的代码，
  核实发现的问题，并准备经审查的修复方案。
