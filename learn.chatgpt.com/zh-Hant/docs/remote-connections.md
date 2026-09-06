<!-- source: https://learn.chatgpt.com/zh-Hant/docs/remote-connections -->

Desktop,
  Storage,
  Terminal,
} from "@components/react/oai/platform/ui/Icon.react";

遠端連線可讓你存取在其他裝置或電腦上執行的工作。
在 ChatGPT 行動應用程式中開啟 **遠端** ，即可處理
已連線的 Mac 或 Windows 裝置上的 ChatGPT 或 Codex 對話。你也可以在另一台
執行 ChatGPT 桌面版應用程式的受支援裝置上繼續工作，或將應用程式連線至
SSH 主機上的專案。

遠端存取會使用已連線主機的專案、對話、檔案、憑證、
權限、外掛程式、電腦功能、瀏覽器設定和本機工具。

## 可從遠端進行的操作

- 在主機上的專案中開始新對話，或繼續現有對話。
- 傳送後續指示、回答問題，並引導進行中的工作。
- 核准指令和其他動作。
- 審查輸出、差異、測試結果、終端輸出和螢幕擷取畫面。
- 在 ChatGPT 完成任務或需要你處理時接收通知。
- 在已連線的主機和對話之間切換。

以下各節說明如何在 ChatGPT 行動應用程式中開啟 **遠端** ，以存取
桌面主機。若要將 Codex 連線至 SSH 主機上的專案，請參閱
[連線至 SSH 主機](#connect-to-an-ssh-host)。

<div class="not-prose my-6 max-w-4xl rounded-xl bg-[url('/images/codex/codex-wallpaper-1.webp')] bg-cover bg-center p-4 md:p-8">
  
    
      
    
  
</div>

<a id="before-you-set-up-mobile-access"></a>

## 設定遠端功能前

  遠端功能支援在 macOS 或 Windows 上執行 ChatGPT 桌面版應用程式的主機。
  你可以透過 iOS 或 Android 上的 ChatGPT 控制主機；若另一台 Mac 或
  Windows 裝置提供 **控制其他裝置** 功能，也可從該裝置進行控制。功能是否
  可用，可能因推出進度而異。

請確認你已具備以下項目：

- 你要使用的 ChatGPT 帳戶和工作區具有 Codex 存取權。
- iOS 或 Android 裝置上的最新版 ChatGPT 行動應用程式。如果應用程式未顯示 **遠端**
  功能，請先更新 ChatGPT。
- 最新版適用於 macOS 或 Windows 的 ChatGPT 桌面版應用程式，必須在保持喚醒、
已連網並登入相同帳戶和工作區的主機上執行。行動裝置設定須從該應用程式
開始；無法透過 Codex CLI 或 IDE 擴充功能進行設定。
- 該帳戶或工作區所需的多重要素身分驗證、SSO 或通行密鑰
組態。

如果你透過 ChatGPT 工作區使用 Codex，管理員可能需要先啟用
遠端控制存取權，你才能從手機連線。

<a id="set-up-mobile-access"></a>

## 設定遠端功能

請從要連線之主機上的 ChatGPT 桌面版應用程式開始設定。設定流程會為該主機
啟用遠端存取，並顯示可供你以手機
掃描的 QR 圖碼。
該 QR 圖碼會將手機與主機配對。請將每支手機或每台支援桌面應用程式的
裝置，與其需要控制的每台主機分別配對。

  自 2026 年 6 月 8 日起曾使用的現有連線會維持配對。若自 2026 年 6 月 8 日起
未曾使用某個現有連線，請更新兩個應用程式，並重新配對
裝置。

1. 開始設定遠端功能。

   在主機上開啟 ChatGPT 桌面版應用程式。前往 **設定** \>
**連線** \> **控制此 Mac 或 PC**，然後選取 **設定** 或
**新增**。核准遠端存取，並完成系統要求的驗證。

2. 掃描 QR 圖碼。

   使用手機掃描應用程式顯示的 QR 圖碼。該圖碼會開啟 ChatGPT，
讓你完成行動應用程式與主機的連線。

3. 在 ChatGPT 中完成設定。

   ChatGPT 會開啟遠端設定流程。確認使用相同的 ChatGPT 帳戶
和工作區，再完成必要的多重要素身分驗證、SSO
或通行密鑰驗證步驟。設定成功後，該主機就會顯示在你手機的
遠端功能中。

4. 審查主機設定。

   在主機的應用程式中，前往 **設定** \> **連線** ，即可管理已連線的
   裝置。你也可以選擇是否讓電腦保持喚醒、啟用
   電腦功能，或安裝 Chrome 擴充功能。

  

## 選擇連線對象

先使用你平常操作 ChatGPT 的筆記型電腦或桌上型電腦。若需要持續存取或使用不同環境，
再新增持續開機的電腦或 SSH 主機。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>你的筆記型電腦或桌上型電腦</span></span>

連線至已安裝桌面應用程式的 Mac 或 Windows PC，即可從遠端存取
你原本使用的相同專案、對話、憑證、外掛程式和本機
設定。

如果該電腦進入睡眠狀態、失去網路連線或關閉應用程式，遠端存取
就會中斷，直到電腦再次可用。如果你將這台電腦當作主機裝置，
請讓它持續接通電源；若提供相應選項，請在主機的連線設定中讓電腦
保持喚醒。

Mac 筆記型電腦只要保持上蓋開啟並接通
電源，即可維持遠端存取。若闔上上蓋，還必須連接外接顯示器。選擇
**睡眠** 仍會中斷遠端存取。

Windows 主機若要執行使用
[電腦](/zh-Hant/codex/computer-use)功能的任務，請讓工作階段保持解鎖且可用。Windows 上的電腦功能會在
前景執行，因此遠端控制最適合在主機桌面專供任務使用時，
開始或檢查工作。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>專用的持續開機電腦</span></span>

如果你希望 ChatGPT 在較長時間的工作期間持續保持
可連線，請使用專用且持續開機的 Mac 或 Windows PC。

請在該電腦上安裝 ChatGPT 或
Codex 要使用的專案、憑證、MCP 伺服器、技能和工具。

### <span class="not-prose inline-flex items-center gap-3 align-middle"><span class="inline-flex h-7 w-7 shrink-0 items-center justify-center rounded-md bg-surface-secondary text-secondary"></span><span>遠端開發環境</span></span>

如果專案已位於遠端環境，請使用 SSH 主機或受管理的遠端開發環境。
請先將桌面應用程式主機連線至該環境；手機仍會連線至同一台
主機，而 ChatGPT 則會在遠端環境中工作，並使用該環境的
相依項目、安全性政策及運算
資源。

如需 SSH 設定的詳細資訊，請參閱[連線至 SSH 主機](#connect-to-an-ssh-host)。

  若要在持續開機的電腦或遠端主機上執行瀏覽器或桌面任務，請在該主機上啟用
電腦功能並安裝 Chrome 擴充功能。

## 已連線主機提供的項目

你的手機會將提示詞、核准和後續訊息傳送給 ChatGPT。已連線的
主機則提供 ChatGPT 使用的環境。

這表示：

- 程式碼庫檔案和本機文件來自已連線的主機。
- Shell 指令會在該主機或遠端環境中執行。
- MCP 伺服器、技能、瀏覽器存取權及電腦功能，均來自該主機的
組態。
- 已登入的網站和桌面應用程式，只有在主機能夠
存取時才可使用。
- 沙盒設定、安全性控制措施和動作核准，仍適用於
已連線的工作階段。

安全中繼層可讓你的已授權 ChatGPT 裝置存取受信任的
電腦，同時避免將這些電腦直接暴露於公開網際網路。

## 在另一台裝置上接續工作

你可以從另一台已登入、執行 ChatGPT 桌面版應用程式
且支援遠端控制的裝置繼續工作。例如，若筆記型電腦暫時無法使用，你可以
先用手機在持續開機的主機上開始對話，之後再於筆記型電腦上開啟
應用程式，繼續同一段對話。

在支援此功能的 Mac 或 Windows 裝置上，前往 **設定 \>
連線 \> 控制其他裝置** ，即可新增另一台主機。同一台裝置可以同時允許
遠端存取，並控制另一台裝置。

  

## 連線至 SSH 主機

在 ChatGPT 桌面版應用程式中，從 SSH 主機新增遠端專案，並讓對話使用遠端檔案系統與 Shell。遠端專案中的對話會在遠端主機上執行指令、讀取檔案並寫入變更。

遠端主機的設定應符合一般 SSH 存取所採用的安全標準：使用受信任的金鑰、最低權限帳戶，且不得設置無須身分驗證的公開監聽服務。

1. 將主機新增至 SSH 設定檔，讓 Codex 自動探索該主機。

   ```text
   Host devbox
     HostName devbox.example.com
     User you
     IdentityFile ~/.ssh/id_ed25519

   Codex 會從 `~/.ssh/config` 讀取明確指定的主機別名，並使用
   OpenSSH 解析，同時忽略僅以模式定義的主機。

2. 確認可從執行應用程式的電腦透過 SSH 連線至該主機。

   ```bash
   ssh devbox

3. 在遠端主機上安裝 Codex 並完成身分驗證。

   應用程式會透過 SSH 啟動遠端 Codex App Server，並使用遠端
   使用者的登入 Shell。請確認 `codex` 指令可在
   遠端主機的該 Shell 中透過 `PATH` 執行。

4. 在應用程式中開啟 **設定 \> 連線**，新增或啟用 SSH 主機，再
   選擇遠端專案資料夾。

  

<a id="hand-off-a-thread-between-hosts"></a>
<a id="hand-off-a-chat-between-hosts"></a>
<a id="hand-off-a-task-between-hosts"></a>

## 在主機之間移交對話

移交功能可在本機電腦與已連線的遠端主機之間轉移現有對話及其 Git 狀態。您可以先在本機開始工作，再到遠端電腦的工作樹中繼續，之後再將對話移交回本機。

移交對話前，請先連線至目的地主機，並在該主機上儲存對應同一 Git 程式碼庫的專案。如果專案是程式碼庫的子目錄，請在兩部主機上儲存相同的子目錄。Codex 只會顯示已儲存相符專案的目的地主機。

若要移交對話：

1. 在桌面應用程式中開啟對話。
2. 在對話底部選取目前的執行位置，接著選取
   目的地主機。選取 **此電腦** ，即可將遠端對話
   移交回本機電腦。
3. 審查目的地與分支，然後選取 **移交**。

Codex 會在目的地主機上建立或重複使用工作樹，傳輸對話與 Git 狀態，並將對話切換至該主機。如果對話正在執行，移交時會先中斷目前的回應，再移轉對話。

您也可以在另一段對話中，要求 Codex 將指定名稱的對話移交至已連線的主機。Codex 無法移交提出要求的對話，也不支援將對話移交至 Codex 雲端環境。

## 身分驗證與網路暴露

遠端連線會使用 SSH 啟動及管理遠端 Codex App Server。請勿在共用或公用網路上直接暴露 App Server 的傳輸通道。

若要存取目前網路以外的遠端電腦，請使用 VPN 或網狀網路工具，不要將 App Server 直接暴露在網際網路上。

## 疑難排解

### 手機上看不到主機

確認主機上的桌面應用程式正在執行，且已啟用 **允許
其他裝置連線**，並確認兩部裝置使用相同的 ChatGPT 帳戶與
工作區。如果您自 2026 年 6 月 8 日起未曾使用該連線，請更新兩個
應用程式，並重新配對裝置。

### 重新登入後遠端控制為關閉狀態

登出 ChatGPT 會關閉 **遠端控制**，但不會移除
現有的裝置配對。重新登入後，請開啟 **遠端控制** ，以
恢復先前的連線狀態。

如果開啟 **遠端控制** 並選取 **新增** 後出現錯誤，
請重新啟動主機上的 ChatGPT 桌面版應用程式，然後再試一次。

### 核准要求未出現

在 ChatGPT 行動版應用程式中開啟 **遠端**。確認手機與主機使用
相同的 ChatGPT 帳戶及工作區，然後重新掃描 QR 碼，或從主機重新開始
設定。若您使用 ChatGPT 工作區，請要求管理員確認
已啟用遠端控制存取權。

### 遠端工作階段中斷連線

檢查主機是否進入睡眠狀態、中斷網路連線，或應用程式是否已關閉。ChatGPT 執行工作時，請讓主機保持喚醒並維持連線。

### 設定因身分驗證而受阻

依照設定期間顯示的提示，完成帳戶或工作區的身分驗證。如果您的組織要求 SSO、多重要素驗證或通行金鑰，請完成該流程後再試一次。如果設定仍失敗，請要求工作區管理員確認已啟用遠端控制存取權。

## 另請參閱

- [ChatGPT 桌面版應用程式](/zh-Hant/codex/app)
- [功能](/zh-Hant/codex/features)
- [ChatGPT 桌面版應用程式設定](/codex/reference/settings)
- [電腦](/zh-Hant/codex/computer-use)
- [Chrome 擴充功能](/zh-Hant/codex/chrome-extension)
- [命令列選項](/codex/developer-commands?surface=cli)
- [身分驗證](/zh-Hant/codex/auth)
