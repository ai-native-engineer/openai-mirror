<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/plugin/export-findings -->

完了した Codex Security スキャンは、次のいずれかの用途に使用できます：

- **エクスポート** では、ポータブルな JSON、CSV、または SARIF ファイルを作成します。
- **検出結果の追跡** では、選択した検出結果を Linear、GitHub、または Jira の
  イシューとして、あるいは GitHub Security Advisory の非公開ドラフト 1 件として準備します。Codex は
  重複をチェックし、書き込み前に承認を待ちます。

どちらのワークフローでも、封印済みのスキャンバンドルは変更されません。

  利用できるアーティファクトへのリンクとエクスポート形式は、使用する Codex のインターフェースと
  インストール済みプラグインのバージョンによって異なります。[プラグインの
  変更履歴](/ja-JP/codex/security/plugin/changelog) を確認してから、その形式を
  自動化で使用してください。

## ポータブルなアーティファクトのエクスポート

デスクトップアプリで、**セキュリティ** \> **スキャン** から完了済みのスキャンを開きます。
利用可能なアーティファクトへのリンクを使って、`report.md`、`findings.json`、
`scan-manifest.json`、`coverage.json`、または SARIF レポート（存在する場合）を確認します。

別のサポート対象形式を作成するには、封印済みバンドルを変更せず、完了済みスキャンから
検出結果をエクスポートするよう Codex に依頼します：

```text
Export the findings from [completed scan directory] as [JSON, CSV, or SARIF]. Do not modify the sealed scan bundle or upload its contents.

出力先に適した形式を選択します：

| 形式 | 用途                                                        |
| ------ | ----------------------------------------------------------------- |
| JSON   | ツールやスクリプトで利用できるように、封印済みの構造化された検出結果を保持します。    |
| CSV    | 検出結果と現在のローカルトリアージ状態をスプレッドシートで確認します。  |
| SARIF  | SARIF 交換形式に対応したツールへ検出結果を送信します。 |

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    完了済みスキャンから、カバレッジ、検出結果、スキャンマニフェスト、Markdown レポート、または SARIF
アーティファクトを開きます。
  </figcaption>
</figure>

**Markdown レポート** を選択し、`report.md` を設定済みの外部
エディターで開きます。使用されるエディターはシステム設定によって異なります。以下の例では、
生成されたレポートの内容を示しています。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    生成された Markdown レポートで、スキャン範囲、脅威モデル、検証済みの検出結果、および詳細レポートへの
リンクを確認します。
  </figcaption>
</figure>

返されたアーティファクトのパスを使用します。別のツールでスキャンの完全な
コンテキストが必要な場合は、元の `scan-manifest.json`、`findings.json`、および
`coverage.json` をまとめて保管してください。エクスポートしても、検出結果がコードスキャン
サービスにアップロードされることはありません。

## 選択した検出結果の追跡

`$codex-security:track-findings` を、検証済みの検出結果 1 件、または同じ封印済みスキャンから
明示的に選択した最大 25 件の検出結果のバッチとともに実行します。1 回の
実行で使用できるプロバイダーと出力先は、それぞれ 1 つです。GitHub Security
Advisory の非公開ドラフトで受け付けられる検出結果は 1 件だけです。

Linear イシューを準備するには、次の内容を送信します：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for the Linear team [team] and project [project, if
any]. Check for duplicates and show me the exact issue title, body, metadata,
and destination. Do not create or update anything until I approve that payload.

GitHub イシューを準備するには、次の内容を送信します：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for GitHub repository [owner/repository]. Check open
and closed issues for duplicates and show me the exact issue title, body,
metadata, repository visibility, and authenticated transport. Do not create or
update anything until I approve that payload.

Jira イシューを準備するには、次の内容を送信します：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] for Jira project [project key] as [issue type].
Check for duplicates and show me the exact issue summary, description,
metadata, and destination. Do not create or update anything until I approve
that payload.

Jira での追跡には Codex の Atlassian Rovo プラグインが必要です。イシューを再利用するには
読み取りアクセス権が必要で、作成または更新するには読み取りと書き込みの両方のアクセス権が必要です。

GitHub Security Advisory の非公開ドラフトを準備するには、次の内容を送信します：

```text
Use $codex-security:track-findings to prepare finding [finding ID] from
[completed scan directory] as a private draft GitHub Security Advisory in
[owner/repository]. Verify the sealed source revision, repository, affected
paths, package metadata, and duplicate state. Show me the exact advisory
payload, authenticated GitHub CLI identity, and disclosure warnings. Do not
create anything until I approve that payload.

  アドバイザリのドラフトには、封印済みの `git_revision` スキャンで得られた検出結果 1 件、
  検証済みで一般公開されている正規のソースリポジトリ、および管理者権限が必要です。この
  ワークフローでは、アドバイザリの一括処理、更新、公開、クローズはできません。ソースがこれらの要件を満たさない場合は、承認済みの
  非公開イシューの出力先を使用してください。

## 書き込み案のレビュー

1. 検出結果 ID とフィンガープリントが、対象の封印済みスキャンに由来することを確認します。
2. プロバイダー、指定どおりの Linear チーム、GitHub リポジトリ、Jira プロジェクト、または
アドバイザリ用リポジトリと、実際の出力先で現在設定されている公開範囲を確認します。
3. 重複判定の結果を確認します：`create`、`reuse`、`update`、または `blocked`。
4. 提示されたタイトル、本文、ソース内の場所、プロバイダーの
メタデータを漏れなく確認します。出力先で公開すべきでない
エクスプロイトの詳細や内部証拠は削除してください。
5. 提示されたとおりのペイロードだけを承認してください。出力先、公開範囲、検出結果の
セット、または本文に変更がある場合は、新しいプレビューが必要です。

機密性の高い検出結果は非公開の出力先に送信してください。内部または公開の GitHub リポジトリに
イシューを作成する場合は、公開範囲に関する明示的な警告と、内容全体の
承認が必要です。アドバイザリのドラフトの説明は最終的に公開されるものとして
扱い、承認前に認証情報、非公開の証拠、不要な
エクスプロイトの詳細を削除してください。

外部アクションは Codex の会話内でレビューし、承認してください。承認しても、
セキュリティワークベンチに個別のイシュー画面やアドバイザリ画面は作成されません。

## 追跡項目の確認

書き込み案を承認すると、Codex は封印済みのソース、出力先、アクセス権、
重複状態を再確認します。バッチの場合は、検出結果を 1 件ずつ処理し、
不確実な結果が初めて出た時点で停止します。作成、更新、または
再利用が完了するのは、Codex が対象のイシューそのものを読み戻し、その
関連付け識別子と内容を検証した後だけです。

返されたイシューまたはアドバイザリの正規 URL を、トリアージ記録と一緒に保管します。
オーナーがその項目を修正対象として受け入れたら、[検出結果の修正と検証](/ja-JP/codex/security/plugin/fix-findings)
に進みます。
