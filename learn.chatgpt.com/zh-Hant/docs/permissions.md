<!-- source: https://learn.chatgpt.com/zh-Hant/docs/permissions -->

Beta 版。權限設定檔仍在積極開發中，可能會變更。

  權限設定檔不可與舊版沙盒設定併用。請設定
  `default_permissions` 和 `[permissions]`，或 `sandbox_mode` /
`sandbox_workspace_write`，兩者不可併用。如果 `sandbox_mode` 出現在任何
  已載入的設定檔中、您傳入 `--sandbox`，或選取的組態設定檔設定了
`sandbox_mode`，Codex 就會使用這些舊版沙盒設定，而非
`default_permissions`。

受管理的 `allowed_permission_profiles` 是例外：它會讓 Codex 使用
權限設定檔。請移除
`sandbox_mode` 和 `[sandbox_workspace_write]` 等舊版設定，再部署受管理的
設定檔允許清單。若企業採用混合版本部署，可以暫時保留
受管理的 `allowed_sandbox_modes` 要求，作為相容性
限制，直到所有用戶端都執行 Codex 0.138.0 或更新版本。

權限設定檔可讓您對 Codex 代為執行的本機指令套用最低權限界限。
設定檔是一項具名原則，結合檔案系統規則與網路規則：前者定義指令
可讀取或寫入的內容，後者定義指令
可連線的目的地。

  設定檔中的 `network.enabled = true` 允許指令存取網路，但
  不會啟動網路代理伺服器。若要強制執行設定檔的網域規則，還須將
`features.network_proxy = true` 設定於 `config.toml` 中，或採用已啟用、
  由管理員管理的 `[experimental_network]` 要求。如果沒有作用中的
  代理伺服器，設定檔的網域規則就不會限制直接網路存取。

使用設定檔可為 Codex 提供目前對話所需的足夠存取權，而不必授予
對您電腦或網路的廣泛存取權。例如，唯讀設定檔可讓
Codex 檢查專案但不能編輯，而可寫入的設定檔則可將編輯範圍
限制於所選工作區根目錄。

本機權限設定檔支援 macOS、Linux、WSL 和原生
Windows。請參閱 [範圍與強制執行](#scope-and-enforcement)，了解各平台的
詳細資訊與注意事項。

如需 Codex 雲端的網路設定，請參閱 [網際網路存取](/zh-Hant/codex/cloud/internet-access)。

## 定義並選取設定檔

Codex 提供三個內建權限設定檔：

- `:read-only` 會將本機執行的指令限制為唯讀。
- `:workspace` 允許在作用中的工作區根目錄及系統暫存目錄中寫入。
- `:danger-full-access` 會解除本機沙盒限制，只有在有意授予這類廣泛存取權時
  才應使用。

在 `[permissions.<name>]` 下建立具名設定檔，然後將頂層
`default_permissions` 鍵設為該設定檔名稱或上述任一內建值。
在此範例中，`project-edit` 是使用者定義的設定檔名稱，而非內建
值。

企業管理員可以定義設定檔，並限制
使用者可選取的設定檔，方法是使用受管理的 `requirements.toml`。一旦
`allowed_permission_profiles` 存在，未列入清單的設定檔就會遭到拒絕，
包括未列入的內建設定檔，以及未來 Codex 版本新增的設定檔。請參閱
[控制可用的權限設定檔](/zh-Hant/codex/enterprise/managed-configuration#control-available-permission-profiles)
，了解建議的受管理設定。

自訂設定檔使用兩項相關概念：

- `[permissions.<name>.workspace_roots]` 會新增具體目錄，將其
  視為該設定檔的工作區根目錄。
- `[permissions.<name>.filesystem.":workspace_roots"]` 定義 Codex 在每個有效工作區根目錄內套用的檔案系統
  規則：這些根目錄包括目前
  工作階段的執行階段工作區根目錄，以及上述由設定檔定義的根目錄。

設定檔也採用一般的組態分層模型。優先順序較高的層級可以
在相同設定檔名稱下新增或取代項目，無須重新定義整個
設定檔。

例如，組織層級的組態和使用者層級的組態可以各自延伸
相同的設定檔：

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

`server` 啟用時，兩個工作區根目錄都會納入最終生效的
設定檔。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

此設定檔會：

- 讀取常用開發工具所需的最少執行階段路徑。
- 將相同的工作區根目錄規則套用至目前工作階段和
設定檔定義的根目錄。
- 讓 `.devcontainer/` 等 IDE 相關設定在每個
  根目錄下都維持唯讀。
- 透過 glob 規則拒絕存取相符的環境檔案。
- 僅允許符合已設定網域原則的網路存取。

在作用中的設定檔內，即使範圍較廣的路徑可供讀取或寫入，
範圍較窄的拒絕規則仍然有效。例如，設定檔可讓工作區根目錄
允許寫入，同時將相符的 `.env` 路徑設為 `deny`。

## 延伸設定檔

設定檔若與內建設定檔或其他具名設定檔大致相同，請使用 `extends`
加以延伸。建議優先延伸內建設定檔，而非從頭建立，以便
沿用基本防護措施。例如，延伸 `:workspace` 時，
工作區根目錄中的 `.codex` 目錄會維持唯讀，除非您明確
覆寫這項設定。只需設定一次父設定檔，再新增或覆寫
有差異的規則。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

此設定檔以 `:workspace` 為基礎，繼續拒絕存取相符的 `.env` 檔案，並
允許對 `api.openai.com` 發出請求。設定檔可以延伸 `:read-only`、
`:workspace` 或其他具名設定檔，但不能延伸
`:danger-full-access`；Codex 也會拒絕未知的父設定檔，以及繼承
循環。

## 組態規格

| 項目                                                             | 類型 / 值              | 預設值                 | 詳細資訊                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | 字串形式的設定檔名稱        | 無                    | 指定 Codex 預設套用的權限設定檔。其值必須符合 `[permissions]` 下的設定檔，或 `:workspace` 等內建設定檔。請明確設定此項，以確保行為可預期；只有在明確允許 `:workspace` 和 `:read-only` 時，受管理的要求才可省略此項。在此設定方式下，除非受管理的 `allowed_permission_profiles` 指示 Codex 使用權限設定檔，否則 Codex 會使用舊版沙盒設定。 |
| `[permissions.<name>]`                                            | 表格                      | 無                    | 定義具名設定檔。`default_permissions` 會選取一個設定檔作為預設值；其他權限設定檔設定也會使用該設定檔名稱。                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | 字串                     | 無                    | 提供設定檔的易讀說明。設定檔不會透過 `extends` 繼承父設定檔的說明。                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | 字串形式的設定檔名稱        | 無                    | 以另一個具名設定檔，或內建的 `:read-only` 或 `:workspace` 設定檔作為此設定檔的基礎。Codex 會拒絕 `:danger-full-access`、未知的父設定檔和繼承循環。                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | 表格                      | 無                    | 新增由設定檔定義的工作區根目錄，並對這些根目錄和目前工作階段的執行階段工作區根目錄一併套用 `:workspace_roots` 檔案系統規則。                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | 布林值                    | `false`                 | 值為 `true` 時，將路徑加入設定檔的工作區根目錄集合。設為 `false` 的項目則不會啟用。                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | 表格                      | 無                    | 將檔案系統路徑對應至存取值或限定範圍的子路徑對應。若缺少檔案系統表格，或表格為空，檔案系統存取會維持受限，並於啟動時發出警告。                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | 數值                     | 無                    | 當 Codex 在沙盒啟動前為相符項目建立快照時，限制 Linux、WSL 和原生 Windows 上拒絕讀取的 glob 規則展開範圍。較大的數值可能會增加啟動時的掃描工作量。請使用至少為 `1` 的值，以便在無界 `**` 模式需要時進行有界預先展開。                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`、`write` 或 `deny` | 無                    | 針對支援的路徑授予直接存取權。`deny` 會拒絕存取，且優先於具體程度相同的 `write` 或 `read` 項目。Codex 會拒絕作用中執行階段無法強制執行的直接寫入規則。                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`、`write` 或 `deny` | 無                    | 授予對 `<path>` 後代路徑的存取權。基底路徑請使用 `.`。其他子路徑必須是相對的後代路徑，且不得包含 `.` 或 `..` 元件。                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | 表格                      | 無                    | 設定指令的網路存取權，以及運作中的網路 Proxy 所強制執行的原則。除非管理員管理的網路要求會啟動 Proxy，否則請啟用 `features.network_proxy`。                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | 布林值                    | `false`                 | 啟用設定檔中指令的網路存取權。此設定不會啟動網路 Proxy；若沒有運作中的 Proxy，指令可直接連線，不受網域限制。                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | 表格                      | 無                    | 將主機模式對應至 `allow` 或 `deny`。規則僅在網路 Proxy 運作時生效。若沒有 `allow` 項目，運作中的 Proxy 會封鎖網域要求，且拒絕項目優先於允許項目。                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` 或 `deny`          | 無                    | 支援完全相符的主機名稱、比對子網域的 `*.example.com`、比對網域本身及子網域的 `**.example.com`，以及僅適用於允許規則的全域萬用字元 `*`。主機模式會經過標準化，包括移除前後空白、轉為小寫、移除結尾句點，以及移除簡單的連接埠或方括號。                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | 表格                      | 無                    | 定義 Unix 通訊端允許清單的覆寫對應。僅適用於 Docker 等本機整合。                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` 或 `deny`          | 無                    | 使用 `allow` 將 Unix 通訊端的絕對路徑加入有效允許清單，或使用 `deny` 拒絕該路徑。遭拒絕的項目不會列入有效允許清單。                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | URL 字串                 | `http://127.0.0.1:3128` | 供 `HTTP_PROXY`、`HTTPS_PROXY`、WebSocket Proxy 變數及相關工具 Proxy 環境變數使用的 HTTP Proxy 接聽程式。                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | 布林值                    | `true`                  | 啟用供 `ALL_PROXY` 與 FTP Proxy 變數使用的 SOCKS5 接聽程式。                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | URL 字串                 | `http://127.0.0.1:8081` | SOCKS5 接聽程式位址。                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | 布林值                    | `true`                  | 在 SOCKS5 接聽程式啟用時，啟用 SOCKS5 UDP 支援。                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | 布林值                    | `true`                  | 允許網路沙盒 Proxy 在處理傳出要求時，遵循上游 `HTTP(S)_PROXY` 與 `ALL_PROXY` 設定。                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | 布林值                    | `false`                 | 設為 `true` 時，會停用本機／私人網路防護機制。設為 `false` 時，`localhost` 或 `127.0.0.1` 等確切的本機常值必須明確加入允許清單；解析至本機或私人 IP 的主機名稱仍會遭封鎖。                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | 布林值                    | `false`                 | 允許 Proxy 接聽程式繫結至非回送位址。一般本機開發請保持未設定。                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | 布林值                    | `false`                 | 在支援 Unix 通訊端 Proxy 的情況下，略過 Unix 通訊端允許清單。這是一項會大幅放寬本機限制的例外機制。                                                                                                                                                                                                                                                                                                               |

## 檔案系統權限

檔案系統項目可使用 `read`、`write` 或 `deny`：

| 存取權  | 含義                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | 允許指令讀取該路徑下的檔案及列出目錄。指令無法在該處建立、修改、重新命名或刪除檔案。 |
| `write` | 允許指令讀取及修改該路徑下的檔案；在作業系統允許的情況下，也包括建立、重新命名及刪除檔案。  |
| `deny`  | 拒絕讀取及寫入該路徑下的內容。可用來在較廣泛的 `read` 或 `write` 授權範圍內，劃出拒絕存取的子路徑。         |

較具體的項目會覆寫較廣泛的項目。若有兩個項目以
同一路徑為目標，`deny` 優先於 `write`，而 `write` 則優先
於 `read`。

這項優先順序可讓設定檔先定義較廣泛的工作範圍，再劃出
應維持無法讀取的檔案或目錄：

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

在此範例中，工作區根目錄仍可寫入，`.devcontainer/` 維持
可讀取但不可寫入，而符合比對條件的環境檔案仍
無法供沙盒內的指令存取。

更具體的路徑也可在較廣泛的拒絕規則內，重新開放範圍較小的子樹：

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

支援的路徑形式：

| 路徑               | 含義                                                                                     | 可限定範圍的子路徑 |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | 檔案系統根目錄                                                                         | 僅限 `.`        |
| `:minimal`         | 常用工具所需的平台與執行階段路徑                                           | 僅限 `.`        |
| `:workspace_roots` | 目前工作階段的工作區根目錄，以及任何已啟用且由設定檔定義的工作區根目錄      | 是             |
| `:tmpdir`          | 若 `$TMPDIR` 可用，則為其位置                                               | 僅限 `.`        |
| `:slash_tmp`       | 若存在，則為 `/tmp` 資料夾                                                             | 僅限 `.`        |
| `/absolute/path`   | 平台的絕對路徑，例如 macOS/Linux/WSL 上的 `/path`，或原生 Windows 上的 `C:\path` | 是             |
| `~/path`           | 目前使用者主目錄下的路徑                                              | 是             |

在原生 Windows 上，相對於主目錄的路徑也可以使用反斜線，例如
`~\work`。

只有在設定檔確實需要廣泛的讀取範圍時，才使用 `:root`：

```toml
[permissions.audit.filesystem]
":root" = "read"

請使用 `:workspace_roots` 下的巢狀項目，將存取範圍限縮至相對於工作區根目錄的
子路徑：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

巢狀子路徑必須位於其工作區根目錄內。系統會拒絕
`../other-repo` 這類向上存取父目錄的路徑。

### 使用確切路徑或 glob 模式拒絕讀取

對於 Codex 不應讀取的檔案或子目錄樹，請使用 `deny`；即使較廣泛的
設定檔規則允許存取鄰近位置，也應如此。確切路徑適合用於
`~/.ssh` 這類固定位置。設定檔若需涵蓋一類確切位置會因程式碼庫而異的
敏感檔案，glob 模式會更合適。

當 glob 模式位於 `:workspace_roots` 下時，Codex 會以每個
有效的工作區根目錄為基準解讀該模式。例如：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

此規則會拒絕讀取符合條件的 `.env` 檔案，無論這些檔案位於執行階段的
工作區根目錄，或是設定檔定義的工作區根目錄下。若要維持正常的
工作區寫入權限，同時禁止讀取環境檔案、產生的機密資料，或其他
含有認證資訊的類似檔案，即可使用此規則。

`deny` glob 模式可作為拒絕讀取規則。`read` 或 `write` glob 模式
在 Linux、WSL 和原生 Windows 的沙盒中較不具可攜性，因此應盡可能優先使用確切
路徑或 `"docs/**" = "read"` 這類子目錄樹規則。

在 Linux、WSL 和原生 Windows 上，無界的 `**` 拒絕讀取模式可能需要在
沙盒啟動前進行有界預先展開。使用無界模式時，請設定 `glob_scan_max_depth`，例如
`"**/*.env" = "deny"`：

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` 至少必須為 `1`。數值越高，沙盒啟動前的掃描深度越深，
可能增加 Linux、WSL 和原生 Windows 的啟動工作量。
若不想使用有界展開，可明確列舉各個深度，例如
`*.env`、`*/*.env` 和 `*/*/*.env`。

若相同規則還需套用至目前工作階段根目錄以外的位置，
請在設定檔中加入可重複使用的工作區根目錄：

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

啟用此設定檔後，Codex 會將 `:workspace_roots` 規則套用至
目前工作階段的執行階段工作區根目錄，以及每個已啟用且由設定檔定義的
工作區根目錄。

在原生 Windows 上，`D:\work` 這類磁碟機代號路徑，以及
`\\server\share` 這類 UNC 路徑，都可作為絕對路徑。

## 網路權限

網路存取與網路篩選是兩項獨立設定。設定
`permissions.<name>.network.enabled = true`，即可讓指令存取網路；
另須啟用 `features.network_proxy`，才能強制執行設定檔的網域規則：

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

實際行為取決於這兩項設定：

- 網路關閉：無論代理伺服器功能是否啟用，指令都
無法存取網路。
- 網路開啟、代理伺服器關閉：指令可直接、不受限制地存取
網路。權限設定檔中的網域規則不會生效。
- 網路開啟、代理伺服器開啟：指令會使用代理伺服器，並由代理伺服器強制執行設定檔的
網域規則。若啟用中的代理伺服器未設定任何允許的網域，就會封鎖外部
目的地。

新增 `[permissions.<name>.network.domains]` 或設定
`permissions.<name>.network.enabled = true`，都不會啟用
`features.network_proxy`。管理員也可透過
`[experimental_network]` 設定，在 `requirements.toml` 中啟用代理伺服器。請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-network-access-requirements)。

啟用後，網路沙盒代理伺服器預設會繫結至本機監聽器：

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

除非需要與特定執行階段整合，否則請維持這些監聽器的預設設定。
`dangerously_*` 網路設定鍵是供特殊環境繞過限制的機制，
不應用於一般本機開發。

### 本機與私有網路

啟用網路代理伺服器後，Codex 預設會套用本機／私有網路防護，
以防範 DNS 重新繫結，以及意外存取本機
服務。若要明確允許以常值指定的本機目標，請將確切的
主機名稱或 IP 位址常值加入允許清單：

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

僅在設定檔必須連線至已列入允許清單的主機名稱時，才設定 `allow_local_binding = true`；
這些主機名稱會解析為本機或私有位址：

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Unix 通訊端

Unix 通訊端代理功能可供 Docker 等工具繞過本機限制。請
謹慎使用：

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

使用 `deny` 可拒絕通訊端路徑，包括繼承而來的允許項目。遭拒的
通訊端路徑不會納入有效的允許清單。

啟用 Unix 通訊端時，請確保代理伺服器監聽器仍繫結至回送位址。

## 從舊有沙盒設定遷移

若要以一個可重複使用的設定檔同時描述檔案系統與網路行為，可使用權限設定檔取代舊有的 `sandbox_mode` 與
`sandbox_workspace_write` 組合。每個工作階段應擇一使用其中一套
系統，不可
同時使用兩套。

建議起點：

- 唯讀工作流程可使用內建的 `:read-only` 設定檔，或定義只在必要位置
  授予讀取權限的自訂設定檔。
- 若要編輯工作區，請使用內建的 `:workspace` 設定檔，或定義
  透過 `:workspace_roots` 寫入，且只加入工作流程所需額外
  暫存或快取路徑的自訂設定檔。
- 如需不受限制的本機執行，請僅在確實有意採用 `:danger-full-access`
  所提供的最廣泛本機存取模式時，使用此設定檔。

設定檔用來描述工作階段在本機的預設安全態勢。組織管理的
要求仍可加入限制，使用者設定不應
放寬這些限制。請參閱 [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)，
瞭解管理員強制執行的檔案系統與網路限制。

## 適用範圍與強制執行

權限設定檔會界定本機沙盒指令的
執行範圍。請搭配核准政策，以及網頁搜尋、連接器、MCP 伺服器、
內建瀏覽器、電腦與 Codex 雲端
各自獨立的控制項使用。

### 設定檔控制的項目

- **本機指令執行：** 權限設定檔會管控在您電腦上以沙盒方式執行的指令。
  連接器、MCP 伺服器、瀏覽器或
  電腦操作介面、Codex 雲端環境設定，以及經核准的
  權限提升，則有各自的控制機制。
- **檔案系統寫入：** 具備寫入能力的設定檔可產生持續存在的變更。
  對指令碼、建置步驟、套件管理器掛勾、Shell 啟動
  檔案與共用目錄的寫入都應視為敏感操作，因為後續工具或使用者可能在
  原始沙盒上下文之外執行這些檔案。
- **對外連線目的地：** 網路網域規則只有在網路代理伺服器啟用期間，才能限制沙盒中
  指令流量可前往的目的地。這些規則不會
  判定允許的目的地是否可信，且萬用字元允許
  規則的涵蓋範圍仍然廣泛。
- **本機服務：** 啟用中的網路代理伺服器預設會封鎖本機與私有網路
  目標。將 `localhost`、私有 IP 位址或 Unix 通訊端加入允許清單，或設定
`allow_local_binding = true`，都會明確開放本機服務的存取權。

### 網路代理伺服器無法控制的項目

網路代理伺服器只會篩選在沙盒中執行的本機指令
所產生的流量，不會將設定檔的網域允許清單套用至下列項目：

- **網頁搜尋：** 託管搜尋工具有自己的存取設定。請使用
`web_search` 控管搜尋工具；對於受管理的用戶端，也可使用 `allowed_web_search_modes`
  加以控制。`tools.web_search.allowed_domains` 只會篩選搜尋結果，不會限制指令的
  網路存取。
- **應用程式與連接器：** 由連接器支援的工具會使用各自的服務端
  連線、工作區權限，以及應用程式或工具設定。
- **MCP 伺服器：** 本機與遠端 MCP 伺服器使用各自的處理程序或
  傳輸機制。請透過 `mcp_servers` 設定與受管理的伺服器
  允許清單加以控管。
- **瀏覽器與電腦：** 瀏覽器導覽與電腦操作
  各自使用獨立的功能與核准控制機制。
- **Codex 服務流量：** 模型、身分驗證與其他用戶端服務
  請求會使用用戶端獨立的 HTTP 與系統代理伺服器設定。
- **Codex 雲端：** 這些任務會使用其所屬環境的
[網際網路存取設定](/zh-Hant/codex/cloud/internet-access)。

若要限制上述項目，請直接設定各項功能。指令的網路
允許清單並非適用於 Codex 所有操作的全域網路政策。

### 強制執行的運作方式

- 在 macOS 上，Codex 使用 Seatbelt 沙盒設定檔。若平台沙盒無法
強制執行所選政策，Codex 會拒絕執行指令，
而非逕自在未套用沙盒的情況下執行。
- 在 Linux 和 WSL 上，Codex 使用 [bubblewrap](https://github.com/containers/bubblewrap)
  與 [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html)，
  並可透過 Landlock 提供相容性備援路徑。可採用的最強
  強制執行方式取決於使用者命名空間和核心支援；受限的
  容器主機可能迫使系統改用相容性路徑，而不受支援的權限分割政策
  則會遭到拒絕。
- 在原生 Windows 上，[`elevated` 沙盒](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)
  提供最強的防護，因為可使用專用的低權限沙盒使用者、
  檔案系統權限邊界與防火牆規則。`unelevated`
  沙盒則是網路隔離較弱的備援方案，無法強制執行
  所有細分的讀取／寫入例外範圍，因此系統會拒絕不受支援的政策。如需 Linux 沙盒模型，
  請使用 WSL。

### 操作指引

請選擇仍能完成任務、權限範圍最小的設定檔，尤其是在
授予寫入權限或對外網路存取權時。核准政策、機密資訊
處理方式與允許規則，都應與該存取層級一致。

## 常見設定檔

### 唯讀且設有網路允許清單

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### 檔案存取僅限工作區

以下是權限設定檔範例：Codex 可寫入工作區資料夾，但不得讀取檔案系統的其他部分（`:minimal` 所定義的少數例外除外）。

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### 工作區寫入且無網路存取

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### 工作區寫入且可存取公開網路

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

只有在您打算允許存取公開網路時，才應使用全域 `"*"` 允許規則。
拒絕規則可限縮範圍較廣的允許清單。
