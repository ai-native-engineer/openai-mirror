<!-- source: https://learn.chatgpt.com/zh-Hant/docs/browser -->

Codex CLI 和 Codex IDE 擴充功能皆不提供瀏覽器。請開啟
ChatGPT 桌面版應用程式，以使用內建瀏覽器。

瀏覽器可讓 ChatGPT 開啟網站、蒐集最新資訊並執行操作，
而您始終保有控制權。您可以用它比較選項、在網站上完成多步驟任務，
或審查正在建立的頁面。

您可以在網頁版 ChatGPT 和 ChatGPT 桌面版應用程式中使用瀏覽器。

[GPT-6 Astra](/zh-Hant/codex/models#gpt-6-astra) 提升了視覺判斷能力，
適合用於對照螢幕擷取畫面檢查頁面，或完成跨網站工作流程等任務。
如果模型選擇器中提供此模型，請選用它，
並說明如何驗證完成結果。

在受管理的桌面環境中，管理員可以限制瀏覽器來源、
上傳、下載及開發人員存取權。請參閱
[受管理的瀏覽器控制項](/zh-Hant/codex/enterprise/managed-configuration#control-browser-and-computer-use)。

請將頁面內容視為不可信任的上下文。在分享敏感資訊或允許 ChatGPT 執行操作前，
請先審查網站及預定執行的操作。

ChatGPT 桌面版應用程式的內建瀏覽器，讓您與 ChatGPT 能在對話中共同查看
網站和本機網頁應用程式。您可以藉此預覽頁面、直接在畫面上提供意見回饋，
或讓 ChatGPT 代表您與網站互動。

內建瀏覽器使用獨立的瀏覽器設定檔，與您平常使用的瀏覽器分開。
它不會自動共用您現有的分頁或瀏覽器工作階段。
任務需要帳戶時，您可以直接登入。開啟 **設定 \>
瀏覽器** ，即可管理瀏覽器資料，
以及您裝置上可用的設定檔匯入功能。

瀏覽器下載的檔案預設會儲存至系統的「下載項目」資料夾。在 **設定 \>
瀏覽器**中，您可以選擇其他下載位置、重設為系統預設位置，
或開啟 **詢問下載檔案的儲存位置**。

當 ChatGPT 需要操作現有的 Chrome、Edge、Brave、Opera 或 Vivaldi 分頁，
或使用您平常的瀏覽器設定檔時，
請改用[瀏覽器擴充功能](/zh-Hant/codex/chrome-extension)。

您可以從工具列開啟內建瀏覽器，也可以按一下 URL、手動前往網頁，
或按下 <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>
（Windows 上為 <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>B</kbd>）。

  
    
  

## 從網址列搜尋

在內建瀏覽器的網址列輸入文字，即可從其瀏覽記錄中尋找頁面。
選取相符的頁面即可重新開啟；若瀏覽記錄沒有相符結果，
則可輸入搜尋字詞來搜尋 Google。

內建瀏覽器擁有獨立的設定檔和瀏覽記錄。搜尋結果不會
自動包含您平常使用的 Chrome 設定檔或其他瀏覽器中的頁面。

## 管理瀏覽記錄

開啟 **設定 \> 瀏覽器** ，即可搜尋內建瀏覽器的瀏覽記錄、重新開啟造訪過的頁面，
或在貴組織允許時移除瀏覽記錄項目。
使用**清除瀏覽資料** ，可選擇時間範圍，
以及要移除的瀏覽資料類型。

如果支援這項功能，ChatGPT 可要求搜尋您的瀏覽記錄，以找出
與目前任務相關的頁面。允許存取前，請先審查要求。
瀏覽記錄可能包含內部 URL、搜尋字詞及其他敏感資訊，
因此請只在任務需要這類上下文時允許存取。

<a id="browser-use"></a>

## 在瀏覽器中使用電腦功能

在桌面 App 中，電腦功能可讓 ChatGPT Work 或 Codex 直接操作內建瀏覽器。
您選用的服務可以開啟頁面、點按、輸入文字、
檢查頁面的呈現狀態、擷取螢幕畫面，
並在頁面中驗證執行成果。

瀏覽器隨附於桌面 App，並會自動安裝。
請 ChatGPT 或 Codex 在任務中使用內建瀏覽器，
或直接使用 `@Browser` 指定瀏覽器。

例如：

```text
Use the browser to open http://localhost:3000/settings, reproduce the layout
bug, and fix only the overflowing controls.

除非您已允許該網站，否則 ChatGPT 使用網站前會先詢問。
您可以在 **設定 \> 瀏覽器**中管理允許和封鎖的網站。
ChatGPT 也會在執行敏感操作前要求確認，例如提交資訊、
購買商品、變更權限或刪除資料。
ChatGPT 無法在內建瀏覽器中自動上傳檔案。

  頁面上的指示可能具有誤導性或惡意。授予網站權限只代表允許
ChatGPT 與該網站互動，不代表網站內容可信，
也不代表已核准所有操作。

## 預覽頁面

1. 在[整合式終端](/zh-Hant/codex/integrated-terminal)中，或透過[本機環境動作](/zh-Hant/codex/environments/local-environment#actions)，啟動應用程式的開發伺服器。
2. 按一下 URL，或在瀏覽器中手動前往，
即可開啟本機路由、以檔案為來源的頁面或公開頁面。
3. 對照程式碼差異，審查頁面的呈現狀態。
4. 在需要變更的元素或區域留下瀏覽器留言。
5. 請 ChatGPT 處理留言，並將處理範圍限縮。

例如：

```text
I left comments on the pricing page in the built-in browser. Address the mobile
layout issues and keep the card structure unchanged.

## 在頁面上留言

如果只有在呈現後的頁面中才能看出錯誤，請使用瀏覽器留言，
向 ChatGPT 提供精確的意見回饋。

1. 開啟 **註解模式**。
2. 按一下元素，或拖曳以選取區域。
3. 撰寫並儲存留言。
4. 在對話中傳送訊息，請 ChatGPT 處理留言。

留言清楚指出問題及期望結果時，效果最佳：

```text
This button overflows on mobile. Keep the label on one line if it fits,
otherwise wrap it without changing the card height.

```text
This tooltip covers the data point under the cursor. Reposition the tooltip so
it stays inside the chart bounds.

<section class="feature-grid">

<div>

### 樣式意見回饋

在頁面某個區段新增註解時，請選取文字輸入框旁的 **調整** ，
向 ChatGPT 提供更細緻的樣式意見回饋。
您可以修改字型、文字、間距和顏色等設定值，在頁面上預覽結果，
再傳送註解，讓 ChatGPT 更清楚您想要的效果。

</div>

  
    
  

</section>

## 限定瀏覽器任務的範圍

讓每項瀏覽器任務保持精簡，以便一次完成審查。

- 指明頁面、路由或 URL。
- 指明您關注的狀態，例如載入中、空白、錯誤或成功。
- 直接在需要變更的確切元素或區域留言。
- ChatGPT 完成後，再次審查頁面。
- 請 ChatGPT 在開啟本機頁面前，
先啟動或檢查開發伺服器。

如果涉及程式碼庫變更，請透過[審查窗格](/zh-Hant/codex/code-review?surface=app)
檢查變更並留言。

<section class="feature-grid">

<div>

## 開發人員模式

開發人員模式可搭配 Chrome 和內建瀏覽器中的電腦功能使用，
讓 ChatGPT 以受控方式存取 Chrome DevTools Protocol (CDP)。您可以藉此
分析 JavaScript 效能、檢查主控台輸出和網路流量、檢查 DOM
與已套用的樣式，或診斷執行中瀏覽器的問題。

若要啟用，請開啟[**設定 \> 瀏覽器**](codex://settings/browser-use)，
並在 **開發人員模式**下開啟 **啟用完整 CDP 存取權**。
如果貴組織已停用這項設定，您就無法在本機啟用。
管理員可在 [`requirements.toml`](/zh-Hant/codex/enterprise/managed-configuration#pin-feature-flags) 的 `[features]` 區段中
設定 `browser_use_full_cdp_access = false`，
以停用完整 CDP 存取權，並防止使用者在 ChatGPT 桌面版應用程式中
啟用對應設定。

完整 CDP 存取權可能暴露瀏覽器內部的敏感資訊。ChatGPT 使用
完整 CDP 檢查網站前，會要求您明確核准。核准前，請先審查
網站、任務和要求的存取權。

若要使用內建瀏覽器，請使用 `@Browser`。若要在 Chrome 中使用開發人員模式，
請先[設定 Chrome 擴充功能](/zh-Hant/codex/chrome-extension)，再叫用 `@Chrome`。

例如：

```text
This app is slow. Use @Browser to capture a performance trace and inspect
network traffic, then identify the bottleneck.

</div>

  
    
  

</section>

## 使用 ChatGPT Work 完成跨網站任務

ChatGPT Work 可以跨網站完成任務，包括需要登入的網站。

Work 使用自己的瀏覽器。這個瀏覽器在雲端的獨立電腦上執行，不是您手機或筆記型電腦上的瀏覽器。

在網頁版或行動版的 ChatGPT Work 中開始任務後，即使您離開並闔上電腦，ChatGPT 仍可繼續執行。Work 能使用自己的電腦，透過閱讀網頁、點擊和輸入文字，完成各式各樣的網路任務。它會根據您的要求，使用外掛程式、瀏覽器，或搭配使用兩者。

例如，ChatGPT 可以協助您：

- 查詢 DMV 的可預約時段並完成預約。
- 登入您的公用事業帳戶並比較方案。
- 尋找並儲存符合您條件的公寓房源。
- 在社群媒體上研究競爭對手。
- 在您的會計軟體中完成結帳。

您可以控制 ChatGPT 能存取哪些網站。ChatGPT 經過訓練，會在執行可能造成重大影響的操作（例如完成預約或付款）前要求您確認。如果 ChatGPT 因任何原因無法繼續，您可以透過行動裝置或桌面裝置接管它的電腦，親自操作。

Plus 和 Pro 方案的使用者可在網頁版和行動版使用 ChatGPT Work，瀏覽需要身分驗證的網站。

實際可用性取決於推出進度。企業或 Edu 工作區無法使用網站登入功能。

## ChatGPT Work 電腦的運作方式

當任務需要使用網站時，ChatGPT 會使用自己的瀏覽器瀏覽頁面、收集資訊，並在線上完成各個步驟。

預設情況下，ChatGPT 會在存取新網站前詢問您。您可以逐一核准要求，或調整設定，讓 ChatGPT 自動核准存取與任務相關的網站。ChatGPT Work 一律會在執行可能造成重大影響的操作（例如提交您的資訊以進行預約，或完成付款）前要求確認。

## 登入網站

如果網站需要登入，ChatGPT Work 會請您登入。完成身分驗證後，它會繼續在已登入的網站上執行任務。您的工作階段會保持有效，供後續任務使用，因此不必每次都重新登入。

### 使用安全登入表單

ChatGPT 無法看到您的使用者名稱或密碼；模型也絕不會看到這些資訊，這些資訊也絕不會用於模型訓練。ChatGPT 不會儲存您的使用者名稱或密碼。您隨時可以前往 **設定** \> **雲端瀏覽器** \> **瀏覽器資料**，刪除所有網站或個別網站的瀏覽記錄；這會將您登出相關網站。

當 ChatGPT 遇到登入畫面時，會暫停並視需要請您輸入登入憑證和雙因素驗證碼。在 iOS 上，您可以使用受支援的密碼管理工具順暢地登入。

請使用 ChatGPT 提供的登入表單，不要在對話中傳送密碼。

![iOS 上的 ChatGPT Work 暫停 DMV 任務，並顯示安全登入表單，內含網站網址和已遮蔽的密碼。](/images/codex/cloud-browser-auth/sign-in.webp)

### 在網頁上登入

如果有提供此選項，請選取 **改在網頁上登入** ，直接在雲端瀏覽器中登入。登入期間，任務會暫停。選取 **我已完成** 即可將控制權交還給 ChatGPT。您也可以略過或取消要求。

<a id="start-a-browser-task"></a>
<a id="start-browser-work"></a>
<a id="web-start-browser-work"></a>

## 如何在 ChatGPT Work 中開始任務

1. 開啟 ChatGPT 網頁版或行動版，並在 Work 中開始任務。
2. 說明您希望 ChatGPT 做什麼。
3. 若出現提示，請核准網站存取要求。
4. 如果網站要求登入，請直接登入。
5. 在對話中追蹤任務進度。
6. 審查結果，並核准任何可能造成重大影響的操作。

您不需要另外選取瀏覽器。ChatGPT 會根據您的要求決定何時使用瀏覽器。

有些網站會封鎖存取。如果遇到這種情況，ChatGPT 會告知您，並在可行時嘗試其他方式完成任務。

<a id="website-permissions-and-confirmations"></a>
<a id="web-website-permissions-and-confirmations"></a>

## 安全性與使用者控制項

在 ChatGPT 設定中開啟 **雲端瀏覽器** ，即可管理網站權限。可用選項包括：

- **一律詢問**：手動審查每個網站存取要求。
- **自動核准**：讓 ChatGPT 在檢查網站與您任務的相關性後，自動核准存取。
- **一律允許**：省略額外的審查步驟，直接允許存取網站。我們提供此選項是為了盡量簡化操作，但不建議使用。

![雲端瀏覽器設定，顯示「一律詢問」、「自動核准」和「一律允許」三個網站權限選項。](/images/codex/cloud-browser-auth/website-permissions.webp)

您也可以針對個別網站設定允許或封鎖，以覆寫預設權限。

在 ChatGPT 請您登入任何網站前，額外的審查模型會檢查登入要求及您即將輸入資訊的位置，確認是否有網路釣魚或欺騙的跡象。我們會針對提示注入、網路釣魚及非預期操作等風險測試智慧體。

為確保過程完全透明，您會看到網站網址及登入表單的預覽，也可以在繼續之前查看實際網站。透過安全登入表單輸入的憑證會直接傳送至瀏覽器，模型無法看到。

<a id="browser-data"></a>
<a id="web-browser-data"></a>

## 隱私權與瀏覽器資料

ChatGPT Work 的電腦與您裝置上的瀏覽器分開運作，並保有自己的 Cookie、瀏覽器資料和已登入的工作階段。ChatGPT 在完成任務時使用的資訊，會依照您選擇的 ChatGPT 資料控制設定處理。您可以在 ChatGPT 網頁版和行動版的 **設定** \> **資料控制**中檢視這些設定。

它不會使用您個人瀏覽器中已開啟的分頁、瀏覽記錄、已儲存的密碼、Cookie、擴充功能或現有的登入工作階段。

若要清除瀏覽器資料，請前往 **設定** \> **雲端瀏覽器** \> **瀏覽器資料** \> **全部清除**。這會將您登出 ChatGPT Work 瀏覽器中的網站，因此執行後續任務時需要重新登入。

![雲端瀏覽器設定，包含「瀏覽器資料」區段及「Cookie」控制項，可用來管理雲端瀏覽器儲存的 Cookie。](/images/codex/cloud-browser-auth/browser-data.webp)

## 限制

- 並非所有工作區或推出階段都提供網站登入功能。如果任務需要使用不受支援的登入方式，請自行完成該步驟，或使用其他可用工具。
- 有些網站會封鎖自動化瀏覽器，或要求完成 CAPTCHA。ChatGPT 可能無法在這些網站上完成任務。
- 能否使用雲端瀏覽功能，可能取決於您的方案、工作區設定及推出進度。除免費版和 Go 外，所有付費方案皆可在所有地區使用雲端瀏覽功能。企業管理員必須為其工作區啟用雲端瀏覽功能。

推出期間，即使您的方案支援瀏覽器，它也可能不會立即顯示。
