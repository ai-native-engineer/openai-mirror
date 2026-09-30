<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/methods/create/ -->

## Create an agent

`beta.agents.create(AgentCreateParams**kwargs)  -> Agent`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

- `model: str`

  The model to use for the agent. The requested model name is preserved.

- `instructions: Optional[str]`

  Additional instructions appended to the agent's default base instructions. Omit or set to null to add no custom instructions.

- `metadata: Optional[Dict[str, str]]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `multi_agent: Optional[MultiAgentConfigParam]`

  Configuration for creating and coordinating subagents. Subagent tools are disabled by default.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Optional[int]`

    Maximum number of subagents that may run concurrently. Defaults to 6.

- `name: Optional[str]`

  A human-readable name for the agent. Omission or null leaves the agent unnamed.

- `reasoning: Optional[AgentReasoningParam]`

  Configuration for model reasoning. Omission uses the model's default effort.

  - `effort: Optional[Literal["none", "minimal", "low", 4 more]]`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `"none"`

    - `"minimal"`

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `summary: Optional[Literal["concise", "detailed", "auto"]]`

    Controls whether the response includes a reasoning summary.

    - `"concise"`

      Returns a concise reasoning summary when supported.

    - `"detailed"`

      Returns a detailed reasoning summary when supported.

    - `"auto"`

      Automatically selects the most detailed summary supported by the model.

- `service_tier: Optional[Literal["auto", "default", "flex", 3 more]]`

  The service tier used for model requests. Defaults to `auto`.

  - `"auto"`

    Selects the service tier automatically.

  - `"default"`

    Uses the default service tier.

  - `"flex"`

    Uses the flex service tier.

  - `"priority"`

    Uses the priority service tier.

  - `"fast"`

    Uses the fast service tier.

  - `"ultrafast"`

    Uses the ultrafast service tier.

- `text: Optional[AgentTextParam]`

  Configuration for generated text. Defaults to the `text` format and medium verbosity.

  - `format: Optional[TextFormatParam]`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `class TextFormatParamText: …`

      Generates ordinary text without a structured-output constraint.

      - `type: Literal["text"]`

        The type of the object. Always `text`.

        - `"text"`

    - `class TextFormatParamJSONSchema: …`

      Constrains generated text to a JSON Schema.

      - `schema: Dict[str, object]`

        The JSON Schema that generated text must match.

      - `type: Literal["json_schema"]`

        The type of the object. Always `json_schema`.

        - `"json_schema"`

  - `verbosity: Optional[Literal["low", "medium", "high"]]`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `"low"`

      Produces less text.

    - `"medium"`

      Uses the default amount of text.

    - `"high"`

      Produces more text.

- `tools: Optional[Iterable[PersistedAgentToolParam]]`

  Tools available to the agent. Defaults to an empty list.

  - `class PersistedAgentToolConfigParamFunction: …`

    A function defined by the application.

    - `description: str`

      A description of what the function does.

    - `name: str`

      The name of the function.

    - `parameters: Dict[str, object]`

      A JSON Schema object describing the function's arguments.

    - `type: Literal["function"]`

      The type of the object. Always `function`.

      - `"function"`

    - `defer_loading: Optional[bool]`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `class PersistedAgentToolConfigParamToolSearch: …`

    Discovers deferred function tools and loads them into the model context.

    - `type: Literal["tool_search"]`

      The type of the object. Always `tool_search`.

      - `"tool_search"`

  - `class PersistedAgentToolConfigParamProgrammaticToolCalling: …`

    Enables calling tools from model-generated code.

    - `type: Literal["programmatic_tool_calling"]`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

    - `enabled: Optional[bool]`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class PersistedAgentToolConfigParamMcp: …`

    Tools provided by a remote MCP server without stored credentials.

    - `server_label: str`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransportParam`

      The credential-free transport used to connect to the MCP server.

      - `class PersistedMcpTransportConfigParamHTTP: …`

        Connects to an MCP server over HTTP.

        - `server_url: str`

          The URL of the MCP server.

        - `type: Literal["http"]`

          The type of the object. Always `http`.

          - `"http"`

        - `headers: Optional[Dict[str, str]]`

          Non-secret HTTP headers sent to the MCP server.

      - `class PersistedMcpTransportConfigParamStdio: …`

        Starts an MCP server as a local process.

        - `command: str`

          The command used to start the MCP server.

        - `cwd: str`

          The working directory used to start the MCP server.

        - `type: Literal["stdio"]`

          The type of the object. Always `stdio`.

          - `"stdio"`

        - `args: Optional[List[str]]`

          Arguments passed to the MCP server command.

        - `env_vars: Optional[List[str]]`

          Environment variable names to inherit from the selected execution environment.

    - `type: Literal["mcp"]`

      The type of the object. Always `mcp`.

      - `"mcp"`

    - `allowed_tools: Optional[List[str]]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: Optional[Literal["service", "environment"]]`

      Selects where outbound MCP HTTP connections originate.

      - `"service"`

        Uses the Managed Agents service network.

      - `"environment"`

        Uses the session's execution environment.

    - `credential_id: Optional[str]`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Optional[Dict[str, object]]`

      Metadata included with requests to this MCP server.

    - `required: Optional[bool]`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class PersistedAgentToolConfigParamWebSearch: …`

    Web search.

    - `type: Literal["web_search"]`

      The type of the object. Always `web_search`.

      - `"web_search"`

    - `allowed_domains: Optional[List[str]]`

      Domains the search may include.

    - `context_size: Optional[Literal["low", "medium", "high"]]`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location: Optional[PersistedAgentToolConfigParamWebSearchLocation]`

      Approximate location used to localize search results.

      - `city: Optional[str]`

        The city name.

      - `country: Optional[str]`

        The two-letter ISO country code, such as `US`.

      - `region: Optional[str]`

        The region or state name.

      - `timezone: Optional[str]`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: Optional[Literal["disabled", "cached", "live"]]`

      The source used for web search results. Defaults to `live`.

      - `"disabled"`

        Disables web search.

      - `"cached"`

        Uses cached search results.

      - `"live"`

        Searches the live web.

  - `class PersistedAgentToolConfigParamComputerUse: …`

    Browser use in an OpenAI-hosted session.

    - `type: Literal["computer_use"]`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

    - `include_screenshots: Optional[bool]`

      Whether computer tool outputs include screenshots. Defaults to `false`.

- `class Agent: …`

  A reusable agent scoped to the caller's project.

  - `id: str`

    The ID of the reusable agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: Optional[str]`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the agent.

  - `model: str`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Optional[int]`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: Optional[str]`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: Literal["agent"]`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: Optional[Literal["none", "minimal", "low", 4 more]]`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: Optional[Literal["concise", "detailed", "auto"]]`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: Literal["auto", "default", "flex", 3 more]`

    The resolved service-tier policy used for model requests.

    - `"auto"`

    - `"default"`

    - `"flex"`

    - `"priority"`

    - `"fast"`

    - `"ultrafast"`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class TextFormatResourceText: …`

        Generates ordinary text without a structured-output constraint.

        - `type: Literal["text"]`

          The type of the object. Always `text`.

          - `"text"`

      - `class TextFormatResourceJSONSchema: …`

        Constrains generated text to a JSON Schema.

        - `schema: Dict[str, object]`

          The JSON Schema that generated text must match.

        - `type: Literal["json_schema"]`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: Literal["low", "medium", "high"]`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: List[PersistedAgentTool]`

    Tools available to the agent.

    - `class PersistedAgentToolResourceFunction: …`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: str`

        A description of what the function does.

      - `name: str`

        The name of the function.

      - `parameters: Dict[str, object]`

        A JSON Schema object describing the function's arguments.

      - `type: Literal["function"]`

        The type of the object. Always `function`.

        - `"function"`

    - `class PersistedAgentToolResourceToolSearch: …`

      Discovers deferred function tools and loads them into the model context.

      - `type: Literal["tool_search"]`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `class PersistedAgentToolResourceProgrammaticToolCalling: …`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: Literal["programmatic_tool_calling"]`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `class PersistedAgentToolResourceMcp: …`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Optional[List[str]]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: Literal["service", "environment"]`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: Optional[str]`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Dict[str, object]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: str`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class PersistedMcpTransportResourceHTTP: …`

          Connects to an MCP server over HTTP.

          - `headers: Dict[str, str]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: str`

            The URL of the MCP server.

          - `type: Literal["http"]`

            The type of the object. Always `http`.

            - `"http"`

        - `class PersistedMcpTransportResourceStdio: …`

          Starts an MCP server as a local process.

          - `args: List[str]`

            Arguments passed to the MCP server command.

          - `command: str`

            The command used to start the MCP server.

          - `cwd: str`

            The working directory used to start the MCP server.

          - `env_vars: List[str]`

            Environment variable names inherited from the execution environment.

          - `type: Literal["stdio"]`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: Literal["mcp"]`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `class PersistedAgentToolResourceWebSearch: …`

      Web search.

      - `allowed_domains: Optional[List[str]]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: Literal["low", "medium", "high"]`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Optional[PersistedAgentToolResourceWebSearchLocation]`

        Approximate location used to localize search results, if provided.

        - `city: Optional[str]`

          The city name.

        - `country: Optional[str]`

          The two-letter ISO country code, such as `US`.

        - `region: Optional[str]`

          The region or state name.

        - `timezone: Optional[str]`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: Literal["disabled", "cached", "live"]`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: Literal["web_search"]`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `class PersistedAgentToolResourceComputerUse: …`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: Literal["computer_use"]`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the agent was last updated.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
agent = client.beta.agents.create(
    model="model",
print(agent.id)

  "instructions": "instructions",
  "metadata": {
    "foo": "string"
  "model": "model",
  "multi_agent": {
    "enabled": true,
    "max_concurrent_subagents": 1
  "object": "agent",
  "reasoning": {
    "effort": "none",
    "summary": "concise"
  "service_tier": "auto",
  "text": {
    "format": {
      "type": "text"
    "verbosity": "low"
  "tools": [
      "defer_loading": true,
      "description": "description",
      "parameters": {
        "foo": "bar"
      "type": "function"
  "updated_at": 0
