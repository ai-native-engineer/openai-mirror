<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/workspace-analytics -->

ワークスペース全体の導入状況を把握するには、ChatGPT ワークスペースの分析を使用します。Codex に特化したレポートには Codex 分析を使用します。プログラムから集計データを取得するには Analytics API を、監査可能な記録には Compliance API を使用します。

これらのレポート手段は、プロダクトへのアクセス権を付与したり、実行時のポリシーを設定したりするものではありません。
管理の範囲については、[ロールとワークスペースの権限](/ja-JP/codex/enterprise/roles-and-workspace-permissions)
を参照してください。

## レポート手段の選択

| レポート手段                     | 用途                                                    | 仕様の管理元                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ChatGPT ワークスペースの分析 | ワークスペース全体の導入状況と活用状況を確認できるインタラクティブなレポート | [ワークスペースの分析に関するヘルプセンターのガイド](https://help.openai.com/en/articles/10875114)                               |
| Codex 分析             | Codex の導入状況とアクティビティに特化したインタラクティブなレポート  | 認証後に利用できる [Codex 分析ダッシュボード](https://admin.openai.com/analytics/codex)                                |
| Analytics API               | プログラムから利用できる Codex の集計レポート                      | [Codex Analytics API リファレンス](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| Compliance API              | 監査、セキュリティ、法務、調査に関する記録             | [Admin API リファレンス](https://chatgpt.com/public/admin/api-reference)                                              |

## ChatGPT ワークスペースの分析のレビュー

ChatGPT ワークスペースの分析では、対応するワークスペース機能全体の導入状況と活用状況をインタラクティブに確認できます。
提供状況、ロール、ダッシュボードのセクション、データの鮮度、プライバシーの取り扱い、エクスポート形式は変更される場合があります。
現在の対象範囲と手順については、
[ChatGPT Enterprise および Edu 向けワークスペースの分析](https://help.openai.com/en/articles/10875114)
を参照してください。

ダウンロードしたレポートは、個人を識別できる組織データとして扱ってください。エクスポートしたデータにも集計ダッシュボードと同じプライバシー上の特性があると考えず、組織のアクセス、保存、保持に関するポリシーを適用してください。

## Codex 分析のレビュー

認証後に利用できる [Codex 分析ダッシュボード](https://admin.openai.com/analytics/codex)は、Codex のレポートに特化しています。
スキーマの安定性を保証するものとはみなさず、データをインタラクティブに探索するために使用してください。
ダッシュボードのカテゴリ、フィールド、フィルター、エクスポート形式は、
このページの更新とは関係なく変更される場合があります。

レポートを自動化するには、[Analytics API](/ja-JP/codex/enterprise/analytics-api) を使用し、
その API リファレンスに従ってください。監査可能な記録には、
[Compliance API](/ja-JP/codex/enterprise/compliance-api) を使用してください。

## レポートデータの解釈

次の点に留意してください。

- ChatGPT ワークスペースの分析と Codex 分析では、対象となるプロダクトの範囲が異なります。
- 集計された分析データと監査記録は目的が異なり、それぞれ別の仕様に従います。
- 分析はアクティビティを示すものであり、アクセス権を付与したり、実行時の権限を変更したりするものではありません。
- [ChatGPT の利用上限と支出管理](/ja-JP/codex/enterprise/usage-limits)は、
  ワークスペースに適用される別の制約であり、プランによって異なります。
