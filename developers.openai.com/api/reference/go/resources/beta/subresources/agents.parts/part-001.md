<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

# Agents

## Create an agent

`client.Beta.Agents.New(ctx, body) (*Agent, error)`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `body BetaAgentNewParams`

  - `Model param.Field[string]`

    The model to use for the agent. The requested model name is preserved.

  - `Instructions param.Field[string]`

    Additional instructions appended to the agent's default base instructions. Omit or set to null to add no custom instructions.

  - `Metadata param.Field[map[string, string]]`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

  - `MultiAgent param.Field[MultiAgentConfigParamResp]`

    Configuration for creating and coordinating subagents. Subagent tools are disabled by default.

  - `Name param.Field[string]`

    A human-readable name for the agent. Omission or null leaves the agent unnamed.

  - `Reasoning param.Field[AgentReasoningParamResp]`

    Configuration for model reasoning. Omission uses the model's default effort.

  - `ServiceTier param.Field[BetaAgentNewParamsServiceTier]`

    The service tier used for model requests. Defaults to `auto`.

    - `const BetaAgentNewParamsServiceTierAuto BetaAgentNewParamsServiceTier = "auto"`

      Selects the service tier automatically.

    - `const BetaAgentNewParamsServiceTierDefault BetaAgentNewParamsServiceTier = "default"`

      Uses the default service tier.

    - `const BetaAgentNewParamsServiceTierFlex BetaAgentNewParamsServiceTier = "flex"`

      Uses the flex service tier.

    - `const BetaAgentNewParamsServiceTierPriority BetaAgentNewParamsServiceTier = "priority"`

      Uses the priority service tier.

    - `const BetaAgentNewParamsServiceTierFast BetaAgentNewParamsServiceTier = "fast"`

      Uses the fast service tier.

    - `const BetaAgentNewParamsServiceTierUltrafast BetaAgentNewParamsServiceTier = "ultrafast"`

      Uses the ultrafast service tier.

  - `Text param.Field[AgentTextParamResp]`

    Configuration for generated text. Defaults to the `text` format and medium verbosity.

  - `Tools param.Field[[]PersistedAgentToolParamUnionResp]`

    Tools available to the agent. Defaults to an empty list.

    - `PersistedAgentToolParamFunctionResp`

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

      - `DeferLoading bool`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `PersistedAgentToolParamToolSearchResp`

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `PersistedAgentToolParamProgrammaticToolCallingResp`

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `Enabled bool`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `PersistedAgentToolParamMcpResp`

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportParamUnionResp`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportParamHTTPResp`

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

        - `PersistedMcpTransportParamStdioResp`

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

          - `Args []string`

            Arguments passed to the MCP server command.

          - `EnvVars []string`

            Environment variable names to inherit from the selected execution environment.

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

      - `AllowedTools []string`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `ConnectionOrigin string`

        Selects where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolParamMcpConnectionOriginService PersistedAgentToolParamMcpConnectionOrigin = "service"`

          Uses the Managed Agents service network.

        - `const PersistedAgentToolParamMcpConnectionOriginEnvironment PersistedAgentToolParamMcpConnectionOrigin = "environment"`

          Uses the session's execution environment.

      - `CredentialID string`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `PersistedAgentToolParamWebSearchResp`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

      - `AllowedDomains []string`

        Domains the search may include.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolParamWebSearchContextSizeLow PersistedAgentToolParamWebSearchContextSize = "low"`

        - `const PersistedAgentToolParamWebSearchContextSizeMedium PersistedAgentToolParamWebSearchContextSize = "medium"`

        - `const PersistedAgentToolParamWebSearchContextSizeHigh PersistedAgentToolParamWebSearchContextSize = "high"`

      - `Location PersistedAgentToolParamWebSearchLocationResp`

        Approximate location used to localize search results.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results. Defaults to `live`.

        - `const PersistedAgentToolParamWebSearchModeDisabled PersistedAgentToolParamWebSearchMode = "disabled"`

          Disables web search.

        - `const PersistedAgentToolParamWebSearchModeCached PersistedAgentToolParamWebSearchMode = "cached"`

          Uses cached search results.

        - `const PersistedAgentToolParamWebSearchModeLive PersistedAgentToolParamWebSearchMode = "live"`

          Searches the live web.

    - `PersistedAgentToolParamComputerUseResp`

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `type Agent struct{…}`

  A reusable agent scoped to the caller's project.

  - `ID string`

    The ID of the reusable agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the agent was created.

  - `Instructions string`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the agent.

  - `Model string`

    The requested model name used for inference.

  - `MultiAgent MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Name string`

    A human-readable name for the agent, or null if it is unnamed.

  - `Object Agent`

    The object type. Always `agent`.

    - `const AgentAgent Agent = "agent"`

  - `Reasoning AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AgentServiceTier`

    The resolved service-tier policy used for model requests.

    - `const AgentServiceTierAuto AgentServiceTier = "auto"`

    - `const AgentServiceTierDefault AgentServiceTier = "default"`

    - `const AgentServiceTierFlex AgentServiceTier = "flex"`

    - `const AgentServiceTierPriority AgentServiceTier = "priority"`

    - `const AgentServiceTierFast AgentServiceTier = "fast"`

    - `const AgentServiceTierUltrafast AgentServiceTier = "ultrafast"`

  - `Text AgentText`

    The resolved configuration for text generated by the agent.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []PersistedAgentToolUnion`

    Tools available to the agent.

    - `type PersistedAgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

    - `type PersistedAgentToolToolSearch struct{…}`

      Discovers deferred function tools and loads them into the model context.

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type PersistedAgentToolMcp struct{…}`

      Tools provided by a remote MCP server without stored credentials.

      - `AllowedTools []string`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

        - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportUnion`

        The credential-free transport used to connect to the MCP server.

        - `type PersistedMcpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type PersistedMcpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type PersistedAgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

        - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

        - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

      - `Location PersistedAgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results.

        - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

        - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

        - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type PersistedAgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agent, err := client.Beta.Agents.New(context.TODO(), openai.BetaAgentNewParams{
    Model: "model",
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agent.ID)
}
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

`client.Beta.Agents.Delete(ctx, agentID) (*AgentDeleted, error)`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID string`

### Returns

- `type AgentDeleted struct{…}`

  A deleted reusable agent.

  - `ID string`

    The ID of the deleted agent.

  - `Deleted bool`

    Whether the agent was deleted. Always `true`.

  - `Object AgentDeleted`

    The object type. Always `agent.deleted`.

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agentDeleted, err := client.Beta.Agents.Delete(context.TODO(), "agent_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentDeleted.ID)
}
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

`client.Beta.Agents.List(ctx, query) (*CursorPage[Agent], error)`

**get** `/agents`

Lists reusable agents in the current project. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `query BetaAgentListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return.

  - `Order param.Field[BetaAgentListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentListParamsOrderAsc BetaAgentListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentListParamsOrderDesc BetaAgentListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type Agent struct{…}`

  A reusable agent scoped to the caller's project.

  - `ID string`

    The ID of the reusable agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the agent was created.

  - `Instructions string`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the agent.

  - `Model string`

    The requested model name used for inference.

  - `MultiAgent MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Name string`

    A human-readable name for the agent, or null if it is unnamed.

  - `Object Agent`

    The object type. Always `agent`.

    - `const AgentAgent Agent = "agent"`

  - `Reasoning AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AgentServiceTier`

    The resolved service-tier policy used for model requests.

    - `const AgentServiceTierAuto AgentServiceTier = "auto"`

    - `const AgentServiceTierDefault AgentServiceTier = "default"`

    - `const AgentServiceTierFlex AgentServiceTier = "flex"`

    - `const AgentServiceTierPriority AgentServiceTier = "priority"`

    - `const AgentServiceTierFast AgentServiceTier = "fast"`

    - `const AgentServiceTierUltrafast AgentServiceTier = "ultrafast"`

  - `Text AgentText`

    The resolved configuration for text generated by the agent.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []PersistedAgentToolUnion`

    Tools available to the agent.

    - `type PersistedAgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

    - `type PersistedAgentToolToolSearch struct{…}`

      Discovers deferred function tools and loads them into the model context.

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type PersistedAgentToolMcp struct{…}`

      Tools provided by a remote MCP server without stored credentials.

      - `AllowedTools []string`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

        - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportUnion`

        The credential-free transport used to connect to the MCP server.

        - `type PersistedMcpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type PersistedMcpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type PersistedAgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

        - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

        - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

      - `Location PersistedAgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results.

        - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

        - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

        - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type PersistedAgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.List(context.TODO(), openai.BetaAgentListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Get(ctx, agentID) (*Agent, error)`

**get** `/agents/{agent_id}`

Retrieves a reusable agent by ID. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID string`

### Returns

- `type Agent struct{…}`

  A reusable agent scoped to the caller's project.

  - `ID string`

    The ID of the reusable agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the agent was created.

  - `Instructions string`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the agent.

  - `Model string`

    The requested model name used for inference.

  - `MultiAgent MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Name string`

    A human-readable name for the agent, or null if it is unnamed.

  - `Object Agent`

    The object type. Always `agent`.

    - `const AgentAgent Agent = "agent"`

  - `Reasoning AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AgentServiceTier`

    The resolved service-tier policy used for model requests.

    - `const AgentServiceTierAuto AgentServiceTier = "auto"`

    - `const AgentServiceTierDefault AgentServiceTier = "default"`

    - `const AgentServiceTierFlex AgentServiceTier = "flex"`

    - `const AgentServiceTierPriority AgentServiceTier = "priority"`

    - `const AgentServiceTierFast AgentServiceTier = "fast"`

    - `const AgentServiceTierUltrafast AgentServiceTier = "ultrafast"`

  - `Text AgentText`

    The resolved configuration for text generated by the agent.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []PersistedAgentToolUnion`

    Tools available to the agent.

    - `type PersistedAgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

    - `type PersistedAgentToolToolSearch struct{…}`

      Discovers deferred function tools and loads them into the model context.

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type PersistedAgentToolMcp struct{…}`

      Tools provided by a remote MCP server without stored credentials.

      - `AllowedTools []string`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

        - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportUnion`

        The credential-free transport used to connect to the MCP server.

        - `type PersistedMcpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type PersistedMcpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type PersistedAgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

        - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

        - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

      - `Location PersistedAgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results.

        - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

        - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

        - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type PersistedAgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agent, err := client.Beta.Agents.Get(context.TODO(), "agent_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agent.ID)
}
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

`client.Beta.Agents.Update(ctx, agentID, body) (*Agent, error)`

**post** `/agents/{agent_id}`

Updates a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `agentID string`

- `body BetaAgentUpdateParams`

  - `Instructions param.Field[string]`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `Model param.Field[string]`

    The model to use for the agent. The requested model name is preserved.

  - `MultiAgent param.Field[MultiAgentConfigParamResp]`

    Configuration for creating and coordinating subagents.

  - `Name param.Field[string]`

    A replacement name. Omit to leave unchanged, or pass null to clear it.

  - `Reasoning param.Field[AgentReasoningParamResp]`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

  - `ServiceTier param.Field[BetaAgentUpdateParamsServiceTier]`

    The service tier used for model requests.

    - `const BetaAgentUpdateParamsServiceTierAuto BetaAgentUpdateParamsServiceTier = "auto"`

      Selects the service tier automatically.

    - `const BetaAgentUpdateParamsServiceTierDefault BetaAgentUpdateParamsServiceTier = "default"`

      Uses the default service tier.

    - `const BetaAgentUpdateParamsServiceTierFlex BetaAgentUpdateParamsServiceTier = "flex"`

      Uses the flex service tier.

    - `const BetaAgentUpdateParamsServiceTierPriority BetaAgentUpdateParamsServiceTier = "priority"`

      Uses the priority service tier.

    - `const BetaAgentUpdateParamsServiceTierFast BetaAgentUpdateParamsServiceTier = "fast"`

      Uses the fast service tier.

    - `const BetaAgentUpdateParamsServiceTierUltrafast BetaAgentUpdateParamsServiceTier = "ultrafast"`

      Uses the ultrafast service tier.

  - `Text param.Field[AgentTextParamResp]`

    Configuration for text generated by the agent.

  - `Tools param.Field[[]PersistedAgentToolParamUnionResp]`

    Tools available to the agent.

    - `PersistedAgentToolParamFunctionResp`

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

      - `DeferLoading bool`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `PersistedAgentToolParamToolSearchResp`

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `PersistedAgentToolParamProgrammaticToolCallingResp`

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `Enabled bool`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `PersistedAgentToolParamMcpResp`

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportParamUnionResp`

        The credential-free transport used to connect to the MCP server.

        - `PersistedMcpTransportParamHTTPResp`

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

        - `PersistedMcpTransportParamStdioResp`

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

          - `Args []string`

            Arguments passed to the MCP server command.

          - `EnvVars []string`

            Environment variable names to inherit from the selected execution environment.

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

      - `AllowedTools []string`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `ConnectionOrigin string`

        Selects where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolParamMcpConnectionOriginService PersistedAgentToolParamMcpConnectionOrigin = "service"`

          Uses the Managed Agents service network.

        - `const PersistedAgentToolParamMcpConnectionOriginEnvironment PersistedAgentToolParamMcpConnectionOrigin = "environment"`

          Uses the session's execution environment.

      - `CredentialID string`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `PersistedAgentToolParamWebSearchResp`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

      - `AllowedDomains []string`

        Domains the search may include.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolParamWebSearchContextSizeLow PersistedAgentToolParamWebSearchContextSize = "low"`

        - `const PersistedAgentToolParamWebSearchContextSizeMedium PersistedAgentToolParamWebSearchContextSize = "medium"`

        - `const PersistedAgentToolParamWebSearchContextSizeHigh PersistedAgentToolParamWebSearchContextSize = "high"`

      - `Location PersistedAgentToolParamWebSearchLocationResp`

        Approximate location used to localize search results.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results. Defaults to `live`.

        - `const PersistedAgentToolParamWebSearchModeDisabled PersistedAgentToolParamWebSearchMode = "disabled"`

          Disables web search.

        - `const PersistedAgentToolParamWebSearchModeCached PersistedAgentToolParamWebSearchMode = "cached"`

          Uses cached search results.

        - `const PersistedAgentToolParamWebSearchModeLive PersistedAgentToolParamWebSearchMode = "live"`

          Searches the live web.

    - `PersistedAgentToolParamComputerUseResp`

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `type Agent struct{…}`

  A reusable agent scoped to the caller's project.

  - `ID string`

    The ID of the reusable agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the agent was created.

  - `Instructions string`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the agent.

  - `Model string`

    The requested model name used for inference.

  - `MultiAgent MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Name string`

    A human-readable name for the agent, or null if it is unnamed.

  - `Object Agent`

    The object type. Always `agent`.

    - `const AgentAgent Agent = "agent"`

  - `Reasoning AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AgentServiceTier`

    The resolved service-tier policy used for model requests.

    - `const AgentServiceTierAuto AgentServiceTier = "auto"`

    - `const AgentServiceTierDefault AgentServiceTier = "default"`

    - `const AgentServiceTierFlex AgentServiceTier = "flex"`

    - `const AgentServiceTierPriority AgentServiceTier = "priority"`

    - `const AgentServiceTierFast AgentServiceTier = "fast"`

    - `const AgentServiceTierUltrafast AgentServiceTier = "ultrafast"`

  - `Text AgentText`

    The resolved configuration for text generated by the agent.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []PersistedAgentToolUnion`

    Tools available to the agent.

    - `type PersistedAgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

    - `type PersistedAgentToolToolSearch struct{…}`

      Discovers deferred function tools and loads them into the model context.

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type PersistedAgentToolMcp struct{…}`

      Tools provided by a remote MCP server without stored credentials.

      - `AllowedTools []string`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

        - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportUnion`

        The credential-free transport used to connect to the MCP server.

        - `type PersistedMcpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type PersistedMcpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type PersistedAgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

        - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

        - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

      - `Location PersistedAgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results.

        - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

        - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

        - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type PersistedAgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agent, err := client.Beta.Agents.Update(
    context.TODO(),
    "agent_id",
    openai.BetaAgentUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agent.ID)
}
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

- `type Agent struct{…}`

  A reusable agent scoped to the caller's project.

  - `ID string`

    The ID of the reusable agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the agent was created.

  - `Instructions string`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the agent.

  - `Model string`

    The requested model name used for inference.

  - `MultiAgent MultiAgentConfig`

    The resolved configuration for creating and coordinating subagents.

    - `Enabled bool`

      Whether subagent tools are enabled. Defaults to false.

    - `MaxConcurrentSubagents int64`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Name string`

    A human-readable name for the agent, or null if it is unnamed.

  - `Object Agent`

    The object type. Always `agent`.

    - `const AgentAgent Agent = "agent"`

  - `Reasoning AgentReasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Effort AgentReasoningEffort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

      - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

      - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

      - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

      - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

      - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

      - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

    - `Summary AgentReasoningSummary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

        Returns a concise reasoning summary when supported.

      - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

        Returns a detailed reasoning summary when supported.

      - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier AgentServiceTier`

    The resolved service-tier policy used for model requests.

    - `const AgentServiceTierAuto AgentServiceTier = "auto"`

    - `const AgentServiceTierDefault AgentServiceTier = "default"`

    - `const AgentServiceTierFlex AgentServiceTier = "flex"`

    - `const AgentServiceTierPriority AgentServiceTier = "priority"`

    - `const AgentServiceTierFast AgentServiceTier = "fast"`

    - `const AgentServiceTierUltrafast AgentServiceTier = "ultrafast"`

  - `Text AgentText`

    The resolved configuration for text generated by the agent.

    - `Format TextFormatUnion`

      The effective output format. Defaults to ordinary text.

      - `type TextFormatText struct{…}`

        Generates ordinary text without a structured-output constraint.

        - `Type Text`

          The type of the object. Always `text`.

          - `const TextText Text = "text"`

      - `type TextFormatJSONSchema struct{…}`

        Constrains generated text to a JSON Schema.

        - `Schema map[string, any]`

          The JSON Schema that generated text must match.

        - `Type JSONSchema`

          The type of the object. Always `json_schema`.

          - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

    - `Verbosity AgentTextVerbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

      - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

      - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

  - `Tools []PersistedAgentToolUnion`

    Tools available to the agent.

    - `type PersistedAgentToolFunction struct{…}`

      A function defined by the application.

      - `DeferLoading bool`

        Whether the function is deferred and discovered through tool search.

      - `Description string`

        A description of what the function does.

      - `Name string`

        The name of the function.

      - `Parameters map[string, any]`

        A JSON Schema object describing the function's arguments.

      - `Type Function`

        The type of the object. Always `function`.

        - `const FunctionFunction Function = "function"`

    - `type PersistedAgentToolToolSearch struct{…}`

      Discovers deferred function tools and loads them into the model context.

      - `Type ToolSearch`

        The type of the object. Always `tool_search`.

        - `const ToolSearchToolSearch ToolSearch = "tool_search"`

    - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

      Enables calling tools from model-generated code.

      - `Enabled bool`

        Whether tools can be called from model-generated code.

      - `Type ProgrammaticToolCalling`

        The type of the object. Always `programmatic_tool_calling`.

        - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `type PersistedAgentToolMcp struct{…}`

      Tools provided by a remote MCP server without stored credentials.

      - `AllowedTools []string`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin string`

        Where outbound MCP HTTP connections originate.

        - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

        - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

      - `CredentialID string`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata map[string, any]`

        Metadata included with requests to this MCP server.

      - `Required bool`

        Whether this MCP server must initialize before the first turn.

      - `ServerLabel string`

        A label used to identify the MCP server in tool calls.

      - `Transport PersistedMcpTransportUnion`

        The credential-free transport used to connect to the MCP server.

        - `type PersistedMcpTransportHTTP struct{…}`

          Connects to an MCP server over HTTP.

          - `Headers map[string, string]`

            Non-secret HTTP headers sent to the MCP server.

          - `ServerURL string`

            The URL of the MCP server.

          - `Type HTTP`

            The type of the object. Always `http`.

            - `const HTTPHTTP HTTP = "http"`

        - `type PersistedMcpTransportStdio struct{…}`

          Starts an MCP server as a local process.

          - `Args []string`

            Arguments passed to the MCP server command.

          - `Command string`

            The command used to start the MCP server.

          - `Cwd string`

            The working directory used to start the MCP server.

          - `EnvVars []string`

            Environment variable names inherited from the execution environment.

          - `Type Stdio`

            The type of the object. Always `stdio`.

            - `const StdioStdio Stdio = "stdio"`

      - `Type Mcp`

        The type of the object. Always `mcp`.

        - `const McpMcp Mcp = "mcp"`

    - `type PersistedAgentToolWebSearch struct{…}`

      Web search.

      - `AllowedDomains []string`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize string`

        The amount of search context made available to the model. Defaults to `medium`.

        - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

        - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

        - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

      - `Location PersistedAgentToolWebSearchLocation`

        Approximate location used to localize search results, if provided.

        - `City string`

          The city name.

        - `Country string`

          The two-letter ISO country code, such as `US`.

        - `Region string`

          The region or state name.

        - `Timezone string`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode string`

        The source used for web search results.

        - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

        - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

        - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

      - `Type WebSearch`

        The type of the object. Always `web_search`.

        - `const WebSearchWebSearch WebSearch = "web_search"`

    - `type PersistedAgentToolComputerUse struct{…}`

      Browser use in an OpenAI-hosted session.

      - `IncludeScreenshots bool`

        Whether computer tool outputs include screenshots.

      - `Type ComputerUse`

        The type of the object. Always `computer_use`.

        - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the agent was last updated.

### Agent Browser Authentication Cancel Param

- `type AgentBrowserAuthenticationCancelParamResp struct{…}`

  - `Action Cancel`

    - `const CancelCancel Cancel = "cancel"`

  - `Type BrowserAuthentication`

    - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

### Agent Browser Authentication Submit Param

- `type AgentBrowserAuthenticationSubmitParamResp struct{…}`

  - `Action Submit`

    - `const SubmitSubmit Submit = "submit"`

  - `Fields []AgentBrowserAuthenticationSubmitParamFieldResp`

    Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

    - `FieldID string`

      The field ID from the required action.

    - `Value string`

      The value to enter into the registered control.

  - `Type BrowserAuthentication`

    - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

  - `SelectedOption string`

    The chosen method. Required when the required action contains options.

### Agent Browser Origin Access Param

- `type AgentBrowserOriginAccessParamResp struct{…}`

  - `Decision AgentBrowserOriginAccessParamDecision`

    Whether to allow, deny, or cancel the requested origin access.

    - `const AgentBrowserOriginAccessParamDecisionApprove AgentBrowserOriginAccessParamDecision = "approve"`

      Allow the browser to access this origin.

    - `const AgentBrowserOriginAccessParamDecisionDeny AgentBrowserOriginAccessParamDecision = "deny"`

      Deny access to this origin.

    - `const AgentBrowserOriginAccessParamDecisionCancel AgentBrowserOriginAccessParamDecision = "cancel"`

      Dismiss this request without approving access.

  - `Type BrowserOriginAccess`

    - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

### Agent Close Subagent Call Item

- `type AgentCloseSubagentCallItem struct{…}`

  A request to close a subagent.

  - `ID string`

    The ID of the tool call item.

  - `RecipientAgentID string`

    The ID of the agent to close.

  - `SenderAgentID string`

    The ID of the agent requesting the close.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type CloseSubagentCall`

    The item type. Always `close_subagent_call`.

    - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

      The current public item type.

### Agent Command Execution Item

- `type AgentCommandExecutionItem struct{…}`

  A command execution produced by the agent.

  - `ID string`

    The ID of the command execution item.

  - `Command string`

    The command that was executed.

  - `Cwd string`

    The working directory used to execute the command.

  - `DurationMs int64`

    The command duration in milliseconds.

  - `ExitCode int64`

    The process exit code, if the command completed.

  - `Output string`

    The command output, if available.

  - `Status AgentFunctionCallStatus`

    The status of the command execution.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type CommandExecution`

    The item type. Always `command_execution`.

    - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

### Agent Content

- `type AgentContentUnion interface{…}`

  A plaintext or encrypted content part exchanged between agents.

  - `type OutputText struct{…}`

    A text content part produced by the agent.

    - `Text string`

      The text produced by the agent.

    - `Type OutputText`

      The content type. Always `output_text`.

      - `const OutputTextOutputText OutputText = "output_text"`

  - `type AgentContentEncryptedContent struct{…}`

    Encrypted content exchanged between agents.

    - `EncryptedContent string`

      The encrypted content payload.

    - `Type EncryptedContent`

      The content type. Always `encrypted_content`.

      - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

### Agent Create Subagent Call Item

- `type AgentCreateSubagentCallItem struct{…}`

  A request to spawn a subagent.

  - `ID string`

    The ID of the tool call item.

  - `AgentID string`

    The ID of the agent that requested the subagent.

  - `Content []AgentContentUnion`

    The task given to the spawned agent.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `Model string`

    The model requested for the spawned agent.

  - `ReasoningEffort string`

    The reasoning effort requested for the spawned agent.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type CreateSubagentCall`

    The item type. Always `create_subagent_call`.

    - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

      The current public item type.

### Agent Deleted

- `type AgentDeleted struct{…}`

  A deleted reusable agent.

  - `ID string`

    The ID of the deleted agent.

  - `Deleted bool`

    Whether the agent was deleted. Always `true`.

  - `Object AgentDeleted`

    The object type. Always `agent.deleted`.

    - `const AgentDeletedAgentDeleted AgentDeleted = "agent.deleted"`

### Agent Function Call Item

- `type AgentFunctionCallItem struct{…}`

  A function call produced by the agent.

  - `ID string`

    The ID of the function call item.

  - `Arguments any`

    The arguments to pass to the function.

  - `CallID string`

    The ID used to submit the function result.

  - `Name string`

    The name of the function to call.

  - `Status AgentFunctionCallStatus`

    The status of the function call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type FunctionCall`

    The item type. Always `function_call`.

    - `const FunctionCallFunctionCall FunctionCall = "function_call"`

### Agent Function Call Output

- `type AgentFunctionCallOutputUnion interface{…}`

  The text or model-input content supplied as a function result.

  - `string`

  - `type AgentFunctionCallOutputArray []InputContentUnion`

    - `type InputContentInputText struct{…}`

      Text input recorded in a session item.

      - `Text string`

        The text supplied to the agent.

      - `Type InputText`

        The type of the object. Always `input_text`.

        - `const InputTextInputText InputText = "input_text"`

    - `type InputContentInputImage struct{…}`

      Image input recorded in a session item.

      - `ImageURL string`

        The URL of the image supplied to the agent, which may be a base64-encoded data URL.

      - `Type InputImage`

        The type of the object. Always `input_image`.

        - `const InputImageInputImage InputImage = "input_image"`

### Agent Function Call Output Param

- `type AgentFunctionCallOutputParamUnionResp interface{…}`

  A function result represented as text or supported model-input content.

  - `string`

  - `[]InputContentParamUnionResp`

    - `InputContentParamInputTextResp`

      - `Text string`

        The text sent to the model.

      - `Type InputText`

        The type of the object. Always `input_text`.

        - `const InputTextInputText InputText = "input_text"`

    - `InputContentParamInputImageResp`

      - `ImageURL string`

        The URL of the image sent to the model.

      - `Type InputImage`

        The type of the object. Always `input_image`.

        - `const InputImageInputImage InputImage = "input_image"`

### Agent Function Call Status

- `type AgentFunctionCallStatus string`

  The status of a tool call.

  - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

    The call is in progress.

  - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

    The call completed successfully.

  - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

    The call failed.

  - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

    The call stopped before completing.

### Agent Interrupt Subagent Call Item

- `type AgentInterruptSubagentCallItem struct{…}`

  A request to interrupt a subagent's current turn. The subagent remains available.

  - `ID string`

    The ID of the tool call item.

  - `RecipientAgentID string`

    The ID of the agent to interrupt.

  - `SenderAgentID string`

    The ID of the agent requesting the interrupt.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type InterruptSubagentCall`

    The item type. Always `interrupt_subagent_call`.

    - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

      The current public item type.

### Agent Mcp Call Item

- `type AgentMcpCallItem struct{…}`

  A call to a tool on an MCP server.

  - `ID string`

    The ID of the MCP call item.

  - `Arguments any`

    The arguments passed to the MCP tool.

  - `Error any`

    The error returned by the MCP tool, if any.

  - `Name string`

    The name of the MCP tool.

  - `Output any`

    The output returned by the MCP tool, if any.

  - `ServerLabel string`

    The label of the MCP server.

  - `Status AgentFunctionCallStatus`

    The status of the MCP tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type McpCall`

    The item type. Always `mcp_call`.

    - `const McpCallMcpCall McpCall = "mcp_call"`

### Agent Output Command Execution Output Delta Event

- `type AgentOutputCommandExecutionOutputDeltaEvent struct{…}`

  Emitted when command execution produces an output delta.

  - `Delta string`

    The output text that was appended.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the command execution item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentOutputCommandExecutionOutputDelta`

    The type of the object. Always `agent.output.command_execution_output.delta`.

    - `const AgentOutputCommandExecutionOutputDeltaAgentOutputCommandExecutionOutputDelta AgentOutputCommandExecutionOutputDelta = "agent.output.command_execution_output.delta"`

### Agent Output Item

- `type AgentOutputItemUnion interface{…}`

  An output item produced by an agent.

  - `type AgentSessionAssistantMessage struct{…}`

    An assistant message produced by the agent.

    - `ID string`

      The ID of the message.

    - `Content []OutputText`

      The content of the message.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `Phase AgentSessionAssistantMessagePhase`

      The phase of the assistant message.

      - `const AgentSessionAssistantMessagePhaseCommentary AgentSessionAssistantMessagePhase = "commentary"`

        Commentary produced while the agent works.

      - `const AgentSessionAssistantMessagePhaseFinalAnswer AgentSessionAssistantMessagePhase = "final_answer"`

        The agent's final answer.

    - `Role Assistant`

      The role of the message author. Always `assistant`.

      - `const AssistantAssistant Assistant = "assistant"`

    - `Status AgentOutputItemStatus`

      The status of the message.

      - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

        The item is in progress.

      - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

        The item is complete.

      - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

        The item stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

    - `Name string`

      The name of the function to call.

    - `Status AgentFunctionCallStatus`

      The status of the function call.

      - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

        The call is in progress.

      - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

        The call completed successfully.

      - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

        The call failed.

      - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

        The call stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentOutputItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

    - `Output AgentOutputItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentOutputItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

    - `Request AgentOutputItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

      - `Fields []AgentOutputItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        - `ID string`

          The field ID to submit as field_id in a fields entry.

        - `Label string`

          The label to display beside the control.

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

      - `Options []AgentOutputItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        - `ID string`

          The option ID to submit as selected_option.

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

        - `Label string`

          The method label to display.

      - `Reason string`

        Why the agent needs the user to sign in.

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

    - `TurnID string`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

        - `Query string`

          The search query, when a single query was used.

        - `Type Search`

          The type of the object. Always `search`.

          - `const SearchSearch Search = "search"`

      - `type WebSearchActionOpenPage struct{…}`

        Opens a web page.

        - `Type OpenPage`

          The type of the object. Always `open_page`.

          - `const OpenPageOpenPage OpenPage = "open_page"`

        - `URL string`

          The URL of the page that was opened.

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

    - `Command string`

      The command that was executed.

    - `Cwd string`

      The working directory used to execute the command.

    - `DurationMs int64`

      The command duration in milliseconds.

    - `ExitCode int64`

      The process exit code, if the command completed.

    - `Output string`

      The command output, if available.

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

    - `AgentID string`

      The ID of the agent that requested the subagent.

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `Model string`

      The model requested for the spawned agent.

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

        The current public item type.

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

    - `SenderAgentID string`

      The ID of the agent sending the input.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

        The current public item type.

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to resume.

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

        The current public item type.

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

    - `SenderAgentID string`

      The ID of the agent waiting for results.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

        The current public item type.

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

        The current public item type.

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to close.

    - `SenderAgentID string`

      The ID of the agent requesting the close.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

        The current public item type.

### Agent Output Item Status

- `type AgentOutputItemStatus string`

  The status of an agent output item.

  - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

    The item is in progress.

  - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

    The item is complete.

  - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

    The item stopped before completing.

### Agent Reasoning

- `type AgentReasoning struct{…}`

  The reasoning configuration used by an agent.

  - `Effort AgentReasoningEffort`

    The requested reasoning effort, or `null` when the model selects its own default.

    - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

    - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

    - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

    - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

    - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

    - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

    - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

  - `Summary AgentReasoningSummary`

    The requested reasoning summary format, or `null` when summaries are disabled.

    - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

      Returns a concise reasoning summary when supported.

    - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

      Returns a detailed reasoning summary when supported.

    - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

      Automatically selects the most detailed summary supported by the model.

### Agent Reasoning Item

- `type AgentReasoningItem struct{…}`

  A reasoning item produced by the agent.

  - `ID string`

    The ID of the reasoning item.

  - `Status AgentOutputItemStatus`

    The status of the reasoning item.

    - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

      The item is in progress.

    - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

      The item is complete.

    - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

      The item stopped before completing.

  - `Summary []SummaryText`

    The reasoning summaries produced by the agent.

    - `Text string`

      The reasoning summary text.

    - `Type SummaryText`

      The content type. Always `summary_text`.

      - `const SummaryTextSummaryText SummaryText = "summary_text"`

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type Reasoning`

    The item type. Always `reasoning`.

    - `const ReasoningReasoning Reasoning = "reasoning"`

### Agent Reasoning Param

- `type AgentReasoningParamResp struct{…}`

  Reasoning configuration for the agent.

  - `Effort AgentReasoningParamEffort`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `const AgentReasoningParamEffortNone AgentReasoningParamEffort = "none"`

    - `const AgentReasoningParamEffortMinimal AgentReasoningParamEffort = "minimal"`

    - `const AgentReasoningParamEffortLow AgentReasoningParamEffort = "low"`

    - `const AgentReasoningParamEffortMedium AgentReasoningParamEffort = "medium"`

    - `const AgentReasoningParamEffortHigh AgentReasoningParamEffort = "high"`

    - `const AgentReasoningParamEffortXhigh AgentReasoningParamEffort = "xhigh"`

    - `const AgentReasoningParamEffortMax AgentReasoningParamEffort = "max"`

  - `Summary AgentReasoningParamSummary`

    Controls whether the response includes a reasoning summary.

    - `const AgentReasoningParamSummaryConcise AgentReasoningParamSummary = "concise"`

      Returns a concise reasoning summary when supported.

    - `const AgentReasoningParamSummaryDetailed AgentReasoningParamSummary = "detailed"`

      Returns a detailed reasoning summary when supported.

    - `const AgentReasoningParamSummaryAuto AgentReasoningParamSummary = "auto"`

      Automatically selects the most detailed summary supported by the model.

### Agent Resume Subagent Call Item

- `type AgentResumeSubagentCallItem struct{…}`

  A request to resume a subagent.

  - `ID string`

    The ID of the tool call item.

  - `RecipientAgentID string`

    The ID of the agent to resume.

  - `SenderAgentID string`

    The ID of the agent requesting the resume.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type ResumeSubagentCall`

    The item type. Always `resume_subagent_call`.

    - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

      The current public item type.

### Agent Send Subagent Input Call Item

- `type AgentSendSubagentInputCallItem struct{…}`

  A request to send input to another agent.

  - `ID string`

    The ID of the tool call item.

  - `Content []AgentContentUnion`

    The input sent to the receiving agent.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `RecipientAgentID string`

    The ID of the agent receiving the input.

  - `SenderAgentID string`

    The ID of the agent sending the input.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type SendSubagentInputCall`

    The item type. Always `send_subagent_input_call`.

    - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

      The current public item type.

### Agent Session

- `type AgentSession struct{…}`

  A Managed Agents session.

  - `ID string`

    The ID of the session.

  - `Agent AgentSessionAgent`

    The agent running in the session.

    - `ID string`

      The ID of the agent.

    - `Instructions string`

      Custom instructions appended to the agent's default base instructions.

    - `Model string`

      The model used by the agent.

    - `MultiAgent MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled. Defaults to false.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Name string`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `Reasoning AgentReasoning`

      The agent's reasoning configuration.

      - `Effort AgentReasoningEffort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

        - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

        - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

        - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

        - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

        - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

        - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

      - `Summary AgentReasoningSummary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

      - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

      - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

      - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

      - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

      - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

    - `Text AgentText`

      Configuration for text generated by the agent.

      - `Format TextFormatUnion`

        The effective output format. Defaults to ordinary text.

        - `type TextFormatText struct{…}`

          Generates ordinary text without a structured-output constraint.

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `type TextFormatJSONSchema struct{…}`

          Constrains generated text to a JSON Schema.

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextVerbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

        - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

        - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

    - `Tools []AgentToolUnion`

      Tools available to the agent.

      - `type AgentToolFunction struct{…}`

        A function defined by the application.

        - `DeferLoading bool`

          Whether the function is deferred and discovered through tool search.

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

      - `type AgentToolProgrammaticToolCalling struct{…}`

        Enables calling tools from model-generated code.

        - `Enabled bool`

          Whether tools can be called from model-generated code.

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `type AgentToolMcp struct{…}`

        Tools provided by a remote MCP server.

        - `AllowedTools []string`

          The MCP tools the agent may call.

        - `ConnectionOrigin string`

          Where outbound MCP HTTP connections originate.

          - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

          - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

        - `CredentialID string`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn.

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportUnion`

          The transport used to connect to the MCP server.

          - `type McpTransportHTTP struct{…}`

            Connects to an MCP server over HTTP.

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

          - `type McpTransportStdio struct{…}`

            Starts an MCP server as a local process.

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `EnvVars []string`

              Environment variable names inherited from the execution environment.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

      - `type AgentToolWebSearch struct{…}`

        Web search.

        - `AllowedDomains []string`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

          - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

          - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

        - `Location AgentToolWebSearchLocation`

          Approximate location used to localize search results, if provided.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results.

          - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

          - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

          - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

      - `type AgentToolComputerUse struct{…}`

        Browser use in an OpenAI-hosted session.

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots.

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment EnvironmentUnion`

    The execution environment for the session.

    - `type EnvironmentNone struct{…}`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `Type None`

        The type of the object. Always `none`.

        - `const NoneNone None = "none"`

    - `type EnvironmentOpenAIHosted struct{…}`

      An environment hosted by OpenAI.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `Desktop EnvironmentOpenAIHostedDesktop`

        The effective desktop configuration.

        - `Enabled bool`

          Whether the environment provisions a desktop and browser proxy.

      - `Files []HostedEnvironmentFileUnion`

        Files available in the environment, excluding their contents.

        - `type HostedEnvironmentFileID struct{…}`

          A file copied from the OpenAI Files API.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `FileID string`

            The ID of the uploaded file.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type FileID`

            The type of the object. Always `file_id`.

            - `const FileIDFileID FileID = "file_id"`

        - `type HostedEnvironmentFileInline struct{…}`

          A file supplied inline when the session was created.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Network EnvironmentOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `Access string`

          The environment's network access mode.

          - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

            Allows unrestricted network access.

          - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

            Disables network access.

          - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

            Applies the configured domain restrictions.

        - `AllowedDomains []string`

          Domains the environment may access when network access is restricted.

      - `Packages EnvironmentOpenAIHostedPackages`

        Packages installed in the environment.

        - `Npm []string`

          npm packages installed globally in the environment.

        - `Python []string`

          Python packages installed in the environment.

        - `System []string`

          System packages installed in the environment.

      - `Plugins []HostedPlugin`

        Plugins installed in the environment, excluding their archive contents.

        - `Description string`

          The installed plugin description.

        - `Name string`

          The installed plugin name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

      - `Skills []HostedSkillUnion`

        Skills installed in the environment, excluding their archive contents.

        - `type HostedSkillReference struct{…}`

          A skill installed from the Skills API.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `SkillID string`

            The referenced skill ID.

          - `Type SkillReference`

            The type of the object. Always `skill_reference`.

            - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

          - `Version string`

            The concrete skill version installed for this session.

        - `type HostedSkillInline struct{…}`

          A skill installed from an inline ZIP archive.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Type OpenAIHosted`

        The type of the object. Always `openai_hosted`.

        - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `ContainerSize string`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

        - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

        - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

    - `type EnvironmentSelfHosted struct{…}`

      An environment hosted by the application.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `RemoteURL string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `Type SelfHosted`

        The type of the object. Always `self_hosted`.

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

      - `WorkspaceDirectory string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Error string`

    The error that caused the session to fail, if any.

  - `LastActiveAt int64`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the session.

  - `Object AgentSession`

    The object type. Always `agent.session`.

    - `const AgentSessionAgentSession AgentSession = "agent.session"`

  - `RequiredActions []AgentSessionRequiredActionUnion`

    Actions that must be completed before the session can continue.

    - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

      Respond to a computer-use request.

      - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

        The information needed to render the request.

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

          A browser origin awaiting the application's approval decision.

          - `Origin string`

            The origin the browser needs permission to access.

          - `Reason string`

            The browser's explanation for this request, or null when unavailable.

          - `Type BrowserOriginAccess`

            The type of the object. Always `browser_origin_access`.

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `RequestID string`

        The registered request ID to echo when responding.

      - `TurnID string`

        The turn that requested approval.

      - `Type ComputerUseApprovalRequest`

        The type of the object. Always `computer_use_approval_request`.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionRequiredActionFunctionCall struct{…}`

      Run a function tool and submit its result.

      - `Arguments any`

        The arguments supplied by the model.

      - `CallID string`

        The ID to include when submitting the function result.

      - `Name string`

        The function name.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type FunctionCall`

        The type of the object. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

      Reconnect a session environment.

      - `EnvironmentID string`

        The ID of the environment to reconnect.

      - `Type EnvironmentConnection`

        The type of the object. Always `environment_connection`.

        - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

  - `Status AgentSessionStatus`

    The current status of the session.

    - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

      The session is processing a turn.

    - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

      The session is waiting for one or more required actions.

    - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

      The session failed.

  - `Usage TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

  - `VaultIDs []string`

    The IDs of vaults made available to the session.

### Agent Session Assistant Message

- `type AgentSessionAssistantMessage struct{…}`

  An assistant message produced by the agent.

  - `ID string`

    The ID of the message.

  - `Content []OutputText`

    The content of the message.

    - `Text string`

      The text produced by the agent.

    - `Type OutputText`

      The content type. Always `output_text`.

      - `const OutputTextOutputText OutputText = "output_text"`

  - `Phase AgentSessionAssistantMessagePhase`

    The phase of the assistant message.

    - `const AgentSessionAssistantMessagePhaseCommentary AgentSessionAssistantMessagePhase = "commentary"`

      Commentary produced while the agent works.

    - `const AgentSessionAssistantMessagePhaseFinalAnswer AgentSessionAssistantMessagePhase = "final_answer"`

      The agent's final answer.

  - `Role Assistant`

    The role of the message author. Always `assistant`.

    - `const AssistantAssistant Assistant = "assistant"`

  - `Status AgentOutputItemStatus`

    The status of the message.

    - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

      The item is in progress.

    - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

      The item is complete.

    - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

      The item stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type Message`

    The item type. Always `message`.

    - `const MessageMessage Message = "message"`

### Agent Session Created Event

- `type AgentSessionCreatedEvent struct{…}`

  Emitted when a session is created.

  - `EventID string`

    The unique ID of the event.

  - `Session AgentSession`

    The session that was created.

    - `ID string`

      The ID of the session.

    - `Agent AgentSessionAgent`

      The agent running in the session.

      - `ID string`

        The ID of the agent.

      - `Instructions string`

        Custom instructions appended to the agent's default base instructions.

      - `Model string`

        The model used by the agent.

      - `MultiAgent MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Name string`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `Reasoning AgentReasoning`

        The agent's reasoning configuration.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

        - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

        - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

        - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

        - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

        - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

      - `Text AgentText`

        Configuration for text generated by the agent.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Tools available to the agent.

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

          - `Name string`

            The name of the function.

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

              - `Command string`

                The command used to start the MCP server.

              - `Cwd string`

                The working directory used to start the MCP server.

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

            - `Country string`

              The two-letter ISO country code, such as `US`.

            - `Region string`

              The region or state name.

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `CreatedAt int64`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment EnvironmentUnion`

      The execution environment for the session.

      - `type EnvironmentNone struct{…}`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type EnvironmentOpenAIHosted struct{…}`

        An environment hosted by OpenAI.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `Desktop EnvironmentOpenAIHostedDesktop`

          The effective desktop configuration.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `Files []HostedEnvironmentFileUnion`

          Files available in the environment, excluding their contents.

          - `type HostedEnvironmentFileID struct{…}`

            A file copied from the OpenAI Files API.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `FileID string`

              The ID of the uploaded file.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type HostedEnvironmentFileInline struct{…}`

            A file supplied inline when the session was created.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

        - `Packages EnvironmentOpenAIHostedPackages`

          Packages installed in the environment.

          - `Npm []string`

            npm packages installed globally in the environment.

          - `Python []string`

            Python packages installed in the environment.

          - `System []string`

            System packages installed in the environment.

        - `Plugins []HostedPlugin`

          Plugins installed in the environment, excluding their archive contents.

          - `Description string`

            The installed plugin description.

          - `Name string`

            The installed plugin name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []HostedSkillUnion`

          Skills installed in the environment, excluding their archive contents.

          - `type HostedSkillReference struct{…}`

            A skill installed from the Skills API.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `SkillID string`

              The referenced skill ID.

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The concrete skill version installed for this session.

          - `type HostedSkillInline struct{…}`

            A skill installed from an inline ZIP archive.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `ContainerSize string`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

          - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

      - `type EnvironmentSelfHosted struct{…}`

        An environment hosted by the application.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `RemoteURL string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Error string`

      The error that caused the session to fail, if any.

    - `LastActiveAt int64`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the session.

    - `Object AgentSession`

      The object type. Always `agent.session`.

      - `const AgentSessionAgentSession AgentSession = "agent.session"`

    - `RequiredActions []AgentSessionRequiredActionUnion`

      Actions that must be completed before the session can continue.

      - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

        Respond to a computer-use request.

        - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

          The information needed to render the request.

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

            A registered form awaiting the application's response.

            - `CredentialOrigin string`

              The registered form or frame origin where values will be entered.

            - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

              Controls to render. All submitted values are sensitive.

              - `ID string`

                The field ID to submit as field_id in a fields entry.

              - `Label string`

                The label to display beside the control.

              - `Required bool`

                Whether this control requires a nonempty value.

              - `Type string`

                The rendering type, such as email, password, or text.

            - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

              Sign-in methods. Empty for a plain form.

              - `ID string`

                The option ID to submit as selected_option.

              - `FieldIDs []string`

                IDs from the registered fields that this method accepts.

              - `Label string`

                The method label to display.

            - `Reason string`

              Why the agent needs the user to sign in.

            - `Type BrowserAuthentication`

              The type of the object. Always `browser_authentication`.

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

            A browser origin awaiting the application's approval decision.

            - `Origin string`

              The origin the browser needs permission to access.

            - `Reason string`

              The browser's explanation for this request, or null when unavailable.

            - `Type BrowserOriginAccess`

              The type of the object. Always `browser_origin_access`.

              - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

        - `RequestID string`

          The registered request ID to echo when responding.

        - `TurnID string`

          The turn that requested approval.

        - `Type ComputerUseApprovalRequest`

          The type of the object. Always `computer_use_approval_request`.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionRequiredActionFunctionCall struct{…}`

        Run a function tool and submit its result.

        - `Arguments any`

          The arguments supplied by the model.

        - `CallID string`

          The ID to include when submitting the function result.

        - `Name string`

          The function name.

        - `TurnID string`

          The ID of the turn that requested the function call.

        - `Type FunctionCall`

          The type of the object. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

        Reconnect a session environment.

        - `EnvironmentID string`

          The ID of the environment to reconnect.

        - `Type EnvironmentConnection`

          The type of the object. Always `environment_connection`.

          - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

    - `Status AgentSessionStatus`

      The current status of the session.

      - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

        The session is processing a turn.

      - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

        The session is waiting for one or more required actions.

      - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

        The session failed.

    - `Usage TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

    - `VaultIDs []string`

      The IDs of vaults made available to the session.

  - `Type AgentSessionCreated`

    The type of the object. Always `agent.session.created`.

    - `const AgentSessionCreatedAgentSessionCreated AgentSessionCreated = "agent.session.created"`

### Agent Session Deleted

- `type AgentSessionDeleted struct{…}`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `ID string`

    The ID of the deleted session.

  - `Deleted bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `Object AgentSessionDeleted`

    The object type. Always `agent.session.deleted`.

    - `const AgentSessionDeletedAgentSessionDeleted AgentSessionDeleted = "agent.session.deleted"`

### Agent Session Environment Connected Event

- `type AgentSessionEnvironmentConnectedEvent struct{…}`

  Emitted when a session environment connects.

  - `Environment AgentSessionEnvironmentState`

    The current environment state.

    - `ID string`

      The public ID of the environment.

    - `Error AgentSessionEnvironmentStateError`

      The error reported while preparing the environment, if any.

      - `Code string`

        A machine-readable error code.

      - `Message string`

        A human-readable error message.

      - `Type string`

        The error type.

    - `Status AgentSessionEnvironmentStateStatus`

      The environment's connection status.

      - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

        The environment is being prepared.

      - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

        The environment is ready to connect.

      - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

        The environment is connected.

      - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

        The environment is disconnected.

      - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

        The environment failed to connect.

    - `Type string`

      The environment type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionEnvironmentConnected`

    The type of the object. Always `agent.session.environment.connected`.

    - `const AgentSessionEnvironmentConnectedAgentSessionEnvironmentConnected AgentSessionEnvironmentConnected = "agent.session.environment.connected"`

### Agent Session Environment Disconnected Event

- `type AgentSessionEnvironmentDisconnectedEvent struct{…}`

  Emitted when a session environment disconnects.

  - `Environment AgentSessionEnvironmentState`

    The current environment state.

    - `ID string`

      The public ID of the environment.

    - `Error AgentSessionEnvironmentStateError`

      The error reported while preparing the environment, if any.

      - `Code string`

        A machine-readable error code.

      - `Message string`

        A human-readable error message.

      - `Type string`

        The error type.

    - `Status AgentSessionEnvironmentStateStatus`

      The environment's connection status.

      - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

        The environment is being prepared.

      - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

        The environment is ready to connect.

      - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

        The environment is connected.

      - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

        The environment is disconnected.

      - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

        The environment failed to connect.

    - `Type string`

      The environment type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionEnvironmentDisconnected`

    The type of the object. Always `agent.session.environment.disconnected`.

    - `const AgentSessionEnvironmentDisconnectedAgentSessionEnvironmentDisconnected AgentSessionEnvironmentDisconnected = "agent.session.environment.disconnected"`

### Agent Session Environment Failed Event

- `type AgentSessionEnvironmentFailedEvent struct{…}`

  Emitted when a session environment fails.

  - `Environment AgentSessionEnvironmentState`

    The current environment state.

    - `ID string`

      The public ID of the environment.

    - `Error AgentSessionEnvironmentStateError`

      The error reported while preparing the environment, if any.

      - `Code string`

        A machine-readable error code.

      - `Message string`

        A human-readable error message.

      - `Type string`

        The error type.

    - `Status AgentSessionEnvironmentStateStatus`

      The environment's connection status.

      - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

        The environment is being prepared.

      - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

        The environment is ready to connect.

      - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

        The environment is connected.

      - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

        The environment is disconnected.

      - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

        The environment failed to connect.

    - `Type string`

      The environment type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionEnvironmentFailed`

    The type of the object. Always `agent.session.environment.failed`.

    - `const AgentSessionEnvironmentFailedAgentSessionEnvironmentFailed AgentSessionEnvironmentFailed = "agent.session.environment.failed"`

### Agent Session Environment Pending Event

- `type AgentSessionEnvironmentPendingEvent struct{…}`

  Emitted while a session environment is being prepared.

  - `Environment AgentSessionEnvironmentState`

    The current environment state.

    - `ID string`

      The public ID of the environment.

    - `Error AgentSessionEnvironmentStateError`

      The error reported while preparing the environment, if any.

      - `Code string`

        A machine-readable error code.

      - `Message string`

        A human-readable error message.

      - `Type string`

        The error type.

    - `Status AgentSessionEnvironmentStateStatus`

      The environment's connection status.

      - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

        The environment is being prepared.

      - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

        The environment is ready to connect.

      - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

        The environment is connected.

      - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

        The environment is disconnected.

      - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

        The environment failed to connect.

    - `Type string`

      The environment type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionEnvironmentPending`

    The type of the object. Always `agent.session.environment.pending`.

    - `const AgentSessionEnvironmentPendingAgentSessionEnvironmentPending AgentSessionEnvironmentPending = "agent.session.environment.pending"`

### Agent Session Environment Ready Event

- `type AgentSessionEnvironmentReadyEvent struct{…}`

  Emitted when a hosted session environment is ready to connect.

  - `Environment AgentSessionEnvironmentState`

    The current environment state.

    - `ID string`

      The public ID of the environment.

    - `Error AgentSessionEnvironmentStateError`

      The error reported while preparing the environment, if any.

      - `Code string`

        A machine-readable error code.

      - `Message string`

        A human-readable error message.

      - `Type string`

        The error type.

    - `Status AgentSessionEnvironmentStateStatus`

      The environment's connection status.

      - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

        The environment is being prepared.

      - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

        The environment is ready to connect.

      - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

        The environment is connected.

      - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

        The environment is disconnected.

      - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

        The environment failed to connect.

    - `Type string`

      The environment type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionEnvironmentReady`

    The type of the object. Always `agent.session.environment.ready`.

    - `const AgentSessionEnvironmentReadyAgentSessionEnvironmentReady AgentSessionEnvironmentReady = "agent.session.environment.ready"`

### Agent Session Environment Reset Event

- `type AgentSessionEnvironmentResetEvent struct{…}`

  Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

  - `EnvironmentID string`

    The stable environment ID, retained across sandbox replacements.

  - `EventID string`

    The unique ID of the event.

  - `ResetCount int64`

    Monotonically increasing reset number. Repeated notifications share this number.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The associated turn, when applicable.

  - `Type AgentSessionEnvironmentReset`

    The type of the object. Always `agent.session.environment.reset`.

    - `const AgentSessionEnvironmentResetAgentSessionEnvironmentReset AgentSessionEnvironmentReset = "agent.session.environment.reset"`

### Agent Session Environment State

- `type AgentSessionEnvironmentState struct{…}`

  The current state of a session environment.

  - `ID string`

    The public ID of the environment.

  - `Error AgentSessionEnvironmentStateError`

    The error reported while preparing the environment, if any.

    - `Code string`

      A machine-readable error code.

    - `Message string`

      A human-readable error message.

    - `Type string`

      The error type.

  - `Status AgentSessionEnvironmentStateStatus`

    The environment's connection status.

    - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

      The environment is being prepared.

    - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

      The environment is ready to connect.

    - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

      The environment is connected.

    - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

      The environment is disconnected.

    - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

      The environment failed to connect.

  - `Type string`

    The environment type.

### Agent Session Error Event

- `type AgentSessionErrorEvent struct{…}`

  Emitted when a turn or session fails.

  - `Error SessionError`

    The error that occurred.

    - `Code string`

      The machine-readable error code, if any.

    - `Message string`

      A customer-safe explanation of the error.

    - `Param string`

      The request parameter associated with the error, if any.

    - `Type string`

      The error type.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Type Error`

    The type of the object. Always `error`.

    - `const ErrorError Error = "error"`

### Agent Session Event

- `type AgentSessionEventUnion interface{…}`

  An event emitted by a Managed Agents session.

  - `type AgentSessionErrorEvent struct{…}`

    Emitted when a turn or session fails.

    - `Error SessionError`

      The error that occurred.

      - `Code string`

        The machine-readable error code, if any.

      - `Message string`

        A customer-safe explanation of the error.

      - `Param string`

        The request parameter associated with the error, if any.

      - `Type string`

        The error type.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Type Error`

      The type of the object. Always `error`.

      - `const ErrorError Error = "error"`

  - `type AgentSessionEnvironmentReadyEvent struct{…}`

    Emitted when a hosted session environment is ready to connect.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

      - `ID string`

        The public ID of the environment.

      - `Error AgentSessionEnvironmentStateError`

        The error reported while preparing the environment, if any.

        - `Code string`

          A machine-readable error code.

        - `Message string`

          A human-readable error message.

        - `Type string`

          The error type.

      - `Status AgentSessionEnvironmentStateStatus`

        The environment's connection status.

        - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

          The environment is being prepared.

        - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

          The environment is ready to connect.

        - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

          The environment is connected.

        - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

          The environment is disconnected.

        - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

          The environment failed to connect.

      - `Type string`

        The environment type.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentReady`

      The type of the object. Always `agent.session.environment.ready`.

      - `const AgentSessionEnvironmentReadyAgentSessionEnvironmentReady AgentSessionEnvironmentReady = "agent.session.environment.ready"`

  - `type AgentSessionEnvironmentResetEvent struct{…}`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `EnvironmentID string`

      The stable environment ID, retained across sandbox replacements.

    - `EventID string`

      The unique ID of the event.

    - `ResetCount int64`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The associated turn, when applicable.

    - `Type AgentSessionEnvironmentReset`

      The type of the object. Always `agent.session.environment.reset`.

      - `const AgentSessionEnvironmentResetAgentSessionEnvironmentReset AgentSessionEnvironmentReset = "agent.session.environment.reset"`

  - `type AgentOutputCommandExecutionOutputDeltaEvent struct{…}`

    Emitted when command execution produces an output delta.

    - `Delta string`

      The output text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the command execution item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentOutputCommandExecutionOutputDelta`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `const AgentOutputCommandExecutionOutputDeltaAgentOutputCommandExecutionOutputDelta AgentOutputCommandExecutionOutputDelta = "agent.output.command_execution_output.delta"`

  - `type AgentSessionCreatedEvent struct{…}`

    Emitted when a session is created.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that was created.

      - `ID string`

        The ID of the session.

      - `Agent AgentSessionAgent`

        The agent running in the session.

        - `ID string`

          The ID of the agent.

        - `Instructions string`

          Custom instructions appended to the agent's default base instructions.

        - `Model string`

          The model used by the agent.

        - `MultiAgent MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `Enabled bool`

            Whether subagent tools are enabled. Defaults to false.

          - `MaxConcurrentSubagents int64`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `Name string`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `Reasoning AgentReasoning`

          The agent's reasoning configuration.

          - `Effort AgentReasoningEffort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

            - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

            - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

            - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

            - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

            - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

            - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

          - `Summary AgentReasoningSummary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

              Returns a concise reasoning summary when supported.

            - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

              Returns a detailed reasoning summary when supported.

            - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier string`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

          - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

          - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

          - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

          - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

          - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

        - `Text AgentText`

          Configuration for text generated by the agent.

          - `Format TextFormatUnion`

            The effective output format. Defaults to ordinary text.

            - `type TextFormatText struct{…}`

              Generates ordinary text without a structured-output constraint.

              - `Type Text`

                The type of the object. Always `text`.

                - `const TextText Text = "text"`

            - `type TextFormatJSONSchema struct{…}`

              Constrains generated text to a JSON Schema.

              - `Schema map[string, any]`

                The JSON Schema that generated text must match.

              - `Type JSONSchema`

                The type of the object. Always `json_schema`.

                - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

          - `Verbosity AgentTextVerbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

            - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

            - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

        - `Tools []AgentToolUnion`

          Tools available to the agent.

          - `type AgentToolFunction struct{…}`

            A function defined by the application.

            - `DeferLoading bool`

              Whether the function is deferred and discovered through tool search.

            - `Description string`

              A description of what the function does.

            - `Name string`

              The name of the function.

            - `Parameters map[string, any]`

              A JSON Schema object describing the function's arguments.

            - `Type Function`

              The type of the object. Always `function`.

              - `const FunctionFunction Function = "function"`

          - `type AgentToolProgrammaticToolCalling struct{…}`

            Enables calling tools from model-generated code.

            - `Enabled bool`

              Whether tools can be called from model-generated code.

            - `Type ProgrammaticToolCalling`

              The type of the object. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type AgentToolMcp struct{…}`

            Tools provided by a remote MCP server.

            - `AllowedTools []string`

              The MCP tools the agent may call.

            - `ConnectionOrigin string`

              Where outbound MCP HTTP connections originate.

              - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

              - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

            - `CredentialID string`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `RequestMetadata map[string, any]`

              Metadata included with requests to this MCP server.

            - `Required bool`

              Whether this MCP server must initialize before the first turn.

            - `ServerLabel string`

              A label used to identify the MCP server in tool calls.

            - `Transport McpTransportUnion`

              The transport used to connect to the MCP server.

              - `type McpTransportHTTP struct{…}`

                Connects to an MCP server over HTTP.

                - `ServerURL string`

                  The URL of the MCP server.

                - `Type HTTP`

                  The type of the object. Always `http`.

                  - `const HTTPHTTP HTTP = "http"`

              - `type McpTransportStdio struct{…}`

                Starts an MCP server as a local process.

                - `Args []string`

                  Arguments passed to the MCP server command.

                - `Command string`

                  The command used to start the MCP server.

                - `Cwd string`

                  The working directory used to start the MCP server.

                - `EnvVars []string`

                  Environment variable names inherited from the execution environment.

                - `Type Stdio`

                  The type of the object. Always `stdio`.

                  - `const StdioStdio Stdio = "stdio"`

            - `Type Mcp`

              The type of the object. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

          - `type AgentToolWebSearch struct{…}`

            Web search.

            - `AllowedDomains []string`

              Allowed search domains, or `null` when the search is unrestricted.

            - `ContextSize string`

              The amount of search context made available to the model. Defaults to `medium`.

              - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

              - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

              - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

            - `Location AgentToolWebSearchLocation`

              Approximate location used to localize search results, if provided.

              - `City string`

                The city name.

              - `Country string`

                The two-letter ISO country code, such as `US`.

              - `Region string`

                The region or state name.

              - `Timezone string`

                The IANA timezone, such as `America/Los_Angeles`.

            - `Mode string`

              The source used for web search results.

              - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

              - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

              - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

            - `Type WebSearch`

              The type of the object. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

          - `type AgentToolComputerUse struct{…}`

            Browser use in an OpenAI-hosted session.

            - `IncludeScreenshots bool`

              Whether computer tool outputs include screenshots.

            - `Type ComputerUse`

              The type of the object. Always `computer_use`.

              - `const ComputerUseComputerUse ComputerUse = "computer_use"`

      - `CreatedAt int64`

        The Unix timestamp, in seconds, when the session was created.

      - `Environment EnvironmentUnion`

        The execution environment for the session.

        - `type EnvironmentNone struct{…}`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type EnvironmentOpenAIHosted struct{…}`

          An environment hosted by OpenAI.

          - `ID string`

            The public ID of the environment.

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent.

          - `Desktop EnvironmentOpenAIHostedDesktop`

            The effective desktop configuration.

            - `Enabled bool`

              Whether the environment provisions a desktop and browser proxy.

          - `Files []HostedEnvironmentFileUnion`

            Files available in the environment, excluding their contents.

            - `type HostedEnvironmentFileID struct{…}`

              A file copied from the OpenAI Files API.

              - `ID string`

                The session-scoped ID of the file in the execution environment.

              - `FileID string`

                The ID of the uploaded file.

              - `Path string`

                The file's absolute path inside the environment.

              - `SizeBytes int64`

                The decoded file size in bytes.

              - `Type FileID`

                The type of the object. Always `file_id`.

                - `const FileIDFileID FileID = "file_id"`

            - `type HostedEnvironmentFileInline struct{…}`

              A file supplied inline when the session was created.

              - `ID string`

                The session-scoped ID of the file in the execution environment.

              - `Path string`

                The file's absolute path inside the environment.

              - `SizeBytes int64`

                The decoded file size in bytes.

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Network EnvironmentOpenAIHostedNetwork`

            The effective network access policy for the environment.

            - `Access string`

              The environment's network access mode.

              - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

                Allows unrestricted network access.

              - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

                Disables network access.

              - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

                Applies the configured domain restrictions.

            - `AllowedDomains []string`

              Domains the environment may access when network access is restricted.

          - `Packages EnvironmentOpenAIHostedPackages`

            Packages installed in the environment.

            - `Npm []string`

              npm packages installed globally in the environment.

            - `Python []string`

              Python packages installed in the environment.

            - `System []string`

              System packages installed in the environment.

          - `Plugins []HostedPlugin`

            Plugins installed in the environment, excluding their archive contents.

            - `Description string`

              The installed plugin description.

            - `Name string`

              The installed plugin name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

          - `Skills []HostedSkillUnion`

            Skills installed in the environment, excluding their archive contents.

            - `type HostedSkillReference struct{…}`

              A skill installed from the Skills API.

              - `Description string`

                The installed skill description.

              - `Name string`

                The installed skill name.

              - `SkillID string`

                The referenced skill ID.

              - `Type SkillReference`

                The type of the object. Always `skill_reference`.

                - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

              - `Version string`

                The concrete skill version installed for this session.

            - `type HostedSkillInline struct{…}`

              A skill installed from an inline ZIP archive.

              - `Description string`

                The installed skill description.

              - `Name string`

                The installed skill name.

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Type OpenAIHosted`

            The type of the object. Always `openai_hosted`.

            - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `ContainerSize string`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

            - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

            - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

        - `type EnvironmentSelfHosted struct{…}`

          An environment hosted by the application.

          - `ID string`

            The public ID of the environment.

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent.

          - `RemoteURL string`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `Type SelfHosted`

            The type of the object. Always `self_hosted`.

            - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

          - `WorkspaceDirectory string`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `Error string`

        The error that caused the session to fail, if any.

      - `LastActiveAt int64`

        The Unix timestamp, in seconds, when the session was last active.

      - `Metadata map[string, string]`

        Custom string key-value pairs attached to the session.

      - `Object AgentSession`

        The object type. Always `agent.session`.

        - `const AgentSessionAgentSession AgentSession = "agent.session"`

      - `RequiredActions []AgentSessionRequiredActionUnion`

        Actions that must be completed before the session can continue.

        - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

          Respond to a computer-use request.

          - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

            The information needed to render the request.

            - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

              A registered form awaiting the application's response.

              - `CredentialOrigin string`

                The registered form or frame origin where values will be entered.

              - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

                Controls to render. All submitted values are sensitive.

                - `ID string`

                  The field ID to submit as field_id in a fields entry.

                - `Label string`

                  The label to display beside the control.

                - `Required bool`

                  Whether this control requires a nonempty value.

                - `Type string`

                  The rendering type, such as email, password, or text.

              - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

                Sign-in methods. Empty for a plain form.

                - `ID string`

                  The option ID to submit as selected_option.

                - `FieldIDs []string`

                  IDs from the registered fields that this method accepts.

                - `Label string`

                  The method label to display.

              - `Reason string`

                Why the agent needs the user to sign in.

              - `Type BrowserAuthentication`

                The type of the object. Always `browser_authentication`.

                - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

            - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

              A browser origin awaiting the application's approval decision.

              - `Origin string`

                The origin the browser needs permission to access.

              - `Reason string`

                The browser's explanation for this request, or null when unavailable.

              - `Type BrowserOriginAccess`

                The type of the object. Always `browser_origin_access`.

                - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

          - `RequestID string`

            The registered request ID to echo when responding.

          - `TurnID string`

            The turn that requested approval.

          - `Type ComputerUseApprovalRequest`

            The type of the object. Always `computer_use_approval_request`.

            - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

        - `type AgentSessionRequiredActionFunctionCall struct{…}`

          Run a function tool and submit its result.

          - `Arguments any`

            The arguments supplied by the model.

          - `CallID string`

            The ID to include when submitting the function result.

          - `Name string`

            The function name.

          - `TurnID string`

            The ID of the turn that requested the function call.

          - `Type FunctionCall`

            The type of the object. Always `function_call`.

            - `const FunctionCallFunctionCall FunctionCall = "function_call"`

        - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

          Reconnect a session environment.

          - `EnvironmentID string`

            The ID of the environment to reconnect.

          - `Type EnvironmentConnection`

            The type of the object. Always `environment_connection`.

            - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

      - `Status AgentSessionStatus`

        The current status of the session.

        - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

          The session is processing a turn.

        - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

          The session is waiting for one or more required actions.

        - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

          The session failed.

      - `Usage TokenUsage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `InputTokens int64`

          The number of input tokens used by the agent.

        - `InputTokensDetails TokenUsageInputTokensDetails`

          A breakdown of the agent's input token usage.

          - `CachedTokens int64`

            The number of input tokens retrieved from the prompt cache.

        - `OutputTokens int64`

          The number of output tokens generated by the agent.

        - `OutputTokensDetails TokenUsageOutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `ReasoningTokens int64`

            The number of output tokens used for reasoning.

        - `TotalTokens int64`

          The total number of input and output tokens used by the agent.

      - `VaultIDs []string`

        The IDs of vaults made available to the session.

    - `Type AgentSessionCreated`

      The type of the object. Always `agent.session.created`.

      - `const AgentSessionCreatedAgentSessionCreated AgentSessionCreated = "agent.session.created"`

  - `type AgentSessionTurnCreatedEvent struct{…}`

    Emitted when a turn is created.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The turn at the time it was created.

      - `ID string`

        The ID of the turn.

      - `AgentID string`

        The ID of the agent that ran the turn.

      - `CompletedAt int64`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `CreatedAt int64`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `Error SessionTurnError`

        A customer-safe error. Non-null only for a failed turn.

        - `Code SessionTurnErrorCode`

          A stable, machine-readable failure category.

          - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

            The request exceeds the model's context window.

          - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

            The session has reached its usage budget.

          - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

            The organization has reached a usage, plan, or billing limit.

          - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

            The organization has no API credits remaining.

          - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

            The request exceeds the available rate limit.

          - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

            Flex processing is temporarily unavailable.

          - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

            The model service is temporarily overloaded.

          - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

            The request was rejected by a safety policy.

          - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

            The request was blocked by the safety systems.

          - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

            The request could not connect to the model service.

          - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

            The model service encountered an unexpected error.

          - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

            The API credentials are invalid or lack the required access.

          - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

            The request contains invalid input or configuration.

          - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

            The requested model or resource is unavailable.

          - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

            The request could not complete in its execution environment.

          - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

            The executor must be upgraded before it can run this turn.

          - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

            The session cannot accept additional input while a request is running.

          - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

            The request timed out before the model service responded.

          - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

            An unexpected internal error prevented the session request from completing.

        - `Message string`

          A customer-safe explanation of the failure.

      - `Object TurnObject`

        The object type. Always `agent.session.turn`.

        - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

      - `SessionID string`

        The ID of the session that owns the turn.

      - `StartedAt int64`

        The Unix timestamp, in seconds, when the turn started.

      - `Status TurnStatus`

        The current status of the turn.

        - `const TurnStatusQueued TurnStatus = "queued"`

          The turn is waiting to start.

        - `const TurnStatusInProgress TurnStatus = "in_progress"`

          The turn is in progress.

        - `const TurnStatusWaiting TurnStatus = "waiting"`

          The turn is waiting for external input.

        - `const TurnStatusCompleted TurnStatus = "completed"`

          The turn completed successfully.

        - `const TurnStatusFailed TurnStatus = "failed"`

          The turn failed.

        - `const TurnStatusCancelled TurnStatus = "cancelled"`

          The turn was cancelled.

      - `SubagentID string`

        The ID of the subagent that ran the turn, if applicable.

      - `Usage TokenUsage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCreated`

      The type of the object. Always `agent.session.turn.created`.

      - `const AgentSessionTurnCreatedAgentSessionTurnCreated AgentSessionTurnCreated = "agent.session.turn.created"`

  - `type AgentSessionTurnInProgressEvent struct{…}`

    Emitted when a turn starts running.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The turn at the time it started running.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnInProgress`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `const AgentSessionTurnInProgressAgentSessionTurnInProgress AgentSessionTurnInProgress = "agent.session.turn.in_progress"`

  - `type AgentSessionTurnCompletedEvent struct{…}`

    Emitted when a turn completes.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The completed turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCompleted`

      The type of the object. Always `agent.session.turn.completed`.

      - `const AgentSessionTurnCompletedAgentSessionTurnCompleted AgentSessionTurnCompleted = "agent.session.turn.completed"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnFailedEvent struct{…}`

    Emitted when a turn fails.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The failed turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnFailed`

      The type of the object. Always `agent.session.turn.failed`.

      - `const AgentSessionTurnFailedAgentSessionTurnFailed AgentSessionTurnFailed = "agent.session.turn.failed"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnCancelledEvent struct{…}`

    Emitted when a turn is cancelled.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The cancelled turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCancelled`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `const AgentSessionTurnCancelledAgentSessionTurnCancelled AgentSessionTurnCancelled = "agent.session.turn.cancelled"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnItemAddedEvent struct{…}`

    Emitted when an item is added to a turn.

    - `EventID string`

      The unique ID of the event.

    - `Item AgentSessionItemUnion`

      The item that was added.

      - `type AgentSessionMessage struct{…}`

        A user or assistant message recorded in a session.

        - `ID string`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `Content []AgentSessionMessageContentUnion`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `type AgentSessionMessageContentInputText struct{…}`

            Text supplied by the user.

            - `Text string`

              The text supplied by the user.

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type AgentSessionMessageContentInputImage struct{…}`

            An image supplied by the user.

            - `ImageURL string`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

          - `type AgentSessionMessageContentOutputText struct{…}`

            Text produced by the assistant.

            - `Text string`

              The text produced by the assistant.

            - `Type OutputText`

              The type of the object. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Phase AgentSessionMessagePhase`

          The phase of an assistant message. Null for user messages.

          - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

            Commentary produced while the agent works.

          - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

            The agent's final answer.

        - `Role AgentSessionMessageRole`

          The role of the message author.

          - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

          - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

        - `Status AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

            The item is in progress.

          - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

            The item is complete.

          - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

            The item stopped before completing.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Message`

          The item type. Always `message`.

          - `const MessageMessage Message = "message"`

      - `type AgentReasoningItem struct{…}`

        A reasoning item produced by the agent.

        - `ID string`

          The ID of the reasoning item.

        - `Status AgentOutputItemStatus`

          The status of the reasoning item.

        - `Summary []SummaryText`

          The reasoning summaries produced by the agent.

          - `Text string`

            The reasoning summary text.

          - `Type SummaryText`

            The content type. Always `summary_text`.

            - `const SummaryTextSummaryText SummaryText = "summary_text"`

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Reasoning`

          The item type. Always `reasoning`.

          - `const ReasoningReasoning Reasoning = "reasoning"`

      - `type AgentFunctionCallItem struct{…}`

        A function call produced by the agent.

        - `ID string`

          The ID of the function call item.

        - `Arguments any`

          The arguments to pass to the function.

        - `CallID string`

          The ID used to submit the function result.

        - `Name string`

          The name of the function to call.

        - `Status AgentFunctionCallStatus`

          The status of the function call.

          - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

            The call is in progress.

          - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

            The call completed successfully.

          - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

            The call failed.

          - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

            The call stopped before completing.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type FunctionCall`

          The item type. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionItemFunctionCallOutput struct{…}`

        The result supplied for a function call.

        - `ID string`

          The ID of the function call output item.

        - `CallID string`

          The ID of the function call that produced this output.

        - `Error string`

          The error message, if the call failed.

        - `Output AgentFunctionCallOutputUnion`

          The function result, if the call succeeded.

          - `string`

          - `type AgentFunctionCallOutputArray []InputContentUnion`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

        - `Status AgentFunctionCallStatus`

          The status of the function call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type FunctionCallOutput`

          The item type. Always `function_call_output`.

          - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

      - `type AgentSessionItemAgentMessage struct{…}`

        A message exchanged between agent threads.

        - `ID string`

          The ID of the message.

        - `Content []AgentContentUnion`

          The content exchanged between the agents.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

            - `Text string`

              The text produced by the agent.

            - `Type OutputText`

              The content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

            - `EncryptedContent string`

              The encrypted content payload.

            - `Type EncryptedContent`

              The content type. Always `encrypted_content`.

              - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

        - `RecipientAgentID string`

          The ID or name of the receiving agent.

        - `SenderAgentID string`

          The ID or name of the sending agent.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type AgentMessage`

          The item type. Always `agent_message`.

          - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

      - `type AgentMcpCallItem struct{…}`

        A call to a tool on an MCP server.

        - `ID string`

          The ID of the MCP call item.

        - `Arguments any`

          The arguments passed to the MCP tool.

        - `Error any`

          The error returned by the MCP tool, if any.

        - `Name string`

          The name of the MCP tool.

        - `Output any`

          The output returned by the MCP tool, if any.

        - `ServerLabel string`

          The label of the MCP server.

        - `Status AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type McpCall`

          The item type. Always `mcp_call`.

          - `const McpCallMcpCall McpCall = "mcp_call"`

      - `type AgentSessionItemComputerUseCall struct{…}`

        One execution of the platform-provided computer-use capability.

        - `ID string`

          The ID of the activity item.

        - `Output AgentSessionItemComputerUseCallOutput`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `ImageURL string`

            The complete JPEG image as a base64 data URL.

          - `Type ComputerScreenshot`

            The content type. Always `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

        - `Status AgentFunctionCallStatus`

          The execution status of the activity.

        - `Title string`

          A model-generated description of the activity, when available.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseCall`

          The item type. Always `computer_use_call`.

          - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

      - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

        A credential-free history record of the emitted login request.

        - `ID string`

          The stable history item ID.

        - `Request AgentSessionItemComputerUseApprovalRequestRequest`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `RequestID string`

        - `TurnID string`

        - `Type ComputerUseApprovalRequest`

          The item type. Always computer_use_approval_request.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

        A credential-free record of an admitted response, not proof of completion.

        - `ID string`

          The stable history item ID.

        - `RequestID string`

          The registered request answered by this item.

        - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

          The admitted response, without submitted credential values.

          - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

            - `Action Submit`

              - `const SubmitSubmit Submit = "submit"`

            - `SelectedOption string`

              The chosen sign-in method, or null when no options were offered.

            - `Type BrowserAuthentication`

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

            - `Action Cancel`

              - `const CancelCancel Cancel = "cancel"`

            - `Type BrowserAuthentication`

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseApprovalRequestResult`

          - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

      - `type AgentWebSearchCallItem struct{…}`

        A web search call produced by the agent.

        - `ID string`

          The ID of the web search call.

        - `Action WebSearchActionUnion`

          The action performed by the web search tool.

          - `type WebSearchActionSearch struct{…}`

            A search query or group of search queries.

            - `Queries []string`

              The search queries, when multiple queries were used.

            - `Query string`

              The search query, when a single query was used.

            - `Type Search`

              The type of the object. Always `search`.

              - `const SearchSearch Search = "search"`

          - `type WebSearchActionOpenPage struct{…}`

            Opens a web page.

            - `Type OpenPage`

              The type of the object. Always `open_page`.

              - `const OpenPageOpenPage OpenPage = "open_page"`

            - `URL string`

              The URL of the page that was opened.

          - `type WebSearchActionFindInPage struct{…}`

            Finds text within a web page.

            - `Pattern string`

              The text pattern that was searched for.

            - `Type FindInPage`

              The type of the object. Always `find_in_page`.

              - `const FindInPageFindInPage FindInPage = "find_in_page"`

            - `URL string`

              The URL of the page that was searched.

          - `type WebSearchActionOther struct{…}`

            Another web search action.

            - `Type Other`

              The type of the object. Always `other`.

              - `const OtherOther Other = "other"`

        - `Status AgentOutputItemStatus`

          The status of the web search call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type WebSearchCall`

          The item type. Always `web_search_call`.

          - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

      - `type AgentCommandExecutionItem struct{…}`

        A command execution produced by the agent.

        - `ID string`

          The ID of the command execution item.

        - `Command string`

          The command that was executed.

        - `Cwd string`

          The working directory used to execute the command.

        - `DurationMs int64`

          The command duration in milliseconds.

        - `ExitCode int64`

          The process exit code, if the command completed.

        - `Output string`

          The command output, if available.

        - `Status AgentFunctionCallStatus`

          The status of the command execution.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CommandExecution`

          The item type. Always `command_execution`.

          - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

      - `type AgentCreateSubagentCallItem struct{…}`

        A request to spawn a subagent.

        - `ID string`

          The ID of the tool call item.

        - `AgentID string`

          The ID of the agent that requested the subagent.

        - `Content []AgentContentUnion`

          The task given to the spawned agent.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

        - `Model string`

          The model requested for the spawned agent.

        - `ReasoningEffort string`

          The reasoning effort requested for the spawned agent.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CreateSubagentCall`

          The item type. Always `create_subagent_call`.

          - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

            The current public item type.

      - `type AgentSendSubagentInputCallItem struct{…}`

        A request to send input to another agent.

        - `ID string`

          The ID of the tool call item.

        - `Content []AgentContentUnion`

          The input sent to the receiving agent.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

        - `RecipientAgentID string`

          The ID of the agent receiving the input.

        - `SenderAgentID string`

          The ID of the agent sending the input.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type SendSubagentInputCall`

          The item type. Always `send_subagent_input_call`.

          - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

            The current public item type.

      - `type AgentResumeSubagentCallItem struct{…}`

        A request to resume a subagent.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to resume.

        - `SenderAgentID string`

          The ID of the agent requesting the resume.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ResumeSubagentCall`

          The item type. Always `resume_subagent_call`.

          - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

            The current public item type.

      - `type AgentWaitForSubagentsCallItem struct{…}`

        A request to wait for one or more subagents.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentIDs []string`

          The IDs of the agents to wait for.

        - `SenderAgentID string`

          The ID of the agent waiting for results.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type WaitForSubagentsCall`

          The item type. Always `wait_for_subagents_call`.

          - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

            The current public item type.

      - `type AgentInterruptSubagentCallItem struct{…}`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to interrupt.

        - `SenderAgentID string`

          The ID of the agent requesting the interrupt.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type InterruptSubagentCall`

          The item type. Always `interrupt_subagent_call`.

          - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

            The current public item type.

      - `type AgentCloseSubagentCallItem struct{…}`

        A request to close a subagent.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to close.

        - `SenderAgentID string`

          The ID of the agent requesting the close.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CloseSubagentCall`

          The item type. Always `close_subagent_call`.

          - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

            The current public item type.

    - `OutputIndex int64`

      The index of the item in the turn output, when the item is agent output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnItemAdded`

      The type of the object. Always `agent.session.turn.item.added`.

      - `const AgentSessionTurnItemAddedAgentSessionTurnItemAdded AgentSessionTurnItemAdded = "agent.session.turn.item.added"`

  - `type AgentSessionIdleEvent struct{…}`

    Emitted when a session becomes idle.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that became idle.

    - `Type AgentSessionIdle`

      The type of the object. Always `agent.session.idle`.

      - `const AgentSessionIdleAgentSessionIdle AgentSessionIdle = "agent.session.idle"`

  - `type AgentSessionInProgressEvent struct{…}`

    Emitted when a session starts processing a turn.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that started processing.

    - `Type AgentSessionInProgress`

      The type of the object. Always `agent.session.in_progress`.

      - `const AgentSessionInProgressAgentSessionInProgress AgentSessionInProgress = "agent.session.in_progress"`

  - `type AgentSessionRequiresActionEvent struct{…}`

    Emitted when a session is waiting for one or more required actions.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session and its current required actions.

    - `Type AgentSessionRequiresAction`

      The type of the object. Always `agent.session.requires_action`.

      - `const AgentSessionRequiresActionAgentSessionRequiresAction AgentSessionRequiresAction = "agent.session.requires_action"`

  - `type AgentSessionFailedEvent struct{…}`

    Emitted when a session fails.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The failed session.

    - `Type AgentSessionFailed`

      The type of the object. Always `agent.session.failed`.

      - `const AgentSessionFailedAgentSessionFailed AgentSessionFailed = "agent.session.failed"`

  - `type AgentSessionEnvironmentPendingEvent struct{…}`

    Emitted while a session environment is being prepared.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentPending`

      The type of the object. Always `agent.session.environment.pending`.

      - `const AgentSessionEnvironmentPendingAgentSessionEnvironmentPending AgentSessionEnvironmentPending = "agent.session.environment.pending"`

  - `type AgentSessionEnvironmentConnectedEvent struct{…}`

    Emitted when a session environment connects.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentConnected`

      The type of the object. Always `agent.session.environment.connected`.

      - `const AgentSessionEnvironmentConnectedAgentSessionEnvironmentConnected AgentSessionEnvironmentConnected = "agent.session.environment.connected"`

  - `type AgentSessionEnvironmentDisconnectedEvent struct{…}`

    Emitted when a session environment disconnects.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentDisconnected`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `const AgentSessionEnvironmentDisconnectedAgentSessionEnvironmentDisconnected AgentSessionEnvironmentDisconnected = "agent.session.environment.disconnected"`

  - `type AgentSessionEnvironmentFailedEvent struct{…}`

    Emitted when a session environment fails.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentFailed`

      The type of the object. Always `agent.session.environment.failed`.

      - `const AgentSessionEnvironmentFailedAgentSessionEnvironmentFailed AgentSessionEnvironmentFailed = "agent.session.environment.failed"`

  - `type AgentSessionSubagentCreatedEvent struct{…}`

    Emitted when a subagent is created.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that was created.

      - `ID string`

        The ID of the subagent.

      - `ClosedAt int64`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `Instructions []AgentContentUnion`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

      - `Name string`

        The runner-assigned nickname, or null when unavailable.

      - `Object SubagentObject`

        The object type. Always `agent.session.subagent`.

        - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

      - `OpenedAt int64`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `ParentAgentID string`

        The ID of the agent that created this subagent.

      - `SessionID string`

        The ID of the session that owns the subagent.

      - `Status SubagentStatus`

        The current status of the subagent.

        - `const SubagentStatusActive SubagentStatus = "active"`

          The subagent remains available, including while idle between turns.

        - `const SubagentStatusClosed SubagentStatus = "closed"`

          The subagent is closed.

    - `Type AgentSessionSubagentCreated`

      The type of the object. Always `agent.session.subagent.created`.

      - `const AgentSessionSubagentCreatedAgentSessionSubagentCreated AgentSessionSubagentCreated = "agent.session.subagent.created"`

  - `type AgentSessionSubagentActiveEvent struct{…}`

    Emitted when a closed subagent successfully resumes.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that resumed.

    - `Type AgentSessionSubagentActive`

      The type of the object. Always `agent.session.subagent.active`.

      - `const AgentSessionSubagentActiveAgentSessionSubagentActive AgentSessionSubagentActive = "agent.session.subagent.active"`

  - `type AgentSessionSubagentClosedEvent struct{…}`

    Emitted when a subagent is closed.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that was closed.

    - `Type AgentSessionSubagentClosed`

      The type of the object. Always `agent.session.subagent.closed`.

      - `const AgentSessionSubagentClosedAgentSessionSubagentClosed AgentSessionSubagentClosed = "agent.session.subagent.closed"`

  - `type AgentSessionTurnItemDoneEvent struct{…}`

    Emitted when an output item is complete.

    - `EventID string`

      The unique ID of the event.

    - `Item AgentOutputItemUnion`

      The completed output item.

      - `type AgentSessionAssistantMessage struct{…}`

        An assistant message produced by the agent.

        - `ID string`

          The ID of the message.

        - `Content []OutputText`

          The content of the message.

          - `Text string`

            The text produced by the agent.

          - `Type OutputText`

            The content type. Always `output_text`.

        - `Phase AgentSessionAssistantMessagePhase`

          The phase of the assistant message.

          - `const AgentSessionAssistantMessagePhaseCommentary AgentSessionAssistantMessagePhase = "commentary"`

            Commentary produced while the agent works.

          - `const AgentSessionAssistantMessagePhaseFinalAnswer AgentSessionAssistantMessagePhase = "final_answer"`

            The agent's final answer.

        - `Role Assistant`

          The role of the message author. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `Status AgentOutputItemStatus`

          The status of the message.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Message`

          The item type. Always `message`.

          - `const MessageMessage Message = "message"`

      - `type AgentReasoningItem struct{…}`

        A reasoning item produced by the agent.

      - `type AgentFunctionCallItem struct{…}`

        A function call produced by the agent.

      - `type AgentMcpCallItem struct{…}`

        A call to a tool on an MCP server.

      - `type AgentOutputItemComputerUseCall struct{…}`

        One execution of the platform-provided computer-use capability.

        - `ID string`

          The ID of the activity item.

        - `Output AgentOutputItemComputerUseCallOutput`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `ImageURL string`

            The complete JPEG image as a base64 data URL.

          - `Type ComputerScreenshot`

            The content type. Always `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

        - `Status AgentFunctionCallStatus`

          The execution status of the activity.

        - `Title string`

          A model-generated description of the activity, when available.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseCall`

          The item type. Always `computer_use_call`.

          - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

      - `type AgentOutputItemComputerUseApprovalRequest struct{…}`

        A credential-free history record of the emitted login request.

        - `ID string`

          The stable history item ID.

        - `Request AgentOutputItemComputerUseApprovalRequestRequest`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentOutputItemComputerUseApprovalRequestRequestField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentOutputItemComputerUseApprovalRequestRequestOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `RequestID string`

        - `TurnID string`

        - `Type ComputerUseApprovalRequest`

          The item type. Always computer_use_approval_request.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentWebSearchCallItem struct{…}`

        A web search call produced by the agent.

      - `type AgentCommandExecutionItem struct{…}`

        A command execution produced by the agent.

      - `type AgentCreateSubagentCallItem struct{…}`

        A request to spawn a subagent.

      - `type AgentSendSubagentInputCallItem struct{…}`

        A request to send input to another agent.

      - `type AgentResumeSubagentCallItem struct{…}`

        A request to resume a subagent.

      - `type AgentWaitForSubagentsCallItem struct{…}`

        A request to wait for one or more subagents.

      - `type AgentInterruptSubagentCallItem struct{…}`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `type AgentCloseSubagentCallItem struct{…}`

        A request to close a subagent.

    - `OutputIndex int64`

      The index of the output item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnItemDone`

      The type of the object. Always `agent.session.turn.item.done`.

      - `const AgentSessionTurnItemDoneAgentSessionTurnItemDone AgentSessionTurnItemDone = "agent.session.turn.item.done"`

  - `type AgentSessionTurnContentPartAddedEvent struct{…}`

    Emitted when an output text content part is added.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part OutputText`

      The initial content part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnContentPartAdded`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `const AgentSessionTurnContentPartAddedAgentSessionTurnContentPartAdded AgentSessionTurnContentPartAdded = "agent.session.turn.content_part.added"`

  - `type AgentSessionTurnContentPartDoneEvent struct{…}`

    Emitted when an output content part is complete.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part OutputText`

      The completed content part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnContentPartDone`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `const AgentSessionTurnContentPartDoneAgentSessionTurnContentPartDone AgentSessionTurnContentPartDone = "agent.session.turn.content_part.done"`

  - `type AgentSessionTurnOutputTextDeltaEvent struct{…}`

    Emitted when text is appended to an output text content part.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `Delta string`

      The text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnOutputTextDelta`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `const AgentSessionTurnOutputTextDeltaAgentSessionTurnOutputTextDelta AgentSessionTurnOutputTextDelta = "agent.session.turn.output_text.delta"`

  - `type AgentSessionTurnOutputTextDoneEvent struct{…}`

    Emitted when an output text content part is complete.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Text string`

      The complete output text.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnOutputTextDone`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `const AgentSessionTurnOutputTextDoneAgentSessionTurnOutputTextDone AgentSessionTurnOutputTextDone = "agent.session.turn.output_text.done"`

  - `type AgentSessionTurnReasoningSummaryPartAddedEvent struct{…}`

    Emitted when a reasoning summary content part is added.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part SummaryText`

      The initial summary part.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryPartAdded`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `const AgentSessionTurnReasoningSummaryPartAddedAgentSessionTurnReasoningSummaryPartAdded AgentSessionTurnReasoningSummaryPartAdded = "agent.session.turn.reasoning_summary_part.added"`

  - `type AgentSessionTurnReasoningSummaryPartDoneEvent struct{…}`

    Emitted when a reasoning summary part is complete.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part SummaryText`

      The completed summary part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Status Incomplete`

      Present as `incomplete` when summary generation was interrupted.

      - `const IncompleteIncomplete Incomplete = "incomplete"`

    - `SummaryIndex int64`

      The index of the summary part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryPartDone`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `const AgentSessionTurnReasoningSummaryPartDoneAgentSessionTurnReasoningSummaryPartDone AgentSessionTurnReasoningSummaryPartDone = "agent.session.turn.reasoning_summary_part.done"`

  - `type AgentSessionTurnReasoningSummaryTextDeltaEvent struct{…}`

    Emitted when text is appended to a reasoning summary.

    - `Delta string`

      The summary text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryTextDelta`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `const AgentSessionTurnReasoningSummaryTextDeltaAgentSessionTurnReasoningSummaryTextDelta AgentSessionTurnReasoningSummaryTextDelta = "agent.session.turn.reasoning_summary_text.delta"`

  - `type AgentSessionTurnReasoningSummaryTextDoneEvent struct{…}`

    Emitted when a reasoning summary content part is complete.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `Text string`

      The complete reasoning summary text.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryTextDone`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `const AgentSessionTurnReasoningSummaryTextDoneAgentSessionTurnReasoningSummaryTextDone AgentSessionTurnReasoningSummaryTextDone = "agent.session.turn.reasoning_summary_text.done"`

### Agent Session Failed Event

- `type AgentSessionFailedEvent struct{…}`

  Emitted when a session fails.

  - `EventID string`

    The unique ID of the event.

  - `Session AgentSession`

    The failed session.

    - `ID string`

      The ID of the session.

    - `Agent AgentSessionAgent`

      The agent running in the session.

      - `ID string`

        The ID of the agent.

      - `Instructions string`

        Custom instructions appended to the agent's default base instructions.

      - `Model string`

        The model used by the agent.

      - `MultiAgent MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Name string`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `Reasoning AgentReasoning`

        The agent's reasoning configuration.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

        - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

        - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

        - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

        - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

        - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

      - `Text AgentText`

        Configuration for text generated by the agent.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Tools available to the agent.

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

          - `Name string`

            The name of the function.

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

              - `Command string`

                The command used to start the MCP server.

              - `Cwd string`

                The working directory used to start the MCP server.

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

            - `Country string`

              The two-letter ISO country code, such as `US`.

            - `Region string`

              The region or state name.

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `CreatedAt int64`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment EnvironmentUnion`

      The execution environment for the session.

      - `type EnvironmentNone struct{…}`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type EnvironmentOpenAIHosted struct{…}`

        An environment hosted by OpenAI.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `Desktop EnvironmentOpenAIHostedDesktop`

          The effective desktop configuration.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `Files []HostedEnvironmentFileUnion`

          Files available in the environment, excluding their contents.

          - `type HostedEnvironmentFileID struct{…}`

            A file copied from the OpenAI Files API.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `FileID string`

              The ID of the uploaded file.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type HostedEnvironmentFileInline struct{…}`

            A file supplied inline when the session was created.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

        - `Packages EnvironmentOpenAIHostedPackages`

          Packages installed in the environment.

          - `Npm []string`

            npm packages installed globally in the environment.

          - `Python []string`

            Python packages installed in the environment.

          - `System []string`

            System packages installed in the environment.

        - `Plugins []HostedPlugin`

          Plugins installed in the environment, excluding their archive contents.

          - `Description string`

            The installed plugin description.

          - `Name string`

            The installed plugin name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []HostedSkillUnion`

          Skills installed in the environment, excluding their archive contents.

          - `type HostedSkillReference struct{…}`

            A skill installed from the Skills API.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `SkillID string`

              The referenced skill ID.

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The concrete skill version installed for this session.

          - `type HostedSkillInline struct{…}`

            A skill installed from an inline ZIP archive.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `ContainerSize string`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

          - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

      - `type EnvironmentSelfHosted struct{…}`

        An environment hosted by the application.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `RemoteURL string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Error string`

      The error that caused the session to fail, if any.

    - `LastActiveAt int64`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the session.

    - `Object AgentSession`

      The object type. Always `agent.session`.

      - `const AgentSessionAgentSession AgentSession = "agent.session"`

    - `RequiredActions []AgentSessionRequiredActionUnion`

      Actions that must be completed before the session can continue.

      - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

        Respond to a computer-use request.

        - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

          The information needed to render the request.

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

            A registered form awaiting the application's response.

            - `CredentialOrigin string`

              The registered form or frame origin where values will be entered.

            - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

              Controls to render. All submitted values are sensitive.

              - `ID string`

                The field ID to submit as field_id in a fields entry.

              - `Label string`

                The label to display beside the control.

              - `Required bool`

                Whether this control requires a nonempty value.

              - `Type string`

                The rendering type, such as email, password, or text.

            - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

              Sign-in methods. Empty for a plain form.

              - `ID string`

                The option ID to submit as selected_option.

              - `FieldIDs []string`

                IDs from the registered fields that this method accepts.

              - `Label string`

                The method label to display.

            - `Reason string`

              Why the agent needs the user to sign in.

            - `Type BrowserAuthentication`

              The type of the object. Always `browser_authentication`.

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

            A browser origin awaiting the application's approval decision.

            - `Origin string`

              The origin the browser needs permission to access.

            - `Reason string`

              The browser's explanation for this request, or null when unavailable.

            - `Type BrowserOriginAccess`

              The type of the object. Always `browser_origin_access`.

              - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

        - `RequestID string`

          The registered request ID to echo when responding.

        - `TurnID string`

          The turn that requested approval.

        - `Type ComputerUseApprovalRequest`

          The type of the object. Always `computer_use_approval_request`.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionRequiredActionFunctionCall struct{…}`

        Run a function tool and submit its result.

        - `Arguments any`

          The arguments supplied by the model.

        - `CallID string`

          The ID to include when submitting the function result.

        - `Name string`

          The function name.

        - `TurnID string`

          The ID of the turn that requested the function call.

        - `Type FunctionCall`

          The type of the object. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

        Reconnect a session environment.

        - `EnvironmentID string`

          The ID of the environment to reconnect.

        - `Type EnvironmentConnection`

          The type of the object. Always `environment_connection`.

          - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

    - `Status AgentSessionStatus`

      The current status of the session.

      - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

        The session is processing a turn.

      - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

        The session is waiting for one or more required actions.

      - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

        The session failed.

    - `Usage TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

    - `VaultIDs []string`

      The IDs of vaults made available to the session.

  - `Type AgentSessionFailed`

    The type of the object. Always `agent.session.failed`.

    - `const AgentSessionFailedAgentSessionFailed AgentSessionFailed = "agent.session.failed"`

### Agent Session Idle Event

- `type AgentSessionIdleEvent struct{…}`

  Emitted when a session becomes idle.

  - `EventID string`

    The unique ID of the event.

  - `Session AgentSession`

    The session that became idle.

    - `ID string`

      The ID of the session.

    - `Agent AgentSessionAgent`

      The agent running in the session.

      - `ID string`

        The ID of the agent.

      - `Instructions string`

        Custom instructions appended to the agent's default base instructions.

      - `Model string`

        The model used by the agent.

      - `MultiAgent MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Name string`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `Reasoning AgentReasoning`

        The agent's reasoning configuration.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

        - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

        - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

        - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

        - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

        - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

      - `Text AgentText`

        Configuration for text generated by the agent.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Tools available to the agent.

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

          - `Name string`

            The name of the function.

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

              - `Command string`

                The command used to start the MCP server.

              - `Cwd string`

                The working directory used to start the MCP server.

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

            - `Country string`

              The two-letter ISO country code, such as `US`.

            - `Region string`

              The region or state name.

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `CreatedAt int64`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment EnvironmentUnion`

      The execution environment for the session.

      - `type EnvironmentNone struct{…}`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type EnvironmentOpenAIHosted struct{…}`

        An environment hosted by OpenAI.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `Desktop EnvironmentOpenAIHostedDesktop`

          The effective desktop configuration.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `Files []HostedEnvironmentFileUnion`

          Files available in the environment, excluding their contents.

          - `type HostedEnvironmentFileID struct{…}`

            A file copied from the OpenAI Files API.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `FileID string`

              The ID of the uploaded file.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type HostedEnvironmentFileInline struct{…}`

            A file supplied inline when the session was created.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

        - `Packages EnvironmentOpenAIHostedPackages`

          Packages installed in the environment.

          - `Npm []string`

            npm packages installed globally in the environment.

          - `Python []string`

            Python packages installed in the environment.

          - `System []string`

            System packages installed in the environment.

        - `Plugins []HostedPlugin`

          Plugins installed in the environment, excluding their archive contents.

          - `Description string`

            The installed plugin description.

          - `Name string`

            The installed plugin name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []HostedSkillUnion`

          Skills installed in the environment, excluding their archive contents.

          - `type HostedSkillReference struct{…}`

            A skill installed from the Skills API.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `SkillID string`

              The referenced skill ID.

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The concrete skill version installed for this session.

          - `type HostedSkillInline struct{…}`

            A skill installed from an inline ZIP archive.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `ContainerSize string`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

          - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

      - `type EnvironmentSelfHosted struct{…}`

        An environment hosted by the application.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `RemoteURL string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Error string`

      The error that caused the session to fail, if any.

    - `LastActiveAt int64`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the session.

    - `Object AgentSession`

      The object type. Always `agent.session`.

      - `const AgentSessionAgentSession AgentSession = "agent.session"`

    - `RequiredActions []AgentSessionRequiredActionUnion`

      Actions that must be completed before the session can continue.

      - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

        Respond to a computer-use request.

        - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

          The information needed to render the request.

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

            A registered form awaiting the application's response.

            - `CredentialOrigin string`

              The registered form or frame origin where values will be entered.

            - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

              Controls to render. All submitted values are sensitive.

              - `ID string`

                The field ID to submit as field_id in a fields entry.

              - `Label string`

                The label to display beside the control.

              - `Required bool`

                Whether this control requires a nonempty value.

              - `Type string`

                The rendering type, such as email, password, or text.

            - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

              Sign-in methods. Empty for a plain form.

              - `ID string`

                The option ID to submit as selected_option.

              - `FieldIDs []string`

                IDs from the registered fields that this method accepts.

              - `Label string`

                The method label to display.

            - `Reason string`

              Why the agent needs the user to sign in.

            - `Type BrowserAuthentication`

              The type of the object. Always `browser_authentication`.

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

            A browser origin awaiting the application's approval decision.

            - `Origin string`

              The origin the browser needs permission to access.

            - `Reason string`

              The browser's explanation for this request, or null when unavailable.

            - `Type BrowserOriginAccess`

              The type of the object. Always `browser_origin_access`.

              - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

        - `RequestID string`

          The registered request ID to echo when responding.

        - `TurnID string`

          The turn that requested approval.

        - `Type ComputerUseApprovalRequest`

          The type of the object. Always `computer_use_approval_request`.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionRequiredActionFunctionCall struct{…}`

        Run a function tool and submit its result.

        - `Arguments any`

          The arguments supplied by the model.

        - `CallID string`

          The ID to include when submitting the function result.

        - `Name string`

          The function name.

        - `TurnID string`

          The ID of the turn that requested the function call.

        - `Type FunctionCall`

          The type of the object. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

        Reconnect a session environment.

        - `EnvironmentID string`

          The ID of the environment to reconnect.

        - `Type EnvironmentConnection`

          The type of the object. Always `environment_connection`.

          - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

    - `Status AgentSessionStatus`

      The current status of the session.

      - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

        The session is processing a turn.

      - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

        The session is waiting for one or more required actions.

      - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

        The session failed.

    - `Usage TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

    - `VaultIDs []string`

      The IDs of vaults made available to the session.

  - `Type AgentSessionIdle`

    The type of the object. Always `agent.session.idle`.

    - `const AgentSessionIdleAgentSessionIdle AgentSessionIdle = "agent.session.idle"`

### Agent Session In Progress Event

- `type AgentSessionInProgressEvent struct{…}`

  Emitted when a session starts processing a turn.

  - `EventID string`

    The unique ID of the event.

  - `Session AgentSession`

    The session that started processing.

    - `ID string`

      The ID of the session.

    - `Agent AgentSessionAgent`

      The agent running in the session.

      - `ID string`

        The ID of the agent.

      - `Instructions string`

        Custom instructions appended to the agent's default base instructions.

      - `Model string`

        The model used by the agent.

      - `MultiAgent MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Name string`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `Reasoning AgentReasoning`

        The agent's reasoning configuration.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

        - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

        - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

        - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

        - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

        - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

      - `Text AgentText`

        Configuration for text generated by the agent.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Tools available to the agent.

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

          - `Name string`

            The name of the function.

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

              - `Command string`

                The command used to start the MCP server.

              - `Cwd string`

                The working directory used to start the MCP server.

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

            - `Country string`

              The two-letter ISO country code, such as `US`.

            - `Region string`

              The region or state name.

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `CreatedAt int64`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment EnvironmentUnion`

      The execution environment for the session.

      - `type EnvironmentNone struct{…}`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type EnvironmentOpenAIHosted struct{…}`

        An environment hosted by OpenAI.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `Desktop EnvironmentOpenAIHostedDesktop`

          The effective desktop configuration.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `Files []HostedEnvironmentFileUnion`

          Files available in the environment, excluding their contents.

          - `type HostedEnvironmentFileID struct{…}`

            A file copied from the OpenAI Files API.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `FileID string`

              The ID of the uploaded file.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type HostedEnvironmentFileInline struct{…}`

            A file supplied inline when the session was created.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

        - `Packages EnvironmentOpenAIHostedPackages`

          Packages installed in the environment.

          - `Npm []string`

            npm packages installed globally in the environment.

          - `Python []string`

            Python packages installed in the environment.

          - `System []string`

            System packages installed in the environment.

        - `Plugins []HostedPlugin`

          Plugins installed in the environment, excluding their archive contents.

          - `Description string`

            The installed plugin description.

          - `Name string`

            The installed plugin name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []HostedSkillUnion`

          Skills installed in the environment, excluding their archive contents.

          - `type HostedSkillReference struct{…}`

            A skill installed from the Skills API.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `SkillID string`

              The referenced skill ID.

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The concrete skill version installed for this session.

          - `type HostedSkillInline struct{…}`

            A skill installed from an inline ZIP archive.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `ContainerSize string`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

          - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

      - `type EnvironmentSelfHosted struct{…}`

        An environment hosted by the application.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `RemoteURL string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Error string`

      The error that caused the session to fail, if any.

    - `LastActiveAt int64`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the session.

    - `Object AgentSession`

      The object type. Always `agent.session`.

      - `const AgentSessionAgentSession AgentSession = "agent.session"`

    - `RequiredActions []AgentSessionRequiredActionUnion`

      Actions that must be completed before the session can continue.

      - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

        Respond to a computer-use request.

        - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

          The information needed to render the request.

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

            A registered form awaiting the application's response.

            - `CredentialOrigin string`

              The registered form or frame origin where values will be entered.

            - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

              Controls to render. All submitted values are sensitive.

              - `ID string`

                The field ID to submit as field_id in a fields entry.

              - `Label string`

                The label to display beside the control.

              - `Required bool`

                Whether this control requires a nonempty value.

              - `Type string`

                The rendering type, such as email, password, or text.

            - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

              Sign-in methods. Empty for a plain form.

              - `ID string`

                The option ID to submit as selected_option.

              - `FieldIDs []string`

                IDs from the registered fields that this method accepts.

              - `Label string`

                The method label to display.

            - `Reason string`

              Why the agent needs the user to sign in.

            - `Type BrowserAuthentication`

              The type of the object. Always `browser_authentication`.

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

            A browser origin awaiting the application's approval decision.

            - `Origin string`

              The origin the browser needs permission to access.

            - `Reason string`

              The browser's explanation for this request, or null when unavailable.

            - `Type BrowserOriginAccess`

              The type of the object. Always `browser_origin_access`.

              - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

        - `RequestID string`

          The registered request ID to echo when responding.

        - `TurnID string`

          The turn that requested approval.

        - `Type ComputerUseApprovalRequest`

          The type of the object. Always `computer_use_approval_request`.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionRequiredActionFunctionCall struct{…}`

        Run a function tool and submit its result.

        - `Arguments any`

          The arguments supplied by the model.

        - `CallID string`

          The ID to include when submitting the function result.

        - `Name string`

          The function name.

        - `TurnID string`

          The ID of the turn that requested the function call.

        - `Type FunctionCall`

          The type of the object. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

        Reconnect a session environment.

        - `EnvironmentID string`

          The ID of the environment to reconnect.

        - `Type EnvironmentConnection`

          The type of the object. Always `environment_connection`.

          - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

    - `Status AgentSessionStatus`

      The current status of the session.

      - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

        The session is processing a turn.

      - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

        The session is waiting for one or more required actions.

      - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

        The session failed.

    - `Usage TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

    - `VaultIDs []string`

      The IDs of vaults made available to the session.

  - `Type AgentSessionInProgress`

    The type of the object. Always `agent.session.in_progress`.

    - `const AgentSessionInProgressAgentSessionInProgress AgentSessionInProgress = "agent.session.in_progress"`

### Agent Session Input Message Param

- `type AgentSessionInputMessageParamResp struct{…}`

  A user message submitted to a session.

  - `Content []InputContentParamUnionResp`

    The content of the message.

    - `InputContentParamInputTextResp`

      - `Text string`

        The text sent to the model.

      - `Type InputText`

        The type of the object. Always `input_text`.

        - `const InputTextInputText InputText = "input_text"`

    - `InputContentParamInputImageResp`

      - `ImageURL string`

        The URL of the image sent to the model.

      - `Type InputImage`

        The type of the object. Always `input_image`.

        - `const InputImageInputImage InputImage = "input_image"`

  - `Role User`

    The role of the message author. Always `user`.

    - `const UserUser User = "user"`

  - `Type AgentSessionInputMessageParamType`

    The type of the input item. Always `message`.

    - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

### Agent Session Input Param

- `type AgentSessionInputParamUnionResp interface{…}`

  Input submitted to an existing session.

  - `AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResultResp`

    - `RequestID string`

      The registered request ID from the required action.

    - `Response AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponseUnionResp`

      The response for this request type.

      - `type AgentBrowserAuthenticationSubmitParamResp struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `Fields []AgentBrowserAuthenticationSubmitParamFieldResp`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `FieldID string`

            The field ID from the required action.

          - `Value string`

            The value to enter into the registered control.

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `SelectedOption string`

          The chosen method. Required when the required action contains options.

      - `type AgentBrowserAuthenticationCancelParamResp struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentBrowserOriginAccessParamResp struct{…}`

        - `Decision AgentBrowserOriginAccessParamDecision`

          Whether to allow, deny, or cancel the requested origin access.

          - `const AgentBrowserOriginAccessParamDecisionApprove AgentBrowserOriginAccessParamDecision = "approve"`

            Allow the browser to access this origin.

          - `const AgentBrowserOriginAccessParamDecisionDeny AgentBrowserOriginAccessParamDecision = "deny"`

            Deny access to this origin.

          - `const AgentBrowserOriginAccessParamDecisionCancel AgentBrowserOriginAccessParamDecision = "cancel"`

            Dismiss this request without approving access.

        - `Type BrowserOriginAccess`

          - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

    - `Type AgentSessionInputComputerUseApprovalRequestResult`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `const AgentSessionInputComputerUseApprovalRequestResultAgentSessionInputComputerUseApprovalRequestResult AgentSessionInputComputerUseApprovalRequestResult = "agent.session.input.computer_use_approval_request_result"`

  - `AgentSessionInputParamAgentSessionInputMessageResp`

    - `Input []AgentSessionInputMessageParamResp`

      The user messages to add to the session.

      - `Content []InputContentParamUnionResp`

        The content of the message.

        - `InputContentParamInputTextResp`

          - `Text string`

            The text sent to the model.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `InputContentParamInputImageResp`

          - `ImageURL string`

            The URL of the image sent to the model.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

      - `Role User`

        The role of the message author. Always `user`.

        - `const UserUser User = "user"`

      - `Type AgentSessionInputMessageParamType`

        The type of the input item. Always `message`.

        - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

    - `Type AgentSessionInputMessage`

      The type of the object. Always `agent.session.input.message`.

      - `const AgentSessionInputMessageAgentSessionInputMessage AgentSessionInputMessage = "agent.session.input.message"`

  - `AgentSessionInputParamAgentSessionInputCancelResp`

    - `Type AgentSessionInputCancel`

      The type of the object. Always `agent.session.input.cancel`.

      - `const AgentSessionInputCancelAgentSessionInputCancel AgentSessionInputCancel = "agent.session.input.cancel"`

  - `AgentSessionInputParamAgentSessionInputToolResultResp`

    - `CallID string`

      The ID of the function call.

    - `Success bool`

      Whether the function call succeeded.

    - `TurnID string`

      The ID of the turn that requested the function call.

    - `Type AgentSessionInputToolResult`

      The type of the object. Always `agent.session.input.tool_result`.

      - `const AgentSessionInputToolResultAgentSessionInputToolResult AgentSessionInputToolResult = "agent.session.input.tool_result"`

    - `Error string`

      The error message when the call failed.

    - `Output AgentFunctionCallOutputParamUnionResp`

      The function result when the call succeeded.

      - `string`

      - `[]InputContentParamUnionResp`

        - `InputContentParamInputTextResp`

        - `InputContentParamInputImageResp`

### Agent Session Item

- `type AgentSessionItemUnion interface{…}`

  An item associated with a session turn.

  - `type AgentSessionMessage struct{…}`

    A user or assistant message recorded in a session.

    - `ID string`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `Content []AgentSessionMessageContentUnion`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `type AgentSessionMessageContentInputText struct{…}`

        Text supplied by the user.

        - `Text string`

          The text supplied by the user.

        - `Type InputText`

          The type of the object. Always `input_text`.

          - `const InputTextInputText InputText = "input_text"`

      - `type AgentSessionMessageContentInputImage struct{…}`

        An image supplied by the user.

        - `ImageURL string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `Type InputImage`

          The type of the object. Always `input_image`.

          - `const InputImageInputImage InputImage = "input_image"`

      - `type AgentSessionMessageContentOutputText struct{…}`

        Text produced by the assistant.

        - `Text string`

          The text produced by the assistant.

        - `Type OutputText`

          The type of the object. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

    - `Phase AgentSessionMessagePhase`

      The phase of an assistant message. Null for user messages.

      - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

        Commentary produced while the agent works.

      - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

        The agent's final answer.

    - `Role AgentSessionMessageRole`

      The role of the message author.

      - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

      - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

    - `Status AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

        The item is in progress.

      - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

        The item is complete.

      - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

        The item stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

    - `Name string`

      The name of the function to call.

    - `Status AgentFunctionCallStatus`

      The status of the function call.

      - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

        The call is in progress.

      - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

        The call completed successfully.

      - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

        The call failed.

      - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

        The call stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentSessionItemFunctionCallOutput struct{…}`

    The result supplied for a function call.

    - `ID string`

      The ID of the function call output item.

    - `CallID string`

      The ID of the function call that produced this output.

    - `Error string`

      The error message, if the call failed.

    - `Output AgentFunctionCallOutputUnion`

      The function result, if the call succeeded.

      - `string`

      - `type AgentFunctionCallOutputArray []InputContentUnion`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

    - `Status AgentFunctionCallStatus`

      The status of the function call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCallOutput`

      The item type. Always `function_call_output`.

      - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

  - `type AgentSessionItemAgentMessage struct{…}`

    A message exchanged between agent threads.

    - `ID string`

      The ID of the message.

    - `Content []AgentContentUnion`

      The content exchanged between the agents.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `RecipientAgentID string`

      The ID or name of the receiving agent.

    - `SenderAgentID string`

      The ID or name of the sending agent.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type AgentMessage`

      The item type. Always `agent_message`.

      - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

  - `type AgentMcpCallItem struct{…}`

    A call to a tool on an MCP server.

    - `ID string`

      The ID of the MCP call item.

    - `Arguments any`

      The arguments passed to the MCP tool.

    - `Error any`

      The error returned by the MCP tool, if any.

    - `Name string`

      The name of the MCP tool.

    - `Output any`

      The output returned by the MCP tool, if any.

    - `ServerLabel string`

      The label of the MCP server.

    - `Status AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type McpCall`

      The item type. Always `mcp_call`.

      - `const McpCallMcpCall McpCall = "mcp_call"`

  - `type AgentSessionItemComputerUseCall struct{…}`

    One execution of the platform-provided computer-use capability.

    - `ID string`

      The ID of the activity item.

    - `Output AgentSessionItemComputerUseCallOutput`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `ImageURL string`

        The complete JPEG image as a base64 data URL.

      - `Type ComputerScreenshot`

        The content type. Always `computer_screenshot`.

        - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

    - `Status AgentFunctionCallStatus`

      The execution status of the activity.

    - `Title string`

      A model-generated description of the activity, when available.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseCall`

      The item type. Always `computer_use_call`.

      - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

  - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

    A credential-free history record of the emitted login request.

    - `ID string`

      The stable history item ID.

    - `Request AgentSessionItemComputerUseApprovalRequestRequest`

      A registered form awaiting the application's response.

      - `CredentialOrigin string`

        The registered form or frame origin where values will be entered.

      - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

        Controls to render. All submitted values are sensitive.

        - `ID string`

          The field ID to submit as field_id in a fields entry.

        - `Label string`

          The label to display beside the control.

        - `Required bool`

          Whether this control requires a nonempty value.

        - `Type string`

          The rendering type, such as email, password, or text.

      - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

        Sign-in methods. Empty for a plain form.

        - `ID string`

          The option ID to submit as selected_option.

        - `FieldIDs []string`

          IDs from the registered fields that this method accepts.

        - `Label string`

          The method label to display.

      - `Reason string`

        Why the agent needs the user to sign in.

      - `Type BrowserAuthentication`

        The type of the object. Always `browser_authentication`.

        - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `RequestID string`

    - `TurnID string`

    - `Type ComputerUseApprovalRequest`

      The item type. Always computer_use_approval_request.

      - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

  - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

    A credential-free record of an admitted response, not proof of completion.

    - `ID string`

      The stable history item ID.

    - `RequestID string`

      The registered request answered by this item.

    - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

      The admitted response, without submitted credential values.

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

        - `Action Submit`

          - `const SubmitSubmit Submit = "submit"`

        - `SelectedOption string`

          The chosen sign-in method, or null when no options were offered.

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

        - `Action Cancel`

          - `const CancelCancel Cancel = "cancel"`

        - `Type BrowserAuthentication`

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ComputerUseApprovalRequestResult`

      - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

  - `type AgentWebSearchCallItem struct{…}`

    A web search call produced by the agent.

    - `ID string`

      The ID of the web search call.

    - `Action WebSearchActionUnion`

      The action performed by the web search tool.

      - `type WebSearchActionSearch struct{…}`

        A search query or group of search queries.

        - `Queries []string`

          The search queries, when multiple queries were used.

        - `Query string`

          The search query, when a single query was used.

        - `Type Search`

          The type of the object. Always `search`.

          - `const SearchSearch Search = "search"`

      - `type WebSearchActionOpenPage struct{…}`

        Opens a web page.

        - `Type OpenPage`

          The type of the object. Always `open_page`.

          - `const OpenPageOpenPage OpenPage = "open_page"`

        - `URL string`

          The URL of the page that was opened.

      - `type WebSearchActionFindInPage struct{…}`

        Finds text within a web page.

        - `Pattern string`

          The text pattern that was searched for.

        - `Type FindInPage`

          The type of the object. Always `find_in_page`.

          - `const FindInPageFindInPage FindInPage = "find_in_page"`

        - `URL string`

          The URL of the page that was searched.

      - `type WebSearchActionOther struct{…}`

        Another web search action.

        - `Type Other`

          The type of the object. Always `other`.

          - `const OtherOther Other = "other"`

    - `Status AgentOutputItemStatus`

      The status of the web search call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WebSearchCall`

      The item type. Always `web_search_call`.

      - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

  - `type AgentCommandExecutionItem struct{…}`

    A command execution produced by the agent.

    - `ID string`

      The ID of the command execution item.

    - `Command string`

      The command that was executed.

    - `Cwd string`

      The working directory used to execute the command.

    - `DurationMs int64`

      The command duration in milliseconds.

    - `ExitCode int64`

      The process exit code, if the command completed.

    - `Output string`

      The command output, if available.

    - `Status AgentFunctionCallStatus`

      The status of the command execution.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CommandExecution`

      The item type. Always `command_execution`.

      - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

  - `type AgentCreateSubagentCallItem struct{…}`

    A request to spawn a subagent.

    - `ID string`

      The ID of the tool call item.

    - `AgentID string`

      The ID of the agent that requested the subagent.

    - `Content []AgentContentUnion`

      The task given to the spawned agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `Model string`

      The model requested for the spawned agent.

    - `ReasoningEffort string`

      The reasoning effort requested for the spawned agent.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CreateSubagentCall`

      The item type. Always `create_subagent_call`.

      - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

        The current public item type.

  - `type AgentSendSubagentInputCallItem struct{…}`

    A request to send input to another agent.

    - `ID string`

      The ID of the tool call item.

    - `Content []AgentContentUnion`

      The input sent to the receiving agent.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

    - `RecipientAgentID string`

      The ID of the agent receiving the input.

    - `SenderAgentID string`

      The ID of the agent sending the input.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type SendSubagentInputCall`

      The item type. Always `send_subagent_input_call`.

      - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

        The current public item type.

  - `type AgentResumeSubagentCallItem struct{…}`

    A request to resume a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to resume.

    - `SenderAgentID string`

      The ID of the agent requesting the resume.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type ResumeSubagentCall`

      The item type. Always `resume_subagent_call`.

      - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

        The current public item type.

  - `type AgentWaitForSubagentsCallItem struct{…}`

    A request to wait for one or more subagents.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentIDs []string`

      The IDs of the agents to wait for.

    - `SenderAgentID string`

      The ID of the agent waiting for results.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type WaitForSubagentsCall`

      The item type. Always `wait_for_subagents_call`.

      - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

        The current public item type.

  - `type AgentInterruptSubagentCallItem struct{…}`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to interrupt.

    - `SenderAgentID string`

      The ID of the agent requesting the interrupt.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type InterruptSubagentCall`

      The item type. Always `interrupt_subagent_call`.

      - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

        The current public item type.

  - `type AgentCloseSubagentCallItem struct{…}`

    A request to close a subagent.

    - `ID string`

      The ID of the tool call item.

    - `RecipientAgentID string`

      The ID of the agent to close.

    - `SenderAgentID string`

      The ID of the agent requesting the close.

    - `Status AgentFunctionCallStatus`

      The status of the tool call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type CloseSubagentCall`

      The item type. Always `close_subagent_call`.

      - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

        The current public item type.

### Agent Session Message

- `type AgentSessionMessage struct{…}`

  A user or assistant message recorded in a session.

  - `ID string`

    The ID of this item, or null for legacy user messages whose ID was not recorded.

  - `Content []AgentSessionMessageContentUnion`

    The content of the message. User messages contain input text or images; assistant messages contain output text.

    - `type AgentSessionMessageContentInputText struct{…}`

      Text supplied by the user.

      - `Text string`

        The text supplied by the user.

      - `Type InputText`

        The type of the object. Always `input_text`.

        - `const InputTextInputText InputText = "input_text"`

    - `type AgentSessionMessageContentInputImage struct{…}`

      An image supplied by the user.

      - `ImageURL string`

        The URL of the image supplied by the user, which may be a base64-encoded data URL.

      - `Type InputImage`

        The type of the object. Always `input_image`.

        - `const InputImageInputImage InputImage = "input_image"`

    - `type AgentSessionMessageContentOutputText struct{…}`

      Text produced by the assistant.

      - `Text string`

        The text produced by the assistant.

      - `Type OutputText`

        The type of the object. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

  - `Phase AgentSessionMessagePhase`

    The phase of an assistant message. Null for user messages.

    - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

      Commentary produced while the agent works.

    - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

      The agent's final answer.

  - `Role AgentSessionMessageRole`

    The role of the message author.

    - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

    - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

  - `Status AgentOutputItemStatus`

    The status of the message. User messages are always `completed`.

    - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

      The item is in progress.

    - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

      The item is complete.

    - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

      The item stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type Message`

    The item type. Always `message`.

    - `const MessageMessage Message = "message"`

### Agent Session Message Content

- `type AgentSessionMessageContentUnion interface{…}`

  A content part in a session message.

  - `type AgentSessionMessageContentInputText struct{…}`

    Text supplied by the user.

    - `Text string`

      The text supplied by the user.

    - `Type InputText`

      The type of the object. Always `input_text`.

      - `const InputTextInputText InputText = "input_text"`

  - `type AgentSessionMessageContentInputImage struct{…}`

    An image supplied by the user.

    - `ImageURL string`

      The URL of the image supplied by the user, which may be a base64-encoded data URL.

    - `Type InputImage`

      The type of the object. Always `input_image`.

      - `const InputImageInputImage InputImage = "input_image"`

  - `type AgentSessionMessageContentOutputText struct{…}`

    Text produced by the assistant.

    - `Text string`

      The text produced by the assistant.

    - `Type OutputText`

      The type of the object. Always `output_text`.

      - `const OutputTextOutputText OutputText = "output_text"`

### Agent Session Requires Action Event

- `type AgentSessionRequiresActionEvent struct{…}`

  Emitted when a session is waiting for one or more required actions.

  - `EventID string`

    The unique ID of the event.

  - `Session AgentSession`

    The session and its current required actions.

    - `ID string`

      The ID of the session.

    - `Agent AgentSessionAgent`

      The agent running in the session.

      - `ID string`

        The ID of the agent.

      - `Instructions string`

        Custom instructions appended to the agent's default base instructions.

      - `Model string`

        The model used by the agent.

      - `MultiAgent MultiAgentConfig`

        Configuration for creating and coordinating subagents.

        - `Enabled bool`

          Whether subagent tools are enabled. Defaults to false.

        - `MaxConcurrentSubagents int64`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Name string`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `Reasoning AgentReasoning`

        The agent's reasoning configuration.

        - `Effort AgentReasoningEffort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

          - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

          - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

          - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

          - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

          - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

          - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

        - `Summary AgentReasoningSummary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

            Returns a concise reasoning summary when supported.

          - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

            Returns a detailed reasoning summary when supported.

          - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier string`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

        - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

        - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

        - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

        - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

        - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

      - `Text AgentText`

        Configuration for text generated by the agent.

        - `Format TextFormatUnion`

          The effective output format. Defaults to ordinary text.

          - `type TextFormatText struct{…}`

            Generates ordinary text without a structured-output constraint.

            - `Type Text`

              The type of the object. Always `text`.

              - `const TextText Text = "text"`

          - `type TextFormatJSONSchema struct{…}`

            Constrains generated text to a JSON Schema.

            - `Schema map[string, any]`

              The JSON Schema that generated text must match.

            - `Type JSONSchema`

              The type of the object. Always `json_schema`.

              - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

        - `Verbosity AgentTextVerbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

          - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

          - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

      - `Tools []AgentToolUnion`

        Tools available to the agent.

        - `type AgentToolFunction struct{…}`

          A function defined by the application.

          - `DeferLoading bool`

            Whether the function is deferred and discovered through tool search.

          - `Description string`

            A description of what the function does.

          - `Name string`

            The name of the function.

          - `Parameters map[string, any]`

            A JSON Schema object describing the function's arguments.

          - `Type Function`

            The type of the object. Always `function`.

            - `const FunctionFunction Function = "function"`

        - `type AgentToolProgrammaticToolCalling struct{…}`

          Enables calling tools from model-generated code.

          - `Enabled bool`

            Whether tools can be called from model-generated code.

          - `Type ProgrammaticToolCalling`

            The type of the object. Always `programmatic_tool_calling`.

            - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `type AgentToolMcp struct{…}`

          Tools provided by a remote MCP server.

          - `AllowedTools []string`

            The MCP tools the agent may call.

          - `ConnectionOrigin string`

            Where outbound MCP HTTP connections originate.

            - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

            - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

          - `CredentialID string`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata map[string, any]`

            Metadata included with requests to this MCP server.

          - `Required bool`

            Whether this MCP server must initialize before the first turn.

          - `ServerLabel string`

            A label used to identify the MCP server in tool calls.

          - `Transport McpTransportUnion`

            The transport used to connect to the MCP server.

            - `type McpTransportHTTP struct{…}`

              Connects to an MCP server over HTTP.

              - `ServerURL string`

                The URL of the MCP server.

              - `Type HTTP`

                The type of the object. Always `http`.

                - `const HTTPHTTP HTTP = "http"`

            - `type McpTransportStdio struct{…}`

              Starts an MCP server as a local process.

              - `Args []string`

                Arguments passed to the MCP server command.

              - `Command string`

                The command used to start the MCP server.

              - `Cwd string`

                The working directory used to start the MCP server.

              - `EnvVars []string`

                Environment variable names inherited from the execution environment.

              - `Type Stdio`

                The type of the object. Always `stdio`.

                - `const StdioStdio Stdio = "stdio"`

          - `Type Mcp`

            The type of the object. Always `mcp`.

            - `const McpMcp Mcp = "mcp"`

        - `type AgentToolWebSearch struct{…}`

          Web search.

          - `AllowedDomains []string`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize string`

            The amount of search context made available to the model. Defaults to `medium`.

            - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

            - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

            - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

          - `Location AgentToolWebSearchLocation`

            Approximate location used to localize search results, if provided.

            - `City string`

              The city name.

            - `Country string`

              The two-letter ISO country code, such as `US`.

            - `Region string`

              The region or state name.

            - `Timezone string`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode string`

            The source used for web search results.

            - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

            - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

            - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

          - `Type WebSearch`

            The type of the object. Always `web_search`.

            - `const WebSearchWebSearch WebSearch = "web_search"`

        - `type AgentToolComputerUse struct{…}`

          Browser use in an OpenAI-hosted session.

          - `IncludeScreenshots bool`

            Whether computer tool outputs include screenshots.

          - `Type ComputerUse`

            The type of the object. Always `computer_use`.

            - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `CreatedAt int64`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment EnvironmentUnion`

      The execution environment for the session.

      - `type EnvironmentNone struct{…}`

        The session talks to CCA without selecting or provisioning an execution environment.

        - `Type None`

          The type of the object. Always `none`.

          - `const NoneNone None = "none"`

      - `type EnvironmentOpenAIHosted struct{…}`

        An environment hosted by OpenAI.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `Desktop EnvironmentOpenAIHostedDesktop`

          The effective desktop configuration.

          - `Enabled bool`

            Whether the environment provisions a desktop and browser proxy.

        - `Files []HostedEnvironmentFileUnion`

          Files available in the environment, excluding their contents.

          - `type HostedEnvironmentFileID struct{…}`

            A file copied from the OpenAI Files API.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `FileID string`

              The ID of the uploaded file.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type FileID`

              The type of the object. Always `file_id`.

              - `const FileIDFileID FileID = "file_id"`

          - `type HostedEnvironmentFileInline struct{…}`

            A file supplied inline when the session was created.

            - `ID string`

              The session-scoped ID of the file in the execution environment.

            - `Path string`

              The file's absolute path inside the environment.

            - `SizeBytes int64`

              The decoded file size in bytes.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Network EnvironmentOpenAIHostedNetwork`

          The effective network access policy for the environment.

          - `Access string`

            The environment's network access mode.

            - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

              Allows unrestricted network access.

            - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

              Disables network access.

            - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

              Applies the configured domain restrictions.

          - `AllowedDomains []string`

            Domains the environment may access when network access is restricted.

        - `Packages EnvironmentOpenAIHostedPackages`

          Packages installed in the environment.

          - `Npm []string`

            npm packages installed globally in the environment.

          - `Python []string`

            Python packages installed in the environment.

          - `System []string`

            System packages installed in the environment.

        - `Plugins []HostedPlugin`

          Plugins installed in the environment, excluding their archive contents.

          - `Description string`

            The installed plugin description.

          - `Name string`

            The installed plugin name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

        - `Skills []HostedSkillUnion`

          Skills installed in the environment, excluding their archive contents.

          - `type HostedSkillReference struct{…}`

            A skill installed from the Skills API.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `SkillID string`

              The referenced skill ID.

            - `Type SkillReference`

              The type of the object. Always `skill_reference`.

              - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

            - `Version string`

              The concrete skill version installed for this session.

          - `type HostedSkillInline struct{…}`

            A skill installed from an inline ZIP archive.

            - `Description string`

              The installed skill description.

            - `Name string`

              The installed skill name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

        - `Type OpenAIHosted`

          The type of the object. Always `openai_hosted`.

          - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

        - `ContainerSize string`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

          - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

          - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

      - `type EnvironmentSelfHosted struct{…}`

        An environment hosted by the application.

        - `ID string`

          The public ID of the environment.

        - `CapabilityDirectories []string`

          Directories that contain capabilities exposed to the agent.

        - `RemoteURL string`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `Type SelfHosted`

          The type of the object. Always `self_hosted`.

          - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

        - `WorkspaceDirectory string`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Error string`

      The error that caused the session to fail, if any.

    - `LastActiveAt int64`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata map[string, string]`

      Custom string key-value pairs attached to the session.

    - `Object AgentSession`

      The object type. Always `agent.session`.

      - `const AgentSessionAgentSession AgentSession = "agent.session"`

    - `RequiredActions []AgentSessionRequiredActionUnion`

      Actions that must be completed before the session can continue.

      - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

        Respond to a computer-use request.

        - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

          The information needed to render the request.

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

            A registered form awaiting the application's response.

            - `CredentialOrigin string`

              The registered form or frame origin where values will be entered.

            - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

              Controls to render. All submitted values are sensitive.

              - `ID string`

                The field ID to submit as field_id in a fields entry.

              - `Label string`

                The label to display beside the control.

              - `Required bool`

                Whether this control requires a nonempty value.

              - `Type string`

                The rendering type, such as email, password, or text.

            - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

              Sign-in methods. Empty for a plain form.

              - `ID string`

                The option ID to submit as selected_option.

              - `FieldIDs []string`

                IDs from the registered fields that this method accepts.

              - `Label string`

                The method label to display.

            - `Reason string`

              Why the agent needs the user to sign in.

            - `Type BrowserAuthentication`

              The type of the object. Always `browser_authentication`.

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

            A browser origin awaiting the application's approval decision.

            - `Origin string`

              The origin the browser needs permission to access.

            - `Reason string`

              The browser's explanation for this request, or null when unavailable.

            - `Type BrowserOriginAccess`

              The type of the object. Always `browser_origin_access`.

              - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

        - `RequestID string`

          The registered request ID to echo when responding.

        - `TurnID string`

          The turn that requested approval.

        - `Type ComputerUseApprovalRequest`

          The type of the object. Always `computer_use_approval_request`.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionRequiredActionFunctionCall struct{…}`

        Run a function tool and submit its result.

        - `Arguments any`

          The arguments supplied by the model.

        - `CallID string`

          The ID to include when submitting the function result.

        - `Name string`

          The function name.

        - `TurnID string`

          The ID of the turn that requested the function call.

        - `Type FunctionCall`

          The type of the object. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

        Reconnect a session environment.

        - `EnvironmentID string`

          The ID of the environment to reconnect.

        - `Type EnvironmentConnection`

          The type of the object. Always `environment_connection`.

          - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

    - `Status AgentSessionStatus`

      The current status of the session.

      - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

        The session is processing a turn.

      - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

        The session is waiting for one or more required actions.

      - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

        The session failed.

    - `Usage TokenUsage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

    - `VaultIDs []string`

      The IDs of vaults made available to the session.

  - `Type AgentSessionRequiresAction`

    The type of the object. Always `agent.session.requires_action`.

    - `const AgentSessionRequiresActionAgentSessionRequiresAction AgentSessionRequiresAction = "agent.session.requires_action"`

### Agent Session Subagent Active Event

- `type AgentSessionSubagentActiveEvent struct{…}`

  Emitted when a closed subagent successfully resumes.

  - `EventID string`

    The unique ID of the event.

  - `Subagent Subagent`

    The subagent that resumed.

    - `ID string`

      The ID of the subagent.

    - `ClosedAt int64`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Instructions []AgentContentUnion`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `Name string`

      The runner-assigned nickname, or null when unavailable.

    - `Object SubagentObject`

      The object type. Always `agent.session.subagent`.

      - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

    - `OpenedAt int64`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `ParentAgentID string`

      The ID of the agent that created this subagent.

    - `SessionID string`

      The ID of the session that owns the subagent.

    - `Status SubagentStatus`

      The current status of the subagent.

      - `const SubagentStatusActive SubagentStatus = "active"`

        The subagent remains available, including while idle between turns.

      - `const SubagentStatusClosed SubagentStatus = "closed"`

        The subagent is closed.

  - `Type AgentSessionSubagentActive`

    The type of the object. Always `agent.session.subagent.active`.

    - `const AgentSessionSubagentActiveAgentSessionSubagentActive AgentSessionSubagentActive = "agent.session.subagent.active"`

### Agent Session Subagent Closed Event

- `type AgentSessionSubagentClosedEvent struct{…}`

  Emitted when a subagent is closed.

  - `EventID string`

    The unique ID of the event.

  - `Subagent Subagent`

    The subagent that was closed.

    - `ID string`

      The ID of the subagent.

    - `ClosedAt int64`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Instructions []AgentContentUnion`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `Name string`

      The runner-assigned nickname, or null when unavailable.

    - `Object SubagentObject`

      The object type. Always `agent.session.subagent`.

      - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

    - `OpenedAt int64`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `ParentAgentID string`

      The ID of the agent that created this subagent.

    - `SessionID string`

      The ID of the session that owns the subagent.

    - `Status SubagentStatus`

      The current status of the subagent.

      - `const SubagentStatusActive SubagentStatus = "active"`

        The subagent remains available, including while idle between turns.

      - `const SubagentStatusClosed SubagentStatus = "closed"`

        The subagent is closed.

  - `Type AgentSessionSubagentClosed`

    The type of the object. Always `agent.session.subagent.closed`.

    - `const AgentSessionSubagentClosedAgentSessionSubagentClosed AgentSessionSubagentClosed = "agent.session.subagent.closed"`

### Agent Session Subagent Created Event

- `type AgentSessionSubagentCreatedEvent struct{…}`

  Emitted when a subagent is created.

  - `EventID string`

    The unique ID of the event.

  - `Subagent Subagent`

    The subagent that was created.

    - `ID string`

      The ID of the subagent.

    - `ClosedAt int64`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Instructions []AgentContentUnion`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `type OutputText struct{…}`

        A text content part produced by the agent.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `type AgentContentEncryptedContent struct{…}`

        Encrypted content exchanged between agents.

        - `EncryptedContent string`

          The encrypted content payload.

        - `Type EncryptedContent`

          The content type. Always `encrypted_content`.

          - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

    - `Name string`

      The runner-assigned nickname, or null when unavailable.

    - `Object SubagentObject`

      The object type. Always `agent.session.subagent`.

      - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

    - `OpenedAt int64`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `ParentAgentID string`

      The ID of the agent that created this subagent.

    - `SessionID string`

      The ID of the session that owns the subagent.

    - `Status SubagentStatus`

      The current status of the subagent.

      - `const SubagentStatusActive SubagentStatus = "active"`

        The subagent remains available, including while idle between turns.

      - `const SubagentStatusClosed SubagentStatus = "closed"`

        The subagent is closed.

  - `Type AgentSessionSubagentCreated`

    The type of the object. Always `agent.session.subagent.created`.

    - `const AgentSessionSubagentCreatedAgentSessionSubagentCreated AgentSessionSubagentCreated = "agent.session.subagent.created"`

### Agent Session Turn Cancelled Event

- `type AgentSessionTurnCancelledEvent struct{…}`

  Emitted when a turn is cancelled.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Turn Turn`

    The cancelled turn.

    - `ID string`

      The ID of the turn.

    - `AgentID string`

      The ID of the agent that ran the turn.

    - `CompletedAt int64`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `CreatedAt int64`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Error SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `Code SessionTurnErrorCode`

        A stable, machine-readable failure category.

        - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

          The request exceeds the model's context window.

        - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

          The session has reached its usage budget.

        - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

          The model service is temporarily overloaded.

        - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

          The request was rejected by a safety policy.

        - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

          The request could not connect to the model service.

        - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

          The model service encountered an unexpected error.

        - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

          The API credentials are invalid or lack the required access.

        - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

          The request contains invalid input or configuration.

        - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

          The requested model or resource is unavailable.

        - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

          The request could not complete in its execution environment.

        - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

          The request timed out before the model service responded.

        - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `Message string`

        A customer-safe explanation of the failure.

    - `Object TurnObject`

      The object type. Always `agent.session.turn`.

      - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

    - `SessionID string`

      The ID of the session that owns the turn.

    - `StartedAt int64`

      The Unix timestamp, in seconds, when the turn started.

    - `Status TurnStatus`

      The current status of the turn.

      - `const TurnStatusQueued TurnStatus = "queued"`

        The turn is waiting to start.

      - `const TurnStatusInProgress TurnStatus = "in_progress"`

        The turn is in progress.

      - `const TurnStatusWaiting TurnStatus = "waiting"`

        The turn is waiting for external input.

      - `const TurnStatusCompleted TurnStatus = "completed"`

        The turn completed successfully.

      - `const TurnStatusFailed TurnStatus = "failed"`

        The turn failed.

      - `const TurnStatusCancelled TurnStatus = "cancelled"`

        The turn was cancelled.

    - `SubagentID string`

      The ID of the subagent that ran the turn, if applicable.

    - `Usage TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

  - `TurnID string`

    The ID of the turn associated with the event.

  - `Type AgentSessionTurnCancelled`

    The type of the object. Always `agent.session.turn.cancelled`.

    - `const AgentSessionTurnCancelledAgentSessionTurnCancelled AgentSessionTurnCancelled = "agent.session.turn.cancelled"`

  - `Usage TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Completed Event

- `type AgentSessionTurnCompletedEvent struct{…}`

  Emitted when a turn completes.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Turn Turn`

    The completed turn.

    - `ID string`

      The ID of the turn.

    - `AgentID string`

      The ID of the agent that ran the turn.

    - `CompletedAt int64`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `CreatedAt int64`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Error SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `Code SessionTurnErrorCode`

        A stable, machine-readable failure category.

        - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

          The request exceeds the model's context window.

        - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

          The session has reached its usage budget.

        - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

          The model service is temporarily overloaded.

        - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

          The request was rejected by a safety policy.

        - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

          The request could not connect to the model service.

        - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

          The model service encountered an unexpected error.

        - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

          The API credentials are invalid or lack the required access.

        - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

          The request contains invalid input or configuration.

        - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

          The requested model or resource is unavailable.

        - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

          The request could not complete in its execution environment.

        - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

          The request timed out before the model service responded.

        - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `Message string`

        A customer-safe explanation of the failure.

    - `Object TurnObject`

      The object type. Always `agent.session.turn`.

      - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

    - `SessionID string`

      The ID of the session that owns the turn.

    - `StartedAt int64`

      The Unix timestamp, in seconds, when the turn started.

    - `Status TurnStatus`

      The current status of the turn.

      - `const TurnStatusQueued TurnStatus = "queued"`

        The turn is waiting to start.

      - `const TurnStatusInProgress TurnStatus = "in_progress"`

        The turn is in progress.

      - `const TurnStatusWaiting TurnStatus = "waiting"`

        The turn is waiting for external input.

      - `const TurnStatusCompleted TurnStatus = "completed"`

        The turn completed successfully.

      - `const TurnStatusFailed TurnStatus = "failed"`

        The turn failed.

      - `const TurnStatusCancelled TurnStatus = "cancelled"`

        The turn was cancelled.

    - `SubagentID string`

      The ID of the subagent that ran the turn, if applicable.

    - `Usage TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

  - `TurnID string`

    The ID of the turn associated with the event.

  - `Type AgentSessionTurnCompleted`

    The type of the object. Always `agent.session.turn.completed`.

    - `const AgentSessionTurnCompletedAgentSessionTurnCompleted AgentSessionTurnCompleted = "agent.session.turn.completed"`

  - `Usage TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Content Part Added Event

- `type AgentSessionTurnContentPartAddedEvent struct{…}`

  Emitted when an output text content part is added.

  - `ContentIndex int64`

    The index of the content part in the message.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the message item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `Part OutputText`

    The initial content part.

    - `Text string`

      The text produced by the agent.

    - `Type OutputText`

      The content type. Always `output_text`.

      - `const OutputTextOutputText OutputText = "output_text"`

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnContentPartAdded`

    The type of the object. Always `agent.session.turn.content_part.added`.

    - `const AgentSessionTurnContentPartAddedAgentSessionTurnContentPartAdded AgentSessionTurnContentPartAdded = "agent.session.turn.content_part.added"`

### Agent Session Turn Content Part Done Event

- `type AgentSessionTurnContentPartDoneEvent struct{…}`

  Emitted when an output content part is complete.

  - `ContentIndex int64`

    The index of the content part in the message.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the message item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `Part OutputText`

    The completed content part.

    - `Text string`

      The text produced by the agent.

    - `Type OutputText`

      The content type. Always `output_text`.

      - `const OutputTextOutputText OutputText = "output_text"`

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnContentPartDone`

    The type of the object. Always `agent.session.turn.content_part.done`.

    - `const AgentSessionTurnContentPartDoneAgentSessionTurnContentPartDone AgentSessionTurnContentPartDone = "agent.session.turn.content_part.done"`

### Agent Session Turn Created Event

- `type AgentSessionTurnCreatedEvent struct{…}`

  Emitted when a turn is created.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Turn Turn`

    The turn at the time it was created.

    - `ID string`

      The ID of the turn.

    - `AgentID string`

      The ID of the agent that ran the turn.

    - `CompletedAt int64`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `CreatedAt int64`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Error SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `Code SessionTurnErrorCode`

        A stable, machine-readable failure category.

        - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

          The request exceeds the model's context window.

        - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

          The session has reached its usage budget.

        - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

          The model service is temporarily overloaded.

        - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

          The request was rejected by a safety policy.

        - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

          The request could not connect to the model service.

        - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

          The model service encountered an unexpected error.

        - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

          The API credentials are invalid or lack the required access.

        - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

          The request contains invalid input or configuration.

        - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

          The requested model or resource is unavailable.

        - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

          The request could not complete in its execution environment.

        - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

          The request timed out before the model service responded.

        - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `Message string`

        A customer-safe explanation of the failure.

    - `Object TurnObject`

      The object type. Always `agent.session.turn`.

      - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

    - `SessionID string`

      The ID of the session that owns the turn.

    - `StartedAt int64`

      The Unix timestamp, in seconds, when the turn started.

    - `Status TurnStatus`

      The current status of the turn.

      - `const TurnStatusQueued TurnStatus = "queued"`

        The turn is waiting to start.

      - `const TurnStatusInProgress TurnStatus = "in_progress"`

        The turn is in progress.

      - `const TurnStatusWaiting TurnStatus = "waiting"`

        The turn is waiting for external input.

      - `const TurnStatusCompleted TurnStatus = "completed"`

        The turn completed successfully.

      - `const TurnStatusFailed TurnStatus = "failed"`

        The turn failed.

      - `const TurnStatusCancelled TurnStatus = "cancelled"`

        The turn was cancelled.

    - `SubagentID string`

      The ID of the subagent that ran the turn, if applicable.

    - `Usage TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

  - `TurnID string`

    The ID of the turn associated with the event.

  - `Type AgentSessionTurnCreated`

    The type of the object. Always `agent.session.turn.created`.

    - `const AgentSessionTurnCreatedAgentSessionTurnCreated AgentSessionTurnCreated = "agent.session.turn.created"`

### Agent Session Turn Failed Event

- `type AgentSessionTurnFailedEvent struct{…}`

  Emitted when a turn fails.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Turn Turn`

    The failed turn.

    - `ID string`

      The ID of the turn.

    - `AgentID string`

      The ID of the agent that ran the turn.

    - `CompletedAt int64`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `CreatedAt int64`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Error SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `Code SessionTurnErrorCode`

        A stable, machine-readable failure category.

        - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

          The request exceeds the model's context window.

        - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

          The session has reached its usage budget.

        - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

          The model service is temporarily overloaded.

        - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

          The request was rejected by a safety policy.

        - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

          The request could not connect to the model service.

        - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

          The model service encountered an unexpected error.

        - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

          The API credentials are invalid or lack the required access.

        - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

          The request contains invalid input or configuration.

        - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

          The requested model or resource is unavailable.

        - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

          The request could not complete in its execution environment.

        - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

          The request timed out before the model service responded.

        - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `Message string`

        A customer-safe explanation of the failure.

    - `Object TurnObject`

      The object type. Always `agent.session.turn`.

      - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

    - `SessionID string`

      The ID of the session that owns the turn.

    - `StartedAt int64`

      The Unix timestamp, in seconds, when the turn started.

    - `Status TurnStatus`

      The current status of the turn.

      - `const TurnStatusQueued TurnStatus = "queued"`

        The turn is waiting to start.

      - `const TurnStatusInProgress TurnStatus = "in_progress"`

        The turn is in progress.

      - `const TurnStatusWaiting TurnStatus = "waiting"`

        The turn is waiting for external input.

      - `const TurnStatusCompleted TurnStatus = "completed"`

        The turn completed successfully.

      - `const TurnStatusFailed TurnStatus = "failed"`

        The turn failed.

      - `const TurnStatusCancelled TurnStatus = "cancelled"`

        The turn was cancelled.

    - `SubagentID string`

      The ID of the subagent that ran the turn, if applicable.

    - `Usage TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

  - `TurnID string`

    The ID of the turn associated with the event.

  - `Type AgentSessionTurnFailed`

    The type of the object. Always `agent.session.turn.failed`.

    - `const AgentSessionTurnFailedAgentSessionTurnFailed AgentSessionTurnFailed = "agent.session.turn.failed"`

  - `Usage TokenUsage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn In Progress Event

- `type AgentSessionTurnInProgressEvent struct{…}`

  Emitted when a turn starts running.

  - `EventID string`

    The unique ID of the event.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Turn Turn`

    The turn at the time it started running.

    - `ID string`

      The ID of the turn.

    - `AgentID string`

      The ID of the agent that ran the turn.

    - `CompletedAt int64`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `CreatedAt int64`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Error SessionTurnError`

      A customer-safe error. Non-null only for a failed turn.

      - `Code SessionTurnErrorCode`

        A stable, machine-readable failure category.

        - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

          The request exceeds the model's context window.

        - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

          The session has reached its usage budget.

        - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

          The organization has reached a usage, plan, or billing limit.

        - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

          The organization has no API credits remaining.

        - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

          The request exceeds the available rate limit.

        - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

          Flex processing is temporarily unavailable.

        - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

          The model service is temporarily overloaded.

        - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

          The request was rejected by a safety policy.

        - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

          The request was blocked by the safety systems.

        - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

          The request could not connect to the model service.

        - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

          The model service encountered an unexpected error.

        - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

          The API credentials are invalid or lack the required access.

        - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

          The request contains invalid input or configuration.

        - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

          The requested model or resource is unavailable.

        - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

          The request could not complete in its execution environment.

        - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

          The executor must be upgraded before it can run this turn.

        - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

          The session cannot accept additional input while a request is running.

        - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

          The request timed out before the model service responded.

        - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

          An unexpected internal error prevented the session request from completing.

      - `Message string`

        A customer-safe explanation of the failure.

    - `Object TurnObject`

      The object type. Always `agent.session.turn`.

      - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

    - `SessionID string`

      The ID of the session that owns the turn.

    - `StartedAt int64`

      The Unix timestamp, in seconds, when the turn started.

    - `Status TurnStatus`

      The current status of the turn.

      - `const TurnStatusQueued TurnStatus = "queued"`

        The turn is waiting to start.

      - `const TurnStatusInProgress TurnStatus = "in_progress"`

        The turn is in progress.

      - `const TurnStatusWaiting TurnStatus = "waiting"`

        The turn is waiting for external input.

      - `const TurnStatusCompleted TurnStatus = "completed"`

        The turn completed successfully.

      - `const TurnStatusFailed TurnStatus = "failed"`

        The turn failed.

      - `const TurnStatusCancelled TurnStatus = "cancelled"`

        The turn was cancelled.

    - `SubagentID string`

      The ID of the subagent that ran the turn, if applicable.

    - `Usage TokenUsage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `InputTokens int64`

        The number of input tokens used by the agent.

      - `InputTokensDetails TokenUsageInputTokensDetails`

        A breakdown of the agent's input token usage.

        - `CachedTokens int64`

          The number of input tokens retrieved from the prompt cache.

      - `OutputTokens int64`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails TokenUsageOutputTokensDetails`

        A breakdown of the agent's output token usage.

        - `ReasoningTokens int64`

          The number of output tokens used for reasoning.

      - `TotalTokens int64`

        The total number of input and output tokens used by the agent.

  - `TurnID string`

    The ID of the turn associated with the event.

  - `Type AgentSessionTurnInProgress`

    The type of the object. Always `agent.session.turn.in_progress`.

    - `const AgentSessionTurnInProgressAgentSessionTurnInProgress AgentSessionTurnInProgress = "agent.session.turn.in_progress"`

### Agent Session Turn Item Added Event

- `type AgentSessionTurnItemAddedEvent struct{…}`

  Emitted when an item is added to a turn.

  - `EventID string`

    The unique ID of the event.

  - `Item AgentSessionItemUnion`

    The item that was added.

    - `type AgentSessionMessage struct{…}`

      A user or assistant message recorded in a session.

      - `ID string`

        The ID of this item, or null for legacy user messages whose ID was not recorded.

      - `Content []AgentSessionMessageContentUnion`

        The content of the message. User messages contain input text or images; assistant messages contain output text.

        - `type AgentSessionMessageContentInputText struct{…}`

          Text supplied by the user.

          - `Text string`

            The text supplied by the user.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type AgentSessionMessageContentInputImage struct{…}`

          An image supplied by the user.

          - `ImageURL string`

            The URL of the image supplied by the user, which may be a base64-encoded data URL.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

        - `type AgentSessionMessageContentOutputText struct{…}`

          Text produced by the assistant.

          - `Text string`

            The text produced by the assistant.

          - `Type OutputText`

            The type of the object. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

      - `Phase AgentSessionMessagePhase`

        The phase of an assistant message. Null for user messages.

        - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

          Commentary produced while the agent works.

        - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

          The agent's final answer.

      - `Role AgentSessionMessageRole`

        The role of the message author.

        - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

        - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

      - `Status AgentOutputItemStatus`

        The status of the message. User messages are always `completed`.

        - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

          The item is in progress.

        - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

          The item is complete.

        - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

          The item stopped before completing.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type Message`

        The item type. Always `message`.

        - `const MessageMessage Message = "message"`

    - `type AgentReasoningItem struct{…}`

      A reasoning item produced by the agent.

      - `ID string`

        The ID of the reasoning item.

      - `Status AgentOutputItemStatus`

        The status of the reasoning item.

      - `Summary []SummaryText`

        The reasoning summaries produced by the agent.

        - `Text string`

          The reasoning summary text.

        - `Type SummaryText`

          The content type. Always `summary_text`.

          - `const SummaryTextSummaryText SummaryText = "summary_text"`

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type Reasoning`

        The item type. Always `reasoning`.

        - `const ReasoningReasoning Reasoning = "reasoning"`

    - `type AgentFunctionCallItem struct{…}`

      A function call produced by the agent.

      - `ID string`

        The ID of the function call item.

      - `Arguments any`

        The arguments to pass to the function.

      - `CallID string`

        The ID used to submit the function result.

      - `Name string`

        The name of the function to call.

      - `Status AgentFunctionCallStatus`

        The status of the function call.

        - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

          The call is in progress.

        - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

          The call completed successfully.

        - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

          The call failed.

        - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

          The call stopped before completing.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type FunctionCall`

        The item type. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionItemFunctionCallOutput struct{…}`

      The result supplied for a function call.

      - `ID string`

        The ID of the function call output item.

      - `CallID string`

        The ID of the function call that produced this output.

      - `Error string`

        The error message, if the call failed.

      - `Output AgentFunctionCallOutputUnion`

        The function result, if the call succeeded.

        - `string`

        - `type AgentFunctionCallOutputArray []InputContentUnion`

          - `type InputContentInputText struct{…}`

            Text input recorded in a session item.

            - `Text string`

              The text supplied to the agent.

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type InputContentInputImage struct{…}`

            Image input recorded in a session item.

            - `ImageURL string`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

      - `Status AgentFunctionCallStatus`

        The status of the function call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type FunctionCallOutput`

        The item type. Always `function_call_output`.

        - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

    - `type AgentSessionItemAgentMessage struct{…}`

      A message exchanged between agent threads.

      - `ID string`

        The ID of the message.

      - `Content []AgentContentUnion`

        The content exchanged between the agents.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

          - `Text string`

            The text produced by the agent.

          - `Type OutputText`

            The content type. Always `output_text`.

            - `const OutputTextOutputText OutputText = "output_text"`

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

          - `EncryptedContent string`

            The encrypted content payload.

          - `Type EncryptedContent`

            The content type. Always `encrypted_content`.

            - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

      - `RecipientAgentID string`

        The ID or name of the receiving agent.

      - `SenderAgentID string`

        The ID or name of the sending agent.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type AgentMessage`

        The item type. Always `agent_message`.

        - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

    - `type AgentMcpCallItem struct{…}`

      A call to a tool on an MCP server.

      - `ID string`

        The ID of the MCP call item.

      - `Arguments any`

        The arguments passed to the MCP tool.

      - `Error any`

        The error returned by the MCP tool, if any.

      - `Name string`

        The name of the MCP tool.

      - `Output any`

        The output returned by the MCP tool, if any.

      - `ServerLabel string`

        The label of the MCP server.

      - `Status AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type McpCall`

        The item type. Always `mcp_call`.

        - `const McpCallMcpCall McpCall = "mcp_call"`

    - `type AgentSessionItemComputerUseCall struct{…}`

      One execution of the platform-provided computer-use capability.

      - `ID string`

        The ID of the activity item.

      - `Output AgentSessionItemComputerUseCallOutput`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `ImageURL string`

          The complete JPEG image as a base64 data URL.

        - `Type ComputerScreenshot`

          The content type. Always `computer_screenshot`.

          - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

      - `Status AgentFunctionCallStatus`

        The execution status of the activity.

      - `Title string`

        A model-generated description of the activity, when available.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type ComputerUseCall`

        The item type. Always `computer_use_call`.

        - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

    - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

      A credential-free history record of the emitted login request.

      - `ID string`

        The stable history item ID.

      - `Request AgentSessionItemComputerUseApprovalRequestRequest`

        A registered form awaiting the application's response.

        - `CredentialOrigin string`

          The registered form or frame origin where values will be entered.

        - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

          Controls to render. All submitted values are sensitive.

          - `ID string`

            The field ID to submit as field_id in a fields entry.

          - `Label string`

            The label to display beside the control.

          - `Required bool`

            Whether this control requires a nonempty value.

          - `Type string`

            The rendering type, such as email, password, or text.

        - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

          Sign-in methods. Empty for a plain form.

          - `ID string`

            The option ID to submit as selected_option.

          - `FieldIDs []string`

            IDs from the registered fields that this method accepts.

          - `Label string`

            The method label to display.

        - `Reason string`

          Why the agent needs the user to sign in.

        - `Type BrowserAuthentication`

          The type of the object. Always `browser_authentication`.

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `RequestID string`

      - `TurnID string`

      - `Type ComputerUseApprovalRequest`

        The item type. Always computer_use_approval_request.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

      A credential-free record of an admitted response, not proof of completion.

      - `ID string`

        The stable history item ID.

      - `RequestID string`

        The registered request answered by this item.

      - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

        The admitted response, without submitted credential values.

        - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

          - `Action Submit`

            - `const SubmitSubmit Submit = "submit"`

          - `SelectedOption string`

            The chosen sign-in method, or null when no options were offered.

          - `Type BrowserAuthentication`

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

          - `Action Cancel`

            - `const CancelCancel Cancel = "cancel"`

          - `Type BrowserAuthentication`

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type ComputerUseApprovalRequestResult`

        - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

    - `type AgentWebSearchCallItem struct{…}`

      A web search call produced by the agent.

      - `ID string`

        The ID of the web search call.

      - `Action WebSearchActionUnion`

        The action performed by the web search tool.

        - `type WebSearchActionSearch struct{…}`

          A search query or group of search queries.

          - `Queries []string`

            The search queries, when multiple queries were used.

          - `Query string`

            The search query, when a single query was used.

          - `Type Search`

            The type of the object. Always `search`.

            - `const SearchSearch Search = "search"`

        - `type WebSearchActionOpenPage struct{…}`

          Opens a web page.

          - `Type OpenPage`

            The type of the object. Always `open_page`.

            - `const OpenPageOpenPage OpenPage = "open_page"`

          - `URL string`

            The URL of the page that was opened.

        - `type WebSearchActionFindInPage struct{…}`

          Finds text within a web page.

          - `Pattern string`

            The text pattern that was searched for.

          - `Type FindInPage`

            The type of the object. Always `find_in_page`.

            - `const FindInPageFindInPage FindInPage = "find_in_page"`

          - `URL string`

            The URL of the page that was searched.

        - `type WebSearchActionOther struct{…}`

          Another web search action.

          - `Type Other`

            The type of the object. Always `other`.

            - `const OtherOther Other = "other"`

      - `Status AgentOutputItemStatus`

        The status of the web search call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type WebSearchCall`

        The item type. Always `web_search_call`.

        - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

    - `type AgentCommandExecutionItem struct{…}`

      A command execution produced by the agent.

      - `ID string`

        The ID of the command execution item.

      - `Command string`

        The command that was executed.

      - `Cwd string`

        The working directory used to execute the command.

      - `DurationMs int64`

        The command duration in milliseconds.

      - `ExitCode int64`

        The process exit code, if the command completed.

      - `Output string`

        The command output, if available.

      - `Status AgentFunctionCallStatus`

        The status of the command execution.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CommandExecution`

        The item type. Always `command_execution`.

        - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

    - `type AgentCreateSubagentCallItem struct{…}`

      A request to spawn a subagent.

      - `ID string`

        The ID of the tool call item.

      - `AgentID string`

        The ID of the agent that requested the subagent.

      - `Content []AgentContentUnion`

        The task given to the spawned agent.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

      - `Model string`

        The model requested for the spawned agent.

      - `ReasoningEffort string`

        The reasoning effort requested for the spawned agent.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CreateSubagentCall`

        The item type. Always `create_subagent_call`.

        - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

          The current public item type.

    - `type AgentSendSubagentInputCallItem struct{…}`

      A request to send input to another agent.

      - `ID string`

        The ID of the tool call item.

      - `Content []AgentContentUnion`

        The input sent to the receiving agent.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

      - `RecipientAgentID string`

        The ID of the agent receiving the input.

      - `SenderAgentID string`

        The ID of the agent sending the input.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type SendSubagentInputCall`

        The item type. Always `send_subagent_input_call`.

        - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

          The current public item type.

    - `type AgentResumeSubagentCallItem struct{…}`

      A request to resume a subagent.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to resume.

      - `SenderAgentID string`

        The ID of the agent requesting the resume.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type ResumeSubagentCall`

        The item type. Always `resume_subagent_call`.

        - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

          The current public item type.

    - `type AgentWaitForSubagentsCallItem struct{…}`

      A request to wait for one or more subagents.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentIDs []string`

        The IDs of the agents to wait for.

      - `SenderAgentID string`

        The ID of the agent waiting for results.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type WaitForSubagentsCall`

        The item type. Always `wait_for_subagents_call`.

        - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

          The current public item type.

    - `type AgentInterruptSubagentCallItem struct{…}`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to interrupt.

      - `SenderAgentID string`

        The ID of the agent requesting the interrupt.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type InterruptSubagentCall`

        The item type. Always `interrupt_subagent_call`.

        - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

          The current public item type.

    - `type AgentCloseSubagentCallItem struct{…}`

      A request to close a subagent.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to close.

      - `SenderAgentID string`

        The ID of the agent requesting the close.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CloseSubagentCall`

        The item type. Always `close_subagent_call`.

        - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

          The current public item type.

  - `OutputIndex int64`

    The index of the item in the turn output, when the item is agent output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnItemAdded`

    The type of the object. Always `agent.session.turn.item.added`.

    - `const AgentSessionTurnItemAddedAgentSessionTurnItemAdded AgentSessionTurnItemAdded = "agent.session.turn.item.added"`

### Agent Session Turn Item Done Event

- `type AgentSessionTurnItemDoneEvent struct{…}`

  Emitted when an output item is complete.

  - `EventID string`

    The unique ID of the event.

  - `Item AgentOutputItemUnion`

    The completed output item.

    - `type AgentSessionAssistantMessage struct{…}`

      An assistant message produced by the agent.

      - `ID string`

        The ID of the message.

      - `Content []OutputText`

        The content of the message.

        - `Text string`

          The text produced by the agent.

        - `Type OutputText`

          The content type. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

      - `Phase AgentSessionAssistantMessagePhase`

        The phase of the assistant message.

        - `const AgentSessionAssistantMessagePhaseCommentary AgentSessionAssistantMessagePhase = "commentary"`

          Commentary produced while the agent works.

        - `const AgentSessionAssistantMessagePhaseFinalAnswer AgentSessionAssistantMessagePhase = "final_answer"`

          The agent's final answer.

      - `Role Assistant`

        The role of the message author. Always `assistant`.

        - `const AssistantAssistant Assistant = "assistant"`

      - `Status AgentOutputItemStatus`

        The status of the message.

        - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

          The item is in progress.

        - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

          The item is complete.

        - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

          The item stopped before completing.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type Message`

        The item type. Always `message`.

        - `const MessageMessage Message = "message"`

    - `type AgentReasoningItem struct{…}`

      A reasoning item produced by the agent.

      - `ID string`

        The ID of the reasoning item.

      - `Status AgentOutputItemStatus`

        The status of the reasoning item.

      - `Summary []SummaryText`

        The reasoning summaries produced by the agent.

        - `Text string`

          The reasoning summary text.

        - `Type SummaryText`

          The content type. Always `summary_text`.

          - `const SummaryTextSummaryText SummaryText = "summary_text"`

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type Reasoning`

        The item type. Always `reasoning`.

        - `const ReasoningReasoning Reasoning = "reasoning"`

    - `type AgentFunctionCallItem struct{…}`

      A function call produced by the agent.

      - `ID string`

        The ID of the function call item.

      - `Arguments any`

        The arguments to pass to the function.

      - `CallID string`

        The ID used to submit the function result.

      - `Name string`

        The name of the function to call.

      - `Status AgentFunctionCallStatus`

        The status of the function call.

        - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

          The call is in progress.

        - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

          The call completed successfully.

        - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

          The call failed.

        - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

          The call stopped before completing.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type FunctionCall`

        The item type. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentMcpCallItem struct{…}`

      A call to a tool on an MCP server.

      - `ID string`

        The ID of the MCP call item.

      - `Arguments any`

        The arguments passed to the MCP tool.

      - `Error any`

        The error returned by the MCP tool, if any.

      - `Name string`

        The name of the MCP tool.

      - `Output any`

        The output returned by the MCP tool, if any.

      - `ServerLabel string`

        The label of the MCP server.

      - `Status AgentFunctionCallStatus`

        The status of the MCP tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type McpCall`

        The item type. Always `mcp_call`.

        - `const McpCallMcpCall McpCall = "mcp_call"`

    - `type AgentOutputItemComputerUseCall struct{…}`

      One execution of the platform-provided computer-use capability.

      - `ID string`

        The ID of the activity item.

      - `Output AgentOutputItemComputerUseCallOutput`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `ImageURL string`

          The complete JPEG image as a base64 data URL.

        - `Type ComputerScreenshot`

          The content type. Always `computer_screenshot`.

          - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

      - `Status AgentFunctionCallStatus`

        The execution status of the activity.

      - `Title string`

        A model-generated description of the activity, when available.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type ComputerUseCall`

        The item type. Always `computer_use_call`.

        - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

    - `type AgentOutputItemComputerUseApprovalRequest struct{…}`

      A credential-free history record of the emitted login request.

      - `ID string`

        The stable history item ID.

      - `Request AgentOutputItemComputerUseApprovalRequestRequest`

        A registered form awaiting the application's response.

        - `CredentialOrigin string`

          The registered form or frame origin where values will be entered.

        - `Fields []AgentOutputItemComputerUseApprovalRequestRequestField`

          Controls to render. All submitted values are sensitive.

          - `ID string`

            The field ID to submit as field_id in a fields entry.

          - `Label string`

            The label to display beside the control.

          - `Required bool`

            Whether this control requires a nonempty value.

          - `Type string`

            The rendering type, such as email, password, or text.

        - `Options []AgentOutputItemComputerUseApprovalRequestRequestOption`

          Sign-in methods. Empty for a plain form.

          - `ID string`

            The option ID to submit as selected_option.

          - `FieldIDs []string`

            IDs from the registered fields that this method accepts.

          - `Label string`

            The method label to display.

        - `Reason string`

          Why the agent needs the user to sign in.

        - `Type BrowserAuthentication`

          The type of the object. Always `browser_authentication`.

          - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

      - `RequestID string`

      - `TurnID string`

      - `Type ComputerUseApprovalRequest`

        The item type. Always computer_use_approval_request.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentWebSearchCallItem struct{…}`

      A web search call produced by the agent.

      - `ID string`

        The ID of the web search call.

      - `Action WebSearchActionUnion`

        The action performed by the web search tool.

        - `type WebSearchActionSearch struct{…}`

          A search query or group of search queries.

          - `Queries []string`

            The search queries, when multiple queries were used.

          - `Query string`

            The search query, when a single query was used.

          - `Type Search`

            The type of the object. Always `search`.

            - `const SearchSearch Search = "search"`

        - `type WebSearchActionOpenPage struct{…}`

          Opens a web page.

          - `Type OpenPage`

            The type of the object. Always `open_page`.

            - `const OpenPageOpenPage OpenPage = "open_page"`

          - `URL string`

            The URL of the page that was opened.

        - `type WebSearchActionFindInPage struct{…}`

          Finds text within a web page.

          - `Pattern string`

            The text pattern that was searched for.

          - `Type FindInPage`

            The type of the object. Always `find_in_page`.

            - `const FindInPageFindInPage FindInPage = "find_in_page"`

          - `URL string`

            The URL of the page that was searched.

        - `type WebSearchActionOther struct{…}`

          Another web search action.

          - `Type Other`

            The type of the object. Always `other`.

            - `const OtherOther Other = "other"`

      - `Status AgentOutputItemStatus`

        The status of the web search call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type WebSearchCall`

        The item type. Always `web_search_call`.

        - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

    - `type AgentCommandExecutionItem struct{…}`

      A command execution produced by the agent.

      - `ID string`

        The ID of the command execution item.

      - `Command string`

        The command that was executed.

      - `Cwd string`

        The working directory used to execute the command.

      - `DurationMs int64`

        The command duration in milliseconds.

      - `ExitCode int64`

        The process exit code, if the command completed.

      - `Output string`

        The command output, if available.

      - `Status AgentFunctionCallStatus`

        The status of the command execution.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CommandExecution`

        The item type. Always `command_execution`.

        - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

    - `type AgentCreateSubagentCallItem struct{…}`

      A request to spawn a subagent.

      - `ID string`

        The ID of the tool call item.

      - `AgentID string`

        The ID of the agent that requested the subagent.

      - `Content []AgentContentUnion`

        The task given to the spawned agent.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

          - `Text string`

            The text produced by the agent.

          - `Type OutputText`

            The content type. Always `output_text`.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

          - `EncryptedContent string`

            The encrypted content payload.

          - `Type EncryptedContent`

            The content type. Always `encrypted_content`.

            - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

      - `Model string`

        The model requested for the spawned agent.

      - `ReasoningEffort string`

        The reasoning effort requested for the spawned agent.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CreateSubagentCall`

        The item type. Always `create_subagent_call`.

        - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

          The current public item type.

    - `type AgentSendSubagentInputCallItem struct{…}`

      A request to send input to another agent.

      - `ID string`

        The ID of the tool call item.

      - `Content []AgentContentUnion`

        The input sent to the receiving agent.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

      - `RecipientAgentID string`

        The ID of the agent receiving the input.

      - `SenderAgentID string`

        The ID of the agent sending the input.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type SendSubagentInputCall`

        The item type. Always `send_subagent_input_call`.

        - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

          The current public item type.

    - `type AgentResumeSubagentCallItem struct{…}`

      A request to resume a subagent.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to resume.

      - `SenderAgentID string`

        The ID of the agent requesting the resume.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type ResumeSubagentCall`

        The item type. Always `resume_subagent_call`.

        - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

          The current public item type.

    - `type AgentWaitForSubagentsCallItem struct{…}`

      A request to wait for one or more subagents.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentIDs []string`

        The IDs of the agents to wait for.

      - `SenderAgentID string`

        The ID of the agent waiting for results.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type WaitForSubagentsCall`

        The item type. Always `wait_for_subagents_call`.

        - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

          The current public item type.

    - `type AgentInterruptSubagentCallItem struct{…}`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to interrupt.

      - `SenderAgentID string`

        The ID of the agent requesting the interrupt.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type InterruptSubagentCall`

        The item type. Always `interrupt_subagent_call`.

        - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

          The current public item type.

    - `type AgentCloseSubagentCallItem struct{…}`

      A request to close a subagent.

      - `ID string`

        The ID of the tool call item.

      - `RecipientAgentID string`

        The ID of the agent to close.

      - `SenderAgentID string`

        The ID of the agent requesting the close.

      - `Status AgentFunctionCallStatus`

        The status of the tool call.

      - `TurnID string`

        The ID of the turn that contains this item.

      - `Type CloseSubagentCall`

        The item type. Always `close_subagent_call`.

        - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

          The current public item type.

  - `OutputIndex int64`

    The index of the output item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnItemDone`

    The type of the object. Always `agent.session.turn.item.done`.

    - `const AgentSessionTurnItemDoneAgentSessionTurnItemDone AgentSessionTurnItemDone = "agent.session.turn.item.done"`

### Agent Session Turn Output Text Delta Event

- `type AgentSessionTurnOutputTextDeltaEvent struct{…}`

  Emitted when text is appended to an output text content part.

  - `ContentIndex int64`

    The index of the content part in the message.

  - `Delta string`

    The text that was appended.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the message item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnOutputTextDelta`

    The type of the object. Always `agent.session.turn.output_text.delta`.

    - `const AgentSessionTurnOutputTextDeltaAgentSessionTurnOutputTextDelta AgentSessionTurnOutputTextDelta = "agent.session.turn.output_text.delta"`

### Agent Session Turn Output Text Done Event

- `type AgentSessionTurnOutputTextDoneEvent struct{…}`

  Emitted when an output text content part is complete.

  - `ContentIndex int64`

    The index of the content part in the message.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the message item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `Text string`

    The complete output text.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnOutputTextDone`

    The type of the object. Always `agent.session.turn.output_text.done`.

    - `const AgentSessionTurnOutputTextDoneAgentSessionTurnOutputTextDone AgentSessionTurnOutputTextDone = "agent.session.turn.output_text.done"`

### Agent Session Turn Reasoning Summary Part Added Event

- `type AgentSessionTurnReasoningSummaryPartAddedEvent struct{…}`

  Emitted when a reasoning summary content part is added.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the reasoning item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `Part SummaryText`

    The initial summary part.

    - `Text string`

      The reasoning summary text.

    - `Type SummaryText`

      The content type. Always `summary_text`.

      - `const SummaryTextSummaryText SummaryText = "summary_text"`

  - `SessionID string`

    The ID of the session associated with the event.

  - `SummaryIndex int64`

    The index of the summary content part.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnReasoningSummaryPartAdded`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

    - `const AgentSessionTurnReasoningSummaryPartAddedAgentSessionTurnReasoningSummaryPartAdded AgentSessionTurnReasoningSummaryPartAdded = "agent.session.turn.reasoning_summary_part.added"`

### Agent Session Turn Reasoning Summary Part Done Event

- `type AgentSessionTurnReasoningSummaryPartDoneEvent struct{…}`

  Emitted when a reasoning summary part is complete.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the reasoning item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `Part SummaryText`

    The completed summary part.

    - `Text string`

      The reasoning summary text.

    - `Type SummaryText`

      The content type. Always `summary_text`.

      - `const SummaryTextSummaryText SummaryText = "summary_text"`

  - `SessionID string`

    The ID of the session associated with the event.

  - `Status Incomplete`

    Present as `incomplete` when summary generation was interrupted.

    - `const IncompleteIncomplete Incomplete = "incomplete"`

  - `SummaryIndex int64`

    The index of the summary part.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnReasoningSummaryPartDone`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

    - `const AgentSessionTurnReasoningSummaryPartDoneAgentSessionTurnReasoningSummaryPartDone AgentSessionTurnReasoningSummaryPartDone = "agent.session.turn.reasoning_summary_part.done"`

### Agent Session Turn Reasoning Summary Text Delta Event

- `type AgentSessionTurnReasoningSummaryTextDeltaEvent struct{…}`

  Emitted when text is appended to a reasoning summary.

  - `Delta string`

    The summary text that was appended.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the reasoning item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `SummaryIndex int64`

    The index of the summary content part.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnReasoningSummaryTextDelta`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

    - `const AgentSessionTurnReasoningSummaryTextDeltaAgentSessionTurnReasoningSummaryTextDelta AgentSessionTurnReasoningSummaryTextDelta = "agent.session.turn.reasoning_summary_text.delta"`

### Agent Session Turn Reasoning Summary Text Done Event

- `type AgentSessionTurnReasoningSummaryTextDoneEvent struct{…}`

  Emitted when a reasoning summary content part is complete.

  - `EventID string`

    The unique ID of the event.

  - `ItemID string`

    The ID of the reasoning item.

  - `OutputIndex int64`

    The index of the item in the turn output.

  - `SessionID string`

    The ID of the session associated with the event.

  - `SummaryIndex int64`

    The index of the summary content part.

  - `Text string`

    The complete reasoning summary text.

  - `TurnID string`

    The ID of the turn associated with the event, when applicable.

  - `Type AgentSessionTurnReasoningSummaryTextDone`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

    - `const AgentSessionTurnReasoningSummaryTextDoneAgentSessionTurnReasoningSummaryTextDone AgentSessionTurnReasoningSummaryTextDone = "agent.session.turn.reasoning_summary_text.done"`

### Agent Text

- `type AgentText struct{…}`

  The text configuration used by an agent.

  - `Format TextFormatUnion`

    The effective output format. Defaults to ordinary text.

    - `type TextFormatText struct{…}`

      Generates ordinary text without a structured-output constraint.

      - `Type Text`

        The type of the object. Always `text`.

        - `const TextText Text = "text"`

    - `type TextFormatJSONSchema struct{…}`

      Constrains generated text to a JSON Schema.

      - `Schema map[string, any]`

        The JSON Schema that generated text must match.

      - `Type JSONSchema`

        The type of the object. Always `json_schema`.

        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

  - `Verbosity AgentTextVerbosity`

    The amount of text produced by the agent. Defaults to `medium`.

    - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

    - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

    - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

### Agent Text Param

- `type AgentTextParamResp struct{…}`

  Configuration for text generated by the agent.

  - `Format TextFormatParamUnionResp`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `TextFormatParamTextResp`

      - `Type Text`

        The type of the object. Always `text`.

        - `const TextText Text = "text"`

    - `TextFormatParamJSONSchemaResp`

      - `Schema map[string, any]`

        The JSON Schema that generated text must match.

      - `Type JSONSchema`

        The type of the object. Always `json_schema`.

        - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

  - `Verbosity AgentTextParamVerbosity`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `const AgentTextParamVerbosityLow AgentTextParamVerbosity = "low"`

      Produces less text.

    - `const AgentTextParamVerbosityMedium AgentTextParamVerbosity = "medium"`

      Uses the default amount of text.

    - `const AgentTextParamVerbosityHigh AgentTextParamVerbosity = "high"`

      Produces more text.

### Agent Tool

- `type AgentToolUnion interface{…}`

  A tool available to the agent.

  - `type AgentToolFunction struct{…}`

    A function defined by the application.

    - `DeferLoading bool`

      Whether the function is deferred and discovered through tool search.

    - `Description string`

      A description of what the function does.

    - `Name string`

      The name of the function.

    - `Parameters map[string, any]`

      A JSON Schema object describing the function's arguments.

    - `Type Function`

      The type of the object. Always `function`.

      - `const FunctionFunction Function = "function"`

  - `type AgentToolProgrammaticToolCalling struct{…}`

    Enables calling tools from model-generated code.

    - `Enabled bool`

      Whether tools can be called from model-generated code.

    - `Type ProgrammaticToolCalling`

      The type of the object. Always `programmatic_tool_calling`.

      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

  - `type AgentToolMcp struct{…}`

    Tools provided by a remote MCP server.

    - `AllowedTools []string`

      The MCP tools the agent may call.

    - `ConnectionOrigin string`

      Where outbound MCP HTTP connections originate.

      - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

      - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

    - `CredentialID string`

      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

    - `RequestMetadata map[string, any]`

      Metadata included with requests to this MCP server.

    - `Required bool`

      Whether this MCP server must initialize before the first turn.

    - `ServerLabel string`

      A label used to identify the MCP server in tool calls.

    - `Transport McpTransportUnion`

      The transport used to connect to the MCP server.

      - `type McpTransportHTTP struct{…}`

        Connects to an MCP server over HTTP.

        - `ServerURL string`

          The URL of the MCP server.

        - `Type HTTP`

          The type of the object. Always `http`.

          - `const HTTPHTTP HTTP = "http"`

      - `type McpTransportStdio struct{…}`

        Starts an MCP server as a local process.

        - `Args []string`

          Arguments passed to the MCP server command.

        - `Command string`

          The command used to start the MCP server.

        - `Cwd string`

          The working directory used to start the MCP server.

        - `EnvVars []string`

          Environment variable names inherited from the execution environment.

        - `Type Stdio`

          The type of the object. Always `stdio`.

          - `const StdioStdio Stdio = "stdio"`

    - `Type Mcp`

      The type of the object. Always `mcp`.

      - `const McpMcp Mcp = "mcp"`

  - `type AgentToolWebSearch struct{…}`

    Web search.

    - `AllowedDomains []string`

      Allowed search domains, or `null` when the search is unrestricted.

    - `ContextSize string`

      The amount of search context made available to the model. Defaults to `medium`.

      - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

      - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

      - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

    - `Location AgentToolWebSearchLocation`

      Approximate location used to localize search results, if provided.

      - `City string`

        The city name.

      - `Country string`

        The two-letter ISO country code, such as `US`.

      - `Region string`

        The region or state name.

      - `Timezone string`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode string`

      The source used for web search results.

      - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

      - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

      - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

    - `Type WebSearch`

      The type of the object. Always `web_search`.

      - `const WebSearchWebSearch WebSearch = "web_search"`

  - `type AgentToolComputerUse struct{…}`

    Browser use in an OpenAI-hosted session.

    - `IncludeScreenshots bool`

      Whether computer tool outputs include screenshots.

    - `Type ComputerUse`

      The type of the object. Always `computer_use`.

      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

### Agent Tool Param

- `type AgentToolParamUnionResp interface{…}`

  A tool available to the agent.

  - `AgentToolParamFunctionResp`

    - `Description string`

      A description of what the function does.

    - `Name string`

      The name of the function.

    - `Parameters map[string, any]`

      A JSON Schema object describing the function's arguments.

    - `Type Function`

      The type of the object. Always `function`.

      - `const FunctionFunction Function = "function"`

    - `DeferLoading bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `AgentToolParamToolSearchResp`

    - `Type ToolSearch`

      The type of the object. Always `tool_search`.

      - `const ToolSearchToolSearch ToolSearch = "tool_search"`

  - `AgentToolParamProgrammaticToolCallingResp`

    - `Type ProgrammaticToolCalling`

      The type of the object. Always `programmatic_tool_calling`.

      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `Enabled bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `AgentToolParamMcpResp`

    - `ServerLabel string`

      A label used to identify the MCP server in tool calls.

    - `Transport McpTransportParamUnionResp`

      The transport used to connect to the MCP server.

      - `McpTransportParamHTTPResp`

        - `ServerURL string`

          The URL of the MCP server.

        - `Type HTTP`

          The type of the object. Always `http`.

          - `const HTTPHTTP HTTP = "http"`

        - `Authorization string`

          The authorization value sent to the MCP server, if any.

        - `Headers map[string, string]`

          Additional HTTP headers sent to the MCP server.

      - `McpTransportParamStdioResp`

        - `Command string`

          The command used to start the MCP server.

        - `Cwd string`

          The working directory used to start the MCP server.

        - `Type Stdio`

          The type of the object. Always `stdio`.

          - `const StdioStdio Stdio = "stdio"`

        - `Args []string`

          Arguments passed to the MCP server command.

        - `Env map[string, string]`

          Environment variables set for the MCP server process.

        - `EnvVars []string`

          Environment variable names to inherit from the selected execution environment.

    - `Type Mcp`

      The type of the object. Always `mcp`.

      - `const McpMcp Mcp = "mcp"`

    - `AllowedTools []string`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `ConnectionOrigin string`

      Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

      - `const AgentToolParamMcpConnectionOriginService AgentToolParamMcpConnectionOrigin = "service"`

        Uses the Managed Agents service network.

      - `const AgentToolParamMcpConnectionOriginEnvironment AgentToolParamMcpConnectionOrigin = "environment"`

        Uses the session's execution environment.

    - `CredentialID string`

      The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

    - `RequestMetadata map[string, any]`

      Metadata included with requests to this MCP server.

    - `Required bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `AgentToolParamWebSearchResp`

    - `Type WebSearch`

      The type of the object. Always `web_search`.

      - `const WebSearchWebSearch WebSearch = "web_search"`

    - `AllowedDomains []string`

      Domains the search may include.

    - `ContextSize string`

      The amount of search context made available to the model. Defaults to `medium`.

      - `const AgentToolParamWebSearchContextSizeLow AgentToolParamWebSearchContextSize = "low"`

      - `const AgentToolParamWebSearchContextSizeMedium AgentToolParamWebSearchContextSize = "medium"`

      - `const AgentToolParamWebSearchContextSizeHigh AgentToolParamWebSearchContextSize = "high"`

    - `Location AgentToolParamWebSearchLocationResp`

      Approximate location used to localize search results.

      - `City string`

        The city name.

      - `Country string`

        The two-letter ISO country code, such as `US`.

      - `Region string`

        The region or state name.

      - `Timezone string`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode string`

      The source used for web search results. Defaults to `live`.

      - `const AgentToolParamWebSearchModeDisabled AgentToolParamWebSearchMode = "disabled"`

        Disables web search.

      - `const AgentToolParamWebSearchModeCached AgentToolParamWebSearchMode = "cached"`

        Uses cached search results.

      - `const AgentToolParamWebSearchModeLive AgentToolParamWebSearchMode = "live"`

        Searches the live web.

  - `AgentToolParamComputerUseResp`

    - `Type ComputerUse`

      The type of the object. Always `computer_use`.

      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `IncludeScreenshots bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Agent Wait For Subagents Call Item

- `type AgentWaitForSubagentsCallItem struct{…}`

  A request to wait for one or more subagents.

  - `ID string`

    The ID of the tool call item.

  - `RecipientAgentIDs []string`

    The IDs of the agents to wait for.

  - `SenderAgentID string`

    The ID of the agent waiting for results.

  - `Status AgentFunctionCallStatus`

    The status of the tool call.

    - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

      The call is in progress.

    - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

      The call completed successfully.

    - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

      The call failed.

    - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

      The call stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type WaitForSubagentsCall`

    The item type. Always `wait_for_subagents_call`.

    - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

      The current public item type.

### Agent Web Search Call Item

- `type AgentWebSearchCallItem struct{…}`

  A web search call produced by the agent.

  - `ID string`

    The ID of the web search call.

  - `Action WebSearchActionUnion`

    The action performed by the web search tool.

    - `type WebSearchActionSearch struct{…}`

      A search query or group of search queries.

      - `Queries []string`

        The search queries, when multiple queries were used.

      - `Query string`

        The search query, when a single query was used.

      - `Type Search`

        The type of the object. Always `search`.

        - `const SearchSearch Search = "search"`

    - `type WebSearchActionOpenPage struct{…}`

      Opens a web page.

      - `Type OpenPage`

        The type of the object. Always `open_page`.

        - `const OpenPageOpenPage OpenPage = "open_page"`

      - `URL string`

        The URL of the page that was opened.

    - `type WebSearchActionFindInPage struct{…}`

      Finds text within a web page.

      - `Pattern string`

        The text pattern that was searched for.

      - `Type FindInPage`

        The type of the object. Always `find_in_page`.

        - `const FindInPageFindInPage FindInPage = "find_in_page"`

      - `URL string`

        The URL of the page that was searched.

    - `type WebSearchActionOther struct{…}`

      Another web search action.

      - `Type Other`

        The type of the object. Always `other`.

        - `const OtherOther Other = "other"`

  - `Status AgentOutputItemStatus`

    The status of the web search call.

    - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

      The item is in progress.

    - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

      The item is complete.

    - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

      The item stopped before completing.

  - `TurnID string`

    The ID of the turn that contains this item.

  - `Type WebSearchCall`

    The item type. Always `web_search_call`.

    - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

### Environment

- `type EnvironmentUnion interface{…}`

  The execution environment for a session.

  - `type EnvironmentNone struct{…}`

    The session talks to CCA without selecting or provisioning an execution environment.

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `type EnvironmentOpenAIHosted struct{…}`

    An environment hosted by OpenAI.

    - `ID string`

      The public ID of the environment.

    - `CapabilityDirectories []string`

      Directories that contain capabilities exposed to the agent.

    - `Desktop EnvironmentOpenAIHostedDesktop`

      The effective desktop configuration.

      - `Enabled bool`

        Whether the environment provisions a desktop and browser proxy.

    - `Files []HostedEnvironmentFileUnion`

      Files available in the environment, excluding their contents.

      - `type HostedEnvironmentFileID struct{…}`

        A file copied from the OpenAI Files API.

        - `ID string`

          The session-scoped ID of the file in the execution environment.

        - `FileID string`

          The ID of the uploaded file.

        - `Path string`

          The file's absolute path inside the environment.

        - `SizeBytes int64`

          The decoded file size in bytes.

        - `Type FileID`

          The type of the object. Always `file_id`.

          - `const FileIDFileID FileID = "file_id"`

      - `type HostedEnvironmentFileInline struct{…}`

        A file supplied inline when the session was created.

        - `ID string`

          The session-scoped ID of the file in the execution environment.

        - `Path string`

          The file's absolute path inside the environment.

        - `SizeBytes int64`

          The decoded file size in bytes.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Network EnvironmentOpenAIHostedNetwork`

      The effective network access policy for the environment.

      - `Access string`

        The environment's network access mode.

        - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

          Allows unrestricted network access.

        - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

          Disables network access.

        - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

          Applies the configured domain restrictions.

      - `AllowedDomains []string`

        Domains the environment may access when network access is restricted.

    - `Packages EnvironmentOpenAIHostedPackages`

      Packages installed in the environment.

      - `Npm []string`

        npm packages installed globally in the environment.

      - `Python []string`

        Python packages installed in the environment.

      - `System []string`

        System packages installed in the environment.

    - `Plugins []HostedPlugin`

      Plugins installed in the environment, excluding their archive contents.

      - `Description string`

        The installed plugin description.

      - `Name string`

        The installed plugin name.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

    - `Skills []HostedSkillUnion`

      Skills installed in the environment, excluding their archive contents.

      - `type HostedSkillReference struct{…}`

        A skill installed from the Skills API.

        - `Description string`

          The installed skill description.

        - `Name string`

          The installed skill name.

        - `SkillID string`

          The referenced skill ID.

        - `Type SkillReference`

          The type of the object. Always `skill_reference`.

          - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

        - `Version string`

          The concrete skill version installed for this session.

      - `type HostedSkillInline struct{…}`

        A skill installed from an inline ZIP archive.

        - `Description string`

          The installed skill description.

        - `Name string`

          The installed skill name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Type OpenAIHosted`

      The type of the object. Always `openai_hosted`.

      - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

    - `ContainerSize string`

      The effective CPU and memory tier, or null when unknown or outside the public tiers.

      - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

      - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

      - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

  - `type EnvironmentSelfHosted struct{…}`

    An environment hosted by the application.

    - `ID string`

      The public ID of the environment.

    - `CapabilityDirectories []string`

      Directories that contain capabilities exposed to the agent.

    - `RemoteURL string`

      Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

    - `Type SelfHosted`

      The type of the object. Always `self_hosted`.

      - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

    - `WorkspaceDirectory string`

      The absolute project directory inside the environment. Defaults to `/workspace`.

### Environment Param

- `type EnvironmentParamUnionResp interface{…}`

  The execution environment and optional reusable template for a session.

  - `EnvironmentParamNoneResp`

    - `Type None`

      The type of the object. Always `none`.

      - `const NoneNone None = "none"`

  - `EnvironmentParamOpenAIHostedResp`

    - `Type OpenAIHosted`

      The type of the object. Always `openai_hosted`.

      - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

    - `CapabilityDirectories []string`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `ContainerSize string`

      The hosted container size. Omission selects the medium tier.

      - `const EnvironmentParamOpenAIHostedContainerSizeSmall EnvironmentParamOpenAIHostedContainerSize = "small"`

      - `const EnvironmentParamOpenAIHostedContainerSizeMedium EnvironmentParamOpenAIHostedContainerSize = "medium"`

      - `const EnvironmentParamOpenAIHostedContainerSizeLarge EnvironmentParamOpenAIHostedContainerSize = "large"`

    - `Desktop EnvironmentParamOpenAIHostedDesktopResp`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `Enabled bool`

        Whether to provision the desktop and its browser proxy.

    - `Env map[string, string]`

      Environment variables made available to the agent.

    - `EnvironmentTemplateID string`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `Files []HostedEnvironmentFileParamUnionResp`

      Files available before the agent starts. Defaults to an empty list.

      - `HostedEnvironmentFileParamFileIDResp`

        - `FileID string`

          The ID of the uploaded file.

        - `Path string`

          The absolute destination path inside `/workspace`.

        - `Type FileID`

          The type of the object. Always `file_id`.

          - `const FileIDFileID FileID = "file_id"`

      - `HostedEnvironmentFileParamInlineResp`

        - `Data string`

          The standard-base64-encoded file contents.

        - `Path string`

          The absolute destination path inside `/workspace`.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

    - `Network EnvironmentParamOpenAIHostedNetworkResp`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `Access string`

        The environment's network access mode.

        - `const EnvironmentParamOpenAIHostedNetworkAccessEnabled EnvironmentParamOpenAIHostedNetworkAccess = "enabled"`

          Allows unrestricted network access.

        - `const EnvironmentParamOpenAIHostedNetworkAccessDisabled EnvironmentParamOpenAIHostedNetworkAccess = "disabled"`

          Disables network access.

        - `const EnvironmentParamOpenAIHostedNetworkAccessRestricted EnvironmentParamOpenAIHostedNetworkAccess = "restricted"`

          Applies the configured domain restrictions.

      - `AllowedDomains []string`

        Domains the environment may access when network access is restricted.

      - `BlockedDomains []string`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `Packages EnvironmentParamOpenAIHostedPackagesResp`

      Packages to install in the environment. Defaults to empty package lists.

      - `Npm []string`

        npm packages to install globally. Defaults to an empty list.

      - `Python []string`

        Python packages to install. Defaults to an empty list.

      - `System []string`

        System packages to install. Defaults to an empty list.

    - `Plugins []HostedPluginParamResp`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `Description string`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `Name string`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

        - `Data string`

          Standard-base64 encoded ZIP archive bytes.

        - `MediaType ApplicationZip`

          The archive media type, always `application/zip`.

          - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

            A ZIP archive.

        - `Type Base64`

          The type of the object. Always `base64`.

          - `const Base64Base64 Base64 = "base64"`

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

    - `SetupCommands []SetupCommandParamResp`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `Command string`

        The shell command to execute.

      - `Cwd string`

        The absolute working directory. Defaults to `/workspace`.

    - `Skills []HostedSkillParamUnionResp`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `HostedSkillParamSkillReferenceResp`

        - `SkillID string`

          The ID of the skill created through `/v1/skills`.

        - `Type SkillReference`

          The type of the object. Always `skill_reference`.

          - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

        - `Version string`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `HostedSkillParamInlineResp`

        - `Description string`

          The skill description declared in `SKILL.md`.

        - `Name string`

          The skill name declared in `SKILL.md`.

        - `Source InlineCapabilitySourceParamResp`

          Provides ZIP bytes encoded with standard base64.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

  - `EnvironmentParamSelfHostedResp`

    - `Type SelfHosted`

      The type of the object. Always `self_hosted`.

      - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

    - `WorkspaceDirectory string`

      Absolute project directory inside the self-hosted environment.

    - `CapabilityDirectories []string`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

### Hosted Environment File

- `type HostedEnvironmentFileUnion interface{…}`

  Metadata for a file materialized in an OpenAI-hosted execution environment.

  - `type HostedEnvironmentFileID struct{…}`

    A file copied from the OpenAI Files API.

    - `ID string`

      The session-scoped ID of the file in the execution environment.

    - `FileID string`

      The ID of the uploaded file.

    - `Path string`

      The file's absolute path inside the environment.

    - `SizeBytes int64`

      The decoded file size in bytes.

    - `Type FileID`

      The type of the object. Always `file_id`.

      - `const FileIDFileID FileID = "file_id"`

  - `type HostedEnvironmentFileInline struct{…}`

    A file supplied inline when the session was created.

    - `ID string`

      The session-scoped ID of the file in the execution environment.

    - `Path string`

      The file's absolute path inside the environment.

    - `SizeBytes int64`

      The decoded file size in bytes.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

### Hosted Environment File ID

- `type HostedEnvironmentFileID struct{…}`

  A file copied from the OpenAI Files API.

  - `ID string`

    The session-scoped ID of the file in the execution environment.

  - `FileID string`

    The ID of the uploaded file.

  - `Path string`

    The file's absolute path inside the environment.

  - `SizeBytes int64`

    The decoded file size in bytes.

  - `Type FileID`

    The type of the object. Always `file_id`.

    - `const FileIDFileID FileID = "file_id"`

### Hosted Environment File Param

- `type HostedEnvironmentFileParamUnionResp interface{…}`

  A file materialized in an OpenAI-hosted execution environment.

  - `HostedEnvironmentFileParamFileIDResp`

    - `FileID string`

      The ID of the uploaded file.

    - `Path string`

      The absolute destination path inside `/workspace`.

    - `Type FileID`

      The type of the object. Always `file_id`.

      - `const FileIDFileID FileID = "file_id"`

  - `HostedEnvironmentFileParamInlineResp`

    - `Data string`

      The standard-base64-encoded file contents.

    - `Path string`

      The absolute destination path inside `/workspace`.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

### Hosted Plugin

- `type HostedPlugin struct{…}`

  A plugin installed from an inline ZIP archive.

  - `Description string`

    The installed plugin description.

  - `Name string`

    The installed plugin name.

  - `Type Inline`

    The type of the object. Always `inline`.

    - `const InlineInline Inline = "inline"`

### Hosted Plugin Param

- `type HostedPluginParamResp struct{…}`

  Supplies a plugin ZIP directly in the session request.

  - `Description string`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `Name string`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `Source InlineCapabilitySourceParamResp`

    Provides ZIP bytes encoded with standard base64.

    - `Data string`

      Standard-base64 encoded ZIP archive bytes.

    - `MediaType ApplicationZip`

      The archive media type, always `application/zip`.

      - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

        A ZIP archive.

    - `Type Base64`

      The type of the object. Always `base64`.

      - `const Base64Base64 Base64 = "base64"`

  - `Type Inline`

    The type of the object. Always `inline`.

    - `const InlineInline Inline = "inline"`

### Hosted Skill

- `type HostedSkillUnion interface{…}`

  A skill installed in an OpenAI-hosted environment.

  - `type HostedSkillReference struct{…}`

    A skill installed from the Skills API.

    - `Description string`

      The installed skill description.

    - `Name string`

      The installed skill name.

    - `SkillID string`

      The referenced skill ID.

    - `Type SkillReference`

      The type of the object. Always `skill_reference`.

      - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

    - `Version string`

      The concrete skill version installed for this session.

  - `type HostedSkillInline struct{…}`

    A skill installed from an inline ZIP archive.

    - `Description string`

      The installed skill description.

    - `Name string`

      The installed skill name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

### Hosted Skill Param

- `type HostedSkillParamUnionResp interface{…}`

  A skill installed in an OpenAI-hosted environment.

  - `HostedSkillParamSkillReferenceResp`

    - `SkillID string`

      The ID of the skill created through `/v1/skills`.

    - `Type SkillReference`

      The type of the object. Always `skill_reference`.

      - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

    - `Version string`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `HostedSkillParamInlineResp`

    - `Description string`

      The skill description declared in `SKILL.md`.

    - `Name string`

      The skill name declared in `SKILL.md`.

    - `Source InlineCapabilitySourceParamResp`

      Provides ZIP bytes encoded with standard base64.

      - `Data string`

        Standard-base64 encoded ZIP archive bytes.

      - `MediaType ApplicationZip`

        The archive media type, always `application/zip`.

        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

          A ZIP archive.

      - `Type Base64`

        The type of the object. Always `base64`.

        - `const Base64Base64 Base64 = "base64"`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

### Hosted Skill Reference

- `type HostedSkillReference struct{…}`

  A skill installed from the Skills API.

  - `Description string`

    The installed skill description.

  - `Name string`

    The installed skill name.

  - `SkillID string`

    The referenced skill ID.

  - `Type SkillReference`

    The type of the object. Always `skill_reference`.

    - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

  - `Version string`

    The concrete skill version installed for this session.

### Inline Capability Source Param

- `type InlineCapabilitySourceParamResp struct{…}`

  Provides ZIP bytes encoded with standard base64.

  - `Data string`

    Standard-base64 encoded ZIP archive bytes.

  - `MediaType ApplicationZip`

    The archive media type, always `application/zip`.

    - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

      A ZIP archive.

  - `Type Base64`

    The type of the object. Always `base64`.

    - `const Base64Base64 Base64 = "base64"`

### Input Content

- `type InputContentUnion interface{…}`

  User-provided content recorded in a session item.

  - `type InputContentInputText struct{…}`

    Text input recorded in a session item.

    - `Text string`

      The text supplied to the agent.

    - `Type InputText`

      The type of the object. Always `input_text`.

      - `const InputTextInputText InputText = "input_text"`

  - `type InputContentInputImage struct{…}`

    Image input recorded in a session item.

    - `ImageURL string`

      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

    - `Type InputImage`

      The type of the object. Always `input_image`.

      - `const InputImageInputImage InputImage = "input_image"`

### Input Content Param

- `type InputContentParamUnionResp interface{…}`

  Content included in an input message.

  - `InputContentParamInputTextResp`

    - `Text string`

      The text sent to the model.

    - `Type InputText`

      The type of the object. Always `input_text`.

      - `const InputTextInputText InputText = "input_text"`

  - `InputContentParamInputImageResp`

    - `ImageURL string`

      The URL of the image sent to the model.

    - `Type InputImage`

      The type of the object. Always `input_image`.

      - `const InputImageInputImage InputImage = "input_image"`

### Mcp Transport

- `type McpTransportUnion interface{…}`

  The transport used to connect to an MCP server.

  - `type McpTransportHTTP struct{…}`

    Connects to an MCP server over HTTP.

    - `ServerURL string`

      The URL of the MCP server.

    - `Type HTTP`

      The type of the object. Always `http`.

      - `const HTTPHTTP HTTP = "http"`

  - `type McpTransportStdio struct{…}`

    Starts an MCP server as a local process.

    - `Args []string`

      Arguments passed to the MCP server command.

    - `Command string`

      The command used to start the MCP server.

    - `Cwd string`

      The working directory used to start the MCP server.

    - `EnvVars []string`

      Environment variable names inherited from the execution environment.

    - `Type Stdio`

      The type of the object. Always `stdio`.

      - `const StdioStdio Stdio = "stdio"`

### Mcp Transport Param

- `type McpTransportParamUnionResp interface{…}`

  The transport used to connect to an MCP server.

  - `McpTransportParamHTTPResp`

    - `ServerURL string`

      The URL of the MCP server.

    - `Type HTTP`

      The type of the object. Always `http`.

      - `const HTTPHTTP HTTP = "http"`

    - `Authorization string`

      The authorization value sent to the MCP server, if any.

    - `Headers map[string, string]`

      Additional HTTP headers sent to the MCP server.

  - `McpTransportParamStdioResp`

    - `Command string`

      The command used to start the MCP server.

    - `Cwd string`

      The working directory used to start the MCP server.

    - `Type Stdio`

      The type of the object. Always `stdio`.

      - `const StdioStdio Stdio = "stdio"`

    - `Args []string`

      Arguments passed to the MCP server command.

    - `Env map[string, string]`

      Environment variables set for the MCP server process.

    - `EnvVars []string`

      Environment variable names to inherit from the selected execution environment.

### Multi Agent Config

- `type MultiAgentConfig struct{…}`

  The resolved configuration for creating and coordinating subagents.

  - `Enabled bool`

    Whether subagent tools are enabled. Defaults to false.

  - `MaxConcurrentSubagents int64`

    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

### Multi Agent Config Param

- `type MultiAgentConfigParamResp struct{…}`

  Explicit configuration for creating and coordinating subagents.

  - `Enabled bool`

    Whether subagent tools are enabled.

  - `MaxConcurrentSubagents int64`

    Maximum number of subagents that may run concurrently. Defaults to 6.

### Output Text

- `type OutputText struct{…}`

  A text content part produced by the agent.

  - `Text string`

    The text produced by the agent.

  - `Type OutputText`

    The content type. Always `output_text`.

    - `const OutputTextOutputText OutputText = "output_text"`

### Persisted Agent Tool

- `type PersistedAgentToolUnion interface{…}`

  A credential-free tool available to a reusable agent.

  - `type PersistedAgentToolFunction struct{…}`

    A function defined by the application.

    - `DeferLoading bool`

      Whether the function is deferred and discovered through tool search.

    - `Description string`

      A description of what the function does.

    - `Name string`

      The name of the function.

    - `Parameters map[string, any]`

      A JSON Schema object describing the function's arguments.

    - `Type Function`

      The type of the object. Always `function`.

      - `const FunctionFunction Function = "function"`

  - `type PersistedAgentToolToolSearch struct{…}`

    Discovers deferred function tools and loads them into the model context.

    - `Type ToolSearch`

      The type of the object. Always `tool_search`.

      - `const ToolSearchToolSearch ToolSearch = "tool_search"`

  - `type PersistedAgentToolProgrammaticToolCalling struct{…}`

    Enables calling tools from model-generated code.

    - `Enabled bool`

      Whether tools can be called from model-generated code.

    - `Type ProgrammaticToolCalling`

      The type of the object. Always `programmatic_tool_calling`.

      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

  - `type PersistedAgentToolMcp struct{…}`

    Tools provided by a remote MCP server without stored credentials.

    - `AllowedTools []string`

      The MCP tools the agent may call, or null when all server tools are allowed.

    - `ConnectionOrigin string`

      Where outbound MCP HTTP connections originate.

      - `const PersistedAgentToolMcpConnectionOriginService PersistedAgentToolMcpConnectionOrigin = "service"`

      - `const PersistedAgentToolMcpConnectionOriginEnvironment PersistedAgentToolMcpConnectionOrigin = "environment"`

    - `CredentialID string`

      The vault credential selected for this MCP server, if any.

    - `RequestMetadata map[string, any]`

      Metadata included with requests to this MCP server.

    - `Required bool`

      Whether this MCP server must initialize before the first turn.

    - `ServerLabel string`

      A label used to identify the MCP server in tool calls.

    - `Transport PersistedMcpTransportUnion`

      The credential-free transport used to connect to the MCP server.

      - `type PersistedMcpTransportHTTP struct{…}`

        Connects to an MCP server over HTTP.

        - `Headers map[string, string]`

          Non-secret HTTP headers sent to the MCP server.

        - `ServerURL string`

          The URL of the MCP server.

        - `Type HTTP`

          The type of the object. Always `http`.

          - `const HTTPHTTP HTTP = "http"`

      - `type PersistedMcpTransportStdio struct{…}`

        Starts an MCP server as a local process.

        - `Args []string`

          Arguments passed to the MCP server command.

        - `Command string`

          The command used to start the MCP server.

        - `Cwd string`

          The working directory used to start the MCP server.

        - `EnvVars []string`

          Environment variable names inherited from the execution environment.

        - `Type Stdio`

          The type of the object. Always `stdio`.

          - `const StdioStdio Stdio = "stdio"`

    - `Type Mcp`

      The type of the object. Always `mcp`.

      - `const McpMcp Mcp = "mcp"`

  - `type PersistedAgentToolWebSearch struct{…}`

    Web search.

    - `AllowedDomains []string`

      Allowed search domains, or `null` when the search is unrestricted.

    - `ContextSize string`

      The amount of search context made available to the model. Defaults to `medium`.

      - `const PersistedAgentToolWebSearchContextSizeLow PersistedAgentToolWebSearchContextSize = "low"`

      - `const PersistedAgentToolWebSearchContextSizeMedium PersistedAgentToolWebSearchContextSize = "medium"`

      - `const PersistedAgentToolWebSearchContextSizeHigh PersistedAgentToolWebSearchContextSize = "high"`

    - `Location PersistedAgentToolWebSearchLocation`

      Approximate location used to localize search results, if provided.

      - `City string`

        The city name.

      - `Country string`

        The two-letter ISO country code, such as `US`.

      - `Region string`

        The region or state name.

      - `Timezone string`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode string`

      The source used for web search results.

      - `const PersistedAgentToolWebSearchModeDisabled PersistedAgentToolWebSearchMode = "disabled"`

      - `const PersistedAgentToolWebSearchModeCached PersistedAgentToolWebSearchMode = "cached"`

      - `const PersistedAgentToolWebSearchModeLive PersistedAgentToolWebSearchMode = "live"`

    - `Type WebSearch`

      The type of the object. Always `web_search`.

      - `const WebSearchWebSearch WebSearch = "web_search"`

  - `type PersistedAgentToolComputerUse struct{…}`

    Browser use in an OpenAI-hosted session.

    - `IncludeScreenshots bool`

      Whether computer tool outputs include screenshots.

    - `Type ComputerUse`

      The type of the object. Always `computer_use`.

      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

### Persisted Agent Tool Param

- `type PersistedAgentToolParamUnionResp interface{…}`

  A tool that can be stored on a reusable agent without session credentials.

  - `PersistedAgentToolParamFunctionResp`

    - `Description string`

      A description of what the function does.

    - `Name string`

      The name of the function.

    - `Parameters map[string, any]`

      A JSON Schema object describing the function's arguments.

    - `Type Function`

      The type of the object. Always `function`.

      - `const FunctionFunction Function = "function"`

    - `DeferLoading bool`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `PersistedAgentToolParamToolSearchResp`

    - `Type ToolSearch`

      The type of the object. Always `tool_search`.

      - `const ToolSearchToolSearch ToolSearch = "tool_search"`

  - `PersistedAgentToolParamProgrammaticToolCallingResp`

    - `Type ProgrammaticToolCalling`

      The type of the object. Always `programmatic_tool_calling`.

      - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

    - `Enabled bool`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `PersistedAgentToolParamMcpResp`

    - `ServerLabel string`

      A label used to identify the MCP server in tool calls.

    - `Transport PersistedMcpTransportParamUnionResp`

      The credential-free transport used to connect to the MCP server.

      - `PersistedMcpTransportParamHTTPResp`

        - `ServerURL string`

          The URL of the MCP server.

        - `Type HTTP`

          The type of the object. Always `http`.

          - `const HTTPHTTP HTTP = "http"`

        - `Headers map[string, string]`

          Non-secret HTTP headers sent to the MCP server.

      - `PersistedMcpTransportParamStdioResp`

        - `Command string`

          The command used to start the MCP server.

        - `Cwd string`

          The working directory used to start the MCP server.

        - `Type Stdio`

          The type of the object. Always `stdio`.

          - `const StdioStdio Stdio = "stdio"`

        - `Args []string`

          Arguments passed to the MCP server command.

        - `EnvVars []string`

          Environment variable names to inherit from the selected execution environment.

    - `Type Mcp`

      The type of the object. Always `mcp`.

      - `const McpMcp Mcp = "mcp"`

    - `AllowedTools []string`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `ConnectionOrigin string`

      Selects where outbound MCP HTTP connections originate.

      - `const PersistedAgentToolParamMcpConnectionOriginService PersistedAgentToolParamMcpConnectionOrigin = "service"`

        Uses the Managed Agents service network.

      - `const PersistedAgentToolParamMcpConnectionOriginEnvironment PersistedAgentToolParamMcpConnectionOrigin = "environment"`

        Uses the session's execution environment.

    - `CredentialID string`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `RequestMetadata map[string, any]`

      Metadata included with requests to this MCP server.

    - `Required bool`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `PersistedAgentToolParamWebSearchResp`

    - `Type WebSearch`

      The type of the object. Always `web_search`.

      - `const WebSearchWebSearch WebSearch = "web_search"`

    - `AllowedDomains []string`

      Domains the search may include.

    - `ContextSize string`

      The amount of search context made available to the model. Defaults to `medium`.

      - `const PersistedAgentToolParamWebSearchContextSizeLow PersistedAgentToolParamWebSearchContextSize = "low"`

      - `const PersistedAgentToolParamWebSearchContextSizeMedium PersistedAgentToolParamWebSearchContextSize = "medium"`

      - `const PersistedAgentToolParamWebSearchContextSizeHigh PersistedAgentToolParamWebSearchContextSize = "high"`

    - `Location PersistedAgentToolParamWebSearchLocationResp`

      Approximate location used to localize search results.

      - `City string`

        The city name.

      - `Country string`

        The two-letter ISO country code, such as `US`.

      - `Region string`

        The region or state name.

      - `Timezone string`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode string`

      The source used for web search results. Defaults to `live`.

      - `const PersistedAgentToolParamWebSearchModeDisabled PersistedAgentToolParamWebSearchMode = "disabled"`

        Disables web search.

      - `const PersistedAgentToolParamWebSearchModeCached PersistedAgentToolParamWebSearchMode = "cached"`

        Uses cached search results.

      - `const PersistedAgentToolParamWebSearchModeLive PersistedAgentToolParamWebSearchMode = "live"`

        Searches the live web.

  - `PersistedAgentToolParamComputerUseResp`

    - `Type ComputerUse`

      The type of the object. Always `computer_use`.

      - `const ComputerUseComputerUse ComputerUse = "computer_use"`

    - `IncludeScreenshots bool`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Persisted Mcp Transport

- `type PersistedMcpTransportUnion interface{…}`

  A credential-free transport used to connect to an MCP server.

  - `type PersistedMcpTransportHTTP struct{…}`

    Connects to an MCP server over HTTP.

    - `Headers map[string, string]`

      Non-secret HTTP headers sent to the MCP server.

    - `ServerURL string`

      The URL of the MCP server.

    - `Type HTTP`

      The type of the object. Always `http`.

      - `const HTTPHTTP HTTP = "http"`

  - `type PersistedMcpTransportStdio struct{…}`

    Starts an MCP server as a local process.

    - `Args []string`

      Arguments passed to the MCP server command.

    - `Command string`

      The command used to start the MCP server.

    - `Cwd string`

      The working directory used to start the MCP server.

    - `EnvVars []string`

      Environment variable names inherited from the execution environment.

    - `Type Stdio`

      The type of the object. Always `stdio`.

      - `const StdioStdio Stdio = "stdio"`

### Persisted Mcp Transport Param

- `type PersistedMcpTransportParamUnionResp interface{…}`

  A credential-free transport used to connect to an MCP server.

  - `PersistedMcpTransportParamHTTPResp`

    - `ServerURL string`

      The URL of the MCP server.

    - `Type HTTP`

      The type of the object. Always `http`.

      - `const HTTPHTTP HTTP = "http"`

    - `Headers map[string, string]`

      Non-secret HTTP headers sent to the MCP server.

  - `PersistedMcpTransportParamStdioResp`

    - `Command string`

      The command used to start the MCP server.

    - `Cwd string`

      The working directory used to start the MCP server.

    - `Type Stdio`

      The type of the object. Always `stdio`.

      - `const StdioStdio Stdio = "stdio"`

    - `Args []string`

      Arguments passed to the MCP server command.

    - `EnvVars []string`

      Environment variable names to inherit from the selected execution environment.

### Session Error

- `type SessionError struct{…}`

  An error payload with the same public fields as Responses API streaming errors.

  - `Code string`

    The machine-readable error code, if any.

  - `Message string`

    A customer-safe explanation of the error.

  - `Param string`

    The request parameter associated with the error, if any.

  - `Type string`

    The error type.

### Session Turn Error

- `type SessionTurnError struct{…}`

  A customer-safe error describing why a session request failed.

  - `Code SessionTurnErrorCode`

    A stable, machine-readable failure category.

    - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

      The request exceeds the model's context window.

    - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

      The session has reached its usage budget.

    - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

      The organization has reached a usage, plan, or billing limit.

    - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

      The organization has no API credits remaining.

    - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

      The request exceeds the available rate limit.

    - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

      Flex processing is temporarily unavailable.

    - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

      The model service is temporarily overloaded.

    - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

      The request was rejected by a safety policy.

    - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

      The request was blocked by the safety systems.

    - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

      The request could not connect to the model service.

    - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

      The model service encountered an unexpected error.

    - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

      The API credentials are invalid or lack the required access.

    - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

      The request contains invalid input or configuration.

    - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

      The requested model or resource is unavailable.

    - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

      The request could not complete in its execution environment.

    - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

      The executor must be upgraded before it can run this turn.

    - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

      The session cannot accept additional input while a request is running.

    - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

      The request timed out before the model service responded.

    - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

      An unexpected internal error prevented the session request from completing.

  - `Message string`

    A customer-safe explanation of the failure.

### Setup Command Param

- `type SetupCommandParamResp struct{…}`

  A confidential setup command executed before the hosted agent starts.

  - `Command string`

    The shell command to execute.

  - `Cwd string`

    The absolute working directory. Defaults to `/workspace`.

### Subagent

- `type Subagent struct{…}`

  A subagent created within a session.

  - `ID string`

    The ID of the subagent.

  - `ClosedAt int64`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Instructions []AgentContentUnion`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `type OutputText struct{…}`

      A text content part produced by the agent.

      - `Text string`

        The text produced by the agent.

      - `Type OutputText`

        The content type. Always `output_text`.

        - `const OutputTextOutputText OutputText = "output_text"`

    - `type AgentContentEncryptedContent struct{…}`

      Encrypted content exchanged between agents.

      - `EncryptedContent string`

        The encrypted content payload.

      - `Type EncryptedContent`

        The content type. Always `encrypted_content`.

        - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

  - `Name string`

    The runner-assigned nickname, or null when unavailable.

  - `Object SubagentObject`

    The object type. Always `agent.session.subagent`.

    - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

  - `OpenedAt int64`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `ParentAgentID string`

    The ID of the agent that created this subagent.

  - `SessionID string`

    The ID of the session that owns the subagent.

  - `Status SubagentStatus`

    The current status of the subagent.

    - `const SubagentStatusActive SubagentStatus = "active"`

      The subagent remains available, including while idle between turns.

    - `const SubagentStatusClosed SubagentStatus = "closed"`

      The subagent is closed.

### Summary Text

- `type SummaryText struct{…}`

  A reasoning summary content part.

  - `Text string`

    The reasoning summary text.

  - `Type SummaryText`

    The content type. Always `summary_text`.

    - `const SummaryTextSummaryText SummaryText = "summary_text"`

### Text Format

- `type TextFormatUnion interface{…}`

  The effective output format for generated text.

  - `type TextFormatText struct{…}`

    Generates ordinary text without a structured-output constraint.

    - `Type Text`

      The type of the object. Always `text`.

      - `const TextText Text = "text"`

  - `type TextFormatJSONSchema struct{…}`

    Constrains generated text to a JSON Schema.

    - `Schema map[string, any]`

      The JSON Schema that generated text must match.

    - `Type JSONSchema`

      The type of the object. Always `json_schema`.

      - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

### Text Format Param

- `type TextFormatParamUnionResp interface{…}`

  The output format for generated text.

  - `TextFormatParamTextResp`

    - `Type Text`

      The type of the object. Always `text`.

      - `const TextText Text = "text"`

  - `TextFormatParamJSONSchemaResp`

    - `Schema map[string, any]`

      The JSON Schema that generated text must match.

    - `Type JSONSchema`

      The type of the object. Always `json_schema`.

      - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

### Token Usage

- `type TokenUsage struct{…}`

  Recorded token usage for a session or turn. Usage is best effort and may change.

  - `InputTokens int64`

    The number of input tokens used by the agent.

  - `InputTokensDetails TokenUsageInputTokensDetails`

    A breakdown of the agent's input token usage.

    - `CachedTokens int64`

      The number of input tokens retrieved from the prompt cache.

  - `OutputTokens int64`

    The number of output tokens generated by the agent.

  - `OutputTokensDetails TokenUsageOutputTokensDetails`

    A breakdown of the agent's output token usage.

    - `ReasoningTokens int64`

      The number of output tokens used for reasoning.

  - `TotalTokens int64`

    The total number of input and output tokens used by the agent.

### Web Search Action

- `type WebSearchActionUnion interface{…}`

  An action performed by the web search tool.

  - `type WebSearchActionSearch struct{…}`

    A search query or group of search queries.

    - `Queries []string`

      The search queries, when multiple queries were used.

    - `Query string`

      The search query, when a single query was used.

    - `Type Search`

      The type of the object. Always `search`.

      - `const SearchSearch Search = "search"`

  - `type WebSearchActionOpenPage struct{…}`

    Opens a web page.

    - `Type OpenPage`

      The type of the object. Always `open_page`.

      - `const OpenPageOpenPage OpenPage = "open_page"`

    - `URL string`

      The URL of the page that was opened.

  - `type WebSearchActionFindInPage struct{…}`

    Finds text within a web page.

    - `Pattern string`

      The text pattern that was searched for.

    - `Type FindInPage`

      The type of the object. Always `find_in_page`.

      - `const FindInPageFindInPage FindInPage = "find_in_page"`

    - `URL string`

      The URL of the page that was searched.

  - `type WebSearchActionOther struct{…}`

    Another web search action.

    - `Type Other`

      The type of the object. Always `other`.

      - `const OtherOther Other = "other"`

# Environments

## Retrieve an agent environment

`client.Beta.Agents.Environments.Get(ctx, environmentID) (*EnvironmentInfo, error)`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `environmentID string`

### Returns

- `type EnvironmentInfo struct{…}`

  Safe metadata for a first-class execution environment.

  - `ID string`

    The ID of the environment.

  - `Files []HostedEnvironmentFileUnion`

    Files installed in the environment, without their contents.

    - `type HostedEnvironmentFileID struct{…}`

      A file copied from the OpenAI Files API.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type HostedEnvironmentFileInline struct{…}`

      A file supplied inline when the session was created.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Object AgentEnvironment`

    The object type. Always `agent.environment`.

    - `const AgentEnvironmentAgentEnvironment AgentEnvironment = "agent.environment"`

  - `Plugins []HostedPlugin`

    Plugins installed in the environment, without their archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []HostedSkillUnion`

    Skills installed in the environment, without their archive contents.

    - `type HostedSkillReference struct{…}`

      A skill installed from the Skills API.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The concrete skill version installed for this session.

    - `type HostedSkillInline struct{…}`

      A skill installed from an inline ZIP archive.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Status EnvironmentInfoStatus`

    The current environment connection status.

    - `const EnvironmentInfoStatusPending EnvironmentInfoStatus = "pending"`

    - `const EnvironmentInfoStatusConnected EnvironmentInfoStatus = "connected"`

    - `const EnvironmentInfoStatusDisconnected EnvironmentInfoStatus = "disconnected"`

    - `const EnvironmentInfoStatusExpired EnvironmentInfoStatus = "expired"`

    - `const EnvironmentInfoStatusFailed EnvironmentInfoStatus = "failed"`

  - `Type EnvironmentInfoType`

    Whether the environment is hosted by OpenAI or by the application.

    - `const EnvironmentInfoTypeOpenAIHosted EnvironmentInfoType = "openai_hosted"`

    - `const EnvironmentInfoTypeSelfHosted EnvironmentInfoType = "self_hosted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentInfo, err := client.Beta.Agents.Environments.Get(context.TODO(), "environment_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentInfo.ID)
}
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

- `type EnvironmentInfo struct{…}`

  Safe metadata for a first-class execution environment.

  - `ID string`

    The ID of the environment.

  - `Files []HostedEnvironmentFileUnion`

    Files installed in the environment, without their contents.

    - `type HostedEnvironmentFileID struct{…}`

      A file copied from the OpenAI Files API.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type HostedEnvironmentFileInline struct{…}`

      A file supplied inline when the session was created.

      - `ID string`

        The session-scoped ID of the file in the execution environment.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded file size in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Object AgentEnvironment`

    The object type. Always `agent.environment`.

    - `const AgentEnvironmentAgentEnvironment AgentEnvironment = "agent.environment"`

  - `Plugins []HostedPlugin`

    Plugins installed in the environment, without their archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []HostedSkillUnion`

    Skills installed in the environment, without their archive contents.

    - `type HostedSkillReference struct{…}`

      A skill installed from the Skills API.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The concrete skill version installed for this session.

    - `type HostedSkillInline struct{…}`

      A skill installed from an inline ZIP archive.

      - `Description string`

        The installed skill description.

      - `Name string`

        The installed skill name.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Status EnvironmentInfoStatus`

    The current environment connection status.

    - `const EnvironmentInfoStatusPending EnvironmentInfoStatus = "pending"`

    - `const EnvironmentInfoStatusConnected EnvironmentInfoStatus = "connected"`

    - `const EnvironmentInfoStatusDisconnected EnvironmentInfoStatus = "disconnected"`

    - `const EnvironmentInfoStatusExpired EnvironmentInfoStatus = "expired"`

    - `const EnvironmentInfoStatusFailed EnvironmentInfoStatus = "failed"`

  - `Type EnvironmentInfoType`

    Whether the environment is hosted by OpenAI or by the application.

    - `const EnvironmentInfoTypeOpenAIHosted EnvironmentInfoType = "openai_hosted"`

    - `const EnvironmentInfoTypeSelfHosted EnvironmentInfoType = "self_hosted"`

# Files

## Create an agent environment file

`client.Beta.Agents.Environments.Files.New(ctx, environmentID, body) (*EnvironmentFile, error)`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID string`

- `body BetaAgentEnvironmentFileNewParams`

  - `FileID param.Field[string]`

    The ID of the uploaded file.

  - `Path param.Field[string]`

    The absolute destination path inside `/workspace`.

  - `Type param.Field[FileID]`

    The type of the object. Always `file_id`.

    - `const FileIDFileID FileID = "file_id"`

### Returns

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentFile, err := client.Beta.Agents.Environments.Files.New(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileNewParams{
      HostedEnvironmentFileParamUnionResp: map[string]any{},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentFile.EnvironmentID)
}
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

`client.Beta.Agents.Environments.Files.List(ctx, environmentID, query) (*TokenPage[EnvironmentFile], error)`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `environmentID string`

- `query BetaAgentEnvironmentFileListParams`

  - `Limit param.Field[int64]`

    The maximum number of files to return, between 1 and 100.

  - `Order param.Field[BetaAgentEnvironmentFileListParamsOrder]`

    Sort by case-sensitive path components. Defaults to descending.

    - `const BetaAgentEnvironmentFileListParamsOrderAsc BetaAgentEnvironmentFileListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentFileListParamsOrderDesc BetaAgentEnvironmentFileListParamsOrder = "desc"`

      Returns resources in descending order.

  - `Page param.Field[string]`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `Path param.Field[string]`

    Restrict the listing to this absolute workspace directory.

### Returns

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Environments.Files.List(
    context.TODO(),
    "environment_id",
    openai.BetaAgentEnvironmentFileListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

- `type EnvironmentFile struct{…}`

  A live file in an execution environment.

  - `EnvironmentID string`

    The ID of the environment containing this file.

  - `Object AgentEnvironmentFile`

    The object type. Always `agent.environment.file`.

    - `const AgentEnvironmentFileAgentEnvironmentFile AgentEnvironmentFile = "agent.environment.file"`

  - `Path string`

    The absolute file path inside the environment's workspace.

  - `SizeBytes int64`

    The file size in bytes.

# Templates

## Create an agent environment template

`client.Beta.Agents.Environments.Templates.New(ctx, body) (*EnvironmentTemplate, error)`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `body BetaAgentEnvironmentTemplateNewParams`

  - `CapabilityDirectories param.Field[[]string]`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `Desktop param.Field[BetaAgentEnvironmentTemplateNewParamsDesktop]`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `Enabled bool`

      Whether to provision the desktop and its browser proxy.

  - `Env param.Field[map[string, string]]`

    Environment variables made available to the agent.

  - `Files param.Field[[]HostedEnvironmentFileParamUnionResp]`

    Files available before the agent starts. Defaults to an empty list.

    - `HostedEnvironmentFileParamFileIDResp`

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `HostedEnvironmentFileParamInlineResp`

      - `Data string`

        The standard-base64-encoded file contents.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name param.Field[string]`

    An optional human-readable display name for the template.

  - `Network param.Field[BetaAgentEnvironmentTemplateNewParamsNetwork]`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

    - `Access string`

      The environment's network access mode.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessEnabled BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessDisabled BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "disabled"`

        Disables network access.

      - `const BetaAgentEnvironmentTemplateNewParamsNetworkAccessRestricted BetaAgentEnvironmentTemplateNewParamsNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

    - `BlockedDomains []string`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Packages param.Field[BetaAgentEnvironmentTemplateNewParamsPackages]`

    Packages to install in the environment. Defaults to empty package lists.

    - `Npm []string`

      npm packages to install globally. Defaults to an empty list.

    - `Python []string`

      Python packages to install. Defaults to an empty list.

    - `System []string`

      System packages to install. Defaults to an empty list.

  - `Plugins param.Field[[]HostedPluginParamResp]`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `Description string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `Name string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `Source InlineCapabilitySourceParamResp`

      Provides ZIP bytes encoded with standard base64.

      - `Data string`

        Standard-base64 encoded ZIP archive bytes.

      - `MediaType ApplicationZip`

        The archive media type, always `application/zip`.

        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

          A ZIP archive.

      - `Type Base64`

        The type of the object. Always `base64`.

        - `const Base64Base64 Base64 = "base64"`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `SetupCommands param.Field[[]SetupCommandParamResp]`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `Command string`

      The shell command to execute.

    - `Cwd string`

      The absolute working directory. Defaults to `/workspace`.

  - `Skills param.Field[[]HostedSkillParamUnionResp]`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `HostedSkillParamSkillReferenceResp`

      - `SkillID string`

        The ID of the skill created through `/v1/skills`.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInlineResp`

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.New(context.TODO(), openai.BetaAgentEnvironmentTemplateNewParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

`client.Beta.Agents.Environments.Templates.Delete(ctx, environmentTemplateID) (*EnvironmentTemplateDeleted, error)`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

### Returns

- `type EnvironmentTemplateDeleted struct{…}`

  A deleted reusable environment template.

  - `ID string`

    The ID of the deleted environment template.

  - `Deleted bool`

    Whether the environment template was deleted. Always `true`.

  - `Object AgentEnvironmentTemplateDeleted`

    The object type. Always `agent.environment.template.deleted`.

    - `const AgentEnvironmentTemplateDeletedAgentEnvironmentTemplateDeleted AgentEnvironmentTemplateDeleted = "agent.environment.template.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplateDeleted, err := client.Beta.Agents.Environments.Templates.Delete(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplateDeleted.ID)
}
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

`client.Beta.Agents.Environments.Templates.List(ctx, query) (*CursorPage[EnvironmentTemplate], error)`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `query BetaAgentEnvironmentTemplateListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentEnvironmentTemplateListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentEnvironmentTemplateListParamsOrderAsc BetaAgentEnvironmentTemplateListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentEnvironmentTemplateListParamsOrderDesc BetaAgentEnvironmentTemplateListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Environments.Templates.List(context.TODO(), openai.BetaAgentEnvironmentTemplateListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Environments.Templates.Get(ctx, environmentTemplateID) (*EnvironmentTemplate, error)`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.Get(context.TODO(), "environment_template_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

`client.Beta.Agents.Environments.Templates.Update(ctx, environmentTemplateID, body) (*EnvironmentTemplate, error)`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `environmentTemplateID string`

- `body BetaAgentEnvironmentTemplateUpdateParams`

  - `CapabilityDirectories param.Field[[]string]`

    Directories that expose capabilities to the agent.

  - `Desktop param.Field[BetaAgentEnvironmentTemplateUpdateParamsDesktop]`

    Replacement desktop configuration, or null to disable the desktop.

    - `Enabled bool`

      Whether to provision the desktop and its browser proxy.

  - `Env param.Field[map[string, string]]`

    Replacement confidential environment values.

  - `Files param.Field[[]HostedEnvironmentFileParamUnionResp]`

    Replacement file configuration materialized for each new session.

    - `HostedEnvironmentFileParamFileIDResp`

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `HostedEnvironmentFileParamInlineResp`

      - `Data string`

        The standard-base64-encoded file contents.

      - `Path string`

        The absolute destination path inside `/workspace`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name param.Field[string]`

    A replacement human-readable display name, or `null` to clear the name.

  - `Network param.Field[BetaAgentEnvironmentTemplateUpdateParamsNetwork]`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

    - `Access string`

      The environment's network access mode.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessEnabled BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessDisabled BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "disabled"`

        Disables network access.

      - `const BetaAgentEnvironmentTemplateUpdateParamsNetworkAccessRestricted BetaAgentEnvironmentTemplateUpdateParamsNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

    - `BlockedDomains []string`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Packages param.Field[BetaAgentEnvironmentTemplateUpdateParamsPackages]`

    Packages installed before the runtime network policy applies.

    - `Npm []string`

      npm packages to install globally. Defaults to an empty list.

    - `Python []string`

      Python packages to install. Defaults to an empty list.

    - `System []string`

      System packages to install. Defaults to an empty list.

  - `Plugins param.Field[[]HostedPluginParamResp]`

    Replacement plugin configuration installed for each new session.

    - `Description string`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `Name string`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `Source InlineCapabilitySourceParamResp`

      Provides ZIP bytes encoded with standard base64.

      - `Data string`

        Standard-base64 encoded ZIP archive bytes.

      - `MediaType ApplicationZip`

        The archive media type, always `application/zip`.

        - `const ApplicationZipApplicationZip ApplicationZip = "application/zip"`

          A ZIP archive.

      - `Type Base64`

        The type of the object. Always `base64`.

        - `const Base64Base64 Base64 = "base64"`

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `SetupCommands param.Field[[]SetupCommandParamResp]`

    Replacement confidential setup commands, never included in returned resources.

    - `Command string`

      The shell command to execute.

    - `Cwd string`

      The absolute working directory. Defaults to `/workspace`.

  - `Skills param.Field[[]HostedSkillParamUnionResp]`

    Replacement skill configuration installed for each new session.

    - `HostedSkillParamSkillReferenceResp`

      - `SkillID string`

        The ID of the skill created through `/v1/skills`.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `HostedSkillParamInlineResp`

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Source InlineCapabilitySourceParamResp`

        Provides ZIP bytes encoded with standard base64.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

### Returns

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  environmentTemplate, err := client.Beta.Agents.Environments.Templates.Update(
    context.TODO(),
    "environment_template_id",
    openai.BetaAgentEnvironmentTemplateUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", environmentTemplate.ID)
}
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

- `type EnvironmentTemplate struct{…}`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `ID string`

    The ID of the reusable environment template.

  - `CapabilityDirectories []string`

    Directories that expose capabilities to the agent.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop EnvironmentTemplateDesktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `Enabled bool`

      Whether the environment provisions a desktop and browser proxy.

  - `Files []EnvironmentTemplateFileUnion`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `type EnvironmentTemplateFileFileID struct{…}`

      A project-scoped Files API reference resolved separately for each session.

      - `FileID string`

        The ID of the uploaded file.

      - `Path string`

        The file's absolute path inside the environment.

      - `Type FileID`

        The type of the object. Always `file_id`.

        - `const FileIDFileID FileID = "file_id"`

    - `type EnvironmentTemplateFileInline struct{…}`

      Metadata for confidential inline file contents.

      - `Path string`

        The file's absolute path inside the environment.

      - `SizeBytes int64`

        The decoded size of the inline file in bytes.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `Name string`

    An optional human-readable display name for the template.

  - `Network EnvironmentTemplateNetwork`

    Runtime network access for each OpenAI-hosted environment.

    - `Access string`

      The environment's network access mode.

      - `const EnvironmentTemplateNetworkAccessEnabled EnvironmentTemplateNetworkAccess = "enabled"`

        Allows unrestricted network access.

      - `const EnvironmentTemplateNetworkAccessDisabled EnvironmentTemplateNetworkAccess = "disabled"`

        Disables network access.

      - `const EnvironmentTemplateNetworkAccessRestricted EnvironmentTemplateNetworkAccess = "restricted"`

        Applies the configured domain restrictions.

    - `AllowedDomains []string`

      Domains the environment may access when network access is restricted.

  - `Object AgentEnvironmentTemplate`

    The object type. Always `agent.environment.template`.

    - `const AgentEnvironmentTemplateAgentEnvironmentTemplate AgentEnvironmentTemplate = "agent.environment.template"`

  - `Packages EnvironmentTemplatePackages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `Npm []string`

      npm packages installed globally in the environment.

    - `Python []string`

      Python packages installed in the environment.

    - `System []string`

      System packages installed in the environment.

  - `Plugins []HostedPlugin`

    Safe plugin metadata, excluding inline archive contents.

    - `Description string`

      The installed plugin description.

    - `Name string`

      The installed plugin name.

    - `Type Inline`

      The type of the object. Always `inline`.

      - `const InlineInline Inline = "inline"`

  - `Skills []EnvironmentTemplateSkillUnion`

    Safe skill metadata, preserving unresolved version selectors.

    - `type EnvironmentTemplateSkillSkillReference struct{…}`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `SkillID string`

        The referenced skill ID.

      - `Type SkillReference`

        The type of the object. Always `skill_reference`.

        - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

      - `Version string`

        The requested version selector, including `latest`.

    - `type EnvironmentTemplateSkillInline struct{…}`

      Safe metadata for an inline skill archive.

      - `Description string`

        The skill description declared in `SKILL.md`.

      - `Name string`

        The skill name declared in `SKILL.md`.

      - `Type Inline`

        The type of the object. Always `inline`.

        - `const InlineInline Inline = "inline"`

  - `UpdatedAt int64`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `type EnvironmentTemplateDeleted struct{…}`

  A deleted reusable environment template.

  - `ID string`

    The ID of the deleted environment template.

  - `Deleted bool`

    Whether the environment template was deleted. Always `true`.

  - `Object AgentEnvironmentTemplateDeleted`

    The object type. Always `agent.environment.template.deleted`.

    - `const AgentEnvironmentTemplateDeletedAgentEnvironmentTemplateDeleted AgentEnvironmentTemplateDeleted = "agent.environment.template.deleted"`

# Sessions

## Create an agent session

`client.Beta.Agents.Sessions.New(ctx, body) (*AgentSession, error)`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `body BetaAgentSessionNewParams`

  - `Environment param.Field[EnvironmentParamUnionResp]`

    An inline execution environment or a reference to an environment template.

  - `Agent param.Field[BetaAgentSessionNewParamsAgent]`

    Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

    - `Instructions string`

      Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

    - `Model string`

      The model to use for the agent. The requested model name is preserved.

    - `MultiAgent MultiAgentConfigParamResp`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently. Defaults to 6.

    - `Reasoning AgentReasoningParamResp`

      Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

      - `Effort AgentReasoningParamEffort`

        The amount of reasoning effort the model should use. Omission lets the model select it.

        - `const AgentReasoningParamEffortNone AgentReasoningParamEffort = "none"`

        - `const AgentReasoningParamEffortMinimal AgentReasoningParamEffort = "minimal"`

        - `const AgentReasoningParamEffortLow AgentReasoningParamEffort = "low"`

        - `const AgentReasoningParamEffortMedium AgentReasoningParamEffort = "medium"`

        - `const AgentReasoningParamEffortHigh AgentReasoningParamEffort = "high"`

        - `const AgentReasoningParamEffortXhigh AgentReasoningParamEffort = "xhigh"`

        - `const AgentReasoningParamEffortMax AgentReasoningParamEffort = "max"`

      - `Summary AgentReasoningParamSummary`

        Controls whether the response includes a reasoning summary.

        - `const AgentReasoningParamSummaryConcise AgentReasoningParamSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningParamSummaryDetailed AgentReasoningParamSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningParamSummaryAuto AgentReasoningParamSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The service tier used for model requests.

      - `const BetaAgentSessionNewParamsAgentServiceTierAuto BetaAgentSessionNewParamsAgentServiceTier = "auto"`

        Selects the service tier automatically.

      - `const BetaAgentSessionNewParamsAgentServiceTierDefault BetaAgentSessionNewParamsAgentServiceTier = "default"`

        Uses the default service tier.

      - `const BetaAgentSessionNewParamsAgentServiceTierFlex BetaAgentSessionNewParamsAgentServiceTier = "flex"`

        Uses the flex service tier.

      - `const BetaAgentSessionNewParamsAgentServiceTierPriority BetaAgentSessionNewParamsAgentServiceTier = "priority"`

        Uses the priority service tier.

      - `const BetaAgentSessionNewParamsAgentServiceTierFast BetaAgentSessionNewParamsAgentServiceTier = "fast"`

        Uses the fast service tier.

      - `const BetaAgentSessionNewParamsAgentServiceTierUltrafast BetaAgentSessionNewParamsAgentServiceTier = "ultrafast"`

        Uses the ultrafast service tier.

    - `Text AgentTextParamResp`

      Configuration for text generated by the agent.

      - `Format TextFormatParamUnionResp`

        The output format. Omission uses ordinary text (`{"type": "text"}`).

        - `TextFormatParamTextResp`

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `TextFormatParamJSONSchemaResp`

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextParamVerbosity`

        The amount of text the model should produce. Defaults to `medium`, matching Responses.

        - `const AgentTextParamVerbosityLow AgentTextParamVerbosity = "low"`

          Produces less text.

        - `const AgentTextParamVerbosityMedium AgentTextParamVerbosity = "medium"`

          Uses the default amount of text.

        - `const AgentTextParamVerbosityHigh AgentTextParamVerbosity = "high"`

          Produces more text.

    - `Tools []AgentToolParamUnionResp`

      Tools available to the agent. Omit to inherit, or pass null to clear them.

      - `AgentToolParamFunctionResp`

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

        - `DeferLoading bool`

          Whether this function is deferred and discovered through tool search. Defaults to `false`.

      - `AgentToolParamToolSearchResp`

        - `Type ToolSearch`

          The type of the object. Always `tool_search`.

          - `const ToolSearchToolSearch ToolSearch = "tool_search"`

      - `AgentToolParamProgrammaticToolCallingResp`

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

        - `Enabled bool`

          Whether tools can be called from model-generated code. Defaults to `true`.

      - `AgentToolParamMcpResp`

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportParamUnionResp`

          The transport used to connect to the MCP server.

          - `McpTransportParamHTTPResp`

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

            - `Authorization string`

              The authorization value sent to the MCP server, if any.

            - `Headers map[string, string]`

              Additional HTTP headers sent to the MCP server.

          - `McpTransportParamStdioResp`

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Env map[string, string]`

              Environment variables set for the MCP server process.

            - `EnvVars []string`

              Environment variable names to inherit from the selected execution environment.

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

        - `AllowedTools []string`

          The MCP tools the agent may call. All server tools are allowed when omitted.

        - `ConnectionOrigin string`

          Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

          - `const AgentToolParamMcpConnectionOriginService AgentToolParamMcpConnectionOrigin = "service"`

            Uses the Managed Agents service network.

          - `const AgentToolParamMcpConnectionOriginEnvironment AgentToolParamMcpConnectionOrigin = "environment"`

            Uses the session's execution environment.

        - `CredentialID string`

          The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn. Defaults to `false`.

      - `AgentToolParamWebSearchResp`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

        - `AllowedDomains []string`

          Domains the search may include.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolParamWebSearchContextSizeLow AgentToolParamWebSearchContextSize = "low"`

          - `const AgentToolParamWebSearchContextSizeMedium AgentToolParamWebSearchContextSize = "medium"`

          - `const AgentToolParamWebSearchContextSizeHigh AgentToolParamWebSearchContextSize = "high"`

        - `Location AgentToolParamWebSearchLocationResp`

          Approximate location used to localize search results.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results. Defaults to `live`.

          - `const AgentToolParamWebSearchModeDisabled AgentToolParamWebSearchMode = "disabled"`

            Disables web search.

          - `const AgentToolParamWebSearchModeCached AgentToolParamWebSearchMode = "cached"`

            Uses cached search results.

          - `const AgentToolParamWebSearchModeLive AgentToolParamWebSearchMode = "live"`

            Searches the live web.

      - `AgentToolParamComputerUseResp`

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots. Defaults to `false`.

  - `AgentID param.Field[string]`

    The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

  - `Input param.Field[BetaAgentSessionNewParamsInputUnion]`

    Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

    - `string`

    - `[]AgentSessionInputMessageParam`

      - `Content []InputContentParamUnionResp`

        The content of the message.

        - `InputContentParamInputTextResp`

          - `Text string`

            The text sent to the model.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `InputContentParamInputImageResp`

          - `ImageURL string`

            The URL of the image sent to the model.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

      - `Role User`

        The role of the message author. Always `user`.

        - `const UserUser User = "user"`

      - `Type AgentSessionInputMessageParamType`

        The type of the input item. Always `message`.

        - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

  - `Metadata param.Field[map[string, string]]`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

  - ``

  - `VaultIDs param.Field[[]string]`

    The IDs of vaults made available to the session.

### Returns

- `type AgentSession struct{…}`

  A Managed Agents session.

  - `ID string`

    The ID of the session.

  - `Agent AgentSessionAgent`

    The agent running in the session.

    - `ID string`

      The ID of the agent.

    - `Instructions string`

      Custom instructions appended to the agent's default base instructions.

    - `Model string`

      The model used by the agent.

    - `MultiAgent MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled. Defaults to false.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Name string`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `Reasoning AgentReasoning`

      The agent's reasoning configuration.

      - `Effort AgentReasoningEffort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

        - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

        - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

        - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

        - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

        - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

        - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

      - `Summary AgentReasoningSummary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

      - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

      - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

      - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

      - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

      - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

    - `Text AgentText`

      Configuration for text generated by the agent.

      - `Format TextFormatUnion`

        The effective output format. Defaults to ordinary text.

        - `type TextFormatText struct{…}`

          Generates ordinary text without a structured-output constraint.

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `type TextFormatJSONSchema struct{…}`

          Constrains generated text to a JSON Schema.

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextVerbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

        - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

        - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

    - `Tools []AgentToolUnion`

      Tools available to the agent.

      - `type AgentToolFunction struct{…}`

        A function defined by the application.

        - `DeferLoading bool`

          Whether the function is deferred and discovered through tool search.

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

      - `type AgentToolProgrammaticToolCalling struct{…}`

        Enables calling tools from model-generated code.

        - `Enabled bool`

          Whether tools can be called from model-generated code.

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `type AgentToolMcp struct{…}`

        Tools provided by a remote MCP server.

        - `AllowedTools []string`

          The MCP tools the agent may call.

        - `ConnectionOrigin string`

          Where outbound MCP HTTP connections originate.

          - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

          - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

        - `CredentialID string`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn.

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportUnion`

          The transport used to connect to the MCP server.

          - `type McpTransportHTTP struct{…}`

            Connects to an MCP server over HTTP.

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

          - `type McpTransportStdio struct{…}`

            Starts an MCP server as a local process.

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `EnvVars []string`

              Environment variable names inherited from the execution environment.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

      - `type AgentToolWebSearch struct{…}`

        Web search.

        - `AllowedDomains []string`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

          - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

          - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

        - `Location AgentToolWebSearchLocation`

          Approximate location used to localize search results, if provided.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results.

          - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

          - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

          - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

      - `type AgentToolComputerUse struct{…}`

        Browser use in an OpenAI-hosted session.

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots.

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment EnvironmentUnion`

    The execution environment for the session.

    - `type EnvironmentNone struct{…}`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `Type None`

        The type of the object. Always `none`.

        - `const NoneNone None = "none"`

    - `type EnvironmentOpenAIHosted struct{…}`

      An environment hosted by OpenAI.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `Desktop EnvironmentOpenAIHostedDesktop`

        The effective desktop configuration.

        - `Enabled bool`

          Whether the environment provisions a desktop and browser proxy.

      - `Files []HostedEnvironmentFileUnion`

        Files available in the environment, excluding their contents.

        - `type HostedEnvironmentFileID struct{…}`

          A file copied from the OpenAI Files API.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `FileID string`

            The ID of the uploaded file.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type FileID`

            The type of the object. Always `file_id`.

            - `const FileIDFileID FileID = "file_id"`

        - `type HostedEnvironmentFileInline struct{…}`

          A file supplied inline when the session was created.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Network EnvironmentOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `Access string`

          The environment's network access mode.

          - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

            Allows unrestricted network access.

          - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

            Disables network access.

          - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

            Applies the configured domain restrictions.

        - `AllowedDomains []string`

          Domains the environment may access when network access is restricted.

      - `Packages EnvironmentOpenAIHostedPackages`

        Packages installed in the environment.

        - `Npm []string`

          npm packages installed globally in the environment.

        - `Python []string`

          Python packages installed in the environment.

        - `System []string`

          System packages installed in the environment.

      - `Plugins []HostedPlugin`

        Plugins installed in the environment, excluding their archive contents.

        - `Description string`

          The installed plugin description.

        - `Name string`

          The installed plugin name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

      - `Skills []HostedSkillUnion`

        Skills installed in the environment, excluding their archive contents.

        - `type HostedSkillReference struct{…}`

          A skill installed from the Skills API.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `SkillID string`

            The referenced skill ID.

          - `Type SkillReference`

            The type of the object. Always `skill_reference`.

            - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

          - `Version string`

            The concrete skill version installed for this session.

        - `type HostedSkillInline struct{…}`

          A skill installed from an inline ZIP archive.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Type OpenAIHosted`

        The type of the object. Always `openai_hosted`.

        - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `ContainerSize string`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

        - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

        - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

    - `type EnvironmentSelfHosted struct{…}`

      An environment hosted by the application.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `RemoteURL string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `Type SelfHosted`

        The type of the object. Always `self_hosted`.

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

      - `WorkspaceDirectory string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Error string`

    The error that caused the session to fail, if any.

  - `LastActiveAt int64`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the session.

  - `Object AgentSession`

    The object type. Always `agent.session`.

    - `const AgentSessionAgentSession AgentSession = "agent.session"`

  - `RequiredActions []AgentSessionRequiredActionUnion`

    Actions that must be completed before the session can continue.

    - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

      Respond to a computer-use request.

      - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

        The information needed to render the request.

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

          A browser origin awaiting the application's approval decision.

          - `Origin string`

            The origin the browser needs permission to access.

          - `Reason string`

            The browser's explanation for this request, or null when unavailable.

          - `Type BrowserOriginAccess`

            The type of the object. Always `browser_origin_access`.

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `RequestID string`

        The registered request ID to echo when responding.

      - `TurnID string`

        The turn that requested approval.

      - `Type ComputerUseApprovalRequest`

        The type of the object. Always `computer_use_approval_request`.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionRequiredActionFunctionCall struct{…}`

      Run a function tool and submit its result.

      - `Arguments any`

        The arguments supplied by the model.

      - `CallID string`

        The ID to include when submitting the function result.

      - `Name string`

        The function name.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type FunctionCall`

        The type of the object. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

      Reconnect a session environment.

      - `EnvironmentID string`

        The ID of the environment to reconnect.

      - `Type EnvironmentConnection`

        The type of the object. Always `environment_connection`.

        - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

  - `Status AgentSessionStatus`

    The current status of the session.

    - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

      The session is processing a turn.

    - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

      The session is waiting for one or more required actions.

    - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

      The session failed.

  - `Usage TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

  - `VaultIDs []string`

    The IDs of vaults made available to the session.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agentSession, err := client.Beta.Agents.Sessions.New(context.TODO(), openai.BetaAgentSessionNewParams{
    Environment: openai.EnvironmentParamUnion{
      OfNone: &openai.EnvironmentParamNone{

      },
    },
  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentSession.ID)
}
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

`client.Beta.Agents.Sessions.Delete(ctx, sessionID) (*AgentSessionDeleted, error)`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID string`

### Returns

- `type AgentSessionDeleted struct{…}`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `ID string`

    The ID of the deleted session.

  - `Deleted bool`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `Object AgentSessionDeleted`

    The object type. Always `agent.session.deleted`.

    - `const AgentSessionDeletedAgentSessionDeleted AgentSessionDeleted = "agent.session.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agentSessionDeleted, err := client.Beta.Agents.Sessions.Delete(context.TODO(), "session_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentSessionDeleted.ID)
}
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

`client.Beta.Agents.Sessions.List(ctx, query) (*CursorPage[AgentSession], error)`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `query BetaAgentSessionListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `AgentID param.Field[string]`

    Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

  - `Limit param.Field[int64]`

    The maximum number of resources to return.

  - `Order param.Field[BetaAgentSessionListParamsOrder]`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `const BetaAgentSessionListParamsOrderAsc BetaAgentSessionListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionListParamsOrderDesc BetaAgentSessionListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AgentSession struct{…}`

  A Managed Agents session.

  - `ID string`

    The ID of the session.

  - `Agent AgentSessionAgent`

    The agent running in the session.

    - `ID string`

      The ID of the agent.

    - `Instructions string`

      Custom instructions appended to the agent's default base instructions.

    - `Model string`

      The model used by the agent.

    - `MultiAgent MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled. Defaults to false.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Name string`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `Reasoning AgentReasoning`

      The agent's reasoning configuration.

      - `Effort AgentReasoningEffort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

        - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

        - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

        - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

        - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

        - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

        - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

      - `Summary AgentReasoningSummary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

      - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

      - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

      - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

      - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

      - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

    - `Text AgentText`

      Configuration for text generated by the agent.

      - `Format TextFormatUnion`

        The effective output format. Defaults to ordinary text.

        - `type TextFormatText struct{…}`

          Generates ordinary text without a structured-output constraint.

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `type TextFormatJSONSchema struct{…}`

          Constrains generated text to a JSON Schema.

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextVerbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

        - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

        - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

    - `Tools []AgentToolUnion`

      Tools available to the agent.

      - `type AgentToolFunction struct{…}`

        A function defined by the application.

        - `DeferLoading bool`

          Whether the function is deferred and discovered through tool search.

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

      - `type AgentToolProgrammaticToolCalling struct{…}`

        Enables calling tools from model-generated code.

        - `Enabled bool`

          Whether tools can be called from model-generated code.

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `type AgentToolMcp struct{…}`

        Tools provided by a remote MCP server.

        - `AllowedTools []string`

          The MCP tools the agent may call.

        - `ConnectionOrigin string`

          Where outbound MCP HTTP connections originate.

          - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

          - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

        - `CredentialID string`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn.

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportUnion`

          The transport used to connect to the MCP server.

          - `type McpTransportHTTP struct{…}`

            Connects to an MCP server over HTTP.

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

          - `type McpTransportStdio struct{…}`

            Starts an MCP server as a local process.

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `EnvVars []string`

              Environment variable names inherited from the execution environment.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

      - `type AgentToolWebSearch struct{…}`

        Web search.

        - `AllowedDomains []string`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

          - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

          - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

        - `Location AgentToolWebSearchLocation`

          Approximate location used to localize search results, if provided.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results.

          - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

          - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

          - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

      - `type AgentToolComputerUse struct{…}`

        Browser use in an OpenAI-hosted session.

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots.

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment EnvironmentUnion`

    The execution environment for the session.

    - `type EnvironmentNone struct{…}`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `Type None`

        The type of the object. Always `none`.

        - `const NoneNone None = "none"`

    - `type EnvironmentOpenAIHosted struct{…}`

      An environment hosted by OpenAI.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `Desktop EnvironmentOpenAIHostedDesktop`

        The effective desktop configuration.

        - `Enabled bool`

          Whether the environment provisions a desktop and browser proxy.

      - `Files []HostedEnvironmentFileUnion`

        Files available in the environment, excluding their contents.

        - `type HostedEnvironmentFileID struct{…}`

          A file copied from the OpenAI Files API.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `FileID string`

            The ID of the uploaded file.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type FileID`

            The type of the object. Always `file_id`.

            - `const FileIDFileID FileID = "file_id"`

        - `type HostedEnvironmentFileInline struct{…}`

          A file supplied inline when the session was created.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Network EnvironmentOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `Access string`

          The environment's network access mode.

          - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

            Allows unrestricted network access.

          - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

            Disables network access.

          - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

            Applies the configured domain restrictions.

        - `AllowedDomains []string`

          Domains the environment may access when network access is restricted.

      - `Packages EnvironmentOpenAIHostedPackages`

        Packages installed in the environment.

        - `Npm []string`

          npm packages installed globally in the environment.

        - `Python []string`

          Python packages installed in the environment.

        - `System []string`

          System packages installed in the environment.

      - `Plugins []HostedPlugin`

        Plugins installed in the environment, excluding their archive contents.

        - `Description string`

          The installed plugin description.

        - `Name string`

          The installed plugin name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

      - `Skills []HostedSkillUnion`

        Skills installed in the environment, excluding their archive contents.

        - `type HostedSkillReference struct{…}`

          A skill installed from the Skills API.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `SkillID string`

            The referenced skill ID.

          - `Type SkillReference`

            The type of the object. Always `skill_reference`.

            - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

          - `Version string`

            The concrete skill version installed for this session.

        - `type HostedSkillInline struct{…}`

          A skill installed from an inline ZIP archive.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Type OpenAIHosted`

        The type of the object. Always `openai_hosted`.

        - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `ContainerSize string`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

        - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

        - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

    - `type EnvironmentSelfHosted struct{…}`

      An environment hosted by the application.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `RemoteURL string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `Type SelfHosted`

        The type of the object. Always `self_hosted`.

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

      - `WorkspaceDirectory string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Error string`

    The error that caused the session to fail, if any.

  - `LastActiveAt int64`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the session.

  - `Object AgentSession`

    The object type. Always `agent.session`.

    - `const AgentSessionAgentSession AgentSession = "agent.session"`

  - `RequiredActions []AgentSessionRequiredActionUnion`

    Actions that must be completed before the session can continue.

    - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

      Respond to a computer-use request.

      - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

        The information needed to render the request.

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

          A browser origin awaiting the application's approval decision.

          - `Origin string`

            The origin the browser needs permission to access.

          - `Reason string`

            The browser's explanation for this request, or null when unavailable.

          - `Type BrowserOriginAccess`

            The type of the object. Always `browser_origin_access`.

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `RequestID string`

        The registered request ID to echo when responding.

      - `TurnID string`

        The turn that requested approval.

      - `Type ComputerUseApprovalRequest`

        The type of the object. Always `computer_use_approval_request`.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionRequiredActionFunctionCall struct{…}`

      Run a function tool and submit its result.

      - `Arguments any`

        The arguments supplied by the model.

      - `CallID string`

        The ID to include when submitting the function result.

      - `Name string`

        The function name.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type FunctionCall`

        The type of the object. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

      Reconnect a session environment.

      - `EnvironmentID string`

        The ID of the environment to reconnect.

      - `Type EnvironmentConnection`

        The type of the object. Always `environment_connection`.

        - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

  - `Status AgentSessionStatus`

    The current status of the session.

    - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

      The session is processing a turn.

    - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

      The session is waiting for one or more required actions.

    - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

      The session failed.

  - `Usage TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

  - `VaultIDs []string`

    The IDs of vaults made available to the session.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Sessions.List(context.TODO(), openai.BetaAgentSessionListParams{

  })
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Sessions.Get(ctx, sessionID) (*AgentSession, error)`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID string`

### Returns

- `type AgentSession struct{…}`

  A Managed Agents session.

  - `ID string`

    The ID of the session.

  - `Agent AgentSessionAgent`

    The agent running in the session.

    - `ID string`

      The ID of the agent.

    - `Instructions string`

      Custom instructions appended to the agent's default base instructions.

    - `Model string`

      The model used by the agent.

    - `MultiAgent MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled. Defaults to false.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Name string`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `Reasoning AgentReasoning`

      The agent's reasoning configuration.

      - `Effort AgentReasoningEffort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

        - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

        - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

        - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

        - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

        - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

        - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

      - `Summary AgentReasoningSummary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

      - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

      - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

      - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

      - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

      - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

    - `Text AgentText`

      Configuration for text generated by the agent.

      - `Format TextFormatUnion`

        The effective output format. Defaults to ordinary text.

        - `type TextFormatText struct{…}`

          Generates ordinary text without a structured-output constraint.

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `type TextFormatJSONSchema struct{…}`

          Constrains generated text to a JSON Schema.

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextVerbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

        - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

        - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

    - `Tools []AgentToolUnion`

      Tools available to the agent.

      - `type AgentToolFunction struct{…}`

        A function defined by the application.

        - `DeferLoading bool`

          Whether the function is deferred and discovered through tool search.

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

      - `type AgentToolProgrammaticToolCalling struct{…}`

        Enables calling tools from model-generated code.

        - `Enabled bool`

          Whether tools can be called from model-generated code.

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `type AgentToolMcp struct{…}`

        Tools provided by a remote MCP server.

        - `AllowedTools []string`

          The MCP tools the agent may call.

        - `ConnectionOrigin string`

          Where outbound MCP HTTP connections originate.

          - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

          - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

        - `CredentialID string`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn.

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportUnion`

          The transport used to connect to the MCP server.

          - `type McpTransportHTTP struct{…}`

            Connects to an MCP server over HTTP.

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

          - `type McpTransportStdio struct{…}`

            Starts an MCP server as a local process.

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `EnvVars []string`

              Environment variable names inherited from the execution environment.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

      - `type AgentToolWebSearch struct{…}`

        Web search.

        - `AllowedDomains []string`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

          - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

          - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

        - `Location AgentToolWebSearchLocation`

          Approximate location used to localize search results, if provided.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results.

          - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

          - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

          - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

      - `type AgentToolComputerUse struct{…}`

        Browser use in an OpenAI-hosted session.

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots.

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment EnvironmentUnion`

    The execution environment for the session.

    - `type EnvironmentNone struct{…}`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `Type None`

        The type of the object. Always `none`.

        - `const NoneNone None = "none"`

    - `type EnvironmentOpenAIHosted struct{…}`

      An environment hosted by OpenAI.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `Desktop EnvironmentOpenAIHostedDesktop`

        The effective desktop configuration.

        - `Enabled bool`

          Whether the environment provisions a desktop and browser proxy.

      - `Files []HostedEnvironmentFileUnion`

        Files available in the environment, excluding their contents.

        - `type HostedEnvironmentFileID struct{…}`

          A file copied from the OpenAI Files API.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `FileID string`

            The ID of the uploaded file.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type FileID`

            The type of the object. Always `file_id`.

            - `const FileIDFileID FileID = "file_id"`

        - `type HostedEnvironmentFileInline struct{…}`

          A file supplied inline when the session was created.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Network EnvironmentOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `Access string`

          The environment's network access mode.

          - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

            Allows unrestricted network access.

          - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

            Disables network access.

          - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

            Applies the configured domain restrictions.

        - `AllowedDomains []string`

          Domains the environment may access when network access is restricted.

      - `Packages EnvironmentOpenAIHostedPackages`

        Packages installed in the environment.

        - `Npm []string`

          npm packages installed globally in the environment.

        - `Python []string`

          Python packages installed in the environment.

        - `System []string`

          System packages installed in the environment.

      - `Plugins []HostedPlugin`

        Plugins installed in the environment, excluding their archive contents.

        - `Description string`

          The installed plugin description.

        - `Name string`

          The installed plugin name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

      - `Skills []HostedSkillUnion`

        Skills installed in the environment, excluding their archive contents.

        - `type HostedSkillReference struct{…}`

          A skill installed from the Skills API.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `SkillID string`

            The referenced skill ID.

          - `Type SkillReference`

            The type of the object. Always `skill_reference`.

            - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

          - `Version string`

            The concrete skill version installed for this session.

        - `type HostedSkillInline struct{…}`

          A skill installed from an inline ZIP archive.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Type OpenAIHosted`

        The type of the object. Always `openai_hosted`.

        - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `ContainerSize string`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

        - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

        - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

    - `type EnvironmentSelfHosted struct{…}`

      An environment hosted by the application.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `RemoteURL string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `Type SelfHosted`

        The type of the object. Always `self_hosted`.

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

      - `WorkspaceDirectory string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Error string`

    The error that caused the session to fail, if any.

  - `LastActiveAt int64`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the session.

  - `Object AgentSession`

    The object type. Always `agent.session`.

    - `const AgentSessionAgentSession AgentSession = "agent.session"`

  - `RequiredActions []AgentSessionRequiredActionUnion`

    Actions that must be completed before the session can continue.

    - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

      Respond to a computer-use request.

      - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

        The information needed to render the request.

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

          A browser origin awaiting the application's approval decision.

          - `Origin string`

            The origin the browser needs permission to access.

          - `Reason string`

            The browser's explanation for this request, or null when unavailable.

          - `Type BrowserOriginAccess`

            The type of the object. Always `browser_origin_access`.

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `RequestID string`

        The registered request ID to echo when responding.

      - `TurnID string`

        The turn that requested approval.

      - `Type ComputerUseApprovalRequest`

        The type of the object. Always `computer_use_approval_request`.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionRequiredActionFunctionCall struct{…}`

      Run a function tool and submit its result.

      - `Arguments any`

        The arguments supplied by the model.

      - `CallID string`

        The ID to include when submitting the function result.

      - `Name string`

        The function name.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type FunctionCall`

        The type of the object. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

      Reconnect a session environment.

      - `EnvironmentID string`

        The ID of the environment to reconnect.

      - `Type EnvironmentConnection`

        The type of the object. Always `environment_connection`.

        - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

  - `Status AgentSessionStatus`

    The current status of the session.

    - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

      The session is processing a turn.

    - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

      The session is waiting for one or more required actions.

    - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

      The session failed.

  - `Usage TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

  - `VaultIDs []string`

    The IDs of vaults made available to the session.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agentSession, err := client.Beta.Agents.Sessions.Get(context.TODO(), "session_id")
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentSession.ID)
}
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

`client.Beta.Agents.Sessions.Update(ctx, sessionID, body) (*AgentSession, error)`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `sessionID string`

- `body BetaAgentSessionUpdateParams`

  - `Agent param.Field[BetaAgentSessionUpdateParamsAgent]`

    Model settings for subsequent turns. Omitted fields stay unchanged.

    - `Model string`

      The model for subsequent turns. Omit to keep the current model.

    - `Reasoning BetaAgentSessionUpdateParamsAgentReasoning`

      Reasoning settings to update. Omit to keep the current effort.

      - `Effort string`

        Omit to keep the current effort. Null selects the model's default effort.

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortNone BetaAgentSessionUpdateParamsAgentReasoningEffort = "none"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortMinimal BetaAgentSessionUpdateParamsAgentReasoningEffort = "minimal"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortLow BetaAgentSessionUpdateParamsAgentReasoningEffort = "low"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortMedium BetaAgentSessionUpdateParamsAgentReasoningEffort = "medium"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortHigh BetaAgentSessionUpdateParamsAgentReasoningEffort = "high"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortXhigh BetaAgentSessionUpdateParamsAgentReasoningEffort = "xhigh"`

        - `const BetaAgentSessionUpdateParamsAgentReasoningEffortMax BetaAgentSessionUpdateParamsAgentReasoningEffort = "max"`

    - `ServiceTier string`

      Omit to keep the current tier. Null resets it to auto.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierAuto BetaAgentSessionUpdateParamsAgentServiceTier = "auto"`

        Selects the service tier automatically.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierDefault BetaAgentSessionUpdateParamsAgentServiceTier = "default"`

        Uses the default service tier.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierFlex BetaAgentSessionUpdateParamsAgentServiceTier = "flex"`

        Uses the flex service tier.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierPriority BetaAgentSessionUpdateParamsAgentServiceTier = "priority"`

        Uses the priority service tier.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierFast BetaAgentSessionUpdateParamsAgentServiceTier = "fast"`

        Uses the fast service tier.

      - `const BetaAgentSessionUpdateParamsAgentServiceTierUltrafast BetaAgentSessionUpdateParamsAgentServiceTier = "ultrafast"`

        Uses the ultrafast service tier.

  - `Metadata param.Field[map[string, string]]`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `type AgentSession struct{…}`

  A Managed Agents session.

  - `ID string`

    The ID of the session.

  - `Agent AgentSessionAgent`

    The agent running in the session.

    - `ID string`

      The ID of the agent.

    - `Instructions string`

      Custom instructions appended to the agent's default base instructions.

    - `Model string`

      The model used by the agent.

    - `MultiAgent MultiAgentConfig`

      Configuration for creating and coordinating subagents.

      - `Enabled bool`

        Whether subagent tools are enabled. Defaults to false.

      - `MaxConcurrentSubagents int64`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Name string`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `Reasoning AgentReasoning`

      The agent's reasoning configuration.

      - `Effort AgentReasoningEffort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

        - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

        - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

        - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

        - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

        - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

        - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

      - `Summary AgentReasoningSummary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

          Returns a concise reasoning summary when supported.

        - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

          Returns a detailed reasoning summary when supported.

        - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier string`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

      - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

      - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

      - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

      - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

      - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

    - `Text AgentText`

      Configuration for text generated by the agent.

      - `Format TextFormatUnion`

        The effective output format. Defaults to ordinary text.

        - `type TextFormatText struct{…}`

          Generates ordinary text without a structured-output constraint.

          - `Type Text`

            The type of the object. Always `text`.

            - `const TextText Text = "text"`

        - `type TextFormatJSONSchema struct{…}`

          Constrains generated text to a JSON Schema.

          - `Schema map[string, any]`

            The JSON Schema that generated text must match.

          - `Type JSONSchema`

            The type of the object. Always `json_schema`.

            - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

      - `Verbosity AgentTextVerbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

        - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

        - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

    - `Tools []AgentToolUnion`

      Tools available to the agent.

      - `type AgentToolFunction struct{…}`

        A function defined by the application.

        - `DeferLoading bool`

          Whether the function is deferred and discovered through tool search.

        - `Description string`

          A description of what the function does.

        - `Name string`

          The name of the function.

        - `Parameters map[string, any]`

          A JSON Schema object describing the function's arguments.

        - `Type Function`

          The type of the object. Always `function`.

          - `const FunctionFunction Function = "function"`

      - `type AgentToolProgrammaticToolCalling struct{…}`

        Enables calling tools from model-generated code.

        - `Enabled bool`

          Whether tools can be called from model-generated code.

        - `Type ProgrammaticToolCalling`

          The type of the object. Always `programmatic_tool_calling`.

          - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

      - `type AgentToolMcp struct{…}`

        Tools provided by a remote MCP server.

        - `AllowedTools []string`

          The MCP tools the agent may call.

        - `ConnectionOrigin string`

          Where outbound MCP HTTP connections originate.

          - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

          - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

        - `CredentialID string`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata map[string, any]`

          Metadata included with requests to this MCP server.

        - `Required bool`

          Whether this MCP server must initialize before the first turn.

        - `ServerLabel string`

          A label used to identify the MCP server in tool calls.

        - `Transport McpTransportUnion`

          The transport used to connect to the MCP server.

          - `type McpTransportHTTP struct{…}`

            Connects to an MCP server over HTTP.

            - `ServerURL string`

              The URL of the MCP server.

            - `Type HTTP`

              The type of the object. Always `http`.

              - `const HTTPHTTP HTTP = "http"`

          - `type McpTransportStdio struct{…}`

            Starts an MCP server as a local process.

            - `Args []string`

              Arguments passed to the MCP server command.

            - `Command string`

              The command used to start the MCP server.

            - `Cwd string`

              The working directory used to start the MCP server.

            - `EnvVars []string`

              Environment variable names inherited from the execution environment.

            - `Type Stdio`

              The type of the object. Always `stdio`.

              - `const StdioStdio Stdio = "stdio"`

        - `Type Mcp`

          The type of the object. Always `mcp`.

          - `const McpMcp Mcp = "mcp"`

      - `type AgentToolWebSearch struct{…}`

        Web search.

        - `AllowedDomains []string`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize string`

          The amount of search context made available to the model. Defaults to `medium`.

          - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

          - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

          - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

        - `Location AgentToolWebSearchLocation`

          Approximate location used to localize search results, if provided.

          - `City string`

            The city name.

          - `Country string`

            The two-letter ISO country code, such as `US`.

          - `Region string`

            The region or state name.

          - `Timezone string`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode string`

          The source used for web search results.

          - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

          - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

          - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

        - `Type WebSearch`

          The type of the object. Always `web_search`.

          - `const WebSearchWebSearch WebSearch = "web_search"`

      - `type AgentToolComputerUse struct{…}`

        Browser use in an OpenAI-hosted session.

        - `IncludeScreenshots bool`

          Whether computer tool outputs include screenshots.

        - `Type ComputerUse`

          The type of the object. Always `computer_use`.

          - `const ComputerUseComputerUse ComputerUse = "computer_use"`

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment EnvironmentUnion`

    The execution environment for the session.

    - `type EnvironmentNone struct{…}`

      The session talks to CCA without selecting or provisioning an execution environment.

      - `Type None`

        The type of the object. Always `none`.

        - `const NoneNone None = "none"`

    - `type EnvironmentOpenAIHosted struct{…}`

      An environment hosted by OpenAI.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `Desktop EnvironmentOpenAIHostedDesktop`

        The effective desktop configuration.

        - `Enabled bool`

          Whether the environment provisions a desktop and browser proxy.

      - `Files []HostedEnvironmentFileUnion`

        Files available in the environment, excluding their contents.

        - `type HostedEnvironmentFileID struct{…}`

          A file copied from the OpenAI Files API.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `FileID string`

            The ID of the uploaded file.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type FileID`

            The type of the object. Always `file_id`.

            - `const FileIDFileID FileID = "file_id"`

        - `type HostedEnvironmentFileInline struct{…}`

          A file supplied inline when the session was created.

          - `ID string`

            The session-scoped ID of the file in the execution environment.

          - `Path string`

            The file's absolute path inside the environment.

          - `SizeBytes int64`

            The decoded file size in bytes.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Network EnvironmentOpenAIHostedNetwork`

        The effective network access policy for the environment.

        - `Access string`

          The environment's network access mode.

          - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

            Allows unrestricted network access.

          - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

            Disables network access.

          - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

            Applies the configured domain restrictions.

        - `AllowedDomains []string`

          Domains the environment may access when network access is restricted.

      - `Packages EnvironmentOpenAIHostedPackages`

        Packages installed in the environment.

        - `Npm []string`

          npm packages installed globally in the environment.

        - `Python []string`

          Python packages installed in the environment.

        - `System []string`

          System packages installed in the environment.

      - `Plugins []HostedPlugin`

        Plugins installed in the environment, excluding their archive contents.

        - `Description string`

          The installed plugin description.

        - `Name string`

          The installed plugin name.

        - `Type Inline`

          The type of the object. Always `inline`.

          - `const InlineInline Inline = "inline"`

      - `Skills []HostedSkillUnion`

        Skills installed in the environment, excluding their archive contents.

        - `type HostedSkillReference struct{…}`

          A skill installed from the Skills API.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `SkillID string`

            The referenced skill ID.

          - `Type SkillReference`

            The type of the object. Always `skill_reference`.

            - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

          - `Version string`

            The concrete skill version installed for this session.

        - `type HostedSkillInline struct{…}`

          A skill installed from an inline ZIP archive.

          - `Description string`

            The installed skill description.

          - `Name string`

            The installed skill name.

          - `Type Inline`

            The type of the object. Always `inline`.

            - `const InlineInline Inline = "inline"`

      - `Type OpenAIHosted`

        The type of the object. Always `openai_hosted`.

        - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

      - `ContainerSize string`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

        - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

        - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

    - `type EnvironmentSelfHosted struct{…}`

      An environment hosted by the application.

      - `ID string`

        The public ID of the environment.

      - `CapabilityDirectories []string`

        Directories that contain capabilities exposed to the agent.

      - `RemoteURL string`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `Type SelfHosted`

        The type of the object. Always `self_hosted`.

        - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

      - `WorkspaceDirectory string`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Error string`

    The error that caused the session to fail, if any.

  - `LastActiveAt int64`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata map[string, string]`

    Custom string key-value pairs attached to the session.

  - `Object AgentSession`

    The object type. Always `agent.session`.

    - `const AgentSessionAgentSession AgentSession = "agent.session"`

  - `RequiredActions []AgentSessionRequiredActionUnion`

    Actions that must be completed before the session can continue.

    - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

      Respond to a computer-use request.

      - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

        The information needed to render the request.

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

          A browser origin awaiting the application's approval decision.

          - `Origin string`

            The origin the browser needs permission to access.

          - `Reason string`

            The browser's explanation for this request, or null when unavailable.

          - `Type BrowserOriginAccess`

            The type of the object. Always `browser_origin_access`.

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `RequestID string`

        The registered request ID to echo when responding.

      - `TurnID string`

        The turn that requested approval.

      - `Type ComputerUseApprovalRequest`

        The type of the object. Always `computer_use_approval_request`.

        - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

    - `type AgentSessionRequiredActionFunctionCall struct{…}`

      Run a function tool and submit its result.

      - `Arguments any`

        The arguments supplied by the model.

      - `CallID string`

        The ID to include when submitting the function result.

      - `Name string`

        The function name.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type FunctionCall`

        The type of the object. Always `function_call`.

        - `const FunctionCallFunctionCall FunctionCall = "function_call"`

    - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

      Reconnect a session environment.

      - `EnvironmentID string`

        The ID of the environment to reconnect.

      - `Type EnvironmentConnection`

        The type of the object. Always `environment_connection`.

        - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

  - `Status AgentSessionStatus`

    The current status of the session.

    - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

      The session is processing a turn.

    - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

      The session is waiting for one or more required actions.

    - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

      The session failed.

  - `Usage TokenUsage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `InputTokens int64`

      The number of input tokens used by the agent.

    - `InputTokensDetails TokenUsageInputTokensDetails`

      A breakdown of the agent's input token usage.

      - `CachedTokens int64`

        The number of input tokens retrieved from the prompt cache.

    - `OutputTokens int64`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails TokenUsageOutputTokensDetails`

      A breakdown of the agent's output token usage.

      - `ReasoningTokens int64`

        The number of output tokens used for reasoning.

    - `TotalTokens int64`

      The total number of input and output tokens used by the agent.

  - `VaultIDs []string`

    The IDs of vaults made available to the session.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  agentSession, err := client.Beta.Agents.Sessions.Update(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionUpdateParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", agentSession.ID)
}
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

`client.Beta.Agents.Sessions.Artifacts.Content(ctx, sessionID, artifactID) (*Response, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type BetaAgentSessionArtifactContentResponse interface{…}`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  response, err := client.Beta.Agents.Sessions.Artifacts.Content(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", response)
}
```

## Delete an agent session artifact

`client.Beta.Agents.Sessions.Artifacts.Delete(ctx, sessionID, artifactID) (*SessionArtifactDeleted, error)`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type SessionArtifactDeleted struct{…}`

  Confirmation that an immutable session artifact was deleted.

  - `ID string`

    The ID of the deleted session artifact.

  - `Deleted bool`

    Whether the session artifact was deleted. Always `true`.

  - `Object AgentSessionArtifactDeleted`

    The object type. Always `agent.session.artifact.deleted`.

    - `const AgentSessionArtifactDeletedAgentSessionArtifactDeleted AgentSessionArtifactDeleted = "agent.session.artifact.deleted"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  sessionArtifactDeleted, err := client.Beta.Agents.Sessions.Artifacts.Delete(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", sessionArtifactDeleted.ID)
}
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

`client.Beta.Agents.Sessions.Artifacts.List(ctx, sessionID, query) (*CursorPage[SessionArtifact], error)`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `query BetaAgentSessionArtifactListParams`

  - `After param.Field[string]`

    Return artifacts after this immutable artifact ID.

  - `EnvironmentID param.Field[string]`

    Restrict the listing to artifacts produced by this environment.

  - `Limit param.Field[int64]`

    The maximum number of artifacts to return, between 1 and 100.

  - `Order param.Field[BetaAgentSessionArtifactListParamsOrder]`

    Sort by creation time and ID. Defaults to descending.

    - `const BetaAgentSessionArtifactListParamsOrderAsc BetaAgentSessionArtifactListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionArtifactListParamsOrderDesc BetaAgentSessionArtifactListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  page, err := client.Beta.Agents.Sessions.Artifacts.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionArtifactListParams{

    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", page)
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

`client.Beta.Agents.Sessions.Artifacts.Get(ctx, sessionID, artifactID) (*SessionArtifact, error)`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `sessionID string`

- `artifactID string`

### Returns

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  sessionArtifact, err := client.Beta.Agents.Sessions.Artifacts.Get(
    context.TODO(),
    "session_id",
    "artifact_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", sessionArtifact.ID)
}
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

- `type SessionArtifact struct{…}`

  An immutable file published by a completed hosted session turn.

  - `ID string`

    The immutable artifact ID.

  - `CreatedAt int64`

    The Unix timestamp, in seconds, when the artifact was published.

  - `EnvironmentID string`

    The ID of the environment that produced the artifact.

  - `Object AgentSessionArtifact`

    The object type. Always `agent.session.artifact`.

    - `const AgentSessionArtifactAgentSessionArtifact AgentSessionArtifact = "agent.session.artifact"`

  - `Path string`

    The original absolute file path in the execution environment.

  - `SessionID string`

    The ID of the session that owns the artifact.

  - `SizeBytes int64`

    The immutable artifact size in bytes.

  - `TurnID string`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `type SessionArtifactDeleted struct{…}`

  Confirmation that an immutable session artifact was deleted.

  - `ID string`

    The ID of the deleted session artifact.

  - `Deleted bool`

    Whether the session artifact was deleted. Always `true`.

  - `Object AgentSessionArtifactDeleted`

    The object type. Always `agent.session.artifact.deleted`.

    - `const AgentSessionArtifactDeletedAgentSessionArtifactDeleted AgentSessionArtifactDeleted = "agent.session.artifact.deleted"`

# Events

## Create agent session input events

`client.Beta.Agents.Sessions.Events.New(ctx, sessionID, params) error`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `sessionID string`

- `params BetaAgentSessionEventNewParams`

  - `Events param.Field[[]AgentSessionInputParamUnionResp]`

    Body param: The input events to submit to the session.

    - `AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResultResp`

      - `RequestID string`

        The registered request ID from the required action.

      - `Response AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponseUnionResp`

        The response for this request type.

        - `type AgentBrowserAuthenticationSubmitParamResp struct{…}`

          - `Action Submit`

            - `const SubmitSubmit Submit = "submit"`

          - `Fields []AgentBrowserAuthenticationSubmitParamFieldResp`

            Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

            - `FieldID string`

              The field ID from the required action.

            - `Value string`

              The value to enter into the registered control.

          - `Type BrowserAuthentication`

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `SelectedOption string`

            The chosen method. Required when the required action contains options.

        - `type AgentBrowserAuthenticationCancelParamResp struct{…}`

          - `Action Cancel`

            - `const CancelCancel Cancel = "cancel"`

          - `Type BrowserAuthentication`

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `type AgentBrowserOriginAccessParamResp struct{…}`

          - `Decision AgentBrowserOriginAccessParamDecision`

            Whether to allow, deny, or cancel the requested origin access.

            - `const AgentBrowserOriginAccessParamDecisionApprove AgentBrowserOriginAccessParamDecision = "approve"`

              Allow the browser to access this origin.

            - `const AgentBrowserOriginAccessParamDecisionDeny AgentBrowserOriginAccessParamDecision = "deny"`

              Deny access to this origin.

            - `const AgentBrowserOriginAccessParamDecisionCancel AgentBrowserOriginAccessParamDecision = "cancel"`

              Dismiss this request without approving access.

          - `Type BrowserOriginAccess`

            - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

      - `Type AgentSessionInputComputerUseApprovalRequestResult`

        The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

        - `const AgentSessionInputComputerUseApprovalRequestResultAgentSessionInputComputerUseApprovalRequestResult AgentSessionInputComputerUseApprovalRequestResult = "agent.session.input.computer_use_approval_request_result"`

    - `AgentSessionInputParamAgentSessionInputMessageResp`

      - `Input []AgentSessionInputMessageParamResp`

        The user messages to add to the session.

        - `Content []InputContentParamUnionResp`

          The content of the message.

          - `InputContentParamInputTextResp`

            - `Text string`

              The text sent to the model.

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `InputContentParamInputImageResp`

            - `ImageURL string`

              The URL of the image sent to the model.

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

        - `Role User`

          The role of the message author. Always `user`.

          - `const UserUser User = "user"`

        - `Type AgentSessionInputMessageParamType`

          The type of the input item. Always `message`.

          - `const AgentSessionInputMessageParamTypeMessage AgentSessionInputMessageParamType = "message"`

      - `Type AgentSessionInputMessage`

        The type of the object. Always `agent.session.input.message`.

        - `const AgentSessionInputMessageAgentSessionInputMessage AgentSessionInputMessage = "agent.session.input.message"`

    - `AgentSessionInputParamAgentSessionInputCancelResp`

      - `Type AgentSessionInputCancel`

        The type of the object. Always `agent.session.input.cancel`.

        - `const AgentSessionInputCancelAgentSessionInputCancel AgentSessionInputCancel = "agent.session.input.cancel"`

    - `AgentSessionInputParamAgentSessionInputToolResultResp`

      - `CallID string`

        The ID of the function call.

      - `Success bool`

        Whether the function call succeeded.

      - `TurnID string`

        The ID of the turn that requested the function call.

      - `Type AgentSessionInputToolResult`

        The type of the object. Always `agent.session.input.tool_result`.

        - `const AgentSessionInputToolResultAgentSessionInputToolResult AgentSessionInputToolResult = "agent.session.input.tool_result"`

      - `Error string`

        The error message when the call failed.

      - `Output AgentFunctionCallOutputParamUnionResp`

        The function result when the call succeeded.

        - `string`

        - `[]InputContentParamUnionResp`

          - `InputContentParamInputTextResp`

          - `InputContentParamInputImageResp`

  - `IdempotencyKey param.Field[string]`

    Header param: An optional client-generated key that makes retries of submitted messages idempotent.

### Example

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  err := client.Beta.Agents.Sessions.Events.New(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionEventNewParams{
      Events: []openai.AgentSessionInputParamUnion{openai.AgentSessionInputParamUnion{
        OfAgentSessionInputComputerUseApprovalRequestResult: &openai.AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResult{
          RequestID: "request_id",
          Response: openai.AgentSessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponseUnion{
            OfBrowserAuthentication: &openai.AgentBrowserAuthenticationSubmitParam{
              Fields: []openai.AgentBrowserAuthenticationSubmitParamField{openai.AgentBrowserAuthenticationSubmitParamField{
                FieldID: "field_id",
                Value: "value",
              }},
            },
          },
        },
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
}
```

## Stream agent session events

`client.Beta.Agents.Sessions.Events.Stream(ctx, sessionID) (*AgentSessionEventUnion, error)`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `sessionID string`

### Returns

- `type AgentSessionEventUnion interface{…}`

  An event emitted by a Managed Agents session.

  - `type AgentSessionErrorEvent struct{…}`

    Emitted when a turn or session fails.

    - `Error SessionError`

      The error that occurred.

      - `Code string`

        The machine-readable error code, if any.

      - `Message string`

        A customer-safe explanation of the error.

      - `Param string`

        The request parameter associated with the error, if any.

      - `Type string`

        The error type.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Type Error`

      The type of the object. Always `error`.

      - `const ErrorError Error = "error"`

  - `type AgentSessionEnvironmentReadyEvent struct{…}`

    Emitted when a hosted session environment is ready to connect.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

      - `ID string`

        The public ID of the environment.

      - `Error AgentSessionEnvironmentStateError`

        The error reported while preparing the environment, if any.

        - `Code string`

          A machine-readable error code.

        - `Message string`

          A human-readable error message.

        - `Type string`

          The error type.

      - `Status AgentSessionEnvironmentStateStatus`

        The environment's connection status.

        - `const AgentSessionEnvironmentStateStatusPending AgentSessionEnvironmentStateStatus = "pending"`

          The environment is being prepared.

        - `const AgentSessionEnvironmentStateStatusReady AgentSessionEnvironmentStateStatus = "ready"`

          The environment is ready to connect.

        - `const AgentSessionEnvironmentStateStatusConnected AgentSessionEnvironmentStateStatus = "connected"`

          The environment is connected.

        - `const AgentSessionEnvironmentStateStatusDisconnected AgentSessionEnvironmentStateStatus = "disconnected"`

          The environment is disconnected.

        - `const AgentSessionEnvironmentStateStatusFailed AgentSessionEnvironmentStateStatus = "failed"`

          The environment failed to connect.

      - `Type string`

        The environment type.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentReady`

      The type of the object. Always `agent.session.environment.ready`.

      - `const AgentSessionEnvironmentReadyAgentSessionEnvironmentReady AgentSessionEnvironmentReady = "agent.session.environment.ready"`

  - `type AgentSessionEnvironmentResetEvent struct{…}`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `EnvironmentID string`

      The stable environment ID, retained across sandbox replacements.

    - `EventID string`

      The unique ID of the event.

    - `ResetCount int64`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The associated turn, when applicable.

    - `Type AgentSessionEnvironmentReset`

      The type of the object. Always `agent.session.environment.reset`.

      - `const AgentSessionEnvironmentResetAgentSessionEnvironmentReset AgentSessionEnvironmentReset = "agent.session.environment.reset"`

  - `type AgentOutputCommandExecutionOutputDeltaEvent struct{…}`

    Emitted when command execution produces an output delta.

    - `Delta string`

      The output text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the command execution item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentOutputCommandExecutionOutputDelta`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `const AgentOutputCommandExecutionOutputDeltaAgentOutputCommandExecutionOutputDelta AgentOutputCommandExecutionOutputDelta = "agent.output.command_execution_output.delta"`

  - `type AgentSessionCreatedEvent struct{…}`

    Emitted when a session is created.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that was created.

      - `ID string`

        The ID of the session.

      - `Agent AgentSessionAgent`

        The agent running in the session.

        - `ID string`

          The ID of the agent.

        - `Instructions string`

          Custom instructions appended to the agent's default base instructions.

        - `Model string`

          The model used by the agent.

        - `MultiAgent MultiAgentConfig`

          Configuration for creating and coordinating subagents.

          - `Enabled bool`

            Whether subagent tools are enabled. Defaults to false.

          - `MaxConcurrentSubagents int64`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `Name string`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `Reasoning AgentReasoning`

          The agent's reasoning configuration.

          - `Effort AgentReasoningEffort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `const AgentReasoningEffortNone AgentReasoningEffort = "none"`

            - `const AgentReasoningEffortMinimal AgentReasoningEffort = "minimal"`

            - `const AgentReasoningEffortLow AgentReasoningEffort = "low"`

            - `const AgentReasoningEffortMedium AgentReasoningEffort = "medium"`

            - `const AgentReasoningEffortHigh AgentReasoningEffort = "high"`

            - `const AgentReasoningEffortXhigh AgentReasoningEffort = "xhigh"`

            - `const AgentReasoningEffortMax AgentReasoningEffort = "max"`

          - `Summary AgentReasoningSummary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `const AgentReasoningSummaryConcise AgentReasoningSummary = "concise"`

              Returns a concise reasoning summary when supported.

            - `const AgentReasoningSummaryDetailed AgentReasoningSummary = "detailed"`

              Returns a detailed reasoning summary when supported.

            - `const AgentReasoningSummaryAuto AgentReasoningSummary = "auto"`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier string`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `const AgentSessionAgentServiceTierAuto AgentSessionAgentServiceTier = "auto"`

          - `const AgentSessionAgentServiceTierDefault AgentSessionAgentServiceTier = "default"`

          - `const AgentSessionAgentServiceTierFlex AgentSessionAgentServiceTier = "flex"`

          - `const AgentSessionAgentServiceTierPriority AgentSessionAgentServiceTier = "priority"`

          - `const AgentSessionAgentServiceTierFast AgentSessionAgentServiceTier = "fast"`

          - `const AgentSessionAgentServiceTierUltrafast AgentSessionAgentServiceTier = "ultrafast"`

        - `Text AgentText`

          Configuration for text generated by the agent.

          - `Format TextFormatUnion`

            The effective output format. Defaults to ordinary text.

            - `type TextFormatText struct{…}`

              Generates ordinary text without a structured-output constraint.

              - `Type Text`

                The type of the object. Always `text`.

                - `const TextText Text = "text"`

            - `type TextFormatJSONSchema struct{…}`

              Constrains generated text to a JSON Schema.

              - `Schema map[string, any]`

                The JSON Schema that generated text must match.

              - `Type JSONSchema`

                The type of the object. Always `json_schema`.

                - `const JSONSchemaJSONSchema JSONSchema = "json_schema"`

          - `Verbosity AgentTextVerbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `const AgentTextVerbosityLow AgentTextVerbosity = "low"`

            - `const AgentTextVerbosityMedium AgentTextVerbosity = "medium"`

            - `const AgentTextVerbosityHigh AgentTextVerbosity = "high"`

        - `Tools []AgentToolUnion`

          Tools available to the agent.

          - `type AgentToolFunction struct{…}`

            A function defined by the application.

            - `DeferLoading bool`

              Whether the function is deferred and discovered through tool search.

            - `Description string`

              A description of what the function does.

            - `Name string`

              The name of the function.

            - `Parameters map[string, any]`

              A JSON Schema object describing the function's arguments.

            - `Type Function`

              The type of the object. Always `function`.

              - `const FunctionFunction Function = "function"`

          - `type AgentToolProgrammaticToolCalling struct{…}`

            Enables calling tools from model-generated code.

            - `Enabled bool`

              Whether tools can be called from model-generated code.

            - `Type ProgrammaticToolCalling`

              The type of the object. Always `programmatic_tool_calling`.

              - `const ProgrammaticToolCallingProgrammaticToolCalling ProgrammaticToolCalling = "programmatic_tool_calling"`

          - `type AgentToolMcp struct{…}`

            Tools provided by a remote MCP server.

            - `AllowedTools []string`

              The MCP tools the agent may call.

            - `ConnectionOrigin string`

              Where outbound MCP HTTP connections originate.

              - `const AgentToolMcpConnectionOriginService AgentToolMcpConnectionOrigin = "service"`

              - `const AgentToolMcpConnectionOriginEnvironment AgentToolMcpConnectionOrigin = "environment"`

            - `CredentialID string`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `RequestMetadata map[string, any]`

              Metadata included with requests to this MCP server.

            - `Required bool`

              Whether this MCP server must initialize before the first turn.

            - `ServerLabel string`

              A label used to identify the MCP server in tool calls.

            - `Transport McpTransportUnion`

              The transport used to connect to the MCP server.

              - `type McpTransportHTTP struct{…}`

                Connects to an MCP server over HTTP.

                - `ServerURL string`

                  The URL of the MCP server.

                - `Type HTTP`

                  The type of the object. Always `http`.

                  - `const HTTPHTTP HTTP = "http"`

              - `type McpTransportStdio struct{…}`

                Starts an MCP server as a local process.

                - `Args []string`

                  Arguments passed to the MCP server command.

                - `Command string`

                  The command used to start the MCP server.

                - `Cwd string`

                  The working directory used to start the MCP server.

                - `EnvVars []string`

                  Environment variable names inherited from the execution environment.

                - `Type Stdio`

                  The type of the object. Always `stdio`.

                  - `const StdioStdio Stdio = "stdio"`

            - `Type Mcp`

              The type of the object. Always `mcp`.

              - `const McpMcp Mcp = "mcp"`

          - `type AgentToolWebSearch struct{…}`

            Web search.

            - `AllowedDomains []string`

              Allowed search domains, or `null` when the search is unrestricted.

            - `ContextSize string`

              The amount of search context made available to the model. Defaults to `medium`.

              - `const AgentToolWebSearchContextSizeLow AgentToolWebSearchContextSize = "low"`

              - `const AgentToolWebSearchContextSizeMedium AgentToolWebSearchContextSize = "medium"`

              - `const AgentToolWebSearchContextSizeHigh AgentToolWebSearchContextSize = "high"`

            - `Location AgentToolWebSearchLocation`

              Approximate location used to localize search results, if provided.

              - `City string`

                The city name.

              - `Country string`

                The two-letter ISO country code, such as `US`.

              - `Region string`

                The region or state name.

              - `Timezone string`

                The IANA timezone, such as `America/Los_Angeles`.

            - `Mode string`

              The source used for web search results.

              - `const AgentToolWebSearchModeDisabled AgentToolWebSearchMode = "disabled"`

              - `const AgentToolWebSearchModeCached AgentToolWebSearchMode = "cached"`

              - `const AgentToolWebSearchModeLive AgentToolWebSearchMode = "live"`

            - `Type WebSearch`

              The type of the object. Always `web_search`.

              - `const WebSearchWebSearch WebSearch = "web_search"`

          - `type AgentToolComputerUse struct{…}`

            Browser use in an OpenAI-hosted session.

            - `IncludeScreenshots bool`

              Whether computer tool outputs include screenshots.

            - `Type ComputerUse`

              The type of the object. Always `computer_use`.

              - `const ComputerUseComputerUse ComputerUse = "computer_use"`

      - `CreatedAt int64`

        The Unix timestamp, in seconds, when the session was created.

      - `Environment EnvironmentUnion`

        The execution environment for the session.

        - `type EnvironmentNone struct{…}`

          The session talks to CCA without selecting or provisioning an execution environment.

          - `Type None`

            The type of the object. Always `none`.

            - `const NoneNone None = "none"`

        - `type EnvironmentOpenAIHosted struct{…}`

          An environment hosted by OpenAI.

          - `ID string`

            The public ID of the environment.

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent.

          - `Desktop EnvironmentOpenAIHostedDesktop`

            The effective desktop configuration.

            - `Enabled bool`

              Whether the environment provisions a desktop and browser proxy.

          - `Files []HostedEnvironmentFileUnion`

            Files available in the environment, excluding their contents.

            - `type HostedEnvironmentFileID struct{…}`

              A file copied from the OpenAI Files API.

              - `ID string`

                The session-scoped ID of the file in the execution environment.

              - `FileID string`

                The ID of the uploaded file.

              - `Path string`

                The file's absolute path inside the environment.

              - `SizeBytes int64`

                The decoded file size in bytes.

              - `Type FileID`

                The type of the object. Always `file_id`.

                - `const FileIDFileID FileID = "file_id"`

            - `type HostedEnvironmentFileInline struct{…}`

              A file supplied inline when the session was created.

              - `ID string`

                The session-scoped ID of the file in the execution environment.

              - `Path string`

                The file's absolute path inside the environment.

              - `SizeBytes int64`

                The decoded file size in bytes.

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Network EnvironmentOpenAIHostedNetwork`

            The effective network access policy for the environment.

            - `Access string`

              The environment's network access mode.

              - `const EnvironmentOpenAIHostedNetworkAccessEnabled EnvironmentOpenAIHostedNetworkAccess = "enabled"`

                Allows unrestricted network access.

              - `const EnvironmentOpenAIHostedNetworkAccessDisabled EnvironmentOpenAIHostedNetworkAccess = "disabled"`

                Disables network access.

              - `const EnvironmentOpenAIHostedNetworkAccessRestricted EnvironmentOpenAIHostedNetworkAccess = "restricted"`

                Applies the configured domain restrictions.

            - `AllowedDomains []string`

              Domains the environment may access when network access is restricted.

          - `Packages EnvironmentOpenAIHostedPackages`

            Packages installed in the environment.

            - `Npm []string`

              npm packages installed globally in the environment.

            - `Python []string`

              Python packages installed in the environment.

            - `System []string`

              System packages installed in the environment.

          - `Plugins []HostedPlugin`

            Plugins installed in the environment, excluding their archive contents.

            - `Description string`

              The installed plugin description.

            - `Name string`

              The installed plugin name.

            - `Type Inline`

              The type of the object. Always `inline`.

              - `const InlineInline Inline = "inline"`

          - `Skills []HostedSkillUnion`

            Skills installed in the environment, excluding their archive contents.

            - `type HostedSkillReference struct{…}`

              A skill installed from the Skills API.

              - `Description string`

                The installed skill description.

              - `Name string`

                The installed skill name.

              - `SkillID string`

                The referenced skill ID.

              - `Type SkillReference`

                The type of the object. Always `skill_reference`.

                - `const SkillReferenceSkillReference SkillReference = "skill_reference"`

              - `Version string`

                The concrete skill version installed for this session.

            - `type HostedSkillInline struct{…}`

              A skill installed from an inline ZIP archive.

              - `Description string`

                The installed skill description.

              - `Name string`

                The installed skill name.

              - `Type Inline`

                The type of the object. Always `inline`.

                - `const InlineInline Inline = "inline"`

          - `Type OpenAIHosted`

            The type of the object. Always `openai_hosted`.

            - `const OpenAIHostedOpenAIHosted OpenAIHosted = "openai_hosted"`

          - `ContainerSize string`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `const EnvironmentOpenAIHostedContainerSizeSmall EnvironmentOpenAIHostedContainerSize = "small"`

            - `const EnvironmentOpenAIHostedContainerSizeMedium EnvironmentOpenAIHostedContainerSize = "medium"`

            - `const EnvironmentOpenAIHostedContainerSizeLarge EnvironmentOpenAIHostedContainerSize = "large"`

        - `type EnvironmentSelfHosted struct{…}`

          An environment hosted by the application.

          - `ID string`

            The public ID of the environment.

          - `CapabilityDirectories []string`

            Directories that contain capabilities exposed to the agent.

          - `RemoteURL string`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `Type SelfHosted`

            The type of the object. Always `self_hosted`.

            - `const SelfHostedSelfHosted SelfHosted = "self_hosted"`

          - `WorkspaceDirectory string`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `Error string`

        The error that caused the session to fail, if any.

      - `LastActiveAt int64`

        The Unix timestamp, in seconds, when the session was last active.

      - `Metadata map[string, string]`

        Custom string key-value pairs attached to the session.

      - `Object AgentSession`

        The object type. Always `agent.session`.

        - `const AgentSessionAgentSession AgentSession = "agent.session"`

      - `RequiredActions []AgentSessionRequiredActionUnion`

        Actions that must be completed before the session can continue.

        - `type AgentSessionRequiredActionComputerUseApprovalRequest struct{…}`

          Respond to a computer-use request.

          - `Request AgentSessionRequiredActionComputerUseApprovalRequestRequestUnion`

            The information needed to render the request.

            - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthentication struct{…}`

              A registered form awaiting the application's response.

              - `CredentialOrigin string`

                The registered form or frame origin where values will be entered.

              - `Fields []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationField`

                Controls to render. All submitted values are sensitive.

                - `ID string`

                  The field ID to submit as field_id in a fields entry.

                - `Label string`

                  The label to display beside the control.

                - `Required bool`

                  Whether this control requires a nonempty value.

                - `Type string`

                  The rendering type, such as email, password, or text.

              - `Options []AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserAuthenticationOption`

                Sign-in methods. Empty for a plain form.

                - `ID string`

                  The option ID to submit as selected_option.

                - `FieldIDs []string`

                  IDs from the registered fields that this method accepts.

                - `Label string`

                  The method label to display.

              - `Reason string`

                Why the agent needs the user to sign in.

              - `Type BrowserAuthentication`

                The type of the object. Always `browser_authentication`.

                - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

            - `type AgentSessionRequiredActionComputerUseApprovalRequestRequestBrowserOriginAccess struct{…}`

              A browser origin awaiting the application's approval decision.

              - `Origin string`

                The origin the browser needs permission to access.

              - `Reason string`

                The browser's explanation for this request, or null when unavailable.

              - `Type BrowserOriginAccess`

                The type of the object. Always `browser_origin_access`.

                - `const BrowserOriginAccessBrowserOriginAccess BrowserOriginAccess = "browser_origin_access"`

          - `RequestID string`

            The registered request ID to echo when responding.

          - `TurnID string`

            The turn that requested approval.

          - `Type ComputerUseApprovalRequest`

            The type of the object. Always `computer_use_approval_request`.

            - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

        - `type AgentSessionRequiredActionFunctionCall struct{…}`

          Run a function tool and submit its result.

          - `Arguments any`

            The arguments supplied by the model.

          - `CallID string`

            The ID to include when submitting the function result.

          - `Name string`

            The function name.

          - `TurnID string`

            The ID of the turn that requested the function call.

          - `Type FunctionCall`

            The type of the object. Always `function_call`.

            - `const FunctionCallFunctionCall FunctionCall = "function_call"`

        - `type AgentSessionRequiredActionEnvironmentConnection struct{…}`

          Reconnect a session environment.

          - `EnvironmentID string`

            The ID of the environment to reconnect.

          - `Type EnvironmentConnection`

            The type of the object. Always `environment_connection`.

            - `const EnvironmentConnectionEnvironmentConnection EnvironmentConnection = "environment_connection"`

      - `Status AgentSessionStatus`

        The current status of the session.

        - `const AgentSessionStatusIdle AgentSessionStatus = "idle"`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `const AgentSessionStatusInProgress AgentSessionStatus = "in_progress"`

          The session is processing a turn.

        - `const AgentSessionStatusRequiresAction AgentSessionStatus = "requires_action"`

          The session is waiting for one or more required actions.

        - `const AgentSessionStatusFailed AgentSessionStatus = "failed"`

          The session failed.

      - `Usage TokenUsage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `InputTokens int64`

          The number of input tokens used by the agent.

        - `InputTokensDetails TokenUsageInputTokensDetails`

          A breakdown of the agent's input token usage.

          - `CachedTokens int64`

            The number of input tokens retrieved from the prompt cache.

        - `OutputTokens int64`

          The number of output tokens generated by the agent.

        - `OutputTokensDetails TokenUsageOutputTokensDetails`

          A breakdown of the agent's output token usage.

          - `ReasoningTokens int64`

            The number of output tokens used for reasoning.

        - `TotalTokens int64`

          The total number of input and output tokens used by the agent.

      - `VaultIDs []string`

        The IDs of vaults made available to the session.

    - `Type AgentSessionCreated`

      The type of the object. Always `agent.session.created`.

      - `const AgentSessionCreatedAgentSessionCreated AgentSessionCreated = "agent.session.created"`

  - `type AgentSessionTurnCreatedEvent struct{…}`

    Emitted when a turn is created.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The turn at the time it was created.

      - `ID string`

        The ID of the turn.

      - `AgentID string`

        The ID of the agent that ran the turn.

      - `CompletedAt int64`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `CreatedAt int64`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `Error SessionTurnError`

        A customer-safe error. Non-null only for a failed turn.

        - `Code SessionTurnErrorCode`

          A stable, machine-readable failure category.

          - `const SessionTurnErrorCodeContextLengthExceeded SessionTurnErrorCode = "context_length_exceeded"`

            The request exceeds the model's context window.

          - `const SessionTurnErrorCodeSessionBudgetExceeded SessionTurnErrorCode = "session_budget_exceeded"`

            The session has reached its usage budget.

          - `const SessionTurnErrorCodeUsageLimitExceeded SessionTurnErrorCode = "usage_limit_exceeded"`

            The organization has reached a usage, plan, or billing limit.

          - `const SessionTurnErrorCodeCreditBalanceExhausted SessionTurnErrorCode = "credit_balance_exhausted"`

            The organization has no API credits remaining.

          - `const SessionTurnErrorCodeRateLimitExceeded SessionTurnErrorCode = "rate_limit_exceeded"`

            The request exceeds the available rate limit.

          - `const SessionTurnErrorCodeFlexUnavailable SessionTurnErrorCode = "flex_unavailable"`

            Flex processing is temporarily unavailable.

          - `const SessionTurnErrorCodeServerOverloaded SessionTurnErrorCode = "server_overloaded"`

            The model service is temporarily overloaded.

          - `const SessionTurnErrorCodeCyberPolicy SessionTurnErrorCode = "cyber_policy"`

            The request was rejected by a safety policy.

          - `const SessionTurnErrorCodeMisalignmentPolicyViolation SessionTurnErrorCode = "misalignment_policy_violation"`

            The request was blocked by the safety systems.

          - `const SessionTurnErrorCodeConnectionFailed SessionTurnErrorCode = "connection_failed"`

            The request could not connect to the model service.

          - `const SessionTurnErrorCodeServerError SessionTurnErrorCode = "server_error"`

            The model service encountered an unexpected error.

          - `const SessionTurnErrorCodeAuthenticationError SessionTurnErrorCode = "authentication_error"`

            The API credentials are invalid or lack the required access.

          - `const SessionTurnErrorCodeInvalidRequest SessionTurnErrorCode = "invalid_request"`

            The request contains invalid input or configuration.

          - `const SessionTurnErrorCodeResourceNotFound SessionTurnErrorCode = "resource_not_found"`

            The requested model or resource is unavailable.

          - `const SessionTurnErrorCodeSandboxError SessionTurnErrorCode = "sandbox_error"`

            The request could not complete in its execution environment.

          - `const SessionTurnErrorCodeExecutorVersionIncompatible SessionTurnErrorCode = "executor_version_incompatible"`

            The executor must be upgraded before it can run this turn.

          - `const SessionTurnErrorCodeActiveTurnNotSteerable SessionTurnErrorCode = "active_turn_not_steerable"`

            The session cannot accept additional input while a request is running.

          - `const SessionTurnErrorCodeRequestTimeout SessionTurnErrorCode = "request_timeout"`

            The request timed out before the model service responded.

          - `const SessionTurnErrorCodeInternalError SessionTurnErrorCode = "internal_error"`

            An unexpected internal error prevented the session request from completing.

        - `Message string`

          A customer-safe explanation of the failure.

      - `Object TurnObject`

        The object type. Always `agent.session.turn`.

        - `const TurnObjectAgentSessionTurn TurnObject = "agent.session.turn"`

      - `SessionID string`

        The ID of the session that owns the turn.

      - `StartedAt int64`

        The Unix timestamp, in seconds, when the turn started.

      - `Status TurnStatus`

        The current status of the turn.

        - `const TurnStatusQueued TurnStatus = "queued"`

          The turn is waiting to start.

        - `const TurnStatusInProgress TurnStatus = "in_progress"`

          The turn is in progress.

        - `const TurnStatusWaiting TurnStatus = "waiting"`

          The turn is waiting for external input.

        - `const TurnStatusCompleted TurnStatus = "completed"`

          The turn completed successfully.

        - `const TurnStatusFailed TurnStatus = "failed"`

          The turn failed.

        - `const TurnStatusCancelled TurnStatus = "cancelled"`

          The turn was cancelled.

      - `SubagentID string`

        The ID of the subagent that ran the turn, if applicable.

      - `Usage TokenUsage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCreated`

      The type of the object. Always `agent.session.turn.created`.

      - `const AgentSessionTurnCreatedAgentSessionTurnCreated AgentSessionTurnCreated = "agent.session.turn.created"`

  - `type AgentSessionTurnInProgressEvent struct{…}`

    Emitted when a turn starts running.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The turn at the time it started running.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnInProgress`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `const AgentSessionTurnInProgressAgentSessionTurnInProgress AgentSessionTurnInProgress = "agent.session.turn.in_progress"`

  - `type AgentSessionTurnCompletedEvent struct{…}`

    Emitted when a turn completes.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The completed turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCompleted`

      The type of the object. Always `agent.session.turn.completed`.

      - `const AgentSessionTurnCompletedAgentSessionTurnCompleted AgentSessionTurnCompleted = "agent.session.turn.completed"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnFailedEvent struct{…}`

    Emitted when a turn fails.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The failed turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnFailed`

      The type of the object. Always `agent.session.turn.failed`.

      - `const AgentSessionTurnFailedAgentSessionTurnFailed AgentSessionTurnFailed = "agent.session.turn.failed"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnCancelledEvent struct{…}`

    Emitted when a turn is cancelled.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Turn Turn`

      The cancelled turn.

    - `TurnID string`

      The ID of the turn associated with the event.

    - `Type AgentSessionTurnCancelled`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `const AgentSessionTurnCancelledAgentSessionTurnCancelled AgentSessionTurnCancelled = "agent.session.turn.cancelled"`

    - `Usage TokenUsage`

      Token usage by the root agent during the turn, when available.

  - `type AgentSessionTurnItemAddedEvent struct{…}`

    Emitted when an item is added to a turn.

    - `EventID string`

      The unique ID of the event.

    - `Item AgentSessionItemUnion`

      The item that was added.

      - `type AgentSessionMessage struct{…}`

        A user or assistant message recorded in a session.

        - `ID string`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `Content []AgentSessionMessageContentUnion`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `type AgentSessionMessageContentInputText struct{…}`

            Text supplied by the user.

            - `Text string`

              The text supplied by the user.

            - `Type InputText`

              The type of the object. Always `input_text`.

              - `const InputTextInputText InputText = "input_text"`

          - `type AgentSessionMessageContentInputImage struct{…}`

            An image supplied by the user.

            - `ImageURL string`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `Type InputImage`

              The type of the object. Always `input_image`.

              - `const InputImageInputImage InputImage = "input_image"`

          - `type AgentSessionMessageContentOutputText struct{…}`

            Text produced by the assistant.

            - `Text string`

              The text produced by the assistant.

            - `Type OutputText`

              The type of the object. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

        - `Phase AgentSessionMessagePhase`

          The phase of an assistant message. Null for user messages.

          - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

            Commentary produced while the agent works.

          - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

            The agent's final answer.

        - `Role AgentSessionMessageRole`

          The role of the message author.

          - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

          - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

        - `Status AgentOutputItemStatus`

          The status of the message. User messages are always `completed`.

          - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

            The item is in progress.

          - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

            The item is complete.

          - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

            The item stopped before completing.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Message`

          The item type. Always `message`.

          - `const MessageMessage Message = "message"`

      - `type AgentReasoningItem struct{…}`

        A reasoning item produced by the agent.

        - `ID string`

          The ID of the reasoning item.

        - `Status AgentOutputItemStatus`

          The status of the reasoning item.

        - `Summary []SummaryText`

          The reasoning summaries produced by the agent.

          - `Text string`

            The reasoning summary text.

          - `Type SummaryText`

            The content type. Always `summary_text`.

            - `const SummaryTextSummaryText SummaryText = "summary_text"`

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Reasoning`

          The item type. Always `reasoning`.

          - `const ReasoningReasoning Reasoning = "reasoning"`

      - `type AgentFunctionCallItem struct{…}`

        A function call produced by the agent.

        - `ID string`

          The ID of the function call item.

        - `Arguments any`

          The arguments to pass to the function.

        - `CallID string`

          The ID used to submit the function result.

        - `Name string`

          The name of the function to call.

        - `Status AgentFunctionCallStatus`

          The status of the function call.

          - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

            The call is in progress.

          - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

            The call completed successfully.

          - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

            The call failed.

          - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

            The call stopped before completing.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type FunctionCall`

          The item type. Always `function_call`.

          - `const FunctionCallFunctionCall FunctionCall = "function_call"`

      - `type AgentSessionItemFunctionCallOutput struct{…}`

        The result supplied for a function call.

        - `ID string`

          The ID of the function call output item.

        - `CallID string`

          The ID of the function call that produced this output.

        - `Error string`

          The error message, if the call failed.

        - `Output AgentFunctionCallOutputUnion`

          The function result, if the call succeeded.

          - `string`

          - `type AgentFunctionCallOutputArray []InputContentUnion`

            - `type InputContentInputText struct{…}`

              Text input recorded in a session item.

              - `Text string`

                The text supplied to the agent.

              - `Type InputText`

                The type of the object. Always `input_text`.

                - `const InputTextInputText InputText = "input_text"`

            - `type InputContentInputImage struct{…}`

              Image input recorded in a session item.

              - `ImageURL string`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `Type InputImage`

                The type of the object. Always `input_image`.

                - `const InputImageInputImage InputImage = "input_image"`

        - `Status AgentFunctionCallStatus`

          The status of the function call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type FunctionCallOutput`

          The item type. Always `function_call_output`.

          - `const FunctionCallOutputFunctionCallOutput FunctionCallOutput = "function_call_output"`

      - `type AgentSessionItemAgentMessage struct{…}`

        A message exchanged between agent threads.

        - `ID string`

          The ID of the message.

        - `Content []AgentContentUnion`

          The content exchanged between the agents.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

            - `Text string`

              The text produced by the agent.

            - `Type OutputText`

              The content type. Always `output_text`.

              - `const OutputTextOutputText OutputText = "output_text"`

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

            - `EncryptedContent string`

              The encrypted content payload.

            - `Type EncryptedContent`

              The content type. Always `encrypted_content`.

              - `const EncryptedContentEncryptedContent EncryptedContent = "encrypted_content"`

        - `RecipientAgentID string`

          The ID or name of the receiving agent.

        - `SenderAgentID string`

          The ID or name of the sending agent.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type AgentMessage`

          The item type. Always `agent_message`.

          - `const AgentMessageAgentMessage AgentMessage = "agent_message"`

      - `type AgentMcpCallItem struct{…}`

        A call to a tool on an MCP server.

        - `ID string`

          The ID of the MCP call item.

        - `Arguments any`

          The arguments passed to the MCP tool.

        - `Error any`

          The error returned by the MCP tool, if any.

        - `Name string`

          The name of the MCP tool.

        - `Output any`

          The output returned by the MCP tool, if any.

        - `ServerLabel string`

          The label of the MCP server.

        - `Status AgentFunctionCallStatus`

          The status of the MCP tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type McpCall`

          The item type. Always `mcp_call`.

          - `const McpCallMcpCall McpCall = "mcp_call"`

      - `type AgentSessionItemComputerUseCall struct{…}`

        One execution of the platform-provided computer-use capability.

        - `ID string`

          The ID of the activity item.

        - `Output AgentSessionItemComputerUseCallOutput`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `ImageURL string`

            The complete JPEG image as a base64 data URL.

          - `Type ComputerScreenshot`

            The content type. Always `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

        - `Status AgentFunctionCallStatus`

          The execution status of the activity.

        - `Title string`

          A model-generated description of the activity, when available.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseCall`

          The item type. Always `computer_use_call`.

          - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

      - `type AgentSessionItemComputerUseApprovalRequest struct{…}`

        A credential-free history record of the emitted login request.

        - `ID string`

          The stable history item ID.

        - `Request AgentSessionItemComputerUseApprovalRequestRequest`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentSessionItemComputerUseApprovalRequestRequestField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentSessionItemComputerUseApprovalRequestRequestOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `RequestID string`

        - `TurnID string`

        - `Type ComputerUseApprovalRequest`

          The item type. Always computer_use_approval_request.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentSessionItemComputerUseApprovalRequestResult struct{…}`

        A credential-free record of an admitted response, not proof of completion.

        - `ID string`

          The stable history item ID.

        - `RequestID string`

          The registered request answered by this item.

        - `Response AgentSessionItemComputerUseApprovalRequestResultResponseUnion`

          The admitted response, without submitted credential values.

          - `type AgentSessionItemComputerUseApprovalRequestResultResponseSubmit struct{…}`

            - `Action Submit`

              - `const SubmitSubmit Submit = "submit"`

            - `SelectedOption string`

              The chosen sign-in method, or null when no options were offered.

            - `Type BrowserAuthentication`

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

          - `type AgentSessionItemComputerUseApprovalRequestResultResponseCancel struct{…}`

            - `Action Cancel`

              - `const CancelCancel Cancel = "cancel"`

            - `Type BrowserAuthentication`

              - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseApprovalRequestResult`

          - `const ComputerUseApprovalRequestResultComputerUseApprovalRequestResult ComputerUseApprovalRequestResult = "computer_use_approval_request_result"`

      - `type AgentWebSearchCallItem struct{…}`

        A web search call produced by the agent.

        - `ID string`

          The ID of the web search call.

        - `Action WebSearchActionUnion`

          The action performed by the web search tool.

          - `type WebSearchActionSearch struct{…}`

            A search query or group of search queries.

            - `Queries []string`

              The search queries, when multiple queries were used.

            - `Query string`

              The search query, when a single query was used.

            - `Type Search`

              The type of the object. Always `search`.

              - `const SearchSearch Search = "search"`

          - `type WebSearchActionOpenPage struct{…}`

            Opens a web page.

            - `Type OpenPage`

              The type of the object. Always `open_page`.

              - `const OpenPageOpenPage OpenPage = "open_page"`

            - `URL string`

              The URL of the page that was opened.

          - `type WebSearchActionFindInPage struct{…}`

            Finds text within a web page.

            - `Pattern string`

              The text pattern that was searched for.

            - `Type FindInPage`

              The type of the object. Always `find_in_page`.

              - `const FindInPageFindInPage FindInPage = "find_in_page"`

            - `URL string`

              The URL of the page that was searched.

          - `type WebSearchActionOther struct{…}`

            Another web search action.

            - `Type Other`

              The type of the object. Always `other`.

              - `const OtherOther Other = "other"`

        - `Status AgentOutputItemStatus`

          The status of the web search call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type WebSearchCall`

          The item type. Always `web_search_call`.

          - `const WebSearchCallWebSearchCall WebSearchCall = "web_search_call"`

      - `type AgentCommandExecutionItem struct{…}`

        A command execution produced by the agent.

        - `ID string`

          The ID of the command execution item.

        - `Command string`

          The command that was executed.

        - `Cwd string`

          The working directory used to execute the command.

        - `DurationMs int64`

          The command duration in milliseconds.

        - `ExitCode int64`

          The process exit code, if the command completed.

        - `Output string`

          The command output, if available.

        - `Status AgentFunctionCallStatus`

          The status of the command execution.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CommandExecution`

          The item type. Always `command_execution`.

          - `const CommandExecutionCommandExecution CommandExecution = "command_execution"`

      - `type AgentCreateSubagentCallItem struct{…}`

        A request to spawn a subagent.

        - `ID string`

          The ID of the tool call item.

        - `AgentID string`

          The ID of the agent that requested the subagent.

        - `Content []AgentContentUnion`

          The task given to the spawned agent.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

        - `Model string`

          The model requested for the spawned agent.

        - `ReasoningEffort string`

          The reasoning effort requested for the spawned agent.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CreateSubagentCall`

          The item type. Always `create_subagent_call`.

          - `const CreateSubagentCallCreateSubagentCall CreateSubagentCall = "create_subagent_call"`

            The current public item type.

      - `type AgentSendSubagentInputCallItem struct{…}`

        A request to send input to another agent.

        - `ID string`

          The ID of the tool call item.

        - `Content []AgentContentUnion`

          The input sent to the receiving agent.

          - `type OutputText struct{…}`

            A text content part produced by the agent.

          - `type AgentContentEncryptedContent struct{…}`

            Encrypted content exchanged between agents.

        - `RecipientAgentID string`

          The ID of the agent receiving the input.

        - `SenderAgentID string`

          The ID of the agent sending the input.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type SendSubagentInputCall`

          The item type. Always `send_subagent_input_call`.

          - `const SendSubagentInputCallSendSubagentInputCall SendSubagentInputCall = "send_subagent_input_call"`

            The current public item type.

      - `type AgentResumeSubagentCallItem struct{…}`

        A request to resume a subagent.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to resume.

        - `SenderAgentID string`

          The ID of the agent requesting the resume.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ResumeSubagentCall`

          The item type. Always `resume_subagent_call`.

          - `const ResumeSubagentCallResumeSubagentCall ResumeSubagentCall = "resume_subagent_call"`

            The current public item type.

      - `type AgentWaitForSubagentsCallItem struct{…}`

        A request to wait for one or more subagents.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentIDs []string`

          The IDs of the agents to wait for.

        - `SenderAgentID string`

          The ID of the agent waiting for results.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type WaitForSubagentsCall`

          The item type. Always `wait_for_subagents_call`.

          - `const WaitForSubagentsCallWaitForSubagentsCall WaitForSubagentsCall = "wait_for_subagents_call"`

            The current public item type.

      - `type AgentInterruptSubagentCallItem struct{…}`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to interrupt.

        - `SenderAgentID string`

          The ID of the agent requesting the interrupt.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type InterruptSubagentCall`

          The item type. Always `interrupt_subagent_call`.

          - `const InterruptSubagentCallInterruptSubagentCall InterruptSubagentCall = "interrupt_subagent_call"`

            The current public item type.

      - `type AgentCloseSubagentCallItem struct{…}`

        A request to close a subagent.

        - `ID string`

          The ID of the tool call item.

        - `RecipientAgentID string`

          The ID of the agent to close.

        - `SenderAgentID string`

          The ID of the agent requesting the close.

        - `Status AgentFunctionCallStatus`

          The status of the tool call.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type CloseSubagentCall`

          The item type. Always `close_subagent_call`.

          - `const CloseSubagentCallCloseSubagentCall CloseSubagentCall = "close_subagent_call"`

            The current public item type.

    - `OutputIndex int64`

      The index of the item in the turn output, when the item is agent output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnItemAdded`

      The type of the object. Always `agent.session.turn.item.added`.

      - `const AgentSessionTurnItemAddedAgentSessionTurnItemAdded AgentSessionTurnItemAdded = "agent.session.turn.item.added"`

  - `type AgentSessionIdleEvent struct{…}`

    Emitted when a session becomes idle.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that became idle.

    - `Type AgentSessionIdle`

      The type of the object. Always `agent.session.idle`.

      - `const AgentSessionIdleAgentSessionIdle AgentSessionIdle = "agent.session.idle"`

  - `type AgentSessionInProgressEvent struct{…}`

    Emitted when a session starts processing a turn.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session that started processing.

    - `Type AgentSessionInProgress`

      The type of the object. Always `agent.session.in_progress`.

      - `const AgentSessionInProgressAgentSessionInProgress AgentSessionInProgress = "agent.session.in_progress"`

  - `type AgentSessionRequiresActionEvent struct{…}`

    Emitted when a session is waiting for one or more required actions.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The session and its current required actions.

    - `Type AgentSessionRequiresAction`

      The type of the object. Always `agent.session.requires_action`.

      - `const AgentSessionRequiresActionAgentSessionRequiresAction AgentSessionRequiresAction = "agent.session.requires_action"`

  - `type AgentSessionFailedEvent struct{…}`

    Emitted when a session fails.

    - `EventID string`

      The unique ID of the event.

    - `Session AgentSession`

      The failed session.

    - `Type AgentSessionFailed`

      The type of the object. Always `agent.session.failed`.

      - `const AgentSessionFailedAgentSessionFailed AgentSessionFailed = "agent.session.failed"`

  - `type AgentSessionEnvironmentPendingEvent struct{…}`

    Emitted while a session environment is being prepared.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentPending`

      The type of the object. Always `agent.session.environment.pending`.

      - `const AgentSessionEnvironmentPendingAgentSessionEnvironmentPending AgentSessionEnvironmentPending = "agent.session.environment.pending"`

  - `type AgentSessionEnvironmentConnectedEvent struct{…}`

    Emitted when a session environment connects.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentConnected`

      The type of the object. Always `agent.session.environment.connected`.

      - `const AgentSessionEnvironmentConnectedAgentSessionEnvironmentConnected AgentSessionEnvironmentConnected = "agent.session.environment.connected"`

  - `type AgentSessionEnvironmentDisconnectedEvent struct{…}`

    Emitted when a session environment disconnects.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentDisconnected`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `const AgentSessionEnvironmentDisconnectedAgentSessionEnvironmentDisconnected AgentSessionEnvironmentDisconnected = "agent.session.environment.disconnected"`

  - `type AgentSessionEnvironmentFailedEvent struct{…}`

    Emitted when a session environment fails.

    - `Environment AgentSessionEnvironmentState`

      The current environment state.

    - `EventID string`

      The unique ID of the event.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionEnvironmentFailed`

      The type of the object. Always `agent.session.environment.failed`.

      - `const AgentSessionEnvironmentFailedAgentSessionEnvironmentFailed AgentSessionEnvironmentFailed = "agent.session.environment.failed"`

  - `type AgentSessionSubagentCreatedEvent struct{…}`

    Emitted when a subagent is created.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that was created.

      - `ID string`

        The ID of the subagent.

      - `ClosedAt int64`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `Instructions []AgentContentUnion`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `type OutputText struct{…}`

          A text content part produced by the agent.

        - `type AgentContentEncryptedContent struct{…}`

          Encrypted content exchanged between agents.

      - `Name string`

        The runner-assigned nickname, or null when unavailable.

      - `Object SubagentObject`

        The object type. Always `agent.session.subagent`.

        - `const SubagentObjectAgentSessionSubagent SubagentObject = "agent.session.subagent"`

      - `OpenedAt int64`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `ParentAgentID string`

        The ID of the agent that created this subagent.

      - `SessionID string`

        The ID of the session that owns the subagent.

      - `Status SubagentStatus`

        The current status of the subagent.

        - `const SubagentStatusActive SubagentStatus = "active"`

          The subagent remains available, including while idle between turns.

        - `const SubagentStatusClosed SubagentStatus = "closed"`

          The subagent is closed.

    - `Type AgentSessionSubagentCreated`

      The type of the object. Always `agent.session.subagent.created`.

      - `const AgentSessionSubagentCreatedAgentSessionSubagentCreated AgentSessionSubagentCreated = "agent.session.subagent.created"`

  - `type AgentSessionSubagentActiveEvent struct{…}`

    Emitted when a closed subagent successfully resumes.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that resumed.

    - `Type AgentSessionSubagentActive`

      The type of the object. Always `agent.session.subagent.active`.

      - `const AgentSessionSubagentActiveAgentSessionSubagentActive AgentSessionSubagentActive = "agent.session.subagent.active"`

  - `type AgentSessionSubagentClosedEvent struct{…}`

    Emitted when a subagent is closed.

    - `EventID string`

      The unique ID of the event.

    - `Subagent Subagent`

      The subagent that was closed.

    - `Type AgentSessionSubagentClosed`

      The type of the object. Always `agent.session.subagent.closed`.

      - `const AgentSessionSubagentClosedAgentSessionSubagentClosed AgentSessionSubagentClosed = "agent.session.subagent.closed"`

  - `type AgentSessionTurnItemDoneEvent struct{…}`

    Emitted when an output item is complete.

    - `EventID string`

      The unique ID of the event.

    - `Item AgentOutputItemUnion`

      The completed output item.

      - `type AgentSessionAssistantMessage struct{…}`

        An assistant message produced by the agent.

        - `ID string`

          The ID of the message.

        - `Content []OutputText`

          The content of the message.

          - `Text string`

            The text produced by the agent.

          - `Type OutputText`

            The content type. Always `output_text`.

        - `Phase AgentSessionAssistantMessagePhase`

          The phase of the assistant message.

          - `const AgentSessionAssistantMessagePhaseCommentary AgentSessionAssistantMessagePhase = "commentary"`

            Commentary produced while the agent works.

          - `const AgentSessionAssistantMessagePhaseFinalAnswer AgentSessionAssistantMessagePhase = "final_answer"`

            The agent's final answer.

        - `Role Assistant`

          The role of the message author. Always `assistant`.

          - `const AssistantAssistant Assistant = "assistant"`

        - `Status AgentOutputItemStatus`

          The status of the message.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type Message`

          The item type. Always `message`.

          - `const MessageMessage Message = "message"`

      - `type AgentReasoningItem struct{…}`

        A reasoning item produced by the agent.

      - `type AgentFunctionCallItem struct{…}`

        A function call produced by the agent.

      - `type AgentMcpCallItem struct{…}`

        A call to a tool on an MCP server.

      - `type AgentOutputItemComputerUseCall struct{…}`

        One execution of the platform-provided computer-use capability.

        - `ID string`

          The ID of the activity item.

        - `Output AgentOutputItemComputerUseCallOutput`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `ImageURL string`

            The complete JPEG image as a base64 data URL.

          - `Type ComputerScreenshot`

            The content type. Always `computer_screenshot`.

            - `const ComputerScreenshotComputerScreenshot ComputerScreenshot = "computer_screenshot"`

        - `Status AgentFunctionCallStatus`

          The execution status of the activity.

        - `Title string`

          A model-generated description of the activity, when available.

        - `TurnID string`

          The ID of the turn that contains this item.

        - `Type ComputerUseCall`

          The item type. Always `computer_use_call`.

          - `const ComputerUseCallComputerUseCall ComputerUseCall = "computer_use_call"`

      - `type AgentOutputItemComputerUseApprovalRequest struct{…}`

        A credential-free history record of the emitted login request.

        - `ID string`

          The stable history item ID.

        - `Request AgentOutputItemComputerUseApprovalRequestRequest`

          A registered form awaiting the application's response.

          - `CredentialOrigin string`

            The registered form or frame origin where values will be entered.

          - `Fields []AgentOutputItemComputerUseApprovalRequestRequestField`

            Controls to render. All submitted values are sensitive.

            - `ID string`

              The field ID to submit as field_id in a fields entry.

            - `Label string`

              The label to display beside the control.

            - `Required bool`

              Whether this control requires a nonempty value.

            - `Type string`

              The rendering type, such as email, password, or text.

          - `Options []AgentOutputItemComputerUseApprovalRequestRequestOption`

            Sign-in methods. Empty for a plain form.

            - `ID string`

              The option ID to submit as selected_option.

            - `FieldIDs []string`

              IDs from the registered fields that this method accepts.

            - `Label string`

              The method label to display.

          - `Reason string`

            Why the agent needs the user to sign in.

          - `Type BrowserAuthentication`

            The type of the object. Always `browser_authentication`.

            - `const BrowserAuthenticationBrowserAuthentication BrowserAuthentication = "browser_authentication"`

        - `RequestID string`

        - `TurnID string`

        - `Type ComputerUseApprovalRequest`

          The item type. Always computer_use_approval_request.

          - `const ComputerUseApprovalRequestComputerUseApprovalRequest ComputerUseApprovalRequest = "computer_use_approval_request"`

      - `type AgentWebSearchCallItem struct{…}`

        A web search call produced by the agent.

      - `type AgentCommandExecutionItem struct{…}`

        A command execution produced by the agent.

      - `type AgentCreateSubagentCallItem struct{…}`

        A request to spawn a subagent.

      - `type AgentSendSubagentInputCallItem struct{…}`

        A request to send input to another agent.

      - `type AgentResumeSubagentCallItem struct{…}`

        A request to resume a subagent.

      - `type AgentWaitForSubagentsCallItem struct{…}`

        A request to wait for one or more subagents.

      - `type AgentInterruptSubagentCallItem struct{…}`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `type AgentCloseSubagentCallItem struct{…}`

        A request to close a subagent.

    - `OutputIndex int64`

      The index of the output item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnItemDone`

      The type of the object. Always `agent.session.turn.item.done`.

      - `const AgentSessionTurnItemDoneAgentSessionTurnItemDone AgentSessionTurnItemDone = "agent.session.turn.item.done"`

  - `type AgentSessionTurnContentPartAddedEvent struct{…}`

    Emitted when an output text content part is added.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part OutputText`

      The initial content part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnContentPartAdded`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `const AgentSessionTurnContentPartAddedAgentSessionTurnContentPartAdded AgentSessionTurnContentPartAdded = "agent.session.turn.content_part.added"`

  - `type AgentSessionTurnContentPartDoneEvent struct{…}`

    Emitted when an output content part is complete.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part OutputText`

      The completed content part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnContentPartDone`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `const AgentSessionTurnContentPartDoneAgentSessionTurnContentPartDone AgentSessionTurnContentPartDone = "agent.session.turn.content_part.done"`

  - `type AgentSessionTurnOutputTextDeltaEvent struct{…}`

    Emitted when text is appended to an output text content part.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `Delta string`

      The text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnOutputTextDelta`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `const AgentSessionTurnOutputTextDeltaAgentSessionTurnOutputTextDelta AgentSessionTurnOutputTextDelta = "agent.session.turn.output_text.delta"`

  - `type AgentSessionTurnOutputTextDoneEvent struct{…}`

    Emitted when an output text content part is complete.

    - `ContentIndex int64`

      The index of the content part in the message.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the message item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Text string`

      The complete output text.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnOutputTextDone`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `const AgentSessionTurnOutputTextDoneAgentSessionTurnOutputTextDone AgentSessionTurnOutputTextDone = "agent.session.turn.output_text.done"`

  - `type AgentSessionTurnReasoningSummaryPartAddedEvent struct{…}`

    Emitted when a reasoning summary content part is added.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part SummaryText`

      The initial summary part.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryPartAdded`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `const AgentSessionTurnReasoningSummaryPartAddedAgentSessionTurnReasoningSummaryPartAdded AgentSessionTurnReasoningSummaryPartAdded = "agent.session.turn.reasoning_summary_part.added"`

  - `type AgentSessionTurnReasoningSummaryPartDoneEvent struct{…}`

    Emitted when a reasoning summary part is complete.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `Part SummaryText`

      The completed summary part.

    - `SessionID string`

      The ID of the session associated with the event.

    - `Status Incomplete`

      Present as `incomplete` when summary generation was interrupted.

      - `const IncompleteIncomplete Incomplete = "incomplete"`

    - `SummaryIndex int64`

      The index of the summary part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryPartDone`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `const AgentSessionTurnReasoningSummaryPartDoneAgentSessionTurnReasoningSummaryPartDone AgentSessionTurnReasoningSummaryPartDone = "agent.session.turn.reasoning_summary_part.done"`

  - `type AgentSessionTurnReasoningSummaryTextDeltaEvent struct{…}`

    Emitted when text is appended to a reasoning summary.

    - `Delta string`

      The summary text that was appended.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryTextDelta`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `const AgentSessionTurnReasoningSummaryTextDeltaAgentSessionTurnReasoningSummaryTextDelta AgentSessionTurnReasoningSummaryTextDelta = "agent.session.turn.reasoning_summary_text.delta"`

  - `type AgentSessionTurnReasoningSummaryTextDoneEvent struct{…}`

    Emitted when a reasoning summary content part is complete.

    - `EventID string`

      The unique ID of the event.

    - `ItemID string`

      The ID of the reasoning item.

    - `OutputIndex int64`

      The index of the item in the turn output.

    - `SessionID string`

      The ID of the session associated with the event.

    - `SummaryIndex int64`

      The index of the summary content part.

    - `Text string`

      The complete reasoning summary text.

    - `TurnID string`

      The ID of the turn associated with the event, when applicable.

    - `Type AgentSessionTurnReasoningSummaryTextDone`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `const AgentSessionTurnReasoningSummaryTextDoneAgentSessionTurnReasoningSummaryTextDone AgentSessionTurnReasoningSummaryTextDone = "agent.session.turn.reasoning_summary_text.done"`

### Example

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
)

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  )
  stream := client.Beta.Agents.Sessions.Events.StreamStreaming(context.TODO(), "session_id")
  for stream.Next() {
  fmt.Printf("%+v\n", stream.Current())
  }
  err := stream.Err()
  if err != nil {
    panic(err.Error())
  }
}
```

# Items

## List agent session items

`client.Beta.Agents.Sessions.Items.List(ctx, sessionID, query) (*CursorPage[AgentSessionItemUnion], error)`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `sessionID string`

- `query BetaAgentSessionItemListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionItemListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionItemListParamsOrderAsc BetaAgentSessionItemListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionItemListParamsOrderDesc BetaAgentSessionItemListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type AgentSessionItemUnion interface{…}`

  An item associated with a session turn.

  - `type AgentSessionMessage struct{…}`

    A user or assistant message recorded in a session.

    - `ID string`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `Content []AgentSessionMessageContentUnion`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `type AgentSessionMessageContentInputText struct{…}`

        Text supplied by the user.

        - `Text string`

          The text supplied by the user.

        - `Type InputText`

          The type of the object. Always `input_text`.

          - `const InputTextInputText InputText = "input_text"`

      - `type AgentSessionMessageContentInputImage struct{…}`

        An image supplied by the user.

        - `ImageURL string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `Type InputImage`

          The type of the object. Always `input_image`.

          - `const InputImageInputImage InputImage = "input_image"`

      - `type AgentSessionMessageContentOutputText struct{…}`

        Text produced by the assistant.

        - `Text string`

          The text produced by the assistant.

        - `Type OutputText`

          The type of the object. Always `output_text`.

          - `const OutputTextOutputText OutputText = "output_text"`

    - `Phase AgentSessionMessagePhase`

      The phase of an assistant message. Null for user messages.

      - `const AgentSessionMessagePhaseCommentary AgentSessionMessagePhase = "commentary"`

        Commentary produced while the agent works.

      - `const AgentSessionMessagePhaseFinalAnswer AgentSessionMessagePhase = "final_answer"`

        The agent's final answer.

    - `Role AgentSessionMessageRole`

      The role of the message author.

      - `const AgentSessionMessageRoleUser AgentSessionMessageRole = "user"`

      - `const AgentSessionMessageRoleAssistant AgentSessionMessageRole = "assistant"`

    - `Status AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `const AgentOutputItemStatusInProgress AgentOutputItemStatus = "in_progress"`

        The item is in progress.

      - `const AgentOutputItemStatusCompleted AgentOutputItemStatus = "completed"`

        The item is complete.

      - `const AgentOutputItemStatusIncomplete AgentOutputItemStatus = "incomplete"`

        The item stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Message`

      The item type. Always `message`.

      - `const MessageMessage Message = "message"`

  - `type AgentReasoningItem struct{…}`

    A reasoning item produced by the agent.

    - `ID string`

      The ID of the reasoning item.

    - `Status AgentOutputItemStatus`

      The status of the reasoning item.

    - `Summary []SummaryText`

      The reasoning summaries produced by the agent.

      - `Text string`

        The reasoning summary text.

      - `Type SummaryText`

        The content type. Always `summary_text`.

        - `const SummaryTextSummaryText SummaryText = "summary_text"`

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type Reasoning`

      The item type. Always `reasoning`.

      - `const ReasoningReasoning Reasoning = "reasoning"`

  - `type AgentFunctionCallItem struct{…}`

    A function call produced by the agent.

    - `ID string`

      The ID of the function call item.

    - `Arguments any`

      The arguments to pass to the function.

    - `CallID string`

      The ID used to submit the function result.

    - `Name string`

      The name of the function to call.

    - `Status AgentFunctionCallStatus`

      The status of the function call.

      - `const AgentFunctionCallStatusInProgress AgentFunctionCallStatus = "in_progress"`

        The call is in progress.

      - `const AgentFunctionCallStatusCompleted AgentFunctionCallStatus = "completed"`

        The call completed successfully.

      - `const AgentFunctionCallStatusFailed AgentFunctionCallStatus = "failed"`

        The call failed.

      - `const AgentFunctionCallStatusIncomplete AgentFunctionCallStatus = "incomplete"`

        The call stopped before completing.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCall`

      The item type. Always `function_call`.

      - `const FunctionCallFunctionCall FunctionCall = "function_call"`

  - `type AgentSessionItemFunctionCallOutput struct{…}`

    The result supplied for a function call.

    - `ID string`

      The ID of the function call output item.

    - `CallID string`

      The ID of the function call that produced this output.

    - `Error string`

      The error message, if the call failed.

    - `Output AgentFunctionCallOutputUnion`

      The function result, if the call succeeded.

      - `string`

      - `type AgentFunctionCallOutputArray []InputContentUnion`

        - `type InputContentInputText struct{…}`

          Text input recorded in a session item.

          - `Text string`

            The text supplied to the agent.

          - `Type InputText`

            The type of the object. Always `input_text`.

            - `const InputTextInputText InputText = "input_text"`

        - `type InputContentInputImage struct{…}`

          Image input recorded in a session item.

          - `ImageURL string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `Type InputImage`

            The type of the object. Always `input_image`.

            - `const InputImageInputImage InputImage = "input_image"`

    - `Status AgentFunctionCallStatus`

      The status of the function call.

    - `TurnID string`

      The ID of the turn that contains this item.

    - `Type FunctionCallOutput`

      The item type. Always `function_call_output`.
