<!-- source: https://learn.chatgpt.com/zh-Hant/docs/security/plugin/fix-findings -->

使用 Codex Security 將已接受的安全性發現項目轉為具針對性且
經過驗證的修補程式。您可以在安全性工作台中作業，或透過提示詞、指令列或 CI/CD 執行修復
工作流程。Codex 會驗證問題，
並在測試安全且可行時新增具針對性的回歸測試；該測試會
在修正前失敗，並在修正後通過。它也會確認正常
行為仍可運作。如果回歸測試不安全或不可行，Codex
會記錄證據缺口，改為提供可重複執行且最有力的驗證
成品。

先從一個已接受的發現項目著手，並審查建議的修補程式與驗證
證據。如果此工作流程符合您的標準，請在不同的 Codex 任務或 CI/CD 作業中，逐一處理其他已接受的
發現項目。限制每項任務的範圍，可讓其程式碼變更與證據
更容易審查。

## 在 UI 中修正發現項目

從 **發現項目** 開啟已接受的發現項目，或從 **掃描** 開啟已完成的掃描。
審查其證據，然後使用 **修補程式** 產生、審查、套用及驗證
一項具針對性的修正。

1. 產生具針對性的修補程式

   開啟發現項目，選取 **修補程式** 分頁，然後選取 **產生修補程式**。
   若情況可行，Codex 會驗證或重現問題，並在不修改所選簽出內容的情況下建立修補程式
   成品。

2. 審查建議的差異內容

   仔細閱讀所有變更過的原始碼、回歸測試及驗證成品。請拒絕
大範圍重構、無關的清理，或任何會削弱其他安全性
控制措施的變更。

3. 在本機套用修補程式

   確認差異內容可接受後，才選取 **套用修補程式**。Codex 會將
   剛產生的修補程式完整套用至工作樹，並記錄該狀態。繼續之前，請審查
   工作樹的差異內容。

4. 驗證修正

   選取 **驗證修正**。Codex 會重新執行原始重現程序，或目前可用且最有力的
   漏洞利用檢查。如果回歸測試安全且可行，Codex
   會檢查該測試是否在修正前失敗，並在修正後通過。如果測試
   不安全或不可行，Codex 會記錄證據缺口，改為提供
   可重複執行且最有力的驗證成品。它也會檢查
   正常行為、相近的繞過方式及相關的程式碼庫測試。

5. 審慎決定是否關閉發現項目

   驗證不會自動關閉發現項目。請審查相關指令、
結果，以及仍存在的證據缺口；然後註明符合實情的
原因並關閉發現項目，或保持開啟以繼續處理。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    請先審查產生的安全性修正，再將其套用至您的簽出內容。
  </figcaption>
</figure>

## 透過 CLI 修正發現項目

針對來自掃描、工單、安全性公告、漏洞揭露、
安全性評估或內部審查且已接受的發現項目，請使用 Codex CLI。

請先將 Codex Security 安裝到 `CODEX_HOME` 中，也就是 `codex exec` 使用的位置，再
執行這些指令。全新的 CI 執行器預設
不包含市集外掛程式。

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

請提供已知的來源端、接收端、攻擊者輸入、影響、預期的不變條件、
重現程序、受影響的檔案及驗證指令。Codex 可檢查
程式碼庫，以找出缺少的技術細節。Codex 不應自行假設
產品政策或預期的安全性不變條件，而應先詢問。

若要自動執行，請簽出程式碼、備妥發現項目報告，
並將外掛程式安裝到執行器的 `CODEX_HOME`。接著啟用工作區
寫入權限，並將提示詞傳給 `codex exec`：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## 在 CI/CD 中掃描並修正發現項目

請先將 Codex Security 安裝到執行器的 `CODEX_HOME`，再叫用任一
技能。下列指令會使用已安裝的外掛程式；這些指令不會安裝該外掛程式。

在 CI/CD 中，將變更掃描與修復分開進行，並要求掃描不得
變更簽出內容。將已完成掃描的目錄保留為作業
成品，審查發現項目，並針對每個已接受且要修復的
發現項目，啟動獨立的 Codex 任務或作業。

依預設，`codex exec` 使用唯讀沙盒。執行變更掃描與
修復時，都請使用 `--sandbox workspace-write`。掃描需要該權限
來儲存暫存成品，但其提示詞仍須要求 `Do not modify
the checkout`。修復需要相同權限，才能寫入具針對性的
修補程式與驗證證據。請參閱 [權限與
安全性](/zh-Hant/codex/non-interactive-mode#permissions-and-safety)。

針對每次掃描及每個已接受的發現項目：

1. 解析該項變更的基底修訂版本與頂端修訂版本。
2. 對該差異執行 `$codex-security:security-diff-scan`，且不得修改
   簽出內容。
3. 保留完整的掃描目錄，並選取要修正的發現項目。
4. 對每個已接受的發現項目，各叫用一次 `$codex-security:fix-finding`，並傳入
   該發現項目的 ID 及已完成掃描的目錄。
5. 產生一個具針對性的修補程式，並新增一項會在
修正前失敗、修正後通過的回歸測試。如果該測試不安全或不可行，請記錄
證據缺口，改用可重複執行且最有力的驗證成品。
6. 驗證原始問題與正常行為。每個修補程式、測試
或備用驗證成品、驗證指令，以及任何證據缺口，
都應各自獨立傳回。

首先，在不修改簽出內容的情況下掃描變更：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

接著，修正已完成掃描中的一個已接受發現項目：

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

針對其餘每個
已接受的發現項目，在獨立任務或作業中重複執行第二個指令。驗證後，請透過您的一般
程式碼審查與發布流程合併各修補程式。若要在
修復前將發現項目交給其他團隊，請參閱 [匯出或追蹤
發現項目](/zh-Hant/codex/security/plugin/export-findings)。
