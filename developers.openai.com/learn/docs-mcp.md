<!-- source: https://developers.openai.com/learn/docs-mcp/ -->

## Search developer resources

OpenAI hosts a public Model Context Protocol (MCP) server for developer documentation on developers.openai.com and platform.openai.com.

**Server URL (streamable HTTP):** `https://developers.openai.com/mcp`

## What it provides

* Read-only access to OpenAI developer documentation (search + page content).
* A way to pull documentation into your agent’s context while you work.

This MCP server is documentation-only. It does not call the OpenAI API on your
behalf.

## Quickstart

Choose an option 

CodexVS CodeCursorClaude Code

You can connect Codex to [MCP servers](/codex/mcp) in the [CLI](/codex/cli) or [IDE extension](/codex/ide). The configuration is shared between both so you only have to set it up once.

Add the server using the Codex CLI:

codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp

Verify it’s configured:

codex mcp list

Alternatively, you can add it in `~/.codex/config.toml` directly:

[mcp_servers.openaiDeveloperDocs]
url = "https://developers.openai.com/mcp"

To have Codex reliably use the MCP server, add this snippet to your `AGENTS.md`:

Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.

VS Code supports MCP servers when using GitHub Copilot in Agent mode.

Click the following link to add the Docs MCP to VS Code:

[Install in VS Code](vscode:mcp/install?%7B%22name%22%3A%20%22openaiDeveloperDocs%22%2C%20%22type%22%3A%20%22http%22%2C%20%22url%22%3A%20%22https%3A//developers.openai.com/mcp%22%7D)

Alternatively, you can manually add a `.vscode/mcp.json` in your project root:

  "servers": {
    "openaiDeveloperDocs": {
      "type": "http",
      "url": "https://developers.openai.com/mcp"

To have VS Code reliably use the MCP server, add this snippet to your `AGENTS.md`:

Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.

Open Copilot Chat, switch to **Agent** mode, enable the server in the tools picker, and ask an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

Cursor has native MCP support and reads configuration from `mcp.json`.

Install with Cursor:

[Install in Cursor](https://cursor.com/en-US/install-mcp?name=openaiDeveloperDocs&config=eyJ1cmwiOiAiaHR0cHM6Ly9kZXZlbG9wZXJzLm9wZW5haS5jb20vbWNwIn0%3D)

Alternatively, create a `~/.cursor/mcp.json` (macOS/Linux) and add:

  "mcpServers": {
    "openaiDeveloperDocs": {
      "url": "https://developers.openai.com/mcp"

To have Cursor reliably use the MCP server, add this snippet to your `AGENTS.md`:

Always use the OpenAI developer documentation MCP server if you need to work with the OpenAI API, ChatGPT Apps SDK, Codex,… without me having to explicitly ask.

Restart Cursor and ask Cursor’s agent an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

Claude Code supports remote HTTP MCP servers through the `claude mcp` CLI.

Add the Docs MCP server from the project where you use Claude Code:

claude mcp add --transport http openaiDeveloperDocs https://developers.openai.com/mcp

Verify it’s configured:

claude mcp list

To make the server available across all Claude Code projects on your machine, add it with user scope:

claude mcp add --transport http --scope user openaiDeveloperDocs https://developers.openai.com/mcp

In Claude Code, run `/mcp` to confirm the server is connected. Then ask an OpenAI-related question like:

> Look up the request schema for Responses API tools in the OpenAI developer docs and summarize the required fields.

## Tips

* If you don’t have the snippet in the AGENTS.md file, you need to explicitly tell your agent to consult the Docs MCP server for the answer.
* If you have more than one MCP server, keep server names short and descriptive to aid the agent in selecting the server.

## OpenAI Docs Skill

If you use skills in your AI tooling, pair this MCP server with the
[OpenAI Docs Skill](https://github.com/openai/skills/blob/main/skills/.curated/openai-docs/SKILL.md).
It tells the agent to use Docs MCP tools first for OpenAI questions, then fall back to official OpenAI domains.

1. Install the skill from the [OpenAI skills repository](https://github.com/openai/skills).
2. Confirm you configured this Docs MCP server at `https://developers.openai.com/mcp`.
3. Enable the skill for your project or session in your agent tooling.
4. Ask OpenAI product/API questions and request citations so answers stay traceable to docs sources.
