<!-- source: https://learn.chatgpt.com/ja-JP/docs/cli-customization -->

Codex CLI には、対話型セッションの表示方法や、
コマンドとプロンプトの入力方法を設定するためのターミナル固有のオプションがあります。

## 構文ハイライトとテーマ

ターミナル UI（TUI）では、フェンス付き Markdown コードブロックに加え、
ファイルの差分にも構文ハイライトが適用されます。`/theme` を実行すると、テーマピッカーが開き、テーマをプレビューして、
選択内容を `tui.theme` の設定として `$CODEX_HOME/config.toml` に保存できます。

カスタムテーマを追加するには、`.tmTheme` ファイルを `$CODEX_HOME/themes` に配置してから、
テーマピッカーでそのテーマを選択します。

## シェル補完

Bash、Z shell、Fish、PowerShell のいずれかに対応する補完スクリプトを生成します：

```bash
codex completion zsh

シェルの構成ファイルからスクリプトを読み込みます。Z shell の場合は、次を追加します：

```bash
eval "$(codex completion zsh)"

Z shell で `command not found: compdef` と表示された場合は、補完システムを初期化してから、
Codex の補完を読み込みます：

```bash
autoload -Uz compinit && compinit
eval "$(codex completion zsh)"

シェルを再起動し、`codex` と入力して <kbd>Tab</kbd> キーを押し、補完が動作することを確認します。

## プロンプトエディター

長いプロンプトを入力する場合は、コンポーザーで <kbd>Ctrl</kbd>+<kbd>G</kbd> を押すと、
`VISUAL` で指定されたエディターが開きます。`EDITOR` は、`VISUAL` が設定されていない場合に使用されます。送信前に内容を保存し、
エディターを閉じると、テキストがコンポーザーに戻ります。

対話型セッションでのキーボード操作と、コマンドおよびオプションの全一覧については、以下を参照してください：
[コマンド](/codex/developer-commands?surface=cli#cli-interactive-shortcuts)。
