<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/threat-model -->

瞭解什麼是威脅模型，以及編輯威脅模型能如何改善 Codex Security 的建議。

## 什麼是威脅模型

威脅模型是一份簡短的安全性摘要，說明程式碼庫如何運作。在 Codex Security 中，你會將它編輯為 `project overview`，系統則會在後續掃描、排定優先順序和審查時，將它用作掃描上下文。

Codex Security 會根據程式碼建立初稿。若發現項目看起來不太準確，首先應編輯的就是威脅模型。

實用的威脅模型會明確列出：

- 進入點和不受信任的輸入
- 信任邊界和身分驗證假設
- 敏感資料路徑或具特殊權限的操作
- 團隊希望優先審查的範圍

例如：

> 用於帳戶變更的公開 API。接受 JSON 請求和檔案上傳。使用內部驗證服務進行身分檢查，並透過內部服務寫入計費變更。審查時應著重於身分驗證檢查、上傳內容剖析，以及服務之間的信任邊界。

這可讓 Codex Security 在執行後續掃描及排定發現項目優先順序時，有更好的起點。

## 改善並重新檢視威脅模型

若想改善結果，請先編輯威脅模型。當發現項目未涵蓋你關注的範圍，或出現在非預期的位置時，請調整威脅模型。威脅模型會改變後續掃描所使用的上下文。

  有些使用者會將目前的威脅模型複製到 Codex，並透過對話加以改善，
以他們希望更仔細審查的範圍為依據，然後將更新後的
版本貼回 Web UI。

### 編輯位置

若要審查或更新威脅模型，請前往 [Codex Security 掃描](https://chatgpt.com/codex/security/scans)，開啟程式碼庫，然後按一下 **編輯**。

## 相關文件

- [Codex Security 雲端服務設定](/zh-Hant/codex/security/setup) 涵蓋程式碼庫設定及發現項目審查。
- [Codex Security](/zh-Hant/codex/security) 提供產品概覽。
- [Codex Security 雲端常見問題](/zh-Hant/codex/security/faq) 解答常見的雲端問題。
