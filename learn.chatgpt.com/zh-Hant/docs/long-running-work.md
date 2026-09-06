<!-- source: https://learn.chatgpt.com/zh-Hant/docs/long-running-work -->

對於可能需要多個步驟的工作，請向 ChatGPT 明確說明預期成果、限制條件，
以及完成標準。將相關工作集中在同一個對話中，讓
ChatGPT 能運用相同的上下文決定下一步，並判斷
工作何時完成。

在 ChatGPT 桌面版應用程式中，輸入 `/goal` 以啟動目標模式。進度列
可讓你在 ChatGPT 執行工作時，暫停、恢復、編輯或清除目標。

如要在 ChatGPT Web 中執行託管的長時間工作，請使用 ChatGPT Work，並在提示詞中直接寫明
預期成果、限制條件和審查標準。

請在同一個 Web 對話中繼續補充上下文、變更限制條件，或
要求提供最新狀態。彼此獨立的任務若能
平行執行，請分別使用不同對話，並避免讓兩項任務都取得同一個已連線來源的寫入權限。
對於相關工作，請將對話和來源檔案集中在同一個
[專案](/zh-Hant/codex/projects)中。

在互動式 Codex CLI 工作階段中，輸入 `/goal` 以啟動目標模式。繼續使用
同一個工作階段，引導工作進行或要求提供最新狀態。

在 IDE 擴充功能對話中，輸入 `/goal`，即可為已開啟的
工作區啟動目標模式。請在同一個對話中持續引導執行中的任務。

  
    
  

<a id="start-a-goal"></a>
<a id="define-what-done-means"></a>
<a id="steer-a-running-goal"></a>
<a id="run-goals-in-parallel"></a>
<a id="related-docs"></a>

## 啟動目目標

在 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中輸入 `/goal`。
目標文字既是第一則提示詞，也是該
任務的完成條件。

如果預期成果仍不明確，請先使用 `/plan`。請 ChatGPT 向你提問、
找出限制條件，並將結果整理成具備可衡量成功
標準的目標。接著使用 `/goal` 啟動完善後的目標。

## 定義完成標準

撰寫能讓 ChatGPT 自行驗證進度的目標。若適用，請納入
以下三項內容：

| 目標要素     | 應納入的內容                                                               |
| ---------------- | ----------------------------------------------------------------------------- |
| **成果**      | 說明期望達成的成果，而非只列出 ChatGPT 應執行的事項。   |
| **限制條件**  | 列出必要的工具、界限、相容性需求，或應避免採用的方法。 |
| **驗證** | 加入能證明工作已完成的測試、衡量方式或審查標準。  |

例如：

```text
Migrate this codebase from JavaScript to TypeScript. Preserve existing behavior,
compile in strict mode without explicit `any` types, and make the full test suite pass.

## 引導執行中的目標

在 ChatGPT 桌面版應用程式中，目標進度列會顯示在撰寫工具上方。你可以使用該進度列
暫停或恢復工作、編輯目標，或清除目標。目標執行期間，也可以傳送後續
訊息來補充上下文或調整限制條件。

如需查看狀態摘要或取得說明，又不想中斷主要對話，請使用
側邊對話。若預期即將失去連線，請先暫停
目標；準備好讓 ChatGPT 繼續執行時，再恢復目標。

<a id="steer-a-running-task"></a>

## 引導執行中的工作

請在同一個對話中繼續補充上下文、調整限制條件，或要求
提供狀態摘要。如果另一項任務可以
獨立執行，請另開對話。

## 引導執行中的目標

在同一個互動式工作階段中傳送後續訊息，以補充上下文或
調整限制條件。如果希望 Codex 在繼續執行前彙整
目前進度，請要求提供狀態摘要。

## 引導執行中的目標

請在同一個 IDE 對話中繼續補充上下文、調整限制條件，或要求提供
狀態摘要。目標執行期間，請確保工作區維持可用。

啟動目標不會讓 ChatGPT 取得更廣泛的存取權。系統會維持原有的
[沙盒和核准政策](/zh-Hant/codex/sandboxing)，並在需要
做出決定時暫停。透過[自動核准
審查](/zh-Hant/codex/sandboxing/auto-review)，獨立的審查者可以
在不擴大原有權限範圍的情況下，評估符合條件的要求。

## 平行執行多個目標

每個對話都保有各自的上下文、訊息、結果和目標。你可以同時執行多個
對話，但應避免讓兩個對話變更相同的檔案。請使用
[工作樹](/zh-Hant/codex/environments/git-worktrees)，為平行進行程式碼編寫的對話提供獨立的
簽出目錄。

執行本機工作時，請在設定中開啟 **執行時防止睡眠** ，讓 Mac
保持喚醒。透過[寵物](/zh-Hant/codex/pets?surface=app)或[系統
通知](/zh-Hant/codex/notifications?surface=app)，即可得知對話何時需要輸入內容
或已可供審查。

## 相關文件

- [專案和對話](/zh-Hant/codex/projects)
- [目標模式與提示詞](/zh-Hant/codex/prompting#goal-mode)
- [Git 工作樹](/zh-Hant/codex/environments/git-worktrees)

## 相關文件

- [專案和對話](/zh-Hant/codex/projects)
- [排程任務](/zh-Hant/codex/automations)
- [沙盒和權限](/zh-Hant/codex/sandboxing)
