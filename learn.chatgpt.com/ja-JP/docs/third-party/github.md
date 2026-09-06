<!-- source: https://learn.chatgpt.com/ja-JP/docs/third-party/github -->

Codex コードレビューを使用すると、GitHub の Pull Request に対して、重要な問題に絞った追加レビューを実施できます。Codex は Pull Request の差分を確認し、リポジトリのガイダンスに従って、重大な問題に焦点を当てた標準的な GitHub コードレビューを投稿します。リサーチプレビューとして提供されるセキュリティレビューでは、Pull Request に潜在するセキュリティ上の問題をさらに詳しく調べます。

<br />

## 開始前の準備

以下を確認してください：

- レビュー対象のリポジトリに[Codex Cloud](/ja-JP/codex/cloud) がセットアップされていること
- [Codex のコードレビュー設定](https://chatgpt.com/codex/settings/code-review)へのアクセス権
- Codex にリポジトリ固有のレビューガイダンスを適用する場合に必要な `AGENTS.md` ファイル

## Codex コードレビューのセットアップ

自動レビューを構成するには、接続済みの GitHub リポジトリと、その設定に対する GitHub のプッシュ権限または管理者権限が必要です。

1. [Codex Cloud](/ja-JP/codex/cloud) をセットアップします。
2. [Codex の設定](https://chatgpt.com/codex/settings/code-review)を開きます。
3. リポジトリの **コードレビュー** を有効にします。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## Codex レビューのリクエスト

1. Pull Request のコメントで `@codex review` をメンションします。
2. Codex がリアクション（👀）し、レビューを投稿するまで待ちます。

<div class="not-prose max-w-xl mr-auto">
  
    
      
    
  
</div>
<br />

Codex はチームメイトと同じように、Pull Request にレビューを投稿します。GitHub では P0 と P1 の問題だけを指摘するため、レビューコメントは優先度の高いリスクに集中します。

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>
<br />

## 自動レビューの有効化

すべての Pull Request を Codex に自動レビューさせるには、
**自動レビュー** を [Codex の設定](https://chatgpt.com/codex/settings/code-review)で有効にします。
レビュー対象の新しい PR が作成されるたびに Codex がレビューを投稿するため、
`@codex review` をコメントする必要はありません。

## Codex のレビュー内容のカスタマイズ

Codex はリポジトリ内の `AGENTS.md` ファイルを検索し、該当する
コードレビューのルールに従います。ルールの対象コードに最も近いファイルに `## Code Review Rules` セクションを追加します。
関連するチェックをまとめたほうがわかりやすい場合は、`###` 見出しを
使用します。

たとえば、実験レポートサービスでは、エクスポージャー後の行動によって比較コホートが変更されないようにできます：

```md
## Code Review Rules

### Experiment cohorts

- Do not filter treatment comparisons on post-exposure behavior, including conversion or retention.
  Safe path: build cohorts from assignment or exposure; report conversion as an outcome.

リポジトリ全体のルールはルートの `AGENTS.md` に、サービス固有のルールは
`services/experiment_reporting/AGENTS.md` などの下位ディレクトリにあるファイルに記述します。Codex は、
変更された各ファイルに対応するルートのガイダンスと、より詳細なガイダンスを適用するため、
無関係な変更にサービス固有のコンテキストを含める必要はありません。

まずは、レビュー担当者がよく説明するチェック内容を反映した簡潔なルールを 2～3 個用意します。有用なルール：

- **影響が大きいリポジトリ固有の動作に注目します。** 指摘対象となる
  互換性の制約、データ境界、危険な副作用を記述し、
  それが重要な理由も説明します。
- **安全な方法や例外を明記します。** Codex が実際の問題と想定どおりの動作を
  区別できるよう、十分なコンテキストを示します。
- **ルールの適用範囲を限定し、長期的に有効な内容にします。** 変更される可能性のある関数名ではなく、
  期待する結果を重視し、ガイダンスを対象コードの近くに配置します。
- **機械的なチェックは CI に任せます。** フォーマットやリントなど、
  機械的に判定できるチェックはレビューのルールに含めないでください。

代表的な Pull Request を作成し、`@codex review` でレビューをリクエストします。
得られた指摘とフィードバックに基づいてルールを調整し、ノイズを生むガイダンスは
適用範囲を絞るか削除します。

コードレビューのルールは Codex の指針となるものであり、テスト、ブランチ保護、必要な承認に代わるものではありません。

今回のレビューだけで特定の点に注目させるには、その内容を Pull Request のコメントに追加します：

`@codex review for issues in the database migration`

## セキュリティレビュー

セキュリティレビューは、Pull Request に含まれるセキュリティ上の問題を特に重視したいお客様向けの追加レビューです。Pull Request の差分、補足となるリポジトリのコンテキスト、設定済みの脅威モデルやセキュリティガイダンスを分析し、セキュリティ固有のリスクをコードレビューよりも深く調べます。

コードレビューでも一般的なレビューの一環としてセキュリティ関連の問題を検出できるため、コードレビューとセキュリティレビューの指摘が重複する場合があります。

### セキュリティレビューのセットアップ

詳しいセットアップ手順と構成オプションについては、[セキュリティ
レビュー](/ja-JP/codex/security/security-review)を参照してください。

1. [Codex Cloud](/ja-JP/codex/cloud) をセットアップします。
2. [Codex の設定](https://chatgpt.com/codex/settings/code-review)を開きます。
3. **リポジトリの設定**で、セキュリティレビューの対象となる Pull Request と
   実行タイミングを選択します。コードレビューと同時に実行するには、 **コードレビューが実行されるたび** を
   選択します。

### セキュリティレビューのリクエスト

セキュリティレビューを手動でリクエストするには、Pull Request に次のコメントを追加します：

`@codex security review`

レビューの実行中は Codex がリアクションし、完了するとセキュリティ上の指摘を
Pull Request に直接投稿します。関連する Codex タスクを開き、 **セキュリティ
レポート** タブを選択すると、レポート全体を確認できます。

## レビューの指摘への対応

Codex がレビューを投稿した後、別のコメントを残すことで、同じ Pull Request 内の問題の修正を依頼できます：

```md
@codex fix the P1 issue

Codex は Pull Request をコンテキストとしてクラウドチャットを開始し、必要な権限がある場合は修正をブランチにプッシュできます。

## Codex へのその他のタスクの依頼

コメントで `@codex` をメンションし、`review` 以外の内容を指定すると、Codex は Pull Request をコンテキストとして[クラウドチャット](/ja-JP/codex/cloud)を開始します。

```md
@codex fix the CI failures

## コードレビューのトラブルシューティング

Codex がリアクションせず、レビューも投稿しない場合：

- 対象リポジトリの **コードレビュー** が [Codex の設定](https://chatgpt.com/codex/settings/code-review)で有効になっていることを確認します。
- Pull Request が、[Codex Cloud](/ja-JP/codex/cloud) をセットアップ済みのリポジトリに属していることを確認します。
- Pull Request のコメントでは、正確なトリガーである `@codex review` を使用してください。
- 自動レビューの場合は、 **自動レビュー** が有効であることと、
  Pull Request のイベントがレビューのトリガー設定と一致していることを確認します。
