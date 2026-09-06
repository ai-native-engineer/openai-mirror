<!-- source: https://learn.chatgpt.com/zh-Hans/docs/linux/linux-app -->

Linux 版 ChatGPT 桌面应用现已推出预览版。请安装适用于您的 Linux 发行版和处理器架构的软件包，然后使用您的 ChatGPT 账户登录，即可处理项目和本地文件，并使用 Codex。

## 支持的发行版和架构

预览版支持以下 Linux 发行版的桌面版本：

- Ubuntu 24.04 LTS 和 26.04 LTS
- Debian 13
- Fedora 43 和 44

每个受支持的发行版均提供适用于 x64 和 ARM64 处理器的软件包。要查看您的处理器架构，请运行：

```bash
uname -m

输出为 `x86_64` 表示处理器采用 x64 架构；输出为 `aarch64` 或
`arm64` 表示处理器采用 ARM64 架构。

## 下载合适的软件包

对于 Ubuntu 或 Debian，请选择 `.deb`；对于 Fedora，请选择 `.rpm`：

| 发行版     | 架构 | 下载                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu 或 Debian | x64          | [下载适用于 x64 的 `.deb`](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu 或 Debian | ARM64        | [下载适用于 ARM64 的 `.deb`](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [下载适用于 x64 的 `.rpm`](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [下载适用于 ARM64 的 `.rpm`](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## 在 Ubuntu 或 Debian 上安装

下载适用于您的处理器架构的 `.deb` 软件包。然后打开
终端，切换到该软件包所在的目录，并使用
`apt` 安装：

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

对于 ARM64，请将 `chatgpt_amd64.deb` 替换为 `chatgpt_arm64.deb`。

从应用程序菜单中打开 **ChatGPT** ，或在终端中运行 `chatgpt`。
使用您的 ChatGPT 账户登录，然后按照
[桌面应用快速入门](/zh-Hans/codex/quickstart?setup=app)中的说明操作。

## 在 Fedora 上安装

下载适用于您的处理器架构的 `.rpm` 软件包。然后打开
终端，切换到该软件包所在的目录，并使用
`dnf` 安装：

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

对于 ARM64，请将 `chatgpt.x86_64.rpm` 替换为 `chatgpt.aarch64.rpm`。

从应用程序菜单中打开 **ChatGPT** ，或在终端中运行 `chatgpt`。
使用您的 ChatGPT 账户登录，然后按照
[桌面应用快速入门](/zh-Hans/codex/quickstart?setup=app)中的说明操作。

## 更新应用

软件包会在安装过程中配置经签名的 OpenAI 软件包仓库。请使用您所用发行版的软件包管理器安装后续更新。

在 Ubuntu 或 Debian 上，运行：

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

在 Fedora 上，运行：

```bash
sudo dnf upgrade --refresh chatgpt

## 兼容性与限制

预览版支持
[支持的发行版和架构](#supported-distributions-and-architectures)中列出的桌面发行版。
其他 Linux 发行版也可能正常运行，但不受正式支持。

某些功能有单独的平台要求。例如，
[计算机使用](/zh-Hans/codex/computer-use)功能可在 macOS 和 Windows 上使用，但
Linux 预览版暂未提供此功能。未来版本将添加对 Linux 的支持。

## Wayland 支持

原生 Wayland 支持目前仍处于实验阶段，后续将持续改进。在 Wayland 会话中，如果 XWayland 可用，应用会使用 XWayland。要显式选择原生 Wayland，请彻底退出应用，然后从终端启动：

```bash
chatgpt --ozone-platform=wayland

在原生 Wayland 支持逐步完善期间，浮动窗口、窗口定位、焦点和键盘快捷键等功能可能无法完全正常工作。

## 后续步骤

- 请参照[桌面应用快速入门](/zh-Hans/codex/quickstart?setup=app)进行操作。
- 设置 [Chrome 扩展程序](/zh-Hans/codex/chrome-extension)，以实现浏览器集成。
- 审查本地项目和命令的[权限](/zh-Hans/codex/permissions)。
