<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/access-tokens -->

Codex 存取權杖是權限範圍限於 Codex 的 ChatGPT 工作區憑證。這類權杖讓受信任的非互動式本機工作流程，包括 Codex CLI 與以 App Server 為基礎的自動化流程，使用 ChatGPT 工作區身分進行身分驗證。當指令碼、排程作業或 CI 執行器需要重複存取本機 Codex 時，請使用這類權杖。

  Codex 存取權杖目前支援 ChatGPT Business 與
ChatGPT Enterprise 工作區。

請在 ChatGPT 管理控制台的[存取權杖](https://chatgpt.com/admin/access-tokens)頁面建立個人存取權杖。每個權杖都屬於其建立者及該使用者的 ChatGPT 工作區。權杖可作為程式化本機工作流程的智慧體身分。若要瞭解從專用非人員工作區身分的詳細資料頁面建立的權杖，請參閱[服務帳戶](/zh-Hant/codex/enterprise/service-accounts)。

  如果平台 API 金鑰適用於您的自動化流程，請繼續使用 API 金鑰進行身分驗證。當受信任的本機工作流程明確需要 ChatGPT 工作區存取權、由工作區管理的權益或企業控制措施時，請使用 Codex 存取權杖。

  需要從自己的系統觸發已發布的 ChatGPT 工作區智慧體嗎？這類
  工作流程需要 **工作區智慧體** 存取權。僅限 Codex 的權杖無法
  用於工作區智慧體觸發呼叫的身分驗證。如果權杖對話框提供
**範圍**選項，觸發智慧體時請選取 **工作區智慧體** ，而
  執行 Codex 自動化時請選取 **Codex** 。只有在工作流程需要每一項範圍時，
  才授予多個範圍。請參閱[使用工作區智慧體存取權杖
  進行身分驗證](/workspace-agents/authentication)。

## 存取權杖的運作方式

當 Codex CLI 或 App Server 用戶端需要在無須使用者完成瀏覽器登入的情況下執行時，請使用存取權杖。權杖代表建立它的 ChatGPT 工作區使用者，因此執行作業可使用該使用者的存取權，並顯示在工作區治理資料中。

用戶端會在執行作業開始時檢查權杖，並將該次執行與工作區身分建立關聯。請像處理其他自動化機密一樣處理權杖：將其儲存在機密管理工具中，避免寫入紀錄，並依組織政策輪替。

存取權杖適用於：

- 由受信任的自動化流程執行的 `codex exec` 作業。
- 需要以非互動方式重複執行 Codex CLI 的本機指令碼。
- 以 App Server 為基礎的受信任自動化流程。
- 將使用量與 ChatGPT 工作區使用者而非 API 組織金鑰建立關聯的企業工作流程。

應避免的主要風險：

- **機密外洩：** 任何取得權杖的人都能以權杖建立者的身分，透過 Codex CLI 或 App Server 用戶端啟動本機執行作業。請將權杖儲存在機密管理工具中，避免寫入紀錄，並依組織政策輪替。
- **執行器的可信度：** 公開 CI、來自分支程式碼庫的 Pull Request 或共用機器，可能讓工作區外的人員取得權杖。存取權杖只能用於受信任的執行器。
- **共用身分：** 如果彼此無關的團隊共用同一人的權杖，擁有權和稽核軌跡會變得較不明確。請為特定工作流程的擁有者建立權杖。
- **過時的憑證：** 工作流程變更後，長效權杖仍可能保持有效。請優先使用有時限的權杖，並撤銷不再使用的權杖。
- **範圍或憑證類型錯誤：** Codex 自動化需要 Codex 存取權，
  觸發工作區智慧體需要工作區智慧體存取權，而一般 OpenAI API 呼叫
  需要平台 API 金鑰。如果畫面顯示 **範圍** ，請只授予
  工作流程所需的權限。

## 啟用存取權杖建立功能

請使用工作區設定中的存取權杖權限，為獲准成員開啟存取權杖建立功能。

存取權杖權限控制權杖的建立。這項權限不會授予 ChatGPT 桌面版應用程式、Codex CLI 或 IDE 擴充功能的存取權，也不會變更成員的席位類型、內建工作區角色或本機執行階段權限設定檔。透過權杖進行身分驗證的 Codex CLI 和 App Server 工作流程，也需要使用者具備本機 Codex 權限。

若要瞭解這些控制項之間的關係，請參閱
[角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)。

  
    
  

1. 請工作區擁有者開啟
[工作區設定 \> 權限與角色](https://chatgpt.com/admin/permissions)。
2. 如果畫面顯示 **存取權杖** 區段，請啟用 **允許使用者建立
   個人存取權杖**。如果沒有該區段，請啟用 **允許
   成員使用 Codex 存取權杖** ，此設定位於 **Codex 與 Work 本機** 或
**Codex 本機**區段。
3. 為工作流程擁有者啟用對應的本機 Codex 權限：
在 **Codex 與 Work 本機**區段中啟用**允許成員在本機使用 Codex 與 Work** ，
   或在 **Codex 本機**區段中啟用 **允許成員在本機使用 Codex** 。若 **Work
   本機** 有獨立區段，其中的 **在本機使用 Work** 控制 Work 的使用權限，
   使用 Codex 權杖不需要啟用此設定。

只允許瞭解權杖儲存位置、預定使用權杖的自動化流程及輪替排程的人員或服務擁有者建立存取權杖。

停用本機 Codex 權限會暫停受影響成員所擁有的有效 Codex 權杖，但不會撤銷這些權杖。恢復本機 Codex 存取權後，這些權杖會重新啟用。如果需要永久終止存取權，請撤銷權杖。

## 設定存取權杖有效期限上限

工作區擁有者可設定成員建立新存取權杖時
能選擇的最長有效期限。請開啟
[工作區設定 \> 權限與角色](https://chatgpt.com/admin/permissions)。
如果畫面顯示 **存取權杖** 區段，請在該處設定 **存取權杖有效期限上限**。
否則，請在 **Codex 與 Work 本機** 或
**Codex 本機**區段中尋找此設定。

  
    
  

此上限適用於新建立的存取權杖。現有權杖會保留目前的有效期限。

## 建立存取權杖

在存取權杖頁面為權杖命名，檢視可用的產品範圍，並選擇適當的有效期限。

1. 前往[存取權杖](https://chatgpt.com/admin/access-tokens)頁面。
2. 選取 **建立**。

  
    
  

3. 輸入能描述用途的名稱，例如 `release-ci` 或 `nightly-docs-check`。

  
    
  

4. 如果對話框顯示 **範圍**，請選取 **Codex**。只有在同一個工作流程也需要觸發工作區智慧體時，才選取 **工作區
   智慧體** 。
   如果對話框沒有範圍選擇器，建立的權杖就僅限 Codex 使用。
5. 請選擇有限的有效期限，例如 7、30、60 或 90 天。設有權限範圍的
   個人存取權杖必須設有到期日。早期僅供 Codex 使用的對話框
   可能提供 **永不到期**選項；除非組織
   核准使用此選項，並依既定排程輪替權杖，否則請避免選取。
6. 選取 **建立**。
7. 請立即複製產生的存取權杖。關閉對話框後，就無法再次查看。
8. 將權杖儲存在機密管理工具或 CI 機密儲存區中。

自訂有效期限最短為一天。已撤銷或已到期的權杖無法用來啟動需經身分驗證的新執行作業。

## 搭配 Codex CLI 使用存取權杖

如果權杖建立對話框列出了所需的 Codex CLI 版本，請先將 CLI 更新至該版本或更新版本，再使用權杖。

對於暫時性自動化流程，請將權杖儲存在 `CODEX_ACCESS_TOKEN` 中，並照常執行 Codex CLI：

```bash

codex exec --json "review this repository and summarize the top risks"

若要保留本機登入狀態，請將權杖以管線方式傳入 `codex login --with-access-token`：

```bash
printf '%s' "$CODEX_ACCESS_TOKEN" | codex login --with-access-token
codex exec "summarize the last release diff"

`codex login --with-access-token` 會將智慧體身分憑證儲存在 Codex CLI 身分驗證儲存區中。如果不想在機器上留存憑證，請改用 `CODEX_ACCESS_TOKEN` 環境變數。

`codex app-server` 可透過 `CODEX_ACCESS_TOKEN` 或
以 `codex login --with-access-token` 建立的登入狀態，使用同一組憑證為其
OpenAI 請求進行身分驗證。這組憑證獨立於用戶端與 App Server 之間的
傳輸身分驗證。對於遠端 WebSocket 連線，請設定
另一個持有人權杖或能力權杖，設定方式請參閱
[App Server](/zh-Hant/codex/app-server)；請勿將 Codex 存取權杖重複用作
傳輸權杖。請參閱
[身分驗證與網路環境變數](/zh-Hant/codex/config-file/environment-variables#authentication-and-network)。

## 輪替或撤銷權杖

請以輪替其他自動化機密的方式輪替存取權杖：

1. 建立替換用權杖。
2. 更新執行器、排程器或機密管理工具中的機密。
3. 使用新權杖執行煙霧測試。
4. 在[存取權杖](https://chatgpt.com/admin/access-tokens)頁面撤銷舊權杖。

工作區擁有者和管理員可以從「存取權杖」頁面撤銷工作區內的任何權杖。具有存取權杖權限的成員只能撤銷自己建立的權杖。

## 權限模型

工作區的存取權杖權限控制權杖的建立。依工作區介面配置而定，
本機 Codex 的存取權由 **允許成員在本機使用 Codex 和 Work** （位於
**本機 Codex 和 Work**）或 **允許成員在本機使用 Codex** （位於 **本機
Codex**）控制。如果 **本機 Work** 有獨立的區段，
**在本機使用 Work** 只控制 Work 的存取權，不會授予 Codex 存取權。成員必須同時具備
本機 Codex 存取權及存取權杖權限，才能執行以權杖驗證身分的
Codex 工作流程。成員可以擁有本機 Codex 存取權，卻沒有
建立存取權杖的權限。

| 功能                                                    | 工作區擁有者和管理員                      | 具有存取權杖權限的成員           | 不具存取權杖權限的成員 |
| ------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------- | -------------------------------------- |
| 開啟[存取權杖](https://chatgpt.com/admin/access-tokens) | 是                                              | 是                                           | 否                                     |
| 建立存取權杖                                          | 是，僅限自己的 ChatGPT 工作區身分    | 是，僅限自己的 ChatGPT 工作區身分 | 否                                     |
| 列出存取權杖                                            | 工作區內的權杖清單，包括每個權杖的建立者 | 僅限自己建立的權杖                      | 否                                     |
| 從「存取權杖」頁面撤銷存取權杖              | 工作區內的任何權杖                       | 僅限自己建立的權杖                      | 無法存取該頁面                         |
| 授予或移除存取權杖權限                       | 僅限工作區擁有者                             | 否                                            | 否                                     |
| 管理其他本機用戶端或 Codex 雲端設定             | 是，視工作區管理員權限而定        | 否，除非擁有者授予存取權             | 否                                     |

簡而言之，工作區擁有者和管理員在工作區層級管理存取權限。成員必須具備存取權杖權限，才能建立及管理自己的權杖，但該權限不會授予管理員權限，也不允許存取其他成員的權杖。

## 疑難排解

### 「存取權杖」頁面傳回 404 或禁止存取

請工作區擁有者依目前的介面，確認你的角色具備 **允許使用者
建立個人存取權杖** 或 **允許成員使用 Codex
存取權杖**權限。若要執行以權杖驗證身分的
Codex 工作流程，也請確認已啟用 **允許成員在本機
使用 Codex 和 Work** 或 **允許成員在本機使用 Codex** 。

### `codex login --with-access-token` 失敗

請確認你複製的是產生的存取權杖，而不是瀏覽器工作階段權杖或 API 平台金鑰。也請確認該權杖處於有效狀態、尚未到期，且所屬使用者具備所需的本機 Codex 權限。

## 相關文件

- [身分驗證](/zh-Hant/codex/auth)
- [服務帳戶](/zh-Hant/codex/enterprise/service-accounts)
- [非互動模式](/zh-Hant/codex/non-interactive-mode)
- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [群組與佈建](/zh-Hant/codex/enterprise/groups-and-provisioning)
- [使用者生命週期管理](/zh-Hant/codex/enterprise/user-lifecycle)
- [角色與工作區權限](/zh-Hant/codex/enterprise/roles-and-workspace-permissions)
- [治理](/zh-Hant/codex/enterprise/governance)
