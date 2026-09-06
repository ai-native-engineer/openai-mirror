<!-- source: https://learn.chatgpt.com/ja-JP/docs/codex-sdk -->

Codex CLI、IDE 拡張機能、Codex Cloud のいずれかで Codex を使用している場合は、プログラムから制御することもできます。

次のような場合は SDK を使用します：

- CI/CD パイプラインの一部として Codex を制御する
- Codex と連携して複雑なエンジニアリングタスクを実行できる独自のエージェントを作成する
- 独自の社内ツールやワークフローに Codex を組み込む
- 独自のアプリケーションに Codex を統合する

CI のジョブを含むコーディングタスクを自動化するには、Codex SDK を使用します。認証、会話履歴、承認、ストリーミング配信されるエージェントイベントを扱うカスタムクライアントを構築するには、[Codex app server](/ja-JP/codex/app-server) を使用します。

`codex mcp-server` は非推奨です。既存の連携向けに、[MCP サーバーガイド](/ja-JP/codex/mcp-server)は引き続き利用できます。

ベータ版へのアクセス権があり、リポジトリまたは変更内容をスキャンして、構造化された
セキュリティ検出結果とカバレッジを取得する必要がある場合は、[Codex Security TypeScript
SDK](/ja-JP/codex/security/sdk) を使用します。

## TypeScript ライブラリ

TypeScript ライブラリを使うと、アプリケーションからローカルの Codex スレッドを開始、継続、再開できます。

このライブラリはサーバー側で使用してください。Node.js 18 以降が必要です。

### インストール

はじめに、`npm` を使用して Codex SDK をインストールします：

```bash
npm install @openai/codex-sdk

### 使用方法

Codex でスレッドを開始し、プロンプトを指定して実行します。

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

同じスレッドで処理を続けるには、もう一度 `run()` を呼び出します。以前のスレッドを再開するには、スレッド ID を指定します。

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

詳しくは、[TypeScript リポジトリ](https://github.com/openai/codex/tree/main/sdk/typescript)をご覧ください。

## Python ライブラリ

Python SDK は、JSON-RPC 経由でローカルの Codex app-server を制御します。Python 3.10 以降が必要です。公開済みの SDK ビルドには、バージョンが固定された Codex CLI ランタイムが依存関係として含まれています。

### インストール

SDK をインストールするには、次を実行します：

```bash
pip install openai-codex

公開済みの SDK ビルドは、バージョンが固定されたランタイムを自動的に使用します。特定のローカル Codex 実行ファイルを意図的に使用する場合にのみ、`CodexConfig(codex_bin=...)` を渡してください。

Python SDK は安定版として提供されています。`pip install openai-codex`
を実行すると、最新の安定版がインストールされます。より新しいプレリリースビルドを利用するには、`pip install --pre openai-codex` を
使用します。

### 使用方法

Codex を起動してスレッドを作成し、プロンプトを実行します：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

アプリケーションですでに非同期処理を使用している場合は、`AsyncCodex` を使用します：

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### サンドボックスのプリセット

スレッドの作成時や、後続のターンのファイルシステムアクセスを変更するときには、同じ `Sandbox` プリセットを
使用します：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

利用可能なプリセット：

- `Sandbox.read_only`：ファイルの読み取りを許可し、書き込みは許可しません。
- `Sandbox.workspace_write`：ファイルの読み取りと、ワークスペースおよび設定済みの書き込み可能なルート内への書き込みを許可します。
- `Sandbox.full_access`：ファイルシステムへのアクセスを制限せずに実行します。

`sandbox=` を省略すると、app-server は設定済みのデフォルト値を使用します。サンドボックス設定を
`run(...)` または `turn(...)` に渡すと、そのターンおよび
同じスレッド内の後続のターンに適用されます。

詳しくは、[Python リポジトリ](https://github.com/openai/codex/tree/main/sdk/python)をご覧ください。
