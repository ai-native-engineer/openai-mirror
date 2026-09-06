<!-- source: https://learn.chatgpt.com/ja-JP/docs/config-file/config-advanced -->

プロバイダー、ポリシー、連携をより細かく制御する必要がある場合は、これらのオプションを使用します。すぐに始めるには、[設定の基本](/ja-JP/codex/config-file/config-basic)を参照してください。

プロジェクトのガイダンス、再利用可能な機能、カスタムスラッシュコマンド、サブエージェントのワークフロー、連携について詳しくは、[カスタマイズ](/ja-JP/codex/customization/overview)を参照してください。設定キーについては、[設定リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

## プロファイル

プロファイルを使うと、名前付きの設定レイヤーを保存し、
CLI から切り替えられます。`--profile profile-name` を指定すると、Codex は
`~/.codex/config.toml` を読み込み、その上に `~/.codex/profile-name.config.toml` を適用します。
プロファイル名には、英字、数字、ハイフン、アンダースコアを使用できます。

プロファイルごとに個別の TOML ファイルを作成します。
プロファイルファイルではトップレベルの設定キーを使用し、`[profiles.profile-name]` の下にネストしないでください。

```toml
# ~/.codex/deep-review.config.toml
model = "gpt-5.5"
model_reasoning_effort = "xhigh"
approval_policy = "on-request"
model_catalog_json = "/Users/me/.codex/model-catalogs/deep-review.json"

```shell
codex --profile deep-review
codex exec --profile deep-review "review this change"

プロファイルファイルは、ユーザーの基本設定より上位で、
プロジェクト設定や CLI 設定より下位のレイヤーにあるため、
基本設定と異なる値だけを指定すれば十分です。プロファイルファイルでは `model_catalog_json` もオーバーライドでき、
両方のファイルに設定されている場合は、Codex がプロファイル側の値を使用します。

Codex 0.134.0 以降では、`--profile` は `[profiles.profile-name]` を
`config.toml` から読み込まなくなり、トップレベルの `profile = "profile-name"` セレクターも
サポートされなくなりました。従来のプロファイル設定を
`~/.codex/profile-name.config.toml` に移行してから、対応する
`[profiles.profile-name]` テーブルと `profile = "profile-name"` セレクターを
`config.toml` から削除してください。

## CLI からの 1 回限りのオーバーライド

`~/.codex/config.toml` を編集する方法のほか、CLI から 1 回の実行に限って設定をオーバーライドすることもできます：

- 専用フラグがある場合は、そちらを優先してください（例：`--model`）。
- 任意のキーをオーバーライドする必要がある場合は、`-c` / `--config` を使用します。

例：

```shell
# Dedicated flag
codex --model gpt-5.6-terra

# Generic key/value override (value is TOML, not JSON)
codex --config model='"gpt-5.6-terra"'
codex --config sandbox_workspace_write.network_access=true
codex --config 'shell_environment_policy.include_only=["PATH","HOME"]'

注意事項：

- キーではドット記法を使用してネストされた値を設定できます（例：`mcp_servers.context7.enabled=false`）。
- `--config` の値は TOML として解析されます。迷った場合は、シェルが値を空白で分割しないように、値を引用符で囲んでください。
- 値を TOML として解析できない場合、Codex は文字列として扱います。

## 設定と状態の保存場所

Codex はローカルの状態を `CODEX_HOME` 配下に保存します（デフォルトは `~/.codex`）。

一般的なファイルは次のとおりです：

- `config.toml`（ローカル設定）
- `auth.json`（ファイルベースで認証情報を保存する場合）、または OS のキーチェーン／キーリング
- `history.jsonl`（履歴の永続化が有効な場合）
- ログやキャッシュなど、その他のユーザーごとの状態

認証情報の保存モードを含む認証の詳細については、[認証](/ja-JP/codex/auth)を参照してください。設定キーの一覧については、[設定リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

リポジトリにチェックインするかシステムパスに配置する、共有のデフォルト設定、ルール、スキルについては、[チーム設定](/ja-JP/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config)を参照してください。

組み込みの OpenAI プロバイダーを LLM プロキシ、ルーター、またはデータレジデンシーが有効なプロジェクトに接続するだけなら、新しいプロバイダーを定義する代わりに、`openai_base_url` を `config.toml` 内で設定します。これにより、組み込みの `openai` プロバイダーのベース URL を変更でき、別途 `model_providers.<id>` エントリを作成する必要はありません。

```toml
openai_base_url = "https://us.api.openai.com/v1"

## プロジェクト設定ファイル（`.codex/config.toml`）

ユーザー設定に加えて、Codex はリポジトリ内の `.codex/config.toml` ファイルから、プロジェクト単位のオーバーライドを読み込みます。Codex はプロジェクトルートから現在の作業ディレクトリまでたどり、見つかったすべての `.codex/config.toml` を読み込みます。複数のファイルで同じキーが定義されている場合は、作業ディレクトリに最も近いファイルが優先されます。

セキュリティ上、Codex がプロジェクト単位の設定ファイルを読み込むのは、プロジェクトが信頼されている場合に限られます。プロジェクトが信頼されていない場合、Codex はプロジェクトの `.codex/` レイヤーを無視します。これには `.codex/config.toml`、プロジェクトローカルのフック、プロジェクトローカルのルールが含まれます。ユーザー用とシステム用のレイヤーは別に扱われ、引き続き読み込まれます。

プロジェクト設定内の相対パス（例：`model_instructions_file`）は、`config.toml` を含む `.codex/` フォルダーを基準に解決されます。

プロジェクト設定ファイルでは、認証情報のリダイレクト、
ホストが管理するアプリリクエストのメタデータ変更、プロバイダー認証の変更、設定プロファイルの選択、
マシン上での通知／テレメトリコマンドの実行に関する設定をオーバーライドできません。
Codex は、プロジェクトローカルの `.codex/config.toml` に次のキーがある場合はそれらを無視し、
起動時に警告を表示します：`openai_base_url`、`chatgpt_base_url`、
`apps_mcp_product_sku`、`model_provider`、`model_providers`、`notify`、
`profile`、`profiles`、`experimental_realtime_ws_base_url`、`otel`。プロバイダー、通知、
テレメトリのキーは、ユーザーレベルの
`~/.codex/config.toml` に設定してください。設定プロファイルは `--profile profile-name`
と `~/.codex/profile-name.config.toml` を使用して選択します。

## フック

Codex は、アクティブな設定レイヤーと同じ場所にある `hooks.json` ファイル、またはインラインの
`[hooks]` テーブルを含む `config.toml` ファイルからも、ライフサイクルフックを読み込めます。

実際には、次の 4 か所が特に便利です：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

プロジェクトローカルのフックは、プロジェクトの `.codex/` レイヤーが信頼されている場合にのみ読み込まれます。
ユーザーレベルのフックは、プロジェクトの信頼状態とは無関係です。

インライン TOML フックは、`hooks.json` と同じイベント構造を使用します：

```toml
[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

同じレイヤーに `hooks.json` とインライン `[hooks]` の両方が含まれる場合、Codex は
両方を読み込み、警告を表示します。レイヤーごとにどちらか一方の形式を使用してください。

現在のイベント一覧、入力フィールド、出力時の動作、制限事項については、
[フック](/ja-JP/codex/hooks)を参照してください。

## エージェントのロール（`config.toml` 内の `[agents]`）

サブエージェントのロール設定（`config.toml` 内の `[agents]`）については、[サブエージェント](/ja-JP/codex/agent-configuration/subagents)を参照してください。

## プロジェクトルートの検出

Codex は、作業ディレクトリからプロジェクトルートまで上位ディレクトリをたどり、プロジェクト設定（`.codex/` レイヤーや `AGENTS.md` など）を検出します。

デフォルトでは、Codex は `.git` を含むディレクトリをプロジェクトルートとして扱います。この動作をカスタマイズするには、`config.toml` で `project_root_markers` を設定します：

```toml
# Treat a directory as the project root when it contains any of these markers.
project_root_markers = [".git", ".hg", ".sl"]

`project_root_markers = []` を設定すると、親ディレクトリの検索を省略し、現在の作業ディレクトリをプロジェクトルートとして扱います。

## カスタムモデルプロバイダー

モデルプロバイダーは、Codex がモデルに接続する方法（ベース URL、通信 API、認証、任意の HTTP ヘッダー）を定義します。カスタムプロバイダーでは、予約済みの組み込みプロバイダー ID である `openai`、`ollama`、`lmstudio` を再利用できません。

追加のプロバイダーを定義し、`model_provider` でそれらを指定します：

```toml
model = "gpt-5.6-terra"
model_provider = "proxy"

[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "http://proxy.example.com"
env_key = "OPENAI_API_KEY"

[model_providers.local_ollama]
name = "Ollama"
base_url = "http://localhost:11434/v1"

[model_providers.mistral]
name = "Mistral"
base_url = "https://api.mistral.ai/v1"
env_key = "MISTRAL_API_KEY"

カスタムプロバイダーがスタンドアロンのウェブ検索エンドポイントに対応している場合は、
プロバイダーの設定でその機能を宣言します：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
env_key = "OPENAI_API_KEY"
supports_standalone_web_search = true

カスタムプロバイダーでは、この設定のデフォルト値は `false` です。
スタンドアロンのウェブ検索は開発中で、デフォルトでは無効です。プロバイダーの機能を `true` に設定しても有効にはなりません。
プロバイダーが互換性のあるエンドポイントに対応し、
選択したモデルとランタイムもスタンドアロン検索に対応している必要があります。
設定済みの [`web_search` モード](/ja-JP/codex/web-search)と管理対象の検索制限も、
引き続き適用されます。

必要に応じてリクエストヘッダーを追加します：

```toml
[model_providers.example]
http_headers = { "X-Example-Header" = "example-value" }
env_http_headers = { "X-Example-Features" = "EXAMPLE_FEATURES" }

プロバイダーで、Codex が外部の認証情報ヘルパーからベアラートークンを取得する必要がある場合は、コマンドベースの認証を使用します：

```toml
[model_providers.proxy]
name = "OpenAI using LLM proxy"
base_url = "https://proxy.example.com/v1"
wire_api = "responses"

[model_providers.proxy.auth]
command = "/usr/local/bin/fetch-codex-token"
args = ["--audience", "codex"]
timeout_ms = 5000
refresh_interval_ms = 300000

認証コマンドは `stdin` を受け取らず、トークンを stdout に出力する必要があります。Codex は前後の空白を削除し、空のトークンをエラーとして扱い、`refresh_interval_ms` で指定した間隔で事前に更新します。認証を再試行した後にのみ更新するには、`refresh_interval_ms = 0` を設定します。`[model_providers.<id>.auth]` を `env_key`、`experimental_bearer_token`、`requires_openai_auth` と併用しないでください。

### Amazon Bedrock プロバイダー

Codex には `amazon-bedrock` モデルプロバイダーが組み込まれています。
これを `model_provider` に直接設定します。カスタムプロバイダーとは異なり、この組み込みプロバイダーでサポートされるのは、
ネストされた AWS プロファイルとリージョンのオーバーライドのみです。

```toml
model_provider = "amazon-bedrock"
model = "<bedrock-model-id>"

[model_providers.amazon-bedrock.aws]
profile = "default"
region = "eu-central-1"

`profile` を省略すると、Codex は標準の AWS 認証情報チェーンを使用します。
`region` には、リクエストを処理するサポート対象の Bedrock リージョンを設定します。

セットアップの全手順、認証オプション、対応モデル、機能の提供状況については、
[Amazon Bedrock での ChatGPT Work と
Codex の利用](/ja-JP/codex/amazon-bedrock)を参照してください。

## OSS モード（ローカルプロバイダー）

Codex は、Ollama や LM Studio などのローカルの「オープンソース」プロバイダーを、
`--oss` の指定時に利用できます。1 回の実行で使用するプロバイダーは
`--local-provider` で選択するか、`oss_provider` をデフォルトとして設定します。どちらも設定されていない場合は、
対話型 CLI では選択を求められ、`codex exec` はエラーで終了します。

```toml
# Default local provider used with `--oss`
oss_provider = "ollama" # or "lmstudio"

## Azure プロバイダーとプロバイダーごとの調整

```toml
[model_providers.azure]
name = "Azure"
base_url = "https://YOUR_PROJECT_NAME.openai.azure.com/openai"
env_key = "AZURE_OPENAI_API_KEY"
query_params = { api-version = "2025-04-01-preview" }
wire_api = "responses"
request_max_retries = 4
stream_max_retries = 10
stream_idle_timeout_ms = 300000

組み込みの OpenAI プロバイダーのベース URL を変更するには、`openai_base_url` を使用してください。組み込みプロバイダー ID はオーバーライドできないため、`[model_providers.openai]` は作成しないでください。

## データレジデンシーを利用する API 組織

[データレジデンシー](https://help.openai.com/en/articles/9903489-data-residency-and-inference-residency-for-chatgpt)を有効にして作成したプロジェクトでは、モデルプロバイダーを作成して、`base_url` が[正しいプレフィックス](/api/docs/guides/your-data#which-models-and-features-are-eligible-for-data-residency)を使用するように更新できます。データレジデンシーを利用する ChatGPT ワークスペースでは、カスタムプロバイダーは不要です。ChatGPT でサインインすると、Codex はワークスペースのレジデンシー設定に従います。

```toml
model_provider = "openaidr"
[model_providers.openaidr]
name = "OpenAI Data Residency"
base_url = "https://us.api.openai.com/v1" # Replace 'us' with domain prefix

## モデルの推論、詳細度、制限

```toml
model_reasoning_summary = "none"          # Disable summaries
model_verbosity = "low"                   # Shorten responses
model_supports_reasoning_summaries = true # Force reasoning
model_context_window = 128000             # Context window size

`model_verbosity` は Responses API を使用するプロバイダーにのみ適用されます。Chat Completions プロバイダーでは、この設定は無視されます。

## 承認ポリシーとサンドボックスモード

承認の厳格さ（Codex が一時停止するタイミングに影響）とサンドボックスレベル（ファイルおよびネットワークへのアクセスに影響）を選択します。

`config.toml` を編集する際に注意すべき運用上の詳細については、[一般的なサンドボックスと承認の組み合わせ](/ja-JP/codex/agent-approvals-security#common-sandbox-and-approval-combinations)、[書き込み可能なルート内の保護されたパス](/ja-JP/codex/agent-approvals-security#protected-paths-in-writable-roots)、[ネットワークアクセス](/ja-JP/codex/agent-approvals-security#network-access)を参照してください。

ファイルシステムとネットワークへのアクセスをまとめて構成するベータ版の権限プロファイルについては、[権限](/ja-JP/codex/permissions)を参照してください。

プロンプトのカテゴリごとに許可または自動拒否を設定できる、きめ細かな承認ポリシー（`approval_policy = { granular = { ... } }`）も使用できます。これは、一部のケースでは通常の対話型承認を行い、`request_permissions` やスキルスクリプトのプロンプトなど、その他のケースでは自動的に拒否して安全性を確保したい場合に便利です。

`approvals_reviewer = "auto_review"` を設定すると、対象となる対話型の承認リクエストが自動レビューに回されます。
変更されるのはレビュー担当者であり、
サンドボックスの境界は変わりません。

ローカルのレビューポリシーの指示には `[auto_review].policy` を使用します。
管理対象の `guardian_policy_config` が優先されます。

```toml
approval_policy = "untrusted"   # Other options: on-request, never, or { granular = { ... } }
approvals_reviewer = "user"     # Or "auto_review" for automatic review
sandbox_mode = "workspace-write"
allow_login_shell = false       # Optional hardening: disallow login shells for shell tools

# Example granular approval policy:
# approval_policy = { granular = {
#   sandbox_approval = true,
#   rules = true,
#   mcp_elicitations = true,
#   request_permissions = false,
#   skill_approval = false
# } }

[sandbox_workspace_write]
exclude_tmpdir_env_var = false  # Allow $TMPDIR
exclude_slash_tmp = false       # Allow /tmp
writable_roots = ["/Users/YOU/.pyenv/shims"]
network_access = false          # Opt in to outbound network

[auto_review]
policy = """
Use your organization's automatic review policy.
"""

### 名前付き権限プロファイル

組み込みプロファイル、カスタムプロファイルの構文、
ファイルシステムとネットワークの構成モデル全体については、[権限](/ja-JP/codex/permissions)を参照してください。

すべての設定キーと要件に関する制約については、
[設定リファレンス](/ja-JP/codex/config-file/config-reference)と
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)を参照してください。

  workspace-write モードでは、一部の環境で、ワークスペースの他の部分が書き込み可能でも、`.git/` と `.codex/` は読み取り専用に保たれます。
  そのため、
  `git commit` などのコマンドをサンドボックスの外で実行するには、
  引き続き承認が必要になる場合があります。Codex に特定のコマンドをスキップさせたい場合（たとえば、サンドボックス外で `git
  commit` をブロックする場合）は、
<a href="/codex/agent-configuration/rules">ルール</a>を使用してください。

サンドボックスを完全に無効にします（環境ですでにプロセスが分離されている場合にのみ使用してください）：

```toml
sandbox_mode = "danger-full-access"

## シェル環境ポリシー

`shell_environment_policy` は、Codex が起動するコマンドに渡す環境変数を制御します。
`inherit = "none"` を使用すると空の環境から開始でき、
`inherit = "core"` を使用すると絞り込んだ変数セットを継承できます。明示的な値とキー指定のフィルターを追加し、
起動するコマンドに不要なシークレットが渡されないようにします。

```toml
[shell_environment_policy]
inherit = "core"
set = { MY_FLAG = "1" }
ignore_default_excludes = false

[shell_environment_policy.filters]
"AWS_*" = "exclude"
"AZURE_*" = "exclude"

フィルターパターンでは大文字と小文字が区別されず、`*` と `?` を使用できます。`"exclude"` を使用すると、一致する変数を削除できます。
いずれかのパターンで `"include"` を使用すると、Codex は
include パターンに一致する変数だけを保持します。
include パターンでは、すでに除外された変数は復元されません。
フィルターキーは、大文字と小文字を区別せずに構成レイヤー間でマージされます。

`ignore_default_excludes` のデフォルトは `true` であるため、Codex は
`KEY`、`SECRET`、または `TOKEN` を名前に含む変数を自動的に削除しません。この値を `false` に設定すると、
明示的なフィルターを実行する前に、それらの自動除外が適用されます。

Codex は、最初に自動除外、次にカスタム除外、
`set` で指定した値、最後に include パターンの許可リストを適用します。`set`
は除外の後に適用されるため、除外された変数を復元できます。
ただし、include パターンの許可リストによって、復元された値が削除されることもあります。

従来の `exclude` 配列と `include_only` 配列は、既存の構成では引き続きサポートされます。
同じ構成レイヤー内では、どちらの配列も
`[shell_environment_policy.filters]` と組み合わせないでください。
Codex は、その組み合わせを拒否します。

## MCP サーバー

構成の詳細については、専用の [MCP ドキュメント](/ja-JP/codex/extend/mcp)を参照してください。

## オブザーバビリティとテレメトリ

Codex の実行状況（API リクエスト、SSE イベント、プロンプト、ツールの承認と結果）を追跡するには、OpenTelemetry（OTel）のログエクスポートを有効にします。デフォルトでは無効になっており、`[otel]` でオプトインします：

```toml
[otel]
environment = "staging"   # defaults to "dev"
exporter = "none"         # set to otlp-http or otlp-grpc to send events
log_user_prompt = false   # redact user prompts unless explicitly enabled

エクスポーターを選択します：

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

`exporter = "none"` の場合、Codex はイベントを記録しますが、何も送信しません。エクスポーターは非同期でバッチ処理を行い、シャットダウン時にフラッシュします。イベントのメタデータには、サービス名、CLI のバージョン、環境タグ、会話 ID、モデル、サンドボックスと承認の設定、イベントごとのフィールドが含まれます（[設定リファレンス](/ja-JP/codex/config-file/config-reference)を参照）。

### 出力内容

Codex は、実行とツールの使用に関する構造化ログイベントを出力します。代表的なイベントの種類は次のとおりです：

- `codex.conversation_starts`（モデル、推論設定、サンドボックス/承認ポリシー）
- `codex.api_request`（試行、ステータス/成否、所要時間、エラーの詳細）
- `codex.sse_event`（ストリームイベントの種類、成否、所要時間、および `response.completed` でのトークン数）
- `codex.websocket_request` と `codex.websocket_event`（リクエストの所要時間、およびメッセージごとの種類/成否/エラー）
- `codex.user_prompt`（長さ。内容は明示的に有効にしない限り伏せられます）
- `codex.tool_decision`（承認または拒否、および設定とユーザーのどちらによる判断か）
- `codex.tool_result`（所要時間、成功、出力スニペット）

### 出力される OTel メトリクス

OTel メトリクスパイプラインを有効にすると、Codex は API、ストリーム、ツールのアクティビティについて、カウンターと所要時間のヒストグラムを出力します。

以下の各メトリクスには、次のデフォルトのメタデータタグも含まれます：`auth_mode`、`originator`、`session_source`、`model`、`app.version`。

| メトリクス                                | 種類      | フィールド              | 説明                                                       |
| ------------------------------------- | --------- | ------------------- | ----------------------------------------------------------------- |
| `codex.api_request`                   | カウンター   | `status`、`success` | HTTP ステータスと成否別の API リクエスト数。             |
| `codex.api_request.duration_ms`       | ヒストグラム | `status`、`success` | API リクエストの所要時間（ミリ秒単位）。                             |
| `codex.sse_event`                     | カウンター   | `kind`、`success`   | イベントの種類と成否別の SSE イベント数。                |
| `codex.sse_event.duration_ms`         | ヒストグラム | `kind`、`success`   | SSE イベントの処理時間（ミリ秒単位）。                    |
| `codex.websocket.request`             | カウンター   | `success`           | 成否別の WebSocket リクエスト数。                       |
| `codex.websocket.request.duration_ms` | ヒストグラム | `success`           | WebSocket リクエストの所要時間（ミリ秒単位）。                       |
| `codex.websocket.event`               | カウンター   | `kind`、`success`   | 種類と成否別の WebSocket メッセージ/イベント数。        |
| `codex.websocket.event.duration_ms`   | ヒストグラム | `kind`、`success`   | WebSocket メッセージ/イベントの処理時間（ミリ秒単位）。      |
| `codex.tool.call`                     | カウンター   | `tool`, `success`   | ツール名と成功／失敗別のツール呼び出し回数。           |
| `codex.tool.call.duration_ms`         | ヒストグラム | `tool`, `success`   | ツール名と結果別のツール実行時間（ミリ秒）。 |

テレメトリに関するセキュリティとプライバシーの詳細については、[セキュリティ](/ja-JP/codex/agent-approvals-security#monitoring-and-telemetry)を参照してください。

### メトリクス

デフォルトでは、Codex は匿名の利用状況と稼働状況に関する少量のデータを定期的に OpenAI に送信します。これにより、Codex が正常に動作していない状況を検出し、利用されている機能や構成オプションを把握できるため、Codex チームは最も重要な点に注力できます。これらのメトリクスに個人を特定できる情報（PII）は含まれません。メトリクスの収集は、OTel のログ／トレースのエクスポートとは独立しています。

マシン上の ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能でメトリクスの収集を完全に無効にするには、構成で analytics フラグを設定します。

```toml
[analytics]
enabled = false

各メトリクスには、固有のフィールドに加えて、以下のデフォルトのコンテキストフィールドが含まれます。

#### デフォルトのコンテキストフィールド（すべてのイベント／メトリクスに適用）

- `auth_mode`: `swic` \| `api` \| `unknown`
- `model`: 使用したモデル名
- `app.version`: Codex のバージョン

#### メトリクスカタログ

各メトリクスには、必須フィールドに加えて、上記のデフォルトのコンテキストフィールドが含まれます。以下のメトリクス名では接頭辞 `codex.` を省略しています。
ほとんどのメトリクス名は `codex-rs/otel/src/metrics/names.rs` に集約されていますが、このファイル以外で出力される機能固有のメトリクスも掲載しています。
メトリクスに `tool` フィールドが含まれる場合、その値は使用された内部ツール（`apply_patch` や `shell` など）を示し、実際のシェルコマンドや `codex` が適用しようとしているパッチは含まれません。

#### ランタイムとモデル通信

| メトリクス                                          | 種類      | フィールド               | 説明                                                  |
| ----------------------------------------------- | --------- | -------------------- | ------------------------------------------------------------ |
| `api_request`                                   | カウンター   | `status`, `success`  | HTTP ステータスと成功／失敗別の API リクエスト数。        |
| `api_request.duration_ms`                       | ヒストグラム | `status`, `success`  | API リクエストの所要時間（ミリ秒）。                        |
| `sse_event`                                     | カウンター   | `kind`, `success`    | イベントの種類と成功／失敗別の SSE イベント数。           |
| `sse_event.duration_ms`                         | ヒストグラム | `kind`, `success`    | SSE イベントの処理時間（ミリ秒）。               |
| `websocket.request`                             | カウンター   | `success`            | 成功／失敗別の WebSocket リクエスト数。                  |
| `websocket.request.duration_ms`                 | ヒストグラム | `success`            | WebSocket リクエストの所要時間（ミリ秒）。                  |
| `websocket.event`                               | カウンター   | `kind`, `success`    | 種類と成功／失敗別の WebSocket メッセージ／イベント数。   |
| `websocket.event.duration_ms`                   | ヒストグラム | `kind`, `success`    | WebSocket メッセージ／イベントの処理時間（ミリ秒）。 |
| `responses_api_overhead.duration_ms`            | ヒストグラム |                      | WebSocket レスポンスから取得した Responses API のオーバーヘッド時間。      |
| `responses_api_inference_time.duration_ms`      | ヒストグラム |                      | WebSocket レスポンスから取得した Responses API の推論時間。     |
| `responses_api_engine_iapi_ttft.duration_ms`    | ヒストグラム |                      | Responses API エンジンの IAPI における最初のトークンまでの時間。        |
| `responses_api_engine_service_ttft.duration_ms` | ヒストグラム |                      | Responses API エンジンのサービスにおける最初のトークンまでの時間。     |
| `responses_api_engine_iapi_tbt.duration_ms`     | ヒストグラム |                      | Responses API エンジンの IAPI におけるトークン間の時間。         |
| `responses_api_engine_service_tbt.duration_ms`  | ヒストグラム |                      | Responses API エンジンのサービスにおけるトークン間の時間。      |
| `transport.fallback_to_http`                    | カウンター   | `from_wire_api`      | WebSocket から HTTP へのフォールバック回数。                            |
| `remote_models.fetch_update.duration_ms`        | ヒストグラム |                      | リモートモデル定義の取得にかかる時間。                      |
| `remote_models.load_cache.duration_ms`          | ヒストグラム |                      | リモートモデルキャッシュの読み込みにかかる時間。                         |
| `startup_prewarm.duration_ms`                   | ヒストグラム | `status`             | 結果別の起動時プリウォーム時間。                         |
| `startup_prewarm.age_at_first_turn_ms`          | ヒストグラム | `status`             | 最初の実ターンで解決された時点における、起動時プリウォームの経過時間。    |
| `cloud_requirements.fetch.duration_ms`          | ヒストグラム |                      | ワークスペースで管理されるクラウド要件の取得時間。         |
| `cloud_requirements.fetch_attempt`              | カウンター   | 注記を参照             | ワークスペースで管理されるクラウド要件の取得試行。         |
| `cloud_requirements.fetch_final`                | カウンター   | 注記を参照             | ワークスペースで管理されるクラウド要件の最終取得結果。    |
| `cloud_requirements.load`                       | カウンター   | `trigger`、`outcome` | ワークスペースで管理されるクラウド要件の読み込み結果。           |

`cloud_requirements.fetch_attempt` メトリクスには、`trigger`、`attempt`、`outcome`、`status_code` の各フィールドが含まれます。`cloud_requirements.fetch_final` メトリクスには、`trigger`、`outcome`、`reason`、`attempt_count`、`status_code` の各フィールドが含まれます。

#### ターンとツールのアクティビティ

| メトリクス                                 | 種類      | フィールド                                                                    | 説明                                                                                                      |
| -------------------------------------- | --------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `turn.e2e_duration_ms`                 | ヒストグラム |                                                                           | ターン全体のエンドツーエンド所要時間。                                                                                 |
| `turn.ttft.duration_ms`                | ヒストグラム |                                                                           | ターンで最初のトークンが出力されるまでの時間。                                                                                  |
| `turn.ttfm.duration_ms`                | ヒストグラム |                                                                           | ターンで最初のモデル出力項目が得られるまでの時間。                                                                      |
| `turn.network_proxy`                   | カウンター   | `active`、`tmp_mem_enabled`                                               | そのターンで管理対象のネットワークプロキシが有効だったかどうか。                                                       |
| `turn.memory`                          | カウンター   | `read_allowed`、`feature_enabled`、`config_use_memories`、`has_citations` | ターンごとのメモリ読み取り可否とメモリ引用の使用状況。                                                     |
| `turn.tool.call`                       | ヒストグラム | `tmp_mem_enabled`                                                         | ターン内のツール呼び出し回数。                                                                                |
| `turn.token_usage`                     | ヒストグラム | `token_type`、`tmp_mem_enabled`                                           | ターンごとのトークン使用量（`total`、`input`、`cached_input`、`output`、または `reasoning_output` の各トークン種別）。          |
| `tool.call`                            | カウンター   | `tool`、`success`                                                         | ツール名および成否別のツール呼び出し回数。                                                          |
| `tool.call.duration_ms`                | ヒストグラム | `tool`、`success`                                                         | ツール名および結果別のツール実行時間（ミリ秒）。                                                |
| `tool.unified_exec`                    | カウンター   | `tty`                                                                     | TTY モード別の統合 exec ツール呼び出し回数。                                                                             |
| `approval.requested`                   | カウンター   | `tool`、`approved`                                                        | ツール承認リクエストの結果（`approved`、`approved_with_amendment`、`approved_for_session`、`denied`、`abort`）。 |
| `mcp.call`                             | カウンター   | 注記を参照                                                                  | MCP ツールの呼び出し結果。                                                                                      |
| `mcp.call.duration_ms`                 | ヒストグラム | 注記を参照                                                                  | MCP ツールの呼び出し所要時間。                                                                                    |
| `mcp.tools.list.duration_ms`           | ヒストグラム | `cache`                                                                   | MCP ツール一覧取得の所要時間（キャッシュのヒット/ミス状態を含む）。                                                          |
| `mcp.tools.fetch_uncached.duration_ms` | ヒストグラム |                                                                           | MCP ツールの取得がキャッシュミスした場合の所要時間。                                                                |
| `mcp.tools.cache_write.duration_ms`    | ヒストグラム |                                                                           | Codex アプリの MCP ツールキャッシュへの書き込み時間。                                                                    |
| `hooks.run`                            | カウンター   | `hook_name`、`source`、`status`                                           | フック名、ソース、ステータス別のフック実行回数。                                                                 |
| `hooks.run.duration_ms`                | ヒストグラム | `hook_name`、`source`、`status`                                           | フックの実行時間（ミリ秒）。                                                                               |

`mcp.call` と `mcp.call.duration_ms` のメトリクスには `status` が含まれます。通常のツール呼び出しで出力されるメトリクスには `tool` も含まれ、利用可能な場合は `connector_id` と `connector_name` も含まれます。ブロックされた Codex アプリの MCP 呼び出しでは、`mcp.call` が `status` のみを含む形で出力されることがあります。

#### スレッド、タスク、機能

| メトリクス                            | 種類      | フィールド                | 説明                                                                      |
| --------------------------------- | --------- | --------------------- | -------------------------------------------------------------------------------- |
| `feature.state`                   | カウンター   | `feature`、`value`    | デフォルトと異なる機能の値（デフォルト以外の値 1 件につき 1 行を出力）。         |
| `status_line`                     | カウンター   |                       | 設定済みのステータス行で開始されたセッション。                                   |
| `model_warning`                   | カウンター   |                       | モデルに送信された警告。                                                       |
| `thread.started`                  | カウンター   | `is_git`              | 作業ディレクトリが Git リポジトリ内にあるかどうかでタグ付けされた新規スレッドの作成。    |
| `conversation.turn.count`         | カウンター   |                       | スレッド終了時に記録される、スレッドごとのユーザー／アシスタントのターン数。              |
| `thread.fork`                     | カウンター   | `source`              | 既存スレッドのフォークによる新規スレッドの作成。                                |
| `thread.rename`                   | カウンター   |                       | スレッド名の変更。                                                                  |
| `thread.side`                     | カウンター   | `source`              | サイド会話の作成。                                                       |
| `thread.skills.enabled_total`     | ヒストグラム |                       | 新規スレッドで有効になっているスキル数。                                       |
| `thread.skills.kept_total`        | ヒストグラム |                       | プロンプトのレンダリング後も保持された有効なスキル数。                            |
| `thread.skills.truncated`         | ヒストグラム |                       | スキルのレンダリング時に、有効なスキルのリストが切り詰められたかどうか（`1` または `0`）。          |
| `task.compact`                    | カウンター   | `type`                | 手動と自動の両方を含む、種類別（`remote` または `local`）のコンパクション数。 |
| `task.review`                     | カウンター   |                       | トリガーされたレビュー数。                                                     |
| `task.undo`                       | カウンター   |                       | トリガーされた取り消し操作の数。                                                |
| `task.user_shell`                 | カウンター   |                       | ユーザーによるシェル操作の数（例：TUI での `!`）。                       |
| `shell_snapshot`                  | カウンター   | 注記を参照              | シェルスナップショットの取得が成功したかどうか。                                       |
| `shell_snapshot.duration_ms`      | ヒストグラム | `success`             | シェルスナップショットの取得にかかった時間。                                                   |
| `skill.injected`                  | カウンター   | `status`、`skill`     | スキル注入の結果（スキル別）。                                               |
| `plugins.startup_sync`            | カウンター   | `transport`、`status` | キュレーション済みプラグインの起動時同期の試行回数。                                            |
| `plugins.startup_sync.final`      | カウンター   | `transport`、`status` | キュレーション済みプラグインの起動時同期の最終結果。                                       |
| `multi_agent.spawn`               | カウンター   | `role`                | ロール別のエージェント起動数。                                                            |
| `multi_agent.resume`              | カウンター   |                       | エージェントの再開回数。                                                                   |
| `multi_agent.nickname_pool_reset` | カウンター   |                       | エージェントのニックネームプールのリセット回数。                                                      |

`shell_snapshot` メトリクスには `success` が含まれ、失敗時には `failure_reason` も含まれます。

#### メモリとローカル状態

| メトリクス                         | 種類      | フィールド                    | 説明                                               |
| ------------------------------ | --------- | ------------------------- | --------------------------------------------------------- |
| `memory.phase1`                | カウンター   | `status`                  | メモリフェーズ 1 のステータス別ジョブ数。                      |
| `memory.phase1.e2e_ms`         | ヒストグラム |                           | メモリフェーズ 1 のエンドツーエンド所要時間。                   |
| `memory.phase1.output`         | カウンター   |                           | メモリフェーズ 1 で書き込まれた出力数。                           |
| `memory.phase1.token_usage`    | ヒストグラム | `token_type`              | メモリフェーズ 1 のトークン種別ごとのトークン使用量。                 |
| `memory.phase2`                | カウンター   | `status`                  | メモリフェーズ 2 のステータス別ジョブ数。                      |
| `memory.phase2.e2e_ms`         | ヒストグラム |                           | メモリフェーズ 2 のエンドツーエンド所要時間。                   |
| `memory.phase2.input`          | カウンター   |                           | メモリフェーズ 2 の入力数。                               |
| `memory.phase2.token_usage`    | ヒストグラム | `token_type`              | メモリフェーズ 2 のトークン種別ごとのトークン使用量。                 |
| `memories.usage`               | カウンター   | `kind`、`tool`、`success` | 種類、ツール、成否別のメモリ使用回数。          |
| `external_agent_config.detect` | カウンター   | 注記を参照                  | 移行項目タイプ別の外部エージェント設定の検出数。  |
| `external_agent_config.import` | カウンター   | 注記を参照                  | 移行項目タイプ別の外部エージェント設定のインポート数。     |
| `db.backfill`                  | カウンター   | `status`                  | 初期状態 DB のバックフィル結果（`upserted`、`failed`）。 |
| `db.backfill.duration_ms`      | ヒストグラム | `status`                  | 初期状態 DB のバックフィル所要時間。                |
| `db.error`                     | カウンター   | `stage`                   | 状態 DB の操作中に発生したエラー数。                        |

`external_agent_config.detect` と `external_agent_config.import` のメトリクスには `migration_type` が含まれ、スキルの移行には `skills_count` も含まれます。

#### Windows サンドボックス

| メトリクス                                           | 種類      | フィールド                                    | 説明                                           |
| ------------------------------------------------ | --------- | ----------------------------------------- | ----------------------------------------------------- |
| `windows_sandbox.setup_success`                  | カウンター   | `originator`、`mode`                      | Windows サンドボックスのセットアップ成功数。                      |
| `windows_sandbox.setup_failure`                  | カウンター   | `originator`、`mode`                      | Windows サンドボックスのセットアップ失敗数。                       |
| `windows_sandbox.setup_duration_ms`              | ヒストグラム | `result`、`originator`、`mode`            | Windows サンドボックスのセットアップ所要時間。                       |
| `windows_sandbox.elevated_setup_success`         | カウンター   |                                           | 管理者権限での Windows サンドボックスのセットアップ成功数。             |
| `windows_sandbox.elevated_setup_failure`         | カウンター   | 注記を参照                                  | 管理者権限での Windows サンドボックスのセットアップ失敗数。              |
| `windows_sandbox.elevated_setup_canceled`        | カウンター   | 注記を参照                                  | 管理者権限での Windows サンドボックスのセットアップ試行のキャンセル数。     |
| `windows_sandbox.elevated_setup_duration_ms`     | ヒストグラム | `result`                                  | 管理者権限での Windows サンドボックスのセットアップ所要時間。              |
| `windows_sandbox.elevated_prompt_shown`          | カウンター   |                                           | 管理者権限でのサンドボックスセットアップ用プロンプトが表示された回数。                  |
| `windows_sandbox.elevated_prompt_accept`         | カウンター   |                                           | 管理者権限でのサンドボックスセットアップ用プロンプトが承諾された回数。               |
| `windows_sandbox.elevated_prompt_use_legacy`     | カウンター   |                                           | 管理者権限でのセットアップ用プロンプトで、ユーザーが従来のサンドボックスを選択した回数。   |
| `windows_sandbox.elevated_prompt_quit`           | カウンター   |                                           | 管理者権限でのセットアップ用プロンプトでユーザーが終了した回数。                   |
| `windows_sandbox.fallback_prompt_shown`          | カウンター   |                                           | フォールバック用サンドボックスのプロンプト表示。                        |
| `windows_sandbox.fallback_retry_elevated`        | カウンター   |                                           | ユーザーがフォールバックプロンプトから昇格セットアップを再試行。 |
| `windows_sandbox.fallback_use_legacy`            | カウンター   |                                           | ユーザーがフォールバックプロンプトで従来のサンドボックスを選択。   |
| `windows_sandbox.fallback_prompt_quit`           | カウンター   |                                           | ユーザーがフォールバックプロンプトで終了。                   |
| `windows_sandbox.legacy_setup_preflight_failed`  | カウンター   | 注記を参照                                  | 従来の Windows サンドボックスセットアップの事前チェック失敗。       |
| `windows_sandbox.setup_elevated_sandbox_command` | カウンター   |                                           | 昇格サンドボックスのセットアップコマンドの呼び出し。               |
| `windows_sandbox.createprocessasuserw_failed`    | カウンター   | `error_code`、`path_kind`、`exe`、`level` | Windows での `CreateProcessAsUserW` の失敗。              |

昇格セットアップの失敗メトリクスには、Windows セットアップの失敗に関する詳細情報が利用できる場合、`code` と `message` が含まれます。共有セットアップパスから発行された場合は、`originator` も含まれることがあります。`windows_sandbox.legacy_setup_preflight_failed` メトリクスには、共有セットアップパスから発行された場合に `originator` が含まれますが、フォールバックプロンプトでの事前チェック失敗にはフィールドがまったく含まれないことがあります。

### フィードバックの制御

デフォルトでは、ローカルクライアントのユーザーは `/feedback` からフィードバックを送信できます。マシン上の ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能のすべてでフィードバック収集を無効にするには、設定を更新します：

```toml
[feedback]
enabled = false

無効にすると、`/feedback` には無効であることを示すメッセージが表示され、Codex はフィードバックの送信を拒否します。

### 推論イベントの表示と非表示

CI ログなどに表示される冗長な「推論」出力を減らしたい場合は、次のように抑制できます：

```toml
hide_agent_reasoning = true

モデルが未加工の推論内容を出力したときに、それを表示するには：

```toml
show_raw_agent_reasoning = true

未加工の推論は、ワークフローで許容できる場合にのみ有効にしてください。一部のモデルやプロバイダー（`gpt-oss` など）は未加工の推論を出力しません。その場合、この設定による表示上の変化はありません。

## 通知

Codex が対応イベント（現在は `agent-turn-complete` のみ）を発行するたびに外部プログラムを起動するには、`notify` を使用します。デスクトップのトースト通知、チャットの Webhook、CI の更新など、TUI の組み込み通知では対応できない別経路での通知に便利です。

```toml
notify = ["python3", "/path/to/notify.py"]

`agent-turn-complete` に反応する `notify.py` の例（一部省略）：

```python
#!/usr/bin/env python3

def main() -> int:
    notification = json.loads(sys.argv[1])
    if notification.get("type") != "agent-turn-complete":
        return 0
    title = f"Codex: {notification.get('last-assistant-message', 'Turn Complete!')}"
    message = " ".join(notification.get("input-messages", []))
    subprocess.check_output([
        "terminal-notifier",
        "-title", title,
        "-message", message,
        "-group", "codex-" + notification.get("thread-id", ""),
        "-activate", "com.googlecode.iterm2",
    ])
    return 0

if __name__ == "__main__":
    sys.exit(main())

スクリプトは単一の JSON 引数を受け取ります。主なフィールドは次のとおりです：

- `type`（現在は `agent-turn-complete`）
- `thread-id`（セッション識別子）
- `turn-id`（ターン識別子）
- `cwd`（作業ディレクトリ）
- `input-messages`（そのターンにつながったユーザーメッセージ）
- `last-assistant-message`（最後のアシスタントメッセージのテキスト）

スクリプトをディスク上の任意の場所に配置し、`notify` でそのパスを指定します。

#### `notify` と `tui.notifications` の比較

- `notify` は外部プログラムを実行します。Webhook、デスクトップ通知ツール、CI フックなどに適しています。
- `tui.notifications` は TUI に組み込まれており、必要に応じてイベント種別（`agent-turn-complete` や `approval-requested` など）でフィルタリングできます。
- `tui.notification_method` は、TUI がターミナル通知を発行する方法（`auto`、`osc9`、`bel` のいずれか）を制御します。
- `tui.notification_condition` は、TUI 通知の送信タイミングを、
  ターミナルが `unfocused` の場合のみとするか、`always` とするかを制御します。

`auto` モードでは、Codex は OSC 9 通知（ターミナルによってはデスクトップ通知として解釈されるターミナルエスケープシーケンス）を優先し、それ以外の場合は BEL（`\x07`）にフォールバックします。

正確なキーについては、[構成リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

## 履歴の永続化

デフォルトでは、Codex はローカルセッションの会話記録を `CODEX_HOME` 配下（例：`~/.codex/history.jsonl`）に保存します。ローカル履歴の永続化を無効にするには、次のように設定します：

```toml
[history]
persistence = "none"

履歴ファイルのサイズに上限を設定するには、`history.max_bytes` を設定します。ファイルが上限を超えると、Codex は最も古いエントリを削除し、最新の記録を残してファイルのコンパクションを行います。

```toml
[history]
max_bytes = 104857600 # 100 MiB

## クリック可能な引用

対応するターミナルまたはエディターとの連携機能を使用している場合、Codex はファイルの引用をクリック可能なリンクとして表示できます。Codex が使用する URI スキームを選択するには、`file_opener` を設定します：

```toml
file_opener = "vscode" # or cursor, windsurf, vscode-insiders, none

たとえば、`/home/user/project/main.py:42` のような引用は、クリック可能な `vscode://file/...:42` リンクに書き換えられます。

## プロジェクト指示の検出

Codex は `AGENTS.md` と関連ファイルを読み込み、セッションの最初のターンに一定量のプロジェクト指示を含めます。この動作は次の 2 つの設定で制御します：

- `project_doc_max_bytes`：各 `AGENTS.md` ファイルから読み込む量
- `project_doc_fallback_filenames`：各ディレクトリ階層で `AGENTS.md` が見つからない場合に追加で試すファイル名

詳しい手順については、[AGENTS.md を使用したカスタム指示](/ja-JP/codex/agent-configuration/agents-md)を参照してください。

## デスクトップ

このセクションのオプションは、ChatGPT デスクトップアプリにのみ適用されます。

### カスタムファイルハンドラーの追加

ユーザーレベルの `~/.codex/config.toml` で、
`desktop.custom_file_handlers` 配下にエントリを追加すると、
ChatGPT デスクトップアプリがデフォルトでは対応していないエディターや内部ランチャーでファイルを開けます。
各エントリにより、アプリの **次で開く** メニューにエディターの候補が追加されます。
`command` が既存の絶対パスであるか、アプリの `PATH` から解決できる場合に、その候補が表示されます。

次の例では、ファイルをハンドラーに渡す 3 つの方法を示します：

```toml
# Append the opened path directly after the command.
[desktop.custom_file_handlers.vscodium]
label = "VSCodium"
icon = "/Users/you/.codex/icons/vscodium.png"
command = "codium"

# Place fixed arguments before the opened path.
[desktop.custom_file_handlers.textedit]
label = "TextEdit"
icon = "/Users/you/.codex/icons/textedit.png"
command = "/usr/bin/open"
args = ["-a", "TextEdit"]

# Append one JSON argument with the path and editor context.
[desktop.custom_file_handlers.company_editor]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"
input = "json_argument"

`config.toml` を保存してから、ChatGPT デスクトップアプリを再起動します。

ハンドラー ID は TOML テーブルヘッダーの最後のセグメントです。
長さは 1～64 文字で、先頭には ASCII の英字または数字を使用し、それ以外には
ASCII の英字、数字、ピリオド、アンダースコア、ハイフンのみを使用できます。
アプリでは ID に `custom:` プレフィックスを付けて公開します。たとえば、`company_editor` は
`custom:company_editor` になります。ピリオドを含む ID は、
TOML がネストされたテーブルとして解釈しないよう、引用符で囲みます。例：

```toml
[desktop.custom_file_handlers."company.editor"]
label = "Company Editor"
icon = "/opt/company/editor/icon.png"
command = "/opt/company/bin/editor"

各ハンドラーでは次のフィールドを使用できます：

| フィールド          | 必須 | 説明                                                                                                                                                              |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `label`        | はい      | アプリ内での表示名。                                                                                                                                                 |
| `icon`         | はい      | アプリに同梱されているアイコン（`apps/vscode.png` など）、base64 形式の `data:image/...` URL、`file:` URI、またはローカル画像の絶対パス。サポート対象外のソースでは、デフォルトの VS Code アイコンが使用されます。 |
| `command`      | はい      | 検出して起動する実行可能ファイルのパス、またはコマンド名。                                                                                                                    |
| `args`         | いいえ       | `command` とファイル入力の間に挿入される文字列の配列。デフォルトは `[]` です。                                                                                            |
| `input`        | いいえ       | アプリがファイル入力を送信する方法：`path`、`json_argument`、または `json_stdin`。デフォルトは `path` です。                                                                              |
| `supports_ssh` | いいえ       | SSH ワークスペース内のファイルに対してハンドラーを利用できるようにするかどうか。デフォルトは `false` です。ハンドラーでリモートホストとパスの詳細が必要な場合は、`json_stdin` を使用します。                     |

`input` の値によって、`args` の後に続く内容が決まります：

- `path` の場合、パスがコマンドの最後の引数として追加されます。
- `json_argument` の場合、`target`、`path`、`appPath`、
`location` を含む JSON オブジェクトが追加されます。`location` の値は、1 始まりの `line` と
`column` の値を持つオブジェクト、または `null` です。
- `json_stdin` の場合、引数を追加する代わりに、JSON オブジェクトを
  標準入力に書き込みます。このオブジェクトには `hostConfig`、`remoteWorkspaceRoot`、
`remotePath` も含まれます。該当しない場合、これらのフィールドの値は `null` になります。

たとえば、`company_editor` は、ユーザーが
ソースコードの特定の位置を開いたときに、次の引数を受け取れます：

```json
{
  "target": "custom:company_editor",
  "path": "/repo/src/index.ts",
  "appPath": null,
  "location": { "line": 12, "column": 3 }
}

カスタムハンドラーを優先エディターとして選択すると、組み込みエディターを選択した場合と同様に、
プロジェクトごとの設定を含めて選択内容が保存されます。

## TUI オプション

サブコマンドを指定せずに `codex` を実行すると、対話型ターミナル UI（TUI）が起動します。Codex では、`[tui]` に次のような TUI 固有の構成項目が用意されています：

- `tui.notifications`：通知の有効化／無効化、または特定の種類への制限
- `tui.notification_method`：ターミナル通知に `auto`、`osc9`、`bel` のいずれかを選択
- `tui.notification_condition`：`unfocused` または `always` を選択し、
  通知を発行する条件を指定
- `tui.animations`：ASCII アニメーションとシマー効果の有効化／無効化
- `tui.alternate_screen`：代替画面の使用を制御（ターミナルのスクロールバックを保持するには `never` に設定）
- `tui.show_tooltips`：ウェルカム画面でのオンボーディング用ツールチップの表示／非表示

`tui.notification_method` のデフォルトは `auto` です。`auto` モードでは、Codex は、ターミナルが対応しているとみられる場合には OSC 9 通知（一部のターミナルがデスクトップ通知として解釈するターミナルのエスケープシーケンス）を優先し、それ以外の場合には BEL（`\x07`）にフォールバックします。

キーの全一覧については、[構成リファレンス](/ja-JP/codex/config-file/config-reference) を参照してください。
