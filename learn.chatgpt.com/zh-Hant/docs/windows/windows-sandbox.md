<!-- source: https://learn.chatgpt.com/zh-Hant/docs/windows/windows-sandbox -->

在 Windows 上透過原生 [ChatGPT 桌面版應用程式](/zh-Hant/codex/windows/windows-app)、
[CLI](/zh-Hant/codex/cli) 或 [IDE 擴充功能](/zh-Hant/codex/ide)使用 Codex。

Windows 版 ChatGPT 桌面版應用程式支援多項核心工作流程，例如平行對話、
工作樹、排程任務、Git 功能、內建瀏覽器、檔案預覽、
外掛程式和技能。

這款應用程式可在 PowerShell 中透過 Windows 沙盒原生執行，不需要
WSL 或虛擬機器。如此一來，Codex 可沿用 Windows 原生
工作流程，同時落實檔案系統與網路權限限制。

  
    
  

<div class="mb-8">
  
</div>

原生 Windows 沙盒提供兩種模式：

- 在 Windows 上以防護較強的 `elevated` 沙盒原生執行，
- 在 Windows 上以備援的 `unelevated` 沙盒原生執行。

<span id="windows-sandbox"></span>

## 設定 Windows 沙盒

在 Windows 上原生執行 Codex 時，智慧體模式會使用 Windows 沙盒，
禁止在工作資料夾以外寫入檔案系統，並封鎖未經你明確核准的
網路存取。

原生 Windows 沙盒支援兩種模式，可在
`config.toml` 中設定：

```toml
[windows]
sandbox = "elevated" # or "unelevated"

`elevated` 是建議優先使用的原生 Windows 沙盒。它使用專用的
低權限沙盒使用者、檔案系統權限界限、防火牆
規則，以及在沙盒中執行指令所需的本機原則變更。

`unelevated` 是備援的原生 Windows 沙盒。它會使用從目前使用者衍生的
受限 Windows Token 執行指令，套用以 ACL 為基礎的
檔案系統界限，並以環境層級的離線控制取代
離線使用者專用的防火牆規則。其防護弱於 `elevated`，但在
須經系統管理員核准的設定遭到本機或
企業原則封鎖時，仍可派上用場。

若兩種模式都可用，請使用 `elevated`。若預設的原生沙盒
無法在你的環境中運作，可在排解設定問題期間使用 `unelevated`
作為備援。

企業系統管理員可透過
[`requirements.toml`](/zh-Hant/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)，限制 Codex 可使用的原生沙盒實作：

```toml
[windows]
allowed_sandbox_implementations = ["elevated"]

此範例要求使用 `elevated` 沙盒，並防止使用者
改用 `unelevated`。若要允許任一種實作，請同時列入這兩個值；
未選擇模式時，Codex 會優先使用 `elevated`。請參閱
[`requirements.toml` 參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)，瞭解
支援的值。

預設情況下，兩種沙盒模式也都會使用私人桌面，以加強 UI
隔離。只有在相容性需要時，才設定 `windows.sandbox_private_desktop = false`，以使用
舊版 `Winsta0\\Default` 行為。

### 沙盒權限

  以完整存取權模式執行 Codex 時，其操作不再侷限於你的專案
  目錄，可能無意間執行破壞性操作，導致
  資料遺失。為了更安全地執行自動化，請保留沙盒界限，並透過
[規則](/zh-Hant/codex/agent-configuration/rules)處理特定例外；或將你的
[核准政策設為
  never](/zh-Hant/codex/agent-approvals-security#run-without-approval-prompts)，讓
  Codex 嘗試在不要求提升權限的情況下解決問題，
  實際行為取決於你的 [核准與安全性設定](/zh-Hant/codex/agent-approvals-security)。

### Windows 版本對照表

| Windows 版本                  | 支援層級   | 備註                                                                                                                                                                                 |
| -------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows 11                       | 建議使用     | 這是在 Windows 上使用 Codex 的最佳基準環境。若要將企業部署標準化，請使用此版本。                                                                                       |
| 較新且已完整更新的 Windows 10 | 盡力支援     | 可以運作，但可靠性不如 Windows 11。在 Windows 10 上，Codex 需要包含 ConPTY 在內的新式主控台支援。實際上，必須使用 Windows 10 1809 版或更新版本。 |
| 較舊的 Windows 10 組建版本          | 不建議使用 | 較可能缺少 ConPTY 等必要的主控台元件，也較容易在企業環境中設定失敗。                                                                          |

其他環境前提：

- `winget` 應可正常使用。若缺少此工具，請先更新 Windows，或安裝
  Windows 套件管理員，再設定 Codex。
- 建議使用的原生沙盒須完成經系統管理員核准的設定。
- 即使作業系統版本本身符合要求，某些由企業管理的裝置
仍會封鎖必要的設定步驟。

### 授予沙盒讀取權限

若指令因 Windows 沙盒無法讀取目錄而失敗，請使用：

```text
/sandbox-add-read-dir C:\absolute\directory\path

路徑必須是現有目錄的絕對路徑。指令成功執行後，在目前工作階段內，後續於沙盒中執行的指令即可讀取該目錄。

<span id="windows-subsystem-for-linux"></span>

預設請使用原生 Windows 沙盒。請在以下情況選擇 [WSL](/zh-Hant/codex/windows/wsl)：
需要 Linux 原生工具、工作流程已在 WSL2 中執行，或
兩種原生 Windows 沙盒模式皆無法滿足需求。

## 疑難排解與常見問題

為受管理的 Windows 電腦進行疑難排解時，請先檢查原生
沙盒模式、Windows 版本，以及 Codex 顯示的任何原則錯誤。大多數原生
Windows 支援問題都源於沙盒設定、登入權限或檔案系統
權限，而非編輯器本身。

若 Codex 無法完成 `elevated` 沙盒設定，最常見原因
如下：

- Windows UAC 或系統管理員提示遭到拒絕，
- 電腦不允許建立本機使用者或群組，
- 電腦不允許變更防火牆規則，
- 電腦封鎖沙盒使用者所需的登入權限，
- 或其他企業原則封鎖部分設定流程。

可嘗試的做法：

1. 請再次嘗試設定 `elevated` 沙盒；若環境允許，
   請核准系統管理員提示。
2. 若公司的筆記型電腦封鎖這項操作，請詢問 IT 團隊，確認該電腦
是否允許經系統管理員核准的設定，包括建立本機使用者或群組、設定防火牆，
以及授予沙盒使用者所需的登入權限。
3. 若預設設定仍然失敗，請使用 `unelevated` 沙盒，
   以便在調查問題期間繼續工作。

這表示 Codex 無法在你的電腦上完成防護較強的 `elevated` 沙盒
設定。

- Codex 仍可在沙盒模式下執行。
- 此模式仍會套用以 ACL 為基礎的檔案系統界限，但不會使用
  `elevated` 的獨立沙盒使用者界限，且網路
  隔離較弱。
- 這是實用的備援方案，但不是企業長期使用的首選
組態。

若你使用受管理的企業筆記型電腦，最佳的長期解決方式通常是請 IT 團隊協助，
讓 `elevated` 沙盒正常運作。

若沙盒中的指令執行失敗並顯示錯誤 `1385`，表示 Windows 拒絕沙盒使用者使用
啟動指令所需的登入類型。

實際上，這通常表示 Codex 已成功建立沙盒使用者，
但 Windows 原則仍阻止這些使用者在沙盒中
執行指令。

處理方式：

1. 請詢問 IT 團隊，裝置原則是否已將必要的登入權限
授予 Codex 所建立的沙盒使用者。
2. 若問題只影響部分電腦或團隊，
請比較群組原則或 OU 是否存在差異。
3. 如果需要立即繼續工作，請暫時使用 `unelevated` 沙盒，等待
   原則問題調查完成。
4. 請傳送 `CODEX_HOME/.sandbox/sandbox.log`，並附上 Windows 版本以及
   失敗情況的簡短說明。

Codex 可能會警告某些資料夾允許 `Everyone` 寫入。

如果看到此警告，表示這些資料夾的 Windows 權限設定過於寬鬆，
導致沙盒無法完整保護這些資料夾。

處理方式：

1. 檢查 Codex 在警告中列出的資料夾。
2. 若這項變更適合您的環境，請移除 `Everyone` 對這些資料夾的
   寫入權限。
3. 修正這些權限後，請重新啟動 Codex
或再次執行沙盒設定。

如果不確定如何變更這些權限，請向 IT 團隊尋求協助。

部分 Codex 對話會刻意在沒有對外網路存取權的情況下執行，
具體取決於所使用的權限模式。

如果任務因無法連上網路而失敗：

1. 檢查該任務原本是否應在網路停用的情況下執行。
2. 如果原本預期可以存取網路，請重新啟動 Codex 並再試一次。
3. 如果問題持續發生，請收集沙盒記錄，讓團隊檢查
這台電腦的沙盒是否處於設定不完整或故障狀態。

以下變更可能導致這種情況：

- 移動程式碼庫或工作區，
- 變更電腦權限，
- 變更 Windows 原則，
- 或進行其他系統組態變更。

可嘗試以下做法：

1. 重新啟動 Codex。
2. 再次嘗試設定 `elevated` 沙盒。
3. 若問題仍未解決，請使用 `unelevated` 沙盒作為
   暫時的備用方案。
4. 收集沙盒記錄以供審查。

如果問題仍未解決，請傳送：

- `CODEX_HOME/.sandbox/sandbox.log`

一併提供以下資訊也會很有幫助：

- 您嘗試執行之操作的簡短說明，
- 是 `elevated` 沙盒失敗，還是使用了 `unelevated` 沙盒，
- App 中顯示的任何錯誤訊息，
- 是否看到 `1385`，或其他 Windows 或 PowerShell 錯誤，
- 以及您使用的是 Windows 11 還是 Windows 10。

請勿傳送：

- `CODEX_HOME/.sandbox-secrets/` 的內容

系統可能缺少部分原生相依項目所需的 C++ 開發工具：

- Visual Studio Build Tools（C++ 工作負載）
- Microsoft Visual C++ Redistributable (x64)
- 使用 `winget` 時，請執行 `winget install --id Microsoft.VisualStudio.2022.BuildTools -e`

安裝完成後，請完全關閉 VS Code，再重新啟動。
