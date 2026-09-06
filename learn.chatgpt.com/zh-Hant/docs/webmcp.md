<!-- source: https://learn.chatgpt.com/zh-Hant/docs/webmcp -->

網站工具是 ChatGPT 依據
[WebMCP 標準提案](https://webmachinelearning.github.io/webmcp/)所實作的功能。透過 WebMCP，
網站除了提供既有的使用者介面，
也能直接向 AI 智慧體提供實用的操作。你和智慧體可以使用同一個即時頁面
與已登入的工作階段。

在 ChatGPT 桌面版應用程式的[內建瀏覽器](/zh-Hant/codex/browser)中，
ChatGPT Work 和 Codex 可以找到並使用可用的網站工具。

  使用網站工具時，請選用 GPT-5.6 Sol 或 GPT-5.6 Terra。GPT-5.6 Luna 目前停用了
WebMCP。請將 ChatGPT 桌面版應用程式更新至最新版本。
網站工具不適用於企業或 Edu 工作區。是否能使用這項功能，
也取決於推出進度及目前頁面提供的工具。

## WebMCP 與 MCP 的比較

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/learn/architecture)
可將 AI 應用程式連接至本機或遠端伺服器。其工具不依賴已開啟的網頁
也能運作，例如在服務中搜尋，或透過 API
管理記錄。

[WebMCP](https://github.com/webmachinelearning/webmcp) 讓網站以一組預先定義的工具，
將功能提供給智慧體。智慧體造訪網站時就能找到這些工具，
因此使用者不必另行安裝 MCP 伺服器，
也不必設定其他連線，就能使用這些功能。

當你和智慧體需要查看相同內容時，這種方式就很實用，
例如編輯畫布或探索儀表板。
[搭配 MCP 伺服器的外掛程式](/zh-Hant/codex/build-plugins)則能提供
不依賴已開啟頁面即可運作的整合功能。網站可以同時支援這兩種方式。

## 在瀏覽器中的運作方式

在內建瀏覽器中開啟網站，並請 ChatGPT Work 或 Codex 協助處理任務。
如果頁面提供網站工具，智慧體就能在你正在瀏覽的網站中找到並使用
相關操作。例如，文件編輯器可能會讓智慧體
尋找某個章節，或留下留言供你審查。

在瀏覽器網址列選取 **網站工具** ，即可查看網站
提供哪些工具。選擇 **可用的網站工具** ，即可逐一查看工具。
網站執行每項請求前，瀏覽器都會先行檢查，
智慧體也能檢查頁面，確認有哪些變更。若有近期活動可供查看，
請選擇 **最近使用** ，開啟 **來源** 並審查這些呼叫。

在此範例中，展開 **可用的網站工具** ，
即可查看 [Margin](https://margin-local-docs.openai.chatgpt.site) 提供的工具。

  

工具屬於提供它們的頁面。關閉或離開頁面後，
該頁面的工具可能就無法使用。如果沒有合適的工具可用，
智慧體或許仍能使用原有的瀏覽器功能。

## 範例：探索 OpenAI 文件

ChatGPT 學習和 OpenAI 開發人員網站都提供網站工具，可用來尋找及閱讀
文件。在撰寫工具中選取 **在 ChatGPT 中開啟** ，即可在桌面 App 的
瀏覽器中開啟「學習」，並在旁邊開啟新對話，內含已準備好傳送的這則提示詞。

智慧體可以使用這些工具搜尋、閱讀及開啟相關頁面：

| 工具                    | 功能                                                             |
| ----------------------- | ------------------------------------------------------------------------ |
| `search_openai_docs`    | 搜尋 OpenAI 文件。                                           |
| `lookup_page`           | 依路徑或 URL 讀取文件頁面。                               |
| `lookup_context`        | 讀取目前的文件路由與選取的文字。                          |
| `navigate_to_page`      | 在目前的文件網站中開啟相符的頁面。                 |
| `generate_custom_guide` | 開始產生自訂的建置或學習指南，並傳回其狀態與連結。 |

文件智慧體會以非同步方式產生自訂指南。收到指南連結，並不代表產生作業已完成。

## 安全性與使用者控制項

網站提供的工具定義與結果都屬於不受信任的內容。工具的名稱或「僅讀取資料」的宣稱，並不能證明工具的實際行為。網站上的指示不會授予智慧體分享無關資訊或執行敏感操作的權限。

在內建瀏覽器中，每次工具呼叫都會在執行前接受安全審查。一般的網站存取與確認政策仍然適用，包括傳送訊息、購物、刪除資料或變更權限等會造成實際影響的操作。瀏覽器會將每次呼叫與其來源頁面及工具註冊資訊綁定。這些檢查能降低風險，但不代表網站或其輸出就值得信任。

你可以在 **設定 \> 瀏覽器 \> 權限**中關閉 **啟用網站工具** 。
在分享敏感資訊或依賴某項變更前，
請先審查網站、要求執行的操作及其結果。

請透過 OpenAI 的
[安全性漏洞賞金計畫](https://bugcrowd.com/engagements/openai)回報安全性漏洞。關於 AI 安全風險，
請參閱
[安全漏洞賞金計畫](https://openai.com/index/safety-bug-bounty/)。請遵循
各計畫的適用範圍與提交指示。

## 限制

ChatGPT 的內建瀏覽器目前僅支援部分 WebMCP API。
不支援下列功能：

- **宣告式 API：** 透過 HTML 表單屬性定義的工具
  無法作為網站工具使用。
- **iframe 內的工具：** 瀏覽器不會偵測在 iframe 內註冊的工具，
  包括同源與跨來源 iframe。

請使用 JavaScript 在頂層頁面註冊工具，做法如
[下一節](#add-webmcp-to-your-website)所示。ChatGPT Work 和 Codex 仍可能
使用一般瀏覽器功能與表單互動，但這些互動
並不是 WebMCP 工具呼叫。

WebMCP 規格與 Chrome 開發人員指南涵蓋的 API 範圍更廣，包括內建瀏覽器目前尚未支援的功能。

## 為你的網站加入 WebMCP

你可以請 Codex 為你正在開發的網頁應用程式或
[Site](/zh-Hant/codex/sites) 加入 WebMCP 支援。說明你希望智慧體能執行哪些操作，
並請 Codex 沿用應用程式既有的邏輯與權限。

先從應用程式已支援的操作著手。例如：

- 儀表板可讓智慧體設定日期範圍，並查看圖表所依據的資料。
- 文件編輯器可讓智慧體尋找特定章節、提出編輯建議，或留下註解供你審查。
- 旅遊規劃工具可讓智慧體在你查看地圖時，比較選項並更新行程。

你也可以自行撰寫程式碼。在頁面的 JavaScript 模組中，檢查瀏覽器是否支援 WebMCP，並註冊工具。以下唯讀範例會傳回目前頁面的標題：

```javascript
if (typeof document.modelContext?.registerTool === "function") {
  await document.modelContext.registerTool({
    name: "get_page_title",
    description: "Read the title of the current page.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true },
    execute: async () => ({ title: document.title }),
  });
}

相容的智慧體可以找到 `get_page_title` 並取得頁面目前的標題。
對於接受引數的工具，請在輸入結構描述中說明這些引數，
並在 `execute` 處理常式中使用它們，
以呼叫應用程式既有的邏輯。

限制輸入範圍、說明副作用，並傳回足夠的資訊以驗證結果。沿用應用程式既有的身分驗證、授權與輸入驗證機制。保留一般介面，供使用者及不支援 WebMCP 的瀏覽器使用。

如需 API 詳細資訊與範例，請參閱
[WebMCP 規格](https://webmachinelearning.github.io/webmcp/)和
[Chrome 開發人員指南](https://developer.chrome.com/docs/ai/webmcp)。
