<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

# Agents

## Create an agent

`client.beta.agents.create(AgentCreateParamsbody, RequestOptionsoptions?): Agent`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `body: AgentCreateParams`

  - `model: string`

    The model to use for the agent. The requested model name is preserved.

  - `instructions?: string | null`

    Additional instructions appended to the agent's default base instructions. Omit or set to null to add no custom instructions.

  - `metadata?: Record<string, string> | null`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

  - `multi_agent?: MultiAgentConfigParam | null`

    Configuration for creating and coordinating subagents. Subagent tools are disabled by default.

    - `enabled: boolean`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents?: number`

      Maximum number of subagents that may run concurrently. Defaults to 6.

  - `name?: string | null`

    A human-readable name for the agent. Omission or null leaves the agent unnamed.

  - `reasoning?: AgentReasoningParam | null`

    Configuration for model reasoning. Omission uses the model's default effort.

    - `effort?: "none" | "minimal" | "low" | 4 more | null`

      The amount of reasoning effort the model should use. Omission lets the model select it.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary?: "concise" | "detailed" | "auto" | null`

      Controls whether the response includes a reasoning summary.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

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

  - `text?: AgentTextParam | null`

    Configuration for generated text. Defaults to the `text` format and medium verbosity.

    - `format?: TextFormatParam | null`

      The output format. Omission uses ordinary text (`{"type": "text"}`).

      - `TextFormatParamText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatParamJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity?: "low" | "medium" | "high" | null`

      The amount of text the model should produce. Defaults to `medium`, matching Responses.

      - `"low"`

        Produces less text.

      - `"medium"`

        Uses the default amount of text.

      - `"high"`

        Produces more text.

  - `tools?: Array<PersistedAgentToolParam> | null`

    Tools available to the agent. Defaults to an empty list.

    - `PersistedAgentToolConfigParamFunction`

      A function defined by the application.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

      - `defer_loading?: boolean`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `PersistedAgentToolConfigParamToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolConfigParamProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

      - `enabled?: boolean`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `PersistedAgentToolConfigParamMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransportParam`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportConfigParamHTTP`

          Connects to an MCP server over HTTP.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

          - `headers?: Record<string, string> | null`

            Non-secret HTTP headers sent to the MCP server.

        - `PersistedMcpTransportConfigParamStdio`

          Starts an MCP server as a local process.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

          - `args?: Array<string> | null`

            Arguments passed to the MCP server command.

          - `env_vars?: Array<string> | null`

            Environment variable names to inherit from the selected execution environment.

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

      - `allowed_tools?: Array<string> | null`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin?: "service" | "environment" | null`

        Selects where outbound MCP HTTP connections originate.

        - `"service"`

          Uses the Managed Agents service network.

        - `"environment"`

          Uses the session's execution environment.

      - `credential_id?: string | null`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `request_metadata?: Record<string, unknown> | null`

        Metadata included with requests to this MCP server.

      - `required?: boolean`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `PersistedAgentToolConfigParamWebSearch`

      Web search.

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

      - `allowed_domains?: Array<string> | null`

        Domains the search may include.

      - `context_size?: "low" | "medium" | "high" | null`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location?: Location | null`

        Approximate location used to localize search results.

        - `city?: string | null`

          The city name.

        - `country?: string | null`

          The two-letter ISO country code, such as `US`.

        - `region?: string | null`

          The region or state name.

        - `timezone?: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode?: "disabled" | "cached" | "live" | null`

        The source used for web search results. Defaults to `live`.

        - `"disabled"`

          Disables web search.

        - `"cached"`

          Uses cached search results.

        - `"live"`

          Searches the live web.

    - `PersistedAgentToolConfigParamComputerUse`

      Browser use in an OpenAI-hosted session.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

      - `include_screenshots?: boolean`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `Agent`

  A reusable agent scoped to the caller's project.

  - `id: string`

    The ID of the reusable agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: string | null`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the agent.

  - `model: string`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: number | null`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: string | null`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: "agent"`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: "none" | "minimal" | "low" | 4 more | null`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: "concise" | "detailed" | "auto" | null`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: "auto" | "default" | "flex" | 3 more`

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

      - `TextFormatResourceText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatResourceJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: "low" | "medium" | "high"`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: Array<PersistedAgentTool>`

    Tools available to the agent.

    - `PersistedAgentToolResourceFunction`

      A function defined by the application.

      - `defer_loading: boolean`

        Whether the function is deferred and discovered through tool search.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

    - `PersistedAgentToolResourceToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolResourceProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: boolean`

        Whether tools can be called from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `PersistedAgentToolResourceMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array<string> | null`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: "service" | "environment"`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: string | null`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Record<string, unknown>`

        Metadata included with requests to this MCP server.

      - `required: boolean`

        Whether this MCP server must initialize before the first turn.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportResourceHTTP`

          Connects to an MCP server over HTTP.

          - `headers: Record<string, string>`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

        - `PersistedMcpTransportResourceStdio`

          Starts an MCP server as a local process.

          - `args: Array<string>`

            Arguments passed to the MCP server command.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `env_vars: Array<string>`

            Environment variable names inherited from the execution environment.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `PersistedAgentToolResourceWebSearch`

      Web search.

      - `allowed_domains: Array<string> | null`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: "low" | "medium" | "high"`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Location | null`

        Approximate location used to localize search results, if provided.

        - `city: string | null`

          The city name.

        - `country: string | null`

          The two-letter ISO country code, such as `US`.

        - `region: string | null`

          The region or state name.

        - `timezone: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: "disabled" | "cached" | "live"`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `PersistedAgentToolResourceComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: boolean`

        Whether computer tool outputs include screenshots.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agent = await client.beta.agents.create({ model: 'model' });

console.log(agent.id);
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

`client.beta.agents.delete(stringagentID, RequestOptionsoptions?): AgentDeleted`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID: string`

### Returns

- `AgentDeleted`

  A deleted reusable agent.

  - `id: string`

    The ID of the deleted agent.

  - `deleted: boolean`

    Whether the agent was deleted. Always `true`.

  - `object: "agent.deleted"`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentDeleted = await client.beta.agents.delete('agent_id');

console.log(agentDeleted.id);
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

`client.beta.agents.list(AgentListParamsquery?, RequestOptionsoptions?): CursorPage<Agent>`

**get** `/agents`

Lists reusable agents in the current project. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `query: AgentListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number | null`

    The maximum number of resources to return.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `Agent`

  A reusable agent scoped to the caller's project.

  - `id: string`

    The ID of the reusable agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: string | null`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the agent.

  - `model: string`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: number | null`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: string | null`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: "agent"`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: "none" | "minimal" | "low" | 4 more | null`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: "concise" | "detailed" | "auto" | null`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: "auto" | "default" | "flex" | 3 more`

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

      - `TextFormatResourceText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatResourceJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: "low" | "medium" | "high"`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: Array<PersistedAgentTool>`

    Tools available to the agent.

    - `PersistedAgentToolResourceFunction`

      A function defined by the application.

      - `defer_loading: boolean`

        Whether the function is deferred and discovered through tool search.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

    - `PersistedAgentToolResourceToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolResourceProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: boolean`

        Whether tools can be called from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `PersistedAgentToolResourceMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array<string> | null`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: "service" | "environment"`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: string | null`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Record<string, unknown>`

        Metadata included with requests to this MCP server.

      - `required: boolean`

        Whether this MCP server must initialize before the first turn.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportResourceHTTP`

          Connects to an MCP server over HTTP.

          - `headers: Record<string, string>`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

        - `PersistedMcpTransportResourceStdio`

          Starts an MCP server as a local process.

          - `args: Array<string>`

            Arguments passed to the MCP server command.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `env_vars: Array<string>`

            Environment variable names inherited from the execution environment.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `PersistedAgentToolResourceWebSearch`

      Web search.

      - `allowed_domains: Array<string> | null`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: "low" | "medium" | "high"`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Location | null`

        Approximate location used to localize search results, if provided.

        - `city: string | null`

          The city name.

        - `country: string | null`

          The two-letter ISO country code, such as `US`.

        - `region: string | null`

          The region or state name.

        - `timezone: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: "disabled" | "cached" | "live"`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `PersistedAgentToolResourceComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: boolean`

        Whether computer tool outputs include screenshots.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agent of client.beta.agents.list()) {
  console.log(agent.id);
}
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

`client.beta.agents.retrieve(stringagentID, RequestOptionsoptions?): Agent`

**get** `/agents/{agent_id}`

Retrieves a reusable agent by ID. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID: string`

### Returns

- `Agent`

  A reusable agent scoped to the caller's project.

  - `id: string`

    The ID of the reusable agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: string | null`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the agent.

  - `model: string`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: number | null`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: string | null`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: "agent"`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: "none" | "minimal" | "low" | 4 more | null`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: "concise" | "detailed" | "auto" | null`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: "auto" | "default" | "flex" | 3 more`

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

      - `TextFormatResourceText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatResourceJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: "low" | "medium" | "high"`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: Array<PersistedAgentTool>`

    Tools available to the agent.

    - `PersistedAgentToolResourceFunction`

      A function defined by the application.

      - `defer_loading: boolean`

        Whether the function is deferred and discovered through tool search.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

    - `PersistedAgentToolResourceToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolResourceProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: boolean`

        Whether tools can be called from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `PersistedAgentToolResourceMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array<string> | null`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: "service" | "environment"`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: string | null`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Record<string, unknown>`

        Metadata included with requests to this MCP server.

      - `required: boolean`

        Whether this MCP server must initialize before the first turn.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportResourceHTTP`

          Connects to an MCP server over HTTP.

          - `headers: Record<string, string>`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

        - `PersistedMcpTransportResourceStdio`

          Starts an MCP server as a local process.

          - `args: Array<string>`

            Arguments passed to the MCP server command.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `env_vars: Array<string>`

            Environment variable names inherited from the execution environment.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `PersistedAgentToolResourceWebSearch`

      Web search.

      - `allowed_domains: Array<string> | null`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: "low" | "medium" | "high"`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Location | null`

        Approximate location used to localize search results, if provided.

        - `city: string | null`

          The city name.

        - `country: string | null`

          The two-letter ISO country code, such as `US`.

        - `region: string | null`

          The region or state name.

        - `timezone: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: "disabled" | "cached" | "live"`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `PersistedAgentToolResourceComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: boolean`

        Whether computer tool outputs include screenshots.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agent = await client.beta.agents.retrieve('agent_id');

console.log(agent.id);
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

`client.beta.agents.update(stringagentID, AgentUpdateParamsbody?, RequestOptionsoptions?): Agent`

**post** `/agents/{agent_id}`

Updates a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID: string`

- `body: AgentUpdateParams`

  - `instructions?: string | null`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `metadata?: Record<string, string> | null`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `model?: string`

    The model to use for the agent. The requested model name is preserved.

  - `multi_agent?: MultiAgentConfigParam | null`

    Configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled.

    - `max_concurrent_subagents?: number`

      Maximum number of subagents that may run concurrently. Defaults to 6.

  - `name?: string | null`

    A replacement name. Omit to leave unchanged, or pass null to clear it.

  - `reasoning?: AgentReasoningParam | null`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

    - `effort?: "none" | "minimal" | "low" | 4 more | null`

      The amount of reasoning effort the model should use. Omission lets the model select it.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary?: "concise" | "detailed" | "auto" | null`

      Controls whether the response includes a reasoning summary.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

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

  - `text?: AgentTextParam | null`

    Configuration for text generated by the agent.

    - `format?: TextFormatParam | null`

      The output format. Omission uses ordinary text (`{"type": "text"}`).

      - `TextFormatParamText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatParamJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity?: "low" | "medium" | "high" | null`

      The amount of text the model should produce. Defaults to `medium`, matching Responses.

      - `"low"`

        Produces less text.

      - `"medium"`

        Uses the default amount of text.

      - `"high"`

        Produces more text.

  - `tools?: Array<PersistedAgentToolParam> | null`

    Tools available to the agent.

    - `PersistedAgentToolConfigParamFunction`

      A function defined by the application.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

      - `defer_loading?: boolean`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `PersistedAgentToolConfigParamToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolConfigParamProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

      - `enabled?: boolean`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `PersistedAgentToolConfigParamMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransportParam`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportConfigParamHTTP`

          Connects to an MCP server over HTTP.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

          - `headers?: Record<string, string> | null`

            Non-secret HTTP headers sent to the MCP server.

        - `PersistedMcpTransportConfigParamStdio`

          Starts an MCP server as a local process.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

          - `args?: Array<string> | null`

            Arguments passed to the MCP server command.

          - `env_vars?: Array<string> | null`

            Environment variable names to inherit from the selected execution environment.

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

      - `allowed_tools?: Array<string> | null`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `connection_origin?: "service" | "environment" | null`

        Selects where outbound MCP HTTP connections originate.

        - `"service"`

          Uses the Managed Agents service network.

        - `"environment"`

          Uses the session's execution environment.

      - `credential_id?: string | null`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `request_metadata?: Record<string, unknown> | null`

        Metadata included with requests to this MCP server.

      - `required?: boolean`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `PersistedAgentToolConfigParamWebSearch`

      Web search.

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

      - `allowed_domains?: Array<string> | null`

        Domains the search may include.

      - `context_size?: "low" | "medium" | "high" | null`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location?: Location | null`

        Approximate location used to localize search results.

        - `city?: string | null`

          The city name.

        - `country?: string | null`

          The two-letter ISO country code, such as `US`.

        - `region?: string | null`

          The region or state name.

        - `timezone?: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode?: "disabled" | "cached" | "live" | null`

        The source used for web search results. Defaults to `live`.

        - `"disabled"`

          Disables web search.

        - `"cached"`

          Uses cached search results.

        - `"live"`

          Searches the live web.

    - `PersistedAgentToolConfigParamComputerUse`

      Browser use in an OpenAI-hosted session.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

      - `include_screenshots?: boolean`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `Agent`

  A reusable agent scoped to the caller's project.

  - `id: string`

    The ID of the reusable agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: string | null`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the agent.

  - `model: string`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: number | null`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: string | null`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: "agent"`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: "none" | "minimal" | "low" | 4 more | null`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: "concise" | "detailed" | "auto" | null`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: "auto" | "default" | "flex" | 3 more`

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

      - `TextFormatResourceText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatResourceJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: "low" | "medium" | "high"`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: Array<PersistedAgentTool>`

    Tools available to the agent.

    - `PersistedAgentToolResourceFunction`

      A function defined by the application.

      - `defer_loading: boolean`

        Whether the function is deferred and discovered through tool search.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

    - `PersistedAgentToolResourceToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolResourceProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: boolean`

        Whether tools can be called from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `PersistedAgentToolResourceMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array<string> | null`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: "service" | "environment"`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: string | null`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Record<string, unknown>`

        Metadata included with requests to this MCP server.

      - `required: boolean`

        Whether this MCP server must initialize before the first turn.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportResourceHTTP`

          Connects to an MCP server over HTTP.

          - `headers: Record<string, string>`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

        - `PersistedMcpTransportResourceStdio`

          Starts an MCP server as a local process.

          - `args: Array<string>`

            Arguments passed to the MCP server command.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `env_vars: Array<string>`

            Environment variable names inherited from the execution environment.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `PersistedAgentToolResourceWebSearch`

      Web search.

      - `allowed_domains: Array<string> | null`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: "low" | "medium" | "high"`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Location | null`

        Approximate location used to localize search results, if provided.

        - `city: string | null`

          The city name.

        - `country: string | null`

          The two-letter ISO country code, such as `US`.

        - `region: string | null`

          The region or state name.

        - `timezone: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: "disabled" | "cached" | "live"`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `PersistedAgentToolResourceComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: boolean`

        Whether computer tool outputs include screenshots.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agent = await client.beta.agents.update('agent_id');

console.log(agent.id);
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

- `Agent`

  A reusable agent scoped to the caller's project.

  - `id: string`

    The ID of the reusable agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the agent was created.

  - `instructions: string | null`

    Custom instructions appended to the agent's default base instructions.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the agent.

  - `model: string`

    The requested model name used for inference.

  - `multi_agent: MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `enabled: boolean`

      Whether subagent tools are enabled. Defaults to false.

    - `max_concurrent_subagents: number | null`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `name: string | null`

    A human-readable name for the agent, or null if it is unnamed.

  - `object: "agent"`

    The object type. Always `agent`.

    - `"agent"`

  - `reasoning: AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `effort: "none" | "minimal" | "low" | 4 more | null`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `"none"`

      - `"minimal"`

      - `"low"`

      - `"medium"`

      - `"high"`

      - `"xhigh"`

      - `"max"`

    - `summary: "concise" | "detailed" | "auto" | null`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `"concise"`

        Returns a concise reasoning summary when supported.

      - `"detailed"`

        Returns a detailed reasoning summary when supported.

      - `"auto"`

        Automatically selects the most detailed summary supported by the model.

  - `service_tier: "auto" | "default" | "flex" | 3 more`

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

      - `TextFormatResourceText`

        Generates ordinary text without a structured-output constraint.

        - `type: "text"`

          The type of the object. Always `text`.

          - `"text"`

      - `TextFormatResourceJSONSchema`

        Constrains generated text to a JSON Schema.

        - `schema: Record<string, unknown>`

          The JSON Schema that generated text must match.

        - `type: "json_schema"`

          The type of the object. Always `json_schema`.

          - `"json_schema"`

    - `verbosity: "low" | "medium" | "high"`

      The amount of text produced by the agent. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

  - `tools: Array<PersistedAgentTool>`

    Tools available to the agent.

    - `PersistedAgentToolResourceFunction`

      A function defined by the application.

      - `defer_loading: boolean`

        Whether the function is deferred and discovered through tool search.

      - `description: string`

        A description of what the function does.

      - `name: string`

        The name of the function.

      - `parameters: Record<string, unknown>`

        A JSON Schema object describing the function's arguments.

      - `type: "function"`

        The type of the object. Always `function`.

        - `"function"`

    - `PersistedAgentToolResourceToolSearch`

      Discovers deferred function tools and loads them into the model context.

      - `type: "tool_search"`

        The type of the object. Always `tool_search`.

        - `"tool_search"`

    - `PersistedAgentToolResourceProgrammaticToolCalling`

      Enables calling tools from model-generated code.

      - `enabled: boolean`

        Whether tools can be called from model-generated code.

      - `type: "programmatic_tool_calling"`

        The type of the object. Always `programmatic_tool_calling`.

        - `"programmatic_tool_calling"`

    - `PersistedAgentToolResourceMcp`

      Tools provided by a remote MCP server without stored credentials.

      - `allowed_tools: Array<string> | null`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `connection_origin: "service" | "environment"`

        Where outbound MCP HTTP connections originate.

        - `"service"`

        - `"environment"`

      - `credential_id: string | null`

        The vault credential selected for this MCP server, if any.

      - `request_metadata: Record<string, unknown>`

        Metadata included with requests to this MCP server.

      - `required: boolean`

        Whether this MCP server must initialize before the first turn.

      - `server_label: string`

        A label used to identify the MCP server in tool calls.

      - `transport: PersistedMcpTransport`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportResourceHTTP`

          Connects to an MCP server over HTTP.

          - `headers: Record<string, string>`

            Non-secret HTTP headers sent to the MCP server.

          - `server_url: string`

            The URL of the MCP server.

          - `type: "http"`

            The type of the object. Always `http`.

            - `"http"`

        - `PersistedMcpTransportResourceStdio`

          Starts an MCP server as a local process.

          - `args: Array<string>`

            Arguments passed to the MCP server command.

          - `command: string`

            The command used to start the MCP server.

          - `cwd: string`

            The working directory used to start the MCP server.

          - `env_vars: Array<string>`

            Environment variable names inherited from the execution environment.

          - `type: "stdio"`

            The type of the object. Always `stdio`.

            - `"stdio"`

      - `type: "mcp"`

        The type of the object. Always `mcp`.

        - `"mcp"`

    - `PersistedAgentToolResourceWebSearch`

      Web search.

      - `allowed_domains: Array<string> | null`

        Allowed search domains, or `null` when the search is unrestricted.

      - `context_size: "low" | "medium" | "high"`

        The amount of search context made available to the model. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

      - `location: Location | null`

        Approximate location used to localize search results, if provided.

        - `city: string | null`

          The city name.

        - `country: string | null`

          The two-letter ISO country code, such as `US`.

        - `region: string | null`

          The region or state name.

        - `timezone: string | null`

          The IANA timezone, such as `America/Los_Angeles`.

      - `mode: "disabled" | "cached" | "live"`

        The source used for web search results.

        - `"disabled"`

        - `"cached"`

        - `"live"`

      - `type: "web_search"`

        The type of the object. Always `web_search`.

        - `"web_search"`

    - `PersistedAgentToolResourceComputerUse`

      Browser use in an OpenAI-hosted session.

      - `include_screenshots: boolean`

        Whether computer tool outputs include screenshots.

      - `type: "computer_use"`

        The type of the object. Always `computer_use`.

        - `"computer_use"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the agent was last updated.

### Agent Browser Authentication Cancel Param

- `AgentBrowserAuthenticationCancelParam`

  - `action: "cancel"`

    - `"cancel"`

  - `type: "browser_authentication"`

    - `"browser_authentication"`

### Agent Browser Authentication Submit Param

- `AgentBrowserAuthenticationSubmitParam`

  - `action: "submit"`

    - `"submit"`

  - `fields: Array<Field>`

    Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

    - `field_id: string`

      The field ID from the required action.

    - `value: string`

      The value to enter into the registered control.

  - `type: "browser_authentication"`

    - `"browser_authentication"`

  - `selected_option?: string | null`

    The chosen method. Required when the required action contains options.

### Agent Browser Origin Access Param

- `AgentBrowserOriginAccessParam`

  - `decision: "approve" | "deny" | "cancel"`

    Whether to allow, deny, or cancel the requested origin access.

    - `"approve"`

      Allow the browser to access this origin.

    - `"deny"`

      Deny access to this origin.

    - `"cancel"`

      Dismiss this request without approving access.

  - `type: "browser_origin_access"`

    - `"browser_origin_access"`

### Agent Close Subagent Call Item

- `AgentCloseSubagentCallItem`

  A request to close a subagent.

  - `id: string`

    The ID of the tool call item.

  - `recipient_agent_id: string`

    The ID of the agent to close.

  - `sender_agent_id: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "close_subagent_call"`

    The item type. Always `close_subagent_call`.

    - `"close_subagent_call"`

      The current public item type.

### Agent Command Execution Item

- `AgentCommandExecutionItem`

  A command execution produced by the agent.

  - `id: string`

    The ID of the command execution item.

  - `command: string`

    The command that was executed.

  - `cwd: string | null`

    The working directory used to execute the command.

  - `duration_ms: number | null`

    The command duration in milliseconds.

  - `exit_code: number | null`

    The process exit code, if the command completed.

  - `output: string | null`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "command_execution"`

    The item type. Always `command_execution`.

    - `"command_execution"`

### Agent Content

- `AgentContent = OutputText | EncryptedContentResource`

  A plaintext or encrypted content part exchanged between agents.

  - `OutputText`

    A text content part produced by the agent.

    - `text: string`

      The text produced by the agent.

    - `type: "output_text"`

      The content type. Always `output_text`.

      - `"output_text"`

  - `EncryptedContentResource`

    Encrypted content exchanged between agents.

    - `encrypted_content: string`

      The encrypted content payload.

    - `type: "encrypted_content"`

      The content type. Always `encrypted_content`.

      - `"encrypted_content"`

### Agent Create Subagent Call Item

- `AgentCreateSubagentCallItem`

  A request to spawn a subagent.

  - `id: string`

    The ID of the tool call item.

  - `agent_id: string`

    The ID of the agent that requested the subagent.

  - `content: Array<AgentContent>`

    The task given to the spawned agent.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `model: string | null`

    The model requested for the spawned agent.

  - `reasoning_effort: string | null`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "create_subagent_call"`

    The item type. Always `create_subagent_call`.

    - `"create_subagent_call"`

      The current public item type.

### Agent Deleted

- `AgentDeleted`

  A deleted reusable agent.

  - `id: string`

    The ID of the deleted agent.

  - `deleted: boolean`

    Whether the agent was deleted. Always `true`.

  - `object: "agent.deleted"`

    The object type. Always `agent.deleted`.

    - `"agent.deleted"`

### Agent Function Call Item

- `AgentFunctionCallItem`

  A function call produced by the agent.

  - `id: string`

    The ID of the function call item.

  - `arguments: unknown`

    The arguments to pass to the function.

  - `call_id: string`

    The ID used to submit the function result.

  - `name: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "function_call"`

    The item type. Always `function_call`.

    - `"function_call"`

### Agent Function Call Output

- `AgentFunctionCallOutput = string | Array<InputContent>`

  The text or model-input content supplied as a function result.

  - `string`

  - `Array<InputContent>`

    - `InputContentResourceInputText`

      Text input recorded in a session item.

      - `text: string`

        The text supplied to the agent.

      - `type: "input_text"`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `InputContentResourceInputImage`

      Image input recorded in a session item.

      - `image_url: string`

        The URL of the image supplied to the agent, which may be a base64-encoded data URL.

      - `type: "input_image"`

        The type of the object. Always `input_image`.

        - `"input_image"`

### Agent Function Call Output Param

- `AgentFunctionCallOutputParam = string | Array<InputContentParam>`

  A function result represented as text or supported model-input content.

  - `string`

  - `Array<InputContentParam>`

    - `InputContentParamInputText`

      Text input to the model.

      - `text: string`

        The text sent to the model.

      - `type: "input_text"`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `InputContentParamInputImage`

      Image input to the model.

      - `image_url: string`

        The URL of the image sent to the model.

      - `type: "input_image"`

        The type of the object. Always `input_image`.

        - `"input_image"`

### Agent Function Call Status

- `AgentFunctionCallStatus = "in_progress" | "completed" | "failed" | "incomplete"`

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

- `AgentInterruptSubagentCallItem`

  A request to interrupt a subagent's current turn. The subagent remains available.

  - `id: string`

    The ID of the tool call item.

  - `recipient_agent_id: string`

    The ID of the agent to interrupt.

  - `sender_agent_id: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "interrupt_subagent_call"`

    The item type. Always `interrupt_subagent_call`.

    - `"interrupt_subagent_call"`

      The current public item type.

### Agent Mcp Call Item

- `AgentMcpCallItem`

  A call to a tool on an MCP server.

  - `id: string`

    The ID of the MCP call item.

  - `arguments: unknown`

    The arguments passed to the MCP tool.

  - `error: unknown`

    The error returned by the MCP tool, if any.

  - `name: string`

    The name of the MCP tool.

  - `output: unknown`

    The output returned by the MCP tool, if any.

  - `server_label: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "mcp_call"`

    The item type. Always `mcp_call`.

    - `"mcp_call"`

### Agent Output Command Execution Output Delta Event

- `AgentOutputCommandExecutionOutputDeltaEvent`

  Emitted when command execution produces an output delta.

  - `delta: string`

    The output text that was appended.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the command execution item.

  - `output_index: number`

    The index of the item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.output.command_execution_output.delta"`

    The type of the object. Always `agent.output.command_execution_output.delta`.

    - `"agent.output.command_execution_output.delta"`

### Agent Output Item

- `AgentOutputItem = AgentSessionAssistantMessage | AgentReasoningItem | AgentFunctionCallItem | 11 more`

  An output item produced by an agent.

  - `AgentSessionAssistantMessage`

    An assistant message produced by the agent.

    - `id: string`

      The ID of the message.

    - `content: Array<OutputText>`

      The content of the message.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of the assistant message.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "assistant"`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Agent Output Item Status

- `AgentOutputItemStatus = "in_progress" | "completed" | "incomplete"`

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

- `AgentReasoning`

  The reasoning configuration used by an agent.

  - `effort: "none" | "minimal" | "low" | 4 more | null`

    The requested reasoning effort, or `null` when the model selects its own default.

    - `"none"`

    - `"minimal"`

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `summary: "concise" | "detailed" | "auto" | null`

    The requested reasoning summary format, or `null` when summaries are disabled.

    - `"concise"`

      Returns a concise reasoning summary when supported.

    - `"detailed"`

      Returns a detailed reasoning summary when supported.

    - `"auto"`

      Automatically selects the most detailed summary supported by the model.

### Agent Reasoning Item

- `AgentReasoningItem`

  A reasoning item produced by the agent.

  - `id: string`

    The ID of the reasoning item.

  - `status: AgentOutputItemStatus | null`

    The status of the reasoning item.

    - `"in_progress"`

      The item is in progress.

    - `"completed"`

      The item is complete.

    - `"incomplete"`

      The item stopped before completing.

  - `summary: Array<SummaryText>`

    The reasoning summaries produced by the agent.

    - `text: string`

      The reasoning summary text.

    - `type: "summary_text"`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "reasoning"`

    The item type. Always `reasoning`.

    - `"reasoning"`

### Agent Reasoning Param

- `AgentReasoningParam`

  Reasoning configuration for the agent.

  - `effort?: "none" | "minimal" | "low" | 4 more | null`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `"none"`

    - `"minimal"`

    - `"low"`

    - `"medium"`

    - `"high"`

    - `"xhigh"`

    - `"max"`

  - `summary?: "concise" | "detailed" | "auto" | null`

    Controls whether the response includes a reasoning summary.

    - `"concise"`

      Returns a concise reasoning summary when supported.

    - `"detailed"`

      Returns a detailed reasoning summary when supported.

    - `"auto"`

      Automatically selects the most detailed summary supported by the model.

### Agent Resume Subagent Call Item

- `AgentResumeSubagentCallItem`

  A request to resume a subagent.

  - `id: string`

    The ID of the tool call item.

  - `recipient_agent_id: string`

    The ID of the agent to resume.

  - `sender_agent_id: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "resume_subagent_call"`

    The item type. Always `resume_subagent_call`.

    - `"resume_subagent_call"`

      The current public item type.

### Agent Send Subagent Input Call Item

- `AgentSendSubagentInputCallItem`

  A request to send input to another agent.

  - `id: string`

    The ID of the tool call item.

  - `content: Array<AgentContent>`

    The input sent to the receiving agent.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `recipient_agent_id: string`

    The ID of the agent receiving the input.

  - `sender_agent_id: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "send_subagent_input_call"`

    The item type. Always `send_subagent_input_call`.

    - `"send_subagent_input_call"`

      The current public item type.

### Agent Session

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: "none" | "minimal" | "low" | 4 more | null`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

      - `summary: "concise" | "detailed" | "auto" | null`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `"concise"`

          Returns a concise reasoning summary when supported.

        - `"detailed"`

          Returns a detailed reasoning summary when supported.

        - `"auto"`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: "auto" | "default" | "flex" | 3 more`

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

        - `TextFormatResourceText`

          Generates ordinary text without a structured-output constraint.

          - `type: "text"`

            The type of the object. Always `text`.

            - `"text"`

        - `TextFormatResourceJSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Record<string, unknown>`

            The JSON Schema that generated text must match.

          - `type: "json_schema"`

            The type of the object. Always `json_schema`.

            - `"json_schema"`

      - `verbosity: "low" | "medium" | "high"`

        The amount of text produced by the agent. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

    - `tools: Array<AgentTool>`

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

      - `AgentToolResourceProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: boolean`

          Whether tools can be called from model-generated code.

        - `type: "programmatic_tool_calling"`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `AgentToolResourceMcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array<string> | null`

          The MCP tools the agent may call.

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

            - `type: "stdio"`

              The type of the object. Always `stdio`.

              - `"stdio"`

        - `type: "mcp"`

          The type of the object. Always `mcp`.

          - `"mcp"`

      - `AgentToolResourceWebSearch`

        Web search.

        - `allowed_domains: Array<string> | null`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: "disabled" | "cached" | "live"`

          The source used for web search results.

          - `"disabled"`

          - `"cached"`

          - `"live"`

        - `type: "web_search"`

          The type of the object. Always `web_search`.

          - `"web_search"`

      - `AgentToolResourceComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: boolean`

          Whether computer tool outputs include screenshots.

        - `type: "computer_use"`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

        - `access: "enabled" | "disabled" | "restricted"`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: Array<string>`

          Domains the environment may access when network access is restricted.

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

### Agent Session Assistant Message

- `AgentSessionAssistantMessage`

  An assistant message produced by the agent.

  - `id: string`

    The ID of the message.

  - `content: Array<OutputText>`

    The content of the message.

    - `text: string`

      The text produced by the agent.

    - `type: "output_text"`

      The content type. Always `output_text`.

      - `"output_text"`

  - `phase: "commentary" | "final_answer" | null`

    The phase of the assistant message.

    - `"commentary"`

      Commentary produced while the agent works.

    - `"final_answer"`

      The agent's final answer.

  - `role: "assistant"`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "message"`

    The item type. Always `message`.

    - `"message"`

### Agent Session Created Event

- `AgentSessionCreatedEvent`

  Emitted when a session is created.

  - `event_id: string`

    The unique ID of the event.

  - `session: AgentSession`

    The session that was created.

    - `id: string`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: string`

        The ID of the agent.

      - `instructions: string | null`

        Custom instructions appended to the agent's default base instructions.

      - `model: string`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: number | null`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: string | null`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: "none" | "minimal" | "low" | 4 more | null`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: "concise" | "detailed" | "auto" | null`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: "auto" | "default" | "flex" | 3 more`

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

          - `TextFormatResourceText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatResourceJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: "low" | "medium" | "high"`

          The amount of text produced by the agent. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

      - `tools: Array<AgentTool>`

        Tools available to the agent.

        - `AgentToolResourceFunction`

          A function defined by the application.

          - `defer_loading: boolean`

            Whether the function is deferred and discovered through tool search.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

        - `AgentToolResourceProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: boolean`

            Whether tools can be called from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `AgentToolResourceMcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array<string> | null`

            The MCP tools the agent may call.

          - `connection_origin: "service" | "environment"`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: string | null`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Record<string, unknown>`

            Metadata included with requests to this MCP server.

          - `required: boolean`

            Whether this MCP server must initialize before the first turn.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `McpTransportResourceHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

            - `McpTransportResourceStdio`

              Starts an MCP server as a local process.

              - `args: Array<string>`

                Arguments passed to the MCP server command.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `env_vars: Array<string>`

                Environment variable names inherited from the execution environment.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

        - `AgentToolResourceWebSearch`

          Web search.

          - `allowed_domains: Array<string> | null`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: "low" | "medium" | "high"`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Location | null`

            Approximate location used to localize search results, if provided.

            - `city: string | null`

              The city name.

            - `country: string | null`

              The two-letter ISO country code, such as `US`.

            - `region: string | null`

              The region or state name.

            - `timezone: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: "disabled" | "cached" | "live"`

            The source used for web search results.

            - `"disabled"`

            - `"cached"`

            - `"live"`

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

        - `AgentToolResourceComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: boolean`

            Whether computer tool outputs include screenshots.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: number`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `EnvironmentResourceNone`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentResourceOpenAIHosted`

        An environment hosted by OpenAI.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop`

          The effective desktop configuration.

          - `enabled: boolean`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array<HostedEnvironmentFile>`

          Files available in the environment, excluding their contents.

          - `HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileResourceInline`

            A file supplied inline when the session was created.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Network`

          The effective network access policy for the environment.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Array<string>`

            Domains the environment may access when network access is restricted.

        - `packages: Packages`

          Packages installed in the environment.

          - `npm: Array<string>`

            npm packages installed globally in the environment.

          - `python: Array<string>`

            Python packages installed in the environment.

          - `system: Array<string>`

            System packages installed in the environment.

        - `plugins: Array<HostedPlugin>`

          Plugins installed in the environment, excluding their archive contents.

          - `description: string`

            The installed plugin description.

          - `name: string`

            The installed plugin name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: Array<HostedSkill>`

          Skills installed in the environment, excluding their archive contents.

          - `HostedSkillReference`

            A skill installed from the Skills API.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `skill_id: string`

              The referenced skill ID.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: string`

              The concrete skill version installed for this session.

          - `HostedSkillResourceInline`

            A skill installed from an inline ZIP archive.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size?: "small" | "medium" | "large" | null`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `EnvironmentResourceSelfHosted`

        An environment hosted by the application.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: string | null`

      The error that caused the session to fail, if any.

    - `last_active_at: number`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the session.

    - `object: "agent.session"`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

      Actions that must be completed before the session can continue.

      - `SessionRequiredActionResourceComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          The information needed to render the request.

          - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: string | null`

              The registered form or frame origin where values will be entered.

            - `fields: Array<Field>`

              Controls to render. All submitted values are sensitive.

              - `id: string`

                The field ID to submit as field_id in a fields entry.

              - `label: string`

                The label to display beside the control.

              - `required: boolean`

                Whether this control requires a nonempty value.

              - `type: string`

                The rendering type, such as email, password, or text.

            - `options: Array<Option>`

              Sign-in methods. Empty for a plain form.

              - `id: string`

                The option ID to submit as selected_option.

              - `field_ids: Array<string>`

                IDs from the registered fields that this method accepts.

              - `label: string`

                The method label to display.

            - `reason: string | null`

              Why the agent needs the user to sign in.

            - `type: "browser_authentication"`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: string`

              The origin the browser needs permission to access.

            - `reason: string | null`

              The browser's explanation for this request, or null when unavailable.

            - `type: "browser_origin_access"`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: string`

          The registered request ID to echo when responding.

        - `turn_id: string`

          The turn that requested approval.

        - `type: "computer_use_approval_request"`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `SessionRequiredActionResourceFunctionCall`

        Run a function tool and submit its result.

        - `arguments: unknown`

          The arguments supplied by the model.

        - `call_id: string`

          The ID to include when submitting the function result.

        - `name: string`

          The function name.

        - `turn_id: string`

          The ID of the turn that requested the function call.

        - `type: "function_call"`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `SessionRequiredActionResourceEnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: string`

          The ID of the environment to reconnect.

        - `type: "environment_connection"`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: "idle" | "in_progress" | "requires_action" | "failed"`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: TokenUsage | null`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array<string>`

      The IDs of vaults made available to the session.

  - `type: "agent.session.created"`

    The type of the object. Always `agent.session.created`.

    - `"agent.session.created"`

### Agent Session Deleted

- `AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: string`

    The ID of the deleted session.

  - `deleted: boolean`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: "agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `"agent.session.deleted"`

### Agent Session Environment Connected Event

- `AgentSessionEnvironmentConnectedEvent`

  Emitted when a session environment connects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: string`

      The public ID of the environment.

    - `error: Error | null`

      The error reported while preparing the environment, if any.

      - `code: string`

        A machine-readable error code.

      - `message: string`

        A human-readable error message.

      - `type: string`

        The error type.

    - `status: "pending" | "ready" | "connected" | 2 more`

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

    - `type: string`

      The environment type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.environment.connected"`

    The type of the object. Always `agent.session.environment.connected`.

    - `"agent.session.environment.connected"`

### Agent Session Environment Disconnected Event

- `AgentSessionEnvironmentDisconnectedEvent`

  Emitted when a session environment disconnects.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: string`

      The public ID of the environment.

    - `error: Error | null`

      The error reported while preparing the environment, if any.

      - `code: string`

        A machine-readable error code.

      - `message: string`

        A human-readable error message.

      - `type: string`

        The error type.

    - `status: "pending" | "ready" | "connected" | 2 more`

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

    - `type: string`

      The environment type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.environment.disconnected"`

    The type of the object. Always `agent.session.environment.disconnected`.

    - `"agent.session.environment.disconnected"`

### Agent Session Environment Failed Event

- `AgentSessionEnvironmentFailedEvent`

  Emitted when a session environment fails.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: string`

      The public ID of the environment.

    - `error: Error | null`

      The error reported while preparing the environment, if any.

      - `code: string`

        A machine-readable error code.

      - `message: string`

        A human-readable error message.

      - `type: string`

        The error type.

    - `status: "pending" | "ready" | "connected" | 2 more`

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

    - `type: string`

      The environment type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.environment.failed"`

    The type of the object. Always `agent.session.environment.failed`.

    - `"agent.session.environment.failed"`

### Agent Session Environment Pending Event

- `AgentSessionEnvironmentPendingEvent`

  Emitted while a session environment is being prepared.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: string`

      The public ID of the environment.

    - `error: Error | null`

      The error reported while preparing the environment, if any.

      - `code: string`

        A machine-readable error code.

      - `message: string`

        A human-readable error message.

      - `type: string`

        The error type.

    - `status: "pending" | "ready" | "connected" | 2 more`

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

    - `type: string`

      The environment type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.environment.pending"`

    The type of the object. Always `agent.session.environment.pending`.

    - `"agent.session.environment.pending"`

### Agent Session Environment Ready Event

- `AgentSessionEnvironmentReadyEvent`

  Emitted when a hosted session environment is ready to connect.

  - `environment: AgentSessionEnvironmentState`

    The current environment state.

    - `id: string`

      The public ID of the environment.

    - `error: Error | null`

      The error reported while preparing the environment, if any.

      - `code: string`

        A machine-readable error code.

      - `message: string`

        A human-readable error message.

      - `type: string`

        The error type.

    - `status: "pending" | "ready" | "connected" | 2 more`

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

    - `type: string`

      The environment type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.environment.ready"`

    The type of the object. Always `agent.session.environment.ready`.

    - `"agent.session.environment.ready"`

### Agent Session Environment Reset Event

- `AgentSessionEnvironmentResetEvent`

  Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

  - `environment_id: string`

    The stable environment ID, retained across sandbox replacements.

  - `event_id: string`

    The unique ID of the event.

  - `reset_count: number`

    Monotonically increasing reset number. Repeated notifications share this number.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The associated turn, when applicable.

  - `type: "agent.session.environment.reset"`

    The type of the object. Always `agent.session.environment.reset`.

    - `"agent.session.environment.reset"`

### Agent Session Environment State

- `AgentSessionEnvironmentState`

  The current state of a session environment.

  - `id: string`

    The public ID of the environment.

  - `error: Error | null`

    The error reported while preparing the environment, if any.

    - `code: string`

      A machine-readable error code.

    - `message: string`

      A human-readable error message.

    - `type: string`

      The error type.

  - `status: "pending" | "ready" | "connected" | 2 more`

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

  - `type: string`

    The environment type.

### Agent Session Error Event

- `AgentSessionErrorEvent`

  Emitted when a turn or session fails.

  - `error: SessionError`

    The error that occurred.

    - `code: string | null`

      The machine-readable error code, if any.

    - `message: string`

      A customer-safe explanation of the error.

    - `param: string | null`

      The request parameter associated with the error, if any.

    - `type: string`

      The error type.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `type: "error"`

    The type of the object. Always `error`.

    - `"error"`

### Agent Session Event

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: string | null`

        The machine-readable error code, if any.

      - `message: string`

        A customer-safe explanation of the error.

      - `param: string | null`

        The request parameter associated with the error, if any.

      - `type: string`

        The error type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `type: "error"`

      The type of the object. Always `error`.

      - `"error"`

  - `AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: string`

        The public ID of the environment.

      - `error: Error | null`

        The error reported while preparing the environment, if any.

        - `code: string`

          A machine-readable error code.

        - `message: string`

          A human-readable error message.

        - `type: string`

          The error type.

      - `status: "pending" | "ready" | "connected" | 2 more`

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

      - `type: string`

        The environment type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: string`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: string`

      The unique ID of the event.

    - `reset_count: number`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The associated turn, when applicable.

    - `type: "agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: string`

      The output text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the command execution item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: string`

        The ID of the session.

      - `agent: Agent`

        The agent running in the session.

        - `id: string`

          The ID of the agent.

        - `instructions: string | null`

          Custom instructions appended to the agent's default base instructions.

        - `model: string`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: boolean`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: number | null`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: string | null`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

          - `effort: "none" | "minimal" | "low" | 4 more | null`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `"none"`

            - `"minimal"`

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `summary: "concise" | "detailed" | "auto" | null`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `"concise"`

              Returns a concise reasoning summary when supported.

            - `"detailed"`

              Returns a detailed reasoning summary when supported.

            - `"auto"`

              Automatically selects the most detailed summary supported by the model.

        - `service_tier: "auto" | "default" | "flex" | 3 more`

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

            - `TextFormatResourceText`

              Generates ordinary text without a structured-output constraint.

              - `type: "text"`

                The type of the object. Always `text`.

                - `"text"`

            - `TextFormatResourceJSONSchema`

              Constrains generated text to a JSON Schema.

              - `schema: Record<string, unknown>`

                The JSON Schema that generated text must match.

              - `type: "json_schema"`

                The type of the object. Always `json_schema`.

                - `"json_schema"`

          - `verbosity: "low" | "medium" | "high"`

            The amount of text produced by the agent. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

        - `tools: Array<AgentTool>`

          Tools available to the agent.

          - `AgentToolResourceFunction`

            A function defined by the application.

            - `defer_loading: boolean`

              Whether the function is deferred and discovered through tool search.

            - `description: string`

              A description of what the function does.

            - `name: string`

              The name of the function.

            - `parameters: Record<string, unknown>`

              A JSON Schema object describing the function's arguments.

            - `type: "function"`

              The type of the object. Always `function`.

              - `"function"`

          - `AgentToolResourceProgrammaticToolCalling`

            Enables calling tools from model-generated code.

            - `enabled: boolean`

              Whether tools can be called from model-generated code.

            - `type: "programmatic_tool_calling"`

              The type of the object. Always `programmatic_tool_calling`.

              - `"programmatic_tool_calling"`

          - `AgentToolResourceMcp`

            Tools provided by a remote MCP server.

            - `allowed_tools: Array<string> | null`

              The MCP tools the agent may call.

            - `connection_origin: "service" | "environment"`

              Where outbound MCP HTTP connections originate.

              - `"service"`

              - `"environment"`

            - `credential_id: string | null`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Record<string, unknown>`

              Metadata included with requests to this MCP server.

            - `required: boolean`

              Whether this MCP server must initialize before the first turn.

            - `server_label: string`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `McpTransportResourceHTTP`

                Connects to an MCP server over HTTP.

                - `server_url: string`

                  The URL of the MCP server.

                - `type: "http"`

                  The type of the object. Always `http`.

                  - `"http"`

              - `McpTransportResourceStdio`

                Starts an MCP server as a local process.

                - `args: Array<string>`

                  Arguments passed to the MCP server command.

                - `command: string`

                  The command used to start the MCP server.

                - `cwd: string`

                  The working directory used to start the MCP server.

                - `env_vars: Array<string>`

                  Environment variable names inherited from the execution environment.

                - `type: "stdio"`

                  The type of the object. Always `stdio`.

                  - `"stdio"`

            - `type: "mcp"`

              The type of the object. Always `mcp`.

              - `"mcp"`

          - `AgentToolResourceWebSearch`

            Web search.

            - `allowed_domains: Array<string> | null`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: "low" | "medium" | "high"`

              The amount of search context made available to the model. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

            - `location: Location | null`

              Approximate location used to localize search results, if provided.

              - `city: string | null`

                The city name.

              - `country: string | null`

                The two-letter ISO country code, such as `US`.

              - `region: string | null`

                The region or state name.

              - `timezone: string | null`

                The IANA timezone, such as `America/Los_Angeles`.

            - `mode: "disabled" | "cached" | "live"`

              The source used for web search results.

              - `"disabled"`

              - `"cached"`

              - `"live"`

            - `type: "web_search"`

              The type of the object. Always `web_search`.

              - `"web_search"`

          - `AgentToolResourceComputerUse`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: boolean`

              Whether computer tool outputs include screenshots.

            - `type: "computer_use"`

              The type of the object. Always `computer_use`.

              - `"computer_use"`

      - `created_at: number`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `EnvironmentResourceNone`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: "none"`

            The type of the object. Always `none`.

            - `"none"`

        - `EnvironmentResourceOpenAIHosted`

          An environment hosted by OpenAI.

          - `id: string`

            The public ID of the environment.

          - `capability_directories: Array<string>`

            Directories that contain capabilities exposed to the agent.

          - `desktop: Desktop`

            The effective desktop configuration.

            - `enabled: boolean`

              Whether the environment provisions a desktop and browser proxy.

          - `files: Array<HostedEnvironmentFile>`

            Files available in the environment, excluding their contents.

            - `HostedEnvironmentFileID`

              A file copied from the OpenAI Files API.

              - `id: string`

                The session-scoped ID of the file in the execution environment.

              - `file_id: string`

                The ID of the uploaded file.

              - `path: string`

                The file's absolute path inside the environment.

              - `size_bytes: number`

                The decoded file size in bytes.

              - `type: "file_id"`

                The type of the object. Always `file_id`.

                - `"file_id"`

            - `HostedEnvironmentFileResourceInline`

              A file supplied inline when the session was created.

              - `id: string`

                The session-scoped ID of the file in the execution environment.

              - `path: string`

                The file's absolute path inside the environment.

              - `size_bytes: number`

                The decoded file size in bytes.

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

          - `network: Network`

            The effective network access policy for the environment.

            - `access: "enabled" | "disabled" | "restricted"`

              The environment's network access mode.

              - `"enabled"`

                Allows unrestricted network access.

              - `"disabled"`

                Disables network access.

              - `"restricted"`

                Applies the configured domain restrictions.

            - `allowed_domains: Array<string>`

              Domains the environment may access when network access is restricted.

          - `packages: Packages`

            Packages installed in the environment.

            - `npm: Array<string>`

              npm packages installed globally in the environment.

            - `python: Array<string>`

              Python packages installed in the environment.

            - `system: Array<string>`

              System packages installed in the environment.

          - `plugins: Array<HostedPlugin>`

            Plugins installed in the environment, excluding their archive contents.

            - `description: string`

              The installed plugin description.

            - `name: string`

              The installed plugin name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

          - `skills: Array<HostedSkill>`

            Skills installed in the environment, excluding their archive contents.

            - `HostedSkillReference`

              A skill installed from the Skills API.

              - `description: string`

                The installed skill description.

              - `name: string`

                The installed skill name.

              - `skill_id: string`

                The referenced skill ID.

              - `type: "skill_reference"`

                The type of the object. Always `skill_reference`.

                - `"skill_reference"`

              - `version: string`

                The concrete skill version installed for this session.

            - `HostedSkillResourceInline`

              A skill installed from an inline ZIP archive.

              - `description: string`

                The installed skill description.

              - `name: string`

                The installed skill name.

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

          - `type: "openai_hosted"`

            The type of the object. Always `openai_hosted`.

            - `"openai_hosted"`

          - `container_size?: "small" | "medium" | "large" | null`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `"small"`

            - `"medium"`

            - `"large"`

        - `EnvironmentResourceSelfHosted`

          An environment hosted by the application.

          - `id: string`

            The public ID of the environment.

          - `capability_directories: Array<string>`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: string`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: "self_hosted"`

            The type of the object. Always `self_hosted`.

            - `"self_hosted"`

          - `workspace_directory: string`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: string | null`

        The error that caused the session to fail, if any.

      - `last_active_at: number`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Record<string, string>`

        Custom string key-value pairs attached to the session.

      - `object: "agent.session"`

        The object type. Always `agent.session`.

        - `"agent.session"`

      - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

        Actions that must be completed before the session can continue.

        - `SessionRequiredActionResourceComputerUseApprovalRequest`

          Respond to a computer-use request.

          - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            The information needed to render the request.

            - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

              A registered form awaiting the application's response.

              - `credential_origin: string | null`

                The registered form or frame origin where values will be entered.

              - `fields: Array<Field>`

                Controls to render. All submitted values are sensitive.

                - `id: string`

                  The field ID to submit as field_id in a fields entry.

                - `label: string`

                  The label to display beside the control.

                - `required: boolean`

                  Whether this control requires a nonempty value.

                - `type: string`

                  The rendering type, such as email, password, or text.

              - `options: Array<Option>`

                Sign-in methods. Empty for a plain form.

                - `id: string`

                  The option ID to submit as selected_option.

                - `field_ids: Array<string>`

                  IDs from the registered fields that this method accepts.

                - `label: string`

                  The method label to display.

              - `reason: string | null`

                Why the agent needs the user to sign in.

              - `type: "browser_authentication"`

                The type of the object. Always `browser_authentication`.

                - `"browser_authentication"`

            - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

              A browser origin awaiting the application's approval decision.

              - `origin: string`

                The origin the browser needs permission to access.

              - `reason: string | null`

                The browser's explanation for this request, or null when unavailable.

              - `type: "browser_origin_access"`

                The type of the object. Always `browser_origin_access`.

                - `"browser_origin_access"`

          - `request_id: string`

            The registered request ID to echo when responding.

          - `turn_id: string`

            The turn that requested approval.

          - `type: "computer_use_approval_request"`

            The type of the object. Always `computer_use_approval_request`.

            - `"computer_use_approval_request"`

        - `SessionRequiredActionResourceFunctionCall`

          Run a function tool and submit its result.

          - `arguments: unknown`

            The arguments supplied by the model.

          - `call_id: string`

            The ID to include when submitting the function result.

          - `name: string`

            The function name.

          - `turn_id: string`

            The ID of the turn that requested the function call.

          - `type: "function_call"`

            The type of the object. Always `function_call`.

            - `"function_call"`

        - `SessionRequiredActionResourceEnvironmentConnection`

          Reconnect a session environment.

          - `environment_id: string`

            The ID of the environment to reconnect.

          - `type: "environment_connection"`

            The type of the object. Always `environment_connection`.

            - `"environment_connection"`

      - `status: "idle" | "in_progress" | "requires_action" | "failed"`

        The current status of the session.

        - `"idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `"in_progress"`

          The session is processing a turn.

        - `"requires_action"`

          The session is waiting for one or more required actions.

        - `"failed"`

          The session failed.

      - `usage: TokenUsage | null`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: number`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails`

          A breakdown of the agent's input token usage.

          - `cached_tokens: number`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: number`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: number`

            The number of output tokens used for reasoning.

        - `total_tokens: number`

          The total number of input and output tokens used by the agent.

      - `vault_ids: Array<string>`

        The IDs of vaults made available to the session.

    - `type: "agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: string`

        The ID of the turn.

      - `agent_id: string`

        The ID of the agent that ran the turn.

      - `completed_at: number | null`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: number`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError | null`

        A customer-safe error. Non-null only for a failed turn.

        - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

        - `message: string`

          A customer-safe explanation of the failure.

      - `object: "agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: string`

        The ID of the session that owns the turn.

      - `started_at: number | null`

        The Unix timestamp, in seconds, when the turn started.

      - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

      - `subagent_id: string | null`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage | null`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: string | null`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array<AgentSessionMessageContent>`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `MessageContentResourceInputText`

            Text supplied by the user.

            - `text: string`

              The text supplied by the user.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `MessageContentResourceInputImage`

            An image supplied by the user.

            - `image_url: string`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `MessageContentResourceOutputText`

            Text produced by the assistant.

            - `text: string`

              The text produced by the assistant.

            - `type: "output_text"`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: "commentary" | "final_answer" | null`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "user" | "assistant"`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: string`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus | null`

          The status of the reasoning item.

        - `summary: Array<SummaryText>`

          The reasoning summaries produced by the agent.

          - `text: string`

            The reasoning summary text.

          - `type: "summary_text"`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "reasoning"`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: string`

          The ID of the function call item.

        - `arguments: unknown`

          The arguments to pass to the function.

        - `call_id: string`

          The ID used to submit the function result.

        - `name: string`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call"`

          The item type. Always `function_call`.

          - `"function_call"`

      - `FunctionCallOutputItemResource`

        The result supplied for a function call.

        - `id: string`

          The ID of the function call output item.

        - `call_id: string`

          The ID of the function call that produced this output.

        - `error: string | null`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput | null`

          The function result, if the call succeeded.

          - `string`

          - `Array<InputContent>`

            - `InputContentResourceInputText`

              Text input recorded in a session item.

              - `text: string`

                The text supplied to the agent.

              - `type: "input_text"`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `InputContentResourceInputImage`

              Image input recorded in a session item.

              - `image_url: string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: "input_image"`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call_output"`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `AgentMessageItemResource`

        A message exchanged between agent threads.

        - `id: string`

          The ID of the message.

        - `content: Array<AgentContent>`

          The content exchanged between the agents.

          - `OutputText`

            A text content part produced by the agent.

            - `text: string`

              The text produced by the agent.

            - `type: "output_text"`

              The content type. Always `output_text`.

              - `"output_text"`

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

            - `encrypted_content: string`

              The encrypted content payload.

            - `type: "encrypted_content"`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: string`

          The ID or name of the receiving agent.

        - `sender_agent_id: string`

          The ID or name of the sending agent.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "agent_message"`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: string`

          The ID of the MCP call item.

        - `arguments: unknown`

          The arguments passed to the MCP tool.

        - `error: unknown`

          The error returned by the MCP tool, if any.

        - `name: string`

          The name of the MCP tool.

        - `output: unknown`

          The output returned by the MCP tool, if any.

        - `server_label: string`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "mcp_call"`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `ComputerUseApprovalRequestResultItemResource`

        A credential-free record of an admitted response, not proof of completion.

        - `id: string`

          The stable history item ID.

        - `request_id: string`

          The registered request answered by this item.

        - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

          The admitted response, without submitted credential values.

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

            - `action: "submit"`

              - `"submit"`

            - `selected_option: string | null`

              The chosen sign-in method, or null when no options were offered.

            - `type: "browser_authentication"`

              - `"browser_authentication"`

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

            - `action: "cancel"`

              - `"cancel"`

            - `type: "browser_authentication"`

              - `"browser_authentication"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_approval_request_result"`

          - `"computer_use_approval_request_result"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: string`

          The ID of the web search call.

        - `action: WebSearchAction | null`

          The action performed by the web search tool.

          - `WebSearchActionResourceSearch`

            A search query or group of search queries.

            - `queries: Array<string> | null`

              The search queries, when multiple queries were used.

            - `query: string | null`

              The search query, when a single query was used.

            - `type: "search"`

              The type of the object. Always `search`.

              - `"search"`

          - `WebSearchActionResourceOpenPage`

            Opens a web page.

            - `type: "open_page"`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: string | null`

              The URL of the page that was opened.

          - `WebSearchActionResourceFindInPage`

            Finds text within a web page.

            - `pattern: string | null`

              The text pattern that was searched for.

            - `type: "find_in_page"`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: string | null`

              The URL of the page that was searched.

          - `WebSearchActionResourceOther`

            Another web search action.

            - `type: "other"`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "web_search_call"`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: string`

          The ID of the command execution item.

        - `command: string`

          The command that was executed.

        - `cwd: string | null`

          The working directory used to execute the command.

        - `duration_ms: number | null`

          The command duration in milliseconds.

        - `exit_code: number | null`

          The process exit code, if the command completed.

        - `output: string | null`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "command_execution"`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: string`

          The ID of the tool call item.

        - `agent_id: string`

          The ID of the agent that requested the subagent.

        - `content: Array<AgentContent>`

          The task given to the spawned agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `model: string | null`

          The model requested for the spawned agent.

        - `reasoning_effort: string | null`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "create_subagent_call"`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: string`

          The ID of the tool call item.

        - `content: Array<AgentContent>`

          The input sent to the receiving agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: string`

          The ID of the agent receiving the input.

        - `sender_agent_id: string`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "send_subagent_input_call"`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to resume.

        - `sender_agent_id: string`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "resume_subagent_call"`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_ids: Array<string>`

          The IDs of the agents to wait for.

        - `sender_agent_id: string`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "wait_for_subagents_call"`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to interrupt.

        - `sender_agent_id: string`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "interrupt_subagent_call"`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to close.

        - `sender_agent_id: string`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "close_subagent_call"`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: number | null`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: "agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: "agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: "agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: "agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: string`

        The ID of the subagent.

      - `closed_at: number | null`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array<AgentContent> | null`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `name: string | null`

        The runner-assigned nickname, or null when unavailable.

      - `object: "agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: number`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: string`

        The ID of the agent that created this subagent.

      - `session_id: string`

        The ID of the session that owns the subagent.

      - `status: "active" | "closed"`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: "agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: "agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: "agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: string`

          The ID of the message.

        - `content: Array<OutputText>`

          The content of the message.

          - `text: string`

            The text produced by the agent.

          - `type: "output_text"`

            The content type. Always `output_text`.

        - `phase: "commentary" | "final_answer" | null`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "assistant"`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

      - `AgentFunctionCallItem`

        A function call produced by the agent.

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: number`

      The index of the output item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: number`

      The index of the content part in the message.

    - `delta: string`

      The text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `text: string`

      The complete output text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `status: "incomplete" | null`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: number`

      The index of the summary part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: string`

      The summary text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `text: string`

      The complete reasoning summary text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

### Agent Session Failed Event

- `AgentSessionFailedEvent`

  Emitted when a session fails.

  - `event_id: string`

    The unique ID of the event.

  - `session: AgentSession`

    The failed session.

    - `id: string`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: string`

        The ID of the agent.

      - `instructions: string | null`

        Custom instructions appended to the agent's default base instructions.

      - `model: string`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: number | null`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: string | null`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: "none" | "minimal" | "low" | 4 more | null`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: "concise" | "detailed" | "auto" | null`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: "auto" | "default" | "flex" | 3 more`

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

          - `TextFormatResourceText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatResourceJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: "low" | "medium" | "high"`

          The amount of text produced by the agent. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

      - `tools: Array<AgentTool>`

        Tools available to the agent.

        - `AgentToolResourceFunction`

          A function defined by the application.

          - `defer_loading: boolean`

            Whether the function is deferred and discovered through tool search.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

        - `AgentToolResourceProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: boolean`

            Whether tools can be called from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `AgentToolResourceMcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array<string> | null`

            The MCP tools the agent may call.

          - `connection_origin: "service" | "environment"`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: string | null`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Record<string, unknown>`

            Metadata included with requests to this MCP server.

          - `required: boolean`

            Whether this MCP server must initialize before the first turn.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `McpTransportResourceHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

            - `McpTransportResourceStdio`

              Starts an MCP server as a local process.

              - `args: Array<string>`

                Arguments passed to the MCP server command.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `env_vars: Array<string>`

                Environment variable names inherited from the execution environment.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

        - `AgentToolResourceWebSearch`

          Web search.

          - `allowed_domains: Array<string> | null`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: "low" | "medium" | "high"`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Location | null`

            Approximate location used to localize search results, if provided.

            - `city: string | null`

              The city name.

            - `country: string | null`

              The two-letter ISO country code, such as `US`.

            - `region: string | null`

              The region or state name.

            - `timezone: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: "disabled" | "cached" | "live"`

            The source used for web search results.

            - `"disabled"`

            - `"cached"`

            - `"live"`

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

        - `AgentToolResourceComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: boolean`

            Whether computer tool outputs include screenshots.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: number`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `EnvironmentResourceNone`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentResourceOpenAIHosted`

        An environment hosted by OpenAI.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop`

          The effective desktop configuration.

          - `enabled: boolean`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array<HostedEnvironmentFile>`

          Files available in the environment, excluding their contents.

          - `HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileResourceInline`

            A file supplied inline when the session was created.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Network`

          The effective network access policy for the environment.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Array<string>`

            Domains the environment may access when network access is restricted.

        - `packages: Packages`

          Packages installed in the environment.

          - `npm: Array<string>`

            npm packages installed globally in the environment.

          - `python: Array<string>`

            Python packages installed in the environment.

          - `system: Array<string>`

            System packages installed in the environment.

        - `plugins: Array<HostedPlugin>`

          Plugins installed in the environment, excluding their archive contents.

          - `description: string`

            The installed plugin description.

          - `name: string`

            The installed plugin name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: Array<HostedSkill>`

          Skills installed in the environment, excluding their archive contents.

          - `HostedSkillReference`

            A skill installed from the Skills API.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `skill_id: string`

              The referenced skill ID.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: string`

              The concrete skill version installed for this session.

          - `HostedSkillResourceInline`

            A skill installed from an inline ZIP archive.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size?: "small" | "medium" | "large" | null`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `EnvironmentResourceSelfHosted`

        An environment hosted by the application.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: string | null`

      The error that caused the session to fail, if any.

    - `last_active_at: number`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the session.

    - `object: "agent.session"`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

      Actions that must be completed before the session can continue.

      - `SessionRequiredActionResourceComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          The information needed to render the request.

          - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: string | null`

              The registered form or frame origin where values will be entered.

            - `fields: Array<Field>`

              Controls to render. All submitted values are sensitive.

              - `id: string`

                The field ID to submit as field_id in a fields entry.

              - `label: string`

                The label to display beside the control.

              - `required: boolean`

                Whether this control requires a nonempty value.

              - `type: string`

                The rendering type, such as email, password, or text.

            - `options: Array<Option>`

              Sign-in methods. Empty for a plain form.

              - `id: string`

                The option ID to submit as selected_option.

              - `field_ids: Array<string>`

                IDs from the registered fields that this method accepts.

              - `label: string`

                The method label to display.

            - `reason: string | null`

              Why the agent needs the user to sign in.

            - `type: "browser_authentication"`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: string`

              The origin the browser needs permission to access.

            - `reason: string | null`

              The browser's explanation for this request, or null when unavailable.

            - `type: "browser_origin_access"`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: string`

          The registered request ID to echo when responding.

        - `turn_id: string`

          The turn that requested approval.

        - `type: "computer_use_approval_request"`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `SessionRequiredActionResourceFunctionCall`

        Run a function tool and submit its result.

        - `arguments: unknown`

          The arguments supplied by the model.

        - `call_id: string`

          The ID to include when submitting the function result.

        - `name: string`

          The function name.

        - `turn_id: string`

          The ID of the turn that requested the function call.

        - `type: "function_call"`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `SessionRequiredActionResourceEnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: string`

          The ID of the environment to reconnect.

        - `type: "environment_connection"`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: "idle" | "in_progress" | "requires_action" | "failed"`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: TokenUsage | null`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array<string>`

      The IDs of vaults made available to the session.

  - `type: "agent.session.failed"`

    The type of the object. Always `agent.session.failed`.

    - `"agent.session.failed"`

### Agent Session Idle Event

- `AgentSessionIdleEvent`

  Emitted when a session becomes idle.

  - `event_id: string`

    The unique ID of the event.

  - `session: AgentSession`

    The session that became idle.

    - `id: string`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: string`

        The ID of the agent.

      - `instructions: string | null`

        Custom instructions appended to the agent's default base instructions.

      - `model: string`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: number | null`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: string | null`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: "none" | "minimal" | "low" | 4 more | null`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: "concise" | "detailed" | "auto" | null`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: "auto" | "default" | "flex" | 3 more`

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

          - `TextFormatResourceText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatResourceJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: "low" | "medium" | "high"`

          The amount of text produced by the agent. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

      - `tools: Array<AgentTool>`

        Tools available to the agent.

        - `AgentToolResourceFunction`

          A function defined by the application.

          - `defer_loading: boolean`

            Whether the function is deferred and discovered through tool search.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

        - `AgentToolResourceProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: boolean`

            Whether tools can be called from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `AgentToolResourceMcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array<string> | null`

            The MCP tools the agent may call.

          - `connection_origin: "service" | "environment"`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: string | null`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Record<string, unknown>`

            Metadata included with requests to this MCP server.

          - `required: boolean`

            Whether this MCP server must initialize before the first turn.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `McpTransportResourceHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

            - `McpTransportResourceStdio`

              Starts an MCP server as a local process.

              - `args: Array<string>`

                Arguments passed to the MCP server command.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `env_vars: Array<string>`

                Environment variable names inherited from the execution environment.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

        - `AgentToolResourceWebSearch`

          Web search.

          - `allowed_domains: Array<string> | null`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: "low" | "medium" | "high"`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Location | null`

            Approximate location used to localize search results, if provided.

            - `city: string | null`

              The city name.

            - `country: string | null`

              The two-letter ISO country code, such as `US`.

            - `region: string | null`

              The region or state name.

            - `timezone: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: "disabled" | "cached" | "live"`

            The source used for web search results.

            - `"disabled"`

            - `"cached"`

            - `"live"`

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

        - `AgentToolResourceComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: boolean`

            Whether computer tool outputs include screenshots.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: number`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `EnvironmentResourceNone`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentResourceOpenAIHosted`

        An environment hosted by OpenAI.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop`

          The effective desktop configuration.

          - `enabled: boolean`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array<HostedEnvironmentFile>`

          Files available in the environment, excluding their contents.

          - `HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileResourceInline`

            A file supplied inline when the session was created.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Network`

          The effective network access policy for the environment.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Array<string>`

            Domains the environment may access when network access is restricted.

        - `packages: Packages`

          Packages installed in the environment.

          - `npm: Array<string>`

            npm packages installed globally in the environment.

          - `python: Array<string>`

            Python packages installed in the environment.

          - `system: Array<string>`

            System packages installed in the environment.

        - `plugins: Array<HostedPlugin>`

          Plugins installed in the environment, excluding their archive contents.

          - `description: string`

            The installed plugin description.

          - `name: string`

            The installed plugin name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: Array<HostedSkill>`

          Skills installed in the environment, excluding their archive contents.

          - `HostedSkillReference`

            A skill installed from the Skills API.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `skill_id: string`

              The referenced skill ID.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: string`

              The concrete skill version installed for this session.

          - `HostedSkillResourceInline`

            A skill installed from an inline ZIP archive.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size?: "small" | "medium" | "large" | null`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `EnvironmentResourceSelfHosted`

        An environment hosted by the application.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: string | null`

      The error that caused the session to fail, if any.

    - `last_active_at: number`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the session.

    - `object: "agent.session"`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

      Actions that must be completed before the session can continue.

      - `SessionRequiredActionResourceComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          The information needed to render the request.

          - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: string | null`

              The registered form or frame origin where values will be entered.

            - `fields: Array<Field>`

              Controls to render. All submitted values are sensitive.

              - `id: string`

                The field ID to submit as field_id in a fields entry.

              - `label: string`

                The label to display beside the control.

              - `required: boolean`

                Whether this control requires a nonempty value.

              - `type: string`

                The rendering type, such as email, password, or text.

            - `options: Array<Option>`

              Sign-in methods. Empty for a plain form.

              - `id: string`

                The option ID to submit as selected_option.

              - `field_ids: Array<string>`

                IDs from the registered fields that this method accepts.

              - `label: string`

                The method label to display.

            - `reason: string | null`

              Why the agent needs the user to sign in.

            - `type: "browser_authentication"`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: string`

              The origin the browser needs permission to access.

            - `reason: string | null`

              The browser's explanation for this request, or null when unavailable.

            - `type: "browser_origin_access"`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: string`

          The registered request ID to echo when responding.

        - `turn_id: string`

          The turn that requested approval.

        - `type: "computer_use_approval_request"`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `SessionRequiredActionResourceFunctionCall`

        Run a function tool and submit its result.

        - `arguments: unknown`

          The arguments supplied by the model.

        - `call_id: string`

          The ID to include when submitting the function result.

        - `name: string`

          The function name.

        - `turn_id: string`

          The ID of the turn that requested the function call.

        - `type: "function_call"`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `SessionRequiredActionResourceEnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: string`

          The ID of the environment to reconnect.

        - `type: "environment_connection"`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: "idle" | "in_progress" | "requires_action" | "failed"`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: TokenUsage | null`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array<string>`

      The IDs of vaults made available to the session.

  - `type: "agent.session.idle"`

    The type of the object. Always `agent.session.idle`.

    - `"agent.session.idle"`

### Agent Session In Progress Event

- `AgentSessionInProgressEvent`

  Emitted when a session starts processing a turn.

  - `event_id: string`

    The unique ID of the event.

  - `session: AgentSession`

    The session that started processing.

    - `id: string`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: string`

        The ID of the agent.

      - `instructions: string | null`

        Custom instructions appended to the agent's default base instructions.

      - `model: string`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: number | null`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: string | null`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: "none" | "minimal" | "low" | 4 more | null`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: "concise" | "detailed" | "auto" | null`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: "auto" | "default" | "flex" | 3 more`

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

          - `TextFormatResourceText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatResourceJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: "low" | "medium" | "high"`

          The amount of text produced by the agent. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

      - `tools: Array<AgentTool>`

        Tools available to the agent.

        - `AgentToolResourceFunction`

          A function defined by the application.

          - `defer_loading: boolean`

            Whether the function is deferred and discovered through tool search.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

        - `AgentToolResourceProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: boolean`

            Whether tools can be called from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `AgentToolResourceMcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array<string> | null`

            The MCP tools the agent may call.

          - `connection_origin: "service" | "environment"`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: string | null`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Record<string, unknown>`

            Metadata included with requests to this MCP server.

          - `required: boolean`

            Whether this MCP server must initialize before the first turn.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `McpTransportResourceHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

            - `McpTransportResourceStdio`

              Starts an MCP server as a local process.

              - `args: Array<string>`

                Arguments passed to the MCP server command.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `env_vars: Array<string>`

                Environment variable names inherited from the execution environment.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

        - `AgentToolResourceWebSearch`

          Web search.

          - `allowed_domains: Array<string> | null`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: "low" | "medium" | "high"`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Location | null`

            Approximate location used to localize search results, if provided.

            - `city: string | null`

              The city name.

            - `country: string | null`

              The two-letter ISO country code, such as `US`.

            - `region: string | null`

              The region or state name.

            - `timezone: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: "disabled" | "cached" | "live"`

            The source used for web search results.

            - `"disabled"`

            - `"cached"`

            - `"live"`

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

        - `AgentToolResourceComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: boolean`

            Whether computer tool outputs include screenshots.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: number`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `EnvironmentResourceNone`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentResourceOpenAIHosted`

        An environment hosted by OpenAI.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop`

          The effective desktop configuration.

          - `enabled: boolean`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array<HostedEnvironmentFile>`

          Files available in the environment, excluding their contents.

          - `HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileResourceInline`

            A file supplied inline when the session was created.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Network`

          The effective network access policy for the environment.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Array<string>`

            Domains the environment may access when network access is restricted.

        - `packages: Packages`

          Packages installed in the environment.

          - `npm: Array<string>`

            npm packages installed globally in the environment.

          - `python: Array<string>`

            Python packages installed in the environment.

          - `system: Array<string>`

            System packages installed in the environment.

        - `plugins: Array<HostedPlugin>`

          Plugins installed in the environment, excluding their archive contents.

          - `description: string`

            The installed plugin description.

          - `name: string`

            The installed plugin name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: Array<HostedSkill>`

          Skills installed in the environment, excluding their archive contents.

          - `HostedSkillReference`

            A skill installed from the Skills API.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `skill_id: string`

              The referenced skill ID.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: string`

              The concrete skill version installed for this session.

          - `HostedSkillResourceInline`

            A skill installed from an inline ZIP archive.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size?: "small" | "medium" | "large" | null`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `EnvironmentResourceSelfHosted`

        An environment hosted by the application.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: string | null`

      The error that caused the session to fail, if any.

    - `last_active_at: number`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the session.

    - `object: "agent.session"`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

      Actions that must be completed before the session can continue.

      - `SessionRequiredActionResourceComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          The information needed to render the request.

          - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: string | null`

              The registered form or frame origin where values will be entered.

            - `fields: Array<Field>`

              Controls to render. All submitted values are sensitive.

              - `id: string`

                The field ID to submit as field_id in a fields entry.

              - `label: string`

                The label to display beside the control.

              - `required: boolean`

                Whether this control requires a nonempty value.

              - `type: string`

                The rendering type, such as email, password, or text.

            - `options: Array<Option>`

              Sign-in methods. Empty for a plain form.

              - `id: string`

                The option ID to submit as selected_option.

              - `field_ids: Array<string>`

                IDs from the registered fields that this method accepts.

              - `label: string`

                The method label to display.

            - `reason: string | null`

              Why the agent needs the user to sign in.

            - `type: "browser_authentication"`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: string`

              The origin the browser needs permission to access.

            - `reason: string | null`

              The browser's explanation for this request, or null when unavailable.

            - `type: "browser_origin_access"`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: string`

          The registered request ID to echo when responding.

        - `turn_id: string`

          The turn that requested approval.

        - `type: "computer_use_approval_request"`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `SessionRequiredActionResourceFunctionCall`

        Run a function tool and submit its result.

        - `arguments: unknown`

          The arguments supplied by the model.

        - `call_id: string`

          The ID to include when submitting the function result.

        - `name: string`

          The function name.

        - `turn_id: string`

          The ID of the turn that requested the function call.

        - `type: "function_call"`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `SessionRequiredActionResourceEnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: string`

          The ID of the environment to reconnect.

        - `type: "environment_connection"`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: "idle" | "in_progress" | "requires_action" | "failed"`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: TokenUsage | null`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array<string>`

      The IDs of vaults made available to the session.

  - `type: "agent.session.in_progress"`

    The type of the object. Always `agent.session.in_progress`.

    - `"agent.session.in_progress"`

### Agent Session Input Message Param

- `AgentSessionInputMessageParam`

  A user message submitted to a session.

  - `content: Array<InputContentParam>`

    The content of the message.

    - `InputContentParamInputText`

      Text input to the model.

      - `text: string`

        The text sent to the model.

      - `type: "input_text"`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `InputContentParamInputImage`

      Image input to the model.

      - `image_url: string`

        The URL of the image sent to the model.

      - `type: "input_image"`

        The type of the object. Always `input_image`.

        - `"input_image"`

  - `role: "user"`

    The role of the message author. Always `user`.

    - `"user"`

  - `type?: "message"`

    The type of the input item. Always `message`.

    - `"message"`

### Agent Session Input Param

- `AgentSessionInputParam = SessionInputParamAgentSessionInputComputerUseApprovalRequestResult | SessionInputParamAgentSessionInputMessage | SessionInputParamAgentSessionInputCancel | SessionInputParamAgentSessionInputToolResult`

  Input submitted to an existing session.

  - `SessionInputParamAgentSessionInputComputerUseApprovalRequestResult`

    Responds to a pending Computer Use approval request.

    - `request_id: string`

      The registered request ID from the required action.

    - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

      The response for this request type.

      - `AgentBrowserAuthenticationSubmitParam`

        - `action: "submit"`

          - `"submit"`

        - `fields: Array<Field>`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: string`

            The field ID from the required action.

          - `value: string`

            The value to enter into the registered control.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

        - `selected_option?: string | null`

          The chosen method. Required when the required action contains options.

      - `AgentBrowserAuthenticationCancelParam`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `AgentBrowserOriginAccessParam`

        - `decision: "approve" | "deny" | "cancel"`

          Whether to allow, deny, or cancel the requested origin access.

          - `"approve"`

            Allow the browser to access this origin.

          - `"deny"`

            Deny access to this origin.

          - `"cancel"`

            Dismiss this request without approving access.

        - `type: "browser_origin_access"`

          - `"browser_origin_access"`

    - `type: "agent.session.input.computer_use_approval_request_result"`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `"agent.session.input.computer_use_approval_request_result"`

  - `SessionInputParamAgentSessionInputMessage`

    Adds one or more user messages and starts a turn.

    - `input: Array<AgentSessionInputMessageParam>`

      The user messages to add to the session.

      - `content: Array<InputContentParam>`

        The content of the message.

        - `InputContentParamInputText`

          Text input to the model.

          - `text: string`

            The text sent to the model.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentParamInputImage`

          Image input to the model.

          - `image_url: string`

            The URL of the image sent to the model.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: "user"`

        The role of the message author. Always `user`.

        - `"user"`

      - `type?: "message"`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: "agent.session.input.message"`

      The type of the object. Always `agent.session.input.message`.

      - `"agent.session.input.message"`

  - `SessionInputParamAgentSessionInputCancel`

    Cancels the session's active turn.

    - `type: "agent.session.input.cancel"`

      The type of the object. Always `agent.session.input.cancel`.

      - `"agent.session.input.cancel"`

  - `SessionInputParamAgentSessionInputToolResult`

    Submits the result of a function call.

    - `call_id: string`

      The ID of the function call.

    - `success: boolean`

      Whether the function call succeeded.

    - `turn_id: string`

      The ID of the turn that requested the function call.

    - `type: "agent.session.input.tool_result"`

      The type of the object. Always `agent.session.input.tool_result`.

      - `"agent.session.input.tool_result"`

    - `error?: string | null`

      The error message when the call failed.

    - `output?: AgentFunctionCallOutputParam | null`

      The function result when the call succeeded.

      - `string`

      - `Array<InputContentParam>`

        - `InputContentParamInputText`

          Text input to the model.

        - `InputContentParamInputImage`

          Image input to the model.

### Agent Session Item

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: string | null`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

        - `type: "output_text"`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "user" | "assistant"`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

    - `call_id: string`

      The ID of the function call that produced this output.

    - `error: string | null`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

    - `sender_agent_id: string`

      The ID or name of the sending agent.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

    - `request_id: string`

      The registered request answered by this item.

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Agent Session Message

- `AgentSessionMessage`

  A user or assistant message recorded in a session.

  - `id: string | null`

    The ID of this item, or null for legacy user messages whose ID was not recorded.

  - `content: Array<AgentSessionMessageContent>`

    The content of the message. User messages contain input text or images; assistant messages contain output text.

    - `MessageContentResourceInputText`

      Text supplied by the user.

      - `text: string`

        The text supplied by the user.

      - `type: "input_text"`

        The type of the object. Always `input_text`.

        - `"input_text"`

    - `MessageContentResourceInputImage`

      An image supplied by the user.

      - `image_url: string`

        The URL of the image supplied by the user, which may be a base64-encoded data URL.

      - `type: "input_image"`

        The type of the object. Always `input_image`.

        - `"input_image"`

    - `MessageContentResourceOutputText`

      Text produced by the assistant.

      - `text: string`

        The text produced by the assistant.

      - `type: "output_text"`

        The type of the object. Always `output_text`.

        - `"output_text"`

  - `phase: "commentary" | "final_answer" | null`

    The phase of an assistant message. Null for user messages.

    - `"commentary"`

      Commentary produced while the agent works.

    - `"final_answer"`

      The agent's final answer.

  - `role: "user" | "assistant"`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "message"`

    The item type. Always `message`.

    - `"message"`

### Agent Session Message Content

- `AgentSessionMessageContent = MessageContentResourceInputText | MessageContentResourceInputImage | MessageContentResourceOutputText`

  A content part in a session message.

  - `MessageContentResourceInputText`

    Text supplied by the user.

    - `text: string`

      The text supplied by the user.

    - `type: "input_text"`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `MessageContentResourceInputImage`

    An image supplied by the user.

    - `image_url: string`

      The URL of the image supplied by the user, which may be a base64-encoded data URL.

    - `type: "input_image"`

      The type of the object. Always `input_image`.

      - `"input_image"`

  - `MessageContentResourceOutputText`

    Text produced by the assistant.

    - `text: string`

      The text produced by the assistant.

    - `type: "output_text"`

      The type of the object. Always `output_text`.

      - `"output_text"`

### Agent Session Requires Action Event

- `AgentSessionRequiresActionEvent`

  Emitted when a session is waiting for one or more required actions.

  - `event_id: string`

    The unique ID of the event.

  - `session: AgentSession`

    The session and its current required actions.

    - `id: string`

      The ID of the session.

    - `agent: Agent`

      The agent running in the session.

      - `id: string`

        The ID of the agent.

      - `instructions: string | null`

        Custom instructions appended to the agent's default base instructions.

      - `model: string`

        The model used by the agent.

      - `multi_agent: MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled. Defaults to false.

        - `max_concurrent_subagents: number | null`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `name: string | null`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `reasoning: AgentReasoning`

        The agent's reasoning configuration.

        - `effort: "none" | "minimal" | "low" | 4 more | null`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary: "concise" | "detailed" | "auto" | null`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier: "auto" | "default" | "flex" | 3 more`

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

          - `TextFormatResourceText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatResourceJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity: "low" | "medium" | "high"`

          The amount of text produced by the agent. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

      - `tools: Array<AgentTool>`

        Tools available to the agent.

        - `AgentToolResourceFunction`

          A function defined by the application.

          - `defer_loading: boolean`

            Whether the function is deferred and discovered through tool search.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

        - `AgentToolResourceProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `enabled: boolean`

            Whether tools can be called from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

        - `AgentToolResourceMcp`

          Tools provided by a remote MCP server.

          - `allowed_tools: Array<string> | null`

            The MCP tools the agent may call.

          - `connection_origin: "service" | "environment"`

            Where outbound MCP HTTP connections originate.

            - `"service"`

            - `"environment"`

          - `credential_id: string | null`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `request_metadata: Record<string, unknown>`

            Metadata included with requests to this MCP server.

          - `required: boolean`

            Whether this MCP server must initialize before the first turn.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransport`

            The transport used to connect to the MCP server.

            - `McpTransportResourceHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

            - `McpTransportResourceStdio`

              Starts an MCP server as a local process.

              - `args: Array<string>`

                Arguments passed to the MCP server command.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `env_vars: Array<string>`

                Environment variable names inherited from the execution environment.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

        - `AgentToolResourceWebSearch`

          Web search.

          - `allowed_domains: Array<string> | null`

            Allowed search domains, or `null` when the search is unrestricted.

          - `context_size: "low" | "medium" | "high"`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location: Location | null`

            Approximate location used to localize search results, if provided.

            - `city: string | null`

              The city name.

            - `country: string | null`

              The two-letter ISO country code, such as `US`.

            - `region: string | null`

              The region or state name.

            - `timezone: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode: "disabled" | "cached" | "live"`

            The source used for web search results.

            - `"disabled"`

            - `"cached"`

            - `"live"`

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

        - `AgentToolResourceComputerUse`

          Browser use in an OpenAI-hosted session.

          - `include_screenshots: boolean`

            Whether computer tool outputs include screenshots.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

    - `created_at: number`

      The Unix timestamp, in seconds, when the session was created.

    - `environment: Environment`

      The execution environment for the session.

      - `EnvironmentResourceNone`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentResourceOpenAIHosted`

        An environment hosted by OpenAI.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `desktop: Desktop`

          The effective desktop configuration.

          - `enabled: boolean`

            Whether the environment provisions a desktop and browser proxy.

        - `files: Array<HostedEnvironmentFile>`

          Files available in the environment, excluding their contents.

          - `HostedEnvironmentFileID`

            A file copied from the OpenAI Files API.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileResourceInline`

            A file supplied inline when the session was created.

            - `id: string`

              The session-scoped ID of the file in the execution environment.

            - `path: string`

              The file's absolute path inside the environment.

            - `size_bytes: number`

              The decoded file size in bytes.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network: Network`

          The effective network access policy for the environment.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains: Array<string>`

            Domains the environment may access when network access is restricted.

        - `packages: Packages`

          Packages installed in the environment.

          - `npm: Array<string>`

            npm packages installed globally in the environment.

          - `python: Array<string>`

            Python packages installed in the environment.

          - `system: Array<string>`

            System packages installed in the environment.

        - `plugins: Array<HostedPlugin>`

          Plugins installed in the environment, excluding their archive contents.

          - `description: string`

            The installed plugin description.

          - `name: string`

            The installed plugin name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `skills: Array<HostedSkill>`

          Skills installed in the environment, excluding their archive contents.

          - `HostedSkillReference`

            A skill installed from the Skills API.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `skill_id: string`

              The referenced skill ID.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version: string`

              The concrete skill version installed for this session.

          - `HostedSkillResourceInline`

            A skill installed from an inline ZIP archive.

            - `description: string`

              The installed skill description.

            - `name: string`

              The installed skill name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `container_size?: "small" | "medium" | "large" | null`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `"small"`

          - `"medium"`

          - `"large"`

      - `EnvironmentResourceSelfHosted`

        An environment hosted by the application.

        - `id: string`

          The public ID of the environment.

        - `capability_directories: Array<string>`

          Directories that contain capabilities exposed to the agent.

        - `remote_url: string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `error: string | null`

      The error that caused the session to fail, if any.

    - `last_active_at: number`

      The Unix timestamp, in seconds, when the session was last active.

    - `metadata: Record<string, string>`

      Custom string key-value pairs attached to the session.

    - `object: "agent.session"`

      The object type. Always `agent.session`.

      - `"agent.session"`

    - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

      Actions that must be completed before the session can continue.

      - `SessionRequiredActionResourceComputerUseApprovalRequest`

        Respond to a computer-use request.

        - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          The information needed to render the request.

          - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

            A registered form awaiting the application's response.

            - `credential_origin: string | null`

              The registered form or frame origin where values will be entered.

            - `fields: Array<Field>`

              Controls to render. All submitted values are sensitive.

              - `id: string`

                The field ID to submit as field_id in a fields entry.

              - `label: string`

                The label to display beside the control.

              - `required: boolean`

                Whether this control requires a nonempty value.

              - `type: string`

                The rendering type, such as email, password, or text.

            - `options: Array<Option>`

              Sign-in methods. Empty for a plain form.

              - `id: string`

                The option ID to submit as selected_option.

              - `field_ids: Array<string>`

                IDs from the registered fields that this method accepts.

              - `label: string`

                The method label to display.

            - `reason: string | null`

              Why the agent needs the user to sign in.

            - `type: "browser_authentication"`

              The type of the object. Always `browser_authentication`.

              - `"browser_authentication"`

          - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            A browser origin awaiting the application's approval decision.

            - `origin: string`

              The origin the browser needs permission to access.

            - `reason: string | null`

              The browser's explanation for this request, or null when unavailable.

            - `type: "browser_origin_access"`

              The type of the object. Always `browser_origin_access`.

              - `"browser_origin_access"`

        - `request_id: string`

          The registered request ID to echo when responding.

        - `turn_id: string`

          The turn that requested approval.

        - `type: "computer_use_approval_request"`

          The type of the object. Always `computer_use_approval_request`.

          - `"computer_use_approval_request"`

      - `SessionRequiredActionResourceFunctionCall`

        Run a function tool and submit its result.

        - `arguments: unknown`

          The arguments supplied by the model.

        - `call_id: string`

          The ID to include when submitting the function result.

        - `name: string`

          The function name.

        - `turn_id: string`

          The ID of the turn that requested the function call.

        - `type: "function_call"`

          The type of the object. Always `function_call`.

          - `"function_call"`

      - `SessionRequiredActionResourceEnvironmentConnection`

        Reconnect a session environment.

        - `environment_id: string`

          The ID of the environment to reconnect.

        - `type: "environment_connection"`

          The type of the object. Always `environment_connection`.

          - `"environment_connection"`

    - `status: "idle" | "in_progress" | "requires_action" | "failed"`

      The current status of the session.

      - `"idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `"in_progress"`

        The session is processing a turn.

      - `"requires_action"`

        The session is waiting for one or more required actions.

      - `"failed"`

        The session failed.

    - `usage: TokenUsage | null`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

    - `vault_ids: Array<string>`

      The IDs of vaults made available to the session.

  - `type: "agent.session.requires_action"`

    The type of the object. Always `agent.session.requires_action`.

    - `"agent.session.requires_action"`

### Agent Session Subagent Active Event

- `AgentSessionSubagentActiveEvent`

  Emitted when a closed subagent successfully resumes.

  - `event_id: string`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that resumed.

    - `id: string`

      The ID of the subagent.

    - `closed_at: number | null`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array<AgentContent> | null`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: string | null`

      The runner-assigned nickname, or null when unavailable.

    - `object: "agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: number`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: string`

      The ID of the agent that created this subagent.

    - `session_id: string`

      The ID of the session that owns the subagent.

    - `status: "active" | "closed"`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: "agent.session.subagent.active"`

    The type of the object. Always `agent.session.subagent.active`.

    - `"agent.session.subagent.active"`

### Agent Session Subagent Closed Event

- `AgentSessionSubagentClosedEvent`

  Emitted when a subagent is closed.

  - `event_id: string`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was closed.

    - `id: string`

      The ID of the subagent.

    - `closed_at: number | null`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array<AgentContent> | null`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: string | null`

      The runner-assigned nickname, or null when unavailable.

    - `object: "agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: number`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: string`

      The ID of the agent that created this subagent.

    - `session_id: string`

      The ID of the session that owns the subagent.

    - `status: "active" | "closed"`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: "agent.session.subagent.closed"`

    The type of the object. Always `agent.session.subagent.closed`.

    - `"agent.session.subagent.closed"`

### Agent Session Subagent Created Event

- `AgentSessionSubagentCreatedEvent`

  Emitted when a subagent is created.

  - `event_id: string`

    The unique ID of the event.

  - `subagent: Subagent`

    The subagent that was created.

    - `id: string`

      The ID of the subagent.

    - `closed_at: number | null`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `instructions: Array<AgentContent> | null`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `name: string | null`

      The runner-assigned nickname, or null when unavailable.

    - `object: "agent.session.subagent"`

      The object type. Always `agent.session.subagent`.

      - `"agent.session.subagent"`

    - `opened_at: number`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `parent_agent_id: string`

      The ID of the agent that created this subagent.

    - `session_id: string`

      The ID of the session that owns the subagent.

    - `status: "active" | "closed"`

      The current status of the subagent.

      - `"active"`

        The subagent remains available, including while idle between turns.

      - `"closed"`

        The subagent is closed.

  - `type: "agent.session.subagent.created"`

    The type of the object. Always `agent.session.subagent.created`.

    - `"agent.session.subagent.created"`

### Agent Session Turn Cancelled Event

- `AgentSessionTurnCancelledEvent`

  Emitted when a turn is cancelled.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn: Turn`

    The cancelled turn.

    - `id: string`

      The ID of the turn.

    - `agent_id: string`

      The ID of the agent that ran the turn.

    - `completed_at: number | null`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: number`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError | null`

      A customer-safe error. Non-null only for a failed turn.

      - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

      - `message: string`

        A customer-safe explanation of the failure.

    - `object: "agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: string`

      The ID of the session that owns the turn.

    - `started_at: number | null`

      The Unix timestamp, in seconds, when the turn started.

    - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

    - `subagent_id: string | null`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage | null`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

  - `turn_id: string`

    The ID of the turn associated with the event.

  - `type: "agent.session.turn.cancelled"`

    The type of the object. Always `agent.session.turn.cancelled`.

    - `"agent.session.turn.cancelled"`

  - `usage: TokenUsage | null`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Completed Event

- `AgentSessionTurnCompletedEvent`

  Emitted when a turn completes.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn: Turn`

    The completed turn.

    - `id: string`

      The ID of the turn.

    - `agent_id: string`

      The ID of the agent that ran the turn.

    - `completed_at: number | null`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: number`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError | null`

      A customer-safe error. Non-null only for a failed turn.

      - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

      - `message: string`

        A customer-safe explanation of the failure.

    - `object: "agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: string`

      The ID of the session that owns the turn.

    - `started_at: number | null`

      The Unix timestamp, in seconds, when the turn started.

    - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

    - `subagent_id: string | null`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage | null`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

  - `turn_id: string`

    The ID of the turn associated with the event.

  - `type: "agent.session.turn.completed"`

    The type of the object. Always `agent.session.turn.completed`.

    - `"agent.session.turn.completed"`

  - `usage: TokenUsage | null`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Content Part Added Event

- `AgentSessionTurnContentPartAddedEvent`

  Emitted when an output text content part is added.

  - `content_index: number`

    The index of the content part in the message.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the message item.

  - `output_index: number`

    The index of the item in the turn output.

  - `part: OutputText`

    The initial content part.

    - `text: string`

      The text produced by the agent.

    - `type: "output_text"`

      The content type. Always `output_text`.

      - `"output_text"`

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.content_part.added"`

    The type of the object. Always `agent.session.turn.content_part.added`.

    - `"agent.session.turn.content_part.added"`

### Agent Session Turn Content Part Done Event

- `AgentSessionTurnContentPartDoneEvent`

  Emitted when an output content part is complete.

  - `content_index: number`

    The index of the content part in the message.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the message item.

  - `output_index: number`

    The index of the item in the turn output.

  - `part: OutputText`

    The completed content part.

    - `text: string`

      The text produced by the agent.

    - `type: "output_text"`

      The content type. Always `output_text`.

      - `"output_text"`

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.content_part.done"`

    The type of the object. Always `agent.session.turn.content_part.done`.

    - `"agent.session.turn.content_part.done"`

### Agent Session Turn Created Event

- `AgentSessionTurnCreatedEvent`

  Emitted when a turn is created.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it was created.

    - `id: string`

      The ID of the turn.

    - `agent_id: string`

      The ID of the agent that ran the turn.

    - `completed_at: number | null`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: number`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError | null`

      A customer-safe error. Non-null only for a failed turn.

      - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

      - `message: string`

        A customer-safe explanation of the failure.

    - `object: "agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: string`

      The ID of the session that owns the turn.

    - `started_at: number | null`

      The Unix timestamp, in seconds, when the turn started.

    - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

    - `subagent_id: string | null`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage | null`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

  - `turn_id: string`

    The ID of the turn associated with the event.

  - `type: "agent.session.turn.created"`

    The type of the object. Always `agent.session.turn.created`.

    - `"agent.session.turn.created"`

### Agent Session Turn Failed Event

- `AgentSessionTurnFailedEvent`

  Emitted when a turn fails.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn: Turn`

    The failed turn.

    - `id: string`

      The ID of the turn.

    - `agent_id: string`

      The ID of the agent that ran the turn.

    - `completed_at: number | null`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: number`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError | null`

      A customer-safe error. Non-null only for a failed turn.

      - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

      - `message: string`

        A customer-safe explanation of the failure.

    - `object: "agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: string`

      The ID of the session that owns the turn.

    - `started_at: number | null`

      The Unix timestamp, in seconds, when the turn started.

    - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

    - `subagent_id: string | null`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage | null`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

  - `turn_id: string`

    The ID of the turn associated with the event.

  - `type: "agent.session.turn.failed"`

    The type of the object. Always `agent.session.turn.failed`.

    - `"agent.session.turn.failed"`

  - `usage: TokenUsage | null`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn In Progress Event

- `AgentSessionTurnInProgressEvent`

  Emitted when a turn starts running.

  - `event_id: string`

    The unique ID of the event.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn: Turn`

    The turn at the time it started running.

    - `id: string`

      The ID of the turn.

    - `agent_id: string`

      The ID of the agent that ran the turn.

    - `completed_at: number | null`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `created_at: number`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `error: SessionTurnError | null`

      A customer-safe error. Non-null only for a failed turn.

      - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

      - `message: string`

        A customer-safe explanation of the failure.

    - `object: "agent.session.turn"`

      The object type. Always `agent.session.turn`.

      - `"agent.session.turn"`

    - `session_id: string`

      The ID of the session that owns the turn.

    - `started_at: number | null`

      The Unix timestamp, in seconds, when the turn started.

    - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

    - `subagent_id: string | null`

      The ID of the subagent that ran the turn, if applicable.

    - `usage: TokenUsage | null`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `input_tokens: number`

        The number of input tokens used by the agent.

      - `input_tokens_details: InputTokensDetails`

        A breakdown of the agent's input token usage.

        - `cached_tokens: number`

          The number of input tokens retrieved from the prompt cache.

      - `output_tokens: number`

        The number of output tokens generated by the agent.

      - `output_tokens_details: OutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `reasoning_tokens: number`

          The number of output tokens used for reasoning.

      - `total_tokens: number`

        The total number of input and output tokens used by the agent.

  - `turn_id: string`

    The ID of the turn associated with the event.

  - `type: "agent.session.turn.in_progress"`

    The type of the object. Always `agent.session.turn.in_progress`.

    - `"agent.session.turn.in_progress"`

### Agent Session Turn Item Added Event

- `AgentSessionTurnItemAddedEvent`

  Emitted when an item is added to a turn.

  - `event_id: string`

    The unique ID of the event.

  - `item: AgentSessionItem`

    The item that was added.

    - `AgentSessionMessage`

      A user or assistant message recorded in a session.

      - `id: string | null`

        The ID of this item, or null for legacy user messages whose ID was not recorded.

      - `content: Array<AgentSessionMessageContent>`

        The content of the message. User messages contain input text or images; assistant messages contain output text.

        - `MessageContentResourceInputText`

          Text supplied by the user.

          - `text: string`

            The text supplied by the user.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `MessageContentResourceInputImage`

          An image supplied by the user.

          - `image_url: string`

            The URL of the image supplied by the user, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

        - `MessageContentResourceOutputText`

          Text produced by the assistant.

          - `text: string`

            The text produced by the assistant.

          - `type: "output_text"`

            The type of the object. Always `output_text`.

            - `"output_text"`

      - `phase: "commentary" | "final_answer" | null`

        The phase of an assistant message. Null for user messages.

        - `"commentary"`

          Commentary produced while the agent works.

        - `"final_answer"`

          The agent's final answer.

      - `role: "user" | "assistant"`

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

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "message"`

        The item type. Always `message`.

        - `"message"`

    - `AgentReasoningItem`

      A reasoning item produced by the agent.

      - `id: string`

        The ID of the reasoning item.

      - `status: AgentOutputItemStatus | null`

        The status of the reasoning item.

      - `summary: Array<SummaryText>`

        The reasoning summaries produced by the agent.

        - `text: string`

          The reasoning summary text.

        - `type: "summary_text"`

          The content type. Always `summary_text`.

          - `"summary_text"`

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "reasoning"`

        The item type. Always `reasoning`.

        - `"reasoning"`

    - `AgentFunctionCallItem`

      A function call produced by the agent.

      - `id: string`

        The ID of the function call item.

      - `arguments: unknown`

        The arguments to pass to the function.

      - `call_id: string`

        The ID used to submit the function result.

      - `name: string`

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

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "function_call"`

        The item type. Always `function_call`.

        - `"function_call"`

    - `FunctionCallOutputItemResource`

      The result supplied for a function call.

      - `id: string`

        The ID of the function call output item.

      - `call_id: string`

        The ID of the function call that produced this output.

      - `error: string | null`

        The error message, if the call failed.

      - `output: AgentFunctionCallOutput | null`

        The function result, if the call succeeded.

        - `string`

        - `Array<InputContent>`

          - `InputContentResourceInputText`

            Text input recorded in a session item.

            - `text: string`

              The text supplied to the agent.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `InputContentResourceInputImage`

            Image input recorded in a session item.

            - `image_url: string`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

      - `status: AgentFunctionCallStatus`

        The status of the function call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "function_call_output"`

        The item type. Always `function_call_output`.

        - `"function_call_output"`

    - `AgentMessageItemResource`

      A message exchanged between agent threads.

      - `id: string`

        The ID of the message.

      - `content: Array<AgentContent>`

        The content exchanged between the agents.

        - `OutputText`

          A text content part produced by the agent.

          - `text: string`

            The text produced by the agent.

          - `type: "output_text"`

            The content type. Always `output_text`.

            - `"output_text"`

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

          - `encrypted_content: string`

            The encrypted content payload.

          - `type: "encrypted_content"`

            The content type. Always `encrypted_content`.

            - `"encrypted_content"`

      - `recipient_agent_id: string`

        The ID or name of the receiving agent.

      - `sender_agent_id: string`

        The ID or name of the sending agent.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "agent_message"`

        The item type. Always `agent_message`.

        - `"agent_message"`

    - `AgentMcpCallItem`

      A call to a tool on an MCP server.

      - `id: string`

        The ID of the MCP call item.

      - `arguments: unknown`

        The arguments passed to the MCP tool.

      - `error: unknown`

        The error returned by the MCP tool, if any.

      - `name: string`

        The name of the MCP tool.

      - `output: unknown`

        The output returned by the MCP tool, if any.

      - `server_label: string`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "mcp_call"`

        The item type. Always `mcp_call`.

        - `"mcp_call"`

    - `ComputerUseCallItemResource`

      One execution of the platform-provided computer-use capability.

      - `id: string`

        The ID of the activity item.

      - `output: Output | null`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: string`

          The complete JPEG image as a base64 data URL.

        - `type: "computer_screenshot"`

          The content type. Always `computer_screenshot`.

          - `"computer_screenshot"`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: string | null`

        A model-generated description of the activity, when available.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "computer_use_call"`

        The item type. Always `computer_use_call`.

        - `"computer_use_call"`

    - `BrowserAuthenticationRequestItemResource`

      A credential-free history record of the emitted login request.

      - `id: string`

        The stable history item ID.

      - `request: Request`

        A registered form awaiting the application's response.

        - `credential_origin: string | null`

          The registered form or frame origin where values will be entered.

        - `fields: Array<Field>`

          Controls to render. All submitted values are sensitive.

          - `id: string`

            The field ID to submit as field_id in a fields entry.

          - `label: string`

            The label to display beside the control.

          - `required: boolean`

            Whether this control requires a nonempty value.

          - `type: string`

            The rendering type, such as email, password, or text.

        - `options: Array<Option>`

          Sign-in methods. Empty for a plain form.

          - `id: string`

            The option ID to submit as selected_option.

          - `field_ids: Array<string>`

            IDs from the registered fields that this method accepts.

          - `label: string`

            The method label to display.

        - `reason: string | null`

          Why the agent needs the user to sign in.

        - `type: "browser_authentication"`

          The type of the object. Always `browser_authentication`.

          - `"browser_authentication"`

      - `request_id: string`

      - `turn_id: string`

      - `type: "computer_use_approval_request"`

        The item type. Always computer_use_approval_request.

        - `"computer_use_approval_request"`

    - `ComputerUseApprovalRequestResultItemResource`

      A credential-free record of an admitted response, not proof of completion.

      - `id: string`

        The stable history item ID.

      - `request_id: string`

        The registered request answered by this item.

      - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        The admitted response, without submitted credential values.

        - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

          - `action: "submit"`

            - `"submit"`

          - `selected_option: string | null`

            The chosen sign-in method, or null when no options were offered.

          - `type: "browser_authentication"`

            - `"browser_authentication"`

        - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

          - `action: "cancel"`

            - `"cancel"`

          - `type: "browser_authentication"`

            - `"browser_authentication"`

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "computer_use_approval_request_result"`

        - `"computer_use_approval_request_result"`

    - `AgentWebSearchCallItem`

      A web search call produced by the agent.

      - `id: string`

        The ID of the web search call.

      - `action: WebSearchAction | null`

        The action performed by the web search tool.

        - `WebSearchActionResourceSearch`

          A search query or group of search queries.

          - `queries: Array<string> | null`

            The search queries, when multiple queries were used.

          - `query: string | null`

            The search query, when a single query was used.

          - `type: "search"`

            The type of the object. Always `search`.

            - `"search"`

        - `WebSearchActionResourceOpenPage`

          Opens a web page.

          - `type: "open_page"`

            The type of the object. Always `open_page`.

            - `"open_page"`

          - `url: string | null`

            The URL of the page that was opened.

        - `WebSearchActionResourceFindInPage`

          Finds text within a web page.

          - `pattern: string | null`

            The text pattern that was searched for.

          - `type: "find_in_page"`

            The type of the object. Always `find_in_page`.

            - `"find_in_page"`

          - `url: string | null`

            The URL of the page that was searched.

        - `WebSearchActionResourceOther`

          Another web search action.

          - `type: "other"`

            The type of the object. Always `other`.

            - `"other"`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "web_search_call"`

        The item type. Always `web_search_call`.

        - `"web_search_call"`

    - `AgentCommandExecutionItem`

      A command execution produced by the agent.

      - `id: string`

        The ID of the command execution item.

      - `command: string`

        The command that was executed.

      - `cwd: string | null`

        The working directory used to execute the command.

      - `duration_ms: number | null`

        The command duration in milliseconds.

      - `exit_code: number | null`

        The process exit code, if the command completed.

      - `output: string | null`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "command_execution"`

        The item type. Always `command_execution`.

        - `"command_execution"`

    - `AgentCreateSubagentCallItem`

      A request to spawn a subagent.

      - `id: string`

        The ID of the tool call item.

      - `agent_id: string`

        The ID of the agent that requested the subagent.

      - `content: Array<AgentContent>`

        The task given to the spawned agent.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `model: string | null`

        The model requested for the spawned agent.

      - `reasoning_effort: string | null`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "create_subagent_call"`

        The item type. Always `create_subagent_call`.

        - `"create_subagent_call"`

          The current public item type.

    - `AgentSendSubagentInputCallItem`

      A request to send input to another agent.

      - `id: string`

        The ID of the tool call item.

      - `content: Array<AgentContent>`

        The input sent to the receiving agent.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: string`

        The ID of the agent receiving the input.

      - `sender_agent_id: string`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "send_subagent_input_call"`

        The item type. Always `send_subagent_input_call`.

        - `"send_subagent_input_call"`

          The current public item type.

    - `AgentResumeSubagentCallItem`

      A request to resume a subagent.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to resume.

      - `sender_agent_id: string`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "resume_subagent_call"`

        The item type. Always `resume_subagent_call`.

        - `"resume_subagent_call"`

          The current public item type.

    - `AgentWaitForSubagentsCallItem`

      A request to wait for one or more subagents.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_ids: Array<string>`

        The IDs of the agents to wait for.

      - `sender_agent_id: string`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "wait_for_subagents_call"`

        The item type. Always `wait_for_subagents_call`.

        - `"wait_for_subagents_call"`

          The current public item type.

    - `AgentInterruptSubagentCallItem`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to interrupt.

      - `sender_agent_id: string`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "interrupt_subagent_call"`

        The item type. Always `interrupt_subagent_call`.

        - `"interrupt_subagent_call"`

          The current public item type.

    - `AgentCloseSubagentCallItem`

      A request to close a subagent.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to close.

      - `sender_agent_id: string`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "close_subagent_call"`

        The item type. Always `close_subagent_call`.

        - `"close_subagent_call"`

          The current public item type.

  - `output_index: number | null`

    The index of the item in the turn output, when the item is agent output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.item.added"`

    The type of the object. Always `agent.session.turn.item.added`.

    - `"agent.session.turn.item.added"`

### Agent Session Turn Item Done Event

- `AgentSessionTurnItemDoneEvent`

  Emitted when an output item is complete.

  - `event_id: string`

    The unique ID of the event.

  - `item: AgentOutputItem`

    The completed output item.

    - `AgentSessionAssistantMessage`

      An assistant message produced by the agent.

      - `id: string`

        The ID of the message.

      - `content: Array<OutputText>`

        The content of the message.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `phase: "commentary" | "final_answer" | null`

        The phase of the assistant message.

        - `"commentary"`

          Commentary produced while the agent works.

        - `"final_answer"`

          The agent's final answer.

      - `role: "assistant"`

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

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "message"`

        The item type. Always `message`.

        - `"message"`

    - `AgentReasoningItem`

      A reasoning item produced by the agent.

      - `id: string`

        The ID of the reasoning item.

      - `status: AgentOutputItemStatus | null`

        The status of the reasoning item.

      - `summary: Array<SummaryText>`

        The reasoning summaries produced by the agent.

        - `text: string`

          The reasoning summary text.

        - `type: "summary_text"`

          The content type. Always `summary_text`.

          - `"summary_text"`

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "reasoning"`

        The item type. Always `reasoning`.

        - `"reasoning"`

    - `AgentFunctionCallItem`

      A function call produced by the agent.

      - `id: string`

        The ID of the function call item.

      - `arguments: unknown`

        The arguments to pass to the function.

      - `call_id: string`

        The ID used to submit the function result.

      - `name: string`

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

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "function_call"`

        The item type. Always `function_call`.

        - `"function_call"`

    - `AgentMcpCallItem`

      A call to a tool on an MCP server.

      - `id: string`

        The ID of the MCP call item.

      - `arguments: unknown`

        The arguments passed to the MCP tool.

      - `error: unknown`

        The error returned by the MCP tool, if any.

      - `name: string`

        The name of the MCP tool.

      - `output: unknown`

        The output returned by the MCP tool, if any.

      - `server_label: string`

        The label of the MCP server.

      - `status: AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "mcp_call"`

        The item type. Always `mcp_call`.

        - `"mcp_call"`

    - `ComputerUseCallItemResource`

      One execution of the platform-provided computer-use capability.

      - `id: string`

        The ID of the activity item.

      - `output: Output | null`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `image_url: string`

          The complete JPEG image as a base64 data URL.

        - `type: "computer_screenshot"`

          The content type. Always `computer_screenshot`.

          - `"computer_screenshot"`

      - `status: AgentFunctionCallStatus`

        The execution status of the activity.

      - `title: string | null`

        A model-generated description of the activity, when available.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "computer_use_call"`

        The item type. Always `computer_use_call`.

        - `"computer_use_call"`

    - `BrowserAuthenticationRequestItemResource`

      A credential-free history record of the emitted login request.

      - `id: string`

        The stable history item ID.

      - `request: Request`

        A registered form awaiting the application's response.

        - `credential_origin: string | null`

          The registered form or frame origin where values will be entered.

        - `fields: Array<Field>`

          Controls to render. All submitted values are sensitive.

          - `id: string`

            The field ID to submit as field_id in a fields entry.

          - `label: string`

            The label to display beside the control.

          - `required: boolean`

            Whether this control requires a nonempty value.

          - `type: string`

            The rendering type, such as email, password, or text.

        - `options: Array<Option>`

          Sign-in methods. Empty for a plain form.

          - `id: string`

            The option ID to submit as selected_option.

          - `field_ids: Array<string>`

            IDs from the registered fields that this method accepts.

          - `label: string`

            The method label to display.

        - `reason: string | null`

          Why the agent needs the user to sign in.

        - `type: "browser_authentication"`

          The type of the object. Always `browser_authentication`.

          - `"browser_authentication"`

      - `request_id: string`

      - `turn_id: string`

      - `type: "computer_use_approval_request"`

        The item type. Always computer_use_approval_request.

        - `"computer_use_approval_request"`

    - `AgentWebSearchCallItem`

      A web search call produced by the agent.

      - `id: string`

        The ID of the web search call.

      - `action: WebSearchAction | null`

        The action performed by the web search tool.

        - `WebSearchActionResourceSearch`

          A search query or group of search queries.

          - `queries: Array<string> | null`

            The search queries, when multiple queries were used.

          - `query: string | null`

            The search query, when a single query was used.

          - `type: "search"`

            The type of the object. Always `search`.

            - `"search"`

        - `WebSearchActionResourceOpenPage`

          Opens a web page.

          - `type: "open_page"`

            The type of the object. Always `open_page`.

            - `"open_page"`

          - `url: string | null`

            The URL of the page that was opened.

        - `WebSearchActionResourceFindInPage`

          Finds text within a web page.

          - `pattern: string | null`

            The text pattern that was searched for.

          - `type: "find_in_page"`

            The type of the object. Always `find_in_page`.

            - `"find_in_page"`

          - `url: string | null`

            The URL of the page that was searched.

        - `WebSearchActionResourceOther`

          Another web search action.

          - `type: "other"`

            The type of the object. Always `other`.

            - `"other"`

      - `status: AgentOutputItemStatus`

        The status of the web search call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "web_search_call"`

        The item type. Always `web_search_call`.

        - `"web_search_call"`

    - `AgentCommandExecutionItem`

      A command execution produced by the agent.

      - `id: string`

        The ID of the command execution item.

      - `command: string`

        The command that was executed.

      - `cwd: string | null`

        The working directory used to execute the command.

      - `duration_ms: number | null`

        The command duration in milliseconds.

      - `exit_code: number | null`

        The process exit code, if the command completed.

      - `output: string | null`

        The command output, if available.

      - `status: AgentFunctionCallStatus`

        The status of the command execution.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "command_execution"`

        The item type. Always `command_execution`.

        - `"command_execution"`

    - `AgentCreateSubagentCallItem`

      A request to spawn a subagent.

      - `id: string`

        The ID of the tool call item.

      - `agent_id: string`

        The ID of the agent that requested the subagent.

      - `content: Array<AgentContent>`

        The task given to the spawned agent.

        - `OutputText`

          A text content part produced by the agent.

          - `text: string`

            The text produced by the agent.

          - `type: "output_text"`

            The content type. Always `output_text`.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

          - `encrypted_content: string`

            The encrypted content payload.

          - `type: "encrypted_content"`

            The content type. Always `encrypted_content`.

            - `"encrypted_content"`

      - `model: string | null`

        The model requested for the spawned agent.

      - `reasoning_effort: string | null`

        The reasoning effort requested for the spawned agent.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "create_subagent_call"`

        The item type. Always `create_subagent_call`.

        - `"create_subagent_call"`

          The current public item type.

    - `AgentSendSubagentInputCallItem`

      A request to send input to another agent.

      - `id: string`

        The ID of the tool call item.

      - `content: Array<AgentContent>`

        The input sent to the receiving agent.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `recipient_agent_id: string`

        The ID of the agent receiving the input.

      - `sender_agent_id: string`

        The ID of the agent sending the input.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "send_subagent_input_call"`

        The item type. Always `send_subagent_input_call`.

        - `"send_subagent_input_call"`

          The current public item type.

    - `AgentResumeSubagentCallItem`

      A request to resume a subagent.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to resume.

      - `sender_agent_id: string`

        The ID of the agent requesting the resume.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "resume_subagent_call"`

        The item type. Always `resume_subagent_call`.

        - `"resume_subagent_call"`

          The current public item type.

    - `AgentWaitForSubagentsCallItem`

      A request to wait for one or more subagents.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_ids: Array<string>`

        The IDs of the agents to wait for.

      - `sender_agent_id: string`

        The ID of the agent waiting for results.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "wait_for_subagents_call"`

        The item type. Always `wait_for_subagents_call`.

        - `"wait_for_subagents_call"`

          The current public item type.

    - `AgentInterruptSubagentCallItem`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to interrupt.

      - `sender_agent_id: string`

        The ID of the agent requesting the interrupt.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "interrupt_subagent_call"`

        The item type. Always `interrupt_subagent_call`.

        - `"interrupt_subagent_call"`

          The current public item type.

    - `AgentCloseSubagentCallItem`

      A request to close a subagent.

      - `id: string`

        The ID of the tool call item.

      - `recipient_agent_id: string`

        The ID of the agent to close.

      - `sender_agent_id: string`

        The ID of the agent requesting the close.

      - `status: AgentFunctionCallStatus`

        The status of the tool call.

      - `turn_id: string`

        The ID of the turn that contains this item.

      - `type: "close_subagent_call"`

        The item type. Always `close_subagent_call`.

        - `"close_subagent_call"`

          The current public item type.

  - `output_index: number`

    The index of the output item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.item.done"`

    The type of the object. Always `agent.session.turn.item.done`.

    - `"agent.session.turn.item.done"`

### Agent Session Turn Output Text Delta Event

- `AgentSessionTurnOutputTextDeltaEvent`

  Emitted when text is appended to an output text content part.

  - `content_index: number`

    The index of the content part in the message.

  - `delta: string`

    The text that was appended.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the message item.

  - `output_index: number`

    The index of the item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.output_text.delta"`

    The type of the object. Always `agent.session.turn.output_text.delta`.

    - `"agent.session.turn.output_text.delta"`

### Agent Session Turn Output Text Done Event

- `AgentSessionTurnOutputTextDoneEvent`

  Emitted when an output text content part is complete.

  - `content_index: number`

    The index of the content part in the message.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the message item.

  - `output_index: number`

    The index of the item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `text: string`

    The complete output text.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.output_text.done"`

    The type of the object. Always `agent.session.turn.output_text.done`.

    - `"agent.session.turn.output_text.done"`

### Agent Session Turn Reasoning Summary Part Added Event

- `AgentSessionTurnReasoningSummaryPartAddedEvent`

  Emitted when a reasoning summary content part is added.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the reasoning item.

  - `output_index: number`

    The index of the item in the turn output.

  - `part: SummaryText`

    The initial summary part.

    - `text: string`

      The reasoning summary text.

    - `type: "summary_text"`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `session_id: string`

    The ID of the session associated with the event.

  - `summary_index: number`

    The index of the summary content part.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.reasoning_summary_part.added"`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

    - `"agent.session.turn.reasoning_summary_part.added"`

### Agent Session Turn Reasoning Summary Part Done Event

- `AgentSessionTurnReasoningSummaryPartDoneEvent`

  Emitted when a reasoning summary part is complete.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the reasoning item.

  - `output_index: number`

    The index of the item in the turn output.

  - `part: SummaryText`

    The completed summary part.

    - `text: string`

      The reasoning summary text.

    - `type: "summary_text"`

      The content type. Always `summary_text`.

      - `"summary_text"`

  - `session_id: string`

    The ID of the session associated with the event.

  - `status: "incomplete" | null`

    Present as `incomplete` when summary generation was interrupted.

    - `"incomplete"`

  - `summary_index: number`

    The index of the summary part.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.reasoning_summary_part.done"`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

    - `"agent.session.turn.reasoning_summary_part.done"`

### Agent Session Turn Reasoning Summary Text Delta Event

- `AgentSessionTurnReasoningSummaryTextDeltaEvent`

  Emitted when text is appended to a reasoning summary.

  - `delta: string`

    The summary text that was appended.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the reasoning item.

  - `output_index: number`

    The index of the item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `summary_index: number`

    The index of the summary content part.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.reasoning_summary_text.delta"`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

    - `"agent.session.turn.reasoning_summary_text.delta"`

### Agent Session Turn Reasoning Summary Text Done Event

- `AgentSessionTurnReasoningSummaryTextDoneEvent`

  Emitted when a reasoning summary content part is complete.

  - `event_id: string`

    The unique ID of the event.

  - `item_id: string`

    The ID of the reasoning item.

  - `output_index: number`

    The index of the item in the turn output.

  - `session_id: string`

    The ID of the session associated with the event.

  - `summary_index: number`

    The index of the summary content part.

  - `text: string`

    The complete reasoning summary text.

  - `turn_id: string | null`

    The ID of the turn associated with the event, when applicable.

  - `type: "agent.session.turn.reasoning_summary_text.done"`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

    - `"agent.session.turn.reasoning_summary_text.done"`

### Agent Text

- `AgentText`

  The text configuration used by an agent.

  - `format: TextFormat`

    The effective output format. Defaults to ordinary text.

    - `TextFormatResourceText`

      Generates ordinary text without a structured-output constraint.

      - `type: "text"`

        The type of the object. Always `text`.

        - `"text"`

    - `TextFormatResourceJSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Record<string, unknown>`

        The JSON Schema that generated text must match.

      - `type: "json_schema"`

        The type of the object. Always `json_schema`.

        - `"json_schema"`

  - `verbosity: "low" | "medium" | "high"`

    The amount of text produced by the agent. Defaults to `medium`.

    - `"low"`

    - `"medium"`

    - `"high"`

### Agent Text Param

- `AgentTextParam`

  Configuration for text generated by the agent.

  - `format?: TextFormatParam | null`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `TextFormatParamText`

      Generates ordinary text without a structured-output constraint.

      - `type: "text"`

        The type of the object. Always `text`.

        - `"text"`

    - `TextFormatParamJSONSchema`

      Constrains generated text to a JSON Schema.

      - `schema: Record<string, unknown>`

        The JSON Schema that generated text must match.

      - `type: "json_schema"`

        The type of the object. Always `json_schema`.

        - `"json_schema"`

  - `verbosity?: "low" | "medium" | "high" | null`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `"low"`

      Produces less text.

    - `"medium"`

      Uses the default amount of text.

    - `"high"`

      Produces more text.

### Agent Tool

- `AgentTool = AgentToolResourceFunction | AgentToolResourceProgrammaticToolCalling | AgentToolResourceMcp | 2 more`

  A tool available to the agent.

  - `AgentToolResourceFunction`

    A function defined by the application.

    - `defer_loading: boolean`

      Whether the function is deferred and discovered through tool search.

    - `description: string`

      A description of what the function does.

    - `name: string`

      The name of the function.

    - `parameters: Record<string, unknown>`

      A JSON Schema object describing the function's arguments.

    - `type: "function"`

      The type of the object. Always `function`.

      - `"function"`

  - `AgentToolResourceProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `enabled: boolean`

      Whether tools can be called from model-generated code.

    - `type: "programmatic_tool_calling"`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

  - `AgentToolResourceMcp`

    Tools provided by a remote MCP server.

    - `allowed_tools: Array<string> | null`

      The MCP tools the agent may call.

    - `connection_origin: "service" | "environment"`

      Where outbound MCP HTTP connections originate.

      - `"service"`

      - `"environment"`

    - `credential_id: string | null`

      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

    - `request_metadata: Record<string, unknown>`

      Metadata included with requests to this MCP server.

    - `required: boolean`

      Whether this MCP server must initialize before the first turn.

    - `server_label: string`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransport`

      The transport used to connect to the MCP server.

      - `McpTransportResourceHTTP`

        Connects to an MCP server over HTTP.

        - `server_url: string`

          The URL of the MCP server.

        - `type: "http"`

          The type of the object. Always `http`.

          - `"http"`

      - `McpTransportResourceStdio`

        Starts an MCP server as a local process.

        - `args: Array<string>`

          Arguments passed to the MCP server command.

        - `command: string`

          The command used to start the MCP server.

        - `cwd: string`

          The working directory used to start the MCP server.

        - `env_vars: Array<string>`

          Environment variable names inherited from the execution environment.

        - `type: "stdio"`

          The type of the object. Always `stdio`.

          - `"stdio"`

    - `type: "mcp"`

      The type of the object. Always `mcp`.

      - `"mcp"`

  - `AgentToolResourceWebSearch`

    Web search.

    - `allowed_domains: Array<string> | null`

      Allowed search domains, or `null` when the search is unrestricted.

    - `context_size: "low" | "medium" | "high"`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location: Location | null`

      Approximate location used to localize search results, if provided.

      - `city: string | null`

        The city name.

      - `country: string | null`

        The two-letter ISO country code, such as `US`.

      - `region: string | null`

        The region or state name.

      - `timezone: string | null`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: "disabled" | "cached" | "live"`

      The source used for web search results.

      - `"disabled"`

      - `"cached"`

      - `"live"`

    - `type: "web_search"`

      The type of the object. Always `web_search`.

      - `"web_search"`

  - `AgentToolResourceComputerUse`

    Browser use in an OpenAI-hosted session.

    - `include_screenshots: boolean`

      Whether computer tool outputs include screenshots.

    - `type: "computer_use"`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

### Agent Tool Param

- `AgentToolParam = AgentToolConfigParamFunction | AgentToolConfigParamToolSearch | AgentToolConfigParamProgrammaticToolCalling | 3 more`

  A tool available to the agent.

  - `AgentToolConfigParamFunction`

    A function defined by the application.

    - `description: string`

      A description of what the function does.

    - `name: string`

      The name of the function.

    - `parameters: Record<string, unknown>`

      A JSON Schema object describing the function's arguments.

    - `type: "function"`

      The type of the object. Always `function`.

      - `"function"`

    - `defer_loading?: boolean`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `AgentToolConfigParamToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: "tool_search"`

      The type of the object. Always `tool_search`.

      - `"tool_search"`

  - `AgentToolConfigParamProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: "programmatic_tool_calling"`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

    - `enabled?: boolean`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `AgentToolConfigParamMcp`

    Tools provided by a remote MCP server.

    - `server_label: string`

      A label used to identify the MCP server in tool calls.

    - `transport: McpTransportParam`

      The transport used to connect to the MCP server.

      - `McpTransportConfigParamHTTP`

        Connects to an MCP server over HTTP.

        - `server_url: string`

          The URL of the MCP server.

        - `type: "http"`

          The type of the object. Always `http`.

          - `"http"`

        - `authorization?: string | null`

          The authorization value sent to the MCP server, if any.

        - `headers?: Record<string, string> | null`

          Additional HTTP headers sent to the MCP server.

      - `McpTransportConfigParamStdio`

        Starts an MCP server as a local process.

        - `command: string`

          The command used to start the MCP server.

        - `cwd: string`

          The working directory used to start the MCP server.

        - `type: "stdio"`

          The type of the object. Always `stdio`.

          - `"stdio"`

        - `args?: Array<string> | null`

          Arguments passed to the MCP server command.

        - `env?: Record<string, string> | null`

          Environment variables set for the MCP server process.

        - `env_vars?: Array<string> | null`

          Environment variable names to inherit from the selected execution environment.

    - `type: "mcp"`

      The type of the object. Always `mcp`.

      - `"mcp"`

    - `allowed_tools?: Array<string> | null`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin?: "service" | "environment" | null`

      Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

      - `"service"`

        Uses the Managed Agents service network.

      - `"environment"`

        Uses the session's execution environment.

    - `credential_id?: string | null`

      The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata?: Record<string, unknown> | null`

      Metadata included with requests to this MCP server.

    - `required?: boolean`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `AgentToolConfigParamWebSearch`

    Web search.

    - `type: "web_search"`

      The type of the object. Always `web_search`.

      - `"web_search"`

    - `allowed_domains?: Array<string> | null`

      Domains the search may include.

    - `context_size?: "low" | "medium" | "high" | null`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location?: Location | null`

      Approximate location used to localize search results.

      - `city?: string | null`

        The city name.

      - `country?: string | null`

        The two-letter ISO country code, such as `US`.

      - `region?: string | null`

        The region or state name.

      - `timezone?: string | null`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode?: "disabled" | "cached" | "live" | null`

      The source used for web search results. Defaults to `live`.

      - `"disabled"`

        Disables web search.

      - `"cached"`

        Uses cached search results.

      - `"live"`

        Searches the live web.

  - `AgentToolConfigParamComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: "computer_use"`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

    - `include_screenshots?: boolean`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Agent Wait For Subagents Call Item

- `AgentWaitForSubagentsCallItem`

  A request to wait for one or more subagents.

  - `id: string`

    The ID of the tool call item.

  - `recipient_agent_ids: Array<string>`

    The IDs of the agents to wait for.

  - `sender_agent_id: string`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "wait_for_subagents_call"`

    The item type. Always `wait_for_subagents_call`.

    - `"wait_for_subagents_call"`

      The current public item type.

### Agent Web Search Call Item

- `AgentWebSearchCallItem`

  A web search call produced by the agent.

  - `id: string`

    The ID of the web search call.

  - `action: WebSearchAction | null`

    The action performed by the web search tool.

    - `WebSearchActionResourceSearch`

      A search query or group of search queries.

      - `queries: Array<string> | null`

        The search queries, when multiple queries were used.

      - `query: string | null`

        The search query, when a single query was used.

      - `type: "search"`

        The type of the object. Always `search`.

        - `"search"`

    - `WebSearchActionResourceOpenPage`

      Opens a web page.

      - `type: "open_page"`

        The type of the object. Always `open_page`.

        - `"open_page"`

      - `url: string | null`

        The URL of the page that was opened.

    - `WebSearchActionResourceFindInPage`

      Finds text within a web page.

      - `pattern: string | null`

        The text pattern that was searched for.

      - `type: "find_in_page"`

        The type of the object. Always `find_in_page`.

        - `"find_in_page"`

      - `url: string | null`

        The URL of the page that was searched.

    - `WebSearchActionResourceOther`

      Another web search action.

      - `type: "other"`

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

  - `turn_id: string`

    The ID of the turn that contains this item.

  - `type: "web_search_call"`

    The item type. Always `web_search_call`.

    - `"web_search_call"`

### Environment

- `Environment = EnvironmentResourceNone | EnvironmentResourceOpenAIHosted | EnvironmentResourceSelfHosted`

  The execution environment for a session.

  - `EnvironmentResourceNone`

    The session talks to CCA without selecting or provisioning an execution environment.

    - `type: "none"`

      The type of the object. Always `none`.

      - `"none"`

  - `EnvironmentResourceOpenAIHosted`

    An environment hosted by OpenAI.

    - `id: string`

      The public ID of the environment.

    - `capability_directories: Array<string>`

      Directories that contain capabilities exposed to the agent.

    - `desktop: Desktop`

      The effective desktop configuration.

      - `enabled: boolean`

        Whether the environment provisions a desktop and browser proxy.

    - `files: Array<HostedEnvironmentFile>`

      Files available in the environment, excluding their contents.

      - `HostedEnvironmentFileID`

        A file copied from the OpenAI Files API.

        - `id: string`

          The session-scoped ID of the file in the execution environment.

        - `file_id: string`

          The ID of the uploaded file.

        - `path: string`

          The file's absolute path inside the environment.

        - `size_bytes: number`

          The decoded file size in bytes.

        - `type: "file_id"`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `HostedEnvironmentFileResourceInline`

        A file supplied inline when the session was created.

        - `id: string`

          The session-scoped ID of the file in the execution environment.

        - `path: string`

          The file's absolute path inside the environment.

        - `size_bytes: number`

          The decoded file size in bytes.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network: Network`

      The effective network access policy for the environment.

      - `access: "enabled" | "disabled" | "restricted"`

        The environment's network access mode.

        - `"enabled"`

          Allows unrestricted network access.

        - `"disabled"`

          Disables network access.

        - `"restricted"`

          Applies the configured domain restrictions.

      - `allowed_domains: Array<string>`

        Domains the environment may access when network access is restricted.

    - `packages: Packages`

      Packages installed in the environment.

      - `npm: Array<string>`

        npm packages installed globally in the environment.

      - `python: Array<string>`

        Python packages installed in the environment.

      - `system: Array<string>`

        System packages installed in the environment.

    - `plugins: Array<HostedPlugin>`

      Plugins installed in the environment, excluding their archive contents.

      - `description: string`

        The installed plugin description.

      - `name: string`

        The installed plugin name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

    - `skills: Array<HostedSkill>`

      Skills installed in the environment, excluding their archive contents.

      - `HostedSkillReference`

        A skill installed from the Skills API.

        - `description: string`

          The installed skill description.

        - `name: string`

          The installed skill name.

        - `skill_id: string`

          The referenced skill ID.

        - `type: "skill_reference"`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version: string`

          The concrete skill version installed for this session.

      - `HostedSkillResourceInline`

        A skill installed from an inline ZIP archive.

        - `description: string`

          The installed skill description.

        - `name: string`

          The installed skill name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

    - `type: "openai_hosted"`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `container_size?: "small" | "medium" | "large" | null`

      The effective CPU and memory tier, or null when unknown or outside the public tiers.

      - `"small"`

      - `"medium"`

      - `"large"`

  - `EnvironmentResourceSelfHosted`

    An environment hosted by the application.

    - `id: string`

      The public ID of the environment.

    - `capability_directories: Array<string>`

      Directories that contain capabilities exposed to the agent.

    - `remote_url: string`

      Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

    - `type: "self_hosted"`

      The type of the object. Always `self_hosted`.

      - `"self_hosted"`

    - `workspace_directory: string`

      The absolute project directory inside the environment. Defaults to `/workspace`.

### Environment Param

- `EnvironmentParam = EnvironmentParamNone | EnvironmentParamOpenAIHosted | EnvironmentParamSelfHosted`

  The execution environment and optional reusable template for a session.

  - `EnvironmentParamNone`

    Runs the agent without an execution environment.

    - `type: "none"`

      The type of the object. Always `none`.

      - `"none"`

  - `EnvironmentParamOpenAIHosted`

    An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

    - `type: "openai_hosted"`

      The type of the object. Always `openai_hosted`.

      - `"openai_hosted"`

    - `capability_directories?: Array<string> | null`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `container_size?: "small" | "medium" | "large"`

      The hosted container size. Omission selects the medium tier.

      - `"small"`

      - `"medium"`

      - `"large"`

    - `desktop?: Desktop | null`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `enabled: boolean`

        Whether to provision the desktop and its browser proxy.

    - `env?: Record<string, string> | null`

      Environment variables made available to the agent.

    - `environment_template_id?: string`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `files?: Array<HostedEnvironmentFileParam> | null`

      Files available before the agent starts. Defaults to an empty list.

      - `HostedEnvironmentFileParamFileID`

        A file previously uploaded through the OpenAI Files API.

        - `file_id: string`

          The ID of the uploaded file.

        - `path: string`

          The absolute destination path inside `/workspace`.

        - `type: "file_id"`

          The type of the object. Always `file_id`.

          - `"file_id"`

      - `HostedEnvironmentFileParamInline`

        A file supplied directly as standard-base64 data.

        - `data: string`

          The standard-base64-encoded file contents.

        - `path: string`

          The absolute destination path inside `/workspace`.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

    - `network?: Network | null`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `access: "enabled" | "disabled" | "restricted"`

        The environment's network access mode.

        - `"enabled"`

          Allows unrestricted network access.

        - `"disabled"`

          Disables network access.

        - `"restricted"`

          Applies the configured domain restrictions.

      - `allowed_domains?: Array<string> | null`

        Domains the environment may access when network access is restricted.

      - `blocked_domains?: Array<string> | null`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `packages?: Packages | null`

      Packages to install in the environment. Defaults to empty package lists.

      - `npm?: Array<string> | null`

        npm packages to install globally. Defaults to an empty list.

      - `python?: Array<string> | null`

        Python packages to install. Defaults to an empty list.

      - `system?: Array<string> | null`

        System packages to install. Defaults to an empty list.

    - `plugins?: Array<HostedPluginParam> | null`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `description: string`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `name: string`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

        - `data: string`

          Standard-base64 encoded ZIP archive bytes.

        - `media_type: "application/zip"`

          The archive media type, always `application/zip`.

          - `"application/zip"`

            A ZIP archive.

        - `type: "base64"`

          The type of the object. Always `base64`.

          - `"base64"`

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

    - `setup_commands?: Array<SetupCommandParam> | null`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `command: string`

        The shell command to execute.

      - `cwd?: string | null`

        The absolute working directory. Defaults to `/workspace`.

    - `skills?: Array<HostedSkillParam> | null`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `HostedSkillParamSkillReference`

        References a skill uploaded through the Skills API.

        - `skill_id: string`

          The ID of the skill created through `/v1/skills`.

        - `type: "skill_reference"`

          The type of the object. Always `skill_reference`.

          - `"skill_reference"`

        - `version?: string | null`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `HostedSkillParamInline`

        Supplies a skill ZIP directly in the session request.

        - `description: string`

          The skill description declared in `SKILL.md`.

        - `name: string`

          The skill name declared in `SKILL.md`.

        - `source: InlineCapabilitySourceParam`

          Provides ZIP bytes encoded with standard base64.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

  - `EnvironmentParamSelfHosted`

    An application-hosted environment configured inline.

    - `type: "self_hosted"`

      The type of the object. Always `self_hosted`.

      - `"self_hosted"`

    - `workspace_directory: string`

      Absolute project directory inside the self-hosted environment.

    - `capability_directories?: Array<string> | null`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

### Hosted Environment File

- `HostedEnvironmentFile = HostedEnvironmentFileID | HostedEnvironmentFileResourceInline`

  Metadata for a file materialized in an OpenAI-hosted execution environment.

  - `HostedEnvironmentFileID`

    A file copied from the OpenAI Files API.

    - `id: string`

      The session-scoped ID of the file in the execution environment.

    - `file_id: string`

      The ID of the uploaded file.

    - `path: string`

      The file's absolute path inside the environment.

    - `size_bytes: number`

      The decoded file size in bytes.

    - `type: "file_id"`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `HostedEnvironmentFileResourceInline`

    A file supplied inline when the session was created.

    - `id: string`

      The session-scoped ID of the file in the execution environment.

    - `path: string`

      The file's absolute path inside the environment.

    - `size_bytes: number`

      The decoded file size in bytes.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Environment File ID

- `HostedEnvironmentFileID`

  A file copied from the OpenAI Files API.

  - `id: string`

    The session-scoped ID of the file in the execution environment.

  - `file_id: string`

    The ID of the uploaded file.

  - `path: string`

    The file's absolute path inside the environment.

  - `size_bytes: number`

    The decoded file size in bytes.

  - `type: "file_id"`

    The type of the object. Always `file_id`.

    - `"file_id"`

### Hosted Environment File Param

- `HostedEnvironmentFileParam = HostedEnvironmentFileParamFileID | HostedEnvironmentFileParamInline`

  A file materialized in an OpenAI-hosted execution environment.

  - `HostedEnvironmentFileParamFileID`

    A file previously uploaded through the OpenAI Files API.

    - `file_id: string`

      The ID of the uploaded file.

    - `path: string`

      The absolute destination path inside `/workspace`.

    - `type: "file_id"`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `HostedEnvironmentFileParamInline`

    A file supplied directly as standard-base64 data.

    - `data: string`

      The standard-base64-encoded file contents.

    - `path: string`

      The absolute destination path inside `/workspace`.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Plugin

- `HostedPlugin`

  A plugin installed from an inline ZIP archive.

  - `description: string`

    The installed plugin description.

  - `name: string`

    The installed plugin name.

  - `type: "inline"`

    The type of the object. Always `inline`.

    - `"inline"`

### Hosted Plugin Param

- `HostedPluginParam`

  Supplies a plugin ZIP directly in the session request.

  - `description: string`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `name: string`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `source: InlineCapabilitySourceParam`

    Provides ZIP bytes encoded with standard base64.

    - `data: string`

      Standard-base64 encoded ZIP archive bytes.

    - `media_type: "application/zip"`

      The archive media type, always `application/zip`.

      - `"application/zip"`

        A ZIP archive.

    - `type: "base64"`

      The type of the object. Always `base64`.

      - `"base64"`

  - `type: "inline"`

    The type of the object. Always `inline`.

    - `"inline"`

### Hosted Skill

- `HostedSkill = HostedSkillReference | HostedSkillResourceInline`

  A skill installed in an OpenAI-hosted environment.

  - `HostedSkillReference`

    A skill installed from the Skills API.

    - `description: string`

      The installed skill description.

    - `name: string`

      The installed skill name.

    - `skill_id: string`

      The referenced skill ID.

    - `type: "skill_reference"`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version: string`

      The concrete skill version installed for this session.

  - `HostedSkillResourceInline`

    A skill installed from an inline ZIP archive.

    - `description: string`

      The installed skill description.

    - `name: string`

      The installed skill name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Skill Param

- `HostedSkillParam = HostedSkillParamSkillReference | HostedSkillParamInline`

  A skill installed in an OpenAI-hosted environment.

  - `HostedSkillParamSkillReference`

    References a skill uploaded through the Skills API.

    - `skill_id: string`

      The ID of the skill created through `/v1/skills`.

    - `type: "skill_reference"`

      The type of the object. Always `skill_reference`.

      - `"skill_reference"`

    - `version?: string | null`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `HostedSkillParamInline`

    Supplies a skill ZIP directly in the session request.

    - `description: string`

      The skill description declared in `SKILL.md`.

    - `name: string`

      The skill name declared in `SKILL.md`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: string`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: "application/zip"`

        The archive media type, always `application/zip`.

        - `"application/zip"`

          A ZIP archive.

      - `type: "base64"`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

### Hosted Skill Reference

- `HostedSkillReference`

  A skill installed from the Skills API.

  - `description: string`

    The installed skill description.

  - `name: string`

    The installed skill name.

  - `skill_id: string`

    The referenced skill ID.

  - `type: "skill_reference"`

    The type of the object. Always `skill_reference`.

    - `"skill_reference"`

  - `version: string`

    The concrete skill version installed for this session.

### Inline Capability Source Param

- `InlineCapabilitySourceParam`

  Provides ZIP bytes encoded with standard base64.

  - `data: string`

    Standard-base64 encoded ZIP archive bytes.

  - `media_type: "application/zip"`

    The archive media type, always `application/zip`.

    - `"application/zip"`

      A ZIP archive.

  - `type: "base64"`

    The type of the object. Always `base64`.

    - `"base64"`

### Input Content

- `InputContent = InputContentResourceInputText | InputContentResourceInputImage`

  User-provided content recorded in a session item.

  - `InputContentResourceInputText`

    Text input recorded in a session item.

    - `text: string`

      The text supplied to the agent.

    - `type: "input_text"`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `InputContentResourceInputImage`

    Image input recorded in a session item.

    - `image_url: string`

      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

    - `type: "input_image"`

      The type of the object. Always `input_image`.

      - `"input_image"`

### Input Content Param

- `InputContentParam = InputContentParamInputText | InputContentParamInputImage`

  Content included in an input message.

  - `InputContentParamInputText`

    Text input to the model.

    - `text: string`

      The text sent to the model.

    - `type: "input_text"`

      The type of the object. Always `input_text`.

      - `"input_text"`

  - `InputContentParamInputImage`

    Image input to the model.

    - `image_url: string`

      The URL of the image sent to the model.

    - `type: "input_image"`

      The type of the object. Always `input_image`.

      - `"input_image"`

### Mcp Transport

- `McpTransport = McpTransportResourceHTTP | McpTransportResourceStdio`

  The transport used to connect to an MCP server.

  - `McpTransportResourceHTTP`

    Connects to an MCP server over HTTP.

    - `server_url: string`

      The URL of the MCP server.

    - `type: "http"`

      The type of the object. Always `http`.

      - `"http"`

  - `McpTransportResourceStdio`

    Starts an MCP server as a local process.

    - `args: Array<string>`

      Arguments passed to the MCP server command.

    - `command: string`

      The command used to start the MCP server.

    - `cwd: string`

      The working directory used to start the MCP server.

    - `env_vars: Array<string>`

      Environment variable names inherited from the execution environment.

    - `type: "stdio"`

      The type of the object. Always `stdio`.

      - `"stdio"`

### Mcp Transport Param

- `McpTransportParam = McpTransportConfigParamHTTP | McpTransportConfigParamStdio`

  The transport used to connect to an MCP server.

  - `McpTransportConfigParamHTTP`

    Connects to an MCP server over HTTP.

    - `server_url: string`

      The URL of the MCP server.

    - `type: "http"`

      The type of the object. Always `http`.

      - `"http"`

    - `authorization?: string | null`

      The authorization value sent to the MCP server, if any.

    - `headers?: Record<string, string> | null`

      Additional HTTP headers sent to the MCP server.

  - `McpTransportConfigParamStdio`

    Starts an MCP server as a local process.

    - `command: string`

      The command used to start the MCP server.

    - `cwd: string`

      The working directory used to start the MCP server.

    - `type: "stdio"`

      The type of the object. Always `stdio`.

      - `"stdio"`

    - `args?: Array<string> | null`

      Arguments passed to the MCP server command.

    - `env?: Record<string, string> | null`

      Environment variables set for the MCP server process.

    - `env_vars?: Array<string> | null`

      Environment variable names to inherit from the selected execution environment.

### Multi Agent Config

- `MultiAgentConfig`

  The resolved configuration for creating and coordinating subagents.

  - `enabled: boolean`

    Whether subagent tools are enabled. Defaults to false.

  - `max_concurrent_subagents: number | null`

    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

### Multi Agent Config Param

- `MultiAgentConfigParam`

  Explicit configuration for creating and coordinating subagents.

  - `enabled: boolean`

    Whether subagent tools are enabled.

  - `max_concurrent_subagents?: number`

    Maximum number of subagents that may run concurrently. Defaults to 6.

### Output Text

- `OutputText`

  A text content part produced by the agent.

  - `text: string`

    The text produced by the agent.

  - `type: "output_text"`

    The content type. Always `output_text`.

    - `"output_text"`

### Persisted Agent Tool

- `PersistedAgentTool = PersistedAgentToolResourceFunction | PersistedAgentToolResourceToolSearch | PersistedAgentToolResourceProgrammaticToolCalling | 3 more`

  A credential-free tool available to a reusable agent.

  - `PersistedAgentToolResourceFunction`

    A function defined by the application.

    - `defer_loading: boolean`

      Whether the function is deferred and discovered through tool search.

    - `description: string`

      A description of what the function does.

    - `name: string`

      The name of the function.

    - `parameters: Record<string, unknown>`

      A JSON Schema object describing the function's arguments.

    - `type: "function"`

      The type of the object. Always `function`.

      - `"function"`

  - `PersistedAgentToolResourceToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: "tool_search"`

      The type of the object. Always `tool_search`.

      - `"tool_search"`

  - `PersistedAgentToolResourceProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `enabled: boolean`

      Whether tools can be called from model-generated code.

    - `type: "programmatic_tool_calling"`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

  - `PersistedAgentToolResourceMcp`

    Tools provided by a remote MCP server without stored credentials.

    - `allowed_tools: Array<string> | null`

      The MCP tools the agent may call, or null when all server tools are allowed.

    - `connection_origin: "service" | "environment"`

      Where outbound MCP HTTP connections originate.

      - `"service"`

      - `"environment"`

    - `credential_id: string | null`

      The vault credential selected for this MCP server, if any.

    - `request_metadata: Record<string, unknown>`

      Metadata included with requests to this MCP server.

    - `required: boolean`

      Whether this MCP server must initialize before the first turn.

    - `server_label: string`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransport`

      The credential-free transport used to connect to the MCP server.

      - `PersistedMcpTransportResourceHTTP`

        Connects to an MCP server over HTTP.

        - `headers: Record<string, string>`

          Non-secret HTTP headers sent to the MCP server.

        - `server_url: string`

          The URL of the MCP server.

        - `type: "http"`

          The type of the object. Always `http`.

          - `"http"`

      - `PersistedMcpTransportResourceStdio`

        Starts an MCP server as a local process.

        - `args: Array<string>`

          Arguments passed to the MCP server command.

        - `command: string`

          The command used to start the MCP server.

        - `cwd: string`

          The working directory used to start the MCP server.

        - `env_vars: Array<string>`

          Environment variable names inherited from the execution environment.

        - `type: "stdio"`

          The type of the object. Always `stdio`.

          - `"stdio"`

    - `type: "mcp"`

      The type of the object. Always `mcp`.

      - `"mcp"`

  - `PersistedAgentToolResourceWebSearch`

    Web search.

    - `allowed_domains: Array<string> | null`

      Allowed search domains, or `null` when the search is unrestricted.

    - `context_size: "low" | "medium" | "high"`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location: Location | null`

      Approximate location used to localize search results, if provided.

      - `city: string | null`

        The city name.

      - `country: string | null`

        The two-letter ISO country code, such as `US`.

      - `region: string | null`

        The region or state name.

      - `timezone: string | null`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode: "disabled" | "cached" | "live"`

      The source used for web search results.

      - `"disabled"`

      - `"cached"`

      - `"live"`

    - `type: "web_search"`

      The type of the object. Always `web_search`.

      - `"web_search"`

  - `PersistedAgentToolResourceComputerUse`

    Browser use in an OpenAI-hosted session.

    - `include_screenshots: boolean`

      Whether computer tool outputs include screenshots.

    - `type: "computer_use"`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

### Persisted Agent Tool Param

- `PersistedAgentToolParam = PersistedAgentToolConfigParamFunction | PersistedAgentToolConfigParamToolSearch | PersistedAgentToolConfigParamProgrammaticToolCalling | 3 more`

  A tool that can be stored on a reusable agent without session credentials.

  - `PersistedAgentToolConfigParamFunction`

    A function defined by the application.

    - `description: string`

      A description of what the function does.

    - `name: string`

      The name of the function.

    - `parameters: Record<string, unknown>`

      A JSON Schema object describing the function's arguments.

    - `type: "function"`

      The type of the object. Always `function`.

      - `"function"`

    - `defer_loading?: boolean`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `PersistedAgentToolConfigParamToolSearch`

    Discovers deferred function tools and loads them into the model context.

    - `type: "tool_search"`

      The type of the object. Always `tool_search`.

      - `"tool_search"`

  - `PersistedAgentToolConfigParamProgrammaticToolCalling`

    Enables calling tools from model-generated code.

    - `type: "programmatic_tool_calling"`

      The type of the object. Always `programmatic_tool_calling`.

      - `"programmatic_tool_calling"`

    - `enabled?: boolean`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `PersistedAgentToolConfigParamMcp`

    Tools provided by a remote MCP server without stored credentials.

    - `server_label: string`

      A label used to identify the MCP server in tool calls.

    - `transport: PersistedMcpTransportParam`

      The credential-free transport used to connect to the MCP server.

      - `PersistedMcpTransportConfigParamHTTP`

        Connects to an MCP server over HTTP.

        - `server_url: string`

          The URL of the MCP server.

        - `type: "http"`

          The type of the object. Always `http`.

          - `"http"`

        - `headers?: Record<string, string> | null`

          Non-secret HTTP headers sent to the MCP server.

      - `PersistedMcpTransportConfigParamStdio`

        Starts an MCP server as a local process.

        - `command: string`

          The command used to start the MCP server.

        - `cwd: string`

          The working directory used to start the MCP server.

        - `type: "stdio"`

          The type of the object. Always `stdio`.

          - `"stdio"`

        - `args?: Array<string> | null`

          Arguments passed to the MCP server command.

        - `env_vars?: Array<string> | null`

          Environment variable names to inherit from the selected execution environment.

    - `type: "mcp"`

      The type of the object. Always `mcp`.

      - `"mcp"`

    - `allowed_tools?: Array<string> | null`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `connection_origin?: "service" | "environment" | null`

      Selects where outbound MCP HTTP connections originate.

      - `"service"`

        Uses the Managed Agents service network.

      - `"environment"`

        Uses the session's execution environment.

    - `credential_id?: string | null`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `request_metadata?: Record<string, unknown> | null`

      Metadata included with requests to this MCP server.

    - `required?: boolean`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `PersistedAgentToolConfigParamWebSearch`

    Web search.

    - `type: "web_search"`

      The type of the object. Always `web_search`.

      - `"web_search"`

    - `allowed_domains?: Array<string> | null`

      Domains the search may include.

    - `context_size?: "low" | "medium" | "high" | null`

      The amount of search context made available to the model. Defaults to `medium`.

      - `"low"`

      - `"medium"`

      - `"high"`

    - `location?: Location | null`

      Approximate location used to localize search results.

      - `city?: string | null`

        The city name.

      - `country?: string | null`

        The two-letter ISO country code, such as `US`.

      - `region?: string | null`

        The region or state name.

      - `timezone?: string | null`

        The IANA timezone, such as `America/Los_Angeles`.

    - `mode?: "disabled" | "cached" | "live" | null`

      The source used for web search results. Defaults to `live`.

      - `"disabled"`

        Disables web search.

      - `"cached"`

        Uses cached search results.

      - `"live"`

        Searches the live web.

  - `PersistedAgentToolConfigParamComputerUse`

    Browser use in an OpenAI-hosted session.

    - `type: "computer_use"`

      The type of the object. Always `computer_use`.

      - `"computer_use"`

    - `include_screenshots?: boolean`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Persisted Mcp Transport

- `PersistedMcpTransport = PersistedMcpTransportResourceHTTP | PersistedMcpTransportResourceStdio`

  A credential-free transport used to connect to an MCP server.

  - `PersistedMcpTransportResourceHTTP`

    Connects to an MCP server over HTTP.

    - `headers: Record<string, string>`

      Non-secret HTTP headers sent to the MCP server.

    - `server_url: string`

      The URL of the MCP server.

    - `type: "http"`

      The type of the object. Always `http`.

      - `"http"`

  - `PersistedMcpTransportResourceStdio`

    Starts an MCP server as a local process.

    - `args: Array<string>`

      Arguments passed to the MCP server command.

    - `command: string`

      The command used to start the MCP server.

    - `cwd: string`

      The working directory used to start the MCP server.

    - `env_vars: Array<string>`

      Environment variable names inherited from the execution environment.

    - `type: "stdio"`

      The type of the object. Always `stdio`.

      - `"stdio"`

### Persisted Mcp Transport Param

- `PersistedMcpTransportParam = PersistedMcpTransportConfigParamHTTP | PersistedMcpTransportConfigParamStdio`

  A credential-free transport used to connect to an MCP server.

  - `PersistedMcpTransportConfigParamHTTP`

    Connects to an MCP server over HTTP.

    - `server_url: string`

      The URL of the MCP server.

    - `type: "http"`

      The type of the object. Always `http`.

      - `"http"`

    - `headers?: Record<string, string> | null`

      Non-secret HTTP headers sent to the MCP server.

  - `PersistedMcpTransportConfigParamStdio`

    Starts an MCP server as a local process.

    - `command: string`

      The command used to start the MCP server.

    - `cwd: string`

      The working directory used to start the MCP server.

    - `type: "stdio"`

      The type of the object. Always `stdio`.

      - `"stdio"`

    - `args?: Array<string> | null`

      Arguments passed to the MCP server command.

    - `env_vars?: Array<string> | null`

      Environment variable names to inherit from the selected execution environment.

### Session Error

- `SessionError`

  An error payload with the same public fields as Responses API streaming errors.

  - `code: string | null`

    The machine-readable error code, if any.

  - `message: string`

    A customer-safe explanation of the error.

  - `param: string | null`

    The request parameter associated with the error, if any.

  - `type: string`

    The error type.

### Session Turn Error

- `SessionTurnError`

  A customer-safe error describing why a session request failed.

  - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

  - `message: string`

    A customer-safe explanation of the failure.

### Setup Command Param

- `SetupCommandParam`

  A confidential setup command executed before the hosted agent starts.

  - `command: string`

    The shell command to execute.

  - `cwd?: string | null`

    The absolute working directory. Defaults to `/workspace`.

### Subagent

- `Subagent`

  A subagent created within a session.

  - `id: string`

    The ID of the subagent.

  - `closed_at: number | null`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array<AgentContent> | null`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: string | null`

    The runner-assigned nickname, or null when unavailable.

  - `object: "agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: number`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: string`

    The ID of the agent that created this subagent.

  - `session_id: string`

    The ID of the session that owns the subagent.

  - `status: "active" | "closed"`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Summary Text

- `SummaryText`

  A reasoning summary content part.

  - `text: string`

    The reasoning summary text.

  - `type: "summary_text"`

    The content type. Always `summary_text`.

    - `"summary_text"`

### Text Format

- `TextFormat = TextFormatResourceText | TextFormatResourceJSONSchema`

  The effective output format for generated text.

  - `TextFormatResourceText`

    Generates ordinary text without a structured-output constraint.

    - `type: "text"`

      The type of the object. Always `text`.

      - `"text"`

  - `TextFormatResourceJSONSchema`

    Constrains generated text to a JSON Schema.

    - `schema: Record<string, unknown>`

      The JSON Schema that generated text must match.

    - `type: "json_schema"`

      The type of the object. Always `json_schema`.

      - `"json_schema"`

### Text Format Param

- `TextFormatParam = TextFormatParamText | TextFormatParamJSONSchema`

  The output format for generated text.

  - `TextFormatParamText`

    Generates ordinary text without a structured-output constraint.

    - `type: "text"`

      The type of the object. Always `text`.

      - `"text"`

  - `TextFormatParamJSONSchema`

    Constrains generated text to a JSON Schema.

    - `schema: Record<string, unknown>`

      The JSON Schema that generated text must match.

    - `type: "json_schema"`

      The type of the object. Always `json_schema`.

      - `"json_schema"`

### Token Usage

- `TokenUsage`

  Recorded token usage for a session or turn. Usage is best effort and may change.

  - `input_tokens: number`

    The number of input tokens used by the agent.

  - `input_tokens_details: InputTokensDetails`

    A breakdown of the agent's input token usage.

    - `cached_tokens: number`

      The number of input tokens retrieved from the prompt cache.

  - `output_tokens: number`

    The number of output tokens generated by the agent.

  - `output_tokens_details: OutputTokensDetails`

    A breakdown of the agent's output token usage.

    - `reasoning_tokens: number`

      The number of output tokens used for reasoning.

  - `total_tokens: number`

    The total number of input and output tokens used by the agent.

### Web Search Action

- `WebSearchAction = WebSearchActionResourceSearch | WebSearchActionResourceOpenPage | WebSearchActionResourceFindInPage | WebSearchActionResourceOther`

  An action performed by the web search tool.

  - `WebSearchActionResourceSearch`

    A search query or group of search queries.

    - `queries: Array<string> | null`

      The search queries, when multiple queries were used.

    - `query: string | null`

      The search query, when a single query was used.

    - `type: "search"`

      The type of the object. Always `search`.

      - `"search"`

  - `WebSearchActionResourceOpenPage`

    Opens a web page.

    - `type: "open_page"`

      The type of the object. Always `open_page`.

      - `"open_page"`

    - `url: string | null`

      The URL of the page that was opened.

  - `WebSearchActionResourceFindInPage`

    Finds text within a web page.

    - `pattern: string | null`

      The text pattern that was searched for.

    - `type: "find_in_page"`

      The type of the object. Always `find_in_page`.

      - `"find_in_page"`

    - `url: string | null`

      The URL of the page that was searched.

  - `WebSearchActionResourceOther`

    Another web search action.

    - `type: "other"`

      The type of the object. Always `other`.

      - `"other"`

# Environments

## Retrieve an agent environment

`client.beta.agents.environments.retrieve(stringenvironmentID, RequestOptionsoptions?): EnvironmentInfo`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environmentID: string`

### Returns

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "connected" | "disconnected" | 2 more`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentInfo = await client.beta.agents.environments.retrieve('environment_id');

console.log(environmentInfo.id);
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

- `EnvironmentInfo`

  Safe metadata for a first-class execution environment.

  - `id: string`

    The ID of the environment.

  - `files: Array<HostedEnvironmentFile>`

    Files installed in the environment, without their contents.

    - `HostedEnvironmentFileID`

      A file copied from the OpenAI Files API.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileResourceInline`

      A file supplied inline when the session was created.

      - `id: string`

        The session-scoped ID of the file in the execution environment.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded file size in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `object: "agent.environment"`

    The object type. Always `agent.environment`.

    - `"agent.environment"`

  - `plugins: Array<HostedPlugin>`

    Plugins installed in the environment, without their archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedSkill>`

    Skills installed in the environment, without their archive contents.

    - `HostedSkillReference`

      A skill installed from the Skills API.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string`

        The concrete skill version installed for this session.

    - `HostedSkillResourceInline`

      A skill installed from an inline ZIP archive.

      - `description: string`

        The installed skill description.

      - `name: string`

        The installed skill name.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `status: "pending" | "connected" | "disconnected" | 2 more`

    The current environment connection status.

    - `"pending"`

    - `"connected"`

    - `"disconnected"`

    - `"expired"`

    - `"failed"`

  - `type: "openai_hosted" | "self_hosted"`

    Whether the environment is hosted by OpenAI or by the application.

    - `"openai_hosted"`

    - `"self_hosted"`

# Files

## Create an agent environment file

`client.beta.agents.environments.files.create(stringenvironmentID, FileCreateParamsbody, RequestOptionsoptions?): EnvironmentFile`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID: string`

- `FileCreateParams = HostedEnvironmentFileParamFileID | HostedEnvironmentFileParamInline`

  - `FileCreateParamsBase`

    - `file_id?: string`

      The ID of the uploaded file.

    - `path_?: string`

      The absolute destination path inside `/workspace`.

    - `type?: "file_id"`

      The type of the object. Always `file_id`.

      - `"file_id"`

  - `HostedEnvironmentFileParamFileID extends FileCreateParamsBase`

  - `HostedEnvironmentFileParamInline extends FileCreateParamsBase`

### Returns

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentFile = await client.beta.agents.environments.files.create('environment_id');

console.log(environmentFile.environment_id);
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

`client.beta.agents.environments.files.list(stringenvironmentID, FileListParamsquery?, RequestOptionsoptions?): TokenPage<EnvironmentFile>`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID: string`

- `query: FileListParams`

  - `limit?: number | null`

    The maximum number of files to return, between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort by case-sensitive path components. Defaults to descending.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `page?: string`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `path_?: string | null`

    Restrict the listing to this absolute workspace directory.

### Returns

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const environmentFile of client.beta.agents.environments.files.list('environment_id')) {
  console.log(environmentFile.environment_id);
}
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

- `EnvironmentFile`

  A live file in an execution environment.

  - `environment_id: string`

    The ID of the environment containing this file.

  - `object: "agent.environment.file"`

    The object type. Always `agent.environment.file`.

    - `"agent.environment.file"`

  - `path: string`

    The absolute file path inside the environment's workspace.

  - `size_bytes: number`

    The file size in bytes.

# Templates

## Create an agent environment template

`client.beta.agents.environments.templates.create(TemplateCreateParamsbody?, RequestOptionsoptions?): EnvironmentTemplate`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `body: TemplateCreateParams`

  - `capability_directories?: Array<string> | null`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `desktop?: Desktop | null`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `enabled: boolean`

      Whether to provision the desktop and its browser proxy.

  - `env?: Record<string, string> | null`

    Environment variables made available to the agent.

  - `files?: Array<HostedEnvironmentFileParam> | null`

    Files available before the agent starts. Defaults to an empty list.

    - `HostedEnvironmentFileParamFileID`

      A file previously uploaded through the OpenAI Files API.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileParamInline`

      A file supplied directly as standard-base64 data.

      - `data: string`

        The standard-base64-encoded file contents.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name?: string | null`

    An optional human-readable display name for the template.

  - `network?: Network | null`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

    - `access: "enabled" | "disabled" | "restricted"`

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

    - `allowed_domains?: Array<string> | null`

      Domains the environment may access when network access is restricted.

    - `blocked_domains?: Array<string> | null`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `packages?: Packages | null`

    Packages to install in the environment. Defaults to empty package lists.

    - `npm?: Array<string> | null`

      npm packages to install globally. Defaults to an empty list.

    - `python?: Array<string> | null`

      Python packages to install. Defaults to an empty list.

    - `system?: Array<string> | null`

      System packages to install. Defaults to an empty list.

  - `plugins?: Array<HostedPluginParam> | null`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `description: string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `name: string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: string`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: "application/zip"`

        The archive media type, always `application/zip`.

        - `"application/zip"`

          A ZIP archive.

      - `type: "base64"`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `setup_commands?: Array<SetupCommandParam> | null`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `command: string`

      The shell command to execute.

    - `cwd?: string | null`

      The absolute working directory. Defaults to `/workspace`.

  - `skills?: Array<HostedSkillParam> | null`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `HostedSkillParamSkillReference`

      References a skill uploaded through the Skills API.

      - `skill_id: string`

        The ID of the skill created through `/v1/skills`.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version?: string | null`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInline`

      Supplies a skill ZIP directly in the session request.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

### Returns

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.create();

console.log(environmentTemplate.id);
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

`client.beta.agents.environments.templates.delete(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplateDeleted`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

### Returns

- `EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: string`

    The ID of the deleted environment template.

  - `deleted: boolean`

    Whether the environment template was deleted. Always `true`.

  - `object: "agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplateDeleted = await client.beta.agents.environments.templates.delete(
  'environment_template_id',
);

console.log(environmentTemplateDeleted.id);
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

`client.beta.agents.environments.templates.list(TemplateListParamsquery?, RequestOptionsoptions?): CursorPage<EnvironmentTemplate>`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `query: TemplateListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const environmentTemplate of client.beta.agents.environments.templates.list()) {
  console.log(environmentTemplate.id);
}
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

`client.beta.agents.environments.templates.retrieve(stringenvironmentTemplateID, RequestOptionsoptions?): EnvironmentTemplate`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

### Returns

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.retrieve(
  'environment_template_id',
);

console.log(environmentTemplate.id);
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

`client.beta.agents.environments.templates.update(stringenvironmentTemplateID, TemplateUpdateParamsbody?, RequestOptionsoptions?): EnvironmentTemplate`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID: string`

- `body: TemplateUpdateParams`

  - `capability_directories?: Array<string> | null`

    Directories that expose capabilities to the agent.

  - `desktop?: Desktop | null`

    Replacement desktop configuration, or null to disable the desktop.

    - `enabled: boolean`

      Whether to provision the desktop and its browser proxy.

  - `env?: Record<string, string> | null`

    Replacement confidential environment values.

  - `files?: Array<HostedEnvironmentFileParam> | null`

    Replacement file configuration materialized for each new session.

    - `HostedEnvironmentFileParamFileID`

      A file previously uploaded through the OpenAI Files API.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedEnvironmentFileParamInline`

      A file supplied directly as standard-base64 data.

      - `data: string`

        The standard-base64-encoded file contents.

      - `path: string`

        The absolute destination path inside `/workspace`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name?: string | null`

    A replacement human-readable display name, or `null` to clear the name.

  - `network?: Network | null`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

    - `access: "enabled" | "disabled" | "restricted"`

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

    - `allowed_domains?: Array<string> | null`

      Domains the environment may access when network access is restricted.

    - `blocked_domains?: Array<string> | null`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `packages?: Packages | null`

    Packages installed before the runtime network policy applies.

    - `npm?: Array<string> | null`

      npm packages to install globally. Defaults to an empty list.

    - `python?: Array<string> | null`

      Python packages to install. Defaults to an empty list.

    - `system?: Array<string> | null`

      System packages to install. Defaults to an empty list.

  - `plugins?: Array<HostedPluginParam> | null`

    Replacement plugin configuration installed for each new session.

    - `description: string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `name: string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `source: InlineCapabilitySourceParam`

      Provides ZIP bytes encoded with standard base64.

      - `data: string`

        Standard-base64 encoded ZIP archive bytes.

      - `media_type: "application/zip"`

        The archive media type, always `application/zip`.

        - `"application/zip"`

          A ZIP archive.

      - `type: "base64"`

        The type of the object. Always `base64`.

        - `"base64"`

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `setup_commands?: Array<SetupCommandParam> | null`

    Replacement confidential setup commands, never included in returned resources.

    - `command: string`

      The shell command to execute.

    - `cwd?: string | null`

      The absolute working directory. Defaults to `/workspace`.

  - `skills?: Array<HostedSkillParam> | null`

    Replacement skill configuration installed for each new session.

    - `HostedSkillParamSkillReference`

      References a skill uploaded through the Skills API.

      - `skill_id: string`

        The ID of the skill created through `/v1/skills`.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version?: string | null`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInline`

      Supplies a skill ZIP directly in the session request.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `source: InlineCapabilitySourceParam`

        Provides ZIP bytes encoded with standard base64.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

### Returns

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const environmentTemplate = await client.beta.agents.environments.templates.update(
  'environment_template_id',
);

console.log(environmentTemplate.id);
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

- `EnvironmentTemplate`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `id: string`

    The ID of the reusable environment template.

  - `capability_directories: Array<string>`

    Directories that expose capabilities to the agent.

  - `created_at: number`

    The Unix timestamp, in seconds, when the template was created.

  - `desktop: Desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `enabled: boolean`

      Whether the environment provisions a desktop and browser proxy.

  - `files: Array<HostedTemplateFileResourceFileID | HostedTemplateFileResourceInline>`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `HostedTemplateFileResourceFileID`

      A project-scoped Files API reference resolved separately for each session.

      - `file_id: string`

        The ID of the uploaded file.

      - `path: string`

        The file's absolute path inside the environment.

      - `type: "file_id"`

        The type of the object. Always `file_id`.

        - `"file_id"`

    - `HostedTemplateFileResourceInline`

      Metadata for confidential inline file contents.

      - `path: string`

        The file's absolute path inside the environment.

      - `size_bytes: number`

        The decoded size of the inline file in bytes.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `name: string | null`

    An optional human-readable display name for the template.

  - `network: Network`

    Runtime network access for each OpenAI-hosted environment.

    - `access: "enabled" | "disabled" | "restricted"`

      The environment's network access mode.

      - `"enabled"`

        Allows unrestricted network access.

      - `"disabled"`

        Disables network access.

      - `"restricted"`

        Applies the configured domain restrictions.

    - `allowed_domains: Array<string>`

      Domains the environment may access when network access is restricted.

  - `object: "agent.environment.template"`

    The object type. Always `agent.environment.template`.

    - `"agent.environment.template"`

  - `packages: Packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `npm: Array<string>`

      npm packages installed globally in the environment.

    - `python: Array<string>`

      Python packages installed in the environment.

    - `system: Array<string>`

      System packages installed in the environment.

  - `plugins: Array<HostedPlugin>`

    Safe plugin metadata, excluding inline archive contents.

    - `description: string`

      The installed plugin description.

    - `name: string`

      The installed plugin name.

    - `type: "inline"`

      The type of the object. Always `inline`.

      - `"inline"`

  - `skills: Array<HostedTemplateSkillResourceSkillReference | HostedTemplateSkillResourceInline>`

    Safe skill metadata, preserving unresolved version selectors.

    - `HostedTemplateSkillResourceSkillReference`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `skill_id: string`

        The referenced skill ID.

      - `type: "skill_reference"`

        The type of the object. Always `skill_reference`.

        - `"skill_reference"`

      - `version: string | null`

        The requested version selector, including `latest`.

    - `HostedTemplateSkillResourceInline`

      Safe metadata for an inline skill archive.

      - `description: string`

        The skill description declared in `SKILL.md`.

      - `name: string`

        The skill name declared in `SKILL.md`.

      - `type: "inline"`

        The type of the object. Always `inline`.

        - `"inline"`

  - `updated_at: number`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `EnvironmentTemplateDeleted`

  A deleted reusable environment template.

  - `id: string`

    The ID of the deleted environment template.

  - `deleted: boolean`

    Whether the environment template was deleted. Always `true`.

  - `object: "agent.environment.template.deleted"`

    The object type. Always `agent.environment.template.deleted`.

    - `"agent.environment.template.deleted"`

# Sessions

## Create an agent session

`client.beta.agents.sessions.create(SessionCreateParamsbody, RequestOptionsoptions?): AgentSession | Stream<AgentSessionEvent>`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `SessionCreateParams = SessionCreateParamsNonStreaming | SessionCreateParamsStreaming`

  - `SessionCreateParamsBase`

    - `environment: EnvironmentParam`

      An inline execution environment or a reference to an environment template.

      - `EnvironmentParamNone`

        Runs the agent without an execution environment.

        - `type: "none"`

          The type of the object. Always `none`.

          - `"none"`

      - `EnvironmentParamOpenAIHosted`

        An existing OpenAI-hosted environment or new inline/template-based hosted configuration.

        - `type: "openai_hosted"`

          The type of the object. Always `openai_hosted`.

          - `"openai_hosted"`

        - `capability_directories?: Array<string> | null`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

        - `container_size?: "small" | "medium" | "large"`

          The hosted container size. Omission selects the medium tier.

          - `"small"`

          - `"medium"`

          - `"large"`

        - `desktop?: Desktop | null`

          Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

          - `enabled: boolean`

            Whether to provision the desktop and its browser proxy.

        - `env?: Record<string, string> | null`

          Environment variables made available to the agent.

        - `environment_template_id?: string`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

        - `files?: Array<HostedEnvironmentFileParam> | null`

          Files available before the agent starts. Defaults to an empty list.

          - `HostedEnvironmentFileParamFileID`

            A file previously uploaded through the OpenAI Files API.

            - `file_id: string`

              The ID of the uploaded file.

            - `path: string`

              The absolute destination path inside `/workspace`.

            - `type: "file_id"`

              The type of the object. Always `file_id`.

              - `"file_id"`

          - `HostedEnvironmentFileParamInline`

            A file supplied directly as standard-base64 data.

            - `data: string`

              The standard-base64-encoded file contents.

            - `path: string`

              The absolute destination path inside `/workspace`.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

        - `network?: Network | null`

          Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

          - `access: "enabled" | "disabled" | "restricted"`

            The environment's network access mode.

            - `"enabled"`

              Allows unrestricted network access.

            - `"disabled"`

              Disables network access.

            - `"restricted"`

              Applies the configured domain restrictions.

          - `allowed_domains?: Array<string> | null`

            Domains the environment may access when network access is restricted.

          - `blocked_domains?: Array<string> | null`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

        - `packages?: Packages | null`

          Packages to install in the environment. Defaults to empty package lists.

          - `npm?: Array<string> | null`

            npm packages to install globally. Defaults to an empty list.

          - `python?: Array<string> | null`

            Python packages to install. Defaults to an empty list.

          - `system?: Array<string> | null`

            System packages to install. Defaults to an empty list.

        - `plugins?: Array<HostedPluginParam> | null`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          - `description: string`

            The plugin description declared in `.codex-plugin/plugin.json`.

          - `name: string`

            The plugin name declared in `.codex-plugin/plugin.json`.

          - `source: InlineCapabilitySourceParam`

            Provides ZIP bytes encoded with standard base64.

            - `data: string`

              Standard-base64 encoded ZIP archive bytes.

            - `media_type: "application/zip"`

              The archive media type, always `application/zip`.

              - `"application/zip"`

                A ZIP archive.

            - `type: "base64"`

              The type of the object. Always `base64`.

              - `"base64"`

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

        - `setup_commands?: Array<SetupCommandParam> | null`

          Ordered, confidential setup commands. Command bodies are never returned.

          - `command: string`

            The shell command to execute.

          - `cwd?: string | null`

            The absolute working directory. Defaults to `/workspace`.

        - `skills?: Array<HostedSkillParam> | null`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          - `HostedSkillParamSkillReference`

            References a skill uploaded through the Skills API.

            - `skill_id: string`

              The ID of the skill created through `/v1/skills`.

            - `type: "skill_reference"`

              The type of the object. Always `skill_reference`.

              - `"skill_reference"`

            - `version?: string | null`

              The skill version, a positive integer or `latest`; omission selects the default.

          - `HostedSkillParamInline`

            Supplies a skill ZIP directly in the session request.

            - `description: string`

              The skill description declared in `SKILL.md`.

            - `name: string`

              The skill name declared in `SKILL.md`.

            - `source: InlineCapabilitySourceParam`

              Provides ZIP bytes encoded with standard base64.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

      - `EnvironmentParamSelfHosted`

        An application-hosted environment configured inline.

        - `type: "self_hosted"`

          The type of the object. Always `self_hosted`.

          - `"self_hosted"`

        - `workspace_directory: string`

          Absolute project directory inside the self-hosted environment.

        - `capability_directories?: Array<string> | null`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `agent?: Agent`

      Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

      - `instructions?: string | null`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

      - `model?: string`

        The model to use for the agent. The requested model name is preserved.

      - `multi_agent?: MultiAgentConfigParam | null`

        Configuration for creating and coordinating subagents.

        - `enabled: boolean`

          Whether subagent tools are enabled.

        - `max_concurrent_subagents?: number`

          Maximum number of subagents that may run concurrently. Defaults to 6.

      - `reasoning?: AgentReasoningParam | null`

        Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

        - `effort?: "none" | "minimal" | "low" | 4 more | null`

          The amount of reasoning effort the model should use. Omission lets the model select it.

          - `"none"`

          - `"minimal"`

          - `"low"`

          - `"medium"`

          - `"high"`

          - `"xhigh"`

          - `"max"`

        - `summary?: "concise" | "detailed" | "auto" | null`

          Controls whether the response includes a reasoning summary.

          - `"concise"`

            Returns a concise reasoning summary when supported.

          - `"detailed"`

            Returns a detailed reasoning summary when supported.

          - `"auto"`

            Automatically selects the most detailed summary supported by the model.

      - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

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

      - `text?: AgentTextParam | null`

        Configuration for text generated by the agent.

        - `format?: TextFormatParam | null`

          The output format. Omission uses ordinary text (`{"type": "text"}`).

          - `TextFormatParamText`

            Generates ordinary text without a structured-output constraint.

            - `type: "text"`

              The type of the object. Always `text`.

              - `"text"`

          - `TextFormatParamJSONSchema`

            Constrains generated text to a JSON Schema.

            - `schema: Record<string, unknown>`

              The JSON Schema that generated text must match.

            - `type: "json_schema"`

              The type of the object. Always `json_schema`.

              - `"json_schema"`

        - `verbosity?: "low" | "medium" | "high" | null`

          The amount of text the model should produce. Defaults to `medium`, matching Responses.

          - `"low"`

            Produces less text.

          - `"medium"`

            Uses the default amount of text.

          - `"high"`

            Produces more text.

      - `tools?: Array<AgentToolParam> | null`

        Tools available to the agent. Omit to inherit, or pass null to clear them.

        - `AgentToolConfigParamFunction`

          A function defined by the application.

          - `description: string`

            A description of what the function does.

          - `name: string`

            The name of the function.

          - `parameters: Record<string, unknown>`

            A JSON Schema object describing the function's arguments.

          - `type: "function"`

            The type of the object. Always `function`.

            - `"function"`

          - `defer_loading?: boolean`

            Whether this function is deferred and discovered through tool search. Defaults to `false`.

        - `AgentToolConfigParamToolSearch`

          Discovers deferred function tools and loads them into the model context.

          - `type: "tool_search"`

            The type of the object. Always `tool_search`.

            - `"tool_search"`

        - `AgentToolConfigParamProgrammaticToolCalling`

          Enables calling tools from model-generated code.

          - `type: "programmatic_tool_calling"`

            The type of the object. Always `programmatic_tool_calling`.

            - `"programmatic_tool_calling"`

          - `enabled?: boolean`

            Whether tools can be called from model-generated code. Defaults to `true`.

        - `AgentToolConfigParamMcp`

          Tools provided by a remote MCP server.

          - `server_label: string`

            A label used to identify the MCP server in tool calls.

          - `transport: McpTransportParam`

            The transport used to connect to the MCP server.

            - `McpTransportConfigParamHTTP`

              Connects to an MCP server over HTTP.

              - `server_url: string`

                The URL of the MCP server.

              - `type: "http"`

                The type of the object. Always `http`.

                - `"http"`

              - `authorization?: string | null`

                The authorization value sent to the MCP server, if any.

              - `headers?: Record<string, string> | null`

                Additional HTTP headers sent to the MCP server.

            - `McpTransportConfigParamStdio`

              Starts an MCP server as a local process.

              - `command: string`

                The command used to start the MCP server.

              - `cwd: string`

                The working directory used to start the MCP server.

              - `type: "stdio"`

                The type of the object. Always `stdio`.

                - `"stdio"`

              - `args?: Array<string> | null`

                Arguments passed to the MCP server command.

              - `env?: Record<string, string> | null`

                Environment variables set for the MCP server process.

              - `env_vars?: Array<string> | null`

                Environment variable names to inherit from the selected execution environment.

          - `type: "mcp"`

            The type of the object. Always `mcp`.

            - `"mcp"`

          - `allowed_tools?: Array<string> | null`

            The MCP tools the agent may call. All server tools are allowed when omitted.

          - `connection_origin?: "service" | "environment" | null`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `"service"`

              Uses the Managed Agents service network.

            - `"environment"`

              Uses the session's execution environment.

          - `credential_id?: string | null`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

          - `request_metadata?: Record<string, unknown> | null`

            Metadata included with requests to this MCP server.

          - `required?: boolean`

            Whether this MCP server must initialize before the first turn. Defaults to `false`.

        - `AgentToolConfigParamWebSearch`

          Web search.

          - `type: "web_search"`

            The type of the object. Always `web_search`.

            - `"web_search"`

          - `allowed_domains?: Array<string> | null`

            Domains the search may include.

          - `context_size?: "low" | "medium" | "high" | null`

            The amount of search context made available to the model. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

          - `location?: Location | null`

            Approximate location used to localize search results.

            - `city?: string | null`

              The city name.

            - `country?: string | null`

              The two-letter ISO country code, such as `US`.

            - `region?: string | null`

              The region or state name.

            - `timezone?: string | null`

              The IANA timezone, such as `America/Los_Angeles`.

          - `mode?: "disabled" | "cached" | "live" | null`

            The source used for web search results. Defaults to `live`.

            - `"disabled"`

              Disables web search.

            - `"cached"`

              Uses cached search results.

            - `"live"`

              Searches the live web.

        - `AgentToolConfigParamComputerUse`

          Browser use in an OpenAI-hosted session.

          - `type: "computer_use"`

            The type of the object. Always `computer_use`.

            - `"computer_use"`

          - `include_screenshots?: boolean`

            Whether computer tool outputs include screenshots. Defaults to `false`.

    - `agent_id?: string`

      The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

    - `input?: string | Array<AgentSessionInputMessageParam> | null`

      Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

      - `string`

      - `Array<AgentSessionInputMessageParam>`

        - `content: Array<InputContentParam>`

          The content of the message.

          - `InputContentParamInputText`

            Text input to the model.

            - `text: string`

              The text sent to the model.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `InputContentParamInputImage`

            Image input to the model.

            - `image_url: string`

              The URL of the image sent to the model.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

        - `role: "user"`

          The role of the message author. Always `user`.

          - `"user"`

        - `type?: "message"`

          The type of the input item. Always `message`.

          - `"message"`

    - `metadata?: Record<string, string> | null`

      Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

    - `stream?: false`

      Whether to stream session events as server-sent events. Defaults to `false`.

      - `false`

    - `vault_ids?: Array<string> | null`

      The IDs of vaults made available to the session.

  - `SessionCreateParamsNonStreaming extends SessionCreateParamsBase`

    - `stream?: false`

      Whether to stream session events as server-sent events. Defaults to `false`.

  - `SessionCreateParamsStreaming extends SessionCreateParamsBase`

    - `stream: true`

      Whether to stream session events as server-sent events. Defaults to `false`.

      - `true`

### Returns

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: "none" | "minimal" | "low" | 4 more | null`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

      - `summary: "concise" | "detailed" | "auto" | null`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `"concise"`

          Returns a concise reasoning summary when supported.

        - `"detailed"`

          Returns a detailed reasoning summary when supported.

        - `"auto"`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: "auto" | "default" | "flex" | 3 more`

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

        - `TextFormatResourceText`

          Generates ordinary text without a structured-output constraint.

          - `type: "text"`

            The type of the object. Always `text`.

            - `"text"`

        - `TextFormatResourceJSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Record<string, unknown>`

            The JSON Schema that generated text must match.

          - `type: "json_schema"`

            The type of the object. Always `json_schema`.

            - `"json_schema"`

      - `verbosity: "low" | "medium" | "high"`

        The amount of text produced by the agent. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

    - `tools: Array<AgentTool>`

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

      - `AgentToolResourceProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: boolean`

          Whether tools can be called from model-generated code.

        - `type: "programmatic_tool_calling"`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `AgentToolResourceMcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array<string> | null`

          The MCP tools the agent may call.

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

            - `type: "stdio"`

              The type of the object. Always `stdio`.

              - `"stdio"`

        - `type: "mcp"`

          The type of the object. Always `mcp`.

          - `"mcp"`

      - `AgentToolResourceWebSearch`

        Web search.

        - `allowed_domains: Array<string> | null`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: "disabled" | "cached" | "live"`

          The source used for web search results.

          - `"disabled"`

          - `"cached"`

          - `"live"`

        - `type: "web_search"`

          The type of the object. Always `web_search`.

          - `"web_search"`

      - `AgentToolResourceComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: boolean`

          Whether computer tool outputs include screenshots.

        - `type: "computer_use"`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

        - `access: "enabled" | "disabled" | "restricted"`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: Array<string>`

          Domains the environment may access when network access is restricted.

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSession = await client.beta.agents.sessions.create({ environment: { type: 'none' } });

console.log(agentSession.id);
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

`client.beta.agents.sessions.delete(stringsessionID, RequestOptionsoptions?): AgentSessionDeleted`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID: string`

### Returns

- `AgentSessionDeleted`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `id: string`

    The ID of the deleted session.

  - `deleted: boolean`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `object: "agent.session.deleted"`

    The object type. Always `agent.session.deleted`.

    - `"agent.session.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSessionDeleted = await client.beta.agents.sessions.delete('session_id');

console.log(agentSessionDeleted.id);
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

`client.beta.agents.sessions.list(SessionListParamsquery?, RequestOptionsoptions?): CursorPage<AgentSession>`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `query: SessionListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `agent_id?: string`

    Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

  - `limit?: number | null`

    The maximum number of resources to return.

  - `order?: "asc" | "desc"`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: "none" | "minimal" | "low" | 4 more | null`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

      - `summary: "concise" | "detailed" | "auto" | null`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `"concise"`

          Returns a concise reasoning summary when supported.

        - `"detailed"`

          Returns a detailed reasoning summary when supported.

        - `"auto"`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: "auto" | "default" | "flex" | 3 more`

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

        - `TextFormatResourceText`

          Generates ordinary text without a structured-output constraint.

          - `type: "text"`

            The type of the object. Always `text`.

            - `"text"`

        - `TextFormatResourceJSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Record<string, unknown>`

            The JSON Schema that generated text must match.

          - `type: "json_schema"`

            The type of the object. Always `json_schema`.

            - `"json_schema"`

      - `verbosity: "low" | "medium" | "high"`

        The amount of text produced by the agent. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

    - `tools: Array<AgentTool>`

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

      - `AgentToolResourceProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: boolean`

          Whether tools can be called from model-generated code.

        - `type: "programmatic_tool_calling"`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `AgentToolResourceMcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array<string> | null`

          The MCP tools the agent may call.

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

            - `type: "stdio"`

              The type of the object. Always `stdio`.

              - `"stdio"`

        - `type: "mcp"`

          The type of the object. Always `mcp`.

          - `"mcp"`

      - `AgentToolResourceWebSearch`

        Web search.

        - `allowed_domains: Array<string> | null`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: "disabled" | "cached" | "live"`

          The source used for web search results.

          - `"disabled"`

          - `"cached"`

          - `"live"`

        - `type: "web_search"`

          The type of the object. Always `web_search`.

          - `"web_search"`

      - `AgentToolResourceComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: boolean`

          Whether computer tool outputs include screenshots.

        - `type: "computer_use"`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

        - `access: "enabled" | "disabled" | "restricted"`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: Array<string>`

          Domains the environment may access when network access is restricted.

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSession of client.beta.agents.sessions.list()) {
  console.log(agentSession.id);
}
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

`client.beta.agents.sessions.retrieve(stringsessionID, RequestOptionsoptions?): AgentSession`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID: string`

### Returns

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: "none" | "minimal" | "low" | 4 more | null`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

      - `summary: "concise" | "detailed" | "auto" | null`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `"concise"`

          Returns a concise reasoning summary when supported.

        - `"detailed"`

          Returns a detailed reasoning summary when supported.

        - `"auto"`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: "auto" | "default" | "flex" | 3 more`

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

        - `TextFormatResourceText`

          Generates ordinary text without a structured-output constraint.

          - `type: "text"`

            The type of the object. Always `text`.

            - `"text"`

        - `TextFormatResourceJSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Record<string, unknown>`

            The JSON Schema that generated text must match.

          - `type: "json_schema"`

            The type of the object. Always `json_schema`.

            - `"json_schema"`

      - `verbosity: "low" | "medium" | "high"`

        The amount of text produced by the agent. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

    - `tools: Array<AgentTool>`

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

      - `AgentToolResourceProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: boolean`

          Whether tools can be called from model-generated code.

        - `type: "programmatic_tool_calling"`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `AgentToolResourceMcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array<string> | null`

          The MCP tools the agent may call.

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

            - `type: "stdio"`

              The type of the object. Always `stdio`.

              - `"stdio"`

        - `type: "mcp"`

          The type of the object. Always `mcp`.

          - `"mcp"`

      - `AgentToolResourceWebSearch`

        Web search.

        - `allowed_domains: Array<string> | null`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: "disabled" | "cached" | "live"`

          The source used for web search results.

          - `"disabled"`

          - `"cached"`

          - `"live"`

        - `type: "web_search"`

          The type of the object. Always `web_search`.

          - `"web_search"`

      - `AgentToolResourceComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: boolean`

          Whether computer tool outputs include screenshots.

        - `type: "computer_use"`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

        - `access: "enabled" | "disabled" | "restricted"`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: Array<string>`

          Domains the environment may access when network access is restricted.

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSession = await client.beta.agents.sessions.retrieve('session_id');

console.log(agentSession.id);
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

`client.beta.agents.sessions.update(stringsessionID, SessionUpdateParamsbody?, RequestOptionsoptions?): AgentSession`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID: string`

- `body: SessionUpdateParams`

  - `agent?: Agent`

    Model settings for subsequent turns. Omitted fields stay unchanged.

    - `model?: string`

      The model for subsequent turns. Omit to keep the current model.

    - `reasoning?: Reasoning`

      Reasoning settings to update. Omit to keep the current effort.

      - `effort?: "none" | "minimal" | "low" | 4 more | null`

        Omit to keep the current effort. Null selects the model's default effort.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

    - `service_tier?: "auto" | "default" | "flex" | 3 more | null`

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

  - `metadata?: Record<string, string> | null`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `AgentSession`

  A Managed Agents session.

  - `id: string`

    The ID of the session.

  - `agent: Agent`

    The agent running in the session.

    - `id: string`

      The ID of the agent.

    - `instructions: string | null`

      Custom instructions appended to the agent's default base instructions.

    - `model: string`

      The model used by the agent.

    - `multi_agent: MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `enabled: boolean`

        Whether subagent tools are enabled. Defaults to false.

      - `max_concurrent_subagents: number | null`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `name: string | null`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `reasoning: AgentReasoning`

      The agent's reasoning configuration.

      - `effort: "none" | "minimal" | "low" | 4 more | null`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `"none"`

        - `"minimal"`

        - `"low"`

        - `"medium"`

        - `"high"`

        - `"xhigh"`

        - `"max"`

      - `summary: "concise" | "detailed" | "auto" | null`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `"concise"`

          Returns a concise reasoning summary when supported.

        - `"detailed"`

          Returns a detailed reasoning summary when supported.

        - `"auto"`

          Automatically selects the most detailed summary supported by the model.

    - `service_tier: "auto" | "default" | "flex" | 3 more`

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

        - `TextFormatResourceText`

          Generates ordinary text without a structured-output constraint.

          - `type: "text"`

            The type of the object. Always `text`.

            - `"text"`

        - `TextFormatResourceJSONSchema`

          Constrains generated text to a JSON Schema.

          - `schema: Record<string, unknown>`

            The JSON Schema that generated text must match.

          - `type: "json_schema"`

            The type of the object. Always `json_schema`.

            - `"json_schema"`

      - `verbosity: "low" | "medium" | "high"`

        The amount of text produced by the agent. Defaults to `medium`.

        - `"low"`

        - `"medium"`

        - `"high"`

    - `tools: Array<AgentTool>`

      Tools available to the agent.

      - `AgentToolResourceFunction`

        A function defined by the application.

        - `defer_loading: boolean`

          Whether the function is deferred and discovered through tool search.

        - `description: string`

          A description of what the function does.

        - `name: string`

          The name of the function.

        - `parameters: Record<string, unknown>`

          A JSON Schema object describing the function's arguments.

        - `type: "function"`

          The type of the object. Always `function`.

          - `"function"`

      - `AgentToolResourceProgrammaticToolCalling`

        Enables calling tools from model-generated code.

        - `enabled: boolean`

          Whether tools can be called from model-generated code.

        - `type: "programmatic_tool_calling"`

          The type of the object. Always `programmatic_tool_calling`.

          - `"programmatic_tool_calling"`

      - `AgentToolResourceMcp`

        Tools provided by a remote MCP server.

        - `allowed_tools: Array<string> | null`

          The MCP tools the agent may call.

        - `connection_origin: "service" | "environment"`

          Where outbound MCP HTTP connections originate.

          - `"service"`

          - `"environment"`

        - `credential_id: string | null`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `request_metadata: Record<string, unknown>`

          Metadata included with requests to this MCP server.

        - `required: boolean`

          Whether this MCP server must initialize before the first turn.

        - `server_label: string`

          A label used to identify the MCP server in tool calls.

        - `transport: McpTransport`

          The transport used to connect to the MCP server.

          - `McpTransportResourceHTTP`

            Connects to an MCP server over HTTP.

            - `server_url: string`

              The URL of the MCP server.

            - `type: "http"`

              The type of the object. Always `http`.

              - `"http"`

          - `McpTransportResourceStdio`

            Starts an MCP server as a local process.

            - `args: Array<string>`

              Arguments passed to the MCP server command.

            - `command: string`

              The command used to start the MCP server.

            - `cwd: string`

              The working directory used to start the MCP server.

            - `env_vars: Array<string>`

              Environment variable names inherited from the execution environment.

            - `type: "stdio"`

              The type of the object. Always `stdio`.

              - `"stdio"`

        - `type: "mcp"`

          The type of the object. Always `mcp`.

          - `"mcp"`

      - `AgentToolResourceWebSearch`

        Web search.

        - `allowed_domains: Array<string> | null`

          Allowed search domains, or `null` when the search is unrestricted.

        - `context_size: "low" | "medium" | "high"`

          The amount of search context made available to the model. Defaults to `medium`.

          - `"low"`

          - `"medium"`

          - `"high"`

        - `location: Location | null`

          Approximate location used to localize search results, if provided.

          - `city: string | null`

            The city name.

          - `country: string | null`

            The two-letter ISO country code, such as `US`.

          - `region: string | null`

            The region or state name.

          - `timezone: string | null`

            The IANA timezone, such as `America/Los_Angeles`.

        - `mode: "disabled" | "cached" | "live"`

          The source used for web search results.

          - `"disabled"`

          - `"cached"`

          - `"live"`

        - `type: "web_search"`

          The type of the object. Always `web_search`.

          - `"web_search"`

      - `AgentToolResourceComputerUse`

        Browser use in an OpenAI-hosted session.

        - `include_screenshots: boolean`

          Whether computer tool outputs include screenshots.

        - `type: "computer_use"`

          The type of the object. Always `computer_use`.

          - `"computer_use"`

  - `created_at: number`

    The Unix timestamp, in seconds, when the session was created.

  - `environment: Environment`

    The execution environment for the session.

    - `EnvironmentResourceNone`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `type: "none"`

        The type of the object. Always `none`.

        - `"none"`

    - `EnvironmentResourceOpenAIHosted`

      An environment hosted by OpenAI.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `desktop: Desktop`

        The effective desktop configuration.

        - `enabled: boolean`

          Whether the environment provisions a desktop and browser proxy.

      - `files: Array<HostedEnvironmentFile>`

        Files available in the environment, excluding their contents.

        - `HostedEnvironmentFileID`

          A file copied from the OpenAI Files API.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `file_id: string`

            The ID of the uploaded file.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "file_id"`

            The type of the object. Always `file_id`.

            - `"file_id"`

        - `HostedEnvironmentFileResourceInline`

          A file supplied inline when the session was created.

          - `id: string`

            The session-scoped ID of the file in the execution environment.

          - `path: string`

            The file's absolute path inside the environment.

          - `size_bytes: number`

            The decoded file size in bytes.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `network: Network`

        The effective network access policy for the environment.

        - `access: "enabled" | "disabled" | "restricted"`

          The environment's network access mode.

          - `"enabled"`

            Allows unrestricted network access.

          - `"disabled"`

            Disables network access.

          - `"restricted"`

            Applies the configured domain restrictions.

        - `allowed_domains: Array<string>`

          Domains the environment may access when network access is restricted.

      - `packages: Packages`

        Packages installed in the environment.

        - `npm: Array<string>`

          npm packages installed globally in the environment.

        - `python: Array<string>`

          Python packages installed in the environment.

        - `system: Array<string>`

          System packages installed in the environment.

      - `plugins: Array<HostedPlugin>`

        Plugins installed in the environment, excluding their archive contents.

        - `description: string`

          The installed plugin description.

        - `name: string`

          The installed plugin name.

        - `type: "inline"`

          The type of the object. Always `inline`.

          - `"inline"`

      - `skills: Array<HostedSkill>`

        Skills installed in the environment, excluding their archive contents.

        - `HostedSkillReference`

          A skill installed from the Skills API.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `skill_id: string`

            The referenced skill ID.

          - `type: "skill_reference"`

            The type of the object. Always `skill_reference`.

            - `"skill_reference"`

          - `version: string`

            The concrete skill version installed for this session.

        - `HostedSkillResourceInline`

          A skill installed from an inline ZIP archive.

          - `description: string`

            The installed skill description.

          - `name: string`

            The installed skill name.

          - `type: "inline"`

            The type of the object. Always `inline`.

            - `"inline"`

      - `type: "openai_hosted"`

        The type of the object. Always `openai_hosted`.

        - `"openai_hosted"`

      - `container_size?: "small" | "medium" | "large" | null`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `"small"`

        - `"medium"`

        - `"large"`

    - `EnvironmentResourceSelfHosted`

      An environment hosted by the application.

      - `id: string`

        The public ID of the environment.

      - `capability_directories: Array<string>`

        Directories that contain capabilities exposed to the agent.

      - `remote_url: string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `type: "self_hosted"`

        The type of the object. Always `self_hosted`.

        - `"self_hosted"`

      - `workspace_directory: string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `error: string | null`

    The error that caused the session to fail, if any.

  - `last_active_at: number`

    The Unix timestamp, in seconds, when the session was last active.

  - `metadata: Record<string, string>`

    Custom string key-value pairs attached to the session.

  - `object: "agent.session"`

    The object type. Always `agent.session`.

    - `"agent.session"`

  - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

    Actions that must be completed before the session can continue.

    - `SessionRequiredActionResourceComputerUseApprovalRequest`

      Respond to a computer-use request.

      - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

        The information needed to render the request.

        - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

          A browser origin awaiting the application's approval decision.

          - `origin: string`

            The origin the browser needs permission to access.

          - `reason: string | null`

            The browser's explanation for this request, or null when unavailable.

          - `type: "browser_origin_access"`

            The type of the object. Always `browser_origin_access`.

            - `"browser_origin_access"`

      - `request_id: string`

        The registered request ID to echo when responding.

      - `turn_id: string`

        The turn that requested approval.

      - `type: "computer_use_approval_request"`

        The type of the object. Always `computer_use_approval_request`.

        - `"computer_use_approval_request"`

    - `SessionRequiredActionResourceFunctionCall`

      Run a function tool and submit its result.

      - `arguments: unknown`

        The arguments supplied by the model.

      - `call_id: string`

        The ID to include when submitting the function result.

      - `name: string`

        The function name.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "function_call"`

        The type of the object. Always `function_call`.

        - `"function_call"`

    - `SessionRequiredActionResourceEnvironmentConnection`

      Reconnect a session environment.

      - `environment_id: string`

        The ID of the environment to reconnect.

      - `type: "environment_connection"`

        The type of the object. Always `environment_connection`.

        - `"environment_connection"`

  - `status: "idle" | "in_progress" | "requires_action" | "failed"`

    The current status of the session.

    - `"idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `"in_progress"`

      The session is processing a turn.

    - `"requires_action"`

      The session is waiting for one or more required actions.

    - `"failed"`

      The session failed.

  - `usage: TokenUsage | null`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

  - `vault_ids: Array<string>`

    The IDs of vaults made available to the session.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSession = await client.beta.agents.sessions.update('session_id');

console.log(agentSession.id);
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

`client.beta.agents.sessions.artifacts.content(stringartifactID, ArtifactContentParamsparams, RequestOptionsoptions?): Response`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactContentParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `unnamed_schema_2 = Response`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const response = await client.beta.agents.sessions.artifacts.content('artifact_id', {
  session_id: 'session_id',
});

console.log(response);

const content = await response.blob();
console.log(content);
```

## Delete an agent session artifact

`client.beta.agents.sessions.artifacts.delete(stringartifactID, ArtifactDeleteParamsparams, RequestOptionsoptions?): SessionArtifactDeleted`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactDeleteParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: string`

    The ID of the deleted session artifact.

  - `deleted: boolean`

    Whether the session artifact was deleted. Always `true`.

  - `object: "agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const sessionArtifactDeleted = await client.beta.agents.sessions.artifacts.delete('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifactDeleted.id);
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

`client.beta.agents.sessions.artifacts.list(stringsessionID, ArtifactListParamsquery?, RequestOptionsoptions?): CursorPage<SessionArtifact>`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID: string`

- `query: ArtifactListParams`

  - `after?: string | null`

    Return artifacts after this immutable artifact ID.

  - `environment_id?: string | null`

    Restrict the listing to artifacts produced by this environment.

  - `limit?: number | null`

    The maximum number of artifacts to return, between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort by creation time and ID. Defaults to descending.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const sessionArtifact of client.beta.agents.sessions.artifacts.list('session_id')) {
  console.log(sessionArtifact.id);
}
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

`client.beta.agents.sessions.artifacts.retrieve(stringartifactID, ArtifactRetrieveParamsparams, RequestOptionsoptions?): SessionArtifact`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `artifactID: string`

- `params: ArtifactRetrieveParams`

  - `session_id: string`

    The ID of the session that owns the artifact.

### Returns

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const sessionArtifact = await client.beta.agents.sessions.artifacts.retrieve('artifact_id', {
  session_id: 'session_id',
});

console.log(sessionArtifact.id);
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

- `SessionArtifact`

  An immutable file published by a completed hosted session turn.

  - `id: string`

    The immutable artifact ID.

  - `created_at: number`

    The Unix timestamp, in seconds, when the artifact was published.

  - `environment_id: string`

    The ID of the environment that produced the artifact.

  - `object: "agent.session.artifact"`

    The object type. Always `agent.session.artifact`.

    - `"agent.session.artifact"`

  - `path: string`

    The original absolute file path in the execution environment.

  - `session_id: string`

    The ID of the session that owns the artifact.

  - `size_bytes: number`

    The immutable artifact size in bytes.

  - `turn_id: string`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `SessionArtifactDeleted`

  Confirmation that an immutable session artifact was deleted.

  - `id: string`

    The ID of the deleted session artifact.

  - `deleted: boolean`

    Whether the session artifact was deleted. Always `true`.

  - `object: "agent.session.artifact.deleted"`

    The object type. Always `agent.session.artifact.deleted`.

    - `"agent.session.artifact.deleted"`

# Events

## Create agent session input events

`client.beta.agents.sessions.events.create(stringsessionID, EventCreateParamsparams, RequestOptionsoptions?): void`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `sessionID: string`

- `params: EventCreateParams`

  - `events: Array<AgentSessionInputParam>`

    Body param: The input events to submit to the session.

    - `SessionInputParamAgentSessionInputComputerUseApprovalRequestResult`

      Responds to a pending Computer Use approval request.

      - `request_id: string`

        The registered request ID from the required action.

      - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

        The response for this request type.

        - `AgentBrowserAuthenticationSubmitParam`

          - `action: "submit"`

            - `"submit"`

          - `fields: Array<Field>`

            Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

            - `field_id: string`

              The field ID from the required action.

            - `value: string`

              The value to enter into the registered control.

          - `type: "browser_authentication"`

            - `"browser_authentication"`

          - `selected_option?: string | null`

            The chosen method. Required when the required action contains options.

        - `AgentBrowserAuthenticationCancelParam`

          - `action: "cancel"`

            - `"cancel"`

          - `type: "browser_authentication"`

            - `"browser_authentication"`

        - `AgentBrowserOriginAccessParam`

          - `decision: "approve" | "deny" | "cancel"`

            Whether to allow, deny, or cancel the requested origin access.

            - `"approve"`

              Allow the browser to access this origin.

            - `"deny"`

              Deny access to this origin.

            - `"cancel"`

              Dismiss this request without approving access.

          - `type: "browser_origin_access"`

            - `"browser_origin_access"`

      - `type: "agent.session.input.computer_use_approval_request_result"`

        The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

        - `"agent.session.input.computer_use_approval_request_result"`

    - `SessionInputParamAgentSessionInputMessage`

      Adds one or more user messages and starts a turn.

      - `input: Array<AgentSessionInputMessageParam>`

        The user messages to add to the session.

        - `content: Array<InputContentParam>`

          The content of the message.

          - `InputContentParamInputText`

            Text input to the model.

            - `text: string`

              The text sent to the model.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `InputContentParamInputImage`

            Image input to the model.

            - `image_url: string`

              The URL of the image sent to the model.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

        - `role: "user"`

          The role of the message author. Always `user`.

          - `"user"`

        - `type?: "message"`

          The type of the input item. Always `message`.

          - `"message"`

      - `type: "agent.session.input.message"`

        The type of the object. Always `agent.session.input.message`.

        - `"agent.session.input.message"`

    - `SessionInputParamAgentSessionInputCancel`

      Cancels the session's active turn.

      - `type: "agent.session.input.cancel"`

        The type of the object. Always `agent.session.input.cancel`.

        - `"agent.session.input.cancel"`

    - `SessionInputParamAgentSessionInputToolResult`

      Submits the result of a function call.

      - `call_id: string`

        The ID of the function call.

      - `success: boolean`

        Whether the function call succeeded.

      - `turn_id: string`

        The ID of the turn that requested the function call.

      - `type: "agent.session.input.tool_result"`

        The type of the object. Always `agent.session.input.tool_result`.

        - `"agent.session.input.tool_result"`

      - `error?: string | null`

        The error message when the call failed.

      - `output?: AgentFunctionCallOutputParam | null`

        The function result when the call succeeded.

        - `string`

        - `Array<InputContentParam>`

          - `InputContentParamInputText`

            Text input to the model.

          - `InputContentParamInputImage`

            Image input to the model.

  - `idempotencyKey?: string`

    Header param: An optional client-generated key that makes retries of submitted messages idempotent.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.beta.agents.sessions.events.create('session_id', {
  events: [
    {
      request_id: 'request_id',
      response: {
        action: 'submit',
        fields: [{ field_id: 'field_id', value: 'value' }],
        type: 'browser_authentication',
      },
      type: 'agent.session.input.computer_use_approval_request_result',
    },
  ],
});
```

## Stream agent session events

`client.beta.agents.sessions.events.stream(stringsessionID, RequestOptionsoptions?): AgentSessionEvent | Stream<AgentSessionEvent>`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `sessionID: string`

### Returns

- `AgentSessionEvent = AgentSessionErrorEvent | AgentSessionEnvironmentReadyEvent | AgentSessionEnvironmentResetEvent | 28 more`

  An event emitted by a Managed Agents session.

  - `AgentSessionErrorEvent`

    Emitted when a turn or session fails.

    - `error: SessionError`

      The error that occurred.

      - `code: string | null`

        The machine-readable error code, if any.

      - `message: string`

        A customer-safe explanation of the error.

      - `param: string | null`

        The request parameter associated with the error, if any.

      - `type: string`

        The error type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `type: "error"`

      The type of the object. Always `error`.

      - `"error"`

  - `AgentSessionEnvironmentReadyEvent`

    Emitted when a hosted session environment is ready to connect.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

      - `id: string`

        The public ID of the environment.

      - `error: Error | null`

        The error reported while preparing the environment, if any.

        - `code: string`

          A machine-readable error code.

        - `message: string`

          A human-readable error message.

        - `type: string`

          The error type.

      - `status: "pending" | "ready" | "connected" | 2 more`

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

      - `type: string`

        The environment type.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.ready"`

      The type of the object. Always `agent.session.environment.ready`.

      - `"agent.session.environment.ready"`

  - `AgentSessionEnvironmentResetEvent`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `environment_id: string`

      The stable environment ID, retained across sandbox replacements.

    - `event_id: string`

      The unique ID of the event.

    - `reset_count: number`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The associated turn, when applicable.

    - `type: "agent.session.environment.reset"`

      The type of the object. Always `agent.session.environment.reset`.

      - `"agent.session.environment.reset"`

  - `AgentOutputCommandExecutionOutputDeltaEvent`

    Emitted when command execution produces an output delta.

    - `delta: string`

      The output text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the command execution item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.output.command_execution_output.delta"`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `"agent.output.command_execution_output.delta"`

  - `AgentSessionCreatedEvent`

    Emitted when a session is created.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that was created.

      - `id: string`

        The ID of the session.

      - `agent: Agent`

        The agent running in the session.

        - `id: string`

          The ID of the agent.

        - `instructions: string | null`

          Custom instructions appended to the agent's default base instructions.

        - `model: string`

          The model used by the agent.

        - `multi_agent: MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `enabled: boolean`

            Whether subagent tools are enabled. Defaults to false.

          - `max_concurrent_subagents: number | null`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `name: string | null`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `reasoning: AgentReasoning`

          The agent's reasoning configuration.

          - `effort: "none" | "minimal" | "low" | 4 more | null`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `"none"`

            - `"minimal"`

            - `"low"`

            - `"medium"`

            - `"high"`

            - `"xhigh"`

            - `"max"`

          - `summary: "concise" | "detailed" | "auto" | null`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `"concise"`

              Returns a concise reasoning summary when supported.

            - `"detailed"`

              Returns a detailed reasoning summary when supported.

            - `"auto"`

              Automatically selects the most detailed summary supported by the model.

        - `service_tier: "auto" | "default" | "flex" | 3 more`

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

            - `TextFormatResourceText`

              Generates ordinary text without a structured-output constraint.

              - `type: "text"`

                The type of the object. Always `text`.

                - `"text"`

            - `TextFormatResourceJSONSchema`

              Constrains generated text to a JSON Schema.

              - `schema: Record<string, unknown>`

                The JSON Schema that generated text must match.

              - `type: "json_schema"`

                The type of the object. Always `json_schema`.

                - `"json_schema"`

          - `verbosity: "low" | "medium" | "high"`

            The amount of text produced by the agent. Defaults to `medium`.

            - `"low"`

            - `"medium"`

            - `"high"`

        - `tools: Array<AgentTool>`

          Tools available to the agent.

          - `AgentToolResourceFunction`

            A function defined by the application.

            - `defer_loading: boolean`

              Whether the function is deferred and discovered through tool search.

            - `description: string`

              A description of what the function does.

            - `name: string`

              The name of the function.

            - `parameters: Record<string, unknown>`

              A JSON Schema object describing the function's arguments.

            - `type: "function"`

              The type of the object. Always `function`.

              - `"function"`

          - `AgentToolResourceProgrammaticToolCalling`

            Enables calling tools from model-generated code.

            - `enabled: boolean`

              Whether tools can be called from model-generated code.

            - `type: "programmatic_tool_calling"`

              The type of the object. Always `programmatic_tool_calling`.

              - `"programmatic_tool_calling"`

          - `AgentToolResourceMcp`

            Tools provided by a remote MCP server.

            - `allowed_tools: Array<string> | null`

              The MCP tools the agent may call.

            - `connection_origin: "service" | "environment"`

              Where outbound MCP HTTP connections originate.

              - `"service"`

              - `"environment"`

            - `credential_id: string | null`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `request_metadata: Record<string, unknown>`

              Metadata included with requests to this MCP server.

            - `required: boolean`

              Whether this MCP server must initialize before the first turn.

            - `server_label: string`

              A label used to identify the MCP server in tool calls.

            - `transport: McpTransport`

              The transport used to connect to the MCP server.

              - `McpTransportResourceHTTP`

                Connects to an MCP server over HTTP.

                - `server_url: string`

                  The URL of the MCP server.

                - `type: "http"`

                  The type of the object. Always `http`.

                  - `"http"`

              - `McpTransportResourceStdio`

                Starts an MCP server as a local process.

                - `args: Array<string>`

                  Arguments passed to the MCP server command.

                - `command: string`

                  The command used to start the MCP server.

                - `cwd: string`

                  The working directory used to start the MCP server.

                - `env_vars: Array<string>`

                  Environment variable names inherited from the execution environment.

                - `type: "stdio"`

                  The type of the object. Always `stdio`.

                  - `"stdio"`

            - `type: "mcp"`

              The type of the object. Always `mcp`.

              - `"mcp"`

          - `AgentToolResourceWebSearch`

            Web search.

            - `allowed_domains: Array<string> | null`

              Allowed search domains, or `null` when the search is unrestricted.

            - `context_size: "low" | "medium" | "high"`

              The amount of search context made available to the model. Defaults to `medium`.

              - `"low"`

              - `"medium"`

              - `"high"`

            - `location: Location | null`

              Approximate location used to localize search results, if provided.

              - `city: string | null`

                The city name.

              - `country: string | null`

                The two-letter ISO country code, such as `US`.

              - `region: string | null`

                The region or state name.

              - `timezone: string | null`

                The IANA timezone, such as `America/Los_Angeles`.

            - `mode: "disabled" | "cached" | "live"`

              The source used for web search results.

              - `"disabled"`

              - `"cached"`

              - `"live"`

            - `type: "web_search"`

              The type of the object. Always `web_search`.

              - `"web_search"`

          - `AgentToolResourceComputerUse`

            Browser use in an OpenAI-hosted session.

            - `include_screenshots: boolean`

              Whether computer tool outputs include screenshots.

            - `type: "computer_use"`

              The type of the object. Always `computer_use`.

              - `"computer_use"`

      - `created_at: number`

        The Unix timestamp, in seconds, when the session was created.

      - `environment: Environment`

        The execution environment for the session.

        - `EnvironmentResourceNone`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `type: "none"`

            The type of the object. Always `none`.

            - `"none"`

        - `EnvironmentResourceOpenAIHosted`

          An environment hosted by OpenAI.

          - `id: string`

            The public ID of the environment.

          - `capability_directories: Array<string>`

            Directories that contain capabilities exposed to the agent.

          - `desktop: Desktop`

            The effective desktop configuration.

            - `enabled: boolean`

              Whether the environment provisions a desktop and browser proxy.

          - `files: Array<HostedEnvironmentFile>`

            Files available in the environment, excluding their contents.

            - `HostedEnvironmentFileID`

              A file copied from the OpenAI Files API.

              - `id: string`

                The session-scoped ID of the file in the execution environment.

              - `file_id: string`

                The ID of the uploaded file.

              - `path: string`

                The file's absolute path inside the environment.

              - `size_bytes: number`

                The decoded file size in bytes.

              - `type: "file_id"`

                The type of the object. Always `file_id`.

                - `"file_id"`

            - `HostedEnvironmentFileResourceInline`

              A file supplied inline when the session was created.

              - `id: string`

                The session-scoped ID of the file in the execution environment.

              - `path: string`

                The file's absolute path inside the environment.

              - `size_bytes: number`

                The decoded file size in bytes.

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

          - `network: Network`

            The effective network access policy for the environment.

            - `access: "enabled" | "disabled" | "restricted"`

              The environment's network access mode.

              - `"enabled"`

                Allows unrestricted network access.

              - `"disabled"`

                Disables network access.

              - `"restricted"`

                Applies the configured domain restrictions.

            - `allowed_domains: Array<string>`

              Domains the environment may access when network access is restricted.

          - `packages: Packages`

            Packages installed in the environment.

            - `npm: Array<string>`

              npm packages installed globally in the environment.

            - `python: Array<string>`

              Python packages installed in the environment.

            - `system: Array<string>`

              System packages installed in the environment.

          - `plugins: Array<HostedPlugin>`

            Plugins installed in the environment, excluding their archive contents.

            - `description: string`

              The installed plugin description.

            - `name: string`

              The installed plugin name.

            - `type: "inline"`

              The type of the object. Always `inline`.

              - `"inline"`

          - `skills: Array<HostedSkill>`

            Skills installed in the environment, excluding their archive contents.

            - `HostedSkillReference`

              A skill installed from the Skills API.

              - `description: string`

                The installed skill description.

              - `name: string`

                The installed skill name.

              - `skill_id: string`

                The referenced skill ID.

              - `type: "skill_reference"`

                The type of the object. Always `skill_reference`.

                - `"skill_reference"`

              - `version: string`

                The concrete skill version installed for this session.

            - `HostedSkillResourceInline`

              A skill installed from an inline ZIP archive.

              - `description: string`

                The installed skill description.

              - `name: string`

                The installed skill name.

              - `type: "inline"`

                The type of the object. Always `inline`.

                - `"inline"`

          - `type: "openai_hosted"`

            The type of the object. Always `openai_hosted`.

            - `"openai_hosted"`

          - `container_size?: "small" | "medium" | "large" | null`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `"small"`

            - `"medium"`

            - `"large"`

        - `EnvironmentResourceSelfHosted`

          An environment hosted by the application.

          - `id: string`

            The public ID of the environment.

          - `capability_directories: Array<string>`

            Directories that contain capabilities exposed to the agent.

          - `remote_url: string`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `type: "self_hosted"`

            The type of the object. Always `self_hosted`.

            - `"self_hosted"`

          - `workspace_directory: string`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `error: string | null`

        The error that caused the session to fail, if any.

      - `last_active_at: number`

        The Unix timestamp, in seconds, when the session was last active.

      - `metadata: Record<string, string>`

        Custom string key-value pairs attached to the session.

      - `object: "agent.session"`

        The object type. Always `agent.session`.

        - `"agent.session"`

      - `required_actions: Array<SessionRequiredActionResourceComputerUseApprovalRequest | SessionRequiredActionResourceFunctionCall | SessionRequiredActionResourceEnvironmentConnection>`

        Actions that must be completed before the session can continue.

        - `SessionRequiredActionResourceComputerUseApprovalRequest`

          Respond to a computer-use request.

          - `request: ComputerUseApprovalRequestKindResourceBrowserAuthentication | ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

            The information needed to render the request.

            - `ComputerUseApprovalRequestKindResourceBrowserAuthentication`

              A registered form awaiting the application's response.

              - `credential_origin: string | null`

                The registered form or frame origin where values will be entered.

              - `fields: Array<Field>`

                Controls to render. All submitted values are sensitive.

                - `id: string`

                  The field ID to submit as field_id in a fields entry.

                - `label: string`

                  The label to display beside the control.

                - `required: boolean`

                  Whether this control requires a nonempty value.

                - `type: string`

                  The rendering type, such as email, password, or text.

              - `options: Array<Option>`

                Sign-in methods. Empty for a plain form.

                - `id: string`

                  The option ID to submit as selected_option.

                - `field_ids: Array<string>`

                  IDs from the registered fields that this method accepts.

                - `label: string`

                  The method label to display.

              - `reason: string | null`

                Why the agent needs the user to sign in.

              - `type: "browser_authentication"`

                The type of the object. Always `browser_authentication`.

                - `"browser_authentication"`

            - `ComputerUseApprovalRequestKindResourceBrowserOriginAccess`

              A browser origin awaiting the application's approval decision.

              - `origin: string`

                The origin the browser needs permission to access.

              - `reason: string | null`

                The browser's explanation for this request, or null when unavailable.

              - `type: "browser_origin_access"`

                The type of the object. Always `browser_origin_access`.

                - `"browser_origin_access"`

          - `request_id: string`

            The registered request ID to echo when responding.

          - `turn_id: string`

            The turn that requested approval.

          - `type: "computer_use_approval_request"`

            The type of the object. Always `computer_use_approval_request`.

            - `"computer_use_approval_request"`

        - `SessionRequiredActionResourceFunctionCall`

          Run a function tool and submit its result.

          - `arguments: unknown`

            The arguments supplied by the model.

          - `call_id: string`

            The ID to include when submitting the function result.

          - `name: string`

            The function name.

          - `turn_id: string`

            The ID of the turn that requested the function call.

          - `type: "function_call"`

            The type of the object. Always `function_call`.

            - `"function_call"`

        - `SessionRequiredActionResourceEnvironmentConnection`

          Reconnect a session environment.

          - `environment_id: string`

            The ID of the environment to reconnect.

          - `type: "environment_connection"`

            The type of the object. Always `environment_connection`.

            - `"environment_connection"`

      - `status: "idle" | "in_progress" | "requires_action" | "failed"`

        The current status of the session.

        - `"idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `"in_progress"`

          The session is processing a turn.

        - `"requires_action"`

          The session is waiting for one or more required actions.

        - `"failed"`

          The session failed.

      - `usage: TokenUsage | null`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `input_tokens: number`

          The number of input tokens used by the agent.

        - `input_tokens_details: InputTokensDetails`

          A breakdown of the agent's input token usage.

          - `cached_tokens: number`

            The number of input tokens retrieved from the prompt cache.

        - `output_tokens: number`

          The number of output tokens generated by the agent.

        - `output_tokens_details: OutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `reasoning_tokens: number`

            The number of output tokens used for reasoning.

        - `total_tokens: number`

          The total number of input and output tokens used by the agent.

      - `vault_ids: Array<string>`

        The IDs of vaults made available to the session.

    - `type: "agent.session.created"`

      The type of the object. Always `agent.session.created`.

      - `"agent.session.created"`

  - `AgentSessionTurnCreatedEvent`

    Emitted when a turn is created.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it was created.

      - `id: string`

        The ID of the turn.

      - `agent_id: string`

        The ID of the agent that ran the turn.

      - `completed_at: number | null`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `created_at: number`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `error: SessionTurnError | null`

        A customer-safe error. Non-null only for a failed turn.

        - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

        - `message: string`

          A customer-safe explanation of the failure.

      - `object: "agent.session.turn"`

        The object type. Always `agent.session.turn`.

        - `"agent.session.turn"`

      - `session_id: string`

        The ID of the session that owns the turn.

      - `started_at: number | null`

        The Unix timestamp, in seconds, when the turn started.

      - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

      - `subagent_id: string | null`

        The ID of the subagent that ran the turn, if applicable.

      - `usage: TokenUsage | null`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.created"`

      The type of the object. Always `agent.session.turn.created`.

      - `"agent.session.turn.created"`

  - `AgentSessionTurnInProgressEvent`

    Emitted when a turn starts running.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The turn at the time it started running.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.in_progress"`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `"agent.session.turn.in_progress"`

  - `AgentSessionTurnCompletedEvent`

    Emitted when a turn completes.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The completed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.completed"`

      The type of the object. Always `agent.session.turn.completed`.

      - `"agent.session.turn.completed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnFailedEvent`

    Emitted when a turn fails.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The failed turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.failed"`

      The type of the object. Always `agent.session.turn.failed`.

      - `"agent.session.turn.failed"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnCancelledEvent`

    Emitted when a turn is cancelled.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn: Turn`

      The cancelled turn.

    - `turn_id: string`

      The ID of the turn associated with the event.

    - `type: "agent.session.turn.cancelled"`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `"agent.session.turn.cancelled"`

    - `usage: TokenUsage | null`

      Token usage by the root agent during the turn, when available.

  - `AgentSessionTurnItemAddedEvent`

    Emitted when an item is added to a turn.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentSessionItem`

      The item that was added.

      - `AgentSessionMessage`

        A user or assistant message recorded in a session.

        - `id: string | null`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `content: Array<AgentSessionMessageContent>`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `MessageContentResourceInputText`

            Text supplied by the user.

            - `text: string`

              The text supplied by the user.

            - `type: "input_text"`

              The type of the object. Always `input_text`.

              - `"input_text"`

          - `MessageContentResourceInputImage`

            An image supplied by the user.

            - `image_url: string`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `type: "input_image"`

              The type of the object. Always `input_image`.

              - `"input_image"`

          - `MessageContentResourceOutputText`

            Text produced by the assistant.

            - `text: string`

              The text produced by the assistant.

            - `type: "output_text"`

              The type of the object. Always `output_text`.

              - `"output_text"`

        - `phase: "commentary" | "final_answer" | null`

          The phase of an assistant message. Null for user messages.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "user" | "assistant"`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

        - `id: string`

          The ID of the reasoning item.

        - `status: AgentOutputItemStatus | null`

          The status of the reasoning item.

        - `summary: Array<SummaryText>`

          The reasoning summaries produced by the agent.

          - `text: string`

            The reasoning summary text.

          - `type: "summary_text"`

            The content type. Always `summary_text`.

            - `"summary_text"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "reasoning"`

          The item type. Always `reasoning`.

          - `"reasoning"`

      - `AgentFunctionCallItem`

        A function call produced by the agent.

        - `id: string`

          The ID of the function call item.

        - `arguments: unknown`

          The arguments to pass to the function.

        - `call_id: string`

          The ID used to submit the function result.

        - `name: string`

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

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call"`

          The item type. Always `function_call`.

          - `"function_call"`

      - `FunctionCallOutputItemResource`

        The result supplied for a function call.

        - `id: string`

          The ID of the function call output item.

        - `call_id: string`

          The ID of the function call that produced this output.

        - `error: string | null`

          The error message, if the call failed.

        - `output: AgentFunctionCallOutput | null`

          The function result, if the call succeeded.

          - `string`

          - `Array<InputContent>`

            - `InputContentResourceInputText`

              Text input recorded in a session item.

              - `text: string`

                The text supplied to the agent.

              - `type: "input_text"`

                The type of the object. Always `input_text`.

                - `"input_text"`

            - `InputContentResourceInputImage`

              Image input recorded in a session item.

              - `image_url: string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `type: "input_image"`

                The type of the object. Always `input_image`.

                - `"input_image"`

        - `status: AgentFunctionCallStatus`

          The status of the function call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "function_call_output"`

          The item type. Always `function_call_output`.

          - `"function_call_output"`

      - `AgentMessageItemResource`

        A message exchanged between agent threads.

        - `id: string`

          The ID of the message.

        - `content: Array<AgentContent>`

          The content exchanged between the agents.

          - `OutputText`

            A text content part produced by the agent.

            - `text: string`

              The text produced by the agent.

            - `type: "output_text"`

              The content type. Always `output_text`.

              - `"output_text"`

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

            - `encrypted_content: string`

              The encrypted content payload.

            - `type: "encrypted_content"`

              The content type. Always `encrypted_content`.

              - `"encrypted_content"`

        - `recipient_agent_id: string`

          The ID or name of the receiving agent.

        - `sender_agent_id: string`

          The ID or name of the sending agent.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "agent_message"`

          The item type. Always `agent_message`.

          - `"agent_message"`

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

        - `id: string`

          The ID of the MCP call item.

        - `arguments: unknown`

          The arguments passed to the MCP tool.

        - `error: unknown`

          The error returned by the MCP tool, if any.

        - `name: string`

          The name of the MCP tool.

        - `output: unknown`

          The output returned by the MCP tool, if any.

        - `server_label: string`

          The label of the MCP server.

        - `status: AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "mcp_call"`

          The item type. Always `mcp_call`.

          - `"mcp_call"`

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `ComputerUseApprovalRequestResultItemResource`

        A credential-free record of an admitted response, not proof of completion.

        - `id: string`

          The stable history item ID.

        - `request_id: string`

          The registered request answered by this item.

        - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

          The admitted response, without submitted credential values.

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

            - `action: "submit"`

              - `"submit"`

            - `selected_option: string | null`

              The chosen sign-in method, or null when no options were offered.

            - `type: "browser_authentication"`

              - `"browser_authentication"`

          - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

            - `action: "cancel"`

              - `"cancel"`

            - `type: "browser_authentication"`

              - `"browser_authentication"`

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_approval_request_result"`

          - `"computer_use_approval_request_result"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

        - `id: string`

          The ID of the web search call.

        - `action: WebSearchAction | null`

          The action performed by the web search tool.

          - `WebSearchActionResourceSearch`

            A search query or group of search queries.

            - `queries: Array<string> | null`

              The search queries, when multiple queries were used.

            - `query: string | null`

              The search query, when a single query was used.

            - `type: "search"`

              The type of the object. Always `search`.

              - `"search"`

          - `WebSearchActionResourceOpenPage`

            Opens a web page.

            - `type: "open_page"`

              The type of the object. Always `open_page`.

              - `"open_page"`

            - `url: string | null`

              The URL of the page that was opened.

          - `WebSearchActionResourceFindInPage`

            Finds text within a web page.

            - `pattern: string | null`

              The text pattern that was searched for.

            - `type: "find_in_page"`

              The type of the object. Always `find_in_page`.

              - `"find_in_page"`

            - `url: string | null`

              The URL of the page that was searched.

          - `WebSearchActionResourceOther`

            Another web search action.

            - `type: "other"`

              The type of the object. Always `other`.

              - `"other"`

        - `status: AgentOutputItemStatus`

          The status of the web search call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "web_search_call"`

          The item type. Always `web_search_call`.

          - `"web_search_call"`

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

        - `id: string`

          The ID of the command execution item.

        - `command: string`

          The command that was executed.

        - `cwd: string | null`

          The working directory used to execute the command.

        - `duration_ms: number | null`

          The command duration in milliseconds.

        - `exit_code: number | null`

          The process exit code, if the command completed.

        - `output: string | null`

          The command output, if available.

        - `status: AgentFunctionCallStatus`

          The status of the command execution.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "command_execution"`

          The item type. Always `command_execution`.

          - `"command_execution"`

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

        - `id: string`

          The ID of the tool call item.

        - `agent_id: string`

          The ID of the agent that requested the subagent.

        - `content: Array<AgentContent>`

          The task given to the spawned agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `model: string | null`

          The model requested for the spawned agent.

        - `reasoning_effort: string | null`

          The reasoning effort requested for the spawned agent.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "create_subagent_call"`

          The item type. Always `create_subagent_call`.

          - `"create_subagent_call"`

            The current public item type.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

        - `id: string`

          The ID of the tool call item.

        - `content: Array<AgentContent>`

          The input sent to the receiving agent.

          - `OutputText`

            A text content part produced by the agent.

          - `EncryptedContentResource`

            Encrypted content exchanged between agents.

        - `recipient_agent_id: string`

          The ID of the agent receiving the input.

        - `sender_agent_id: string`

          The ID of the agent sending the input.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "send_subagent_input_call"`

          The item type. Always `send_subagent_input_call`.

          - `"send_subagent_input_call"`

            The current public item type.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to resume.

        - `sender_agent_id: string`

          The ID of the agent requesting the resume.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "resume_subagent_call"`

          The item type. Always `resume_subagent_call`.

          - `"resume_subagent_call"`

            The current public item type.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_ids: Array<string>`

          The IDs of the agents to wait for.

        - `sender_agent_id: string`

          The ID of the agent waiting for results.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "wait_for_subagents_call"`

          The item type. Always `wait_for_subagents_call`.

          - `"wait_for_subagents_call"`

            The current public item type.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to interrupt.

        - `sender_agent_id: string`

          The ID of the agent requesting the interrupt.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "interrupt_subagent_call"`

          The item type. Always `interrupt_subagent_call`.

          - `"interrupt_subagent_call"`

            The current public item type.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

        - `id: string`

          The ID of the tool call item.

        - `recipient_agent_id: string`

          The ID of the agent to close.

        - `sender_agent_id: string`

          The ID of the agent requesting the close.

        - `status: AgentFunctionCallStatus`

          The status of the tool call.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "close_subagent_call"`

          The item type. Always `close_subagent_call`.

          - `"close_subagent_call"`

            The current public item type.

    - `output_index: number | null`

      The index of the item in the turn output, when the item is agent output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.added"`

      The type of the object. Always `agent.session.turn.item.added`.

      - `"agent.session.turn.item.added"`

  - `AgentSessionIdleEvent`

    Emitted when a session becomes idle.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that became idle.

    - `type: "agent.session.idle"`

      The type of the object. Always `agent.session.idle`.

      - `"agent.session.idle"`

  - `AgentSessionInProgressEvent`

    Emitted when a session starts processing a turn.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session that started processing.

    - `type: "agent.session.in_progress"`

      The type of the object. Always `agent.session.in_progress`.

      - `"agent.session.in_progress"`

  - `AgentSessionRequiresActionEvent`

    Emitted when a session is waiting for one or more required actions.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The session and its current required actions.

    - `type: "agent.session.requires_action"`

      The type of the object. Always `agent.session.requires_action`.

      - `"agent.session.requires_action"`

  - `AgentSessionFailedEvent`

    Emitted when a session fails.

    - `event_id: string`

      The unique ID of the event.

    - `session: AgentSession`

      The failed session.

    - `type: "agent.session.failed"`

      The type of the object. Always `agent.session.failed`.

      - `"agent.session.failed"`

  - `AgentSessionEnvironmentPendingEvent`

    Emitted while a session environment is being prepared.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.pending"`

      The type of the object. Always `agent.session.environment.pending`.

      - `"agent.session.environment.pending"`

  - `AgentSessionEnvironmentConnectedEvent`

    Emitted when a session environment connects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.connected"`

      The type of the object. Always `agent.session.environment.connected`.

      - `"agent.session.environment.connected"`

  - `AgentSessionEnvironmentDisconnectedEvent`

    Emitted when a session environment disconnects.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.disconnected"`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `"agent.session.environment.disconnected"`

  - `AgentSessionEnvironmentFailedEvent`

    Emitted when a session environment fails.

    - `environment: AgentSessionEnvironmentState`

      The current environment state.

    - `event_id: string`

      The unique ID of the event.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.environment.failed"`

      The type of the object. Always `agent.session.environment.failed`.

      - `"agent.session.environment.failed"`

  - `AgentSessionSubagentCreatedEvent`

    Emitted when a subagent is created.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was created.

      - `id: string`

        The ID of the subagent.

      - `closed_at: number | null`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `instructions: Array<AgentContent> | null`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `OutputText`

          A text content part produced by the agent.

        - `EncryptedContentResource`

          Encrypted content exchanged between agents.

      - `name: string | null`

        The runner-assigned nickname, or null when unavailable.

      - `object: "agent.session.subagent"`

        The object type. Always `agent.session.subagent`.

        - `"agent.session.subagent"`

      - `opened_at: number`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `parent_agent_id: string`

        The ID of the agent that created this subagent.

      - `session_id: string`

        The ID of the session that owns the subagent.

      - `status: "active" | "closed"`

        The current status of the subagent.

        - `"active"`

          The subagent remains available, including while idle between turns.

        - `"closed"`

          The subagent is closed.

    - `type: "agent.session.subagent.created"`

      The type of the object. Always `agent.session.subagent.created`.

      - `"agent.session.subagent.created"`

  - `AgentSessionSubagentActiveEvent`

    Emitted when a closed subagent successfully resumes.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that resumed.

    - `type: "agent.session.subagent.active"`

      The type of the object. Always `agent.session.subagent.active`.

      - `"agent.session.subagent.active"`

  - `AgentSessionSubagentClosedEvent`

    Emitted when a subagent is closed.

    - `event_id: string`

      The unique ID of the event.

    - `subagent: Subagent`

      The subagent that was closed.

    - `type: "agent.session.subagent.closed"`

      The type of the object. Always `agent.session.subagent.closed`.

      - `"agent.session.subagent.closed"`

  - `AgentSessionTurnItemDoneEvent`

    Emitted when an output item is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item: AgentOutputItem`

      The completed output item.

      - `AgentSessionAssistantMessage`

        An assistant message produced by the agent.

        - `id: string`

          The ID of the message.

        - `content: Array<OutputText>`

          The content of the message.

          - `text: string`

            The text produced by the agent.

          - `type: "output_text"`

            The content type. Always `output_text`.

        - `phase: "commentary" | "final_answer" | null`

          The phase of the assistant message.

          - `"commentary"`

            Commentary produced while the agent works.

          - `"final_answer"`

            The agent's final answer.

        - `role: "assistant"`

          The role of the message author. Always `assistant`.

          - `"assistant"`

        - `status: AgentOutputItemStatus`

          The status of the message.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "message"`

          The item type. Always `message`.

          - `"message"`

      - `AgentReasoningItem`

        A reasoning item produced by the agent.

      - `AgentFunctionCallItem`

        A function call produced by the agent.

      - `AgentMcpCallItem`

        A call to a tool on an MCP server.

      - `ComputerUseCallItemResource`

        One execution of the platform-provided computer-use capability.

        - `id: string`

          The ID of the activity item.

        - `output: Output | null`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `image_url: string`

            The complete JPEG image as a base64 data URL.

          - `type: "computer_screenshot"`

            The content type. Always `computer_screenshot`.

            - `"computer_screenshot"`

        - `status: AgentFunctionCallStatus`

          The execution status of the activity.

        - `title: string | null`

          A model-generated description of the activity, when available.

        - `turn_id: string`

          The ID of the turn that contains this item.

        - `type: "computer_use_call"`

          The item type. Always `computer_use_call`.

          - `"computer_use_call"`

      - `BrowserAuthenticationRequestItemResource`

        A credential-free history record of the emitted login request.

        - `id: string`

          The stable history item ID.

        - `request: Request`

          A registered form awaiting the application's response.

          - `credential_origin: string | null`

            The registered form or frame origin where values will be entered.

          - `fields: Array<Field>`

            Controls to render. All submitted values are sensitive.

            - `id: string`

              The field ID to submit as field_id in a fields entry.

            - `label: string`

              The label to display beside the control.

            - `required: boolean`

              Whether this control requires a nonempty value.

            - `type: string`

              The rendering type, such as email, password, or text.

          - `options: Array<Option>`

            Sign-in methods. Empty for a plain form.

            - `id: string`

              The option ID to submit as selected_option.

            - `field_ids: Array<string>`

              IDs from the registered fields that this method accepts.

            - `label: string`

              The method label to display.

          - `reason: string | null`

            Why the agent needs the user to sign in.

          - `type: "browser_authentication"`

            The type of the object. Always `browser_authentication`.

            - `"browser_authentication"`

        - `request_id: string`

        - `turn_id: string`

        - `type: "computer_use_approval_request"`

          The item type. Always computer_use_approval_request.

          - `"computer_use_approval_request"`

      - `AgentWebSearchCallItem`

        A web search call produced by the agent.

      - `AgentCommandExecutionItem`

        A command execution produced by the agent.

      - `AgentCreateSubagentCallItem`

        A request to spawn a subagent.

      - `AgentSendSubagentInputCallItem`

        A request to send input to another agent.

      - `AgentResumeSubagentCallItem`

        A request to resume a subagent.

      - `AgentWaitForSubagentsCallItem`

        A request to wait for one or more subagents.

      - `AgentInterruptSubagentCallItem`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `AgentCloseSubagentCallItem`

        A request to close a subagent.

    - `output_index: number`

      The index of the output item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.item.done"`

      The type of the object. Always `agent.session.turn.item.done`.

      - `"agent.session.turn.item.done"`

  - `AgentSessionTurnContentPartAddedEvent`

    Emitted when an output text content part is added.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The initial content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.added"`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `"agent.session.turn.content_part.added"`

  - `AgentSessionTurnContentPartDoneEvent`

    Emitted when an output content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: OutputText`

      The completed content part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.content_part.done"`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `"agent.session.turn.content_part.done"`

  - `AgentSessionTurnOutputTextDeltaEvent`

    Emitted when text is appended to an output text content part.

    - `content_index: number`

      The index of the content part in the message.

    - `delta: string`

      The text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.delta"`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `"agent.session.turn.output_text.delta"`

  - `AgentSessionTurnOutputTextDoneEvent`

    Emitted when an output text content part is complete.

    - `content_index: number`

      The index of the content part in the message.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the message item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `text: string`

      The complete output text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.output_text.done"`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `"agent.session.turn.output_text.done"`

  - `AgentSessionTurnReasoningSummaryPartAddedEvent`

    Emitted when a reasoning summary content part is added.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The initial summary part.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.added"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `"agent.session.turn.reasoning_summary_part.added"`

  - `AgentSessionTurnReasoningSummaryPartDoneEvent`

    Emitted when a reasoning summary part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `part: SummaryText`

      The completed summary part.

    - `session_id: string`

      The ID of the session associated with the event.

    - `status: "incomplete" | null`

      Present as `incomplete` when summary generation was interrupted.

      - `"incomplete"`

    - `summary_index: number`

      The index of the summary part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_part.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `"agent.session.turn.reasoning_summary_part.done"`

  - `AgentSessionTurnReasoningSummaryTextDeltaEvent`

    Emitted when text is appended to a reasoning summary.

    - `delta: string`

      The summary text that was appended.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.delta"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `"agent.session.turn.reasoning_summary_text.delta"`

  - `AgentSessionTurnReasoningSummaryTextDoneEvent`

    Emitted when a reasoning summary content part is complete.

    - `event_id: string`

      The unique ID of the event.

    - `item_id: string`

      The ID of the reasoning item.

    - `output_index: number`

      The index of the item in the turn output.

    - `session_id: string`

      The ID of the session associated with the event.

    - `summary_index: number`

      The index of the summary content part.

    - `text: string`

      The complete reasoning summary text.

    - `turn_id: string | null`

      The ID of the turn associated with the event, when applicable.

    - `type: "agent.session.turn.reasoning_summary_text.done"`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `"agent.session.turn.reasoning_summary_text.done"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const agentSessionEvent = await client.beta.agents.sessions.events.stream('session_id');

console.log(agentSessionEvent);
```

# Items

## List agent session items

`client.beta.agents.sessions.items.list(stringsessionID, ItemListParamsquery?, RequestOptionsoptions?): CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `sessionID: string`

- `query: ItemListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: string | null`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

        - `type: "output_text"`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "user" | "assistant"`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

    - `call_id: string`

      The ID of the function call that produced this output.

    - `error: string | null`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

    - `sender_agent_id: string`

      The ID or name of the sending agent.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

    - `request_id: string`

      The registered request answered by this item.

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSessionItem of client.beta.agents.sessions.items.list('session_id')) {
  console.log(agentSessionItem);
}
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

`client.beta.agents.sessions.subagents.list(stringsessionID, SubagentListParamsquery?, RequestOptionsoptions?): CursorPage<Subagent>`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID: string`

- `query: SubagentListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `Subagent`

  A subagent created within a session.

  - `id: string`

    The ID of the subagent.

  - `closed_at: number | null`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array<AgentContent> | null`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: string | null`

    The runner-assigned nickname, or null when unavailable.

  - `object: "agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: number`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: string`

    The ID of the agent that created this subagent.

  - `session_id: string`

    The ID of the session that owns the subagent.

  - `status: "active" | "closed"`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const subagent of client.beta.agents.sessions.subagents.list('session_id')) {
  console.log(subagent.id);
}
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

`client.beta.agents.sessions.subagents.retrieve(stringsubagentID, SubagentRetrieveParamsparams, RequestOptionsoptions?): Subagent`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `subagentID: string`

- `params: SubagentRetrieveParams`

  - `session_id: string`

    The ID of the session.

### Returns

- `Subagent`

  A subagent created within a session.

  - `id: string`

    The ID of the subagent.

  - `closed_at: number | null`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `instructions: Array<AgentContent> | null`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `OutputText`

      A text content part produced by the agent.

      - `text: string`

        The text produced by the agent.

      - `type: "output_text"`

        The content type. Always `output_text`.

        - `"output_text"`

    - `EncryptedContentResource`

      Encrypted content exchanged between agents.

      - `encrypted_content: string`

        The encrypted content payload.

      - `type: "encrypted_content"`

        The content type. Always `encrypted_content`.

        - `"encrypted_content"`

  - `name: string | null`

    The runner-assigned nickname, or null when unavailable.

  - `object: "agent.session.subagent"`

    The object type. Always `agent.session.subagent`.

    - `"agent.session.subagent"`

  - `opened_at: number`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `parent_agent_id: string`

    The ID of the agent that created this subagent.

  - `session_id: string`

    The ID of the session that owns the subagent.

  - `status: "active" | "closed"`

    The current status of the subagent.

    - `"active"`

      The subagent remains available, including while idle between turns.

    - `"closed"`

      The subagent is closed.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const subagent = await client.beta.agents.sessions.subagents.retrieve('subagent_id', {
  session_id: 'session_id',
});

console.log(subagent.id);
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

`client.beta.agents.sessions.subagents.items.list(stringsubagentID, ItemListParamsparams, RequestOptionsoptions?): CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `subagentID: string`

- `params: ItemListParams`

  - `session_id: string`

    Path param: The ID of the session.

  - `after?: string`

    Query param: Return resources after this resource ID in the selected order.

  - `limit?: number`

    Query param: The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    Query param: The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: string | null`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

        - `type: "output_text"`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "user" | "assistant"`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

    - `call_id: string`

      The ID of the function call that produced this output.

    - `error: string | null`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

    - `sender_agent_id: string`

      The ID or name of the sending agent.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

    - `request_id: string`

      The registered request answered by this item.

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSessionItem of client.beta.agents.sessions.subagents.items.list(
  'subagent_id',
  { session_id: 'session_id' },
)) {
  console.log(agentSessionItem);
}
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

`client.beta.agents.sessions.subagents.turns.list(stringsubagentID, TurnListParamsparams, RequestOptionsoptions?): CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `subagentID: string`

- `params: TurnListParams`

  - `session_id: string`

    Path param: The ID of the session.

  - `after?: string`

    Query param: Return resources after this resource ID in the selected order.

  - `limit?: number`

    Query param: The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    Query param: The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `Turn`

  The canonical public representation of a session turn.

  - `id: string`

    The ID of the turn.

  - `agent_id: string`

    The ID of the agent that ran the turn.

  - `completed_at: number | null`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: number`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError | null`

    A customer-safe error. Non-null only for a failed turn.

    - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

    - `message: string`

      A customer-safe explanation of the failure.

  - `object: "agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: string`

    The ID of the session that owns the turn.

  - `started_at: number | null`

    The Unix timestamp, in seconds, when the turn started.

  - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

  - `subagent_id: string | null`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage | null`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const turn of client.beta.agents.sessions.subagents.turns.list('subagent_id', {
  session_id: 'session_id',
})) {
  console.log(turn.id);
}
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

`client.beta.agents.sessions.subagents.turns.retrieve(stringturnID, TurnRetrieveParamsparams, RequestOptionsoptions?): Turn`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `turnID: string`

- `params: TurnRetrieveParams`

  - `session_id: string`

    The ID of the session.

  - `subagent_id: string`

    The ID of the subagent in this session.

### Returns

- `Turn`

  The canonical public representation of a session turn.

  - `id: string`

    The ID of the turn.

  - `agent_id: string`

    The ID of the agent that ran the turn.

  - `completed_at: number | null`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: number`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError | null`

    A customer-safe error. Non-null only for a failed turn.

    - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

    - `message: string`

      A customer-safe explanation of the failure.

  - `object: "agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: string`

    The ID of the session that owns the turn.

  - `started_at: number | null`

    The Unix timestamp, in seconds, when the turn started.

  - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

  - `subagent_id: string | null`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage | null`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const turn = await client.beta.agents.sessions.subagents.turns.retrieve('turn_id', {
  session_id: 'session_id',
  subagent_id: 'subagent_id',
});

console.log(turn.id);
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

`client.beta.agents.sessions.subagents.turns.items.list(stringturnID, ItemListParamsparams, RequestOptionsoptions?): CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `turnID: string`

- `params: ItemListParams`

  - `session_id: string`

    Path param: The ID of the session.

  - `subagent_id: string`

    Path param: The ID of the subagent in this session.

  - `after?: string`

    Query param: Return resources after this resource ID in the selected order.

  - `limit?: number`

    Query param: The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    Query param: The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: string | null`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

        - `type: "output_text"`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "user" | "assistant"`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

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

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

    - `call_id: string`

      The ID of the function call that produced this output.

    - `error: string | null`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

    - `sender_agent_id: string`

      The ID or name of the sending agent.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

    - `request_id: string`

      The registered request answered by this item.

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSessionItem of client.beta.agents.sessions.subagents.turns.items.list(
  'turn_id',
  { session_id: 'session_id', subagent_id: 'subagent_id' },
)) {
  console.log(agentSessionItem);
}
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

`client.beta.agents.sessions.turns.list(stringsessionID, TurnListParamsquery?, RequestOptionsoptions?): CursorPage<Turn>`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `sessionID: string`

- `query: TurnListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `order?: "asc" | "desc"`

    The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `Turn`

  The canonical public representation of a session turn.

  - `id: string`

    The ID of the turn.

  - `agent_id: string`

    The ID of the agent that ran the turn.

  - `completed_at: number | null`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: number`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError | null`

    A customer-safe error. Non-null only for a failed turn.

    - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

    - `message: string`

      A customer-safe explanation of the failure.

  - `object: "agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: string`

    The ID of the session that owns the turn.

  - `started_at: number | null`

    The Unix timestamp, in seconds, when the turn started.

  - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

  - `subagent_id: string | null`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage | null`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const turn of client.beta.agents.sessions.turns.list('session_id')) {
  console.log(turn.id);
}
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

`client.beta.agents.sessions.turns.retrieve(stringturnID, TurnRetrieveParamsparams, RequestOptionsoptions?): Turn`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `turnID: string`

- `params: TurnRetrieveParams`

  - `session_id: string`

    The ID of the session that owns the turn.

### Returns

- `Turn`

  The canonical public representation of a session turn.

  - `id: string`

    The ID of the turn.

  - `agent_id: string`

    The ID of the agent that ran the turn.

  - `completed_at: number | null`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: number`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError | null`

    A customer-safe error. Non-null only for a failed turn.

    - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

    - `message: string`

      A customer-safe explanation of the failure.

  - `object: "agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: string`

    The ID of the session that owns the turn.

  - `started_at: number | null`

    The Unix timestamp, in seconds, when the turn started.

  - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

  - `subagent_id: string | null`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage | null`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const turn = await client.beta.agents.sessions.turns.retrieve('turn_id', {
  session_id: 'session_id',
});

console.log(turn.id);
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

- `Turn`

  The canonical public representation of a session turn.

  - `id: string`

    The ID of the turn.

  - `agent_id: string`

    The ID of the agent that ran the turn.

  - `completed_at: number | null`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `created_at: number`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `error: SessionTurnError | null`

    A customer-safe error. Non-null only for a failed turn.

    - `code: "context_length_exceeded" | "session_budget_exceeded" | "usage_limit_exceeded" | 16 more`

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

    - `message: string`

      A customer-safe explanation of the failure.

  - `object: "agent.session.turn"`

    The object type. Always `agent.session.turn`.

    - `"agent.session.turn"`

  - `session_id: string`

    The ID of the session that owns the turn.

  - `started_at: number | null`

    The Unix timestamp, in seconds, when the turn started.

  - `status: "queued" | "in_progress" | "waiting" | 3 more`

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

  - `subagent_id: string | null`

    The ID of the subagent that ran the turn, if applicable.

  - `usage: TokenUsage | null`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `input_tokens: number`

      The number of input tokens used by the agent.

    - `input_tokens_details: InputTokensDetails`

      A breakdown of the agent's input token usage.

      - `cached_tokens: number`

        The number of input tokens retrieved from the prompt cache.

    - `output_tokens: number`

      The number of output tokens generated by the agent.

    - `output_tokens_details: OutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `reasoning_tokens: number`

        The number of output tokens used for reasoning.

    - `total_tokens: number`

      The total number of input and output tokens used by the agent.

# Vaults

## Create a vault

`client.beta.agents.vaults.create(VaultCreateParamsbody?, RequestOptionsoptions?): Vault`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `body: VaultCreateParams`

  - `metadata?: Record<string, string> | null`

    Key-value pairs to associate with the vault, such as an application or team identifier.

  - `name?: string`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vault = await client.beta.agents.vaults.create();

console.log(vault.id);
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

`client.beta.agents.vaults.delete(stringvaultID, RequestOptionsoptions?): VaultDeleted`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

### Returns

- `VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: string`

    The ID of the deleted vault.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.deleted"`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vaultDeleted = await client.beta.agents.vaults.delete('vault_id');

console.log(vaultDeleted.id);
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

`client.beta.agents.vaults.list(VaultListParamsquery?, RequestOptionsoptions?): CursorPage<Vault>`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `query: VaultListParams`

  - `after?: string`

    Return resources after this resource ID in the selected order.

  - `limit?: number | null`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `order?: "asc" | "desc"`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

  - `status?: VaultStatusFilter`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `VaultStatus = "active" | "archived"`

      Whether a vault or credential is active or archived.

      - `"active"`

      - `"archived"`

    - `Array<VaultStatus>`

      - `"active"`

      - `"archived"`

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const vault of client.beta.agents.vaults.list()) {
  console.log(vault.id);
}
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

`client.beta.agents.vaults.retrieve(stringvaultID, RequestOptionsoptions?): Vault`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

### Returns

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

const vault = await client.beta.agents.vaults.retrieve('vault_id');

console.log(vault.id);
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

- `Vault`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `id: string`

    The ID of the vault.

  - `created_at: number`

    The Unix timestamp, in seconds, when the vault was created.

  - `metadata: Record<string, string>`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `name: string | null`

    The human-readable name of the vault, if set.

  - `object: "vault"`

    The object type. Always `vault`.

    - `"vault"`

### Vault Deleted

- `VaultDeleted`

  Confirmation that a vault was deleted.

  - `id: string`

    The ID of the deleted vault.

  - `deleted: boolean`

    Whether the resource was deleted. Always `true`.

  - `object: "vault.deleted"`

    The object type. Always `vault.deleted`.

    - `"vault.deleted"`

### Vault Status

- `VaultStatus = "active" | "archived"`

  Whether a vault or credential is active or archived.

  - `"active"`

  - `"archived"`

### Vault Status Filter

- `VaultStatusFilter = VaultStatus | Array<VaultStatus>`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `VaultStatus = "active" | "archived"`

    Whether a vault or credential is active or archived.

    - `"active"`

    - `"archived"`

  - `Array<VaultStatus>`

    - `"active"`

    - `"archived"`

# Credentials

## Create a vault credential

`client.beta.agents.vaults.credentials.create(stringvaultID, CredentialCreateParamsbody, RequestOptionsoptions?): Credential`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `vaultID: string`

- `body: CredentialCreateParams`

  - `auth: CredentialAuthCreateParam`

    The authentication method and write-only secret values to store.

    - `CreateVaultCredentialAuthParamMcpOauth`

      An OAuth credential for an HTTPS MCP destination.

      - `access_token: string`

        A write-only OAuth access token; never returned by credential resources.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "mcp_oauth"`

        The type of the object. Always `mcp_oauth`.

        - `"mcp_oauth"`

      - `expires_at?: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `refresh?: Refresh | null`

        Optional refresh configuration for an HTTPS OAuth token endpoint.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `refresh_token: string`

          The refresh token to store. This secret is never returned in credential resources.

        - `token_endpoint: string`

          The HTTPS OAuth token endpoint used to exchange the refresh token for a new access token.

        - `token_endpoint_auth: McpOauthTokenEndpointAuthCreateParam`

          How the OAuth client authenticates to the token endpoint.

          - `CreateMcpOauthTokenEndpointAuthParamNone`

            Sends the client ID without a client secret.

            - `type: "none"`

              The type of the object. Always `none`.

              - `"none"`

          - `CreateMcpOauthTokenEndpointAuthParamClientSecretBasic`

            Sends the client ID and secret using HTTP Basic authentication.

            - `client_secret: string`

              The OAuth client secret to store. Never returned in credential resources.

            - `type: "client_secret_basic"`

              The type of the object. Always `client_secret_basic`.

              - `"client_secret_basic"`

          - `CreateMcpOauthTokenEndpointAuthParamClientSecretPost`

            Sends the client ID and secret in the token request body.

            - `client_secret: string`

              The OAuth client secret to store. Never returned in credential resources.

            - `type: "client_secret_post"`

              The type of the object. Always `client_secret_post`.

              - `"client_secret_post"`

        - `resource?: string | null`

          The resource URI to send to the OAuth token endpoint during refresh, if required.

        - `scope?: string | null`

          Space-separated OAuth scopes to request during refresh, if required.

    - `CreateVaultCredentialAuthParamStaticBearer`

      A bearer token for an MCP server, without automatic OAuth refresh.

      - `token: string`

        The bearer token to store. This secret is never returned in credential resources.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `type: "static_bearer"`

        The type of the object. Always `static_bearer`.

        - `"static_bearer"`

    - `CreateVaultCredentialAuthParamEnvironmentVariable`

      An HTTP credential for OpenAI-hosted environments only. The sandbox receives an environment variable containing a placeholder, not the secret. Use the placeholder unchanged in outgoing requests. The egress proxy replaces the placeholder with the secret for allowed HTTPS destinations on ports 443 and 8443. Sandbox code cannot read the real secret or use it for local computation, such as signing a request.

      - `networking: CredentialNetworkingParam`

        The destinations where the proxy can substitute this secret. The environment network policy must also allow them.

        - `VaultCredentialNetworkingParamUnrestricted`

          Allows substitution for destinations permitted by the environment network policy. Requires `environment.network.access` to be `restricted`, with explicit `allowed_domains`.

          - `type: "unrestricted"`

            The type of the object. Always `unrestricted`.

            - `"unrestricted"`

        - `VaultCredentialNetworkingParamLimited`

          Allows substitution only for the listed hosts. The environment network policy must also allow these hosts.

          - `allowed_hosts: Array<string>`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `type: "limited"`

            The type of the object. Always `limited`.

            - `"limited"`

      - `secret_name: string`

        The environment variable name that receives the placeholder, such as `SERVICE_API_KEY`. Use ASCII letters, digits, and underscores, starting with a letter or underscore. Names starting with `CODEX_` and managed proxy or certificate variable names are reserved.

      - `secret_value: string`

        The write-only secret to store. Never returned in credential resources or supplied directly to sandbox code. Must be nonempty and must not contain carriage returns, newlines, or NUL bytes.

      - `type: "environment_variable"`

        The type of the object. Always `environment_variable`.

        - `"environment_variable"`

  - `name: string`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  - `metadata?: Record<string, string>`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `Credential`

  Metadata for a stored credential. Secret values are never returned.

  - `id: string`

    The ID of the credential.

  - `auth: CredentialAuth`

    The authentication method and non-secret configuration of the credential.

    - `VaultCredentialAuthResourceMcpOauth`

      Public metadata for an OAuth credential; tokens and client secrets are never returned.

      - `expires_at: string | null`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `mcp_server_url: string`

        The HTTPS MCP server URL authorized by this credential.

      - `refresh: Refresh | null`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `client_id: string`

          The OAuth client ID used when requesting a new access token.

        - `resource: string | null`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.
