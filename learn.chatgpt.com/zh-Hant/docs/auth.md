<!-- source: https://learn.chatgpt.com/zh-Hant/docs/auth -->

## OpenAI 身分驗證

<a id="sign-in-with-chatgpt"></a>

使用 OpenAI 模型時，Codex 支援兩種登入方式：

- 使用 ChatGPT 登入，透過訂閱方案取得存取權
- 使用 API 金鑰登入，依使用量計費

ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能都支援這兩種登入
方式來執行本機工作。Codex 雲端則必須使用 ChatGPT 登入。

您的登入方式也決定適用哪些管理控制措施與資料處理政策。

- 使用 ChatGPT 登入時，Codex 的使用會遵循 ChatGPT 工作區
權限、角色型存取控制 (RBAC)，以及 ChatGPT Enterprise 的
資料保留與資料駐留設定。
- 使用 API 金鑰時，則會改為遵循 API 組織的資料保留與
資料共用設定。

對於受管理的工作區，身分驗證只是存取控制的其中一層。工作區
成員資格與佈建決定誰能登入，而席位和
工作區角色則決定他們可使用哪些產品介面與功能。
若要在 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能中執行本機工作，
權限設定檔會限制智慧體能在裝置上執行的動作。請參閱
[群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
及 [角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
，以規劃這些控制措施。

### 使用 ChatGPT 登入

當您從 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能使用 ChatGPT 登入時，登入流程會開啟瀏覽器視窗。登入後，瀏覽器會將您的認證資料傳回 Codex。

### ChatGPT 網頁版

開啟 [ChatGPT](https://chatgpt.com) 並登入，然後選擇您
要使用的工作區。ChatGPT 網頁版會將已驗證的工作階段保留在瀏覽器中。

#### ChatGPT 桌面版應用程式

在未登入畫面上，選取 **繼續登入**，然後完成
瀏覽器流程。

#### Codex CLI

執行 `codex login`，然後完成瀏覽器流程。若沒有有效的工作階段，這是預設的
身分驗證方式。

#### IDE 擴充功能

在未登入畫面上，選取 **使用 ChatGPT 登入**，然後完成
瀏覽器流程。

<a id="sign-in-with-an-api-key"></a>

### 使用 API 金鑰登入

您也可以使用 API 金鑰登入 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能。請從 [OpenAI 儀表板](https://platform.openai.com/api-keys)取得 API 金鑰。

#### ChatGPT 桌面版應用程式

在未登入畫面上，選取 **使用其他方式登入**、輸入金鑰，然後
選取 **繼續**。

#### Codex CLI

透過 stdin 將金鑰以管線方式傳給 `codex login`：

```shell
printenv OPENAI_API_KEY | codex login --with-api-key

#### IDE 擴充功能

在未登入畫面上，選取 **使用 API 金鑰**、輸入金鑰，然後選取
**確定**。

OpenAI 會透過您的 OpenAI Platform 帳戶，依標準 API 費率計收 API 金鑰用量。請參閱 [API 定價頁面](https://openai.com/api/pricing/)。

API 金鑰身分驗證支援本機 Codex 工作流程，但部分
依賴 ChatGPT 工作區存取權或雲端服務的功能會受限或無法使用。
如需比較各方案的支援情況，請參閱
[功能可用性](/zh-Hant/codex/pricing#feature-availability)。

對於 Codex CLI，以及 ChatGPT 桌面版應用程式中的 Codex，API 金鑰身分驗證
可讓您存取受支援且由 OpenAI 精選的外掛程式。部分外掛程式
無法使用，因為其連線流程需要目前不受支援的 OAuth
功能。請參閱 [使用外掛程式](/zh-Hant/codex/plugins#api-key-availability)。

使用 API 金鑰登入時，Codex 會採用標準 API 定價，而不會使用
ChatGPT 方案內含的點數。

API 金鑰身分驗證可用於程式化的 Codex CLI 工作流程，例如 CI/CD
作業。請勿在不受信任或公開的環境中提供 Codex 執行功能。

### 檢查身分驗證狀態或登出

開啟個人資料選單，確認目前使用的帳戶和工作區。若要結束該瀏覽器中的
ChatGPT 網頁版工作階段，請選取 **登出**。

開啟個人資料選單，查看目前的帳戶或 API 金鑰狀態。選取
**登出** 即可清除目前的認證資料。

執行 `codex login status` 以查看目前使用的身分驗證方式。若使用已儲存的
身分驗證資料，請執行 `codex logout` 以清除目前的認證資料。當
處理程序選用工作負載身分時，Codex 會拒絕 `codex login` 和
`codex logout`，因為身分驗證由處理程序環境控制。

開啟個人資料選單，查看目前的帳戶或 API 金鑰狀態。選取
**登出** 即可清除目前的認證資料。

### 使用 Codex 存取權杖進行企業自動化

在 ChatGPT Enterprise 工作區中，管理員可授予存取權杖
權限，讓獲准的成員建立 Codex 存取權杖，用於受信任、
非互動式的 Codex 本機工作流程。若自動化作業
不透過瀏覽器登入，但需要存取 ChatGPT 工作區、使用由 ChatGPT 管理的 Codex 使用資格，或
套用企業工作區控制，請使用存取權杖。

存取權杖適用於受信任的指令碼、排程器及私有 CI
執行器。一般 OpenAI API 呼叫則應繼續使用 Platform API 金鑰。

如需設定步驟，以及權限、輪替與撤銷的相關指引，請參閱
[存取權杖](/zh-Hant/codex/enterprise/access-tokens)。

如果您的雲端平台、CI 系統或叢集已簽發短效
工作負載 Token，請使用
[工作負載身分聯盟](/zh-Hant/codex/enterprise/workload-identity)
，而不要儲存 OpenAI 認證資料。

如果您的環境已提供 Codex 存取權杖，請透過管線將它傳給 CLI：

```shell
printenv CODEX_ACCESS_TOKEN | codex login --with-access-token

## 保護您的 Codex 雲端帳戶

Codex 雲端會直接與您的程式碼庫互動，因此需要比許多其他 ChatGPT 功能更嚴密的安全防護。請啟用多因素身分驗證（MFA）。

若使用社群登入供應商（Google、Microsoft、Apple），則不必在 ChatGPT 帳戶上啟用 MFA，但可透過該社群登入供應商設定 MFA。

如需設定指示，請參閱：

- [Google](https://support.google.com/accounts/answer/185839)
- [Microsoft](https://support.microsoft.com/en-us/topic/what-is-multifactor-authentication-e5e39437-121c-be60-d123-eda06bddf661)
- [Apple](https://support.apple.com/en-us/102660)

若透過單一登入（SSO）存取 ChatGPT，您組織的 SSO 管理員應為所有使用者強制啟用 MFA。

若使用電子郵件地址和密碼登入，必須先為帳戶設定 MFA，才能存取 Codex 雲端。

若您的帳戶支援多種登入方式，且其中一種是電子郵件地址和密碼，即使您使用其他方式登入，也必須先設定 MFA，才能存取 Codex。

<a id="login-caching"></a>

## 登入快取

當您使用 ChatGPT 或 API 金鑰登入 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能時，登入資料會儲存至快取並重複使用。CLI 和擴充功能共用同一份快取登入資料。若從任一端登出，下次啟動 CLI 或擴充功能時，就必須重新登入。

Codex 會將登入資料快取於本機的純文字檔案 `~/.codex/auth.json`，或作業系統專用的認證資料存放區中。

針對使用 ChatGPT 登入的工作階段，Codex 會在使用期間於 Token 到期前自動更新 Token，因此使用中的工作階段通常可持續進行，不需要再次透過瀏覽器登入。

<a id="credential-storage"></a>
<a id="enforce-a-login-method-or-workspace"></a>

## 認證資料儲存

使用 `cli_auth_credentials_store` 控制 Codex CLI 儲存快取認證資料的位置：

```toml
# file | keyring | auto
cli_auth_credentials_store = "keyring"

- `file` 會將認證資料儲存在 `auth.json` 中，該檔案位於 `CODEX_HOME` 下（預設為 `~/.codex`）。
- `keyring` 會將認證資料儲存在作業系統的認證資料存放區中。
- `auto` 會在可用時使用作業系統的認證資料存放區，否則改用 `auth.json`。

請參閱[組態參考資料](/zh-Hant/codex/config-file/config-reference)，瞭解完整的
`config.toml` 結構描述。

  若使用檔案型儲存空間，請像保護密碼一樣保護 `~/.codex/auth.json`，因為其中
  包含存取權杖。請勿提交這個檔案、將其貼到工單中，或在
  對話中分享。

## 強制使用特定登入方式或工作區

在受管理的環境中，管理員可限制使用者可採用的身分驗證方式：

```toml
# Only allow ChatGPT login or only allow API key login.
forced_login_method = "chatgpt" # or "api"

# When using ChatGPT login, restrict users to a specific workspace.
forced_chatgpt_workspace_id = "00000000-0000-0000-0000-000000000000"

如果目前的認證資料不符合設定的限制，Codex 會將使用者登出並結束執行。

這些設定通常透過受管理的設定套用，而不是由個別使用者分別設定。請參閱 [受管理的設定](/zh-Hant/codex/enterprise/managed-configuration)。

## 登入診斷

直接執行 `codex login` 時，會將專用的 `codex-login.log` 檔案寫入
您設定的記錄目錄。當您需要偵錯瀏覽器登入或
裝置代碼驗證失敗，或支援人員要求提供登入專用記錄時，請使用此檔案。

## 自訂 CA 憑證套件

若您的網路使用企業 TLS 代理伺服器或私有根 CA，請在登入前設定
`CODEX_CA_CERTIFICATE`，使其指向 PEM 憑證套件。若未設定
`CODEX_CA_CERTIFICATE`，Codex 會改用 `SSL_CERT_FILE`。這些
自訂 CA 設定同樣適用於登入、一般 HTTPS 要求及安全 WebSocket
連線。

```shell

codex login

## 在無頭裝置上登入

如果您使用 Codex CLI 登入 ChatGPT，以下情況可能會讓瀏覽器式登入 UI 無法運作：

- 您正在遠端或無頭環境中執行 CLI。
- 您的本機網路組態封鎖了 localhost 回呼；您登入後，Codex 會使用這項回呼將 OAuth Token 傳回 CLI。

在這些情況下，建議使用裝置代碼身分驗證（Beta 版）。在互動式登入 UI 中，選擇 **使用裝置代碼登入**，或直接執行 `codex login --device-auth`。如果您的環境無法使用裝置代碼身分驗證，請改用其中一種備用方法。

### 建議使用：裝置代碼身分驗證（Beta 版）

1. 在 ChatGPT 安全性設定（個人帳戶）或 ChatGPT 工作區權限（工作區管理員）中啟用裝置代碼登入。
2. 在執行 Codex 的終端中，選擇以下其中一種方式：
   - 在互動式登入 UI 中，選取 **使用裝置代碼登入**。
   - 執行 `codex login --device-auth`。
3. 在瀏覽器中開啟連結並登入，然後輸入一次性代碼。

如果您的環境無法使用裝置代碼登入，請採用下列其中一種
備用方法。

### 備用方法：在本機完成身分驗證並複製登入快取

如果您能在有瀏覽器的機器上完成登入流程，就可以將快取的認證資料複製到無頭機器。

1. 在可使用瀏覽器登入流程的機器上，執行 `codex login`。
2. 確認登入快取檔案 `~/.codex/auth.json` 已存在。
3. 將 `~/.codex/auth.json` 複製到無頭機器上的 `~/.codex/auth.json`。

請像保護密碼一樣保護 `~/.codex/auth.json`，因為其中包含存取權杖。請勿提交這個檔案、將其貼到工單中，或在對話中分享。

如果您的作業系統將認證資料儲存在認證資料存放區，而非 `~/.codex/auth.json`，此方法可能不適用。如需設定檔案型儲存空間，請參閱
[認證資料儲存](/zh-Hant/codex/auth#credential-storage)。

透過 SSH 複製到遠端機器：

```shell
ssh user@remote 'mkdir -p ~/.codex'
scp ~/.codex/auth.json user@remote:~/.codex/auth.json

或者，使用不需 `scp` 的單行指令：

```shell
ssh user@remote 'mkdir -p ~/.codex && cat > ~/.codex/auth.json' < ~/.codex/auth.json

複製到 Docker 容器：

```shell
# Replace MY_CONTAINER with the name or ID of your container.
CONTAINER_HOME=$(docker exec MY_CONTAINER printenv HOME)
docker exec MY_CONTAINER mkdir -p "$CONTAINER_HOME/.codex"
docker cp ~/.codex/auth.json MY_CONTAINER:"$CONTAINER_HOME/.codex/auth.json"

如需瞭解如何在受信任的 CI/CD 執行器上使用此模式的進階版本，請參閱
[在 CI/CD 中維護 Codex 帳戶身分驗證（進階）](/codex/auth/ci-cd-auth)。
該指南說明如何讓 Codex 在正常執行期間重新整理 `auth.json`，
並保留更新後的檔案，供下一項作業使用。API 金鑰仍是自動化作業
建議採用的預設方式。

### 備用方法：透過 SSH 轉送 localhost 回呼

如果您能在本機與遠端主機之間轉送連接埠，即可透過通道轉送 Codex 的本機回呼伺服器（預設為 `localhost:1455`），使用標準的瀏覽器登入流程。

1. 從本機啟動連接埠轉送：

```shell
ssh -L 1455:localhost:1455 user@remote

2. 在該 SSH 工作階段中執行 `codex login`，然後在本機開啟輸出的位址並依照指示操作。

## 其他模型供應商

在組態檔案中定義 [自訂模型供應商](/zh-Hant/codex/config-file/config-advanced#custom-model-providers) 時，可以選擇以下其中一種身分驗證方式：

- **OpenAI 身分驗證**：設定 `requires_openai_auth = true` 以使用 OpenAI 身分驗證。接著，您可以使用 ChatGPT 或 API 金鑰登入。若透過 LLM 代理伺服器存取 OpenAI 模型，這項設定很實用。當 `requires_openai_auth = true` 時，Codex 會忽略 `env_key`。
- **環境變數身分驗證**：設定 `env_key = "<ENV_VARIABLE_NAME>"`，以使用名稱為 `<ENV_VARIABLE_NAME>` 的本機環境變數所提供的供應商專用 API 金鑰。
- **不使用身分驗證**：如果未設定 `requires_openai_auth`（或將其設為 `false`），且也未設定 `env_key`，Codex 會假設該供應商不需要身分驗證。這對本機模型很實用。
