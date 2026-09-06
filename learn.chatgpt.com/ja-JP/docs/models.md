<!-- source: https://learn.chatgpt.com/ja-JP/docs/models -->

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## モデルの選択

ChatGPT デスクトップアプリでは、コンポーザーの下にあるモデルと推論の設定で、利用可能なモデルを選択し、推論強度を調整します。

推論強度を上げると、複雑なタスクでよりよい結果が得られる可能性がありますが、処理に時間がかかり、使用するトークンも増えます。まずはデフォルトの推論強度を使い、より綿密な計画や分析が必要なタスクでは強度を上げてください。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> モードは、単一のエージェントでの実行にとどまりません。
複雑な作業を高速化するために
[サブエージェント](/codex/agent-configuration/subagents)を使用します。
そのため、サブエージェントに分担できる大規模なタスクに適しています。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## モデルの選択

これらの推奨事項は、Web 版の **ChatGPT Work** に適用されます。
コンポーザーの下にあるモデルと推論の設定で、利用可能なモデルを選択し、
推論強度を調整します。

推論強度を上げると、複雑なタスクでよりよい結果が得られる可能性がありますが、処理に時間がかかり、使用するトークンも増えます。まずはデフォルトの推論強度を使い、より綿密な計画や分析が必要なタスクでは強度を上げてください。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> モードは、単一のエージェントでの実行にとどまりません。
複雑な作業を高速化するために
[サブエージェント](/codex/agent-configuration/subagents)を使用します。
そのため、サブエージェントに分担できる大規模なタスクに適しています。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_minmax(22rem,25rem)] lg:items-start">
  <div class="min-w-0">

## モデルの選択

対話型の CLI セッションでは、`/model` でモデルの切り替えや
推論強度の調整ができます。次のように、Codex の起動時に
`--model` またはそのエイリアス `-m` を指定してモデルを選択することもできます。

非対話型の実行でも、次のように同じオプションを使用できます。

推論強度を高くすると、複雑なタスクでより良い結果を得られる可能性がありますが、時間がかかり、トークンの使用量も増えます。まずはデフォルトの推論強度で始め、より綿密な計画や分析が必要な場合に強度を上げてください。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> モードでは、単一のエージェントだけで実行するのではなく、
複雑な作業を速く進めるために
[サブエージェント](/codex/agent-configuration/subagents)を使います。
複数のサブエージェントに分担できる大規模なタスクに適しています。

  </div>
  
</div>

<div class="grid gap-5 lg:grid-cols-[minmax(0,1fr)_14rem] lg:items-start">
  <div class="min-w-0">

## モデルの選択

コンポーザーの下にあるモデル切り替えメニューを使って、利用可能なモデルと推論強度を選択します。

推論強度を高くすると、複雑なタスクでより良い結果を得られる可能性がありますが、時間がかかり、トークンの使用量も増えます。まずはデフォルトの推論強度で始め、より綿密な計画や分析が必要な場合に強度を上げてください。

<strong className="text-[#8756e8] dark:text-[#bda4ff]">Ultra</strong> モードでは、単一のエージェントだけで実行するのではなく、
複雑な作業を速く進めるために
[サブエージェント](/codex/agent-configuration/subagents)を使います。
複数のサブエージェントに分担できる大規模なタスクに適しています。

  </div>
  
</div>

<a id="recommended-models"></a>
<a id="other-models"></a>
<a id="deprecated-codex-models"></a>
<a id="configure-your-default-local-model"></a>
<a id="choose-a-model-for-cloud-tasks"></a>
<a id="gpt-6-astra"></a>

## 推奨モデル

<a id="app-compare-models"></a>

<div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
  

  

</div>

利用可否は、提供状況、サインイン方法、使用するクライアントによって異なります。
各プランでの利用条件と使用量については[料金](/ja-JP/codex/pricing)を、
Enterprise での利用については[ワークスペースでのモデルの利用可否](/ja-JP/codex/enterprise/workspace-model-availability#gpt-6-astra-in-enterprise)を参照してください。

  まずは、お使いのアカウントで利用できるパワーのデフォルト設定から始めてください。
より深い推論が必要なら**賢さ重視** へ、より速く低コストで作業するなら **速さ重視** へ調整します。
  `gpt-5.6-luna` を使いたい場合や、モデル、推論強度、速度を個別に指定したい場合は、
   **上級** を開いてください。

選択画面の図は GPT-5.6 の操作項目を示しています。対象となる Pro、Business（$100）、Enterprise アカウントでは、Astra の提供開始に伴い、パワーの選択肢が Terra 軽量、Sol 軽量、Sol 中、Astra 軽量、Astra 中、Astra 極高に更新されます。選択肢はプランや提供段階によって異なる場合があります。

### 実験的なコンテキスト管理

対応する Codex クライアントでは、ChatGPT Plus または Pro でサインインしているユーザーが、実験的なコンテキスト管理を有効にできます。Astra はコンテキストウィンドウをまたいでメモを保持し、同じタスク内の過去のメッセージやツールの結果を検索できます。この実験的機能はデフォルトではオフになっており、提供開始時点では Business、Enterprise、API キーでのサインインでは利用できません。

有効にするには、`config.toml` に `features.context_management.experimental_mode = true` を設定し、
新しいタスクを開始します。設定項目については[構成リファレンス](/ja-JP/codex/config-file/config-reference)を、
ファイルの場所については[構成の基本](/ja-JP/codex/config-file/config-basic)を参照してください。
ワークスペースの要件は引き続き適用されます。

<a id="choosing-sol-terra-and-luna"></a>

## Astra、Sol、Terra、Luna の選び方

複数の手順やツールにわたって最高の性能が必要なタスクには、
 **Astra** を選んでください。 **Sol** は深い検討と丁寧な仕上げを得意とし、 **Terra** は日常的な作業に、
 **Luna** は内容が明確な反復タスクに適しています。

### 各モデルの得意分野

- **Astra は、最も難しい作業を最初から最後まで進めるのに適しています。** 継続的な推論と判断を必要とする、
  コード、アプリ、リサーチにまたがる一連のワークフローには Astra を選んでください。
  役立つ成果を得るための基準となる情報源、テンプレート、制約、確認項目を与えます。
  Astra は、元の目標や制約を見失わずに、
  的を絞った質問をし、ユーザーの指示を取り入れる能力に優れています。
- **Sol は、複雑で自由度の高い作業に適しています。** 曖昧な点が多いタスク、難しいタスク、
  重要度の高いタスクなど、綿密な分析や判断、丁寧な仕上げが必要な作業には Sol を選んでください。
  たとえば、複雑なコード変更、deep research、完成度の高い文書作成などです。
  範囲の狭いタスクでは、完了条件を明確にして、作業の焦点がぶれないようにします。
- **Terra は実用的な万能型です。** Sol ほど深く掘り下げる必要はないものの、
  高い推論能力とツールの活用が求められる日常的な作業には Terra を選んでください。
  これまで GPT-5.5 に任せていた作業なら、まず Terra を試すとよいでしょう。
- **Luna は、内容が明確な反復タスクに適しています。** 求める結果が明確で、具体的なタスクを大量に処理する場合は Luna を選んでください。
  たとえば、抽出、分類、変換、構造化された要約などです。
  

### 推論強度の選択

必要な結果が得られる範囲で、推論強度をできるだけ低く設定します。より綿密な計画、分析、確認が必要なタスクでは、推論強度を上げてください。

- ChatGPT デスクトップアプリ、ウェブ版 ChatGPT Work、IDE 拡張機能の**軽量** 、または CLI の **低** は、
  短時間で取り組める、範囲の明確なタスクに適しています。
- **中** は、より綿密な計画が必要なタスクで、速度と推論の深さのバランスを取ります。
- **高** と **極高** は、複数の手順や情報源、トレードオフが関わる
  難しい作業に適しています。

GPT-5.5 と GPT-5.6 の推論強度には、正確な対応関係はありません。よく知っているタスクを低めの設定で試し、結果に応じて調整してください。

### Max と Ultra の使い分け

**Max** では、選択したモデルが 1 つのタスクについて推論する時間が長くなります。
速度や使用量よりも推論の深さが重要となる、特に難しい問題に使用してください。
選択肢に Max が表示されない場合は、アプリの設定で有効にする必要があります。

**Ultra** は、[サブエージェント](/ja-JP/codex/agent-configuration/subagents)を使って、
複雑なタスクの各部分を並列で処理します。作業を意味のある単位に分割できる場合に選んでください。
ほとんどのタスクでは、Max や Ultra は必要ありません。

デスクトップアプリのモデルスライダーに Ultra が表示されない場合は、
**設定** \> **構成**を開き、 **モデル選択スライダーに Ultra を表示**をオンにします。

## その他のモデル

ChatGPT でサインインする場合、Codex は上記の推奨モデルで最適に動作します。

  <strong>
    GPT-5.4 と GPT-5.4 mini は、2026 年 8 月 31 日に Codex での提供を終了します。
  </strong>{" "}
  ChatGPT でサインインする場合は、保存済みの構成、カスタムエージェント、スケジュール済みタスクで、
`gpt-5.4` を `gpt-5.6-terra` に、`gpt-5.4-mini` を `gpt-5.6-luna` に置き換えてください。
  OpenAI API と、ご自身の API キーで認証した Codex は影響を受けません。
  

  <div class="not-prose grid gap-6 md:grid-cols-2 xl:grid-cols-3">
    

    

    

  </div>

用途に合わせて、[Chat Completions](https://platform.openai.com/docs/api-reference/chat) または [Responses APIs](https://platform.openai.com/docs/api-reference/responses) に対応する任意のモデルやプロバイダーを Codex で使用することもできます。

  Chat Completions API のサポートは非推奨となっており、今後の Codex のリリースで削除されます。

## 非推奨の Codex モデル

ChatGPT でサインインする場合、Codex での `gpt-5.4` と `gpt-5.4-mini` モデルの提供は、
2026 年 8 月 31 日に終了します。ワークスペースのデフォルト設定、保存済みのモデル設定、
管理対象の設定、カスタムエージェント、スケジュール済みタスクで、
`gpt-5.4` を `gpt-5.6-terra` に、`gpt-5.4-mini` を `gpt-5.6-luna` に置き換えてください。

ChatGPT でサインインする場合、Codex では `gpt-5.2` と `gpt-5.3-codex` モデルはすでに非推奨となっています。
これらのモデルを引き続き参照しているスクリプト、設定ファイル、
`codex exec --model` コマンドを更新してください。

OpenAI API と、自分の API キーで認証する Codex は、
GPT-5.4 の提供終了の影響を受けません。現在利用可能な API モデルについては、
[API モデルのページ](/api/docs/models)をご覧ください。

## ローカルで使用するデフォルトモデルの設定

ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能は、同じ[設定ファイル](/ja-JP/codex/config-file/config-basic) `config.toml` を使用します。
モデルを指定するには、設定ファイルに `model` エントリを追加します。
モデルを指定しない場合、
ChatGPT デスクトップアプリ、Codex CLI、IDE 拡張機能は推奨モデルを使用します。

## クラウドチャット用モデルの選択

現在、Codex Cloud のチャットで使用するデフォルトモデルは変更できません。
