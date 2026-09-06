<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/admin-plugin -->

このガイドを使って、Admin プラグインが一般的な管理業務をどう支援するかを理解し、タスクの準備を進め、適切な承認とコンテキストをそろえて主要なユースケースのプロンプトを試してみてください。

## 1. Admin プラグインの用途

Admin プラグインは、ChatGPT Work 内で設定、権限、制御を直接管理できるよう支援するために設計されています。日常的な言葉で目的を伝えると、プラグインが必要な入力情報を集め、現在の状態を読み取り、確認した内容を説明して、対応可能な次の手順を案内します。

### Admin プラグインの役割

- API リクエストを自分で書かなくても、管理業務の依頼を明確なワークフローにまとめます。
- 判断や変更の承認を行う前に、ワークスペースの現在の状態をレビューします。
- 回答の根拠となる、利用が許可されたソースとフィールドを示し、検証できなかった点も明らかにします。
- 対応可能な変更を行う前にレビューのために一時停止し、変更後はレコードを再度読み取って結果を確認します。

プラグインは、内部で特定の管理 API と、承認済みの接続されたデータソースを使用します。すべての管理システムを統合したり、利用者の権限を拡張したり、あらゆる API 操作を ChatGPT で利用できるようにしたりするものではありません。プラグインが読み取りや変更を行える範囲は、引き続きデータを所有するシステムが制御します。

### 管理 API の役割

管理 API は、ソフトウェアがデータや対応可能な操作を要求するための構造化された方法を提供します。組織は管理 API を使って、内部プロセスや外部ツールを構築できます。代表的な例として、定期レポート、多数のレコードに対する反復作業、承認済みシステムとの接続があります。通常、これらのワークフローには、エンジニアリング、セキュリティ、ガバナンスの観点からのレビューが必要です。

このガイドを利用するために API ワークフローを構築する必要はありません。以降は Admin プラグインを中心に説明します。また、ChatGPT ワークスペースの管理と API プラットフォームの管理は引き続き別々で、それぞれに権限と認証の要件があります。

### 認証情報の保護

組織が承認した接続とシークレット保管システムのみを使用してください。実際の管理 API キーを ChatGPT、Codex、ドキュメント、ソースファイルに決して貼り付けないでください。

## 2. Admin プラグインの利用準備

対応している単発のタスクを日常的な言葉で進めたい場合は、Admin プラグインを使用します。目的を説明し、固定 ID、またはレポート作成用の承認済みコンテキストを提供してください。プラグインは、確認できた内容や変更予定の内容を提示するので、それを見て続行するかどうかを判断できます。

プラグインが使用するのは、そのタスクで利用を許可されたソース、認証情報、操作だけです。すべての管理システムを統合したり、権限を拡張したりするものではありません。正しい情報の基準は、引き続き元のシステムです。

### 始める前の確認事項

1. レコードがどの管理領域にあるかを確認します。
2. 必要な入力情報をそろえ、承認を得ます。
3. 読み取り専用のリクエストから始めます。
4. どのソースとフィールドを使ったか、何を検証できなかったかをプラグインに尋ねます。
5. 対応している変更を行う場合は、承認する前に計画をレビューします。その後、レコードを再度読み取って結果を確認するようプラグインに依頼します。

ワークスペースでプラグインを利用できることと、必要な権限があることを確認してください。以下のロールとアクセスに関するユースケースは、現時点で文書化されているプラグインの対応範囲に沿ったものです。プラグインは、ロール、機能の権限、ユーザーやグループへの割り当てをレビューできます。あなたが確認した後は、既存のグループに既存のロールを割り当てることもできます。

プラグインでは、ロールの作成、ロールの権限の変更、特定のコネクタへのアクセスの確認はできません。

分析のユースケースには、承認済みの接続されたデータソースへのアクセスが必要です。ROI 分析には、ビジネスまたはエンジニアリングの成果に関する承認済みの情報も必要で、利用記録だけでは不十分です。

## 3. Admin プラグインの主なユースケース

ユースケースを選び、各プレースホルダーを承認済みリクエストの値に置き換え、手順に沿って順番に進めます。タスクがプラグインの対応範囲内の変更で、すでに承認を得ている場合を除き、読み取り専用のリクエストから始めてください。

### ワークスペースのロール一覧の表示

**プロンプト例**

```text
List the roles in workspace {workspace_id}. Separate built-in and custom roles. For each role, explain which features it can use and show the users or groups assigned to it. Don’t make changes.

**手順**

1. **準備：** ワークスペース ID と、この情報を閲覧する権限があることを確認します。
2. **実行：** 読み取り専用でロール一覧を取得するよう依頼します。
3. **レビュー：** ロールの種類、機能へのアクセス、割り当てを確認します。
4. **検証：** 予期しない点があれば、変更を加えずに調べます。

### 個別のロールのレビュー

**プロンプト例**

```text
Review role {role_id}. Explain its permissions in plain language, show who has it, and flag anything that looks broader than expected. Don’t edit the role.

**手順**

1. **準備：** ロール ID とワークスペースを確認します。
2. **実行：** 読み取り専用でロールをレビューするよう依頼します。
3. **レビュー：** 権限と割り当てが、そのロールの目的に合っているかを確認します。
4. **検証：** ロールの所有者への質問を書き留めます。プラグインではロールを作成したり、その権限を編集したりできない点に注意してください。

### ユーザーやグループのアクセス権の把握

**プロンプト例**

```text
Help me understand the access for user {user_id} or group {group_id}. Show their assigned roles, explain what access those roles provide, and point out overlaps or gaps. Clearly say what you can’t verify.

**手順**

1. **準備：** ユーザーやグループの固定 ID を使用します。
2. **実行：** アクセス権を説明するようプラグインに依頼します。
3. **レビュー：** 割り当てられているロールと、それらのロールで付与されるアクセス権を確認します。重複や不足があれば記録します。
4. **検証：** プラグインから参照できない情報がある場合は、推測せず「不明」と記録します。

### グループへの既存ロールの割り当て

**プロンプト例**

```text
Before making a change, show the current roles for group {group_id} and explain what role {role_id} would add. Confirm the recorded approver and wait for my explicit approval. After the assignment, verify the group’s updated roles.

**手順**

1. **準備：** グループ ID とロール ID を確認します。承認済みのリクエストと、記録されている承認者を確認します。
2. **実行：** 現在のロールと変更予定の内容を示すようプラグインに依頼します。
3. **レビュー：** 計画が承認済みのリクエストと一致している場合にのみ承認します。
4. **検証：** 割り当て後にグループを再確認し、既存のロールが承認どおりに追加されていることを確認します。

### コネクタに関する一般的な権限の確認

**プロンプト例**

```text
Check whether user {user_id} has general connector access through their assigned roles. Ask the plugin to show which permissions support its answer. If it can’t verify access to a specific connector, have it say so clearly.

**手順**

1. **準備：** ユーザー ID と、そのユーザーのアクセス権をレビューする権限があることを確認します。
2. **実行：** 一般的な権限の確認を依頼します。
3. **レビュー：** 割り当てられたロールと、回答の根拠となった権限を確認します。
4. **検証：** これは一般的な権限の確認にのみ使用します。特定のコネクタや接続先の項目にアクセスできることを証明するものではありません。

### 承認済みの変更のトラブルシューティング

**プロンプト例**

```text
Review approved change {change_record_id}. Compare the requested result with the current workspace. If it failed, check the workspace and role first. Then confirm who owns the record, explain the issue, and suggest the safest next step.

**手順**

1. **準備：** 承認済みの変更記録と、意図した結果を確認します。
2. **実行：** リクエストとワークスペースの現在の状態を比較するよう、プラグインに依頼します。
3. **レビュー：** ワークスペースとロールを確認します。次に、レコードの所有者を確認します。
4. **検証：** 次の手順を選ぶ前に、ワークスペースの現在の状態を確認し、それを判断の基準とします。

### コストとモデルの組み合わせの最適化

**プロンプト例**

```text
For {date_range} in workspace {workspace_id}, group verified token use and cost by use case. Compare models and reasoning modes using the speed and quality information available. Flag costly workflows when the data shows little evidence of value. Recommend where spending could be reduced or redirected toward work with stronger productivity or cost results. Include any approved revenue or quality signals. Estimate possible savings, explain tradeoffs, and separate verified observations from assumptions or missing inputs. Keep this read-only.

**手順**

1. **準備：** ワークスペースと対象期間を確認し、コストデータが期間全体を網羅していることを確かめます。承認済みのパフォーマンスや成果に関するフィールドのうち、どれが利用可能かを確認します。
2. **実行：** コストとモデルの比較を依頼します。
3. **レビュー：** データからわかることを、仮定、不足している入力情報、トレードオフと区別します。
4. **検証：** 実行に移す前に、コスト削減の見込みを Finance およびワークフローの責任者と確認します。

### 利用状況と定着状況の把握

**プロンプト例**

```text
Analyze workspace {workspace_id} during {date_range}. Show tasks and token use by team and business function. Group cost by use case. Summarize what teams use ChatGPT and Codex to accomplish. Include examples from Legal, Marketing, and Sales. Compare available use of skills and plugins. Only report tool calls, connected apps, and multi-tool workflows if those fields are available. Show where teams use more advanced workflows and where there may be room to expand. Rank the top {5_or_10} use cases and show whether a small group of highly active users accounts for most usage. Don’t guess about activity that is not in the data.

**手順**

1. **準備：** ワークスペース、対象期間、チームのマッピングを確認します。ユーザー単位のレポート作成が承認されていることを確かめます。
2. **実行：** 利用状況と定着状況の分析を依頼します。
3. **レビュー：** 要求したフィールドのうち、どれが利用可能かを確認します。データのないアクティビティは推測で補わず、対象から外します。
4. **検証：** 利用量が多くても、高度な活用、ビジネス価値、個人の業績を証明するものではありません。

### ビジネス価値と ROI の測定

**プロンプト例**

```text
For workspace {workspace_id} in {date_range}, combine verified usage and cost with approved outcomes. Estimate value by team and use case. Include approved Sales measures for productivity, revenue, and quality. Compare teams and models, as well as workflows and user segments. Rank returns against cost. Show the sources and formula. Clearly state assumptions, limits, and missing inputs. Don’t claim ChatGPT caused the outcomes. Keep this read-only.

**手順**

1. **準備：** ワークスペースと対象期間を確認してから、承認済みの成果情報を確認します。計算式とプライバシーに関するルールをレビューします。
2. **実行：** ROI 分析を依頼します。
3. **レビュー：** すべての情報源と仮定を確認します。制約や不足している入力情報を一つずつ記録します。
4. **検証：** 利用状況だけでは ROI や因果関係を証明できません。結果を Finance および事業責任者とレビューします。

### Codex の ROI の評価

**プロンプト例**

```text
For workspace {workspace_id}, combine verified Codex usage and cost from {date_range} with approved engineering outcomes. Estimate ROI by team, repository, and workflow. Compare productivity and delivery speed with code quality and engineering cost. Identify workflows that show high value or use many resources. Recommend changes to the model, reasoning mode, or workflow. Explain the tradeoffs and uncertainty. Present the findings as patterns in the available data, not proof that Codex caused the outcome. Return findings only; do not make changes.

**手順**

1. **準備：** ワークスペースと報告対象期間を確認します。チームとリポジトリのマッピング、および承認済みのベースラインデータをレビューします。
2. **実行：** Codex の ROI 分析を依頼します。
3. **レビュー：** 観測されたパターンと仮定を区別します。ユーザーとリポジトリのデータを保護します。
4. **検証：** 推奨事項と成果のベースラインをエンジニアリング部門とレビューします。

## 4. API ワークフローを検討する場面

API を使って独自の管理プロセスや外部ツールを構築している組織もあります。この方法は、スケジュールに沿った作業や継続的な作業に対応できます。また、多数のレコードを扱う処理や、承認済みの社内システムとの接続が必要な処理にも役立ちます。これは、Admin プラグインの案内に沿って作業する方法とは別のものです。

まず、対象となる管理タスクを明確にします。必要な入力情報と権限、レビューのポイント、期待する結果、その結果の記録方法を洗い出します。組織でこのタスクを自動化する場合は、適切なエンジニアリング、セキュリティ、ガバナンスの各チームと連携し、認証情報を承認済みのシークレット保管先に保存し、デプロイ前にワークフローをテストします。

### 関連リソース

- [ChatGPT ワークスペースの Admin API リファレンス](https://chatgpt.com/public/admin/api-reference)
- [管理範囲の区分](/ja-JP/codex/enterprise/roles-and-workspace-permissions#understand-the-control-boundaries)
- [ChatGPT ワークスペースの Analytics API](/ja-JP/codex/enterprise/analytics-api)
- [ChatGPT ワークスペースの Compliance API](/ja-JP/codex/enterprise/compliance-api)
