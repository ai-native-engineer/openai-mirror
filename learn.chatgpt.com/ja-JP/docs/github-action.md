<!-- source: https://learn.chatgpt.com/ja-JP/docs/github-action -->

Codex GitHub Action（`openai/codex-action@v1`）を使用すると、CI/CD ジョブで Codex を実行したり、パッチを適用したり、GitHub Actions ワークフローからレビューを投稿したりできます。
このアクションは Codex CLI をインストールし、API キーを指定すると Responses API プロキシを起動して、指定した権限で `codex exec` を実行します。

次のような場合に、このアクションを使用します：

- CLI を自分で管理することなく、Pull Request やリリースに対する Codex のフィードバックを自動化します。
- Codex による品質チェックを CI パイプラインに組み込み、その結果に基づいて変更を制御します。
- ワークフローファイルから、反復可能な Codex タスク（コードレビュー、リリース準備、移行）を実行します。

CI の例については、[非対話モード](/ja-JP/codex/non-interactive-mode) を参照し、[openai/codex-action リポジトリ](https://github.com/openai/codex-action) でソースコードを確認してください。

## 前提条件

- OpenAI キーを GitHub シークレット（例：`OPENAI_API_KEY`）として保存し、ワークフローから参照します。
- Linux または macOS のランナーでジョブを実行します。Windows では、`safety-strategy: unsafe` を設定します。
- Codex がリポジトリの内容を読み取れるように、アクションを呼び出す前にコードをチェックアウトします。
- 実行するプロンプトを決めます。インラインテキストを `prompt` で指定するか、リポジトリにコミットしたファイルを `prompt-file` で指定できます。

## ワークフロー例

以下のサンプルワークフローでは、新しい Pull Request をレビューして Codex の応答を取得し、その内容を PR に投稿します。

```yaml
name: Codex pull request review
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  codex:
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      final_message: ${{ steps.run_codex.outputs.final-message }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: refs/pull/${{ github.event.pull_request.number }}/merge
          fetch-depth: 0
          persist-credentials: false

      - name: Run Codex
        id: run_codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt-file: .github/codex/prompts/review.md
          output-file: codex-output.md

  post_feedback:
    runs-on: ubuntu-latest
    needs: codex
    if: needs.codex.outputs.final_message != ''
    permissions:
      issues: write
      pull-requests: write
    steps:
      - name: Post Codex feedback
        uses: actions/github-script@v7
        with:
          github-token: ${{ github.token }}
          script: |
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.payload.pull_request.number,
              body: process.env.CODEX_FINAL_MESSAGE,
            });
        env:
          CODEX_FINAL_MESSAGE: ${{ needs.codex.outputs.final_message }}

`.github/codex/prompts/review.md` を独自のプロンプトファイルに置き換えるか、`prompt` 入力でインラインテキストを指定します。この例では、後で確認したりアーティファクトとしてアップロードしたりできるように、Codex の最終メッセージも `codex-output.md` に書き込みます。

## `codex exec` の構成

`codex exec` のオプションに対応するアクションの入力値を設定して、Codex の実行方法を細かく調整します：

- `prompt` または `prompt-file`（いずれか一方を選択）：タスクを記述した Markdown またはテキストファイルへのリポジトリ内パス、あるいはインライン指示を指定します。プロンプトは `.github/codex/prompts/` に保存することを検討してください。
- `codex-args`：追加の CLI フラグ。セッション、プロファイル、MCP 設定を構成するには、JSON 配列（例：`["--ephemeral"]`）またはシェル文字列（`--profile ci`）を指定します。
- `model` および `effort`：使用する Codex のエージェント構成を選択します。空欄にするとデフォルトが使用されます。
- `sandbox`：サンドボックスモード（`workspace-write`、`read-only`、`danger-full-access`）を、実行中に Codex が必要とする権限に合わせます。
- `output-file`：Codex の最終メッセージをディスクに保存し、後続のステップでアップロードや差分比較ができるようにします。
- `codex-version`：特定の CLI リリースを固定して使用します。空欄にすると、公開されている最新バージョンが使用されます。
- `codex-home`：ステップ間で構成ファイルや MCP のセットアップを再利用する場合は、共有の Codex ホームディレクトリを指定します。

## 権限の管理

制限しない限り、GitHub ホステッドランナー上の Codex には広範なアクセス権があります。次の入力でアクセス範囲を制御します：

- `safety-strategy`（デフォルト：`drop-sudo`）は、Codex の実行前に `sudo` を削除します。この変更はジョブ内では元に戻せず、メモリ内のシークレットを保護します。Windows では `safety-strategy: unsafe` を設定する必要があります。
- `unprivileged-user` では、`safety-strategy: unprivileged-user` と `codex-user` を組み合わせ、特定のアカウントで Codex を実行します。そのユーザーがチェックアウトしたリポジトリを読み書きできることを確認してください（所有権の修正方法については、[`unprivileged-user` の例](https://github.com/openai/codex-action/blob/main/examples/unprivileged-user.yml) を参照してください）。
- `read-only` により、Codex はファイルを変更したりネットワークを使用したりできなくなりますが、引き続き昇格された権限で実行されます。シークレットの保護を `read-only` だけに依存しないでください。
- `sandbox` は、Codex 自体のファイルシステムおよびネットワークへのアクセスを制限します。タスクを完了できる範囲で、最も制限の厳しいオプションを選択します。
- `allow-users` と `allow-bots` は、ワークフローをトリガーできるユーザーを制限します。デフォルトでは、書き込み権限を持つユーザーだけがアクションを実行できます。追加で信頼するアカウントを明示的に指定するか、デフォルト動作を使用する場合はフィールドを空欄のままにします。

## 出力の取得

このアクションは、Codex の最終メッセージを `final-message` 出力として返します。上記のようにジョブ出力にマッピングするか、後続のステップで直接処理します。ランナーから完全なトランスクリプトを収集する場合は、`output-file` とアーティファクトのアップロード機能を組み合わせます。構造化データが必要な場合は、`--output-schema` を `codex-args` 経由で渡し、JSON の構造を適用します。

## セキュリティチェックリスト

- ワークフローを開始できるユーザーを制限します。誰でもリポジトリに対して Codex を実行できるようにするのではなく、信頼できるイベントや明示的な承認を優先してください。
- プロンプトインジェクションを防ぐため、Pull Request、コミットメッセージ、イシュー本文からのプロンプト入力をサニタイズします。Codex に渡す前に、HTML コメントや非表示テキストを確認してください。
- `safety-strategy` を `drop-sudo` に維持するか、Codex を非特権ユーザーとして実行して、`OPENAI_API_KEY` を保護します。マルチテナントランナーでは、アクションを `unsafe` モードのままにしないでください。
- 後続のステップが予期しない状態変更を引き継がないように、Codex はジョブの最後のステップとして実行します。
- プロキシログやアクション出力によってシークレット情報が漏えいした可能性がある場合は、直ちにキーをローテーションしてください。

## トラブルシューティング

- **prompt と prompt-file の両方を設定している**：入力元を 1 つだけ指定するように、重複した入力を削除します。
- **responses-api-proxy がサーバー情報を書き込まない**：API キーが存在し、有効であることを確認します。プロキシは `openai-api-key` を指定した場合にのみ起動します。
- **想定では `sudo` が削除されるが、`sudo` が成功した**：前のステップで `sudo` が復元されていないことと、ランナー OS が Linux または macOS であることを確認します。新しいジョブで再実行してください。
- **権限エラー（`drop-sudo` の適用後）**：アクションの実行前に書き込み権限を付与します（例：`chmod -R g+rwX "$GITHUB_WORKSPACE"` を実行するか、unprivileged-user パターンを使用します）。
- **許可されていないトリガーがブロックされた**：デフォルトで許可される書き込み権限を持つコラボレーター以外のサービスアカウントも許可する必要がある場合は、`allow-users` または `allow-bots` の入力を調整します。
