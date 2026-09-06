<!-- source: https://learn.chatgpt.com/ja-JP/docs/agent-approvals-security -->

Codex はコードとデータの保護に役立ち、誤用のリスクを軽減します。

  このページでは、サンドボックス、承認、
  ネットワークアクセスなど、Codex を安全に運用する方法を説明します。接続済みの GitHub リポジトリをスキャンする製品、
  Codex Security については、[Codex Security](/ja-JP/codex/security) を参照してください。

デフォルトでは、エージェントはネットワークアクセスを無効にした状態で実行されます。ローカル環境では、Codex は OS によって強制されるサンドボックスを使用し、アクセス範囲を通常は現在のワークスペースに制限します。さらに、操作前に停止してユーザーに承認を求めるタイミングを、承認ポリシーで制御します。

ChatGPT デスクトップアプリ、
Codex CLI、IDE 拡張機能におけるサンドボックスの仕組みの概要は、[サンドボックス](/ja-JP/codex/sandboxing)を参照してください。
エンタープライズセキュリティの全体像については、[Codex セキュリティホワイトペーパー](https://trust.openai.com/?itemUid=382f924d-54f3-43a8-a9df-c39e6c959958&source=click)を参照してください。

## サンドボックスと承認

Codex のセキュリティ制御は、連携して機能する次の 2 つのレイヤーで構成されます。

- **サンドボックスモード**：モデルが生成したコマンドを実行する際に、Codex が技術的に実行できる操作を定めます。たとえば、書き込み可能な場所やネットワークへのアクセス可否などです。
- **承認ポリシー**：Codex が操作を実行する前に、ユーザーに承認を求める必要があるタイミングを定めます。たとえば、サンドボックス外での操作、ネットワークの使用、信頼済みのコマンド群に含まれないコマンドの実行などです。

Codex は、実行場所に応じて異なるサンドボックスモードを使用します。

- **Codex Cloud**：OpenAI が管理する分離されたコンテナー内で実行されるため、ホストシステムや無関係なデータにはアクセスできません。ランタイムは 2 つのフェーズで構成されます。セットアップはエージェントフェーズの前に実行され、指定された依存関係をインストールするためにネットワークへアクセスできます。その後のエージェントフェーズは、その環境でインターネットアクセスを有効にしない限り、デフォルトでオフラインで実行されます。クラウド環境に設定されたシークレットはセットアップ中にのみ使用でき、エージェントフェーズの開始前に削除されます。
- **Codex CLI / IDE 拡張機能**：OS レベルの仕組みによってサンドボックスポリシーが強制されます。デフォルトではネットワークにアクセスできず、書き込み権限はアクティブなワークスペースに限定されます。リスク許容度に応じて、サンドボックス、承認ポリシー、ネットワーク設定を構成できます。

`Auto` プリセット（例：`--sandbox workspace-write --ask-for-approval on-request`）では、Codex は作業ディレクトリ内で、ファイルの読み取り、編集、コマンドの実行を自動的に行えます。

ワークスペース外のファイルを編集する場合や、ネットワークアクセスが必要なコマンドを実行する場合、Codex は承認を求めます。変更を加えずにチャットや計画だけを行うには、`/permissions` コマンドで `read-only` モードに切り替えてください。

副作用があることを示すアプリ（コネクタ）のツール呼び出しについては、シェルコマンドの実行やファイルの変更を伴わない場合でも、Codex が承認を求めることがあります。破壊的な操作を行うアプリや MCP のツール呼び出しは、ツールが破壊的な操作を示すアノテーションを提示している場合、必ず承認が必要です。ただし、読み取りを示すアノテーションを提示している場合は、そちらが優先されます。

## 安全性モニタリングとタスクの一時停止

GPT-6 Astra には、Codex と ChatGPT Work での安全性モニタリングが組み込まれています。モニタリングは非同期で実行され、モデルに安全でない可能性のある動作を検出すると、タスクを一時停止することがあります。一時停止は、そのきっかけとなった操作の後に行われる場合があります。モニタリングは、サンドボックス、権限、結果のレビューに代わるものではありません。

タスクが一時停止した場合は通知を読み、検出内容を確認できる場合はレビューしてください。タスクを安全に続行できることを確認してから再開してください。通知にタスクが終了したと表示される場合や、再開する選択肢がない場合は、そのクライアントから再開することはできません。

| 利用環境とデータ制御                                                                               | 検出内容の確認と再開                                       |
| ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| 検出内容の確認と再開に対応し、ここに記載するデータ制御が適用されていない Codex および ChatGPT Work クライアント | 再開する前に検出内容をレビューしてください。                      |
| Codex CLI とモバイル                                                                                    | 検出内容の詳細確認と再開は利用できません。タスクは終了します。 |
| ゼロデータ保持、Modified Abuse Monitoring、または米国外のデータストレージレジデンシー                        | 検出内容の詳細確認と再開は利用できません。タスクは終了します。 |

安全性モニタリングは、タスク実行中のモデルの動作を評価します。
[承認リクエストの自動レビュー](/ja-JP/codex/sandboxing/auto-review)は、承認が必要な個々の操作を、
実行前に評価します。自動レビューで操作が承認されていても、
その操作を含むタスクが後からモニタリングによって一時停止されることがあります。

## ネットワークアクセス 

Codex Cloud で完全なインターネットアクセスまたはドメイン許可リストを有効にする方法については、[エージェントのインターネットアクセス](/ja-JP/codex/cloud/internet-access)を参照してください。

ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能のデフォルトの `workspace-write` サンドボックスモードでは、次のように設定で有効にしない限り、ネットワークアクセスは無効のままです。

```toml
[sandbox_workspace_write]
network_access = true

### ネットワーク分離

ネットワークアクセスは、スクリプト、プログラム、
コマンドから起動されるサブプロセスに適用される接続先ルールによって制御されます。
コマンドのネットワークアクセスがすでに有効な場合は、`network_proxy` 機能をオンにすると、
そのトラフィックを設定したネットワークポリシーに従って制限できます。
ドメインルールを追加しただけでは、プロキシは有効になりません。

```toml
[features.network_proxy]
enabled = true
domains = { "api.openai.com" = "allow", "example.com" = "deny" }

単発の CLI セッションでは、有効と無効の切り替えだけが必要な場合は真偽値の省略形式を使用し、ポリシーオプションも設定する場合はテーブル形式を使用します。

```bash
codex \
  -c 'features.network_proxy=true' \
  -c 'sandbox_workspace_write.network_access=true'

codex \
  -c 'features.network_proxy.enabled=true' \
  -c 'features.network_proxy.domains={ "api.openai.com" = "allow", "example.com" = "deny" }' \
  -c 'sandbox_workspace_write.network_access=true'

この機能は、有効なネットワークアクセスの制御方法を変更するものであり、
それ自体でネットワークアクセスを許可するものではありません。コマンドにネットワークアクセスを許可するかどうかは、`sandbox_workspace_write.network_access` を
`workspace-write` の設定と組み合わせて指定します。

- ネットワークがオフ + `network_proxy` がオン：ネットワークはオフのままで、この機能は何も行いません。
- ネットワークがオン + `network_proxy` がオフ：ネットワークはオンのままで、
  外部への直接アクセスに制限はありません。
- ネットワークがオン + `network_proxy` がオン：ネットワークはオンのままで、
  アウトバウンドトラフィックは設定されたネットワークポリシーによって制限されます。

プロキシ機能は、[権限プロファイル](/ja-JP/codex/permissions#network-permissions)にも適用されます。
プロファイルの `network.enabled = true` はコマンドによるネットワークアクセスを許可し、
`features.network_proxy = true` は、そのプロファイルに設定されたドメインルールによる
制御を有効にします。

```toml
default_permissions = "project-edit"

[features]
network_proxy = true

[permissions.project-edit]
extends = ":workspace"

[permissions.project-edit.network]
enabled = true

[permissions.project-edit.network.domains]
"api.openai.com" = "allow"

この例でプロキシ機能を省略すると、コマンドはネットワークへ直接アクセスでき、
`api.openai.com` の許可ルールによって接続先が制限されることはありません。

管理者が管理する `experimental_network` の要件は、
ユーザー側の機能の切り替えとは別です。これらの要件により、`features.network_proxy` がなくても、
サンドボックス化されたネットワークを構成して起動できます。ただし、適用中のサンドボックスでネットワークアクセスが無効な場合は、
有効にはなりません。管理者側の `requirements.toml` の形式については、
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration#configure-network-access-requirements)を参照してください。

#### ネットワークポリシー

ドメインルールは、許可リストを基本として適用されます。

- 完全一致のホスト指定は、そのホスト名にのみ一致します。
- `*.example.com` は `api.example.com` などのサブドメインに一致しますが、
`example.com` には一致しません。
- `**.example.com` はルートドメインとサブドメインの両方に一致します。
- グローバルな `*` の許可ルールは、拒否されていないすべての公開ホストに一致します。`*` は
  広範なネットワークアクセスを許可する設定として扱い、可能な限り対象を限定したルールを使用してください。
- `deny` は常に `allow` より優先され、グローバルな `*` を使用できるのは許可ルールのみです。

#### ローカルおよびプライベートの接続先

デフォルトでは、`allow_local_binding = false` によってループバック、リンクローカル、
プライベートネットワークの接続先がブロックされます。

- 個別の例外：コマンドが 1 つのローカル接続先を必要とする場合は、
  完全一致するローカル IP リテラルまたは `localhost` の許可ルールを追加します。
- 広範なアクセス：ローカルネットワークやプライベートネットワークへのアクセス範囲を
  意図的に広げたい場合にのみ、`allow_local_binding = true` を設定してください。
- ワイルドカード：ワイルドカードルールは、明示的なローカルの例外とは見なされません。
- 解決先アドレス：ローカルまたはプライベートの IP アドレスに解決されるホスト名は、許可リストに一致していてもブロックされたままです。

#### DNS リバインディング対策

ホスト名を許可する前に、Codex はベストエフォートで DNS と IP アドレスの分類を確認します。

- 名前解決が失敗またはタイムアウトした場合は、アクセスがブロックされます。
- 非公開アドレスに解決されるホスト名はブロックされます。
- このチェックによって DNS リバインディングのリスクは軽減されますが、完全には排除できません。リバインディングを完全に防ぐには、名前解決した IP アドレスをトランスポート層まで一貫して固定する必要があります。

悪意のある DNS が想定する脅威に含まれる場合は、より下位のレイヤーでも外向きの通信を制御してください。

#### 危険な設定

次の 2 つの設定は、意図的に信頼境界を広げます。

- `dangerously_allow_non_loopback_proxy = true` を設定すると、
  プロキシリスナーがループバック以外にも公開される可能性があります。
- `dangerously_allow_all_unix_sockets = true` は Unix ソケットの許可リストを迂回します。

これらは厳密に管理された環境でのみ使用してください。Unix ソケットのプロキシ機能が有効な場合、ループバック以外へのバインドを要求しても、リスナーはループバックに限定されます。そのため、サンドボックス内のネットワーク通信が、リモートからローカルのデーモンへ接続するための中継経路になることはありません。

`network_proxy` はデフォルトでオフです。有効にすると、次のように動作します：

| 設定                                | デフォルト | 動作                                                                                                                                                                              |
| -------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enabled`                              | `false` | コマンドのネットワークアクセスがすでにオンになっている場合にのみ、サンドボックス内のネットワーク通信を開始します。                                                                                                           |
| `domains`                              | 未設定   | 許可リスト方式で動作するため、`allow` ルールを追加するまで外部の接続先は許可されません。ホストの完全一致、範囲を限定したワイルドカード、すべてを対象とする `*` の許可ルールに対応しています。`deny` が常に優先されます。 |
| `unix_sockets`                         | 未設定   | 明示的な `allow` ルールを追加するまで、Unix ソケットの接続先は許可されません。                                                                                                         |
| `allow_local_binding`                  | `false` | ローカル IP アドレスのリテラルを完全一致で指定する許可ルール、または `localhost` の許可ルールを追加するか、ローカルやプライベートネットワークへのより広範なアクセスを明示的に有効にしない限り、それらの接続先をブロックします。                |
| `enable_socks5`                        | `true`  | ポリシーで許可されている場合に、SOCKS5 を利用可能にします。                                                                                                                                         |
| `enable_socks5_udp`                    | `true`  | SOCKS5 が利用可能な場合は、SOCKS5 経由の UDP を許可します。                                                                                                                                      |
| `allow_upstream_proxy`                 | `true`  | 環境で設定された上流プロキシを、サンドボックス内のネットワーク通信で使用できるようにします。                                                                                                               |
| `dangerously_allow_non_loopback_proxy` | `false` | 意図的に localhost の外部へ公開しない限り、リスナーのエンドポイントをループバックに限定します。                                                                                            |
| `dangerously_allow_all_unix_sockets`   | `false` | 意図的に保護を迂回しない限り、Unix ソケットへのアクセスを許可リストに基づいて制御します。                                                                                              |

### コマンド用ネットワークプロキシの対象外となる通信

ネットワークプロキシがフィルタリングするのは、ローカルのコマンドサンドボックス内で実行されるスクリプト、プログラム、子プロセスです。ウェブ検索、アプリやコネクタのツール呼び出し、MCP サーバーへの接続、ブラウザやコンピューターの使用による操作、Codex Cloud のタスク、クライアントによるモデルや認証のリクエストはフィルタリングされません。これらには、別個のサービス接続、機能設定、ワークスペースポリシー、または環境制御が使用されます。

ブラウザツールは、オリジンにアクセスする前に、
管理対象のネットワーク拒否ルールと、指定した接続先のみを許可するリストを個別に確認します。ブラウザのオリジンポリシーでは、サイトへのアクセス、
アップロード、ダウンロード、開発者ツールをさらに制限できます。詳しくは、
[管理対象のブラウザ制御](/ja-JP/codex/enterprise/managed-configuration#control-browser-and-computer-use)を参照してください。

管理対象ユーザーについては、コマンドのネットワークポリシーと、
`allowed_web_search_modes`、承認済みの `mcp_servers`、
アプリ、プラグイン、ブラウザ、コンピューターの使用に関する機能要件などの制御を組み合わせてください。詳しくは、
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)を参照してください。

起動したコマンドにネットワークへの完全なアクセスを許可しなくても、[ウェブ検索ツール](https://platform.openai.com/docs/guides/tools-web-search)を制御できます。Codex はデフォルトで、ウェブ検索キャッシュを使用して結果にアクセスします。このキャッシュは OpenAI が管理するウェブ検索結果のインデックスであるため、キャッシュモードではライブページを取得せず、事前にインデックス化された結果が返されます。これにより、任意のライブコンテンツによるプロンプトインジェクションにさらされるリスクは減りますが、ウェブ検索結果は引き続き信頼できないものとして扱ってください。`--yolo` または別の[フルアクセスのサンドボックス設定](#common-sandbox-and-approval-combinations)を使用している場合、ウェブ検索はデフォルトでライブ検索結果を返します。ライブブラウジングを許可するには `--search` を使用するか `web_search = "live"` を設定し、ツールをオフにするには `"disabled"` を設定します：

```toml
web_search = "cached"  # default
# web_search = "disabled"
# web_search = "live"  # same as --search

外部ウェブアクセスを検索インデックス経由に限定する場合は、`web_search = "indexed"` を設定します。
Codex でネットワークアクセスやウェブ検索を有効にする際は注意してください。
プロンプトインジェクションにより、エージェントが信頼できない指示を取得して従う可能性があります。

## デフォルト設定と推奨事項

- Codex は起動時にフォルダーがバージョン管理されているかを検出し、次の設定を推奨します：
  - バージョン管理下のフォルダー：`Auto`（ワークスペースへの書き込み + リクエスト時の承認）
  - バージョン管理下にないフォルダー：`read-only`
- 設定によっては、作業ディレクトリを明示的に信頼するまで、Codex が `read-only` で起動する場合もあります。信頼の設定は、オンボーディングプロンプトや `/permissions` などから行えます。
- ワークスペースには、現在のディレクトリと `/tmp` などの一時ディレクトリが含まれます。ワークスペースに含まれるディレクトリを確認するには、`/status` コマンドを使用します。
- デフォルト設定を使用するには、`codex` を実行します。
- これらを明示的に設定することもできます：
  - `codex --sandbox workspace-write --ask-for-approval on-request`
  - `codex --sandbox read-only --ask-for-approval on-request`

### 書き込み可能なルート内の保護されたパス

デフォルトの `workspace-write` サンドボックスポリシーでは、書き込み可能なルート内にも保護されたパスがあります：

- `<writable_root>/.git` は、ディレクトリかファイルかにかかわらず、読み取り専用として保護されます。
- `<writable_root>/.git` がポインターファイル（`gitdir: ...`）の場合、解決された Git ディレクトリのパスも読み取り専用として保護されます。
- `<writable_root>/.agents` がディレクトリとして存在する場合は、読み取り専用として保護されます。
- `<writable_root>/.codex` がディレクトリとして存在する場合は、読み取り専用として保護されます。
- 保護は再帰的に適用されるため、これらのパス配下はすべて読み取り専用になります。

### 承認プロンプトなしでの実行

`--ask-for-approval never` または短縮形式の `-a never` を使用すると、承認プロンプトを無効にできます。

このオプションはすべての `--sandbox` モードで使用できるため、Codex の自律性のレベルは引き続き制御できます。Codex は設定された制約の範囲内で可能な限り対応します。

Codex に、承認プロンプトなしでファイルを読み取り、編集し、ネットワークアクセスが可能な状態でコマンドを実行させる必要がある場合は、`--sandbox danger-full-access`（または `--dangerously-bypass-approvals-and-sandbox` フラグ）を使用します。使用する前に十分注意してください。

中間的な設定として、`approval_policy = { granular = { ... } }` を使用すると、特定のカテゴリの承認プロンプトは対話形式のまま維持し、それ以外は自動的に拒否できます。きめ細かなポリシーの対象には、サンドボックスの承認、execpolicy-rule のプロンプト、MCP プロンプト、`request_permissions` プロンプト、スキルスクリプトの承認が含まれます。

### 承認リクエストの自動レビュー

デフォルトでは、承認リクエストはユーザーに送られます：

```toml
approvals_reviewer = "user"

承認リクエストの自動レビューは、
`approval_policy = "on-request"` やきめ細かな承認ポリシーなど、承認が対話形式で行われる場合に適用されます。
`approvals_reviewer = "auto_review"` を設定すると、対象となる承認リクエストが、
Codex による実行前にレビュー担当エージェントへ送られます：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"

レビュー担当エージェントのライフサイクル全体、トリガー条件、設定の優先順位、
失敗時の動作については、
[自動レビュー](/ja-JP/codex/sandboxing/auto-review)を参照してください。

レビュー担当エージェントが評価するのは、サンドボックス権限の昇格、
ブロックされたネットワークリクエスト、`request_permissions` プロンプト、
副作用を伴うアプリや MCP のツール呼び出しなど、すでに承認が必要な操作だけです。サンドボックス内で完結する操作は、
追加のレビューなしで続行されます。

レビューポリシーでは、データ流出、認証情報の探索、持続的なセキュリティの弱体化、破壊的な操作をチェックします。低リスクおよび中リスクの操作は、ポリシーで許可されていれば続行できます。重大リスクの操作はポリシーによって拒否されます。高リスクの操作には、ユーザーからの十分な認可があり、該当する拒否ルールがないことが必要です。プロンプトの構築、レビューセッション、解析のいずれかが失敗した場合は、安全側に倒して操作を実行しません。タイムアウトは別途通知されますが、その場合も操作は実行されません。

[デフォルトのレビューポリシー](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)は、
オープンソースの Codex リポジトリにあります。企業は、
管理対象要件の `guardian_policy_config` を使用して、テナント固有のセクションを置き換えられます。
ローカルの `[auto_review].policy` に指定したテキストも使用できますが、
管理対象要件が優先されます。設定の詳細については、
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration#configure-automatic-review-policy)を参照してください。

ChatGPT デスクトップアプリでは、これらのレビューは「レビュー中」「承認済み」「拒否」「中止」「タイムアウト」などのステータスを持つ自動レビュー項目として表示されます。また、レビュー対象のリクエストに関するリスクレベルとユーザー認可の評価が含まれる場合もあります。

自動レビューではモデルが追加で呼び出されるため、Codex の使用量が増える可能性があります。
管理者は `allowed_approvals_reviewers` を使用して自動レビューを制限できます。

### サンドボックスと承認の一般的な組み合わせ

| 目的                                                            | フラグ / 設定                                                                                                                      | 効果                                                                                                                                           |
| ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 自動（プリセット）                                                     | _フラグは不要_ 、または `--sandbox workspace-write --ask-for-approval on-request`                                                      | Codex はワークスペース内でファイルを読み取り、編集し、コマンドを実行できます。ワークスペース外での編集やネットワークアクセスには承認が必要です。 |
| 安全な読み取り専用の閲覧                                           | `--sandbox read-only --ask-for-approval on-request`                                                                                 | Codex はファイルを読み取り、質問に回答できます。編集、コマンドの実行、ネットワークアクセスには承認が必要です。                               |
| 読み取り専用の非対話型実行（CI）                                    | `--sandbox read-only --ask-for-approval never`                                                                                      | Codex はファイルの読み取りのみ行え、承認を求めることはありません。                                                                                              |
| 編集は自動で行い、信頼できないコマンドの実行時には承認を要求 | `--sandbox workspace-write --ask-for-approval untrusted`                                                                            | Codex はファイルを読み取って編集できますが、信頼できないコマンドを実行する前には承認を求めます。                                                           |
| 自動レビューモード                                                  | `--sandbox workspace-write --ask-for-approval on-request -c approvals_reviewer=auto_review` または `approvals_reviewer = "auto_review"` | サンドボックスの境界は標準の on-request モードと同じですが、対象の承認リクエストはユーザーに表示されず、自動レビューで審査されます。  |
| 危険なフルアクセス                                             | `--dangerously-bypass-approvals-and-sandbox`（エイリアス：`--yolo`）                                                                      |  サンドボックスなし、承認なし _（非推奨）_                                                                               |

非対話型の実行には `codex exec --sandbox workspace-write` を使用してください。従来の `codex exec --full-auto` による呼び出しも互換性のために残されていますが、非推奨となっており、警告が表示されます。

`--ask-for-approval untrusted` を指定すると、Codex は安全性が確認されている読み取り操作のみを自動実行します。状態を変更したり、外部での実行を引き起こしたりする可能性のあるコマンド（破壊的な Git 操作や、Git の出力・設定の上書きに関するフラグなど）には承認が必要です。

#### `config.toml` での構成

構成全般のワークフローについては、[設定の基本](/ja-JP/codex/config-file/config-basic)、[高度な設定](/ja-JP/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)、[構成リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

```toml
# Always ask for approval mode
approval_policy = "untrusted"
sandbox_mode    = "read-only"
allow_login_shell = false # optional hardening: disallow login shells for shell-based tools

# Optional: Allow network in workspace-write mode
[sandbox_workspace_write]
network_access = true

# Optional: granular approval policy
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

プリセットを[プロファイルファイル](/ja-JP/codex/config-file/config-advanced#profiles)として保存し、`codex --profile profile-name` で選択することもできます：

```toml
# ~/.codex/full_auto.config.toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

```toml
# ~/.codex/readonly_quiet.config.toml
approval_policy = "never"
sandbox_mode    = "read-only"

### ローカルでのサンドボックスのテスト

Codex のサンドボックス内でコマンドを実行したときの動作を確認するには、次の Codex CLI コマンドを使用します：

```bash
# macOS
codex sandbox macos [--permissions-profile <name>] [--log-denials] [COMMAND]...
# Linux
codex sandbox linux [--permissions-profile <name>] [COMMAND]...
# Windows
codex sandbox windows [--permissions-profile <name>] [COMMAND]...

`sandbox` コマンドは `codex debug` としても使用できます。プラットフォーム別のヘルパーにも、`codex sandbox seatbelt` や `codex sandbox landlock` などのエイリアスがあります。

## OS レベルのサンドボックス

Codex では、OS に応じて異なる方法でサンドボックスを適用します：

- **macOS** では Seatbelt ポリシーを使用し、選択した `--sandbox` モードに対応するプロファイル（`-p`）を指定して `sandbox-exec` でコマンドを実行します。読み取りアクセスを制限する設定でプラットフォームのデフォルト設定が有効になっている場合、Codex は `/System` へのアクセスを広く許可するのではなく、精査された macOS プラットフォームポリシーを追加して、一般的なツールとの互換性を維持します。
- **Linux** では、デフォルトで `bwrap` と `seccomp` を組み合わせて使用します。
- **Windows** では、[Windows Subsystem for Linux 2（WSL2）](/ja-JP/codex/windows/wsl)で実行する場合に Linux サンドボックスの実装を使用します。WSL1 は Codex `0.114` までサポートされていましたが、`0.115` 以降は Linux サンドボックスが `bwrap` に移行したため、サポートされなくなりました。Windows でネイティブに実行する場合、Codex は [Windows サンドボックス](/ja-JP/codex/windows/windows-sandbox#windows-sandbox)の実装を使用します。

Windows で使用する Codex IDE 拡張機能は、WSL2 を直接サポートしています。WSL2 が利用可能な場合にエージェントを常に WSL2 内で実行するには、VS Code で次のように設定します：

```json
{
  "chatgpt.runCodexInWindowsSubsystemForLinux": true
}

これにより、ホスト OS が Windows であっても、IDE 拡張機能では、コマンド、承認、ファイルシステムへのアクセスに Linux サンドボックスの動作仕様が適用されます。詳しくは [WSL ガイド](/ja-JP/codex/windows/wsl)を参照してください。

Windows でネイティブに実行する場合は、`config.toml` でネイティブサンドボックスモードを設定します：

```toml
[windows]
sandbox = "unelevated" # or "elevated"
# sandbox_private_desktop = true  # default; set false only for compatibility

詳しくは、[Windows セットアップガイド](/ja-JP/codex/windows/windows-sandbox#windows-sandbox)を参照してください。

Docker などのコンテナー環境で Linux を実行する場合、ホストまたはコンテナーの構成によって、Codex に必要な名前空間、setuid `bwrap`、`seccomp` の操作がブロックされていると、サンドボックスが動作しないことがあります。

その場合は、必要な分離を実現するように Docker コンテナーを構成し、コンテナー内で `codex` に `--sandbox danger-full-access`（または `--dangerously-bypass-approvals-and-sandbox` フラグ）を指定して実行します。

### Dev Containers での Codex の実行

ホストで Linux サンドボックスを直接実行できない場合や、組織ですでにコンテナーを使った開発が標準化されている場合は、Dev Containers で Codex を実行し、Docker を外側の分離境界として使用します。この方法は、Visual Studio Code Dev Containers と互換ツールで利用できます。

[Codex のセキュアな devcontainer サンプル](https://github.com/openai/codex/tree/main/.devcontainer)をリファレンス実装として使用してください。このサンプルでは、Codex、一般的な開発ツール、`bubblewrap`、ファイアウォールによるアウトバウンド制御を導入します。

  開発コンテナーには高い保護効果がありますが、
  すべての攻撃を防げるわけではありません。コンテナー内で `--sandbox danger-full-access` または
`--dangerously-bypass-approvals-and-sandbox` を指定して Codex を実行すると、
  悪意のあるプロジェクトによって、Codex の認証情報を含め、
  開発コンテナー内で利用できるあらゆる情報が外部に流出するおそれがあります。この方法は信頼できるリポジトリでのみ使用し、
  ほかの高権限環境と同様に Codex の動作を監視してください。

リファレンス実装には次のものが含まれます：

- Codex と一般的な開発ツールがインストールされた Ubuntu 24.04 ベースイメージ
- アウトバウンドアクセス用の許可リストベースのファイアウォールプロファイル
- ワークスペースをコンテナー内で開き直すための VS Code 設定と推奨拡張機能
- コマンド履歴と Codex の構成を保持するための永続マウント
- コンテナーで必要なケーパビリティが付与されている場合に、Codex が引き続き Linux サンドボックスを使用できるようにする `bubblewrap`

次の手順で試せます：

1. Visual Studio Code と [Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)をインストールします。
2. Codex のサンプルに含まれる `.devcontainer` の設定をリポジトリにコピーするか、Codex リポジトリから直接始めます。
3. VS Code で **Dev Containers: Open Folder in Container...** を実行し、`.devcontainer/devcontainer.secure.json` を選択します。
4. コンテナーが起動したら、ターミナルを開いて `codex` を実行します。

CLI からコンテナーを起動することもできます：

```bash
devcontainer up --workspace-folder . --config .devcontainer/devcontainer.secure.json

このサンプルは主に次の 3 つの要素で構成されます：

- `.devcontainer/devcontainer.secure.json` は、コンテナーの設定、ケーパビリティ、マウント、環境変数、VS Code 拡張機能を制御します。
- `.devcontainer/Dockerfile.secure` は、Ubuntu ベースのイメージとインストールするツールを定義します。
- `.devcontainer/init-firewall.sh` は、アウトバウンドネットワークポリシーを適用します。

リファレンスのファイアウォールは、あくまで出発点として用意されています。分離をドメインの許可リストに依存する場合は、TTL を考慮した更新や DNS 対応ファイアウォールなど、環境に適した DNS リバインディング対策と DNS 更新時の保護策を実装してください。

コンテナー内では、次のいずれかのモードを選択します：

- Dev Container プロファイルで、`bwrap` が内部サンドボックスを作成するために必要なケーパビリティが付与されている場合は、Codex の Linux サンドボックスを有効なままにします。
- コンテナーをセキュリティ境界とする場合は、Codex が 2 層目のサンドボックスを作成しようとしないように、コンテナー内で `--sandbox danger-full-access` を指定して Codex を実行します。

## バージョン管理

Codex は、バージョン管理を取り入れたワークフローで最も効果的に機能します：

- 機能ブランチで作業し、Codex に委任する前に `git status` をクリーンな状態に保ってください。これにより、Codex のパッチを切り分けたり元に戻したりしやすくなります。
- 追跡対象のファイルを直接編集するよりも、パッチベースのワークフロー（`git diff`/`git apply` など）を優先してください。小さな単位でロールバックできるように、こまめにコミットしてください。
- Codex の提案もほかの PR と同様に扱ってください。対象を絞った検証を行い、差分をレビューして、監査に備えてコミットメッセージに判断内容を記録します。

## 監視とテレメトリ

Codex は、OpenTelemetry（OTel）によるオプトインの監視をサポートしています。これにより、ローカル環境のデフォルトのセキュリティ設定を弱めることなく、チームが利用状況を監査し、問題を調査し、コンプライアンス要件を満たせます。テレメトリはデフォルトで無効になっているため、設定で明示的に有効にしてください。

### 概要

- ローカルでの実行をその環境内で完結させるため、Codex では OTel のエクスポートがデフォルトで無効になっています。
- 有効にすると、Codex は、チャット、API リクエスト、SSE/WebSocket ストリームのアクティビティ、ユーザープロンプト（デフォルトでは伏せ字）、ツールの承認判断、ツールの結果を含む構造化ログイベントを出力します。
- Codex は、開発・ステージング・本番環境のトラフィックを区別するため、エクスポートするイベントに `service.name`（生成元）、CLI のバージョン、環境ラベルを付与します。

### OTel の有効化（オプトイン）

Codex の構成（通常は `~/.codex/config.toml`）に `[otel]` ブロックを追加し、エクスポーターを選択して、プロンプトのテキストをログに記録するかどうかを指定します。

```toml
[otel]
environment = "staging"   # dev | staging | prod
exporter = "none"          # none | otlp-http | otlp-grpc
log_user_prompt = false     # redact prompt text unless policy allows

- `exporter = "none"` を設定すると、計測機能は有効なままですが、データはどこにも送信されません。
- イベントを独自のコレクターに送信するには、次のいずれかを選択します：

```toml
[otel]
exporter = { otlp-http = {
  endpoint = "https://otel.example.com/v1/logs",
  protocol = "binary",
  headers = { "x-otlp-api-key" = "${OTLP_TOKEN}" }
}}

```toml
[otel]
exporter = { otlp-grpc = {
  endpoint = "https://otel.example.com:4317",
  headers = { "x-otlp-meta" = "abc123" }
}}

Codex はイベントをバッチにまとめ、終了時にフラッシュします。エクスポートするのは、Codex の OTel モジュールが生成したテレメトリのみです。

### イベントのカテゴリ

代表的なイベントの種類は次のとおりです。

- `codex.conversation_starts`（モデル、推論設定、サンドボックス／承認ポリシー）
- `codex.api_request`（試行、ステータス／成否、所要時間、エラーの詳細）
- `codex.sse_event`（ストリームイベントの種類、成功／失敗、所要時間、および `response.completed` のトークン数）
- `codex.websocket_request` と `codex.websocket_event`（リクエストの所要時間、およびメッセージごとの種類／成否／エラー）
- `codex.user_prompt`（長さ。内容の記録を明示的に有効にしない限り、内容はマスキング）
- `codex.tool_decision`（承認／拒否、判断元：構成またはユーザー）
- `codex.tool_result`（所要時間、成否、出力の抜粋）

関連する OTel メトリクス（カウンターと所要時間のヒストグラムのペア）には、`codex.api_request`、`codex.sse_event`、`codex.websocket.request`、`codex.websocket.event`、`codex.tool.call` があり、それぞれに対応する `.duration_ms` インストゥルメントが含まれます。

イベントの完全な一覧と構成リファレンスについては、[GitHub の Codex 構成ドキュメント](https://github.com/openai/codex/blob/main/docs/config.md#otel)を参照してください。

### セキュリティとプライバシーのガイダンス

- ポリシーでプロンプト内容の保存が明示的に許可されていない限り、`log_user_prompt = false` を維持してください。プロンプトにはソースコードや機密データが含まれる可能性があります。
- テレメトリの送信先は自ら管理するコレクターに限定し、コンプライアンス要件に沿った保持制限とアクセス制御を適用してください。
- ツールの引数と出力は機密情報として扱ってください。可能な場合は、コレクターまたは SIEM でのマスキングを優先してください。
- Codex にセッションの記録を `CODEX_HOME` 配下に保存させたくない場合は、ローカルデータの保持設定（`history.persistence` / `history.max_bytes` など）を確認してください。[高度な設定](/ja-JP/codex/config-file/config-advanced#history-persistence)と[構成リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。
- ネットワークアクセスを無効にした状態で CLI を実行すると、OTel のエクスポートデータはコレクターに到達しません。エクスポートするには、`workspace-write` モードで OTel エンドポイントへのネットワークアクセスを許可するか、コレクターのドメインを許可リストに登録したうえで Codex Cloud からエクスポートしてください。
- 承認やサンドボックスの変更、予期しないツール実行がないか、イベントを定期的に確認してください。

OTel は任意で利用する機能であり、前述のサンドボックスと承認による保護を置き換えるものではなく、補完することを目的としています。

## 管理対象の設定

エンタープライズ管理者は、[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)でワークスペースの Codex セキュリティ設定を構成できます。セットアップとポリシーの詳細については、リンク先のページを参照してください。
