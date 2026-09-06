<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/github-code-reviews -->

## 使用方法

まず、Codex コードレビューを GitHub の組織またはリポジトリに追加します。
詳しくは [GitHub での Codex コードレビュー](/ja-JP/codex/third-party/github) をご覧ください。

Codex がすべての Pull Request を自動的にレビューするよう設定することも、Pull Request のコメントに `@codex review` と入力してレビューを依頼することもできます。

Codex がリグレッションや潜在的な問題を指摘した場合は、Pull Request に `@codex fix it` のようなフォローアッププロンプトをコメントとして投稿すれば、Codex に修正を依頼できます。

これにより、新しいクラウドチャットが開始され、問題の修正と Pull Request の更新が行われます。

## レビュー指針の定義

Codex のレビュー対象をカスタマイズする場合は `## Code Review Rules` セクションを追加します。追加先は、ルールの適用対象となるコードに最も近い
`AGENTS.md` です。例：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

リポジトリ全体に適用するルールはルートの `AGENTS.md` に、サービス固有のルールは
下位ディレクトリのファイルに記述します。ルールは簡潔にし、指摘対象の挙動に加えて、該当する場合は
安全な代替手段や例外も記述します。フォーマットチェックと lint チェックは CI に任せます。セットアップとルール作成のガイダンスについては
[Codex のレビュー対象のカスタマイズ](/ja-JP/codex/third-party/github#customize-what-codex-reviews)
をご覧ください。
