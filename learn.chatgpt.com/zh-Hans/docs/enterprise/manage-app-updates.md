<!-- source: https://learn.chatgpt.com/zh-Hans/docs/enterprise/manage-app-updates -->

ChatGPT 桌面应用通常会自行检查并安装更新。如果
您的组织需要在用户收到新版本前对其进行审查，您
可以关闭应用的内置更新程序，并通过
设备管理平台部署已批准的版本。

应用的更新程序默认保持启用。将其关闭不会阻止
Microsoft Store、Microsoft Intune、移动设备管理（MDM）、软件包
管理器或其他外部部署工具安装更新。

## 开始之前

请确认您具备以下条件：

- 您拥有工作空间的 Codex 管理员权限，并可访问
[托管配置](https://chatgpt.com/codex/settings/managed-configs)
  。
- 一个适用于 macOS 或 Windows 且支持
组织管理更新的 ChatGPT 桌面应用版本。
- 一个 MDM 或软件部署平台，可将已批准的应用软件包
安装到您的托管设备上。
- 用于测试新版本、部署安全更新并跟踪
已安装应用版本的流程。

如果您尚未在 Windows 上部署此应用，请先参阅
[部署 Windows 应用](/zh-Hans/codex/enterprise/windows-deployment)。

## 关闭应用内更新

  关闭应用内更新后，您的组织负责
及时部署新的应用版本和安全修复。延迟更新可能会
使应用及其捆绑组件面临已知安全
漏洞。旧版应用不会获得单独的安全补丁或
延长支持服务。

创建一个托管策略，禁用桌面应用自身的更新程序：

1. 打开
[托管配置](https://chatgpt.com/codex/settings/managed-configs)。
2. 选择 **添加策略**，或者针对您要管理的用户、组或
   平台打开现有策略。
3. 在 **目标** 中，选择 **添加目标**，将策略分配给特定的
**组**、**用户**或 **平台**。请尽可能
   先从小型试点组开始。
4. 打开 **原始 TOML**，然后找到 **requirements.toml** 编辑器。
5. 添加以下策略：

   ```toml
   [features]
   in_app_updates = false

   如果策略已包含 `[features]` 表，请将
`in_app_updates = false` 添加到该表中。不要添加第二个 `[features]` 表，
   也不要将此设置放入 **config.toml**。

6. 选择 **保存更改**。
7. 请让受影响的用户完全退出并重新打开 ChatGPT 桌面应用。仅关闭
应用窗口不一定能重新启动应用。

有些工作空间会显示策略列表编辑器，而不是 **原始 TOML** 选项卡。在
该界面中，请将同一个 TOML 块直接添加到适用的策略；如果可用，请使用
**组** 进行分配，然后选择 **保存**。

如需了解托管策略的交付和优先级详情，请参阅
[托管配置](/zh-Hans/codex/enterprise/managed-configuration)。

## 验证托管设置

应用重启后，请在受影响用户的设备上验证策略：

1. 使用受该策略覆盖的账户登录 ChatGPT 桌面应用。
2. 打开 **设置** \> **通用**。
3. 找到 **应用内更新**，确认其中显示 **已托管** 和以下消息：
   “您的组织已关闭应用内更新。”
4. 确认您的设备管理平台仍可部署已批准的应用
版本。

即使策略
阻止应用内更新，**检查更新** 菜单选项也可能仍然可见。请使用 **已托管** 指示器验证策略，
而不要根据该菜单选项是否出现来判断。

如果首次重启后未显示该指示器，应用可能仍在
使用缓存的策略。请等待策略刷新，然后再次完全退出并重新打开
应用。在显示 **已托管** 之前，请勿认为更新限制已经生效。

## 部署已批准的应用版本

关闭应用内更新后，请使用现有的设备管理流程
交付新版本：

1. 选择您的组织计划部署的应用版本。
2. 为设备群中的每种操作系统和
设备架构获取受支持的安装包。
3. 使用一小组具有代表性的用户测试该版本。
4. 通过 Microsoft Intune、您的 MDM 平台或
其他软件部署工具部署已批准的软件包。
5. 检查设备清单，确认您的平台已安装目标
版本，然后将部署范围扩大到其他组。

您的管理平台决定如何分阶段部署版本、选择版本，
以及如何在部署未完成时恢复。如果平台允许
回滚，恢复到旧版本并不会延长支持期限，也不保证
服务兼容性。

对于 macOS，请下载
[ChatGPT 桌面应用安装程序](https://persistent.oaistatic.com/codex-app-prod/ChatGPT.dmg)。
有关 Windows 安装方法和特定架构的软件包，请参阅
[部署 Windows 应用](/zh-Hans/codex/enterprise/windows-deployment)。

## 重新开启应用内更新

要恢复应用的正常更新行为：

1. 找出为受影响用户关闭更新的托管策略、系统 `requirements.toml` 文件和 MDM
   配置描述文件。
2. 将 `in_app_updates = false` 从每个适用的 `[features]` 表中移除。
3. 保存策略更改，并重新部署所有已更新的设备管理要求配置。
4. 请让受影响的用户完全退出并重新打开 ChatGPT 桌面应用。
5. 检查 **设置** \> **通用**，确认标为托管的 **应用内更新**
   行不再显示。

当没有适用的策略设置 `in_app_updates = false` 时，应用的内置
更新程序会恢复正常行为。如果仍显示 **已托管** 指示器，
请检查其他工作空间策略、MDM 配置描述文件和系统
`requirements.toml` 文件。有关各个托管来源的应用顺序，请参阅
[位置和优先级](/zh-Hans/codex/enterprise/managed-configuration#locations-and-precedence)
。

## 了解安全和支持责任

应用收到并应用托管更新策略后，该策略会：

- 阻止桌面应用通过自身的更新程序
检查、下载或安装更新。
- 不提供由 OpenAI 管理的版本锁定或单独的发布渠道，
也不保证旧版本的服务兼容性。
- 适用于受支持的 macOS 和 Windows 版本上的 ChatGPT 桌面应用。它
不管理移动应用、Codex CLI 或 IDE 扩展的更新。

## 排查常见问题

如果身份验证问题、连接问题或超时导致应用
无法获取或应用托管策略，其内置更新程序可能会
保持启用。在显示 **已托管** 之前，请勿认定应用已阻止更新。

如果未显示 **已托管** 指示器，请确认：

- 受影响的用户选择了正确的工作空间。
- 该策略的目标是该用户、组或平台。
- 设备运行的是受支持的应用版本。
- 应用可连接到用于交付托管策略的服务。
- 该设置位于 **requirements.toml** 中，而不是 **config.toml** 中。
- 您保存策略后，用户已完全退出并重新打开应用。

如果无法打开“托管配置”或保存策略，请确认您拥有
该工作空间的 Codex 管理员访问权限。

如果您禁用应用内更新后应用版本发生变化，请检查是否是
Microsoft Store、Intune、MDM、软件包管理器或其他部署系统
安装了该更新。该策略仅控制应用内置的更新程序。

## 相关文档

- [托管配置](/zh-Hans/codex/enterprise/managed-configuration)
- [部署 Windows 应用](/zh-Hans/codex/enterprise/windows-deployment)
- [`requirements.toml` 配置参考](/zh-Hans/codex/config-file/config-reference#requirementstoml)
- [管理员部署指南](/zh-Hans/codex/enterprise/admin-setup)
