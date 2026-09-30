<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

# Agents

## Create an agent

`beta.agents.create(**kwargs) -> Agent`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `model: String`

  The model to use for the agent. The requested model name is preserved.

- `instructions: String`

  Additional instructions appended to the agent's default base instructions. Omit or set to null to add no custom instructions.

- `metadata: Hash[Symbol, String]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `multi_agent: MultiAgentConfigParam`

  Configuration for creating and coordinating subagents. Subagent tools are disabled by default.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Integer`

    Maximum number of subagents that may run concurrently. Defaults to 6.

- `name: String`

  A human-readable name for the agent. Omission or null leaves the agent unnamed.

- `reasoning: AgentReasoningParam`

  Configuration for model reasoning. Omission uses the model's default effort.

  - `effort: :none | :minimal | :low | 4 more`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `:none`

    - `:minimal`

    - `:low`

    - `:medium`

    - `:high`

    - `:xhigh`

    - `:max`

  - `summary: :concise | :detailed | :auto`

    Controls whether the response includes a reasoning summary.

    - `:concise`

      Returns a concise reasoning summary when supported.

    - `:detailed`

      Returns a detailed reasoning summary when supported.

    - `:auto`

      Automatically selects the most detailed summary supported by the model.

- `service_tier: :auto | :default | :flex | 3 more`

  The service tier used for model requests. Defaults to `auto`.

  - `:auto`

    Selects the service tier automatically.

  - `:default`

    Uses the default service tier.

  - `:flex`

    Uses the flex service tier.

  - `:priority`

    Uses the priority service tier.

  - `:fast`

    Uses the fast service tier.

  - `:ultrafast`

    Uses the ultrafast service tier.

- `text: AgentTextParam`

  Configuration for generated text. Defaults to the `text` format and medium verbosity.

  - `format_: TextFormatParam`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `class Text`

      Generates ordinary text without a structured-output constraint.

      - `type: :text`

        The type of the object. Always `text`.

        - `:text`

    - `class JSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Hash[Symbol, untyped]`

        The JSON Schema that generated text must match.

      - `type: :json_schema`

        The type of the object. Always `json_schema`.

        - `:json_schema`

  - `verbosity: :low | :medium | :high`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `:low`

      Produces less text.

    - `:medium`

      Uses the default amount of text.

    - `:high`

      Produces more text.

- `tools: Array[PersistedAgentToolParam]`

  Tools available to the agent. Defaults to an empty list.

  - `class Function`

    A function defined by the application.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

    - `defer_loading: bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `class ToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: :tool_search`

      The type of the object. Always `tool_search`.

      - `:tool_search`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

    - `enabled: bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class Mcp`

    Tools provided by a remote MCP server without stored credentials.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransportParam`

      The credential-free transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

        - `headers: Hash[Symbol, String]`

          Non-secret HTTP headers sent to the MCP server.

      - `class Stdio`

        Starts an MCP server as a local process.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `env_vars: Array[String]`

          Environment variable names to inherit from the selected execution environment.

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: :service | :environment`

      Selects where outbound MCP HTTP connections originate.

      - `:service`

        Uses the Managed Agents service network.

      - `:environment`

        Uses the session's execution environment.

    - `credential_id: String`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class WebSearch`

    Web search.

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

    - `allowed_domains: Array[String]`

      Domains the search may include.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results. Defaults to `live`.

      - `:disabled`

        Disables web search.

      - `:cached`

        Uses cached search results.

      - `:live`

        Searches the live web.

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `class Agent`

  A reusable agent scoped to the caller's project.

  - `id: String`

    The ID of the reusable agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: String`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the agent.

  - `model: String`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: String`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: :agent`

    The object type. Always `agent`.

    - `:agent`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: :none | :minimal | :low | 4 more`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The resolved service-tier policy used for model requests.

    - `:auto`

    - `:default`

    - `:flex`

    - `:priority`

    - `:fast`

    - `:ultrafast`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format_: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text produced by the agent. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

  - `tools: Array[PersistedAgentTool]`

    Tools available to the agent.

    - `class Function`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

    - `class Mcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: :service | :environment`

        Where outbound MCP HTTP connections originate.

        - `:service`

        - `:environment`

      - `credential_id: String`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `headers: Hash[Symbol, String]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

        - `class Stdio`

          Starts an MCP server as a local process.

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `env_vars: Array[String]`

            Environment variable names inherited from the execution environment.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

    - `class WebSearch`

      Web search.

      - `allowed_domains: Array[String]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results, if provided.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results.

        - `:disabled`

        - `:cached`

        - `:live`

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent = openai.beta.agents.create(model: "model")

puts(agent)
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

`beta.agents.delete(agent_id) -> AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: String`

### Returns

- `class AgentDeleted`

  A deleted reusable agent.

  - `id: String`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: :"agent.deleted"`

    The object type. Always `agent.deleted`.

    - `:"agent.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_deleted = openai.beta.agents.delete("agent_id")

puts(agent_deleted)
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

`beta.agents.list(**kwargs) -> CursorPage<Agent>`

**get** `/agents`

Lists reusable agents in the current project. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Agent`

  A reusable agent scoped to the caller's project.

  - `id: String`

    The ID of the reusable agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: String`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the agent.

  - `model: String`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: String`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: :agent`

    The object type. Always `agent`.

    - `:agent`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: :none | :minimal | :low | 4 more`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The resolved service-tier policy used for model requests.

    - `:auto`

    - `:default`

    - `:flex`

    - `:priority`

    - `:fast`

    - `:ultrafast`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format_: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text produced by the agent. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

  - `tools: Array[PersistedAgentTool]`

    Tools available to the agent.

    - `class Function`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

    - `class Mcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: :service | :environment`

        Where outbound MCP HTTP connections originate.

        - `:service`

        - `:environment`

      - `credential_id: String`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `headers: Hash[Symbol, String]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

        - `class Stdio`

          Starts an MCP server as a local process.

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `env_vars: Array[String]`

            Environment variable names inherited from the execution environment.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

    - `class WebSearch`

      Web search.

      - `allowed_domains: Array[String]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results, if provided.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results.

        - `:disabled`

        - `:cached`

        - `:live`

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.list

puts(page)
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

`beta.agents.retrieve(agent_id) -> Agent`

**get** `/agents/{agent_id}`

Retrieves a reusable agent by ID. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: String`

### Returns

- `class Agent`

  A reusable agent scoped to the caller's project.

  - `id: String`

    The ID of the reusable agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: String`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the agent.

  - `model: String`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: String`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: :agent`

    The object type. Always `agent`.

    - `:agent`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: :none | :minimal | :low | 4 more`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The resolved service-tier policy used for model requests.

    - `:auto`

    - `:default`

    - `:flex`

    - `:priority`

    - `:fast`

    - `:ultrafast`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format_: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text produced by the agent. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

  - `tools: Array[PersistedAgentTool]`

    Tools available to the agent.

    - `class Function`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

    - `class Mcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: :service | :environment`

        Where outbound MCP HTTP connections originate.

        - `:service`

        - `:environment`

      - `credential_id: String`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `headers: Hash[Symbol, String]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

        - `class Stdio`

          Starts an MCP server as a local process.

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `env_vars: Array[String]`

            Environment variable names inherited from the execution environment.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

    - `class WebSearch`

      Web search.

      - `allowed_domains: Array[String]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results, if provided.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results.

        - `:disabled`

        - `:cached`

        - `:live`

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent = openai.beta.agents.retrieve("agent_id")

puts(agent)
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

`beta.agents.update(agent_id, **kwargs) -> Agent`

**post** `/agents/{agent_id}`

Updates a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agent_id: String`

- `instructions: String`

  Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

- `model: String`

  The model to use for the agent. The requested model name is preserved.

- `multi_agent: MultiAgentConfigParam`

  Configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Integer`

    Maximum number of subagents that may run concurrently. Defaults to 6.

- `name: String`

  A replacement name. Omit to leave unchanged, or pass null to clear it.

- `reasoning: AgentReasoningParam`

  Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

  - `effort: :none | :minimal | :low | 4 more`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `:none`

    - `:minimal`

    - `:low`

    - `:medium`

    - `:high`

    - `:xhigh`

    - `:max`

  - `summary: :concise | :detailed | :auto`

    Controls whether the response includes a reasoning summary.

    - `:concise`

      Returns a concise reasoning summary when supported.

    - `:detailed`

      Returns a detailed reasoning summary when supported.

    - `:auto`

      Automatically selects the most detailed summary supported by the model.

- `service_tier: :auto | :default | :flex | 3 more`

  The service tier used for model requests.

  - `:auto`

    Selects the service tier automatically.

  - `:default`

    Uses the default service tier.

  - `:flex`

    Uses the flex service tier.

  - `:priority`

    Uses the priority service tier.

  - `:fast`

    Uses the fast service tier.

  - `:ultrafast`

    Uses the ultrafast service tier.

- `text: AgentTextParam`

  Configuration for text generated by the agent.

  - `format_: TextFormatParam`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `class Text`

      Generates ordinary text without a structured-output constraint.

      - `type: :text`

        The type of the object. Always `text`.

        - `:text`

    - `class JSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Hash[Symbol, untyped]`

        The JSON Schema that generated text must match.

      - `type: :json_schema`

        The type of the object. Always `json_schema`.

        - `:json_schema`

  - `verbosity: :low | :medium | :high`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `:low`

      Produces less text.

    - `:medium`

      Uses the default amount of text.

    - `:high`

      Produces more text.

- `tools: Array[PersistedAgentToolParam]`

  Tools available to the agent.

  - `class Function`

    A function defined by the application.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

    - `defer_loading: bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `class ToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: :tool_search`

      The type of the object. Always `tool_search`.

      - `:tool_search`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

    - `enabled: bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class Mcp`

    Tools provided by a remote MCP server without stored credentials.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransportParam`

      The credential-free transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

        - `headers: Hash[Symbol, String]`

          Non-secret HTTP headers sent to the MCP server.

      - `class Stdio`

        Starts an MCP server as a local process.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `env_vars: Array[String]`

          Environment variable names to inherit from the selected execution environment.

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: :service | :environment`

      Selects where outbound MCP HTTP connections originate.

      - `:service`

        Uses the Managed Agents service network.

      - `:environment`

        Uses the session's execution environment.

    - `credential_id: String`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class WebSearch`

    Web search.

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

    - `allowed_domains: Array[String]`

      Domains the search may include.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results. Defaults to `live`.

      - `:disabled`

        Disables web search.

      - `:cached`

        Uses cached search results.

      - `:live`

        Searches the live web.

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `class Agent`

  A reusable agent scoped to the caller's project.

  - `id: String`

    The ID of the reusable agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: String`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the agent.

  - `model: String`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: String`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: :agent`

    The object type. Always `agent`.

    - `:agent`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: :none | :minimal | :low | 4 more`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The resolved service-tier policy used for model requests.

    - `:auto`

    - `:default`

    - `:flex`

    - `:priority`

    - `:fast`

    - `:ultrafast`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format_: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text produced by the agent. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

  - `tools: Array[PersistedAgentTool]`

    Tools available to the agent.

    - `class Function`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

    - `class Mcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: :service | :environment`

        Where outbound MCP HTTP connections originate.

        - `:service`

        - `:environment`

      - `credential_id: String`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `headers: Hash[Symbol, String]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

        - `class Stdio`

          Starts an MCP server as a local process.

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `env_vars: Array[String]`

            Environment variable names inherited from the execution environment.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

    - `class WebSearch`

      Web search.

      - `allowed_domains: Array[String]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results, if provided.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results.

        - `:disabled`

        - `:cached`

        - `:live`

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent = openai.beta.agents.update("agent_id")

puts(agent)
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

- `class Agent`

  A reusable agent scoped to the caller's project.

  - `id: String`

    The ID of the reusable agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: String`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the agent.

  - `model: String`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: String`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: :agent`

    The object type. Always `agent`.

    - `:agent`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: :none | :minimal | :low | 4 more`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The resolved service-tier policy used for model requests.

    - `:auto`

    - `:default`

    - `:flex`

    - `:priority`

    - `:fast`

    - `:ultrafast`

  - `text: AgentText`

    The resolved configuration for text generated by the agent.

    - `format_: TextFormat`

      The effective output format. Defaults to ordinary text.

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text produced by the agent. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

  - `tools: Array[PersistedAgentTool]`

    Tools available to the agent.

    - `class Function`

      A function defined by the application.

      - `defer_loading: bool`

        Whether the function is deferred and discovered through tool search.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: bool`

        Whether tools can be called from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

    - `class Mcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: :service | :environment`

        Where outbound MCP HTTP connections originate.

        - `:service`

        - `:environment`

      - `credential_id: String`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `headers: Hash[Symbol, String]`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

        - `class Stdio`

          Starts an MCP server as a local process.

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `env_vars: Array[String]`

            Environment variable names inherited from the execution environment.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

    - `class WebSearch`

      Web search.

      - `allowed_domains: Array[String]`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results, if provided.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results.

        - `:disabled`

        - `:cached`

        - `:live`

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the agent was last updated.

### Agent Browser Authentication Cancel Param

- `class AgentBrowserAuthenticationCancelParam`

  - `action: :cancel`

    - `:cancel`

  - `type: :browser_authentication`

    - `:browser_authentication`

### Agent Browser Authentication Submit Param

- `class AgentBrowserAuthenticationSubmitParam`

  - `action: :submit`

    - `:submit`

  - `fields: Array[Field{ field_id, value}]`

    Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

    - `field_id: String`

      The field ID from the required action.

    - `value: String`

      The value to enter into the registered control.

  - `type: :browser_authentication`

    - `:browser_authentication`

  - `selected_option: String`

    The chosen method. Required when the required action contains options.

### Agent Browser Origin Access Param

- `class AgentBrowserOriginAccessParam`

  - `decision: :approve | :deny | :cancel`

    Whether to allow, deny, or cancel the requested origin access.

    - `:approve`

      Allow the browser to access this origin.

    - `:deny`

      Deny access to this origin.

    - `:cancel`

      Dismiss this request without approving access.

  - `type: :browser_origin_access`

    - `:browser_origin_access`

### Agent Close Subagent Call Item

- `class AgentCloseSubagentCallItem`

  A request to close a subagent.

  - `id: String`

    The ID of the tool call item.

  - `recipient_agent_id: String`

    The ID of the agent to close.

  - `sender_agent_id: String`

    The ID of the agent requesting the close.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :close_subagent_call`

    The item type. Always `close_subagent_call`.

    - `:close_subagent_call`

      The current public item type.

### Agent Command Execution Item

- `class AgentCommandExecutionItem`

  A command execution produced by the agent.

  - `id: String`

    The ID of the command execution item.

  - `command: String`

    The command that was executed.

  - `cwd: String`

    The working directory used to execute the command.

  - `duration_ms: Integer`

    The command duration in milliseconds.

  - `exit_code: Integer`

    The process exit code, if the command completed.

  - `output: String`

    The command output, if available.

  - `status: AgentFunctionCallStatus`

    The status of the command execution.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :command_execution`

    The item type. Always `command_execution`.

    - `:command_execution`

### Agent Content

- `AgentContent = OutputText | EncryptedContent{ encrypted_content, type}`

  A plaintext or encrypted content part exchanged between agents.

  - `class OutputText`

    A text content part produced by the agent.

    - `text: String`

      The text produced by the agent.

    - `type: :output_text`

      The content type. Always `output_text`.

      - `:output_text`

  - `class EncryptedContent`

    Encrypted content exchanged between agents.

    - `encrypted_content: String`

      The encrypted content payload.

    - `type: :encrypted_content`

      The content type. Always `encrypted_content`.

      - `:encrypted_content`

### Agent Create Subagent Call Item

- `class AgentCreateSubagentCallItem`

  A request to spawn a subagent.

  - `id: String`

    The ID of the tool call item.

  - `agent_id: String`

    The ID of the agent that requested the subagent.

  - `content: Array[AgentContent]`

    The task given to the spawned agent.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `model: String`

    The model requested for the spawned agent.

  - `reasoning_effort: String`

    The reasoning effort requested for the spawned agent.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :create_subagent_call`

    The item type. Always `create_subagent_call`.

    - `:create_subagent_call`

      The current public item type.

### Agent Deleted

- `class AgentDeleted`

  A deleted reusable agent.

  - `id: String`

    The ID of the deleted agent.

  - `deleted: bool`

    Whether the agent was deleted. Always `true`.

  - `object: :"agent.deleted"`

    The object type. Always `agent.deleted`.

    - `:"agent.deleted"`

### Agent Function Call Item

- `class AgentFunctionCallItem`

  A function call produced by the agent.

  - `id: String`

    The ID of the function call item.

  - `arguments: untyped`

    The arguments to pass to the function.

  - `call_id: String`

    The ID used to submit the function result.

  - `name: String`

    The name of the function to call.

  - `status: AgentFunctionCallStatus`

    The status of the function call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :function_call`

    The item type. Always `function_call`.

    - `:function_call`

### Agent Function Call Output

- `AgentFunctionCallOutput = String | Array[InputContent]`

  The text or model-input content supplied as a function result.

  - `String = String`

  - `UnionMember1 = Array[InputContent]`

    - `class InputText`

      Text input recorded in a session item.

      - `text: String`

        The text supplied to the agent.

      - `type: :input_text`

        The type of the object. Always `input_text`.

        - `:input_text`

    - `class InputImage`

      Image input recorded in a session item.

      - `image_url: String`

        The URL of the image supplied to the agent, which may be a base64-encoded data URL.

      - `type: :input_image`

        The type of the object. Always `input_image`.

        - `:input_image`

### Agent Function Call Output Param

- `AgentFunctionCallOutputParam = String | Array[InputContentParam]`

  A function result represented as text or supported model-input content.

  - `String = String`

  - `UnionMember1 = Array[InputContentParam]`

    - `class InputText`

      Text input to the model.

      - `text: String`

        The text sent to the model.

      - `type: :input_text`

        The type of the object. Always `input_text`.

        - `:input_text`

    - `class InputImage`

      Image input to the model.

      - `image_url: String`

        The URL of the image sent to the model.

      - `type: :input_image`

        The type of the object. Always `input_image`.

        - `:input_image`

### Agent Function Call Status

- `AgentFunctionCallStatus = :in_progress | :completed | :failed | :incomplete`

  The status of a tool call.

  - `:in_progress`

    The call is in progress.

  - `:completed`

    The call completed successfully.

  - `:failed`

    The call failed.

  - `:incomplete`

    The call stopped before completing.

### Agent Interrupt Subagent Call Item

- `class AgentInterruptSubagentCallItem`

  A request to interrupt a subagent's current turn. The subagent remains available.

  - `id: String`

    The ID of the tool call item.

  - `recipient_agent_id: String`

    The ID of the agent to interrupt.

  - `sender_agent_id: String`

    The ID of the agent requesting the interrupt.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :interrupt_subagent_call`

    The item type. Always `interrupt_subagent_call`.

    - `:interrupt_subagent_call`

      The current public item type.

### Agent Mcp Call Item

- `class AgentMcpCallItem`

  A call to a tool on an MCP server.

  - `id: String`

    The ID of the MCP call item.

  - `arguments: untyped`

    The arguments passed to the MCP tool.

  - `error: untyped`

    The error returned by the MCP tool, if any.

  - `name: String`

    The name of the MCP tool.

  - `output: untyped`

    The output returned by the MCP tool, if any.

  - `server_label: String`

    The label of the MCP server.

  - `status: AgentFunctionCallStatus`

    The status of the MCP tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :mcp_call`

    The item type. Always `mcp_call`.

    - `:mcp_call`

### Agent Output Command Execution Output Delta Event

- `class AgentOutputCommandExecutionOutputDeltaEvent`

  Emitted when command execution produces an output delta.

  - `delta: String`

    The output text that was appended.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the command execution item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.output.command_execution_output.delta"`

    The type of the object. Always `agent.output.command_execution_output.delta`.

    - `:"agent.output.command_execution_output.delta"`

### Agent Output Item

- `AgentOutputItem = AgentSessionAssistantMessage | AgentReasoningItem | AgentFunctionCallItem | 11 more`

  An output item produced by an agent.

  - `class AgentSessionAssistantMessage`

    An assistant message produced by the agent.

    - `id: String`

      The ID of the message.

    - `content: Array[OutputText]`

      The content of the message.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of the assistant message.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :assistant`

      The role of the message author. Always `assistant`.

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Agent Output Item Status

- `AgentOutputItemStatus = :in_progress | :completed | :incomplete`

  The status of an agent output item.

  - `:in_progress`

    The item is in progress.

  - `:completed`

    The item is complete.

  - `:incomplete`

    The item stopped before completing.

### Agent Reasoning

- `class AgentReasoning`

  The reasoning configuration used by an agent.

  - `effort: :none | :minimal | :low | 4 more`

    The requested reasoning effort, or `null` when the model selects its own default.

    - `:none`

    - `:minimal`

    - `:low`

    - `:medium`

    - `:high`

    - `:xhigh`

    - `:max`

  - `summary: :concise | :detailed | :auto`

    The requested reasoning summary format, or `null` when summaries are disabled.

    - `:concise`

      Returns a concise reasoning summary when supported.

    - `:detailed`

      Returns a detailed reasoning summary when supported.

    - `:auto`

      Automatically selects the most detailed summary supported by the model.

### Agent Reasoning Item

- `class AgentReasoningItem`

  A reasoning item produced by the agent.

  - `id: String`

    The ID of the reasoning item.

  - `status: AgentOutputItemStatus`

    The status of the reasoning item.

    - `:in_progress`

      The item is in progress.

    - `:completed`

      The item is complete.

    - `:incomplete`

      The item stopped before completing.

  - `summary: Array[SummaryText]`

    The reasoning summaries produced by the agent.

    - `text: String`

      The reasoning summary text.

    - `type: :summary_text`

      The content type. Always `summary_text`.

      - `:summary_text`

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :reasoning`

    The item type. Always `reasoning`.

    - `:reasoning`

### Agent Reasoning Param

- `class AgentReasoningParam`

  Reasoning configuration for the agent.

  - `effort: :none | :minimal | :low | 4 more`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `:none`

    - `:minimal`

    - `:low`

    - `:medium`

    - `:high`

    - `:xhigh`

    - `:max`

  - `summary: :concise | :detailed | :auto`

    Controls whether the response includes a reasoning summary.

    - `:concise`

      Returns a concise reasoning summary when supported.

    - `:detailed`

      Returns a detailed reasoning summary when supported.

    - `:auto`

      Automatically selects the most detailed summary supported by the model.

### Agent Resume Subagent Call Item

- `class AgentResumeSubagentCallItem`

  A request to resume a subagent.

  - `id: String`

    The ID of the tool call item.

  - `recipient_agent_id: String`

    The ID of the agent to resume.

  - `sender_agent_id: String`

    The ID of the agent requesting the resume.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :resume_subagent_call`

    The item type. Always `resume_subagent_call`.

    - `:resume_subagent_call`

      The current public item type.

### Agent Send Subagent Input Call Item

- `class AgentSendSubagentInputCallItem`

  A request to send input to another agent.

  - `id: String`

    The ID of the tool call item.

  - `content: Array[AgentContent]`

    The input sent to the receiving agent.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `recipient_agent_id: String`

    The ID of the agent receiving the input.

  - `sender_agent_id: String`

    The ID of the agent sending the input.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :send_subagent_input_call`

    The item type. Always `send_subagent_input_call`.

    - `:send_subagent_input_call`

      The current public item type.

### Agent Session

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: :none | :minimal | :low | 4 more`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `summary: :concise | :detailed | :auto`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `:concise`

          Returns a concise reasoning summary when supported.

        - `:detailed`

          Returns a detailed reasoning summary when supported.

        - `:auto`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: :auto | :default | :flex | 3 more`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

      - `format_: TextFormat`

        The effective output format. Defaults to ordinary text.

        - `class Text`

          Generates ordinary text without a structured-output constraint.

          - `type: :text`

            The type of the object. Always `text`.

            - `:text`

        - `class JSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Hash[Symbol, untyped]`

            The JSON Schema that generated text must match.

          - `type: :json_schema`

            The type of the object. Always `json_schema`.

            - `:json_schema`

      - `verbosity: :low | :medium | :high`

        The amount of text produced by the agent. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

    - `tools: Array[AgentTool]`

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

      - `class ProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: :programmatic_tool_calling`

          The type of the object. Always `programmatic_tool_calling`.

          - `:programmatic_tool_calling`

      - `class Mcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array[String]`

          The MCP tools the agent may call.

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

            - `type: :stdio`

              The type of the object. Always `stdio`.

              - `:stdio`

        - `type: :mcp`

          The type of the object. Always `mcp`.

          - `:mcp`

      - `class WebSearch`

        Web search.

        - `allowed_domains: Array[String]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: :disabled | :cached | :live`

          The source used for web search results.

          - `:disabled`

          - `:cached`

          - `:live`

        - `type: :web_search`

          The type of the object. Always `web_search`.

          - `:web_search`

      - `class ComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: :computer_use`

          The type of the object. Always `computer_use`.

          - `:computer_use`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

        - `access: :enabled | :disabled | :restricted`

          The environment's network access mode.

          - `:enabled`

            Allows unrestricted network access.

          - `:disabled`

            Disables network access.

          - `:restricted`

            Applies the configured domain restrictions.

        - `allowed_domains: Array[String]`

          Domains the environment may access when network access is restricted.

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Agent Session Assistant Message

- `class AgentSessionAssistantMessage`

  An assistant message produced by the agent.

  - `id: String`

    The ID of the message.

  - `content: Array[OutputText]`

    The content of the message.

    - `text: String`

      The text produced by the agent.

    - `type: :output_text`

      The content type. Always `output_text`.

      - `:output_text`

  - `phase: :commentary | :final_answer`

    The phase of the assistant message.

    - `:commentary`

      Commentary produced while the agent works.

    - `:final_answer`

      The agent's final answer.

  - `role: :assistant`

    The role of the message author. Always `assistant`.

    - `:assistant`

  - `status: AgentOutputItemStatus`

    The status of the message.

    - `:in_progress`

      The item is in progress.

    - `:completed`

      The item is complete.

    - `:incomplete`

      The item stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :message`

    The item type. Always `message`.

    - `:message`

### Agent Session Created Event

- `class AgentSessionCreatedEvent`

  Emitted when a session is created.

  - `event_id: String`

    The unique ID of the event.

  - `session: AgentSession`

    The session that was created.

    - `id: String`

      The ID of the session.

    - `agent: Agent{ id, instructions, model, 6 more}`

      The agent running in the session.

      - `id: String`

        The ID of the agent.

      - `instructions: String`

        Custom instructions appended to the agent's default base instructions.

      - `model: String`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Integer`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: String`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: :none | :minimal | :low | 4 more`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

          - `:max`

        - `summary: :concise | :detailed | :auto`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `:concise`

            Returns a concise reasoning summary when supported.

          - `:detailed`

            Returns a detailed reasoning summary when supported.

          - `:auto`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: :auto | :default | :flex | 3 more`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `:auto`

        - `:default`

        - `:flex`

        - `:priority`

        - `:fast`

        - `:ultrafast`

      - `text: AgentText`

        Configuration for text generated by the agent.

        - `format_: TextFormat`

          The effective output format. Defaults to ordinary text.

          - `class Text`

            Generates ordinary text without a structured-output constraint.

            - `type: :text`

              The type of the object. Always `text`.

              - `:text`

          - `class JSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Hash[Symbol, untyped]`

              The JSON Schema that generated text must match.

            - `type: :json_schema`

              The type of the object. Always `json_schema`.

              - `:json_schema`

        - `verbosity: :low | :medium | :high`

          The amount of text produced by the agent. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

      - `tools: Array[AgentTool]`

        Tools available to the agent.

        - `class Function`

          A function defined by the application.

          - `defer_loading: bool`

            Whether the function is deferred and discovered through tool search.

          - `description: String`

            A description of what the function does.

          - `name: String`

            The name of the function.

          - `parameters: Hash[Symbol, untyped]`

            A JSON Schema object describing the function's arguments.

          - `type: :function`

            The type of the object. Always `function`.

            - `:function`

        - `class ProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: :programmatic_tool_calling`

            The type of the object. Always `programmatic_tool_calling`.

            - `:programmatic_tool_calling`

        - `class Mcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array[String]`

            The MCP tools the agent may call.

          - `connection_origin: :service | :environment`

            Where outbound MCP HTTP connections originate.

            - `:service`

            - `:environment`

          - `credential_id: String`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Hash[Symbol, untyped]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: String`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class HTTP`

              Connects to an MCP server over HTTP.

              - `server_url: String`

                The URL of the MCP server.

              - `type: :http`

                The type of the object. Always `http`.

                - `:http`

            - `class Stdio`

              Starts an MCP server as a local process.

              - `args: Array[String]`

                Arguments passed to the MCP server command.

              - `command: String`

                The command used to start the MCP server.

              - `cwd: String`

                The working directory used to start the MCP server.

              - `env_vars: Array[String]`

                Environment variable names inherited from the execution environment.

              - `type: :stdio`

                The type of the object. Always `stdio`.

                - `:stdio`

          - `type: :mcp`

            The type of the object. Always `mcp`.

            - `:mcp`

        - `class WebSearch`

          Web search.

          - `allowed_domains: Array[String]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: :low | :medium | :high`

            The amount of search context made available to the model. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

          - `location: Location{ city, country, region, timezone}`

            Approximate location used to localize search results, if provided.

            - `city: String`

              The city name.

            - `country: String`

              The two-letter ISO country code, such as `US`.

            - `region: String`

              The region or state name.

            - `timezone: String`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: :disabled | :cached | :live`

            The source used for web search results.

            - `:disabled`

            - `:cached`

            - `:live`

          - `type: :web_search`

            The type of the object. Always `web_search`.

            - `:web_search`

        - `class ComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: :computer_use`

            The type of the object. Always `computer_use`.

            - `:computer_use`

    - `created_at: Integer`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class None`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: :none`

          The type of the object. Always `none`.

          - `:none`

      - `class OpenAIHosted`

        An environment hosted by OpenAI.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop{ enabled}`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `file_id: String`

              The ID of the uploaded file.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :file_id`

              The type of the object. Always `file_id`.

              - `:file_id`

          - `class Inline`

            A file supplied inline when the session was created.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `network: Network{ access, allowed_domains}`

          The effective network access policy for the environment.

          - `access: :enabled | :disabled | :restricted`

            The environment's network access mode.

            - `:enabled`

              Allows unrestricted network access.

            - `:disabled`

              Disables network access.

            - `:restricted`

              Applies the configured domain restrictions.

          - `allowed_domains: Array[String]`

            Domains the environment may access when network access is restricted.

        - `packages: Packages{ npm, python, system_}`

          Packages installed in the environment.

          - `npm: Array[String]`

            npm packages installed globally in the environment.

          - `python: Array[String]`

            Python packages installed in the environment.

          - `system_: Array[String]`

            System packages installed in the environment.

        - `plugins: Array[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: String`

            The installed plugin description.

          - `name: String`

            The installed plugin name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

        - `skills: Array[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference`

            A skill installed from the Skills API.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `skill_id: String`

              The referenced skill ID.

            - `type: :skill_reference`

              The type of the object. Always `skill_reference`.

              - `:skill_reference`

            - `version: String`

              The concrete skill version installed for this session.

          - `class Inline`

            A skill installed from an inline ZIP archive.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `type: :openai_hosted`

          The type of the object. Always `openai_hosted`.

          - `:openai_hosted`

        - `container_size: :small | :medium | :large`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `:small`

          - `:medium`

          - `:large`

      - `class SelfHosted`

        An environment hosted by the application.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: String`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: :self_hosted`

          The type of the object. Always `self_hosted`.

          - `:self_hosted`

        - `workspace_directory: String`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: String`

      The error that caused the session to fail, if any.

    - `last_active_at: Integer`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Hash[Symbol, String]`

      Custom string key-value pairs attached to the session.

    - `object: :"agent.session"`

      The object type. Always `agent.session`.

      - `:"agent.session"`

    - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

          The information needed to render the request.

          - `class BrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: String`

              The registered form or frame origin where values will be entered.

            - `fields: Array[Field{ id, label, required, type}]`

              Controls to render. All submitted values are sensitive.

              - `id: String`

                The field ID to submit as field_id in a fields entry.

              - `label: String`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: String`

                The rendering type, such as email, password, or text.

            - `options: Array[Option{ id, field_ids, label}]`

              Sign-in methods. Empty for a plain form.

              - `id: String`

                The option ID to submit as selected_option.

              - `field_ids: Array[String]`

                IDs from the registered fields that this method accepts.

              - `label: String`

                The method label to display.

            - `reason: String`

              Why the agent needs the user to sign in.

            - `type: :browser_authentication`

              The type of the object. Always `browser_authentication`.

              - `:browser_authentication`

          - `class BrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: String`

              The origin the browser needs permission to access.

            - `reason: String`

              The browser's explanation for this request, or null when unavailable.

            - `type: :browser_origin_access`

              The type of the object. Always `browser_origin_access`.

              - `:browser_origin_access`

        - `request_id: String`

          The registered request ID to echo when responding.

        - `turn_id: String`

          The turn that requested approval.

        - `type: :computer_use_approval_request`

          The type of the object. Always `computer_use_approval_request`.

          - `:computer_use_approval_request`

      - `class FunctionCall`

        Run a function tool and submit its result.

        - `arguments: untyped`

          The arguments supplied by the model.

        - `call_id: String`

          The ID to include when submitting the function result.

        - `name: String`

          The function name.

        - `turn_id: String`

          The ID of the turn that requested the function call.

        - `type: :function_call`

          The type of the object. Always `function_call`.

          - `:function_call`

      - `class EnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: String`

          The ID of the environment to reconnect.

        - `type: :environment_connection`

          The type of the object. Always `environment_connection`.

          - `:environment_connection`

    - `status: :idle | :in_progress | :requires_action | :failed`

      The current status of the session.

      - `:idle`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `:in_progress`

        The session is processing a turn.

      - `:requires_action`

        The session is waiting for one or more required actions.

      - `:failed`

        The session failed.

    - `usage: TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array[String]`

      The IDs of vaults made available to the session.

  - `type: :"agent.session.created"`

    The type of the object. Always `agent.session.created`.

    - `:"agent.session.created"`

### Agent Session Deleted

- `class AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: String`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: :"agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `:"agent.session.deleted"`

### Agent Session Environment Connected Event

- `class AgentSessionEnvironmentConnectedEvent`

  Emitted when a session environment connects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: String`

      The public ID of the environment.

    - `error: Error{ code, message, type}`

      The error reported while preparing the environment, if any.

      - `code: String`

        A machine-readable error code.

      - `message: String`

        A human-readable error message.

      - `type: String`

        The error type.

    - `status: :pending | :ready | :connected | 2 more`

      The environment's connection status.

      - `:pending`

        The environment is being prepared.

      - `:ready`

        The environment is ready to connect.

      - `:connected`

        The environment is connected.

      - `:disconnected`

        The environment is disconnected.

      - `:failed`

        The environment failed to connect.

    - `type: String`

      The environment type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.environment.connected"`

    The type of the object. Always `agent.session.environment.connected`.

    - `:"agent.session.environment.connected"`

### Agent Session Environment Disconnected Event

- `class AgentSessionEnvironmentDisconnectedEvent`

  Emitted when a session environment disconnects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: String`

      The public ID of the environment.

    - `error: Error{ code, message, type}`

      The error reported while preparing the environment, if any.

      - `code: String`

        A machine-readable error code.

      - `message: String`

        A human-readable error message.

      - `type: String`

        The error type.

    - `status: :pending | :ready | :connected | 2 more`

      The environment's connection status.

      - `:pending`

        The environment is being prepared.

      - `:ready`

        The environment is ready to connect.

      - `:connected`

        The environment is connected.

      - `:disconnected`

        The environment is disconnected.

      - `:failed`

        The environment failed to connect.

    - `type: String`

      The environment type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.environment.disconnected"`

    The type of the object. Always `agent.session.environment.disconnected`.

    - `:"agent.session.environment.disconnected"`

### Agent Session Environment Failed Event

- `class AgentSessionEnvironmentFailedEvent`

  Emitted when a session environment fails.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: String`

      The public ID of the environment.

    - `error: Error{ code, message, type}`

      The error reported while preparing the environment, if any.

      - `code: String`

        A machine-readable error code.

      - `message: String`

        A human-readable error message.

      - `type: String`

        The error type.

    - `status: :pending | :ready | :connected | 2 more`

      The environment's connection status.

      - `:pending`

        The environment is being prepared.

      - `:ready`

        The environment is ready to connect.

      - `:connected`

        The environment is connected.

      - `:disconnected`

        The environment is disconnected.

      - `:failed`

        The environment failed to connect.

    - `type: String`

      The environment type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.environment.failed"`

    The type of the object. Always `agent.session.environment.failed`.

    - `:"agent.session.environment.failed"`

### Agent Session Environment Pending Event

- `class AgentSessionEnvironmentPendingEvent`

  Emitted while a session environment is being prepared.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: String`

      The public ID of the environment.

    - `error: Error{ code, message, type}`

      The error reported while preparing the environment, if any.

      - `code: String`

        A machine-readable error code.

      - `message: String`

        A human-readable error message.

      - `type: String`

        The error type.

    - `status: :pending | :ready | :connected | 2 more`

      The environment's connection status.

      - `:pending`

        The environment is being prepared.

      - `:ready`

        The environment is ready to connect.

      - `:connected`

        The environment is connected.

      - `:disconnected`

        The environment is disconnected.

      - `:failed`

        The environment failed to connect.

    - `type: String`

      The environment type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.environment.pending"`

    The type of the object. Always `agent.session.environment.pending`.

    - `:"agent.session.environment.pending"`

### Agent Session Environment Ready Event

- `class AgentSessionEnvironmentReadyEvent`

  Emitted when a hosted session environment is ready to connect.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: String`

      The public ID of the environment.

    - `error: Error{ code, message, type}`

      The error reported while preparing the environment, if any.

      - `code: String`

        A machine-readable error code.

      - `message: String`

        A human-readable error message.

      - `type: String`

        The error type.

    - `status: :pending | :ready | :connected | 2 more`

      The environment's connection status.

      - `:pending`

        The environment is being prepared.

      - `:ready`

        The environment is ready to connect.

      - `:connected`

        The environment is connected.

      - `:disconnected`

        The environment is disconnected.

      - `:failed`

        The environment failed to connect.

    - `type: String`

      The environment type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.environment.ready"`

    The type of the object. Always `agent.session.environment.ready`.

    - `:"agent.session.environment.ready"`

### Agent Session Environment Reset Event

- `class AgentSessionEnvironmentResetEvent`

  Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

  - `environment_id: String`

    The stable environment ID, retained across sandbox replacements.

  - `event_id: String`

    The unique ID of the event.

  - `reset_count: Integer`

    Monotonically increasing reset number. Repeated notifications share this number.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The associated turn, when applicable.

  - `type: :"agent.session.environment.reset"`

    The type of the object. Always `agent.session.environment.reset`.

    - `:"agent.session.environment.reset"`

### Agent Session Environment State

- `class AgentSessionEnvironmentState`

  The current state of a session environment.

  - `id: String`

    The public ID of the environment.

  - `error: Error{ code, message, type}`

    The error reported while preparing the environment, if any.

    - `code: String`

      A machine-readable error code.

    - `message: String`

      A human-readable error message.

    - `type: String`

      The error type.

  - `status: :pending | :ready | :connected | 2 more`

    The environment's connection status.

    - `:pending`

      The environment is being prepared.

    - `:ready`

      The environment is ready to connect.

    - `:connected`

      The environment is connected.

    - `:disconnected`

      The environment is disconnected.

    - `:failed`

      The environment failed to connect.

  - `type: String`

    The environment type.

### Agent Session Error Event

- `class AgentSessionErrorEvent`

  Emitted when a turn or session fails.

  - `error: SessionError`

    The error that occurred.

    - `code: String`

      The machine-readable error code, if any.

    - `message: String`

      A customer-safe explanation of the error.

    - `param: String`

      The request parameter associated with the error, if any.

    - `type: String`

      The error type.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `type: :error`

    The type of the object. Always `error`.

    - `:error`

### Agent Session Event

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: String`

        The machine-readable error code, if any.

      - `message: String`

        A customer-safe explanation of the error.

      - `param: String`

        The request parameter associated with the error, if any.

      - `type: String`

        The error type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `type: :error`

      The type of the object. Always `error`.

      - `:error`

  - `class AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: String`

        The public ID of the environment.

      - `error: Error{ code, message, type}`

        The error reported while preparing the environment, if any.

        - `code: String`

          A machine-readable error code.

        - `message: String`

          A human-readable error message.

        - `type: String`

          The error type.

      - `status: :pending | :ready | :connected | 2 more`

        The environment's connection status.

        - `:pending`

          The environment is being prepared.

        - `:ready`

          The environment is ready to connect.

        - `:connected`

          The environment is connected.

        - `:disconnected`

          The environment is disconnected.

        - `:failed`

          The environment failed to connect.

      - `type: String`

        The environment type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `:"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: String`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: String`

      The unique ID of the event.

    - `reset_count: Integer`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The associated turn, when applicable.

    - `type: :"agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `:"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: String`

      The output text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the command execution item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `:"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: String`

        The ID of the session.

      - `agent: Agent{ id, instructions, model, 6 more}`

        The agent running in the session.

        - `id: String`

          The ID of the agent.

        - `instructions: String`

          Custom instructions appended to the agent's default base instructions.

        - `model: String`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: bool`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: Integer`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: String`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

          - `effort: :none | :minimal | :low | 4 more`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

            - `:max`

          - `summary: :concise | :detailed | :auto`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `:concise`

              Returns a concise reasoning summary when supported.

            - `:detailed`

              Returns a detailed reasoning summary when supported.

            - `:auto`

              Automatically selects the most detailed summary supported by the model.

        - `service_tier: :auto | :default | :flex | 3 more`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `:auto`

          - `:default`

          - `:flex`

          - `:priority`

          - `:fast`

          - `:ultrafast`

        - `text: AgentText`

          Configuration for text generated by the agent.

          - `format_: TextFormat`

            The effective output format. Defaults to ordinary text.

            - `class Text`

              Generates ordinary text without a structured-output constraint.

              - `type: :text`

                The type of the object. Always `text`.

                - `:text`

            - `class JSONSchema`

              Constrains generated text to a JSON Schema.

              - `schema: Hash[Symbol, untyped]`

                The JSON Schema that generated text must match.

              - `type: :json_schema`

                The type of the object. Always `json_schema`.

                - `:json_schema`

          - `verbosity: :low | :medium | :high`

            The amount of text produced by the agent. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

        - `tools: Array[AgentTool]`

          Tools available to the agent.

          - `class Function`

            A function defined by the application.

            - `defer_loading: bool`

              Whether the function is deferred and discovered through tool search.

            - `description: String`

              A description of what the function does.

            - `name: String`

              The name of the function.

            - `parameters: Hash[Symbol, untyped]`

              A JSON Schema object describing the function's arguments.

            - `type: :function`

              The type of the object. Always `function`.

              - `:function`

          - `class ProgrammaticToolCalling`

            Enables calling tools from model-generated code.

            - `enabled: bool`

              Whether tools can be called from model-generated code.

            - `type: :programmatic_tool_calling`

              The type of the object. Always `programmatic_tool_calling`.

              - `:programmatic_tool_calling`

          - `class Mcp`

            Tools provided by a remote MCP server.

            - `allowed_tools: Array[String]`

              The MCP tools the agent may call.

            - `connection_origin: :service | :environment`

              Where outbound MCP HTTP connections originate.

              - `:service`

              - `:environment`

            - `credential_id: String`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Hash[Symbol, untyped]`

              Metadata included with requests to this MCP server.

            - `required: bool`

              Whether this MCP server must initialize before the first turn.

            - `server_label: String`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `class HTTP`

                Connects to an MCP server over HTTP.

                - `server_url: String`

                  The URL of the MCP server.

                - `type: :http`

                  The type of the object. Always `http`.

                  - `:http`

              - `class Stdio`

                Starts an MCP server as a local process.

                - `args: Array[String]`

                  Arguments passed to the MCP server command.

                - `command: String`

                  The command used to start the MCP server.

                - `cwd: String`

                  The working directory used to start the MCP server.

                - `env_vars: Array[String]`

                  Environment variable names inherited from the execution environment.

                - `type: :stdio`

                  The type of the object. Always `stdio`.

                  - `:stdio`

            - `type: :mcp`

              The type of the object. Always `mcp`.

              - `:mcp`

          - `class WebSearch`

            Web search.

            - `allowed_domains: Array[String]`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: :low | :medium | :high`

              The amount of search context made available to the model. Defaults to `medium`.

              - `:low`

              - `:medium`

              - `:high`

            - `location: Location{ city, country, region, timezone}`

              Approximate location used to localize search results, if provided.

              - `city: String`

                The city name.

              - `country: String`

                The two-letter ISO country code, such as `US`.

              - `region: String`

                The region or state name.

              - `timezone: String`

                The IANA timezone, such as `America/Los_Angeles`.

            - `mode: :disabled | :cached | :live`

              The source used for web search results.

              - `:disabled`

              - `:cached`

              - `:live`

            - `type: :web_search`

              The type of the object. Always `web_search`.

              - `:web_search`

          - `class ComputerUse`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: bool`

              Whether computer tool outputs include screenshots.

            - `type: :computer_use`

              The type of the object. Always `computer_use`.

              - `:computer_use`

      - `created_at: Integer`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `class None`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class OpenAIHosted`

          An environment hosted by OpenAI.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `desktop: Desktop{ enabled}`

            The effective desktop configuration.

            - `enabled: bool`

              Whether the environment provisions a desktop and browser proxy.

          - `files: Array[HostedEnvironmentFile]`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileID`

              A file copied from the OpenAI Files API.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `file_id: String`

                The ID of the uploaded file.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :file_id`

                The type of the object. Always `file_id`.

                - `:file_id`

            - `class Inline`

              A file supplied inline when the session was created.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `network: Network{ access, allowed_domains}`

            The effective network access policy for the environment.

            - `access: :enabled | :disabled | :restricted`

              The environment's network access mode.

              - `:enabled`

                Allows unrestricted network access.

              - `:disabled`

                Disables network access.

              - `:restricted`

                Applies the configured domain restrictions.

            - `allowed_domains: Array[String]`

              Domains the environment may access when network access is restricted.

          - `packages: Packages{ npm, python, system_}`

            Packages installed in the environment.

            - `npm: Array[String]`

              npm packages installed globally in the environment.

            - `python: Array[String]`

              Python packages installed in the environment.

            - `system_: Array[String]`

              System packages installed in the environment.

          - `plugins: Array[HostedPlugin]`

            Plugins installed in the environment, excluding their archive contents.

            - `description: String`

              The installed plugin description.

            - `name: String`

              The installed plugin name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

          - `skills: Array[HostedSkill]`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference`

              A skill installed from the Skills API.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `skill_id: String`

                The referenced skill ID.

              - `type: :skill_reference`

                The type of the object. Always `skill_reference`.

                - `:skill_reference`

              - `version: String`

                The concrete skill version installed for this session.

            - `class Inline`

              A skill installed from an inline ZIP archive.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `type: :openai_hosted`

            The type of the object. Always `openai_hosted`.

            - `:openai_hosted`

          - `container_size: :small | :medium | :large`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `:small`

            - `:medium`

            - `:large`

        - `class SelfHosted`

          An environment hosted by the application.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: String`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: :self_hosted`

            The type of the object. Always `self_hosted`.

            - `:self_hosted`

          - `workspace_directory: String`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: String`

        The error that caused the session to fail, if any.

      - `last_active_at: Integer`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Hash[Symbol, String]`

        Custom string key-value pairs attached to the session.

      - `object: :"agent.session"`

        The object type. Always `agent.session`.

        - `:"agent.session"`

      - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

        Actions that must be completed before the session can continue.

        - `class ComputerUseApprovalRequest`

          Respond to a computer-use request.

          - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

            The information needed to render the request.

            - `class BrowserAuthentication`

              A registered form awaiting the application's response.

              - `credential_origin: String`

                The registered form or frame origin where values will be entered.

              - `fields: Array[Field{ id, label, required, type}]`

                Controls to render. All submitted values are sensitive.

                - `id: String`

                  The field ID to submit as field_id in a fields entry.

                - `label: String`

                  The label to display beside the control.

                - `required: bool`

                  Whether this control requires a nonempty value.

                - `type: String`

                  The rendering type, such as email, password, or text.

              - `options: Array[Option{ id, field_ids, label}]`

                Sign-in methods. Empty for a plain form.

                - `id: String`

                  The option ID to submit as selected_option.

                - `field_ids: Array[String]`

                  IDs from the registered fields that this method accepts.

                - `label: String`

                  The method label to display.

              - `reason: String`

                Why the agent needs the user to sign in.

              - `type: :browser_authentication`

                The type of the object. Always `browser_authentication`.

                - `:browser_authentication`

            - `class BrowserOriginAccess`

              A browser origin awaiting the application's approval decision.

              - `origin: String`

                The origin the browser needs permission to access.

              - `reason: String`

                The browser's explanation for this request, or null when unavailable.

              - `type: :browser_origin_access`

                The type of the object. Always `browser_origin_access`.

                - `:browser_origin_access`

          - `request_id: String`

            The registered request ID to echo when responding.

          - `turn_id: String`

            The turn that requested approval.

          - `type: :computer_use_approval_request`

            The type of the object. Always `computer_use_approval_request`.

            - `:computer_use_approval_request`

        - `class FunctionCall`

          Run a function tool and submit its result.

          - `arguments: untyped`

            The arguments supplied by the model.

          - `call_id: String`

            The ID to include when submitting the function result.

          - `name: String`

            The function name.

          - `turn_id: String`

            The ID of the turn that requested the function call.

          - `type: :function_call`

            The type of the object. Always `function_call`.

            - `:function_call`

        - `class EnvironmentConnection`

          Reconnect a session environment.

          - `environment_id: String`

            The ID of the environment to reconnect.

          - `type: :environment_connection`

            The type of the object. Always `environment_connection`.

            - `:environment_connection`

      - `status: :idle | :in_progress | :requires_action | :failed`

        The current status of the session.

        - `:idle`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `:in_progress`

          The session is processing a turn.

        - `:requires_action`

          The session is waiting for one or more required actions.

        - `:failed`

          The session failed.

      - `usage: TokenUsage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: Integer`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails{ cached_tokens}`

          A breakdown of the agent's input token usage.

          - `cached_tokens: Integer`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: Integer`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: Integer`

            The number of output tokens used for reasoning.

        - `total_tokens: Integer`

          The total number of input and output tokens used by the agent.

      - `vault_ids: Array[String]`

        The IDs of vaults made available to the session.

    - `type: :"agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `:"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: String`

        The ID of the turn.

      - `agent_id: String`

        The ID of the agent that ran the turn.

      - `completed_at: Integer`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: Integer`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError`

        A customer-safe error. Non-null only for a failed turn.

        - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

          A stable, machine-readable failure category.

          - `:context_length_exceeded`

            The request exceeds the model's context window.

          - `:session_budget_exceeded`

            The session has reached its usage budget.

          - `:usage_limit_exceeded`

            The organization has reached a usage, plan, or billing limit.

          - `:credit_balance_exhausted`

            The organization has no API credits remaining.

          - `:rate_limit_exceeded`

            The request exceeds the available rate limit.

          - `:flex_unavailable`

            Flex processing is temporarily unavailable.

          - `:server_overloaded`

            The model service is temporarily overloaded.

          - `:cyber_policy`

            The request was rejected by a safety policy.

          - `:misalignment_policy_violation`

            The request was blocked by the safety systems.

          - `:connection_failed`

            The request could not connect to the model service.

          - `:server_error`

            The model service encountered an unexpected error.

          - `:authentication_error`

            The API credentials are invalid or lack the required access.

          - `:invalid_request`

            The request contains invalid input or configuration.

          - `:resource_not_found`

            The requested model or resource is unavailable.

          - `:sandbox_error`

            The request could not complete in its execution environment.

          - `:executor_version_incompatible`

            The executor must be upgraded before it can run this turn.

          - `:active_turn_not_steerable`

            The session cannot accept additional input while a request is running.

          - `:request_timeout`

            The request timed out before the model service responded.

          - `:internal_error`

            An unexpected internal error prevented the session request from completing.

        - `message: String`

          A customer-safe explanation of the failure.

      - `object: :"agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `:"agent.session.turn"`

      - `session_id: String`

        The ID of the session that owns the turn.

      - `started_at: Integer`

        The Unix timestamp, in seconds, when the turn started.

      - `status: :queued | :in_progress | :waiting | 3 more`

        The current status of the turn.

        - `:queued`

          The turn is waiting to start.

        - `:in_progress`

          The turn is in progress.

        - `:waiting`

          The turn is waiting for external input.

        - `:completed`

          The turn completed successfully.

        - `:failed`

          The turn failed.

        - `:cancelled`

          The turn was cancelled.

      - `subagent_id: String`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `:"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `:"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `:"agent.session.turn.completed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `:"agent.session.turn.failed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `:"agent.session.turn.cancelled"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: String`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class InputText`

            Text supplied by the user.

            - `text: String`

              The text supplied by the user.

            - `type: :input_text`

              The type of the object. Always `input_text`.

              - `:input_text`

          - `class InputImage`

            An image supplied by the user.

            - `image_url: String`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: :input_image`

              The type of the object. Always `input_image`.

              - `:input_image`

          - `class OutputText`

            Text produced by the assistant.

            - `text: String`

              The text produced by the assistant.

            - `type: :output_text`

              The type of the object. Always `output_text`.

              - `:output_text`

        - `phase: :commentary | :final_answer`

          The phase of an assistant message. Null for user messages.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :user | :assistant`

          The role of the message author.

          - `:user`

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `:in_progress`

            The item is in progress.

          - `:completed`

            The item is complete.

          - `:incomplete`

            The item stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: String`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus`

          The status of the reasoning item.

        - `summary: Array[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: String`

            The reasoning summary text.

          - `type: :summary_text`

            The content type. Always `summary_text`.

            - `:summary_text`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :reasoning`

          The item type. Always `reasoning`.

          - `:reasoning`

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: String`

          The ID of the function call item.

        - `arguments: untyped`

          The arguments to pass to the function.

        - `call_id: String`

          The ID used to submit the function result.

        - `name: String`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `:in_progress`

            The call is in progress.

          - `:completed`

            The call completed successfully.

          - `:failed`

            The call failed.

          - `:incomplete`

            The call stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call`

          The item type. Always `function_call`.

          - `:function_call`

      - `class FunctionCallOutput`

        The result supplied for a function call.

        - `id: String`

          The ID of the function call output item.

        - `call_id: String`

          The ID of the function call that produced this output.

        - `error: String`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput`

          The function result, if the call succeeded.

          - `String = String`

          - `UnionMember1 = Array[InputContent]`

            - `class InputText`

              Text input recorded in a session item.

              - `text: String`

                The text supplied to the agent.

              - `type: :input_text`

                The type of the object. Always `input_text`.

                - `:input_text`

            - `class InputImage`

              Image input recorded in a session item.

              - `image_url: String`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: :input_image`

                The type of the object. Always `input_image`.

                - `:input_image`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call_output`

          The item type. Always `function_call_output`.

          - `:function_call_output`

      - `class AgentMessage`

        A message exchanged between agent threads.

        - `id: String`

          The ID of the message.

        - `content: Array[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText`

            A text content part produced by the agent.

            - `text: String`

              The text produced by the agent.

            - `type: :output_text`

              The content type. Always `output_text`.

              - `:output_text`

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

            - `encrypted_content: String`

              The encrypted content payload.

            - `type: :encrypted_content`

              The content type. Always `encrypted_content`.

              - `:encrypted_content`

        - `recipient_agent_id: String`

          The ID or name of the receiving agent.

        - `sender_agent_id: String`

          The ID or name of the sending agent.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :agent_message`

          The item type. Always `agent_message`.

          - `:agent_message`

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: String`

          The ID of the MCP call item.

        - `arguments: untyped`

          The arguments passed to the MCP tool.

        - `error: untyped`

          The error returned by the MCP tool, if any.

        - `name: String`

          The name of the MCP tool.

        - `output: untyped`

          The output returned by the MCP tool, if any.

        - `server_label: String`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :mcp_call`

          The item type. Always `mcp_call`.

          - `:mcp_call`

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class ComputerUseApprovalRequestResult`

        A credential-free record of an admitted response, not proof of completion.

        - `id: String`

          The stable history item ID.

        - `request_id: String`

          The registered request answered by this item.

        - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

          The admitted response, without submitted credential values.

          - `class Submit`

            - `action: :submit`

              - `:submit`

            - `selected_option: String`

              The chosen sign-in method, or null when no options were offered.

            - `type: :browser_authentication`

              - `:browser_authentication`

          - `class Cancel`

            - `action: :cancel`

              - `:cancel`

            - `type: :browser_authentication`

              - `:browser_authentication`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_approval_request_result`

          - `:computer_use_approval_request_result`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: String`

          The ID of the web search call.

        - `action: WebSearchAction`

          The action performed by the web search tool.

          - `class Search`

            A search query or group of search queries.

            - `queries: Array[String]`

              The search queries, when multiple queries were used.

            - `query: String`

              The search query, when a single query was used.

            - `type: :search`

              The type of the object. Always `search`.

              - `:search`

          - `class OpenPage`

            Opens a web page.

            - `type: :open_page`

              The type of the object. Always `open_page`.

              - `:open_page`

            - `url: String`

              The URL of the page that was opened.

          - `class FindInPage`

            Finds text within a web page.

            - `pattern: String`

              The text pattern that was searched for.

            - `type: :find_in_page`

              The type of the object. Always `find_in_page`.

              - `:find_in_page`

            - `url: String`

              The URL of the page that was searched.

          - `class Other`

            Another web search action.

            - `type: :other`

              The type of the object. Always `other`.

              - `:other`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :web_search_call`

          The item type. Always `web_search_call`.

          - `:web_search_call`

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: String`

          The ID of the command execution item.

        - `command: String`

          The command that was executed.

        - `cwd: String`

          The working directory used to execute the command.

        - `duration_ms: Integer`

          The command duration in milliseconds.

        - `exit_code: Integer`

          The process exit code, if the command completed.

        - `output: String`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :command_execution`

          The item type. Always `command_execution`.

          - `:command_execution`

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: String`

          The ID of the tool call item.

        - `agent_id: String`

          The ID of the agent that requested the subagent.

        - `content: Array[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `model: String`

          The model requested for the spawned agent.

        - `reasoning_effort: String`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :create_subagent_call`

          The item type. Always `create_subagent_call`.

          - `:create_subagent_call`

            The current public item type.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: String`

          The ID of the tool call item.

        - `content: Array[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: String`

          The ID of the agent receiving the input.

        - `sender_agent_id: String`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :send_subagent_input_call`

          The item type. Always `send_subagent_input_call`.

          - `:send_subagent_input_call`

            The current public item type.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to resume.

        - `sender_agent_id: String`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :resume_subagent_call`

          The item type. Always `resume_subagent_call`.

          - `:resume_subagent_call`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_ids: Array[String]`

          The IDs of the agents to wait for.

        - `sender_agent_id: String`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :wait_for_subagents_call`

          The item type. Always `wait_for_subagents_call`.

          - `:wait_for_subagents_call`

            The current public item type.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to interrupt.

        - `sender_agent_id: String`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :interrupt_subagent_call`

          The item type. Always `interrupt_subagent_call`.

          - `:interrupt_subagent_call`

            The current public item type.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to close.

        - `sender_agent_id: String`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :close_subagent_call`

          The item type. Always `close_subagent_call`.

          - `:close_subagent_call`

            The current public item type.

    - `output_index: Integer`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `:"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: :"agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `:"agent.session.idle"`

  - `class AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: :"agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `:"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: :"agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `:"agent.session.requires_action"`

  - `class AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: :"agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `:"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `:"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `:"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `:"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `:"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: String`

        The ID of the subagent.

      - `closed_at: Integer`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array[AgentContent]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `name: String`

        The runner-assigned nickname, or null when unavailable.

      - `object: :"agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `:"agent.session.subagent"`

      - `opened_at: Integer`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: String`

        The ID of the agent that created this subagent.

      - `session_id: String`

        The ID of the session that owns the subagent.

      - `status: :active | :closed`

        The current status of the subagent.

        - `:active`

          The subagent remains available, including while idle between turns.

        - `:closed`

          The subagent is closed.

    - `type: :"agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `:"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: :"agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `:"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: :"agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `:"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: String`

          The ID of the message.

        - `content: Array[OutputText]`

          The content of the message.

          - `text: String`

            The text produced by the agent.

          - `type: :output_text`

            The content type. Always `output_text`.

        - `phase: :commentary | :final_answer`

          The phase of the assistant message.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :assistant`

          The role of the message author. Always `assistant`.

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: Integer`

      The index of the output item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `:"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `:"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `:"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: Integer`

      The index of the content part in the message.

    - `delta: String`

      The text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `:"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `text: String`

      The complete output text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `:"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `:"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `status: :incomplete`

      Present as `incomplete` when summary generation was interrupted.

      - `:incomplete`

    - `summary_index: Integer`

      The index of the summary part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `:"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: String`

      The summary text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `:"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `text: String`

      The complete reasoning summary text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `:"agent.session.turn.reasoning_summary_text.done"`

### Agent Session Failed Event

- `class AgentSessionFailedEvent`

  Emitted when a session fails.

  - `event_id: String`

    The unique ID of the event.

  - `session: AgentSession`

    The failed session.

    - `id: String`

      The ID of the session.

    - `agent: Agent{ id, instructions, model, 6 more}`

      The agent running in the session.

      - `id: String`

        The ID of the agent.

      - `instructions: String`

        Custom instructions appended to the agent's default base instructions.

      - `model: String`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Integer`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: String`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: :none | :minimal | :low | 4 more`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

          - `:max`

        - `summary: :concise | :detailed | :auto`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `:concise`

            Returns a concise reasoning summary when supported.

          - `:detailed`

            Returns a detailed reasoning summary when supported.

          - `:auto`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: :auto | :default | :flex | 3 more`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `:auto`

        - `:default`

        - `:flex`

        - `:priority`

        - `:fast`

        - `:ultrafast`

      - `text: AgentText`

        Configuration for text generated by the agent.

        - `format_: TextFormat`

          The effective output format. Defaults to ordinary text.

          - `class Text`

            Generates ordinary text without a structured-output constraint.

            - `type: :text`

              The type of the object. Always `text`.

              - `:text`

          - `class JSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Hash[Symbol, untyped]`

              The JSON Schema that generated text must match.

            - `type: :json_schema`

              The type of the object. Always `json_schema`.

              - `:json_schema`

        - `verbosity: :low | :medium | :high`

          The amount of text produced by the agent. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

      - `tools: Array[AgentTool]`

        Tools available to the agent.

        - `class Function`

          A function defined by the application.

          - `defer_loading: bool`

            Whether the function is deferred and discovered through tool search.

          - `description: String`

            A description of what the function does.

          - `name: String`

            The name of the function.

          - `parameters: Hash[Symbol, untyped]`

            A JSON Schema object describing the function's arguments.

          - `type: :function`

            The type of the object. Always `function`.

            - `:function`

        - `class ProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: :programmatic_tool_calling`

            The type of the object. Always `programmatic_tool_calling`.

            - `:programmatic_tool_calling`

        - `class Mcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array[String]`

            The MCP tools the agent may call.

          - `connection_origin: :service | :environment`

            Where outbound MCP HTTP connections originate.

            - `:service`

            - `:environment`

          - `credential_id: String`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Hash[Symbol, untyped]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: String`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class HTTP`

              Connects to an MCP server over HTTP.

              - `server_url: String`

                The URL of the MCP server.

              - `type: :http`

                The type of the object. Always `http`.

                - `:http`

            - `class Stdio`

              Starts an MCP server as a local process.

              - `args: Array[String]`

                Arguments passed to the MCP server command.

              - `command: String`

                The command used to start the MCP server.

              - `cwd: String`

                The working directory used to start the MCP server.

              - `env_vars: Array[String]`

                Environment variable names inherited from the execution environment.

              - `type: :stdio`

                The type of the object. Always `stdio`.

                - `:stdio`

          - `type: :mcp`

            The type of the object. Always `mcp`.

            - `:mcp`

        - `class WebSearch`

          Web search.

          - `allowed_domains: Array[String]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: :low | :medium | :high`

            The amount of search context made available to the model. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

          - `location: Location{ city, country, region, timezone}`

            Approximate location used to localize search results, if provided.

            - `city: String`

              The city name.

            - `country: String`

              The two-letter ISO country code, such as `US`.

            - `region: String`

              The region or state name.

            - `timezone: String`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: :disabled | :cached | :live`

            The source used for web search results.

            - `:disabled`

            - `:cached`

            - `:live`

          - `type: :web_search`

            The type of the object. Always `web_search`.

            - `:web_search`

        - `class ComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: :computer_use`

            The type of the object. Always `computer_use`.

            - `:computer_use`

    - `created_at: Integer`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class None`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: :none`

          The type of the object. Always `none`.

          - `:none`

      - `class OpenAIHosted`

        An environment hosted by OpenAI.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop{ enabled}`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `file_id: String`

              The ID of the uploaded file.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :file_id`

              The type of the object. Always `file_id`.

              - `:file_id`

          - `class Inline`

            A file supplied inline when the session was created.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `network: Network{ access, allowed_domains}`

          The effective network access policy for the environment.

          - `access: :enabled | :disabled | :restricted`

            The environment's network access mode.

            - `:enabled`

              Allows unrestricted network access.

            - `:disabled`

              Disables network access.

            - `:restricted`

              Applies the configured domain restrictions.

          - `allowed_domains: Array[String]`

            Domains the environment may access when network access is restricted.

        - `packages: Packages{ npm, python, system_}`

          Packages installed in the environment.

          - `npm: Array[String]`

            npm packages installed globally in the environment.

          - `python: Array[String]`

            Python packages installed in the environment.

          - `system_: Array[String]`

            System packages installed in the environment.

        - `plugins: Array[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: String`

            The installed plugin description.

          - `name: String`

            The installed plugin name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

        - `skills: Array[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference`

            A skill installed from the Skills API.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `skill_id: String`

              The referenced skill ID.

            - `type: :skill_reference`

              The type of the object. Always `skill_reference`.

              - `:skill_reference`

            - `version: String`

              The concrete skill version installed for this session.

          - `class Inline`

            A skill installed from an inline ZIP archive.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `type: :openai_hosted`

          The type of the object. Always `openai_hosted`.

          - `:openai_hosted`

        - `container_size: :small | :medium | :large`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `:small`

          - `:medium`

          - `:large`

      - `class SelfHosted`

        An environment hosted by the application.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: String`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: :self_hosted`

          The type of the object. Always `self_hosted`.

          - `:self_hosted`

        - `workspace_directory: String`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: String`

      The error that caused the session to fail, if any.

    - `last_active_at: Integer`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Hash[Symbol, String]`

      Custom string key-value pairs attached to the session.

    - `object: :"agent.session"`

      The object type. Always `agent.session`.

      - `:"agent.session"`

    - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

          The information needed to render the request.

          - `class BrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: String`

              The registered form or frame origin where values will be entered.

            - `fields: Array[Field{ id, label, required, type}]`

              Controls to render. All submitted values are sensitive.

              - `id: String`

                The field ID to submit as field_id in a fields entry.

              - `label: String`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: String`

                The rendering type, such as email, password, or text.

            - `options: Array[Option{ id, field_ids, label}]`

              Sign-in methods. Empty for a plain form.

              - `id: String`

                The option ID to submit as selected_option.

              - `field_ids: Array[String]`

                IDs from the registered fields that this method accepts.

              - `label: String`

                The method label to display.

            - `reason: String`

              Why the agent needs the user to sign in.

            - `type: :browser_authentication`

              The type of the object. Always `browser_authentication`.

              - `:browser_authentication`

          - `class BrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: String`

              The origin the browser needs permission to access.

            - `reason: String`

              The browser's explanation for this request, or null when unavailable.

            - `type: :browser_origin_access`

              The type of the object. Always `browser_origin_access`.

              - `:browser_origin_access`

        - `request_id: String`

          The registered request ID to echo when responding.

        - `turn_id: String`

          The turn that requested approval.

        - `type: :computer_use_approval_request`

          The type of the object. Always `computer_use_approval_request`.

          - `:computer_use_approval_request`

      - `class FunctionCall`

        Run a function tool and submit its result.

        - `arguments: untyped`

          The arguments supplied by the model.

        - `call_id: String`

          The ID to include when submitting the function result.

        - `name: String`

          The function name.

        - `turn_id: String`

          The ID of the turn that requested the function call.

        - `type: :function_call`

          The type of the object. Always `function_call`.

          - `:function_call`

      - `class EnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: String`

          The ID of the environment to reconnect.

        - `type: :environment_connection`

          The type of the object. Always `environment_connection`.

          - `:environment_connection`

    - `status: :idle | :in_progress | :requires_action | :failed`

      The current status of the session.

      - `:idle`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `:in_progress`

        The session is processing a turn.

      - `:requires_action`

        The session is waiting for one or more required actions.

      - `:failed`

        The session failed.

    - `usage: TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array[String]`

      The IDs of vaults made available to the session.

  - `type: :"agent.session.failed"`

    The type of the object. Always `agent.session.failed`.

    - `:"agent.session.failed"`

### Agent Session Idle Event

- `class AgentSessionIdleEvent`

  Emitted when a session becomes idle.

  - `event_id: String`

    The unique ID of the event.

  - `session: AgentSession`

    The session that became idle.

    - `id: String`

      The ID of the session.

    - `agent: Agent{ id, instructions, model, 6 more}`

      The agent running in the session.

      - `id: String`

        The ID of the agent.

      - `instructions: String`

        Custom instructions appended to the agent's default base instructions.

      - `model: String`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Integer`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: String`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: :none | :minimal | :low | 4 more`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

          - `:max`

        - `summary: :concise | :detailed | :auto`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `:concise`

            Returns a concise reasoning summary when supported.

          - `:detailed`

            Returns a detailed reasoning summary when supported.

          - `:auto`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: :auto | :default | :flex | 3 more`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `:auto`

        - `:default`

        - `:flex`

        - `:priority`

        - `:fast`

        - `:ultrafast`

      - `text: AgentText`

        Configuration for text generated by the agent.

        - `format_: TextFormat`

          The effective output format. Defaults to ordinary text.

          - `class Text`

            Generates ordinary text without a structured-output constraint.

            - `type: :text`

              The type of the object. Always `text`.

              - `:text`

          - `class JSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Hash[Symbol, untyped]`

              The JSON Schema that generated text must match.

            - `type: :json_schema`

              The type of the object. Always `json_schema`.

              - `:json_schema`

        - `verbosity: :low | :medium | :high`

          The amount of text produced by the agent. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

      - `tools: Array[AgentTool]`

        Tools available to the agent.

        - `class Function`

          A function defined by the application.

          - `defer_loading: bool`

            Whether the function is deferred and discovered through tool search.

          - `description: String`

            A description of what the function does.

          - `name: String`

            The name of the function.

          - `parameters: Hash[Symbol, untyped]`

            A JSON Schema object describing the function's arguments.

          - `type: :function`

            The type of the object. Always `function`.

            - `:function`

        - `class ProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: :programmatic_tool_calling`

            The type of the object. Always `programmatic_tool_calling`.

            - `:programmatic_tool_calling`

        - `class Mcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array[String]`

            The MCP tools the agent may call.

          - `connection_origin: :service | :environment`

            Where outbound MCP HTTP connections originate.

            - `:service`

            - `:environment`

          - `credential_id: String`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Hash[Symbol, untyped]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: String`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class HTTP`

              Connects to an MCP server over HTTP.

              - `server_url: String`

                The URL of the MCP server.

              - `type: :http`

                The type of the object. Always `http`.

                - `:http`

            - `class Stdio`

              Starts an MCP server as a local process.

              - `args: Array[String]`

                Arguments passed to the MCP server command.

              - `command: String`

                The command used to start the MCP server.

              - `cwd: String`

                The working directory used to start the MCP server.

              - `env_vars: Array[String]`

                Environment variable names inherited from the execution environment.

              - `type: :stdio`

                The type of the object. Always `stdio`.

                - `:stdio`

          - `type: :mcp`

            The type of the object. Always `mcp`.

            - `:mcp`

        - `class WebSearch`

          Web search.

          - `allowed_domains: Array[String]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: :low | :medium | :high`

            The amount of search context made available to the model. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

          - `location: Location{ city, country, region, timezone}`

            Approximate location used to localize search results, if provided.

            - `city: String`

              The city name.

            - `country: String`

              The two-letter ISO country code, such as `US`.

            - `region: String`

              The region or state name.

            - `timezone: String`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: :disabled | :cached | :live`

            The source used for web search results.

            - `:disabled`

            - `:cached`

            - `:live`

          - `type: :web_search`

            The type of the object. Always `web_search`.

            - `:web_search`

        - `class ComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: :computer_use`

            The type of the object. Always `computer_use`.

            - `:computer_use`

    - `created_at: Integer`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class None`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: :none`

          The type of the object. Always `none`.

          - `:none`

      - `class OpenAIHosted`

        An environment hosted by OpenAI.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop{ enabled}`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `file_id: String`

              The ID of the uploaded file.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :file_id`

              The type of the object. Always `file_id`.

              - `:file_id`

          - `class Inline`

            A file supplied inline when the session was created.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `network: Network{ access, allowed_domains}`

          The effective network access policy for the environment.

          - `access: :enabled | :disabled | :restricted`

            The environment's network access mode.

            - `:enabled`

              Allows unrestricted network access.

            - `:disabled`

              Disables network access.

            - `:restricted`

              Applies the configured domain restrictions.

          - `allowed_domains: Array[String]`

            Domains the environment may access when network access is restricted.

        - `packages: Packages{ npm, python, system_}`

          Packages installed in the environment.

          - `npm: Array[String]`

            npm packages installed globally in the environment.

          - `python: Array[String]`

            Python packages installed in the environment.

          - `system_: Array[String]`

            System packages installed in the environment.

        - `plugins: Array[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: String`

            The installed plugin description.

          - `name: String`

            The installed plugin name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

        - `skills: Array[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference`

            A skill installed from the Skills API.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `skill_id: String`

              The referenced skill ID.

            - `type: :skill_reference`

              The type of the object. Always `skill_reference`.

              - `:skill_reference`

            - `version: String`

              The concrete skill version installed for this session.

          - `class Inline`

            A skill installed from an inline ZIP archive.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `type: :openai_hosted`

          The type of the object. Always `openai_hosted`.

          - `:openai_hosted`

        - `container_size: :small | :medium | :large`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `:small`

          - `:medium`

          - `:large`

      - `class SelfHosted`

        An environment hosted by the application.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: String`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: :self_hosted`

          The type of the object. Always `self_hosted`.

          - `:self_hosted`

        - `workspace_directory: String`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: String`

      The error that caused the session to fail, if any.

    - `last_active_at: Integer`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Hash[Symbol, String]`

      Custom string key-value pairs attached to the session.

    - `object: :"agent.session"`

      The object type. Always `agent.session`.

      - `:"agent.session"`

    - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

          The information needed to render the request.

          - `class BrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: String`

              The registered form or frame origin where values will be entered.

            - `fields: Array[Field{ id, label, required, type}]`

              Controls to render. All submitted values are sensitive.

              - `id: String`

                The field ID to submit as field_id in a fields entry.

              - `label: String`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: String`

                The rendering type, such as email, password, or text.

            - `options: Array[Option{ id, field_ids, label}]`

              Sign-in methods. Empty for a plain form.

              - `id: String`

                The option ID to submit as selected_option.

              - `field_ids: Array[String]`

                IDs from the registered fields that this method accepts.

              - `label: String`

                The method label to display.

            - `reason: String`

              Why the agent needs the user to sign in.

            - `type: :browser_authentication`

              The type of the object. Always `browser_authentication`.

              - `:browser_authentication`

          - `class BrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: String`

              The origin the browser needs permission to access.

            - `reason: String`

              The browser's explanation for this request, or null when unavailable.

            - `type: :browser_origin_access`

              The type of the object. Always `browser_origin_access`.

              - `:browser_origin_access`

        - `request_id: String`

          The registered request ID to echo when responding.

        - `turn_id: String`

          The turn that requested approval.

        - `type: :computer_use_approval_request`

          The type of the object. Always `computer_use_approval_request`.

          - `:computer_use_approval_request`

      - `class FunctionCall`

        Run a function tool and submit its result.

        - `arguments: untyped`

          The arguments supplied by the model.

        - `call_id: String`

          The ID to include when submitting the function result.

        - `name: String`

          The function name.

        - `turn_id: String`

          The ID of the turn that requested the function call.

        - `type: :function_call`

          The type of the object. Always `function_call`.

          - `:function_call`

      - `class EnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: String`

          The ID of the environment to reconnect.

        - `type: :environment_connection`

          The type of the object. Always `environment_connection`.

          - `:environment_connection`

    - `status: :idle | :in_progress | :requires_action | :failed`

      The current status of the session.

      - `:idle`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `:in_progress`

        The session is processing a turn.

      - `:requires_action`

        The session is waiting for one or more required actions.

      - `:failed`

        The session failed.

    - `usage: TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array[String]`

      The IDs of vaults made available to the session.

  - `type: :"agent.session.idle"`

    The type of the object. Always `agent.session.idle`.

    - `:"agent.session.idle"`

### Agent Session In Progress Event

- `class AgentSessionInProgressEvent`

  Emitted when a session starts processing a turn.

  - `event_id: String`

    The unique ID of the event.

  - `session: AgentSession`

    The session that started processing.

    - `id: String`

      The ID of the session.

    - `agent: Agent{ id, instructions, model, 6 more}`

      The agent running in the session.

      - `id: String`

        The ID of the agent.

      - `instructions: String`

        Custom instructions appended to the agent's default base instructions.

      - `model: String`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Integer`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: String`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: :none | :minimal | :low | 4 more`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

          - `:max`

        - `summary: :concise | :detailed | :auto`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `:concise`

            Returns a concise reasoning summary when supported.

          - `:detailed`

            Returns a detailed reasoning summary when supported.

          - `:auto`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: :auto | :default | :flex | 3 more`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `:auto`

        - `:default`

        - `:flex`

        - `:priority`

        - `:fast`

        - `:ultrafast`

      - `text: AgentText`

        Configuration for text generated by the agent.

        - `format_: TextFormat`

          The effective output format. Defaults to ordinary text.

          - `class Text`

            Generates ordinary text without a structured-output constraint.

            - `type: :text`

              The type of the object. Always `text`.

              - `:text`

          - `class JSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Hash[Symbol, untyped]`

              The JSON Schema that generated text must match.

            - `type: :json_schema`

              The type of the object. Always `json_schema`.

              - `:json_schema`

        - `verbosity: :low | :medium | :high`

          The amount of text produced by the agent. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

      - `tools: Array[AgentTool]`

        Tools available to the agent.

        - `class Function`

          A function defined by the application.

          - `defer_loading: bool`

            Whether the function is deferred and discovered through tool search.

          - `description: String`

            A description of what the function does.

          - `name: String`

            The name of the function.

          - `parameters: Hash[Symbol, untyped]`

            A JSON Schema object describing the function's arguments.

          - `type: :function`

            The type of the object. Always `function`.

            - `:function`

        - `class ProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: :programmatic_tool_calling`

            The type of the object. Always `programmatic_tool_calling`.

            - `:programmatic_tool_calling`

        - `class Mcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array[String]`

            The MCP tools the agent may call.

          - `connection_origin: :service | :environment`

            Where outbound MCP HTTP connections originate.

            - `:service`

            - `:environment`

          - `credential_id: String`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Hash[Symbol, untyped]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: String`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class HTTP`

              Connects to an MCP server over HTTP.

              - `server_url: String`

                The URL of the MCP server.

              - `type: :http`

                The type of the object. Always `http`.

                - `:http`

            - `class Stdio`

              Starts an MCP server as a local process.

              - `args: Array[String]`

                Arguments passed to the MCP server command.

              - `command: String`

                The command used to start the MCP server.

              - `cwd: String`

                The working directory used to start the MCP server.

              - `env_vars: Array[String]`

                Environment variable names inherited from the execution environment.

              - `type: :stdio`

                The type of the object. Always `stdio`.

                - `:stdio`

          - `type: :mcp`

            The type of the object. Always `mcp`.

            - `:mcp`

        - `class WebSearch`

          Web search.

          - `allowed_domains: Array[String]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: :low | :medium | :high`

            The amount of search context made available to the model. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

          - `location: Location{ city, country, region, timezone}`

            Approximate location used to localize search results, if provided.

            - `city: String`

              The city name.

            - `country: String`

              The two-letter ISO country code, such as `US`.

            - `region: String`

              The region or state name.

            - `timezone: String`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: :disabled | :cached | :live`

            The source used for web search results.

            - `:disabled`

            - `:cached`

            - `:live`

          - `type: :web_search`

            The type of the object. Always `web_search`.

            - `:web_search`

        - `class ComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: :computer_use`

            The type of the object. Always `computer_use`.

            - `:computer_use`

    - `created_at: Integer`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class None`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: :none`

          The type of the object. Always `none`.

          - `:none`

      - `class OpenAIHosted`

        An environment hosted by OpenAI.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop{ enabled}`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `file_id: String`

              The ID of the uploaded file.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :file_id`

              The type of the object. Always `file_id`.

              - `:file_id`

          - `class Inline`

            A file supplied inline when the session was created.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `network: Network{ access, allowed_domains}`

          The effective network access policy for the environment.

          - `access: :enabled | :disabled | :restricted`

            The environment's network access mode.

            - `:enabled`

              Allows unrestricted network access.

            - `:disabled`

              Disables network access.

            - `:restricted`

              Applies the configured domain restrictions.

          - `allowed_domains: Array[String]`

            Domains the environment may access when network access is restricted.

        - `packages: Packages{ npm, python, system_}`

          Packages installed in the environment.

          - `npm: Array[String]`

            npm packages installed globally in the environment.

          - `python: Array[String]`

            Python packages installed in the environment.

          - `system_: Array[String]`

            System packages installed in the environment.

        - `plugins: Array[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: String`

            The installed plugin description.

          - `name: String`

            The installed plugin name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

        - `skills: Array[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference`

            A skill installed from the Skills API.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `skill_id: String`

              The referenced skill ID.

            - `type: :skill_reference`

              The type of the object. Always `skill_reference`.

              - `:skill_reference`

            - `version: String`

              The concrete skill version installed for this session.

          - `class Inline`

            A skill installed from an inline ZIP archive.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `type: :openai_hosted`

          The type of the object. Always `openai_hosted`.

          - `:openai_hosted`

        - `container_size: :small | :medium | :large`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `:small`

          - `:medium`

          - `:large`

      - `class SelfHosted`

        An environment hosted by the application.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: String`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: :self_hosted`

          The type of the object. Always `self_hosted`.

          - `:self_hosted`

        - `workspace_directory: String`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: String`

      The error that caused the session to fail, if any.

    - `last_active_at: Integer`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Hash[Symbol, String]`

      Custom string key-value pairs attached to the session.

    - `object: :"agent.session"`

      The object type. Always `agent.session`.

      - `:"agent.session"`

    - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

          The information needed to render the request.

          - `class BrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: String`

              The registered form or frame origin where values will be entered.

            - `fields: Array[Field{ id, label, required, type}]`

              Controls to render. All submitted values are sensitive.

              - `id: String`

                The field ID to submit as field_id in a fields entry.

              - `label: String`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: String`

                The rendering type, such as email, password, or text.

            - `options: Array[Option{ id, field_ids, label}]`

              Sign-in methods. Empty for a plain form.

              - `id: String`

                The option ID to submit as selected_option.

              - `field_ids: Array[String]`

                IDs from the registered fields that this method accepts.

              - `label: String`

                The method label to display.

            - `reason: String`

              Why the agent needs the user to sign in.

            - `type: :browser_authentication`

              The type of the object. Always `browser_authentication`.

              - `:browser_authentication`

          - `class BrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: String`

              The origin the browser needs permission to access.

            - `reason: String`

              The browser's explanation for this request, or null when unavailable.

            - `type: :browser_origin_access`

              The type of the object. Always `browser_origin_access`.

              - `:browser_origin_access`

        - `request_id: String`

          The registered request ID to echo when responding.

        - `turn_id: String`

          The turn that requested approval.

        - `type: :computer_use_approval_request`

          The type of the object. Always `computer_use_approval_request`.

          - `:computer_use_approval_request`

      - `class FunctionCall`

        Run a function tool and submit its result.

        - `arguments: untyped`

          The arguments supplied by the model.

        - `call_id: String`

          The ID to include when submitting the function result.

        - `name: String`

          The function name.

        - `turn_id: String`

          The ID of the turn that requested the function call.

        - `type: :function_call`

          The type of the object. Always `function_call`.

          - `:function_call`

      - `class EnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: String`

          The ID of the environment to reconnect.

        - `type: :environment_connection`

          The type of the object. Always `environment_connection`.

          - `:environment_connection`

    - `status: :idle | :in_progress | :requires_action | :failed`

      The current status of the session.

      - `:idle`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `:in_progress`

        The session is processing a turn.

      - `:requires_action`

        The session is waiting for one or more required actions.

      - `:failed`

        The session failed.

    - `usage: TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array[String]`

      The IDs of vaults made available to the session.

  - `type: :"agent.session.in_progress"`

    The type of the object. Always `agent.session.in_progress`.

    - `:"agent.session.in_progress"`

### Agent Session Input Message Param

- `class AgentSessionInputMessageParam`

  A user message submitted to a session.

  - `content: Array[InputContentParam]`

    The content of the message.

    - `class InputText`

      Text input to the model.

      - `text: String`

        The text sent to the model.

      - `type: :input_text`

        The type of the object. Always `input_text`.

        - `:input_text`

    - `class InputImage`

      Image input to the model.

      - `image_url: String`

        The URL of the image sent to the model.

      - `type: :input_image`

        The type of the object. Always `input_image`.

        - `:input_image`

  - `role: :user`

    The role of the message author. Always `user`.

    - `:user`

  - `type: :message`

    The type of the input item. Always `message`.

    - `:message`

### Agent Session Input Param

- `AgentSessionInputParam = AgentSessionInputComputerUseApprovalRequestResult{ request_id, response, type} | AgentSessionInputMessage{ input, type} | AgentSessionInputCancel{ type} | AgentSessionInputToolResult{ call_id, success, turn_id, 3 more}`

  Input submitted to an existing session.

  - `class AgentSessionInputComputerUseApprovalRequestResult`

    Responds to a pending Computer Use approval request.

    - `request_id: String`

      The registered request ID from the required action.

    - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam`

        - `action: :submit`

          - `:submit`

        - `fields: Array[Field{ field_id, value}]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: String`

            The field ID from the required action.

          - `value: String`

            The value to enter into the registered control.

        - `type: :browser_authentication`

          - `:browser_authentication`

        - `selected_option: String`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class AgentBrowserOriginAccessParam`

        - `decision: :approve | :deny | :cancel`

          Whether to allow, deny, or cancel the requested origin access.

          - `:approve`

            Allow the browser to access this origin.

          - `:deny`

            Deny access to this origin.

          - `:cancel`

            Dismiss this request without approving access.

        - `type: :browser_origin_access`

          - `:browser_origin_access`

    - `type: :"agent.session.input.computer_use_approval_request_result"`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `:"agent.session.input.computer_use_approval_request_result"`

  - `class AgentSessionInputMessage`

    Adds one or more user messages and starts a turn.

    - `input: Array[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: Array[InputContentParam]`

        The content of the message.

        - `class InputText`

          Text input to the model.

          - `text: String`

            The text sent to the model.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input to the model.

          - `image_url: String`

            The URL of the image sent to the model.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

      - `role: :user`

        The role of the message author. Always `user`.

        - `:user`

      - `type: :message`

        The type of the input item. Always `message`.

        - `:message`

    - `type: :"agent.session.input.message"`

      The type of the object. Always `agent.session.input.message`.

      - `:"agent.session.input.message"`

  - `class AgentSessionInputCancel`

    Cancels the session's active turn.

    - `type: :"agent.session.input.cancel"`

      The type of the object. Always `agent.session.input.cancel`.

      - `:"agent.session.input.cancel"`

  - `class AgentSessionInputToolResult`

    Submits the result of a function call.

    - `call_id: String`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: String`

      The ID of the turn that requested the function call.

    - `type: :"agent.session.input.tool_result"`

      The type of the object. Always `agent.session.input.tool_result`.

      - `:"agent.session.input.tool_result"`

    - `error: String`

      The error message when the call failed.

    - `output: AgentFunctionCallOutputParam`

      The function result when the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContentParam]`

        - `class InputText`

          Text input to the model.

        - `class InputImage`

          Image input to the model.

### Agent Session Item

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Agent Session Message

- `class AgentSessionMessage`

  A user or assistant message recorded in a session.

  - `id: String`

    The ID of this item, or null for legacy user messages whose ID was not recorded.

  - `content: Array[AgentSessionMessageContent]`

    The content of the message. User messages contain input text or images; assistant messages contain output text.

    - `class InputText`

      Text supplied by the user.

      - `text: String`

        The text supplied by the user.

      - `type: :input_text`

        The type of the object. Always `input_text`.

        - `:input_text`

    - `class InputImage`

      An image supplied by the user.

      - `image_url: String`

        The URL of the image supplied by the user, which may be a base64-encoded data URL.

      - `type: :input_image`

        The type of the object. Always `input_image`.

        - `:input_image`

    - `class OutputText`

      Text produced by the assistant.

      - `text: String`

        The text produced by the assistant.

      - `type: :output_text`

        The type of the object. Always `output_text`.

        - `:output_text`

  - `phase: :commentary | :final_answer`

    The phase of an assistant message. Null for user messages.

    - `:commentary`

      Commentary produced while the agent works.

    - `:final_answer`

      The agent's final answer.

  - `role: :user | :assistant`

    The role of the message author.

    - `:user`

    - `:assistant`

  - `status: AgentOutputItemStatus`

    The status of the message. User messages are always `completed`.

    - `:in_progress`

      The item is in progress.

    - `:completed`

      The item is complete.

    - `:incomplete`

      The item stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :message`

    The item type. Always `message`.

    - `:message`

### Agent Session Message Content

- `AgentSessionMessageContent = InputText{ text, type} | InputImage{ image_url, type} | OutputText{ text, type}`

  A content part in a session message.

  - `class InputText`

    Text supplied by the user.

    - `text: String`

      The text supplied by the user.

    - `type: :input_text`

      The type of the object. Always `input_text`.

      - `:input_text`

  - `class InputImage`

    An image supplied by the user.

    - `image_url: String`

      The URL of the image supplied by the user, which may be a base64-encoded data URL.

    - `type: :input_image`

      The type of the object. Always `input_image`.

      - `:input_image`

  - `class OutputText`

    Text produced by the assistant.

    - `text: String`

      The text produced by the assistant.

    - `type: :output_text`

      The type of the object. Always `output_text`.

      - `:output_text`

### Agent Session Requires Action Event

- `class AgentSessionRequiresActionEvent`

  Emitted when a session is waiting for one or more required actions.

  - `event_id: String`

    The unique ID of the event.

  - `session: AgentSession`

    The session and its current required actions.

    - `id: String`

      The ID of the session.

    - `agent: Agent{ id, instructions, model, 6 more}`

      The agent running in the session.

      - `id: String`

        The ID of the agent.

      - `instructions: String`

        Custom instructions appended to the agent's default base instructions.

      - `model: String`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: bool`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: Integer`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: String`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: :none | :minimal | :low | 4 more`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `:none`

          - `:minimal`

          - `:low`

          - `:medium`

          - `:high`

          - `:xhigh`

          - `:max`

        - `summary: :concise | :detailed | :auto`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `:concise`

            Returns a concise reasoning summary when supported.

          - `:detailed`

            Returns a detailed reasoning summary when supported.

          - `:auto`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: :auto | :default | :flex | 3 more`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `:auto`

        - `:default`

        - `:flex`

        - `:priority`

        - `:fast`

        - `:ultrafast`

      - `text: AgentText`

        Configuration for text generated by the agent.

        - `format_: TextFormat`

          The effective output format. Defaults to ordinary text.

          - `class Text`

            Generates ordinary text without a structured-output constraint.

            - `type: :text`

              The type of the object. Always `text`.

              - `:text`

          - `class JSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Hash[Symbol, untyped]`

              The JSON Schema that generated text must match.

            - `type: :json_schema`

              The type of the object. Always `json_schema`.

              - `:json_schema`

        - `verbosity: :low | :medium | :high`

          The amount of text produced by the agent. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

      - `tools: Array[AgentTool]`

        Tools available to the agent.

        - `class Function`

          A function defined by the application.

          - `defer_loading: bool`

            Whether the function is deferred and discovered through tool search.

          - `description: String`

            A description of what the function does.

          - `name: String`

            The name of the function.

          - `parameters: Hash[Symbol, untyped]`

            A JSON Schema object describing the function's arguments.

          - `type: :function`

            The type of the object. Always `function`.

            - `:function`

        - `class ProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: bool`

            Whether tools can be called from model-generated code.

          - `type: :programmatic_tool_calling`

            The type of the object. Always `programmatic_tool_calling`.

            - `:programmatic_tool_calling`

        - `class Mcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array[String]`

            The MCP tools the agent may call.

          - `connection_origin: :service | :environment`

            Where outbound MCP HTTP connections originate.

            - `:service`

            - `:environment`

          - `credential_id: String`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Hash[Symbol, untyped]`

            Metadata included with requests to this MCP server.

          - `required: bool`

            Whether this MCP server must initialize before the first turn.

          - `server_label: String`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `class HTTP`

              Connects to an MCP server over HTTP.

              - `server_url: String`

                The URL of the MCP server.

              - `type: :http`

                The type of the object. Always `http`.

                - `:http`

            - `class Stdio`

              Starts an MCP server as a local process.

              - `args: Array[String]`

                Arguments passed to the MCP server command.

              - `command: String`

                The command used to start the MCP server.

              - `cwd: String`

                The working directory used to start the MCP server.

              - `env_vars: Array[String]`

                Environment variable names inherited from the execution environment.

              - `type: :stdio`

                The type of the object. Always `stdio`.

                - `:stdio`

          - `type: :mcp`

            The type of the object. Always `mcp`.

            - `:mcp`

        - `class WebSearch`

          Web search.

          - `allowed_domains: Array[String]`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: :low | :medium | :high`

            The amount of search context made available to the model. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

          - `location: Location{ city, country, region, timezone}`

            Approximate location used to localize search results, if provided.

            - `city: String`

              The city name.

            - `country: String`

              The two-letter ISO country code, such as `US`.

            - `region: String`

              The region or state name.

            - `timezone: String`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: :disabled | :cached | :live`

            The source used for web search results.

            - `:disabled`

            - `:cached`

            - `:live`

          - `type: :web_search`

            The type of the object. Always `web_search`.

            - `:web_search`

        - `class ComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: bool`

            Whether computer tool outputs include screenshots.

          - `type: :computer_use`

            The type of the object. Always `computer_use`.

            - `:computer_use`

    - `created_at: Integer`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `class None`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: :none`

          The type of the object. Always `none`.

          - `:none`

      - `class OpenAIHosted`

        An environment hosted by OpenAI.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop{ enabled}`

          The effective desktop configuration.

          - `enabled: bool`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array[HostedEnvironmentFile]`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `file_id: String`

              The ID of the uploaded file.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :file_id`

              The type of the object. Always `file_id`.

              - `:file_id`

          - `class Inline`

            A file supplied inline when the session was created.

            - `id: String`

              The session-scoped ID of the file in the execution environment.

            - `path: String`

              The file's absolute path inside the environment.

            - `size_bytes: Integer`

              The decoded file size in bytes.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `network: Network{ access, allowed_domains}`

          The effective network access policy for the environment.

          - `access: :enabled | :disabled | :restricted`

            The environment's network access mode.

            - `:enabled`

              Allows unrestricted network access.

            - `:disabled`

              Disables network access.

            - `:restricted`

              Applies the configured domain restrictions.

          - `allowed_domains: Array[String]`

            Domains the environment may access when network access is restricted.

        - `packages: Packages{ npm, python, system_}`

          Packages installed in the environment.

          - `npm: Array[String]`

            npm packages installed globally in the environment.

          - `python: Array[String]`

            Python packages installed in the environment.

          - `system_: Array[String]`

            System packages installed in the environment.

        - `plugins: Array[HostedPlugin]`

          Plugins installed in the environment, excluding their archive contents.

          - `description: String`

            The installed plugin description.

          - `name: String`

            The installed plugin name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

        - `skills: Array[HostedSkill]`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference`

            A skill installed from the Skills API.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `skill_id: String`

              The referenced skill ID.

            - `type: :skill_reference`

              The type of the object. Always `skill_reference`.

              - `:skill_reference`

            - `version: String`

              The concrete skill version installed for this session.

          - `class Inline`

            A skill installed from an inline ZIP archive.

            - `description: String`

              The installed skill description.

            - `name: String`

              The installed skill name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

        - `type: :openai_hosted`

          The type of the object. Always `openai_hosted`.

          - `:openai_hosted`

        - `container_size: :small | :medium | :large`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `:small`

          - `:medium`

          - `:large`

      - `class SelfHosted`

        An environment hosted by the application.

        - `id: String`

          The public ID of the environment.

        - `capability_directories: Array[String]`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: String`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: :self_hosted`

          The type of the object. Always `self_hosted`.

          - `:self_hosted`

        - `workspace_directory: String`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: String`

      The error that caused the session to fail, if any.

    - `last_active_at: Integer`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Hash[Symbol, String]`

      Custom string key-value pairs attached to the session.

    - `object: :"agent.session"`

      The object type. Always `agent.session`.

      - `:"agent.session"`

    - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

          The information needed to render the request.

          - `class BrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: String`

              The registered form or frame origin where values will be entered.

            - `fields: Array[Field{ id, label, required, type}]`

              Controls to render. All submitted values are sensitive.

              - `id: String`

                The field ID to submit as field_id in a fields entry.

              - `label: String`

                The label to display beside the control.

              - `required: bool`

                Whether this control requires a nonempty value.

              - `type: String`

                The rendering type, such as email, password, or text.

            - `options: Array[Option{ id, field_ids, label}]`

              Sign-in methods. Empty for a plain form.

              - `id: String`

                The option ID to submit as selected_option.

              - `field_ids: Array[String]`

                IDs from the registered fields that this method accepts.

              - `label: String`

                The method label to display.

            - `reason: String`

              Why the agent needs the user to sign in.

            - `type: :browser_authentication`

              The type of the object. Always `browser_authentication`.

              - `:browser_authentication`

          - `class BrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: String`

              The origin the browser needs permission to access.

            - `reason: String`

              The browser's explanation for this request, or null when unavailable.

            - `type: :browser_origin_access`

              The type of the object. Always `browser_origin_access`.

              - `:browser_origin_access`

        - `request_id: String`

          The registered request ID to echo when responding.

        - `turn_id: String`

          The turn that requested approval.

        - `type: :computer_use_approval_request`

          The type of the object. Always `computer_use_approval_request`.

          - `:computer_use_approval_request`

      - `class FunctionCall`

        Run a function tool and submit its result.

        - `arguments: untyped`

          The arguments supplied by the model.

        - `call_id: String`

          The ID to include when submitting the function result.

        - `name: String`

          The function name.

        - `turn_id: String`

          The ID of the turn that requested the function call.

        - `type: :function_call`

          The type of the object. Always `function_call`.

          - `:function_call`

      - `class EnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: String`

          The ID of the environment to reconnect.

        - `type: :environment_connection`

          The type of the object. Always `environment_connection`.

          - `:environment_connection`

    - `status: :idle | :in_progress | :requires_action | :failed`

      The current status of the session.

      - `:idle`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `:in_progress`

        The session is processing a turn.

      - `:requires_action`

        The session is waiting for one or more required actions.

      - `:failed`

        The session failed.

    - `usage: TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array[String]`

      The IDs of vaults made available to the session.

  - `type: :"agent.session.requires_action"`

    The type of the object. Always `agent.session.requires_action`.

    - `:"agent.session.requires_action"`

### Agent Session Subagent Active Event

- `class AgentSessionSubagentActiveEvent`

  Emitted when a closed subagent successfully resumes.

  - `event_id: String`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that resumed.

    - `id: String`

      The ID of the subagent.

    - `closed_at: Integer`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array[AgentContent]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `name: String`

      The runner-assigned nickname, or null when unavailable.

    - `object: :"agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `:"agent.session.subagent"`

    - `opened_at: Integer`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: String`

      The ID of the agent that created this subagent.

    - `session_id: String`

      The ID of the session that owns the subagent.

    - `status: :active | :closed`

      The current status of the subagent.

      - `:active`

        The subagent remains available, including while idle between turns.

      - `:closed`

        The subagent is closed.

  - `type: :"agent.session.subagent.active"`

    The type of the object. Always `agent.session.subagent.active`.

    - `:"agent.session.subagent.active"`

### Agent Session Subagent Closed Event

- `class AgentSessionSubagentClosedEvent`

  Emitted when a subagent is closed.

  - `event_id: String`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was closed.

    - `id: String`

      The ID of the subagent.

    - `closed_at: Integer`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array[AgentContent]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `name: String`

      The runner-assigned nickname, or null when unavailable.

    - `object: :"agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `:"agent.session.subagent"`

    - `opened_at: Integer`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: String`

      The ID of the agent that created this subagent.

    - `session_id: String`

      The ID of the session that owns the subagent.

    - `status: :active | :closed`

      The current status of the subagent.

      - `:active`

        The subagent remains available, including while idle between turns.

      - `:closed`

        The subagent is closed.

  - `type: :"agent.session.subagent.closed"`

    The type of the object. Always `agent.session.subagent.closed`.

    - `:"agent.session.subagent.closed"`

### Agent Session Subagent Created Event

- `class AgentSessionSubagentCreatedEvent`

  Emitted when a subagent is created.

  - `event_id: String`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was created.

    - `id: String`

      The ID of the subagent.

    - `closed_at: Integer`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array[AgentContent]`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `name: String`

      The runner-assigned nickname, or null when unavailable.

    - `object: :"agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `:"agent.session.subagent"`

    - `opened_at: Integer`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: String`

      The ID of the agent that created this subagent.

    - `session_id: String`

      The ID of the session that owns the subagent.

    - `status: :active | :closed`

      The current status of the subagent.

      - `:active`

        The subagent remains available, including while idle between turns.

      - `:closed`

        The subagent is closed.

  - `type: :"agent.session.subagent.created"`

    The type of the object. Always `agent.session.subagent.created`.

    - `:"agent.session.subagent.created"`

### Agent Session Turn Cancelled Event

- `class AgentSessionTurnCancelledEvent`

  Emitted when a turn is cancelled.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn: Turn`

    The cancelled turn.

    - `id: String`

      The ID of the turn.

    - `agent_id: String`

      The ID of the agent that ran the turn.

    - `completed_at: Integer`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: Integer`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

        A stable, machine-readable failure category.

        - `:context_length_exceeded`

          The request exceeds the model's context window.

        - `:session_budget_exceeded`

          The session has reached its usage budget.

        - `:usage_limit_exceeded`

          The organization has reached a usage, plan, or billing limit.

        - `:credit_balance_exhausted`

          The organization has no API credits remaining.

        - `:rate_limit_exceeded`

          The request exceeds the available rate limit.

        - `:flex_unavailable`

          Flex processing is temporarily unavailable.

        - `:server_overloaded`

          The model service is temporarily overloaded.

        - `:cyber_policy`

          The request was rejected by a safety policy.

        - `:misalignment_policy_violation`

          The request was blocked by the safety systems.

        - `:connection_failed`

          The request could not connect to the model service.

        - `:server_error`

          The model service encountered an unexpected error.

        - `:authentication_error`

          The API credentials are invalid or lack the required access.

        - `:invalid_request`

          The request contains invalid input or configuration.

        - `:resource_not_found`

          The requested model or resource is unavailable.

        - `:sandbox_error`

          The request could not complete in its execution environment.

        - `:executor_version_incompatible`

          The executor must be upgraded before it can run this turn.

        - `:active_turn_not_steerable`

          The session cannot accept additional input while a request is running.

        - `:request_timeout`

          The request timed out before the model service responded.

        - `:internal_error`

          An unexpected internal error prevented the session request from completing.

      - `message: String`

        A customer-safe explanation of the failure.

    - `object: :"agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `:"agent.session.turn"`

    - `session_id: String`

      The ID of the session that owns the turn.

    - `started_at: Integer`

      The Unix timestamp, in seconds, when the turn started.

    - `status: :queued | :in_progress | :waiting | 3 more`

      The current status of the turn.

      - `:queued`

        The turn is waiting to start.

      - `:in_progress`

        The turn is in progress.

      - `:waiting`

        The turn is waiting for external input.

      - `:completed`

        The turn completed successfully.

      - `:failed`

        The turn failed.

      - `:cancelled`

        The turn was cancelled.

    - `subagent_id: String`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

  - `turn_id: String`

    The ID of the turn associated with the event.

  - `type: :"agent.session.turn.cancelled"`

    The type of the object. Always `agent.session.turn.cancelled`.

    - `:"agent.session.turn.cancelled"`

  - `usage: TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Completed Event

- `class AgentSessionTurnCompletedEvent`

  Emitted when a turn completes.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn: Turn`

    The completed turn.

    - `id: String`

      The ID of the turn.

    - `agent_id: String`

      The ID of the agent that ran the turn.

    - `completed_at: Integer`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: Integer`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

        A stable, machine-readable failure category.

        - `:context_length_exceeded`

          The request exceeds the model's context window.

        - `:session_budget_exceeded`

          The session has reached its usage budget.

        - `:usage_limit_exceeded`

          The organization has reached a usage, plan, or billing limit.

        - `:credit_balance_exhausted`

          The organization has no API credits remaining.

        - `:rate_limit_exceeded`

          The request exceeds the available rate limit.

        - `:flex_unavailable`

          Flex processing is temporarily unavailable.

        - `:server_overloaded`

          The model service is temporarily overloaded.

        - `:cyber_policy`

          The request was rejected by a safety policy.

        - `:misalignment_policy_violation`

          The request was blocked by the safety systems.

        - `:connection_failed`

          The request could not connect to the model service.

        - `:server_error`

          The model service encountered an unexpected error.

        - `:authentication_error`

          The API credentials are invalid or lack the required access.

        - `:invalid_request`

          The request contains invalid input or configuration.

        - `:resource_not_found`

          The requested model or resource is unavailable.

        - `:sandbox_error`

          The request could not complete in its execution environment.

        - `:executor_version_incompatible`

          The executor must be upgraded before it can run this turn.

        - `:active_turn_not_steerable`

          The session cannot accept additional input while a request is running.

        - `:request_timeout`

          The request timed out before the model service responded.

        - `:internal_error`

          An unexpected internal error prevented the session request from completing.

      - `message: String`

        A customer-safe explanation of the failure.

    - `object: :"agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `:"agent.session.turn"`

    - `session_id: String`

      The ID of the session that owns the turn.

    - `started_at: Integer`

      The Unix timestamp, in seconds, when the turn started.

    - `status: :queued | :in_progress | :waiting | 3 more`

      The current status of the turn.

      - `:queued`

        The turn is waiting to start.

      - `:in_progress`

        The turn is in progress.

      - `:waiting`

        The turn is waiting for external input.

      - `:completed`

        The turn completed successfully.

      - `:failed`

        The turn failed.

      - `:cancelled`

        The turn was cancelled.

    - `subagent_id: String`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

  - `turn_id: String`

    The ID of the turn associated with the event.

  - `type: :"agent.session.turn.completed"`

    The type of the object. Always `agent.session.turn.completed`.

    - `:"agent.session.turn.completed"`

  - `usage: TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Content Part Added Event

- `class AgentSessionTurnContentPartAddedEvent`

  Emitted when an output text content part is added.

  - `content_index: Integer`

    The index of the content part in the message.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the message item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `part: OutputText`

    The initial content part.

    - `text: String`

      The text produced by the agent.

    - `type: :output_text`

      The content type. Always `output_text`.

      - `:output_text`

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.content_part.added"`

    The type of the object. Always `agent.session.turn.content_part.added`.

    - `:"agent.session.turn.content_part.added"`

### Agent Session Turn Content Part Done Event

- `class AgentSessionTurnContentPartDoneEvent`

  Emitted when an output content part is complete.

  - `content_index: Integer`

    The index of the content part in the message.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the message item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `part: OutputText`

    The completed content part.

    - `text: String`

      The text produced by the agent.

    - `type: :output_text`

      The content type. Always `output_text`.

      - `:output_text`

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.content_part.done"`

    The type of the object. Always `agent.session.turn.content_part.done`.

    - `:"agent.session.turn.content_part.done"`

### Agent Session Turn Created Event

- `class AgentSessionTurnCreatedEvent`

  Emitted when a turn is created.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it was created.

    - `id: String`

      The ID of the turn.

    - `agent_id: String`

      The ID of the agent that ran the turn.

    - `completed_at: Integer`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: Integer`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

        A stable, machine-readable failure category.

        - `:context_length_exceeded`

          The request exceeds the model's context window.

        - `:session_budget_exceeded`

          The session has reached its usage budget.

        - `:usage_limit_exceeded`

          The organization has reached a usage, plan, or billing limit.

        - `:credit_balance_exhausted`

          The organization has no API credits remaining.

        - `:rate_limit_exceeded`

          The request exceeds the available rate limit.

        - `:flex_unavailable`

          Flex processing is temporarily unavailable.

        - `:server_overloaded`

          The model service is temporarily overloaded.

        - `:cyber_policy`

          The request was rejected by a safety policy.

        - `:misalignment_policy_violation`

          The request was blocked by the safety systems.

        - `:connection_failed`

          The request could not connect to the model service.

        - `:server_error`

          The model service encountered an unexpected error.

        - `:authentication_error`

          The API credentials are invalid or lack the required access.

        - `:invalid_request`

          The request contains invalid input or configuration.

        - `:resource_not_found`

          The requested model or resource is unavailable.

        - `:sandbox_error`

          The request could not complete in its execution environment.

        - `:executor_version_incompatible`

          The executor must be upgraded before it can run this turn.

        - `:active_turn_not_steerable`

          The session cannot accept additional input while a request is running.

        - `:request_timeout`

          The request timed out before the model service responded.

        - `:internal_error`

          An unexpected internal error prevented the session request from completing.

      - `message: String`

        A customer-safe explanation of the failure.

    - `object: :"agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `:"agent.session.turn"`

    - `session_id: String`

      The ID of the session that owns the turn.

    - `started_at: Integer`

      The Unix timestamp, in seconds, when the turn started.

    - `status: :queued | :in_progress | :waiting | 3 more`

      The current status of the turn.

      - `:queued`

        The turn is waiting to start.

      - `:in_progress`

        The turn is in progress.

      - `:waiting`

        The turn is waiting for external input.

      - `:completed`

        The turn completed successfully.

      - `:failed`

        The turn failed.

      - `:cancelled`

        The turn was cancelled.

    - `subagent_id: String`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

  - `turn_id: String`

    The ID of the turn associated with the event.

  - `type: :"agent.session.turn.created"`

    The type of the object. Always `agent.session.turn.created`.

    - `:"agent.session.turn.created"`

### Agent Session Turn Failed Event

- `class AgentSessionTurnFailedEvent`

  Emitted when a turn fails.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn: Turn`

    The failed turn.

    - `id: String`

      The ID of the turn.

    - `agent_id: String`

      The ID of the agent that ran the turn.

    - `completed_at: Integer`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: Integer`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

        A stable, machine-readable failure category.

        - `:context_length_exceeded`

          The request exceeds the model's context window.

        - `:session_budget_exceeded`

          The session has reached its usage budget.

        - `:usage_limit_exceeded`

          The organization has reached a usage, plan, or billing limit.

        - `:credit_balance_exhausted`

          The organization has no API credits remaining.

        - `:rate_limit_exceeded`

          The request exceeds the available rate limit.

        - `:flex_unavailable`

          Flex processing is temporarily unavailable.

        - `:server_overloaded`

          The model service is temporarily overloaded.

        - `:cyber_policy`

          The request was rejected by a safety policy.

        - `:misalignment_policy_violation`

          The request was blocked by the safety systems.

        - `:connection_failed`

          The request could not connect to the model service.

        - `:server_error`

          The model service encountered an unexpected error.

        - `:authentication_error`

          The API credentials are invalid or lack the required access.

        - `:invalid_request`

          The request contains invalid input or configuration.

        - `:resource_not_found`

          The requested model or resource is unavailable.

        - `:sandbox_error`

          The request could not complete in its execution environment.

        - `:executor_version_incompatible`

          The executor must be upgraded before it can run this turn.

        - `:active_turn_not_steerable`

          The session cannot accept additional input while a request is running.

        - `:request_timeout`

          The request timed out before the model service responded.

        - `:internal_error`

          An unexpected internal error prevented the session request from completing.

      - `message: String`

        A customer-safe explanation of the failure.

    - `object: :"agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `:"agent.session.turn"`

    - `session_id: String`

      The ID of the session that owns the turn.

    - `started_at: Integer`

      The Unix timestamp, in seconds, when the turn started.

    - `status: :queued | :in_progress | :waiting | 3 more`

      The current status of the turn.

      - `:queued`

        The turn is waiting to start.

      - `:in_progress`

        The turn is in progress.

      - `:waiting`

        The turn is waiting for external input.

      - `:completed`

        The turn completed successfully.

      - `:failed`

        The turn failed.

      - `:cancelled`

        The turn was cancelled.

    - `subagent_id: String`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

  - `turn_id: String`

    The ID of the turn associated with the event.

  - `type: :"agent.session.turn.failed"`

    The type of the object. Always `agent.session.turn.failed`.

    - `:"agent.session.turn.failed"`

  - `usage: TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn In Progress Event

- `class AgentSessionTurnInProgressEvent`

  Emitted when a turn starts running.

  - `event_id: String`

    The unique ID of the event.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it started running.

    - `id: String`

      The ID of the turn.

    - `agent_id: String`

      The ID of the agent that ran the turn.

    - `completed_at: Integer`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: Integer`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

        A stable, machine-readable failure category.

        - `:context_length_exceeded`

          The request exceeds the model's context window.

        - `:session_budget_exceeded`

          The session has reached its usage budget.

        - `:usage_limit_exceeded`

          The organization has reached a usage, plan, or billing limit.

        - `:credit_balance_exhausted`

          The organization has no API credits remaining.

        - `:rate_limit_exceeded`

          The request exceeds the available rate limit.

        - `:flex_unavailable`

          Flex processing is temporarily unavailable.

        - `:server_overloaded`

          The model service is temporarily overloaded.

        - `:cyber_policy`

          The request was rejected by a safety policy.

        - `:misalignment_policy_violation`

          The request was blocked by the safety systems.

        - `:connection_failed`

          The request could not connect to the model service.

        - `:server_error`

          The model service encountered an unexpected error.

        - `:authentication_error`

          The API credentials are invalid or lack the required access.

        - `:invalid_request`

          The request contains invalid input or configuration.

        - `:resource_not_found`

          The requested model or resource is unavailable.

        - `:sandbox_error`

          The request could not complete in its execution environment.

        - `:executor_version_incompatible`

          The executor must be upgraded before it can run this turn.

        - `:active_turn_not_steerable`

          The session cannot accept additional input while a request is running.

        - `:request_timeout`

          The request timed out before the model service responded.

        - `:internal_error`

          An unexpected internal error prevented the session request from completing.

      - `message: String`

        A customer-safe explanation of the failure.

    - `object: :"agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `:"agent.session.turn"`

    - `session_id: String`

      The ID of the session that owns the turn.

    - `started_at: Integer`

      The Unix timestamp, in seconds, when the turn started.

    - `status: :queued | :in_progress | :waiting | 3 more`

      The current status of the turn.

      - `:queued`

        The turn is waiting to start.

      - `:in_progress`

        The turn is in progress.

      - `:waiting`

        The turn is waiting for external input.

      - `:completed`

        The turn completed successfully.

      - `:failed`

        The turn failed.

      - `:cancelled`

        The turn was cancelled.

    - `subagent_id: String`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: Integer`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails{ cached_tokens}`

        A breakdown of the agent's input token usage.

        - `cached_tokens: Integer`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: Integer`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: Integer`

          The number of output tokens used for reasoning.

      - `total_tokens: Integer`

        The total number of input and output tokens used by the agent.

  - `turn_id: String`

    The ID of the turn associated with the event.

  - `type: :"agent.session.turn.in_progress"`

    The type of the object. Always `agent.session.turn.in_progress`.

    - `:"agent.session.turn.in_progress"`

### Agent Session Turn Item Added Event

- `class AgentSessionTurnItemAddedEvent`

  Emitted when an item is added to a turn.

  - `event_id: String`

    The unique ID of the event.

  - `item: AgentSessionItem`

    The item that was added.

    - `class AgentSessionMessage`

      A user or assistant message recorded in a session.

      - `id: String`

        The ID of this item, or null for legacy user messages whose ID was not recorded.

      - `content: Array[AgentSessionMessageContent]`

        The content of the message. User messages contain input text or images; assistant messages contain output text.

        - `class InputText`

          Text supplied by the user.

          - `text: String`

            The text supplied by the user.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          An image supplied by the user.

          - `image_url: String`

            The URL of the image supplied by the user, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

        - `class OutputText`

          Text produced by the assistant.

          - `text: String`

            The text produced by the assistant.

          - `type: :output_text`

            The type of the object. Always `output_text`.

            - `:output_text`

      - `phase: :commentary | :final_answer`

        The phase of an assistant message. Null for user messages.

        - `:commentary`

          Commentary produced while the agent works.

        - `:final_answer`

          The agent's final answer.

      - `role: :user | :assistant`

        The role of the message author.

        - `:user`

        - `:assistant`

      - `status: AgentOutputItemStatus`

        The status of the message. User messages are always `completed`.

        - `:in_progress`

          The item is in progress.

        - `:completed`

          The item is complete.

        - `:incomplete`

          The item stopped before completing.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :message`

        The item type. Always `message`.

        - `:message`

    - `class AgentReasoningItem`

      A reasoning item produced by the agent.

      - `id: String`

        The ID of the reasoning item.

      - `status: AgentOutputItemStatus`

        The status of the reasoning item.

      - `summary: Array[SummaryText]`

        The reasoning summaries produced by the agent.

        - `text: String`

          The reasoning summary text.

        - `type: :summary_text`

          The content type. Always `summary_text`.

          - `:summary_text`

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :reasoning`

        The item type. Always `reasoning`.

        - `:reasoning`

    - `class AgentFunctionCallItem`

      A function call produced by the agent.

      - `id: String`

        The ID of the function call item.

      - `arguments: untyped`

        The arguments to pass to the function.

      - `call_id: String`

        The ID used to submit the function result.

      - `name: String`

        The name of the function to call.

      - `status: AgentFunctionCallStatus`

        The status of the function call.

        - `:in_progress`

          The call is in progress.

        - `:completed`

          The call completed successfully.

        - `:failed`

          The call failed.

        - `:incomplete`

          The call stopped before completing.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :function_call`

        The item type. Always `function_call`.

        - `:function_call`

    - `class FunctionCallOutput`

      The result supplied for a function call.

      - `id: String`

        The ID of the function call output item.

      - `call_id: String`

        The ID of the function call that produced this output.

      - `error: String`

        The error message, if the call failed.

      - `output: AgentFunctionCallOutput`

        The function result, if the call succeeded.

        - `String = String`

        - `UnionMember1 = Array[InputContent]`

          - `class InputText`

            Text input recorded in a session item.

            - `text: String`

              The text supplied to the agent.

            - `type: :input_text`

              The type of the object. Always `input_text`.

              - `:input_text`

          - `class InputImage`

            Image input recorded in a session item.

            - `image_url: String`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            - `type: :input_image`

              The type of the object. Always `input_image`.

              - `:input_image`

      - `status: AgentFunctionCallStatus`

        The status of the function call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :function_call_output`

        The item type. Always `function_call_output`.

        - `:function_call_output`

    - `class AgentMessage`

      A message exchanged between agent threads.

      - `id: String`

        The ID of the message.

      - `content: Array[AgentContent]`

        The content exchanged between the agents.

        - `class OutputText`

          A text content part produced by the agent.

          - `text: String`

            The text produced by the agent.

          - `type: :output_text`

            The content type. Always `output_text`.

            - `:output_text`

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

          - `encrypted_content: String`

            The encrypted content payload.

          - `type: :encrypted_content`

            The content type. Always `encrypted_content`.

            - `:encrypted_content`

      - `recipient_agent_id: String`

        The ID or name of the receiving agent.

      - `sender_agent_id: String`

        The ID or name of the sending agent.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :agent_message`

        The item type. Always `agent_message`.

        - `:agent_message`

    - `class AgentMcpCallItem`

      A call to a tool on an MCP server.

      - `id: String`

        The ID of the MCP call item.

      - `arguments: untyped`

        The arguments passed to the MCP tool.

      - `error: untyped`

        The error returned by the MCP tool, if any.

      - `name: String`

        The name of the MCP tool.

      - `output: untyped`

        The output returned by the MCP tool, if any.

      - `server_label: String`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :mcp_call`

        The item type. Always `mcp_call`.

        - `:mcp_call`

    - `class ComputerUseCall`

      One execution of the platform-provided computer-use capability.

      - `id: String`

        The ID of the activity item.

      - `output: Output{ image_url, type}`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: String`

          The complete JPEG image as a base64 data URL.

        - `type: :computer_screenshot`

          The content type. Always `computer_screenshot`.

          - `:computer_screenshot`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: String`

        A model-generated description of the activity, when available.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :computer_use_call`

        The item type. Always `computer_use_call`.

        - `:computer_use_call`

    - `class ComputerUseApprovalRequest`

      A credential-free history record of the emitted login request.

      - `id: String`

        The stable history item ID.

      - `request: Request{ credential_origin, fields, options, 2 more}`

        A registered form awaiting the application's response.

        - `credential_origin: String`

          The registered form or frame origin where values will be entered.

        - `fields: Array[Field{ id, label, required, type}]`

          Controls to render. All submitted values are sensitive.

          - `id: String`

            The field ID to submit as field_id in a fields entry.

          - `label: String`

            The label to display beside the control.

          - `required: bool`

            Whether this control requires a nonempty value.

          - `type: String`

            The rendering type, such as email, password, or text.

        - `options: Array[Option{ id, field_ids, label}]`

          Sign-in methods. Empty for a plain form.

          - `id: String`

            The option ID to submit as selected_option.

          - `field_ids: Array[String]`

            IDs from the registered fields that this method accepts.

          - `label: String`

            The method label to display.

        - `reason: String`

          Why the agent needs the user to sign in.

        - `type: :browser_authentication`

          The type of the object. Always `browser_authentication`.

          - `:browser_authentication`

      - `request_id: String`

      - `turn_id: String`

      - `type: :computer_use_approval_request`

        The item type. Always computer_use_approval_request.

        - `:computer_use_approval_request`

    - `class ComputerUseApprovalRequestResult`

      A credential-free record of an admitted response, not proof of completion.

      - `id: String`

        The stable history item ID.

      - `request_id: String`

        The registered request answered by this item.

      - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

        The admitted response, without submitted credential values.

        - `class Submit`

          - `action: :submit`

            - `:submit`

          - `selected_option: String`

            The chosen sign-in method, or null when no options were offered.

          - `type: :browser_authentication`

            - `:browser_authentication`

        - `class Cancel`

          - `action: :cancel`

            - `:cancel`

          - `type: :browser_authentication`

            - `:browser_authentication`

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :computer_use_approval_request_result`

        - `:computer_use_approval_request_result`

    - `class AgentWebSearchCallItem`

      A web search call produced by the agent.

      - `id: String`

        The ID of the web search call.

      - `action: WebSearchAction`

        The action performed by the web search tool.

        - `class Search`

          A search query or group of search queries.

          - `queries: Array[String]`

            The search queries, when multiple queries were used.

          - `query: String`

            The search query, when a single query was used.

          - `type: :search`

            The type of the object. Always `search`.

            - `:search`

        - `class OpenPage`

          Opens a web page.

          - `type: :open_page`

            The type of the object. Always `open_page`.

            - `:open_page`

          - `url: String`

            The URL of the page that was opened.

        - `class FindInPage`

          Finds text within a web page.

          - `pattern: String`

            The text pattern that was searched for.

          - `type: :find_in_page`

            The type of the object. Always `find_in_page`.

            - `:find_in_page`

          - `url: String`

            The URL of the page that was searched.

        - `class Other`

          Another web search action.

          - `type: :other`

            The type of the object. Always `other`.

            - `:other`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :web_search_call`

        The item type. Always `web_search_call`.

        - `:web_search_call`

    - `class AgentCommandExecutionItem`

      A command execution produced by the agent.

      - `id: String`

        The ID of the command execution item.

      - `command: String`

        The command that was executed.

      - `cwd: String`

        The working directory used to execute the command.

      - `duration_ms: Integer`

        The command duration in milliseconds.

      - `exit_code: Integer`

        The process exit code, if the command completed.

      - `output: String`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :command_execution`

        The item type. Always `command_execution`.

        - `:command_execution`

    - `class AgentCreateSubagentCallItem`

      A request to spawn a subagent.

      - `id: String`

        The ID of the tool call item.

      - `agent_id: String`

        The ID of the agent that requested the subagent.

      - `content: Array[AgentContent]`

        The task given to the spawned agent.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `model: String`

        The model requested for the spawned agent.

      - `reasoning_effort: String`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :create_subagent_call`

        The item type. Always `create_subagent_call`.

        - `:create_subagent_call`

          The current public item type.

    - `class AgentSendSubagentInputCallItem`

      A request to send input to another agent.

      - `id: String`

        The ID of the tool call item.

      - `content: Array[AgentContent]`

        The input sent to the receiving agent.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: String`

        The ID of the agent receiving the input.

      - `sender_agent_id: String`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :send_subagent_input_call`

        The item type. Always `send_subagent_input_call`.

        - `:send_subagent_input_call`

          The current public item type.

    - `class AgentResumeSubagentCallItem`

      A request to resume a subagent.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to resume.

      - `sender_agent_id: String`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :resume_subagent_call`

        The item type. Always `resume_subagent_call`.

        - `:resume_subagent_call`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem`

      A request to wait for one or more subagents.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_ids: Array[String]`

        The IDs of the agents to wait for.

      - `sender_agent_id: String`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :wait_for_subagents_call`

        The item type. Always `wait_for_subagents_call`.

        - `:wait_for_subagents_call`

          The current public item type.

    - `class AgentInterruptSubagentCallItem`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to interrupt.

      - `sender_agent_id: String`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :interrupt_subagent_call`

        The item type. Always `interrupt_subagent_call`.

        - `:interrupt_subagent_call`

          The current public item type.

    - `class AgentCloseSubagentCallItem`

      A request to close a subagent.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to close.

      - `sender_agent_id: String`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :close_subagent_call`

        The item type. Always `close_subagent_call`.

        - `:close_subagent_call`

          The current public item type.

  - `output_index: Integer`

    The index of the item in the turn output, when the item is agent output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.item.added"`

    The type of the object. Always `agent.session.turn.item.added`.

    - `:"agent.session.turn.item.added"`

### Agent Session Turn Item Done Event

- `class AgentSessionTurnItemDoneEvent`

  Emitted when an output item is complete.

  - `event_id: String`

    The unique ID of the event.

  - `item: AgentOutputItem`

    The completed output item.

    - `class AgentSessionAssistantMessage`

      An assistant message produced by the agent.

      - `id: String`

        The ID of the message.

      - `content: Array[OutputText]`

        The content of the message.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `phase: :commentary | :final_answer`

        The phase of the assistant message.

        - `:commentary`

          Commentary produced while the agent works.

        - `:final_answer`

          The agent's final answer.

      - `role: :assistant`

        The role of the message author. Always `assistant`.

        - `:assistant`

      - `status: AgentOutputItemStatus`

        The status of the message.

        - `:in_progress`

          The item is in progress.

        - `:completed`

          The item is complete.

        - `:incomplete`

          The item stopped before completing.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :message`

        The item type. Always `message`.

        - `:message`

    - `class AgentReasoningItem`

      A reasoning item produced by the agent.

      - `id: String`

        The ID of the reasoning item.

      - `status: AgentOutputItemStatus`

        The status of the reasoning item.

      - `summary: Array[SummaryText]`

        The reasoning summaries produced by the agent.

        - `text: String`

          The reasoning summary text.

        - `type: :summary_text`

          The content type. Always `summary_text`.

          - `:summary_text`

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :reasoning`

        The item type. Always `reasoning`.

        - `:reasoning`

    - `class AgentFunctionCallItem`

      A function call produced by the agent.

      - `id: String`

        The ID of the function call item.

      - `arguments: untyped`

        The arguments to pass to the function.

      - `call_id: String`

        The ID used to submit the function result.

      - `name: String`

        The name of the function to call.

      - `status: AgentFunctionCallStatus`

        The status of the function call.

        - `:in_progress`

          The call is in progress.

        - `:completed`

          The call completed successfully.

        - `:failed`

          The call failed.

        - `:incomplete`

          The call stopped before completing.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :function_call`

        The item type. Always `function_call`.

        - `:function_call`

    - `class AgentMcpCallItem`

      A call to a tool on an MCP server.

      - `id: String`

        The ID of the MCP call item.

      - `arguments: untyped`

        The arguments passed to the MCP tool.

      - `error: untyped`

        The error returned by the MCP tool, if any.

      - `name: String`

        The name of the MCP tool.

      - `output: untyped`

        The output returned by the MCP tool, if any.

      - `server_label: String`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :mcp_call`

        The item type. Always `mcp_call`.

        - `:mcp_call`

    - `class ComputerUseCall`

      One execution of the platform-provided computer-use capability.

      - `id: String`

        The ID of the activity item.

      - `output: Output{ image_url, type}`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: String`

          The complete JPEG image as a base64 data URL.

        - `type: :computer_screenshot`

          The content type. Always `computer_screenshot`.

          - `:computer_screenshot`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: String`

        A model-generated description of the activity, when available.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :computer_use_call`

        The item type. Always `computer_use_call`.

        - `:computer_use_call`

    - `class ComputerUseApprovalRequest`

      A credential-free history record of the emitted login request.

      - `id: String`

        The stable history item ID.

      - `request: Request{ credential_origin, fields, options, 2 more}`

        A registered form awaiting the application's response.

        - `credential_origin: String`

          The registered form or frame origin where values will be entered.

        - `fields: Array[Field{ id, label, required, type}]`

          Controls to render. All submitted values are sensitive.

          - `id: String`

            The field ID to submit as field_id in a fields entry.

          - `label: String`

            The label to display beside the control.

          - `required: bool`

            Whether this control requires a nonempty value.

          - `type: String`

            The rendering type, such as email, password, or text.

        - `options: Array[Option{ id, field_ids, label}]`

          Sign-in methods. Empty for a plain form.

          - `id: String`

            The option ID to submit as selected_option.

          - `field_ids: Array[String]`

            IDs from the registered fields that this method accepts.

          - `label: String`

            The method label to display.

        - `reason: String`

          Why the agent needs the user to sign in.

        - `type: :browser_authentication`

          The type of the object. Always `browser_authentication`.

          - `:browser_authentication`

      - `request_id: String`

      - `turn_id: String`

      - `type: :computer_use_approval_request`

        The item type. Always computer_use_approval_request.

        - `:computer_use_approval_request`

    - `class AgentWebSearchCallItem`

      A web search call produced by the agent.

      - `id: String`

        The ID of the web search call.

      - `action: WebSearchAction`

        The action performed by the web search tool.

        - `class Search`

          A search query or group of search queries.

          - `queries: Array[String]`

            The search queries, when multiple queries were used.

          - `query: String`

            The search query, when a single query was used.

          - `type: :search`

            The type of the object. Always `search`.

            - `:search`

        - `class OpenPage`

          Opens a web page.

          - `type: :open_page`

            The type of the object. Always `open_page`.

            - `:open_page`

          - `url: String`

            The URL of the page that was opened.

        - `class FindInPage`

          Finds text within a web page.

          - `pattern: String`

            The text pattern that was searched for.

          - `type: :find_in_page`

            The type of the object. Always `find_in_page`.

            - `:find_in_page`

          - `url: String`

            The URL of the page that was searched.

        - `class Other`

          Another web search action.

          - `type: :other`

            The type of the object. Always `other`.

            - `:other`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :web_search_call`

        The item type. Always `web_search_call`.

        - `:web_search_call`

    - `class AgentCommandExecutionItem`

      A command execution produced by the agent.

      - `id: String`

        The ID of the command execution item.

      - `command: String`

        The command that was executed.

      - `cwd: String`

        The working directory used to execute the command.

      - `duration_ms: Integer`

        The command duration in milliseconds.

      - `exit_code: Integer`

        The process exit code, if the command completed.

      - `output: String`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :command_execution`

        The item type. Always `command_execution`.

        - `:command_execution`

    - `class AgentCreateSubagentCallItem`

      A request to spawn a subagent.

      - `id: String`

        The ID of the tool call item.

      - `agent_id: String`

        The ID of the agent that requested the subagent.

      - `content: Array[AgentContent]`

        The task given to the spawned agent.

        - `class OutputText`

          A text content part produced by the agent.

          - `text: String`

            The text produced by the agent.

          - `type: :output_text`

            The content type. Always `output_text`.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

          - `encrypted_content: String`

            The encrypted content payload.

          - `type: :encrypted_content`

            The content type. Always `encrypted_content`.

            - `:encrypted_content`

      - `model: String`

        The model requested for the spawned agent.

      - `reasoning_effort: String`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :create_subagent_call`

        The item type. Always `create_subagent_call`.

        - `:create_subagent_call`

          The current public item type.

    - `class AgentSendSubagentInputCallItem`

      A request to send input to another agent.

      - `id: String`

        The ID of the tool call item.

      - `content: Array[AgentContent]`

        The input sent to the receiving agent.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: String`

        The ID of the agent receiving the input.

      - `sender_agent_id: String`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :send_subagent_input_call`

        The item type. Always `send_subagent_input_call`.

        - `:send_subagent_input_call`

          The current public item type.

    - `class AgentResumeSubagentCallItem`

      A request to resume a subagent.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to resume.

      - `sender_agent_id: String`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :resume_subagent_call`

        The item type. Always `resume_subagent_call`.

        - `:resume_subagent_call`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem`

      A request to wait for one or more subagents.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_ids: Array[String]`

        The IDs of the agents to wait for.

      - `sender_agent_id: String`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :wait_for_subagents_call`

        The item type. Always `wait_for_subagents_call`.

        - `:wait_for_subagents_call`

          The current public item type.

    - `class AgentInterruptSubagentCallItem`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to interrupt.

      - `sender_agent_id: String`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :interrupt_subagent_call`

        The item type. Always `interrupt_subagent_call`.

        - `:interrupt_subagent_call`

          The current public item type.

    - `class AgentCloseSubagentCallItem`

      A request to close a subagent.

      - `id: String`

        The ID of the tool call item.

      - `recipient_agent_id: String`

        The ID of the agent to close.

      - `sender_agent_id: String`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: String`

        The ID of the turn that contains this item.

      - `type: :close_subagent_call`

        The item type. Always `close_subagent_call`.

        - `:close_subagent_call`

          The current public item type.

  - `output_index: Integer`

    The index of the output item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.item.done"`

    The type of the object. Always `agent.session.turn.item.done`.

    - `:"agent.session.turn.item.done"`

### Agent Session Turn Output Text Delta Event

- `class AgentSessionTurnOutputTextDeltaEvent`

  Emitted when text is appended to an output text content part.

  - `content_index: Integer`

    The index of the content part in the message.

  - `delta: String`

    The text that was appended.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the message item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.output_text.delta"`

    The type of the object. Always `agent.session.turn.output_text.delta`.

    - `:"agent.session.turn.output_text.delta"`

### Agent Session Turn Output Text Done Event

- `class AgentSessionTurnOutputTextDoneEvent`

  Emitted when an output text content part is complete.

  - `content_index: Integer`

    The index of the content part in the message.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the message item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `text: String`

    The complete output text.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.output_text.done"`

    The type of the object. Always `agent.session.turn.output_text.done`.

    - `:"agent.session.turn.output_text.done"`

### Agent Session Turn Reasoning Summary Part Added Event

- `class AgentSessionTurnReasoningSummaryPartAddedEvent`

  Emitted when a reasoning summary content part is added.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the reasoning item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `part: SummaryText`

    The initial summary part.

    - `text: String`

      The reasoning summary text.

    - `type: :summary_text`

      The content type. Always `summary_text`.

      - `:summary_text`

  - `session_id: String`

    The ID of the session associated with the event.

  - `summary_index: Integer`

    The index of the summary content part.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.reasoning_summary_part.added"`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

    - `:"agent.session.turn.reasoning_summary_part.added"`

### Agent Session Turn Reasoning Summary Part Done Event

- `class AgentSessionTurnReasoningSummaryPartDoneEvent`

  Emitted when a reasoning summary part is complete.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the reasoning item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `part: SummaryText`

    The completed summary part.

    - `text: String`

      The reasoning summary text.

    - `type: :summary_text`

      The content type. Always `summary_text`.

      - `:summary_text`

  - `session_id: String`

    The ID of the session associated with the event.

  - `status: :incomplete`

    Present as `incomplete` when summary generation was interrupted.

    - `:incomplete`

  - `summary_index: Integer`

    The index of the summary part.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.reasoning_summary_part.done"`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

    - `:"agent.session.turn.reasoning_summary_part.done"`

### Agent Session Turn Reasoning Summary Text Delta Event

- `class AgentSessionTurnReasoningSummaryTextDeltaEvent`

  Emitted when text is appended to a reasoning summary.

  - `delta: String`

    The summary text that was appended.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the reasoning item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `summary_index: Integer`

    The index of the summary content part.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.reasoning_summary_text.delta"`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

    - `:"agent.session.turn.reasoning_summary_text.delta"`

### Agent Session Turn Reasoning Summary Text Done Event

- `class AgentSessionTurnReasoningSummaryTextDoneEvent`

  Emitted when a reasoning summary content part is complete.

  - `event_id: String`

    The unique ID of the event.

  - `item_id: String`

    The ID of the reasoning item.

  - `output_index: Integer`

    The index of the item in the turn output.

  - `session_id: String`

    The ID of the session associated with the event.

  - `summary_index: Integer`

    The index of the summary content part.

  - `text: String`

    The complete reasoning summary text.

  - `turn_id: String`

    The ID of the turn associated with the event, when applicable.

  - `type: :"agent.session.turn.reasoning_summary_text.done"`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

    - `:"agent.session.turn.reasoning_summary_text.done"`

### Agent Text

- `class AgentText`

  The text configuration used by an agent.

  - `format_: TextFormat`

    The effective output format. Defaults to ordinary text.

    - `class Text`

      Generates ordinary text without a structured-output constraint.

      - `type: :text`

        The type of the object. Always `text`.

        - `:text`

    - `class JSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Hash[Symbol, untyped]`

        The JSON Schema that generated text must match.

      - `type: :json_schema`

        The type of the object. Always `json_schema`.

        - `:json_schema`

  - `verbosity: :low | :medium | :high`

    The amount of text produced by the agent. Defaults to `medium`.

    - `:low`

    - `:medium`

    - `:high`

### Agent Text Param

- `class AgentTextParam`

  Configuration for text generated by the agent.

  - `format_: TextFormatParam`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `class Text`

      Generates ordinary text without a structured-output constraint.

      - `type: :text`

        The type of the object. Always `text`.

        - `:text`

    - `class JSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Hash[Symbol, untyped]`

        The JSON Schema that generated text must match.

      - `type: :json_schema`

        The type of the object. Always `json_schema`.

        - `:json_schema`

  - `verbosity: :low | :medium | :high`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `:low`

      Produces less text.

    - `:medium`

      Uses the default amount of text.

    - `:high`

      Produces more text.

### Agent Tool

- `AgentTool = Function{ defer_loading, description, name, 2 more} | ProgrammaticToolCalling{ enabled, type} | Mcp{ allowed_tools, connection_origin, credential_id, 5 more} | 2 more`

  A tool available to the agent.

  - `class Function`

    A function defined by the application.

    - `defer_loading: bool`

      Whether the function is deferred and discovered through tool search.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `enabled: bool`

      Whether tools can be called from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

  - `class Mcp`

    Tools provided by a remote MCP server.

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call.

    - `connection_origin: :service | :environment`

      Where outbound MCP HTTP connections originate.

      - `:service`

      - `:environment`

    - `credential_id: String`

      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransport`

      The transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

      - `class Stdio`

        Starts an MCP server as a local process.

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `env_vars: Array[String]`

          Environment variable names inherited from the execution environment.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

  - `class WebSearch`

    Web search.

    - `allowed_domains: Array[String]`

      Allowed search domains, or `null` when the search is unrestricted.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results, if provided.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results.

      - `:disabled`

      - `:cached`

      - `:live`

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

### Agent Tool Param

- `AgentToolParam = Function{ description, name, parameters, 2 more} | ToolSearch{ type} | ProgrammaticToolCalling{ type, enabled} | 3 more`

  A tool available to the agent.

  - `class Function`

    A function defined by the application.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

    - `defer_loading: bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `class ToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: :tool_search`

      The type of the object. Always `tool_search`.

      - `:tool_search`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

    - `enabled: bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class Mcp`

    Tools provided by a remote MCP server.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransportParam`

      The transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

        - `authorization: String`

          The authorization value sent to the MCP server, if any.

        - `headers: Hash[Symbol, String]`

          Additional HTTP headers sent to the MCP server.

      - `class Stdio`

        Starts an MCP server as a local process.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `env: Hash[Symbol, String]`

          Environment variables set for the MCP server process.

        - `env_vars: Array[String]`

          Environment variable names to inherit from the selected execution environment.

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: :service | :environment`

      Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

      - `:service`

        Uses the Managed Agents service network.

      - `:environment`

        Uses the session's execution environment.

    - `credential_id: String`

      The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class WebSearch`

    Web search.

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

    - `allowed_domains: Array[String]`

      Domains the search may include.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results. Defaults to `live`.

      - `:disabled`

        Disables web search.

      - `:cached`

        Uses cached search results.

      - `:live`

        Searches the live web.

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Agent Wait For Subagents Call Item

- `class AgentWaitForSubagentsCallItem`

  A request to wait for one or more subagents.

  - `id: String`

    The ID of the tool call item.

  - `recipient_agent_ids: Array[String]`

    The IDs of the agents to wait for.

  - `sender_agent_id: String`

    The ID of the agent waiting for results.

  - `status: AgentFunctionCallStatus`

    The status of the tool call.

    - `:in_progress`

      The call is in progress.

    - `:completed`

      The call completed successfully.

    - `:failed`

      The call failed.

    - `:incomplete`

      The call stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :wait_for_subagents_call`

    The item type. Always `wait_for_subagents_call`.

    - `:wait_for_subagents_call`

      The current public item type.

### Agent Web Search Call Item

- `class AgentWebSearchCallItem`

  A web search call produced by the agent.

  - `id: String`

    The ID of the web search call.

  - `action: WebSearchAction`

    The action performed by the web search tool.

    - `class Search`

      A search query or group of search queries.

      - `queries: Array[String]`

        The search queries, when multiple queries were used.

      - `query: String`

        The search query, when a single query was used.

      - `type: :search`

        The type of the object. Always `search`.

        - `:search`

    - `class OpenPage`

      Opens a web page.

      - `type: :open_page`

        The type of the object. Always `open_page`.

        - `:open_page`

      - `url: String`

        The URL of the page that was opened.

    - `class FindInPage`

      Finds text within a web page.

      - `pattern: String`

        The text pattern that was searched for.

      - `type: :find_in_page`

        The type of the object. Always `find_in_page`.

        - `:find_in_page`

      - `url: String`

        The URL of the page that was searched.

    - `class Other`

      Another web search action.

      - `type: :other`

        The type of the object. Always `other`.

        - `:other`

  - `status: AgentOutputItemStatus`

    The status of the web search call.

    - `:in_progress`

      The item is in progress.

    - `:completed`

      The item is complete.

    - `:incomplete`

      The item stopped before completing.

  - `turn_id: String`

    The ID of the turn that contains this item.

  - `type: :web_search_call`

    The item type. Always `web_search_call`.

    - `:web_search_call`

### Environment

- `Environment = None{ type} | OpenAIHosted{ id, capability_directories, desktop, 7 more} | SelfHosted{ id, capability_directories, remote_url, 2 more}`

  The execution environment for a session.

  - `class None`

    The session talks to CCA without selecting or provisioning an execution environment.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class OpenAIHosted`

    An environment hosted by OpenAI.

    - `id: String`

      The public ID of the environment.

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent.

    - `desktop: Desktop{ enabled}`

      The effective desktop configuration.

      - `enabled: bool`

        Whether the environment provisions a desktop and browser proxy.

    - `files: Array[HostedEnvironmentFile]`

      Files available in the environment, excluding their contents.

      - `class HostedEnvironmentFileID`

        A file copied from the OpenAI Files API.

        - `id: String`

          The session-scoped ID of the file in the execution environment.

        - `file_id: String`

          The ID of the uploaded file.

        - `path: String`

          The file's absolute path inside the environment.

        - `size_bytes: Integer`

          The decoded file size in bytes.

        - `type: :file_id`

          The type of the object. Always `file_id`.

          - `:file_id`

      - `class Inline`

        A file supplied inline when the session was created.

        - `id: String`

          The session-scoped ID of the file in the execution environment.

        - `path: String`

          The file's absolute path inside the environment.

        - `size_bytes: Integer`

          The decoded file size in bytes.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

    - `network: Network{ access, allowed_domains}`

      The effective network access policy for the environment.

      - `access: :enabled | :disabled | :restricted`

        The environment's network access mode.

        - `:enabled`

          Allows unrestricted network access.

        - `:disabled`

          Disables network access.

        - `:restricted`

          Applies the configured domain restrictions.

      - `allowed_domains: Array[String]`

        Domains the environment may access when network access is restricted.

    - `packages: Packages{ npm, python, system_}`

      Packages installed in the environment.

      - `npm: Array[String]`

        npm packages installed globally in the environment.

      - `python: Array[String]`

        Python packages installed in the environment.

      - `system_: Array[String]`

        System packages installed in the environment.

    - `plugins: Array[HostedPlugin]`

      Plugins installed in the environment, excluding their archive contents.

      - `description: String`

        The installed plugin description.

      - `name: String`

        The installed plugin name.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

    - `skills: Array[HostedSkill]`

      Skills installed in the environment, excluding their archive contents.

      - `class HostedSkillReference`

        A skill installed from the Skills API.

        - `description: String`

          The installed skill description.

        - `name: String`

          The installed skill name.

        - `skill_id: String`

          The referenced skill ID.

        - `type: :skill_reference`

          The type of the object. Always `skill_reference`.

          - `:skill_reference`

        - `version: String`

          The concrete skill version installed for this session.

      - `class Inline`

        A skill installed from an inline ZIP archive.

        - `description: String`

          The installed skill description.

        - `name: String`

          The installed skill name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

    - `type: :openai_hosted`

      The type of the object. Always `openai_hosted`.

      - `:openai_hosted`

    - `container_size: :small | :medium | :large`

      The effective CPU and memory tier, or null when unknown or outside the public tiers.

      - `:small`

      - `:medium`

      - `:large`

  - `class SelfHosted`

    An environment hosted by the application.

    - `id: String`

      The public ID of the environment.

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent.

    - `remote_url: String`

      Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

    - `type: :self_hosted`

      The type of the object. Always `self_hosted`.

      - `:self_hosted`

    - `workspace_directory: String`

      The absolute project directory inside the environment. Defaults to `/workspace`.

### Environment Param

- `EnvironmentParam = None{ type} | OpenAIHosted{ type, capability_directories, container_size, 9 more} | SelfHosted{ type, workspace_directory, capability_directories}`

  The execution environment and optional reusable template for a session.

  - `class None`

    Runs the agent without an execution environment.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class OpenAIHosted`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: :openai_hosted`

      The type of the object. Always `openai_hosted`.

      - `:openai_hosted`

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size: :small | :medium | :large`

      The hosted container size. Omission selects the medium tier.

      - `:small`

      - `:medium`

      - `:large`

    - `desktop: Desktop{ enabled}`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: bool`

        Whether to provision the desktop and its browser proxy.

    - `env: Hash[Symbol, String]`

      Environment variables made available to the agent.

    - `environment_template_id: String`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Array[HostedEnvironmentFileParam]`

      Files available before the agent starts. Defaults to an empty list.

      - `class FileID`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: String`

          The ID of the uploaded file.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :file_id`

          The type of the object. Always `file_id`.

          - `:file_id`

      - `class Inline`

        A file supplied directly as standard-base64 data.

        - `data: String`

          The standard-base64-encoded file contents.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

    - `network: Network{ access, allowed_domains, blocked_domains}`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `access: :enabled | :disabled | :restricted`

        The environment's network access mode.

        - `:enabled`

          Allows unrestricted network access.

        - `:disabled`

          Disables network access.

        - `:restricted`

          Applies the configured domain restrictions.

      - `allowed_domains: Array[String]`

        Domains the environment may access when network access is restricted.

      - `blocked_domains: Array[String]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Packages{ npm, python, system_}`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Array[String]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Array[String]`

        Python packages to install. Defaults to an empty list.

      - `system_: Array[String]`

        System packages to install. Defaults to an empty list.

    - `plugins: Array[HostedPluginParam]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: String`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: String`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: String`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: :"application/zip"`

          The archive media type, always `application/zip`.

          - `:"application/zip"`

            A ZIP archive.

        - `type: :base64`

          The type of the object. Always `base64`.

          - `:base64`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

    - `setup_commands: Array[SetupCommandParam]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: String`

        The shell command to execute.

      - `cwd: String`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Array[HostedSkillParam]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class SkillReference`

        References a skill uploaded through the Skills API.

        - `skill_id: String`

          The ID of the skill created through `/v1/skills`.

        - `type: :skill_reference`

          The type of the object. Always `skill_reference`.

          - `:skill_reference`

        - `version: String`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class Inline`

        Supplies a skill ZIP directly in the session request.

        - `description: String`

          The skill description declared in `SKILL.md`.

        - `name: String`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

  - `class SelfHosted`

    An application-hosted environment configured inline.

    - `type: :self_hosted`

      The type of the object. Always `self_hosted`.

      - `:self_hosted`

    - `workspace_directory: String`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

### Hosted Environment File

- `HostedEnvironmentFile = HostedEnvironmentFileID | Inline{ id, path, size_bytes, type}`

  Metadata for a file materialized in an OpenAI-hosted execution environment.

  - `class HostedEnvironmentFileID`

    A file copied from the OpenAI Files API.

    - `id: String`

      The session-scoped ID of the file in the execution environment.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The file's absolute path inside the environment.

    - `size_bytes: Integer`

      The decoded file size in bytes.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied inline when the session was created.

    - `id: String`

      The session-scoped ID of the file in the execution environment.

    - `path: String`

      The file's absolute path inside the environment.

    - `size_bytes: Integer`

      The decoded file size in bytes.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Hosted Environment File ID

- `class HostedEnvironmentFileID`

  A file copied from the OpenAI Files API.

  - `id: String`

    The session-scoped ID of the file in the execution environment.

  - `file_id: String`

    The ID of the uploaded file.

  - `path: String`

    The file's absolute path inside the environment.

  - `size_bytes: Integer`

    The decoded file size in bytes.

  - `type: :file_id`

    The type of the object. Always `file_id`.

    - `:file_id`

### Hosted Environment File Param

- `HostedEnvironmentFileParam = FileID{ file_id, path, type} | Inline{ data, path, type}`

  A file materialized in an OpenAI-hosted execution environment.

  - `class FileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied directly as standard-base64 data.

    - `data: String`

      The standard-base64-encoded file contents.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Hosted Plugin

- `class HostedPlugin`

  A plugin installed from an inline ZIP archive.

  - `description: String`

    The installed plugin description.

  - `name: String`

    The installed plugin name.

  - `type: :inline`

    The type of the object. Always `inline`.

    - `:inline`

### Hosted Plugin Param

- `class HostedPluginParam`

  Supplies a plugin ZIP directly in the session request.

  - `description: String`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: String`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: String`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: :"application/zip"`

      The archive media type, always `application/zip`.

      - `:"application/zip"`

        A ZIP archive.

    - `type: :base64`

      The type of the object. Always `base64`.

      - `:base64`

  - `type: :inline`

    The type of the object. Always `inline`.

    - `:inline`

### Hosted Skill

- `HostedSkill = HostedSkillReference | Inline{ description, name, type}`

  A skill installed in an OpenAI-hosted environment.

  - `class HostedSkillReference`

    A skill installed from the Skills API.

    - `description: String`

      The installed skill description.

    - `name: String`

      The installed skill name.

    - `skill_id: String`

      The referenced skill ID.

    - `type: :skill_reference`

      The type of the object. Always `skill_reference`.

      - `:skill_reference`

    - `version: String`

      The concrete skill version installed for this session.

  - `class Inline`

    A skill installed from an inline ZIP archive.

    - `description: String`

      The installed skill description.

    - `name: String`

      The installed skill name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Hosted Skill Param

- `HostedSkillParam = SkillReference{ skill_id, type, version} | Inline{ description, name, source, type}`

  A skill installed in an OpenAI-hosted environment.

  - `class SkillReference`

    References a skill uploaded through the Skills API.

    - `skill_id: String`

      The ID of the skill created through `/v1/skills`.

    - `type: :skill_reference`

      The type of the object. Always `skill_reference`.

      - `:skill_reference`

    - `version: String`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class Inline`

    Supplies a skill ZIP directly in the session request.

    - `description: String`

      The skill description declared in `SKILL.md`.

    - `name: String`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: String`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: :"application/zip"`

        The archive media type, always `application/zip`.

        - `:"application/zip"`

          A ZIP archive.

      - `type: :base64`

        The type of the object. Always `base64`.

        - `:base64`

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Hosted Skill Reference

- `class HostedSkillReference`

  A skill installed from the Skills API.

  - `description: String`

    The installed skill description.

  - `name: String`

    The installed skill name.

  - `skill_id: String`

    The referenced skill ID.

  - `type: :skill_reference`

    The type of the object. Always `skill_reference`.

    - `:skill_reference`

  - `version: String`

    The concrete skill version installed for this session.

### Inline Capability Source Param

- `class InlineCapabilitySourceParam`

  Provides ZIP bytes encoded with standard base64.

  - `data: String`

    Standard-base64 encoded ZIP archive bytes.

  - `media_type: :"application/zip"`

    The archive media type, always `application/zip`.

    - `:"application/zip"`

      A ZIP archive.

  - `type: :base64`

    The type of the object. Always `base64`.

    - `:base64`

### Input Content

- `InputContent = InputText{ text, type} | InputImage{ image_url, type}`

  User-provided content recorded in a session item.

  - `class InputText`

    Text input recorded in a session item.

    - `text: String`

      The text supplied to the agent.

    - `type: :input_text`

      The type of the object. Always `input_text`.

      - `:input_text`

  - `class InputImage`

    Image input recorded in a session item.

    - `image_url: String`

      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

    - `type: :input_image`

      The type of the object. Always `input_image`.

      - `:input_image`

### Input Content Param

- `InputContentParam = InputText{ text, type} | InputImage{ image_url, type}`

  Content included in an input message.

  - `class InputText`

    Text input to the model.

    - `text: String`

      The text sent to the model.

    - `type: :input_text`

      The type of the object. Always `input_text`.

      - `:input_text`

  - `class InputImage`

    Image input to the model.

    - `image_url: String`

      The URL of the image sent to the model.

    - `type: :input_image`

      The type of the object. Always `input_image`.

      - `:input_image`

### Mcp Transport

- `McpTransport = HTTP{ server_url, type} | Stdio{ args, command, cwd, 2 more}`

  The transport used to connect to an MCP server.

  - `class HTTP`

    Connects to an MCP server over HTTP.

    - `server_url: String`

      The URL of the MCP server.

    - `type: :http`

      The type of the object. Always `http`.

      - `:http`

  - `class Stdio`

    Starts an MCP server as a local process.

    - `args: Array[String]`

      Arguments passed to the MCP server command.

    - `command: String`

      The command used to start the MCP server.

    - `cwd: String`

      The working directory used to start the MCP server.

    - `env_vars: Array[String]`

      Environment variable names inherited from the execution environment.

    - `type: :stdio`

      The type of the object. Always `stdio`.

      - `:stdio`

### Mcp Transport Param

- `McpTransportParam = HTTP{ server_url, type, authorization, headers} | Stdio{ command, cwd, type, 3 more}`

  The transport used to connect to an MCP server.

  - `class HTTP`

    Connects to an MCP server over HTTP.

    - `server_url: String`

      The URL of the MCP server.

    - `type: :http`

      The type of the object. Always `http`.

      - `:http`

    - `authorization: String`

      The authorization value sent to the MCP server, if any.

    - `headers: Hash[Symbol, String]`

      Additional HTTP headers sent to the MCP server.

  - `class Stdio`

    Starts an MCP server as a local process.

    - `command: String`

      The command used to start the MCP server.

    - `cwd: String`

      The working directory used to start the MCP server.

    - `type: :stdio`

      The type of the object. Always `stdio`.

      - `:stdio`

    - `args: Array[String]`

      Arguments passed to the MCP server command.

    - `env: Hash[Symbol, String]`

      Environment variables set for the MCP server process.

    - `env_vars: Array[String]`

      Environment variable names to inherit from the selected execution environment.

### Multi Agent Config

- `class MultiAgentConfig`

  The resolved configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled. Defaults to false.

  - `max_concurrent_subagents: Integer`

    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

### Multi Agent Config Param

- `class MultiAgentConfigParam`

  Explicit configuration for creating and coordinating subagents.

  - `enabled: bool`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents: Integer`

    Maximum number of subagents that may run concurrently. Defaults to 6.

### Output Text

- `class OutputText`

  A text content part produced by the agent.

  - `text: String`

    The text produced by the agent.

  - `type: :output_text`

    The content type. Always `output_text`.

    - `:output_text`

### Persisted Agent Tool

- `PersistedAgentTool = Function{ defer_loading, description, name, 2 more} | ToolSearch{ type} | ProgrammaticToolCalling{ enabled, type} | 3 more`

  A credential-free tool available to a reusable agent.

  - `class Function`

    A function defined by the application.

    - `defer_loading: bool`

      Whether the function is deferred and discovered through tool search.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

  - `class ToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: :tool_search`

      The type of the object. Always `tool_search`.

      - `:tool_search`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `enabled: bool`

      Whether tools can be called from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

  - `class Mcp`

    Tools provided by a remote MCP server without stored credentials.

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call, or null when all server tools are allowed.

    - `connection_origin: :service | :environment`

      Where outbound MCP HTTP connections originate.

      - `:service`

      - `:environment`

    - `credential_id: String`

      The vault credential selected for this MCP server, if any.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransport`

      The credential-free transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `headers: Hash[Symbol, String]`

          Non-secret HTTP headers sent to the MCP server.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

      - `class Stdio`

        Starts an MCP server as a local process.

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `env_vars: Array[String]`

          Environment variable names inherited from the execution environment.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

  - `class WebSearch`

    Web search.

    - `allowed_domains: Array[String]`

      Allowed search domains, or `null` when the search is unrestricted.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results, if provided.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results.

      - `:disabled`

      - `:cached`

      - `:live`

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

### Persisted Agent Tool Param

- `PersistedAgentToolParam = Function{ description, name, parameters, 2 more} | ToolSearch{ type} | ProgrammaticToolCalling{ type, enabled} | 3 more`

  A tool that can be stored on a reusable agent without session credentials.

  - `class Function`

    A function defined by the application.

    - `description: String`

      A description of what the function does.

    - `name: String`

      The name of the function.

    - `parameters: Hash[Symbol, untyped]`

      A JSON Schema object describing the function's arguments.

    - `type: :function`

      The type of the object. Always `function`.

      - `:function`

    - `defer_loading: bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `class ToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: :tool_search`

      The type of the object. Always `tool_search`.

      - `:tool_search`

  - `class ProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: :programmatic_tool_calling`

      The type of the object. Always `programmatic_tool_calling`.

      - `:programmatic_tool_calling`

    - `enabled: bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `class Mcp`

    Tools provided by a remote MCP server without stored credentials.

    - `server_label: String`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransportParam`

      The credential-free transport used to connect to the MCP server.

      - `class HTTP`

        Connects to an MCP server over HTTP.

        - `server_url: String`

          The URL of the MCP server.

        - `type: :http`

          The type of the object. Always `http`.

          - `:http`

        - `headers: Hash[Symbol, String]`

          Non-secret HTTP headers sent to the MCP server.

      - `class Stdio`

        Starts an MCP server as a local process.

        - `command: String`

          The command used to start the MCP server.

        - `cwd: String`

          The working directory used to start the MCP server.

        - `type: :stdio`

          The type of the object. Always `stdio`.

          - `:stdio`

        - `args: Array[String]`

          Arguments passed to the MCP server command.

        - `env_vars: Array[String]`

          Environment variable names to inherit from the selected execution environment.

    - `type: :mcp`

      The type of the object. Always `mcp`.

      - `:mcp`

    - `allowed_tools: Array[String]`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin: :service | :environment`

      Selects where outbound MCP HTTP connections originate.

      - `:service`

        Uses the Managed Agents service network.

      - `:environment`

        Uses the session's execution environment.

    - `credential_id: String`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Hash[Symbol, untyped]`

      Metadata included with requests to this MCP server.

    - `required: bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `class WebSearch`

    Web search.

    - `type: :web_search`

      The type of the object. Always `web_search`.

      - `:web_search`

    - `allowed_domains: Array[String]`

      Domains the search may include.

    - `context_size: :low | :medium | :high`

      The amount of search context made available to the model. Defaults to `medium`.

      - `:low`

      - `:medium`

      - `:high`

    - `location: Location{ city, country, region, timezone}`

      Approximate location used to localize search results.

      - `city: String`

        The city name.

      - `country: String`

        The two-letter ISO country code, such as `US`.

      - `region: String`

        The region or state name.

      - `timezone: String`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: :disabled | :cached | :live`

      The source used for web search results. Defaults to `live`.

      - `:disabled`

        Disables web search.

      - `:cached`

        Uses cached search results.

      - `:live`

        Searches the live web.

  - `class ComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: :computer_use`

      The type of the object. Always `computer_use`.

      - `:computer_use`

    - `include_screenshots: bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Persisted Mcp Transport

- `PersistedMcpTransport = HTTP{ headers, server_url, type} | Stdio{ args, command, cwd, 2 more}`

  A credential-free transport used to connect to an MCP server.

  - `class HTTP`

    Connects to an MCP server over HTTP.

    - `headers: Hash[Symbol, String]`

      Non-secret HTTP headers sent to the MCP server.

    - `server_url: String`

      The URL of the MCP server.

    - `type: :http`

      The type of the object. Always `http`.

      - `:http`

  - `class Stdio`

    Starts an MCP server as a local process.

    - `args: Array[String]`

      Arguments passed to the MCP server command.

    - `command: String`

      The command used to start the MCP server.

    - `cwd: String`

      The working directory used to start the MCP server.

    - `env_vars: Array[String]`

      Environment variable names inherited from the execution environment.

    - `type: :stdio`

      The type of the object. Always `stdio`.

      - `:stdio`

### Persisted Mcp Transport Param

- `PersistedMcpTransportParam = HTTP{ server_url, type, headers} | Stdio{ command, cwd, type, 2 more}`

  A credential-free transport used to connect to an MCP server.

  - `class HTTP`

    Connects to an MCP server over HTTP.

    - `server_url: String`

      The URL of the MCP server.

    - `type: :http`

      The type of the object. Always `http`.

      - `:http`

    - `headers: Hash[Symbol, String]`

      Non-secret HTTP headers sent to the MCP server.

  - `class Stdio`

    Starts an MCP server as a local process.

    - `command: String`

      The command used to start the MCP server.

    - `cwd: String`

      The working directory used to start the MCP server.

    - `type: :stdio`

      The type of the object. Always `stdio`.

      - `:stdio`

    - `args: Array[String]`

      Arguments passed to the MCP server command.

    - `env_vars: Array[String]`

      Environment variable names to inherit from the selected execution environment.

### Session Error

- `class SessionError`

  An error payload with the same public fields as Responses API streaming errors.

  - `code: String`

    The machine-readable error code, if any.

  - `message: String`

    A customer-safe explanation of the error.

  - `param: String`

    The request parameter associated with the error, if any.

  - `type: String`

    The error type.

### Session Turn Error

- `class SessionTurnError`

  A customer-safe error describing why a session request failed.

  - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

    A stable, machine-readable failure category.

    - `:context_length_exceeded`

      The request exceeds the model's context window.

    - `:session_budget_exceeded`

      The session has reached its usage budget.

    - `:usage_limit_exceeded`

      The organization has reached a usage, plan, or billing limit.

    - `:credit_balance_exhausted`

      The organization has no API credits remaining.

    - `:rate_limit_exceeded`

      The request exceeds the available rate limit.

    - `:flex_unavailable`

      Flex processing is temporarily unavailable.

    - `:server_overloaded`

      The model service is temporarily overloaded.

    - `:cyber_policy`

      The request was rejected by a safety policy.

    - `:misalignment_policy_violation`

      The request was blocked by the safety systems.

    - `:connection_failed`

      The request could not connect to the model service.

    - `:server_error`

      The model service encountered an unexpected error.

    - `:authentication_error`

      The API credentials are invalid or lack the required access.

    - `:invalid_request`

      The request contains invalid input or configuration.

    - `:resource_not_found`

      The requested model or resource is unavailable.

    - `:sandbox_error`

      The request could not complete in its execution environment.

    - `:executor_version_incompatible`

      The executor must be upgraded before it can run this turn.

    - `:active_turn_not_steerable`

      The session cannot accept additional input while a request is running.

    - `:request_timeout`

      The request timed out before the model service responded.

    - `:internal_error`

      An unexpected internal error prevented the session request from completing.

  - `message: String`

    A customer-safe explanation of the failure.

### Setup Command Param

- `class SetupCommandParam`

  A confidential setup command executed before the hosted agent starts.

  - `command: String`

    The shell command to execute.

  - `cwd: String`

    The absolute working directory. Defaults to `/workspace`.

### Subagent

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

### Summary Text

- `class SummaryText`

  A reasoning summary content part.

  - `text: String`

    The reasoning summary text.

  - `type: :summary_text`

    The content type. Always `summary_text`.

    - `:summary_text`

### Text Format

- `TextFormat = Text{ type} | JSONSchema{ schema, type}`

  The effective output format for generated text.

  - `class Text`

    Generates ordinary text without a structured-output constraint.

    - `type: :text`

      The type of the object. Always `text`.

      - `:text`

  - `class JSONSchema`

    Constrains generated text to a JSON Schema.

    - `schema: Hash[Symbol, untyped]`

      The JSON Schema that generated text must match.

    - `type: :json_schema`

      The type of the object. Always `json_schema`.

      - `:json_schema`

### Text Format Param

- `TextFormatParam = Text{ type} | JSONSchema{ schema, type}`

  The output format for generated text.

  - `class Text`

    Generates ordinary text without a structured-output constraint.

    - `type: :text`

      The type of the object. Always `text`.

      - `:text`

  - `class JSONSchema`

    Constrains generated text to a JSON Schema.

    - `schema: Hash[Symbol, untyped]`

      The JSON Schema that generated text must match.

    - `type: :json_schema`

      The type of the object. Always `json_schema`.

      - `:json_schema`

### Token Usage

- `class TokenUsage`

  Recorded token usage for a session or turn. Usage is best effort and may change.

  - `input_tokens: Integer`

    The number of input tokens used by the agent.

  - `input_tokens_details: InputTokensDetails{ cached_tokens}`

    A breakdown of the agent's input token usage.

    - `cached_tokens: Integer`

      The number of input tokens retrieved from the prompt cache.

  - `output_tokens: Integer`

    The number of output tokens generated by the agent.

  - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

    A breakdown of the agent's output token usage.

    - `reasoning_tokens: Integer`

      The number of output tokens used for reasoning.

  - `total_tokens: Integer`

    The total number of input and output tokens used by the agent.

### Web Search Action

- `WebSearchAction = Search{ queries, query, type} | OpenPage{ type, url} | FindInPage{ pattern, type, url} | Other{ type}`

  An action performed by the web search tool.

  - `class Search`

    A search query or group of search queries.

    - `queries: Array[String]`

      The search queries, when multiple queries were used.

    - `query: String`

      The search query, when a single query was used.

    - `type: :search`

      The type of the object. Always `search`.

      - `:search`

  - `class OpenPage`

    Opens a web page.

    - `type: :open_page`

      The type of the object. Always `open_page`.

      - `:open_page`

    - `url: String`

      The URL of the page that was opened.

  - `class FindInPage`

    Finds text within a web page.

    - `pattern: String`

      The text pattern that was searched for.

    - `type: :find_in_page`

      The type of the object. Always `find_in_page`.

      - `:find_in_page`

    - `url: String`

      The URL of the page that was searched.

  - `class Other`

    Another web search action.

    - `type: :other`

      The type of the object. Always `other`.

      - `:other`

# Environments

## Retrieve an agent environment

`beta.agents.environments.retrieve(environment_id) -> EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environment_id: String`

### Returns

- `class EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: String`

    The ID of the environment.

  - `files: Array[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      A file supplied inline when the session was created.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `object: :"agent.environment"`

    The object type. Always `agent.environment`.

    - `:"agent.environment"`

  - `plugins: Array[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference`

      A skill installed from the Skills API.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The concrete skill version installed for this session.

    - `class Inline`

      A skill installed from an inline ZIP archive.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `status: :pending | :connected | :disconnected | 2 more`

    The current environment connection status.

    - `:pending`

    - `:connected`

    - `:disconnected`

    - `:expired`

    - `:failed`

  - `type: :openai_hosted | :self_hosted`

    Whether the environment is hosted by OpenAI or by the application.

    - `:openai_hosted`

    - `:self_hosted`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_info = openai.beta.agents.environments.retrieve("environment_id")

puts(environment_info)
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

- `class EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: String`

    The ID of the environment.

  - `files: Array[HostedEnvironmentFile]`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      A file supplied inline when the session was created.

      - `id: String`

        The session-scoped ID of the file in the execution environment.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded file size in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `object: :"agent.environment"`

    The object type. Always `agent.environment`.

    - `:"agent.environment"`

  - `plugins: Array[HostedPlugin]`

    Plugins installed in the environment, without their archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[HostedSkill]`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference`

      A skill installed from the Skills API.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The concrete skill version installed for this session.

    - `class Inline`

      A skill installed from an inline ZIP archive.

      - `description: String`

        The installed skill description.

      - `name: String`

        The installed skill name.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `status: :pending | :connected | :disconnected | 2 more`

    The current environment connection status.

    - `:pending`

    - `:connected`

    - `:disconnected`

    - `:expired`

    - `:failed`

  - `type: :openai_hosted | :self_hosted`

    Whether the environment is hosted by OpenAI or by the application.

    - `:openai_hosted`

    - `:self_hosted`

# Files

## Create an agent environment file

`beta.agents.environments.files.create(environment_id, **kwargs) -> EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: String`

- `hosted_environment_file_param: HostedEnvironmentFileParam`

  A file materialized in an OpenAI-hosted execution environment.

  - `class FileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied directly as standard-base64 data.

    - `data: String`

      The standard-base64-encoded file contents.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Returns

- `class EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: String`

    The ID of the environment containing this file.

  - `object: :"agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `:"agent.environment.file"`

  - `path: String`

    The absolute file path inside the environment's workspace.

  - `size_bytes: Integer`

    The file size in bytes.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_file = openai.beta.agents.environments.files.create("environment_id")

puts(environment_file)
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

`beta.agents.environments.files.list(environment_id, **kwargs) -> TokenPage<EnvironmentFile>`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environment_id: String`

- `limit: Integer`

  The maximum number of files to return, between 1 and 100.

- `order: :asc | :desc`

  Sort by case-sensitive path components. Defaults to descending.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `page: String`

  The opaque token from the previous page. Keep the same path, order, and limit.

- `path: String`

  Restrict the listing to this absolute workspace directory.

### Returns

- `class EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: String`

    The ID of the environment containing this file.

  - `object: :"agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `:"agent.environment.file"`

  - `path: String`

    The absolute file path inside the environment's workspace.

  - `size_bytes: Integer`

    The file size in bytes.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.environments.files.list("environment_id")

puts(page)
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

- `class EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: String`

    The ID of the environment containing this file.

  - `object: :"agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `:"agent.environment.file"`

  - `path: String`

    The absolute file path inside the environment's workspace.

  - `size_bytes: Integer`

    The file size in bytes.

# Templates

## Create an agent environment template

`beta.agents.environments.templates.create(**kwargs) -> EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `capability_directories: Array[String]`

  Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `desktop: Desktop{ enabled}`

  Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Hash[Symbol, String]`

  Environment variables made available to the agent.

- `files: Array[HostedEnvironmentFileParam]`

  Files available before the agent starts. Defaults to an empty list.

  - `class FileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied directly as standard-base64 data.

    - `data: String`

      The standard-base64-encoded file contents.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

- `name: String`

  An optional human-readable display name for the template.

- `network: Network{ access, allowed_domains, blocked_domains}`

  Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

  - `access: :enabled | :disabled | :restricted`

    The environment's network access mode.

    - `:enabled`

      Allows unrestricted network access.

    - `:disabled`

      Disables network access.

    - `:restricted`

      Applies the configured domain restrictions.

  - `allowed_domains: Array[String]`

    Domains the environment may access when network access is restricted.

  - `blocked_domains: Array[String]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Packages{ npm, python, system_}`

  Packages to install in the environment. Defaults to empty package lists.

  - `npm: Array[String]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Array[String]`

    Python packages to install. Defaults to an empty list.

  - `system_: Array[String]`

    System packages to install. Defaults to an empty list.

- `plugins: Array[HostedPluginParam]`

  Plugins provided as inline ZIP archives. Defaults to an empty list.

  - `description: String`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: String`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: String`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: :"application/zip"`

      The archive media type, always `application/zip`.

      - `:"application/zip"`

        A ZIP archive.

    - `type: :base64`

      The type of the object. Always `base64`.

      - `:base64`

  - `type: :inline`

    The type of the object. Always `inline`.

    - `:inline`

- `setup_commands: Array[SetupCommandParam]`

  Ordered, confidential setup commands. Command bodies are never returned.

  - `command: String`

    The shell command to execute.

  - `cwd: String`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Array[HostedSkillParam]`

  Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

  - `class SkillReference`

    References a skill uploaded through the Skills API.

    - `skill_id: String`

      The ID of the skill created through `/v1/skills`.

    - `type: :skill_reference`

      The type of the object. Always `skill_reference`.

      - `:skill_reference`

    - `version: String`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class Inline`

    Supplies a skill ZIP directly in the session request.

    - `description: String`

      The skill description declared in `SKILL.md`.

    - `name: String`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Returns

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template = openai.beta.agents.environments.templates.create

puts(environment_template)
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

`beta.agents.environments.templates.delete(environment_template_id) -> EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: String`

### Returns

- `class EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: String`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: :"agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `:"agent.environment.template.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template_deleted = openai.beta.agents.environments.templates.delete("environment_template_id")

puts(environment_template_deleted)
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

`beta.agents.environments.templates.list(**kwargs) -> CursorPage<EnvironmentTemplate>`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.environments.templates.list

puts(page)
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

`beta.agents.environments.templates.retrieve(environment_template_id) -> EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: String`

### Returns

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template = openai.beta.agents.environments.templates.retrieve("environment_template_id")

puts(environment_template)
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

`beta.agents.environments.templates.update(environment_template_id, **kwargs) -> EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environment_template_id: String`

- `capability_directories: Array[String]`

  Directories that expose capabilities to the agent.

- `desktop: Desktop{ enabled}`

  Replacement desktop configuration, or null to disable the desktop.

  - `enabled: bool`

    Whether to provision the desktop and its browser proxy.

- `env: Hash[Symbol, String]`

  Replacement confidential environment values.

- `files: Array[HostedEnvironmentFileParam]`

  Replacement file configuration materialized for each new session.

  - `class FileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: String`

      The ID of the uploaded file.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :file_id`

      The type of the object. Always `file_id`.

      - `:file_id`

  - `class Inline`

    A file supplied directly as standard-base64 data.

    - `data: String`

      The standard-base64-encoded file contents.

    - `path: String`

      The absolute destination path inside `/workspace`.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

- `name: String`

  A replacement human-readable display name, or `null` to clear the name.

- `network: Network{ access, allowed_domains, blocked_domains}`

  Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

  - `access: :enabled | :disabled | :restricted`

    The environment's network access mode.

    - `:enabled`

      Allows unrestricted network access.

    - `:disabled`

      Disables network access.

    - `:restricted`

      Applies the configured domain restrictions.

  - `allowed_domains: Array[String]`

    Domains the environment may access when network access is restricted.

  - `blocked_domains: Array[String]`

    Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

- `packages: Packages{ npm, python, system_}`

  Packages installed before the runtime network policy applies.

  - `npm: Array[String]`

    npm packages to install globally. Defaults to an empty list.

  - `python: Array[String]`

    Python packages to install. Defaults to an empty list.

  - `system_: Array[String]`

    System packages to install. Defaults to an empty list.

- `plugins: Array[HostedPluginParam]`

  Replacement plugin configuration installed for each new session.

  - `description: String`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: String`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: String`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: :"application/zip"`

      The archive media type, always `application/zip`.

      - `:"application/zip"`

        A ZIP archive.

    - `type: :base64`

      The type of the object. Always `base64`.

      - `:base64`

  - `type: :inline`

    The type of the object. Always `inline`.

    - `:inline`

- `setup_commands: Array[SetupCommandParam]`

  Replacement confidential setup commands, never included in returned resources.

  - `command: String`

    The shell command to execute.

  - `cwd: String`

    The absolute working directory. Defaults to `/workspace`.

- `skills: Array[HostedSkillParam]`

  Replacement skill configuration installed for each new session.

  - `class SkillReference`

    References a skill uploaded through the Skills API.

    - `skill_id: String`

      The ID of the skill created through `/v1/skills`.

    - `type: :skill_reference`

      The type of the object. Always `skill_reference`.

      - `:skill_reference`

    - `version: String`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `class Inline`

    Supplies a skill ZIP directly in the session request.

    - `description: String`

      The skill description declared in `SKILL.md`.

    - `name: String`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

### Returns

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

environment_template = openai.beta.agents.environments.templates.update("environment_template_id")

puts(environment_template)
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

- `class EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: String`

    The ID of the reusable environment template.

  - `capability_directories: Array[String]`

    Directories that expose capabilities to the agent.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop{ enabled}`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: bool`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array[FileID{ file_id, path, type} | Inline{ path, size_bytes, type}]`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: String`

        The ID of the uploaded file.

      - `path: String`

        The file's absolute path inside the environment.

      - `type: :file_id`

        The type of the object. Always `file_id`.

        - `:file_id`

    - `class Inline`

      Metadata for confidential inline file contents.

      - `path: String`

        The file's absolute path inside the environment.

      - `size_bytes: Integer`

        The decoded size of the inline file in bytes.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `name: String`

    An optional human-readable display name for the template.

  - `network: Network{ access, allowed_domains}`

    Runtime network access for each OpenAI-hosted environment.

    - `access: :enabled | :disabled | :restricted`

      The environment's network access mode.

      - `:enabled`

        Allows unrestricted network access.

      - `:disabled`

        Disables network access.

      - `:restricted`

        Applies the configured domain restrictions.

    - `allowed_domains: Array[String]`

      Domains the environment may access when network access is restricted.

  - `object: :"agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `:"agent.environment.template"`

  - `packages: Packages{ npm, python, system_}`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array[String]`

      npm packages installed globally in the environment.

    - `python: Array[String]`

      Python packages installed in the environment.

    - `system_: Array[String]`

      System packages installed in the environment.

  - `plugins: Array[HostedPlugin]`

    Safe plugin metadata, excluding inline archive contents.

    - `description: String`

      The installed plugin description.

    - `name: String`

      The installed plugin name.

    - `type: :inline`

      The type of the object. Always `inline`.

      - `:inline`

  - `skills: Array[SkillReference{ skill_id, type, version} | Inline{ description, name, type}]`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: String`

        The referenced skill ID.

      - `type: :skill_reference`

        The type of the object. Always `skill_reference`.

        - `:skill_reference`

      - `version: String`

        The requested version selector, including `latest`.

    - `class Inline`

      Safe metadata for an inline skill archive.

      - `description: String`

        The skill description declared in `SKILL.md`.

      - `name: String`

        The skill name declared in `SKILL.md`.

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `class EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: String`

    The ID of the deleted environment template.

  - `deleted: bool`

    Whether the environment template was deleted. Always `true`.

  - `object: :"agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `:"agent.environment.template.deleted"`

# Sessions

## Create an agent session

`beta.agents.sessions.create(**kwargs) -> AgentSession`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `environment: EnvironmentParam`

  An inline execution environment or a reference to an environment template.

  - `class None`

    Runs the agent without an execution environment.

    - `type: :none`

      The type of the object. Always `none`.

      - `:none`

  - `class OpenAIHosted`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: :openai_hosted`

      The type of the object. Always `openai_hosted`.

      - `:openai_hosted`

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size: :small | :medium | :large`

      The hosted container size. Omission selects the medium tier.

      - `:small`

      - `:medium`

      - `:large`

    - `desktop: Desktop{ enabled}`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: bool`

        Whether to provision the desktop and its browser proxy.

    - `env: Hash[Symbol, String]`

      Environment variables made available to the agent.

    - `environment_template_id: String`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files: Array[HostedEnvironmentFileParam]`

      Files available before the agent starts. Defaults to an empty list.

      - `class FileID`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: String`

          The ID of the uploaded file.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :file_id`

          The type of the object. Always `file_id`.

          - `:file_id`

      - `class Inline`

        A file supplied directly as standard-base64 data.

        - `data: String`

          The standard-base64-encoded file contents.

        - `path: String`

          The absolute destination path inside `/workspace`.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

    - `network: Network{ access, allowed_domains, blocked_domains}`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `access: :enabled | :disabled | :restricted`

        The environment's network access mode.

        - `:enabled`

          Allows unrestricted network access.

        - `:disabled`

          Disables network access.

        - `:restricted`

          Applies the configured domain restrictions.

      - `allowed_domains: Array[String]`

        Domains the environment may access when network access is restricted.

      - `blocked_domains: Array[String]`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages: Packages{ npm, python, system_}`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm: Array[String]`

        npm packages to install globally. Defaults to an empty list.

      - `python: Array[String]`

        Python packages to install. Defaults to an empty list.

      - `system_: Array[String]`

        System packages to install. Defaults to an empty list.

    - `plugins: Array[HostedPluginParam]`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: String`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: String`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: String`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: :"application/zip"`

          The archive media type, always `application/zip`.

          - `:"application/zip"`

            A ZIP archive.

        - `type: :base64`

          The type of the object. Always `base64`.

          - `:base64`

      - `type: :inline`

        The type of the object. Always `inline`.

        - `:inline`

    - `setup_commands: Array[SetupCommandParam]`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: String`

        The shell command to execute.

      - `cwd: String`

        The absolute working directory. Defaults to `/workspace`.

    - `skills: Array[HostedSkillParam]`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `class SkillReference`

        References a skill uploaded through the Skills API.

        - `skill_id: String`

          The ID of the skill created through `/v1/skills`.

        - `type: :skill_reference`

          The type of the object. Always `skill_reference`.

          - `:skill_reference`

        - `version: String`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `class Inline`

        Supplies a skill ZIP directly in the session request.

        - `description: String`

          The skill description declared in `SKILL.md`.

        - `name: String`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

  - `class SelfHosted`

    An application-hosted environment configured inline.

    - `type: :self_hosted`

      The type of the object. Always `self_hosted`.

      - `:self_hosted`

    - `workspace_directory: String`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories: Array[String]`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

- `agent: Agent{ instructions, model, multi_agent, 4 more}`

  Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

  - `instructions: String`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `model: String`

    The model to use for the agent. The requested model name is preserved.

  - `multi_agent: MultiAgentConfigParam`

    Configuration for creating and coordinating subagents.

    - `enabled: bool`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents: Integer`

      Maximum number of subagents that may run concurrently. Defaults to 6.

  - `reasoning: AgentReasoningParam`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

    - `effort: :none | :minimal | :low | 4 more`

      The amount of reasoning effort the model should use. Omission lets the model select it.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

    - `summary: :concise | :detailed | :auto`

      Controls whether the response includes a reasoning summary.

      - `:concise`

        Returns a concise reasoning summary when supported.

      - `:detailed`

        Returns a detailed reasoning summary when supported.

      - `:auto`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: :auto | :default | :flex | 3 more`

    The service tier used for model requests.

    - `:auto`

      Selects the service tier automatically.

    - `:default`

      Uses the default service tier.

    - `:flex`

      Uses the flex service tier.

    - `:priority`

      Uses the priority service tier.

    - `:fast`

      Uses the fast service tier.

    - `:ultrafast`

      Uses the ultrafast service tier.

  - `text: AgentTextParam`

    Configuration for text generated by the agent.

    - `format_: TextFormatParam`

      The output format. Omission uses ordinary text (`{"type": "text"}`).

      - `class Text`

        Generates ordinary text without a structured-output constraint.

        - `type: :text`

          The type of the object. Always `text`.

          - `:text`

      - `class JSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Hash[Symbol, untyped]`

          The JSON Schema that generated text must match.

        - `type: :json_schema`

          The type of the object. Always `json_schema`.

          - `:json_schema`

    - `verbosity: :low | :medium | :high`

      The amount of text the model should produce. Defaults to `medium`, matching Responses.

      - `:low`

        Produces less text.

      - `:medium`

        Uses the default amount of text.

      - `:high`

        Produces more text.

  - `tools: Array[AgentToolParam]`

    Tools available to the agent. Omit to inherit, or pass null to clear them.

    - `class Function`

      A function defined by the application.

      - `description: String`

        A description of what the function does.

      - `name: String`

        The name of the function.

      - `parameters: Hash[Symbol, untyped]`

        A JSON Schema object describing the function's arguments.

      - `type: :function`

        The type of the object. Always `function`.

        - `:function`

      - `defer_loading: bool`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `class ToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: :tool_search`

        The type of the object. Always `tool_search`.

        - `:tool_search`

    - `class ProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `type: :programmatic_tool_calling`

        The type of the object. Always `programmatic_tool_calling`.

        - `:programmatic_tool_calling`

      - `enabled: bool`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `class Mcp`

      Tools provided by a remote MCP server.

      - `server_label: String`

        A label used to identify the MCP server in tool calls.

      - `transport: McpTransportParam`

        The transport used to connect to the MCP server.

        - `class HTTP`

          Connects to an MCP server over HTTP.

          - `server_url: String`

            The URL of the MCP server.

          - `type: :http`

            The type of the object. Always `http`.

            - `:http`

          - `authorization: String`

            The authorization value sent to the MCP server, if any.

          - `headers: Hash[Symbol, String]`

            Additional HTTP headers sent to the MCP server.

        - `class Stdio`

          Starts an MCP server as a local process.

          - `command: String`

            The command used to start the MCP server.

          - `cwd: String`

            The working directory used to start the MCP server.

          - `type: :stdio`

            The type of the object. Always `stdio`.

            - `:stdio`

          - `args: Array[String]`

            Arguments passed to the MCP server command.

          - `env: Hash[Symbol, String]`

            Environment variables set for the MCP server process.

          - `env_vars: Array[String]`

            Environment variable names to inherit from the selected execution environment.

      - `type: :mcp`

        The type of the object. Always `mcp`.

        - `:mcp`

      - `allowed_tools: Array[String]`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin: :service | :environment`

        Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

        - `:service`

          Uses the Managed Agents service network.

        - `:environment`

          Uses the session's execution environment.

      - `credential_id: String`

        The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

      - `request_metadata: Hash[Symbol, untyped]`

        Metadata included with requests to this MCP server.

      - `required: bool`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `class WebSearch`

      Web search.

      - `type: :web_search`

        The type of the object. Always `web_search`.

        - `:web_search`

      - `allowed_domains: Array[String]`

        Domains the search may include.

      - `context_size: :low | :medium | :high`

        The amount of search context made available to the model. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

      - `location: Location{ city, country, region, timezone}`

        Approximate location used to localize search results.

        - `city: String`

          The city name.

        - `country: String`

          The two-letter ISO country code, such as `US`.

        - `region: String`

          The region or state name.

        - `timezone: String`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: :disabled | :cached | :live`

        The source used for web search results. Defaults to `live`.

        - `:disabled`

          Disables web search.

        - `:cached`

          Uses cached search results.

        - `:live`

          Searches the live web.

    - `class ComputerUse`

      Browser use in an OpenAI-hosted session.

      - `type: :computer_use`

        The type of the object. Always `computer_use`.

        - `:computer_use`

      - `include_screenshots: bool`

        Whether computer tool outputs include screenshots. Defaults to `false`.

- `agent_id: String`

  The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

- `input: String | Array[AgentSessionInputMessageParam]`

  Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

  - `String = String`

  - `UnionMember1 = Array[AgentSessionInputMessageParam]`

    - `content: Array[InputContentParam]`

      The content of the message.

      - `class InputText`

        Text input to the model.

        - `text: String`

          The text sent to the model.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        Image input to the model.

        - `image_url: String`

          The URL of the image sent to the model.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

    - `role: :user`

      The role of the message author. Always `user`.

      - `:user`

    - `type: :message`

      The type of the input item. Always `message`.

      - `:message`

- `metadata: Hash[Symbol, String]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

- `stream: bool`

  Whether to stream session events as server-sent events. Defaults to `false`.

- `vault_ids: Array[String]`

  The IDs of vaults made available to the session.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: :none | :minimal | :low | 4 more`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `summary: :concise | :detailed | :auto`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `:concise`

          Returns a concise reasoning summary when supported.

        - `:detailed`

          Returns a detailed reasoning summary when supported.

        - `:auto`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: :auto | :default | :flex | 3 more`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

      - `format_: TextFormat`

        The effective output format. Defaults to ordinary text.

        - `class Text`

          Generates ordinary text without a structured-output constraint.

          - `type: :text`

            The type of the object. Always `text`.

            - `:text`

        - `class JSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Hash[Symbol, untyped]`

            The JSON Schema that generated text must match.

          - `type: :json_schema`

            The type of the object. Always `json_schema`.

            - `:json_schema`

      - `verbosity: :low | :medium | :high`

        The amount of text produced by the agent. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

    - `tools: Array[AgentTool]`

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

      - `class ProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: :programmatic_tool_calling`

          The type of the object. Always `programmatic_tool_calling`.

          - `:programmatic_tool_calling`

      - `class Mcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array[String]`

          The MCP tools the agent may call.

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

            - `type: :stdio`

              The type of the object. Always `stdio`.

              - `:stdio`

        - `type: :mcp`

          The type of the object. Always `mcp`.

          - `:mcp`

      - `class WebSearch`

        Web search.

        - `allowed_domains: Array[String]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: :disabled | :cached | :live`

          The source used for web search results.

          - `:disabled`

          - `:cached`

          - `:live`

        - `type: :web_search`

          The type of the object. Always `web_search`.

          - `:web_search`

      - `class ComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: :computer_use`

          The type of the object. Always `computer_use`.

          - `:computer_use`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

        - `access: :enabled | :disabled | :restricted`

          The environment's network access mode.

          - `:enabled`

            Allows unrestricted network access.

          - `:disabled`

            Disables network access.

          - `:restricted`

            Applies the configured domain restrictions.

        - `allowed_domains: Array[String]`

          Domains the environment may access when network access is restricted.

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.create(environment: {type: :none})

puts(agent_session)
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

`beta.agents.sessions.delete(session_id) -> AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

### Returns

- `class AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: String`

    The ID of the deleted session.

  - `deleted: bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: :"agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `:"agent.session.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session_deleted = openai.beta.agents.sessions.delete("session_id")

puts(agent_session_deleted)
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

`beta.agents.sessions.list(**kwargs) -> CursorPage<AgentSession>`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `after: String`

  Return resources after this resource ID in the selected order.

- `agent_id: String`

  Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

- `limit: Integer`

  The maximum number of resources to return.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: :none | :minimal | :low | 4 more`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `summary: :concise | :detailed | :auto`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `:concise`

          Returns a concise reasoning summary when supported.

        - `:detailed`

          Returns a detailed reasoning summary when supported.

        - `:auto`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: :auto | :default | :flex | 3 more`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

      - `format_: TextFormat`

        The effective output format. Defaults to ordinary text.

        - `class Text`

          Generates ordinary text without a structured-output constraint.

          - `type: :text`

            The type of the object. Always `text`.

            - `:text`

        - `class JSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Hash[Symbol, untyped]`

            The JSON Schema that generated text must match.

          - `type: :json_schema`

            The type of the object. Always `json_schema`.

            - `:json_schema`

      - `verbosity: :low | :medium | :high`

        The amount of text produced by the agent. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

    - `tools: Array[AgentTool]`

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

      - `class ProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: :programmatic_tool_calling`

          The type of the object. Always `programmatic_tool_calling`.

          - `:programmatic_tool_calling`

      - `class Mcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array[String]`

          The MCP tools the agent may call.

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

            - `type: :stdio`

              The type of the object. Always `stdio`.

              - `:stdio`

        - `type: :mcp`

          The type of the object. Always `mcp`.

          - `:mcp`

      - `class WebSearch`

        Web search.

        - `allowed_domains: Array[String]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: :disabled | :cached | :live`

          The source used for web search results.

          - `:disabled`

          - `:cached`

          - `:live`

        - `type: :web_search`

          The type of the object. Always `web_search`.

          - `:web_search`

      - `class ComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: :computer_use`

          The type of the object. Always `computer_use`.

          - `:computer_use`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

        - `access: :enabled | :disabled | :restricted`

          The environment's network access mode.

          - `:enabled`

            Allows unrestricted network access.

          - `:disabled`

            Disables network access.

          - `:restricted`

            Applies the configured domain restrictions.

        - `allowed_domains: Array[String]`

          Domains the environment may access when network access is restricted.

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.list

puts(page)
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

`beta.agents.sessions.retrieve(session_id) -> AgentSession`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: :none | :minimal | :low | 4 more`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `summary: :concise | :detailed | :auto`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `:concise`

          Returns a concise reasoning summary when supported.

        - `:detailed`

          Returns a detailed reasoning summary when supported.

        - `:auto`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: :auto | :default | :flex | 3 more`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

      - `format_: TextFormat`

        The effective output format. Defaults to ordinary text.

        - `class Text`

          Generates ordinary text without a structured-output constraint.

          - `type: :text`

            The type of the object. Always `text`.

            - `:text`

        - `class JSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Hash[Symbol, untyped]`

            The JSON Schema that generated text must match.

          - `type: :json_schema`

            The type of the object. Always `json_schema`.

            - `:json_schema`

      - `verbosity: :low | :medium | :high`

        The amount of text produced by the agent. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

    - `tools: Array[AgentTool]`

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

      - `class ProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: :programmatic_tool_calling`

          The type of the object. Always `programmatic_tool_calling`.

          - `:programmatic_tool_calling`

      - `class Mcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array[String]`

          The MCP tools the agent may call.

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

            - `type: :stdio`

              The type of the object. Always `stdio`.

              - `:stdio`

        - `type: :mcp`

          The type of the object. Always `mcp`.

          - `:mcp`

      - `class WebSearch`

        Web search.

        - `allowed_domains: Array[String]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: :disabled | :cached | :live`

          The source used for web search results.

          - `:disabled`

          - `:cached`

          - `:live`

        - `type: :web_search`

          The type of the object. Always `web_search`.

          - `:web_search`

      - `class ComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: :computer_use`

          The type of the object. Always `computer_use`.

          - `:computer_use`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

        - `access: :enabled | :disabled | :restricted`

          The environment's network access mode.

          - `:enabled`

            Allows unrestricted network access.

          - `:disabled`

            Disables network access.

          - `:restricted`

            Applies the configured domain restrictions.

        - `allowed_domains: Array[String]`

          Domains the environment may access when network access is restricted.

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.retrieve("session_id")

puts(agent_session)
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

`beta.agents.sessions.update(session_id, **kwargs) -> AgentSession`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `session_id: String`

- `agent: Agent{ model, reasoning, service_tier}`

  Model settings for subsequent turns. Omitted fields stay unchanged.

  - `model: String`

    The model for subsequent turns. Omit to keep the current model.

  - `reasoning: Reasoning{ effort}`

    Reasoning settings to update. Omit to keep the current effort.

    - `effort: :none | :minimal | :low | 4 more`

      Omit to keep the current effort. Null selects the model's default effort.

      - `:none`

      - `:minimal`

      - `:low`

      - `:medium`

      - `:high`

      - `:xhigh`

      - `:max`

  - `service_tier: :auto | :default | :flex | 3 more`

    Omit to keep the current tier. Null resets it to auto.

    - `:auto`

      Selects the service tier automatically.

    - `:default`

      Uses the default service tier.

    - `:flex`

      Uses the flex service tier.

    - `:priority`

      Uses the priority service tier.

    - `:fast`

      Uses the fast service tier.

    - `:ultrafast`

      Uses the ultrafast service tier.

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class AgentSession`

  A Managed Agents session.

  - `id: String`

    The ID of the session.

  - `agent: Agent{ id, instructions, model, 6 more}`

    The agent running in the session.

    - `id: String`

      The ID of the agent.

    - `instructions: String`

      Custom instructions appended to the agent's default base instructions.

    - `model: String`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: bool`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: Integer`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: String`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: :none | :minimal | :low | 4 more`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `:none`

        - `:minimal`

        - `:low`

        - `:medium`

        - `:high`

        - `:xhigh`

        - `:max`

      - `summary: :concise | :detailed | :auto`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `:concise`

          Returns a concise reasoning summary when supported.

        - `:detailed`

          Returns a detailed reasoning summary when supported.

        - `:auto`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: :auto | :default | :flex | 3 more`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `:auto`

      - `:default`

      - `:flex`

      - `:priority`

      - `:fast`

      - `:ultrafast`

    - `text: AgentText`

      Configuration for text generated by the agent.

      - `format_: TextFormat`

        The effective output format. Defaults to ordinary text.

        - `class Text`

          Generates ordinary text without a structured-output constraint.

          - `type: :text`

            The type of the object. Always `text`.

            - `:text`

        - `class JSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Hash[Symbol, untyped]`

            The JSON Schema that generated text must match.

          - `type: :json_schema`

            The type of the object. Always `json_schema`.

            - `:json_schema`

      - `verbosity: :low | :medium | :high`

        The amount of text produced by the agent. Defaults to `medium`.

        - `:low`

        - `:medium`

        - `:high`

    - `tools: Array[AgentTool]`

      Tools available to the agent.

      - `class Function`

        A function defined by the application.

        - `defer_loading: bool`

          Whether the function is deferred and discovered through tool search.

        - `description: String`

          A description of what the function does.

        - `name: String`

          The name of the function.

        - `parameters: Hash[Symbol, untyped]`

          A JSON Schema object describing the function's arguments.

        - `type: :function`

          The type of the object. Always `function`.

          - `:function`

      - `class ProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: bool`

          Whether tools can be called from model-generated code.

        - `type: :programmatic_tool_calling`

          The type of the object. Always `programmatic_tool_calling`.

          - `:programmatic_tool_calling`

      - `class Mcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array[String]`

          The MCP tools the agent may call.

        - `connection_origin: :service | :environment`

          Where outbound MCP HTTP connections originate.

          - `:service`

          - `:environment`

        - `credential_id: String`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Hash[Symbol, untyped]`

          Metadata included with requests to this MCP server.

        - `required: bool`

          Whether this MCP server must initialize before the first turn.

        - `server_label: String`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `class HTTP`

            Connects to an MCP server over HTTP.

            - `server_url: String`

              The URL of the MCP server.

            - `type: :http`

              The type of the object. Always `http`.

              - `:http`

          - `class Stdio`

            Starts an MCP server as a local process.

            - `args: Array[String]`

              Arguments passed to the MCP server command.

            - `command: String`

              The command used to start the MCP server.

            - `cwd: String`

              The working directory used to start the MCP server.

            - `env_vars: Array[String]`

              Environment variable names inherited from the execution environment.

            - `type: :stdio`

              The type of the object. Always `stdio`.

              - `:stdio`

        - `type: :mcp`

          The type of the object. Always `mcp`.

          - `:mcp`

      - `class WebSearch`

        Web search.

        - `allowed_domains: Array[String]`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: :low | :medium | :high`

          The amount of search context made available to the model. Defaults to `medium`.

          - `:low`

          - `:medium`

          - `:high`

        - `location: Location{ city, country, region, timezone}`

          Approximate location used to localize search results, if provided.

          - `city: String`

            The city name.

          - `country: String`

            The two-letter ISO country code, such as `US`.

          - `region: String`

            The region or state name.

          - `timezone: String`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: :disabled | :cached | :live`

          The source used for web search results.

          - `:disabled`

          - `:cached`

          - `:live`

        - `type: :web_search`

          The type of the object. Always `web_search`.

          - `:web_search`

      - `class ComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: bool`

          Whether computer tool outputs include screenshots.

        - `type: :computer_use`

          The type of the object. Always `computer_use`.

          - `:computer_use`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `class None`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: :none`

        The type of the object. Always `none`.

        - `:none`

    - `class OpenAIHosted`

      An environment hosted by OpenAI.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop{ enabled}`

        The effective desktop configuration.

        - `enabled: bool`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array[HostedEnvironmentFile]`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `file_id: String`

            The ID of the uploaded file.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :file_id`

            The type of the object. Always `file_id`.

            - `:file_id`

        - `class Inline`

          A file supplied inline when the session was created.

          - `id: String`

            The session-scoped ID of the file in the execution environment.

          - `path: String`

            The file's absolute path inside the environment.

          - `size_bytes: Integer`

            The decoded file size in bytes.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `network: Network{ access, allowed_domains}`

        The effective network access policy for the environment.

        - `access: :enabled | :disabled | :restricted`

          The environment's network access mode.

          - `:enabled`

            Allows unrestricted network access.

          - `:disabled`

            Disables network access.

          - `:restricted`

            Applies the configured domain restrictions.

        - `allowed_domains: Array[String]`

          Domains the environment may access when network access is restricted.

      - `packages: Packages{ npm, python, system_}`

        Packages installed in the environment.

        - `npm: Array[String]`

          npm packages installed globally in the environment.

        - `python: Array[String]`

          Python packages installed in the environment.

        - `system_: Array[String]`

          System packages installed in the environment.

      - `plugins: Array[HostedPlugin]`

        Plugins installed in the environment, excluding their archive contents.

        - `description: String`

          The installed plugin description.

        - `name: String`

          The installed plugin name.

        - `type: :inline`

          The type of the object. Always `inline`.

          - `:inline`

      - `skills: Array[HostedSkill]`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference`

          A skill installed from the Skills API.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `skill_id: String`

            The referenced skill ID.

          - `type: :skill_reference`

            The type of the object. Always `skill_reference`.

            - `:skill_reference`

          - `version: String`

            The concrete skill version installed for this session.

        - `class Inline`

          A skill installed from an inline ZIP archive.

          - `description: String`

            The installed skill description.

          - `name: String`

            The installed skill name.

          - `type: :inline`

            The type of the object. Always `inline`.

            - `:inline`

      - `type: :openai_hosted`

        The type of the object. Always `openai_hosted`.

        - `:openai_hosted`

      - `container_size: :small | :medium | :large`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `:small`

        - `:medium`

        - `:large`

    - `class SelfHosted`

      An environment hosted by the application.

      - `id: String`

        The public ID of the environment.

      - `capability_directories: Array[String]`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: String`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: :self_hosted`

        The type of the object. Always `self_hosted`.

        - `:self_hosted`

      - `workspace_directory: String`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: String`

    The error that caused the session to fail, if any.

  - `last_active_at: Integer`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Hash[Symbol, String]`

    Custom string key-value pairs attached to the session.

  - `object: :"agent.session"`

    The object type. Always `agent.session`.

    - `:"agent.session"`

  - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

        The information needed to render the request.

        - `class BrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `class BrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: String`

            The origin the browser needs permission to access.

          - `reason: String`

            The browser's explanation for this request, or null when unavailable.

          - `type: :browser_origin_access`

            The type of the object. Always `browser_origin_access`.

            - `:browser_origin_access`

      - `request_id: String`

        The registered request ID to echo when responding.

      - `turn_id: String`

        The turn that requested approval.

      - `type: :computer_use_approval_request`

        The type of the object. Always `computer_use_approval_request`.

        - `:computer_use_approval_request`

    - `class FunctionCall`

      Run a function tool and submit its result.

      - `arguments: untyped`

        The arguments supplied by the model.

      - `call_id: String`

        The ID to include when submitting the function result.

      - `name: String`

        The function name.

      - `turn_id: String`

        The ID of the turn that requested the function call.

      - `type: :function_call`

        The type of the object. Always `function_call`.

        - `:function_call`

    - `class EnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: String`

        The ID of the environment to reconnect.

      - `type: :environment_connection`

        The type of the object. Always `environment_connection`.

        - `:environment_connection`

  - `status: :idle | :in_progress | :requires_action | :failed`

    The current status of the session.

    - `:idle`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `:in_progress`

      The session is processing a turn.

    - `:requires_action`

      The session is waiting for one or more required actions.

    - `:failed`

      The session failed.

  - `usage: TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array[String]`

    The IDs of vaults made available to the session.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session = openai.beta.agents.sessions.update("session_id")

puts(agent_session)
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

`beta.agents.sessions.artifacts.content(artifact_id, **kwargs) -> StringIO`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `StringIO`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

response = openai.beta.agents.sessions.artifacts.content("artifact_id", session_id: "session_id")

puts(response)
```

## Delete an agent session artifact

`beta.agents.sessions.artifacts.delete(artifact_id, **kwargs) -> SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact_deleted = openai.beta.agents.sessions.artifacts.delete("artifact_id", session_id: "session_id")

puts(session_artifact_deleted)
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

`beta.agents.sessions.artifacts.list(session_id, **kwargs) -> CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `after: String`

  Return artifacts after this immutable artifact ID.

- `environment_id: String`

  Restrict the listing to artifacts produced by this environment.

- `limit: Integer`

  The maximum number of artifacts to return, between 1 and 100.

- `order: :asc | :desc`

  Sort by creation time and ID. Defaults to descending.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.artifacts.list("session_id")

puts(page)
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

`beta.agents.sessions.artifacts.retrieve(artifact_id, **kwargs) -> SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `session_id: String`

- `artifact_id: String`

### Returns

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

session_artifact = openai.beta.agents.sessions.artifacts.retrieve("artifact_id", session_id: "session_id")

puts(session_artifact)
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

- `class SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: String`

    The immutable artifact ID.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: String`

    The ID of the environment that produced the artifact.

  - `object: :"agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `:"agent.session.artifact"`

  - `path: String`

    The original absolute file path in the execution environment.

  - `session_id: String`

    The ID of the session that owns the artifact.

  - `size_bytes: Integer`

    The immutable artifact size in bytes.

  - `turn_id: String`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `class SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: String`

    The ID of the deleted session artifact.

  - `deleted: bool`

    Whether the session artifact was deleted. Always `true`.

  - `object: :"agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `:"agent.session.artifact.deleted"`

# Events

## Create agent session input events

`beta.agents.sessions.events.create(session_id, **kwargs) -> void`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: String`

- `events: Array[AgentSessionInputParam]`

  The input events to submit to the session.

  - `class AgentSessionInputComputerUseApprovalRequestResult`

    Responds to a pending Computer Use approval request.

    - `request_id: String`

      The registered request ID from the required action.

    - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam`

        - `action: :submit`

          - `:submit`

        - `fields: Array[Field{ field_id, value}]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: String`

            The field ID from the required action.

          - `value: String`

            The value to enter into the registered control.

        - `type: :browser_authentication`

          - `:browser_authentication`

        - `selected_option: String`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class AgentBrowserOriginAccessParam`

        - `decision: :approve | :deny | :cancel`

          Whether to allow, deny, or cancel the requested origin access.

          - `:approve`

            Allow the browser to access this origin.

          - `:deny`

            Deny access to this origin.

          - `:cancel`

            Dismiss this request without approving access.

        - `type: :browser_origin_access`

          - `:browser_origin_access`

    - `type: :"agent.session.input.computer_use_approval_request_result"`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `:"agent.session.input.computer_use_approval_request_result"`

  - `class AgentSessionInputMessage`

    Adds one or more user messages and starts a turn.

    - `input: Array[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: Array[InputContentParam]`

        The content of the message.

        - `class InputText`

          Text input to the model.

          - `text: String`

            The text sent to the model.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input to the model.

          - `image_url: String`

            The URL of the image sent to the model.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

      - `role: :user`

        The role of the message author. Always `user`.

        - `:user`

      - `type: :message`

        The type of the input item. Always `message`.

        - `:message`

    - `type: :"agent.session.input.message"`

      The type of the object. Always `agent.session.input.message`.

      - `:"agent.session.input.message"`

  - `class AgentSessionInputCancel`

    Cancels the session's active turn.

    - `type: :"agent.session.input.cancel"`

      The type of the object. Always `agent.session.input.cancel`.

      - `:"agent.session.input.cancel"`

  - `class AgentSessionInputToolResult`

    Submits the result of a function call.

    - `call_id: String`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: String`

      The ID of the turn that requested the function call.

    - `type: :"agent.session.input.tool_result"`

      The type of the object. Always `agent.session.input.tool_result`.

      - `:"agent.session.input.tool_result"`

    - `error: String`

      The error message when the call failed.

    - `output: AgentFunctionCallOutputParam`

      The function result when the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContentParam]`

        - `class InputText`

          Text input to the model.

        - `class InputImage`

          Image input to the model.

- `idempotency_key: String`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.beta.agents.sessions.events.create(
  "session_id",
  events: [
    {
      request_id: "request_id",
      response: {action: "submit", fields: [{field_id: "field_id", value: "value"}], type: :browser_authentication},
      type: :"agent.session.input.computer_use_approval_request_result"
    }
  ]
)

puts(result)
```

## Stream agent session events

`beta.agents.sessions.events.stream(session_id) -> AgentSessionEvent`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `session_id: String`

### Returns

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: String`

        The machine-readable error code, if any.

      - `message: String`

        A customer-safe explanation of the error.

      - `param: String`

        The request parameter associated with the error, if any.

      - `type: String`

        The error type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `type: :error`

      The type of the object. Always `error`.

      - `:error`

  - `class AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: String`

        The public ID of the environment.

      - `error: Error{ code, message, type}`

        The error reported while preparing the environment, if any.

        - `code: String`

          A machine-readable error code.

        - `message: String`

          A human-readable error message.

        - `type: String`

          The error type.

      - `status: :pending | :ready | :connected | 2 more`

        The environment's connection status.

        - `:pending`

          The environment is being prepared.

        - `:ready`

          The environment is ready to connect.

        - `:connected`

          The environment is connected.

        - `:disconnected`

          The environment is disconnected.

        - `:failed`

          The environment failed to connect.

      - `type: String`

        The environment type.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `:"agent.session.environment.ready"`

  - `class AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: String`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: String`

      The unique ID of the event.

    - `reset_count: Integer`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The associated turn, when applicable.

    - `type: :"agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `:"agent.session.environment.reset"`

  - `class AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: String`

      The output text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the command execution item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `:"agent.output.command_execution_output.delta"`

  - `class AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: String`

        The ID of the session.

      - `agent: Agent{ id, instructions, model, 6 more}`

        The agent running in the session.

        - `id: String`

          The ID of the agent.

        - `instructions: String`

          Custom instructions appended to the agent's default base instructions.

        - `model: String`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: bool`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: Integer`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: String`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

          - `effort: :none | :minimal | :low | 4 more`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `:none`

            - `:minimal`

            - `:low`

            - `:medium`

            - `:high`

            - `:xhigh`

            - `:max`

          - `summary: :concise | :detailed | :auto`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `:concise`

              Returns a concise reasoning summary when supported.

            - `:detailed`

              Returns a detailed reasoning summary when supported.

            - `:auto`

              Automatically selects the most detailed summary supported by the model.

        - `service_tier: :auto | :default | :flex | 3 more`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `:auto`

          - `:default`

          - `:flex`

          - `:priority`

          - `:fast`

          - `:ultrafast`

        - `text: AgentText`

          Configuration for text generated by the agent.

          - `format_: TextFormat`

            The effective output format. Defaults to ordinary text.

            - `class Text`

              Generates ordinary text without a structured-output constraint.

              - `type: :text`

                The type of the object. Always `text`.

                - `:text`

            - `class JSONSchema`

              Constrains generated text to a JSON Schema.

              - `schema: Hash[Symbol, untyped]`

                The JSON Schema that generated text must match.

              - `type: :json_schema`

                The type of the object. Always `json_schema`.

                - `:json_schema`

          - `verbosity: :low | :medium | :high`

            The amount of text produced by the agent. Defaults to `medium`.

            - `:low`

            - `:medium`

            - `:high`

        - `tools: Array[AgentTool]`

          Tools available to the agent.

          - `class Function`

            A function defined by the application.

            - `defer_loading: bool`

              Whether the function is deferred and discovered through tool search.

            - `description: String`

              A description of what the function does.

            - `name: String`

              The name of the function.

            - `parameters: Hash[Symbol, untyped]`

              A JSON Schema object describing the function's arguments.

            - `type: :function`

              The type of the object. Always `function`.

              - `:function`

          - `class ProgrammaticToolCalling`

            Enables calling tools from model-generated code.

            - `enabled: bool`

              Whether tools can be called from model-generated code.

            - `type: :programmatic_tool_calling`

              The type of the object. Always `programmatic_tool_calling`.

              - `:programmatic_tool_calling`

          - `class Mcp`

            Tools provided by a remote MCP server.

            - `allowed_tools: Array[String]`

              The MCP tools the agent may call.

            - `connection_origin: :service | :environment`

              Where outbound MCP HTTP connections originate.

              - `:service`

              - `:environment`

            - `credential_id: String`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Hash[Symbol, untyped]`

              Metadata included with requests to this MCP server.

            - `required: bool`

              Whether this MCP server must initialize before the first turn.

            - `server_label: String`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `class HTTP`

                Connects to an MCP server over HTTP.

                - `server_url: String`

                  The URL of the MCP server.

                - `type: :http`

                  The type of the object. Always `http`.

                  - `:http`

              - `class Stdio`

                Starts an MCP server as a local process.

                - `args: Array[String]`

                  Arguments passed to the MCP server command.

                - `command: String`

                  The command used to start the MCP server.

                - `cwd: String`

                  The working directory used to start the MCP server.

                - `env_vars: Array[String]`

                  Environment variable names inherited from the execution environment.

                - `type: :stdio`

                  The type of the object. Always `stdio`.

                  - `:stdio`

            - `type: :mcp`

              The type of the object. Always `mcp`.

              - `:mcp`

          - `class WebSearch`

            Web search.

            - `allowed_domains: Array[String]`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: :low | :medium | :high`

              The amount of search context made available to the model. Defaults to `medium`.

              - `:low`

              - `:medium`

              - `:high`

            - `location: Location{ city, country, region, timezone}`

              Approximate location used to localize search results, if provided.

              - `city: String`

                The city name.

              - `country: String`

                The two-letter ISO country code, such as `US`.

              - `region: String`

                The region or state name.

              - `timezone: String`

                The IANA timezone, such as `America/Los_Angeles`.

            - `mode: :disabled | :cached | :live`

              The source used for web search results.

              - `:disabled`

              - `:cached`

              - `:live`

            - `type: :web_search`

              The type of the object. Always `web_search`.

              - `:web_search`

          - `class ComputerUse`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: bool`

              Whether computer tool outputs include screenshots.

            - `type: :computer_use`

              The type of the object. Always `computer_use`.

              - `:computer_use`

      - `created_at: Integer`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `class None`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class OpenAIHosted`

          An environment hosted by OpenAI.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `desktop: Desktop{ enabled}`

            The effective desktop configuration.

            - `enabled: bool`

              Whether the environment provisions a desktop and browser proxy.

          - `files: Array[HostedEnvironmentFile]`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileID`

              A file copied from the OpenAI Files API.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `file_id: String`

                The ID of the uploaded file.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :file_id`

                The type of the object. Always `file_id`.

                - `:file_id`

            - `class Inline`

              A file supplied inline when the session was created.

              - `id: String`

                The session-scoped ID of the file in the execution environment.

              - `path: String`

                The file's absolute path inside the environment.

              - `size_bytes: Integer`

                The decoded file size in bytes.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `network: Network{ access, allowed_domains}`

            The effective network access policy for the environment.

            - `access: :enabled | :disabled | :restricted`

              The environment's network access mode.

              - `:enabled`

                Allows unrestricted network access.

              - `:disabled`

                Disables network access.

              - `:restricted`

                Applies the configured domain restrictions.

            - `allowed_domains: Array[String]`

              Domains the environment may access when network access is restricted.

          - `packages: Packages{ npm, python, system_}`

            Packages installed in the environment.

            - `npm: Array[String]`

              npm packages installed globally in the environment.

            - `python: Array[String]`

              Python packages installed in the environment.

            - `system_: Array[String]`

              System packages installed in the environment.

          - `plugins: Array[HostedPlugin]`

            Plugins installed in the environment, excluding their archive contents.

            - `description: String`

              The installed plugin description.

            - `name: String`

              The installed plugin name.

            - `type: :inline`

              The type of the object. Always `inline`.

              - `:inline`

          - `skills: Array[HostedSkill]`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference`

              A skill installed from the Skills API.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `skill_id: String`

                The referenced skill ID.

              - `type: :skill_reference`

                The type of the object. Always `skill_reference`.

                - `:skill_reference`

              - `version: String`

                The concrete skill version installed for this session.

            - `class Inline`

              A skill installed from an inline ZIP archive.

              - `description: String`

                The installed skill description.

              - `name: String`

                The installed skill name.

              - `type: :inline`

                The type of the object. Always `inline`.

                - `:inline`

          - `type: :openai_hosted`

            The type of the object. Always `openai_hosted`.

            - `:openai_hosted`

          - `container_size: :small | :medium | :large`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `:small`

            - `:medium`

            - `:large`

        - `class SelfHosted`

          An environment hosted by the application.

          - `id: String`

            The public ID of the environment.

          - `capability_directories: Array[String]`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: String`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: :self_hosted`

            The type of the object. Always `self_hosted`.

            - `:self_hosted`

          - `workspace_directory: String`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: String`

        The error that caused the session to fail, if any.

      - `last_active_at: Integer`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Hash[Symbol, String]`

        Custom string key-value pairs attached to the session.

      - `object: :"agent.session"`

        The object type. Always `agent.session`.

        - `:"agent.session"`

      - `required_actions: Array[ComputerUseApprovalRequest{ request, request_id, turn_id, type} | FunctionCall{ arguments, call_id, name, 2 more} | EnvironmentConnection{ environment_id, type}]`

        Actions that must be completed before the session can continue.

        - `class ComputerUseApprovalRequest`

          Respond to a computer-use request.

          - `request: BrowserAuthentication{ credential_origin, fields, options, 2 more} | BrowserOriginAccess{ origin, reason, type}`

            The information needed to render the request.

            - `class BrowserAuthentication`

              A registered form awaiting the application's response.

              - `credential_origin: String`

                The registered form or frame origin where values will be entered.

              - `fields: Array[Field{ id, label, required, type}]`

                Controls to render. All submitted values are sensitive.

                - `id: String`

                  The field ID to submit as field_id in a fields entry.

                - `label: String`

                  The label to display beside the control.

                - `required: bool`

                  Whether this control requires a nonempty value.

                - `type: String`

                  The rendering type, such as email, password, or text.

              - `options: Array[Option{ id, field_ids, label}]`

                Sign-in methods. Empty for a plain form.

                - `id: String`

                  The option ID to submit as selected_option.

                - `field_ids: Array[String]`

                  IDs from the registered fields that this method accepts.

                - `label: String`

                  The method label to display.

              - `reason: String`

                Why the agent needs the user to sign in.

              - `type: :browser_authentication`

                The type of the object. Always `browser_authentication`.

                - `:browser_authentication`

            - `class BrowserOriginAccess`

              A browser origin awaiting the application's approval decision.

              - `origin: String`

                The origin the browser needs permission to access.

              - `reason: String`

                The browser's explanation for this request, or null when unavailable.

              - `type: :browser_origin_access`

                The type of the object. Always `browser_origin_access`.

                - `:browser_origin_access`

          - `request_id: String`

            The registered request ID to echo when responding.

          - `turn_id: String`

            The turn that requested approval.

          - `type: :computer_use_approval_request`

            The type of the object. Always `computer_use_approval_request`.

            - `:computer_use_approval_request`

        - `class FunctionCall`

          Run a function tool and submit its result.

          - `arguments: untyped`

            The arguments supplied by the model.

          - `call_id: String`

            The ID to include when submitting the function result.

          - `name: String`

            The function name.

          - `turn_id: String`

            The ID of the turn that requested the function call.

          - `type: :function_call`

            The type of the object. Always `function_call`.

            - `:function_call`

        - `class EnvironmentConnection`

          Reconnect a session environment.

          - `environment_id: String`

            The ID of the environment to reconnect.

          - `type: :environment_connection`

            The type of the object. Always `environment_connection`.

            - `:environment_connection`

      - `status: :idle | :in_progress | :requires_action | :failed`

        The current status of the session.

        - `:idle`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `:in_progress`

          The session is processing a turn.

        - `:requires_action`

          The session is waiting for one or more required actions.

        - `:failed`

          The session failed.

      - `usage: TokenUsage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: Integer`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails{ cached_tokens}`

          A breakdown of the agent's input token usage.

          - `cached_tokens: Integer`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: Integer`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: Integer`

            The number of output tokens used for reasoning.

        - `total_tokens: Integer`

          The total number of input and output tokens used by the agent.

      - `vault_ids: Array[String]`

        The IDs of vaults made available to the session.

    - `type: :"agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `:"agent.session.created"`

  - `class AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: String`

        The ID of the turn.

      - `agent_id: String`

        The ID of the agent that ran the turn.

      - `completed_at: Integer`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: Integer`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError`

        A customer-safe error. Non-null only for a failed turn.

        - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

          A stable, machine-readable failure category.

          - `:context_length_exceeded`

            The request exceeds the model's context window.

          - `:session_budget_exceeded`

            The session has reached its usage budget.

          - `:usage_limit_exceeded`

            The organization has reached a usage, plan, or billing limit.

          - `:credit_balance_exhausted`

            The organization has no API credits remaining.

          - `:rate_limit_exceeded`

            The request exceeds the available rate limit.

          - `:flex_unavailable`

            Flex processing is temporarily unavailable.

          - `:server_overloaded`

            The model service is temporarily overloaded.

          - `:cyber_policy`

            The request was rejected by a safety policy.

          - `:misalignment_policy_violation`

            The request was blocked by the safety systems.

          - `:connection_failed`

            The request could not connect to the model service.

          - `:server_error`

            The model service encountered an unexpected error.

          - `:authentication_error`

            The API credentials are invalid or lack the required access.

          - `:invalid_request`

            The request contains invalid input or configuration.

          - `:resource_not_found`

            The requested model or resource is unavailable.

          - `:sandbox_error`

            The request could not complete in its execution environment.

          - `:executor_version_incompatible`

            The executor must be upgraded before it can run this turn.

          - `:active_turn_not_steerable`

            The session cannot accept additional input while a request is running.

          - `:request_timeout`

            The request timed out before the model service responded.

          - `:internal_error`

            An unexpected internal error prevented the session request from completing.

        - `message: String`

          A customer-safe explanation of the failure.

      - `object: :"agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `:"agent.session.turn"`

      - `session_id: String`

        The ID of the session that owns the turn.

      - `started_at: Integer`

        The Unix timestamp, in seconds, when the turn started.

      - `status: :queued | :in_progress | :waiting | 3 more`

        The current status of the turn.

        - `:queued`

          The turn is waiting to start.

        - `:in_progress`

          The turn is in progress.

        - `:waiting`

          The turn is waiting for external input.

        - `:completed`

          The turn completed successfully.

        - `:failed`

          The turn failed.

        - `:cancelled`

          The turn was cancelled.

      - `subagent_id: String`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `:"agent.session.turn.created"`

  - `class AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `:"agent.session.turn.in_progress"`

  - `class AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `:"agent.session.turn.completed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `:"agent.session.turn.failed"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: String`

      The ID of the turn associated with the event.

    - `type: :"agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `:"agent.session.turn.cancelled"`

    - `usage: TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `class AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: String`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array[AgentSessionMessageContent]`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `class InputText`

            Text supplied by the user.

            - `text: String`

              The text supplied by the user.

            - `type: :input_text`

              The type of the object. Always `input_text`.

              - `:input_text`

          - `class InputImage`

            An image supplied by the user.

            - `image_url: String`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: :input_image`

              The type of the object. Always `input_image`.

              - `:input_image`

          - `class OutputText`

            Text produced by the assistant.

            - `text: String`

              The text produced by the assistant.

            - `type: :output_text`

              The type of the object. Always `output_text`.

              - `:output_text`

        - `phase: :commentary | :final_answer`

          The phase of an assistant message. Null for user messages.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :user | :assistant`

          The role of the message author.

          - `:user`

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `:in_progress`

            The item is in progress.

          - `:completed`

            The item is complete.

          - `:incomplete`

            The item stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: String`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus`

          The status of the reasoning item.

        - `summary: Array[SummaryText]`

          The reasoning summaries produced by the agent.

          - `text: String`

            The reasoning summary text.

          - `type: :summary_text`

            The content type. Always `summary_text`.

            - `:summary_text`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :reasoning`

          The item type. Always `reasoning`.

          - `:reasoning`

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: String`

          The ID of the function call item.

        - `arguments: untyped`

          The arguments to pass to the function.

        - `call_id: String`

          The ID used to submit the function result.

        - `name: String`

          The name of the function to call.

        - `status: AgentFunctionCallStatus`

          The status of the function call.

          - `:in_progress`

            The call is in progress.

          - `:completed`

            The call completed successfully.

          - `:failed`

            The call failed.

          - `:incomplete`

            The call stopped before completing.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call`

          The item type. Always `function_call`.

          - `:function_call`

      - `class FunctionCallOutput`

        The result supplied for a function call.

        - `id: String`

          The ID of the function call output item.

        - `call_id: String`

          The ID of the function call that produced this output.

        - `error: String`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput`

          The function result, if the call succeeded.

          - `String = String`

          - `UnionMember1 = Array[InputContent]`

            - `class InputText`

              Text input recorded in a session item.

              - `text: String`

                The text supplied to the agent.

              - `type: :input_text`

                The type of the object. Always `input_text`.

                - `:input_text`

            - `class InputImage`

              Image input recorded in a session item.

              - `image_url: String`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: :input_image`

                The type of the object. Always `input_image`.

                - `:input_image`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :function_call_output`

          The item type. Always `function_call_output`.

          - `:function_call_output`

      - `class AgentMessage`

        A message exchanged between agent threads.

        - `id: String`

          The ID of the message.

        - `content: Array[AgentContent]`

          The content exchanged between the agents.

          - `class OutputText`

            A text content part produced by the agent.

            - `text: String`

              The text produced by the agent.

            - `type: :output_text`

              The content type. Always `output_text`.

              - `:output_text`

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

            - `encrypted_content: String`

              The encrypted content payload.

            - `type: :encrypted_content`

              The content type. Always `encrypted_content`.

              - `:encrypted_content`

        - `recipient_agent_id: String`

          The ID or name of the receiving agent.

        - `sender_agent_id: String`

          The ID or name of the sending agent.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :agent_message`

          The item type. Always `agent_message`.

          - `:agent_message`

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: String`

          The ID of the MCP call item.

        - `arguments: untyped`

          The arguments passed to the MCP tool.

        - `error: untyped`

          The error returned by the MCP tool, if any.

        - `name: String`

          The name of the MCP tool.

        - `output: untyped`

          The output returned by the MCP tool, if any.

        - `server_label: String`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :mcp_call`

          The item type. Always `mcp_call`.

          - `:mcp_call`

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class ComputerUseApprovalRequestResult`

        A credential-free record of an admitted response, not proof of completion.

        - `id: String`

          The stable history item ID.

        - `request_id: String`

          The registered request answered by this item.

        - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

          The admitted response, without submitted credential values.

          - `class Submit`

            - `action: :submit`

              - `:submit`

            - `selected_option: String`

              The chosen sign-in method, or null when no options were offered.

            - `type: :browser_authentication`

              - `:browser_authentication`

          - `class Cancel`

            - `action: :cancel`

              - `:cancel`

            - `type: :browser_authentication`

              - `:browser_authentication`

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_approval_request_result`

          - `:computer_use_approval_request_result`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: String`

          The ID of the web search call.

        - `action: WebSearchAction`

          The action performed by the web search tool.

          - `class Search`

            A search query or group of search queries.

            - `queries: Array[String]`

              The search queries, when multiple queries were used.

            - `query: String`

              The search query, when a single query was used.

            - `type: :search`

              The type of the object. Always `search`.

              - `:search`

          - `class OpenPage`

            Opens a web page.

            - `type: :open_page`

              The type of the object. Always `open_page`.

              - `:open_page`

            - `url: String`

              The URL of the page that was opened.

          - `class FindInPage`

            Finds text within a web page.

            - `pattern: String`

              The text pattern that was searched for.

            - `type: :find_in_page`

              The type of the object. Always `find_in_page`.

              - `:find_in_page`

            - `url: String`

              The URL of the page that was searched.

          - `class Other`

            Another web search action.

            - `type: :other`

              The type of the object. Always `other`.

              - `:other`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :web_search_call`

          The item type. Always `web_search_call`.

          - `:web_search_call`

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: String`

          The ID of the command execution item.

        - `command: String`

          The command that was executed.

        - `cwd: String`

          The working directory used to execute the command.

        - `duration_ms: Integer`

          The command duration in milliseconds.

        - `exit_code: Integer`

          The process exit code, if the command completed.

        - `output: String`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :command_execution`

          The item type. Always `command_execution`.

          - `:command_execution`

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: String`

          The ID of the tool call item.

        - `agent_id: String`

          The ID of the agent that requested the subagent.

        - `content: Array[AgentContent]`

          The task given to the spawned agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `model: String`

          The model requested for the spawned agent.

        - `reasoning_effort: String`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :create_subagent_call`

          The item type. Always `create_subagent_call`.

          - `:create_subagent_call`

            The current public item type.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: String`

          The ID of the tool call item.

        - `content: Array[AgentContent]`

          The input sent to the receiving agent.

          - `class OutputText`

            A text content part produced by the agent.

          - `class EncryptedContent`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: String`

          The ID of the agent receiving the input.

        - `sender_agent_id: String`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :send_subagent_input_call`

          The item type. Always `send_subagent_input_call`.

          - `:send_subagent_input_call`

            The current public item type.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to resume.

        - `sender_agent_id: String`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :resume_subagent_call`

          The item type. Always `resume_subagent_call`.

          - `:resume_subagent_call`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_ids: Array[String]`

          The IDs of the agents to wait for.

        - `sender_agent_id: String`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :wait_for_subagents_call`

          The item type. Always `wait_for_subagents_call`.

          - `:wait_for_subagents_call`

            The current public item type.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to interrupt.

        - `sender_agent_id: String`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :interrupt_subagent_call`

          The item type. Always `interrupt_subagent_call`.

          - `:interrupt_subagent_call`

            The current public item type.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: String`

          The ID of the tool call item.

        - `recipient_agent_id: String`

          The ID of the agent to close.

        - `sender_agent_id: String`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :close_subagent_call`

          The item type. Always `close_subagent_call`.

          - `:close_subagent_call`

            The current public item type.

    - `output_index: Integer`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `:"agent.session.turn.item.added"`

  - `class AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: :"agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `:"agent.session.idle"`

  - `class AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: :"agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `:"agent.session.in_progress"`

  - `class AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: :"agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `:"agent.session.requires_action"`

  - `class AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: String`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: :"agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `:"agent.session.failed"`

  - `class AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `:"agent.session.environment.pending"`

  - `class AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `:"agent.session.environment.connected"`

  - `class AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `:"agent.session.environment.disconnected"`

  - `class AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: String`

      The unique ID of the event.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `:"agent.session.environment.failed"`

  - `class AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: String`

        The ID of the subagent.

      - `closed_at: Integer`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array[AgentContent]`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText`

          A text content part produced by the agent.

        - `class EncryptedContent`

          Encrypted content exchanged between agents.

      - `name: String`

        The runner-assigned nickname, or null when unavailable.

      - `object: :"agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `:"agent.session.subagent"`

      - `opened_at: Integer`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: String`

        The ID of the agent that created this subagent.

      - `session_id: String`

        The ID of the session that owns the subagent.

      - `status: :active | :closed`

        The current status of the subagent.

        - `:active`

          The subagent remains available, including while idle between turns.

        - `:closed`

          The subagent is closed.

    - `type: :"agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `:"agent.session.subagent.created"`

  - `class AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: :"agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `:"agent.session.subagent.active"`

  - `class AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: String`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: :"agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `:"agent.session.subagent.closed"`

  - `class AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `class AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: String`

          The ID of the message.

        - `content: Array[OutputText]`

          The content of the message.

          - `text: String`

            The text produced by the agent.

          - `type: :output_text`

            The content type. Always `output_text`.

        - `phase: :commentary | :final_answer`

          The phase of the assistant message.

          - `:commentary`

            Commentary produced while the agent works.

          - `:final_answer`

            The agent's final answer.

        - `role: :assistant`

          The role of the message author. Always `assistant`.

          - `:assistant`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :message`

          The item type. Always `message`.

          - `:message`

      - `class AgentReasoningItem`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem`

        A function call produced by the agent.

      - `class AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `class ComputerUseCall`

        One execution of the platform-provided computer-use capability.

        - `id: String`

          The ID of the activity item.

        - `output: Output{ image_url, type}`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: String`

            The complete JPEG image as a base64 data URL.

          - `type: :computer_screenshot`

            The content type. Always `computer_screenshot`.

            - `:computer_screenshot`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: String`

          A model-generated description of the activity, when available.

        - `turn_id: String`

          The ID of the turn that contains this item.

        - `type: :computer_use_call`

          The item type. Always `computer_use_call`.

          - `:computer_use_call`

      - `class ComputerUseApprovalRequest`

        A credential-free history record of the emitted login request.

        - `id: String`

          The stable history item ID.

        - `request: Request{ credential_origin, fields, options, 2 more}`

          A registered form awaiting the application's response.

          - `credential_origin: String`

            The registered form or frame origin where values will be entered.

          - `fields: Array[Field{ id, label, required, type}]`

            Controls to render. All submitted values are sensitive.

            - `id: String`

              The field ID to submit as field_id in a fields entry.

            - `label: String`

              The label to display beside the control.

            - `required: bool`

              Whether this control requires a nonempty value.

            - `type: String`

              The rendering type, such as email, password, or text.

          - `options: Array[Option{ id, field_ids, label}]`

            Sign-in methods. Empty for a plain form.

            - `id: String`

              The option ID to submit as selected_option.

            - `field_ids: Array[String]`

              IDs from the registered fields that this method accepts.

            - `label: String`

              The method label to display.

          - `reason: String`

            Why the agent needs the user to sign in.

          - `type: :browser_authentication`

            The type of the object. Always `browser_authentication`.

            - `:browser_authentication`

        - `request_id: String`

        - `turn_id: String`

        - `type: :computer_use_approval_request`

          The item type. Always computer_use_approval_request.

          - `:computer_use_approval_request`

      - `class AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: Integer`

      The index of the output item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `:"agent.session.turn.item.done"`

  - `class AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `:"agent.session.turn.content_part.added"`

  - `class AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `:"agent.session.turn.content_part.done"`

  - `class AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: Integer`

      The index of the content part in the message.

    - `delta: String`

      The text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `:"agent.session.turn.output_text.delta"`

  - `class AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: Integer`

      The index of the content part in the message.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the message item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `text: String`

      The complete output text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `:"agent.session.turn.output_text.done"`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `:"agent.session.turn.reasoning_summary_part.added"`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: String`

      The ID of the session associated with the event.

    - `status: :incomplete`

      Present as `incomplete` when summary generation was interrupted.

      - `:incomplete`

    - `summary_index: Integer`

      The index of the summary part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `:"agent.session.turn.reasoning_summary_part.done"`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: String`

      The summary text that was appended.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `:"agent.session.turn.reasoning_summary_text.delta"`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: String`

      The unique ID of the event.

    - `item_id: String`

      The ID of the reasoning item.

    - `output_index: Integer`

      The index of the item in the turn output.

    - `session_id: String`

      The ID of the session associated with the event.

    - `summary_index: Integer`

      The index of the summary content part.

    - `text: String`

      The complete reasoning summary text.

    - `turn_id: String`

      The ID of the turn associated with the event, when applicable.

    - `type: :"agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `:"agent.session.turn.reasoning_summary_text.done"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

agent_session_event = openai.beta.agents.sessions.events.stream("session_id")

puts(agent_session_event)
```

# Items

## List agent session items

`beta.agents.sessions.items.list(session_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.items.list("session_id")

puts(page)
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

`beta.agents.sessions.subagents.list(session_id, **kwargs) -> CursorPage<Subagent>`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.list("session_id")

puts(page)
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

`beta.agents.sessions.subagents.retrieve(subagent_id, **kwargs) -> Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

### Returns

- `class Subagent`

  A subagent created within a session.

  - `id: String`

    The ID of the subagent.

  - `closed_at: Integer`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array[AgentContent]`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText`

      A text content part produced by the agent.

      - `text: String`

        The text produced by the agent.

      - `type: :output_text`

        The content type. Always `output_text`.

        - `:output_text`

    - `class EncryptedContent`

      Encrypted content exchanged between agents.

      - `encrypted_content: String`

        The encrypted content payload.

      - `type: :encrypted_content`

        The content type. Always `encrypted_content`.

        - `:encrypted_content`

  - `name: String`

    The runner-assigned nickname, or null when unavailable.

  - `object: :"agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `:"agent.session.subagent"`

  - `opened_at: Integer`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: String`

    The ID of the agent that created this subagent.

  - `session_id: String`

    The ID of the session that owns the subagent.

  - `status: :active | :closed`

    The current status of the subagent.

    - `:active`

      The subagent remains available, including while idle between turns.

    - `:closed`

      The subagent is closed.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

subagent = openai.beta.agents.sessions.subagents.retrieve("subagent_id", session_id: "session_id")

puts(subagent)
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

`beta.agents.sessions.subagents.items.list(subagent_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.items.list("subagent_id", session_id: "session_id")

puts(page)
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

`beta.agents.sessions.subagents.turns.list(subagent_id, **kwargs) -> CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.turns.list("subagent_id", session_id: "session_id")

puts(page)
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

`beta.agents.sessions.subagents.turns.retrieve(turn_id, **kwargs) -> Turn`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `turn_id: String`

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

turn = openai.beta.agents.sessions.subagents.turns.retrieve(
  "turn_id",
  session_id: "session_id",
  subagent_id: "subagent_id"
)

puts(turn)
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

`beta.agents.sessions.subagents.turns.items.list(turn_id, **kwargs) -> CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `session_id: String`

- `subagent_id: String`

- `turn_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: String`

        The reasoning summary text.

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

    - `name: String`

      The name of the function to call.

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

    - `call_id: String`

      The ID of the function call that produced this output.

    - `error: String`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

    - `sender_agent_id: String`

      The ID or name of the sending agent.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        - `id: String`

          The field ID to submit as field_id in a fields entry.

        - `label: String`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        - `id: String`

          The option ID to submit as selected_option.

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

        - `label: String`

          The method label to display.

      - `reason: String`

        Why the agent needs the user to sign in.

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

    - `turn_id: String`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

    - `request_id: String`

      The registered request answered by this item.

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

        - `query: String`

          The search query, when a single query was used.

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

    - `command: String`

      The command that was executed.

    - `cwd: String`

      The working directory used to execute the command.

    - `duration_ms: Integer`

      The command duration in milliseconds.

    - `exit_code: Integer`

      The process exit code, if the command completed.

    - `output: String`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

    - `agent_id: String`

      The ID of the agent that requested the subagent.

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

        The current public item type.

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

    - `sender_agent_id: String`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

        The current public item type.

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to resume.

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

        The current public item type.

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

        The current public item type.

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

    - `recipient_agent_id: String`

      The ID of the agent to close.

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

        The current public item type.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.subagents.turns.items.list(
  "turn_id",
  session_id: "session_id",
  subagent_id: "subagent_id"
)

puts(page)
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

`beta.agents.sessions.turns.list(session_id, **kwargs) -> CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.turns.list("session_id")

puts(page)
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

`beta.agents.sessions.turns.retrieve(turn_id, **kwargs) -> Turn`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `session_id: String`

- `turn_id: String`

### Returns

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

turn = openai.beta.agents.sessions.turns.retrieve("turn_id", session_id: "session_id")

puts(turn)
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

- `class Turn`

  The canonical public representation of a session turn.

  - `id: String`

    The ID of the turn.

  - `agent_id: String`

    The ID of the agent that ran the turn.

  - `completed_at: Integer`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: Integer`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError`

    A customer-safe error. Non-null only for a failed turn.

    - `code: :context_length_exceeded | :session_budget_exceeded | :usage_limit_exceeded | 16 more`

      A stable, machine-readable failure category.

      - `:context_length_exceeded`

        The request exceeds the model's context window.

      - `:session_budget_exceeded`

        The session has reached its usage budget.

      - `:usage_limit_exceeded`

        The organization has reached a usage, plan, or billing limit.

      - `:credit_balance_exhausted`

        The organization has no API credits remaining.

      - `:rate_limit_exceeded`

        The request exceeds the available rate limit.

      - `:flex_unavailable`

        Flex processing is temporarily unavailable.

      - `:server_overloaded`

        The model service is temporarily overloaded.

      - `:cyber_policy`

        The request was rejected by a safety policy.

      - `:misalignment_policy_violation`

        The request was blocked by the safety systems.

      - `:connection_failed`

        The request could not connect to the model service.

      - `:server_error`

        The model service encountered an unexpected error.

      - `:authentication_error`

        The API credentials are invalid or lack the required access.

      - `:invalid_request`

        The request contains invalid input or configuration.

      - `:resource_not_found`

        The requested model or resource is unavailable.

      - `:sandbox_error`

        The request could not complete in its execution environment.

      - `:executor_version_incompatible`

        The executor must be upgraded before it can run this turn.

      - `:active_turn_not_steerable`

        The session cannot accept additional input while a request is running.

      - `:request_timeout`

        The request timed out before the model service responded.

      - `:internal_error`

        An unexpected internal error prevented the session request from completing.

    - `message: String`

      A customer-safe explanation of the failure.

  - `object: :"agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `:"agent.session.turn"`

  - `session_id: String`

    The ID of the session that owns the turn.

  - `started_at: Integer`

    The Unix timestamp, in seconds, when the turn started.

  - `status: :queued | :in_progress | :waiting | 3 more`

    The current status of the turn.

    - `:queued`

      The turn is waiting to start.

    - `:in_progress`

      The turn is in progress.

    - `:waiting`

      The turn is waiting for external input.

    - `:completed`

      The turn completed successfully.

    - `:failed`

      The turn failed.

    - `:cancelled`

      The turn was cancelled.

  - `subagent_id: String`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: Integer`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails{ cached_tokens}`

      A breakdown of the agent's input token usage.

      - `cached_tokens: Integer`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: Integer`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails{ reasoning_tokens}`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: Integer`

        The number of output tokens used for reasoning.

    - `total_tokens: Integer`

      The total number of input and output tokens used by the agent.

# Vaults

## Create a vault

`beta.agents.vaults.create(**kwargs) -> Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `metadata: Hash[Symbol, String]`

  Key-value pairs to associate with the vault, such as an application or team identifier.

- `name: String`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault = openai.beta.agents.vaults.create

puts(vault)
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

`beta.agents.vaults.delete(vault_id) -> VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

### Returns

- `class VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: String`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.deleted"`

    The object type. Always `vault.deleted`.

    - `:"vault.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault_deleted = openai.beta.agents.vaults.delete("vault_id")

puts(vault_deleted)
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

`beta.agents.vaults.list(**kwargs) -> CursorPage<Vault>`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `status: VaultStatusFilter`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

### Returns

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.vaults.list

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault

`beta.agents.vaults.retrieve(vault_id) -> Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

### Returns

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

vault = openai.beta.agents.vaults.retrieve("vault_id")

puts(vault)
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

## Domain Types

### Vault

- `class Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: String`

    The ID of the vault.

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Hash[Symbol, String]`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: String`

    The human-readable name of the vault, if set.

  - `object: :vault`

    The object type. Always `vault`.

    - `:vault`

### Vault Deleted

- `class VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: String`

    The ID of the deleted vault.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.deleted"`

    The object type. Always `vault.deleted`.

    - `:"vault.deleted"`

### Vault Status

- `VaultStatus = :active | :archived`

  Whether a vault or credential is active or archived.

  - `:active`

  - `:archived`

### Vault Status Filter

- `VaultStatusFilter = VaultStatus | Array[VaultStatus]`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

# Credentials

## Create a vault credential

`beta.agents.vaults.credentials.create(vault_id, **kwargs) -> Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `auth: CredentialAuthCreateParam`

  The authentication method and write-only secret values to store.

  - `class McpOauth`

    An OAuth credential for an HTTPS MCP destination.

    - `access_token: String`

      A write-only OAuth access token; never returned by credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `expires_at: String`

      When the OAuth access token expires, as an RFC 3339 timestamp, if known.

    - `refresh: Refresh{ client_id, refresh_token, token_endpoint, 3 more}`

      Optional refresh configuration for an HTTPS OAuth token endpoint.

      - `client_id: String`

        The OAuth client ID used when requesting a new access token.

      - `refresh_token: String`

        The refresh token to store. This secret is never returned in credential resources.

      - `token_endpoint: String`

        The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

        How the OAuth client authenticates to the token endpoint.

        - `class None`

          Sends the client ID without a client secret.

          - `type: :none`

            The type of the object. Always `none`.

            - `:none`

        - `class ClientSecretBasic`

          Sends the client ID and secret using HTTP Basic authentication.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

        - `class ClientSecretPost`

          Sends the client ID and secret in the token request body.

          - `client_secret: String`

            The OAuth client secret to store. Never returned in credential resources.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

      - `resource: String`

        The resource URI to send to the OAuth token endpoint during refresh, if required.

      - `scope: String`

        Space-separated OAuth scopes to request during refresh, if required.

  - `class StaticBearer`

    A bearer token for an MCP server, without automatic OAuth refresh.

    - `token: String`

      The bearer token to store. This secret is never returned in credential resources.

    - `mcp_server_url: String`

      The HTTPS MCP server URL authorized by this credential.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

    - `networking: CredentialNetworkingParam`

      The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

      - `class Unrestricted`

        Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

        - `type: :unrestricted`

          The type of the object. Always `unrestricted`.

          - `:unrestricted`

      - `class Limited`

        Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

        - `allowed_hosts: Array[String]`

          The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

        - `type: :limited`

          The type of the object. Always `limited`.

          - `:limited`

    - `secret_name: String`

      The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

    - `secret_value: String`

      The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

- `name: String`

  The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

- `metadata: Hash[Symbol, String]`

  Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential = openai.beta.agents.vaults.credentials.create(
  "vault_id",
  auth: {access_token: "access_token", mcp_server_url: "mcp_server_url", type: :mcp_oauth},
  name: "x"
)

puts(credential)
```

#### Response

```json
{
  "id": "id",
  "auth": {
    "expires_at": "expires_at",
    "mcp_server_url": "mcp_server_url",
    "refresh": {
      "client_id": "client_id",
      "resource": "resource",
      "scope": "scope",
      "token_endpoint": "token_endpoint",
      "token_endpoint_auth": {
        "type": "none"
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Delete a vault credential

`beta.agents.vaults.credentials.delete(credential_id, **kwargs) -> CredentialDeleted`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

### Returns

- `class CredentialDeleted`

  Confirmation that a vault credential was deleted.

  - `id: String`

    The ID of the deleted credential.

  - `deleted: bool`

    Whether the resource was deleted. Always `true`.

  - `object: :"vault.credential.deleted"`

    The object type. Always `vault.credential.deleted`.

    - `:"vault.credential.deleted"`

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential_deleted = openai.beta.agents.vaults.credentials.delete("credential_id", vault_id: "vault_id")

puts(credential_deleted)
```

#### Response

```json
{
  "id": "id",
  "deleted": true,
  "object": "vault.credential.deleted"
}
```

## List vault credentials

`beta.agents.vaults.credentials.list(vault_id, **kwargs) -> CursorPage<Credential>`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `after: String`

  Return resources after this resource ID in the selected order.

- `limit: Integer`

  The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

- `order: :asc | :desc`

  Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `status: VaultStatusFilter`

  Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

  - `VaultStatus = :active | :archived`

    Whether a vault or credential is active or archived.

    - `:active`

    - `:archived`

  - `UnionMember1 = Array[VaultStatus]`

    - `:active`

    - `:archived`

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.vaults.credentials.list("vault_id")

puts(page)
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "auth": {
        "expires_at": "expires_at",
        "mcp_server_url": "mcp_server_url",
        "refresh": {
          "client_id": "client_id",
          "resource": "resource",
          "scope": "scope",
          "token_endpoint": "token_endpoint",
          "token_endpoint_auth": {
            "type": "none"
          }
        },
        "type": "mcp_oauth"
      },
      "created_at": 0,
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "vault.credential",
      "updated_at": 0,
      "vault_id": "vault_id"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a vault credential

`beta.agents.vaults.credentials.retrieve(credential_id, **kwargs) -> Credential`

**get** `/vaults/{vault_id}/credentials/{credential_id}`

Retrieves vault credential metadata without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

credential = openai.beta.agents.vaults.credentials.retrieve("credential_id", vault_id: "vault_id")

puts(credential)
```

#### Response

```json
{
  "id": "id",
  "auth": {
    "expires_at": "expires_at",
    "mcp_server_url": "mcp_server_url",
    "refresh": {
      "client_id": "client_id",
      "resource": "resource",
      "scope": "scope",
      "token_endpoint": "token_endpoint",
      "token_endpoint_auth": {
        "type": "none"
      }
    },
    "type": "mcp_oauth"
  },
  "created_at": 0,
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "vault.credential",
  "updated_at": 0,
  "vault_id": "vault_id"
}
```

## Update a vault credential

`beta.agents.vaults.credentials.update(credential_id, **kwargs) -> Credential`

**post** `/vaults/{vault_id}/credentials/{credential_id}`

Updates credential metadata or rotates its write-only secret. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vault_id: String`

- `credential_id: String`

- `auth: CredentialAuthRotateParam`

  Replacement values for the credential's existing authentication method.

  - `class McpOauth`

    Rotate an OAuth credential for an HTTPS MCP destination.

    - `type: :mcp_oauth`

      The type of the object. Always `mcp_oauth`.

      - `:mcp_oauth`

    - `access_token: String`

      A write-only replacement OAuth access token.

    - `expires_at: String`

      The replacement expiry as an RFC 3339 timestamp, or `null` to clear it. Omitting this field preserves the expiry unless a new access token is supplied, in which case the expiry is cleared.

    - `refresh: Refresh{ refresh_token, scope, token_endpoint_auth}`

      Optional write-only refresh-token and client-secret updates.

      - `refresh_token: String`

        The replacement refresh token. Omit or pass `null` to keep the stored token. This secret is never returned in resources.

      - `scope: String`

        Replacement space-separated OAuth scopes for refresh requests. Omit to keep the scopes, or pass `null` to stop sending a scope parameter.

      - `token_endpoint_auth: McpOauthTokenEndpointAuthRotateParam`

        Client-secret updates for the existing token endpoint authentication method.

        - `class ClientSecretBasic`

          Updates credentials sent using HTTP Basic authentication.

          - `type: :client_secret_basic`

            The type of the object. Always `client_secret_basic`.

            - `:client_secret_basic`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

        - `class ClientSecretPost`

          Updates credentials sent in the token request body.

          - `type: :client_secret_post`

            The type of the object. Always `client_secret_post`.

            - `:client_secret_post`

          - `client_secret: String`

            The replacement OAuth client secret. Omit or pass `null` to keep the stored secret. This secret is never returned in resources.

  - `class StaticBearer`

    Replace the bearer token for the credential's MCP server.

    - `token: String`

      The replacement bearer token. This secret is never returned in credential resources.

    - `type: :static_bearer`

      The type of the object. Always `static_bearer`.

      - `:static_bearer`

  - `class EnvironmentVariable`

    Replace the secret for an OpenAI-hosted environment credential. The environment variable name and networking configuration remain unchanged.

    - `secret_value: String`

      The write-only replacement secret. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

    - `type: :environment_variable`

      The type of the object. Always `environment_variable`.

      - `:environment_variable`

- `metadata: Hash[Symbol, String]`

  Replaces all metadata. Omit to preserve it, or pass {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: String`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `class McpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: String`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh{ client_id, resource, scope, 2 more}`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: String`

          The OAuth client ID used when requesting a new access token.

        - `resource: String`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `scope: String`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `token_endpoint: String`

          The HTTPS OAuth token endpoint used for refresh.

        - `token_endpoint_auth: McpOauthTokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `class None`

            Sends the client ID without a client secret.

            - `type: :none`

              The type of the object. Always `none`.

              - `:none`

          - `class ClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `type: :client_secret_basic`

              The type of the object. Always `client_secret_basic`.

              - `:client_secret_basic`

          - `class ClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `type: :client_secret_post`

              The type of the object. Always `client_secret_post`.

              - `:client_secret_post`

      - `type: :mcp_oauth`

        The type of the object. Always `mcp_oauth`.

        - `:mcp_oauth`

    - `class StaticBearer`

      Metadata for a bearer-token credential, without automatic OAuth refresh.

      - `mcp_server_url: String`

        The HTTPS MCP server URL authorized by this credential.

      - `type: :static_bearer`

        The type of the object. Always `static_bearer`.

        - `:static_bearer`

    - `class EnvironmentVariable`

      Metadata for an HTTP credential used only in OpenAI-hosted environments. Sandbox code receives a placeholder. The proxy substitutes the secret for allowed HTTPS destinations on ports 443 and 8443. The real secret is not available to sandbox code for local computation and is never returned in this resource.

      - `networking: CredentialNetworking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `class Unrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: :unrestricted`

            The type of the object. Always `unrestricted`.

            - `:unrestricted`

        - `class Limited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array[String]`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: :limited`

            The type of the object. Always `limited`.

            - `:limited`

      - `secret_name: String`

        The environment variable name that receives the placeholder in the sandbox.

      - `type: :environment_variable`

        The type of the object. Always `environment_variable`.

        - `:environment_variable`

  - `created_at: Integer`

    The Unix timestamp, in seconds, when the credential was created.

  - `metadata: Hash[Symbol, String]`

    Application-defined key-value pairs associated with this credential.

  - `name: String`

    The human-readable name of the credential.

  - `object: :"vault.credential"`

    The object type. Always `vault.credential`.

    - `:"vault.credential"`

  - `updated_at: Integer`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `vault_id: String`

    The ID of the vault containing this credential.

### Example

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")
