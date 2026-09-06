<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/setup -->

本頁將引導你使用 Codex Security 雲端服務，從取得初始存取權到審查發現項目，並建立修正用
Pull Request。

  請先確認已完成 Codex 雲端設定。若尚未設定，請參閱 [Codex
  雲端](/zh-Hant/codex/cloud) 以開始使用。

## 1. 存取權與環境

Codex Security 雲端服務會掃描已透過
[Codex 雲端](/zh-Hant/codex/cloud) 連線的 GitHub 程式碼庫。

- 請確認你的工作區可存取 Codex Security 雲端服務。
- 請確認要掃描的程式碼庫已可在 Codex 雲端中使用。

前往 [Codex 環境](https://chatgpt.com/codex/settings/environments)，檢查該程式碼庫是否已有環境。若沒有，請先在該處建立環境再繼續。

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 2. 新增安全性掃描

環境建立後，前往 [建立安全性掃描](https://chatgpt.com/codex/security/scans/new)，然後選擇剛才連線的程式碼庫。

Codex Security 會先從最新的提交開始，往回掃描程式碼庫，藉此建立掃描上下文，並在有新提交時更新該上下文。

若要設定程式碼庫：

1. 選取 GitHub 組織。
2. 選取程式碼庫。
3. 選取要掃描的分支。
4. 選取環境。
5. 選擇 **歷史記錄範圍**。範圍越長，可提供的上下文越多，但回溯掃描所需時間也越長。
6. 按一下 **建立**。

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

## 3. 初始掃描可能需要一段時間

建立掃描後，Codex Security 會先在所選的歷史記錄範圍內執行提交層級的安全性掃描。
初始回溯掃描可能需要數小時，程式碼庫較大或歷史記錄範圍較長時尤其如此。
如果沒有立即顯示發現項目，這是正常現象。請先等待初始掃描完成，再建立問題單或進行疑難排解。

  系統會自動且完整地設定初始掃描，這可能需要數小時。
如果第一批發現項目延遲出現，不必擔心。

## 4. 審查掃描並改善威脅模型

<div class="not-prose my-8 max-w-6xl overflow-hidden rounded-xl border border-subtle bg-surface">
  
    
      
    
  
</div>

初始掃描完成後，開啟該掃描並審查系統產生的威脅模型。
初始發現項目出現後，更新威脅模型，使其符合你的架構、信任邊界及業務上下文。
這有助於 Codex Security 為團隊判定問題的優先順序。

  如果想改變掃描結果，可以編輯威脅模型，納入更新後的
範圍、優先順序及假設。

初始發現項目出現後，請重新檢視模型，讓掃描指引與目前的優先事項保持一致。
持續更新模型有助於 Codex Security 提供更好的建議。

如需深入瞭解威脅模型及其對嚴重程度判定與分流處理的影響，請參閱 [改善威脅模型](/zh-Hant/codex/security/threat-model)。

## 5. 審查發現項目並進行修補

初始回溯掃描完成後，請在 **發現項目** 檢視畫面中審查發現項目。

你可以使用兩種檢視畫面：

- **建議的發現項目**：持續更新的清單，列出程式碼庫中最嚴重的 10 個問題
- **所有發現項目**：可排序及篩選的表格，列出整個程式碼庫的發現項目

  
    
  

按一下發現項目即可開啟其詳細資料頁面，其中包含：

- 問題的簡要說明
- 重要中繼資料，例如提交詳細資訊和檔案路徑
- 結合上下文對影響進行推理
- 相關程式碼片段
- 呼叫路徑或資料流上下文（如有）
- 驗證步驟及驗證輸出

你可以審查每個發現項目，並直接從發現項目詳細資料頁面建立 PR。

## 相關文件

- [Codex Security](/zh-Hant/codex/security) 提供產品概覽。
- [Codex Security 雲端服務常見問題](/zh-Hant/codex/security/faq) 涵蓋常見的雲端服務問題。
- [改善威脅模型](/zh-Hant/codex/security/threat-model) 說明如何改善掃描上下文及發現項目優先順序的判定方式。
