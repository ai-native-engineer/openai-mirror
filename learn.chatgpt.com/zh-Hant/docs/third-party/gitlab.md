<!-- source: https://learn.chatgpt.com/zh-Hant/docs/third-party/gitlab -->

使用 Codex 程式碼審查，為 GitLab 合併請求額外進行一輪
重點明確的審查。Codex 會審查合併請求的程式碼差異、遵循程式碼庫的
指引，並發布著重於重大問題的標準 GitLab 程式碼審查。

GitLab 支援功能目前處於 Beta 測試階段，適用於所有 ChatGPT 方案。Codex
整合功能在 Codex 雲端執行。此 Beta 版不包含桌面 App 中的 GitHub 式
程式碼庫控制項，例如 **建立 Pull Request**。

## 開始之前

請確認您已具備：

- 已連結的 GitLab 帳戶。GitLab.com 需要完成
[標準連線流程](https://help.openai.com/articles/20001486)；
  自行管理的 GitLab 或 Dedicated GitLab 執行個體則需要
[由工作區管理員設定範本](https://help.openai.com/articles/20001487)。
- `AGENTS.md` 檔案，可讓 Codex 遵循程式碼庫專屬的審查
  指引。

## 設定 Codex 程式碼審查

### 設定 GitLab 連線和 Codex 審查身分

使用 GitLab.com 時，請先
[在 ChatGPT 中連結 GitLab](https://help.openai.com/articles/20001486)，再於 Codex 中連結 GitLab 帳戶。
使用自行管理的 GitLab 或 Dedicated GitLab 時，每位審查者都應在
[工作區管理員範本](https://help.openai.com/articles/20001487)
發布後再進行連結。

使用自行管理的 GitLab 或 Dedicated GitLab 時，請開啟 **Codex 雲端** → **設定** →
[**連接器**](https://chatgpt.com/codex/cloud/settings/connectors)。
工作區管理員可以讓 Codex 建立服務帳戶，或儲存現有服務帳戶的
個人存取權杖。

#### 讓 Codex 建立帳戶

在 **Codex 雲端** → **設定** → **連接器** 中，選取自行管理的 GitLab 或
Dedicated GitLab 主機所對應的應用程式 → 選取 **設定服務帳戶** →
**建立服務帳戶**。完成設定的工作區管理員必須擁有
GitLab 執行個體的管理員存取權。選擇 **所選群組**
或 **僅限所選專案**，接著選取 Codex 應運作的位置並建立
帳戶。群組選項會授予每個所選群組 Developer 存取權，且其專案與
子群組也會繼承該權限；專案選項則只會將 Developer
存取權授予您選取的個別專案。Codex 會建立 ChatGPT
Codex Connector 執行個體服務帳戶，並配發具備
`api` 範圍的個人存取權杖。

#### 使用現有帳戶

在 GitLab 中建立或選擇服務帳戶，且僅授予 Codex 應運作之群組或
專案的 Developer 存取權。前往 **服務
帳戶** 頁面，選取該帳戶 → **管理存取權杖** → **新增
權杖** ，以
[建立個人存取權杖](https://docs.gitlab.com/user/profile/service_accounts/#create-a-personal-access-token-for-a-service-account)；
該權杖必須具備 `api` 範圍，且距離到期日至少還有 30 天。返回
Codex，選擇 **使用現有服務帳戶**，貼上權杖，然後選取
**儲存權杖**。權杖儲存時會加密，且之後不會再顯示。

#### 管理服務帳戶權杖

工作區管理員可在 **Codex 雲端** →
**設定** → **連接器** 中管理服務帳戶。對於 Codex 建立的帳戶，管理員可撤銷
目前的權杖並產生新的權杖。對於現有帳戶，管理員可在 Codex 中
更換或移除已儲存的權杖，並視需要另外在 GitLab 中
撤銷該權杖。必須先設定有效的權杖，Codex 才能回應 GitLab
活動。

### 選擇 GitLab 活動傳送至 Codex 的方式

#### 為程式碼編寫任務或專案專屬設定建立專案環境

在 **Codex 雲端** → **設定** → **環境** 中選取 GitLab 專案，
並在需要 Codex 為該專案撰寫或執行程式碼時建立專案環境，
例如編輯檔案、提交變更或將更新推送至
合併請求分支；若審查作業依賴專案專屬的機密資訊、
網路存取權或設定指令，也需要建立專案環境。

使用 GitLab.com 時，也必須具備專案環境，才能啟用 Codex 審查。

建立環境時，請開啟 **啟用來自 GitLab 的 Codex 活動**，
以安裝專案 webhook，將合併請求、留言和議題
事件傳送至 Codex。建立專案 webhook 必須具備 Maintainer 或 Owner
存取權、管理員存取權，或可管理專案
 webhook 的自訂角色。已簽署的專案與群組 webhook 需要 GitLab 19.0 或更新版本。
對於自行管理的 GitLab 19.0，請確認 `webhook_signing_token` 功能旗標已
啟用；該旗標預設為啟用，並已在 GitLab 19.1 中移除。

#### 為 GitLab 群組內的專案啟用 Codex 審查活動

使用自行管理的 GitLab 或 Dedicated GitLab 時，工作區管理員可開啟 **環境**
→ **GitLab 活動** → **管理群組** ，為群組
及其子群組啟用 Codex 審查。Codex 會安裝群組 webhook，涵蓋該群組
內的所有專案。已連結的 GitLab 使用者必須是群組 Owner，且
群組 webhook 需要 GitLab Premium 或 Ultimate，以及 GitLab 19.0 或更新版本。

群組活動可啟用程式碼審查，但不會建立專案環境。
如要執行由 GitLab 觸發的程式碼編寫任務，例如編輯檔案、執行指令、
提交變更或將更新推送至合併請求，
請建立專案環境。

### 設定程式碼審查政策

在
[Codex 審查設定](https://chatgpt.com/codex/cloud/settings/code-review?provider=gitlab)中設定程式碼審查政策。
選擇程式碼庫政策：`Review my MRs`、`Review team MRs`、
`Review all MRs` 或 `Follow personal`。接著選擇審查執行時機： **MR 開啟時**、
**每次推送時**或 **智慧觸發（實驗性）**。程式碼庫設定可
覆寫個人預設值。

## 要求 Codex 審查

1. 在合併請求的留言中提及 `@codex review`。
2. 等待 Codex 以表情符號（👀）回應並發布審查結果。

Codex 會像團隊成員一樣，針對合併請求發布 GitLab 討論與留言。
根據預設，手動要求的審查可能包含 P0、P1 和 P2 等級的問題；
自動審查則著重於 P0 和 P1 等級的問題。

## 啟用自動審查

若要自動審查符合條件的合併請求，請在 Codex 設定中啟用 **自動
審查** ，選擇 GitLab 程式碼庫政策，並選擇
觸發條件： **MR 開啟時**、 **每次推送時**或 **智慧觸發（實驗性）**。
當合併請求事件符合該政策與觸發條件時，即使沒有 `@codex review` 留言，
Codex 也會執行審查。

必須透過專案 webhook 或上層群組的 webhook 啟用 GitLab 活動。
使用自行管理的 GitLab 或 Dedicated GitLab 時，已設定的服務帳戶
也必須具備將內容寫回專案的存取權。若已設定專案環境，Codex
會使用該環境。若上層群組已啟用活動，
其下層專案會繼承相應的涵蓋範圍。

## 自訂 Codex 的審查內容

Codex 會在程式碼庫中搜尋 `AGENTS.md` 檔案，並遵循適用的
程式碼審查規則。請在最接近受規則約束之程式碼的檔案中，新增 `## Code Review Rules`
區段。必要時可使用 `###` 標題，將相關檢查項目
分組。

例如，實驗報告服務可防止曝光後的行為
改變比較群組：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

將適用整個程式碼庫的規則放在根目錄的 `AGENTS.md` 中，並將服務專屬規則放入
子目錄中的檔案，例如 `services/experiment_reporting/AGENTS.md`。Codex 會針對每個變更的檔案，
套用根目錄指引及更具體、適用於該檔案的指引，
因此無關的變更不必包含特定服務的上下文。

先從兩到三條簡明規則開始，納入審查者經常說明的
檢查項目。以下是實用的規則：

- **著重於影響重大、且為程式碼庫所特有的行為。** 說明應標示的
  相容性限制、資料邊界或不安全的副作用，
  以及這些問題為何重要。
- **說明安全的處理方式或例外情況。** 提供 Codex 充分的上下文，
  以區分真正的問題和預期行為。
- **讓規則具備明確範圍並維持長期適用。** 優先描述預期結果，
  不要依賴可能變動的函式名稱，並將指引放在其適用的程式碼附近。
- **將機械式檢查留給 CI。** 不要在審查規則中納入格式設定、lint 或其他
  可由固定規則判定的檢查。

開啟具有代表性的合併請求，並以 `@codex review` 要求審查。
根據審查發現的問題與收到的回饋調整規則，並縮小或
移除會產生雜訊的指引。

程式碼審查規則用於引導 Codex，不能取代測試、分支保護機制
或必要的核准程序。

若有一次性的審查重點，請將其加入合併請求留言：

`@codex review for issues in the database migration`

## 處理審查發現的問題

修正審查發現的問題需要 **已設定的專案環境**；群組
活動本身僅支援審查，無法執行程式碼編寫任務。若專案已具備
環境，請在同一個合併請求中再留下一則
留言，要求 Codex 修正問題：

```md
@codex fix the P1 issue

Codex 會以合併請求作為上下文，啟動[雲端對話](/zh-Hant/codex/cloud)，並在具備
相關權限時，將修正內容推送回該分支。

## 指派其他任務給 Codex

其他程式碼編寫任務同樣需要 **已設定的專案環境**；群組
活動本身僅支援審查。如果您在留言中提及 `@codex`，並附上
`review` 以外的內容，Codex 會啟動[雲端對話](/zh-Hant/codex/cloud)，並以
您的合併請求作為上下文。

```md
@codex fix the CI failures

## 排解程式碼審查問題

如果 Codex 沒有回應或發布審查結果：

- 確認已選取預期的 GitLab 應用程式；如果使用專案專屬
設定，請確認該專案具備預期的 Codex 雲端環境。
- 確認專案或上層群組已啟用活動。在 GitLab 中檢查
**Webhook** →
[**近期事件**](https://docs.gitlab.com/user/project/integrations/webhooks/)，
  並確認合併請求和留言事件已成功傳送。
- 使用自行管理的 GitLab 或 Dedicated GitLab 時，請確認專案或群組 webhook 已
  簽署、已啟用 SSL 驗證，且執行個體使用 GitLab 19.0 或
  更新版本。對於自行管理的 GitLab 19.0，請確認 `webhook_signing_token` 功能
  旗標已啟用；並修復因執行失敗而自動停用的掛勾。
- 使用自行管理的 GitLab 或 Dedicated GitLab 時，請確認現有服務帳戶的
  個人存取權杖仍有效，且具備 `api` 範圍。如果服務帳戶由 Codex
  建立，請確認已在
[Codex 連接器設定](https://chatgpt.com/codex/cloud/settings/connectors)中正確設定該帳戶，
  且已啟用該專案或群組。
- 使用自行管理的 GitLab 或 Dedicated GitLab 時，請確認具備專案或上層群組 Developer 存取權的
是工作區服務帳戶，而不只是已連結的 GitLab 使用者，這樣 Codex 才能
發布審查結果和表情回應。成員資格可由下層繼承；
活動與服務帳戶存取權彼此獨立。
- 確認已啟用 **程式碼審查** 或 **自動審查** ，且 MR 符合
  程式碼庫政策與觸發條件。
- 使用 `@codex review`。
