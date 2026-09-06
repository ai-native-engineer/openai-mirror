<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/export-findings -->

已完成的 Codex Security 掃描可用於下列兩種交接作業：

- **匯出** 會建立 JSON、CSV 或 SARIF 格式的可攜式檔案。
- **追蹤發現項目** 會將選取的發現項目準備成 Linear、GitHub 或 Jira
  議題，或一則私密的 GitHub 安全性公告草稿。Codex 會檢查是否有
  重複項目，並在寫入前等待您的核准。

這兩種工作流程都不會變更已封存的掃描套件。

  可用哪些產出檔案連結和匯出格式，取決於您使用的 Codex 介面和
  已安裝的外掛程式版本。請先查看 [外掛程式
  更新日誌](/zh-Hant/codex/security/plugin/changelog)，再將某種格式用於
  自動化。

## 匯出可攜式產出檔案

在桌面應用程式中，從 **安全性** \> **掃描** 開啟已完成的掃描。使用該掃描
提供的產出檔案連結，檢視 `report.md`、`findings.json`、
`scan-manifest.json`、`coverage.json`，以及 SARIF 報告（如有）。

若要建立其他支援的格式，請要求 Codex 從已完成的掃描中匯出發現項目，
但不要修改其已封存的掃描套件：

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

選擇適合目的地的格式：

| 格式 | 用途                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | 保留已封存的結構化發現項目，以供工具和指令碼使用。    |
| CSV    | 在試算表中審查發現項目及目前的本機分流狀態。  |
| SARIF  | 將發現項目傳送至支援 SARIF 交換格式的工具。 |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    從已完成的掃描中開啟涵蓋範圍、發現項目、掃描資訊清單、Markdown 報告或 SARIF
產出檔案。
  </figcaption>
</figure>

選取 **Markdown 報告** 後，檔案 `report.md` 會在您設定的外部
編輯器中開啟。使用哪個編輯器取決於您的系統設定；下方範例顯示
產生的報告內容。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    在產生的 Markdown 報告中，審查掃描範圍、威脅模型、已驗證的發現項目，以及詳細報告
連結。
  </figcaption>
</figure>

使用傳回的產出檔案路徑。如果其他工具需要完整的掃描
上下文，請將原始的 `scan-manifest.json`、`findings.json` 和
`coverage.json` 保存在一起。匯出作業不會將發現項目上傳至程式碼掃描
服務。

## 追蹤選取的發現項目

執行 `$codex-security:track-findings` 並指定一個已驗證的發現項目，或
明確選取同一個已封存掃描中的一批發現項目（最多 25 個）。每次
執行都使用一個提供者和一個目的地。每份私密的 GitHub 安全性
公告草稿只能接受一個發現項目。

若要準備 Linear 議題，請傳送以下內容：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

若要準備 GitHub 議題，請傳送以下內容：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

若要準備 Jira 議題，請傳送以下內容：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

若要在 Codex 中追蹤 Jira 議題，必須安裝 Atlassian Rovo 外掛程式。若要重複使用議題，
必須具備讀取權限；若要建立或更新議題，則必須具備讀取與寫入權限。

若要準備私密的 GitHub 安全性公告草稿，請傳送以下內容：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  建立安全性公告草稿時，必須有一個來自已封存的 `git_revision` 掃描的發現項目、
  經過驗證的公開正式來源程式碼庫，以及管理員存取權。此
  工作流程不會批次處理、更新、發布或關閉安全性公告。若來源不符合這些要求，請改用已核准的
  私密議題目的地。

## 審查擬寫入的內容

1. 確認發現項目 ID 和指紋來自指定的已封存掃描。
2. 確認提供者、確切的 Linear 團隊、GitHub 程式碼庫、Jira 專案或
安全性公告程式碼庫，以及目的地目前的可見度。
3. 審查重複項目檢查的結果： `create`、`reuse`、`update` 或 `blocked`。
4. 完整閱讀擬寫入的標題、內文、原始碼位置和提供者
中繼資料。若目的地
不應公開漏洞利用細節或內部證據，請將其移除。
5. 僅核准該份確切的酬載內容。如果目的地、可見度、發現項目
集合或內文有任何變更，就必須重新產生預覽。

敏感的發現項目應傳送至私密目的地。在內部或公開的
GitHub 程式碼庫中建立議題時，必須顯示明確的可見度警告，
並核准完整內容。請將安全性公告草稿的說明視為
日後會公開的內容，並在核准前移除認證資訊、私密證據和不必要的
漏洞利用細節。

在 Codex 對話中審查並核准外部操作。核准
不會在安全性工作台中建立獨立的議題或安全性公告畫面。

## 驗證已追蹤的項目

核准擬寫入的內容後，Codex 會重新檢查已封存的來源、
目的地、存取權和重複項目狀態。若為批次，Codex 會逐一處理發現項目，
並在遇到第一個不確定的結果時停止。建立、更新或
重複使用只有在 Codex 讀回確切的議題並驗證其
繫結識別碼和內容後才算完成。

將傳回的議題或安全性公告標準 URL 與分流記錄一併保存。
請接著參閱 [修正並驗證發現項目](/zh-Hant/codex/security/plugin/fix-findings)，
但須等到負責人接受該項目進行修正後再繼續。
