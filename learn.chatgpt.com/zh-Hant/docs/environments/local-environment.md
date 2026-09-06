<!-- source: https://learn.chatgpt.com/zh-Hant/docs/environments/local-environment -->

本機環境可讓您設定工作樹的準備步驟，以及專案的常用動作。

  本機環境僅適用於 ChatGPT 桌面版應用程式中的 Codex。
  設定或使用本機環境前，請先選取 **Codex** 。

您可以透過 [ChatGPT 桌面版應用程式設定](codex://settings)窗格來設定本機環境。您可以將產生的檔案簽入專案的 Git 程式碼庫，與其他人共用。

Codex 會將此組態儲存在專案根目錄的 `.codex` 資料夾中。
如果您的程式碼庫包含多個專案，請開啟
包含共用 `.codex` 資料夾的專案目錄。

## 設定指令碼

由於工作樹的執行目錄與本機對話不同，專案可能尚未完成設定，也可能缺少相依套件或未簽入程式碼庫的檔案。Codex 在新對話開始時建立工作樹時，設定指令碼會自動執行。

使用此指令碼執行設定環境所需的任何指令，例如安裝相依套件或執行建置流程。

例如，對於 TypeScript 專案，您可以使用設定指令碼安裝相依套件，並執行初始建置：

```bash
npm install
npm run build

如果您的設定因平台而異，請定義 macOS、Windows 或 Linux 專用的設定指令碼，以覆寫預設指令碼。

## 動作

<section class="feature-grid">

<div>
使用動作來定義常用任務，例如啟動應用程式的開發伺服器或執行測試套件。這些動作會顯示在 ChatGPT 桌面版應用程式的頂端列，方便快速存取。這些動作會在應用程式的[整合式終端](/zh-Hant/codex/integrated-terminal)中執行。

使用動作可省去反覆輸入觸發專案建置或啟動開發伺服器等常用操作的指令。若只需進行一次快速偵錯，可直接使用整合式終端。

</div>

  
    
  

</section>

例如，您可以為 Node.js 專案建立包含下列指令碼的「執行」動作：

```bash
npm start

如果動作所用的指令因平台而異，請為 macOS、Windows 和 Linux 分別定義適用於各平台的指令碼。

請為每個動作選擇對應的圖示，以便識別。

## 使用內建 Git 工具

<div class="my-8 grid gap-6 md:grid-cols-[minmax(0,1fr)_minmax(16rem,42%)] md:items-center">

<div>

在 Codex 中，ChatGPT 桌面版應用程式會在每個本機專案和工作樹旁提供
常用的 Git 控制項。差異窗格會顯示目前簽出內容的變更，
並讓您加入行內註解，交由 Codex 處理。您可以暫存或還原個別區塊、
暫存或還原整個檔案、提交變更、推送分支，以及建立 Pull Request，
全程無須離開應用程式。

使用 [整合式終端](/zh-Hant/codex/integrated-terminal) 執行應用程式未提供的 Git
操作。若要隔離同時進行的變更，
避免影響本機簽出內容，請在 [工作樹](/zh-Hant/codex/environments/git-worktrees) 中啟動任務。

</div>

  

</div>
