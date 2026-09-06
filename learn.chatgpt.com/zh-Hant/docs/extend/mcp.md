<!-- source: https://learn.chatgpt.com/zh-Hant/docs/extend/mcp -->

模型上下文協定（MCP）可將模型連接至工具與上下文。您可以透過這項協定讓 ChatGPT 或 Codex 存取第三方文件，或與瀏覽器、Figma 等開發工具互動。

ChatGPT 網頁版可以使用外掛程式提供、由 MCP 支援的遠端工具。本機 Codex 用戶端也可以直接連線至 MCP 伺服器，並共用組態。

<a id="supported-mcp-features"></a>

ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能支援 MCP 伺服器，並針對同一部 Codex 主機共用 MCP 組態。

下列支援的伺服器功能適用於在 Codex 主機上設定的 MCP 伺服器。託管的外掛程式工具可能具備不同功能。

## 支援的 MCP 功能

- **STDIO 伺服器**：以本機處理程序執行的伺服器（由指令啟動）。
  - 環境變數
- **可串流 HTTP 伺服器**：透過位址存取的伺服器。
  - Bearer Token 身分驗證
  - OAuth 身分驗證，包括用戶端 ID 中繼資料文件（CIMD）和動態用戶端註冊（DCR）
  - 適用於受信任的第一方伺服器的 ChatGPT 工作階段身分驗證
- **伺服器指示**：Codex 會讀取初始化時傳回的 MCP `instructions` 欄位，將其作為適用於整個伺服器的指引，搭配該伺服器的工具使用。

若您為 Codex 建置或維護 MCP 伺服器，請使用 `instructions` 說明適用於整個伺服器的跨工具工作流程、限制條件與速率限制。請確保前 512 個字元的內容可獨立理解，讓 Codex 決定如何使用伺服器時能取得最重要的指引。

## 將 Codex 連線至 MCP 伺服器

Codex 會將 MCP 組態連同其他 Codex 組態設定儲存在 `config.toml` 中。預設位置為 `~/.codex/config.toml`，但您也可以使用 `.codex/config.toml` 將 MCP 伺服器限定在專案範圍內（僅限受信任的專案）。

ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能會共用此組態。設定 MCP 伺服器後，您可以在這些用戶端之間切換，無須重新設定。

### 在 ChatGPT 桌面版應用程式中設定

1. 開啟「 **設定**」，然後選取「 **MCP 伺服器**」。
2. 選取「 **新增伺服器**」。
3. 輸入名稱，選擇「 **STDIO** 」或「 **可串流 HTTP**」，並提供
   伺服器的指令或 URL。
4. 儲存伺服器設定，然後選取「 **重新啟動**」。

伺服器清單會顯示哪些伺服器已啟用，以及哪些需要 OAuth。當 OAuth 伺服器需要登入時，請選取
「**身分驗證** 」。在撰寫工具中輸入 `/mcp`，
即可查看已連線的伺服器。

## 在 ChatGPT 網頁版中使用 MCP 支援的工具

在託管的 ChatGPT Work 對話中，安裝[外掛程式](/zh-Hant/codex/plugins)，即可使用其
隨附的連接器和遠端 MCP 工具。安裝後，對話與 Work 都可以
使用這些工具。工作區管理員可以控制
哪些外掛程式和工具可供使用。

ChatGPT 網頁版不會讀取本機 Codex 組態檔案，也不會提供本機的
Codex 指令選單。開啟「 **外掛程式** 」分頁，
即可瀏覽及管理可用工具。

### 使用 CLI 進行設定

#### 新增 MCP 伺服器

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

例如，若要新增 Context7（提供開發人員文件的免費 MCP 伺服器），您可以執行下列指令：

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### 其他 CLI 指令

執行 `codex mcp list` 可查看已設定的伺服器。若要查看所有可用的 MCP 指令，
請執行 `codex mcp --help`。對於支援 OAuth 的伺服器，請執行
`codex mcp login <server-name>`。

#### 終端使用者介面（TUI）

在 `codex` TUI 中，使用 `/mcp` 查看目前作用中的 MCP 伺服器。

### 在 IDE 擴充功能中設定

1. 開啟齒輪圖示選單，然後選取「 **MCP 伺服器**」。
2. 選取「 **新增伺服器**」。
3. 輸入名稱，選擇「 **STDIO** 」或「 **可串流 HTTP**」，並提供
   伺服器的指令或 URL。
4. 儲存伺服器設定，然後選取「 **重新啟動擴充功能**」。

MCP 伺服器清單會顯示哪些伺服器已啟用，以及哪些需要 OAuth。
當 OAuth 伺服器需要登入時，請選取「 **身分驗證** 」。

### 使用 config.toml 進行設定

若要更細緻地控制設定，請編輯 `~/.codex/config.toml` 或專案範圍的
`.codex/config.toml`。請參閱[組態參考資料](/zh-Hant/codex/config-file/config-reference)，
其中提供所有支援的 MCP 選項清單，並可搜尋。

在組態檔案中，使用 `[mcp_servers.<server-name>]` 資料表設定每個 MCP 伺服器。

<a id="stdio-servers"></a>

#### STDIO 伺服器

- `command`（必要）：啟動伺服器的指令。
- `args`（選用）：要傳遞給伺服器的引數。
- `env`（選用）：要為伺服器設定的環境變數。
- `env_vars`（選用）：允許並轉送的環境變數。
- `cwd`（選用）：啟動伺服器時使用的工作目錄。
- `experimental_environment`（選用）：設為 `remote`，即可在有可用的遠端執行器環境時，
  透過該環境啟動 stdio 伺服器。

`env_vars` 可包含一般變數名稱，或指定了來源的物件：

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

字串項目和 `source = "local"` 都會從 Codex 的本機環境讀取值。
`source = "remote"` 會從遠端執行器環境讀取值，且需要
遠端 MCP stdio。

<a id="streamable-http-servers"></a>

#### 可串流 HTTP 伺服器

- `url`（必要）：伺服器位址。
- `auth`（選用）：在嘗試已設定的 Bearer Token 與
  授權標頭之後，再嘗試的身分驗證方式。使用 `oauth`（預設值）可採用已儲存的 MCP OAuth 認證資訊。
  使用 `chatgpt` 則可針對受信任的第一方 ChatGPT 來源，
  使用目前的 ChatGPT 工作階段，並以已儲存的 OAuth 認證資訊作為備援。
- `bearer_token_env_var`（選用）：環境變數的名稱，其值為要在 `Authorization` 中傳送的 Bearer Token。
- `http_headers`（選用）：標頭名稱與靜態值的對應表。
- `env_http_headers`（選用）：標頭名稱與環境變數名稱的對應表（值取自環境）。
- `http_headers_helper`（選用）：輸出 JSON 物件的本機指令，物件中包含
  標頭名稱及其字串值，例如 `{"X-Auth": "temporary-token"}`。
  支援從本機環境建立的 HTTP MCP 連線；不支援
  stdio 伺服器，也不支援透過遠端執行環境建立的連線。

Codex 會為連線快取輔助程式提供的標頭。當同源 POST 要求
傳回 `401` 或 `403` 時，Codex 會重新整理標頭一次，且只有在
輔助程式傳回的值有變更時才會重試。明確指定的 Bearer Token 與 OAuth 認證資訊
優先於輔助程式提供的 `Authorization` 標頭。
回報授權範圍不足的 OAuth `403` 回應不會觸發
輔助程式的標頭更新。

若無法從任何來源取得認證資訊，Codex 可以在不進行
身分驗證的情況下連線至伺服器。請另外執行 `codex mcp login <server-name>`，
以啟動 MCP OAuth 登入流程。

#### 其他組態選項

- `startup_timeout_sec`（選用）：伺服器啟動的逾時時間（秒）。預設值：`10`。
- `tool_timeout_sec`（選用）：伺服器執行工具的逾時時間（秒）。預設值：`60`。
- `enabled`（選用）：設為 `false` 可停用伺服器，而不必刪除它。
- `required`（選用）：設為 `true` 後，若這個已啟用的伺服器無法初始化，啟動就會失敗。
- `enabled_tools`（選用）：工具允許清單。
- `disabled_tools`（選用）：工具拒絕清單（在 `enabled_tools` 之後套用）。
- `default_tools_approval_mode`（選用）：此伺服器所提供工具的
  預設核准行為。支援的值包括 `auto`、`prompt`、`writes` 和
`approve`。`writes` 模式會針對未標示為唯讀的工具要求核准。
- `tools.<tool>.approval_mode`（選用）：個別工具的核准行為覆寫設定。
- `tools.<tool>.output_token_limit`（選用）：單一工具輸出的 Token 額度，必須為正數，
  且不含標準的 20% 序列化預留額度。此設定會覆寫
  模型對該工具預設的輸出截斷額度。

頂層設定 `mcp_optional_startup_grace_ms` 控制 Codex 建立初始工具目錄時，
等待選用 MCP 伺服器的時間。
預設為 `1000` 毫秒。設為 `0` 時，會改為依各伺服器的
`startup_timeout_sec` 等待。必要伺服器仍會使用各自的
啟動逾時設定。

#### OAuth 用戶端註冊與回呼

如果您的授權伺服器要求使用預先註冊的 OAuth 用戶端，請在新增 MCP 伺服器時提供該用戶端的 ID：

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex 會顯示完整的回呼 URL，供您向提供者註冊：

```text
OAuth callback URL: http://127.0.0.1/callback

Codex 會將回呼與用戶端 ID 一併儲存到 `config.toml`，供後續
登入使用：

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

新增的預先註冊用戶端只有在
授權伺服器宣告
`authorization_response_iss_parameter_supported: true`，並在中繼資料中提供
`issuer` 時，才會使用固定的回呼。若未宣告支援簽發者識別，Codex 會附加伺服器專屬的
回呼 ID，例如 `http://127.0.0.1/callback/XuuuHAzzHOni`。未儲存回呼的既有用戶端
會繼續使用各自回呼 ID 專屬的重新導向。

登入時，回呼的選擇取決於 OAuth 組態與授權伺服器的中繼資料：

| OAuth 組態                                                | 簽發者識別支援           | 使用的回呼                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 已設定 `callback_url`，但未設定 `client_id`                                 | 支援                | 使用已設定的回呼進行用戶端註冊。                                                                                           |
| 已設定 `callback_url`，但未設定 `client_id`                                 | 不支援              | 在已設定的回呼後附加伺服器專屬的回呼 ID，再用於用戶端註冊。                                             |
| 已設定 `client_id` 和 `callback_url`                                     | 支援                | 沿用已設定的回呼；授權回應必須包含相符的 `iss`。                                                     |
| 已設定 `client_id`，且 `callback_url` 以正確的回呼 ID 結尾 | 不支援              | 沿用已設定的回呼，不作變更。                                                                                                       |
| 已設定 `client_id`，且 `callback_url` 缺少正確的回呼 ID   | 不支援              | 忽略已設定的回呼。Codex 會使用 `mcp_oauth_callback_url`（若未設定則使用 `http://127.0.0.1/callback`），並附加回呼 ID。 |
| 已設定 `client_id`，但未設定 `callback_url`                    | 無論是否支援 | Codex 會使用全域或預設回呼，並附加伺服器專屬的回呼 ID。                                                           |

這項備援處理不會修改已儲存的回呼 URL。Codex 會根據 MCP 伺服器 URL（包括其路徑與查詢字串）衍生回呼 ID。自動登入與明確觸發的登入都適用相同的選擇規則。

如果需要自訂回呼路徑或遠端 Devbox 入口 URL，請設定 `mcp_oauth_callback_url`。
當提供者支援簽發者識別時，新增的預先註冊用戶端會直接使用該 URL，
不作變更。否則，它們會使用
已設定的 URL，並附加伺服器專屬的回呼 ID。請務必註冊
與 `codex mcp add` 顯示內容完全一致的回呼。

對於未指定連接埠的 `http://127.0.0.1` 回呼，Codex 顯示與儲存的 URL
會省略接聽連接埠，並在授權時
加入目前使用的接聽連接埠。這項替換不適用於 `localhost`、IPv6 主機、
HTTPS URL 或已包含連接埠的回呼。授權伺服器
必須依據
[RFC 8252 第 7.3 節](https://www.rfc-editor.org/rfc/rfc8252#section-7.3) 接受可變動的回送連接埠。

設定 `mcp_oauth_callback_port` 可選用固定的全域接聽連接埠，或設定
`mcp_servers.<server-name>.oauth.callback_port`，為單一伺服器覆寫此設定。
在回呼 URL 中明確指定連接埠，並不會設定接聽程式。使用
直接回送回呼時，請使用未指定連接埠的 `http://127.0.0.1`，或為回呼 URL 與接聽程式
明確設定相同的連接埠。透過代理的回呼
可以刻意使用與本機接聽連接埠不同的外部 URL 連接埠。
本機回呼 URL 會繫結至本機介面；非本機回呼 URL
則會繫結至 `0.0.0.0`。

Codex 會在交換授權碼前驗證所有傳回的 `iss`。
只要 `iss` 不符，就一定會拒絕回應。若已宣告支援簽發者識別，
缺少 `iss` 也會導致回應遭拒。這兩種失敗情況都不會交換授權碼，
也不會改用其他回呼。回呼 URL 格式錯誤，或宣告支援簽發者識別卻
未在中繼資料中提供簽發者，也都會直接導致失敗。請參閱
[驗證使用者身分](/plugins/build/auth)。

如果 MCP 伺服器宣告 `scopes_supported`，Codex 會在 OAuth 登入時優先使用
伺服器宣告的授權範圍。否則，Codex 會改用
在 `config.toml` 中設定的授權範圍。

#### OAuth 用戶端註冊

Codex 支援 [OAuth 用戶端 ID 中繼資料文件（CIMD）](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
與動態用戶端註冊（DCR）。預設情況下，Codex 會在以下條件都成立時
自動選擇 CIMD：授權伺服器宣告
`client_id_metadata_document_supported: true`、將 `none` 列入
`token_endpoint_auth_methods_supported`，且回呼使用受支援的
回送 URL。否則，如果 DCR 可用，Codex 就會使用 DCR。若已設定 OAuth 用戶端
ID，則一律優先使用該 ID，並略過用戶端註冊。

使用 CIMD 時，Codex 會採用由 ChatGPT 託管、專屬於該 MCP 伺服器的中繼資料文件：

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex 會根據 MCP 伺服器 URL 衍生 `<callback_id>`，並將其加入
回送重新導向 URI，例如
`http://127.0.0.1:<port>/callback/<callback_id>`。中繼資料文件會註冊
不含連接埠的對應回送 URI。授權伺服器必須接受登入時選定的
連接埠，同時確保主機與路徑完全相符，以符合
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3) 的規範。若要自訂
回呼主機、路徑或查詢參數，則必須使用 DCR，或使用已設定的 OAuth
用戶端 ID。

即將支援固定的共用 CIMD 文件，目前仍在開發中：

```text
https://chatgpt.com/oauth/codex/client.json

Codex 將使用共用 `/callback` 路徑的固定文件，但前提是
授權伺服器宣告
`authorization_response_iss_parameter_supported: true`、在中繼資料中提供有效的
`issuer`，並在授權回應中包含相符的 `iss`。
回應未與簽發者繫結的伺服器，將繼續使用
回呼專屬文件。

若要為單次 CLI 登入選擇註冊方式，請使用
`--oauth-client-registration`：

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

預設值為 `auto`。所選的註冊方式只適用於目前這次登入，
不會儲存到 `config.toml`。

#### config.toml 範例

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### 外掛程式提供的 MCP 伺服器

已安裝的外掛程式可在其資訊清單中附帶 MCP 伺服器。這些
伺服器由外掛程式啟動，因此使用者設定不會指定其
傳輸指令。仍可透過使用者設定，在
`plugins.<plugin>.mcp_servers.<server>` 下控制啟用／停用狀態與工具政策。

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

外掛程式提供的 HTTP MCP 伺服器也可以在 `.mcp.json` 中宣告 OAuth 設定。
外掛程式資訊清單使用 camelCase 欄位名稱 `clientId`、`callbackUrl` 和
`callbackPort`：

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

外掛程式提供的 MCP 伺服器與其他 MCP 伺服器
遵循相同的回呼選擇規則。如果外掛程式提供了 `clientId`，其提供者不支援
與簽發者繫結的回呼，且 `callbackUrl` 缺少伺服器專屬的回呼
ID，Codex 就會在登入時忽略該 URL，改用 `mcp_oauth_callback_url`，或在未設定時
使用 `http://127.0.0.1/callback`，並附加回呼 ID。
已設定的 `callbackUrl` 保持不變。

外掛程式的 `oauth.callbackPort` 會覆寫全域設定
`mcp_oauth_callback_port`；若兩者皆未設定，Codex 會選擇暫時性連接埠。
`callbackUrl` 內的連接埠不會決定接聽連接埠。若要使用
固定連接埠的直接回送回呼，請將兩個值設為相同：

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

使用遠端入口或其他代理時，只要代理會將流量轉送至已設定的接聽程式，就可以刻意讓回呼 URL 連接埠與本機接聽連接埠不同。

## 實用的 MCP 伺服器範例

MCP 伺服器持續增加。以下是幾個常見的伺服器：

- [OpenAI 文件 MCP](/learn/docs-mcp)：搜尋及閱讀 OpenAI 開發人員文件。
- [Context7](https://github.com/upstash/context7)：連線至最新的開發人員文件。
- Figma [本機](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)與[遠端](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)：存取您的 Figma 設計。
- [Playwright](https://www.npmjs.com/package/@playwright/mcp)：使用 Playwright 控制並檢查瀏覽器。
- [Chrome 開發人員工具](https://github.com/ChromeDevTools/chrome-devtools-mcp/)：控制並檢查 Chrome。
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex)：存取 Sentry 日誌。
- [GitHub](https://github.com/github/github-mcp-server)：管理 GitHub 上 `git` 支援範圍以外的項目（例如 Pull Request 和議題）。
