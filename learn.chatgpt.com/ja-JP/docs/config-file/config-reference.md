<!-- source: https://learn.chatgpt.com/ja-JP/docs/config-file/config-reference -->

このページは、Codex の設定ファイルを調べるための検索可能なリファレンスです。概念の解説や例については、まず[設定の基本](/ja-JP/codex/config-file/config-basic)と[高度な設定](/ja-JP/codex/config-file/config-advanced)を参照してください。

## `config.toml`

ユーザーレベルの設定は `~/.codex/config.toml` にあります。プロジェクト単位の上書き設定を `.codex/config.toml` ファイルに追加することもできます。Codex は、プロジェクトを信頼している場合にのみ、プロジェクト単位の設定ファイルを読み込みます。

プロジェクト単位の設定では、マシンローカルのプロバイダー、認証、
ホスト側で管理するアプリリクエストのメタデータ、通知、設定プロファイルの選択、
テレメトリのルーティングキーを上書きできません。Codex は、`openai_base_url`、
`chatgpt_base_url`、`apps_mcp_product_sku`、`model_provider`、
`model_providers`、`notify`、`profile`、`profiles`、
`experimental_realtime_ws_base_url`、`otel` が
プロジェクト内の `.codex/config.toml` に含まれていても無視します。プロバイダー、通知、テレメトリのキーは、
代わりにユーザーレベルの設定に記述してください。設定の[プロファイルファイル](/ja-JP/codex/config-file/config-advanced#profiles)は、
`config.toml` と同じディレクトリに `$CODEX_HOME/profile-name.config.toml` として配置します。
`--profile profile-name` で使用するプロファイルを選択します。

サンドボックスと承認に関するキー（`approval_policy`、`sandbox_mode`、`sandbox_workspace_write.*`）については、このリファレンスと併せて[サンドボックスと承認](/ja-JP/codex/agent-approvals-security#sandbox-and-approvals)、[書き込み可能なルート内の保護されたパス](/ja-JP/codex/agent-approvals-security#protected-paths-in-writable-roots)、[ネットワークアクセス](/ja-JP/codex/agent-approvals-security#network-access)を参照してください。ベータ版の権限プロファイルについては、[権限](/ja-JP/codex/permissions)を参照してください。

<ConfigTable
  options={[
    {
      key: "model",
      type: "string",
      description: "使用するモデルです（例：`gpt-5.5`）。",
    },
    {
      key: "review_model",
      type: "string",
      description:
        "`/review` で使用するモデルの上書き設定です（任意）。デフォルトでは、現在のセッションのモデルを使用します。",
    },
    {
      key: "model_provider",
      type: "string",
      description: "`model_providers` のプロバイダー ID です（デフォルト：`openai`）。",
    },
    {
      key: "openai_base_url",
      type: "string",
      description:
        "組み込みの `openai` モデルプロバイダーのベース URL を上書きします。",
    },
    {
      key: "model_context_window",
      type: "number",
      description: "アクティブなモデルで使用できるコンテキストウィンドウのトークン数です。",
    },
    {
      key: "model_auto_compact_token_limit",
      type: "number",
      description:
        "履歴の自動コンパクションを開始するトークン数のしきい値です。未設定の場合は、モデルのデフォルト値を使用します。",
    },
    {
      key: "model_auto_compact_token_limit_scope",
      type: "total | body_after_prefix",
      description:
        "自動コンパクションのしきい値の計算で、アクティブなコンテキスト全体（デフォルトの `total`）を数えるか、引き継がれたコンパクションウィンドウのプレフィックスより後の増加分（`body_after_prefix`）のみを数えるかを指定します。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description:
        "起動時に読み込む JSON モデルカタログのパスです（任意）。選択した `$CODEX_HOME/profile-name.config.toml` プロファイルファイルで、プロファイルごとにこの設定を上書きできます。",
    },
    {
      key: "oss_provider",
      type: "lmstudio | ollama",
      description:
        "`--oss` で実行する際に使用するデフォルトのローカルプロバイダーです。未設定の場合は、プロバイダーの指定を求めます。",
    },
    {
      key: "approval_policy",
      type: "untrusted | on-request | never | { granular = { sandbox_approval = bool, rules = bool, mcp_elicitations = bool, request_permissions = bool, skill_approval = bool } }",
      description:
        "コマンド実行前に Codex が一時停止して承認を求めるタイミングを指定します。`approval_policy = { granular = { ... } }` を使用すると、ほかのプロンプトでは対話形式を維持しながら、特定のカテゴリのプロンプトについて表示を許可するか自動拒否するかを指定することもできます。`on-failure` は非推奨です。対話型の実行では `on-request`、非対話型の実行では `never` を使用してください。",
    },
    {
      key: "approval_policy.granular.sandbox_approval",
      type: "boolean",
      description:
        "`true` の場合、サンドボックスの権限昇格に関する承認プロンプトの表示が許可されます。",
    },
    {
      key: "approval_policy.granular.rules",
      type: "boolean",
      description:
        "`true` の場合、execpolicy の `prompt` ルールによって発生する承認プロンプトの表示が許可されます。",
    },
    {
      key: "approval_policy.granular.mcp_elicitations",
      type: "boolean",
      description:
        "`true` の場合、MCP の誘発プロンプトは自動拒否されず、表示が許可されます。",
    },
    {
      key: "approval_policy.granular.request_permissions",
      type: "boolean",
      description:
        "`true` の場合、`request_permissions` ツールからのプロンプトの表示が許可されます。",
    },
    {
      key: "approval_policy.granular.skill_approval",
      type: "boolean",
      description:
        "`true` の場合、スキルスクリプトの承認プロンプトの表示が許可されます。",
    },
    {
      key: "approvals_reviewer",
      type: "user | auto_review",
      description:
        "`on-request` またはきめ細かな承認ポリシーで、対象となる承認プロンプトを誰がレビューするかを指定します。デフォルトは `user` です。`auto_review` ではレビュー担当のサブエージェントを使用します。この設定はサンドボックスの動作を変更しません。また、サンドボックス内ですでに許可されている操作をレビューの対象にすることもありません。",
    },
    {
      key: "auto_review.policy",
      type: "string",
      description:
        "自動レビュー用のローカルなポリシー指示を Markdown 形式で指定します。管理設定の `guardian_policy_config` が優先されます。空の値は無視されます。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description:
        "シェルベースのツールがログインシェルとして動作できるようにします。デフォルトは `true` です。`false` の場合、`login = true` のリクエストは拒否され、`login` を省略するとデフォルトで非ログインシェルになります。",
    },
    {
      key: "sandbox_mode",
      type: "read-only | workspace-write | danger-full-access",
      description:
        "コマンド実行時のファイルシステムおよびネットワークアクセスに適用するサンドボックスポリシーです。",
    },
    {
      key: "sandbox_workspace_write.writable_roots",
      type: "array<string>",
      description:
        "`sandbox_mode = \"workspace-write\"` の場合に追加する、書き込み可能なルートです。",
    },
    {
      key: "sandbox_workspace_write.network_access",
      type: "boolean",
      description:
        "workspace-write サンドボックス内で外部へのネットワークアクセスを許可します。",
    },
    {
      key: "sandbox_workspace_write.exclude_tmpdir_env_var",
      type: "boolean",
      description:
        "workspace-write モードで、書き込み可能なルートから `$TMPDIR` を除外します。",
    },
    {
      key: "sandbox_workspace_write.exclude_slash_tmp",
      type: "boolean",
      description:
        "workspace-write モードで、書き込み可能なルートから `/tmp` を除外します。",
    },
    {
      key: "windows.sandbox",
      type: "unelevated | elevated",
      description:
        "Windows 上で Codex をネイティブ実行する場合の、Windows 専用のネイティブサンドボックスモードです。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "Windows のネイティブ環境では、サンドボックス化された最終的な子プロセスをデフォルトでプライベートデスクトップ上で実行します。従来の `Winsta0\\\\Default` の動作との互換性が必要な場合にのみ `false` に設定してください。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "ブラウザの履歴へのアクセスを制限するには、`false` に設定します。管理要件によって、この制限を強制することもできます。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "フォールバックとして適用する、ブラウザのオリジンに対する制限です。`access`、`uploads`、`downloads`、`full_cdp_access` に対応しており、それぞれ `allow` または `deny` に設定します。",
    },
    {
      key: "browser_use.origins.<origin>",
      type: "table",
      description:
        "`browser_use.default_origin_policy` と同じフィールドを使用する、オリジンごとのブラウザ制限です。HTTP または HTTPS スキームを含め、必要に応じてポートを指定します。パス、クエリ、フラグメントは含めません。ローカルの設定値で、管理設定による拒否を緩和することはできません。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "コンピューターの使用で、フォールバックとして適用するネイティブアプリへのアクセスポリシーです。アプリ固有のエントリでポリシーを指定できます。ローカル設定で管理設定による制限を緩和することはできません。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description: "バンドル識別子をキーとして指定する、macOS ネイティブアプリへのアクセス設定です。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "Application User Model ID（AUMID）をキーとして指定する、パッケージ化された Windows アプリへのアクセス設定です。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "Windows 実行ファイルへのアクセスルールです。各ルールには `publisher_name`、`product_name`、`access`（`allow` または `deny`）が必要です。`binary_name` は任意です。",
    },
    {
      key: "computer_use.windows.always_allowed_app_ids",
      type: "array<string>",
      description:
        "「コンピューターの使用」で、承認を求めずに開ける Windows アプリの識別子です。一覧にないアプリには承認が必要です。保存済みの項目は、ChatGPT デスクトップアプリの「コンピューターの使用」設定から削除してください。",
    },
    {
      key: "notify",
      type: "array<string>",
      description:
        "通知時に呼び出されるコマンドです。Codex から JSON ペイロードを受け取ります。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description:
        "Codex の起動時に更新を確認します（更新を一元管理している場合にのみ false に設定してください）。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "すべてのローカルクライアントで `/feedback` によるフィードバック送信を有効にします（デフォルト：true）。",
    },
    {
      key: "analytics.enabled",
      type: "boolean",
      description:
        "このマシン／プロファイルのアナリティクスを有効または無効にします。未設定の場合は、クライアントのデフォルトが適用されます。",
    },
    {
      key: "instructions",
      type: "string",
      description:
        "将来の利用のために予約されています。`model_instructions_file` または `AGENTS.md` の使用を推奨します。",
    },
    {
      key: "developer_instructions",
      type: "string",
      description:
        "セッションに挿入する追加の開発者指示です（任意）。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description:
        "Codex がログファイルを書き込むディレクトリです。デフォルトは `$CODEX_HOME/log` です。この設定を明示すると、オプトイン方式のプレーンテキスト TUI ログ `codex-tui.log` も有効になり、同じディレクトリに出力されます。",
    },
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex が SQLite ベースの状態 DB を保存するディレクトリです。この DB は、エージェントのジョブや、その他の再開可能なランタイム状態に使用されます。",
    },
    {
      key: "compact_prompt",
      type: "string",
      description: "履歴のコンパクション用プロンプトをインラインで上書きします。",
    },
    {
      key: "model_instructions_file",
      type: "string (path)",
      description:
        "組み込みの指示を置き換える設定です。`AGENTS.md` の代わりに使用します。",
    },
    {
      key: "personality",
      type: "none | friendly | pragmatic",
      description:
        "`supportsPersonality` への対応を示すモデルのデフォルトのコミュニケーションスタイルです。スレッド単位、ターン単位、または `/personality` で上書きできます。",
    },
    {
      key: "service_tier",
      type: "string",
      description:
        "新しいターンで優先するサービスティアです。`fast`、またはアクティブなモデルが提示するほかのティアを使用してください。`fast` はリクエスト値 `priority` に対応します。",
    },
    {
      key: "experimental_compact_prompt_file",
      type: "string (path)",
      description:
        "コンパクション用プロンプトの上書き設定をファイルから読み込みます（試験的機能）。",
    },
    {
      key: "skills.max_context_tokens",
      type: "integer (positive)",
      description:
        "利用可能なスキルのカタログに割り当てるトークン数です。デフォルトはモデルのコンテキストウィンドウの 2% です。明示的に指定する値の上限は `10000` トークンです。",
    },
    {
      key: "skills.config",
      type: "array<object>",
      description: "config.toml に保存される、スキルごとの有効／無効の上書き設定です。",
    },
    {
      key: "skills.config.<index>.path",
      type: "string (path)",
      description: "`SKILL.md` を含むスキルフォルダーへのパスです。",
    },
    {
      key: "skills.config.<index>.enabled",
      type: "boolean",
      description: "参照先のスキルを有効または無効にします。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "ID で指定したアプリ／コネクタを有効または無効にします（デフォルト：true）。",
    },
    {
      key: "apps._default.enabled",
      type: "boolean",
      description:
        "アプリごとの上書き設定がない場合に、すべてのアプリに適用する有効／無効のデフォルト設定です。",
    },
    {
      key: "apps._default.destructive_enabled",
      type: "boolean",
      description:
        "`destructive_hint = true` が設定されたアプリツールを、デフォルトで許可するか拒否するかを指定します。",
    },
    {
      key: "apps._default.open_world_enabled",
      type: "boolean",
      description:
        "`open_world_hint = true` が設定されたアプリツールを、デフォルトで許可するか拒否するかを指定します。",
    },
    {
      key: "apps._default.approvals_reviewer",
      type: "user | auto_review",
      description:
        "アプリごとの上書き設定がない場合に、アプリツールの承認プロンプトをレビューするデフォルトの担当者です。省略すると、アプリは最上位の `approvals_reviewer` の値を継承します。",
    },
    {
      key: "apps._default.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "アプリ単位またはツール単位の上書き設定がないアプリツールに適用する、承認に関するデフォルトの動作です。",
    },
    {
      key: "apps.<id>.destructive_enabled",
      type: "boolean",
      description:
        "このアプリのツールのうち、`destructive_hint = true` を示すものを許可またはブロックします。",
    },
    {
      key: "apps.<id>.open_world_enabled",
      type: "boolean",
      description:
        "このアプリのツールのうち、`open_world_hint = true` を示すものを許可またはブロックします。",
    },
    {
      key: "apps.<id>.default_tools_enabled",
      type: "boolean",
      description:
        "ツールごとの上書き設定がない場合に、このアプリのツールに適用するデフォルトの有効・無効の設定です。",
    },
    {
      key: "apps.<id>.approvals_reviewer",
      type: "user | auto_review",
      description:
        "このアプリのツールの承認リクエストをレビューする担当です。`apps._default.approvals_reviewer` を上書きします。",
    },
    {
      key: "apps.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "ツールごとの上書き設定がない場合に、このアプリのツールに適用するデフォルトの承認動作です。",
    },
    {
      key: "apps.<id>.tools.<tool>.enabled",
      type: "boolean",
      description:
        "アプリの個々のツール（例：`repos/list`）の有効・無効を上書きする設定です。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "アプリの特定のツールに適用する承認動作の上書き設定です。",
    },
    {
      key: "tool_suggest.discoverables",
      type: "array<table>",
      description:
        "追加で検出できるコネクタやプラグインについて、ツールの提案を許可します。各エントリには `type = \"connector\"` または `\"plugin\"` と、`id` を指定します。",
    },
    {
      key: "tool_suggest.disabled_tools",
      type: "array<table>",
      description:
        "検出可能な特定のコネクタやプラグインの提案を無効にします。各エントリには `type = \"connector\"` または `\"plugin\"` と、`id` を指定します。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "アプリ（コネクタ）連携を有効にします。安定版の機能で、デフォルトで有効です。アプリとコネクタの通信は、サンドボックス内のコマンド用ネットワークプロキシや、そのドメイン許可リストによる制御の対象外です。",
    },
    {
      key: "features.hooks",
      type: "boolean",
      description:
        "`hooks.json` またはインラインの `[hooks]` 構成から読み込むライフサイクルフックを有効にします。`features.codex_hooks` は非推奨の別名です。",
    },
    {
      key: "features.code_mode.enabled",
      type: "boolean",
      description:
        "コードモード機能の構成を有効にします。この機能は開発中で、デフォルトでは無効です。",
    },
    {
      key: "features.code_mode.excluded_tool_namespaces",
      type: "array<string>",
      description:
        "コードモードで、ネストされたコードモードのツールガイダンスとエグゼキューターへの公開対象から除外するツールの名前空間です。",
    },
    {
      key: "features.code_mode.direct_only_tool_namespaces",
      type: "array<string>",
      description:
        "コードモードで、直接のツール呼び出しを通じてのみ使用できるツールの名前空間です。",
    },
    {
      key: "features.context_management.experimental_mode",
      type: "boolean",
      description:
        "試験的なコンテキスト管理を有効にします。デフォルトでは無効です。コンテキストを繰り返し単一の要約に圧縮する代わりに、メモと検索可能な履歴を使って、蓄積された詳細情報を保持します。Plus、Pro、または Pro Lite の ChatGPT アカウントでのサインインが必要です。",
    },
    {
      key: "features.rollout_budget.enabled",
      type: "boolean",
      description:
        "ロールアウト予算の追跡を有効にします。この機能は開発中で、デフォルトでは無効です。有効にする場合は `features.rollout_budget.limit_tokens` が必須です。",
    },
    {
      key: "features.rollout_budget.limit_tokens",
      type: "integer",
      description:
        "ロールアウト予算の追跡に使用するトークン数の上限です。正の値で指定します。ロールアウト予算を有効にする場合は必須です。",
    },
    {
      key: "features.rollout_budget.reminder_interval_tokens",
      type: "integer",
      description:
        "ロールアウト予算のリマインダーの間隔です。正のトークン数で指定します。デフォルトは `limit_tokens` の 10% で、最小値は 1 トークンです。",
    },
    {
      key: "features.rollout_budget.sampling_token_weight",
      type: "number",
      description:
        "ロールアウト予算の計算で、サンプリングされたトークンに適用する有限かつ非負の倍率です。デフォルトは `1.0` です。",
    },
    {
      key: "features.rollout_budget.prefill_token_weight",
      type: "number",
      description:
        "ロールアウト予算の計算で、プリフィルトークンに適用する有限かつ非負の倍率です。デフォルトは `1.0` です。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "`config.toml` 内でインライン定義するライフサイクルフックです。`hooks.json` と同じイベントスキーマを使用します。例とサポート対象のイベントについては、フックガイドを参照してください。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "`PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit`、`Stop`、`Interrupt` などのフックイベント用のマッチャーグループです。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "マッチャーグループ用のフックハンドラーです。コマンドフックと MCP ツールフックをサポートしています。プロンプトフックとエージェントフックのハンドラーは解析されますが、スキップされます。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "トリガー元の処理を遅らせることなく、コマンドフックをバックグラウンドで実行します。デフォルトは `false` です。`SessionEnd` は常に同期実行されます。[フックのバックグラウンド実行](/codex/hooks#run-hooks-in-the-background)を参照してください。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "大きすぎる `additionalContext` をディスクに保存し、モデルには短いプレビューを提示するための、ハンドラーごとのおおよそのトークンしきい値です。デフォルトは `2500` です。`0` の場合はコンテキスト全体をモデルに直接渡します。[サイズの大きいフック出力](/codex/hooks#large-hook-output)を参照してください。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "コマンドフックのコマンドを Windows でのみ上書きする設定です。TOML の別名 `command_windows` も使用できます。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description:
        "[メモリ](/codex/customization/memories)を有効にします。デフォルトでは無効です。",
    },
    {
      key: "mcp_optional_startup_grace_ms",
      type: "integer (milliseconds)",
      description:
        "初期ツールカタログの構築時に、必須ではない MCP サーバーに共通で適用する待機時間です。デフォルトは `1000` です。`0` に設定すると、代わりに各サーバーの `startup_timeout_sec` に従って待機します。",
    },
    {
      key: "mcp_servers.<id>.command",
      type: "string",
      description: "MCP stdio サーバーの起動コマンドです。",
    },
    {
      key: "mcp_servers.<id>.args",
      type: "array<string>",
      description: "MCP stdio サーバーのコマンドに渡す引数です。",
    },
    {
      key: "mcp_servers.<id>.env",
      type: "map<string,string>",
      description: "MCP stdio サーバーに転送する環境変数です。",
    },
    {
      key: "mcp_servers.<id>.env_vars",
      type: 'array<string | { name = string, source = "local" | "remote" }>',
      description:
        "MCP stdio サーバー向けに許可リストへ追加する環境変数です。文字列で指定したエントリは、デフォルトで `source = \"local\"` として扱われます。`source = \"remote\"` は、エグゼキューターを介したリモート stdio でのみ使用してください。",
    },
    {
      key: "mcp_servers.<id>.cwd",
      type: "string",
      description: "MCP stdio サーバープロセスの作業ディレクトリです。",
    },
    {
      key: "mcp_servers.<id>.url",
      type: "string",
      description: "MCP streamable HTTP サーバーのエンドポイントです。",
    },
    {
      key: "mcp_servers.<id>.auth",
      type: "oauth | chatgpt",
      description:
        "MCP HTTP サーバーで、設定済みの Bearer トークンと認可ヘッダーに次いで使用する認証フォールバックです。`oauth`（デフォルト）では、保存済みの MCP OAuth 認証情報があれば使用します。`chatgpt` では、信頼されたファーストパーティの ChatGPT オリジンに対して現在の ChatGPT セッションを使用し、その後、保存済みの OAuth 認証情報にフォールバックします。いずれの取得元からも認証情報が得られない場合、どちらのモードでも認証なしで接続できます。",
    },
    {
      key: "mcp_servers.<id>.oauth.client_id",
      type: "string",
      description:
        "この MCP サーバーでの認可とトークン交換に使用する、事前登録済みの OAuth クライアント ID です。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_url",
      type: "string",
      description:
        "サーバー固有の OAuth コールバックです。発行者の識別がサポートされている場合、または URL の末尾がすでにサーバー固有のコールバック ID である場合、事前登録済みのクライアントはこのコールバックを再利用します。それ以外の場合、Codex はグローバルまたはデフォルトのコールバックにその ID を付加して使用します。事前登録済みの ID がないクライアントは、クライアント登録時にこのコールバックを使用します。",
    },
    {
      key: "mcp_servers.<id>.oauth.callback_port",
      type: "integer",
      description:
        "この MCP サーバーの OAuth コールバックリスナーで使用する固定ポートです。`mcp_oauth_callback_port` を上書きします。URL にポートを明示した直接のループバックコールバックを使用する場合は、リスナーポートにも同じポートを設定してください。",
    },
    {
      key: "mcp_servers.<id>.bearer_token_env_var",
      type: "string",
      description:
        "MCP HTTP サーバーの Bearer トークンの取得元となる環境変数です。",
    },
    {
      key: "mcp_servers.<id>.http_headers",
      type: "map<string,string>",
      description: "各 MCP HTTP リクエストに含める静的な HTTP ヘッダーです。",
    },
    {
      key: "mcp_servers.<id>.http_headers_helper",
      type: "string (command)",
      description:
        "HTTP ヘッダーの名前と値を JSON オブジェクトとして出力するローカルコマンドです。ローカル接続の HTTP MCP サーバーでのみサポートされます。明示的に指定した Bearer トークンと OAuth 認証情報は、ヘルパーが提供する Authorization ヘッダーよりも優先されます。",
    },
    {
      key: "mcp_servers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "環境変数から値を設定する、MCP HTTP サーバー用の HTTP ヘッダーです。",
    },
    {
      key: "mcp_servers.<id>.enabled",
      type: "boolean",
      description: "構成を削除せずに MCP サーバーを無効にします。",
    },
    {
      key: "mcp_servers.<id>.required",
      type: "boolean",
      description:
        "true の場合、有効化されているこの MCP サーバーを初期化できないと、起動または再開に失敗します。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_sec",
      type: "number",
      description:
        "MCP サーバーの起動タイムアウトを上書きします。デフォルトは 10 秒です。",
    },
    {
      key: "mcp_servers.<id>.startup_timeout_ms",
      type: "number",
      description: "`startup_timeout_sec` をミリ秒単位で指定するための別名です。",
    },
    {
      key: "mcp_servers.<id>.tool_timeout_sec",
      type: "number",
      description:
        "MCP サーバーのツールごとのタイムアウトを上書きします。デフォルトは 60 秒です。",
    },
    {
      key: "mcp_servers.<id>.enabled_tools",
      type: "array<string>",
      description: "MCP サーバーが公開するツール名の許可リストです。",
    },
    {
      key: "mcp_servers.<id>.disabled_tools",
      type: "array<string>",
      description:
        "MCP サーバーの `enabled_tools` の適用後に適用する拒否リストです。",
    },
    {
      key: "mcp_servers.<id>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "ツールごとの上書き設定がない場合に、このサーバーの MCP ツールに適用するデフォルトの承認動作です。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "このサーバーの特定の MCP ツールに適用する承認動作の上書き設定です。",
    },
    {
      key: "mcp_servers.<id>.tools.<tool>.output_token_limit",
      type: "integer (positive)",
      description:
        "特定の MCP ツールの出力に割り当てるトークン予算です。シリアライズ用の標準の余裕分 20% を加える前の値です。そのツールについて、モデルがデフォルトで使用する出力切り詰めのトークン予算を上書きします。",
    },
    {
      key: "mcp_servers.<id>.scopes",
      type: "array<string>",
      description:
        "その MCP サーバーへの認証時に要求する OAuth スコープです。",
    },
    {
      key: "mcp_servers.<id>.oauth_resource",
      type: "string",
      description:
        "MCP へのログイン時に含める、任意指定の RFC 8707 OAuth リソースパラメーターです。",
    },
    {
      key: "mcp_servers.<id>.experimental_environment",
      type: "local | remote",
      description:
        "MCP サーバーの配置先を指定する試験的な設定です。`remote` は、リモートエグゼキューター環境を介して stdio サーバーを起動します。streamable HTTP のリモート配置は実装されていません。",
    },
    {
      key: "agents",
      type: "table",
      description:
        "マルチエージェントの設定とカスタムロール宣言です。スカラー設定の名前は予約されており、カスタムロール名には使用できません。",
    },
    {
      key: "agents.enabled",
      type: "boolean",
      description: "マルチエージェントツールを有効または無効にします。デフォルトは true です。",
    },
    {
      key: "agents.max_concurrent_threads_per_session",
      type: "number",
      description:
        "プライマリスレッドを除き、生成されたエージェントのスレッドを同時に開いておける最大数です。未設定の場合は Codex がデフォルト値を選択します。",
    },
    {
      key: "agents.max_threads",
      type: "number",
      description:
        "`agents.max_concurrent_threads_per_session` の従来の別名です。",
    },
    {
      key: "agents.default_subagent_model",
      type: "string",
      description:
        "生成するエージェントのデフォルトモデルです。生成時にモデルが明示的に指定されている場合は、その指定が優先されます。",
    },
    {
      key: "agents.default_subagent_reasoning_effort",
      type: "string",
      description:
        "生成するエージェントのデフォルトの推論強度です。生成時に推論強度が明示的に指定されている場合は、その指定が優先されます。",
    },
    {
      key: "agents.interrupt_message",
      type: "boolean",
      description:
        "エージェントのターンが中断されたときに、モデルから参照できるメッセージを記録します。デフォルトは true です。",
    },
    {
      key: "agents.<name>.description",
      type: "string",
      description:
        "そのエージェント種別を選択して生成するときに Codex に提示される、ロールに関するガイダンスです。",
    },
    {
      key: "agents.<name>.config_file",
      type: "string (path)",
      description:
        "そのロール用の TOML 構成レイヤーへのパスです。相対パスは、ロールを宣言している設定ファイルを基準に解決されます。",
    },
    {
      key: "memories.generate_memories",
      type: "boolean",
      description:
        "`false` の場合、新しく作成されたスレッドはメモリ生成の入力として保存されません。デフォルトは `true` です。",
    },
    {
      key: "memories.use_memories",
      type: "boolean",
      description:
        "`false` の場合、Codex は既存のメモリを今後のセッションに組み込みません。デフォルトは `true` です。",
    },
    {
      key: "memories.disable_on_external_context",
      type: "boolean",
      description:
        "`true` の場合、MCP ツール呼び出し、ウェブ検索、ツール検索などの外部コンテキストを使用するスレッドをメモリ生成の対象から除外します。デフォルトは `false` です。従来のエイリアスは `memories.no_memories_if_mcp_or_web_search` です。",
    },
    {
      key: "memories.max_raw_memories_for_consolidation",
      type: "number",
      description:
        "全体の統合に向けて保持する、最近の未加工メモリの最大数です。デフォルトは `256`、上限は `4096` です。",
    },
    {
      key: "memories.max_unused_days",
      type: "number",
      description:
        "メモリを統合対象に含めるための、最終使用日からの最大経過日数です。デフォルトは `30` で、`0`～`365` の範囲に制限されます。",
    },
    {
      key: "memories.max_rollout_age_days",
      type: "number",
      description:
        "メモリ生成の対象となるスレッドの最大経過期間です。デフォルトは `30` で、`0`～`90` の範囲に制限されます。",
    },
    {
      key: "memories.max_rollouts_per_startup",
      type: "number",
      description:
        "起動時の 1 回の処理で扱うロールアウト候補の最大数です。デフォルトは `16`、上限は `128` です。",
    },
    {
      key: "memories.min_rollout_idle_hours",
      type: "number",
      description:
        "スレッドがメモリ生成の対象となるまでに必要な最小アイドル時間です。デフォルトは `6` で、`1`～`48` の範囲に制限されます。",
    },
    {
      key: "memories.min_rate_limit_remaining_percent",
      type: "number",
      description:
        "メモリ生成を開始するために必要な、Codex のレート制限ウィンドウにおける残量の最小割合です。デフォルトは `25` で、`0`～`100` の範囲に制限されます。",
    },
    {
      key: "memories.extract_model",
      type: "string",
      description: "スレッドごとのメモリ抽出に使用するモデルの上書き設定です（任意）。",
    },
    {
      key: "memories.consolidation_model",
      type: "string",
      description: "全体のメモリ統合に使用するモデルの上書き設定です（任意）。",
    },
    {
      key: "features.unified_exec",
      type: "boolean",
      description:
        "PTY を使用する統合 exec ツールを使用します（安定版、Windows を除きデフォルトで有効）。",
    },
    {
      key: "features.shell_snapshot",
      type: "boolean",
      description:
        "シェル環境のスナップショットを作成し、コマンドの繰り返し実行を高速化します（安定版、デフォルトで有効）。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description:
        "マルチエージェントの連携ツール（`spawn_agent`、`send_input`、`resume_agent`、`wait_agent`、`close_agent`）を有効にします（安定版、デフォルトで有効）。",
    },
    {
      key: "features.goals",
      type: "boolean",
      description:
        "目標の永続化と自動継続を有効にします（安定版、デフォルトで有効）。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description: "リモートプラグインカタログを有効にします（安定版、デフォルトで有効）。",
    },
    {
      key: "features.personality",
      type: "boolean",
      description:
        "パーソナリティの選択 UI を有効にします（安定版、デフォルトで有効）。",
    },
    {
      key: "features.network_proxy",
      type: "boolean | table",
      description:
        "サンドボックス内で実行するコマンド用のネットワークプロキシを起動します（実験的機能、デフォルトでは無効）。管理者が管理する `experimental_network` 要件が有効で、その要件によってプロキシが起動される場合を除き、権限プロファイルのドメインルールを適用するにはこの設定が必要です。`domains` などの機能レベルのポリシーオプションを設定する場合は、テーブル形式を使用してください。ウェブ検索、アプリ、MCP、その他のホスト型ツールはフィルタリングされません。",
    },
    {
      key: "features.network_proxy.enabled",
      type: "boolean",
      description:
        "コマンドのネットワークアクセスが有効な場合に、サンドボックス内で実行するコマンド用のネットワークプロキシを起動します。デフォルトは `false` です。プロキシが無効な間は、権限プロファイルのドメインルールは適用されません。",
    },
    {
      key: "features.network_proxy.domains",
      type: "map<string, allow | deny>",
      description:
        "サンドボックス内のネットワーク接続に適用されるドメインポリシーです。デフォルトでは未設定で、`allow` ルールを追加するまで外部の宛先は許可されません。ホストへの完全一致、サブドメインのみに一致する `*.example.com`、ドメイン自体とサブドメインに一致する `**.example.com`、すべてのホストに一致する `*` の許可ルールをサポートします。`*` を使用すると、パブリックネットワークへのアウトバウンドアクセスが広範に開放されるため、範囲を限定したルールを推奨します。ブロックする宛先には `deny` ルールを追加します。競合した場合は `deny` が優先されます。",
    },
    {
      key: "features.network_proxy.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "サンドボックス内のネットワーク接続に適用される Unix ソケットポリシーです。デフォルトでは未設定です。許可するソケットには `allow` エントリを追加してください。",
    },
    {
      key: "features.network_proxy.allow_local_binding",
      type: "boolean",
      description:
        "より広範なローカル／プライベートネットワークへのアクセスを許可します。デフォルトは `false` です。ただし、ローカル IP アドレスのリテラルまたは `localhost` に完全一致する許可ルールを使用すれば、特定のローカル宛先へのアクセスを許可できます。",
    },
    {
      key: "features.network_proxy.enable_socks5",
      type: "boolean",
      description: "SOCKS5 サポートを有効にします。デフォルトは `true` です。",
    },
    {
      key: "features.network_proxy.enable_socks5_udp",
      type: "boolean",
      description: "SOCKS5 経由の UDP 通信を許可します。デフォルトは `true` です。",
    },
    {
      key: "features.network_proxy.allow_upstream_proxy",
      type: "boolean",
      description:
        "環境で設定されたアップストリームプロキシを経由する多段接続を許可します。デフォルトは `true` です。",
    },
    {
      key: "features.network_proxy.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "ループバック以外のリスナーアドレスを許可します。デフォルトは `false` です。有効にすると、localhost 以外からもプロキシリスナーにアクセスできるようになる可能性があります。",
    },
    {
      key: "features.network_proxy.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "許可リストに含まれる宛先だけに限定せず、任意の Unix ソケット宛先を許可します。デフォルトは `false` です。厳密に管理された環境でのみ使用してください。",
    },
    {
      key: "features.network_proxy.proxy_url",
      type: "string",
      description:
        "サンドボックス内のネットワーク接続に使用する HTTP リスナー URL です。デフォルトは `\"http://127.0.0.1:3128\"` です。",
    },
    {
      key: "features.network_proxy.socks_url",
      type: "string",
      description:
        "SOCKS5 リスナー URL です。デフォルトは `\"http://127.0.0.1:8081\"` です。",
    },
    {
      key: "features.web_search",
      type: "boolean",
      description:
        "従来の切り替え設定です（非推奨）。代わりにトップレベルの `web_search` 設定を使用してください。",
    },
    {
      key: "features.web_search_cached",
      type: "boolean",
      description:
        "従来の切り替え設定です（非推奨）。`web_search` が未設定の場合、true は `web_search = \"cached\"` に対応します。",
    },
    {
      key: "features.web_search_request",
      type: "boolean",
      description:
        "従来の切り替え設定です（非推奨）。`web_search` が未設定の場合、true は `web_search = \"live\"` に対応します。",
    },
    {
      key: "features.shell_tool",
      type: "boolean",
      description:
        "コマンド実行用のデフォルトの `shell` ツールを有効にします（安定版、デフォルトで有効）。",
    },
    {
      key: "features.enable_request_compression",
      type: "boolean",
      description:
        "サポートされている場合、ストリーミングリクエストのボディを zstd で圧縮します（安定版、デフォルトで有効）。",
    },
    {
      key: "features.skill_mcp_dependency_install",
      type: "boolean",
      description:
        "スキルに必要な MCP 依存関係が不足している場合に、確認プロンプトの表示とインストールを許可します（安定版、デフォルトで有効）。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "TUI でモデルカタログのサービスティアを選択できるようにします（安定版、デフォルトで有効）。使用中のモデルが対応を示している場合は、Fast ティアのコマンドも有効にします。",
    },
    {
      key: "features.prevent_idle_sleep",
      type: "boolean",
      description:
        "ターンの実行中にマシンがスリープしないようにします（実験的機能、デフォルトでは無効）。",
    },
    {
      key: "suppress_unstable_features_warning",
      type: "boolean",
      description:
        "開発中の機能フラグを有効にしたときに表示される警告を抑制します。",
    },
    {
      key: "model_providers.<id>",
      type: "table",
      description:
        "カスタムプロバイダーの定義です。組み込みプロバイダーの ID（`openai`、`ollama`、`lmstudio`）は予約済みであり、上書きできません。",
    },
    {
      key: "model_providers.<id>.name",
      type: "string",
      description: "カスタムモデルプロバイダーの表示名です。",
    },
    {
      key: "model_providers.<id>.base_url",
      type: "string",
      description: "モデルプロバイダーの API ベース URL です。",
    },
    {
      key: "model_providers.<id>.env_key",
      type: "string",
      description: "プロバイダーの API キーを指定する環境変数です。",
    },
    {
      key: "model_providers.<id>.env_key_instructions",
      type: "string",
      description: "プロバイダーの API キーに関するセットアップ案内です（任意）。",
    },
    {
      key: "model_providers.<id>.experimental_bearer_token",
      type: "string",
      description:
        "プロバイダーに直接指定する Bearer トークンです（非推奨。代わりに `env_key` を使用してください）。",
    },
    {
      key: "model_providers.<id>.requires_openai_auth",
      type: "boolean",
      description:
        "プロバイダーで OpenAI 認証を使用します（デフォルト：false）。",
    },
    {
      key: "model_providers.<id>.wire_api",
      type: "responses",
      description:
        "プロバイダーが使用するプロトコルです。サポートされている値は `responses` のみで、省略した場合もデフォルトでこの値が使用されます。",
    },
    {
      key: "model_providers.<id>.query_params",
      type: "map<string,string>",
      description: "プロバイダーへのリクエストに追加するクエリパラメーターです。",
    },
    {
      key: "model_providers.<id>.http_headers",
      type: "map<string,string>",
      description: "プロバイダーへのリクエストに追加する静的 HTTP ヘッダーです。",
    },
    {
      key: "model_providers.<id>.env_http_headers",
      type: "map<string,string>",
      description:
        "環境変数が存在する場合に、その値から設定される HTTP ヘッダーです。",
    },
    {
      key: "model_providers.<id>.request_max_retries",
      type: "number",
      description:
        "プロバイダーへの HTTP リクエストの再試行回数です（デフォルト：4 回）。",
    },
    {
      key: "model_providers.<id>.stream_max_retries",
      type: "number",
      description: "SSE ストリーミングが中断した場合の再試行回数です（デフォルト：5 回）。",
    },
    {
      key: "model_providers.<id>.stream_idle_timeout_ms",
      type: "number",
      description:
        "SSE ストリームのアイドルタイムアウトです（ミリ秒、デフォルト：300000）。",
    },
    {
      key: "model_providers.<id>.supports_websockets",
      type: "boolean",
      description:
        "プロバイダーが Responses API の WebSocket トランスポートに対応しているかどうかを指定します。",
    },
    {
      key: "model_providers.<id>.supports_standalone_web_search",
      type: "boolean",
      description:
        "互換性のあるスタンドアロンのウェブ検索エンドポイントへの対応を宣言します（デフォルト：false）。スタンドアロン検索は開発中であり、デフォルトでは無効です。プロバイダーが対応しているだけでは有効になりません。",
    },
    {
      key: "model_providers.<id>.auth",
      type: "table",
      description:
        "カスタムプロバイダーで、コマンドを使って Bearer トークンを取得するための設定です。`env_key`、`experimental_bearer_token`、`requires_openai_auth` と併用しないでください。",
    },
    {
      key: "model_providers.<id>.auth.command",
      type: "string",
      description:
        "Codex が Bearer トークンを必要とするときに実行するコマンドです。このコマンドはトークンを stdout に出力する必要があります。",
    },
    {
      key: "model_providers.<id>.auth.args",
      type: "array<string>",
      description: "トークン取得コマンドに渡す引数です。",
    },
    {
      key: "model_providers.<id>.auth.timeout_ms",
      type: "number",
      description:
        "トークン取得コマンドの最大実行時間です（ミリ秒、デフォルト：5000）。",
    },
    {
      key: "model_providers.<id>.auth.refresh_interval_ms",
      type: "number",
      description:
        "Codex がトークンを事前に更新する間隔です（ミリ秒、デフォルト：300000）。認証の再試行後にのみ更新するには `0` に設定します。",
    },
    {
      key: "model_providers.<id>.auth.cwd",
      type: "string (path)",
      description: "トークン取得コマンドの作業ディレクトリです。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.profile",
      type: "string",
      description:
        "組み込みの `amazon-bedrock` プロバイダーで使用する AWS プロファイル名です。",
    },
    {
      key: "model_providers.amazon-bedrock.aws.region",
      type: "string",
      description: "組み込みの `amazon-bedrock` プロバイダーで使用する AWS リージョンです。",
    },
    {
      key: "model_reasoning_effort",
      type: "minimal | low | medium | high | xhigh",
      description:
        "対応モデルの推論強度を調整します（Responses API のみ。`xhigh` が利用できるかはモデルによって異なります）。",
    },
    {
      key: "plan_mode_reasoning_effort",
      type: "none | minimal | low | medium | high | xhigh",
      description:
        "プランモード専用の推論強度の上書き設定です。未設定の場合、プランモードでは組み込みプリセットのデフォルト値が使用されます。",
    },
    {
      key: "model_reasoning_summary",
      type: "auto | concise | detailed | none",
      description:
        "推論要約の詳細度を選択するか、要約を完全に無効にします。",
    },
    {
      key: "model_verbosity",
      type: "low | medium | high",
      description:
        "GPT-5 Responses API の出力の詳細度を任意で上書きする設定です。未設定の場合、選択したモデルまたはプリセットのデフォルト値が使用されます。",
    },
    {
      key: "model_supports_reasoning_summaries",
      type: "boolean",
      description: "Codex が推論メタデータを送信するかどうかを強制的に指定します。",
    },
    {
      key: "shell_environment_policy.inherit",
      type: "all | core | none",
      description:
        "サブプロセスの起動時に環境変数を継承するための基本方針です。",
    },
    {
      key: "shell_environment_policy.ignore_default_excludes",
      type: "boolean",
      description:
        "他のフィルターを適用する前に、名前に KEY、SECRET、TOKEN を含む変数を保持します（デフォルト：true）。シークレットを示す変数名を自動的に除外するには、false に設定します。",
    },
    {
      key: "shell_environment_policy.filters",
      type: "map<string, include | exclude>",
      description:
        "大文字と小文字を区別しない、標準形式の環境変数パターンフィルターです。含める対象のエントリは許可リストを作成しますが、除外された値を復元することはできません。明示的な `set` の値は、除外処理の後に適用されます。同じレイヤーで、フィルターと従来の `exclude` または `include_only` 配列を併用しないでください。",
    },
    {
      key: "shell_environment_policy.exclude",
      type: "array<string>",
      description:
        "従来の環境変数の除外パターンです。新しい構成では `shell_environment_policy.filters` を使用してください。同じレイヤーで両方の形式を併用しないでください。",
    },
    {
      key: "shell_environment_policy.include_only",
      type: "array<string>",
      description:
        "従来の環境変数パターンの許可リストです。新しい構成では `shell_environment_policy.filters` を使用してください。同じレイヤーで両方の形式を併用しないでください。",
    },
    {
      key: "shell_environment_policy.set",
      type: "map<string,string>",
      description:
        "除外処理の後に明示的に追加する環境変数の値です。これらの値も、含める対象を指定するフィルターによって削除される場合があります。",
    },
    {
      key: "shell_environment_policy.experimental_use_profile",
      type: "boolean",
      description: "サブプロセスの起動時に、ユーザーのシェルプロファイルを使用します。",
    },
    {
      key: "project_root_markers",
      type: "array<string>",
      description:
        "プロジェクトルートの判定に使うマーカーファイル名のリストです。親ディレクトリをたどってプロジェクトルートを探すときに使用します。",
    },
    {
      key: "project_doc_max_bytes",
      type: "number",
      description:
        "プロジェクトの指示を組み立てる際に `AGENTS.md` から読み込む最大バイト数です。",
    },
    {
      key: "project_doc_fallback_filenames",
      type: "array<string>",
      description: "`AGENTS.md` がない場合に追加で探すファイル名です。",
    },
    {
      key: "history.persistence",
      type: "save-all | none",
      description:
        "Codex がセッションの記録を history.jsonl に保存するかどうかを制御します。",
    },
    {
      key: "tool_output_token_limit",
      type: "number",
      description:
        "個々のツールや関数の出力を履歴に保存する際のトークン数の上限です。",
    },
    {
      key: "background_terminal_max_timeout",
      type: "number",
      description:
        "空の `write_stdin` ポーリング（バックグラウンド ターミナルのポーリング）の最大待機時間（ミリ秒）です。デフォルトは `300000`（5 分）です。従来の `background_terminal_timeout` キーに代わる設定です。",
    },
    {
      key: "history.max_bytes",
      type: "number",
      description:
        "設定すると、古いエントリから順に削除し、履歴ファイルのサイズを指定したバイト数以内に制限します。",
    },
    {
      key: "file_opener",
      type: "vscode | vscode-insiders | windsurf | cursor | none",
      description:
        "Codex の出力に含まれる引用を開くための URI スキームです（デフォルト：`vscode`）。",
    },
    {
      key: "otel.environment",
      type: "string",
      description:
        "送出される OpenTelemetry イベントに適用する環境タグです（デフォルト：`dev`）。",
    },
    {
      key: "otel.exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry エクスポーターを選択し、必要に応じてエンドポイントのメタデータを指定します。",
    },
    {
      key: "otel.trace_exporter",
      type: "none | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry トレースエクスポーターを選択し、必要に応じてエンドポイントのメタデータを指定します。",
    },
    {
      key: "otel.metrics_exporter",
      type: "none | statsig | otlp-http | otlp-grpc",
      description:
        "OpenTelemetry メトリクスエクスポーターを選択します（デフォルト：`statsig`）。",
    },
    {
      key: "otel.log_user_prompt",
      type: "boolean",
      description:
        "未加工のユーザープロンプトを OpenTelemetry ログとともにエクスポートする機能を有効にします。",
    },
    {
      key: "otel.exporter.<id>.endpoint",
      type: "string",
      description: "OTEL ログ用エクスポーターのエンドポイントです。",
    },
    {
      key: "otel.exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP エクスポーターが使用するプロトコルです。",
    },
    {
      key: "otel.exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL エクスポーターのリクエストに含める静的ヘッダーです。",
    },
    {
      key: "otel.trace_exporter.<id>.endpoint",
      type: "string",
      description: "OTEL ログ用トレースエクスポーターのエンドポイントです。",
    },
    {
      key: "otel.trace_exporter.<id>.protocol",
      type: "binary | json",
      description: "OTLP/HTTP トレースエクスポーターが使用するプロトコルです。",
    },
    {
      key: "otel.trace_exporter.<id>.headers",
      type: "map<string,string>",
      description: "OTEL トレースエクスポーターのリクエストに含める静的ヘッダーです。",
    },
    {
      key: "otel.exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL エクスポーターの TLS 接続で使用する CA 証明書のパスです。",
    },
    {
      key: "otel.exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL エクスポーターの TLS 接続で使用するクライアント証明書のパスです。",
    },
    {
      key: "otel.exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL エクスポーターの TLS 接続で使用するクライアント秘密鍵のパスです。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.ca-certificate",
      type: "string",
      description: "OTEL トレースエクスポーターの TLS 接続で使用する CA 証明書のパスです。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-certificate",
      type: "string",
      description: "OTEL トレースエクスポーターの TLS 接続で使用するクライアント証明書のパスです。",
    },
    {
      key: "otel.trace_exporter.<id>.tls.client-private-key",
      type: "string",
      description: "OTEL トレースエクスポーターの TLS 接続で使用するクライアント秘密鍵のパスです。",
    },
    {
      key: "desktop.custom_file_handlers.<id>",
      type: "table",
      description:
        "ユーザーレベルでのみ使用できます。ChatGPT デスクトップアプリの **アプリで開く** メニューに追加する項目を定義します。例とハンドラー ID の制約については、[カスタムファイルハンドラーの追加](/codex/config-file/config-advanced#add-custom-file-handlers) を参照してください。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.label",
      type: "string",
      description: "**アプリで開く** メニューに表示される名前です。必須です。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.icon",
      type: "string",
      description:
        "ハンドラーのアイコンには、バンドル済みアセットのパス、Base64 エンコードされた `data:image/...` URL、ファイル URI、またはローカルの絶対パスを指定します。必須です。サポートされていないソースの場合は、デフォルトの VS Code アイコンを使用します。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.command",
      type: "string",
      description:
        "検出して起動する実行可能ファイルのパスまたはコマンド名です。必須です。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.args",
      type: "array<string>",
      description:
        "コマンドとファイル入力の間に挿入する引数です（デフォルト：`[]`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.input",
      type: "path | json_argument | json_stdin",
      description:
        "アプリがハンドラーにファイル入力を渡す方法です（デフォルト：`path`）。",
    },
    {
      key: "desktop.custom_file_handlers.<id>.supports_ssh",
      type: "boolean",
      description:
        "SSH ワークスペース内のファイルで、このハンドラーを選択可能にします（デフォルト：`false`）。",
    },
    {
      key: "tui",
      type: "table",
      description:
        "インラインのデスクトップ通知の有効化など、TUI 固有のオプションです。",
    },
    {
      key: "tui.notifications",
      type: "boolean | array<string>",
      description:
        "TUI 通知を有効にします。必要に応じて、特定のイベントタイプに限定できます。",
    },
    {
      key: "tui.notification_method",
      type: "auto | osc9 | bel",
      description:
        "ターミナル通知の送信方式です（デフォルト：auto）。",
    },
    {
      key: "tui.notification_condition",
      type: "unfocused | always",
      description:
        "TUI 通知を、ターミナルにフォーカスがない場合のみ送信するか、フォーカスの有無にかかわらず送信するかを制御します。デフォルトは `unfocused` です。",
    },
    {
      key: "tui.animations",
      type: "boolean",
      description:
        "ターミナルのアニメーション（ウェルカム画面、シマー、スピナー）を有効にします（デフォルト：true）。",
    },
    {
      key: "tui.alternate_screen",
      type: "auto | always | never",
      description:
        "TUI で代替画面を使用するかどうかを制御します。デフォルトは auto です。auto の場合、Zellij ではスクロールバックを保持するため代替画面を使用しません。",
    },
    {
      key: "tui.resume_cwd",
      type: "current | session",
      description:
        "セッションを再開またはフォークするときに使用する作業ディレクトリです。未設定の場合、現在のディレクトリがセッションに保存されたディレクトリと異なると、Codex が使用するディレクトリの選択を求めます。",
    },
    {
      key: "tui.vim_mode_default",
      type: "boolean",
      description:
        "コンポーザーを、挿入モードではなく Vim のノーマルモードで起動します（デフォルト：false）。セッションごとに `/vim` で切り替えることもできます。",
    },
    {
      key: "tui.raw_output_mode",
      type: "boolean",
      description:
        "ターミナル上で範囲を選択してコピーしやすくするため、TUI を raw スクロールバックモードで起動します（デフォルト：false）。`/raw` またはデフォルトの `alt-r` キーバインドで切り替えられます。",
    },
    {
      key: "tui.show_tooltips",
      type: "boolean",
      description:
        "TUI のウェルカム画面にオンボーディングのツールチップを表示します（デフォルト：true）。",
    },
    {
      key: "tui.status_line",
      type: "array<string> | null",
      description:
        "TUI フッターのステータス行に表示する項目識別子を順番に並べたリストです。`null` を指定すると、ステータス行が無効になります。",
    },
    {
      key: "tui.terminal_title",
      type: "array<string> | null",
      description:
        "ターミナルのウィンドウ／タブのタイトルに表示する項目識別子を順番に並べたリストです。デフォルトは `[\"spinner\", \"project\"]` です。`null` を指定すると、タイトルの更新が無効になります。",
    },
    {
      key: "tui.theme",
      type: "string",
      description:
        "構文ハイライトのテーマを上書きします（ケバブケースのテーマ名）。",
    },
    {
      key: "tui.keymap.<context>.<action>",
      type: "string | array<string>",
      description:
        "TUI アクションに割り当てるキーボードショートカットです。サポートされるコンテキストには、`global`、`chat`、`composer`、`editor`、`vim_normal`、`vim_operator`、`vim_text_object`、`pager`、`list`、`approval` があります。一部のコンポーザーアクションでは、対応する `tui.keymap.global` の割り当てがフォールバックとして使用されます。サポートされている場合は、コンテキスト固有の割り当てが優先されます。",
    },
    {
      key: "tui.keymap.<context>.<action> = []",
      type: "empty array",
      description:
        "そのキーマップのコンテキストで、アクションの割り当てを解除します。キー名には、`ctrl-a`、`shift-enter`、`page-down`、`minus` などの正規化された文字列を使用します。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled",
      type: "boolean",
      description:
        "プラグインのマニフェストを変更せずに、インストール済みプラグインに同梱された MCP サーバーを有効または無効にします。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.default_tools_approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "プラグインが提供する MCP サーバー上のツールに対するデフォルトの承認動作です。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.enabled_tools",
      type: "array<string>",
      description:
        "プラグインが提供する MCP サーバーから公開されるツールの許可リストです。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.disabled_tools",
      type: "array<string>",
      description:
        "プラグインが提供する MCP サーバーで、`enabled_tools` の後に適用する拒否リストです。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description:
        "プラグインが提供する MCP ツールの承認動作をツールごとに上書きします。",
    },
    {
      key: "tui.model_availability_nux.<model>",
      type: "integer",
      description: "モデルのスラッグをキーとする起動時ツールチップの内部状態です。",
    },
    {
      key: "hide_agent_reasoning",
      type: "boolean",
      description:
        "TUI と `codex exec` の両方の出力で推論イベントを抑制します。",
    },
    {
      key: "show_raw_agent_reasoning",
      type: "boolean",
      description:
        "アクティブなモデルが未加工の推論内容を出力した場合に、それを表示します。",
    },
    {
      key: "disable_paste_burst",
      type: "boolean",
      description: "TUI のバーストペースト検出を無効にします。",
    },
    {
      key: "windows_wsl_setup_acknowledged",
      type: "boolean",
      description: "Windows の初期設定ガイドを確認済みかどうかを記録します（Windows のみ）。",
    },
    {
      key: "chatgpt_base_url",
      type: "string",
      description: "ChatGPT のログインフローで使用するベース URL を上書きします。",
    },
    {
      key: "cli_auth_credentials_store",
      type: "file | keyring | auto",
      description:
        "CLI が認証情報をキャッシュする保存先を指定します（auth.json ファイルまたは OS のキーチェーン）。",
    },
    {
      key: "mcp_oauth_credentials_store",
      type: "auto | file | keyring",
      description: "MCP OAuth 認証情報の優先保存先です。",
    },
    {
      key: "mcp_oauth_callback_port",
      type: "integer",
      description:
        "MCP OAuth ログインで使用するローカル HTTP コールバックサーバーの固定ポートをグローバルに指定します（任意）。サーバー固有の `oauth.callback_port` が優先されます。どちらも設定されていない場合、Codex は OS が選択した一時ポートにバインドします。",
    },
    {
      key: "mcp_oauth_callback_url",
      type: "string",
      description:
        "MCP OAuth ログイン用のベースコールバック URL です（任意）。devbox のイングレス URL などを指定します。認可サーバーが発行者の識別に対応している場合、新しく追加した事前登録済みクライアントはこの URL をそのまま使用します。コールバックが保存されていない既存のクライアントは、サーバー固有のコールバック ID を追加します。発行者の識別に対応していない場合、設定済みのコールバックに必要な ID がない事前登録済み MCP サーバーは、この URL に ID を追加したものにフォールバックします。コールバック URL のポート番号では、リスナーのポートは指定されません。",
    },
    {
      key: "experimental_use_unified_exec_tool",
      type: "boolean",
      description:
        "統合実行を有効にするための旧名称です。`[features].unified_exec` または `codex --enable unified_exec` を使用してください。",
    },
    {
      key: "tools.web_search",
      type: 'boolean | { context_size = "low|medium|high", allowed_domains = [string], location = { country, region, city, timezone } }',
      description:
        "ウェブ検索ツールの構成です（任意）。オブジェクト形式では、検索コンテキストのサイズ、検索を許可するドメイン、ユーザーのおおよその位置を設定できます。これらの検索ドメインフィルターは、サンドボックス内で実行するコマンドのネットワークドメインルールとは別であり、コネクタや MCP サーバーを制限しません。",
    },
    {
      key: "tools.view_image",
      type: "boolean",
      description: "ローカル画像を添付するツール `view_image` を有効にします。",
    },
    {
      key: "web_search",
      type: "disabled | cached | indexed | live",
      description:
        "ウェブ検索モードです（デフォルト：`\"cached\"`。cached は外部ウェブにアクセスせず、OpenAI が管理するインデックスを使用します。indexed は検索インデックスで許可された場合に限り外部アクセスを認めます。`--yolo` または他のフルアクセスのサンドボックス設定を使用する場合、デフォルトは `\"live\"` になります）。制限のないリアルタイム取得には `\"live\"` を、ツールを削除するには `\"disabled\"` を使用します。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "サンドボックス内のツール呼び出しに適用するデフォルト権限プロファイルの名前です。組み込みのプロファイルは `:read-only`、`:workspace`、`:danger-full-access` です。カスタムプロファイル名には、対応する `[permissions.<name>]` テーブルが必要です。`sandbox_mode` または `[sandbox_workspace_write]` と併用しないでください。",
    },
    {
      key: "permissions.<name>.description",
      type: "string",
      description:
        "この名前付きプロファイルの説明文です。`extends` を使用しても、親プロファイルの説明は継承されません。",
    },
    {
      key: "permissions.<name>.extends",
      type: "string",
      description:
        "この名前付きプロファイルより先に適用する親プロファイルです（任意）。別の名前付きプロファイル、`:read-only`、または `:workspace` を指定します。`:danger-full-access`、未定義の親プロファイル、循環参照は拒否されます。",
    },
    {
      key: "permissions.<name>.workspace_roots",
      type: "table",
      description:
        "プロファイルで定義するワークスペースルートです。セッション実行時のワークスペースルートとともに、`:workspace_roots` のファイルシステムルールが適用されます。",
    },
    {
      key: "permissions.<name>.workspace_roots.<path>",
      type: "boolean",
      description:
        "`true` の場合、そのパスをプロファイルのワークスペースルートに追加します。無効化されたエントリは適用されません。",
    },
    {
      key: "permissions.<name>.filesystem",
      type: "table",
      description:
        "名前付きのファイルシステム権限プロファイルです。各キーには、絶対パス、または `:minimal` や `:workspace_roots` などの特殊トークンを指定します。",
    },
    {
      key: "permissions.<name>.filesystem.glob_scan_max_depth",
      type: "number",
      description:
        "サンドボックスの起動前に一致するパスのスナップショットを作成するプラットフォームで、読み取り拒否用の glob パターンを展開する際の最大深度です。設定する場合は `1` 以上にする必要があります。",
    },
    {
      key: "permissions.<name>.filesystem.<path-or-glob>",
      type: '"read" | "write" | "deny" | table',
      description:
        "パス、glob パターン、特殊トークンへの直接アクセスを許可するか、そのルート配下のネストされたエントリの適用範囲を設定します。一致するパスの読み取りを拒否するには `\"deny\"` を使用します。",
    },
    {
      key: 'permissions.<name>.filesystem.":workspace_roots".<subpath-or-glob>',
      type: '"read" | "write" | "deny"',
      description:
        "実際に適用される各ワークスペースルートを基準に、ファイルシステムアクセスの範囲を設定します。ルート自体には `\".\"` を使用します。`\"**/*.env\"` などの glob 形式のサブパスでは、`\"deny\"` によって読み取りを拒否できます。",
    },
    {
      key: "permissions.<name>.network.enabled",
      type: "boolean",
      description:
        "この権限プロファイルでコマンドのネットワークアクセスを有効にします。この設定ではネットワークプロキシは起動しません。`features.network_proxy` が有効でなく、管理者が管理するネットワーク要件も有効になっていない場合、コマンドはネットワークに直接アクセスし、プロファイルのドメインルールは適用されません。",
    },
    {
      key: "permissions.<name>.network.proxy_url",
      type: "string",
      description:
        "この権限プロファイルでサンドボックス内のネットワーク通信を有効にした場合に使用する HTTP リスナーの URL です。",
    },
    {
      key: "permissions.<name>.network.enable_socks5",
      type: "boolean",
      description:
        "この権限プロファイルでサンドボックス内のネットワーク通信を有効にした場合に、SOCKS5 を利用可能にします。",
    },
    {
      key: "permissions.<name>.network.socks_url",
      type: "string",
      description: "この権限プロファイルで使用する SOCKS5 プロキシのエンドポイントです。",
    },
    {
      key: "permissions.<name>.network.enable_socks5_udp",
      type: "boolean",
      description: "有効にすると、SOCKS5 リスナー経由の UDP 通信を許可します。",
    },
    {
      key: "permissions.<name>.network.allow_upstream_proxy",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク通信が別のアップストリームプロキシを経由することを許可します。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク通信のリスナーが、ループバック以外のアドレスにバインドすることを許可します。有効にすると、リスナーが localhost 以外からアクセス可能になる場合があります。",
    },
    {
      key: "permissions.<name>.network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "Unix ソケットの宛先をデフォルトの限定された範囲に制限せず、任意の宛先を許可します。厳格に管理された環境でのみ使用してください。",
    },
    {
      key: "permissions.<name>.network.mode",
      type: "limited | full",
      description: "サブプロセスのトラフィックに使用するネットワークプロキシモードです。",
    },
    {
      key: "permissions.<name>.network.domains",
      type: "table",
      description:
        "サンドボックス内で実行するコマンドのドメインルールです。`features.network_proxy`、または有効化された管理者管理のネットワーク要件によってプロキシが起動した場合にのみ適用されます。ホストの完全一致、`*.example.com`、`**.example.com`、すべてを対象とする `*` の許可ルールに対応し、`deny` が優先されます。ウェブ検索、アプリ、MCP サーバーは制限されません。",
    },
    {
      key: "permissions.<name>.network.domains.<pattern>",
      type: "allow | deny",
      description:
        "完全一致するホスト、または `*.example.com` や `**.example.com` などの範囲を限定したワイルドカードパターンを許可または拒否します。",
    },
    {
      key: "permissions.<name>.network.unix_sockets",
      type: "table",
      description:
        "サンドボックス内のネットワーク通信に適用する Unix ソケット許可リストのオーバーライド設定です。ソケットパスをキーとして使用し、`allow` でパスを追加し、`deny` で拒否します。",
    },
    {
      key: "permissions.<name>.network.unix_sockets.<path>",
      type: "allow | deny",
      description:
        "`allow` を使用して Unix ソケットの絶対パスを実際に適用される許可リストに追加するか、`deny` を使用して拒否します。拒否されたエントリは、実際に適用される許可リストから除外されます。",
    },
    {
      key: "permissions.<name>.network.allow_local_binding",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク通信を通じて、ローカルネットワークやプライベートネットワークへの広範なアクセスを許可します。この設定が `false` のままでも、ローカル IP アドレスのリテラルまたは `localhost` に完全一致する許可ルールによって、特定のローカル接続先へのアクセスを許可できます。",
    },
    {
      key: "projects.<path>.trust_level",
      type: "string",
      description:
        "プロジェクトまたは Worktree を信頼済みまたは未信頼としてマークします（`\"trusted\"` | `\"untrusted\"`）。未信頼のプロジェクトでは、プロジェクトローカルの構成、フック、ルールなど、プロジェクト単位の `.codex/` レイヤーがスキップされます。",
    },
    {
      key: "notice.hide_full_access_warning",
      type: "boolean",
      description: "フルアクセスの警告プロンプトを確認済みかどうかを記録します。",
    },
    {
      key: "notice.hide_world_writable_warning",
      type: "boolean",
      description:
        "Windows で全ユーザーが書き込み可能なディレクトリに関する警告を確認済みかどうかを記録します。",
    },
    {
      key: "notice.hide_rate_limit_model_nudge",
      type: "boolean",
      description: "レート制限に伴うモデル切り替えリマインダーのオプトアウト状態を記録します。",
    },
    {
      key: "notice.hide_gpt5_1_migration_prompt",
      type: "boolean",
      description: "GPT-5.1 移行プロンプトを確認済みかどうかを記録します。",
    },
    {
      key: "notice.hide_gpt-5.1-codex-max_migration_prompt",
      type: "boolean",
      description:
        "gpt-5.1-codex-max 移行プロンプトを確認済みかどうかを記録します。",
    },
    {
      key: "notice.model_migrations",
      type: "map<string,string>",
      description: "確認済みのモデル移行を old->new 形式のマッピングとして記録します。",
    },
    {
      key: "forced_login_method",
      type: "chatgpt | api",
      description: "Codex で使用できる認証方法を特定の方式に限定します。",
    },
    {
      key: "forced_chatgpt_workspace_id",
      type: "string (uuid)",
      description: "ChatGPT へのログインを特定のワークスペース識別子に限定します。",
    },
  ]}
  client:load
/>

`config.toml` の最新の JSON スキーマは[こちら](/codex/config-schema.json)で確認できます。

VS Code または Cursor で `config.toml` を編集する際に自動補完と診断を利用するには、[Even Better TOML](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) 拡張機能をインストールし、`config.toml` の先頭に次の行を追加してください：

```toml
#:schema https://developers.openai.com/codex/config-schema.json

注：`experimental_instructions_file` の名前を `model_instructions_file` に変更してください。Codex では古いキーが非推奨となっているため、既存の構成を新しい名前に更新してください。

## `requirements.toml`

`requirements.toml` は管理者が強制適用する構成ファイルで、セキュリティに関わる設定にユーザーが上書きできない制約を課します。詳細、配置場所、例については、[管理者が強制適用する要件](/ja-JP/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)を参照してください。

ChatGPT Business および ChatGPT Enterprise のユーザーには、Codex がクラウドから取得した要件も適用できます。優先順位の詳細は、セキュリティページを参照してください。

ランタイムの機能フラグを固定するには、`requirements.toml` の `[features]` を使用します。
使用する正規キーは `config.toml` と同じです。
要件には、`config.toml` の対象外となる、ドキュメントに記載されたアプリ専用キーも含められます。
省略したキーには制約が適用されません。

一部の管理対象要件では、許可リストを使わず、構成値を特定の値に固定します。ユーザーは、強制適用されたパス、更新設定、ログインシェルポリシー、フィードバック設定、Windows のプライベートデスクトップ設定を上書きできません。

管理対象の権限プロファイル許可リストを使用するには、Codex 0.138.0 以降が必要です。
Codex 0.137.0 以前では、`allowed_permission_profiles` と管理対象の `default_permissions` が
無視されます。

`allowed_sandbox_modes` は `sandbox_mode` と組み合わせて使用します。
権限プロファイルを導入する場合は、`allowed_permission_profiles` と
管理対象の `default_permissions` を組み合わせて使用します。

`[models.new_thread]` テーブルでは、管理対象のデフォルト値を指定しますが、値は強制されません。
専用の CLI フラグまたは `--config` によるオーバーライドで起動時に明示した設定が優先されます。
モデルまたは推論強度を明示的にオーバーライドすると、管理対象のモデルフィールドは両方ともスキップされます。
`service_tier` はこれらとは独立しています。

ブラウザ関連の要件は、3 つの異なる操作対象をカバーします。
`in_app_browser` は、ユーザーが開いて直接操作するブラウザペインを制御します。
`browser_use` は、エージェントによるブラウザ内の作業を制御します。
`computer_use` は、エージェントによるネイティブデスクトップアプリ内の作業を制御します。

ブラウザとコンピューターの使用に関するネストされたポリシー値は、それ自体でアクセスを許可するものではありません。
オリジンまたはアプリ固有の `allow` は、同じポリシーソースのフォールバック設定を上書きできますが、
通常の機能、承認、その他のポリシーのチェックは引き続き適用されます。
管理対象要件と `config.toml` の両方が適用される場合は、
どちらか一方の `deny` が優先されます。

<ConfigTable
  options={[
    {
      key: "sqlite_home",
      type: "string (path)",
      description:
        "Codex が SQLite ベースのランタイム状態を保存するディレクトリを固定します。",
    },
    {
      key: "log_dir",
      type: "string (path)",
      description: "Codex がローカルログファイルを書き込むディレクトリを固定します。",
    },
    {
      key: "model_catalog_json",
      type: "string (path)",
      description: "Codex が起動時に使用する JSON モデルカタログを固定します。",
    },
    {
      key: "check_for_update_on_startup",
      type: "boolean",
      description: "Codex が起動時に更新を確認するかどうかの設定を強制適用します。",
    },
    {
      key: "allow_login_shell",
      type: "boolean",
      description: "シェルツールがログインシェルを起動できるかどうかの設定を強制適用します。",
    },
    {
      key: "feedback",
      type: "table",
      description: "管理対象のフィードバック設定です。",
    },
    {
      key: "feedback.enabled",
      type: "boolean",
      description:
        "Codex のすべてのクライアントで、ユーザーがフィードバックを送信できるかどうかの設定を強制適用します。",
    },
    {
      key: "allowed_approval_policies",
      type: "array<string>",
      description:
        "`approval_policy` で許可される値（例：`untrusted`、`on-request`、`never`、`granular`）です。",
    },
    {
      key: "allowed_approvals_reviewers",
      type: "array<string>",
      description:
        "`approvals_reviewer` で許可される値（`user`、`auto_review` など）です。",
    },
    {
      key: "guardian_policy_config",
      type: "string",
      description:
        "自動レビューに使用する、管理対象の Markdown 形式のポリシー指示です。ローカルの `[auto_review].policy` より優先されます。空の値は無視されます。",
    },
    {
      key: "allowed_permission_profiles",
      type: "table<boolean>",
      description:
        "許可する権限プロファイルの完全なリストです。`true` に設定したプロファイルは許可されます。省略したプロファイルや `false` に設定したプロファイルは、将来のバージョンで追加されるものも含めて拒否されます。複数の要件ソースを組み合わせる場合、エントリはプロファイル名で照合されます。",
    },
    {
      key: "allowed_permission_profiles.<name>",
      type: "boolean",
      description:
        "読み込み済みの設定または要件ソースで定義された、組み込みまたはカスタムの権限プロファイルを許可または拒否します。後から適用される優先順位の高い要件ソースでは、`false` を使用して、先に適用された優先順位の低いソースで許可されたプロファイルを無効にできます。",
    },
    {
      key: "default_permissions",
      type: "string",
      description:
        "管理対象のデフォルト権限プロファイルです。このプロファイルは `allowed_permission_profiles` で許可されている必要があります。動作を予測しやすくするため、明示的に設定してください。省略した場合、Codex がデフォルトで `:workspace` を使用するのは、`:workspace` と `:read-only` の両方が明示的に許可されている場合のみです。",
    },
    {
      key: "enforce_residency",
      type: "string",
      description:
        "Codex サービスの通信に、サポートされているデータレジデンシーの使用を必須にします。現在は `us` を指定できます。",
    },
    {
      key: "models",
      type: "table",
      description:
        "新しいスレッドに適用する、管理対象のモデルのデフォルト設定です。これらの値はユーザーやプロジェクトのデフォルト設定より優先されますが、新しいスレッドで明示的に選択すれば上書きできます。",
    },
    {
      key: "models.new_thread",
      type: "table",
      description:
        "新しいローカルスレッドの開始時に適用するデフォルト設定です。各モデル設定は省略可能です。",
    },
    {
      key: "models.new_thread.model",
      type: "string",
      description:
        "新しいスレッドのデフォルトモデルです。`--model` またはモデルや推論に関する `--config` による明示的な上書きが優先されます。",
    },
    {
      key: "models.new_thread.model_reasoning_effort",
      type: "string",
      description:
        "新しいスレッドのデフォルトの推論強度です。モデルまたは推論強度を明示的に上書きすると、管理対象のモデル関連フィールドは両方とも適用されません。",
    },
    {
      key: "models.new_thread.service_tier",
      type: "string",
      description:
        "新しいスレッドのデフォルトのサービスティアです。サービスティアを明示的に上書きすると、モデル関連フィールドとは独立して、その値が優先されます。",
    },
    {
      key: "permissions",
      type: "table",
      description:
        "プロファイル名をキーとする、管理者定義の権限プロファイルです。`config.toml` と同じプロファイルフィールドを使用します。",
    },
    {
      key: "permissions.<name>",
      type: "table",
      description:
        "管理者が定義する権限プロファイルです。名前の先頭に `:` は使用できません。予約名 `filesystem` や、読み込み済みの設定にあるプロファイルと同じ名前も使用できません。`config.toml` と同じプロファイルフィールドを使用します。完全なプロファイルスキーマについては、権限ガイドを参照してください。",
    },
    {
      key: "allowed_sandbox_modes",
      type: "array<string>",
      description: "`sandbox_mode` に許可される値です。",
    },
    {
      key: "windows",
      type: "table",
      description: "ネイティブ Windows サンドボックスの要件です。",
    },
    {
      key: "windows.allowed_sandbox_implementations",
      type: "array<string>",
      description:
        "`windows.sandbox` で許可されるネイティブ Windows サンドボックスの実装（`elevated` と `unelevated`）です。リストを空にすることはできません。両方が許可されていてモードが選択されていない場合、Codex は `elevated` を優先します。",
    },
    {
      key: "windows.sandbox_private_desktop",
      type: "boolean",
      description:
        "ネイティブ Windows サンドボックスがプライベートデスクトップで子プロセスを起動するかどうかの設定を強制します。",
    },
    {
      key: "remote_sandbox_config",
      type: "array<table>",
      description:
        "ホスト固有のサンドボックス要件です。解決されたホスト名に `hostname_patterns` が一致する最初のエントリが、その要件ソースの最上位の `allowed_sandbox_modes` を上書きします。現在、ホスト固有のエントリが上書きするのはサンドボックスモードのみです。",
    },
    {
      key: "remote_sandbox_config[].hostname_patterns",
      type: "array<string>",
      description:
        "大文字と小文字を区別しないホスト名パターンです。任意の文字列に一致する `*` と、1 文字に一致する `?` に対応しています。",
    },
    {
      key: "remote_sandbox_config[].allowed_sandbox_modes",
      type: "array<string>",
      description:
        "このホスト固有のエントリに一致した場合に適用する、許可されたサンドボックスモードです。",
    },
    {
      key: "allowed_web_search_modes",
      type: "array<string>",
      description:
        "`web_search` に許可される値（`disabled`、`cached`、`indexed`、`live`）です。`disabled` は常に許可されます。空のリストを指定すると、実質的に `disabled` のみが許可されます。",
    },
    {
      key: "allow_managed_hooks_only",
      type: "boolean",
      description:
        "`true` の場合、Codex はユーザー、プロジェクト、セッション、プラグインの各フックをスキップしますが、`requirements.toml` およびその他の管理対象の設定レイヤーからの管理対象フックは引き続き許可します。",
    },
    {
      key: "allow_appshots",
      type: "boolean",
      description:
        "`false` に設定すると、管理対象ユーザーの Appshots が無効になります。省略した場合、Appshots は要件による制約を受けず、製品の通常の提供状況に従います。",
    },
    {
      key: "allow_remote_control",
      type: "boolean",
      description:
        "`false` に設定すると、管理対象ユーザーのデバイスのリモート制御が無効になります。省略した場合、デバイスのリモート制御は要件による制約を受けず、製品の通常の提供状況に従います。",
    },
    {
      key: "allow_browser_and_computer_use",
      type: "boolean",
      description:
        "`false` に設定すると、エージェントによるブラウザ操作と、ネイティブアプリでのコンピューターの使用の両方をブロックします。`true` に設定したり省略したりしても、どちらの機能も有効にはなりません。他の機能、ポリシー、承認のチェックは引き続き適用されます。",
    },
    {
      key: "features.plugin_sharing",
      type: "boolean",
      description:
        "クラウドで管理される `requirements.toml` で `false` に設定すると、ローカルでビルドしたプラグインのワークスペース内での共有が無効になります。",
    },
    {
      key: "features",
      type: "table",
      description:
        "機能の固定値です。ランタイム機能には `config.toml` の正規名を使用します。ここでは、ドキュメントに記載されたアプリ専用の要件キーにも対応しています。",
    },
    {
      key: "features.<name>",
      type: "boolean",
      description:
        "ドキュメントに記載されたランタイム機能またはアプリ機能を、有効または無効の状態に固定します。",
    },
    {
      key: "features.apps",
      type: "boolean",
      description:
        "管理対象ユーザー向けに、アプリ連携の利用可否を固定します。",
    },
    {
      key: "features.in_app_updates",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、アプリ内アップデートが無効になります。この要件を省略した場合、アップデートはデフォルトで有効なままです。",
    },
    {
      key: "features.in_app_browser",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、ユーザーが開いて直接操作する組み込みのブラウザペインが無効になります。",
    },
    {
      key: "features.browser_use",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、エージェントによるブラウザ操作が無効になります。",
    },
    {
      key: "features.browser_use_external",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、Codex は ChatGPT ブラウザ拡張機能を通じて対応ブラウザを操作できなくなります。既存のタブやサインイン済みのセッションの操作も対象です。",
    },
    {
      key: "features.browser_use_full_cdp_access",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、ブラウザ開発者モードを含むローカルランタイムでの Chrome DevTools Protocol へのフルアクセスが無効になり、ChatGPT デスクトップアプリで対応する設定を有効にできなくなります。省略した場合は、製品の通常の提供状況が適用されます。",
    },
    {
      key: "features.fast_mode",
      type: "boolean",
      description:
        "管理対象ユーザー向けに、正規の `fast_mode` 機能の有効・無効を固定します。",
    },
    {
      key: "features.guardian_approval",
      type: "boolean",
      description:
        "管理対象ユーザー向けに、Guardian 承認の利用可否を固定します。",
    },
    {
      key: "features.memories",
      type: "boolean",
      description: "管理対象ユーザー向けに、メモリの利用可否を固定します。",
    },
    {
      key: "features.multi_agent",
      type: "boolean",
      description: "管理対象ユーザー向けに、マルチエージェント機能の利用可否を固定します。",
    },
    {
      key: "features.plugins",
      type: "boolean",
      description: "管理対象ユーザー向けに、プラグインの利用可否を固定します。",
    },
    {
      key: "features.remote_plugin",
      type: "boolean",
      description:
        "管理対象ユーザー向けに、リモートプラグインカタログの利用可否を固定します。",
    },
    {
      key: "features.computer_use",
      type: "boolean",
      description:
        "`requirements.toml` で `false` に設定すると、コンピューターの使用、記録と再生、および関連するインストールや有効化のフローが無効になります。",
    },
    {
      key: "features.workspace_dependencies",
      type: "boolean",
      description:
        "管理対象ユーザー向けに、同梱のワークスペース依存関係用ランタイムの利用可否を固定します。",
    },
    {
      key: "in_app_browser",
      type: "table",
      description:
        "組み込みのブラウザペインに関する要件です。これらの設定は、エージェントによるブラウザ操作を制御しません。",
    },
    {
      key: "in_app_browser.allow_external_browser_settings_import",
      type: "boolean",
      description:
        "`false` に設定すると、ユーザーは外部ブラウザの設定や閲覧データを組み込みのブラウザにインポートできなくなります。`true` に設定するか省略した場合、製品の他のチェックで許可されれば、引き続きインポートできます。これは管理専用の設定で、`config.toml` で上書きすることはできません。",
    },
    {
      key: "browser_use",
      type: "table",
      description: "エージェントによるブラウザ操作に関する管理対象の要件です。",
    },
    {
      key: "browser_use.allow_history_access",
      type: "boolean",
      description:
        "`false` に設定すると、ブラウザ機能は閲覧履歴を読み取れなくなります。`true` に設定するか省略した場合、通常の履歴設定と利用可否のチェックが引き続き適用されます。",
    },
    {
      key: "browser_use.disable_auto_review",
      type: "boolean",
      description:
        "`true` に設定すると、ブラウザ機能の自動レビューをスキップし、代わりにユーザーに承認を求めます。`false` に設定するか省略した場合、他の設定で許可されていれば、自動レビューを引き続き利用できます。",
    },
    {
      key: "browser_use.allow_global_persistent_approval",
      type: "boolean",
      description:
        "`false` に設定すると、ブラウザ機能は、すべてのサイトからのダウンロードを許可する承認など、全サイトを対象とする `Always allow` 承認を作成したり適用したりできなくなります。保存済みの承認は無視されますが、削除されません。`true` に設定したり省略したりしても、承認が作成されることはありません。",
    },
    {
      key: "browser_use.default_origin_policy",
      type: "table",
      description:
        "`browser_use.origins` 内の一致するエントリに設定が定義されていない場合に使用する、ブラウザ機能の各設定のフォールバックです。一致するオリジンルールがあれば、そのソースのフォールバックは置き換えられます。その後、Codex は管理対象の要件とユーザー設定のうち、より厳しい結果を適用します。",
    },
    {
      key: "browser_use.default_origin_policy.access",
      type: "allow | deny",
      description:
        "`deny` を使用すると、フォールバックが適用されるオリジンでブラウザ機能をブロックします。拒否されたオリジンでは、アップロード、ダウンロード、ブラウザのデバッグ機能へのフルアクセス、自動レビューもブロックされます。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.default_origin_policy.downloads",
      type: "allow | deny",
      description:
        "`deny` を使用すると、フォールバックが適用されるオリジンでブラウザ機能によるダウンロードをブロックします。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.default_origin_policy.uploads",
      type: "allow | deny",
      description:
        "`deny` を使用すると、フォールバックが適用されるオリジンでブラウザ機能によるアップロードをブロックします。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.default_origin_policy.full_cdp_access",
      type: "allow | deny",
      description:
        "`deny` を使用すると、フォールバックが適用されるオリジンで Chrome DevTools Protocol（CDP）へのフルアクセスをブロックします。`allow` は、通常のオプトインと承認のチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.default_origin_policy.auto_review",
      type: "allow | deny",
      description:
        "`deny` を使用すると、フォールバックが適用されるオリジンで自動レビューをスキップし、代わりにユーザーに承認を求めます。`allow` の場合、他の設定で許可されていれば、自動レビューを引き続き利用できます。",
    },
    {
      key: "browser_use.default_origin_policy.persistent_approval",
      type: "boolean",
      description:
        "`false` に設定すると、ブラウザ機能は、フォールバックが適用されるオリジンで `Always allow` 承認を保存したり適用したりできなくなります。現在のターンまたはスレッドを対象とする承認は引き続き適用できます。`true` は、他の条件で許可されている場合に `Always allow` を利用可能にしますが、承認を作成することはありません。",
    },
    {
      key: "browser_use.default_origin_policy.access_approval_lifetime",
      type: "turn | thread",
      description:
        "永続化されないサイトアクセス承認の有効期間を設定します。`turn` は現在のターンに限定し、`thread` は現在のスレッドが終わるまで保持します。`Always allow` が利用可能かどうかは、`persistent_approval` で個別に制御します。製品のデフォルトは `thread` です。",
    },
    {
      key: "browser_use.origins",
      type: "map<string, table>",
      description:
        "オリジン固有のブラウザポリシーです。キーには `<scheme>://<host-pattern>[:<port>]` を使用し、スキームは `http` または `https` を指定します。ホストを完全一致で指定するか、サブドメインのみを対象とする `*.example.com`、ベースドメインとそのサブドメインを対象とする `**.example.com` を使用します。その他の `*` ワイルドカードはドットをまたいで一致するため、`region*.example.com` は `region.api.example.com` にも一致します。ホストに `*` を指定すると、そのスキームのすべてのホストに一致します。スキームとデフォルト以外のポートは区別されます。明示的に指定されたデフォルトポートは正規化によって除去されます。パス、クエリ、埋め込まれたユーザー名やパスワード、スキームやポートのワイルドカードは無効です。TOML では、`[browser_use.origins.\"https://**.example.com\"]` のようにパターンを引用符で囲みます。",
    },
    {
      key: "browser_use.origins.<pattern>",
      type: "table",
      description:
        "このパターンに一致するオリジンのポリシーです。複数のパターンが一致する場合、Codex は機能ごとに最も制限の厳しい値を使用します。`allow` より `deny`、`true` より `false`、`thread` より `turn` が優先されます。",
    },
    {
      key: "browser_use.origins.<pattern>.access",
      type: "allow | deny",
      description:
        "`deny` を使用すると、一致するオリジンでブラウザ機能をブロックします。拒否されたオリジンでは、アップロード、ダウンロード、ブラウザのデバッグ機能へのフルアクセス、自動レビューもブロックされます。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.origins.<pattern>.downloads",
      type: "allow | deny",
      description:
        "`deny` を使用すると、一致するオリジンでブラウザ機能によるダウンロードをブロックします。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.origins.<pattern>.uploads",
      type: "allow | deny",
      description:
        "`deny` を使用すると、一致するオリジンでブラウザ機能によるアップロードをブロックします。`allow` は、通常の承認とポリシーのチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.origins.<pattern>.full_cdp_access",
      type: "allow | deny",
      description:
        "`deny` を使用すると、一致するオリジンで Chrome DevTools Protocol（CDP）へのフルアクセスをブロックします。`allow` は、通常のオプトインと承認のチェックを続行できるようにするだけです。",
    },
    {
      key: "browser_use.origins.<pattern>.auto_review",
      type: "allow | deny",
      description:
        "`deny` を使用すると、一致するオリジンで自動レビューをスキップし、代わりにユーザーに承認を求めます。`allow` の場合、他の設定で許可されていれば、自動レビューを引き続き利用できます。",
    },
    {
      key: "browser_use.origins.<pattern>.persistent_approval",
      type: "boolean",
      description:
        "`false` に設定すると、ブラウザ機能は、一致するオリジンで `Always allow` 承認を保存したり適用したりできなくなります。現在のターンまたはスレッドを対象とする承認は引き続き適用できます。`true` は、他の条件で許可されている場合に `Always allow` を利用可能にしますが、承認を作成することはありません。",
    },
    {
      key: "browser_use.origins.<pattern>.access_approval_lifetime",
      type: "turn | thread",
      description:
        "一致するオリジンについて、永続化されないサイトアクセス承認の有効期間を設定します。`turn` は現在のターンに限定し、`thread` は現在のスレッドが終わるまで保持します。`Always allow` が利用可能かどうかは、`persistent_approval` で個別に制御します。",
    },
    {
      key: "computer_use",
      type: "table",
      description:
        "ネイティブデスクトップアプリ内でエージェントが行う作業に関する管理対象の要件です。管理対象のアプリルールと `config.toml` のアプリルールの両方が強制されます。アプリは、それぞれのポリシーソースで許可されている必要があります。",
    },
    {
      key: "computer_use.allow_locked_computer_use",
      type: "boolean",
      description:
        "`false` に設定すると、管理対象の macOS デバイスでユーザーがロック中の使用を有効にできなくなります。この要件は有効化のための操作項目を削除しますが、すでに有効になっているロック中の使用を無効にはしません。省略した場合は、通常の製品の提供条件が適用されます。",
    },
    {
      key: "computer_use.allow_persistent_approval",
      type: "boolean",
      description:
        "`false` に設定すると、アプリの承認をセッション間で保存するオプションが削除されます。現在のセッションに対する承認は引き続き利用できます。`true` に設定したり省略したりしても、アプリが承認されるわけではありません。",
    },
    {
      key: "computer_use.default_app_access",
      type: "allow | deny",
      description:
        "プラットフォーム固有のルールに一致しないネイティブアプリに適用する、フォールバックのアクセス設定です。`deny` はアクセスをブロックします。`allow` は通常の承認とポリシーのチェックを続行できるようにするだけです。製品のデフォルトは `allow` です。",
    },
    {
      key: "computer_use.macos",
      type: "table",
      description: "macOS 向けのコンピューターの使用に関するアプリルールです。",
    },
    {
      key: "computer_use.macos.bundle_ids",
      type: "map<string, allow | deny>",
      description:
        "macOS の正確なバンドル識別子を `allow` または `deny` に対応付けます。一致するルールは、同じポリシーソース内の `computer_use.default_app_access` に優先して適用されます。管理要件またはユーザー設定のいずれかで拒否されていれば、アクセスは引き続きブロックされます。",
    },
    {
      key: "computer_use.macos.bundle_ids.<bundle-id>",
      type: "allow | deny",
      description:
        "`deny` を使用すると、指定したバンドル識別子に完全一致するアプリをブロックします。`allow` が上書きするのは、このポリシーソースのデフォルトだけです。アプリを許可するには、他のすべてのポリシーソースと通常の承認フローでも許可される必要があります。",
    },
    {
      key: "computer_use.windows",
      type: "table",
      description:
        "パッケージ化された Windows アプリとパッケージ化されていない Windows アプリに適用する、コンピューターの使用に関するアプリルールです。",
    },
    {
      key: "computer_use.windows.aumids",
      type: "map<string, allow | deny>",
      description:
        "署名済みのパッケージアプリについて、登録済みの正確な Application User Model ID（AUMID）を `allow` または `deny` に対応付けます。一致するルールは、同じポリシーソース内の `computer_use.default_app_access` に優先して適用されます。",
    },
    {
      key: "computer_use.windows.aumids.<aumid>",
      type: "allow | deny",
      description:
        "`deny` を使用すると、指定した識別情報に完全一致するパッケージアプリをブロックします。`allow` が上書きするのは、このポリシーソースのデフォルトだけです。アプリを許可するには、他のすべてのポリシーソースと通常の承認フローでも許可される必要があります。",
    },
    {
      key: "computer_use.windows.exes",
      type: "array<table>",
      description:
        "署名済みでパッケージ化されていない Windows 実行ファイルに適用するルールです。ルールの照合には、実行ファイルのパスや現在のファイル名ではなく、検証済みの発行元と署名されたバージョン情報を使用します。一致する拒否ルールは、一致する許可ルールに優先します。署名のない実行ファイルには `computer_use.default_app_access` が適用されます。署名された識別情報を一意に検証できない実行ファイルはブロックされます。",
    },
    {
      key: "computer_use.windows.exes[].publisher_name",
      type: "string",
      description:
        "実行ファイルの信頼された署名証明書に記載された、正確な発行元名です。Windows の X.500 識別名形式で指定する必須項目です。",
    },
    {
      key: "computer_use.windows.exes[].product_name",
      type: "string",
      description:
        "実行ファイルの署名されたバージョン情報に記載された、正確な `ProductName` です。必須項目です。",
    },
    {
      key: "computer_use.windows.exes[].binary_name",
      type: "string",
      description:
        "実行ファイルの署名されたバージョン情報に記載された `OriginalFilename` です。省略可能で、照合では大文字と小文字を区別しません。発行元と製品が一致するルールでこの値が必要とされているのに、実行ファイルにその値が含まれていない場合、コンピューターの使用はその実行ファイルをブロックします。",
    },
    {
      key: "computer_use.windows.exes[].access",
      type: "allow | deny",
      description:
        "一致する実行ファイルに対するアクセスの判定です。必須項目です。`deny` はアクセスをブロックします。`allow` が上書きするのは、このポリシーソースのデフォルトだけです。アプリを許可するには、他のすべてのポリシーソースと通常の承認フローでも許可される必要があります。",
    },
    {
      key: "experimental_network",
      type: "table",
      description:
        "サンドボックス内のローカルコマンドに対し、`requirements.toml` によって強制適用される、管理者が管理するネットワーク要件です。有効にすると、`features.network_proxy` がなくても、この要件によってコマンド用のネットワークプロキシを起動できます。ブラウザツールは、管理対象のネットワーク拒否ルールと、管理者の許可ルールだけを有効にする許可リストを別途チェックします。この要件は、ブラウザの通信をプロキシ経由にするものではなく、ウェブ検索、アプリ、MCP サーバー、ネイティブアプリの通信、Codex Cloud のネットワーク通信を制御するものでもありません。",
    },
    {
      key: "experimental_network.enabled",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク要件を有効にします。使用中のサンドボックスがコマンドのネットワーク通信を無効にしている場合、この設定でネットワークアクセスが許可されるわけではありません。",
    },
    {
      key: "experimental_network.http_port",
      type: "integer",
      description:
        "`[experimental_network]` の要件に使用するループバック HTTP リスナーポートです。",
    },
    {
      key: "experimental_network.socks_port",
      type: "integer",
      description:
        "`[experimental_network]` の要件に使用するループバック SOCKS5 リスナーポートです。",
    },
    {
      key: "experimental_network.allow_upstream_proxy",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク通信で、環境で指定された上流プロキシへのチェーン接続を許可します。",
    },
    {
      key: "experimental_network.dangerously_allow_non_loopback_proxy",
      type: "boolean",
      description:
        "`[experimental_network]` の要件で、ループバック以外のリスナーアドレスを許可します。有効にすると、localhost の外部からリスナーにアクセスできるようになる可能性があります。",
    },
    {
      key: "experimental_network.dangerously_allow_all_unix_sockets",
      type: "boolean",
      description:
        "許可リストにある宛先だけでなく、任意の Unix ソケットの宛先へのアクセスを許可します。厳密に管理された環境でのみ使用してください。",
    },
    {
      key: "experimental_network.domains",
      type: "map<string, allow | deny>",
      description:
        "サンドボックス内のネットワーク通信に適用する、マップ形式の管理者ドメインポリシーです。完全一致のホスト、サブドメインのみを対象とする `*.example.com`、頂点ドメインとサブドメインを対象とする `**.example.com`、すべてを対象とする `*` の許可ルールに対応しています。`*` はパブリックネットワークへの送信アクセスを広範囲に許可するため、対象範囲を限定したルールを推奨します。競合する場合は `deny` が優先されます。`experimental_network.allowed_domains` または `experimental_network.denied_domains` と併用しないでください。",
    },
    {
      key: "experimental_network.allowed_domains",
      type: "array<string>",
      description:
        "管理対象のネットワークプロキシが有効な間、サンドボックス内のコマンドのネットワーク通信に適用される管理者の許可ルールです。ウェブ検索、アプリ、MCP サーバーには適用されません。`experimental_network.domains` と併用しないでください。",
    },
    {
      key: "experimental_network.denied_domains",
      type: "array<string>",
      description:
        "サンドボックス内のネットワーク通信に適用する、リスト形式の管理者の拒否ルールです。`experimental_network.domains` と併用しないでください。",
    },
    {
      key: "experimental_network.managed_allowed_domains_only",
      type: "boolean",
      description:
        "`true` の場合、サンドボックス内のネットワーク要件が有効な間は、管理者が管理する許可ルールだけが有効となり、ユーザーによる許可リストへの追加は無視されます。管理対象の許可ルールがない場合も、ユーザーが追加したドメインの許可ルールは有効になりません。",
    },
    {
      key: "experimental_network.unix_sockets",
      type: "map<string, allow | deny>",
      description:
        "サンドボックス内のネットワーク通信に適用する、管理者が管理する Unix ソケットポリシーです。",
    },
    {
      key: "experimental_network.allow_local_binding",
      type: "boolean",
      description:
        "サンドボックス内のネットワーク通信で、ローカルネットワークやプライベートネットワークへのより広範なアクセスを許可します。`false` のままでも、ローカル IP アドレスのリテラルまたは `localhost` に完全一致する許可ルールによって、特定のローカル宛先へのアクセスを許可できます。",
    },
    {
      key: "hooks",
      type: "table",
      description:
        "管理者が強制適用する管理対象のライフサイクルフックです。管理対象フックのディレクトリが必要で、`config.toml` 内のインラインの `[hooks]` と同じイベントスキーマを使用します。",
    },
    {
      key: "hooks.managed_dir",
      type: "string (absolute path)",
      description:
        "macOS と Linux で管理対象フックのスクリプトを格納するディレクトリです。Codex は管理対象フックを読み込む前に、絶対パスであることと、ディレクトリが存在することを検証します。",
    },
    {
      key: "hooks.windows_managed_dir",
      type: "string (absolute path)",
      description:
        "Windows で管理対象フックのスクリプトを格納するディレクトリです。Codex は管理対象フックを読み込む前に、絶対パスであることと、ディレクトリが存在することを検証します。",
    },
    {
      key: "hooks.",
      type: "array<table>",
      description:
        "`PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`SessionStart`、`SessionEnd`、`SubagentStart`、`SubagentStop`、`UserPromptSubmit`、`Stop` などのフックイベントに対するマッチャーグループです。",
    },
    {
      key: "hooks.[].hooks",
      type: "array<table>",
      description:
        "マッチャーグループのフックハンドラーです。コマンドフックと MCP ツールフックに対応しています。プロンプトとエージェントのフックハンドラーは解析されますが、実行はスキップされます。",
    },
    {
      key: "hooks.[].hooks[].async",
      type: "boolean",
      description:
        "トリガーとなる操作を遅らせずに、コマンドフックをバックグラウンドで実行します。デフォルトは `false` です。`SessionEnd` は常に同期的に実行されます。[フックのバックグラウンド実行](/codex/hooks#run-hooks-in-the-background)を参照してください。",
    },
    {
      key: "hooks.[].hooks[].additionalContextLimit",
      type: "integer",
      description:
        "サイズの大きい `additionalContext` をディスクに保存し、短いプレビューをモデルに表示するための、ハンドラーごとのおおよそのトークンしきい値です。デフォルトは `2500` です。`0` にすると、コンテキスト全体をモデルに直接渡します。[サイズの大きいフック出力](/codex/hooks#large-hook-output)を参照してください。",
    },
    {
      key: "hooks.[].hooks[].commandWindows",
      type: "string",
      description:
        "コマンドフックに適用する、Windows 専用のコマンド上書き設定です。TOML のエイリアス `command_windows` も使用できます。",
    },
    {
      key: "permissions.filesystem.deny_read",
      type: "array<string>",
      description:
        "管理者が強制適用する、ファイルシステムの読み取り拒否設定です。エントリにはパスまたは glob パターンを指定できます。ユーザーはローカル設定でこの制限を緩和できません。",
    },
    {
      key: "mcp_servers",
      type: "table",
      description:
        "有効化を許可する MCP サーバーの許可リストです。MCP サーバーを有効にするには、サーバー名（`<id>`）と識別情報の両方が一致する必要があります。設定済みの MCP サーバーでも、許可リストにない場合や識別情報が一致しない場合は無効になります。",
    },
    {
      key: "mcp_servers.<id>.identity",
      type: "table",
      description:
        "単一の MCP サーバーの識別ルールです。`command`（stdio）または `url`（ストリーミング対応 HTTP）のいずれかを設定します。",
    },
    {
      key: "mcp_servers.<id>.identity.command",
      type: "string | table",
      description:
        "MCP stdio サーバーをコマンド文字列の完全一致で許可するか、マッチャーテーブルを使用して実行ファイルの完全一致と引数ごとの順序どおりの照合を必須にします。文字列形式では、引数、`cwd`、`env`、`env_vars` は検査されません。",
    },
    {
      key: "mcp_servers.<id>.identity.command.executable",
      type: "string",
      description:
        "stdio サーバーに設定された `command` が完全一致する必要のある実行ファイルです。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args",
      type: "array<table>",
      description:
        "stdio サーバーの引数を順序どおりに照合するマッチャーです。設定された引数リストはマッチャーのリストと同じ長さで、すべての位置で一致する必要があります。コマンドマッチャーは `cwd`、`env`、`env_vars` を検査しません。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "この引数位置で使用する照合操作です。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].value",
      type: "string",
      description: "`exact` または `prefix` の引数マッチャーで使用する値です。",
    },
    {
      key: "mcp_servers.<id>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 引数マッチャーで使用する正規表現です。有効な正規表現で、引数の値全体に一致する必要があります。",
    },
    {
      key: "mcp_servers.<id>.identity.url",
      type: "string | table",
      description:
        "MCP のストリーミング対応 HTTP サーバーを URL 文字列の完全一致で許可するか、`exact`、`prefix`、`regex` のいずれかを指定した値マッチャーテーブルを使用します。",
    },
    {
      key: "mcp_servers.<id>.identity.url.match",
      type: "exact | prefix | regex",
      description: "設定された MCP サーバーの URL に対する照合操作です。",
    },
    {
      key: "mcp_servers.<id>.identity.url.value",
      type: "string",
      description: "`exact` または `prefix` の URL マッチャーで使用する値です。",
    },
    {
      key: "mcp_servers.<id>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL マッチャーで使用する正規表現です。有効な正規表現で、URL の値全体に一致する必要があります。",
    },
    {
      key: "plugins",
      type: "table",
      description:
        "プラグイン識別子をキーとする、プラグインごとの MCP サーバー許可リストです。このテーブルが存在する場合、プラグインにバンドルされたサーバーは、対応するプラグインとサーバーのエントリがなければ無効になります。",
    },
    {
      key: "plugins.<plugin>.mcp_servers",
      type: "table",
      description:
        "単一のプラグインにバンドルされた MCP サーバーの許可リストです。プラグインのサーバー要件では、トップレベルの `mcp_servers` 要件と同じ形式で、識別情報の完全一致やマッチャーを指定します。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity",
      type: "table",
      description:
        "プラグインにバンドルされた単一の MCP サーバーの識別ルールです。`command`（stdio）または `url`（ストリーミング対応 HTTP）のいずれかを設定します。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command",
      type: "string | table",
      description:
        "プラグインの stdio MCP サーバーをコマンド文字列の完全一致で許可するか、マッチャーテーブルを使用して実行ファイルの完全一致と引数ごとの順序どおりの照合を必須にします。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.executable",
      type: "string",
      description:
        "プラグインにバンドルされた stdio サーバーに設定されたコマンドが完全一致する必要のある実行ファイルです。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args",
      type: "array<table>",
      description:
        "プラグインにバンドルされた stdio サーバーの引数を順序どおりに照合するマッチャーです。設定された引数リストはマッチャーのリストと同じ長さで、すべての位置で一致する必要があります。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].match",
      type: "exact | prefix | regex",
      description: "この引数位置で使用する照合操作です。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].value",
      type: "string",
      description: "`exact` または `prefix` の引数マッチャーで使用する値です。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.command.args[].expression",
      type: "string",
      description:
        "`regex` 引数マッチャーで使用する正規表現です。引数の値全体に一致する必要があります。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url",
      type: "string | table",
      description:
        "プラグインのストリーミング対応 HTTP MCP サーバーを URL 文字列の完全一致で許可するか、`exact`、`prefix`、`regex` のいずれかを指定した値マッチャーテーブルを使用します。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.match",
      type: "exact | prefix | regex",
      description: "プラグインにバンドルされた MCP サーバーの URL に対する照合操作です。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.value",
      type: "string",
      description: "`exact` または `prefix` の URL マッチャーで使用する値です。",
    },
    {
      key: "plugins.<plugin>.mcp_servers.<server>.identity.url.expression",
      type: "string",
      description:
        "`regex` URL マッチャーで使用する正規表現です。URL の値全体に一致する必要があります。",
    },
    {
      key: "marketplaces",
      type: "table",
      description:
        "プラグインマーケットプレイスのソースに関する管理者要件です。`restrict_to_allowed_sources` が `true` の場合にルールが適用されます。",
    },
    {
      key: "marketplaces.restrict_to_allowed_sources",
      type: "boolean",
      description:
        "`true` の場合、マーケットプレイスの追加、プラグインのインストール、設定済み Git マーケットプレイスの更新を行うには、ユーザーが設定したマーケットプレイスのソースが `allowed_sources` と一致している必要があります。Codex が管理する OpenAI マーケットプレイスは、ソースと名前が予約済みの値に一致していれば、引き続き許可されます。この設定では、ユーザーが設定済みのマーケットプレイスは実行時にフィルタリングされません。",
    },
    {
      key: "marketplaces.allowed_sources",
      type: "table",
      description:
        "管理者が選択したルール名をキーとする、許可されたマーケットプレイスのソースです。異なる名前のエントリは要件レイヤー間で集約されます。同じ名前のエントリ内のフィールドには、通常のレイヤーの優先順位が適用されます。",
    },
    {
      key: "marketplaces.allowed_sources.<name>",
      type: "table",
      description:
        "許可するソースのルールを 1 つ定義します。要件のマージ後の最終的な `source` 値によって、Codex が解釈する同階層のフィールドが決まります。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.source",
      type: "git | host_pattern | local",
      description:
        "マーケットプレイスのソースを照合する方式です。単一のリポジトリには `git`、正規表現で照合する Git ホストには `host_pattern`、単一のディレクトリには `local` を使用します。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.url",
      type: "string",
      description:
        "`source = \"git\"` の場合に必須となる Git リポジトリの URL です。Codex は設定された URL と許可された URL を正規化したうえで、リポジトリの完全一致を求めます。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.ref",
      type: "string",
      description:
        "`git` ルールで完全一致を求める Git ref を指定します。省略可能です。省略すると、一致するリポジトリのすべての ref が許可されます。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.host_pattern",
      type: "string",
      description:
        "`source = \"host_pattern\"` の場合に必須となる正規表現です。Codex は HTTPS、SSH、または SCP 形式の Git ソースから抽出し、小文字に変換したホスト名と照合します。ホスト名全体の一致を求めるには、`^` と `$` を使用します。",
    },
    {
      key: "marketplaces.allowed_sources.<name>.path",
      type: "string (absolute path)",
      description:
        "`source = \"local\"` の場合に必須となるローカルのマーケットプレイスディレクトリです。Codex では絶対パスが必須で、正規化後のパスを比較します。",
    },
    {
      key: "apps",
      type: "table",
      description:
        "アプリ識別子をキーとする、管理対象のアプリ要件です。要件によってアプリを無効にしたり、個々のツールの承認動作を制限したりできます。",
    },
    {
      key: "apps.<id>.enabled",
      type: "boolean",
      description:
        "アプリを無効にするには `false` に設定します。複数の要件ソースをマージしても、アプリを無効にする要件による制限は維持されます。",
    },
    {
      key: "apps.<id>.tools.<tool>.approval_mode",
      type: "auto | prompt | writes | approve",
      description: "個別のアプリツールに対して、管理対象の承認モードを設定します。",
    },
    {
      key: "rules",
      type: "table",
      description:
        "`.rules` ファイルとマージされる、管理者が強制するコマンドルールです。要件内のルールは、制限を課すものでなければなりません。",
    },
    {
      key: "rules.prefix_rules",
      type: "array<table>",
      description:
        "強制適用するプレフィックスルールの一覧です。各ルールには `pattern` と `decision` を含める必要があります。",
    },
    {
      key: "rules.prefix_rules[].pattern",
      type: "array<table>",
      description:
        "パターントークンで表したコマンドのプレフィックスです。各トークンには `token` または `any_of` のどちらかを設定します。",
    },
    {
      key: "rules.prefix_rules[].pattern[].token",
      type: "string",
      description: "この位置で使用する単一のリテラルトークンです。",
    },
    {
      key: "rules.prefix_rules[].pattern[].any_of",
      type: "array<string>",
      description: "この位置で許可する代替トークンの一覧です。",
    },
    {
      key: "rules.prefix_rules[].decision",
      type: "prompt | forbidden",
      description:
        "必須です。要件内のルールでは、承認を求めるか禁止することだけが可能で、許可はできません。",
    },
    {
      key: "rules.prefix_rules[].justification",
      type: "string",
      description:
        "承認プロンプトや拒否メッセージに表示する理由です。省略可能ですが、指定する場合は空にできません。",
    },
  ]}
  client:load
/>
