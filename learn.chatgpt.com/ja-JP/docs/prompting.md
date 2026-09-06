<!-- source: https://learn.chatgpt.com/ja-JP/docs/prompting -->

<a id="prompts"></a>

## プロンプトの概要

プロンプトとは、知りたいこと、作りたいもの、変更したいことを ChatGPT に伝える方法です。プロンプトは、質問、指示、目標のいずれでも構いません。技術的な構文や決まった形式は必要ありません。まずは自分の言葉で伝え、応答を確認して、フォローアップメッセージで結果を調整します。

多くの場合、短いプロンプトで十分です。規模の大きなタスクや重要なタスクでは、必要な要素を含めます。

- **目的：** ChatGPT に何をしてほしいですか？
- **コンテキスト：** どのような情報や情報源が役立ちますか？
- **出力：** どのような形式、長さ、詳細度が必要ですか？
- **制約：** 何を変更せずに維持する必要がありますか？
  ChatGPT が避けるべきことや、実行前にあなたに確認すべきことは何ですか？

役立つ要素だけを使ってください。すべての項目を埋めたり、決められた形式に従ったりする必要はありません。

## 求める結果の説明

細かな手順を列挙するのではなく、まず求める結果を伝えます。対象者や形式によって ChatGPT が作成すべき内容が変わる場合は、それらも含めます。

```text
Turn these meeting notes into a short update for the project team.
Put the decisions and next steps first.

このプロンプトは、何を作成し、誰が読むのかを示しています。進め方そのものが重要な場合は、その手順を説明します。それ以外の場合は、ChatGPT が情報を検索、比較し、進め方を調整できる余地を残します。

<a id="context"></a>

## 役立つコンテキストの追加

結果に影響する可能性のある情報を共有します。重要な情報源だけを追加し、それぞれから ChatGPT が何を把握すべきかを説明します。

- ドキュメント、スプレッドシート、プレゼンテーション、PDF ファイルは、
  ChatGPT に要約、比較、変換、または[レビュー用ファイルの作成](/ja-JP/codex/artifacts-viewer)を依頼する場合に添付します。
- タスクに視覚的なコンテキストが必要な場合は、スクリーンショット、図、その他の[画像入力](/ja-JP/codex/image-inputs)を追加します。
  画像だけに頼らず、
  重要な箇所を明示してください。
- 回答に最新情報が必要な場合は、ChatGPT に[ウェブ検索](/ja-JP/codex/web-search)を使うよう依頼します。
  結果を確認する必要がある場合は、情報源の提示も求めます。
- [プロジェクト](/ja-JP/codex/projects)を使うと、
  関連するチャット間でファイルや情報源、ローカルフォルダーを共有できます。

### 接続済みソースの利用

ChatGPT が接続済みソースにアクセスできる場合は、どこを検索し、何を見つけるべきかを伝えます。実行する検索を一つひとつ指定する必要はありません。

```text
Use the latest project plan in Drive and relevant decisions and updates from
the project's Slack channel to prepare a status update.

接続済みソースを使用するには、対応するプラグインが必要です。利用できるかどうかは、プランやワークスペースの設定によって異なる場合があります。

### プラグインの利用

プラグインは ChatGPT と Codex に、再利用可能な指示と、
Google Drive、Gmail、Slack、GitHub などのツールへの接続を提供します。どちらの製品も、
共通のディレクトリから公開プラグインを取得します。必要な結果を伝えれば、
利用中の環境で使えるツールの中から適切なものが選択されます。ChatGPT で特定のプラグインを選ぶには、コンポーザーに `@`
と入力します。

  
    <span slot="icon">
      
    </span>
    ChatGPT と Codex でプラグインを検索、インストールして利用します。
  

### ChatGPT のパーソナライズ

複数のチャットに共通して適用したい設定は、 **設定 \> パーソナライズ**
でカスタム指示として登録します。現在のチャットだけに必要な詳細は、
プロンプトに含めます。

  
    <span slot="icon">
      
    </span>
    デフォルトのパーソナリティ、カスタム指示、その他のアプリ設定を指定します。
  

## 問題を未然に防ぐ制約の設定

制約とは、ChatGPT が余計な作業を増やしたり、意図しない操作を行ったりしないために必要な、最小限の指示です。誤った箇所を変更すると結果が使えなくなる場合や、他の人に影響が及ぶ前に内容を確認したい場合は、制約を追加します。

- 承認済みの日付と予算額を変更しないでください。
- 提供された情報源のみを使用してください。不足している情報は推測せず、その旨を明記してください。
- 提案は指定された予算内に収めてください。
- メッセージは下書きとして作成してください。送信しないでください。

特に重要な制約を一つか二つに絞ります。ChatGPT が行うすべての手順を管理する必要はありません。

## そのまま使える形への仕上げ

結果の使い道を ChatGPT に伝えます。そうすることで、用途に合った長さ、詳細度、構成を選べるようになります。

- ディレクターが会議前にざっと目を通せる 1 ページの要約にしてください。決定事項と次のステップを最初に記載してください。
- このメモを、決定事項、担当者、期限を記載したフォローアップメールにまとめてください。
- 支出の予定額と実績額を比較する見やすい表を作成し、10% を超える差異を強調してください。

重要な作業では、すべてのアクション項目に担当者と期限が設定されているかを確認したり、検証できなかった情報を明示したりするよう ChatGPT に最終チェックを依頼します。使用または共有する前に、結果を自分でも確認してください。

## フォローアップメッセージによる結果の改善

最初のプロンプトを完璧にする必要はありません。結果を確認したうえで、希望する変更を具体的に依頼します。

```text
Make the opening more direct, keep the evidence, and move the recommendation
above the background section.

最初からやり直さなくても、不足している情報源を追加したり、方向性を修正したり、別の案を求めたり、詳細度を変えたりできます。

### 方向修正とキューへの追加

Codex の作業中でも、現在の実行が終わるのを待たずに別のメッセージを送信できます。

- **方向修正** では、現在の実行にメッセージを追加します。
  方向性を変えたり、不足している詳細を補ったり、新しい情報を共有したりする場合に使用します。
- **キュー** では、メッセージを次回の実行用に保存します。
  現在の作業が終わってから行うべきフォローアップに使用します。

ChatGPT デスクトップアプリでは、
[**設定 \> 一般 \> フォローアップの動作**](/ja-JP/codex/app/settings#general)からデフォルトの動作を選択します。
キューに登録したメッセージはコンポーザーの上に表示され、編集、並べ替え、送信、
削除が可能です。この設定画面には、デフォルトを変更せず、1 件のメッセージだけ
もう一方の動作を適用するためのショートカットも表示されます。

Codex CLI では、Codex の作業中に <kbd>Enter</kbd> を押すと、現在のターンの方向を修正できます。
<kbd>Tab</kbd> を押すと、メッセージが次のターンのキューに登録されます。詳しくは、
[対話型ショートカット](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)
を参照してください。

## 各要素の組み合わせ

接続済みソースを使ったプロジェクトの進捗報告では、必要な要素を盛り込んだプロンプトは次のようになります。

```text
Prepare a one-page project status update for Monday's leadership meeting. Use
the latest project plan in Drive and relevant decisions and updates from the
project's Slack channel.

Lead with the decisions leadership needs to make and the next steps. Summarize
progress, risks, owners, and due dates. Keep approved dates and budget figures
unchanged. Flag any conflicting or missing information, and don't send or
publish anything.

Before you finish, check that every next step has an owner and due date.

このプロンプトでは、 **目的**、 **コンテキスト**、 **出力**、 **制約**をすべて示し、
細かな手順を列挙せずに最終チェックを依頼しています。

## 音声入力の利用

ChatGPT デスクトップアプリでは、コンポーザーが表示されている状態で <kbd>Ctrl+Shift+D</kbd> を押し、
話し始めます。ChatGPT が話した内容をコンポーザーに文字起こしするため、
プロンプトを送信する前に確認、編集できます。

  
    
  

<a id="threads"></a>
<a id="chats"></a>

## チャット向けのプロンプト例

質問、アイデア出し、下書きの作成、日常的な判断にはチャットを使います。まず求める結果を伝え、回答に影響する場合にだけ詳細を追加します。

### トピックの理解

```text
Explain how compound interest works for someone who has never invested.
Use one concrete example and define any financial terms you introduce.

### 文章の作成と推敲

```text
Draft a friendly email declining this invitation because I will be traveling.
Keep it under 120 words and leave the door open for a future event.

### 選択肢の比較

```text
Compare these two phone plans for one person who travels internationally twice
a year. Show the important differences in a table, then recommend one and explain
the tradeoff.

### 実践的な計画の作成

```text
Plan five weekday dinners that take less than 30 minutes. Avoid peanuts, reuse
ingredients across meals, and finish with one consolidated shopping list.

<a id="prompting-for-work"></a>
<a id="prompting-in-work-mode"></a>

## ChatGPT Work のプロンプト

簡単な質問、短い文章の書き直し、ブレインストーミング、簡単な下書きにはチャットを使用します。さまざまな情報源やツールを利用するタスク、複数の手順を伴うタスク、変更を加えるタスク、まとまった成果物を作成するタスクには ChatGPT Work を使用します。

ChatGPT Work では、必要な成果を説明し、資料を提供して、対象読者を指定し、作業のレビュー方法を伝えます。ChatGPT には計画を立て、必要な情報を収集し、ファイルを作成して、完了前にその内容を確認するよう依頼します。

<a id="use-work-efficiently"></a>
<a id="use-work-mode-efficiently"></a>

### ChatGPT Work の効率的な使い方

ChatGPT Work は、時間のかかるタスクや繰り返し行うタスク、完成後も再利用できるファイルの作成に役立ちます。クレジットを多く消費するタスクでも、時間の節約、品質の向上、重要な意思決定につながるのであれば、実行する価値があります。

まずは、レビューできる成果を 1 つに絞ります：

- 関連する情報源だけを含め、必要に応じて対象期間を限定します。
- 対象読者、出力形式、希望する長さを指定します。
- 必須の作業と、任意の改善や仕上げを分けます。
- 進め方が重要な場合は、計画を立てるよう依頼します。ほかの人が頼りにしている情報を ChatGPT が送信、公開、変更する前に、必ず自分の承認を求めるよう指定します。
- 必要なくなった作業が始まった場合は、タスクの範囲を絞るか、タスクを停止します。

最初の成果をレビューし、指示を調整して、うまくいった場合はそのワークフローを再利用します。

### 資料から完成版ファイルを作成

```text
Use the attached quarterly reports to create a leadership brief and a six-slide
presentation.

The audience is the executive team. Lead with the three decisions they need to
make, distinguish reported facts from your analysis, cite each number to its
source file, and check that the brief and slides agree before you finish.

### 意思決定のための調査

```text
Research three customer-support platforms for a 50-person company. Compare
pricing, security, integrations, and migration effort using current sources.
Deliver a recommendation memo with links, assumptions, and the questions we
should answer before signing a contract.

### ローンチの進行管理

```text
Create a launch plan for the attached product brief. Include the timeline,
owners, dependencies, risks, announcement draft, customer FAQ, and a checklist
for launch day. Flag any missing decisions before producing the final files.

定期的な作業では、まず通常のチャットでプロンプトを調整します。
出力の信頼性を確認できたら、[そのチャット内でタスクをスケジュールします](/ja-JP/codex/automations#schedule-a-task-inside-a-chat)。
スケジュール実行のたびに新しいチャットを開始する場合は、
代わりに独立したスケジュール済みタスクを作成します。

<a id="use-editor-context"></a>

## Codex へのプロンプト

ChatGPT にコード、コードベース、開発ツールを扱わせたい場合は、Codex を使用します。効果的な Codex のプロンプトでは、求める動作を明示し、関連するコードや再現手順を示し、重要な制約を守るよう指定したうえで、変更の検証方法を伝えます。

<a id="goal-mode"></a>

複数の手順を伴うタスクで、編集前に Codex に調査と進め方の提案を依頼する場合は、アプリのコンポーザーに `/plan` を入力します。
[Goal モード](/ja-JP/codex/long-running-work)を利用できる場合は、
計画の作成後に `/goal` を使って継続的な目標を設定します。[アプリの
スラッシュコマンド](/codex/reference/slash-commands)を参照すると、
現在のコマンド一覧を確認できます。

### 以下の例の見方

各ワークフローには、次の内容が含まれます：

- **使用する場面** と、最適な Codex の利用形態（IDE、CLI、クラウド）
- **手順** （ユーザープロンプトの例を含む）
- **コンテキストに関する注記**：Codex が自動的に参照できるものと、ユーザーが添付する必要があるもの
- **検証**：出力の確認方法

> **注：** IDE 拡張機能では、開いているファイルが自動的にコンテキストとして含まれます。CLI では、パスを明示するか、`/mention` と `@` のパス自動補完を使ってファイルを添付します。

Codex は、ファイルとネットワークへのアクセスを制限する[サンドボックス](/ja-JP/codex/sandboxing)内でローカルコマンドを実行します。
タスクでその境界を越える必要がある場合は、
ユーザーの承認ポリシーに従ってから処理を続行します。

### コードベースの説明

オンボーディング時、サービスの引き継ぎ時、またはプロトコル、データモデル、リクエストフローを理解したい場合に使用します。

#### IDE 拡張機能のワークフロー（ローカル調査を最速で進める方法）

1. 関連性が最も高いファイルを開きます。
2. 確認したいコードを選択します（任意ですが推奨）。
3. Codex にプロンプトを入力します：

   ```text
   Explain how the request flows through the selected code.

   Include:
   - a short summary of the responsibilities of each module involved
   - what data is validated and where
   - one or two "gotchas" to watch for when changing this

検証：

- 検証できる図やチェックリストの作成を依頼します：

```text
Summarize the request flow as a numbered list of steps. Then list the files involved.

#### CLI ワークフロー（対話の記録とシェルコマンドが必要な場合）

1. 対話型セッションを開始します：

   ```bash
   codex

2. ファイルを添付し（任意）、プロンプトを入力します：

   ```text
   I need to understand the protocol used by this service. Read @foo.ts @schema.ts and explain the schema and request/response flow. Focus on required vs optional fields and backward compatibility rules.

コンテキストに関する注記：

- コンポーザーで `@` を使うとワークスペース内のファイルパスを挿入でき、`/mention` を使うと特定のファイルを添付できます。

### バグの修正

ローカルで再現できる不具合がある場合に使用します。

#### CLI ワークフロー（再現と検証をすばやく繰り返す方法）

1. リポジトリのルートで Codex を起動します：

   ```bash
   codex

2. 再現手順と、原因として疑わしいファイルを Codex に伝えます：

   ```text
   Bug: Clicking "Save" on the settings screen sometimes shows "Saved" but doesn't persist the change.

   Repro:
   1) Start the app: npm run dev
   2) Go to /settings
   3) Toggle "Enable alerts"
   4) Click Save
   5) Refresh the page: the toggle resets

   Constraints:
   - Do not change the API shape.
   - Keep the fix minimal and add a regression test if feasible.

   Start by reproducing the bug locally, then propose a patch and run checks.

コンテキストに関する注記：

- ユーザーが提供するもの：再現手順と制約（概要説明よりも重要）
- Codex が提供するもの：コマンド出力、見つかった呼び出し箇所、実行中に発生したスタックトレース

検証：

- 修正後、Codex は再現手順をもう一度実行する必要があります。
- 標準のチェック用パイプラインがある場合は、その実行を Codex に依頼します：

```text
After the fix, run lint + the smallest relevant test suite. Report the commands and results.

#### IDE 拡張機能のワークフロー

1. バグがあると思われるファイルと、その直近の呼び出し元を開きます。
2. Codex にプロンプトを入力します：

   ```text
   Find the bug causing "Saved" to show without persisting changes. After proposing the fix, tell me how to verify it in the UI.

### テストの作成

テスト対象の範囲を正確に指定したい場合に使用します。

#### IDE 拡張機能のワークフロー（選択範囲を使用）

1. 対象の関数を含むファイルを開きます。
2. 関数を定義している行を選択します。コマンドパレットから「Add to Codex Thread」を選び、選択した行をコンテキストに追加します。
3. Codex にプロンプトを入力します：

   ```text
   Write a unit test for this function. Follow conventions used in other tests.

コンテキストに関する注記：

- 「Add to Codex Thread」コマンドが提供するもの：選択した行（「行番号」の範囲）と、開いているファイル

#### CLI ワークフロー（プロンプトでパスと行範囲を指定）

1. Codex を起動します：

   ```bash
   codex

2. 関数名を指定してプロンプトを入力します：

   ```text
   Add a test for the invert_list function in @transform.ts. Cover the happy path plus edge cases.

### スクリーンショットを基にしたプロトタイプ作成

デザインモック、スクリーンショット、UI の参考資料から、動作するプロトタイプを作成したい場合に使用します。

#### CLI ワークフロー（画像とプロンプト）

1. スクリーンショットをローカルに保存します（例：`./specs/ui.png`）。
2. Codex を実行します：

   ```bash
   codex

3. 画像ファイルをターミナルにドラッグして、プロンプトに添付します。

4. 続けて、制約と構成を指定します：

   ```text
   Create a new dashboard based on this image.

   Constraints:
   - Use react, vite, and tailwind. Write the code in typescript.
   - Match spacing, typography, and layout as closely as possible.

   Outputs:
   - A new route/page that renders the UI
   - Any small components needed
   - README.md with instructions to run it locally

コンテキストに関する注記：

- 画像から視覚的な要件は伝わりますが、実装上の制約（フレームワーク、ルーティング、コンポーネントのスタイル）は別途指定する必要があります。
- 画像に示されていない動作（ホバー状態、検証ルール、キーボード操作など）は、テキストで指定します。

検証：

- Codex に、許可されている場合は開発サーバーを起動し、確認すべき場所を具体的に示すよう依頼します：

```text
Start the dev server and tell me the local URL/route to view the prototype.

#### IDE 拡張機能のワークフロー（画像と既存ファイル）

1. Codex のチャットに画像を添付します（ドラッグ＆ドロップまたは貼り付け）。
2. Codex にプロンプトを入力します：

   ```text
   Create a new settings page. Use the attached screenshot as the target UI.
   Follow design and visual patterns from other files in this project.

### ライブ更新を使った UI の反復改善

Codex がコードを編集する間に、「デザイン → 調整 → 再読み込み → 調整」を短いサイクルで繰り返したい場合に使用します。

#### CLI ワークフロー（Vite 実行後の短いプロンプトによる反復）

1. Codex を起動します：

   ```bash
   codex

2. 別のターミナルウィンドウで開発サーバーを起動します：

   ```bash
   npm run dev

3. Codex に変更を指示します：

   ```text
   Propose 2-3 styling improvements for the landing page.

4. 方向性を一つ選び、短く具体的なプロンプトで調整を繰り返します：

   ```text
   Go with option 2.

   Change only the header:
   - make the typography more editorial
   - increase whitespace
   - ensure it still looks good on mobile

5. 対象を絞った依頼を繰り返します：

   ```text
   Next iteration: reduce visual noise.
   Keep the layout, but simplify colors and remove any redundant borders.

検証：

- Codex がコードを更新するたびに、ブラウザで変更を確認します。
- 採用する変更はコミットし、採用しない変更は元に戻します。
- 編集内容を元に戻したり変更したりした場合は、その旨を Codex に伝え、次のプロンプトに取り組む際に変更内容が上書きされないようにします。

### リファクタリングをクラウドに委任

ローカルのコンテキストを基にアプローチを設計し、時間のかかる実装を並行して実行できるクラウドのチャットに委任したい場合に使用します。

#### ローカルでの計画（IDE）

1. 変更を明確に比較できるよう、現在の作業内容をコミットするか、少なくともスタッシュしておきます。
2. Codex にリファクタリング計画の作成を依頼します。`$plan` スキルを利用できる場合は、明示的に呼び出します：

   ```text
   $plan

   We need to refactor the auth subsystem to:
   - split responsibilities (token parsing vs session loading vs permissions)
   - reduce circular imports
   - improve testability

   Constraints:
   - No user-visible behavior changes
   - Keep public APIs stable
   - Include a step-by-step migration plan

3. 計画をレビューし、変更点をすり合わせます：

   ```text
   Revise the plan to:
   - specify exactly which files move in each milestone
   - include a rollback strategy

コンテキストに関する注記：

- 計画の策定は、Codex が現在のコード（エントリーポイント、モジュール境界、依存関係グラフの手がかりなど）をローカルでスキャンできる場合に最も効果的です。

#### クラウドへの委任（IDE → クラウド）

1. まだ設定していない場合は、[Codex のクラウド環境](/ja-JP/codex/environments/cloud-environment)を設定します。
2. プロンプトコンポーザーの下にあるクラウドアイコンをクリックし、クラウド環境を選択します。
3. 次のプロンプトを入力すると、Codex は既存のチャットのコンテキスト（計画やローカルで行ったソースコードの変更を含む）を引き継ぎ、クラウドに新しいチャットを作成します。

   ```text
   Implement Milestone 1 from the plan.

4. クラウド上の差分をレビューし、必要に応じて調整を繰り返します。

5. クラウドから直接 PR を作成するか、変更をローカルに取り込んでテストし、仕上げます。

6. 計画に含まれるほかのマイルストーンについても、同じ手順を繰り返します。

クラウドに委任されたタスクは、分離された環境で実行されます。
インターネットアクセスは、その環境で有効にしない限り、エージェントフェーズ中は無効です。
詳しくは、[クラウドでのインターネットアクセス](/ja-JP/codex/cloud/internet-access)をご覧ください。

### ローカルでのコードレビュー

コミットまたは PR の作成前に、別の視点から確認してもらいたい場合に使用します。

#### CLI ワークフロー（作業ツリーのレビュー）

1. Codex を起動します：

   ```bash
   codex

2. レビューコマンドを実行します：

   ```text
   /review

3. 任意：重点的に確認してほしい内容を指定します：

   ```text
   /review Focus on edge cases and security issues

検証：

- レビューのフィードバックに基づいて修正を適用し、`/review` を再実行して、問題が解決したことを確認します。

### GitHub 上の Pull Request のレビュー

ブランチをローカルにプルせずに、レビューのフィードバックを得たい場合に使用します。

この機能を使用する前に、リポジトリで Codex の **コードレビュー** を有効にします。詳しくは、[コードレビュー](/ja-JP/codex/third-party/github)をご覧ください。

#### GitHub ワークフロー（コメントベース）

1. GitHub で Pull Request を開きます。
2. レビューで重点的に確認してほしい領域を明示し、Codex をタグ付けしたコメントを残します：

   ```text
   @codex review

3. 任意：より具体的な指示を入力します。

   ```text
   @codex review for security vulnerabilities and security concerns

### ドキュメントの更新

ドキュメントを正確かつ分かりやすく更新する必要がある場合に使用します。

#### IDE または CLI のワークフロー（ローカルでの編集と検証）

1. 変更対象のドキュメントファイルを特定し、IDE で開くか、IDE または CLI で `@` を使ってメンションします。
2. 対象範囲と検証要件を指定して、Codex に指示します：

   ```text
   Update the "advanced features" documentation to provide authentication troubleshooting guidance. Verify that all links are valid.

3. Codex が変更案を作成したら、ドキュメントをレビューし、必要に応じて修正を重ねます。

検証：

- レンダリングされたページを読みます。
