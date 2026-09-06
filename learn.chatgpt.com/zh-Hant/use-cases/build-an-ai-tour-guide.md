<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/build-an-ai-tour-guide -->

## 簡介

有些工作流程只要有人指引該前往哪裡、選取什麼，就更容易上手。使用 Codex 建立導覽，引導使用者操作你的網頁應用程式，讓他們親自執行各項動作。

透過能存取應用程式控制項、狀態及文件的 WebMCP 工具，Codex 可以根據使用者看到的畫面，選擇下一步的操作指引。尚未連線至服務的使用者，與已完成設定的使用者，需要從不同的步驟開始。

## 使用方式

1. 在 Codex 中開啟應用程式的程式碼庫，並選擇一個要引導的工作流程，例如連線至服務或新增資料夾。
2. 提供相關文件，並說明導覽應處理哪些初始狀態。
3. 執行本頁的起始提示詞，加入導覽目標、UI 狀態工具，以及存取應用程式操作指示的功能。
4. 在 Codex 能呼叫應用程式 WebMCP 工具的瀏覽器環境中測試流程。請 Codex 引導你，再親自完成每個步驟。

第一個導覽的範圍應保持精簡。先確認它能引導使用者從設定一路完成流程，再加入更多工作流程。

## 範例：在 Runme 中新增 Google Drive 資料夾

在 <a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a> 中，使用者可以編輯筆記本，並透過檔案總管新增 Google Drive 資料夾及瀏覽檔案。導覽可協助新使用者找到這些控制項，並熟悉操作流程。

若想進一步了解 Runme，可以閱讀〈<a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">在 OpenAI 使用 Codex 自動化重複性工作</a>〉。

觀看 Codex 如何醒目標示 Runme 的控制項並解釋其用途。下方螢幕擷取畫面展示另一個專門引導使用者新增 Google Drive 資料夾的導覽。

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    你的瀏覽器不支援影片標籤。
  </video>
</figure>

Google Drive 導覽從一個請求開始：

### 連線至 Google Drive

Codex 會檢查 Google Drive 是否已連線。如果尚未連線，Codex 會醒目標示「 **連線至 Google Drive** 」，並請使用者選取該控制項以完成連線。

![Codex 醒目標示 Runme 中的「連線至 Google Drive」，並說明如何開始。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### 開啟檔案總管

連線完成後，Codex 會引導使用者前往檔案總管。下一步的操作指引會依更新後的應用程式狀態調整。

![Codex 醒目標示用來開啟 Runme 檔案總管的控制項。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### 新增資料夾

使用者展開工具列後，Codex 會醒目標示用來新增 Google Drive 資料夾的控制項。使用者全程掌握操作，也能學會下次要在哪裡找到這個控制項。

![Codex 醒目標示 Runme 中用來新增 Google Drive 資料夾的控制項。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## 提供 Codex 引導使用者所需的上下文

Runme 的實作提供三類上下文：導覽目標、應用程式狀態及文件。以下工具名稱來自 Runme；請依照相同的功能分工，為你的應用程式設計工具。

### 讓控制項能被找到

為導覽目標設定穩定且具有語意的 `data-tour-id` 值，並為每個目標提供標籤及描述。Runme 透過三個 WebMCP 工具提供這些控制項的存取介面：

- `listTargets` 列出已註冊的目標、ID、標籤及描述。
- `showTourStep({ target, title?, message, placement? })` 醒目標示目標並顯示說明。
- `dismiss` 移除醒目標示。

如此一來，Codex 就能識別控制項並解釋其用途，而不必代替使用者執行該控制項的動作。

### 讀取狀態並等待使用者操作

Runme 將導覽相關狀態保存在 React 外部，並透過控制器提供存取。其 `getUiSnapshot` 工具會提供目前的 UI 狀態，包括登入狀態。`waitForUiChange(...)` 則讓 Codex 等待狀態變更，例如使用者選取醒目標示的控制項。

請 Codex 在每次互動後重新讀取狀態。是否推進導覽，應取決於應用程式中實際發生的情況，而非 Codex 是否已顯示操作指引。

### 將操作指示隨應用程式一併提供

Runme 將 Markdown 文件與應用程式一併封裝，並透過 WebMCP 提供存取：

- `readInstructionsForAIAgents` 說明 Codex 應如何與應用程式及其工具互動。
- `listDocumentation()` 列出可用的頁面及其描述。
- `getDocumentation({ name })` 以 Markdown 格式傳回選定的頁面。

導覽的操作指示及工具可以隨應用程式一併發布，不需要另行提供專用的 Codex 導覽外掛程式。

## 審查導覽

從不同的初始狀態提出相同請求。確認導覽會略過已完成的設定、等待使用者操作，並在 UI 變更時更新指引。

也要測試步驟遭取消及控制項尚未顯示的情境。Codex 應說明缺少什麼，或選擇可行的下一步，不應只因為醒目標示了按鈕，就宣稱動作已成功完成。

身分驗證、權限檢查及使用者操作都應維持在應用程式的既有流程中。導覽應協助使用者了解介面，而不繞過這些控管機制。

## 後續建議

第一個流程正常運作後，可以在同一段對話中繼續：

- 「在 Google Drive 已連線且檔案總管已關閉的情況下，測試這個導覽。」
- 「處理使用者取消某個步驟後，又要求繼續導覽的情況。」
- 「為 \[next workflow\] 新增導覽，沿用現有的導覽目標與狀態工具。」
