<!-- source: https://learn.chatgpt.com/zh-Hans/docs/windows/wsl -->

使用 WSL2 时，Codex 会在 Linux 环境中运行，而不是使用
原生的 [Windows 沙盒](/zh-Hans/codex/windows/windows-sandbox)。如果您需要 Linux 原生
工具，您的代码仓库和开发工作流已经位于 WSL2 中，或者
两种原生 Windows 沙盒模式都无法在您的环境中正常运行，请选择 WSL2。

Codex `0.114` 及更早版本支持 WSL1。从 Codex `0.115` 起，Linux
沙盒改用 `bubblewrap`，因此不再支持 WSL1。

## 从 WSL 内启动 VS Code

有关分步说明，请参阅 [VS Code 官方 WSL 教程](https://code.visualstudio.com/docs/remote/wsl-tutorial)。

### 前提条件

- 已安装 WSL 的 Windows 系统。要安装 WSL，请以管理员身份打开 PowerShell，然后运行 `wsl --install`（Ubuntu 是常见选择）。
- VS Code 已安装 [WSL 扩展程序](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl)。

### 从 WSL 终端打开 VS Code

```bash
# From your WSL shell
cd ~/code/your-project
code .

此操作会打开一个 WSL 远程窗口，并在需要时安装 VS Code Server，同时确保集成终端在 Linux 中运行。

### 确认您已连接到 WSL

- 查看绿色状态栏是否显示 `WSL: <distro>`。
- 集成终端应显示 Linux 路径（例如 `/home/...`），而不是 `C:\`。
- 您可以使用以下命令进行验证：

  ```bash
  echo $WSL_DISTRO_NAME

  该命令会输出您的发行版名称。

  如果状态栏中没有显示“WSL: ...”，请按 `Ctrl+Shift+P`，选择
`WSL: Reopen Folder in WSL`，并将您的代码仓库保存在 `/home/...` 下（而不是
`C:\`），以获得最佳性能。

  如果 Windows App 或项目选择器未显示您的 WSL 代码仓库，请在文件选择器或文件资源管理器中输入
<code>\\wsl$</code>，然后前往您的
  发行版主目录。

## 在 WSL 中使用 Codex CLI

请在以管理员身份运行的 PowerShell 或 Windows 终端中运行以下命令：

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

然后在 WSL shell 中运行以下命令：

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## 在 WSL 中处理代码

- 在 <code>/mnt/c/...</code> 这类 Windows 挂载路径中处理代码，速度可能比在 Windows 原生路径中更慢。请将您的代码仓库保存在 Linux 主目录下（例如 <code>~/code/my-app</code>），以提升 I/O 速度，并减少符号链接和权限问题：
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- 如果您需要从 Windows 访问文件，可以在文件资源管理器中的 <code>\\wsl$\\Ubuntu\\home&lt;user\></code> 下找到这些文件。

## 故障排除和常见问题

- 请确保您的工作目录不在 <code>/mnt/c</code> 下。请将代码仓库移到 WSL 中（例如 <code>~/code/...</code>）。
- 如有需要，请增加分配给 WSL 的内存和 CPU；请将 WSL 更新到最新版本：
  ```powershell
  wsl --update
  wsl --shutdown

请确认该二进制文件存在，且可通过 WSL 中的 `PATH` 找到：

```bash
which codex || echo "codex not found"

如果找不到该二进制文件，请遵循 [Codex CLI 设置说明](#use-codex-cli-with-wsl)。
