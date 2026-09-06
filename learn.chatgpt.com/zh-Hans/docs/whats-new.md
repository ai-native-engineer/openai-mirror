<!-- source: https://learn.chatgpt.com/zh-Hans/docs/whats-new -->

这份每周摘要介绍可能改变您工作方式的 ChatGPT 和 Codex 功能，
并提供示例和延伸阅读链接。如需了解各版本更新、错误修复
和细微改进，请参阅 [Codex 更新日志](/codex/changelog)。

## 2026 年 8 月 31 日至 9 月 4 日

### 使用 GPT-6 Astra 应对复杂工作

[GPT-6 Astra](/zh-Hans/codex/models#gpt-6-astra) 结合先进的推理能力、计算机使用能力
和更强的判断力，可在 Codex 和 ChatGPT Work 中处理涉及代码、应用
和研究的复杂工作。您可以用它执行工作流程、检查结果，
并生成符合您的模板
和任务要求的文档、电子表格或演示文稿。

当您的账户可以使用 Astra 后，请在模型选择器中选择它。
开始大型任务前，请参阅[用量与定价](/zh-Hans/codex/pricing)。
Enterprise 用户既需要符合推出条件，
也需要管理员启用后才能使用。

## 2026 年 8 月 24 日至 28 日

### 在更多网站上开展工作

- **使用您的浏览器：** 除了 Chrome，您还可以通过 ChatGPT 桌面应用在 [Edge、Brave、Opera 或 Vivaldi](/zh-Hans/codex/chrome-extension)
  中开展工作。将已打开的标签页引入 ChatGPT Work 或 Codex 聊天，
  即可在您已登录的网站上处理任务。
  Opera 支持浏览器控制，但不支持侧边聊天。

- **使用网站提供的工具：** 通过[站点工具（WebMCP）](/zh-Hans/codex/webmcp)，ChatGPT Work 和 Codex
  可以在桌面应用的内置浏览器中调用网站提供的操作。
  例如，文档编辑器可以提供工具，
  用于查找章节或添加评论。请更新桌面应用，
  并使用 GPT-5.6 Sol 或 GPT-5.6 Terra。GPT-5.6 Luna 不支持站点工具，
  Enterprise 或 Edu 工作空间也无法使用此功能。

- **通过云端浏览器登录：** 使用符合条件的方案时，您可以在网页端、iOS 或 Android 的 ChatGPT Work 中
  继续处理需要网站账户的任务。
  请按照[登录请求](/zh-Hans/codex/browser?surface=web#web-sign-in-to-a-website)的提示操作，
  在登录流程中输入您的信息，不要在聊天中输入。
  这不会连接您的本地浏览器配置文件。
  网站登录功能不适用于 Enterprise 或 Edu 工作空间。

功能是否可用取决于推出进度和工作空间设置。

[阅读 8 月 25 日浏览器功能的
发布说明](/codex/changelog#codex-2026-08-25-browser)。

### 通过应用事件触发计划任务

[计划任务](/zh-Hans/codex/automations?surface=web#web-trigger-tasks-from-app-events)现在可以在 Gmail、Slack 或 GitHub 中发生受支持的事件时启动。
使用事件触发器分拣新邮件、汇总频道动态，
或处理 Pull Request 反馈，
无需按固定频率轮询。

符合条件的方案可在网页版和移动版 ChatGPT 中使用事件触发的任务。请先连接相关应用，并批准其请求的访问权限。在受管理的工作空间中，管理员可以控制访问权限。

<PromptComponent
  prompt={`当我在 <owner>/<repository> 中的某个 Pull Request 收到新的审查反馈时，请总结反馈并拟定修改计划。`}
/>

[阅读 8 月 25 日的
发布说明](/codex/changelog#codex-2026-08-25-event-triggers)。

## 2026 年 8 月 17 日至 21 日

### 使用更多应用和内容开展工作

- **Apple Messages：** [在 Mac 上查找聊天、总结消息、拟写回复，并通过 Messages 发送](/zh-Hans/codex/plugins?surface=app#app-use-apple-messages-from-codex)。所有方案均可在 macOS 版 ChatGPT 桌面应用中使用此插件。请在 ChatGPT Work 和 Codex 中使用它，普通 ChatGPT 聊天不支持此插件。默认情况下，ChatGPT 仅在您批准消息及其收件人后才会发送。

- **站点协同编辑：** 在支持此功能时，您可以[邀请工作空间中的活跃成员担任编辑者](/zh-Hans/codex/sites#collaborate-on-a-site)。所有者首次发布站点后，编辑者可以完善站点并发布更新。受邀编辑者可以读取站点线上数据库中的数据；所有者仍保留对共享和设置的控制权。

- **可编辑的站点 URL：** 在支持此功能时，您可以[为现有站点选择新的 ChatGPT 托管地址](/zh-Hans/codex/sites#change-a-site-url)，无需重新部署。原地址会重定向至新地址。

- **欧洲地区的计算机使用记录：** 您可以在 EEA、瑞士和英国使用[计算机使用记录](/zh-Hans/codex/customization/computer-history)。该功能对 macOS 上的 ChatGPT Pro、Business 和 Enterprise 用户仍默认关闭。Business 和 Enterprise 管理员必须先启用访问权限。

- **分享对话线程快照：** 在 macOS 版 ChatGPT 桌面应用中[分享本地 Codex 对话线程的只读快照](/zh-Hans/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread)。个人账户生成的链接可供任何持有该链接的人查看；工作空间账户生成的链接仅限原工作空间查看。Codex 会遮盖符合已知机密信息模式的内容，但快照中仍可能存在敏感内容，因此分享前请先审查。

- **统一的置顶对话线程：** 让您的[置顶聊天](/zh-Hans/codex/projects?surface=app#app-organize-projects-and-chats)在桌面端与 iOS 之间保持同步。

[阅读 8 月 20 日发布说明](/codex/changelog#codex-2026-08-20-app)。

### 在 Codex 云端处理 GitLab 项目

[GitLab 支持](/zh-Hans/codex/third-party/gitlab)现已向所有 ChatGPT 方案开放测试版。
连接项目并创建云端环境，
使用 `@codex` 从议题或合并请求启动任务，
并请求对合并请求进行单次或自动审查。

该集成在 Codex 云端运行，受管理工作空间的管理员可以将其禁用。由 GitLab 触发的活动要求具备配置相应 webhook 的权限。GitLab Self-Managed 和 GitLab Dedicated 连接需要由工作空间管理员设置；webhook 活动要求 GitLab 19.0 或更高版本。

[阅读 8 月 19 日 GitLab 的
发布说明](/codex/changelog#codex-2026-08-19-gitlab)。

### 导出公开插件元数据以供审查

符合条件的 ChatGPT Enterprise 工作空间所有者和管理员可以将
其工作空间可见的公开插件列表下载为 CSV 文件。在
[管理 \> 插件](https://chatgpt.com/admin/plugins)中，选择 **公开**，然后
选择下载图标（**导出 CSV**）。

导出内容列出插件、应用和聊天技能的名称及说明，以及开发者、版本、以 UTC 记录的添加日期和 OpenAI 验证元数据。导出使用的公开目录快照最多可能滞后 48 小时，且不包含为该工作空间创建的插件。FedRAMP 工作空间无法使用此导出功能。

[阅读 8 月 17 日管理员导出功能的
发布说明](/codex/changelog#codex-2026-08-17-admin-csv)。

## 2026 年 8 月 10 日至 14 日

### 通过计算机使用记录查找先前的工作

[计算机使用记录](/zh-Hans/codex/customization/computer-history)会将您在应用和网站中的活动
整理为可搜索的时间线和记忆，供 ChatGPT 和 Codex 使用。
请仅在您愿意共享这些上下文信息时启用此功能，之后可以
选择纳入记录的应用和网站、暂停收集，
并随时查看或删除使用记录。

ChatGPT Pro、Business 和 Enterprise 客户可在 macOS 版 ChatGPT 桌面应用中使用计算机使用记录。Business 和 Enterprise 管理员必须先启用访问权限。该功能初期不在欧盟、瑞士和英国提供。

### 在 Linux 上使用 ChatGPT 桌面应用

[Linux 版 ChatGPT 桌面应用](/zh-Hans/codex/linux/linux-app)现已推出预览版。
在受支持的 Ubuntu 或 Debian 发行版上安装 `.deb` 软件包，
或在 Fedora 上安装 `.rpm` 软件包。
这些软件包同时支持 x64 和 ARM64 处理器。

使用您的 ChatGPT 账户登录，即可处理项目和本地文件，并使用 Codex。包括计算机使用在内的部分功能尚未在 Linux 预览版中提供。

### 将现有的智能体配置和工作内容一并迁移

将[指令、设置、技能、插件、项目和近期
工作内容](/codex/import)从 **Claude Code**、<strong>Claude Cowork</strong> 或
**Cursor** 导入 ChatGPT 桌面应用。在
**设置 \> 导入** 中开启自动更新，让导入的工作内容保持同步。

在 Codex CLI 中，使用 `/import` 将 Claude Code 或 Cursor 中受支持的配置
和最近的聊天导入您的本地会话。

[阅读 8 月 11 日桌面端和 CLI 的
发布说明](/codex/changelog#codex-2026-08-11-app)。

### 为安全防御工作选择合适的访问权限

Daybreak 现为获批的安全防御人员提供两个级别。 **Daybreak Blue** 支持
常规安全防御工作，例如代码安全审查、事件响应和
补丁验证。 **Daybreak Red** 需要单独审批，并允许用户
访问专门训练的模型，用于经授权的安全评估。

访问需获得 [Trusted Access for
Cyber](/zh-Hans/codex/cyber-safety#trusted-access-for-cyber) 授权，且仅限于
获批的身份、工作空间或组织、模型和产品界面。

[阅读 8 月 10 日 Daybreak 的
公告](/codex/changelog#codex-2026-08-10-daybreak)。

## 2026 年 8 月 3–7 日

### 通过 ChatGPT 语音讨论文件和项目

[ChatGPT 语音](/zh-Hans/codex/features/voice)现在支持已上传的文件和
[ChatGPT 项目](/zh-Hans/codex/projects)。您可以在语音对话中询问文档相关问题，
或利用项目近期的聊天、来源资料和
指令，继续推进该项目。

### 使用教育专用插件开展学习和教学

三个新[插件](/zh-Hans/codex/plugins)为
ChatGPT Work 和 Codex 带来面向课堂的专用工作流。 **大学生** 插件可创建学习指南、
练习测验、抽认卡和互动式讲解。 **高校教师** 插件可帮助
制定课程计划、准备教学材料和设计考核。 **K–12 教师** 插件支持
制定教案、准备课堂资源，以及提供适合
不同学习者的材料。

这些插件可在 ChatGPT Edu 和学区部署的 ChatGPT for Teachers 中使用。
学校决定可用的工具和权限。请阅读
[教育插件
公告](https://openai.com/index/learn-teach-chatgpt-work-codex/)。

### 复用已保存的文件，更快找到以往的工作

在网页端，您可以将资料库中保存的文件添加到对话中，无需重新上传；
也可以在资料库中搜索，并在粘贴带格式的文本时保留标题、
链接和列表。搜索功能还可在网页端、iOS 和 Android 上
匹配文件夹和对话标题。

现在，超过 10,000 个字符的粘贴内容会在所有 ChatGPT 套餐中转为附件，
包括 Enterprise 和 Edu。如果您想将内容移回消息中，请选择 **在文本框中显示** ，
即可将其还原为消息文本。

请阅读 [ChatGPT 的
发布说明](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)。

### 查看 ChatGPT Work 的剩余可用量

符合条件的个人套餐和 ChatGPT Business 用户可以直接在网页端侧边栏中查看
ChatGPT Work 的剩余可用量。可用的额度选项取决于
您的账户和工作空间权限。ChatGPT Work 和 Codex 仍然
共用同一套[用量限制和额度](/zh-Hans/codex/pricing)。

### 选择 GPT-5.6 在 ChatGPT 中的回答方式

ChatGPT Plus 和 Pro 用户可以通过新增的滑块，调整 GPT-5.6 Sol
回答问题时的思考深度。更新后的模型还会提供更可靠的事实
和更切题的回答。GPT-5.6 Luna 成为免费版
和 Go 套餐中的默认 ChatGPT 模型。

这些变化适用于 ChatGPT 对话，不会改变
ChatGPT Work 或 Codex 中的模型行为。请阅读 [ChatGPT 的
发布说明](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)。

### 在 Codex CLI 0.147.0 中整理工作并切换智能体

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
新增了可持久保存、手动排序的聊天分区，以及可移植的 Agent 插件。
您可以搜索本地、个人、工作空间和远程插件目录，或
[导入 Cursor 和 Claude Code 的设置](/zh-Hans/codex/import)，而不会重复创建
已同步的对话。

使用 `--approve-for-me` 可为符合条件的请求启用[审批请求的自动
审查](/zh-Hans/codex/sandboxing/auto-review)，而不会扩大
文件系统或网络权限。Amazon Bedrock 会话也新增了带缓存的
网页搜索和远程对话压缩功能。

### 跟踪并恢复更深入的安全扫描

托管版 Codex Security 插件的 `0.1.16` 至 `0.1.18` 版本新增了实时扫描
进度、实测 Token 用量、可恢复的深度扫描，以及可配置的
发现上限。最新版本还支持代码仓库扫描及其委派的工作进程通过 Amazon Bedrock
进行身份验证。

您可以使用 [Codex Security 工作台](/zh-Hans/codex/security/plugin/workbench)查看
扫描进度和发现的问题；如果需要更全面的评估，可以[配置深度
扫描](/zh-Hans/codex/security/plugin/deep-scans)。
查看[插件更新日志](/zh-Hans/codex/security/plugin/changelog)，
确认已安装的版本支持哪些功能。

### 审查 GitHub Pull Request，查找安全风险

[Codex Security 审查](/zh-Hans/codex/security/security-review)会结合代码仓库上下文、威胁模型和安全指南，
分析 Pull Request 中的变更。
您可以配置自动审查，使其在 Pull Request 创建或收到新提交时运行，
也可以直接通过 `@codex security review` 请求审查。

该功能以研究预览版形式向符合条件的 ChatGPT Enterprise、
Business、Edu 和 Pro 客户开放。Plus 套餐不支持此功能，且可能存在
用量限制。

## 2026 年 7 月 27–31 日

### 以更低费率使用 GPT-5.6 Terra 和 Luna

GPT-5.6 Terra 的价格现已降低 20%，GPT-5.6 Luna 的价格降低 80%。输入、
缓存输入和输出费率均按各自的相同比例下调。更新后的
[用量限制和费率](/zh-Hans/codex/pricing)使 Terra 更适合日常工作，
而 Luna 尤其适合范围明确的编程任务和大批量任务。

### 从浏览器和已打开的标签页中查找有用的上下文

在 ChatGPT 桌面应用中，[内置浏览器](/zh-Hans/codex/browser)可以从您的浏览历史中
查找页面，也可以直接通过地址栏进行 Google 搜索。
当任务需要先前的上下文时，ChatGPT 也可以
搜索您的浏览历史。

[Chrome 扩展程序](/zh-Hans/codex/chrome-extension)让您可以引用已打开的标签页、
将选中的页面文本带入侧边聊天、就 YouTube 视频提问，
或从页面的右键菜单中选择 **询问 ChatGPT** 。在 ChatGPT 将浏览历史信息用于任务之前，
请审查并批准
使用浏览历史的请求。

### 跨代码仓库审查更改

当[本地项目包含多个
文件夹](/zh-Hans/codex/projects#use-local-projects-for-folders-and-codebases)时，
桌面应用会显示每个代码仓库及其中更改的行。选择
**审查** 即可一起查看各仓库的差异，无需在不同的
审查视图之间切换。

### 在对话中完善生成的图像

在展开的查看器中打开生成的图像，然后在
**聚焦视图** 和 **画布视图**之间切换。您可以为不同图像添加评论，选择要保留的
版本，并提出有针对性的修改要求，无需离开聊天。
进一步了解[图像生成](/zh-Hans/codex/image-generation)。

### 查找需要您关注的聊天

桌面应用新增的 **活动视图** 汇集了您最近参与的聊天
和需要您关注的工作。选择侧边栏中的铃铛图标，
即可打开此视图。

[阅读 7 月 30 日桌面应用
发布说明](/codex/changelog#codex-2026-07-30-app)。

### 通过“使用 ChatGPT 登录”连接合作伙伴工具

“**使用 ChatGPT 登录** ”功能正以测试版形式逐步在受支持的插件和
合作伙伴网站中推出，首批包括 Airtable、GitLab、HubSpot、Notion、Supabase
和 Vercel。您可以用更少的步骤创建或关联合作伙伴账户，然后
在 ChatGPT 或 Codex 中开始使用该服务。

合作伙伴只会收到您的姓名、电子邮件地址和头像（如有）。
每个插件请求的访问权限仍需单独审查
和审批。阅读[7 月 29 日的登录功能
公告](/codex/changelog#codex-2026-07-29)。

### 在专用的学术研究工作空间中协作

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)
为符合条件的高校教师和博士后研究人员提供专用 ChatGPT 工作空间，
可免费使用 12 个月。经批准的团队最多可包含五名
来自同一机构且通过验证的研究人员，并享有企业数据保护
和 ChatGPT Pro 级别的使用限额。参与者可在 ChatGPT、ChatGPT Work 和 Codex 中使用 GPT-5.6，
开展研究和编程工作流。

该计划提供 ChatGPT 使用权限，不包含 OpenAI API 额度。申请者需
[通过机构验证，并有符合条件的
研究论文](https://help.openai.com/en/articles/20001406)。

### 在 iOS 上更可靠地继续 Codex 任务

当您返回应用或使用 Face ID 解锁设备时，iOS 版 ChatGPT 1.2026.202 能更可靠地重新连接任务。
语音对话会使用您选择的 ChatGPT 音色，并显示使用限额警告。
编辑器现在也会推荐已安装的插件及其技能，
与桌面应用保持一致。

此版本还改进了目标的暂停和恢复控件、行内表格
和视觉主题、工作空间中大规模差异的显示、选中文本的引用，
以及模型恢复功能。阅读[7 月 27 日 iOS
发布说明](/codex/changelog#codex-2026-07-27-mobile)。

### 比较安全扫描并管理发现的问题

托管版 Codex Security 插件的 `0.1.14` 和 `0.1.15` 版本新增了扫描对比、
误报反馈、限定作用范围的 `SECURITY.md` 策略，并提供了更清晰的代码仓库
和问题历史记录。您可以选择发现的问题，在 Linear 或 GitHub 议题中跟踪；
Codex 会在您批准前审查拟执行的操作。

使用现有的 [Codex Security
工作台](/zh-Hans/codex/security/plugin/workbench)，在桌面应用中审查已保存的扫描、发现的问题、
代码仓库历史记录和修复情况。托管插件
目录提供 `0.1.15` 版本，而公开的 CLI 插件市场
提供 `0.1.11` 版本。在依赖新功能之前，请查看 [Codex Security 插件
更新日志](/zh-Hans/codex/security/plugin/changelog)。

### 通过终端、CI 或 TypeScript 运行安全扫描

公开发布的 `@openai/codex-security` CLI 和 TypeScript SDK 已更新至
`0.1.5` 版本，版本号独立于 Codex Security 插件。
使用此软件包，您可以[通过 CLI 运行扫描](/zh-Hans/codex/security/cli)，
在 [CI](/zh-Hans/codex/security/cli/ci) 中审查 Pull Request 更改并上传 SARIF 结果，或
针对 GitHub 代码仓库
或固定 CSV 清单中的仓库运行可恢复的[批量扫描](/zh-Hans/codex/security/cli/bulk-scans)。

您还可以通过 [Codex Security TypeScript SDK](/zh-Hans/codex/security/sdk)，
将扫描、进度报告、费用控制和取消功能集成到自己的工具中。
该软件包公开提供，但运行扫描仍需 Codex Security 访问权限。
部分全仓库扫描还需要 Trusted Access for Cyber。

### 整理会话并扩展 Codex CLI 0.146.0

[Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0)
让您可以用 `/new release prep` 或 `/clear bug bash` 为新聊天命名、
置顶重要线程，以及在侧边对话之间切换而无需关闭它们。
此版本还新增了临时派生对话、适用于兼容的
自定义模型提供商的独立网页搜索、执行器提供的技能，以及对智能体插件
清单、工作空间插件发布和其他插件市场的支持。

对于自定义客户端，[App Server](/zh-Hans/codex/app-server) 可以筛选已置顶的线程、
在内存中创建派生会话、检查已安装连接器的状态，
以及读取连接器元数据。实验性的 WebSocket 支持还可将 app-server 连接到
远程代码模式主机。在开放远程连接前，请查阅
[app-server 安全要求](/zh-Hans/codex/app-server#connect-the-cli-terminal-ui)。
此版本还改进了代理支持、
MCP 重新连接、终端响应速度和 Windows 沙盒的可靠性。

### 使用 GPT-5.6 Sol 执行托管的 Codex 工作

[GPT-5.6 Sol](/zh-Hans/codex/models#recommended-models) 现已为符合条件的客户提供 Codex 云端代码审查
和质量保证支持。Sol 是 GPT-5.6 系列的旗舰模型，
适用于复杂编程、研究、计算机使用和安全工作。
Codex 云端会自动选择模型；Terra 和 Luna 仍可在
受支持的本地和网页界面中使用。

### 为 GPT-5.4 模型停用做好准备

8 月 31 日，GPT-5.4 和 GPT-5.4 mini 将不再面向使用 ChatGPT 登录的 Codex 用户提供。
请将 `gpt-5.4` 替换为 `gpt-5.6-terra`，并将 `gpt-5.4-mini`
替换为 `gpt-5.6-luna`，更新范围包括工作空间默认设置、已保存的模型设置、
托管配置、自定义智能体和计划任务。

OpenAI API 和使用 API 密钥进行身份验证的 Codex 会话不受影响。
请在停用日期前查看[已弃用的 Codex 模型](/zh-Hans/codex/models#deprecated-codex-models)
和[工作空间模型
可用性](/zh-Hans/codex/enterprise/workspace-model-availability)
。

## 2026 年 7 月 20–24 日

### 通过 ChatGPT 语音讨论工作

由 GPT-Live 驱动的[ChatGPT 语音](/zh-Hans/codex/features/voice)让您可以通过语音
在 ChatGPT 桌面应用的聊天、Work 和 Codex 中讨论工作、协调任务。
在语音模式下开始新的聊天或任务，然后让 ChatGPT 启动、检查或
引导其他线程中的工作。

在 macOS 上，开启 **屏幕上下文** 后，说一句“看看这个”，即可分享
您当前位于前台的[应用窗口快照](/zh-Hans/codex/appshots)。

Plus、Pro、Business、Edu 和企业套餐用户可以在
桌面应用中或通过[iOS 上的远程功能](/zh-Hans/codex/remote-connections#set-up-mobile-access)使用语音。

### 在一个本地项目中跨多个文件夹工作

ChatGPT 桌面应用中的本地项目现在可以包含多个相关
文件夹。请选择一个主文件夹，用于新建聊天、执行 Git 操作，以及
自动发现 `AGENTS.md`、技能和 `config.toml`。其他文件夹仍可
用于文件搜索、读取和编辑。

打开 **编辑项目** ，[添加文件夹并选择
主文件夹](/zh-Hans/codex/projects#use-local-projects-for-folders-and-codebases)。

[阅读 7 月 23 日发布说明](/codex/changelog#codex-2026-07-23-app)。

## 2026 年 7 月 13 日至 17 日

### 在桌面端集中查看 Work 对话和项目

ChatGPT 桌面应用现在将聊天和 Work 对话集中在 ChatGPT 视图中。
云端 Work 对话会在网页端、移动端和桌面端同步；本地 Work 对话则保留在您的计算机上。
桌面应用现已支持 ChatGPT 项目。
Codex 继续为开发者工作流提供专用视图和独立的历史记录。

[比较桌面端的 ChatGPT Work
和 Codex](/zh-Hans/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop)，选择
适合您任务的视图。

### 使用 Codex Micro 控制 Codex 的并行任务

7 月 15 日，OpenAI 与 Work Louder 推出了
[Codex Micro](/zh-Hans/codex/features/codex-micro)，这是一款限量生产的实体控制器，
用于操作 ChatGPT 桌面应用中的 Codex。它的 Agent 按键可显示
最多六个聊天的状态，并在这些聊天间切换。可自定义的命令按键、
模拟摇杆和旋钮可用于触发常用操作或技能、启动按住说话功能，以及
调整推理强度，全程无需离开键盘。

### 通过 Amazon Bedrock 使用 GPT-5.6

GPT-5.6 Sol、Terra 和 Luna 已通过 Amazon Bedrock 正式发布。
本地 ChatGPT Work 和 Codex 界面可以使用内置的
[`amazon-bedrock` 提供商](/zh-Hans/codex/amazon-bedrock)，通过 Bedrock API 密钥或
AWS SDK 凭证链进行身份验证。这包括 ChatGPT 桌面应用中的 Work 和 Codex、
Codex CLI、IDE 扩展和 Codex SDK。

### 在 iOS 上查看 Codex 任务的可视化内容

iOS 版 ChatGPT 1.2026.188 为 Codex 任务新增了内嵌可视化功能，并
改进了从对话创建和管理任务的体验，包括为
新建任务提供可靠的访问链接。阅读
[7 月 13 日 iOS 发布说明](/codex/changelog#codex-2026-07-13-mobile)。

## 2026 年 7 月 6 日至 10 日

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### 在 ChatGPT 中开展更具挑战性的工作

ChatGPT 中的 [ChatGPT Work](/zh-Hans/codex/get-started-with-work) 可以从
您的文件和[插件](/zh-Hans/codex/plugins)中收集上下文，
跨工作流执行操作，并创建可供审查的文档、演示文稿、
电子表格、站点及其他成品。它由
[GPT-5.6](/zh-Hans/codex/models) 驱动，可以将目标拆解为步骤并持续工作数小时，同时
您可以跟进进度、回答问题、调整方向，以及审批
重要操作。

[计划任务](/zh-Hans/codex/automations)可在您离开时继续推进工作，
支持单次运行、按计划运行、事件触发运行，以及在监测
变化时运行。

### 选择合适的 GPT-5.6 模型

[GPT-5.6 系列](/zh-Hans/codex/models#recommended-models)提供三款推荐模型，
适用于 ChatGPT Work、ChatGPT 桌面应用、Codex CLI 和 Codex IDE 扩展。
Sol 是面向复杂编程、计算机使用、研究和
安全工作的旗舰模型。Terra 在日常工作中兼顾能力与成本，
而 Luna 则是速度最快、成本最低的选择。默认的 **强劲** 设置使用 Sol，
推理级别为中。

### 在 ChatGPT 桌面应用中使用 Codex

7 月 9 日，Codex App 并入了适用于 macOS 和 Windows 的
[ChatGPT 桌面应用](/zh-Hans/codex/app)。Codex 保留了
专属编程体验，与 ChatGPT 的聊天和 Work 并列。Codex 的
功能包括在差异视图中进行行内编辑、在侧边面板中审查 Pull Request、由 GPT-5.6 驱动且速度更快的
[计算机使用](/zh-Hans/codex/computer-use)，以及支持多个代码仓库的
项目。

现有 Codex App 用户可以照常更新。您可以将 Codex 设为默认视图，
使用 Codex 标志作为应用图标，并通过 ChatGPT 移动应用访问桌面端的 Codex 项目。
更新后的桌面应用已面向全球所有 ChatGPT 套餐用户开放，
包括免费版用户。

## 2026 年 6 月 15 日至 19 日

### 将演示的工作流转化为可复用技能

通过[录制与重放](/zh-Hans/codex/extend/record-and-replay)，您可以在 macOS 上向 ChatGPT 或
Codex 演示工作流，并将演示转化为可复用的技能。对于
演示比描述更容易的重复性任务，您可以使用此功能，然后完善
生成的技能，并使用新输入重放。该功能初期不面向
欧洲经济区、英国和瑞士开放，且需要计算机使用功能。

<a id="continue-a-task-on-another-host"></a>

### 在另一台主机上继续聊天

[聊天交接](/zh-Hans/codex/remote-connections#hand-off-a-chat-between-hosts)
可在您的本地计算机与已连接的
远程主机之间转移聊天及其 Git 状态。Codex 可以在目标主机上创建或复用工作树，
转移聊天，并在匹配的项目中继续工作。

同一桌面版本还为计划任务的运行历史新增了批量操作，
您可以将所有运行记录标为已读，或一次性归档符合条件的运行记录。

### 在 iOS 上浏览和审查工作空间

在 iOS 版 ChatGPT 移动应用中， **远程** 新增了工作空间文件浏览器、
新建聊天时使用的目录选择器、差异视图的展开和折叠控件，以及
仅对当前聊天生效或跨聊天生效的 MCP 审批选项。

计算机使用、Chrome 扩展程序、记忆和 Chronicle 也开始
向欧洲经济区、英国和瑞士逐步推出。在这些地区，记忆仍默认关闭，
而 Chronicle 是一项需要用户主动启用的研究预览功能，
面向 macOS 上的 ChatGPT Pro 订阅用户。

阅读[6 月 15 日 iOS](/codex/changelog#codex-2026-06-15-mobile)、
[6 月 16 日可用范围更新](/codex/changelog#codex-2026-06-16-app)和
[6 月 18 日应用](/codex/changelog#codex-2026-06-18-app)的发布说明。

## 2026 年 6 月 8 日至 12 日

### 使用浏览器开发者模式调试 Web 应用

通过[开发者模式](/zh-Hans/codex/browser?surface=app#app-developer-mode)，Codex 可以在受控条件下
使用 Chrome 和内置浏览器中的 Chrome DevTools Protocol 功能。
在对您的应用进行性能分析或调试时，Codex 可以检查网络流量、控制台输出、运行时错误和
页面状态。在
**设置** \> **浏览器**的 **开发者模式** 下，开启 **启用完整 CDP 访问权限**。Codex 在网站上使用该权限前，会请求
您的明确审批。

CDP 和 DOM 快照优化减少了与浏览器的往返交互，
因此浏览器操作速度也最高可达原来的两倍。

  
    
  

### 将现有配置迁移到 Codex

新的迁移流程可在首次设置时，从其他编程智能体导入受支持的
配置。Codex App 还新增了用于创建项目指令的 `/init`，
并改进了插件管理、浏览器诊断，以及已完成聊天的
摘要。

<a id="set-up-codex-tasks-from-ios"></a>

### 在 iOS 上设置 Codex 聊天

现在，您可以通过 iOS 上的远程功能选择分支、创建工作树、运行环境设置脚本，
管理目标，以及添加行内审查评论。

阅读[6 月 9 日应用](/codex/changelog#codex-2026-06-09-app)、
[6 月 9 日 iOS](/codex/changelog#codex-2026-06-09-mobile)和
[6 月 11 日应用](/codex/changelog#codex-2026-06-11-app)的发布说明。

## 2026 年 6 月 1 日至 5 日

### 使用站点功能构建和部署网站

[站点](/zh-Hans/codex/sites)让 ChatGPT 能够创建、保存、部署和检查由 OpenAI 托管的网站、
仪表板、内部工具、网页应用和游戏。站点功能在网页版和桌面版 ChatGPT 中设有
专门的入口，您可以在那里重新打开项目，
管理托管环境的值和密钥，无需另行搭建
部署技术栈。

### 通过 Amazon Bedrock 使用 Codex

您可以[通过 Amazon Bedrock 使用 Codex](/zh-Hans/codex/amazon-bedrock)运行本地工作流，
由 AWS 管理身份验证、账户控制和计费。
iOS 上的远程功能还新增了可选的应用内锁定、后续交互行为设置、
差异视图自动换行，以及通过 SSH 连接 Windows 计算机的支持。
桌面应用新增了终端位置控制，
并在个人资料视图中提供活动洞察。

[阅读 2026 年 6 月的所有发布说明](/codex/changelog#month-2026-06)。

## 2026 年 5 月 25–29 日

### 使用 Windows 应用并远程控制 Codex

[计算机使用](/zh-Hans/codex/computer-use#windows-foreground-use)新增了在 Windows 桌面应用中
查看界面、点击和输入的支持。开始前，请先安装计算机使用插件。
在 Windows 上，Codex 使用当前活动的桌面，
并在任务运行期间接管前台。远程连接也支持 Windows。
在 ChatGPT 移动应用中，打开 **远程** 即可在 Windows 设备上开始工作，
也可以使用运行 ChatGPT 桌面应用的 Mac，
从其他地方查看进度。

iOS 上的远程功能还新增了“聚焦”和“快捷指令”入口、
已归档聊天浏览功能、`/side`，以及保存或复制已渲染图像的选项。
桌面应用新增了本地项目和工作树的聊天协调功能、
按内容和分支名称搜索历史聊天的功能，以及
后台子智能体的一致视觉标识。

阅读[5 月 25 日 iOS](/codex/changelog#codex-2026-05-25-mobile)和
[5 月 29 日应用](/codex/changelog#codex-2026-05-28-app)的发布说明。

## 2026 年 5 月 18–22 日

### 通过应用快照向 Codex 提供任意 Mac 应用的上下文

[应用快照](/zh-Hans/codex/appshots)会在您同时按下两个 Command 键时，
将当前位于前台的应用窗口快照及可用文本发送给 Codex。
Codex 可从设计工具、仪表板、文档和其他应用中获取工作上下文，
无需您复制、粘贴或描述屏幕内容。

### 跟进长时间运行的目标

[目标模式](/zh-Hans/codex/prompting#goal-mode)已不再是实验性功能，
现可在 Codex App、IDE 扩展和 CLI 中使用，适合需要
数小时或数天才能完成的目标。[锁定后使用](/zh-Hans/codex/computer-use#locked-use)功能让 Codex 能够
在 Mac 锁定后继续执行获批的计算机使用任务，包括通过
ChatGPT 移动应用中的**远程** 功能执行的任务。ChatGPT Business 工作空间还可以
[与工作空间成员共享可复用的插件包](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace)。

[阅读 5 月 21 日的发布说明](/codex/changelog#codex-2026-05-21)。

## 2026 年 5 月 11–15 日

### 从移动端继续桌面上的工作

在 ChatGPT 移动应用中， **远程** 可连接运行 ChatGPT 桌面应用的 Mac。
工作在所连接的主机上运行，因此，当您通过手机继续工作时，
项目、文件、凭据、插件、技能和配置
都仍然可用。请参阅[远程连接](/zh-Hans/codex/remote-connections)，
设置主机并从另一台设备继续工作。

### 自动化可信工作流

钩子现已正式发布，可在智能体生命周期的关键节点
运行自定义命令。ChatGPT Enterprise 管理员还可以启用
[Codex 访问令牌](/zh-Hans/codex/enterprise/access-tokens)，供可信脚本、
调度器和私有 CI 运行器使用。企业指南也扩展了内容，涵盖
Codex 的受管设置和控制措施。

[阅读 5 月 14 日的发布说明](/codex/changelog#codex-2026-05-13-app)。

## 2026 年 5 月 4–8 日

### 使用 Chrome 扩展程序跨浏览器标签页工作

[Chrome 扩展程序](/zh-Hans/codex/chrome-extension)可在后台
跨标签页并行工作，无需接管您的浏览器。
您可以控制 Codex 能使用哪些网站，从而在一个任务中跨多个网页应用完成研究、
数据录入和验证。

Codex App 还新增了听写文本整理功能，以及用于名称、
文件路径和代码符号的自定义词典。ChatGPT Enterprise 工作空间所有者可允许
成员创建 [Codex 访问令牌](/zh-Hans/codex/enterprise/access-tokens)，用于
可信的非交互式本地工作流。

阅读[5 月 5 日应用](/codex/changelog#codex-2026-05-05-app)、
[5 月 5 日访问令牌](/codex/changelog#codex-2026-05-05)和
[Chrome 版 Codex](/codex/changelog#codex-2026-05-07)的发布说明。

## 2026 年 4 月 20–24 日

### 使用 GPT-5.5 处理复杂工作

[GPT-5.5](/zh-Hans/codex/models)已在 Codex 中推出，成为大多数任务的推荐模型，
在代码实现、调试、测试、计算机使用、
研究以及交付完整的知识工作成果方面表现出色。

### 让 Codex 操作浏览器并审查审批请求

[内置浏览器中的计算机使用](/zh-Hans/codex/browser?surface=app#app-computer-use-in-the-browser)
让 Codex 能够点击操作本地开发服务器提供的页面和基于文件的页面，
复现问题并验证修复。符合条件的审批请求也可以
交由[审批请求自动审查](/zh-Hans/codex/sandboxing/auto-review)处理，
该功能会在操作执行前显示审查状态和风险。

[阅读 4 月 23 日的发布说明](/codex/changelog#codex-2026-04-23)。

## 2026 年 4 月 13–17 日

### 在同一处预览和操作

[内置浏览器](/zh-Hans/codex/browser?surface=app)新增了实时预览和页面评论，
[计算机使用](/zh-Hans/codex/computer-use)则让 Codex 能够查看并
操作 macOS 应用。两者结合，让界面实现和端到端验证
能够与代码修改在同一项任务中完成。

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### 从聊天开始，持续推进工作

[独立聊天](/zh-Hans/codex/projects#start-without-a-project)让您无需选择项目文件夹
就能开始。此次更新还加入了
[聊天内的计划任务](/zh-Hans/codex/automations#schedule-a-task-inside-a-chat)、
Pull Request 上下文和更丰富的文件预览，以及[记忆](/zh-Hans/codex/customization/memories)功能，
支持跨聊天开展工作。

[阅读 4 月 16 日的 Codex App 发布说明](/codex/changelog#codex-2026-04-16-app)。

## 2026 年 4 月 6–10 日

### 在应用中审查 Pull Request 并交付变更

审查功能新增了可折叠的行内评论、行内审查和独立窗口审查模式，
并提供了更清晰的 Git 和源代码上下文。随后，Pull Request 动态、
评论和推送选项也与工作空间文件标签页一起整合进应用，
让您无需切换工具，就能检查变更并作出回应。

阅读 [4 月 9 日](/codex/changelog#codex-2026-04-09-app)和
[4 月 10 日](/codex/changelog#codex-2026-04-10-app)的 Codex App 发布说明，或
了解如何[在应用中审查变更](/zh-Hans/codex/code-review?surface=app)。

## 2026 年 3 月 23–27 日

### 将工作流打包为插件

[插件](/zh-Hans/codex/plugins)以可安装的软件包形式推出，包含技能、
连接器和 MCP 服务器。完整工作流因此更容易查找、
安装和共享，重新设计的插件和技能页面也更清晰地展示了
内容与状态。同一周还推出了历史聊天搜索功能。

阅读[任务搜索](/codex/changelog#codex-2026-03-24-app)、
[插件上线](/codex/changelog#codex-2026-03-25)和
[Codex App](/codex/changelog#codex-2026-03-25-app)的发布说明。

## 2026 年 3 月 16–20 日

### 从更早的消息派生聊天，并在编辑器中选择工具

您可以从更早的消息派生聊天，在保留原有思路的同时，
更方便地尝试新方案。编写消息时也可以使用模型和推理命令，
已启用的技能会显示在 `@` 菜单中，
GPT-5.4 mini 则为较轻量的任务和子智能体提供了更快的选择。

阅读 [GPT-5.4 mini](/codex/changelog#codex-2026-03-17)、
[聊天控制](/codex/changelog#codex-2026-03-18-app)和
[技能菜单](/codex/changelog#codex-2026-03-19-app)的发布说明。

## 2026 年 3 月 9–13 日

### 为计划任务选择合适的环境

[计划任务](/zh-Hans/codex/automations)可以在本地或工作树中运行，
并明确指定模型和推理级别。可复用模板让常见任务的配置更快捷，
而自定义主题让您更容易按个人喜好
调整工作空间。

  
    
  

### 让 Codex 检查终端输出

Codex 还可以读取当前聊天的[集成终端](/zh-Hans/codex/integrated-terminal#run-and-validate-your-project)。
它能够直接检查运行中的开发服务器或构建输出，
无需您手动粘贴。

阅读 [3 月 11 日](/codex/changelog#codex-2026-03-11-app)和
[3 月 12 日](/codex/changelog#codex-2026-03-12-app)的 Codex App 发布说明。

## 2026 年 3 月 2 日至 6 日

### 在 Windows 上原生运行 Codex

Codex App 推出了 [Windows](/zh-Hans/codex/windows/windows-app) 版，原生支持 PowerShell
和沙盒，并提供工作树、计划任务和技能。偏好 Linux 环境的开发者
仍可使用 WSL。

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### 在本地与工作树之间迁移聊天

[本地与工作树之间的交接](/zh-Hans/codex/environments/git-worktrees#working-between-local-and-worktree)
让您能够迁移正在进行的聊天，同时保留其上下文。GPT-5.4
也于同一周在 Codex 中推出，支持编程、计算机使用以及
需要更长上下文的工作流。

阅读 [Windows 版发布](/codex/changelog#codex-2026-03-04-app)、
[工作树交接](/codex/changelog#codex-2026-03-03-app)和
[GPT-5.4](/codex/changelog#codex-2026-03-05) 的发布说明。

## 2026 年 2 月 9 日至 13 日

### 实时迭代，通过派生聊天探索新方案

GPT-5.3-Codex-Spark 进入研究预览阶段，以近乎即时的响应速度支持实时编程迭代。应用还新增了聊天派生功能和始终置顶的悬浮聊天窗口，让您能够探索其他方案，或将 Codex 放在编辑器或浏览器旁边。

阅读 [Spark](/codex/changelog#codex-2026-02-12) 和
[Codex App](/codex/changelog#codex-2026-02-12-app) 的发布说明，或查看
当前的[模型指南](/zh-Hans/codex/models)。

## 2026 年 2 月 2 日至 6 日

### Codex App 在 macOS 上推出

Codex App 最初作为桌面工作空间推出，支持同时开展多个项目聊天，
并提供内置 Git 审查、工作树、技能、计划任务和语音听写功能。
如今，[ChatGPT 桌面应用](/zh-Hans/codex/app)中的 Codex 已具备这些功能。

  
    
  

### 调整进行中的工作方向并添加文件

回合内引导功能让您无需停止正在生成的回复，
就能调整 Codex 的工作方向；文件附件也不再仅限于图片。
这些交互方式奠定了基础，让您能够通过后续消息[即时引导 Codex 或将消息加入队列](/zh-Hans/codex/prompting#steering-and-queuing)，
并提供 Codex 所需的上下文。

阅读 [Codex App 发布说明](/codex/changelog#codex-2026-02-02)和
[2 月 5 日应用发布说明](/codex/changelog#codex-2026-02-05-app)。
