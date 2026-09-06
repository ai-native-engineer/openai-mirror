<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/chatgpt-work-overview -->

ChatGPT Work 与 Codex 共用核心执行、隔离和权限机制，且均位于您的 ChatGPT Business 或 Enterprise 协议所涵盖的同一安全边界内。两者各自可用的能力和控制设置取决于任务是在本地还是云端运行、有哪些可用工具，以及适用的工作空间策略。

ChatGPT Work 可以使用已获授权的工作空间成员能够访问的信息、文件、应用和工具，完成多步骤任务。在网页端，这些任务在云端运行，而不是在该成员的设备上运行。

本概览介绍执行边界、网络和应用控制、数据处理，以及如何使用网页端的 ChatGPT Work 安全地执行任务。功能可用性和管理控制设置取决于您的套餐和工作空间配置。

如需集中了解托管执行、已连接账户的权限、
浏览器与网络设置、保留规则以及可供审计查看的信息，请参阅
[ChatGPT Work 云端安全](/zh-Hans/codex/enterprise/chatgpt-work-cloud-security)。

如需了解设备访问、本地浏览器会话、受管理的策略，
以及本地数据处理，请参阅
[ChatGPT Work 本地安全](/zh-Hans/codex/enterprise/chatgpt-work-local-security)。

## 执行隔离、文件和设备访问

ChatGPT Work 可用的文件和工具取决于 Work 的运行位置、用户权限和管理员配置。

### 本地 Work

本地 Work 通过用户设备上的 ChatGPT 桌面应用运行任务。它可以访问可供其使用的本地文件、应用和其他资源，但受用户权限、适用的工作空间控制措施和设备安全策略约束。与 Web 端的 Work 不同，本地 Work 可以操作保留在您计算机上的资源，无需您将文件上传到云端对话。

### 云端 Work

云端 Work 可在受支持的网页端、移动端和桌面端使用。它在 OpenAI 管理的基础设施上的隔离环境中运行 Codex 执行框架。云端对话可在这些平台之间同步；用户离开对话时，受支持的任务也可以继续执行。

网页端的 Work 无法直接访问用户计算机上的文件、应用或已打开的浏览器标签页。用户可以通过上传文件、将文件添加到受支持的项目，或使用已获授权的已连接应用来提供文件。桌面端通过自身的权限控制对本地文件和应用的访问。

当
[资料库](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
可用时，符合条件的已上传或生成的文件可以保存到其中。
管理员可以控制 ChatGPT 是否自动引用保存在
资料库中的文件。关闭自动引用不会阻止用户
主动访问或附加其有权使用的文件。

请参阅[代码和 shell 沙盒](/zh-Hans/codex/sandboxing?surface=web)、
[创建和编辑文档、电子表格与演示文稿](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work)，
以及
[ChatGPT 中的文件存储和资料库](https://help.openai.com/en/articles/20001052-library-for-chatgpt)。

## 网络访问与外部目标地址

Work 使用代码/shell 执行、云端浏览器等工具完成任务。这些工具各自的权限均可配置。

- **代码和 shell 命令**：能否访问公共互联网取决于适用的
  工作空间策略和个人的 Work 网络设置。不允许访问公共互联网时，
  命令仍可访问经 OpenAI 批准且
  维持 Work 正常运行所需的目标地址。这项设置控制的是网络目标地址，而非
  哪些命令可以运行。
- **网页搜索**：搜索功能的控制设置独立于 Work 代码和 shell 的
  网络设置。

如果个人的代码和 shell 设置可用，可在
**设置** \> **数据控制** \> **Work 网络访问**中找到。启用 **允许
访问公共互联网** 不会绕过适用的管理员
限制。关闭该设置后，代码和 shell 命令只能访问
受管理的允许列表中的必要目标地址；这不会停用已连接应用、
网页搜索或云端浏览器。

对代码和 shell 网络设置的更改会在当前运行
结束且 Work 刷新其执行环境后生效。请参阅
[代码和 shell 沙盒](/zh-Hans/codex/sandboxing?surface=web)及
[Work 访问控制](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)。

出站交互控制独立于
[工作空间 IP 访问限制](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt)；
后者用于限制对 ChatGPT 工作空间或合规 API 的入站访问。

## 云端浏览器与网站访问

ChatGPT Work 可使用的工具之一是
[云端浏览器](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)，
它不同于
[应用内浏览器](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)。
它以远程方式运行，使用独立于用户本地浏览器的会话。
它无法访问本地标签页、扩展程序、浏览历史记录、
已保存的密码或已通过身份验证的本地会话。

云端浏览器可以浏览公开网站、在受支持的公开表单中填写信息，并结合经批准的应用中的相关信息执行网站任务。Enterprise 和 Edu 工作空间不支持通过云端浏览器登录网站。浏览器的可用性取决于您的套餐、所在地区、功能开放进度和工作空间权限。在 Enterprise 工作空间中，管理员除了启用 Work 访问权限，还必须启用云端浏览器访问权限。

网站访问和相关操作分别受不同的控制设置约束：

- 默认情况下，ChatGPT 会在访问新网站之前询问。相关功能可用时，用户
  可以选择 **始终询问**、 **自动审批**或 **始终允许**，并允许或
  阻止访问特定网站。 **自动审批** 会执行自动化风险检查。
**始终允许** 会取消网站访问时的交互式审查。管理员
  同样可以限制用户的审批设置（例如，
  在整个工作空间中禁用 **始终允许** ）。
- 允许访问某个网站，并不意味着已批准该网站上的所有操作。对于可能产生财务、法律、账户方面或其他重大承诺的操作，ChatGPT 可以在执行前另行请求确认。

用户可以在 Work 对话中查看可用的页面截图和浏览器操作回放。这些用户可见的记录并不意味着它们可通过合规 API 导出，也不构成管理员可查看的完整执行历史记录。

请参阅
[在 ChatGPT 中使用云端浏览器](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
和[浏览器](/zh-Hans/codex/browser?surface=web)。

## 已连接应用、凭据与权限

已连接的应用或插件只能通过您的工作空间允许的集成，并在相应连接获授予的权限范围内，为 Work 提供访问权限。管理员可以在管理仪表板中控制插件和应用的可用性、工作空间角色的访问权限、外部授权、操作设置以及源系统权限。

在 Enterprise 和 Edu 工作空间中，插件及其依赖的应用默认处于关闭状态。在 Business 工作空间中，插件和应用默认处于开启状态。将插件设为可用，并不会自动启用其所需的应用，也不会自动授予账户访问权限。必须先为个人账户、共享账户或智能体自有账户授权所需的连接，ChatGPT Work 才能通过该连接进行访问。共享连接或智能体自有连接使用的是所连接账户在源系统中的权限，这些权限可能与发起请求的用户的权限不同。

在支持该功能的情况下，管理员可以将应用限制为只读操作，或限定其只能执行一组经批准的操作。应用权限设置还可以决定 ChatGPT 在使用应用、进行更改或执行重要操作之前是否需要询问。并非所有应用都支持相同的操作控制措施，也不是每项操作都需要由人工单独确认。

对于已同步的应用，源内容或权限的变更可能需要一段时间才会显示出来。断开应用连接不会自动移除已经保存在对话、生成的文件或具有独立保留政策的记录中的信息。

请参阅
[插件和应用的管理员控制、安全与合规](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business)、
[插件控制](/zh-Hans/codex/enterprise/apps-and-connectors)、
[由管理员管理的 Google Workspace 设置](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup)，以及
[支持同步的 ChatGPT 应用](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync)。

## 隐私与数据处理

ChatGPT Work 遵循适用于您的 ChatGPT 工作空间的隐私、安全和数据处理政策。对话、上传的文件、生成的文件、已连接应用和浏览器数据可能适用不同的保留和删除规则。

如需了解详情，请参阅[企业隐私](https://openai.com/enterprise-privacy/)、
[聊天和文件保留政策](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt)、
[数据驻留与推理驻留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)，
以及[ChatGPT Work 管理员常见问题](/zh-Hans/codex/enterprise/work-admin-faq)。

### 保留规则因数据类型而异

- **Work 对话：** 遵循适用的 ChatGPT 工作空间对话
  保留和删除设置。
- **保存在资料库中的文件：** 遵循适用的文件和工作空间保留规则。
  删除对话不会删除
  保存在资料库中的文件。
- **项目文件：** 保留在项目中，直至项目被删除，并受
  适用的删除规则和例外情况约束。
- **资料库之外的临时上传文件：** 对于 Enterprise，临时上传的文件可能在
  48 小时后过期，除非适用其他保留设置。
- **已保存的记忆（如果已启用）：** 遵循单独的记忆控制设置。
- **云端浏览器 Cookie：** 与本地浏览器数据相互独立。用户可以
  在云端浏览器设置中清除这些 Cookie。
- **合规日志平台记录：** 在平台中可供访问 30 天。
  导出的副本遵循接收系统的保留政策。
- **已连接应用的数据：** 源记录遵循已连接应用的政策。
  保存在聊天、文件或同步索引中的副本也须
  遵循适用的 OpenAI 存储和保留规则。

删除对话、结束 Work 任务、清除浏览器 Cookie，以及保留合规记录，都是不同的操作。删除聊天后，该聊天将不再显示，并安排在 30 天内永久删除；具体以已公布的安全、法律和去标识化例外规定为准。

请参阅
[聊天和文件保留政策](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt)、
[ChatGPT 中的记忆](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq)，
以及
[OpenAI 合规平台](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)。
