<!-- source: https://learn.chatgpt.com/zh-Hant/docs/windows/wsl -->

使用 WSL2 時，Codex 會在 Linux 環境中執行，而非使用
原生 [Windows 沙盒](/zh-Hant/codex/windows/windows-sandbox)。如果您需要 Linux 原生
工具、程式碼庫與開發工作流程已位於 WSL2 中，或
兩種原生 Windows 沙盒模式都無法在您的環境中運作，請選擇 WSL2。

WSL1 支援至 Codex `0.114` 版本。自 Codex `0.115` 起，Linux
沙盒改用 `bubblewrap`，因此不再支援 WSL1。

## 從 WSL 內啟動 VS Code

如需逐步操作說明，請參閱 [官方 VS Code WSL 教學](https://code.visualstudio.com/docs/remote/wsl-tutorial)。

### 必要條件

- 已安裝 WSL 的 Windows。若要安裝 WSL，請以系統管理員身分開啟 PowerShell，然後執行 `wsl --install`（Ubuntu 是常見的選擇）。
- 已安裝 [WSL 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) 的 VS Code。

### 從 WSL 終端開啟 VS Code

```bash
# From your WSL shell
cd ~/code/your-project
code .

這會開啟 WSL 遠端視窗、視需要安裝 VS Code Server，並確保整合式終端在 Linux 中執行。

### 確認您已連線至 WSL

- 尋找顯示 `WSL: <distro>` 的綠色狀態列。
- 整合式終端應顯示 Linux 路徑（例如 `/home/...`），而非 `C:\`。
- 您可以使用以下指令驗證：

  ```bash
  echo $WSL_DISTRO_NAME

  此指令會輸出您的發行版名稱。

  如果狀態列中沒有顯示「WSL: ...」，請按 `Ctrl+Shift+P`，選擇
`WSL: Reopen Folder in WSL`，並將程式碼庫存放在 `/home/...` 下（而不是
`C:\`），以獲得最佳效能。

  如果 Windows App 或專案選擇器未顯示您的 WSL 程式碼庫，請在檔案選擇器或檔案總管中輸入
<code>\\wsl$</code>，然後前往您所用
  發行版的主目錄。

## 搭配 WSL 使用 Codex CLI

請在已提升權限的 PowerShell 或 Windows Terminal 中執行以下指令：

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

接著，請在 WSL 殼層中執行以下指令：

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## 在 WSL 中處理程式碼

- 在 <code>/mnt/c/...</code> 這類 Windows 掛載路徑中處理程式碼，可能比在 Windows 原生路徑中更慢。請將程式碼庫放在 Linux 主目錄下（例如 <code>~/code/my-app</code>），以提升 I/O 速度，並減少符號連結和權限問題：
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- 如需從 Windows 存取檔案，可在檔案總管的 <code>\\wsl$\\Ubuntu\\home&lt;user\></code> 路徑下找到這些檔案。

## 疑難排解與常見問題

- 請確認工作目錄不在 <code>/mnt/c</code> 下。請將程式碼庫移至 WSL（例如 <code>~/code/...</code>）。
- 如有需要，請增加 WSL 的記憶體與 CPU，並將 WSL 更新至最新版本：
  ```powershell
  wsl --update
  wsl --shutdown

確認 WSL 中有該二進位檔，且其所在目錄已加入 `PATH`：

```bash
which codex || echo "codex not found"

如果找不到二進位檔，請依照 [Codex CLI 設定說明](#use-codex-cli-with-wsl)。
