<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/managed-configuration -->

管理対象の設定では、ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能の対象機能について、対応するローカルランタイムの動作を制御します。対応する要件は、クライアントやバージョンによって異なる場合があります。管理対象の設定によって、ChatGPT ワークスペースへのアクセス権が付与されたり、シートが割り当てられたり、ワークスペースのロールベースのアクセス制御（RBAC）が置き換えられたりすることはありません。ワークスペースの機能へのアクセスについては[ロールとワークスペースの権限](/ja-JP/codex/enterprise/roles-and-workspace-permissions)を、ローカルランタイムのポリシーについてはこのページを参照してください。

エンタープライズ管理者は、対応するローカルクライアントの動作を次の 2 つの方法で制御できます：

- **要件**：管理者が強制適用する、ユーザーが上書きできない制約
- **管理対象のデフォルト値**：対応するクライアントの起動時に適用される初期値です。ユーザーは実行中に設定を変更できますが、クライアントは次回の起動時に管理対象のデフォルト値を再適用します。

## 管理者が強制適用する要件（requirements.toml）

要件は、セキュリティ上重要な設定を制限します。対象となるのは、承認ポリシー、承認リクエストのレビュアー、自動レビューポリシー、サンドボックスモード、権限プロファイル、ウェブ検索モード、管理対象のフック、ユーザーが有効化できる MCP サーバー、およびユーザー設定のプラグインマーケットプレイスソースのうち、追加、インストール元としての使用、更新を許可するものです。設定の解決時に、たとえば `config.toml`、[プロファイルファイル](/ja-JP/codex/config-file/config-advanced#profiles)、CLI による設定の上書きから取得した値が強制適用されるルールと競合すると、ローカルクライアントは適合する値にフォールバックし、ユーザーに通知します。`mcp_servers` の許可リストを設定した場合、クライアントは名前と識別情報の両方が承認済みエントリと一致するときにのみ MCP サーバーを有効化し、それ以外の場合は無効化します。

要件では、`requirements.toml` 内の `[features]` テーブルを使用して[機能フラグ](/ja-JP/codex/config-file/config-basic/#feature-flags)も制限できます。機能は必ずしもセキュリティに関わるものではありませんが、企業は必要に応じて値を固定できます。省略したキーは制限されません。

Codex 0.138.0 以降では、[権限プロファイル](/ja-JP/codex/permissions)と、
`allowed_permission_profiles` および管理対象の `default_permissions` を使用することを推奨します。
`allowed_sandbox_modes` は、`sandbox_mode` を引き続き設定している
従来の導入環境でのみ使用してください。

キーの正確な一覧については、[構成リファレンスの `requirements.toml` セクション](/ja-JP/codex/config-file/config-reference#requirementstoml)を参照してください。

### 配置場所と優先順位

対応する各ローカルクライアントは、優先順位の低いものから高いものへと、次の順序で要件を統合します：

1. システムの `requirements.toml`（Linux や macOS を含む Unix システムでは `/etc/codex/requirements.toml`、
   Windows では
   `%ProgramData%\OpenAI\Codex\requirements.toml`）
2. クラウド構成バンドルで配信される、企業が管理する要件
3. ローカルクライアントが要件として再解釈する、従来の `managed_config.toml` フィールド
4. `com.openai.codex:requirements_toml_base64` を通じて配信される
macOS の管理対象環境設定（MDM）

優先順位の高いレイヤーは、低いレイヤーの
通常のスカラー値とリスト値を上書きします。テーブルはキーごとにマージされますが、
ルール、フック、ファイルシステムの制限などの要件は、フィールドごとに統合方法が異なります。
すべてのフィールドが同じ方法でマージされるとは想定せず、
[`requirements.toml` リファレンス](/ja-JP/codex/config-file/config-reference#requirementstoml)で
現在のスキーマを確認してください。

後方互換性を確保するため、対応するローカルクライアントは、
従来の `approval_policy`、`approvals_reviewer`、`sandbox_mode` の各フィールドを要件として再解釈します。
この変換では、必要に応じて互換性を確保するための選択肢が追加されます。
明示的な許可リストには `requirements.toml` を使用してください。

### クラウド管理の要件

対応プランのユーザーが ChatGPT でサインインすると、
対応するローカルクライアントは、管理者が強制適用するワークスペースに関連付けられた要件を受信できます。
これは、`requirements.toml` と互換性のあるポリシーの配信チャネルです。
ワークスペースへのアクセス権を付与したり、ワークスペースの RBAC を置き換えたりするものではありません。

[管理対象の設定](https://chatgpt.com/codex/settings/managed-configs)を開いて、
クラウド管理の要件を作成し、割り当てます。たとえば、次のポリシーでは、
承認とサンドボックスの選択肢を制限し、
対応するシェルのエントリポイントを実行する前に確認を求めます：

```toml
allowed_approval_policies = ["on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

[rules]
prefix_rules = [
  { pattern = [{ any_of = ["bash", "sh", "zsh"] }], decision = "prompt", justification = "Require explicit approval for shell entry points" },
]

管理対象のすべてのクライアントバージョンが選択したキーに対応していることを確認し、組織全体に割り当てる前に少人数のグループでポリシーをテストしてください。現在のスキーマは構成リファレンスで、現在の割り当て動作は管理画面で確認してください。

サービスは、サインイン中のユーザーの識別情報に適用される、
企業が管理する要件レイヤーを選択します。ローカルクライアントは、
それらのレイヤーを[配置場所と優先順位](#locations-and-precedence)に記載された他の要件ソースと併せて評価します。
ワークスペース側での作成と割り当てには、
現在の管理画面を使用してください。コピーしたグループ照合アルゴリズムに依存しないでください。
この動作は管理サービスが担っており、
ローカルの要件形式とは独立して変更できます。

対応するキーと使用例については、
[requirements.toml の例](#example-requirementstoml)と
[`requirements.toml` リファレンス](/ja-JP/codex/config-file/config-reference#requirementstoml)を参照してください。

#### ローカルクライアントでのクラウド管理要件の適用方法

対応プランのユーザーが対応するローカルクライアントを起動し、ChatGPT でサインインすると、クライアントはまず、そのユーザーの識別情報と一致する有効なキャッシュエントリがあるか確認します。有効なエントリがない場合は、再試行を行いながら該当するバンドルを取得し、成功すると署名付きのキャッシュエントリを書き込みます。リクエストが失敗またはタイムアウトし、有効なキャッシュもない場合、クラウド構成バンドルの読み込みはエラーを返します。クラウド管理の要件レイヤーなしで、何も通知せずに起動することはありません。

キャッシュの解決後、クライアントはクラウド要件を前述の他の要件レイヤーと統合します。バックグラウンド更新では、次回以降の起動に向けてキャッシュを更新できますが、現在のプロセスにすでに読み込まれた要件は置き換えられません。

### 管理者と従業員の利用体験の確認

各管理対象ポリシーの担当者を定め、適用対象となるユーザーまたはグループを記録してください。また、ファイルシステム、ネットワーク、承認、権限プロファイルに制限を設ける業務上の理由を文書化してください。

導入範囲を拡大する前に、代表的なユーザーと、承認済みのワークフローおよび意図的に許可していないワークフローをテストしてください。ワークスペースのロールやグループだけでローカルの制限が強制適用されるとは想定せず、対応するクライアントで実際に適用されている設定を確認してください。

### requirements.toml の例

この例では、`--ask-for-approval never` と `--sandbox danger-full-access`（`--yolo` を含む）をブロックします：

```toml
allowed_approval_policies = ["untrusted", "on-request"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

### Appshots の無効化

管理対象ユーザーの Appshots を無効化するには、トップレベルの `allow_appshots` 要件を設定します：

```toml
allow_appshots = false

Appshots を利用できる環境では、`allow_appshots = false` によって Appshots が無効化されます。
このキーを省略すると、要件による Appshots の制限はなく、
通常どおり製品の利用可否がチェックされます。
`configRequirements/read` を通じて実際に適用されている要件を読み取る App Server クライアントは、
`allowAppshots` として同じ制限を受け取ります。`allowAppshots` が省略されている場合や値が `null` の場合は、
Appshots は無効化されません。

### デバイスのリモートコントロールの無効化

管理対象ユーザーの[デバイスのリモートコントロール](/ja-JP/codex/remote-connections#pick-up-work-from-another-device)を無効化するには、
トップレベルの `allow_remote_control` 要件を設定します：

```toml
allow_remote_control = false

デバイスのリモートコントロールに対応する環境では、`allow_remote_control = false` によって無効化されます。
このキーを省略すると、要件によるデバイスのリモートコントロールの制限はなく、
通常どおり製品の利用可否がチェックされます。
この要件によって SSH リモート接続が無効化されることはありません。

### 利用可能な権限プロファイルの制御

`allowed_permission_profiles` を使用して、組み込みおよびカスタムのプロファイルのうち、
ユーザーが選択できる[権限プロファイル](/ja-JP/codex/permissions)を制御します。
これは、`allowed_sandbox_modes` に相当する権限プロファイル用の設定です。
ユーザーが権限を選択する方法に合った許可リストを使用してください。

権限プロファイルの許可リストには、Codex 0.138.0 以降が必要です。
Codex 0.137.0 以前では、`allowed_permission_profiles` と
管理対象の `default_permissions` が無視されます。

以下の権限プロファイルの例は、管理対象のすべてのクライアントで対応バージョンが稼働している場合にのみ使用してください。全クライアントのアップグレードが完了するまでは、管理対象のカスタムプロファイルを配布しないでください。

このテーブルを指定した場合、これが許可されるプロファイルの完全な一覧となります。
`true` に設定されたプロファイルは許可され、省略されたプロファイルや `false` に設定されたプロファイルは拒否されます。
今後の Codex バージョンで追加される組み込みプロファイルも対象です。

#### 標準プロファイルの許可

このポリシーでは、読み取り専用のアクセスとワークスペースへのアクセスは許可されますが、フルアクセスは許可されません：

```toml
default_permissions = ":workspace"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

#### 最小権限の管理対象デフォルト値の追加

管理者は、同じ要件ソースにカスタムプロファイルを定義できます。
ユーザーが読み込んでいる設定内の名前と競合しないよう、
組織固有のプロファイル名を使用してください。カスタム名は `:` で始めることができず、
予約済みの名前である `filesystem` も使用できません。

Codex 0.137.0 以前を実行しているクライアントには、管理対象のカスタムプロファイルを配布しないでください。これらのクライアントはプロファイルテーブルを認識しますが、そのプロファイルを選択する管理対象のデフォルト値は認識しません。

例：

```toml
default_permissions = "acme_review_only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
acme_review_only = true
# ":danger-full-access" is intentionally omitted, so it is denied.

[permissions.acme_review_only]
description = "Review code without modifying the workspace."
extends = ":read-only"

#### 企業が定義したプロファイルのみの許可

ユーザーが管理者定義のプロファイルのみを選択できるようにするには、組み込みプロファイルをすべて省略します：

```toml
default_permissions = "acme_workspace"

[allowed_permission_profiles]
acme_workspace = true

[permissions.acme_workspace]
description = "Workspace access with sensitive files denied."
extends = ":workspace"

[permissions.acme_workspace.filesystem]
glob_scan_max_depth = 3

[permissions.acme_workspace.filesystem.":workspace_roots"]
"**/*.env" = "deny"

ユーザーが組み込みの `:workspace` プロファイルを直接選択できない場合でも、
カスタムプロファイルで `:workspace` を拡張できます。

#### 別のソースで許可されたプロファイルの無効化

権限の許可リストは、プロファイル名ごとに統合されます。
クラウド要件はシステム要件よりも優先順位が高いため、クラウド要件で `false` を指定すると、
システムファイルで許可されたプロファイルを無効化できます。

クラウド要件：

```toml
default_permissions = ":read-only"

[allowed_permission_profiles]
":read-only" = true
":workspace" = false

システム要件：

```toml
[allowed_permission_profiles]
":read-only" = true
":workspace" = true  # Not honored because cloud requirements set this to false.

`default_permissions` には、許可されたプロファイルを明示的に設定してください。
この設定を省略すると、`:workspace` と `:read-only` の両方が明示的に許可されている場合に限り、
ローカルランタイムはデフォルトとして `:workspace` を使用します。`allowed_permission_profiles` がない場合、
管理対象の要件は、ユーザーが選択できるプロファイル名を制限しません。
各エントリには、組み込みプロファイル、または
読み込み済みの設定や要件ソースで定義されたカスタムプロファイルの名前を指定する必要があります。
動作を一元的に制御するには、カスタムプロファイルを管理対象の要件で定義してください。

### ホストごとのサンドボックス要件の上書き

1 つの管理対象ポリシーでホストごとに異なるサンドボックス要件を適用する場合は、`[[remote_sandbox_config]]` を使用します。
たとえば、ノート PC にはより厳格なデフォルト値を維持しながら、
条件に一致する開発マシンや CI ランナーではワークスペースへの書き込みを許可できます。
現在、ホスト固有のエントリで上書きできるのは `allowed_sandbox_modes` のみです：

```toml
allowed_sandbox_modes = ["read-only"]

[[remote_sandbox_config]]
hostname_patterns = ["*.devbox.example.com", "runner-??.ci.example.com"]
allowed_sandbox_modes = ["read-only", "workspace-write"]

ローカルランタイムは、`hostname_patterns` の各エントリを、
可能な範囲で解決したホスト名と比較します。完全修飾ドメイン名を取得できる場合はそちらを優先し、
取得できない場合はローカルのホスト名を使用します。照合では大文字と小文字を区別しません。
`*` は任意の文字列に一致し、`?` は 1 文字に一致します。

同じ要件ソース内では、最初に一致した `[[remote_sandbox_config]]` エントリが優先されます。
一致するエントリがない場合、ローカルランタイムは
トップレベルの `allowed_sandbox_modes` を維持します。ホスト名の照合はポリシーの選択専用です。
デバイスが認証済みであることの証明として扱わないでください。

ウェブ検索モードも制限できます：

```toml
allowed_web_search_modes = ["cached"] # "disabled" remains implicitly allowed

`allowed_web_search_modes = []` では `"disabled"` のみが許可されます。
たとえば、`allowed_web_search_modes = ["cached"]` を設定すると、`danger-full-access` セッションでもライブウェブ検索は実行できません。

### ネットワークアクセス要件の構成

  `[experimental_network]` は試験段階の機能であり、今後変更される可能性があります。
  ユーザーが使用するローカルクライアントのバージョンとオペレーティングシステムで検証せずに、
  これらの要件を企業の導入環境全体で広く有効にしないでください。
  Windows のサポートはまだ限定的なため、お使いの環境でテストしていない場合は、
  このポリシーを Windows ユーザーに適用しないでください。

管理者がネットワークアクセス要件を一元的に定義するには、
`requirements.toml` の `[experimental_network]` を使用します。これらの要件は、
ユーザー側の `features.network_proxy` の切り替え設定とは別のものです。この機能フラグがなくてもサンドボックスのネットワークを構成できますが、
使用中のサンドボックスでネットワークが無効になっている場合は、
コマンドにネットワークアクセスを許可しません。管理対象プロキシを有効にするには、
`experimental_network.enabled = true` を設定します。
ドメインルールだけではプロキシは有効になりません。

```toml
[experimental_network]
enabled = true
managed_allowed_domains_only = true

[experimental_network.domains]
"api.openai.com" = "allow"
"**.example.com" = "allow"
"blocked.example.com" = "deny"
"**.exfil.example.com" = "deny"

`experimental_network.managed_allowed_domains_only = true` は、
`[experimental_network.domains]` に管理者が管理する `"allow"` エントリも定義し、
それらのルールだけで許可を判定する場合にのみ使用してください。
管理対象の許可ルールがない状態で `true` に設定すると、ユーザーが追加したドメイン許可ルールは
無効になります。正規の `domains` マップを、
従来の `allowed_domains` または `denied_domains` リストと併用しないでください。

`*.example.com` はサブドメインにのみ一致します。`**.example.com` はドメイン自体と
そのサブドメインに一致します。一致する拒否ルールがある場合は、許可ルールより優先されます。

ドメイン構文、ローカルまたはプライベートの宛先に関するルール、拒否ルールを許可ルールより優先する動作、
DNS リバインディングの制限は、
[エージェントの承認とセキュリティ](/ja-JP/codex/agent-approvals-security#network-isolation)で説明しているサンドボックスネットワークの動作と同じです。

プロキシは、サンドボックス内で実行されるローカルコマンドの通信をルーティングします。ブラウザツールも、オリジンにアクセスする前に、管理対象のネットワーク拒否ルールと、そのリストだけで許可を判定する許可リストを確認します。これは独立したポリシーチェックであり、ブラウザの通信をコマンド用プロキシ経由でルーティングするものではありません。このプロキシは、ウェブ検索、アプリとコネクタ、MCP サーバー、ネイティブアプリの通信、Codex サービスへのリクエスト、Codex Cloud の通信をフィルタリングしません。対象ごとに次の制御を使用してください：

- `allowed_web_search_modes` を使用してウェブ検索を制限します。
- `features.apps = false` を使用してアプリとコネクタの連携を無効にし、
対応する環境では `features.plugins = false` を使用してプラグインを無効にします。
- 管理対象の `mcp_servers` の承認済みリストを使用して、MCP サーバーを制限します。
- `browser_use`、`in_app_browser`、
`computer_use` などの機能要件を使用して、ブラウザ機能とコンピューターの使用を制限します。
- Codex Cloud のネットワークアクセスは、そのクラウド環境の設定で構成します。

コマンド用のドメイン許可リストは、これらの機能ごとの制御に代わるものではありません。

### ブラウザとコンピューターの使用の制御

対応するデスクトップクライアントを制限するには、`requirements.toml` の `[browser_use]` テーブルと `[computer_use]` テーブルを
使用します。導入環境で使用するクライアントのバージョンと
オペレーティングシステムでポリシーを検証してください。許可ルールを設定しても、
プラグインのインストールやオペレーティングシステムの権限付与は行われず、
レビューが必要な操作が承認されることもありません。

ブラウザアクセスには、オリジンポリシーを構成します。オリジンには、
`https://example.com` や `https://*.example.com:8443` のように、スキーム、ホスト、任意のポートが含まれます。
パス、クエリ、フラグメントは含めないでください。
コマンドのネットワーク通信に対するドメインルールとは異なり、ブラウザのオリジンルールは HTTP と HTTPS を区別し、
ポートも照合します。

この例では、ブラウザアクセスを承認済みのサイトに制限し、そのサイトでのアップロードと Chrome DevTools Protocol（CDP）へのフルアクセスを禁止します：

```toml
[browser_use]
allow_history_access = false
allow_global_persistent_approval = false

[browser_use.default_origin_policy]
access = "deny"

[browser_use.origins."https://example.com"]
access = "allow"
uploads = "deny"
downloads = "allow"
full_cdp_access = "deny"
persistent_approval = false
access_approval_lifetime = "turn"

一致するオリジンルールは、フィールドごとに評価されます。一致する拒否ルールが優先され、それ以外では、一致するルールで指定されていないフィールドにデフォルトのオリジンポリシーが適用されます。ローカル構成で制限を追加することはできますが、管理対象の拒否ルールを緩和することはできません。ネットワーク拒否ルールと、管理対象のリストだけで許可を判定するネットワーク許可リストも引き続き適用されます。

ブラウザ操作の承認リクエストに対する自動レビューを無効にするには、`browser_use.disable_auto_review = true` を設定します。
特定のオリジンで自動レビューを制限するには、
そのオリジンのポリシーに `auto_review = "deny"` を設定します。これは承認の処理を制御するものであり、
モデルの安全性監視を無効にするものではありません。

ネイティブアプリについては、デフォルトのアクセスポリシーを設定し、許可するアプリを指定します。たとえば、次の macOS ポリシーは「計算機」を許可し、承認の保存を禁止します：

```toml
[computer_use]
default_app_access = "deny"
allow_persistent_approval = false

[computer_use.macos.bundle_ids]
"com.apple.calculator" = "allow"

Windows ポリシーでは、
`computer_use.windows.aumids` でパッケージアプリを、
`computer_use.windows.exes` で実行可能ファイルを識別できます。実行可能ファイルのルールには `publisher_name`、
`product_name`、`access` が必須で、`binary_name` は任意です。表示名だけでなく、
検証済みのアプリ識別情報を使用してください。

すべてのフィールドについては[構成リファレンス](/ja-JP/codex/config-file/config-reference#requirementstoml)を、
管理対象の macOS デバイスについては
[ロック中の使用制限](#restrict-locked-computer-use)を参照してください。

### 機能フラグの固定

管理対象の `requirements.toml` を受け取るユーザーに対して、
[機能フラグ](/ja-JP/codex/config-file/config-basic/#feature-flags)を固定することもできます：

```toml
[features]
personality = true
unified_exec = false

# Disable surface-specific features when needed.
browser_use = false
browser_use_full_cdp_access = false
browser_use_external = false
in_app_browser = false
in_app_updates = false
computer_use = false

ランタイム機能には、`config.toml` の `[features]` テーブルにある正規の機能キーを使用してください。
ローカルランタイムは、認識した機能を固定値に合わせて正規化し、
`config.toml` またはプロファイルファイルの機能設定に対する、
固定値と競合する書き込みを拒否します。

<a id="disable-codex-feature-surfaces"></a>

- `in_app_browser = false` は、組み込みのブラウザペインを無効にします。
- `in_app_updates = false` は、対応する環境では再起動時に
  ChatGPT デスクトップアプリ自体のアップデーターを無効にします。外部からのパッケージ配布には影響せず、
  古いバージョンのアプリに対するサポートも延長されません。セットアップとロールアウトの詳細については、
[アプリの更新管理](/ja-JP/codex/enterprise/manage-app-updates)を参照してください。
- `browser_use = false` は、ブラウザでのコンピューターの使用を無効にし、ブラウザエージェントも利用できないようにします。
- `browser_use_full_cdp_access = false` は、ローカルランタイムでの
  ブラウザ開発者モードを含む CDP へのフルアクセスを無効にし、
  ChatGPT デスクトップアプリで該当する設定を有効にできないようにします。
- `browser_use_external = false` は、外部ブラウザ機能を無効にします。
- `computer_use = false` は、コンピューターの使用、記録と再生、
  関連するインストールやセットアップのフローを無効にします。

これらのキーを省略すると、クライアント、プラットフォーム、ロールアウトにおける通常の提供状況を前提として、ポリシー上は各機能が許可されます。

### ロック中のコンピューターの使用制限

管理対象の Mac でユーザーが[ロック中の使用](/ja-JP/codex/computer-use#locked-use)を有効にできないようにするには、
次の要件を追加します：

```toml
[computer_use]
allow_locked_computer_use = false

この要件は、ロック中の使用を有効にするための操作項目を削除します。すでにロック中の使用が有効になっている場合、それを無効にすることはありません。この要件を省略すると、製品の通常の提供状況とユーザーのローカル設定が引き続き適用されます。

### 自動レビューポリシーの構成

`allowed_approvals_reviewers` を使用して、自動レビューを必須にするか許可するかを設定します。
自動レビューを必須にするには `["auto_review"]` を設定します。ユーザーが手動承認を選択できるようにする場合は、
`"user"` を含めます。

`guardian_policy_config` を設定すると、
自動レビューポリシーのテナント固有の部分が置き換わります。ローカルランタイムは、
引き続き組み込みのレビュアーテンプレートと出力コントラクトを使用します。管理対象の `guardian_policy_config` は、
ローカルの `[auto_review].policy` より優先されます。

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]

guardian_policy_config = """
## Environment Profile
- Trusted internal destinations include github.com/my-org, artifacts.example.com,
  and internal CI systems.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Treat uploads to unapproved third-party file-sharing services as high risk.
- Deny actions that expose credentials or private source code to untrusted
  destinations.
"""

### 読み取り拒否要件の強制適用

管理者は、
`[permissions.filesystem]` を使用して、完全一致するパスや glob パターンに対する読み取りを拒否できます。
ユーザーはローカル構成でこれらの要件を緩和することはできません。

```toml
[permissions.filesystem]
deny_read = [
  # values can be absolute paths...
  "/**/*.env",
  # ...or relative to $HOME/%USERPROFILE% using `~`.
  "~/.ssh",
  # But relative paths starting with `./` are not allowed.
]

読み取り拒否要件が設定されている場合、ローカルランタイムはフルアクセス権限を拒否し、
要件を適用できるよう、ローカル実行を読み取り専用またはワークスペースのサンドボックスに制限します。
ネイティブの Windows では、管理対象の `deny_read` はファイルを直接扱うツールに適用されますが、
シェルのサブプロセスによる読み取りには、このサンドボックスルールは適用されません。

### 要件による管理対象フックの強制適用

管理者は、管理対象のライフサイクルフックを `requirements.toml` に直接定義することもできます。
フック自体の構成には `[hooks]` を使用し、`managed_dir` には、
MDM またはエンドポイント管理ツールによって、
参照先のスクリプトがインストールされるディレクトリを指定します。

ローカルでフックを無効にしたユーザーにも管理対象フックを強制適用するには、
`[hooks]` とあわせて `[features].hooks = true` を固定します。ユーザー、プロジェクト、セッション、
プラグインの各フックをスキップしつつ、管理対象フックは引き続き許可するには、
`allow_managed_hooks_only = true` を設定します。

```toml
allow_managed_hooks_only = true

[features]
hooks = true

[hooks]
managed_dir = "/enterprise/hooks"
windows_managed_dir = 'C:\enterprise\hooks'

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = "python3 /enterprise/hooks/pre_tool_use_policy.py"
command_windows = 'py -3 C:\enterprise\hooks\pre_tool_use_policy.py'
timeout = 30
statusMessage = "Checking managed Bash command"

注：

- ローカルランタイムは `requirements.toml` のフック構成を強制適用しますが、
  `managed_dir` 内のスクリプトは配布しません。
- これらのスクリプトは、MDM またはデバイス管理ソリューションを使用して配布してください。
- 管理対象フックのコマンドでは、構成済みの管理対象ディレクトリ配下にあるスクリプトを絶対パスで参照してください。
- `allow_managed_hooks_only = true` を設定すると、ユーザー、プロジェクト、セッション、
  プラグイン由来のフックはスキップされますが、`requirements.toml` や
  その他の管理対象構成レイヤーのフックは引き続き読み込まれます。

### 要件によるコマンドルールの強制適用

管理者は `requirements.toml` で、
`[rules]` テーブルを使用して、コマンドを制限するルールを強制適用することもできます。これらのルールは通常の `.rules` ファイルとマージされ、
引き続き最も制限の厳しい判定が優先されます。

`.rules` とは異なり、要件ルールでは `decision` を指定する必要があり、
その値は `"prompt"` または `"forbidden"` でなければなりません（`"allow"` は指定できません）。

```toml
[rules]
prefix_rules = [
  { pattern = [{ token = "rm" }], decision = "forbidden", justification = "Use git clean -fd instead." },
  { pattern = [{ token = "git" }, { any_of = ["push", "commit"] }], decision = "prompt", justification = "Require review before mutating history." },
]

ローカルクライアントで有効にできる MCP サーバーを制限するには、`mcp_servers` の承認済みリストを追加します。
stdio サーバーについては `command` を照合し、
Streamable HTTP サーバーについては `url` を照合します：

```toml
[mcp_servers.docs]
identity = { command = "codex-mcp" }

[mcp_servers.remote]
identity = { url = "https://example.com/mcp" }

`identity.command` を文字列として指定した場合、照合されるのは構成済みの `command` のみです。
`args`、`cwd`、`env`、`env_vars` は検査されません。

stdio 呼び出し全体を制限するには、実行可能ファイルと各位置引数を照合します：

```toml
[mcp_servers.internal.identity]
command = { executable = "/usr/local/bin/codex-mcp", args = [
  { match = "exact", value = "serve" },
  { match = "prefix", value = "--workspace=" },
] }

実行可能ファイル、引数の数、引数の順序が一致している必要があります。
引数と URL のルールは、`exact`、`prefix`、値全体を対象とする `regex` による照合に対応しています。
構造化されたコマンドルールでも、`cwd`、`env`、`env_vars` は検査されません。
プラグインに同梱された MCP サーバーでは、
`plugins.<plugin>.mcp_servers.<server>` 配下で同じ形式の識別情報を使用します。

`mcp_servers` が存在するものの空の場合、ローカルクライアントはすべての MCP サーバーを無効にします。

### プラグインの利用可否の制御

対応するローカルクライアントでプラグインを無効にするには、
`requirements.toml` で `features.plugins` を `false` に設定します：

```toml
features.plugins = false

この設定は、ユーザーが API キーで Codex にサインインする場合にも適用されます。
対応する構成については、[`features.plugins`
のリファレンス](/ja-JP/codex/config-file/config-reference#requirementstoml)を
参照してください。

### プラグインマーケットプレイスのソース制限

ユーザーが構成したマーケットプレイスソースでの操作を制限するには、
`restrict_to_allowed_sources = true` を設定し、1 つ以上のソースルールを定義します：

```toml
[marketplaces]
restrict_to_allowed_sources = true

[marketplaces.allowed_sources.company_plugins]
source = "git"
url = "https://github.com/example/company-plugins.git"
ref = "main"

[marketplaces.allowed_sources.internal_git]
source = "host_pattern"
host_pattern = '^git\.example\.com$'

[marketplaces.allowed_sources.local_plugins]
source = "local"
path = "/opt/company/codex-plugins"

Git ルールは、正規化されたリポジトリ URL を照合し、
`ref` が指定されている場合は、その完全一致も確認します。ホストパターンは、小文字に変換した Git ホストを対象に照合する正規表現です。
ホスト名全体と一致させるには、`^` と `$` を使用します。ローカルルールでは、
正規化された絶対パスが必要です。完全なスキーマとマージ動作については、
[`requirements.toml` リファレンス](/ja-JP/codex/config-file/config-reference#requirementstoml)を参照してください。

これらの要件は、ユーザーが構成したソースに対する操作のうち、ルールに一致しないマーケットプレイスの追加、プラグインのインストール、構成済み Git マーケットプレイスの更新を拒否します。Codex が管理する OpenAI マーケットプレイスは、ソースと予約名が一致する場合、引き続き利用できます。これらの要件は、ユーザーがすでに構成したマーケットプレイスやそのプラグインを実行時にフィルタリングするものではありません。

これらのソース制限は、プラグインのマーケットプレイス操作に対応するローカルクライアント、つまりデスクトップアプリ内の ChatGPT と Codex、および Codex CLI にのみ適用されます。Web 版やモバイル版の ChatGPT でのプラグイン利用は制御せず、IDE 拡張機能にプラグインを追加するものでもありません。

## 管理対象のデフォルト（`managed_config.toml`）

管理対象のデフォルトは、対応するローカルクライアントの起動時に使用する構成を定めます。
起動時には、ユーザーのローカルの `config.toml` と、CLI の `--config` による
上書き設定より優先されます。ユーザーは実行中にこれらの設定を変更できますが、
クライアントの次回起動時には、デフォルトが再び適用されます。

ChatGPT でサインインするユーザー向けに、管理対象のデフォルト、macOS MDM プロファイル、または保存済みの構成で `gpt-5.4`
または `gpt-5.4-mini` を固定している場合は、2026 年 8 月 31 日より前に更新してください。`gpt-5.4` を `gpt-5.6-terra` に、`gpt-5.4-mini` を
`gpt-5.6-luna` に置き換えます。OpenAI API と、自分の API キーで認証した Codex は
影響を受けません。[ワークスペースで利用可能な
モデル](/ja-JP/codex/enterprise/workspace-model-availability#prepare-for-the-gpt-54-retirement)を参照してください。

管理対象のデフォルトが要件を満たしていることを確認してください。ローカルランタイムは、許可されていない値を拒否します。

### 優先順位とレイヤー構成

ローカルランタイムは、次の優先順位で構成を組み合わせ、実際に適用する構成を決定します（上位が下位を上書きします）：

- 管理対象の環境設定（macOS MDM、最優先）
- `managed_config.toml`（システムファイル／管理対象ファイル）
- `config.toml`（ユーザーの基本構成）

CLI の `--config key=value` による上書きは基本構成に適用されますが、管理対象レイヤーがさらにそれを上書きします。そのため、ローカルフラグを指定しても、実行は毎回、管理対象のデフォルトから開始されます。

クラウド管理の要件は、管理対象のデフォルトではなく要件レイヤーに適用されます。優先順位については、上記の「管理者が適用する要件」セクションを参照してください。

### 保存場所

- Linux/macOS（Unix）：`/etc/codex/managed_config.toml`
- Windows／Unix 以外：`~/.codex/managed_config.toml`

ファイルが存在しない場合、ローカルランタイムは管理対象レイヤーをスキップします。

### macOS の管理対象の環境設定（MDM）

macOS では、管理者は以下のドメインとキーに base64 エンコードされた TOML ペイロードを設定するデバイスプロファイルを配布できます：

- 環境設定ドメイン：`com.openai.codex`
- キー：
  - `config_toml_base64`（管理対象のデフォルト）
  - `requirements_toml_base64`（要件）

ローカルランタイムは、これらの「管理対象の環境設定」ペイロードを TOML として解析します。
管理対象のデフォルト（`config_toml_base64`）では、管理対象の環境設定が
最優先されます。要件（`requirements_toml_base64`）では、
前述のクラウド管理の要件の優先順位に従います。
要件側の `[features]` テーブルは、`requirements_toml_base64` でも同様に使用できます。
ここでも正規の機能キーを使用してください。

### MDM セットアップのワークフロー

ローカルランタイムは標準の macOS MDM ペイロードに対応しているため、
`Jamf Pro`、`Fleet`、`Kandji` などのツールで設定を配布できます。
簡単な導入手順は次のとおりです：

1. 管理対象ペイロードの TOML を作成し、`base64` でエンコードします（改行なし）。
2. その文字列を、MDM プロファイルの `com.openai.codex` ドメインにある `config_toml_base64`（管理対象のデフォルト）または `requirements_toml_base64`（要件）に設定します。
3. プロファイルを配布した後、対応するローカルクライアントを再起動し、起動時の構成概要に管理対象の値が反映されていることを確認するよう、ユーザーに依頼します。
4. ポリシーを取り消す場合や変更する場合は、管理対象ペイロードを更新してください。クライアントは次回の起動時に、更新された環境設定を読み込みます。

シークレットや変更頻度の高い動的な値をペイロードに埋め込まないでください。管理対象の TOML も、他の MDM 設定と同様に変更管理の対象として扱ってください。

### managed\_config.toml の例

```toml
# Set conservative defaults
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false             # keep network disabled unless explicitly allowed

[otel]
environment = "prod"
exporter = "otlp-http"            # point at your collector
log_user_prompt = false            # keep prompts redacted
# exporter details live under exporter tables; see Monitoring and telemetry above

### 推奨ガードレール

- ほとんどのユーザーには承認を伴う `workspace-write` を推奨します。フルアクセスは、管理下にあるコンテナに限定してください。
- セキュリティレビューでコレクターまたはワークフローに必要なドメインへのアクセスが許可されていない限り、`network_access = false` を維持してください。
- 管理対象の設定を使用して OTel の設定（エクスポーター、環境）を固定してください。ただし、ポリシーでプロンプト内容の保存が明示的に許可されていない限り、`log_user_prompt = false` を維持してください。
- 構成のずれを検出するため、ローカルの `config.toml` と管理対象のポリシーの差分を定期的に監査してください。管理対象レイヤーがローカルのフラグやファイルより優先されるようにしてください。
