<!-- source: https://learn.chatgpt.com/zh-Hant/docs/plugins -->

## 概覽

外掛程式將各項功能整合成可在 ChatGPT 和 Codex 中重複使用的工作流程，其中可包含技能、連接器，或同時包含兩者。兩款產品共用同一個通用外掛程式目錄，因此您可以在兩者支援的介面上找到相同的公開外掛程式。

外掛程式可用於網頁版、桌面版和行動版 ChatGPT 的對話與 Work，也可用於 ChatGPT 桌面版應用程式中的 Codex。Codex CLI 也提供適用於 Codex 環境的外掛程式瀏覽器。IDE 擴充功能不支援外掛程式。

在行動裝置上，您可以在對話或 Work 中使用您帳戶可用的外掛程式。

開啟 **外掛程式** 分頁，即可瀏覽及安裝外掛程式。
安裝後，即可在 ChatGPT 的對話或 Work 中，或在 Codex 中使用外掛程式。
已安裝的外掛程式可為新對話加入技能、連接器和 MCP 工具。

開啟 **外掛程式** 分頁，即可瀏覽及安裝外掛程式。
安裝後，即可在對話或 Work 中使用外掛程式。外掛程式可能會提示您先連接外部服務，
完成連接後才能使用其工具。

在 Codex CLI 中輸入 `/plugins`，即可開啟外掛程式瀏覽器。
從已設定的市集安裝外掛程式後，請先啟動新的工作階段，
再使用其中隨附的技能或工具。

<a id="plugin-directory-in-the-ide-extension"></a>

### 在支援的介面上使用外掛程式

IDE 擴充功能無法使用外掛程式。若要瀏覽並安裝 Codex 的外掛程式，請使用 ChatGPT 桌面版應用程式或 Codex CLI。

擴充 ChatGPT 與 Codex 的功能，例如：

- 安裝 Codex Security 外掛程式，以掃描授權範圍內的程式碼，並確認疑似弱點的偵測結果。
- 安裝 Gmail 外掛程式，以使用 Gmail 處理工作。
- 安裝 Google Drive 外掛程式，以便跨 Drive、Docs、Sheets 和 Slides 處理工作。
- 安裝 Slack 外掛程式，以摘要頻道內容或草擬回覆。

外掛程式可包含下列一或多個部分：

- **技能：** 可重複使用的指示，適用於特定類型的工作。
  ChatGPT 和 Codex 可在需要時載入技能，依循正確步驟，
  並使用適合該任務的參考資料或輔助指令碼。
- **連接器：** 與 GitHub、Slack 或 Google Drive 等工具建立的連線，
  讓 ChatGPT 和 Codex 能讀取這些工具中的資訊，並在其中執行操作。
  連接器會提供工具，也可選擇加入自訂 UI。
- **MCP 伺服器：** 讓 ChatGPT 和 Codex 存取更多工具或共用資訊的服務，
  通常來自本機專案以外的系統。它們也是連接器背後的服務，
  負責定義工具、強制執行身分驗證、傳回結構化資料，
  並對外部系統執行操作。
- **瀏覽器擴充功能：** 提供外掛程式在執行工作流程時
  所需的瀏覽器功能。
- **掛勾：** 在生命週期中設定的時點執行的指令。
  啟用外掛程式掛勾前，請先審查並確認其值得信任。
- **排程任務範本：** 在支援排程任務的環境中，
  作為建立定期任務的起點，並可重複使用。

您可以透過市集來源發布外掛程式，與他人分享，
例如使用專案或團隊的程式碼庫市集。請參閱[建置外掛程式](https://developers.openai.com/plugins/build/plugins)，
了解市集設定、封裝和散布方式。

若您要開發整合功能，請先參閱
[建置 MCP 伺服器](https://developers.openai.com/plugins/build/mcp-server)。
若外掛程式需要自訂 UI，請參閱
[選用 UI 指南](https://developers.openai.com/plugins/build/chatgpt-ui)。

## 使用及安裝外掛程式

<a id="plugin-directory-in-the-codex-app"></a>

### 通用外掛程式目錄

ChatGPT 和 Codex 使用相同的公開外掛程式目錄。
在網頁版 ChatGPT 或 ChatGPT 桌面版應用程式中，開啟 **外掛程式** 分頁即可瀏覽及安裝外掛程式。

  
    
  

外掛程式目錄將外掛程式分成下列分頁：

- **OpenAI：** 由 OpenAI 建置的外掛程式。
- **您的工作區名稱：** 由您的工作區提供的外掛程式。
- **個人：** 個人市集中的外掛程式；若有相關外掛程式，則會顯示 **由我建立** 和
**與我分享** 區段。

使用獨立的 **已安裝** 列，檢視您已安裝的外掛程式。

工作區管理員可以為團隊匯入並同步 GitHub 市集。
請參閱[外掛程式管理](/zh-Hant/codex/enterprise/plugin-management)，
了解設定與存取要求。

### 安裝及使用外掛程式

開啟外掛程式目錄後：

1. 搜尋或瀏覽外掛程式，然後開啟其詳細資料。
2. 選取加號按鈕以安裝外掛程式。
3. 如果外掛程式需要連接器，請依提示進行連接。有些外掛程式會在安裝期間要求您完成身分驗證，另一些則會在首次使用時才提出要求。
4. 安裝完成後，開始新對話，並要求 ChatGPT 或 Codex 使用此外掛程式。

### 透過「使用 ChatGPT 登入」連接支援的合作夥伴服務

**使用 ChatGPT 登入** 功能正以測試版形式逐步推出，適用於支援的外掛程式和
合作夥伴網站，包括 Airtable、GitLab、HubSpot、Notion、Supabase 和 Vercel。
如果有此選項，請在連接外掛程式時選取 **使用 ChatGPT 登入** ，
即可在該服務建立帳戶，或連結現有帳戶。

登入時只會將您的姓名、電子郵件地址和個人資料相片（如有）分享給合作夥伴。這不會授予外掛程式存取您資料的權限，也不會自動核准操作。使用連線前，請另行審查並核准外掛程式要求的權限。

安裝外掛程式後，即可直接在提示詞輸入框中使用：

  
    
  

<div class="not-prose mt-4 grid gap-4 md:grid-cols-2">
  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">直接描述任務</p>
    <p class="mt-2 text-sm text-secondary">
      說明您想要的結果，例如「摘要 Gmail 中今天的未讀討論串」或「從 Google Drive 擷取最新的發布說明」。
    </p>
    <p class="mt-3 text-sm text-secondary">
      若希望 ChatGPT 為任務挑選合適的已安裝工具，請使用這種方式。
    </p>
  </div>

  <div class="rounded-xl border border-subtle bg-surface px-5 py-4">
    <p class="text-sm font-semibold text-default">選擇特定外掛程式</p>
    <p class="mt-2 text-sm text-secondary">
      輸入 <code>@</code>，即可明確叫用此外掛程式，
      或其隨附的某項技能。
    </p>
    <p class="mt-3 text-sm text-secondary">
      若想指定 ChatGPT 應使用哪個外掛程式或技能，請使用這種方式。
      請參閱<a href="/codex/skills-and-plugins">技能與外掛程式</a>。
    </p>
  </div>
</div>

### 在 Codex 中使用 Apple Messages

macOS 的 ChatGPT 桌面版應用程式在所有方案中都提供 Apple Messages 外掛程式。在 Codex 和 ChatGPT Work 中，此外掛程式可讀取及搜尋您 Mac 上的 iMessage、SMS 和 RCS 對話，並透過 Messages 應用程式代您傳送訊息。它無法讓您透過 Messages 與 ChatGPT 遠端互動，也無法在一般 ChatGPT 對話中使用。

本次發行的 Messages 外掛程式僅包含在 ChatGPT 桌面版應用程式的 Apple Silicon (arm64) 建置版本中。

1. 開啟 **外掛程式**，找到 Apple Messages 外掛程式並安裝。
2. 開始新的 Codex 或 ChatGPT Work 對話，並要求其尋找、摘要、草擬或傳送訊息。
3. 在 ChatGPT 讀取 Messages 前，請授予所要求的 macOS 權限。
4. 允許傳送前，請先審查訊息內容及收件人。

預設情況下，ChatGPT 只有在您核准訊息內容及收件人後才會傳送訊息。
選取 **允許一次** ，即可只核准這次傳送。若選取
**一律允許傳送至此對話**，ChatGPT 之後就能傳送訊息至該 Messages 對話，
無須再次取得傳送核准。

對於可能含有不可信或誤導性指示的對話，請保留每次傳送前的核准要求。持續核准會讓您失去在 ChatGPT 以您的名義傳送訊息前，最後一次審查訊息的機會。只有在您接受這項風險時，才應使用持續核准。

若要恢復每次傳送前的核准要求，請開啟 **設定** \> **電腦** ，並選取
 **Messages** 旁的**管理** 。在 **一律允許傳送**區段中，
選取該對話旁的垃圾桶圖示，然後確認 **移除**。
ChatGPT 之後再次傳送訊息至該對話前，會先要求核准。

**已知問題：** 如果您的任務設為 **完整存取權** ，或因其他設定而停用
核准提示，Apple Messages 可能無法顯示傳送訊息所需的
確認提示。請切換為 **要求核准** 或 **代我核准** ，然後再試一次。

Apple Messages 在您的 Mac 上執行，無法直接在網頁版或行動版 ChatGPT、
Codex CLI 或 IDE 擴充功能中使用。

在受管理的工作區中，管理員可以透過現有的「電腦」控制項
停用 Apple Messages。

<a id="plugin-directory-in-codex-cli"></a>

### Codex CLI 中的外掛程式瀏覽器

在 Codex CLI 中，執行下列指令以開啟外掛程式瀏覽器：

```text
codex
/plugins

  
    
  

CLI 外掛程式瀏覽器會依市集將外掛程式分組。使用市集分頁
切換來源、開啟外掛程式以查看詳細資訊，以及安裝或解除安裝
市集項目；選取已安裝的外掛程式並按下 <kbd>Space</kbd>，即可
啟用或停用。

<a id="api-key-availability"></a>

### API 金鑰適用情況

如果您[使用 OpenAI API 金鑰
登入 Codex](/zh-Hant/codex/auth#sign-in-with-an-api-key)，即可在 Codex CLI 與 ChatGPT 桌面應用程式中的 Codex
瀏覽、安裝及管理受支援的 OpenAI 精選外掛程式。
部分外掛程式無法搭配 API 金鑰身分驗證使用，因為其
連線流程需要不受支援的 OAuth 功能。請至
[平台用量頁面](https://platform.openai.com/usage)檢視外掛程式的使用情形。

### 權限與資料分享的運作方式

在網頁版 ChatGPT 中，對話與 Work 會使用該對話可用的工作區權限與工具。
連接器仍須各自登入並取得存取權。

當外掛程式功能透過 Codex 主機執行時，適用該主機的[沙盒與
核准政策](/zh-Hant/codex/agent-approvals-security)。
連線至外部服務時，則使用該服務本身的身分驗證與
存取控制。

- 安裝後，開始新對話或 CLI 工作階段，
即可使用隨附的技能。
- 如果外掛程式包含連接器，您目前使用的產品可能會在設定期間
或首次使用時，提示您安裝或登入這些連接器。
- 如果外掛程式包含 MCP 伺服器，您可能需要先完成額外設定
或身分驗證，才能使用這些伺服器。
- 當 ChatGPT 透過隨附的連接器傳送資料時，
即適用該服務的條款與隱私權政策。

### 移除外掛程式

若要移除外掛程式，請從支援的外掛程式瀏覽器開啟該外掛程式，並在提供此操作時選取
**解除安裝外掛程式** 。由工作區安裝或
預設提供的外掛程式可能沒有此操作選項，
而是由您的工作區管理員管理。

解除安裝外掛程式會從該 ChatGPT 或 Codex 環境中移除外掛程式套件，
但隨附的連接器仍會保持連線，直到您在 ChatGPT 中
管理這些連接器為止。

## 建置自己的外掛程式

如果您想建立、測試或散布自己的外掛程式，請參閱
[建置外掛程式](https://developers.openai.com/plugins/build/plugins)。該頁面涵蓋在本機建立專案骨架、
手動設定市集、工作區分享、外掛程式資訊清單，
以及封裝指南。

如果您的外掛程式包含由伺服器支援的功能，請參閱
[建置 MCP 伺服器](https://developers.openai.com/plugins/build/mcp-server)。
MCP 工具可在沒有自訂 UI 的情況下運作；當視覺介面有助於
工作流程時，也可以傳回 UI。

當您的外掛程式準備好接受審查時，請參閱
[提交外掛程式](https://developers.openai.com/plugins/deploy/submission)，瞭解 OpenAI 平台的提交流程、
所需權限、審查資料、MCP 檢查，
以及測試案例要求。

## 外掛程式指南

- [錄製與重播](/zh-Hant/codex/extend/record-and-replay)：向 ChatGPT 示範一次工作流程，
  即可將其轉換為可重複使用的技能。
- [Codex Security 外掛程式](/zh-Hant/codex/security/plugin)：掃描經授權的程式碼，
  確認發現的問題，並準備經審查的修正內容。
