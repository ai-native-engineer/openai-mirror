<!-- source: https://learn.chatgpt.com/ja-JP/docs/open-source -->

OpenAI は Codex の主要部分をオープンソースとして開発しています。開発は GitHub 上で進められており、進捗の確認、問題の報告、改善への貢献が可能です。

広く使われているオープンソースプロジェクトをメンテナンスしている方、または重要なプロジェクトを支えるメンテナーを推薦したい方は、API クレジット、Codex を利用できる ChatGPT Pro、Codex Security への限定アクセスを得るために、[Codex for OSS プログラムに申請することもできます](/community/codex-for-oss)。

## オープンソースコンポーネント

| コンポーネント                     | 参照先                                                                                             | 備考                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Codex CLI                     | [openai/codex](https://github.com/openai/codex)                                                           | Codex のオープンソース開発の主要拠点      |
| Codex SDK                     | [openai/codex/codex-sdk](https://github.com/openai/codex/tree/main/sdk)                                   | Codex リポジトリ内の SDK ソースコード                      |
| Codex Security CLI            | [openai/codex-security](https://github.com/openai/codex-security)                                         | セキュリティ上の脆弱性を検出・検証する CLI |
| Codex Security TypeScript SDK | [openai/codex-security/sdk/typescript](https://github.com/openai/codex-security/tree/main/sdk/typescript) | Codex Security のスキャンを実行する TypeScript SDK         |
| Codex App Server              | [openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)         | Codex リポジトリ内の App Server ソースコード               |
| スキル                        | [openai/skills](https://github.com/openai/skills)                                                         | ChatGPT と Codex を拡張する再利用可能なスキル           |
| プラグイン                       | [openai/plugins](https://github.com/openai/plugins)                                                       | ChatGPT と Codex 向けの再利用可能なプラグイン                  |
| IDE 拡張機能                 | -                                                                                                         | オープンソースではありません                                         |
| Codex Cloud                   | -                                                                                                         | オープンソースではありません                                         |
| 汎用クラウド環境   | [openai/codex-universal](https://github.com/openai/codex-universal)                                       | Codex Cloud で使用されるベース環境                    |

## 問題の報告先と機能リクエスト先

バグ報告と機能リクエストには、適切な GitHub リポジトリを使用してください：

- Codex のバグ報告と機能リクエスト：[openai/codex/issues](https://github.com/openai/codex/issues)
- Codex Security CLI と TypeScript SDK のバグ報告と機能リクエスト：[openai/codex-security/issues](https://github.com/openai/codex-security/issues)
- ディスカッションフォーラム：[openai/codex/discussions](https://github.com/openai/codex/discussions)

イシューを作成する際は、使用しているコンポーネント（CLI、SDK、IDE 拡張機能、Codex Cloud、Codex Security のいずれか）と、可能であればそのバージョンを記載してください。
