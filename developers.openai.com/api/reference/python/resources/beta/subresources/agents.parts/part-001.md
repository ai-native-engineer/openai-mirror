<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

# Agents

## Create an agent

`beta.agents.create(AgentCreateParams**kwargs)  -> Agent`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent = client.beta.agents.create(
    model="model",
)
print(agent.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "instructions": "instructions",
  "metadata": {
    "foo": "string"
  },
  "model": "model",
  "multi_agent": {
    "enabled": true,
    "max_concurrent_subagents": 1
  },
  "name": "name",
  "object": "agent",
  "reasoning": {
    "effort": "none",
    "summary": "concise"
  },
  "service_tier": "auto",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  "tools": [
    {
      "defer_loading": true,
      "description": "description",
      "name": "name",
      "parameters": {
        "foo": "bar"
      },
      "type": "function"
    }
  ],
  "updated_at": 0
}
```

## Delete an agent

`beta.agents.delete(stragent_id)  -> AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: str`

### Returns

- `class AgentDeleted: …`

  A deleted reusable agent.

  - `id: str`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: Literal["agent.deleted"]`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent_deleted = client.beta.agents.delete(
    "agent_id",
)
print(agent_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.deleted"
}
```

## List agents

`beta.agents.list(AgentListParams**kwargs)  -> SyncCursorPage[Agent]`

**get** `/agents`

Lists reusable agents in the current project. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "instructions": "instructions",
      "metadata": {
        "foo": "string"
      },
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
      "name": "name",
      "object": "agent",
      "reasoning": {
        "effort": "none",
        "summary": "concise"
      },
      "service_tier": "auto",
      "text": {
        "format": {
          "type": "text"
        },
        "verbosity": "low"
      },
      "tools": [
        {
          "defer_loading": true,
          "description": "description",
          "name": "name",
          "parameters": {
            "foo": "bar"
          },
          "type": "function"
        }
      ],
      "updated_at": 0
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent

`beta.agents.retrieve(stragent_id)  -> Agent`

**get** `/agents/{agent_id}`

Retrieves a reusable agent by ID. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: str`

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent = client.beta.agents.retrieve(
    "agent_id",
)
print(agent.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "instructions": "instructions",
  "metadata": {
    "foo": "string"
  },
  "model": "model",
  "multi_agent": {
    "enabled": true,
    "max_concurrent_subagents": 1
  },
  "name": "name",
  "object": "agent",
  "reasoning": {
    "effort": "none",
    "summary": "concise"
  },
  "service_tier": "auto",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  "tools": [
    {
      "defer_loading": true,
      "description": "description",
      "name": "name",
      "parameters": {
        "foo": "bar"
      },
      "type": "function"
    }
  ],
  "updated_at": 0
}
```

## Update an agent

`beta.agents.update(stragent_id, AgentUpdateParams**kwargs)  -> Agent`

**post** `/agents/{agent_id}`

Updates a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: str`

- `instructions: Optional[str]`

  Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

- `metadata: Optional[Dict[str, str]]`

  Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

- `model: Optional[str]`

  The model to use for the agent. The requested model name is preserved.

- `multi_agent: Optional[MultiAgentConfigParam]`

  Configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Optional[int]`

    Maximum number of subagents that may run concurrently. Defaults to 6.

- `name: Optional[str]`

  A replacement name. Omit to leave unchanged, or pass null to clear it.

- `reasoning: Optional[AgentReasoningParam]`

  Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

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

  The service tier used for model requests.

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

  Configuration for text generated by the agent.

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

  Tools available to the agent.

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

### Returns

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

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent = client.beta.agents.update(
    agent_id="agent_id",
)
print(agent.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "instructions": "instructions",
  "metadata": {
    "foo": "string"
  },
  "model": "model",
  "multi_agent": {
    "enabled": true,
    "max_concurrent_subagents": 1
  },
  "name": "name",
  "object": "agent",
  "reasoning": {
    "effort": "none",
    "summary": "concise"
  },
  "service_tier": "auto",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  "tools": [
    {
      "defer_loading": true,
      "description": "description",
      "name": "name",
      "parameters": {
        "foo": "bar"
      },
      "type": "function"
    }
  ],
  "updated_at": 0
}
```

## Domain Types

### Agent

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

### Agent Browser Authentication Cancel Param

- `class AgentBrowserAuthenticationCancelParam: …`

  - `action: Literal["cancel"]`

    - `"cancel"`

  - `type: Literal["browser_authentication"]`

    - `"browser_authentication"`

### Agent Browser Authentication Submit Param

- `class AgentBrowserAuthenticationSubmitParam: …`

  - `action: Literal["submit"]`

    - `"submit"`

  - `fields: List[Field]`

    Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

    - `field_id: str`

      The field ID from the required action.

    - `value: str`

      The value to enter into the registered control.

  - `type: Literal["browser_authentication"]`

    - `"browser_authentication"`

  - `selected_option: Optional[str]`

    The chosen method. Required when the required action contains options.

### Agent Browser Origin Access Param

- `class AgentBrowserOriginAccessParam: …`

  - `decision: Literal["approve", "deny", "cancel"]`

    Whether to allow, deny, or cancel the requested origin access.

    - `"approve"`

      Allow the browser to access this origin.

    - `"deny"`

      Deny access to this origin.

    - `"cancel"`

      Dismiss this request without approving access.

  - `type: Literal["browser_origin_access"]`

    - `"browser_origin_access"`

### Agent Close Subagent Call Item

- `class AgentCloseSubagentCallItem: …`

  A request to close a subagent.

  - `id: str`

    The ID of the tool call item.

  - `recipient_agent_id: str`

    The ID of the agent to close.

  - `sender_agent_id: str`

    The ID of the agent requesting the close.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["close_subagent_call"]`

    The item type. Always `close_subagent_call`.

    - `"close_subagent_call"`

      The current public item type.

### Agent Command Execution Item

- `class AgentCommandExecutionItem: …`

  A command execution produced by the agent.

  - `id: str`

    The ID of the command execution item.

  - `command: str`

    The command that was executed.

  - `cwd: Optional[str]`

    The working directory used to execute the command.

  - `duration_ms: Optional[int]`

    The command duration in milliseconds.

  - `exit_code: Optional[int]`

    The process exit code, if the command completed.

  - `output: Optional[str]`

    The command output, if available.

  - `status: AgentFunctionCallStatus`

    The status of the command execution.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["command_execution"]`

    The item type. Always `command_execution`.

    - `"command_execution"`

### Agent Content

- `AgentContent`

  A plaintext or encrypted content part exchanged between agents.

  - `class OutputText: …`

    A text content part produced by the agent.

    - `text: str`

      The text produced by the agent.

    - `type: Literal["output_text"]`

      The content type. Always `output_text`.

      - `"output_text"`

  - `class EncryptedContentResource: …`

    Encrypted content exchanged between agents.

    - `encrypted_content: str`

      The encrypted content payload.

    - `type: Literal["encrypted_content"]`

      The content type. Always `encrypted_content`.

      - `"encrypted_content"`

### Agent Create Subagent Call Item

- `class AgentCreateSubagentCallItem: …`

  A request to spawn a subagent.

  - `id: str`

    The ID of the tool call item.

  - `agent_id: str`

    The ID of the agent that requested the subagent.

  - `content: List[AgentContent]`

    The task given to the spawned agent.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `model: Optional[str]`

    The model requested for the spawned agent.

  - `reasoning_effort: Optional[str]`

    The reasoning effort requested for the spawned agent.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["create_subagent_call"]`

    The item type. Always `create_subagent_call`.

    - `"create_subagent_call"`

      The current public item type.

### Agent Deleted

- `class AgentDeleted: …`

  A deleted reusable agent.

  - `id: str`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: Literal["agent.deleted"]`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

### Agent Function Call Item

- `class AgentFunctionCallItem: …`

  A function call produced by the agent.

  - `id: str`

    The ID of the function call item.

  - `arguments: object`

    The arguments to pass to the function.

  - `call_id: str`

    The ID used to submit the function result.

  - `name: str`

    The name of the function to call.

  - `status: AgentFunctionCallStatus`

    The status of the function call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["function_call"]`

    The item type. Always `function_call`.

    - `"function_call"`

### Agent Function Call Output

- `Union[str, List[InputContent]]`

  The text or model-input content supplied as a function result.

  - `str`

  - `List[InputContent]`

    - `class InputContentResourceInputText: …`

      Text input recorded in a session item.

      - `text: str`

        The text supplied to the agent.

      - `type: Literal["input_text"]`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `class InputContentResourceInputImage: …`

      Image input recorded in a session item.

      - `image_url: str`

        The URL of the image supplied to the agent, which may be a base64-encoded data URL.

      - `type: Literal["input_image"]`

        The type of the object. Always `input_image`.

        - `"input_image"`

### Agent Function Call Output Param

- `Union[str, List[InputContentParam]]`

  A function result represented as text or supported model-input content.

  - `str`

  - `List[InputContentParam]`

    - `class InputContentParamInputText: …`

      Text input to the model.

      - `text: str`

        The text sent to the model.

      - `type: Literal["input_text"]`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `class InputContentParamInputImage: …`

      Image input to the model.

      - `image_url: str`

        The URL of the image sent to the model.

      - `type: Literal["input_image"]`

        The type of the object. Always `input_image`.

        - `"input_image"`

### Agent Function Call Status

- `Literal["in_progress", "completed", "failed", "incomplete"]`

  The status of a tool call.

  - `in_progress` - The call is in progress.
  - `completed` - The call completed successfully.
  - `failed` - The call failed.
  - `incomplete` - The call stopped before completing.

  - `"in_progress"`

    The call is in progress.

  - `"completed"`

    The call completed successfully.

  - `"failed"`

    The call failed.

  - `"incomplete"`

    The call stopped before completing.

### Agent Interrupt Subagent Call Item

- `class AgentInterruptSubagentCallItem: …`

  A request to interrupt a subagent's current turn. The subagent remains available.

  - `id: str`

    The ID of the tool call item.

  - `recipient_agent_id: str`

    The ID of the agent to interrupt.

  - `sender_agent_id: str`

    The ID of the agent requesting the interrupt.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["interrupt_subagent_call"]`

    The item type. Always `interrupt_subagent_call`.

    - `"interrupt_subagent_call"`

      The current public item type.

### Agent Mcp Call Item

- `class AgentMcpCallItem: …`

  A call to a tool on an MCP server.

  - `id: str`

    The ID of the MCP call item.

  - `arguments: object`

    The arguments passed to the MCP tool.

  - `error: object`

    The error returned by the MCP tool, if any.

  - `name: str`

    The name of the MCP tool.

  - `output: object`

    The output returned by the MCP tool, if any.

  - `server_label: str`

    The label of the MCP server.

  - `status: AgentFunctionCallStatus`

    The status of the MCP tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["mcp_call"]`

    The item type. Always `mcp_call`.

    - `"mcp_call"`

### Agent Output Command Execution Output Delta Event

- `class AgentOutputCommandExecutionOutputDeltaEvent: …`

  Emitted when command execution produces an output delta.

  - `delta: str`

    The output text that was appended.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the command execution item.

  - `output_index: int`

    The index of the item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.output.command_execution_output.delta"]`

    The type of the object. Always `agent.output.command_execution_output.delta`.

    - `"agent.output.command_execution_output.delta"`

### Agent Output Item

- `AgentOutputItem`

  An output item produced by an agent.

  - `class AgentSessionAssistantMessage: …`

    An assistant message produced by the agent.

    - `id: str`

      The ID of the message.

    - `content: List[OutputText]`

      The content of the message.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of the assistant message.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["assistant"]`

      The role of the message author. Always `assistant`.

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Agent Output Item Status

- `Literal["in_progress", "completed", "incomplete"]`

  The status of an agent output item.

  - `in_progress` - The item is in progress.
  - `completed` - The item is complete.
  - `incomplete` - The item stopped before completing.

  - `"in_progress"`

    The item is in progress.

  - `"completed"`

    The item is complete.

  - `"incomplete"`

    The item stopped before completing.

### Agent Reasoning

- `class AgentReasoning: …`

  The reasoning configuration used by an agent.

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

### Agent Reasoning Item

- `class AgentReasoningItem: …`

  A reasoning item produced by the agent.

  - `id: str`

    The ID of the reasoning item.

  - `status: Optional[AgentOutputItemStatus]`

    The status of the reasoning item.

    - `"in_progress"`

      The item is in progress.

    - `"completed"`

      The item is complete.

    - `"incomplete"`

      The item stopped before completing.

  - `summary: List[SummaryText]`

    The reasoning summaries produced by the agent.

    - `text: str`

      The reasoning summary text.

    - `type: Literal["summary_text"]`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["reasoning"]`

    The item type. Always `reasoning`.

    - `"reasoning"`

### Agent Reasoning Param

- `class AgentReasoningParam: …`

  Reasoning configuration for the agent.

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

### Agent Resume Subagent Call Item

- `class AgentResumeSubagentCallItem: …`

  A request to resume a subagent.

  - `id: str`

    The ID of the tool call item.

  - `recipient_agent_id: str`

    The ID of the agent to resume.

  - `sender_agent_id: str`

    The ID of the agent requesting the resume.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["resume_subagent_call"]`

    The item type. Always `resume_subagent_call`.

    - `"resume_subagent_call"`

      The current public item type.

### Agent Send Subagent Input Call Item

- `class AgentSendSubagentInputCallItem: …`

  A request to send input to another agent.

  - `id: str`

    The ID of the tool call item.

  - `content: List[AgentContent]`

    The input sent to the receiving agent.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `recipient_agent_id: str`

    The ID of the agent receiving the input.

  - `sender_agent_id: str`

    The ID of the agent sending the input.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["send_subagent_input_call"]`

    The item type. Always `send_subagent_input_call`.

    - `"send_subagent_input_call"`

      The current public item type.

### Agent Session

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

    - `tools: List[AgentTool]`

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

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

      - `class AgentToolResourceProgrammaticToolCalling: …`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: Literal["programmatic_tool_calling"]`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `class AgentToolResourceMcp: …`

        Tools provided by a remote MCP server.

        - `allowed_tools: Optional[List[str]]`

          The MCP tools the agent may call.

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

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

      - `class AgentToolResourceWebSearch: …`

        Web search.

        - `allowed_domains: Optional[List[str]]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

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

      - `class AgentToolResourceComputerUse: …`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: Literal["computer_use"]`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `access: Literal["enabled", "disabled", "restricted"]`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: List[str]`

          Domains the environment may access when network access is restricted.

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

### Agent Session Assistant Message

- `class AgentSessionAssistantMessage: …`

  An assistant message produced by the agent.

  - `id: str`

    The ID of the message.

  - `content: List[OutputText]`

    The content of the message.

    - `text: str`

      The text produced by the agent.

    - `type: Literal["output_text"]`

      The content type. Always `output_text`.

      - `"output_text"`

  - `phase: Optional[Literal["commentary", "final_answer"]]`

    The phase of the assistant message.

    - `"commentary"`

      Commentary produced while the agent works.

    - `"final_answer"`

      The agent's final answer.

  - `role: Literal["assistant"]`

    The role of the message author. Always `assistant`.

    - `"assistant"`

  - `status: AgentOutputItemStatus`

    The status of the message.

    - `"in_progress"`

      The item is in progress.

    - `"completed"`

      The item is complete.

    - `"incomplete"`

      The item stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["message"]`

    The item type. Always `message`.

    - `"message"`

### Agent Session Created Event

- `class AgentSessionCreatedEvent: …`

  Emitted when a session is created.

  - `event_id: str`

    The unique ID of the event.

  - `session: AgentSession`

    The session that was created.

    - `id: str`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: str`

        The ID of the agent.

      - `instructions: Optional[str]`

        Custom instructions appended to the agent's default base instructions.

      - `model: str`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: Optional[str]`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

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

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `"auto"`

        - `"default"`

        - `"flex"`

        - `"priority"`

        - `"fast"`

        - `"ultrafast"`

      - `text: AgentText`

        Configuration for text generated by the agent.

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

      - `tools: List[AgentTool]`

        Tools available to the agent.

        - `class AgentToolResourceFunction: …`

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

        - `class AgentToolResourceProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `class AgentToolResourceMcp: …`

          Tools provided by a remote MCP server.

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call.

          - `connection_origin: Literal["service", "environment"]`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: Optional[str]`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Dict[str, object]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class McpTransportResourceHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

            - `class McpTransportResourceStdio: …`

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

        - `class AgentToolResourceWebSearch: …`

          Web search.

          - `allowed_domains: Optional[List[str]]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: Literal["low", "medium", "high"]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolResourceWebSearchLocation]`

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

        - `class AgentToolResourceComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: int`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class EnvironmentResourceNone: …`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentResourceOpenAIHosted: …`

        An environment hosted by OpenAI.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: EnvironmentResourceOpenAIHostedDesktop`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: List[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID: …`

            A file copied from the OpenAI Files API.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `file_id: str`

              The ID of the uploaded file.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileResourceInline: …`

            A file supplied inline when the session was created.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: EnvironmentResourceOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: List[str]`

            Domains the environment may access when network access is restricted.

        - `packages: EnvironmentResourceOpenAIHostedPackages`

          Packages installed in the environment.

          - `npm: List[str]`

            npm packages installed globally in the environment.

          - `python: List[str]`

            Python packages installed in the environment.

          - `system: List[str]`

            System packages installed in the environment.

        - `plugins: List[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: str`

            The installed plugin description.

          - `name: str`

            The installed plugin name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: List[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference: …`

            A skill installed from the Skills API.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `skill_id: str`

              The referenced skill ID.

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: str`

              The concrete skill version installed for this session.

          - `class HostedSkillResourceInline: …`

            A skill installed from an inline ZIP archive.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `class EnvironmentResourceSelfHosted: …`

        An environment hosted by the application.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: str`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: Optional[str]`

      The error that caused the session to fail, if any.

    - `last_active_at: int`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the session.

    - `object: Literal["agent.session"]`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: List[RequiredAction]`

      Actions that must be completed before the session can continue.

      - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

        Respond to a computer-use request.

        - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

          The information needed to render the request.

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

            A registered form awaiting the application's response.

            - `credential_origin: Optional[str]`

              The registered form or frame origin where values will be entered.

            - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

              Controls to render. All submitted values are sensitive.

              - `id: str`

                The field ID to submit as field_id in a fields entry.

              - `label: str`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: str`

                The rendering type, such as email, password, or text.

            - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

              Sign-in methods. Empty for a plain form.

              - `id: str`

                The option ID to submit as selected_option.

              - `field_ids: List[str]`

                IDs from the registered fields that this method accepts.

              - `label: str`

                The method label to display.

            - `reason: Optional[str]`

              Why the agent needs the user to sign in.

            - `type: Literal["browser_authentication"]`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

            A browser origin awaiting the application's approval decision.

            - `origin: str`

              The origin the browser needs permission to access.

            - `reason: Optional[str]`

              The browser's explanation for this request, or null when unavailable.

            - `type: Literal["browser_origin_access"]`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: str`

          The registered request ID to echo when responding.

        - `turn_id: str`

          The turn that requested approval.

        - `type: Literal["computer_use_approval_request"]`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

        Run a function tool and submit its result.

        - `arguments: object`

          The arguments supplied by the model.

        - `call_id: str`

          The ID to include when submitting the function result.

        - `name: str`

          The function name.

        - `turn_id: str`

          The ID of the turn that requested the function call.

        - `type: Literal["function_call"]`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

        Reconnect a session environment.

        - `environment_id: str`

          The ID of the environment to reconnect.

        - `type: Literal["environment_connection"]`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

    - `vault_ids: List[str]`

      The IDs of vaults made available to the session.

  - `type: Literal["agent.session.created"]`

    The type of the object. Always `agent.session.created`.

    - `"agent.session.created"`

### Agent Session Deleted

- `class AgentSessionDeleted: …`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: str`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: Literal["agent.session.deleted"]`

    The object type. Always `agent.session.deleted`.

    - `"agent.session.deleted"`

### Agent Session Environment Connected Event

- `class AgentSessionEnvironmentConnectedEvent: …`

  Emitted when a session environment connects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: str`

      The public ID of the environment.

    - `error: Optional[Error]`

      The error reported while preparing the environment, if any.

      - `code: str`

        A machine-readable error code.

      - `message: str`

        A human-readable error message.

      - `type: str`

        The error type.

    - `status: Literal["pending", "ready", "connected", 2 more]`

      The environment's connection status.

      - `"pending"`

        The environment is being prepared.

      - `"ready"`

        The environment is ready to connect.

      - `"connected"`

        The environment is connected.

      - `"disconnected"`

        The environment is disconnected.

      - `"failed"`

        The environment failed to connect.

    - `type: str`

      The environment type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.environment.connected"]`

    The type of the object. Always `agent.session.environment.connected`.

    - `"agent.session.environment.connected"`

### Agent Session Environment Disconnected Event

- `class AgentSessionEnvironmentDisconnectedEvent: …`

  Emitted when a session environment disconnects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: str`

      The public ID of the environment.

    - `error: Optional[Error]`

      The error reported while preparing the environment, if any.

      - `code: str`

        A machine-readable error code.

      - `message: str`

        A human-readable error message.

      - `type: str`

        The error type.

    - `status: Literal["pending", "ready", "connected", 2 more]`

      The environment's connection status.

      - `"pending"`

        The environment is being prepared.

      - `"ready"`

        The environment is ready to connect.

      - `"connected"`

        The environment is connected.

      - `"disconnected"`

        The environment is disconnected.

      - `"failed"`

        The environment failed to connect.

    - `type: str`

      The environment type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.environment.disconnected"]`

    The type of the object. Always `agent.session.environment.disconnected`.

    - `"agent.session.environment.disconnected"`

### Agent Session Environment Failed Event

- `class AgentSessionEnvironmentFailedEvent: …`

  Emitted when a session environment fails.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: str`

      The public ID of the environment.

    - `error: Optional[Error]`

      The error reported while preparing the environment, if any.

      - `code: str`

        A machine-readable error code.

      - `message: str`

        A human-readable error message.

      - `type: str`

        The error type.

    - `status: Literal["pending", "ready", "connected", 2 more]`

      The environment's connection status.

      - `"pending"`

        The environment is being prepared.

      - `"ready"`

        The environment is ready to connect.

      - `"connected"`

        The environment is connected.

      - `"disconnected"`

        The environment is disconnected.

      - `"failed"`

        The environment failed to connect.

    - `type: str`

      The environment type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.environment.failed"]`

    The type of the object. Always `agent.session.environment.failed`.

    - `"agent.session.environment.failed"`

### Agent Session Environment Pending Event

- `class AgentSessionEnvironmentPendingEvent: …`

  Emitted while a session environment is being prepared.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: str`

      The public ID of the environment.

    - `error: Optional[Error]`

      The error reported while preparing the environment, if any.

      - `code: str`

        A machine-readable error code.

      - `message: str`

        A human-readable error message.

      - `type: str`

        The error type.

    - `status: Literal["pending", "ready", "connected", 2 more]`

      The environment's connection status.

      - `"pending"`

        The environment is being prepared.

      - `"ready"`

        The environment is ready to connect.

      - `"connected"`

        The environment is connected.

      - `"disconnected"`

        The environment is disconnected.

      - `"failed"`

        The environment failed to connect.

    - `type: str`

      The environment type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.environment.pending"]`

    The type of the object. Always `agent.session.environment.pending`.

    - `"agent.session.environment.pending"`

### Agent Session Environment Ready Event

- `class AgentSessionEnvironmentReadyEvent: …`

  Emitted when a hosted session environment is ready to connect.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: str`

      The public ID of the environment.

    - `error: Optional[Error]`

      The error reported while preparing the environment, if any.

      - `code: str`

        A machine-readable error code.

      - `message: str`

        A human-readable error message.

      - `type: str`

        The error type.

    - `status: Literal["pending", "ready", "connected", 2 more]`

      The environment's connection status.

      - `"pending"`

        The environment is being prepared.

      - `"ready"`

        The environment is ready to connect.

      - `"connected"`

        The environment is connected.

      - `"disconnected"`

        The environment is disconnected.

      - `"failed"`

        The environment failed to connect.

    - `type: str`

      The environment type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.environment.ready"]`

    The type of the object. Always `agent.session.environment.ready`.

    - `"agent.session.environment.ready"`

### Agent Session Environment Reset Event

- `class AgentSessionEnvironmentResetEvent: …`

  Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

  - `environment_id: str`

    The stable environment ID, retained across sandbox replacements.

  - `event_id: str`

    The unique ID of the event.

  - `reset_count: int`

    Monotonically increasing reset number. Repeated notifications share this number.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The associated turn, when applicable.

  - `type: Literal["agent.session.environment.reset"]`

    The type of the object. Always `agent.session.environment.reset`.

    - `"agent.session.environment.reset"`

### Agent Session Environment State

- `class AgentSessionEnvironmentState: …`

  The current state of a session environment.

  - `id: str`

    The public ID of the environment.

  - `error: Optional[Error]`

    The error reported while preparing the environment, if any.

    - `code: str`

      A machine-readable error code.

    - `message: str`

      A human-readable error message.

    - `type: str`

      The error type.

  - `status: Literal["pending", "ready", "connected", 2 more]`

    The environment's connection status.

    - `"pending"`

      The environment is being prepared.

    - `"ready"`

      The environment is ready to connect.

    - `"connected"`

      The environment is connected.

    - `"disconnected"`

      The environment is disconnected.

    - `"failed"`

      The environment failed to connect.

  - `type: str`

    The environment type.

### Agent Session Error Event

- `class AgentSessionErrorEvent: …`

  Emitted when a turn or session fails.

  - `error: SessionError`

    The error that occurred.

    - `code: Optional[str]`

      The machine-readable error code, if any.

    - `message: str`

      A customer-safe explanation of the error.

    - `param: Optional[str]`

      The request parameter associated with the error, if any.

    - `type: str`

      The error type.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `type: Literal["error"]`

    The type of the object. Always `error`.

    - `"error"`

### Agent Session Event

- `AgentSessionEvent`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent: …`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: Optional[str]`

        The machine-readable error code, if any.

      - `message: str`

        A customer-safe explanation of the error.

      - `param: Optional[str]`

        The request parameter associated with the error, if any.

      - `type: str`

        The error type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `type: Literal["error"]`

      The type of the object. Always `error`.

      - `"error"`

  - `class AgentSessionEnvironmentReadyEvent: …`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: str`

        The public ID of the environment.

      - `error: Optional[Error]`

        The error reported while preparing the environment, if any.

        - `code: str`

          A machine-readable error code.

        - `message: str`

          A human-readable error message.

        - `type: str`

          The error type.

      - `status: Literal["pending", "ready", "connected", 2 more]`

        The environment's connection status.

        - `"pending"`

          The environment is being prepared.

        - `"ready"`

          The environment is ready to connect.

        - `"connected"`

          The environment is connected.

        - `"disconnected"`

          The environment is disconnected.

        - `"failed"`

          The environment failed to connect.

      - `type: str`

        The environment type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.ready"]`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent: …`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: str`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: str`

      The unique ID of the event.

    - `reset_count: int`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The associated turn, when applicable.

    - `type: Literal["agent.session.environment.reset"]`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent: …`

    Emitted when command execution produces an output delta.

    - `delta: str`

      The output text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the command execution item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.output.command_execution_output.delta"]`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent: …`

    Emitted when a session is created.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: str`

        The ID of the session.

      - `agent: Agent`

        The agent running in the session.

        - `id: str`

          The ID of the agent.

        - `instructions: Optional[str]`

          Custom instructions appended to the agent's default base instructions.

        - `model: str`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: bool`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: Optional[int]`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: Optional[str]`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

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

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `"auto"`

          - `"default"`

          - `"flex"`

          - `"priority"`

          - `"fast"`

          - `"ultrafast"`

        - `text: AgentText`

          Configuration for text generated by the agent.

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

        - `tools: List[AgentTool]`

          Tools available to the agent.

          - `class AgentToolResourceFunction: …`

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

          - `class AgentToolResourceProgrammaticToolCalling: …`

            Enables calling tools from model-generated code.

            - `enabled: bool`

              Whether tools can be called from model-generated code.

            - `type: Literal["programmatic_tool_calling"]`

              The type of the object. Always `programmatic_tool_calling`.

              - `"programmatic_tool_calling"`

          - `class AgentToolResourceMcp: …`

            Tools provided by a remote MCP server.

            - `allowed_tools: Optional[List[str]]`

              The MCP tools the agent may call.

            - `connection_origin: Literal["service", "environment"]`

              Where outbound MCP HTTP connections originate.

              - `"service"`

              - `"environment"`

            - `credential_id: Optional[str]`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Dict[str, object]`

              Metadata included with requests to this MCP server.

            - `required: bool`

              Whether this MCP server must initialize before the first turn.

            - `server_label: str`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `class McpTransportResourceHTTP: …`

                Connects to an MCP server over HTTP.

                - `server_url: str`

                  The URL of the MCP server.

                - `type: Literal["http"]`

                  The type of the object. Always `http`.

                  - `"http"`

              - `class McpTransportResourceStdio: …`

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

          - `class AgentToolResourceWebSearch: …`

            Web search.

            - `allowed_domains: Optional[List[str]]`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: Literal["low", "medium", "high"]`

              The amount of search context made available to the model. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

            - `location: Optional[AgentToolResourceWebSearchLocation]`

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

          - `class AgentToolResourceComputerUse: …`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: bool`

              Whether computer tool outputs include screenshots.

            - `type: Literal["computer_use"]`

              The type of the object. Always `computer_use`.

              - `"computer_use"`

      - `created_at: int`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `class EnvironmentResourceNone: …`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: Literal["none"]`

            The type of the object. Always `none`.

            - `"none"`

        - `class EnvironmentResourceOpenAIHosted: …`

          An environment hosted by OpenAI.

          - `id: str`

            The public ID of the environment.

          - `capability_directories: List[str]`

            Directories that contain capabilities exposed to the agent.

          - `desktop: EnvironmentResourceOpenAIHostedDesktop`

            The effective desktop configuration.

            - `enabled: bool`

              Whether the environment provisions a desktop and browser proxy.

          - `files: List[HostedEnvironmentFile]`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileID: …`

              A file copied from the OpenAI Files API.

              - `id: str`

                The session-scoped ID of the file in the execution environment.

              - `file_id: str`

                The ID of the uploaded file.

              - `path: str`

                The file's absolute path inside the environment.

              - `size_bytes: int`

                The decoded file size in bytes.

              - `type: Literal["file_id"]`

                The type of the object. Always `file_id`.

                - `"file_id"`

            - `class HostedEnvironmentFileResourceInline: …`

              A file supplied inline when the session was created.

              - `id: str`

                The session-scoped ID of the file in the execution environment.

              - `path: str`

                The file's absolute path inside the environment.

              - `size_bytes: int`

                The decoded file size in bytes.

              - `type: Literal["inline"]`

                The type of the object. Always `inline`.

                - `"inline"`

          - `network: EnvironmentResourceOpenAIHostedNetwork`

            The effective network access policy for the environment.

            - `access: Literal["enabled", "disabled", "restricted"]`

              The environment's network access mode.

              - `"enabled"`

                Allows unrestricted network access.

              - `"disabled"`

                Disables network access.

              - `"restricted"`

                Applies the configured domain restrictions.

            - `allowed_domains: List[str]`

              Domains the environment may access when network access is restricted.

          - `packages: EnvironmentResourceOpenAIHostedPackages`

            Packages installed in the environment.

            - `npm: List[str]`

              npm packages installed globally in the environment.

            - `python: List[str]`

              Python packages installed in the environment.

            - `system: List[str]`

              System packages installed in the environment.

          - `plugins: List[HostedPlugin]`

            Plugins installed in the environment, excluding their archive contents.

            - `description: str`

              The installed plugin description.

            - `name: str`

              The installed plugin name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

          - `skills: List[HostedSkill]`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference: …`

              A skill installed from the Skills API.

              - `description: str`

                The installed skill description.

              - `name: str`

                The installed skill name.

              - `skill_id: str`

                The referenced skill ID.

              - `type: Literal["skill_reference"]`

                The type of the object. Always `skill_reference`.

                - `"skill_reference"`

              - `version: str`

                The concrete skill version installed for this session.

            - `class HostedSkillResourceInline: …`

              A skill installed from an inline ZIP archive.

              - `description: str`

                The installed skill description.

              - `name: str`

                The installed skill name.

              - `type: Literal["inline"]`

                The type of the object. Always `inline`.

                - `"inline"`

          - `type: Literal["openai_hosted"]`

            The type of the object. Always `openai_hosted`.

            - `"openai_hosted"`

          - `container_size: Optional[Literal["small", "medium", "large"]]`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `"small"`

            - `"medium"`

            - `"large"`

        - `class EnvironmentResourceSelfHosted: …`

          An environment hosted by the application.

          - `id: str`

            The public ID of the environment.

          - `capability_directories: List[str]`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: str`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: Literal["self_hosted"]`

            The type of the object. Always `self_hosted`.

            - `"self_hosted"`

          - `workspace_directory: str`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: Optional[str]`

        The error that caused the session to fail, if any.

      - `last_active_at: int`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Dict[str, str]`

        Custom string key-value pairs attached to the session.

      - `object: Literal["agent.session"]`

        The object type. Always `agent.session`.

        - `"agent.session"`

      - `required_actions: List[RequiredAction]`

        Actions that must be completed before the session can continue.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

          Respond to a computer-use request.

          - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

            The information needed to render the request.

            - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

              A registered form awaiting the application's response.

              - `credential_origin: Optional[str]`

                The registered form or frame origin where values will be entered.

              - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

                Controls to render. All submitted values are sensitive.

                - `id: str`

                  The field ID to submit as field_id in a fields entry.

                - `label: str`

                  The label to display beside the control.

                - `required: bool`

                  Whether this control requires a nonempty value.

                - `type: str`

                  The rendering type, such as email, password, or text.

              - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

                Sign-in methods. Empty for a plain form.

                - `id: str`

                  The option ID to submit as selected_option.

                - `field_ids: List[str]`

                  IDs from the registered fields that this method accepts.

                - `label: str`

                  The method label to display.

              - `reason: Optional[str]`

                Why the agent needs the user to sign in.

              - `type: Literal["browser_authentication"]`

                The type of the object. Always `browser_authentication`.

                - `"browser_authentication"`

            - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

              A browser origin awaiting the application's approval decision.

              - `origin: str`

                The origin the browser needs permission to access.

              - `reason: Optional[str]`

                The browser's explanation for this request, or null when unavailable.

              - `type: Literal["browser_origin_access"]`

                The type of the object. Always `browser_origin_access`.

                - `"browser_origin_access"`

          - `request_id: str`

            The registered request ID to echo when responding.

          - `turn_id: str`

            The turn that requested approval.

          - `type: Literal["computer_use_approval_request"]`

            The type of the object. Always `computer_use_approval_request`.

            - `"computer_use_approval_request"`

        - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

          Run a function tool and submit its result.

          - `arguments: object`

            The arguments supplied by the model.

          - `call_id: str`

            The ID to include when submitting the function result.

          - `name: str`

            The function name.

          - `turn_id: str`

            The ID of the turn that requested the function call.

          - `type: Literal["function_call"]`

            The type of the object. Always `function_call`.

            - `"function_call"`

        - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

          Reconnect a session environment.

          - `environment_id: str`

            The ID of the environment to reconnect.

          - `type: Literal["environment_connection"]`

            The type of the object. Always `environment_connection`.

            - `"environment_connection"`

      - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

        The current status of the session.

        - `"idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `"in_progress"`

          The session is processing a turn.

        - `"requires_action"`

          The session is waiting for one or more required actions.

        - `"failed"`

          The session failed.

      - `usage: Optional[TokenUsage]`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: int`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails`

          A breakdown of the agent's input token usage.

          - `cached_tokens: int`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: int`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: int`

            The number of output tokens used for reasoning.

        - `total_tokens: int`

          The total number of input and output tokens used by the agent.

      - `vault_ids: List[str]`

        The IDs of vaults made available to the session.

    - `type: Literal["agent.session.created"]`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent: …`

    Emitted when a turn is created.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: str`

        The ID of the turn.

      - `agent_id: str`

        The ID of the agent that ran the turn.

      - `completed_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: int`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: Optional[SessionTurnError]`

        A customer-safe error. Non-null only for a failed turn.

        - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

          A stable, machine-readable failure category.

          - `"context_length_exceeded"`

            The request exceeds the model's context window.

          - `"session_budget_exceeded"`

            The session has reached its usage budget.

          - `"usage_limit_exceeded"`

            The organization has reached a usage, plan, or billing limit.

          - `"credit_balance_exhausted"`

            The organization has no API credits remaining.

          - `"rate_limit_exceeded"`

            The request exceeds the available rate limit.

          - `"flex_unavailable"`

            Flex processing is temporarily unavailable.

          - `"server_overloaded"`

            The model service is temporarily overloaded.

          - `"cyber_policy"`

            The request was rejected by a safety policy.

          - `"misalignment_policy_violation"`

            The request was blocked by the safety systems.

          - `"connection_failed"`

            The request could not connect to the model service.

          - `"server_error"`

            The model service encountered an unexpected error.

          - `"authentication_error"`

            The API credentials are invalid or lack the required access.

          - `"invalid_request"`

            The request contains invalid input or configuration.

          - `"resource_not_found"`

            The requested model or resource is unavailable.

          - `"sandbox_error"`

            The request could not complete in its execution environment.

          - `"executor_version_incompatible"`

            The executor must be upgraded before it can run this turn.

          - `"active_turn_not_steerable"`

            The session cannot accept additional input while a request is running.

          - `"request_timeout"`

            The request timed out before the model service responded.

          - `"internal_error"`

            An unexpected internal error prevented the session request from completing.

        - `message: str`

          A customer-safe explanation of the failure.

      - `object: Literal["agent.session.turn"]`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: str`

        The ID of the session that owns the turn.

      - `started_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn started.

      - `status: Literal["queued", "in_progress", "waiting", 3 more]`

        The current status of the turn.

        - `"queued"`

          The turn is waiting to start.

        - `"in_progress"`

          The turn is in progress.

        - `"waiting"`

          The turn is waiting for external input.

        - `"completed"`

          The turn completed successfully.

        - `"failed"`

          The turn failed.

        - `"cancelled"`

          The turn was cancelled.

      - `subagent_id: Optional[str]`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: Optional[TokenUsage]`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.created"]`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent: …`

    Emitted when a turn starts running.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.in_progress"]`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent: …`

    Emitted when a turn completes.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.completed"]`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent: …`

    Emitted when a turn fails.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.failed"]`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent: …`

    Emitted when a turn is cancelled.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.cancelled"]`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent: …`

    Emitted when an item is added to a turn.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage: …`

        A user or assistant message recorded in a session.

        - `id: Optional[str]`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: List[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class MessageContentResourceInputText: …`

            Text supplied by the user.

            - `text: str`

              The text supplied by the user.

            - `type: Literal["input_text"]`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `class MessageContentResourceInputImage: …`

            An image supplied by the user.

            - `image_url: str`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: Literal["input_image"]`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `class MessageContentResourceOutputText: …`

            Text produced by the assistant.

            - `text: str`

              The text produced by the assistant.

            - `type: Literal["output_text"]`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["user", "assistant"]`

          The role of the message author.

          - `"user"`

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `"in_progress"`

            The item is in progress.

          - `"completed"`

            The item is complete.

          - `"incomplete"`

            The item stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

        - `id: str`

          The ID of the reasoning item.

        - `status: Optional[AgentOutputItemStatus]`

          The status of the reasoning item.

        - `summary: List[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: str`

            The reasoning summary text.

          - `type: Literal["summary_text"]`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["reasoning"]`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

        - `id: str`

          The ID of the function call item.

        - `arguments: object`

          The arguments to pass to the function.

        - `call_id: str`

          The ID used to submit the function result.

        - `name: str`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `"in_progress"`

            The call is in progress.

          - `"completed"`

            The call completed successfully.

          - `"failed"`

            The call failed.

          - `"incomplete"`

            The call stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call"]`

          The item type. Always `function_call`.

          - `"function_call"`

      - `class FunctionCallOutputItemResource: …`

        The result supplied for a function call.

        - `id: str`

          The ID of the function call output item.

        - `call_id: str`

          The ID of the function call that produced this output.

        - `error: Optional[str]`

          The error message, if the call failed.

        - `output: Optional[AgentFunctionCallOutput]`

          The function result, if the call succeeded.

          - `str`

          - `List[InputContent]`

            - `class InputContentResourceInputText: …`

              Text input recorded in a session item.

              - `text: str`

                The text supplied to the agent.

              - `type: Literal["input_text"]`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `class InputContentResourceInputImage: …`

              Image input recorded in a session item.

              - `image_url: str`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: Literal["input_image"]`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call_output"]`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `class AgentMessageItemResource: …`

        A message exchanged between agent threads.

        - `id: str`

          The ID of the message.

        - `content: List[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText: …`

            A text content part produced by the agent.

            - `text: str`

              The text produced by the agent.

            - `type: Literal["output_text"]`

              The content type. Always `output_text`.

              - `"output_text"`

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

            - `encrypted_content: str`

              The encrypted content payload.

            - `type: Literal["encrypted_content"]`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: str`

          The ID or name of the receiving agent.

        - `sender_agent_id: str`

          The ID or name of the sending agent.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["agent_message"]`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

        - `id: str`

          The ID of the MCP call item.

        - `arguments: object`

          The arguments passed to the MCP tool.

        - `error: object`

          The error returned by the MCP tool, if any.

        - `name: str`

          The name of the MCP tool.

        - `output: object`

          The output returned by the MCP tool, if any.

        - `server_label: str`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["mcp_call"]`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class ComputerUseApprovalRequestResultItemResource: …`

        A credential-free record of an admitted response, not proof of completion.

        - `id: str`

          The stable history item ID.

        - `request_id: str`

          The registered request answered by this item.

        - `response: ComputerUseApprovalRequestResultItemResourceResponse`

          The admitted response, without submitted credential values.

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

            - `action: Literal["submit"]`

              - `"submit"`

            - `selected_option: Optional[str]`

              The chosen sign-in method, or null when no options were offered.

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

            - `action: Literal["cancel"]`

              - `"cancel"`

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_approval_request_result"]`

          - `"computer_use_approval_request_result"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

        - `id: str`

          The ID of the web search call.

        - `action: Optional[WebSearchAction]`

          The action performed by the web search tool.

          - `class WebSearchActionResourceSearch: …`

            A search query or group of search queries.

            - `queries: Optional[List[str]]`

              The search queries, when multiple queries were used.

            - `query: Optional[str]`

              The search query, when a single query was used.

            - `type: Literal["search"]`

              The type of the object. Always `search`.

              - `"search"`

          - `class WebSearchActionResourceOpenPage: …`

            Opens a web page.

            - `type: Literal["open_page"]`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: Optional[str]`

              The URL of the page that was opened.

          - `class WebSearchActionResourceFindInPage: …`

            Finds text within a web page.

            - `pattern: Optional[str]`

              The text pattern that was searched for.

            - `type: Literal["find_in_page"]`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: Optional[str]`

              The URL of the page that was searched.

          - `class WebSearchActionResourceOther: …`

            Another web search action.

            - `type: Literal["other"]`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["web_search_call"]`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

        - `id: str`

          The ID of the command execution item.

        - `command: str`

          The command that was executed.

        - `cwd: Optional[str]`

          The working directory used to execute the command.

        - `duration_ms: Optional[int]`

          The command duration in milliseconds.

        - `exit_code: Optional[int]`

          The process exit code, if the command completed.

        - `output: Optional[str]`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["command_execution"]`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

        - `id: str`

          The ID of the tool call item.

        - `agent_id: str`

          The ID of the agent that requested the subagent.

        - `content: List[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `model: Optional[str]`

          The model requested for the spawned agent.

        - `reasoning_effort: Optional[str]`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["create_subagent_call"]`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

        - `id: str`

          The ID of the tool call item.

        - `content: List[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: str`

          The ID of the agent receiving the input.

        - `sender_agent_id: str`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["send_subagent_input_call"]`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to resume.

        - `sender_agent_id: str`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["resume_subagent_call"]`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_ids: List[str]`

          The IDs of the agents to wait for.

        - `sender_agent_id: str`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["wait_for_subagents_call"]`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to interrupt.

        - `sender_agent_id: str`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["interrupt_subagent_call"]`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to close.

        - `sender_agent_id: str`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["close_subagent_call"]`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: Optional[int]`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.added"]`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent: …`

    Emitted when a session becomes idle.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: Literal["agent.session.idle"]`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `class AgentSessionInProgressEvent: …`

    Emitted when a session starts processing a turn.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: Literal["agent.session.in_progress"]`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent: …`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: Literal["agent.session.requires_action"]`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `class AgentSessionFailedEvent: …`

    Emitted when a session fails.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: Literal["agent.session.failed"]`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent: …`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.pending"]`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent: …`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.connected"]`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent: …`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.disconnected"]`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent: …`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.failed"]`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent: …`

    Emitted when a subagent is created.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: str`

        The ID of the subagent.

      - `closed_at: Optional[int]`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Optional[List[AgentContent]]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `name: Optional[str]`

        The runner-assigned nickname, or null when unavailable.

      - `object: Literal["agent.session.subagent"]`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: int`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: str`

        The ID of the agent that created this subagent.

      - `session_id: str`

        The ID of the session that owns the subagent.

      - `status: Literal["active", "closed"]`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: Literal["agent.session.subagent.created"]`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent: …`

    Emitted when a closed subagent successfully resumes.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: Literal["agent.session.subagent.active"]`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent: …`

    Emitted when a subagent is closed.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: Literal["agent.session.subagent.closed"]`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent: …`

    Emitted when an output item is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage: …`

        An assistant message produced by the agent.

        - `id: str`

          The ID of the message.

        - `content: List[OutputText]`

          The content of the message.

          - `text: str`

            The text produced by the agent.

          - `type: Literal["output_text"]`

            The content type. Always `output_text`.

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["assistant"]`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

    - `output_index: int`

      The index of the output item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.done"]`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent: …`

    Emitted when an output text content part is added.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.added"]`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent: …`

    Emitted when an output content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.done"]`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent: …`

    Emitted when text is appended to an output text content part.

    - `content_index: int`

      The index of the content part in the message.

    - `delta: str`

      The text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.delta"]`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent: …`

    Emitted when an output text content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `text: str`

      The complete output text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.done"]`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent: …`

    Emitted when a reasoning summary content part is added.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.added"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent: …`

    Emitted when a reasoning summary part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `status: Optional[Literal["incomplete"]]`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: int`

      The index of the summary part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent: …`

    Emitted when text is appended to a reasoning summary.

    - `delta: str`

      The summary text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.delta"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent: …`

    Emitted when a reasoning summary content part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `text: str`

      The complete reasoning summary text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

### Agent Session Failed Event

- `class AgentSessionFailedEvent: …`

  Emitted when a session fails.

  - `event_id: str`

    The unique ID of the event.

  - `session: AgentSession`

    The failed session.

    - `id: str`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: str`

        The ID of the agent.

      - `instructions: Optional[str]`

        Custom instructions appended to the agent's default base instructions.

      - `model: str`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: Optional[str]`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

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

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `"auto"`

        - `"default"`

        - `"flex"`

        - `"priority"`

        - `"fast"`

        - `"ultrafast"`

      - `text: AgentText`

        Configuration for text generated by the agent.

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

      - `tools: List[AgentTool]`

        Tools available to the agent.

        - `class AgentToolResourceFunction: …`

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

        - `class AgentToolResourceProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `class AgentToolResourceMcp: …`

          Tools provided by a remote MCP server.

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call.

          - `connection_origin: Literal["service", "environment"]`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: Optional[str]`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Dict[str, object]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class McpTransportResourceHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

            - `class McpTransportResourceStdio: …`

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

        - `class AgentToolResourceWebSearch: …`

          Web search.

          - `allowed_domains: Optional[List[str]]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: Literal["low", "medium", "high"]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolResourceWebSearchLocation]`

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

        - `class AgentToolResourceComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: int`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class EnvironmentResourceNone: …`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentResourceOpenAIHosted: …`

        An environment hosted by OpenAI.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: EnvironmentResourceOpenAIHostedDesktop`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: List[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID: …`

            A file copied from the OpenAI Files API.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `file_id: str`

              The ID of the uploaded file.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileResourceInline: …`

            A file supplied inline when the session was created.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: EnvironmentResourceOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: List[str]`

            Domains the environment may access when network access is restricted.

        - `packages: EnvironmentResourceOpenAIHostedPackages`

          Packages installed in the environment.

          - `npm: List[str]`

            npm packages installed globally in the environment.

          - `python: List[str]`

            Python packages installed in the environment.

          - `system: List[str]`

            System packages installed in the environment.

        - `plugins: List[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: str`

            The installed plugin description.

          - `name: str`

            The installed plugin name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: List[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference: …`

            A skill installed from the Skills API.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `skill_id: str`

              The referenced skill ID.

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: str`

              The concrete skill version installed for this session.

          - `class HostedSkillResourceInline: …`

            A skill installed from an inline ZIP archive.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `class EnvironmentResourceSelfHosted: …`

        An environment hosted by the application.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: str`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: Optional[str]`

      The error that caused the session to fail, if any.

    - `last_active_at: int`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the session.

    - `object: Literal["agent.session"]`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: List[RequiredAction]`

      Actions that must be completed before the session can continue.

      - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

        Respond to a computer-use request.

        - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

          The information needed to render the request.

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

            A registered form awaiting the application's response.

            - `credential_origin: Optional[str]`

              The registered form or frame origin where values will be entered.

            - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

              Controls to render. All submitted values are sensitive.

              - `id: str`

                The field ID to submit as field_id in a fields entry.

              - `label: str`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: str`

                The rendering type, such as email, password, or text.

            - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

              Sign-in methods. Empty for a plain form.

              - `id: str`

                The option ID to submit as selected_option.

              - `field_ids: List[str]`

                IDs from the registered fields that this method accepts.

              - `label: str`

                The method label to display.

            - `reason: Optional[str]`

              Why the agent needs the user to sign in.

            - `type: Literal["browser_authentication"]`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

            A browser origin awaiting the application's approval decision.

            - `origin: str`

              The origin the browser needs permission to access.

            - `reason: Optional[str]`

              The browser's explanation for this request, or null when unavailable.

            - `type: Literal["browser_origin_access"]`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: str`

          The registered request ID to echo when responding.

        - `turn_id: str`

          The turn that requested approval.

        - `type: Literal["computer_use_approval_request"]`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

        Run a function tool and submit its result.

        - `arguments: object`

          The arguments supplied by the model.

        - `call_id: str`

          The ID to include when submitting the function result.

        - `name: str`

          The function name.

        - `turn_id: str`

          The ID of the turn that requested the function call.

        - `type: Literal["function_call"]`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

        Reconnect a session environment.

        - `environment_id: str`

          The ID of the environment to reconnect.

        - `type: Literal["environment_connection"]`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

    - `vault_ids: List[str]`

      The IDs of vaults made available to the session.

  - `type: Literal["agent.session.failed"]`

    The type of the object. Always `agent.session.failed`.

    - `"agent.session.failed"`

### Agent Session Idle Event

- `class AgentSessionIdleEvent: …`

  Emitted when a session becomes idle.

  - `event_id: str`

    The unique ID of the event.

  - `session: AgentSession`

    The session that became idle.

    - `id: str`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: str`

        The ID of the agent.

      - `instructions: Optional[str]`

        Custom instructions appended to the agent's default base instructions.

      - `model: str`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: Optional[str]`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

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

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `"auto"`

        - `"default"`

        - `"flex"`

        - `"priority"`

        - `"fast"`

        - `"ultrafast"`

      - `text: AgentText`

        Configuration for text generated by the agent.

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

      - `tools: List[AgentTool]`

        Tools available to the agent.

        - `class AgentToolResourceFunction: …`

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

        - `class AgentToolResourceProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `class AgentToolResourceMcp: …`

          Tools provided by a remote MCP server.

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call.

          - `connection_origin: Literal["service", "environment"]`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: Optional[str]`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Dict[str, object]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class McpTransportResourceHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

            - `class McpTransportResourceStdio: …`

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

        - `class AgentToolResourceWebSearch: …`

          Web search.

          - `allowed_domains: Optional[List[str]]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: Literal["low", "medium", "high"]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolResourceWebSearchLocation]`

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

        - `class AgentToolResourceComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: int`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class EnvironmentResourceNone: …`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentResourceOpenAIHosted: …`

        An environment hosted by OpenAI.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: EnvironmentResourceOpenAIHostedDesktop`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: List[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID: …`

            A file copied from the OpenAI Files API.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `file_id: str`

              The ID of the uploaded file.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileResourceInline: …`

            A file supplied inline when the session was created.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: EnvironmentResourceOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: List[str]`

            Domains the environment may access when network access is restricted.

        - `packages: EnvironmentResourceOpenAIHostedPackages`

          Packages installed in the environment.

          - `npm: List[str]`

            npm packages installed globally in the environment.

          - `python: List[str]`

            Python packages installed in the environment.

          - `system: List[str]`

            System packages installed in the environment.

        - `plugins: List[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: str`

            The installed plugin description.

          - `name: str`

            The installed plugin name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: List[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference: …`

            A skill installed from the Skills API.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `skill_id: str`

              The referenced skill ID.

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: str`

              The concrete skill version installed for this session.

          - `class HostedSkillResourceInline: …`

            A skill installed from an inline ZIP archive.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `class EnvironmentResourceSelfHosted: …`

        An environment hosted by the application.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: str`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: Optional[str]`

      The error that caused the session to fail, if any.

    - `last_active_at: int`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the session.

    - `object: Literal["agent.session"]`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: List[RequiredAction]`

      Actions that must be completed before the session can continue.

      - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

        Respond to a computer-use request.

        - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

          The information needed to render the request.

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

            A registered form awaiting the application's response.

            - `credential_origin: Optional[str]`

              The registered form or frame origin where values will be entered.

            - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

              Controls to render. All submitted values are sensitive.

              - `id: str`

                The field ID to submit as field_id in a fields entry.

              - `label: str`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: str`

                The rendering type, such as email, password, or text.

            - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

              Sign-in methods. Empty for a plain form.

              - `id: str`

                The option ID to submit as selected_option.

              - `field_ids: List[str]`

                IDs from the registered fields that this method accepts.

              - `label: str`

                The method label to display.

            - `reason: Optional[str]`

              Why the agent needs the user to sign in.

            - `type: Literal["browser_authentication"]`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

            A browser origin awaiting the application's approval decision.

            - `origin: str`

              The origin the browser needs permission to access.

            - `reason: Optional[str]`

              The browser's explanation for this request, or null when unavailable.

            - `type: Literal["browser_origin_access"]`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: str`

          The registered request ID to echo when responding.

        - `turn_id: str`

          The turn that requested approval.

        - `type: Literal["computer_use_approval_request"]`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

        Run a function tool and submit its result.

        - `arguments: object`

          The arguments supplied by the model.

        - `call_id: str`

          The ID to include when submitting the function result.

        - `name: str`

          The function name.

        - `turn_id: str`

          The ID of the turn that requested the function call.

        - `type: Literal["function_call"]`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

        Reconnect a session environment.

        - `environment_id: str`

          The ID of the environment to reconnect.

        - `type: Literal["environment_connection"]`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

    - `vault_ids: List[str]`

      The IDs of vaults made available to the session.

  - `type: Literal["agent.session.idle"]`

    The type of the object. Always `agent.session.idle`.

    - `"agent.session.idle"`

### Agent Session In Progress Event

- `class AgentSessionInProgressEvent: …`

  Emitted when a session starts processing a turn.

  - `event_id: str`

    The unique ID of the event.

  - `session: AgentSession`

    The session that started processing.

    - `id: str`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: str`

        The ID of the agent.

      - `instructions: Optional[str]`

        Custom instructions appended to the agent's default base instructions.

      - `model: str`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: Optional[str]`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

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

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `"auto"`

        - `"default"`

        - `"flex"`

        - `"priority"`

        - `"fast"`

        - `"ultrafast"`

      - `text: AgentText`

        Configuration for text generated by the agent.

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

      - `tools: List[AgentTool]`

        Tools available to the agent.

        - `class AgentToolResourceFunction: …`

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

        - `class AgentToolResourceProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `class AgentToolResourceMcp: …`

          Tools provided by a remote MCP server.

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call.

          - `connection_origin: Literal["service", "environment"]`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: Optional[str]`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Dict[str, object]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class McpTransportResourceHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

            - `class McpTransportResourceStdio: …`

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

        - `class AgentToolResourceWebSearch: …`

          Web search.

          - `allowed_domains: Optional[List[str]]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: Literal["low", "medium", "high"]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolResourceWebSearchLocation]`

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

        - `class AgentToolResourceComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: int`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class EnvironmentResourceNone: …`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentResourceOpenAIHosted: …`

        An environment hosted by OpenAI.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: EnvironmentResourceOpenAIHostedDesktop`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: List[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID: …`

            A file copied from the OpenAI Files API.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `file_id: str`

              The ID of the uploaded file.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileResourceInline: …`

            A file supplied inline when the session was created.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: EnvironmentResourceOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: List[str]`

            Domains the environment may access when network access is restricted.

        - `packages: EnvironmentResourceOpenAIHostedPackages`

          Packages installed in the environment.

          - `npm: List[str]`

            npm packages installed globally in the environment.

          - `python: List[str]`

            Python packages installed in the environment.

          - `system: List[str]`

            System packages installed in the environment.

        - `plugins: List[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: str`

            The installed plugin description.

          - `name: str`

            The installed plugin name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: List[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference: …`

            A skill installed from the Skills API.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `skill_id: str`

              The referenced skill ID.

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: str`

              The concrete skill version installed for this session.

          - `class HostedSkillResourceInline: …`

            A skill installed from an inline ZIP archive.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `class EnvironmentResourceSelfHosted: …`

        An environment hosted by the application.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: str`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: Optional[str]`

      The error that caused the session to fail, if any.

    - `last_active_at: int`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the session.

    - `object: Literal["agent.session"]`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: List[RequiredAction]`

      Actions that must be completed before the session can continue.

      - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

        Respond to a computer-use request.

        - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

          The information needed to render the request.

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

            A registered form awaiting the application's response.

            - `credential_origin: Optional[str]`

              The registered form or frame origin where values will be entered.

            - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

              Controls to render. All submitted values are sensitive.

              - `id: str`

                The field ID to submit as field_id in a fields entry.

              - `label: str`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: str`

                The rendering type, such as email, password, or text.

            - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

              Sign-in methods. Empty for a plain form.

              - `id: str`

                The option ID to submit as selected_option.

              - `field_ids: List[str]`

                IDs from the registered fields that this method accepts.

              - `label: str`

                The method label to display.

            - `reason: Optional[str]`

              Why the agent needs the user to sign in.

            - `type: Literal["browser_authentication"]`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

            A browser origin awaiting the application's approval decision.

            - `origin: str`

              The origin the browser needs permission to access.

            - `reason: Optional[str]`

              The browser's explanation for this request, or null when unavailable.

            - `type: Literal["browser_origin_access"]`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: str`

          The registered request ID to echo when responding.

        - `turn_id: str`

          The turn that requested approval.

        - `type: Literal["computer_use_approval_request"]`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

        Run a function tool and submit its result.

        - `arguments: object`

          The arguments supplied by the model.

        - `call_id: str`

          The ID to include when submitting the function result.

        - `name: str`

          The function name.

        - `turn_id: str`

          The ID of the turn that requested the function call.

        - `type: Literal["function_call"]`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

        Reconnect a session environment.

        - `environment_id: str`

          The ID of the environment to reconnect.

        - `type: Literal["environment_connection"]`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

    - `vault_ids: List[str]`

      The IDs of vaults made available to the session.

  - `type: Literal["agent.session.in_progress"]`

    The type of the object. Always `agent.session.in_progress`.

    - `"agent.session.in_progress"`

### Agent Session Input Message Param

- `class AgentSessionInputMessageParam: …`

  A user message submitted to a session.

  - `content: List[InputContentParam]`

    The content of the message.

    - `class InputContentParamInputText: …`

      Text input to the model.

      - `text: str`

        The text sent to the model.

      - `type: Literal["input_text"]`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `class InputContentParamInputImage: …`

      Image input to the model.

      - `image_url: str`

        The URL of the image sent to the model.

      - `type: Literal["input_image"]`

        The type of the object. Always `input_image`.

        - `"input_image"`

  - `role: Literal["user"]`

    The role of the message author. Always `user`.

    - `"user"`

  - `type: Optional[Literal["message"]]`

    The type of the input item. Always `message`.

    - `"message"`

### Agent Session Input Param

- `AgentSessionInputParam`

  Input submitted to an existing session.

  - `class SessionInputParamAgentSessionInputComputerUseApprovalRequestResult: …`

    Responds to a pending Computer Use approval request.

    - `request_id: str`

      The registered request ID from the required action.

    - `response: SessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponse`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `fields: List[Field]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: str`

            The field ID from the required action.

          - `value: str`

            The value to enter into the registered control.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

        - `selected_option: Optional[str]`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class AgentBrowserOriginAccessParam: …`

        - `decision: Literal["approve", "deny", "cancel"]`

          Whether to allow, deny, or cancel the requested origin access.

          - `"approve"`

            Allow the browser to access this origin.

          - `"deny"`

            Deny access to this origin.

          - `"cancel"`

            Dismiss this request without approving access.

        - `type: Literal["browser_origin_access"]`

          - `"browser_origin_access"`

    - `type: Literal["agent.session.input.computer_use_approval_request_result"]`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `"agent.session.input.computer_use_approval_request_result"`

  - `class SessionInputParamAgentSessionInputMessage: …`

    Adds one or more user messages and starts a turn.

    - `input: List[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: List[InputContentParam]`

        The content of the message.

        - `class InputContentParamInputText: …`

          Text input to the model.

          - `text: str`

            The text sent to the model.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentParamInputImage: …`

          Image input to the model.

          - `image_url: str`

            The URL of the image sent to the model.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: Literal["user"]`

        The role of the message author. Always `user`.

        - `"user"`

      - `type: Optional[Literal["message"]]`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: Literal["agent.session.input.message"]`

      The type of the object. Always `agent.session.input.message`.

      - `"agent.session.input.message"`

  - `class SessionInputParamAgentSessionInputCancel: …`

    Cancels the session's active turn.

    - `type: Literal["agent.session.input.cancel"]`

      The type of the object. Always `agent.session.input.cancel`.

      - `"agent.session.input.cancel"`

  - `class SessionInputParamAgentSessionInputToolResult: …`

    Submits the result of a function call.

    - `call_id: str`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: str`

      The ID of the turn that requested the function call.

    - `type: Literal["agent.session.input.tool_result"]`

      The type of the object. Always `agent.session.input.tool_result`.

      - `"agent.session.input.tool_result"`

    - `error: Optional[str]`

      The error message when the call failed.

    - `output: Optional[AgentFunctionCallOutputParam]`

      The function result when the call succeeded.

      - `str`

      - `List[InputContentParam]`

        - `class InputContentParamInputText: …`

          Text input to the model.

        - `class InputContentParamInputImage: …`

          Image input to the model.

### Agent Session Item

- `AgentSessionItem`

  An item associated with a session turn.

  - `class AgentSessionMessage: …`

    A user or assistant message recorded in a session.

    - `id: Optional[str]`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: List[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class MessageContentResourceInputText: …`

        Text supplied by the user.

        - `text: str`

          The text supplied by the user.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class MessageContentResourceInputImage: …`

        An image supplied by the user.

        - `image_url: str`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `class MessageContentResourceOutputText: …`

        Text produced by the assistant.

        - `text: str`

          The text produced by the assistant.

        - `type: Literal["output_text"]`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["user", "assistant"]`

      The role of the message author.

      - `"user"`

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class FunctionCallOutputItemResource: …`

    The result supplied for a function call.

    - `id: str`

      The ID of the function call output item.

    - `call_id: str`

      The ID of the function call that produced this output.

    - `error: Optional[str]`

      The error message, if the call failed.

    - `output: Optional[AgentFunctionCallOutput]`

      The function result, if the call succeeded.

      - `str`

      - `List[InputContent]`

        - `class InputContentResourceInputText: …`

          Text input recorded in a session item.

          - `text: str`

            The text supplied to the agent.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentResourceInputImage: …`

          Image input recorded in a session item.

          - `image_url: str`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call_output"]`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `class AgentMessageItemResource: …`

    A message exchanged between agent threads.

    - `id: str`

      The ID of the message.

    - `content: List[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: str`

      The ID or name of the receiving agent.

    - `sender_agent_id: str`

      The ID or name of the sending agent.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["agent_message"]`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class ComputerUseApprovalRequestResultItemResource: …`

    A credential-free record of an admitted response, not proof of completion.

    - `id: str`

      The stable history item ID.

    - `request_id: str`

      The registered request answered by this item.

    - `response: ComputerUseApprovalRequestResultItemResourceResponse`

      The admitted response, without submitted credential values.

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `selected_option: Optional[str]`

          The chosen sign-in method, or null when no options were offered.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_approval_request_result"]`

      - `"computer_use_approval_request_result"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Agent Session Message

- `class AgentSessionMessage: …`

  A user or assistant message recorded in a session.

  - `id: Optional[str]`

    The ID of this item, or null for legacy user messages whose ID was not recorded.

  - `content: List[AgentSessionMessageContent]`

    The content of the message. User messages contain input text or images; assistant messages contain output text.

    - `class MessageContentResourceInputText: …`

      Text supplied by the user.

      - `text: str`

        The text supplied by the user.

      - `type: Literal["input_text"]`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `class MessageContentResourceInputImage: …`

      An image supplied by the user.

      - `image_url: str`

        The URL of the image supplied by the user, which may be a base64-encoded data URL.

      - `type: Literal["input_image"]`

        The type of the object. Always `input_image`.

        - `"input_image"`

    - `class MessageContentResourceOutputText: …`

      Text produced by the assistant.

      - `text: str`

        The text produced by the assistant.

      - `type: Literal["output_text"]`

        The type of the object. Always `output_text`.

        - `"output_text"`

  - `phase: Optional[Literal["commentary", "final_answer"]]`

    The phase of an assistant message. Null for user messages.

    - `"commentary"`

      Commentary produced while the agent works.

    - `"final_answer"`

      The agent's final answer.

  - `role: Literal["user", "assistant"]`

    The role of the message author.

    - `"user"`

    - `"assistant"`

  - `status: AgentOutputItemStatus`

    The status of the message. User messages are always `completed`.

    - `"in_progress"`

      The item is in progress.

    - `"completed"`

      The item is complete.

    - `"incomplete"`

      The item stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["message"]`

    The item type. Always `message`.

    - `"message"`

### Agent Session Message Content

- `AgentSessionMessageContent`

  A content part in a session message.

  - `class MessageContentResourceInputText: …`

    Text supplied by the user.

    - `text: str`

      The text supplied by the user.

    - `type: Literal["input_text"]`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `class MessageContentResourceInputImage: …`

    An image supplied by the user.

    - `image_url: str`

      The URL of the image supplied by the user, which may be a base64-encoded data URL.

    - `type: Literal["input_image"]`

      The type of the object. Always `input_image`.

      - `"input_image"`

  - `class MessageContentResourceOutputText: …`

    Text produced by the assistant.

    - `text: str`

      The text produced by the assistant.

    - `type: Literal["output_text"]`

      The type of the object. Always `output_text`.

      - `"output_text"`

### Agent Session Requires Action Event

- `class AgentSessionRequiresActionEvent: …`

  Emitted when a session is waiting for one or more required actions.

  - `event_id: str`

    The unique ID of the event.

  - `session: AgentSession`

    The session and its current required actions.

    - `id: str`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: str`

        The ID of the agent.

      - `instructions: Optional[str]`

        Custom instructions appended to the agent's default base instructions.

      - `model: str`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Optional[int]`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: Optional[str]`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

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

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `"auto"`

        - `"default"`

        - `"flex"`

        - `"priority"`

        - `"fast"`

        - `"ultrafast"`

      - `text: AgentText`

        Configuration for text generated by the agent.

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

      - `tools: List[AgentTool]`

        Tools available to the agent.

        - `class AgentToolResourceFunction: …`

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

        - `class AgentToolResourceProgrammaticToolCalling: …`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: Literal["programmatic_tool_calling"]`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `class AgentToolResourceMcp: …`

          Tools provided by a remote MCP server.

          - `allowed_tools: Optional[List[str]]`

            The MCP tools the agent may call.

          - `connection_origin: Literal["service", "environment"]`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: Optional[str]`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Dict[str, object]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: str`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class McpTransportResourceHTTP: …`

              Connects to an MCP server over HTTP.

              - `server_url: str`

                The URL of the MCP server.

              - `type: Literal["http"]`

                The type of the object. Always `http`.

                - `"http"`

            - `class McpTransportResourceStdio: …`

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

        - `class AgentToolResourceWebSearch: …`

          Web search.

          - `allowed_domains: Optional[List[str]]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: Literal["low", "medium", "high"]`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Optional[AgentToolResourceWebSearchLocation]`

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

        - `class AgentToolResourceComputerUse: …`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: Literal["computer_use"]`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: int`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class EnvironmentResourceNone: …`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: Literal["none"]`

          The type of the object. Always `none`.

          - `"none"`

      - `class EnvironmentResourceOpenAIHosted: …`

        An environment hosted by OpenAI.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: EnvironmentResourceOpenAIHostedDesktop`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: List[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID: …`

            A file copied from the OpenAI Files API.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `file_id: str`

              The ID of the uploaded file.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["file_id"]`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `class HostedEnvironmentFileResourceInline: …`

            A file supplied inline when the session was created.

            - `id: str`

              The session-scoped ID of the file in the execution environment.

            - `path: str`

              The file's absolute path inside the environment.

            - `size_bytes: int`

              The decoded file size in bytes.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: EnvironmentResourceOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `access: Literal["enabled", "disabled", "restricted"]`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: List[str]`

            Domains the environment may access when network access is restricted.

        - `packages: EnvironmentResourceOpenAIHostedPackages`

          Packages installed in the environment.

          - `npm: List[str]`

            npm packages installed globally in the environment.

          - `python: List[str]`

            Python packages installed in the environment.

          - `system: List[str]`

            System packages installed in the environment.

        - `plugins: List[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: str`

            The installed plugin description.

          - `name: str`

            The installed plugin name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: List[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference: …`

            A skill installed from the Skills API.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `skill_id: str`

              The referenced skill ID.

            - `type: Literal["skill_reference"]`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: str`

              The concrete skill version installed for this session.

          - `class HostedSkillResourceInline: …`

            A skill installed from an inline ZIP archive.

            - `description: str`

              The installed skill description.

            - `name: str`

              The installed skill name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: Literal["openai_hosted"]`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size: Optional[Literal["small", "medium", "large"]]`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `class EnvironmentResourceSelfHosted: …`

        An environment hosted by the application.

        - `id: str`

          The public ID of the environment.

        - `capability_directories: List[str]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: str`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: Literal["self_hosted"]`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: str`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: Optional[str]`

      The error that caused the session to fail, if any.

    - `last_active_at: int`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Dict[str, str]`

      Custom string key-value pairs attached to the session.

    - `object: Literal["agent.session"]`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: List[RequiredAction]`

      Actions that must be completed before the session can continue.

      - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

        Respond to a computer-use request.

        - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

          The information needed to render the request.

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

            A registered form awaiting the application's response.

            - `credential_origin: Optional[str]`

              The registered form or frame origin where values will be entered.

            - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

              Controls to render. All submitted values are sensitive.

              - `id: str`

                The field ID to submit as field_id in a fields entry.

              - `label: str`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: str`

                The rendering type, such as email, password, or text.

            - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

              Sign-in methods. Empty for a plain form.

              - `id: str`

                The option ID to submit as selected_option.

              - `field_ids: List[str]`

                IDs from the registered fields that this method accepts.

              - `label: str`

                The method label to display.

            - `reason: Optional[str]`

              Why the agent needs the user to sign in.

            - `type: Literal["browser_authentication"]`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

            A browser origin awaiting the application's approval decision.

            - `origin: str`

              The origin the browser needs permission to access.

            - `reason: Optional[str]`

              The browser's explanation for this request, or null when unavailable.

            - `type: Literal["browser_origin_access"]`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: str`

          The registered request ID to echo when responding.

        - `turn_id: str`

          The turn that requested approval.

        - `type: Literal["computer_use_approval_request"]`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

        Run a function tool and submit its result.

        - `arguments: object`

          The arguments supplied by the model.

        - `call_id: str`

          The ID to include when submitting the function result.

        - `name: str`

          The function name.

        - `turn_id: str`

          The ID of the turn that requested the function call.

        - `type: Literal["function_call"]`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

        Reconnect a session environment.

        - `environment_id: str`

          The ID of the environment to reconnect.

        - `type: Literal["environment_connection"]`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

    - `vault_ids: List[str]`

      The IDs of vaults made available to the session.

  - `type: Literal["agent.session.requires_action"]`

    The type of the object. Always `agent.session.requires_action`.

    - `"agent.session.requires_action"`

### Agent Session Subagent Active Event

- `class AgentSessionSubagentActiveEvent: …`

  Emitted when a closed subagent successfully resumes.

  - `event_id: str`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that resumed.

    - `id: str`

      The ID of the subagent.

    - `closed_at: Optional[int]`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Optional[List[AgentContent]]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: Optional[str]`

      The runner-assigned nickname, or null when unavailable.

    - `object: Literal["agent.session.subagent"]`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: int`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: str`

      The ID of the agent that created this subagent.

    - `session_id: str`

      The ID of the session that owns the subagent.

    - `status: Literal["active", "closed"]`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: Literal["agent.session.subagent.active"]`

    The type of the object. Always `agent.session.subagent.active`.

    - `"agent.session.subagent.active"`

### Agent Session Subagent Closed Event

- `class AgentSessionSubagentClosedEvent: …`

  Emitted when a subagent is closed.

  - `event_id: str`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was closed.

    - `id: str`

      The ID of the subagent.

    - `closed_at: Optional[int]`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Optional[List[AgentContent]]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: Optional[str]`

      The runner-assigned nickname, or null when unavailable.

    - `object: Literal["agent.session.subagent"]`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: int`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: str`

      The ID of the agent that created this subagent.

    - `session_id: str`

      The ID of the session that owns the subagent.

    - `status: Literal["active", "closed"]`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: Literal["agent.session.subagent.closed"]`

    The type of the object. Always `agent.session.subagent.closed`.

    - `"agent.session.subagent.closed"`

### Agent Session Subagent Created Event

- `class AgentSessionSubagentCreatedEvent: …`

  Emitted when a subagent is created.

  - `event_id: str`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was created.

    - `id: str`

      The ID of the subagent.

    - `closed_at: Optional[int]`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Optional[List[AgentContent]]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: Optional[str]`

      The runner-assigned nickname, or null when unavailable.

    - `object: Literal["agent.session.subagent"]`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: int`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: str`

      The ID of the agent that created this subagent.

    - `session_id: str`

      The ID of the session that owns the subagent.

    - `status: Literal["active", "closed"]`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: Literal["agent.session.subagent.created"]`

    The type of the object. Always `agent.session.subagent.created`.

    - `"agent.session.subagent.created"`

### Agent Session Turn Cancelled Event

- `class AgentSessionTurnCancelledEvent: …`

  Emitted when a turn is cancelled.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn: Turn`

    The cancelled turn.

    - `id: str`

      The ID of the turn.

    - `agent_id: str`

      The ID of the agent that ran the turn.

    - `completed_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: int`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: Optional[SessionTurnError]`

      A customer-safe error. Non-null only for a failed turn.

      - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

        A stable, machine-readable failure category.

        - `"context_length_exceeded"`

          The request exceeds the model's context window.

        - `"session_budget_exceeded"`

          The session has reached its usage budget.

        - `"usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `"credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `"rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `"flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `"server_overloaded"`

          The model service is temporarily overloaded.

        - `"cyber_policy"`

          The request was rejected by a safety policy.

        - `"misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `"connection_failed"`

          The request could not connect to the model service.

        - `"server_error"`

          The model service encountered an unexpected error.

        - `"authentication_error"`

          The API credentials are invalid or lack the required access.

        - `"invalid_request"`

          The request contains invalid input or configuration.

        - `"resource_not_found"`

          The requested model or resource is unavailable.

        - `"sandbox_error"`

          The request could not complete in its execution environment.

        - `"executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `"active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `"request_timeout"`

          The request timed out before the model service responded.

        - `"internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `message: str`

        A customer-safe explanation of the failure.

    - `object: Literal["agent.session.turn"]`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: str`

      The ID of the session that owns the turn.

    - `started_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn started.

    - `status: Literal["queued", "in_progress", "waiting", 3 more]`

      The current status of the turn.

      - `"queued"`

        The turn is waiting to start.

      - `"in_progress"`

        The turn is in progress.

      - `"waiting"`

        The turn is waiting for external input.

      - `"completed"`

        The turn completed successfully.

      - `"failed"`

        The turn failed.

      - `"cancelled"`

        The turn was cancelled.

    - `subagent_id: Optional[str]`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

  - `turn_id: str`

    The ID of the turn associated with the event.

  - `type: Literal["agent.session.turn.cancelled"]`

    The type of the object. Always `agent.session.turn.cancelled`.

    - `"agent.session.turn.cancelled"`

  - `usage: Optional[TokenUsage]`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Completed Event

- `class AgentSessionTurnCompletedEvent: …`

  Emitted when a turn completes.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn: Turn`

    The completed turn.

    - `id: str`

      The ID of the turn.

    - `agent_id: str`

      The ID of the agent that ran the turn.

    - `completed_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: int`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: Optional[SessionTurnError]`

      A customer-safe error. Non-null only for a failed turn.

      - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

        A stable, machine-readable failure category.

        - `"context_length_exceeded"`

          The request exceeds the model's context window.

        - `"session_budget_exceeded"`

          The session has reached its usage budget.

        - `"usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `"credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `"rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `"flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `"server_overloaded"`

          The model service is temporarily overloaded.

        - `"cyber_policy"`

          The request was rejected by a safety policy.

        - `"misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `"connection_failed"`

          The request could not connect to the model service.

        - `"server_error"`

          The model service encountered an unexpected error.

        - `"authentication_error"`

          The API credentials are invalid or lack the required access.

        - `"invalid_request"`

          The request contains invalid input or configuration.

        - `"resource_not_found"`

          The requested model or resource is unavailable.

        - `"sandbox_error"`

          The request could not complete in its execution environment.

        - `"executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `"active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `"request_timeout"`

          The request timed out before the model service responded.

        - `"internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `message: str`

        A customer-safe explanation of the failure.

    - `object: Literal["agent.session.turn"]`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: str`

      The ID of the session that owns the turn.

    - `started_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn started.

    - `status: Literal["queued", "in_progress", "waiting", 3 more]`

      The current status of the turn.

      - `"queued"`

        The turn is waiting to start.

      - `"in_progress"`

        The turn is in progress.

      - `"waiting"`

        The turn is waiting for external input.

      - `"completed"`

        The turn completed successfully.

      - `"failed"`

        The turn failed.

      - `"cancelled"`

        The turn was cancelled.

    - `subagent_id: Optional[str]`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

  - `turn_id: str`

    The ID of the turn associated with the event.

  - `type: Literal["agent.session.turn.completed"]`

    The type of the object. Always `agent.session.turn.completed`.

    - `"agent.session.turn.completed"`

  - `usage: Optional[TokenUsage]`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Content Part Added Event

- `class AgentSessionTurnContentPartAddedEvent: …`

  Emitted when an output text content part is added.

  - `content_index: int`

    The index of the content part in the message.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the message item.

  - `output_index: int`

    The index of the item in the turn output.

  - `part: OutputText`

    The initial content part.

    - `text: str`

      The text produced by the agent.

    - `type: Literal["output_text"]`

      The content type. Always `output_text`.

      - `"output_text"`

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.content_part.added"]`

    The type of the object. Always `agent.session.turn.content_part.added`.

    - `"agent.session.turn.content_part.added"`

### Agent Session Turn Content Part Done Event

- `class AgentSessionTurnContentPartDoneEvent: …`

  Emitted when an output content part is complete.

  - `content_index: int`

    The index of the content part in the message.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the message item.

  - `output_index: int`

    The index of the item in the turn output.

  - `part: OutputText`

    The completed content part.

    - `text: str`

      The text produced by the agent.

    - `type: Literal["output_text"]`

      The content type. Always `output_text`.

      - `"output_text"`

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.content_part.done"]`

    The type of the object. Always `agent.session.turn.content_part.done`.

    - `"agent.session.turn.content_part.done"`

### Agent Session Turn Created Event

- `class AgentSessionTurnCreatedEvent: …`

  Emitted when a turn is created.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it was created.

    - `id: str`

      The ID of the turn.

    - `agent_id: str`

      The ID of the agent that ran the turn.

    - `completed_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: int`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: Optional[SessionTurnError]`

      A customer-safe error. Non-null only for a failed turn.

      - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

        A stable, machine-readable failure category.

        - `"context_length_exceeded"`

          The request exceeds the model's context window.

        - `"session_budget_exceeded"`

          The session has reached its usage budget.

        - `"usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `"credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `"rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `"flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `"server_overloaded"`

          The model service is temporarily overloaded.

        - `"cyber_policy"`

          The request was rejected by a safety policy.

        - `"misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `"connection_failed"`

          The request could not connect to the model service.

        - `"server_error"`

          The model service encountered an unexpected error.

        - `"authentication_error"`

          The API credentials are invalid or lack the required access.

        - `"invalid_request"`

          The request contains invalid input or configuration.

        - `"resource_not_found"`

          The requested model or resource is unavailable.

        - `"sandbox_error"`

          The request could not complete in its execution environment.

        - `"executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `"active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `"request_timeout"`

          The request timed out before the model service responded.

        - `"internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `message: str`

        A customer-safe explanation of the failure.

    - `object: Literal["agent.session.turn"]`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: str`

      The ID of the session that owns the turn.

    - `started_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn started.

    - `status: Literal["queued", "in_progress", "waiting", 3 more]`

      The current status of the turn.

      - `"queued"`

        The turn is waiting to start.

      - `"in_progress"`

        The turn is in progress.

      - `"waiting"`

        The turn is waiting for external input.

      - `"completed"`

        The turn completed successfully.

      - `"failed"`

        The turn failed.

      - `"cancelled"`

        The turn was cancelled.

    - `subagent_id: Optional[str]`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

  - `turn_id: str`

    The ID of the turn associated with the event.

  - `type: Literal["agent.session.turn.created"]`

    The type of the object. Always `agent.session.turn.created`.

    - `"agent.session.turn.created"`

### Agent Session Turn Failed Event

- `class AgentSessionTurnFailedEvent: …`

  Emitted when a turn fails.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn: Turn`

    The failed turn.

    - `id: str`

      The ID of the turn.

    - `agent_id: str`

      The ID of the agent that ran the turn.

    - `completed_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: int`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: Optional[SessionTurnError]`

      A customer-safe error. Non-null only for a failed turn.

      - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

        A stable, machine-readable failure category.

        - `"context_length_exceeded"`

          The request exceeds the model's context window.

        - `"session_budget_exceeded"`

          The session has reached its usage budget.

        - `"usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `"credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `"rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `"flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `"server_overloaded"`

          The model service is temporarily overloaded.

        - `"cyber_policy"`

          The request was rejected by a safety policy.

        - `"misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `"connection_failed"`

          The request could not connect to the model service.

        - `"server_error"`

          The model service encountered an unexpected error.

        - `"authentication_error"`

          The API credentials are invalid or lack the required access.

        - `"invalid_request"`

          The request contains invalid input or configuration.

        - `"resource_not_found"`

          The requested model or resource is unavailable.

        - `"sandbox_error"`

          The request could not complete in its execution environment.

        - `"executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `"active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `"request_timeout"`

          The request timed out before the model service responded.

        - `"internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `message: str`

        A customer-safe explanation of the failure.

    - `object: Literal["agent.session.turn"]`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: str`

      The ID of the session that owns the turn.

    - `started_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn started.

    - `status: Literal["queued", "in_progress", "waiting", 3 more]`

      The current status of the turn.

      - `"queued"`

        The turn is waiting to start.

      - `"in_progress"`

        The turn is in progress.

      - `"waiting"`

        The turn is waiting for external input.

      - `"completed"`

        The turn completed successfully.

      - `"failed"`

        The turn failed.

      - `"cancelled"`

        The turn was cancelled.

    - `subagent_id: Optional[str]`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

  - `turn_id: str`

    The ID of the turn associated with the event.

  - `type: Literal["agent.session.turn.failed"]`

    The type of the object. Always `agent.session.turn.failed`.

    - `"agent.session.turn.failed"`

  - `usage: Optional[TokenUsage]`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn In Progress Event

- `class AgentSessionTurnInProgressEvent: …`

  Emitted when a turn starts running.

  - `event_id: str`

    The unique ID of the event.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it started running.

    - `id: str`

      The ID of the turn.

    - `agent_id: str`

      The ID of the agent that ran the turn.

    - `completed_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: int`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: Optional[SessionTurnError]`

      A customer-safe error. Non-null only for a failed turn.

      - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

        A stable, machine-readable failure category.

        - `"context_length_exceeded"`

          The request exceeds the model's context window.

        - `"session_budget_exceeded"`

          The session has reached its usage budget.

        - `"usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `"credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `"rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `"flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `"server_overloaded"`

          The model service is temporarily overloaded.

        - `"cyber_policy"`

          The request was rejected by a safety policy.

        - `"misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `"connection_failed"`

          The request could not connect to the model service.

        - `"server_error"`

          The model service encountered an unexpected error.

        - `"authentication_error"`

          The API credentials are invalid or lack the required access.

        - `"invalid_request"`

          The request contains invalid input or configuration.

        - `"resource_not_found"`

          The requested model or resource is unavailable.

        - `"sandbox_error"`

          The request could not complete in its execution environment.

        - `"executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `"active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `"request_timeout"`

          The request timed out before the model service responded.

        - `"internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `message: str`

        A customer-safe explanation of the failure.

    - `object: Literal["agent.session.turn"]`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: str`

      The ID of the session that owns the turn.

    - `started_at: Optional[int]`

      The Unix timestamp, in seconds, when the turn started.

    - `status: Literal["queued", "in_progress", "waiting", 3 more]`

      The current status of the turn.

      - `"queued"`

        The turn is waiting to start.

      - `"in_progress"`

        The turn is in progress.

      - `"waiting"`

        The turn is waiting for external input.

      - `"completed"`

        The turn completed successfully.

      - `"failed"`

        The turn failed.

      - `"cancelled"`

        The turn was cancelled.

    - `subagent_id: Optional[str]`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: Optional[TokenUsage]`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: int`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: int`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: int`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: int`

          The number of output tokens used for reasoning.

      - `total_tokens: int`

        The total number of input and output tokens used by the agent.

  - `turn_id: str`

    The ID of the turn associated with the event.

  - `type: Literal["agent.session.turn.in_progress"]`

    The type of the object. Always `agent.session.turn.in_progress`.

    - `"agent.session.turn.in_progress"`

### Agent Session Turn Item Added Event

- `class AgentSessionTurnItemAddedEvent: …`

  Emitted when an item is added to a turn.

  - `event_id: str`

    The unique ID of the event.

  - `item: AgentSessionItem`

    The item that was added.

    - `class AgentSessionMessage: …`

      A user or assistant message recorded in a session.

      - `id: Optional[str]`

        The ID of this item, or null for legacy user messages whose ID was not recorded.

      - `content: List[AgentSessionMessageContent]`

        The content of the message. User messages contain input text or images; assistant messages contain output text.

        - `class MessageContentResourceInputText: …`

          Text supplied by the user.

          - `text: str`

            The text supplied by the user.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class MessageContentResourceInputImage: …`

          An image supplied by the user.

          - `image_url: str`

            The URL of the image supplied by the user, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

        - `class MessageContentResourceOutputText: …`

          Text produced by the assistant.

          - `text: str`

            The text produced by the assistant.

          - `type: Literal["output_text"]`

            The type of the object. Always `output_text`.

            - `"output_text"`

      - `phase: Optional[Literal["commentary", "final_answer"]]`

        The phase of an assistant message. Null for user messages.

        - `"commentary"`

          Commentary produced while the agent works.

        - `"final_answer"`

          The agent's final answer.

      - `role: Literal["user", "assistant"]`

        The role of the message author.

        - `"user"`

        - `"assistant"`

      - `status: AgentOutputItemStatus`

        The status of the message. User messages are always `completed`.

        - `"in_progress"`

          The item is in progress.

        - `"completed"`

          The item is complete.

        - `"incomplete"`

          The item stopped before completing.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["message"]`

        The item type. Always `message`.

        - `"message"`

    - `class AgentReasoningItem: …`

      A reasoning item produced by the agent.

      - `id: str`

        The ID of the reasoning item.

      - `status: Optional[AgentOutputItemStatus]`

        The status of the reasoning item.

      - `summary: List[SummaryText]`

        The reasoning summaries produced by the agent.

        - `text: str`

          The reasoning summary text.

        - `type: Literal["summary_text"]`

          The content type. Always `summary_text`.

          - `"summary_text"`

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["reasoning"]`

        The item type. Always `reasoning`.

        - `"reasoning"`

    - `class AgentFunctionCallItem: …`

      A function call produced by the agent.

      - `id: str`

        The ID of the function call item.

      - `arguments: object`

        The arguments to pass to the function.

      - `call_id: str`

        The ID used to submit the function result.

      - `name: str`

        The name of the function to call.

      - `status: AgentFunctionCallStatus`

        The status of the function call.

        - `"in_progress"`

          The call is in progress.

        - `"completed"`

          The call completed successfully.

        - `"failed"`

          The call failed.

        - `"incomplete"`

          The call stopped before completing.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["function_call"]`

        The item type. Always `function_call`.

        - `"function_call"`

    - `class FunctionCallOutputItemResource: …`

      The result supplied for a function call.

      - `id: str`

        The ID of the function call output item.

      - `call_id: str`

        The ID of the function call that produced this output.

      - `error: Optional[str]`

        The error message, if the call failed.

      - `output: Optional[AgentFunctionCallOutput]`

        The function result, if the call succeeded.

        - `str`

        - `List[InputContent]`

          - `class InputContentResourceInputText: …`

            Text input recorded in a session item.

            - `text: str`

              The text supplied to the agent.

            - `type: Literal["input_text"]`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `class InputContentResourceInputImage: …`

            Image input recorded in a session item.

            - `image_url: str`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            - `type: Literal["input_image"]`

              The type of the object. Always `input_image`.

              - `"input_image"`

      - `status: AgentFunctionCallStatus`

        The status of the function call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["function_call_output"]`

        The item type. Always `function_call_output`.

        - `"function_call_output"`

    - `class AgentMessageItemResource: …`

      A message exchanged between agent threads.

      - `id: str`

        The ID of the message.

      - `content: List[AgentContent]`

        The content exchanged between the agents.

        - `class OutputText: …`

          A text content part produced by the agent.

          - `text: str`

            The text produced by the agent.

          - `type: Literal["output_text"]`

            The content type. Always `output_text`.

            - `"output_text"`

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

          - `encrypted_content: str`

            The encrypted content payload.

          - `type: Literal["encrypted_content"]`

            The content type. Always `encrypted_content`.

            - `"encrypted_content"`

      - `recipient_agent_id: str`

        The ID or name of the receiving agent.

      - `sender_agent_id: str`

        The ID or name of the sending agent.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["agent_message"]`

        The item type. Always `agent_message`.

        - `"agent_message"`

    - `class AgentMcpCallItem: …`

      A call to a tool on an MCP server.

      - `id: str`

        The ID of the MCP call item.

      - `arguments: object`

        The arguments passed to the MCP tool.

      - `error: object`

        The error returned by the MCP tool, if any.

      - `name: str`

        The name of the MCP tool.

      - `output: object`

        The output returned by the MCP tool, if any.

      - `server_label: str`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["mcp_call"]`

        The item type. Always `mcp_call`.

        - `"mcp_call"`

    - `class ComputerUseCallItemResource: …`

      One execution of the platform-provided computer-use capability.

      - `id: str`

        The ID of the activity item.

      - `output: Optional[ComputerUseCallItemResourceOutput]`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: str`

          The complete JPEG image as a base64 data URL.

        - `type: Literal["computer_screenshot"]`

          The content type. Always `computer_screenshot`.

          - `"computer_screenshot"`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: Optional[str]`

        A model-generated description of the activity, when available.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["computer_use_call"]`

        The item type. Always `computer_use_call`.

        - `"computer_use_call"`

    - `class BrowserAuthenticationRequestItemResource: …`

      A credential-free history record of the emitted login request.

      - `id: str`

        The stable history item ID.

      - `request: BrowserAuthenticationRequestItemResourceRequest`

        A registered form awaiting the application's response.

        - `credential_origin: Optional[str]`

          The registered form or frame origin where values will be entered.

        - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

          Controls to render. All submitted values are sensitive.

          - `id: str`

            The field ID to submit as field_id in a fields entry.

          - `label: str`

            The label to display beside the control.

          - `required: bool`

            Whether this control requires a nonempty value.

          - `type: str`

            The rendering type, such as email, password, or text.

        - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

          Sign-in methods. Empty for a plain form.

          - `id: str`

            The option ID to submit as selected_option.

          - `field_ids: List[str]`

            IDs from the registered fields that this method accepts.

          - `label: str`

            The method label to display.

        - `reason: Optional[str]`

          Why the agent needs the user to sign in.

        - `type: Literal["browser_authentication"]`

          The type of the object. Always `browser_authentication`.

          - `"browser_authentication"`

      - `request_id: str`

      - `turn_id: str`

      - `type: Literal["computer_use_approval_request"]`

        The item type. Always computer_use_approval_request.

        - `"computer_use_approval_request"`

    - `class ComputerUseApprovalRequestResultItemResource: …`

      A credential-free record of an admitted response, not proof of completion.

      - `id: str`

        The stable history item ID.

      - `request_id: str`

        The registered request answered by this item.

      - `response: ComputerUseApprovalRequestResultItemResourceResponse`

        The admitted response, without submitted credential values.

        - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

          - `action: Literal["submit"]`

            - `"submit"`

          - `selected_option: Optional[str]`

            The chosen sign-in method, or null when no options were offered.

          - `type: Literal["browser_authentication"]`

            - `"browser_authentication"`

        - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

          - `action: Literal["cancel"]`

            - `"cancel"`

          - `type: Literal["browser_authentication"]`

            - `"browser_authentication"`

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["computer_use_approval_request_result"]`

        - `"computer_use_approval_request_result"`

    - `class AgentWebSearchCallItem: …`

      A web search call produced by the agent.

      - `id: str`

        The ID of the web search call.

      - `action: Optional[WebSearchAction]`

        The action performed by the web search tool.

        - `class WebSearchActionResourceSearch: …`

          A search query or group of search queries.

          - `queries: Optional[List[str]]`

            The search queries, when multiple queries were used.

          - `query: Optional[str]`

            The search query, when a single query was used.

          - `type: Literal["search"]`

            The type of the object. Always `search`.

            - `"search"`

        - `class WebSearchActionResourceOpenPage: …`

          Opens a web page.

          - `type: Literal["open_page"]`

            The type of the object. Always `open_page`.

            - `"open_page"`

          - `url: Optional[str]`

            The URL of the page that was opened.

        - `class WebSearchActionResourceFindInPage: …`

          Finds text within a web page.

          - `pattern: Optional[str]`

            The text pattern that was searched for.

          - `type: Literal["find_in_page"]`

            The type of the object. Always `find_in_page`.

            - `"find_in_page"`

          - `url: Optional[str]`

            The URL of the page that was searched.

        - `class WebSearchActionResourceOther: …`

          Another web search action.

          - `type: Literal["other"]`

            The type of the object. Always `other`.

            - `"other"`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["web_search_call"]`

        The item type. Always `web_search_call`.

        - `"web_search_call"`

    - `class AgentCommandExecutionItem: …`

      A command execution produced by the agent.

      - `id: str`

        The ID of the command execution item.

      - `command: str`

        The command that was executed.

      - `cwd: Optional[str]`

        The working directory used to execute the command.

      - `duration_ms: Optional[int]`

        The command duration in milliseconds.

      - `exit_code: Optional[int]`

        The process exit code, if the command completed.

      - `output: Optional[str]`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["command_execution"]`

        The item type. Always `command_execution`.

        - `"command_execution"`

    - `class AgentCreateSubagentCallItem: …`

      A request to spawn a subagent.

      - `id: str`

        The ID of the tool call item.

      - `agent_id: str`

        The ID of the agent that requested the subagent.

      - `content: List[AgentContent]`

        The task given to the spawned agent.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `model: Optional[str]`

        The model requested for the spawned agent.

      - `reasoning_effort: Optional[str]`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["create_subagent_call"]`

        The item type. Always `create_subagent_call`.

        - `"create_subagent_call"`

          The current public item type.

    - `class AgentSendSubagentInputCallItem: …`

      A request to send input to another agent.

      - `id: str`

        The ID of the tool call item.

      - `content: List[AgentContent]`

        The input sent to the receiving agent.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: str`

        The ID of the agent receiving the input.

      - `sender_agent_id: str`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["send_subagent_input_call"]`

        The item type. Always `send_subagent_input_call`.

        - `"send_subagent_input_call"`

          The current public item type.

    - `class AgentResumeSubagentCallItem: …`

      A request to resume a subagent.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to resume.

      - `sender_agent_id: str`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["resume_subagent_call"]`

        The item type. Always `resume_subagent_call`.

        - `"resume_subagent_call"`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem: …`

      A request to wait for one or more subagents.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_ids: List[str]`

        The IDs of the agents to wait for.

      - `sender_agent_id: str`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["wait_for_subagents_call"]`

        The item type. Always `wait_for_subagents_call`.

        - `"wait_for_subagents_call"`

          The current public item type.

    - `class AgentInterruptSubagentCallItem: …`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to interrupt.

      - `sender_agent_id: str`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["interrupt_subagent_call"]`

        The item type. Always `interrupt_subagent_call`.

        - `"interrupt_subagent_call"`

          The current public item type.

    - `class AgentCloseSubagentCallItem: …`

      A request to close a subagent.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to close.

      - `sender_agent_id: str`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["close_subagent_call"]`

        The item type. Always `close_subagent_call`.

        - `"close_subagent_call"`

          The current public item type.

  - `output_index: Optional[int]`

    The index of the item in the turn output, when the item is agent output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.item.added"]`

    The type of the object. Always `agent.session.turn.item.added`.

    - `"agent.session.turn.item.added"`

### Agent Session Turn Item Done Event

- `class AgentSessionTurnItemDoneEvent: …`

  Emitted when an output item is complete.

  - `event_id: str`

    The unique ID of the event.

  - `item: AgentOutputItem`

    The completed output item.

    - `class AgentSessionAssistantMessage: …`

      An assistant message produced by the agent.

      - `id: str`

        The ID of the message.

      - `content: List[OutputText]`

        The content of the message.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `phase: Optional[Literal["commentary", "final_answer"]]`

        The phase of the assistant message.

        - `"commentary"`

          Commentary produced while the agent works.

        - `"final_answer"`

          The agent's final answer.

      - `role: Literal["assistant"]`

        The role of the message author. Always `assistant`.

        - `"assistant"`

      - `status: AgentOutputItemStatus`

        The status of the message.

        - `"in_progress"`

          The item is in progress.

        - `"completed"`

          The item is complete.

        - `"incomplete"`

          The item stopped before completing.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["message"]`

        The item type. Always `message`.

        - `"message"`

    - `class AgentReasoningItem: …`

      A reasoning item produced by the agent.

      - `id: str`

        The ID of the reasoning item.

      - `status: Optional[AgentOutputItemStatus]`

        The status of the reasoning item.

      - `summary: List[SummaryText]`

        The reasoning summaries produced by the agent.

        - `text: str`

          The reasoning summary text.

        - `type: Literal["summary_text"]`

          The content type. Always `summary_text`.

          - `"summary_text"`

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["reasoning"]`

        The item type. Always `reasoning`.

        - `"reasoning"`

    - `class AgentFunctionCallItem: …`

      A function call produced by the agent.

      - `id: str`

        The ID of the function call item.

      - `arguments: object`

        The arguments to pass to the function.

      - `call_id: str`

        The ID used to submit the function result.

      - `name: str`

        The name of the function to call.

      - `status: AgentFunctionCallStatus`

        The status of the function call.

        - `"in_progress"`

          The call is in progress.

        - `"completed"`

          The call completed successfully.

        - `"failed"`

          The call failed.

        - `"incomplete"`

          The call stopped before completing.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["function_call"]`

        The item type. Always `function_call`.

        - `"function_call"`

    - `class AgentMcpCallItem: …`

      A call to a tool on an MCP server.

      - `id: str`

        The ID of the MCP call item.

      - `arguments: object`

        The arguments passed to the MCP tool.

      - `error: object`

        The error returned by the MCP tool, if any.

      - `name: str`

        The name of the MCP tool.

      - `output: object`

        The output returned by the MCP tool, if any.

      - `server_label: str`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["mcp_call"]`

        The item type. Always `mcp_call`.

        - `"mcp_call"`

    - `class ComputerUseCallItemResource: …`

      One execution of the platform-provided computer-use capability.

      - `id: str`

        The ID of the activity item.

      - `output: Optional[ComputerUseCallItemResourceOutput]`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: str`

          The complete JPEG image as a base64 data URL.

        - `type: Literal["computer_screenshot"]`

          The content type. Always `computer_screenshot`.

          - `"computer_screenshot"`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: Optional[str]`

        A model-generated description of the activity, when available.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["computer_use_call"]`

        The item type. Always `computer_use_call`.

        - `"computer_use_call"`

    - `class BrowserAuthenticationRequestItemResource: …`

      A credential-free history record of the emitted login request.

      - `id: str`

        The stable history item ID.

      - `request: BrowserAuthenticationRequestItemResourceRequest`

        A registered form awaiting the application's response.

        - `credential_origin: Optional[str]`

          The registered form or frame origin where values will be entered.

        - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

          Controls to render. All submitted values are sensitive.

          - `id: str`

            The field ID to submit as field_id in a fields entry.

          - `label: str`

            The label to display beside the control.

          - `required: bool`

            Whether this control requires a nonempty value.

          - `type: str`

            The rendering type, such as email, password, or text.

        - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

          Sign-in methods. Empty for a plain form.

          - `id: str`

            The option ID to submit as selected_option.

          - `field_ids: List[str]`

            IDs from the registered fields that this method accepts.

          - `label: str`

            The method label to display.

        - `reason: Optional[str]`

          Why the agent needs the user to sign in.

        - `type: Literal["browser_authentication"]`

          The type of the object. Always `browser_authentication`.

          - `"browser_authentication"`

      - `request_id: str`

      - `turn_id: str`

      - `type: Literal["computer_use_approval_request"]`

        The item type. Always computer_use_approval_request.

        - `"computer_use_approval_request"`

    - `class AgentWebSearchCallItem: …`

      A web search call produced by the agent.

      - `id: str`

        The ID of the web search call.

      - `action: Optional[WebSearchAction]`

        The action performed by the web search tool.

        - `class WebSearchActionResourceSearch: …`

          A search query or group of search queries.

          - `queries: Optional[List[str]]`

            The search queries, when multiple queries were used.

          - `query: Optional[str]`

            The search query, when a single query was used.

          - `type: Literal["search"]`

            The type of the object. Always `search`.

            - `"search"`

        - `class WebSearchActionResourceOpenPage: …`

          Opens a web page.

          - `type: Literal["open_page"]`

            The type of the object. Always `open_page`.

            - `"open_page"`

          - `url: Optional[str]`

            The URL of the page that was opened.

        - `class WebSearchActionResourceFindInPage: …`

          Finds text within a web page.

          - `pattern: Optional[str]`

            The text pattern that was searched for.

          - `type: Literal["find_in_page"]`

            The type of the object. Always `find_in_page`.

            - `"find_in_page"`

          - `url: Optional[str]`

            The URL of the page that was searched.

        - `class WebSearchActionResourceOther: …`

          Another web search action.

          - `type: Literal["other"]`

            The type of the object. Always `other`.

            - `"other"`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["web_search_call"]`

        The item type. Always `web_search_call`.

        - `"web_search_call"`

    - `class AgentCommandExecutionItem: …`

      A command execution produced by the agent.

      - `id: str`

        The ID of the command execution item.

      - `command: str`

        The command that was executed.

      - `cwd: Optional[str]`

        The working directory used to execute the command.

      - `duration_ms: Optional[int]`

        The command duration in milliseconds.

      - `exit_code: Optional[int]`

        The process exit code, if the command completed.

      - `output: Optional[str]`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["command_execution"]`

        The item type. Always `command_execution`.

        - `"command_execution"`

    - `class AgentCreateSubagentCallItem: …`

      A request to spawn a subagent.

      - `id: str`

        The ID of the tool call item.

      - `agent_id: str`

        The ID of the agent that requested the subagent.

      - `content: List[AgentContent]`

        The task given to the spawned agent.

        - `class OutputText: …`

          A text content part produced by the agent.

          - `text: str`

            The text produced by the agent.

          - `type: Literal["output_text"]`

            The content type. Always `output_text`.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

          - `encrypted_content: str`

            The encrypted content payload.

          - `type: Literal["encrypted_content"]`

            The content type. Always `encrypted_content`.

            - `"encrypted_content"`

      - `model: Optional[str]`

        The model requested for the spawned agent.

      - `reasoning_effort: Optional[str]`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["create_subagent_call"]`

        The item type. Always `create_subagent_call`.

        - `"create_subagent_call"`

          The current public item type.

    - `class AgentSendSubagentInputCallItem: …`

      A request to send input to another agent.

      - `id: str`

        The ID of the tool call item.

      - `content: List[AgentContent]`

        The input sent to the receiving agent.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: str`

        The ID of the agent receiving the input.

      - `sender_agent_id: str`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["send_subagent_input_call"]`

        The item type. Always `send_subagent_input_call`.

        - `"send_subagent_input_call"`

          The current public item type.

    - `class AgentResumeSubagentCallItem: …`

      A request to resume a subagent.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to resume.

      - `sender_agent_id: str`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["resume_subagent_call"]`

        The item type. Always `resume_subagent_call`.

        - `"resume_subagent_call"`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem: …`

      A request to wait for one or more subagents.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_ids: List[str]`

        The IDs of the agents to wait for.

      - `sender_agent_id: str`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["wait_for_subagents_call"]`

        The item type. Always `wait_for_subagents_call`.

        - `"wait_for_subagents_call"`

          The current public item type.

    - `class AgentInterruptSubagentCallItem: …`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to interrupt.

      - `sender_agent_id: str`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["interrupt_subagent_call"]`

        The item type. Always `interrupt_subagent_call`.

        - `"interrupt_subagent_call"`

          The current public item type.

    - `class AgentCloseSubagentCallItem: …`

      A request to close a subagent.

      - `id: str`

        The ID of the tool call item.

      - `recipient_agent_id: str`

        The ID of the agent to close.

      - `sender_agent_id: str`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: str`

        The ID of the turn that contains this item.

      - `type: Literal["close_subagent_call"]`

        The item type. Always `close_subagent_call`.

        - `"close_subagent_call"`

          The current public item type.

  - `output_index: int`

    The index of the output item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.item.done"]`

    The type of the object. Always `agent.session.turn.item.done`.

    - `"agent.session.turn.item.done"`

### Agent Session Turn Output Text Delta Event

- `class AgentSessionTurnOutputTextDeltaEvent: …`

  Emitted when text is appended to an output text content part.

  - `content_index: int`

    The index of the content part in the message.

  - `delta: str`

    The text that was appended.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the message item.

  - `output_index: int`

    The index of the item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.output_text.delta"]`

    The type of the object. Always `agent.session.turn.output_text.delta`.

    - `"agent.session.turn.output_text.delta"`

### Agent Session Turn Output Text Done Event

- `class AgentSessionTurnOutputTextDoneEvent: …`

  Emitted when an output text content part is complete.

  - `content_index: int`

    The index of the content part in the message.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the message item.

  - `output_index: int`

    The index of the item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `text: str`

    The complete output text.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.output_text.done"]`

    The type of the object. Always `agent.session.turn.output_text.done`.

    - `"agent.session.turn.output_text.done"`

### Agent Session Turn Reasoning Summary Part Added Event

- `class AgentSessionTurnReasoningSummaryPartAddedEvent: …`

  Emitted when a reasoning summary content part is added.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the reasoning item.

  - `output_index: int`

    The index of the item in the turn output.

  - `part: SummaryText`

    The initial summary part.

    - `text: str`

      The reasoning summary text.

    - `type: Literal["summary_text"]`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `session_id: str`

    The ID of the session associated with the event.

  - `summary_index: int`

    The index of the summary content part.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.reasoning_summary_part.added"]`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

    - `"agent.session.turn.reasoning_summary_part.added"`

### Agent Session Turn Reasoning Summary Part Done Event

- `class AgentSessionTurnReasoningSummaryPartDoneEvent: …`

  Emitted when a reasoning summary part is complete.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the reasoning item.

  - `output_index: int`

    The index of the item in the turn output.

  - `part: SummaryText`

    The completed summary part.

    - `text: str`

      The reasoning summary text.

    - `type: Literal["summary_text"]`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `session_id: str`

    The ID of the session associated with the event.

  - `status: Optional[Literal["incomplete"]]`

    Present as `incomplete` when summary generation was interrupted.

    - `"incomplete"`

  - `summary_index: int`

    The index of the summary part.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.reasoning_summary_part.done"]`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

    - `"agent.session.turn.reasoning_summary_part.done"`

### Agent Session Turn Reasoning Summary Text Delta Event

- `class AgentSessionTurnReasoningSummaryTextDeltaEvent: …`

  Emitted when text is appended to a reasoning summary.

  - `delta: str`

    The summary text that was appended.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the reasoning item.

  - `output_index: int`

    The index of the item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `summary_index: int`

    The index of the summary content part.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.reasoning_summary_text.delta"]`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

    - `"agent.session.turn.reasoning_summary_text.delta"`

### Agent Session Turn Reasoning Summary Text Done Event

- `class AgentSessionTurnReasoningSummaryTextDoneEvent: …`

  Emitted when a reasoning summary content part is complete.

  - `event_id: str`

    The unique ID of the event.

  - `item_id: str`

    The ID of the reasoning item.

  - `output_index: int`

    The index of the item in the turn output.

  - `session_id: str`

    The ID of the session associated with the event.

  - `summary_index: int`

    The index of the summary content part.

  - `text: str`

    The complete reasoning summary text.

  - `turn_id: Optional[str]`

    The ID of the turn associated with the event, when applicable.

  - `type: Literal["agent.session.turn.reasoning_summary_text.done"]`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

    - `"agent.session.turn.reasoning_summary_text.done"`

### Agent Text

- `class AgentText: …`

  The text configuration used by an agent.

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

### Agent Text Param

- `class AgentTextParam: …`

  Configuration for text generated by the agent.

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

### Agent Tool

- `AgentTool`

  A tool available to the agent.

  - `class AgentToolResourceFunction: …`

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

  - `class AgentToolResourceProgrammaticToolCalling: …`

    Enables calling tools from model-generated code.

    - `enabled: bool`

      Whether tools can be called from model-generated code.

    - `type: Literal["programmatic_tool_calling"]`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

  - `class AgentToolResourceMcp: …`

    Tools provided by a remote MCP server.

    - `allowed_tools: Optional[List[str]]`

      The MCP tools the agent may call.

    - `connection_origin: Literal["service", "environment"]`

      Where outbound MCP HTTP connections originate.

      - `"service"`

      - `"environment"`

    - `credential_id: Optional[str]`

      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Dict[str, object]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn.

    - `server_label: str`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransport`

      The transport used to connect to the MCP server.

      - `class McpTransportResourceHTTP: …`

        Connects to an MCP server over HTTP.

        - `server_url: str`

          The URL of the MCP server.

        - `type: Literal["http"]`

          The type of the object. Always `http`.

          - `"http"`

      - `class McpTransportResourceStdio: …`

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

  - `class AgentToolResourceWebSearch: …`

    Web search.

    - `allowed_domains: Optional[List[str]]`

      Allowed search domains, or `null` when the search is unrestricted.

    - `context_size: Literal["low", "medium", "high"]`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location: Optional[AgentToolResourceWebSearchLocation]`

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

  - `class AgentToolResourceComputerUse: …`

    Browser use in an OpenAI-hosted session.

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots.

    - `type: Literal["computer_use"]`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

### Agent Tool Param

- `AgentToolParam`

  A tool available to the agent.

  - `class AgentToolConfigParamFunction: …`

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

  - `class AgentToolConfigParamToolSearch: …`

    Discovers deferred function tools and loads them into the model context.

    - `type: Literal["tool_search"]`

      The type of the object. Always `tool_search`.

      - `"tool_search"`

  - `class AgentToolConfigParamProgrammaticToolCalling: …`

    Enables calling tools from model-generated code.

    - `type: Literal["programmatic_tool_calling"]`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

    - `enabled: Optional[bool]`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class AgentToolConfigParamMcp: …`

    Tools provided by a remote MCP server.

    - `server_label: str`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransportParam`

      The transport used to connect to the MCP server.

      - `class McpTransportConfigParamHTTP: …`

        Connects to an MCP server over HTTP.

        - `server_url: str`

          The URL of the MCP server.

        - `type: Literal["http"]`

          The type of the object. Always `http`.

          - `"http"`

        - `authorization: Optional[str]`

          The authorization value sent to the MCP server, if any.

        - `headers: Optional[Dict[str, str]]`

          Additional HTTP headers sent to the MCP server.

      - `class McpTransportConfigParamStdio: …`

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

        - `env: Optional[Dict[str, str]]`

          Environment variables set for the MCP server process.

        - `env_vars: Optional[List[str]]`

          Environment variable names to inherit from the selected execution environment.

    - `type: Literal["mcp"]`

      The type of the object. Always `mcp`.

      - `"mcp"`

    - `allowed_tools: Optional[List[str]]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: Optional[Literal["service", "environment"]]`

      Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

      - `"service"`

        Uses the Managed Agents service network.

      - `"environment"`

        Uses the session's execution environment.

    - `credential_id: Optional[str]`

      The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Optional[Dict[str, object]]`

      Metadata included with requests to this MCP server.

    - `required: Optional[bool]`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class AgentToolConfigParamWebSearch: …`

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

    - `location: Optional[AgentToolConfigParamWebSearchLocation]`

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

  - `class AgentToolConfigParamComputerUse: …`

    Browser use in an OpenAI-hosted session.

    - `type: Literal["computer_use"]`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

    - `include_screenshots: Optional[bool]`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Agent Wait For Subagents Call Item

- `class AgentWaitForSubagentsCallItem: …`

  A request to wait for one or more subagents.

  - `id: str`

    The ID of the tool call item.

  - `recipient_agent_ids: List[str]`

    The IDs of the agents to wait for.

  - `sender_agent_id: str`

    The ID of the agent waiting for results.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `"in_progress"`

      The call is in progress.

    - `"completed"`

      The call completed successfully.

    - `"failed"`

      The call failed.

    - `"incomplete"`

      The call stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["wait_for_subagents_call"]`

    The item type. Always `wait_for_subagents_call`.

    - `"wait_for_subagents_call"`

      The current public item type.

### Agent Web Search Call Item

- `class AgentWebSearchCallItem: …`

  A web search call produced by the agent.

  - `id: str`

    The ID of the web search call.

  - `action: Optional[WebSearchAction]`

    The action performed by the web search tool.

    - `class WebSearchActionResourceSearch: …`

      A search query or group of search queries.

      - `queries: Optional[List[str]]`

        The search queries, when multiple queries were used.

      - `query: Optional[str]`

        The search query, when a single query was used.

      - `type: Literal["search"]`

        The type of the object. Always `search`.

        - `"search"`

    - `class WebSearchActionResourceOpenPage: …`

      Opens a web page.

      - `type: Literal["open_page"]`

        The type of the object. Always `open_page`.

        - `"open_page"`

      - `url: Optional[str]`

        The URL of the page that was opened.

    - `class WebSearchActionResourceFindInPage: …`

      Finds text within a web page.

      - `pattern: Optional[str]`

        The text pattern that was searched for.

      - `type: Literal["find_in_page"]`

        The type of the object. Always `find_in_page`.

        - `"find_in_page"`

      - `url: Optional[str]`

        The URL of the page that was searched.

    - `class WebSearchActionResourceOther: …`

      Another web search action.

      - `type: Literal["other"]`

        The type of the object. Always `other`.

        - `"other"`

  - `status: AgentOutputItemStatus`

    The status of the web search call.

    - `"in_progress"`

      The item is in progress.

    - `"completed"`

      The item is complete.

    - `"incomplete"`

      The item stopped before completing.

  - `turn_id: str`

    The ID of the turn that contains this item.

  - `type: Literal["web_search_call"]`

    The item type. Always `web_search_call`.

    - `"web_search_call"`

### Environment

- `Environment`

  The execution environment for a session.

  - `class EnvironmentResourceNone: …`

    The session talks to CCA without selecting or provisioning an execution environment.

    - `type: Literal["none"]`

      The type of the object. Always `none`.

      - `"none"`

  - `class EnvironmentResourceOpenAIHosted: …`

    An environment hosted by OpenAI.

    - `id: str`

      The public ID of the environment.

    - `capability_directories: List[str]`

      Directories that contain capabilities exposed to the agent.

    - `desktop: EnvironmentResourceOpenAIHostedDesktop`

      The effective desktop configuration.

      - `enabled: bool`

        Whether the environment provisions a desktop and browser proxy.

    - `files: List[HostedEnvironmentFile]`

      Files available in the environment, excluding their contents.

      - `class HostedEnvironmentFileID: …`

        A file copied from the OpenAI Files API.

        - `id: str`

          The session-scoped ID of the file in the execution environment.

        - `file_id: str`

          The ID of the uploaded file.

        - `path: str`

          The file's absolute path inside the environment.

        - `size_bytes: int`

          The decoded file size in bytes.

        - `type: Literal["file_id"]`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `class HostedEnvironmentFileResourceInline: …`

        A file supplied inline when the session was created.

        - `id: str`

          The session-scoped ID of the file in the execution environment.

        - `path: str`

          The file's absolute path inside the environment.

        - `size_bytes: int`

          The decoded file size in bytes.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network: EnvironmentResourceOpenAIHostedNetwork`

      The effective network access policy for the environment.

      - `access: Literal["enabled", "disabled", "restricted"]`

        The environment's network access mode.

        - `"enabled"`

          Allows unrestricted network access.

        - `"disabled"`

          Disables network access.

        - `"restricted"`

          Applies the configured domain restrictions.

      - `allowed_domains: List[str]`

        Domains the environment may access when network access is restricted.

    - `packages: EnvironmentResourceOpenAIHostedPackages`

      Packages installed in the environment.

      - `npm: List[str]`

        npm packages installed globally in the environment.

      - `python: List[str]`

        Python packages installed in the environment.

      - `system: List[str]`

        System packages installed in the environment.

    - `plugins: List[HostedPlugin]`

      Plugins installed in the environment, excluding their archive contents.

      - `description: str`

        The installed plugin description.

      - `name: str`

        The installed plugin name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

    - `skills: List[HostedSkill]`

      Skills installed in the environment, excluding their archive contents.

      - `class HostedSkillReference: …`

        A skill installed from the Skills API.

        - `description: str`

          The installed skill description.

        - `name: str`

          The installed skill name.

        - `skill_id: str`

          The referenced skill ID.

        - `type: Literal["skill_reference"]`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version: str`

          The concrete skill version installed for this session.

      - `class HostedSkillResourceInline: …`

        A skill installed from an inline ZIP archive.

        - `description: str`

          The installed skill description.

        - `name: str`

          The installed skill name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

    - `type: Literal["openai_hosted"]`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `container_size: Optional[Literal["small", "medium", "large"]]`

      The effective CPU and memory tier, or null when unknown or outside the public tiers.

      - `"small"`

      - `"medium"`

      - `"large"`

  - `class EnvironmentResourceSelfHosted: …`

    An environment hosted by the application.

    - `id: str`

      The public ID of the environment.

    - `capability_directories: List[str]`

      Directories that contain capabilities exposed to the agent.

    - `remote_url: str`

      Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

    - `type: Literal["self_hosted"]`

      The type of the object. Always `self_hosted`.

      - `"self_hosted"`

    - `workspace_directory: str`

      The absolute project directory inside the environment. Defaults to `/workspace`.

### Environment Param

- `EnvironmentParam`

  The execution environment and optional reusable template for a session.

  - `class EnvironmentParamNone: …`

    Runs the agent without an execution environment.

    - `type: Literal["none"]`

      The type of the object. Always `none`.

      - `"none"`

  - `class EnvironmentParamOpenAIHosted: …`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: Literal["openai_hosted"]`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `capability_directories: Optional[List[str]]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size: Optional[Literal["small", "medium", "large"]]`

      The hosted container size. Omission selects the medium tier.

      - `"small"`

      - `"medium"`

      - `"large"`

    - `desktop: Optional[EnvironmentParamOpenAIHostedDesktop]`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: bool`

        Whether to provision the desktop and its browser proxy.

    - `env: Optional[Dict[str, str]]`

      Environment variables made available to the agent.

    - `environment_template_id: Optional[str]`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Optional[List[HostedEnvironmentFileParam]]`

      Files available before the agent starts. Defaults to an empty list.

      - `class HostedEnvironmentFileParamFileID: …`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: str`

          The ID of the uploaded file.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["file_id"]`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `class HostedEnvironmentFileParamInline: …`

        A file supplied directly as standard-base64 data.

        - `data: str`

          The standard-base64-encoded file contents.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network: Optional[EnvironmentParamOpenAIHostedNetwork]`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `access: Literal["enabled", "disabled", "restricted"]`

        The environment's network access mode.

        - `"enabled"`

          Allows unrestricted network access.

        - `"disabled"`

          Disables network access.

        - `"restricted"`

          Applies the configured domain restrictions.

      - `allowed_domains: Optional[List[str]]`

        Domains the environment may access when network access is restricted.

      - `blocked_domains: Optional[List[str]]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Optional[EnvironmentParamOpenAIHostedPackages]`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Optional[List[str]]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Optional[List[str]]`

        Python packages to install. Defaults to an empty list.

      - `system: Optional[List[str]]`

        System packages to install. Defaults to an empty list.

    - `plugins: Optional[List[HostedPluginParam]]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: str`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: str`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: str`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: Literal["application/zip"]`

          The archive media type, always `application/zip`.

          - `"application/zip"`

            A ZIP archive.

        - `type: Literal["base64"]`

          The type of the object. Always `base64`.

          - `"base64"`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

    - `setup_commands: Optional[List[SetupCommandParam]]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: str`

        The shell command to execute.

      - `cwd: Optional[str]`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Optional[List[HostedSkillParam]]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class HostedSkillParamSkillReference: …`

        References a skill uploaded through the Skills API.

        - `skill_id: str`

          The ID of the skill created through `/v1/skills`.

        - `type: Literal["skill_reference"]`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version: Optional[str]`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class HostedSkillParamInline: …`

        Supplies a skill ZIP directly in the session request.

        - `description: str`

          The skill description declared in `SKILL.md`.

        - `name: str`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

  - `class EnvironmentParamSelfHosted: …`

    An application-hosted environment configured inline.

    - `type: Literal["self_hosted"]`

      The type of the object. Always `self_hosted`.

      - `"self_hosted"`

    - `workspace_directory: str`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories: Optional[List[str]]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

### Hosted Environment File

- `HostedEnvironmentFile`

  Metadata for a file materialized in an OpenAI-hosted execution environment.

  - `class HostedEnvironmentFileID: …`

    A file copied from the OpenAI Files API.

    - `id: str`

      The session-scoped ID of the file in the execution environment.

    - `file_id: str`

      The ID of the uploaded file.

    - `path: str`

      The file's absolute path inside the environment.

    - `size_bytes: int`

      The decoded file size in bytes.

    - `type: Literal["file_id"]`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `class HostedEnvironmentFileResourceInline: …`

    A file supplied inline when the session was created.

    - `id: str`

      The session-scoped ID of the file in the execution environment.

    - `path: str`

      The file's absolute path inside the environment.

    - `size_bytes: int`

      The decoded file size in bytes.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Environment File ID

- `class HostedEnvironmentFileID: …`

  A file copied from the OpenAI Files API.

  - `id: str`

    The session-scoped ID of the file in the execution environment.

  - `file_id: str`

    The ID of the uploaded file.

  - `path: str`

    The file's absolute path inside the environment.

  - `size_bytes: int`

    The decoded file size in bytes.

  - `type: Literal["file_id"]`

    The type of the object. Always `file_id`.

    - `"file_id"`

### Hosted Environment File Param

- `HostedEnvironmentFileParam`

  A file materialized in an OpenAI-hosted execution environment.

  - `class HostedEnvironmentFileParamFileID: …`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: str`

      The ID of the uploaded file.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["file_id"]`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `class HostedEnvironmentFileParamInline: …`

    A file supplied directly as standard-base64 data.

    - `data: str`

      The standard-base64-encoded file contents.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Plugin

- `class HostedPlugin: …`

  A plugin installed from an inline ZIP archive.

  - `description: str`

    The installed plugin description.

  - `name: str`

    The installed plugin name.

  - `type: Literal["inline"]`

    The type of the object. Always `inline`.

    - `"inline"`

### Hosted Plugin Param

- `class HostedPluginParam: …`

  Supplies a plugin ZIP directly in the session request.

  - `description: str`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: str`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: str`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: Literal["application/zip"]`

      The archive media type, always `application/zip`.

      - `"application/zip"`

        A ZIP archive.

    - `type: Literal["base64"]`

      The type of the object. Always `base64`.

      - `"base64"`

  - `type: Literal["inline"]`

    The type of the object. Always `inline`.

    - `"inline"`

### Hosted Skill

- `HostedSkill`

  A skill installed in an OpenAI-hosted environment.

  - `class HostedSkillReference: …`

    A skill installed from the Skills API.

    - `description: str`

      The installed skill description.

    - `name: str`

      The installed skill name.

    - `skill_id: str`

      The referenced skill ID.

    - `type: Literal["skill_reference"]`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: str`

      The concrete skill version installed for this session.

  - `class HostedSkillResourceInline: …`

    A skill installed from an inline ZIP archive.

    - `description: str`

      The installed skill description.

    - `name: str`

      The installed skill name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Skill Param

- `HostedSkillParam`

  A skill installed in an OpenAI-hosted environment.

  - `class HostedSkillParamSkillReference: …`

    References a skill uploaded through the Skills API.

    - `skill_id: str`

      The ID of the skill created through `/v1/skills`.

    - `type: Literal["skill_reference"]`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: Optional[str]`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class HostedSkillParamInline: …`

    Supplies a skill ZIP directly in the session request.

    - `description: str`

      The skill description declared in `SKILL.md`.

    - `name: str`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: str`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: Literal["application/zip"]`

        The archive media type, always `application/zip`.

        - `"application/zip"`

          A ZIP archive.

      - `type: Literal["base64"]`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Skill Reference

- `class HostedSkillReference: …`

  A skill installed from the Skills API.

  - `description: str`

    The installed skill description.

  - `name: str`

    The installed skill name.

  - `skill_id: str`

    The referenced skill ID.

  - `type: Literal["skill_reference"]`

    The type of the object. Always `skill_reference`.

    - `"skill_reference"`

  - `version: str`

    The concrete skill version installed for this session.

### Inline Capability Source Param

- `class InlineCapabilitySourceParam: …`

  Provides ZIP bytes encoded with standard base64.

  - `data: str`

    Standard-base64 encoded ZIP archive bytes.

  - `media_type: Literal["application/zip"]`

    The archive media type, always `application/zip`.

    - `"application/zip"`

      A ZIP archive.

  - `type: Literal["base64"]`

    The type of the object. Always `base64`.

    - `"base64"`

### Input Content

- `InputContent`

  User-provided content recorded in a session item.

  - `class InputContentResourceInputText: …`

    Text input recorded in a session item.

    - `text: str`

      The text supplied to the agent.

    - `type: Literal["input_text"]`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `class InputContentResourceInputImage: …`

    Image input recorded in a session item.

    - `image_url: str`

      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

    - `type: Literal["input_image"]`

      The type of the object. Always `input_image`.

      - `"input_image"`

### Input Content Param

- `InputContentParam`

  Content included in an input message.

  - `class InputContentParamInputText: …`

    Text input to the model.

    - `text: str`

      The text sent to the model.

    - `type: Literal["input_text"]`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `class InputContentParamInputImage: …`

    Image input to the model.

    - `image_url: str`

      The URL of the image sent to the model.

    - `type: Literal["input_image"]`

      The type of the object. Always `input_image`.

      - `"input_image"`

### Mcp Transport

- `McpTransport`

  The transport used to connect to an MCP server.

  - `class McpTransportResourceHTTP: …`

    Connects to an MCP server over HTTP.

    - `server_url: str`

      The URL of the MCP server.

    - `type: Literal["http"]`

      The type of the object. Always `http`.

      - `"http"`

  - `class McpTransportResourceStdio: …`

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

### Mcp Transport Param

- `McpTransportParam`

  The transport used to connect to an MCP server.

  - `class McpTransportConfigParamHTTP: …`

    Connects to an MCP server over HTTP.

    - `server_url: str`

      The URL of the MCP server.

    - `type: Literal["http"]`

      The type of the object. Always `http`.

      - `"http"`

    - `authorization: Optional[str]`

      The authorization value sent to the MCP server, if any.

    - `headers: Optional[Dict[str, str]]`

      Additional HTTP headers sent to the MCP server.

  - `class McpTransportConfigParamStdio: …`

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

    - `env: Optional[Dict[str, str]]`

      Environment variables set for the MCP server process.

    - `env_vars: Optional[List[str]]`

      Environment variable names to inherit from the selected execution environment.

### Multi Agent Config

- `class MultiAgentConfig: …`

  The resolved configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled. Defaults to false.

  - `max_concurrent_subagents: Optional[int]`

    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

### Multi Agent Config Param

- `class MultiAgentConfigParam: …`

  Explicit configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Optional[int]`

    Maximum number of subagents that may run concurrently. Defaults to 6.

### Output Text

- `class OutputText: …`

  A text content part produced by the agent.

  - `text: str`

    The text produced by the agent.

  - `type: Literal["output_text"]`

    The content type. Always `output_text`.

    - `"output_text"`

### Persisted Agent Tool

- `PersistedAgentTool`

  A credential-free tool available to a reusable agent.

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

### Persisted Agent Tool Param

- `PersistedAgentToolParam`

  A tool that can be stored on a reusable agent without session credentials.

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

### Persisted Mcp Transport

- `PersistedMcpTransport`

  A credential-free transport used to connect to an MCP server.

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

### Persisted Mcp Transport Param

- `PersistedMcpTransportParam`

  A credential-free transport used to connect to an MCP server.

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

### Session Error

- `class SessionError: …`

  An error payload with the same public fields as Responses API streaming errors.

  - `code: Optional[str]`

    The machine-readable error code, if any.

  - `message: str`

    A customer-safe explanation of the error.

  - `param: Optional[str]`

    The request parameter associated with the error, if any.

  - `type: str`

    The error type.

### Session Turn Error

- `class SessionTurnError: …`

  A customer-safe error describing why a session request failed.

  - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

    A stable, machine-readable failure category.

    - `"context_length_exceeded"`

      The request exceeds the model's context window.

    - `"session_budget_exceeded"`

      The session has reached its usage budget.

    - `"usage_limit_exceeded"`

      The organization has reached a usage, plan, or billing limit.

    - `"credit_balance_exhausted"`

      The organization has no API credits remaining.

    - `"rate_limit_exceeded"`

      The request exceeds the available rate limit.

    - `"flex_unavailable"`

      Flex processing is temporarily unavailable.

    - `"server_overloaded"`

      The model service is temporarily overloaded.

    - `"cyber_policy"`

      The request was rejected by a safety policy.

    - `"misalignment_policy_violation"`

      The request was blocked by the safety systems.

    - `"connection_failed"`

      The request could not connect to the model service.

    - `"server_error"`

      The model service encountered an unexpected error.

    - `"authentication_error"`

      The API credentials are invalid or lack the required access.

    - `"invalid_request"`

      The request contains invalid input or configuration.

    - `"resource_not_found"`

      The requested model or resource is unavailable.

    - `"sandbox_error"`

      The request could not complete in its execution environment.

    - `"executor_version_incompatible"`

      The executor must be upgraded before it can run this turn.

    - `"active_turn_not_steerable"`

      The session cannot accept additional input while a request is running.

    - `"request_timeout"`

      The request timed out before the model service responded.

    - `"internal_error"`

      An unexpected internal error prevented the session request from completing.

  - `message: str`

    A customer-safe explanation of the failure.

### Setup Command Param

- `class SetupCommandParam: …`

  A confidential setup command executed before the hosted agent starts.

  - `command: str`

    The shell command to execute.

  - `cwd: Optional[str]`

    The absolute working directory. Defaults to `/workspace`.

### Subagent

- `class Subagent: …`

  A subagent created within a session.

  - `id: str`

    The ID of the subagent.

  - `closed_at: Optional[int]`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Optional[List[AgentContent]]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: Optional[str]`

    The runner-assigned nickname, or null when unavailable.

  - `object: Literal["agent.session.subagent"]`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: int`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: str`

    The ID of the agent that created this subagent.

  - `session_id: str`

    The ID of the session that owns the subagent.

  - `status: Literal["active", "closed"]`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Summary Text

- `class SummaryText: …`

  A reasoning summary content part.

  - `text: str`

    The reasoning summary text.

  - `type: Literal["summary_text"]`

    The content type. Always `summary_text`.

    - `"summary_text"`

### Text Format

- `TextFormat`

  The effective output format for generated text.

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

### Text Format Param

- `TextFormatParam`

  The output format for generated text.

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

### Token Usage

- `class TokenUsage: …`

  Recorded token usage for a session or turn. Usage is best effort and may change.

  - `input_tokens: int`

    The number of input tokens used by the agent.

  - `input_tokens_details: InputTokensDetails`

    A breakdown of the agent's input token usage.

    - `cached_tokens: int`

      The number of input tokens retrieved from the prompt cache.

  - `output_tokens: int`

    The number of output tokens generated by the agent.

  - `output_tokens_details: OutputTokensDetails`

    A breakdown of the agent's output token usage.

    - `reasoning_tokens: int`

      The number of output tokens used for reasoning.

  - `total_tokens: int`

    The total number of input and output tokens used by the agent.

### Web Search Action

- `WebSearchAction`

  An action performed by the web search tool.

  - `class WebSearchActionResourceSearch: …`

    A search query or group of search queries.

    - `queries: Optional[List[str]]`

      The search queries, when multiple queries were used.

    - `query: Optional[str]`

      The search query, when a single query was used.

    - `type: Literal["search"]`

      The type of the object. Always `search`.

      - `"search"`

  - `class WebSearchActionResourceOpenPage: …`

    Opens a web page.

    - `type: Literal["open_page"]`

      The type of the object. Always `open_page`.

      - `"open_page"`

    - `url: Optional[str]`

      The URL of the page that was opened.

  - `class WebSearchActionResourceFindInPage: …`

    Finds text within a web page.

    - `pattern: Optional[str]`

      The text pattern that was searched for.

    - `type: Literal["find_in_page"]`

      The type of the object. Always `find_in_page`.

      - `"find_in_page"`

    - `url: Optional[str]`

      The URL of the page that was searched.

  - `class WebSearchActionResourceOther: …`

    Another web search action.

    - `type: Literal["other"]`

      The type of the object. Always `other`.

      - `"other"`

# Environments

## Retrieve an agent environment

`beta.agents.environments.retrieve(strenvironment_id)  -> EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environment_id: str`

### Returns

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "connected", "disconnected", 2 more]`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_info = client.beta.agents.environments.retrieve(
    "environment_id",
)
print(environment_info.id)
```

#### Response

```json
{
  "id": "id",
  "files": [
    {
      "id": "id",
      "file_id": "file_id",
      "path": "path",
      "size_bytes": 0,
      "type": "file_id"
    }
  ],
  "object": "agent.environment",
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "description": "description",
      "name": "name",
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "status": "pending",
  "type": "openai_hosted"
}
```

## Domain Types

### Environment Info

- `class EnvironmentInfo: …`

  Safe metadata for a first-class execution environment.

  - `id: str`

    The ID of the environment.

  - `files: List[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID: …`

      A file copied from the OpenAI Files API.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class HostedEnvironmentFileResourceInline: …`

      A file supplied inline when the session was created.

      - `id: str`

        The session-scoped ID of the file in the execution environment.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded file size in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: Literal["agent.environment"]`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: List[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference: …`

      A skill installed from the Skills API.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: str`

        The concrete skill version installed for this session.

    - `class HostedSkillResourceInline: …`

      A skill installed from an inline ZIP archive.

      - `description: str`

        The installed skill description.

      - `name: str`

        The installed skill name.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: Literal["pending", "connected", "disconnected", 2 more]`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: Literal["openai_hosted", "self_hosted"]`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

# Files

## Create an agent environment file

`beta.agents.environments.files.create(strenvironment_id, FileCreateParams**kwargs)  -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `file_id: Optional[str]`

  The ID of the uploaded file.

- `path: Optional[str]`

  The absolute destination path inside `/workspace`.

- `type: Optional[Literal["file_id"]]`

  The type of the object. Always `file_id`.

  - `"file_id"`

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_file = client.beta.agents.environments.files.create(
    environment_id="environment_id",
)
print(environment_file.environment_id)
```

#### Response

```json
{
  "environment_id": "environment_id",
  "object": "agent.environment.file",
  "path": "path",
  "size_bytes": 0
}
```

## List agent environment files

`beta.agents.environments.files.list(strenvironment_id, FileListParams**kwargs)  -> SyncTokenPage[EnvironmentFile]`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: str`

- `limit: Optional[int]`

  The maximum number of files to return, between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort by case-sensitive path components. Defaults to descending.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `page: Optional[str]`

  The opaque token from the previous page. Keep the same path, order, and limit.

- `path: Optional[str]`

  Restrict the listing to this absolute workspace directory.

### Returns

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.environments.files.list(
    environment_id="environment_id",
)
page = page.data[0]
print(page.environment_id)
```

#### Response

```json
{
  "data": [
    {
      "environment_id": "environment_id",
      "object": "agent.environment.file",
      "path": "path",
      "size_bytes": 0
    }
  ],
  "has_more": true,
  "next": "next",
  "object": "page"
}
```

## Domain Types

### Environment File

- `class EnvironmentFile: …`

  A live file in an execution environment.

  - `environment_id: str`

    The ID of the environment containing this file.

  - `object: Literal["agent.environment.file"]`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: str`

    The absolute file path inside the environment's workspace.

  - `size_bytes: int`

    The file size in bytes.

# Templates

## Create an agent environment template

`beta.agents.environments.templates.create(TemplateCreateParams**kwargs)  -> EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `capability_directories: Optional[Sequence[str]]`

  Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `desktop: Optional[Desktop]`

  Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Optional[Dict[str, str]]`

  Environment variables made available to the agent.

- `files: Optional[Iterable[HostedEnvironmentFileParam]]`

  Files available before the agent starts. Defaults to an empty list.

  - `class HostedEnvironmentFileParamFileID: …`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: str`

      The ID of the uploaded file.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["file_id"]`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `class HostedEnvironmentFileParamInline: …`

    A file supplied directly as standard-base64 data.

    - `data: str`

      The standard-base64-encoded file contents.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

- `name: Optional[str]`

  An optional human-readable display name for the template.

- `network: Optional[Network]`

  Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

  - `access: Literal["enabled", "disabled", "restricted"]`

    The environment's network access mode.

    - `enabled` - Allows unrestricted network access.
    - `disabled` - Disables network access.
    - `restricted` - Applies the configured domain restrictions.

    - `"enabled"`

      Allows unrestricted network access.

    - `"disabled"`

      Disables network access.

    - `"restricted"`

      Applies the configured domain restrictions.

  - `allowed_domains: Optional[Sequence[str]]`

    Domains the environment may access when network access is restricted.

  - `blocked_domains: Optional[Sequence[str]]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Optional[Packages]`

  Packages to install in the environment. Defaults to empty package lists.

  - `npm: Optional[Sequence[str]]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Optional[Sequence[str]]`

    Python packages to install. Defaults to an empty list.

  - `system: Optional[Sequence[str]]`

    System packages to install. Defaults to an empty list.

- `plugins: Optional[Iterable[HostedPluginParam]]`

  Plugins provided as inline ZIP archives. Defaults to an empty list.

  - `description: str`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: str`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: str`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: Literal["application/zip"]`

      The archive media type, always `application/zip`.

      - `"application/zip"`

        A ZIP archive.

    - `type: Literal["base64"]`

      The type of the object. Always `base64`.

      - `"base64"`

  - `type: Literal["inline"]`

    The type of the object. Always `inline`.

    - `"inline"`

- `setup_commands: Optional[Iterable[SetupCommandParam]]`

  Ordered, confidential setup commands. Command bodies are never returned.

  - `command: str`

    The shell command to execute.

  - `cwd: Optional[str]`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Optional[Iterable[HostedSkillParam]]`

  Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

  - `class HostedSkillParamSkillReference: …`

    References a skill uploaded through the Skills API.

    - `skill_id: str`

      The ID of the skill created through `/v1/skills`.

    - `type: Literal["skill_reference"]`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: Optional[str]`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class HostedSkillParamInline: …`

    Supplies a skill ZIP directly in the session request.

    - `description: str`

      The skill description declared in `SKILL.md`.

    - `name: str`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Returns

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.create()
print(environment_template.id)
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Delete an agent environment template

`beta.agents.environments.templates.delete(strenvironment_template_id)  -> EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: str`

### Returns

- `class EnvironmentTemplateDeleted: …`

  A deleted reusable environment template.

  - `id: str`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: Literal["agent.environment.template.deleted"]`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template_deleted = client.beta.agents.environments.templates.delete(
    "environment_template_id",
)
print(environment_template_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.environment.template.deleted"
}
```

## List agent environment templates

`beta.agents.environments.templates.list(TemplateListParams**kwargs)  -> SyncCursorPage[EnvironmentTemplate]`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.environments.templates.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "capability_directories": [
        "string"
      ],
      "created_at": 0,
      "desktop": {
        "enabled": true
      },
      "files": [
        {
          "file_id": "file_id",
          "path": "path",
          "type": "file_id"
        }
      ],
      "name": "name",
      "network": {
        "access": "enabled",
        "allowed_domains": [
          "string"
        ]
      },
      "object": "agent.environment.template",
      "packages": {
        "npm": [
          "string"
        ],
        "python": [
          "string"
        ],
        "system": [
          "string"
        ]
      },
      "plugins": [
        {
          "description": "description",
          "name": "name",
          "type": "inline"
        }
      ],
      "skills": [
        {
          "skill_id": "skill_id",
          "type": "skill_reference",
          "version": "version"
        }
      ],
      "updated_at": 0
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent environment template

`beta.agents.environments.templates.retrieve(strenvironment_template_id)  -> EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: str`

### Returns

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.retrieve(
    "environment_template_id",
)
print(environment_template.id)
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Update an agent environment template

`beta.agents.environments.templates.update(strenvironment_template_id, TemplateUpdateParams**kwargs)  -> EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: str`

- `capability_directories: Optional[Sequence[str]]`

  Directories that expose capabilities to the agent.

- `desktop: Optional[Desktop]`

  Replacement desktop configuration, or null to disable the desktop.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Optional[Dict[str, str]]`

  Replacement confidential environment values.

- `files: Optional[Iterable[HostedEnvironmentFileParam]]`

  Replacement file configuration materialized for each new session.

  - `class HostedEnvironmentFileParamFileID: …`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: str`

      The ID of the uploaded file.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["file_id"]`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `class HostedEnvironmentFileParamInline: …`

    A file supplied directly as standard-base64 data.

    - `data: str`

      The standard-base64-encoded file contents.

    - `path: str`

      The absolute destination path inside `/workspace`.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

- `name: Optional[str]`

  A replacement human-readable display name, or `null` to clear the name.

- `network: Optional[Network]`

  Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

  - `access: Literal["enabled", "disabled", "restricted"]`

    The environment's network access mode.

    - `enabled` - Allows unrestricted network access.
    - `disabled` - Disables network access.
    - `restricted` - Applies the configured domain restrictions.

    - `"enabled"`

      Allows unrestricted network access.

    - `"disabled"`

      Disables network access.

    - `"restricted"`

      Applies the configured domain restrictions.

  - `allowed_domains: Optional[Sequence[str]]`

    Domains the environment may access when network access is restricted.

  - `blocked_domains: Optional[Sequence[str]]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Optional[Packages]`

  Packages installed before the runtime network policy applies.

  - `npm: Optional[Sequence[str]]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Optional[Sequence[str]]`

    Python packages to install. Defaults to an empty list.

  - `system: Optional[Sequence[str]]`

    System packages to install. Defaults to an empty list.

- `plugins: Optional[Iterable[HostedPluginParam]]`

  Replacement plugin configuration installed for each new session.

  - `description: str`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: str`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: str`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: Literal["application/zip"]`

      The archive media type, always `application/zip`.

      - `"application/zip"`

        A ZIP archive.

    - `type: Literal["base64"]`

      The type of the object. Always `base64`.

      - `"base64"`

  - `type: Literal["inline"]`

    The type of the object. Always `inline`.

    - `"inline"`

- `setup_commands: Optional[Iterable[SetupCommandParam]]`

  Replacement confidential setup commands, never included in returned resources.

  - `command: str`

    The shell command to execute.

  - `cwd: Optional[str]`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Optional[Iterable[HostedSkillParam]]`

  Replacement skill configuration installed for each new session.

  - `class HostedSkillParamSkillReference: …`

    References a skill uploaded through the Skills API.

    - `skill_id: str`

      The ID of the skill created through `/v1/skills`.

    - `type: Literal["skill_reference"]`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: Optional[str]`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class HostedSkillParamInline: …`

    Supplies a skill ZIP directly in the session request.

    - `description: str`

      The skill description declared in `SKILL.md`.

    - `name: str`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

### Returns

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
environment_template = client.beta.agents.environments.templates.update(
    environment_template_id="environment_template_id",
)
print(environment_template.id)
```

#### Response

```json
{
  "id": "id",
  "capability_directories": [
    "string"
  ],
  "created_at": 0,
  "desktop": {
    "enabled": true
  },
  "files": [
    {
      "file_id": "file_id",
      "path": "path",
      "type": "file_id"
    }
  ],
  "name": "name",
  "network": {
    "access": "enabled",
    "allowed_domains": [
      "string"
    ]
  },
  "object": "agent.environment.template",
  "packages": {
    "npm": [
      "string"
    ],
    "python": [
      "string"
    ],
    "system": [
      "string"
    ]
  },
  "plugins": [
    {
      "description": "description",
      "name": "name",
      "type": "inline"
    }
  ],
  "skills": [
    {
      "skill_id": "skill_id",
      "type": "skill_reference",
      "version": "version"
    }
  ],
  "updated_at": 0
}
```

## Domain Types

### Environment Template

- `class EnvironmentTemplate: …`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: str`

    The ID of the reusable environment template.

  - `capability_directories: List[str]`

    Directories that expose capabilities to the agent.

  - `created_at: int`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: List[File]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileHostedTemplateFileResourceFileID: …`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: str`

        The ID of the uploaded file.

      - `path: str`

        The file's absolute path inside the environment.

      - `type: Literal["file_id"]`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `class FileHostedTemplateFileResourceInline: …`

      Metadata for confidential inline file contents.

      - `path: str`

        The file's absolute path inside the environment.

      - `size_bytes: int`

        The decoded size of the inline file in bytes.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: Optional[str]`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: Literal["enabled", "disabled", "restricted"]`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: List[str]`

      Domains the environment may access when network access is restricted.

  - `object: Literal["agent.environment.template"]`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: List[str]`

      npm packages installed globally in the environment.

    - `python: List[str]`

      Python packages installed in the environment.

    - `system: List[str]`

      System packages installed in the environment.

  - `plugins: List[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: str`

      The installed plugin description.

    - `name: str`

      The installed plugin name.

    - `type: Literal["inline"]`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: List[Skill]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillHostedTemplateSkillResourceSkillReference: …`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: str`

        The referenced skill ID.

      - `type: Literal["skill_reference"]`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: Optional[str]`

        The requested version selector, including `latest`.

    - `class SkillHostedTemplateSkillResourceInline: …`

      Safe metadata for an inline skill archive.

      - `description: str`

        The skill description declared in `SKILL.md`.

      - `name: str`

        The skill name declared in `SKILL.md`.

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: int`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `class EnvironmentTemplateDeleted: …`

  A deleted reusable environment template.

  - `id: str`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: Literal["agent.environment.template.deleted"]`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

# Sessions

## Create an agent session

`beta.agents.sessions.create(SessionCreateParams**kwargs)  -> AgentSession`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `environment: EnvironmentParam`

  An inline execution environment or a reference to an environment template.

  - `class EnvironmentParamNone: …`

    Runs the agent without an execution environment.

    - `type: Literal["none"]`

      The type of the object. Always `none`.

      - `"none"`

  - `class EnvironmentParamOpenAIHosted: …`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: Literal["openai_hosted"]`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `capability_directories: Optional[List[str]]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size: Optional[Literal["small", "medium", "large"]]`

      The hosted container size. Omission selects the medium tier.

      - `"small"`

      - `"medium"`

      - `"large"`

    - `desktop: Optional[EnvironmentParamOpenAIHostedDesktop]`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: bool`

        Whether to provision the desktop and its browser proxy.

    - `env: Optional[Dict[str, str]]`

      Environment variables made available to the agent.

    - `environment_template_id: Optional[str]`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Optional[List[HostedEnvironmentFileParam]]`

      Files available before the agent starts. Defaults to an empty list.

      - `class HostedEnvironmentFileParamFileID: …`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: str`

          The ID of the uploaded file.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["file_id"]`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `class HostedEnvironmentFileParamInline: …`

        A file supplied directly as standard-base64 data.

        - `data: str`

          The standard-base64-encoded file contents.

        - `path: str`

          The absolute destination path inside `/workspace`.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network: Optional[EnvironmentParamOpenAIHostedNetwork]`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `access: Literal["enabled", "disabled", "restricted"]`

        The environment's network access mode.

        - `"enabled"`

          Allows unrestricted network access.

        - `"disabled"`

          Disables network access.

        - `"restricted"`

          Applies the configured domain restrictions.

      - `allowed_domains: Optional[List[str]]`

        Domains the environment may access when network access is restricted.

      - `blocked_domains: Optional[List[str]]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Optional[EnvironmentParamOpenAIHostedPackages]`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Optional[List[str]]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Optional[List[str]]`

        Python packages to install. Defaults to an empty list.

      - `system: Optional[List[str]]`

        System packages to install. Defaults to an empty list.

    - `plugins: Optional[List[HostedPluginParam]]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: str`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: str`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: str`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: Literal["application/zip"]`

          The archive media type, always `application/zip`.

          - `"application/zip"`

            A ZIP archive.

        - `type: Literal["base64"]`

          The type of the object. Always `base64`.

          - `"base64"`

      - `type: Literal["inline"]`

        The type of the object. Always `inline`.

        - `"inline"`

    - `setup_commands: Optional[List[SetupCommandParam]]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: str`

        The shell command to execute.

      - `cwd: Optional[str]`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Optional[List[HostedSkillParam]]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class HostedSkillParamSkillReference: …`

        References a skill uploaded through the Skills API.

        - `skill_id: str`

          The ID of the skill created through `/v1/skills`.

        - `type: Literal["skill_reference"]`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version: Optional[str]`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class HostedSkillParamInline: …`

        Supplies a skill ZIP directly in the session request.

        - `description: str`

          The skill description declared in `SKILL.md`.

        - `name: str`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

  - `class EnvironmentParamSelfHosted: …`

    An application-hosted environment configured inline.

    - `type: Literal["self_hosted"]`

      The type of the object. Always `self_hosted`.

      - `"self_hosted"`

    - `workspace_directory: str`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories: Optional[List[str]]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `agent: Optional[Agent]`

  Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

  - `instructions: Optional[str]`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `model: Optional[str]`

    The model to use for the agent. The requested model name is preserved.

  - `multi_agent: Optional[MultiAgentConfigParam]`

    Configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents: Optional[int]`

      Maximum number of subagents that may run concurrently. Defaults to 6.

  - `reasoning: Optional[AgentReasoningParam]`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

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

    The service tier used for model requests.

    - `auto` - Selects the service tier automatically.
    - `default` - Uses the default service tier.
    - `flex` - Uses the flex service tier.
    - `priority` - Uses the priority service tier.
    - `fast` - Uses the fast service tier.
    - `ultrafast` - Uses the ultrafast service tier.

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

    Configuration for text generated by the agent.

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

  - `tools: Optional[Iterable[AgentToolParam]]`

    Tools available to the agent. Omit to inherit, or pass null to clear them.

    - `class AgentToolConfigParamFunction: …`

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

    - `class AgentToolConfigParamToolSearch: …`

      Discovers deferred function tools and loads them into the model context.

      - `type: Literal["tool_search"]`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `class AgentToolConfigParamProgrammaticToolCalling: …`

      Enables calling tools from model-generated code.

      - `type: Literal["programmatic_tool_calling"]`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

      - `enabled: Optional[bool]`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `class AgentToolConfigParamMcp: …`

      Tools provided by a remote MCP server.

      - `server_label: str`

        A label used to identify the MCP server in tool calls.

      - `transport: McpTransportParam`

        The transport used to connect to the MCP server.

        - `class McpTransportConfigParamHTTP: …`

          Connects to an MCP server over HTTP.

          - `server_url: str`

            The URL of the MCP server.

          - `type: Literal["http"]`

            The type of the object. Always `http`.

            - `"http"`

          - `authorization: Optional[str]`

            The authorization value sent to the MCP server, if any.

          - `headers: Optional[Dict[str, str]]`

            Additional HTTP headers sent to the MCP server.

        - `class McpTransportConfigParamStdio: …`

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

          - `env: Optional[Dict[str, str]]`

            Environment variables set for the MCP server process.

          - `env_vars: Optional[List[str]]`

            Environment variable names to inherit from the selected execution environment.

      - `type: Literal["mcp"]`

        The type of the object. Always `mcp`.

        - `"mcp"`

      - `allowed_tools: Optional[List[str]]`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin: Optional[Literal["service", "environment"]]`

        Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

        - `"service"`

          Uses the Managed Agents service network.

        - `"environment"`

          Uses the session's execution environment.

      - `credential_id: Optional[str]`

        The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

      - `request_metadata: Optional[Dict[str, object]]`

        Metadata included with requests to this MCP server.

      - `required: Optional[bool]`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `class AgentToolConfigParamWebSearch: …`

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

      - `location: Optional[AgentToolConfigParamWebSearchLocation]`

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

    - `class AgentToolConfigParamComputerUse: …`

      Browser use in an OpenAI-hosted session.

      - `type: Literal["computer_use"]`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

      - `include_screenshots: Optional[bool]`

        Whether computer tool outputs include screenshots. Defaults to `false`.

- `agent_id: Optional[str]`

  The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

- `input: Optional[Union[str, Iterable[AgentSessionInputMessageParam], null]]`

  Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

  - `str`

  - `Iterable[AgentSessionInputMessageParam]`

    - `content: List[InputContentParam]`

      The content of the message.

      - `class InputContentParamInputText: …`

        Text input to the model.

        - `text: str`

          The text sent to the model.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class InputContentParamInputImage: …`

        Image input to the model.

        - `image_url: str`

          The URL of the image sent to the model.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

    - `role: Literal["user"]`

      The role of the message author. Always `user`.

      - `"user"`

    - `type: Optional[Literal["message"]]`

      The type of the input item. Always `message`.

      - `"message"`

- `metadata: Optional[Dict[str, str]]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `stream: Optional[Literal[false]]`

  Whether to stream session events as server-sent events. Defaults to `false`.

  - `false`

- `vault_ids: Optional[Sequence[str]]`

  The IDs of vaults made available to the session.

### Returns

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

    - `tools: List[AgentTool]`

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

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

      - `class AgentToolResourceProgrammaticToolCalling: …`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: Literal["programmatic_tool_calling"]`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `class AgentToolResourceMcp: …`

        Tools provided by a remote MCP server.

        - `allowed_tools: Optional[List[str]]`

          The MCP tools the agent may call.

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

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

      - `class AgentToolResourceWebSearch: …`

        Web search.

        - `allowed_domains: Optional[List[str]]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

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

      - `class AgentToolResourceComputerUse: …`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: Literal["computer_use"]`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `access: Literal["enabled", "disabled", "restricted"]`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: List[str]`

          Domains the environment may access when network access is restricted.

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
for session in client.beta.agents.sessions.create(
    environment={
        "type": "none"
    },
):
  print(session)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
    "reasoning": {
      "effort": "none",
      "summary": "concise"
    },
    "service_tier": "auto",
    "text": {
      "format": {
        "type": "text"
      },
      "verbosity": "low"
    },
    "tools": [
      {
        "defer_loading": true,
        "description": "description",
        "name": "name",
        "parameters": {
          "foo": "bar"
        },
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

## Delete an agent session

`beta.agents.sessions.delete(strsession_id)  -> AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: str`

### Returns

- `class AgentSessionDeleted: …`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: str`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: Literal["agent.session.deleted"]`

    The object type. Always `agent.session.deleted`.

    - `"agent.session.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent_session_deleted = client.beta.agents.sessions.delete(
    "session_id",
)
print(agent_session_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.deleted"
}
```

## List agent sessions

`beta.agents.sessions.list(SessionListParams**kwargs)  -> SyncCursorPage[AgentSession]`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `agent_id: Optional[str]`

  Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

- `limit: Optional[int]`

  The maximum number of resources to return.

- `order: Optional[Literal["asc", "desc"]]`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

    - `tools: List[AgentTool]`

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

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

      - `class AgentToolResourceProgrammaticToolCalling: …`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: Literal["programmatic_tool_calling"]`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `class AgentToolResourceMcp: …`

        Tools provided by a remote MCP server.

        - `allowed_tools: Optional[List[str]]`

          The MCP tools the agent may call.

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

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

      - `class AgentToolResourceWebSearch: …`

        Web search.

        - `allowed_domains: Optional[List[str]]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

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

      - `class AgentToolResourceComputerUse: …`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: Literal["computer_use"]`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `access: Literal["enabled", "disabled", "restricted"]`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: List[str]`

          Domains the environment may access when network access is restricted.

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.list()
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent": {
        "id": "id",
        "instructions": "instructions",
        "model": "model",
        "multi_agent": {
          "enabled": true,
          "max_concurrent_subagents": 1
        },
        "name": "name",
        "reasoning": {
          "effort": "none",
          "summary": "concise"
        },
        "service_tier": "auto",
        "text": {
          "format": {
            "type": "text"
          },
          "verbosity": "low"
        },
        "tools": [
          {
            "defer_loading": true,
            "description": "description",
            "name": "name",
            "parameters": {
              "foo": "bar"
            },
            "type": "function"
          }
        ]
      },
      "created_at": 0,
      "environment": {
        "type": "none"
      },
      "error": "error",
      "last_active_at": 0,
      "metadata": {
        "foo": "string"
      },
      "object": "agent.session",
      "required_actions": [
        {
          "request": {
            "credential_origin": "credential_origin",
            "fields": [
              {
                "id": "id",
                "label": "label",
                "required": true,
                "type": "type"
              }
            ],
            "options": [
              {
                "id": "id",
                "field_ids": [
                  "string"
                ],
                "label": "label"
              }
            ],
            "reason": "reason",
            "type": "browser_authentication"
          },
          "request_id": "request_id",
          "turn_id": "turn_id",
          "type": "computer_use_approval_request"
        }
      ],
      "status": "idle",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      },
      "vault_ids": [
        "string"
      ]
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session

`beta.agents.sessions.retrieve(strsession_id)  -> AgentSession`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: str`

### Returns

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

    - `tools: List[AgentTool]`

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

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

      - `class AgentToolResourceProgrammaticToolCalling: …`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: Literal["programmatic_tool_calling"]`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `class AgentToolResourceMcp: …`

        Tools provided by a remote MCP server.

        - `allowed_tools: Optional[List[str]]`

          The MCP tools the agent may call.

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

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

      - `class AgentToolResourceWebSearch: …`

        Web search.

        - `allowed_domains: Optional[List[str]]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

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

      - `class AgentToolResourceComputerUse: …`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: Literal["computer_use"]`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `access: Literal["enabled", "disabled", "restricted"]`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: List[str]`

          Domains the environment may access when network access is restricted.

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent_session = client.beta.agents.sessions.retrieve(
    "session_id",
)
print(agent_session.id)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
    "reasoning": {
      "effort": "none",
      "summary": "concise"
    },
    "service_tier": "auto",
    "text": {
      "format": {
        "type": "text"
      },
      "verbosity": "low"
    },
    "tools": [
      {
        "defer_loading": true,
        "description": "description",
        "name": "name",
        "parameters": {
          "foo": "bar"
        },
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

## Update an agent session

`beta.agents.sessions.update(strsession_id, SessionUpdateParams**kwargs)  -> AgentSession`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: str`

- `agent: Optional[Agent]`

  Model settings for subsequent turns. Omitted fields stay unchanged.

  - `model: Optional[str]`

    The model for subsequent turns. Omit to keep the current model.

  - `reasoning: Optional[AgentReasoning]`

    Reasoning settings to update. Omit to keep the current effort.

    - `effort: Optional[Literal["none", "minimal", "low", 4 more]]`

      Omit to keep the current effort. Null selects the model's default effort.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

  - `service_tier: Optional[Literal["auto", "default", "flex", 3 more]]`

    Omit to keep the current tier. Null resets it to auto.

    - `auto` - Selects the service tier automatically.
    - `default` - Uses the default service tier.
    - `flex` - Uses the flex service tier.
    - `priority` - Uses the priority service tier.
    - `fast` - Uses the fast service tier.
    - `ultrafast` - Uses the ultrafast service tier.

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

- `metadata: Optional[Dict[str, str]]`

  Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class AgentSession: …`

  A Managed Agents session.

  - `id: str`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: str`

      The ID of the agent.

    - `instructions: Optional[str]`

      Custom instructions appended to the agent's default base instructions.

    - `model: str`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Optional[int]`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: Optional[str]`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

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

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `"auto"`

      - `"default"`

      - `"flex"`

      - `"priority"`

      - `"fast"`

      - `"ultrafast"`

    - `text: AgentText`

      Configuration for text generated by the agent.

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

    - `tools: List[AgentTool]`

      Tools available to the agent.

      - `class AgentToolResourceFunction: …`

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

      - `class AgentToolResourceProgrammaticToolCalling: …`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: Literal["programmatic_tool_calling"]`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `class AgentToolResourceMcp: …`

        Tools provided by a remote MCP server.

        - `allowed_tools: Optional[List[str]]`

          The MCP tools the agent may call.

        - `connection_origin: Literal["service", "environment"]`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: Optional[str]`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Dict[str, object]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: str`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class McpTransportResourceHTTP: …`

            Connects to an MCP server over HTTP.

            - `server_url: str`

              The URL of the MCP server.

            - `type: Literal["http"]`

              The type of the object. Always `http`.

              - `"http"`

          - `class McpTransportResourceStdio: …`

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

      - `class AgentToolResourceWebSearch: …`

        Web search.

        - `allowed_domains: Optional[List[str]]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: Literal["low", "medium", "high"]`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Optional[AgentToolResourceWebSearchLocation]`

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

      - `class AgentToolResourceComputerUse: …`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: Literal["computer_use"]`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: int`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class EnvironmentResourceNone: …`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: Literal["none"]`

        The type of the object. Always `none`.

        - `"none"`

    - `class EnvironmentResourceOpenAIHosted: …`

      An environment hosted by OpenAI.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: EnvironmentResourceOpenAIHostedDesktop`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: List[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID: …`

          A file copied from the OpenAI Files API.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `file_id: str`

            The ID of the uploaded file.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["file_id"]`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `class HostedEnvironmentFileResourceInline: …`

          A file supplied inline when the session was created.

          - `id: str`

            The session-scoped ID of the file in the execution environment.

          - `path: str`

            The file's absolute path inside the environment.

          - `size_bytes: int`

            The decoded file size in bytes.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: EnvironmentResourceOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `access: Literal["enabled", "disabled", "restricted"]`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: List[str]`

          Domains the environment may access when network access is restricted.

      - `packages: EnvironmentResourceOpenAIHostedPackages`

        Packages installed in the environment.

        - `npm: List[str]`

          npm packages installed globally in the environment.

        - `python: List[str]`

          Python packages installed in the environment.

        - `system: List[str]`

          System packages installed in the environment.

      - `plugins: List[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: str`

          The installed plugin description.

        - `name: str`

          The installed plugin name.

        - `type: Literal["inline"]`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: List[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference: …`

          A skill installed from the Skills API.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `skill_id: str`

            The referenced skill ID.

          - `type: Literal["skill_reference"]`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: str`

            The concrete skill version installed for this session.

        - `class HostedSkillResourceInline: …`

          A skill installed from an inline ZIP archive.

          - `description: str`

            The installed skill description.

          - `name: str`

            The installed skill name.

          - `type: Literal["inline"]`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: Literal["openai_hosted"]`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size: Optional[Literal["small", "medium", "large"]]`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `class EnvironmentResourceSelfHosted: …`

      An environment hosted by the application.

      - `id: str`

        The public ID of the environment.

      - `capability_directories: List[str]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: str`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: Literal["self_hosted"]`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: str`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: Optional[str]`

    The error that caused the session to fail, if any.

  - `last_active_at: int`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Dict[str, str]`

    Custom string key-value pairs attached to the session.

  - `object: Literal["agent.session"]`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: List[RequiredAction]`

    Actions that must be completed before the session can continue.

    - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

      Respond to a computer-use request.

      - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

        The information needed to render the request.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

          A browser origin awaiting the application's approval decision.

          - `origin: str`

            The origin the browser needs permission to access.

          - `reason: Optional[str]`

            The browser's explanation for this request, or null when unavailable.

          - `type: Literal["browser_origin_access"]`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: str`

        The registered request ID to echo when responding.

      - `turn_id: str`

        The turn that requested approval.

      - `type: Literal["computer_use_approval_request"]`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

      Run a function tool and submit its result.

      - `arguments: object`

        The arguments supplied by the model.

      - `call_id: str`

        The ID to include when submitting the function result.

      - `name: str`

        The function name.

      - `turn_id: str`

        The ID of the turn that requested the function call.

      - `type: Literal["function_call"]`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

      Reconnect a session environment.

      - `environment_id: str`

        The ID of the environment to reconnect.

      - `type: Literal["environment_connection"]`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

  - `vault_ids: List[str]`

    The IDs of vaults made available to the session.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
agent_session = client.beta.agents.sessions.update(
    session_id="session_id",
)
print(agent_session.id)
```

#### Response

```json
{
  "id": "id",
  "agent": {
    "id": "id",
    "instructions": "instructions",
    "model": "model",
    "multi_agent": {
      "enabled": true,
      "max_concurrent_subagents": 1
    },
    "name": "name",
    "reasoning": {
      "effort": "none",
      "summary": "concise"
    },
    "service_tier": "auto",
    "text": {
      "format": {
        "type": "text"
      },
      "verbosity": "low"
    },
    "tools": [
      {
        "defer_loading": true,
        "description": "description",
        "name": "name",
        "parameters": {
          "foo": "bar"
        },
        "type": "function"
      }
    ]
  },
  "created_at": 0,
  "environment": {
    "type": "none"
  },
  "error": "error",
  "last_active_at": 0,
  "metadata": {
    "foo": "string"
  },
  "object": "agent.session",
  "required_actions": [
    {
      "request": {
        "credential_origin": "credential_origin",
        "fields": [
          {
            "id": "id",
            "label": "label",
            "required": true,
            "type": "type"
          }
        ],
        "options": [
          {
            "id": "id",
            "field_ids": [
              "string"
            ],
            "label": "label"
          }
        ],
        "reason": "reason",
        "type": "browser_authentication"
      },
      "request_id": "request_id",
      "turn_id": "turn_id",
      "type": "computer_use_approval_request"
    }
  ],
  "status": "idle",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "vault_ids": [
    "string"
  ]
}
```

# Artifacts

## Retrieve agent session artifact content

`beta.agents.sessions.artifacts.content(strartifact_id, ArtifactContentParams**kwargs)  -> BinaryResponseContent`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: str`

- `artifact_id: str`

### Returns

- `BinaryResponseContent`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
response = client.beta.agents.sessions.artifacts.content(
    artifact_id="artifact_id",
    session_id="session_id",
)
print(response)
content = response.read()
print(content)
```

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(strartifact_id, ArtifactDeleteParams**kwargs)  -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: str`

- `artifact_id: str`

### Returns

- `class SessionArtifactDeleted: …`

  Confirmation that an immutable session artifact was deleted.

  - `id: str`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: Literal["agent.session.artifact.deleted"]`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
session_artifact_deleted = client.beta.agents.sessions.artifacts.delete(
    artifact_id="artifact_id",
    session_id="session_id",
)
print(session_artifact_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.session.artifact.deleted"
}
```

## List agent session artifacts

`beta.agents.sessions.artifacts.list(strsession_id, ArtifactListParams**kwargs)  -> SyncCursorPage[SessionArtifact]`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: str`

- `after: Optional[str]`

  Return artifacts after this immutable artifact ID.

- `environment_id: Optional[str]`

  Restrict the listing to artifacts produced by this environment.

- `limit: Optional[int]`

  The maximum number of artifacts to return, between 1 and 100.

- `order: Optional[Literal["asc", "desc"]]`

  Sort by creation time and ID. Defaults to descending.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class SessionArtifact: …`

  An immutable file published by a completed hosted session turn.

  - `id: str`

    The immutable artifact ID.

  - `created_at: int`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: str`

    The ID of the environment that produced the artifact.

  - `object: Literal["agent.session.artifact"]`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: str`

    The original absolute file path in the execution environment.

  - `session_id: str`

    The ID of the session that owns the artifact.

  - `size_bytes: int`

    The immutable artifact size in bytes.

  - `turn_id: str`

    The ID of the completed turn that published the artifact.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.artifacts.list(
    session_id="session_id",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "environment_id": "environment_id",
      "object": "agent.session.artifact",
      "path": "path",
      "session_id": "session_id",
      "size_bytes": 0,
      "turn_id": "turn_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session artifact

`beta.agents.sessions.artifacts.retrieve(strartifact_id, ArtifactRetrieveParams**kwargs)  -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: str`

- `artifact_id: str`

### Returns

- `class SessionArtifact: …`

  An immutable file published by a completed hosted session turn.

  - `id: str`

    The immutable artifact ID.

  - `created_at: int`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: str`

    The ID of the environment that produced the artifact.

  - `object: Literal["agent.session.artifact"]`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: str`

    The original absolute file path in the execution environment.

  - `session_id: str`

    The ID of the session that owns the artifact.

  - `size_bytes: int`

    The immutable artifact size in bytes.

  - `turn_id: str`

    The ID of the completed turn that published the artifact.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
session_artifact = client.beta.agents.sessions.artifacts.retrieve(
    artifact_id="artifact_id",
    session_id="session_id",
)
print(session_artifact.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "environment_id": "environment_id",
  "object": "agent.session.artifact",
  "path": "path",
  "session_id": "session_id",
  "size_bytes": 0,
  "turn_id": "turn_id"
}
```

## Domain Types

### Session Artifact

- `class SessionArtifact: …`

  An immutable file published by a completed hosted session turn.

  - `id: str`

    The immutable artifact ID.

  - `created_at: int`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: str`

    The ID of the environment that produced the artifact.

  - `object: Literal["agent.session.artifact"]`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: str`

    The original absolute file path in the execution environment.

  - `session_id: str`

    The ID of the session that owns the artifact.

  - `size_bytes: int`

    The immutable artifact size in bytes.

  - `turn_id: str`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `class SessionArtifactDeleted: …`

  Confirmation that an immutable session artifact was deleted.

  - `id: str`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: Literal["agent.session.artifact.deleted"]`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

# Events

## Create agent session input events

`beta.agents.sessions.events.create(strsession_id, EventCreateParams**kwargs)`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: str`

- `events: Iterable[AgentSessionInputParam]`

  The input events to submit to the session.

  - `class SessionInputParamAgentSessionInputComputerUseApprovalRequestResult: …`

    Responds to a pending Computer Use approval request.

    - `request_id: str`

      The registered request ID from the required action.

    - `response: SessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponse`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `fields: List[Field]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: str`

            The field ID from the required action.

          - `value: str`

            The value to enter into the registered control.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

        - `selected_option: Optional[str]`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class AgentBrowserOriginAccessParam: …`

        - `decision: Literal["approve", "deny", "cancel"]`

          Whether to allow, deny, or cancel the requested origin access.

          - `"approve"`

            Allow the browser to access this origin.

          - `"deny"`

            Deny access to this origin.

          - `"cancel"`

            Dismiss this request without approving access.

        - `type: Literal["browser_origin_access"]`

          - `"browser_origin_access"`

    - `type: Literal["agent.session.input.computer_use_approval_request_result"]`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `"agent.session.input.computer_use_approval_request_result"`

  - `class SessionInputParamAgentSessionInputMessage: …`

    Adds one or more user messages and starts a turn.

    - `input: List[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: List[InputContentParam]`

        The content of the message.

        - `class InputContentParamInputText: …`

          Text input to the model.

          - `text: str`

            The text sent to the model.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentParamInputImage: …`

          Image input to the model.

          - `image_url: str`

            The URL of the image sent to the model.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: Literal["user"]`

        The role of the message author. Always `user`.

        - `"user"`

      - `type: Optional[Literal["message"]]`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: Literal["agent.session.input.message"]`

      The type of the object. Always `agent.session.input.message`.

      - `"agent.session.input.message"`

  - `class SessionInputParamAgentSessionInputCancel: …`

    Cancels the session's active turn.

    - `type: Literal["agent.session.input.cancel"]`

      The type of the object. Always `agent.session.input.cancel`.

      - `"agent.session.input.cancel"`

  - `class SessionInputParamAgentSessionInputToolResult: …`

    Submits the result of a function call.

    - `call_id: str`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: str`

      The ID of the turn that requested the function call.

    - `type: Literal["agent.session.input.tool_result"]`

      The type of the object. Always `agent.session.input.tool_result`.

      - `"agent.session.input.tool_result"`

    - `error: Optional[str]`

      The error message when the call failed.

    - `output: Optional[AgentFunctionCallOutputParam]`

      The function result when the call succeeded.

      - `str`

      - `List[InputContentParam]`

        - `class InputContentParamInputText: …`

          Text input to the model.

        - `class InputContentParamInputImage: …`

          Image input to the model.

- `idempotency_key: Optional[str]`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
client.beta.agents.sessions.events.create(
    session_id="session_id",
    events=[{
        "request_id": "request_id",
        "response": {
            "action": "submit",
            "fields": [{
                "field_id": "field_id",
                "value": "value",
            }],
            "type": "browser_authentication",
        },
        "type": "agent.session.input.computer_use_approval_request_result",
    }],
)
```

## Stream agent session events

`beta.agents.sessions.events.stream(strsession_id)  -> AgentSessionEvent`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: str`

### Returns

- `AgentSessionEvent`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent: …`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: Optional[str]`

        The machine-readable error code, if any.

      - `message: str`

        A customer-safe explanation of the error.

      - `param: Optional[str]`

        The request parameter associated with the error, if any.

      - `type: str`

        The error type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `type: Literal["error"]`

      The type of the object. Always `error`.

      - `"error"`

  - `class AgentSessionEnvironmentReadyEvent: …`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: str`

        The public ID of the environment.

      - `error: Optional[Error]`

        The error reported while preparing the environment, if any.

        - `code: str`

          A machine-readable error code.

        - `message: str`

          A human-readable error message.

        - `type: str`

          The error type.

      - `status: Literal["pending", "ready", "connected", 2 more]`

        The environment's connection status.

        - `"pending"`

          The environment is being prepared.

        - `"ready"`

          The environment is ready to connect.

        - `"connected"`

          The environment is connected.

        - `"disconnected"`

          The environment is disconnected.

        - `"failed"`

          The environment failed to connect.

      - `type: str`

        The environment type.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.ready"]`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent: …`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: str`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: str`

      The unique ID of the event.

    - `reset_count: int`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The associated turn, when applicable.

    - `type: Literal["agent.session.environment.reset"]`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent: …`

    Emitted when command execution produces an output delta.

    - `delta: str`

      The output text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the command execution item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.output.command_execution_output.delta"]`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent: …`

    Emitted when a session is created.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: str`

        The ID of the session.

      - `agent: Agent`

        The agent running in the session.

        - `id: str`

          The ID of the agent.

        - `instructions: Optional[str]`

          Custom instructions appended to the agent's default base instructions.

        - `model: str`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: bool`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: Optional[int]`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: Optional[str]`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

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

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `"auto"`

          - `"default"`

          - `"flex"`

          - `"priority"`

          - `"fast"`

          - `"ultrafast"`

        - `text: AgentText`

          Configuration for text generated by the agent.

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

        - `tools: List[AgentTool]`

          Tools available to the agent.

          - `class AgentToolResourceFunction: …`

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

          - `class AgentToolResourceProgrammaticToolCalling: …`

            Enables calling tools from model-generated code.

            - `enabled: bool`

              Whether tools can be called from model-generated code.

            - `type: Literal["programmatic_tool_calling"]`

              The type of the object. Always `programmatic_tool_calling`.

              - `"programmatic_tool_calling"`

          - `class AgentToolResourceMcp: …`

            Tools provided by a remote MCP server.

            - `allowed_tools: Optional[List[str]]`

              The MCP tools the agent may call.

            - `connection_origin: Literal["service", "environment"]`

              Where outbound MCP HTTP connections originate.

              - `"service"`

              - `"environment"`

            - `credential_id: Optional[str]`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Dict[str, object]`

              Metadata included with requests to this MCP server.

            - `required: bool`

              Whether this MCP server must initialize before the first turn.

            - `server_label: str`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `class McpTransportResourceHTTP: …`

                Connects to an MCP server over HTTP.

                - `server_url: str`

                  The URL of the MCP server.

                - `type: Literal["http"]`

                  The type of the object. Always `http`.

                  - `"http"`

              - `class McpTransportResourceStdio: …`

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

          - `class AgentToolResourceWebSearch: …`

            Web search.

            - `allowed_domains: Optional[List[str]]`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: Literal["low", "medium", "high"]`

              The amount of search context made available to the model. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

            - `location: Optional[AgentToolResourceWebSearchLocation]`

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

          - `class AgentToolResourceComputerUse: …`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: bool`

              Whether computer tool outputs include screenshots.

            - `type: Literal["computer_use"]`

              The type of the object. Always `computer_use`.

              - `"computer_use"`

      - `created_at: int`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `class EnvironmentResourceNone: …`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: Literal["none"]`

            The type of the object. Always `none`.

            - `"none"`

        - `class EnvironmentResourceOpenAIHosted: …`

          An environment hosted by OpenAI.

          - `id: str`

            The public ID of the environment.

          - `capability_directories: List[str]`

            Directories that contain capabilities exposed to the agent.

          - `desktop: EnvironmentResourceOpenAIHostedDesktop`

            The effective desktop configuration.

            - `enabled: bool`

              Whether the environment provisions a desktop and browser proxy.

          - `files: List[HostedEnvironmentFile]`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileID: …`

              A file copied from the OpenAI Files API.

              - `id: str`

                The session-scoped ID of the file in the execution environment.

              - `file_id: str`

                The ID of the uploaded file.

              - `path: str`

                The file's absolute path inside the environment.

              - `size_bytes: int`

                The decoded file size in bytes.

              - `type: Literal["file_id"]`

                The type of the object. Always `file_id`.

                - `"file_id"`

            - `class HostedEnvironmentFileResourceInline: …`

              A file supplied inline when the session was created.

              - `id: str`

                The session-scoped ID of the file in the execution environment.

              - `path: str`

                The file's absolute path inside the environment.

              - `size_bytes: int`

                The decoded file size in bytes.

              - `type: Literal["inline"]`

                The type of the object. Always `inline`.

                - `"inline"`

          - `network: EnvironmentResourceOpenAIHostedNetwork`

            The effective network access policy for the environment.

            - `access: Literal["enabled", "disabled", "restricted"]`

              The environment's network access mode.

              - `"enabled"`

                Allows unrestricted network access.

              - `"disabled"`

                Disables network access.

              - `"restricted"`

                Applies the configured domain restrictions.

            - `allowed_domains: List[str]`

              Domains the environment may access when network access is restricted.

          - `packages: EnvironmentResourceOpenAIHostedPackages`

            Packages installed in the environment.

            - `npm: List[str]`

              npm packages installed globally in the environment.

            - `python: List[str]`

              Python packages installed in the environment.

            - `system: List[str]`

              System packages installed in the environment.

          - `plugins: List[HostedPlugin]`

            Plugins installed in the environment, excluding their archive contents.

            - `description: str`

              The installed plugin description.

            - `name: str`

              The installed plugin name.

            - `type: Literal["inline"]`

              The type of the object. Always `inline`.

              - `"inline"`

          - `skills: List[HostedSkill]`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference: …`

              A skill installed from the Skills API.

              - `description: str`

                The installed skill description.

              - `name: str`

                The installed skill name.

              - `skill_id: str`

                The referenced skill ID.

              - `type: Literal["skill_reference"]`

                The type of the object. Always `skill_reference`.

                - `"skill_reference"`

              - `version: str`

                The concrete skill version installed for this session.

            - `class HostedSkillResourceInline: …`

              A skill installed from an inline ZIP archive.

              - `description: str`

                The installed skill description.

              - `name: str`

                The installed skill name.

              - `type: Literal["inline"]`

                The type of the object. Always `inline`.

                - `"inline"`

          - `type: Literal["openai_hosted"]`

            The type of the object. Always `openai_hosted`.

            - `"openai_hosted"`

          - `container_size: Optional[Literal["small", "medium", "large"]]`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `"small"`

            - `"medium"`

            - `"large"`

        - `class EnvironmentResourceSelfHosted: …`

          An environment hosted by the application.

          - `id: str`

            The public ID of the environment.

          - `capability_directories: List[str]`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: str`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: Literal["self_hosted"]`

            The type of the object. Always `self_hosted`.

            - `"self_hosted"`

          - `workspace_directory: str`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: Optional[str]`

        The error that caused the session to fail, if any.

      - `last_active_at: int`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Dict[str, str]`

        Custom string key-value pairs attached to the session.

      - `object: Literal["agent.session"]`

        The object type. Always `agent.session`.

        - `"agent.session"`

      - `required_actions: List[RequiredAction]`

        Actions that must be completed before the session can continue.

        - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequest: …`

          Respond to a computer-use request.

          - `request: RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequest`

            The information needed to render the request.

            - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthentication: …`

              A registered form awaiting the application's response.

              - `credential_origin: Optional[str]`

                The registered form or frame origin where values will be entered.

              - `fields: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationField]`

                Controls to render. All submitted values are sensitive.

                - `id: str`

                  The field ID to submit as field_id in a fields entry.

                - `label: str`

                  The label to display beside the control.

                - `required: bool`

                  Whether this control requires a nonempty value.

                - `type: str`

                  The rendering type, such as email, password, or text.

              - `options: List[RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserAuthenticationOption]`

                Sign-in methods. Empty for a plain form.

                - `id: str`

                  The option ID to submit as selected_option.

                - `field_ids: List[str]`

                  IDs from the registered fields that this method accepts.

                - `label: str`

                  The method label to display.

              - `reason: Optional[str]`

                Why the agent needs the user to sign in.

              - `type: Literal["browser_authentication"]`

                The type of the object. Always `browser_authentication`.

                - `"browser_authentication"`

            - `class RequiredActionSessionRequiredActionResourceComputerUseApprovalRequestRequestComputerUseApprovalRequestKindResourceBrowserOriginAccess: …`

              A browser origin awaiting the application's approval decision.

              - `origin: str`

                The origin the browser needs permission to access.

              - `reason: Optional[str]`

                The browser's explanation for this request, or null when unavailable.

              - `type: Literal["browser_origin_access"]`

                The type of the object. Always `browser_origin_access`.

                - `"browser_origin_access"`

          - `request_id: str`

            The registered request ID to echo when responding.

          - `turn_id: str`

            The turn that requested approval.

          - `type: Literal["computer_use_approval_request"]`

            The type of the object. Always `computer_use_approval_request`.

            - `"computer_use_approval_request"`

        - `class RequiredActionSessionRequiredActionResourceFunctionCall: …`

          Run a function tool and submit its result.

          - `arguments: object`

            The arguments supplied by the model.

          - `call_id: str`

            The ID to include when submitting the function result.

          - `name: str`

            The function name.

          - `turn_id: str`

            The ID of the turn that requested the function call.

          - `type: Literal["function_call"]`

            The type of the object. Always `function_call`.

            - `"function_call"`

        - `class RequiredActionSessionRequiredActionResourceEnvironmentConnection: …`

          Reconnect a session environment.

          - `environment_id: str`

            The ID of the environment to reconnect.

          - `type: Literal["environment_connection"]`

            The type of the object. Always `environment_connection`.

            - `"environment_connection"`

      - `status: Literal["idle", "in_progress", "requires_action", "failed"]`

        The current status of the session.

        - `"idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `"in_progress"`

          The session is processing a turn.

        - `"requires_action"`

          The session is waiting for one or more required actions.

        - `"failed"`

          The session failed.

      - `usage: Optional[TokenUsage]`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: int`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails`

          A breakdown of the agent's input token usage.

          - `cached_tokens: int`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: int`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: int`

            The number of output tokens used for reasoning.

        - `total_tokens: int`

          The total number of input and output tokens used by the agent.

      - `vault_ids: List[str]`

        The IDs of vaults made available to the session.

    - `type: Literal["agent.session.created"]`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent: …`

    Emitted when a turn is created.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: str`

        The ID of the turn.

      - `agent_id: str`

        The ID of the agent that ran the turn.

      - `completed_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: int`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: Optional[SessionTurnError]`

        A customer-safe error. Non-null only for a failed turn.

        - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

          A stable, machine-readable failure category.

          - `"context_length_exceeded"`

            The request exceeds the model's context window.

          - `"session_budget_exceeded"`

            The session has reached its usage budget.

          - `"usage_limit_exceeded"`

            The organization has reached a usage, plan, or billing limit.

          - `"credit_balance_exhausted"`

            The organization has no API credits remaining.

          - `"rate_limit_exceeded"`

            The request exceeds the available rate limit.

          - `"flex_unavailable"`

            Flex processing is temporarily unavailable.

          - `"server_overloaded"`

            The model service is temporarily overloaded.

          - `"cyber_policy"`

            The request was rejected by a safety policy.

          - `"misalignment_policy_violation"`

            The request was blocked by the safety systems.

          - `"connection_failed"`

            The request could not connect to the model service.

          - `"server_error"`

            The model service encountered an unexpected error.

          - `"authentication_error"`

            The API credentials are invalid or lack the required access.

          - `"invalid_request"`

            The request contains invalid input or configuration.

          - `"resource_not_found"`

            The requested model or resource is unavailable.

          - `"sandbox_error"`

            The request could not complete in its execution environment.

          - `"executor_version_incompatible"`

            The executor must be upgraded before it can run this turn.

          - `"active_turn_not_steerable"`

            The session cannot accept additional input while a request is running.

          - `"request_timeout"`

            The request timed out before the model service responded.

          - `"internal_error"`

            An unexpected internal error prevented the session request from completing.

        - `message: str`

          A customer-safe explanation of the failure.

      - `object: Literal["agent.session.turn"]`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: str`

        The ID of the session that owns the turn.

      - `started_at: Optional[int]`

        The Unix timestamp, in seconds, when the turn started.

      - `status: Literal["queued", "in_progress", "waiting", 3 more]`

        The current status of the turn.

        - `"queued"`

          The turn is waiting to start.

        - `"in_progress"`

          The turn is in progress.

        - `"waiting"`

          The turn is waiting for external input.

        - `"completed"`

          The turn completed successfully.

        - `"failed"`

          The turn failed.

        - `"cancelled"`

          The turn was cancelled.

      - `subagent_id: Optional[str]`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: Optional[TokenUsage]`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.created"]`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent: …`

    Emitted when a turn starts running.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.in_progress"]`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent: …`

    Emitted when a turn completes.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.completed"]`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent: …`

    Emitted when a turn fails.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.failed"]`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent: …`

    Emitted when a turn is cancelled.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: str`

      The ID of the turn associated with the event.

    - `type: Literal["agent.session.turn.cancelled"]`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: Optional[TokenUsage]`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent: …`

    Emitted when an item is added to a turn.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage: …`

        A user or assistant message recorded in a session.

        - `id: Optional[str]`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: List[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class MessageContentResourceInputText: …`

            Text supplied by the user.

            - `text: str`

              The text supplied by the user.

            - `type: Literal["input_text"]`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `class MessageContentResourceInputImage: …`

            An image supplied by the user.

            - `image_url: str`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: Literal["input_image"]`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `class MessageContentResourceOutputText: …`

            Text produced by the assistant.

            - `text: str`

              The text produced by the assistant.

            - `type: Literal["output_text"]`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["user", "assistant"]`

          The role of the message author.

          - `"user"`

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `"in_progress"`

            The item is in progress.

          - `"completed"`

            The item is complete.

          - `"incomplete"`

            The item stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

        - `id: str`

          The ID of the reasoning item.

        - `status: Optional[AgentOutputItemStatus]`

          The status of the reasoning item.

        - `summary: List[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: str`

            The reasoning summary text.

          - `type: Literal["summary_text"]`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["reasoning"]`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

        - `id: str`

          The ID of the function call item.

        - `arguments: object`

          The arguments to pass to the function.

        - `call_id: str`

          The ID used to submit the function result.

        - `name: str`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `"in_progress"`

            The call is in progress.

          - `"completed"`

            The call completed successfully.

          - `"failed"`

            The call failed.

          - `"incomplete"`

            The call stopped before completing.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call"]`

          The item type. Always `function_call`.

          - `"function_call"`

      - `class FunctionCallOutputItemResource: …`

        The result supplied for a function call.

        - `id: str`

          The ID of the function call output item.

        - `call_id: str`

          The ID of the function call that produced this output.

        - `error: Optional[str]`

          The error message, if the call failed.

        - `output: Optional[AgentFunctionCallOutput]`

          The function result, if the call succeeded.

          - `str`

          - `List[InputContent]`

            - `class InputContentResourceInputText: …`

              Text input recorded in a session item.

              - `text: str`

                The text supplied to the agent.

              - `type: Literal["input_text"]`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `class InputContentResourceInputImage: …`

              Image input recorded in a session item.

              - `image_url: str`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: Literal["input_image"]`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["function_call_output"]`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `class AgentMessageItemResource: …`

        A message exchanged between agent threads.

        - `id: str`

          The ID of the message.

        - `content: List[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText: …`

            A text content part produced by the agent.

            - `text: str`

              The text produced by the agent.

            - `type: Literal["output_text"]`

              The content type. Always `output_text`.

              - `"output_text"`

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

            - `encrypted_content: str`

              The encrypted content payload.

            - `type: Literal["encrypted_content"]`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: str`

          The ID or name of the receiving agent.

        - `sender_agent_id: str`

          The ID or name of the sending agent.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["agent_message"]`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

        - `id: str`

          The ID of the MCP call item.

        - `arguments: object`

          The arguments passed to the MCP tool.

        - `error: object`

          The error returned by the MCP tool, if any.

        - `name: str`

          The name of the MCP tool.

        - `output: object`

          The output returned by the MCP tool, if any.

        - `server_label: str`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["mcp_call"]`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class ComputerUseApprovalRequestResultItemResource: …`

        A credential-free record of an admitted response, not proof of completion.

        - `id: str`

          The stable history item ID.

        - `request_id: str`

          The registered request answered by this item.

        - `response: ComputerUseApprovalRequestResultItemResourceResponse`

          The admitted response, without submitted credential values.

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

            - `action: Literal["submit"]`

              - `"submit"`

            - `selected_option: Optional[str]`

              The chosen sign-in method, or null when no options were offered.

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

          - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

            - `action: Literal["cancel"]`

              - `"cancel"`

            - `type: Literal["browser_authentication"]`

              - `"browser_authentication"`

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_approval_request_result"]`

          - `"computer_use_approval_request_result"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

        - `id: str`

          The ID of the web search call.

        - `action: Optional[WebSearchAction]`

          The action performed by the web search tool.

          - `class WebSearchActionResourceSearch: …`

            A search query or group of search queries.

            - `queries: Optional[List[str]]`

              The search queries, when multiple queries were used.

            - `query: Optional[str]`

              The search query, when a single query was used.

            - `type: Literal["search"]`

              The type of the object. Always `search`.

              - `"search"`

          - `class WebSearchActionResourceOpenPage: …`

            Opens a web page.

            - `type: Literal["open_page"]`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: Optional[str]`

              The URL of the page that was opened.

          - `class WebSearchActionResourceFindInPage: …`

            Finds text within a web page.

            - `pattern: Optional[str]`

              The text pattern that was searched for.

            - `type: Literal["find_in_page"]`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: Optional[str]`

              The URL of the page that was searched.

          - `class WebSearchActionResourceOther: …`

            Another web search action.

            - `type: Literal["other"]`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["web_search_call"]`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

        - `id: str`

          The ID of the command execution item.

        - `command: str`

          The command that was executed.

        - `cwd: Optional[str]`

          The working directory used to execute the command.

        - `duration_ms: Optional[int]`

          The command duration in milliseconds.

        - `exit_code: Optional[int]`

          The process exit code, if the command completed.

        - `output: Optional[str]`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["command_execution"]`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

        - `id: str`

          The ID of the tool call item.

        - `agent_id: str`

          The ID of the agent that requested the subagent.

        - `content: List[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `model: Optional[str]`

          The model requested for the spawned agent.

        - `reasoning_effort: Optional[str]`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["create_subagent_call"]`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

        - `id: str`

          The ID of the tool call item.

        - `content: List[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText: …`

            A text content part produced by the agent.

          - `class EncryptedContentResource: …`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: str`

          The ID of the agent receiving the input.

        - `sender_agent_id: str`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["send_subagent_input_call"]`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to resume.

        - `sender_agent_id: str`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["resume_subagent_call"]`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_ids: List[str]`

          The IDs of the agents to wait for.

        - `sender_agent_id: str`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["wait_for_subagents_call"]`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to interrupt.

        - `sender_agent_id: str`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["interrupt_subagent_call"]`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

        - `id: str`

          The ID of the tool call item.

        - `recipient_agent_id: str`

          The ID of the agent to close.

        - `sender_agent_id: str`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["close_subagent_call"]`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: Optional[int]`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.added"]`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent: …`

    Emitted when a session becomes idle.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: Literal["agent.session.idle"]`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `class AgentSessionInProgressEvent: …`

    Emitted when a session starts processing a turn.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: Literal["agent.session.in_progress"]`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent: …`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: Literal["agent.session.requires_action"]`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `class AgentSessionFailedEvent: …`

    Emitted when a session fails.

    - `event_id: str`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: Literal["agent.session.failed"]`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent: …`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.pending"]`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent: …`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.connected"]`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent: …`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.disconnected"]`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent: …`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: str`

      The unique ID of the event.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.environment.failed"]`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent: …`

    Emitted when a subagent is created.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: str`

        The ID of the subagent.

      - `closed_at: Optional[int]`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Optional[List[AgentContent]]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText: …`

          A text content part produced by the agent.

        - `class EncryptedContentResource: …`

          Encrypted content exchanged between agents.

      - `name: Optional[str]`

        The runner-assigned nickname, or null when unavailable.

      - `object: Literal["agent.session.subagent"]`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: int`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: str`

        The ID of the agent that created this subagent.

      - `session_id: str`

        The ID of the session that owns the subagent.

      - `status: Literal["active", "closed"]`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: Literal["agent.session.subagent.created"]`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent: …`

    Emitted when a closed subagent successfully resumes.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: Literal["agent.session.subagent.active"]`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent: …`

    Emitted when a subagent is closed.

    - `event_id: str`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: Literal["agent.session.subagent.closed"]`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent: …`

    Emitted when an output item is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage: …`

        An assistant message produced by the agent.

        - `id: str`

          The ID of the message.

        - `content: List[OutputText]`

          The content of the message.

          - `text: str`

            The text produced by the agent.

          - `type: Literal["output_text"]`

            The content type. Always `output_text`.

        - `phase: Optional[Literal["commentary", "final_answer"]]`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: Literal["assistant"]`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["message"]`

          The item type. Always `message`.

          - `"message"`

      - `class AgentReasoningItem: …`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem: …`

        A function call produced by the agent.

      - `class AgentMcpCallItem: …`

        A call to a tool on an MCP server.

      - `class ComputerUseCallItemResource: …`

        One execution of the platform-provided computer-use capability.

        - `id: str`

          The ID of the activity item.

        - `output: Optional[ComputerUseCallItemResourceOutput]`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: str`

            The complete JPEG image as a base64 data URL.

          - `type: Literal["computer_screenshot"]`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: Optional[str]`

          A model-generated description of the activity, when available.

        - `turn_id: str`

          The ID of the turn that contains this item.

        - `type: Literal["computer_use_call"]`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `class BrowserAuthenticationRequestItemResource: …`

        A credential-free history record of the emitted login request.

        - `id: str`

          The stable history item ID.

        - `request: BrowserAuthenticationRequestItemResourceRequest`

          A registered form awaiting the application's response.

          - `credential_origin: Optional[str]`

            The registered form or frame origin where values will be entered.

          - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

            Controls to render. All submitted values are sensitive.

            - `id: str`

              The field ID to submit as field_id in a fields entry.

            - `label: str`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: str`

              The rendering type, such as email, password, or text.

          - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

            Sign-in methods. Empty for a plain form.

            - `id: str`

              The option ID to submit as selected_option.

            - `field_ids: List[str]`

              IDs from the registered fields that this method accepts.

            - `label: str`

              The method label to display.

          - `reason: Optional[str]`

            Why the agent needs the user to sign in.

          - `type: Literal["browser_authentication"]`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: str`

        - `turn_id: str`

        - `type: Literal["computer_use_approval_request"]`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `class AgentWebSearchCallItem: …`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem: …`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem: …`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem: …`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem: …`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem: …`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem: …`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem: …`

        A request to close a subagent.

    - `output_index: int`

      The index of the output item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.item.done"]`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent: …`

    Emitted when an output text content part is added.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.added"]`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent: …`

    Emitted when an output content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.content_part.done"]`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent: …`

    Emitted when text is appended to an output text content part.

    - `content_index: int`

      The index of the content part in the message.

    - `delta: str`

      The text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.delta"]`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent: …`

    Emitted when an output text content part is complete.

    - `content_index: int`

      The index of the content part in the message.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the message item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `text: str`

      The complete output text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.output_text.done"]`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent: …`

    Emitted when a reasoning summary content part is added.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.added"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent: …`

    Emitted when a reasoning summary part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: str`

      The ID of the session associated with the event.

    - `status: Optional[Literal["incomplete"]]`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: int`

      The index of the summary part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_part.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent: …`

    Emitted when text is appended to a reasoning summary.

    - `delta: str`

      The summary text that was appended.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.delta"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent: …`

    Emitted when a reasoning summary content part is complete.

    - `event_id: str`

      The unique ID of the event.

    - `item_id: str`

      The ID of the reasoning item.

    - `output_index: int`

      The index of the item in the turn output.

    - `session_id: str`

      The ID of the session associated with the event.

    - `summary_index: int`

      The index of the summary content part.

    - `text: str`

      The complete reasoning summary text.

    - `turn_id: Optional[str]`

      The ID of the turn associated with the event, when applicable.

    - `type: Literal["agent.session.turn.reasoning_summary_text.done"]`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
for event in client.beta.agents.sessions.events.stream(
    "session_id",
):
  print(event)
```

# Items

## List agent session items

`beta.agents.sessions.items.list(strsession_id, ItemListParams**kwargs)  -> SyncCursorPage[AgentSessionItem]`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `session_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `AgentSessionItem`

  An item associated with a session turn.

  - `class AgentSessionMessage: …`

    A user or assistant message recorded in a session.

    - `id: Optional[str]`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: List[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class MessageContentResourceInputText: …`

        Text supplied by the user.

        - `text: str`

          The text supplied by the user.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class MessageContentResourceInputImage: …`

        An image supplied by the user.

        - `image_url: str`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `class MessageContentResourceOutputText: …`

        Text produced by the assistant.

        - `text: str`

          The text produced by the assistant.

        - `type: Literal["output_text"]`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["user", "assistant"]`

      The role of the message author.

      - `"user"`

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class FunctionCallOutputItemResource: …`

    The result supplied for a function call.

    - `id: str`

      The ID of the function call output item.

    - `call_id: str`

      The ID of the function call that produced this output.

    - `error: Optional[str]`

      The error message, if the call failed.

    - `output: Optional[AgentFunctionCallOutput]`

      The function result, if the call succeeded.

      - `str`

      - `List[InputContent]`

        - `class InputContentResourceInputText: …`

          Text input recorded in a session item.

          - `text: str`

            The text supplied to the agent.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentResourceInputImage: …`

          Image input recorded in a session item.

          - `image_url: str`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call_output"]`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `class AgentMessageItemResource: …`

    A message exchanged between agent threads.

    - `id: str`

      The ID of the message.

    - `content: List[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: str`

      The ID or name of the receiving agent.

    - `sender_agent_id: str`

      The ID or name of the sending agent.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["agent_message"]`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class ComputerUseApprovalRequestResultItemResource: …`

    A credential-free record of an admitted response, not proof of completion.

    - `id: str`

      The stable history item ID.

    - `request_id: str`

      The registered request answered by this item.

    - `response: ComputerUseApprovalRequestResultItemResourceResponse`

      The admitted response, without submitted credential values.

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `selected_option: Optional[str]`

          The chosen sign-in method, or null when no options were offered.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_approval_request_result"]`

      - `"computer_use_approval_request_result"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.items.list(
    session_id="session_id",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Subagents

## List session subagents

`beta.agents.sessions.subagents.list(strsession_id, SubagentListParams**kwargs)  -> SyncCursorPage[Subagent]`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class Subagent: …`

  A subagent created within a session.

  - `id: str`

    The ID of the subagent.

  - `closed_at: Optional[int]`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Optional[List[AgentContent]]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: Optional[str]`

    The runner-assigned nickname, or null when unavailable.

  - `object: Literal["agent.session.subagent"]`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: int`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: str`

    The ID of the agent that created this subagent.

  - `session_id: str`

    The ID of the session that owns the subagent.

  - `status: Literal["active", "closed"]`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.subagents.list(
    session_id="session_id",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "closed_at": 0,
      "instructions": [
        {
          "text": "text",
          "type": "output_text"
        }
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a session subagent

`beta.agents.sessions.subagents.retrieve(strsubagent_id, SubagentRetrieveParams**kwargs)  -> Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `subagent_id: str`

### Returns

- `class Subagent: …`

  A subagent created within a session.

  - `id: str`

    The ID of the subagent.

  - `closed_at: Optional[int]`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Optional[List[AgentContent]]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText: …`

      A text content part produced by the agent.

      - `text: str`

        The text produced by the agent.

      - `type: Literal["output_text"]`

        The content type. Always `output_text`.

        - `"output_text"`

    - `class EncryptedContentResource: …`

      Encrypted content exchanged between agents.

      - `encrypted_content: str`

        The encrypted content payload.

      - `type: Literal["encrypted_content"]`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: Optional[str]`

    The runner-assigned nickname, or null when unavailable.

  - `object: Literal["agent.session.subagent"]`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: int`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: str`

    The ID of the agent that created this subagent.

  - `session_id: str`

    The ID of the session that owns the subagent.

  - `status: Literal["active", "closed"]`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
subagent = client.beta.agents.sessions.subagents.retrieve(
    subagent_id="subagent_id",
    session_id="session_id",
)
print(subagent.id)
```

#### Response

```json
{
  "id": "id",
  "closed_at": 0,
  "instructions": [
    {
      "text": "text",
      "type": "output_text"
    }
  ],
  "name": "name",
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"
}
```

# Items

## List subagent items

`beta.agents.sessions.subagents.items.list(strsubagent_id, ItemListParams**kwargs)  -> SyncCursorPage[AgentSessionItem]`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `subagent_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `AgentSessionItem`

  An item associated with a session turn.

  - `class AgentSessionMessage: …`

    A user or assistant message recorded in a session.

    - `id: Optional[str]`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: List[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class MessageContentResourceInputText: …`

        Text supplied by the user.

        - `text: str`

          The text supplied by the user.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class MessageContentResourceInputImage: …`

        An image supplied by the user.

        - `image_url: str`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `class MessageContentResourceOutputText: …`

        Text produced by the assistant.

        - `text: str`

          The text produced by the assistant.

        - `type: Literal["output_text"]`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["user", "assistant"]`

      The role of the message author.

      - `"user"`

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class FunctionCallOutputItemResource: …`

    The result supplied for a function call.

    - `id: str`

      The ID of the function call output item.

    - `call_id: str`

      The ID of the function call that produced this output.

    - `error: Optional[str]`

      The error message, if the call failed.

    - `output: Optional[AgentFunctionCallOutput]`

      The function result, if the call succeeded.

      - `str`

      - `List[InputContent]`

        - `class InputContentResourceInputText: …`

          Text input recorded in a session item.

          - `text: str`

            The text supplied to the agent.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentResourceInputImage: …`

          Image input recorded in a session item.

          - `image_url: str`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call_output"]`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `class AgentMessageItemResource: …`

    A message exchanged between agent threads.

    - `id: str`

      The ID of the message.

    - `content: List[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: str`

      The ID or name of the receiving agent.

    - `sender_agent_id: str`

      The ID or name of the sending agent.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["agent_message"]`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class ComputerUseApprovalRequestResultItemResource: …`

    A credential-free record of an admitted response, not proof of completion.

    - `id: str`

      The stable history item ID.

    - `request_id: str`

      The registered request answered by this item.

    - `response: ComputerUseApprovalRequestResultItemResourceResponse`

      The admitted response, without submitted credential values.

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `selected_option: Optional[str]`

          The chosen sign-in method, or null when no options were offered.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_approval_request_result"]`

      - `"computer_use_approval_request_result"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.subagents.items.list(
    subagent_id="subagent_id",
    session_id="session_id",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List subagent turns

`beta.agents.sessions.subagents.turns.list(strsubagent_id, TurnListParams**kwargs)  -> SyncCursorPage[Turn]`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `subagent_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class Turn: …`

  The canonical public representation of a session turn.

  - `id: str`

    The ID of the turn.

  - `agent_id: str`

    The ID of the agent that ran the turn.

  - `completed_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: int`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: Optional[SessionTurnError]`

    A customer-safe error. Non-null only for a failed turn.

    - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

      A stable, machine-readable failure category.

      - `"context_length_exceeded"`

        The request exceeds the model's context window.

      - `"session_budget_exceeded"`

        The session has reached its usage budget.

      - `"usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `"credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `"rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `"flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `"server_overloaded"`

        The model service is temporarily overloaded.

      - `"cyber_policy"`

        The request was rejected by a safety policy.

      - `"misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `"connection_failed"`

        The request could not connect to the model service.

      - `"server_error"`

        The model service encountered an unexpected error.

      - `"authentication_error"`

        The API credentials are invalid or lack the required access.

      - `"invalid_request"`

        The request contains invalid input or configuration.

      - `"resource_not_found"`

        The requested model or resource is unavailable.

      - `"sandbox_error"`

        The request could not complete in its execution environment.

      - `"executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `"active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `"request_timeout"`

        The request timed out before the model service responded.

      - `"internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `message: str`

      A customer-safe explanation of the failure.

  - `object: Literal["agent.session.turn"]`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: str`

    The ID of the session that owns the turn.

  - `started_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn started.

  - `status: Literal["queued", "in_progress", "waiting", 3 more]`

    The current status of the turn.

    - `"queued"`

      The turn is waiting to start.

    - `"in_progress"`

      The turn is in progress.

    - `"waiting"`

      The turn is waiting for external input.

    - `"completed"`

      The turn completed successfully.

    - `"failed"`

      The turn failed.

    - `"cancelled"`

      The turn was cancelled.

  - `subagent_id: Optional[str]`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.subagents.turns.list(
    subagent_id="subagent_id",
    session_id="session_id",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a subagent turn

`beta.agents.sessions.subagents.turns.retrieve(strturn_id, TurnRetrieveParams**kwargs)  -> Turn`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `subagent_id: str`

- `turn_id: str`

### Returns

- `class Turn: …`

  The canonical public representation of a session turn.

  - `id: str`

    The ID of the turn.

  - `agent_id: str`

    The ID of the agent that ran the turn.

  - `completed_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: int`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: Optional[SessionTurnError]`

    A customer-safe error. Non-null only for a failed turn.

    - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

      A stable, machine-readable failure category.

      - `"context_length_exceeded"`

        The request exceeds the model's context window.

      - `"session_budget_exceeded"`

        The session has reached its usage budget.

      - `"usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `"credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `"rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `"flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `"server_overloaded"`

        The model service is temporarily overloaded.

      - `"cyber_policy"`

        The request was rejected by a safety policy.

      - `"misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `"connection_failed"`

        The request could not connect to the model service.

      - `"server_error"`

        The model service encountered an unexpected error.

      - `"authentication_error"`

        The API credentials are invalid or lack the required access.

      - `"invalid_request"`

        The request contains invalid input or configuration.

      - `"resource_not_found"`

        The requested model or resource is unavailable.

      - `"sandbox_error"`

        The request could not complete in its execution environment.

      - `"executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `"active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `"request_timeout"`

        The request timed out before the model service responded.

      - `"internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `message: str`

      A customer-safe explanation of the failure.

  - `object: Literal["agent.session.turn"]`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: str`

    The ID of the session that owns the turn.

  - `started_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn started.

  - `status: Literal["queued", "in_progress", "waiting", 3 more]`

    The current status of the turn.

    - `"queued"`

      The turn is waiting to start.

    - `"in_progress"`

      The turn is in progress.

    - `"waiting"`

      The turn is waiting for external input.

    - `"completed"`

      The turn completed successfully.

    - `"failed"`

      The turn failed.

    - `"cancelled"`

      The turn was cancelled.

  - `subagent_id: Optional[str]`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
turn = client.beta.agents.sessions.subagents.turns.retrieve(
    turn_id="turn_id",
    session_id="session_id",
    subagent_id="subagent_id",
)
print(turn.id)
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

# Items

## List subagent turn items

`beta.agents.sessions.subagents.turns.items.list(strturn_id, ItemListParams**kwargs)  -> SyncCursorPage[AgentSessionItem]`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: str`

- `subagent_id: str`

- `turn_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `AgentSessionItem`

  An item associated with a session turn.

  - `class AgentSessionMessage: …`

    A user or assistant message recorded in a session.

    - `id: Optional[str]`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: List[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class MessageContentResourceInputText: …`

        Text supplied by the user.

        - `text: str`

          The text supplied by the user.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class MessageContentResourceInputImage: …`

        An image supplied by the user.

        - `image_url: str`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `class MessageContentResourceOutputText: …`

        Text produced by the assistant.

        - `text: str`

          The text produced by the assistant.

        - `type: Literal["output_text"]`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["user", "assistant"]`

      The role of the message author.

      - `"user"`

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class FunctionCallOutputItemResource: …`

    The result supplied for a function call.

    - `id: str`

      The ID of the function call output item.

    - `call_id: str`

      The ID of the function call that produced this output.

    - `error: Optional[str]`

      The error message, if the call failed.

    - `output: Optional[AgentFunctionCallOutput]`

      The function result, if the call succeeded.

      - `str`

      - `List[InputContent]`

        - `class InputContentResourceInputText: …`

          Text input recorded in a session item.

          - `text: str`

            The text supplied to the agent.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentResourceInputImage: …`

          Image input recorded in a session item.

          - `image_url: str`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call_output"]`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `class AgentMessageItemResource: …`

    A message exchanged between agent threads.

    - `id: str`

      The ID of the message.

    - `content: List[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: str`

      The ID or name of the receiving agent.

    - `sender_agent_id: str`

      The ID or name of the sending agent.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["agent_message"]`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class ComputerUseApprovalRequestResultItemResource: …`

    A credential-free record of an admitted response, not proof of completion.

    - `id: str`

      The stable history item ID.

    - `request_id: str`

      The registered request answered by this item.

    - `response: ComputerUseApprovalRequestResultItemResourceResponse`

      The admitted response, without submitted credential values.

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `selected_option: Optional[str]`

          The chosen sign-in method, or null when no options were offered.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_approval_request_result"]`

      - `"computer_use_approval_request_result"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.subagents.turns.items.list(
    turn_id="turn_id",
    session_id="session_id",
    subagent_id="subagent_id",
)
page = page.data[0]
print(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "type": "input_text"
        }
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

# Turns

## List agent session turns

`beta.agents.sessions.turns.list(strsession_id, TurnListParams**kwargs)  -> SyncCursorPage[Turn]`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

### Returns

- `class Turn: …`

  The canonical public representation of a session turn.

  - `id: str`

    The ID of the turn.

  - `agent_id: str`

    The ID of the agent that ran the turn.

  - `completed_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: int`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: Optional[SessionTurnError]`

    A customer-safe error. Non-null only for a failed turn.

    - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

      A stable, machine-readable failure category.

      - `"context_length_exceeded"`

        The request exceeds the model's context window.

      - `"session_budget_exceeded"`

        The session has reached its usage budget.

      - `"usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `"credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `"rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `"flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `"server_overloaded"`

        The model service is temporarily overloaded.

      - `"cyber_policy"`

        The request was rejected by a safety policy.

      - `"misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `"connection_failed"`

        The request could not connect to the model service.

      - `"server_error"`

        The model service encountered an unexpected error.

      - `"authentication_error"`

        The API credentials are invalid or lack the required access.

      - `"invalid_request"`

        The request contains invalid input or configuration.

      - `"resource_not_found"`

        The requested model or resource is unavailable.

      - `"sandbox_error"`

        The request could not complete in its execution environment.

      - `"executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `"active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `"request_timeout"`

        The request timed out before the model service responded.

      - `"internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `message: str`

      A customer-safe explanation of the failure.

  - `object: Literal["agent.session.turn"]`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: str`

    The ID of the session that owns the turn.

  - `started_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn started.

  - `status: Literal["queued", "in_progress", "waiting", 3 more]`

    The current status of the turn.

    - `"queued"`

      The turn is waiting to start.

    - `"in_progress"`

      The turn is in progress.

    - `"waiting"`

      The turn is waiting for external input.

    - `"completed"`

      The turn completed successfully.

    - `"failed"`

      The turn failed.

    - `"cancelled"`

      The turn was cancelled.

  - `subagent_id: Optional[str]`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
page = client.beta.agents.sessions.turns.list(
    session_id="session_id",
)
page = page.data[0]
print(page.id)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "agent_id": "agent_id",
      "completed_at": 0,
      "created_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      },
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        },
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        },
        "total_tokens": 0
      }
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve an agent session turn

`beta.agents.sessions.turns.retrieve(strturn_id, TurnRetrieveParams**kwargs)  -> Turn`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: str`

- `turn_id: str`

### Returns

- `class Turn: …`

  The canonical public representation of a session turn.

  - `id: str`

    The ID of the turn.

  - `agent_id: str`

    The ID of the agent that ran the turn.

  - `completed_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: int`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: Optional[SessionTurnError]`

    A customer-safe error. Non-null only for a failed turn.

    - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

      A stable, machine-readable failure category.

      - `"context_length_exceeded"`

        The request exceeds the model's context window.

      - `"session_budget_exceeded"`

        The session has reached its usage budget.

      - `"usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `"credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `"rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `"flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `"server_overloaded"`

        The model service is temporarily overloaded.

      - `"cyber_policy"`

        The request was rejected by a safety policy.

      - `"misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `"connection_failed"`

        The request could not connect to the model service.

      - `"server_error"`

        The model service encountered an unexpected error.

      - `"authentication_error"`

        The API credentials are invalid or lack the required access.

      - `"invalid_request"`

        The request contains invalid input or configuration.

      - `"resource_not_found"`

        The requested model or resource is unavailable.

      - `"sandbox_error"`

        The request could not complete in its execution environment.

      - `"executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `"active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `"request_timeout"`

        The request timed out before the model service responded.

      - `"internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `message: str`

      A customer-safe explanation of the failure.

  - `object: Literal["agent.session.turn"]`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: str`

    The ID of the session that owns the turn.

  - `started_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn started.

  - `status: Literal["queued", "in_progress", "waiting", 3 more]`

    The current status of the turn.

    - `"queued"`

      The turn is waiting to start.

    - `"in_progress"`

      The turn is in progress.

    - `"waiting"`

      The turn is waiting for external input.

    - `"completed"`

      The turn completed successfully.

    - `"failed"`

      The turn failed.

    - `"cancelled"`

      The turn was cancelled.

  - `subagent_id: Optional[str]`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
turn = client.beta.agents.sessions.turns.retrieve(
    turn_id="turn_id",
    session_id="session_id",
)
print(turn.id)
```

#### Response

```json
{
  "id": "id",
  "agent_id": "agent_id",
  "completed_at": 0,
  "created_at": 0,
  "error": {
    "code": "context_length_exceeded",
    "message": "message"
  },
  "object": "agent.session.turn",
  "session_id": "session_id",
  "started_at": 0,
  "status": "queued",
  "subagent_id": "subagent_id",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  }
}
```

## Domain Types

### Turn

- `class Turn: …`

  The canonical public representation of a session turn.

  - `id: str`

    The ID of the turn.

  - `agent_id: str`

    The ID of the agent that ran the turn.

  - `completed_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: int`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: Optional[SessionTurnError]`

    A customer-safe error. Non-null only for a failed turn.

    - `code: Literal["context_length_exceeded", "session_budget_exceeded", "usage_limit_exceeded", 16 more]`

      A stable, machine-readable failure category.

      - `"context_length_exceeded"`

        The request exceeds the model's context window.

      - `"session_budget_exceeded"`

        The session has reached its usage budget.

      - `"usage_limit_exceeded"`

        The organization has reached a usage, plan, or billing limit.

      - `"credit_balance_exhausted"`

        The organization has no API credits remaining.

      - `"rate_limit_exceeded"`

        The request exceeds the available rate limit.

      - `"flex_unavailable"`

        Flex processing is temporarily unavailable.

      - `"server_overloaded"`

        The model service is temporarily overloaded.

      - `"cyber_policy"`

        The request was rejected by a safety policy.

      - `"misalignment_policy_violation"`

        The request was blocked by the safety systems.

      - `"connection_failed"`

        The request could not connect to the model service.

      - `"server_error"`

        The model service encountered an unexpected error.

      - `"authentication_error"`

        The API credentials are invalid or lack the required access.

      - `"invalid_request"`

        The request contains invalid input or configuration.

      - `"resource_not_found"`

        The requested model or resource is unavailable.

      - `"sandbox_error"`

        The request could not complete in its execution environment.

      - `"executor_version_incompatible"`

        The executor must be upgraded before it can run this turn.

      - `"active_turn_not_steerable"`

        The session cannot accept additional input while a request is running.

      - `"request_timeout"`

        The request timed out before the model service responded.

      - `"internal_error"`

        An unexpected internal error prevented the session request from completing.

    - `message: str`

      A customer-safe explanation of the failure.

  - `object: Literal["agent.session.turn"]`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: str`

    The ID of the session that owns the turn.

  - `started_at: Optional[int]`

    The Unix timestamp, in seconds, when the turn started.

  - `status: Literal["queued", "in_progress", "waiting", 3 more]`

    The current status of the turn.

    - `"queued"`

      The turn is waiting to start.

    - `"in_progress"`

      The turn is in progress.

    - `"waiting"`

      The turn is waiting for external input.

    - `"completed"`

      The turn completed successfully.

    - `"failed"`

      The turn failed.

    - `"cancelled"`

      The turn was cancelled.

  - `subagent_id: Optional[str]`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: Optional[TokenUsage]`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: int`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: int`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: int`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: int`

        The number of output tokens used for reasoning.

    - `total_tokens: int`

      The total number of input and output tokens used by the agent.

# Vaults

## Create a vault

`beta.agents.vaults.create(VaultCreateParams**kwargs)  -> Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `metadata: Optional[Dict[str, str]]`

  Key-value pairs to associate with the vault, such as an application or team identifier.

- `name: Optional[str]`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `class Vault: …`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: str`

    The ID of the vault.

  - `created_at: int`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Dict[str, str]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: Optional[str]`

    The human-readable name of the vault, if set.

  - `object: Literal["vault"]`

    The object type. Always `vault`.

    - `"vault"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
vault = client.beta.agents.vaults.create()
print(vault.id)
```

#### Response

```json
{
  "id": "id",
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault"
}
```

## Delete a vault

`beta.agents.vaults.delete(strvault_id)  -> VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: str`

### Returns

- `class VaultDeleted: …`

  Confirmation that a vault was deleted.

  - `id: str`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: Literal["vault.deleted"]`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Example

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)
vault_deleted = client.beta.agents.vaults.delete(
    "vault_id",
)
print(vault_deleted.id)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.deleted"
}
```

## List vaults

`beta.agents.vaults.list(VaultListParams**kwargs)  -> SyncCursorPage[Vault]`

**get** `/vaults`
