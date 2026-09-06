<!-- source: https://learn.chatgpt.com/ja-JP/use-cases/build-an-ai-tour-guide -->

## はじめに

操作する場所や選択する項目を案内してもらうと、覚えやすくなるワークフローもあります。Codex を使って、ユーザーが自分で操作を進められるよう、ウェブアプリ内で案内するツアーを作成します。

アプリのコントロール、状態、ドキュメントを扱う WebMCP ツールにより、Codex はユーザーに見えている画面に基づいて次の案内を選べます。サービスにまだ接続していないユーザーと、すでにセットアップを終えたユーザーでは、最初に必要な手順が異なります。

## 使い方

1. アプリのリポジトリを Codex で開き、サービスへの接続やフォルダーの追加など、案内するワークフローを 1 つ選びます。
2. 関連ドキュメントを提供し、ツアーで対応すべき開始時の状態を説明します。
3. このページの開始用プロンプトを実行して、ツアーの対象要素、UI の状態を扱うツール、アプリの指示へのアクセス手段を追加します。
4. Codex がアプリの WebMCP ツールを呼び出せるブラウザ環境でフローをテストします。Codex に案内を依頼し、各ステップを自分で完了します。

最初のツアーは対象を絞ります。ワークフローを増やす前に、セットアップから完了までユーザーを案内できることを確認します。

## 例：Runme での Google Drive フォルダーの追加

<a href="https://web.runme.dev" target="_blank" rel="noopener noreferrer">Runme</a> では、ユーザーはノートブックを編集し、ファイルエクスプローラーを使って Google Drive のフォルダーを追加したり、ファイル間を移動したりします。ツアーは、新しいユーザーがこれらのコントロールを見つけ、一連の操作を学べるように支援します。

Runme について詳しくは、<a href="https://developers.openai.com/blog/automating-repetitive-work-at-openai-with-codex" target="_blank" rel="noopener noreferrer">Codex による OpenAI の反復作業の自動化</a>をご覧ください。

Codex が Runme のコントロールをハイライトし、その用途を説明する様子をご覧ください。以下のスクリーンショットは、それとは別の、Google Drive フォルダーの追加に絞ったツアーを示しています。

<figure class="not-prose my-4">
  <video
    class="w-full rounded-lg border border-default"
    controls
    muted
    playsinline
    preload="metadata"
    poster="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/tour-demo-poster.webp"
    aria-label="Codex demonstrates an AI tour of Runme's controls"
  >
    <source
      src="https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/runme-ai-tour-demo.webm"
      type="video/webm"
    />
    お使いのブラウザは動画タグに対応していません。
  </video>
</figure>

Google Drive のツアーは、次のリクエストから始まります。

### Google Drive への接続

Codex は Google Drive が接続されているかを確認します。接続されていない場合は「 **Google Drive に接続** 」をハイライトし、それを選択して接続を完了するようユーザーに案内します。

![Codex が Runme の「Google Drive に接続」をハイライトし、始め方を説明しています。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/connect-google-drive.webp)

### ファイルエクスプローラーの表示

接続が完了すると、Codex はユーザーをファイルエクスプローラーに案内します。次の案内は、更新されたアプリの状態に応じて決まります。

![Codex が Runme のファイルエクスプローラーを開くコントロールをハイライトしています。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/open-file-explorer.webp)

### フォルダーの追加

ユーザーがツールバーを展開すると、Codex は Google Drive のフォルダーを追加するコントロールをハイライトします。ユーザーは自分で操作を進めながら、次回に備えてそのコントロールの場所を覚えられます。

![Codex が Runme で Google Drive のフォルダーを追加するコントロールをハイライトしています。](https://cdn.openai.com/devhub/codex-use-cases/build-an-ai-tour-guide/add-google-drive-folder.webp)

## Codex がユーザーを案内するためのコンテキスト

Runme の実装では、ツアーの対象要素、アプリケーションの状態、ドキュメントという 3 種類のコンテキストを提供しています。以下のツール名は Runme のものです。同じ役割のツールを、自分のアプリに合わせて実装してください。

### コントロールを見つけるための仕組み

ツアーの対象要素には、意味の分かる安定した `data-tour-id` 値を付け、それぞれにラベルと説明を用意します。Runme は、次の 3 つの WebMCP ツールを通じてこれらのコントロールを公開しています。

- `listTargets` は、登録された対象要素、ID、ラベル、説明を一覧で返します。
- `showTourStep({ target, title?, message, placement? })` は、対象要素をハイライトして説明を表示します。
- `dismiss` は、ハイライトを解除します。

これにより、Codex はユーザーに代わって操作を実行することなく、コントロールを特定して説明できます。

### 状態の読み取りとユーザー操作の待機

Runme はツアーに関する状態を React の外部で管理し、コントローラーを通じて公開しています。`getUiSnapshot` ツールは、サインインの状態を含む現在の UI の状態を提供します。`waitForUiChange(...)` を使うと、Codex はユーザーがハイライトされたコントロールを選択するなどの変化を待つことができます。

操作のたびに状態を再度読み取るよう Codex に指示します。ツアーを先に進めるかどうかは、Codex がすでに案内を表示したかではなく、アプリで実際に何が起きたかに基づいて判断する必要があります。

### 指示のアプリへの同梱

Runme は Markdown ドキュメントをアプリに同梱し、次の WebMCP ツールから参照できるようにしています。

- `readInstructionsForAIAgents` は、Codex がアプリとそのツールをどのように使うべきかを説明します。
- `listDocumentation()` は、利用可能なページとその説明を一覧で返します。
- `getDocumentation({ name })` は、選択したページを Markdown 形式で返します。

ツアーの指示とツールはアプリと一緒に配布できるため、ツアー専用の Codex プラグインを別途用意する必要はありません。

## ツアーのレビュー

開始時の状態を変えて、同じリクエストを試します。完了済みのセットアップをスキップすること、ユーザーの操作を待つこと、UI の変化に応じて案内を更新することを確認します。

ステップをキャンセルした場合や、コントロールがまだ表示されていない場合もテストします。Codex は、不足しているものを説明するか、次に実行できるステップを選ぶべきです。ボタンをハイライトしただけで、操作が成功したと報告してはいけません。

認証、権限チェック、ユーザー操作は、既存のアプリのフローで行うようにします。ツアーでは、これらの仕組みを迂回せず、ユーザーがインターフェースを理解できるよう支援します。

## 次に試すプロンプト

最初のフローが動作したら、同じチャットで次のように依頼してみてください。

- 「Google Drive がすでに接続されていて、ファイルエクスプローラーが閉じている状態で、このツアーをテストしてください。」
- 「ユーザーがステップをキャンセルした後、ツアーの続行を求めた場合にも対応できるようにしてください。」
- 「既存のターゲットと状態を扱うツールを再利用して、\[next workflow\] のツアーを追加してください。」
