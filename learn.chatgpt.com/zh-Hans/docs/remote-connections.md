<!-- source: https://learn.chatgpt.com/zh-Hans/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

远程连接让您可以访问另一台设备或计算机上正在进行的工作。
在 ChatGPT 移动应用中打开 **远程** ，即可在已连接的 Mac 或 Windows 设备上
使用 ChatGPT 或 Codex 聊天。您还可以通过另一台
运行 ChatGPT 桌面应用的受支持设备继续工作，或将该应用连接到
SSH 主机上的项目。

远程访问使用已连接主机上的项目、聊天、文件、凭据、
权限、插件、计算机使用、浏览器设置和本地工具。

## 您可以远程执行的操作

- 在主机上的项目中新建聊天，或继续现有聊天。
- 发送后续指令、回答问题并引导正在进行的工作。
- 审批命令和其他操作。
- 审查输出、差异、测试结果、终端输出和屏幕截图。
- 当 ChatGPT 完成任务或需要您关注时接收通知。
- 在已连接的主机和聊天之间切换。

以下各节介绍如何在 ChatGPT 移动应用中打开 **远程** ，以访问
桌面主机。要将 Codex 连接到 SSH 主机上的项目，请参阅
[连接到 SSH 主机](#connect-to-an-ssh-host)。

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## 设置“远程”之前

  “远程”支持运行 macOS 或 Windows 版 ChatGPT 桌面应用的主机。
  您可以通过 iOS 或 Android 上的 ChatGPT 控制主机；当另一台 Mac 或
  Windows 设备提供 **控制其他设备** 功能时，也可以通过该设备控制主机。
  功能可用性可能因推出进度而异。

请确保您具备以下条件：

- 您要使用的 ChatGPT 账户和工作空间拥有 Codex 访问权限。
- iOS 或 Android 设备上的最新版 ChatGPT 移动应用。如果 **远程**
  未显示在应用中，请先更新 ChatGPT。
- 一台处于唤醒状态、在线且已登录同一账户和工作空间的主机，
并在其上运行最新版 macOS 或 Windows 版 ChatGPT 桌面应用。移动端设置需从
该应用开始；不能通过 Codex CLI 或 IDE 扩展进行设置。
- 该账户或工作空间所需的多重身份验证、SSO 或通行密钥
配置。

如果您通过 ChatGPT 工作空间使用 Codex，管理员可能需要先启用
远程控制访问权限，您才能通过手机连接。

<a id="set-up-mobile-access"></a>

## 设置“远程”

首先在要连接的主机上打开 ChatGPT 桌面应用。设置流程会
启用该主机的远程访问，并显示一个可以使用手机扫描的
二维码。
该二维码会将这部手机与该主机配对。对于每部手机或受支持的
桌面应用设备，都需要将其与要控制的每台主机分别配对。

  自 2026 年 6 月 8 日以来使用过的现有连接会保持配对状态。如果您自
2026 年 6 月 8 日以来未使用过某个现有连接，请更新两个应用并重新
配对设备。

1. 开始设置“远程”。

   在主机上打开 ChatGPT 桌面应用。依次进入 **设置** \>
**连接** \> **控制此 Mac 或 PC**，然后选择 **设置** 或
**添加**。批准远程访问并完成所需的验证。

2. 扫描二维码。

   使用手机扫描应用显示的二维码。扫描后会打开 ChatGPT，
您即可完成移动应用与主机的连接。

3. 在 ChatGPT 中完成设置。

   ChatGPT 会打开“远程”设置流程。确认使用相同的 ChatGPT 账户
和工作空间，然后完成所有必需的多重身份验证、SSO
或通行密钥步骤。设置成功后，该主机会显示在您手机的
“远程”中。

4. 审查主机设置。

   在主机上的应用中，通过 **设置** \> **连接** 管理已连接的
   设备。您还可以选择是否让计算机保持唤醒、启用
   计算机使用或安装 Chrome 扩展程序。

  

## 选择连接对象

先连接您已经在使用 ChatGPT 的笔记本电脑或台式电脑。需要持续访问
或不同环境时，再添加一台始终开机的计算机或 SSH 主机。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>您的笔记本电脑或台式电脑</span></span>

连接已安装桌面应用的 Mac 或 Windows PC。这样，您就可以远程访问
您已经使用的项目、聊天、凭据、插件和本地
设置。

如果该计算机进入睡眠状态、失去网络连接或应用关闭，远程访问将
停止，直至其再次可用。如果您将这台计算机用作主机设备，请保持其
连接电源，并在相应选项可用时通过主机的连接设置让计算机
保持唤醒。

在 Mac 笔记本电脑上，打开上盖并接通电源时，远程访问可以
保持可用。合上上盖时，还需要连接外接显示器。选择
**睡眠** 仍会使远程访问停止。

在 Windows 主机上，请保持会话处于解锁且可用状态，以执行需要
[计算机使用](/zh-Hans/codex/computer-use)的任务。Windows 上的计算机使用在
前台运行，因此，在将主机桌面专用于该任务时，远程控制最适合用于启动或检查
工作。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>专用且始终开机的计算机</span></span>

如果您希望 ChatGPT 在处理运行时间较长的工作时始终可访问，请使用
一台专用且始终开机的 Mac 或 Windows PC。

在该计算机上安装 ChatGPT 或
Codex 要使用的项目、凭据、MCP 服务器、技能和工具。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>远程开发环境</span></span>

如果项目已经位于远程环境中，请使用 SSH 主机或托管式远程开发环境。
先将运行桌面应用的主机连接到该环境；您的手机仍连接到同一台主机，
ChatGPT 则在远程环境中工作，
并使用该环境的依赖项、
安全策略和计算资源。

有关 SSH 设置的详细信息，请参阅[连接到 SSH 主机](#connect-to-an-ssh-host)。

  若要在始终开机的计算机或远程主机上执行浏览器或桌面任务，请启用
计算机使用，并在该主机上安装 Chrome 扩展程序。

## 已连接主机提供的内容

您的手机会向 ChatGPT 发送提示、审批和后续消息。
已连接的主机提供 ChatGPT 所使用的环境。

这意味着：

- 代码仓库中的文件和本地文档来自已连接的主机。
- Shell 命令在该主机或远程环境中运行。
- MCP 服务器、技能、浏览器访问和计算机使用均由该主机的
配置提供。
- 只有主机能够访问时，已登录的网站和桌面应用才
可用。
- 沙盒设置、安全控制措施和操作审批仍然适用于
已连接的会话。

安全中继层使受信任的计算机可由您已授权的
ChatGPT 设备访问，而无需将这些计算机直接暴露在公共互联网上。

## 从另一台设备继续工作

您可以在另一台已登录、运行 ChatGPT 桌面应用且支持远程控制的设备上
继续工作。例如，如果您的笔记本电脑无法使用，您可以先通过手机在
始终开机的主机上发起聊天，然后打开笔记本电脑上的应用，
继续同一聊天。

在提供此功能的 Mac 或 Windows 设备上，通过 **设置 \>
连接 \> 控制其他设备** 添加另一台主机。一台设备可以在允许
其他设备远程访问自己的同时，控制另一台设备。

  

## 连接到 SSH 主机

在 ChatGPT 桌面应用中，添加 SSH 主机上的远程项目，并通过聊天操作远程文件系统和 shell。远程项目聊天会在远程主机上运行命令、读取文件并写入更改。

确保远程主机遵循与常规 SSH 访问相同的安全要求：使用可信密钥、最小权限账户，并且不开放未经身份验证的公共监听服务。

1. 将该主机添加到您的 SSH 配置中，以便 Codex 自动发现它。

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   Codex 从 `~/.ssh/config` 读取明确指定的主机别名，使用
   OpenSSH 解析这些别名，并忽略仅使用匹配模式定义的主机。

2. 确认您可以从运行应用的计算机通过 SSH 连接到该主机。

   ```bash
   ssh devbox

3. 在远程主机上安装 Codex 并完成身份验证。

   该应用通过 SSH 启动远程 Codex App Server，并使用远程
   用户的登录 shell。请确保在该 shell 中，`codex` 命令可通过
   远程主机的 `PATH` 调用。

4. 在应用中打开 **设置 \> 连接**，添加或启用 SSH 主机，然后
   选择远程项目文件夹。

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## 在主机之间移交聊天

移交功能可在本地计算机与已连接的远程主机之间转移现有聊天及其 Git 状态。您可以先在本地开始工作，再在远程计算机的工作树中继续，之后将聊天移交回来。

移交聊天前，请连接目标主机，并在该主机上为同一个 Git 代码仓库保存项目。如果项目是代码仓库的子目录，请在两台主机上保存同一个子目录。Codex 只会显示已保存匹配项目的目标主机。

要移交聊天：

1. 在桌面应用中打开该聊天。
2. 在聊天底部，选择当前运行位置，再选择
   目标主机。选择 **此电脑** ，即可将远程聊天移交回
   您的本地计算机。
3. 核对目标主机和分支，然后选择 **移交**。

Codex 会在目标主机上创建或复用工作树，传输聊天和 Git 状态，并将聊天切换到该主机。如果聊天正在运行，移交操作会先中断当前响应，再进行传输。

您也可以在另一个聊天中让 Codex 将指定名称的聊天移交到已连接的主机。Codex 无法移交发出该请求的聊天本身，也不支持移交到 Codex 云端环境。

## 身份验证与网络暴露

远程连接使用 SSH 启动和管理远程 Codex App Server。请勿将 App Server 的传输接口直接暴露在共享网络或公共网络中。

如果需要连接当前网络之外的远程计算机，请使用 VPN 或网状网络工具，不要将 App Server 直接暴露到互联网。

## 故障排除

### 您在手机上看不到主机

确认主机上的桌面应用正在运行，您已启用 **允许
其他设备连接**，并且两台设备使用同一个 ChatGPT 账户和
工作空间。如果您自 2026 年 6 月 8 日起未使用过该连接，请更新两个
应用并重新配对设备。

### 重新登录后远程控制处于关闭状态

在 ChatGPT 中退出登录会关闭 **远程控制**，但不会移除您
现有的设备配对。重新登录后，请开启 **远程控制** ，以
恢复之前的连接状态。

如果开启 **远程控制** 并选择 **添加** 后出现错误，
请重新启动主机上的 ChatGPT 桌面应用，然后重试。

### 未显示审批请求

在 ChatGPT 移动应用中打开 **远程**。确认手机和主机使用
同一个 ChatGPT 账户和工作空间，然后重新扫描二维码，或从主机重新开始
设置。如果您使用的是 ChatGPT 工作空间，请让管理员确认
是否已启用远程控制访问权限。

### 远程会话断开

检查主机是否进入睡眠状态、失去网络连接，或者应用是否已关闭。在 ChatGPT 工作期间，请让主机保持唤醒并连接网络。

### 身份验证导致无法完成设置

根据设置过程中显示的提示，完成账户或工作空间的身份验证。如果您的组织要求使用 SSO、多重身份验证或通行密钥，请先完成相应流程，然后再重试。如果设置仍然失败，请让工作空间管理员确认是否已启用远程控制访问权限。

## 另请参阅

- [ChatGPT 桌面应用](/zh-Hans/codex/app)
- [功能](/zh-Hans/codex/features)
- [ChatGPT 桌面应用设置](/codex/reference/settings)
- [计算机使用](/zh-Hans/codex/computer-use)
- [Chrome 扩展程序](/zh-Hans/codex/chrome-extension)
- [命令行选项](/codex/developer-commands?surface=cli)
- [身份验证](/zh-Hans/codex/auth)
