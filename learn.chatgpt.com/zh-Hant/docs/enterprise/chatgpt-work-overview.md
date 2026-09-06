<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/chatgpt-work-overview -->

ChatGPT Work 與 Codex 共用核心的執行、隔離及權限機制，也都在您的 ChatGPT Business 或 Enterprise 合約所涵蓋的相同安全邊界內運作。兩者可用的功能與控制措施，取決於任務是在本機還是雲端執行、可用的工具，以及適用的工作區政策。

ChatGPT Work 可運用獲授權的工作區成員可使用的資訊、檔案、應用程式與工具，完成多步驟任務。在網頁版中，這些任務會在雲端執行，而非在該成員的裝置上執行。

本概覽說明網頁版 ChatGPT Work 的執行邊界、網路與應用程式控制措施、資料處理方式，以及任務如何安全執行。可用功能與管理控制措施取決於您的方案和工作區組態。

如需深入瞭解託管執行、已連線帳戶的權限、
瀏覽器與網路設定、資料保留，以及稽核資訊的可見範圍，請參閱
[ChatGPT Work 雲端安全性](/zh-Hant/codex/enterprise/chatgpt-work-cloud-security)。

如需瞭解裝置存取、本機瀏覽器工作階段、受管理的政策，
以及本機資料的處理方式，請參閱
[ChatGPT Work 本機安全性](/zh-Hant/codex/enterprise/chatgpt-work-local-security)。

## 執行隔離、檔案與裝置存取

ChatGPT Work 可使用哪些檔案與工具，取決於 Work 的執行位置、使用者權限和管理員設定。

### 本機 Work

本機 Work 透過使用者裝置上的 ChatGPT 桌面版應用程式執行任務。它可以存取開放給它的本機檔案、應用程式和其他資源，但仍受使用者權限、適用的工作區控制措施及裝置安全政策約束。與 Web 版 Work 不同，本機 Work 可操作留在您電腦上的資源，無須將檔案上傳至雲端對話。

### 雲端 Work

雲端 Work 可在支援的網頁版、行動版及桌面版介面上使用。它會在 OpenAI 管理的基礎架構上，於隔離環境中執行 Codex 任務執行框架。雲端對話可在這些介面之間同步，受支援的任務也能在使用者離開對話時繼續執行。

網頁版 Work 無法直接存取使用者電腦上的檔案、應用程式或已開啟的瀏覽器分頁。使用者可透過上傳檔案、將檔案加入支援的專案，或使用經授權的已連線應用程式來提供檔案。桌面版則透過自身的權限設定控管本機檔案和應用程式的存取。

當
[檔案庫](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)
可供使用時，符合條件的已上傳或已產生檔案都可儲存在其中。
管理員可控制 ChatGPT 是否自動引用
儲存在檔案庫中的檔案。停用自動引用並不會阻止使用者
主動存取或附加其獲授權使用的檔案。

請參閱[程式碼與 Shell 沙盒](/zh-Hant/codex/sandboxing?surface=web)、
[建立和編輯文件、試算表與簡報](https://help.openai.com/en/articles/20001278-creating-and-editing-documents-spreadsheets-and-presentations-with-chatgpt-work)，
以及
[ChatGPT 中的檔案儲存與檔案庫](https://help.openai.com/en/articles/20001052-library-for-chatgpt)。

## 網路存取與外部目的地

Work 會運用程式碼／Shell 執行工具和雲端瀏覽器等工具來完成任務。每項工具都能設定相應權限。

- **程式碼與 Shell 指令**：是否可存取公開網際網路，取決於適用的
  工作區政策和個人的 Work 網路設定。即使不允許存取公開網際網路，
  指令仍可連線至經 OpenAI 核准、
  維持 Work 運作所需的目的地。此設定控管的是網路目的地，
  而非哪些指令可以執行。
- **網頁搜尋**：搜尋功能有獨立的控制措施，與 Work 的程式碼及 Shell
  網路設定分開管理。

若提供個人的程式碼與 Shell 設定，該選項會顯示在
**設定** \> **資料控制** \> **Work 網路存取** 下。開啟「 **允許存取
公開網際網路** 」不會覆寫適用的管理員
限制。關閉此選項後，程式碼與 Shell 指令只能連線至
受管理的允許清單上列出的必要目的地；這不會停用已連線應用程式、
網頁搜尋或雲端瀏覽器。

程式碼與 Shell 網路設定的變更，要等到目前的執行作業結束，
且 Work 重新整理執行環境後才會生效。請參閱
[程式碼與 Shell 沙盒](/zh-Hant/codex/sandboxing?surface=web)及
[Work 存取控制](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)。

對外互動的控制措施與
[工作區 IP 存取限制](https://help.openai.com/en/articles/12111596-ip-allowlisting-for-chatgpt)各自獨立；
後者用來限制對 ChatGPT 工作區或 Compliance API 的傳入存取。

## 雲端瀏覽器與網站存取

ChatGPT Work 可使用的工具之一是
[雲端瀏覽器](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)；
這項工具不同於
[應用程式內瀏覽器](https://help.openai.com/en/articles/20001277-using-the-built-in-browser-in-the-chatgpt-desktop-app)。
它以遠端方式運作，使用獨立於使用者本機瀏覽器的
瀏覽器工作階段。它無法存取本機分頁、擴充功能、瀏覽紀錄、
已儲存的密碼或已通過驗證的本機工作階段。

雲端瀏覽器可瀏覽公開網站、在支援的公開表單中輸入資訊，並將已核准應用程式中的相關資訊用於網站任務。Enterprise 或 Edu 工作區無法透過雲端瀏覽器登入網站。瀏覽器的可用性取決於您的方案、地區、功能開放進度及工作區權限。對於 Enterprise 工作區，管理員除了啟用 Work 存取權，還必須另外啟用雲端瀏覽器存取權。

網站存取與操作各自設有控制措施：

- 預設情況下，ChatGPT 會在造訪新網站前先詢問。相關選項可用時，
  使用者可以選擇「 **一律詢問**」、「 **自動核准**」或「 **一律允許**」，並允許或
  封鎖個別網站。「 **自動核准** 」會執行自動化風險檢查。
「**一律允許** 」會取消網站存取的互動式審查。管理員
  同樣可限制使用者的核准設定（例如
  在整個工作區停用「 **一律允許** 」）。
- 允許造訪某個網站，不代表核准該網站上的所有操作。若操作可能產生財務、法律、帳戶方面或其他具有重大影響的承諾，ChatGPT 可在執行前另行要求確認。

使用者可在 Work 對話中查看可用的網頁截圖和瀏覽器操作重播。這些使用者可見的紀錄，並不代表可透過 Compliance API 匯出，也不構成管理員可檢視的完整執行歷程。

請參閱
[在 ChatGPT 中使用雲端瀏覽器](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)
及[瀏覽器](/zh-Hant/codex/browser?surface=web)。

## 已連線應用程式、憑證與權限

已連線應用程式或外掛程式只會透過工作區允許的整合，依據該連線獲授予的權限，讓 Work 進行存取。管理員可在管理儀表板中控制外掛程式和應用程式的可用性、工作區角色的存取權、外部授權、操作設定及來源系統權限。

在 Enterprise 和 Edu 工作區中，外掛程式及其所依賴的應用程式預設為關閉。在 Business 工作區中，外掛程式和應用程式則預設為開啟。讓外掛程式可供使用，不會自動啟用其所需的應用程式，也不會授予帳戶存取權。必須先為個人、共用或智慧體擁有的帳戶完成所需連線的授權，ChatGPT Work 才能進行存取。共用或智慧體擁有的連線會使用已連線帳戶在來源系統中的權限，這些權限可能與提出要求的使用者所擁有的權限不同。

在支援的情況下，管理員可將應用程式限制為只能執行唯讀操作或一組經核准的操作。應用程式權限設定也可決定 ChatGPT 在使用應用程式、進行變更或執行重要操作之前是否先詢問。各應用程式支援的操作控制措施不盡相同，也不是每項操作都需要由人員個別確認。

對於具同步功能的應用程式，來源內容或權限的變更可能需要一些時間才會反映出來。中斷應用程式連線不會自動移除已儲存在對話、產生的檔案，或有自身保留政策的紀錄中的資訊。

請參閱
[外掛程式和應用程式的管理控制措施、安全性與合規性](https://help.openai.com/en/articles/11509118-admin-controls-security-and-compliance-in-apps-enterprise-edu-and-business)、
[外掛程式控制措施](/zh-Hant/codex/enterprise/apps-and-connectors)、
[由管理員管理的 Google Workspace 設定](https://help.openai.com/en/articles/10929079-google-workspace-admin-managed-setup)，
以及[具同步功能的 ChatGPT 應用程式](https://help.openai.com/en/articles/10847137-chatgpt-apps-with-sync)。

## 隱私權與資料處理

ChatGPT Work 遵循適用於您 ChatGPT 工作區的隱私權、安全性及資料處理政策。對話、上傳的檔案、產生的檔案、已連線應用程式與瀏覽器資料，可能適用不同的保留和刪除規則。

詳情請參閱[企業隱私權](https://openai.com/enterprise-privacy/)、
[對話與檔案保留政策](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt)、
[資料駐留與推論駐留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)，
以及[ChatGPT Work 管理員常見問題](/zh-Hant/codex/enterprise/work-admin-faq)。

### 資料保留方式因資料類型而異

- **Work 對話：** 遵循適用的 ChatGPT 工作區對話
  保留與刪除設定。
- **儲存在檔案庫中的檔案：** 遵循適用的檔案與工作區
  保留規則。刪除對話不會刪除
  儲存在檔案庫中的檔案。
- **專案檔案：** 會保留在專案中，直到該專案刪除，並遵循
  適用的刪除規則與例外規定。
- **檔案庫以外的暫時上傳檔案：** 在 Enterprise 中，暫時上傳的檔案
  可能在 48 小時後過期，除非適用其他保留設定。
- **已儲存的記憶（若已啟用）：** 遵循獨立的記憶控制設定。
- **雲端瀏覽器 Cookie：** 與本機瀏覽器資料相互獨立。使用者可
  在雲端瀏覽器設定中將其清除。
- **合規紀錄平台的紀錄：** 可在平台中查閱 30 天。
  匯出的副本則遵循接收系統的保留政策。
- **已連線應用程式的資料：** 來源紀錄遵循已連線
  應用程式的政策。儲存在對話、檔案或同步索引中的副本，
  也須遵循適用的 OpenAI 儲存與保留規則。

刪除對話、結束 Work 任務、清除瀏覽器 Cookie 和保留合規紀錄，是不同的操作。刪除對話後，該對話將不再顯示，並會排定在 30 天內永久刪除，但仍適用已公布的安全性、法律及去識別化例外規定。

請參閱
[對話與檔案保留政策](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt)、
[ChatGPT 中的記憶](https://help.openai.com/en/articles/8590148-memory-in-chatgpt-faq)，
以及
[OpenAI 合規平台](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)。
