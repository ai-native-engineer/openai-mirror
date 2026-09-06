<!-- source: https://learn.chatgpt.com/ja-JP/docs/config-file/config-basic -->

Codex は複数の場所から設定情報を読み取ります。個人用のデフォルト設定は `~/.codex/config.toml` に保存され、`.codex/config.toml` ファイルでプロジェクトごとに設定を上書きできます。セキュリティ上、Codex は信頼済みのプロジェクトでのみ、プロジェクトの `.codex/` レイヤーを読み込みます。

## Codex 設定ファイル

Codex はユーザーレベルの設定を `~/.codex/config.toml` に保存します。設定の適用範囲を特定のプロジェクトやサブフォルダーに限定するには、リポジトリに `.codex/config.toml` ファイルを追加します。

Codex IDE 拡張機能から設定ファイルを開くには、右上隅の歯車アイコンを選択し、 **Codex の設定 \> config.toml を開く**を選択します。

CLI と IDE 拡張機能は同じ設定レイヤーを共有します。これらのレイヤーで、次の設定ができます。

- デフォルトのモデルとプロバイダーの設定
- [承認ポリシーとサンドボックスの設定](/ja-JP/codex/agent-approvals-security#sandbox-and-approvals)
- [MCP サーバー](/ja-JP/codex/extend/mcp)の設定

## 設定の優先順位

Codex は次の優先順位で設定値を決定します（上ほど優先）。

1. CLI フラグと `--config` による上書き
2. プロジェクト設定ファイル：`.codex/config.toml`（プロジェクトルートから現在の作業ディレクトリまで順に読み込み、現在のディレクトリに最も近いものを優先。信頼済みのプロジェクトのみ）
3. `--profile profile-name` で選択した[プロファイル](/ja-JP/codex/config-file/config-advanced#profiles)ファイル（`~/.codex/profile-name.config.toml`）
4. ユーザー設定：`~/.codex/config.toml`
5. システム設定（存在する場合）：Unix では `/etc/codex/config.toml`
6. 組み込みのデフォルト設定

この優先順位を利用して、共通のデフォルト設定を `config.toml` に記述し、[プロファイルファイル](/ja-JP/codex/config-file/config-advanced#profiles)には異なる値だけを記述します。

プロジェクトを信頼しない設定にすると、Codex はプロジェクト固有の設定、フック、ルールを含む、プロジェクトスコープの `.codex/` レイヤーを読み込みません。ユーザー設定とシステム設定は引き続き読み込まれ、ユーザーやグローバルのフックとルールも読み込まれます。

`-c`/`--config` による一時的な上書き（TOML の引用符のルールを含む）については、[高度な設定](/ja-JP/codex/config-file/config-advanced#one-off-overrides-from-the-cli)を参照してください。

  管理対象のマシンでは、組織が
`requirements.toml` を通じて制約を強制する場合もあります（たとえば、`approval_policy = "never"` や
`sandbox_mode = "danger-full-access"` の禁止）。[管理対象の
  構成](/ja-JP/codex/enterprise/managed-configuration)と[管理者が強制する
  要件](/ja-JP/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)を参照してください。

## よく使う設定オプション

よく変更されるオプションをいくつか紹介します。

#### デフォルトモデル

CLI と IDE で Codex がデフォルトで使用するモデルを選択します。

#### 承認プロンプト

Codex が生成したコマンドを実行する前に、一時停止して承認を求めるタイミングを設定します。

```toml
approval_policy = "on-request"

`untrusted`、`on-request`、`never` の動作の違いについては、[承認プロンプトなしでの実行](/ja-JP/codex/agent-approvals-security#run-without-approval-prompts)と[一般的なサンドボックスと承認の組み合わせ](/ja-JP/codex/agent-approvals-security#common-sandbox-and-approval-combinations)を参照してください。

#### サンドボックスレベル

コマンド実行中に Codex に許可する、ファイルシステムとネットワークへのアクセス範囲を調整します。

```toml
sandbox_mode = "workspace-write"

モードごとの動作（保護対象の `.git`/`.codex` パスとネットワークのデフォルト設定を含む）については、[サンドボックスと承認](/ja-JP/codex/agent-approvals-security#sandbox-and-approvals)、[書き込み可能なルート内の保護対象パス](/ja-JP/codex/agent-approvals-security#protected-paths-in-writable-roots)、[ネットワークアクセス](/ja-JP/codex/agent-approvals-security#network-access)を参照してください。

#### 権限プロファイル

Codex は、ファイルシステムと
ネットワークのポリシーを再利用するための、名前付き権限プロファイルにも対応しています。組み込みプロファイルは `:read-only`、`:workspace`、
`:danger-full-access` です。カスタムプロファイルでは `[permissions.<name>]` テーブルと、
その名前に一致する `default_permissions` の値を使用します。[権限](/ja-JP/codex/permissions)を参照してください。

#### Windows サンドボックスモード

Windows で Codex をネイティブ実行する場合は、`windows` テーブルでネイティブサンドボックスモードを `elevated` に設定します。管理者権限がない場合、または権限昇格を伴うセットアップに失敗した場合にのみ、`unelevated` を使用します。

```toml
[windows]
sandbox = "elevated"   # Recommended
# sandbox = "unelevated" # Fallback if admin permissions/setup are unavailable

#### ウェブ検索モード

Codex はローカルのチャットでウェブ検索をデフォルトで有効にし、ウェブ検索キャッシュから結果を返します。このキャッシュは OpenAI が管理するウェブ検索結果のインデックスです。キャッシュモードでは、ページをその場で取得する代わりに、事前にインデックス化された結果を返します。これにより、不特定のライブコンテンツからプロンプトインジェクションを受けるリスクは低くなりますが、ウェブ検索結果は引き続き信頼できないものとして扱う必要があります。`--yolo` または他の[フルアクセスのサンドボックス設定](/ja-JP/codex/agent-approvals-security#common-sandbox-and-approval-combinations)を使用している場合、ウェブ検索はデフォルトでライブの結果を返します。`web_search` でモードを選択します。

- `"cached"`（デフォルト）では、ウェブ検索キャッシュから結果を返します。
- `"indexed"` では、検索インデックスによるリクエストの許可判定を通過した場合にのみ、外部ウェブアクセスを許可します。
- `"live"` では、ウェブから最新のデータを取得します（`--search` と同じです）。
- `"disabled"` では、ウェブ検索ツールを無効にします。

```toml
web_search = "cached"  # default; serves results from the web search cache
# web_search = "indexed" # gate external web access through the search index
# web_search = "live"  # fetch the most recent data from the web (same as --search)
# web_search = "disabled"

#### 推論強度

対応モデルでは、推論強度を調整できます。

```toml
model_reasoning_effort = "high"

#### コミュニケーションスタイル

対応モデルのデフォルトのコミュニケーションスタイルを設定します。

```toml
personality = "friendly" # or "pragmatic" or "none"

この設定は、実行中のセッションで後から `/personality` を使って上書きできます。また、app-server API を使用する場合は、スレッド単位やターン単位で上書きできます。

#### TUI キーマップ

`tui.keymap` でターミナルのショートカットをカスタマイズします。一部のコンポーザーアクションでは、対応する `tui.keymap.global` のキーバインドがフォールバックとして使用されます。コンテキスト固有のキーバインドに対応している場合は、そちらが優先されます。空のリストを指定すると、そのアクションのキーバインドが解除されます。

```toml
[tui.keymap.global]
open_transcript = "ctrl-t"

[tui.keymap.composer]
submit = ["enter", "ctrl-m"]

[tui.keymap.chat]
interrupt_turn = "f12"

#### コマンドの実行環境

Codex が起動するコマンドに渡す環境変数を設定します。必要な変数だけを残すには、キーで指定するフィルターを使用します。

```toml
[shell_environment_policy]
ignore_default_excludes = false

[shell_environment_policy.filters]
"PATH" = "include"
"HOME" = "include"

`ignore_default_excludes` のデフォルト値は `true` です。この場合、
名前に `KEY`、`SECRET`、`TOKEN` を含む変数の自動フィルタリングは行われません。この自動フィルタリングを有効にするには、`false` に設定します。
除外ルール、優先順位、
従来の設定については、[シェル環境
ポリシー](/ja-JP/codex/config-file/config-advanced#shell-environment-policy)を参照してください。

#### ログディレクトリ

Codex がローカルログファイルを書き込む場所を変更します。`log_dir` を明示的に設定すると、
通常はオプトインが必要なプレーンテキストの TUI ログ `codex-tui.log` も、そのディレクトリで有効になります。

```toml
log_dir = "/absolute/path/to/codex-logs"

単発で実行する場合は、CLI から設定することもできます。

```bash
codex -c log_dir=./.codex-log

## 機能フラグ

`config.toml` の `[features]` テーブルで、オプション機能や実験的な機能の有効・無効を切り替えます。

### よく使う機能フラグ

| キー                  |        デフォルト        | 成熟度     | 説明                                                                              |
| -------------------- | :-------------------: | ------------ | ---------------------------------------------------------------------------------------- |
| `apps`               |         true          | 安定版       | アプリ（コネクタ）連携を有効化                                                      |
| `goals`              |         true          | 安定版       | 目標の永続化と自動継続を有効化                                        |
| `hooks`              |         true          | 安定版       | `hooks.json` またはインラインの `[hooks]` で定義したライフサイクルフックを有効にします。詳しくは、[フック](/ja-JP/codex/hooks)を参照してください。 |
| `fast_mode`          |         true          | 安定版       | Fast モードの選択と `service_tier = "fast"` による利用を有効化                          |
| `memories`           |         false         | 実験的 | [メモリ](/ja-JP/codex/customization/memories)を有効化                                         |
| `multi_agent`        |         true          | 安定版       | サブエージェントの共同作業ツールを有効化                                                      |
| `personality`        |         true          | 安定版       | パーソナリティの選択コントロールを有効化                                                    |
| `remote_plugin`      |         true          | 安定版       | リモートプラグインカタログを有効化                                                         |
| `shell_snapshot`     |         true          | 安定版       | シェル環境のスナップショットを作成し、コマンドの繰り返し実行を高速化                            |
| `shell_tool`         |         true          | 安定版       | デフォルトの `shell` ツールを有効化                                                          |
| `unified_exec`       | `true`（Windows を除く） | 安定版       | PTY をバックエンドとする統合 exec ツールを使用                                                     |
| `web_search`         |         true          | 非推奨   | 従来の切り替え設定。トップレベルの `web_search` 設定の使用を推奨                                 |
| `web_search_cached`  |         false         | 非推奨   | 未設定の場合に `web_search = "cached"` に対応する従来の切り替え設定                            |
| `web_search_request` |         false         | 非推奨   | 未設定の場合に `web_search = "live"` に対応する従来の切り替え設定                              |

  この表には、一般的なユーザー向けフラグを掲載しています。
  内部機能や開発中の機能をすべて網羅しているわけではありません。「成熟度」列では、
  「実験的」「ベータ」「安定版」などのラベルを使用しています。各ラベルの意味については、[機能の
  成熟度](/ja-JP/codex/feature-maturity)を参照してください。

機能キーを省略すると、デフォルト値が維持されます。

ライフサイクルフックの構成については、[フック](/ja-JP/codex/hooks)を参照してください。

### 機能の有効化

- `config.toml` の `[features]` の下に `feature_name = true` を追加します。
- CLI から `codex --enable feature_name` を実行します。
- 複数の機能を有効にするには、`codex --enable feature_a --enable feature_b` を実行します。
- 機能を無効にするには、`config.toml` で該当するキーを `false` に設定します。
