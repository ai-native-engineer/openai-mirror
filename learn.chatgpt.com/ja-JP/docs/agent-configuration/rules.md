<!-- source: https://learn.chatgpt.com/ja-JP/docs/agent-configuration/rules -->

ルールを使用して、Codex がサンドボックス外で実行できるコマンドを制御します。

ルールは試験的な機能であり、変更される可能性があります。

## ルールファイルの作成

1. `.rules` ファイルを、有効な設定レイヤーの隣にある `rules/` フォルダー内に作成します（例：`~/.codex/rules/default.rules`）。
2. ルールを追加します。この例では、`gh pr view` をサンドボックス外で実行する前に確認を求めます。

   ```python
   # Prompt before running commands with the prefix `gh pr view` outside the sandbox.
   prefix_rule(
       # The prefix to match.
       pattern = ["gh", "pr", "view"],

       # The action to take when Codex requests to run a matching command.
       decision = "prompt",

       # Optional rationale for why this rule exists.
       justification = "Viewing PRs is allowed with approval",

       # `match` and `not_match` are optional "inline unit tests" where you can
       # provide examples of commands that should (or should not) match this rule.
       match = [
           "gh pr view 7888",
           "gh pr view --repo openai/codex",
           "gh pr view 7888 --json title,body,comments",
       ],
       not_match = [
           # Does not match because the `pattern` must be an exact prefix.
           "gh pr --repo openai/codex view 7888",
       ],
   )

3. Codex を再起動します。

Codex は起動時に、すべての有効な設定レイヤー配下の `rules/` をスキャンします。対象には、[チーム設定](/ja-JP/codex/enterprise/admin-setup#step-4-standardize-local-configuration-with-team-config) の配置先と `~/.codex/rules/` のユーザーレイヤーも含まれます。`<repo>/.codex/rules/` にあるプロジェクトローカルのルールは、プロジェクトの `.codex/` レイヤーが信頼されている場合にのみ読み込まれます。

TUI でコマンドを許可リストに追加すると、Codex はユーザーレイヤーの `~/.codex/rules/default.rules` に書き込みます。これにより、以降の実行では確認を省略できます。

スマート承認が有効な場合（デフォルト）、権限昇格リクエスト時に Codex が
`prefix_rule` を提案することがあります。受け入れる前に、提案されたプレフィックスを
慎重に確認してください。

管理者は、制限的な `prefix_rule` エントリを次のファイルから強制適用することもできます：
[`requirements.toml`](/ja-JP/codex/enterprise/managed-configuration#admin-enforced-requirements-requirementstoml)。

## ルールのフィールド

`prefix_rule()` では次のフィールドを指定できます：

- `pattern` **（必須）**：一致させるコマンドのプレフィックスを定義する、空でないリストです。各要素には次のいずれかを指定します：
  - リテラル文字列（例：`"pr"`）
  - その引数位置でいずれかの候補に一致させるリテラルのユニオン（例：`["view", "list"]`）
- `decision` **（デフォルト：`"allow"`）**：ルールが一致したときに実行する処理です。複数のルールが一致した場合、Codex は最も制限の厳しい判定を適用します（`forbidden` \> `prompt` \> `allow`）。
  - `allow`：確認を求めずに、コマンドをサンドボックス外で実行します。
  - `prompt`：一致する呼び出しごとに確認を求めます。
  - `forbidden`：確認を求めずにリクエストをブロックします。
- `justification` **（任意）**：ルールの理由を示す、人が読める空でない文字列です。Codex はこれを承認プロンプトや拒否メッセージに表示することがあります。`forbidden` を使用する場合は、必要に応じて、推奨する代替手段を理由に含めてください（例：`"Use \`rg\` instead of \`grep\`."\`）。
- `match` と `not_match` **（デフォルト：`[]`）**：ルールを読み込む際に Codex が検証する例です。ルールが有効になる前に、これらを使用して誤りを検出できます。

Codex はコマンドを実行するかどうかを判断する際、そのコマンドの引数リストを `pattern` と比較します。内部では、コマンドを引数のリスト（`execvp(3)` が受け取る形式）として扱います。

## シェルラッパーと複合コマンド

一部のツールでは、複数のシェルコマンドを 1 回の呼び出しにまとめます。例：

```text
["bash", "-lc", "git add . && rm -rf /"]

この種のコマンドでは複数の処理が 1 つの文字列に隠れる可能性があるため、Codex は `bash -lc`、`bash -c`、およびそれらに相当する `zsh` / `sh` を特別に扱います。

### Codex がスクリプトを安全に分割できる場合

シェルスクリプトが、次の要素だけで構成される直列のコマンド列である場合：

- 単純な単語（変数展開や `VAR=...`、`$FOO`、`*` などを含まない）
- 安全な演算子（`&&`、`||`、`;`、`|`）による連結

Codex は tree-sitter を使用してスクリプトを解析し、ルールを適用する前に個々のコマンドへ分割します。

上記のスクリプトは、次の 2 つの別個のコマンドとして扱われます：

- `["git", "add", "."]`
- `["rm", "-rf", "/"]`

その後、Codex は各コマンドをルールに照らして評価し、最も制限の厳しい結果を適用します。

`pattern=["git", "add"]` を許可していても、Codex は `git add . && rm -rf /` を自動的には許可しません。`rm -rf /` の部分が個別に評価され、呼び出し全体の自動許可を妨げるためです。

これにより、安全なコマンドに紛れ込ませて危険なコマンドを実行することを防ぎます。

### Codex がスクリプトを分割しない場合

スクリプトで次のような高度なシェル機能を使用している場合：

- リダイレクト（`>`、`>>`、`<`）
- 置換（`$(...)`、`...`）
- 環境変数（`FOO=bar`）
- ワイルドカードパターン（`*`、`?`）
- 制御フロー（`if`、`for`、代入を伴う `&&` など）

Codex はそのスクリプトの解釈も分割も試みません。

このような場合、呼び出し全体を次のように扱います：

```text
["bash", "-lc", "<full script>"]

ルールは、その **単一の** 呼び出しに適用されます。

この処理により、安全に分割できる場合はコマンド単位の評価による安全性を確保し、できない場合は安全側に倒して処理します。

## ルールファイルのテスト

`codex execpolicy check` を使用して、ルールがコマンドにどのように適用されるかテストします：

```shell
codex execpolicy check --pretty \
  --rules ~/.codex/rules/default.rules \
  -- gh pr view 7888 --json title,body,comments

このコマンドは、最も制限の厳しい判定と、一致したルールを示す JSON を出力します。一致したルールに `justification` の値があれば、それも含まれます。複数のファイルを組み合わせるには `--rules` フラグを複数回指定し、出力を整形するには `--pretty` を追加します。

## ルール言語の理解

`.rules` ファイル形式では `Starlark` を使用します（[言語仕様](https://github.com/bazelbuild/starlark/blob/master/spec.md) を参照）。構文は Python に似ていますが、安全に実行できるよう設計されています。ルールエンジンは、ファイルシステムを操作するなどの副作用を発生させずに実行できます。
