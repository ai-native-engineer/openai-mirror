<!-- source: https://learn.chatgpt.com/zh-Hant/docs/config-file/config-basic -->

Codex 會從多個位置讀取組態。您的個人預設值儲存在 `~/.codex/config.toml`，也可以透過 `.codex/config.toml` 檔案新增專案覆寫設定。基於安全考量，Codex 只會在您信任專案時，載入該專案的 `.codex/` 組態層。

## Codex 設定檔

Codex 會將使用者層級的組態儲存在 `~/.codex/config.toml`。若要讓設定僅適用於特定專案或子資料夾，請在程式碼庫中新增 `.codex/config.toml` 檔案。

若要從 Codex IDE 擴充功能開啟設定檔，請選取右上角的齒輪圖示，然後選取 **Codex 設定 \> 開啟 config.toml**。

CLI 和 IDE 擴充功能共用相同的組態層。您可以透過這些組態層執行下列操作：

- 設定預設模型和供應商。
- 設定[核准政策與沙盒設定](/zh-Hant/codex/agent-approvals-security#sandbox-and-approvals)。
- 設定 [MCP 伺服器](/zh-Hant/codex/extend/mcp)。

## 組態優先順序

Codex 會依下列順序決定設定值（優先順序由高至低）：

1. CLI 旗標與 `--config` 覆寫設定
2. 專案設定檔：`.codex/config.toml`，由專案根目錄往下依序套用至目前工作目錄（距目前工作目錄最近者優先；僅限受信任的專案）
3. 使用 `--profile profile-name` 選取的[設定檔](/zh-Hant/codex/config-file/config-advanced#profiles)（`~/.codex/profile-name.config.toml`）
4. 使用者設定：`~/.codex/config.toml`
5. 系統組態（若有）：Unix 上的 `/etc/codex/config.toml`
6. 內建預設值

利用此優先順序，在 `config.toml` 中設定共用預設值，並讓[設定檔](/zh-Hant/codex/config-file/config-advanced#profiles)只保留有差異的設定值。

如果您將專案標示為不受信任，Codex 會略過專案範圍內的 `.codex/` 組態層，包括專案內的組態、掛勾和規則。使用者與系統組態仍會載入，包括使用者與全域層級的掛勾和規則。

如需瞭解如何透過 `-c`/`--config` 進行一次性覆寫（包括 TOML 引號規則），請參閱[進階設定](/zh-Hant/codex/config-file/config-advanced#one-off-overrides-from-the-cli)。

  在受管理的電腦上，您的組織也可能透過
`requirements.toml` 強制套用限制（例如，不允許 `approval_policy = "never"` 或
`sandbox_mode = "danger-full-access"`）。請參閱[受管理的
  組態](/zh-Hant/codex/enterprise/managed-configuration)和[管理員強制執行的
  要求](/zh-Hant/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

## 常用組態選項

以下是幾個最常變更的選項：

#### 預設模型

選擇 Codex 在 CLI 和 IDE 中預設使用的模型。

#### 核准提示

控制 Codex 何時會在執行產生的指令前暫停並詢問您。

```toml
approval_policy = "on-request"

如需瞭解 `untrusted`、`on-request` 與 `never` 的行為差異，請參閱[不顯示核准提示的執行方式](/zh-Hant/codex/agent-approvals-security#run-without-approval-prompts)和[常見的沙盒與核准組合](/zh-Hant/codex/agent-approvals-security#common-sandbox-and-approval-combinations)。

#### 沙盒層級

調整 Codex 在執行指令時對檔案系統和網路的存取程度。

```toml
sandbox_mode = "workspace-write"

如需瞭解各模式的行為（包括受保護的 `.git`/`.codex` 路徑和網路預設值），請參閱[沙盒與核准](/zh-Hant/codex/agent-approvals-security#sandbox-and-approvals)、[可寫入根目錄中的受保護路徑](/zh-Hant/codex/agent-approvals-security#protected-paths-in-writable-roots)，以及[網路存取](/zh-Hant/codex/agent-approvals-security#network-access)。

#### 權限設定檔

Codex 也支援具名權限設定檔，讓您重複使用檔案系統與
網路政策。內建設定檔包括 `:read-only`、`:workspace` 以及
`:danger-full-access`。自訂設定檔使用 `[permissions.<name>]` 資料表，以及
相符的 `default_permissions` 值。請參閱[權限](/zh-Hant/codex/permissions)。

#### Windows 沙盒模式

在 Windows 上以原生方式執行 Codex 時，請在 `windows` 資料表中將原生沙盒模式設為 `elevated`。只有在您沒有系統管理員權限，或提升權限模式的設定失敗時，才使用 `unelevated`。

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### 網頁搜尋模式

Codex 預設會為本機對話啟用網頁搜尋，並從網頁搜尋快取提供結果。此快取是 OpenAI 維護的網頁結果索引，因此快取模式會傳回預先建立索引的結果，而非擷取即時網頁。這可降低接觸任意即時內容所帶來的提示注入風險，但您仍應將網頁結果視為不受信任的內容。如果您使用 `--yolo` 或其他[完整存取權沙盒設定](/zh-Hant/codex/agent-approvals-security#common-sandbox-and-approval-combinations)，網頁搜尋預設會使用即時結果。使用 `web_search` 選擇模式：

- `"cached"`（預設）會從網頁搜尋快取提供結果。
- `"indexed"` 僅在請求受到搜尋索引控管時，才允許存取外部網頁。
- `"live"` 會從網頁擷取最新資料（與 `--search` 相同）。
- `"disabled"` 會停用網頁搜尋工具。

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### 推理投入程度

若模型支援，可調整其推理投入程度。

```toml
model_reasoning_effort = "high"

#### 溝通風格

為支援此功能的模型設定預設溝通風格。

```toml
personality = "friendly" # or "pragmatic" or "none"

您之後可以在進行中的工作階段使用 `/personality` 覆寫此設定；使用 app-server API 時，也可以針對個別對話串或回合進行覆寫。

#### TUI 按鍵對應

在 `tui.keymap` 中自訂終端快速鍵。部分撰寫工具動作會回退使用相符的 `tui.keymap.global` 按鍵繫結；若支援特定上下文的按鍵繫結，則會優先採用。空清單會解除該動作的按鍵繫結。

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### 指令環境

控制 Codex 會將哪些環境變數傳遞給所啟動的指令。使用
以鍵為依據的篩選條件，只保留所需的變數：

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` 預設為 `true`，因此不會自動篩選
名稱中包含 `KEY`、`SECRET` 或 `TOKEN` 的變數。將其設為 `false`
即可啟用這項自動篩選。如需瞭解排除規則、優先順序與
舊版組態，請參閱[Shell 環境
政策](/zh-Hant/codex/config-file/config-advanced#shell-environment-policy)。

#### 記錄檔目錄

覆寫 Codex 寫入本機記錄檔的位置。明確設定 `log_dir` 也會
一併啟用需主動開啟的純文字 TUI 記錄檔 `codex-tui.log`，並將其寫入該目錄。

```toml
log_dir = "/absolute/path/to/codex-logs"

若是一次性執行，也可以從 CLI 設定此值：

```bash
codex -c log_dir=./.codex-log

## 功能旗標

使用 `config.toml` 中的 `[features]` 資料表來啟用或停用選用及實驗性功能。

### 常用功能旗標

| 鍵                  |        預設值        | 成熟度     | 說明                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | 穩定       | 啟用 App（連接器）整合                                                      |
| `goals`              |         true          | 穩定       | 啟用目標持久化與自動接續執行                                        |
| `hooks`              |         true          | 穩定       | 啟用在 `hooks.json` 或內嵌 `[hooks]` 中設定的生命週期掛勾。請參閱 [掛勾](/zh-Hant/codex/hooks)。 |
| `fast_mode`          |         true          | 穩定       | 啟用快速模式選項及 `service_tier = "fast"` 路徑                          |
| `memories`           |         false         | 實驗性 | 啟用 [記憶](/zh-Hant/codex/customization/memories)                                         |
| `multi_agent`        |         true          | 穩定       | 啟用子代理程式協作工具                                                      |
| `personality`        |         true          | 穩定       | 啟用個性選擇控制項                                                    |
| `remote_plugin`      |         true          | 穩定       | 啟用遠端外掛程式目錄                                                         |
| `shell_snapshot`     |         true          | 穩定       | 建立 shell 環境快照，以加快重複執行指令的速度                            |
| `shell_tool`         |         true          | 穩定       | 啟用預設的 `shell` 工具                                                          |
| `unified_exec`       | `true`（Windows 除外） | 穩定       | 使用以 PTY 為後端的統一 exec 工具                                                     |
| `web_search`         |         true          | 已棄用   | 舊版切換選項；請優先使用頂層 `web_search` 設定                                 |
| `web_search_cached`  |         false         | 已棄用   | 舊版切換選項，未設定時會對應至 `web_search = "cached"`                            |
| `web_search_request` |         false         | 已棄用   | 舊版切換選項，未設定時會對應至 `web_search = "live"`                              |

  此表列出供使用者使用的常見旗標，並未涵蓋所有內部功能或
  仍在開發中的功能。「成熟度」欄使用
  「實驗性」、「Beta」和「穩定」等標籤。若要瞭解如何解讀這些標籤，請參閱 [功能
  成熟度](/zh-Hant/codex/feature-maturity)。

省略功能設定鍵，即可沿用其預設值。

如需生命週期掛勾的組態說明，請參閱 [掛勾](/zh-Hant/codex/hooks)。

### 啟用功能

- 在 `config.toml` 中，於 `[features]` 下新增 `feature_name = true`。
- 在 CLI 中執行 `codex --enable feature_name`。
- 若要啟用多項功能，請執行 `codex --enable feature_a --enable feature_b`。
- 若要停用某項功能，請在 `config.toml` 中將該設定鍵設為 `false`。
