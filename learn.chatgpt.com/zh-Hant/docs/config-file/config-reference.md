<!-- source: https://learn.chatgpt.com/zh-Hant/docs/config-file/config-reference -->

本頁提供可搜尋的 Codex 設定檔參考資料。如需概念說明和範例，請先參閱[基本設定](/zh-Hant/codex/config-file/config-basic)和[進階設定](/zh-Hant/codex/config-file/config-advanced)。

## `config.toml`

使用者層級組態儲存在 `~/.codex/config.toml`。您也可以在 `.codex/config.toml` 檔案中加入專案範圍的覆寫設定。只有在您信任專案時，Codex 才會載入專案範圍的設定檔。

專案範圍的組態無法覆寫本機的提供者、身分驗證、
由主機管理的應用程式請求中繼資料、通知、設定檔選擇
或遙測路由設定鍵。如果 `openai_base_url`、
`chatgpt_base_url`、`apps_mcp_product_sku`、`model_provider`、
`model_providers`、`notify`、`profile`、`profiles`、
`experimental_realtime_ws_base_url` 和 `otel` 出現在
專案內的 `.codex/config.toml` 中，Codex 會忽略這些設定；請改將提供者、通知和遙測
設定鍵放在使用者層級組態中。[設定檔](/zh-Hant/codex/config-file/config-advanced#profiles)與
`config.toml` 存放於同一目錄，路徑為 `$CODEX_HOME/profile-name.config.toml`；請使用
`--profile profile-name` 選取。

如需瞭解沙盒與核准設定鍵（`approval_policy`、`sandbox_mode` 和 `sandbox_workspace_write.*`），請搭配本參考資料查閱[沙盒與核准](/zh-Hant/codex/agent-approvals-security#sandbox-and-approvals)、[可寫入根目錄中的受保護路徑](/zh-Hant/codex/agent-approvals-security#protected-paths-in-writable-roots)和[網路存取](/zh-Hant/codex/agent-approvals-security#network-access)。如需測試版權限設定檔的資訊，請參閱[權限](/zh-Hant/codex/permissions)。

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "要使用的模型（例如 `gpt-5.5`）。",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "供 `/review` 使用的選用模型覆寫設定（預設為目前工作階段的模型）。",
    },
    {
      key: "model_provider",
      type: "string",
      description: "來自 `model_providers` 的提供者 ID（預設：`openai`）。",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "內建 `openai` 模型提供者的基礎 URL 覆寫設定。",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "目前模型可用的上下文視窗 Token 數量。",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "觸發自動壓縮歷史記錄的 Token 閾值（未設定時使用模型預設值）。",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "控制自動壓縮閾值是計入目前的完整上下文（`total`，預設值），還是僅計入沿用的壓縮視窗前綴之後的增長量（`body_after_prefix`）。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "啟動時載入的 JSON 模型目錄路徑（選用）。所選的 `$CODEX_HOME/profile-name.config.toml` 設定檔可個別覆寫此路徑。",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "使用 `--oss` 執行時採用的預設本機提供者（若未設定，預設會提示您選擇）。",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "控制 Codex 在執行指令前何時暫停並要求核准。您也可以使用 `approval_policy = { granular = { ... } }`，允許顯示或自動拒絕特定類別的提示，同時讓其他提示維持互動方式。`on-failure` 已棄用；互動式執行請使用 `on-request`，非互動式執行請使用 `never`。",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "設為 `true` 時，允許顯示沙盒權限提升核准提示。",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "設為 `true` 時，允許顯示由 execpolicy `prompt` 規則觸發的核准提示。",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "設為 `true` 時，允許顯示 MCP 資訊請求提示，而不會自動拒絕。",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "設為 `true` 時，允許顯示來自 `request_permissions` 工具的提示。",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "設為 `true` 時，允許顯示技能指令碼核准提示。",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "指定在 `on-request` 或細部核准政策下，由誰審查符合條件的核准提示。預設為 `user`；`auto_review` 會使用審查者子代理程式。此設定不會變更沙盒機制，也不會審查沙盒內已允許的操作。",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "用於自動審查的本機 Markdown 政策指示。受管理的 `guardian_policy_config` 優先。空白值會被忽略。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "允許以 Shell 為基礎的工具使用登入 Shell 語意。預設為 `true`；設為 `false` 時，會拒絕 `login = true` 請求，省略 `login` 時則預設使用非登入 Shell。",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "指令執行期間檔案系統與網路存取的沙盒政策。",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "當 `sandbox_mode = \"workspace-write\"` 時，額外允許寫入的根目錄。",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "允許 workspace-write 沙盒內的對外網路存取。",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "在 workspace-write 模式下，將 `$TMPDIR` 排除在可寫入根目錄之外。",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "在 workspace-write 模式下，將 `/tmp` 排除在可寫入根目錄之外。",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Codex 在 Windows 上原生執行時使用的 Windows 專用原生沙盒模式。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "在 Windows 原生環境中，預設會在私有桌面上執行最終的沙盒子處理程序。只有在需要與舊版 `Winsta0\\\\Default` 行為相容時，才設為 `false`。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "設為 `false` 可限制瀏覽器歷史記錄的存取。受管理的要求可強制執行此限制。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "瀏覽器來源的後備限制。支援 `access`、`uploads`、`downloads` 和 `full_cdp_access`，各項皆可設為 `allow` 或 `deny`。",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "針對個別來源的瀏覽器限制，欄位與 `browser_use.default_origin_policy` 相同。須包含 HTTP 或 HTTPS 通訊協定，可選擇指定連接埠；請勿包含路徑、查詢字串或片段。本機設定值無法放寬受管理的拒絕規則。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "「電腦」功能存取原生應用程式時的後備政策。可透過個別應用程式項目提供政策；本機組態無法放寬受管理的限制。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "以套件組合識別碼為索引鍵的 macOS 原生應用程式存取設定。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "以應用程式使用者模型識別碼（AUMID）為索引鍵的 Windows 封裝應用程式存取設定。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Windows 執行檔存取規則。每項規則都必須包含 `publisher_name`、`product_name` 和 `access`（`allow` 或 `deny`）；`binary_name` 為選用。",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "「電腦」無須顯示提示即可開啟的 Windows 應用程式識別碼。不在清單中的應用程式需要核准；請從 ChatGPT 桌面版應用程式的「電腦」設定中移除已儲存的項目。",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "發出通知時執行的指令；會接收來自 Codex 的 JSON 承載資料。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "啟動時檢查是否有 Codex 更新（僅在集中管理更新時才設為 false）。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "允許所有本機用戶端透過 `/feedback` 提交意見回饋（預設：true）。",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "啟用或停用此電腦／設定檔的分析功能。未設定時，採用用戶端預設值。",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "保留供日後使用；建議優先使用 `model_instructions_file` 或 `AGENTS.md`。",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "注入工作階段的額外開發人員指示（選用）。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Codex 寫入記錄檔的目錄；預設為 `$CODEX_HOME/log`。明確設定此值也會在該目錄中啟用需主動選用的純文字 TUI 記錄檔 `codex-tui.log`。",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex 儲存 SQLite 狀態資料庫的目錄；該資料庫供智慧體作業及其他可恢復的執行階段狀態使用。",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "歷史記錄壓縮提示詞的內嵌覆寫設定。",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "用來取代內建指示，而不是使用 `AGENTS.md`。",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "宣告支援 `supportsPersonality` 的模型所採用的預設溝通風格；可針對個別對話串或輪次覆寫，也可透過 `/personality` 覆寫。",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "新輪次的偏好服務層級。請使用 `fast` 或目前模型宣告支援的其他層級；`fast` 對應至請求值 `priority`。",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "從檔案載入壓縮提示詞的覆寫設定（實驗性）。",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "可用技能目錄的 Token 預算。預設為模型上下文視窗的 2%。明確設定的值上限為 `10000` 個 Token。",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "儲存在 config.toml 中的各技能啟用狀態覆寫設定。",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "包含 `SKILL.md` 的技能資料夾路徑。",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "啟用或停用所參照的技能。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "依 ID 啟用或停用特定應用程式／連接器（預設：true）。",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "所有應用程式的預設啟用狀態，除非個別應用程式有覆寫設定。",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "設有 `destructive_hint = true` 的應用程式工具的預設允許／拒絕設定。",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "設有 `open_world_hint = true` 的應用程式工具的預設允許／拒絕設定。",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "應用程式工具核准提示的預設審查者，除非個別應用程式有覆寫設定。省略時，應用程式會繼承頂層的 `approvals_reviewer` 值。",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "未針對個別應用程式或工具設定覆寫時，應用程式工具的預設核准行為。",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "允許或封鎖此應用程式中宣告 `destructive_hint = true` 的工具。",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "允許或封鎖此應用程式中宣告 `open_world_hint = true` 的工具。",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "此應用程式中工具的預設啟用狀態；如有個別工具的覆寫設定，則以該設定為準。",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "此應用程式工具核准提示的審查者。覆寫 `apps._default.approvals_reviewer`。",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此應用程式中工具的預設核准行為；如有個別工具的覆寫設定，則以該設定為準。",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "個別應用程式工具（例如 `repos/list`）的啟用狀態覆寫設定。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "單一應用程式工具的核准行為覆寫設定。",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "允許工具建議其他可探索的連接器或外掛程式。每個項目使用 `type = \"connector\"` 或 `\"plugin\"`，以及一個 `id`。",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "停用特定可探索連接器或外掛程式的建議。每個項目使用 `type = \"connector\"` 或 `\"plugin\"`，以及一個 `id`。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "啟用應用程式（連接器）整合（穩定；預設啟用）。應用程式與連接器的流量不受沙盒指令的網路代理伺服器或其網域允許清單控制。",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "啟用從 `hooks.json` 或內嵌的 `[hooks]` 組態載入的生命週期掛勾。`features.codex_hooks` 是已棄用的別名。",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "啟用程式碼模式的功能組態。此功能仍在開發中，預設關閉。",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "程式碼模式會從巢狀程式碼模式的工具指引中排除這些工具命名空間，也不會向執行器公開這些命名空間。",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "程式碼模式只能透過直接工具呼叫使用的工具命名空間。",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "啟用實驗性上下文管理（預設關閉）。此功能利用筆記和可搜尋的歷史記錄保留累積的細節，而非反覆將上下文壓縮成單一摘要。必須使用 Plus、Pro 或 Pro Lite 方案登入 ChatGPT。",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "啟用推演預算追蹤。此功能仍在開發中，預設關閉。啟用後，必須設定 `features.rollout_budget.limit_tokens`。",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "推演預算追蹤的 Token 上限，必須為正數。啟用推演預算時，必須設定此項。",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "推演預算提醒之間的 Token 間隔，必須為正數。預設為 `limit_tokens` 的 10%，且至少為 1 個 Token。",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "推演預算計算中取樣 Token 的乘數，必須為有限的非負數。預設為 `1.0`。",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "推演預算計算中預填 Token 的乘數，必須為有限的非負數。預設為 `1.0`。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "在 `config.toml` 中內嵌設定的生命週期掛勾。使用與 `hooks.json` 相同的事件結構描述；如需範例和支援的事件，請參閱掛勾指南。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "用於 `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit`、`Stop` 或 `Interrupt` 等掛勾事件的比對器群組。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "比對器群組的掛勾處理常式。支援指令掛勾和 MCP 工具掛勾；提示詞掛勾與智慧體掛勾的處理常式會經過剖析，但不會執行。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "在背景執行指令掛勾，而不延遲觸發該掛勾的作業。預設為 `false`；`SessionEnd` 一律同步執行。請參閱[在背景執行掛勾](/codex/hooks#run-hooks-in-the-background)。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "每個處理常式適用的概略 Token 閾值；超過閾值時，會將過大的 `additionalContext` 儲存至磁碟，並向模型顯示較短的預覽。預設為 `2500`；設為 `0` 時，會將完整上下文直接傳給模型。請參閱[過大的掛勾輸出](/codex/hooks#large-hook-output)。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "覆寫指令掛勾所用的指令，僅適用於 Windows。也可使用 TOML 別名 `command_windows`。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "啟用[記憶](/codex/customization/memories)（預設關閉）。",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "建立初始工具目錄時，選用 MCP 伺服器共用的等待時間。預設為 `1000`。設為 `0` 時，則改為依各伺服器的 `startup_timeout_sec` 等待。",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "用於啟動 MCP stdio 伺服器的指令。",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "傳遞給 MCP stdio 伺服器指令的引數。",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "轉送至 MCP stdio 伺服器的環境變數。",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "要額外加入 MCP stdio 伺服器允許清單的環境變數。字串項目預設使用 `source = \"local\"`；只有搭配以執行器為後端的遠端 stdio 時，才能使用 `source = \"remote\"`。",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "MCP stdio 伺服器程序的工作目錄。",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "MCP 可串流 HTTP 伺服器的端點。",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "MCP HTTP 伺服器的備援身分驗證方式，優先順序在已設定的 bearer Token 和授權標頭之後。`oauth`（預設）會在有可用憑證時使用已儲存的 MCP OAuth 憑證。`chatgpt` 會對受信任的第一方 ChatGPT 來源使用目前的 ChatGPT 工作階段，並以已儲存的 OAuth 憑證作為備援。如果所有憑證來源都無法提供憑證，兩種模式都能在未經身分驗證的情況下連線。",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "預先註冊的 OAuth 用戶端 ID，用於與此 MCP 伺服器進行授權及 Token 交換。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "伺服器專屬的 OAuth 回呼。當支援簽發者識別，或 URL 已以該伺服器專屬的回呼 ID 結尾時，預先註冊的用戶端會沿用此回呼。否則，Codex 會使用附加了該 ID 的全域或預設回呼。沒有預先註冊 ID 的用戶端會在用戶端註冊期間使用此回呼。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "此 MCP 伺服器的固定 OAuth 回呼接聽連接埠。覆寫 `mcp_oauth_callback_port`。若直接使用回送位址回呼，且 URL 明確指定連接埠，請將接聽連接埠設為相同值。",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "提供 MCP HTTP 伺服器 bearer Token 的環境變數。",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "每個 MCP HTTP 請求中包含的靜態 HTTP 標頭。",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "輸出包含 HTTP 標頭名稱和值的 JSON 物件的本機指令。僅支援從本機連線的 HTTP MCP 伺服器。明確指定的 bearer Token 和 OAuth 憑證，優先於輔助程式提供的 Authorization 標頭。",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "供 MCP HTTP 伺服器使用、值由環境變數填入的 HTTP 標頭。",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "停用 MCP 伺服器，但保留其組態。",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "設為 true 時，若這個已啟用的 MCP 伺服器無法初始化，啟動或恢復就會失敗。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "覆寫 MCP 伺服器預設的 10 秒啟動逾時設定。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "以毫秒為單位的 `startup_timeout_sec` 別名。",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "覆寫 MCP 伺服器每個工具預設的 60 秒逾時設定。",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "允許 MCP 伺服器公開的工具名稱清單。",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "MCP 伺服器在 `enabled_tools` 之後套用的拒絕清單。",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此伺服器上 MCP 工具的預設核准行為；如有個別工具的覆寫設定，則以該設定為準。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "此伺服器上單一 MCP 工具的核准行為覆寫設定。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "單一 MCP 工具輸出的 Token 預算，尚未計入標準的 20% 序列化預留額度。覆寫模型針對該工具的預設輸出截斷預算。",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "向該 MCP 伺服器進行身分驗證時，要請求的 OAuth 授權範圍。",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "MCP 登入時可選擇包含的 RFC 8707 OAuth 資源參數。",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "MCP 伺服器的實驗性執行位置設定。`remote` 會透過遠端執行器環境啟動 stdio 伺服器；尚未實作可串流 HTTP 伺服器的遠端執行位置功能。",
    },
    {
      key: "agents",
      type: "table",
      description:
        "多智慧體設定與自訂角色宣告。純量設定名稱屬於保留名稱，不能作為自訂角色名稱。",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "啟用或停用多智慧體工具（預設為 true）。",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "為智慧體建立的執行緒可同時保持開啟的數量上限，不包含主要執行緒。若未設定，Codex 會選擇預設值。",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "`agents.max_concurrent_threads_per_session` 的舊版別名。",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "建立智慧體時使用的預設模型。若建立時明確指定模型，則以指定的模型為準。",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "建立智慧體時使用的預設推理程度。若建立時明確指定推理程度，則以指定的程度為準。",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "智慧體的輪次中斷時，記錄一則模型可見的訊息（預設為 true）。",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "Codex 選擇並建立該類型智慧體時，向其顯示的角色指引。",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "該角色的 TOML 組態層路徑；相對路徑會以宣告該角色的設定檔所在位置為基準解析。",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "設為 `false` 時，新建立的執行緒不會儲存為記憶生成的輸入資料。預設為 `true`。",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "設為 `false` 時，Codex 不會將現有記憶注入日後的工作階段。預設為 `true`。",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "設為 `true` 時，使用 MCP 工具呼叫、網頁搜尋或工具搜尋等外部上下文的討論串，不會用於產生記憶。預設為 `false`。舊版別名：`memories.no_memories_if_mcp_or_web_search`。",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "保留供全域整合使用的近期原始記憶數量上限。預設為 `256`，上限為 `4096`。",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "記憶自上次使用後仍可納入整合的最長天數。預設為 `30`，值會限制在 `0`-`365` 範圍內。",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "可納入記憶產生流程的討論串最長存續時間。預設為 `30`，值會限制在 `0`-`90` 範圍內。",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "每次啟動處理的候選執行紀錄數量上限。預設為 `16`，上限為 `128`。",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "討論串納入記憶產生流程前所需的最短閒置時間。預設為 `6`，值會限制在 `1`-`48` 範圍內。",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "開始產生記憶前，Codex 速率限制時段內必須保有的最低剩餘額度百分比。預設為 `25`，值會限制在 `0`-`100` 範圍內。",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "個別討論串記憶擷取的模型覆寫設定（選用）。",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "全域記憶整合的模型覆寫設定（選用）。",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "使用以 PTY 為基礎的統一 exec 工具（穩定功能；除 Windows 外，預設啟用）。",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "建立 shell 環境快照，加快重複執行指令的速度（穩定功能；預設啟用）。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "啟用多智慧體協作工具（`spawn_agent`、`send_input`、`resume_agent`、`wait_agent` 和 `close_agent`）（穩定功能；預設啟用）。",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "啟用目標持久化與自動接續功能（穩定功能；預設啟用）。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "啟用遠端外掛程式目錄（穩定功能；預設啟用）。",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "啟用個性選擇控制項（穩定功能；預設啟用）。",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "啟動沙盒指令使用的網路代理伺服器（實驗性功能；預設關閉）。除非由管理員管理的 `experimental_network` 要求已啟用並啟動代理伺服器，否則必須啟用此功能，才能強制執行權限設定檔的網域規則。設定 `domains` 等功能層級的政策選項時，請使用資料表形式。此功能不會篩選網頁搜尋、應用程式、MCP 或其他託管工具。",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "當指令的網路存取已啟用時，啟動沙盒指令的網路代理伺服器。預設為 `false`；代理伺服器關閉時，不會強制執行權限設定檔的網域規則。",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "沙盒網路的網域政策。預設未設定，因此在新增 `allow` 規則前，不允許存取任何外部目的地。支援精確主機比對、僅涵蓋子網域的 `*.example.com`、涵蓋網域本身及其子網域的 `**.example.com`，以及全域 `*` 允許規則；建議使用限定範圍的規則，因為 `*` 會廣泛開放公用網路的對外存取。請為要封鎖的目的地新增 `deny` 規則；發生衝突時以 `deny` 為準。",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "沙盒網路的 Unix 通訊端政策。預設未設定；請為允許的通訊端新增 `allow` 項目。",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "允許更廣泛的本機或私人網路存取。預設為 `false`；針對確切本機 IP 常值或 `localhost` 設定的允許規則，仍可允許存取特定本機目標。",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "提供 SOCKS5 支援。預設為 `true`。",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "允許透過 SOCKS5 使用 UDP。預設為 `true`。",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "允許透過環境中設定的上游代理伺服器進行串接。預設為 `true`。",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允許監聽器使用非回送位址。預設為 `false`；啟用後，可能讓 localhost 以外的來源也能存取代理伺服器監聽器。",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允許存取任意 Unix 通訊端目的地，而非僅限允許清單中的目的地。預設為 `false`；僅限在嚴格受控的環境中使用。",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "沙盒網路使用的 HTTP 監聽器 URL。預設為 `\"http://127.0.0.1:3128\"`。",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "SOCKS5 監聽器 URL。預設為 `\"http://127.0.0.1:8081\"`。",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "已棄用的舊版切換設定；建議改用頂層 `web_search` 設定。",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "已棄用的舊版切換設定。若未設定 `web_search`，true 會對應至 `web_search = \"cached\"`。",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "已棄用的舊版切換設定。若未設定 `web_search`，true 會對應至 `web_search = \"live\"`。",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "啟用用來執行指令的預設 `shell` 工具（穩定功能；預設啟用）。",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "在支援的情況下，使用 zstd 壓縮串流請求主體（穩定功能；預設啟用）。",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "允許在技能缺少 MCP 相依套件時提示使用者並加以安裝（穩定功能；預設啟用）。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "啟用 TUI 中由模型目錄提供的服務層級選擇功能；若目前使用的模型宣告支援快速層級指令，也會一併啟用（穩定功能；預設啟用）。",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "回合執行期間，防止電腦進入睡眠（實驗性功能；預設關閉）。",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "隱藏啟用開發中功能旗標時顯示的警告。",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "自訂供應商定義。內建供應商 ID（`openai`、`ollama` 和 `lmstudio`）均為保留值，無法覆寫。",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "自訂模型供應商的顯示名稱。",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "模型供應商的 API 基底 URL。",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "提供供應商 API 金鑰的環境變數。",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "供應商 API 金鑰的設定指引（選用）。",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "直接設定的供應商 Bearer Token（不建議使用；請改用 `env_key`）。",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "此供應商使用 OpenAI 身分驗證（預設為 false）。",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "供應商使用的通訊協定。唯一支援的值是 `responses`；若省略，預設也會使用此值。",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "附加至供應商請求的額外查詢參數。",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "新增至供應商請求的靜態 HTTP 標頭。",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "當環境變數存在時，以其值填入的 HTTP 標頭。",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "向供應商發出 HTTP 請求時的重試次數（預設：4）。",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "SSE 串流中斷時的重試次數（預設：5）。",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "SSE 串流的閒置逾時，以毫秒為單位（預設：300000）。",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "該供應商是否支援 Responses API 的 WebSocket 傳輸方式。",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "宣告支援相容的獨立網頁搜尋端點（預設：false）。獨立搜尋功能仍在開發中，且預設關閉；供應商相容並不代表此功能會自動啟用。",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "自訂供應商透過指令取得 Bearer Token 的組態。請勿與 `env_key`、`experimental_bearer_token` 或 `requires_openai_auth` 同時使用。",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Codex 需要 Bearer Token 時要執行的指令。該指令必須將 Token 輸出至 stdout。",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "傳給 Token 指令的引數。",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "Token 指令的最長執行時間，以毫秒為單位（預設：5000）。",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Codex 主動更新 Token 的間隔，以毫秒為單位（預設：300000）。設為 `0` 時，僅在身分驗證重試後更新。",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "Token 指令的工作目錄。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "內建 `amazon-bedrock` 供應商使用的 AWS 設定檔名稱。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "內建 `amazon-bedrock` 供應商使用的 AWS 區域。",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "調整受支援模型的推理投入程度（僅限 Responses API；對 `xhigh` 的支援依模型而定）。",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "規劃模式專用的推理覆寫設定。若未設定，規劃模式會使用內建預設組合的預設值。",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "選擇推理摘要的詳細程度，或完全停用摘要。",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "GPT-5 Responses API 輸出詳細程度的覆寫設定（選用）；若未設定，會採用所選模型或預設組合的預設值。",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "強制指定 Codex 傳送或不傳送推理中繼資料。",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "建立子程序時，環境變數繼承的基本規則。",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "在執行其他篩選條件前，保留名稱包含 KEY、SECRET 或 TOKEN 的變數（預設：true）。設為 false 可自動排除名稱含有機密資訊關鍵字的變數。",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "標準的環境變數模式篩選條件，不區分大小寫。包含項目會建立允許清單，但無法還原已排除的值。明確指定的 `set` 值會在排除操作後套用。請勿在同一層中將篩選條件與舊版 `exclude` 或 `include_only` 陣列混用。",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "舊版環境變數排除模式。新的組態請使用 `shell_environment_policy.filters`；請勿在同一層中混用兩種形式。",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "舊版環境變數模式允許清單。新的組態請使用 `shell_environment_policy.filters`；請勿在同一層中混用兩種形式。",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "在排除操作後注入的明確環境變數值；包含篩選條件仍可將其移除。",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "建立子程序時使用使用者的 Shell 設定檔。",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "用來標示專案根目錄的檔名清單；向上搜尋父目錄以尋找專案根目錄時使用。",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "建立專案指示時，從 `AGENTS.md` 讀取的位元組數上限。",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "找不到 `AGENTS.md` 時，會嘗試讀取的其他檔名。",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "控制 Codex 是否將工作階段逐字紀錄儲存至 history.jsonl。",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "將個別工具／函式輸出儲存至歷史紀錄的 Token 預算。",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "不傳入內容的 `write_stdin` 輪詢（背景終端輪詢）所允許的最長等待時間，以毫秒為單位。預設為 `300000`（5 分鐘）。取代舊的 `background_terminal_timeout` 鍵。",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "設定後，會透過刪除最舊的項目，將歷史紀錄檔案大小限制在指定的位元組數內。",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "用於開啟 Codex 輸出中引用內容的 URI 配置（預設：`vscode`）。",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "套用至所發出 OpenTelemetry 事件的環境標記（預設：`dev`）。",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "選擇 OpenTelemetry 匯出器，並提供相關的端點中繼資料。",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "選擇 OpenTelemetry 追蹤匯出器，並提供相關的端點中繼資料。",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "選擇 OpenTelemetry 指標匯出器（預設為 `statsig`）。",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "選擇將原始使用者提示詞隨 OpenTelemetry 紀錄一併匯出。",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 紀錄的匯出器端點。",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 匯出器使用的通訊協定。",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 匯出器請求中包含的靜態標頭。",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "OTEL 紀錄的追蹤匯出器端點。",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP 追蹤匯出器使用的通訊協定。",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL 追蹤匯出器請求中包含的靜態標頭。",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 匯出器 TLS 使用的 CA 憑證路徑。",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 匯出器 TLS 使用的用戶端憑證路徑。",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 匯出器 TLS 使用的用戶端私密金鑰路徑。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL 追蹤匯出器 TLS 使用的 CA 憑證路徑。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL 追蹤匯出器 TLS 使用的用戶端憑證路徑。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL 追蹤匯出器 TLS 使用的用戶端私密金鑰路徑。",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "僅限使用者層級。為 ChatGPT 桌面版應用程式定義額外的 **開啟方式** 目標。請參閱[新增自訂檔案處理程式](/codex/config-file/config-advanced#add-custom-file-handlers)，瞭解相關範例與處理程式 ID 限制。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "顯示在 **開啟方式** 選單中的名稱。必填。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "處理程式圖示的隨附資源路徑、以 Base64 編碼的 `data:image/...` URL、檔案 URI 或本機絕對路徑。必填；不支援的來源會改用預設 VS Code 圖示。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "用於偵測與啟動的可執行檔路徑或指令名稱。必填。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "插入指令與檔案輸入之間的引數（預設：`[]`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "應用程式將檔案輸入傳送至處理程式的方式（預設：`path`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "針對 SSH 工作區中的檔案提供此處理程式（預設：`false`）。",
    },
    {
      key: "tui",
      type: "table",
      description:
        "TUI 專用選項，例如啟用內嵌桌面通知。",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "啟用 TUI 通知，也可選擇限制為特定事件類型。",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "終端通知使用的方式（預設：auto）。",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "控制 TUI 通知是僅在終端未取得焦點時觸發，還是不論焦點狀態皆會觸發。預設為 `unfocused`。",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "啟用終端動畫（歡迎畫面、微光效果、旋轉指示器）（預設：true）。",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "控制 TUI 是否使用替代畫面（預設：auto；auto 在 Zellij 中會略過替代畫面，以保留回捲內容）。",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "恢復工作階段或為其建立分支時使用的工作目錄。若未設定，而目前目錄與工作階段所儲存的目錄不同，Codex 會要求你選擇。",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "啟動撰寫工具時使用 Vim 一般模式，而非插入模式（預設：false）。仍可在每個工作階段使用 `/vim` 切換。",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "以原始回捲模式啟動 TUI，方便選取並複製終端內容（預設：false）。可使用 `/raw` 或預設的 `alt-r` 按鍵繫結切換。",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "在 TUI 歡迎畫面中顯示新手引導工具提示（預設：true）。",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "TUI 底部狀態列項目識別碼的有序清單。`null` 會停用狀態列。",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "終端視窗／分頁標題項目識別碼的有序清單。預設為 `[\"spinner\", \"project\"]`；`null` 會停用標題更新。",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "語法醒目提示佈景主題的覆寫設定（佈景主題名稱採用 kebab-case 格式）。",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "TUI 動作的鍵盤快速鍵繫結。支援的上下文包括 `global`、`chat`、`composer`、`editor`、`vim_normal`、`vim_operator`、`vim_text_object`、`pager`、`list` 和 `approval`。部分撰寫工具動作會使用相符的 `tui.keymap.global` 繫結作為備用；若支援特定上下文的繫結，則優先使用該繫結。",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "解除該動作在此按鍵對應上下文中的繫結。按鍵名稱使用標準化字串，例如 `ctrl-a`、`shift-enter`、`page-down` 或 `minus`。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "在不變更外掛程式資訊清單的情況下，啟用或停用已安裝外掛程式隨附的 MCP 伺服器。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "外掛程式提供的 MCP 伺服器上各項工具的預設核准行為。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "外掛程式提供的 MCP 伺服器所公開的工具允許清單。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "外掛程式提供的 MCP 伺服器的拒絕清單，會在 `enabled_tools` 之後套用。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "針對外掛程式提供的 MCP 工具，個別覆寫核准行為。",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "以模型 Slug 為鍵的啟動工具提示內部狀態。",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "同時隱藏 TUI 和 `codex exec` 輸出中的推理事件。",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "當使用中的模型輸出原始推理內容時，將其顯示。",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "停用 TUI 對短時間大量貼上的偵測。",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "追蹤是否已確認 Windows 初次使用導覽（僅限 Windows）。",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "覆寫 ChatGPT 登入流程使用的基底 URL。",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "控制 CLI 儲存快取認證的位置（auth.json 檔案或作業系統鑰匙圈）。",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "儲存 MCP OAuth 認證的偏好位置。",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "選用的全域固定連接埠，供 MCP OAuth 登入期間的本機 HTTP 回呼伺服器使用。伺服器專屬的 `oauth.callback_port` 設定具有較高優先順序。若兩者皆未設定，Codex 會繫結至作業系統選擇的臨時連接埠。",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "選用的 MCP OAuth 登入基底回呼 URL，例如 devbox 入口 URL。若授權伺服器支援簽發者識別，新加入的預先註冊用戶端會直接使用此 URL，不加以修改；未儲存回呼的既有用戶端則會附加伺服器專屬的回呼 ID。若不支援簽發者識別，任何預先註冊的 MCP 伺服器只要其設定的回呼缺少必要 ID，就會改用此 URL 並附加該 ID。回呼 URL 中的連接埠不會決定接聽器使用的連接埠。",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "啟用統一執行功能的舊名稱；建議使用 `[features].unified_exec` 或 `codex --enable unified_exec`。",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "選用的網頁搜尋工具組態。物件形式可設定搜尋上下文大小、允許搜尋的網域，以及使用者的大致位置。這些搜尋網域篩選條件與沙盒內指令的網路網域規則各自獨立，不會限制連接器或 MCP 伺服器。",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "啟用本機圖片附件工具 `view_image`。",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "網頁搜尋模式（預設為 `\"cached\"`；cached 使用 OpenAI 維護的索引，不存取外部網頁；indexed 僅允許經搜尋索引管控的外部存取；若使用 `--yolo` 或其他完整存取權沙盒設定，則預設為 `\"live\"`）。使用 `\"live\"` 可進行不受限制的即時擷取，使用 `\"disabled\"` 則可移除此工具。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "套用至沙盒內工具呼叫的預設權限設定檔名稱。內建設定檔為 `:read-only`、`:workspace` 和 `:danger-full-access`；自訂設定檔名稱必須有對應的 `[permissions.<name>]` 表。請勿與 `sandbox_mode` 或 `[sandbox_workspace_write]` 同時使用。",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "此具名設定檔的易讀說明。設定檔不會透過 `extends` 繼承父設定檔的說明。",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "選用的父設定檔，會先於此具名設定檔套用。可設為其他具名設定檔、`:read-only` 或 `:workspace`；不接受 `:danger-full-access`、未定義的父設定檔或循環繼承。",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "由設定檔定義的工作區根目錄，會與工作階段執行時的工作區根目錄一同套用 `:workspace_roots` 檔案系統規則。",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "設為 `true` 時，將路徑納入此設定檔的工作區根目錄集合。停用的項目不會生效。",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "具名檔案系統權限設定檔。每個索引鍵都是絕對路徑或特殊 Token，例如 `:minimal` 或 `:workspace_roots`。",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "在會於沙盒啟動前為相符項目建立快照的平台上，展開拒絕讀取 glob 模式的最大深度。若有設定，值必須至少為 `1`。",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "授予路徑、glob 模式或特殊 Token 所指定目標的直接存取權，或將巢狀項目的範圍限定在該根目錄下。使用 `\"deny\"` 拒絕讀取相符路徑。",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "以每個實際生效的工作區根目錄為基準，限定檔案系統的存取範圍。使用 `\".\"` 表示根目錄本身；`\"**/*.env\"` 等 glob 子路徑可使用 `\"deny\"` 拒絕讀取。",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "啟用此權限設定檔下指令的網路存取。這不會啟動網路代理伺服器。如果未啟用 `features.network_proxy`，也未啟用由管理員管理的網路要求，指令會直接存取網路，且設定檔的網域規則不會強制執行。",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "此權限設定檔啟用沙盒網路時所使用的 HTTP 接聽器 URL。",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "此權限設定檔啟用沙盒網路時，提供 SOCKS5 支援。",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "此權限設定檔使用的 SOCKS5 代理伺服器端點。",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "啟用後，允許透過 SOCKS5 接聽器傳送 UDP。",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "允許沙盒網路串接另一個上游代理伺服器。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允許沙盒網路接聽器繫結至非回送位址。啟用後，可能讓 localhost 以外的位置也能存取接聽器。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允許連線至任意 Unix 通訊端目的地，而不限於預設範圍。僅限在嚴格控管的環境中使用。",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "子程序流量使用的網路代理伺服器模式。",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "適用於沙盒內指令的網域規則。僅當 `features.network_proxy` 或已啟用的管理員網路要求啟動代理伺服器時，才會強制執行。支援精確指定的主機、`*.example.com`、`**.example.com` 和全域 `*` 允許規則；`deny` 優先。不會限制網頁搜尋、應用程式或 MCP 伺服器。",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "允許或拒絕精確指定的主機，或 `*.example.com`、`**.example.com` 等限定範圍的萬用字元模式。",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "沙盒網路的 Unix 通訊端允許清單覆寫設定。以通訊端路徑作為索引鍵；`allow` 會新增路徑，`deny` 則拒絕該路徑。",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "使用 `allow` 將 Unix 通訊端絕對路徑加入實際生效的允許清單，或使用 `deny` 拒絕該路徑。遭拒絕的項目不會納入實際生效的允許清單。",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "允許透過沙盒網路存取更廣泛的本機或私人網路。即使此設定維持 `false`，精確指定本機 IP 常值或 `localhost` 的允許規則，仍可允許存取特定本機目標。",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "將專案或工作樹標記為受信任或不受信任（`\"trusted\"` | `\"untrusted\"`）。不受信任的專案會略過專案範圍的 `.codex/` 層，包括專案本機組態、掛勾和規則。",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "追蹤是否已確認完整存取權警告提示。",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "追蹤是否已確認關於 Windows 目錄對所有使用者開放寫入的警告。",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "追蹤是否已選擇不再顯示因速率限制而切換模型的提醒。",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "追蹤是否已確認 GPT-5.1 遷移提示。",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "追蹤是否已確認 gpt-5.1-codex-max 遷移提示。",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "以 old->new 對應關係追蹤已確認的模型遷移。",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "將 Codex 限制為使用特定身分驗證方式。",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "將 ChatGPT 登入限制於特定工作區識別碼。",
    },
  ]}
  client:load
/>

您可以在[此處](/codex/config-schema.json)找到 `config.toml` 的最新 JSON 結構描述。

若要在 VS Code 或 Cursor 中編輯 `config.toml` 時取得自動完成功能和診斷資訊，您可以安裝 [Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) 擴充功能，並將以下這行新增至 `config.toml` 頂端：

```toml
#:schema https://developers.openai.com/codex/config-schema.json

注意：請將 `experimental_instructions_file` 重新命名為 `model_instructions_file`。Codex 已棄用舊索引鍵；請更新現有組態，改用新名稱。

## `requirements.toml`

`requirements.toml` 是由管理員強制套用的組態檔，用來限制涉及安全性的設定，使用者無法覆寫這些限制。如需詳細資訊、位置和範例，請參閱[管理員強制要求](/zh-Hant/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

對於 ChatGPT Business 和 ChatGPT Enterprise 使用者，Codex 也可以套用從雲端擷取的要求。
如需優先順序的詳細資訊，請參閱安全性頁面。

在 `requirements.toml` 中使用 `[features]`，即可透過與 `config.toml` 相同的標準索引鍵，
固定執行階段功能旗標的值。要求也可以包含文件中記載的 App 專用索引鍵，
這些索引鍵不屬於 `config.toml`。
未列出的索引鍵仍不受限制。

部分受管理的要求會強制套用確切的組態值，而非使用允許清單。
使用者無法覆寫強制設定的路徑、更新偏好設定、登入 Shell 原則、
意見回饋設定或 Windows 私人桌面設定。

受管理的權限設定檔允許清單需要 Codex 0.138.0 或更新版本。
Codex 0.137.0 及更早版本會忽略 `allowed_permission_profiles`
以及受管理的 `default_permissions`。

請搭配使用 `allowed_sandbox_modes` 與 `sandbox_mode`。
若部署使用權限設定檔，請搭配使用 `allowed_permission_profiles`
與受管理的 `default_permissions`。

`[models.new_thread]` 表提供受管理的預設值，並非強制設定。
透過專用 CLI 旗標或 `--config` 覆寫所明確指定的啟動選項，具有較高優先順序。
明確覆寫模型或推理投入程度時，會略過兩個受管理的模型欄位；
`service_tier` 則獨立運作。

瀏覽器要求涵蓋三個獨立的操作介面。
`in_app_browser` 控制使用者自行開啟並直接操作的瀏覽器面板。
`browser_use` 控制智慧體在瀏覽器中執行的工作。
`computer_use` 控制智慧體在原生桌面應用程式中執行的工作。

巢狀的瀏覽器與電腦原則值本身不會授予存取權。
針對特定來源或應用程式設定的 `allow`，可覆寫同一原則來源的備援設定，
但一般的功能、核准及其他原則檢查仍然適用。
若受管理的要求與 `config.toml` 同時適用，
任一方的 `deny` 都具有優先權。

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "強制指定 Codex 儲存以 SQLite 為後端的執行階段狀態所用的目錄。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "強制指定 Codex 寫入本機記錄檔的目錄。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "強制指定 Codex 啟動時使用的 JSON 模型目錄。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "強制設定 Codex 啟動時是否檢查更新。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "強制設定 Shell 工具是否可啟動登入 Shell。",
    },
    {
      key: "feedback",
      type: "table",
      description: "受管理的意見回饋設定。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "強制設定使用者是否可透過各個 Codex 用戶端提交意見回饋。",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "`approval_policy` 的允許值，例如 `untrusted`、`on-request`、`never` 和 `granular`。",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "`approvals_reviewer` 的允許值，例如 `user` 和 `auto_review`。",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "供自動審查使用的受管理 Markdown 原則指示。此設定的優先順序高於本機 `[auto_review].policy`。空白值會被忽略。",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "允許使用的權限設定檔完整清單。設為 `true` 的設定檔可供使用。省略或設為 `false` 的設定檔一律禁止使用，包括未來版本新增的設定檔。合併多個需求來源時，會依設定檔名稱比對項目。",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "允許或禁止使用已載入組態或需求來源中定義的內建或自訂權限設定檔。較後套用且優先順序較高的需求來源，可使用 `false` 停用先前優先順序較低的來源所允許的設定檔。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "管理式預設權限設定檔。此設定檔必須獲得 `allowed_permission_profiles` 允許。請明確設定此值，以確保行為符合預期；若省略，只有在 `:workspace` 和 `:read-only` 都明確獲准時，Codex 才會預設使用 `:workspace`。",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "要求 Codex 服務流量使用支援的資料駐留區域。目前接受 `us`。",
    },
    {
      key: "models",
      type: "table",
      description:
        "新對話串的管理式模型預設值。這些值的優先順序高於使用者和專案的預設值，但為新對話串明確選取的設定可覆寫這些值。",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "啟動新本機對話串時套用的預設值。每項模型設定皆為選填。",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "新對話串的預設模型。明確指定的 `--model` 或用於覆寫模型／推理設定的 `--config` 具有較高優先順序。",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "新對話串的預設推理強度。明確覆寫模型或推理強度時，會略過兩個管理式模型欄位。",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "新對話串的預設服務層級。明確指定的服務層級覆寫值具有較高優先順序，且與模型欄位分開處理。",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "由管理員定義的權限設定檔，以設定檔名稱作為索引鍵。使用與 `config.toml` 相同的設定檔欄位。",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "由管理員定義的權限設定檔。名稱不得以 `:` 開頭、使用保留名稱 `filesystem`，或與已載入組態中的設定檔同名。使用與 `config.toml` 相同的設定檔欄位；完整的設定檔結構描述請參閱權限指南。",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "`sandbox_mode` 的允許值。",
    },
    {
      key: "windows",
      type: "table",
      description: "原生 Windows 沙盒需求。",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "`windows.sandbox` 允許使用的原生 Windows 沙盒實作（`elevated` 和 `unelevated`）。清單不得為空。若兩者皆允許且未選擇模式，Codex 會優先使用 `elevated`。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "強制設定原生 Windows 沙盒是否在私有桌面上啟動其子處理程序。",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "主機專屬的沙盒需求。第一個 `hostname_patterns` 符合解析後主機名稱的項目，會覆寫該需求來源的頂層 `allowed_sandbox_modes`。主機專屬項目目前只能覆寫沙盒模式。",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "不區分大小寫的主機名稱模式。支援以 `*` 代表任意字元序列，以 `?` 代表單一字元。",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "此主機專屬項目相符時，所套用的允許沙盒模式。",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "`web_search` 的允許值（`disabled`、`cached`、`indexed`、`live`）。一律允許 `disabled`；空清單實際上只允許 `disabled`。",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "設為 `true` 時，Codex 會略過使用者、專案、工作階段及外掛程式的掛勾，但仍允許來自 `requirements.toml` 和其他管理式組態層的管理式掛勾。",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "設為 `false` 可為受管理使用者停用應用程式快照。若省略，應用程式快照不受需求限制，其可用性依產品的一般規則而定。",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "設為 `false` 可為受管理使用者停用裝置遠端控制。若省略，裝置遠端控制不受需求限制，其可用性依產品的一般規則而定。",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "設為 `false` 可同時封鎖由智慧體操作的瀏覽器功能，以及用於操作原生應用程式的電腦功能。設為 `true` 或省略此值，都不會啟用這兩項功能；其餘功能、原則及核准檢查仍然適用。",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "在雲端管理的 `requirements.toml` 中設為 `false`，即可停用在工作區內分享本機建置外掛程式的功能。",
    },
    {
      key: "features",
      type: "table",
      description:
        "固定的功能設定值。執行階段功能請使用 `config.toml` 中的標準名稱；此處也支援文件所載的應用程式專用需求鍵。",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "要求文件所載的執行階段或應用程式功能維持啟用或停用狀態。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "將受管理使用者的應用程式整合功能固定為啟用或停用。",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false` 可停用應用程式內更新。若省略此需求，更新預設仍維持啟用。",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false`，可停用由使用者直接開啟及操作的內建瀏覽器窗格。",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false`，可停用由智慧體操作的瀏覽器功能。",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false`，可禁止 Codex 透過 ChatGPT 瀏覽器擴充功能操作支援的瀏覽器，包括現有分頁和已登入的工作階段。",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false`，可停用本機執行階段對 Chrome DevTools Protocol 的完整存取，包括瀏覽器開發人員模式，並防止 ChatGPT 桌面版應用程式啟用對應設定。若省略，其可用性依產品的一般規則而定。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "將受管理使用者的標準 `fast_mode` 功能固定為啟用或停用。",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "將受管理使用者的 Guardian 核准功能固定為啟用或停用。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "將受管理使用者的記憶功能固定為啟用或停用。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "將受管理使用者的多智慧體功能固定為啟用或停用。",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "將受管理使用者的外掛程式功能固定為啟用或停用。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "將受管理使用者的遠端外掛程式目錄固定為啟用或停用。",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "在 `requirements.toml` 中設為 `false`，可停用電腦功能、錄製與重播，以及相關的安裝或啟用流程。",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "將受管理使用者隨附的工作區相依性執行階段固定為啟用或停用。",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "內建瀏覽器窗格的需求。這些設定不會控管由智慧體操作的瀏覽器功能。",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "設為 `false`，可禁止使用者將外部瀏覽器的設定或瀏覽資料匯入內建瀏覽器。設為 `true` 或省略此值時，只要其他產品檢查允許，匯入功能仍可使用。此設定僅能透過管理式需求指定，無法透過 `config.toml` 覆寫。",
    },
    {
      key: "browser_use",
      type: "table",
      description: "由智慧體操作的瀏覽器功能所適用的管理式需求。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "設為 `false`，可禁止瀏覽器功能讀取瀏覽器歷程記錄。設為 `true` 或省略此值時，仍適用一般歷程記錄設定及可用性檢查。",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "設為 `true`，可略過瀏覽器功能的自動審查，改為要求使用者核准。設為 `false` 或省略此值時，只要其他設定允許，自動審查仍可使用。",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "設為 `false`，可禁止瀏覽器功能建立或採用涵蓋所有網站的 `Always allow` 核准，例如允許從任何網站下載。現有已儲存的核准會遭忽略，但不會刪除。設為 `true` 或省略此值，不會建立核准。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "若 `browser_use.origins` 下沒有相符項目定義某項瀏覽器功能設定，就使用此處的備援值。相符的網站來源規則會取代該設定來源中的備援值。接著，Codex 會採用管理式需求與使用者組態中較嚴格的結果。",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "使用 `deny`，可對採用備援值的網站來源封鎖瀏覽器功能。遭拒絕的網站來源也會封鎖該處的上傳、下載、完整瀏覽器偵錯存取及自動審查。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "使用 `deny`，可禁止瀏覽器功能從採用備援值的網站來源下載。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "使用 `deny`，可禁止瀏覽器功能上傳至採用備援值的網站來源。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "使用 `deny`，可對採用備援值的網站來源封鎖完整的 Chrome DevTools Protocol（CDP）存取。`allow` 僅允許繼續進行一般的主動啟用與核准檢查。",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "使用 `deny`，可對採用備援值的網站來源略過自動審查，改為要求使用者核准。使用 `allow` 時，只要其他設定允許，自動審查仍可使用。",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "設為 `false`，可禁止瀏覽器功能針對採用備援值的網站來源儲存或採用 `Always allow` 核准。目前回合或對話串的核准仍可套用。`true` 會在其他條件允許時提供 `Always allow` 選項，但不會建立核准。",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "設定非永久性網站存取核准的有效期間：`turn` 將其限制在目前回合內，`thread` 則讓核准在目前對話串的其餘期間持續有效。`persistent_approval` 另外控制是否提供 `Always allow` 選項。產品預設值為 `thread`。",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "網站來源專屬的瀏覽器功能原則。索引鍵使用 `<scheme>://<host-pattern>[:<port>]` 格式，通訊協定配置為 `http` 或 `https`。可使用完整主機名稱、僅比對子網域的 `*.example.com`，或同時比對根網域及其子網域的 `**.example.com`。其他 `*` 萬用字元可跨越句點，因此 `region*.example.com` 也會符合 `region.api.example.com`；主機部分若為 `*`，則會符合該通訊協定配置下的所有主機。比對時會區分通訊協定配置和非預設連接埠；明確指定的預設連接埠會在正規化時移除。路徑、查詢、內嵌的使用者名稱或密碼，以及含有萬用字元的通訊協定配置或連接埠，均屬無效。請在 TOML 中以引號括住模式，例如 `[browser_use.origins.\"https://**.example.com\"]`。",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "適用於符合此模式的網站來源的原則。若有多個模式相符，Codex 會為每項能力採用最嚴格的值：`deny` 優先於 `allow`、`false` 優先於 `true`，且 `turn` 優先於 `thread`。",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "使用 `deny`，可對相符的網站來源封鎖瀏覽器功能。拒絕存取時，也會封鎖該處的上傳、下載、完整瀏覽器偵錯存取及自動審查。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "使用 `deny`，可禁止瀏覽器功能從相符的網站來源下載。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "使用 `deny`，可禁止瀏覽器功能上傳至相符的網站來源。`allow` 僅允許繼續進行一般核准與原則檢查。",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "使用 `deny`，可對相符的網站來源封鎖完整的 Chrome DevTools Protocol（CDP）存取。`allow` 僅允許繼續進行一般的主動啟用與核准檢查。",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "使用 `deny`，可對相符的網站來源略過自動審查，改為要求使用者核准。使用 `allow` 時，只要其他設定允許，自動審查仍可使用。",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "設為 `false`，可禁止瀏覽器功能針對相符的網站來源儲存或採用 `Always allow` 核准。目前回合或對話串的核准仍可套用。`true` 會在其他條件允許時提供 `Always allow` 選項，但不會建立核准。",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "設定相符網站來源的非永久性網站存取核准有效期間：`turn` 將其限制在目前回合內，`thread` 則讓核准在目前對話串的其餘期間持續有效。`persistent_approval` 另外控制是否提供 `Always allow` 選項。",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "智慧體在原生桌面應用程式中執行工作時適用的管理式需求。管理式應用程式規則與 `config.toml` 中的應用程式規則都會強制執行；每個原則來源都必須允許該應用程式。",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "設為 `false` 可防止使用者在受管理的 macOS 裝置上啟用「鎖定時使用」。這項要求會移除啟用控制項，但不會關閉已啟用的「鎖定時使用」。若省略，則依產品的一般可用性規則處理。",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "設為 `false` 可移除跨工作階段儲存應用程式核准的選項。目前工作階段的核准仍可使用。設為 `true` 或省略此設定，都不代表核准應用程式。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "原生應用程式未符合任何平台專屬規則時，採用的預設存取規則。`deny` 會封鎖存取。`allow` 僅允許繼續進行一般核准流程與政策檢查。產品預設值為 `allow`。",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "「電腦」功能在 macOS 上的應用程式規則。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "將精確的 macOS 套件識別碼對應至 `allow` 或 `deny`。相符的規則會取代同一政策來源中的 `computer_use.default_app_access`。受管理要求或使用者組態只要有任一方拒絕，仍會封鎖存取。",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "使用 `deny` 封鎖完全符合此套件識別碼的應用程式。`allow` 只會覆寫此政策來源的預設值，應用程式仍須獲得其他所有政策來源及一般核准流程的允許。",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "「電腦」功能適用於已封裝和未封裝 Windows 應用程式的規則。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "將已簽署封裝應用程式的精確、已註冊應用程式使用者模型識別碼（AUMID）對應至 `allow` 或 `deny`。相符的規則會取代同一政策來源中的 `computer_use.default_app_access`。",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "使用 `deny` 封鎖完全符合此封裝應用程式識別的應用程式。`allow` 只會覆寫此政策來源的預設值，應用程式仍須獲得其他所有政策來源及一般核准流程的允許。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "適用於已簽署但未封裝之 Windows 執行檔的規則。規則會比對執行檔已驗證的發行者與已簽署的版本資訊，而非其路徑或目前的檔名。相符的拒絕規則優先於相符的允許規則。未簽署的執行檔採用 `computer_use.default_app_access`；若無法明確驗證執行檔的簽署身分，則會封鎖該執行檔。",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "必填的精確發行者名稱，取自執行檔受信任的簽署憑證，並採用 Windows X.500 辨別名稱格式。",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "必填且須完全相符的 `ProductName`，取自執行檔已簽署的版本資訊。",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "選填的 `OriginalFilename`，取自執行檔已簽署的版本資訊。比對時不區分大小寫。如果符合發行者與產品的規則要求此值，但執行檔未提供，「電腦」功能會封鎖該執行檔。",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "必填的存取決策，適用於相符的執行檔。`deny` 會封鎖存取。`allow` 只會覆寫此政策來源的預設值，應用程式仍須獲得其他所有政策來源及一般核准流程的允許。",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "由管理員管理、透過 `requirements.toml` 強制執行的網路要求，適用於沙盒中的本機指令。啟用後，即使未設定 `features.network_proxy`，這些要求也能啟動指令網路 Proxy。瀏覽器工具會另外檢查受管理的網路拒絕規則與排他性允許清單。這些要求不會讓瀏覽器流量經由 Proxy 傳送，也不會控制網頁搜尋、應用程式、MCP 伺服器、原生應用程式流量或 Codex 雲端的網路連線。",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "啟用沙盒網路要求。如果目前的沙盒仍關閉指令的網路連線，此設定不會授予網路存取權。",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "`[experimental_network]` 要求所使用的回送 HTTP 接聽連接埠。",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "`[experimental_network]` 要求所使用的回送 SOCKS5 接聽連接埠。",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "允許沙盒網路串接環境中設定的上游 Proxy。",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "允許 `[experimental_network]` 要求使用非回送接聽位址。啟用後，接聽程式可能會開放給 localhost 以外的來源存取。",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "允許存取任意 Unix 通訊端目的地，而非僅限允許清單中的目的地。僅應在嚴格控管的環境中使用。",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "以對應表形式設定的管理員網域政策，適用於沙盒網路。支援精確主機、僅比對子網域的 `*.example.com`、比對根網域及子網域的 `**.example.com`，以及全域 `*` 允許規則。建議使用限定範圍的規則，因為 `*` 會廣泛開放對公用網路的對外存取。發生衝突時，`deny` 優先。請勿與 `experimental_network.allowed_domains` 或 `experimental_network.denied_domains` 同時使用。",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "受管理的網路 Proxy 啟用時，適用於沙盒指令網路連線的管理員允許規則。這些規則不適用於網頁搜尋、應用程式或 MCP 伺服器。請勿與 `experimental_network.domains` 同時使用。",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "以清單形式設定的管理員拒絕規則，適用於沙盒網路。請勿與 `experimental_network.domains` 同時使用。",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "設為 `true` 時，只要沙盒網路要求處於啟用狀態，就只有管理員管理的允許規則會生效；使用者新增的允許清單項目會被忽略。即使沒有受管理的允許規則，使用者新增的網域允許規則也不會繼續生效。",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "由管理員管理的 Unix 通訊端政策，適用於沙盒網路。",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "允許沙盒網路更廣泛地存取本機／私人網路。即使此設定維持 `false`，精確的本機 IP 常值或 `localhost` 允許規則仍可允許存取特定本機目標。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "由管理員強制執行的受管理生命週期掛勾。必須提供受管理掛勾目錄，並採用與 `config.toml` 內嵌 `[hooks]` 相同的事件結構描述。",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "macOS 和 Linux 上存放受管理掛勾指令碼的目錄。Codex 會先確認目錄路徑為絕對路徑且目錄存在，再載入受管理掛勾。",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Windows 上存放受管理掛勾指令碼的目錄。Codex 會先確認目錄路徑為絕對路徑且目錄存在，再載入受管理掛勾。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "掛勾事件的比對器群組，例如 `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit` 或 `Stop`。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "比對器群組的掛勾處理常式。支援指令掛勾和 MCP 工具掛勾；提示詞掛勾和智慧體掛勾的處理常式則會被剖析，但會略過執行。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "在背景執行指令掛勾，不延遲觸發掛勾的操作。預設為 `false`；`SessionEnd` 一律同步執行。請參閱[在背景執行掛勾](/codex/hooks#run-hooks-in-the-background)。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "每個處理常式的大致 Token 門檻；超過門檻時，會將過大的 `additionalContext` 儲存至磁碟，並向模型顯示較短的預覽。預設為 `2500`；設為 `0` 會直接將完整上下文傳給模型。請參閱[大型掛勾輸出](/codex/hooks#large-hook-output)。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "僅限 Windows 使用的指令掛勾指令覆寫設定。也接受 TOML 別名 `command_windows`。",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "由管理員強制執行的檔案系統讀取拒絕規則。項目可以是路徑或 glob 模式，使用者無法透過本機組態放寬這些限制。",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "可啟用的 MCP 伺服器允許清單。伺服器名稱（`<id>`）和識別資訊都必須相符，才能啟用該 MCP 伺服器。任何已設定但不在允許清單中，或識別資訊不符的 MCP 伺服器，都會被停用。",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "單一 MCP 伺服器的識別規則。請設定 `command`（stdio）或 `url`（可串流 HTTP）其中一項。",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "以完全相符的指令字串允許 MCP stdio 伺服器，或使用比對器表格，要求執行檔完全相符，並依序比對引數。字串形式不會檢查引數、`cwd`、`env` 或 `env_vars`。",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "stdio 伺服器所設定的 `command` 必須與此執行檔完全相符。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "stdio 伺服器所用的引數比對器，按引數順序排列。所設定的引數清單長度必須與比對器清單相同，且每個位置都必須相符。指令比對器不會檢查 `cwd`、`env` 或 `env_vars`。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "此引數位置的比對操作。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "`exact` 或 `prefix` 引數比對器所使用的值。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 引數比對器所使用的規則運算式。此運算式必須有效，且與完整的引數值相符。",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "以完全相符的 URL 字串允許 MCP 可串流 HTTP 伺服器，或使用 `exact`、`prefix` 或 `regex` 值比對器表格。",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "所設定的 MCP 伺服器 URL 的比對操作。",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "`exact` 或 `prefix` URL 比對器所使用的值。",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 比對器所使用的規則運算式。此運算式必須有效，且與完整的 URL 值相符。",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "各外掛程式專用的 MCP 伺服器允許清單，以外掛程式識別碼作為索引鍵。若有此表格，外掛程式隨附的伺服器必須有相符的外掛程式與伺服器項目，否則會被停用。",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "單一外掛程式隨附的 MCP 伺服器允許清單。外掛程式伺服器要求採用與頂層 `mcp_servers` 要求相同的精確識別值與比對器格式。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "單一外掛程式隨附的 MCP 伺服器識別規則。請設定 `command`（stdio）或 `url`（可串流 HTTP）其中一項。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "以完全相符的指令字串允許外掛程式的 stdio MCP 伺服器，或使用比對器表格，要求執行檔完全相符，並依序比對引數。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "外掛程式隨附的 stdio 伺服器所設定的指令，必須與此執行檔完全相符。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "外掛程式隨附的 stdio 伺服器所用的引數比對器，按引數順序排列。所設定的引數清單長度必須與比對器清單相同，且每個位置都必須相符。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "此引數位置的比對操作。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "`exact` 或 `prefix` 引數比對器所使用的值。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 引數比對器所使用的規則運算式。此運算式必須與完整的引數值相符。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "以完全相符的 URL 字串允許外掛程式的可串流 HTTP MCP 伺服器，或使用 `exact`、`prefix` 或 `regex` 值比對器表格。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "外掛程式隨附的 MCP 伺服器 URL 的比對操作。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "`exact` 或 `prefix` URL 比對器所使用的值。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL 比對器所使用的規則運算式。此運算式必須與完整的 URL 值相符。",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "外掛程式市集來源的管理員要求。`restrict_to_allowed_sources` 設為 `true` 時，規則會生效。",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "設為 `true` 時，使用者設定的市集來源必須符合 `allowed_sources`，才能執行新增市集、安裝外掛程式及重新整理已設定的 Git 市集等操作。由 Codex 管理的 OpenAI 市集，只要來源與名稱符合保留值，仍可使用。這項設定不會在執行階段篩選使用者已設定的市集。",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "允許的市集來源，以管理員選定的規則名稱作為索引鍵。名稱不同的規則會跨要求層累加；相同名稱下的欄位則採用一般的分層優先順序。",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "一項允許的來源規則。合併要求後的最終 `source` 值決定 Codex 會解讀哪些同層欄位。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "市集來源的比對器類型。使用 `git` 指定單一程式碼庫、`host_pattern` 以正規表示式比對 Git 主機，或 `local` 指定單一目錄。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "當 `source = \"git\"` 時必填的 Git 程式碼庫 URL。Codex 會先將設定的 URL 和允許的 URL 正規化，再要求程式碼庫完全相符。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "`git` 規則可選填的精確 Git ref。省略時，規則會允許相符程式碼庫中的任何 ref。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "當 `source = \"host_pattern\"` 時必填的正規表示式。Codex 會從 HTTPS、SSH 或 SCP 格式的 Git 來源解析出小寫主機名稱，並以此正規表示式進行比對。使用 `^` 和 `$` 可要求完整主機名稱相符。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "當 `source = \"local\"` 時必填的本機市集目錄。Codex 要求使用絕對路徑，並在正規化後比對路徑。",
    },
    {
      key: "apps",
      type: "table",
      description:
        "以應用程式識別碼為索引鍵的受管理應用程式要求。這些要求可停用應用程式，或限制個別工具的核准行為。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "設為 `false` 可停用應用程式。合併多個要求來源時，停用應用程式的要求仍會維持其限制。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "設定單一應用程式工具的受管理核准模式。",
    },
    {
      key: "rules",
      type: "table",
      description:
        "由管理員強制執行的指令規則，會與 `.rules` 檔案合併。要求中的規則必須具有限制性。",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "強制執行的前綴規則清單。每項規則都必須包含 `pattern` 和 `decision`。",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "以模式 Token 表示的指令前綴。每個 Token 都需設定 `token` 或 `any_of` 其中之一。",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "此位置的單一字面值 Token。",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "此位置允許的替代 Token 清單。",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "必填。要求中的規則只能要求核准或禁止，不能允許。",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "選填的理由，若填寫則不得為空，會顯示於核准提示或拒絕訊息中。",
    },
  ]}
  client:load
/>
