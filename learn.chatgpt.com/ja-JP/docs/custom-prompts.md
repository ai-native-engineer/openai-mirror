<!-- source: https://learn.chatgpt.com/ja-JP/docs/custom-prompts -->

カスタムプロンプトは非推奨です。Codex が明示的または暗黙的に呼び出せる再利用可能な
  指示には、[スキル](/ja-JP/codex/build-skills) を使用してください。

カスタムプロンプト（非推奨）では、Markdown ファイルを再利用可能なプロンプトに変換し、Codex CLI と Codex IDE 拡張機能の両方でスラッシュコマンドとして呼び出せます。

カスタムプロンプトは明示的に呼び出す必要があり、ローカルの Codex ホームディレクトリ（例：`~/.codex`）に保存されるため、リポジトリ経由では共有されません。プロンプトを共有したい場合（または Codex が暗黙的に呼び出せるようにしたい場合）は、[スキルを使用してください](/ja-JP/codex/build-skills)。

1. prompts ディレクトリを作成します：

   ```bash
   mkdir -p ~/.codex/prompts

2. 再利用可能な指示を記述した `~/.codex/prompts/draftpr.md` を作成します：

   ```markdown
   ---
   description: Prep a branch, commit, and open a draft PR
   argument-hint: [FILES=<paths>] [PR_TITLE="<title>"]
   ---

   Create a branch named `dev/<feature_name>` for this work.
   If files are specified, stage them first: $FILES.
   Commit the staged changes with a clear message.
   Open a draft PR on the same branch. Use $PR_TITLE when supplied; otherwise write a concise summary yourself.

3. 新しいプロンプトを読み込ませるため、Codex を再起動します（CLI セッションを再起動し、IDE 拡張機能を使用している場合は拡張機能も再読み込みします）。

想定される動作：スラッシュコマンドメニューで `/prompts:draftpr` と入力すると、フロントマターの説明が付いたカスタムコマンドが表示され、ファイルと PR タイトルが省略可能であることを示すヒントも表示されます。

## メタデータと引数の追加

Codex は次回のセッション開始時に、プロンプトのメタデータを読み込み、プレースホルダーを解決します。

- **説明：** ポップアップでコマンド名の下に表示されます。YAML フロントマターで `description:` として設定します。
- **引数のヒント：** 想定されるパラメーターを `argument-hint: KEY=<value>` で記述します。
- **位置指定プレースホルダー：** コマンドの後にスペース区切りで指定した引数に応じて、`$1` から `$9` までが展開されます。`$ARGUMENTS` には、すべての引数が含まれます。
- **名前付きプレースホルダー：** `$FILE` や `$TICKET_ID` のような大文字の名前を使い、値を `KEY=value` の形式で指定します。スペースを含む値は引用符で囲みます（例：`FOCUS="loading state"`）。
- **リテラルのドル記号：** `$$` と記述すると、展開後のプロンプトに単一の `$` が出力されます。

プロンプトファイルを編集した後は、更新内容を反映するために Codex を再起動するか、新しいチャットを開きます。Codex は prompts ディレクトリ内の Markdown 形式ではないファイルを無視します。

## カスタムコマンドの呼び出しと管理

1. Codex CLI または Codex IDE 拡張機能で `/` と入力し、スラッシュコマンドメニューを開きます。
2. `prompts:` またはプロンプト名を入力します（例：`/prompts:draftpr`）。
3. 必要な引数を指定します：

   ```text
   /prompts:draftpr FILES="src/pages/index.astro src/lib/api.ts" PR_TITLE="Add hero animation"

4. Enter キーを押して、展開された指示を送信します（各引数は、不要な場合は省略できます）。

想定される動作：Codex は `draftpr.md` の内容を展開し、プレースホルダーを指定した引数で置き換えてから、その結果をメッセージとして送信します。

`~/.codex/prompts/` 配下のファイルを編集または削除して、プロンプトを管理します。Codex がスキャンするのはそのフォルダー直下の Markdown ファイルのみなので、各カスタムプロンプトはサブディレクトリではなく、`~/.codex/prompts/` 直下に配置してください。
