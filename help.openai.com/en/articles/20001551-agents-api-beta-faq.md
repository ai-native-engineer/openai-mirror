<!-- source: https://help.openai.com/en/articles/20001551-agents-api-beta-faq -->

# Agents API (beta) FAQ

Get started with managed agent sessions, execution environments, usage, and data controls.

The Agents API is available in beta. It lets developers build applications with an OpenAI-managed Codex agent that can work across multiple steps and continue in the same session.

Your application supplies the task, tools, and configuration. OpenAI manages the agent’s session and the coordination between its model and tools.

# What can an agent do?

Depending on its tools and execution environment, an agent can run code, edit files, use MCP connections, and produce files for your application. You can send additional instructions or continue with another task in the same session.

See the [Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview) for supported capabilities and examples.

# How do I get started?

1. Create an application API key in your OpenAI Platform project. Grant `api.agents.read` and `api.agents.write` for sessions, plus `api.responses.write` for model requests.
2. Follow the [quickstart](https://developers.openai.com/api/docs/guides/agents-api/quickstart) to configure an agent, create a session, and submit a task.
3. Follow the session’s events to review progress and results. Save the session ID if you want to continue the work.

Keep your API key outside the agent’s sandbox. Requests require the `OpenAI-Beta: agents=v1` header. OpenAI SDKs add this header automatically.

# Does my agent need a sandbox?

Choose the environment that fits the task:

* **No environment:** The agent answers questions or uses external tools without needing built-in shell commands or workspace files.
* **OpenAI-hosted sandbox:** The agent needs to run scripts or work with files, and you want OpenAI to manage its sandbox.
* **Self-hosted sandbox:** You need your own infrastructure, software, or private network. Your application manages the environment’s lifecycle.

See [Agents API architecture](https://developers.openai.com/api/docs/guides/agents-api/architecture) for configuration details.

# Where can I review a session?

Open [Logs in the Platform dashboard](https://platform.openai.com/logs?api=agents), select **Agents**, and search for the session ID. You can inspect turns, tool calls, and subagent activity.

The [observability guide](https://developers.openai.com/api/docs/guides/agents-api/observability) also explains how to review recorded token usage.

# What if the event stream disconnects?

Retrieve the existing session and its saved items before retrying. This helps you check what happened before submitting more work.

A completed turn does not mean every tool succeeded. Review the reported result. An idle session alone does not establish that the task finished successfully.

# How is usage billed?

Model requests use the selected model’s API rates. OpenAI tools and OpenAI-hosted sandboxes use their applicable tool and container rates.

See [API pricing](https://developers.openai.com/api/docs/pricing) for current rates.

# How are session data and files handled?

The Agents API retains session state so work can continue across turns. You can delete sessions and published artifacts when they are no longer needed. Save any files you need before deleting a session.

The Agents API currently supports data residency in the United States only. It does not support Zero Data Retention, including when you use a self-hosted sandbox. See the [Agents API documentation](https://developers.openai.com/api/docs/guides/agents-api/overview) for data-control details.
