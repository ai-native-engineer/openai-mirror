<!-- source: https://learn.chatgpt.com/zh-Hans/docs/notifications -->

通知会在工作需要您关注时提醒您。相关控件和
通知渠道因使用界面而异。

## 配置桌面通知

打开“[**设置**](codex://settings)”，选择何时显示每轮交互完成提醒：
从不显示、仅当 ChatGPT 在后台运行时显示，或始终显示。您可以使用单独的
控件开启或关闭权限请求通知和问题通知。您的
操作系统可能会要求您授予 ChatGPT
桌面应用发送通知的权限。

### 在“活动”视图中关注聊天动态

如果“**活动**”可用，请选择侧边栏中的铃铛图标，查看以下聊天
：未读聊天、正在运行的聊天或等待您回复的聊天。您还可以打开或
关闭“活动”视图：在 macOS 上使用 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd>，
在 Windows 上则使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd>。

使用该视图中的选项来选择要显示的聊天。根据您当前使用的
界面，选项可能包括 **Work**、**聊天**、**已置顶**和
**计划任务**。您还可以选择“**全部标为已读**”，以清除未读状态。

<a id="follow-task-activity-with-a-pet"></a>

### 使用宠物关注聊天动态

在 ChatGPT 桌面应用中，悬浮宠物是您在其他应用中工作时关注聊天
动态的另一种方式。它可以显示聊天的以下状态：**运行中**、
**需要输入**、**就绪**或**受阻**。

请参阅“[宠物](/zh-Hans/codex/pets?surface=app)”，了解如何选择宠物、了解其状态或
创建您自己的宠物。

## 配置网页通知

打开“**设置 \> 通知**”，管理您的账户可用的通知类别和
渠道。根据具体类别和账户，
可用渠道可能包括推送通知、电子邮件或短信。使用“**管理任务**”（位于任务
通知设置中）打开“**计划任务**”。

## 配置 CLI 通知

有关终端通知和外部通知，请参阅
“[通知](/zh-Hans/codex/config-file/config-advanced#notifications)”一节，该节位于
高级配置指南中。您可以选择 TUI 何时发出通知，
以及 Codex 是否在一轮交互完成时运行外部程序。

<a id="follow-task-activity-in-the-ide"></a>

## 在 IDE 中关注聊天动态

IDE 扩展不提供单独的通知控件。请让
聊天保持打开，以便关注其动态。若要在一轮交互
完成时运行外部程序，请在已连接的 Codex 主机上配置 `notify`。请参阅
“[通知](/zh-Hans/codex/config-file/config-advanced#notifications)”一节，该节位于
高级配置指南中。

## 相关文档

- [长时间运行的任务](/zh-Hans/codex/long-running-work)
- [计划任务](/zh-Hans/codex/automations)
- [宠物](/zh-Hans/codex/pets)
