<!-- source: https://learn.chatgpt.com/ja-JP/docs/agent-configuration/agents-md -->

Codex は作業を始める前に `AGENTS.md` ファイルを読み込みます。グローバルガイダンスにプロジェクト固有のオーバーライドを重ねることで、どのリポジトリを開いても、一貫した前提で各タスクを開始できます。

## Codex によるガイダンスの検出

Codex は起動時に指示チェーンを構築します（実行ごとに 1 回。TUI では通常、新しいセッションを開始するたびに 1 回です）。ガイダンスは次の優先順位で検出されます：

1. **グローバルスコープ：** Codex ホームディレクトリ（デフォルトは `~/.codex`。ただし、`CODEX_HOME` を設定している場合を除きます）で、`AGENTS.override.md` が存在すれば Codex はそのファイルを読み込みます。存在しなければ `AGENTS.md` を読み込みます。この階層では、空でない最初のファイルだけを使用します。
2. **プロジェクトスコープ：** Codex はプロジェクトルート（通常は Git ルート）から現在の作業ディレクトリまで、ディレクトリを順にたどります。プロジェクトルートが見つからない場合は、現在のディレクトリだけを確認します。パス上の各ディレクトリでは、`AGENTS.override.md`、`AGENTS.md`、`project_doc_fallback_filenames` で指定されたフォールバック名の順に確認します。各ディレクトリから含めるファイルは最大 1 つです。
3. **マージ順：** Codex はルートから下位へ順にファイルを連結し、空行で区切ります。現在のディレクトリに近いファイルほど結合後のプロンプト内で後に現れるため、先に読み込まれたガイダンスをオーバーライドします。

Codex は空のファイルをスキップし、合計サイズが `project_doc_max_bytes` で定義された上限（デフォルトは 32 KiB）に達すると、ファイルの追加を停止します。これらの設定項目について詳しくは [プロジェクト指示の検出](/ja-JP/codex/config-file/config-advanced#project-instructions-discovery) を参照してください。上限に達した場合は、上限値を引き上げるか、指示をネストされた複数のディレクトリに分けて配置してください。

## グローバルガイダンスの作成

どのリポジトリでも作業上の取り決めが継承されるように、Codex ホームディレクトリに永続的なデフォルト設定を作成します。

1. ディレクトリが存在することを確認します：

   ```bash
   mkdir -p ~/.codex

2. 再利用できる設定を記述するため、`~/.codex/AGENTS.md` を作成します：

   ```md
   # ~/.codex/AGENTS.md

   ## Working agreements

   - Always run `npm test` after modifying JavaScript files.
   - Prefer `pnpm` when installing dependencies.
   - Ask for confirmation before adding new production dependencies.

3. 任意の場所で Codex を実行し、ファイルが読み込まれることを確認します：

   ```bash
   codex --ask-for-approval never "Summarize the current instructions."

   想定結果：Codex は作業内容を提案する前に、`~/.codex/AGENTS.md` の項目を引用して表示します。

ベースファイルを削除せずに一時的なグローバルオーバーライドが必要な場合は、`~/.codex/AGENTS.override.md` を使用します。共通ガイダンスに戻すには、オーバーライドを削除します。

## プロジェクト指示の階層化

リポジトリレベルのファイルにより、Codex はグローバルなデフォルト設定を継承しつつ、プロジェクトの規約も把握できます。

1. リポジトリのルートに、基本的なセットアップを記述した `AGENTS.md` を追加します：

   ```md
   # AGENTS.md

   ## Repository expectations

   - Run `npm run lint` before opening a pull request.
   - Document public utilities in `docs/` when you change behavior.

2. 特定のチームに異なるルールが必要な場合は、ネストされたディレクトリにオーバーライドを追加します。たとえば、`services/payments/` 内に `AGENTS.override.md` を作成します：

   ```md
   # services/payments/AGENTS.override.md

   ## Payments service rules

   - Use `make test-payments` instead of `npm test`.
   - Never rotate API keys without notifying the security channel.

3. payments ディレクトリから Codex を起動します：

   ```bash
   codex --cd services/payments --ask-for-approval never "List the instruction sources you loaded."

   想定結果：Codex は最初にグローバルファイル、次にリポジトリルートの `AGENTS.md`、最後に payments のオーバーライドを報告します。

Codex は現在のディレクトリに達した時点で検索を終了するため、オーバーライドは、対象となる作業にできるだけ近い場所に配置してください。

グローバルファイルと payments 固有のオーバーライドを追加したリポジトリの例を次に示します：

## コードレビュールールの追加

[GitHub での Codex コードレビュー](/ja-JP/codex/third-party/github#customize-what-codex-reviews) では、
`## Code Review Rules` セクションを、ルールの対象コードに最も近い `AGENTS.md` に
追加します。リポジトリ全体のチェックはルートに、サービス固有の
チェックはネストされたファイルに配置します。

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

ルールは簡潔にし、指摘すべき動作と、安全な対応方法または
例外を説明してください。フォーマットや lint のチェックは CI に任せます。詳しくは [Codex の
レビュー対象のカスタマイズ](/ja-JP/codex/third-party/github#customize-what-codex-reviews) で、
セットアップとルール作成のガイダンスを確認してください。

## フォールバックファイル名のカスタマイズ

リポジトリですでに別のファイル名（例：`TEAM_GUIDE.md`）を使用している場合は、それをフォールバックリストに追加すると、Codex が指示ファイルとして扱います。

1. Codex の構成を編集します：

   ```toml
   # ~/.codex/config.toml
   project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
   project_doc_max_bytes = 65536

2. 更新した構成を読み込むために、Codex を再起動するか、新しいコマンドを実行します。

これで Codex は各ディレクトリを `AGENTS.override.md`、`AGENTS.md`、`TEAM_GUIDE.md`、`.agents.md` の順に確認します。このリストにないファイル名は、指示の検出時に無視されます。引き上げたバイト数の上限により、切り詰められる前により多くのガイダンスを結合できます。

フォールバックリストを設定すると、Codex は代替ファイルを指示として扱います：

プロジェクト固有の自動化ユーザー用など、別のプロファイルを使用する場合は、`CODEX_HOME` 環境変数を設定します：

```bash
CODEX_HOME=$(pwd)/.codex codex exec "List active instruction sources"

想定結果：出力には、カスタム `.codex` ディレクトリを基準とするファイルパスが一覧表示されます。

## セットアップの確認

- リポジトリのルートで `codex --ask-for-approval never "Summarize the current instructions."` を実行します。Codex はグローバルファイルとプロジェクトファイルのガイダンスを、優先順位に従って出力するはずです。
- ネストされたオーバーライドが、より広い範囲のルールを置き換えることを確認するには、`codex --cd subdir --ask-for-approval never "Show which instruction files are active."` を使用します。
- Codex が読み込んだ指示ファイルを監査するには、`codex -c log_dir=./.codex-log` でプレーンテキストの TUI ログを有効にして `./.codex-log/codex-tui.log` を確認するか、セッションログを有効にしている場合は最新の `session-*.jsonl` ファイルを確認します。
- 指示が古いように見える場合は、対象のディレクトリで Codex を再起動します。Codex は実行のたびに（さらに、各 TUI セッションの開始時にも）指示チェーンを再構築するため、手動で消去するキャッシュはありません。

## 検出に関する問題のトラブルシューティング

- **何も読み込まれない：** 目的のリポジトリにいることと、`codex status` が想定どおりのワークスペースルートを報告していることを確認してください。指示ファイルに内容があることも確認してください。Codex は空のファイルを無視します。
- **誤ったガイダンスが表示される：** ディレクトリツリーの上位か Codex ホームディレクトリ内に `AGENTS.override.md` がないか確認してください。通常のファイルにフォールバックするには、そのオーバーライドの名前を変更するか削除します。
- **Codex がフォールバック名を無視する：** `project_doc_fallback_filenames` に対象のファイル名をタイプミスなく指定したことを確認してから、更新した構成を反映するために Codex を再起動します。
- **指示が切り詰められる：** 重要なガイダンスが欠けないように、`project_doc_max_bytes` の値を引き上げるか、大きなファイルをネストされた複数のディレクトリに分割してください。
- **プロファイルが想定と異なる：** Codex を起動する前に `echo $CODEX_HOME` を実行します。デフォルト以外の値が表示された場合、Codex は、ファイルを編集したホームディレクトリとは別の場所を参照します。

## 次のステップ

- 詳しくは、公式の [AGENTS.md](https://agents.md) ウェブサイトをご覧ください。
- 永続的なガイダンスと相性のよい対話パターンについては [Codex へのプロンプト](/ja-JP/codex/prompting) を参照してください。
