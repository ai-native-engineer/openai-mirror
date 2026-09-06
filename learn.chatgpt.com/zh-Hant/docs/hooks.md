<!-- source: https://learn.chatgpt.com/zh-Hant/docs/hooks -->

掛勾是 Codex 的擴充框架，讓您能在智慧體的執行迴圈中執行指令碼或 MCP 工具，實現以下功能：

- 將對話傳送至自訂記錄／分析引擎
- 掃描團隊的提示詞，防止意外貼上 API 金鑰
- 為對話產生摘要，自動建立持久記憶
- 在一輪對話停止時執行自訂驗證檢查，確保遵循標準
- 在特定目錄中自訂提示詞

請留意以下執行階段行為：

- 來自多個檔案且符合條件的掛勾都會執行。
- 同一事件有多個符合條件的指令掛勾時，這些掛勾會同時啟動，因此其中一個掛勾無法阻止另一個符合條件的掛勾啟動。
- 非受管理的掛勾必須先經過審查並設為受信任，才能執行。

掛勾會在對話的不同時機執行：

| 時機                              | 掛勾                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| 一輪對話期間                     | `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、`SubagentStop`、`Stop` |
| 您中斷進行中的一輪對話時 | `Interrupt`（不會為子代理程式執行）                                                                                   |
| 工作階段或子代理程式啟動時 | `SessionStart`、`SubagentStart`                                                                                           |
| 主執行緒結束時         | `SessionEnd`（不會為子代理程式執行）                                                                                  |

## Codex 尋找掛勾的位置

Codex 會在使用中的組態層所在位置尋找以下任一形式的掛勾：

- `hooks.json`
- `config.toml` 內的內嵌 `[hooks]` 資料表

已安裝的外掛程式也可以透過其
資訊清單或預設的 `hooks/hooks.json` 檔案，提供生命週期組態。請參閱[建置
外掛程式](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks)，瞭解
外掛程式的封裝規則。

實務上，最實用的四個位置如下：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

如果掛勾來源不只一個，Codex 會載入所有符合條件的掛勾。
優先順序較高的組態層不會取代優先順序較低的掛勾。
如果單一組態層同時包含 `hooks.json` 和內嵌 `[hooks]`，Codex 會
將兩者合併，並在啟動時發出警告。建議每個組態層只使用一種表示方式。

Codex 也能找到已啟用外掛程式隨附的掛勾。這些掛勾會與其他來源的掛勾一併載入，並採用與其他非受管理掛勾相同的審查與信任流程。

只有在專案的 `.codex/` 組態層受信任時，才會載入專案內的掛勾。
在不受信任的專案中，Codex 仍會從使用者和系統各自
使用中的組態層載入掛勾。

## 審查並信任掛勾

Codex 會先列出已設定的掛勾，再決定哪些可以執行。非受管理的掛勾必須先由您審查其確切定義並設為受信任，才能執行。Codex 會依據掛勾目前的雜湊值記錄信任狀態，因此新增或變更的掛勾會標示為待審查，並在設為受信任前略過。

在 CLI 中使用 `/hooks`，即可檢查掛勾來源、審查新增或變更的掛勾、
信任掛勾，或停用個別非受管理的掛勾。如果啟動時有掛勾需要審查，
Codex 會輸出警告，提示您開啟 `/hooks`。

來自系統、MDM、雲端或 `requirements.toml` 的受管理掛勾會標示為受管理，
並依政策視為受信任，且無法透過使用者掛勾瀏覽器停用。

對於已在 Codex 外部審查掛勾來源的一次性自動化作業，傳入
`--dangerously-bypass-hook-trust` 即可執行已啟用的掛勾，且該次呼叫
不需要已儲存的掛勾信任狀態。

## 組態結構

掛勾分為三個層級：

- 掛勾事件，例如 `PreToolUse`、`PostToolUse`、`PreCompact`、
`SubagentStart` 或 `Stop`
- 決定該事件何時符合條件的比對器群組
- 比對器群組符合條件時會執行的一或多個掛勾處理常式

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

注意事項：

- `description` 是 `hooks.json` 檔案的選用頂層中繼資料，
  不會影響執行哪些掛勾。
- `timeout` 的單位是秒。
- 若省略 `timeout`，Codex 會將大多數掛勾的逾時時間設為 `600` 秒。
  - `SessionEnd` 和 `Interrupt` 的逾時時間預設為 `1` 秒，最高支援 `3` 秒。
- `statusMessage` 為選用項目。
- `additionalContextLimit` 用來設定指令掛勾可傳送給模型的 `additionalContext` 上限。
  超過上限時，Codex 會將完整文字儲存到磁碟，改為傳送較短的預覽。
  請參閱[大量掛勾輸出](#large-hook-output)。
- `commandWindows` 是僅適用於 Windows 的選用指令覆寫設定。在 TOML 中，請使用
`command_windows` 或 `commandWindows`。
- 將 `async` 設為 `true`，即可[在背景
  執行指令掛勾](#run-hooks-in-the-background)。
- 支援 `command` 和 `mcp_tool` 處理常式。`prompt` 和 `agent`
  處理常式則會經過剖析，但不會執行。
- 指令會以工作階段的 `cwd` 作為工作目錄執行。
- 對於程式碼庫內的掛勾，建議以 git 根目錄為基準解析路徑，而不要使用
  `.codex/hooks/...` 之類的相對路徑。Codex 可能會從子目錄啟動，
  而以 git 根目錄為基準的路徑能讓掛勾位置保持不變。

以下是 `config.toml` 中的等效內嵌 TOML：

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## MCP 工具掛勾

MCP 工具掛勾能讓生命週期事件呼叫已連線的 MCP 伺服器上的工具。它會將結構化引數直接傳送給工具，並採用與指令掛勾相同的信任審查流程和輸出契約。

### 設定 MCP 工具掛勾

Codex 寫入或編輯檔案後，這個掛勾會要求 `scanner` MCP 伺服器
掃描每次修補的內容：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| 欄位           | 意義                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | 必須為 `mcp_tool`。                                              |
| `server`        | 已連線的 MCP 伺服器名稱，必填。                |
| `tool`          | 該伺服器提供的工具名稱，必填。                  |
| `input`         | 包含引數範本的 JSON 物件，選填。預設為 `{}`。    |
| `timeout`       | 實際執行的逾時時間，以秒為單位，選填。預設為 `600`。 |
| `statusMessage` | 掛勾執行時顯示的訊息，選填。                      |

### 根據掛勾事件展開引數

使用 `${field.nested}`，透過點號路徑讀取掛勾事件中的欄位。
若預留位置代表整個值，會保留其 JSON 型別。若預留位置位於較長的字串內，
則會呈現為文字。Codex 會遞迴展開物件和陣列。

若事件包含 `{"tool_input":{"file_path":"src/main.rs","count":3}}`，
以下引數範本：

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

展開後為：

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### 執行與生命週期

- 掛勾使用現有的 MCP 連線，不會啟動伺服器或重新連線至伺服器。
- 當工具回傳阻擋決策時，掛勾可以阻擋操作。
發生錯誤、找不到伺服器或工具無法使用，都不會阻擋操作。
- MCP 工具掛勾會同步執行，不會要求工具核准，也不會觸發
其他掛勾。
- 掛勾與伺服器的逾時設定以較短者為準。等待 MCP
資訊請求回應的時間不計入逾時。
- `SessionStart` 掛勾可能會在 MCP 伺服器就緒前執行。若發生這種情況，
  掛勾不會阻擋工作階段。
- `SessionEnd` 不支援 MCP 工具掛勾。

## 停用掛勾

掛勾預設為啟用。若要停用，請在 `config.toml` 中設定：

```toml
[features]
hooks = false

請使用 `hooks` 作為標準功能設定鍵。`codex_hooks` 是
已棄用的別名，但仍可使用。管理員也可以用同樣的方式，
在 `requirements.toml` 中設定 `[features].hooks = false`，強制停用掛勾。

## 來自 `requirements.toml` 的受管理掛勾

企業管理的需求設定也能在 `[hooks]` 下內嵌定義掛勾。
如果管理員希望強制套用掛勾組態，並透過 MDM 或其他裝置管理系統
派送實際的指令碼，便可使用此方式。
若要讓已在本機停用掛勾的使用者也必須執行受管理掛勾，
請在 `requirements.toml` 中定義 `[hooks]`，並強制設定 `[features].hooks = true`。若要忽略
使用者、專案、工作階段和外掛程式的掛勾，同時仍允許
管理員管理的掛勾，請設定 `allow_managed_hooks_only = true`。

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

受管理掛勾的注意事項：

- macOS 和 Linux 使用 `managed_dir`。
- Windows 使用 `windows_managed_dir`。
- Codex 不會派送 `managed_dir` 中的指令碼；
  必須由您的企業工具另行安裝及更新。
- 受管理掛勾的指令應使用指令碼的絕對路徑，且指令碼應位於
組態指定的受管理目錄內。
- `allow_managed_hooks_only = true` 會略過來自使用者、專案、工作階段和
  外掛程式的掛勾，但仍會載入來自 `requirements.toml` 和
  其他受管理組態層的受管理掛勾。

## 外掛程式隨附的掛勾

啟用外掛程式後，Codex 可以載入該外掛程式的生命週期掛勾，
並一併載入使用者、專案和受管理的掛勾。

預設情況下，Codex 會在外掛程式根目錄中尋找 `hooks/hooks.json`。
外掛程式資訊清單可以透過 `.codex-plugin/plugin.json` 中的 `hooks` 項目
覆寫這個預設值。資訊清單項目可以是以 `./` 開頭的路徑、
由以 `./` 開頭的路徑組成的陣列、內嵌掛勾物件，
或內嵌掛勾物件陣列。

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

資訊清單中的掛勾路徑以外掛程式根目錄為基準解析，且必須位於
該根目錄內。如果資訊清單定義了 `hooks`，Codex 就會使用
這些資訊清單項目，而不是預設的 `hooks/hooks.json`。

外掛程式掛勾指令會接收以下環境變數：

- `PLUGIN_ROOT` 是 Codex 專屬的擴充環境變數，指向已安裝外掛程式的
  根目錄。
- `PLUGIN_DATA` 是 Codex 專屬的擴充環境變數，指向外掛程式的
  可寫入資料目錄。
- Codex 也會設定 `CLAUDE_PLUGIN_ROOT` 和 `CLAUDE_PLUGIN_DATA`，
  以便與現有的外掛程式掛勾相容。

外掛程式掛勾使用與其他掛勾相同的事件結構描述。安裝或啟用
外掛程式並不會自動信任其中的掛勾；Codex 會略過外掛程式隨附的掛勾，
直到您審查並信任目前的掛勾定義為止。

## 比對模式

`matcher` 欄位是用於篩選掛勾觸發時機的正規表示式字串。使用 `"*"`、
`""`，或完全省略 `matcher`，即可讓受支援的事件
每次發生時都符合比對。

目前只有部分 Codex 事件會套用 `matcher`：

| 事件               | `matcher` 的篩選對象 | 備註                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | 工具名稱              | 支援範圍包括 `Bash`、`apply_patch`\* 和 MCP 工具名稱 |
| `PostToolUse`       | 工具名稱              | 請參閱[工具涵蓋範圍](#tool-coverage)                          |
| `PostCompact`       | 壓縮觸發方式     | 可用值為 `manual` 或 `auto`                                |
| `PreCompact`        | 壓縮觸發方式     | 可用值為 `manual` 或 `auto`                                |
| `PreToolUse`        | 工具名稱              | 請參閱[工具涵蓋範圍](#tool-coverage)                          |
| `SessionEnd`        | 結束原因             | 目前只有 `other`                                       |
| `SessionStart`      | 啟動來源           | 可用值為 `startup`、`resume`、`clear` 和 `compact`       |
| `SubagentStart`     | 子代理程式類型          | 值取決於啟動的子代理程式                    |
| `SubagentStop`      | 子代理程式類型          | 值取決於停止的子代理程式                     |
| `UserPromptSubmit`  | 不支援          | 此事件會忽略任何已設定的 `matcher`           |
| `Stop`              | 不支援          | 此事件會忽略任何已設定的 `matcher`           |
| `Interrupt`         | 不支援          | 此事件會忽略任何已設定的 `matcher`           |

\*對於 `apply_patch`，`matcher` 的值也可以使用 `Edit` 或 `Write`。

範例：

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### 工具涵蓋範圍

`PreToolUse` 和 `PostToolUse` 可觀察的呼叫不限於 Shell 和 MCP。大多數
本機函式工具使用相同的掛勾路徑，因此您可以比對工具名稱、
檢查其 JSON 引數，並透過 `PreToolUse` 封鎖或改寫呼叫。

| 工具路徑                         | `PreToolUse` | `PostToolUse` | 備註                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Shell 指令                    | 是          | 是           | 以 `Bash` 比對。                                                                                                         |
| 統一執行（`exec_command`）     | 是          | 是           | 以 `Bash` 比對。後續的 `write_stdin` 輪詢可在原始指令完成時傳遞該指令的 `PostToolUse`。 |
| `apply_patch`                     | 是          | 是           | 以 `apply_patch`、`Edit` 或 `Write` 比對。                                                                              |
| MCP 工具                         | 是          | 是           | 比對 MCP 工具名稱，例如 `mcp__filesystem__read_file`。                                                           |
| 其他本機函式工具        | 是          | 是           | 比對函式工具名稱，例如 `update_plan`。`spawn_agent` 也可用 `Agent` 比對。                                 |
| 託管工具，例如 `WebSearch` | 否           | 否            | 這些工具不使用本機函式工具的掛勾路徑。                                                                       |

`write_stdin` 用於既有統一執行工作階段的資料傳輸。
對於已通過 `PreToolUse` 的指令，它在傳送輸入或輪詢時，
不會再次執行 `PreToolUse`。

某些特殊用途的工具路徑可以選擇不使用預設掛勾路徑。請將工具掛勾
視為實用的防護機制，而非完整的強制控管邊界。

## 共用輸入欄位

每個指令掛勾都會透過 `stdin` 接收一個 JSON 物件。

以下是常用的共用欄位：

| 欄位             | 類型             | 說明                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | 目前的 Codex 工作階段 ID。子代理程式掛勾會使用父工作階段 ID。 |
| `transcript_path` | `string \| null` | 工作階段對話記錄檔的路徑（如有）                         |
| `cwd`             | `string`         | 工作階段的工作目錄                                   |
| `hook_event_name` | `string`         | 目前的掛勾事件名稱                                             |
| `model`           | `string`         | Codex 專用擴充欄位。目前使用中的模型 Slug                         |

以回合為範圍的掛勾會在各自的事件專屬表格中，
將 `turn_id` 列為 Codex 專用擴充欄位。

`SessionStart`、`PreToolUse`、`PermissionRequest`、`PostToolUse`、
`UserPromptSubmit`、`SubagentStart`、`SubagentStop`、`Stop` 和 `Interrupt` 也包含
`permission_mode`，用來表示目前的權限模式，值為 `default`、
`acceptEdits`、`plan`、`dontAsk` 或 `bypassPermissions`。

`transcript_path` 提供對話記錄的路徑，方便使用；不過，
對話記錄格式並不是供掛勾使用的穩定介面，日後可能變更。

若需要完整的傳輸格式，請參閱[結構描述](#schemas)。

## 共用輸出欄位

`SessionStart`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、
`SubagentStop` 和 `Stop` 支援這些共用 JSON 欄位。`SubagentStart`
接受以相同格式提供的 `systemMessage` 和掛勾專屬上下文，但
`continue: false` 不會停止子代理程式：

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| 欄位            | 效果                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | 若為 `false`，會將該次掛勾執行標示為已停止      |
| `stopReason`     | 記錄為停止原因             |
| `systemMessage`  | 在 UI 或事件串流中顯示為警告 |
| `suppressOutput` | 目前會剖析，但尚未實作            |

若結束代碼為 `0` 且沒有輸出，則視為成功，Codex 會繼續執行。

`PreToolUse` 和 `PermissionRequest` 支援 `systemMessage`，但這些事件目前不支援 `continue`、
`stopReason` 和 `suppressOutput`。
若 `PreToolUse` 掛勾傳回其中一個不支援的欄位，Codex 會將
該次掛勾執行標示為失敗、回報錯誤，然後繼續工具呼叫。

`PostToolUse` 支援 `systemMessage`、`continue: false` 和 `stopReason`。
`suppressOutput` 會被剖析，但該事件目前不支援此欄位。

### 大量掛勾輸出

預設情況下，Codex 會將每則提供給模型的掛勾輸出訊息限制在約
2,500 個 Token。若掛勾傳回的內容超過此限制，Codex 會將完整文字儲存在
`<temp_dir>/hook_outputs/<session_id>/<uuid>.txt`，並向模型提供
包含開頭與結尾內容、附有儲存檔案路徑的預覽。這種行為稱為
**溢寫**：Codex 會將過大的輸出儲存至磁碟，並以
較短的預覽取代，供模型讀取。若無法寫入檔案，模型仍會
收到截斷的預覽。

  請保持掛勾與外掛程式的上下文精簡。多個掛勾與外掛程式提供的上下文
  會累積，可能降低模型表現。提高 `additionalContextLimit`
  會增加這項風險。請避免將上限設為 `0`，除非掛勾會
  嚴格限制輸出量；否則，單一掛勾可能耗用
  整個上下文視窗。

對於任何會傳回 `additionalContext` 的指令掛勾，
請在處理常式中設定 `additionalContextLimit`，
以自訂大致的 Token 數門檻：

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

若省略 `additionalContextLimit`，門檻會使用預設值 `2500` 個 Token。您可以
使用正整數設定其他門檻，或設為 `0`，將處理常式的
完整額外上下文直接傳給模型。Codex 會獨立評估
每個相符的處理常式。對於無法產生額外上下文的事件，
Codex 會忽略 `additionalContextLimit`，
並回報組態警告。

這項設定僅適用於 `additionalContext`。工具回饋和接續提示詞
仍使用預設限制。

由於過大的輸出可能寫入磁碟，請避免在掛勾輸出中傳回機密資訊或
其他敏感資料。

## 在背景執行掛勾

預設情況下，Codex 會等待指令掛勾完成，才繼續執行
觸發該掛勾的操作。將 `async` 設為 `true`，即可讓指令掛勾在
背景執行，同時讓 Codex 繼續運作。

### 設定背景掛勾

在 `hooks.json` 的指令處理常式中加入 `"async": true`：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

若是在 `config.toml` 中定義的行內掛勾，請設定 `async = true`：

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

背景掛勾與同步指令掛勾使用相同的輸入、比對器、信任審查、逾時設定及
[大量輸出處理機制](#large-hook-output)。與其他指令掛勾相同，
`timeout` 以秒為單位，預設為
`600`。`Interrupt` 掛勾的預設逾時為一秒，上限為三秒，
即使在背景執行也一樣。

### 背景掛勾的執行方式

背景掛勾完成後，Codex 會在對話中下一個安全時機
傳遞受支援的資訊性輸出：

- 若有回合正在進行，Codex 會等待目前的模型請求和工具呼叫
完成，再將輸出提供給該回合的
下一次模型請求。
- 若沒有回合正在進行，Codex 會等到下一個使用者回合。
背景掛勾完成時不會啟動新回合。

請使用與同步掛勾相同的事件專用 JSON 輸出。Codex 會將
`additionalContext` 加入模型的上下文，並將 `systemMessage`
顯示為警告。

  背景掛勾無法阻擋、核准、改寫觸發它們的操作，也無法以其他方式控制該操作。
若要套用工具政策、做出權限決策、拒絕提示詞或續接回合，
請使用同步掛勾。

### 限制

- Codex 在每個工作階段中最多同時執行八個背景掛勾。
其餘掛勾會等待執行中的掛勾完成後再執行。
- 每次相符的叫用都會獨立執行，背景掛勾的完成順序
可能與啟動順序不同。
- 工作階段結束時，Codex 會取消尚未完成的背景掛勾，
並捨棄尚未傳遞的輸出。
- `SessionEnd` 掛勾一律同步執行。

## 掛勾

### SessionStart

在此事件中，`matcher` 會套用至 `source`。

除了 [通用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位    | 型別     | 說明                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | 工作階段的啟動方式：`startup`、`resume`、`clear` 或 `compact` |

輸出至 `stdout` 的純文字會作為額外的開發者上下文加入。

輸出至 `stdout` 的 JSON 支援 [通用輸出欄位](#common-output-fields) 以及以下
掛勾專用結構：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

該 `additionalContext` 文字會作為額外的開發者上下文加入。

Codex 壓縮根工作階段後，`SessionStart` 掛勾若符合
`source: "compact"`，便會在下一次模型請求前執行。這也適用於
回合進行期間發生自動壓縮的情況：Codex 會將掛勾的
額外上下文傳遞給緊接著的續接流程，而不會等到
後續的使用者回合。若掛勾傳回 `continue: false`，Codex 會結束該回合，
不再傳送模型請求。

### SessionEnd

`SessionEnd` 可讓您在工作階段結束時執行指令，例如儲存最後的備註
或清理檔案。它會在以下情況為主執行緒執行：您封存或
刪除仍開啟的對話、Codex 正常關閉，或對話持續閒置
且未在任何已連線的用戶端中開啟達 30 分鐘。
它不會為子代理程式執行。

切換離開對話或呼叫 `thread/unsubscribe` 不會立即結束
工作階段，因此不會立刻執行 `SessionEnd`。掛勾在執行期間
仍可讀取工作階段文字記錄。

`matcher` 會針對此事件篩選 `reason`。目前，`reason` 一律為 `other`。
您可以省略 `matcher`，或使用 `other`，以便在每個 `SessionEnd` 事件發生時執行。

除了 [通用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位    | 型別     | 說明                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | 工作階段結束的原因：`other` |

例如，`SessionEnd` 指令會收到：

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

`SessionEnd` 掛勾一律同步執行，即使 `async` 為 `true` 也一樣。
其輸出僅供參考，不會引導 Codex 的行為，也不會讓執行緒保持開啟。
若指令逾時或因錯誤而結束，Codex 會將其回報為掛勾執行失敗。

### SubagentStart

在此事件中，`matcher` 會套用至 `agent_type`。

除了 [通用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位             | 型別     | 說明                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Codex 專用擴充欄位。目前進行中的 Codex 回合 ID |
| `agent_id`        | `string` | 子代理程式的識別碼                    |
| `agent_type`      | `string` | 子代理程式類型或設定檔                       |
| `permission_mode` | `string` | 目前的權限模式                        |

輸出至 `stdout` 的純文字會作為額外的開發者上下文提供給子代理程式。

輸出至 `stdout` 的 JSON 支援 `systemMessage` 以及以下掛勾專用結構：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

該 `additionalContext` 文字會作為額外的開發者上下文提供給
子代理程式。為了維持相容性，系統會剖析 `continue: false`，但不會因此阻止
子代理程式啟動。

### PreToolUse

`PreToolUse` 可攔截 Bash、透過 `apply_patch` 進行的檔案編輯、
MCP 工具呼叫，以及其他本機函式工具。如需瞭解支援的路徑和例外情況，請參閱 [工具
涵蓋範圍](#tool-coverage)。

`matcher` 會套用至 `tool_name` 和比對器別名。透過
`apply_patch` 編輯檔案時，`matcher` 的值可使用 `apply_patch`、`Edit` 或 `Write`；掛勾輸入
仍會回報 `tool_name: "apply_patch"`。

除了 [通用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位         | 型別         | 說明                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Codex 專用擴充欄位。目前進行中的 Codex 回合 ID                                                                                   |
| `tool_name`   | `string`     | 掛勾使用的標準工具名稱，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 之類的 MCP 名稱                                     |
| `tool_use_id` | `string`     | 本次叫用的工具呼叫 ID                                                                                                 |
| `tool_input`  | `JSON value` | 工具專用輸入。`Bash` 和 `apply_patch` 使用 `tool_input.command`。MCP 及其他本機函式工具會傳送其引數。 |

輸出至 `stdout` 的純文字會被忽略。

輸出至 `stdout` 的 JSON 可使用 `systemMessage`。若要拒絕支援的工具呼叫，請傳回
以下掛勾專用結構：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex 也接受以下舊版封鎖結構：

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

你也可以使用結束代碼 `2`，並將封鎖原因寫入 `stderr`。

若要加入模型可見的上下文而不封鎖呼叫，請傳回
`hookSpecificOutput.additionalContext`：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

若要改寫支援的工具呼叫而不封鎖，請傳回
`permissionDecision: "allow"`，並包含 `updatedInput`：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

對於 Bash 指令和 `apply_patch`，`updatedInput` 必須包含字串型別的
`command` 欄位。對於 MCP 和其他本機函式工具，`updatedInput` 是
用來取代原有引數的物件。傳回 `updatedInput` 時，必須同時包含
`permissionDecision: "allow"`；其他 `updatedInput` 結構都會
被回報為錯誤。

`permissionDecision: "ask"`、舊版 `decision: "approve"`、`continue: false`、
`stopReason` 和 `suppressOutput` 會被解析，但目前尚未支援。
Codex 會將該次掛勾執行標記為失敗、回報錯誤，並繼續執行工具呼叫。

### PermissionRequest

當 Codex 即將要求核准時，`PermissionRequest` 就會執行，例如
要求提升 shell 權限或要求受管理網路核准時。它可以允許或拒絕請求，
也可以不作決定，讓正常的核准提示流程繼續。
不需要核准的指令不會觸發此掛勾。

`matcher` 會套用至 `tool_name` 及比對別名。目前的標準值
包括 `Bash`、`apply_patch`，以及 MCP 工具名稱，例如
`mcp__server__tool`；`apply_patch` 也會比對 `Edit` 和 `Write`。

除了[共通輸入欄位](#common-input-fields)，還有以下欄位：

| 欄位                    | 型別             | 說明                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID                                                                 |
| `tool_name`              | `string`         | 掛勾工具的標準名稱，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 這類 MCP 名稱                   |
| `tool_input`             | `JSON value`     | 工具專屬的輸入。`Bash` 和 `apply_patch` 使用 `tool_input.command`，MCP 工具則會傳送所有引數。 |
| `tool_input.description` | `string \| null` | 供人閱讀的核准原因（若 Codex 有提供）                                                             |

輸出至 `stdout` 的純文字會被忽略。

部分工具輸入可能包含供人閱讀的說明，但不要假設
每個工具都有 `tool_input.description` 欄位。

若要核准請求，請傳回：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

若要拒絕請求，請傳回：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

若多個相符的掛勾傳回決策，只要有 `deny`，就以該決策為準。否則，
`allow` 會讓請求繼續執行，而不顯示核准提示。若沒有
任何相符的掛勾作出決策，Codex 就會使用正常的核准流程。

請勿傳回 `updatedInput`、`updatedPermissions` 或 `interrupt` 來回應
`PermissionRequest`；這些欄位保留供未來功能使用，
目前傳回它們會導致請求遭到拒絕。

### PostToolUse

`PostToolUse` 會在支援的工具產生輸出後執行，包括 Bash、
`apply_patch`、MCP 工具呼叫和其他本機函式工具。對 Bash 而言，
即使指令以非零狀態結束，掛勾仍會執行。它無法復原
已執行工具造成的副作用。支援的路徑及例外情況，
請參閱[工具涵蓋範圍](#tool-coverage)。

`matcher` 會套用至 `tool_name` 及比對別名。透過
`apply_patch` 編輯檔案時，`matcher` 的值可以使用 `apply_patch`、`Edit` 或 `Write`；
掛勾輸入仍會回報 `tool_name: "apply_patch"`。

除了[共通輸入欄位](#common-input-fields)，還有以下欄位：

| 欄位           | 型別         | 說明                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID                                                                                   |
| `tool_name`     | `string`     | 掛勾工具的標準名稱，例如 `Bash`、`apply_patch`，或 `mcp__fs__read` 這類 MCP 名稱                                     |
| `tool_use_id`   | `string`     | 本次工具呼叫的 ID                                                                                                 |
| `tool_input`    | `JSON value` | 工具專屬的輸入。`Bash` 和 `apply_patch` 使用 `tool_input.command`。MCP 和其他本機函式工具會傳送其引數。 |
| `tool_response` | `JSON value` | 工具專屬的輸出。MCP 工具會傳送 MCP 呼叫結果。其他本機函式工具通常會傳送提供給模型的輸出。    |

輸出至 `stdout` 的純文字會被忽略。

輸出至 `stdout` 的 JSON 可使用 `systemMessage`，以及以下掛勾專用結構：

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

其中的 `additionalContext` 文字會作為額外的開發人員上下文加入。

對於此事件，`decision: "block"` 不會復原已完成的 Bash 指令。
Codex 會改為記錄回饋，以該回饋取代工具結果，
並讓模型從掛勾提供的訊息繼續執行。

你也可以使用結束代碼 `2`，並將回饋原因寫入 `stderr`。

若要在指令執行後停止對原始工具結果的正常處理，
請傳回 `continue: false`。Codex 會以你提供的回饋或停止訊息
取代工具結果，然後從該處繼續。

`updatedMCPToolOutput` 和 `suppressOutput` 會被解析，但目前尚未支援。
Codex 會將該次掛勾執行標記為失敗、回報錯誤，並繼續
正常處理工具結果。

#### 程式碼模式中的工具呼叫

當模型使用程式碼模式從 JavaScript 呼叫工具時，掛勾決策會套用
至該巢狀呼叫。`PreToolUse` 可以在工具執行前阻止其執行，或改寫
其輸入。即使 `PostToolUse` 封鎖了呼叫，也無法復原工具的副作用，
但可以阻止原始結果傳入執行中的指令碼。

| 掛勾結果                                                      | 程式碼模式看到的內容                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` 封鎖工具呼叫                                              | 工具呼叫的 Promise 會在工具執行前遭到拒絕。                                                         |
| `PreToolUse` 傳回 `updatedInput`                              | 工具會使用改寫後的輸入執行，Promise 則會以該結果成功完成。                      |
| `PostToolUse` 傳回 `decision: "block"`，或以結束代碼 `2` 結束 | 工具會先執行，接著 Promise 會遭到拒絕，並帶有掛勾提供的原因。                                          |
| `PostToolUse` 傳回 `continue: false`                          | Codex 會以掛勾回饋作為模型可見的結果，但不會拒絕巢狀工具呼叫的 Promise。 |

### PreCompact

`PreCompact` 會在 Codex 壓縮對話前執行。`matcher` 會套用
至 `trigger`，後者的值為 `manual` 或 `auto`。

除了[共通輸入欄位](#common-input-fields)，還有以下欄位：

| 欄位     | 型別     | 說明                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID |
| `trigger` | `string` | 壓縮的觸發方式：`manual` 或 `auto`  |

輸出至 `stdout` 的純文字會被忽略。

輸出至 `stdout` 的 JSON 支援 [共用輸出欄位](#common-output-fields)。如果
相符的 `PreCompact` 掛勾傳回 `continue: false`，Codex 會在
開始壓縮前停止。

### PostCompact

`PostCompact` 會在 Codex 壓縮對話後執行。`matcher` 會套用至
`trigger`，其值為 `manual` 或 `auto`。

除了 [共用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位     | 類型     | 說明                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID |
| `trigger` | `string` | 觸發壓縮的方式：`manual` 或 `auto`  |

輸出至 `stdout` 的純文字會被忽略。

輸出至 `stdout` 的 JSON 支援 [共用輸出欄位](#common-output-fields)。如果
相符的 `PostCompact` 掛勾傳回 `continue: false`，Codex 會在
壓縮完成後停止。

### UserPromptSubmit

此事件目前不使用 `matcher`。

除了 [共用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位     | 類型     | 說明                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID |
| `prompt`  | `string` | 即將送出的使用者提示詞            |

輸出至 `stdout` 的純文字會作為額外的開發者上下文加入。

輸出至 `stdout` 的 JSON 支援 [共用輸出欄位](#common-output-fields)，以及
以下掛勾專用格式：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

`additionalContext` 中的文字會作為額外的開發者上下文加入。

若要阻擋提示詞，請傳回：

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

也可以使用結束代碼 `2`，並將阻擋原因寫入 `stderr`。

### SubagentStop

在此事件中，`matcher` 會套用至 `agent_type`。

除了 [共用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位                    | 類型             | 說明                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID  |
| `agent_id`               | `string`         | 子代理程式的識別碼                     |
| `agent_type`             | `string`         | 子代理程式的類型或設定檔                        |
| `agent_transcript_path`  | `string \| null` | 子代理程式對話紀錄檔案的路徑（若有）    |
| `stop_hook_active`       | `boolean`        | 此子代理程式是否已接續執行     |
| `last_assistant_message` | `string \| null` | 子代理程式最新的助理訊息（若有） |

`SubagentStop` 以結束代碼 `0` 結束時，需在 `stdout` 輸出 JSON。
此事件不接受純文字輸出。

輸出至 `stdout` 的 JSON 支援 [共用輸出欄位](#common-output-fields)。若要要求
Codex 繼續執行子代理程式流程，請傳回：

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

也可以使用結束代碼 `2`，並將接續執行的原因寫入 `stderr`。

如果任何相符的 `SubagentStop` 掛勾傳回 `continue: false`，
該結果會優先於其他相符的 `SubagentStop` 掛勾
所做的接續執行決定。

### Stop

此事件目前不使用 `matcher`。

除了 [共用輸入欄位](#common-input-fields)，另有以下欄位：

| 欄位                    | 類型             | 說明                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Codex 專用擴充欄位。目前作用中的 Codex 回合 ID    |
| `stop_hook_active`       | `boolean`        | 此回合是否已透過 `Stop` 接續執行 |
| `last_assistant_message` | `string \| null` | 最新的助理訊息文字（若有）       |

`Stop` 以結束代碼 `0` 結束時，需在 `stdout` 輸出 JSON。
此事件不接受純文字輸出。

輸出至 `stdout` 的 JSON 支援 [共用輸出欄位](#common-output-fields)。若要讓
Codex 繼續執行，請傳回：

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

也可以使用結束代碼 `2`，並將接續執行的原因寫入 `stderr`。

在此事件中，`decision: "block"` 不會拒絕該回合，而是會指示
Codex 繼續執行，並自動建立新的接續提示詞，
作為新的使用者提示詞，以你提供的 `reason` 作為提示詞文字。

如果任何相符的 `Stop` 掛勾傳回 `continue: false`，該結果會優先於
其他相符的 `Stop` 掛勾所做的接續執行決定。

### Interrupt

當你中斷主執行緒上正在進行的回合時，`Interrupt` 就會執行。你可以用它
記錄中斷事件，或清理掛勾啟動的工作。它不會針對
閒置的執行緒或子代理程式執行，且會忽略任何已設定的 `matcher`。

除了 [共用輸入欄位](#common-input-fields)，此事件還包含
`turn_id`（遭中斷回合的 ID）以及 `permission_mode`。

指令掛勾的預設逾時時間為一秒。可設定的逾時時間
限於一至三秒。掛勾輸出無法阻止
中斷或重新啟動回合。請以結束代碼 `0` 結束且不產生任何輸出，或傳回 JSON，
並視需要加入 `systemMessage` 以顯示警告。
此事件不接受純文字輸出。

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## 結構描述

  連結中的 `main` 分支結構描述可能包含目前版本
  尚未提供的掛勾欄位。目前版本的行為請以本頁為準。

若需要目前確切的傳輸格式，請參閱
[Codex GitHub 程式碼庫](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated)中產生的結構描述。
