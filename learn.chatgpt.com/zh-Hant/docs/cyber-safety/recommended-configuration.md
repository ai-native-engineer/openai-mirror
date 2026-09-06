<!-- source: https://learn.chatgpt.com/zh-Hant/docs/cyber-safety/recommended-configuration -->

適合網路安全工作流程的安全控制措施，取決於所用模型、模型可採取的動作、可存取的系統，以及所涉及資料的敏感程度。

對大多數 Daybreak Blue 工作流程而言，您的組織現有的安全做法，例如存取控制、憑證保護和敏感動作審查，可能就已足夠。

Daybreak Red 工作流程、自主安全測試，以及涉及正式環境系統、敏感資料或外部工具的活動，可能需要更嚴格的防護措施。以下建議主要適用於這些風險較高的情境。

  您有責任評估特定工作流程的風險，並
實作適當的安全控制措施。模型防護措施和 Trusted
Access 無法取代您的組織本身的安全、監控與
監督做法。

Trusted Access 負責管理經核准的模型存取，但不會設定您的環境，也不會對經核准的系統和動作強制設限。您的團隊必須設定適當的隔離、權限、審查、監控與人工監督控制措施。請假設模型、其工具及每個已連線的系統都可能遭入侵，再據此設定環境，使其仍無法連線至未授權的系統、暴露憑證、停用防護措施，或在工作結束後持續留存。

## 隔離環境

請在專用實驗室或沙盒中執行攻擊性安全工作。初始環境不應具備不受限制的網際網路存取權，也不應能存取敏感的正式環境系統、企業網路、無關的工作負載或主機管理介面。除非經核准的工作明確需要並授權，否則應確保無法接觸機密資訊、憑證、持久性存取權或持久性系統變更。

對於風險較高或防護措施較少的工作，每次嘗試都應使用全新且高度隔離的環境。將運算、儲存、網路和身分彼此隔離，並在工作結束後銷毀環境，不要重設或重複使用。

開始風險較高的工作前，先測試檔案系統和網路邊界。測試範圍應涵蓋每個可連線的主機、已連接的工具、受委派的智慧體和下游服務。即使模型或審查者已核准個別動作，也應讓主機環境保持隔離。

## 定義並強制執行核准範圍

在模型開始執行前，請記錄這項工作經核准的系統、工具、動作和時限，包括：

- 經核准的目標系統、主機和環境。
- 排除的系統，包括正式環境系統和無關的基礎架構。
- 經核准的工具與連線服務。
- 經核准與禁止的動作。
- 經核准的開始與結束時間，以及資料處理要求。
- 漏洞揭露、修補程式核准，以及與維護者的協調。
- 停止條件，以及需要明確人工核准的動作。

將這些核准範圍作為任務上下文提供給智慧體。單靠文件無法強制執行這些範圍：請對檔案系統、網路、身分和工具採用獨立控制措施，在可行的情況下讓未授權動作無法執行。

使用 Codex [權限設定檔](/zh-Hant/codex/permissions) 建立最低權限邊界。任務不需進行變更時，請選擇 `:read-only`；需要編輯工作區時，則擴充 `:workspace`。例如：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = "cyber-lab"

[features]
network_proxy = true

[permissions.cyber-lab]
description = "Limit security testing to the approved lab and workspace."
extends = ":workspace"

[permissions.cyber-lab.filesystem]
glob_scan_max_depth = 3

[permissions.cyber-lab.filesystem.":workspace_roots"]
"**/.env*" = "deny"
"**/*.pem" = "deny"

[permissions.cyber-lab.network]
enabled = true
# Uncomment only for an approved host that resolves to a private address.
# allow_local_binding = true

[permissions.cyber-lab.network.domains]
"lab.example.com" = "allow"

`network_proxy` 功能會強制執行經核准的網域限制。若未啟用此功能，
`network.enabled = true` 會允許直接存取網路，而實驗室允許清單
不會限制目的地。網頁搜尋、應用程式、連接器、MCP 伺服器、
瀏覽器活動和 Codex 雲端各自採用不同的控制機制；請限制或停用
經核准的工作流程不需要的每項功能。

將 `lab.example.com` 替換為經核准的目標。受限範圍的檔案系統掃描可避免在 Linux、WSL 和 Windows 上搜尋整個工作區；如果敏感檔案位於更深層，請增加掃描深度，或使用精確指定的拒絕路徑。請勿將權限設定檔與舊版 `sandbox_mode` 設定併用；請遵循 [權限設定檔組態指南](/zh-Hant/codex/permissions#define-and-select-a-profile)。

若經核准的實驗室主機解析為私人位址，即使該主機已在允許清單中，Codex 預設仍會封鎖它。只有在私人網路工作已獲明確核准時，才設定 `allow_local_binding = true`；請將目的地允許清單維持在最小範圍，並查閱 [本機與私人網路指南](/zh-Hant/codex/permissions#local-and-private-networks)。您也可以將經核准的確切私人 IP 位址加入允許清單。

預設封鎖對公開網際網路和正式環境網路的存取。如果必須存取外部網路，請透過由獨立機制強制管控的閘道或代理伺服器進行路由，並採用範圍嚴格受限的允許清單、請求檢查和記錄。对透過套件管理器、Webhook、URL 擷取服務、重新導向、雲端 API 和連線工具建立的間接連線，也套用相同限制。請在執行前載入相依項目，或使用管理員核准的相依項目。

## 保護憑證和敏感資料

請勿將可重複使用的 API 金鑰、雲端憑證、密碼和服務帳戶 Token 放入提示詞、程式碼庫、環境變數、共用檔案系統，以及模型可存取的紀錄中。需要身分驗證時，請使用獨立的憑證代理服務或閘道，提供僅適用於確切目標與允許動作的短期憑證，且不向模型揭露憑證。

只提供經核准任務所需的資料。移除不必要的敏感資訊，封鎖對雲端中繼資料和憑證端點的存取，並將模型產生的檔案視為不受信任。

在網路安全工作流程中，請避免使用 `:danger-full-access` 和 `--yolo`。完整存取權會移除可強制執行且自動審查所依賴的沙盒邊界。受管理的組織可排除 `:danger-full-access` 和 `--yolo`、限制允許的核准政策，並透過 [企業受管理的設定](/zh-Hant/codex/enterprise/managed-configuration#configure-automatic-review-policy) 要求執行自動審查。

為經核准的安全模型啟用 **完整存取權** 前，ChatGPT 桌面版應用程式會顯示該模型專屬的危險動作警告。警告會建議改用 **替我核准** ，並提供 [審查者政策組態](/zh-Hant/codex/sandboxing/auto-review#configuration) 的連結。這項警告不會恢復沙盒邊界，也不會覆寫組織政策。

防護機制會為受控的網路安全工作流程加入以政策為基礎的審查。這些機制無法取代環境隔離、最低權限、明確定義的範圍、監控或人工監督。

## 審查 Codex 的敏感動作

[自動審查](/zh-Hant/codex/sandboxing/auto-review) 會在擬執行的動作開始前，將符合條件的沙盒邊界核准要求交給獨立的審查者。審查者會考量擬執行的動作、範圍受限的任務上下文和適用政策，再核准或拒絕該要求。組織可以根據其核准目標、禁止動作，以及需要人工審查的條件自訂該政策。

凡是會影響正式環境、外部系統、敏感資料、權限提升、持久性存取或不可逆變更的動作，都必須取得明確的人工核准。將網站、程式碼庫、文件和工具輸出中嵌入的指示視為不受信任；這些指示不能擴大授權範圍或覆寫存取控制。

在 ChatGPT 桌面版應用程式中選取經核准的 Daybreak 模型時，如果您的帳戶可使用 **替我核准** 模式且組織政策允許，權限控制項就會自動切換至該模式。使用桌面版應用程式的 `/model` 指令時也是如此。如果該模式無法使用，目前的權限模式會維持不變。選取模型絕不會覆寫組織的受管理要求。

若要執行自動審查，請確保以下三項控制措施均已就緒：

1. 使用互動式核准政策，例如 `approval_policy = "on-request"`。
2. 設定 `approvals_reviewer = "auto_review"`。
3. 維持可強制執行的沙盒或權限設定檔邊界。

向網路允許清單上目標發出的要求會留在網路邊界內，因此不會自動觸發自動審查。即使目的地已在允許清單中，若仍要審查敏感指令，請建立明確的 [指令規則](/zh-Hant/codex/agent-configuration/rules)，並將其放在 `~/.codex/rules/` 下：

```python
prefix_rule(
    pattern = ["curl"],
    decision = "prompt",
    justification = "Review requests to the approved cybersecurity target.",
)

新增規則後，請重新啟動 Codex。設定 `approvals_reviewer = "auto_review"` 後，符合規則的指令會在執行前交由審查者處理。為每個敏感指令新增對應的提示規則，或使用 `approval_mode = "prompt"` 來處理個別 [MCP 工具](/zh-Hant/codex/extend/mcp)。仍須由人員決定的動作，依然需要明確的人工核准。

自動審查不會檢查沙盒內已獲准的例行動作。使用 `approval_policy = "never"` 或完整存取權時，敏感動作可能不會產生可供審查的核准要求。自動審查可能會出錯，且無法取代隔離、明確定義的範圍、監控或明確的人工監督。

若要設定範圍受限的政策並在整個組織強制執行，請參閱 [設定獲授權的網路安全工作流程](/zh-Hant/codex/sandboxing/auto-review#configure-an-authorized-cybersecurity-engagement)。

## 獨立監控並於失效時封鎖

記錄模型請求、工具呼叫、網路活動、憑證使用情況，以及與安全性相關的變更。將紀錄和監控系統置於模型所控制的環境之外。若出現未授權目標、非預期的網路請求、暴露的憑證、政策變更、紀錄缺失或規避防護措施的嘗試，請發出警示。

政策強制執行、憑證代理服務、審查系統和緊急關閉控制措施都應獨立於智慧體。若必要的控制措施或監控系統失效，請停止工作流程。

## 為自訂智慧體工作流程加入防護機制

如果您使用 Responses API、Agents SDK 或其他任務執行框架進行建置，請在工具執行邊界加入審查。執行前，請依據核准的系統、動作和時限檢查擬執行的敏感動作；將有疑義或高風險的動作交由人員處理；透過獨立機制強制執行檔案系統與網路限制；保留稽核紀錄；如果審查者或政策無法使用，則封鎖作業。

Codex 自動審查不會自動保護自訂工具或外部任務執行框架。請參閱適用於 Agents SDK 模式的 [防護機制與人工審查](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)，並以 [開放原始碼審查者政策](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md) 作為參考。

Codex 產品端的沙盒和審查與 [API 網路安全檢查](/api/docs/guides/safety-checks/cybersecurity) 相互獨立。API 防護措施可能會傳回 `cyber_policy` 錯誤，而每位使用者各自的 `safety_identifier` 值可協助限制防護措施所採取動作的影響範圍。

## 清理並驗證結果

工作結束後，撤銷暫時憑證、終止背景程序、移除持久性存取，並銷毀風險較高的環境。確認未留下任何回呼、暴露的成品、共用狀態或跨次執行的存取權，並讓不同的使用者、工作階段和評估彼此隔離。

在依據發現事項採取行動前先行驗證，遵循協調式揭露做法，並確保人員對修復和變更負責。

## 開始之前

請確認經核准的系統和動作、適當的模型、隔離環境、最低權限、受限的網路存取、受保護的憑證、動作審查、獨立監控、緊急停止機制，以及清理計畫。模型防護措施、隔離、範圍受限的權限、動作審查、監控和人工監督可相互補強；其中任何一項都不應是唯一的控制措施。
