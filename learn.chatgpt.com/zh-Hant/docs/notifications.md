<!-- source: https://learn.chatgpt.com/zh-Hant/docs/notifications -->

通知會在工作需要你留意時提醒你。其控制項與
傳送管道會因介面而異。

## 設定桌面通知

開啟 [**設定**](codex://settings)，選擇回合完成提醒的顯示時機：
永不顯示、僅在 ChatGPT 於背景執行時顯示，或一律顯示。另外，
你可以使用個別控制項，分別開啟或關閉權限通知和問題通知。你的
作業系統可能會要求你授予 ChatGPT
桌面應用程式通知權限。

### 在活動檢視中追蹤對話

當 **活動** 可用時，選取側邊欄中的鈴鐺圖示，即可查看
未讀、執行中或正在等待你回覆的對話。你也可以
在 macOS 上使用 <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>U</kbd>，
或在 Windows 上使用 <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>U</kbd>，開啟或關閉活動檢視。

使用這個檢視的選項來選擇要顯示的對話。視你目前使用的
介面而定，選項可能包括 **Work**、**對話**、**已釘選** 和
**排程**。你也可以選取 **全部標示為已讀**，以清除未讀項目。

<a id="follow-task-activity-with-a-pet"></a>

### 透過寵物追蹤對話活動

在 ChatGPT 桌面應用程式中，你還可以在使用其他應用程式時，透過浮動寵物追蹤對話
活動。它可以顯示對話目前的狀態是 **執行中**、
**需要輸入**、**已就緒** 或 **受阻**。

請參閱 [寵物](/zh-Hant/codex/pets?surface=app)，以便選擇寵物、瞭解其狀態，或
建立自己的寵物。

## 設定 Web 通知

開啟 **設定 \> 通知**，管理帳戶可用的通知類別和
管道。視通知類別與帳戶而定，
可用管道可能包括推播通知、電子郵件或簡訊。選取 **管理任務**（位於任務
通知設定中），即可開啟 **排程**。

## 設定 CLI 通知

若要設定終端和外部通知，請參閱
[通知](/zh-Hant/codex/config-file/config-advanced#notifications)；該節位於
進階設定指南中。你可以選擇 TUI 發出通知的時機，
以及 Codex 是否在回合完成時執行外部程式。

<a id="follow-task-activity-in-the-ide"></a>

## 在 IDE 中追蹤對話活動

IDE 擴充功能不提供獨立的通知控制項。請讓
對話保持開啟，以追蹤其活動。若要在回合
完成時執行外部程式，請在所連線的 Codex 主機上設定 `notify`。請參閱
[通知](/zh-Hant/codex/config-file/config-advanced#notifications)；該節位於
進階設定指南中。

## 相關文件

- [長時間執行的工作](/zh-Hant/codex/long-running-work)
- [排程任務](/zh-Hant/codex/automations)
- [寵物](/zh-Hant/codex/pets)
