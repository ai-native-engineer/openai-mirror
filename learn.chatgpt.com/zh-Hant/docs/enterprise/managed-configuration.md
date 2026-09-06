<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/managed-configuration -->

受管理的設定可控制 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中，所涵蓋功能支援的本機執行階段行為。支援的要求可能因用戶端和版本而異。受管理的設定不會授予 ChatGPT 工作區存取權、指派席位，也不會取代工作區的角色型存取控制 (RBAC)。如要管理工作區功能的存取權，請參閱[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)；如要管理本機執行階段政策，請參閱本頁。

企業管理員可以透過兩種方式控制受支援的本機用戶端行為：

- **要求**：由管理員強制執行、使用者無法覆寫的限制。
- **受管理的預設值**：受支援的用戶端啟動時套用的初始值。使用者仍可在執行期間變更設定；用戶端下次啟動時會重新套用受管理的預設值。

## 管理員強制執行的要求（requirements.toml）

要求會限制涉及安全性的設定，包括核准政策、核准審查者、自動審查政策、沙盒模式、權限設定檔、網頁搜尋模式、受管理的掛勾、使用者可啟用哪些 MCP 伺服器，以及對於使用者自行設定的外掛程式市集來源，使用者可新增哪些來源、從哪些來源安裝外掛程式，或重新整理哪些來源。解析組態時（例如來自 `config.toml`、[設定檔](/zh-Hant/codex/config-file/config-advanced#profiles)或 CLI 組態覆寫的設定），如果某個值與強制規則衝突，本機用戶端會改用相容的值並通知使用者。如果設定了 `mcp_servers` 允許清單，只有 MCP 伺服器的名稱和身分都符合已核准的項目時，用戶端才會啟用該伺服器；否則會將其停用。

要求也可以透過 `requirements.toml` 中的 `[features]` 資料表限制[功能旗標](/zh-Hant/codex/config-file/config-basic/#feature-flags)。功能不一定涉及安全性，但企業可視需要固定其設定值。省略的鍵不受限制。

在 Codex 0.138.0 或更新版本中，請優先使用[權限設定檔](/zh-Hant/codex/permissions)
搭配 `allowed_permission_profiles` 和受管理的 `default_permissions`。
只有仍設定 `sandbox_mode` 的舊版部署，
才應使用 `allowed_sandbox_modes`。

如需確切的鍵清單，請參閱[《組態參考資料》中的 `requirements.toml` 章節](/zh-Hant/codex/config-file/config-reference#requirementstoml)。

### 位置與優先順序

每個受支援的本機用戶端都會依優先順序由低到高整合要求：

1. 系統 `requirements.toml`（在 Unix 系統上為 `/etc/codex/requirements.toml`，
   包括 Linux 和 macOS；
   在 Windows 上則為 `%ProgramData%\OpenAI\Codex\requirements.toml`）。
2. 透過雲端組態套件提供、由企業管理的要求。
3. 本機用戶端會重新解譯為要求的舊版 `managed_config.toml` 欄位。
4. 透過 `com.openai.codex:requirements_toml_base64` 提供的
macOS 受管理偏好設定（MDM）。

優先順序較高的層級會覆寫較低層級的一般純量和清單值。
資料表會依鍵合併；規則、掛勾和檔案系統限制等要求，
則各有其欄位專屬的整合方式。請參閱
[`requirements.toml` 參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)
以確認目前的結構描述，
不要假設所有欄位都以相同方式合併。

為維持向後相容性，受支援的本機用戶端會將舊版
`approval_policy`、`approvals_reviewer` 和 `sandbox_mode` 欄位重新解譯為要求。
這項轉換會在必要時新增相容性選項；
如需明確指定允許清單，請使用 `requirements.toml`。

### 雲端管理的要求

使用者透過 ChatGPT 登入且使用支援的方案時，
受支援的本機用戶端可接收與工作區相關聯、由管理員強制執行的要求。
這是用來傳遞與 `requirements.toml` 相容之政策的管道。
它不會授予工作區存取權，也不會取代工作區 RBAC。

請開啟[受管理的設定](https://chatgpt.com/codex/settings/managed-configs)
以建立並指派雲端管理的要求。例如，這項政策會限制
核准與沙盒選項，並在受支援的 Shell 進入點執行前
提示使用者：

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

請確認每個受管理的用戶端版本都支援您選擇的鍵，並在指派給整個組織前，先以小型群組測試政策。請參閱組態參考資料以確認目前的結構描述，並透過管理介面確認目前的指派行為。

此服務會選取適用於已登入身分、由企業管理的要求層級。
本機用戶端會將這些層級與
[位置與優先順序](#locations-and-precedence)所述的其他要求來源一併評估。
請使用目前的管理介面，在工作區端建立及指派要求。
請勿依賴複製而來的群組比對演算法；
這項行為由管理服務負責，且可獨立於
本機要求格式而變更。

如需支援的鍵與範例，請參閱
[requirements.toml 範例](#example-requirementstoml)及
[`requirements.toml` 參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)。

#### 本機用戶端如何套用雲端管理的要求

使用者啟動受支援的本機用戶端，並透過 ChatGPT 登入且使用支援的方案時，用戶端會先檢查是否有有效且與身分相符的快取項目。若沒有有效項目，用戶端會擷取適用的套件，並在必要時重試，成功後寫入已簽署的快取項目。若請求失敗或逾時，且沒有可用的有效快取，雲端組態套件的載入作業會傳回錯誤，而不會在缺少雲端管理的要求層級時，逕自啟動而不告知使用者。

完成快取解析後，用戶端會將雲端要求與前述其他要求層級整合。背景重新整理可更新快取，供後續啟動時使用；但不會取代目前處理程序已載入的要求。

### 確認管理員與員工的使用體驗

為每項受管理的政策指定負責人，記錄應接收該政策的使用者或群組，並記載對檔案系統、網路、核准或權限設定檔施加任何限制的業務理由。

擴大部署範圍前，請找一位具代表性的使用者，測試已核准的工作流程和刻意禁止的工作流程。請確認受支援用戶端中實際生效的設定，不要假設僅憑工作區角色或群組即可強制執行本機限制。

### requirements.toml 範例

此範例會封鎖 `--ask-for-approval never` 和 `--sandbox danger-full-access`（包括 `--yolo`）：

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### 停用應用程式快照

若要為受管理的使用者停用應用程式快照，請設定頂層 `allow_appshots` 要求：

```toml
allow_appshots = false

在應用程式快照可用的情況下，`allow_appshots = false` 會停用這項功能。
若省略此鍵，要求便不會限制應用程式快照，
並會套用一般的產品可用性檢查。App Server 用戶端若透過
`configRequirements/read` 讀取實際生效的要求，會以
`allowAppshots` 接收相同的限制；若省略 `allowAppshots` 或將其值設為 `null`，
則不會停用應用程式快照。

### 停用裝置遠端控制

若要為受管理的使用者停用[裝置遠端控制](/zh-Hant/codex/remote-connections#pick-up-work-from-another-device)，
請設定頂層 `allow_remote_control` 要求：

```toml
allow_remote_control = false

在支援裝置遠端控制的情況下，`allow_remote_control = false` 會停用這項功能。
若省略此鍵，要求便不會限制裝置遠端控制，
並會套用一般的產品可用性檢查。
此要求不會停用 SSH 遠端連線。

### 控制可用的權限設定檔

請使用 `allowed_permission_profiles` 控制使用者可以選擇哪些內建與自訂的
[權限設定檔](/zh-Hant/codex/permissions)。
它對權限設定檔的作用，相當於 `allowed_sandbox_modes` 對沙盒模式的作用；
請依使用者選擇權限的方式，使用對應的允許清單。

權限設定檔允許清單需要 Codex 0.138.0 或更新版本。
Codex 0.137.0 和更舊版本會忽略 `allowed_permission_profiles`
和受管理的 `default_permissions`。

只有在每個受管理的用戶端都執行支援此功能的版本後，才能使用下列權限設定檔範例。所有用戶端完成升級之前，請勿部署受管理的自訂設定檔。

此資料表存在時，即代表允許使用的完整設定檔清單。
設為 `true` 的設定檔會獲准；省略或設為 `false` 的設定檔會遭拒，
包括未來 Codex 版本新增的內建設定檔。

#### 允許標準設定檔

此政策允許唯讀存取權和工作區存取權，但不允許完整存取權：

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### 新增受管理的最小權限預設值

管理員可以在同一個要求來源中定義自訂設定檔。
請使用組織專屬的設定檔名稱，
避免與使用者已載入組態中的名稱衝突。
自訂名稱不能以 `:` 開頭，也不能使用保留名稱 `filesystem`。

請勿將受管理的自訂設定檔部署至執行 Codex 0.137.0 或更舊版本的用戶端。這些用戶端可辨識設定檔資料表，卻無法辨識用來選取該設定檔的受管理預設值。

例如：

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### 僅允許企業定義的設定檔

如果使用者只能選擇管理員定義的設定檔，請省略所有內建設定檔：

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

即使使用者不能直接選擇內建的 `:workspace` 設定檔，
自訂設定檔仍可擴充 `:workspace`。

#### 停用其他來源允許的設定檔

權限允許清單會依設定檔名稱合併。
由於雲端要求的優先順序高於系統要求，因此雲端要求可使用 `false`
停用系統檔案允許的設定檔。

雲端要求：

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

系統要求：

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

請將 `default_permissions` 明確設為允許的設定檔。
若省略此設定，只有在 `:workspace` 和
`:read-only` 都已明確獲准時，本機執行階段才會預設使用 `:workspace`。
當 `allowed_permission_profiles` 不存在時，受管理的要求不會限制使用者可以選擇的設定檔名稱。
每個項目都必須指定內建設定檔，或在已載入的組態或要求來源中
定義的自訂設定檔。請在受管理的要求中定義自訂設定檔，
以集中控制其行為。

### 依主機覆寫沙盒要求

如果同一項受管理的政策需要在不同主機上套用不同的沙盒要求，
請使用 `[[remote_sandbox_config]]`。例如，可為筆記型電腦保留較嚴格的預設值，
同時允許符合條件的開發機器或 CI 執行器寫入工作區。
目前，主機專屬項目只會覆寫 `allowed_sandbox_modes`：

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

本機執行階段會盡可能解析主機名稱，
再將每個 `hostname_patterns` 項目與該名稱比對。它會優先使用完整限定網域名稱，
若無法取得則改用本機主機名稱。比對不區分大小寫；
`*` 可比對任意字元序列，`?` 則可比對單一字元。

在同一個要求來源中，以第一個相符的 `[[remote_sandbox_config]]` 項目為準。
如果沒有相符項目，本機執行階段會保留頂層的 `allowed_sandbox_modes`。
主機名稱比對僅用於選擇政策；
請勿將其視為經過驗證的裝置身分證明。

您也可以限制網頁搜尋模式：

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` 僅允許 `"disabled"`。
例如，設定 `allowed_web_search_modes = ["cached"]` 後，即使在 `danger-full-access` 工作階段中，也無法進行即時網頁搜尋。

### 設定網路存取要求

  `[experimental_network]` 屬於實驗性功能，且可能變更。請先在使用者實際使用的
  本機用戶端版本和作業系統上驗證這些要求，
  再於企業部署中廣泛啟用。Windows 支援
  目前仍有限；除非已在您的環境中完成測試，
  否則請避免將這項政策套用至 Windows 使用者。

管理員需要集中定義網路存取要求時，請使用 `requirements.toml` 中的 `[experimental_network]`。
這些要求與使用者的 `features.network_proxy` 切換設定
彼此獨立：即使未啟用該功能旗標，也能設定沙盒網路，
但若目前使用的沙盒停用網路，這些要求不會授予指令
網路存取權。請設定
`experimental_network.enabled = true` 以啟用受管理的代理伺服器；
僅設定網域規則並不會啟用代理伺服器。

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

只有在您同時於 `[experimental_network.domains]` 中
定義由管理員控管的 `"allow"` 項目，
且希望僅允許這些規則時，才使用 `experimental_network.managed_allowed_domains_only = true`。
若設為 `true` 卻未設定受管理的允許規則，使用者新增的網域允許規則
將不再生效。請勿將標準的 `domains` 對應表與舊版的
`allowed_domains` 或 `denied_domains` 清單混用。

`*.example.com` 僅比對子網域。`**.example.com` 會比對根網域
及其子網域。符合的拒絕規則優先於允許規則。

網域語法、本機／私人目的地規則、拒絕優先於允許的行為，
以及 DNS 重新繫結限制，皆與
[智慧體核准與安全性](/zh-Hant/codex/agent-approvals-security#network-isolation)中說明的沙盒網路行為相同。

代理伺服器會導送在沙盒內執行的本機指令流量。瀏覽器工具也會在存取來源前，檢查受管理的網路拒絕規則與排他性允許清單；這是獨立的政策檢查，並非透過指令代理伺服器導送瀏覽器流量。代理伺服器不會篩選網頁搜尋、應用程式與連接器、MCP 伺服器、原生應用程式流量、Codex 服務請求或 Codex 雲端流量。請針對各項功能使用對應的控制措施：

- 使用 `allowed_web_search_modes` 限制網頁搜尋。
- 使用 `features.apps = false` 停用應用程式和連接器整合，並在支援的情況下
使用 `features.plugins = false` 停用外掛程式。
- 使用受管理的 `mcp_servers` 核准清單，限制 MCP 伺服器。
- 使用 `browser_use`、`in_app_browser` 和
`computer_use` 等功能要求，限制瀏覽器與電腦功能。
- 在雲端環境設定中設定 Codex 雲端的網路存取權。

指令網域允許清單無法取代上述各項功能專屬的控制措施。

### 控制瀏覽器與電腦功能

使用 `requirements.toml` 中的 `[browser_use]` 和 `[computer_use]` 資料表，
限制支援的桌面用戶端。請在部署環境使用的用戶端版本
和作業系統上驗證政策。設定允許規則並不會
安裝外掛程式、授予作業系統權限，或核准
仍須審查的動作。

若要控制瀏覽器存取權，請設定來源政策。來源包含通訊協定、
主機及選填的連接埠，例如 `https://example.com` 或
`https://*.example.com:8443`。請勿包含路徑、查詢字串或片段。
與指令網路的網域規則不同，瀏覽器來源規則會區分 HTTP 和 HTTPS，
並比對連接埠。

此範例將瀏覽器存取範圍限制在已核准的網站，並禁止在該網站上傳檔案及使用完整的 Chrome DevTools Protocol (CDP) 存取權：

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

符合的來源規則會逐一依欄位判定。符合的拒絕規則優先；對於符合規則未指定的欄位，則由預設來源政策提供值。本機組態可以增加限制，但無法放寬受管理的拒絕規則。網路拒絕規則與排他性的受管理網路允許清單仍然適用。

設定 `browser_use.disable_auto_review = true` 可停用瀏覽器動作的
自動核准審查；也可以在來源政策中設定 `auto_review = "deny"`，
限制該來源的自動核准審查。這項設定控制的是核准處理方式，
不會停用模型安全監控。

針對原生應用程式，請設定預設存取政策並指定允許的應用程式。例如，以下 macOS 政策允許使用「計算機」，並禁止儲存核准決定：

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Windows 政策可以使用
`computer_use.windows.aumids` 識別封裝的應用程式，或使用
`computer_use.windows.exes` 識別可執行檔。可執行檔規則必須包含 `publisher_name`、
`product_name` 和 `access`；`binary_name` 則為選填。請使用應用程式經過驗證的
身分識別資訊，不要僅使用顯示名稱。

完整欄位請參閱[組態參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)；
受管理 macOS 裝置的相關限制，
請參閱[鎖定時使用限制](#restrict-locked-computer-use)。

### 固定功能旗標

您也可以為收到受管理 `requirements.toml` 的使用者
固定[功能旗標](/zh-Hant/codex/config-file/config-basic/#feature-flags)：

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

請使用 `config.toml` 的 `[features]` 資料表中的標準功能鍵，設定
執行階段功能。本機執行階段會調整可辨識的功能，使其符合這些
固定設定，並拒絕將衝突的功能設定寫入 `config.toml`
或設定檔。

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` 會停用內建瀏覽器窗格。
- 在支援的情況下，`in_app_updates = false` 會於
  重新啟動時停用 ChatGPT 桌面版應用程式本身的更新程式。這不會影響外部套件部署，
  也不會延長舊版應用程式的支援期限。如需設定和推出作業的指引，請參閱
[管理應用程式更新](/zh-Hant/codex/enterprise/manage-app-updates)。
- `browser_use = false` 會停用瀏覽器中的電腦功能，並使瀏覽器智慧體無法使用。
- `browser_use_full_cdp_access = false` 會停用本機執行階段的完整 CDP 存取權，
  包括瀏覽器開發人員模式，並防止 ChatGPT 桌面版應用程式
  啟用對應設定。
- `browser_use_external = false` 會停用外部瀏覽器功能。
- `computer_use = false` 會停用電腦功能、錄製與重播，以及相關的
  安裝或設定流程。

如果省略這些鍵，政策會允許相關功能，但實際能否使用仍取決於用戶端、平台及功能推出情況。

### 限制鎖定狀態下的電腦使用

若要防止使用者在受管理的 Mac 上啟用[鎖定時使用](/zh-Hant/codex/computer-use#locked-use)，
請新增以下要求：

```toml
[computer_use]
allow_locked_computer_use = false

這項要求會移除啟用「鎖定時使用」的控制項，但若該功能已啟用，則不會將其關閉。如果省略這項要求，產品的一般提供狀況和使用者的本機設定仍然適用。

### 設定自動審查政策

使用 `allowed_approvals_reviewers` 要求或允許自動審查。將其
設為 `["auto_review"]` 可強制進行自動審查；若允許使用者
選擇手動核准，則加入 `"user"`。

設定 `guardian_policy_config`，以取代自動審查政策中
租用戶專屬的部分。本機執行階段仍會使用內建的審查者
範本和輸出合約。受管理的 `guardian_policy_config` 優先於
本機的 `[auto_review].policy`。

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### 強制執行禁止讀取要求

管理員可使用
`[permissions.filesystem]`，針對確切路徑或 glob 模式禁止讀取。使用者無法透過本機
組態放寬這些要求。

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

存在禁止讀取要求時，本機執行階段會拒絕完整存取權，
並讓本機執行維持在唯讀或工作區沙盒中，以便
強制執行這些要求。在原生 Windows 上，受管理的 `deny_read` 適用於直接操作檔案的
工具；Shell 子程序的讀取作業不適用這項沙盒規則。

### 透過要求強制執行受管理的掛勾

管理員也可以直接在 `requirements.toml` 中定義受管理的生命週期掛勾。
使用 `[hooks]` 設定掛勾本身，並將 `managed_dir` 指向
您的 MDM 或端點管理工具用來安裝
所參照指令碼的目錄。

若要對已在本機關閉掛勾的使用者也強制執行受管理的掛勾，請固定
`[features].hooks = true`，並搭配 `[hooks]`。若要略過使用者、專案、工作階段
和外掛程式的掛勾，同時仍允許受管理的掛勾，請設定
`allow_managed_hooks_only = true`。

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

注意事項：

- 本機執行階段會強制執行 `requirements.toml` 中的掛勾組態，
  但不會散發 `managed_dir` 中的指令碼。
- 請透過 MDM 或裝置管理解決方案散發這些指令碼。
- 受管理的掛勾指令應以絕對路徑參照指令碼，且指令碼應位於已設定的受管理目錄下。
- `allow_managed_hooks_only = true` 會略過來自使用者、專案、工作階段和
  外掛程式來源的掛勾，但仍會載入 `requirements.toml` 和其他
  受管理組態層中的掛勾。

### 透過要求強制執行指令規則

管理員也可以在 `requirements.toml` 中
使用 `[rules]` 資料表，強制執行限制性指令規則。這些規則會與一般的 `.rules` 檔案合併，且
仍以限制最嚴格的決策為準。

與 `.rules` 不同，要求中的規則必須指定 `decision`，而該決策
必須為 `"prompt"` 或 `"forbidden"`，不得為 `"allow"`。

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

若要限制本機用戶端可啟用的 MCP 伺服器，請新增 `mcp_servers`
核准清單。對於 stdio 伺服器，請比對 `command`；對於可串流 HTTP
伺服器，請比對 `url`：

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

`identity.command` 的字串形式只會比對已設定的 `command`，
不會檢查 `args`、`cwd`、`env` 或 `env_vars`。

若要限制完整的 stdio 呼叫，請比對可執行檔及每個位置引數：

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

可執行檔、引數數量和引數順序都必須相符。引數及 URL
規則支援 `exact`、`prefix` 和完整值的 `regex` 比對。結構化
指令規則仍不會檢查 `cwd`、`env` 或 `env_vars`。外掛程式隨附的
MCP 伺服器會在
`plugins.<plugin>.mcp_servers.<server>` 下使用相同的身分識別結構。

如果 `mcp_servers` 存在但內容為空，本機用戶端會停用所有 MCP 伺服器。

### 控制外掛程式可用性

若要在支援的本機用戶端中停用外掛程式，請在 `requirements.toml` 中將 `features.plugins`
設為 `false`：

```toml
features.plugins = false

此設定也適用於使用者以 API 金鑰登入 Codex 的情況。請參閱
[`features.plugins`
參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)，瞭解
支援的組態。

### 限制外掛程式市集來源

若要限制對使用者設定之市集來源的操作，請設定
`restrict_to_allowed_sources = true`，並定義一或多項來源規則：

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Git 規則會比對正規化的程式碼庫 URL；若有指定，還會比對完全相符的
`ref`。主機模式是用來比對小寫 Git 主機名稱的正規表示式；
若要比對完整主機名稱，請使用 `^` 和 `$`。本機規則要求使用
經過正規化的絕對路徑。請參閱 [`requirements.toml` 參考資料](/zh-Hant/codex/config-file/config-reference#requirementstoml)，
瞭解完整的結構描述和合併行為。

對於使用者設定的來源，這些要求會拒絕不符合規則的新增市集、安裝外掛程式，以及重新整理已設定 Git 市集等作業。由 Codex 管理的 OpenAI 市集，只要其來源和保留名稱相符，仍可使用。這些要求不會在執行階段篩選已設定的使用者市集或其中的外掛程式。

這些來源限制僅適用於支援外掛程式市集操作的本機用戶端：桌面 App 中的 ChatGPT 和 Codex，以及 Codex CLI。
這些限制不會控管網頁版或行動版 ChatGPT 中的外掛程式使用情形，也不會為 IDE 擴充功能新增外掛程式。

## 受管理的預設值（`managed_config.toml`）

受管理的預設值會決定支援的本機用戶端啟動時使用的組態。
啟動時，這些預設值會覆寫使用者的本機 `config.toml`，以及任何 CLI `--config`
覆寫值。使用者仍可在本次執行期間變更這些設定，
但用戶端下次啟動時會再次套用預設值。

如果受管理的預設值、macOS MDM 設定檔或已儲存的組態，為使用 ChatGPT 登入的使用者指定了 `gpt-5.4`
或 `gpt-5.4-mini`，請在 2026 年 8 月 31 日之前更新。將 `gpt-5.4` 替換為 `gpt-5.6-terra`，並將 `gpt-5.4-mini` 替換為
`gpt-5.6-luna`。OpenAI API 和使用你自己的 API 金鑰進行驗證的 Codex
不受影響。請參閱[工作區模型
可用性](/zh-Hant/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement)。

請確保受管理的預設值符合你的要求；本機執行階段會拒絕不允許的值。

### 優先順序與分層

本機執行階段會依下列順序組合出實際生效的組態（上層覆寫下層）：

- 受管理的偏好設定（macOS MDM；優先順序最高）
- `managed_config.toml`（系統／受管理的檔案）
- `config.toml`（使用者的基礎組態）

CLI `--config key=value` 的覆寫值會套用至基礎組態，但受管理的設定層會覆寫這些值。這表示即使你提供本機旗標，每次執行仍會從受管理的預設值開始。

雲端管理的要求會影響要求層，而非受管理的預設值。優先順序請參閱上方「管理員強制執行的要求」一節。

### 位置

- Linux/macOS（Unix）：`/etc/codex/managed_config.toml`
- Windows／非 Unix：`~/.codex/managed_config.toml`

如果檔案不存在，本機執行階段會略過受管理的設定層。

### macOS 受管理的偏好設定（MDM）

在 macOS 上，管理員可以推送裝置設定檔，在下列位置提供以 base64 編碼的 TOML 承載資料：

- 偏好設定網域：`com.openai.codex`
- 索引鍵：
  - `config_toml_base64`（受管理的預設值）
  - `requirements_toml_base64`（要求）

本機執行階段會將這些「受管理的偏好設定」承載資料解析為 TOML。
對於受管理的預設值（`config_toml_base64`），受管理的偏好設定
具有最高優先順序。對於要求（`requirements_toml_base64`），優先順序則遵循
上述雲端管理要求的順序。
要求端的 `[features]` 表格也適用於 `requirements_toml_base64`；
其中同樣應使用標準功能索引鍵。

### MDM 設定工作流程

本機執行階段支援標準 macOS MDM 承載資料，因此你可以透過
`Jamf Pro`、`Fleet` 或 `Kandji` 等工具分發設定。
簡易部署流程如下：

1. 建立受管理的 TOML 承載資料，並使用 `base64` 編碼（不換行）。
2. 將字串放入 MDM 設定檔中 `com.openai.codex` 網域下的 `config_toml_base64`（受管理的預設值）或 `requirements_toml_base64`（要求）。
3. 推送設定檔後，請使用者重新啟動支援的本機用戶端，並確認啟動時的組態摘要顯示受管理的設定值。
4. 撤銷或變更政策時，請更新受管理的承載資料；用戶端會在下次啟動時讀取更新後的偏好設定。

避免在承載資料中嵌入機密資訊或頻繁變動的動態值。受管理的 TOML 應與其他 MDM 設定一樣納入變更控制。

### managed\_config.toml 範例

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### 建議的防護措施

- 對大多數使用者，建議優先使用 `workspace-write` 並搭配核准機制；完整存取權僅保留給受控容器。
- 除非安全性審查允許使用收集器或存取工作流程所需的網域，否則請維持 `network_access = false`。
- 使用受管理的設定固定 OTel 設定（匯出器、環境），但除非政策明確允許儲存提示詞內容，否則請維持 `log_user_prompt = false`。
- 定期稽核本機 `config.toml` 與受管理政策之間的差異，以偵測設定漂移；受管理的設定層應優先於本機旗標和檔案。
