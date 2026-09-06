<!-- source: https://learn.chatgpt.com/zh-Hans/docs/windows/windows-sandbox -->

在 Windows 上通过原生 [ChatGPT 桌面应用](/zh-Hans/codex/windows/windows-app)、
[CLI](/zh-Hans/codex/cli) 或 [IDE 扩展](/zh-Hans/codex/ide)使用 Codex。

Windows 上的 ChatGPT 桌面应用支持并行聊天、
工作树、计划任务、Git 功能、内置浏览器、文件预览、
插件和技能等核心工作流。

该应用可以通过 Windows 沙盒在 PowerShell 中原生运行，无需
WSL 或虚拟机。这样，Codex 可以继续使用 Windows 原生
工作流，同时限制文件系统和网络权限的范围。

  
    
  

<div class="mb-8">
  
</div>

原生 Windows 沙盒有两种模式：

- 在 Windows 上以原生方式使用防护更强的 `elevated` 沙盒，
- 在 Windows 上以原生方式使用备用的 `unelevated` 沙盒。

<span id="windows-sandbox"></span>

## 配置 Windows 沙盒

当您在 Windows 上原生运行 Codex 时，智能体模式会使用 Windows 沙盒，
阻止写入工作文件夹以外的文件系统，并在未经您明确审批时
阻止网络访问。

原生 Windows 沙盒支持两种模式，您可以在
`config.toml` 中进行配置：

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` 是首选的原生 Windows 沙盒。它使用专用的
低权限沙盒用户、文件系统权限边界、防火墙
规则，以及在沙盒中运行命令所需的本地策略变更。

`unelevated` 是备用的原生 Windows 沙盒。它使用从您当前用户派生的
受限 Windows 令牌运行命令，应用基于 ACL 的
文件系统边界，并采用环境级离线控制，而不是
专用于离线用户的防火墙规则。其防护能力弱于 `elevated`，但
当经管理员批准的设置受到本地或
企业策略阻止时，仍然很实用。

如果两种模式均可用，请使用 `elevated`。如果默认原生沙盒
无法在您的环境中正常工作，请使用 `unelevated` 作为备用方案，同时
排查设置问题。

企业管理员可以限制 Codex 能够使用哪些原生沙盒实现，
具体通过 [`requirements.toml`](/zh-Hans/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml) 进行配置：

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

此示例要求使用 `elevated` 沙盒，并禁止用户
回退到 `unelevated`。若要允许使用任一实现，请同时包含这两个值；
未选择模式时，Codex 会优先使用 `elevated`。请参阅
[`requirements.toml` 参考资料](/zh-Hans/codex/config-file/config-reference#requirementstoml)，了解
支持的取值。

默认情况下，两种沙盒模式还会使用私有桌面，以增强 UI
隔离。仅当出于兼容性需要时，才设置 `windows.sandbox_private_desktop = false`，以使用
旧版 `Winsta0\\Default` 行为。

### 沙盒权限

  以完全访问权限模式运行 Codex 时，Codex 不再局限于您的项目
  目录，并且可能无意中执行破坏性操作，导致
  数据丢失。为了更安全地执行自动化，请保留沙盒边界，并通过
[规则](/zh-Hans/codex/agent-configuration/rules)处理特定例外；或者
[将审批策略设置为
  never](/zh-Hans/codex/agent-approvals-security#run-without-approval-prompts)，让
  Codex 尝试解决问题，而不请求提升权限，
  具体行为取决于您的[审批和安全设置](/zh-Hans/codex/agent-approvals-security)。

### Windows 版本矩阵

| Windows 版本                  | 支持级别   | 备注                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | 推荐     | 这是在 Windows 上运行 Codex 的最佳基准版本。如果您正在标准化企业部署，请使用此版本。                                                                                       |
| 较新且已更新到最新状态的 Windows 10 | 尽力支持     | 可以运行，但可靠性不如 Windows 11。在 Windows 10 上，Codex 依赖包括 ConPTY 在内的现代控制台支持。实际使用中，需要 Windows 10 版本 1809 或更高版本。 |
| 较旧的 Windows 10 版本          | 不推荐 | 更可能缺少 ConPTY 等必需的控制台组件，在企业环境中也更容易失败。                                                                          |

其他环境前提：

- `winget` 应可用。若不可用，请先更新 Windows 或安装
  Windows 程序包管理器，再设置 Codex。
- 设置推荐的原生沙盒需要获得管理员批准。
- 即使操作系统版本本身符合要求，部分由企业管理的设备仍会阻止
必要的设置步骤。

### 授予沙盒读取权限

当 Windows 沙盒无法读取目录，导致命令执行失败时，请使用：

```text
/sandbox-add-read-dir C:\absolute\directory\path

该路径必须是指向现有目录的绝对路径。命令执行成功后，当前会话中后续在沙盒内运行的命令都可以读取该目录。

<span id="windows-subsystem-for-linux"></span>

默认情况下，请使用原生 Windows 沙盒。在以下情况下选择 [WSL](/zh-Hans/codex/windows/wsl)：
您需要 Linux 原生工具、工作流已在 WSL2 中运行，或者
两种原生 Windows 沙盒模式都无法满足您的需求。

## 故障排除和常见问题

如果您正在排查受管理的 Windows 计算机问题，请先检查原生
沙盒模式、Windows 版本以及 Codex 显示的任何策略错误。Windows 原生
运行中的大多数问题都源于沙盒设置、登录权限或文件系统
权限，而不是编辑器本身。

如果 Codex 无法完成 `elevated` 沙盒设置，最常见的原因
包括：

- Windows UAC 提示或管理员提示被拒绝，
- 计算机不允许创建本地用户或组，
- 计算机不允许更改防火墙规则，
- 计算机阻止沙盒用户获取所需的登录权限，
- 或者其他企业策略阻止了部分设置流程。

可尝试以下操作：

1. 再次尝试设置 `elevated` 沙盒，并在环境允许的情况下
   批准管理员提示。
2. 如果您的公司笔记本电脑阻止此操作，请咨询 IT 团队，确认计算机
是否允许经管理员批准后创建本地用户或组、配置防火墙，
以及授予沙盒用户所需的登录权限。
3. 如果默认设置仍然失败，请使用 `unelevated` 沙盒，以便在
   问题排查期间继续工作。

这意味着 Codex 无法在您的计算机上完成防护更强的 `elevated` 沙盒
设置。

- Codex 仍可在沙盒模式下运行。
- 它仍会应用基于 ACL 的文件系统边界，但不会采用
  `elevated` 所使用的独立沙盒用户边界，而且网络
  隔离较弱。
- 这是一种实用的备用方案，但不是企业长期
配置的首选。

如果您使用的是企业管理的笔记本电脑，最佳的长期解决办法通常是
在 IT 团队的帮助下让 `elevated` 沙盒正常运行。

如果在沙盒中运行的命令因错误 `1385` 而失败，则表示 Windows 不允许沙盒用户
使用启动命令所需的登录类型。

实际上，这通常意味着 Codex 已成功创建沙盒用户，
但 Windows 策略仍在阻止这些用户启动沙盒中的
命令。

处理方法：

1. 请向您的 IT 团队确认，设备策略是否已向 Codex 创建的沙盒用户授予
所需的登录权限。
2. 如果问题仅影响部分计算机或团队，
请比较它们在组策略或 OU 方面的差异。
3. 如果您需要立即继续工作，请使用 `unelevated` 沙盒，
   同时调查该策略问题。
4. 请发送 `CODEX_HOME/.sandbox/sandbox.log`，并附上您的 Windows 版本和
   简短的故障说明。

Codex 可能会警告，`Everyone` 对某些文件夹有写入权限。

如果您看到此警告，说明这些文件夹的 Windows 权限设置过于宽松，
导致沙盒无法充分保护它们。

处理方法：

1. 审查 Codex 在警告中列出的文件夹。
2. 如果您的环境允许这样做，请移除 `Everyone` 对这些文件夹的
   写入权限。
3. 更正这些权限后，请重启 Codex 或
重新运行沙盒设置。

如果您不确定如何更改这些权限，请向您的 IT 团队寻求帮助。

某些 Codex 聊天会有意在没有出站网络访问权限的情况下运行，
具体取决于所使用的权限模式。

如果任务因无法访问网络而失败：

1. 请检查该任务是否本应在禁用网络的情况下运行。
2. 如果您预期可以访问网络，请重启 Codex 并重试。
3. 如果问题持续发生，请收集沙盒日志，以便团队检查
计算机上的沙盒是否处于配置不完整或损坏的状态。

发生以下情况后，可能会出现该问题：

- 移动代码仓库或工作空间，
- 更改计算机权限，
- 更改 Windows 策略，
- 或更改其他系统配置。

可以尝试以下方法：

1. 重启 Codex。
2. 再次尝试设置 `elevated` 沙盒。
3. 如果仍无法解决问题，请暂时改用 `unelevated` 沙盒作为
   后备方案。
4. 收集沙盒日志以供审查。

如果问题仍然存在，请发送：

- `CODEX_HOME/.sandbox/sandbox.log`

同时提供以下信息也会有所帮助：

- 简要说明您当时尝试执行的操作，
- `elevated` 沙盒是否出现故障，或是否使用了 `unelevated` 沙盒，
- 应用中显示的任何错误消息，
- 您是否遇到 `1385` 错误，或者其他 Windows 或 PowerShell 错误，
- 以及您使用的是 Windows 11 还是 Windows 10。

请勿发送：

- `CODEX_HOME/.sandbox-secrets/` 中的内容

您的系统可能缺少某些原生依赖项所需的 C++ 开发工具：

- Visual Studio Build Tools（C++ 工作负载）
- Microsoft Visual C++ Redistributable (x64)
- 使用 `winget` 时，请运行 `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

安装完成后，请彻底重启 VS Code。
