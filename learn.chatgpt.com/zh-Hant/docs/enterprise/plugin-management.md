<!-- source: https://learn.chatgpt.com/zh-Hant/docs/enterprise/plugin-management -->

## 開始之前

工作區管理員可以從 GitHub 匯入外掛程式市集，並從程式碼庫同步更新其中的外掛程式。市集是一份 JSON 目錄，列出要匯入的外掛程式。

請使用可讀取市集程式碼庫及其參照的其他程式碼庫的 GitHub 帳戶。公開與私人 GitHub 程式碼庫皆受支援。匯入前，請完成存取程式碼庫所需的任何 GitHub 組織核准程序。

匯入前，請審查程式碼庫內容。新外掛程式的安裝政策預設為 **可用** ，身分驗證則設為在安裝時進行。新市集預設啟用每日自動同步。匯入時會處理所有有效項目，後續同步則會自動新增程式碼庫中的所有新外掛程式。

## 設定市集同步

1. 開啟 **管理** \> **外掛程式** ，然後選取 **新增** \> **匯入市集**。
2. 在 **來源**欄位中輸入程式碼庫 URL，例如 `https://github.com/example/team-plugins`。請僅使用程式碼庫 URL，不要使用分支或資料夾的 URL。
3. 如果市集位於子目錄，請在 **路徑**欄位中輸入該目錄。例如，若檔案位於 `team-tools/.agents/plugins/marketplace.json`，請填入 `team-tools`。若要使用程式碼庫根目錄，請將 **路徑** 留空。請勿輸入資訊清單的檔名。
4. 你也可以輸入 **分支、標籤或提交**。此欄位留空時，會使用程式碼庫的預設分支。指定分支可接收後續提交；指定固定的提交則會維持在該修訂版本。
5. 選取 **匯入市集** ，並在出現提示時授權 GitHub 存取。規模非常大的市集，首次匯入可能長達一小時。後續每日同步通常需要幾分鐘。
6. 審查 **匯入結果**，然後逐一開啟已匯入的外掛程式，設定安裝政策及所需的應用程式。

若要直接要求更新而不等待每日同步，請在 **管理** \> **外掛程式** \> **市集** 中開啟該市集，然後選取 **立即同步**。

## 支援的格式

所選目錄必須包含下列檔案之一：

| 檔案                               | 格式                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | 包含 `plugins` 陣列的 Codex 市集。                          |
| `.claude-plugin/marketplace.json`  | 包含 `plugins` 陣列且與 Claude 相容的市集。              |
| `.claude-plugin/plugin.json`       | 獨立的 Claude 外掛程式，適用於未提供市集資訊清單的情況。 |

市集中的項目可以參照含有 `.codex-plugin/plugin.json` 的原生外掛程式、與 Claude 相容的外掛程式、Agent Plugins 1.0 套件，或受支援的技能套件。

在 Codex 市集中，同一程式碼庫內的外掛程式應使用本機路徑：

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

此路徑是相對於所選市集的根目錄，而非 `.agents/plugins/`。

與 Claude 相容的市集可以使用路徑字串來指定各個本機外掛程式：

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Codex 市集項目也支援使用 `source: "url"` 指定 GitHub 程式碼庫根目錄中的外掛程式，以及使用 `source: "git-subdir"` 指定 GitHub 子目錄中的外掛程式。例如：

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Git 來源可以指定 `ref`，或完整的 40 字元提交 `sha`。授權存取的 GitHub 帳戶必須能讀取每個被參照的程式碼庫。工作區匯入功能目前僅支援 GitHub 程式碼庫。

## 設定工作區存取權

從 GitHub 匯入與同步時，不會套用程式碼庫中的安裝或身分驗證政策，包括 `AVAILABLE`、`INSTALLED_BY_DEFAULT`、`NOT_AVAILABLE`、`ON_INSTALL` 和 `ON_USE`。這些選項由工作區管理員為每個外掛程式設定。同步更新或將現有外掛程式改由 GitHub 管理時，會保留其工作區政策。

使用 **安裝政策** ，為每個符合資格的角色選擇 **可用** 或 **已安裝** 。也必須啟用所需的應用程式，且成員必須具備所連接服務的存取權。匯入外掛程式不會授予應用程式存取權，也不會連接成員的帳戶。如需瞭解角色、應用程式和動作的控制措施，請參閱[外掛程式控制措施](/zh-Hant/codex/enterprise/apps-and-connectors)。

## 將現有外掛程式改由 GitHub 管理

在現有外掛程式的市集項目中新增 `pluginId`：

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

從 **管理** \> **外掛程式** 開啟該外掛程式，並複製其 URL 中位於 `/admin/plugins/` 之後的 ID。將 `pluginId` 放在市集項目中，與 `name` 和 `source` 並列。現有外掛程式必須位於同一個工作區。

這會讓已上傳或其他尚未受管理的工作區外掛程式改由 GitHub 管理。外掛程式會保留其 ID、共用設定與工作區政策。之後的更新將來自 GitHub；無法再透過上傳封存檔取代受管理的外掛程式。已由其他 GitHub 來源管理的外掛程式，無法透過此方式接管。

## 僅限桌面版的外掛程式

任何在 `mcp.json` 或 `.mcp.json` 中宣告 MCP 伺服器的已匯入外掛程式，都會標示為 **僅限桌面版** ，且只能在 ChatGPT 桌面版應用程式中使用。使用遠端 HTTPS URL 的伺服器也包含在內。其他受支援的 MCP 組態形式（例如內嵌伺服器宣告）也有相同限制。

## 使用 `.app.json` 參照現有應用程式

在外掛程式根目錄新增 `.app.json`。檔名以點開頭；不支援省略該點的 `app.json`。

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

將 `asdk_app_example` 替換為現有應用程式的 ID。支援的應用程式 ID 以 `asdk_app_`、`connector_` 或 `templated_apps_` 開頭。請使用應用程式 ID，而非 `plugin_...` ID。例如，包含 `plugin_asdk_app_example` 的外掛程式 URL 代表應用程式 `asdk_app_example`。

此參照在檔案中以 `team-tools` 作為鍵名。若外掛程式依賴此應用程式，請將 `required` 設為 `true`。你可以新增更多項目，以參照其他現有應用程式。

若是原生外掛程式，請在 `.codex-plugin/plugin.json` 中將 `apps` 設為 `./.app.json`。以下是此範例的完整資訊清單：

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

請依照下列目錄結構放置檔案：

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

這項參照不會建立應用程式，也不會授予權限。管理員必須讓預定的角色可使用該應用程式，且成員必須完成所需的身分驗證。現有的應用程式權限、動作控制措施及服務存取規則仍然適用。

## 讓外掛程式保持最新

新市集會每日檢查更新。開啟 **管理** \> **外掛程式** \> **市集**，選取該市集，再選擇 **立即同步** ，即可要求更新，無須等待自動同步。

同步可以新增市集項目並更新現有外掛程式。合併程式碼庫變更前，請先審查內容，因為自動同步會匯入所有新外掛程式。

同步後，請審查狀態與已儲存的報告。 **已完成：N 個錯誤** 表示本輪同步已結束，但部分外掛程式無法處理。若現有外掛程式的更新無效，系統會保留其最近一個可正常運作的版本。在 GitHub 中修正回報的問題後，選取 **立即同步** 即可重試。

從程式碼庫移除項目，不會刪除已匯入工作區的副本。該副本會標示為 **來源中已不存在**。在 ChatGPT 中刪除市集，則會刪除從該市集匯入的所有外掛程式。

## 重新連接 GitHub 或變更存取權

若要 **重新連接 GitHub**，請先確認匯入時使用的 GitHub 帳戶仍可存取該程式碼庫及其參照的所有程式碼庫。接著，原先匯入市集的管理員應在 ChatGPT 中開啟 GitHub 外掛程式，重新連接自己的帳戶，因為市集同步使用的是該管理員的 GitHub 連線。

若要 **移轉給新擁有者**，新的工作區管理員應開啟 **管理** \> **外掛程式** \> **新增** \> **匯入市集** ，使用相同的 **來源**、 **路徑**及 **分支、標籤或提交** 值匯入同一個市集。後續同步將使用這位管理員的 GitHub 連線。

請勿為了重新連接市集或變更擁有者而刪除市集，因為這也會移除從該市集匯入的外掛程式。
