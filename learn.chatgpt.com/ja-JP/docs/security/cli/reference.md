<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli/reference -->

このリファレンスでは、対応している `codex-security` コマンド、フラグ、
出力形式、終了時の動作を確認できます。初回スキャンの手順については、
[CLI クイックスタート](/ja-JP/codex/security/cli)を参照してください。

  `@openai/codex-security` パッケージは公開されています。
  スキャンの実行には Codex Security へのアクセス権が必要です。スキャンではローカルの権限が使用され、
  承認を求めるために一時停止することはありません。開始前に[ローカルスキャンの
  権限](#local-scan-permissions)を確認してください。

`npx @openai/codex-security` で CLI を実行します。

## コマンドの概要

```text
usage: codex-security [--version] <command> [options]

CLI では次のコマンドを使用できます：

| コマンド                       | 用途                                               |
| ----------------------------- | ----------------------------------------------------- |
| `codex-security scan`         | Codex Security スキャンを実行します。                            |
| `codex-security install-hook` | Git の pre-commit セキュリティスキャンをインストールします。               |
| `codex-security bulk-scan`    | リポジトリを検出し、再開可能な一括スキャンを実行します。   |
| `codex-security scans`        | 保存済みのスキャンログを一覧表示、確認、比較、取得します。 |
| `codex-security findings`     | 保存済みのセキュリティ検出結果をレビューし、更新します。            |
| `codex-security export`       | 完了済みの検出結果を CSV、JSON、SARIF 形式でエクスポートします。     |
| `codex-security publish`      | 完了したスキャンの検出結果を Linear に公開します。            |
| `codex-security validate`     | 候補となるセキュリティ検出結果を 1 件以上確認します。        |
| `codex-security patch`        | 1 件以上のセキュリティ上の問題にパッチを適用します。                    |
| `codex-security login`        | サインイン、資格情報の保存、サインイン状態の確認を行います。  |
| `codex-security logout`       | 保存済みのサインイン情報を削除します。                            |
| `codex-security info`         | SDK と同梱プラグインのメタデータを読み取り専用で表示します。       |

CLI では次の連携コマンドも使用できます：

| コマンド                      | 用途                               |
| ---------------------------- | ------------------------------------- |
| `codex-security completions` | シェル補完スクリプトを生成します。    |
| `codex-security mcp`         | CLI を MCP サーバーとして登録します。    |
| `codex-security skills`      | Codex Security のスキルをエージェントに同期します。 |

使用可能なすべてのコマンドを一覧表示します：

```bash
npx @openai/codex-security --help

コマンドに `--help` を追加すると、引数とオプションを確認できます：

```bash
npx @openai/codex-security scan --help

`codex-security --version` はインストール済みのバージョンを出力して終了します。
`codex-security info --json` は SDK と同梱プラグインのバージョンを報告します。
どちらのコマンドにも Python は必要ありません。

### コマンドの探索とエージェントの接続

エージェントが読み取れるコマンドマニフェストを出力します：

```bash
npx @openai/codex-security --llms

スキャン引数のスキーマを JSON 形式で確認します：

```bash
npx @openai/codex-security scan --schema --format json

Bash 用のシェル補完を生成します：

```bash
npx @openai/codex-security completions bash

該当するシェルに合わせて、`bash` を `zsh` または `fish` に置き換えます。

スキャン結果では `--format toon|json|yaml|jsonl` と `--full-output` を使用できます。
フレームワークレベルの `--format` は、完了したスキャンからエクスポートする
成果物の形式を選択する `--export-format` とは別のオプションです。
グローバルコマンドのヘルプには `md` も表示されますが、スキャン結果の Markdown 出力には対応していません。

CLI を MCP サーバーとして登録します：

```bash
npx @openai/codex-security mcp add

Codex Security のスキルをエージェントに同期します：

```bash
npx @openai/codex-security skills add

MCP で公開されるのは、読み取り専用の `info` メタデータコマンドだけです。
スキャン、エクスポート、認証、検証、パッチ適用は CLI でのみ利用できます。

## `codex-security scan`

リポジトリ、選択したパス、コミット済みの変更、
または作業ツリーを対象にスキャンを実行します。

```text
usage: codex-security scan [-h] [--auth {auto,chatgpt,api-key}]
                           [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                           [--path PATH | --diff BASE | --working-tree]
                           [--head HEAD] [--base BASE]
                           [--knowledge-base PATH] [--scan-prompt-file FILE]
                           [--post-scan-prompt-file FILE]
                           [--mode {standard,deep}] [--workers N]
                           [--subagents N] [--stop-after-no-new N]
                           [--max-discovery-runs N] [--max-time-hours HOURS]
                           [--model MODEL]
                           [--effort {minimal,low,medium,high,xhigh,max}]
                           [--output-dir DIR]
                           [--archive-existing]
                           [--plugin-path PATH] [--python PATH]
                           [--codex KEY=VALUE] [--fail-on-severity LEVEL]
                           [--patch] [--patch-severity {critical,high,medium,low}]
                           [--create-pr]
                           [--max-cost USD] [--dry-run] [--headless] [--verbose]
                           [--json] [--format {toon,json,yaml,jsonl}]
                           [--full-output] [repository]

`repository` のデフォルトは現在のディレクトリです。

### スキャン認証の選択

デフォルトの `--auth auto` を使用すると、資格情報が自動的に選択されます。ChatGPT のサインイン情報があり、
`OPENAI_API_KEY` または `CODEX_API_KEY` も利用できる場合、
テキスト出力の対話型スキャンでは、使用する資格情報の選択を求められます。
CI でのスキャン、JSON または JSONL 形式のスキャン、および対話型ターミナルを使用しないその他のスキャンでは、
環境変数の API キーが使用されます。ドライランでは、資格情報の入力を求めることも、読み込むこともありません。

保存済みの資格情報を使用するには、`--auth chatgpt` を指定します：

```bash
npx @openai/codex-security scan . --auth chatgpt

環境変数の API キーを使用するには、`--auth api-key` を指定します：

```bash
npx @openai/codex-security scan . --auth api-key

自動選択時に保存済みの資格情報をデフォルトで使用するには、
`unset OPENAI_API_KEY CODEX_API_KEY` を実行します。

### OpenRouter または Fireworks の使用

API キーとモデルを明示的に指定して、OpenRouter を選択します：

```bash

npx @openai/codex-security scan . \
  --provider openrouter \
  --model anthropic/claude-sonnet-4.5

API キーとモデルを明示的に指定して、Fireworks を選択します：

```bash

npx @openai/codex-security scan . \
  --provider fireworks \
  --model accounts/fireworks/models/qwen3-235b-a22b

どちらのプロバイダーも `bulk-scan` に対応しています。

### Amazon Bedrock の使用

`--provider amazon-bedrock` で Amazon Bedrock を選択し、
`--model` で Bedrock モデルを明示的に指定します：

```bash
npx @openai/codex-security scan . \
  --provider amazon-bedrock \
  --model openai.gpt-5.6-sol

`AWS_REGION` を設定し、`AWS_BEARER_TOKEN_BEDROCK`、標準の AWS アクセスキー、
AWS プロファイル、ウェブアイデンティティ、コンテナの資格情報、
またはデフォルトの AWS 資格情報チェーンで認証します。Bedrock スキャンでは、
`--auth`、ChatGPT へのサインイン、OpenAI API キーではなく、AWS 資格情報を使用します。`scan` と `bulk-scan` の両方が
`--provider` に対応しています。

### スキャン対象の選択

スキャンごとに対象の種類を 1 つ選択します。

| 引数                 | 説明                                                                     |
| ------------------------ | ------------------------------------------------------------------------------- |
| `--path PATH`            | リポジトリからの相対パスをスキャンします。複数のパスを指定する場合は、このフラグを繰り返し使用します。         |
| `--diff BASE`            | `BASE` から `--head` までのコミット済みの変更をスキャンします。ヘッドのデフォルトは `HEAD` です。    |
| `--head HEAD`            | `--diff` で使用するヘッドリビジョンを設定します。                                             |
| `--working-tree`         | `--base` を基準として、ステージ済みおよび未ステージの変更をスキャンします。ベースのデフォルトは `HEAD` です。 |
| `--base BASE`            | `--working-tree` で使用するベースリビジョンを設定します。                                     |
| `--mode {standard,deep}` | スキャンモードを選択します。デフォルトは `standard` です。                                |

`--path`、`--diff`、`--working-tree` は同時に指定できません。`--head` には
`--diff` が必要で、`--base` には `--working-tree` が必要です。deep モードでは、
リポジトリとパスをスキャン対象にできます。

差分スキャンと作業ツリーのスキャンでは、リポジトリ引数に Git Worktree のルートを指定する必要があります。選択した参照は、そのチェックアウト内に存在する必要があります。

リポジトリ全体をスキャンします：

```bash
npx @openai/codex-security scan .

選択したパスをスキャンします：

```bash
npx @openai/codex-security scan . --path src --path tests

コミット済みの変更をスキャンします：

```bash
npx @openai/codex-security scan . --diff origin/main --head HEAD

ステージ済みおよび未ステージの変更をスキャンします：

```bash
npx @openai/codex-security scan . --working-tree --base HEAD

リポジトリをより詳細にレビューします：

```bash
npx @openai/codex-security scan . --mode deep

### 詳細スキャンの構成

`--mode deep` と次のオプションを併用して、ワーカーの同時実行数と実行時間を制御します：

| 引数                 | 説明                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `--workers N`            | 独立した標準スキャンを実行するワーカーの同時実行数の上限です。デフォルトは `4` です。                |
| `--subagents N`          | 各ワーカーが使用できるサブエージェントの数です。デフォルトは `3` です。                                   |
| `--stop-after-no-new N`  | 完了したワーカーのスキャンで、新しい問題が `N` 回連続して見つからなかった場合に停止します。デフォルトは `4` です。 |
| `--max-discovery-runs N` | 独立した標準スキャンの総実行回数の上限です。デフォルトは `40` です。                       |
| `--max-time-hours HOURS` | ワーカーの実行時間の上限を時間単位で指定します。デフォルトは `96` で、小数も指定できます。             |

`--subagents` には 0 または正の整数を指定できます。`--max-time-hours` には、
`96` 以下の正の数を指定できます。
その他のオプションには正の整数を指定する必要があります。これらのオプションは標準スキャンでは使用できません。

たとえば、2 つのワーカーを使用し、最大 10 回の実行を許可して、1.5 時間後にワーカーの実行を停止します：

```bash
npx @openai/codex-security scan . \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

制限時間に達すると、スキャンは未完了のワーカーを停止し、
完了済みのスキャン結果を保持して最終レポートに集約します。
どのワーカーもソースコードのレビューを完了できなかった場合は、カバレッジが部分的であることを記録し、終了コード `2` を返します。

永続的なデフォルト値を `~/.codex/codex-security/config.toml`、または
`$CODEX_HOME/codex-security/config.toml` に設定します。後者は `CODEX_HOME` を設定している場合に使用します：

```toml
[deep_scan]
workers = 2
subagents = 0
stop_after_no_new = 3
max_discovery_runs = 10
max_time_hours = 1.5

コマンドラインオプションは、これらのデフォルト値より優先されます。`scan --workers` は、
1 回の詳細スキャン内で独立した標準スキャンを実行するワーカー数を制御します。`bulk-scan --workers` は、
リポジトリスキャンの同時実行数を制御します。`stop_after_consecutive_errors` は
TOML ファイルでのみ設定でき、デフォルトは `3` です。

### セキュリティコンテキストの追加

`--knowledge-base PATH` を使用して、アーキテクチャ文書、脅威モデル、
またはセキュリティポリシーを指定します。複数のファイルやディレクトリを指定するには、このオプションを繰り返します：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

`.md`、`.markdown`、`.txt`、`.pdf`、および `.docx` の文書ファイルに対応しています。
CLI はディレクトリを再帰的に検索し、リンクされた入力パスを拒否して、
リンクされたディレクトリエントリをスキップします。
抽出した文書の内容は、保存済みのスキャン結果には含めません。

### スキャン指示の追加

スキャン指示を追加するには、テキストファイルまたは Markdown ファイルを
`--scan-prompt-file` で指定します。`--post-scan-prompt-file` を使用すると、
成功したスキャンの後や、カバレッジが不完全なスキャン、
エラーが発生したスキャンの後に、同じ認証済みセッションで追加の指示を実行できます：

```bash
npx @openai/codex-security scan . \
  --scan-prompt-file security-focus.md \
  --post-scan-prompt-file follow-up.md

たとえば、スキャンプロンプトでは認可境界に重点を置き、
フォローアップではスキャンディレクトリに新しい `post-scan-summary.md` を作成するよう指示します。
フォローアップが失敗した場合、CLI は警告を表示し、完了したスキャンを保持します。
スキャンがキャンセルされた場合やコスト上限に達した場合は、
フォローアップは実行されません。

### 出力とポリシーのオプション設定

これらのオプションを使用すると、アーティファクトや以前の結果を保持したり、機械可読な結果を生成したりできます。

| 引数                   | 説明                                                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `--output-dir DIR`         | スキャンアーティファクトを、対象を含む Git Worktree の外にある非公開ディレクトリに書き込みます。デフォルトでは Codex Security の永続状態に保存します。 |
| `--archive-existing`       | 既存の結果を `DIR.previous-<timestamp>-<id>` に移動し、空の出力ディレクトリから開始します。`--output-dir` が必要です。  |
| `--fail-on-severity LEVEL` | 完了したスキャンで、`critical`、`high`、`medium`、`low` のいずれかで指定した重大度以上の検出事項が報告された場合は、終了コード `1` を返します。                  |
| `--patch`                  | 完全なスキャンの終了後に、選択した検出事項を修正して検証します。                                                                      |
| `--patch-severity LEVEL`   | `critical`、`high`、`medium`、または `low` で指定した重大度以上の検出事項にパッチを適用します。デフォルトは `low` です。                                        |
| `--create-pr`              | 検証済みのパッチファイルをコミットし、GitHub で Pull Request を作成します。`--patch` が必要です。                                              |
| `--max-cost USD`           | モデルの推定コストが、米ドルで指定した金額を超えた場合にスキャンを停止します。                                                  |
| `--dry-run`                | スキャンを開始せずに、リポジトリ、対象、ナレッジベース、出力ディレクトリ、Codex の構成を確認します。             |
| `--headless`               | 対話型スキャンダッシュボードの代わりに、進行状況をプレーンテキストで表示します。                                                          |
| `--verbose`                | マスキング済みのライフサイクル、認証、進行状況、コストに関する診断情報を stderr に出力します。                                          |
| `--json`                   | マニフェスト、検出事項、カバレッジ、パス、ターンのメタデータを 1 つの JSON 文書として出力します。                                           |
| `--format FORMAT`          | スキャン結果全体を `toon`、`json`、`yaml`、または `jsonl` 形式で出力します。                                                        |
| `--full-output`            | 結果全体をデフォルトの構造化出力形式で出力します。                                                        |

コスト上限は推定値であり、厳密な支出上限ではありません。
すでに進行中のリクエストが完了すると、上限をわずかに超える場合があります。
詳細スキャンで、Codex Security が完了済みのワーカーの結果を集約した後に上限に達した場合、CLI は利用可能な結果を封印し、
カバレッジを `partial` として記録して終了コード `2` を返します。
それ以外の場合は `2` を返し、利用可能な部分的な出力をディスク上に残します。

`--output-dir` を省略した場合、結果は
`$CODEX_HOME/state/plugins/codex-security/scans/<repository>` に永続的に保存されます。`CODEX_HOME` のデフォルトは
`~/.codex` です。`CODEX_SECURITY_STATE_DIR` を設定すると、結果は代わりに
`$CODEX_SECURITY_STATE_DIR/scans/<repository>` に保存されます。
これらのディレクトリにはソースコードの抜粋や脆弱性の詳細が含まれる可能性があるため、
権限と保持期間を適切に管理してください。

ワークベンチはスキャン履歴を
`$CODEX_HOME/state/plugins/codex-security/workbench.sqlite3` に保存します。
`CODEX_SECURITY_STATE_DIR` を設定すると、ワークベンチのデータベースも移動します。

出力ディレクトリは、スキャン対象のディレクトリと、それを含むすべての
Git Worktree の外に配置する必要があります。スキャン時には
`--archive-existing` を使用して既存の結果ディレクトリを置き換えられます。

出力ディレクトリを再利用する前に、以前の結果を保持するには：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --archive-existing

スキャンはデフォルトではレポートのみを生成します。`--fail-on-severity` を追加すると、
CI で重大度ポリシーを評価できます：

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --output-dir /path/outside/repository/results \
  --json \
  --fail-on-severity high \
  > /path/outside/repository/codex-security.json

ドライランでは、認証情報の読み込み、Codex の起動、プラグインの Python インタープリターの検査を行わずに、ナレッジベース文書を含むローカル入力を確認します：

```bash
npx @openai/codex-security scan . \
  --output-dir /path/outside/repository/results \
  --dry-run

### ランタイムの構成

モデル、インタープリター、プラグイン、または Codex の構成値を明示的に指定する必要がある場合は、ランタイムオプションを使用します。

| 引数                                                  | 説明                                                                                              |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `--auth {auto,chatgpt,api-key}`                           | スキャンの認証情報を選択します。デフォルトは `auto` です。                                                      |
| `--provider {openai,openrouter,fireworks,amazon-bedrock}` | 推論プロバイダーを選択します。デフォルトは `openai` です。                                                  |
| `--model MODEL`                                           | モデルを選択します。デフォルトは `gpt-5.6-sol` です。OpenRouter、Fireworks、Amazon Bedrock を使用する場合は必須です。  |
| `--effort {minimal,low,medium,high,xhigh,max}`            | モデルの推論強度を選択します。デフォルトは `xhigh` です。                                             |
| `--plugin-path PATH`                                      | Codex Security プラグインのディレクトリまたは ZIP ファイルを使用して、同梱のプラグインを上書きします。                             |
| `--python PATH`                                           | プラグインのランタイムで使用する Python インタープリターを選択します。                                                    |
| `--codex KEY=VALUE`                                       | 分離された Codex の構成値を上書きします。値は TOML 構文で指定します。複数の値を指定するには、フラグを繰り返します。 |

TOML を記述せずに別のモデルと推論強度を選択するには：

```bash
npx @openai/codex-security scan . --model gpt-5.6-terra --effort high

`--codex` で渡す文字列の値を引用符で囲み、
TOML パーサーが文字列として受け取れるようにします：

```bash
npx @openai/codex-security scan . --codex 'model="gpt-5.6-terra"'

## `codex-security install-hook`

現在のリポジトリに Git の pre-commit セキュリティチェックをインストールします：

```bash
npx @openai/codex-security install-hook

このチェックでは、各コミットの前にステージ済みと未ステージの変更をスキャンし、
重大度の高い検出結果やスキャンエラーがある場合はコミットをブロックします。`core.hooksPath` の設定に従い、
既存の pre-commit スクリプトは置き換えません。
必要に応じて、重大度のしきい値を変更してください：

```bash
npx @openai/codex-security install-hook . --fail-on-severity medium

## `codex-security bulk-scan`

GitHub リポジトリを検出してスキャンするか、
リポジトリの CSV から再開可能なスキャンを実行します：

GitHub でのリポジトリ検出、CSV インベントリ、キャンペーン結果、
コンテナでのスキャンについて詳しくは、[セキュリティスキャンの
一括実行](/ja-JP/codex/security/cli/bulk-scans)を参照してください。

```text
usage: codex-security bulk-scan [input] [--output-dir DIR]
                                [--workers N] [--mode {standard,deep}]
                                [--provider {openai,openrouter,fireworks,amazon-bedrock}]
                                [--model MODEL]
                                [--effort {minimal,low,medium,high,xhigh,max}]
                                [--knowledge-base PATH]
                                [--scan-prompt-file FILE]
                                [--post-scan-prompt-file FILE]
                                [--max-attempts N] [--plugin-path PATH]
                                [--python PATH] [--codex KEY=VALUE]

引数を指定せずに `npx @openai/codex-security bulk-scan` を実行すると、
リポジトリを対話形式で選択できます。この操作には GitHub CLI へのサインインが必要です。

対話形式での検出時にモデルと推論強度を選択するには：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

事前に用意したリポジトリ一覧を使用する場合は、CSV と `--output-dir` を指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CSV には `id`、`repository`、`revision` の列が必要です。
リビジョンには完全なコミットハッシュを指定する必要があります。任意の `scope`、`mode`、`prompt` 列を使用すると、
リポジトリごとに設定できます：

```csv
id,repository,revision,scope,mode,prompt
service,https://github.com/example/service.git,0123456789abcdef0123456789abcdef01234567,src,standard,Review authorization boundaries.

`--knowledge-base PATH` を使用すると、すべてのリポジトリでセキュリティドキュメントを
共有できます。`--scan-prompt-file FILE` を使用すると、共通のスキャン指示を追加できます。
CSV の `prompt` 列では、その共通プロンプトの後に
リポジトリ固有の指示を追加できます。`--post-scan-prompt-file FILE` は、カバレッジが不完全な場合やエラーが発生した場合も含め、
各スキャンの後にフォローアップ指示を実行します。
スキャンがキャンセルされた場合やコスト上限に達した場合は実行されません。

`--workers` は同時に実行するリポジトリスキャンの数を制限し、デフォルトは `4` です。`--mode` については、
デフォルトが `standard` です。`--max-attempts` のデフォルトは `1` です。
リポジトリまたはスキャンのエラーを再試行するには、`--max-attempts` を設定します。
カバレッジが不完全なまま完了したスキャンは再試行されません。
その結果は引き続き利用でき、コマンドは終了コード `2` を返します。

同じコマンドを再実行すると、既存の出力ディレクトリから処理を再開できます。
CLI は、カバレッジが不完全なものも含め、完了済みのスキャンをスキップします。

コンテナを使用したキャンペーンについては、[Docker での
一括スキャンの実行](/ja-JP/codex/security/cli/bulk-scans#run-bulk-scans-in-docker)を参照してください。

## `codex-security scans`

### 保存済みスキャンの検索

現在のディレクトリの保存済みスキャンを一覧表示します：

```bash
npx @openai/codex-security scans

別のリポジトリのスキャンを一覧表示します：

```bash
npx @openai/codex-security scans list /path/to/repository

特定の出力ディレクトリに保存されているスキャンを検索します：

```bash
npx @openai/codex-security scans list --scan-root /path/outside/repository/results

### スキャンの確認または再実行

保存済みスキャンの結果と構成を表示します：

```bash
npx @openai/codex-security scans show SCAN_ID

以前のスキャンの検出結果へのリンクを含めるには、`--show-linked-findings` を追加します。

元の構成を使用して、現在のチェックアウトに対するスキャンを再実行します：

```bash
npx @openai/codex-security scans rerun SCAN_ID

再実行には、元のスキャンで記録されたバージョンのプラグインが必要です。
インストール済みのバージョンが異なる場合、コマンドは別のプラグインで実行されず、
停止します。

### 保存済みスキャンログの確認

スキャンとそのワーカーについて保存されたすべてのセッションイベントを確認します。
これらのログはマスキングされておらず、ソースコードや認証情報が含まれる可能性があるため、
共有前に内容を確認してください：

```bash
npx @openai/codex-security scans logs SCAN_ID

すべての情報を含む機械処理向けの形式で結果を取得するには、`--json` を追加します。

### 検出結果の照合と比較

2 つのスキャンを比較し、新規、継続中、再オープン、解決済み、不明の
検出結果を特定します：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較では、根本原因が同じ検出結果を自動的に照合し、
保存済みの照合結果を再利用します。照合結果を明示的に保存するには、`scans match` を使用します：

```bash
npx @openai/codex-security scans match PREVIOUS_SCAN_ID CURRENT_SCAN_ID

後のスキャンのカバレッジが不完全な場合や、
検出結果が最初に確認された場所が対象に含まれていない場合、その検出結果は不明と判定されます。既存の照合結果を再計算するには、`--force` を `match` に
追加します。

別のチェックアウトで実行したスキャンも含め、
現在のリポジトリで完了したすべてのスキャンを照合するには：

```bash
npx @openai/codex-security scans match --all

同じ構成で再実行しても、スキャン結果が異なる場合があります。
照合や比較では変更を追跡できますが、結果が常に同じになるわけではなく、
脆弱性が解消されたことの証明にもなりません。`validate` を使用して、
セキュリティ上重要な検出結果を現在のコードに対して再確認してください。

## `codex-security findings`

現在のリポジトリの各スキャンで未解決の検出結果を一覧表示します：

```bash
npx @openai/codex-security findings list

別のチェックアウトを確認するには、リポジトリのパスを指定します：

```bash
npx @openai/codex-security findings list /path/to/repository

`--json` を追加すると、構造化された形式で出力できます。一覧には、
最新のスキャンで確認された検出結果と、そのスキャンでは確認されなかった以前の検出結果が表示されます。

以前の検出結果は、解決または却下されるまで未解決のまま残ります
（最新のスキャンで検出されなくても、修正されたことの証明にはなりません）。

レビュー済みの検出結果を誤検知として記録するには：

```text
usage: codex-security findings false-positive OCCURRENCE_ID
                       --reason REASON

保存済みスキャンを確認し、検出結果が発生した箇所を特定します：

```bash
npx @openai/codex-security scans show SCAN_ID

誤検知と判断した具体的な理由を記録します：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

理由は空欄にできません。Codex Security はこの判断をリポジトリごとに保存し、
今後のスキャンにコンテキストとして提供します。各スキャンでは、現在のソースコード、
セキュリティ対策、到達可能性を個別に再確認します。過去の判断によって、
ルール、パス、脆弱性クラスが抑制されることはありません。

## `codex-security export`

完了してシールされたスキャンから CSV、JSON、または SARIF をエクスポートします。
エクスポートでは出力前にスキャンアーティファクトを検証し、
Codex のランタイムや認証情報には手を加えません。

```text
usage: codex-security export [--export-format {csv,json,sarif}]
                             [--output FILE|-] [--source-root PATH]
                             [--python PATH] scan_dir

`scan_dir` は、完了したスキャンのディレクトリです。

| 引数                           | 説明                                                                                 |
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| `--export-format {csv,json,sarif}` | エクスポート形式を選択します。デフォルトは `sarif` です。                                           |
| `--output FILE\|-`                 | 選択した形式でファイルまたは stdout に書き込みます。デフォルトでは、現在のディレクトリ内のファイルに書き込みます。 |
| `--source-root PATH`               | リポジトリのチェックアウトを使用して、ソース行のフィンガープリントを SARIF に追加します。                          |
| `--python PATH`                    | 同梱のエクスポーターで使用する Python インタープリターを選択します。                                     |

`--source-root` は `--export-format sarif` と組み合わせた場合にのみ使用できます。JSON では、
シール済みの検出結果ドキュメントが保持されます。CSV には移植可能な検出結果の列が含まれますが、
ローカルワークベンチのトリアージ状態は含まれません。

`--output` を指定しない場合、CLI は現在の作業ディレクトリで SARIF を `results.sarif` に、JSON を
`findings.json` に、CSV を `findings.csv` に書き込みます。
エクスポートしたデータには、ソースコードの抜粋や脆弱性の詳細が含まれる場合があります。
コマンドをリポジトリの外部で実行するか、`--output` を指定して、
スキャン対象のチェックアウトの外部にある非公開パスを使用してください。

SARIF をファイルに書き込みます：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root /path/to/repository \
  --output /path/outside/repository/exports/results.sarif

SARIF を stdout に書き込みます：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format sarif \
  --source-root . \
  --output -

検出結果を JSON 形式でエクスポートします：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format json \
  --output /path/outside/repository/exports/findings.json

検出結果を CSV 形式でエクスポートします：

```bash
npx @openai/codex-security export /path/to/scan \
  --export-format csv \
  --output /path/outside/repository/exports/findings.csv

## `codex-security publish scan`

完了したスキャンのすべての検出結果を Linear に登録します：

```text
usage: codex-security publish scan [SCAN_DIR] --to linear
                                   [--linear-team TEAM_ID]
                                   [--project PROJECT_ID]
                                   [--linear-api-key KEY]
                                   [--linear-assignee EMAIL_OR_USER_ID]
                                   [--dry-run] [--json]

`SCAN_DIR` には、完了してシールされたスキャンが含まれている必要があります。
対話型ターミナルでは、この引数を省略すると、ローカルのスキャン履歴から完了済みのスキャンを選択できます。
イシューを作成するには、そのスキャンと検出結果がローカルのスキャン履歴に存在する必要もあります。
ドライランでは、この永続化の確認を行わずに、シール済みのアーティファクトを検証します。

| 引数                             | 説明                                                                                                                                                      |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--to linear`                        | Linear に登録します。この引数は必須です。                                                                                                                    |
| `--linear-team TEAM_ID`              | Linear のチームを選択します。省略した場合は `CODEX_SECURITY_LINEAR_TEAM` を使用します。いずれか一方を指定する必要があります。                                                                 |
| `--project PROJECT_ID`               | Linear のプロジェクトを選択します。省略した場合は `CODEX_SECURITY_LINEAR_PROJECT` を使用します。どちらも設定されていない場合、イシューはチームに直接作成されます。                          |
| `--linear-api-key KEY`               | 直接登録するには、Linear の個人用 API キーを使用します。省略した場合は `CODEX_SECURITY_LINEAR_API_KEY` を使用します。                                                         |
| `--linear-assignee EMAIL_OR_USER_ID` | 作成したイシューの担当者をメールアドレスまたは Linear のユーザー ID で指定します。`--linear-api-key` または `CODEX_SECURITY_LINEAR_API_KEY` が必要です。省略した場合、イシューは未割り当てのままになります。 |
| `--dry-run`                          | Codex の起動、Linear との通信、イシューの作成、登録状態の書き込みを行わずに、イシューのペイロードを準備します。                                                 |
| `--json`                             | 構造化された登録結果を stdout に書き込みます。進捗は引き続き stderr に出力されます。                                                                                      |

  Linear のイシューの説明やドライランの出力には、ソースコードのスニペットや
脆弱性の詳細が含まれる場合があります。登録先は許可された Linear のチームまたは
プロジェクトに限定し、保存した出力は機密情報として取り扱ってください。

ドライラン以外でコマンドを実行するたびに、すべての検出結果について新しいイシューの作成を試みます。
同じスキャンを再度登録しても、既存のイシューの照合、更新、再利用は行われません。
一部の検出結果の登録に失敗した場合でも、作成に成功したイシューは保持され、
コマンドは終了コード `2` を返します。
`--json` を指定した場合は、再試行前に `created` と `failed` の結果を確認し、
重複を避けてください。

公開前にイシューのペイロードをプレビューします：

```bash
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --dry-run \
  --json

### 接続済みの Linear アプリを使用した公開

Linear の API キーを指定しない場合、このコマンドは既存の構成と接続済みの Linear アプリを使用して Codex を起動します。公開前にサインインし、Linear を Codex アカウントに接続してください：

```bash
npx @openai/codex-security login
npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --project PROJECT_ID

### Linear の API キーを使用した公開

`--linear-api-key` または `CODEX_SECURITY_LINEAR_API_KEY` を指定すると、
Linear API を通じて直接公開され、Codex は起動しません。直接公開する場合、
担当者を選択しない限り、イシューは担当者未設定のままです：

```bash

npx @openai/codex-security publish scan /path/to/completed-scan \
  --to linear \
  --linear-team TEAM_ID \
  --linear-assignee teammate@example.com

コマンドラインで指定した値は、対応する環境変数より優先されます。
API キーについては、`CODEX_SECURITY_LINEAR_API_KEY` を `--linear-api-key` より優先してください。
コマンドライン引数はシェル履歴やプロセス一覧に表示される可能性があるためです。

## `codex-security validate` と `codex-security patch`

検出結果の候補が有効かどうかを確認します：

```bash
npx @openai/codex-security validate findings.json \
  "Possible SQL injection in src/query.ts:42"

同梱の修復スキルを使用して修正を生成します：

```bash
npx @openai/codex-security patch findings.json \
  "Missing authorization check in src/routes.ts:18"

各位置引数には、リテラルテキストまたはファイルパスを指定できます。
これらの入力は現在のディレクトリを基準とします。修正後や、後続のスキャンで検出結果が報告されなくなった場合は、`validate` を使用して再確認してください。
スキャン結果を比較するだけでは、
修正が有効だったことは証明できません。

`--effort` を使用すると、どちらのコマンドでも推論強度を選択できます：

```bash
npx @openai/codex-security validate "Possible SQL injection" --effort high

### スキャン後の検出結果の修正

`scan --patch` を使用すると、スキャンの完了後に検出結果を修正できます。
これには `@openai/codex-security` 0.1.15 以降が必要です。
重大度のデフォルトのしきい値は `low` です。次のコマンドは、重大度が「高」または「重大」の検出結果を選択します：

```bash
npx @openai/codex-security scan . --patch --patch-severity high --json

検証済みの検出結果と、すでに修正された検出結果は、`--fail-on-severity` の対象になりません。

### 保存済みの検出結果の修正

検出結果 ID または発生 ID を指定して元のリポジトリを修正するか、保存済みのスキャンから検出結果を選択します：

```bash
npx @openai/codex-security patch OCCURRENCE_ID
npx @openai/codex-security patch --scan SCAN_ID --severity high --json
npx @openai/codex-security patch --scan latest --severity medium

`--scan latest` を指定すると、現在のリポジトリで完了した最新のスキャンが選択されます。
保存済みの検出結果を扱うコマンドは `--json` に対応していますが、リテラルテキストやファイルを入力する場合は対応していません。

`--create-pr` を追加すると、検証済みのパッチファイルだけをコミットし、
GitHub CLI を使用して Pull Request を作成できます：

```bash
npx @openai/codex-security patch --scan SCAN_ID --severity high --create-pr

プッシュまたは Pull Request の作成に失敗した場合は、表示された `patch --resume-pr BRANCH` コマンドで再試行してください。
このコマンドは同じリポジトリから実行します。

### Linear イシューの修正

個人用 API キーには `CODEX_SECURITY_LINEAR_API_KEY` または `LINEAR_API_KEY` を設定し、
OAuth トークンには `LINEAR_ACCESS_TOKEN` を設定します。キーがシェル履歴に残らないよう、
`--linear-api-key KEY` より環境変数の使用を優先してください。

ID または URL を指定してイシューをインポートします。`--linear-issue` を繰り返し指定すると、
複数のイシューを選択できます：

```bash
npx @openai/codex-security patch --linear-issue SEC-123 --linear-issue SEC-124

`--linear-project` を使用して、プロジェクト内の未解決のイシューを選択します。`--linear-filter` を追加すると、
対象を絞り込めます：

```bash
npx @openai/codex-security patch --linear-project "Security backlog" \
  --linear-filter '{"labels":{"name":{"eq":"security"}}}'

フィルターで `state` を設定しない限り、CLI は完了済みまたはキャンセル済みのイシューを除外します。
Linear のイシューは変更されません。

## `codex-security login`、`logout`、`info`

対話形式でサインインします：

```bash
npx @openai/codex-security login

リモートマシンまたはヘッドレスマシンでデバイス認証を使用します：

```bash
npx @openai/codex-security login --device-auth

現在のサインイン状態を確認します：

```bash
npx @openai/codex-security login status

保存されているサインイン情報を削除します：

```bash
npx @openai/codex-security logout

API キーを stdin 経由で渡して保存します：

```bash
printenv OPENAI_API_KEY | npx @openai/codex-security login --with-api-key

エンタープライズアクセストークンを保存します：

```bash
printenv CODEX_ACCESS_TOKEN | npx @openai/codex-security login --with-access-token

SDK と同梱プラグインの読み取り専用メタデータを確認します：

```bash
npx @openai/codex-security info --json

CLI を MCP サーバーとして公開する場合、使用できるコマンドは `info` だけです。
スキャン、エクスポート、公開、サインイン、検証、修正は、引き続き CLI でのみ実行できます。

## スキャン出力の確認

デフォルトでは、スキャンの進捗状況、完了時の概要、エラーは stderr に出力されます。
完全なスキャン結果は stdout に出力されません。構造化されたスキャン結果を stdout に出力するには、`--json`、
`--format`、または `--full-output` を指定します。

対話型ターミナルには、現在のスキャンフェーズ、レビュー済みのファイル、アクティビティ、トークン使用量、推定コストがリアルタイムのダッシュボードに表示されます。
CI やリダイレクトされた出力では、進捗状況がプレーンテキストで表示されます。
`--headless` を追加すると、
対話型ターミナルでも進捗状況をプレーンテキストで表示できます：

```bash
npx @openai/codex-security scan . --headless

ダッシュボードには、進行中のセッションの詳細も表示されます。機密情報は除去されていないため、ソースコードや認証情報が含まれる可能性があります。共有する前に内容を確認してください。

### 詳細な診断情報

`--verbose` を追加すると、機密情報を除去したライフサイクル、認証、進捗状況、コストの
診断情報が stderr に出力されます：

```bash
npx @openai/codex-security scan . --verbose

`CODEX_SECURITY_LOG_LEVEL=debug` を設定すると、フラグを指定せずに同じ診断情報を有効にできます。
`LOG_LEVEL=debug` を設定した場合も、
`CODEX_SECURITY_LOG_LEVEL` が未設定であれば診断情報が有効になります。

### 完了時の概要

スキャンが完了すると、リポジトリ内の未解決の検出結果数、重大度別の内訳、カバレッジ、経過時間、レポートのパス、結果ディレクトリが stderr に出力されます。取得できる場合は、トークン使用量と推定コストも含まれます：

```text
  REPORT    /path/to/scan/report.md

  FINDINGS  4 (3 confirmed this scan; 1 previously found; 1 critical, 2 high, 1 informational)
  COVERAGE  complete
  ELAPSED   1s
  TOKENS    1,250 input, 200 cached, 30 output
  RESULTS   /path/to/scan

情報レベルの検出結果も概要の合計件数に含まれます。
重大度ポリシーの評価対象は、今回のスキャンにおける `critical`、`high`、`medium`、`low` の検出結果のみです。
リポジトリの合計件数に含まれる過去の検出結果は評価されません。

### JSON 出力

`scan --json` は完全な JSON ドキュメントを 1 つ stdout に出力します。
最上位の構造は次のとおりです：

```text
manifest
repositoryFindings
findings
coverage
scanDir
threadId
reportPath
artifactsDir
sarifPath
cost
turn
  id
  status
  durationMs
  finalResponse
  usage

[パッチを適用する](#patch-findings-after-a-scan)場合、JSON 出力にはパッチの適用結果も含まれます。
Pull Request を作成した場合は、その情報も含まれます。

進捗状況、完了時の概要、アーカイブ通知、エラーは引き続き stderr に出力されます。
スキャンが完了していれば、
重大度ポリシーによって終了コード `1` が返される場合や、カバレッジが不完全なために終了コード `2` が返される場合でも、完全な JSON 結果が出力されます。

  `codex-security scan --json` は JSON ドキュメントを 1 つ出力し、`codex exec --json` は JSON Lines 形式のイベントストリームを出力します。
  出力形式は、
  実行するコマンドに合ったものを使用してください。

## スキャンアーティファクト

完了したスキャンでは、人が読める形式のレポートと構造化アーティファクトがまとめて保存されます：

```text
<scan-directory>/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

構造化ファイルには、それぞれ異なる役割があります：

| ファイル                    | 内容                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `scan-manifest.json`    | スキャンの識別情報、状態、対象、スコープ、生成元、シール済みアーティファクトの記録。                                                    |
| `findings.json`         | 検出結果の識別子、重大度、信頼度、分類体系、位置情報、根拠、検証、データフロー、到達可能性、修復策。 |
| `coverage.json`         | レビュー済みの対象領域、除外項目、保留中の作業、未解決事項、カバレッジの完全性。                                        |
| `report.md`             | 人が読める形式のスキャンレポート。                                                                                                           |
| `artifacts/`            | 補助的なスキャンアーティファクト。                                                                                                      |
| `exports/results.sarif` | スキャン中に生成された SARIF（存在する場合）。                                                                                  |

カバレッジの完全性には、次の 3 つの値があります：

- `complete`：選択したスコープのカバレッジが完全であることが記録されています。
- `partial`：保留中の作業またはその他のカバレッジ制限が記録されています。
- `unknown`：カバレッジの完全性が不明であると報告されています。

カバレッジをセキュリティ上の判断の根拠として使用する前に、保留中の対象領域、明示的な除外項目、未解決事項を確認してください。

## 終了コードとシグナル

CLI では、次の終了コードを使用します。

| 終了コード  | 条件                                                                                                                                                                     |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`   | スキャンが完全なカバレッジで完了して重大度ポリシーを満たした場合、一括スキャンまたは公開が失敗せずに完了した場合、または別のコマンドが成功した場合。                  |
| `1`   | 完了したスキャンで、設定された重大度以上の検出結果が報告された場合。                                                                                                       |
| `2`   | CLI が入力、実行時、またはエクスポートのエラーを検出した場合、スキャンのカバレッジが不完全な場合、一括スキャンの対象リポジトリでエラーが発生した場合、または公開に失敗した検出結果が 1 件以上ある場合。 |
| `130` | Ctrl-C によってスキャンまたは公開が中断された場合。                                                                                                                                     |
| `143` | SIGTERM によってスキャンまたは公開が終了した場合。                                                                                                                                     |

カバレッジが `partial` または `unknown` のスキャンは、重大度ポリシーがなくても `2` を返します。
構造化出力を要求すると、完了したスキャンや一部のみ成功した公開についても、
利用可能な結果が stdout に出力されます。CLI は、中断または実行時エラーの発生後、
部分的な出力がある場合は
その保存場所を表示します。

## ローカルスキャンの権限

CLI と SDK のスキャンは、ローカルのオペレーティングシステムにおけるユーザーの権限で実行されます。
すべてのスキャンで `codex_security_scan` ファイルシステムプロファイルを使用し、`approvalPolicy` を
`"never"` に設定します。このプロファイルでは、ローカルファイルシステムの読み取りと、
ワークスペースのルートおよび選択したスキャン状態ディレクトリへの書き込みが許可されます。
スキャンが対話的な承認を求めて停止することはありません。

CLI の `--codex` または SDK の `codexOverrides` で指定した設定では、
`approval_policy`、`sandbox_mode`、ファイルシステムの権限を含め、これらのスキャン制御を置き換えることも
制限することもできません。ホストとネットワークの制限は引き続き適用されます。

スキャンやワークベンチのプロセスには、関係のない API トークンやクラウドの認証情報を含むユーザーの環境が引き継がれる可能性があります。信頼でき、評価する権限があるリポジトリのみをスキャンし、スキャンに必要な認証情報だけを提供してください。

## 認証と前提条件

`OPENAI_API_KEY` または `CODEX_API_KEY` を設定するか、
`npx @openai/codex-security login` でサインインするか、ファイルに保存された既存の Codex サインイン情報を使用します。
OpenRouter または Fireworks の場合は、プロバイダーの API キーを設定し、
モデルを選択します。Amazon Bedrock の場合は、代わりに Bedrock API キー、または
標準の AWS 認証情報チェーンを使用します。

認証情報の選択については、[スキャン認証の
選択](#select-scan-authentication)を参照してください。

CI では、API キーの使用範囲をスキャンのステップに限定し、信頼できるワークフローを使用してください。

CLI には Node.js 22（22.13.0 以降）、24、または 26 が必要です。スキャン、一括スキャン、
エクスポート、スキャン履歴、保存済みの検出結果には、Python 3.10 以降も必要です。
Python 3.10 では `tomli` も必要です。`--python` を `scan`、`bulk-scan`、または
`export` と併用するか、Python を使用する任意のコマンドで `PYTHON` を設定してください。

引き続き、[CLI クイックスタート](/ja-JP/codex/security/cli)、[一括スキャンの
ガイド](/ja-JP/codex/security/cli/bulk-scans)、[CLI のよくある質問](/ja-JP/codex/security/cli/faq)、[CI
ガイド](/ja-JP/codex/security/cli/ci)、または [TypeScript SDK ガイド](/ja-JP/codex/security/sdk)を参照してください。
