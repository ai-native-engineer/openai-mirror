<!-- source: https://learn.chatgpt.com/zh-Hant/docs/config-file/environment-variables -->

Codex 使用 `config.toml` 儲存持久設定。環境變數則可用於
僅在 Shell 範圍內生效的覆寫設定、自動化密鑰、安裝程式行為或診斷。

本頁列出 Codex 直接讀取、穩定且公開的環境變數。
不包括內部開發變數、測試變數，或
透過
[`env_key`](/zh-Hant/codex/config-file/config-advanced#custom-model-providers) 自行指定的供應商專用密鑰名稱。

## 核心位置

| 變數            | 使用元件                                    | 預設值      | 說明                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI、IDE 擴充功能、app-server、安裝程式 | `~/.codex`   | 設定 Codex 狀態資料的根目錄，包括組態、身分驗證資料、記錄、工作階段、技能與獨立套件中繼資料。若設定此變數，該目錄必須已存在。 |
| `CODEX_SQLITE_HOME` | CLI 與 app-server 狀態資料                   | `CODEX_HOME` | 設定以 SQLite 為後端的狀態資料儲存位置。`sqlite_home` 組態選項具有優先權。相對路徑會以目前的工作目錄為基準解析。           |

如需進一步了解儲存在 `CODEX_HOME` 下的檔案，請參閱
[組態與狀態資料的位置](/zh-Hant/codex/config-file/config-advanced#config-and-state-locations)。

## 安裝程式變數

這些變數適用於透過
`https://chatgpt.com/codex/install.sh` 和
`https://chatgpt.com/codex/install.ps1` 提供的獨立安裝指令碼。

| 變數                | 預設值                                                                              | 說明                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | 將值設為 `1`、`true` 或 `yes` 即可略過安裝程式提示。提示會採用預設回應，因此請將此設定用於透過指令碼進行的安裝與更新，而不要用於首次執行時的設定。 |
| `CODEX_INSTALL_DIR`     | `~/.local/bin`（macOS/Linux）；`%LOCALAPPDATA%\Programs\OpenAI\Codex\bin`（Windows） | 變更對使用者可見的 `codex` 指令的安裝位置。獨立套件快取仍位於 `CODEX_HOME/packages/standalone`。                        |

若要進行無人介入安裝，請在 Shell 中設定 `CODEX_NON_INTERACTIVE=1`，並由該 Shell 執行
已下載的安裝程式：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## 身分驗證與網路

| 變數                           | 使用元件                                          | 說明                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec、review、TypeScript SDK、遠端 exec-server | 為非互動式 Codex 程序提供 API 金鑰。執行受程式碼庫控制的程式碼時，請直接在指令中設定此變數，而不要套用至整個作業。             |
| `CODEX_ACCESS_TOKEN`               | CLI、app-server、受信任的自動化作業              | 為受信任的自動化作業提供 ChatGPT 或 Codex 存取權杖。若要保存登入狀態，請透過管線將權杖傳送至 `codex login --with-access-token`。             |
| `OPENAI_FEDERATION_RULE_ID`        | 工作負載身分                                | 選擇為工作負載設定的聯合規則。                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | 工作負載身分                                | 指向包含目前 OIDC Token 或 SPIFFE JWT-SVID 的檔案絕對路徑。                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | 工作負載身分                                | 可選擇提供受限的 JSON 識別碼，供用戶端回報稽核歸屬。這不會影響身分驗證或授權。         |
| `CODEX_CA_CERTIFICATE`             | HTTPS、登入與 WebSocket 用戶端              | 指向 PEM CA 憑證套件，適用於有企業 TLS 攔截或私有根憑證的環境。其優先順序高於 `SSL_CERT_FILE`。 |
| `SSL_CERT_FILE`                    | HTTPS、登入與 WebSocket 用戶端              | 未設定 `CODEX_CA_CERTIFICATE` 時使用的備援 PEM CA 憑證套件路徑。                                                                               |

若要設定供應商 API 金鑰，請將
[`env_key`](/zh-Hant/codex/config-file/config-advanced#custom-model-providers) 設定於模型供應商的
組態中。Codex 會讀取該組態指定的變數，因此變數
名稱本身並非固定的 Codex 環境變數。

如需了解自動化密鑰的處理方式，請參閱
[使用 API 金鑰進行身分驗證](/zh-Hant/codex/non-interactive-mode#use-api-key-auth)。
如需設定存取權杖，請參閱 [存取權杖](/zh-Hant/codex/enterprise/access-tokens)。
如需設定工作負載身分，請參閱
[工作負載身分聯合](/zh-Hant/codex/enterprise/workload-identity)。

## 診斷

| 變數   | 使用元件            | 說明                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI 與 app-server | 控制 Rust 記錄的篩選條件與詳細程度。除非設定詳細程度更高的值，否則 `codex exec` 預設只會輸出 `error` 等級的記錄。 |

`RUST_LOG` 可接受 `error`、`warn`、`info`、`debug` 和
`trace` 等值。它也接受針對特定目標的 Rust 記錄篩選條件，例如
`codex_core=debug,codex_tui=debug`。

互動式 CLI 預設會將診斷資訊記錄在有容量上限的本機儲存區，但
純文字 `codex-tui.log` 檔案須另行啟用。請明確設定 `log_dir`，以取得
疑難排解所需的純文字記錄檔：

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

在非互動模式中，`codex exec` 會直接輸出訊息，而不會寫入
獨立的 TUI 記錄檔。
