<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/deep-scans -->

需要更徹底的審查，且可接受較長的
執行時間時，請執行深度掃描。深度掃描會更廣泛地搜尋程式碼庫，
並可降低各次執行結果的變異性。

請先執行[標準掃描](/zh-Hant/codex/security/plugin/scans)，確認掃描範圍
與結果。需要更徹底的評估時，再執行深度掃描。

## 選擇標準掃描或深度掃描

|                         | 標準掃描                                      | 深度掃描                                             |
| ----------------------- | -------------------------------------------------- | ----------------------------------------------------- |
| 最適合                | 首次執行，以及程式碼庫或資料夾的例行審查 | 在標準掃描後進行更徹底的審查           |
| 變異性             | 標準                                           | 較低                                               |
| 範圍                   | 程式碼庫或明確指定的資料夾                      | 程式碼庫或明確指定的資料夾                         |
| 執行時間與資源用量   | 較低                                              | 較高                                                |
| Pull Request 與差異內容 | 使用變更審查工作流程                     | 不支援；請改用變更審查工作流程 |

## 設定深度掃描的執行參數

若要控制深度掃描的並行作業數與執行時間，請建立或編輯
`~/.codex/codex-security/config.toml`。若已設定 `CODEX_HOME`，請改用
`$CODEX_HOME/codex-security/config.toml`。

例如，以下設定檔會執行時間較短且並行作業數受限的掃描：

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

| 設定                         | 預設值 | 說明                                                                                                        |
| ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------ |
| `workers`                       | `4`     | 允許同時執行的獨立標準掃描工作程式數量。舊有設定值 `"auto"` 也會解析為 `4`。 |
| `subagents`                     | `3`     | 每個工作程式可啟動的子代理程式數量。設為 `0` 即可停用子代理程式。                                                |
| `stop_after_no_new`             | `4`     | 若連續完成的工作程式掃描達此次數，且都沒有新的發現項目，則停止掃描。                                   |
| `stop_after_consecutive_errors` | `3`     | 若工作程式連續發生錯誤達此次數，則停止掃描。                                                                    |
| `max_discovery_runs`            | `40`    | 限制彙整前可執行的獨立標準掃描次數。                                             |
| `max_time_hours`                | `96`    | 將工作程式執行時間限制為大於零且不超過 `96` 小時；必要時可使用小數。                          |

較低的設定值可縮短掃描時間並減少 Token 用量，但可能遺漏發現項目。
組態變更僅適用於新的深度掃描，不適用於已在進行中的掃描。

時間限制到期時，Codex Security 會停止尚未完成的工作程式，保留
已完成的掃描結果，並將其彙整成最終報告。若沒有任何工作程式
在期限前完成原始碼審查，報告會註明掃描僅涵蓋
部分範圍。

`max_time_hours` 設定需要外掛程式版本 `0.1.19` 或更新版本。版本詳情請參閱
[外掛程式更新日誌](/zh-Hant/codex/security/plugin/changelog)。

## 開始深度掃描

在桌面 App 中，開啟 **安全性**，選取 **掃描**，再選取 **+ 掃描**。
選擇程式碼庫或其他資料夾，選取 **程式碼庫**，並開啟
**深度掃描**。掃描會涵蓋所選的整個程式碼庫或資料夾。

您也可以從 Codex 對話啟動涵蓋整個程式碼庫的深度掃描：

```text
Use $codex-security:deep-security-scan to run a deep security scan of this repository.

若要掃描單一程式碼庫中的某個元件，請明確指定其資料夾：

```text
Use $codex-security:deep-security-scan to run a deep security scan of /absolute/path/to/repository/services/payments.

若要在桌面 App 中執行限定範圍的深度掃描，請將資料夾選為程式碼庫。
掃描會涵蓋所選的整個資料夾。

## 確認設定並執行預先檢查

若要獲得最佳掃描品質，請使用 <code>{RECOMMENDED_MODEL_REFERENCES.latestSecurityScanModel.slug}</code>，
並將推理強度設為 `xhigh`。

1. 選取 **程式碼庫** 並開啟 **深度掃描**。
2. 確認程式碼庫或所選資料夾中的程式碼，確實是您要
掃描的內容。
3. 選擇模型與推理強度。
4. 開啟 **其他上下文** ，提供具體攻擊向量、敏感的
   應用程式區域，或無法從程式碼得知的程式碼庫上下文。
5. 選取 **開始掃描**。

深度掃描工作程式會沿用您選擇的模型與推理設定。每個
工作程式都會執行一次完整的標準掃描，Codex Security 會彙整
已完成的結果。您可以在 **掃描**中追蹤已儲存的掃描，或選取 **檢視
活動** 來查看其 Codex 任務。請先查看[外掛程式
更新日誌](/zh-Hant/codex/security/plugin/changelog)，再更新外掛程式或
啟動長時間執行的掃描。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    追蹤進行中的深度掃描階段，並查看其 Codex 活動，
再審查已完成的結果。
  </figcaption>
</figure>

## 審查結果

深度掃描與
標準掃描使用相同的已儲存掃描詳細資料及完整掃描目錄。在 **掃描** 中開啟已完成的掃描，或在
**發現項目**中審查其發現項目。當您要求這些輸出時，產生的 `report.md` 會連結至詳細的漏洞報告
或結構性強化指引。
分享或封存結果時，請將報告與所有連結的 `findings/` 及 `hardening/` 目錄
一併保留。

請先審查涵蓋範圍摘要，再查看發現項目。即使深度掃描也有其限制，
因此請先確認延後檢查的範圍及剩餘的佐證缺口，再做出
結論。對於您接受的發現項目，請接著[修正並驗證
發現項目](/zh-Hant/codex/security/plugin/fix-findings)。

若要審查 Pull Request、提交、分支範圍或本機修補內容，請使用[審查程式碼
變更](/zh-Hant/codex/security/plugin/code-changes)。深度掃描不能取代
以差異內容為核心的工作流程。
