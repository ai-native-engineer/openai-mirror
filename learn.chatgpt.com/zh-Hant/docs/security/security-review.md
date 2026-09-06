<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/security-review -->

Codex Security 審查目前以研究預覽版形式提供。
ChatGPT Enterprise、Business、Edu 和 Pro 客戶均可使用；
Plus 客戶無法使用。推出初期，Codex Security 審查不會
消耗 ChatGPT 點數。可能會有用量限制。

Codex Security 審查是一項額外審查，適合希望
特別關注 Pull Request 中安全性問題的客戶。

Codex Security 審查對特定安全性風險的分析比 [程式碼
審查](/zh-Hant/codex/third-party/github) 更深入，涵蓋
Pull Request 差異、相關的程式碼庫上下文，以及已設定的威脅模型
或安全性指引。程式碼審查在一般審查中也可能找出安全性相關問題，
因此發現項目偶爾可能重疊。

## 開始之前

若要設定自動 Codex Security 審查，您需要：

- 您的工作區具備 Codex Security 審查研究預覽版存取權
- [Codex 雲端](/zh-Hant/codex/cloud) 已設定完成，並連接 GitHub 程式碼庫
- 程式碼庫設定所需的 GitHub 推送或管理員權限

現有的 Codex Security 掃描並非必要。

<a id="configure-security-review"></a>

## 設定 Codex Security 審查

1. 前往 [Codex 設定](https://chatgpt.com/codex/settings/code-review)。
2. 在 **程式碼庫偏好設定** 下，選擇哪些 Pull Request 要接受 Codex
   Security 審查：
   - **依個人設定** 可讓每位貢獻者透過其個人
     Codex Security 審查設定自行選擇啟用。
   - **審查所有 PR** 適用於程式碼庫中的每個 Pull Request。
   - **審查團隊 PR**（若有此選項）適用於由
     您的 ChatGPT 工作區成員開啟的 Pull Request，而非由 GitHub 團隊成員開啟的 Pull Request。
3. 選擇 Codex Security 審查的執行時機：
   - **PR 開啟時** 會在 Pull Request 開啟時獨立執行。
   - **每次推送** 會在推送新的提交後獨立執行。
   - **每當程式碼審查執行時** 需要啟用程式碼審查，並會同時執行 Codex Security
     審查。

## 新增威脅模型上下文

您可以設定威脅模型，讓 Codex 取得有關應用程式的
資產、信任邊界、安全性假設，以及程式碼庫特有風險的上下文。
如果程式碼庫已有 Codex Security 掃描組態，您可以使用
其中的威脅模型。否則，請提供已提交
至程式碼庫的威脅模型檔案路徑。如果未指定來源，Codex 會在每次審查時重新產生
威脅模型。

## 設定回報門檻

預設情況下，自動 Codex Security 審查會回報嚴重性為 **高** 和 **重大**
的發現項目，而手動要求的審查會回報嚴重性為 **中**、**高** 和
**重大** 的發現項目。您可以分別變更
自動與手動審查的最低嚴重性等級，並新增依路徑設定的覆寫規則。

發布至 Pull Request 的發現項目會沿用該 Pull Request 的 GitHub
可見性。任何能查看該 Pull Request 的人都能查看這些發現項目，
這也適用於公開程式碼庫，或由您工作區外部
貢獻者開啟的 Pull Request。對於 Pull Request 留言可能廣泛可見的程式碼庫，
請謹慎選擇回報門檻。回報門檻會控制
Codex 發布至 GitHub 的內容；完整的 Codex Security 審查報告仍會保留在
Codex 中。

<a id="request-a-security-review"></a>

## 要求進行 Codex Security 審查

若要手動要求 Codex Security 審查，請在 Pull Request 中新增以下留言：

`@codex security review`

Codex 會在審查執行期間對該留言做出回應，接著將符合您的
手動回報門檻的發現項目直接發布至 Pull Request。開啟相關的
Codex 任務並選取 **安全性報告** 分頁，即可查看完整報告，
其中包括嚴重性、攻擊路徑、佐證資料、驗證和
修復指引。若沒有任何問題符合回報門檻，Codex 不會
將發現項目發布至 Pull Request。

## 相關文件

- [使用 Codex 審查 GitHub Pull Request](/zh-Hant/codex/third-party/github) 說明程式碼審查及 GitHub 整合功能。
- [Codex Security](/zh-Hant/codex/security) 提供產品概覽。
- [Codex Security 雲端服務設定](/zh-Hant/codex/security/setup) 說明程式碼庫掃描與發現項目審查。
- [改善威脅模型](/zh-Hant/codex/security/threat-model) 說明如何調整程式碼庫上下文。
