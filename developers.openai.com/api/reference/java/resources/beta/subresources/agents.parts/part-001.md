<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/ -->
<!-- part of: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/ -->

<!-- chunk-start -->

# Agents

## Create an agent

`Agent beta().agents().create(AgentCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents`

Creates a reusable agent without storing credentials. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `AgentCreateParams params`

  - `String model`

    The model to use for the agent. The requested model name is preserved.

  - `Optional<String> instructions`

    Additional instructions appended to the agent's default base instructions. Omit or set to null to add no custom instructions.

  - `Optional<Metadata> metadata`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

  - `Optional<MultiAgentConfigParam> multiAgent`

    Configuration for creating and coordinating subagents. Subagent tools are disabled by default.

  - `Optional<String> name`

    A human-readable name for the agent. Omission or null leaves the agent unnamed.

  - `Optional<AgentReasoningParam> reasoning`

    Configuration for model reasoning. Omission uses the model's default effort.

  - `Optional<ServiceTier> serviceTier`

    The service tier used for model requests. Defaults to `auto`.

    - `AUTO("auto")`

      Selects the service tier automatically.

    - `DEFAULT("default")`

      Uses the default service tier.

    - `FLEX("flex")`

      Uses the flex service tier.

    - `PRIORITY("priority")`

      Uses the priority service tier.

    - `FAST("fast")`

      Uses the fast service tier.

    - `ULTRAFAST("ultrafast")`

      Uses the ultrafast service tier.

  - `Optional<AgentTextParam> text`

    Configuration for generated text. Defaults to the `text` format and medium verbosity.

  - `Optional<List<PersistedAgentToolParam>> tools`

    Tools available to the agent. Defaults to an empty list.

    - `Function`

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

      - `Optional<Boolean> deferLoading`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Optional<Boolean> enabled`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `Mcp`

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransportParam transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

          - `Optional<Headers> headers`

            Non-secret HTTP headers sent to the MCP server.

        - `Stdio`

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

          - `Optional<List<String>> args`

            Arguments passed to the MCP server command.

          - `Optional<List<String>> envVars`

            Environment variable names to inherit from the selected execution environment.

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `Optional<ConnectionOrigin> connectionOrigin`

        Selects where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

          Uses the Managed Agents service network.

        - `ENVIRONMENT("environment")`

          Uses the session's execution environment.

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `Optional<RequestMetadata> requestMetadata`

        Metadata included with requests to this MCP server.

      - `Optional<Boolean> required`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `WebSearch`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

      - `Optional<List<String>> allowedDomains`

        Domains the search may include.

      - `Optional<ContextSize> contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Optional<Mode> mode`

        The source used for web search results. Defaults to `live`.

        - `DISABLED("disabled")`

          Disables web search.

        - `CACHED("cached")`

          Uses cached search results.

        - `LIVE("live")`

          Searches the live web.

    - `ComputerUse`

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

      - `Optional<Boolean> includeScreenshots`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `class Agent:`

  A reusable agent scoped to the caller's project.

  - `String id`

    The ID of the reusable agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the agent was created.

  - `Optional<String> instructions`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata metadata`

    Custom string key-value pairs attached to the agent.

  - `String model`

    The requested model name used for inference.

  - `MultiAgentConfig multiAgent`

    The resolved configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Optional<String> name`

    A human-readable name for the agent, or null if it is unnamed.

  - `JsonValue; object_ "agent"constant`

    The object type. Always `agent`.

    - `AGENT("agent")`

  - `AgentReasoning reasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Optional<Effort> effort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

      - `MAX("max")`

    - `Optional<Summary> summary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `CONCISE("concise")`

        Returns a concise reasoning summary when supported.

      - `DETAILED("detailed")`

        Returns a detailed reasoning summary when supported.

      - `AUTO("auto")`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier serviceTier`

    The resolved service-tier policy used for model requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The resolved configuration for text generated by the agent.

    - `TextFormat format`

      The effective output format. Defaults to ordinary text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          The type of the object. Always `text`.

          - `TEXT("text")`

      - `JsonSchema`

        - `Schema schema`

          The JSON Schema that generated text must match.

        - `JsonValue; type "json_schema"constant`

          The type of the object. Always `json_schema`.

          - `JSON_SCHEMA("json_schema")`

    - `Verbosity verbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `List<PersistedAgentTool> tools`

    Tools available to the agent.

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransport transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `Headers headers`

            Non-secret HTTP headers sent to the MCP server.

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode mode`

        The source used for web search results.

        - `DISABLED("disabled")`

        - `CACHED("cached")`

        - `LIVE("live")`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

    - `ComputerUse`

      - `boolean includeScreenshots`

        Whether computer tool outputs include screenshots.

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Agent;
import com.openai.models.beta.agents.AgentCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentCreateParams params = AgentCreateParams.builder()
            .model("model")
            .build();
        Agent agent = client.beta().agents().create(params);
    }
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

`AgentDeleted beta().agents().delete(AgentDeleteParamsparams = AgentDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/{agent_id}`

Deletes a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `AgentDeleteParams params`

  - `Optional<String> agentId`

### Returns

- `class AgentDeleted:`

  A deleted reusable agent.

  - `String id`

    The ID of the deleted agent.

  - `boolean deleted`

    Whether the agent was deleted. Always `true`.

  - `JsonValue; object_ "agent.deleted"constant`

    The object type. Always `agent.deleted`.

    - `AGENT_DELETED("agent.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentDeleteParams;
import com.openai.models.beta.agents.AgentDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentDeleted agentDeleted = client.beta().agents().delete("agent_id");
    }
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

`AgentListPage beta().agents().list(AgentListParamsparams = AgentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents`

Lists reusable agents in the current project. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `AgentListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Agent:`

  A reusable agent scoped to the caller's project.

  - `String id`

    The ID of the reusable agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the agent was created.

  - `Optional<String> instructions`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata metadata`

    Custom string key-value pairs attached to the agent.

  - `String model`

    The requested model name used for inference.

  - `MultiAgentConfig multiAgent`

    The resolved configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Optional<String> name`

    A human-readable name for the agent, or null if it is unnamed.

  - `JsonValue; object_ "agent"constant`

    The object type. Always `agent`.

    - `AGENT("agent")`

  - `AgentReasoning reasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Optional<Effort> effort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

      - `MAX("max")`

    - `Optional<Summary> summary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `CONCISE("concise")`

        Returns a concise reasoning summary when supported.

      - `DETAILED("detailed")`

        Returns a detailed reasoning summary when supported.

      - `AUTO("auto")`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier serviceTier`

    The resolved service-tier policy used for model requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The resolved configuration for text generated by the agent.

    - `TextFormat format`

      The effective output format. Defaults to ordinary text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          The type of the object. Always `text`.

          - `TEXT("text")`

      - `JsonSchema`

        - `Schema schema`

          The JSON Schema that generated text must match.

        - `JsonValue; type "json_schema"constant`

          The type of the object. Always `json_schema`.

          - `JSON_SCHEMA("json_schema")`

    - `Verbosity verbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `List<PersistedAgentTool> tools`

    Tools available to the agent.

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransport transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `Headers headers`

            Non-secret HTTP headers sent to the MCP server.

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode mode`

        The source used for web search results.

        - `DISABLED("disabled")`

        - `CACHED("cached")`

        - `LIVE("live")`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

    - `ComputerUse`

      - `boolean includeScreenshots`

        Whether computer tool outputs include screenshots.

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentListPage;
import com.openai.models.beta.agents.AgentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentListPage page = client.beta().agents().list();
    }
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

`Agent beta().agents().retrieve(AgentRetrieveParamsparams = AgentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/{agent_id}`

Retrieves a reusable agent by ID. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `AgentRetrieveParams params`

  - `Optional<String> agentId`

### Returns

- `class Agent:`

  A reusable agent scoped to the caller's project.

  - `String id`

    The ID of the reusable agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the agent was created.

  - `Optional<String> instructions`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata metadata`

    Custom string key-value pairs attached to the agent.

  - `String model`

    The requested model name used for inference.

  - `MultiAgentConfig multiAgent`

    The resolved configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Optional<String> name`

    A human-readable name for the agent, or null if it is unnamed.

  - `JsonValue; object_ "agent"constant`

    The object type. Always `agent`.

    - `AGENT("agent")`

  - `AgentReasoning reasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Optional<Effort> effort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

      - `MAX("max")`

    - `Optional<Summary> summary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `CONCISE("concise")`

        Returns a concise reasoning summary when supported.

      - `DETAILED("detailed")`

        Returns a detailed reasoning summary when supported.

      - `AUTO("auto")`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier serviceTier`

    The resolved service-tier policy used for model requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The resolved configuration for text generated by the agent.

    - `TextFormat format`

      The effective output format. Defaults to ordinary text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          The type of the object. Always `text`.

          - `TEXT("text")`

      - `JsonSchema`

        - `Schema schema`

          The JSON Schema that generated text must match.

        - `JsonValue; type "json_schema"constant`

          The type of the object. Always `json_schema`.

          - `JSON_SCHEMA("json_schema")`

    - `Verbosity verbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `List<PersistedAgentTool> tools`

    Tools available to the agent.

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransport transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `Headers headers`

            Non-secret HTTP headers sent to the MCP server.

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode mode`

        The source used for web search results.

        - `DISABLED("disabled")`

        - `CACHED("cached")`

        - `LIVE("live")`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

    - `ComputerUse`

      - `boolean includeScreenshots`

        Whether computer tool outputs include screenshots.

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Agent;
import com.openai.models.beta.agents.AgentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Agent agent = client.beta().agents().retrieve("agent_id");
    }
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

`Agent beta().agents().update(AgentUpdateParamsparams = AgentUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/{agent_id}`

Updates a reusable agent. See [agent configuration](/api/docs/guides/agents-api/configuration).

### Parameters

- `AgentUpdateParams params`

  - `Optional<String> agentId`

  - `Optional<String> instructions`

    Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

  - `Optional<Metadata> metadata`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

  - `Optional<String> model`

    The model to use for the agent. The requested model name is preserved.

  - `Optional<MultiAgentConfigParam> multiAgent`

    Configuration for creating and coordinating subagents.

  - `Optional<String> name`

    A replacement name. Omit to leave unchanged, or pass null to clear it.

  - `Optional<AgentReasoningParam> reasoning`

    Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

  - `Optional<ServiceTier> serviceTier`

    The service tier used for model requests.

    - `AUTO("auto")`

      Selects the service tier automatically.

    - `DEFAULT("default")`

      Uses the default service tier.

    - `FLEX("flex")`

      Uses the flex service tier.

    - `PRIORITY("priority")`

      Uses the priority service tier.

    - `FAST("fast")`

      Uses the fast service tier.

    - `ULTRAFAST("ultrafast")`

      Uses the ultrafast service tier.

  - `Optional<AgentTextParam> text`

    Configuration for text generated by the agent.

  - `Optional<List<PersistedAgentToolParam>> tools`

    Tools available to the agent.

    - `Function`

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

      - `Optional<Boolean> deferLoading`

        Whether this function is deferred and discovered through tool search. Defaults to `false`.

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Optional<Boolean> enabled`

        Whether tools can be called from model-generated code. Defaults to `true`.

    - `Mcp`

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransportParam transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

          - `Optional<Headers> headers`

            Non-secret HTTP headers sent to the MCP server.

        - `Stdio`

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

          - `Optional<List<String>> args`

            Arguments passed to the MCP server command.

          - `Optional<List<String>> envVars`

            Environment variable names to inherit from the selected execution environment.

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call. All server tools are allowed when omitted.

      - `Optional<ConnectionOrigin> connectionOrigin`

        Selects where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

          Uses the Managed Agents service network.

        - `ENVIRONMENT("environment")`

          Uses the session's execution environment.

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

      - `Optional<RequestMetadata> requestMetadata`

        Metadata included with requests to this MCP server.

      - `Optional<Boolean> required`

        Whether this MCP server must initialize before the first turn. Defaults to `false`.

    - `WebSearch`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

      - `Optional<List<String>> allowedDomains`

        Domains the search may include.

      - `Optional<ContextSize> contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Optional<Mode> mode`

        The source used for web search results. Defaults to `live`.

        - `DISABLED("disabled")`

          Disables web search.

        - `CACHED("cached")`

          Uses cached search results.

        - `LIVE("live")`

          Searches the live web.

    - `ComputerUse`

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

      - `Optional<Boolean> includeScreenshots`

        Whether computer tool outputs include screenshots. Defaults to `false`.

### Returns

- `class Agent:`

  A reusable agent scoped to the caller's project.

  - `String id`

    The ID of the reusable agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the agent was created.

  - `Optional<String> instructions`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata metadata`

    Custom string key-value pairs attached to the agent.

  - `String model`

    The requested model name used for inference.

  - `MultiAgentConfig multiAgent`

    The resolved configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Optional<String> name`

    A human-readable name for the agent, or null if it is unnamed.

  - `JsonValue; object_ "agent"constant`

    The object type. Always `agent`.

    - `AGENT("agent")`

  - `AgentReasoning reasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Optional<Effort> effort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

      - `MAX("max")`

    - `Optional<Summary> summary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `CONCISE("concise")`

        Returns a concise reasoning summary when supported.

      - `DETAILED("detailed")`

        Returns a detailed reasoning summary when supported.

      - `AUTO("auto")`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier serviceTier`

    The resolved service-tier policy used for model requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The resolved configuration for text generated by the agent.

    - `TextFormat format`

      The effective output format. Defaults to ordinary text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          The type of the object. Always `text`.

          - `TEXT("text")`

      - `JsonSchema`

        - `Schema schema`

          The JSON Schema that generated text must match.

        - `JsonValue; type "json_schema"constant`

          The type of the object. Always `json_schema`.

          - `JSON_SCHEMA("json_schema")`

    - `Verbosity verbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `List<PersistedAgentTool> tools`

    Tools available to the agent.

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransport transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `Headers headers`

            Non-secret HTTP headers sent to the MCP server.

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode mode`

        The source used for web search results.

        - `DISABLED("disabled")`

        - `CACHED("cached")`

        - `LIVE("live")`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

    - `ComputerUse`

      - `boolean includeScreenshots`

        Whether computer tool outputs include screenshots.

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the agent was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Agent;
import com.openai.models.beta.agents.AgentUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Agent agent = client.beta().agents().update("agent_id");
    }
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

- `class Agent:`

  A reusable agent scoped to the caller's project.

  - `String id`

    The ID of the reusable agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the agent was created.

  - `Optional<String> instructions`

    Custom instructions appended to the agent's default base instructions.

  - `Metadata metadata`

    Custom string key-value pairs attached to the agent.

  - `String model`

    The requested model name used for inference.

  - `MultiAgentConfig multiAgent`

    The resolved configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

  - `Optional<String> name`

    A human-readable name for the agent, or null if it is unnamed.

  - `JsonValue; object_ "agent"constant`

    The object type. Always `agent`.

    - `AGENT("agent")`

  - `AgentReasoning reasoning`

    The resolved reasoning configuration, including the model default for an omitted effort.

    - `Optional<Effort> effort`

      The requested reasoning effort, or `null` when the model selects its own default.

      - `NONE("none")`

      - `MINIMAL("minimal")`

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

      - `XHIGH("xhigh")`

      - `MAX("max")`

    - `Optional<Summary> summary`

      The requested reasoning summary format, or `null` when summaries are disabled.

      - `CONCISE("concise")`

        Returns a concise reasoning summary when supported.

      - `DETAILED("detailed")`

        Returns a detailed reasoning summary when supported.

      - `AUTO("auto")`

        Automatically selects the most detailed summary supported by the model.

  - `ServiceTier serviceTier`

    The resolved service-tier policy used for model requests.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The resolved configuration for text generated by the agent.

    - `TextFormat format`

      The effective output format. Defaults to ordinary text.

      - `JsonValue;`

        - `JsonValue; type "text"constant`

          The type of the object. Always `text`.

          - `TEXT("text")`

      - `JsonSchema`

        - `Schema schema`

          The JSON Schema that generated text must match.

        - `JsonValue; type "json_schema"constant`

          The type of the object. Always `json_schema`.

          - `JSON_SCHEMA("json_schema")`

    - `Verbosity verbosity`

      The amount of text produced by the agent. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

  - `List<PersistedAgentTool> tools`

    Tools available to the agent.

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

      - `String name`

        The name of the function.

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

    - `JsonValue;`

      - `JsonValue; type "tool_search"constant`

        The type of the object. Always `tool_search`.

        - `TOOL_SEARCH("tool_search")`

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call, or null when all server tools are allowed.

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The vault credential selected for this MCP server, if any.

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

      - `PersistedMcpTransport transport`

        The credential-free transport used to connect to the MCP server.

        - `Http`

          - `Headers headers`

            Non-secret HTTP headers sent to the MCP server.

          - `String serverUrl`

            The URL of the MCP server.

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

          - `String command`

            The command used to start the MCP server.

          - `String cwd`

            The working directory used to start the MCP server.

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

        - `Optional<String> region`

          The region or state name.

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

      - `Mode mode`

        The source used for web search results.

        - `DISABLED("disabled")`

        - `CACHED("cached")`

        - `LIVE("live")`

      - `JsonValue; type "web_search"constant`

        The type of the object. Always `web_search`.

        - `WEB_SEARCH("web_search")`

    - `ComputerUse`

      - `boolean includeScreenshots`

        Whether computer tool outputs include screenshots.

      - `JsonValue; type "computer_use"constant`

        The type of the object. Always `computer_use`.

        - `COMPUTER_USE("computer_use")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the agent was last updated.

### Agent Browser Authentication Cancel Param

- `class AgentBrowserAuthenticationCancelParam:`

  - `JsonValue; action "cancel"constant`

    - `CANCEL("cancel")`

  - `JsonValue; type "browser_authentication"constant`

    - `BROWSER_AUTHENTICATION("browser_authentication")`

### Agent Browser Authentication Submit Param

- `class AgentBrowserAuthenticationSubmitParam:`

  - `JsonValue; action "submit"constant`

    - `SUBMIT("submit")`

  - `List<Field> fields`

    Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

    - `String fieldId`

      The field ID from the required action.

    - `String value`

      The value to enter into the registered control.

  - `JsonValue; type "browser_authentication"constant`

    - `BROWSER_AUTHENTICATION("browser_authentication")`

  - `Optional<String> selectedOption`

    The chosen method. Required when the required action contains options.

### Agent Browser Origin Access Param

- `class AgentBrowserOriginAccessParam:`

  - `Decision decision`

    Whether to allow, deny, or cancel the requested origin access.

    - `APPROVE("approve")`

      Allow the browser to access this origin.

    - `DENY("deny")`

      Deny access to this origin.

    - `CANCEL("cancel")`

      Dismiss this request without approving access.

  - `JsonValue; type "browser_origin_access"constant`

    - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

### Agent Close Subagent Call Item

- `class AgentCloseSubagentCallItem:`

  A request to close a subagent.

  - `String id`

    The ID of the tool call item.

  - `String recipientAgentId`

    The ID of the agent to close.

  - `String senderAgentId`

    The ID of the agent requesting the close.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "close_subagent_call"constant`

    The item type. Always `close_subagent_call`.

    - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

      The current public item type.

### Agent Command Execution Item

- `class AgentCommandExecutionItem:`

  A command execution produced by the agent.

  - `String id`

    The ID of the command execution item.

  - `String command`

    The command that was executed.

  - `Optional<String> cwd`

    The working directory used to execute the command.

  - `Optional<Long> durationMs`

    The command duration in milliseconds.

  - `Optional<Long> exitCode`

    The process exit code, if the command completed.

  - `Optional<String> output`

    The command output, if available.

  - `AgentFunctionCallStatus status`

    The status of the command execution.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "command_execution"constant`

    The item type. Always `command_execution`.

    - `COMMAND_EXECUTION("command_execution")`

### Agent Content

- `class AgentContent: A class that can be one of several variants.union`

  A plaintext or encrypted content part exchanged between agents.

  - `class OutputText:`

    A text content part produced by the agent.

    - `String text`

      The text produced by the agent.

    - `JsonValue; type "output_text"constant`

      The content type. Always `output_text`.

      - `OUTPUT_TEXT("output_text")`

  - `EncryptedContent`

    - `String encryptedContent`

      The encrypted content payload.

    - `JsonValue; type "encrypted_content"constant`

      The content type. Always `encrypted_content`.

      - `ENCRYPTED_CONTENT("encrypted_content")`

### Agent Create Subagent Call Item

- `class AgentCreateSubagentCallItem:`

  A request to spawn a subagent.

  - `String id`

    The ID of the tool call item.

  - `String agentId`

    The ID of the agent that requested the subagent.

  - `List<AgentContent> content`

    The task given to the spawned agent.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `Optional<String> model`

    The model requested for the spawned agent.

  - `Optional<String> reasoningEffort`

    The reasoning effort requested for the spawned agent.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "create_subagent_call"constant`

    The item type. Always `create_subagent_call`.

    - `CREATE_SUBAGENT_CALL("create_subagent_call")`

      The current public item type.

### Agent Deleted

- `class AgentDeleted:`

  A deleted reusable agent.

  - `String id`

    The ID of the deleted agent.

  - `boolean deleted`

    Whether the agent was deleted. Always `true`.

  - `JsonValue; object_ "agent.deleted"constant`

    The object type. Always `agent.deleted`.

    - `AGENT_DELETED("agent.deleted")`

### Agent Function Call Item

- `class AgentFunctionCallItem:`

  A function call produced by the agent.

  - `String id`

    The ID of the function call item.

  - `JsonValue arguments`

    The arguments to pass to the function.

  - `String callId`

    The ID used to submit the function result.

  - `String name`

    The name of the function to call.

  - `AgentFunctionCallStatus status`

    The status of the function call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "function_call"constant`

    The item type. Always `function_call`.

    - `FUNCTION_CALL("function_call")`

### Agent Function Call Output

- `class AgentFunctionCallOutput: A class that can be one of several variants.union`

  The text or model-input content supplied as a function result.

  - `String`

  - `List<InputContent>`

    - `InputText`

      - `String text`

        The text supplied to the agent.

      - `JsonValue; type "input_text"constant`

        The type of the object. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `InputImage`

      - `String imageUrl`

        The URL of the image supplied to the agent, which may be a base64-encoded data URL.

      - `JsonValue; type "input_image"constant`

        The type of the object. Always `input_image`.

        - `INPUT_IMAGE("input_image")`

### Agent Function Call Output Param

- `class AgentFunctionCallOutputParam: A class that can be one of several variants.union`

  A function result represented as text or supported model-input content.

  - `String`

  - `List<InputContentParam>`

    - `InputText`

      - `String text`

        The text sent to the model.

      - `JsonValue; type "input_text"constant`

        The type of the object. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `InputImage`

      - `String imageUrl`

        The URL of the image sent to the model.

      - `JsonValue; type "input_image"constant`

        The type of the object. Always `input_image`.

        - `INPUT_IMAGE("input_image")`

### Agent Function Call Status

- `enum AgentFunctionCallStatus:`

  The status of a tool call.

  - `IN_PROGRESS("in_progress")`

    The call is in progress.

  - `COMPLETED("completed")`

    The call completed successfully.

  - `FAILED("failed")`

    The call failed.

  - `INCOMPLETE("incomplete")`

    The call stopped before completing.

### Agent Interrupt Subagent Call Item

- `class AgentInterruptSubagentCallItem:`

  A request to interrupt a subagent's current turn. The subagent remains available.

  - `String id`

    The ID of the tool call item.

  - `String recipientAgentId`

    The ID of the agent to interrupt.

  - `String senderAgentId`

    The ID of the agent requesting the interrupt.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "interrupt_subagent_call"constant`

    The item type. Always `interrupt_subagent_call`.

    - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

      The current public item type.

### Agent Mcp Call Item

- `class AgentMcpCallItem:`

  A call to a tool on an MCP server.

  - `String id`

    The ID of the MCP call item.

  - `JsonValue arguments`

    The arguments passed to the MCP tool.

  - `JsonValue error`

    The error returned by the MCP tool, if any.

  - `String name`

    The name of the MCP tool.

  - `JsonValue output`

    The output returned by the MCP tool, if any.

  - `String serverLabel`

    The label of the MCP server.

  - `AgentFunctionCallStatus status`

    The status of the MCP tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "mcp_call"constant`

    The item type. Always `mcp_call`.

    - `MCP_CALL("mcp_call")`

### Agent Output Command Execution Output Delta Event

- `class AgentOutputCommandExecutionOutputDeltaEvent:`

  Emitted when command execution produces an output delta.

  - `String delta`

    The output text that was appended.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the command execution item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.output.command_execution_output.delta"constant`

    The type of the object. Always `agent.output.command_execution_output.delta`.

    - `AGENT_OUTPUT_COMMAND_EXECUTION_OUTPUT_DELTA("agent.output.command_execution_output.delta")`

### Agent Output Item

- `class AgentOutputItem: A class that can be one of several variants.union`

  An output item produced by an agent.

  - `class AgentSessionAssistantMessage:`

    An assistant message produced by the agent.

    - `String id`

      The ID of the message.

    - `List<OutputText> content`

      The content of the message.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `Optional<Phase> phase`

      The phase of the assistant message.

      - `COMMENTARY("commentary")`

        Commentary produced while the agent works.

      - `FINAL_ANSWER("final_answer")`

        The agent's final answer.

    - `JsonValue; role "assistant"constant`

      The role of the message author. Always `assistant`.

      - `ASSISTANT("assistant")`

    - `AgentOutputItemStatus status`

      The status of the message.

      - `IN_PROGRESS("in_progress")`

        The item is in progress.

      - `COMPLETED("completed")`

        The item is complete.

      - `INCOMPLETE("incomplete")`

        The item stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

    - `String name`

      The name of the function to call.

    - `AgentFunctionCallStatus status`

      The status of the function call.

      - `IN_PROGRESS("in_progress")`

        The call is in progress.

      - `COMPLETED("completed")`

        The call completed successfully.

      - `FAILED("failed")`

        The call failed.

      - `INCOMPLETE("incomplete")`

        The call stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        - `String id`

          The field ID to submit as field_id in a fields entry.

        - `String label`

          The label to display beside the control.

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        - `String id`

          The option ID to submit as selected_option.

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

        - `String label`

          The method label to display.

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

    - `String turnId`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

        - `Optional<String> query`

          The search query, when a single query was used.

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

    - `String command`

      The command that was executed.

    - `Optional<String> cwd`

      The working directory used to execute the command.

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

    - `Optional<String> output`

      The command output, if available.

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

    - `String agentId`

      The ID of the agent that requested the subagent.

    - `List<AgentContent> content`

      The task given to the spawned agent.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `Optional<String> model`

      The model requested for the spawned agent.

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

        The current public item type.

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

    - `String senderAgentId`

      The ID of the agent sending the input.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

        The current public item type.

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to resume.

    - `String senderAgentId`

      The ID of the agent requesting the resume.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

    - `String senderAgentId`

      The ID of the agent waiting for results.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

        The current public item type.

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to interrupt.

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

        The current public item type.

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to close.

    - `String senderAgentId`

      The ID of the agent requesting the close.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

        The current public item type.

### Agent Output Item Status

- `enum AgentOutputItemStatus:`

  The status of an agent output item.

  - `IN_PROGRESS("in_progress")`

    The item is in progress.

  - `COMPLETED("completed")`

    The item is complete.

  - `INCOMPLETE("incomplete")`

    The item stopped before completing.

### Agent Reasoning

- `class AgentReasoning:`

  The reasoning configuration used by an agent.

  - `Optional<Effort> effort`

    The requested reasoning effort, or `null` when the model selects its own default.

    - `NONE("none")`

    - `MINIMAL("minimal")`

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

    - `XHIGH("xhigh")`

    - `MAX("max")`

  - `Optional<Summary> summary`

    The requested reasoning summary format, or `null` when summaries are disabled.

    - `CONCISE("concise")`

      Returns a concise reasoning summary when supported.

    - `DETAILED("detailed")`

      Returns a detailed reasoning summary when supported.

    - `AUTO("auto")`

      Automatically selects the most detailed summary supported by the model.

### Agent Reasoning Item

- `class AgentReasoningItem:`

  A reasoning item produced by the agent.

  - `String id`

    The ID of the reasoning item.

  - `Optional<AgentOutputItemStatus> status`

    The status of the reasoning item.

    - `IN_PROGRESS("in_progress")`

      The item is in progress.

    - `COMPLETED("completed")`

      The item is complete.

    - `INCOMPLETE("incomplete")`

      The item stopped before completing.

  - `List<SummaryText> summary`

    The reasoning summaries produced by the agent.

    - `String text`

      The reasoning summary text.

    - `JsonValue; type "summary_text"constant`

      The content type. Always `summary_text`.

      - `SUMMARY_TEXT("summary_text")`

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "reasoning"constant`

    The item type. Always `reasoning`.

    - `REASONING("reasoning")`

### Agent Reasoning Param

- `class AgentReasoningParam:`

  Reasoning configuration for the agent.

  - `Optional<Effort> effort`

    The amount of reasoning effort the model should use. Omission lets the model select it.

    - `NONE("none")`

    - `MINIMAL("minimal")`

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

    - `XHIGH("xhigh")`

    - `MAX("max")`

  - `Optional<Summary> summary`

    Controls whether the response includes a reasoning summary.

    - `CONCISE("concise")`

      Returns a concise reasoning summary when supported.

    - `DETAILED("detailed")`

      Returns a detailed reasoning summary when supported.

    - `AUTO("auto")`

      Automatically selects the most detailed summary supported by the model.

### Agent Resume Subagent Call Item

- `class AgentResumeSubagentCallItem:`

  A request to resume a subagent.

  - `String id`

    The ID of the tool call item.

  - `String recipientAgentId`

    The ID of the agent to resume.

  - `String senderAgentId`

    The ID of the agent requesting the resume.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "resume_subagent_call"constant`

    The item type. Always `resume_subagent_call`.

    - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

      The current public item type.

### Agent Send Subagent Input Call Item

- `class AgentSendSubagentInputCallItem:`

  A request to send input to another agent.

  - `String id`

    The ID of the tool call item.

  - `List<AgentContent> content`

    The input sent to the receiving agent.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `String recipientAgentId`

    The ID of the agent receiving the input.

  - `String senderAgentId`

    The ID of the agent sending the input.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "send_subagent_input_call"constant`

    The item type. Always `send_subagent_input_call`.

    - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

      The current public item type.

### Agent Session

- `class AgentSession:`

  A Managed Agents session.

  - `String id`

    The ID of the session.

  - `Agent agent`

    The agent running in the session.

    - `String id`

      The ID of the agent.

    - `Optional<String> instructions`

      Custom instructions appended to the agent's default base instructions.

    - `String model`

      The model used by the agent.

    - `MultiAgentConfig multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled. Defaults to false.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Optional<String> name`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `AgentReasoning reasoning`

      The agent's reasoning configuration.

      - `Optional<Effort> effort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier serviceTier`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `AUTO("auto")`

      - `DEFAULT("default")`

      - `FLEX("flex")`

      - `PRIORITY("priority")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

    - `AgentText text`

      Configuration for text generated by the agent.

      - `TextFormat format`

        The effective output format. Defaults to ordinary text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Verbosity verbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

    - `List<AgentTool> tools`

      Tools available to the agent.

      - `Function`

        - `boolean deferLoading`

          Whether the function is deferred and discovered through tool search.

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

      - `ProgrammaticToolCalling`

        - `boolean enabled`

          Whether tools can be called from model-generated code.

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Mcp`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call.

        - `ConnectionOrigin connectionOrigin`

          Where outbound MCP HTTP connections originate.

          - `SERVICE("service")`

          - `ENVIRONMENT("environment")`

        - `Optional<String> credentialId`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata requestMetadata`

          Metadata included with requests to this MCP server.

        - `boolean required`

          Whether this MCP server must initialize before the first turn.

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransport transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

          - `Stdio`

            - `List<String> args`

              Arguments passed to the MCP server command.

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `List<String> envVars`

              Environment variable names inherited from the execution environment.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

      - `WebSearch`

        - `Optional<List<String>> allowedDomains`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results, if provided.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode mode`

          The source used for web search results.

          - `DISABLED("disabled")`

          - `CACHED("cached")`

          - `LIVE("live")`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

      - `ComputerUse`

        - `boolean includeScreenshots`

          Whether computer tool outputs include screenshots.

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment environment`

    The execution environment for the session.

    - `JsonValue;`

      - `JsonValue; type "none"constant`

        The type of the object. Always `none`.

        - `NONE("none")`

    - `OpenAIHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `Desktop desktop`

        The effective desktop configuration.

        - `boolean enabled`

          Whether the environment provisions a desktop and browser proxy.

      - `List<HostedEnvironmentFile> files`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileId:`

          A file copied from the OpenAI Files API.

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String fileId`

            The ID of the uploaded file.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "file_id"constant`

            The type of the object. Always `file_id`.

            - `FILE_ID("file_id")`

        - `Inline`

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `Network network`

        The effective network access policy for the environment.

        - `Access access`

          The environment's network access mode.

          - `ENABLED("enabled")`

            Allows unrestricted network access.

          - `DISABLED("disabled")`

            Disables network access.

          - `RESTRICTED("restricted")`

            Applies the configured domain restrictions.

        - `List<String> allowedDomains`

          Domains the environment may access when network access is restricted.

      - `Packages packages`

        Packages installed in the environment.

        - `List<String> npm`

          npm packages installed globally in the environment.

        - `List<String> python`

          Python packages installed in the environment.

        - `List<String> system`

          System packages installed in the environment.

      - `List<HostedPlugin> plugins`

        Plugins installed in the environment, excluding their archive contents.

        - `String description`

          The installed plugin description.

        - `String name`

          The installed plugin name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

      - `List<HostedSkill> skills`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference:`

          A skill installed from the Skills API.

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `String skillId`

            The referenced skill ID.

          - `JsonValue; type "skill_reference"constant`

            The type of the object. Always `skill_reference`.

            - `SKILL_REFERENCE("skill_reference")`

          - `String version`

            The concrete skill version installed for this session.

        - `Inline`

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `JsonValue; type "openai_hosted"constant`

        The type of the object. Always `openai_hosted`.

        - `OPENAI_HOSTED("openai_hosted")`

      - `Optional<ContainerSize> containerSize`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `SMALL("small")`

        - `MEDIUM("medium")`

        - `LARGE("large")`

    - `SelfHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `String remoteUrl`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `JsonValue; type "self_hosted"constant`

        The type of the object. Always `self_hosted`.

        - `SELF_HOSTED("self_hosted")`

      - `String workspaceDirectory`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Optional<String> error`

    The error that caused the session to fail, if any.

  - `long lastActiveAt`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata metadata`

    Custom string key-value pairs attached to the session.

  - `JsonValue; object_ "agent.session"constant`

    The object type. Always `agent.session`.

    - `AGENT_SESSION("agent.session")`

  - `List<RequiredAction> requiredActions`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest:`

      Respond to a computer-use request.

      - `Request request`

        The information needed to render the request.

        - `class BrowserAuthentication:`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class BrowserOriginAccess:`

          A browser origin awaiting the application's approval decision.

          - `String origin`

            The origin the browser needs permission to access.

          - `Optional<String> reason`

            The browser's explanation for this request, or null when unavailable.

          - `JsonValue; type "browser_origin_access"constant`

            The type of the object. Always `browser_origin_access`.

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `String requestId`

        The registered request ID to echo when responding.

      - `String turnId`

        The turn that requested approval.

      - `JsonValue; type "computer_use_approval_request"constant`

        The type of the object. Always `computer_use_approval_request`.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class FunctionCall:`

      Run a function tool and submit its result.

      - `JsonValue arguments`

        The arguments supplied by the model.

      - `String callId`

        The ID to include when submitting the function result.

      - `String name`

        The function name.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "function_call"constant`

        The type of the object. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class EnvironmentConnection:`

      Reconnect a session environment.

      - `String environmentId`

        The ID of the environment to reconnect.

      - `JsonValue; type "environment_connection"constant`

        The type of the object. Always `environment_connection`.

        - `ENVIRONMENT_CONNECTION("environment_connection")`

  - `Status status`

    The current status of the session.

    - `IDLE("idle")`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `IN_PROGRESS("in_progress")`

      The session is processing a turn.

    - `REQUIRES_ACTION("requires_action")`

      The session is waiting for one or more required actions.

    - `FAILED("failed")`

      The session failed.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

  - `List<String> vaultIds`

    The IDs of vaults made available to the session.

### Agent Session Assistant Message

- `class AgentSessionAssistantMessage:`

  An assistant message produced by the agent.

  - `String id`

    The ID of the message.

  - `List<OutputText> content`

    The content of the message.

    - `String text`

      The text produced by the agent.

    - `JsonValue; type "output_text"constant`

      The content type. Always `output_text`.

      - `OUTPUT_TEXT("output_text")`

  - `Optional<Phase> phase`

    The phase of the assistant message.

    - `COMMENTARY("commentary")`

      Commentary produced while the agent works.

    - `FINAL_ANSWER("final_answer")`

      The agent's final answer.

  - `JsonValue; role "assistant"constant`

    The role of the message author. Always `assistant`.

    - `ASSISTANT("assistant")`

  - `AgentOutputItemStatus status`

    The status of the message.

    - `IN_PROGRESS("in_progress")`

      The item is in progress.

    - `COMPLETED("completed")`

      The item is complete.

    - `INCOMPLETE("incomplete")`

      The item stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "message"constant`

    The item type. Always `message`.

    - `MESSAGE("message")`

### Agent Session Created Event

- `class AgentSessionCreatedEvent:`

  Emitted when a session is created.

  - `String eventId`

    The unique ID of the event.

  - `AgentSession session`

    The session that was created.

    - `String id`

      The ID of the session.

    - `Agent agent`

      The agent running in the session.

      - `String id`

        The ID of the agent.

      - `Optional<String> instructions`

        Custom instructions appended to the agent's default base instructions.

      - `String model`

        The model used by the agent.

      - `MultiAgentConfig multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Optional<String> name`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `AgentReasoning reasoning`

        The agent's reasoning configuration.

        - `Optional<Effort> effort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<Summary> summary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `CONCISE("concise")`

            Returns a concise reasoning summary when supported.

          - `DETAILED("detailed")`

            Returns a detailed reasoning summary when supported.

          - `AUTO("auto")`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier serviceTier`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        Configuration for text generated by the agent.

        - `TextFormat format`

          The effective output format. Defaults to ordinary text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              The type of the object. Always `text`.

              - `TEXT("text")`

          - `JsonSchema`

            - `Schema schema`

              The JSON Schema that generated text must match.

            - `JsonValue; type "json_schema"constant`

              The type of the object. Always `json_schema`.

              - `JSON_SCHEMA("json_schema")`

        - `Verbosity verbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `List<AgentTool> tools`

        Tools available to the agent.

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

          - `String name`

            The name of the function.

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

              - `String command`

                The command used to start the MCP server.

              - `String cwd`

                The working directory used to start the MCP server.

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

            - `Optional<String> region`

              The region or state name.

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode mode`

            The source used for web search results.

            - `DISABLED("disabled")`

            - `CACHED("cached")`

            - `LIVE("live")`

          - `JsonValue; type "web_search"constant`

            The type of the object. Always `web_search`.

            - `WEB_SEARCH("web_search")`

        - `ComputerUse`

          - `boolean includeScreenshots`

            Whether computer tool outputs include screenshots.

          - `JsonValue; type "computer_use"constant`

            The type of the object. Always `computer_use`.

            - `COMPUTER_USE("computer_use")`

    - `long createdAt`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment environment`

      The execution environment for the session.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `Desktop desktop`

          The effective desktop configuration.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `List<HostedEnvironmentFile> files`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileId:`

            A file copied from the OpenAI Files API.

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String fileId`

              The ID of the uploaded file.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Network network`

          The effective network access policy for the environment.

          - `Access access`

            The environment's network access mode.

            - `ENABLED("enabled")`

              Allows unrestricted network access.

            - `DISABLED("disabled")`

              Disables network access.

            - `RESTRICTED("restricted")`

              Applies the configured domain restrictions.

          - `List<String> allowedDomains`

            Domains the environment may access when network access is restricted.

        - `Packages packages`

          Packages installed in the environment.

          - `List<String> npm`

            npm packages installed globally in the environment.

          - `List<String> python`

            Python packages installed in the environment.

          - `List<String> system`

            System packages installed in the environment.

        - `List<HostedPlugin> plugins`

          Plugins installed in the environment, excluding their archive contents.

          - `String description`

            The installed plugin description.

          - `String name`

            The installed plugin name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `List<HostedSkill> skills`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference:`

            A skill installed from the Skills API.

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `String skillId`

              The referenced skill ID.

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `String version`

              The concrete skill version installed for this session.

          - `Inline`

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

        - `Optional<ContainerSize> containerSize`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

      - `SelfHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `String remoteUrl`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Optional<String> error`

      The error that caused the session to fail, if any.

    - `long lastActiveAt`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata metadata`

      Custom string key-value pairs attached to the session.

    - `JsonValue; object_ "agent.session"constant`

      The object type. Always `agent.session`.

      - `AGENT_SESSION("agent.session")`

    - `List<RequiredAction> requiredActions`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest:`

        Respond to a computer-use request.

        - `Request request`

          The information needed to render the request.

          - `class BrowserAuthentication:`

            A registered form awaiting the application's response.

            - `Optional<String> credentialOrigin`

              The registered form or frame origin where values will be entered.

            - `List<Field> fields`

              Controls to render. All submitted values are sensitive.

              - `String id`

                The field ID to submit as field_id in a fields entry.

              - `String label`

                The label to display beside the control.

              - `boolean required`

                Whether this control requires a nonempty value.

              - `String type`

                The rendering type, such as email, password, or text.

            - `List<Option> options`

              Sign-in methods. Empty for a plain form.

              - `String id`

                The option ID to submit as selected_option.

              - `List<String> fieldIds`

                IDs from the registered fields that this method accepts.

              - `String label`

                The method label to display.

            - `Optional<String> reason`

              Why the agent needs the user to sign in.

            - `JsonValue; type "browser_authentication"constant`

              The type of the object. Always `browser_authentication`.

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `class BrowserOriginAccess:`

            A browser origin awaiting the application's approval decision.

            - `String origin`

              The origin the browser needs permission to access.

            - `Optional<String> reason`

              The browser's explanation for this request, or null when unavailable.

            - `JsonValue; type "browser_origin_access"constant`

              The type of the object. Always `browser_origin_access`.

              - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

        - `String requestId`

          The registered request ID to echo when responding.

        - `String turnId`

          The turn that requested approval.

        - `JsonValue; type "computer_use_approval_request"constant`

          The type of the object. Always `computer_use_approval_request`.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class FunctionCall:`

        Run a function tool and submit its result.

        - `JsonValue arguments`

          The arguments supplied by the model.

        - `String callId`

          The ID to include when submitting the function result.

        - `String name`

          The function name.

        - `String turnId`

          The ID of the turn that requested the function call.

        - `JsonValue; type "function_call"constant`

          The type of the object. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `class EnvironmentConnection:`

        Reconnect a session environment.

        - `String environmentId`

          The ID of the environment to reconnect.

        - `JsonValue; type "environment_connection"constant`

          The type of the object. Always `environment_connection`.

          - `ENVIRONMENT_CONNECTION("environment_connection")`

    - `Status status`

      The current status of the session.

      - `IDLE("idle")`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `IN_PROGRESS("in_progress")`

        The session is processing a turn.

      - `REQUIRES_ACTION("requires_action")`

        The session is waiting for one or more required actions.

      - `FAILED("failed")`

        The session failed.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

    - `List<String> vaultIds`

      The IDs of vaults made available to the session.

  - `JsonValue; type "agent.session.created"constant`

    The type of the object. Always `agent.session.created`.

    - `AGENT_SESSION_CREATED("agent.session.created")`

### Agent Session Deleted

- `class AgentSessionDeleted:`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `String id`

    The ID of the deleted session.

  - `boolean deleted`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `JsonValue; object_ "agent.session.deleted"constant`

    The object type. Always `agent.session.deleted`.

    - `AGENT_SESSION_DELETED("agent.session.deleted")`

### Agent Session Environment Connected Event

- `class AgentSessionEnvironmentConnectedEvent:`

  Emitted when a session environment connects.

  - `AgentSessionEnvironmentState environment`

    The current environment state.

    - `String id`

      The public ID of the environment.

    - `Optional<Error> error`

      The error reported while preparing the environment, if any.

      - `String code`

        A machine-readable error code.

      - `String message`

        A human-readable error message.

      - `String type`

        The error type.

    - `Status status`

      The environment's connection status.

      - `PENDING("pending")`

        The environment is being prepared.

      - `READY("ready")`

        The environment is ready to connect.

      - `CONNECTED("connected")`

        The environment is connected.

      - `DISCONNECTED("disconnected")`

        The environment is disconnected.

      - `FAILED("failed")`

        The environment failed to connect.

    - `String type`

      The environment type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.environment.connected"constant`

    The type of the object. Always `agent.session.environment.connected`.

    - `AGENT_SESSION_ENVIRONMENT_CONNECTED("agent.session.environment.connected")`

### Agent Session Environment Disconnected Event

- `class AgentSessionEnvironmentDisconnectedEvent:`

  Emitted when a session environment disconnects.

  - `AgentSessionEnvironmentState environment`

    The current environment state.

    - `String id`

      The public ID of the environment.

    - `Optional<Error> error`

      The error reported while preparing the environment, if any.

      - `String code`

        A machine-readable error code.

      - `String message`

        A human-readable error message.

      - `String type`

        The error type.

    - `Status status`

      The environment's connection status.

      - `PENDING("pending")`

        The environment is being prepared.

      - `READY("ready")`

        The environment is ready to connect.

      - `CONNECTED("connected")`

        The environment is connected.

      - `DISCONNECTED("disconnected")`

        The environment is disconnected.

      - `FAILED("failed")`

        The environment failed to connect.

    - `String type`

      The environment type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.environment.disconnected"constant`

    The type of the object. Always `agent.session.environment.disconnected`.

    - `AGENT_SESSION_ENVIRONMENT_DISCONNECTED("agent.session.environment.disconnected")`

### Agent Session Environment Failed Event

- `class AgentSessionEnvironmentFailedEvent:`

  Emitted when a session environment fails.

  - `AgentSessionEnvironmentState environment`

    The current environment state.

    - `String id`

      The public ID of the environment.

    - `Optional<Error> error`

      The error reported while preparing the environment, if any.

      - `String code`

        A machine-readable error code.

      - `String message`

        A human-readable error message.

      - `String type`

        The error type.

    - `Status status`

      The environment's connection status.

      - `PENDING("pending")`

        The environment is being prepared.

      - `READY("ready")`

        The environment is ready to connect.

      - `CONNECTED("connected")`

        The environment is connected.

      - `DISCONNECTED("disconnected")`

        The environment is disconnected.

      - `FAILED("failed")`

        The environment failed to connect.

    - `String type`

      The environment type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.environment.failed"constant`

    The type of the object. Always `agent.session.environment.failed`.

    - `AGENT_SESSION_ENVIRONMENT_FAILED("agent.session.environment.failed")`

### Agent Session Environment Pending Event

- `class AgentSessionEnvironmentPendingEvent:`

  Emitted while a session environment is being prepared.

  - `AgentSessionEnvironmentState environment`

    The current environment state.

    - `String id`

      The public ID of the environment.

    - `Optional<Error> error`

      The error reported while preparing the environment, if any.

      - `String code`

        A machine-readable error code.

      - `String message`

        A human-readable error message.

      - `String type`

        The error type.

    - `Status status`

      The environment's connection status.

      - `PENDING("pending")`

        The environment is being prepared.

      - `READY("ready")`

        The environment is ready to connect.

      - `CONNECTED("connected")`

        The environment is connected.

      - `DISCONNECTED("disconnected")`

        The environment is disconnected.

      - `FAILED("failed")`

        The environment failed to connect.

    - `String type`

      The environment type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.environment.pending"constant`

    The type of the object. Always `agent.session.environment.pending`.

    - `AGENT_SESSION_ENVIRONMENT_PENDING("agent.session.environment.pending")`

### Agent Session Environment Ready Event

- `class AgentSessionEnvironmentReadyEvent:`

  Emitted when a hosted session environment is ready to connect.

  - `AgentSessionEnvironmentState environment`

    The current environment state.

    - `String id`

      The public ID of the environment.

    - `Optional<Error> error`

      The error reported while preparing the environment, if any.

      - `String code`

        A machine-readable error code.

      - `String message`

        A human-readable error message.

      - `String type`

        The error type.

    - `Status status`

      The environment's connection status.

      - `PENDING("pending")`

        The environment is being prepared.

      - `READY("ready")`

        The environment is ready to connect.

      - `CONNECTED("connected")`

        The environment is connected.

      - `DISCONNECTED("disconnected")`

        The environment is disconnected.

      - `FAILED("failed")`

        The environment failed to connect.

    - `String type`

      The environment type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.environment.ready"constant`

    The type of the object. Always `agent.session.environment.ready`.

    - `AGENT_SESSION_ENVIRONMENT_READY("agent.session.environment.ready")`

### Agent Session Environment Reset Event

- `class AgentSessionEnvironmentResetEvent:`

  Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

  - `String environmentId`

    The stable environment ID, retained across sandbox replacements.

  - `String eventId`

    The unique ID of the event.

  - `long resetCount`

    Monotonically increasing reset number. Repeated notifications share this number.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The associated turn, when applicable.

  - `JsonValue; type "agent.session.environment.reset"constant`

    The type of the object. Always `agent.session.environment.reset`.

    - `AGENT_SESSION_ENVIRONMENT_RESET("agent.session.environment.reset")`

### Agent Session Environment State

- `class AgentSessionEnvironmentState:`

  The current state of a session environment.

  - `String id`

    The public ID of the environment.

  - `Optional<Error> error`

    The error reported while preparing the environment, if any.

    - `String code`

      A machine-readable error code.

    - `String message`

      A human-readable error message.

    - `String type`

      The error type.

  - `Status status`

    The environment's connection status.

    - `PENDING("pending")`

      The environment is being prepared.

    - `READY("ready")`

      The environment is ready to connect.

    - `CONNECTED("connected")`

      The environment is connected.

    - `DISCONNECTED("disconnected")`

      The environment is disconnected.

    - `FAILED("failed")`

      The environment failed to connect.

  - `String type`

    The environment type.

### Agent Session Error Event

- `class AgentSessionErrorEvent:`

  Emitted when a turn or session fails.

  - `SessionError error`

    The error that occurred.

    - `Optional<String> code`

      The machine-readable error code, if any.

    - `String message`

      A customer-safe explanation of the error.

    - `Optional<String> param`

      The request parameter associated with the error, if any.

    - `String type`

      The error type.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `JsonValue; type "error"constant`

    The type of the object. Always `error`.

    - `ERROR("error")`

### Agent Session Event

- `class AgentSessionEvent: A class that can be one of several variants.union`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent:`

    Emitted when a turn or session fails.

    - `SessionError error`

      The error that occurred.

      - `Optional<String> code`

        The machine-readable error code, if any.

      - `String message`

        A customer-safe explanation of the error.

      - `Optional<String> param`

        The request parameter associated with the error, if any.

      - `String type`

        The error type.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `JsonValue; type "error"constant`

      The type of the object. Always `error`.

      - `ERROR("error")`

  - `class AgentSessionEnvironmentReadyEvent:`

    Emitted when a hosted session environment is ready to connect.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

      - `String id`

        The public ID of the environment.

      - `Optional<Error> error`

        The error reported while preparing the environment, if any.

        - `String code`

          A machine-readable error code.

        - `String message`

          A human-readable error message.

        - `String type`

          The error type.

      - `Status status`

        The environment's connection status.

        - `PENDING("pending")`

          The environment is being prepared.

        - `READY("ready")`

          The environment is ready to connect.

        - `CONNECTED("connected")`

          The environment is connected.

        - `DISCONNECTED("disconnected")`

          The environment is disconnected.

        - `FAILED("failed")`

          The environment failed to connect.

      - `String type`

        The environment type.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.ready"constant`

      The type of the object. Always `agent.session.environment.ready`.

      - `AGENT_SESSION_ENVIRONMENT_READY("agent.session.environment.ready")`

  - `class AgentSessionEnvironmentResetEvent:`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `String environmentId`

      The stable environment ID, retained across sandbox replacements.

    - `String eventId`

      The unique ID of the event.

    - `long resetCount`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The associated turn, when applicable.

    - `JsonValue; type "agent.session.environment.reset"constant`

      The type of the object. Always `agent.session.environment.reset`.

      - `AGENT_SESSION_ENVIRONMENT_RESET("agent.session.environment.reset")`

  - `class AgentOutputCommandExecutionOutputDeltaEvent:`

    Emitted when command execution produces an output delta.

    - `String delta`

      The output text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the command execution item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.output.command_execution_output.delta"constant`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `AGENT_OUTPUT_COMMAND_EXECUTION_OUTPUT_DELTA("agent.output.command_execution_output.delta")`

  - `class AgentSessionCreatedEvent:`

    Emitted when a session is created.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that was created.

      - `String id`

        The ID of the session.

      - `Agent agent`

        The agent running in the session.

        - `String id`

          The ID of the agent.

        - `Optional<String> instructions`

          Custom instructions appended to the agent's default base instructions.

        - `String model`

          The model used by the agent.

        - `MultiAgentConfig multiAgent`

          Configuration for creating and coordinating subagents.

          - `boolean enabled`

            Whether subagent tools are enabled. Defaults to false.

          - `Optional<Long> maxConcurrentSubagents`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `Optional<String> name`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `AgentReasoning reasoning`

          The agent's reasoning configuration.

          - `Optional<Effort> effort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

            - `MAX("max")`

          - `Optional<Summary> summary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `CONCISE("concise")`

              Returns a concise reasoning summary when supported.

            - `DETAILED("detailed")`

              Returns a detailed reasoning summary when supported.

            - `AUTO("auto")`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier serviceTier`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `FAST("fast")`

          - `ULTRAFAST("ultrafast")`

        - `AgentText text`

          Configuration for text generated by the agent.

          - `TextFormat format`

            The effective output format. Defaults to ordinary text.

            - `JsonValue;`

              - `JsonValue; type "text"constant`

                The type of the object. Always `text`.

                - `TEXT("text")`

            - `JsonSchema`

              - `Schema schema`

                The JSON Schema that generated text must match.

              - `JsonValue; type "json_schema"constant`

                The type of the object. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

          - `Verbosity verbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `List<AgentTool> tools`

          Tools available to the agent.

          - `Function`

            - `boolean deferLoading`

              Whether the function is deferred and discovered through tool search.

            - `String description`

              A description of what the function does.

            - `String name`

              The name of the function.

            - `Parameters parameters`

              A JSON Schema object describing the function's arguments.

            - `JsonValue; type "function"constant`

              The type of the object. Always `function`.

              - `FUNCTION("function")`

          - `ProgrammaticToolCalling`

            - `boolean enabled`

              Whether tools can be called from model-generated code.

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the object. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `Mcp`

            - `Optional<List<String>> allowedTools`

              The MCP tools the agent may call.

            - `ConnectionOrigin connectionOrigin`

              Where outbound MCP HTTP connections originate.

              - `SERVICE("service")`

              - `ENVIRONMENT("environment")`

            - `Optional<String> credentialId`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `RequestMetadata requestMetadata`

              Metadata included with requests to this MCP server.

            - `boolean required`

              Whether this MCP server must initialize before the first turn.

            - `String serverLabel`

              A label used to identify the MCP server in tool calls.

            - `McpTransport transport`

              The transport used to connect to the MCP server.

              - `Http`

                - `String serverUrl`

                  The URL of the MCP server.

                - `JsonValue; type "http"constant`

                  The type of the object. Always `http`.

                  - `HTTP("http")`

              - `Stdio`

                - `List<String> args`

                  Arguments passed to the MCP server command.

                - `String command`

                  The command used to start the MCP server.

                - `String cwd`

                  The working directory used to start the MCP server.

                - `List<String> envVars`

                  Environment variable names inherited from the execution environment.

                - `JsonValue; type "stdio"constant`

                  The type of the object. Always `stdio`.

                  - `STDIO("stdio")`

            - `JsonValue; type "mcp"constant`

              The type of the object. Always `mcp`.

              - `MCP("mcp")`

          - `WebSearch`

            - `Optional<List<String>> allowedDomains`

              Allowed search domains, or `null` when the search is unrestricted.

            - `ContextSize contextSize`

              The amount of search context made available to the model. Defaults to `medium`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<Location> location`

              Approximate location used to localize search results, if provided.

              - `Optional<String> city`

                The city name.

              - `Optional<String> country`

                The two-letter ISO country code, such as `US`.

              - `Optional<String> region`

                The region or state name.

              - `Optional<String> timezone`

                The IANA timezone, such as `America/Los_Angeles`.

            - `Mode mode`

              The source used for web search results.

              - `DISABLED("disabled")`

              - `CACHED("cached")`

              - `LIVE("live")`

            - `JsonValue; type "web_search"constant`

              The type of the object. Always `web_search`.

              - `WEB_SEARCH("web_search")`

          - `ComputerUse`

            - `boolean includeScreenshots`

              Whether computer tool outputs include screenshots.

            - `JsonValue; type "computer_use"constant`

              The type of the object. Always `computer_use`.

              - `COMPUTER_USE("computer_use")`

      - `long createdAt`

        The Unix timestamp, in seconds, when the session was created.

      - `Environment environment`

        The execution environment for the session.

        - `JsonValue;`

          - `JsonValue; type "none"constant`

            The type of the object. Always `none`.

            - `NONE("none")`

        - `OpenAIHosted`

          - `String id`

            The public ID of the environment.

          - `List<String> capabilityDirectories`

            Directories that contain capabilities exposed to the agent.

          - `Desktop desktop`

            The effective desktop configuration.

            - `boolean enabled`

              Whether the environment provisions a desktop and browser proxy.

          - `List<HostedEnvironmentFile> files`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileId:`

              A file copied from the OpenAI Files API.

              - `String id`

                The session-scoped ID of the file in the execution environment.

              - `String fileId`

                The ID of the uploaded file.

              - `String path`

                The file's absolute path inside the environment.

              - `long sizeBytes`

                The decoded file size in bytes.

              - `JsonValue; type "file_id"constant`

                The type of the object. Always `file_id`.

                - `FILE_ID("file_id")`

            - `Inline`

              - `String id`

                The session-scoped ID of the file in the execution environment.

              - `String path`

                The file's absolute path inside the environment.

              - `long sizeBytes`

                The decoded file size in bytes.

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `Network network`

            The effective network access policy for the environment.

            - `Access access`

              The environment's network access mode.

              - `ENABLED("enabled")`

                Allows unrestricted network access.

              - `DISABLED("disabled")`

                Disables network access.

              - `RESTRICTED("restricted")`

                Applies the configured domain restrictions.

            - `List<String> allowedDomains`

              Domains the environment may access when network access is restricted.

          - `Packages packages`

            Packages installed in the environment.

            - `List<String> npm`

              npm packages installed globally in the environment.

            - `List<String> python`

              Python packages installed in the environment.

            - `List<String> system`

              System packages installed in the environment.

          - `List<HostedPlugin> plugins`

            Plugins installed in the environment, excluding their archive contents.

            - `String description`

              The installed plugin description.

            - `String name`

              The installed plugin name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

          - `List<HostedSkill> skills`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference:`

              A skill installed from the Skills API.

              - `String description`

                The installed skill description.

              - `String name`

                The installed skill name.

              - `String skillId`

                The referenced skill ID.

              - `JsonValue; type "skill_reference"constant`

                The type of the object. Always `skill_reference`.

                - `SKILL_REFERENCE("skill_reference")`

              - `String version`

                The concrete skill version installed for this session.

            - `Inline`

              - `String description`

                The installed skill description.

              - `String name`

                The installed skill name.

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `JsonValue; type "openai_hosted"constant`

            The type of the object. Always `openai_hosted`.

            - `OPENAI_HOSTED("openai_hosted")`

          - `Optional<ContainerSize> containerSize`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `SMALL("small")`

            - `MEDIUM("medium")`

            - `LARGE("large")`

        - `SelfHosted`

          - `String id`

            The public ID of the environment.

          - `List<String> capabilityDirectories`

            Directories that contain capabilities exposed to the agent.

          - `String remoteUrl`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `JsonValue; type "self_hosted"constant`

            The type of the object. Always `self_hosted`.

            - `SELF_HOSTED("self_hosted")`

          - `String workspaceDirectory`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `Optional<String> error`

        The error that caused the session to fail, if any.

      - `long lastActiveAt`

        The Unix timestamp, in seconds, when the session was last active.

      - `Metadata metadata`

        Custom string key-value pairs attached to the session.

      - `JsonValue; object_ "agent.session"constant`

        The object type. Always `agent.session`.

        - `AGENT_SESSION("agent.session")`

      - `List<RequiredAction> requiredActions`

        Actions that must be completed before the session can continue.

        - `class ComputerUseApprovalRequest:`

          Respond to a computer-use request.

          - `Request request`

            The information needed to render the request.

            - `class BrowserAuthentication:`

              A registered form awaiting the application's response.

              - `Optional<String> credentialOrigin`

                The registered form or frame origin where values will be entered.

              - `List<Field> fields`

                Controls to render. All submitted values are sensitive.

                - `String id`

                  The field ID to submit as field_id in a fields entry.

                - `String label`

                  The label to display beside the control.

                - `boolean required`

                  Whether this control requires a nonempty value.

                - `String type`

                  The rendering type, such as email, password, or text.

              - `List<Option> options`

                Sign-in methods. Empty for a plain form.

                - `String id`

                  The option ID to submit as selected_option.

                - `List<String> fieldIds`

                  IDs from the registered fields that this method accepts.

                - `String label`

                  The method label to display.

              - `Optional<String> reason`

                Why the agent needs the user to sign in.

              - `JsonValue; type "browser_authentication"constant`

                The type of the object. Always `browser_authentication`.

                - `BROWSER_AUTHENTICATION("browser_authentication")`

            - `class BrowserOriginAccess:`

              A browser origin awaiting the application's approval decision.

              - `String origin`

                The origin the browser needs permission to access.

              - `Optional<String> reason`

                The browser's explanation for this request, or null when unavailable.

              - `JsonValue; type "browser_origin_access"constant`

                The type of the object. Always `browser_origin_access`.

                - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

          - `String requestId`

            The registered request ID to echo when responding.

          - `String turnId`

            The turn that requested approval.

          - `JsonValue; type "computer_use_approval_request"constant`

            The type of the object. Always `computer_use_approval_request`.

            - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

        - `class FunctionCall:`

          Run a function tool and submit its result.

          - `JsonValue arguments`

            The arguments supplied by the model.

          - `String callId`

            The ID to include when submitting the function result.

          - `String name`

            The function name.

          - `String turnId`

            The ID of the turn that requested the function call.

          - `JsonValue; type "function_call"constant`

            The type of the object. Always `function_call`.

            - `FUNCTION_CALL("function_call")`

        - `class EnvironmentConnection:`

          Reconnect a session environment.

          - `String environmentId`

            The ID of the environment to reconnect.

          - `JsonValue; type "environment_connection"constant`

            The type of the object. Always `environment_connection`.

            - `ENVIRONMENT_CONNECTION("environment_connection")`

      - `Status status`

        The current status of the session.

        - `IDLE("idle")`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `IN_PROGRESS("in_progress")`

          The session is processing a turn.

        - `REQUIRES_ACTION("requires_action")`

          The session is waiting for one or more required actions.

        - `FAILED("failed")`

          The session failed.

      - `Optional<TokenUsage> usage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `long inputTokens`

          The number of input tokens used by the agent.

        - `InputTokensDetails inputTokensDetails`

          A breakdown of the agent's input token usage.

          - `long cachedTokens`

            The number of input tokens retrieved from the prompt cache.

        - `long outputTokens`

          The number of output tokens generated by the agent.

        - `OutputTokensDetails outputTokensDetails`

          A breakdown of the agent's output token usage.

          - `long reasoningTokens`

            The number of output tokens used for reasoning.

        - `long totalTokens`

          The total number of input and output tokens used by the agent.

      - `List<String> vaultIds`

        The IDs of vaults made available to the session.

    - `JsonValue; type "agent.session.created"constant`

      The type of the object. Always `agent.session.created`.

      - `AGENT_SESSION_CREATED("agent.session.created")`

  - `class AgentSessionTurnCreatedEvent:`

    Emitted when a turn is created.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The turn at the time it was created.

      - `String id`

        The ID of the turn.

      - `String agentId`

        The ID of the agent that ran the turn.

      - `Optional<Long> completedAt`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `long createdAt`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `Optional<SessionTurnError> error`

        A customer-safe error. Non-null only for a failed turn.

        - `Code code`

          A stable, machine-readable failure category.

          - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

            The request exceeds the model's context window.

          - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

            The session has reached its usage budget.

          - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

            The organization has reached a usage, plan, or billing limit.

          - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

            The organization has no API credits remaining.

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

            The request exceeds the available rate limit.

          - `FLEX_UNAVAILABLE("flex_unavailable")`

            Flex processing is temporarily unavailable.

          - `SERVER_OVERLOADED("server_overloaded")`

            The model service is temporarily overloaded.

          - `CYBER_POLICY("cyber_policy")`

            The request was rejected by a safety policy.

          - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

            The request was blocked by the safety systems.

          - `CONNECTION_FAILED("connection_failed")`

            The request could not connect to the model service.

          - `SERVER_ERROR("server_error")`

            The model service encountered an unexpected error.

          - `AUTHENTICATION_ERROR("authentication_error")`

            The API credentials are invalid or lack the required access.

          - `INVALID_REQUEST("invalid_request")`

            The request contains invalid input or configuration.

          - `RESOURCE_NOT_FOUND("resource_not_found")`

            The requested model or resource is unavailable.

          - `SANDBOX_ERROR("sandbox_error")`

            The request could not complete in its execution environment.

          - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

            The executor must be upgraded before it can run this turn.

          - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

            The session cannot accept additional input while a request is running.

          - `REQUEST_TIMEOUT("request_timeout")`

            The request timed out before the model service responded.

          - `INTERNAL_ERROR("internal_error")`

            An unexpected internal error prevented the session request from completing.

        - `String message`

          A customer-safe explanation of the failure.

      - `Object object_`

        The object type. Always `agent.session.turn`.

        - `AGENT_SESSION_TURN("agent.session.turn")`

      - `String sessionId`

        The ID of the session that owns the turn.

      - `Optional<Long> startedAt`

        The Unix timestamp, in seconds, when the turn started.

      - `Status status`

        The current status of the turn.

        - `QUEUED("queued")`

          The turn is waiting to start.

        - `IN_PROGRESS("in_progress")`

          The turn is in progress.

        - `WAITING("waiting")`

          The turn is waiting for external input.

        - `COMPLETED("completed")`

          The turn completed successfully.

        - `FAILED("failed")`

          The turn failed.

        - `CANCELLED("cancelled")`

          The turn was cancelled.

      - `Optional<String> subagentId`

        The ID of the subagent that ran the turn, if applicable.

      - `Optional<TokenUsage> usage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.created"constant`

      The type of the object. Always `agent.session.turn.created`.

      - `AGENT_SESSION_TURN_CREATED("agent.session.turn.created")`

  - `class AgentSessionTurnInProgressEvent:`

    Emitted when a turn starts running.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The turn at the time it started running.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.in_progress"constant`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `AGENT_SESSION_TURN_IN_PROGRESS("agent.session.turn.in_progress")`

  - `class AgentSessionTurnCompletedEvent:`

    Emitted when a turn completes.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The completed turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.completed"constant`

      The type of the object. Always `agent.session.turn.completed`.

      - `AGENT_SESSION_TURN_COMPLETED("agent.session.turn.completed")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent:`

    Emitted when a turn fails.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The failed turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.failed"constant`

      The type of the object. Always `agent.session.turn.failed`.

      - `AGENT_SESSION_TURN_FAILED("agent.session.turn.failed")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent:`

    Emitted when a turn is cancelled.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The cancelled turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.cancelled"constant`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `AGENT_SESSION_TURN_CANCELLED("agent.session.turn.cancelled")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent:`

    Emitted when an item is added to a turn.

    - `String eventId`

      The unique ID of the event.

    - `AgentSessionItem item`

      The item that was added.

      - `class AgentSessionMessage:`

        A user or assistant message recorded in a session.

        - `Optional<String> id`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `List<AgentSessionMessageContent> content`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `InputText`

            - `String text`

              The text supplied by the user.

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

          - `OutputText`

            - `String text`

              The text produced by the assistant.

            - `JsonValue; type "output_text"constant`

              The type of the object. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `Optional<Phase> phase`

          The phase of an assistant message. Null for user messages.

          - `COMMENTARY("commentary")`

            Commentary produced while the agent works.

          - `FINAL_ANSWER("final_answer")`

            The agent's final answer.

        - `Role role`

          The role of the message author.

          - `USER("user")`

          - `ASSISTANT("assistant")`

        - `AgentOutputItemStatus status`

          The status of the message. User messages are always `completed`.

          - `IN_PROGRESS("in_progress")`

            The item is in progress.

          - `COMPLETED("completed")`

            The item is complete.

          - `INCOMPLETE("incomplete")`

            The item stopped before completing.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "message"constant`

          The item type. Always `message`.

          - `MESSAGE("message")`

      - `class AgentReasoningItem:`

        A reasoning item produced by the agent.

        - `String id`

          The ID of the reasoning item.

        - `Optional<AgentOutputItemStatus> status`

          The status of the reasoning item.

        - `List<SummaryText> summary`

          The reasoning summaries produced by the agent.

          - `String text`

            The reasoning summary text.

          - `JsonValue; type "summary_text"constant`

            The content type. Always `summary_text`.

            - `SUMMARY_TEXT("summary_text")`

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "reasoning"constant`

          The item type. Always `reasoning`.

          - `REASONING("reasoning")`

      - `class AgentFunctionCallItem:`

        A function call produced by the agent.

        - `String id`

          The ID of the function call item.

        - `JsonValue arguments`

          The arguments to pass to the function.

        - `String callId`

          The ID used to submit the function result.

        - `String name`

          The name of the function to call.

        - `AgentFunctionCallStatus status`

          The status of the function call.

          - `IN_PROGRESS("in_progress")`

            The call is in progress.

          - `COMPLETED("completed")`

            The call completed successfully.

          - `FAILED("failed")`

            The call failed.

          - `INCOMPLETE("incomplete")`

            The call stopped before completing.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "function_call"constant`

          The item type. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `FunctionCallOutput`

        - `String id`

          The ID of the function call output item.

        - `String callId`

          The ID of the function call that produced this output.

        - `Optional<String> error`

          The error message, if the call failed.

        - `Optional<AgentFunctionCallOutput> output`

          The function result, if the call succeeded.

          - `String`

          - `List<InputContent>`

            - `InputText`

              - `String text`

                The text supplied to the agent.

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

        - `AgentFunctionCallStatus status`

          The status of the function call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "function_call_output"constant`

          The item type. Always `function_call_output`.

          - `FUNCTION_CALL_OUTPUT("function_call_output")`

      - `AgentMessage`

        - `String id`

          The ID of the message.

        - `List<AgentContent> content`

          The content exchanged between the agents.

          - `class OutputText:`

            A text content part produced by the agent.

            - `String text`

              The text produced by the agent.

            - `JsonValue; type "output_text"constant`

              The content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `EncryptedContent`

            - `String encryptedContent`

              The encrypted content payload.

            - `JsonValue; type "encrypted_content"constant`

              The content type. Always `encrypted_content`.

              - `ENCRYPTED_CONTENT("encrypted_content")`

        - `String recipientAgentId`

          The ID or name of the receiving agent.

        - `String senderAgentId`

          The ID or name of the sending agent.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "agent_message"constant`

          The item type. Always `agent_message`.

          - `AGENT_MESSAGE("agent_message")`

      - `class AgentMcpCallItem:`

        A call to a tool on an MCP server.

        - `String id`

          The ID of the MCP call item.

        - `JsonValue arguments`

          The arguments passed to the MCP tool.

        - `JsonValue error`

          The error returned by the MCP tool, if any.

        - `String name`

          The name of the MCP tool.

        - `JsonValue output`

          The output returned by the MCP tool, if any.

        - `String serverLabel`

          The label of the MCP server.

        - `AgentFunctionCallStatus status`

          The status of the MCP tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "mcp_call"constant`

          The item type. Always `mcp_call`.

          - `MCP_CALL("mcp_call")`

      - `ComputerUseCall`

        - `String id`

          The ID of the activity item.

        - `Optional<Output> output`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `String imageUrl`

            The complete JPEG image as a base64 data URL.

          - `JsonValue; type "computer_screenshot"constant`

            The content type. Always `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

        - `AgentFunctionCallStatus status`

          The execution status of the activity.

        - `Optional<String> title`

          A model-generated description of the activity, when available.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_call"constant`

          The item type. Always `computer_use_call`.

          - `COMPUTER_USE_CALL("computer_use_call")`

      - `ComputerUseApprovalRequest`

        - `String id`

          The stable history item ID.

        - `Request request`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String requestId`

        - `String turnId`

        - `JsonValue; type "computer_use_approval_request"constant`

          The item type. Always computer_use_approval_request.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `ComputerUseApprovalRequestResult`

        - `String id`

          The stable history item ID.

        - `String requestId`

          The registered request answered by this item.

        - `Response response`

          The admitted response, without submitted credential values.

          - `class Submit:`

            - `JsonValue; action "submit"constant`

              - `SUBMIT("submit")`

            - `Optional<String> selectedOption`

              The chosen sign-in method, or null when no options were offered.

            - `JsonValue; type "browser_authentication"constant`

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `JsonValue;`

            - `JsonValue; action "cancel"constant`

              - `CANCEL("cancel")`

            - `JsonValue; type "browser_authentication"constant`

              - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_approval_request_result"constant`

          - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

      - `class AgentWebSearchCallItem:`

        A web search call produced by the agent.

        - `String id`

          The ID of the web search call.

        - `Optional<WebSearchAction> action`

          The action performed by the web search tool.

          - `Search`

            - `Optional<List<String>> queries`

              The search queries, when multiple queries were used.

            - `Optional<String> query`

              The search query, when a single query was used.

            - `JsonValue; type "search"constant`

              The type of the object. Always `search`.

              - `SEARCH("search")`

          - `OpenPage`

            - `JsonValue; type "open_page"constant`

              The type of the object. Always `open_page`.

              - `OPEN_PAGE("open_page")`

            - `Optional<String> url`

              The URL of the page that was opened.

          - `FindInPage`

            - `Optional<String> pattern`

              The text pattern that was searched for.

            - `JsonValue; type "find_in_page"constant`

              The type of the object. Always `find_in_page`.

              - `FIND_IN_PAGE("find_in_page")`

            - `Optional<String> url`

              The URL of the page that was searched.

          - `JsonValue;`

            - `JsonValue; type "other"constant`

              The type of the object. Always `other`.

              - `OTHER("other")`

        - `AgentOutputItemStatus status`

          The status of the web search call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "web_search_call"constant`

          The item type. Always `web_search_call`.

          - `WEB_SEARCH_CALL("web_search_call")`

      - `class AgentCommandExecutionItem:`

        A command execution produced by the agent.

        - `String id`

          The ID of the command execution item.

        - `String command`

          The command that was executed.

        - `Optional<String> cwd`

          The working directory used to execute the command.

        - `Optional<Long> durationMs`

          The command duration in milliseconds.

        - `Optional<Long> exitCode`

          The process exit code, if the command completed.

        - `Optional<String> output`

          The command output, if available.

        - `AgentFunctionCallStatus status`

          The status of the command execution.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "command_execution"constant`

          The item type. Always `command_execution`.

          - `COMMAND_EXECUTION("command_execution")`

      - `class AgentCreateSubagentCallItem:`

        A request to spawn a subagent.

        - `String id`

          The ID of the tool call item.

        - `String agentId`

          The ID of the agent that requested the subagent.

        - `List<AgentContent> content`

          The task given to the spawned agent.

          - `class OutputText:`

            A text content part produced by the agent.

          - `EncryptedContent`

        - `Optional<String> model`

          The model requested for the spawned agent.

        - `Optional<String> reasoningEffort`

          The reasoning effort requested for the spawned agent.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "create_subagent_call"constant`

          The item type. Always `create_subagent_call`.

          - `CREATE_SUBAGENT_CALL("create_subagent_call")`

            The current public item type.

      - `class AgentSendSubagentInputCallItem:`

        A request to send input to another agent.

        - `String id`

          The ID of the tool call item.

        - `List<AgentContent> content`

          The input sent to the receiving agent.

          - `class OutputText:`

            A text content part produced by the agent.

          - `EncryptedContent`

        - `String recipientAgentId`

          The ID of the agent receiving the input.

        - `String senderAgentId`

          The ID of the agent sending the input.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "send_subagent_input_call"constant`

          The item type. Always `send_subagent_input_call`.

          - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

            The current public item type.

      - `class AgentResumeSubagentCallItem:`

        A request to resume a subagent.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to resume.

        - `String senderAgentId`

          The ID of the agent requesting the resume.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "resume_subagent_call"constant`

          The item type. Always `resume_subagent_call`.

          - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem:`

        A request to wait for one or more subagents.

        - `String id`

          The ID of the tool call item.

        - `List<String> recipientAgentIds`

          The IDs of the agents to wait for.

        - `String senderAgentId`

          The ID of the agent waiting for results.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "wait_for_subagents_call"constant`

          The item type. Always `wait_for_subagents_call`.

          - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

            The current public item type.

      - `class AgentInterruptSubagentCallItem:`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to interrupt.

        - `String senderAgentId`

          The ID of the agent requesting the interrupt.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "interrupt_subagent_call"constant`

          The item type. Always `interrupt_subagent_call`.

          - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

            The current public item type.

      - `class AgentCloseSubagentCallItem:`

        A request to close a subagent.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to close.

        - `String senderAgentId`

          The ID of the agent requesting the close.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "close_subagent_call"constant`

          The item type. Always `close_subagent_call`.

          - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

            The current public item type.

    - `Optional<Long> outputIndex`

      The index of the item in the turn output, when the item is agent output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.item.added"constant`

      The type of the object. Always `agent.session.turn.item.added`.

      - `AGENT_SESSION_TURN_ITEM_ADDED("agent.session.turn.item.added")`

  - `class AgentSessionIdleEvent:`

    Emitted when a session becomes idle.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that became idle.

    - `JsonValue; type "agent.session.idle"constant`

      The type of the object. Always `agent.session.idle`.

      - `AGENT_SESSION_IDLE("agent.session.idle")`

  - `class AgentSessionInProgressEvent:`

    Emitted when a session starts processing a turn.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that started processing.

    - `JsonValue; type "agent.session.in_progress"constant`

      The type of the object. Always `agent.session.in_progress`.

      - `AGENT_SESSION_IN_PROGRESS("agent.session.in_progress")`

  - `class AgentSessionRequiresActionEvent:`

    Emitted when a session is waiting for one or more required actions.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session and its current required actions.

    - `JsonValue; type "agent.session.requires_action"constant`

      The type of the object. Always `agent.session.requires_action`.

      - `AGENT_SESSION_REQUIRES_ACTION("agent.session.requires_action")`

  - `class AgentSessionFailedEvent:`

    Emitted when a session fails.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The failed session.

    - `JsonValue; type "agent.session.failed"constant`

      The type of the object. Always `agent.session.failed`.

      - `AGENT_SESSION_FAILED("agent.session.failed")`

  - `class AgentSessionEnvironmentPendingEvent:`

    Emitted while a session environment is being prepared.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.pending"constant`

      The type of the object. Always `agent.session.environment.pending`.

      - `AGENT_SESSION_ENVIRONMENT_PENDING("agent.session.environment.pending")`

  - `class AgentSessionEnvironmentConnectedEvent:`

    Emitted when a session environment connects.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.connected"constant`

      The type of the object. Always `agent.session.environment.connected`.

      - `AGENT_SESSION_ENVIRONMENT_CONNECTED("agent.session.environment.connected")`

  - `class AgentSessionEnvironmentDisconnectedEvent:`

    Emitted when a session environment disconnects.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.disconnected"constant`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `AGENT_SESSION_ENVIRONMENT_DISCONNECTED("agent.session.environment.disconnected")`

  - `class AgentSessionEnvironmentFailedEvent:`

    Emitted when a session environment fails.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.failed"constant`

      The type of the object. Always `agent.session.environment.failed`.

      - `AGENT_SESSION_ENVIRONMENT_FAILED("agent.session.environment.failed")`

  - `class AgentSessionSubagentCreatedEvent:`

    Emitted when a subagent is created.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that was created.

      - `String id`

        The ID of the subagent.

      - `Optional<Long> closedAt`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `Optional<List<AgentContent>> instructions`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText:`

          A text content part produced by the agent.

        - `EncryptedContent`

      - `Optional<String> name`

        The runner-assigned nickname, or null when unavailable.

      - `Object object_`

        The object type. Always `agent.session.subagent`.

        - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

      - `long openedAt`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `String parentAgentId`

        The ID of the agent that created this subagent.

      - `String sessionId`

        The ID of the session that owns the subagent.

      - `Status status`

        The current status of the subagent.

        - `ACTIVE("active")`

          The subagent remains available, including while idle between turns.

        - `CLOSED("closed")`

          The subagent is closed.

    - `JsonValue; type "agent.session.subagent.created"constant`

      The type of the object. Always `agent.session.subagent.created`.

      - `AGENT_SESSION_SUBAGENT_CREATED("agent.session.subagent.created")`

  - `class AgentSessionSubagentActiveEvent:`

    Emitted when a closed subagent successfully resumes.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that resumed.

    - `JsonValue; type "agent.session.subagent.active"constant`

      The type of the object. Always `agent.session.subagent.active`.

      - `AGENT_SESSION_SUBAGENT_ACTIVE("agent.session.subagent.active")`

  - `class AgentSessionSubagentClosedEvent:`

    Emitted when a subagent is closed.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that was closed.

    - `JsonValue; type "agent.session.subagent.closed"constant`

      The type of the object. Always `agent.session.subagent.closed`.

      - `AGENT_SESSION_SUBAGENT_CLOSED("agent.session.subagent.closed")`

  - `class AgentSessionTurnItemDoneEvent:`

    Emitted when an output item is complete.

    - `String eventId`

      The unique ID of the event.

    - `AgentOutputItem item`

      The completed output item.

      - `class AgentSessionAssistantMessage:`

        An assistant message produced by the agent.

        - `String id`

          The ID of the message.

        - `List<OutputText> content`

          The content of the message.

          - `String text`

            The text produced by the agent.

          - `JsonValue; type "output_text"constant`

            The content type. Always `output_text`.

        - `Optional<Phase> phase`

          The phase of the assistant message.

          - `COMMENTARY("commentary")`

            Commentary produced while the agent works.

          - `FINAL_ANSWER("final_answer")`

            The agent's final answer.

        - `JsonValue; role "assistant"constant`

          The role of the message author. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `AgentOutputItemStatus status`

          The status of the message.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "message"constant`

          The item type. Always `message`.

          - `MESSAGE("message")`

      - `class AgentReasoningItem:`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem:`

        A function call produced by the agent.

      - `class AgentMcpCallItem:`

        A call to a tool on an MCP server.

      - `ComputerUseCall`

        - `String id`

          The ID of the activity item.

        - `Optional<Output> output`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `String imageUrl`

            The complete JPEG image as a base64 data URL.

          - `JsonValue; type "computer_screenshot"constant`

            The content type. Always `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

        - `AgentFunctionCallStatus status`

          The execution status of the activity.

        - `Optional<String> title`

          A model-generated description of the activity, when available.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_call"constant`

          The item type. Always `computer_use_call`.

          - `COMPUTER_USE_CALL("computer_use_call")`

      - `ComputerUseApprovalRequest`

        - `String id`

          The stable history item ID.

        - `Request request`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String requestId`

        - `String turnId`

        - `JsonValue; type "computer_use_approval_request"constant`

          The item type. Always computer_use_approval_request.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class AgentWebSearchCallItem:`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem:`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem:`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem:`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem:`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem:`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem:`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem:`

        A request to close a subagent.

    - `long outputIndex`

      The index of the output item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.item.done"constant`

      The type of the object. Always `agent.session.turn.item.done`.

      - `AGENT_SESSION_TURN_ITEM_DONE("agent.session.turn.item.done")`

  - `class AgentSessionTurnContentPartAddedEvent:`

    Emitted when an output text content part is added.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `OutputText part`

      The initial content part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.content_part.added"constant`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `AGENT_SESSION_TURN_CONTENT_PART_ADDED("agent.session.turn.content_part.added")`

  - `class AgentSessionTurnContentPartDoneEvent:`

    Emitted when an output content part is complete.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `OutputText part`

      The completed content part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.content_part.done"constant`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `AGENT_SESSION_TURN_CONTENT_PART_DONE("agent.session.turn.content_part.done")`

  - `class AgentSessionTurnOutputTextDeltaEvent:`

    Emitted when text is appended to an output text content part.

    - `long contentIndex`

      The index of the content part in the message.

    - `String delta`

      The text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.output_text.delta"constant`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `AGENT_SESSION_TURN_OUTPUT_TEXT_DELTA("agent.session.turn.output_text.delta")`

  - `class AgentSessionTurnOutputTextDoneEvent:`

    Emitted when an output text content part is complete.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `String text`

      The complete output text.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.output_text.done"constant`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `AGENT_SESSION_TURN_OUTPUT_TEXT_DONE("agent.session.turn.output_text.done")`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent:`

    Emitted when a reasoning summary content part is added.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `SummaryText part`

      The initial summary part.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_part.added"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_ADDED("agent.session.turn.reasoning_summary_part.added")`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent:`

    Emitted when a reasoning summary part is complete.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `SummaryText part`

      The completed summary part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<Status> status`

      Present as `incomplete` when summary generation was interrupted.

      - `INCOMPLETE("incomplete")`

    - `long summaryIndex`

      The index of the summary part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_part.done"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_DONE("agent.session.turn.reasoning_summary_part.done")`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent:`

    Emitted when text is appended to a reasoning summary.

    - `String delta`

      The summary text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_text.delta"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DELTA("agent.session.turn.reasoning_summary_text.delta")`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent:`

    Emitted when a reasoning summary content part is complete.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `String text`

      The complete reasoning summary text.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_text.done"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DONE("agent.session.turn.reasoning_summary_text.done")`

### Agent Session Failed Event

- `class AgentSessionFailedEvent:`

  Emitted when a session fails.

  - `String eventId`

    The unique ID of the event.

  - `AgentSession session`

    The failed session.

    - `String id`

      The ID of the session.

    - `Agent agent`

      The agent running in the session.

      - `String id`

        The ID of the agent.

      - `Optional<String> instructions`

        Custom instructions appended to the agent's default base instructions.

      - `String model`

        The model used by the agent.

      - `MultiAgentConfig multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Optional<String> name`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `AgentReasoning reasoning`

        The agent's reasoning configuration.

        - `Optional<Effort> effort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<Summary> summary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `CONCISE("concise")`

            Returns a concise reasoning summary when supported.

          - `DETAILED("detailed")`

            Returns a detailed reasoning summary when supported.

          - `AUTO("auto")`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier serviceTier`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        Configuration for text generated by the agent.

        - `TextFormat format`

          The effective output format. Defaults to ordinary text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              The type of the object. Always `text`.

              - `TEXT("text")`

          - `JsonSchema`

            - `Schema schema`

              The JSON Schema that generated text must match.

            - `JsonValue; type "json_schema"constant`

              The type of the object. Always `json_schema`.

              - `JSON_SCHEMA("json_schema")`

        - `Verbosity verbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `List<AgentTool> tools`

        Tools available to the agent.

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

          - `String name`

            The name of the function.

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

              - `String command`

                The command used to start the MCP server.

              - `String cwd`

                The working directory used to start the MCP server.

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

            - `Optional<String> region`

              The region or state name.

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode mode`

            The source used for web search results.

            - `DISABLED("disabled")`

            - `CACHED("cached")`

            - `LIVE("live")`

          - `JsonValue; type "web_search"constant`

            The type of the object. Always `web_search`.

            - `WEB_SEARCH("web_search")`

        - `ComputerUse`

          - `boolean includeScreenshots`

            Whether computer tool outputs include screenshots.

          - `JsonValue; type "computer_use"constant`

            The type of the object. Always `computer_use`.

            - `COMPUTER_USE("computer_use")`

    - `long createdAt`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment environment`

      The execution environment for the session.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `Desktop desktop`

          The effective desktop configuration.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `List<HostedEnvironmentFile> files`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileId:`

            A file copied from the OpenAI Files API.

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String fileId`

              The ID of the uploaded file.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Network network`

          The effective network access policy for the environment.

          - `Access access`

            The environment's network access mode.

            - `ENABLED("enabled")`

              Allows unrestricted network access.

            - `DISABLED("disabled")`

              Disables network access.

            - `RESTRICTED("restricted")`

              Applies the configured domain restrictions.

          - `List<String> allowedDomains`

            Domains the environment may access when network access is restricted.

        - `Packages packages`

          Packages installed in the environment.

          - `List<String> npm`

            npm packages installed globally in the environment.

          - `List<String> python`

            Python packages installed in the environment.

          - `List<String> system`

            System packages installed in the environment.

        - `List<HostedPlugin> plugins`

          Plugins installed in the environment, excluding their archive contents.

          - `String description`

            The installed plugin description.

          - `String name`

            The installed plugin name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `List<HostedSkill> skills`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference:`

            A skill installed from the Skills API.

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `String skillId`

              The referenced skill ID.

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `String version`

              The concrete skill version installed for this session.

          - `Inline`

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

        - `Optional<ContainerSize> containerSize`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

      - `SelfHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `String remoteUrl`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Optional<String> error`

      The error that caused the session to fail, if any.

    - `long lastActiveAt`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata metadata`

      Custom string key-value pairs attached to the session.

    - `JsonValue; object_ "agent.session"constant`

      The object type. Always `agent.session`.

      - `AGENT_SESSION("agent.session")`

    - `List<RequiredAction> requiredActions`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest:`

        Respond to a computer-use request.

        - `Request request`

          The information needed to render the request.

          - `class BrowserAuthentication:`

            A registered form awaiting the application's response.

            - `Optional<String> credentialOrigin`

              The registered form or frame origin where values will be entered.

            - `List<Field> fields`

              Controls to render. All submitted values are sensitive.

              - `String id`

                The field ID to submit as field_id in a fields entry.

              - `String label`

                The label to display beside the control.

              - `boolean required`

                Whether this control requires a nonempty value.

              - `String type`

                The rendering type, such as email, password, or text.

            - `List<Option> options`

              Sign-in methods. Empty for a plain form.

              - `String id`

                The option ID to submit as selected_option.

              - `List<String> fieldIds`

                IDs from the registered fields that this method accepts.

              - `String label`

                The method label to display.

            - `Optional<String> reason`

              Why the agent needs the user to sign in.

            - `JsonValue; type "browser_authentication"constant`

              The type of the object. Always `browser_authentication`.

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `class BrowserOriginAccess:`

            A browser origin awaiting the application's approval decision.

            - `String origin`

              The origin the browser needs permission to access.

            - `Optional<String> reason`

              The browser's explanation for this request, or null when unavailable.

            - `JsonValue; type "browser_origin_access"constant`

              The type of the object. Always `browser_origin_access`.

              - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

        - `String requestId`

          The registered request ID to echo when responding.

        - `String turnId`

          The turn that requested approval.

        - `JsonValue; type "computer_use_approval_request"constant`

          The type of the object. Always `computer_use_approval_request`.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class FunctionCall:`

        Run a function tool and submit its result.

        - `JsonValue arguments`

          The arguments supplied by the model.

        - `String callId`

          The ID to include when submitting the function result.

        - `String name`

          The function name.

        - `String turnId`

          The ID of the turn that requested the function call.

        - `JsonValue; type "function_call"constant`

          The type of the object. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `class EnvironmentConnection:`

        Reconnect a session environment.

        - `String environmentId`

          The ID of the environment to reconnect.

        - `JsonValue; type "environment_connection"constant`

          The type of the object. Always `environment_connection`.

          - `ENVIRONMENT_CONNECTION("environment_connection")`

    - `Status status`

      The current status of the session.

      - `IDLE("idle")`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `IN_PROGRESS("in_progress")`

        The session is processing a turn.

      - `REQUIRES_ACTION("requires_action")`

        The session is waiting for one or more required actions.

      - `FAILED("failed")`

        The session failed.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

    - `List<String> vaultIds`

      The IDs of vaults made available to the session.

  - `JsonValue; type "agent.session.failed"constant`

    The type of the object. Always `agent.session.failed`.

    - `AGENT_SESSION_FAILED("agent.session.failed")`

### Agent Session Idle Event

- `class AgentSessionIdleEvent:`

  Emitted when a session becomes idle.

  - `String eventId`

    The unique ID of the event.

  - `AgentSession session`

    The session that became idle.

    - `String id`

      The ID of the session.

    - `Agent agent`

      The agent running in the session.

      - `String id`

        The ID of the agent.

      - `Optional<String> instructions`

        Custom instructions appended to the agent's default base instructions.

      - `String model`

        The model used by the agent.

      - `MultiAgentConfig multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Optional<String> name`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `AgentReasoning reasoning`

        The agent's reasoning configuration.

        - `Optional<Effort> effort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<Summary> summary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `CONCISE("concise")`

            Returns a concise reasoning summary when supported.

          - `DETAILED("detailed")`

            Returns a detailed reasoning summary when supported.

          - `AUTO("auto")`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier serviceTier`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        Configuration for text generated by the agent.

        - `TextFormat format`

          The effective output format. Defaults to ordinary text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              The type of the object. Always `text`.

              - `TEXT("text")`

          - `JsonSchema`

            - `Schema schema`

              The JSON Schema that generated text must match.

            - `JsonValue; type "json_schema"constant`

              The type of the object. Always `json_schema`.

              - `JSON_SCHEMA("json_schema")`

        - `Verbosity verbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `List<AgentTool> tools`

        Tools available to the agent.

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

          - `String name`

            The name of the function.

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

              - `String command`

                The command used to start the MCP server.

              - `String cwd`

                The working directory used to start the MCP server.

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

            - `Optional<String> region`

              The region or state name.

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode mode`

            The source used for web search results.

            - `DISABLED("disabled")`

            - `CACHED("cached")`

            - `LIVE("live")`

          - `JsonValue; type "web_search"constant`

            The type of the object. Always `web_search`.

            - `WEB_SEARCH("web_search")`

        - `ComputerUse`

          - `boolean includeScreenshots`

            Whether computer tool outputs include screenshots.

          - `JsonValue; type "computer_use"constant`

            The type of the object. Always `computer_use`.

            - `COMPUTER_USE("computer_use")`

    - `long createdAt`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment environment`

      The execution environment for the session.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `Desktop desktop`

          The effective desktop configuration.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `List<HostedEnvironmentFile> files`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileId:`

            A file copied from the OpenAI Files API.

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String fileId`

              The ID of the uploaded file.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Network network`

          The effective network access policy for the environment.

          - `Access access`

            The environment's network access mode.

            - `ENABLED("enabled")`

              Allows unrestricted network access.

            - `DISABLED("disabled")`

              Disables network access.

            - `RESTRICTED("restricted")`

              Applies the configured domain restrictions.

          - `List<String> allowedDomains`

            Domains the environment may access when network access is restricted.

        - `Packages packages`

          Packages installed in the environment.

          - `List<String> npm`

            npm packages installed globally in the environment.

          - `List<String> python`

            Python packages installed in the environment.

          - `List<String> system`

            System packages installed in the environment.

        - `List<HostedPlugin> plugins`

          Plugins installed in the environment, excluding their archive contents.

          - `String description`

            The installed plugin description.

          - `String name`

            The installed plugin name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `List<HostedSkill> skills`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference:`

            A skill installed from the Skills API.

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `String skillId`

              The referenced skill ID.

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `String version`

              The concrete skill version installed for this session.

          - `Inline`

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

        - `Optional<ContainerSize> containerSize`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

      - `SelfHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `String remoteUrl`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Optional<String> error`

      The error that caused the session to fail, if any.

    - `long lastActiveAt`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata metadata`

      Custom string key-value pairs attached to the session.

    - `JsonValue; object_ "agent.session"constant`

      The object type. Always `agent.session`.

      - `AGENT_SESSION("agent.session")`

    - `List<RequiredAction> requiredActions`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest:`

        Respond to a computer-use request.

        - `Request request`

          The information needed to render the request.

          - `class BrowserAuthentication:`

            A registered form awaiting the application's response.

            - `Optional<String> credentialOrigin`

              The registered form or frame origin where values will be entered.

            - `List<Field> fields`

              Controls to render. All submitted values are sensitive.

              - `String id`

                The field ID to submit as field_id in a fields entry.

              - `String label`

                The label to display beside the control.

              - `boolean required`

                Whether this control requires a nonempty value.

              - `String type`

                The rendering type, such as email, password, or text.

            - `List<Option> options`

              Sign-in methods. Empty for a plain form.

              - `String id`

                The option ID to submit as selected_option.

              - `List<String> fieldIds`

                IDs from the registered fields that this method accepts.

              - `String label`

                The method label to display.

            - `Optional<String> reason`

              Why the agent needs the user to sign in.

            - `JsonValue; type "browser_authentication"constant`

              The type of the object. Always `browser_authentication`.

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `class BrowserOriginAccess:`

            A browser origin awaiting the application's approval decision.

            - `String origin`

              The origin the browser needs permission to access.

            - `Optional<String> reason`

              The browser's explanation for this request, or null when unavailable.

            - `JsonValue; type "browser_origin_access"constant`

              The type of the object. Always `browser_origin_access`.

              - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

        - `String requestId`

          The registered request ID to echo when responding.

        - `String turnId`

          The turn that requested approval.

        - `JsonValue; type "computer_use_approval_request"constant`

          The type of the object. Always `computer_use_approval_request`.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class FunctionCall:`

        Run a function tool and submit its result.

        - `JsonValue arguments`

          The arguments supplied by the model.

        - `String callId`

          The ID to include when submitting the function result.

        - `String name`

          The function name.

        - `String turnId`

          The ID of the turn that requested the function call.

        - `JsonValue; type "function_call"constant`

          The type of the object. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `class EnvironmentConnection:`

        Reconnect a session environment.

        - `String environmentId`

          The ID of the environment to reconnect.

        - `JsonValue; type "environment_connection"constant`

          The type of the object. Always `environment_connection`.

          - `ENVIRONMENT_CONNECTION("environment_connection")`

    - `Status status`

      The current status of the session.

      - `IDLE("idle")`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `IN_PROGRESS("in_progress")`

        The session is processing a turn.

      - `REQUIRES_ACTION("requires_action")`

        The session is waiting for one or more required actions.

      - `FAILED("failed")`

        The session failed.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

    - `List<String> vaultIds`

      The IDs of vaults made available to the session.

  - `JsonValue; type "agent.session.idle"constant`

    The type of the object. Always `agent.session.idle`.

    - `AGENT_SESSION_IDLE("agent.session.idle")`

### Agent Session In Progress Event

- `class AgentSessionInProgressEvent:`

  Emitted when a session starts processing a turn.

  - `String eventId`

    The unique ID of the event.

  - `AgentSession session`

    The session that started processing.

    - `String id`

      The ID of the session.

    - `Agent agent`

      The agent running in the session.

      - `String id`

        The ID of the agent.

      - `Optional<String> instructions`

        Custom instructions appended to the agent's default base instructions.

      - `String model`

        The model used by the agent.

      - `MultiAgentConfig multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Optional<String> name`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `AgentReasoning reasoning`

        The agent's reasoning configuration.

        - `Optional<Effort> effort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<Summary> summary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `CONCISE("concise")`

            Returns a concise reasoning summary when supported.

          - `DETAILED("detailed")`

            Returns a detailed reasoning summary when supported.

          - `AUTO("auto")`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier serviceTier`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        Configuration for text generated by the agent.

        - `TextFormat format`

          The effective output format. Defaults to ordinary text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              The type of the object. Always `text`.

              - `TEXT("text")`

          - `JsonSchema`

            - `Schema schema`

              The JSON Schema that generated text must match.

            - `JsonValue; type "json_schema"constant`

              The type of the object. Always `json_schema`.

              - `JSON_SCHEMA("json_schema")`

        - `Verbosity verbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `List<AgentTool> tools`

        Tools available to the agent.

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

          - `String name`

            The name of the function.

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

              - `String command`

                The command used to start the MCP server.

              - `String cwd`

                The working directory used to start the MCP server.

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

            - `Optional<String> region`

              The region or state name.

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode mode`

            The source used for web search results.

            - `DISABLED("disabled")`

            - `CACHED("cached")`

            - `LIVE("live")`

          - `JsonValue; type "web_search"constant`

            The type of the object. Always `web_search`.

            - `WEB_SEARCH("web_search")`

        - `ComputerUse`

          - `boolean includeScreenshots`

            Whether computer tool outputs include screenshots.

          - `JsonValue; type "computer_use"constant`

            The type of the object. Always `computer_use`.

            - `COMPUTER_USE("computer_use")`

    - `long createdAt`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment environment`

      The execution environment for the session.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `Desktop desktop`

          The effective desktop configuration.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `List<HostedEnvironmentFile> files`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileId:`

            A file copied from the OpenAI Files API.

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String fileId`

              The ID of the uploaded file.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Network network`

          The effective network access policy for the environment.

          - `Access access`

            The environment's network access mode.

            - `ENABLED("enabled")`

              Allows unrestricted network access.

            - `DISABLED("disabled")`

              Disables network access.

            - `RESTRICTED("restricted")`

              Applies the configured domain restrictions.

          - `List<String> allowedDomains`

            Domains the environment may access when network access is restricted.

        - `Packages packages`

          Packages installed in the environment.

          - `List<String> npm`

            npm packages installed globally in the environment.

          - `List<String> python`

            Python packages installed in the environment.

          - `List<String> system`

            System packages installed in the environment.

        - `List<HostedPlugin> plugins`

          Plugins installed in the environment, excluding their archive contents.

          - `String description`

            The installed plugin description.

          - `String name`

            The installed plugin name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `List<HostedSkill> skills`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference:`

            A skill installed from the Skills API.

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `String skillId`

              The referenced skill ID.

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `String version`

              The concrete skill version installed for this session.

          - `Inline`

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

        - `Optional<ContainerSize> containerSize`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

      - `SelfHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `String remoteUrl`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Optional<String> error`

      The error that caused the session to fail, if any.

    - `long lastActiveAt`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata metadata`

      Custom string key-value pairs attached to the session.

    - `JsonValue; object_ "agent.session"constant`

      The object type. Always `agent.session`.

      - `AGENT_SESSION("agent.session")`

    - `List<RequiredAction> requiredActions`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest:`

        Respond to a computer-use request.

        - `Request request`

          The information needed to render the request.

          - `class BrowserAuthentication:`

            A registered form awaiting the application's response.

            - `Optional<String> credentialOrigin`

              The registered form or frame origin where values will be entered.

            - `List<Field> fields`

              Controls to render. All submitted values are sensitive.

              - `String id`

                The field ID to submit as field_id in a fields entry.

              - `String label`

                The label to display beside the control.

              - `boolean required`

                Whether this control requires a nonempty value.

              - `String type`

                The rendering type, such as email, password, or text.

            - `List<Option> options`

              Sign-in methods. Empty for a plain form.

              - `String id`

                The option ID to submit as selected_option.

              - `List<String> fieldIds`

                IDs from the registered fields that this method accepts.

              - `String label`

                The method label to display.

            - `Optional<String> reason`

              Why the agent needs the user to sign in.

            - `JsonValue; type "browser_authentication"constant`

              The type of the object. Always `browser_authentication`.

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `class BrowserOriginAccess:`

            A browser origin awaiting the application's approval decision.

            - `String origin`

              The origin the browser needs permission to access.

            - `Optional<String> reason`

              The browser's explanation for this request, or null when unavailable.

            - `JsonValue; type "browser_origin_access"constant`

              The type of the object. Always `browser_origin_access`.

              - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

        - `String requestId`

          The registered request ID to echo when responding.

        - `String turnId`

          The turn that requested approval.

        - `JsonValue; type "computer_use_approval_request"constant`

          The type of the object. Always `computer_use_approval_request`.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class FunctionCall:`

        Run a function tool and submit its result.

        - `JsonValue arguments`

          The arguments supplied by the model.

        - `String callId`

          The ID to include when submitting the function result.

        - `String name`

          The function name.

        - `String turnId`

          The ID of the turn that requested the function call.

        - `JsonValue; type "function_call"constant`

          The type of the object. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `class EnvironmentConnection:`

        Reconnect a session environment.

        - `String environmentId`

          The ID of the environment to reconnect.

        - `JsonValue; type "environment_connection"constant`

          The type of the object. Always `environment_connection`.

          - `ENVIRONMENT_CONNECTION("environment_connection")`

    - `Status status`

      The current status of the session.

      - `IDLE("idle")`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `IN_PROGRESS("in_progress")`

        The session is processing a turn.

      - `REQUIRES_ACTION("requires_action")`

        The session is waiting for one or more required actions.

      - `FAILED("failed")`

        The session failed.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

    - `List<String> vaultIds`

      The IDs of vaults made available to the session.

  - `JsonValue; type "agent.session.in_progress"constant`

    The type of the object. Always `agent.session.in_progress`.

    - `AGENT_SESSION_IN_PROGRESS("agent.session.in_progress")`

### Agent Session Input Message Param

- `class AgentSessionInputMessageParam:`

  A user message submitted to a session.

  - `List<InputContentParam> content`

    The content of the message.

    - `InputText`

      - `String text`

        The text sent to the model.

      - `JsonValue; type "input_text"constant`

        The type of the object. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `InputImage`

      - `String imageUrl`

        The URL of the image sent to the model.

      - `JsonValue; type "input_image"constant`

        The type of the object. Always `input_image`.

        - `INPUT_IMAGE("input_image")`

  - `JsonValue; role "user"constant`

    The role of the message author. Always `user`.

    - `USER("user")`

  - `Optional<Type> type`

    The type of the input item. Always `message`.

    - `MESSAGE("message")`

### Agent Session Input Param

- `class AgentSessionInputParam: A class that can be one of several variants.union`

  Input submitted to an existing session.

  - `AgentSessionInputComputerUseApprovalRequestResult`

    - `String requestId`

      The registered request ID from the required action.

    - `Response response`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `List<Field> fields`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `String fieldId`

            The field ID from the required action.

          - `String value`

            The value to enter into the registered control.

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `Optional<String> selectedOption`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam:`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `class AgentBrowserOriginAccessParam:`

        - `Decision decision`

          Whether to allow, deny, or cancel the requested origin access.

          - `APPROVE("approve")`

            Allow the browser to access this origin.

          - `DENY("deny")`

            Deny access to this origin.

          - `CANCEL("cancel")`

            Dismiss this request without approving access.

        - `JsonValue; type "browser_origin_access"constant`

          - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

    - `JsonValue; type "agent.session.input.computer_use_approval_request_result"constant`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `AGENT_SESSION_INPUT_COMPUTER_USE_APPROVAL_REQUEST_RESULT("agent.session.input.computer_use_approval_request_result")`

  - `AgentSessionInputMessage`

    - `List<AgentSessionInputMessageParam> input`

      The user messages to add to the session.

      - `List<InputContentParam> content`

        The content of the message.

        - `InputText`

          - `String text`

            The text sent to the model.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image sent to the model.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

      - `JsonValue; role "user"constant`

        The role of the message author. Always `user`.

        - `USER("user")`

      - `Optional<Type> type`

        The type of the input item. Always `message`.

        - `MESSAGE("message")`

    - `JsonValue; type "agent.session.input.message"constant`

      The type of the object. Always `agent.session.input.message`.

      - `AGENT_SESSION_INPUT_MESSAGE("agent.session.input.message")`

  - `JsonValue;`

    - `JsonValue; type "agent.session.input.cancel"constant`

      The type of the object. Always `agent.session.input.cancel`.

      - `AGENT_SESSION_INPUT_CANCEL("agent.session.input.cancel")`

  - `AgentSessionInputToolResult`

    - `String callId`

      The ID of the function call.

    - `boolean success`

      Whether the function call succeeded.

    - `String turnId`

      The ID of the turn that requested the function call.

    - `JsonValue; type "agent.session.input.tool_result"constant`

      The type of the object. Always `agent.session.input.tool_result`.

      - `AGENT_SESSION_INPUT_TOOL_RESULT("agent.session.input.tool_result")`

    - `Optional<String> error`

      The error message when the call failed.

    - `Optional<AgentFunctionCallOutputParam> output`

      The function result when the call succeeded.

      - `String`

      - `List<InputContentParam>`

        - `InputText`

        - `InputImage`

### Agent Session Item

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

  - `class AgentSessionMessage:`

    A user or assistant message recorded in a session.

    - `Optional<String> id`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `List<AgentSessionMessageContent> content`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `InputText`

        - `String text`

          The text supplied by the user.

        - `JsonValue; type "input_text"constant`

          The type of the object. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `InputImage`

        - `String imageUrl`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `JsonValue; type "input_image"constant`

          The type of the object. Always `input_image`.

          - `INPUT_IMAGE("input_image")`

      - `OutputText`

        - `String text`

          The text produced by the assistant.

        - `JsonValue; type "output_text"constant`

          The type of the object. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

    - `Optional<Phase> phase`

      The phase of an assistant message. Null for user messages.

      - `COMMENTARY("commentary")`

        Commentary produced while the agent works.

      - `FINAL_ANSWER("final_answer")`

        The agent's final answer.

    - `Role role`

      The role of the message author.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `AgentOutputItemStatus status`

      The status of the message. User messages are always `completed`.

      - `IN_PROGRESS("in_progress")`

        The item is in progress.

      - `COMPLETED("completed")`

        The item is complete.

      - `INCOMPLETE("incomplete")`

        The item stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

    - `String name`

      The name of the function to call.

    - `AgentFunctionCallStatus status`

      The status of the function call.

      - `IN_PROGRESS("in_progress")`

        The call is in progress.

      - `COMPLETED("completed")`

        The call completed successfully.

      - `FAILED("failed")`

        The call failed.

      - `INCOMPLETE("incomplete")`

        The call stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `FunctionCallOutput`

    - `String id`

      The ID of the function call output item.

    - `String callId`

      The ID of the function call that produced this output.

    - `Optional<String> error`

      The error message, if the call failed.

    - `Optional<AgentFunctionCallOutput> output`

      The function result, if the call succeeded.

      - `String`

      - `List<InputContent>`

        - `InputText`

          - `String text`

            The text supplied to the agent.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

    - `AgentFunctionCallStatus status`

      The status of the function call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call_output"constant`

      The item type. Always `function_call_output`.

      - `FUNCTION_CALL_OUTPUT("function_call_output")`

  - `AgentMessage`

    - `String id`

      The ID of the message.

    - `List<AgentContent> content`

      The content exchanged between the agents.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `String recipientAgentId`

      The ID or name of the receiving agent.

    - `String senderAgentId`

      The ID or name of the sending agent.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "agent_message"constant`

      The item type. Always `agent_message`.

      - `AGENT_MESSAGE("agent_message")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        - `String id`

          The field ID to submit as field_id in a fields entry.

        - `String label`

          The label to display beside the control.

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        - `String id`

          The option ID to submit as selected_option.

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

        - `String label`

          The method label to display.

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

    - `String turnId`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `ComputerUseApprovalRequestResult`

    - `String id`

      The stable history item ID.

    - `String requestId`

      The registered request answered by this item.

    - `Response response`

      The admitted response, without submitted credential values.

      - `class Submit:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `Optional<String> selectedOption`

          The chosen sign-in method, or null when no options were offered.

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `JsonValue;`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_approval_request_result"constant`

      - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

        - `Optional<String> query`

          The search query, when a single query was used.

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

    - `String command`

      The command that was executed.

    - `Optional<String> cwd`

      The working directory used to execute the command.

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

    - `Optional<String> output`

      The command output, if available.

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

    - `String agentId`

      The ID of the agent that requested the subagent.

    - `List<AgentContent> content`

      The task given to the spawned agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `Optional<String> model`

      The model requested for the spawned agent.

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

        The current public item type.

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

    - `String senderAgentId`

      The ID of the agent sending the input.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

        The current public item type.

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to resume.

    - `String senderAgentId`

      The ID of the agent requesting the resume.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

    - `String senderAgentId`

      The ID of the agent waiting for results.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

        The current public item type.

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to interrupt.

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

        The current public item type.

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to close.

    - `String senderAgentId`

      The ID of the agent requesting the close.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

        The current public item type.

### Agent Session Message

- `class AgentSessionMessage:`

  A user or assistant message recorded in a session.

  - `Optional<String> id`

    The ID of this item, or null for legacy user messages whose ID was not recorded.

  - `List<AgentSessionMessageContent> content`

    The content of the message. User messages contain input text or images; assistant messages contain output text.

    - `InputText`

      - `String text`

        The text supplied by the user.

      - `JsonValue; type "input_text"constant`

        The type of the object. Always `input_text`.

        - `INPUT_TEXT("input_text")`

    - `InputImage`

      - `String imageUrl`

        The URL of the image supplied by the user, which may be a base64-encoded data URL.

      - `JsonValue; type "input_image"constant`

        The type of the object. Always `input_image`.

        - `INPUT_IMAGE("input_image")`

    - `OutputText`

      - `String text`

        The text produced by the assistant.

      - `JsonValue; type "output_text"constant`

        The type of the object. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

  - `Optional<Phase> phase`

    The phase of an assistant message. Null for user messages.

    - `COMMENTARY("commentary")`

      Commentary produced while the agent works.

    - `FINAL_ANSWER("final_answer")`

      The agent's final answer.

  - `Role role`

    The role of the message author.

    - `USER("user")`

    - `ASSISTANT("assistant")`

  - `AgentOutputItemStatus status`

    The status of the message. User messages are always `completed`.

    - `IN_PROGRESS("in_progress")`

      The item is in progress.

    - `COMPLETED("completed")`

      The item is complete.

    - `INCOMPLETE("incomplete")`

      The item stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "message"constant`

    The item type. Always `message`.

    - `MESSAGE("message")`

### Agent Session Message Content

- `class AgentSessionMessageContent: A class that can be one of several variants.union`

  A content part in a session message.

  - `InputText`

    - `String text`

      The text supplied by the user.

    - `JsonValue; type "input_text"constant`

      The type of the object. Always `input_text`.

      - `INPUT_TEXT("input_text")`

  - `InputImage`

    - `String imageUrl`

      The URL of the image supplied by the user, which may be a base64-encoded data URL.

    - `JsonValue; type "input_image"constant`

      The type of the object. Always `input_image`.

      - `INPUT_IMAGE("input_image")`

  - `OutputText`

    - `String text`

      The text produced by the assistant.

    - `JsonValue; type "output_text"constant`

      The type of the object. Always `output_text`.

      - `OUTPUT_TEXT("output_text")`

### Agent Session Requires Action Event

- `class AgentSessionRequiresActionEvent:`

  Emitted when a session is waiting for one or more required actions.

  - `String eventId`

    The unique ID of the event.

  - `AgentSession session`

    The session and its current required actions.

    - `String id`

      The ID of the session.

    - `Agent agent`

      The agent running in the session.

      - `String id`

        The ID of the agent.

      - `Optional<String> instructions`

        Custom instructions appended to the agent's default base instructions.

      - `String model`

        The model used by the agent.

      - `MultiAgentConfig multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      - `Optional<String> name`

        The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

      - `AgentReasoning reasoning`

        The agent's reasoning configuration.

        - `Optional<Effort> effort`

          The requested reasoning effort, or `null` when the model selects its own default.

          - `NONE("none")`

          - `MINIMAL("minimal")`

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

          - `XHIGH("xhigh")`

          - `MAX("max")`

        - `Optional<Summary> summary`

          The requested reasoning summary format, or `null` when summaries are disabled.

          - `CONCISE("concise")`

            Returns a concise reasoning summary when supported.

          - `DETAILED("detailed")`

            Returns a detailed reasoning summary when supported.

          - `AUTO("auto")`

            Automatically selects the most detailed summary supported by the model.

      - `ServiceTier serviceTier`

        The effective service-tier policy for model requests. Defaults to `auto`.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        Configuration for text generated by the agent.

        - `TextFormat format`

          The effective output format. Defaults to ordinary text.

          - `JsonValue;`

            - `JsonValue; type "text"constant`

              The type of the object. Always `text`.

              - `TEXT("text")`

          - `JsonSchema`

            - `Schema schema`

              The JSON Schema that generated text must match.

            - `JsonValue; type "json_schema"constant`

              The type of the object. Always `json_schema`.

              - `JSON_SCHEMA("json_schema")`

        - `Verbosity verbosity`

          The amount of text produced by the agent. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

      - `List<AgentTool> tools`

        Tools available to the agent.

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

          - `String name`

            The name of the function.

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

              - `String command`

                The command used to start the MCP server.

              - `String cwd`

                The working directory used to start the MCP server.

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

            - `Optional<String> region`

              The region or state name.

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

          - `Mode mode`

            The source used for web search results.

            - `DISABLED("disabled")`

            - `CACHED("cached")`

            - `LIVE("live")`

          - `JsonValue; type "web_search"constant`

            The type of the object. Always `web_search`.

            - `WEB_SEARCH("web_search")`

        - `ComputerUse`

          - `boolean includeScreenshots`

            Whether computer tool outputs include screenshots.

          - `JsonValue; type "computer_use"constant`

            The type of the object. Always `computer_use`.

            - `COMPUTER_USE("computer_use")`

    - `long createdAt`

      The Unix timestamp, in seconds, when the session was created.

    - `Environment environment`

      The execution environment for the session.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `Desktop desktop`

          The effective desktop configuration.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `List<HostedEnvironmentFile> files`

          Files available in the environment, excluding their contents.

          - `class HostedEnvironmentFileId:`

            A file copied from the OpenAI Files API.

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String fileId`

              The ID of the uploaded file.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String id`

              The session-scoped ID of the file in the execution environment.

            - `String path`

              The file's absolute path inside the environment.

            - `long sizeBytes`

              The decoded file size in bytes.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Network network`

          The effective network access policy for the environment.

          - `Access access`

            The environment's network access mode.

            - `ENABLED("enabled")`

              Allows unrestricted network access.

            - `DISABLED("disabled")`

              Disables network access.

            - `RESTRICTED("restricted")`

              Applies the configured domain restrictions.

          - `List<String> allowedDomains`

            Domains the environment may access when network access is restricted.

        - `Packages packages`

          Packages installed in the environment.

          - `List<String> npm`

            npm packages installed globally in the environment.

          - `List<String> python`

            Python packages installed in the environment.

          - `List<String> system`

            System packages installed in the environment.

        - `List<HostedPlugin> plugins`

          Plugins installed in the environment, excluding their archive contents.

          - `String description`

            The installed plugin description.

          - `String name`

            The installed plugin name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `List<HostedSkill> skills`

          Skills installed in the environment, excluding their archive contents.

          - `class HostedSkillReference:`

            A skill installed from the Skills API.

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `String skillId`

              The referenced skill ID.

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `String version`

              The concrete skill version installed for this session.

          - `Inline`

            - `String description`

              The installed skill description.

            - `String name`

              The installed skill name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

        - `Optional<ContainerSize> containerSize`

          The effective CPU and memory tier, or null when unknown or outside the public tiers.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

      - `SelfHosted`

        - `String id`

          The public ID of the environment.

        - `List<String> capabilityDirectories`

          Directories that contain capabilities exposed to the agent.

        - `String remoteUrl`

          Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory inside the environment. Defaults to `/workspace`.

    - `Optional<String> error`

      The error that caused the session to fail, if any.

    - `long lastActiveAt`

      The Unix timestamp, in seconds, when the session was last active.

    - `Metadata metadata`

      Custom string key-value pairs attached to the session.

    - `JsonValue; object_ "agent.session"constant`

      The object type. Always `agent.session`.

      - `AGENT_SESSION("agent.session")`

    - `List<RequiredAction> requiredActions`

      Actions that must be completed before the session can continue.

      - `class ComputerUseApprovalRequest:`

        Respond to a computer-use request.

        - `Request request`

          The information needed to render the request.

          - `class BrowserAuthentication:`

            A registered form awaiting the application's response.

            - `Optional<String> credentialOrigin`

              The registered form or frame origin where values will be entered.

            - `List<Field> fields`

              Controls to render. All submitted values are sensitive.

              - `String id`

                The field ID to submit as field_id in a fields entry.

              - `String label`

                The label to display beside the control.

              - `boolean required`

                Whether this control requires a nonempty value.

              - `String type`

                The rendering type, such as email, password, or text.

            - `List<Option> options`

              Sign-in methods. Empty for a plain form.

              - `String id`

                The option ID to submit as selected_option.

              - `List<String> fieldIds`

                IDs from the registered fields that this method accepts.

              - `String label`

                The method label to display.

            - `Optional<String> reason`

              Why the agent needs the user to sign in.

            - `JsonValue; type "browser_authentication"constant`

              The type of the object. Always `browser_authentication`.

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `class BrowserOriginAccess:`

            A browser origin awaiting the application's approval decision.

            - `String origin`

              The origin the browser needs permission to access.

            - `Optional<String> reason`

              The browser's explanation for this request, or null when unavailable.

            - `JsonValue; type "browser_origin_access"constant`

              The type of the object. Always `browser_origin_access`.

              - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

        - `String requestId`

          The registered request ID to echo when responding.

        - `String turnId`

          The turn that requested approval.

        - `JsonValue; type "computer_use_approval_request"constant`

          The type of the object. Always `computer_use_approval_request`.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class FunctionCall:`

        Run a function tool and submit its result.

        - `JsonValue arguments`

          The arguments supplied by the model.

        - `String callId`

          The ID to include when submitting the function result.

        - `String name`

          The function name.

        - `String turnId`

          The ID of the turn that requested the function call.

        - `JsonValue; type "function_call"constant`

          The type of the object. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `class EnvironmentConnection:`

        Reconnect a session environment.

        - `String environmentId`

          The ID of the environment to reconnect.

        - `JsonValue; type "environment_connection"constant`

          The type of the object. Always `environment_connection`.

          - `ENVIRONMENT_CONNECTION("environment_connection")`

    - `Status status`

      The current status of the session.

      - `IDLE("idle")`

        The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

      - `IN_PROGRESS("in_progress")`

        The session is processing a turn.

      - `REQUIRES_ACTION("requires_action")`

        The session is waiting for one or more required actions.

      - `FAILED("failed")`

        The session failed.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the session, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

    - `List<String> vaultIds`

      The IDs of vaults made available to the session.

  - `JsonValue; type "agent.session.requires_action"constant`

    The type of the object. Always `agent.session.requires_action`.

    - `AGENT_SESSION_REQUIRES_ACTION("agent.session.requires_action")`

### Agent Session Subagent Active Event

- `class AgentSessionSubagentActiveEvent:`

  Emitted when a closed subagent successfully resumes.

  - `String eventId`

    The unique ID of the event.

  - `Subagent subagent`

    The subagent that resumed.

    - `String id`

      The ID of the subagent.

    - `Optional<Long> closedAt`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Optional<List<AgentContent>> instructions`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `Optional<String> name`

      The runner-assigned nickname, or null when unavailable.

    - `Object object_`

      The object type. Always `agent.session.subagent`.

      - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

    - `long openedAt`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `String parentAgentId`

      The ID of the agent that created this subagent.

    - `String sessionId`

      The ID of the session that owns the subagent.

    - `Status status`

      The current status of the subagent.

      - `ACTIVE("active")`

        The subagent remains available, including while idle between turns.

      - `CLOSED("closed")`

        The subagent is closed.

  - `JsonValue; type "agent.session.subagent.active"constant`

    The type of the object. Always `agent.session.subagent.active`.

    - `AGENT_SESSION_SUBAGENT_ACTIVE("agent.session.subagent.active")`

### Agent Session Subagent Closed Event

- `class AgentSessionSubagentClosedEvent:`

  Emitted when a subagent is closed.

  - `String eventId`

    The unique ID of the event.

  - `Subagent subagent`

    The subagent that was closed.

    - `String id`

      The ID of the subagent.

    - `Optional<Long> closedAt`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Optional<List<AgentContent>> instructions`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `Optional<String> name`

      The runner-assigned nickname, or null when unavailable.

    - `Object object_`

      The object type. Always `agent.session.subagent`.

      - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

    - `long openedAt`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `String parentAgentId`

      The ID of the agent that created this subagent.

    - `String sessionId`

      The ID of the session that owns the subagent.

    - `Status status`

      The current status of the subagent.

      - `ACTIVE("active")`

        The subagent remains available, including while idle between turns.

      - `CLOSED("closed")`

        The subagent is closed.

  - `JsonValue; type "agent.session.subagent.closed"constant`

    The type of the object. Always `agent.session.subagent.closed`.

    - `AGENT_SESSION_SUBAGENT_CLOSED("agent.session.subagent.closed")`

### Agent Session Subagent Created Event

- `class AgentSessionSubagentCreatedEvent:`

  Emitted when a subagent is created.

  - `String eventId`

    The unique ID of the event.

  - `Subagent subagent`

    The subagent that was created.

    - `String id`

      The ID of the subagent.

    - `Optional<Long> closedAt`

      The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

    - `Optional<List<AgentContent>> instructions`

      Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `Optional<String> name`

      The runner-assigned nickname, or null when unavailable.

    - `Object object_`

      The object type. Always `agent.session.subagent`.

      - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

    - `long openedAt`

      The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

    - `String parentAgentId`

      The ID of the agent that created this subagent.

    - `String sessionId`

      The ID of the session that owns the subagent.

    - `Status status`

      The current status of the subagent.

      - `ACTIVE("active")`

        The subagent remains available, including while idle between turns.

      - `CLOSED("closed")`

        The subagent is closed.

  - `JsonValue; type "agent.session.subagent.created"constant`

    The type of the object. Always `agent.session.subagent.created`.

    - `AGENT_SESSION_SUBAGENT_CREATED("agent.session.subagent.created")`

### Agent Session Turn Cancelled Event

- `class AgentSessionTurnCancelledEvent:`

  Emitted when a turn is cancelled.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Turn turn`

    The cancelled turn.

    - `String id`

      The ID of the turn.

    - `String agentId`

      The ID of the agent that ran the turn.

    - `Optional<Long> completedAt`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `long createdAt`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Optional<SessionTurnError> error`

      A customer-safe error. Non-null only for a failed turn.

      - `Code code`

        A stable, machine-readable failure category.

        - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

          The request exceeds the model's context window.

        - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

          The session has reached its usage budget.

        - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

          The organization has reached a usage, plan, or billing limit.

        - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

          The organization has no API credits remaining.

        - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          The request exceeds the available rate limit.

        - `FLEX_UNAVAILABLE("flex_unavailable")`

          Flex processing is temporarily unavailable.

        - `SERVER_OVERLOADED("server_overloaded")`

          The model service is temporarily overloaded.

        - `CYBER_POLICY("cyber_policy")`

          The request was rejected by a safety policy.

        - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

          The request was blocked by the safety systems.

        - `CONNECTION_FAILED("connection_failed")`

          The request could not connect to the model service.

        - `SERVER_ERROR("server_error")`

          The model service encountered an unexpected error.

        - `AUTHENTICATION_ERROR("authentication_error")`

          The API credentials are invalid or lack the required access.

        - `INVALID_REQUEST("invalid_request")`

          The request contains invalid input or configuration.

        - `RESOURCE_NOT_FOUND("resource_not_found")`

          The requested model or resource is unavailable.

        - `SANDBOX_ERROR("sandbox_error")`

          The request could not complete in its execution environment.

        - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

          The executor must be upgraded before it can run this turn.

        - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

          The session cannot accept additional input while a request is running.

        - `REQUEST_TIMEOUT("request_timeout")`

          The request timed out before the model service responded.

        - `INTERNAL_ERROR("internal_error")`

          An unexpected internal error prevented the session request from completing.

      - `String message`

        A customer-safe explanation of the failure.

    - `Object object_`

      The object type. Always `agent.session.turn`.

      - `AGENT_SESSION_TURN("agent.session.turn")`

    - `String sessionId`

      The ID of the session that owns the turn.

    - `Optional<Long> startedAt`

      The Unix timestamp, in seconds, when the turn started.

    - `Status status`

      The current status of the turn.

      - `QUEUED("queued")`

        The turn is waiting to start.

      - `IN_PROGRESS("in_progress")`

        The turn is in progress.

      - `WAITING("waiting")`

        The turn is waiting for external input.

      - `COMPLETED("completed")`

        The turn completed successfully.

      - `FAILED("failed")`

        The turn failed.

      - `CANCELLED("cancelled")`

        The turn was cancelled.

    - `Optional<String> subagentId`

      The ID of the subagent that ran the turn, if applicable.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

  - `String turnId`

    The ID of the turn associated with the event.

  - `JsonValue; type "agent.session.turn.cancelled"constant`

    The type of the object. Always `agent.session.turn.cancelled`.

    - `AGENT_SESSION_TURN_CANCELLED("agent.session.turn.cancelled")`

  - `Optional<TokenUsage> usage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Completed Event

- `class AgentSessionTurnCompletedEvent:`

  Emitted when a turn completes.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Turn turn`

    The completed turn.

    - `String id`

      The ID of the turn.

    - `String agentId`

      The ID of the agent that ran the turn.

    - `Optional<Long> completedAt`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `long createdAt`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Optional<SessionTurnError> error`

      A customer-safe error. Non-null only for a failed turn.

      - `Code code`

        A stable, machine-readable failure category.

        - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

          The request exceeds the model's context window.

        - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

          The session has reached its usage budget.

        - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

          The organization has reached a usage, plan, or billing limit.

        - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

          The organization has no API credits remaining.

        - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          The request exceeds the available rate limit.

        - `FLEX_UNAVAILABLE("flex_unavailable")`

          Flex processing is temporarily unavailable.

        - `SERVER_OVERLOADED("server_overloaded")`

          The model service is temporarily overloaded.

        - `CYBER_POLICY("cyber_policy")`

          The request was rejected by a safety policy.

        - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

          The request was blocked by the safety systems.

        - `CONNECTION_FAILED("connection_failed")`

          The request could not connect to the model service.

        - `SERVER_ERROR("server_error")`

          The model service encountered an unexpected error.

        - `AUTHENTICATION_ERROR("authentication_error")`

          The API credentials are invalid or lack the required access.

        - `INVALID_REQUEST("invalid_request")`

          The request contains invalid input or configuration.

        - `RESOURCE_NOT_FOUND("resource_not_found")`

          The requested model or resource is unavailable.

        - `SANDBOX_ERROR("sandbox_error")`

          The request could not complete in its execution environment.

        - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

          The executor must be upgraded before it can run this turn.

        - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

          The session cannot accept additional input while a request is running.

        - `REQUEST_TIMEOUT("request_timeout")`

          The request timed out before the model service responded.

        - `INTERNAL_ERROR("internal_error")`

          An unexpected internal error prevented the session request from completing.

      - `String message`

        A customer-safe explanation of the failure.

    - `Object object_`

      The object type. Always `agent.session.turn`.

      - `AGENT_SESSION_TURN("agent.session.turn")`

    - `String sessionId`

      The ID of the session that owns the turn.

    - `Optional<Long> startedAt`

      The Unix timestamp, in seconds, when the turn started.

    - `Status status`

      The current status of the turn.

      - `QUEUED("queued")`

        The turn is waiting to start.

      - `IN_PROGRESS("in_progress")`

        The turn is in progress.

      - `WAITING("waiting")`

        The turn is waiting for external input.

      - `COMPLETED("completed")`

        The turn completed successfully.

      - `FAILED("failed")`

        The turn failed.

      - `CANCELLED("cancelled")`

        The turn was cancelled.

    - `Optional<String> subagentId`

      The ID of the subagent that ran the turn, if applicable.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

  - `String turnId`

    The ID of the turn associated with the event.

  - `JsonValue; type "agent.session.turn.completed"constant`

    The type of the object. Always `agent.session.turn.completed`.

    - `AGENT_SESSION_TURN_COMPLETED("agent.session.turn.completed")`

  - `Optional<TokenUsage> usage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn Content Part Added Event

- `class AgentSessionTurnContentPartAddedEvent:`

  Emitted when an output text content part is added.

  - `long contentIndex`

    The index of the content part in the message.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the message item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `OutputText part`

    The initial content part.

    - `String text`

      The text produced by the agent.

    - `JsonValue; type "output_text"constant`

      The content type. Always `output_text`.

      - `OUTPUT_TEXT("output_text")`

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.content_part.added"constant`

    The type of the object. Always `agent.session.turn.content_part.added`.

    - `AGENT_SESSION_TURN_CONTENT_PART_ADDED("agent.session.turn.content_part.added")`

### Agent Session Turn Content Part Done Event

- `class AgentSessionTurnContentPartDoneEvent:`

  Emitted when an output content part is complete.

  - `long contentIndex`

    The index of the content part in the message.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the message item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `OutputText part`

    The completed content part.

    - `String text`

      The text produced by the agent.

    - `JsonValue; type "output_text"constant`

      The content type. Always `output_text`.

      - `OUTPUT_TEXT("output_text")`

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.content_part.done"constant`

    The type of the object. Always `agent.session.turn.content_part.done`.

    - `AGENT_SESSION_TURN_CONTENT_PART_DONE("agent.session.turn.content_part.done")`

### Agent Session Turn Created Event

- `class AgentSessionTurnCreatedEvent:`

  Emitted when a turn is created.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Turn turn`

    The turn at the time it was created.

    - `String id`

      The ID of the turn.

    - `String agentId`

      The ID of the agent that ran the turn.

    - `Optional<Long> completedAt`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `long createdAt`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Optional<SessionTurnError> error`

      A customer-safe error. Non-null only for a failed turn.

      - `Code code`

        A stable, machine-readable failure category.

        - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

          The request exceeds the model's context window.

        - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

          The session has reached its usage budget.

        - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

          The organization has reached a usage, plan, or billing limit.

        - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

          The organization has no API credits remaining.

        - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          The request exceeds the available rate limit.

        - `FLEX_UNAVAILABLE("flex_unavailable")`

          Flex processing is temporarily unavailable.

        - `SERVER_OVERLOADED("server_overloaded")`

          The model service is temporarily overloaded.

        - `CYBER_POLICY("cyber_policy")`

          The request was rejected by a safety policy.

        - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

          The request was blocked by the safety systems.

        - `CONNECTION_FAILED("connection_failed")`

          The request could not connect to the model service.

        - `SERVER_ERROR("server_error")`

          The model service encountered an unexpected error.

        - `AUTHENTICATION_ERROR("authentication_error")`

          The API credentials are invalid or lack the required access.

        - `INVALID_REQUEST("invalid_request")`

          The request contains invalid input or configuration.

        - `RESOURCE_NOT_FOUND("resource_not_found")`

          The requested model or resource is unavailable.

        - `SANDBOX_ERROR("sandbox_error")`

          The request could not complete in its execution environment.

        - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

          The executor must be upgraded before it can run this turn.

        - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

          The session cannot accept additional input while a request is running.

        - `REQUEST_TIMEOUT("request_timeout")`

          The request timed out before the model service responded.

        - `INTERNAL_ERROR("internal_error")`

          An unexpected internal error prevented the session request from completing.

      - `String message`

        A customer-safe explanation of the failure.

    - `Object object_`

      The object type. Always `agent.session.turn`.

      - `AGENT_SESSION_TURN("agent.session.turn")`

    - `String sessionId`

      The ID of the session that owns the turn.

    - `Optional<Long> startedAt`

      The Unix timestamp, in seconds, when the turn started.

    - `Status status`

      The current status of the turn.

      - `QUEUED("queued")`

        The turn is waiting to start.

      - `IN_PROGRESS("in_progress")`

        The turn is in progress.

      - `WAITING("waiting")`

        The turn is waiting for external input.

      - `COMPLETED("completed")`

        The turn completed successfully.

      - `FAILED("failed")`

        The turn failed.

      - `CANCELLED("cancelled")`

        The turn was cancelled.

    - `Optional<String> subagentId`

      The ID of the subagent that ran the turn, if applicable.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

  - `String turnId`

    The ID of the turn associated with the event.

  - `JsonValue; type "agent.session.turn.created"constant`

    The type of the object. Always `agent.session.turn.created`.

    - `AGENT_SESSION_TURN_CREATED("agent.session.turn.created")`

### Agent Session Turn Failed Event

- `class AgentSessionTurnFailedEvent:`

  Emitted when a turn fails.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Turn turn`

    The failed turn.

    - `String id`

      The ID of the turn.

    - `String agentId`

      The ID of the agent that ran the turn.

    - `Optional<Long> completedAt`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `long createdAt`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Optional<SessionTurnError> error`

      A customer-safe error. Non-null only for a failed turn.

      - `Code code`

        A stable, machine-readable failure category.

        - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

          The request exceeds the model's context window.

        - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

          The session has reached its usage budget.

        - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

          The organization has reached a usage, plan, or billing limit.

        - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

          The organization has no API credits remaining.

        - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          The request exceeds the available rate limit.

        - `FLEX_UNAVAILABLE("flex_unavailable")`

          Flex processing is temporarily unavailable.

        - `SERVER_OVERLOADED("server_overloaded")`

          The model service is temporarily overloaded.

        - `CYBER_POLICY("cyber_policy")`

          The request was rejected by a safety policy.

        - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

          The request was blocked by the safety systems.

        - `CONNECTION_FAILED("connection_failed")`

          The request could not connect to the model service.

        - `SERVER_ERROR("server_error")`

          The model service encountered an unexpected error.

        - `AUTHENTICATION_ERROR("authentication_error")`

          The API credentials are invalid or lack the required access.

        - `INVALID_REQUEST("invalid_request")`

          The request contains invalid input or configuration.

        - `RESOURCE_NOT_FOUND("resource_not_found")`

          The requested model or resource is unavailable.

        - `SANDBOX_ERROR("sandbox_error")`

          The request could not complete in its execution environment.

        - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

          The executor must be upgraded before it can run this turn.

        - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

          The session cannot accept additional input while a request is running.

        - `REQUEST_TIMEOUT("request_timeout")`

          The request timed out before the model service responded.

        - `INTERNAL_ERROR("internal_error")`

          An unexpected internal error prevented the session request from completing.

      - `String message`

        A customer-safe explanation of the failure.

    - `Object object_`

      The object type. Always `agent.session.turn`.

      - `AGENT_SESSION_TURN("agent.session.turn")`

    - `String sessionId`

      The ID of the session that owns the turn.

    - `Optional<Long> startedAt`

      The Unix timestamp, in seconds, when the turn started.

    - `Status status`

      The current status of the turn.

      - `QUEUED("queued")`

        The turn is waiting to start.

      - `IN_PROGRESS("in_progress")`

        The turn is in progress.

      - `WAITING("waiting")`

        The turn is waiting for external input.

      - `COMPLETED("completed")`

        The turn completed successfully.

      - `FAILED("failed")`

        The turn failed.

      - `CANCELLED("cancelled")`

        The turn was cancelled.

    - `Optional<String> subagentId`

      The ID of the subagent that ran the turn, if applicable.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

  - `String turnId`

    The ID of the turn associated with the event.

  - `JsonValue; type "agent.session.turn.failed"constant`

    The type of the object. Always `agent.session.turn.failed`.

    - `AGENT_SESSION_TURN_FAILED("agent.session.turn.failed")`

  - `Optional<TokenUsage> usage`

    Token usage by the root agent during the turn, when available.

### Agent Session Turn In Progress Event

- `class AgentSessionTurnInProgressEvent:`

  Emitted when a turn starts running.

  - `String eventId`

    The unique ID of the event.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Turn turn`

    The turn at the time it started running.

    - `String id`

      The ID of the turn.

    - `String agentId`

      The ID of the agent that ran the turn.

    - `Optional<Long> completedAt`

      The Unix timestamp, in seconds, when the turn reached a terminal state.

    - `long createdAt`

      The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

    - `Optional<SessionTurnError> error`

      A customer-safe error. Non-null only for a failed turn.

      - `Code code`

        A stable, machine-readable failure category.

        - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

          The request exceeds the model's context window.

        - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

          The session has reached its usage budget.

        - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

          The organization has reached a usage, plan, or billing limit.

        - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

          The organization has no API credits remaining.

        - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

          The request exceeds the available rate limit.

        - `FLEX_UNAVAILABLE("flex_unavailable")`

          Flex processing is temporarily unavailable.

        - `SERVER_OVERLOADED("server_overloaded")`

          The model service is temporarily overloaded.

        - `CYBER_POLICY("cyber_policy")`

          The request was rejected by a safety policy.

        - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

          The request was blocked by the safety systems.

        - `CONNECTION_FAILED("connection_failed")`

          The request could not connect to the model service.

        - `SERVER_ERROR("server_error")`

          The model service encountered an unexpected error.

        - `AUTHENTICATION_ERROR("authentication_error")`

          The API credentials are invalid or lack the required access.

        - `INVALID_REQUEST("invalid_request")`

          The request contains invalid input or configuration.

        - `RESOURCE_NOT_FOUND("resource_not_found")`

          The requested model or resource is unavailable.

        - `SANDBOX_ERROR("sandbox_error")`

          The request could not complete in its execution environment.

        - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

          The executor must be upgraded before it can run this turn.

        - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

          The session cannot accept additional input while a request is running.

        - `REQUEST_TIMEOUT("request_timeout")`

          The request timed out before the model service responded.

        - `INTERNAL_ERROR("internal_error")`

          An unexpected internal error prevented the session request from completing.

      - `String message`

        A customer-safe explanation of the failure.

    - `Object object_`

      The object type. Always `agent.session.turn`.

      - `AGENT_SESSION_TURN("agent.session.turn")`

    - `String sessionId`

      The ID of the session that owns the turn.

    - `Optional<Long> startedAt`

      The Unix timestamp, in seconds, when the turn started.

    - `Status status`

      The current status of the turn.

      - `QUEUED("queued")`

        The turn is waiting to start.

      - `IN_PROGRESS("in_progress")`

        The turn is in progress.

      - `WAITING("waiting")`

        The turn is waiting for external input.

      - `COMPLETED("completed")`

        The turn completed successfully.

      - `FAILED("failed")`

        The turn failed.

      - `CANCELLED("cancelled")`

        The turn was cancelled.

    - `Optional<String> subagentId`

      The ID of the subagent that ran the turn, if applicable.

    - `Optional<TokenUsage> usage`

      Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

      - `long inputTokens`

        The number of input tokens used by the agent.

      - `InputTokensDetails inputTokensDetails`

        A breakdown of the agent's input token usage.

        - `long cachedTokens`

          The number of input tokens retrieved from the prompt cache.

      - `long outputTokens`

        The number of output tokens generated by the agent.

      - `OutputTokensDetails outputTokensDetails`

        A breakdown of the agent's output token usage.

        - `long reasoningTokens`

          The number of output tokens used for reasoning.

      - `long totalTokens`

        The total number of input and output tokens used by the agent.

  - `String turnId`

    The ID of the turn associated with the event.

  - `JsonValue; type "agent.session.turn.in_progress"constant`

    The type of the object. Always `agent.session.turn.in_progress`.

    - `AGENT_SESSION_TURN_IN_PROGRESS("agent.session.turn.in_progress")`

### Agent Session Turn Item Added Event

- `class AgentSessionTurnItemAddedEvent:`

  Emitted when an item is added to a turn.

  - `String eventId`

    The unique ID of the event.

  - `AgentSessionItem item`

    The item that was added.

    - `class AgentSessionMessage:`

      A user or assistant message recorded in a session.

      - `Optional<String> id`

        The ID of this item, or null for legacy user messages whose ID was not recorded.

      - `List<AgentSessionMessageContent> content`

        The content of the message. User messages contain input text or images; assistant messages contain output text.

        - `InputText`

          - `String text`

            The text supplied by the user.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied by the user, which may be a base64-encoded data URL.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

        - `OutputText`

          - `String text`

            The text produced by the assistant.

          - `JsonValue; type "output_text"constant`

            The type of the object. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

      - `Optional<Phase> phase`

        The phase of an assistant message. Null for user messages.

        - `COMMENTARY("commentary")`

          Commentary produced while the agent works.

        - `FINAL_ANSWER("final_answer")`

          The agent's final answer.

      - `Role role`

        The role of the message author.

        - `USER("user")`

        - `ASSISTANT("assistant")`

      - `AgentOutputItemStatus status`

        The status of the message. User messages are always `completed`.

        - `IN_PROGRESS("in_progress")`

          The item is in progress.

        - `COMPLETED("completed")`

          The item is complete.

        - `INCOMPLETE("incomplete")`

          The item stopped before completing.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "message"constant`

        The item type. Always `message`.

        - `MESSAGE("message")`

    - `class AgentReasoningItem:`

      A reasoning item produced by the agent.

      - `String id`

        The ID of the reasoning item.

      - `Optional<AgentOutputItemStatus> status`

        The status of the reasoning item.

      - `List<SummaryText> summary`

        The reasoning summaries produced by the agent.

        - `String text`

          The reasoning summary text.

        - `JsonValue; type "summary_text"constant`

          The content type. Always `summary_text`.

          - `SUMMARY_TEXT("summary_text")`

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "reasoning"constant`

        The item type. Always `reasoning`.

        - `REASONING("reasoning")`

    - `class AgentFunctionCallItem:`

      A function call produced by the agent.

      - `String id`

        The ID of the function call item.

      - `JsonValue arguments`

        The arguments to pass to the function.

      - `String callId`

        The ID used to submit the function result.

      - `String name`

        The name of the function to call.

      - `AgentFunctionCallStatus status`

        The status of the function call.

        - `IN_PROGRESS("in_progress")`

          The call is in progress.

        - `COMPLETED("completed")`

          The call completed successfully.

        - `FAILED("failed")`

          The call failed.

        - `INCOMPLETE("incomplete")`

          The call stopped before completing.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "function_call"constant`

        The item type. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `FunctionCallOutput`

      - `String id`

        The ID of the function call output item.

      - `String callId`

        The ID of the function call that produced this output.

      - `Optional<String> error`

        The error message, if the call failed.

      - `Optional<AgentFunctionCallOutput> output`

        The function result, if the call succeeded.

        - `String`

        - `List<InputContent>`

          - `InputText`

            - `String text`

              The text supplied to the agent.

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

      - `AgentFunctionCallStatus status`

        The status of the function call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "function_call_output"constant`

        The item type. Always `function_call_output`.

        - `FUNCTION_CALL_OUTPUT("function_call_output")`

    - `AgentMessage`

      - `String id`

        The ID of the message.

      - `List<AgentContent> content`

        The content exchanged between the agents.

        - `class OutputText:`

          A text content part produced by the agent.

          - `String text`

            The text produced by the agent.

          - `JsonValue; type "output_text"constant`

            The content type. Always `output_text`.

            - `OUTPUT_TEXT("output_text")`

        - `EncryptedContent`

          - `String encryptedContent`

            The encrypted content payload.

          - `JsonValue; type "encrypted_content"constant`

            The content type. Always `encrypted_content`.

            - `ENCRYPTED_CONTENT("encrypted_content")`

      - `String recipientAgentId`

        The ID or name of the receiving agent.

      - `String senderAgentId`

        The ID or name of the sending agent.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "agent_message"constant`

        The item type. Always `agent_message`.

        - `AGENT_MESSAGE("agent_message")`

    - `class AgentMcpCallItem:`

      A call to a tool on an MCP server.

      - `String id`

        The ID of the MCP call item.

      - `JsonValue arguments`

        The arguments passed to the MCP tool.

      - `JsonValue error`

        The error returned by the MCP tool, if any.

      - `String name`

        The name of the MCP tool.

      - `JsonValue output`

        The output returned by the MCP tool, if any.

      - `String serverLabel`

        The label of the MCP server.

      - `AgentFunctionCallStatus status`

        The status of the MCP tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "mcp_call"constant`

        The item type. Always `mcp_call`.

        - `MCP_CALL("mcp_call")`

    - `ComputerUseCall`

      - `String id`

        The ID of the activity item.

      - `Optional<Output> output`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `String imageUrl`

          The complete JPEG image as a base64 data URL.

        - `JsonValue; type "computer_screenshot"constant`

          The content type. Always `computer_screenshot`.

          - `COMPUTER_SCREENSHOT("computer_screenshot")`

      - `AgentFunctionCallStatus status`

        The execution status of the activity.

      - `Optional<String> title`

        A model-generated description of the activity, when available.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "computer_use_call"constant`

        The item type. Always `computer_use_call`.

        - `COMPUTER_USE_CALL("computer_use_call")`

    - `ComputerUseApprovalRequest`

      - `String id`

        The stable history item ID.

      - `Request request`

        A registered form awaiting the application's response.

        - `Optional<String> credentialOrigin`

          The registered form or frame origin where values will be entered.

        - `List<Field> fields`

          Controls to render. All submitted values are sensitive.

          - `String id`

            The field ID to submit as field_id in a fields entry.

          - `String label`

            The label to display beside the control.

          - `boolean required`

            Whether this control requires a nonempty value.

          - `String type`

            The rendering type, such as email, password, or text.

        - `List<Option> options`

          Sign-in methods. Empty for a plain form.

          - `String id`

            The option ID to submit as selected_option.

          - `List<String> fieldIds`

            IDs from the registered fields that this method accepts.

          - `String label`

            The method label to display.

        - `Optional<String> reason`

          Why the agent needs the user to sign in.

        - `JsonValue; type "browser_authentication"constant`

          The type of the object. Always `browser_authentication`.

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `String requestId`

      - `String turnId`

      - `JsonValue; type "computer_use_approval_request"constant`

        The item type. Always computer_use_approval_request.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `ComputerUseApprovalRequestResult`

      - `String id`

        The stable history item ID.

      - `String requestId`

        The registered request answered by this item.

      - `Response response`

        The admitted response, without submitted credential values.

        - `class Submit:`

          - `JsonValue; action "submit"constant`

            - `SUBMIT("submit")`

          - `Optional<String> selectedOption`

            The chosen sign-in method, or null when no options were offered.

          - `JsonValue; type "browser_authentication"constant`

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `JsonValue;`

          - `JsonValue; action "cancel"constant`

            - `CANCEL("cancel")`

          - `JsonValue; type "browser_authentication"constant`

            - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "computer_use_approval_request_result"constant`

        - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

    - `class AgentWebSearchCallItem:`

      A web search call produced by the agent.

      - `String id`

        The ID of the web search call.

      - `Optional<WebSearchAction> action`

        The action performed by the web search tool.

        - `Search`

          - `Optional<List<String>> queries`

            The search queries, when multiple queries were used.

          - `Optional<String> query`

            The search query, when a single query was used.

          - `JsonValue; type "search"constant`

            The type of the object. Always `search`.

            - `SEARCH("search")`

        - `OpenPage`

          - `JsonValue; type "open_page"constant`

            The type of the object. Always `open_page`.

            - `OPEN_PAGE("open_page")`

          - `Optional<String> url`

            The URL of the page that was opened.

        - `FindInPage`

          - `Optional<String> pattern`

            The text pattern that was searched for.

          - `JsonValue; type "find_in_page"constant`

            The type of the object. Always `find_in_page`.

            - `FIND_IN_PAGE("find_in_page")`

          - `Optional<String> url`

            The URL of the page that was searched.

        - `JsonValue;`

          - `JsonValue; type "other"constant`

            The type of the object. Always `other`.

            - `OTHER("other")`

      - `AgentOutputItemStatus status`

        The status of the web search call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "web_search_call"constant`

        The item type. Always `web_search_call`.

        - `WEB_SEARCH_CALL("web_search_call")`

    - `class AgentCommandExecutionItem:`

      A command execution produced by the agent.

      - `String id`

        The ID of the command execution item.

      - `String command`

        The command that was executed.

      - `Optional<String> cwd`

        The working directory used to execute the command.

      - `Optional<Long> durationMs`

        The command duration in milliseconds.

      - `Optional<Long> exitCode`

        The process exit code, if the command completed.

      - `Optional<String> output`

        The command output, if available.

      - `AgentFunctionCallStatus status`

        The status of the command execution.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "command_execution"constant`

        The item type. Always `command_execution`.

        - `COMMAND_EXECUTION("command_execution")`

    - `class AgentCreateSubagentCallItem:`

      A request to spawn a subagent.

      - `String id`

        The ID of the tool call item.

      - `String agentId`

        The ID of the agent that requested the subagent.

      - `List<AgentContent> content`

        The task given to the spawned agent.

        - `class OutputText:`

          A text content part produced by the agent.

        - `EncryptedContent`

      - `Optional<String> model`

        The model requested for the spawned agent.

      - `Optional<String> reasoningEffort`

        The reasoning effort requested for the spawned agent.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "create_subagent_call"constant`

        The item type. Always `create_subagent_call`.

        - `CREATE_SUBAGENT_CALL("create_subagent_call")`

          The current public item type.

    - `class AgentSendSubagentInputCallItem:`

      A request to send input to another agent.

      - `String id`

        The ID of the tool call item.

      - `List<AgentContent> content`

        The input sent to the receiving agent.

        - `class OutputText:`

          A text content part produced by the agent.

        - `EncryptedContent`

      - `String recipientAgentId`

        The ID of the agent receiving the input.

      - `String senderAgentId`

        The ID of the agent sending the input.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "send_subagent_input_call"constant`

        The item type. Always `send_subagent_input_call`.

        - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

          The current public item type.

    - `class AgentResumeSubagentCallItem:`

      A request to resume a subagent.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to resume.

      - `String senderAgentId`

        The ID of the agent requesting the resume.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "resume_subagent_call"constant`

        The item type. Always `resume_subagent_call`.

        - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem:`

      A request to wait for one or more subagents.

      - `String id`

        The ID of the tool call item.

      - `List<String> recipientAgentIds`

        The IDs of the agents to wait for.

      - `String senderAgentId`

        The ID of the agent waiting for results.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "wait_for_subagents_call"constant`

        The item type. Always `wait_for_subagents_call`.

        - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

          The current public item type.

    - `class AgentInterruptSubagentCallItem:`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to interrupt.

      - `String senderAgentId`

        The ID of the agent requesting the interrupt.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "interrupt_subagent_call"constant`

        The item type. Always `interrupt_subagent_call`.

        - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

          The current public item type.

    - `class AgentCloseSubagentCallItem:`

      A request to close a subagent.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to close.

      - `String senderAgentId`

        The ID of the agent requesting the close.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "close_subagent_call"constant`

        The item type. Always `close_subagent_call`.

        - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

          The current public item type.

  - `Optional<Long> outputIndex`

    The index of the item in the turn output, when the item is agent output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.item.added"constant`

    The type of the object. Always `agent.session.turn.item.added`.

    - `AGENT_SESSION_TURN_ITEM_ADDED("agent.session.turn.item.added")`

### Agent Session Turn Item Done Event

- `class AgentSessionTurnItemDoneEvent:`

  Emitted when an output item is complete.

  - `String eventId`

    The unique ID of the event.

  - `AgentOutputItem item`

    The completed output item.

    - `class AgentSessionAssistantMessage:`

      An assistant message produced by the agent.

      - `String id`

        The ID of the message.

      - `List<OutputText> content`

        The content of the message.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `Optional<Phase> phase`

        The phase of the assistant message.

        - `COMMENTARY("commentary")`

          Commentary produced while the agent works.

        - `FINAL_ANSWER("final_answer")`

          The agent's final answer.

      - `JsonValue; role "assistant"constant`

        The role of the message author. Always `assistant`.

        - `ASSISTANT("assistant")`

      - `AgentOutputItemStatus status`

        The status of the message.

        - `IN_PROGRESS("in_progress")`

          The item is in progress.

        - `COMPLETED("completed")`

          The item is complete.

        - `INCOMPLETE("incomplete")`

          The item stopped before completing.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "message"constant`

        The item type. Always `message`.

        - `MESSAGE("message")`

    - `class AgentReasoningItem:`

      A reasoning item produced by the agent.

      - `String id`

        The ID of the reasoning item.

      - `Optional<AgentOutputItemStatus> status`

        The status of the reasoning item.

      - `List<SummaryText> summary`

        The reasoning summaries produced by the agent.

        - `String text`

          The reasoning summary text.

        - `JsonValue; type "summary_text"constant`

          The content type. Always `summary_text`.

          - `SUMMARY_TEXT("summary_text")`

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "reasoning"constant`

        The item type. Always `reasoning`.

        - `REASONING("reasoning")`

    - `class AgentFunctionCallItem:`

      A function call produced by the agent.

      - `String id`

        The ID of the function call item.

      - `JsonValue arguments`

        The arguments to pass to the function.

      - `String callId`

        The ID used to submit the function result.

      - `String name`

        The name of the function to call.

      - `AgentFunctionCallStatus status`

        The status of the function call.

        - `IN_PROGRESS("in_progress")`

          The call is in progress.

        - `COMPLETED("completed")`

          The call completed successfully.

        - `FAILED("failed")`

          The call failed.

        - `INCOMPLETE("incomplete")`

          The call stopped before completing.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "function_call"constant`

        The item type. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class AgentMcpCallItem:`

      A call to a tool on an MCP server.

      - `String id`

        The ID of the MCP call item.

      - `JsonValue arguments`

        The arguments passed to the MCP tool.

      - `JsonValue error`

        The error returned by the MCP tool, if any.

      - `String name`

        The name of the MCP tool.

      - `JsonValue output`

        The output returned by the MCP tool, if any.

      - `String serverLabel`

        The label of the MCP server.

      - `AgentFunctionCallStatus status`

        The status of the MCP tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "mcp_call"constant`

        The item type. Always `mcp_call`.

        - `MCP_CALL("mcp_call")`

    - `ComputerUseCall`

      - `String id`

        The ID of the activity item.

      - `Optional<Output> output`

        The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

        - `String imageUrl`

          The complete JPEG image as a base64 data URL.

        - `JsonValue; type "computer_screenshot"constant`

          The content type. Always `computer_screenshot`.

          - `COMPUTER_SCREENSHOT("computer_screenshot")`

      - `AgentFunctionCallStatus status`

        The execution status of the activity.

      - `Optional<String> title`

        A model-generated description of the activity, when available.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "computer_use_call"constant`

        The item type. Always `computer_use_call`.

        - `COMPUTER_USE_CALL("computer_use_call")`

    - `ComputerUseApprovalRequest`

      - `String id`

        The stable history item ID.

      - `Request request`

        A registered form awaiting the application's response.

        - `Optional<String> credentialOrigin`

          The registered form or frame origin where values will be entered.

        - `List<Field> fields`

          Controls to render. All submitted values are sensitive.

          - `String id`

            The field ID to submit as field_id in a fields entry.

          - `String label`

            The label to display beside the control.

          - `boolean required`

            Whether this control requires a nonempty value.

          - `String type`

            The rendering type, such as email, password, or text.

        - `List<Option> options`

          Sign-in methods. Empty for a plain form.

          - `String id`

            The option ID to submit as selected_option.

          - `List<String> fieldIds`

            IDs from the registered fields that this method accepts.

          - `String label`

            The method label to display.

        - `Optional<String> reason`

          Why the agent needs the user to sign in.

        - `JsonValue; type "browser_authentication"constant`

          The type of the object. Always `browser_authentication`.

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `String requestId`

      - `String turnId`

      - `JsonValue; type "computer_use_approval_request"constant`

        The item type. Always computer_use_approval_request.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class AgentWebSearchCallItem:`

      A web search call produced by the agent.

      - `String id`

        The ID of the web search call.

      - `Optional<WebSearchAction> action`

        The action performed by the web search tool.

        - `Search`

          - `Optional<List<String>> queries`

            The search queries, when multiple queries were used.

          - `Optional<String> query`

            The search query, when a single query was used.

          - `JsonValue; type "search"constant`

            The type of the object. Always `search`.

            - `SEARCH("search")`

        - `OpenPage`

          - `JsonValue; type "open_page"constant`

            The type of the object. Always `open_page`.

            - `OPEN_PAGE("open_page")`

          - `Optional<String> url`

            The URL of the page that was opened.

        - `FindInPage`

          - `Optional<String> pattern`

            The text pattern that was searched for.

          - `JsonValue; type "find_in_page"constant`

            The type of the object. Always `find_in_page`.

            - `FIND_IN_PAGE("find_in_page")`

          - `Optional<String> url`

            The URL of the page that was searched.

        - `JsonValue;`

          - `JsonValue; type "other"constant`

            The type of the object. Always `other`.

            - `OTHER("other")`

      - `AgentOutputItemStatus status`

        The status of the web search call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "web_search_call"constant`

        The item type. Always `web_search_call`.

        - `WEB_SEARCH_CALL("web_search_call")`

    - `class AgentCommandExecutionItem:`

      A command execution produced by the agent.

      - `String id`

        The ID of the command execution item.

      - `String command`

        The command that was executed.

      - `Optional<String> cwd`

        The working directory used to execute the command.

      - `Optional<Long> durationMs`

        The command duration in milliseconds.

      - `Optional<Long> exitCode`

        The process exit code, if the command completed.

      - `Optional<String> output`

        The command output, if available.

      - `AgentFunctionCallStatus status`

        The status of the command execution.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "command_execution"constant`

        The item type. Always `command_execution`.

        - `COMMAND_EXECUTION("command_execution")`

    - `class AgentCreateSubagentCallItem:`

      A request to spawn a subagent.

      - `String id`

        The ID of the tool call item.

      - `String agentId`

        The ID of the agent that requested the subagent.

      - `List<AgentContent> content`

        The task given to the spawned agent.

        - `class OutputText:`

          A text content part produced by the agent.

          - `String text`

            The text produced by the agent.

          - `JsonValue; type "output_text"constant`

            The content type. Always `output_text`.

        - `EncryptedContent`

          - `String encryptedContent`

            The encrypted content payload.

          - `JsonValue; type "encrypted_content"constant`

            The content type. Always `encrypted_content`.

            - `ENCRYPTED_CONTENT("encrypted_content")`

      - `Optional<String> model`

        The model requested for the spawned agent.

      - `Optional<String> reasoningEffort`

        The reasoning effort requested for the spawned agent.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "create_subagent_call"constant`

        The item type. Always `create_subagent_call`.

        - `CREATE_SUBAGENT_CALL("create_subagent_call")`

          The current public item type.

    - `class AgentSendSubagentInputCallItem:`

      A request to send input to another agent.

      - `String id`

        The ID of the tool call item.

      - `List<AgentContent> content`

        The input sent to the receiving agent.

        - `class OutputText:`

          A text content part produced by the agent.

        - `EncryptedContent`

      - `String recipientAgentId`

        The ID of the agent receiving the input.

      - `String senderAgentId`

        The ID of the agent sending the input.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "send_subagent_input_call"constant`

        The item type. Always `send_subagent_input_call`.

        - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

          The current public item type.

    - `class AgentResumeSubagentCallItem:`

      A request to resume a subagent.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to resume.

      - `String senderAgentId`

        The ID of the agent requesting the resume.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "resume_subagent_call"constant`

        The item type. Always `resume_subagent_call`.

        - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

          The current public item type.

    - `class AgentWaitForSubagentsCallItem:`

      A request to wait for one or more subagents.

      - `String id`

        The ID of the tool call item.

      - `List<String> recipientAgentIds`

        The IDs of the agents to wait for.

      - `String senderAgentId`

        The ID of the agent waiting for results.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "wait_for_subagents_call"constant`

        The item type. Always `wait_for_subagents_call`.

        - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

          The current public item type.

    - `class AgentInterruptSubagentCallItem:`

      A request to interrupt a subagent's current turn. The subagent remains available.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to interrupt.

      - `String senderAgentId`

        The ID of the agent requesting the interrupt.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "interrupt_subagent_call"constant`

        The item type. Always `interrupt_subagent_call`.

        - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

          The current public item type.

    - `class AgentCloseSubagentCallItem:`

      A request to close a subagent.

      - `String id`

        The ID of the tool call item.

      - `String recipientAgentId`

        The ID of the agent to close.

      - `String senderAgentId`

        The ID of the agent requesting the close.

      - `AgentFunctionCallStatus status`

        The status of the tool call.

      - `String turnId`

        The ID of the turn that contains this item.

      - `JsonValue; type "close_subagent_call"constant`

        The item type. Always `close_subagent_call`.

        - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

          The current public item type.

  - `long outputIndex`

    The index of the output item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.item.done"constant`

    The type of the object. Always `agent.session.turn.item.done`.

    - `AGENT_SESSION_TURN_ITEM_DONE("agent.session.turn.item.done")`

### Agent Session Turn Output Text Delta Event

- `class AgentSessionTurnOutputTextDeltaEvent:`

  Emitted when text is appended to an output text content part.

  - `long contentIndex`

    The index of the content part in the message.

  - `String delta`

    The text that was appended.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the message item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.output_text.delta"constant`

    The type of the object. Always `agent.session.turn.output_text.delta`.

    - `AGENT_SESSION_TURN_OUTPUT_TEXT_DELTA("agent.session.turn.output_text.delta")`

### Agent Session Turn Output Text Done Event

- `class AgentSessionTurnOutputTextDoneEvent:`

  Emitted when an output text content part is complete.

  - `long contentIndex`

    The index of the content part in the message.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the message item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `String text`

    The complete output text.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.output_text.done"constant`

    The type of the object. Always `agent.session.turn.output_text.done`.

    - `AGENT_SESSION_TURN_OUTPUT_TEXT_DONE("agent.session.turn.output_text.done")`

### Agent Session Turn Reasoning Summary Part Added Event

- `class AgentSessionTurnReasoningSummaryPartAddedEvent:`

  Emitted when a reasoning summary content part is added.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the reasoning item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `SummaryText part`

    The initial summary part.

    - `String text`

      The reasoning summary text.

    - `JsonValue; type "summary_text"constant`

      The content type. Always `summary_text`.

      - `SUMMARY_TEXT("summary_text")`

  - `String sessionId`

    The ID of the session associated with the event.

  - `long summaryIndex`

    The index of the summary content part.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.reasoning_summary_part.added"constant`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

    - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_ADDED("agent.session.turn.reasoning_summary_part.added")`

### Agent Session Turn Reasoning Summary Part Done Event

- `class AgentSessionTurnReasoningSummaryPartDoneEvent:`

  Emitted when a reasoning summary part is complete.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the reasoning item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `SummaryText part`

    The completed summary part.

    - `String text`

      The reasoning summary text.

    - `JsonValue; type "summary_text"constant`

      The content type. Always `summary_text`.

      - `SUMMARY_TEXT("summary_text")`

  - `String sessionId`

    The ID of the session associated with the event.

  - `Optional<Status> status`

    Present as `incomplete` when summary generation was interrupted.

    - `INCOMPLETE("incomplete")`

  - `long summaryIndex`

    The index of the summary part.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.reasoning_summary_part.done"constant`

    The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

    - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_DONE("agent.session.turn.reasoning_summary_part.done")`

### Agent Session Turn Reasoning Summary Text Delta Event

- `class AgentSessionTurnReasoningSummaryTextDeltaEvent:`

  Emitted when text is appended to a reasoning summary.

  - `String delta`

    The summary text that was appended.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the reasoning item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `long summaryIndex`

    The index of the summary content part.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.reasoning_summary_text.delta"constant`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

    - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DELTA("agent.session.turn.reasoning_summary_text.delta")`

### Agent Session Turn Reasoning Summary Text Done Event

- `class AgentSessionTurnReasoningSummaryTextDoneEvent:`

  Emitted when a reasoning summary content part is complete.

  - `String eventId`

    The unique ID of the event.

  - `String itemId`

    The ID of the reasoning item.

  - `long outputIndex`

    The index of the item in the turn output.

  - `String sessionId`

    The ID of the session associated with the event.

  - `long summaryIndex`

    The index of the summary content part.

  - `String text`

    The complete reasoning summary text.

  - `Optional<String> turnId`

    The ID of the turn associated with the event, when applicable.

  - `JsonValue; type "agent.session.turn.reasoning_summary_text.done"constant`

    The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

    - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DONE("agent.session.turn.reasoning_summary_text.done")`

### Agent Text

- `class AgentText:`

  The text configuration used by an agent.

  - `TextFormat format`

    The effective output format. Defaults to ordinary text.

    - `JsonValue;`

      - `JsonValue; type "text"constant`

        The type of the object. Always `text`.

        - `TEXT("text")`

    - `JsonSchema`

      - `Schema schema`

        The JSON Schema that generated text must match.

      - `JsonValue; type "json_schema"constant`

        The type of the object. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Verbosity verbosity`

    The amount of text produced by the agent. Defaults to `medium`.

    - `LOW("low")`

    - `MEDIUM("medium")`

    - `HIGH("high")`

### Agent Text Param

- `class AgentTextParam:`

  Configuration for text generated by the agent.

  - `Optional<TextFormatParam> format`

    The output format. Omission uses ordinary text (`{"type": "text"}`).

    - `JsonValue;`

      - `JsonValue; type "text"constant`

        The type of the object. Always `text`.

        - `TEXT("text")`

    - `JsonSchema`

      - `Schema schema`

        The JSON Schema that generated text must match.

      - `JsonValue; type "json_schema"constant`

        The type of the object. Always `json_schema`.

        - `JSON_SCHEMA("json_schema")`

  - `Optional<Verbosity> verbosity`

    The amount of text the model should produce. Defaults to `medium`, matching Responses.

    - `LOW("low")`

      Produces less text.

    - `MEDIUM("medium")`

      Uses the default amount of text.

    - `HIGH("high")`

      Produces more text.

### Agent Tool

- `class AgentTool: A class that can be one of several variants.union`

  A tool available to the agent.

  - `Function`

    - `boolean deferLoading`

      Whether the function is deferred and discovered through tool search.

    - `String description`

      A description of what the function does.

    - `String name`

      The name of the function.

    - `Parameters parameters`

      A JSON Schema object describing the function's arguments.

    - `JsonValue; type "function"constant`

      The type of the object. Always `function`.

      - `FUNCTION("function")`

  - `ProgrammaticToolCalling`

    - `boolean enabled`

      Whether tools can be called from model-generated code.

    - `JsonValue; type "programmatic_tool_calling"constant`

      The type of the object. Always `programmatic_tool_calling`.

      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

  - `Mcp`

    - `Optional<List<String>> allowedTools`

      The MCP tools the agent may call.

    - `ConnectionOrigin connectionOrigin`

      Where outbound MCP HTTP connections originate.

      - `SERVICE("service")`

      - `ENVIRONMENT("environment")`

    - `Optional<String> credentialId`

      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

    - `RequestMetadata requestMetadata`

      Metadata included with requests to this MCP server.

    - `boolean required`

      Whether this MCP server must initialize before the first turn.

    - `String serverLabel`

      A label used to identify the MCP server in tool calls.

    - `McpTransport transport`

      The transport used to connect to the MCP server.

      - `Http`

        - `String serverUrl`

          The URL of the MCP server.

        - `JsonValue; type "http"constant`

          The type of the object. Always `http`.

          - `HTTP("http")`

      - `Stdio`

        - `List<String> args`

          Arguments passed to the MCP server command.

        - `String command`

          The command used to start the MCP server.

        - `String cwd`

          The working directory used to start the MCP server.

        - `List<String> envVars`

          Environment variable names inherited from the execution environment.

        - `JsonValue; type "stdio"constant`

          The type of the object. Always `stdio`.

          - `STDIO("stdio")`

    - `JsonValue; type "mcp"constant`

      The type of the object. Always `mcp`.

      - `MCP("mcp")`

  - `WebSearch`

    - `Optional<List<String>> allowedDomains`

      Allowed search domains, or `null` when the search is unrestricted.

    - `ContextSize contextSize`

      The amount of search context made available to the model. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

    - `Optional<Location> location`

      Approximate location used to localize search results, if provided.

      - `Optional<String> city`

        The city name.

      - `Optional<String> country`

        The two-letter ISO country code, such as `US`.

      - `Optional<String> region`

        The region or state name.

      - `Optional<String> timezone`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode mode`

      The source used for web search results.

      - `DISABLED("disabled")`

      - `CACHED("cached")`

      - `LIVE("live")`

    - `JsonValue; type "web_search"constant`

      The type of the object. Always `web_search`.

      - `WEB_SEARCH("web_search")`

  - `ComputerUse`

    - `boolean includeScreenshots`

      Whether computer tool outputs include screenshots.

    - `JsonValue; type "computer_use"constant`

      The type of the object. Always `computer_use`.

      - `COMPUTER_USE("computer_use")`

### Agent Tool Param

- `class AgentToolParam: A class that can be one of several variants.union`

  A tool available to the agent.

  - `Function`

    - `String description`

      A description of what the function does.

    - `String name`

      The name of the function.

    - `Parameters parameters`

      A JSON Schema object describing the function's arguments.

    - `JsonValue; type "function"constant`

      The type of the object. Always `function`.

      - `FUNCTION("function")`

    - `Optional<Boolean> deferLoading`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `JsonValue;`

    - `JsonValue; type "tool_search"constant`

      The type of the object. Always `tool_search`.

      - `TOOL_SEARCH("tool_search")`

  - `ProgrammaticToolCalling`

    - `JsonValue; type "programmatic_tool_calling"constant`

      The type of the object. Always `programmatic_tool_calling`.

      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Optional<Boolean> enabled`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `Mcp`

    - `String serverLabel`

      A label used to identify the MCP server in tool calls.

    - `McpTransportParam transport`

      The transport used to connect to the MCP server.

      - `Http`

        - `String serverUrl`

          The URL of the MCP server.

        - `JsonValue; type "http"constant`

          The type of the object. Always `http`.

          - `HTTP("http")`

        - `Optional<String> authorization`

          The authorization value sent to the MCP server, if any.

        - `Optional<Headers> headers`

          Additional HTTP headers sent to the MCP server.

      - `Stdio`

        - `String command`

          The command used to start the MCP server.

        - `String cwd`

          The working directory used to start the MCP server.

        - `JsonValue; type "stdio"constant`

          The type of the object. Always `stdio`.

          - `STDIO("stdio")`

        - `Optional<List<String>> args`

          Arguments passed to the MCP server command.

        - `Optional<Env> env`

          Environment variables set for the MCP server process.

        - `Optional<List<String>> envVars`

          Environment variable names to inherit from the selected execution environment.

    - `JsonValue; type "mcp"constant`

      The type of the object. Always `mcp`.

      - `MCP("mcp")`

    - `Optional<List<String>> allowedTools`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `Optional<ConnectionOrigin> connectionOrigin`

      Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

      - `SERVICE("service")`

        Uses the Managed Agents service network.

      - `ENVIRONMENT("environment")`

        Uses the session's execution environment.

    - `Optional<String> credentialId`

      The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

    - `Optional<RequestMetadata> requestMetadata`

      Metadata included with requests to this MCP server.

    - `Optional<Boolean> required`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `WebSearch`

    - `JsonValue; type "web_search"constant`

      The type of the object. Always `web_search`.

      - `WEB_SEARCH("web_search")`

    - `Optional<List<String>> allowedDomains`

      Domains the search may include.

    - `Optional<ContextSize> contextSize`

      The amount of search context made available to the model. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

    - `Optional<Location> location`

      Approximate location used to localize search results.

      - `Optional<String> city`

        The city name.

      - `Optional<String> country`

        The two-letter ISO country code, such as `US`.

      - `Optional<String> region`

        The region or state name.

      - `Optional<String> timezone`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Optional<Mode> mode`

      The source used for web search results. Defaults to `live`.

      - `DISABLED("disabled")`

        Disables web search.

      - `CACHED("cached")`

        Uses cached search results.

      - `LIVE("live")`

        Searches the live web.

  - `ComputerUse`

    - `JsonValue; type "computer_use"constant`

      The type of the object. Always `computer_use`.

      - `COMPUTER_USE("computer_use")`

    - `Optional<Boolean> includeScreenshots`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Agent Wait For Subagents Call Item

- `class AgentWaitForSubagentsCallItem:`

  A request to wait for one or more subagents.

  - `String id`

    The ID of the tool call item.

  - `List<String> recipientAgentIds`

    The IDs of the agents to wait for.

  - `String senderAgentId`

    The ID of the agent waiting for results.

  - `AgentFunctionCallStatus status`

    The status of the tool call.

    - `IN_PROGRESS("in_progress")`

      The call is in progress.

    - `COMPLETED("completed")`

      The call completed successfully.

    - `FAILED("failed")`

      The call failed.

    - `INCOMPLETE("incomplete")`

      The call stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "wait_for_subagents_call"constant`

    The item type. Always `wait_for_subagents_call`.

    - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

      The current public item type.

### Agent Web Search Call Item

- `class AgentWebSearchCallItem:`

  A web search call produced by the agent.

  - `String id`

    The ID of the web search call.

  - `Optional<WebSearchAction> action`

    The action performed by the web search tool.

    - `Search`

      - `Optional<List<String>> queries`

        The search queries, when multiple queries were used.

      - `Optional<String> query`

        The search query, when a single query was used.

      - `JsonValue; type "search"constant`

        The type of the object. Always `search`.

        - `SEARCH("search")`

    - `OpenPage`

      - `JsonValue; type "open_page"constant`

        The type of the object. Always `open_page`.

        - `OPEN_PAGE("open_page")`

      - `Optional<String> url`

        The URL of the page that was opened.

    - `FindInPage`

      - `Optional<String> pattern`

        The text pattern that was searched for.

      - `JsonValue; type "find_in_page"constant`

        The type of the object. Always `find_in_page`.

        - `FIND_IN_PAGE("find_in_page")`

      - `Optional<String> url`

        The URL of the page that was searched.

    - `JsonValue;`

      - `JsonValue; type "other"constant`

        The type of the object. Always `other`.

        - `OTHER("other")`

  - `AgentOutputItemStatus status`

    The status of the web search call.

    - `IN_PROGRESS("in_progress")`

      The item is in progress.

    - `COMPLETED("completed")`

      The item is complete.

    - `INCOMPLETE("incomplete")`

      The item stopped before completing.

  - `String turnId`

    The ID of the turn that contains this item.

  - `JsonValue; type "web_search_call"constant`

    The item type. Always `web_search_call`.

    - `WEB_SEARCH_CALL("web_search_call")`

### Environment

- `class Environment: A class that can be one of several variants.union`

  The execution environment for a session.

  - `JsonValue;`

    - `JsonValue; type "none"constant`

      The type of the object. Always `none`.

      - `NONE("none")`

  - `OpenAIHosted`

    - `String id`

      The public ID of the environment.

    - `List<String> capabilityDirectories`

      Directories that contain capabilities exposed to the agent.

    - `Desktop desktop`

      The effective desktop configuration.

      - `boolean enabled`

        Whether the environment provisions a desktop and browser proxy.

    - `List<HostedEnvironmentFile> files`

      Files available in the environment, excluding their contents.

      - `class HostedEnvironmentFileId:`

        A file copied from the OpenAI Files API.

        - `String id`

          The session-scoped ID of the file in the execution environment.

        - `String fileId`

          The ID of the uploaded file.

        - `String path`

          The file's absolute path inside the environment.

        - `long sizeBytes`

          The decoded file size in bytes.

        - `JsonValue; type "file_id"constant`

          The type of the object. Always `file_id`.

          - `FILE_ID("file_id")`

      - `Inline`

        - `String id`

          The session-scoped ID of the file in the execution environment.

        - `String path`

          The file's absolute path inside the environment.

        - `long sizeBytes`

          The decoded file size in bytes.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `Network network`

      The effective network access policy for the environment.

      - `Access access`

        The environment's network access mode.

        - `ENABLED("enabled")`

          Allows unrestricted network access.

        - `DISABLED("disabled")`

          Disables network access.

        - `RESTRICTED("restricted")`

          Applies the configured domain restrictions.

      - `List<String> allowedDomains`

        Domains the environment may access when network access is restricted.

    - `Packages packages`

      Packages installed in the environment.

      - `List<String> npm`

        npm packages installed globally in the environment.

      - `List<String> python`

        Python packages installed in the environment.

      - `List<String> system`

        System packages installed in the environment.

    - `List<HostedPlugin> plugins`

      Plugins installed in the environment, excluding their archive contents.

      - `String description`

        The installed plugin description.

      - `String name`

        The installed plugin name.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

    - `List<HostedSkill> skills`

      Skills installed in the environment, excluding their archive contents.

      - `class HostedSkillReference:`

        A skill installed from the Skills API.

        - `String description`

          The installed skill description.

        - `String name`

          The installed skill name.

        - `String skillId`

          The referenced skill ID.

        - `JsonValue; type "skill_reference"constant`

          The type of the object. Always `skill_reference`.

          - `SKILL_REFERENCE("skill_reference")`

        - `String version`

          The concrete skill version installed for this session.

      - `Inline`

        - `String description`

          The installed skill description.

        - `String name`

          The installed skill name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `JsonValue; type "openai_hosted"constant`

      The type of the object. Always `openai_hosted`.

      - `OPENAI_HOSTED("openai_hosted")`

    - `Optional<ContainerSize> containerSize`

      The effective CPU and memory tier, or null when unknown or outside the public tiers.

      - `SMALL("small")`

      - `MEDIUM("medium")`

      - `LARGE("large")`

  - `SelfHosted`

    - `String id`

      The public ID of the environment.

    - `List<String> capabilityDirectories`

      Directories that contain capabilities exposed to the agent.

    - `String remoteUrl`

      Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

    - `JsonValue; type "self_hosted"constant`

      The type of the object. Always `self_hosted`.

      - `SELF_HOSTED("self_hosted")`

    - `String workspaceDirectory`

      The absolute project directory inside the environment. Defaults to `/workspace`.

### Environment Param

- `class EnvironmentParam: A class that can be one of several variants.union`

  The execution environment and optional reusable template for a session.

  - `JsonValue;`

    - `JsonValue; type "none"constant`

      The type of the object. Always `none`.

      - `NONE("none")`

  - `OpenAIHosted`

    - `JsonValue; type "openai_hosted"constant`

      The type of the object. Always `openai_hosted`.

      - `OPENAI_HOSTED("openai_hosted")`

    - `Optional<List<String>> capabilityDirectories`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

    - `Optional<ContainerSize> containerSize`

      The hosted container size. Omission selects the medium tier.

      - `SMALL("small")`

      - `MEDIUM("medium")`

      - `LARGE("large")`

    - `Optional<Desktop> desktop`

      Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

      - `boolean enabled`

        Whether to provision the desktop and its browser proxy.

    - `Optional<Env> env`

      Environment variables made available to the agent.

    - `Optional<String> environmentTemplateId`

      A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

    - `Optional<List<HostedEnvironmentFileParam>> files`

      Files available before the agent starts. Defaults to an empty list.

      - `FileId`

        - `String fileId`

          The ID of the uploaded file.

        - `String path`

          The absolute destination path inside `/workspace`.

        - `JsonValue; type "file_id"constant`

          The type of the object. Always `file_id`.

          - `FILE_ID("file_id")`

      - `Inline`

        - `String data`

          The standard-base64-encoded file contents.

        - `String path`

          The absolute destination path inside `/workspace`.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `Optional<Network> network`

      Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

      - `Access access`

        The environment's network access mode.

        - `ENABLED("enabled")`

          Allows unrestricted network access.

        - `DISABLED("disabled")`

          Disables network access.

        - `RESTRICTED("restricted")`

          Applies the configured domain restrictions.

      - `Optional<List<String>> allowedDomains`

        Domains the environment may access when network access is restricted.

      - `Optional<List<String>> blockedDomains`

        Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

    - `Optional<Packages> packages`

      Packages to install in the environment. Defaults to empty package lists.

      - `Optional<List<String>> npm`

        npm packages to install globally. Defaults to an empty list.

      - `Optional<List<String>> python`

        Python packages to install. Defaults to an empty list.

      - `Optional<List<String>> system`

        System packages to install. Defaults to an empty list.

    - `Optional<List<HostedPluginParam>> plugins`

      Plugins provided as inline ZIP archives. Defaults to an empty list.

      - `String description`

        The plugin description declared in `.codex-plugin/plugin.json`.

      - `String name`

        The plugin name declared in `.codex-plugin/plugin.json`.

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

        - `String data`

          Standard-base64 encoded ZIP archive bytes.

        - `JsonValue; mediaType "application/zip"constant`

          The archive media type, always `application/zip`.

          - `APPLICATION_ZIP("application/zip")`

            A ZIP archive.

        - `JsonValue; type "base64"constant`

          The type of the object. Always `base64`.

          - `BASE64("base64")`

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

    - `Optional<List<SetupCommandParam>> setupCommands`

      Ordered, confidential setup commands. Command bodies are never returned.

      - `String command`

        The shell command to execute.

      - `Optional<String> cwd`

        The absolute working directory. Defaults to `/workspace`.

    - `Optional<List<HostedSkillParam>> skills`

      Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

      - `SkillReference`

        - `String skillId`

          The ID of the skill created through `/v1/skills`.

        - `JsonValue; type "skill_reference"constant`

          The type of the object. Always `skill_reference`.

          - `SKILL_REFERENCE("skill_reference")`

        - `Optional<String> version`

          The skill version, a positive integer or `latest`; omission selects the default.

      - `Inline`

        - `String description`

          The skill description declared in `SKILL.md`.

        - `String name`

          The skill name declared in `SKILL.md`.

        - `InlineCapabilitySourceParam source`

          Provides ZIP bytes encoded with standard base64.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

  - `SelfHosted`

    - `JsonValue; type "self_hosted"constant`

      The type of the object. Always `self_hosted`.

      - `SELF_HOSTED("self_hosted")`

    - `String workspaceDirectory`

      Absolute project directory inside the self-hosted environment.

    - `Optional<List<String>> capabilityDirectories`

      Directories that contain capabilities exposed to the agent. Defaults to an empty list.

### Hosted Environment File

- `class HostedEnvironmentFile: A class that can be one of several variants.union`

  Metadata for a file materialized in an OpenAI-hosted execution environment.

  - `class HostedEnvironmentFileId:`

    A file copied from the OpenAI Files API.

    - `String id`

      The session-scoped ID of the file in the execution environment.

    - `String fileId`

      The ID of the uploaded file.

    - `String path`

      The file's absolute path inside the environment.

    - `long sizeBytes`

      The decoded file size in bytes.

    - `JsonValue; type "file_id"constant`

      The type of the object. Always `file_id`.

      - `FILE_ID("file_id")`

  - `Inline`

    - `String id`

      The session-scoped ID of the file in the execution environment.

    - `String path`

      The file's absolute path inside the environment.

    - `long sizeBytes`

      The decoded file size in bytes.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

### Hosted Environment File ID

- `class HostedEnvironmentFileId:`

  A file copied from the OpenAI Files API.

  - `String id`

    The session-scoped ID of the file in the execution environment.

  - `String fileId`

    The ID of the uploaded file.

  - `String path`

    The file's absolute path inside the environment.

  - `long sizeBytes`

    The decoded file size in bytes.

  - `JsonValue; type "file_id"constant`

    The type of the object. Always `file_id`.

    - `FILE_ID("file_id")`

### Hosted Environment File Param

- `class HostedEnvironmentFileParam: A class that can be one of several variants.union`

  A file materialized in an OpenAI-hosted execution environment.

  - `FileId`

    - `String fileId`

      The ID of the uploaded file.

    - `String path`

      The absolute destination path inside `/workspace`.

    - `JsonValue; type "file_id"constant`

      The type of the object. Always `file_id`.

      - `FILE_ID("file_id")`

  - `Inline`

    - `String data`

      The standard-base64-encoded file contents.

    - `String path`

      The absolute destination path inside `/workspace`.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

### Hosted Plugin

- `class HostedPlugin:`

  A plugin installed from an inline ZIP archive.

  - `String description`

    The installed plugin description.

  - `String name`

    The installed plugin name.

  - `JsonValue; type "inline"constant`

    The type of the object. Always `inline`.

    - `INLINE("inline")`

### Hosted Plugin Param

- `class HostedPluginParam:`

  Supplies a plugin ZIP directly in the session request.

  - `String description`

    The plugin description declared in `.codex-plugin/plugin.json`.

  - `String name`

    The plugin name declared in `.codex-plugin/plugin.json`.

  - `InlineCapabilitySourceParam source`

    Provides ZIP bytes encoded with standard base64.

    - `String data`

      Standard-base64 encoded ZIP archive bytes.

    - `JsonValue; mediaType "application/zip"constant`

      The archive media type, always `application/zip`.

      - `APPLICATION_ZIP("application/zip")`

        A ZIP archive.

    - `JsonValue; type "base64"constant`

      The type of the object. Always `base64`.

      - `BASE64("base64")`

  - `JsonValue; type "inline"constant`

    The type of the object. Always `inline`.

    - `INLINE("inline")`

### Hosted Skill

- `class HostedSkill: A class that can be one of several variants.union`

  A skill installed in an OpenAI-hosted environment.

  - `class HostedSkillReference:`

    A skill installed from the Skills API.

    - `String description`

      The installed skill description.

    - `String name`

      The installed skill name.

    - `String skillId`

      The referenced skill ID.

    - `JsonValue; type "skill_reference"constant`

      The type of the object. Always `skill_reference`.

      - `SKILL_REFERENCE("skill_reference")`

    - `String version`

      The concrete skill version installed for this session.

  - `Inline`

    - `String description`

      The installed skill description.

    - `String name`

      The installed skill name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

### Hosted Skill Param

- `class HostedSkillParam: A class that can be one of several variants.union`

  A skill installed in an OpenAI-hosted environment.

  - `SkillReference`

    - `String skillId`

      The ID of the skill created through `/v1/skills`.

    - `JsonValue; type "skill_reference"constant`

      The type of the object. Always `skill_reference`.

      - `SKILL_REFERENCE("skill_reference")`

    - `Optional<String> version`

      The skill version, a positive integer or `latest`; omission selects the default.

  - `Inline`

    - `String description`

      The skill description declared in `SKILL.md`.

    - `String name`

      The skill name declared in `SKILL.md`.

    - `InlineCapabilitySourceParam source`

      Provides ZIP bytes encoded with standard base64.

      - `String data`

        Standard-base64 encoded ZIP archive bytes.

      - `JsonValue; mediaType "application/zip"constant`

        The archive media type, always `application/zip`.

        - `APPLICATION_ZIP("application/zip")`

          A ZIP archive.

      - `JsonValue; type "base64"constant`

        The type of the object. Always `base64`.

        - `BASE64("base64")`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

### Hosted Skill Reference

- `class HostedSkillReference:`

  A skill installed from the Skills API.

  - `String description`

    The installed skill description.

  - `String name`

    The installed skill name.

  - `String skillId`

    The referenced skill ID.

  - `JsonValue; type "skill_reference"constant`

    The type of the object. Always `skill_reference`.

    - `SKILL_REFERENCE("skill_reference")`

  - `String version`

    The concrete skill version installed for this session.

### Inline Capability Source Param

- `class InlineCapabilitySourceParam:`

  Provides ZIP bytes encoded with standard base64.

  - `String data`

    Standard-base64 encoded ZIP archive bytes.

  - `JsonValue; mediaType "application/zip"constant`

    The archive media type, always `application/zip`.

    - `APPLICATION_ZIP("application/zip")`

      A ZIP archive.

  - `JsonValue; type "base64"constant`

    The type of the object. Always `base64`.

    - `BASE64("base64")`

### Input Content

- `class InputContent: A class that can be one of several variants.union`

  User-provided content recorded in a session item.

  - `InputText`

    - `String text`

      The text supplied to the agent.

    - `JsonValue; type "input_text"constant`

      The type of the object. Always `input_text`.

      - `INPUT_TEXT("input_text")`

  - `InputImage`

    - `String imageUrl`

      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

    - `JsonValue; type "input_image"constant`

      The type of the object. Always `input_image`.

      - `INPUT_IMAGE("input_image")`

### Input Content Param

- `class InputContentParam: A class that can be one of several variants.union`

  Content included in an input message.

  - `InputText`

    - `String text`

      The text sent to the model.

    - `JsonValue; type "input_text"constant`

      The type of the object. Always `input_text`.

      - `INPUT_TEXT("input_text")`

  - `InputImage`

    - `String imageUrl`

      The URL of the image sent to the model.

    - `JsonValue; type "input_image"constant`

      The type of the object. Always `input_image`.

      - `INPUT_IMAGE("input_image")`

### Mcp Transport

- `class McpTransport: A class that can be one of several variants.union`

  The transport used to connect to an MCP server.

  - `Http`

    - `String serverUrl`

      The URL of the MCP server.

    - `JsonValue; type "http"constant`

      The type of the object. Always `http`.

      - `HTTP("http")`

  - `Stdio`

    - `List<String> args`

      Arguments passed to the MCP server command.

    - `String command`

      The command used to start the MCP server.

    - `String cwd`

      The working directory used to start the MCP server.

    - `List<String> envVars`

      Environment variable names inherited from the execution environment.

    - `JsonValue; type "stdio"constant`

      The type of the object. Always `stdio`.

      - `STDIO("stdio")`

### Mcp Transport Param

- `class McpTransportParam: A class that can be one of several variants.union`

  The transport used to connect to an MCP server.

  - `Http`

    - `String serverUrl`

      The URL of the MCP server.

    - `JsonValue; type "http"constant`

      The type of the object. Always `http`.

      - `HTTP("http")`

    - `Optional<String> authorization`

      The authorization value sent to the MCP server, if any.

    - `Optional<Headers> headers`

      Additional HTTP headers sent to the MCP server.

  - `Stdio`

    - `String command`

      The command used to start the MCP server.

    - `String cwd`

      The working directory used to start the MCP server.

    - `JsonValue; type "stdio"constant`

      The type of the object. Always `stdio`.

      - `STDIO("stdio")`

    - `Optional<List<String>> args`

      Arguments passed to the MCP server command.

    - `Optional<Env> env`

      Environment variables set for the MCP server process.

    - `Optional<List<String>> envVars`

      Environment variable names to inherit from the selected execution environment.

### Multi Agent Config

- `class MultiAgentConfig:`

  The resolved configuration for creating and coordinating subagents.

  - `boolean enabled`

    Whether subagent tools are enabled. Defaults to false.

  - `Optional<Long> maxConcurrentSubagents`

    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

### Multi Agent Config Param

- `class MultiAgentConfigParam:`

  Explicit configuration for creating and coordinating subagents.

  - `boolean enabled`

    Whether subagent tools are enabled.

  - `Optional<Long> maxConcurrentSubagents`

    Maximum number of subagents that may run concurrently. Defaults to 6.

### Output Text

- `class OutputText:`

  A text content part produced by the agent.

  - `String text`

    The text produced by the agent.

  - `JsonValue; type "output_text"constant`

    The content type. Always `output_text`.

    - `OUTPUT_TEXT("output_text")`

### Persisted Agent Tool

- `class PersistedAgentTool: A class that can be one of several variants.union`

  A credential-free tool available to a reusable agent.

  - `Function`

    - `boolean deferLoading`

      Whether the function is deferred and discovered through tool search.

    - `String description`

      A description of what the function does.

    - `String name`

      The name of the function.

    - `Parameters parameters`

      A JSON Schema object describing the function's arguments.

    - `JsonValue; type "function"constant`

      The type of the object. Always `function`.

      - `FUNCTION("function")`

  - `JsonValue;`

    - `JsonValue; type "tool_search"constant`

      The type of the object. Always `tool_search`.

      - `TOOL_SEARCH("tool_search")`

  - `ProgrammaticToolCalling`

    - `boolean enabled`

      Whether tools can be called from model-generated code.

    - `JsonValue; type "programmatic_tool_calling"constant`

      The type of the object. Always `programmatic_tool_calling`.

      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

  - `Mcp`

    - `Optional<List<String>> allowedTools`

      The MCP tools the agent may call, or null when all server tools are allowed.

    - `ConnectionOrigin connectionOrigin`

      Where outbound MCP HTTP connections originate.

      - `SERVICE("service")`

      - `ENVIRONMENT("environment")`

    - `Optional<String> credentialId`

      The vault credential selected for this MCP server, if any.

    - `RequestMetadata requestMetadata`

      Metadata included with requests to this MCP server.

    - `boolean required`

      Whether this MCP server must initialize before the first turn.

    - `String serverLabel`

      A label used to identify the MCP server in tool calls.

    - `PersistedMcpTransport transport`

      The credential-free transport used to connect to the MCP server.

      - `Http`

        - `Headers headers`

          Non-secret HTTP headers sent to the MCP server.

        - `String serverUrl`

          The URL of the MCP server.

        - `JsonValue; type "http"constant`

          The type of the object. Always `http`.

          - `HTTP("http")`

      - `Stdio`

        - `List<String> args`

          Arguments passed to the MCP server command.

        - `String command`

          The command used to start the MCP server.

        - `String cwd`

          The working directory used to start the MCP server.

        - `List<String> envVars`

          Environment variable names inherited from the execution environment.

        - `JsonValue; type "stdio"constant`

          The type of the object. Always `stdio`.

          - `STDIO("stdio")`

    - `JsonValue; type "mcp"constant`

      The type of the object. Always `mcp`.

      - `MCP("mcp")`

  - `WebSearch`

    - `Optional<List<String>> allowedDomains`

      Allowed search domains, or `null` when the search is unrestricted.

    - `ContextSize contextSize`

      The amount of search context made available to the model. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

    - `Optional<Location> location`

      Approximate location used to localize search results, if provided.

      - `Optional<String> city`

        The city name.

      - `Optional<String> country`

        The two-letter ISO country code, such as `US`.

      - `Optional<String> region`

        The region or state name.

      - `Optional<String> timezone`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Mode mode`

      The source used for web search results.

      - `DISABLED("disabled")`

      - `CACHED("cached")`

      - `LIVE("live")`

    - `JsonValue; type "web_search"constant`

      The type of the object. Always `web_search`.

      - `WEB_SEARCH("web_search")`

  - `ComputerUse`

    - `boolean includeScreenshots`

      Whether computer tool outputs include screenshots.

    - `JsonValue; type "computer_use"constant`

      The type of the object. Always `computer_use`.

      - `COMPUTER_USE("computer_use")`

### Persisted Agent Tool Param

- `class PersistedAgentToolParam: A class that can be one of several variants.union`

  A tool that can be stored on a reusable agent without session credentials.

  - `Function`

    - `String description`

      A description of what the function does.

    - `String name`

      The name of the function.

    - `Parameters parameters`

      A JSON Schema object describing the function's arguments.

    - `JsonValue; type "function"constant`

      The type of the object. Always `function`.

      - `FUNCTION("function")`

    - `Optional<Boolean> deferLoading`

      Whether this function is deferred and discovered through tool search. Defaults to `false`.

  - `JsonValue;`

    - `JsonValue; type "tool_search"constant`

      The type of the object. Always `tool_search`.

      - `TOOL_SEARCH("tool_search")`

  - `ProgrammaticToolCalling`

    - `JsonValue; type "programmatic_tool_calling"constant`

      The type of the object. Always `programmatic_tool_calling`.

      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Optional<Boolean> enabled`

      Whether tools can be called from model-generated code. Defaults to `true`.

  - `Mcp`

    - `String serverLabel`

      A label used to identify the MCP server in tool calls.

    - `PersistedMcpTransportParam transport`

      The credential-free transport used to connect to the MCP server.

      - `Http`

        - `String serverUrl`

          The URL of the MCP server.

        - `JsonValue; type "http"constant`

          The type of the object. Always `http`.

          - `HTTP("http")`

        - `Optional<Headers> headers`

          Non-secret HTTP headers sent to the MCP server.

      - `Stdio`

        - `String command`

          The command used to start the MCP server.

        - `String cwd`

          The working directory used to start the MCP server.

        - `JsonValue; type "stdio"constant`

          The type of the object. Always `stdio`.

          - `STDIO("stdio")`

        - `Optional<List<String>> args`

          Arguments passed to the MCP server command.

        - `Optional<List<String>> envVars`

          Environment variable names to inherit from the selected execution environment.

    - `JsonValue; type "mcp"constant`

      The type of the object. Always `mcp`.

      - `MCP("mcp")`

    - `Optional<List<String>> allowedTools`

      The MCP tools the agent may call. All server tools are allowed when omitted.

    - `Optional<ConnectionOrigin> connectionOrigin`

      Selects where outbound MCP HTTP connections originate.

      - `SERVICE("service")`

        Uses the Managed Agents service network.

      - `ENVIRONMENT("environment")`

        Uses the session's execution environment.

    - `Optional<String> credentialId`

      The vault credential selected for this MCP server. Optional when exactly one attached credential matches the server URL.

    - `Optional<RequestMetadata> requestMetadata`

      Metadata included with requests to this MCP server.

    - `Optional<Boolean> required`

      Whether this MCP server must initialize before the first turn. Defaults to `false`.

  - `WebSearch`

    - `JsonValue; type "web_search"constant`

      The type of the object. Always `web_search`.

      - `WEB_SEARCH("web_search")`

    - `Optional<List<String>> allowedDomains`

      Domains the search may include.

    - `Optional<ContextSize> contextSize`

      The amount of search context made available to the model. Defaults to `medium`.

      - `LOW("low")`

      - `MEDIUM("medium")`

      - `HIGH("high")`

    - `Optional<Location> location`

      Approximate location used to localize search results.

      - `Optional<String> city`

        The city name.

      - `Optional<String> country`

        The two-letter ISO country code, such as `US`.

      - `Optional<String> region`

        The region or state name.

      - `Optional<String> timezone`

        The IANA timezone, such as `America/Los_Angeles`.

    - `Optional<Mode> mode`

      The source used for web search results. Defaults to `live`.

      - `DISABLED("disabled")`

        Disables web search.

      - `CACHED("cached")`

        Uses cached search results.

      - `LIVE("live")`

        Searches the live web.

  - `ComputerUse`

    - `JsonValue; type "computer_use"constant`

      The type of the object. Always `computer_use`.

      - `COMPUTER_USE("computer_use")`

    - `Optional<Boolean> includeScreenshots`

      Whether computer tool outputs include screenshots. Defaults to `false`.

### Persisted Mcp Transport

- `class PersistedMcpTransport: A class that can be one of several variants.union`

  A credential-free transport used to connect to an MCP server.

  - `Http`

    - `Headers headers`

      Non-secret HTTP headers sent to the MCP server.

    - `String serverUrl`

      The URL of the MCP server.

    - `JsonValue; type "http"constant`

      The type of the object. Always `http`.

      - `HTTP("http")`

  - `Stdio`

    - `List<String> args`

      Arguments passed to the MCP server command.

    - `String command`

      The command used to start the MCP server.

    - `String cwd`

      The working directory used to start the MCP server.

    - `List<String> envVars`

      Environment variable names inherited from the execution environment.

    - `JsonValue; type "stdio"constant`

      The type of the object. Always `stdio`.

      - `STDIO("stdio")`

### Persisted Mcp Transport Param

- `class PersistedMcpTransportParam: A class that can be one of several variants.union`

  A credential-free transport used to connect to an MCP server.

  - `Http`

    - `String serverUrl`

      The URL of the MCP server.

    - `JsonValue; type "http"constant`

      The type of the object. Always `http`.

      - `HTTP("http")`

    - `Optional<Headers> headers`

      Non-secret HTTP headers sent to the MCP server.

  - `Stdio`

    - `String command`

      The command used to start the MCP server.

    - `String cwd`

      The working directory used to start the MCP server.

    - `JsonValue; type "stdio"constant`

      The type of the object. Always `stdio`.

      - `STDIO("stdio")`

    - `Optional<List<String>> args`

      Arguments passed to the MCP server command.

    - `Optional<List<String>> envVars`

      Environment variable names to inherit from the selected execution environment.

### Session Error

- `class SessionError:`

  An error payload with the same public fields as Responses API streaming errors.

  - `Optional<String> code`

    The machine-readable error code, if any.

  - `String message`

    A customer-safe explanation of the error.

  - `Optional<String> param`

    The request parameter associated with the error, if any.

  - `String type`

    The error type.

### Session Turn Error

- `class SessionTurnError:`

  A customer-safe error describing why a session request failed.

  - `Code code`

    A stable, machine-readable failure category.

    - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

      The request exceeds the model's context window.

    - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

      The session has reached its usage budget.

    - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

      The organization has reached a usage, plan, or billing limit.

    - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

      The organization has no API credits remaining.

    - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

      The request exceeds the available rate limit.

    - `FLEX_UNAVAILABLE("flex_unavailable")`

      Flex processing is temporarily unavailable.

    - `SERVER_OVERLOADED("server_overloaded")`

      The model service is temporarily overloaded.

    - `CYBER_POLICY("cyber_policy")`

      The request was rejected by a safety policy.

    - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

      The request was blocked by the safety systems.

    - `CONNECTION_FAILED("connection_failed")`

      The request could not connect to the model service.

    - `SERVER_ERROR("server_error")`

      The model service encountered an unexpected error.

    - `AUTHENTICATION_ERROR("authentication_error")`

      The API credentials are invalid or lack the required access.

    - `INVALID_REQUEST("invalid_request")`

      The request contains invalid input or configuration.

    - `RESOURCE_NOT_FOUND("resource_not_found")`

      The requested model or resource is unavailable.

    - `SANDBOX_ERROR("sandbox_error")`

      The request could not complete in its execution environment.

    - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

      The executor must be upgraded before it can run this turn.

    - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

      The session cannot accept additional input while a request is running.

    - `REQUEST_TIMEOUT("request_timeout")`

      The request timed out before the model service responded.

    - `INTERNAL_ERROR("internal_error")`

      An unexpected internal error prevented the session request from completing.

  - `String message`

    A customer-safe explanation of the failure.

### Setup Command Param

- `class SetupCommandParam:`

  A confidential setup command executed before the hosted agent starts.

  - `String command`

    The shell command to execute.

  - `Optional<String> cwd`

    The absolute working directory. Defaults to `/workspace`.

### Subagent

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `Optional<String> name`

    The runner-assigned nickname, or null when unavailable.

  - `Object object_`

    The object type. Always `agent.session.subagent`.

    - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

  - `long openedAt`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `String parentAgentId`

    The ID of the agent that created this subagent.

  - `String sessionId`

    The ID of the session that owns the subagent.

  - `Status status`

    The current status of the subagent.

    - `ACTIVE("active")`

      The subagent remains available, including while idle between turns.

    - `CLOSED("closed")`

      The subagent is closed.

### Summary Text

- `class SummaryText:`

  A reasoning summary content part.

  - `String text`

    The reasoning summary text.

  - `JsonValue; type "summary_text"constant`

    The content type. Always `summary_text`.

    - `SUMMARY_TEXT("summary_text")`

### Text Format

- `class TextFormat: A class that can be one of several variants.union`

  The effective output format for generated text.

  - `JsonValue;`

    - `JsonValue; type "text"constant`

      The type of the object. Always `text`.

      - `TEXT("text")`

  - `JsonSchema`

    - `Schema schema`

      The JSON Schema that generated text must match.

    - `JsonValue; type "json_schema"constant`

      The type of the object. Always `json_schema`.

      - `JSON_SCHEMA("json_schema")`

### Text Format Param

- `class TextFormatParam: A class that can be one of several variants.union`

  The output format for generated text.

  - `JsonValue;`

    - `JsonValue; type "text"constant`

      The type of the object. Always `text`.

      - `TEXT("text")`

  - `JsonSchema`

    - `Schema schema`

      The JSON Schema that generated text must match.

    - `JsonValue; type "json_schema"constant`

      The type of the object. Always `json_schema`.

      - `JSON_SCHEMA("json_schema")`

### Token Usage

- `class TokenUsage:`

  Recorded token usage for a session or turn. Usage is best effort and may change.

  - `long inputTokens`

    The number of input tokens used by the agent.

  - `InputTokensDetails inputTokensDetails`

    A breakdown of the agent's input token usage.

    - `long cachedTokens`

      The number of input tokens retrieved from the prompt cache.

  - `long outputTokens`

    The number of output tokens generated by the agent.

  - `OutputTokensDetails outputTokensDetails`

    A breakdown of the agent's output token usage.

    - `long reasoningTokens`

      The number of output tokens used for reasoning.

  - `long totalTokens`

    The total number of input and output tokens used by the agent.

### Web Search Action

- `class WebSearchAction: A class that can be one of several variants.union`

  An action performed by the web search tool.

  - `Search`

    - `Optional<List<String>> queries`

      The search queries, when multiple queries were used.

    - `Optional<String> query`

      The search query, when a single query was used.

    - `JsonValue; type "search"constant`

      The type of the object. Always `search`.

      - `SEARCH("search")`

  - `OpenPage`

    - `JsonValue; type "open_page"constant`

      The type of the object. Always `open_page`.

      - `OPEN_PAGE("open_page")`

    - `Optional<String> url`

      The URL of the page that was opened.

  - `FindInPage`

    - `Optional<String> pattern`

      The text pattern that was searched for.

    - `JsonValue; type "find_in_page"constant`

      The type of the object. Always `find_in_page`.

      - `FIND_IN_PAGE("find_in_page")`

    - `Optional<String> url`

      The URL of the page that was searched.

  - `JsonValue;`

    - `JsonValue; type "other"constant`

      The type of the object. Always `other`.

      - `OTHER("other")`

# Environments

## Retrieve an agent environment

`EnvironmentInfo beta().agents().environments().retrieve(EnvironmentRetrieveParamsparams = EnvironmentRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}`

Retrieves an execution environment's connection status and safe installed metadata. See [environment lifecycle](/api/docs/guides/agents-api/environments/lifecycle).

### Parameters

- `EnvironmentRetrieveParams params`

  - `Optional<String> environmentId`

### Returns

- `class EnvironmentInfo:`

  Safe metadata for a first-class execution environment.

  - `String id`

    The ID of the environment.

  - `List<HostedEnvironmentFile> files`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileId:`

      A file copied from the OpenAI Files API.

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `JsonValue; object_ "agent.environment"constant`

    The object type. Always `agent.environment`.

    - `AGENT_ENVIRONMENT("agent.environment")`

  - `List<HostedPlugin> plugins`

    Plugins installed in the environment, without their archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<HostedSkill> skills`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference:`

      A skill installed from the Skills API.

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `String version`

        The concrete skill version installed for this session.

    - `Inline`

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Status status`

    The current environment connection status.

    - `PENDING("pending")`

    - `CONNECTED("connected")`

    - `DISCONNECTED("disconnected")`

    - `EXPIRED("expired")`

    - `FAILED("failed")`

  - `Type type`

    Whether the environment is hosted by OpenAI or by the application.

    - `OPENAI_HOSTED("openai_hosted")`

    - `SELF_HOSTED("self_hosted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.EnvironmentInfo;
import com.openai.models.beta.agents.environments.EnvironmentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentInfo environmentInfo = client.beta().agents().environments().retrieve("environment_id");
    }
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

- `class EnvironmentInfo:`

  Safe metadata for a first-class execution environment.

  - `String id`

    The ID of the environment.

  - `List<HostedEnvironmentFile> files`

    Files installed in the environment, without their contents.

    - `class HostedEnvironmentFileId:`

      A file copied from the OpenAI Files API.

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String id`

        The session-scoped ID of the file in the execution environment.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded file size in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `JsonValue; object_ "agent.environment"constant`

    The object type. Always `agent.environment`.

    - `AGENT_ENVIRONMENT("agent.environment")`

  - `List<HostedPlugin> plugins`

    Plugins installed in the environment, without their archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<HostedSkill> skills`

    Skills installed in the environment, without their archive contents.

    - `class HostedSkillReference:`

      A skill installed from the Skills API.

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `String version`

        The concrete skill version installed for this session.

    - `Inline`

      - `String description`

        The installed skill description.

      - `String name`

        The installed skill name.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Status status`

    The current environment connection status.

    - `PENDING("pending")`

    - `CONNECTED("connected")`

    - `DISCONNECTED("disconnected")`

    - `EXPIRED("expired")`

    - `FAILED("failed")`

  - `Type type`

    Whether the environment is hosted by OpenAI or by the application.

    - `OPENAI_HOSTED("openai_hosted")`

    - `SELF_HOSTED("self_hosted")`

# Files

## Create an agent environment file

`EnvironmentFile beta().agents().environments().files().create(FileCreateParamsparams = FileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/{environment_id}/files`

Copies inline bytes or a Files API file into a connected execution environment. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `FileCreateParams params`

  - `Optional<String> environmentId`

  - `Optional<HostedEnvironmentFileParam> hostedEnvironmentFileParam`

    A file materialized in an OpenAI-hosted execution environment.

### Returns

- `class EnvironmentFile:`

  A live file in an execution environment.

  - `String environmentId`

    The ID of the environment containing this file.

  - `JsonValue; object_ "agent.environment.file"constant`

    The object type. Always `agent.environment.file`.

    - `AGENT_ENVIRONMENT_FILE("agent.environment.file")`

  - `String path`

    The absolute file path inside the environment's workspace.

  - `long sizeBytes`

    The file size in bytes.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.files.EnvironmentFile;
import com.openai.models.beta.agents.environments.files.FileCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentFile environmentFile = client.beta().agents().environments().files().create("environment_id");
    }
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

`FileListPage beta().agents().environments().files().list(FileListParamsparams = FileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/{environment_id}/files`

Lists live files on a connected execution environment with optional directory filtering and opaque cursor pagination. See [environment files](/api/docs/guides/agents-api/environments/files).

### Parameters

- `FileListParams params`

  - `Optional<String> environmentId`

  - `Optional<Long> limit`

    The maximum number of files to return, between 1 and 100.

  - `Optional<Order> order`

    Sort by case-sensitive path components. Defaults to descending.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<String> page`

    The opaque token from the previous page. Keep the same path, order, and limit.

  - `Optional<String> path`

    Restrict the listing to this absolute workspace directory.

### Returns

- `class EnvironmentFile:`

  A live file in an execution environment.

  - `String environmentId`

    The ID of the environment containing this file.

  - `JsonValue; object_ "agent.environment.file"constant`

    The object type. Always `agent.environment.file`.

    - `AGENT_ENVIRONMENT_FILE("agent.environment.file")`

  - `String path`

    The absolute file path inside the environment's workspace.

  - `long sizeBytes`

    The file size in bytes.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.files.FileListPage;
import com.openai.models.beta.agents.environments.files.FileListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        FileListPage page = client.beta().agents().environments().files().list("environment_id");
    }
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

- `class EnvironmentFile:`

  A live file in an execution environment.

  - `String environmentId`

    The ID of the environment containing this file.

  - `JsonValue; object_ "agent.environment.file"constant`

    The object type. Always `agent.environment.file`.

    - `AGENT_ENVIRONMENT_FILE("agent.environment.file")`

  - `String path`

    The absolute file path inside the environment's workspace.

  - `long sizeBytes`

    The file size in bytes.

# Templates

## Create an agent environment template

`EnvironmentTemplate beta().agents().environments().templates().create(TemplateCreateParamsparams = TemplateCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/templates`

Creates reusable environment configuration without returning confidential setup commands or environment values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateCreateParams params`

  - `Optional<List<String>> capabilityDirectories`

    Directories that contain capabilities exposed to the agent. Defaults to an empty list.

  - `Optional<Desktop> desktop`

    Desktop provisioning. Omission or null inherits the template setting, or defaults to disabled.

    - `boolean enabled`

      Whether to provision the desktop and its browser proxy.

  - `Optional<Env> env`

    Environment variables made available to the agent.

  - `Optional<List<HostedEnvironmentFileParam>> files`

    Files available before the agent starts. Defaults to an empty list.

    - `FileId`

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String data`

        The standard-base64-encoded file contents.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Optional<Network> network`

    Network access policy for the environment. Defaults to disabled for GA requests and enabled for beta requests.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `Optional<List<String>> allowedDomains`

      Domains the environment may access when network access is restricted.

    - `Optional<List<String>> blockedDomains`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Optional<Packages> packages`

    Packages to install in the environment. Defaults to empty package lists.

    - `Optional<List<String>> npm`

      npm packages to install globally. Defaults to an empty list.

    - `Optional<List<String>> python`

      Python packages to install. Defaults to an empty list.

    - `Optional<List<String>> system`

      System packages to install. Defaults to an empty list.

  - `Optional<List<HostedPluginParam>> plugins`

    Plugins provided as inline ZIP archives. Defaults to an empty list.

    - `String description`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `String name`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `InlineCapabilitySourceParam source`

      Provides ZIP bytes encoded with standard base64.

      - `String data`

        Standard-base64 encoded ZIP archive bytes.

      - `JsonValue; mediaType "application/zip"constant`

        The archive media type, always `application/zip`.

        - `APPLICATION_ZIP("application/zip")`

          A ZIP archive.

      - `JsonValue; type "base64"constant`

        The type of the object. Always `base64`.

        - `BASE64("base64")`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `Optional<List<SetupCommandParam>> setupCommands`

    Ordered, confidential setup commands. Command bodies are never returned.

    - `String command`

      The shell command to execute.

    - `Optional<String> cwd`

      The absolute working directory. Defaults to `/workspace`.

  - `Optional<List<HostedSkillParam>> skills`

    Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

    - `SkillReference`

      - `String skillId`

        The ID of the skill created through `/v1/skills`.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `Inline`

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().create();
    }
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

`EnvironmentTemplateDeleted beta().agents().environments().templates().delete(TemplateDeleteParamsparams = TemplateDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/environments/templates/{environment_template_id}`

Deletes reusable environment configuration and all confidential template inputs. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateDeleteParams params`

  - `Optional<String> environmentTemplateId`

### Returns

- `class EnvironmentTemplateDeleted:`

  A deleted reusable environment template.

  - `String id`

    The ID of the deleted environment template.

  - `boolean deleted`

    Whether the environment template was deleted. Always `true`.

  - `JsonValue; object_ "agent.environment.template.deleted"constant`

    The object type. Always `agent.environment.template.deleted`.

    - `AGENT_ENVIRONMENT_TEMPLATE_DELETED("agent.environment.template.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplateDeleted;
import com.openai.models.beta.agents.environments.templates.TemplateDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplateDeleted environmentTemplateDeleted = client.beta().agents().environments().templates().delete("environment_template_id");
    }
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

`TemplateListPage beta().agents().environments().templates().list(TemplateListParamsparams = TemplateListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/templates`

Lists reusable environment templates without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.TemplateListPage;
import com.openai.models.beta.agents.environments.templates.TemplateListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TemplateListPage page = client.beta().agents().environments().templates().list();
    }
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

`EnvironmentTemplate beta().agents().environments().templates().retrieve(TemplateRetrieveParamsparams = TemplateRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/environments/templates/{environment_template_id}`

Retrieves reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateRetrieveParams params`

  - `Optional<String> environmentTemplateId`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().retrieve("environment_template_id");
    }
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

`EnvironmentTemplate beta().agents().environments().templates().update(TemplateUpdateParamsparams = TemplateUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/environments/templates/{environment_template_id}`

Updates reusable environment configuration without returning confidential values. See [reusing a hosted setup](/api/docs/guides/agents-api/tools#reuse-a-hosted-plugin-setup).

### Parameters

- `TemplateUpdateParams params`

  - `Optional<String> environmentTemplateId`

  - `Optional<List<String>> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `Optional<Desktop> desktop`

    Replacement desktop configuration, or null to disable the desktop.

    - `boolean enabled`

      Whether to provision the desktop and its browser proxy.

  - `Optional<Env> env`

    Replacement confidential environment values.

  - `Optional<List<HostedEnvironmentFileParam>> files`

    Replacement file configuration materialized for each new session.

    - `FileId`

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `Inline`

      - `String data`

        The standard-base64-encoded file contents.

      - `String path`

        The absolute destination path inside `/workspace`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    A replacement human-readable display name, or `null` to clear the name.

  - `Optional<Network> network`

    Network access available after setup completes. Omit to preserve the current policy, or pass `null` to reset to disabled for GA requests or enabled for beta requests.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `Optional<List<String>> allowedDomains`

      Domains the environment may access when network access is restricted.

    - `Optional<List<String>> blockedDomains`

      Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

  - `Optional<Packages> packages`

    Packages installed before the runtime network policy applies.

    - `Optional<List<String>> npm`

      npm packages to install globally. Defaults to an empty list.

    - `Optional<List<String>> python`

      Python packages to install. Defaults to an empty list.

    - `Optional<List<String>> system`

      System packages to install. Defaults to an empty list.

  - `Optional<List<HostedPluginParam>> plugins`

    Replacement plugin configuration installed for each new session.

    - `String description`

      The plugin description declared in `.codex-plugin/plugin.json`.

    - `String name`

      The plugin name declared in `.codex-plugin/plugin.json`.

    - `InlineCapabilitySourceParam source`

      Provides ZIP bytes encoded with standard base64.

      - `String data`

        Standard-base64 encoded ZIP archive bytes.

      - `JsonValue; mediaType "application/zip"constant`

        The archive media type, always `application/zip`.

        - `APPLICATION_ZIP("application/zip")`

          A ZIP archive.

      - `JsonValue; type "base64"constant`

        The type of the object. Always `base64`.

        - `BASE64("base64")`

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `Optional<List<SetupCommandParam>> setupCommands`

    Replacement confidential setup commands, never included in returned resources.

    - `String command`

      The shell command to execute.

    - `Optional<String> cwd`

      The absolute working directory. Defaults to `/workspace`.

  - `Optional<List<HostedSkillParam>> skills`

    Replacement skill configuration installed for each new session.

    - `SkillReference`

      - `String skillId`

        The ID of the skill created through `/v1/skills`.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The skill version, a positive integer or `latest`; omission selects the default.

    - `Inline`

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `InlineCapabilitySourceParam source`

        Provides ZIP bytes encoded with standard base64.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

### Returns

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.environments.templates.EnvironmentTemplate;
import com.openai.models.beta.agents.environments.templates.TemplateUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EnvironmentTemplate environmentTemplate = client.beta().agents().environments().templates().update("environment_template_id");
    }
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

- `class EnvironmentTemplate:`

  Reusable configuration that provisions a fresh OpenAI-hosted environment for each session.

  - `String id`

    The ID of the reusable environment template.

  - `List<String> capabilityDirectories`

    Directories that expose capabilities to the agent.

  - `long createdAt`

    The Unix timestamp, in seconds, when the template was created.

  - `Desktop desktop`

    Desktop configuration for each OpenAI-hosted environment.

    - `boolean enabled`

      Whether the environment provisions a desktop and browser proxy.

  - `List<File> files`

    Safe file metadata, excluding contents and session-scoped file IDs.

    - `class FileId:`

      A project-scoped Files API reference resolved separately for each session.

      - `String fileId`

        The ID of the uploaded file.

      - `String path`

        The file's absolute path inside the environment.

      - `JsonValue; type "file_id"constant`

        The type of the object. Always `file_id`.

        - `FILE_ID("file_id")`

    - `class Inline:`

      Metadata for confidential inline file contents.

      - `String path`

        The file's absolute path inside the environment.

      - `long sizeBytes`

        The decoded size of the inline file in bytes.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `Optional<String> name`

    An optional human-readable display name for the template.

  - `Network network`

    Runtime network access for each OpenAI-hosted environment.

    - `Access access`

      The environment's network access mode.

      - `ENABLED("enabled")`

        Allows unrestricted network access.

      - `DISABLED("disabled")`

        Disables network access.

      - `RESTRICTED("restricted")`

        Applies the configured domain restrictions.

    - `List<String> allowedDomains`

      Domains the environment may access when network access is restricted.

  - `JsonValue; object_ "agent.environment.template"constant`

    The object type. Always `agent.environment.template`.

    - `AGENT_ENVIRONMENT_TEMPLATE("agent.environment.template")`

  - `Packages packages`

    Packages installed in each fresh OpenAI-hosted environment.

    - `List<String> npm`

      npm packages installed globally in the environment.

    - `List<String> python`

      Python packages installed in the environment.

    - `List<String> system`

      System packages installed in the environment.

  - `List<HostedPlugin> plugins`

    Safe plugin metadata, excluding inline archive contents.

    - `String description`

      The installed plugin description.

    - `String name`

      The installed plugin name.

    - `JsonValue; type "inline"constant`

      The type of the object. Always `inline`.

      - `INLINE("inline")`

  - `List<Skill> skills`

    Safe skill metadata, preserving unresolved version selectors.

    - `class SkillReference:`

      A skill resolved afresh from the Skills API whenever a session starts.

      - `String skillId`

        The referenced skill ID.

      - `JsonValue; type "skill_reference"constant`

        The type of the object. Always `skill_reference`.

        - `SKILL_REFERENCE("skill_reference")`

      - `Optional<String> version`

        The requested version selector, including `latest`.

    - `class Inline:`

      Safe metadata for an inline skill archive.

      - `String description`

        The skill description declared in `SKILL.md`.

      - `String name`

        The skill name declared in `SKILL.md`.

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the template was last updated.

### Environment Template Deleted

- `class EnvironmentTemplateDeleted:`

  A deleted reusable environment template.

  - `String id`

    The ID of the deleted environment template.

  - `boolean deleted`

    Whether the environment template was deleted. Always `true`.

  - `JsonValue; object_ "agent.environment.template.deleted"constant`

    The object type. Always `agent.environment.template.deleted`.

    - `AGENT_ENVIRONMENT_TEMPLATE_DELETED("agent.environment.template.deleted")`

# Sessions

## Create an agent session

`AgentSession beta().agents().sessions().create(SessionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/sessions`

Creates a managed agent session, optionally submits initial input, and returns the session or streams its events when stream is true. See [running sessions](/api/docs/guides/agents-api/sessions).

### Parameters

- `SessionCreateParams params`

  - `EnvironmentParam environment`

    An inline execution environment or a reference to an environment template.

  - `Optional<Agent> agent`

    Agent configuration. With `agent_id`, supplied fields override the saved agent for this session. Without `agent_id`, `model` is required.

    - `Optional<String> instructions`

      Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

    - `Optional<String> model`

      The model to use for the agent. The requested model name is preserved.

    - `Optional<MultiAgentConfigParam> multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently. Defaults to 6.

    - `Optional<AgentReasoningParam> reasoning`

      Configuration for model reasoning. Omit to keep the current settings; pass `null` to reset to the model's default effort.

      - `Optional<Effort> effort`

        The amount of reasoning effort the model should use. Omission lets the model select it.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        Controls whether the response includes a reasoning summary.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `Optional<ServiceTier> serviceTier`

      The service tier used for model requests.

      - `AUTO("auto")`

        Selects the service tier automatically.

      - `DEFAULT("default")`

        Uses the default service tier.

      - `FLEX("flex")`

        Uses the flex service tier.

      - `PRIORITY("priority")`

        Uses the priority service tier.

      - `FAST("fast")`

        Uses the fast service tier.

      - `ULTRAFAST("ultrafast")`

        Uses the ultrafast service tier.

    - `Optional<AgentTextParam> text`

      Configuration for text generated by the agent.

      - `Optional<TextFormatParam> format`

        The output format. Omission uses ordinary text (`{"type": "text"}`).

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Optional<Verbosity> verbosity`

        The amount of text the model should produce. Defaults to `medium`, matching Responses.

        - `LOW("low")`

          Produces less text.

        - `MEDIUM("medium")`

          Uses the default amount of text.

        - `HIGH("high")`

          Produces more text.

    - `Optional<List<AgentToolParam>> tools`

      Tools available to the agent. Omit to inherit, or pass null to clear them.

      - `Function`

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

        - `Optional<Boolean> deferLoading`

          Whether this function is deferred and discovered through tool search. Defaults to `false`.

      - `JsonValue;`

        - `JsonValue; type "tool_search"constant`

          The type of the object. Always `tool_search`.

          - `TOOL_SEARCH("tool_search")`

      - `ProgrammaticToolCalling`

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Optional<Boolean> enabled`

          Whether tools can be called from model-generated code. Defaults to `true`.

      - `Mcp`

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransportParam transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

            - `Optional<String> authorization`

              The authorization value sent to the MCP server, if any.

            - `Optional<Headers> headers`

              Additional HTTP headers sent to the MCP server.

          - `Stdio`

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

            - `Optional<List<String>> args`

              Arguments passed to the MCP server command.

            - `Optional<Env> env`

              Environment variables set for the MCP server process.

            - `Optional<List<String>> envVars`

              Environment variable names to inherit from the selected execution environment.

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call. All server tools are allowed when omitted.

        - `Optional<ConnectionOrigin> connectionOrigin`

          Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

          - `SERVICE("service")`

            Uses the Managed Agents service network.

          - `ENVIRONMENT("environment")`

            Uses the session's execution environment.

        - `Optional<String> credentialId`

          The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

        - `Optional<RequestMetadata> requestMetadata`

          Metadata included with requests to this MCP server.

        - `Optional<Boolean> required`

          Whether this MCP server must initialize before the first turn. Defaults to `false`.

      - `WebSearch`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

        - `Optional<List<String>> allowedDomains`

          Domains the search may include.

        - `Optional<ContextSize> contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Optional<Mode> mode`

          The source used for web search results. Defaults to `live`.

          - `DISABLED("disabled")`

            Disables web search.

          - `CACHED("cached")`

            Uses cached search results.

          - `LIVE("live")`

            Searches the live web.

      - `ComputerUse`

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

        - `Optional<Boolean> includeScreenshots`

          Whether computer tool outputs include screenshots. Defaults to `false`.

  - `Optional<String> agentId`

    The ID of a saved reusable agent. Omit `agent` to use its configuration unchanged.

  - `Optional<Input> input`

    Initial input to submit when the session is created. A string is shorthand for a single user message. Required when `environment.type` is `none`, or when `stream` is `true` for an environment that is not `self_hosted`; optional for self-hosted and non-streaming execution environments.

    - `String`

    - `List<AgentSessionInputMessageParam>`

      - `List<InputContentParam> content`

        The content of the message.

        - `InputText`

          - `String text`

            The text sent to the model.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image sent to the model.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

      - `JsonValue; role "user"constant`

        The role of the message author. Always `user`.

        - `USER("user")`

      - `Optional<Type> type`

        The type of the input item. Always `message`.

        - `MESSAGE("message")`

  - `Optional<Metadata> metadata`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Omission or null defaults to an empty map.

  - `Optional<List<String>> vaultIds`

    The IDs of vaults made available to the session.

### Returns

- `class AgentSession:`

  A Managed Agents session.

  - `String id`

    The ID of the session.

  - `Agent agent`

    The agent running in the session.

    - `String id`

      The ID of the agent.

    - `Optional<String> instructions`

      Custom instructions appended to the agent's default base instructions.

    - `String model`

      The model used by the agent.

    - `MultiAgentConfig multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled. Defaults to false.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Optional<String> name`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `AgentReasoning reasoning`

      The agent's reasoning configuration.

      - `Optional<Effort> effort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier serviceTier`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `AUTO("auto")`

      - `DEFAULT("default")`

      - `FLEX("flex")`

      - `PRIORITY("priority")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

    - `AgentText text`

      Configuration for text generated by the agent.

      - `TextFormat format`

        The effective output format. Defaults to ordinary text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Verbosity verbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

    - `List<AgentTool> tools`

      Tools available to the agent.

      - `Function`

        - `boolean deferLoading`

          Whether the function is deferred and discovered through tool search.

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

      - `ProgrammaticToolCalling`

        - `boolean enabled`

          Whether tools can be called from model-generated code.

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Mcp`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call.

        - `ConnectionOrigin connectionOrigin`

          Where outbound MCP HTTP connections originate.

          - `SERVICE("service")`

          - `ENVIRONMENT("environment")`

        - `Optional<String> credentialId`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata requestMetadata`

          Metadata included with requests to this MCP server.

        - `boolean required`

          Whether this MCP server must initialize before the first turn.

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransport transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

          - `Stdio`

            - `List<String> args`

              Arguments passed to the MCP server command.

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `List<String> envVars`

              Environment variable names inherited from the execution environment.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

      - `WebSearch`

        - `Optional<List<String>> allowedDomains`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results, if provided.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode mode`

          The source used for web search results.

          - `DISABLED("disabled")`

          - `CACHED("cached")`

          - `LIVE("live")`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

      - `ComputerUse`

        - `boolean includeScreenshots`

          Whether computer tool outputs include screenshots.

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment environment`

    The execution environment for the session.

    - `JsonValue;`

      - `JsonValue; type "none"constant`

        The type of the object. Always `none`.

        - `NONE("none")`

    - `OpenAIHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `Desktop desktop`

        The effective desktop configuration.

        - `boolean enabled`

          Whether the environment provisions a desktop and browser proxy.

      - `List<HostedEnvironmentFile> files`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileId:`

          A file copied from the OpenAI Files API.

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String fileId`

            The ID of the uploaded file.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "file_id"constant`

            The type of the object. Always `file_id`.

            - `FILE_ID("file_id")`

        - `Inline`

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `Network network`

        The effective network access policy for the environment.

        - `Access access`

          The environment's network access mode.

          - `ENABLED("enabled")`

            Allows unrestricted network access.

          - `DISABLED("disabled")`

            Disables network access.

          - `RESTRICTED("restricted")`

            Applies the configured domain restrictions.

        - `List<String> allowedDomains`

          Domains the environment may access when network access is restricted.

      - `Packages packages`

        Packages installed in the environment.

        - `List<String> npm`

          npm packages installed globally in the environment.

        - `List<String> python`

          Python packages installed in the environment.

        - `List<String> system`

          System packages installed in the environment.

      - `List<HostedPlugin> plugins`

        Plugins installed in the environment, excluding their archive contents.

        - `String description`

          The installed plugin description.

        - `String name`

          The installed plugin name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

      - `List<HostedSkill> skills`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference:`

          A skill installed from the Skills API.

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `String skillId`

            The referenced skill ID.

          - `JsonValue; type "skill_reference"constant`

            The type of the object. Always `skill_reference`.

            - `SKILL_REFERENCE("skill_reference")`

          - `String version`

            The concrete skill version installed for this session.

        - `Inline`

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `JsonValue; type "openai_hosted"constant`

        The type of the object. Always `openai_hosted`.

        - `OPENAI_HOSTED("openai_hosted")`

      - `Optional<ContainerSize> containerSize`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `SMALL("small")`

        - `MEDIUM("medium")`

        - `LARGE("large")`

    - `SelfHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `String remoteUrl`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `JsonValue; type "self_hosted"constant`

        The type of the object. Always `self_hosted`.

        - `SELF_HOSTED("self_hosted")`

      - `String workspaceDirectory`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Optional<String> error`

    The error that caused the session to fail, if any.

  - `long lastActiveAt`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata metadata`

    Custom string key-value pairs attached to the session.

  - `JsonValue; object_ "agent.session"constant`

    The object type. Always `agent.session`.

    - `AGENT_SESSION("agent.session")`

  - `List<RequiredAction> requiredActions`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest:`

      Respond to a computer-use request.

      - `Request request`

        The information needed to render the request.

        - `class BrowserAuthentication:`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class BrowserOriginAccess:`

          A browser origin awaiting the application's approval decision.

          - `String origin`

            The origin the browser needs permission to access.

          - `Optional<String> reason`

            The browser's explanation for this request, or null when unavailable.

          - `JsonValue; type "browser_origin_access"constant`

            The type of the object. Always `browser_origin_access`.

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `String requestId`

        The registered request ID to echo when responding.

      - `String turnId`

        The turn that requested approval.

      - `JsonValue; type "computer_use_approval_request"constant`

        The type of the object. Always `computer_use_approval_request`.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class FunctionCall:`

      Run a function tool and submit its result.

      - `JsonValue arguments`

        The arguments supplied by the model.

      - `String callId`

        The ID to include when submitting the function result.

      - `String name`

        The function name.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "function_call"constant`

        The type of the object. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class EnvironmentConnection:`

      Reconnect a session environment.

      - `String environmentId`

        The ID of the environment to reconnect.

      - `JsonValue; type "environment_connection"constant`

        The type of the object. Always `environment_connection`.

        - `ENVIRONMENT_CONNECTION("environment_connection")`

  - `Status status`

    The current status of the session.

    - `IDLE("idle")`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `IN_PROGRESS("in_progress")`

      The session is processing a turn.

    - `REQUIRES_ACTION("requires_action")`

      The session is waiting for one or more required actions.

    - `FAILED("failed")`

      The session failed.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

  - `List<String> vaultIds`

    The IDs of vaults made available to the session.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.JsonValue;
import com.openai.models.beta.agents.AgentSession;
import com.openai.models.beta.agents.EnvironmentParam;
import com.openai.models.beta.agents.sessions.SessionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionCreateParams params = SessionCreateParams.builder()
            .environmentNone()
            .build();
        AgentSession agentSession = client.beta().agents().sessions().create(params);
    }
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

`AgentSessionDeleted beta().agents().sessions().delete(SessionDeleteParamsparams = SessionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/sessions/{session_id}`

Removes a managed agent session from the public API and returns a deletion confirmation. If backend execution has ended, deletion can cancel a still-open public turn and abandon unpublished outputs. Running execution must be cancelled first. Physical cleanup may continue asynchronously. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `SessionDeleteParams params`

  - `Optional<String> sessionId`

### Returns

- `class AgentSessionDeleted:`

  A Managed Agents session removed from the public API. Physical cleanup may continue asynchronously.

  - `String id`

    The ID of the deleted session.

  - `boolean deleted`

    Whether the session has been removed from the public API. Always `true`. Physical cleanup may still be in progress.

  - `JsonValue; object_ "agent.session.deleted"constant`

    The object type. Always `agent.session.deleted`.

    - `AGENT_SESSION_DELETED("agent.session.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentSessionDeleted;
import com.openai.models.beta.agents.sessions.SessionDeleteParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentSessionDeleted agentSessionDeleted = client.beta().agents().sessions().delete("session_id");
    }
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

`SessionListPage beta().agents().sessions().list(SessionListParamsparams = SessionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions`

Lists managed agent sessions using ID-based pagination and the requested sort order. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `SessionListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<String> agentId`

    Only return sessions whose root agent has this ID. Omit to return sessions for all agents.

  - `Optional<Long> limit`

    The maximum number of resources to return.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSession:`

  A Managed Agents session.

  - `String id`

    The ID of the session.

  - `Agent agent`

    The agent running in the session.

    - `String id`

      The ID of the agent.

    - `Optional<String> instructions`

      Custom instructions appended to the agent's default base instructions.

    - `String model`

      The model used by the agent.

    - `MultiAgentConfig multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled. Defaults to false.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Optional<String> name`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `AgentReasoning reasoning`

      The agent's reasoning configuration.

      - `Optional<Effort> effort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier serviceTier`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `AUTO("auto")`

      - `DEFAULT("default")`

      - `FLEX("flex")`

      - `PRIORITY("priority")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

    - `AgentText text`

      Configuration for text generated by the agent.

      - `TextFormat format`

        The effective output format. Defaults to ordinary text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Verbosity verbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

    - `List<AgentTool> tools`

      Tools available to the agent.

      - `Function`

        - `boolean deferLoading`

          Whether the function is deferred and discovered through tool search.

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

      - `ProgrammaticToolCalling`

        - `boolean enabled`

          Whether tools can be called from model-generated code.

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Mcp`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call.

        - `ConnectionOrigin connectionOrigin`

          Where outbound MCP HTTP connections originate.

          - `SERVICE("service")`

          - `ENVIRONMENT("environment")`

        - `Optional<String> credentialId`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata requestMetadata`

          Metadata included with requests to this MCP server.

        - `boolean required`

          Whether this MCP server must initialize before the first turn.

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransport transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

          - `Stdio`

            - `List<String> args`

              Arguments passed to the MCP server command.

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `List<String> envVars`

              Environment variable names inherited from the execution environment.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

      - `WebSearch`

        - `Optional<List<String>> allowedDomains`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results, if provided.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode mode`

          The source used for web search results.

          - `DISABLED("disabled")`

          - `CACHED("cached")`

          - `LIVE("live")`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

      - `ComputerUse`

        - `boolean includeScreenshots`

          Whether computer tool outputs include screenshots.

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment environment`

    The execution environment for the session.

    - `JsonValue;`

      - `JsonValue; type "none"constant`

        The type of the object. Always `none`.

        - `NONE("none")`

    - `OpenAIHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `Desktop desktop`

        The effective desktop configuration.

        - `boolean enabled`

          Whether the environment provisions a desktop and browser proxy.

      - `List<HostedEnvironmentFile> files`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileId:`

          A file copied from the OpenAI Files API.

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String fileId`

            The ID of the uploaded file.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "file_id"constant`

            The type of the object. Always `file_id`.

            - `FILE_ID("file_id")`

        - `Inline`

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `Network network`

        The effective network access policy for the environment.

        - `Access access`

          The environment's network access mode.

          - `ENABLED("enabled")`

            Allows unrestricted network access.

          - `DISABLED("disabled")`

            Disables network access.

          - `RESTRICTED("restricted")`

            Applies the configured domain restrictions.

        - `List<String> allowedDomains`

          Domains the environment may access when network access is restricted.

      - `Packages packages`

        Packages installed in the environment.

        - `List<String> npm`

          npm packages installed globally in the environment.

        - `List<String> python`

          Python packages installed in the environment.

        - `List<String> system`

          System packages installed in the environment.

      - `List<HostedPlugin> plugins`

        Plugins installed in the environment, excluding their archive contents.

        - `String description`

          The installed plugin description.

        - `String name`

          The installed plugin name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

      - `List<HostedSkill> skills`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference:`

          A skill installed from the Skills API.

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `String skillId`

            The referenced skill ID.

          - `JsonValue; type "skill_reference"constant`

            The type of the object. Always `skill_reference`.

            - `SKILL_REFERENCE("skill_reference")`

          - `String version`

            The concrete skill version installed for this session.

        - `Inline`

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `JsonValue; type "openai_hosted"constant`

        The type of the object. Always `openai_hosted`.

        - `OPENAI_HOSTED("openai_hosted")`

      - `Optional<ContainerSize> containerSize`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `SMALL("small")`

        - `MEDIUM("medium")`

        - `LARGE("large")`

    - `SelfHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `String remoteUrl`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `JsonValue; type "self_hosted"constant`

        The type of the object. Always `self_hosted`.

        - `SELF_HOSTED("self_hosted")`

      - `String workspaceDirectory`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Optional<String> error`

    The error that caused the session to fail, if any.

  - `long lastActiveAt`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata metadata`

    Custom string key-value pairs attached to the session.

  - `JsonValue; object_ "agent.session"constant`

    The object type. Always `agent.session`.

    - `AGENT_SESSION("agent.session")`

  - `List<RequiredAction> requiredActions`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest:`

      Respond to a computer-use request.

      - `Request request`

        The information needed to render the request.

        - `class BrowserAuthentication:`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class BrowserOriginAccess:`

          A browser origin awaiting the application's approval decision.

          - `String origin`

            The origin the browser needs permission to access.

          - `Optional<String> reason`

            The browser's explanation for this request, or null when unavailable.

          - `JsonValue; type "browser_origin_access"constant`

            The type of the object. Always `browser_origin_access`.

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `String requestId`

        The registered request ID to echo when responding.

      - `String turnId`

        The turn that requested approval.

      - `JsonValue; type "computer_use_approval_request"constant`

        The type of the object. Always `computer_use_approval_request`.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class FunctionCall:`

      Run a function tool and submit its result.

      - `JsonValue arguments`

        The arguments supplied by the model.

      - `String callId`

        The ID to include when submitting the function result.

      - `String name`

        The function name.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "function_call"constant`

        The type of the object. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class EnvironmentConnection:`

      Reconnect a session environment.

      - `String environmentId`

        The ID of the environment to reconnect.

      - `JsonValue; type "environment_connection"constant`

        The type of the object. Always `environment_connection`.

        - `ENVIRONMENT_CONNECTION("environment_connection")`

  - `Status status`

    The current status of the session.

    - `IDLE("idle")`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `IN_PROGRESS("in_progress")`

      The session is processing a turn.

    - `REQUIRES_ACTION("requires_action")`

      The session is waiting for one or more required actions.

    - `FAILED("failed")`

      The session failed.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

  - `List<String> vaultIds`

    The IDs of vaults made available to the session.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.SessionListPage;
import com.openai.models.beta.agents.sessions.SessionListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SessionListPage page = client.beta().agents().sessions().list();
    }
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

`AgentSession beta().agents().sessions().retrieve(SessionRetrieveParamsparams = SessionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}`

Retrieves the current state of a managed agent session. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `SessionRetrieveParams params`

  - `Optional<String> sessionId`

### Returns

- `class AgentSession:`

  A Managed Agents session.

  - `String id`

    The ID of the session.

  - `Agent agent`

    The agent running in the session.

    - `String id`

      The ID of the agent.

    - `Optional<String> instructions`

      Custom instructions appended to the agent's default base instructions.

    - `String model`

      The model used by the agent.

    - `MultiAgentConfig multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled. Defaults to false.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Optional<String> name`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `AgentReasoning reasoning`

      The agent's reasoning configuration.

      - `Optional<Effort> effort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier serviceTier`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `AUTO("auto")`

      - `DEFAULT("default")`

      - `FLEX("flex")`

      - `PRIORITY("priority")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

    - `AgentText text`

      Configuration for text generated by the agent.

      - `TextFormat format`

        The effective output format. Defaults to ordinary text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Verbosity verbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

    - `List<AgentTool> tools`

      Tools available to the agent.

      - `Function`

        - `boolean deferLoading`

          Whether the function is deferred and discovered through tool search.

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

      - `ProgrammaticToolCalling`

        - `boolean enabled`

          Whether tools can be called from model-generated code.

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Mcp`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call.

        - `ConnectionOrigin connectionOrigin`

          Where outbound MCP HTTP connections originate.

          - `SERVICE("service")`

          - `ENVIRONMENT("environment")`

        - `Optional<String> credentialId`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata requestMetadata`

          Metadata included with requests to this MCP server.

        - `boolean required`

          Whether this MCP server must initialize before the first turn.

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransport transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

          - `Stdio`

            - `List<String> args`

              Arguments passed to the MCP server command.

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `List<String> envVars`

              Environment variable names inherited from the execution environment.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

      - `WebSearch`

        - `Optional<List<String>> allowedDomains`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results, if provided.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode mode`

          The source used for web search results.

          - `DISABLED("disabled")`

          - `CACHED("cached")`

          - `LIVE("live")`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

      - `ComputerUse`

        - `boolean includeScreenshots`

          Whether computer tool outputs include screenshots.

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment environment`

    The execution environment for the session.

    - `JsonValue;`

      - `JsonValue; type "none"constant`

        The type of the object. Always `none`.

        - `NONE("none")`

    - `OpenAIHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `Desktop desktop`

        The effective desktop configuration.

        - `boolean enabled`

          Whether the environment provisions a desktop and browser proxy.

      - `List<HostedEnvironmentFile> files`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileId:`

          A file copied from the OpenAI Files API.

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String fileId`

            The ID of the uploaded file.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "file_id"constant`

            The type of the object. Always `file_id`.

            - `FILE_ID("file_id")`

        - `Inline`

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `Network network`

        The effective network access policy for the environment.

        - `Access access`

          The environment's network access mode.

          - `ENABLED("enabled")`

            Allows unrestricted network access.

          - `DISABLED("disabled")`

            Disables network access.

          - `RESTRICTED("restricted")`

            Applies the configured domain restrictions.

        - `List<String> allowedDomains`

          Domains the environment may access when network access is restricted.

      - `Packages packages`

        Packages installed in the environment.

        - `List<String> npm`

          npm packages installed globally in the environment.

        - `List<String> python`

          Python packages installed in the environment.

        - `List<String> system`

          System packages installed in the environment.

      - `List<HostedPlugin> plugins`

        Plugins installed in the environment, excluding their archive contents.

        - `String description`

          The installed plugin description.

        - `String name`

          The installed plugin name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

      - `List<HostedSkill> skills`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference:`

          A skill installed from the Skills API.

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `String skillId`

            The referenced skill ID.

          - `JsonValue; type "skill_reference"constant`

            The type of the object. Always `skill_reference`.

            - `SKILL_REFERENCE("skill_reference")`

          - `String version`

            The concrete skill version installed for this session.

        - `Inline`

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `JsonValue; type "openai_hosted"constant`

        The type of the object. Always `openai_hosted`.

        - `OPENAI_HOSTED("openai_hosted")`

      - `Optional<ContainerSize> containerSize`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `SMALL("small")`

        - `MEDIUM("medium")`

        - `LARGE("large")`

    - `SelfHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `String remoteUrl`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `JsonValue; type "self_hosted"constant`

        The type of the object. Always `self_hosted`.

        - `SELF_HOSTED("self_hosted")`

      - `String workspaceDirectory`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Optional<String> error`

    The error that caused the session to fail, if any.

  - `long lastActiveAt`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata metadata`

    Custom string key-value pairs attached to the session.

  - `JsonValue; object_ "agent.session"constant`

    The object type. Always `agent.session`.

    - `AGENT_SESSION("agent.session")`

  - `List<RequiredAction> requiredActions`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest:`

      Respond to a computer-use request.

      - `Request request`

        The information needed to render the request.

        - `class BrowserAuthentication:`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class BrowserOriginAccess:`

          A browser origin awaiting the application's approval decision.

          - `String origin`

            The origin the browser needs permission to access.

          - `Optional<String> reason`

            The browser's explanation for this request, or null when unavailable.

          - `JsonValue; type "browser_origin_access"constant`

            The type of the object. Always `browser_origin_access`.

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `String requestId`

        The registered request ID to echo when responding.

      - `String turnId`

        The turn that requested approval.

      - `JsonValue; type "computer_use_approval_request"constant`

        The type of the object. Always `computer_use_approval_request`.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class FunctionCall:`

      Run a function tool and submit its result.

      - `JsonValue arguments`

        The arguments supplied by the model.

      - `String callId`

        The ID to include when submitting the function result.

      - `String name`

        The function name.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "function_call"constant`

        The type of the object. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class EnvironmentConnection:`

      Reconnect a session environment.

      - `String environmentId`

        The ID of the environment to reconnect.

      - `JsonValue; type "environment_connection"constant`

        The type of the object. Always `environment_connection`.

        - `ENVIRONMENT_CONNECTION("environment_connection")`

  - `Status status`

    The current status of the session.

    - `IDLE("idle")`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `IN_PROGRESS("in_progress")`

      The session is processing a turn.

    - `REQUIRES_ACTION("requires_action")`

      The session is waiting for one or more required actions.

    - `FAILED("failed")`

      The session failed.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

  - `List<String> vaultIds`

    The IDs of vaults made available to the session.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentSession;
import com.openai.models.beta.agents.sessions.SessionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentSession agentSession = client.beta().agents().sessions().retrieve("session_id");
    }
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

`AgentSession beta().agents().sessions().update(SessionUpdateParamsparams = SessionUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/sessions/{session_id}`

Updates session metadata, model, reasoning effort, or service tier. Model settings apply to subsequent turns. Omitted fields are unchanged. See [managing sessions](/api/docs/guides/agents-api/sessions/manage).

### Parameters

- `SessionUpdateParams params`

  - `Optional<String> sessionId`

  - `Optional<Agent> agent`

    Model settings for subsequent turns. Omitted fields stay unchanged.

    - `Optional<String> model`

      The model for subsequent turns. Omit to keep the current model.

    - `Optional<Reasoning> reasoning`

      Reasoning settings to update. Omit to keep the current effort.

      - `Optional<Effort> effort`

        Omit to keep the current effort. Null selects the model's default effort.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

    - `Optional<ServiceTier> serviceTier`

      Omit to keep the current tier. Null resets it to auto.

      - `AUTO("auto")`

        Selects the service tier automatically.

      - `DEFAULT("default")`

        Uses the default service tier.

      - `FLEX("flex")`

        Uses the flex service tier.

      - `PRIORITY("priority")`

        Uses the priority service tier.

      - `FAST("fast")`

        Uses the fast service tier.

      - `ULTRAFAST("ultrafast")`

        Uses the ultrafast service tier.

  - `Optional<Metadata> metadata`

    Replaces all metadata. Omit to leave unchanged, or pass null or {} to clear it. Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters.

### Returns

- `class AgentSession:`

  A Managed Agents session.

  - `String id`

    The ID of the session.

  - `Agent agent`

    The agent running in the session.

    - `String id`

      The ID of the agent.

    - `Optional<String> instructions`

      Custom instructions appended to the agent's default base instructions.

    - `String model`

      The model used by the agent.

    - `MultiAgentConfig multiAgent`

      Configuration for creating and coordinating subagents.

      - `boolean enabled`

        Whether subagent tools are enabled. Defaults to false.

      - `Optional<Long> maxConcurrentSubagents`

        Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

    - `Optional<String> name`

      The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

    - `AgentReasoning reasoning`

      The agent's reasoning configuration.

      - `Optional<Effort> effort`

        The requested reasoning effort, or `null` when the model selects its own default.

        - `NONE("none")`

        - `MINIMAL("minimal")`

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

        - `XHIGH("xhigh")`

        - `MAX("max")`

      - `Optional<Summary> summary`

        The requested reasoning summary format, or `null` when summaries are disabled.

        - `CONCISE("concise")`

          Returns a concise reasoning summary when supported.

        - `DETAILED("detailed")`

          Returns a detailed reasoning summary when supported.

        - `AUTO("auto")`

          Automatically selects the most detailed summary supported by the model.

    - `ServiceTier serviceTier`

      The effective service-tier policy for model requests. Defaults to `auto`.

      - `AUTO("auto")`

      - `DEFAULT("default")`

      - `FLEX("flex")`

      - `PRIORITY("priority")`

      - `FAST("fast")`

      - `ULTRAFAST("ultrafast")`

    - `AgentText text`

      Configuration for text generated by the agent.

      - `TextFormat format`

        The effective output format. Defaults to ordinary text.

        - `JsonValue;`

          - `JsonValue; type "text"constant`

            The type of the object. Always `text`.

            - `TEXT("text")`

        - `JsonSchema`

          - `Schema schema`

            The JSON Schema that generated text must match.

          - `JsonValue; type "json_schema"constant`

            The type of the object. Always `json_schema`.

            - `JSON_SCHEMA("json_schema")`

      - `Verbosity verbosity`

        The amount of text produced by the agent. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

    - `List<AgentTool> tools`

      Tools available to the agent.

      - `Function`

        - `boolean deferLoading`

          Whether the function is deferred and discovered through tool search.

        - `String description`

          A description of what the function does.

        - `String name`

          The name of the function.

        - `Parameters parameters`

          A JSON Schema object describing the function's arguments.

        - `JsonValue; type "function"constant`

          The type of the object. Always `function`.

          - `FUNCTION("function")`

      - `ProgrammaticToolCalling`

        - `boolean enabled`

          Whether tools can be called from model-generated code.

        - `JsonValue; type "programmatic_tool_calling"constant`

          The type of the object. Always `programmatic_tool_calling`.

          - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

      - `Mcp`

        - `Optional<List<String>> allowedTools`

          The MCP tools the agent may call.

        - `ConnectionOrigin connectionOrigin`

          Where outbound MCP HTTP connections originate.

          - `SERVICE("service")`

          - `ENVIRONMENT("environment")`

        - `Optional<String> credentialId`

          The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        - `RequestMetadata requestMetadata`

          Metadata included with requests to this MCP server.

        - `boolean required`

          Whether this MCP server must initialize before the first turn.

        - `String serverLabel`

          A label used to identify the MCP server in tool calls.

        - `McpTransport transport`

          The transport used to connect to the MCP server.

          - `Http`

            - `String serverUrl`

              The URL of the MCP server.

            - `JsonValue; type "http"constant`

              The type of the object. Always `http`.

              - `HTTP("http")`

          - `Stdio`

            - `List<String> args`

              Arguments passed to the MCP server command.

            - `String command`

              The command used to start the MCP server.

            - `String cwd`

              The working directory used to start the MCP server.

            - `List<String> envVars`

              Environment variable names inherited from the execution environment.

            - `JsonValue; type "stdio"constant`

              The type of the object. Always `stdio`.

              - `STDIO("stdio")`

        - `JsonValue; type "mcp"constant`

          The type of the object. Always `mcp`.

          - `MCP("mcp")`

      - `WebSearch`

        - `Optional<List<String>> allowedDomains`

          Allowed search domains, or `null` when the search is unrestricted.

        - `ContextSize contextSize`

          The amount of search context made available to the model. Defaults to `medium`.

          - `LOW("low")`

          - `MEDIUM("medium")`

          - `HIGH("high")`

        - `Optional<Location> location`

          Approximate location used to localize search results, if provided.

          - `Optional<String> city`

            The city name.

          - `Optional<String> country`

            The two-letter ISO country code, such as `US`.

          - `Optional<String> region`

            The region or state name.

          - `Optional<String> timezone`

            The IANA timezone, such as `America/Los_Angeles`.

        - `Mode mode`

          The source used for web search results.

          - `DISABLED("disabled")`

          - `CACHED("cached")`

          - `LIVE("live")`

        - `JsonValue; type "web_search"constant`

          The type of the object. Always `web_search`.

          - `WEB_SEARCH("web_search")`

      - `ComputerUse`

        - `boolean includeScreenshots`

          Whether computer tool outputs include screenshots.

        - `JsonValue; type "computer_use"constant`

          The type of the object. Always `computer_use`.

          - `COMPUTER_USE("computer_use")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the session was created.

  - `Environment environment`

    The execution environment for the session.

    - `JsonValue;`

      - `JsonValue; type "none"constant`

        The type of the object. Always `none`.

        - `NONE("none")`

    - `OpenAIHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `Desktop desktop`

        The effective desktop configuration.

        - `boolean enabled`

          Whether the environment provisions a desktop and browser proxy.

      - `List<HostedEnvironmentFile> files`

        Files available in the environment, excluding their contents.

        - `class HostedEnvironmentFileId:`

          A file copied from the OpenAI Files API.

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String fileId`

            The ID of the uploaded file.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "file_id"constant`

            The type of the object. Always `file_id`.

            - `FILE_ID("file_id")`

        - `Inline`

          - `String id`

            The session-scoped ID of the file in the execution environment.

          - `String path`

            The file's absolute path inside the environment.

          - `long sizeBytes`

            The decoded file size in bytes.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `Network network`

        The effective network access policy for the environment.

        - `Access access`

          The environment's network access mode.

          - `ENABLED("enabled")`

            Allows unrestricted network access.

          - `DISABLED("disabled")`

            Disables network access.

          - `RESTRICTED("restricted")`

            Applies the configured domain restrictions.

        - `List<String> allowedDomains`

          Domains the environment may access when network access is restricted.

      - `Packages packages`

        Packages installed in the environment.

        - `List<String> npm`

          npm packages installed globally in the environment.

        - `List<String> python`

          Python packages installed in the environment.

        - `List<String> system`

          System packages installed in the environment.

      - `List<HostedPlugin> plugins`

        Plugins installed in the environment, excluding their archive contents.

        - `String description`

          The installed plugin description.

        - `String name`

          The installed plugin name.

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

      - `List<HostedSkill> skills`

        Skills installed in the environment, excluding their archive contents.

        - `class HostedSkillReference:`

          A skill installed from the Skills API.

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `String skillId`

            The referenced skill ID.

          - `JsonValue; type "skill_reference"constant`

            The type of the object. Always `skill_reference`.

            - `SKILL_REFERENCE("skill_reference")`

          - `String version`

            The concrete skill version installed for this session.

        - `Inline`

          - `String description`

            The installed skill description.

          - `String name`

            The installed skill name.

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

      - `JsonValue; type "openai_hosted"constant`

        The type of the object. Always `openai_hosted`.

        - `OPENAI_HOSTED("openai_hosted")`

      - `Optional<ContainerSize> containerSize`

        The effective CPU and memory tier, or null when unknown or outside the public tiers.

        - `SMALL("small")`

        - `MEDIUM("medium")`

        - `LARGE("large")`

    - `SelfHosted`

      - `String id`

        The public ID of the environment.

      - `List<String> capabilityDirectories`

        Directories that contain capabilities exposed to the agent.

      - `String remoteUrl`

        Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

      - `JsonValue; type "self_hosted"constant`

        The type of the object. Always `self_hosted`.

        - `SELF_HOSTED("self_hosted")`

      - `String workspaceDirectory`

        The absolute project directory inside the environment. Defaults to `/workspace`.

  - `Optional<String> error`

    The error that caused the session to fail, if any.

  - `long lastActiveAt`

    The Unix timestamp, in seconds, when the session was last active.

  - `Metadata metadata`

    Custom string key-value pairs attached to the session.

  - `JsonValue; object_ "agent.session"constant`

    The object type. Always `agent.session`.

    - `AGENT_SESSION("agent.session")`

  - `List<RequiredAction> requiredActions`

    Actions that must be completed before the session can continue.

    - `class ComputerUseApprovalRequest:`

      Respond to a computer-use request.

      - `Request request`

        The information needed to render the request.

        - `class BrowserAuthentication:`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class BrowserOriginAccess:`

          A browser origin awaiting the application's approval decision.

          - `String origin`

            The origin the browser needs permission to access.

          - `Optional<String> reason`

            The browser's explanation for this request, or null when unavailable.

          - `JsonValue; type "browser_origin_access"constant`

            The type of the object. Always `browser_origin_access`.

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `String requestId`

        The registered request ID to echo when responding.

      - `String turnId`

        The turn that requested approval.

      - `JsonValue; type "computer_use_approval_request"constant`

        The type of the object. Always `computer_use_approval_request`.

        - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

    - `class FunctionCall:`

      Run a function tool and submit its result.

      - `JsonValue arguments`

        The arguments supplied by the model.

      - `String callId`

        The ID to include when submitting the function result.

      - `String name`

        The function name.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "function_call"constant`

        The type of the object. Always `function_call`.

        - `FUNCTION_CALL("function_call")`

    - `class EnvironmentConnection:`

      Reconnect a session environment.

      - `String environmentId`

        The ID of the environment to reconnect.

      - `JsonValue; type "environment_connection"constant`

        The type of the object. Always `environment_connection`.

        - `ENVIRONMENT_CONNECTION("environment_connection")`

  - `Status status`

    The current status of the session.

    - `IDLE("idle")`

      The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

    - `IN_PROGRESS("in_progress")`

      The session is processing a turn.

    - `REQUIRES_ACTION("requires_action")`

      The session is waiting for one or more required actions.

    - `FAILED("failed")`

      The session failed.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the session, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

  - `List<String> vaultIds`

    The IDs of vaults made available to the session.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentSession;
import com.openai.models.beta.agents.sessions.SessionUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AgentSession agentSession = client.beta().agents().sessions().update("session_id");
    }
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

`HttpResponse beta().agents().sessions().artifacts().content(ArtifactContentParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}/content`

Downloads immutable session artifact bytes after the execution environment expires. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactContentParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.HttpResponse;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactContentParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactContentParams params = ArtifactContentParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        HttpResponse response = client.beta().agents().sessions().artifacts().content(params);
    }
}
```

## Delete an agent session artifact

`SessionArtifactDeleted beta().agents().sessions().artifacts().delete(ArtifactDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Deletes an immutable session artifact without deleting its live environment file or original Files API object. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactDeleteParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Returns

- `class SessionArtifactDeleted:`

  Confirmation that an immutable session artifact was deleted.

  - `String id`

    The ID of the deleted session artifact.

  - `boolean deleted`

    Whether the session artifact was deleted. Always `true`.

  - `JsonValue; object_ "agent.session.artifact.deleted"constant`

    The object type. Always `agent.session.artifact.deleted`.

    - `AGENT_SESSION_ARTIFACT_DELETED("agent.session.artifact.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactDeleteParams;
import com.openai.models.beta.agents.sessions.artifacts.SessionArtifactDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactDeleteParams params = ArtifactDeleteParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        SessionArtifactDeleted sessionArtifactDeleted = client.beta().agents().sessions().artifacts().delete(params);
    }
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

`ArtifactListPage beta().agents().sessions().artifacts().list(ArtifactListParamsparams = ArtifactListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts`

Lists immutable artifacts published by completed hosted session turns. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return artifacts after this immutable artifact ID.

  - `Optional<String> environmentId`

    Restrict the listing to artifacts produced by this environment.

  - `Optional<Long> limit`

    The maximum number of artifacts to return, between 1 and 100.

  - `Optional<Order> order`

    Sort by creation time and ID. Defaults to descending.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class SessionArtifact:`

  An immutable file published by a completed hosted session turn.

  - `String id`

    The immutable artifact ID.

  - `long createdAt`

    The Unix timestamp, in seconds, when the artifact was published.

  - `String environmentId`

    The ID of the environment that produced the artifact.

  - `JsonValue; object_ "agent.session.artifact"constant`

    The object type. Always `agent.session.artifact`.

    - `AGENT_SESSION_ARTIFACT("agent.session.artifact")`

  - `String path`

    The original absolute file path in the execution environment.

  - `String sessionId`

    The ID of the session that owns the artifact.

  - `long sizeBytes`

    The immutable artifact size in bytes.

  - `String turnId`

    The ID of the completed turn that published the artifact.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactListPage;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactListPage page = client.beta().agents().sessions().artifacts().list("session_id");
    }
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

`SessionArtifact beta().agents().sessions().artifacts().retrieve(ArtifactRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/artifacts/{artifact_id}`

Retrieves immutable metadata for one durable session artifact. See [session artifacts](/api/docs/guides/agents-api/environments/files#openai-hosted-artifacts).

### Parameters

- `ArtifactRetrieveParams params`

  - `String sessionId`

  - `Optional<String> artifactId`

### Returns

- `class SessionArtifact:`

  An immutable file published by a completed hosted session turn.

  - `String id`

    The immutable artifact ID.

  - `long createdAt`

    The Unix timestamp, in seconds, when the artifact was published.

  - `String environmentId`

    The ID of the environment that produced the artifact.

  - `JsonValue; object_ "agent.session.artifact"constant`

    The object type. Always `agent.session.artifact`.

    - `AGENT_SESSION_ARTIFACT("agent.session.artifact")`

  - `String path`

    The original absolute file path in the execution environment.

  - `String sessionId`

    The ID of the session that owns the artifact.

  - `long sizeBytes`

    The immutable artifact size in bytes.

  - `String turnId`

    The ID of the completed turn that published the artifact.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.artifacts.ArtifactRetrieveParams;
import com.openai.models.beta.agents.sessions.artifacts.SessionArtifact;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ArtifactRetrieveParams params = ArtifactRetrieveParams.builder()
            .sessionId("session_id")
            .artifactId("artifact_id")
            .build();
        SessionArtifact sessionArtifact = client.beta().agents().sessions().artifacts().retrieve(params);
    }
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

- `class SessionArtifact:`

  An immutable file published by a completed hosted session turn.

  - `String id`

    The immutable artifact ID.

  - `long createdAt`

    The Unix timestamp, in seconds, when the artifact was published.

  - `String environmentId`

    The ID of the environment that produced the artifact.

  - `JsonValue; object_ "agent.session.artifact"constant`

    The object type. Always `agent.session.artifact`.

    - `AGENT_SESSION_ARTIFACT("agent.session.artifact")`

  - `String path`

    The original absolute file path in the execution environment.

  - `String sessionId`

    The ID of the session that owns the artifact.

  - `long sizeBytes`

    The immutable artifact size in bytes.

  - `String turnId`

    The ID of the completed turn that published the artifact.

### Session Artifact Deleted

- `class SessionArtifactDeleted:`

  Confirmation that an immutable session artifact was deleted.

  - `String id`

    The ID of the deleted session artifact.

  - `boolean deleted`

    Whether the session artifact was deleted. Always `true`.

  - `JsonValue; object_ "agent.session.artifact.deleted"constant`

    The object type. Always `agent.session.artifact.deleted`.

    - `AGENT_SESSION_ARTIFACT_DELETED("agent.session.artifact.deleted")`

# Events

## Create agent session input events

`beta().agents().sessions().events().create(EventCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `EventCreateParams params`

  - `Optional<String> sessionId`

  - `Optional<String> idempotencyKey`

  - `List<AgentSessionInputParam> events`

    The input events to submit to the session.

    - `AgentSessionInputComputerUseApprovalRequestResult`

      - `String requestId`

        The registered request ID from the required action.

      - `Response response`

        The response for this request type.

        - `class AgentBrowserAuthenticationSubmitParam:`

          - `JsonValue; action "submit"constant`

            - `SUBMIT("submit")`

          - `List<Field> fields`

            Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

            - `String fieldId`

              The field ID from the required action.

            - `String value`

              The value to enter into the registered control.

          - `JsonValue; type "browser_authentication"constant`

            - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `Optional<String> selectedOption`

            The chosen method. Required when the required action contains options.

        - `class AgentBrowserAuthenticationCancelParam:`

          - `JsonValue; action "cancel"constant`

            - `CANCEL("cancel")`

          - `JsonValue; type "browser_authentication"constant`

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `class AgentBrowserOriginAccessParam:`

          - `Decision decision`

            Whether to allow, deny, or cancel the requested origin access.

            - `APPROVE("approve")`

              Allow the browser to access this origin.

            - `DENY("deny")`

              Deny access to this origin.

            - `CANCEL("cancel")`

              Dismiss this request without approving access.

          - `JsonValue; type "browser_origin_access"constant`

            - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

      - `JsonValue; type "agent.session.input.computer_use_approval_request_result"constant`

        The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

        - `AGENT_SESSION_INPUT_COMPUTER_USE_APPROVAL_REQUEST_RESULT("agent.session.input.computer_use_approval_request_result")`

    - `AgentSessionInputMessage`

      - `List<AgentSessionInputMessageParam> input`

        The user messages to add to the session.

        - `List<InputContentParam> content`

          The content of the message.

          - `InputText`

            - `String text`

              The text sent to the model.

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image sent to the model.

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

        - `JsonValue; role "user"constant`

          The role of the message author. Always `user`.

          - `USER("user")`

        - `Optional<Type> type`

          The type of the input item. Always `message`.

          - `MESSAGE("message")`

      - `JsonValue; type "agent.session.input.message"constant`

        The type of the object. Always `agent.session.input.message`.

        - `AGENT_SESSION_INPUT_MESSAGE("agent.session.input.message")`

    - `JsonValue;`

      - `JsonValue; type "agent.session.input.cancel"constant`

        The type of the object. Always `agent.session.input.cancel`.

        - `AGENT_SESSION_INPUT_CANCEL("agent.session.input.cancel")`

    - `AgentSessionInputToolResult`

      - `String callId`

        The ID of the function call.

      - `boolean success`

        Whether the function call succeeded.

      - `String turnId`

        The ID of the turn that requested the function call.

      - `JsonValue; type "agent.session.input.tool_result"constant`

        The type of the object. Always `agent.session.input.tool_result`.

        - `AGENT_SESSION_INPUT_TOOL_RESULT("agent.session.input.tool_result")`

      - `Optional<String> error`

        The error message when the call failed.

      - `Optional<AgentFunctionCallOutputParam> output`

        The function result when the call succeeded.

        - `String`

        - `List<InputContentParam>`

          - `InputText`

          - `InputImage`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentBrowserAuthenticationSubmitParam;
import com.openai.models.beta.agents.AgentSessionInputParam;
import com.openai.models.beta.agents.sessions.events.EventCreateParams;
import java.util.List;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        EventCreateParams params = EventCreateParams.builder()
            .sessionId("session_id")
            .addEvent(AgentSessionInputParam.AgentSessionInputComputerUseApprovalRequestResult.builder()
                .requestId("request_id")
                .browserAuthenticationResponse(List.of(AgentBrowserAuthenticationSubmitParam.Field.builder()
                    .fieldId("field_id")
                    .value("value")
                    .build()))
                .build())
            .build();
        client.beta().agents().sessions().events().create(params);
    }
}
```

## Stream agent session events

`AgentSessionEvent beta().agents().sessions().events().streamStreaming(EventStreamParamsparams = EventStreamParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/events`

Streams live events for an agent session. See [session events](/api/docs/guides/agents-api/sessions/events).

### Parameters

- `EventStreamParams params`

  - `Optional<String> sessionId`

### Returns

- `class AgentSessionEvent: A class that can be one of several variants.union`

  An event emitted by a Managed Agents session.

  - `class AgentSessionErrorEvent:`

    Emitted when a turn or session fails.

    - `SessionError error`

      The error that occurred.

      - `Optional<String> code`

        The machine-readable error code, if any.

      - `String message`

        A customer-safe explanation of the error.

      - `Optional<String> param`

        The request parameter associated with the error, if any.

      - `String type`

        The error type.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `JsonValue; type "error"constant`

      The type of the object. Always `error`.

      - `ERROR("error")`

  - `class AgentSessionEnvironmentReadyEvent:`

    Emitted when a hosted session environment is ready to connect.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

      - `String id`

        The public ID of the environment.

      - `Optional<Error> error`

        The error reported while preparing the environment, if any.

        - `String code`

          A machine-readable error code.

        - `String message`

          A human-readable error message.

        - `String type`

          The error type.

      - `Status status`

        The environment's connection status.

        - `PENDING("pending")`

          The environment is being prepared.

        - `READY("ready")`

          The environment is ready to connect.

        - `CONNECTED("connected")`

          The environment is connected.

        - `DISCONNECTED("disconnected")`

          The environment is disconnected.

        - `FAILED("failed")`

          The environment failed to connect.

      - `String type`

        The environment type.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.ready"constant`

      The type of the object. Always `agent.session.environment.ready`.

      - `AGENT_SESSION_ENVIRONMENT_READY("agent.session.environment.ready")`

  - `class AgentSessionEnvironmentResetEvent:`

    Emitted after a hosted sandbox is replaced. Conversation history survives; changes to the previous sandbox's files and processes do not.

    - `String environmentId`

      The stable environment ID, retained across sandbox replacements.

    - `String eventId`

      The unique ID of the event.

    - `long resetCount`

      Monotonically increasing reset number. Repeated notifications share this number.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The associated turn, when applicable.

    - `JsonValue; type "agent.session.environment.reset"constant`

      The type of the object. Always `agent.session.environment.reset`.

      - `AGENT_SESSION_ENVIRONMENT_RESET("agent.session.environment.reset")`

  - `class AgentOutputCommandExecutionOutputDeltaEvent:`

    Emitted when command execution produces an output delta.

    - `String delta`

      The output text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the command execution item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.output.command_execution_output.delta"constant`

      The type of the object. Always `agent.output.command_execution_output.delta`.

      - `AGENT_OUTPUT_COMMAND_EXECUTION_OUTPUT_DELTA("agent.output.command_execution_output.delta")`

  - `class AgentSessionCreatedEvent:`

    Emitted when a session is created.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that was created.

      - `String id`

        The ID of the session.

      - `Agent agent`

        The agent running in the session.

        - `String id`

          The ID of the agent.

        - `Optional<String> instructions`

          Custom instructions appended to the agent's default base instructions.

        - `String model`

          The model used by the agent.

        - `MultiAgentConfig multiAgent`

          Configuration for creating and coordinating subagents.

          - `boolean enabled`

            Whether subagent tools are enabled. Defaults to false.

          - `Optional<Long> maxConcurrentSubagents`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

        - `Optional<String> name`

          The reusable agent's name when the session was created, or null if no name was saved. Later changes to the agent's name do not affect this value.

        - `AgentReasoning reasoning`

          The agent's reasoning configuration.

          - `Optional<Effort> effort`

            The requested reasoning effort, or `null` when the model selects its own default.

            - `NONE("none")`

            - `MINIMAL("minimal")`

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

            - `XHIGH("xhigh")`

            - `MAX("max")`

          - `Optional<Summary> summary`

            The requested reasoning summary format, or `null` when summaries are disabled.

            - `CONCISE("concise")`

              Returns a concise reasoning summary when supported.

            - `DETAILED("detailed")`

              Returns a detailed reasoning summary when supported.

            - `AUTO("auto")`

              Automatically selects the most detailed summary supported by the model.

        - `ServiceTier serviceTier`

          The effective service-tier policy for model requests. Defaults to `auto`.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `FAST("fast")`

          - `ULTRAFAST("ultrafast")`

        - `AgentText text`

          Configuration for text generated by the agent.

          - `TextFormat format`

            The effective output format. Defaults to ordinary text.

            - `JsonValue;`

              - `JsonValue; type "text"constant`

                The type of the object. Always `text`.

                - `TEXT("text")`

            - `JsonSchema`

              - `Schema schema`

                The JSON Schema that generated text must match.

              - `JsonValue; type "json_schema"constant`

                The type of the object. Always `json_schema`.

                - `JSON_SCHEMA("json_schema")`

          - `Verbosity verbosity`

            The amount of text produced by the agent. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

        - `List<AgentTool> tools`

          Tools available to the agent.

          - `Function`

            - `boolean deferLoading`

              Whether the function is deferred and discovered through tool search.

            - `String description`

              A description of what the function does.

            - `String name`

              The name of the function.

            - `Parameters parameters`

              A JSON Schema object describing the function's arguments.

            - `JsonValue; type "function"constant`

              The type of the object. Always `function`.

              - `FUNCTION("function")`

          - `ProgrammaticToolCalling`

            - `boolean enabled`

              Whether tools can be called from model-generated code.

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the object. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `Mcp`

            - `Optional<List<String>> allowedTools`

              The MCP tools the agent may call.

            - `ConnectionOrigin connectionOrigin`

              Where outbound MCP HTTP connections originate.

              - `SERVICE("service")`

              - `ENVIRONMENT("environment")`

            - `Optional<String> credentialId`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            - `RequestMetadata requestMetadata`

              Metadata included with requests to this MCP server.

            - `boolean required`

              Whether this MCP server must initialize before the first turn.

            - `String serverLabel`

              A label used to identify the MCP server in tool calls.

            - `McpTransport transport`

              The transport used to connect to the MCP server.

              - `Http`

                - `String serverUrl`

                  The URL of the MCP server.

                - `JsonValue; type "http"constant`

                  The type of the object. Always `http`.

                  - `HTTP("http")`

              - `Stdio`

                - `List<String> args`

                  Arguments passed to the MCP server command.

                - `String command`

                  The command used to start the MCP server.

                - `String cwd`

                  The working directory used to start the MCP server.

                - `List<String> envVars`

                  Environment variable names inherited from the execution environment.

                - `JsonValue; type "stdio"constant`

                  The type of the object. Always `stdio`.

                  - `STDIO("stdio")`

            - `JsonValue; type "mcp"constant`

              The type of the object. Always `mcp`.

              - `MCP("mcp")`

          - `WebSearch`

            - `Optional<List<String>> allowedDomains`

              Allowed search domains, or `null` when the search is unrestricted.

            - `ContextSize contextSize`

              The amount of search context made available to the model. Defaults to `medium`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<Location> location`

              Approximate location used to localize search results, if provided.

              - `Optional<String> city`

                The city name.

              - `Optional<String> country`

                The two-letter ISO country code, such as `US`.

              - `Optional<String> region`

                The region or state name.

              - `Optional<String> timezone`

                The IANA timezone, such as `America/Los_Angeles`.

            - `Mode mode`

              The source used for web search results.

              - `DISABLED("disabled")`

              - `CACHED("cached")`

              - `LIVE("live")`

            - `JsonValue; type "web_search"constant`

              The type of the object. Always `web_search`.

              - `WEB_SEARCH("web_search")`

          - `ComputerUse`

            - `boolean includeScreenshots`

              Whether computer tool outputs include screenshots.

            - `JsonValue; type "computer_use"constant`

              The type of the object. Always `computer_use`.

              - `COMPUTER_USE("computer_use")`

      - `long createdAt`

        The Unix timestamp, in seconds, when the session was created.

      - `Environment environment`

        The execution environment for the session.

        - `JsonValue;`

          - `JsonValue; type "none"constant`

            The type of the object. Always `none`.

            - `NONE("none")`

        - `OpenAIHosted`

          - `String id`

            The public ID of the environment.

          - `List<String> capabilityDirectories`

            Directories that contain capabilities exposed to the agent.

          - `Desktop desktop`

            The effective desktop configuration.

            - `boolean enabled`

              Whether the environment provisions a desktop and browser proxy.

          - `List<HostedEnvironmentFile> files`

            Files available in the environment, excluding their contents.

            - `class HostedEnvironmentFileId:`

              A file copied from the OpenAI Files API.

              - `String id`

                The session-scoped ID of the file in the execution environment.

              - `String fileId`

                The ID of the uploaded file.

              - `String path`

                The file's absolute path inside the environment.

              - `long sizeBytes`

                The decoded file size in bytes.

              - `JsonValue; type "file_id"constant`

                The type of the object. Always `file_id`.

                - `FILE_ID("file_id")`

            - `Inline`

              - `String id`

                The session-scoped ID of the file in the execution environment.

              - `String path`

                The file's absolute path inside the environment.

              - `long sizeBytes`

                The decoded file size in bytes.

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `Network network`

            The effective network access policy for the environment.

            - `Access access`

              The environment's network access mode.

              - `ENABLED("enabled")`

                Allows unrestricted network access.

              - `DISABLED("disabled")`

                Disables network access.

              - `RESTRICTED("restricted")`

                Applies the configured domain restrictions.

            - `List<String> allowedDomains`

              Domains the environment may access when network access is restricted.

          - `Packages packages`

            Packages installed in the environment.

            - `List<String> npm`

              npm packages installed globally in the environment.

            - `List<String> python`

              Python packages installed in the environment.

            - `List<String> system`

              System packages installed in the environment.

          - `List<HostedPlugin> plugins`

            Plugins installed in the environment, excluding their archive contents.

            - `String description`

              The installed plugin description.

            - `String name`

              The installed plugin name.

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

          - `List<HostedSkill> skills`

            Skills installed in the environment, excluding their archive contents.

            - `class HostedSkillReference:`

              A skill installed from the Skills API.

              - `String description`

                The installed skill description.

              - `String name`

                The installed skill name.

              - `String skillId`

                The referenced skill ID.

              - `JsonValue; type "skill_reference"constant`

                The type of the object. Always `skill_reference`.

                - `SKILL_REFERENCE("skill_reference")`

              - `String version`

                The concrete skill version installed for this session.

            - `Inline`

              - `String description`

                The installed skill description.

              - `String name`

                The installed skill name.

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `JsonValue; type "openai_hosted"constant`

            The type of the object. Always `openai_hosted`.

            - `OPENAI_HOSTED("openai_hosted")`

          - `Optional<ContainerSize> containerSize`

            The effective CPU and memory tier, or null when unknown or outside the public tiers.

            - `SMALL("small")`

            - `MEDIUM("medium")`

            - `LARGE("large")`

        - `SelfHosted`

          - `String id`

            The public ID of the environment.

          - `List<String> capabilityDirectories`

            Directories that contain capabilities exposed to the agent.

          - `String remoteUrl`

            Pass this URL unchanged to `codex exec-server --remote` when connecting this environment.

          - `JsonValue; type "self_hosted"constant`

            The type of the object. Always `self_hosted`.

            - `SELF_HOSTED("self_hosted")`

          - `String workspaceDirectory`

            The absolute project directory inside the environment. Defaults to `/workspace`.

      - `Optional<String> error`

        The error that caused the session to fail, if any.

      - `long lastActiveAt`

        The Unix timestamp, in seconds, when the session was last active.

      - `Metadata metadata`

        Custom string key-value pairs attached to the session.

      - `JsonValue; object_ "agent.session"constant`

        The object type. Always `agent.session`.

        - `AGENT_SESSION("agent.session")`

      - `List<RequiredAction> requiredActions`

        Actions that must be completed before the session can continue.

        - `class ComputerUseApprovalRequest:`

          Respond to a computer-use request.

          - `Request request`

            The information needed to render the request.

            - `class BrowserAuthentication:`

              A registered form awaiting the application's response.

              - `Optional<String> credentialOrigin`

                The registered form or frame origin where values will be entered.

              - `List<Field> fields`

                Controls to render. All submitted values are sensitive.

                - `String id`

                  The field ID to submit as field_id in a fields entry.

                - `String label`

                  The label to display beside the control.

                - `boolean required`

                  Whether this control requires a nonempty value.

                - `String type`

                  The rendering type, such as email, password, or text.

              - `List<Option> options`

                Sign-in methods. Empty for a plain form.

                - `String id`

                  The option ID to submit as selected_option.

                - `List<String> fieldIds`

                  IDs from the registered fields that this method accepts.

                - `String label`

                  The method label to display.

              - `Optional<String> reason`

                Why the agent needs the user to sign in.

              - `JsonValue; type "browser_authentication"constant`

                The type of the object. Always `browser_authentication`.

                - `BROWSER_AUTHENTICATION("browser_authentication")`

            - `class BrowserOriginAccess:`

              A browser origin awaiting the application's approval decision.

              - `String origin`

                The origin the browser needs permission to access.

              - `Optional<String> reason`

                The browser's explanation for this request, or null when unavailable.

              - `JsonValue; type "browser_origin_access"constant`

                The type of the object. Always `browser_origin_access`.

                - `BROWSER_ORIGIN_ACCESS("browser_origin_access")`

          - `String requestId`

            The registered request ID to echo when responding.

          - `String turnId`

            The turn that requested approval.

          - `JsonValue; type "computer_use_approval_request"constant`

            The type of the object. Always `computer_use_approval_request`.

            - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

        - `class FunctionCall:`

          Run a function tool and submit its result.

          - `JsonValue arguments`

            The arguments supplied by the model.

          - `String callId`

            The ID to include when submitting the function result.

          - `String name`

            The function name.

          - `String turnId`

            The ID of the turn that requested the function call.

          - `JsonValue; type "function_call"constant`

            The type of the object. Always `function_call`.

            - `FUNCTION_CALL("function_call")`

        - `class EnvironmentConnection:`

          Reconnect a session environment.

          - `String environmentId`

            The ID of the environment to reconnect.

          - `JsonValue; type "environment_connection"constant`

            The type of the object. Always `environment_connection`.

            - `ENVIRONMENT_CONNECTION("environment_connection")`

      - `Status status`

        The current status of the session.

        - `IDLE("idle")`

          The session has no turn in progress and is ready for input. A hosted environment may still be provisioning.

        - `IN_PROGRESS("in_progress")`

          The session is processing a turn.

        - `REQUIRES_ACTION("requires_action")`

          The session is waiting for one or more required actions.

        - `FAILED("failed")`

          The session failed.

      - `Optional<TokenUsage> usage`

        Best-effort token usage for the session, or null if unknown. Recorded usage may change.

        - `long inputTokens`

          The number of input tokens used by the agent.

        - `InputTokensDetails inputTokensDetails`

          A breakdown of the agent's input token usage.

          - `long cachedTokens`

            The number of input tokens retrieved from the prompt cache.

        - `long outputTokens`

          The number of output tokens generated by the agent.

        - `OutputTokensDetails outputTokensDetails`

          A breakdown of the agent's output token usage.

          - `long reasoningTokens`

            The number of output tokens used for reasoning.

        - `long totalTokens`

          The total number of input and output tokens used by the agent.

      - `List<String> vaultIds`

        The IDs of vaults made available to the session.

    - `JsonValue; type "agent.session.created"constant`

      The type of the object. Always `agent.session.created`.

      - `AGENT_SESSION_CREATED("agent.session.created")`

  - `class AgentSessionTurnCreatedEvent:`

    Emitted when a turn is created.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The turn at the time it was created.

      - `String id`

        The ID of the turn.

      - `String agentId`

        The ID of the agent that ran the turn.

      - `Optional<Long> completedAt`

        The Unix timestamp, in seconds, when the turn reached a terminal state.

      - `long createdAt`

        The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

      - `Optional<SessionTurnError> error`

        A customer-safe error. Non-null only for a failed turn.

        - `Code code`

          A stable, machine-readable failure category.

          - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

            The request exceeds the model's context window.

          - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

            The session has reached its usage budget.

          - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

            The organization has reached a usage, plan, or billing limit.

          - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

            The organization has no API credits remaining.

          - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

            The request exceeds the available rate limit.

          - `FLEX_UNAVAILABLE("flex_unavailable")`

            Flex processing is temporarily unavailable.

          - `SERVER_OVERLOADED("server_overloaded")`

            The model service is temporarily overloaded.

          - `CYBER_POLICY("cyber_policy")`

            The request was rejected by a safety policy.

          - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

            The request was blocked by the safety systems.

          - `CONNECTION_FAILED("connection_failed")`

            The request could not connect to the model service.

          - `SERVER_ERROR("server_error")`

            The model service encountered an unexpected error.

          - `AUTHENTICATION_ERROR("authentication_error")`

            The API credentials are invalid or lack the required access.

          - `INVALID_REQUEST("invalid_request")`

            The request contains invalid input or configuration.

          - `RESOURCE_NOT_FOUND("resource_not_found")`

            The requested model or resource is unavailable.

          - `SANDBOX_ERROR("sandbox_error")`

            The request could not complete in its execution environment.

          - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

            The executor must be upgraded before it can run this turn.

          - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

            The session cannot accept additional input while a request is running.

          - `REQUEST_TIMEOUT("request_timeout")`

            The request timed out before the model service responded.

          - `INTERNAL_ERROR("internal_error")`

            An unexpected internal error prevented the session request from completing.

        - `String message`

          A customer-safe explanation of the failure.

      - `Object object_`

        The object type. Always `agent.session.turn`.

        - `AGENT_SESSION_TURN("agent.session.turn")`

      - `String sessionId`

        The ID of the session that owns the turn.

      - `Optional<Long> startedAt`

        The Unix timestamp, in seconds, when the turn started.

      - `Status status`

        The current status of the turn.

        - `QUEUED("queued")`

          The turn is waiting to start.

        - `IN_PROGRESS("in_progress")`

          The turn is in progress.

        - `WAITING("waiting")`

          The turn is waiting for external input.

        - `COMPLETED("completed")`

          The turn completed successfully.

        - `FAILED("failed")`

          The turn failed.

        - `CANCELLED("cancelled")`

          The turn was cancelled.

      - `Optional<String> subagentId`

        The ID of the subagent that ran the turn, if applicable.

      - `Optional<TokenUsage> usage`

        Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.created"constant`

      The type of the object. Always `agent.session.turn.created`.

      - `AGENT_SESSION_TURN_CREATED("agent.session.turn.created")`

  - `class AgentSessionTurnInProgressEvent:`

    Emitted when a turn starts running.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The turn at the time it started running.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.in_progress"constant`

      The type of the object. Always `agent.session.turn.in_progress`.

      - `AGENT_SESSION_TURN_IN_PROGRESS("agent.session.turn.in_progress")`

  - `class AgentSessionTurnCompletedEvent:`

    Emitted when a turn completes.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The completed turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.completed"constant`

      The type of the object. Always `agent.session.turn.completed`.

      - `AGENT_SESSION_TURN_COMPLETED("agent.session.turn.completed")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnFailedEvent:`

    Emitted when a turn fails.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The failed turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.failed"constant`

      The type of the object. Always `agent.session.turn.failed`.

      - `AGENT_SESSION_TURN_FAILED("agent.session.turn.failed")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnCancelledEvent:`

    Emitted when a turn is cancelled.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Turn turn`

      The cancelled turn.

    - `String turnId`

      The ID of the turn associated with the event.

    - `JsonValue; type "agent.session.turn.cancelled"constant`

      The type of the object. Always `agent.session.turn.cancelled`.

      - `AGENT_SESSION_TURN_CANCELLED("agent.session.turn.cancelled")`

    - `Optional<TokenUsage> usage`

      Token usage by the root agent during the turn, when available.

  - `class AgentSessionTurnItemAddedEvent:`

    Emitted when an item is added to a turn.

    - `String eventId`

      The unique ID of the event.

    - `AgentSessionItem item`

      The item that was added.

      - `class AgentSessionMessage:`

        A user or assistant message recorded in a session.

        - `Optional<String> id`

          The ID of this item, or null for legacy user messages whose ID was not recorded.

        - `List<AgentSessionMessageContent> content`

          The content of the message. User messages contain input text or images; assistant messages contain output text.

          - `InputText`

            - `String text`

              The text supplied by the user.

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image supplied by the user, which may be a base64-encoded data URL.

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

          - `OutputText`

            - `String text`

              The text produced by the assistant.

            - `JsonValue; type "output_text"constant`

              The type of the object. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

        - `Optional<Phase> phase`

          The phase of an assistant message. Null for user messages.

          - `COMMENTARY("commentary")`

            Commentary produced while the agent works.

          - `FINAL_ANSWER("final_answer")`

            The agent's final answer.

        - `Role role`

          The role of the message author.

          - `USER("user")`

          - `ASSISTANT("assistant")`

        - `AgentOutputItemStatus status`

          The status of the message. User messages are always `completed`.

          - `IN_PROGRESS("in_progress")`

            The item is in progress.

          - `COMPLETED("completed")`

            The item is complete.

          - `INCOMPLETE("incomplete")`

            The item stopped before completing.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "message"constant`

          The item type. Always `message`.

          - `MESSAGE("message")`

      - `class AgentReasoningItem:`

        A reasoning item produced by the agent.

        - `String id`

          The ID of the reasoning item.

        - `Optional<AgentOutputItemStatus> status`

          The status of the reasoning item.

        - `List<SummaryText> summary`

          The reasoning summaries produced by the agent.

          - `String text`

            The reasoning summary text.

          - `JsonValue; type "summary_text"constant`

            The content type. Always `summary_text`.

            - `SUMMARY_TEXT("summary_text")`

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "reasoning"constant`

          The item type. Always `reasoning`.

          - `REASONING("reasoning")`

      - `class AgentFunctionCallItem:`

        A function call produced by the agent.

        - `String id`

          The ID of the function call item.

        - `JsonValue arguments`

          The arguments to pass to the function.

        - `String callId`

          The ID used to submit the function result.

        - `String name`

          The name of the function to call.

        - `AgentFunctionCallStatus status`

          The status of the function call.

          - `IN_PROGRESS("in_progress")`

            The call is in progress.

          - `COMPLETED("completed")`

            The call completed successfully.

          - `FAILED("failed")`

            The call failed.

          - `INCOMPLETE("incomplete")`

            The call stopped before completing.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "function_call"constant`

          The item type. Always `function_call`.

          - `FUNCTION_CALL("function_call")`

      - `FunctionCallOutput`

        - `String id`

          The ID of the function call output item.

        - `String callId`

          The ID of the function call that produced this output.

        - `Optional<String> error`

          The error message, if the call failed.

        - `Optional<AgentFunctionCallOutput> output`

          The function result, if the call succeeded.

          - `String`

          - `List<InputContent>`

            - `InputText`

              - `String text`

                The text supplied to the agent.

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

        - `AgentFunctionCallStatus status`

          The status of the function call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "function_call_output"constant`

          The item type. Always `function_call_output`.

          - `FUNCTION_CALL_OUTPUT("function_call_output")`

      - `AgentMessage`

        - `String id`

          The ID of the message.

        - `List<AgentContent> content`

          The content exchanged between the agents.

          - `class OutputText:`

            A text content part produced by the agent.

            - `String text`

              The text produced by the agent.

            - `JsonValue; type "output_text"constant`

              The content type. Always `output_text`.

              - `OUTPUT_TEXT("output_text")`

          - `EncryptedContent`

            - `String encryptedContent`

              The encrypted content payload.

            - `JsonValue; type "encrypted_content"constant`

              The content type. Always `encrypted_content`.

              - `ENCRYPTED_CONTENT("encrypted_content")`

        - `String recipientAgentId`

          The ID or name of the receiving agent.

        - `String senderAgentId`

          The ID or name of the sending agent.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "agent_message"constant`

          The item type. Always `agent_message`.

          - `AGENT_MESSAGE("agent_message")`

      - `class AgentMcpCallItem:`

        A call to a tool on an MCP server.

        - `String id`

          The ID of the MCP call item.

        - `JsonValue arguments`

          The arguments passed to the MCP tool.

        - `JsonValue error`

          The error returned by the MCP tool, if any.

        - `String name`

          The name of the MCP tool.

        - `JsonValue output`

          The output returned by the MCP tool, if any.

        - `String serverLabel`

          The label of the MCP server.

        - `AgentFunctionCallStatus status`

          The status of the MCP tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "mcp_call"constant`

          The item type. Always `mcp_call`.

          - `MCP_CALL("mcp_call")`

      - `ComputerUseCall`

        - `String id`

          The ID of the activity item.

        - `Optional<Output> output`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `String imageUrl`

            The complete JPEG image as a base64 data URL.

          - `JsonValue; type "computer_screenshot"constant`

            The content type. Always `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

        - `AgentFunctionCallStatus status`

          The execution status of the activity.

        - `Optional<String> title`

          A model-generated description of the activity, when available.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_call"constant`

          The item type. Always `computer_use_call`.

          - `COMPUTER_USE_CALL("computer_use_call")`

      - `ComputerUseApprovalRequest`

        - `String id`

          The stable history item ID.

        - `Request request`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String requestId`

        - `String turnId`

        - `JsonValue; type "computer_use_approval_request"constant`

          The item type. Always computer_use_approval_request.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `ComputerUseApprovalRequestResult`

        - `String id`

          The stable history item ID.

        - `String requestId`

          The registered request answered by this item.

        - `Response response`

          The admitted response, without submitted credential values.

          - `class Submit:`

            - `JsonValue; action "submit"constant`

              - `SUBMIT("submit")`

            - `Optional<String> selectedOption`

              The chosen sign-in method, or null when no options were offered.

            - `JsonValue; type "browser_authentication"constant`

              - `BROWSER_AUTHENTICATION("browser_authentication")`

          - `JsonValue;`

            - `JsonValue; action "cancel"constant`

              - `CANCEL("cancel")`

            - `JsonValue; type "browser_authentication"constant`

              - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_approval_request_result"constant`

          - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

      - `class AgentWebSearchCallItem:`

        A web search call produced by the agent.

        - `String id`

          The ID of the web search call.

        - `Optional<WebSearchAction> action`

          The action performed by the web search tool.

          - `Search`

            - `Optional<List<String>> queries`

              The search queries, when multiple queries were used.

            - `Optional<String> query`

              The search query, when a single query was used.

            - `JsonValue; type "search"constant`

              The type of the object. Always `search`.

              - `SEARCH("search")`

          - `OpenPage`

            - `JsonValue; type "open_page"constant`

              The type of the object. Always `open_page`.

              - `OPEN_PAGE("open_page")`

            - `Optional<String> url`

              The URL of the page that was opened.

          - `FindInPage`

            - `Optional<String> pattern`

              The text pattern that was searched for.

            - `JsonValue; type "find_in_page"constant`

              The type of the object. Always `find_in_page`.

              - `FIND_IN_PAGE("find_in_page")`

            - `Optional<String> url`

              The URL of the page that was searched.

          - `JsonValue;`

            - `JsonValue; type "other"constant`

              The type of the object. Always `other`.

              - `OTHER("other")`

        - `AgentOutputItemStatus status`

          The status of the web search call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "web_search_call"constant`

          The item type. Always `web_search_call`.

          - `WEB_SEARCH_CALL("web_search_call")`

      - `class AgentCommandExecutionItem:`

        A command execution produced by the agent.

        - `String id`

          The ID of the command execution item.

        - `String command`

          The command that was executed.

        - `Optional<String> cwd`

          The working directory used to execute the command.

        - `Optional<Long> durationMs`

          The command duration in milliseconds.

        - `Optional<Long> exitCode`

          The process exit code, if the command completed.

        - `Optional<String> output`

          The command output, if available.

        - `AgentFunctionCallStatus status`

          The status of the command execution.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "command_execution"constant`

          The item type. Always `command_execution`.

          - `COMMAND_EXECUTION("command_execution")`

      - `class AgentCreateSubagentCallItem:`

        A request to spawn a subagent.

        - `String id`

          The ID of the tool call item.

        - `String agentId`

          The ID of the agent that requested the subagent.

        - `List<AgentContent> content`

          The task given to the spawned agent.

          - `class OutputText:`

            A text content part produced by the agent.

          - `EncryptedContent`

        - `Optional<String> model`

          The model requested for the spawned agent.

        - `Optional<String> reasoningEffort`

          The reasoning effort requested for the spawned agent.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "create_subagent_call"constant`

          The item type. Always `create_subagent_call`.

          - `CREATE_SUBAGENT_CALL("create_subagent_call")`

            The current public item type.

      - `class AgentSendSubagentInputCallItem:`

        A request to send input to another agent.

        - `String id`

          The ID of the tool call item.

        - `List<AgentContent> content`

          The input sent to the receiving agent.

          - `class OutputText:`

            A text content part produced by the agent.

          - `EncryptedContent`

        - `String recipientAgentId`

          The ID of the agent receiving the input.

        - `String senderAgentId`

          The ID of the agent sending the input.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "send_subagent_input_call"constant`

          The item type. Always `send_subagent_input_call`.

          - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

            The current public item type.

      - `class AgentResumeSubagentCallItem:`

        A request to resume a subagent.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to resume.

        - `String senderAgentId`

          The ID of the agent requesting the resume.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "resume_subagent_call"constant`

          The item type. Always `resume_subagent_call`.

          - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

            The current public item type.

      - `class AgentWaitForSubagentsCallItem:`

        A request to wait for one or more subagents.

        - `String id`

          The ID of the tool call item.

        - `List<String> recipientAgentIds`

          The IDs of the agents to wait for.

        - `String senderAgentId`

          The ID of the agent waiting for results.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "wait_for_subagents_call"constant`

          The item type. Always `wait_for_subagents_call`.

          - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

            The current public item type.

      - `class AgentInterruptSubagentCallItem:`

        A request to interrupt a subagent's current turn. The subagent remains available.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to interrupt.

        - `String senderAgentId`

          The ID of the agent requesting the interrupt.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "interrupt_subagent_call"constant`

          The item type. Always `interrupt_subagent_call`.

          - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

            The current public item type.

      - `class AgentCloseSubagentCallItem:`

        A request to close a subagent.

        - `String id`

          The ID of the tool call item.

        - `String recipientAgentId`

          The ID of the agent to close.

        - `String senderAgentId`

          The ID of the agent requesting the close.

        - `AgentFunctionCallStatus status`

          The status of the tool call.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "close_subagent_call"constant`

          The item type. Always `close_subagent_call`.

          - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

            The current public item type.

    - `Optional<Long> outputIndex`

      The index of the item in the turn output, when the item is agent output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.item.added"constant`

      The type of the object. Always `agent.session.turn.item.added`.

      - `AGENT_SESSION_TURN_ITEM_ADDED("agent.session.turn.item.added")`

  - `class AgentSessionIdleEvent:`

    Emitted when a session becomes idle.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that became idle.

    - `JsonValue; type "agent.session.idle"constant`

      The type of the object. Always `agent.session.idle`.

      - `AGENT_SESSION_IDLE("agent.session.idle")`

  - `class AgentSessionInProgressEvent:`

    Emitted when a session starts processing a turn.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session that started processing.

    - `JsonValue; type "agent.session.in_progress"constant`

      The type of the object. Always `agent.session.in_progress`.

      - `AGENT_SESSION_IN_PROGRESS("agent.session.in_progress")`

  - `class AgentSessionRequiresActionEvent:`

    Emitted when a session is waiting for one or more required actions.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The session and its current required actions.

    - `JsonValue; type "agent.session.requires_action"constant`

      The type of the object. Always `agent.session.requires_action`.

      - `AGENT_SESSION_REQUIRES_ACTION("agent.session.requires_action")`

  - `class AgentSessionFailedEvent:`

    Emitted when a session fails.

    - `String eventId`

      The unique ID of the event.

    - `AgentSession session`

      The failed session.

    - `JsonValue; type "agent.session.failed"constant`

      The type of the object. Always `agent.session.failed`.

      - `AGENT_SESSION_FAILED("agent.session.failed")`

  - `class AgentSessionEnvironmentPendingEvent:`

    Emitted while a session environment is being prepared.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.pending"constant`

      The type of the object. Always `agent.session.environment.pending`.

      - `AGENT_SESSION_ENVIRONMENT_PENDING("agent.session.environment.pending")`

  - `class AgentSessionEnvironmentConnectedEvent:`

    Emitted when a session environment connects.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.connected"constant`

      The type of the object. Always `agent.session.environment.connected`.

      - `AGENT_SESSION_ENVIRONMENT_CONNECTED("agent.session.environment.connected")`

  - `class AgentSessionEnvironmentDisconnectedEvent:`

    Emitted when a session environment disconnects.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.disconnected"constant`

      The type of the object. Always `agent.session.environment.disconnected`.

      - `AGENT_SESSION_ENVIRONMENT_DISCONNECTED("agent.session.environment.disconnected")`

  - `class AgentSessionEnvironmentFailedEvent:`

    Emitted when a session environment fails.

    - `AgentSessionEnvironmentState environment`

      The current environment state.

    - `String eventId`

      The unique ID of the event.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.environment.failed"constant`

      The type of the object. Always `agent.session.environment.failed`.

      - `AGENT_SESSION_ENVIRONMENT_FAILED("agent.session.environment.failed")`

  - `class AgentSessionSubagentCreatedEvent:`

    Emitted when a subagent is created.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that was created.

      - `String id`

        The ID of the subagent.

      - `Optional<Long> closedAt`

        The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

      - `Optional<List<AgentContent>> instructions`

        Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

        - `class OutputText:`

          A text content part produced by the agent.

        - `EncryptedContent`

      - `Optional<String> name`

        The runner-assigned nickname, or null when unavailable.

      - `Object object_`

        The object type. Always `agent.session.subagent`.

        - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

      - `long openedAt`

        The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

      - `String parentAgentId`

        The ID of the agent that created this subagent.

      - `String sessionId`

        The ID of the session that owns the subagent.

      - `Status status`

        The current status of the subagent.

        - `ACTIVE("active")`

          The subagent remains available, including while idle between turns.

        - `CLOSED("closed")`

          The subagent is closed.

    - `JsonValue; type "agent.session.subagent.created"constant`

      The type of the object. Always `agent.session.subagent.created`.

      - `AGENT_SESSION_SUBAGENT_CREATED("agent.session.subagent.created")`

  - `class AgentSessionSubagentActiveEvent:`

    Emitted when a closed subagent successfully resumes.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that resumed.

    - `JsonValue; type "agent.session.subagent.active"constant`

      The type of the object. Always `agent.session.subagent.active`.

      - `AGENT_SESSION_SUBAGENT_ACTIVE("agent.session.subagent.active")`

  - `class AgentSessionSubagentClosedEvent:`

    Emitted when a subagent is closed.

    - `String eventId`

      The unique ID of the event.

    - `Subagent subagent`

      The subagent that was closed.

    - `JsonValue; type "agent.session.subagent.closed"constant`

      The type of the object. Always `agent.session.subagent.closed`.

      - `AGENT_SESSION_SUBAGENT_CLOSED("agent.session.subagent.closed")`

  - `class AgentSessionTurnItemDoneEvent:`

    Emitted when an output item is complete.

    - `String eventId`

      The unique ID of the event.

    - `AgentOutputItem item`

      The completed output item.

      - `class AgentSessionAssistantMessage:`

        An assistant message produced by the agent.

        - `String id`

          The ID of the message.

        - `List<OutputText> content`

          The content of the message.

          - `String text`

            The text produced by the agent.

          - `JsonValue; type "output_text"constant`

            The content type. Always `output_text`.

        - `Optional<Phase> phase`

          The phase of the assistant message.

          - `COMMENTARY("commentary")`

            Commentary produced while the agent works.

          - `FINAL_ANSWER("final_answer")`

            The agent's final answer.

        - `JsonValue; role "assistant"constant`

          The role of the message author. Always `assistant`.

          - `ASSISTANT("assistant")`

        - `AgentOutputItemStatus status`

          The status of the message.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "message"constant`

          The item type. Always `message`.

          - `MESSAGE("message")`

      - `class AgentReasoningItem:`

        A reasoning item produced by the agent.

      - `class AgentFunctionCallItem:`

        A function call produced by the agent.

      - `class AgentMcpCallItem:`

        A call to a tool on an MCP server.

      - `ComputerUseCall`

        - `String id`

          The ID of the activity item.

        - `Optional<Output> output`

          The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

          - `String imageUrl`

            The complete JPEG image as a base64 data URL.

          - `JsonValue; type "computer_screenshot"constant`

            The content type. Always `computer_screenshot`.

            - `COMPUTER_SCREENSHOT("computer_screenshot")`

        - `AgentFunctionCallStatus status`

          The execution status of the activity.

        - `Optional<String> title`

          A model-generated description of the activity, when available.

        - `String turnId`

          The ID of the turn that contains this item.

        - `JsonValue; type "computer_use_call"constant`

          The item type. Always `computer_use_call`.

          - `COMPUTER_USE_CALL("computer_use_call")`

      - `ComputerUseApprovalRequest`

        - `String id`

          The stable history item ID.

        - `Request request`

          A registered form awaiting the application's response.

          - `Optional<String> credentialOrigin`

            The registered form or frame origin where values will be entered.

          - `List<Field> fields`

            Controls to render. All submitted values are sensitive.

            - `String id`

              The field ID to submit as field_id in a fields entry.

            - `String label`

              The label to display beside the control.

            - `boolean required`

              Whether this control requires a nonempty value.

            - `String type`

              The rendering type, such as email, password, or text.

          - `List<Option> options`

            Sign-in methods. Empty for a plain form.

            - `String id`

              The option ID to submit as selected_option.

            - `List<String> fieldIds`

              IDs from the registered fields that this method accepts.

            - `String label`

              The method label to display.

          - `Optional<String> reason`

            Why the agent needs the user to sign in.

          - `JsonValue; type "browser_authentication"constant`

            The type of the object. Always `browser_authentication`.

            - `BROWSER_AUTHENTICATION("browser_authentication")`

        - `String requestId`

        - `String turnId`

        - `JsonValue; type "computer_use_approval_request"constant`

          The item type. Always computer_use_approval_request.

          - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

      - `class AgentWebSearchCallItem:`

        A web search call produced by the agent.

      - `class AgentCommandExecutionItem:`

        A command execution produced by the agent.

      - `class AgentCreateSubagentCallItem:`

        A request to spawn a subagent.

      - `class AgentSendSubagentInputCallItem:`

        A request to send input to another agent.

      - `class AgentResumeSubagentCallItem:`

        A request to resume a subagent.

      - `class AgentWaitForSubagentsCallItem:`

        A request to wait for one or more subagents.

      - `class AgentInterruptSubagentCallItem:`

        A request to interrupt a subagent's current turn. The subagent remains available.

      - `class AgentCloseSubagentCallItem:`

        A request to close a subagent.

    - `long outputIndex`

      The index of the output item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.item.done"constant`

      The type of the object. Always `agent.session.turn.item.done`.

      - `AGENT_SESSION_TURN_ITEM_DONE("agent.session.turn.item.done")`

  - `class AgentSessionTurnContentPartAddedEvent:`

    Emitted when an output text content part is added.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `OutputText part`

      The initial content part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.content_part.added"constant`

      The type of the object. Always `agent.session.turn.content_part.added`.

      - `AGENT_SESSION_TURN_CONTENT_PART_ADDED("agent.session.turn.content_part.added")`

  - `class AgentSessionTurnContentPartDoneEvent:`

    Emitted when an output content part is complete.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `OutputText part`

      The completed content part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.content_part.done"constant`

      The type of the object. Always `agent.session.turn.content_part.done`.

      - `AGENT_SESSION_TURN_CONTENT_PART_DONE("agent.session.turn.content_part.done")`

  - `class AgentSessionTurnOutputTextDeltaEvent:`

    Emitted when text is appended to an output text content part.

    - `long contentIndex`

      The index of the content part in the message.

    - `String delta`

      The text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.output_text.delta"constant`

      The type of the object. Always `agent.session.turn.output_text.delta`.

      - `AGENT_SESSION_TURN_OUTPUT_TEXT_DELTA("agent.session.turn.output_text.delta")`

  - `class AgentSessionTurnOutputTextDoneEvent:`

    Emitted when an output text content part is complete.

    - `long contentIndex`

      The index of the content part in the message.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the message item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `String text`

      The complete output text.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.output_text.done"constant`

      The type of the object. Always `agent.session.turn.output_text.done`.

      - `AGENT_SESSION_TURN_OUTPUT_TEXT_DONE("agent.session.turn.output_text.done")`

  - `class AgentSessionTurnReasoningSummaryPartAddedEvent:`

    Emitted when a reasoning summary content part is added.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `SummaryText part`

      The initial summary part.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_part.added"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.added`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_ADDED("agent.session.turn.reasoning_summary_part.added")`

  - `class AgentSessionTurnReasoningSummaryPartDoneEvent:`

    Emitted when a reasoning summary part is complete.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `SummaryText part`

      The completed summary part.

    - `String sessionId`

      The ID of the session associated with the event.

    - `Optional<Status> status`

      Present as `incomplete` when summary generation was interrupted.

      - `INCOMPLETE("incomplete")`

    - `long summaryIndex`

      The index of the summary part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_part.done"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_part.done`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_PART_DONE("agent.session.turn.reasoning_summary_part.done")`

  - `class AgentSessionTurnReasoningSummaryTextDeltaEvent:`

    Emitted when text is appended to a reasoning summary.

    - `String delta`

      The summary text that was appended.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_text.delta"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.delta`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DELTA("agent.session.turn.reasoning_summary_text.delta")`

  - `class AgentSessionTurnReasoningSummaryTextDoneEvent:`

    Emitted when a reasoning summary content part is complete.

    - `String eventId`

      The unique ID of the event.

    - `String itemId`

      The ID of the reasoning item.

    - `long outputIndex`

      The index of the item in the turn output.

    - `String sessionId`

      The ID of the session associated with the event.

    - `long summaryIndex`

      The index of the summary content part.

    - `String text`

      The complete reasoning summary text.

    - `Optional<String> turnId`

      The ID of the turn associated with the event, when applicable.

    - `JsonValue; type "agent.session.turn.reasoning_summary_text.done"constant`

      The type of the object. Always `agent.session.turn.reasoning_summary_text.done`.

      - `AGENT_SESSION_TURN_REASONING_SUMMARY_TEXT_DONE("agent.session.turn.reasoning_summary_text.done")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.core.http.StreamResponse;
import com.openai.models.beta.agents.AgentSessionEvent;
import com.openai.models.beta.agents.sessions.events.EventStreamParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        StreamResponse<AgentSessionEvent> agentSessionEvent = client.beta().agents().sessions().events().streamStreaming("session_id");
    }
}
```

# Items

## List agent session items

`ItemListPage beta().agents().sessions().items().list(ItemListParamsparams = ItemListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/items`

Lists items produced by the session's root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `ItemListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

  - `class AgentSessionMessage:`

    A user or assistant message recorded in a session.

    - `Optional<String> id`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `List<AgentSessionMessageContent> content`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `InputText`

        - `String text`

          The text supplied by the user.

        - `JsonValue; type "input_text"constant`

          The type of the object. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `InputImage`

        - `String imageUrl`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `JsonValue; type "input_image"constant`

          The type of the object. Always `input_image`.

          - `INPUT_IMAGE("input_image")`

      - `OutputText`

        - `String text`

          The text produced by the assistant.

        - `JsonValue; type "output_text"constant`

          The type of the object. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

    - `Optional<Phase> phase`

      The phase of an assistant message. Null for user messages.

      - `COMMENTARY("commentary")`

        Commentary produced while the agent works.

      - `FINAL_ANSWER("final_answer")`

        The agent's final answer.

    - `Role role`

      The role of the message author.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `AgentOutputItemStatus status`

      The status of the message. User messages are always `completed`.

      - `IN_PROGRESS("in_progress")`

        The item is in progress.

      - `COMPLETED("completed")`

        The item is complete.

      - `INCOMPLETE("incomplete")`

        The item stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

    - `String name`

      The name of the function to call.

    - `AgentFunctionCallStatus status`

      The status of the function call.

      - `IN_PROGRESS("in_progress")`

        The call is in progress.

      - `COMPLETED("completed")`

        The call completed successfully.

      - `FAILED("failed")`

        The call failed.

      - `INCOMPLETE("incomplete")`

        The call stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `FunctionCallOutput`

    - `String id`

      The ID of the function call output item.

    - `String callId`

      The ID of the function call that produced this output.

    - `Optional<String> error`

      The error message, if the call failed.

    - `Optional<AgentFunctionCallOutput> output`

      The function result, if the call succeeded.

      - `String`

      - `List<InputContent>`

        - `InputText`

          - `String text`

            The text supplied to the agent.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

    - `AgentFunctionCallStatus status`

      The status of the function call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call_output"constant`

      The item type. Always `function_call_output`.

      - `FUNCTION_CALL_OUTPUT("function_call_output")`

  - `AgentMessage`

    - `String id`

      The ID of the message.

    - `List<AgentContent> content`

      The content exchanged between the agents.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `String recipientAgentId`

      The ID or name of the receiving agent.

    - `String senderAgentId`

      The ID or name of the sending agent.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "agent_message"constant`

      The item type. Always `agent_message`.

      - `AGENT_MESSAGE("agent_message")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        - `String id`

          The field ID to submit as field_id in a fields entry.

        - `String label`

          The label to display beside the control.

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        - `String id`

          The option ID to submit as selected_option.

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

        - `String label`

          The method label to display.

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

    - `String turnId`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `ComputerUseApprovalRequestResult`

    - `String id`

      The stable history item ID.

    - `String requestId`

      The registered request answered by this item.

    - `Response response`

      The admitted response, without submitted credential values.

      - `class Submit:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `Optional<String> selectedOption`

          The chosen sign-in method, or null when no options were offered.

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `JsonValue;`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_approval_request_result"constant`

      - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

        - `Optional<String> query`

          The search query, when a single query was used.

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

    - `String command`

      The command that was executed.

    - `Optional<String> cwd`

      The working directory used to execute the command.

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

    - `Optional<String> output`

      The command output, if available.

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

    - `String agentId`

      The ID of the agent that requested the subagent.

    - `List<AgentContent> content`

      The task given to the spawned agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `Optional<String> model`

      The model requested for the spawned agent.

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

        The current public item type.

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

    - `String senderAgentId`

      The ID of the agent sending the input.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

        The current public item type.

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to resume.

    - `String senderAgentId`

      The ID of the agent requesting the resume.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

    - `String senderAgentId`

      The ID of the agent waiting for results.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

        The current public item type.

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to interrupt.

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

        The current public item type.

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to close.

    - `String senderAgentId`

      The ID of the agent requesting the close.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

        The current public item type.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.items.ItemListPage;
import com.openai.models.beta.agents.sessions.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListPage page = client.beta().agents().sessions().items().list("session_id");
    }
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

`SubagentListPage beta().agents().sessions().subagents().list(SubagentListParamsparams = SubagentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `SubagentListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `Optional<String> name`

    The runner-assigned nickname, or null when unavailable.

  - `Object object_`

    The object type. Always `agent.session.subagent`.

    - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

  - `long openedAt`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `String parentAgentId`

    The ID of the agent that created this subagent.

  - `String sessionId`

    The ID of the session that owns the subagent.

  - `Status status`

    The current status of the subagent.

    - `ACTIVE("active")`

      The subagent remains available, including while idle between turns.

    - `CLOSED("closed")`

      The subagent is closed.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.SubagentListPage;
import com.openai.models.beta.agents.sessions.subagents.SubagentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentListPage page = client.beta().agents().sessions().subagents().list("session_id");
    }
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

`Subagent beta().agents().sessions().subagents().retrieve(SubagentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `SubagentRetrieveParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

### Returns

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

    - `class OutputText:`

      A text content part produced by the agent.

      - `String text`

        The text produced by the agent.

      - `JsonValue; type "output_text"constant`

        The content type. Always `output_text`.

        - `OUTPUT_TEXT("output_text")`

    - `EncryptedContent`

      - `String encryptedContent`

        The encrypted content payload.

      - `JsonValue; type "encrypted_content"constant`

        The content type. Always `encrypted_content`.

        - `ENCRYPTED_CONTENT("encrypted_content")`

  - `Optional<String> name`

    The runner-assigned nickname, or null when unavailable.

  - `Object object_`

    The object type. Always `agent.session.subagent`.

    - `AGENT_SESSION_SUBAGENT("agent.session.subagent")`

  - `long openedAt`

    The Unix timestamp, in seconds, when the subagent was first opened. Resuming does not change it.

  - `String parentAgentId`

    The ID of the agent that created this subagent.

  - `String sessionId`

    The ID of the session that owns the subagent.

  - `Status status`

    The current status of the subagent.

    - `ACTIVE("active")`

      The subagent remains available, including while idle between turns.

    - `CLOSED("closed")`

      The subagent is closed.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Subagent;
import com.openai.models.beta.agents.sessions.subagents.SubagentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentRetrieveParams params = SubagentRetrieveParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        Subagent subagent = client.beta().agents().sessions().subagents().retrieve(params);
    }
}
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

`ItemListPage beta().agents().sessions().subagents().items().list(ItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `ItemListParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

  - `class AgentSessionMessage:`

    A user or assistant message recorded in a session.

    - `Optional<String> id`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `List<AgentSessionMessageContent> content`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `InputText`

        - `String text`

          The text supplied by the user.

        - `JsonValue; type "input_text"constant`

          The type of the object. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `InputImage`

        - `String imageUrl`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `JsonValue; type "input_image"constant`

          The type of the object. Always `input_image`.

          - `INPUT_IMAGE("input_image")`

      - `OutputText`

        - `String text`

          The text produced by the assistant.

        - `JsonValue; type "output_text"constant`

          The type of the object. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

    - `Optional<Phase> phase`

      The phase of an assistant message. Null for user messages.

      - `COMMENTARY("commentary")`

        Commentary produced while the agent works.

      - `FINAL_ANSWER("final_answer")`

        The agent's final answer.

    - `Role role`

      The role of the message author.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `AgentOutputItemStatus status`

      The status of the message. User messages are always `completed`.

      - `IN_PROGRESS("in_progress")`

        The item is in progress.

      - `COMPLETED("completed")`

        The item is complete.

      - `INCOMPLETE("incomplete")`

        The item stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

    - `String name`

      The name of the function to call.

    - `AgentFunctionCallStatus status`

      The status of the function call.

      - `IN_PROGRESS("in_progress")`

        The call is in progress.

      - `COMPLETED("completed")`

        The call completed successfully.

      - `FAILED("failed")`

        The call failed.

      - `INCOMPLETE("incomplete")`

        The call stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `FunctionCallOutput`

    - `String id`

      The ID of the function call output item.

    - `String callId`

      The ID of the function call that produced this output.

    - `Optional<String> error`

      The error message, if the call failed.

    - `Optional<AgentFunctionCallOutput> output`

      The function result, if the call succeeded.

      - `String`

      - `List<InputContent>`

        - `InputText`

          - `String text`

            The text supplied to the agent.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

    - `AgentFunctionCallStatus status`

      The status of the function call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call_output"constant`

      The item type. Always `function_call_output`.

      - `FUNCTION_CALL_OUTPUT("function_call_output")`

  - `AgentMessage`

    - `String id`

      The ID of the message.

    - `List<AgentContent> content`

      The content exchanged between the agents.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `String recipientAgentId`

      The ID or name of the receiving agent.

    - `String senderAgentId`

      The ID or name of the sending agent.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "agent_message"constant`

      The item type. Always `agent_message`.

      - `AGENT_MESSAGE("agent_message")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        - `String id`

          The field ID to submit as field_id in a fields entry.

        - `String label`

          The label to display beside the control.

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        - `String id`

          The option ID to submit as selected_option.

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

        - `String label`

          The method label to display.

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

    - `String turnId`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `ComputerUseApprovalRequestResult`

    - `String id`

      The stable history item ID.

    - `String requestId`

      The registered request answered by this item.

    - `Response response`

      The admitted response, without submitted credential values.

      - `class Submit:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `Optional<String> selectedOption`

          The chosen sign-in method, or null when no options were offered.

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `JsonValue;`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_approval_request_result"constant`

      - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

        - `Optional<String> query`

          The search query, when a single query was used.

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

    - `String command`

      The command that was executed.

    - `Optional<String> cwd`

      The working directory used to execute the command.

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

    - `Optional<String> output`

      The command output, if available.

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

    - `String agentId`

      The ID of the agent that requested the subagent.

    - `List<AgentContent> content`

      The task given to the spawned agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `Optional<String> model`

      The model requested for the spawned agent.

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

        The current public item type.

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

    - `String senderAgentId`

      The ID of the agent sending the input.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

        The current public item type.

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to resume.

    - `String senderAgentId`

      The ID of the agent requesting the resume.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

    - `String senderAgentId`

      The ID of the agent waiting for results.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

        The current public item type.

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to interrupt.

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

        The current public item type.

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to close.

    - `String senderAgentId`

      The ID of the agent requesting the close.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

        The current public item type.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.items.ItemListPage;
import com.openai.models.beta.agents.sessions.subagents.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListParams params = ItemListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        ItemListPage page = client.beta().agents().sessions().subagents().items().list(params);
    }
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

`TurnListPage beta().agents().sessions().subagents().turns().list(TurnListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `TurnListParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

  - `String id`

    The ID of the turn.

  - `String agentId`

    The ID of the agent that ran the turn.

  - `Optional<Long> completedAt`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `long createdAt`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Optional<SessionTurnError> error`

    A customer-safe error. Non-null only for a failed turn.

    - `Code code`

      A stable, machine-readable failure category.

      - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

        The request exceeds the model's context window.

      - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

        The session has reached its usage budget.

      - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

        The organization has reached a usage, plan, or billing limit.

      - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

        The organization has no API credits remaining.

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        The request exceeds the available rate limit.

      - `FLEX_UNAVAILABLE("flex_unavailable")`

        Flex processing is temporarily unavailable.

      - `SERVER_OVERLOADED("server_overloaded")`

        The model service is temporarily overloaded.

      - `CYBER_POLICY("cyber_policy")`

        The request was rejected by a safety policy.

      - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

        The request was blocked by the safety systems.

      - `CONNECTION_FAILED("connection_failed")`

        The request could not connect to the model service.

      - `SERVER_ERROR("server_error")`

        The model service encountered an unexpected error.

      - `AUTHENTICATION_ERROR("authentication_error")`

        The API credentials are invalid or lack the required access.

      - `INVALID_REQUEST("invalid_request")`

        The request contains invalid input or configuration.

      - `RESOURCE_NOT_FOUND("resource_not_found")`

        The requested model or resource is unavailable.

      - `SANDBOX_ERROR("sandbox_error")`

        The request could not complete in its execution environment.

      - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

        The executor must be upgraded before it can run this turn.

      - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

        The session cannot accept additional input while a request is running.

      - `REQUEST_TIMEOUT("request_timeout")`

        The request timed out before the model service responded.

      - `INTERNAL_ERROR("internal_error")`

        An unexpected internal error prevented the session request from completing.

    - `String message`

      A customer-safe explanation of the failure.

  - `Object object_`

    The object type. Always `agent.session.turn`.

    - `AGENT_SESSION_TURN("agent.session.turn")`

  - `String sessionId`

    The ID of the session that owns the turn.

  - `Optional<Long> startedAt`

    The Unix timestamp, in seconds, when the turn started.

  - `Status status`

    The current status of the turn.

    - `QUEUED("queued")`

      The turn is waiting to start.

    - `IN_PROGRESS("in_progress")`

      The turn is in progress.

    - `WAITING("waiting")`

      The turn is waiting for external input.

    - `COMPLETED("completed")`

      The turn completed successfully.

    - `FAILED("failed")`

      The turn failed.

    - `CANCELLED("cancelled")`

      The turn was cancelled.

  - `Optional<String> subagentId`

    The ID of the subagent that ran the turn, if applicable.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnListPage;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnListParams params = TurnListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        TurnListPage page = client.beta().agents().sessions().subagents().turns().list(params);
    }
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

`Turn beta().agents().sessions().subagents().turns().retrieve(TurnRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `TurnRetrieveParams params`

  - `String sessionId`

  - `String subagentId`

  - `Optional<String> turnId`

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

  - `String id`

    The ID of the turn.

  - `String agentId`

    The ID of the agent that ran the turn.

  - `Optional<Long> completedAt`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `long createdAt`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Optional<SessionTurnError> error`

    A customer-safe error. Non-null only for a failed turn.

    - `Code code`

      A stable, machine-readable failure category.

      - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

        The request exceeds the model's context window.

      - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

        The session has reached its usage budget.

      - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

        The organization has reached a usage, plan, or billing limit.

      - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

        The organization has no API credits remaining.

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        The request exceeds the available rate limit.

      - `FLEX_UNAVAILABLE("flex_unavailable")`

        Flex processing is temporarily unavailable.

      - `SERVER_OVERLOADED("server_overloaded")`

        The model service is temporarily overloaded.

      - `CYBER_POLICY("cyber_policy")`

        The request was rejected by a safety policy.

      - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

        The request was blocked by the safety systems.

      - `CONNECTION_FAILED("connection_failed")`

        The request could not connect to the model service.

      - `SERVER_ERROR("server_error")`

        The model service encountered an unexpected error.

      - `AUTHENTICATION_ERROR("authentication_error")`

        The API credentials are invalid or lack the required access.

      - `INVALID_REQUEST("invalid_request")`

        The request contains invalid input or configuration.

      - `RESOURCE_NOT_FOUND("resource_not_found")`

        The requested model or resource is unavailable.

      - `SANDBOX_ERROR("sandbox_error")`

        The request could not complete in its execution environment.

      - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

        The executor must be upgraded before it can run this turn.

      - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

        The session cannot accept additional input while a request is running.

      - `REQUEST_TIMEOUT("request_timeout")`

        The request timed out before the model service responded.

      - `INTERNAL_ERROR("internal_error")`

        An unexpected internal error prevented the session request from completing.

    - `String message`

      A customer-safe explanation of the failure.

  - `Object object_`

    The object type. Always `agent.session.turn`.

    - `AGENT_SESSION_TURN("agent.session.turn")`

  - `String sessionId`

    The ID of the session that owns the turn.

  - `Optional<Long> startedAt`

    The Unix timestamp, in seconds, when the turn started.

  - `Status status`

    The current status of the turn.

    - `QUEUED("queued")`

      The turn is waiting to start.

    - `IN_PROGRESS("in_progress")`

      The turn is in progress.

    - `WAITING("waiting")`

      The turn is waiting for external input.

    - `COMPLETED("completed")`

      The turn completed successfully.

    - `FAILED("failed")`

      The turn failed.

    - `CANCELLED("cancelled")`

      The turn was cancelled.

  - `Optional<String> subagentId`

    The ID of the subagent that ran the turn, if applicable.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnRetrieveParams;
import com.openai.models.beta.agents.sessions.turns.Turn;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnRetrieveParams params = TurnRetrieveParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .turnId("turn_id")
            .build();
        Turn turn = client.beta().agents().sessions().subagents().turns().retrieve(params);
    }
}
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

`ItemListPage beta().agents().sessions().subagents().turns().items().list(ItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `ItemListParams params`

  - `String sessionId`

  - `String subagentId`

  - `Optional<String> turnId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

  - `class AgentSessionMessage:`

    A user or assistant message recorded in a session.

    - `Optional<String> id`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `List<AgentSessionMessageContent> content`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `InputText`

        - `String text`

          The text supplied by the user.

        - `JsonValue; type "input_text"constant`

          The type of the object. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `InputImage`

        - `String imageUrl`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `JsonValue; type "input_image"constant`

          The type of the object. Always `input_image`.

          - `INPUT_IMAGE("input_image")`

      - `OutputText`

        - `String text`

          The text produced by the assistant.

        - `JsonValue; type "output_text"constant`

          The type of the object. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

    - `Optional<Phase> phase`

      The phase of an assistant message. Null for user messages.

      - `COMMENTARY("commentary")`

        Commentary produced while the agent works.

      - `FINAL_ANSWER("final_answer")`

        The agent's final answer.

    - `Role role`

      The role of the message author.

      - `USER("user")`

      - `ASSISTANT("assistant")`

    - `AgentOutputItemStatus status`

      The status of the message. User messages are always `completed`.

      - `IN_PROGRESS("in_progress")`

        The item is in progress.

      - `COMPLETED("completed")`

        The item is complete.

      - `INCOMPLETE("incomplete")`

        The item stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      - `String text`

        The reasoning summary text.

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

    - `String name`

      The name of the function to call.

    - `AgentFunctionCallStatus status`

      The status of the function call.

      - `IN_PROGRESS("in_progress")`

        The call is in progress.

      - `COMPLETED("completed")`

        The call completed successfully.

      - `FAILED("failed")`

        The call failed.

      - `INCOMPLETE("incomplete")`

        The call stopped before completing.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `FunctionCallOutput`

    - `String id`

      The ID of the function call output item.

    - `String callId`

      The ID of the function call that produced this output.

    - `Optional<String> error`

      The error message, if the call failed.

    - `Optional<AgentFunctionCallOutput> output`

      The function result, if the call succeeded.

      - `String`

      - `List<InputContent>`

        - `InputText`

          - `String text`

            The text supplied to the agent.

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

    - `AgentFunctionCallStatus status`

      The status of the function call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "function_call_output"constant`

      The item type. Always `function_call_output`.

      - `FUNCTION_CALL_OUTPUT("function_call_output")`

  - `AgentMessage`

    - `String id`

      The ID of the message.

    - `List<AgentContent> content`

      The content exchanged between the agents.

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `String recipientAgentId`

      The ID or name of the receiving agent.

    - `String senderAgentId`

      The ID or name of the sending agent.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "agent_message"constant`

      The item type. Always `agent_message`.

      - `AGENT_MESSAGE("agent_message")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        - `String id`

          The field ID to submit as field_id in a fields entry.

        - `String label`

          The label to display beside the control.

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        - `String id`

          The option ID to submit as selected_option.

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

        - `String label`

          The method label to display.

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

    - `String turnId`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `ComputerUseApprovalRequestResult`

    - `String id`

      The stable history item ID.

    - `String requestId`

      The registered request answered by this item.

    - `Response response`

      The admitted response, without submitted credential values.

      - `class Submit:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `Optional<String> selectedOption`

          The chosen sign-in method, or null when no options were offered.

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `JsonValue;`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "computer_use_approval_request_result"constant`

      - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

        - `Optional<String> query`

          The search query, when a single query was used.

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

    - `String command`

      The command that was executed.

    - `Optional<String> cwd`

      The working directory used to execute the command.

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

    - `Optional<String> output`

      The command output, if available.

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

    - `String agentId`

      The ID of the agent that requested the subagent.

    - `List<AgentContent> content`

      The task given to the spawned agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `Optional<String> model`

      The model requested for the spawned agent.

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

        The current public item type.

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

    - `String senderAgentId`

      The ID of the agent sending the input.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

        The current public item type.

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to resume.

    - `String senderAgentId`

      The ID of the agent requesting the resume.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

    - `String senderAgentId`

      The ID of the agent waiting for results.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

        The current public item type.

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to interrupt.

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

        The current public item type.

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

    - `String recipientAgentId`

      The ID of the agent to close.

    - `String senderAgentId`

      The ID of the agent requesting the close.

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

        The current public item type.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.items.ItemListPage;
import com.openai.models.beta.agents.sessions.subagents.turns.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListParams params = ItemListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .turnId("turn_id")
            .build();
        ItemListPage page = client.beta().agents().sessions().subagents().turns().items().list(params);
    }
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

`TurnListPage beta().agents().sessions().turns().list(TurnListParamsparams = TurnListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `TurnListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

  - `String id`

    The ID of the turn.

  - `String agentId`

    The ID of the agent that ran the turn.

  - `Optional<Long> completedAt`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `long createdAt`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Optional<SessionTurnError> error`

    A customer-safe error. Non-null only for a failed turn.

    - `Code code`

      A stable, machine-readable failure category.

      - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

        The request exceeds the model's context window.

      - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

        The session has reached its usage budget.

      - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

        The organization has reached a usage, plan, or billing limit.

      - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

        The organization has no API credits remaining.

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        The request exceeds the available rate limit.

      - `FLEX_UNAVAILABLE("flex_unavailable")`

        Flex processing is temporarily unavailable.

      - `SERVER_OVERLOADED("server_overloaded")`

        The model service is temporarily overloaded.

      - `CYBER_POLICY("cyber_policy")`

        The request was rejected by a safety policy.

      - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

        The request was blocked by the safety systems.

      - `CONNECTION_FAILED("connection_failed")`

        The request could not connect to the model service.

      - `SERVER_ERROR("server_error")`

        The model service encountered an unexpected error.

      - `AUTHENTICATION_ERROR("authentication_error")`

        The API credentials are invalid or lack the required access.

      - `INVALID_REQUEST("invalid_request")`

        The request contains invalid input or configuration.

      - `RESOURCE_NOT_FOUND("resource_not_found")`

        The requested model or resource is unavailable.

      - `SANDBOX_ERROR("sandbox_error")`

        The request could not complete in its execution environment.

      - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

        The executor must be upgraded before it can run this turn.

      - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

        The session cannot accept additional input while a request is running.

      - `REQUEST_TIMEOUT("request_timeout")`

        The request timed out before the model service responded.

      - `INTERNAL_ERROR("internal_error")`

        An unexpected internal error prevented the session request from completing.

    - `String message`

      A customer-safe explanation of the failure.

  - `Object object_`

    The object type. Always `agent.session.turn`.

    - `AGENT_SESSION_TURN("agent.session.turn")`

  - `String sessionId`

    The ID of the session that owns the turn.

  - `Optional<Long> startedAt`

    The Unix timestamp, in seconds, when the turn started.

  - `Status status`

    The current status of the turn.

    - `QUEUED("queued")`

      The turn is waiting to start.

    - `IN_PROGRESS("in_progress")`

      The turn is in progress.

    - `WAITING("waiting")`

      The turn is waiting for external input.

    - `COMPLETED("completed")`

      The turn completed successfully.

    - `FAILED("failed")`

      The turn failed.

    - `CANCELLED("cancelled")`

      The turn was cancelled.

  - `Optional<String> subagentId`

    The ID of the subagent that ran the turn, if applicable.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.turns.TurnListPage;
import com.openai.models.beta.agents.sessions.turns.TurnListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnListPage page = client.beta().agents().sessions().turns().list("session_id");
    }
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

`Turn beta().agents().sessions().turns().retrieve(TurnRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/turns/{turn_id}`

Retrieves a turn's current status, timestamps, usage, and error. Returns 404 if the turn does not belong to the session. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

### Parameters

- `TurnRetrieveParams params`

  - `String sessionId`

  - `Optional<String> turnId`

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

  - `String id`

    The ID of the turn.

  - `String agentId`

    The ID of the agent that ran the turn.

  - `Optional<Long> completedAt`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `long createdAt`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Optional<SessionTurnError> error`

    A customer-safe error. Non-null only for a failed turn.

    - `Code code`

      A stable, machine-readable failure category.

      - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

        The request exceeds the model's context window.

      - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

        The session has reached its usage budget.

      - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

        The organization has reached a usage, plan, or billing limit.

      - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

        The organization has no API credits remaining.

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        The request exceeds the available rate limit.

      - `FLEX_UNAVAILABLE("flex_unavailable")`

        Flex processing is temporarily unavailable.

      - `SERVER_OVERLOADED("server_overloaded")`

        The model service is temporarily overloaded.

      - `CYBER_POLICY("cyber_policy")`

        The request was rejected by a safety policy.

      - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

        The request was blocked by the safety systems.

      - `CONNECTION_FAILED("connection_failed")`

        The request could not connect to the model service.

      - `SERVER_ERROR("server_error")`

        The model service encountered an unexpected error.

      - `AUTHENTICATION_ERROR("authentication_error")`

        The API credentials are invalid or lack the required access.

      - `INVALID_REQUEST("invalid_request")`

        The request contains invalid input or configuration.

      - `RESOURCE_NOT_FOUND("resource_not_found")`

        The requested model or resource is unavailable.

      - `SANDBOX_ERROR("sandbox_error")`

        The request could not complete in its execution environment.

      - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

        The executor must be upgraded before it can run this turn.

      - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

        The session cannot accept additional input while a request is running.

      - `REQUEST_TIMEOUT("request_timeout")`

        The request timed out before the model service responded.

      - `INTERNAL_ERROR("internal_error")`

        An unexpected internal error prevented the session request from completing.

    - `String message`

      A customer-safe explanation of the failure.

  - `Object object_`

    The object type. Always `agent.session.turn`.

    - `AGENT_SESSION_TURN("agent.session.turn")`

  - `String sessionId`

    The ID of the session that owns the turn.

  - `Optional<Long> startedAt`

    The Unix timestamp, in seconds, when the turn started.

  - `Status status`

    The current status of the turn.

    - `QUEUED("queued")`

      The turn is waiting to start.

    - `IN_PROGRESS("in_progress")`

      The turn is in progress.

    - `WAITING("waiting")`

      The turn is waiting for external input.

    - `COMPLETED("completed")`

      The turn completed successfully.

    - `FAILED("failed")`

      The turn failed.

    - `CANCELLED("cancelled")`

      The turn was cancelled.

  - `Optional<String> subagentId`

    The ID of the subagent that ran the turn, if applicable.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.turns.Turn;
import com.openai.models.beta.agents.sessions.turns.TurnRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnRetrieveParams params = TurnRetrieveParams.builder()
            .sessionId("session_id")
            .turnId("turn_id")
            .build();
        Turn turn = client.beta().agents().sessions().turns().retrieve(params);
    }
}
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

- `class Turn:`

  The canonical public representation of a session turn.

  - `String id`

    The ID of the turn.

  - `String agentId`

    The ID of the agent that ran the turn.

  - `Optional<Long> completedAt`

    The Unix timestamp, in seconds, when the turn reached a terminal state.

  - `long createdAt`

    The Unix timestamp, in seconds, used to order the turn by creation time. Subagent turns use their start time, falling back to completion time or the subagent opening time when the preceding timestamps are unavailable.

  - `Optional<SessionTurnError> error`

    A customer-safe error. Non-null only for a failed turn.

    - `Code code`

      A stable, machine-readable failure category.

      - `CONTEXT_LENGTH_EXCEEDED("context_length_exceeded")`

        The request exceeds the model's context window.

      - `SESSION_BUDGET_EXCEEDED("session_budget_exceeded")`

        The session has reached its usage budget.

      - `USAGE_LIMIT_EXCEEDED("usage_limit_exceeded")`

        The organization has reached a usage, plan, or billing limit.

      - `CREDIT_BALANCE_EXHAUSTED("credit_balance_exhausted")`

        The organization has no API credits remaining.

      - `RATE_LIMIT_EXCEEDED("rate_limit_exceeded")`

        The request exceeds the available rate limit.

      - `FLEX_UNAVAILABLE("flex_unavailable")`

        Flex processing is temporarily unavailable.

      - `SERVER_OVERLOADED("server_overloaded")`

        The model service is temporarily overloaded.

      - `CYBER_POLICY("cyber_policy")`

        The request was rejected by a safety policy.

      - `MISALIGNMENT_POLICY_VIOLATION("misalignment_policy_violation")`

        The request was blocked by the safety systems.

      - `CONNECTION_FAILED("connection_failed")`

        The request could not connect to the model service.

      - `SERVER_ERROR("server_error")`

        The model service encountered an unexpected error.

      - `AUTHENTICATION_ERROR("authentication_error")`

        The API credentials are invalid or lack the required access.

      - `INVALID_REQUEST("invalid_request")`

        The request contains invalid input or configuration.

      - `RESOURCE_NOT_FOUND("resource_not_found")`

        The requested model or resource is unavailable.

      - `SANDBOX_ERROR("sandbox_error")`

        The request could not complete in its execution environment.

      - `EXECUTOR_VERSION_INCOMPATIBLE("executor_version_incompatible")`

        The executor must be upgraded before it can run this turn.

      - `ACTIVE_TURN_NOT_STEERABLE("active_turn_not_steerable")`

        The session cannot accept additional input while a request is running.

      - `REQUEST_TIMEOUT("request_timeout")`

        The request timed out before the model service responded.

      - `INTERNAL_ERROR("internal_error")`

        An unexpected internal error prevented the session request from completing.

    - `String message`

      A customer-safe explanation of the failure.

  - `Object object_`

    The object type. Always `agent.session.turn`.

    - `AGENT_SESSION_TURN("agent.session.turn")`

  - `String sessionId`

    The ID of the session that owns the turn.

  - `Optional<Long> startedAt`

    The Unix timestamp, in seconds, when the turn started.

  - `Status status`

    The current status of the turn.

    - `QUEUED("queued")`

      The turn is waiting to start.

    - `IN_PROGRESS("in_progress")`

      The turn is in progress.

    - `WAITING("waiting")`

      The turn is waiting for external input.

    - `COMPLETED("completed")`

      The turn completed successfully.

    - `FAILED("failed")`

      The turn failed.

    - `CANCELLED("cancelled")`

      The turn was cancelled.

  - `Optional<String> subagentId`

    The ID of the subagent that ran the turn, if applicable.

  - `Optional<TokenUsage> usage`

    Best-effort token usage for the turn, or null if unknown. Recorded usage may change.

    - `long inputTokens`

      The number of input tokens used by the agent.

    - `InputTokensDetails inputTokensDetails`

      A breakdown of the agent's input token usage.

      - `long cachedTokens`

        The number of input tokens retrieved from the prompt cache.

    - `long outputTokens`

      The number of output tokens generated by the agent.

    - `OutputTokensDetails outputTokensDetails`

      A breakdown of the agent's output token usage.

      - `long reasoningTokens`

        The number of output tokens used for reasoning.

    - `long totalTokens`

      The total number of input and output tokens used by the agent.

# Vaults

## Create a vault

`Vault beta().agents().vaults().create(VaultCreateParamsparams = VaultCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vaults`

Creates a vault for the current project. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `VaultCreateParams params`

  - `Optional<Metadata> metadata`

    Key-value pairs to associate with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

### Returns

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.Vault;
import com.openai.models.beta.agents.vaults.VaultCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Vault vault = client.beta().agents().vaults().create();
    }
}
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

`VaultDeleted beta().agents().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vaults/{vault_id}`

Deletes a vault and all its credentials. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `VaultDeleteParams params`

  - `Optional<String> vaultId`

### Returns

- `class VaultDeleted:`

  Confirmation that a vault was deleted.

  - `String id`

    The ID of the deleted vault.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.deleted"constant`

    The object type. Always `vault.deleted`.

    - `VAULT_DELETED("vault.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.VaultDeleteParams;
import com.openai.models.beta.agents.vaults.VaultDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VaultDeleted vaultDeleted = client.beta().agents().vaults().delete("vault_id");
    }
}
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

`VaultListPage beta().agents().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults`

Lists vaults using ID-based pagination. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `VaultListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<VaultStatusFilter> status`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `enum VaultStatus:`

      Whether a vault or credential is active or archived.

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

    - `List<VaultStatus>`

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

### Returns

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.VaultListPage;
import com.openai.models.beta.agents.vaults.VaultListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        VaultListPage page = client.beta().agents().vaults().list();
    }
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

`Vault beta().agents().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}`

Retrieves a vault by its ID. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `VaultRetrieveParams params`

  - `Optional<String> vaultId`

### Returns

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.Vault;
import com.openai.models.beta.agents.vaults.VaultRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Vault vault = client.beta().agents().vaults().retrieve("vault_id");
    }
}
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

- `class Vault:`

  A collection of credentials for MCP servers and OpenAI-hosted environments.

  - `String id`

    The ID of the vault.

  - `long createdAt`

    The Unix timestamp, in seconds, when the vault was created.

  - `Metadata metadata`

    Key-value pairs associated with the vault, such as an application or team identifier.

  - `Optional<String> name`

    The human-readable name of the vault, if set.

  - `JsonValue; object_ "vault"constant`

    The object type. Always `vault`.

    - `VAULT("vault")`

### Vault Deleted

- `class VaultDeleted:`

  Confirmation that a vault was deleted.

  - `String id`

    The ID of the deleted vault.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.deleted"constant`

    The object type. Always `vault.deleted`.

    - `VAULT_DELETED("vault.deleted")`

### Vault Status

- `enum VaultStatus:`

  Whether a vault or credential is active or archived.

  - `ACTIVE("active")`

  - `ARCHIVED("archived")`

### Vault Status Filter

- `class VaultStatusFilter: A class that can be one of several variants.union`

  One or more lifecycle statuses to include when listing vaults or credentials.

  - `enum VaultStatus:`

    Whether a vault or credential is active or archived.

    - `ACTIVE("active")`

    - `ARCHIVED("archived")`

  - `List<VaultStatus>`

    - `ACTIVE("active")`

    - `ARCHIVED("archived")`

# Credentials

## Create a vault credential

`Credential beta().agents().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/vaults/{vault_id}/credentials`

Creates a vault credential. Secret values are write-only and are never returned. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `CredentialCreateParams params`

  - `Optional<String> vaultId`

  - `CredentialAuthCreateParam auth`

    The authentication method and write-only secret values to store.

  - `String name`

    The name is trimmed before storage. It must contain 1 to 256 UTF-8 bytes after trimming.

  - `Optional<Metadata> metadata`

    Up to 16 string key-value pairs, with keys up to 64 and values up to 512 characters. Defaults to an empty map.

### Returns

- `class Credential:`

  Metadata for a stored credential. Secret values are never returned.

  - `String id`

    The ID of the credential.

  - `CredentialAuth auth`

    The authentication method and non-secret configuration of the credential.

    - `McpOAuth`

      - `Optional<String> expiresAt`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `Optional<Refresh> refresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `String clientId`

          The OAuth client ID used when requesting a new access token.

        - `Optional<String> resource`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Optional<String> scope`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `String tokenEndpoint`

          The HTTPS OAuth token endpoint used for refresh.

        - `McpOAuthTokenEndpointAuth tokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_basic"constant`

              The type of the object. Always `client_secret_basic`.

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_post"constant`

              The type of the object. Always `client_secret_post`.

              - `CLIENT_SECRET_POST("client_secret_post")`

      - `JsonValue; type "mcp_oauth"constant`

        The type of the object. Always `mcp_oauth`.

        - `MCP_OAUTH("mcp_oauth")`

    - `StaticBearer`

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `JsonValue; type "static_bearer"constant`

        The type of the object. Always `static_bearer`.

        - `STATIC_BEARER("static_bearer")`

    - `EnvironmentVariable`

      - `CredentialNetworking networking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `JsonValue;`

          - `JsonValue; type "unrestricted"constant`

            The type of the object. Always `unrestricted`.

            - `UNRESTRICTED("unrestricted")`

        - `Limited`

          - `List<String> allowedHosts`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `JsonValue; type "limited"constant`

            The type of the object. Always `limited`.

            - `LIMITED("limited")`

      - `String secretName`

        The environment variable name that receives the placeholder in the sandbox.

      - `JsonValue; type "environment_variable"constant`

        The type of the object. Always `environment_variable`.

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata metadata`

    Application-defined key-value pairs associated with this credential.

  - `String name`

    The human-readable name of the credential.

  - `JsonValue; object_ "vault.credential"constant`

    The object type. Always `vault.credential`.

    - `VAULT_CREDENTIAL("vault.credential")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `String vaultId`

    The ID of the vault containing this credential.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.Credential;
import com.openai.models.beta.agents.vaults.credentials.CredentialAuthCreateParam;
import com.openai.models.beta.agents.vaults.credentials.CredentialCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialCreateParams params = CredentialCreateParams.builder()
            .vaultId("vault_id")
            .auth(CredentialAuthCreateParam.McpOAuth.builder()
                .accessToken("access_token")
                .mcpServerUrl("mcp_server_url")
                .build())
            .name("x")
            .build();
        Credential credential = client.beta().agents().vaults().credentials().create(params);
    }
}
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

`CredentialDeleted beta().agents().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/vaults/{vault_id}/credentials/{credential_id}`

Deletes a vault credential. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `CredentialDeleteParams params`

  - `String vaultId`

  - `Optional<String> credentialId`

### Returns

- `class CredentialDeleted:`

  Confirmation that a vault credential was deleted.

  - `String id`

    The ID of the deleted credential.

  - `boolean deleted`

    Whether the resource was deleted. Always `true`.

  - `JsonValue; object_ "vault.credential.deleted"constant`

    The object type. Always `vault.credential.deleted`.

    - `VAULT_CREDENTIAL_DELETED("vault.credential.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.CredentialDeleteParams;
import com.openai.models.beta.agents.vaults.credentials.CredentialDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialDeleteParams params = CredentialDeleteParams.builder()
            .vaultId("vault_id")
            .credentialId("credential_id")
            .build();
        CredentialDeleted credentialDeleted = client.beta().agents().vaults().credentials().delete(params);
    }
}
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

`CredentialListPage beta().agents().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/vaults/{vault_id}/credentials`

Lists a vault's credentials using ID-based pagination without returning secret values. See [vaults](/api/docs/guides/agents-api/tools/vaults).

### Parameters

- `CredentialListParams params`

  - `Optional<String> vaultId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return. Defaults to 20. Values are clamped between 1 and 100.

  - `Optional<Order> order`

    Sort order by the `created_at` timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<VaultStatusFilter> status`

    Filter by one status or a list, such as `status=active` or `status[]=active&status[]=archived`. Both statuses are included by default.

    - `enum VaultStatus:`

      Whether a vault or credential is active or archived.

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

    - `List<VaultStatus>`

      - `ACTIVE("active")`

      - `ARCHIVED("archived")`

### Returns

- `class Credential:`

  Metadata for a stored credential. Secret values are never returned.

  - `String id`

    The ID of the credential.

  - `CredentialAuth auth`

    The authentication method and non-secret configuration of the credential.

    - `McpOAuth`

      - `Optional<String> expiresAt`

        When the OAuth access token expires, as an RFC 3339 timestamp, if known.

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `Optional<Refresh> refresh`

        Public refresh metadata without refresh tokens or OAuth client secrets.

        - `String clientId`

          The OAuth client ID used when requesting a new access token.

        - `Optional<String> resource`

          The resource URI sent to the OAuth token endpoint during refresh, if configured.

        - `Optional<String> scope`

          Space-separated OAuth scopes requested during refresh, if configured.

        - `String tokenEndpoint`

          The HTTPS OAuth token endpoint used for refresh.

        - `McpOAuthTokenEndpointAuth tokenEndpointAuth`

          How the OAuth client authenticates to the token endpoint, excluding its client secret.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_basic"constant`

              The type of the object. Always `client_secret_basic`.

              - `CLIENT_SECRET_BASIC("client_secret_basic")`

          - `JsonValue;`

            - `JsonValue; type "client_secret_post"constant`

              The type of the object. Always `client_secret_post`.

              - `CLIENT_SECRET_POST("client_secret_post")`

      - `JsonValue; type "mcp_oauth"constant`

        The type of the object. Always `mcp_oauth`.

        - `MCP_OAUTH("mcp_oauth")`

    - `StaticBearer`

      - `String mcpServerUrl`

        The HTTPS MCP server URL authorized by this credential.

      - `JsonValue; type "static_bearer"constant`

        The type of the object. Always `static_bearer`.

        - `STATIC_BEARER("static_bearer")`

    - `EnvironmentVariable`

      - `CredentialNetworking networking`

        The destinations where the proxy can substitute the secret, subject to the environment network policy.

        - `JsonValue;`

          - `JsonValue; type "unrestricted"constant`

            The type of the object. Always `unrestricted`.

            - `UNRESTRICTED("unrestricted")`

        - `Limited`

          - `List<String> allowedHosts`

            The 1 to 16 distinct allowed hostnames or IPv4 addresses, normalized to lowercase. Entries contain no scheme, path, port, or wildcard. IPv6 addresses are not supported.

          - `JsonValue; type "limited"constant`

            The type of the object. Always `limited`.

            - `LIMITED("limited")`

      - `String secretName`

        The environment variable name that receives the placeholder in the sandbox.

      - `JsonValue; type "environment_variable"constant`

        The type of the object. Always `environment_variable`.

        - `ENVIRONMENT_VARIABLE("environment_variable")`

  - `long createdAt`

    The Unix timestamp, in seconds, when the credential was created.

  - `Metadata metadata`

    Application-defined key-value pairs associated with this credential.

  - `String name`

    The human-readable name of the credential.

  - `JsonValue; object_ "vault.credential"constant`

    The object type. Always `vault.credential`.

    - `VAULT_CREDENTIAL("vault.credential")`

  - `long updatedAt`

    The Unix timestamp, in seconds, when the credential was last updated.

  - `String vaultId`

    The ID of the vault containing this credential.

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.vaults.credentials.CredentialListPage;
import com.openai.models.beta.agents.vaults.credentials.CredentialListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        CredentialListPage page = client.beta().agents().vaults().credentials().list("vault_id");
    }
}
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
