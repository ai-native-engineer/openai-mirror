<!-- source: https://learn.chatgpt.com/zh-Hant/docs/whats-new -->

這份每週摘要介紹可能改變您工作方式的 ChatGPT 與 Codex 功能，
並提供範例和延伸閱讀連結。如需查看所有版本更新、錯誤修正
及小幅改進，請參閱 [Codex 更新日誌](/codex/changelog)。

## 2026 年 8 月 31 日至 9 月 4 日

### 使用 GPT-6 Astra 處理高難度工作

[GPT-6 Astra](/zh-Hant/codex/models#gpt-6-astra) 結合進階推理、電腦操作
與更強的判斷力，可在 Codex 和 ChatGPT Work 中處理
涉及程式碼、應用程式與研究的複雜工作。您可以用它執行工作流程、檢查結果，
並產出符合您範本與任務需求的文件、
試算表或簡報。

您的帳戶獲得 Astra 存取權後，即可從模型選擇器中選取。
開始大型任務前，請先查看[用量與定價](/zh-Hant/codex/pricing)。
Enterprise 使用者必須符合本次開放資格，
且由管理員啟用後，才能存取。

## 2026 年 8 月 24–28 日

### 在更多網站上完成工作

- **使用您的瀏覽器：** 除了 Chrome，現在也能透過 ChatGPT 桌面版應用程式使用 [Edge、Brave、Opera 或 Vivaldi](/zh-Hant/codex/chrome-extension)。
  將已開啟的分頁帶入 ChatGPT Work 或 Codex 對話，
  即可在已登入的網站上工作。
  Opera 支援瀏覽器控制，但不提供側邊對話。

- **使用網站提供的工具：** 透過[網站工具（WebMCP）](/zh-Hant/codex/webmcp)，ChatGPT Work 與 Codex
  可以在桌面版應用程式的內建瀏覽器中，使用網站提供的操作。
  例如，文件編輯器可以提供尋找章節
  或新增留言的工具。請更新桌面版應用程式，並使用 GPT-5.6 Sol 或
  GPT-5.6 Terra。網站工具不支援 GPT-5.6 Luna，
  也不適用於 Enterprise 或 Edu 工作區。

- **透過雲端瀏覽器登入：** 符合資格的方案使用者可在網頁版、iOS 或 Android 的 ChatGPT Work 中，
  繼續處理需要網站帳戶的任務。
  請依照[登入要求](/zh-Hant/codex/browser?surface=web#web-sign-in-to-a-website)
  操作，並在登入流程中輸入您的資料，請勿在對話中輸入。
  這不會連接您的本機瀏覽器設定檔。網站登入功能不適用於
  Enterprise 或 Edu 工作區。

開放情況取決於推出進度和工作區設定。

[閱讀 8 月 25 日瀏覽器的
版本資訊](/codex/changelog#codex-2026-08-25-browser)。

### 透過應用程式事件觸發排程任務

[排程任務](/zh-Hant/codex/automations?surface=web#web-trigger-tasks-from-app-events)現在可以在 Gmail、Slack 或 GitHub
發生支援的事件時啟動。利用事件觸發條件，
即可分類處理新郵件、彙整頻道動態，或依據 Pull Request 的回饋採取行動，
無須按固定頻率輪詢。

符合資格的方案可在網頁版和行動版 ChatGPT 中使用事件觸發的任務。
請先連接相關應用程式，並核准其要求的存取權。在受管理的
工作區中，管理員可以控管存取權。

<PromptComponent
  prompt={`當我在 <owner>/<repository> 中的任一 Pull Request 收到新的審查回饋時，彙整回饋並擬定修改計畫。`}
/>

[閱讀 8 月 25 日的
版本資訊](/codex/changelog#codex-2026-08-25-event-triggers)。

## 2026 年 8 月 17–21 日

### 使用更多應用程式與內容完成工作

- **Apple Messages：** [找出對話、彙整訊息、擬定回覆，並透過 Mac 上的 Messages 傳送訊息](/zh-Hant/codex/plugins?surface=app#app-use-apple-messages-from-codex)。此外掛程式在 macOS 上的 ChatGPT 桌面版應用程式中適用於所有方案。請在 ChatGPT Work 和 Codex 中使用；一般 ChatGPT 對話無法使用。預設情況下，ChatGPT 只會在您核准訊息內容及收件人後傳送。

- **共同編輯 Site：** 如已開放，您可以[邀請工作區的活躍成員擔任編輯者](/zh-Hant/codex/sites#collaborate-on-a-site)。Site 擁有者首次發布後，編輯者即可改善 Site 並發布更新。受邀的編輯者可以讀取 Site 線上資料庫中的資料；分享與設定的控制權仍由擁有者保留。

- **可編輯的 Site 網址：** 如已開放，您可以[為現有 Site 選擇由 ChatGPT 託管的新網址](/zh-Hant/codex/sites#change-a-site-url)，無須重新部署。原網址會重新導向至新網址。

- **歐洲的電腦使用紀錄：** 您可以在 EEA、瑞士與英國使用[電腦使用紀錄](/zh-Hant/codex/customization/computer-history)。對於使用 macOS 的 ChatGPT Pro、Business 和 Enterprise 使用者，此功能仍預設為關閉。Business 和 Enterprise 管理員必須先啟用存取權。

- **分享討論串快照：** 透過 macOS 上的 ChatGPT 桌面版應用程式[分享本機 Codex 討論串的唯讀快照](/zh-Hant/codex/use-chatgpt#share-a-read-only-snapshot-of-a-codex-thread)。以個人帳戶建立的連結，任何持有連結的人都能查看；以工作區帳戶建立的連結則僅限原工作區成員查看。Codex 會遮蔽符合已知機密資訊模式的內容，但快照中仍可能保留敏感內容，因此請在分享前先行審查。

- **統一同步已釘選的討論串：** 讓您的[已釘選對話](/zh-Hant/codex/projects?surface=app#app-organize-projects-and-chats)在桌面版與 iOS 之間保持同步。

[閱讀 8 月 20 日的版本資訊](/codex/changelog#codex-2026-08-20-app)。

### 在 Codex 雲端處理 GitLab 專案

[GitLab 支援](/zh-Hant/codex/third-party/gitlab)現已針對所有 ChatGPT 方案推出測試版。
您可以連接專案、建立雲端環境，
在議題或合併請求中透過 `@codex` 啟動任務，
並要求對合併請求進行單次或自動審查。

這項整合在 Codex 雲端執行，受管理工作區的管理員可以將其停用。
由 GitLab 觸發的活動需要設定相關 webhook 的權限。
GitLab Self-Managed 和 GitLab Dedicated 連線須由工作區管理員設定；
webhook 活動須使用 GitLab 19.0 或更新版本。

[閱讀 8 月 19 日 GitLab 的
版本資訊](/codex/changelog#codex-2026-08-19-gitlab)。

### 匯出公開外掛程式的中繼資料以供審查

符合資格的 ChatGPT Enterprise 工作區擁有者和管理員可以下載
列出工作區可見公開外掛程式的 CSV 檔案。在
[管理員 \> 外掛程式](https://chatgpt.com/admin/plugins)中選取 **公開**，然後
選取下載圖示（**匯出 CSV**）。

匯出內容會列出外掛程式、應用程式及對話技能的名稱與說明，以及
開發者、版本、新增日期（UTC）和 OpenAI 驗證中繼資料。
此匯出功能使用公開目錄快照，快照資料最多可能是 48 小時前的內容，且不包含
專為該工作區建立的外掛程式。
FedRAMP 工作區無法使用此匯出功能。

[閱讀 8 月 17 日管理員匯出功能的
版本資訊](/codex/changelog#codex-2026-08-17-admin-csv)。

## 2026 年 8 月 10–14 日

### 透過電腦使用紀錄尋找先前的工作內容

[電腦使用紀錄](/zh-Hant/codex/customization/computer-history)會將您在應用程式與網站上的活動
整理成可搜尋的時間軸與記憶，供 ChatGPT 和 Codex 使用。
只有在您願意分享這些上下文時才開啟此功能，接著即可
選擇要納入紀錄的應用程式與網站、暫停收集，並隨時
檢視或刪除使用紀錄。

ChatGPT Pro、Business 和 Enterprise 客戶可在 macOS 上的
ChatGPT 桌面版應用程式中使用電腦使用紀錄。Business 和 Enterprise
管理員必須先啟用存取權。初期開放地區不包括
歐盟、瑞士與英國。

### 在 Linux 上使用 ChatGPT 桌面版應用程式

[適用於 Linux 的 ChatGPT 桌面版應用程式](/zh-Hant/codex/linux/linux-app)現已推出預覽版。
您可以在受支援的 Ubuntu 或 Debian 發行版上安裝 `.deb` 套件，
或在 Fedora 上安裝 `.rpm` 套件。
提供適用於 x64 和 ARM64 處理器的套件。

使用 ChatGPT 帳戶登入，即可處理專案和本機檔案，並使用
Codex。部分功能（包括「電腦」）尚未在
Linux 預覽版中開放。

### 沿用既有的智慧體設定與工作內容

您可以從 **Claude Code**、<strong>Claude Cowork</strong> 或
**Cursor** 將[指示、設定、技能、外掛程式、專案及近期
工作內容匯入](/codex/import) ChatGPT 桌面版應用程式。在
**設定 \> 匯入** 中開啟自動更新，讓匯入的工作內容保持同步。

在 Codex CLI 中，使用 `/import` 將 Claude Code 或 Cursor 中支援的設定與近期對話
匯入本機工作階段。

[閱讀 8 月 11 日桌面版與 CLI 的
版本資訊](/codex/changelog#codex-2026-08-11-app)。

### 為資安防禦工作選擇合適的存取權

Daybreak 現在為經核准的防禦人員提供兩個層級。 **Daybreak Blue** 支援
一般防禦工作，例如程式碼安全性審查、事件應變及
修補程式驗證。 **Daybreak Red** 須另行取得核准，並提供
專為此用途訓練的模型存取權，以執行已獲授權的安全性評估。

存取須具備 [Trusted Access for
Cyber](/zh-Hant/codex/cyber-safety#trusted-access-for-cyber) 資格，且僅適用於
經核准的身分、工作區或組織、模型及產品介面。

[閱讀 8 月 10 日 Daybreak 的
公告](/codex/changelog#codex-2026-08-10-daybreak)。

## 2026 年 8 月 3–7 日

### 透過 ChatGPT 語音討論檔案和專案

[ChatGPT 語音](/zh-Hant/codex/features/voice)現已支援上傳的檔案和
[ChatGPT 專案](/zh-Hant/codex/projects)。你可以在語音對話中
詢問文件內容，或利用專案最近的對話、來源及
指示，繼續推進專案。

### 使用教育專用外掛程式學習與教學

三款新的[外掛程式](/zh-Hant/codex/plugins)將課堂專用工作流程帶入
ChatGPT Work 和 Codex。 **大學生** 可建立學習指南、
練習測驗、學習卡及互動式說明。 **大學教育工作者** 協助
制定課程計畫、教材與評量。 **K–12 教育工作者** 支援
教案規劃、課堂資源，以及針對不同學習者
調整的教材。

這些外掛程式可透過 ChatGPT Edu，以及學區部署的 ChatGPT for Teachers
使用。可用的工具與權限由學校控管。請閱讀
[教育外掛程式
公告](https://openai.com/index/learn-teach-chatgpt-work-codex/)。

### 重複使用已儲存的檔案，更快找到過去的工作

在網頁版，你可以將檔案庫中已儲存的檔案加入對話，無須重新上傳，
也可以搜尋檔案庫，或貼上格式化文字並保留標題、
連結與清單。網頁版、iOS 和 Android 上的搜尋也能比對資料夾
與對話標題。

現在，所有 ChatGPT 方案（包括 Enterprise 和 Edu）
都會將超過 10,000 個字元的貼上內容轉為附件。若想將內容移回訊息，
可選取 **在文字欄位中顯示** 。

閱讀 [ChatGPT
版本資訊](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)。

### 查看 ChatGPT Work 的剩餘用量

符合資格的個人方案和 ChatGPT Business 使用者，可以直接在網頁版側邊欄查看
ChatGPT Work 的剩餘用量。可用的點數選項取決於
你的帳戶與工作區權限。ChatGPT Work 和 Codex 仍然
共用相同的[使用上限與點數](/zh-Hant/codex/pricing)。

### 選擇 GPT-5.6 在 ChatGPT 中的回覆方式

透過新增的滑桿，ChatGPT Plus 和 Pro 使用者可以調整 GPT-5.6 Sol
回覆時投入的思考程度。更新後的模型也會提供更可靠的事實資訊，
回答更切題。GPT-5.6 Luna 成為免費版與 Go 方案的
ChatGPT 預設模型。

這些變更適用於 ChatGPT 對話，不會改變模型
在 ChatGPT Work 或 Codex 中的行為。請閱讀 [ChatGPT
版本資訊](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)。

### 在 Codex CLI 0.147.0 中整理工作並切換智慧體

[Codex CLI 0.147.0](https://github.com/openai/codex/releases/tag/rust-v0.147.0)
新增可持續保留、手動排序的對話區段，以及可攜式智慧體外掛程式。
你可以搜尋本機、個人、工作區與遠端外掛程式目錄，或
[匯入 Cursor 和 Claude Code 設定](/zh-Hant/codex/import)，而不會重複建立
已同步的對話。

使用 `--approve-for-me` 可針對符合條件的要求啟用[核准要求
自動審查](/zh-Hant/codex/sandboxing/auto-review)，且不會擴大
檔案系統或網路權限。Amazon Bedrock 工作階段也新增支援具快取功能的
網頁搜尋，以及遠端對話壓縮。

### 追蹤並接續更深入的安全性掃描

託管式 Codex Security 外掛程式的 `0.1.16` 至 `0.1.18` 版本新增即時掃描
進度、實測 Token 用量、可接續的深度掃描，以及可設定的
探索上限。最新版本也支援透過 Amazon Bedrock
進行身分驗證，供程式碼庫掃描及其委派的工作程序使用。

使用 [Codex Security 工作台](/zh-Hant/codex/security/plugin/workbench)查看
掃描進度與發現項目；若需要更全面的評估，也可[設定深度
掃描](/zh-Hant/codex/security/plugin/deep-scans)。
查看[外掛程式更新日誌](/zh-Hant/codex/security/plugin/changelog)，以
確認你安裝的版本支援哪些功能。

### 審查 GitHub Pull Request 的安全性風險

[Codex Security 審查](/zh-Hant/codex/security/security-review)會結合程式碼庫上下文、威脅模型與安全性指引，
分析 Pull Request 的變更。
你可以設定在 Pull Request 建立或收到新提交時自動執行
審查，也可以直接使用 `@codex security review` 提出審查要求。

此功能以研究預覽版形式提供給符合資格的 ChatGPT Enterprise、
Business、Edu 和 Pro 客戶。Plus 不提供此功能，且可能設有
使用上限。

## 2026 年 7 月 27–31 日

### 以更低費率使用 GPT-5.6 Terra 和 Luna

GPT-5.6 Terra 現已降價 20%，GPT-5.6 Luna 則降價 80%。輸入、
快取輸入與輸出費率均按相同比例降低。更新後的
[使用上限與費率](/zh-Hant/codex/pricing)讓 Terra 更適合日常
工作，而 Luna 則特別適合範圍明確的程式碼編寫與大量任務。

### 從瀏覽器和開啟的分頁中尋找實用的上下文

在 ChatGPT 桌面版應用程式中，[內建瀏覽器](/zh-Hant/codex/browser)可以從瀏覽紀錄中尋找
網頁，也能直接從網址列搜尋 Google。
當任務需要先前的上下文時，ChatGPT 也可以
搜尋你的瀏覽紀錄。

[Chrome 擴充功能](/zh-Hant/codex/chrome-extension)讓你可以提及已開啟的分頁、
將網頁上選取的文字帶入側邊對話、針對 YouTube 影片提問，
或從網頁的快顯選單中選取 **詢問 ChatGPT** 。請先審查並核准
使用瀏覽紀錄的要求，ChatGPT 才會將這些資訊納入
任務。

### 跨程式碼庫審查變更

當[本機專案包含多個
資料夾](/zh-Hant/codex/projects#use-local-projects-for-folders-and-codebases)時，
桌面版應用程式會顯示每個程式碼庫及其變更行數。選取
**審查** ，即可一併檢視差異，無須在不同的
審查檢視間切換。

### 在對話中微調生成的圖像

在展開的檢視器中開啟生成的圖像，然後在
**焦點檢視** 與 **畫布檢視**之間切換。你可以在多張圖像上新增註解，選擇
要保留的版本，並要求針對特定部分編輯，全程無須離開對話。
進一步瞭解[圖像生成](/zh-Hant/codex/image-generation)。

### 找出需要你關注的對話

桌面版應用程式新增的 **活動檢視** 會集中顯示你最近
參與的對話，以及需要你關注的工作。選取側邊欄的鈴鐺圖示，
即可開啟這個檢視。

[閱讀 7 月 30 日桌面版應用程式的
版本資訊](/codex/changelog#codex-2026-07-30-app)。

### 透過「使用 ChatGPT 登入」連接合作夥伴的工具

**使用 ChatGPT 登入** 正以測試版形式陸續在支援的外掛程式和
合作夥伴網站推出，首波包括 Airtable、GitLab、HubSpot、Notion、Supabase 和
 Vercel。你可以用更少的步驟建立或連結合作夥伴帳戶，接著在 ChatGPT 或 Codex 中
開始使用該服務。

合作夥伴只會收到你的姓名、電子郵件地址，
以及個人資料相片（若有）。每個外掛程式要求的存取權仍須個別審查
與核准。請閱讀[7 月 29 日的登入功能
公告](/codex/changelog#codex-2026-07-29)。

### 在學術研究專用工作區中協作

[ChatGPT for Academic Researchers](https://openai.com/index/chatgpt-for-academic-researchers/)
為符合資格的大專院校教師及博士後研究人員提供 12 個月的免費
ChatGPT 專用工作區使用權。獲核准的團隊最多可包含五名
來自同一機構且通過驗證的研究人員，並享有商務資料保護
及 ChatGPT Pro 等級的使用量上限。參與者可使用 GPT-5.6，
在 ChatGPT、ChatGPT Work 和 Codex 中進行研究與程式碼編寫工作流程。

此計畫提供 ChatGPT 使用權，不包含 OpenAI API 點數。申請者須
[通過機構驗證，並具備符合條件的研究
論文](https://help.openai.com/en/articles/20001406)。

### 在 iOS 上更穩定地接續 Codex 任務

ChatGPT iOS 版 1.2026.202 能在你返回應用程式或使用 Face ID 解鎖裝置時，更穩定地
重新連線至任務。語音對話會使用你選擇的 ChatGPT 聲音，並顯示使用量上限警告。
撰寫工具現在也會推薦已安裝的外掛程式及其技能，
行為與桌面版應用程式一致。

此版本也改善了目標的暫停與繼續控制項、行內表格
與視覺主題、工作區中的大量差異、所選文字的引用，以及模型
還原功能。請閱讀[7 月 27 日 iOS 的
版本資訊](/codex/changelog#codex-2026-07-27-mobile)。

### 比較安全掃描並管理發現的問題

託管版 Codex Security 外掛程式 `0.1.14` 和 `0.1.15` 新增掃描比較、
誤報回饋、有明確適用範圍的 `SECURITY.md` 政策，以及更清楚的程式碼庫
與各項問題的歷史紀錄。你可以選擇發現的問題，在 Linear 或 GitHub 議題中追蹤，
Codex 會先審查提議的動作，再由你核准。

使用現有的 [Codex Security
工作台](/zh-Hant/codex/security/plugin/workbench)，在桌面版應用程式中審查已儲存的掃描、發現的問題、
程式碼庫歷史紀錄與修復情況。託管外掛程式目錄
提供 `0.1.15` 版，而公開的 CLI 外掛程式市集
提供 `0.1.11` 版。採用新功能前，請先查看 [Codex Security 外掛程式的
更新日誌](/zh-Hant/codex/security/plugin/changelog)。

### 從終端、CI 或 TypeScript 執行安全掃描

公開的 `@openai/codex-security` CLI 和 TypeScript SDK 已更新至
`0.1.5` 版，版本編號與 Codex Security 外掛程式分開。你可以使用這個
套件[從 CLI 執行掃描](/zh-Hant/codex/security/cli)，審查 Pull Request 的
變更並在 [CI](/zh-Hant/codex/security/cli/ci) 中上傳 SARIF 結果，或執行
可接續的[批次掃描](/zh-Hant/codex/security/cli/bulk-scans)，掃描範圍可涵蓋 GitHub
程式碼庫或固定 CSV 清單中的項目。

透過 [Codex Security TypeScript SDK](/zh-Hant/codex/security/sdk)，你也能在自己的工具中加入
掃描、進度回報、成本控制及取消功能。
這個套件雖然公開提供，但執行掃描仍需具備 Codex Security
存取權。部分完整程式碼庫掃描還需要 Trusted Access for Cyber。

### 整理工作階段並擴充 Codex CLI 0.146.0

在 [Codex CLI 0.146.0](https://github.com/openai/codex/releases/tag/rust-v0.146.0) 中，
你可以使用 `/new release prep` 或 `/clear bug bash` 為新對話命名、釘選
重要討論串，以及在側邊對話之間切換而不必關閉它們。
此版本也新增暫時的對話分支、供相容自訂模型供應商使用的
獨立網頁搜尋、由執行器提供的技能，並支援智慧體外掛程式
資訊清單、工作區外掛程式發布及其他外掛程式市集。

對自訂用戶端而言，[App Server](/zh-Hant/codex/app-server) 可篩選已釘選的
討論串、在記憶體中建立分支、檢查已安裝連接器的狀態，以及讀取
連接器中繼資料。實驗性的 WebSocket 支援也能將 app-server 連線至
遠端 Code Mode 主機。開放遠端連線前，請先查看
[app-server 安全性要求](/zh-Hant/codex/app-server#connect-the-cli-terminal-ui)。
此版本也改善了代理伺服器支援、
MCP 重新連線、終端回應速度及 Windows 沙盒的可靠性。

### 使用 GPT-5.6 Sol 處理託管環境中的 Codex 工作

[GPT-5.6 Sol](/zh-Hant/codex/models#recommended-models) 現在為符合資格的客戶提供 Codex 雲端程式碼
審查與品質保證功能。Sol 是 GPT-5.6 的旗艦
模型，適合複雜的程式碼編寫、研究、電腦操作與安全工作。
Codex 雲端會自動選擇模型；Terra 和 Luna 仍可在
支援的本機與網頁介面中使用。

### 為 GPT-5.4 模型停用做好準備

自 8 月 31 日起，使用 ChatGPT 登入的使用者將無法再於 Codex 使用 GPT-5.4 和 GPT-5.4 mini。
請將 `gpt-5.4` 替換為 `gpt-5.6-terra`，並將 `gpt-5.4-mini`
替換為 `gpt-5.6-luna`；更新範圍包括工作區預設值、已儲存的模型設定、
受管組態、自訂智慧體和排程任務。

OpenAI API 與使用 API 金鑰驗證身分的 Codex 工作階段
不受影響。請查看[已棄用的 Codex 模型](/zh-Hant/codex/models#deprecated-codex-models)
與[工作區模型的
可用性](/zh-Hant/codex/enterprise/workspace-model-availability)，並在
停用前完成確認。

## 2026 年 7 月 20–24 日

### 透過 ChatGPT 語音討論工作

由 GPT-Live 驅動的 [ChatGPT 語音](/zh-Hant/codex/features/voice)讓你能在 ChatGPT 桌面版應用程式中，
透過語音討論工作，並協調「對話」、Work 和 Codex 中的任務。
以語音模式開始新對話或任務，接著請 ChatGPT 啟動、查看或
引導其他討論串中的工作。

在 macOS 上，開啟 **螢幕上下文** 後，只要說「看看這個」，
就能分享最前方視窗的[應用程式快照](/zh-Hant/codex/appshots)。

Plus、Pro、Business、Edu 和 Enterprise 方案使用者可在
桌面版應用程式及 [iOS 上的遠端功能](/zh-Hant/codex/remote-connections#set-up-mobile-access)中使用語音。

### 在同一個本機專案中跨多個資料夾工作

ChatGPT 桌面版應用程式的本機專案現在可以包含多個相關資料夾。
您可以選擇一個主要資料夾，用於新增對話、Git 操作，
以及自動尋找 `AGENTS.md`、技能和 `config.toml`。
次要資料夾仍可用於搜尋、讀取與編輯檔案。

開啟 **編輯專案** ，即可[新增資料夾並
選擇主要資料夾](/zh-Hant/codex/projects#use-local-projects-for-folders-and-codebases)。

[請參閱 7 月 23 日版本資訊](/codex/changelog#codex-2026-07-23-app)。

## 2026 年 7 月 13 日至 17 日

### 在桌面版集中管理 Work 對話與專案

ChatGPT 桌面版應用程式現在會將「對話」與 Work 中的對話集中在 ChatGPT 檢視中。
雲端 Work 對話會在網頁版、行動版與桌面版之間同步；本機 Work 對話則保留在您的電腦上。
桌面版應用程式也提供 ChatGPT 專案。
Codex 保留專用檢視與獨立的歷史紀錄，以支援開發人員的工作流程。

[比較桌面版的 ChatGPT Work 與
Codex](/zh-Hant/codex/use-chatgpt#compare-chatgpt-work-and-codex-on-desktop)，選擇
適合您任務的檢視。

### 使用 Codex Micro 掌控並行的 Codex 工作

7 月 15 日，OpenAI 與 Work Louder 推出
[Codex Micro](/zh-Hant/codex/features/codex-micro)，這是一款限量生產的實體控制裝置，
用來操作 ChatGPT 桌面版應用程式中的 Codex。它的智慧體鍵可顯示
最多六個對話的狀態，並在對話間切換。可自訂的指令鍵、
類比搖桿與旋鈕，讓您無須離開鍵盤，就能觸發常用動作或技能、啟動按住說話，
並調整推理強度。

### 透過 Amazon Bedrock 使用 GPT-5.6

GPT-5.6 Sol、Terra 和 Luna 已透過 Amazon Bedrock 正式開放使用。
本機的 ChatGPT Work 和 Codex 介面可使用內建的
[`amazon-bedrock` 提供者](/zh-Hant/codex/amazon-bedrock)，搭配 Bedrock API 金鑰或
AWS SDK 憑證鏈。支援範圍包括 ChatGPT 桌面版應用程式中的 Work 與 Codex，
以及 Codex CLI、IDE 擴充功能和 Codex SDK。

### 在 iOS 上查看 Codex 任務的視覺化內容

iOS 版 ChatGPT 1.2026.188 為 Codex 任務新增行內視覺化功能，
並改善從對話建立及管理任務的體驗，包括讓新建任務的連結
能可靠地開啟對應任務。請參閱
[7 月 13 日 iOS 版本資訊](/codex/changelog#codex-2026-07-13-mobile)。

## 2026 年 7 月 6 日至 10 日

<a id="take-on-ambitious-work-with-chatgpt-work"></a>

### 在 ChatGPT 中挑戰更艱鉅的工作

ChatGPT 中的 [ChatGPT Work](/zh-Hant/codex/get-started-with-work) 可從
您的檔案與[外掛程式](/zh-Hant/codex/plugins)收集上下文，
跨工作流程採取行動，並產生可供審查的文件、簡報、
試算表、Sites 和其他成品。它採用
[GPT-5.6](/zh-Hant/codex/models)，能將目標拆解為步驟並持續工作數小時，期間
您可以追蹤進度、回答問題、調整方向，
以及核准重要動作。

[排程任務](/zh-Hant/codex/automations)可在您不在時繼續推進工作，
支援單次執行、依排程執行、事件發生時執行，
或在監測變更期間執行。

### 選擇合適的 GPT-5.6 模型

[GPT-5.6 系列](/zh-Hant/codex/models#recommended-models)提供三款推薦模型，
可在 ChatGPT Work、ChatGPT 桌面版應用程式、Codex CLI 和 Codex IDE 擴充功能中使用。
Sol 是旗艦模型，適合複雜的程式碼編寫、電腦操作、研究與
安全性工作。Terra 為日常工作兼顧能力與成本，
而 Luna 則是速度最快、成本最低的選擇。預設的 **強效** 設定使用 Sol，並將
推理強度設為「中」。

### 在 ChatGPT 桌面版應用程式中使用 Codex

7 月 9 日，Codex App 併入 macOS 與 Windows 版的
[ChatGPT 桌面版應用程式](/zh-Hant/codex/app)。Codex 保留
專屬的程式碼編寫體驗，與 ChatGPT 的「對話」和 Work 並列。
Codex 支援直接在差異檢視中編輯、在側邊面板中審查 Pull Request、
由 GPT-5.6 驅動且速度更快的[電腦](/zh-Hant/codex/computer-use)功能，
以及包含多個程式碼庫的專案。

既有的 Codex App 使用者可以照常更新。您可以將 Codex 設為預設檢視、
使用 Codex 標誌作為應用程式圖示，並從 ChatGPT 行動版應用程式存取桌面版的 Codex 專案。
更新後的桌面版應用程式已在全球開放給所有 ChatGPT 方案使用者，包括免費版。

## 2026 年 6 月 15 日至 19 日

### 將示範的工作流程轉為可重複使用的技能

透過[錄製與重播](/zh-Hant/codex/extend/record-and-replay)，您可以在 macOS 上向 ChatGPT 或
Codex 示範工作流程，並將示範轉為可重複使用的技能。
這項功能適合用於示範比描述更容易的重複性任務；您可以再調整
產生的技能，並以新的輸入重播。初期開放範圍不包括
歐洲經濟區、英國與瑞士，且需要電腦功能。

<a id="continue-a-task-on-another-host"></a>

### 在另一台主機上繼續對話

透過[對話交接](/zh-Hant/codex/remote-connections#hand-off-a-chat-between-hosts)，
您可以在本機電腦與已連線的遠端主機之間移動對話及其 Git 狀態。
Codex 可以在目的地主機建立或重複使用工作樹、
移轉對話，並從對應的專案繼續工作。

同一個桌面版更新也為排程執行紀錄新增批次操作，
讓您能將所有執行紀錄標為已讀，或一次封存符合條件的執行紀錄。

### 透過 iOS 瀏覽及審查工作區

ChatGPT 行動版應用程式的 **遠端** 功能在 iOS 上新增了工作區檔案瀏覽器、
新增對話時的目錄選擇器、差異檢視的展開與收合控制項，
以及適用於個別對話或跨對話的 MCP 核准選項。

電腦功能、Chrome 擴充功能、記憶與 Chronicle 也開始陸續向歐洲經濟區、英國與瑞士推出。
在這些地區，記憶仍預設關閉；Chronicle 則是供 macOS 上的 ChatGPT Pro 訂閱者
自行選擇啟用的研究預覽功能。

請參閱 [6 月 15 日 iOS](/codex/changelog#codex-2026-06-15-mobile)、
[6 月 16 日開放範圍](/codex/changelog#codex-2026-06-16-app)與
[6 月 18 日 App](/codex/changelog#codex-2026-06-18-app) 的版本資訊。

## 2026 年 6 月 8 日至 12 日

### 使用瀏覽器開發人員模式偵錯網頁應用程式

[開發人員模式](/zh-Hant/codex/browser?surface=app#app-developer-mode)讓 Codex 能在受控的範圍內
使用 Chrome 與內建瀏覽器中的 Chrome DevTools Protocol 功能。
Codex 在分析應用程式效能或偵錯時，可檢查網路流量、主控台輸出、執行階段錯誤與
頁面狀態。在
**設定** \> **瀏覽器**的 **開發人員模式** 下，開啟 **啟用完整 CDP 存取權**。Codex 在網站上使用這項存取權前，
會要求您明確核准。

CDP 與 DOM 快照的最佳化減少了與瀏覽器往返通訊的次數，
讓瀏覽器操作速度最高可達原本的兩倍。

  
    
  

### 將您的設定匯入 Codex

新的移轉流程可在初次設定時，從其他程式開發智慧體匯入支援的設定。
Codex App 也新增 `/init`，用來建立專案指示，
並改善外掛程式管理、瀏覽器診斷，
以及已完成對話的摘要。

<a id="set-up-codex-tasks-from-ios"></a>

### 透過 iOS 設定 Codex 對話

iOS 上的遠端功能現在可以選擇分支、建立工作樹、執行環境設定指令碼、
管理目標，以及新增行內審查留言。

請參閱 [6 月 9 日 App](/codex/changelog#codex-2026-06-09-app)、
[6 月 9 日 iOS](/codex/changelog#codex-2026-06-09-mobile) 與
[6 月 11 日 App](/codex/changelog#codex-2026-06-11-app) 的版本資訊。

## 2026 年 6 月 1 日至 5 日

### 使用 Sites 建立與部署網站

[Sites](/zh-Hant/codex/sites) 讓 ChatGPT 建立、儲存、部署及檢查由 OpenAI 託管的網站、
儀表板、內部工具、網頁應用程式和遊戲。Sites 在網頁版與桌面版 ChatGPT 中
設有專屬入口，讓你能返回專案，
管理託管環境的設定值與機密資訊，無須另外建置
部署所需的整套系統。

### 透過 Amazon Bedrock 使用 Codex

你可以[透過 Amazon Bedrock 使用 Codex](/zh-Hant/codex/amazon-bedrock)，在本機
工作流程中使用由 AWS 管理的身分驗證、帳戶控管和計費。
iOS 上的遠端功能也新增了可選用的應用程式內鎖定、後續訊息行為設定、
差異檢視自動換行，以及透過 SSH 連線至 Windows 電腦的功能。
桌面版應用程式則新增了終端位置控制，並在個人資料檢視中
提供活動分析。

[閱讀 2026 年 6 月的所有版本說明](/codex/changelog#month-2026-06)。

## 2026 年 5 月 25–29 日

### 使用 Windows 應用程式並遠端控制 Codex

[電腦](/zh-Hant/codex/computer-use#windows-foreground-use)功能新增了在 Windows 桌面應用程式中
查看畫面、點擊及輸入文字的支援。開始前請先安裝
電腦外掛程式。在 Windows 上，Codex 會使用目前作用中的桌面，並在任務執行期間
接管前景操作。遠端連線也支援 Windows。
在 ChatGPT 行動版應用程式中，開啟 **遠端** 即可在 Windows 裝置上開始工作，
或使用執行 ChatGPT 桌面版應用程式的 Mac，
並從其他地方查看進度。

iOS 上的遠端功能也新增了 Spotlight 和「捷徑」入口、
瀏覽已封存對話的功能、`/side`，以及儲存或複製算繪完成的圖像的選項。
桌面版應用程式為本機專案和工作樹新增了對話協調功能，
支援依內容與分支名稱搜尋過往對話，並為
背景子代理程式提供一致的視覺識別標記。

閱讀 [5 月 25 日的 iOS](/codex/changelog#codex-2026-05-25-mobile) 與
[5 月 29 日的 App](/codex/changelog#codex-2026-05-28-app) 版本說明。

## 2026 年 5 月 18–22 日

### 透過應用程式快照，將任何 Mac 應用程式的上下文提供給 Codex

同時按下兩個 Command 鍵時，[應用程式快照](/zh-Hant/codex/appshots)會將最前方應用程式視窗的
螢幕截圖與可取得的文字傳送給 Codex。Codex 因此能從
設計工具、儀表板、文件及其他應用程式取得工作所需的上下文，
不必由你複製、貼上或描述螢幕上的內容。

### 追蹤長時間執行的目標

[目標模式](/zh-Hant/codex/prompting#goal-mode)已結束實驗階段，
可在 Codex App、IDE 擴充功能和 CLI 中使用，適合可能需要
數小時或數天完成的目標。[鎖定時使用](/zh-Hant/codex/computer-use#locked-use)可讓 Codex
在 Mac 鎖定後繼續執行已核准的電腦操作工作，也支援透過
ChatGPT 行動版應用程式中的**遠端** 功能執行。ChatGPT Business 工作區也能
[與工作區成員分享可重複使用的外掛程式套件](https://developers.openai.com/plugins/build/plugins#share-a-local-plugin-with-your-workspace)。

[閱讀 5 月 21 日的推出說明](/codex/changelog#codex-2026-05-21)。

## 2026 年 5 月 11–15 日

### 從行動裝置接續桌面上的工作

ChatGPT 行動版應用程式中的 **遠端** 功能可連線至執行 ChatGPT 桌面版應用程式的 Mac。
由於工作是在已連線的主機上執行，因此當你從手機繼續工作時，專案、檔案、
憑證、外掛程式、技能和組態
都仍可使用。請參閱[遠端連線](/zh-Hant/codex/remote-connections)，
了解如何設定主機並從其他裝置接續工作。

### 將可信任的工作流程自動化

掛勾已正式推出，可在智慧體生命週期的關鍵時點
執行自訂指令。ChatGPT Enterprise 管理員也能啟用
[Codex 存取權杖](/zh-Hant/codex/enterprise/access-tokens)，供可信任的指令碼、
排程器及私有 CI 執行器使用。企業指南也擴充了內容，涵蓋
Codex 的受管理設定與控管。

[閱讀 5 月 14 日的推出說明](/codex/changelog#codex-2026-05-13-app)。

## 2026 年 5 月 4–8 日

### 透過 Chrome 擴充功能跨瀏覽器分頁工作

[Chrome 擴充功能](/zh-Hant/codex/chrome-extension)可在背景
跨分頁平行工作，不會接管你的瀏覽器。
你可以控制 Codex 能使用哪些網站，讓你能在同一個任務中整合跨網頁應用程式的研究、
資料輸入與驗證工作。

Codex App 也新增了聽寫文字整理功能，以及用於名稱、
檔案路徑與程式碼符號的自訂字典。ChatGPT Enterprise 工作區擁有者可允許
成員建立 [Codex 存取權杖](/zh-Hant/codex/enterprise/access-tokens)，用於
可信任的非互動式本機工作流程。

閱讀 [5 月 5 日的 App](/codex/changelog#codex-2026-05-05-app)、
[5 月 5 日的存取權杖](/codex/changelog#codex-2026-05-05)及
[Codex for Chrome](/codex/changelog#codex-2026-05-07) 推出說明。

## 2026 年 4 月 20–24 日

### 使用 GPT-5.5 處理複雜工作

[GPT-5.5](/zh-Hant/codex/models) 在 Codex 上線，成為大多數任務的建議模型，
在實作、除錯、測試、電腦操作、
研究與產出完整知識工作成果方面表現出色。

### 讓 Codex 操作瀏覽器並審查核准請求

[內建瀏覽器中的電腦功能](/zh-Hant/codex/browser?surface=app#app-computer-use-in-the-browser)
可讓 Codex 透過點擊操作本機開發伺服器提供的頁面與以檔案為來源的頁面，
重現問題並驗證修正。符合條件的核准請求也可
進行[自動核准審查](/zh-Hant/codex/sandboxing/auto-review)，
在動作執行前顯示審查狀態與風險。

[閱讀 4 月 23 日的推出說明](/codex/changelog#codex-2026-04-23)。

## 2026 年 4 月 13 日至 17 日

### 在同一處預覽並操作工作成果

[內建瀏覽器](/zh-Hant/codex/browser?surface=app)新增了即時預覽和頁面留言，
而[電腦](/zh-Hant/codex/computer-use)功能讓 Codex 能查看並操作 macOS 應用程式。
兩者結合，讓視覺介面實作和端對端驗證
能與程式碼變更在同一個任務中完成。

  
    
  

<a id="start-with-a-task-and-keep-it-moving"></a>

### 從對話開始，持續推進工作

[獨立對話](/zh-Hant/codex/projects#start-without-a-project)讓你不必先選擇專案資料夾，
就能開始工作。這次更新也新增了
[對話內的排程任務](/zh-Hant/codex/automations#schedule-a-task-inside-a-chat)、
Pull Request 上下文、更豐富的檔案預覽，以及[記憶](/zh-Hant/codex/customization/memories)功能，
支援跨對話的工作。

[閱讀 4 月 16 日的 Codex App 版本資訊](/codex/changelog#codex-2026-04-16-app)。

## 2026 年 4 月 6 日至 10 日

### 在應用程式中審查並交付 Pull Request

審查功能新增了可收合的行內留言、行內與獨立審查模式，
並更清楚地呈現 Git 和原始碼上下文。隨後，Pull Request 動態、
留言和推送選項也整合進應用程式，與工作區檔案分頁並列，
讓你不必切換工具，就能檢視變更並回應。

閱讀 [4 月 9 日](/codex/changelog#codex-2026-04-09-app)和
[4 月 10 日](/codex/changelog#codex-2026-04-10-app)的 Codex App 版本資訊，或
瞭解如何[在應用程式中審查變更](/zh-Hant/codex/code-review?surface=app)。

## 2026 年 3 月 23 日至 27 日

### 將工作流程打包為外掛程式

[外掛程式](/zh-Hant/codex/plugins)以可安裝套件的形式推出，整合技能、
連接器和 MCP 伺服器，讓完整的工作流程更容易被找到、安裝與分享。
重新設計的外掛程式和技能頁面，也更清楚地呈現其內容與狀態。
該週也推出了搜尋過往對話的功能。

閱讀[任務搜尋](/codex/changelog#codex-2026-03-24-app)、
[外掛程式推出](/codex/changelog#codex-2026-03-25)和
[Codex App](/codex/changelog#codex-2026-03-25-app) 的版本資訊。

## 2026 年 3 月 16 日至 20 日

### 從先前訊息建立分支，並在撰寫工具中選擇工具

你可以從較早的訊息建立對話分支，
不必捨棄原本的對話進程，就能更輕鬆地嘗試新做法。撰寫訊息時也能使用模型和推理指令，
已啟用的技能會出現在 `@` 選單中，
GPT-5.4 mini 則為較簡單的任務和子代理程式提供了更快速的選擇。

閱讀 [GPT-5.4 mini](/codex/changelog#codex-2026-03-17)、
[對話控制](/codex/changelog#codex-2026-03-18-app)和
[技能選單](/codex/changelog#codex-2026-03-19-app)的版本資訊。

## 2026 年 3 月 9 日至 13 日

### 為排程工作選擇合適的環境

[排程任務](/zh-Hant/codex/automations)可在本機或工作樹中執行，
並可明確指定模型和推理等級。可重複使用的範本讓常見任務的設定更快速，
自訂主題則讓你更容易
打造個人化的工作區。

  
    
  

### 讓 Codex 檢查終端輸出

Codex 也能讀取目前對話的[整合式終端](/zh-Hant/codex/integrated-terminal#run-and-validate-your-project)，
直接檢視執行中的開發伺服器或建置輸出，
不必再請你貼上內容。

閱讀 [3 月 11 日](/codex/changelog#codex-2026-03-11-app)與
[3 月 12 日](/codex/changelog#codex-2026-03-12-app)的 Codex App 版本說明。

## 2026 年 3 月 2–6 日

### 在 Windows 上原生執行 Codex

Codex App 推出 [Windows](/zh-Hant/codex/windows/windows-app) 版，原生支援 PowerShell
與沙盒，並提供工作樹、排程任務和技能。偏好 Linux 環境的開發人員
仍可使用 WSL。

  
    
  

<a id="move-tasks-between-local-and-worktree"></a>

### 在本機與工作樹之間移動對話

[本機與工作樹之間的交接功能](/zh-Hant/codex/environments/git-worktrees#working-between-local-and-worktree)
讓你能在保留上下文的情況下移動進行中的對話。GPT-5.4
也在同一週加入 Codex，支援程式碼編寫、電腦操作，以及需要較長上下文的
工作流程。

閱讀 [Windows 版推出](/codex/changelog#codex-2026-03-04-app)、
[工作樹交接](/codex/changelog#codex-2026-03-03-app)與
[GPT-5.4](/codex/changelog#codex-2026-03-05) 的版本說明。

## 2026 年 2 月 9–13 日

### 即時迭代，建立分支探索不同做法

GPT-5.3-Codex-Spark 推出研究預覽版，以近乎即時的回應速度支援
即時程式碼迭代。Codex App 也新增了對話分支和
永遠置頂的浮動對話視窗，讓你能探索其他做法，或
將 Codex 放在編輯器或瀏覽器旁。

閱讀 [Spark](/codex/changelog#codex-2026-02-12) 與
[Codex App](/codex/changelog#codex-2026-02-12-app) 的版本說明，或參閱
目前的[模型指南](/zh-Hant/codex/models)。

## 2026 年 2 月 2–6 日

### Codex App 推出 macOS 版

Codex App 最初以桌面工作區的形式推出，可同時進行多個專案對話，
並提供內建 Git 審查、工作樹、技能、排程任務和語音聽寫功能。
如今，你可以在 [ChatGPT 桌面版應用程式](/zh-Hant/codex/app) 的 Codex 中使用這些功能。

  
    
  

### 調整進行中工作的方向並加入檔案

回應中途引導功能讓你不必停止
進行中的回應，就能調整 Codex 的方向；檔案附件也不再僅限於圖片。這些互動方式
奠定了[透過後續訊息引導工作，以及將訊息排入佇列](/zh-Hant/codex/prompting#steering-and-queuing)的基礎，
讓你能提供 Codex 所需的上下文。

閱讀 [Codex App 推出說明](/codex/changelog#codex-2026-02-02)與
[2 月 5 日 App 版本說明](/codex/changelog#codex-2026-02-05-app)。
