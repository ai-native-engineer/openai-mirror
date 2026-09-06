<!-- source: https://learn.chatgpt.com/zh-Hant/docs/sandboxing/auto-review -->

自動審查會在沙盒邊界以獨立的
審查智慧體取代手動核准。主要 Codex 智慧體仍會在相同的沙盒內執行，並採用
相同的核准政策，以及相同的網路和檔案系統限制。差別只在於，符合條件的
權限提高要求由誰審查。

  自動審查僅適用於互動式核准。實際上，這
  表示使用 `approval_policy = "on-request"`，或使用仍會
  顯示相關提示類別的精細核准政策。如果使用 `approval_policy = "never"`，
  就沒有可供審查的項目。

在 ChatGPT 桌面 App 中，選取已核准的 Daybreak 模型
會自動將權限控制項切換為 **替我核准**，但前提是您的帳戶可使用該
模式，且組織政策允許。這項行為
也適用於桌面 App 的 `/model` 指令。如果該模式
無法使用，目前的權限模式會維持不變。選取模型
絕不會覆寫組織的受管理要求。

為已核准的安全性模型啟用 **完整存取權** 前，
ChatGPT 桌面 App 會顯示該模型專屬的危險動作警告。
警告會改為建議使用 **替我核准**，並連結至
[審查政策組態](#configuration)。此警告不會恢復
沙盒邊界，也不會覆寫組織政策。

## 自動審查的運作方式

概略流程如下：

1. 主要智慧體會在 `read-only` 或 `workspace-write` 中運作。
2. 當需要跨越沙盒邊界時，就會要求核准。
3. 如果設定為 `approvals_reviewer = "auto_review"`，Codex 會將該核准要求
   交由獨立的審查智慧體處理，而不是暫停並等候人工處理。
4. 審查智慧體會判斷是否應執行該動作，並傳回判斷理由。
5. 如果動作獲得核准，就會繼續執行。如果遭拒，系統會指示主要
智慧體尋找實質上更安全的做法，否則就停止並詢問
使用者。

自動審查只是更換審查者，並非授予權限。它不會擴大
`writable_roots`、啟用網路存取或削弱受保護的路徑，只會
改變 Codex 處理原本就需要核准之動作的方式。

## 觸發時機

自動審查會評估原本需要暫停並等待人工處理的核准要求。
這些要求包括：

- 要求提高沙盒權限的 Shell 或 exec 工具呼叫。
- 遭目前沙盒或政策封鎖的網路請求。
- 對允許寫入的根目錄以外的檔案進行編輯。
- 根據工具註解
或設定的核准模式而需要核准的 MCP 或應用程式工具呼叫。
- 電腦存取新網站或網域的動作。

自動審查不會針對沙盒內已允許的例行動作執行。
如果指令可在目前的 `sandbox_mode` 下執行，或工具呼叫
未超出允許的政策範圍，主要智慧體會直接繼續執行，無須審查。

電腦是另一種情況。電腦的 App 核准仍會
直接顯示給使用者，因此自動審查不會取代這些 App 層級的提示。

## 自動審查會封鎖哪些動作

整體而言，自動審查旨在封鎖下列動作：

- 將私密資料、機密資訊或憑證傳送至不受信任的目的地
- 探查憑證、Token、Cookie 或工作階段資料
- 大範圍或持續削弱安全性的動作
- 具有重大不可逆損害風險的破壞性動作

確切政策位於 Codex 開放原始碼程式碼庫內：
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
與
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
這項政策可由各企業透過 `guardian_policy_config` 自訂，或
由各使用者透過本機的 [`[auto_review].policy`](/zh-Hant/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) 自訂。

## 審查智慧體看到的內容

審查智慧體本身也是 Codex 智慧體，但職責比主要智慧體更專一：
判斷是否應執行某個跨越邊界的特定動作。

審查智慧體會看到精簡的對話記錄，以及確切的核准要求。內容
通常包括使用者訊息、已顯示的助理更新、相關工具
呼叫和工具輸出，以及目前提請核准的動作。它也可以
執行唯讀檢查以取得缺少的上下文，但很少這麼做。

不包含助理的隱藏推理。自動審查看到的是已保留的
對話項目和工具證據，而非私密的思路鏈。

## 遭拒與失敗時的行為

明確拒絕不會當作一般沙盒錯誤處理。Codex 會將
審查理由傳回主要智慧體，並加入更嚴格的指示：

- 不得透過變通方法、間接執行或規避
政策來達成相同結果。
- 只有改採實質上更安全的替代方案，才能繼續。
- 否則，請停止並詢問使用者。

Codex 也會為每一輪套用拒絕斷路器。在目前的
開放原始碼實作中，自動審查會在連續遭拒 `3` 次，
或遭拒 `10` 次且這些拒絕落在同一輪最近 `50`
次審查的滾動視窗內時，中斷該輪。

任何非拒絕結果都會重設連續拒絕計數器。斷路器觸發時，
Codex 會發出警告，並以中斷方式終止目前這一輪，而不會
讓智慧體反覆提出更多提高權限要求。

逾時會與明確拒絕分開顯示，且系統會告知主要智慧體，
單憑逾時並不能證明該動作不安全。

遭拒動作也有明確的覆寫途徑。在目前的
開放原始碼 TUI 中，執行 `/approve` 以開啟 **自動審查遭拒項目** 選擇器，然後
選取一個最近遭拒的動作，核准重試一次。Codex 會為每項任務記錄最多 10
個最近遭拒項目。這項核准的範圍很窄：只適用於該項確切
遭拒的動作，不適用於未來的類似動作；系統會記錄該核准，讓它在
相同上下文中重試一次；而且重試仍會經過自動審查。實際運作上，
Codex 會為該項確切動作注入一個限定於開發者層級的核准標記。接著，
審查智慧體會將使用者的明確覆寫視為上下文，但仍會遵循
政策；如果政策規定使用者無權覆寫這類
拒絕，審查智慧體仍可再次拒絕。

## 組態

如需設定詳細資訊，請參閱
[受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-automatic-review-policy)。

預設審查政策位於 Codex 開放原始碼程式碼庫中：
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
企業可在受管理的要求中使用
`guardian_policy_config` 取代其中的租用戶專屬區段。個別使用者也可設定
本機的
[`[auto_review].policy`](/zh-Hant/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
並將其寫入 `config.toml`，但受管理的要求具有優先權：

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

如要自訂政策，請先複製整份預設政策文字，再
根據您自己的風險概況逐步調整。

## 設定已獲授權的網路安全作業

對於已獲授權的安全性工作，請搭配使用自動審查、書面記載的
作業範圍，以及遵循最小權限原則的 [權限設定檔](/zh-Hant/codex/permissions)。
使用已核准的實驗室目標，記錄動作和作業時段，並將
正式環境系統、不相關的主機、憑證和持久性變更
排除在範圍之外，除非已明確獲得授權。

`[auto_review].policy` 和 `guardian_policy_config` 都會取代您目前的
審查政策，且不會與模型隨附或
由組織管理的政策合併。內建的審查指示和回應
格式仍然適用。使用任一範例前，請複製目前
政策的完整內容，保留所有現有規則，並加入已核准工作的規則。
請以這份完整政策取代全大寫的預留位置。如果您無法
存取目前的政策，請勿覆寫。

以下本機 `config.toml` 範本會啟用審查，並在現有審查政策之後加入限定範圍的
條件：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

將範例中的目標與允許動作替換為實際獲核准的範圍。
使用獨立的檔案系統與網路規則來強制執行目標限制；
審查指示無法取代這些邊界。

組織可以在受管理的 `requirements.toml` 中強制執行相同條件：

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` 會控制目前的權限設定檔。
`allowed_sandbox_modes` 也能在仍使用
舊版 `sandbox_mode` 的部署中防止啟用完整存取權。

受管理的 `guardian_policy_config` 優先於使用者的本機
`[auto_review].policy`。請繼續採用 `approval_policy = "on-request"` 或其他
符合條件的互動式核准政策，並維持可強制執行的沙盒邊界。
使用 `approval_policy = "never"`、`:danger-full-access` 或 `--yolo` 時，動作
可能不會產生審查所需的跨越邊界核准要求。

允許清單中的網路目的地本身不會觸發審查。請加入
明確的 [指令規則](/zh-Hant/codex/agent-configuration/rules)，並設定
`decision = "prompt"`，或將敏感的 MCP 工具設定為需要核准，
以便沙盒內的動作仍須交由審查智慧體處理。

若要了解模型存取、作業設定和自訂智慧體工作流程，請參閱 [模型與受信任存取權](/zh-Hant/codex/cyber-safety) 和 [建議
組態](/zh-Hant/codex/cyber-safety/recommended-configuration)。
若要了解企業層級的優先順序及支援的用戶端版本，請參閱 [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-automatic-review-policy)。
自訂 API 或
Agents SDK 任務執行框架則應採用 [防護機制與人工審查](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)。

## 在不削弱安全性的情況下降低審查量

自動審查在沙盒已涵蓋您常用且安全的
工作流程時效果最佳。如果太多瑣碎動作需要審查，應先修正邊界，
而不是讓審查智慧體長期核准這些徒增干擾的權限提高要求。

實務上，效益最高的變更包括：

- 加入範圍有限的
[`writable_roots`](/zh-Hant/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  供您刻意使用的暫存目錄或相鄰程式碼庫使用。
- 加入範圍嚴格限定的 [前綴規則](/zh-Hant/codex/agent-configuration/rules)。請優先採用精確的指令
  前綴，例如 `["cargo", "test"]` 或 `["pnpm", "run", "lint"]`，不要採用過於廣泛的
  模式，例如 `["python"]` 或 `["curl"]`。廣泛規則經常會消除
  自動審查原本要保護的邊界。

自動審查工作階段的對話記錄預設會保留在 `~/.codex/sessions` 下，
因此您可以先要求 Codex 分析其中的過往活動，再變更
政策或權限。

## 限制

自動審查可改善長時間執行智慧體式工作時的預設運作狀態，
但並非確定性的安全保證。

- 它只會評估要求跨越邊界的動作。
- 它仍可能出錯，尤其是在對抗性或不尋常的情境下。
- 它應與良好的沙盒設計、監控及
組織專屬政策相輔相成，而非取代它們。

如需瞭解研究依據與已發布的評估結果，請參閱
[關於自動審查的 Alignment Research 文章](https://alignment.openai.com/auto-review/)。
