<!-- source: https://learn.chatgpt.com/ja-JP/docs/sandboxing/auto-review -->

自動レビューは、サンドボックス境界での手動承認を、別の
レビュー担当エージェントによるレビューに置き換えます。メインの Codex エージェントは、引き続き同じサンドボックス内で、
同じ承認ポリシー、同じネットワークとファイルシステムの制限のもとで動作します。
異なるのは、対象となる権限昇格リクエストを誰がレビューするかです。

  自動レビューが適用されるのは、承認が対話型の場合だけです。具体的には、
  `approval_policy = "on-request"`、または関連するプロンプトカテゴリを
  引き続き表示する詳細な承認ポリシーを使用している場合です。`approval_policy = "never"` では、
  レビュー対象となるものはありません。

ChatGPT デスクトップアプリで承認済みの Daybreak モデルを選択すると、そのモードが
お使いのアカウントで利用可能で、組織ポリシーで許可されている場合、権限コントロールが自動的に **代わりに承認** に
切り替わります。デスクトップアプリの `/model` コマンドを使用した場合も
同様です。そのモードを利用できない場合、現在の権限モードは
変更されません。モデルの選択によって、組織が管理する要件が
上書きされることはありません。

承認済みのセキュリティモデルで **フルアクセス** を有効にする前に、
ChatGPT デスクトップアプリには、危険なアクションに関するモデル固有の警告が表示されます。この
警告では、**代わりに承認** の使用を推奨し、次のページへのリンクを表示します：
[レビューポリシーの構成](#configuration)。この警告によって
サンドボックス境界が復元されたり、組織ポリシーが上書きされたりすることはありません。

## 自動レビューの仕組み

大まかな流れは次のとおりです：

1. メインエージェントは、`read-only` または `workspace-write` のサンドボックス内で動作します。
2. サンドボックス境界を越える必要がある場合は、承認をリクエストします。
3. 設定が `approvals_reviewer = "auto_review"` の場合、Codex は人による対応のために停止せず、その承認リクエストを
   別のレビュー担当エージェントに振り分けます。
4. レビュー担当エージェントは、アクションを実行すべきかどうかを判断し、その理由を返します。
5. アクションが承認されると、実行が続行されます。拒否された場合、メイン
エージェントには、実質的により安全な方法を見つけるか、停止して
ユーザーに確認するよう指示されます。

自動レビューはレビュー担当を切り替えるものであり、権限を付与するものではありません。自動レビューによって
`writable_roots` が拡張されたり、ネットワークアクセスが有効になったり、保護対象パスの保護が弱められたりすることはありません。自動レビューで
変わるのは、すでに承認が必要なアクションを Codex が処理する方法だけです。

## 自動レビューの実行条件

自動レビューは、通常なら人の対応を待つために処理を一時停止する承認リクエストを評価します。
対象は次のとおりです：

- サンドボックスでの権限昇格を要求する Shell または exec ツール呼び出し
- 現在のサンドボックスまたはポリシーでブロックされるネットワークリクエスト
- 許可された書き込み可能ルートの外部に対するファイル編集
- ツールのアノテーション
または設定済みの承認モードに基づいて承認が必要となる、MCP またはアプリのツール呼び出し
- コンピューターの使用による、新しいウェブサイトまたはドメインへのアクセス

自動レビューは、サンドボックス内ですでに許可されている通常のアクションには
実行されません。アクティブな `sandbox_mode` でコマンドを実行できる場合や、ツール呼び出しが
ポリシーで許可された範囲内に収まる場合、メインエージェントはレビューなしで処理を続行します。

コンピューターの使用は別のケースです。コンピューターの使用に関する App の承認は引き続き
ユーザーに直接表示されるため、自動レビューがこれらのアプリレベルのプロンプトに取って代わることはありません。

## 自動レビューのブロック対象

大まかには、自動レビューは次のようなアクションをブロックするよう設計されています：

- 非公開データ、シークレット、認証情報を信頼されていない送信先に送ること
- 認証情報、トークン、Cookie、セッション情報の探索
- 広範囲または永続的にセキュリティを弱めること
- 取り返しのつかない損害につながる重大なリスクを伴う破壊的アクション

正確なポリシーは、オープンソースの Codex リポジトリにあります：
[policy\_template.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy_template.md)
および
[policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
このポリシーは、エンタープライズ単位では `guardian_policy_config`、
ユーザー単位ではローカルの [`[auto_review].policy`](/ja-JP/codex/config-file/config-advanced#approval-policies-and-sandbox-modes) でカスタマイズできます。

## レビュー担当エージェントが参照する情報

レビュー担当エージェント自体も Codex エージェントですが、その役割はメインエージェントより限定されています：
特定の境界越えを伴うアクションを実行すべきかどうかの判断です。

レビュー担当エージェントには、簡潔なトランスクリプトと承認リクエストの正確な内容が提示されます。通常、
これにはユーザーメッセージ、ユーザーに表示されたアシスタントの更新、関連するツール
呼び出しとツール出力、承認対象として現在提案されているアクションが含まれます。また、
不足しているコンテキストを収集するために読み取り専用のチェックを実行できますが、実行することはまれです。

非表示のアシスタント推論は含まれません。自動レビューが参照するのは、保持された
チャット項目とツールの証拠であり、非公開の思考の連鎖ではありません。

## 拒否時と失敗時の動作

明示的な拒否は、通常のサンドボックスエラーとしては扱われません。Codex はレビュー理由を
メインエージェントに返し、さらに強い次の指示を追加します：

- 同じ結果を、回避策、間接実行、またはポリシーの迂回によって
実現しようとしないでください。
- 実質的により安全な代替手段がある場合にのみ続行してください。
- それ以外の場合は、停止してユーザーに確認してください。

Codex はターンごとに拒否サーキットブレーカーも適用します。現在の
オープンソース実装では、連続して `3`
回拒否された場合、または `10` 回の拒否が、同じターン内の直近 `50` 件の
レビューを対象とするローリングウィンドウ内で発生した場合、自動レビューがそのターンを中断します。

拒否以外の結果が出ると、連続拒否カウンターはリセットされます。ブレーカーが作動すると、
Codex は警告を発し、エージェントに権限昇格をさらに試行させてループさせるのではなく、
割り込みによって現在のターンを中止します。

タイムアウトは明示的な拒否とは別に表示され、メインエージェントには、
タイムアウトだけではアクションが安全でない証拠にはならないことが通知されます。

拒否されたアクションには、明示的な上書き手段もあります。現在の
オープンソース TUI では、`/approve` を実行して **自動レビューの拒否** ピッカーを開き、
最近拒否されたアクションを 1 件選んで、1 回限りの再試行を承認します。Codex は
タスクごとに最近の拒否を最大 10 件記録します。この承認の適用範囲は限定的です。対象は
拒否されたそのアクションだけで、今後の類似アクションには適用されません。同じコンテキストで 1 回再試行するための承認として
記録され、再試行時にも自動レビューが実行されます。内部では、
Codex がそのアクション専用の開発者スコープの承認マーカーを挿入します。
レビュー担当エージェントは、ユーザーによるその明示的な上書きをコンテキストとして参照しますが、引き続き
ポリシーに従います。ポリシー上、ユーザーがその種の拒否を上書きできない場合は、
再度拒否できます。

## 構成

セットアップの詳細については、次を参照してください：
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration#configure-automatic-review-policy)。

デフォルトのレビューポリシーは、オープンソースの Codex リポジトリにあります：
[core/src/guardian/policy.md](https://github.com/openai/codex/blob/main/codex-rs/core/src/guardian/policy.md)。
エンタープライズでは、管理対象の要件でテナント固有のセクションを
`guardian_policy_config` に置き換えられます。個々のユーザーが
ローカルで設定できる項目は次のとおりです：
[`[auto_review].policy`](/ja-JP/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)。
設定先は `config.toml` ですが、管理対象の要件が優先されます：

```toml
[auto_review]
policy = """
YOUR POLICY GOES HERE
"""

ポリシーをカスタマイズするには、まずデフォルトポリシーの文面全体をコピーしてから、
個別のリスクプロファイルに基づいて調整を重ねてください。

## 許可されたサイバーセキュリティ業務の構成

許可されたセキュリティ業務では、自動レビューに、書面化した
実施範囲と最小権限の [権限プロファイル](/ja-JP/codex/permissions) を組み合わせてください。
承認済みのラボターゲットを使用し、アクションと実施期間を文書化してください。また、
本番システム、無関係なホスト、認証情報、永続的な変更は、明示的に許可されていない限り
対象外にしてください。

`[auto_review].policy` と `guardian_policy_config` はどちらも、現在の
レビューポリシーを置き換えます。モデルに同梱されているポリシーや、
組織が管理するポリシーとはマージされません。組み込みのレビュー手順と応答
形式は引き続き適用されます。いずれかの例を使用する前に、現在の
ポリシー全体をコピーし、既存のルールをすべて保持したうえで、承認済みの業務に必要なルールを追加してください。
大文字のプレースホルダーを、その完全なポリシーで置き換えてください。現在のポリシーに
アクセスできない場合は、上書きしないでください。

次のローカル `config.toml` テンプレートはレビューを有効にし、既存のレビューポリシーの後に、適用範囲を限定した
条件を追加します：

```toml
approval_policy = "on-request"
approvals_reviewer = "auto_review"
default_permissions = ":workspace"

[auto_review]
policy = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.
- Approved actions: inspect the target, reproduce authorized vulnerabilities,
  and validate fixes within the documented engagement window.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only actions against the approved target that match the documented
  engagement scope and approved actions.
- Deny out-of-scope or unknown hosts, production access, credential theft,
  persistence, data exfiltration, destructive operations, and policy bypass.
- Deny ambiguous actions and high-impact changes until a human explicitly
  approves the exact target, action, and side effects.
"""

例の対象と許可されるアクションを、実際に承認された範囲に置き換えてください。
対象の制限は、独立したファイルシステムとネットワークのルールで適用してください。
レビュー担当エージェントへの指示は、これらの境界に代わるものではありません。

組織は、管理対象の `requirements.toml` で同じ条件を適用できます：

```toml
allowed_approval_policies = ["on-request"]
allowed_approvals_reviewers = ["auto_review"]
allowed_sandbox_modes = ["read-only", "workspace-write"]
default_permissions = ":workspace"

guardian_policy_config = """
PASTE THE COMPLETE ACTIVE REVIEWER POLICY HERE BEFORE USING THIS EXAMPLE.

## Environment Profile
- Authorized target: lab.example.com.

## Tenant Risk Taxonomy and Allow/Deny Rules
- Allow only approved actions against the documented engagement target.
- Deny out-of-scope hosts, production access, credential theft, persistence,
  data exfiltration, destructive operations, and attempts to bypass policy.
- Deny ambiguous or high-impact actions until a human explicitly approves the
  exact target, action, and side effects.
"""

[allowed_permission_profiles]
":read-only" = true
":workspace" = true
# ":danger-full-access" is omitted, so it is denied.

`allowed_permission_profiles` は現在の権限プロファイルを制御します。
`allowed_sandbox_modes` は、
従来の `sandbox_mode` を引き続き使用しているデプロイ環境でも、フルアクセスを禁止します。

管理対象の `guardian_policy_config` は、ユーザーのローカル
`[auto_review].policy` より優先されます。`approval_policy = "on-request"` または
レビューの対象となる別の対話型承認ポリシーを維持し、強制可能なサンドボックス境界も維持してください。
`approval_policy = "never"`、`:danger-full-access`、`--yolo` のいずれかを使用すると、アクションで
レビューに必要な境界越え承認リクエストが作成されない可能性があります。

許可リストにあるネットワーク送信先は、それだけではレビューをトリガーしません。サンドボックス内のアクションもレビュー担当エージェントに送る必要がある場合は、明示的なルールとして
[コマンドルール](/ja-JP/codex/agent-configuration/rules)（
`decision = "prompt"` を指定）を追加するか、機密性の高い MCP ツールで承認を必須に
設定してください。

モデルへのアクセス、業務のセットアップ、カスタムエージェントワークフローの参考資料：[モデルと信頼済みアクセス](/ja-JP/codex/cyber-safety)、[推奨
構成](/ja-JP/codex/cyber-safety/recommended-configuration)。
エンタープライズでの優先順位と対応クライアントバージョンの参考資料：[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration#configure-automatic-review-policy)。
カスタム API または
Agents SDK ハーネスでは、[ガードレールと人によるレビュー](/api/docs/guides/agents/guardrails-approvals#review-cybersecurity-actions-before-execution)を使用してください。

## セキュリティを弱めずにレビュー量を削減

自動レビューは、よく使う安全なワークフローがサンドボックスですでにカバーされている場合に最も効果を発揮します。日常的なアクションの
レビューが多すぎる場合は、ノイズの多い権限昇格を延々と承認するようレビュー担当エージェントに教えるのではなく、まず境界を
修正してください。

実際に最も効果が大きい変更は次のとおりです：

- 意図的に使用するスクラッチディレクトリや隣接リポジトリに対して、適用範囲を限定した
[`writable_roots`](/ja-JP/codex/config-file/config-advanced#approval-policies-and-sandbox-modes)
  を追加してください。
- 次を追加してください：適用範囲を限定した [プレフィックスルール](/ja-JP/codex/agent-configuration/rules)。
  `["cargo", "test"]` や `["pnpm", "run", "lint"]` のような正確なコマンドプレフィックスを、
  `["python"]` や `["curl"]` のような広範なパターンより優先してください。広範なルールによって、
  自動レビューが保護するはずの境界そのものが失われることがよくあります。

自動レビューのセッショントランスクリプトは、デフォルトで `~/.codex/sessions` 配下に
保持されます。そのため、ポリシーや権限を変更する前に、そこにある過去のトラフィックを分析するよう
Codex に依頼できます。

## 制限

自動レビューにより、長時間にわたるエージェント型の作業をデフォルトでより適切に運用できますが、
セキュリティを確実に保証するものではありません。

- 境界を越えるために承認を求めるアクションのみを評価します。
- それでも、特に敵対的な状況や通常とは異なる状況では、判断を誤る可能性があります。
- 適切なサンドボックス設計や監視、
組織固有のポリシーに代わるものではなく、それらを補完するものとして使用してください。

研究上の根拠と公開済みの評価結果については、
[自動レビューに関する Alignment Research の投稿](https://alignment.openai.com/auto-review/)をご覧ください。
