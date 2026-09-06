<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/api-integration-migrations -->

## はじめに

新しいモデルや API 機能のリリースに合わせてインテグレーションをアップグレードし、最新の改善を活用することをお勧めします。
モデルを切り替える際は、モデル名を更新するだけでは済まないことがよくあります。

API に変更が加わる場合もあります。たとえば GPT-5.4 モデルでは、アシスタントメッセージに新しい `phase` パラメーターを追加しました。このパラメーターをインテグレーションに含めることが重要です。ただし、特に注意すべきなのは、モデルによって動作が異なり、既存のプロンプトの変更が必要になる場合があることです。

新しいモデルに移行する際は、必要なコード変更を行うだけでなく、ワークフローへの影響も必ず評価してください。

## OpenAI Docs スキルの活用

[モデルガイダンス](/api/docs/guides/latest-model)のページには、モデルの世代ごとに API 機能、モデルの動作、移行、プロンプトに関するガイダンスがまとめられています。

OpenAI Docs スキルには、移行時の具体的な参考資料として[個別のガイダンス](https://github.com/openai/codex/blob/6323f0104d17d211029faab149231ba787f7da37/codex-rs/skills/src/assets/samples/openai-docs/references/upgrading-to-gpt-5p4.md)も含まれています。現在のアップグレード先については、[モデルガイダンス](/api/docs/guides/latest-model)のページを参照してください。

Codex には OpenAI Docs スキルが標準で含まれるようになりました。OpenAI API を使って開発する際に、最新のドキュメントとガイダンスをすべて参照できるよう、プロンプトでこのスキルを必ず指定してください。

## 堅牢な評価パイプラインの構築

Codex は最新のプロンプトガイダンスに基づいてプロンプトを自動更新できますが、インテグレーションが想定どおりに動作していることを自動で検証できる仕組みも用意してください。

インテグレーションを変更するたびに実行できる評価パイプラインを必ず構築し、動作にリグレッションがないことを検証してください。

この [Cookbook ガイド](/cookbook/examples/evaluation/building_resilient_prompts_using_an_evaluation_flywheel)では、OpenAI の [Evals API](/api/docs/guides/evals) を使ってこれを実現する方法を詳しく説明しています。
