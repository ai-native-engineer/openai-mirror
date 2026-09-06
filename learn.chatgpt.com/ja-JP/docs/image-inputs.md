<!-- source: https://learn.chatgpt.com/ja-JP/docs/image-inputs -->

タスクに視覚的なコンテキストが必要な場合は、エラー画面の
スクリーンショット、インターフェースデザイン、アーキテクチャ図、既存のアセットなどの画像をプロンプトに追加します。また、
何を確認してほしいか、どのような結果を求めているかを ChatGPT に説明してください。タスクを伝える際は、画像
だけに頼らないでください。

<kbd>Shift</kbd> キーを押しながら画像をプロンプトコンポーザーにドラッグして
コンテキストとして追加します。システム上の画像を確認するよう ChatGPT に依頼したり、
スクリーンショットツールを使って別のアプリでの作業結果を検証したりすることもできます。

ChatGPT の Web コンポーザーに画像を添付するか、貼り付けるか、ドラッグします。プロンプトで、
何を確認してほしいか、その画像からどのような結果を求めているかを ChatGPT に伝えます。

対話型コンポーザーに画像を貼り付けるか、1 つ以上のファイルを
コマンドラインで渡します：

```bash
codex -i screenshot.png "Explain this error and suggest the smallest fix"
codex --image before.png,after.png "Compare these states and list the regressions"

複数の画像を使用する場合は、パスをカンマで区切るか、 `--image` を繰り返し指定します。Codex
では、PNG や JPEG などの一般的な画像形式を使用できます。

<kbd>Shift</kbd> キーを押しながら画像をプロンプトコンポーザーにドラッグすると、
拡張機能がドロップ操作をエディターに渡さず、そのまま受け付けます。

## 画像に合わせたプロンプトの作成

画像が何を示しているかを明記し、重要な箇所を示して、必要な出力
と制約を指定します。複数の画像を添付する場合は、各画像を区別して示し、
ChatGPT にどのように比較してほしいかを説明します。

例：

```text
Compare this checkout screen with the design. Fix spacing and typography only;
do not change behavior. Verify the result with a new screenshot.

## 適切な画像機能の選択

視覚的な参考資料を ChatGPT に確認してほしい場合は、画像入力を使用します。
[画像生成](/ja-JP/codex/image-generation) は、ChatGPT に
画像を作成または編集してほしい場合に使用します。
