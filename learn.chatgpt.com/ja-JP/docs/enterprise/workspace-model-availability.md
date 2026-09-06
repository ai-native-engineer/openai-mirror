<!-- source: https://learn.chatgpt.com/ja-JP/docs/enterprise/workspace-model-availability -->

利用できるモデルは、プロダクトの利用環境とサインイン方法によって異なります。ChatGPT ワークスペースのモデル設定は、ChatGPT デスクトップアプリ内の Codex、Codex CLI、IDE 拡張機能、Codex Cloud、OpenAI API に自動的には適用されません。

管理体系の全体像については、
[ロールとワークスペースの権限](/ja-JP/codex/enterprise/roles-and-workspace-permissions)を参照してください。

## モデルアクセスの適用範囲の確認

| プロダクトまたは認証の境界                                                         | モデルアクセスの決定要因                                                                                  | 最新情報の参照先                                                                                                                |
| ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| ChatGPT ワークスペース                                                                          | ワークスペースのプラン、メンバーのアクセス権、ワークスペース設定、サポートされているロールの権限                 | [ChatGPT Enterprise と Edu のモデルと制限](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits) |
| ChatGPT でサインインして利用する ChatGPT デスクトップアプリ内の Codex、Codex CLI、IDE 拡張機能        | 利用するクライアントがサポートするモデルと、サインイン中の ChatGPT アカウントに付与されているアクセス権    | [Codex のモデル](/ja-JP/codex/models)とワークスペースに関する最新ガイダンス                                                                  |
| Codex Cloud                                                                                | ホスト型 Codex ワークフローがサポートするモデルと、サインイン中の ChatGPT アカウントに付与されているアクセス権 | [Codex のモデル](/ja-JP/codex/models)と [Codex Cloud](/ja-JP/codex/cloud)                                                                 |
| API キー認証を使用する ChatGPT デスクトップアプリ内の Codex、Codex CLI、IDE 拡張機能 | キーに関連付けられた OpenAI API の組織とプロジェクト                                       | [認証](/ja-JP/codex/auth)と [API プラットフォーム](https://platform.openai.com/docs/overview)                        |

ユーザーが実際に利用しているプロダクトの利用環境について、参照先で最新情報を確認してください。モデルカタログを転記したり、ChatGPT のモデル選択設定が、ChatGPT デスクトップアプリ内の Codex、Codex CLI、IDE 拡張機能、Codex Cloud、API プラットフォームにも同じように適用されると考えたりしないでください。

## 従業員が迷わず使い始められる初期設定

パイロットグループを招待する前に、ワークスペースの[モデル設定](https://help.openai.com/en/articles/8411955)を確認してください。
ワークスペースのオーナーと管理者は、
チャット用と Work および Codex 用の初期設定を個別に構成できます。
対応している場合は、チャット、Work、ローカルの Codex について、開始時のモデル、推論レベル、速度、
新しいチャットの動作を選択してください。

これらの選択肢は権限ではなく、デフォルト設定として扱ってください。利用できるモデルは、メンバーのシート、ロール、ワークスペースまたは API の認証主体、強制適用されるワークスペースの要件、実際に利用しているプロダクトの利用環境によって決まります。初期設定によって、利用できないモデルへのアクセス権を付与したり、これらの要件を上書きしたりすることはできません。Codex Cloud ではデフォルトのモデルを変更できません。

Fast モードの利用可否は、ワークスペース、プロダクトの利用環境、
および強制適用される `features.fast_mode` 設定によって決まります。
この設定は [`requirements.toml`](/ja-JP/codex/config-file/config-reference#requirementstoml) で指定されます。
管理対象のローカル Codex クライアントでは、この設定で Fast モードをオンまたはオフに固定できます。
これは初期設定ではなく、ワークスペースやプロダクトでの利用可否を上書きすることもできません。

## Enterprise での GPT-6 Astra

初期ロールアウトでは、管理者が Astra を有効にするには、組織に Daybreak へのアクセス権が必要です。
ChatGPT Enterprise では、提供開始後の最初の 2 週間、
Astra はデフォルトでオフになっています。対象ワークスペースの管理者は、
チャット、Work、Codex で、
ユーザーまたはグループに対して Astra を有効にできます。既存のプロダクトの利用資格要件は引き続き適用されます。
[ワークスペースのモデル設定](https://help.openai.com/en/articles/8411955)を確認し、
パイロットグループが使用する各クライアントで利用できることを確認してください。

アクセスを有効にすることと、開始時のモデルを選ぶことは別の判断です。
Astra をデフォルトに設定する前に、該当するシート、ロール、課金形態を確認してください。
利用枠と課金については[料金](/ja-JP/codex/pricing)を、
レビューのために一時停止するタスクについては[安全性の監視](/ja-JP/codex/agent-approvals-security#safety-monitoring-and-paused-tasks)を
参照してください。

API キーでサインインする場合、Astra へのアクセスは、キーに関連付けられた API の組織とプロジェクトによって決まります。ChatGPT ワークスペースで Astra を有効にしても、API へのアクセス権は付与されません。API キーによる早期アクセスには、クライアントの設定も必要です。セットアップ手順は OpenAI のアカウント担当チームにお問い合わせください。モデルの選択やローカル設定の変更だけでは、アクセス権は付与されません。

## GPT-5.4 の提供終了への準備

2026 年 8 月 31 日に、ChatGPT でサインインしているユーザー向けの Codex では、GPT-5.4 と GPT-5.4 mini の提供が終了します。それまでに、対象となるワークスペースのデフォルト設定、保存済みのモデル設定、管理対象の設定、カスタムエージェント、スケジュール済みタスクを次のように更新してください。

- `gpt-5.4` を `gpt-5.6-terra`（GPT-5.6 Terra）に置き換えてください。
- `gpt-5.4-mini` を `gpt-5.6-luna`（GPT-5.6 Luna）に置き換えてください。

OpenAI API と、自身の API キーで認証した Codex は影響を受けません。
移行の詳細については、[Codex のモデル](/ja-JP/codex/models#deprecated-codex-models)と
[管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)を
参照してください。

## モデルアクセスと実行時権限の分離

モデルアクセスによって、対応するプロダクトの利用環境で認証済みユーザーがモデルを利用できるかどうかが決まります。ローカルの権限プロファイルと管理対象の要件によって、ローカル実行の開始後にエージェントが行える操作が決まります。たとえば、変更できるファイルやアクセスできるネットワーク接続先などです。

権限プロファイルでモデルへのアクセス権を付与することはできません。また、モデルアクセスによって、実行に適用されるサンドボックス、承認ポリシー、ネットワーク制御、ソースシステムの権限による制限が緩和されることもありません。

## モデルアクセスのトラブルシューティング

ユーザーが想定しているモデルを選択できない場合は、次の点を確認してください。

- プロダクトの利用環境とサインイン方法を確認します。
- ChatGPT ワークスペース、または API プラットフォームの組織とプロジェクトを確認します。
- その認証境界に現在適用されているアクセス制御を確認します。
- 選択したローカルクライアントまたは Codex Cloud が、そのモデルをサポートしているか確認します。

## 最新情報の参照先

- [ChatGPT Enterprise と Edu のモデルと制限](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-models-limits)
- [ワークスペース設定の管理](https://help.openai.com/en/articles/8411955)
- [ロールベースのアクセス制御](https://help.openai.com/en/articles/11750701-rbac)
- [Codex のモデル](/ja-JP/codex/models)
- [プラン別の Codex 機能の利用可否](/ja-JP/codex/pricing#feature-availability)
- [認証](/ja-JP/codex/auth)

## 関連ドキュメント

- [管理者向けロールアウトガイド](/ja-JP/codex/enterprise/admin-setup)
- [グループとプロビジョニング](/ja-JP/codex/enterprise/groups-and-provisioning)
- [ロールとワークスペースの権限](/ja-JP/codex/enterprise/roles-and-workspace-permissions)
- [管理対象の設定](/ja-JP/codex/enterprise/managed-configuration)
