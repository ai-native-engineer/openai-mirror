<!-- source: https://learn.chatgpt.com/zh-Hant/use-cases/deep-security-scan -->

## 選擇深入的程式碼庫審查

當您需要對程式碼庫或明確指定的資料夾進行更全面的
弱點審查，並能預留較長的執行時間時，請使用深度掃描。Codex Security
外掛程式會反覆執行探索，再驗證發現項目並排定
優先順序，因此此工作流程比一般掃描需要更多時間和資源。

深度掃描可以審查整個程式碼庫，也可以審查一個明確指定的套件或
目錄。若要審查 Pull Request、提交、分支差異或工作樹修補程式，
請使用
[$codex-security:security-diff-scan](/zh-Hant/codex/use-cases/scan-code-changes-for-security)。

## 準備經授權的掃描

1. 在 Codex 中開啟程式碼庫，並完成 [Codex Security 外掛程式快速入門](/zh-Hant/codex/security/plugin)。
2. 確認您擁有該程式碼庫，或已獲授權對其進行評估。
3. 將架構、信任邊界、安全性不變條件、發現項目判定準則、
   排除項目和嚴重性等方面的指引加入 `SECURITY.md`。若政策僅適用於特定目錄，請使用巢狀的 `SECURITY.md`
   檔案。
4. 將支援的建置、測試和驗證指令，以及其他程式碼庫
   操作說明保留在 `AGENTS.md` 中。
5. 執行起始提示詞，讓掃描完成反覆探索、
驗證、攻擊路徑分析和最終報告等階段。
6. 審查發現項目工作區、報告及任何證據缺口。有需要時，請要求提供詳細的
弱點報告或結構性強化指引。

## 修復前先審查證據

最終結果應指出受影響的位置、該行為為何可觸發、
Codex 執行了哪些驗證、任何剩餘的證據缺口，以及
範圍明確的修復方向。請區分沒有驗證證據的發現項目
與已驗證的發現項目。

只有在您選定並審查某個發現項目後，才開始修復。請使用
[修復弱點待辦清單](/zh-Hant/codex/use-cases/remediate-vulnerability-backlog)
，透過針對性的迴歸驗證逐一修復發現項目。

如需設定、執行前檢查、限定範圍的目標和預期執行時間，請參閱 [執行深度
安全性掃描](/zh-Hant/codex/security/plugin/deep-scans)。
