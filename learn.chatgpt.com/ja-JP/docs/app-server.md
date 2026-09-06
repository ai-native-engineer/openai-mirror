<!-- source: https://learn.chatgpt.com/ja-JP/docs/app-server -->

Codex app-server は、Codex VS Code 拡張機能など、多機能なクライアントを動かすために Codex が使用するインターフェースです。認証、会話履歴、承認、エージェントイベントのストリーミングなどを独自の製品に深く統合したい場合に使用します。app-server の実装は、Codex の GitHub リポジトリ（[openai/codex/codex-rs/app-server](https://github.com/openai/codex/tree/main/codex-rs/app-server)）でオープンソースとして公開されています。Codex のオープンソースコンポーネントの一覧は、[オープンソース](/ja-JP/codex/open-source)のページを参照してください。

  ジョブを自動化する場合や CI で Codex を実行する場合は、代わりに
<a href="/codex/codex-sdk">Codex SDK</a> を使用してください。

## CLI ターミナル UI の接続

リモートターミナル UI モードでは、あるマシンで app-server を実行し、別のマシンの Codex CLI ターミナルインターフェースから接続できます。WebSocket リスナーを起動します：

```bash
codex app-server --listen ws://127.0.0.1:4500

続いて、ターミナル UI を接続します：

```bash
codex --remote ws://127.0.0.1:4500

ローカル以外から接続する場合は、WebSocket 認証を設定し、TLS で接続を保護します。ベアラートークンは環境変数に保存し、トークンそのものをコマンドラインに指定する代わりに、その環境変数名を渡します：

```bash

codex --remote wss://remote-host:4500 \
  --remote-auth-token-env CODEX_REMOTE_TOKEN

`--remote` オプションには、`ws://`、`wss://`、`unix://`、
`unix://PATH` の各エンドポイントを指定できます。平文の WebSocket は、localhost または
SSH ポートフォワーディング経由の接続にのみ使用してください。

## リモート Code Mode ホストへの接続

デフォルトでは、app-server はローカルの Code Mode ホストを起動します。代わりにリモートホストを使用するには、そのホストのセキュアな WebSocket URL を指定します：

```bash
codex app-server --code-mode-host wss://code-mode.example.com/host

`--code-mode-host` は、app-server から Code Mode ホストへのアウトバウンド接続を制御します。
クライアントから app-server への接続方法を制御する `--listen` は変更しません。
同じ app-server プロセス内のすべてのスレッドは、選択された
Code Mode ホストへの接続を共有します。

リモートホストには `wss://` を使用してください。`ws://` は localhost または
SSH ポートフォワーディング経由の接続にのみ使用してください。app-server コマンドと
WebSocket トランスポートはいずれも実験的な機能で、本番ワークロードでの使用はサポートされていません。

## プロトコル

[MCP](https://modelcontextprotocol.io/) と同様に、`codex app-server` は JSON-RPC 2.0 メッセージによる双方向通信をサポートします（通信時には `"jsonrpc":"2.0"` ヘッダーを省略します）。

対応するトランスポート：

- `stdio`（`--listen stdio://`、デフォルト）：改行区切りの JSON（JSONL）
- `websocket`（`--listen ws://IP:PORT`、実験的でサポート対象外）：
  WebSocket テキストフレームごとに 1 件の JSON-RPC メッセージ
- Unix ソケット（`--listen unix://` または `--listen unix://PATH`）：標準の HTTP Upgrade ハンドシェイクを使用し、
  Codex のデフォルトの app-server 制御ソケット、またはカスタムの
  Unix ソケットパスを経由する WebSocket 接続
- `off`（`--listen off`）：ローカルトランスポートを公開しない

`--listen ws://IP:PORT` で実行すると、同じリスナーが基本的な
HTTP ヘルスプローブにも応答します：

- `GET /readyz` は、リスナーが新しい接続の受け入れを開始すると `200 OK` を返します。
- `GET /healthz` は、リクエストに `Origin` ヘッダーが含まれていない場合に
  `200 OK` を返します。
- `Origin` ヘッダーを含むリクエストは、`403 Forbidden` で拒否されます。

WebSocket トランスポートは実験的な機能で、サポート対象外です。
`ws://127.0.0.1:PORT` などのローカルリスナーは、localhost や SSH ポートフォワーディングを使うワークフローに適しています。
ロールアウト中の現時点では、ループバック以外の
WebSocket リスナーはデフォルトで未認証の接続を許可します。そのため、リモートからアクセスできるように公開する前に、
WebSocket 認証を設定してください。

対応する WebSocket 認証フラグ：

- `--ws-auth capability-token --ws-token-file /absolute/path`
- `--ws-auth capability-token --ws-token-sha256 HEX`
- `--ws-auth signed-bearer-token --ws-shared-secret-file /absolute/path`

署名付きベアラートークンを使用する場合は、`--ws-issuer`、`--ws-audience`、
`--ws-max-clock-skew-seconds` も設定できます。クライアントは WebSocket ハンドシェイク時に認証情報を
`Authorization: Bearer <token>` として提示します。app-server は
JSON-RPC の `initialize` より前に認証を必須とします。

生のベアラートークンをコマンドラインで渡すよりも、`--ws-token-file` の使用を推奨します。
`--ws-token-sha256` は、クライアントが高エントロピーの生のトークンを別のローカルシークレットストアに保持している場合にのみ使用してください。
ハッシュは検証用の値にすぎません。
クライアントには引き続き元のトークンが必要です。

WebSocket モードでは、app-server は容量に上限のあるキューを使用します。リクエストの受信キューがいっぱいになると、
サーバーは JSON-RPC エラーコード `-32001` とメッセージ
`"Server overloaded; retry later."` を返して新しいリクエストを拒否します。
クライアントは、待機時間を指数関数的に延ばし、ジッターを加えて再試行してください。

## メッセージスキーマ

リクエストには `method`、`params`、`id` が含まれます：

```json
{ "method": "thread/start", "id": 10, "params": { "model": "gpt-5.6-terra" } }

レスポンスでは、同じ `id` が `result` または `error` とともに返されます：

```json
{ "id": 10, "result": { "thread": { "id": "thr_123" } } }

```json
{ "id": 10, "error": { "code": 123, "message": "Something went wrong" } }

通知では `id` を省略し、`method` と `params` のみを使用します：

```json
{ "method": "turn/started", "params": { "turn": { "id": "turn_456" } } }

CLI から TypeScript スキーマまたは JSON Schema バンドルを生成できます。各出力は実行した Codex のバージョンに固有のもので、生成された成果物はそのバージョンと完全に一致します：

```bash
codex app-server generate-ts --out ./schemas
codex app-server generate-json-schema --out ./schemas

## はじめに

1. サーバーは `codex app-server`（デフォルトの stdio トランスポート）、
`codex app-server --listen ws://127.0.0.1:4500`（TCP WebSocket）、または
`codex app-server --listen unix://`（デフォルトの Unix ソケット）で起動します。
2. 選択したトランスポート経由でクライアントを接続し、`initialize`、続いて `initialized` 通知を送信します。
3. スレッドとターンを開始し、アクティブなトランスポートストリームから通知を読み続けます。

例（Node.js / TypeScript）：

```ts

const proc = spawn("codex", ["app-server"], {
  stdio: ["pipe", "pipe", "inherit"],
});
const rl = readline.createInterface({ input: proc.stdout });

const send = (message: unknown) => {
  proc.stdin.write(`${JSON.stringify(message)}\n`);
};

let threadId: string | null = null;

rl.on("line", (line) => {
  const msg = JSON.parse(line) as any;
  console.log("server:", msg);

  if (msg.id === 1 && msg.result?.thread?.id && !threadId) {
    threadId = msg.result.thread.id;
    send({
      method: "turn/start",
      id: 2,
      params: {
        threadId,
        input: [{ type: "text", text: "Summarize this repo." }],
      },
    });
  }
});

send({
  method: "initialize",
  id: 0,
  params: {
    clientInfo: {
      name: "my_product",
      title: "My Product",
      version: "0.1.0",
    },
  },
});
send({ method: "initialized", params: {} });
send({ method: "thread/start", id: 1, params: { model: "gpt-5.6-terra" } });

## 基本要素

- **スレッド**：ユーザーと Codex エージェントの間の会話です。スレッドにはターンが含まれます。
- **ターン**：1 件のユーザーリクエストと、それに続くエージェントの作業から成ります。ターンにはアイテムが含まれ、更新内容が順次ストリーミング配信されます。
- **アイテム**：入出力の単位（ユーザーメッセージ、エージェントメッセージ、コマンド実行、ファイル変更、ツール呼び出しなど）

スレッド API を使用して、会話を作成、一覧表示、アーカイブします。ターン API で会話を進め、ターン通知を通じて進行状況をストリーミング配信します。

## ライフサイクルの概要

- **接続ごとに一度だけ初期化**：トランスポート接続を開いた直後に、クライアントのメタデータを含む `initialize` リクエストを送信し、続いて `initialized` を送信します。サーバーは、このハンドシェイクより前にその接続上で受信したすべてのリクエストを拒否します。
- **スレッドの開始（または再開）**：新しい会話を始めるには `thread/start`、既存の会話を続けるには `thread/resume`、履歴を新しいスレッド ID に分岐させるには `thread/fork` を呼び出します。
- **ターンの開始**：対象の `threadId` とユーザー入力を指定して `turn/start` を呼び出します。オプションのフィールドでは、モデル、パーソナリティ、`cwd`、サンドボックスポリシーなどを上書きできます。
- **進行中のターンへの追加指示**：`turn/steer` を呼び出すと、新しいターンを作成せずに、現在進行中のターンへユーザー入力を追加できます。
- **イベントのストリーミング**：`turn/start` の実行後は、stdout に出力される通知を読み続けます。これには `thread/archived`、`thread/unarchived`、`item/started`、`item/completed`、`item/agentMessage/delta`、ツールの進行状況、その他の更新が含まれます。
- **ターンの終了**：モデルの処理が完了したとき、または `turn/interrupt` によるキャンセル後に、サーバーは最終ステータスを含む `turn/completed` を送信します。

## 初期化

クライアントは各トランスポート接続で、他のメソッドを呼び出す前に `initialize` リクエストを一度だけ送信し、その後 `initialized` 通知で確認応答する必要があります。初期化前に送信されたリクエストには `Not initialized` エラーが返され、同じ接続で `initialize` を繰り返し呼び出すと `Already initialized` が返されます。

サーバーは、上流サービスに提示するユーザーエージェント文字列に加え、実行環境を示す `platformFamily` と `platformOs` の値を返します。連携機能を識別するために `clientInfo` を設定してください。

`initialize.params.capabilities` では、次のクライアント機能もサポートされます：

- `optOutNotificationMethods`：この接続で抑制する通知のメソッド名を指定します。
  照合は完全一致で、ワイルドカードやプレフィックスでの照合は行いません。
  不明な名前は受け付けられますが、無視されます。
- `requestAttestation`：サーバーから開始される `attestation/generate` リクエストの受信を有効にします。
  上流サービス向けのアテステーションを提供するデスクトップホストは、
  不透明な値 `{ "token": "..." }` で応答します。
- `mcpServerOpenaiFormElicitation`：下流の MCP サーバーによる
  OpenAI の拡張フォーム形式の `mcpServer/elicitation/request` の送信を許可

**重要**：コンプライアンス・ログ・プラットフォームでクライアントを識別するため、`clientInfo.name` を使用してください。企業での利用を想定した新しい Codex 連携機能を開発している場合は、既知のクライアント一覧への追加について OpenAI にお問い合わせください。詳しくは、[Codex ログのリファレンス](https://chatgpt.com/public/admin/api-reference#tag/Codex)を参照してください。

例（Codex VS Code 拡張機能より）：

```json
{
  "method": "initialize",
  "id": 0,
  "params": {
    "clientInfo": {
      "name": "codex_vscode",
      "title": "Codex VS Code Extension",
      "version": "0.1.0"
    }
  }
}

通知のオプトアウト例：

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true,
      "optOutNotificationMethods": ["thread/started", "item/agentMessage/delta"]
    }
  }
}

## 実験的 API へのオプトイン

app-server の一部のメソッドとフィールドは、`experimentalApi` 機能を有効にした場合にのみ利用できる設計になっています。

- 安定版 API のみを使用するには、`capabilities` を省略するか、`experimentalApi` を `false` に設定します。この場合、サーバーは実験的なメソッドやフィールドを拒否します。
- 試験的なメソッドとフィールドを有効にするには、`capabilities.experimentalApi` を `true` に設定します。

```json
{
  "method": "initialize",
  "id": 1,
  "params": {
    "clientInfo": {
      "name": "my_client",
      "title": "My Client",
      "version": "0.1.0"
    },
    "capabilities": {
      "experimentalApi": true
    }
  }
}

クライアントがオプトインせずに試験的なメソッドまたはフィールドを送信すると、app-server は次のエラーを返して拒否します。

`<descriptor> requires experimentalApi capability`

## API の概要

- `thread/start` - 新しいスレッドを作成し、`thread/started` を送出します。そのスレッドのターンとアイテムのイベントの購読も自動的に開始します。
- `thread/resume` - ID を指定して既存のスレッドを再度開き、以後の `turn/start` 呼び出しでそのスレッドにターンを追加できるようにします。
- `thread/fork` - 保存済みの履歴をコピーし、新しいスレッド ID でスレッドをフォークします。`lastTurnId` を渡すと、そのターンまでの履歴をコピーし、それ以降のターンを除外します。`ephemeral: true` を渡すと、メモリ内にフォークを作成します。新しいスレッドに対して `thread/started` を送出し、返されるスレッドには、利用可能な場合に `forkedFromId` が含まれます。
- `thread/read` - スレッドを再開せずに、ID を指定して保存済みのスレッドを取得します。`includeTurns` を設定すると、ターン履歴全体が返されます。返される `thread` オブジェクトには、実行時の `status` が含まれます。
- `thread/list` - 保存済みのスレッドログをページ単位で取得します。カーソルベースのページネーションに加え、`modelProviders`、`sourceKinds`、`archived`、`isPinned`、`cwd`、`useStateDbOnly`、`searchTerm`、試験的な `parentThreadId` または `ancestorThreadId` のフィルターに対応しています。返される `thread` オブジェクトには、実行時の `status` が含まれます。
- `thread/turns/list` - 試験的機能です。スレッドを再開せずに、保存済みのスレッドのターン履歴をページ単位で取得します。`itemsView` で、ターン内のアイテムを省略するか、要約するか、全内容を読み込むかを制御します。
- `thread/items/list` - 試験的機能です。永続化されたスレッドアイテムをページ単位で取得します。必要に応じて、1 つの `turnId` に限定することもできます。使用中のスレッドストアがアイテムのページネーションに対応している必要があります。
- `thread/loaded/list` - 現在メモリに読み込まれているスレッド ID の一覧を取得します。
- `thread/name/set` - 読み込み済みのスレッドまたは永続化されたロールアウトについて、ユーザーに表示するスレッド名を設定または更新し、`thread/name/updated` を送出します。
- `thread/goal/set` - スレッドの目標を設定し、`thread/goal/updated` を送出します。
- `thread/goal/get` - スレッドの現在の目標を取得します。
- `thread/goal/clear` - スレッドの目標をクリアし、`thread/goal/cleared` を送出します。
- `thread/metadata/update` - 永続化された `gitInfo` と `isPinned` を含む、SQLite に保存されたスレッドメタデータを部分更新します。
- `thread/archive` - スレッドのログファイルをアーカイブディレクトリに移動します。そこから生成された子孫スレッドのうち、未アーカイブのスレッドのログについてもアーカイブを試みます。成功すると `{}` を返し、アーカイブしたスレッドごとに `thread/archived` を送出します。
- `thread/delete` - 永続化されたアクティブなスレッドまたはアーカイブ済みのスレッドと、そこから生成されたすべての子孫スレッドを完全に削除します。成功すると `{}` を返し、削除したスレッドごとに `thread/deleted` を送出します。
- `thread/unsubscribe` - この接続によるスレッドのターンとアイテムのイベントの購読を解除します。これが最後の購読者だった場合、購読者がいない非アクティブ状態で猶予期間が経過すると、サーバーはスレッドをメモリから解放し、`thread/closed` を送出します。
- `thread/unarchive` - アーカイブ済みのスレッドのロールアウトを、アクティブなセッションのディレクトリに復元します。復元した `thread` を返し、`thread/unarchived` を送出します。
- `thread/status/changed` - 読み込み済みのスレッドの実行時の `status` が変更されたときに送出される通知
- `thread/compact/start` - スレッドの会話履歴のコンパクションを開始します。すぐに `{}` を返し、進捗は `turn/*` と `item/*` の通知を通じてストリーミングされます。
- `thread/shellCommand` - ユーザーの操作に基づいて、スレッドに対してシェルコマンドを実行します。このコマンドはサンドボックスの外部でフルアクセスで実行され、スレッドのサンドボックスポリシーを継承しません。
- `thread/backgroundTerminals/clean` - スレッドで実行中のバックグラウンド ターミナルをすべて停止します（試験的機能、`capabilities.experimentalApi` が必要）。
- `thread/backgroundTerminals/list` - 読み込み済みのスレッドで実行中のバックグラウンド ターミナルの一覧を取得します（試験的機能、`capabilities.experimentalApi` が必要）。
- `thread/backgroundTerminals/terminate` - app-server の `processId` を指定して、実行中のバックグラウンド ターミナルを 1 つ終了します（試験的機能、`capabilities.experimentalApi` が必要）。
- `thread/rollback` - 非推奨です。メモリ内のコンテキストから直近 N 件のターンを削除し、ロールバックマーカーを永続化します。更新後の `thread` を返します。
- `turn/start` - スレッドにユーザー入力または単独のツール出力を追加して、Codex による生成を開始します。初期状態の `turn` を応答として返し、イベントをストリーミングします。`collaborationMode` では、`settings.developer_instructions: null` は「選択したモードの組み込みの指示を使用する」という意味です。
- `thread/inject_items` - ユーザーのターンを開始せずに、読み込み済みのスレッドでモデルが参照する履歴に、未加工の Responses API アイテムを追加します。
- `turn/steer` - スレッドで現在進行中のターンにユーザー入力を追加し、受け付けた `turnId` を返します。
- `turn/interrupt` - 進行中のターンのキャンセルをリクエストします。成功すると `{}` を返し、ターンは `status: "interrupted"` で終了します。
- `review/start` - スレッドの Codex レビュアーを開始し、`enteredReviewMode` アイテムと `exitedReviewMode` アイテムを送出します。
- `command/exec` - スレッドやターンを開始せずに、サーバーのサンドボックス内で 1 つのコマンドを実行します。
- `command/exec/write` - 実行中の `command/exec` セッションの `stdin` にバイト列を書き込むか、`stdin` を閉じます。
- `command/exec/resize` - 実行中の PTY ベースの `command/exec` セッションのサイズを変更します。
- `command/exec/terminate` - 実行中の `command/exec` セッションを停止します。
- `command/exec/outputDelta`（通知） - ストリーミング中の `command/exec` セッションから出力される、base64 でエンコードされた stdout/stderr のチャンクを伝える通知
- `process/spawn` - Codex のサンドボックス外でプロセスセッションを明示的に開始します（試験的機能、`capabilities.experimentalApi` が必要）。
- `process/writeStdin` - 実行中の `process/spawn` セッションの stdin にバイト列を書き込むか、stdin を閉じます（試験的機能）。
- `process/resizePty` - 実行中の PTY ベースのプロセスセッションのサイズを変更します（試験的機能）。
- `process/kill` - 実行中のプロセスセッションを終了します（試験的機能）。
- `process/outputDelta` と `process/exited`（通知） - プロセス出力のストリーミングとプロセスの終了ステータスを伝える通知（試験的機能）
- `model/list` - 利用可能なモデルの一覧を取得します。`includeHidden: true` を設定すると、`hidden: true` のエントリも含まれます。各モデルには、推論強度の選択肢、任意項目の `upgrade`、`inputModalities` が含まれます。
- `modelProvider/capabilities/read` - モデルとプロバイダーの組み合わせごとに、プロバイダーが対応する機能の範囲を取得します。
- `experimentalFeature/list` - ライフサイクル段階のメタデータを含む機能フラグの一覧を、カーソルベースのページネーションで取得します。
- `experimentalFeature/enablement/set` - `apps` や `plugins` など、サポート対象の機能キーについて、メモリ内の実行時設定を部分更新します。
- `environment/info` - 試験的機能です。設定済みの実行環境に接続し、そのシェルとデフォルトの作業ディレクトリを返します。
- `permissionProfile/list` - ベータ版の権限プロファイルの一覧を、適用中の要件でそれぞれが許可されるかどうかの情報とともに取得します。カーソルベースのページネーションに対応しています。
- `collaborationMode/list` - コラボレーションモードのプリセットの一覧を取得します（試験的機能、ページネーションなし）。
- `skills/list` - 1 つ以上の `cwd` の値に対応するスキルの一覧を取得します（`forceReload` と任意指定の `perCwdExtraUserRoots` に対応）。
- `skills/extraRoots/set` - スタンドアロンのスキルを検出するための、プロセス単位の追加ルートを置き換えます。この設定は永続化しません。
- `skills/changed`（通知） - 監視対象のローカルスキルファイルが変更されたときに送出される通知
- `hooks/list` - 1 つ以上の `cwd` の値について、検出されたライフサイクルフックの一覧を取得します。
- `marketplace/add` - リモートのプラグインマーケットプレイスを追加し、ユーザーのマーケットプレイス設定に永続化します。
- `marketplace/remove` - 設定済みのマーケットプレイスを削除し、インストール済みのマーケットプレイスルートが存在する場合は、それも削除します。
- `marketplace/upgrade` - 設定済みの Git マーケットプレイスを更新します。マーケットプレイス名を省略すると、設定済みのすべての Git マーケットプレイスを更新します。
- `plugin/list` - 開発中です。検出されたプラグインマーケットプレイスとプラグインの状態の一覧を取得します。これには、インストールと認証のポリシーメタデータ、マーケットプレイスの読み込みエラー、注目のプラグイン ID、ローカル、Git、パッケージレジストリ、またはリモートのプラグインソースに関するメタデータが含まれます。概要には、リモートの `version`、ローカルの `localVersion`、構造化されたライト／ダーク用アイコン情報、および `installPolicySource` が含まれる場合があります。現在のリモートエントリでは、この値は `null`、`WORKSPACE_SETTING`、`IMPLICIT_CANONICAL_APP` のいずれかになります。現時点では、本番環境のクライアントからこのメソッドを呼び出さないでください。
- `plugin/read` - 開発中です。マーケットプレイスのパスまたはリモートマーケットプレイス名に加えてプラグイン名を指定し、1 つのプラグインを取得します。同梱のスキルやアプリ、MCP サーバー名が含まれ、リモートカタログが提供している場合は、リモートプラグインの `shareUrl` も含まれます。現時点では、本番環境のクライアントからこのメソッドを呼び出さないでください。
- `plugin/install` - 開発中です。マーケットプレイスのパスまたはリモートマーケットプレイス名を指定して、プラグインをインストールします。現時点では、本番環境のクライアントからこのメソッドを呼び出さないでください。
- `plugin/uninstall` - 開発中です。インストール済みのプラグインをアンインストールします。現時点では、本番環境のクライアントからこのメソッドを呼び出さないでください。
- `plugin/skill/read` - リモートマーケットプレイス、プラグイン ID、スキル名を指定して、リモートプラグインに含まれるスキルの Markdown をオンデマンドで取得します。
- `app/installed` - インストール済みアプリの実行時の状態を取得します。各アプリが実際に有効かどうか、呼び出し可能かどうかも含まれます。
- `app/list` - 利用可能なアプリ（コネクタ）の一覧をページ単位で取得します。アクセス可否と有効状態のメタデータも含まれます。
- `app/read` - 指定したアプリ ID のメタデータと、必要に応じて表示専用のツール概要を取得します。
- `skills/config/write` - パスを指定してスキルを有効または無効にします。
- `mcpServer/oauth/login` - 構成済みの MCP サーバーへの OAuth ログインを開始し、認可 URL を返します。完了時に `mcpServer/oauthLogin/completed` を発行します。
- `tool/requestUserInput` - ツール呼び出しのために、ユーザーに 1～3 件の短い質問への回答を求めます（実験的）。質問では、自由入力の選択肢に `isOther` を設定できます。
- `mcpServer/elicitation/request`（サーバーリクエスト） - 構造化フォームへの入力、または MCP サーバーから要求された URL フローの確認をクライアントに求めます。
- `item/permissions/requestApproval`（サーバーリクエスト） - 組み込みの `request_permissions` ツールが要求したネットワークまたはファイルシステムの権限の一部を付与するよう、クライアントに求めます。
- `config/mcpServer/reload` - MCP サーバーの構成をディスクから再読み込みし、読み込み済みスレッドの更新をキューに登録します。
- `mcpServerStatus/list` - MCP サーバー、ツール、リソース、認証状態を一覧表示します（カーソルと件数上限によるページネーション）。すべてのデータを取得するには `detail: "full"`、リソースを省略するには `detail: "toolsAndAuthOnly"` を使用します。
- `mcpServer/resource/read` - 初期化済みの MCP サーバーを介して、単一の MCP リソースを読み取ります。
- `mcpServer/tool/call` - スレッド用に構成された MCP サーバー上のツールを呼び出します。
- `mcpServer/startupStatus/updated`（通知） - 読み込み済みスレッドで、構成済みの MCP サーバーの起動状態が変化したときに発行されます。
- `windowsSandbox/setupStart` - `elevated` または `unelevated` モードで Windows サンドボックスのセットアップを開始します。すぐにレスポンスを返し、その後 `windowsSandbox/setupCompleted` を発行します。
- `feedback/upload` - フィードバックレポートを送信します（分類、任意の理由やログ、会話 ID、および任意の `extraLogFiles` 添付ファイル）。
- `config/read` - ディスク上の構成を階層に従って統合し、実効構成を取得します。
- `externalAgentConfig/detect` - `includeHome` と省略可能な `cwds` を使用して、移行可能な外部エージェントのアーティファクトを検出します。検出された各項目には `cwd` が含まれます（ホームの場合は `null`）。
- `externalAgentConfig/import` - `migrationItems` を明示的に渡し、各項目に `cwd`（ホームの場合は `null`）を指定して、選択した外部エージェントの移行項目を適用します。サポートされる項目の種類には、構成、スキル、`AGENTS.md`、プラグイン、MCP サーバーの構成、サブエージェント、フック、コマンド、セッションがあります。インポート対象がある場合は、処理の完了に伴って `externalAgentConfig/import/progress` と `externalAgentConfig/import/completed` が発行されます。プラグインとセッションのインポートは非同期で完了する場合があります。
- `config/value/write` - ディスク上にあるユーザーの `config.toml` に、構成のキーと値を 1 組書き込みます。
- `config/batchWrite` - ディスク上にあるユーザーの `config.toml` に、構成の変更をアトミックに適用します。
- `configRequirements/read` - `requirements.toml` と MDM のいずれかまたは両方から、管理対象の設定の正確な内容、許可リスト、固定された `featureRequirements`、ネットワーク要件を含む要件を取得します（要件が未設定の場合は `null`）。
- `fs/readFile`、`fs/writeFile`、`fs/createDirectory`、`fs/getMetadata`、`fs/readDirectory`、`fs/remove`、`fs/copy`、`fs/watch`、`fs/unwatch`、および `fs/changed`（通知） - app-server v2 ファイルシステム API を介して、ファイルシステム上の絶対パスを対象に操作します。

プラグインの概要にはユニオン型の `source` が含まれます。ローカルプラグインは
`{ "type": "local", "path": ... }`、Git ベースのマーケットプレイスのエントリは
`{ "type": "git", "url": ..., "path": ..., "refName": ..., "sha": ... }` を返します。
パッケージレジストリのエントリは
`{ "type": "npm", "package": ..., "version": ..., "registry": ... }`、
リモートカタログのエントリは `{ "type": "remote" }` を返します。
リモートのみのカタログエントリでは、`PluginMarketplaceEntry.path` が `null` になる場合があります。
これらのプラグインを読み取る場合やインストールする場合は、
`remoteMarketplaceName` を `marketplacePath` の代わりに渡します。

## モデル

### モデルの一覧取得（`model/list`）

モデルまたはパーソナリティのセレクターを表示する前に、`model/list` を呼び出して、利用可能なモデルとその対応機能を確認します。

```json
{ "method": "model/list", "id": 6, "params": { "limit": 20, "includeHidden": false } }
{ "id": 6, "result": {
  "data": [{
    "id": "gpt-5.6-sol",
    "model": "gpt-5.6-sol",
    "displayName": "GPT-5.6-Sol",
    "hidden": false,
    "defaultReasoningEffort": "low",
    "supportedReasoningEfforts": [{
      "reasoningEffort": "low",
      "description": "Fast responses with lighter reasoning"
    }],
    "inputModalities": ["text", "image"],
    "supportsPersonality": true,
    "isDefault": true
  }],
  "nextCursor": null
} }

各モデルのエントリには、次の項目が含まれる場合があります。

- `supportedReasoningEfforts` - モデルがサポートする推論強度の選択肢
- `defaultReasoningEffort` - クライアント向けに推奨されるデフォルトの推論強度
- `upgrade` - クライアントで移行を促す際に使用する、推奨アップグレード先のモデル ID（省略可能）
- `upgradeInfo` - クライアントで移行を促す際に使用するアップグレードメタデータ（省略可能）
- `hidden` - デフォルトの選択リストでモデルが非表示になっているかどうか
- `inputModalities` - モデルがサポートする入力タイプ（例：`text`、`image`）
- `supportsPersonality` - モデルが `/personality` などのパーソナリティ固有の指示をサポートするかどうか
- `isDefault` - モデルがデフォルトとして推奨されているかどうか

デフォルトでは、`model/list` は選択リストに表示されるモデルだけを返します。一覧全体を取得し、`hidden` を使ってクライアント側でフィルタリングしたい場合は、`includeHidden: true` を設定します。

古いモデルカタログで `inputModalities` がない場合は、後方互換性を保つために `["text", "image"]` として扱います。

### 実験的機能の一覧取得（`experimentalFeature/list`）

このエンドポイントを使用して、機能フラグとそのメタデータ、ライフサイクルステージを確認します。

```json
{ "method": "experimentalFeature/list", "id": 7, "params": { "limit": 20 } }
{ "id": 7, "result": {
  "data": [{
    "name": "unified_exec",
    "stage": "beta",
    "displayName": "Unified exec",
    "description": "Use the unified PTY-backed execution tool.",
    "announcement": "Beta rollout for improved command execution reliability.",
    "enabled": false,
    "defaultEnabled": false
  }],
  "nextCursor": null
} }

`stage` の値は、`beta`、`underDevelopment`、`stable`、`deprecated`、`removed` のいずれかです。ベータ版以外のフラグでは、`displayName`、`description`、`announcement` が `null` の場合があります。

### 実行環境の確認（実験的）

構成済みのリモート環境で作業を始める前に、`environment/info` を使用してその環境を確認します。
このメソッドには `capabilities.experimentalApi = true` が必要です。

```json
{ "method": "environment/info", "id": 8, "params": { "environmentId": "devbox" } }
{ "id": 8, "result": {
  "shell": { "name": "zsh", "path": "/bin/zsh" },
  "cwd": "file:///workspace/project"
} }

`cwd` は `null` の場合があります。値がある場合は、その環境固有のパス構文を使用した
正規の `file:` URI です。不明な環境 ID や、接続またはプロトコルの障害に対しては、
リクエストエラーが返されます。

## スレッド

- `thread/read` は、保存済みのスレッドをサブスクライブせずに読み取ります。ターンを含めるには `includeTurns` を設定します。
- `thread/turns/list` は実験的なメソッドで、保存済みのスレッドを再開せずに、そのターン履歴をページ単位で取得します。
  `itemsView` を使用して、ターンの項目を省略するか、
  要約して読み込むか、完全に読み込むかを選択します。
- `thread/items/list` は実験的なメソッドで、永続化されたスレッドの項目をページ単位で取得します。必要に応じて、対象を 1 つのターンに限定できます。
- `thread/list` は、カーソルベースのページネーションに加え、`modelProviders`、`sourceKinds`、`archived`、`isPinned`、`cwd`、`useStateDbOnly`、`searchTerm`、および実験的な `parentThreadId` または `ancestorThreadId` によるフィルタリングをサポートします。
- `thread/loaded/list` は、現在メモリ内にあるスレッド ID を返します。
- `thread/archive` は、永続化されたスレッドの JSONL ログをアーカイブディレクトリに移動します。また、そこから生成された子孫スレッドのログのうち、まだアーカイブされていないものについてもアーカイブを試みます。
- `thread/delete` は、永続化されたアクティブまたはアーカイブ済みのスレッドと、そこから生成された子孫スレッドを完全に削除します。
- `thread/metadata/update` は、永続化された `gitInfo` と `isPinned` を含む、保存済みスレッドのメタデータを部分更新します。
- `thread/unsubscribe` は、読み込み済みスレッドに対する現在の接続のサブスクリプションを解除します。非アクティブ状態が猶予期間を超えて続くと、`thread/closed` が発行されることがあります。
- `thread/unarchive` は、アーカイブ済みのスレッドロールアウトをアクティブセッションのディレクトリに復元します。
- `thread/compact/start` はコンパクションを開始し、直ちに `{}` を返します。
- `thread/rollback` は非推奨です。直近の N ターンをメモリ内のコンテキストから削除し、スレッドの永続化された JSONL ログにロールバックマーカーを記録します。
- `thread/inject_items` は、読み込み済みスレッド内のモデルから参照できる履歴に、Responses API の項目をそのまま追加します。ユーザーターンは開始しません。

### スレッドの開始または再開

Codex で新しい会話を始める場合は、新規スレッドを開始します。

```json
{ "method": "thread/start", "id": 10, "params": {
  "model": "gpt-5.6-terra",
  "cwd": "/Users/me/project",
  "approvalPolicy": "never",
  "sandbox": "workspaceWrite",
  "personality": "friendly",
  "serviceName": "my_app_server_client"
} }
{ "id": 10, "result": {
  "thread": {
    "id": "thr_123",
    "sessionId": "thr_123",
    "preview": "",
    "ephemeral": false,
    "modelProvider": "openai",
    "createdAt": 1730910000
  }
} }
{ "method": "thread/started", "params": { "thread": { "id": "thr_123" } } }

`serviceName` は省略可能です。app-server でスレッド単位のメトリクスにインテグレーションのサービス名をタグ付けしたい場合に設定します。

`thread/start`、`thread/resume`、`thread/fork` は、
読み込み済みの指示ファイルのパスを格納した配列 `instructionSources` を返します。
各パスには、取得元の環境に固有の絶対パス構文が使用されます。
これはリモート環境にも当てはまります。

実験的なクライアントでは、`thread/start` の `historyMode` に `"legacy"`（デフォルト）
または `"paginated"` を設定できます。ページネーション対応スレッドの作成はまだサポートされておらず、
JSON-RPC エラー `-32601` が返されます。app-server は、
既存のページネーション対応レコードの一覧取得と要約の読み取りに対応しています。
ただし、履歴のページネーションがサポートされるまでは、履歴全体の読み取り、ターンのページネーション、再開は処理を続行せずエラーになります。

`capabilities.experimentalApi` を有効にしたベータ版クライアントは、
名前付き権限プロファイルの ID を `permissions` に渡し、従来の `sandbox` フィールドの代わりに使用できます。
`permissions` と `sandbox` を同時に送信しないでください。
`permissionProfile/list` をプロジェクトの `cwd` とともに使用すると、
利用可能なプロファイルと、管理対象の要件で各プロファイルが許可されるかどうかを確認できます。

`thread.sessionId` は、現在アクティブなセッションツリーのルートを識別します。
ルートスレッドは自身のスレッド ID をセッション ID として使用し、
フォークされたスレッドは元のルートのセッション ID を保持します。クライアントは、セッション ID をスレッド ID から導出せず、
`thread.sessionId` から読み取ってください。

保存済みセッションを続行するには、`thread/resume` を呼び出し、以前に記録した `thread.id` を渡します。レスポンス形式は `thread/start` と同じです。また、`thread/start` がサポートする `personality` などの構成オーバーライドも同様に渡せます。

```json
{ "method": "thread/resume", "id": 11, "params": {
  "threadId": "thr_123",
  "personality": "friendly"
} }
{ "id": 11, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false } } }

スレッドを再開しただけでは、`thread.updatedAt` もロールアウトファイルの更新日時も更新されません。タイムスタンプは、ターンを開始すると更新されます。

構成内で有効な MCP サーバーを `required` として指定し、そのサーバーの初期化に失敗した場合、`thread/start` と `thread/resume` は、そのサーバーなしで続行せずに失敗します。

`thread/start` の `dynamicTools` は試験的なフィールドです（`capabilities.experimentalApi = true` が必要です）。Codex はこれらの動的ツールをスレッドのロールアウトメタデータに永続化し、新しい動的ツールを指定しない場合は `thread/resume` で復元します。

ロールアウトに記録されたモデルとは異なるモデルで再開すると、Codex は警告を出し、次のターンで一度だけモデル切り替えの指示を適用します。

### スレッドの目標管理

`thread/goal/set`、`thread/goal/get`、`thread/goal/clear` を使用して、
TUI の `/goal` で表示されるものと同じ、永続化された目標の状態を管理します。

```json
{ "method": "thread/goal/set", "id": 13, "params": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000
} }
{ "id": 13, "result": { "goal": {
  "threadId": "thr_123",
  "objective": "Finish the migration and keep tests green",
  "status": "active",
  "tokenBudget": 40000,
  "tokensUsed": 0,
  "timeUsedSeconds": 0
} } }
{ "method": "thread/goal/updated", "params": {
  "threadId": "thr_123",
  "goal": {
    "threadId": "thr_123",
    "objective": "Finish the migration and keep tests green",
    "status": "active",
    "tokenBudget": 40000,
    "tokensUsed": 0,
    "timeUsedSeconds": 0
  }
} }

目標の内容は空にできず、4,000 文字以内である必要があります。
新しい内容を指定すると、目標が置き換えられ、使用量の集計がリセットされます。
終了状態にない現在の目標と同じ内容を指定するか、`objective` を省略すると、
使用履歴を保持したまま、状態またはトークン予算が更新されます。

保存済みセッションから分岐するには、`thread.id` を指定して `thread/fork` を呼び出します。これにより、新しいスレッド ID が作成され、そのスレッドの `thread/started` 通知が送出されます。
`lastTurnId` を指定すると、そのターンを含めてそこまでの履歴がコピーされ、
それ以降のターンは除外されます：

```json
{ "method": "thread/fork", "id": 12, "params": { "threadId": "thr_123", "lastTurnId": "turn_456" } }
{ "id": 12, "result": { "thread": { "id": "thr_456", "sessionId": "thr_123", "forkedFromId": "thr_123" } } }
{ "method": "thread/started", "params": { "thread": { "id": "thr_456" } } }

App-server は、進行中のターンを指す `lastTurnId` を拒否します。
分岐元のスレッドでターンが進行中にこのフィールドを省略すると、フォークには中断マーカーが記録され、
未完了のターンがマーカーなしで残ることはありません。

`ephemeral: true` を指定すると、保存済みスレッドの一覧に追加せずに、
メモリ内にフォークを作成できます：

```json
{
  "method": "thread/fork",
  "id": 13,
  "params": {
    "threadId": "thr_123",
    "ephemeral": true
  }
}
{
  "id": 13,
  "result": {
    "thread": {
      "id": "thr_789",
      "sessionId": "thr_789",
      "forkedFromId": "thr_123",
      "ephemeral": true
    }
  }
}

ページネーション対象のスレッドから一時的なフォークを作成する場合は、`excludeTurns: true` も必要です。
このフィールドは試験的なもので、`capabilities.experimentalApi = true` が必要です。

ユーザー向けのスレッドタイトルが設定されている場合、app-server は `thread/list`、`thread/read`、`thread/resume`、`thread/unarchive`、`thread/rollback` の各レスポンスの `thread.name` に値を設定します。後からタイトルが設定されるまで、`thread/start` と `thread/fork` では `name` が省略されるか、`null` が返される場合があります。

### 保存済みスレッドの読み取り（再開なし）

スレッドの再開やイベントの購読をせずに保存済みスレッドのデータを取得する場合は、`thread/read` を使用します。

- `includeTurns` - `true` の場合、レスポンスにはスレッドのターンが含まれます。`false` の場合や省略した場合は、スレッドの概要だけが返されます。
- 返される `thread` オブジェクトには、実行時の `status`（`notLoaded`、`idle`、`systemError`、または `activeFlags` を伴う `active`）が含まれます。

```json
{ "method": "thread/read", "id": 19, "params": { "threadId": "thr_123", "includeTurns": true } }
{ "id": 19, "result": { "thread": { "id": "thr_123", "name": "Bug bash notes", "ephemeral": false, "status": { "type": "notLoaded" }, "turns": [] } } }

`thread/resume` とは異なり、`thread/read` はスレッドをメモリにロードせず、`thread/started` も送出しません。

### スレッドのターン一覧

`thread/turns/list` は試験的な機能です。保存済みスレッドを再開せずに、そのターン履歴をページ単位で取得する場合に使用します。デフォルトでは結果が新しい順に並ぶため、クライアントは `nextCursor` を使って古いターンを取得できます。レスポンスには `backwardsCursor` も含まれます。これを `cursor` として `sortDirection: "asc"` とともに渡すと、前に取得したページの最初のアイテムより新しいターンを取得できます。

`itemsView` は、レスポンスに含めるターン内のアイテムデータの量を制御します：

- `notLoaded` ではアイテムが省略されます。
- `summary` ではアイテムの要約データが返されます。設定を省略した場合も、このデフォルト値が使用されます。
- `full` ではアイテムの完全なデータが返されます。

```json
{ "method": "thread/turns/list", "id": 20, "params": {
  "threadId": "thr_123",
  "limit": 50,
  "sortDirection": "desc",
  "itemsView": "summary"
} }
{ "id": 20, "result": {
  "data": [],
  "nextCursor": "older-turns-cursor-or-null",
  "backwardsCursor": "newer-turns-cursor-or-null"
} }

`thread/items/list` も試験的な機能です。
スレッドを再開せずに、永続化されたアイテムをページ単位で取得します。`turnId` を指定すると、結果は 1 つのターンに限定されます。
省略すると、スレッド全体のアイテムをページ単位で取得できます。
使用中のスレッドストアがアイテムのページネーションに対応している必要があります。対応していない場合、サーバーはメソッド非対応エラーを返します。

### スレッド一覧（ページネーションとフィルター）

`thread/list` を使って履歴 UI を表示できます。デフォルトでは、結果が `createdAt` の新しい順に並びます。フィルターはページネーションの前に適用されます。次の項目を任意に組み合わせて指定します：

- `cursor` - 前のレスポンスに含まれる不透明な文字列（最初のページでは省略）
- `limit` - 未設定の場合、サーバーは適切なページサイズをデフォルトで使用します。
- `sortKey` - `created_at`（デフォルト）、`updated_at`、または `recency_at`
- `sortDirection` - `desc`（デフォルト）または `asc`
- `modelProviders` - 結果を特定のプロバイダーに限定します。未設定の場合や null または空の配列を指定した場合は、すべてのプロバイダーが対象になります。
- `sourceKinds` - 結果を特定のスレッドソースに限定します。省略した場合や `[]` を指定した場合、サーバーはデフォルトで対話型ソースである `cli` と `vscode` だけを対象にします。
- `archived` - `true` の場合、アーカイブ済みスレッドのみを一覧表示します。`false` の場合や省略した場合は、アーカイブされていないスレッドを一覧表示します（デフォルト）。
- `isPinned` - 指定すると、永続化されたピン留め状態が一致するスレッドだけを返します。省略すると、ピン留め済みと未ピン留めの両方のスレッドを返します。
- `cwd` - セッションの現在の作業ディレクトリが、指定したパスまたは配列内のいずれかのパスと完全に一致するスレッドに結果を限定します。相対パスは、app-server プロセスの作業ディレクトリを基準に解決されます。
- `useStateDbOnly` - `true` の場合、メタデータを修復するための JSONL スレッドログのスキャンを行わず、状態データベースの結果を返します。省略するか `false` を指定すると、デフォルトのスキャンと修復が実行されます。
- `searchTerm` - 抽出されたタイトルに指定した部分文字列を含むスレッドに結果を限定します。大文字と小文字は区別されます。
- `parentThreadId` - 指定した親スレッドの直接の子スレッドに結果を限定します。このフィルターは試験的な機能であり、`capabilities.experimentalApi = true` が必要です。
- `ancestorThreadId` - 指定したスレッドから生成された子孫スレッドに、階層の深さを問わず結果を限定します。このフィルターは試験的な機能であり、`capabilities.experimentalApi = true` が必要です。`parentThreadId` とは組み合わせないでください。

`sourceKinds` には次の値を指定できます：

- `cli`
- `vscode`
- `exec`
- `appServer`
- `subAgent`
- `subAgentReview`
- `subAgentCompact`
- `subAgentThreadSpawn`
- `subAgentOther`
- `unknown`

例：

```json
{ "method": "thread/list", "id": 20, "params": {
  "cursor": null,
  "limit": 25,
  "sortKey": "created_at"
} }
{ "id": 20, "result": {
  "data": [
    { "id": "thr_a", "preview": "Create a TUI", "ephemeral": false, "isPinned": true, "modelProvider": "openai", "createdAt": 1730831111, "updatedAt": 1730831111, "name": "TUI prototype", "status": { "type": "notLoaded" } },
    { "id": "thr_b", "preview": "Fix tests", "ephemeral": false, "isPinned": false, "modelProvider": "openai", "createdAt": 1730750000, "updatedAt": 1730750000, "status": { "type": "notLoaded" } }
  ],
  "nextCursor": "opaque-token-or-null"
} }

`nextCursor` が `null` の場合は、最後のページに達しています。

### 保存済みスレッドのメタデータ更新

`thread/metadata/update` を使用すると、スレッドを再開せずに保存済みのスレッドメタデータを部分更新できます。
スレッドをピン留めしたりピン留めを解除したりするには `isPinned` を設定し、永続化された Git メタデータを変更するには `gitInfo` を更新します。
省略したフィールドは変更されません。
`null` を明示的に指定すると、保存済みの Git メタデータの値が消去されます。

```json
{ "method": "thread/metadata/update", "id": 21, "params": {
  "threadId": "thr_123",
  "isPinned": true,
  "gitInfo": { "branch": "feature/sidebar-pr" }
} }
{ "id": 21, "result": {
  "thread": {
    "id": "thr_123",
    "isPinned": true,
    "gitInfo": { "sha": null, "branch": "feature/sidebar-pr", "originUrl": null }
  }
} }

### スレッドの稼働状況の変化の追跡

ロード済みスレッドの実行時の稼働状況が変わるたびに、`thread/status/changed` が送出されます。ペイロードには `threadId` と新しい `status` が含まれます。

```json
{
  "method": "thread/status/changed",
  "params": {
    "threadId": "thr_123",
    "status": { "type": "active", "activeFlags": ["waitingOnApproval"] }
  }
}

### ロード済みスレッドの一覧

`thread/loaded/list` は、現在メモリにロードされているスレッド ID を返します。

```json
{ "method": "thread/loaded/list", "id": 21 }
{ "id": 21, "result": { "data": ["thr_123", "thr_456"] } }

### ロード済みスレッドの購読解除

`thread/unsubscribe` は、現在の接続によるスレッドの購読を解除します。レスポンスの状態は次のいずれかです：

- `unsubscribed`：接続がスレッドを購読しており、その購読が解除された場合
- `notSubscribed`：接続がそのスレッドを購読していなかった場合
- `notLoaded`：スレッドがロードされていない場合

これが最後の購読者だった場合、サーバーは、購読者がおらず、スレッドのアクティビティもない状態が 30 分間続くまで、スレッドをロードしたままにします。猶予期間が終了すると、app-server はスレッドをアンロードし、`notLoaded` への遷移を示す `thread/status/changed` 通知と `thread/closed` 通知を送出します。

```json
{ "method": "thread/unsubscribe", "id": 22, "params": { "threadId": "thr_123" } }
{ "id": 22, "result": { "status": "unsubscribed" } }

その後、スレッドが期限切れになった場合：

```json
{ "method": "thread/status/changed", "params": {
    "threadId": "thr_123",
    "status": { "type": "notLoaded" }
} }
{ "method": "thread/closed", "params": { "threadId": "thr_123" } }

### スレッドのアーカイブ

`thread/archive` を使用して、永続化されたスレッドログ（ディスク上に JSONL ファイルとして保存）をアーカイブ済みセッションのディレクトリに移動します。スレッドをアーカイブすると、そのスレッドから生成された子孫スレッドのうち、まだアーカイブされていないもののアーカイブも試みます。

```json
{ "method": "thread/archive", "id": 22, "params": { "threadId": "thr_b" } }
{ "id": 22, "result": {} }
{ "method": "thread/archived", "params": { "threadId": "thr_b" } }
{ "method": "thread/archived", "params": { "threadId": "thr_child" } }

`archived: true` を指定しない限り、アーカイブ済みスレッドは以降の `thread/list` 呼び出しの結果に表示されません。サーバーは、実際にアーカイブした各スレッドについて `thread/archived` 通知を 1 件送出します。生成された子孫スレッドをアーカイブできない場合でも、その子孫スレッドのアーカイブ通知を送出せずに、リクエストが成功することがあります。

### スレッドの削除

`thread/delete` を使用して、永続化されたアクティブまたはアーカイブ済みのスレッドと、そこから生成された子孫スレッドを完全に削除します。
サーバーは既存のロールアウトファイルと関連するメタデータを削除してから、成功を返します。
見つからないロールアウトファイルは、すでに削除されたものとして扱われます。
一時的なルートスレッドは削除できません。

```json
{ "method": "thread/delete", "id": 23, "params": { "threadId": "thr_b" } }
{ "id": 23, "result": {} }
{ "method": "thread/deleted", "params": { "threadId": "thr_b" } }
{ "method": "thread/deleted", "params": { "threadId": "thr_child" } }

### スレッドのアーカイブ解除

`thread/unarchive` を使用して、アーカイブ済みスレッドのロールアウトをアクティブなセッションのディレクトリに戻します。

```json
{ "method": "thread/unarchive", "id": 24, "params": { "threadId": "thr_b" } }
{ "id": 24, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes" } } }
{ "method": "thread/unarchived", "params": { "threadId": "thr_b" } }

### スレッドのコンパクション開始

`thread/compact/start` を使用して、スレッド履歴のコンパクションを手動で開始します。リクエストは直ちに `{}` を返します。

App-server は、進行状況を同じ `threadId` に対する標準の `turn/*` および `item/*` 通知として送出します。これには、`contextCompaction` アイテムのライフサイクル（`item/started`、続いて `item/completed`）も含まれます。

```json
{ "method": "thread/compact/start", "id": 25, "params": { "threadId": "thr_b" } }
{ "id": 25, "result": {} }

### スレッドのシェルコマンド実行

スレッドに関連付けられた、ユーザーが開始するシェルコマンドには `thread/shellCommand` を使用します。リクエストには即座に `{}` が返され、進行状況は標準の `turn/*` および `item/*` 通知を通じてストリーミングされます。

この API はサンドボックス外でフルアクセスで実行され、スレッドのサンドボックスポリシーを継承しません。クライアントでは、ユーザーが明示的に開始したコマンドに限って、この API を利用できるようにしてください。

スレッドにすでにアクティブなターンがある場合、コマンドはそのターンの補助アクションとして実行され、整形済みの出力がターンのメッセージストリームに挿入されます。スレッドがアイドル状態の場合、app-server はシェルコマンド用の独立したターンを開始します。

`timeoutMs` を設定すると、実行時間をミリ秒単位で制限できます。
省略するか `null` を渡すと、デフォルトの 1 時間が適用されます。`0` は即時タイムアウトを要求し、負の値は拒否されます。
タイムアウトの設定によって、即座に返される RPC の受領確認が遅れることはありません。

```json
{ "method": "thread/shellCommand", "id": 26, "params": { "threadId": "thr_b", "command": "git status --short", "timeoutMs": 10000 } }
{ "id": 26, "result": {} }

### バックグラウンド ターミナルのクリーンアップ

スレッドに関連付けられている実行中のバックグラウンド ターミナルをすべて停止するには、`thread/backgroundTerminals/clean` を使用します。このメソッドは試験運用版であり、`capabilities.experimentalApi = true` が必要です。

```json
{ "method": "thread/backgroundTerminals/clean", "id": 27, "params": { "threadId": "thr_b" } }
{ "id": 27, "result": {} }

`thread/backgroundTerminals/list` を使用すると、読み込み済みスレッドで実行中のバックグラウンド ターミナルを確認できます。
リクエストは標準の `cursor` と `limit` によるページネーションに対応しており、
返される `processId` は app-server のプロセス ID です。
このメソッドは試験運用版であり、`capabilities.experimentalApi = true` が必要です：

```json
{ "method": "thread/backgroundTerminals/list", "id": 28, "params": { "threadId": "thr_b" } }
{ "id": 28, "result": { "data": [
  {
    "itemId": "item_456",
    "processId": "42",
    "command": "python3 -m http.server",
    "cwd": "/workspace",
    "osPid": null,
    "cpuPercent": null,
    "rssKb": null
  }
], "nextCursor": null } }

`thread/backgroundTerminals/terminate` にその `processId` を指定すると、バックグラウンド ターミナルを 1 つ停止できます。
このメソッドは試験運用版であり、
`capabilities.experimentalApi = true` が必要です：

```json
{ "method": "thread/backgroundTerminals/terminate", "id": 29, "params": { "threadId": "thr_b", "processId": "42" } }
{ "id": 29, "result": { "terminated": true } }

### 直近のターンのロールバック

`thread/rollback` は非推奨であり、今後削除されます。
メモリ内のコンテキストから末尾の `numTurns` 件のエントリを削除し、
ロールアウトログにロールバックマーカーを永続化します。
返される `thread` の `turns` には、ロールバック後の内容が格納されます。

```json
{ "method": "thread/rollback", "id": 30, "params": { "threadId": "thr_b", "numTurns": 1 } }
{ "id": 30, "result": { "thread": { "id": "thr_b", "name": "Bug bash notes", "ephemeral": false } } }

## ターン

`input` フィールドはアイテムのリストを受け付けます：

- `{ "type": "text", "text": "Explain this diff" }`
- `{ "type": "image", "url": "https://.../design.png" }`
- `{ "type": "localImage", "path": "/tmp/screenshot.png" }`

ターンごとに設定（モデル、推論強度、パーソナリティ、`cwd`、サンドボックスポリシー、要約）を上書きできます。指定した設定は、同じスレッドの後続のターンでデフォルトとして使われます。`outputSchema` は現在のターンにのみ適用されます。`sandboxPolicy.type = "externalSandbox"` の場合は、`networkAccess` を `restricted` または `enabled` に設定します。一方、`workspaceWrite` では `networkAccess` は引き続きブール値です。

`turn/start.collaborationMode` では、`settings.developer_instructions: null` はモードの指示を消去するのではなく、「選択したモードの組み込み指示を使用する」ことを意味します。

### サンドボックスの読み取りアクセス（`ReadOnlyAccess`）

`sandboxPolicy` は明示的な読み取りアクセス制御に対応しています：

- `readOnly`：省略可能な `access`（デフォルトは `{ "type": "fullAccess" }`。アクセス可能なルートの限定も可能）
- `workspaceWrite`：省略可能な `readOnlyAccess`（デフォルトは `{ "type": "fullAccess" }`。アクセス可能なルートの限定も可能）

制限付き読み取りアクセスの形式：

```json
{
  "type": "restricted",
  "includePlatformDefaults": true,
  "readableRoots": ["/Users/me/shared-read-only"]
}

macOS では、`includePlatformDefaults: true` を指定すると、読み取り制限のあるセッションに、あらかじめ選定されたプラットフォーム既定の Seatbelt ポリシーが追加されます。これにより、`/System` 全体へのアクセスを一律に許可することなく、ツールの互換性が向上します。

例：

```json
{ "type": "readOnly", "access": { "type": "fullAccess" } }

```json
{
  "type": "workspaceWrite",
  "writableRoots": ["/Users/me/project"],
  "readOnlyAccess": {
    "type": "restricted",
    "includePlatformDefaults": true,
    "readableRoots": ["/Users/me/shared-read-only"]
  },
  "networkAccess": false
}

### ターンの開始

```json
{ "method": "turn/start", "id": 30, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Run tests" } ],
  "cwd": "/Users/me/project",
  "approvalPolicy": "unlessTrusted",
  "sandboxPolicy": {
    "type": "workspaceWrite",
    "writableRoots": ["/Users/me/project"],
    "networkAccess": true
  },
  "model": "gpt-5.6-terra",
  "effort": "medium",
  "summary": "concise",
  "personality": "friendly",
  "outputSchema": {
    "type": "object",
    "properties": { "answer": { "type": "string" } },
    "required": ["answer"],
    "additionalProperties": false
  }
} }
{ "id": 30, "result": { "turn": { "id": "turn_456", "status": "inProgress", "items": [], "error": null } } }

クライアントが実行したツールの出力でターンを開始するには、`toolOutput` を渡します。
空でない `name`、省略可能な `namespace`、文字列またはコンテンツアイテムの配列を値とする `output` を指定してください。
`input` は空の配列に設定します。
`toolOutput` と空でないユーザー入力は組み合わせられません。

```json
{
  "method": "turn/start",
  "id": 31,
  "params": {
    "threadId": "thr_123",
    "input": [],
    "toolOutput": {
      "name": "run_tests",
      "namespace": null,
      "output": "All 42 tests passed."
    }
  }
}

この出力は会話内でもツール出力として扱われ、
通知や永続化された履歴では `functionCallOutput` アイテムとして表示されます。
通常のターンがすでにアクティブな場合、Codex はそのターンのキューに出力を追加します。

### スレッドへのアイテムの挿入

`thread/inject_items` を使用すると、ユーザーターンを開始せずに、事前に作成した Responses API のアイテムを読み込み済みスレッドのプロンプト履歴に追加できます。これらのアイテムはロールアウトに永続化され、以降のモデルリクエストに含まれます。

```json
{ "method": "thread/inject_items", "id": 31, "params": {
  "threadId": "thr_123",
  "items": [
    {
      "type": "message",
      "role": "assistant",
      "content": [{ "type": "output_text", "text": "Previously computed context." }]
    }
  ]
} }
{ "id": 31, "result": {} }

### 進行中のターンへの追加指示

現在進行中のターンにユーザー入力を追加するには、`turn/steer` を使用します。

- `expectedTurnId` を含めてください。値はアクティブなターンの ID と一致している必要があります。
- スレッドにアクティブなターンがない場合、リクエストは失敗します。
- `turn/steer` は新しい `turn/started` 通知を送信しません。
- `turn/steer` は、ターン単位の上書き設定（`model`、`cwd`、`sandboxPolicy`、`outputSchema`）を受け付けません。

```json
{ "method": "turn/steer", "id": 32, "params": {
  "threadId": "thr_123",
  "input": [ { "type": "text", "text": "Actually focus on failing tests first." } ],
  "expectedTurnId": "turn_456"
} }
{ "id": 32, "result": { "turnId": "turn_456" } }

### ターンの開始（スキルの呼び出し）

テキスト入力に `$<skill-name>` を含め、併せて `skill` 入力アイテムを追加すると、スキルを明示的に呼び出せます。

```json
{ "method": "turn/start", "id": 33, "params": {
  "threadId": "thr_123",
  "input": [
    { "type": "text", "text": "$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage." },
    { "type": "skill", "name": "skill-creator", "path": "/Users/me/.codex/skills/skill-creator/SKILL.md" }
  ]
} }
{ "id": 33, "result": { "turn": { "id": "turn_457", "status": "inProgress", "items": [], "error": null } } }

### ターンの中断

```json
{ "method": "turn/interrupt", "id": 31, "params": { "threadId": "thr_123", "turnId": "turn_456" } }
{ "id": 31, "result": {} }

成功すると、ターンは `status: "interrupted"` で終了します。

## レビュー

`review/start` はスレッドに対して Codex のレビュアーを実行し、レビューアイテムをストリーミングします。レビュー対象には次のものが含まれます：

- `uncommittedChanges`
- `baseBranch`（ブランチとの差分）
- `commit`（特定のコミットのレビュー）
- `custom`（自由形式の指示）

既存のスレッドでレビューを実行するには `delivery: "inline"`（デフォルト）を使用し、新しいレビュースレッドをフォークするには `delivery: "detached"` を使用します。

リクエストとレスポンスの例：

```json
{ "method": "review/start", "id": 40, "params": {
  "threadId": "thr_123",
  "delivery": "inline",
  "target": { "type": "commit", "sha": "1234567deadbeef", "title": "Polish tui colors" }
} }
{ "id": 40, "result": {
  "turn": {
    "id": "turn_900",
    "status": "inProgress",
    "items": [
      { "type": "userMessage", "id": "turn_900", "content": [ { "type": "text", "text": "Review commit 1234567: Polish tui colors" } ] }
    ],
    "error": null
  },
  "reviewThreadId": "thr_123"
} }

別スレッドでレビューを実行するには `"delivery": "detached"` を使用します。レスポンスの形式は同じですが、`reviewThreadId` は新しいレビュースレッドの ID になります（元の `threadId` とは異なります）。また、サーバーはレビューターンのストリーミングを開始する前に、その新しいスレッドについて `thread/started` 通知を送信します。

Codex は通常の `turn/started` 通知に続けて、`enteredReviewMode` アイテムを含む `item/started` をストリーミングします：

```json
{
  "method": "item/started",
  "params": {
    "item": {
      "type": "enteredReviewMode",
      "id": "turn_900",
      "review": "current changes"
    }
  }
}

レビュアーの処理が完了すると、サーバーは最終レビューのテキストを持つ `exitedReviewMode` アイテムを含んだ `item/started` と `item/completed` を送信します：

```json
{
  "method": "item/completed",
  "params": {
    "item": {
      "type": "exitedReviewMode",
      "id": "turn_900",
      "review": "Looks solid overall..."
    }
  }
}

この通知を使用して、クライアントにレビュアーの出力を表示します。

## プロセスの実行

`process/*` は、明示的にプロセスを制御する試験運用版の API です。
使用には `capabilities.experimentalApi = true` が必要で、Codex のサンドボックス外で実行されます。
クライアントでローカルプロセスの制御を意図的にサンドボックスなしで提供する場合に限り、
使用してください。

`process/spawn` でプロセスを開始し、`processHandle` を指定します。
そのハンドルを標準入力、サイズ変更、終了のリクエストに使用します。
出力は `process/outputDelta` 通知を通じてストリーミングされ、
完了情報は `process/exited` を通じてストリーミングされます。

```json
{ "method": "process/spawn", "id": 48, "params": {
  "command": ["python3", "-m", "pytest", "-q"],
  "processHandle": "pytest-1",
  "cwd": "/Users/me/project",
  "tty": true
} }
{ "id": 48, "result": {} }
{ "method": "process/outputDelta", "params": {
  "processHandle": "pytest-1",
  "stream": "stdout",
  "deltaBase64": "Li4u"
} }
{ "method": "process/exited", "params": {
  "processHandle": "pytest-1",
  "exitCode": 0
} }

`process/writeStdin` に `deltaBase64`、`closeStdin`、またはその両方を指定して、入力を送信します。
PTY のサイズ変更イベントには `process/resizePty` を使用し、
実行中のプロセスを終了するには `process/kill` を使用します。

## コマンドの実行

`command/exec` は、スレッドを作成せずに、サーバーのサンドボックス内で単一のコマンド（`argv` 配列）を実行します。

```json
{ "method": "command/exec", "id": 50, "params": {
  "command": ["ls", "-la"],
  "cwd": "/Users/me/project",
  "sandboxPolicy": { "type": "workspaceWrite" },
  "timeoutMs": 10000
} }
{ "id": 50, "result": { "exitCode": 0, "stdout": "...", "stderr": "" } }

サーバープロセスをすでにサンドボックス化しており、Codex 側でのサンドボックス適用を省略する場合は、`sandboxPolicy.type = "externalSandbox"` を使用します。外部サンドボックスモードでは、`networkAccess` を `restricted`（デフォルト）または `enabled` に設定します。`readOnly` と `workspaceWrite` には、上記と同じ省略可能な `access` / `readOnlyAccess` 構造を使用します。

注意事項：

- サーバーは空の `command` 配列を拒否します。
- `sandboxPolicy` は、`turn/start` と同じ形式を受け付けます（例：`dangerFullAccess`、`readOnly`、`workspaceWrite`、`externalSandbox`）。
- `timeoutMs` を省略した場合は、サーバーのデフォルト値が使用されます。
- PTY を使用するセッションには `tty: true` を設定します。後で `command/exec/write`、`command/exec/resize`、または `command/exec/terminate` を呼び出す予定がある場合は、`processId` を使用します。
- `streamStdoutStderr: true` を設定すると、コマンドの実行中に `command/exec/outputDelta` 通知を受信できます。

### 管理者要件の読み取り（`configRequirements/read`）

`requirements.toml`、MDM、またはその両方から読み込まれた管理者要件の適用内容を確認するには、`configRequirements/read` を使用します。

```json
{ "method": "configRequirements/read", "id": 52, "params": {} }
{ "id": 52, "result": {
  "requirements": {
    "allowedApprovalPolicies": ["onRequest", "unlessTrusted"],
    "allowedSandboxModes": ["readOnly", "workspaceWrite"],
    "featureRequirements": {
      "personality": true,
      "unified_exec": false
    },
    "network": {
      "enabled": true,
      "allowedDomains": ["api.openai.com"],
      "allowUnixSockets": ["/tmp/example.sock"],
      "dangerouslyAllowAllUnixSockets": false
    }
  }
} }

要件が設定されていない場合、`result.requirements` は `null` です。サポートされるキーと値について詳しくは、[`requirements.toml`](/ja-JP/codex/config-file/config-reference#requirementstoml) のドキュメントを参照してください。

### Windows サンドボックスのセットアップ（`windowsSandbox/setupStart`）

独自の Windows クライアントでは、起動時のチェックで処理をブロックせずに、サンドボックスのセットアップを非同期で開始できます。

```json
{ "method": "windowsSandbox/setupStart", "id": 53, "params": { "mode": "elevated" } }
{ "id": 53, "result": { "started": true } }

App Server はバックグラウンドでセットアップを開始し、後で完了通知を送信します。

```json
{
  "method": "windowsSandbox/setupCompleted",
  "params": { "mode": "elevated", "success": true, "error": null }
}

モード：

- `elevated` - 管理者権限で Windows サンドボックスのセットアップ処理を実行します。
- `unelevated` - 従来のセットアップおよび事前チェック処理を実行します。

## ファイルシステム

v2 のファイルシステム API は絶対パスを対象に動作します。ファイルまたはディレクトリの変更後にクライアントで UI の状態を無効化する必要がある場合は、`fs/watch` を使用します。

```json
{ "method": "fs/watch", "id": 54, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "path": "/Users/me/project/.git/HEAD"
} }
{ "id": 54, "result": { "path": "/Users/me/project/.git/HEAD" } }
{ "method": "fs/changed", "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1",
  "changedPaths": ["/Users/me/project/.git/HEAD"]
} }
{ "method": "fs/unwatch", "id": 55, "params": {
  "watchId": "0195ec6b-1d6f-7c2e-8c7a-56f2c4a8b9d1"
} }
{ "id": 55, "result": {} }

ファイルを監視すると、置換や名前変更操作による更新も含め、そのファイルパスに対して `fs/changed` が送信されます。

## イベント

イベント通知は、スレッドとターンのライフサイクル、およびそれらに含まれるアイテムに関する情報を、サーバー側から配信するストリームです。スレッドを開始または再開したら、アクティブなトランスポートストリームから `thread/started`、`thread/archived`、`thread/unarchived`、`thread/closed`、`thread/status/changed`、`turn/*`、`item/*`、`serverRequest/resolved` の通知を読み取り続けます。

### 通知のオプトアウト

クライアントは、`initialize.params.capabilities.optOutNotificationMethods` に正確なメソッド名を指定して送信することで、接続ごとに特定の通知を抑制できます。

- 完全一致でのみ照合します。`item/agentMessage/delta` を指定すると、そのメソッドの通知だけが抑制されます。
- 不明なメソッド名は無視されます。
- 現行の `thread/*`、`turn/*`、`item/*`、および関連する v2 通知に適用されます。
- リクエスト、レスポンス、エラーには適用されません。

### ファイルのあいまい検索イベント（試験的）

ファイルのあいまい検索のセッション API は、クエリごとに次の通知を送信します。

- `fuzzyFileSearch/sessionUpdated` - アクティブなクエリに対する現時点の一致結果を含む `{ sessionId, query, files }`
- `fuzzyFileSearch/sessionCompleted` - そのクエリのインデックス作成と照合が完了すると送信される `{ sessionId }`

### 警告イベント

- `configWarning` - 構成や初期化に関する復旧可能な問題が発生した場合に送信される
  `{ summary, details?, path?, range? }`
- `warning` - 致命的ではない実行時の警告を通知する `{ threadId?, message }`

### Windows サンドボックスのセットアップイベント

- `windowsSandbox/setupCompleted` - `windowsSandbox/setupStart` リクエストの完了後に送信される `{ mode, success, error }`

### ターンイベント

- `turn/started` - ターン ID、空の `items`、`status: "inProgress"` を含む `{ turn }`
- `turn/completed` - `{ turn }` の `turn.status` は、`completed`、`interrupted`、`failed` のいずれかです。失敗時には `{ error: { message, codexErrorInfo?, additionalDetails? } }` が含まれます。
- `turn/diff/updated` - ターン内のすべてのファイル変更を集約した最新の unified 形式の差分を含む `{ threadId, turnId, diff }`
- `turn/plan/updated` - エージェントがプランを共有または変更するたびに、`{ turnId, explanation?, plan }` が送信されます。`plan` の各エントリは `{ step, status }` で、`status` は `pending`、`inProgress`、`completed` のいずれかです。
- `hook/started` と `hook/completed` - 同期ライフサイクルフックの開始時と、最終的な実行サマリーが利用可能になったときに、それぞれ `{ threadId, turnId?, run }` が送信されます。非同期フックでは、これらの通知は送信されません。
- `model/safetyBuffering/updated` - 安全性のために応答の一時的なバッファリングが始まると送信される `{ threadId, turnId, model, useCases, reasons, showBufferingUi, fasterModel }`
- `model/rerouted` - サービスがリクエストを別のモデルへルーティングすると送信される `{ threadId, turnId, fromModel, toModel, reason }`
- `model/verification` - サービスで追加のアカウント確認が必要になると送信される `{ threadId, turnId, verifications }`
- `thread/tokenUsage/updated` - アクティブなスレッドの使用量の更新

`turn/diff/updated` と `turn/plan/updated` には現在、アイテムイベントがストリーミングされている場合でも空の `items` 配列が含まれます。ターンのアイテムについては、`item/*` 通知を正として扱ってください。

### アイテム

`ThreadItem` は、ターンのレスポンスと `item/*` 通知に含まれるタグ付きユニオンです。一般的なアイテム型は次のとおりです。

- `userMessage` - `content` がユーザー入力（`text`、`image`、または `localImage`）のリストになっている `{id, content}`
- `functionCallOutput` - `{id, name, namespace, output}` は、`turn/start.toolOutput` を通じて渡される単独のツール出力を表します。`namespace` は `null` の場合があります。
- `agentMessage` - `{id, text, phase?}` には、それまでに蓄積されたエージェントの応答が含まれます。`phase` が含まれる場合は、Responses API の通信形式で使用される値（`commentary`、`final_answer`）が設定されます。
- `plan` - `{id, text}` には、プランモードで提案されたプランのテキストが含まれます。`item/completed` で受け取る最終的な `plan` アイテムを正として扱ってください。
- `reasoning` - `summary` にストリーミングされた推論の要約を、`content` に未加工の推論ブロックを格納する `{id, summary, content}`
- `commandExecution` - `{id, command, cwd, status, commandActions, aggregatedOutput?, exitCode?, durationMs?}`
- `fileChange` - `{id, changes, status}` は提案された編集内容を表します。`changes` は `{path, kind, diff}` のリストです。
- `mcpToolCall` - `{id, server, tool, status, arguments, appContext?, pluginId?, result?, error?}`。信頼済みの MCP アプリでは、`appContext` に `connectorId`、`linkId`、`resourceUri`、`appName`、`templateId`、およびコネクタの安定したアクション名を示す `actionName` を含めることができます。古い永続化済みアイテムでは、新しいメタデータが省略されている場合があります。非推奨のトップレベルの `mcpAppResourceUri` ではなく、`appContext.resourceUri` を使用してください。
- `dynamicToolCall` - クライアント側で実行される動的ツール呼び出しを表す `{id, tool, arguments, status, contentItems?, success?, durationMs?}`
- `collabToolCall` - `{id, tool, status, senderThreadId, receiverThreadId?, newThreadId?, prompt?, agentStatus?}`
- `webSearch` - エージェントが発行したウェブ検索リクエストを表す `{id, query, action?}`
- `imageView` - エージェントが画像ビューアーツールを呼び出したときに送信される `{id, path}`
- `enteredReviewMode` - レビュアーの開始時に送信される `{id, review}`
- `exitedReviewMode` - レビュアーの完了時に送信される `{id, review}`
- `contextCompaction` - Codex が会話履歴のコンパクションを実行したときに送信される `{id}`

`webSearch.action` では、アクションの `type` は `search`（`query?`、`queries?`）、`openPage`（`url?`）、または `findInPage`（`url?`、`pattern?`）のいずれかです。

App Server では、従来の `thread/compacted` 通知は非推奨です。代わりに `contextCompaction` アイテムを使用してください。

すべてのアイテムは、次の 2 つの共通ライフサイクルイベントを送信します。

- `item/started` - 新しい作業単位の処理が始まると、完全な `item` が送信されます。`item.id` は、デルタで使用される `itemId` と一致します。
- `item/completed` - 作業が完了すると、最終的な `item` が送信されます。これを確定した状態として扱ってください。

### アイテムのデルタ

- `item/agentMessage/delta` - ストリーミングされたテキストをエージェントメッセージに追加します。
- `item/plan/delta` - 提案されたプランのテキストをストリーミングします。最終的な `plan` アイテムは、連結したデルタと完全には一致しない場合があります。
- `item/reasoning/summaryTextDelta` - 人が読める推論の要約をストリーミングします。新しい要約セクションが始まると、`summaryIndex` が増加します。
- `item/reasoning/summaryPartAdded` - 推論の要約セクション間の境界を示します。
- `item/reasoning/textDelta` - モデルが対応している場合に、未加工の推論テキストをストリーミングします。
- `item/commandExecution/outputDelta` - コマンドの stdout/stderr をストリーミングします。デルタを順番に追加してください。
- `item/fileChange/outputDelta` - 従来の `apply_patch` テキスト出力との互換性を保つための、非推奨の通知です。現在の app-server はこの通知を発行しません。代わりに `fileChange` 項目と `turn/diff/updated` を使用してください。

## エラー

ターンが失敗すると、サーバーは `{ error: { message, codexErrorInfo?, additionalDetails? } }` を含む `error` イベントを発行し、その後 `status: "failed"` でターンを終了します。アップストリームの HTTP ステータスが得られる場合は、`codexErrorInfo.httpStatusCode` に格納されます。

`codexErrorInfo` の主な値は次のとおりです：

- `ContextWindowExceeded`
- `UsageLimitExceeded`
- `HttpConnectionFailed`（アップストリームの 4xx/5xx エラー）
- `ResponseStreamConnectionFailed`
- `ResponseStreamDisconnected`
- `ResponseTooManyFailedAttempts`
- `BadRequest`、`Unauthorized`、`SandboxError`、`InternalServerError`、`Other`

アップストリームの HTTP ステータスが得られる場合、サーバーは該当する `codexErrorInfo` バリアントの `httpStatusCode` にその値を含めて転送します。

## 承認

ユーザーの Codex 設定によっては、コマンドの実行やファイルの変更に承認が必要になる場合があります。app-server はサーバー起点の JSON-RPC リクエストをクライアントに送信し、クライアントは判断結果を含むペイロードで応答します。

- コマンド実行に対する判断：`accept`、`acceptForSession`、`decline`、`cancel`、または `{ "acceptWithExecpolicyAmendment": { "execpolicy_amendment": ["cmd", "..."] } }`
- ファイル変更に対する判断：`accept`、`acceptForSession`、`decline`、`cancel`

- リクエストには `threadId` と `turnId` が含まれます。これらを使用して、UI の状態をアクティブな会話の範囲で管理してください。
- サーバーは作業を再開するか拒否し、`item/completed` で項目を終了します。

### コマンド実行の承認

メッセージの順序：

1. `item/started` は、`command`、`cwd` などのフィールドを持つ、保留中の `commandExecution` 項目を示します。
2. `item/commandExecution/requestApproval` には `itemId`、`threadId`、`turnId` に加え、省略可能な `reason`、`command`、`cwd`、`commandActions`、`proposedExecpolicyAmendment`、`networkApprovalContext`、`availableDecisions` が含まれます。`initialize.params.capabilities.experimentalApi = true` の場合、ペイロードには、コマンドごとに要求されたサンドボックス内のアクセス権を示す試験的な `additionalPermissions` も含まれることがあります。`additionalPermissions` 内のファイルシステムパスは、通信時にはすべて絶対パスです。
3. クライアントは、上記のコマンド実行に対する承認判断のいずれかで応答します。
4. `serverRequest/resolved` は、保留中のリクエストに応答があったか、そのリクエストがクリアされたことを示します。
5. `item/completed` は、`status: completed | failed | declined` を含む最終的な `commandExecution` 項目を返します。

`networkApprovalContext` が存在する場合、このプロンプトは管理対象のネットワークアクセスに対するものであり、一般的なシェルコマンドの承認ではありません。現在の v2 スキーマでは、接続先の `host` と `protocol` が提供されます。クライアントはネットワークアクセス専用のプロンプトを表示し、`command` がユーザーにとって意味のあるシェルコマンドのプレビューになっていることを前提としないでください。

Codex は、同時に発生するネットワーク承認プロンプトを接続先（`host`、プロトコル、ポート）ごとにまとめます。そのため、app-server は、同じ接続先への複数の待機中リクエストを処理可能にするプロンプトを 1 つだけ送信することがあります。同じホストでもポートが異なる場合は別々に扱われます。

### ファイル変更の承認

メッセージの順序：

1. `item/started` は、提案された変更内容を示す `changes` と `status: "inProgress"` を含む `fileChange` 項目を発行します。
2. `item/fileChange/requestApproval` には、`itemId`、`threadId`、`turnId` と、省略可能な `reason` および `grantRoot` が含まれます。
3. クライアントは、上記のファイル変更に対する承認判断のいずれかで応答します。
4. `serverRequest/resolved` は、保留中のリクエストに応答があったか、そのリクエストがクリアされたことを示します。
5. `item/completed` は、`status: completed | failed | declined` を含む最終的な `fileChange` 項目を返します。

### `tool/requestUserInput`

クライアントが `item/tool/requestUserInput` に応答すると、app-server は `{ threadId, requestId }` を含む `serverRequest/resolved` を発行します。クライアントが応答する前に、ターンの開始、完了、または中断によって保留中のリクエストがクリアされた場合も、サーバーはその処理について同じ通知を発行します。

リクエストパラメーターには `autoResolutionMs` が含まれ、その値はミリ秒単位のタイムアウトを表す整数または
`null` です。
値が設定されている場合、ユーザーが応答しなければ、ホストクライアントは指定された時間の経過後にプロンプトを自動的に解決できます。

### 権限リクエスト

組み込みの `request_permissions` ツールは、
`item/permissions/requestApproval` を送信します。このリクエストには `threadId`、`turnId`、`itemId`、
`environmentId`、`cwd`、省略可能な `reason` と、要求されたネットワークまたはファイルシステムの権限が含まれます。
要求された権限のうち、付与したものだけを含む `permissions` で応答してください。
`scope` を `"session"` に設定すると、同じセッション内の後続ターンでも付与された権限が維持されます。
省略するか `"turn"` を使用すると、権限はそのターンだけに付与されます。
要求されていない権限は無視されます。

### MCP サーバーの誘発リクエスト

MCP サーバーは `mcpServer/elicitation/request` を使用してターンを中断できます。
リクエストには `threadId`、省略可能な `turnId`、`serverName` と、
次のいずれかのリクエスト形式が含まれます：

- `mode: "form"` または `mode: "openai/form"`：`message` と
`requestedSchema` を含む
- `mode: "url"`：`message`、`url`、`elicitationId` を含む

`action: "accept"` と要求された `content` で応答するか、
`action: "decline"` または `"cancel"` のいずれかと `content: null` で応答してください。その後、app-server は
`serverRequest/resolved` を発行します。`openai/form` バリアントを受信するには、
`initialize.params.capabilities.mcpServerOpenaiFormElicitation` でオプトインしてください。

### 動的ツール呼び出し（試験的）

`thread/start` の `dynamicTools` と、それに対応する `item/tool/call` のリクエストまたはレスポンスのフローは、試験的な API です。

動的ツール名と名前空間名は、Responses API の命名上の制約に従う必要があります。
Codex の組み込みツールで使われる予約済みの名前空間名は使用しないでください。

ターン中に動的ツールが呼び出されると、app-server は次を発行します：

1. `item/started`：`item.type = "dynamicToolCall"`、`status = "inProgress"` に加えて `tool` と `arguments` を含む
2. `item/tool/call`：サーバーからクライアントへのリクエスト
3. 返されたコンテンツ項目を含むクライアントのレスポンスペイロード
4. `item/completed`：`item.type = "dynamicToolCall"`、最終的な `status`、返された `contentItems` または `success` の値を含む

### MCP ツール呼び出しの承認（アプリ）

App（コネクタ）のツール呼び出しにも承認が必要になる場合があります。アプリのツール呼び出しに副作用がある場合、サーバーは `tool/requestUserInput` で **承認**、 **拒否**、 **キャンセル**などの選択肢を提示し、承認を求めることがあります。破壊的な操作を示すツールアノテーションがあると、ツールがより低い権限を示すヒントも提示している場合でも、必ず承認が求められます。ユーザーが拒否またはキャンセルすると、関連する `mcpToolCall` 項目はツールを実行せず、エラーで完了します。

## スキル

ユーザーのテキスト入力に `$<skill-name>` を含めて、スキルを呼び出します。モデルによる名前の解決に頼らず、サーバーがスキルの指示をすべて挿入できるよう、`skill` 入力項目を追加することを推奨します。

```json
{
  "method": "turn/start",
  "id": 101,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$skill-creator Add a new skill for triaging flaky CI."
      },
      {
        "type": "skill",
        "name": "skill-creator",
        "path": "/Users/me/.codex/skills/skill-creator/SKILL.md"
      }
    ]
  }
}

`skill` 項目を省略しても、モデルは `$<skill-name>` マーカーを解析してスキルを見つけようとしますが、遅延が増える可能性があります。

例：

$skill-creator Add a new skill for triaging flaky CI and include step-by-step usage.

`skills/list` を使用して利用可能なスキルを取得します。必要に応じて `cwds` で範囲を限定し、`forceReload` を指定できます。また、`perCwdExtraUserRoots` を含めると、特定の `cwd` 値に対して、追加の絶対パスを `user` スコープとしてスキャンできます。app-server は、`cwd` が `cwds` に含まれていないエントリを無視します。`skills/list` は `cwd` ごとにキャッシュされた結果を再利用する場合があります。ディスクから再読み込みするには、`forceReload: true` を設定してください。サーバーは、`interface` と `dependencies` が存在する場合、`SKILL.json` から読み取ります。

```json
{ "method": "skills/list", "id": 25, "params": {
  "cwds": ["/Users/me/project", "/Users/me/other-project"],
  "forceReload": true,
  "perCwdExtraUserRoots": [
    {
      "cwd": "/Users/me/project",
      "extraUserRoots": ["/Users/me/shared-skills"]
    }
  ]
} }
{ "id": 25, "result": {
  "data": [{
    "cwd": "/Users/me/project",
    "skills": [
      {
        "name": "skill-creator",
        "description": "Create or update a Codex skill",
        "enabled": true,
        "interface": {
          "displayName": "Skill Creator",
          "shortDescription": "Create or update a Codex skill"
        },
        "dependencies": {
          "tools": [
            {
              "type": "env_var",
              "value": "GITHUB_TOKEN",
              "description": "GitHub API token"
            },
            {
              "type": "mcp",
              "value": "github",
              "transport": "streamable_http",
              "url": "https://example.com/mcp"
            }
          ]
        }
      }
    ],
    "errors": []
  }]
} }

監視対象のローカルスキルファイルが変更されると、サーバーは `skills/changed` 通知も発行します。これを無効化のシグナルとして扱い、必要に応じて現在のパラメーターで `skills/list` を再実行してください。

パスを指定してスキルを有効または無効にするには：

```json
{
  "method": "skills/config/write",
  "id": 26,
  "params": {
    "path": "/Users/me/.codex/skills/skill-creator/SKILL.md",
    "enabled": false
  }
}

## アプリ（コネクタ）

`app/installed` を使用して、インストール済みアプリの最新のコミット済みランタイムスナップショットを読み取ります。
各結果には、アプリの `id`、`runtimeName`（または `null`）、
実効的な `enabled` の状態と `callable` の状態が含まれます。
アプリを呼び出せるのは、実効構成でアプリが有効化され、
モデルから参照できるツールの少なくとも 1 つが、アプリとツールのポリシーに準拠している場合だけです。

```json
{
  "method": "app/installed",
  "id": 49,
  "params": {
    "threadId": "thread-1",
    "forceRefresh": false
  }
}
{
  "id": 49,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "runtimeName": "Demo App",
        "enabled": true,
        "callable": true
      }
    ]
  }
}

`threadId` を省略すると、読み込み済みスレッドの構成ではなくグローバル構成が使用されます。
`forceRefresh: true` を設定すると、読み取り前にコネクタのランタイムスナップショットが更新されます。
グローバルポリシーまたはワークスペースポリシーによってアプリへのアクセスがブロックされている場合でも、
検出されたアプリが `enabled` と `callable` を `false` に設定した状態で表示されることがあります。

`app/list` を使用して利用可能なアプリを取得します。CLI/TUI では、`/apps` がユーザー向けの選択画面です。カスタムクライアントでは、`app/list` を直接呼び出します。各エントリには `isAccessible`（ユーザーが利用可能かどうか）と `isEnabled`（`config.toml` で有効かどうか）の両方が含まれるため、クライアントはインストールやアクセスの状態と、ローカルでの有効化状態を区別できます。アプリのエントリには、省略可能な `branding`、`appMetadata`、`labels` フィールドが含まれる場合もあります。

```json
{ "method": "app/list", "id": 50, "params": {
  "cursor": null,
  "limit": 50,
  "threadId": "thread-1",
  "forceRefetch": false
} }
{ "id": 50, "result": {
  "data": [
    {
      "id": "demo-app",
      "name": "Demo App",
      "description": "Example connector for documentation.",
      "logoUrl": "https://example.com/demo-app.png",
      "logoUrlDark": null,
      "distributionChannel": null,
      "branding": null,
      "appMetadata": null,
      "labels": null,
      "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
      "isAccessible": true,
      "isEnabled": true
    }
  ],
  "nextCursor": null
} }

`threadId` を指定すると、アプリ機能の利用制御（`features.apps`）には、そのスレッドの構成スナップショットが使用されます。省略した場合、app-server は最新のグローバル構成を使用します。

`app/list` は、アクセス可能なアプリとディレクトリ内のアプリの両方の読み込みが完了してから結果を返します。`forceRefetch: true` を設定すると、アプリのキャッシュを使用せずに最新データを取得できます。キャッシュエントリは、更新が成功した場合にのみ置き換えられます。

アクセス可能なアプリとディレクトリ内のアプリのどちらかの読み込みが完了するたびに、サーバーは `app/list/updated` 通知も発行します。各通知には、統合された最新のアプリ一覧が含まれます。

```json
{
  "method": "app/list/updated",
  "params": {
    "data": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "logoUrl": "https://example.com/demo-app.png",
        "logoUrlDark": null,
        "distributionChannel": null,
        "branding": null,
        "appMetadata": null,
        "labels": null,
        "installUrl": "https://chatgpt.com/apps/demo-app/demo-app",
        "isAccessible": true,
        "isEnabled": true
      }
    ]
  }
}

アプリ ID がすでにわかっており、インストール済みアプリのランタイム状態ではなくメタデータが必要な場合は、`app/read` を使用します。
`appIds` には最大 100 件の ID を指定できます。
同じ ID が複数回指定された場合、サーバーは最初に出現したものだけを保持し、
`apps` と `missingAppIds` の両方でその順序を維持します。
不明なアプリやアクセスできないアプリは、リクエスト全体を失敗させずに `missingAppIds` で返されます。

```json
{
  "method": "app/read",
  "id": 52,
  "params": {
    "appIds": ["demo-app", "missing-app"],
    "includeTools": true
  }
}
{
  "id": 52,
  "result": {
    "apps": [
      {
        "id": "demo-app",
        "name": "Demo App",
        "description": "Example connector for documentation.",
        "iconUrl": null,
        "iconUrlDark": null,
        "distributionChannel": null,
        "installUrl": null,
        "pluginDisplayNames": [],
        "toolSummaries": [
          {
            "name": "search",
            "title": "Search",
            "description": "Search the app.",
            "isEnabled": true,
            "disabledReason": null,
            "isReadOnly": true
          }
        ]
      }
    ],
    "missingAppIds": ["missing-app"]
  }
}

表示専用の公開ツール概要を要求するには、`includeTools: true` を設定します。
メタデータのレスポンスには、インストール済みアプリのランタイム状態は含まれず、
ツール呼び出しを許可するものでもありません。実際に適用される `enabled` と `callable` の状態は、
`app/installed` で確認します。

アプリを呼び出すには、テキスト入力に `$<app-slug>` を挿入し、`app://<id>` のパスを持つ `mention` 入力項目を追加します（推奨）。

```json
{
  "method": "turn/start",
  "id": 51,
  "params": {
    "threadId": "thread-1",
    "input": [
      {
        "type": "text",
        "text": "$demo-app Pull the latest updates from the team."
      },
      {
        "type": "mention",
        "name": "Demo App",
        "path": "app://demo-app"
      }
    ]
  }
}

### 設定 RPC によるアプリ設定の例

`config/read`、`config/value/write`、`config/batchWrite` を使用して、`config.toml` 内のアプリの制御設定を確認または更新します。

実際に適用されるアプリ設定の構造（`_default` とツールごとの上書き設定を含む）を読み取ります：

```json
{ "method": "config/read", "id": 60, "params": { "includeLayers": false } }
{ "id": 60, "result": {
  "config": {
    "apps": {
      "_default": {
        "enabled": true,
        "destructive_enabled": true,
        "open_world_enabled": true,
        "approvals_reviewer": "user",
        "default_tools_approval_mode": "auto"
      },
      "google_drive": {
        "enabled": true,
        "destructive_enabled": false,
        "approvals_reviewer": "auto_review",
        "default_tools_approval_mode": "prompt",
        "tools": {
          "files/delete": { "enabled": false, "approval_mode": "approve" }
        }
      }
    }
  }
} }

`apps._default.approvals_reviewer` は、アプリごとの値で上書きされない限り、
すべてのアプリのレビュアーを設定します。両方が省略されている場合、
アプリは最上位の `approvals_reviewer` の値を継承します。
`apps._default.default_tools_approval_mode` は、アプリごとまたはツールごとの上書き設定がないツールに適用する承認モードを設定します。
管理設定の承認モード要件が、
ツールの承認モード設定より優先されます。

アプリ設定を 1 つ更新します：

```json
{
  "method": "config/value/write",
  "id": 61,
  "params": {
    "keyPath": "apps.google_drive.default_tools_approval_mode",
    "value": "prompt",
    "mergeStrategy": "replace"
  }
}

複数のアプリ設定の変更をアトミックに適用します：

```json
{
  "method": "config/batchWrite",
  "id": 62,
  "params": {
    "edits": [
      {
        "keyPath": "apps._default.destructive_enabled",
        "value": false,
        "mergeStrategy": "upsert"
      },
      {
        "keyPath": "apps.google_drive.tools.files/delete.approval_mode",
        "value": "approve",
        "mergeStrategy": "upsert"
      }
    ]
  }
}

### 外部エージェント設定の検出とインポート

`externalAgentConfig/detect` を使用して移行可能な外部エージェントのアーティファクトを検出し、選択した項目を `externalAgentConfig/import` に渡します。

検出例：

```json
{ "method": "externalAgentConfig/detect", "id": 63, "params": {
  "includeHome": true,
  "cwds": ["/Users/me/project"]
} }
{ "id": 63, "result": {
  "items": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    },
    {
      "itemType": "SKILLS",
      "description": "Copy skill folders from /Users/me/.claude/skills to /Users/me/.agents/skills.",
      "cwd": null
    }
  ]
} }

インポート例：

```json
{ "method": "externalAgentConfig/import", "id": 64, "params": {
  "migrationItems": [
    {
      "itemType": "AGENTS_MD",
      "description": "Import /Users/me/project/CLAUDE.md to /Users/me/project/AGENTS.md.",
      "cwd": "/Users/me/project"
    }
  ],
  "source": "claude-code"
} }
{ "id": 64, "result": { "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868" } }

省略可能な最上位のインポートパラメーター `source` は、
選択した移行項目を生成したプロダクトを示します。

項目タイプごとの処理が完了するたびに、サーバーは `externalAgentConfig/import/progress` を送信し、
すべての同期インポートとバックグラウンドインポートが完了すると `externalAgentConfig/import/completed` を送信します。
これらの通知には、レスポンスと同じ `importId` と、
タイプごとの `successes` と `failures` を含む `itemTypeResults` が含まれます。
完了通知はレスポンスの直後に届く場合もあれば、
バックグラウンドでのリモートインポートの完了後に届く場合もあります。

```json
{ "method": "externalAgentConfig/import/progress", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }
{ "method": "externalAgentConfig/import/completed", "params": {
  "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
  "itemTypeResults": [
    {
      "itemType": "AGENTS_MD",
      "successes": [
        { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
      ],
      "failures": []
    }
  ]
} }

過去に完了したインポートを読み取ります：

```json
{ "method": "externalAgentConfig/import/readHistories", "id": 65 }
{ "id": 65, "result": { "data": [
  {
    "importId": "8ae96ff3-3425-4f4c-8772-b6fd61502868",
    "completedAtMs": 1781784000000,
    "successes": [
      { "itemType": "AGENTS_MD", "cwd": "/Users/me/project", "source": null, "target": "/Users/me/project/AGENTS.md" }
    ],
    "failures": []
  }
] } }

サポートされている `itemType` の値は、`AGENTS_MD`、`CONFIG`、`SKILLS`、`PLUGINS`、
`MCP_SERVER_CONFIG`、`SUBAGENTS`、`HOOKS`、`COMMANDS`、`SESSIONS` です。
`PLUGINS` の項目では、`details.plugins` に各 `marketplaceName` と、
Codex が移行を試みられる `pluginNames` が一覧として含まれます。
検出結果には、まだ処理が必要な項目だけが含まれます。たとえば、`AGENTS.md` がすでに存在し、空でない場合、
Codex は AGENTS の移行をスキップします。
また、スキルのインポートで既存のスキルディレクトリが上書きされることはありません。

`.claude/settings.json` からプラグインを検出する際、
Codex は設定済みのマーケットプレイスのソースを `extraKnownMarketplaces` から読み取ります。
`enabledPlugins` に `claude-plugins-official` のプラグインが含まれていても、マーケットプレイスのソースがない場合、
Codex は `anthropics/claude-plugins-official` をソースと推定します。

## 認証エンドポイント

JSON-RPC の認証・アカウント機能では、リクエスト／レスポンス型のメソッドに加え、サーバー主導の通知（`id` なし）を利用できます。これらを使用して、認証状態の確認、ログインの開始やキャンセル、ログアウト、ChatGPT のレート制限の確認、クレジット切れや使用量上限についてのワークスペース所有者への通知を行えます。

### 認証モード

Codex は次の認証モードをサポートしています。`account/updated.authMode` は現在有効なモードを示し、取得できる場合は現在の ChatGPT の `planType` も含みます。`account/read` でも、アカウントとプランの詳細を確認できます。

- **API キー（`apikey`）** ：呼び出し元が `type: "apiKey"` を指定して OpenAI API キーを渡し、Codex が API リクエスト用に保存します。
- **ChatGPT 管理モード（`chatgpt`）** ：Codex が ChatGPT の OAuth フローを管理し、トークンを永続化して自動的に更新します。ブラウザフローの場合は `type: "chatgpt"`、デバイスコードフローの場合は `type: "chatgptDeviceCode"` で開始します。
- **ChatGPT 外部トークン（`chatgptAuthTokens`）** ：実験的なモードで、ユーザーの ChatGPT 認証ライフサイクルをすでに管理しているホストアプリを対象としています。ホストアプリは `accessToken` と `chatgptAccountId`、必要に応じて `chatgptPlanType` を直接提供し、要求された場合はトークンを更新する必要があります。
- **Amazon Bedrock** ：`account/read` は Bedrock アカウントを `type: "amazonBedrock"` として返し、認証情報の取得元が Codex が管理する Bedrock API キー（`credentialSource: "codexManaged"`）か、外部の AWS 認証情報チェーン（`credentialSource: "awsManaged"`）かを示します。`account/updated.authMode` では、Codex が管理する Bedrock API キーに `bedrockApiKey` を使用します。

### API の概要

- `account/read`：現在のアカウント情報を取得し、必要に応じてトークンを更新します。
- `account/login/start`：ログインを開始します（`apiKey`、`chatgpt`、`chatgptDeviceCode`、または実験的な `chatgptAuthTokens`）。
- `account/login/completed`（通知）：ログインの試行が完了したときに送信されます（成功またはエラー）。
- `account/login/cancel`：ChatGPT 管理モードで保留中のログインを、`loginId` を指定してキャンセルします。
- `account/logout`：ログアウトします。これにより `account/updated` が送信されます。
- `account/updated`（通知）：認証モードが変更されるたびに送信されます（`authMode` は `apikey`、`chatgpt`、`chatgptAuthTokens`、`agentIdentity`、`personalAccessToken`、`bedrockApiKey`、または `null`）。取得できる場合は `planType` も含まれます。
- `account/chatgptAuthTokens/refresh`（サーバーリクエスト）：認可エラーの発生後に、外部で管理されている新しい ChatGPT トークンを要求します。
- `account/rateLimits/read`：ChatGPT のレート制限を取得します。
- `account/rateLimits/updated`（通知）：ユーザーに適用される ChatGPT のレート制限が変更されるたびに送信されます。
- `account/sendAddCreditsNudgeEmail`：クレジット切れまたは使用量上限への到達について、ワークスペースの所有者にメールを送信するよう ChatGPT に依頼します。
- `account/rateLimitResetCredit/consume`：呼び出し元が指定した `idempotencyKey` の値を使用して、獲得済みのレート制限リセットを 1 回分消費します。
- `account/usage/read`：ChatGPT アカウントのトークン使用状況の概要と日次バケットを取得します。
- `account/workspaceMessages/read`：現在有効なワークスペースメッセージを取得します。取得できる場合は通知の見出しも含まれます。
- `mcpServer/oauthLogin/completed`（通知）：`mcpServer/oauth/login` フローの完了後に送信されます。ペイロードには `{ name, threadId, success, error? }` が含まれます。アプリ単位またはプラグインの OAuth フローでは、`threadId` が `null` となる場合があります。
- `mcpServer/startupStatus/updated`（通知）：設定済みの MCP サーバーの起動状態が変化したときに送信されます。ペイロードには `{ threadId, name, status, error, failureReason }` が含まれます。アプリ単位の起動では、`threadId` は `null` です。起動に失敗した場合、`failureReason: "reauthenticationRequired"` は、保存済みの OAuth 認証情報が期限切れになり、更新できなかったことを示します。そのため、クライアント側でサーバーへの再接続を案内してください。

### 1) 認証状態の確認

リクエスト：

```json
{ "method": "account/read", "id": 1, "params": { "refreshToken": false } }

レスポンス例：

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": false } }

```json
{ "id": 1, "result": { "account": null, "requiresOpenaiAuth": true } }

```json
{
  "id": 1,
  "result": { "account": { "type": "apiKey" }, "requiresOpenaiAuth": true }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "codexManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "amazonBedrock",
      "credentialSource": "awsManaged"
    },
    "requiresOpenaiAuth": false
  }
}

```json
{
  "id": 1,
  "result": {
    "account": {
      "type": "chatgpt",
      "email": "user@example.com",
      "planType": "pro"
    },
    "requiresOpenaiAuth": true
  }
}

フィールドの補足：

- `refreshToken`（boolean）：ChatGPT 管理モードでトークンを強制的に更新するには、`true` に設定します。外部トークンモード（`chatgptAuthTokens`）では、app-server はこのフラグを無視します。
- ChatGPT アカウントにメールアドレスがない場合、`email` は `null` です。
- `requiresOpenaiAuth` は現在有効なプロバイダーを反映します。`false` の場合、Codex は OpenAI の認証情報なしで実行できます。
- Amazon Bedrock は、Codex が管理する Bedrock API キーを使用する場合は `credentialSource: "codexManaged"` を返します。
  外部の AWS 認証情報の取得経路を使用する場合は `credentialSource: "awsManaged"` を返します。
  これらの値は、選択された認証情報の取得元を示します。
  AWS 認証情報チェーンで認証情報を取得できるかどうかまでは、
  検証しません。

### 2) API キーによるログイン

1. 送信：

   ```json
   {
     "method": "account/login/start",
     "id": 2,
     "params": { "type": "apiKey", "apiKey": "sk-..." }
   }

2. 想定される結果：

   ```json
   { "id": 2, "result": { "type": "apiKey" } }

3. 通知：

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "apikey", "planType": null }
   }

### 3) ChatGPT でのログイン（ブラウザフロー）

1. 開始：

   ```json
   {
     "method": "account/login/start",
     "id": 3,
     "params": {
       "type": "chatgpt",
       "useHostedLoginSuccessPage": true,
       "appBrand": "chatgpt"
     }
   }

   デフォルトでは、ブラウザのコールバックに成功するとローカルのログイン完了ページにリダイレクトされます。
   組織のセットアップが不要な場合にホスト型のログイン完了ページを使用するには、`useHostedLoginSuccessPage: true` を設定します。
   ホスト型のログイン完了ページを有効にした場合、`appBrand` には `"codex"` または `"chatgpt"` を指定できます。
   省略した場合や `null` の場合は、
デフォルト値の `"codex"` が使用されます。

   ```json
   {
     "id": 3,
     "result": {
       "type": "chatgpt",
       "loginId": "<uuid>",
       "authUrl": "https://chatgpt.com/...&redirect_uri=http%3A%2F%2Flocalhost%3A<port>%2Fauth%2Fcallback"
     }
   }

2. ブラウザで `authUrl` を開きます。ローカルのコールバックは app-server がホストします。
3. 通知を待ちます：

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3b) ChatGPT でのログイン（デバイスコードフロー）

クライアント側でサインイン手順を管理する場合や、ブラウザのコールバックが不安定な場合に、このフローを使用します。

1. 開始：

   ```json
   {
     "method": "account/login/start",
     "id": 4,
     "params": { "type": "chatgptDeviceCode" }
   }

   ```json
   {
     "id": 4,
     "result": {
       "type": "chatgptDeviceCode",
       "loginId": "<uuid>",
       "verificationUrl": "https://auth.openai.com/codex/device",
       "userCode": "ABCD-1234"
     }
   }

2. `verificationUrl` と `userCode` をユーザーに表示します。UX はフロントエンド側で管理します。
3. 通知を待ちます：

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": "<uuid>", "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgpt", "planType": "plus" }
   }

### 3c) 外部管理の ChatGPT トークンによるログイン（`chatgptAuthTokens`）

この実験的なモードは、ホストアプリケーションがユーザーの ChatGPT 認証ライフサイクルを管理し、トークンを直接提供する場合にのみ使用してください。このログイン方式を使用する前に、クライアントは `initialize` 時に `capabilities.experimentalApi = true` を設定する必要があります。

1. 送信：

   ```json
   {
     "method": "account/login/start",
     "id": 7,
     "params": {
       "type": "chatgptAuthTokens",
       "accessToken": "<jwt>",
       "chatgptAccountId": "org-123",
       "chatgptPlanType": "business"
     }
   }

2. 期待されるレスポンス：

   ```json
   { "id": 7, "result": { "type": "chatgptAuthTokens" } }

3. 通知：

   ```json
   {
     "method": "account/login/completed",
     "params": { "loginId": null, "success": true, "error": null }
   }

   ```json
   {
     "method": "account/updated",
     "params": { "authMode": "chatgptAuthTokens", "planType": "business" }
   }

サーバーが `401 Unauthorized` を受信すると、ホストアプリに更新済みのトークンを要求する場合があります：

```json
{
  "method": "account/chatgptAuthTokens/refresh",
  "id": 8,
  "params": { "reason": "unauthorized", "previousAccountId": "org-123" }
}
{ "id": 8, "result": { "accessToken": "<jwt>", "chatgptAccountId": "org-123", "chatgptPlanType": "business" } }

更新成功を示すレスポンスを受信すると、サーバーは元のリクエストを再試行します。リクエストは約 10 秒後にタイムアウトします。

### 4) ChatGPT ログインのキャンセル

```json
{ "method": "account/login/cancel", "id": 4, "params": { "loginId": "<uuid>" } }
{ "method": "account/login/completed", "params": { "loginId": "<uuid>", "success": false, "error": "..." } }

### 5) ログアウト

```json
{ "method": "account/logout", "id": 5 }
{ "id": 5, "result": {} }
{ "method": "account/updated", "params": { "authMode": null, "planType": null } }

### 6) レート制限（ChatGPT）

```json
{ "method": "account/rateLimits/read", "id": 6 }
{ "id": 6, "result": {
  "rateLimits": {
    "limitId": "codex",
    "limitName": null,
    "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
    "secondary": null,
    "rateLimitReachedType": null
  },
  "rateLimitsByLimitId": {
    "codex": {
      "limitId": "codex",
      "limitName": null,
      "primary": { "usedPercent": 25, "windowDurationMins": 15, "resetsAt": 1730947200 },
      "secondary": null,
      "rateLimitReachedType": null
    },
    "codex_other": {
      "limitId": "codex_other",
      "limitName": "codex_other",
      "primary": { "usedPercent": 42, "windowDurationMins": 60, "resetsAt": 1730950800 },
      "secondary": null,
      "rateLimitReachedType": null
    }
  },
  "rateLimitResetCredits": {
    "availableCount": 2,
    "credits": [{
      "id": "RateLimitResetCredit_1",
      "resetType": "codexRateLimits",
      "status": "available",
      "grantedAt": 1781654400,
      "expiresAt": 1784246400,
      "title": "Rate-limit reset",
      "description": "Reset an eligible Codex rate-limit window."
    }]
  }
} }
{ "method": "account/rateLimits/updated", "params": {
  "rateLimits": {
    "limitId": "codex",
    "primary": { "usedPercent": 31, "windowDurationMins": 15, "resetsAt": 1730948100 }
  }
} }

フィールドに関する注意事項：

- `rateLimits` は、後方互換性のある単一バケットのビューです。
- `rateLimitsByLimitId` は、計測対象の `limit_id`（例：`codex`）をキーとする複数バケットのビューで、省略される場合があります。
- `limitId` は、計測対象バケットの識別子です。
- `limitName` は、バケットのユーザー向けラベルで、省略可能です。
- `usedPercent` は、クォータ期間内の現在の使用率です。
- `windowDurationMins` は、クォータ期間の長さです。
- `resetsAt` は、次回のリセット時刻を示す秒単位の Unix タイムスタンプです。
- `planType` は、サーバーがバケットに関連付けられた ChatGPT プランを返す場合に含まれます。
- `credits` は、サーバーがワークスペースの残りのクレジットに関する詳細を返す場合に含まれます。
- `rateLimitReachedType` は、制限に達した場合に、サーバーが分類した制限状態を示します。
- サービスが獲得済みリセットの利用可能回数を提供する場合、`rateLimitResetCredits` にその値が含まれます。提供しない場合は `null` です。
- 回数のみが判明している場合、`rateLimitResetCredits.credits` は `null` です。空の配列は、サービスが詳細を取得した結果、利用可能なクレジットがなかったことを意味します。サービスが詳細行の件数を制限する場合があるため、`availableCount` を正として扱ってください。
- 各詳細行には、不透明な `id`、`resetType`、`status`、`grantedAt`、`expiresAt`（`null` の場合があります）、`title`（`null` の場合があります）、および `description`（`null` の場合があります）が含まれます。
- リセットを使用した後は、`account/rateLimits/read` を呼び出して情報を取得してください。

### 7) トークン使用量（ChatGPT）

`account/usage/read` を使用して、ChatGPT のトークン使用状況の概要フィールドを取得します。
オプションで日次バケットも取得できます。

```json
{ "method": "account/usage/read", "id": 7 }
{ "id": 7, "result": {
  "summary": {
    "lifetimeTokens": 1234567,
    "peakDailyTokens": 45678,
    "longestRunningTurnSec": 540,
    "currentStreakDays": 8,
    "longestStreakDays": 14
  },
  "dailyUsageBuckets": [
    { "startDate": "2026-06-18", "tokens": 12345 }
  ]
} }

フィールドに関する注意事項：

- サービスがその指標を返していない場合、`summary` の値は `null` になることがあります。
- `dailyUsageBuckets` は `null` の場合があります。値が存在する場合、各バケットには `startDate` と `tokens` が含まれます。
- このエンドポイントには、Codex サービスによる認証が必要です。ChatGPT、外部管理の ChatGPT トークン、エージェント ID、個人アクセストークンによる認証は利用できますが、API キーのみの認証と Bedrock 認証は利用できません。

### 8) 獲得済みのレート制限リセット（ChatGPT）

`account/rateLimitResetCredit/consume` を使用して、獲得済みのリセットを 1 回分消費します。

```json
{ "method": "account/rateLimitResetCredit/consume", "id": 8, "params": { "idempotencyKey": "8ae96ff3-3425-4f4c-8772-b6fd61502868", "creditId": "RateLimitResetCredit_1" } }
{ "id": 8, "result": { "outcome": "reset" } }

フィールドに関する注意事項：

- `idempotencyKey` は空でない値にする必要があります。論理的な引き換え処理ごとに UUID を使用し、その処理を再試行する場合は同じ値を再利用してください。
- `creditId` は省略可能です。指定する場合は、`account/rateLimits/read` から取得した空でない不透明な ID を使用する必要があります。省略すると、サービスが次に利用可能なクレジットを選択します。
- `reset` は、クレジットが消費されたことを意味します。
- `alreadyRedeemed` は、同じ引き換え処理が以前に完了していることを意味します。冪等な成功として扱い、アカウントの制限情報を再取得してください。
- `nothingToReset` は、リセット対象となるレート制限期間がないことを意味します。
- `noCredit` は、アカウントに利用可能な獲得済みリセットクレジットがないことを意味します。
- このレスポンスから更新後のレート制限期間を推測せず、リセットを使用した後に `account/rateLimits/read` を呼び出して情報を取得してください。

### 9) 制限に関するワークスペース所有者への通知

`account/sendAddCreditsNudgeEmail` を使用して、クレジットを使い切った場合や使用量の上限に達した場合に、ワークスペースの所有者へメールを送信するよう ChatGPT に依頼します。

```json
{ "method": "account/sendAddCreditsNudgeEmail", "id": 9, "params": { "creditType": "credits" } }
{ "id": 9, "result": { "status": "sent" } }

ワークスペースのクレジットを使い切った場合は `creditType: "credits"` を、ワークスペースの使用量の上限に達した場合は `creditType: "usage_limit"` を使用します。所有者に最近すでに通知している場合、レスポンスのステータスは `cooldown_active` です。

### 10) ワークスペースのメッセージ（ChatGPT）

`account/workspaceMessages/read` を使用して、現在のワークスペースで有効なメッセージを取得します。
利用可能な場合は、通知の見出しも含まれます。

```json
{ "method": "account/workspaceMessages/read", "id": 10 }
{ "id": 10, "result": { "featureEnabled": true, "messages": [
  { "messageId": "msg_123", "messageType": "headline", "messageBody": "Workspace maintenance starts at 5pm.", "createdAt": 1781395200, "archivedAt": null }
] } }
