<!-- source: https://learn.chatgpt.com/zh-Hant/docs/cli-customization -->

Codex CLI 提供終端專用選項，可調整互動式工作階段的
外觀，以及輸入指令和提示詞的方式。

## 語法醒目提示和主題

終端使用者介面 (TUI) 會為以圍欄標示的 Markdown 程式碼區塊和檔案
差異套用語法醒目提示。執行 `/theme` 即可開啟主題選擇器、預覽主題，並將你的
選擇儲存至 `$CODEX_HOME/config.toml` 中的 `tui.theme`。

若要新增自訂主題，請將 `.tmTheme` 檔案放入 `$CODEX_HOME/themes`，然後
從主題選擇器中選取該主題。

## Shell 自動完成

為 Bash、Z shell、Fish 或 PowerShell 產生自動完成指令碼：

```bash
codex completion zsh

請從 Shell 組態載入此指令碼。若使用 Z shell，請新增：

```bash
eval "$(codex completion zsh)"

如果 Z shell 顯示 `command not found: compdef`，請先初始化其自動完成系統，
再載入 Codex 的自動完成功能：

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

重新啟動 Shell，輸入 `codex`，然後按下 <kbd>Tab</kbd> 鍵，以確認自動完成功能是否正常運作。

## 提示詞編輯器

若提示詞較長，請在撰寫工具中按下 <kbd>Ctrl</kbd>+<kbd>G</kbd>，以開啟
由 `VISUAL` 指定的編輯器；若未設定 `VISUAL`，則改用 `EDITOR` 指定的編輯器。儲存
並關閉編輯器，讓文字回到撰寫工具後再傳送。

如需互動式鍵盤控制方式，以及完整的指令和選項清單，請參閱
[指令](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)。
