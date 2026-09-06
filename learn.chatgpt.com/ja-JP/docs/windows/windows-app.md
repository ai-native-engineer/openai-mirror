<!-- source: https://learn.chatgpt.com/ja-JP/docs/windows/windows-app -->

# Windows 向け ChatGPT デスクトップアプリ

[Windows 向け ChatGPT デスクトップアプリ](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) では、1 つのインターフェースで
プロジェクトを横断して作業し、複数のチャットを並行して実行し、結果をレビューできます。
Windows アプリは、Worktree、スケジュール済みタスク、Git 機能、
内蔵ブラウザ、ファイルプレビュー、プラグイン、スキルなどの主要なワークフローに対応しています。
PowerShell と
[Windows サンドボックス](/ja-JP/codex/windows/windows-sandbox#windows-sandbox) を使って Windows 上でネイティブに実行することも、
[Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl) で実行するよう構成することもできます。

  
    
  

## ChatGPT デスクトップアプリのダウンロード

Windows 向け [ChatGPT デスクトップアプリ](https://get.microsoft.com/installer/download/9PLM9XGG6VKS?cid=website_cta_psi) をダウンロードします。

次に、[クイックスタート](/ja-JP/codex/quickstart?setup=app) に沿って利用を開始します。

エンタープライズ向けのインストール方法と更新オプションについては、
[Windows アプリの展開](/ja-JP/codex/enterprise/windows-deployment) を参照してください。

コマンドラインからインストールする場合は、次のコマンドを実行します：

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

## ネイティブサンドボックス

Windows の ChatGPT デスクトップアプリは、エージェントを PowerShell で実行する場合はネイティブの [Windows サンドボックス](/ja-JP/codex/windows/windows-sandbox#windows-sandbox) に対応し、[Windows Subsystem for Linux 2 (WSL2)](#windows-subsystem-for-linux-wsl) で実行する場合は Linux のサンドボックスを使用します。どちらのモードでもサンドボックスによる保護を適用するには、Codex にメッセージを送信する前に、コンポーザーの下にある **承認を求める** を選択します。

  Codex をフルアクセスモードで実行すると、アクセス範囲がプロジェクトディレクトリに
  限定されず、意図しない破壊的な操作によって
  データが失われるおそれがあります。サンドボックスによる制限を維持し、
[ルール](/ja-JP/codex/agent-configuration/rules) で対象を絞って例外を設定するか、
[承認ポリシーを
  never に設定](/ja-JP/codex/agent-approvals-security#run-without-approval-prompts) してください。後者の場合、
  Codex は権限の昇格を求めずに問題の解決を試みます。
  この動作は [承認とセキュリティの設定](/ja-JP/codex/agent-approvals-security) に基づきます。

## 開発環境に合わせたカスタマイズ

<section class="feature-grid">

<div>

### 使用するエディター

**開く** で使用する既定のアプリとして、Visual Studio や VS Code などの
エディターを選択します。この選択はプロジェクトごとに上書きできます。すでに
 **開く** メニューでプロジェクトごとに別のアプリを選択している場合は、その
プロジェクト固有の選択が優先されます。

</div>

  
    
  

</section>

<section class="feature-grid inverse">

<div>

### 統合ターミナル

既定の統合ターミナルも選択できます。インストールされているツールに応じて、
次の選択肢があります：

- PowerShell
- コマンド プロンプト
- Git Bash
- WSL

この変更が適用されるのは、新しいターミナルセッションのみです。すでに
統合ターミナルを開いている場合、新しい既定のターミナルを表示するには、
アプリを再起動するか、新しいチャットを開始してください。

</div>

  
    
  

</section>

## Windows Subsystem for Linux (WSL)

既定では、ChatGPT デスクトップアプリは Windows ネイティブの Codex エージェントを使用し、
そのエージェントは PowerShell でコマンドを実行します。Windows Subsystem for Linux 2 (WSL2) 内の
プロジェクトも、必要に応じて `wsl` CLI を使って扱えます。

WSL ファイルシステムからプロジェクトを追加するには、 **新しいプロジェクトを追加** をクリックするか、
<kbd>Ctrl</kbd>+<kbd>O</kbd> を押し、エクスプローラーのウィンドウに `\\wsl$\` と入力します。
続いて、使用する Linux ディストリビューションと開くフォルダーを
選択します。

Windows ネイティブエージェントを引き続き使用する場合は、プロジェクトを
Windows ファイルシステムに保存し、WSL から
`/mnt/<drive>/...` 経由でアクセスすることをお勧めします。この方法は、プロジェクトを
WSL ファイルシステムから直接開くよりも確実です。

エージェント自体を WSL2 で実行するには、 **[設定](codex://settings)** を開き、
エージェントを Windows ネイティブから WSL に切り替えて、 **アプリを再起動** します。
再起動するまで変更は有効になりません。再起動後もプロジェクトは
そのまま保持されるはずです。

WSL1 は Codex `0.114` までサポートされていました。Codex `0.115` 以降は、Linux の
サンドボックスが `bubblewrap` に移行したため、WSL1 はサポートされなくなりました。

  
    
  

統合ターミナルは、エージェントとは別に設定します。
[開発環境に合わせたカスタマイズ](#customize-for-your-dev-setup) で、
ターミナルの選択肢を確認してください。ワークフローに応じて、エージェントを WSL で実行しながらターミナルでは PowerShell を
使用することも、両方で WSL を使用することもできます。

## 便利な開発ツール

一般的な開発ツールをいくつか事前にインストールしておくと、Codex を最大限に活用できます：

- **Git**：ChatGPT デスクトップアプリのレビューパネルを動作させ、変更内容の確認や
  取り消しを可能にします。
- **Node.js**：エージェントがタスクをより
  効率的に実行するために使用する一般的なツールです。
- **Python**：エージェントがタスクをより
  効率的に実行するために使用する一般的なツールです。
- **.NET SDK**：Windows ネイティブアプリのビルドに役立ちます。
- **GitHub CLI**：ChatGPT デスクトップアプリで GitHub 固有の機能を利用できるようにします。

Windows の既定のパッケージマネージャー `winget` でこれらをインストールするには、次の内容を
[統合ターミナル](/ja-JP/codex/integrated-terminal) に貼り付けるか、
Codex にインストールを依頼します：

```powershell
winget install --id Git.Git
winget install --id OpenJS.NodeJS.LTS
winget install --id Python.Python.3.14
winget install --id Microsoft.DotNet.SDK.10
winget install --id GitHub.cli
```

GitHub CLI をインストールしたら、`gh auth login` を実行して、アプリの
GitHub 機能を有効にします。

Python または .NET の別のバージョンが必要な場合は、パッケージ ID を希望する
バージョンのものに変更してください。

## トラブルシューティングとよくある質問

### 昇格した権限でのコマンド実行

Codex に昇格した権限でコマンドを実行させる必要がある場合は、
ChatGPT デスクトップアプリ自体を管理者として起動します。インストール後にスタートメニューを開き、
アプリを探して **管理者として実行** を選択します。Codex エージェントはその
権限レベルを継承します。

### PowerShell の実行ポリシーによるコマンドのブロック

PowerShell で Node.js や `npm` などのツールを使用したことがない場合、
Codex エージェントまたは統合ターミナルで、実行ポリシーに関するエラーが発生することがあります。

Codex が PowerShell スクリプトを作成した場合にも、同じ問題が発生することがあります。
その場合、PowerShell でスクリプトを実行する前に、
制限の緩い実行ポリシーに変更する必要が生じることがあります。

エラーは次のように表示されることがあります：

```text
npm.ps1 cannot be loaded because running scripts is disabled on this system.
```

一般的な対処方法は、実行ポリシーを `RemoteSigned` に設定することです：

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
```

ポリシーを変更する前に、詳細やその他の選択肢について、Microsoft の
[実行ポリシーガイド](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies) を
確認してください。

### Windows のローカル環境スクリプト

[ローカル環境](/ja-JP/codex/environments/local-environment) でクロスプラットフォーム対応の
`npm` スクリプトなどのコマンドを使用している場合は、1 つのセットアップスクリプトまたは
アクションセットをすべてのプラットフォームで共有できます。

Windows 固有の動作が必要な場合は、Windows 固有のセットアップスクリプトまたは
Windows 固有のアクションを作成します。

アクションは、統合ターミナルで使用している環境で実行されます。詳しくは、
[開発環境に合わせたカスタマイズ](#customize-for-your-dev-setup) を参照してください。

ローカルのセットアップスクリプトは、エージェントの実行環境で動作します。エージェントが WSL を使用している場合は WSL、
それ以外の場合は PowerShell で実行されます。

### WSL との構成、認証、セッションの共有

Windows アプリは、Windows ネイティブ版 Codex と同じ Codex ホームディレクトリを使用します：
`%USERPROFILE%\.codex`。

WSL 内でも Codex CLI を実行する場合、CLI は既定で Linux のホームディレクトリを使用するため、
構成、キャッシュされた認証情報、セッション履歴は
Windows アプリと自動的には共有されません。

これらを共有するには、次のいずれかの方法を使用します：

- ファイルシステム上で、WSL の `~/.codex` を `%USERPROFILE%\.codex` と同期します。
- `CODEX_HOME` を設定し、WSL の参照先を Windows の Codex ホームディレクトリに指定します：

```bash

```

すべてのシェルでこの設定を有効にするには、
WSL のシェルプロファイル（`~/.bashrc` や `~/.zshrc` など）に追加します。

### Git 機能の利用不可

Windows に Git がネイティブインストールされていない場合は、
アプリの一部の機能を使用できません。`winget install Git.Git` を PowerShell または `cmd.exe` で実行し、Git をインストールします。

### `\\wsl$` から開いたプロジェクトにおける Git の検出失敗

Windows ネイティブのエージェントで、WSL からもアクセスできるプロジェクトを使用する場合は、
プロジェクトを Windows のネイティブドライブに保存し、
WSL から `/mnt/<drive>/...` 経由でアクセスする方法が、現時点では最も確実な回避策です。

### `Cmder` が「開く」ダイアログに表示されない問題

`Cmder` がインストールされているにもかかわらず Codex の「開く」ダイアログに表示されない場合は、
Windows のスタートメニューに追加します。`Cmder` を右クリックして **スタートに追加**を選択し、
Codex またはコンピューターを再起動します。
