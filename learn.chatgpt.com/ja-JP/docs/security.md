<!-- source: https://learn.chatgpt.com/ja-JP/docs/security -->

Codex Security は、セキュリティチームとエンジニアリングチームによる
脆弱性の発見、確認、修正を支援するアプリケーションセキュリティエージェントです。
Codex、ターミナル、TypeScript SDK、または接続済みの
GitHub リポジトリで利用できます。

最初のローカルスキャンを手順に沿って実行するには、[Codex Security プラグインの
クイックスタート](/ja-JP/codex/security/plugin)から始めてください。

## デスクトップアプリでの Codex Security の使用

ChatGPT デスクトップアプリで ChatGPT のドロップダウンメニューを開き、 **Codex** を選択します。
Codex Security プラグインをインストールして有効にし、サイドバーの **セキュリティ** を開きます。
セキュリティワークベンチでは、スキャン、検出結果、リポジトリを一元管理でき、
Codex は各スキャンをタスクとして実行します。

- **スキャン** では、スキャンの開始、進捗の確認、保存済みの結果のレビューを行えます。
- **検出結果** では、完了した各スキャンの問題と証拠を確認できます。
- **リポジトリ** では、リポジトリの履歴や未解決の検出結果を確認できます。

[セキュリティワークベンチの使用](/ja-JP/codex/security/plugin/workbench)では、
デスクトップアプリのワークフロー全体を確認できます。

### プラグインのユースケース

- [セキュリティスキャンの実行](/ja-JP/codex/security/plugin/scans)対象は、リポジトリまたは対象範囲を限定した 1 つのフォルダーです。
- [詳細なセキュリティスキャンの実行](/ja-JP/codex/security/plugin/deep-scans)は、より広範なレビューが必要で、完了まで長く待てる場合に適しています。
- [コード変更のレビュー](/ja-JP/codex/security/plugin/code-changes)は、Pull Request またはブランチをマージする前に行います。
- [バックログのトリアージ](/ja-JP/codex/security/plugin/triage-backlog)は、レビューが必要な既存のセキュリティ検出結果がある場合に行います。
- [検出結果の修正と検証](/ja-JP/codex/security/plugin/fix-findings)では、承認済みの検出結果に対して範囲を限定したパッチを適用します。
- [検出結果のエクスポートまたは追跡](/ja-JP/codex/security/plugin/export-findings)には、可搬形式のアーティファクト、または承認が必要な追跡先を使用します。
- 提供された検出結果、開示メモ、ソース、PoC を基に、[脆弱性レポートを作成する](/ja-JP/codex/security/plugin/vulnerability-reports)ことができます。
- スキャン結果またはその他のセキュリティ上の証拠に基づいて、[セキュリティ強化を提案する](/ja-JP/codex/security/plugin/security-hardening)ことができます。
- Codex Security プラグインの[新着情報](/ja-JP/codex/security/plugin/changelog)を確認できます。

  デスクトップアプリのセキュリティワークベンチと Codex CLI では、Codex Security プラグインを使用します。
  Codex Security クラウドは、Codex Cloud を介して接続済みの GitHub リポジトリをスキャンします。
  Codex のサンドボックス、承認、ネットワーク制御、管理者設定については、
[エージェントの承認とセキュリティ](/ja-JP/codex/agent-approvals-security)を参照してください。

## Codex Security CLI と SDK

CLI と TypeScript SDK は、一般公開されている
[`@openai/codex-security`](https://github.com/openai/codex-security) パッケージとして提供されています。
CLI は `npx` で実行します：

```bash
npx @openai/codex-security --help

スキャンを実行するには、Codex Security へのアクセス権が必要です。最良の結果を得るには、
[Trusted Access for Cyber](https://chatgpt.com/cyber) で認証済みのアカウントを使用してください。

プラグインと同じスキャナーを、複数のリポジトリで継続的に使用できます。CLI は
GitHub リポジトリを検出し、一括スキャンを再開し、複数回のスキャンにわたって検出結果を追跡し、
誤検出に関するフィードバックを記録します。アーキテクチャ情報とセキュリティポリシーを追加し、
推定コストの上限を設定したり、CI やコミット前にチェックを実行したりできます。
TypeScript SDK を使用すると、スキャン機能、進捗報告、コスト管理を
アプリケーションや開発ツールに組み込めます。

- [CLI クイックスタートから始めて](/ja-JP/codex/security/cli) CLI をセットアップし、
  リポジトリの事前チェックとローカルスキャンを実行します。
- [セキュリティスキャンの一括実行](/ja-JP/codex/security/cli/bulk-scans)により、GitHub リポジトリを検出したり、
  CSV インベントリから再開可能なキャンペーンを実行したりできます。
- [CI でのスキャンの実行](/ja-JP/codex/security/cli/ci)により、Pull Request の変更をレビューし、
  アーティファクトを保存し、SARIF をアップロードして重大度ポリシーを設定できます。
- [CLI のよくある質問](/ja-JP/codex/security/cli/faq)では、スキャン履歴、
  誤検出に関するフィードバック、カバレッジ、修正の検証についての回答を確認できます。
- [CLI リファレンス](/ja-JP/codex/security/cli/reference)で、サポートされている
  コマンド、フラグ、出力形式、アーティファクト、終了コードを確認できます。
- [TypeScript SDK を組み込む](/ja-JP/codex/security/sdk)ことで、コードから対象を選択し、
  結果の確認、進捗の追跡、スキャンのキャンセルを行えます。

## Codex Security クラウド

Codex Security クラウドは現在、リサーチプレビューとして提供されています。
接続済みの GitHub リポジトリをスキャンし、潜在的なセキュリティ問題を検出します。

チームを次のように支援します：

1. **脆弱性が疑われる箇所を発見** するため、リポジトリ固有の脅威モデルと実際のコードのコンテキストを使用します。
2. **ノイズを削減** するため、レビュー前に検出結果を検証します。
3. **検出結果を修正につなげる** ため、優先順位付きの結果、証拠、推奨されるパッチ候補を提示します。

## Codex Security クラウドの仕組み

Codex Security は、接続済みのリポジトリをコミットごとにスキャンします。
リポジトリからスキャン用のコンテキストを構築し、そのコンテキストに照らして脆弱性が疑われる箇所を確認したうえで、確度の高い問題を隔離環境で検証してから提示します。

次の点を重視したワークフローを利用できます：

- 汎用的なシグネチャではなく、リポジトリ固有のコンテキストを使用
- 誤検出の削減に役立つ、検証で得られた証拠
- GitHub でレビューできる修正案

## Codex Security クラウドへのアクセスと前提条件

Codex Security クラウドは、Codex Cloud を介して接続済みの GitHub リポジトリと連携します。
リポジトリが表示されない場合は、Codex Cloud のワークスペースでそのリポジトリを利用できるか確認するか、
OpenAI のアカウントチームにお問い合わせください。

## 関連ドキュメント

- [Codex Security プラグインのクイックスタート](/ja-JP/codex/security/plugin)では、インストールから最初のローカルスキャンまでの手順を説明します。
- [セキュリティワークベンチ](/ja-JP/codex/security/plugin/workbench)では、デスクトップアプリの保存済みスキャン、検出結果、リポジトリ、スキャンアクティビティについて説明します。
- [Codex Security CLI クイックスタート](/ja-JP/codex/security/cli)では、セットアップ、事前チェック、ターミナルでの最初のスキャンの手順を説明します。
- [セキュリティスキャンの一括実行](/ja-JP/codex/security/cli/bulk-scans)では、GitHub リポジトリの検出、CSV インベントリ、キャンペーン結果、再開時の動作について説明します。
- [Codex Security CLI のよくある質問](/ja-JP/codex/security/cli/faq)では、スキャン、検出結果、カバレッジ、コストに関する一般的な質問に回答します。
- [Codex Security TypeScript SDK](/ja-JP/codex/security/sdk) では、アプリケーションまたは開発ツールからスキャンを実行する方法を説明します。
- [Codex Security クラウドのセットアップ](/ja-JP/codex/security/setup)では、セットアップ、スキャン、検出結果のレビューについて詳しく説明します。
- [セキュリティレビュー](/ja-JP/codex/security/security-review)では、GitHub の Pull Request に対して詳細なセキュリティレビューを実行する方法を説明します。
- [脅威モデルを改善する](/ja-JP/codex/security/threat-model)ために、スコープ、エントリポイント、重要度に関する前提を調整する方法を説明します。
- [Codex Security クラウドに関するよくある質問](/ja-JP/codex/security/faq)では、クラウド製品についてよく寄せられる質問を取り上げます。
