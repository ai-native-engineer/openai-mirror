<!-- source: https://learn.chatgpt.com/ja-JP/docs/integrated-terminal -->

ChatGPT デスクトップアプリの各チャットには、現在のプロジェクトまたは
Worktree 専用のターミナルが用意されています。アプリの右上にあるターミナルアイコンから開くか、
<kbd>Ctrl</kbd>+<kbd>\`</kbd> を押します。

  
    
  

## プロジェクトの実行と検証

ターミナルを使用すると、アプリを切り替えることなく、変更を検証し、スクリプトを実行し、Git 操作を行えます。ChatGPT は現在のターミナル出力を読み取れるため、一緒に作業しながら、実行中の開発サーバーを確認したり、失敗したビルドを参照したりできます。

よく使うコマンドの例：

- `git status`
- `git pull --rebase`
- `pnpm test` または `npm test`
- `pnpm run lint` またはプロジェクト固有の別のチェック

## 再利用可能なアクションの作成

定期的に実行するコマンドがある場合は、[ローカル環境](/ja-JP/codex/environments/local-environment#actions)でアクションを定義します。アクションは
ChatGPT
デスクトップアプリでショートカットとして表示され、統合ターミナルで実行されます。

<kbd>Cmd</kbd>+<kbd>K</kbd>
を押すと、アプリのコマンドパレットが開きますが、ターミナルはクリアされません。ターミナルをクリアするには、<kbd>Ctrl</kbd>+<kbd>L</kbd> を押します。
