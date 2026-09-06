<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security -->

Codex Security 是一款應用程式安全性智慧體，可協助安全性與
工程團隊找出、確認並修復漏洞。您可以在
Codex 中、從終端、透過 TypeScript SDK，或搭配已連線的 GitHub
程式碼庫使用它。

如要依照明確步驟執行第一次本機掃描，請先參閱 [Codex Security 外掛程式
快速入門](/zh-Hant/codex/security/plugin)。

## 在桌面 App 中使用 Codex Security

在 ChatGPT 桌面版應用程式中，開啟 ChatGPT 下拉式選單，並選取 **Codex**。
安裝並啟用 Codex Security 外掛程式，即可在側邊欄開啟 **安全性** 。
安全性工作台會集中管理您的掃描、發現項目與程式碼庫，
每次掃描則由 Codex 在個別任務中執行。

- 使用 **掃描** 啟動掃描、追蹤進度，並審查已儲存的結果。
- 使用 **發現項目** 檢查各次已完成掃描中的問題與證據。
- 使用 **程式碼庫** 審查程式碼庫歷程與尚未結案的發現項目。

請參閱 [使用安全性工作台](/zh-Hant/codex/security/plugin/workbench)，瞭解
桌面 App 的完整工作流程。

### 探索外掛程式使用案例

- [執行安全性掃描](/zh-Hant/codex/security/plugin/scans)，掃描程式碼庫或指定範圍的單一資料夾。
- [執行深度安全性掃描](/zh-Hant/codex/security/plugin/deep-scans)，適用於需要更廣泛的審查，且可以等待較長時間讓掃描完成的情況。
- 在合併 Pull Request 或分支前，[審查程式碼變更](/zh-Hant/codex/security/plugin/code-changes)。
- 需要審查現有安全性發現項目時，請[對待辦清單進行分級處理](/zh-Hant/codex/security/plugin/triage-backlog)。
- [修復並驗證發現項目](/zh-Hant/codex/security/plugin/fix-findings)，針對已核准的發現項目套用範圍受限的修補程式。
- [匯出或追蹤發現項目](/zh-Hant/codex/security/plugin/export-findings)，將其輸出為可攜式成品，或傳送至需經核准的追蹤目的地。
- 根據提供的發現項目、揭露說明、原始碼與 PoCs，[撰寫漏洞報告](/zh-Hant/codex/security/plugin/vulnerability-reports)。
- 根據掃描結果或其他安全性證據，[提出安全性強化方案](/zh-Hant/codex/security/plugin/security-hardening)。
- [查看最新消息](/zh-Hant/codex/security/plugin/changelog)，瞭解 Codex Security 外掛程式的更新內容。

  桌面 App 的安全性工作台與 Codex CLI 使用 Codex Security 外掛程式。
  Codex Security 雲端服務會透過 Codex 雲端掃描已連線的 GitHub 程式碼庫。
  如需瞭解 Codex 的沙盒、核准、網路控制措施及管理員設定，請參閱
[代理核准與安全性](/zh-Hant/codex/agent-approvals-security)。

## Codex Security CLI 與 SDK

CLI 與 TypeScript SDK 以公開的
[`@openai/codex-security`](https://github.com/openai/codex-security) 套件形式提供。
使用 `npx` 執行 CLI：

```bash
npx @openai/codex-security --help

執行掃描需要 Codex Security 的存取權。為獲得最佳結果，請使用已通過
[Trusted Access for Cyber](https://chatgpt.com/cyber) 驗證的帳戶。

跨不同程式碼庫持續使用與外掛程式相同的掃描器。CLI
會探索 GitHub 程式碼庫、接續執行大量掃描、跨多次掃描追蹤發現項目，
並記錄誤報回饋。您可以加入架構與安全性
政策、設定預估成本上限，或在 CI 中及提交前執行檢查。
使用 TypeScript SDK，將掃描、進度報告及成本控管功能
整合至應用程式或開發工具中。

- [從 CLI 快速入門開始](/zh-Hant/codex/security/cli)，以設定 CLI、
  對程式碼庫執行預檢，並執行本機掃描。
- [執行大量安全性掃描](/zh-Hant/codex/security/cli/bulk-scans)，以探索 GitHub
  程式碼庫，或根據 CSV 清冊執行可接續的掃描活動。
- [在 CI 中執行掃描](/zh-Hant/codex/security/cli/ci)，以審查 Pull Request 的變更、
  保留成品、上傳 SARIF，以及設定嚴重性政策。
- [閱讀 CLI 常見問題](/zh-Hant/codex/security/cli/faq)，查詢掃描歷程、
  誤報回饋、涵蓋範圍與修復驗證等問題的解答。
- [參閱 CLI 參考資料](/zh-Hant/codex/security/cli/reference)，查看支援的
  指令、旗標、輸出格式、成品與結束代碼。
- [整合 TypeScript SDK](/zh-Hant/codex/security/sdk)，即可透過程式碼選取目標、
  檢查結果、追蹤進度並取消掃描。

## Codex Security 雲端服務

Codex Security 雲端服務目前處於研究預覽階段。它會掃描已連線的
GitHub 程式碼庫，找出可能的安全性問題。

它可協助團隊：

1. **找出可能的漏洞** ：運用程式碼庫專屬的威脅模型與實際程式碼上下文。
2. **降低雜訊** ：先驗證發現項目，再進行審查。
3. **推進發現項目的修復流程** ：提供排序後的結果、證據與建議的修補選項。

## Codex Security 雲端服務的運作方式

Codex Security 會依序掃描已連線程式碼庫中的每次提交。
它會根據您的程式碼庫建立掃描上下文、依據該上下文檢查可能的漏洞，並先在隔離環境中驗證可信度高的問題，再顯示這些問題。

您會獲得一套著重以下項目的工作流程：

- 程式碼庫專屬的上下文，而非通用特徵碼
- 有助於減少誤報的驗證證據
- 可在 GitHub 上審查的建議修復方案

## Codex Security 雲端服務的存取權與先決條件

Codex Security 雲端服務會透過 Codex 雲端，與已連線的 GitHub 程式碼庫搭配運作。
如果看不到某個程式碼庫，請確認該程式碼庫是否可在您的 Codex 雲端工作區中使用，
或聯絡您的 OpenAI 客戶團隊。

## 相關文件

- [Codex Security 外掛程式快速入門](/zh-Hant/codex/security/plugin) 逐步說明安裝程序與第一次本機掃描。
- [安全性工作台](/zh-Hant/codex/security/plugin/workbench) 說明桌面 App 中已儲存的掃描、發現項目、程式碼庫與掃描活動。
- [Codex Security CLI 快速入門](/zh-Hant/codex/security/cli) 逐步說明設定、預檢，以及首次在終端執行掃描的方式。
- [執行大量安全性掃描](/zh-Hant/codex/security/cli/bulk-scans) 說明如何探索 GitHub 程式碼庫、使用 CSV 清冊、查看掃描活動結果，以及接續執行掃描。
- [Codex Security CLI 常見問題](/zh-Hant/codex/security/cli/faq) 解答關於掃描、發現項目、涵蓋範圍與成本的常見問題。
- [Codex Security TypeScript SDK](/zh-Hant/codex/security/sdk) 說明如何從應用程式或開發工具執行掃描。
- [Codex Security 雲端服務設定](/zh-Hant/codex/security/setup) 詳細說明設定、掃描，以及發現項目的審查方式。
- [安全性審查](/zh-Hant/codex/security/security-review) 說明如何針對 GitHub Pull Request 執行深入的安全性審查。
- [改善威脅模型](/zh-Hant/codex/security/threat-model) 說明如何調整範圍、進入點與關鍵性假設。
- [Codex Security 雲端服務常見問題](/zh-Hant/codex/security/faq) 涵蓋雲端產品的常見問題。
