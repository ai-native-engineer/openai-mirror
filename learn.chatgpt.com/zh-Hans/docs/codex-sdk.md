<!-- source: https://learn.chatgpt.com/zh-Hans/docs/codex-sdk -->

如果您通过 Codex CLI、IDE 扩展或 Codex 云端使用 Codex，也可以以编程方式控制它。

当您需要执行以下操作时，请使用 SDK：

- 在您的 CI/CD 流水线中控制 Codex
- 创建自己的智能体，让它与 Codex 交互以执行复杂的工程任务
- 将 Codex 集成到您自己的内部工具和工作流中
- 将 Codex 集成到您自己的应用中

使用 Codex SDK 自动执行编码任务，包括 CI 中的作业。使用 [Codex App Server](/zh-Hans/codex/app-server) 构建自定义客户端，以处理身份验证、对话历史记录、审批以及流式传输的智能体事件。

`codex mcp-server` 已弃用。现有集成仍可参考 [MCP 服务器指南](/zh-Hans/codex/mcp-server)。

如果您拥有 Beta 版访问权限，并需要扫描代码仓库或变更以获取结构化的
安全扫描结果和覆盖范围信息，请使用 [Codex Security TypeScript
SDK](/zh-Hans/codex/security/sdk)。

## TypeScript 库

TypeScript 库让您的应用能够启动、继续和恢复本地 Codex 线程。

请在服务器端使用该库；它需要 Node.js 18 或更高版本。

### 安装

首先，请使用 `npm` 安装 Codex SDK：

```bash
npm install @openai/codex-sdk

### 用法

在 Codex 中启动一个线程，并使用您的提示运行该线程。

```ts

const codex = new Codex();
const thread = codex.startThread();
const result = await thread.run(
  "Make a plan to diagnose and fix the CI failures"
);

console.log(result.finalResponse);

再次调用 `run()` 可继续同一线程；您也可以提供线程 ID 来恢复之前的线程。

```ts
// running the same thread
const result = await thread.run("Implement the plan");

console.log(result.finalResponse);

// resuming past thread

const threadId = "<thread-id>";
const thread2 = codex.resumeThread(threadId);
const result2 = await thread2.run("Pick up where you left off");

console.log(result2.finalResponse);

有关更多详细信息，请参阅 [TypeScript 代码仓库](https://github.com/openai/codex/tree/main/sdk/typescript)。

## Python 库

Python SDK 通过 JSON-RPC 控制本地 Codex app-server。它需要 Python 3.10 或更高版本。已发布的 SDK 构建版本包含固定版本的 Codex CLI 运行时依赖项。

### 安装

要安装 SDK，请运行：

```bash
pip install openai-codex

已发布的 SDK 构建版本会自动使用各自固定版本的运行时。仅当您有意改用某个特定的本地 Codex 可执行文件时，才传入 `CodexConfig(codex_bin=...)`。

Python SDK 已发布稳定版。`pip install openai-codex`
会安装最新的稳定版。使用 `pip install --pre openai-codex` 可选择
使用更新的预发布构建版本。

### 用法

启动 Codex，创建一个线程，然后运行提示：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(
        model="gpt-5.6-terra",
        sandbox=Sandbox.workspace_write,
    )
    result = thread.run("Make a plan to diagnose and fix the CI failures")
    print(result.final_response)

如果您的应用已采用异步方式运行，请使用 `AsyncCodex`：

```python

from openai_codex import AsyncCodex

async def main() -> None:
    async with AsyncCodex() as codex:
        thread = await codex.thread_start(model="gpt-5.6-terra")
        result = await thread.run("Implement the plan")
        print(result.final_response)

asyncio.run(main())

### 沙盒预设

创建线程时，或为线程的后续轮次更改文件系统
访问权限时，请使用相同的 `Sandbox` 预设：

```python
from openai_codex import Codex, Sandbox

with Codex() as codex:
    thread = codex.thread_start(sandbox=Sandbox.workspace_write)
    thread.run("Make the requested change.")
    review = thread.run("Review the diff only.", sandbox=Sandbox.read_only)

可用预设：

- `Sandbox.read_only`：读取文件，但不允许写入。
- `Sandbox.workspace_write`：读取文件，并可在工作空间及已配置的可写根目录中写入。
- `Sandbox.full_access`：在不受文件系统访问限制的情况下运行。

省略 `sandbox=` 时，app-server 会使用其配置的默认值。将沙盒设置
传入 `run(...)` 或 `turn(...)` 后，该设置会应用于该轮次及
同一线程中的后续轮次。

有关更多详细信息，请参阅 [Python 代码仓库](https://github.com/openai/codex/tree/main/sdk/python)。
