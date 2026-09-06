<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/compliance-api -->

監査可能な記録が必要なセキュリティ、法務、ガバナンス、調査のワークフローには、Compliance API を使用します。導入状況や傾向の測定には、コンプライアンス記録ではなく分析を使用します。

[Admin API リファレンス](https://chatgpt.com/public/admin/api-reference)は、
現在のアクセス要件、イベントの対象範囲、ルート、スキーマ、フィルター、
データ保持、リクエストの動作に関する正式な情報源です。

利用可能なコンプライアンス機能と一般的な連携パターンの概要については、
[コンプライアンスプラットフォームガイド](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)を参照してください。

## Compliance API の利用場面

Compliance API は、次の用途に適しています。

- サポート対象の記録を監査システムまたは調査システムにエクスポート
- 組織のデータ保持およびリーガルホールドのプロセスを適用
- Codex のアクティビティを、ほかのセキュリティデータまたは ID データと関連付け
- セキュリティ、法務、ガバナンスに関する承認済みの調査を支援

Compliance API は生産性ダッシュボードではありません。
コード品質や個人のパフォーマンスの推定には使用しないでください。導入状況のレポートには、[ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)
または [Analytics API](/ja-JP/codex/enterprise/analytics-api) を使用してください。

## はじめに

1. [Admin API リファレンス](https://chatgpt.com/public/admin/api-reference)を開き、
   お使いの管理者ロールで必要なコンプライアンスリソースにアクセスできることを
   確認します。
2. 継続的な収集には、追記専用のコンプライアンスログストリームを使用します。現在サポートされているリソースと取得パターンは、API リファレンスで確認してください。
3. [ログファイルをダウンロード](#download-logs)し、
   非本番環境のセキュリティ情報・イベント管理（SIEM）システムまたはデータレイクへの取り込みをテストします。
4. 継続的に収集するスケジュールを設定し、エクスポートした記録に組織のアクセス、データ保持、リーガルホールドに関する管理ルールを適用します。取得元の保持期間が組織の保持ポリシーに代わるものだと考えないでください。

たとえば、セキュリティチームは、改変不可能なコンプライアンスイベントを調査のために SIEM にストリーミングしたり、承認された電子情報開示ワークフローに転送したりできます。現在のルートとスキーマについては、このガイドからエンドポイントの仕様をコピーするのではなく、API リファレンスを参照してください。

### ログのダウンロード

[Bash スクリプト](/downloads/compliance-api/download_compliance_files.sh)
または [PowerShell スクリプト](/downloads/compliance-api/download_compliance_files.ps1)をダウンロードします。
どちらのスクリプトも、ページネーションをたどって、指定したタイムスタンプより後の利用可能なログファイルをすべて一覧表示してダウンロードし、
JSONL を標準出力に書き込みます。エラーは標準エラー出力に書き込まれます。

`COMPLIANCE_API_KEY` に Enterprise Compliance API キーを設定します。
`<workspace_or_org_id>` は ChatGPT ワークスペース ID または API プラットフォームの組織 ID に、
`<after>` はタイムゾーンを含む ISO 8601 形式のタイムスタンプに置き換えます。
この例では、`AUTH_LOG` ファイルを 100 件ずつ取得します。

macOS または Linux では、Bash、`curl`、`jq` をインストールしてから、次のコマンドを実行します。

```bash
bash ./download_compliance_files.sh "<workspace_or_org_id>" AUTH_LOG 100 "<after>" > output.jsonl

Windows 用スクリプトは PowerShell 5.1 以降に対応しています。ダウンロードしたファイルの内容を確認してください。
Windows によってブロックされていて、組織の実行ポリシーで許可されている場合は、
`Unblock-File -Path .\download_compliance_files.ps1` を実行します。この例では、
PowerShell 7 を使用して、バイトオーダーマークなしの UTF-8 で保存します。

```powershell
.\download_compliance_files.ps1 "<workspace_or_org_id>" AUTH_LOG 100 "<after>" |
  Set-Content -Encoding utf8NoBOM output.jsonl

## 管理範囲の確認

コンプライアンスの対象範囲は、ChatGPT ワークスペースと、現在の API リファレンスに記載された製品に基づきます。API プラットフォームの組織データには、API データと管理に関する独自の制御が適用されます。

現在のルート、イベントの対象範囲、スキーマ、フィルター、データ保持の仕組み、権限要件、リクエストの処理方法に関する正式な情報源は、API リファレンスです。このページでは、その仕様を重複して記載しません。

## 関連ドキュメント

- [ワークスペースの分析](/ja-JP/codex/enterprise/workspace-analytics)
- [管理者向けロールアウトガイド](/ja-JP/codex/enterprise/admin-setup)
- [ガバナンス](/ja-JP/codex/enterprise/governance)
- [Analytics API](/ja-JP/codex/enterprise/analytics-api)
