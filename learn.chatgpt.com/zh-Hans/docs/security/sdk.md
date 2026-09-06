<!-- source: https://learn.chatgpt.com/zh-Hans/docs/security/sdk -->

通过您的应用或开发者工具，使用 Codex Security TypeScript SDK 对代码仓库和代码更改进行安全扫描。SDK 会返回带类型信息的发现结果、覆盖范围详情和扫描产物路径。对于长时间运行的扫描，它支持预检、成本限制、进度回调和取消操作。

该 SDK 使用 ECMAScript 模块（ESM），可使用 Node.js 22
（22.13.0 或更高版本）、24 或 26 在服务器端运行。扫描还需要 Python 3.10 或更高版本。
使用 Python 3.10 时还需要安装 `tomli` 包。

  Codex Security SDK 已[在
  GitHub 上公开提供](https://github.com/openai/codex-security)。运行扫描需要
  Codex Security 访问权限。对于通用编程智能体，请参阅 [Codex SDK
  指南](/zh-Hans/codex/codex-sdk)。对于终端和 CI 工作流，请参阅 [Codex
  Security CLI 快速入门](/zh-Hans/codex/security/cli)。

## 设置 SDK

安装 SDK：

```bash
npm install @openai/codex-security

开始扫描前，请设置 `OPENAI_API_KEY` 或 `CODEX_API_KEY`，使用
文件中保存的现有 Codex 登录信息，或[配置其他
提供商](#configure-the-runtime-and-credentials)。Amazon Bedrock 使用 AWS
凭据；OpenRouter 和 Fireworks 使用相应提供商专用的 API 密钥和
配置。

为获得最佳效果，请使用已通过 [Trusted Access for
Cyber](https://chatgpt.com/cyber) 验证的账户。登录或提供 API 密钥并不会
授予 Trusted Access 权限。

## 运行扫描

仅扫描您信任且有权评估的代码仓库。SDK 以您本地操作系统的权限运行，
绝不会暂停等待审批。
扫描进程可能继承您的环境，因此开始前请移除
无关凭据。请参阅[本地扫描
权限](/zh-Hans/codex/security/cli/reference#local-scan-permissions)。

创建一个 `CodexSecurity` 客户端，运行标准代码仓库扫描，并在任务完成后关闭
客户端。传入 `outputDir`，指定所属 Git 工作树之外的私有
结果目录。

如果省略 `outputDir`，Codex Security 会将结果保存在自身的持久化
状态目录中。结果可能包含源代码片段和漏洞
详情，因此请选择适当的权限和保留政策。

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

`run` 会启动扫描、等待扫描完成、验证已封存的产物，
并返回 `ScanResult`。`close` 会释放隔离运行时，并支持
重复调用。

## 通过预检检查输入

开始扫描前，使用 `preflight` 检查代码仓库、目标、模式、知识库文档、
输出位置和 Codex 配置：

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

预检不会触及 Codex 运行时和凭据，也会将插件和 Python 的查找留到实际扫描时进行。因此，预检适合在执行长时间运行或需要凭据的操作之前检查用户输入。

要预览现有结果目录的归档，请设置
`archiveExisting: true`：

```ts
const plan = await security.preflight("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
});

console.log(plan.archiveDir);

返回的 `archiveDir` 可预览归档命名方式。最终路径可能
有所不同，因为 `run` 会自行生成唯一的目标位置。如需获取实际的
归档路径，请使用 `onOutputArchived`：

```ts
await security.run("/path/to/repository", {
  outputDir: "/path/outside/repository/results",
  archiveExisting: true,
  onOutputArchived(archiveDir) {
    console.log("Archived results:", archiveDir);
  },
});

扫描会先归档此前的结果，然后使用空的输出目录开始运行。

## 选择扫描目标

SDK 支持以代码仓库、路径、已提交的差异或工作树作为目标。默认目标是整个代码仓库。

### 扫描选定路径

传入由代码仓库内路径组成的数组：

```ts
const result = await security.run("/path/to/repository", {
  target: ["services/billing", "packages/auth"],
});

路径可以指向文件或目录。SDK 会在代码仓库内解析每条路径，并移除重复项。

### 扫描已提交的更改

使用 `DiffTarget.refs` 扫描本地可用的两个
Git 修订版本之间已提交的更改：

```ts

const target = DiffTarget.refs({
  base: "origin/main",
  head: "HEAD",
});

const result = await security.run("/path/to/repository", { target });

目标版本默认为 `HEAD`。对于差异目标，代码仓库参数必须
指向 Git 工作树的根目录。

### 扫描工作树

使用 `DiffTarget.workingTree` 扫描相对于基准
修订版本的已暂存和未暂存更改：

```ts
const target = DiffTarget.workingTree({ base: "HEAD" });
const result = await security.run("/path/to/repository", { target });

基准版本默认为 `HEAD`。请先获取所选修订版本，再开始
差异或工作树扫描。

### 选择深度模式

对于需要更广泛审查的代码仓库或路径扫描，请设置 `mode: "deep"`：

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

深度模式支持代码仓库和路径目标。对于差异和
工作树扫描，请使用标准模式。可选设置用于控制并发运行的独立
标准扫描工作进程数量、每个工作进程的子智能体数量、连续完成且未产生新发现结果的工作进程扫描次数，
以及工作进程的运行总次数和持续时间。这些设置
要求使用 `mode: "deep"`。

`maxTimeHours` 默认为 `96`，接受不超过 `96` 的正数，
包括以小数表示的小时数。达到截止时间后，Codex Security 会停止尚未完成的
工作进程，保留已完成的扫描结果，并将这些结果汇总到最终
报告中。请先审查 `result.coverage.completeness`，再将限时
扫描作为完整覆盖的证据。

### 添加安全知识库

通过
`knowledgeBasePaths` 传入架构文档、威胁模型或安全策略：

```ts
const result = await security.run("/path/to/repository", {
  knowledgeBasePaths: [
    "/path/to/architecture.md",
    "/path/to/security-policies",
  ],
});

SDK 接受文件或目录，并会递归搜索目录。
支持的文档格式包括 `.md`、`.markdown`、`.txt`、`.pdf` 和 `.docx`。
SDK 会拒绝链接形式的输入路径、跳过链接形式的目录项，
并且不会将提取的文档内容写入已保存的扫描结果。

### 添加扫描和后续处理指令

使用 `scanPrompt` 指定扫描重点，并使用 `postScanPrompt` 请求后续处理：

```ts
const result = await security.run("/path/to/repository", {
  scanPrompt: "Focus on tenant isolation and authorization checks.",
  postScanPrompt: "Write confirmed findings to post-scan-summary.md.",
});

如果后续处理失败，SDK 会保留已完成的扫描，并通过
`onWarning` 报告错误，同时还原后续处理
更改过的所有已完成扫描产物。

### 设置扫描预算

设置 `maxCostUsd`，以便在预计模型成本超过限制时停止扫描。
使用 `onCost` 跟踪扫描运行期间的成本：

```ts
const result = await security.run("/path/to/repository", {
  maxCostUsd: 5,
  onCost(cost) {
    console.log(cost.estimatedUsd);
  },
});

console.log(result.cost?.estimatedUsd);

该限制用于估算支出，并非硬性上限，因此已经
进行中的请求完成后，支出可能略高于该限制。如果深度扫描在
Codex Security 汇总已完成工作进程的结果后达到限制，`run` 会返回一个结果，
其中 `coverage.completeness` 设置为 `"partial"`，并通过
`onWarning` 报告预算警告。

如果扫描无法生成已完成的部分结果，`run` 会抛出
`ScanCostLimitExceededError`，并保留所有可用输出。

## 处理扫描结果

`ScanResult` 提供结构化文档、扫描元数据和产物
路径：

| 属性             | 内容                                                                           |
| -------------------- | ---------------------------------------------------------------------------------- |
| `manifest`           | 已封存的扫描清单，包括目标、范围、生成方和产物记录。 |
| `findings`           | 当前扫描的发现结果。从 `findings.findings` 读取发现结果对象。     |
| `repositoryFindings` | 如果有扫描历史记录，则包含代码仓库历次扫描中尚未解决的发现结果。             |
| `coverage`           | 已审查范围、排除项、暂缓处理的工作、未决问题和完整性。    |
| `scanDir`            | 扫描目录。                                                                |
| `threadId`           | 此次扫描的 Codex 线程标识符。                                          |
| `turnResult`         | 轮次状态、响应和可用的用量元数据。                               |
| `cost`               | 模型和 Token 的预计成本；不可用时为 `null`。                        |
| `reportPath`         | 指向 `report.md` 的路径。                                                           |
| `manifestPath`       | 指向 `scan-manifest.json` 的路径。                                                  |
| `findingsPath`       | 指向 `findings.json` 的路径。                                                       |
| `coveragePath`       | 指向 `coverage.json` 的路径。                                                       |
| `artifactsDir`       | 辅助产物目录。                                                |
| `sarifPath`          | 生成的 SARIF 路径；没有 SARIF 时为 `null`。                          |
| `pluginVersion`      | 扫描生成方记录的版本。                                         |

要在后续扫描中要求使用同一插件，请传入
`expectedPluginVersion: result.pluginVersion`。如果已安装的插件版本不同，SDK 会
拒绝扫描。

直接使用结构化的发现结果和覆盖范围：

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

发现结果可包含可选的 `codeEvidence`、`rootCause`、`validation`、
`attackPath`、`remediationTests` 和 `preventiveControls` 字段。

对于整个代码仓库的发现结果，`confirmedInLatestScan` 用于区分
最新扫描中发现的问题与先前发现但仍未解决的问题：

```ts
for (const finding of result.repositoryFindings ?? []) {
  console.log(finding.title, finding.confirmedInLatestScan);
}

覆盖完整性为 `complete`、`partial` 或 `unknown`。在将扫描结果作为
安全决策依据之前，请审查延后审查的范围、排除项和
待解决的问题。

`result.toJSON()` 返回一个可直接序列化为 JSON 的对象，其中包含清单、代码仓库及当前扫描的发现结果、
覆盖范围、扫描和线程标识符、`reportPath`、`artifactsDir`、
`sarifPath`、成本及轮次元数据。

## 跟踪或取消扫描

传入 `ScanOptions` 回调，以报告扫描启动、工作器进度和
连接重试情况：

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

请传入 `AbortSignal`，以处理由请求、作业控制器
或超时触发的取消操作：

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

扫描中断后，`scanDir` 中可能留下部分输出。需要调查结果时，请保留
该目录。

显示扫描设置进度的应用也可以使用 `ScanOptions` 的
生命周期回调：

| 回调                            | 调用时机                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `onAuthentication(authentication)`  | 扫描选择身份验证方法时。          |
| `onOutputArchived(archiveDir)`      | 现有结果移至归档目录时。      |
| `onOutputDirReady(scanDir)`         | 私有扫描目录准备就绪时。                 |
| `onScanStarted()`                   | 扫描设置完成并开始执行时。           |
| `onTrustedAccessStatus(status)`     | Trusted Access 状态可用时。             |
| `onReconnect(attempt, maxAttempts)` | SDK 重试已断开连接的扫描流时。          |
| `onActivity(activity)`              | 命令、工具、推理步骤或消息发生更新时。 |
| `onProgress(progress)`              | 扫描阶段或已审查文件数量发生变化时。       |
| `onWorkerStatus(status)`            | 工作器的预检或分派状态发生变化时。         |
| `onSessionEvent(session)`           | 扫描会话或工作器会话发出事件时。             |
| `onCost(cost)`                      | 更新后的扫描成本估算值可用时。         |
| `onWarning(warning)`                | 扫描发出警告时。                          |
| `onObserverError(observer, error)`  | 另一个扫描生命周期回调引发错误时。     |

Trusted Access 状态为 `granted`、`not_granted` 或 `unknown`。访问权限缺失
或未知时，也会触发 `onWarning`。

`onSessionEvent` 接收未经脱敏的事件，其中可能包含源代码
或凭据。在将其发送到共享日志或其他服务
之前，请先进行过滤。

## 配置运行时和凭据

需要特定插件、解释器或
Codex 设置时，请传入运行时配置：

```ts
const security = new CodexSecurity({
  pluginPath: "/path/to/codex-security-plugin",
  pythonPath: "/path/to/python",
  codexOverrides: {
    model: "gpt-5.6-terra",
    model_reasoning_effort: "high",
  },
});

`pluginPath` 接受插件目录或 ZIP 文件。`pythonPath` 用于选择
插件解释器。`codexOverrides` 将受支持的值合并到隔离的
Codex 配置中。扫描默认使用 `gpt-5.6-sol`，推理强度
为极高。在 `codexOverrides` 中设置 `model` 和 `model_reasoning_effort`，即可使用
其他模型或推理强度。若要使用 [Amazon
Bedrock](/zh-Hans/codex/security/cli/reference#use-amazon-bedrock)，请
在 `codexOverrides` 中设置 `model_provider` 和 `model`。

`codexOverrides` 无法限制扫描对文件系统的访问，也无法更改其
审批策略。请参阅[本地扫描
权限](/zh-Hans/codex/security/cli/reference#local-scan-permissions)。

对于 OpenRouter 或 Fireworks，还需提供对应的 API 密钥，并在
`codexOverrides` 中提供完整的提供商配置。例如，请设置
`OPENROUTER_API_KEY` 并配置 OpenRouter：

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

对于 Fireworks，请将两个 `openrouter` 键都改为 `fireworks`，将 `name` 设置为
`Fireworks AI`，将 `env_key` 设置为 `FIREWORKS_API_KEY`，使用
`https://api.fireworks.ai/inference/v1` 作为 `base_url`，并选择 Fireworks
模型。

客户端还提供受支持的身份验证方法：

| 方法                     | 用途                                                     |
| -------------------------- | ----------------------------------------------------------- |
| `loginApiKey(apiKey)`      | 使用 API 密钥对隔离运行时进行身份验证。          |
| `loginChatGPT()`           | 启动浏览器登录流程并返回登录句柄。     |
| `loginChatGPTDeviceCode()` | 启动设备代码登录流程并返回登录句柄。 |
| `account()`                | 返回当前身份验证状态。                    |
| `logout()`                 | 清除隔离环境中的身份验证信息。                              |

登录句柄提供 `waitForInstructions`、`authUrl`、`verificationUrl`、
`userCode`、`wait` 和 `cancel`，使应用能够展示并完成
所选的登录流程。SDK 可以复用存储在文件中的 Codex 登录信息。API 密钥
适合用于 CI 和服务器端自动化。

当 API 密钥和已存储的登录信息均可用时，SDK 默认使用 API
密钥。若要改用您的 ChatGPT 登录信息，请为扫描选择该登录方式：

```ts
const result = await security.run("/path/to/repository", {
  auth: "chatgpt",
});

设置 `auth: "api-key"`，以要求使用环境中的 API 密钥。`preflight` 也接受
相同的 `auth` 选项。

## 处理扫描错误

捕获与您的应用可以采取的
操作相匹配的导出错误类：

| 错误                            | 含义                                                            |
| -------------------------------- | ------------------------------------------------------------------ |
| `AuthenticationRequiredError`    | 扫描需要受支持的凭据。                               |
| `ConfigurationError`             | Codex 配置或覆盖设置不符合要求。                  |
| `InvalidTargetError`             | 代码仓库、路径、模式或 Git 目标不符合要求。           |
| `OutputDirectoryError`           | 输出位置或其权限不符合要求。             |
| `OutputInsideProtectedRootError` | 输出目录位于被扫描的代码仓库或工作树内。 |
| `PluginPythonUnavailableError`   | 没有可用的 Python 解释器。                        |
| `PluginBootstrapError`           | 插件运行时无法启动。                                |
| `ScanCostLimitExceededError`     | 扫描超过了预估成本上限。                        |
| `IncompleteScanError`            | 扫描在生成所需结果之前结束。               |
| `ContractValidationError`        | 已完成的扫描返回了结构化契约错误。             |
| `ScanInterruptedError`           | 扫描因中断而停止，并且可能留下了部分输出。 |

接下来，请参阅 [CLI 快速入门](/zh-Hans/codex/security/cli)、[CI
指南](/zh-Hans/codex/security/cli/ci)或 [CLI
参考资料](/zh-Hans/codex/security/cli/reference)。
