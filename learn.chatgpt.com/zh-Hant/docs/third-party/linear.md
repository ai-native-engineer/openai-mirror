<!-- source: https://learn.chatgpt.com/zh-Hant/docs/third-party/linear -->

在 Linear 中使用 Codex，即可透過議題委派工作。將議題指派給 Codex，或在留言中提及 `@Codex`，Codex 就會建立雲端對話，並回報進度與結果。

Linear 中的 Codex 適用於付費方案（請參閱 [定價](/zh-Hant/codex/pricing)）。

如果您使用企業方案，請要求 ChatGPT 工作區管理員在 [工作區設定](https://chatgpt.com/admin/settings) 中啟用 Codex 雲端對話，並在 [連接器設定](https://chatgpt.com/admin/ca) 中啟用 **Codex for Linear** 。

## 設定 Linear 整合功能

1. 若要設定 [Codex 雲端對話](/zh-Hant/codex/cloud)，請在 [Codex](https://chatgpt.com/codex) 中連接 GitHub，並為您希望 Codex 使用的程式碼庫建立 [環境](/zh-Hant/codex/environments/cloud-environment)。
2. 前往 [Codex 設定](https://chatgpt.com/codex/settings/connectors)，為您的工作區安裝 **Codex for Linear** 。
3. 在 Linear 議題的留言串中提及 `@Codex`，即可連結您的 Linear 帳戶。

## 將工作委派給 Codex

您可以透過以下兩種方式委派工作：

### 將議題指派給 Codex

安裝整合功能後，您可以像指派給團隊成員一樣，將議題指派給 Codex。Codex 會開始處理工作，並在議題中發布進度更新。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### 在留言中提及 `@Codex`

您也可以在留言串中提及 `@Codex`，以委派工作或提出問題。Codex 回覆後，請在同一留言串中接續回覆，以繼續同一段對話。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Codex 開始處理議題後，會 [選擇作業環境和程式碼庫](#how-codex-chooses-an-environment-and-repo)。
若要指定特定程式碼庫，請在留言中加以指明，例如：`@Codex fix this in openai/codex`。

若要追蹤進度：

- 開啟議題中的 **活動** ，即可查看進度更新。
- 開啟對話連結，即可追蹤更詳細的進度。

Codex 完成後，會發布摘要與已完成對話的連結，讓您建立 Pull Request。

### Codex 如何選擇環境和程式碼庫

- Linear 會根據議題的上下文建議程式碼庫，而 Codex 會選擇最符合該建議的環境。如果要求不明確，則會改用您最近使用的環境。
- 對話會在該環境程式碼庫對應表中所列第一個程式碼庫的預設分支上執行。如果您需要變更預設程式碼庫或新增更多程式碼庫，請在 Codex 中更新程式碼庫對應表。
- 如果沒有合適的環境或程式碼庫，Codex 會在 Linear 中回覆修正問題的指示，讓您修正後再重試。

## 自動將議題指派給 Codex

您可以使用分流規則，自動將議題指派給 Codex：

1. 在 Linear 中，前往 **設定**。
2. 在 **您的團隊** 下方，選取您的團隊。
3. 在工作流程設定中，開啟 **分流** 並啟用此功能。
4. 在 **分流規則** 中建立規則，並選擇 **委派** \> **Codex** （以及您想設定的任何其他屬性）。

Linear 會自動將進入分流的新議題指派給 Codex。
使用分流規則時，Codex 會透過議題建立者的帳戶執行對話。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## 資料使用、隱私權與安全性

當您提及 `@Codex` 或將議題指派給 Codex 時，Codex 會接收議題內容，以了解您的要求並建立對話。
資料處理方式遵循 OpenAI 的 [隱私權政策](https://openai.com/privacy)、[使用條款](https://openai.com/terms/)，以及其他適用的 [政策](https://openai.com/policies)。
如需進一步了解安全性，請參閱 [Codex 安全性文件](/zh-Hant/codex/agent-approvals-security)。

Codex 使用大型語言模型，可能會出錯。請務必審查回答與程式碼差異。

## 提示與疑難排解

- **缺少連線**：如果 Codex 無法確認您的 Linear 連線，會在議題中回覆連結，讓您連結帳戶。
- **環境選擇不符預期**：請在留言串中回覆您想使用的環境（例如：`@Codex please run this in openai/codex`）。
- **處理了錯誤的程式碼區段**：請在議題中補充上下文，或在提及 `@Codex` 的留言中提供明確指示。
- **更多協助**：請參閱 [OpenAI 說明中心](https://help.openai.com/)。

<a id="connect-linear-for-local-tasks-mcp"></a>

## 連接 Linear 以進行本機工作（MCP）

如果您使用 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能，且希望在本機存取 Linear 議題，請設定 Linear 模型上下文協定（MCP）伺服器。

如需進一步了解，[請參閱 Linear MCP 文件](https://linear.app/integrations/codex-mcp)。

無論使用 IDE 擴充功能或 CLI，MCP 伺服器的設定步驟都相同，因為兩者共用同一份組態。

### 使用 CLI（建議）

如果您已安裝 CLI，請執行：

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

系統會提示您登入 Linear 帳戶，並將該帳戶連結至 Codex。

### 手動設定

1. 在編輯器中開啟 `~/.codex/config.toml`。
2. 加入以下內容：

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. 執行 `codex mcp login linear` 以登入。
