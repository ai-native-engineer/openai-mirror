<!-- source: https://learn.chatgpt.com/zh-Hant/docs/integrated-terminal -->

ChatGPT 桌面版應用程式中的每個對話都包含一個终端，其範圍限定於目前的專案或
工作樹。請按一下應用程式右上角的終端圖示，或
按下 <kbd>Ctrl</kbd>+<kbd>\`</kbd>，即可開啟。

  
    
  

## 執行並驗證專案

無須切換應用程式，即可使用終端驗證變更、執行指令碼，並進行 Git 操作。ChatGPT 可以讀取目前的終端輸出，因此與你協作時，能檢查執行中的開發伺服器，或參考建置失敗的結果。

常用指令包括：

- `git status`
- `git pull --rebase`
- `pnpm test` 或 `npm test`
- `pnpm run lint` 或其他專案專屬的檢查

## 建立可重複使用的動作

如果你經常執行某項指令，請在[本機環境](/zh-Hant/codex/environments/local-environment#actions)中定義一個動作。
動作會在 ChatGPT 桌面版應用程式中顯示為捷徑，並於整合式
終端執行。

<kbd>Cmd</kbd>+<kbd>K</kbd> 可開啟應用程式的指令選擇區，但不會清除
終端。若要清除終端，請按下 <kbd>Ctrl</kbd>+<kbd>L</kbd>。
