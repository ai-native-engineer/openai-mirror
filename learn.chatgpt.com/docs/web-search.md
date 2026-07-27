<!-- source: https://learn.chatgpt.com/docs/web-search -->

OverviewFeaturesConfigurationDevelopersSecurityAdministrationUse CasesResourcesDocs sectionFeatures

![](/images/codex/surface-icons/chatgpt-app.webp)ChatGPT desktop app

ChatGPT includes a first-party web search tool. Treat all web results as
untrusted input.

In the ChatGPT desktop app, ask for current information in a chat. ChatGPT records
search activity with the other tool calls in the transcript.

In ChatGPT web, ask for current information or sources. Search results and
citations appear in the chat when ChatGPT uses web search. Workspace
settings can limit whether search is available.

In the CLI, pass `--search` to fetch live results for one run:

```
codex --search "Summarize the latest release notes for this dependency"
```

Searches appear as `web_search` items in the interactive transcript and in
`codex exec --json` output.

In the IDE extension, ask Codex to search while you work in the editor. The
extension uses the connected Codex host’s search mode. Search activity appears
in the chat transcript.

## Configure local web search

For local Codex chats, Codex enables cached search by default. Cached mode uses
an OpenAI-maintained index instead of fetching arbitrary pages live, which
lowers—but doesn’t remove—prompt injection risk.

Use live search when your task depends on the latest information. Set
`web_search = "live"` in `config.toml`. Set `web_search = "disabled"` to turn
the tool off. The `"indexed"` mode permits external web access only when the
search index gates the request. When Codex runs with full access, web search
defaults to live results. See [Config basics](/codex/config-file/config-basic)
for config file locations and precedence.

For network boundaries that apply to Codex cloud environments, see [Internet
access](/codex/cloud/internet-access).
