<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/plugin/fix-findings -->

Codex Security を使用して、承認済みのセキュリティ検出事項を、対象を絞った
検証済みのパッチに変換します。Codex Security のワークベンチで作業することも、プロンプト、コマンドライン、CI/CD から修正
ワークフローを実行することもできます。Codex は問題を検証し、
テストを安全かつ現実的に実施できる場合は、修正前には失敗し、修正後には成功する、対象を絞った回帰テストを
追加します。また、正当な
動作が引き続き機能することも確認します。回帰テストが安全でないか実行できない場合、Codex は
検証上の不足を記録し、代わりに反復可能な最も強力な検証
アーティファクトを提示します。

まず、承認済みの検出事項を 1 件選び、提案されたパッチと検証
エビデンスをレビューします。ワークフローが基準を満たしている場合は、ほかの承認済み
検出事項を 1 件ずつ、個別の Codex タスクまたは CI/CD ジョブで処理します。各タスクの
対象範囲を限定すると、コード変更とエビデンスをレビューしやすくなります。

## UI での検出事項の修正

承認済みの検出事項を **検出事項** から開くか、**スキャン** にある完了済みのスキャンから開きます。
そのエビデンスを確認してから、**パッチ** を使用して、
対象を絞った修正を 1 件生成し、レビュー、適用、検証します。

1. 対象を絞ったパッチの生成

   検出事項を開いて、 **パッチ** タブを選択し、続いて **パッチを生成** を選択します。
   Codex は、可能な場合は問題を検証または再現し、選択したチェックアウトを変更せずに、
   パッチアーティファクトを作成します。

2. 提案された差分のレビュー

   変更されたソースコード、回帰テスト、検証アーティファクトをすべて確認します。
広範なリファクタリング、無関係なクリーンアップ、または別のセキュリティ
制御を弱める変更は却下します。

3. パッチのローカル適用

   差分に問題がないことを確認してから、 **パッチを適用** を選択します。Codex は、
   生成されたパッチをそのまま作業ツリーに適用し、その状態を記録します。続行する前に、
   作業ツリーの差分をレビューしてください。

4. 修正の検証

   **修正を検証** を選択します。Codex は、元の再現手順または利用可能な中で最も強力な
   エクスプロイト検査を再実行します。回帰テストを安全かつ現実的に実施できる場合、Codex は、
   そのテストが修正前には失敗し、修正後には成功することを確認します。テストが
   安全でないか実行できない場合は、検証上の不足を記録し、代わりに
   反復可能な最も強力な検証アーティファクトを提示します。また、
   正当な動作、類似のバイパス経路、関連するリポジトリのテストも確認します。

5. 検出事項の明示的なクローズ

   検証によって検出事項が自動的にクローズされることはありません。コマンド、
結果、残っている検証上の不足を確認してから、正確な
理由を指定して検出事項をクローズするか、追加対応のためにオープンのままにします。

<figure className="not-prose my-8">
  
  <figcaption className="mt-3 text-sm text-secondary">
    生成されたセキュリティ修正をチェックアウトに適用する前に、レビューしてください。
  </figcaption>
</figure>

## CLI での検出事項の修正

スキャン、チケット、アドバイザリ、
脆弱性開示、セキュリティ評価、または内部レビューから得られた承認済みの検出事項には、Codex CLI を使用します。

これらのコマンドを実行する前に、`CODEX_HOME`（`codex exec` が使用する場所）に Codex Security を
インストールしてください。新しい CI ランナーには、マーケットプレイスのプラグインがデフォルトでは
含まれていません。

```text
Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.

既知のソース、シンク、攻撃者の入力、影響、期待される不変条件、
再現手順、影響を受けるファイル、検証コマンドを含めてください。不足している技術的な詳細は、Codex が
リポジトリを調べて確認できます。ただし、製品ポリシーや想定される
セキュリティ不変条件を推測する前に、確認を求める必要があります。

自動実行では、コードをチェックアウトし、検出事項レポートを参照できるようにして、
ランナーの `CODEX_HOME` にプラグインをインストールします。続いて、ワークスペースへの
書き込みを有効にし、プロンプトを `codex exec` に渡します:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <report-path>. Validate the issue, make the smallest safe change, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

## CI/CD での検出事項のスキャンと修正

いずれかのスキルを呼び出す前に、ランナーの `CODEX_HOME` に Codex Security を
インストールしてください。以下のコマンドはインストール済みのプラグインを使用するだけで、プラグイン自体はインストールしません。

CI/CD では、変更内容のスキャンと修正処理を分け、スキャンでは
チェックアウトを変更しないことを必須にします。完了したスキャンのディレクトリをジョブの
アーティファクトとして保存し、検出事項をレビューしたうえで、修正対象として承認された
検出事項ごとに、個別の Codex タスクまたはジョブを開始します。

`codex exec` は、デフォルトで読み取り専用のサンドボックスを使用します。変更内容のスキャンと
修正処理の両方を `--sandbox workspace-write` で実行してください。スキャンには、一時アーティファクトを保存するためにこの権限が
必要ですが、プロンプトでは引き続き `Do not modify
the checkout` を要件として明記する必要があります。修正処理には、対象を絞った
パッチと検証エビデンスを書き込むために同じ権限が必要です。詳しくは、 [権限と
安全性](/ja-JP/codex/non-interactive-mode#permissions-and-safety) を参照してください。

各スキャンと承認済みの各検出事項について:

1. 変更のベースリビジョンとヘッドリビジョンを特定します。
2. チェックアウトを変更せずに、その差分に対して `$codex-security:security-diff-scan` を
   実行します。
3. スキャンディレクトリ全体を保存し、修正する検出事項を選択します。
4. 承認済みの検出事項ごとに `$codex-security:fix-finding` を 1 回呼び出し、その
   検出事項 ID と完了したスキャンのディレクトリを渡します。
5. 対象を絞ったパッチを 1 つ生成し、修正前には失敗して修正後には
成功する回帰テストを追加します。そのテストが安全でないか実行できない場合は、
検証上の不足を記録し、代わりに反復可能な最も強力な検証アーティファクトを使用します。
6. 元の問題と正当な動作を検証します。パッチ、テストまたは代替の検証アーティファクト、
検証コマンド、検証上の不足がある場合はその内容を、検出事項ごとに
個別に返します。

まず、チェックアウトを変更せずに変更内容をスキャンします:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:security-diff-scan to review changes from <base-revision> to <head-revision> for security regressions. Do not modify the checkout.'

次に、完了したスキャンに含まれる承認済みの検出事項を 1 件修正します:

```bash
codex exec --sandbox workspace-write 'Use $codex-security:fix-finding to fix finding <finding-id> from <completed-scan-directory>. Validate the finding, generate one minimal patch, and add a focused regression test that fails before the fix and passes after it. If that test is unsafe or infeasible, record the proof gap and provide the strongest repeatable validation artifact instead. Verify that the issue no longer reproduces.'

残っている承認済みの検出事項ごとに、2 番目のコマンドを個別のタスクまたはジョブで
繰り返します。検証後、通常のコードレビューとリリースプロセスを通じて各パッチを
マージします。修正前に検出事項を別のチームへ引き渡す方法については、
[検出事項のエクスポートまたは
追跡](/ja-JP/codex/security/plugin/export-findings) を参照してください。
