<!-- source: https://learn.chatgpt.com/ja-JP/docs/automations -->

定期タスクをバックグラウンドで実行するようにスケジュールできます。Web 版とモバイル版の ChatGPT では、
対象プランで、対応するアプリのイベントをきっかけにタスクを実行することもできます。アクティブなタスク、
一時停止中や完了済みのタスク、最近の実行は **スケジュール済み**で確認できます。
スケジュール済みタスクを[スキル](/ja-JP/codex/build-skills)と組み合わせると、より複雑な作業にも対応できます。

ChatGPT デスクトップアプリでは、スケジュール済みタスクでローカルプロジェクトを扱い、プロジェクトディレクトリまたは分離された Worktree で実行できます。スケジュール済みタスクでローカルファイルが必要な場合は、コンピューターの電源を入れ、アプリを起動したままにしてください。

ワークスペースでスケジュール済みタスクが有効になっている場合は、Web のチャットまたは
ChatGPT Work から作成し、 **スケジュール済み**で実行を管理します。Web のタスクは、
アップロード済みのコンテキストや接続済みのツールを使用できますが、
コンピューター上のフォルダーを直接操作することはできません。

Codex CLI には、スケジュール済みの管理インターフェースはありません。スケジュール済みタスクの作成と管理には、Web 版 ChatGPT またはデスクトップアプリを使用してください。CLI では、プロンプト、スキル、スクリプトを事前に準備してテストできます。

IDE 拡張機能には、スケジュール済みの管理インターフェースはありません。スケジュール済みタスクの作成と管理には、Web 版 ChatGPT またはデスクトップアプリを使用してください。IDE 拡張機能では、プロンプト、スキル、ワークスペースの変更を事前に準備してテストできます。

<a id="managing-tasks"></a>
<a id="ask-codex-to-create-or-update-automations"></a>
<a id="ask-chatgpt-to-create-or-update-scheduled-tasks"></a>
<a id="thread-automations"></a>
<a id="scheduled-tasks-in-threads"></a>
<a id="scheduled-tasks-in-chats"></a>
<a id="schedule-work-from-a-task"></a>
<a id="schedule-a-task-inside-a-chat"></a>
<a id="test-automations"></a>
<a id="test-scheduled-tasks"></a>
<a id="worktree-cleanup-for-automations"></a>
<a id="worktree-cleanup-for-scheduled-tasks"></a>
<a id="permissions-and-security-model"></a>
<a id="examples"></a>
<a id="automatically-create-new-skills"></a>
<a id="stay-up-to-date-with-your-project"></a>
<a id="combining-automations-with-skills-to-fix-your-own-bugs"></a>
<a id="combining-scheduled-tasks-with-skills-to-fix-your-own-bugs"></a>

## Web でのスケジュール済みタスクの管理

**スケジュール済み** を開いて、タスクの状態と最近の実行を確認します。
毎回保存済みのプロンプトから開始したい場合は、単独のスケジュール済みタスクを使用します。
ChatGPT が既存のコンテキストを使って同じチャットに戻るようにするには、
チャット内のスケジュール済みタスクを使用します。

Web のスケジュール済みタスクでは、そのチャットで利用できるアップロード済みファイル、接続済みのツール、スキル、プラグインを使用できます。実行の合間に、ローカルフォルダーや Worktree を利用可能な状態で保持することはありません。継続して使う指示はタスクのプロンプトまたは添付したスキルに含め、必要な資料は、アクセス可能なプロジェクト、アップロード済みファイル、または接続済みのサービスで利用できるようにしておいてください。

タスクをスケジュールする前に、通常の Web チャットでプロンプトをテストしてください。最初の数回の実行を確認し、結果の範囲が広すぎる場合や追加のコンテキストが必要な場合は、プロンプト、ツール、実行頻度を調整します。

## アプリのイベントをきっかけとするタスクの実行

対象プランでは、Gmail、Slack、GitHub で対応するイベントが発生したときに、スケジュール済みタスクを実行できます。イベントをトリガーとするタスクは、Web 版とモバイル版の ChatGPT で利用できます。ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能では利用できません。

ChatGPT にタスクの作成を依頼し、監視するイベントと、そのイベントが発生したときに行う処理を説明してください。トリガーはタスクを実行するタイミングを決め、保存済みのプロンプトは各実行で行う処理を決めます。1 つのタスクで複数のイベントトリガーを使用できますが、イベントトリガーと時刻に基づくスケジュールを組み合わせることはできません。

対応するイベントトリガーには、次のものがあります。

- **Gmail：** 新着メール（必要に応じて送信者や件名で絞り込み可能）
- **Slack：** 選択したチャンネルの新着メッセージが対象です。必要に応じて投稿者や、
  スレッドへの返信を含めるかどうかで絞り込めます。リアクション、編集、削除、
  ダイレクトメッセージには対応していません。
- **GitHub：** リポジトリ内の Pull Request のアクティビティが対象です。Pull Request、
  作成者、タイトル、ラベルで絞り込み、レビュー、コメント、コミットの更新のどれをトリガーにするか、
  あるいはマージのみをトリガーにするかを選択できます。

タスクを作成する前に、アプリを接続して必要な権限を付与してください。
Slack では、タスクが監視するすべてのチャンネルに `@ChatGPT` を追加します。
GitHub では、接続したアプリにリポジトリへのアクセス権が必要です。

条件に一致する複数のイベントが短時間に続けて発生すると、ChatGPT が
1 回の実行にまとめることがあります。 **スケジュール済み** を開いて保留中のイベントを確認するか、
 **今すぐ実行**を選択して処理します。

利用できるかどうかは、プランとワークスペースの設定によって異なります。
管理対象のワークスペースでは、管理者が **イベントをトリガーとする
スケジュール済みタスクを許可** 権限でアクセスを制御できます。

たとえば、テレメトリエラーを評価して修正を提出するタスクや、
コードベースの最近の変更に関するレポートを作成するタスクをスケジュールできます。
同じコンテキストを使い続ける必要がある作業では、[既存のチャット内でタスクをスケジュールします](#schedule-a-task-inside-a-chat)。

プロジェクト単位のスケジュール済みタスクを使う場合は、コンピューターの電源を入れ、ChatGPT デスクトップアプリを起動したままにしてください。タスクの実行予定時刻に、選択したプロジェクトがディスク上で引き続き利用できる必要があります。

Git リポジトリでは、スケジュール済みタスクの実行先をローカルプロジェクトか、
新しい [Worktree](/ja-JP/codex/environments/git-worktrees) から選択できます。
どちらもバックグラウンドで実行されます。Worktree では、スケジュール済みタスクによる変更を
ローカルで進めている未完了の作業から分離できます。一方、ローカルプロジェクトで実行すると、
作業中のファイルが変更される可能性があります。バージョン管理されていないプロジェクトでは、
スケジュール済みタスクはプロジェクトディレクトリで直接実行されます。

モデルと推論強度はデフォルト設定のままにすることも、スケジュール済みタスクの実行方法をより細かく制御したい場合は明示的に選択することもできます。

スケジュール済みタスクで、ChatGPT へのサインインで `gpt-5.4` または `gpt-5.4-mini` を使用している場合は、
これらのモデルが 2026 年 8 月 31 日に廃止される前に更新してください。`gpt-5.4` を
`gpt-5.6-terra` に、`gpt-5.4-mini` を `gpt-5.6-luna` に置き換えてください。

  

スケジュール済みタスクは、デフォルトのサンドボックス設定でユーザーの操作なしに実行されます。
タスクを正常に実行できる最小限のアクセス権から始め、
ネットワークアクセスや、より広範なファイルアクセスは必要な場合にのみ許可してください。詳しくは、[サンドボックスの仕組み](/ja-JP/codex/sandboxing)を参照してください。

## スケジュール済みタスクの管理

ChatGPT デスクトップアプリのサイドバーにある **スケジュール済み** で、
すべてのスケジュール済みタスクとその実行を確認できます。

**スケジュール済み** ビューは受信トレイとして機能します。報告事項のあるスケジュール済みタスクの実行が
ここに表示され、対応が必要な実行は未読マークで示されます。

  

単独のスケジュール済みタスクは、スケジュールに沿った実行のたびに新しいチャットを開始し、
結果を **スケジュール済み**に報告します。各実行を独立させたい場合や、
1 つのスケジュール済みタスクを 1 つ以上のプロジェクトで実行したい場合に使用します。
独自の実行頻度を設定するには、カスタムスケジュールの設定項目を使用します。より高度なスケジュールでは、
RFC 5545 の繰り返しルール（RRULE）を編集します。たとえば、
`RRULE:FREQ=MONTHLY;BYMONTHDAY=1;BYHOUR=9;BYMINUTE=0` のように指定します。

Git リポジトリでは、各スケジュール済みタスクをローカルプロジェクト、または
バックグラウンド実行専用の [Worktree](/ja-JP/codex/environments/git-worktrees) で実行できます。
スケジュール済みタスクによる変更を、ローカルで進めている未完了の作業から分離したい場合は、
Worktree を使用します。メインのチェックアウトを直接操作させたい場合は、
ローカルモードを使用します。ただし、現在編集中のファイルが変更される可能性がある点に注意してください。
バージョン管理されていないプロジェクトでは、スケジュール済みタスクはプロジェクトディレクトリで直接実行されます。
同じスケジュール済みタスクを複数のプロジェクトで実行することもできます。

Web の ChatGPT Work、またはデスクトップアプリの ChatGPT Work や
Codex で作成したスケジュール済みタスクは、プラグインを使用できます。スキルも使用できます。
スケジュール済みタスクを保守しやすく、チーム間で共有しやすくするには、
[スキル](/ja-JP/codex/build-skills)で処理内容を定義し、ツールとコンテキストを提供します。
ツールの自動選択に依存させたくないワークフローでは、
タスクのプロンプトで特定のスキルを選択または呼び出します。

## ChatGPT にスケジュール済みタスクの作成や更新を依頼

ChatGPT または Codex のチャットから、スケジュール済みタスクを作成、更新できます。作業内容と実行するタイミングに加え、各実行で現在のチャットに戻るか、新しいチャットを開始するかを指定してください。ChatGPT はプロンプトの下書きを作成し、適切な実行先を選択できます。また、タスクの対象範囲や実行頻度が変わったときは、タスクを更新できます。

たとえば、デプロイの完了を待つ間、現在のチャットでフォローアップするよう ChatGPT にスケジュールを依頼したり、プロジェクトを定期的に確認する単独のスケジュール済みタスクの作成を依頼したりできます。

スキルからスケジュール済みタスクを作成、更新することもできます。たとえば、Pull Request を継続的に監視するスキルで、GitHub プラグインを使って PR の状態を確認し、レビューで新たに指摘された箇所を修正するスケジュール済みタスクを設定できます。

## チャット内でのタスクのスケジュール設定

ChatGPT がスケジュールに沿って既存のチャットに戻るようにするには、そのチャット内でタスクをスケジュールします。このスケジュール済みタスクは、毎回新しいプロンプトから開始するのではなく、チャットの既存のコンテキストを使用します。

チャット内のスケジュール済みタスクでは、フォローアップを繰り返すために分単位の実行間隔を設定できます。特定の時刻に状況を確認したい場合は、日次や週次のスケジュールも使用できます。

チャット内でのタスクのスケジュール設定は、次の用途に適しています。

- 長時間実行される処理を、完了するまで確認
- 対応するアプリのイベントへの応答ではなく、定期的なスナップショットが必要な場合に、接続済みの情報源を一定の頻度で確認
- 一定の頻度でレビューループを続けるよう ChatGPT に通知
- PR の状態確認や新しいフィードバックへの対応など、プラグインを使うワークフローをスキルで実行
- コンテキストを失わずに、進行中の調査やトリアージのチャットを継続

各実行を独立させたい場合や、
報告事項を **スケジュール済み**に個別の実行として表示したい場合は、単独のスケジュール済みタスクを使用します。

チャット内でタスクをスケジュールする場合は、繰り返し使えるプロンプトにしてください。プロンプトには、各実行で ChatGPT が行うこと、報告すべき重要な事項があるかどうかの判断方法、停止するタイミングやユーザーに入力を求めるタイミングを記述します。

## スケジュール済みタスクのテスト

タスクをスケジュールする前に、まず通常のチャットでプロンプトを手動でテストしてください。これにより、次の点を確認できます。

- プロンプトが明確で、対象範囲が適切に設定されていること
- 選択済みまたはデフォルトのモデル、推論強度、ツールが期待どおりに動作すること
- 生成された出力をレビューできること

スケジュールに沿った実行を開始したら、最初の数回の出力をレビューし、必要に応じてプロンプトや実行頻度を調整します。

ChatGPT デスクトップアプリでは、スケジュール済みタスクのプロンプトで
`$skill-name` を使用すると、スキルを明示的に呼び出せます。

## スケジュール済みタスク用 Worktree のクリーンアップ

Git リポジトリで Worktree を選択した場合、実行頻度が高いと、時間の経過とともに多数の Worktree が作成されることがあります。不要になった実行はアーカイブし、その Worktree を保持する予定がない限り、実行をピン留めしないでください。

## 権限とセキュリティモデル

スケジュール済みタスクはユーザーの操作なしに実行され、デフォルトのサンドボックス設定を使用します。

これらの制限をわかりやすく説明した
[サンドボックスの概要](/ja-JP/codex/sandboxing)をご覧ください。ファイルシステムとネットワークのルールについては、
[権限](/ja-JP/codex/permissions)をご覧ください。

- サンドボックスモードが **読み取り専用**の場合、
  ファイルの変更、ネットワークへのアクセス、コンピューター上のアプリの操作のいずれかが必要なツール呼び出しは失敗します。
  サンドボックスの設定を「ワークスペースへの書き込み」に変更することを検討してください。
- サンドボックスモードが **workspace-write** の場合、
  ワークスペース外のファイルの変更、ネットワークへのアクセス、
  コンピューター上のアプリの操作のいずれかが必要なツール呼び出しは失敗します。サンドボックス外で実行するコマンドを、
  [ルール](/ja-JP/codex/agent-configuration/rules)を使って個別に許可リストに追加できます。
- サンドボックスモードが **フルアクセス**の場合、
  ChatGPT が確認せずにファイルの変更、コマンドの実行、ネットワークへのアクセスを行う可能性があるため、
  バックグラウンドで実行されるスケジュール済みタスクのリスクが高くなります。サンドボックスの設定を「ワークスペースへの書き込み」に変更し、
  [ルール](/ja-JP/codex/agent-configuration/rules)を使って、エージェントがフルアクセスで実行できるコマンドを
  個別に指定することを検討してください。

管理対象の環境では、管理者は
要件を強制適用することで、これらの動作を制限できます。たとえば、`approval_policy =
"never"` を禁止したり、許可するサンドボックスモードを制限したりできます。
[管理者が強制する要件（`requirements.toml`）](/ja-JP/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)をご覧ください。

組織のポリシーで許可されている場合、スケジュール済みタスクは `approval_policy = "never"` を使用します。
管理者の要件によって `approval_policy = "never"` が禁止されている場合は、
スケジュール済みタスクには、選択した権限モードの
承認動作が代わりに適用されます。

## 例

### 新しいスキルの自動作成

```markdown
Scan all of the `~/.codex/sessions` files from the past day and if there have been any issues using particular skills, update the skills to be more helpful. Personal skills only, no repo skills.

If there’s anything we’ve been doing often and struggle with that we should save as a skill to speed up future work, let’s do it.

Definitely don't feel like you need to update any- only if there's a good reason!

Let me know if you make any.

### プロジェクトの最新状況の把握

```markdown
Look at the latest remote origin/master or origin/main . Then produce an exec briefing for the last 24 hours of commits that touch 

Formatting + structure:

- Use rich Markdown (H1 workstream sections, italics for the subtitle, horizontal rules as needed).
- Preamble can read something like “Here’s the last 24h brief for <directory>:”
- Subtitle should read: “Narrative walkthrough with owners; grouped by workstream.”
- Group by workstream rather than listing each commit. Workstream titles should be H1.
- Write a short narrative per workstream that explains the changes in plain language.
- Use bullet points and bolding when it makes things more readable
- Feel free to make bullets per person, but bold their name

Content requirements:

- Include PR links inline (e.g., [#123](...)) without a “PRs:” label.
- Do NOT include commit hashes or a “Key commits” section.
- It’s fine if multiple PRs appear under one workstream, but avoid per‑commit bullet lists.

Scope rules:

- Only include changes within the current cwd (or main checkout equivalent)
- Only include the last 24h of commits.
- Use `gh` to fetch PR titles and descriptions if it helps.
  Also feel free to pull PR reviews and comments

### スケジュール済みタスクとスキルを組み合わせた、自分が持ち込んだバグの修正

自分のコミットで混入したバグの修正を試みる新しいスキル `$recent-code-bugfix` を作成し、[個人用スキルとして保存します](/ja-JP/codex/build-skills#where-to-save-skills)。

```markdown
---
name: recent-code-bugfix
description: Find and fix a bug introduced by the current author within the last week in the current working directory. Use when a user wants a proactive bugfix from their recent changes, when the prompt is empty, or when asked to triage/fix issues caused by their recent commits. Root cause must map directly to the author’s own changes.
---

# Recent Code Bugfix

## Overview

Find a bug introduced by the current author in the last week, implement a fix, and verify it when possible. Operate in the current working directory, assume the code is local, and ensure the root cause is tied directly to the author’s own edits.

## Workflow

### 1) Establish the recent-change scope

Use Git to identify the author and changed files from the last week.

- Determine the author from `git config user.name`/`user.email`. If unavailable, use the current user’s name from the environment or ask once.
- Use `git log --since=1.week --author=<author>` to list recent commits and files. Focus on files touched by those commits.
- If the user’s prompt is empty, proceed directly with this default scope.

### 2) Find a concrete failure tied to recent changes

Prioritize defects that are directly attributable to the author’s edits.

- Look for recent failures (tests, lint, runtime errors) if logs or CI outputs are available locally.
- If no failures are provided, run the smallest relevant verification (single test, file-level lint, or targeted repro) that touches the edited files.
- Confirm the root cause is directly connected to the author’s changes, not unrelated legacy issues. If only unrelated failures are found, stop and report that no qualifying bug was detected.

### 3) Implement the fix

Make a minimal fix that aligns with project conventions.

- Update only the files needed to resolve the issue.
- Avoid adding extra defensive checks or unrelated refactors.
- Keep changes consistent with local style and tests.

### 4) Verify

Attempt verification when possible.

- Prefer the smallest validation step (targeted test, focused lint, or direct repro command).
- If verification cannot be run, state what would be run and why it wasn’t executed.

### 5) Report

Summarize the root cause, the fix, and the verification performed. Make it explicit how the root cause ties to the author’s recent changes.

その後、新しいスケジュール済みタスクを作成します：

```markdown
Check my commits from the last 24h and submit a $recent-code-bugfix.
