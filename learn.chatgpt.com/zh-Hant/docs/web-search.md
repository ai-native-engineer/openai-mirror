<!-- source: https://learn.chatgpt.com/zh-Hant/docs/web-search -->

ChatGPT 內建第一方網頁搜尋工具。請將所有網頁搜尋結果視為
不受信任的輸入。

在 ChatGPT 桌面版應用程式中，可在對話中要求提供最新資訊。ChatGPT 會在對話記錄中一併記錄
搜尋活動和其他工具呼叫。

在 ChatGPT 網頁版中，可要求提供最新資訊或來源。ChatGPT 使用網頁搜尋時，搜尋結果和
引用資料會顯示在對話中。工作區
設定可限制搜尋功能是否可用。

在 CLI 中傳入 `--search`，即可擷取該次執行的即時結果：

```bash
codex --search "Summarize the latest release notes for this dependency"

搜尋會以 `web_search` 項目顯示在互動式對話記錄與
`codex exec --json` 輸出中。

使用編輯器工作時，可在 IDE 擴充功能中要求 Codex 進行搜尋。該
擴充功能會使用已連線的 Codex 主機的搜尋模式。搜尋活動會顯示
在對話記錄中。

## 設定本機網頁搜尋

在 Codex 本機對話中，Codex 預設啟用快取搜尋。快取模式使用
由 OpenAI 維護的索引，而不會即時擷取任意網頁，因此可
降低提示注入風險，但無法完全消除。

網頁搜尋是託管工具，獨立於受沙盒限制的本機指令網路連線。
它不會使用權限設定檔的網路代理伺服器或網域允許清單，即使
指令的網路存取功能已停用，也仍可能維持可用。請視需要
透過 `web_search`、`tools.web_search.allowed_domains` 和受管理的
`allowed_web_search_modes` 設定搜尋功能。搜尋網域篩選器不會限制
本機指令流量、應用程式、連接器或 MCP 伺服器。

如果任務仰賴最新資訊，請使用即時搜尋。請將
`web_search = "live"` 設定於 `config.toml` 中。設定 `web_search = "disabled"` 即可
停用此工具。`"indexed"` 模式只有在
搜尋索引放行請求時，才允許存取外部網頁。當 Codex 以完整存取權執行時，網頁搜尋
預設會使用即時結果。請參閱 [基本設定](/zh-Hant/codex/config-file/config-basic)
以瞭解設定檔的位置與優先順序。

### 使用自訂模型供應商進行搜尋

當自訂模型供應商支援
相容的搜尋端點時，即可選擇啟用獨立網頁搜尋：

```toml
model_provider = "custom"
web_search = "live"

[model_providers.custom]
name = "Custom Responses provider"
base_url = "https://example.com/v1"
env_key = "CUSTOM_RESPONSES_API_KEY"
supports_standalone_web_search = true

自訂供應商預設採用 `supports_standalone_web_search = false`。
獨立網頁搜尋仍在開發中，且預設為停用。
設定供應商的這項能力並不會啟用此功能：供應商、
所選模型和執行階段也都必須支援獨立搜尋。工作區限制與
受管理的搜尋限制仍然適用。

如需瞭解適用於 Codex 雲端環境的網路邊界，請參閱 [網際網路
存取](/zh-Hant/codex/cloud/internet-access)。
