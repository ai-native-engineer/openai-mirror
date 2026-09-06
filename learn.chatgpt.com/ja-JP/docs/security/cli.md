<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli -->

Codex Security は、セキュリティチームとエンジニアリングチームによる脆弱性の発見、確認、修正を支援します。コマンドラインインターフェース（CLI）を使用して、自分が所有しているリポジトリや評価を許可されているリポジトリをスキャンし、検出事項を継続的にレビューして、変更が取り込まれる前に確認できます。

  `@openai/codex-security` パッケージは公開されています。スキャンの実行には
  Codex Security へのアクセス権が必要です。Codex で対話型スキャンを実行するには、[Codex Security
  プラグインのクイックスタート](/ja-JP/codex/security/plugin)から始めてください。接続済みの GitHub リポジトリについては、
  [Codex Security クラウドのセットアップ](/ja-JP/codex/security/setup)を参照してください。

## 前提条件の確認

CLI には Node.js 22（22.13.0 以降）、24、または 26 が必要です。スキャン、一括スキャン、
エクスポート、スキャン履歴、保存済みの検出事項を利用するには、Python 3.10 以降も必要です。
詳細については、[認証と
前提条件](/ja-JP/codex/security/cli/reference#authentication-and-prerequisites)を参照してください。

## CLI のセットアップと検証

`npx` で CLI を実行し、バージョンを確認します：

```bash
npx @openai/codex-security --version

パッケージと同梱プラグインの両方のバージョンを確認するには、次を実行します：

```bash
npx @openai/codex-security info --json

パッケージの変更点については、
[CLI と SDK のリリース](https://github.com/openai/codex-security/releases)を参照してください。

利用可能なコマンドを一覧表示します：

```bash
npx @openai/codex-security --help

[CLI リファレンス](/ja-JP/codex/security/cli/reference)も参照してください。

## サインイン

ローカルで使用する場合は、ChatGPT アカウントでサインインします：

```bash
npx @openai/codex-security login

リモートマシンまたはヘッドレスマシンでは、デバイス認証を使用します：

```bash
npx @openai/codex-security login --device-auth

CI などの自動化ワークフローでは、OpenAI API キーを設定します：

```bash

AWS の認証情報については、[Amazon Bedrock
のセットアップ](/ja-JP/codex/security/cli/reference#use-amazon-bedrock)を参照してください。[OpenRouter または
Fireworks](/ja-JP/codex/security/cli/reference#use-openrouter-or-fireworks) を使用する場合は、
プロバイダーの API キーを設定し、`--provider` と `--model` でモデルを選択します。

API キーも設定されている場合に ChatGPT でのサインインを使用するには、明示的に選択します：

```bash
npx @openai/codex-security scan . --auth chatgpt

環境に設定された API キーの使用を必須にするには、API キー認証を選択します：

```bash
npx @openai/codex-security scan . --auth api-key

アカウントやリポジトリによっては、
リポジトリ全体のスキャンに [Trusted Access for Cyber](https://chatgpt.com/cyber) も必要になる場合があります。

## スキャンの準備

信頼でき、評価の許可を得ているリポジトリを選択してください。
スキャンではローカルのオペレーティングシステムの権限が使用され、承認を求めて一時停止することはありません。
スキャンプロセスは環境を継承する可能性があるため、開始前に無関係な認証情報を削除してください。
詳しくは、[ローカルスキャンの
権限](/ja-JP/codex/security/cli/reference#local-scan-permissions)を参照してください。

スキャン結果の保存先として、リポジトリの外部にあるディレクトリを選択します：

```bash
REPOSITORY=/path/to/repository
SCAN_DIR=/path/outside/repository/codex-security-results

`--output-dir` を省略すると、Codex Security は専用の永続的な状態ディレクトリに結果を保存します。
結果にはソースコードの抜粋や脆弱性の詳細が含まれる場合があるため、
非公開の保存場所と適切な保持ポリシーを選択してください。

デフォルトの状態ディレクトリに書き込めない場合は、スキャン対象のリポジトリ外にある書き込み可能なディレクトリを選択します：

```bash

スキャンを開始する前に、リポジトリ、ターゲット、出力ディレクトリを確認します：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --dry-run

ドライランでは、`--knowledge-base` で指定されたパスを含むローカル入力を確認します。
Codex の起動、認証情報の読み込み、プラグインの Python
インタープリターの検査は行いません。

## 初回スキャンの実行

標準スキャンを実行し、選択したディレクトリに結果を保存します：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR"

対話型ターミナルには、スキャンのライブダッシュボードが表示されます。`--headless` を追加すると、
代わりに進行状況がプレーンテキストで行単位に表示されます。CI や対話型セッションのないターミナルでは、
進行状況が自動的にプレーンテキストで表示されます。

ダッシュボードには、進行中のセッションの詳細も表示されます。ソースコードや認証情報が含まれる場合があるため、共有する前に内容を確認してください。

デフォルトでは、CLI はスキャンの進行状況と完了時の概要を stderr に書き込みます。スキャン結果全体は stdout に出力しません。スキャンが完了すると、次のような概要が出力されます：

```text
  REPORT    /path/outside/repository/codex-security-results/report.md

  FINDINGS  2 (2 confirmed this scan; 0 previously found; 1 high, 1 medium)
  COVERAGE  complete
  ELAPSED   42s
  RESULTS   /path/outside/repository/codex-security-results

トークン使用量と推定コストは、取得できる場合に表示されます。完全な結果を機械可読な JSON として出力するには、構造化出力を明示的に指定します：

```bash
npx @openai/codex-security scan "$REPOSITORY" --output-dir "$SCAN_DIR" --json

スキャンはデフォルトではレポートのみを生成するため、検出事項をローカルでレビューできます。
[CI
でのスキャン実行](/ja-JP/codex/security/cli/ci)の準備が整ったら、重大度のしきい値の追加を検討してください。

## モデルと推論強度の選択

スキャンでは、デフォルトでモデル `gpt-5.6-sol` と推論強度 `xhigh` が使用されます。
タスクで必要な場合は、別のモデルと推論強度を選択します：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --model gpt-5.6-terra \
  --effort high

サポートされる推論強度は、`minimal`、`low`、`medium`、`high`、`xhigh`、
`max` です。

## 結果のレビュー

読みやすい形式の結果を確認するには、`report.md` を開きます。
スキャンディレクトリには、自動化で使用する構造化ファイルも含まれています：

```text
codex-security-results/
├── scan-manifest.json
├── findings.json
├── coverage.json
├── report.md
├── artifacts/
└── exports/
    └── results.sarif       # when produced

- `scan-manifest.json` には、ターゲット、スコープ、生成元、
  封印されたアーティファクトが記録されます。
- `findings.json` には、各検出事項の重大度、信頼度、該当箇所、根拠、
  修正方法が記録されます。
- `coverage.json` には、レビュー済みの領域、除外項目、保留中の作業、
  未解決事項、カバレッジの完全性が記録されます。

カバレッジは `complete`、`partial`、`unknown` のいずれかです。
スキャンをレビュー実施の証拠として扱う前に、保留中の領域や未解決事項を確認してください。
[CLI リファレンス](/ja-JP/codex/security/cli/reference#scan-artifacts)では、
アーティファクトと出力に関する完全な仕様を説明しています。

## 検出事項のレビューとパッチ適用

検出事項がある対話型スキャンが完了すると、CLI に検出事項ブラウザが表示されます。根拠を確認し、修正する検出事項を選択してください。保存されたタスクは Codex デスクトップアプリで確認できます。

重大度が高い検出事項や致命的な検出事項に、ブラウザを使用せずにパッチを適用するには：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --patch --patch-severity high --json

検証済みのパッチをコミットし、GitHub の Pull Request を作成するには、`--create-pr` を追加します。

保存済みの検出事項にパッチを適用したり、Linear のイシューをインポートしたりすることもできます。
[`validate` と `patch` のリファレンス](/ja-JP/codex/security/cli/reference#codex-security-validate-and-codex-security-patch)を参照してください。

## 次に実行するスキャンの選択

リポジトリに個別のサービスやパッケージが含まれる場合は、パススキャンを使用します：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --path services/billing \
  --path packages/auth

ベースリビジョンから `HEAD` までのコミット済みの変更をレビューします：

```bash
npx @openai/codex-security scan "$REPOSITORY" --diff origin/main --head HEAD

ステージ済みおよび未ステージの変更を `HEAD` と比較してレビューします：

```bash
npx @openai/codex-security scan "$REPOSITORY" --working-tree --base HEAD

差分スキャンとワーキングツリースキャンでは、リポジトリ引数に Git Worktree のルートを指定する必要があります。差分スキャンを開始する前に、選択したリビジョンをフェッチしてください。

リポジトリまたはパスをより広範にレビューする必要がある場合は、deep モードを使用します：

```bash
npx @openai/codex-security scan "$REPOSITORY" --mode deep

ワーカー、サブエージェント、スキャンの停止タイミングを制御するには：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --mode deep \
  --workers 2 \
  --subagents 0 \
  --stop-after-no-new 3 \
  --max-discovery-runs 10 \
  --max-time-hours 1.5

これらのオプションには deep モードが必要です。deep モードはリポジトリとパスを対象とするスキャンに対応していますが、
差分スキャンやワーキングツリースキャンには対応していません。ここで、`--workers` は 1 回のスキャン内で独立して実行される標準スキャンワーカーを制御し、
`bulk-scan --workers` は同時に実行するリポジトリスキャンを制御します。
`--max-time-hours` には `96` 時間以下の正の値を指定でき、
小数による時間指定も可能です。上限に達すると、スキャンは未完了のワーカーを停止し、
完了済みのスキャン結果を保持して、最終レポートに集約します。

## アーキテクチャとセキュリティのコンテキストの追加

アーキテクチャ文書、脅威モデル、セキュリティポリシーをスキャンのコンテキストとして指定します。これにより、Codex Security はシステムの実際の仕組みに照らして検出事項を評価できます：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

## カスタムスキャン指示の追加

セキュリティ上の優先事項を重点的にスキャンするための指示を追加します。フォローアップの指示には、2 つ目のファイルを使用します：

```bash
npx @openai/codex-security scan "$REPOSITORY" \
  --scan-prompt-file /path/to/scan.md \
  --post-scan-prompt-file /path/to/follow-up.md

フォローアップは、成功したスキャンの後や、カバレッジが不完全なスキャンまたはエラーが発生したスキャンの後に、
同じ認証済みセッションで実行されます。フォローアップが失敗した場合は、
CLI が警告を表示し、完了済みのスキャンを保持します。
キャンセル後や、コスト上限に達したスキャンの後には実行されません。
どちらのオプションも `bulk-scan` で使用でき、CSV の `prompt` 列でリポジトリ固有の指示を追加できます。

## スキャン予算の設定

`--max-cost` を使用すると、モデルの推定コストが USD 建ての上限を超えた時点で、
スキャンを停止できます：

```bash
npx @openai/codex-security scan "$REPOSITORY" --max-cost 5

すでに進行中のリクエストは、上限をわずかに超えて完了する場合があります。
Codex Security が完了済みのワーカーの結果を集約した後に deep スキャンが上限に達した場合、
CLI は完成したレポートを保存し、カバレッジを `partial` として記録して、
終了コード `2` を返します。スキャンで完成したレポートを生成できない場合は、
利用可能な部分的な出力がディスク上に保持されます。

## 各コミット前の変更のスキャン

リポジトリに Git の pre-commit セキュリティチェックをインストールします：

```bash
npx @openai/codex-security install-hook

このチェックは、各コミットの前にステージ済みと未ステージの変更をスキャンします。既存の pre-commit スクリプトを置き換えることなく、重大度の高い検出結果やスキャンエラーがある場合にコミットをブロックします。

## リポジトリの一括スキャン

リポジトリを検出する前に GitHub にサインインします：

```bash
gh auth login

GitHub アカウントまたは組織からリポジトリを検出し、選択します：

```bash
npx @openai/codex-security bulk-scan

対話形式のフローでは、アーカイブ済みのリポジトリとフォークされたリポジトリが除外されます。スキャンを開始する前に、選択したリポジトリの確認を求められます。

準備済みのリポジトリ一覧をスキャンするには、CSV と出力ディレクトリを指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

同じコマンドを再実行すると、既存の一括スキャンを再開できます。
Codex Security は完了済みのリポジトリをスキップします。`--max-attempts 3` を追加すると、
一時的なリポジトリエラーやスキャンエラーの発生時に再試行できます。

GitHub でのリポジトリ検出、CSV の準備、キャンペーン結果、Docker のセットアップについては、
[セキュリティスキャンの一括実行](/ja-JP/codex/security/cli/bulk-scans)を参照してください。

## Docker での一括スキャンの実行

Codex Security の Docker イメージを利用できる場合は、提供されている堅牢化済みの Compose 構成とセキュリティプロファイルを Linux の Docker ホストで使用します。ホストは非特権ユーザー名前空間の作成に対応している必要があります。リポジトリの CSV を指定し、結果とサインイン状態を永続化用のマウントディレクトリに保存し、認証情報を環境またはシークレットマネージャーを通じて渡します：

```bash
docker compose run --rm codex-security \
  bulk-scan /input/repositories.csv \
  --output-dir /output \
  --workers 4

コンテナは対話型プロンプトなしで一括スキャンを実行します。
リポジトリを対話形式で検出する場合は、Docker の外で CLI を使用します。
プライベートリポジトリの場合は、`GH_TOKEN` または `GITHUB_TOKEN` を環境またはシークレットマネージャーを通じて渡します。
アカウントとリポジトリへのアクセスを含む[サインイン要件](#sign-in)は、
コンテナ内のスキャンにも適用されます。

## 保存済みスキャンの再確認

リポジトリの保存済みスキャンを一覧表示します：

```bash
npx @openai/codex-security scans list "$REPOSITORY"

結果からスキャン ID をコピーし、その検出結果と構成を確認します：

```bash
npx @openai/codex-security scans show SCAN_ID

スキャンおよびそのワーカーの保存済みイベントを確認するには：

```bash
npx @openai/codex-security scans logs SCAN_ID

保存されたログはマスキングされておらず、ソースコードや認証情報が含まれている可能性があります。共有する前に内容を確認してください。

リポジトリのすべてのスキャンにおける未解決の検出結果を一覧表示します：

```bash
npx @openai/codex-security findings list "$REPOSITORY"

最新のスキャンで確認されなかった場合でも、以前の検出結果は未解決のままです。

レビュー済みの検出結果を誤検知としてマークするには、その検出結果が該当しない理由を説明します：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The route already checks permissions"

以降のスキャンでは、その説明を考慮しつつ、現在のコードを再確認します。

元の構成を使用して、現在のチェックアウトに対して同じスキャンを実行します：

```bash
npx @openai/codex-security scans rerun SCAN_ID

新規、継続中、再オープン、解決済み、または状態不明の検出結果を特定するには、2 つのスキャンを比較します：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較では、根本原因に基づいて検出結果を自動的に照合し、保存済みの照合結果を再利用します。

一括スキャン用 CSV の形式、スキャン履歴のフィルター、コマンドオプションについては、
[CLI リファレンス](/ja-JP/codex/security/cli/reference)を参照してください。

目的に合うワークフローを選んで続行します：

- [セキュリティスキャンの一括実行](/ja-JP/codex/security/cli/bulk-scans)では、GitHub リポジトリを検出したり、
  ピン留め済みの CSV インベントリをスキャンしたりできます。
- [CLI のよくある質問](/ja-JP/codex/security/cli/faq)では、スキャン履歴、
  誤検知に関するフィードバック、カバレッジ、修正の検証についての回答を確認できます。
- [CI でのスキャンの実行](/ja-JP/codex/security/cli/ci)により、Pull Request のレビュー、
  結果の保存、重大度ポリシーの設定を行えます。
- [CLI リファレンス](/ja-JP/codex/security/cli/reference)で、すべてのフラグ、
  出力形式、アーティファクト、終了コードを確認できます。
- [TypeScript SDK の統合](/ja-JP/codex/security/sdk)により、
  アプリケーションまたは開発ツールからスキャンを実行できます。
