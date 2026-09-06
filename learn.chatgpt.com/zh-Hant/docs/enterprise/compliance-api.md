<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/compliance-api -->

使用 Compliance API 執行需要可稽核紀錄的安全性、法律、治理與調查工作流程。
若要衡量採用情形與趨勢，請使用分析資料，
而非合規紀錄。

[Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)
是目前存取要求、事件涵蓋範圍、路由、
結構描述、篩選條件、資料保留與請求行為的權威依據。

如需概略瞭解可用的合規介面與常見整合模式，
請參閱[合規平台指南](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)。

## 使用 Compliance API 的時機

當您有以下需求時，適合使用 Compliance API：

- 將受支援的紀錄匯出至稽核或調查系統。
- 執行組織的資料保留與法務保留程序。
- 將 Codex 活動與其他安全性或身分資料建立關聯。
- 支援經核准的安全性、法律或治理調查。

它不是生產力儀表板。請勿用它推斷程式碼品質或
個人績效。若要製作採用情形報告，請使用[工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)
或 [Analytics API](/zh-Hant/codex/enterprise/analytics-api)。

## 開始使用

1. 開啟 [Admin API 參考文件](https://chatgpt.com/public/admin/api-reference)，並
   確認您的管理員角色可以存取
   所需的合規資源。
2. 使用僅允許附加資料的合規紀錄串流持續收集資料。
請查閱 API 參考文件，
瞭解目前支援的資源與擷取模式。
3. [下載紀錄檔](#download-logs)，並測試將資料匯入非生產環境的
   安全資訊與事件管理（SIEM）系統或資料湖。
4. 排程持續收集作業，並對匯出的紀錄套用組織的存取、
資料保留與法務保留控制措施。請勿假設來源端的
保留期限可以取代組織的保留政策。

例如，資安團隊可以將不可變更的合規事件以串流方式傳送至其
SIEM 以進行調查，或將這些事件轉送至經核准的電子蒐證工作流程。
如需目前的路由與結構描述，請查閱 API 參考文件，
不要從本指南複製端點規格。

### 下載紀錄

下載 [Bash 指令碼](/downloads/compliance-api/download_compliance_files.sh)
或 [PowerShell 指令碼](/downloads/compliance-api/download_compliance_files.ps1)。
兩者都會逐頁列出並下載指定時間戳記之後的所有可用紀錄檔，
並將 JSONL 寫入標準輸出。錯誤訊息則寫入標準錯誤輸出。

將 `COMPLIANCE_API_KEY` 設為您的 Enterprise Compliance API 金鑰。將
`<workspace_or_org_id>` 替換為您的 ChatGPT 工作區 ID 或 API 平台
組織 ID，並將 `<after>` 替換為包含時區的 ISO 8601 時間戳記。
此範例會擷取 `AUTH_LOG` 檔案，每次 100 個。

在 macOS 或 Linux 上，安裝 Bash、`curl` 和 `jq`，然後執行：

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Windows 指令碼支援 PowerShell 5.1 或更新版本。請審查下載的檔案。
如果 Windows 封鎖該檔案，且組織的執行原則允許解除封鎖，請執行
`Unblock-File -Path .\download_compliance_files.ps1`。此範例使用
PowerShell 7，將檔案儲存為不含位元組順序標記的 UTF-8 格式：

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## 確認管理界線

合規涵蓋範圍以 ChatGPT 工作區及目前 API 參考文件中
所列的產品為準。Platform API 的組織資料則適用
其自身的 API 資料與管理控制措施。

目前的路由、事件涵蓋範圍、結構描述、篩選條件、資料保留方式、
權限要求與請求運作方式，皆以 API 參考文件為準。
本頁不會重複列出這套規格。

## 相關文件

- [工作區分析](/zh-Hant/codex/enterprise/workspace-analytics)
- [管理員導入指南](/zh-Hant/codex/enterprise/admin-setup)
- [治理](/zh-Hant/codex/enterprise/governance)
- [Analytics API](/zh-Hant/codex/enterprise/analytics-api)
