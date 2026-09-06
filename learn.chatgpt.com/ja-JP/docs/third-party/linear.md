<!-- source: https://learn.chatgpt.com/ja-JP/docs/third-party/linear -->

Linear では、イシューから Codex に作業を委任できます。イシューを Codex に割り当てるか、コメントで `@Codex` にメンションすると、Codex がクラウドチャットを作成し、進捗と結果を返信します。

Linear での Codex は有料プランで利用できます（[料金](/ja-JP/codex/pricing)を参照）。

エンタープライズプランをご利用の場合は、ChatGPT ワークスペースの管理者に、[ワークスペース設定](https://chatgpt.com/admin/settings)で Codex のクラウドチャットを有効にし、[コネクタ設定](https://chatgpt.com/admin/ca)で **Codex for Linear** を有効にするよう依頼してください。

## Linear 連携のセットアップ

1. [Codex のクラウドチャット](/ja-JP/codex/cloud)をセットアップするには、[Codex](https://chatgpt.com/codex) で GitHub に接続し、Codex に作業させたいリポジトリの[環境](/ja-JP/codex/environments/cloud-environment)を作成します。
2. [Codex の設定](https://chatgpt.com/codex/settings/connectors)を開き、ワークスペースに **Codex for Linear** をインストールします。
3. Linear のイシューのコメントスレッドで `@Codex` にメンションし、Linear アカウントを連携します。

## Codex への作業の委任

委任方法は 2 つあります：

### Codex へのイシューの割り当て

連携をインストールすると、チームメンバーに割り当てるのと同じ方法でイシューを Codex に割り当てられます。Codex は作業を開始し、更新情報をイシューに投稿します。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### コメントでの `@Codex` へのメンション

コメントスレッドで `@Codex` にメンションして、作業を委任したり質問したりすることもできます。Codex から返信があったら、スレッドで追加の返信をして、同じチャットを続けます。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Codex がイシューの作業を開始すると、[作業する環境とリポジトリを選択します](#how-codex-chooses-an-environment-and-repo)。
特定のリポジトリを指定するには、コメントにそのリポジトリを含めます。例： `@Codex fix this in openai/codex`。

進捗を確認するには：

- イシューの **アクティビティ** を開き、進捗状況を確認します。
- チャットのリンクを開き、詳しい進捗を確認します。

Codex が作業を完了すると、要約と完了したチャットへのリンクを投稿します。このリンクから Pull Request を作成できます。

### Codex による環境とリポジトリの選択方法

- Linear はイシューのコンテキストに基づいてリポジトリを提案します。Codex はその提案に最も合う環境を選択します。リクエストが曖昧な場合は、直近に使用した環境を選択します。
- チャットは、その環境のリポジトリマップで最初に指定されているリポジトリのデフォルトブランチを対象に実行されます。別のリポジトリをデフォルトにする場合やリポジトリを追加する場合は、Codex でリポジトリマップを更新します。
- 適切な環境またはリポジトリが見つからない場合、Codex は Linear で、再試行前に問題を解決するための手順を返信します。

## Codex へのイシューの自動割り当て

トリアージルールを使用すると、イシューを Codex に自動で割り当てられます：

1. Linear で **設定**を開きます。
2. **自分のチーム**で、対象のチームを選択します。
3. ワークフロー設定で **トリアージ** を開き、有効にします。
4. **トリアージルール**でルールを作成し、 **委任** \> **Codex** を選択します（必要に応じて、ほかのプロパティも設定します）。

Linear は、トリアージに入った新しいイシューを Codex に自動で割り当てます。
トリアージルールを使用する場合、Codex はイシュー作成者のアカウントでチャットを実行します。

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## データの利用、プライバシー、セキュリティ

`@Codex` にメンションするか、イシューを Codex に割り当てると、Codex はリクエストを理解してチャットを作成するために、そのイシューの内容を受け取ります。
データの取り扱いは、OpenAI の[プライバシーポリシー](https://openai.com/privacy)、[利用規約](https://openai.com/terms/)、その他の適用される[ポリシー](https://openai.com/policies)に従います。
セキュリティについて詳しくは、[Codex のセキュリティドキュメント](/ja-JP/codex/agent-approvals-security)をご覧ください。

Codex が使用する大規模言語モデルは、誤った結果を出すことがあります。回答と差分は必ずレビューしてください。

## ヒントとトラブルシューティング

- **接続が見つからない場合**：Codex が Linear との接続を確認できない場合、アカウント接続用のリンクを含む返信をイシューに投稿します。
- **想定外の環境が選択された場合**：使用したい環境を指定してスレッドに返信します（例： `@Codex please run this in openai/codex`）。
- **コードの対象箇所が誤っている場合**：イシューにコンテキストを追加するか、`@Codex` へのコメントで具体的に指示します。
- **その他のヘルプ**：[OpenAI ヘルプセンター](https://help.openai.com/)をご覧ください。

<a id="connect-linear-for-local-tasks-mcp"></a>

## ローカル作業用の Linear 接続（MCP）

ChatGPT デスクトップアプリ、Codex CLI、または IDE 拡張機能から Linear のイシューにローカルでアクセスするには、Linear の Model Context Protocol（MCP）サーバーを構成します。

詳しくは、[Linear の MCP ドキュメント](https://linear.app/integrations/codex-mcp)をご覧ください。

IDE 拡張機能と CLI は同じ構成を共有しているため、どちらを使用する場合も MCP サーバーのセットアップ手順は同じです。

### CLI の使用（推奨）

CLI がインストールされている場合は、次のコマンドを実行します：

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

Linear アカウントでサインインし、そのアカウントを Codex に接続するよう求められます。

### 手動構成

1. エディターで `~/.codex/config.toml` を開きます。
2. 次の内容を追加します：

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. `codex mcp login linear` を実行してログインします。
