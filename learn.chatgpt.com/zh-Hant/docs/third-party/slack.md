<!-- source: https://learn.chatgpt.com/zh-Hant/docs/third-party/slack -->

在 Slack 中使用 Codex，即可從頻道和討論串啟動程式碼編寫工作。提及 `@Codex` 並附上提示詞，Codex 便會建立雲端對話並回覆結果。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## 設定 Slack 應用程式

1. 設定 [Codex 雲端對話](/zh-Hant/codex/cloud)。您需要 Plus、Pro、Business、Enterprise 或 Edu 方案（請參閱 [ChatGPT 定價](https://chatgpt.com/pricing)）、已連結的 GitHub 帳戶，以及至少一個 [環境](/zh-Hant/codex/environments/cloud-environment)。
2. 前往 [Codex 設定](https://chatgpt.com/codex/settings/connectors)，並將 Slack 應用程式安裝到您的工作區。視 Slack 工作區政策而定，可能需要管理員核准安裝。
3. 將 `@Codex` 加入頻道。如果尚未加入，您提及它時 Slack 會顯示提示。

<a id="start-a-task"></a>

## 開始對話

1. 在頻道或討論串中提及 `@Codex`，並附上您的提示詞。Codex 可以參考討論串中的先前訊息，因此通常不必重述上下文。
2. （選用）請在提示詞中指定環境或程式碼庫，例如：`@Codex fix the above in openai/codex`。
3. 等待 Codex 加上表情符號回應（👀），並回覆對話連結。完成後，Codex 會發布結果，並視您的設定在討論串中發布答案。

### Codex 如何選擇環境和程式碼庫

- Codex 會檢視您可存取的環境，並選擇最符合您要求的環境。如果要求不夠明確，就會改用您最近使用的環境。
- 對話會在該環境程式碼庫對應表所列的第一個程式碼庫之預設分支上執行。若要變更預設程式碼庫或加入更多程式碼庫，請在 Codex 中更新程式碼庫對應表。
- 如果沒有可用的合適環境或程式碼庫，Codex 會在 Slack 中回覆操作指示，說明如何修正問題後再重試。

### 企業資料控管

在預設情況下，Codex 會在討論串中回覆答案，該答案可能包含其執行環境中的資訊。
若要避免這種情況，企業管理員可取消勾選 **允許 Codex Slack 應用程式在任務完成時發布答案** 選項；此選項位於 [ChatGPT 工作區設定](https://chatgpt.com/admin/settings)。管理員關閉發布答案功能後，Codex 只會回覆對話連結。

### 資料使用、隱私權與安全性

當您提及 `@Codex` 時，Codex 會接收您的訊息和討論串記錄，以瞭解您的要求並建立對話。
資料處理方式遵循 OpenAI 的 [隱私權政策](https://openai.com/privacy)、[使用條款](https://openai.com/terms/)及其他適用的 [政策](https://openai.com/policies)。
如需進一步瞭解安全性，請參閱 Codex [安全性文件](/zh-Hant/codex/agent-approvals-security)。

Codex 使用的大型語言模型可能會出錯。請務必審查答案和差異內容。

### 提示與疑難排解

- **缺少連線**：如果 Codex 無法確認您的 Slack 或 GitHub 連線，就會回覆重新連線的連結。
- **環境選擇不如預期**：請在討論串中回覆，說明您想使用的環境（例如 `Please run this in openai/openai (applied)`），然後再次提及 `@Codex`。
- **冗長或複雜的討論串**：請在最新訊息中彙整重要細節，以免 Codex 遺漏討論串較早訊息中的上下文。
- **工作區發布**：部分企業工作區限制發布最終答案。在這種情況下，請開啟對話連結以查看進度和結果。
- **取得更多協助**：請參閱 [OpenAI 說明中心](https://help.openai.com/)。
