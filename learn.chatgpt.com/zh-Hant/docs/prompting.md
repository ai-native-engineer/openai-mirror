<!-- source: https://learn.chatgpt.com/zh-Hant/docs/prompting -->

<a id="prompts"></a>

## 提示詞概覽

提示詞是你用來告訴 ChatGPT 想了解、製作或變更什麼的方式。提示詞可以是問題、指示或目標。你不需要使用技術語法或遵循固定公式。先用自己的話說明需求，檢視回覆，再透過後續訊息調整結果。

簡短的提示詞通常就足夠。面對規模較大或更重要的任務時，請納入真正重要的要素：

- **目標：** ChatGPT 應該做什麼？
- **上下文：** 哪些資訊或資料來源會有幫助？
- **輸出：** 你需要什麼格式、長度或詳細程度？
- **界限：** 哪些內容必須維持不變？ChatGPT 應避免哪些事項，或在採取行動前應與你
  確認哪些事項？

只使用有幫助的部分即可。你不必填寫每個項目，也不必遵循特定格式。

## 說明你需要的結果

先說明需要的結果，而不是詳列步驟。如果受眾或格式會影響 ChatGPT 應產生的內容，請一併說明。

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

這個提示詞說明要建立什麼，以及誰會閱讀。若流程本身很重要，請加以說明；否則，應讓 ChatGPT 保有搜尋、比較資訊及調整做法的空間。

<a id="context"></a>

## 補充有用的上下文

提供可能影響結果的資訊。只加入真正重要的資料來源，並說明 ChatGPT 應從每個來源取得哪些資訊。

- 若希望
  ChatGPT 摘要、比較或轉換內容，或[建立供審查的檔案](/zh-Hant/codex/artifacts-viewer)，請附上文件、試算表、簡報或 PDF 檔案。
- 如果任務需要視覺上下文，請提供螢幕截圖、圖表或其他[圖像輸入](/zh-Hant/codex/image-inputs)，
  並指出重要區域，
  不要只依靠圖像本身。
- 若答案需要最新資訊，請要求 ChatGPT 使用[網頁搜尋](/zh-Hant/codex/web-search)；
  需要查核結果時，也請要求提供資料來源。
- 使用[專案](/zh-Hant/codex/projects)，讓相關對話共用檔案、
  資料來源或本機資料夾。

### 使用已連線的資料來源

當 ChatGPT 能存取已連線的資料來源時，請指明應查找的位置和內容。你不必逐一說明它應執行哪些搜尋。

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

已連線的資料來源需要對應的外掛程式，是否可用可能取決於你的方案和工作區設定。

### 使用外掛程式

外掛程式可為 ChatGPT 和 Codex 提供可重複使用的指示，並連線至
Google Drive、Gmail、Slack 和 GitHub 等工具。兩項產品都從同一個通用目錄取得公開外掛程式。
請說明需要的結果，
並讓目前使用的介面從可用工具中選擇。在 ChatGPT 的訊息輸入框中輸入 `@`
即可選擇特定外掛程式。

  
    <span slot="icon">
      
    </span>
    在 ChatGPT 和 Codex 中尋找、安裝及使用外掛程式。
  

### 個人化 ChatGPT

請在 **設定 \> 個人化**
中，將適用於所有對話的偏好設為自訂指令。只與目前對話相關的細節，請寫在
提示詞中。

  
    <span slot="icon">
      
    </span>
    設定預設個性、自訂指令及其他應用程式偏好設定。
  

## 設定界限，避免造成實際問題

界限是 ChatGPT 避免增加額外工作或採取非預期行動所需的少數幾項指示。若改錯細節會使結果無法使用，或你希望在相關事項影響他人前先行審查，就應加入界限。

- 請勿變更已核准的日期和預算金額。
- 只使用提供的資料來源。請標示缺少的資訊，不要自行猜測。
- 提出的建議不得超出指定預算。
- 將訊息寫成草稿，不要傳送。

專注於最重要的一兩項界限即可。你不需要控制 ChatGPT 採取的每個步驟。

## 讓結果可直接使用

請告訴 ChatGPT 你打算如何使用結果，協助它選擇適當的長度、詳細程度和編排方式。

- 整理成一頁摘要，讓主管能在會議前快速瀏覽。將決策和後續步驟放在最前面。
- 將這些筆記整理成後續電子郵件，列出決策、負責人和截止日期。
- 建立清楚的表格，比較預計支出與實際支出，並醒目標示任何超過 10% 的差異。

對於重要工作，請要求 ChatGPT 進行最後檢查，例如確認每個行動項目都有負責人和截止日期，或標示無法驗證的資訊。接著，在使用或分享結果前，請親自檢視。

## 透過後續訊息改善結果

第一個提示詞不必完美。先檢視結果，再說明你想要的具體變更。

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

你可以補上缺少的資料來源、修正方向、要求其他方案，或調整詳細程度，不必從頭開始。

### 引導與排入佇列

當 Codex 已在處理工作時，你仍可傳送另一則訊息，不必等待目前這次執行完成：

- **引導** 會將訊息加入目前這次執行。可用來調整方向、補上
  缺少的細節，或提供新資訊。
- **排入佇列** 會將訊息保留給下一次執行。若後續訊息需要
  等目前工作完成後再處理，請使用這項功能。

在 ChatGPT 桌面版應用程式中，請在
[**設定 \> 一般 \> 後續訊息行為**](/zh-Hant/codex/app/settings#general)中選擇預設行為。
排入佇列的訊息會顯示在訊息輸入框上方，你可以編輯、重新排序、傳送或
刪除這些訊息。該設定也會顯示快速鍵，讓你在不變更預設行為的情況下，
針對單一訊息使用另一種行為。

在 Codex CLI 中，當 Codex 正在執行時，按下 <kbd>Enter</kbd> 可引導目前
回合，或按下 <kbd>Tab</kbd> 將訊息排入下一回合的佇列。請參閱
[互動式快速鍵](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
以瞭解詳情。

## 整合各項要素

如果要使用已連線的資料來源整理專案進度，完整的提示詞可以這樣寫：

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

這個提示詞涵蓋 **目標**、 **上下文**、 **輸出**和 **界限**，並
要求進行最後檢查，無須逐一詳述每個步驟。

## 使用語音聽寫

在 ChatGPT 桌面版應用程式中，訊息輸入框顯示時按下 <kbd>Ctrl+Shift+D</kbd>
即可開始說話。ChatGPT 會將你說的內容轉錄至訊息輸入框，
讓你在傳送提示詞前檢視及編輯。

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## 對話提示詞範例

使用對話來提問、發想、撰寫草稿及處理日常決策。先說明想要的結果，只有在細節會影響答案時才補充。

### 瞭解主題

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### 草擬並潤飾文字

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### 比較選項

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### 擬定可行計畫

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## ChatGPT Work 提示詞

若要快速提問、進行簡短改寫、腦力激盪或撰寫簡單的
草稿，請使用對話。若任務需要運用不同來源或工具、包含一
連串步驟、進行變更，或產出較大型的成果，請使用 ChatGPT Work。

在 ChatGPT Work 中，請描述所需成果、提供來源材料、指出
受眾，並說明你會如何審查工作成果。請 ChatGPT 規劃、
蒐集所需資訊、建立檔案，並在完成前檢查這些檔案。

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### 有效運用 ChatGPT Work

ChatGPT Work 適合處理耗時或週期性任務，也適合製作可供你
重複使用的成品檔案。若能節省
時間、提升品質或協助你做出重要決策，即使任務會使用較多點數，仍可能值得執行。

從一項你可以審查的成果開始：

- 只納入相關來源，並在適當時限制日期範圍。
- 明確指定受眾、輸出格式和所需長度。
- 將必要工作與選用的改善或潤飾項目分開。
- 當執行方式很重要時，請要求 ChatGPT 先提出計畫。ChatGPT
在傳送、發布或變更他人仰賴的資訊之前，必須先取得你的核准。
- 如果任務開始進行你不再需要的工作，請縮小範圍或停止任務。

審查第一份成果、調整指示，並在工作流程可行時
重複使用。

### 將來源材料轉化為成品檔案

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### 為決策進行研究

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### 協調發布作業

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

對於週期性工作，請先在一般對話中調整提示詞。確認輸出結果
可靠後，[在該對話中排程任務](/zh-Hant/codex/automations#schedule-a-task-inside-a-chat)。
如果每次排程執行都應開啟
新的對話，請改為建立獨立的排程任務。

<a id="use-editor-context"></a>

## Codex 提示詞

若要讓 ChatGPT 處理程式碼、程式碼庫或開發工具，請使用 Codex。
實用的 Codex 提示詞會說明你想要的行為、指出相關程式碼或
重現步驟、納入重要限制，並說明如何驗證
變更。

<a id="goal-mode"></a>

針對多步驟任務，請在 App 撰寫工具中輸入 `/plan`，讓 Codex
在編輯前先調查並提出作法。當 [目標模式](/zh-Hant/codex/long-running-work)
可用時，請在計畫完成後使用 `/goal` 設定持續性目標。請參閱 [App 斜線
指令](/codex/reference/slash-commands)，
查看目前的指令清單。

### 如何閱讀這些範例

每個工作流程都包含下列內容：

- **適用時機** ，以及最適合使用的 Codex 介面（IDE、CLI 或雲端）。
- **步驟** ，並附上使用者提示詞範例。
- **上下文說明**：Codex 會自動取得哪些內容，以及你應附加哪些內容。
- **驗證**：如何檢查輸出結果。

> **注意：** IDE 擴充功能會自動將你開啟的檔案納入上下文。在 CLI 中，請明確指出路徑，或使用 `/mention` 及 `@` 路徑自動完成功能來附加檔案。

Codex 會使用 [沙盒](/zh-Hant/codex/sandboxing)
執行本機指令；該沙盒會限制檔案和網路存取。若任務需要跨越這項界線，
Codex 會先遵循你的核准政策，再繼續執行。

### 解說程式碼庫

適合在你剛開始熟悉系統、接手服務，或試圖釐清通訊協定、資料模型或請求流程時使用。

#### IDE 擴充功能工作流程（最快的本機探索方式）

1. 開啟最相關的檔案。
2. 選取你關注的程式碼（可選，但建議這麼做）。
3. 向 Codex 輸入提示詞：

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

驗證：

- 要求提供可供你驗證的圖解或檢查清單：

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### CLI 工作流程（適合需要操作記錄和 Shell 指令時使用）

1. 啟動互動式工作階段：

   ```bash
   codex

2. 附加檔案（可選）並輸入提示詞：

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

上下文說明：

- 你可以在撰寫工具中使用 `@` 插入工作區內的檔案路徑，或使用 `/mention` 附加特定檔案。

### 修正錯誤

當你遇到可在本機重現的異常行為時，請使用此方法。

#### CLI 工作流程（快速反覆進行重現與驗證）

1. 從程式碼庫根目錄啟動 Codex：

   ```bash
   codex

2. 向 Codex 提供重現步驟，以及你懷疑有問題的檔案：

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

上下文說明：

- 由你提供：重現步驟與限制條件（這些資訊比概略說明更重要）。
- 由 Codex 提供：指令輸出、找到的呼叫位置，以及執行過程中觸發的任何堆疊追蹤。

驗證：

- 修正後，Codex 應再次執行重現步驟。
- 如果有標準檢查流程，請 Codex 執行該流程：

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### IDE 擴充功能工作流程

1. 開啟你認為錯誤所在的檔案，以及其最接近的呼叫端。
2. 向 Codex 輸入提示詞：

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### 撰寫測試

適合在你想精確界定測試範圍時使用。

#### IDE 擴充功能工作流程（以選取內容為基礎）

1. 開啟包含該函式的檔案。
2. 選取定義該函式的程式碼行。從指令選擇區選擇「Add to Codex Thread」，將這些程式碼行加入上下文。
3. 向 Codex 輸入提示詞：

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

上下文說明：

- 由「Add to Codex Thread」指令提供：選取的程式碼行（這就是「行號」範圍），以及開啟的檔案。

#### CLI 工作流程（在提示詞中描述路徑和行號範圍）

1. 啟動 Codex：

   ```bash
   codex

2. 在提示詞中指定函式名稱：

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### 根據螢幕截圖製作原型

想將設計稿、螢幕截圖或 UI 參考資料轉換成可運作的原型時，請使用此工作流程。

#### CLI 工作流程（圖像 + 提示詞）

1. 將螢幕截圖儲存至本機（例如 `./specs/ui.png`）。
2. 執行 Codex：

   ```bash
   codex

3. 將圖像檔案拖曳至終端，以附加至提示詞。

4. 接著補充限制條件與結構：

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

上下文注意事項：

- 圖像呈現視覺需求，但你仍需指定實作限制條件（框架、路由和元件樣式）。
- 以文字補充圖像未呈現的行為，例如滑鼠懸停狀態、驗證規則或鍵盤互動。

驗證：

- 如果允許，請 Codex 執行開發伺服器，並明確說明應查看的位置：

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### IDE 擴充功能工作流程（圖像 + 現有檔案）

1. 在 Codex 對話中附加圖像（拖放或貼上）。
2. 向 Codex 輸入提示詞：

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### 透過即時更新反覆調整 UI

想在 Codex 編輯程式碼時，持續進行「設計 → 微調 → 重新整理 → 微調」的緊湊循環時，請使用此工作流程。

#### CLI 工作流程（執行 Vite，再以簡短提示詞反覆調整）

1. 啟動 Codex：

   ```bash
   codex

2. 在另一個終端視窗中啟動開發伺服器：

   ```bash
   npm run dev

3. 輸入提示詞，請 Codex 進行變更：

   ```text
   Propose 2-3 styling improvements for the landing page.

4. 選定方向，並使用簡短且明確的提示詞反覆調整：

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. 針對特定項目重複提出要求：

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

驗證：

- Codex 更新程式碼時，請在瀏覽器中檢視變更。
- 提交你滿意的變更，並還原不滿意的變更。
- 如果你還原或修改某項編輯內容，請告知 Codex，以免它處理下一個提示詞時覆寫你的編輯。

### 將重構工作委派至雲端

想先根據本機上下文規劃做法，再將耗時的實作工作委派給可平行執行的雲端對話時，請使用此工作流程。

#### 本機規劃（IDE）

1. 請確認目前的工作已提交，或至少已儲藏，以便清楚比較變更。
2. 請 Codex 擬定重構計畫。如果可以使用 `$plan` 技能，請明確叫用該技能：

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. 審查計畫並討論調整方式：

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

上下文注意事項：

- 當 Codex 能在本機掃描現有程式碼（進入點、模組邊界和相依關係圖線索）時，規劃效果最佳。

#### 雲端委派（IDE → 雲端）

1. 如果尚未設定，請設定 [Codex 雲端環境](/zh-Hant/codex/environments/cloud-environment)。
2. 按一下提示詞撰寫工具下方的雲端圖示，然後選取你的雲端環境。
3. 輸入下一個提示詞時，Codex 會在雲端建立新的對話，並沿用現有對話的上下文（包括計畫及任何本機原始碼變更）。

   ```text
   Implement Milestone 1 from the plan.

4. 審查雲端差異，並視需要反覆調整。

5. 直接從雲端建立 PR，或將變更拉取至本機進行測試並完成收尾。

6. 繼續針對計畫中的其他里程碑反覆調整。

委派至雲端的任務會在隔離環境中執行。在智慧體執行階段，網際網路存取會
保持關閉，除非你為該環境啟用這項功能。進一步瞭解
[雲端網際網路存取](/zh-Hant/codex/cloud/internet-access)。

### 進行本機程式碼審查

想在提交變更或建立 PR 前多一道檢查時，請使用此工作流程。

#### CLI 工作流程（審查你的工作樹）

1. 啟動 Codex：

   ```bash
   codex

2. 執行審查指令：

   ```text
   /review

3. 選用：提供自訂的審查重點指示：

   ```text
   /review Focus on edge cases and security issues

驗證：

- 根據審查意見修正問題，然後重新執行 `/review`，確認問題已解決。

### 審查 GitHub Pull Request

想在不必將分支拉取至本機的情況下取得審查意見時，請使用此工作流程。

使用此功能前，請先在程式碼庫中啟用 Codex **程式碼審查** 。請參閱 [程式碼審查](/zh-Hant/codex/third-party/github)。

#### GitHub 工作流程（留言驅動）

1. 在 GitHub 上開啟 Pull Request。
2. 留言標註 Codex，並明確列出審查重點：

   ```text
   @codex review

3. 選用：提供更明確的指示。

   ```text
   @codex review for security vulnerabilities and security concerns

### 更新文件

需要對文件進行準確且清楚的變更時，請使用此工作流程。

#### IDE 或 CLI 工作流程（本機編輯 + 本機驗證）

1. 找出要變更的文件檔案，並開啟這些檔案（IDE），或使用 `@` 提及這些檔案（IDE 或 CLI）。
2. 向 Codex 提供提示詞，說明工作範圍與驗證要求：

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Codex 擬定變更內容後，請審查文件並視需要反覆調整。

驗證：

- 閱讀轉譯後的頁面。
