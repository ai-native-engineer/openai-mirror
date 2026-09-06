<!-- source: https://learn.chatgpt.com/ja-JP/docs/windows/wsl -->

WSL2 を使用すると、Codex は Linux 環境内で実行され、
ネイティブの [Windows サンドボックス](/ja-JP/codex/windows/windows-sandbox) は使用しません。Linux ネイティブの
ツールが必要な場合、リポジトリと開発ワークフローがすでに WSL2 内にある場合、または
Windows ネイティブの 2 種類のサンドボックスモードのどちらもお使いの環境で動作しない場合は、WSL2 を選択してください。

WSL1 は Codex `0.114` までサポートされていました。Codex `0.115` 以降、Linux
サンドボックスは `bubblewrap` に移行したため、WSL1 はサポートされなくなりました。

## WSL 内から VS Code を起動

手順については、[公式の VS Code WSL チュートリアル](https://code.visualstudio.com/docs/remote/wsl-tutorial) を参照してください。

### 前提条件

- WSL がインストールされた Windows が必要です。WSL をインストールするには、PowerShell を管理者として開き、`wsl --install` を実行します（Ubuntu が一般的な選択肢です）。
- [WSL 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) がインストールされた VS Code

### WSL ターミナルから VS Code を開く

```bash
# From your WSL shell
cd ~/code/your-project
code .

これにより、WSL リモートウィンドウが開き、必要に応じて VS Code Server がインストールされ、統合ターミナルが Linux 内で動作するようになります。

### WSL への接続を確認

- 緑色のステータスバーに `WSL: <distro>` と表示されていることを確認します。
- 統合ターミナルには、`/home/...` などの Linux パスが表示され、`C:\` は表示されないはずです。
- 次のコマンドで確認できます：

  ```bash
  echo $WSL_DISTRO_NAME

  ディストリビューション名が出力されます。

  ステータスバーに「WSL: ...」が表示されない場合は、`Ctrl+Shift+P` を押し、
`WSL: Reopen Folder in WSL` を選択してください。パフォーマンスを最大限に高めるには、リポジトリを `/home/...` 配下（
`C:\` 配下ではなく）に置いてください。

  Windows アプリまたはプロジェクト選択画面に WSL リポジトリが表示されない場合は、
<code>\\wsl$</code> をファイル選択画面またはエクスプローラーに入力してから、使用している
  ディストリビューションのホームディレクトリに移動してください。

## WSL で Codex CLI を使用

管理者権限で開いた PowerShell または Windows ターミナルで、次のコマンドを実行してください：

```powershell
# Install default Linux distribution (like Ubuntu)
wsl --install

# Start a shell inside Windows Subsystem for Linux
wsl

続いて、WSL シェルから次のコマンドを実行してください：

```bash
# Install and run Codex in WSL
curl -fsSL https://chatgpt.com/codex/install.sh | sh
codex

## WSL 内でのコード作業

- Windows にマウントされた <code>/mnt/c/...</code> のようなパスで作業すると、Windows ネイティブのパスで作業するよりも遅くなることがあります。I/O を高速化し、シンボリックリンクや権限の問題を減らすには、リポジトリを Linux のホームディレクトリ（<code>~/code/my-app</code> など）配下に置いてください：
  ```bash
  mkdir -p ~/code && cd ~/code
  git clone https://github.com/your/repo.git
  cd repo
- Windows からファイルにアクセスする必要がある場合、対象のファイルはエクスプローラーの <code>\\wsl$\\Ubuntu\\home&lt;user\></code> 配下にあります。

## トラブルシューティングとよくある質問

- <code>/mnt/c</code> 配下で作業していないことを確認してください。リポジトリを WSL 内（例：<code>~/code/...</code>）に移動してください。
- 必要に応じて、WSL に割り当てるメモリと CPU を増やし、WSL を最新バージョンに更新します：
  ```powershell
  wsl --update
  wsl --shutdown

バイナリが WSL 内に存在し、そのディレクトリが `PATH` に含まれていることを確認します：

```bash
which codex || echo "codex not found"

バイナリが見つからない場合は、[Codex CLI のセットアップ手順](#use-codex-cli-with-wsl) に従ってください。
