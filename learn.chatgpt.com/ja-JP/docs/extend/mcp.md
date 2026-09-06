<!-- source: https://learn.chatgpt.com/ja-JP/docs/extend/mcp -->

Model Context Protocol（MCP）は、モデルをツールやコンテキストに接続します。これにより、ChatGPT や Codex がサードパーティのドキュメントにアクセスしたり、ブラウザや Figma などの開発ツールを操作したりできるようになります。

ChatGPT Web では、プラグインが提供するリモートの MCP 対応ツールを利用できます。ローカルの Codex クライアントも MCP サーバーに直接接続し、構成を共有できます。

<a id="supported-mcp-features"></a>

ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能はいずれも MCP サーバーに対応しており、同じ Codex ホストの MCP 構成を共有します。

以下のサーバー機能は、Codex ホストに構成された MCP サーバーに適用されます。ホスト型のプラグインツールでは、利用できる機能が異なる場合があります。

## サポート対象の MCP 機能

- **STDIO サーバー**：ローカルプロセスとして実行されるサーバー（コマンドで起動）
  - 環境変数
- **Streamable HTTP サーバー**：アドレスを指定してアクセスするサーバー
  - Bearer トークン認証
  - Client ID Metadata Documents（CIMD）や Dynamic Client Registration（DCR）に対応した OAuth 認証
  - 信頼済みのファーストパーティサーバーに対する ChatGPT セッション認証
- **サーバーの指示**：Codex は初期化時に返される MCP の `instructions` フィールドを読み取り、サーバーのツールと併せて、サーバー全体に適用される指針として使用します。

Codex 向けの MCP サーバーを構築または保守する場合は、複数のツールを使うワークフローや、サーバー全体に適用される制約とレート制限を `instructions` に記述します。Codex がサーバーの利用方法を判断する際に最も重要な指針を参照できるよう、先頭の 512 文字だけで内容が完結するようにしてください。

## Codex と MCP サーバーの接続

Codex は MCP の構成を、ほかの Codex 設定とともに `config.toml` に保存します。デフォルトでは `~/.codex/config.toml` に保存されますが、`.codex/config.toml` を使用して MCP サーバーの適用範囲をプロジェクトに限定することもできます（信頼済みのプロジェクトのみ）。

この構成は、ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能で共有されます。MCP サーバーを一度構成すれば、セットアップをやり直すことなく、これらのクライアントを切り替えられます。

### ChatGPT デスクトップアプリでの構成

1. 「 **設定**」を開き、「 **MCP サーバー**」を選択します。
2. 「 **サーバーを追加**」を選択します。
3. 名前を入力して「 **STDIO** 」または「 **Streamable HTTP**」を選択し、
   サーバーのコマンドまたは URL を指定します。
4. サーバーを保存してから、「 **再起動**」を選択します。

サーバー一覧では、各サーバーが有効かどうか、OAuth が必要かどうかを確認できます。
OAuth サーバーへのサインインが必要な場合は、「**認証** 」を選択します。コンポーザーに `/mcp` と入力すると、
接続済みのサーバーを表示できます。

## ChatGPT Web での MCP 対応ツールの使用

ホスト型の ChatGPT Work チャットで[プラグイン](/ja-JP/codex/plugins)をインストールすると、
付属のコネクタとリモート MCP ツールを利用できます。インストール後は、
チャットと Work のどちらでもこれらのツールを利用できます。ワークスペース管理者は、
利用できるプラグインとツールを管理できます。

ChatGPT Web はローカルの Codex 構成ファイルを読み込まず、
ローカルの Codex コマンドメニューも表示しません。「 **プラグイン** 」タブを開くと、
利用可能なツールを確認・管理できます。

### CLI での構成

#### MCP サーバーの追加

```bash
codex mcp add <server-name> --env VAR1=VALUE1 --env VAR2=VALUE2 -- <stdio server-command>

たとえば、開発者向けドキュメント用の無料 MCP サーバーである Context7 を追加するには、次のコマンドを実行できます。

```bash
codex mcp add context7 -- npx -y @upstash/context7-mcp

#### その他の CLI コマンド

構成済みのサーバーを確認するには `codex mcp list` を実行します。
利用可能なすべての MCP コマンドを確認するには `codex mcp --help` を実行します。
OAuth に対応するサーバーの場合は `codex mcp login <server-name>` を実行します。

#### ターミナル UI（TUI）

`codex` の TUI で `/mcp` を使用すると、アクティブな MCP サーバーを確認できます。

### IDE 拡張機能での構成

1. 歯車メニューを開き、「 **MCP サーバー**」を選択します。
2. 「 **サーバーを追加**」を選択します。
3. 名前を入力して「 **STDIO** 」または「 **Streamable HTTP**」を選択し、
   サーバーのコマンドまたは URL を指定します。
4. サーバーを保存してから、「 **拡張機能を再起動**」を選択します。

MCP サーバー一覧では、各サーバーが有効かどうか、OAuth が必要かどうかを確認できます。
OAuth サーバーへのサインインが必要な場合は、「 **認証** 」を選択します。

### config.toml による構成

より細かく制御するには `~/.codex/config.toml` を編集するか、
プロジェクト単位の `.codex/config.toml` を編集します。[構成リファレンス](/ja-JP/codex/config-file/config-reference)には、
サポートされているすべての MCP オプションを検索できる一覧があります。

各 MCP サーバーは、構成ファイル内の `[mcp_servers.<server-name>]` テーブルで構成します。

<a id="stdio-servers"></a>

#### STDIO サーバー

- `command`（必須）：サーバーを起動するコマンド
- `args`（任意）：サーバーに渡す引数
- `env`（任意）：サーバーに設定する環境変数
- `env_vars`（任意）：許可して転送する環境変数
- `cwd`（任意）：サーバー起動時の作業ディレクトリ
- `experimental_environment`（任意）：`remote` に設定すると、リモート実行環境が利用可能な場合は、
  その環境を介して stdio サーバーを起動します。

`env_vars` には、変数名をそのまま指定するか、取得元を指定したオブジェクトを使用できます。

```toml
env_vars = ["LOCAL_TOKEN", { name = "REMOTE_TOKEN", source = "remote" }]

文字列で指定した項目と `source = "local"` を指定した項目では、Codex のローカル環境から値を読み取ります。
`source = "remote"` を指定すると、リモート実行環境から値を読み取ります。この場合は、
リモート MCP stdio が必要です。

<a id="streamable-http-servers"></a>

#### Streamable HTTP サーバー

- `url`（必須）：サーバーのアドレス
- `auth`（任意）：構成済みの Bearer トークンと認可ヘッダーの後に試す認証方式です。
  保存済みの MCP OAuth 認証情報を使用するには、`oauth`（デフォルト）を指定します。
  `chatgpt` を指定すると、信頼済みのファーストパーティ ChatGPT オリジンに対して現在の ChatGPT セッションを使用し、
  保存済みの OAuth をフォールバックとして使用します。
- `bearer_token_env_var`（任意）：`Authorization` で送信する Bearer トークンを格納した環境変数の名前
- `http_headers`（任意）：ヘッダー名を静的な値に対応付けるマップ
- `env_http_headers`（任意）：ヘッダー名を環境変数名に対応付けるマップ（値は環境から取得）
- `http_headers_helper`（任意）：ヘッダー名と文字列値からなる
  JSON オブジェクトを出力するローカルコマンドです。出力例は `{"X-Auth": "temporary-token"}` です。
  ローカル環境からの HTTP MCP 接続に対応していますが、
  stdio サーバーやリモート実行環境を介した接続には対応していません。

Codex は接続に使うヘルパーのヘッダーをキャッシュします。
同一オリジンへの POST が `401` または `403` を返すと、ヘッダーを一度更新し、
ヘルパーが前回と異なる値を返した場合にのみ再試行します。明示的に指定した Bearer トークンと OAuth 認証情報は、
ヘルパーが提供する `Authorization` ヘッダーより優先されます。
スコープの不足を示す OAuth の `403` レスポンスでは、
ヘルパーによる更新は行われません。

どの取得元からも認証情報を取得できない場合、Codex は認証なしでサーバーに接続できます。
`codex mcp login <server-name>` を別途実行して、
MCP の OAuth ログインを開始します。

#### その他の構成オプション

- `startup_timeout_sec`（任意）：サーバーの起動タイムアウト（秒）。デフォルト値：`10`
- `tool_timeout_sec`（任意）：サーバーによるツール実行時のタイムアウト（秒）。デフォルト値：`60`
- `enabled`（任意）：`false` に設定すると、サーバーを削除せずに無効化できます。
- `required`（任意）：`true` に設定すると、有効になっているこのサーバーを初期化できない場合に起動が失敗します。
- `enabled_tools`（任意）：ツールの許可リスト
- `disabled_tools`（任意）：ツールの拒否リスト（`enabled_tools` の適用後に適用）
- `default_tools_approval_mode`（任意）：このサーバーのツールに対する
  デフォルトの承認動作。使用できる値は `auto`、`prompt`、`writes`、
`approve` です。`writes` モードでは、読み取り専用としてマークされていないツールについて承認を求めます。
- `tools.<tool>.approval_mode`（任意）：ツールごとの承認動作の上書き
- `tools.<tool>.output_token_limit`（任意）：1 つのツールの出力に割り当てるトークン数の上限を正の値で指定します。
  標準で設けられるシリアライズ用の余裕分 20% を加算する前の値です。
  そのツールの出力を切り詰める際の、モデルのデフォルトの上限を上書きします。

トップレベルの `mcp_optional_startup_grace_ms` 設定は、Codex が初期ツールカタログを作成する際に、
必須ではない MCP サーバーの起動を待つ時間を制御します。
デフォルトは `1000` ミリ秒です。`0` に設定すると、代わりに各サーバーの
`startup_timeout_sec` に従って待機します。必須のサーバーには、
引き続きそれぞれの起動タイムアウトが適用されます。

#### OAuth クライアント登録とコールバック

認可サーバーで事前登録済みの OAuth クライアントが必要な場合は、MCP サーバーの追加時にそのクライアント ID を指定します：

```bash
codex mcp add example --url https://mcp.example.com --oauth-client-id my-client

Codex は、プロバイダーに登録する完全なコールバック URL を表示します：

```text
OAuth callback URL: http://127.0.0.1/callback

Codex は、以降のログイン用に、コールバックをクライアント ID とともに
`config.toml` に保存します：

```toml
[mcp_servers.example]
url = "https://mcp.example.com"

[mcp_servers.example.oauth]
client_id = "my-client"
callback_url = "http://127.0.0.1/callback"

新たに追加した事前登録済みクライアントが固定のコールバックを使用するのは、
認可サーバーが `authorization_response_iss_parameter_supported: true` を公開し、
メタデータで `issuer` を提供する場合に限られます。
発行者識別への対応が公開されていない場合は、Codex がサーバー固有のコールバック ID を付加します。
たとえば、`http://127.0.0.1/callback/XuuuHAzzHOni` のようになります。
コールバックを保存していない既存のクライアントは、引き続きコールバック ID 固有のリダイレクトを使用します。

ログイン時のコールバックは、OAuth の構成と認可サーバーのメタデータに応じて、次のように選択されます：

| OAuth 構成                                                | 発行者識別への対応           | 使用するコールバック                                                                                                                                      |
| ------------------------------------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `callback_url` を設定し、`client_id` は未設定                                 | 対応                | 設定済みのコールバックをクライアント登録に使用します。                                                                                           |
| `callback_url` を設定し、`client_id` は未設定                                 | 非対応              | 設定済みのコールバックにサーバー固有のコールバック ID を付加し、クライアント登録に使用します。                                             |
| `client_id` と `callback_url`                                     | 対応                | 設定済みのコールバックを再利用します。認可レスポンスには、一致する `iss` が含まれている必要があります。                                                     |
| `client_id` と、末尾に正しいコールバック ID を含む `callback_url` | 非対応              | 設定済みのコールバックを変更せずに再利用します。                                                                                                       |
| `client_id` と、正しいコールバック ID がない `callback_url`   | 非対応              | 設定済みのコールバックは無視されます。Codex は `mcp_oauth_callback_url` を使用し、未設定の場合は `http://127.0.0.1/callback` を使用します。いずれの場合もコールバック ID を付加します。 |
| `client_id` を設定し、`callback_url` は未設定                    | 対応・非対応のいずれも | Codex は、グローバル設定のコールバックまたはデフォルトのコールバックに、サーバー固有のコールバック ID を付加して使用します。                                                           |

このフォールバックによって、保存済みのコールバック URL が変更されることはありません。Codex は、パスとクエリ文字列を含む MCP サーバーの URL からコールバック ID を導出します。自動ログインと明示的なログインには、同じ選択ルールが適用されます。

カスタムのコールバックパスやリモート Devbox のイングレス URL が必要な場合は、`mcp_oauth_callback_url` を設定します。
新たに追加した事前登録済みクライアントは、プロバイダーが発行者識別に対応している場合、
その URL を変更せずに使用します。対応していない場合は、
設定済みの URL にサーバー固有のコールバック ID を付加して使用します。
必ず `codex mcp add` に表示されたコールバックをそのまま登録してください。

ポートを指定しない `http://127.0.0.1` のコールバックでは、
Codex は表示・保存する URL からリスナーポートを省略し、
認可時に使用中のリスナーポートを挿入します。この置換は、`localhost`、IPv6 ホスト、
HTTPS URL、またはポートがすでに含まれているコールバックには適用されません。
認可サーバーは、[RFC 8252 の第 7.3 節](https://www.rfc-editor.org/rfc/rfc8252#section-7.3)に従い、
ループバックのポート番号が変わっても受け入れる必要があります。

グローバルで固定のリスナーポートを使うには、`mcp_oauth_callback_port` を設定します。
特定のサーバーだけでこの設定を上書きするには、`mcp_servers.<server-name>.oauth.callback_port` を設定します。
コールバック URL にポートを明示しても、リスナーの設定には反映されません。
ループバックで直接コールバックする場合は、ポートなしの `http://127.0.0.1` を使用するか、
コールバック URL とリスナーの両方に同じポートを明示的に設定してください。
プロキシ経由のコールバックでは、外部 URL のポートをローカルのリスナーポートと意図的に異なる値にすることができます。
ローカルのコールバック URL はローカルインターフェースにバインドされ、
ローカル以外のコールバック URL は `0.0.0.0` にバインドされます。

Codex は、認可コードを交換する前に、返された `iss` を検証します。
`iss` が一致しない場合、レスポンスは必ず拒否されます。発行者識別への対応が公開されている場合は、
`iss` が欠落していても拒否されます。どちらの場合も、認可コードの交換や
別のコールバックへのフォールバックは行いません。コールバック URL の形式が不正な場合や、
発行者識別への対応を公開しながらメタデータに発行者がない場合も、処理を続行できないエラーになります。
[ユーザーの認証](/plugins/build/auth)をご覧ください。

MCP サーバーが `scopes_supported` を公開している場合、
Codex は OAuth ログイン時に、そのサーバーが公開するスコープを優先します。
それ以外の場合は、`config.toml` に設定されたスコープにフォールバックします。

#### OAuth クライアント登録

Codex は [OAuth クライアント ID メタデータドキュメント（CIMD）](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)と
動的クライアント登録（DCR）に対応しています。デフォルトでは、
認可サーバーが `client_id_metadata_document_supported: true` を公開し、
`token_endpoint_auth_methods_supported` に `none` が含まれ、
コールバックに対応済みのループバック URL が使用される場合に、
Codex は CIMD を自動的に選択します。それ以外の場合は、DCR が利用可能であれば使用します。
設定済みの OAuth クライアント ID が常に優先され、その場合はクライアント登録を省略します。

CIMD では、Codex は ChatGPT がホストする MCP サーバー固有のメタデータドキュメントを使用します：

```text
https://chatgpt.com/oauth/codex/<callback_id>/client.json

Codex は MCP サーバーの URL から `<callback_id>` を導出し、
ループバックリダイレクト URI に含めます。たとえば、
`http://127.0.0.1:<port>/callback/<callback_id>` のような URI です。メタデータドキュメントには、
対応するループバック URI がポートなしで登録されます。認可サーバーは、
ホストとパスを完全に一致させたうえで、ログイン時に選択されたポートを受け入れる必要があります。これは、
[RFC 8252](https://www.rfc-editor.org/rfc/rfc8252.html#section-7.3) で定められた要件です。
カスタムのコールバックホスト、パス、クエリパラメーターを使用する場合は、
DCR または設定済みの OAuth クライアント ID が必要です。

固定の共有 CIMD ドキュメントへの対応は現在開発中で、近日中に提供予定です：

```text
https://chatgpt.com/oauth/codex/client.json

認可サーバーが `authorization_response_iss_parameter_supported: true` を公開し、
メタデータで有効な `issuer` を提供し、
認可レスポンスに一致する `iss` を含める場合、
Codex は今後、共有の `/callback` パスを持つ固定のドキュメントを使用するようになります。
発行者に紐付いたレスポンスを返さないサーバーでは、
引き続きコールバック固有のドキュメントを使用します。

1 回の CLI ログインで登録方法を指定するには、
`--oauth-client-registration` を使用します：

```bash
codex mcp login <server-name> --oauth-client-registration cimd
codex mcp login <server-name> --oauth-client-registration dcr

デフォルトは `auto` です。選択した登録方法は現在のログインにのみ適用され、
`config.toml` には保存されません。

#### config.toml の例

```toml
[mcp_servers.context7]
command = "npx"
args = ["-y", "@upstash/context7-mcp"]
env_vars = ["LOCAL_TOKEN"]

[mcp_servers.context7.env]
MY_ENV_VAR = "MY_ENV_VALUE"

```toml
# Optional MCP OAuth callback overrides (used by `codex mcp login`)
mcp_oauth_callback_port = 5555
mcp_oauth_callback_url = "https://devbox.example.internal/callback"

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }

```toml
[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
enabled_tools = ["open", "screenshot"]
disabled_tools = ["screenshot"] # applied after enabled_tools
default_tools_approval_mode = "prompt"
startup_timeout_sec = 20
tool_timeout_sec = 45
enabled = true

[mcp_servers.chrome_devtools.tools.open]
approval_mode = "approve"
output_token_limit = 30000

### プラグインが提供する MCP サーバー

インストール済みのプラグインは、プラグインマニフェストに MCP サーバーを同梱できます。
これらのサーバーはプラグインから起動されるため、
ユーザー設定ではトランスポートコマンドを設定しません。ただし、有効・無効の状態とツールポリシーは、
ユーザー設定の `plugins.<plugin>.mcp_servers.<server>` で引き続き制御できます。

```toml
[plugins."sample@test".mcp_servers.sample]
enabled = true
default_tools_approval_mode = "prompt"
enabled_tools = ["read", "search"]

[plugins."sample@test".mcp_servers.sample.tools.search]
approval_mode = "approve"

プラグインが提供する HTTP MCP サーバーは、`.mcp.json` で OAuth 設定を宣言することもできます。
プラグインマニフェストでは、camelCase 形式のフィールド名 `clientId`、`callbackUrl`、
`callbackPort` を使用します：

```json
{
  "mcpServers": {
    "sample": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "clientId": "my-pre-registered-client",
        "callbackUrl": "http://127.0.0.1/callback/registered"
      }
    }
  }
}

プラグインが提供する MCP サーバーにも、他の MCP サーバーと同じコールバック選択ルールが適用されます。
プラグインが `clientId` を提供し、そのプロバイダーが発行者に紐付いたコールバックに対応しておらず、
さらに `callbackUrl` にサーバー固有のコールバック ID が含まれていない場合、
Codex はそのログインではこの URL を無視します。代わりに `mcp_oauth_callback_url` を、
未設定の場合は `http://127.0.0.1/callback` を使用し、いずれの場合もコールバック ID を付加します。
設定済みの `callbackUrl` は変更されません。

プラグインの `oauth.callbackPort` は、グローバル設定の `mcp_oauth_callback_port` を上書きします。
どちらも未設定の場合、Codex はエフェメラルポートを選択します。
`callbackUrl` に含まれるポートは、リスナーポートの選択には使われません。
固定ポートを使ってループバックで直接コールバックする場合は、両方の値を一致させてください：

```json
{
  "callbackUrl": "http://127.0.0.1:4321/callback/registered",
  "callbackPort": 4321
}

リモートイングレスやその他のプロキシを使用する場合、プロキシが設定済みのリスナーに転送するのであれば、コールバック URL のポートとローカルのリスナーポートを意図的に異なる値にすることができます。

## 便利な MCP サーバーの例

MCP サーバーの種類は増え続けています。代表的なものをいくつか紹介します：

- [OpenAI ドキュメント MCP](/learn/docs-mcp)：OpenAI の開発者向けドキュメントを検索して閲覧します。
- [Context7](https://github.com/upstash/context7)：最新の開発者向けドキュメントに接続します。
- Figma の[ローカル](https://developers.figma.com/docs/figma-mcp-server/local-server-installation/)と[リモート](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)：Figma のデザインにアクセスします。
- [Playwright](https://www.npmjs.com/package/@playwright/mcp)：Playwright を使用してブラウザを操作し、検査します。
- [Chrome デベロッパーツール](https://github.com/ChromeDevTools/chrome-devtools-mcp/)：Chrome を操作し、検査します。
- [Sentry](https://docs.sentry.io/product/sentry-mcp/#codex)：Sentry のログにアクセスします。
- [GitHub](https://github.com/github/github-mcp-server)：`git` が対応していない操作（Pull Request やイシューの管理など）も含めて、GitHub を管理します。
