<!-- source: https://learn.chatgpt.com/zh-Hant/docs/linux/linux-app -->

適用於 Linux 的 ChatGPT 桌面版應用程式現已推出預覽版。請安裝適用於您的 Linux 發行版和處理器架構的套件，然後登入 ChatGPT 帳戶，即可使用專案、本機檔案和 Codex。

## 支援的發行版與架構

預覽版支援以下 Linux 發行版的桌面版本：

- Ubuntu 24.04 LTS 和 26.04 LTS
- Debian 13
- Fedora 43 和 44

每個支援的發行版均提供適用於 x64 和 ARM64 處理器的套件。若要查看您的處理器架構，請執行：

```bash
uname -m

輸出 `x86_64` 表示處理器架構為 x64；輸出 `aarch64` 或
`arm64` 則表示處理器架構為 ARM64。

## 下載適合的套件

Ubuntu 或 Debian 請選擇 `.deb`，Fedora 請選擇 `.rpm`：

| 發行版     | 架構 | 下載                                                                                                          |
| ---------------- | ------------ | ----------------------------------------------------------------------------------------------------------------- |
| Ubuntu 或 Debian | x64          | [下載適用於 x64 的 `.deb`](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_amd64.deb)     |
| Ubuntu 或 Debian | ARM64        | [下載適用於 ARM64 的 `.deb`](https://persistent.oaistatic.com/codex-app-prod/linux/deb/latest/chatgpt_arm64.deb)   |
| Fedora           | x64          | [下載適用於 x64 的 `.rpm`](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.x86_64.rpm)    |
| Fedora           | ARM64        | [下載適用於 ARM64 的 `.rpm`](https://persistent.oaistatic.com/codex-app-prod/linux/rpm/latest/chatgpt.aarch64.rpm) |

## 在 Ubuntu 或 Debian 上安裝

請下載符合您處理器架構的 `.deb` 套件。接著開啟
終端，切換至套件所在的目錄，再使用
`apt` 安裝：

```bash
cd ~/Downloads
sudo apt install ./chatgpt_amd64.deb

若使用 ARM64，請將 `chatgpt_amd64.deb` 替換為 `chatgpt_arm64.deb`。

從應用程式選單開啟 **ChatGPT** ，或在終端執行 `chatgpt`。
登入您的 ChatGPT 帳戶，並參閱
[桌面 App 快速入門](/zh-Hant/codex/quickstart?setup=app)。

## 在 Fedora 上安裝

請下載符合您處理器架構的 `.rpm` 套件。接著開啟
終端，切換至套件所在的目錄，再使用
`dnf` 安裝：

```bash
cd ~/Downloads
sudo dnf install ./chatgpt.x86_64.rpm

若使用 ARM64，請將 `chatgpt.x86_64.rpm` 替換為 `chatgpt.aarch64.rpm`。

從應用程式選單開啟 **ChatGPT** ，或在終端執行 `chatgpt`。
登入您的 ChatGPT 帳戶，並參閱
[桌面 App 快速入門](/zh-Hant/codex/quickstart?setup=app)。

## 更新應用程式

套件會在安裝期間設定已簽署的 OpenAI 套件庫。請使用發行版的套件管理工具安裝後續更新。

在 Ubuntu 或 Debian 上，請執行：

```bash
sudo apt update
sudo apt install --only-upgrade chatgpt

在 Fedora 上，請執行：

```bash
sudo dnf upgrade --refresh chatgpt

## 相容性與限制

預覽版支援
[支援的發行版與架構](#supported-distributions-and-architectures)一節所列的桌面發行版。
其他 Linux 發行版可能也能運作，但不在正式支援範圍內。

部分功能有各自的平台需求。例如，
[電腦](/zh-Hant/codex/computer-use)功能適用於 macOS 和 Windows，但 Linux 預覽版
目前尚未提供此功能。未來版本將新增 Linux 支援。

## Wayland 支援

原生 Wayland 支援仍處於實驗階段，並將持續改善。在 Wayland 工作階段中，應用程式會在 XWayland 可用時使用它。若要明確選用原生 Wayland，請先完全結束應用程式，再從終端啟動：

```bash
chatgpt --ozone-platform=wayland

在原生 Wayland 支援逐漸完善期間，部分功能可能無法完整運作，例如浮動視窗、視窗定位、焦點和鍵盤快速鍵。

## 後續步驟

- 請參閱[桌面 App 快速入門](/zh-Hant/codex/quickstart?setup=app)。
- 設定 [Chrome 擴充功能](/zh-Hant/codex/chrome-extension)，以便與瀏覽器整合。
- 審查本機專案和指令的[權限](/zh-Hant/codex/permissions)。
