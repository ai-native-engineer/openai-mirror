<!-- source: https://learn.chatgpt.com/ja-JP/docs/config-file/environment-variables -->

Codex では、永続的な設定に `config.toml` を使用します。
シェルスコープでの設定の上書き、自動化処理用のシークレット、インストーラーの動作制御、診断には、環境変数を使用します。

このページには、Codex が直接読み取る公開環境変数のうち、安定して利用できるものを掲載しています。
内部開発用変数、テスト用変数、または
プロバイダー固有のシークレット名（
[`env_key`](/ja-JP/codex/config-file/config-advanced#custom-model-providers) で独自に指定するもの）は掲載していません。

## 主要な保存場所

| 変数            | 使用箇所                                    | デフォルト      | 説明                                                                                                                                                      |
| ------------------- | ------------------------------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_HOME`        | CLI、IDE 拡張機能、App Server、インストーラー | `~/.codex`   | 構成、認証情報、ログ、セッション、スキル、スタンドアロンパッケージのメタデータなど、Codex の状態データを格納するルートディレクトリを設定します。設定する場合は、そのディレクトリがあらかじめ存在している必要があります。 |
| `CODEX_SQLITE_HOME` | CLI と App Server の状態データ                   | `CODEX_HOME` | SQLite を利用する状態データの保存先を設定します。構成オプションの `sqlite_home` が優先されます。相対パスは、現在の作業ディレクトリを基準に解決されます。           |

`CODEX_HOME` 配下に保存されるファイルの詳細については、
[構成と状態データの保存場所](/ja-JP/codex/config-file/config-advanced#config-and-state-locations) を参照してください。

## インストーラー用変数

これらの変数は、
`https://chatgpt.com/codex/install.sh` と
`https://chatgpt.com/codex/install.ps1` で配信されるスタンドアロンインストールスクリプトに適用されます。

| 変数                | デフォルト                                                                              | 説明                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_NON_INTERACTIVE` | `false`                                                                              | インストーラーのプロンプトをスキップするには、`1`、`true`、`yes` のいずれかに設定します。各プロンプトではデフォルトの応答が選択されるため、初回セットアップではなく、スクリプトによるインストールや更新に使用してください。 |
| `CODEX_INSTALL_DIR`     | `~/.local/bin`（macOS/Linux）、`%LOCALAPPDATA%\Programs\OpenAI\Codex\bin`（Windows） | 実際に呼び出される `codex` コマンドのインストール先を変更します。スタンドアロンパッケージのキャッシュは、引き続き `CODEX_HOME/packages/standalone` 配下に保存されます。                        |

無人インストールを行うには、シェルで `CODEX_NON_INTERACTIVE=1` を設定し、そのシェルから
ダウンロードしたインストーラーを実行します：

```bash
curl -fsSL https://chatgpt.com/codex/install.sh | CODEX_NON_INTERACTIVE=1 sh

```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex

## 認証とネットワーク

| 変数                           | 使用箇所                                          | 説明                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `CODEX_API_KEY`                    | Exec、レビュー、TypeScript SDK、リモート exec-server | 非対話モードの Codex プロセスに API キーを渡します。リポジトリ管理下のコードを実行する場合は、ジョブ全体ではなく、インラインで設定してください。             |
| `CODEX_ACCESS_TOKEN`               | CLI、App Server、信頼できる自動化処理              | 信頼できる自動化処理で使用する ChatGPT または Codex のアクセストークンを指定します。ログイン情報を永続化するには、このトークンを `codex login --with-access-token` にパイプで渡します。             |
| `OPENAI_FEDERATION_RULE_ID`        | ワークロード ID                                | ワークロード用に構成されたフェデレーションルールを選択します。                                                                                        |
| `OPENAI_IDENTITY_TOKEN_FILE`       | ワークロード ID                                | 現在の OIDC トークンまたは SPIFFE JWT-SVID が格納されたファイルの絶対パスを指定します。                                                |
| `OPENAI_WORKLOAD_IDENTITY_CONTEXT` | ワークロード ID                                | クライアントが報告する監査上の帰属情報として、制限付きの JSON 識別子を任意で指定できます。認証や認可には影響しません。         |
| `CODEX_CA_CERTIFICATE`             | HTTPS、ログイン、WebSocket の各クライアント              | 企業内で TLS 通信をインターセプトする環境や、プライベートルート証明書を使用する環境向けに、PEM 形式の CA バンドルを指定します。`SSL_CERT_FILE` より優先されます。 |
| `SSL_CERT_FILE`                    | HTTPS、ログイン、WebSocket の各クライアント              | `CODEX_CA_CERTIFICATE` が設定されていない場合に使用する、フォールバック用の PEM 形式の CA バンドルのパスです。                                                                               |

プロバイダーの API キーを使用する場合は、
[`env_key`](/ja-JP/codex/config-file/config-advanced#custom-model-providers) をモデルプロバイダーの構成で設定します。
Codex はその構成で指定された名前の変数を読み取るため、
変数名自体は Codex の固定の環境変数ではありません。

自動化処理でのシークレットの取り扱いについては、
[API キー認証の使用](/ja-JP/codex/non-interactive-mode#use-api-key-auth) を参照してください。
アクセストークンの設定については、[アクセストークン](/ja-JP/codex/enterprise/access-tokens) を参照してください。
ワークロード ID の設定については、
[ワークロード ID フェデレーション](/ja-JP/codex/enterprise/workload-identity) を参照してください。

## 診断

| 変数   | 使用箇所            | 説明                                                                                                             |
| ---------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| `RUST_LOG` | CLI と App Server | Rust ログのフィルタリングと詳細度を制御します。`codex exec` のログ出力は、より詳細な値を設定しない限り、デフォルトで `error` レベルです。 |

`RUST_LOG` には、`error`、`warn`、`info`、`debug`、
`trace` などの値を指定できます。また、
`codex_core=debug,codex_tui=debug` のように、対象をさらに絞り込んだ Rust ログフィルターも指定できます。

対話型 CLI はデフォルトで、容量制限のあるローカルストアに診断情報を記録しますが、
プレーンテキストの `codex-tui.log` ファイルへの記録はオプトインです。`log_dir` は、トラブルシューティングで
プレーンテキストログが必要な場合に明示的に設定します：

```bash
RUST_LOG=debug codex -c log_dir=./.codex-log
tail -F ./.codex-log/codex-tui.log

非対話モードでは、`codex exec` はメッセージをインラインで出力し、
別の TUI ログファイルには書き込みません。
