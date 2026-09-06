<!-- source: https://learn.chatgpt.com/zh-Hant/docs/sandboxing -->

沙盒是一道界線，讓智慧體能自主行動，同時避免其
不受限制地存取您的電腦。當本機對話透過
**ChatGPT 桌面版應用程式**、 **Codex CLI** 或 **IDE 擴充功能** 執行指令時，這些指令會在
受限環境中執行，而非預設以完整存取權執行。

該環境界定智慧體可自行執行哪些操作，例如可修改哪些檔案，
以及指令能否使用網路。只要任務維持在
這些界線內，智慧體就能持續執行，不必停下來要求確認。當
智慧體需要越過界線時，就會進入核准流程。

  沙盒與核准是兩種相互配合、但作用不同的控制機制。
沙盒界定技術界線；核准政策則決定
智慧體何時必須在越過界線前停下來要求核准。

## 沙盒的作用

沙盒不只適用於內建的檔案
操作，也適用於啟動的指令。如果智慧體執行 `git`、套件管理器或測試執行器等工具，
這些指令會沿用相同的沙盒界線。

Codex 會在每個作業系統上採用平台原生的強制執行機制。其實作方式在
macOS、Linux、WSL2 與原生 Windows 上各不相同，但所有
介面的理念一致：為智慧體提供有明確界線的工作環境，讓例行任務能在
清楚的限制內自主執行。

## 為何重要

沙盒可減輕核准疲勞。智慧體不必要求您確認每一項
低風險指令，而能在您已核准的界線內讀取檔案、進行編輯，並執行例行專案
指令。

這也為智慧體式工作提供更清楚的信任模型。您不只是
相信智慧體的意圖，更是相信它會在
強制執行的限制內運作。如此一來，您就能更放心地讓智慧體獨立工作，
同時仍清楚知道它何時會停下來尋求協助。

## 開始使用

預設權限模式會自動套用沙盒機制。

### 先決條件

在 **macOS** 上，沙盒會使用內建的 Seatbelt
架構，無須額外設定即可運作。

在 **Windows** 上，若於 PowerShell 中執行，Codex 會使用原生的 [Windows
沙盒](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)；若於 WSL2 中執行，則會使用
Linux 沙盒實作。

在 **Linux 和 WSL2** 上，請先使用套件管理器安裝 `bubblewrap`：

  <div slot="ubuntu-debian">

```bash
sudo apt install bubblewrap

  </div>

  <div slot="fedora">

```bash
sudo dnf install bubblewrap

  </div>

Codex 會尋找 `bwrap`，並使用 `PATH` 中第一個找到的可執行檔。如果沒有可用的 `bwrap`
可執行檔，Codex 會改用隨附的輔助程式，但該程式
需要系統支援建立非特權使用者命名空間。安裝
提供 `bwrap` 的發行版套件，可確保此設定穩定運作。

缺少 `bwrap`，或輔助程式
無法建立所需的使用者命名空間時，Codex 會顯示啟動警告。在限制這項
AppArmor 設定的發行版上，應優先載入 `bwrap` AppArmor 設定檔，讓 `bwrap` 能
繼續運作，而無須在整個系統停用此限制。

  **Ubuntu AppArmor 注意事項：** 在 Ubuntu 25.04 上，從 Ubuntu 套件庫安裝 `bubblewrap`
  後，應可正常運作，無須額外設定 AppArmor。
`bwrap-userns-restrict` 設定檔隨附於 `apparmor` 套件中，路徑為
`/etc/apparmor.d/bwrap-userns-restrict`。

在 Ubuntu 24.04 上，Codex 仍可能警告無法建立所需的使用者
命名空間，即使已安裝 `bubblewrap` 亦然。請複製並載入額外的設定檔：

```bash
sudo apt update
sudo apt install apparmor-profiles apparmor-utils
sudo install -m 0644 \
  /usr/share/apparmor/extra-profiles/bwrap-userns-restrict \
  /etc/apparmor.d/bwrap-userns-restrict
sudo apparmor_parser -r /etc/apparmor.d/bwrap-userns-restrict

`apparmor_parser -r` 會將設定檔載入核心，無須重新啟動。您
也可以重新載入所有 AppArmor 設定檔：

```bash
sudo systemctl reload apparmor.service

如果該設定檔無法取得或未能解決問題，您可以使用以下方式停用
AppArmor 的非特權使用者命名空間限制：

```bash
sudo sysctl -w kernel.apparmor_restrict_unprivileged_userns=0

## 權限的運作方式

請使用目前介面上的權限控制項，變更 Codex 處理本機
操作的方式。

核准機制決定 Codex 何時應在執行操作前暫停，而沙盒則
決定指令可存取哪些檔案和網路資源。當
核准要求提供不同範圍，例如僅核准一次或核准整個工作階段時，
請選擇能讓任務繼續的最小範圍。預設應維持專案
界線；請使用不同的專案或工作樹，而不要
擴大對無關程式碼庫的存取權。

ChatGPT Work 會在受管理且隔離的環境中執行程式碼和 Shell 指令。
工作區政策和各工具專屬的控制項，會決定哪些能力
可供使用。如果此設定可用，請前往 **設定 \> 資料控制項 \> Work
網路存取** ，管理程式碼和 Shell 指令的網路存取。請開啟
**允許公用網際網路存取** ，讓這些指令能連線至公用
網際網路。關閉時，指令只能連線至受管理的允許清單所列的
必要主機名稱。

網頁搜尋、外掛程式與遠端瀏覽器各有獨立的控制項。
目前的程式碼或 Shell 執行作業結束，且 Work
重新整理其執行環境後，變更才會生效。ChatGPT 網頁版不提供本機
Codex 沙盒或核准模式選擇器。

在 ChatGPT 桌面版應用程式中，請使用撰寫工具下方的權限控制項。
視您的組態而定，選單可能包含 **要求核准**、
**代我核准** （適用於符合條件的核准要求）、 **完整存取權**，以及具名或
自訂的權限設定檔。

在 CLI 中，請輸入
[`/permissions`](/codex/developer-commands?surface=cli#cli-update-permissions-with-permissions)
以開啟權限選擇器，並變更作用中的權限設定檔。

在 IDE 擴充功能中，請使用撰寫工具下方的權限控制項。
視您的組態而定，選單可能包含 **要求核准**、
**代我核准** （適用於符合條件的核准要求）、 **完整存取權**，以及具名或
自訂的權限設定檔。

<div class="not-prose my-8 max-w-[18rem] mr-auto">
  
    
      
    
  
</div>

<a id="configure-defaults"></a>

## 設定預設值

若希望每次都以相同方式開始，請在 `config.toml` 中設定預設值。
[基本設定](/zh-Hant/codex/config-file/config-basic) 說明其運作方式，而
[組態參考資料](/zh-Hant/codex/config-file/config-reference) 則記載以下項目的確切鍵：
`sandbox_mode`、`approval_policy`、`approvals_reviewer` 與
`sandbox_workspace_write.writable_roots`。您可以使用這些設定，決定智慧體預設可擁有多少
自主權、可寫入哪些目錄、應在何時
暫停以要求核准，以及由誰審查符合條件的核准要求。

概括而言，常見的沙盒模式如下：

- `read-only`：智慧體可以檢查檔案，但未經核准，無法編輯檔案或執行
  指令。
- `workspace-write`：智慧體可以讀取檔案、在工作區內編輯檔案，並在該界線內執行
  例行本機指令。這是本機工作的預設模式，
  可讓操作更加順暢。
- `danger-full-access`：智慧體執行時不受沙盒限制。這會移除
  檔案系統與網路界線，因此只應在您希望
  智慧體以完整存取權執行操作時使用。

常見的核准政策如下：

- `untrusted`：智慧體會在執行不屬於其受信任
  集合的指令前，先要求核准。
- `on-request`：智慧體預設會在沙盒內工作，只有在
  需要越過該界線時才會要求核准。
- `never`：智慧體不會因核准提示而暫停。

採用互動式核准時，您也可以透過
`approvals_reviewer` 指定審查者：

- `user`：核准提示會顯示給使用者。這是預設值。
- `auto_review`：符合條件的核准提示會交由審查智慧體處理（請參閱
[自動審查](/zh-Hant/codex/sandboxing/auto-review)）。

完整存取權是指同時使用 `sandbox_mode = "danger-full-access"` 與
`approval_policy = "never"`。相較之下，風險較低的本機自動化
預設組合是同時使用 `sandbox_mode = "workspace-write"` 與
`approval_policy = "on-request"`，或使用對應的 CLI 旗標
`--sandbox workspace-write --ask-for-approval on-request`。接著，您可以保留
`approvals_reviewer = "user"` 以採用手動核准，或設定
`approvals_reviewer = "auto_review"` 以自動審查核准要求。

若智慧體需要跨多個目錄工作，您可透過可寫入根目錄
擴充它能修改的範圍，而不必完全移除沙盒。如果
您需要更寬或更窄的信任界線，請調整預設沙盒模式
與核准政策，而不要依賴一次性的例外。

當工作流程需要特定例外時，請使用 [規則](/zh-Hant/codex/agent-configuration/rules)。規則
可針對沙盒外的指令前綴設定允許、要求核准或禁止，這通常
比大幅擴大存取權更合適。若要瞭解 IDE 專屬的設定
入口，請參閱 [Codex IDE 擴充功能設定](/codex/developer-settings?surface=ide)。

自動審查功能可用時，不會改變沙盒界線。它是
該界線上核准要求可選用的 `approvals_reviewer` 設定之一，例如
沙盒權限提升、遭封鎖的網路存取，或仍需核准且會產生副作用的工具呼叫。
沙盒內已獲允許的操作無須額外審查即可執行。
若要瞭解審查者生命週期、觸發類型、拒絕的
語意及組態詳細資訊，請參閱
[自動審查](/zh-Hant/codex/sandboxing/auto-review)。

平台詳細資訊載於各平台的專屬文件中。如需瞭解原生 Windows 的設定、
行為與疑難排解，請參閱 [Windows](/zh-Hant/codex/windows/windows-sandbox)。若要瞭解管理員
相關要求，以及組織層級對沙盒與核准的限制，請參閱
[代理核准與安全性](/zh-Hant/codex/agent-approvals-security)。
