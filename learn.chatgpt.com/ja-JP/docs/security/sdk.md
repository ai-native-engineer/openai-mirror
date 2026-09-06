<!-- source: https://learn.chatgpt.com/ja-JP/docs/security/sdk -->

Codex Security TypeScript SDK を使用すると、アプリケーションや開発ツールから、リポジトリやコードの変更に対してセキュリティスキャンを実行できます。SDK は、型付きの検出結果、カバレッジの詳細、スキャンアーティファクトへのパスを返します。長時間のスキャンでは、プリフライトチェック、コスト制限、進行状況コールバック、キャンセルにも対応しています。

SDK は ECMAScript モジュール（ESM）を使用し、Node.js 22
（22.13.0 以降）、24、または 26 を使用してサーバー側で動作します。スキャンには Python 3.10 以降も必要です。
Python 3.10 では、`tomli` パッケージも必要です。

  Codex Security SDK は [GitHub
  で一般公開されています](https://github.com/openai/codex-security)。スキャンを実行するには、
  Codex Security へのアクセス権が必要です。一般的なコーディングエージェントについては、[Codex SDK
  ガイド](/ja-JP/codex/codex-sdk)を参照してください。ターミナルと CI のワークフローについては、[Codex Security CLI
  クイックスタート](/ja-JP/codex/security/cli)を参照してください。

## SDK のセットアップ

SDK をインストールします：

```bash
npm install @openai/codex-security

スキャンを開始する前に、`OPENAI_API_KEY` または `CODEX_API_KEY` を設定するか、
ファイルに保存された既存の Codex サインインを使用するか、[別の
プロバイダーを構成してください](#configure-the-runtime-and-credentials)。Amazon Bedrock では AWS
認証情報を使用し、OpenRouter と Fireworks ではプロバイダー固有の API キーと
構成を使用します。

最適な結果を得るには、[Trusted Access for
Cyber](https://chatgpt.com/cyber) の利用資格が確認済みのアカウントを使用してください。サインインや API キーの提供だけでは、
Trusted Access は付与されません。

## スキャンの実行

信頼でき、評価する権限があるリポジトリのみをスキャンしてください。SDK は
ローカルのオペレーティングシステムの権限で実行され、承認を求めて一時停止することはありません。
スキャンプロセスが環境を継承する場合があるため、開始前に無関係な認証情報を
削除してください。詳しくは、[ローカルスキャンの
権限](/ja-JP/codex/security/cli/reference#local-scan-permissions)を参照してください。

`CodexSecurity` クライアントを 1 つ作成して標準のリポジトリスキャンを実行し、
作業が完了したらクライアントを閉じます。`outputDir` を渡すと、
対象を含む Git Worktree の外部にある非公開の結果ディレクトリを指定できます。

`outputDir` を省略すると、Codex Security は独自の永続的な
状態ディレクトリに結果を保存します。結果にはソースの抜粋や脆弱性の
詳細が含まれる場合があるため、適切な権限と保持ポリシーを選択してください。

```ts

const security = new CodexSecurity();

try {
  const result = await security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
  });

  console.log(result.reportPath);
  console.log(result.coverage.completeness);
  console.log(result.findings.findings.length);
} finally {
  await security.close();
}

`run` はスキャンを開始し、完了を待って封印済みのアーティファクトを検証し、
`ScanResult` を返します。`close` は分離されたランタイムを解放し、
繰り返し呼び出せます。

## プリフライトによる入力確認

スキャンを開始する前に、`preflight` を使用して、リポジトリ、ターゲット、モード、ナレッジベースのドキュメント、
出力先、Codex の構成を確認します：

```ts
const plan = await security.preflight("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
  knowledgeBasePaths: ["/path/to/architecture.md"],
  outputDir: "/path/outside/repository/results",
});

console.log(plan.repository);
console.log(plan.target.kind);
console.log(plan.mode);
console.log(plan.outputDir);

プリフライトでは、Codex ランタイムと認証情報は変更されません。プラグインと Python の検出もスキャンの実行時まで行われません。そのため、長時間実行される処理や認証情報を使用する処理の前に、ユーザー入力を確認する場合に役立ちます。

既存の結果ディレクトリのアーカイブ処理をプレビューするには、
`archiveExisting: true` を設定します：

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

返される `archiveDir` でアーカイブ名を事前に確認できます。
`run` が独自の一意な保存先を生成するため、最終的なパスは異なる場合があります。
実際のアーカイブパスは `onOutputArchived` で取得します：

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

スキャンでは以前の結果をアーカイブし、空の出力ディレクトリから開始します。

## スキャンターゲットの選択

SDK は、リポジトリ、パス、コミット済み差分、Worktree の各ターゲットに対応しています。デフォルトのターゲットはリポジトリ全体です。

### 選択したパスのスキャン

リポジトリ内のパスを配列で渡します：

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

パスにはファイルまたはディレクトリを指定できます。SDK は各パスをリポジトリ内のパスとして解決し、重複を削除します。

### コミット済み変更のスキャン

`DiffTarget.refs` を使用して、ローカルで利用できる 2 つの
Git リビジョン間のコミット済み変更をスキャンします：

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

head のデフォルト値は `HEAD` です。差分ターゲットでは、リポジトリ引数に
Git Worktree のルートを指定する必要があります。

### Worktree のスキャン

`DiffTarget.workingTree` を使用して、ベースリビジョンに対する
ステージ済みおよび未ステージの変更をスキャンします：

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

base のデフォルト値は `HEAD` です。差分または Worktree のスキャンを開始する前に、
選択したリビジョンをフェッチしてください。

### deep モードの選択

より広範なレビューが必要なリポジトリまたはパスのスキャンでは、`mode: "deep"` を設定します：

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing"],
  mode: "deep",
  workers: 2,
  subagents: 0,
  stopAfterNoNew: 3,
  maxDiscoveryRuns: 10,
  maxTimeHours: 1.5,
});

deep モードは、リポジトリとパスのターゲットに対応しています。差分と
Worktree のスキャンには標準モードを使用してください。オプション設定では、独立した標準スキャンワーカーの
同時実行数、ワーカーごとのサブエージェント数、新たな検出結果がないまま完了したワーカースキャンの
連続回数、ワーカーの合計実行回数と実行時間を制御できます。これらの設定には
`mode: "deep"` が必要です。

`maxTimeHours` のデフォルト値は `96` で、`96` 以下の正の数値を指定できます。
小数による時間指定にも対応しています。制限時間に達すると、Codex Security は未完了の
ワーカーを停止し、完了したスキャン結果を保持して最終レポートに集約します。
制限時間付きのスキャンを完全なカバレッジの根拠と見なす前に、`result.coverage.completeness` を
確認してください。

### セキュリティナレッジベースの追加

アーキテクチャドキュメント、脅威モデル、またはセキュリティポリシーを、
`knowledgeBasePaths` で渡します：

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

SDK はファイルまたはディレクトリを受け入れ、ディレクトリを再帰的に検索します。
対応するドキュメント形式は `.md`、`.markdown`、`.txt`、`.pdf`、`.docx` です。
SDK はリンクされた入力パスを拒否し、リンクされたディレクトリエントリをスキップして、
抽出したドキュメントの内容を保存されるスキャン結果には含めません。

### スキャン指示とフォローアップ指示の追加

`scanPrompt` でスキャンの重点を指定し、`postScanPrompt` でフォローアップをリクエストします：

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

フォローアップが失敗した場合、SDK は完了したスキャンを保持し、
`onWarning` を通じてエラーを報告します。フォローアップによって変更された
完了したスキャンのアーティファクトはすべて復元します。

### スキャン予算の設定

`maxCostUsd` を設定して、推定モデルコストが上限を超えたときにスキャンを停止します。
スキャン実行中のコストを追跡するには、`onCost` を使用します：

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

この上限は支出額の見積もりに基づくもので、厳密な上限ではありません。そのため、すでに実行中の
リクエストは、上限をわずかに超えて完了する場合があります。Codex Security が完了したワーカーの結果を集約した後、
deep モードのスキャンが上限に達した場合、`run` は
`coverage.completeness` を `"partial"` に設定した結果を返し、予算に関する警告を
`onWarning` を通じて報告します。

スキャンで完了済みの部分的な結果を生成できない場合、`run` は
`ScanCostLimitExceededError` をスローし、利用可能な出力を保持します。

## スキャン結果の利用

`ScanResult` から、構造化ドキュメント、スキャンのメタデータ、アーティファクトの
パスにアクセスできます：

| プロパティ             | 内容                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | ターゲット、スコープ、生成元、アーティファクトのレコードを含む、封印済みのスキャンマニフェスト。 |
| `findings`           | 今回のスキャンの検出結果。検出結果オブジェクトは `findings.findings` から読み取ります。     |
| `repositoryFindings` | スキャン履歴を利用できる場合に取得される、リポジトリの各スキャンにまたがる未解決の検出結果。             |
| `coverage`           | レビュー済みの対象領域、除外項目、保留中の作業、未解決の疑問点、完全性。    |
| `scanDir`            | スキャンディレクトリ。                                                                |
| `threadId`           | スキャンの Codex スレッド識別子。                                          |
| `turnResult`         | ターンのステータス、レスポンス、利用可能な使用量メタデータ。                               |
| `cost`               | モデルとトークンの推定コスト。利用できない場合は `null`。                        |
| `reportPath`         | `report.md` へのパス。                                                           |
| `manifestPath`       | `scan-manifest.json` へのパス。                                                  |
| `findingsPath`       | `findings.json` へのパス。                                                       |
| `coveragePath`       | `coverage.json` へのパス。                                                       |
| `artifactsDir`       | 補助アーティファクトのディレクトリ。                                                |
| `sarifPath`          | 生成された SARIF のパス。SARIF がない場合は `null`。                          |
| `pluginVersion`      | スキャン生成元が記録したバージョン。                                         |

後続のスキャンで同じプラグインの使用を必須にするには、
`expectedPluginVersion: result.pluginVersion` を渡します。インストール済みのプラグインのバージョンが
異なる場合、SDK はスキャンを拒否します。

構造化された検出結果とカバレッジを直接使用します：

```ts
for (const finding of result.findings.findings) {
  const location = finding.locations[0];
  if (location === undefined) continue;

  console.log(
    finding.severity.level,
    `${location.path}:${location.startLine}`,
    finding.title
  );
}

for (const deferred of result.coverage.deferred) {
  console.log(deferred.id, deferred.reason);
}

検出結果には、任意項目として `codeEvidence`、`rootCause`、`validation`、
`attackPath`、`remediationTests`、`preventiveControls` の各フィールドが含まれる場合があります。

リポジトリ全体の検出結果では、`confirmedInLatestScan` により、最新のスキャンで
確認された検出結果と、以前のスキャンから未解決のまま残っている検出結果を区別できます：

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

カバレッジの完全性は `complete`、`partial`、`unknown` のいずれかです。
スキャン結果をセキュリティ上の判断の根拠にする前に、
レビューが保留された対象領域、除外項目、未解決の疑問点を確認してください。

`result.toJSON()` は、マニフェスト、リポジトリ全体と今回のスキャンの検出結果、
カバレッジ、スキャンとスレッドの識別子、`reportPath`、`artifactsDir`、
`sarifPath`、コスト、ターンのメタデータを、JSON に変換できる 1 つのオブジェクトとして返します。

## スキャンの追跡とキャンセル

`ScanOptions` のコールバックを渡すと、スキャンの開始、ワーカーの進捗、
接続の再試行を報告できます：

```ts
const result = await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  onScanStarted() {
    console.log("Scan started");
  },
  onProgress(progress) {
    console.log(progress.phase, progress.filesCompleted, progress.filesTotal);
  },
  onWorkerStatus(status) {
    console.log(status.kind, status);
  },
  onSessionEvent(session) {
    console.log(session.threadId, session.worker, session.event["type"]);
  },
  onReconnect(attempt, maxAttempts) {
    console.log(`Reconnect attempt ${attempt} of ${maxAttempts}`);
  },
  onObserverError(observer, error) {
    console.error(`${observer} failed`, error);
  },
});

console.log(result.reportPath);

リクエスト、ジョブコントローラー、
またはタイムアウトによってキャンセルする場合は、`AbortSignal` を渡します：

```ts

const controller = new AbortController();

try {
  const scan = security.run("/path/to/repository", {
    outputDir: "/path/outside/repository/results",
    signal: controller.signal,
  });

  controller.abort();
  await scan;
} catch (error) {
  if (error instanceof ScanInterruptedError) {
    console.error(error.scanDir);
  } else {
    throw error;
  }
}

スキャンを中断すると、`scanDir` に部分的な出力が残ることがあります。
結果を調査する必要がある場合は、このディレクトリを保持してください。

スキャンのセットアップの進捗を表示するアプリケーションでは、`ScanOptions` の
ライフサイクルコールバックも使用できます：

| コールバック                            | 呼び出しのタイミング                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | スキャンの認証方式が選択されます。          |
| `onOutputArchived(archiveDir)`      | 既存の結果がアーカイブディレクトリに移動します。      |
| `onOutputDirReady(scanDir)`         | 非公開のスキャンディレクトリの準備が整います。                 |
| `onScanStarted()`                   | スキャンのセットアップが完了し、実行が開始されます。           |
| `onTrustedAccessStatus(status)`     | Trusted Access のステータスを取得できるようになります。             |
| `onReconnect(attempt, maxAttempts)` | SDK が切断されたスキャンストリームへの接続を再試行します。          |
| `onActivity(activity)`              | コマンド、ツール、推論ステップ、またはメッセージが更新されます。 |
| `onProgress(progress)`              | スキャンフェーズまたはレビュー済みのファイル数が変わります。       |
| `onWorkerStatus(status)`            | ワーカーのプリフライトまたはディスパッチのステータスが変わります。         |
| `onSessionEvent(session)`           | スキャンまたはワーカーセッションがイベントを発行します。             |
| `onCost(cost)`                      | 更新されたスキャンの推定コストを取得できるようになります。         |
| `onWarning(warning)`                | スキャン中に警告が報告されます。                          |
| `onObserverError(observer, error)`  | 別のスキャンライフサイクルコールバックがエラーをスローします。     |

Trusted Access のステータスは `granted`、`not_granted`、`unknown` のいずれかです。アクセス権がない場合や
アクセス権の有無が不明な場合にも、`onWarning` が呼び出されます。

`onSessionEvent` が受け取るイベントはマスキングされておらず、
ソースコードや認証情報が含まれる場合があります。共有ログやほかの
サービスに送信する前に、フィルタリングしてください。

## ランタイムと認証情報の構成

特定のプラグイン、インタープリター、または
Codex の設定が必要な場合は、ランタイム構成を渡します：

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` にはプラグインディレクトリまたは ZIP を指定できます。`pythonPath` では
プラグインのインタープリターを選択します。`codexOverrides` は、サポートされている値を分離された
Codex の構成にマージします。スキャンでは、デフォルトで `gpt-5.6-sol` を極高の推論強度で
使用します。別のモデルまたは推論強度を使用するには、`model` と `model_reasoning_effort` を `codexOverrides` に
設定します。[Amazon
Bedrock](/ja-JP/codex/security/cli/reference#use-amazon-bedrock) を使用するには、
`model_provider` と `model` を `codexOverrides` に設定します。

`codexOverrides` では、スキャンによるファイルシステムへのアクセスを制限したり、
承認ポリシーを変更したりすることはできません。詳しくは、[ローカルスキャンの
権限](/ja-JP/codex/security/cli/reference#local-scan-permissions)を参照してください。

OpenRouter または Fireworks を使用する場合は、対応する API キーに加え、
`codexOverrides` にプロバイダーの完全な構成を指定します。たとえば、
`OPENROUTER_API_KEY` を設定し、OpenRouter を次のように構成します：

```ts
const security = new CodexSecurity({
  codexOverrides: {
    model: "anthropic/claude-sonnet-4.5",
    model_provider: "openrouter",
    model_providers: {
      openrouter: {
        name: "OpenRouter",
        base_url: "https://openrouter.ai/api/v1",
        env_key: "OPENROUTER_API_KEY",
        wire_api: "responses",
      },
    },
  },
});

Fireworks では、両方の `openrouter` キーを `fireworks` に変更し、`name` を
`Fireworks AI` に、`env_key` を `FIREWORKS_API_KEY` に設定します。さらに、
`https://api.fireworks.ai/inference/v1` を `base_url` として使用し、Fireworks の
モデルを選択します。

クライアントは、サポートされている次の認証メソッドも提供します：

| メソッド                     | 用途                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | 分離されたランタイムを API キーで認証します。          |
| `loginChatGPT()`           | ブラウザでのサインインフローを開始し、ログインハンドルを返します。     |
| `loginChatGPTDeviceCode()` | デバイスコードによるサインインフローを開始し、ログインハンドルを返します。 |
| `account()`                | 現在の認証状態を返します。                    |
| `logout()`                 | 分離環境の認証情報を消去します。                              |

ログインハンドルには `waitForInstructions`、`authUrl`、`verificationUrl`、
`userCode`、`wait`、`cancel` が用意されているため、アプリケーションは選択した
サインインフローを提示し、完了できます。SDK はファイルに保存された Codex のサインイン情報を再利用できます。API キーは
CI やサーバー側の自動化に適しています。

API キーと保存済みのサインイン情報の両方を利用できる場合、SDK はデフォルトで API キーを使用します。
代わりに ChatGPT のサインイン情報を使用するには、スキャン時にそれを選択します：

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

環境変数の API キーを必須にするには、`auth: "api-key"` を設定します。`preflight` でも
同じ `auth` オプションを使用できます。

## スキャンエラーの処理

アプリケーションで実行できる対処に合った、
エクスポート済みのエラークラスをキャッチします：

| エラー                            | 意味                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | スキャンにはサポート対象の認証情報が必要です。                               |
| `ConfigurationError`             | Codex の構成またはオーバーライドが不適切です。                  |
| `InvalidTargetError`             | リポジトリ、パス、モード、または Git ターゲットが不適切です。           |
| `OutputDirectoryError`           | 出力先またはその権限が不適切です。             |
| `OutputInsideProtectedRootError` | 出力ディレクトリが、スキャン対象のリポジトリまたは Worktree 内にあります。 |
| `PluginPythonUnavailableError`   | 使用可能な Python インタープリターがありません。                        |
| `PluginBootstrapError`           | プラグインランタイムを起動できませんでした。                                |
| `ScanCostLimitExceededError`     | スキャンが推定コストの上限を超えました。                        |
| `IncompleteScanError`            | 必要な結果が生成される前にスキャンが終了しました。               |
| `ContractValidationError`        | 完了したスキャンから構造化コントラクトエラーが返されました。             |
| `ScanInterruptedError`           | 中断によりスキャンが停止し、部分的な出力が残っている可能性があります。 |

続いて、[CLI クイックスタート](/ja-JP/codex/security/cli)、[CI
ガイド](/ja-JP/codex/security/cli/ci)、または [CLI
リファレンス](/ja-JP/codex/security/cli/reference) を参照してください。
