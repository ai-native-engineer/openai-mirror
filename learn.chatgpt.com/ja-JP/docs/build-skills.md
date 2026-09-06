<!-- source: https://learn.chatgpt.com/ja-JP/docs/build-skills -->

エージェントスキルを使用して、ChatGPT と Codex にタスク固有の機能を追加できます。
スキルには指示、リソース、必要に応じてスクリプトがまとめられており、
どちらの製品でもワークフローを確実に実行できます。スキルは、
[オープンなエージェントスキル標準](https://agentskills.io)に基づいています。

スキルは、再利用可能なワークフローを記述するための形式です。
プラグインは、ChatGPT と Codex が共有する共通のプラグインディレクトリを通じて、
再利用可能なスキルとコネクタを配布します。プラグインは、Web 版 ChatGPT、デスクトップ版 ChatGPT、
モバイル版 ChatGPT のチャットと Work、ChatGPT デスクトップアプリ内の Codex、
Codex CLI で利用できます。まずスキルでワークフロー自体を設計し、
[プラグイン](https://developers.openai.com/plugins/build/plugins)としてパッケージ化することで、
ほかのユーザーもインストールできるようになります。

スタンドアロンのスキルは、ChatGPT デスクトップアプリ、Codex CLI、
IDE 拡張機能で利用できます。プラグインに組み込まれたスキルは、
Web 版 ChatGPT、デスクトップ版 ChatGPT、モバイル版 ChatGPT のチャットと Work でも利用できます。

ChatGPT デスクトップアプリでは、サイドバーの **スキル** を開くと、
各プロジェクトで作成したスキルを表示して詳しく確認できます。

  
    
  

スキルでは、コンテキストを効率的に管理するために **段階的開示** を採用しています。
ChatGPT と Codex は、最初に各スキルの名前と説明を読み込み、
そのスキルを使用すると判断した時点で、`SKILL.md` の指示全文を読み込みます。

Codex では、最初の一覧に各スキルのファイルパスも含まれます。
プロンプトの残りの部分を圧迫しないよう、この一覧が使用できるのは、
モデルのコンテキストウィンドウの最大 2%、コンテキストウィンドウが不明な場合は 8,000 文字までです。
多数のスキルがインストールされている場合、Codex はまずスキルの説明を短縮します。
スキルセットが大規模な場合は、Codex が最初の一覧から一部のスキルを省略し、警告を表示することがあります。

この上限は、最初のスキル一覧にのみ適用されます。Codex がスキルを選択すると、そのスキルの SKILL.md に記載された指示をすべて読み込みます。

スキルは、`SKILL.md` ファイルと、必要に応じてスクリプトや参考資料を格納したディレクトリです。`SKILL.md` ファイルには `name` と `description` を含める必要があります。

<a id="how-codex-uses-skills"></a>

## ChatGPT と Codex でのスキルの利用方法

ChatGPT と Codex では、次の 2 つの方法でスキルを呼び出せます：

1. **明示的な呼び出し：** プロンプトでスキルを直接指定します。
   ChatGPT では `@` を入力してスキルを選択します。Codex CLI または IDE 拡張機能では、
`/skills` を実行するか `$` を入力して、スキルをメンションします。
2. **暗黙的な呼び出し：** ChatGPT または Codex は、
   タスクがスキルの `description` と一致する場合に、そのスキルを選択できます。

暗黙的な照合は `description` に依存するため、対象範囲と対象外の事項を明確にした、
簡潔な説明を記述してください。説明が短縮されてもホストがスキルを照合できるよう、
主要なユースケースとトリガーワードを冒頭に記載してください。

## スキルの作成

すでにワークフローを把握しており、説明するより実演する方が簡単な場合は、
[記録と再生](/ja-JP/codex/extend/record-and-replay)を使用してください。レコーダーがワークフローを記録し、
手順を確認したうえで、
実演に基づく再利用可能なスキルの草案を作成します。

スキルを言葉で説明して作成する場合は、組み込みの作成ツールを使用してください。
ChatGPT Work では `@skill-creator` を使って呼び出します。Codex では、次のように呼び出します：

```text
$skill-creator

作成ツールは、スキルの機能、トリガーされるタイミング、指示のみにするかスクリプトも含めるかを尋ねます。デフォルトは指示のみです。

`SKILL.md` ファイルを含むフォルダーを作成して、スキルを手動で作成することもできます：

```md
---
name: skill-name
description: Explain exactly when this skill should and should not trigger.
---

Skill instructions for ChatGPT or Codex to follow.

Codex はスキルの変更を自動的に検出します。更新が反映されない場合は、Codex を再起動してください。

<a id="where-to-save-skills"></a>

## Codex がローカルスキルを読み込む場所

Codex は、リポジトリ、ユーザー、管理者、システムの各場所からスキルを読み込みます。リポジトリでは、現在の作業ディレクトリからリポジトリのルートまでのすべてのディレクトリで `.agents/skills` をスキャンします。2 つのスキルの `name` が同じでも、Codex はそれらを統合しません。どちらもスキル選択画面に表示される場合があります。

| スキルのスコープ | 場所                                                                                                  | おすすめの用途                                                                                                                                                                                        |
| :---------- | :-------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `REPO`      | `$CWD/.agents/skills` <br /> 現在の作業ディレクトリ：Codex を起動する場所。                           | リポジトリやコード環境では、チームが特定の作業フォルダーに関連するスキルをチェックインできます。たとえば、特定のマイクロサービスやモジュールだけに関連するスキルです。                              |
| `REPO`      | `$CWD/../.agents/skills` <br /> Git リポジトリ内で Codex を起動したときの、CWD より上位のフォルダー。         | 入れ子のフォルダーを含むリポジトリでは、組織が親フォルダー内の共有領域に関連するスキルをチェックインできます。                                                                       |
| `REPO`      | `$REPO_ROOT/.agents/skills` <br /> Git リポジトリ内で Codex を起動したときの最上位のルートフォルダー。 | 入れ子のフォルダーを含むリポジトリでは、組織がすべてのリポジトリ利用者に関連するスキルをチェックインできます。これらは、リポジトリ内のすべてのサブフォルダーで利用できるルートスキルとして機能します。 |
| `USER`      | `$HOME/.agents/skills` <br /> ユーザーの個人用フォルダーに保存されたすべてのスキル。                         | ユーザーが作業するあらゆるリポジトリで利用できる、そのユーザー向けのスキルを選定する場合に使用します。                                                                                                           |
| `ADMIN`     | `/etc/codex/skills` <br /> マシンまたはコンテナ上の共有システム領域に保存されたすべてのスキル。 | SDK スクリプトや自動化のほか、マシン上の各ユーザーが利用できるデフォルトの管理者スキルをチェックインするために使用します。                                                                                     |
| `SYSTEM`    | OpenAI により Codex に同梱されています。                                                                             | skill-creator や plan といった、幅広いユーザーに役立つスキルです。Codex の起動時に、すべてのユーザーが利用できます。                                                                   |

Codex はシンボリックリンクされたスキルフォルダーに対応しており、これらの場所をスキャンする際はリンク先をたどります。

これらの場所は、スキルの作成とローカルでの検出に使用します。
再利用可能なスキルを単一のリポジトリ外に配布する場合や、
必要に応じてコネクタと一緒にバンドルする場合は、[プラグイン](https://developers.openai.com/plugins/build/plugins)を使用してください。

## プラグインによるスキルの配布

スキルフォルダーを直接使用する方法は、ローカルでの作成やリポジトリ単位のワークフローに最適です。
再利用可能なスキルを配布する場合、2 つ以上のスキルをまとめる場合、
またはスキルをコネクタと一緒に提供する場合は、
[プラグイン](https://developers.openai.com/plugins/build/plugins)としてパッケージ化してください。

プラグインには、1 つ以上のスキルを含めることができます。
また、必要に応じて、登録済みの MCP サーバー接続、同梱する MCP サーバーの構成、
表示用アセットを 1 つのパッケージにまとめることもできます。

## ローカル利用向け厳選スキルのインストール

ローカルの Codex セットアップに、組み込み以外の厳選スキルを追加するには、`$skill-installer` を使用します。たとえば、`$linear` スキルをインストールするには、次のようにします：

```bash
$skill-installer linear

インストーラーに指示して、ほかのリポジトリからスキルをダウンロードすることもできます。
Codex は新しくインストールされたスキルを自動的に検出します。
スキルが表示されない場合は、Codex を再起動してください。

ローカルでのセットアップや実験には、この方法を使用します。
独自のスキルを再利用可能な形で配布する場合は、プラグインを優先してください。

## ローカル Codex スキルの有効化と無効化

`[[skills.config]]` エントリを `~/.codex/config.toml` で設定すると、スキルを削除せずに無効化できます：

```toml
[[skills.config]]
path = "/path/to/skill/SKILL.md"
enabled = false

`~/.codex/config.toml` を変更した後は、Codex を再起動してください。

## オプションのメタデータ

スキルをよりスムーズに利用できるよう、`agents/openai.yaml` を追加して、[ChatGPT デスクトップアプリ](/ja-JP/codex/app)の UI メタデータを構成し、呼び出しポリシーを設定して、ツールの依存関係を宣言します。

```yaml
interface:
  display_name: "Optional user-facing name"
  short_description: "Optional user-facing description"
  icon_small: "./assets/small-logo.svg"
  icon_large: "./assets/large-logo.png"
  brand_color: "#3B82F6"
  default_prompt: "Optional surrounding prompt to use the skill with"

policy:
  allow_implicit_invocation: false

dependencies:
  tools:
    - type: "mcp"
      value: "openaiDeveloperDocs"
      description: "OpenAI Docs MCP server"
      transport: "streamable_http"
      url: "https://developers.openai.com/mcp"

`allow_implicit_invocation`（デフォルト：`true`）：`false` の場合、Codex はユーザーのプロンプトに基づいてスキルを暗黙的に呼び出しません。ただし、`$skill` による明示的な呼び出しは引き続き可能です。

## ベストプラクティス

- 各スキルは 1 つの作業に特化させます。
- 決定論的な動作や外部ツールが必要な場合を除き、スクリプトより指示を優先します。
- 入力と出力を明示し、各手順を命令形で記述します。
- スキルの説明と照らし合わせてプロンプトをテストし、意図したとおりに起動することを確認します。

その他の例については、
[GitHub CI の修復](https://github.com/openai/skills/tree/main/skills/.curated/gh-fix-ci)、
[PDF](https://github.com/openai/skills/tree/main/skills/.curated/pdf)、
[Linear](https://github.com/openai/skills/tree/main/skills/.curated/linear)、
[openai/skills](https://github.com/openai/skills)、および
[エージェントスキル仕様](https://agentskills.io/specification)を参照してください。インストール可能な形で
配布する場合は、[プラグイン](https://developers.openai.com/plugins/build/plugins)を優先してください。
