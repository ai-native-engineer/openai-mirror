<!-- source: https://learn.chatgpt.com/ja-JP/docs/non-interactive-mode -->

非対話モードでは、対話型 TUI を開かずに、スクリプト（継続的インテグレーション（CI）ジョブなど）から Codex を実行できます。
`codex exec` で起動します。

各フラグの詳細については、[`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec) を参照してください。

## `codex exec` の使用場面

Codex で次のことを行う場合は、`codex exec` を使用します：

- パイプライン（CI、マージ前チェック、スケジュール済みジョブ）の一部として実行
- 他のツールにパイプできる出力を生成（リリースノートや要約の作成など）
- コマンドの出力を Codex に渡し、Codex の出力を他のツールに渡す CLI ワークフローに自然に統合
- 事前に明示したサンドボックス設定と承認設定で実行

## 基本的な使い方

タスクのプロンプトを 1 つの引数として渡します：

```bash
codex exec "summarize the repository structure and list the top 5 risky areas"

`codex exec` の実行中、Codex は進行状況を `stderr` に逐次出力し、エージェントの最終メッセージだけを `stdout` に出力します。そのため、最終結果を簡単にリダイレクトしたり、パイプで渡したりできます：

```bash
codex exec "generate release notes for the last 10 commits" | tee release-notes.md

セッションのロールアウトファイルをディスクに保存したくない場合は、`--ephemeral` を使用します：

```bash
codex exec --ephemeral "triage this repository and suggest next steps"

stdin へのパイプ入力とプロンプト引数を併用すると、Codex はプロンプトを指示として、パイプ入力の内容を追加のコンテキストとして扱います。

これにより、1 つのコマンドで入力を生成し、そのまま Codex に渡せます：

```bash
curl -s https://jsonplaceholder.typicode.com/comments \
  | codex exec "format the top 20 items into a markdown table" \
  > table.md

stdin の高度なパイプ処理パターンについては、[stdin の高度なパイプ処理](#advanced-stdin-piping)を参照してください。

## 権限と安全性

`codex exec` は、デフォルトでは読み取り専用のサンドボックスで実行されます。自動化では、ワークフローに必要な最小限の権限を設定します：

- 編集を許可：`codex exec --sandbox workspace-write "<task>"`
- より広範なアクセスを許可：`codex exec --sandbox danger-full-access "<task>"`

`danger-full-access` は、管理下にある環境（隔離された CI ランナーやコンテナなど）でのみ使用してください。

Codex は `codex exec --full-auto` を互換性維持のための非推奨フラグとして残しており、警告を表示します。新しいスクリプトでは、明示的な `--sandbox workspace-write` フラグを使用してください。

`--ignore-user-config` は、`$CODEX_HOME/config.toml` を読み込まずに実行する必要がある場合に使用します。`--ignore-rules` は、管理下にある自動化環境でユーザーおよびプロジェクトの execpolicy `.rules` ファイルをスキップする必要がある場合に使用します。

有効な MCP サーバーに `required = true` を設定し、その初期化に失敗した場合、`codex exec` はそのサーバーなしで処理を続行せず、エラーで終了します。

## 機械可読な形式での出力

スクリプトで Codex の出力を処理するには、JSON Lines 形式の出力を使用します：

```bash
codex exec --json "summarize the repo structure" | jq

`--json` を有効にすると、`stdout` は JSON Lines（JSONL）ストリームになり、実行中に Codex が出力するすべてのイベントを取得できます。イベントタイプには、`thread.started`、`turn.started`、`turn.completed`、`turn.failed`、`item.*`、`error` があります。

アイテムタイプには、エージェントメッセージ、推論、コマンド実行、ファイル変更、MCP ツール呼び出し、ウェブ検索、プランの更新があります。

JSON ストリームの例（各行は 1 つの JSON オブジェクト）：

```jsonl
{"type":"thread.started","thread_id":"0199a213-81c0-7800-8aa1-bbab2a035a53"}
{"type":"turn.started"}
{"type":"item.started","item":{"id":"item_1","type":"command_execution","command":"bash -lc ls","status":"in_progress"}}
{"type":"item.completed","item":{"id":"item_3","type":"agent_message","text":"Repo contains docs, sdk, and examples directories."}}
{"type":"turn.completed","usage":{"input_tokens":24763,"cached_input_tokens":24448,"output_tokens":122,"reasoning_output_tokens":0}}

最終メッセージだけが必要な場合は、`-o <path>`/`--output-last-message <path>` を使用してファイルに書き込みます。最終メッセージはファイルに書き込まれ、引き続き `stdout` にも出力されます（詳細は [`codex exec`](/codex/developer-commands?surface=cli#cli-codex-exec) を参照してください）。

## スキーマを使用した構造化出力の作成

後続のステップで構造化データが必要な場合は、`--output-schema` を使用して、JSON Schema に準拠する最終応答をリクエストします。
これは、固定のフィールドが必要な自動化ワークフロー（ジョブの要約、リスクレポート、リリースメタデータなど）に役立ちます。

`schema.json`

```json
{
  "type": "object",
  "properties": {
    "project_name": { "type": "string" },
    "programming_languages": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": ["project_name", "programming_languages"],
  "additionalProperties": false
}

スキーマを指定して Codex を実行し、最終的な JSON 応答をディスクに書き込みます：

```bash
codex exec "Extract project metadata" \
  --output-schema ./schema.json \
  -o ./project-metadata.json

最終出力の例（stdout）：

```json
{
  "project_name": "Codex CLI",
  "programming_languages": ["Rust", "TypeScript", "Shell"]
}

## 自動化における認証

`codex exec` は、デフォルトで保存済みの CLI 認証情報を再利用します。CI では、認証情報を明示的に指定するのが一般的です：

信頼できるクラウド環境または CI ランタイムで、すでに有効期間の短いワークロードトークンを受け取っている場合は、
OpenAI の認証情報を保存する代わりに、
[ワークロード ID フェデレーション](/ja-JP/codex/enterprise/workload-identity)を使用して
認証してください。

### API キー認証の使用

GitHub Actions では、CLI を自分でインストールして認証する代わりに、[Codex GitHub Action](/ja-JP/codex/github-action) を使用してください。このアクションは、Codex をインストールし、Responses API プロキシを起動して、設定可能な安全性戦略に従って Codex を実行することで、API キーの露出を抑えるよう設計されています。

リポジトリ管理下のコードをチェックアウトまたは実行するワークフローでは、`OPENAI_API_KEY` や `CODEX_API_KEY` をジョブレベルの環境変数として設定しないでください。同じジョブ内のビルドスクリプト、テスト、依存関係のライフサイクルフック、または侵害されたアクションから、これらの環境変数を読み取れるためです。

その他の自動化環境では、`CODEX_API_KEY` は必要な Codex の呼び出しにのみ設定し、
同じプロセス環境で信頼できないコードが
実行されないようにしてください。

1 回の実行だけ別の API キーを使用するには、`CODEX_API_KEY` をインラインで設定します：

```bash
CODEX_API_KEY=<api-key> codex exec --json "triage open bug reports"

`CODEX_API_KEY` は、`codex exec`、`codex review`、TypeScript SDK、
`codex exec-server --remote` で使用できます。

API キーではなく Codex ユーザーアカウントで CI/CD ジョブを実行する必要がある場合は、
このセクションを参照してください。たとえば、信頼できるランナーで ChatGPT 管理の Codex アクセスを使用するエンタープライズチームや、
API キーではなく ChatGPT/Codex のレート制限が適用される形で利用する必要があるユーザーが該当します。

API キーはプロビジョニングとローテーションが容易なため、
自動化では API キーをデフォルトで使用するのが適切です。
この方法は、自身の Codex アカウントとして実行する必要が明確にある場合にのみ使用してください。

`~/.codex/auth.json` にはアクセストークンが含まれているため、パスワードと同様に扱ってください。
コミットしたり、チケットに貼り付けたり、チャットで共有したりしないでください。

このワークフローを公開リポジトリやオープンソースリポジトリで使用しないでください。ランナーで `codex login` を
使用できない場合は、安全なストレージを介して `auth.json` を配置し、
ランナー上で Codex を実行して、Codex がファイルを元の場所で更新するようにします。
更新されたファイルは、次回以降の実行でも使用できるよう永続化してください。

[CI/CD での Codex アカウント認証の維持（上級）](/codex/auth/ci-cd-auth)を参照してください。

## 非対話セッションの再開

前回の実行を続行する必要がある場合（2 段階のパイプラインなど）は、`resume` サブコマンドを使用します：

```bash
codex exec "review the change for race conditions"
codex exec resume --last "fix the race conditions you found"

`codex exec resume <SESSION_ID>` を使用して、特定のセッション ID を指定することもできます。

## Git リポジトリが必要

破壊的な変更を防ぐため、Codex では Git リポジトリ内でコマンドを実行する必要があります。環境の安全性を確信できる場合は、`codex exec --skip-git-repo-check` を使用してこのチェックを無効にできます。

## 一般的な自動化パターン

### 例：GitHub Actions での CI エラーの自動修正

GitHub Actions のワークフローでは、Codex をインストールして API キーをシェルステップに渡す代わりに、[`openai/codex-action`](https://github.com/openai/codex-action) を使用してください。このアクションは、OpenAI API キー用の安全なプロキシを起動します。

CI ワークフローが失敗したときに、Codex を使用して修正案を自動的に提案できます。流れは次のとおりです：

1. メインの CI ワークフローがエラーで終了したときに後続のワークフローをトリガー
2. リポジトリの読み取り権限のみで、失敗したコミットをチェックアウト
3. Codex の実行前に、OpenAI API キーを各ステップに公開せずにセットアップコマンドを実行
4. Codex GitHub Action を実行
5. Codex によるローカルの変更をパッチアーティファクトとして保存
6. 別のジョブでパッチを適用し、Pull Request を作成します。

以下の Codex ジョブに付与される権限は `contents: read` のみです。Codex の実行後は、差分だけをシリアライズしてアーティファクトにします。一方、`open_pr` ジョブにはリポジトリへの書き込み権限が付与されますが、`OPENAI_API_KEY` は渡されません。

この例では Node.js プロジェクトを前提としています。お使いの技術スタックに合わせて、セットアップコマンドとテストコマンドを調整してください。

詳しいセキュリティチェックリストについては、[Codex GitHub Action のセキュリティガイダンス](https://github.com/openai/codex-action/blob/main/docs/security.md)を参照してください。

```yaml
name: Codex auto-fix on CI failure

on:
  workflow_run:
    workflows: ["CI"]
    types: [completed]

jobs:
  generate_fix:
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    runs-on: ubuntu-latest
    permissions:
      contents: read
    outputs:
      has_patch: ${{ steps.diff.outputs.has_patch }}
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: |
          if [ -f package-lock.json ]; then npm ci; fi

      - name: Run Codex
        uses: openai/codex-action@v1
        with:
          openai-api-key: ${{ secrets.OPENAI_API_KEY }}
          prompt: |
            The CI workflow "${{ github.event.workflow_run.name }}" failed for commit
            ${{ github.event.workflow_run.head_sha }}.

            Run `npm test --silent` to reproduce the failure. Identify the minimal
            change needed to make the tests pass, implement only that change, and
            run `npm test --silent` again.

            Do not refactor unrelated files.

      - name: Create patch artifact
        id: diff
        run: |
          git add -N .
          git diff --binary HEAD > codex.patch
          if [ -s codex.patch ]; then
            echo "has_patch=true" >> "$GITHUB_OUTPUT"
          else
            echo "has_patch=false" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload patch artifact
        if: steps.diff.outputs.has_patch == 'true'
        uses: actions/upload-artifact@v4
        with:
          name: codex-fix-patch
          path: codex.patch
          if-no-files-found: error

  open_pr:
    runs-on: ubuntu-latest
    needs: generate_fix
    if: needs.generate_fix.outputs.has_patch == 'true'
    permissions:
      contents: write
      pull-requests: write
    steps:
      - uses: actions/checkout@v5
        with:
          ref: ${{ github.event.workflow_run.head_sha }}
          fetch-depth: 0

      - uses: actions/download-artifact@v4
        with:
          name: codex-fix-patch

      - name: Apply Codex patch
        run: git apply --index codex.patch

      - name: Open pull request
        env:
          GH_TOKEN: ${{ github.token }}
          FAILED_HEAD_BRANCH: ${{ github.event.workflow_run.head_branch }}
          FAILED_HEAD_SHA: ${{ github.event.workflow_run.head_sha }}
          RUN_ID: ${{ github.event.workflow_run.run_id }}
        run: |
          branch="codex/auto-fix-$RUN_ID"

          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git switch -c "$branch"
          git commit -m "Auto-fix failing CI via Codex"
          git push origin "$branch"

          {
            echo "Codex generated this patch after CI failed for \`$FAILED_HEAD_SHA\`."
            echo
            echo "Review the changes before merging."
          } > pr-body.md

          gh pr create \
            --base "$FAILED_HEAD_BRANCH" \
            --head "$branch" \
            --title "Auto-fix failing CI via Codex" \
            --body-file pr-body.md

## 上級者向けの stdin パイプ処理

別のコマンドが Codex への入力を生成する場合は、指示をどこから与えるかに応じて stdin の利用パターンを選びます。指示があらかじめ決まっており、パイプ経由の出力をコンテキストとして渡す場合は、prompt-plus-stdin を使用します。stdin をプロンプト全体として扱う場合は、`codex exec -` を使用します。

### prompt-plus-stdin の使用

prompt-plus-stdin は、Codex に確認させたいデータを別のコマンドですでに生成している場合に便利です。このモードでは、自分で指示を記述し、出力をコンテキストとしてパイプ経由で渡します。そのため、コマンド出力、ログ、生成データを中心とした CLI ワークフローに適しています。

```bash
npm test 2>&1 \
  | codex exec "summarize the failing tests and propose the smallest likely fix" \
  | tee test-summary.md

### ログの要約

```bash
tail -n 200 app.log \
  | codex exec "identify the likely root cause, cite the most important errors, and suggest the next three debugging steps" \
  > log-triage.md

### TLS または HTTP の問題の調査

```bash
curl -vv https://api.example.com/health 2>&1 \
  | codex exec "explain the TLS or HTTP failure and suggest the most likely fix" \
  > tls-debug.md

### Slack 投稿用の状況報告の作成

```bash
gh run view 123456 --log \
  | codex exec "write a concise Slack-ready update on the CI failure, including the likely cause and next step" \
  | pbcopy

### CI ログに基づく Pull Request コメントの下書き

```bash
gh run view 123456 --log \
  | codex exec "summarize the failure in 5 bullets for the pull request thread" \
  | gh pr comment 789 --body-file -

### `codex exec -` の使用（stdin がプロンプトの場合）

プロンプト引数を省略すると、Codex は stdin からプロンプトを読み取ります。この動作を明示的に指定する場合は、`codex exec -` を使用します。

別のコマンドやスクリプトでプロンプト全体を動的に生成する場合は、`-` センチネルが便利です。これは、プロンプトをファイルに保存する場合や、シェルスクリプトでプロンプトを組み立てる場合、リアルタイムのコマンド出力と指示を組み合わせてからプロンプト全体を Codex に渡す場合に適しています。

```bash
cat prompt.txt | codex exec -

```bash
printf "Summarize this error log in 3 bullets:\n\n%s\n" "$(tail -n 200 app.log)" \
  | codex exec -

```bash
generate_prompt.sh | codex exec - --json > result.jsonl
