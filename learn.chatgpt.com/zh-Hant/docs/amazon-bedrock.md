<!-- source: https://learn.chatgpt.com/zh-Hant/docs/amazon-bedrock -->

設定本機 ChatGPT Work 和 Codex 介面，以使用可透過 Amazon Bedrock 取得的 OpenAI 模型。在此設定中，本機用戶端會透過 AWS 管理的身分驗證和存取控制，將模型要求傳送至 Bedrock。

## 運作方式

將 Amazon Bedrock 設為本機 ChatGPT Work 或 Codex 介面的模型提供者時，要求不會經過 OpenAI 託管的 Responses API。本機用戶端會將模型要求傳送至 Amazon Bedrock，而 Bedrock 會為受支援的 OpenAI 模型提供與 OpenAI 相容的 Responses API 實作。

  身分驗證採用 AWS 原生機制。使用者會使用 Bedrock API 金鑰或 AWS
  IAM 憑證進行身分驗證。使用此提供者時，不會透過 ChatGPT 登入，也不會使用 `OPENAI_API_KEY`
  進行身分驗證。

## 開始之前

請確認您具備：

- Amazon Bedrock 中受支援 OpenAI 模型的存取權。
- 所選模型可用的 AWS 區域。
- 已為 AWS 帳戶設定 Amazon Bedrock Mantle 路徑的身分驗證。

## 設定提供者

將 Amazon Bedrock Mantle 路徑的 `amazon-bedrock` 模型提供者新增至
`~/.codex/config.toml`。ChatGPT 桌面版應用程式、Codex CLI、IDE 擴充功能和
SDK 都會讀取相同的本機組態層級。您可以選擇是否指定模型。
請視需要明確選取受支援的模型。

```toml
model_provider = "amazon-bedrock"

  本指南涵蓋受支援的 AWS 商業區域中的 Amazon Bedrock Mantle 路徑。本機 ChatGPT Work 和 Codex 介面不支援 AWS GovCloud 區域中的 Bedrock Mantle 端點。

## 身分驗證選項

本機 ChatGPT Work 和 Codex 介面支援兩種 Bedrock 身分驗證路徑。系統會依下列順序檢查：

1. Bedrock API 金鑰。
2. AWS SDK 憑證鏈。

### 選項 1：Bedrock API 金鑰

請在本機用戶端會讀取的環境中設定 Bedrock API 金鑰。使用 API 金鑰進行身分驗證時，必須指定區域。

```shell

### 選項 2：AWS SDK 憑證

若您的組織透過 AWS SDK 憑證鏈管理 Bedrock 存取權，請使用此路徑。本機用戶端可以使用下列標準 AWS SDK 憑證來源：

#### 共用 AWS 組態檔案

設定共用的 AWS `config` 和 `credentials` 檔案：

```shell
aws configure

#### 環境變數

設定標準 AWS SDK 憑證環境變數：

```shell

#### AWS Management Console 憑證

使用 AWS Management Console 憑證登入：

```shell
aws login

#### AWS SSO 或具名設定檔

使用 AWS SSO 登入並選取具名設定檔：

```shell
aws sso login --profile codex-bedrock

#### 聯合身分

若使用企業 SSO 或 OIDC 聯合，請在本機用戶端之外使用
`credential_process` 設定聯合身分，並讓 AWS SDK 解析
憑證。請將瀏覽器登入、Token 交換、快取及更新功能放在
AWS 設定檔的 `credential_process` 輔助程式中。

## 桌面 App 與 IDE 擴充功能

桌面 App 和 IDE 擴充功能可能不會繼承 shell
中的環境變數。請將必要的值寫入 `~/.codex/.env`，再重新啟動應用程式或
擴充功能。

```shell

## 驗證設定

- 在 Codex CLI 中開啟 `/status`，並確認 Codex 使用的是
`amazon-bedrock` 模型提供者。
- 重新啟動 ChatGPT 桌面版應用程式後，選取 Work 或 Codex 並開始新任務。
- 重新啟動 IDE 擴充功能後，開始新的工作階段。
- 確認所選模型可在已設定的 AWS 區域中使用，且 AWS 身分具備該模型的存取權限。

## 支援的模型

使用確切的模型 ID：

```text
openai.gpt-5.6-sol
openai.gpt-5.6-terra
openai.gpt-5.6-luna
openai.gpt-5.5
openai.gpt-5.4

模型可用性會因 AWS 區域而異。選取模型前，請參閱 [各
AWS
區域的模型支援情況](https://docs.aws.amazon.com/bedrock/latest/userguide/models-region-compatibility.html)。

## 功能可用性

此組態支援本機 ChatGPT Work 和 Codex 工作流程。託管的網頁版 ChatGPT Work、Codex 雲端，以及任何仰賴 OpenAI 託管的雲端服務、託管工具或雲端管理探索機制的功能，目前皆無法使用。

  快速模式無法搭配 Amazon Bedrock 使用。快速模式採用優先處理，而 Amazon Bedrock 初期提供的服務僅支援隨需推論。

  

  <div
    id="codex-plan-region-limits"
    className="not-prose mt-3 text-sm text-secondary"
  >
    <sup>\*</sup> 目前僅特定地區提供此功能。請參閱
    各項功能的文件，進一步瞭解地區限制。
  </div>
  <div
    id="codex-plan-plugin-limits"
    className="not-prose mt-1 text-sm text-secondary"
  >
    <sup>†</sup> 不需要 ChatGPT 身分驗證的本機外掛程式套件和 OpenAI 精選外掛程式
    （包括 Codex Security）皆可使用。
    需要 ChatGPT 身分驗證、連接器或雲端託管
    共用功能的外掛程式無法使用。
  </div>

## 疑難排解

如果設定失敗，請檢查下列項目：

- 模型 ID 與受支援模型的 ID 完全相符。
- 已指定提供該模型的 AWS 區域。
- Bedrock API 金鑰或 AWS 憑證有效且未過期。
- AWS 身分具有存取所選 Bedrock 模型的權限。
- `AWS_BEARER_TOKEN_BEDROCK` 並未設為已過期或非預期的金鑰。
- 使用桌面 App 或 IDE 擴充功能時，所需的環境變數
  皆已設定在 `~/.codex/.env` 中。

## 支援範圍

OpenAI 支援團隊可協助處理 ChatGPT Work 和 Codex 用戶端的設定與組態、
本機 CLI、桌面 App 和 IDE 擴充功能的運作情況，
以及本機產品的使用體驗。

若問題涉及 AWS 憑證、IAM 權限、Bedrock 模型存取權、配額、計費、
區域供應情況、Bedrock 請求失敗、AWS 服務日誌或 Bedrock
服務的運作情況，請聯絡客戶的 AWS 管理員或 AWS Support。
