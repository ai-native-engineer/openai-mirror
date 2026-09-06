<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/analytics-api -->

Codex Analytics API は、ChatGPT ワークスペースにおける Codex の利用状況とアクティビティの集計指標を提供します。

[Codex Analytics API リファレンス](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)は、
最新のアクセス要件、ルート、リクエストとレスポンスのスキーマ、
指標、時間の扱い、ページネーションに関する正式な情報源です。

## Analytics API の使用場面

Analytics API は、次のような用途に適しています。

- Codex の定期レポート作成を自動化する
- Codex の集計指標を組織内データと結合する
- 承認された対象者向けに、管理されたレポートレイヤーを構築する
- インテグレーションがインタラクティブなダッシュボードに依存することを避ける

監査ログの生データを扱うインターフェースではありません。
ワークフローで監査可能なアクティビティ記録が必要な場合は、
[Compliance API](/ja-JP/codex/enterprise/compliance-api) を使用してください。

## 管理範囲の確認

Analytics API の結果は ChatGPT ワークスペースに限定されますが、リクエストの認証には Platform 組織の API キーを使用します。キーが属する組織は、ワークスペースに関連付けられた組織と一致している必要があります。

キーのプロビジョニング、スコープ要件、ルート、スキーマ、フィールド、時間の扱い、ページネーションの動作に関する最新の仕様は、API リファレンスで定義されています。このページでは、その仕様を重複して掲載しません。

## 関連ドキュメント

- [ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)
- [管理者向けロールアウトガイド](/ja-JP/codex/enterprise/admin-setup)
- [ガバナンス](/ja-JP/codex/enterprise/governance)
- [Compliance API](/ja-JP/codex/enterprise/compliance-api)
