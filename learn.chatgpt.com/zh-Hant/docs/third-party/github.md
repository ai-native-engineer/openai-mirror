<!-- source: https://learn.chatgpt.com/zh-Hant/docs/third-party/github -->

使用 Codex 程式碼審查，為 GitHub Pull Request 增加一輪能有效找出關鍵問題的審查。
Codex 會審查 Pull Request 的差異，遵循程式碼庫指引，
並發布著重重大問題的標準 GitHub 程式碼審查結果。
目前以研究預覽版提供的安全性審查，會更深入地檢查 Pull Request 中
可能存在的安全性問題。

<br />

## 開始之前

請確認符合以下條件：

- 已為你要審查的程式碼庫設定 [Codex 雲端](/zh-Hant/codex/cloud)。
- 具備 [Codex 程式碼審查設定](https://chatgpt.com/codex/settings/code-review) 的存取權。
- 若要讓 Codex 遵循程式碼庫專屬的審查指引，請準備 `AGENTS.md` 檔案。

## 設定 Codex 程式碼審查

若要設定自動審查，你需要已連線的 GitHub 程式碼庫，並具備設定該程式碼庫所需的
GitHub 推送或管理員權限。

1. 設定 [Codex 雲端](/zh-Hant/codex/cloud)。
2. 前往 [Codex 設定](https://chatgpt.com/codex/settings/code-review)。
3. 為你的程式碼庫開啟 **程式碼審查** 。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 要求 Codex 審查

1. 在 Pull Request 留言中提及 `@codex review`。
2. 等待 Codex 做出回應（👀）並發布審查結果。

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex 會像團隊成員一樣，在 Pull Request 上發布審查結果。在 GitHub 中，
Codex 只會標記 P0 和 P1 問題，讓審查留言聚焦於
高優先順序的風險。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 啟用自動審查

若要讓 Codex 自動審查每個 Pull Request，請開啟
**自動審查** ；此選項位於 [Codex 設定](https://chatgpt.com/codex/settings/code-review)。
每當有人開啟新的 PR 以供審查時，Codex 都會發布審查結果，且
不需要 `@codex review` 留言。

## 自訂 Codex 審查的內容

Codex 會在程式碼庫中搜尋 `AGENTS.md` 檔案，並遵循適用的
程式碼審查規則。請將 `## Code Review Rules` 區段加入最接近
規則所適用程式碼的檔案。必要時，使用 `###` 標題將相關檢查
分組。

例如，實驗報告服務可防止曝光後的行為
改變比較群組：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

將適用於整個程式碼庫的規則放在根目錄的 `AGENTS.md` 中，服務專屬規則則
放在巢狀檔案中，例如 `services/experiment_reporting/AGENTS.md`。Codex
會對每個變更的檔案套用根目錄指引與涵蓋該檔案的更具體指引，因此
不相關的變更無須帶入服務專屬的上下文。

先從兩到三條簡潔規則開始，將審查者經常需要說明的檢查項目明文化。實用的規則包括：

- **聚焦於影響重大且為程式碼庫特有的行為。** 說明應標記的
  相容性限制、資料邊界或不安全副作用，以及
  這些問題為何重要。
- **說明安全的處理方式或例外情況。** 提供 Codex 足夠的上下文，以便區分
  真正的問題與預期行為。
- **讓規則的適用範圍明確且能長期有效。** 應著重於結果，而非可能變更的函式名稱，
  並將指引放在所規範的程式碼附近。
- **將制式檢查留給 CI。** 不要將格式檢查、lint 與其他
  確定性檢查納入審查規則。

開啟具代表性的 Pull Request，並使用 `@codex review` 要求審查。
根據審查結果和回饋調整規則，並縮小會產生雜訊的指引範圍，或
將其移除。

程式碼審查規則可引導 Codex，但不能取代測試、分支保護或
必要的核准。

若要指定單次審查的重點，請將其加入 Pull Request 留言：

`@codex review for issues in the database migration`

## 安全性審查

安全性審查是一項額外的審查，適合希望
特別關注 Pull Request 安全性問題的客戶。針對特定的安全性風險，
它會分析 Pull Request 差異、相關的程式碼庫上下文，
以及已設定的威脅模型或安全性指引，
提供比程式碼審查更深入的檢查。

程式碼審查在一般審查過程中也能找出與安全性相關的問題，
因此程式碼審查與安全性審查所發現的問題
偶爾可能重疊。

### 設定安全性審查

如需更詳細的設定說明和組態選項，請參閱 [安全性
審查](/zh-Hant/codex/security/security-review)。

1. 設定 [Codex 雲端](/zh-Hant/codex/cloud)。
2. 前往 [Codex 設定](https://chatgpt.com/codex/settings/code-review)。
3. 在 **程式碼庫偏好設定** 中，選擇哪些 Pull Request 要接受安全性
   審查，以及執行時機。選取 **每當程式碼審查執行時** ，即可讓它
   與程式碼審查一併執行。

### 要求安全性審查

若要手動要求安全性審查，請在 Pull Request 中加入以下留言：

`@codex security review`

審查執行期間，Codex 會做出回應，接著直接
在 Pull Request 上發布發現的安全性問題。開啟相關的 Codex 任務，然後選取 **安全性
報告** 分頁，即可查看完整報告。

## 處理審查結果

Codex 發布審查結果後，你可以再留一則留言，
要求它修正同一個 Pull Request 中的問題：

```md
@codex fix the P1 issue

Codex 會以該 Pull Request 作為上下文開始雲端對話；具備權限時，
也能將修正推送回分支。

## 交辦其他任務給 Codex

如果你在留言中提及 `@codex`，並輸入 `review` 以外的內容，Codex 便會以你的 Pull Request 作為上下文，開始 [雲端對話](/zh-Hant/codex/cloud)。

```md
@codex fix the CI failures

## 排解程式碼審查問題

如果 Codex 沒有做出回應或發布審查結果：

- 確認你已為該程式碼庫開啟 **程式碼審查** ；此選項位於 [Codex 設定](https://chatgpt.com/codex/settings/code-review)。
- 確認該 Pull Request 所屬的程式碼庫已設定 [Codex 雲端](/zh-Hant/codex/cloud)。
- 在 Pull Request 留言中使用完全相符的觸發指令 `@codex review`。
- 若為自動審查，請確認已開啟 **自動審查** ，且
  Pull Request 事件符合你的審查觸發設定。
