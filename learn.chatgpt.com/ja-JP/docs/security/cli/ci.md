<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli/ci -->

CI で Codex Security CLI を実行し、Pull Request またはマージリクエストの変更内容を正確にレビューして、検出結果とカバレッジを保持します。必要に応じて、指定した重大度を基準にチェックを失敗させることもできます。まずは結果を参考情報として確認し、スキャンの品質と実行時間を評価したうえで、リポジトリに適した重大度ポリシーを追加してください。

  公開されている `@openai/codex-security` パッケージをインストールします。
  スキャンの実行には、引き続き Codex Security へのアクセス権が必要です。

このガイドでは、GitHub Actions と GitLab CI/CD の例を紹介します。同じスキャンコマンドとエクスポートコマンドは、ほかの CI システムでも使用できます。

## ワークフローの準備

CI プロバイダーのシークレットストアに、OpenAI API キーを
`CODEX_SECURITY_API_KEY` という名前で保存します。

このシークレットを、スキャンステップの環境変数 `OPENAI_API_KEY` に直接割り当てます。
認証情報を利用できる範囲はスキャンプロセスに限定し、
`--auth api-key` で明示的に選択します。

ワークフローは、信頼できるリポジトリと Pull Request に対してのみ実行してください。スキャンはランナーのローカル権限で実行され、承認を待って一時停止することはありません。スキャンプロセスはジョブの環境を継承する可能性があるため、無関係なトークンやクラウド認証情報をジョブの環境に含めないでください。

ランナーには次のものが必要です：

- Node.js 22（22.13.0 以降）、24、または 26
- Python 3.10 以降
- リポジトリのチェックアウト先の外部にインストールした公開済みの
  `@openai/codex-security` パッケージ
- Git がマージベースを計算するために必要な、Pull Request またはマージリクエストの head と base の履歴

## GitHub Actions ワークフローの追加

非公開または内部リポジトリでは、SARIF をアップロードする前に
[GitHub Code Security](https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github)
を有効にしてください。

`.github/workflows/codex-security.yml` を作成します。
Pull Request をチェックアウトする前に、`@openai/codex-security` を
`$RUNNER_TEMP/codex-security` 配下にインストールし、信頼できる実行可能ファイルを
`$RUNNER_TEMP/codex-security/node_modules/.bin/codex-security` で利用できるようにします：

```yaml
name: Codex Security scan

on:
  pull_request:

jobs:
  codex-security:
    if: github.event.pull_request.head.repo.full_name == github.repository && github.actor != 'dependabot[bot]'
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    steps:
      - name: Set up Node.js
        uses: actions/setup-node@820762786026740c76f36085b0efc47a31fe5020 # v7
        with:
          node-version: "26"

      - name: Set up Python
        uses: actions/setup-python@5fda3b95a4ea91299a34e894583c3862153e4b97 # v7
        with:
          python-version: "3.14"

      - name: Install Codex Security
        run: |
          set -euo pipefail
          npm install \
            --prefix "$RUNNER_TEMP/codex-security" \
            --ignore-scripts \
            --no-audit \
            --no-fund \
            @openai/codex-security

      - name: Verify Codex Security
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
        run: |
          set -euo pipefail
          test -x "$CODEX_SECURITY_BIN"
          "$CODEX_SECURITY_BIN" --version

      - name: Check out the pull request
        uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1 # v7
        with:
          ref: ${{ github.event.pull_request.head.sha }}
          fetch-depth: 0
          persist-credentials: false

      - name: Scan the pull request
        env:
          OPENAI_API_KEY: ${{ secrets.CODEX_SECURITY_API_KEY }}
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          CODEX_SECURITY_STATE_DIR: ${{ runner.temp }}/codex-security-state
          BASE_SHA: ${{ github.event.pull_request.base.sha }}
          HEAD_SHA: ${{ github.event.pull_request.head.sha }}
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
        run: |
          set -euo pipefail
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          "$CODEX_SECURITY_BIN" scan . \
            --diff "$BASE_REVISION" \
            --head "$HEAD_SHA" \
            --auth api-key \
            --output-dir "$SCAN_DIR" \
            --json > "$RUNNER_TEMP/codex-security.json"

      - name: Export SARIF
        id: export-sarif
        if: always()
        env:
          CODEX_SECURITY_BIN: ${{ runner.temp }}/codex-security/node_modules/.bin/codex-security
          SCAN_DIR: ${{ runner.temp }}/codex-security-results
          SARIF_FILE: ${{ runner.temp }}/codex-security.sarif
        run: |
          set -euo pipefail
          if test -f "$SCAN_DIR/scan-manifest.json"; then
            "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
              --export-format sarif \
              --source-root "$GITHUB_WORKSPACE" \
              --output "$SARIF_FILE"
            echo "available=true" >> "$GITHUB_OUTPUT"
          fi

      - name: Upload SARIF
        if: always() && steps.export-sarif.outputs.available == 'true'
        uses: github/codeql-action/upload-sarif@e4fba868fa4b1b91e1fdab776edc8cfbe6e9fb81 # v4
        with:
          sarif_file: ${{ runner.temp }}/codex-security.sarif
          ref: refs/pull/${{ github.event.pull_request.number }}/head
          sha: ${{ github.event.pull_request.head.sha }}
          category: codex-security

      - name: Preserve scan results
        if: always()
        uses: actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a # v7
        with:
          name: codex-security-results
          path: |
            ${{ runner.temp }}/codex-security-results
            ${{ runner.temp }}/codex-security.json
          if-no-files-found: warn
          retention-days: 7

ワークフローは Pull Request の head をチェックアウトし、マージベースを計算して、
その 2 つのリビジョン間のコミット済みの変更をスキャンします。
履歴全体を取得することで、対象を正確に特定できます。`persist-credentials: false` を設定すると、
チェックアウトしたリポジトリの Git 構成にリポジトリトークンが保存されなくなります。
チェックアウト前に CLI をインストールして絶対パスで実行することで、
リポジトリ側で制御される実行可能ファイルにスキャンの認証情報が渡るのを防ぎます。`--auth api-key` により、
スコープを限定した API キーを明示的に選択します。
スキャン履歴は、リポジトリ外の書き込み可能な状態保存用ディレクトリに保存されます。

`--json` は完全な JSON ドキュメントを 1 つ stdout に書き込むため、
ワークフローでそのまま保存できます。進捗、完了時の概要、エラーは引き続き stderr に出力されます。
これは、JSON Lines のイベントストリームを出力する `codex exec --json` とは異なります。

エクスポートステップでは、完了・封印済みのスキャン結果を読み込み、SARIF を書き出します。Codex のランタイムや認証情報には変更を加えません。スキャンのアーティファクトには、脆弱性を含むソースコードの断片、根拠、修正の詳細が含まれる場合があります。リポジトリに適したアクセス制御と短い保持期間を設定してください。

## GitLab CI/CD パイプラインの追加

保護されたデフォルトブランチのスキャン、任意で有効化するディープスキャンのスケジュール実行、
SARIF ポリシーに基づく独立した合否判定、オプションの検証済みドラフトマージリクエストを含む
本番用ワークフローについては、[GitLab CI/CD での
Codex Security の実行](/ja-JP/codex/security/cli/ci/gitlab)を参照してください。

GitLab Ultimate 19.2 以降では、
[SARIF 2.1.0 レポート](https://docs.gitlab.com/ci/yaml/artifacts_reports/#artifactsreportssarif)を取り込めます。
パイプラインを実行する前に、マスクおよび非表示に設定した CI/CD 変数
`CODEX_SECURITY_API_KEY` を追加してください。

次の最小構成の例では、スキャン専用の `security` ジョブを
ルートの `.gitlab-ci.yml` に追加します。ファイル内の既存のステージとジョブはそのまま残してください。
デフォルトではマージリクエストの変更をスキャンします。`CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` を
`"true"` に設定すると、デフォルトブランチ全体もスキャンできます：

```yaml
variables:
  CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH: "false"

stages:
  - test
  - security

codex-security:
  stage: security
  image: node:26-bookworm-slim
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event" && $CI_MERGE_REQUEST_SOURCE_PROJECT_ID == $CI_PROJECT_ID'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "diff"
    - if: '$CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH && $CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH == "true"'
      variables:
        CODEX_SECURITY_SCAN_SCOPE: "full"
  variables:
    GIT_DEPTH: "0"
    CODEX_SECURITY_CLI_DIR: "/tmp/codex-security-cli"
  before_script:
    - |
      set -eu
      apt-get update -qq
      apt-get install -y -qq --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        ripgrep
      npm install \
        --prefix "$CODEX_SECURITY_CLI_DIR" \
        --ignore-scripts \
        --no-audit \
        --no-fund \
        @openai/codex-security@0.1.20

      test -x "$CODEX_SECURITY_BIN"
      "$CODEX_SECURITY_BIN" --version
  script:
    - |
      set -eu
      if test -z "${CODEX_SECURITY_API_KEY:-}"; then
        echo "Set the CODEX_SECURITY_API_KEY CI/CD variable." >&2
        exit 2
      fi

      codex_security_api_key="$CODEX_SECURITY_API_KEY"
      unset CODEX_SECURITY_API_KEY

      case "${CODEX_SECURITY_SCAN_SCOPE:-}" in
        diff)
          BASE_SHA="$CI_MERGE_REQUEST_DIFF_BASE_SHA"
          HEAD_SHA="$CI_COMMIT_SHA"
          BASE_REVISION="$(git merge-base "$BASE_SHA" "$HEAD_SHA")"
          set -- --diff "$BASE_REVISION" --head "$HEAD_SHA"
          echo "Scanning committed changes from $BASE_REVISION to $HEAD_SHA."
          ;;
        full)
          set -- --mode standard
          echo "Scanning the complete default branch at $CI_COMMIT_SHA."
          ;;
        *)
          echo "Unsupported Codex Security scan scope: ${CODEX_SECURITY_SCAN_SCOPE:-unset}" >&2
          exit 2
          ;;
      esac

      SCAN_DIR="/tmp/codex-security-results-$CI_JOB_ID"
      JSON_FILE="/tmp/codex-security-$CI_JOB_ID.json"
      SARIF_FILE="/tmp/codex-security-$CI_JOB_ID.sarif"

      install -d -m 700 "$CODEX_SECURITY_STATE_DIR" "$SCAN_DIR"

      set +e
      OPENAI_API_KEY="$codex_security_api_key" \
        "$CODEX_SECURITY_BIN" scan . \
          "$@" \
          --auth api-key \
          --output-dir "$SCAN_DIR" \
          --json > "$JSON_FILE"
      scan_exit="$?"
      set -e
      unset codex_security_api_key

      install -d -m 700 codex-security-artifacts/results
      cp -R "$SCAN_DIR"/. codex-security-artifacts/results/
      if test -s "$JSON_FILE"; then
        cp "$JSON_FILE" codex-security-artifacts/codex-security.json
      fi
      printf '%s\n' "$scan_exit" > codex-security-artifacts/scan-exit-code.txt

      export_exit=0
      if test -f "$SCAN_DIR/scan-manifest.json"; then
        set +e
        "$CODEX_SECURITY_BIN" export "$SCAN_DIR" \
          --export-format sarif \
          --source-root "$CI_PROJECT_DIR" \
          --output "$SARIF_FILE"
        export_exit="$?"
        set -e
        if test -s "$SARIF_FILE"; then
          cp "$SARIF_FILE" codex-security-artifacts/codex-security.sarif
        fi
      fi

      if test "$scan_exit" -ne 0; then
        exit "$scan_exit"
      fi
      exit "$export_exit"
  artifacts:
    when: always
    access: maintainer
    expire_in: 7 days
    paths:
      - codex-security-artifacts/
    reports:
      sarif: codex-security-artifacts/codex-security.sarif

デフォルトでは、このジョブは同じプロジェクト内のブランチからのマージリクエストでのみ実行されるため、
フォーク側のパイプラインにはスキャンの認証情報が渡されません。
グループ、プロジェクト、またはパイプラインのレベルで `CODEX_SECURITY_FULL_SCAN_DEFAULT_BRANCH` を `"true"` に設定すると、
デフォルトブランチでも標準のフルスキャンが実行されます。
フルスキャンは差分スキャンよりも時間とコストがかかります。

`GIT_DEPTH: "0"` を設定すると、マージリクエストのスキャン時に、
`CI_MERGE_REQUEST_DIFF_BASE_SHA` と `CI_COMMIT_SHA` からマージベースを計算するために必要な履歴が取得されます。

このジョブは CLI を `/tmp` 配下にインストールして絶対パスで実行し、
API キーをスキャンプロセスにのみ渡します。`artifacts: when: always` により、
スキャンが失敗した場合も SARIF レポートが保持されます。一方、`artifacts:access: maintainer` により、
詳細なスキャン結果へのアクセスが制限されます。

`.gitlab-ci.yml` を変更すると CI/CD 変数が漏えいする可能性があるため、
ジョブを実行する前にパイプラインの変更をレビューしてください。
[`CODEX_SECURITY_API_KEY` を保護対象に設定した場合](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#control-access-to-protected-variables-and-runners)、
GitLab でこの変数を使用できるのは、同じプロジェクト内の保護されたブランチ間のマージリクエストで、
かつユーザーがターゲットブランチにアクセスできる場合に限られます。

このセクションの冒頭にリンクを掲載した GitLab 専用ガイドでは、この最小構成のジョブを本番用ワークフローへ拡張する方法を説明しています。

## 重大度ポリシーの選択

どちらの例も `--fail-on-severity` を省略しているため、レポートのみの構成です。
検出結果をチェックの成否に反映する準備ができたら、
スキャンコマンドにしきい値を追加します：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --fail-on-severity high

サポートされるしきい値は `critical`、`high`、`medium`、`low` です。
しきい値の判定対象となるのは、今回のスキャンで検出された、その重大度以上の問題です。
リポジトリの概要に表示される以前からの未解決の検出結果は、ポリシーの判定に影響しません。

スキャンステップでは、次の終了コードを使用します：

| 終了コード  | 意味                                                                                 |
| ----- | --------------------------------------------------------------------------------------- |
| `0`   | スキャンが完全なカバレッジで完了し、設定されているポリシーがあれば、その判定にも合格しました。            |
| `1`   | 完了したスキャンに、しきい値以上の重大度の検出結果が含まれています。                        |
| `2`   | CLI が入力エラーまたは実行時エラーを検出したか、完了したスキャンのカバレッジが不完全です。 |
| `130` | Ctrl-C によりスキャンが中断されました。                                                            |
| `143` | SIGTERM によりスキャンが終了しました。                                                            |

カバレッジが `partial` または `unknown` のスキャンは、重大度ポリシーがなくても `2` を返します。
この場合も、CLI は得られた検出結果とカバレッジを書き出します。
チェック結果を確定的なものとみなす前に、`coverage.json` でスキャンが保留された領域を確認してください。

## 既存の結果ディレクトリでの再試行

CI ジョブごとに新しいランナーディレクトリを使用してください。
永続ランナーまたはセルフホスト型ランナーでは、`--archive-existing` を使用して以前の結果を保持します：

```bash
"$CODEX_SECURITY_BIN" scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --archive-existing

このコマンドは以前の結果をアーカイブし、空のスキャンディレクトリから開始します。

## CI スキャンのトラブルシューティング

- **不明な Git ref、または想定外の差分：** base と head の履歴を取得し、
  マージベースを計算して、両方のリビジョンを明示的に指定します。
- **保護されている、または空でない出力ディレクトリ：** 対象の Git Worktree の外部にある非公開ディレクトリを選択してください。
  ディレクトリに結果がすでに含まれている場合は、
  `--archive-existing` を使用します。
- **認証情報がない場合：** `CODEX_SECURITY_API_KEY` が信頼できるワークフローまたはパイプラインで利用でき、
  スキャンプロセスの環境変数
`OPENAI_API_KEY` に直接割り当てられていることを確認してください。
- **スキャン履歴エラー：** `CODEX_SECURITY_STATE_DIR` に、
  リポジトリ外の書き込み可能なディレクトリを指定します。
- **Python セットアップエラー：** ランナーで Python 3.10 以降を使用していることを確認してください。
- **カバレッジが不完全な場合：** 保留された対象領域や未解決事項も含めて `coverage.json` を確認し、
  適切な対象または環境で再実行してください。
- **SARIF エクスポートエラー：** スキャンが完了しており、
  スキャンディレクトリ一式を利用できることを確認してください。エクスポートでは、
  封印済みのアーティファクトを検証してから SARIF を書き出します。
- **SARIF アップロードエラー：** GitHub Actions では、組織が対象リポジトリで
  GitHub Code Security を有効にしており、ワークフローに
`actions: read`、`contents: read`、`security-events: write` の権限が付与されていることを確認してください。
  GitLab CI/CD では、プロジェクトで GitLab Ultimate 19.2 以降を使用しており、
  ジョブが `artifacts:reports:sarif` を介して SARIF 2.1.0 ファイルをアップロードすることを確認してください。

すべてのコマンド、フラグ、アーティファクト、出力フィールドについては、[CLI
リファレンス](/ja-JP/codex/security/cli/reference)を参照してください。
プラグインを使った対話型の CI レビューについては、[コード変更のセキュリティレビュー](/ja-JP/codex/security/plugin/code-changes#automate-reviews-in-cicd)を参照してください。
