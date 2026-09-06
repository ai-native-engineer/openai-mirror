<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli/bulk-scans -->

`npx @openai/codex-security bulk-scan` を使用すると、1 回のキャンペーンでリポジトリをまとめてレビューできます。
個人の GitHub アカウントまたは組織からリポジトリを検出するか、
各リポジトリを正確な Git リビジョンに固定する
CSV を指定します。

  `@openai/codex-security` パッケージは公開されています。
  スキャンを実行するには Codex Security へのアクセス権が必要です。[CLI クイックスタート](/ja-JP/codex/security/cli) の手順に従って、
  CLI をインストールし、サインインしてください。

## リポジトリの取得元の選択

| 取得元           | 適した用途                                                                          |
| ---------------- | --------------------------------------------------------------------------------------- |
| GitHub からの検出 | 個人の GitHub アカウントまたは組織から、リポジトリを対話形式で選択します。 |
| CSV インベントリ    | 正確に指定したリポジトリのリビジョンを対象に、繰り返し実行可能な自動キャンペーンを実施します。                |

どちらのワークフローでも、進行状況とリポジトリごとの結果が保存され、中断後にキャンペーンを再開できます。

## GitHub リポジトリの検出

GitHub CLI でサインインします：

```bash
gh auth login

対話形式の一括スキャンを開始します：

```bash
npx @openai/codex-security bulk-scan

CLI が次の手順を案内します：

1. 個人の GitHub アカウントまたは組織を選択します。
2. 過去 90 日以内にアクティブだったリポジトリをレビューします。
3. リポジトリ一覧を検索し、スキャンするリポジトリを選択します。
4. スキャン結果の保存先ディレクトリを選択します。
5. 選択したリポジトリをレビューし、キャンペーンを確定します。

アーカイブ済みのリポジトリとフォークされたリポジトリは、検出対象から除外されます。
CLI は、選択した各リポジトリについて、デフォルトブランチの正確なコミットを
`<output-directory>/repositories.csv` に記録します。選択内容を確定するまで、
スキャンは開始されません。

GitHub Enterprise Server を使用するには、まず GitHub ホストにサインインします：

```bash
gh auth login --hostname github.example.com

リポジトリの検出を開始するときに `GH_HOST` を設定します：

```bash
GH_HOST=github.example.com npx @openai/codex-security bulk-scan

対話形式の検出にはターミナルが必要です。CI やコンテナで実行する場合、またはリポジトリ一覧を事前に用意している場合は、代わりに CSV インベントリを使用してください。

## リポジトリ CSV の作成

各リポジトリと固定するリビジョンを 1 行ずつ記載した CSV を作成します：

```csv
id,repository,revision,scope,mode,prompt
payments,https://github.com/example/payments.git,0123456789abcdef0123456789abcdef01234567,services/api,standard,Review payment authorization and refunds.
identity,https://github.com/example/identity.git,fedcba9876543210fedcba9876543210fedcba98,,deep,Review session and identity boundaries.

CSV では次の列を使用できます：

| 列       | 必須 | 説明                                                                                                |
| ------------ | -------- | ---------------------------------------------------------------------------------------------------------- |
| `id`         | はい      | 一意のリポジトリ識別子。使用できる文字は、英字、数字、ピリオド、ハイフン、アンダースコアです。                      |
| `repository` | はい      | HTTPS URL、SSH URL、またはローカルリポジトリのパス。相対パスは CSV ディレクトリを基準に解決されます。               |
| `revision`   | はい      | 40 文字または 64 文字の完全な Git コミット SHA。ブランチ名、タグ、短縮されたコミットハッシュはサポートされません。 |
| `scope`      | いいえ       | リポジトリからの相対パスで指定するスキャン対象ディレクトリ。値を省略すると、リポジトリ全体がスキャンされます。                       |
| `mode`       | いいえ       | `standard` または `deep`。値を省略すると、コマンドで選択したモードが使用されます。                                   |
| `prompt`     | いいえ       | このリポジトリに固有のスキャン指示。                                                             |

ローカルリポジトリの完全なコミット SHA を確認するには、次を実行します：

```bash
git -C /path/to/repository rev-parse HEAD

## CSV を使用したキャンペーンの実行

CSV と、リポジトリの外にある非公開の出力ディレクトリを指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

`--workers` はリポジトリスキャンの同時実行数を制御し、デフォルト値は `4` です。
各ディープスキャン内の独立した標準スキャンワーカーの数を設定するものではありません。
その上限は
[`[deep_scan]`](/ja-JP/codex/security/cli/reference#configure-deep-scans) で設定します。`--mode
deep` を指定すると、独自の `mode` が設定されていない行でディープスキャンが使用されます。
各 CSV 行では、スキャンモードとリポジトリの対象範囲を個別に選択できます。

キャンペーン内の各ディープスキャンでワーカーの実行を制限するには、`[deep_scan].max_time_hours` を設定します。
`--max-time-hours` フラグは `scan` で使用できますが、`bulk-scan` では使用できません。

CLI は、固定された各リビジョンをチェックアウトし、選択した対象をスキャンして結果を記録した後、一時的にチェックアウトしたリポジトリを削除します。リポジトリが完了と見なされるのは、スキャンが対象範囲を完全に網羅し、必要な結果アーティファクトがすべて存在する場合のみです。

## セキュリティコンテキストと指示の共有

アーキテクチャドキュメント、脅威モデル、セキュリティポリシーをすべてのスキャンに追加するには、
`--knowledge-base` を使用します。複数のファイルやディレクトリを追加する場合は、フラグを繰り返し指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

共有のスキャン指示を追加する場合や、各スキャンの後にフォローアップを実行する場合は、プロンプトファイルを指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --scan-prompt-file scan-instructions.md \
  --post-scan-prompt-file follow-up.md

CLI は、共有のスキャン指示の後に、CSV に記載された各リポジトリの `prompt` を追加します。
フォローアップ指示は、スキャンが成功した場合だけでなく、対象範囲の網羅が不完全な場合やエラーが発生した場合にも、
同じ認証済みセッションで実行されます。
ただし、キャンセルされた場合や、スキャンがコスト上限に達した場合は実行されません。プロンプトファイルのパスは、
現在のディレクトリを基準に解決されます。

## モデルと推論強度の選択

一括スキャンでは、デフォルトで `gpt-5.6-sol` を使用し、推論強度は `xhigh` です。
CSV キャンペーンで別のモデルと推論強度を選択するには、次のようにします：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --model gpt-5.6-terra \
  --effort high

対話形式でリポジトリを検出する場合も、同じオプションを使用できます：

```bash
npx @openai/codex-security bulk-scan --model gpt-5.6-terra --effort high

サポートされている推論強度は、`minimal`、`low`、`medium`、`high`、`xhigh` です。

OpenRouter を使用する場合は `OPENROUTER_API_KEY`、Fireworks を使用する場合は `FIREWORKS_API_KEY` を設定し、
`--provider` と `--model` を指定します。認証情報と使用例については、
[OpenRouter または Fireworks の
セットアップ](/ja-JP/codex/security/cli/reference#use-openrouter-or-fireworks) または [Amazon Bedrock の
セットアップ](/ja-JP/codex/security/cli/reference#use-amazon-bedrock) を参照してください。

## キャンペーン結果のレビュー

出力ディレクトリには、リビジョンを固定したキャンペーン情報、追記専用の結果台帳、リポジトリごと・試行ごとの個別アーティファクトが含まれます：

```text
security-scans/
├── manifest.json
├── results.jsonl
├── checkouts/
└── artifacts/
    ├── payments/
    │   └── attempt-1/
    │       ├── scan-manifest.json
    │       ├── findings.json
    │       ├── coverage.json
    │       └── report.md
    └── identity/
        └── attempt-1/
            ├── scan-manifest.json
            ├── findings.json
            ├── coverage.json
            └── report.md

- `manifest.json` には、キャンペーン内のリポジトリ、固定されたリビジョン、対象範囲、
  スキャンモード、共有指示またはリポジトリ固有の指示が記録されます。
- `results.jsonl` には、リポジトリごとの各試行、ステータス、アーティファクトディレクトリ、
  取得できたコスト情報やエラーの詳細が記録されます。
- `report.md` は、リポジトリの 1 回の試行についてまとめた、読みやすいレポートです。
- `findings.json` と `coverage.json` には、その試行の検出結果と、
  レビュー済みの対象範囲が記録されます。

結果を持ち出せる形式にするには、完了したリポジトリスキャンを 1 件エクスポートします：

```bash
npx @openai/codex-security export \
  /path/outside/repositories/security-scans/artifacts/payments/attempt-1 \
  --export-format sarif \
  --output /path/outside/repositories/payments.sarif

結果には、ソースコードの抜粋や脆弱性の詳細が含まれる場合があります。
出力ディレクトリはスキャン対象のリポジトリ外に置いて非公開にし、
適切な保持ポリシーに従って管理してください。

## キャンペーンの再開

同じ CSV と出力ディレクトリを使用して、元のコマンドを実行します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

CLI は未完了のリポジトリスキャンを再開し、完了済みのスキャンはスキップします。
カバレッジが不完全なスキャンは再試行されません。これらのスキャン結果は引き続き利用でき、
コマンドは終了コード `2` で終了します。

既存の出力ディレクトリでは、リポジトリインベントリ、スキャン指示、フォローアップ指示を
変更しないでください。CLI はピン留め済みのマニフェストを確認し、別の
キャンペーンを拒否します。リポジトリ、リビジョン、スコープ、スキャンモード、
共通の指示またはリポジトリ固有の指示を変更する場合は、新しい出力ディレクトリを使用してください。

## エラーが発生したリポジトリの再試行

`--max-attempts` を使用すると、一時的なチェックアウトエラーや
スキャンエラーが発生したリポジトリを再試行できます：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

デフォルトでは、リポジトリごとの試行は 1 回です。各試行には、
専用のレシートとアーティファクトディレクトリが割り当てられます。再試行の対象には、
チェックアウトエラー、スキャンの失敗、必須アーティファクトの欠落が含まれます。
カバレッジが不完全なまま完了したスキャンは再試行されません。

一括スキャンの終了コードは次のとおりです：

| 終了コード | 意味                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------- |
| `0`       | すべてのリポジトリの処理が正常に完了しました。                                                                              |
| `2`       | いずれかのリポジトリの処理が完了しなかった、スキャンのカバレッジが不完全だった、またはコマンドで入力エラーか実行時エラーが発生しました。 |
| `130`     | Ctrl-C によってキャンペーンが中断されました。                                                                                      |
| `143`     | SIGTERM によってキャンペーンが終了しました。                                                                                      |

## Docker での一括スキャンの実行

[Codex Security
リポジトリ](https://github.com/openai/codex-security)には、Linux の Docker ホスト上で
CSV キャンペーンを自動実行するための、セキュリティを強化した Compose 構成が含まれています。
ホストは、非特権ユーザーによるユーザー名前空間の作成をサポートしている必要があります。

リポジトリの CSV、スキャン結果、サインイン状態は、永続ディレクトリにマウントしたままにしてください。
OpenAI の認証情報は、環境またはシークレットマネージャーを通じて提供してください。
非公開の GitHub リポジトリでは、`GH_TOKEN` または `GITHUB_TOKEN`
を同じ方法で提供してください。

マウント済みの CSV と出力ディレクトリを使用してイメージを実行します：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

同じマウント済みの CSV と出力ディレクトリを使用して、キャンペーンを再開します。
GitHub Enterprise Server を使用する場合は、`CODEX_SECURITY_GIT_HOST` に GitHub ホストを設定してください。

利用可能なすべてのフラグについては、[bulk-scan
コマンドリファレンス](/ja-JP/codex/security/cli/reference#codex-security-bulk-scan)を参照してください。
スキャンのカバレッジや検出結果に関するよくある質問については、[CLI
のよくある質問](/ja-JP/codex/security/cli/faq)を参照してください。
