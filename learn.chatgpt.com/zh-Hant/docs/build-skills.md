<!-- source: https://learn.chatgpt.com/zh-Hant/docs/build-skills -->

透過智慧體技能，為 ChatGPT 與 Codex 擴充特定任務所需的能力。
技能會封裝指示、資源和選用的指令碼，讓這兩項產品
都能可靠地遵循工作流程。技能建構於
[開放式智慧體技能標準](https://agentskills.io)。

技能是建立可重複使用工作流程的編寫格式。外掛程式可透過
ChatGPT 與 Codex 共用的通用外掛程式目錄，發佈
可重複使用的技能與連接器。外掛程式可用於網頁版、
桌面版和行動版 ChatGPT 中的對話與 Work，也可用於 ChatGPT 桌面版應用程式
中的 Codex，以及 Codex CLI。先使用技能設計工作流程，再將其封裝為
[外掛程式](https://developers.openai.com/plugins/build/plugins)，即可讓
其他人安裝。

獨立技能可在 ChatGPT 桌面版應用程式、Codex CLI
和 IDE 擴充功能中使用。外掛程式內附的技能也可用於
網頁版、桌面版和行動版 ChatGPT 中的對話與 Work。

在 ChatGPT 桌面版應用程式中，開啟側邊欄的 **技能** ，即可檢視和探索
你在各個專案中建立的技能。

  
    
  

技能採用 **漸進式揭露** ，有效管理上下文。ChatGPT 與
Codex 一開始只會取得每項技能的名稱和說明，待決定使用該技能時，才會載入完整的
`SKILL.md` 指示。

在 Codex 中，初始清單也會包含每項技能的檔案路徑。為避免
排擠提示詞的其他內容，這份清單最多只會使用模型上下文視窗的 2%；
若上下文視窗大小不明，則上限為 8,000 個字元。如果安裝了許多技能，
Codex 會先縮短技能說明。如果技能數量龐大，Codex 可能會從
初始清單中省略部分技能，並顯示警告。

這項預算僅適用於初始技能清單。Codex 選取某項技能後，仍會讀取該技能完整的 SKILL.md 指示。

技能是一個包含 `SKILL.md` 檔案的目錄，也可視需要納入指令碼和參考資料。`SKILL.md` 檔案必須包含 `name` 和 `description`。

<a id="how-codex-uses-skills"></a>

## ChatGPT 與 Codex 如何使用技能

ChatGPT 與 Codex 可透過兩種方式啟用技能：

1. **明確叫用：** 在提示詞中直接加入技能。在
   ChatGPT 中，輸入 `@` 以選取技能。在 Codex CLI 或 IDE 擴充功能中，執行
`/skills` 或輸入 `$`，以提及技能。
2. **隱含叫用：** 當你的任務
   符合技能的 `description` 時，ChatGPT 或 Codex 可以選擇該技能。

由於隱含比對取決於 `description`，請撰寫簡潔的說明，
清楚界定適用範圍與界線。將主要使用案例和觸發詞放在開頭，
即使說明被縮短，主機仍能比對到該技能。

## 建立技能

如果你已熟悉工作流程，而且示範比描述更容易，請使用
[錄製與重播](/zh-Hant/codex/extend/record-and-replay)。錄製工具會擷取
工作流程、檢查各個步驟，並根據
示範內容草擬可重複使用的技能。

如果你想改用文字描述技能，請使用內建的建立工具。
在 ChatGPT Work 中，使用 `@skill-creator` 叫用。在 Codex 中，叫用方式如下：

```text
$skill-creator

建立工具會詢問技能的用途、應在何時觸發，以及是否只包含指示或同時包含指令碼。預設為只包含指示。

你也可以手動建立一個包含 `SKILL.md` 檔案的資料夾，藉此建立技能：

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex 會自動偵測技能變更。如果未出現更新，請重新啟動 Codex。

<a id="where-to-save-skills"></a>

## Codex 載入本機技能的位置

Codex 會從程式碼庫、使用者、管理員和系統位置讀取技能。對於程式碼庫，Codex 會掃描從目前工作目錄到程式碼庫根目錄之間每個目錄中的 `.agents/skills`。如果兩項技能的 `name` 相同，Codex 不會將其合併；兩者都可能出現在技能選擇器中。

| 技能範圍 | 位置                                                                                                  | 建議用途                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> 目前的工作目錄：啟動 Codex 的位置。                           | 如果你位於程式碼庫或程式碼環境中，團隊可提交與工作資料夾相關的技能。例如，只適用於特定微服務或模組的技能。                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> 在 Git 程式碼庫內啟動 Codex 時，CWD 上層的資料夾。         | 如果程式碼庫含有巢狀資料夾，組織可在上層資料夾中提交適用於共用區域的技能。                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> 在 Git 程式碼庫內啟動 Codex 時，最上層的根資料夾。 | 如果程式碼庫含有巢狀資料夾，組織可提交適用於所有程式碼庫使用者的技能。這些技能會作為根層級技能，供程式碼庫中的任何子資料夾使用。 |
| `USER`      | `$HOME/.agents/skills` <br /> 提交至使用者個人資料夾的任何技能。                         | 用於整理與使用者相關，且適用於該使用者所用任何程式碼庫的技能。                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> 提交至機器或容器中共用系統位置的任何技能。 | 適用於 SDK 指令碼、自動化，以及提交該機器上所有使用者都可使用的預設管理員技能。                                                                                     |
| `SYSTEM`    | 由 OpenAI 隨 Codex 一併提供。                                                                             | 適用於廣大使用者的實用技能，例如 skill-creator 和 plan 技能。所有使用者啟動 Codex 時都可使用。                                                                   |

Codex 支援以符號連結建立的技能資料夾，掃描這些位置時會跟隨符號連結的目標。

這些位置用於編寫和在本機探索技能。如果你想
在單一程式碼庫之外發佈可重複使用的技能，或選擇性地將技能與
連接器一起封裝，請使用 [外掛程式](https://developers.openai.com/plugins/build/plugins)。

## 使用外掛程式發佈技能

直接使用技能資料夾最適合在本機編寫技能，以及執行限於程式碼庫的工作流程。若
要發佈可重複使用的技能、將兩項或更多技能封裝在一起，或
將技能與連接器一併提供，請將這些內容封裝成
[外掛程式](https://developers.openai.com/plugins/build/plugins)。

外掛程式可包含一項或多項技能，也可視需要將已註冊的
MCP 伺服器連線、內附的 MCP 伺服器組態，以及
呈現用資產封裝在同一個套件中。

## 安裝精選技能供本機使用

若要為你的 Codex 本機設定新增內建技能以外的精選技能，請使用 `$skill-installer`。例如，若要安裝 `$linear` 技能：

```bash
$skill-installer linear

你也可以透過提示詞要求安裝工具從其他程式碼庫下載技能。
Codex 會自動偵測新安裝的技能；如果某項技能沒有出現，
請重新啟動 Codex。

此方式適用於本機設定和實驗。若要發佈自己建立的
可重複使用技能，請優先使用外掛程式。

## 啟用或停用 Codex 本機技能

使用 `[[skills.config]]` 設定項目（位於 `~/.codex/config.toml` 中），即可停用技能而不必刪除：

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

變更 `~/.codex/config.toml` 後，請重新啟動 Codex。

## 選用中繼資料

新增 `agents/openai.yaml`，即可在 [ChatGPT 桌面版應用程式](/zh-Hant/codex/app) 中設定 UI 中繼資料、設定叫用原則，並宣告工具相依性，讓技能使用體驗更加順暢。

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation`（預設值：`true`）：設為 `false` 時，Codex 不會根據使用者提示詞隱含叫用技能；仍可透過 `$skill` 明確叫用。

## 最佳實務

- 讓每項技能只專注於一項工作。
- 除非需要確定性行為或外部工具，否則請優先使用指示，而不是指令碼。
- 以祈使句撰寫步驟，並明確說明輸入與輸出。
- 根據技能說明測試提示詞，確認觸發行為正確。

如需更多範例，請參閱
[GitHub CI 修復](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)、
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf)、
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear)、
[openai/skills](https://github.com/openai/skills)，以及
[智慧體技能規格](https://agentskills.io/specification)。若要
以可安裝的形式發佈，請優先使用 [外掛程式](https://developers.openai.com/plugins/build/plugins)。
