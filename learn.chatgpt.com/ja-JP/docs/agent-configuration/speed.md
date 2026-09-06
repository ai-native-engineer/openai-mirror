<!-- source: https://learn.chatgpt.com/ja-JP/docs/agent-configuration/speed -->

<strong>ChatGPT Work と Codex は利用枠を共有します。</strong>
  どちらにも同じ料金体系、クレジット、利用上限が適用されます。
  詳しくは [Codex の料金](/codex/pricing)をご覧ください。

## Fast モード

Codex では、クレジット消費量を増やすことでモデルの速度を向上させることができます。

GPT-5.6、GPT-5.5、GPT-5.4 では、Fast モードでモデルの速度が 1.5 倍になります。GPT-5.6 と GPT-5.5 は標準レートの 2.5 倍、GPT-5.4 は標準レートの 2 倍のクレジットを消費します。

GPT-6 Astra の Fast モードを利用できる環境では、クレジット消費量は標準レートの 2.5 倍になります。
モデルの提供状況については[モデル](/ja-JP/codex/models)、
トークン料金については[料金](/ja-JP/codex/pricing#token-rates)をご覧ください。

CLI で `/fast on`、`/fast off`、または `/fast status` を実行すると、現在の設定を変更したり確認したりできます。
また、`config.toml` に `service_tier =
"fast"` と `[features].fast_mode = true` を設定すると、デフォルト設定を永続化できます。
ChatGPT でサインインすると、ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能で Fast モードを利用できます。
Fast モードは ChatGPT クレジットを使用する機能です。
API キーを使用する場合、Codex には API トークン料金が適用され、ChatGPT クレジットの倍率は適用されません。
API の優先処理には独自の課金レートがあり、
GPT-5.6 では標準 API トークンレートの 2 倍の料金がかかります。

## Codex-Spark

GPT-5.3-Codex-Spark は、ほぼ瞬時に応答し、リアルタイムでコーディングを反復できるよう最適化された、高速ながら性能は低めの別個の Codex モデルです。クレジット消費レートを上げて対応モデルを高速化する Fast モードとは異なり、Codex-Spark は独立したモデルとして選択でき、独自の利用上限があります。

リサーチプレビュー期間中、Codex-Spark を利用できるのは ChatGPT Pro の契約者のみです。
