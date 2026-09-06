<!-- source: https://learn.chatgpt.com/zh-Hant/docs/reference/troubleshooting -->

## 常見問題

### 側邊面板中出現 Codex 未編輯的檔案

如果您的專案位於 Git 程式碼庫內，審查窗格會根據專案的 Git 狀態自動
顯示變更，其中也包括並非由 Codex
所做的變更。

在審查窗格中，您可以在已暫存與尚未
暫存的變更之間切換，並將您的分支與 main 比較。

若只想查看 Codex 上一輪所做的變更，請將差異
窗格切換至 **上一輪** 檢視。

[進一步瞭解如何使用審查窗格](/zh-Hant/codex/code-review?surface=app)。

### 從側邊欄移除專案

若要從側邊欄移除專案，請將游標移到專案名稱上，按一下
三點圖示，然後選擇「移除」。若要還原，請重新加入
專案：使用 **新增專案** 按鈕（位於 **對話** 旁），或按下

<kbd>Cmd</kbd>+<kbd>O</kbd>。

<a id="find-archived-threads"></a>
<a id="find-archived-tasks"></a>

### 尋找已封存的對話

已封存的對話可在 [設定](codex://settings) 中找到。取消封存
對話後，對話會重新出現在側邊欄中的原始位置。

<a id="only-some-threads-appear-in-the-sidebar"></a>
<a id="only-some-tasks-appear-in-the-sidebar"></a>

### 側邊欄只顯示部分對話

側邊欄可讓您依專案狀態篩選對話。如果有
對話未顯示，請選取 **對話** 旁的篩選圖示，然後選取
**依時間排序**。如果仍找不到該對話，請開啟
[設定](codex://settings)，並查看 **已封存的對話**。

### 程式碼無法在工作樹中執行

工作樹會建立在不同的目錄中，且預設會繼承已提交至
Git 的檔案。視您管理專案相依性與工具的方式而定，
您可能必須在工作樹中使用
[本機環境](/zh-Hant/codex/environments/local-environment) 執行設定指令碼，或複製已忽略的設定檔案，
方法是使用 [`.worktreeinclude`](/zh-Hant/codex/environments/git-worktrees#copy-ignored-local-files-into-managed-worktrees)。
另一種做法是在一般的本機專案中簽出這些變更。若要深入瞭解，請參閱
[工作樹文件](/zh-Hant/codex/environments/git-worktrees)。

### App 未偵測到隊友分享的本機環境

本機環境組態必須放在 `.codex` 資料夾中，此資料夾必須位於
專案根目錄。如果您使用包含多個
專案的 monorepo，請確定您是在包含
`.codex` 資料夾的目錄中開啟專案。

### Codex 要求存取 Apple Music

根據您的任務，Codex 可能需要瀏覽檔案系統。macOS 上的某些
目錄（包括「音樂」、「下載項目」或「桌面」）需要
使用者另行核准。如果 Codex 需要讀取您的主目錄，
macOS 會提示您核准存取這些資料夾。

<a id="automations-create-many-worktrees"></a>

### 排程任務會建立許多工作樹

頻繁執行的排程任務久而久之可能建立許多工作樹。請封存不再需要的排程
執行作業；除非您打算保留這些執行作業的
工作樹，否則請勿釘選這些執行作業。

### 選錯目標後復原提示詞

如果不小心選錯目標（**本機**、**工作樹**，或 **雲端**）並開始了對話，您可以取消目前的執行作業，然後在撰寫工具中按向上鍵，以復原上一個提示詞。

### 功能可在 Codex CLI 中運作，但無法在 ChatGPT 桌面 App 中運作

ChatGPT 桌面 App 和 Codex CLI 可能包含不同版本的 Codex，因此
功能可能會先在其中一個介面推出，再於另一個介面推出。實驗性功能可能
也會先在 Codex CLI 推出。

若要取得系統上的 Codex CLI 版本，請執行：

```bash
codex --version

若要取得 ChatGPT 桌面 App 隨附的 Codex 版本，請使用
為維持相容性而保留的 `Codex.app` 套件組路徑：

```bash
/Applications/Codex.app/Contents/Resources/codex --version

## 意見回饋與記錄檔

在訊息輸入框中輸入 <kbd>/</kbd>，向團隊提供意見回饋。如果
您在現有對話中啟動意見回饋流程，可以選擇將
現有工作階段連同意見回饋一起分享。提交意見回饋後，
您會收到可與團隊分享的工作階段 ID。

若要回報問題：

1. 在 Codex 的 GitHub 程式碼庫中尋找 [現有議題](https://github.com/openai/codex/issues)。
2. [建立新的 GitHub 議題](https://github.com/openai/codex/issues/new?template=2-bug-report.yml&steps=Uploaded%20thread%3A%20019c0d37-d2b6-74c0-918f-0e64af9b6e14)

更多記錄檔位於下列位置：

- App 記錄檔（macOS）： `~/Library/Logs/com.openai.codex/YYYY/MM/DD`
- 工作階段轉錄檔： `$CODEX_HOME/sessions`（預設： `~/.codex/sessions`）
- 已封存的工作階段： `$CODEX_HOME/archived_sessions`（預設： `~/.codex/archived_sessions`）

如果要分享記錄檔，請先檢查內容，確認其中不含敏感
資訊。

## 卡住狀態與復原方式

如果對話似乎卡住：

1. 檢查 Codex 是否正在等待核准。
2. 開啟終端並執行 `git status` 之類的基本指令。
3. 以範圍較小且更聚焦的提示詞開始新對話。

如果您不小心取消建立工作樹而遺失提示詞，請在撰寫工具中按向上
鍵以復原提示詞。

## 終端問題

**終端似乎卡住**

1. 關閉終端面板。
2. 按下 <kbd>Ctrl</kbd>+<kbd>\`</kbd> 重新開啟終端。
3. 重新執行 `pwd` 或 `git status` 之類的基本指令。

如果指令行為與預期不同，請先在終端中確認目前的目錄和
分支。

如果仍然卡住，請等您進行中的對話全都完成後，再重新啟動 App。

**字型無法正確顯示**

Codex 在審查窗格、整合式終端，以及 App 內顯示的其他所有程式碼中使用相同字型。您可以在 [設定](codex://settings) 窗格中，透過 **程式碼字型** 選項設定此字型。
