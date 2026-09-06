<!-- source: https://learn.chatgpt.com/zh-Hant/docs/windows/windows-app -->

# Windows 版 ChatGPT 桌面應用程式

[適用於 Windows 的 ChatGPT 桌面版應用程式](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)提供統一介面，讓你
跨專案工作、同時進行多個對話，並審查結果。
Windows 應用程式支援工作樹、排程任務、Git
功能、內建瀏覽器、檔案預覽、外掛程式和技能等核心工作流程。
它透過 PowerShell 和
[Windows 沙盒](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)在 Windows 上以原生方式執行；你也可以設定為
在[適用於 Linux 的 Windows 子系統 2 (WSL2)](#windows-subsystem-for-linux-wsl) 中執行。

  
    
  

## 下載 ChatGPT 桌面版應用程式

下載適用於 Windows 的[ChatGPT 桌面版應用程式](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi)。

接著依照[快速入門](/zh-Hant/codex/quickstart?setup=app)開始使用。

如需企業安裝和更新選項，請參閱
[部署 Windows 應用程式](/zh-Hant/codex/enterprise/windows-deployment)。

如果偏好以指令列安裝，請執行：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## 原生沙盒

當智慧體在 PowerShell 中執行時，Windows 上的 ChatGPT 桌面版應用程式支援原生[Windows 沙盒](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)；當智慧體在[適用於 Linux 的 Windows 子系統 2 (WSL2)](#windows-subsystem-for-linux-wsl) 中執行時，則使用 Linux 沙盒。無論採用哪種模式，若要套用沙盒保護，請先在撰寫工具下方選取 **要求核准** ，再向 Codex 傳送訊息。

  以完整存取權模式執行 Codex，表示 Codex 不受專案
  目錄限制，而且可能無意間執行破壞性操作，導致
  資料遺失。請保留沙盒邊界，並使用
[規則](/zh-Hant/codex/agent-configuration/rules)設定特定例外；或者，將
[核准政策設為
  永不](/zh-Hant/codex/agent-approvals-security#run-without-approval-prompts)，讓
  Codex 嘗試在不要求提升權限的情況下解決問題；具體方式
  取決於你的[核准與安全性設定](/zh-Hant/codex/agent-approvals-security)。

## 自訂開發環境設定

<section class="feature-grid">

<div>

### 偏好的編輯器

請選擇 **開啟**時預設使用的應用程式，例如 Visual Studio、VS Code 或其他
編輯器。你可以針對個別專案覆寫這項預設選擇。如果先前已針對某個專案從
 **開啟** 選單選擇其他應用程式，則會優先採用該專案的
專屬設定。

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### 整合式終端

你也可以選擇預設的整合式終端。
可用選項取決於你安裝的工具，包括：

- PowerShell
- 命令提示字元
- Git Bash
- WSL

這項變更只適用於新的終端工作階段。
如果你已開啟整合式終端，請重新啟動應用程式或開始新對話，
新的預設終端才會顯示。

</div>

  
    
  

</section>

## 適用於 Linux 的 Windows 子系統 (WSL)

根據預設，ChatGPT 桌面版應用程式會使用 Windows 原生 Codex 智慧體。這表示智慧體
會在 PowerShell 中執行指令。應用程式仍可處理位於
適用於 Linux 的 Windows 子系統 2 (WSL2) 中的專案，並在需要時使用 `wsl` CLI。

若要新增 WSL 檔案系統中的專案，請按一下 **新增專案**
或按下 <kbd>Ctrl</kbd>+<kbd>O</kbd>，接著在檔案總管視窗輸入 `\\wsl$\`。
然後選擇你的 Linux 發行版本，以及你
想開啟的資料夾。

若打算繼續使用 Windows 原生智慧體，建議將專案儲存在
Windows 檔案系統，並在 WSL 中透過
`/mnt/<drive>/...` 存取。相較於直接從 WSL 檔案系統開啟專案，
這種設定更可靠。

若要讓智慧體本身在 WSL2 中執行，請開啟 **[設定](codex://settings)**，
將智慧體從 Windows 原生切換為 WSL，並 **重新啟動應用程式**。
變更必須在重新啟動後才會生效。重新啟動後，你的專案應會
保留原狀。

Codex `0.114` 及更早版本支援 WSL1。自 Codex `0.115` 起，Linux
沙盒改用 `bubblewrap`，因此不再支援 WSL1。

  
    
  

整合式終端的設定與智慧體彼此獨立。終端選項請參閱
[自訂開發環境設定](#customize-for-your-dev-setup)。
你可以讓智慧體在 WSL 中執行，同時讓終端使用 PowerShell；
也可以視工作流程需要，讓兩者都使用 WSL。

## 實用的開發工具

預先安裝下列幾項常用開發工具，可讓 Codex 發揮最佳效果：

- **Git**：支援 ChatGPT 桌面版應用程式的審查窗格，讓你檢查或
  還原變更。
- **Node.js**：智慧體可使用這項常用工具，更有效率地
  執行任務。
- **Python**：智慧體可使用這項常用工具，更有效率地
  執行任務。
- **.NET SDK**：建置 Windows 原生應用程式時很實用。
- **GitHub CLI**：支援 ChatGPT 桌面版應用程式中的 GitHub 專屬功能。

若要透過 Windows 預設套件管理員 `winget` 安裝這些工具，請將下列內容
貼到[整合式終端](/zh-Hant/codex/integrated-terminal)，或
請 Codex 代為安裝：

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

安裝 GitHub CLI 後，請執行 `gh auth login`，以啟用
應用程式中的 GitHub 功能。

如果需要其他版本的 Python 或 .NET，請將套件 ID 更換為
所需版本對應的套件 ID。

## 疑難排解與常見問題

### 以提升權限執行指令

如果需要 Codex 以提升權限執行指令，請以系統管理員身分啟動 ChatGPT
桌面版應用程式本身。安裝後，開啟「開始」功能表，
找到應用程式，並選擇 **以系統管理員身分執行**。Codex 智慧體會繼承該
權限層級。

### PowerShell 執行原則阻擋指令

如果你之前從未在 PowerShell 中使用 Node.js 或 `npm` 等工具，
Codex 智慧體或整合式終端可能會遇到執行原則錯誤。

如果 Codex 為你建立 PowerShell 指令碼，也可能發生這種情況。
此時，你可能需要改用限制較寬鬆的執行原則，
PowerShell 才能執行這些指令碼。

錯誤訊息可能如下：

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

常見的解決方式是將執行原則設為 `RemoteSigned`：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

如需詳細資訊和其他選項，請先查看 Microsoft 的
[執行原則指南](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies)，
再變更原則。

### Windows 上的本機環境指令碼

如果你的[本機環境](/zh-Hant/codex/environments/local-environment)使用跨平台
指令，例如 `npm` 指令碼，就可以為所有平台共用一份設定指令碼或
一組動作。

如果需要 Windows 特有的行為，請建立 Windows 專用的設定指令碼，
或建立 Windows 專用的動作。

動作會在整合式終端所使用的環境中執行。詳情請參閱
[自訂開發環境設定](#customize-for-your-dev-setup)。

本機設定指令碼會在智慧體的環境中執行：如果智慧體使用 WSL，便在 WSL 中執行；
否則會在 PowerShell 中執行。

### 與 WSL 共用組態、驗證資訊和工作階段

Windows 應用程式與 Windows 原生 Codex 使用相同的 Codex 主目錄：
`%USERPROFILE%\.codex`。

如果你也在 WSL 中執行 Codex CLI，CLI 預設會使用 Linux
主目錄，因此不會自動與 Windows 應用程式共用組態、快取的驗證資訊，
或工作階段記錄。

若要共用這些內容，請採用下列其中一種方法：

- 將 WSL 的 `~/.codex` 與檔案系統中的 `%USERPROFILE%\.codex` 同步。
- 設定 `CODEX_HOME`，讓 WSL 指向 Windows 上的 Codex 主目錄：

```bash

```

若要在每個 shell 中套用此設定，請將其加入 WSL 的 shell 設定檔，
例如 `~/.bashrc` 或 `~/.zshrc`。

### 無法使用 Git 功能

如果 Windows 上未原生安裝 Git，應用程式將無法使用部分
功能。請執行 `winget install Git.Git` 來安裝，可使用 PowerShell 或 `cmd.exe`。

### 從 `\\wsl$` 開啟的專案偵測不到 Git

目前，如果想針對也可從 WSL 存取的專案使用 Windows 原生智慧體，
最可靠的因應方式是將專案儲存在 Windows 原生磁碟機上，
再透過 `/mnt/<drive>/...` 在 WSL 中存取。

### `Cmder` 未列在「開啟」對話方塊中

如果已安裝 `Cmder`，但未出現在 Codex 的「開啟」對話方塊中，請將它加入
Windows「開始」功能表：以滑鼠右鍵按一下 `Cmder`，選擇 **新增至 \[開始\]**，然後
重新啟動 Codex 或重新開機。
