<!-- source: https://learn.chatgpt.com/ja-JP/docs/agent-configuration/subagents -->

ChatGPT Work と Codex では、専門のエージェントを並列に起動し、その結果を 1 つの応答にまとめるサブエージェントワークフローを実行できます。これは、コードベースの調査や複数段階にわたる機能実装計画の実行など、並列処理に適した複雑なタスクに特に役立ちます。

ローカルの Codex クライアントでは、タスクごとに異なるモデル構成や指示を持つカスタムエージェントも定義できます。

## 利用条件

対象アカウントでは、ChatGPT Work でサブエージェントワークフローを使用し、そのアクティビティを確認できます。

<a id="custom-agents"></a>

現行の Codex では、サブエージェントワークフローがデフォルトで有効になっています。サブエージェントのアクティビティは、ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能に表示されます。

各サブエージェントが個別にモデルを実行し、ツールを使用するため、サブエージェントワークフローは、同等の処理を単一のエージェントで実行する場合よりも多くのトークンを消費します。

ChatGPT Work では、独立して進められる作業をサブエージェントに委任するよう ChatGPT に依頼します。エージェントは ChatGPT がホストする環境で実行され、アクティビティと結果がチャットに表示されます。ほとんどの応答性能レベルでは、委任を明示的に依頼してください。Ultra では、エージェントの並列実行によって速度や品質が大きく向上する場合、ChatGPT が自ら判断して作業を委任できます。

アプリのチャットで Codex に、独立して進められる作業をサブエージェントに委任するよう依頼します。
現行のローカル版 Codex では、直接依頼した場合や、
該当する `AGENTS.md` またはスキルの指示で求められている場合に、委任が行われます。
アプリには各サブエージェントのスレッドが表示されます。
その作業内容とメインチャットに返された要約を確認できます。

対話型 CLI セッションで、Codex にサブエージェントの使用を依頼します。
Codex は、該当する `AGENTS.md` またはスキルに委任の指示がある場合、その指示に従うこともできます。
`/agent` を使用すると、実行中のエージェントスレッドを確認したり、切り替えたりできます。
メインスレッドでは、サブエージェントの結果が最終応答にまとめられます。

IDE のチャットで Codex に、独立して進められる作業をサブエージェントに委任するよう依頼します。
Codex は、該当する `AGENTS.md` またはスキルで委任が求められている場合、その指示に従うこともできます。
バックグラウンドエージェントの UI が利用できる場合は、実行中のサブエージェントがコンポーザーの上に表示されます。
パネルを展開すると、状態を確認したり、実行中のサブエージェントをすべて停止したり、
個々のサブエージェントのスレッドを開いたりできます。

## サブエージェントワークフローの利点

大きなコンテキストウィンドウを持つモデルにも限界があります。要件や制約、意思決定を扱うメインチャットに、調査メモ、テストログ、スタックトレース、コマンド出力といったノイズの多い中間出力があふれると、セッションの信頼性が時間とともに低下する可能性があります。

こうした現象は、一般に次のように表現されます。

- **コンテキスト汚染**：ノイズの多い中間出力に有用な情報が埋もれます。
- **コンテキスト劣化**：関連性の低い情報でチャットが埋まるにつれて、パフォーマンスが低下します。

詳しい背景については、Chroma による[コンテキスト劣化](https://research.trychroma.com/context-rot)の解説を参照してください。

サブエージェントワークフローでは、ノイズの多い作業をメインスレッドから切り離すことで、次のようなメリットが得られます。

- **メインエージェント** を要件、意思決定、最終出力に集中させます。
- 調査、テスト、ログ分析を担当する専門の **サブエージェント** を並列で実行します。
- サブエージェントからは、生の中間出力ではなく **要約** を返します。

作業を独立して並列に実行できる場合は、時間の短縮にもつながります。また、大規模なタスクも範囲を限定した単位に分割することで、扱いやすくなります。たとえば、Codex は数百万トークンに及ぶドキュメントの分析を小さな問題に分割し、要点を抽出してメインスレッドに返すことができます。

まずは、調査、テスト、トリアージ、要約などの読み取り中心のタスクで、エージェントの並列処理を試してください。書き込み中心のワークフローを並列化する場合は、より慎重に対応してください。複数のエージェントが同時にコードを編集すると、競合が発生し、調整のオーバーヘッドが増えるおそれがあります。

## 基本用語

Codex のサブエージェントワークフローには、次のような関連用語があります。

- **サブエージェントワークフロー**：Codex がエージェントを並列に実行し、その結果を統合するワークフロー
- **サブエージェント**：特定のタスクを処理するために Codex が起動する、委任先のエージェント
- **エージェントスレッド**：サブエージェントが作業を行うスレッドです。対応するクライアントでは、スレッドを開いて進捗や結果を確認できます。

## サブエージェントワークフローの開始

ほとんどの応答性能レベルでは、サブエージェントの使用やエージェントによる並列作業を直接依頼してください。Ultra では、ChatGPT が自ら判断し、独立して進められる適切な作業を個別の依頼なしに委任できます。

サブエージェントの使用やエージェントによる並列作業を直接依頼してください。該当するプロジェクトやスキルの指示で委任が求められている場合は、Codex がそれに従って作業を委任することもできます。

実際に手動で開始するには、「エージェントを 2 つ起動してください」「この作業を並列に委任してください」「各項目に 1 つのエージェントを使ってください」などと直接指示します。各サブエージェントが個別にモデルを実行してツールを使用するため、サブエージェントワークフローは、同等の処理を単一のエージェントで実行する場合よりも多くのトークンを消費します。

適切なサブエージェント用プロンプトには、作業の分割方法、Codex が次の処理に進む前にすべてのエージェントの完了を待つべきかどうか、返す要約や出力の内容を明記します。

```text
Review this branch with parallel subagents. Spawn one subagent for security risks, one for test gaps, and one for maintainability. Wait for all three, then summarize the findings by category with file references.

## モデルと推論設定の選択

エージェントごとに、適したモデルと推論設定は異なります。

ChatGPT Work では、コンポーザーからモデルと応答性能レベルを選択します。
選択したモデルに応じて、利用できる応答性能レベルには **軽量**、 **中**、 **高**、
**極高**、 **Max** が含まれる場合があります。 **Ultra** は、対象アカウントと対応モデルでのみ利用できます。
最大限の推論を行い、
ChatGPT が自ら判断して、適した作業をサブエージェントに委任できるようになります。

それ以外の応答性能レベルでは、作業を並列で委任したい場合、サブエージェントの使用を明示的に依頼してください。

サブエージェントのモデルも `model_reasoning_effort` も設定しない場合、サブエージェントは親エージェントのモデルと推論強度を継承します。
明示的な起動リクエストまたは `[agents]` のデフォルト設定でモデルが選択され、
推論強度の明示的な指定も事前設定もない場合は、
サブエージェントはそのモデルのデフォルトの推論強度を使用します。
タスクごとに応答性能、速度、料金のバランスを取るには、
プロンプトで特定のモデルまたは推論強度を指定するか、
`config.toml` で `[agents]` のデフォルト値を設定するか、カスタムエージェントのファイルに `model` と
`model_reasoning_effort` を直接設定してください。
たとえば、高速なスキャンには <code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> を使用し、より高度な推論には、推論強度を高く設定した <code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> を使用します。

  Codex のほとんどのタスクでは、まず{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code> を使用してください。軽めのサブエージェント作業で、より高速かつ低コストの選択肢を求める場合は、{" "}
<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code> を
  使用してください。

### モデルの選択

- **<code>{RECOMMENDED_MODEL_REFERENCES.latestCodexModel.slug}</code>**：高度な処理を担うエージェントには、まずこのモデルを使用してください。広いコンテキストを扱いながら、計画、ツールの使用、検証、完了までの対応が必要となる、不確定要素の多い複数段階の作業で最も力を発揮します。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestMiniModel.slug}</code>**：深い分析よりも速度と効率を優先するエージェントに使用します。調査、読み取り中心のスキャン、大きなファイルのレビュー、補足資料の処理などに適しています。要点をまとめた結果をメインエージェントに返す並列ワーカーにも向いています。
- **<code>{RECOMMENDED_MODEL_REFERENCES.latestNanoModel.slug}</code>**：内容が明確な作業、反復作業、大量の作業を処理する、高速で担当範囲の限定されたエージェントに使用します。

### 推論強度（`model_reasoning_effort`）

- **`ultra`**：選択したモデルがこのレベルに対応している場合に、
  最も深い推論を行うために使用します。
- **`max`** と **`xhigh`**：選択したモデルがこれらのレベルに対応している場合に、
  特に高度な推論を行うために使用します。
- **`high`**：複雑なロジックを追跡したり、前提を確認したり、エッジケースを検討したりする必要があるエージェントに使用します（レビュー担当やセキュリティ重視のエージェントなど）。
- **`medium`**：ほとんどのエージェントに適した、バランスの取れたデフォルト設定
- **`low`**：タスクが単純で、速度を最優先する場合に使用します。

推論強度を上げると、応答時間とトークン消費量が増えますが、複雑な作業の品質が向上する場合があります。詳しくは、[モデル](/ja-JP/codex/models)、[設定の基本](/ja-JP/codex/config-file/config-basic)、[構成リファレンス](/ja-JP/codex/config-file/config-reference)を参照してください。

## オーケストレーションとスレッド制御

新しいサブエージェントの起動、追加指示の振り分け、結果が返るまでの待機、エージェントスレッドの終了など、エージェント間のオーケストレーションは ChatGPT または Codex が担当します。

多数のエージェントが実行されている場合、Codex は要求されたすべての結果がそろうまで待機し、結果を統合した応答を返します。

ほとんどの応答性能レベルでは、ChatGPT は直接依頼された場合にエージェントを起動します。Ultra では、並列作業が有効な場合、ChatGPT が自ら判断して作業を委任することもできます。

現行のローカル版 Codex では、直接依頼された場合や、該当するプロジェクトまたはスキルの指示がある場合にエージェントが起動します。

実際の動作を確認するには、プロジェクトで次のプロンプトを試してください。

```text
I would like to review the following points on the current PR (this branch vs main). Spawn one agent per point, wait for all of them, and summarize the result for each point.
1. Security issue
2. Code quality
3. Bugs
4. Race
5. Test flakiness
6. Maintainability of the code

## サブエージェントの管理

**サブエージェント** を開くと、読み取り専用の **アクティブ** と **完了** の一覧が表示されます。
完了したサブエージェントを選択すると、詳細と結果を確認できます。
ウェブのサイドバーにはサブエージェントのアクティビティが表示されますが、
個々のサブエージェントを停止したり、追加指示を出したりする操作はできません。

- メインスレッドに表示されるアクティビティからサブエージェントのスレッドを開き、作業内容を確認します。
- 実行中のサブエージェントへの追加指示や停止、完了したサブエージェントのスレッドを閉じる操作は、Codex に直接依頼してください。

  

  

- CLI で `/agent` を使用して、アクティブなエージェントスレッドを切り替え、実行中のスレッドを確認します。
- Codex に直接依頼すると、実行中のサブエージェントに追加指示を出したり、停止したり、完了したエージェントスレッドを閉じたりできます。

- バックグラウンドエージェントパネルを利用できる場合は、展開して稼働状況を確認したり、アクティブなサブエージェントを停止したり、サブエージェントスレッドを開いたりできます。
- Codex に直接依頼すると、実行中のサブエージェントに追加指示を出したり、停止したり、完了したサブエージェントスレッドを閉じたりできます。

## 承認とサンドボックスの制御

サブエージェントは現在のサンドボックスポリシーを継承します。

ChatGPT Work は自身のホスト環境でサブエージェントを実行し、ローカルの Codex サンドボックスや承認モードを制御する機能は提供しません。サブエージェントは親チャットで利用可能なツールを使用します。ウェブサイトとコネクタの権限は、引き続きツールごとに管理されます。

サブエージェントはコンポーザーの下で選択した権限モードを継承します。Codex に作業の委任を依頼する前に、親ターンの権限モードを選択してください。

対話型 CLI セッションでは、メインスレッドを表示している間でも、
非アクティブなエージェントスレッドからの承認リクエストが表示されることがあります。
承認オーバーレイにはリクエスト元のスレッドラベルが表示されます。`o` を押すと、
リクエストを承認、拒否、または回答する前に、そのスレッドを開くことができます。

非対話型フローの場合や、実行中に新しい承認リクエストを表示できない場合は、新たな承認が必要な操作が失敗し、Codex がそのエラーを親のワークフローに返します。

Codex は子エージェントを起動する際、親ターンで現在有効なランタイムの上書き設定も再適用します。
これには、セッション中に対話形式で設定したサンドボックスや承認の選択内容が含まれます。
たとえば、`/permissions` による変更や `--yolo` の指定は、
選択したカスタムエージェントファイルに別のデフォルト値が設定されていても適用されます。

サブエージェントはコンポーザーの下で選択した権限モードを継承します。Codex に作業の委任を依頼する前に、親ターンの権限モードを選択してください。

個々の[カスタムエージェント](#custom-agents)のサンドボックス構成を上書きし、特定のエージェントが読み取り専用モードで動作するよう明示的に指定することもできます。

## カスタムエージェント

Codex には、次の組み込みエージェントが付属しています：

- `default`：汎用のフォールバックエージェント
- `worker`：実装と修正を担う、実行重視のエージェント
- `explorer`：読み取り中心のコードベース調査エージェント

独自のカスタムエージェントを定義するには、
個人用エージェントの場合は `~/.codex/agents/` に、プロジェクト単位のエージェントの場合は `.codex/agents/` に、
独立した TOML ファイルを追加します。

各ファイルで 1 つのカスタムエージェントを定義します。Codex はこれらのファイルを、起動したセッションの構成レイヤーとして読み込むため、カスタムエージェントでは通常の Codex セッション構成と同じ設定を上書きできます。この仕組みは専用のエージェントマニフェストよりも扱いが煩雑に感じられることがあり、作成や共有の仕組みが成熟するにつれて形式が変わる可能性があります。

独立した各カスタムエージェントファイルでは、次の項目を定義する必要があります：

- `name`
- `description`
- `developer_instructions`

カスタムエージェントファイルで `model` または `model_reasoning_effort` を設定している場合は、そのファイル内の値が優先されます。
ファイルを適用する前に、Codex は各設定の値を次の優先順位で決定します。
まず起動時に明示した値、次に対応する `[agents]` のデフォルト値、
最後に親の値です。明示的な起動リクエストまたは `[agents]` のデフォルト値でモデルを選択し、
いずれにも推論強度が指定されていない場合は、そのモデルのデフォルト推論強度を使用します。
`model` のみを設定したカスタムエージェントファイルでは、それ以前に決定された推論強度が維持されます。
選択したモデルがその推論強度に対応していない場合や、別の推論強度を使用したい場合は、
ファイル内で `model_reasoning_effort` も設定してください。
`sandbox_mode`、`mcp_servers`、
`skills.config` などのその他のセッション設定は、
カスタムエージェントファイルで省略すると親から継承されます。

### グローバル設定

サブエージェントのグローバル設定は、引き続き[構成](/ja-JP/codex/config-file/config-basic#configuration-precedence)の `[agents]` にあります。

| フィールド                                       | 型    | 必須 | 目的                                                             |
| ------------------------------------------- | ------- | :------: | ------------------------------------------------------------------- |
| `agents.enabled`                            | ブール値 |    いいえ    | マルチエージェントツールを有効または無効にします。                                |
| `agents.max_concurrent_threads_per_session` | 数値  |    いいえ    | メインのスレッドを除き、起動したエージェントのスレッドを同時に開いておける数に上限を設定します。 |
| `agents.default_subagent_model`             | 文字列  |    いいえ    | 起動するエージェントのデフォルトモデルを設定します。                           |
| `agents.default_subagent_reasoning_effort`  | 文字列  |    いいえ    | 起動するエージェントのデフォルト推論強度を設定します。                |
| `agents.interrupt_message`                  | ブール値 |    いいえ    | エージェントのターンが中断されたときに、モデルが参照できるメッセージを記録します。   |

**注：**

- `agents.enabled` のデフォルトは `true` です。マルチエージェントツールを無効にするには、`false` に設定します。
- `agents.max_concurrent_threads_per_session` を未設定にすると、Codex がデフォルトを選択します。既存の構成では、引き続き `agents.max_threads` を従来のエイリアスとして使用できます。
- 起動時に明示した値は、`agents.default_subagent_model` と `agents.default_subagent_reasoning_effort` を上書きします。
- `agents.interrupt_message` のデフォルトは `true` です。モデルが参照できる中断メッセージをエージェントのコンテキストから除外するには、`false` に設定します。
- カスタムエージェントの名前が `explorer` などの組み込みエージェントと一致する場合は、カスタムエージェントが優先されます。

### カスタムエージェントファイルのスキーマ

| フィールド                    | 型   | 必須 | 目的                                                         |
| ------------------------ | ------ | :------: | --------------------------------------------------------------- |
| `name`                   | 文字列 |   はい    | Codex がこのエージェントを起動または参照するときに使用するエージェント名です。 |
| `description`            | 文字列 |   はい    | Codex がこのエージェントを使用すべき場面を示す、利用者向けの説明です。     |
| `developer_instructions` | 文字列 |   はい    | エージェントの動作を定義する基本的な指示です。             |

カスタムエージェントファイルには、サポートされている他の `config.toml` キーも含められます。たとえば、`model`、`model_reasoning_effort`、`sandbox_mode`、`mcp_servers`、`skills.config` です。

Codex は `name` フィールドでカスタムエージェントを識別します。
ファイル名をエージェント名に合わせるのが最も簡単な命名規則ですが、正式な識別基準は `name` フィールドの
値です。

### カスタムエージェントの例

優れたカスタムエージェントは、用途が限定され、明確な方針を持っています。各エージェントに明確な役割と、その役割に適したツールを割り当て、担当外の作業に逸脱しないよう指示してください。

#### 例 1：PR レビュー

このパターンでは、それぞれ役割を絞った 3 つのカスタムエージェントでレビューを分担します。

- `pr_explorer` はコードベースの構造を把握し、根拠を収集します。
- `reviewer` は、正確性、セキュリティ、テストに関するリスクを調査します。
- `docs_researcher` は、専用の MCP サーバーを通じてフレームワークまたは API のドキュメントを確認します。

プロジェクト設定（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 8

`.codex/agents/pr-explorer.toml`：

```toml
name = "pr_explorer"
description = "Read-only codebase explorer for gathering evidence before changes are proposed."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Stay in exploration mode.
Trace the real execution path, cite files and symbols, and avoid proposing fixes unless the parent agent asks for them.
Prefer fast search and targeted file reads over broad scans.
"""

`.codex/agents/reviewer.toml`：

```toml
name = "reviewer"
description = "PR reviewer focused on correctness, security, and missing tests."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "read-only"
developer_instructions = """
Review code like an owner.
Prioritize correctness, security, behavior regressions, and missing test coverage.
Lead with concrete findings, include reproduction steps when possible, and avoid style-only comments unless they hide a real bug.
"""

`.codex/agents/docs-researcher.toml`：

```toml
name = "docs_researcher"
description = "Documentation specialist that uses the docs MCP server to verify APIs and framework behavior."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Use the docs MCP server to confirm APIs, options, and version-specific behavior.
Return concise answers with links or exact references when available.
Do not make code changes.
"""

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

この構成は、次のようなプロンプトに適しています。

```text
Review this branch against main. Have pr_explorer map the affected code paths, reviewer find real risks, and docs_researcher verify the framework APIs that the patch relies on.

#### 例 2：フロントエンド統合のデバッグ

このパターンは、UI のリグレッション、不安定なブラウザ操作フロー、アプリケーションコードと実行中のプロダクトにまたがる統合バグへの対応に役立ちます。

プロジェクト設定（`.codex/config.toml`）：

```toml
[agents]
max_concurrent_threads_per_session = 6

`.codex/agents/code-mapper.toml`：

```toml
name = "code_mapper"
description = "Read-only codebase explorer for locating the relevant frontend and backend code paths."
model = "gpt-5.6-luna"
model_reasoning_effort = "medium"
sandbox_mode = "read-only"
developer_instructions = """
Map the code that owns the failing UI flow.
Identify entry points, state transitions, and likely files before the worker starts editing.
"""

`.codex/agents/browser-debugger.toml`：

```toml
name = "browser_debugger"
description = "UI debugger that uses browser tooling to reproduce issues and capture evidence."
model = "gpt-5.6-terra"
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"
developer_instructions = """
Reproduce the issue in the browser, capture exact steps, and report what the UI actually does.
Use browser tooling for screenshots, console output, and network evidence.
Do not edit application code.
"""

[mcp_servers.chrome_devtools]
url = "http://localhost:3000/mcp"
startup_timeout_sec = 20

`.codex/agents/ui-fixer.toml`：

```toml
name = "ui_fixer"
description = "Implementation-focused agent for small, targeted fixes after the issue is understood."
model = "gpt-5.3-codex-spark"
model_reasoning_effort = "medium"
developer_instructions = """
Own the fix once the issue is reproduced.
Make the smallest defensible change, keep unrelated files untouched, and validate only the behavior you changed.
"""

[[skills.config]]
path = "/Users/me/.agents/skills/docs-editor/SKILL.md"
enabled = false

この構成は、次のようなプロンプトに適しています。

```text
Investigate why the settings modal fails to save. Have browser_debugger reproduce it, code_mapper trace the responsible code path, and ui_fixer implement the smallest fix once the failure mode is clear.
