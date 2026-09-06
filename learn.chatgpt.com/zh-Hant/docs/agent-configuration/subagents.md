<!-- source: https://learn.chatgpt.com/zh-Hant/docs/agent-configuration/subagents -->

ChatGPT Work 和 Codex 可平行啟動各有專長的智慧體，執行子代理程式工作流程，再將結果彙整成一則回應。對於能高度平行處理的複雜任務，例如探索程式碼庫或實作多步驟的功能計畫，這種方式特別有幫助。

在本機 Codex 用戶端中，您也可以針對不同任務定義自訂智慧體，為其設定不同的模型組態與指示。

## 可用性

ChatGPT Work 為符合資格的帳戶提供子代理程式工作流程與活動資訊。

<a id="custom-agents"></a>

目前的 Codex 版本預設啟用子代理程式工作流程。子代理程式活動會顯示在 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中。

由於每個子代理程式都會各自執行模型與工具相關工作，子代理程式工作流程會比同等的單一智慧體執行作業消耗更多 Token。

在 ChatGPT Work 中，請要求 ChatGPT 將可獨立處理的工作委派給子代理程式。這些智慧體會在 ChatGPT 的託管環境中執行，對話中則會顯示其活動與結果。在多數智慧等級下，您需要明確要求委派。使用 Ultra 時，若平行執行智慧體能實質提升速度或品質，ChatGPT 可主動委派工作。

請在 App 對話中要求 Codex 將可獨立處理的工作委派給
子代理程式。目前的本機 Codex 版本會在您直接提出要求，或
適用的 `AGENTS.md` 或技能指示要求委派時進行委派。App 會顯示每個
子代理程式執行緒，讓您檢視其工作內容，以及傳回
主對話的摘要。

請在互動式 CLI 工作階段中要求 Codex 使用子代理程式。Codex 也可遵循
適用的 `AGENTS.md` 或技能指示中的委派要求。執行期間，可使用
`/agent` 檢視智慧體執行緒並在其間切換。主執行緒
會將子代理程式的結果彙整至最終回應中。

請在 IDE 對話中要求 Codex 將可獨立處理的工作委派給子代理程式。
Codex 也可遵循適用的 `AGENTS.md` 或技能指示中的
委派要求。背景智慧體介面可用時，執行中的子代理程式會顯示在
撰寫工具上方。展開面板即可查看其狀態、停止所有執行中的
子代理程式，或開啟個別子代理程式執行緒。

## 子代理程式工作流程為何有幫助

即使有大型上下文視窗，模型仍有限制。如果您用來定義需求、限制與決策的主對話，充斥著探索筆記、測試紀錄、堆疊追蹤和指令輸出等雜亂的中間輸出，工作階段的可靠性可能會隨時間降低。

這通常稱為：

- **上下文污染**：有用的資訊被雜亂的中間輸出掩蓋。
- **上下文衰退**：隨著對話充斥關聯性較低的細節，模型的表現逐漸變差。

如需背景資訊，請參閱 Chroma 有關[上下文衰退](https://research.trychroma.com/context-rot)的文章。

子代理程式工作流程會將容易產生雜訊的工作移出主執行緒，帶來以下好處：

- 讓 **主智慧體** 專注於需求、決策和最終輸出。
- 平行執行各有專長的 **子代理程式** ，進行探索、測試或紀錄分析。
- 讓子代理程式傳回 **摘要** ，而非原始的中間輸出。

當工作可獨立平行執行時，子代理程式工作流程也能節省時間，並將規模較大的任務拆分成範圍明確的部分，使其更容易處理。例如，Codex 可將一份數百萬 Token 文件的分析工作拆成較小的問題，並將精煉後的重點傳回主執行緒。

一開始可將平行智慧體用於以讀取為主的任務，例如探索、測試、問題分流和摘要。使用以寫入為主的平行工作流程時則應更加謹慎，因為多個智慧體同時編輯程式碼可能會造成衝突，並增加協調成本。

## 核心術語

Codex 在子代理程式工作流程中使用以下相關術語：

- **子代理程式工作流程**：Codex 平行執行多個智慧體，並彙整其結果的工作流程。
- **子代理程式**：由 Codex 啟動，並受委派處理特定任務的智慧體。
- **智慧體執行緒**：子代理程式執行工作的執行緒。支援此功能的用戶端可讓您開啟這些執行緒，檢視進度或結果。

## 觸發子代理程式工作流程

在多數智慧等級下，請直接要求使用子代理程式，或讓智慧體平行工作。Ultra 支援主動委派，因此 ChatGPT 可在無須另行要求的情況下，委派適合獨立處理的工作。

請直接要求使用子代理程式，或讓智慧體平行工作。適用的專案或技能指示要求委派時，Codex 也可進行委派。

實務上，手動觸發是指使用直接指示，例如「啟動兩個智慧體」、「委派這項工作，讓智慧體平行處理」，或「每個要點交給一個智慧體」。子代理程式工作流程比同等的單一智慧體執行作業消耗更多 Token，因為每個子代理程式都會各自執行模型與工具相關工作。

良好的子代理程式提示詞應說明如何拆分工作、Codex 是否應等待所有智慧體完成後再繼續，以及要傳回何種摘要或輸出。

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## 選擇模型與推理設定

不同的智慧體需要不同的模型與推理設定。

在 ChatGPT Work 中，請從撰寫工具選擇模型與智慧等級。
視所選模型而定，可用的智慧等級可能包括 **輕度**、 **中**、 **高**、
**極高**和 **Max**。 **Ultra** 僅
開放給符合資格的帳戶，且必須使用支援的模型。它採用最高推理強度，
讓 ChatGPT 能主動將適合的工作委派給子代理程式。

在其他智慧等級下，如果希望平行委派工作，請明確要求使用子代理程式。

如果未設定子代理程式的模型或 `model_reasoning_effort`，
子代理程式會繼承父智慧體的模型與推理強度。若明確的
啟動要求或 `[agents]` 預設值指定了模型，但未
明確指定或設定推理強度，子代理程式會採用該模型的
預設推理強度。若要針對每項任務兼顧智慧、速度和價格，請
在提示詞中要求使用特定模型或推理強度，
在 `config.toml` 中設定 `[agents]` 的預設值，或直接在自訂智慧體檔案中設定 `model` 與
`model_reasoning_effort`。
例如，快速掃描可使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>；對推理要求較高的工作，則可採用推理強度較高的 <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> 組態。

  在 Codex 中，大多數任務建議先使用{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>。如果想以更快的速度、更低的成本
處理較輕量的子代理程式工作，
  請使用{" "}<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>。

### 模型選擇

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**：智慧體需要處理高難度任務時，請優先選擇此模型。它最擅長處理需求模糊、涉及多個步驟，且需要在較大上下文中規劃、使用工具、驗證並持續推進至完成的工作。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**：適合優先考量速度與效率、其次才是深度的智慧體，例如用於探索、以讀取為主的掃描、大型檔案審查或處理輔助文件。對於平行執行工作並將精煉後的結果傳回主智慧體的智慧體，這個模型很適合。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**：適合需要快速執行、職責範圍狹窄的智慧體，用於處理明確、可重複或大量的工作。

### 推理強度（`model_reasoning_effort`）

- **`ultra`**：所選模型支援時，可用於
  最深入的推理。
- **`max`** 和 **`xhigh`**：所選模型支援這些等級時，
  可用於要求特別高的推理。
- **`high`**：適合需要追查複雜邏輯、檢查假設或處理邊界情況的智慧體，例如負責審查或著重安全性的智慧體。
- **`medium`**：適合大多數智慧體的均衡預設值。
- **`low`**：適合任務單純明確，且最重視速度的情況。

提高推理強度會增加回應時間與 Token 用量，但有助於提升複雜工作的品質。如需詳細資訊，請參閱[模型](/zh-Hant/codex/models)、[基本設定](/zh-Hant/codex/config-file/config-basic)和[組態參考資料](/zh-Hant/codex/config-file/config-reference)。

## 編排與執行緒控制

ChatGPT 或 Codex 負責跨智慧體的編排，包括啟動新的子代理程式、轉送後續指示、等待結果，以及關閉智慧體執行緒。

多個智慧體同時執行時，Codex 會等到所有要求的結果都備齊，再傳回彙整後的回應。

在多數智慧等級下，ChatGPT 會在收到直接要求後啟動智慧體。使用 Ultra 時，若平行處理有幫助，ChatGPT 也可主動委派工作。

目前的本機 Codex 版本會在收到直接要求，或適用的專案或技能指示提出要求後，啟動智慧體。

若要查看實際運作情形，請在您的專案中嘗試以下提示詞：

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## 管理子代理程式

開啟 **子代理程式** ，即可查看唯讀的 **執行中** 和 **已完成** 清單。
選取已完成的子代理程式，以檢視其詳細資料和結果。網頁側邊欄會顯示
子代理程式活動，但不提供停止或引導
個別子代理程式的控制項。

- 從主執行緒顯示的活動中開啟子代理程式執行緒，以檢視其工作內容。
- 直接要求 Codex 引導或停止執行中的子代理程式，或關閉已完成的子代理程式執行緒。

  

  

- 在 CLI 中使用 `/agent`，即可在執行中的智慧體執行緒之間切換，並查看進行中的執行緒。
- 直接要求 Codex 引導或停止執行中的子代理程式，或關閉已完成的智慧體執行緒。

- 背景智慧體面板可用時，展開面板即可查看狀態、停止執行中的子代理程式，或開啟子代理程式執行緒。
- 直接要求 Codex 引導或停止執行中的子代理程式，或關閉已完成的子代理程式執行緒。

## 核准與沙盒控制

子代理程式會繼承您目前的沙盒原則。

ChatGPT Work 會在其託管環境中執行子代理程式，不提供本機 Codex 沙盒或核准模式的控制選項。子代理程式會使用上層對話可用的工具。網站與連接器的權限仍依個別工具而定。

子代理程式會繼承您在撰寫工具下方選取的權限模式。要求 Codex 委派工作前，請先為上層輪次選擇權限模式。

在互動式 CLI 工作階段中，即使您正在查看主執行緒，
非作用中的智慧體執行緒仍可能提出核准要求。核准覆疊視窗
會顯示來源執行緒的標籤；您可以按下 `o` 開啟該執行緒，
再核准、拒絕或回應要求。

在非互動式流程中，或執行過程中無法顯示新的核准要求時，需要新核准的動作會失敗，Codex 會將錯誤傳回上層工作流程。

Codex 啟動子智慧體時，也會重新套用上層輪次目前的執行階段覆寫設定。
這包括您在工作階段中以互動方式設定的沙盒與核准選項，
例如透過 `/permissions` 進行的變更或 `--yolo`；即使所選的
自訂智慧體檔案設定了不同的預設值，也同樣適用。

子代理程式會繼承您在撰寫工具下方選取的權限模式。要求 Codex 委派工作前，請先為上層輪次選擇權限模式。

您也可以覆寫個別[自訂智慧體](#custom-agents)的沙盒組態，例如明確指定其中一個以唯讀模式運作。

## 自訂智慧體

Codex 隨附下列內建智慧體：

- `default`：通用備援智慧體。
- `worker`：專注於執行工作的智慧體，用於實作與修正。
- `explorer`：以讀取為主的程式碼庫探索智慧體。

若要定義自己的自訂智慧體，請新增獨立的 TOML 檔案：
個人智慧體放在 `~/.codex/agents/` 下，專案範圍的智慧體
則放在 `.codex/agents/` 下。

每個檔案定義一個自訂智慧體。Codex 會將這些檔案載入為新啟動工作階段的組態層，因此自訂智慧體能覆寫的設定與一般 Codex 工作階段組態相同。相較於專用的智慧體資訊清單，這種方式可能較為繁瑣；隨著編寫與分享方式日趨成熟，格式也可能隨之演進。

每個獨立的自訂智慧體檔案都必須定義：

- `name`
- `description`
- `developer_instructions`

如果自訂智慧體檔案設定了 `model` 或 `model_reasoning_effort`，
會優先採用檔案中的值。套用檔案前，Codex 會依下列優先順序決定各項設定：
啟動時明確指定的值、對應的 `[agents]` 預設值，
最後是上層智慧體的值。如果明確的啟動要求或 `[agents]` 預設值
指定了模型，但兩者都未提供推理強度，
Codex 會使用該模型的預設推理強度。若自訂智慧體檔案只設定 `model`，
則會保留先前決定的推理強度。若要指定不同的推理強度，請在檔案中一併設定 `model_reasoning_effort`；
所選模型不支援該推理強度時，
也請如此設定。其他工作階段設定，例如 `sandbox_mode`、`mcp_servers`
 和 `skills.config`，若自訂智慧體檔案未設定，
則會從上層智慧體繼承。

### 全域設定

子代理程式的全域設定仍位於[組態](/zh-Hant/codex/config-file/config-basic#configuration-precedence)中的 `[agents]` 區段。

| 欄位                                       | 類型    | 必填 | 用途                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | 布林值 |    否    | 啟用或停用多智慧體工具。                                |
| `agents.max_concurrent_threads_per_session` | 數值  |    否    | 限制新啟動智慧體可同時開啟的執行緒數，不含主執行緒。 |
| `agents.default_subagent_model`             | 字串  |    否    | 設定新啟動智慧體的預設模型。                           |
| `agents.default_subagent_reasoning_effort`  | 字串  |    否    | 設定新啟動智慧體的預設推理強度。                |
| `agents.interrupt_message`                  | 布林值 |    否    | 智慧體輪次中斷時，記錄一則模型可見的訊息。   |

**注意事項：**

- `agents.enabled` 的預設值為 `true`。將其設為 `false` 可停用多智慧體工具。
- 若未設定 `agents.max_concurrent_threads_per_session`，Codex 會選擇預設值。現有組態可繼續使用 `agents.max_threads` 作為舊版別名。
- 啟動時明確指定的值會覆寫 `agents.default_subagent_model` 和 `agents.default_subagent_reasoning_effort`。
- `agents.interrupt_message` 的預設值為 `true`。將其設為 `false`，即可讓智慧體的上下文不包含模型可見的中斷訊息。
- 如果自訂智慧體的名稱與 `explorer` 等內建智慧體相同，會優先使用您的自訂智慧體。

### 自訂智慧體檔案結構描述

| 欄位                    | 類型   | 必填 | 用途                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | 字串 |   是    | Codex 啟動或提及此智慧體時使用的名稱。 |
| `description`            | 字串 |   是    | 供使用者閱讀的指引，說明 Codex 應在何時使用此智慧體。     |
| `developer_instructions` | 字串 |   是    | 定義智慧體行為的核心指示。             |

您也可以在自訂智慧體檔案中加入其他受支援的 `config.toml` 設定鍵，例如 `model`、`model_reasoning_effort`、`sandbox_mode`、`mcp_servers` 和 `skills.config`。

Codex 會依據 `name` 欄位識別自訂智慧體。
最簡單的慣例是讓檔名與智慧體名稱相符，
但最終仍以 `name` 欄位為準。

### 自訂智慧體範例

理想的自訂智慧體應專注於特定任務，並具備明確的執行原則。請為每個智慧體指定一項明確的任務，提供適合該任務的工具，並透過指示避免它偏離職責，延伸處理其他相關工作。

#### 範例 1：PR 審查

這種模式會將審查工作分配給三個各有明確職責的自訂智慧體：

- `pr_explorer` 會梳理程式碼庫並蒐集證據。
- `reviewer` 會檢查正確性、安全性與測試方面的風險。
- `docs_researcher` 會透過專用的 MCP 伺服器查閱框架或 API 文件。

專案設定（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`：

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`：

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`：

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

這項設定適合用於以下這類提示詞：

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### 範例 2：前端整合偵錯

這種模式適用於 UI 迴歸問題、不穩定的瀏覽器操作流程，或同時涉及應用程式程式碼與執行中產品的整合錯誤。

專案設定（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`：

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`：

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`：

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

這項設定適合用於以下這類提示詞：

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
