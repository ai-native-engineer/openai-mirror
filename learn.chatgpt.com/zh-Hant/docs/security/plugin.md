<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin -->

Codex Security 會掃描程式碼中的漏洞，並驗證可能成立的發現項目。針對每個可回報的問題，它會提供審查結果所需的證據與修復指引。請僅掃描您擁有或獲准評估的程式碼。

依照本快速入門安裝外掛程式，並在 Codex 中對本機程式碼庫執行標準唯讀掃描。

  本頁介紹桌面 App 或 Codex CLI 中的 Codex Security 外掛程式。若要
  在 Codex 雲端掃描已連線的 GitHub 程式碼庫，請參閱 [Codex Security 雲端服務
  設定](/zh-Hant/codex/security/setup)。

## 安裝外掛程式

1. 開啟 [ChatGPT 桌面版應用程式中的 Codex](/zh-Hant/codex/app)。
2. 開啟 **外掛程式**，搜尋 **Codex Security**，或使用下方按鈕：

   <div className="not-prose my-6">
     
       安裝 Codex Security 外掛程式
     
   </div>

3. 確認外掛程式已啟用，然後在側邊欄開啟 **安全性** 。

1. 在終端中前往您要評估的程式碼庫，然後啟動 Codex：

   ```bash
   codex

2. 輸入 `/plugins`，搜尋 **Codex Security**，然後選取 **安裝
   外掛程式**。
3. 輸入 `/new`，針對該程式碼庫開始新對話。

若要為本機程式碼庫安裝 Codex Security，請使用 ChatGPT 桌面版應用程式或 Codex CLI。

  在使用某項功能或開始長時間執行的掃描前，請先查看[外掛程式更新日誌](/zh-Hant/codex/security/plugin/changelog)。
  如果桌面 App 側邊欄未顯示 **安全性** ，
  請更新 App 和外掛程式，並確認
  外掛程式已啟用。

## 執行第一次掃描

為獲得最佳掃描品質，請使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>，
並將推理強度設為 `xhigh`。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    開始掃描前，請選擇程式碼庫並設定新的安全性掃描。
  </figcaption>
</figure>

1. 開啟掃描設定

   在側邊欄選取 **安全性** ，開啟 **掃描**，再選取 **+ 掃描**。

2. 選擇程式碼庫與掃描範圍

   選取現有程式碼庫或使用其他資料夾。選擇 **程式碼庫**，
   讓 **深度掃描** 維持關閉，並選取整個程式碼庫或單一資料夾。
   確認分支與修訂版本確實對應您要掃描的程式碼。

3. 新增相關上下文

   選擇模型與推理強度。只有在需要描述特定攻擊向量、安全性敏感區域，
   或提供可引導審查的程式碼庫詳細資訊時，
   才開啟 **額外上下文** 。

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       開啟額外上下文，以說明攻擊向量、重點區域與相關的安全性指引。
     </figcaption>
   </figure>

4. 開始掃描

   選取 **開始掃描** ，並在安全性工作台中追蹤各個掃描階段。
   選取 **檢視活動** ，以查看執行掃描的 Codex 任務。

5. 審查結果

   開啟已完成的掃描，查看發現項目、涵蓋範圍與可用的報告檔案。
   使用 **發現項目** 審查各次掃描中的問題，或使用 **程式碼庫**
   查看特定程式碼庫的掃描記錄。

   <figure className="not-prose my-6">
     
     <figcaption className="mt-3 text-sm text-secondary">
       在安全性工作台中審查掃描結果、發現項目與涵蓋範圍。
     </figcaption>
   </figure>

1. 要求執行標準掃描

   在新對話中傳送此提示詞：

   ```text
   Run a Codex Security scan on this repository.

2. 等待掃描完成

   Codex 會在終端中執行掃描，不會開啟設定工作區。請讓任務持續執行，直到 Codex 回報已完成。如果 Codex 發現組態限制，請先審查該限制與所提議的具體變更，再核准組態更新。

3. 審查結果

   先在終端中審查摘要，然後開啟產生的 `report.md`，
   查看完整結果。

請在 ChatGPT 桌面版應用程式或 Codex CLI 中執行此本機外掛程式工作流程。

## 掃描產生的內容

已完成的掃描會保留在 **掃描**中。您可以在安全性工作台審查其發現項目與
涵蓋範圍，或在 **發現項目** 和 **程式碼庫**中查看相關發現項目與程式碼庫
歷程。掃描也會建立
下列檔案。

每次掃描完成後，都會在終端中顯示摘要，並建立下列檔案。

請在 ChatGPT 桌面版應用程式或 Codex CLI 中執行此本機外掛程式工作流程。

- `report.md`，閱讀掃描結果的主要入口。
- `findings/<slug>/`，若有詳細漏洞報告及佐證用的
  概念驗證檔案，便會建立此目錄。
- `hardening/`，若有結構性強化指引及相關提案或
  圖表，便會建立此目錄。
- 供自動化與整合使用的結構化掃描資料，儲存在 `scan-manifest.json`、`findings.json` 和
`coverage.json` 中。您不必開啟這些檔案，
  也能審查掃描結果。

分享或封存結果時，請一併保留完整掃描目錄，
讓 `report.md` 中的連結繼續正常運作。

## 選擇接下來的工作流程

- [使用安全性工作台](/zh-Hant/codex/security/plugin/workbench)，在桌面 App 中管理
  已儲存的掃描、發現項目、程式碼庫與掃描活動。
- 若您具備 Beta 版存取權，且
  需要可重複執行並提供結構化結果的終端工作流程，請[從 CLI 執行掃描](/zh-Hant/codex/security/cli)。
- [執行標準或限定範圍的掃描](/zh-Hant/codex/security/plugin/scans)，以預設工作流程審查
  程式碼庫或單一資料夾。
- [評估第一次掃描](/zh-Hant/codex/security/plugin/scans#assess-a-first-scan)，
  將結果與已知問題比對，並決定何時再次掃描。
- 如果能接受較長的執行時間，請[執行深度掃描](/zh-Hant/codex/security/plugin/deep-scans)，
  以進行更徹底的掃描。
- [審查程式碼變更](/zh-Hant/codex/security/plugin/code-changes)，以評估
  Pull Request、提交、分支範圍或工作樹修補內容。
- [對待辦清單進行分級處理](/zh-Hant/codex/security/plugin/triage-backlog)，以審查現有的
  安全性發現項目。
- 在您接受一個發現項目並決定進行修復後，
  請[修正並驗證該發現項目](/zh-Hant/codex/security/plugin/fix-findings)。
- [匯出或追蹤發現項目](/zh-Hant/codex/security/plugin/export-findings)，以產生
  JSON、CSV 或 SARIF，或建立需經核准的 Linear、GitHub 或 Jira 議題，或非公開的
  GitHub Security Advisory 草稿。
- [撰寫漏洞報告](/zh-Hant/codex/security/plugin/vulnerability-reports)，
  將提供的發現項目、揭露說明、原始碼與 PoCs 整理成
  內容完整且可獨立閱讀的報告。
- [提出安全性強化方案](/zh-Hant/codex/security/plugin/security-hardening)，
  根據掃描結果或其他
  安全性證據，評估結構或架構方面的方案。
