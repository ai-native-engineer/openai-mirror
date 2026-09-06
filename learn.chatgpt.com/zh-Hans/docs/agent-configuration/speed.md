<!-- source: https://learn.chatgpt.com/zh-Hans/docs/agent-configuration/speed -->

<strong>ChatGPT Work 和 Codex 共享用量。</strong> 两者采用相同的
  定价、额度和用量限制。有关详情，
  请参阅 [Codex 定价](/codex/pricing)。

## 快速模式

Codex 可通过增加额度消耗来提高模型速度。

对于 GPT-5.6、GPT-5.5 和 GPT-5.4，快速模式可将模型速度提升至标准模式的 1.5 倍。
GPT-5.6 和 GPT-5.5 的额度消耗速率是标准模式的 2.5 倍；GPT-5.4 的额度消耗速率是标准模式的 2 倍。

在提供 GPT-6 Astra 快速模式的情况下，
其额度消耗速率为标准模式的 2.5 倍。有关模型可用性，请参阅[模型](/zh-Hans/codex/models)；
有关 Token 费率，请参阅[定价](/zh-Hans/codex/pricing#token-rates)。

在 CLI 中使用 `/fast on`、`/fast off` 或 `/fast status` 可更改或查看
当前设置。您也可以在 `config.toml` 中同时设置 `service_tier =
"fast"` 和 `[features].fast_mode = true`，以持久保存默认设置。
使用 ChatGPT 登录后，您可以在 ChatGPT 桌面应用、Codex CLI 和 IDE 扩展中
使用快速模式。快速模式是一项使用 ChatGPT 额度的功能。使用 API 密钥时，
Codex 会改用 API Token 定价，
不适用 ChatGPT 额度消耗倍率。API 优先处理采用单独的费率；对于 GPT-5.6，其费率为
标准 API Token 费率的 2 倍。

## Codex-Spark

GPT-5.3-Codex-Spark 是一款独立的 Codex 模型，速度快但能力较弱，专为近乎即时的实时编程迭代而优化。快速模式通过提高额度消耗速率来加速受支持的模型，而 Codex-Spark 是一个独立的模型选项，有自己的用量限制。

在研究预览期间，Codex-Spark 仅面向 ChatGPT Pro 订阅用户提供。
