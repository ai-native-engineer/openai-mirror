<!-- source: https://learn.chatgpt.com/zh-Hant/docs/config-file/config-advanced -->

當您需要進一步控制供應商、政策與整合時，請使用這些選項。如要快速開始，請參閱 [基本設定](/zh-Hant/codex/config-file/config-basic)。

如需瞭解專案指引、可重複使用的能力、自訂斜線指令、子代理程式工作流程與整合的背景資訊，請參閱 [自訂](/zh-Hant/codex/customization/overview)。如需設定鍵資訊，請參閱 [設定參考資料](/zh-Hant/codex/config-file/config-reference)。

## 設定檔

設定檔可讓您儲存具名設定層，並透過
CLI 在不同設定檔之間切換。傳遞 `--profile profile-name` 時，Codex 會先載入
`~/.codex/config.toml`，再疊加 `~/.codex/profile-name.config.toml`。
設定檔名稱可包含字母、數字、連字號和底線。

請為每個設定檔建立個別的 TOML 檔案。在
設定檔中使用頂層設定鍵；請勿將其巢狀置於 `[profiles.profile-name]` 之下。

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

設定檔層的優先順序高於基本使用者設定，但低於
專案與 CLI 設定，因此只需包含與基本
設定不同的值。設定檔也可以覆寫 `model_catalog_json`；如果兩個檔案都設定此值，Codex 會採用
設定檔中的值。

在 Codex 0.134.0 及更新版本中，`--profile` 不再讀取 `[profiles.profile-name]`
（原本位於 `config.toml`），而且頂層的 `profile = "profile-name"` 選擇器也
不再受支援。請將舊版設定檔設定移至
`~/.codex/profile-name.config.toml`，然後移除相符的
`[profiles.profile-name]` 表格和 `profile = "profile-name"` 選擇器，這兩者位於
`config.toml` 中。

## 透過 CLI 進行單次覆寫

除了編輯 `~/.codex/config.toml`，您也可以透過 CLI 覆寫單次執行的設定：

- 如有專用旗標，請優先使用，例如 `--model`。
- 若需覆寫任意設定鍵，請使用 `-c` / `--config`。

範例：

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

注意事項：

- 設定鍵可以使用點標記法設定巢狀值，例如 `mcp_servers.context7.enabled=false`。
- 系統會將 `--config` 的值剖析為 TOML。如不確定，請為值加上引號，以免 Shell 在空格處將其拆分。
- 若無法將值剖析為 TOML，Codex 會將其視為字串。

## 設定與狀態的位置

Codex 將本機狀態儲存在 `CODEX_HOME` 下，預設為 `~/.codex`。

該位置常見的檔案包括：

- `config.toml`（您的本機設定）
- `auth.json`（若使用檔案型憑證儲存），或作業系統的鑰匙圈／金鑰環
- `history.jsonl`（若已啟用歷程記錄持續保存）
- 其他個別使用者狀態，例如記錄檔與快取

如需身分驗證的詳細資訊，包括憑證儲存模式，請參閱 [身分驗證](/zh-Hant/codex/auth)。如需完整的設定鍵清單，請參閱 [設定參考資料](/zh-Hant/codex/config-file/config-reference)。

如需瞭解存放在程式碼庫或系統路徑中的共用預設值、規則和技能，請參閱 [團隊設定](/zh-Hant/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config)。

如果只需將內建 OpenAI 供應商指向 LLM 代理伺服器、路由器或已啟用資料駐留的專案，請在 `config.toml` 中設定 `openai_base_url`，而不要定義新的供應商。這會變更內建 `openai` 供應商的基礎 URL，無須另外建立 `model_providers.<id>` 項目。

```toml
openai_base_url = "https://us.api.openai.com/v1"

## 專案設定檔（`.codex/config.toml`）

除了使用者設定外，Codex 也會從程式碼庫內的 `.codex/config.toml` 檔案讀取專案層級的覆寫設定。Codex 會從專案根目錄一路走訪至目前工作目錄，並載入找到的每個 `.codex/config.toml`。如果多個檔案定義同一設定鍵，則以最接近工作目錄的檔案為準。

為確保安全，只有在專案受信任時，Codex 才會載入專案層級的設定檔。如果專案不受信任，Codex 會忽略專案的 `.codex/` 層，包括 `.codex/config.toml`、專案內的掛勾及專案內的規則。使用者層和系統層仍然彼此獨立，且照常載入。

專案設定中的相對路徑，例如 `model_instructions_file`，會以 `.codex/` 資料夾為基準解析；該資料夾包含 `config.toml`。

專案設定檔無法覆寫會重新導向憑證、變更
主機端控管的應用程式請求中繼資料、變更供應商身分驗證、選取設定檔，
或執行本機通知／遙測指令的設定。Codex 會忽略
專案內 `.codex/config.toml` 的下列設定鍵，並在發現時顯示
啟動警告：`openai_base_url`、`chatgpt_base_url`、
`apps_mcp_product_sku`、`model_provider`、`model_providers`、`notify`、
`profile`、`profiles`、`experimental_realtime_ws_base_url` 和 `otel`。請在
使用者層級的
`~/.codex/config.toml` 中設定供應商、通知和遙測設定鍵；使用 `--profile profile-name`
和 `~/.codex/profile-name.config.toml` 選取設定檔。

## 掛勾

Codex 也可以從 `hooks.json` 檔案，或從內嵌的
`[hooks]` 表格載入生命週期掛勾；後者位於作用中設定層旁的 `config.toml` 檔案內。

實際上最實用的四個位置如下：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

只有在專案的 `.codex/` 層受信任時，才會載入專案內的掛勾。
使用者層級的掛勾不受專案信任狀態影響。

內嵌 TOML 掛勾使用與 `hooks.json` 相同的事件結構：

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

如果同一層同時包含 `hooks.json` 和內嵌 `[hooks]`，Codex 會將
兩者都載入並發出警告。每一層最好只使用一種表示方式。

如需目前的事件清單、輸入欄位、輸出行為和限制，請參閱
[掛勾](/zh-Hant/codex/hooks)。

## 智慧體角色（`config.toml` 中的 `[agents]`）

如需子代理程式角色設定（`config.toml` 中的 `[agents]`），請參閱 [子代理程式](/zh-Hant/codex/agent-configuration/subagents)。

## 專案根目錄偵測

Codex 會從工作目錄逐層向上搜尋，直到專案根目錄，以尋找專案設定，例如 `.codex/` 層與 `AGENTS.md`。

根據預設，Codex 會將包含 `.git` 的目錄視為專案根目錄。若要自訂此行為，請在 `config.toml` 中設定 `project_root_markers`：

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

設定 `project_root_markers = []`，即可略過上層目錄搜尋，並將目前工作目錄視為專案根目錄。

## 自訂模型供應商

模型供應商定義 Codex 連線至模型的方式，包括基礎 URL、通訊 API、身分驗證及選用的 HTTP 標頭。自訂供應商無法重複使用保留的內建供應商 ID：`openai`、`ollama` 和 `lmstudio`。

定義其他供應商，並讓 `model_provider` 指向這些供應商：

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

如果自訂供應商支援獨立的網頁搜尋端點，請在其供應商設定中宣告
這項能力：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

此設定對自訂供應商預設為 `false`。獨立網頁搜尋
仍在開發中，預設為關閉。將供應商能力設為 `true`
並不會啟用此功能：供應商必須支援相容的端點，
且所選模型與執行階段必須支援獨立搜尋。此外，
已設定的 [`web_search` 模式](/zh-Hant/codex/web-search)與
受管理的搜尋限制仍然適用。

視需要新增請求標頭：

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

當供應商需要 Codex 從外部憑證輔助程式擷取 Bearer Token 時，請使用以指令為基礎的身分驗證：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

身分驗證指令不接收任何 `stdin`，且必須將 Token 輸出至 stdout。Codex 會去除前後空白字元、將空 Token 視為錯誤，並按照 `refresh_interval_ms` 主動重新整理；若設定 `refresh_interval_ms = 0`，則只會在重試身分驗證後重新整理。請勿將 `[model_providers.<id>.auth]` 與 `env_key`、`experimental_bearer_token` 或 `requires_openai_auth` 搭配使用。

### Amazon Bedrock 供應商

Codex 包含內建的 `amazon-bedrock` 模型供應商。請直接將其設為
`model_provider`；與自訂供應商不同，此內建供應商只支援
巢狀設定中的 AWS 設定檔與區域覆寫。

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

若省略 `profile`，Codex 會使用標準 AWS 憑證鏈。請將
`region` 設為要用來處理請求的受支援 Bedrock 區域。

如需完整的設定流程、身分驗證選項、支援的模型和功能
可用性，請參閱 [搭配 Amazon
Bedrock 使用 ChatGPT Work 與 Codex](/zh-Hant/codex/amazon-bedrock)。

## OSS 模式（本機供應商）

Codex 可透過 Ollama 或 LM
Studio 等本機「開源」供應商執行，只需傳遞 `--oss`。若只想在單次執行中選用其中之一，請使用
`--local-provider`，或將 `oss_provider` 設為預設值。若兩者皆未設定，
互動式 CLI 會提示您選擇；`codex exec` 則會結束並顯示錯誤。

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Azure 供應商與個別供應商調校

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

若要變更內建 OpenAI 供應商的基礎 URL，請使用 `openai_base_url`；請勿建立 `[model_providers.openai]`，因為內建供應商 ID 無法覆寫。

## 使用資料駐留的 API 組織

建立時已啟用[資料駐留](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)的專案，可以建立模型供應商，並使用[正確的前置字串](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)更新 `base_url`。對於已啟用資料駐留的 ChatGPT 工作區，不需要自訂供應商；使用 ChatGPT 登入時，Codex 會遵循工作區的資料駐留設定。

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## 模型推理、詳細程度與限制

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` 僅適用於使用 Responses API 的供應商。Chat Completions 供應商會忽略此設定。

## 核准政策與沙盒模式

選擇核准嚴格度（影響 Codex 何時暫停）與沙盒層級（影響檔案/網路存取）。

如需編輯 `config.toml` 時應留意的操作細節，請參閱 [常見的沙盒與核准組合](/zh-Hant/codex/agent-approvals-security#common-sandbox-and-approval-combinations)、[可寫入根目錄中的受保護路徑](/zh-Hant/codex/agent-approvals-security#protected-paths-in-writable-roots)和 [網路存取](/zh-Hant/codex/agent-approvals-security#network-access)。

如需同時設定檔案系統與網路存取的測試版權限設定檔，請參閱 [權限](/zh-Hant/codex/permissions)。

你也可以使用精細核准政策（`approval_policy = { granular = { ... } }`），允許或自動拒絕個別提示詞類別。當你希望某些情況維持一般互動式核准，而其他情況（例如 `request_permissions` 或技能指令碼提示詞）自動採取預設拒絕處置時，這項設定就很實用。

設定 `approvals_reviewer = "auto_review"`，即可將符合條件的互動式核准
要求交由自動審查。此設定會變更審查者，但不會改變沙盒
邊界。

使用 `[auto_review].policy` 設定本機審查者的政策指示。受管理的
`guardian_policy_config` 設定優先適用。

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### 具名權限設定檔

如需內建設定檔、自訂設定檔語法，以及完整的檔案系統與
網路組態模型，請參閱 [權限](/zh-Hant/codex/permissions)。

如需完整的設定鍵清單與要求限制，請參閱
[設定參考](/zh-Hant/codex/config-file/config-reference)和
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)。

  在 workspace-write 模式下，即使工作區其餘部分可寫入，某些環境仍會讓 `.git/` 和 `.codex/`
  維持唯讀。因此，
  `git commit` 等指令仍可能需要核准，才能在
  沙盒外執行。若要讓 Codex 略過特定指令（例如阻止在沙盒外執行 `git
  commit`），請使用
<a href="/codex/agent-configuration/rules">規則</a>。

完全停用沙盒（僅限環境已隔離程序時使用）：

```toml
sandbox_mode = "danger-full-access"

## Shell 環境政策

`shell_environment_policy` 控制 Codex 會將哪些環境變數傳遞給
所啟動的指令。使用 `inherit = "none"` 從空白環境開始，或
使用 `inherit = "core"` 繼承一組精簡的環境變數。加入明確指定的值與依鍵名設定的
篩選條件，避免將不必要的機密資訊傳遞給所啟動的指令。

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

篩選模式不區分大小寫，且支援 `*` 和 `?`。使用 `"exclude"`
移除相符的變數。當任何模式使用 `"include"` 時，Codex 只會保留
符合納入模式的變數。納入模式不會還原
已排除的變數。不同組態層中的篩選鍵會以不區分大小寫的方式
合併。

`ignore_default_excludes` 預設為 `true`，因此 Codex 不會自動
移除名稱含有 `KEY`、`SECRET` 或 `TOKEN` 的變數。將其設為 `false`
即可在執行明確設定的篩選條件前，套用這些自動排除項目。

Codex 會依序套用自動排除、自訂排除、來自
`set` 的值，最後再套用納入模式允許清單。由於 `set` 會在
排除作業之後套用，因此可以還原已排除的變數。納入模式允許清單
仍可移除該還原值。

較舊的 `exclude` 和 `include_only` 陣列在既有
組態中仍受支援。請勿在同一組態層中將任一陣列與
`[shell_environment_policy.filters]` 並用；Codex
會拒絕這種組合。

## MCP 伺服器

如需組態詳細資訊，請參閱專門的 [MCP 文件](/zh-Hant/codex/extend/mcp)。

## 可觀測性與遙測

啟用 OpenTelemetry（OTel）日誌匯出，以追蹤 Codex 執行情況（API 要求、SSE/事件、提示詞、工具核准/結果）。此功能預設為停用；可透過 `[otel]` 啟用：

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

選擇匯出器：

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

若 `exporter = "none"`，Codex 會記錄事件，但不會傳送任何資料。匯出器會以非同步方式批次處理事件，並在關閉時送出剩餘事件。事件中繼資料包含服務名稱、CLI 版本、環境標記、對話 ID、模型、沙盒/核准設定，以及各事件欄位（請參閱[設定參考](/zh-Hant/codex/config-file/config-reference)）。

### 發出的內容

Codex 會針對執行作業與工具使用情況發出結構化日誌事件。代表性事件類型包括：

- `codex.conversation_starts`（模型、推理設定、沙盒/核准政策）
- `codex.api_request`（嘗試次數、狀態/成功與否、持續時間和錯誤詳細資訊）
- `codex.sse_event`（串流事件種類、成功/失敗、持續時間，以及 `response.completed` 的 Token 數量）
- `codex.websocket_request` 和 `codex.websocket_event`（要求持續時間，以及每則訊息的種類/成功與否/錯誤）
- `codex.user_prompt`（長度；除非明確啟用，否則會遮蔽內容）
- `codex.tool_decision`（已核准/已拒絕，以及決策來自組態還是使用者）
- `codex.tool_result`（持續時間、成功與否、輸出片段）

### 發出的 OTel 指標

啟用 OTel 指標管線後，Codex 會針對 API、串流和工具活動發出計數器與持續時間直方圖。

下列每項指標也都包含預設的中繼資料標記：`auth_mode`、`originator`、`session_source`、`model` 和 `app.version`。

| 指標                                | 類型      | 欄位              | 說明                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | 計數器   | `status`、`success` | 依 HTTP 狀態和成功/失敗區分的 API 要求數。             |
| `codex.api_request.duration_ms`       | 直方圖 | `status`、`success` | API 要求的持續時間（以毫秒為單位）。                             |
| `codex.sse_event`                     | 計數器   | `kind`、`success`   | 依事件種類和成功/失敗區分的 SSE 事件數。                |
| `codex.sse_event.duration_ms`         | 直方圖 | `kind`、`success`   | SSE 事件處理時間（以毫秒為單位）。                    |
| `codex.websocket.request`             | 計數器   | `success`           | 依成功/失敗區分的 WebSocket 要求數。                       |
| `codex.websocket.request.duration_ms` | 直方圖 | `success`           | WebSocket 要求的持續時間（以毫秒為單位）。                       |
| `codex.websocket.event`               | 計數器   | `kind`、`success`   | 依類型和成功/失敗區分的 WebSocket 訊息/事件數。        |
| `codex.websocket.event.duration_ms`   | 直方圖 | `kind`、`success`   | WebSocket 訊息/事件處理時間（以毫秒為單位）。      |
| `codex.tool.call`                     | 計數器   | `tool`, `success`   | 依工具名稱及成功或失敗結果統計的工具呼叫次數。           |
| `codex.tool.call.duration_ms`         | 直方圖 | `tool`, `success`   | 依工具名稱與執行結果統計的工具執行時間（毫秒）。 |

如需更多遙測相關的安全性與隱私权指引，請參閱 [安全性](/zh-Hant/codex/agent-approvals-security#monitoring-and-telemetry)。

### 指標

預設情況下，Codex 會定期將少量匿名使用情況與運作狀態資料傳回 OpenAI。這有助於偵測 Codex 無法正常運作的情況，並掌握正在使用哪些功能與組態選項，讓 Codex 團隊能專注於最重要的事項。這些指標不含任何個人識別資訊（PII）。指標收集與 OTel 日誌和追蹤匯出彼此獨立。

若要在同一台電腦上全面停用 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能的指標收集，請在組態中設定 analytics 旗標：

```toml
[analytics]
enabled = false

每個指標都包含本身的欄位，以及下列預設上下文欄位。

#### 預設上下文欄位（適用於所有事件和指標）

- `auth_mode`：`swic` \| `api` \| `unknown`。
- `model`：所使用模型的名稱。
- `app.version`：Codex 版本。

#### 指標目錄

每個指標都包含必要欄位以及上述預設上下文欄位。下列指標名稱省略 `codex.` 前綴。
大多數指標名稱集中定義於 `codex-rs/otel/src/metrics/names.rs`；在該檔案之外發出的功能專屬指標也一併列於此處。
如果指標包含 `tool` 欄位，該欄位會反映所使用的內部工具（例如 `apply_patch` 或 `shell`），不會包含實際的 shell 指令，或 `codex` 嘗試套用的修補程式。

#### 執行階段與模型傳輸

| 指標                                          | 類型      | 欄位               | 說明                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | 計數器   | `status`, `success`  | 依 HTTP 狀態及成功或失敗結果統計的 API 請求次數。        |
| `api_request.duration_ms`                       | 直方圖 | `status`, `success`  | API 請求持續時間（毫秒）。                        |
| `sse_event`                                     | 計數器   | `kind`, `success`    | 依事件種類及成功或失敗結果統計的 SSE 事件數量。           |
| `sse_event.duration_ms`                         | 直方圖 | `kind`, `success`    | SSE 事件處理持續時間（毫秒）。               |
| `websocket.request`                             | 計數器   | `success`            | 依成功或失敗結果統計的 WebSocket 請求次數。                  |
| `websocket.request.duration_ms`                 | 直方圖 | `success`            | WebSocket 請求持續時間（毫秒）。                  |
| `websocket.event`                               | 計數器   | `kind`, `success`    | 依類型及成功或失敗結果統計的 WebSocket 訊息和事件數量。   |
| `websocket.event.duration_ms`                   | 直方圖 | `kind`, `success`    | WebSocket 訊息和事件處理持續時間（毫秒）。 |
| `responses_api_overhead.duration_ms`            | 直方圖 |                      | 從 WebSocket 回應取得的 Responses API 額外負荷時間。      |
| `responses_api_inference_time.duration_ms`      | 直方圖 |                      | 從 WebSocket 回應取得的 Responses API 推論時間。     |
| `responses_api_engine_iapi_ttft.duration_ms`    | 直方圖 |                      | Responses API 引擎 IAPI 的首個 Token 等待時間。        |
| `responses_api_engine_service_ttft.duration_ms` | 直方圖 |                      | Responses API 引擎服務的首個 Token 等待時間。     |
| `responses_api_engine_iapi_tbt.duration_ms`     | 直方圖 |                      | Responses API 引擎 IAPI 的 Token 間隔時間。         |
| `responses_api_engine_service_tbt.duration_ms`  | 直方圖 |                      | Responses API 引擎服務的 Token 間隔時間。      |
| `transport.fallback_to_http`                    | 計數器   | `from_wire_api`      | WebSocket 回退至 HTTP 的次數。                            |
| `remote_models.fetch_update.duration_ms`        | 直方圖 |                      | 擷取遠端模型定義所需的時間。                      |
| `remote_models.load_cache.duration_ms`          | 直方圖 |                      | 載入遠端模型快取所需的時間。                         |
| `startup_prewarm.duration_ms`                   | 直方圖 | `status`             | 依結果分類的啟動預熱持續時間。                         |
| `startup_prewarm.age_at_first_turn_ms`          | 直方圖 | `status`             | 第一個實際輪次取得啟動預熱結果時，該預熱已經過的時間。    |
| `cloud_requirements.fetch.duration_ms`          | 直方圖 |                      | 擷取工作區管理的雲端需求所需的時間。         |
| `cloud_requirements.fetch_attempt`              | 計數器   | 見附註             | 嘗試擷取工作區管理的雲端需求的次數。         |
| `cloud_requirements.fetch_final`                | 計數器   | 見附註             | 工作區管理的雲端需求最終擷取結果。    |
| `cloud_requirements.load`                       | 計數器   | `trigger`、`outcome` | 工作區管理的雲端需求載入結果。           |

`cloud_requirements.fetch_attempt` 指標包含 `trigger`、`attempt`、`outcome` 與 `status_code` 欄位。`cloud_requirements.fetch_final` 指標包含 `trigger`、`outcome`、`reason`、`attempt_count` 與 `status_code` 欄位。

#### 輪次與工具活動

| 指標                                 | 類型      | 欄位                                                                    | 說明                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | 直方圖 |                                                                           | 完整輪次的端對端耗時。                                                                                 |
| `turn.ttft.duration_ms`                | 直方圖 |                                                                           | 輪次產生第一個 Token 所需的時間。                                                                                  |
| `turn.ttfm.duration_ms`                | 直方圖 |                                                                           | 輪次產生第一個模型輸出項目所需的時間。                                                                      |
| `turn.network_proxy`                   | 計數器   | `active`、`tmp_mem_enabled`                                               | 該輪次是否啟用了受管理的網路代理伺服器。                                                       |
| `turn.memory`                          | 計數器   | `read_allowed`、`feature_enabled`、`config_use_memories`、`has_citations` | 各輪次的記憶讀取可用性與記憶引用使用情況。                                                     |
| `turn.tool.call`                       | 直方圖 | `tmp_mem_enabled`                                                         | 輪次中的工具呼叫次數。                                                                                |
| `turn.token_usage`                     | 直方圖 | `token_type`、`tmp_mem_enabled`                                           | 各輪次依 Token 類型區分的 Token 用量（`total`、`input`、`cached_input`、`output` 或 `reasoning_output`）。          |
| `tool.call`                            | 計數器   | `tool`、`success`                                                         | 依工具名稱和成功／失敗狀態區分的工具呼叫次數。                                                          |
| `tool.call.duration_ms`                | 直方圖 | `tool`、`success`                                                         | 依工具名稱和結果區分的工具執行耗時（毫秒）。                                                |
| `tool.unified_exec`                    | 計數器   | `tty`                                                                     | 依 TTY 模式區分的統一 exec 工具呼叫次數。                                                                             |
| `approval.requested`                   | 計數器   | `tool`、`approved`                                                        | 工具核准要求的結果（`approved`、`approved_with_amendment`、`approved_for_session`、`denied`、`abort`）。 |
| `mcp.call`                             | 計數器   | 見附註                                                                  | MCP 工具呼叫結果。                                                                                      |
| `mcp.call.duration_ms`                 | 直方圖 | 見附註                                                                  | MCP 工具呼叫耗時。                                                                                    |
| `mcp.tools.list.duration_ms`           | 直方圖 | `cache`                                                                   | MCP 工具清單作業耗時，包括快取命中／未命中狀態。                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | 直方圖 |                                                                           | 未命中快取的 MCP 工具擷取耗時。                                                                |
| `mcp.tools.cache_write.duration_ms`    | 直方圖 |                                                                           | Codex 應用程式 MCP 工具快取的寫入耗時。                                                                    |
| `hooks.run`                            | 計數器   | `hook_name`、`source`、`status`                                           | 依掛勾名稱、來源和狀態區分的掛勾執行次數。                                                                 |
| `hooks.run.duration_ms`                | 直方圖 | `hook_name`、`source`、`status`                                           | 掛勾執行時間（毫秒）。                                                                               |

`mcp.call` 和 `mcp.call.duration_ms` 指標包含 `status`；一般工具呼叫所發出的資料也包含 `tool`，並會在可用時加入 `connector_id` 和 `connector_name`。遭封鎖的 Codex 應用程式 MCP 呼叫可能會發出 `mcp.call`，其中僅包含 `status`。

#### 對話串、任務和功能

| 指標                            | 類型      | 欄位                | 說明                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | 計數器   | `feature`、`value`    | 與預設值不同的功能值（針對每個非預設值發出一列）。         |
| `status_line`                     | 計數器   |                       | 啟動使用已設定狀態列的工作階段。                                   |
| `model_warning`                   | 計數器   |                       | 傳送至模型的警告。                                                       |
| `thread.started`                  | 計數器   | `is_git`              | 建立新的對話串，並標記工作目錄是否位於 Git 程式碼庫中。    |
| `conversation.turn.count`         | 計數器   |                       | 每個對話串的使用者/助理輪次，於對話串結束時記錄。              |
| `thread.fork`                     | 計數器   | `source`              | 從現有對話串分支建立新的對話串。                                |
| `thread.rename`                   | 計數器   |                       | 對話串已重新命名。                                                                  |
| `thread.side`                     | 計數器   | `source`              | 已建立支線對話。                                                       |
| `thread.skills.enabled_total`     | 直方圖 |                       | 為新對話串啟用的技能數量。                                       |
| `thread.skills.kept_total`        | 直方圖 |                       | 提示詞轉譯後保留的已啟用技能數量。                            |
| `thread.skills.truncated`         | 直方圖 |                       | 技能轉譯是否截斷已啟用的技能清單（`1` 或 `0`）。          |
| `task.compact`                    | 計數器   | `type`                | 各類型（`remote` 或 `local`）的壓縮次數，包括手動與自動壓縮。 |
| `task.review`                     | 計數器   |                       | 觸發的審查次數。                                                     |
| `task.undo`                       | 計數器   |                       | 觸發的復原操作次數。                                                |
| `task.user_shell`                 | 計數器   |                       | 使用者 shell 操作的次數（例如 TUI 中的 `!`）。                       |
| `shell_snapshot`                  | 計數器   | 請參閱附註              | 是否成功建立 shell 快照。                                       |
| `shell_snapshot.duration_ms`      | 直方圖 | `success`             | 建立 shell 快照所需的時間。                                                   |
| `skill.injected`                  | 計數器   | `status`、`skill`     | 依技能區分的技能注入結果。                                               |
| `plugins.startup_sync`            | 計數器   | `transport`、`status` | 啟動時同步精選外掛程式的嘗試次數。                                            |
| `plugins.startup_sync.final`      | 計數器   | `transport`、`status` | 啟動時同步精選外掛程式的最終結果。                                       |
| `multi_agent.spawn`               | 計數器   | `role`                | 依角色區分的智慧體啟動次數。                                                            |
| `multi_agent.resume`              | 計數器   |                       | 智慧體恢復執行次數。                                                                   |
| `multi_agent.nickname_pool_reset` | 計數器   |                       | 智慧體暱稱集區重設次數。                                                      |

`shell_snapshot` 指標包含 `success`，失敗時還會包含 `failure_reason`。

#### 記憶與本機狀態

| 指標                         | 類型      | 欄位                    | 說明                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | 計數器   | `status`                  | 記憶第 1 階段的作業數量，依狀態區分。                      |
| `memory.phase1.e2e_ms`         | 直方圖 |                           | 記憶第 1 階段的端對端執行時間。                   |
| `memory.phase1.output`         | 計數器   |                           | 記憶第 1 階段寫入的輸出數量。                           |
| `memory.phase1.token_usage`    | 直方圖 | `token_type`              | 記憶第 1 階段的 Token 用量，依 Token 類型區分。                 |
| `memory.phase2`                | 計數器   | `status`                  | 記憶第 2 階段的作業數量，依狀態區分。                      |
| `memory.phase2.e2e_ms`         | 直方圖 |                           | 記憶第 2 階段的端對端執行時間。                   |
| `memory.phase2.input`          | 計數器   |                           | 記憶第 2 階段的輸入數量。                               |
| `memory.phase2.token_usage`    | 直方圖 | `token_type`              | 記憶第 2 階段的 Token 用量，依 Token 類型區分。                 |
| `memories.usage`               | 計數器   | `kind`, `tool`, `success` | 記憶使用次數，依種類、工具及成功或失敗區分。          |
| `external_agent_config.detect` | 計數器   | 請參閱附註                  | 外部智慧體設定的偵測次數，依遷移項目類型區分。  |
| `external_agent_config.import` | 計數器   | 請參閱附註                  | 外部智慧體設定的匯入次數，依遷移項目類型區分。     |
| `db.backfill`                  | 計數器   | `status`                  | 初始狀態 DB 回填結果（`upserted`、`failed`）。 |
| `db.backfill.duration_ms`      | 直方圖 | `status`                  | 初始狀態 DB 回填的執行時間。                |
| `db.error`                     | 計數器   | `stage`                   | 狀態 DB 作業期間的錯誤數量。                        |

`external_agent_config.detect` 和 `external_agent_config.import` 指標包含 `migration_type`；技能遷移也包含 `skills_count`。

#### Windows 沙盒

| 指標                                           | 類型      | 欄位                                    | 說明                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | 計數器   | `originator`, `mode`                      | Windows 沙盒設定成功次數。                      |
| `windows_sandbox.setup_failure`                  | 計數器   | `originator`, `mode`                      | Windows 沙盒設定失敗次數。                       |
| `windows_sandbox.setup_duration_ms`              | 直方圖 | `result`, `originator`, `mode`            | Windows 沙盒設定所需時間。                       |
| `windows_sandbox.elevated_setup_success`         | 計數器   |                                           | 提升權限的 Windows 沙盒設定成功次數。             |
| `windows_sandbox.elevated_setup_failure`         | 計數器   | 請參閱附註                                  | 提升權限的 Windows 沙盒設定失敗次數。              |
| `windows_sandbox.elevated_setup_canceled`        | 計數器   | 請參閱附註                                  | 已取消的提升權限 Windows 沙盒設定嘗試次數。     |
| `windows_sandbox.elevated_setup_duration_ms`     | 直方圖 | `result`                                  | 提升權限的 Windows 沙盒設定所需時間。              |
| `windows_sandbox.elevated_prompt_shown`          | 計數器   |                                           | 提升權限沙盒設定提示的顯示次數。                  |
| `windows_sandbox.elevated_prompt_accept`         | 計數器   |                                           | 提升權限沙盒設定提示的接受次數。               |
| `windows_sandbox.elevated_prompt_use_legacy`     | 計數器   |                                           | 使用者在提升權限提示中選擇舊版沙盒的次數。   |
| `windows_sandbox.elevated_prompt_quit`           | 計數器   |                                           | 使用者在提升權限提示中選擇退出的次數。                   |
| `windows_sandbox.fallback_prompt_shown`          | 計數器   |                                           | 已顯示沙盒備援提示。                        |
| `windows_sandbox.fallback_retry_elevated`        | 計數器   |                                           | 使用者在備援提示中重新嘗試提升權限的設定。 |
| `windows_sandbox.fallback_use_legacy`            | 計數器   |                                           | 使用者在備援提示中選擇舊版沙盒。   |
| `windows_sandbox.fallback_prompt_quit`           | 計數器   |                                           | 使用者從備援提示中退出。                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | 計數器   | 請參閱備註                                  | 舊版 Windows 沙盒設定預檢失敗。       |
| `windows_sandbox.setup_elevated_sandbox_command` | 計數器   |                                           | 已叫用提升權限的沙盒設定指令。               |
| `windows_sandbox.createprocessasuserw_failed`    | 計數器   | `error_code`, `path_kind`, `exe`, `level` | Windows `CreateProcessAsUserW` 失敗。              |

提升權限設定失敗的指標在可取得 Windows 設定失敗詳細資料時，會包含 `code` 和 `message`；若由共用設定路徑發出，也可能包含 `originator`。`windows_sandbox.legacy_setup_preflight_failed` 指標若由共用設定路徑發出，則會包含 `originator`；但從備援提示觸發的預檢失敗可能不含任何欄位。

### 意見回饋控制

本機用戶端預設允許使用者透過 `/feedback` 傳送意見回饋。若要在某部電腦上全面停用 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能的意見回饋收集，請更新組態：

```toml
[feedback]
enabled = false

停用後，`/feedback` 會顯示停用訊息，Codex 也會拒絕提交意見回饋。

### 隱藏或顯示推理事件

如果想減少冗雜的「推理」輸出，例如 CI 紀錄中的輸出，可以將其隱藏：

```toml
hide_agent_reasoning = true

如果希望在模型發出原始推理內容時顯示該內容：

```toml
show_raw_agent_reasoning = true

僅在工作流程允許時，才啟用原始推理。某些模型或供應商，例如 `gpt-oss`，不會發出原始推理；在這種情況下，此設定不會產生任何可見效果。

## 通知

使用 `notify`，即可在 Codex 發出支援的事件時觸發外部程式，目前僅支援 `agent-turn-complete`。這適合用於桌面快顯通知、聊天 Webhook、CI 更新，或透過內建 TUI 通知未涵蓋的其他管道發出警示。

```toml
notify = ["python3", "/path/to/notify.py"]

以下是 `notify.py` 範例（已省略部分內容），用於回應 `agent-turn-complete`：

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

此指令碼會接收單一 JSON 引數。常見欄位包括：

- `type`（目前為 `agent-turn-complete`）
- `thread-id`（工作階段識別碼）
- `turn-id`（輪次識別碼）
- `cwd`（工作目錄）
- `input-messages`（促成該輪次的使用者訊息）
- `last-assistant-message`（最後一則助理訊息的文字）

將指令碼存放在磁碟上的某個位置，並將 `notify` 指向該指令碼。

#### `notify` 與 `tui.notifications` 的比較

- `notify` 會執行外部程式，適合用於 Webhook、桌面通知程式和 CI 掛勾。
- `tui.notifications` 內建於 TUI，並可選擇依事件類型進行篩選，例如 `agent-turn-complete` 和 `approval-requested`。
- `tui.notification_method` 控制 TUI 發出終端通知的方式：`auto`、`osc9` 或 `bel`。
- `tui.notification_condition` 控制 TUI 通知是僅在
  終端處於 `unfocused` 狀態時觸發，還是設為 `always`，一律觸發。

在 `auto` 模式下，Codex 會優先使用 OSC 9 通知；這是一種終端逸出序列，部分終端會將其解讀為桌面通知。否則，Codex 會改用 BEL（`\x07`）。

如需確切的組態鍵，請參閱 [組態參考資料](/zh-Hant/codex/config-file/config-reference)。

## 歷史記錄保存

Codex 預設會將本機工作階段記錄儲存在 `CODEX_HOME` 下，例如 `~/.codex/history.jsonl`。若要停止保存本機歷史記錄：

```toml
[history]
persistence = "none"

若要限制歷史記錄檔的大小，請設定 `history.max_bytes`。檔案超過上限時，Codex 會移除最舊的項目並壓縮檔案，同時保留最新記錄。

```toml
[history]
max_bytes = 104857600 # 100 MiB

## 可點選的引用

如果使用支援此功能的終端或編輯器整合，Codex 可將檔案引用呈現為可點選的連結。設定 `file_opener` 以選擇 Codex 使用的 URI 配置：

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

例如，像 `/home/user/project/main.py:42` 這樣的引用可改寫成可點選的 `vscode://file/...:42` 連結。

## 探索專案指示

Codex 會讀取 `AGENTS.md` 及相關檔案，並在工作階段的第一輪納入有限量的專案指引。以下兩項設定可控制其運作方式：

- `project_doc_max_bytes`：要從每個 `AGENTS.md` 檔案讀取多少內容
- `project_doc_fallback_filenames`：在某一目錄層級找不到 `AGENTS.md` 時，要嘗試的其他檔名

如需詳細操作說明，請參閱 [使用 AGENTS.md 自訂指示](/zh-Hant/codex/agent-configuration/agents-md)。

## 桌面版

本節選項僅適用於 ChatGPT 桌面版應用程式。

### 新增自訂檔案處理常式

請在使用者層級的 `~/.codex/config.toml` 中，於
`desktop.custom_file_handlers` 下新增項目，即可使用 ChatGPT 桌面版應用程式預設不支援的編輯器或內部啟動器
開啟檔案。每個項目都會新增一個
編輯器目標，並將其加入應用程式的 **開啟方式** 選單。當
`command` 是現有的絕對路徑，或可透過應用程式的 `PATH` 解析時，應用程式便會列出該目標。

下列範例展示將檔案傳遞給處理常式的三種方式：

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

儲存 `config.toml`，然後重新啟動 ChatGPT 桌面版應用程式。

處理常式 ID 是 TOML 表格標頭的最後一個區段。其長度必須介於
1–64 個字元，並以 ASCII 字母或數字開頭；其餘部分只能包含
ASCII 字母、數字、句點、底線或連字號。應用程式對外提供的
ID 會帶有 `custom:` 前綴；例如，`company_editor` 會變成
`custom:company_editor`。若 ID 包含句點，請以引號括住，以免 TOML
將其解讀為巢狀表格。例如：

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

每個處理常式都支援以下欄位：

| 欄位          | 必填 | 說明                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | 是      | 應用程式中的顯示名稱。                                                                                                                                                 |
| `icon`         | 是      | 隨附的應用程式圖示（例如 `apps/vscode.png`）、base64 `data:image/...` URL、`file:` URI，或本機影像的絕對路徑。不支援的來源會使用預設的 VS Code 圖示。 |
| `command`      | 是      | 用於偵測及啟動的可執行檔路徑或指令名稱。                                                                                                                    |
| `args`         | 否       | 插入於 `command` 與檔案輸入之間的字串陣列。預設為 `[]`。                                                                                            |
| `input`        | 否       | 應用程式傳送檔案輸入的方式：`path`、`json_argument` 或 `json_stdin`。預設為 `path`。                                                                              |
| `supports_ssh` | 否       | 是否為 SSH 工作區中的檔案提供此處理常式。預設為 `false`。處理常式需要遠端主機與路徑詳細資料時，請使用 `json_stdin`。                     |

`input` 的值會控制 `args` 後面接續的內容：

- `path` 會將路徑附加為指令的最後一個引數。
- `json_argument` 會附加一個 JSON 物件，其中包含 `target`、`path`、`appPath` 與
`location`。`location` 的值是物件，其中 `line` 與
`column` 的值皆從 1 起算；也可以是 `null`。
- `json_stdin` 會將 JSON 物件寫入標準輸入，而非新增
  引數。它還包含 `hostConfig`、`remoteWorkspaceRoot` 與
`remotePath`；這些欄位不適用時，其值為 `null`。

例如，`company_editor` 可在使用者開啟某個
特定的原始碼位置時接收此引數：

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

將自訂處理常式選為偏好的編輯器後，系統會以與選取內建編輯器相同的
方式保留這項選擇，包括各專案的偏好設定。

## TUI 選項

執行 `codex` 時若未指定子指令，即會啟動互動式終端使用者介面（TUI）。Codex 在 `[tui]` 區段下提供一些 TUI 專用組態，包括：

- `tui.notifications`：啟用或停用通知（或限制為特定類型）
- `tui.notification_method`：選擇 `auto`、`osc9` 或 `bel` 作為終端通知方式
- `tui.notification_condition`：選擇 `unfocused` 或 `always`，決定何時
  觸發通知
- `tui.animations`：啟用或停用 ASCII 動畫與微光效果
- `tui.alternate_screen`：控制替代畫面的使用方式（設為 `never` 可保留終端回捲記錄）
- `tui.show_tooltips`：顯示或隱藏歡迎畫面上的新手引導工具提示

`tui.notification_method` 預設為 `auto`。在 `auto` 模式下，若終端似乎支援 OSC 9 通知（部分終端會將這種終端逸出序列解讀為桌面通知），Codex 會優先使用這類通知；否則會改用 BEL（`\x07`）。

如需完整的組態鍵清單，請參閱 [組態參考資料](/zh-Hant/codex/config-file/config-reference)。
