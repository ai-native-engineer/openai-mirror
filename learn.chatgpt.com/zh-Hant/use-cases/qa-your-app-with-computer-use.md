<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/qa-your-app-with-computer-use -->

## 簡介

電腦很適合用於品質測試，因為它能查看介面、逐步操作流程、在欄位中輸入內容，並記錄失敗之處。因此，它有助於在貼近實際情境的使用者歷程中找出功能性錯誤與 UI 問題。

關鍵在於告訴 Codex 要測試哪個環境、哪些流程最重要，以及希望收到哪一類報告。

## 使用方式

1. 安裝 [電腦外掛程式](/zh-Hant/codex/computer-use)。
2. 告訴 Codex 要測試哪個 App、組建版本或環境。
3. 列出你最重視的流程或核心使用案例。
4. 要求提供結構化報告，讓輸出結果便於進行問題分流或交接。

你可以採用較概略的說法：

- `@Computer Test my app. Find any major issues and give me a report.`

也可以寫得更明確：

- `@Computer Test my app in staging. Cover signup, invite a teammate, and upgrade billing. Log every bug with repro steps, expected result, actual result, and severity.`

如果你已在程式碼庫中維護測試計畫檔案，請將它附加至對話，或告訴 Codex 該檔案的位置，讓品質測試遵循你既有的流程。

## 實用技巧

### 清楚說明設定

如果帳戶狀態、測試資料、功能旗標或環境選擇會影響流程，請一開始就說明這些資訊。當 Codex 知道測試的是本機環境、預備環境，還是近似正式環境的行為時，結果會好得多。

### 列出你關注的問題類型

請說明你希望 Codex 著重檢查功能失效、版面配置問題、令人困惑的文案、視覺迴歸，還是上述所有項目。

### 決定要停止還是繼續

如果只要出現一個阻斷性問題就應結束本次執行，請明確說明。否則，請 Codex 繼續走完其餘流程，收集所有非阻斷性問題後再彙整。

## 後續建議

完成品質測試後，繼續使用同一個對話，並請 Codex 修正它找到的其中一個錯誤、將發現事項整理成可直接用於 Linear 或 GitHub 的草稿，或讓下一輪測試只聚焦於某個特定的失敗流程。

## 建議提示詞

**執行結構化品質測試**
