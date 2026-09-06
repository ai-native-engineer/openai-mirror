<!-- source: https://learn.chatgpt.com/zh-Hans/docs/windows/windows-app -->

# 适用于 Windows 的 ChatGPT 桌面 App

[适用于 Windows 的 ChatGPT 桌面应用](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)提供统一界面，让您能够
跨项目工作、同时进行多个聊天并审查结果。
Windows 应用支持工作树、计划任务、Git
功能、内置浏览器、文件预览、插件和技能等核心工作流。
它可通过 PowerShell 和
[Windows 沙盒](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)在 Windows 上原生运行，也可配置为
在[适用于 Linux 的 Windows 子系统 2（WSL2）](#windows-subsystem-for-linux-wsl)中运行。

  
    
  

## 下载 ChatGPT 桌面应用

下载适用于 Windows 的 [ChatGPT 桌面应用](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)。

然后按照[快速入门](/zh-Hans/codex/quickstart?setup=app)指南开始使用。

有关企业安装和更新选项，请参阅
[部署 Windows 应用](/zh-Hans/codex/enterprise/windows-deployment)。

如果您希望通过命令行安装，请运行：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## 原生沙盒

当智能体在 PowerShell 中运行时，Windows 上的 ChatGPT 桌面应用支持原生 [Windows 沙盒](/zh-Hans/codex/windows/windows-sandbox#windows-sandbox)；当智能体在[适用于 Linux 的 Windows 子系统 2（WSL2）](#windows-subsystem-for-linux-wsl)中运行时，则使用 Linux 沙盒。要在任一模式下启用沙盒保护，请在向 Codex 发送消息前，选择编辑器下方的“ **请求审批** ”。

  以完全访问权限模式运行 Codex 时，Codex 不再受项目
  目录限制，并可能无意中执行破坏性操作，导致
  数据丢失。请保留沙盒边界，并使用
[规则](/zh-Hans/codex/agent-configuration/rules)设置特定例外；或者将
[审批策略设为
  “从不”](/zh-Hans/codex/agent-approvals-security#run-without-approval-prompts)，让
  Codex 在不请求提升权限的情况下尝试解决问题，具体取决于
  您的[审批和安全设置](/zh-Hans/codex/agent-approvals-security)。

## 根据您的开发环境进行自定义

<section class="feature-grid">

<div>

### 首选编辑器

为“ **打开**”操作选择默认应用，例如 Visual Studio、VS Code 或其他
编辑器。您可以针对各个项目更改这一设置。如果您已经为某个
项目从“ **打开** ”菜单中选择了其他应用，则该项目专属的
选择优先。

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### 集成终端

您还可以选择默认的集成终端。根据您已安装的工具，
可选项包括：

- PowerShell
- 命令提示符
- Git Bash
- WSL

此更改仅适用于新的终端会话。如果您已经打开
集成终端，请重启应用或开始新对话，之后
新的默认终端才会显示。

</div>

  
    
  

</section>

## 适用于 Linux 的 Windows 子系统（WSL）

默认情况下，ChatGPT 桌面应用使用 Windows 原生 Codex 智能体，因此智能体
会在 PowerShell 中运行命令。该应用仍可处理位于
适用于 Linux 的 Windows 子系统 2（WSL2）中的项目，并在需要时使用 `wsl` CLI。

要添加 WSL 文件系统中的项目，请点击“ **添加新项目**”
或按 <kbd>Ctrl</kbd>+<kbd>O</kbd>，然后将 `\\wsl$\` 输入到文件
资源管理器窗口中。接下来，选择您的 Linux 发行版以及
要打开的文件夹。

如果您打算继续使用 Windows 原生智能体，建议将项目保存在
Windows 文件系统中，并在 WSL 中通过
`/mnt/<drive>/...` 访问这些项目。这种设置比直接从 WSL 文件系统
打开项目更加可靠。

如果您希望智能体本身在 WSL2 中运行，请打开“ **[设置](codex://settings)**”，
将智能体从“Windows 原生”切换到“WSL”，然后 **重启应用**。该
更改只有在重启后才会生效。重启后，您的项目应仍保留在
原来的位置。

Codex `0.114` 及更早版本支持 WSL1。从 Codex `0.115` 开始，Linux
沙盒改用 `bubblewrap`，因此不再支持 WSL1。

  
    
  

集成终端与智能体的配置相互独立。有关
终端选项，请参阅[根据您的开发环境进行自定义](#customize-for-your-dev-setup)。您可以
让智能体在 WSL 中运行，同时在终端中继续使用 PowerShell，
也可以让两者都使用 WSL，具体取决于您的工作流程。

## 实用的开发者工具

预先安装以下几种常用开发者工具，可让 Codex 发挥最佳效果：

- **Git**：为 ChatGPT 桌面应用中的审查面板提供支持，让您能够检查或
  还原更改。
- **Node.js**：智能体使用这一常用工具，更高效地
  执行任务。
- **Python**：智能体使用这一常用工具，更高效地
  执行任务。
- **.NET SDK**：可用于构建原生 Windows 应用。
- **GitHub CLI**：为 ChatGPT 桌面应用中的 GitHub 专属功能提供支持。

使用 Windows 默认的包管理器 `winget` 安装这些工具：将以下内容
粘贴到[集成终端](/zh-Hans/codex/integrated-terminal)中，或
让 Codex 代为安装：

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

安装 GitHub CLI 后，运行 `gh auth login`，以启用
应用中的 GitHub 功能。

如果您需要其他版本的 Python 或 .NET，请将软件包 ID 改为
所需版本对应的 ID。

## 故障排除和常见问题

### 以提升的权限运行命令

如果需要 Codex 以提升的权限运行命令，请以管理员身份启动 ChatGPT
桌面应用本身。安装完成后，打开“开始”菜单，
找到该应用并选择“ **以管理员身份运行**”。Codex 智能体将继承该
权限级别。

### PowerShell 执行策略阻止命令运行

如果您之前从未在 PowerShell 中使用过 Node.js 或 `npm` 等工具，
Codex 智能体或集成终端可能会遇到执行策略错误。

如果 Codex 为您创建 PowerShell 脚本，也可能发生这种情况。此时，
您可能需要使用更宽松的执行策略，PowerShell 才能运行
这些脚本。

错误可能如下所示：

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

常见的解决方法是将执行策略设置为 `RemoteSigned`：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

更改策略前，请先查阅 Microsoft 的
[执行策略指南](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)，
了解详细信息和其他选项。

### Windows 上的本地环境脚本

如果您的[本地环境](/zh-Hans/codex/environments/local-environment)使用跨平台
命令，例如 `npm` 脚本，您可以让所有平台共用同一个设置脚本或
同一组操作。

如果需要实现 Windows 特有的行为，请创建 Windows 专用的设置脚本或
Windows 专用的操作。

操作在集成终端所使用的环境中运行。请参阅
[根据您的开发环境进行自定义](#customize-for-your-dev-setup)。

本地设置脚本在智能体环境中运行：如果智能体使用 WSL，则在 WSL 中运行；
否则在 PowerShell 中运行。

### 与 WSL 共享配置、身份验证和会话

Windows 应用与 Windows 上原生运行的 Codex 使用同一个 Codex 主目录：
`%USERPROFILE%\.codex`。

如果您还在 WSL 中运行 Codex CLI，CLI 默认使用 Linux
主目录，因此不会自动与 Windows 应用共享配置、缓存的身份验证
信息或会话历史记录。

要共享这些内容，请采用以下任一方法：

- 将 WSL 中的 `~/.codex` 与文件系统中的 `%USERPROFILE%\.codex` 同步。
- 通过设置 `CODEX_HOME`，让 WSL 指向 Windows 上的 Codex 主目录：

```bash

```

如果您希望该设置在每个 shell 中都生效，请将其添加到 WSL shell 配置文件中，
例如 `~/.bashrc` 或 `~/.zshrc`。

### Git 功能不可用

如果您未在 Windows 上原生安装 Git，应用将无法使用部分
功能。请运行 `winget install Git.Git` 安装 Git，可使用 PowerShell 或 `cmd.exe`。

### 从 `\\wsl$` 打开的项目中检测不到 Git

目前，如果您希望使用 Windows 原生智能体，同时让项目也能
从 WSL 访问，最可靠的解决方法是将项目存储
在 Windows 本地驱动器上，并在 WSL 中通过 `/mnt/<drive>/...` 访问该项目。

### `Cmder` 未列在打开对话框中

如果您已安装 `Cmder`，但它未显示在 Codex 的打开对话框中，请将其添加到
Windows“开始”菜单：右键点击 `Cmder`，选择 **添加到“开始”**，然后
重启 Codex 或重新启动计算机。
