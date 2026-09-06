<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/governance -->

Codex のアクティビティに関するガバナンスには、インタラクティブな分析、プログラムによるレポート作成、関連する ChatGPT の利用管理、監査記録が含まれます。確認したい内容に合う手段を選択してください。分析データとコンプライアンスデータは、それぞれ用途が異なります。

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| 目的                                          | 最初の参照先                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| ChatGPT 全体の導入状況を把握する                      | [ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)              |
| Codex の導入状況とアクティビティをインタラクティブに確認する        | [Codex の分析](#analytics-dashboard)                                   |
| Codex の集計レポートを別のシステムに取り込む     | [Analytics API](/ja-JP/codex/enterprise/analytics-api)                          |
| 監査や調査のために記録をエクスポートする               | [Compliance API](/ja-JP/codex/enterprise/compliance-api)                        |
| プランに応じた ChatGPT ワークスペースのクレジット管理を確認する | [ChatGPT の利用上限と支出管理](/ja-JP/codex/enterprise/usage-limits) |

## 管理機能へのアクセス

- ワークスペースのレポートをインタラクティブに確認するには、
  [ワークスペースの分析](https://chatgpt.com/admin/usage)を開きます。
  [ワークスペースの分析ガイド](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)では、現在のロールとビューについて説明しています。
- レポートをプログラムで定期的に作成する必要がある場合は、
  [Codex Analytics API リファレンス](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)を開きます。
- 監査や調査のための連携を実装するには、
  [Admin API リファレンス](https://chatgpt.com/public/admin/api-reference)と
  [コンプライアンスプラットフォームガイド](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)を開きます。

たとえば、導入状況を手早く確認するにはワークスペースの分析を使用します。Codex の集計レポートをビジネスインテリジェンスシステムに取り込むには Analytics API を、監査可能な記録を SIEM や電子情報開示のワークフローに送信するには Compliance API を使用します。

## 分析ダッシュボード

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT は、ワークスペース全体の導入状況や活用状況を幅広く把握できる分析機能を提供します。Codex の分析は、Codex のアクティビティに焦点を当てています。どちらもインタラクティブなレポート機能であり、未加工の監査ログではありません。

2 つの分析機能を比較し、それぞれの担当者が管理する最新の情報源を確認するには、
[ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)を参照してください。
[ワークスペースの分析](https://chatgpt.com/admin/usage)を直接開くこともできます。
ダッシュボードのラベルやダウンロードしたレポートのフィールドを基に、長期運用を前提とするレポート連携の仕様を定めないでください。
これらは製品の進化に伴って変更される可能性があります。

## 関連する ChatGPT の利用管理

ChatGPT ワークスペースの利用管理は分析とは別の機能であり、機能の利用権限を設定するものではありません。プランによっては、対象の Codex アクティビティで ChatGPT ワークスペースのクレジットが消費される場合があり、利用枠を使い切ると対象機能へのアクセスが一時停止されることがあります。これらの管理機能は、Codex 全体に共通する利用上限を設定するものでも、Platform API の請求を管理するものでもありません。

長期的に有効な適用範囲とヘルプセンターの最新資料については、
[ChatGPT の利用上限と支出管理](/ja-JP/codex/enterprise/usage-limits)を参照してください。

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

プログラムから Codex の集計レポートを取得するには、Analytics API を使用します。データウェアハウスやビジネスインテリジェンスシステムのほか、インタラクティブなダッシュボードに依存すべきではない社内レポートの作成にも適しています。

アクセス要件、ルート、スキーマ、フィールド、レポート対象期間、ページネーションについては、
API リファレンスが正式な情報源です。
連携の基本的な適用範囲と正式なリファレンスへのリンクについては、
[Analytics API](/ja-JP/codex/enterprise/analytics-api)を参照してください。

## Compliance API

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

監査可能な記録を必要とするセキュリティ、法務、ガバナンスのワークフローには、Compliance API を使用します。導入状況や生産性を確認するためのダッシュボードではありません。

対象イベント、スキーマ、権限、フィルター、保持期間、リクエスト時の動作については、
API リファレンスが正式な情報源です。
連携の基本的な適用範囲と正式なリファレンスへのリンクについては、
[Compliance API](/ja-JP/codex/enterprise/compliance-api)を参照してください。

<a id="recommended-pattern"></a>

これらの管理機能のロールアウト順序と検証については、
[管理者向けロールアウトガイド](/ja-JP/codex/enterprise/admin-setup)を参照してください。

## 関連ドキュメント

- [管理者向けロールアウトガイド](/ja-JP/codex/enterprise/admin-setup)
- [ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)
- [Analytics API](/ja-JP/codex/enterprise/analytics-api)
- [Compliance API](/ja-JP/codex/enterprise/compliance-api)
