<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/workload-identity -->

工作負載身分聯盟可讓受信任的自動化程序使用 Codex，無須儲存個人存取 Token 或其他長效 OpenAI 憑證。工作負載會出示由您現有提供者簽發的短效身分 Token。OpenAI 會驗證該 Token，並為受管理的 ChatGPT 工作區中的使用者或服務帳戶傳回短效存取 Token。

在雲端平台、
Kubernetes、CI 系統，以及其他可簽發 OIDC Token 或
SPIFFE JWT-SVID 的環境中，使用工作負載身分執行無人值守的 Codex 程序。如需了解共用信任模型和獨立的 OpenAI API 流程，
請參閱[工作負載身分概覽](/api/docs/guides/workload-identity-federation)。

  Codex 工作負載身分聯盟目前為測試版，必須先為您的
  工作區啟用。如需申請存取權，請聯絡您的 OpenAI 代表或[OpenAI
  支援團隊](https://help.openai.com/en/articles/6614161-how-can-i-contact-support)。

## 開始之前

您需要：

- 在 OpenAI 管理入口網站中管理工作負載身分的權限。
- 受管理的 ChatGPT 工作區。
- 具有該工作區有效成員資格的 ChatGPT 使用者或服務帳戶，或在設定期間建立此類帳戶的權限。
- OIDC Token 或 SPIFFE JWT-SVID，且您已知其簽發者、對象和用於識別身分的宣告。
- 能持續更新 Token，並將其保存在絕對路徑下受保護檔案中的執行階段。
- Codex 0.148.0 或更新版本。
- 實際生效的 Codex 身分驗證政策，須允許 ChatGPT 身分驗證，
  並允許聯盟規則選取的工作區。請參閱[強制指定登入
  方式或工作區](/zh-Hant/codex/auth#enforce-a-login-method-or-workspace)。

OpenAI 不會在交換 Token 時建立主體或授予工作區成員資格。管理員須在工作負載連線前選取或建立主體。建立真人使用者會占用一個工作區席次，且須遵守該工作區的成員資格規則。

在原生 Windows 上，請使用 **提高權限**的
[Windows 沙盒](/zh-Hant/codex/windows/windows-sandbox)。其他 Windows 沙盒模式
無法防止由模型控制的指令存取身分 Token 檔案。

## 取得身分 Token

工作負載執行階段負責取得及更新上游身分 Token。Codex 不會代您呼叫雲端中繼資料服務或身分提供者的用戶端程式庫。

| 執行階段                          | 建議的 Token 檔案來源                                                                                                   |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Kubernetes、AKS、EKS 或 GKE     | 掛載投射的服務帳戶 Token，並將 Codex 指向該檔案。平台會負責輪替該 Token。                                  |
| Microsoft Entra 受控識別 | 執行受信任的主機程序或 sidecar，向 Azure IMDS 要求 Token，並在 Token 到期前更換檔案。                |
| AWS 對外身分聯盟 | 執行受信任的主機程序，呼叫區域 STS `GetWebIdentityToken`，並在 Token 到期前更換檔案。                   |
| Google Cloud                     | 執行受信任的主機程序，向中繼資料伺服器要求身分 Token，並在 Token 到期前更換檔案。        |
| Oracle Cloud Infrastructure      | 執行受信任的主機程序，透過執行個體主體要求 IDCS 存取 Token，並在 Token 到期前更換檔案。 |
| GitHub Actions                   | 要求作業的 OIDC Token，將其寫入受保護的檔案，並在後續交換前要求新的 Token。                    |
| SPIFFE                           | 使用 SPIFFE Workload API 或經核准的輔助程式，將目前有效的 JWT-SVID 寫入檔案。                                      |
| 自訂 OIDC 提供者             | 使用簽發者的工作負載流程取得 JWT，並在 JWT 到期前更新受保護的檔案。                            |

請依照提供者的指南設定 Token 簽發方式，並檢查 Token 範例：

- [Microsoft Azure](/api/docs/guides/workload-identity-federation/microsoft-azure)
- [AWS](/api/docs/guides/workload-identity-federation/aws)
- [Google Cloud](/api/docs/guides/workload-identity-federation/google-cloud)
- [Oracle Cloud Infrastructure](/api/docs/guides/workload-identity-federation/oracle-cloud)
- [GitHub Actions](/api/docs/guides/workload-identity-federation/github-actions)
- [Kubernetes](/api/docs/guides/workload-identity-federation/kubernetes)
- [SPIFFE](/api/docs/guides/workload-identity-federation/spiffe)

在本機解碼 Token 範例，並記錄其 `iss`、`aud`、`sub`，以及其他
您準備信任的宣告。解碼不會驗證簽章。切勿將正式環境的 Token
貼到網站或寫入記錄檔。

## 連接工作負載

管理員會在啟動 Codex 前建立提供者和聯盟規則。

1. 在 OpenAI 管理入口網站中開啟[工作負載身分](https://admin.openai.com/workload-identity)，
   然後選取 **連接工作負載**。
2. 沿用已為 Codex 設定的提供者，或建立新的提供者。提供者預設組態會自動填入 GitHub Actions、Microsoft Entra ID、Google Cloud、AWS、Kubernetes、SPIFFE 和自訂 OIDC 提供者的常用設定。
3. 選取 **Codex** ，以及工作負載可使用的受管理工作區。
4. 新增可識別工作負載的最嚴格條件。比對主體、精確宣告、CEL 條件，或上述條件的組合。新增可接受的對象，以限制規則接受的 Token。每個已設定的比對條件都必須符合。
5. 將規則對應到一名現有的 ChatGPT 使用者或一個服務帳戶，或在設定期間建立其中之一。
6. 審查提供者、條件、工作區、主體、存取範圍及存取
   Token 的有效期間。選取 **連接工作負載**，然後選取 **下載設定**。

下載的檔案包含非機密的聯盟規則 ID，以及 Codex 讀取身分 Token 的檔案路徑。其中不含任何憑證。

如要將設定流程自動化，請使用[工作負載身分 Admin
API](/api/docs/guides/workload-identity-federation/admin-api)。如需了解比對器的
運作方式及範例，請參閱[聯盟規則
參考資料](/api/docs/guides/workload-identity-federation/federation-rules)。

## 設定 Codex 程序

啟動 Codex 的程序必須具備以下兩個工作負載身分變數：

```bash

`OPENAI_FEDERATION_RULE_ID` 並非機密資訊，但 Token 檔案屬於機密。請使用專用目錄中的絕對
路徑，例如 `/var/run/secrets/openai.com`；該目錄必須由
工作負載帳戶擁有，且權限模式須為 `0700`。只有受信任的主機程序
才應寫入該目錄。請勿將該目錄置於程式碼庫或其他
Codex 工具可存取的路徑中。請勿讓憑證出現在記錄檔、Shell 歷史紀錄或建置產物中。

### 新增稽核歸屬資訊

當多個執行階段執行個體共用同一條聯盟規則時，您可以在
Token 簽發稽核事件中識別各個執行個體。將選用的
`OPENAI_WORKLOAD_IDENTITY_CONTEXT` 變數設定為以字串
形式編碼的 JSON 物件：

```bash

  "instance_id": "runner-42",
  "display_name": "payments-prod",
  "labels": {
    "environment": "production",
    "region": "us-west-2"
  }
}'

此物件必須包含 `instance_id`，也可以包含 `display_name`，以及最多
八個標籤。編碼後的物件大小最多為 1,024 位元組。`instance_id` 與
`display_name` 的長度最多為 128 個字元。標籤鍵最多為 64 個
字元，標籤值最多為 256 個字元。

識別碼必須以 ASCII 字母或數字開頭，後續字元可包含
字母、數字、`.`、`_`、`:`、`/`、`@` 和 `-`。標籤鍵支援字母、
數字、`.`、`_` 和 `-`。

OpenAI 會將此上下文視為由用戶端回報的稽核歸屬資訊，而非經過驗證的工作負載身分。這些資訊不會影響身分驗證、授權、規則比對、存取範圍、速率限制、撤銷、功能閘門或指標。請勿在其中放入憑證、機密資訊、個人資料、提示詞、模型輸出或其他客戶內容。

當上下文有效時，OpenAI 會產生穩定的歸屬 ID，範圍限定於租用戶、
提供者、聯合規則和 `instance_id`。為標示歸屬，存取權杖
包含該 ID，但不包含上下文。Token 核發成功的稽核事件
則包含該 ID 和標準化後的上下文。若上下文超出限制或
不符合此結構描述，交換便會失敗並傳回 `invalid_grant`。

Codex 會在處理程序啟動時讀取上下文，不會將上下文、規則 ID 或 Token 檔案路徑傳遞給由模型控制的 Shell、掛勾或 MCP 伺服器。變更上下文後，請重新啟動 Codex。

### 保護並輪替 Token 檔案

在受管理的 Linux、macOS 和 WSL 部署中，請在受管理需求中將整個 Token 目錄加入
[`permissions.filesystem.deny_read`](/zh-Hant/codex/enterprise/managed-configuration#enforce-deny-read-requirements)
設定：

```toml
[permissions.filesystem]
deny_read = ["/var/run/secrets/openai.com"]

這可防止模型控制的指令讀取目前使用的 Token 或暫時替換的 Token，同時仍允許 Codex 主機處理程序使用該 Token 進行交換。針對投影 Token 磁碟區，請禁止讀取整個 Token 掛載點，以及位於其外部的任何後端路徑或解析後的目標路徑。僅靠檔案權限模式及清除環境變數，無法防止以相同使用者身分執行的其他處理程序取得憑證。在原生 Windows 上，請使用上述提升權限的沙盒。

若 Token 來源不會投影出檔案，請讓可信任的主機處理程序在受保護目錄中寫入每個替換檔案，再將其重新命名為目標檔案。原子性重新命名可避免 Codex 讀取到不完整的 Token。舉例來說，請依照提供者的 Token 指令調整這段由主機管理的更新指令碼。執行指令碼前，請先建立目錄：

```bash
set -eu
TOKEN_DIR="/var/run/secrets/openai.com"
TOKEN_FILE="$TOKEN_DIR/identity-token"
umask 077
TOKEN_TEMP="$(mktemp "$TOKEN_DIR/.identity-token.XXXXXX")"
trap 'rm -f -- "$TOKEN_TEMP"' EXIT
trap 'exit 1' HUP INT TERM
your-identity-provider-command > "$TOKEN_TEMP"
test -s "$TOKEN_TEMP"
mv -f -- "$TOKEN_TEMP" "$TOKEN_FILE"

請在 Codex 可控制的任何 Shell 或工具之外執行更新處理程序。更新及清理期間，
請持續套用禁止讀取設定。即使強制停止後留下暫存檔，
該檔案也必須留在禁止讀取的
目錄中。請勿將工作負載身分設定放入 `config.toml`。

## 驗證連線

載入已下載的環境設定，並檢查選取的身分驗證方法：

```bash
. ./workload-identity-idpm_example.env
codex login status

在 PowerShell 中：

```powershell
$env:OPENAI_FEDERATION_RULE_ID = "idpm_..."
$env:OPENAI_IDENTITY_TOKEN_FILE = "C:\run\openai\identity-token"
codex login status

檢查成功時會輸出 `Logged in using workload identity`。這表示
Codex 已透過設定的聯合規則交換 Token。此指令
不會輸出解析出的工作區、身分主體或規則。啟動工作負載之前，
請先在管理入口網站中確認這些值。若 Codex 回報其他
身分驗證方法，表示兩個必要的 WIF 變數未傳入該處理程序。

如果提供者使用 **防止斷言重放** ，且斷言含有 `jti`
宣告，這項檢查會耗用該 `jti`。啟動其他 Codex 處理程序前，
請寫入包含全新 `jti` 的新核發斷言。

在相同環境中執行一個簡單的請求：

```bash
codex exec "Reply with only: workload identity is working"

Codex 會交換上游 Token，並將 OpenAI 存取權杖保留在記憶體中。
它不會將任何一項憑證寫入 `auth.json`、系統金鑰圈或
`config.toml`。

## 讓 Token 保持最新狀態

請在上游 Token 到期前更新身分 Token 檔案。當 Codex 需要另一個 OpenAI 存取權杖時，會重新讀取該檔案。OpenAI Token 會在上游 Token 到期或達到聯合規則設定的有效期限時失效，以較早者為準，且有效時間最長為一小時。

管理員啟用重放防護後，每個上游 JWT 都必須具有
唯一的 `jti`。每次交換前，請寫入包含全新 `jti` 的新核發斷言，
包括長時間執行的處理程序進行更新時。未包含
`jti` 的斷言不受重放防護機制保護。

Codex 會在每個主機處理程序內共用一個記憶體中的交換工作階段。該處理程序中的並行請求會重複使用有效的 OpenAI 存取權杖，並在該權杖到期時共用同一次更新。不同的處理程序會分別進行交換，因此必須使用提供者允許其使用的斷言。

## 憑證優先順序

兩個必要的工作負載身分變數優先於所有其他憑證來源：

1. 只要存在 `OPENAI_FEDERATION_RULE_ID` 或
`OPENAI_IDENTITY_TOKEN_FILE` 其中之一，Codex 就會選擇工作負載身分。
2. 若只存在一個必要變數，Codex 會傳回錯誤，不會改用 API 金鑰、存取權杖或已儲存的登入資訊。
3. 單獨設定 `OPENAI_WORKLOAD_IDENTITY_CONTEXT` 不會選擇工作負載身分。
4. 若兩個必要的 WIF 變數皆不存在，Codex 會套用該使用介面的
   一般憑證規則。對於允許 API 金鑰
   身分驗證的使用介面，`CODEX_API_KEY` 在 `codex exec`、
`codex review`、TypeScript SDK 和 `codex exec-server --remote` 中具有優先權。其他
   使用介面可使用 `CODEX_ACCESS_TOKEN` 或已儲存的登入資訊。

SDK 的 `apiKey` 選項會轉換為 `CODEX_API_KEY`，但只要存在任一必要的 WIF 變數，
WIF 仍具有優先權。使用 WIF 時，請省略此選項，
避免工作負載攜帶未使用的長期有效憑證。

若要在不中斷服務的情況下遷移現有工作負載，請在目前憑證仍可使用時設定 WIF。使用兩個必要的 WIF 變數啟動新的處理程序；即使舊憑證仍然存在，WIF 仍具有優先權。工作負載成功使用 WIF 後，請從其執行階段和機密存放區移除舊憑證，然後將其撤銷。在撤銷之前，您可移除兩個必要的 WIF 變數並啟動新的處理程序，以回復至原設定。

## 支援的 Codex 使用介面

請在執行 Codex 處理程序的機器上設定工作負載身分。

| 使用介面                                         | 支援情形與主機界限                                                                               |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 互動式 `codex`、`resume` 和 `fork`       | 支援。請在已設定的環境中啟動 CLI。                                                 |
| `codex exec`、`exec resume` 和 `codex review` | 支援。只要存在任一必要的 WIF 變數，WIF 就具有優先權。                                      |
| TypeScript SDK                                  | 支援。父處理程序會提供必要的 WIF 變數，以及任何選用的歸屬上下文。 |
| `codex app-server`                              | 支援。請在 app-server 主機上設定 WIF，而不是在遠端用戶端上設定。                                |
| `codex exec-server --remote`                    | 支援遠端環境登錄服務的身分驗證。請在 exec-server 主機上設定 WIF。 |
| 本機 exec-server 的處理程序操作            | 不使用 WIF 身分驗證，而是透過本機 exec-server 通訊協定執行。                         |
| `codex mcp-server`                              | 不支援。                                                                                          |

遠端 app-server 和 exec-server 用戶端絕不會透過各自的通訊協定傳送上游身分 Token。

## 變更或移除存取權

變更規則的主體、對象、宣告、CEL 條件、授權範圍或 Token 有效期限後，這些變更將套用至新的交換。在變更之前核發的 Token 可能仍會保持有效，直到有效期限屆滿。

停用提供者或規則即可立即中止存取。停用後，系統會封鎖新的交換，並撤銷已透過該資源核發的 OpenAI 存取權杖。封存對存取權具有相同影響，且無法復原。變更提供者的信任設定時，也會在新的信任設定生效前撤銷已核發的 Token。

## 稽核變更

建立、更新及封存提供者和聯合規則時，皆會產生稽核
事件。請參閱 [Compliance API 與稽核事件
指南](/zh-Hant/codex/enterprise/compliance-api)，匯出工作區
支援的事件。將這些事件與身分提供者的核發紀錄建立關聯，且切勿在任一系統中
記錄上游斷言或 OpenAI 存取權杖。

當處理程序提供 `OPENAI_WORKLOAD_IDENTITY_CONTEXT` 時，成功的
Token 核發稽核事件也會包含上述穩定的歸屬 ID 與
標準化後的上下文。

## 疑難排解

| 問題現象                                                               | 檢查項目                                                                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Codex 回報工作負載身分組態不完整              | 請在同一個處理程序中設定兩個必要變數，並使用 Token 檔案的絕對路徑。                               |
| Codex 回報其登入政策不允許使用工作負載身分 | 請在生效的政策中允許 ChatGPT 身分驗證，並將規則指定的工作區納入允許的工作區清單。 |
| Codex 回報使用另一項憑證                                      | 將兩個必要的 WIF 變數載入 Codex 處理程序，接著啟動新的處理程序，並重新執行 `codex login status`。  |
| OpenAI 拒絕工作負載上下文                                       | 請檢查其 JSON 結構、大小、允許的字元及欄位限制，並移除敏感內容或客戶內容。            |
| OpenAI 拒絕 Token                                              | 請依照提供者組態，比對 `iss`、`aud`、到期時間、簽署金鑰及斷言有效期限。               |
| 規則不相符                                               | 請確認用戶端使用預期的規則 ID，且所有主體、對象、精確宣告與 CEL 檢查皆通過。  |
| OpenAI 拒絕身分主體                                          | 確認使用者或服務帳戶處於啟用狀態，且為所選工作區的有效成員。                   |
| OpenAI 拒絕重複使用的判斷提示                                   | 取得包含新 `jti` 的新 JWT；請勿使用受重放保護的同一份判斷提示重試。                                  |
| 長時間執行的程序停止更新                               | 確認主機上的更新程序仍會在到期前更換 Token 檔案。                                  |

如需提供者驗證、限制和 CEL 的詳細資訊，請參閱[聯盟規則
參考資料](/api/docs/guides/workload-identity-federation/federation-rules)。
