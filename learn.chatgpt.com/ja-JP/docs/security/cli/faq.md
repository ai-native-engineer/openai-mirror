<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/cli/faq -->

リポジトリのスキャンや、ターミナルでのセキュリティ検出結果の管理について、
よくある質問に回答します。インストールと最初のスキャンについては、
[CLI クイックスタート](/ja-JP/codex/security/cli) を参照してください。

## リポジトリのスキャン

### CLI の利用対象者

`@openai/codex-security` パッケージは公開されています。

スキャンの実行には Codex Security へのアクセス権が必要です。より良い結果を得るには、
[Trusted Access for Cyber](https://chatgpt.com/cyber) の認証を受けたアカウントを使用してください。

### サインイン後もスキャンで API キーが使用される理由

環境に `OPENAI_API_KEY` または `CODEX_API_KEY` が設定されている場合、対話型ターミナルを使用しないスキャンや
JSON 形式および JSONL 形式のスキャンでは、ChatGPT またはアクセストークンによるログインに成功していても、
デフォルトで環境変数の API キーが使用されます。
テキストを出力する対話型スキャンでは、ChatGPT でのサインインも利用できる場合、
認証方法の選択を求められます。ドライランでは、入力を求められることも、認証情報が読み込まれることもありません。

保存済みの認証情報をスキャンで使用するには、明示的に選択します：

```bash
npx @openai/codex-security scan . --auth chatgpt

`OPENAI_API_KEY` または `CODEX_API_KEY` に設定された API キーの使用を必須にするには：

```bash
npx @openai/codex-security scan . --auth api-key

保存済みの認証情報をデフォルトで自動的に使用するには、
`unset OPENAI_API_KEY CODEX_API_KEY` を実行します。サポートされているすべての認証モードについては、
[CLI リファレンス](/ja-JP/codex/security/cli/reference#select-scan-authentication) を参照してください。

### リポジトリ一括スキャンの仕組み

GitHub CLI でサインインします：

```bash
gh auth login

GitHub のアカウントまたは組織からリポジトリを検出し、選択します：

```bash
npx @openai/codex-security bulk-scan

作成済みのリストを使う場合は、リポジトリの CSV と出力ディレクトリを指定します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4

GitHub でのリポジトリ検出、CSV 形式、
キャンペーンの結果、利用可能なオプションについては、[セキュリティスキャンの一括実行](/ja-JP/codex/security/cli/bulk-scans) を参照してください。

### 中断した一括スキャンの再開方法

はい。元の CSV と出力ディレクトリを指定して、同じ一括スキャンコマンドを実行します。Codex Security は処理が完了したリポジトリをスキップします。

リポジトリまたはスキャンの一時的なエラーを再試行するには、`--max-attempts 3` を追加します：

```bash
npx @openai/codex-security bulk-scan repositories.csv \
  --output-dir /path/outside/repositories/security-scans \
  --workers 4 \
  --max-attempts 3

カバレッジが `partial` または `unknown` の完了済みスキャンでは結果が保持され、
キャンペーンは終了コード `2` で終了します。
`--max-attempts` を指定しても、このスキャンは再試行されません。

### スキャンでのアーキテクチャとセキュリティポリシーの活用方法

アーキテクチャに関するドキュメント、脅威モデル、セキュリティポリシーを
`--knowledge-base` で指定します：

```bash
npx @openai/codex-security scan . \
  --knowledge-base /path/to/architecture.md \
  --knowledge-base /path/to/security-policies

Codex Security は、これらのドキュメントを現在のスキャンのコンテキストとして使用します。
対応するファイル形式とディレクトリの動作については、[セキュリティ
コンテキストの追加](/ja-JP/codex/security/cli/reference#add-security-context) を参照してください。

## 検出結果とカバレッジ

### チームによる過去のスキャン結果の確認方法

リポジトリの保存済みスキャンを一覧表示します：

```bash
npx @openai/codex-security scans list /path/to/repository

結果に含まれるスキャン ID を使って、そのスキャンの検出結果を確認します：

```bash
npx @openai/codex-security scans show SCAN_ID

完了した各スキャンでは、レポート、検出結果、カバレッジ、関連アーティファクトが
まとめて保存されます。全体の構成については、[スキャン
アーティファクト](/ja-JP/codex/security/cli/reference#scan-artifacts) を参照してください。

保存されたスキャンイベントとワーカーイベントを確認するには、`scans logs SCAN_ID` を実行します。
これらのログはマスキングされておらず、ソースコードや認証情報が含まれる場合があります。

### CLI でスキャン履歴を保存できない場合の対処方法

Codex Security は、スキャン履歴をワークベンチのデータベースに保存します。デフォルトの状態ディレクトリに書き込めない場合は、リポジトリ外にある非公開のディレクトリを選択します：

```bash

### スキャンにおける新規と既知の検出結果の区別方法

リポジトリに対するすべてのスキャンから、未解決の検出結果を一覧表示します：

```bash
npx @openai/codex-security findings list /path/to/repository

この一覧では、最新のスキャンで確認された検出結果と、そのスキャンで確認されなかった過去の未解決の検出結果が区別されます。

2 回のスキャンの検出結果を比較します：

```bash
npx @openai/codex-security scans compare PREVIOUS_SCAN_ID CURRENT_SCAN_ID

比較では、根本原因に基づいて検出結果が自動的に照合され、保存済みの照合結果が再利用されます。これにより、新規、継続中、再オープン、解決済み、不明の各検出結果が識別されます。後のスキャンで元のターゲットと影響を受けたパスが漏れなくカバーされている場合にのみ、検出結果は解決済みと見なされます。

### 誤検出に関するフィードバックの仕組み

保存済みのスキャンを確認し、オカレンス ID を特定します：

```bash
npx @openai/codex-security scans show SCAN_ID

その検出結果が該当しない理由を記録します：

```bash
npx @openai/codex-security findings false-positive FINDING_OCCURRENCE_ID \
  --reason "The framework escapes this input before it reaches the query"

同じリポジトリに対する今後のスキャンでは、その説明がコンテキストとして使用されます。ただし、現在のソースコード、制御策、到達可能性は引き続き独立して検証されます。検出結果を却下しても、ルール、パス、脆弱性クラスは抑制されません。

コマンドの詳細については、[検出結果の
リファレンス](/ja-JP/codex/security/cli/reference#codex-security-findings) を参照してください。

### スキャンを繰り返すと検出結果が異なる理由

AI を利用したスキャンでは、同じスキャン構成でも結果が変わることがあります。まず、ベースラインスキャンを再実行します：

```bash
npx @openai/codex-security scans rerun BASELINE_SCAN_ID

再実行時には元のスキャン構成が維持され、同じバージョンのプラグインが必要です。インストール済みのプラグインが変更されている場合、コマンドは停止します。

ベースラインと新しいスキャンを比較します：

```bash
npx @openai/codex-security scans compare BASELINE_SCAN_ID REPEAT_SCAN_ID

コンテキストの不足が結果のばらつきにつながる可能性がある場合は、アーキテクチャとセキュリティに関する共通のガイダンスを提供します。照合により、複数回の実行で同じ根本的な問題に対応する検出結果を特定できますが、スキャン結果が毎回同じになるわけではありません。表示されなくなった重要な検出結果は、直接再確認してください。

### チームによる修正の有効性の確認方法

修正を適用したら、元のスキャンを再実行します：

```bash
npx @openai/codex-security scans rerun BEFORE_SCAN_ID

元の検出結果と新しいスキャンを比較します：

```bash
npx @openai/codex-security scans compare BEFORE_SCAN_ID AFTER_SCAN_ID

新しいスキャンが元のターゲットと影響を受けたパスを漏れなくカバーしていることを確認します。次に、元の検出結果を現在のチェックアウトに対して直接再確認します：

```bash
npx @openai/codex-security validate /path/to/original/findings.json \
  "Recheck the SQL injection in src/orders.ts:42 against the current code"

検出結果が見つからなくなったことや、スキャン結果の比較だけでは、修正が有効だったことは証明できません。

### 不完全なカバレッジの意味

カバレッジは `complete`、`partial`、`unknown` のいずれかです。スキャンをレビューの証拠として扱う前に、`coverage.json` で
除外されたパス、保留された対象領域、未解決事項を
確認してください。

カバレッジが部分的または不明のスキャンでは、重大度ポリシーがない場合でも終了コード `2` が返されます。
利用可能な検出結果とカバレッジは保持されます。
後のスキャンが以前の検出結果の元のパスをカバーしていない場合、
その検出結果が存在しなくなったとは判断できません。

## 自動化とコスト

### ディープスキャンの時間制限の仕組み

ディープスキャンの開始時に、ワーカーの実行期限を設定します：

```bash
npx @openai/codex-security scan . --mode deep --max-time-hours 1.5

デフォルトは `96` 時間です。`96` 以下の正の値であれば、
小数も指定できます。期限に達すると、Codex Security は未完了のワーカーを停止し、
完了済みの標準スキャンの結果を保持して最終レポートに集約します。
どのワーカーもソースコードのレビューを完了していない場合、レポートには部分的なカバレッジが記録され、
CLI は終了コード `2` を返します。

設定を永続化する場合や一括キャンペーンでは、`max_time_hours` を
`[deep_scan]` 配下に設定します。[ディープスキャンの
構成](/ja-JP/codex/security/cli/reference#configure-deep-scans) を参照してください。

### スキャンのコスト上限の仕組み

スキャンを開始する前に、推定コストの上限を USD で設定します：

```bash
npx @openai/codex-security scan . --max-cost 5

この上限は見積もりであり、支出を厳密に制限するものではありません。
すでに進行中のリクエストは、上限を超えて完了する場合があります。
Codex Security が完了したワーカーの結果を集約した後にディープスキャンが上限に達した場合、
CLI は部分的なカバレッジを記録した完成済みのレポートを保存し、終了コード `2` で終了します。
それ以外の場合は、利用可能な部分的な出力が保持されます。

### スキャンによるコミットと Pull Request のチェック

ステージ済みと未ステージの変更を対象とするコミット前のセキュリティチェックをインストールします。

```bash
npx @openai/codex-security install-hook

Pull Request のチェックでは、コミット済みの変更をスキャンし、重大度のしきい値を設定します。

```bash
npx @openai/codex-security scan . \
  --diff origin/main \
  --fail-on-severity high

完全なスキャンでは、選択した重大度以上の問題が見つかると、終了コード `1` が返されます。
詳細は[CI でのスキャンの実行](/ja-JP/codex/security/cli/ci)を参照してください。
GitHub Actions の完全なワークフロー、アーティファクトの取り扱い、SARIF のエクスポートについて説明しています。

### 別のアプリケーションからのスキャンの直接実行

はい。[TypeScript SDK](/ja-JP/codex/security/sdk) を使用すると、アプリケーションや開発ツールからスキャンを開始し、
対象を選択して、検出結果とカバレッジを確認し、進捗を追跡して、
コストを制御できます。
