<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/security-hardening -->

使用 `$codex-security:propose-security-hardening`，將一組
安全性證據轉化為結構或架構層面的強化選項。此
工作流程可分析已完成的 Codex Security 掃描，也可從提供的
發現項目、揭露報告、事件審查、評估文件與
原始碼著手。

產出成果是一份設計方案集，而非修補程式，也無法證明
漏洞已修復。Codex 只有在您選定一個選項，並
明確要求它進行該項變更後，才會修改程式碼庫。

## 準備證據

請為此工作流程提供以下內容：

- 掃描目錄，或明確列出的一組發現項目與報告。
- 目標原始碼樹，以及相關修訂版本或快照（若有）。
- PoCs、追蹤記錄、事件證據或評估資料，用以佐證
這些發現項目。
- 效能、記憶體、相容性、可靠性、營運、
交付時程或變更範圍方面的限制。

此工作流程會依據證據，找出反覆遭破壞的不變條件、分散的
控管措施、具有特殊權限的關鍵節點、薄弱的隔離邊界，以及反覆出現的
修復模式。它也可能判定，採用局部修正會比進行架構變更
更符合問題規模。

## 執行工作流程

傳送類似以下內容的提示詞：

```text
Use $codex-security:propose-security-hardening to analyze [scan directory or finding paths] against [source tree and revision]. Develop evidence-backed structural hardening options with engineering tradeoffs, before-and-after diagrams, a migration plan, and an implementation handoff. Do not modify the repository.

## 審查方案集

一份實用的方案集應做到以下幾點：

- 將每項提議的變更與具體的發現項目、原始碼和威脅模型中的
證據建立關聯。
- 說明現行設計，以及新設計應
維持的安全性不變條件。
- 比較不同選項在殘餘風險、效能、
可靠性、營運、相容性與遷移成本方面的差異。
- 只有在證據足以支持某個選項時，才建議採用該選項，並明確列出
各項假設與待釐清問題。
- 納入部署、驗證、回滾與實作指引。
- 明確區分觀察到的事實、推論與擬議的設計屬性。

選擇選項前，請先審查證據與各項取捨。架構
圖或設計建議，不能取代對原始
發現項目或已實作的修正措施進行驗證。

## 使用掃描提供的安全性強化指引

對於含有
可列入報告之發現項目的標準、深度或變更掃描，您可以要求提供安全性強化方案集。Codex 會將方案集寫入 `hardening/hardening.md`，
將結構化分析寫入 `hardening/hardening.json`，並將相關提案
或圖表存放於 `hardening/`。掃描結果會在 `report.md` 中提供方案集的連結。

請保持完整的掃描目錄結構，確保這些連結仍可使用。若要審查
方案集所依據的個別報告，請參閱[撰寫漏洞
報告](/zh-Hant/codex/security/plugin/vulnerability-reports)。
