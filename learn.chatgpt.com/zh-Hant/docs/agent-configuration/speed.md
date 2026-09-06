<!-- source: https://learn.chatgpt.com/zh-Hant/docs/agent-configuration/speed -->

<strong>ChatGPT Work 與 Codex 共用使用額度。</strong> 兩者採用相同的
  定價、點數與用量限制。詳情請參閱
  [Codex 定價](/codex/pricing)。

## 快速模式

Codex 可透過增加點數消耗量來提高模型速度。

快速模式可將 GPT-5.6、GPT-5.5 與 GPT-5.4 的模型速度提升至原本的 1.5 倍。
GPT-5.6 與 GPT-5.5 的點數消耗率為標準模式的 2.5 倍；GPT-5.4 則為標準模式的 2 倍。

在提供 GPT-6 Astra 快速模式的情況下，其點數消耗率為
標準模式的 2.5 倍。模型可用性請參閱[模型](/zh-Hant/codex/models)，
Token 費率請參閱[定價](/zh-Hant/codex/pricing#token-rates)。

在 CLI 中使用 `/fast on`、`/fast off` 或 `/fast status`，即可變更或查看
目前的設定。您也可以將 `service_tier =
"fast"` 與 `[features].fast_mode = true` 寫入 `config.toml`，以儲存預設設定。
透過 ChatGPT 登入後，即可在 ChatGPT 桌面版應用程式、Codex CLI 和 IDE 擴充功能中
使用快速模式。快速模式是一項以 ChatGPT 點數計費的功能。若使用 API 金鑰，
Codex 會改採 API Token 定價，
不適用 ChatGPT 點數倍率。API 優先處理另有計費費率；以 GPT-5.6 而言，其費用為
標準 API Token 費率的 2 倍。

## Codex-Spark

GPT-5.3-Codex-Spark 是一個獨立的 Codex 模型，速度快但能力較弱，專為幾乎無須等待的即時程式碼迭代而最佳化。
快速模式會以較高的點數消耗率提升受支援模型的速度；Codex-Spark 則是獨立的模型選項，有自己的用量限制。

在研究預覽期間，Codex-Spark 僅開放給 ChatGPT Pro 訂閱者使用。
