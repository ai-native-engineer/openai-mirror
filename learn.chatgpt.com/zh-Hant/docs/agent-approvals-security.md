<!-- source: https://learn.chatgpt.com/zh-Hant/docs/agent-approvals-security -->

Codex 有助於保護您的程式碼與資料，並降低遭濫用的風險。

  本頁說明如何安全操作 Codex，包括沙盒、核准
  與網路存取。如果您要尋找的是用於掃描已連線 GitHub 程式碼庫的
  產品 Codex Security，請參閱 [Codex Security](/zh-Hant/codex/security)。

預設情況下，智慧體執行時會關閉網路存取。在本機，Codex 使用由作業系統強制執行的沙盒，限制其可存取的範圍（通常是目前的工作區），並透過核准政策控管何時必須先停下來徵詢您的同意，才能執行動作。

如需概略瞭解沙盒在 ChatGPT 桌面版應用程式、
Codex CLI 與 IDE 擴充功能中的運作方式，請參閱[沙盒](/zh-Hant/codex/sandboxing)。
如需更全面的企業安全性概覽，請參閱 [Codex 安全性白皮書](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)。

## 沙盒與核准

Codex 的安全控管分成兩個相互配合的層級：

- **沙盒模式**：Codex 執行模型生成的指令時，技術上可以執行哪些動作，例如可寫入哪些位置，以及能否存取網路。
- **核准政策**：Codex 必須在執行哪些動作前徵詢您的同意，例如離開沙盒、使用網路，或執行不在受信任集合中的指令。

Codex 會根據執行環境採用不同的沙盒模式：

- **Codex 雲端**：在由 OpenAI 管理的隔離容器中執行，防止存取您的主機系統或不相關的資料。採用兩階段執行模型：設定階段在智慧體階段之前執行，並可存取網路以安裝指定的相依套件；接著，智慧體階段預設會離線執行，除非您為該環境啟用網際網路存取。為雲端環境設定的機密資訊僅能在設定階段使用，並會在智慧體階段開始前移除。
- **Codex CLI／IDE 擴充功能**：由作業系統層級的機制強制執行沙盒政策。預設不允許網路存取，且寫入權限僅限於使用中的工作區。您可以根據自身的風險承受度調整沙盒、核准政策與網路設定。

使用 `Auto` 預設組態時（例如 `--sandbox workspace-write --ask-for-approval on-request`），Codex 可以自動在工作目錄中讀取檔案、進行編輯及執行指令。

若要編輯工作區以外的檔案，或執行需要網路存取的指令，Codex 會要求核准。如果您只想對話或規劃而不進行變更，請使用 `/permissions` 指令切換至 `read-only` 模式。

即使動作並非 Shell 指令或檔案變更，Codex 也可針對標示會產生副作用的應用程式（連接器）工具呼叫要求核准。當應用程式／MCP 工具標示破壞性註記時，其破壞性工具呼叫一律需要核准；但如果工具也標示讀取註記，則以讀取註記為優先。

## 安全監控與暫停的任務

GPT-6 Astra 在 Codex 和 ChatGPT Work 中提供安全監控。監控以非同步方式執行，若偵測到模型行為可能不安全，便可暫停任務。觸發暫停的活動可能已經執行，任務才會暫停；監控無法取代沙盒、權限或結果審查。

如果任務暫停，請閱讀通知，並在有監控結果可供查看時加以審查。確認任務可以安全繼續後，再恢復執行。如果通知指出任務已結束，或未提供恢復執行的選項，就無法從該介面恢復執行。

| 介面與資料控制                                                                               | 監控結果與恢復執行                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 支援查看監控結果與恢復執行流程，且未採用此處所列資料控制的 Codex 與 ChatGPT Work 用戶端 | 恢復執行前，請先審查監控結果。                      |
| Codex CLI 與行動版                                                                                    | 無法查看完整監控結果或恢復執行。任務會結束。 |
| 零資料保留、調整版濫用監控，或美國以外的資料儲存駐留                        | 無法查看完整監控結果或恢復執行。任務會結束。 |

安全監控會評估任務執行期間的模型行為。
[自動核准審查](/zh-Hant/codex/sandboxing/auto-review)則針對原本就需要核准的個別動作，
在執行前進行評估。即使某個動作已通過自動核准審查，
其所屬任務仍可能在之後因監控而暫停。

## 網路存取 

若使用 Codex 雲端，請參閱[智慧體網際網路存取](/zh-Hant/codex/cloud/internet-access)，以啟用完整網際網路存取或網域允許清單。

在 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中，預設的 `workspace-write` 沙盒模式會關閉網路存取，除非您在組態中啟用：

```toml
[sandbox_workspace_write]
network_access = true

### 網路隔離

網路存取透過目的地規則控管，這些規則適用於指令啟動的指令碼、
程式和子處理程序。當指令的網路存取已啟用時，
請開啟 `network_proxy` 功能，讓這些流量
受到您設定的網路政策約束。單純新增網域規則
不會啟用代理功能。

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

對於一次性的 CLI 工作階段，若只需要開關，請使用布林簡寫；若同時要設定政策選項，則使用表格形式：

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

此功能會改變已啟用的網路存取如何受到控管，本身不會授予
網路存取權。請使用 `sandbox_workspace_write.network_access` 並搭配
`workspace-write` 組態，決定是否允許指令存取網路：

- 網路關閉 + `network_proxy` 開啟：網路維持關閉，此功能不會起作用。
- 網路開啟 + `network_proxy` 關閉：網路維持開啟，且可不受限制地
  直接對外存取。
- 網路開啟 + `network_proxy` 開啟：網路維持開啟，且對外流量會
  受到已設定網路政策的限制。

代理功能也適用於[權限設定檔](/zh-Hant/codex/permissions#network-permissions)。
設定檔中的 `network.enabled = true` 可授予指令網路存取權，
而 `features.network_proxy = true` 則會讓該設定檔的網域規則
開始強制生效：

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

如果在這個範例中省略代理功能，指令可直接存取網路，
且 `api.openai.com` 允許規則不會限制其目的地。

由管理員管理的 `experimental_network` 要求與使用者的功能開關
彼此獨立。這些要求不必依賴
`features.network_proxy`，即可設定並啟動沙盒網路；但若目前使用的沙盒
停用網路，也不會開啟網路存取。請參閱[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-network-access-requirements)，
以瞭解管理員端的 `requirements.toml` 結構。

#### 網路政策

網域規則以允許清單為基礎：

- 精確指定的主機只會與其本身相符。
- `*.example.com` 可比對 `api.example.com` 等子網域，但無法比對
`example.com`。
- `**.example.com` 可同時比對根網域和子網域。
- 全域 `*` 允許規則會比對任何未遭拒絕的公用主機。請將 `*`
  視為廣泛的網路存取，並盡可能優先使用限定範圍的規則。
- `deny` 一律優先於 `allow`，且全域 `*` 僅適用於允許規則。

#### 本機與私人網路目的地

預設情況下，`allow_local_binding = false` 會封鎖回送、連結本機與
私人網路目的地：

- 特定例外：當指令需要存取單一本機目標時，
  請新增精確指定本機 IP 常值或 `localhost` 的允許規則。
- 擴大存取範圍：只有在您確實打算擴大本機或私人網路的存取範圍時，
  才設定 `allow_local_binding = true`。
- 萬用字元：萬用字元規則不視為明確的本機例外。
- 解析後的位址：解析為本機或私人 IP 位址的主機名稱，即使符合允許清單，仍會遭到封鎖。

#### DNS 重新綁定防護

允許存取主機名稱前，Codex 會盡可能執行 DNS 與 IP 分類檢查：

- 查詢失敗或逾時時，會封鎖存取。
- 解析為非公用位址的主機名稱會遭到封鎖。
- 這項檢查可降低 DNS 重新綁定風險，但無法完全消除。若要徹底防止重新綁定，就必須一路到傳輸層都固定使用解析後的 IP 位址。

如果威脅範圍包含惡意 DNS，請同時在較低層級強制執行對外流量控制。

#### 危險設定

以下兩項設定的用途是擴大信任邊界：

- `dangerously_allow_non_loopback_proxy = true` 可讓代理監聽器暴露於
  回送位址以外。
- `dangerously_allow_all_unix_sockets = true` 會繞過 Unix socket 允許清單。

請僅在嚴格控管的環境中使用這些設定。啟用 Unix socket 代理功能時，即使要求繫結至非回送位址，監聽器仍只會使用回送位址，避免沙盒網路成為遠端連入本機常駐程式的橋樑。

`network_proxy` 預設為關閉。啟用後的行為如下：

| 設定                                | 預設值 | 行為                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | 只有在指令的網路存取已開啟時，才會啟動沙盒網路。                                                                                                           |
| `domains`                              | 未設定   | 採用允許清單機制，因此在新增 `allow` 規則前，不允許存取任何外部目的地。支援精確主機名稱、限定範圍的萬用字元，以及全域 `*` 允許規則；`deny` 一律優先。 |
| `unix_sockets`                         | 未設定   | 在新增明確的 `allow` 規則前，不允許存取任何 Unix socket 目的地。                                                                                                         |
| `allow_local_binding`                  | `false` | 封鎖本機及私人網路目的地，除非您新增允許規則，指定確切的本機 IP 位址字面值或 `localhost`，或明確啟用更廣泛的本機／私人網路存取。                |
| `enable_socks5`                        | `true`  | 政策允許時，提供 SOCKS5 支援。                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | 當 SOCKS5 可用時，允許透過 SOCKS5 傳送 UDP 流量。                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | 讓沙盒網路遵循環境中設定的上游代理伺服器。                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | 除非您刻意將監聽端點開放至 localhost 以外，否則端點只會使用回送位址。                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | 除非您刻意略過這項保護，否則 Unix socket 存取仍以允許清單為依據。                                                                                              |

### 指令網路代理伺服器未涵蓋的流量

網路代理伺服器會篩選在本機指令沙盒中執行的指令碼、程式及子行程，但不會篩選網頁搜尋、應用程式或連接器工具呼叫、MCP 伺服器連線、瀏覽器或電腦功能的活動、Codex 雲端任務，以及用戶端的模型與身分驗證要求。這些功能各自使用獨立的服務連線、功能設定、工作區政策或環境控制機制。

瀏覽器工具在存取來源前，會另外檢查受管理的網路拒絕規則及排他性允許清單。
瀏覽器來源政策可進一步限制網站存取、
上傳、下載及開發工具。請參閱
[受管理的瀏覽器控制措施](/zh-Hant/codex/enterprise/managed-configuration#control-browser-and-computer-use)。

對於受管理的使用者，請將指令網路政策搭配其他控制措施，例如
`allowed_web_search_modes`、已核准的 `mcp_servers`，以及
應用程式、外掛程式、瀏覽器或電腦功能的要求設定。請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)。

您也可以控制[網頁搜尋工具](https://platform.openai.com/docs/guides/tools-web-search)，而不必授予所啟動的指令完整的網路存取權。Codex 預設會透過網頁搜尋快取取得結果。此快取是 OpenAI 維護的網頁結果索引，因此快取模式會傳回預先建立索引的結果，而不會擷取即時網頁。這可降低任意即時內容帶來的提示注入風險，但您仍應將網頁結果視為不受信任。如果使用 `--yolo` 或其他[完整存取權沙盒設定](#common-sandbox-and-approval-combinations)，網頁搜尋預設會傳回即時結果。使用 `--search` 或設定 `web_search = "live"` 可允許即時瀏覽；將其設為 `"disabled"` 則可關閉此工具：

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

若外部網頁存取應受搜尋索引控管，請設定 `web_search = "indexed"`。
在 Codex 中啟用網路存取或網頁搜尋時請務必謹慎。
提示注入可能導致智慧體擷取並遵循不受信任的指示。

## 預設值與建議

- 啟動時，Codex 會偵測資料夾是否受版本控制，並提出以下建議：
  - 受版本控制的資料夾：`Auto`（工作區寫入 + 提出要求時核准）
  - 未受版本控制的資料夾：`read-only`
- 視您的設定而定，Codex 也可能以 `read-only` 模式啟動，直到您明確信任工作目錄為止（例如透過初始設定提示或 `/permissions`）。
- 工作區包括目前的目錄，以及 `/tmp` 等暫存目錄。使用 `/status` 指令即可查看工作區包含哪些目錄。
- 若要採用預設值，請執行 `codex`。
- 您可以明確設定這些選項：
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### 可寫入根目錄中的受保護路徑

在預設的 `workspace-write` 沙盒政策中，可寫入根目錄仍包含受保護路徑：

- `<writable_root>/.git` 無論是目錄或檔案，都會受到唯讀保護。
- 如果 `<writable_root>/.git` 是指標檔案（`gitdir: ...`），解析後的 Git 目錄路徑也會受到唯讀保護。
- `<writable_root>/.agents` 以目錄形式存在時，會受到唯讀保護。
- `<writable_root>/.codex` 以目錄形式存在時，會受到唯讀保護。
- 這項保護會遞迴套用，因此這些路徑下的所有內容皆為唯讀。

### 執行時不顯示核准提示

您可以使用 `--ask-for-approval never` 或 `-a never`（簡寫）停用核准提示。

此選項適用於所有 `--sandbox` 模式，因此您仍可控制 Codex 的自主程度。Codex 會在您設定的限制內盡力執行。

如果您需要 Codex 在不顯示核准提示的情況下讀取檔案、進行編輯，並執行可存取網路的指令，請使用 `--sandbox danger-full-access`（或 `--dangerously-bypass-approvals-and-sandbox` 旗標）。請先審慎評估。

若要採取折衷方案，可使用 `approval_policy = { granular = { ... } }`，讓特定類別的核准提示保留互動方式，同時自動拒絕其他類別。這項細粒度政策涵蓋沙盒核准、execpolicy-rule 提示、MCP 提示、`request_permissions` 提示及技能指令碼核准。

### 核准要求的自動審查

預設情況下，核准要求會交由您處理：

```toml
approvals_reviewer = "user"

核准要求的自動審查適用於互動式核准，例如
`approval_policy = "on-request"` 或細粒度核准政策。設定
`approvals_reviewer = "auto_review"`，即可在 Codex 執行要求前，先將符合條件的核准要求
交由審查智慧體處理：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

如需了解審查智慧體的完整生命週期、觸發條件、組態優先順序
及失敗時的行為，請參閱
[自動審查](/zh-Hant/codex/sandboxing/auto-review)。

審查智慧體只會評估原本就需要核准的動作，例如沙盒權限提升、
遭封鎖的網路要求、`request_permissions` 提示，或
具有副作用的應用程式與 MCP 工具呼叫。仍在沙盒範圍內的動作
可繼續執行，不需要額外審查。

審查政策會檢查資料外傳、憑證探測、持續削弱安全防護，以及破壞性操作。政策允許時，低風險與中風險操作可以繼續執行。政策會拒絕嚴重風險操作。高風險操作必須取得充分的使用者授權，且不得符合任何拒絕規則。提示詞建置、審查工作階段或剖析失敗時，一律拒絕執行。逾時會另行顯示，但相關操作仍不會執行。

[預設審查政策](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)
位於開放原始碼的 Codex 程式碼庫中。企業可使用受管理要求中的
`guardian_policy_config`，替換政策中的租戶專屬區段。
也支援本機 `[auto_review].policy` 的政策文字，但受管理的要求
優先。如需設定詳細資訊，請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-automatic-review-policy)。

在 ChatGPT 桌面版應用程式中，這些審查會顯示為自動審查項目，並標示「審查中」、「已核准」、「已拒絕」、「已中止」或「已逾時」等狀態。這些項目也可能包含受審查要求的風險等級，以及使用者授權評估。

自動審查需要額外呼叫模型，因此可能增加 Codex 用量。管理員
可使用 `allowed_approvals_reviewers` 加以限制。

### 常見的沙盒與核准組合

| 目的                                                            | 旗標／組態                                                                                                                      | 效果                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 自動（預設組態）                                                     | _不需要旗標_ ，或使用 `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex 可以在工作區中讀取檔案、進行編輯及執行指令。若要編輯工作區外的內容或存取網路，Codex 必須取得核准。 |
| 安全的唯讀瀏覽                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex 可以讀取檔案並回答問題。若要進行編輯、執行指令或存取網路，Codex 必須取得核准。                               |
| 唯讀非互動模式（CI）                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex 只能讀取檔案，且絕不會要求核准。                                                                                              |
| 自動編輯，但執行不受信任的指令前要求核准 | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex 可以讀取及編輯檔案，但執行不受信任的指令前會要求核准。                                                           |
| 自動審查模式                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` 或 `approvals_reviewer = "auto_review"` | 沙盒邊界與標準的 on-request 模式相同，但符合條件的核准要求會交由自動審查處理，而不會顯示給使用者。  |
| 危險的完整存取權                                             | `--dangerously-bypass-approvals-and-sandbox`（別名：`--yolo`）                                                                      |  無沙盒；無需核准 _（不建議）_                                                                               |

非互動式執行請使用 `codex exec --sandbox workspace-write`；Codex 仍保留舊版的 `codex exec --full-auto` 呼叫方式作為已棄用的相容途徑，並會印出警告。

使用 `--ask-for-approval untrusted` 時，Codex 只會自動執行已知安全的讀取操作。可能改變狀態或觸發外部執行途徑的指令（例如破壞性的 Git 操作，或 Git 輸出／組態覆寫旗標）都需要核准。

#### `config.toml` 中的組態

如需瞭解更完整的設定工作流程，請參閱[基本設定](/zh-Hant/codex/config-file/config-basic)、[進階設定](/zh-Hant/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)與[組態參考資料](/zh-Hant/codex/config-file/config-reference)。

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

您也可以將預設組態儲存為[設定檔](/zh-Hant/codex/config-file/config-advanced#profiles)，再透過 `codex --profile profile-name` 選用：

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### 在本機測試沙盒

若要瞭解指令在 Codex 沙盒中執行時的行為，請使用下列 Codex CLI 指令：

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

`sandbox` 指令也可透過 `codex debug` 使用，各平台的輔助工具也有別名，例如 `codex sandbox seatbelt` 和 `codex sandbox landlock`。

## 作業系統層級的沙盒

Codex 會依據您使用的作業系統，以不同方式實施沙盒隔離：

- **macOS** 採用 Seatbelt 政策，使用 `sandbox-exec` 搭配設定檔（`-p`）執行指令；此設定檔對應您選擇的 `--sandbox` 模式。當受限讀取存取啟用平台預設設定時，Codex 會附加經篩選的 macOS 平台政策，而非廣泛允許存取 `/System`，以維持常用工具的相容性。
- **Linux** 預設使用 `bwrap` 搭配 `seccomp`。
- **Windows** 在 [Windows Subsystem for Linux 2 (WSL2)](/zh-Hant/codex/windows/wsl) 中執行時，會使用 Linux 沙盒實作。Codex 至 `0.114` 版本仍支援 WSL1；從 `0.115` 版本起，Linux 沙盒改用 `bwrap`，因此不再支援 WSL1。在 Windows 上原生執行時，Codex 會使用 [Windows 沙盒](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)實作。

Windows 上的 Codex IDE 擴充功能直接支援 WSL2。請在 VS Code 設定中加入下列內容，確保 WSL2 可用時，智慧體會在其中執行：

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

這可確保即使主機作業系統是 Windows，IDE 擴充功能仍會在指令、核准及檔案系統存取方面沿用 Linux 沙盒的語意。詳情請參閱 [WSL 指南](/zh-Hant/codex/windows/wsl)。

在 Windows 上原生執行時，請在 `config.toml` 中設定原生沙盒模式：

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

如需詳細資訊，請參閱 [Windows 設定指南](/zh-Hant/codex/windows/windows-sandbox#windows-sandbox)。

在 Docker 等容器化環境中執行 Linux 時，如果主機或容器組態封鎖 Codex 所需的命名空間、setuid `bwrap` 或 `seccomp` 操作，沙盒可能無法運作。

在這種情況下，請設定 Docker 容器以提供所需的隔離，然後在容器內執行 `codex` 並加上 `--sandbox danger-full-access`（或 `--dangerously-bypass-approvals-and-sandbox` 旗標）。

### 在 Dev Containers 中執行 Codex

如果主機無法直接執行 Linux 沙盒，或組織已將容器化開發列為標準作法，請透過 Dev Containers 執行 Codex，並由 Docker 提供外層隔離邊界。此方式適用於 Visual Studio Code Dev Containers 及相容工具。

請使用 [Codex 安全開發容器範例](https://github.com/openai/codex/tree/main/.devcontainer)作為參考實作。此範例會安裝 Codex、常用開發工具及 `bubblewrap`，並設定以防火牆為基礎的對外存取控管。

  開發容器可提供相當程度的保護，但無法阻止所有
  攻擊。如果您在容器內使用 `--sandbox danger-full-access` 或
`--dangerously-bypass-approvals-and-sandbox` 執行 Codex，惡意專案
  可能外傳開發容器內任何可存取的內容，包括
  Codex 憑證。只應在受信任的程式碼庫中採用這種方式，並
  如同監控其他高權限環境一樣監控 Codex 的活動。

此參考實作包括：

- 已安裝 Codex 和常用開發工具的 Ubuntu 24.04 基礎映像檔；
- 以允許清單控管對外存取的防火牆設定檔；
- 用於在容器中重新開啟工作區的 VS Code 設定與擴充功能建議；
- 用於保存指令歷程記錄與 Codex 組態的持續性掛載；
- `bubblewrap`，讓 Codex 在容器授予所需能力時，仍可使用其 Linux 沙盒。

若要試用：

1. 安裝 Visual Studio Code 與 [Dev Containers 擴充功能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)。
2. 將 Codex 範例中的 `.devcontainer` 設定複製到您的程式碼庫，或直接從 Codex 程式碼庫開始。
3. 在 VS Code 中執行 **Dev Containers: 在容器中開啟資料夾...** ，然後選取 `.devcontainer/devcontainer.secure.json`。
4. 容器啟動後，開啟終端並執行 `codex`。

您也可以從 CLI 啟動容器：

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

此範例包含三個主要部分：

- `.devcontainer/devcontainer.secure.json` 控制容器設定、能力、掛載、環境變數及 VS Code 擴充功能。
- `.devcontainer/Dockerfile.secure` 定義以 Ubuntu 為基礎的映像檔及安裝的工具。
- `.devcontainer/init-firewall.sh` 會套用對外網路政策。

此參考防火牆的設計定位是供您起步使用。如果您的隔離機制仰賴網域允許清單，請實作符合自身環境的 DNS 重新綁定與 DNS 重新整理防護措施，例如依據 TTL 重新整理，或使用可感知 DNS 的防火牆。

請在容器內選擇下列其中一種模式：

- 如果 Dev Container 設定檔授予 `bwrap` 建立內層沙盒所需的能力，請保持 Codex 的 Linux 沙盒啟用。
- 如果您要以容器作為安全邊界，請在容器內使用 `--sandbox danger-full-access` 執行 Codex，以免 Codex 嘗試建立第二層沙盒。

## 版本控制

搭配版本控制工作流程時，Codex 的運作效果最佳：

- 請在功能分支上工作，並在委派工作前確認 `git status` 顯示乾淨狀態。如此可讓 Codex 的修補內容更容易單獨識別與還原。
- 請優先採用以修補檔為基礎的工作流程（例如 `git diff`/`git apply`），而非直接編輯受追蹤的檔案。請經常提交，以便每次只回復少量變更。
- 請像處理其他 PR 一樣處理 Codex 建議：執行針對性驗證、審查差異，並在提交訊息中記錄決策，以供稽核。

## 監控與遙測

Codex 支援透過 OpenTelemetry (OTel) 進行監控，需由您主動啟用。這可協助團隊稽核使用情況、調查問題及滿足合規要求，同時不削弱本機的預設安全性。遙測預設為關閉；請在組態中明確啟用。

### 概覽

- Codex 預設會關閉 OTel 匯出，讓本機執行維持獨立運作。
- 啟用後，Codex 會發出結構化日誌事件，涵蓋對話、API 要求、SSE/WebSocket 串流活動、使用者提示詞（預設會遮蔽）、工具核准決策及工具結果。
- Codex 會以 `service.name`（發起者）、CLI 版本及環境標籤標記匯出的事件，以區分開發／預備／正式環境的流量。

### 啟用 OTel（需主動啟用）

在 Codex 組態中新增 `[otel]` 區塊（組態通常位於 `~/.codex/config.toml`），選擇匯出器，並決定是否記錄提示詞文字。

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` 會讓遙測插樁保持啟用，但不會將資料傳送至任何位置。
- 若要將事件傳送至您自己的收集器，請選擇下列其中一項：

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

Codex 會批次處理事件，並在關閉時將累積的事件全部送出。Codex 只會匯出其 OTel 模組產生的遙測資料。

### 事件類別

代表性的事件類型包括：

- `codex.conversation_starts`（模型、推理設定、沙盒／核准政策）
- `codex.api_request`（嘗試次數、狀態／是否成功、耗時與錯誤詳情）
- `codex.sse_event`（串流事件類型、成功／失敗、耗時，以及 `response.completed` 中的 Token 數量）
- `codex.websocket_request` 與 `codex.websocket_event`（請求耗時，以及每則訊息的類型／是否成功／錯誤）
- `codex.user_prompt`（長度；除非明確啟用內容記錄，否則會遮蔽內容）
- `codex.tool_decision`（已核准／已拒絕，來源：組態或使用者）
- `codex.tool_result`（耗時、是否成功、輸出片段）

相關的 OTel 指標（計數器與耗時直方圖成對搭配）包括 `codex.api_request`、`codex.sse_event`、`codex.websocket.request`、`codex.websocket.event` 和 `codex.tool.call`，各自搭配對應的 `.duration_ms` 測量工具。

如需完整的事件目錄與組態參考資料，請參閱 [GitHub 上的 Codex 組態文件](https://github.com/openai/codex/blob/main/docs/config.md#otel)。

### 安全性與隱私權指引

- 除非政策明確允許儲存提示詞內容，否則請維持 `log_user_prompt = false`。提示詞可能包含原始程式碼和敏感資料。
- 請僅將遙測資料傳送至由您控管的收集器，並採用符合合規要求的資料保留限制與存取控制。
- 請將工具引數和輸出視為敏感資料。可行時，優先在收集器或 SIEM 端遮蔽敏感資訊。
- 如果不希望 Codex 將工作階段紀錄儲存在 `CODEX_HOME` 下，請檢查本機資料保留設定，例如 `history.persistence` / `history.max_bytes`。請參閱[進階設定](/zh-Hant/codex/config-file/config-advanced#history-persistence)與[組態參考資料](/zh-Hant/codex/config-file/config-reference)。
- 如果在停用網路存取的狀態下執行 CLI，OTel 匯出資料將無法送達收集器。若要匯出，請在 `workspace-write` 模式中允許對 OTel 端點的網路存取，或將收集器網域加入核准清單後，從 Codex 雲端匯出。
- 請定期審查事件，檢查核准或沙盒是否有變更，以及是否出現非預期的工具執行。

OTel 是選用功能，旨在補強而非取代上述沙盒與核准保護。

## 受管理的設定

企業管理員可透過[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)，調整工作區的 Codex 安全性設定。設定方式與政策詳情請參閱該頁面。
