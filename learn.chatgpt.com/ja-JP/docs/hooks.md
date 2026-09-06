<!-- source: https://learn.chatgpt.com/ja-JP/docs/hooks -->

フックは Codex の機能を拡張するためのフレームワークです。エージェントの処理ループ中にスクリプトや MCP ツールを実行し、次のような機能を実現できます：

- チャットを独自のログ記録・分析エンジンに送信
- チームのプロンプトをスキャンし、API キーの誤った貼り付けをブロック
- チャットを要約し、永続的なメモリを自動作成
- チャットのターン停止時に独自の検証を実行し、基準への準拠を徹底
- 特定のディレクトリでプロンプトをカスタマイズ

実行時の動作に関する注意点：

- 複数のファイルにある、条件に一致するフックはすべて実行されます。
- 同じイベントに一致するコマンドフックが複数ある場合、同時に起動されます。そのため、あるフックが別の一致するフックの起動を阻止することはできません。
- 管理対象外のフックは、実行前にレビューし、信頼済みにする必要があります。

フックは会話中のさまざまなタイミングで実行されます：

| タイミング                              | フック                                                                                                                     |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| ターン中                     | `PreToolUse`、`PermissionRequest`、`PostToolUse`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、`SubagentStop`、`Stop` |
| 実行中のターンを中断したとき | `Interrupt`（サブエージェントでは実行されません）                                                                                   |
| セッションまたはサブエージェントの開始時 | `SessionStart`、`SubagentStart`                                                                                           |
| メインスレッドの終了時         | `SessionEnd`（サブエージェントでは実行されません）                                                                                  |

## Codex によるフックの検索場所

Codex は、有効な設定レイヤーと同じ場所にあるフックを、次のいずれかの形式で検出します：

- `hooks.json`
- `config.toml` 内のインラインの `[hooks]` テーブル

インストール済みのプラグインには、プラグインのマニフェストまたは
デフォルトの `hooks/hooks.json` ファイルを使って、ライフサイクル設定を同梱することもできます。プラグインのパッケージ化ルールについては、
[プラグインの
ビルド](https://developers.openai.com/plugins/build/plugins#bundled-mcp-servers-and-lifecycle-hooks)を参照してください。

実際に特に役立つのは、次の 4 か所です：

- `~/.codex/hooks.json`
- `~/.codex/config.toml`
- `<repo>/.codex/hooks.json`
- `<repo>/.codex/config.toml`

複数のフック定義元がある場合、Codex は条件に一致するすべてのフックを読み込みます。
優先度の高い設定レイヤーが、優先度の低いレイヤーのフックを置き換えることはありません。
同じレイヤーに `hooks.json` とインラインの `[hooks]` の両方がある場合、Codex はそれらをマージし、起動時に警告を表示します。
レイヤーごとに、いずれか一方の形式を使用することを推奨します。

Codex は、有効なプラグインに同梱されたフックも検出できます。同梱されたフックは他の定義元のフックと併せて読み込まれ、他の管理対象外のフックと同じレビューと信頼設定の手順が適用されます。

プロジェクト内のフックは、プロジェクトの `.codex/` レイヤーが信頼されている場合にのみ読み込まれます。
信頼されていないプロジェクトでも、Codex はユーザーとシステムのフックを
それぞれの有効な設定レイヤーから引き続き読み込みます。

## フックのレビューと信頼設定

Codex は、どのフックを実行できるかを判断する前に、設定済みのフックを一覧表示します。管理対象外のフックを実行するには、そのフックの定義そのものをレビューし、信頼済みにする必要があります。Codex は信頼情報をフックの現在のハッシュに紐づけて記録するため、新規または変更されたフックはレビュー対象としてマークされ、信頼済みになるまでスキップされます。

CLI で `/hooks` を使用すると、フックの定義元の確認や、新規または変更されたフックのレビューができます。
フックを信頼済みにすることや、管理対象外のフックを個別に無効にすることもできます。
起動時にレビューが必要なフックがあると、Codex は `/hooks` を開くよう案内する警告を表示します。

システム、MDM、クラウド、または `requirements.toml` を定義元とする管理対象フックは、管理対象と表示され、
ポリシーに基づいて信頼済みとなります。ユーザー向けのフックブラウザから無効にすることはできません。

Codex の外でフックの定義元を検証済みの単発の自動化では、
`--dangerously-bypass-hook-trust` を指定すると、その呼び出しに限り、
保存済みのフックの信頼情報を必要とせずに、有効なフックを実行できます。

## 設定の構造

フックは次の 3 階層で構成されます：

- `PreToolUse`、`PostToolUse`、`PreCompact`、
`SubagentStart`、`Stop` などのフックイベント
- イベントの一致条件を定めるマッチャーグループ
- マッチャーグループの条件に一致したときに実行される 1 つ以上のフックハンドラー

```json
{
  "description": "Optional lifecycle hooks for this workspace.",
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_start.py",
            "statusMessage": "Loading session notes",
            "additionalContextLimit": 5000
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/session_end.py",
            "timeout": 3
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py\"",
            "statusMessage": "Checking Bash command"
          }
        ]
      }
    ],
    "PermissionRequest": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/permission_request.py\"",
            "statusMessage": "Checking approval request"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py\"",
            "statusMessage": "Reviewing Bash output"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/user_prompt_submit_data_flywheel.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/usr/bin/python3 \"$(git rev-parse --show-toplevel)/.codex/hooks/stop_continue.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}

注意事項：

- `description` は `hooks.json` ファイルの省略可能なトップレベルのメタデータです。
  どのフックが実行されるかには影響しません。
- `timeout` は秒単位です。
- `timeout` を省略すると、Codex はほとんどのフックで `600` 秒を使用します。
  - `SessionEnd` と `Interrupt` のタイムアウトはデフォルトで `1` 秒で、最大 `3` 秒まで設定できます。
- `statusMessage` は省略可能です。
- `additionalContextLimit` は、コマンドフックがモデルに送信できる `additionalContext` の量を設定します。
  この上限を超えると、Codex は全文をディスクに保存し、代わりに短いプレビューを送信します。
  詳しくは[サイズの大きいフック出力](#large-hook-output)を参照してください。
- `commandWindows` は、Windows でのみコマンドを上書きするための省略可能な設定です。
TOML では `command_windows` または `commandWindows` を使用します。
- `async` を `true` に設定すると、[コマンドフックを
  バックグラウンドで実行](#run-hooks-in-the-background)できます。
- `command` と `mcp_tool` のハンドラーに対応しています。
  `prompt` と `agent` のハンドラーは解析されますが、スキップされます。
- コマンドは、セッションの `cwd` を作業ディレクトリとして実行されます。
- リポジトリ内のフックでは、`.codex/hooks/...` のような相対パスを使うよりも、
  Git のルートを基準にパスを解決することを推奨します。
  Codex はサブディレクトリから起動される場合もあるため、Git のルートを基準にするとフックの場所を一定に保てます。

同じ設定を `config.toml` 内のインライン TOML で記述すると、次のようになります：

```toml
[[hooks.SessionStart]]
matcher = "^compact$"

[[hooks.SessionStart.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/session_start.py"'
additionalContextLimit = 5000

[[hooks.PreToolUse]]
matcher = "^Bash$"

[[hooks.PreToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/pre_tool_use_policy.py"'
timeout = 30
statusMessage = "Checking Bash command"

[[hooks.PostToolUse]]
matcher = "^Bash$"

[[hooks.PostToolUse.hooks]]
type = "command"
command = '/usr/bin/python3 "$(git rev-parse --show-toplevel)/.codex/hooks/post_tool_use_review.py"'
timeout = 30
statusMessage = "Reviewing Bash output"

## MCP ツールフック

MCP ツールフックを使うと、ライフサイクルイベントから接続済みの MCP サーバー上のツールを呼び出せます。構造化された引数をツールに直接送信します。レビューと信頼設定の手順、および出力仕様はコマンドフックと同じです。

### MCP ツールフックの設定

このフックは、Codex がファイルを書き込んだり編集したりした後に、
`scanner` MCP サーバーに各パッチのスキャンを依頼します：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "mcp_tool",
            "server": "scanner",
            "tool": "scan_patch",
            "input": { "patch": "${tool_input.command}" },
            "timeout": 30,
            "statusMessage": "Scanning edited files"
          }
        ]
      }
    ]
  }
}

| フィールド           | 説明                                                          |
| --------------- | ---------------------------------------------------------------- |
| `type`          | `mcp_tool` である必要があります。                                              |
| `server`        | 接続済みの MCP サーバーの名前です。指定は必須です。                |
| `tool`          | そのサーバーが公開するツールの名前です。指定は必須です。                  |
| `input`         | 引数テンプレートを格納する JSON オブジェクトです。省略可能で、デフォルトは `{}` です。    |
| `timeout`       | 実際の実行時間に適用するタイムアウト（秒）。省略可能で、デフォルトは `600` です。 |
| `statusMessage` | フックの実行中に表示するメッセージ。省略可能です。                      |

### フックイベントからの引数展開

フックイベント内のフィールドをドット表記で参照するには、`${field.nested}` を使用します。
値全体を占めるプレースホルダーは、元の JSON 型を保持します。文字列の一部として使われるプレースホルダーは、テキストとして展開されます。
Codex はオブジェクトと配列を再帰的に展開します。

イベントに `{"tool_input":{"file_path":"src/main.rs","count":3}}` が含まれている場合、
次の引数テンプレートは、

```json
{
  "path": "${tool_input.file_path}",
  "count": "${tool_input.count}",
  "message": "Scanning ${tool_input.file_path}"
}

次のように展開されます：

```json
{
  "path": "src/main.rs",
  "count": 3,
  "message": "Scanning src/main.rs"
}

### 実行とライフサイクル

- フックは既存の MCP 接続を使用します。サーバーの起動や再接続は行いません。
- ツールがブロックするという判断を返した場合、フックは操作をブロックできます。エラーが発生した場合や、サーバーが存在しない場合、ツールが利用できない場合は、操作をブロックしません。
- MCP ツールフックは同期的に実行されます。ツールの承認を求めたり、他のフックを起動したりすることはありません。
- フックとサーバーのタイムアウトのうち、短い方が適用されます。MCP の誘発に対する応答を待つ時間は、タイムアウト時間に算入されません。
- `SessionStart` フックは、MCP サーバーの準備が整う前に実行されることがあります。
  その場合、セッションをブロックしません。
- `SessionEnd` は MCP ツールフックに対応していません。

## フックの無効化

フックはデフォルトで有効です。無効にするには、`config.toml` で次のように設定します：

```toml
[features]
hooks = false

正式な機能キーには `hooks` を使用します。
`codex_hooks` も非推奨のエイリアスとして引き続き使用できます。
管理者も同様に、`requirements.toml` で `[features].hooks = false` を設定してフックを強制的に無効にできます。

## `requirements.toml` による管理対象フック

エンタープライズで管理する要件設定でも、`[hooks]` の下にフックをインラインで定義できます。
管理者がフック構成を強制しつつ、
実際のスクリプトを MDM や他のデバイス管理システムで配布したい場合に便利です。
ローカルでフックを無効にしたユーザーにも管理対象フックを強制するには、
`requirements.toml` で `[hooks]` とともに `[features].hooks = true` を固定設定します。
ユーザー、プロジェクト、セッション、プラグインのフックを無視し、管理者が管理するフックは引き続き許可するには、
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

管理対象フックに関する注意事項：

- `managed_dir` は macOS と Linux で使用されます。
- `windows_managed_dir` は Windows で使用されます。
- Codex は `managed_dir` 内のスクリプトを配布しません。
  組織の管理ツールで別途インストールし、更新する必要があります。
- 管理対象フックのコマンドでは、設定済みの管理対象ディレクトリ内にあるスクリプトを絶対パスで指定してください。
- `allow_managed_hooks_only = true` を設定すると、
  ユーザー、プロジェクト、セッション、プラグイン由来のフックはスキップされますが、
  `requirements.toml` や他の管理対象構成レイヤーの管理対象フックは引き続き読み込まれます。

## プラグインに同梱されたフック

プラグインを有効にすると、Codex はユーザー、プロジェクト、管理対象の各フックとともに、そのプラグインのライフサイクルフックを読み込めます。

デフォルトでは、Codex はプラグインルート内の `hooks/hooks.json` を探します。
プラグインマニフェストでは、`.codex-plugin/plugin.json` に `hooks` エントリを指定してこのデフォルト設定を上書きできます。
マニフェストのエントリには、`./` で始まるパス、
`./` で始まるパスの配列、インラインのフックオブジェクト、
またはインラインのフックオブジェクトの配列を指定できます。

```json
{
  "name": "repo-policy",
  "hooks": "./hooks/hooks.json"
}

マニフェスト内のフックパスはプラグインルートを基準に解決され、
そのルート内に収まる必要があります。マニフェストで `hooks` が定義されている場合、
Codex はデフォルトの `hooks/hooks.json` ではなく、そのマニフェストのエントリを使用します。

プラグインのフックコマンドには、次の環境変数が渡されます：

- `PLUGIN_ROOT` は Codex 固有の拡張で、
  インストール済みプラグインのルートを指します。
- `PLUGIN_DATA` は Codex 固有の拡張で、
  プラグインの書き込み可能なデータディレクトリを指します。
- Codex は `CLAUDE_PLUGIN_ROOT` と `CLAUDE_PLUGIN_DATA` も設定し、
  既存のプラグインフックとの互換性を確保します。

プラグインフックは、他のフックと同じイベントスキーマを使用します。プラグインをインストールまたは有効化しても、そのフックが自動的に信頼されるわけではありません。現在のフック定義をレビューして信頼済みにするまで、Codex はプラグインに同梱されたフックをスキップします。

## マッチャーパターン

`matcher` フィールドは、フックの実行条件を絞り込む正規表現文字列です。
`"*"` または `""` を指定するか、`matcher` 自体を省略すると、
サポート対象のイベントに毎回一致します。

現在の Codex イベントのうち、`matcher` が適用されるのは一部だけです：

| イベント               | `matcher` の絞り込み対象 | 注記                                                        |
| ------------------- | ---------------------- | ------------------------------------------------------------ |
| `PermissionRequest` | ツール名              | `Bash`、`apply_patch`\*、MCP ツール名などに対応 |
| `PostToolUse`       | ツール名              | [ツールの対応範囲](#tool-coverage)を参照                          |
| `PostCompact`       | コンパクションのトリガー     | 値は `manual` または `auto`                                |
| `PreCompact`        | コンパクションのトリガー     | 値は `manual` または `auto`                                |
| `PreToolUse`        | ツール名              | [ツールの対応範囲](#tool-coverage)を参照                          |
| `SessionEnd`        | 終了理由             | 現時点では `other` のみ                                       |
| `SessionStart`      | 開始元           | 値は `startup`、`resume`、`clear`、`compact`       |
| `SubagentStart`     | サブエージェントの種類          | 値は開始するサブエージェントによって異なります                    |
| `SubagentStop`      | サブエージェントの種類          | 値は停止するサブエージェントによって異なります                     |
| `UserPromptSubmit`  | 非対応          | このイベントでは、`matcher` を設定しても無視されます           |
| `Stop`              | 非対応          | このイベントでは、`matcher` を設定しても無視されます           |
| `Interrupt`         | 非対応          | このイベントでは、`matcher` を設定しても無視されます           |

\*`apply_patch` では、`matcher` の値として `Edit` または `Write` も使用できます。

例：

- `Bash`
- `^apply_patch$`
- `Edit|Write`
- `mcp__filesystem__read_file`
- `mcp__filesystem__.*`
- `startup|resume|clear|compact`
- `manual|auto`

### ツールの対応範囲

`PreToolUse` と `PostToolUse` は、シェルや MCP の呼び出し以外も監視できます。
ほとんどのローカル関数ツールは同じフック実行経路を使うため、ツール名でのマッチングや JSON 引数の確認ができます。
`PreToolUse` では、呼び出しのブロックや書き換えも可能です。

| ツール実行経路                         | `PreToolUse` | `PostToolUse` | 補足                                                                                                                    |
| --------------------------------- | ------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------ |
| シェルコマンド                    | はい          | はい           | `Bash` としてマッチします。                                                                                                         |
| 統合実行（`exec_command`）     | はい          | はい           | `Bash` としてマッチします。その後の `write_stdin` によるポーリングで、元のコマンドの完了時に、そのコマンドの `PostToolUse` が通知される場合があります。 |
| `apply_patch`                     | はい          | はい           | `apply_patch`、`Edit`、`Write` のいずれかとしてマッチします。                                                                              |
| MCP ツール                         | はい          | はい           | `mcp__filesystem__read_file` などの MCP ツール名でマッチします。                                                           |
| その他のローカル関数ツール        | はい          | はい           | `update_plan` などの関数ツール名でマッチします。`spawn_agent` は `Agent` にもマッチします。                                 |
| `WebSearch` などのホスト型ツール | いいえ           | いいえ            | これらは、ローカル関数ツールのフック実行経路を使用しません。                                                                       |

`write_stdin` は、既存の統合実行セッションとの通信に使われます。
すでに `PreToolUse` を通過したコマンドに入力を送信したり、ポーリングしたりする際に、
`PreToolUse` を再実行することはありません。

一部の特殊なツール実行経路では、デフォルトのフック実行経路を使用しない場合があります。ツールフックは、ポリシーの適用を完全に保証する仕組みではなく、有用なガードレールとして扱ってください。

## 共通入力フィールド

すべてのコマンドフックは、`stdin` で JSON オブジェクトを 1 つ受け取ります。

通常使用する共通フィールドは次のとおりです。

| フィールド             | 型             | 意味                                                             |
| ----------------- | ---------------- | ------------------------------------------------------------------- |
| `session_id`      | `string`         | 現在の Codex セッション ID です。サブエージェントのフックでは、親セッションの ID を使用します。 |
| `transcript_path` | `string \| null` | セッションのトランスクリプトファイルがある場合は、そのパス                         |
| `cwd`             | `string`         | セッションの作業ディレクトリ                                   |
| `hook_event_name` | `string`         | 現在のフックイベント名                                             |
| `model`           | `string`         | 使用中のモデルのスラッグ（Codex 固有の拡張）                         |

ターン単位のフックでは、イベント別の表に
`turn_id` が Codex 固有の拡張として記載されています。

`SessionStart`、`PreToolUse`、`PermissionRequest`、`PostToolUse`、
`UserPromptSubmit`、`SubagentStart`、`SubagentStop`、`Stop`、`Interrupt` には、
現在の権限モードを示す `permission_mode` も含まれます。値は `default`、
`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions` のいずれかです。

`transcript_path` は便宜上チャットのトランスクリプトを参照しますが、
その形式はフック向けの安定したインターフェースではなく、今後変更される可能性があります。

通信データ形式の全体を確認するには、[スキーマ](#schemas)を参照してください。

## 共通出力フィールド

`SessionStart`、`PreCompact`、`PostCompact`、`UserPromptSubmit`、
`SubagentStop`、`Stop` は、次の共通 JSON フィールドをサポートしています。
`SubagentStart` は `systemMessage` とフック固有のコンテキストに同じ形式を受け付けますが、
`continue: false` を返してもサブエージェントは停止しません。

```json
{
  "continue": true,
  "stopReason": "optional",
  "systemMessage": "optional",
  "suppressOutput": false
}

| フィールド            | 効果                                          |
| ---------------- | ----------------------------------------------- |
| `continue`       | 値が `false` の場合、そのフックの実行を停止済みとしてマーク      |
| `stopReason`     | 停止理由として記録             |
| `systemMessage`  | UI またはイベントストリームに警告として表示 |
| `suppressOutput` | 現時点では解析のみで、動作は未実装            |

出力がなく終了コードが `0` の場合は、成功として扱われ、Codex は処理を続行します。

`PreToolUse` と `PermissionRequest` は `systemMessage` をサポートしていますが、`continue`、
`stopReason`、`suppressOutput` は現在これらのイベントではサポートされていません。
`PreToolUse` フックがこれらの未サポートフィールドのいずれかを返すと、
Codex はそのフックの実行を失敗としてマークし、エラーを報告したうえでツール呼び出しを続行します。

`PostToolUse` は `systemMessage`、`continue: false`、`stopReason` をサポートしています。
`suppressOutput` は解析されますが、このイベントでは現在サポートされていません。

### 大容量のフック出力

デフォルトでは、Codex はモデルに渡すフック出力メッセージを、
1 件あたり約 2,500 トークンに制限します。フックがこの上限を超える出力を返した場合、
Codex は全文を `<temp_dir>/hook_outputs/<session_id>/<uuid>.txt` に保存し、
先頭と末尾を抜粋したプレビューを、保存先のファイルパスとともにモデルに渡します。
この動作を**スピル**と呼びます。Codex は大きすぎる出力をディスクに保存し、
モデルには代わりに短いプレビューを渡します。ファイルに書き込めない場合でも、
モデルには切り詰めたプレビューが渡されます。

  フックやプラグインのコンテキストは簡潔に保ってください。
  複数のフックやプラグインからのコンテキストが積み重なると、モデルの性能が低下する可能性があります。
  `additionalContextLimit` を引き上げると、そのリスクが高まります。
  フック自体が出力に厳格な上限を設けている場合を除き、上限を `0` に設定することは避けてください。
  そうしないと、1 つのフックだけでコンテキストウィンドウ全体を消費する可能性があります。

`additionalContext` を返すコマンドフックでは、
ハンドラーに `additionalContextLimit` を設定することで、
トークン数のおおよそのしきい値を変更できます。

```json
{
  "type": "command",
  "command": "python3 ~/.codex/hooks/session_start.py",
  "additionalContextLimit": 5000
}

`additionalContextLimit` を省略すると、デフォルトの `2500` トークンのしきい値が使用されます。
別のしきい値を指定するには正の整数を使用します。`0` を指定すると、
ハンドラーの追加コンテキスト全体がモデルに直接渡されます。
Codex は、マッチする各ハンドラーを個別に評価します。
追加コンテキストを生成できないイベントでは、Codex は `additionalContextLimit` を無視し、
構成に関する警告を報告します。

この設定は `additionalContext` にのみ適用されます。
ツールのフィードバックと継続プロンプトには、デフォルトの上限が引き続き適用されます。

大きすぎる出力はディスクに書き込まれる可能性があるため、フックの出力にシークレットやその他の機密データを含めることは避けてください。

## バックグラウンドでのフック実行

デフォルトでは、Codex はコマンドフックの完了を待ってから、
そのフックを起動した操作を続行します。`async` を `true` に設定すると、
Codex が処理を続行する間、コマンドフックをバックグラウンドで実行できます。

### バックグラウンドフックの設定

`hooks.json` のコマンドハンドラーに `"async": true` を追加します：

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ~/.codex/hooks/post_tool_use.py",
            "async": true,
            "timeout": 120
          }
        ]
      }
    ]
  }
}

`config.toml` のインラインフックでは、`async = true` を設定します：

```toml
[[hooks.PostToolUse]]
matcher = "Bash"

[[hooks.PostToolUse.hooks]]
type = "command"
command = "python3 ~/.codex/hooks/post_tool_use.py"
async = true
timeout = 120

バックグラウンドフックの入力、マッチャー、信頼性のレビュー、タイムアウト、
[大量出力の処理](#large-hook-output)は、同期コマンドフックと同じです。
他のコマンドフックと同様に、`timeout` は秒単位で、
デフォルトは `600` です。`Interrupt` フックのタイムアウトはデフォルトで 1 秒、最大で 3 秒で、
バックグラウンドで実行する場合も同じです。

### バックグラウンドフックの動作

バックグラウンドフックが完了すると、Codex はサポート対象の情報提供用の出力を、会話の次の安全なタイミングで渡します：

- ターンの実行中は、Codex は現在のモデルリクエストとツール呼び出しが完了するのを待ち、そのターンの次のモデルリクエストで出力を利用できるようにします。
- 実行中のターンがない場合、Codex は次のユーザーターンまで待機します。バックグラウンドフックが完了しても、新しいターンは開始されません。

同期フックと同じ、イベント固有の JSON 出力を使用します。
Codex は `additionalContext` をモデルのコンテキストに追加し、
`systemMessage` を警告として表示します。

  バックグラウンドフックは、自身を起動した操作をブロックしたり、承認したり、書き換えたり、その他の方法で制御したりすることはできません。ツールのポリシー、権限の判断、プロンプトの拒否、ターンの継続には同期フックを使用してください。

### 制限事項

- Codex は、セッションごとに最大 8 個のバックグラウンドフックを同時に実行します。それを超えるフックは、実行中のフックが完了するまで待機します。
- 条件に一致した呼び出しはそれぞれ独立して実行され、バックグラウンドフックは開始順とは異なる順序で完了する場合があります。
- セッションが終了すると、Codex は未完了のバックグラウンドフックをキャンセルし、まだ渡していない出力を破棄します。
- `SessionEnd` フックは常に同期的に実行されます。

## フック

### SessionStart

このイベントでは、`matcher` が `source` に適用されます。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド    | 型     | 意味                                                             |
| -------- | -------- | ------------------------------------------------------------------- |
| `source` | `string` | セッションの開始方法：`startup`、`resume`、`clear`、または `compact` |

`stdout` に出力されたプレーンテキストは、開発者コンテキストに追加されます。

`stdout` に出力する JSON では、[共通出力フィールド](#common-output-fields)と、
次のフック固有の形式を使用できます：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Load the workspace conventions before editing."
  }
}

この `additionalContext` のテキストは、開発者コンテキストに追加されます。

Codex がルートセッションのコンパクションを行った後、
`source: "compact"` に一致する `SessionStart` フックが、次のモデルリクエストの前に実行されます。
ターンの途中で自動コンパクションが発生した場合も同様です。
Codex は後続のユーザーターンを待たずに、フックが提供する追加のコンテキストを直後の継続処理に渡します。
フックが `continue: false` を返した場合、
Codex は次のモデルリクエストを送信せずにターンを終了します。

### SessionEnd

`SessionEnd` を使用すると、セッションの終了時に、最終メモの保存やファイルのクリーンアップなどのコマンドを実行できます。
メインスレッドでは、まだ開いている会話をアーカイブまたは削除したとき、
Codex が正常終了したとき、または会話がアイドル状態で、
接続中のどのクライアントでも開かれていない状態が 30 分間続いたときに実行されます。
サブエージェントでは実行されません。

会話から別の画面に切り替えたり、`thread/unsubscribe` を呼び出したりしても、セッションはすぐには終了しないため、
`SessionEnd` もすぐには実行されません。
フックは実行中もセッションのトランスクリプトを読み取れます。

このイベントでは、`matcher` が `reason` をフィルタリングします。現時点では、`reason` は常に `other` です。
`matcher` を省略するか `other` を使用すると、すべての `SessionEnd` イベントで実行できます。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド    | 型     | 意味                        |
| -------- | -------- | ------------------------------ |
| `reason` | `string` | セッションの終了理由：`other` |

たとえば、`SessionEnd` コマンドは次の内容を受け取ります：

```json
{
  "session_id": "thr_123",
  "transcript_path": "/workspace/.codex/rollout.jsonl",
  "cwd": "/workspace",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}

`SessionEnd` フックは、`async` が `true` の場合でも常に同期的に実行されます。
情報提供のみを目的とするため、その出力が Codex の動作を制御したり、スレッドを開いたままにしたりすることはありません。
コマンドがタイムアウトするかエラーで終了した場合、Codex はフックの失敗として報告します。

### SubagentStart

このイベントでは、`matcher` が `agent_type` に適用されます。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド             | 型     | 意味                                        |
| ----------------- | -------- | ---------------------------------------------- |
| `turn_id`         | `string` | Codex 固有の拡張。実行中の Codex ターンの ID |
| `agent_id`        | `string` | サブエージェントの識別子                    |
| `agent_type`      | `string` | サブエージェントの種類またはプロファイル                       |
| `permission_mode` | `string` | 現在の権限モード                        |

`stdout` に出力されたプレーンテキストは、サブエージェントの開発者コンテキストに追加されます。

`stdout` に出力する JSON では、`systemMessage` と次のフック固有の形式を使用できます：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "Review the repository test conventions first."
  }
}

この `additionalContext` のテキストは、サブエージェントの開発者コンテキストに追加されます。
`continue: false` は互換性のために解析されますが、
サブエージェントの起動を止めることはありません。

### PreToolUse

`PreToolUse` は、Bash、`apply_patch` を介したファイル編集、
MCP ツール呼び出し、その他のローカル関数ツールをインターセプトできます。対応する実行経路と例外については、[ツールの
対応範囲](#tool-coverage)を参照してください。

`matcher` は `tool_name` とマッチャーのエイリアスに適用されます。
`apply_patch` を介したファイル編集では、`matcher` の値として `apply_patch`、`Edit`、`Write` を使用できますが、
フックの入力に含まれる値は引き続き `tool_name: "apply_patch"` です。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド         | 型         | 意味                                                                                                                          |
| ------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`     | `string`     | Codex 固有の拡張。実行中の Codex ターンの ID                                                                                   |
| `tool_name`   | `string`     | フックで使用する正規のツール名（例：`Bash`、`apply_patch`、または `mcp__fs__read` のような MCP 名）                                     |
| `tool_use_id` | `string`     | この呼び出しに対応するツール呼び出し ID                                                                                                 |
| `tool_input`  | `JSON value` | ツール固有の入力。`Bash` と `apply_patch` は `tool_input.command` を使用します。MCP ツールやその他のローカル関数ツールはそれぞれの引数を送信します。 |

`stdout` に出力されたプレーンテキストは無視されます。

`stdout` に出力する JSON では、`systemMessage` を使用できます。サポート対象のツール呼び出しを拒否するには、
次のフック固有の形式を返します：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by hook."
  }
}

Codex は、次の旧形式のブロック指定も受け付けます：

```json
{
  "decision": "block",
  "reason": "Destructive command blocked by hook."
}

終了コード `2` を使用し、ブロックする理由を `stderr` に書き込むこともできます。

ブロックせずにモデルに渡すコンテキストを追加するには、
`hookSpecificOutput.additionalContext` を返します：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "additionalContext": "The pending command touches generated files."
  }
}

サポート対象のツール呼び出しをブロックせずに書き換えるには、
`permissionDecision: "allow"` とともに `updatedInput` を返します：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "updatedInput": {
      "command": "echo rewritten"
    }
  }
}

Bash コマンドと `apply_patch` では、
`updatedInput` に文字列型の `command` フィールドを含める必要があります。
MCP ツールとその他のローカル関数ツールでは、`updatedInput` は置き換え用の引数オブジェクトです。
`updatedInput` は必ず `permissionDecision: "allow"` とともに返してください。
それ以外の形式の `updatedInput` はエラーとして報告されます。

`permissionDecision: "ask"`、従来の `decision: "approve"`、`continue: false`、
`stopReason`、`suppressOutput` は解析されますが、まだサポートされていません。
Codex はフックの実行を失敗として記録し、エラーを報告したうえで、ツール呼び出しを続行します。

### PermissionRequest

`PermissionRequest` は、シェルの権限昇格や管理対象ネットワークの利用承認など、
Codex が承認を求める直前に実行されます。
リクエストを許可または拒否することも、判断せずに通常の承認プロンプトへ進めることもできます。
承認が不要なコマンドでは実行されません。

`matcher` は `tool_name` とマッチャーのエイリアスに適用されます。
現在の正規値には `Bash`、`apply_patch`、`mcp__server__tool` などの MCP ツール名が含まれます。
`apply_patch` は `Edit` と `Write` にも一致します。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド                    | 型             | 意味                                                                                                        |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------------- |
| `turn_id`                | `string`         | Codex 固有の拡張。アクティブな Codex ターンの ID                                                                 |
| `tool_name`              | `string`         | フックで使用するツールの正規名（`Bash`、`apply_patch`、または `mcp__fs__read` のような MCP ツール名）                   |
| `tool_input`             | `JSON value`     | ツール固有の入力。`Bash` と `apply_patch` は `tool_input.command` を使用し、MCP ツールはすべての引数を送信します。 |
| `tool_input.description` | `string \| null` | 人が読める形式の承認理由（Codex が保持している場合）                                                             |

`stdout` に出力されたプレーンテキストは無視されます。

ツールの入力には人が読める形式の説明が含まれる場合もありますが、
すべてのツールに `tool_input.description` フィールドがあることを前提にしないでください。

リクエストを承認するには、次を返します：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow"
    }
  }
}

リクエストを拒否するには、次を返します：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "deny",
      "message": "Blocked by repository policy."
    }
  }
}

条件に一致する複数のフックが判断を返した場合、1 つでも `deny` があれば、その判断が優先されます。
それ以外の場合は、`allow` によって承認プロンプトを表示せずにリクエストが進みます。
条件に一致するどのフックも判断を返さなかった場合、Codex は通常の承認フローを使用します。

`updatedInput`、`updatedPermissions`、`interrupt` は、
`PermissionRequest` では返さないでください。これらのフィールドは将来の機能用に予約されています。
現時点では、これらを返すと安全のためリクエストが拒否されます。

### PostToolUse

`PostToolUse` は、Bash、
`apply_patch`、MCP ツール呼び出し、その他のローカル関数ツールなど、サポート対象のツールが出力を生成した後に実行されます。
Bash では、ゼロ以外のステータスで終了するコマンドの後にも実行されます。
実行済みのツールによる副作用は取り消せません。
サポート対象の実行経路と例外については、[ツールの対応範囲](#tool-coverage)を参照してください。

`matcher` は `tool_name` とマッチャーのエイリアスに適用されます。
`apply_patch` によるファイル編集では、`matcher` の値に `apply_patch`、`Edit`、`Write` を使用できます。
ただし、フックの入力で報告される値は `tool_name: "apply_patch"` のままです。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド           | 型         | 意味                                                                                                                          |
| --------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| `turn_id`       | `string`     | Codex 固有の拡張。アクティブな Codex ターンの ID                                                                                   |
| `tool_name`     | `string`     | フックで使用するツールの正規名（`Bash`、`apply_patch`、または `mcp__fs__read` のような MCP ツール名）                                     |
| `tool_use_id`   | `string`     | この呼び出しに対応するツール呼び出し ID                                                                                                 |
| `tool_input`    | `JSON value` | ツール固有の入力。`Bash` と `apply_patch` は `tool_input.command` を使用します。MCP ツールとその他のローカル関数ツールは引数を送信します。 |
| `tool_response` | `JSON value` | ツール固有の出力。MCP ツールは MCP 呼び出しの結果を送信します。その他のローカル関数ツールは通常、モデル向けの出力を送信します。    |

`stdout` に出力されたプレーンテキストは無視されます。

`stdout` に出力する JSON では、`systemMessage` と次のフック固有の形式を使用できます：

```json
{
  "decision": "block",
  "reason": "The Bash output needs review before continuing.",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The command updated generated files."
  }
}

この `additionalContext` のテキストは、開発者コンテキストに追加されます。

このイベントでは、`decision: "block"` を返しても、完了した Bash コマンドは取り消されません。
代わりに、Codex はフィードバックを記録し、そのフィードバックでツールの結果を置き換えます。
その後、フックから提供されたメッセージをもとにモデルの処理を続行します。

終了コード `2` を使用し、フィードバックの理由を `stderr` に書き込むこともできます。

コマンドの実行後に、元のツール結果に対する通常の処理を停止するには、
`continue: false` を返します。
Codex はツールの結果を、指定したフィードバックまたは停止メッセージで置き換え、そこから処理を続行します。

`updatedMCPToolOutput` と `suppressOutput` は解析されますが、まだサポートされていません。
Codex はフックの実行を失敗として記録してエラーを報告し、
ツールの結果に対する通常の処理を続行します。

#### コードモードからのツール呼び出し

モデルがコードモードを使って JavaScript からツールを呼び出す場合、そのネストされた呼び出しにフックの判断が適用されます。
`PreToolUse` は、ツールの実行を事前に停止したり、その入力を書き換えたりできます。
ブロックを指示する `PostToolUse` ではツールの副作用を取り消せませんが、
元の結果が実行中のスクリプトに渡らないようにすることはできます。

| フックの結果                                                      | コードモード側での結果                                                                                    |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `PreToolUse` がブロック                                              | ツールが実行される前に、ツールの Promise が拒否されます。                                                         |
| `PreToolUse` が `updatedInput` を返す                              | 書き換えられた入力でツールが実行され、Promise はその結果で解決されます。                      |
| `PostToolUse` が `decision: "block"` を返すか、終了コード `2` で終了する | ツールが実行された後、Promise はフックが示した理由で拒否されます。                                          |
| `PostToolUse` が `continue: false` を返す                          | Codex はモデルに渡す結果としてフックのフィードバックを使用しますが、ネストされたツール呼び出しの Promise は拒否しません。 |

### PreCompact

`PreCompact` は、Codex がチャットのコンパクションを行う前に実行されます。
`matcher` の適用対象は `trigger` で、値は `manual` と `auto` です。

[共通入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド     | 型     | 意味                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 固有の拡張。アクティブな Codex ターンの ID |
| `trigger` | `string` | コンパクションのトリガー：`manual` または `auto`  |

`stdout` に出力されたプレーンテキストは無視されます。

`stdout` に出力する JSON では、[共通の出力フィールド](#common-output-fields)を使用できます。
一致する `PreCompact` フックが `continue: false` を返した場合、
Codex はコンパクション前に停止します。

### PostCompact

`PostCompact` は、Codex がチャットをコンパクションした後に実行されます。
`matcher` は `trigger` に適用され、その値は `manual` または `auto` です。

[共通の入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド     | 型     | 意味                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 固有の拡張。アクティブな Codex ターンの ID |
| `trigger` | `string` | コンパクションのトリガー：`manual` または `auto`  |

`stdout` に出力されたプレーンテキストは無視されます。

`stdout` に出力する JSON では、[共通の出力フィールド](#common-output-fields)を使用できます。
一致する `PostCompact` フックが `continue: false` を返した場合、
Codex はコンパクション後に停止します。

### UserPromptSubmit

現在、このイベントでは `matcher` は使用されません。

[共通の入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド     | 型     | 意味                                        |
| --------- | -------- | ---------------------------------------------- |
| `turn_id` | `string` | Codex 固有の拡張。アクティブな Codex ターンの ID |
| `prompt`  | `string` | これから送信されるユーザープロンプト            |

`stdout` に出力されたプレーンテキストは、開発者コンテキストとして追加されます。

`stdout` に出力する JSON では、[共通の出力フィールド](#common-output-fields)と
次のフック固有の形式を使用できます：

```json
{
  "hookSpecificOutput": {
    "hookEventName": "UserPromptSubmit",
    "additionalContext": "Ask for a clearer reproduction before editing files."
  }
}

その `additionalContext` のテキストは、開発者コンテキストとして追加されます。

プロンプトをブロックするには、次を返します：

```json
{
  "decision": "block",
  "reason": "Ask for confirmation before doing that."
}

終了コード `2` を使用し、ブロックする理由を `stderr` に書き込むこともできます。

### SubagentStop

このイベントでは、`matcher` が `agent_type` に適用されます。

[共通の入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド                    | 型             | 意味                                         |
| ------------------------ | ---------------- | ----------------------------------------------- |
| `turn_id`                | `string`         | Codex 固有の拡張。アクティブな Codex ターンの ID  |
| `agent_id`               | `string`         | サブエージェントの識別子                     |
| `agent_type`             | `string`         | サブエージェントの種類またはプロファイル                        |
| `agent_transcript_path`  | `string \| null` | サブエージェントのトランスクリプトファイルへのパス（存在する場合）    |
| `stop_hook_active`       | `boolean`        | このサブエージェントの処理がすでに続行されたかどうか     |
| `last_assistant_message` | `string \| null` | サブエージェントの最新のアシスタントメッセージ（利用可能な場合） |

`SubagentStop` では、終了コード `0` で終了する場合、`stdout` への出力は JSON である必要があります。
このイベントでは、プレーンテキスト出力は無効です。

`stdout` に出力する JSON では、[共通の出力フィールド](#common-output-fields)を使用できます。
サブエージェントの処理を続行するよう Codex に求めるには、次を返します：

```json
{
  "decision": "block",
  "reason": "Run one more focused pass inside the subagent."
}

終了コード `2` を使用し、続行理由を `stderr` に書き込むこともできます。

一致する `SubagentStop` フックのいずれかが `continue: false` を返した場合、
他の一致する `SubagentStop` フックによる続行の判断よりも、
その結果が優先されます。

### Stop

現在、このイベントでは `matcher` は使用されません。

[共通の入力フィールド](#common-input-fields)に加えて、次のフィールドがあります：

| フィールド                    | 型             | 意味                                           |
| ------------------------ | ---------------- | ------------------------------------------------- |
| `turn_id`                | `string`         | Codex 固有の拡張。アクティブな Codex ターンの ID    |
| `stop_hook_active`       | `boolean`        | このターンが `Stop` によってすでに続行されたかどうか |
| `last_assistant_message` | `string \| null` | 最新のアシスタントメッセージの本文（利用可能な場合）       |

`Stop` では、終了コード `0` で終了する場合、`stdout` への出力は JSON である必要があります。
このイベントでは、プレーンテキスト出力は無効です。

`stdout` に出力する JSON では、[共通の出力フィールド](#common-output-fields)を使用できます。
Codex に処理を続行させるには、次を返します：

```json
{
  "decision": "block",
  "reason": "Run one more pass over the failing tests."
}

終了コード `2` を使用し、続行理由を `stderr` に書き込むこともできます。

このイベントでは、`decision: "block"` を返してもターンは拒否されません。
代わりに Codex に続行を指示し、新しい続行プロンプトを自動的に作成します。
このプロンプトは新しいユーザープロンプトとして機能し、本文には指定した `reason` が使用されます。

一致する `Stop` フックのいずれかが `continue: false` を返した場合、
その結果が、他の一致する `Stop` フックによる続行の判断より優先されます。

### Interrupt

`Interrupt` は、メインスレッドでアクティブなターンを中断したときに実行されます。
中断の記録や、フックが開始した作業の後処理に使用します。
アイドル状態のスレッドやサブエージェントでは実行されず、設定された `matcher` はすべて無視されます。

このイベントには、[共通の入力フィールド](#common-input-fields)に加えて、
中断されたターンの ID である `turn_id` と、`permission_mode` が含まれます。

コマンドフックのデフォルトのタイムアウトは 1 秒です。
設定できるタイムアウトは 1～3 秒に制限されます。フックの出力で中断を防いだり、ターンを再開したりすることはできません。
何も出力せずに終了コード `0` で終了するか、JSON を返してください。
JSON には、警告を表示するための `systemMessage` を任意で含められます。
このイベントでは、プレーンテキスト出力は無効です。

```json
{ "systemMessage": "Saved the interrupted turn to the local audit log." }

## スキーマ

  リンク先の `main` ブランチのスキーマには、現行リリースにはないフックフィールドが含まれている場合があります。
  現行リリースの動作については、このページを参照してください。

現在のワイヤ形式を正確に確認するには、
[Codex の GitHub リポジトリ](https://github.com/openai/codex/tree/main/codex-rs/hooks/schema/generated)にある生成済みのスキーマを参照してください。
