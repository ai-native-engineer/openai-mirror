<!-- source: https://learn.chatgpt.com/ja-JP/docs/permissions -->

ベータ版です。権限プロファイルは現在も開発中のため、変更される可能性があります。

  権限プロファイルは従来のサンドボックス設定と併用できません。
  `default_permissions` と `[permissions]`、または `sandbox_mode` /
`sandbox_workspace_write` のいずれか一方を構成し、両方を同時に設定しないでください。読み込まれた設定ファイルのいずれかに `sandbox_mode` が含まれている場合、
  `--sandbox` を指定した場合、または選択した設定プロファイルで
`sandbox_mode` が設定されている場合、Codex は
`default_permissions` ではなく従来のサンドボックス設定を使用します。

管理対象の `allowed_permission_profiles` は例外であり、Codex に権限プロファイルを使用させます。
管理対象のプロファイル許可リストをデプロイする前に、
`sandbox_mode` や `[sandbox_workspace_write]` などの従来の設定を削除してください。
複数のバージョンが混在するエンタープライズ展開では、
管理対象の `allowed_sandbox_modes` 要件を、
すべてのクライアントで Codex 0.138.0 以降が実行されるまで、一時的な互換性制約として維持できます。

権限プロファイルを使用すると、Codex がユーザーに代わって実行するローカルコマンドに、最小権限に基づく制限を適用できます。プロファイルは、コマンドが読み書きできる対象を定めるファイルシステムルールと、コマンドが到達できる宛先を定めるネットワークルールを組み合わせた名前付きポリシーです。

  プロファイルの `network.enabled = true` はコマンドのネットワークアクセスを許可しますが、
  ネットワークプロキシは起動しません。プロファイルのドメインルールを適用するには、
`features.network_proxy = true` も `config.toml` に設定するか、
  管理者が管理し、有効化した `[experimental_network]` 要件を使用してください。
  プロキシが稼働していない場合、プロファイルのドメインルールによって直接のネットワークアクセスは制限されません。

プロファイルを使用して、マシンやネットワークへの広範なアクセスを許可することなく、現在のチャットに必要なアクセス権を Codex に付与してください。たとえば、読み取り専用プロファイルでは Codex がプロジェクトを編集せずに調査でき、書き込み可能なプロファイルでは編集対象を選択したワークスペースルートに限定できます。

ローカル権限プロファイルは、macOS、Linux、WSL、
ネイティブ Windows に対応しています。[適用範囲と強制](#scope-and-enforcement) を参照し、
プラットフォーム固有の詳細と注意事項を確認してください。

Codex Cloud のネットワーク設定については、[インターネットアクセス](/ja-JP/codex/cloud/internet-access) を参照してください。

## プロファイルの定義と選択

Codex には、次の 3 つの組み込み権限プロファイルがあります。

- `:read-only` は、ローカルコマンドの実行を読み取り専用に制限します。
- `:workspace` は、アクティブなワークスペースルートとシステムの一時ディレクトリ内への書き込みを許可します。
- `:danger-full-access` はローカルのサンドボックス制限を解除します。
  広範なアクセスを意図的に許可する場合にのみ使用してください。

`[permissions.<name>]` の下に名前付きプロファイルを作成してから、
最上位の `default_permissions` キーを、そのプロファイル名または上記の組み込みプロファイルのいずれかに設定します。
この例の `project-edit` はユーザー定義のプロファイル名であり、
組み込みの値ではありません。

エンタープライズ管理者はプロファイルを定義し、
管理対象の `requirements.toml` を通じて、ユーザーが選択できるプロファイルを制限できます。
`allowed_permission_profiles` が設定されている場合、リストに含まれていないプロファイルは拒否されます。
対象には、リストに含まれていない組み込みプロファイルや、将来の Codex バージョンで追加されるプロファイルも含まれます。
[利用可能な権限プロファイルの制御](/ja-JP/codex/enterprise/managed-configuration#control-available-permission-profiles) を参照し、
推奨される管理対象の設定を確認してください。

カスタムプロファイルでは、互いに関連する 2 つの概念を使用します。

- `[permissions.<name>.workspace_roots]` は、
  そのプロファイルのワークスペースルートとして扱う具体的なディレクトリを追加します。
- `[permissions.<name>.filesystem.":workspace_roots"]` は、
  有効な各ワークスペースルート内で Codex が適用するファイルシステムルールを定義します。
  対象には、現在のセッションの実行時ワークスペースルートと、前述のプロファイル定義ルートが含まれます。

プロファイルにも通常の設定レイヤーモデルが適用されます。優先順位が高いレイヤーでは、プロファイル全体を再記述しなくても、同じ名前のプロファイルに項目を追加したり、既存の項目を置き換えたりできます。

たとえば、組織レベルの設定とユーザーレベルの設定で、同じプロファイルをそれぞれ独立して拡張できます。

```toml
# /etc/codex/config.toml
[permissions.server.workspace_roots]
"~/code/server" = true

```toml
# ~/.codex/config.toml
[permissions.server.workspace_roots]
"~/code/mobile-app" = true

`server` が有効な場合、
両方のワークスペースルートが実際に適用されるプロファイルに含まれます。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"
"objects.githubusercontent.com" = "allow"
"*.github.com" = "allow"
"tracking.example.com" = "deny"

このプロファイルの動作は次のとおりです。

- 一般的な開発ツールに必要な最小限の実行時パスの読み取りを許可
- 現在のセッションとプロファイルで定義したルートに、同じワークスペースルートルールを適用
- 各ルートにある `.devcontainer/` などの IDE 関連設定について、
  読み取り専用の状態を維持
- glob ルールに一致する環境ファイルへのアクセスを拒否
- 設定されたドメインポリシーを通じたネットワークアクセスのみを許可

アクティブなプロファイルでは、広い範囲のパスへの読み取りや書き込みが許可されていても、
対象範囲の狭い拒否ルールは引き続き有効です。たとえば、
ワークスペースルートへの書き込みを許可しながら、一致する `.env` パスを `deny` に設定できます。

## プロファイルの拡張

組み込みプロファイルや別の名前付きプロファイルと大部分が同じ場合は、`extends` を使用します。
基本的な保護を引き継ぐため、ゼロから作成するのではなく、組み込みプロファイルを拡張してください。
たとえば `:workspace` を拡張すると、
ワークスペースルートの `.codex` ディレクトリは、明示的に上書きしない限り読み取り専用のままです。
親プロファイルを一度設定したら、
異なるルールだけを追加または上書きしてください。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
description = "Project editing with OpenAI API access."
extends = ":workspace"

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

このプロファイルは `:workspace` を基にし、一致する `.env` ファイルへのアクセスを拒否したまま、
`api.openai.com` へのリクエストを許可します。拡張元として指定できるのは `:read-only`、
`:workspace`、または別の名前付きプロファイルです。
`:danger-full-access` は拡張できません。Codex は、
不明な親プロファイルや継承サイクルも拒否します。

## 構成仕様

| 項目                                                             | 型 / 値              | デフォルト                 | 詳細                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `default_permissions`                                             | プロファイル名（文字列）        | なし                    | Codex がデフォルトで適用する権限プロファイルの名前を指定します。`[permissions]` 配下のプロファイル、または `:workspace` などの組み込みプロファイルと一致する必要があります。動作を予測しやすくするため、明示的に設定してください。管理対象の要件でこの設定を省略できるのは、`:workspace` と `:read-only` の両方が明示的に許可されている場合に限ります。この構成では、管理対象の `allowed_permission_profiles` で権限プロファイルの使用が指示されない限り、Codex は従来のサンドボックス設定を使用します。 |
| `[permissions.<name>]`                                            | テーブル                      | なし                    | 名前付きプロファイルを定義します。`default_permissions` で 1 つのプロファイルをデフォルトとして選択し、ほかの権限プロファイル設定でもそのプロファイル名を使用します。                                                                                                                                                                                                                                                                               |
| `permissions.<name>.description`                                  | 文字列                     | なし                    | プロファイルに、人が読んで理解できる説明を指定します。`extends` を使用しても、親プロファイルの説明は継承されません。                                                                                                                                                                                                                                                                                                 |
| `permissions.<name>.extends`                                      | プロファイル名（文字列）        | なし                    | 別の名前付きプロファイル、または組み込みの `:read-only` か `:workspace` プロファイルを基に、このプロファイルを作成します。Codex は、`:danger-full-access`、不明な親プロファイル、継承サイクルを拒否します。                                                                                                                                                                                                                                            |
| `[permissions.<name>.workspace_roots]`                            | テーブル                      | なし                    | プロファイルで定義したワークスペースルートを追加します。追加したルートには、現在のセッションの実行時ワークスペースルートと同様に `:workspace_roots` ファイルシステムルールが適用されます。                                                                                                                                                                                                                                                                                |
| `permissions.<name>.workspace_roots."<path>"`                     | 真偽値                    | `false`                 | `true` の場合、対象のパスをプロファイルのワークスペースルートの集合に追加します。`false` に設定した項目は無効のままです。                                                                                                                                                                                                                                                                                                                        |
| `[permissions.<name>.filesystem]`                                 | テーブル                      | なし                    | ファイルシステムパスをアクセス値、またはスコープ付きのサブパスマップに対応付けます。ファイルシステムテーブルが存在しない場合や空の場合は、ファイルシステムへのアクセスが制限されたままとなり、起動時に警告が出力されます。                                                                                                                                                                                                                                                               |
| `permissions.<name>.filesystem.glob_scan_max_depth`               | 数値                     | なし                    | Codex がサンドボックスの起動前に一致結果のスナップショットを取得する際、Linux、WSL、ネイティブ Windows での読み取り拒否用 glob の展開を制限します。値を大きくすると、起動時のスキャン処理が増える可能性があります。`1` 以上の値は、上限のない `**` パターンを範囲を限定して事前展開する必要がある場合に指定してください。                                                                                                                                                              |
| `[permissions.<name>.filesystem]."<path>"`                        | `read`、`write`、または `deny` | なし                    | サポート対象のパスへの直接アクセスを許可します。`deny` はアクセスを拒否し、具体性が同じ `write` または `read` の項目より優先されます。Codex は、アクティブなランタイムでは強制できない直接書き込みルールを拒否します。                                                                                                                                                                                                                            |
| `[permissions.<name>.filesystem."<path>"]."<subpath>"`            | `read`、`write`、または `deny` | なし                    | `<path>` の子孫パスへのアクセスを許可します。ベースパスには `.` を使用します。その他のサブパスは、ベースパス配下を指す相対パスである必要があり、`.` または `..` のコンポーネントを含めることはできません。                                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network]`                                    | テーブル                      | なし                    | コマンドのネットワークアクセスと、有効なネットワークプロキシが適用するポリシーを設定します。管理者が管理するネットワーク要件によってプロキシが起動する場合を除き、`features.network_proxy` を有効にしてください。                                                                                                                                                                                                                                    |
| `permissions.<name>.network.enabled`                              | ブール値                    | `false`                 | プロファイル内のコマンドによるネットワークアクセスを有効にします。ネットワークプロキシは起動されないため、有効なプロキシがない場合、コマンドはドメインの制限を受けずに直接接続できます。                                                                                                                                                                                                                                                  |
| `[permissions.<name>.network.domains]`                            | テーブル                      | なし                    | ホストパターンを `allow` または `deny` にマッピングします。ルールはネットワークプロキシが有効な場合にのみ適用されます。`allow` のエントリがない場合、有効なプロキシはドメインへのリクエストをブロックし、拒否エントリは許可エントリより優先されます。                                                                                                                                                                                                                 |
| `permissions.<name>.network.domains."<pattern>"`                  | `allow` または `deny`          | なし                    | 完全一致するホスト、サブドメイン用の `*.example.com`、apex ドメインとサブドメイン用の `**.example.com`、および許可専用のグローバルワイルドカードである `*` に対応しています。ホストパターンは、前後の空白の除去、小文字への変換、末尾のドットの除去、および単純なポート指定や角括弧の除去によって正規化されます。                                                                                                                                                           |
| `[permissions.<name>.network.unix_sockets]`                       | テーブル                      | なし                    | Unix ソケットの許可リストを上書きする設定を定義します。Docker などのローカル連携にのみ使用してください。                                                                                                                                                                                                                                                                                                                                         |
| `permissions.<name>.network.unix_sockets."<path>"`                | `allow` または `deny`          | なし                    | Unix ソケットの絶対パスを、`allow` の場合は実効許可リストに追加し、`deny` の場合は拒否します。拒否されたエントリは実効許可リストから除外されます。                                                                                                                                                                                                                                                                |
| `permissions.<name>.network.proxy_url`                            | URL 文字列                 | `http://127.0.0.1:3128` | `HTTP_PROXY`、`HTTPS_PROXY`、WebSocket プロキシ変数、および関連ツールのプロキシ環境変数に使用する HTTP プロキシリスナーです。                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.enable_socks5`                        | ブール値                    | `true`                  | `ALL_PROXY` と FTP プロキシ変数に使用する SOCKS5 リスナーを有効にします。                                                                                                                                                                                                                                                                                                                                                     |
| `permissions.<name>.network.socks_url`                            | URL 文字列                 | `http://127.0.0.1:8081` | SOCKS5 リスナーのアドレスです。                                                                                                                                                                                                                                                                                                                                                                                                      |
| `permissions.<name>.network.enable_socks5_udp`                    | ブール値                    | `true`                  | SOCKS5 リスナーが有効な場合に、SOCKS5 の UDP サポートを有効にします。                                                                                                                                                                                                                                                                                                                                                               |
| `permissions.<name>.network.allow_upstream_proxy`                 | ブール値                    | `true`                  | 送信リクエストで、ネットワークサンドボックスプロキシがアップストリームの `HTTP(S)_PROXY` および `ALL_PROXY` の設定に従うようにします。                                                                                                                                                                                                                                                                                                          |
| `permissions.<name>.network.allow_local_binding`                  | ブール値                    | `false`                 | `true` の場合、ローカルネットワークとプライベートネットワークへのアクセスを制限する保護機能を無効にします。`false` の場合は、`localhost` や `127.0.0.1` などのローカルリテラルを完全一致で明示的に許可リストに登録する必要があり、ローカル IP またはプライベート IP に解決されるホスト名は引き続きブロックされます。                                                                                                                                                                                                |
| `permissions.<name>.network.dangerously_allow_non_loopback_proxy` | ブール値                    | `false`                 | プロキシリスナーがループバック以外のアドレスにバインドできるようにします。通常のローカル開発では、未設定のままにしてください。                                                                                                                                                                                                                                                                                                                            |
| `permissions.<name>.network.dangerously_allow_all_unix_sockets`   | ブール値                    | `false`                 | Unix ソケットプロキシがサポートされている環境では、Unix ソケットの許可リストをバイパスします。これは、ローカルの制限を広範に回避できる例外機能です。                                                                                                                                                                                                                                                                                                               |

## ファイルシステムの権限

ファイルシステムのエントリには、`read`、`write`、`deny` のいずれかを使用します：

| アクセス  | 意味                                                                                                                           |
| ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `read`  | コマンドがパス配下のファイルを読み取り、ディレクトリの内容を一覧表示することを許可します。そのパス内では、コマンドはファイルを作成、変更、名前変更、削除できません。 |
| `write` | コマンドがパス配下のファイルを読み取り、変更することを許可します。OS で許可されている場合は、ファイルの作成、名前変更、削除も行えます。  |
| `deny`  | パス配下での読み取りと書き込みをどちらも拒否します。より広範な `read` または `write` の許可範囲から、アクセスを拒否するサブパスを切り出すために使用します。         |

より具体的なエントリは、より広範なエントリより優先されます。
2 つのエントリが同じパスを対象とする場合、`deny` は `write` より優先され、`write` は
`read` より優先されます。

この優先順位により、プロファイルではまず広い作業領域を指定し、その後、
読み取り不可のままにするファイルやディレクトリを除外できます：

```toml
[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"
".devcontainer" = "read"
"**/*.env" = "deny"

この例では、ワークスペースルートは書き込み可能なままで、`.devcontainer/` は読み取り専用です。
一致する環境ファイルは、
サンドボックス内のコマンドから引き続きアクセスできません。

より具体的なパスを指定すると、広範な拒否範囲内にある、より狭いサブツリーへのアクセスを再び許可することもできます：

```toml
[permissions.project-edit.filesystem]
"~/Documents" = "deny"
"~/Documents/codex" = "write"

サポートされるパス形式：

| パス               | 意味                                                                                     | スコープ付きサブパス |
| ------------------ | ------------------------------------------------------------------------------------------- | --------------- |
| `:root`            | ファイルシステムのルート                                                                         | `.` のみ        |
| `:minimal`         | 一般的なツールで必要となるプラットフォームおよびランタイムのパス                                           | `.` のみ        |
| `:workspace_roots` | 現在のセッションのワークスペースルートと、プロファイルで定義され有効になっているすべてのワークスペースルート      | はい             |
| `:tmpdir`          | 利用可能な場合の `$TMPDIR` の場所                                               | `.` のみ        |
| `:slash_tmp`       | 存在する場合の `/tmp` フォルダー                                                             | `.` のみ        |
| `/absolute/path`   | macOS/Linux/WSL の `/path` やネイティブ Windows の `C:\path` など、各プラットフォームの絶対パス | はい             |
| `~/path`           | 現在のユーザーのホームディレクトリ配下のパス                                              | はい             |

ネイティブ Windows では、ホームディレクトリからの相対パスにも、
`~\work` のようにバックスラッシュを使用できます。

プロファイルに広範な読み取り権限を意図的に付与する必要がある場合にのみ、`:root` を使用します：

```toml
[permissions.audit.filesystem]
":root" = "read"

`:workspace_roots` 配下のネストされたエントリを使用して、
アクセス範囲をワークスペースルートからの相対サブパスに限定します：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"          # each workspace root
"docs" = "read"        # each workspace-root docs directory
"generated" = "deny"   # each workspace-root generated directory

ネストされたサブパスは、対応するワークスペースルート内に収まる必要があります。
`../other-repo` のように親ディレクトリへ移動するパスは拒否されます。

### 完全一致パスまたは glob パターンによる読み取り拒否

Codex に読み取らせたくないファイルやサブツリーには `deny` を使用します。
周辺領域へのアクセスが、より広範なプロファイルルールで許可されている場合でも、読み取りを拒否できます。
`~/.ssh` のように場所が固定されている場合は、完全一致パスが適しています。
リポジトリごとに正確な場所が異なる機密ファイル群を対象にする場合は、glob パターンが適しています。

glob パターンが `:workspace_roots` 配下にある場合、Codex はこれを、
有効な各ワークスペースルートからの相対パスとして解釈します。例：

```toml
[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

このルールは、各ランタイムワークスペースルートまたはプロファイル定義のワークスペースルート配下にある、条件に一致する `.env` ファイルの読み取りを拒否します。
ワークスペースへの通常の書き込みを維持しながら、
環境ファイルや生成されたシークレット、
その他の認証情報を含む類似ファイルを読み取り不可にしたい場合に使用します。

`deny` の glob パターンは、読み取り拒否ルールとしてサポートされています。`read` または `write` の glob パターンは、
Linux、WSL、ネイティブ Windows のサンドボックスでは移植性が低いため、
可能な限り、完全一致パスか `"docs/**" = "read"` のようなサブツリールールを使用してください。

Linux、WSL、ネイティブ Windows では、深さに上限のない `**` 読み取り拒否パターンについて、
サンドボックスの起動前に深さを制限した事前展開が必要になる場合があります。`glob_scan_max_depth` は、
`"**/*.env" = "deny"` のように深さに上限のないパターンを使用するときに設定します：

```toml
[permissions.project-edit.filesystem]
glob_scan_max_depth = 3

[permissions.project-edit.filesystem.":workspace_roots"]
"**/*.env" = "deny"

`glob_scan_max_depth` は `1` 以上に設定する必要があります。値を大きくすると、
サンドボックスの起動前により深い階層までスキャンされるため、Linux、WSL、ネイティブ Windows では起動時の処理が増える場合があります。
深さを制限した展開を使用しない場合は、
`*.env`、`*/*.env`、`*/*/*.env` のように階層の深さを明示したパターンを列挙してください。

同じルールを現在のセッションルート以外にも適用する場合は、再利用可能なワークスペースルートをプロファイルに追加します：

```toml
[permissions.project-edit.workspace_roots]
"~/code/app" = true
"~/code/shared-lib" = true

このプロファイルが有効な場合、Codex は `:workspace_roots` のルールを、
現在のセッションのランタイムワークスペースルートと、
プロファイルで定義されている有効な各ワークスペースルートに適用します。

ネイティブ Windows では、`D:\work` のようなドライブ文字付きパスと、
`\\server\share` のような UNC パスを絶対パスとして使用できます。

## ネットワーク権限

ネットワークアクセスとネットワークフィルタリングは別々の設定です。
コマンドによるネットワークアクセスを許可するには `permissions.<name>.network.enabled = true` を設定し、
プロファイルのドメインルールを強制適用するには `features.network_proxy` を有効にします：

```toml
[features]
network_proxy = true

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"example.com" = "allow"      # exact host
"*.example.com" = "allow"    # subdomains only
"**.example.com" = "allow"   # apex and subdomains
"ads.example.com" = "deny"   # deny wins over allow

動作は、両方の設定の組み合わせによって決まります：

- ネットワークがオフの場合：プロキシ機能の設定にかかわらず、コマンドはネットワークにアクセスできません。
- ネットワークがオン、プロキシがオフの場合：コマンドはネットワークに直接、制限なくアクセスできます。権限プロファイルのドメインルールは強制適用されません。
- ネットワークがオン、プロキシがオンの場合：コマンドはプロキシを使用し、プロファイルのドメインルールが強制適用されます。有効なプロキシに許可済みドメインが設定されていない場合は、外部の接続先がブロックされます。

`[permissions.<name>.network.domains]` を追加したり、
`permissions.<name>.network.enabled = true` を設定したりしても、
`features.network_proxy` は有効になりません。管理者は別の方法として、
`[experimental_network]` を `requirements.toml` に記述することで、プロキシを有効にすることもできます。詳しくは、
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration#configure-network-access-requirements)を参照してください。

有効な場合、ネットワークサンドボックスプロキシはデフォルトでローカルリスナーにバインドされます：

```toml
[permissions.project-edit.network]
enabled = true
proxy_url = "http://127.0.0.1:3128"
enable_socks5 = true
socks_url = "http://127.0.0.1:8081"
enable_socks5_udp = true

特定のランタイムと連携する場合を除き、
これらのリスナー設定はデフォルトのままにしてください。`dangerously_*` ネットワークキーは、
特殊な環境向けに制限を回避するための設定であり、通常のローカル開発には使用しないでください。

### ローカルネットワークとプライベートネットワーク

ネットワークプロキシが有効な場合、Codex は DNS リバインディングやローカルサービスへの意図しないアクセスを防ぐため、デフォルトでローカルネットワークとプライベートネットワークへのアクセスを制限します。リテラルで指定したローカルの接続先を意図的に許可するには、該当するホスト名または IP アドレスのリテラルを完全一致で許可リストに追加します：

```toml
[permissions.project-edit.network.domains]
"localhost" = "allow"
"127.0.0.1" = "allow"

`allow_local_binding = true` を設定するのは、
許可リストに登録され、ローカルアドレスまたはプライベートアドレスに解決されるホスト名へのアクセスがプロファイルに必要な場合だけです：

```toml
[permissions.project-edit.network]
enabled = true
allow_local_binding = true

[permissions.project-edit.network.domains]
"localhost" = "allow"

### Unix ソケット

Unix ソケットのプロキシ機能は、Docker などのツールでローカルの制限を回避するための手段です。使用は必要最小限に抑えてください：

```toml
[permissions.project-edit.network.unix_sockets]
"/var/run/docker.sock" = "allow"
"/tmp/old.sock" = "deny"

継承された許可エントリを含め、ソケットパスを拒否するには `deny` を使用します。
拒否されたソケットパスは、実際に適用される許可リストから除外されます。

Unix ソケットを有効にする場合は、プロキシリスナーをループバックアドレスにバインドしたままにしてください。

## 従来のサンドボックス設定からの移行

ファイルシステムとネットワークの両方の動作を再利用可能な 1 つのプロファイルで定義したい場合、権限プロファイルは従来の `sandbox_mode` と
`sandbox_workspace_write` を組み合わせる方式に代わるものです。
1 つのセッションでは、どちらか一方の方式のみを使用し、
両方を併用しないでください。

推奨する初期構成：

- 読み取り専用のワークフローでは、組み込みの `:read-only` プロファイルを使用するか、
  必要な場所にのみ読み取りアクセスを許可するカスタムプロファイルを定義します。
- ワークスペースを編集する場合は、組み込みの `:workspace` プロファイルを使用するか、
  `:workspace_roots` 経由で書き込みを許可し、
  ワークフローに必要な追加の一時パスまたはキャッシュパスだけを追加するカスタムプロファイルを定義します。
- 制限なしでローカル実行するために `:danger-full-access` を使用するのは、
  最も広範なローカルアクセスモデルを意図的に採用する場合に限ってください。

プロファイルは、セッションにおけるローカルアクセスのデフォルトの方針を定義します。
組織が管理する要件により、ユーザー設定で緩和してはならない制限が追加されることがあります。
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)を参照し、
管理者が強制適用するファイルシステムとネットワークの制限を確認してください。

## 適用範囲と強制適用

権限プロファイルは、ローカルのサンドボックス内で実行されるコマンドのアクセス境界を定義します。承認ポリシーに加え、ウェブ検索、コネクタ、MCP サーバー、組み込みブラウザ、コンピューターの使用、Codex Cloud に対する個別の制御と組み合わせて使用してください。

### プロファイルの制御対象

- **ローカルコマンドの実行：** 権限プロファイルは、使用中のマシンで実行されるサンドボックス内のコマンドを制御します。
  コネクタ、MCP サーバー、ブラウザまたはコンピューターの使用機能、
  Codex Cloud の環境設定、承認済みの権限昇格には、
  それぞれ独自の制御が適用されます。
- **ファイルシステムへの書き込み：** 書き込み可能なプロファイルでは、永続的な変更を加えられます。
  スクリプト、ビルド手順、パッケージマネージャーのフック、
  シェルの起動ファイル、共有ディレクトリへの書き込みは慎重に扱ってください。
  別のツールやユーザーが後から、元のサンドボックス環境の外でこれらのファイルを実行できるためです。
- **外部への接続先：** ネットワークのドメインルールは、ネットワークプロキシが有効な間に限り、
  サンドボックス内のコマンドが通信できる接続先を制限します。
  許可された接続先が信頼できるかどうかを判断するものではなく、
  ワイルドカードによる許可ルールの適用範囲は広いままです。
- **ローカルサービス：** ネットワークプロキシが有効な場合、ローカルネットワークとプライベートネットワークの接続先はデフォルトでブロックされます。
  `localhost`、プライベート IP アドレス、Unix ソケットを許可リストに追加するか、
`allow_local_binding = true` を設定すると、ローカルサービスへのアクセスが明示的に許可されます。

### ネットワークプロキシの制御対象外

ネットワークプロキシがフィルタリングするのは、サンドボックス内で実行されるローカルコマンドの通信だけです。プロファイルのドメイン許可リストは、次の対象には適用されません：

- **ウェブ検索：** ホスト型の検索ツールは独自のアクセス設定を使用します。
制御には `web_search` を使用し、管理対象のクライアントでは `allowed_web_search_modes` も使用します。
  `tools.web_search.allowed_domains` がフィルタリングするのは検索結果であり、
  コマンドのネットワークアクセスではありません。
- **アプリとコネクタ：** コネクタを利用するツールは、独自のサービス側の接続、
  ワークスペースの権限、アプリまたはツールの設定に基づいて動作します。
- **MCP サーバー：** ローカルおよびリモートの MCP サーバーは、
  独自のプロセスまたはトランスポートを使用します。`mcp_servers` の設定と、
  管理対象のサーバー許可リストを使用して制御してください。
- **ブラウザとコンピューターの使用：** ブラウザでのページ移動やコンピューターの使用機能による操作は、
  それぞれ独自の機能設定と承認設定で制御されます。
- **Codex サービスの通信：** モデル、認証、その他のクライアントサービスへのリクエストには、
  クライアントの独立した HTTP 設定とシステムプロキシ設定が適用されます。
- **Codex Cloud：** これらのタスクには、
それぞれの環境に固有の[インターネットアクセス設定](/ja-JP/codex/cloud/internet-access)が適用されます。

これらの機能を制限するには、各機能を個別に設定してください。コマンド向けのネットワーク許可リストは、Codex が実行できるすべての操作に適用される全体的なネットワークポリシーではありません。

### 強制適用の仕組み

- macOS では、Codex は Seatbelt のサンドボックスプロファイルを使用します。選択したポリシーをプラットフォームのサンドボックスで強制適用できない場合、Codex は、通知なしでコマンドをサンドボックス外で実行するのではなく、実行を拒否します。
- Linux および WSL では、Codex は [bubblewrap](https://github.com/containers/bubblewrap)
  と [seccomp](https://www.kernel.org/doc/html/latest/userspace-api/seccomp_filter.html) を使用し、
  互換性のためのフォールバック手段として Landlock も利用できます。
  最も強力な強制適用方式を利用できるかどうかは、ユーザー名前空間とカーネルのサポート状況によって決まります。
  制限付きのコンテナホストでは互換性のための方式を使用せざるを得ない場合があり、
  サポートされていない分割ポリシーは拒否されます。
- ネイティブ Windows では、[`elevated` サンドボックス](/ja-JP/codex/windows/windows-sandbox#windows-sandbox) が最も強力です。
  専用の低権限サンドボックスユーザー、
  ファイルシステムの権限境界、ファイアウォールルールを使用できるためです。`unelevated` サンドボックスはフォールバック手段であり、
  ネットワークの分離が弱く、
  読み取りと書き込みを分ける例外設定のすべてを強制適用できません。そのため、対応していないポリシーは拒否されます。
  Linux のサンドボックスモデルが必要な場合は、WSL を使用してください。

### 運用上の指針

書き込みや外部へのネットワークアクセスを許可する場合は特に、タスクを完了できる範囲で最も権限の限定されたプロファイルを選択してください。承認ポリシー、シークレットの取り扱い、許可ルールも、そのアクセスレベルに合わせてください。

## 一般的なプロファイル

### ネットワーク許可リスト付きの読み取り専用

```toml
default_permissions = "readonly-net"

[features]
network_proxy = true

[permissions.readonly-net.filesystem]
":minimal" = "read"

[permissions.readonly-net.filesystem.":workspace_roots"]
"." = "read"

[permissions.readonly-net.network]
enabled = true

[permissions.readonly-net.network.domains]
"api.openai.com" = "allow"

### ワークスペースに限定したファイルアクセス

次の例は、Codex によるワークスペースフォルダーへの書き込みを許可する一方で、それ以外のファイルシステムの読み取りを拒否する権限プロファイルです（`:minimal` で定められる限定的な例外を除きます）。

```toml
default_permissions = "workspace-only"

[permissions.workspace-only]
# By extending the :workspace profile, you get Codex's safeguards to ensure
# subfolders such as .codex/ and .git/ within a workspace root are read-only
# while the rest of the folder is writable.
extends = ":workspace"

[permissions.workspace-only.filesystem]
# By default, deny read access to all files on disk.
":root" = "deny"

# Though in practice, a software agent needs to be able to read folders that
# contain common tools, such as `/usr/bin`, to get work done, so grant access
# to a "minimal" set of files and folders, as determined by Codex.
":minimal" = "read"

# By extending the :workspace profile, :tmpdir and :slash_tmp are "write" by
# default, though you can deny access to them altogether, if desired.
":tmpdir" = "deny"
":slash_tmp" = "deny"

### ネットワークアクセスなしのワークスペースへの書き込み

```toml
default_permissions = "project-edit"

[permissions.project-edit.filesystem]
":minimal" = "read"

[permissions.project-edit.filesystem.":workspace_roots"]
"." = "write"

[permissions.project-edit.network]
enabled = false

### パブリック Web へのアクセスを許可したワークスペースへの書き込み

```toml
default_permissions = "workspace-net"

[features]
network_proxy = true

[permissions.workspace-net.filesystem]
":minimal" = "read"

[permissions.workspace-net.filesystem.":workspace_roots"]
"." = "write"

[permissions.workspace-net.network]
enabled = true

[permissions.workspace-net.network.domains]
"*" = "allow"

パブリックネットワークへのアクセスを許可したい場合にのみ、グローバルな `"*"` 許可ルールを使用してください。
拒否ルールを使用すると、広範な許可リストを絞り込めます。
