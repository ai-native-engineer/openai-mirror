<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/admin-plugin -->

透過本指南，了解管理外掛程式如何協助處理常見管理工作、做好任務準備，並在取得適當核准與上下文後，試用主要使用案例的提示詞。

## 1. 了解管理外掛程式的用途

管理外掛程式旨在協助你直接在 ChatGPT Work 中管理設定、權限與控管項目。你只需用日常語言說明目標，外掛程式就會蒐集所需資訊、讀取目前狀態、說明查得的內容，並引導你進行下一步支援的操作。

### 管理外掛程式旨在解決哪些問題

- 將管理需求轉化為清楚的工作流程，無須自行撰寫 API 請求。
- 在做出決策或核准變更之前，審查工作區的目前狀態。
- 列出回答所依據的已授權來源與欄位，以及無法驗證的事項。
- 在執行支援的變更前暫停，等待審查；變更後再讀取一次紀錄，確認結果。

外掛程式會在背後使用特定的管理 API，以及已核准並已連接的資料來源。它不會整合所有管理系統、擴大你的權限，或讓 ChatGPT 能執行所有 API 操作。外掛程式可以讀取或變更哪些內容，仍由擁有資料的系統控管。

### 管理 API 旨在解決哪些問題

管理 API 讓軟體能以結構化方式請求資料或要求執行支援的操作。組織可以使用管理 API 建立內部流程或外部工具。常見例子包括定期產生報表、對大量紀錄執行重複作業，以及連接至已核准的系統。這些工作流程通常需要經過工程、安全性與治理審查。

使用本指南不需要先建立 API 工作流程。後續內容會以管理外掛程式為主。ChatGPT 工作區管理與 API 平台管理仍然彼此獨立，各有其權限與身分驗證要求。

### 確保憑證不外洩

僅使用組織核准的連線與機密儲存系統。切勿將真正的管理 API 金鑰貼到 ChatGPT、Codex、文件或原始碼檔案中。

## 2. 準備使用管理外掛程式

如果你想用日常語言處理一次性任務，且該任務在支援範圍內，就可以使用管理外掛程式。說明目標，並提供固定 ID 或已核准的報表上下文。外掛程式會先顯示查得的內容或預計進行的變更，再由你決定是否繼續。

外掛程式只會使用該任務獲授權使用的來源、憑證與操作。它不會整合所有管理系統，也不會賦予你更廣泛的權限。資料仍以原始系統為準。

### 開始之前

1. 找出存放紀錄的管理區域。
2. 備妥所需資訊，並取得必要核准。
3. 先從唯讀請求開始。
4. 詢問外掛程式使用了哪些來源與欄位，以及有哪些事項無法驗證。
5. 對於支援的變更，請先審查計畫，再予以核准。接著請外掛程式再次讀取紀錄，確認結果。

確認你的工作區可使用此外掛程式，而且你具有所需權限。以下角色與存取權使用案例，依據的是外掛程式目前文件記載的支援範圍。外掛程式可以審查角色、功能權限，以及使用者或群組的角色指派情形。在你確認後，它也能將現有角色指派給現有群組。

外掛程式無法建立角色、變更角色的權限，或確認是否具有特定連接器的存取權。

分析使用案例需要存取已連接且已核准的資料來源。ROI 分析也需要已核准的業務或工程成果；只有使用紀錄並不足夠。

## 3. 探索管理外掛程式的主要使用案例

選擇一個使用案例，以已核准請求中的值取代各個預留位置，然後依序執行步驟。除非任務是已獲核准且在支援範圍內的變更，否則應先從唯讀請求開始。

### 列出工作區角色

**試試這個提示詞**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**步驟**

1. **準備：** 確認工作區 ID，以及你是否獲准查看這些資訊。
2. **執行：** 要求以唯讀方式列出角色。
3. **審查：** 檢查角色類型、功能存取權與指派情形。
4. **驗證：** 釐清任何不符預期的情況，但不要進行變更。

### 審查單一角色

**試試這個提示詞**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**步驟**

1. **準備：** 確認角色 ID 與工作區。
2. **執行：** 要求以唯讀方式審查角色。
3. **審查：** 檢查權限與指派情形是否符合角色的預期用途。
4. **驗證：** 記下要向角色負責人詢問的問題。請記得，外掛程式無法建立角色或編輯其權限。

### 了解使用者或群組的存取權

**試試這個提示詞**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**步驟**

1. **準備：** 使用該使用者或群組的固定 ID。
2. **執行：** 請外掛程式說明存取權。
3. **審查：** 檢查已指派哪些角色，以及這些角色提供哪些存取權。註記任何重疊或缺漏。
4. **驗證：** 若外掛程式無法查看某項資訊，請將其標示為未知，不要猜測。

### 將現有角色指派給群組

**試試這個提示詞**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**步驟**

1. **準備：** 確認群組與角色的 ID。核對已核准的請求，以及紀錄中的核准者。
2. **執行：** 請外掛程式顯示目前的角色與預計變更的內容。
3. **審查：** 只有在計畫符合已核准的請求時，才予以核准。
4. **驗證：** 指派完成後，再次檢查群組，確認已按核准內容新增該現有角色。

### 檢查連接器的一般權限

**試試這個提示詞**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**步驟**

1. **準備：** 確認使用者 ID，以及你是否有權審查該使用者的存取權。
2. **執行：** 要求進行一般權限檢查。
3. **審查：** 檢查已指派的角色，以及回答所依據的權限。
4. **驗證：** 這僅能作為一般檢查，不能證明具有特定連接器或已連線項目的存取權。

### 排解已核准變更的問題

**可嘗試的提示詞**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**步驟**

1. **蒐集資料：** 確認已核准的變更紀錄與預期結果。
2. **執行：** 請外掛程式比對請求內容與工作區目前的狀態。
3. **審查：** 檢查工作區與角色，再確認紀錄擁有者。
4. **驗證：** 在決定下一步之前，請以工作區目前的狀態為準。

### 最佳化成本與模型組合

**可嘗試的提示詞**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**步驟**

1. **蒐集資料：** 確認工作區、日期範圍，以及成本資料是否涵蓋整段期間。檢查有哪些已核准的效能或成果欄位可用。
2. **執行：** 要求提供成本與模型的比較。
3. **審查：** 清楚區分資料呈現的結果與假設、缺少的輸入資料及各項取捨。
4. **驗證：** 採取行動前，先與 Finance 和工作流程負責人確認可能節省的成本。

### 了解使用與採用情況

**可嘗試的提示詞**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**步驟**

1. **蒐集資料：** 檢查工作區、日期範圍與團隊對應關係。確認已獲准提供使用者層級的報表。
2. **執行：** 要求分析使用與採用情況。
3. **審查：** 檢查所要求的欄位有哪些可用。缺少的活動資料應略過，不要自行猜測。
4. **驗證：** 使用量高並不能作為進階應用、商業價值或個人績效的證明。

### 衡量商業價值與 ROI

**可嘗試的提示詞**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**步驟**

1. **蒐集資料：** 檢查工作區與日期範圍，再確認已核准的成果。審查計算公式與隱私規則。
2. **執行：** 要求提供 ROI 分析。
3. **審查：** 檢查每個來源與每項假設。記下每項限制或缺少的輸入資料。
4. **驗證：** 僅憑使用量無法證明 ROI 或因果關係。請與 Finance 和業務負責人共同審查結果。

### 評估 Codex ROI

**可嘗試的提示詞**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**步驟**

1. **蒐集資料：** 確認工作區與報告涵蓋的期間。審查團隊及程式碼庫的對應關係，以及已核准的基準資料。
2. **執行：** 要求提供 Codex ROI 分析。
3. **審查：** 區分觀察到的模式與假設。保護使用者與程式碼庫資料。
4. **驗證：** 與工程團隊共同審查建議與成果基準。

## 4. 何時可考慮採用 API 工作流程

有些組織會使用 API 建立自己的管理流程或外部工具。這種方式可支援排程執行或持續進行的工作。當流程涉及大量紀錄，或需要連接已核准的內部系統時，也能派上用場。這與 Admin 外掛程式提供的引導式體驗是不同的使用方式。

從明確定義的管理任務開始：釐清所需的輸入資料與權限、審查節點、預期結果，以及記錄成果的方式。如果組織要將此任務自動化，請讓相關的工程、安全性與治理團隊參與，將憑證存放在已核准的機密儲存系統中，並在部署前測試工作流程。

### 相關資源

- [ChatGPT 工作區 Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)
- [管理界限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [ChatGPT 工作區 Analytics API](/zh-Hant/codex/enterprise/analytics-api)
- [ChatGPT 工作區 Compliance API](/zh-Hant/codex/enterprise/compliance-api)
