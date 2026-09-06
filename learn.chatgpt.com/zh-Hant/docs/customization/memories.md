<!-- source: https://learn.chatgpt.com/zh-Hant/docs/customization/memories -->

記憶可讓 ChatGPT 和 Codex 將先前工作中的實用上下文帶入
日後的工作。
ChatGPT 網頁版使用 ChatGPT 記憶，而 Codex 本機用戶端則使用獨立的
本機記憶儲存空間與控制項。

請將必要的團隊指引保存在 `AGENTS.md` 或已提交至版本控制的文件中。
記憶應視為有助於回想資訊的輔助層，而非必須始終
適用之規則的唯一依據。

在 ChatGPT 桌面版應用程式中，使用 `/memories` 選擇對話是否可使用
本機記憶，或作為日後產生記憶的來源。若要開啟或關閉這項功能，請前往
**設定 \> 個人化** 。

若要管理 ChatGPT 記憶，請前往 **設定 \> 個人化**。ChatGPT Work 會使用
你的帳戶與工作區可用的記憶設定；不會使用
Codex 本機記憶儲存空間或本機記憶控制項。

在 Codex CLI 的互動式工作階段中，使用 `/memories` 控制
目前的對話能否使用既有的本機記憶，或成為日後產生
記憶時的輸入來源。請參閱 [設定本機記憶](#configure-local-memories)，瞭解該
指令無法使用時的處理方式。

IDE 擴充功能會使用已連線的 Codex 主機的本機記憶儲存空間。
該主機啟用記憶後，請使用與 Codex CLI 相同的
對話層級控制項。

[電腦使用紀錄](/zh-Hant/codex/customization/computer-history) 是 macOS 桌面版
功能，會將已允許的應用程式與網站上的活動轉換為記憶及
時間軸，供 ChatGPT 和 Codex 參考。

<a id="how-memories-work"></a>
<a id="memory-storage"></a>
<a id="control-memories-per-thread"></a>
<a id="control-memories-per-chat"></a>
<a id="control-memories-per-task"></a>
<a id="review-memories"></a>

## Codex 本機記憶的運作方式

啟用記憶後，Codex 可將先前符合條件的對話中的實用上下文
轉換為本機記憶檔案。Codex 會略過進行中或持續時間較短的工作階段，
遮蔽所產生的記憶欄位中的機密資訊，並在背景中更新記憶，
而不是在每次對話結束時立即更新。

記憶不一定會在對話結束後立即更新。Codex 會等到
對話閒置足夠長的時間，避免針對仍在
進行中的工作產生摘要。

當 Codex 速率限制的剩餘百分比低於設定的門檻時，
記憶產生程序也可能略過一次背景處理，以免 Codex 在接近限制時
消耗配額。

## 本機記憶儲存空間

Codex 將記憶儲存在 Codex 主目錄下。預設位置為
`~/.codex`。請參閱 [設定與狀態位置](/zh-Hant/codex/config-file/config-advanced#config-and-state-locations)
以瞭解 Codex 如何使用 `CODEX_HOME`。

主要記憶檔案位於 `~/.codex/memories/` 下，其中包含摘要、
長期保留的項目、最近的輸入，以及先前對話的佐證資料。

請將這些檔案視為自動產生的狀態資料。你可以在疑難排解時
或分享 Codex 主目錄前檢查這些檔案，但請勿將手動
編輯這些檔案作為主要控制方式。

<a id="control-local-memories-per-task"></a>

## 針對個別對話控制本機記憶

在 ChatGPT 桌面版應用程式和 Codex TUI 中，使用 `/memories` 控制
目前對話的記憶行為。對話層級的選項可讓你決定目前
對話能否使用既有記憶，以及 Codex 能否使用該對話
產生日後的記憶。

對話層級的選項不會變更你的全域記憶設定。

## 審查本機記憶

請勿將機密資訊儲存在記憶中。Codex 會遮蔽所產生的記憶
欄位中的機密資訊，但在分享 Codex 主目錄或
產生的記憶資料前，仍應先審查記憶檔案。

<a id="enable-memories"></a>
<a id="configuration"></a>

## 設定本機記憶

Codex 本機記憶預設為關閉。在 ChatGPT 桌面版應用程式中，開啟
**設定 \> 個人化** ，然後開啟 **啟用記憶**。

若透過設定檔進行設定，請將此功能旗標加入 `config.toml`：

```toml
[features]
memories = true

如需設定檔位置和記憶相關設定的完整清單，請參閱
[基本設定](/zh-Hant/codex/config-file/config-basic)及[組態
參考資料](/zh-Hant/codex/config-file/config-reference)。

常見的記憶專用設定包括：

- `memories.generate_memories`：控制新建立的對話是否可
  儲存為記憶產生程序的輸入來源。
- `memories.use_memories`：控制 Codex 是否將既有記憶注入
  日後的工作階段。
- `memories.disable_on_external_context`：值為 `true` 時，若對話使用了
  MCP 工具呼叫、網頁搜尋或工具搜尋等外部上下文，就不會將該對話納入
  記憶產生程序。較舊的 `memories.no_memories_if_mcp_or_web_search` 鍵
  仍可作為別名使用。
- `memories.min_rate_limit_remaining_percent`：控制啟動記憶產生程序前，Codex 速率限制必須達到的最低
  剩餘百分比。
- `memories.extract_model`：覆寫從個別對話擷取記憶時所使用的
  模型。
- `memories.consolidation_model`：覆寫彙整全域記憶時所使用的
  模型。
