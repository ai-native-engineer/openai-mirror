<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/automations/ -->

# Automations

## Create an automation

`Automation beta().agents().automations().create(AutomationCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/automations`

Saves an active automation without invoking it immediately.

### Parameters

- `AutomationCreateParams params`

  - `AutomationScheduleParam automationScheduleParam`

    Creates an automation without invoking it immediately.

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.AgentSessionInputMessageParam;
import com.openai.models.beta.agents.automations.Automation;
import com.openai.models.beta.agents.automations.AutomationCreateParams;
import com.openai.models.beta.agents.automations.AutomationScheduleParam;
import com.openai.models.beta.agents.automations.AutomationTargetParam;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AutomationCreateParams params = AutomationCreateParams.builder()
            .automationScheduleParam(AutomationScheduleParam.Periodic.builder()
                .expression("x")
                .name("x")
                .target(AutomationTargetParam.NewSession.builder()
                    .environmentNone()
                    .addInput(AgentSessionInputMessageParam.builder()
                        .addTextContent("text")
                        .build())
                    .build())
                .timezone("x")
                .build())
            .build();
        Automation automation = client.beta().agents().automations().create(params);
    }
}
```

#### 201 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
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
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Delete an automation

`AutomationDeleted beta().agents().automations().delete(AutomationDeleteParamsparams = AutomationDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**delete** `/agents/automations/{automation_id}`

Deletes the automation and prevents future invocations without deleting its target session.

### Parameters

- `AutomationDeleteParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class AutomationDeleted:`

  - `String id`

    The deleted automation ID.

    `minLength: 0`

  - `boolean deleted`

    Always true.

  - `JsonValue; object_ "agent.automation.deleted"constant`

    Always `agent.automation.deleted`.

    - `AGENT_AUTOMATION_DELETED("agent.automation.deleted")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.AutomationDeleteParams;
import com.openai.models.beta.agents.automations.AutomationDeleted;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AutomationDeleted automationDeleted = client.beta().agents().automations().delete("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "deleted": true,
  "object": "agent.automation.deleted"
}
```

## List automations

`AutomationListPage beta().agents().automations().list(AutomationListParamsparams = AutomationListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/automations`

Lists project-owned automations, optionally filtered by target session.

### Parameters

- `AutomationListParams params`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

  - `Optional<String> sessionId`

    Matches existing-session targets, including agent-created automations.

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.AutomationListPage;
import com.openai.models.beta.agents.automations.AutomationListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AutomationListPage page = client.beta().agents().automations().list();
    }
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "created_at": 0,
      "created_by": {
        "type": "developer"
      },
      "expression": "expression",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "object": "agent.automation",
      "status": "active",
      "target": {
        "agent": {
          "instructions": "instructions",
          "model": "model",
          "multi_agent": {
            "enabled": true,
            "max_concurrent_subagents": 1
          },
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
              "type": "function",
              "async": true
            }
          ],
          "compaction": {
            "async": true
          },
          "experimental": {
            "time_awareness": true
          }
        },
        "agent_id": "agent_id",
        "environment": {
          "type": "none"
        },
        "input": [
          {
            "content": [
              {
                "text": "text",
                "type": "input_text"
              }
            ],
            "role": "user",
            "type": "message"
          }
        ],
        "metadata": {
          "foo": "string"
        },
        "type": "new_session",
        "vault_ids": [
          "string"
        ]
      },
      "timezone": "timezone",
      "type": "periodic"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Pause an automation

`Automation beta().agents().automations().pause(AutomationPauseParamsparams = AutomationPauseParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/automations/{automation_id}/pause`

Pauses future scheduled delivery without stopping an active session.

### Parameters

- `AutomationPauseParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.Automation;
import com.openai.models.beta.agents.automations.AutomationPauseParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Automation automation = client.beta().agents().automations().pause("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
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
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Resume an automation

`Automation beta().agents().automations().resume(AutomationResumeParamsparams = AutomationResumeParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/automations/{automation_id}/resume`

Resumes scheduled delivery; one-time automations without a pending invocation require a future run_at.

### Parameters

- `AutomationResumeParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.Automation;
import com.openai.models.beta.agents.automations.AutomationResumeParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Automation automation = client.beta().agents().automations().resume("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
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
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Get an automation

`Automation beta().agents().automations().retrieve(AutomationRetrieveParamsparams = AutomationRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/automations/{automation_id}`

Retrieves a project-owned automation.

### Parameters

- `AutomationRetrieveParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.Automation;
import com.openai.models.beta.agents.automations.AutomationRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Automation automation = client.beta().agents().automations().retrieve("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
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
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Update an automation

`Automation beta().agents().automations().update(AutomationUpdateParamsparams = AutomationUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/automations/{automation_id}`

Updates supplied fields; target and metadata replace the whole field.

### Parameters

- `AutomationUpdateParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> expression`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 256`

  - `Optional<Metadata> metadata`

    Replaces all metadata; omit to leave unchanged.

  - `Optional<String> name`

    `minLength: 1`, `maxLength: 256`

  - `Optional<Long> runAt`

    A future Unix timestamp in seconds; accepted only before a one-time scheduled invocation exists.

    `format: int64`

  - `Optional<AutomationTargetParam> target`

    Replaces the complete target, retaining its type and any creator session.

  - `Optional<String> timezone`

    Only accepted for periodic automations.

    `minLength: 1`, `maxLength: 128`

### Returns

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.Automation;
import com.openai.models.beta.agents.automations.AutomationUpdateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        Automation automation = client.beta().agents().automations().update("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "created_at": 0,
  "created_by": {
    "type": "developer"
  },
  "expression": "expression",
  "metadata": {
    "foo": "string"
  },
  "name": "name",
  "object": "agent.automation",
  "status": "active",
  "target": {
    "agent": {
      "instructions": "instructions",
      "model": "model",
      "multi_agent": {
        "enabled": true,
        "max_concurrent_subagents": 1
      },
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
          "type": "function",
          "async": true
        }
      ],
      "compaction": {
        "async": true
      },
      "experimental": {
        "time_awareness": true
      }
    },
    "agent_id": "agent_id",
    "environment": {
      "type": "none"
    },
    "input": [
      {
        "content": [
          {
            "text": "text",
            "type": "input_text"
          }
        ],
        "role": "user",
        "type": "message"
      }
    ],
    "metadata": {
      "foo": "string"
    },
    "type": "new_session",
    "vault_ids": [
      "string"
    ]
  },
  "timezone": "timezone",
  "type": "periodic"
}
```

## Domain Types

### Automation

- `class Automation: A class that can be one of several variants.union`

  A saved automation and its schedule.

  - `class PeriodicAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

      - `JsonValue;`

        - `JsonValue; type "developer"constant`

          The type of the object. Always `developer`.

          - `DEVELOPER("developer")`

      - `Agent`

        - `String sessionId`

          The creator session, which is also the automation's target.

          `minLength: 0`

        - `String toolCallId`

          The tool call that created the automation.

          `minLength: 0`

        - `JsonValue; type "agent"constant`

          The type of the object. Always `agent`.

          - `AGENT("agent")`

    - `String expression`

      The cron expression determining scheduled occurrences.

      `minLength: 0`

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `Status status`

      Whether scheduled delivery is active or paused.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

      - `NewSession`

        - `Optional<AutomationAgentConfig> agent`

          The inline agent configuration, or null when agent_id is configured.

          - `Optional<String> instructions`

            Custom instructions, or null when absent.

            `minLength: 0`

          - `String model`

            The requested model name.

            `minLength: 0`

          - `MultiAgentConfig multiAgent`

            The configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled. Defaults to false.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

          - `AgentReasoning reasoning`

            The configured reasoning policy.

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

            The configured service-tier policy.

            - `AUTO("auto")`

            - `DEFAULT("default")`

            - `FLEX("flex")`

            - `PRIORITY("priority")`

            - `FAST("fast")`

            - `ULTRAFAST("ultrafast")`

          - `AgentText text`

            The configured output format and verbosity.

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

            Configured tools, excluding confidential credentials.

            `minItems: 0`, `maxItems: 2000`

            - `Function`

              - `boolean deferLoading`

                Whether the function is deferred and discovered through tool search.

              - `String description`

                A description of what the function does.

                `minLength: 0`

              - `String name`

                The name of the function.

                `minLength: 0`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result.

            - `ProgrammaticToolCalling`

              - `boolean enabled`

                Whether tools can be called from model-generated code.

              - `JsonValue; type "programmatic_tool_calling"constant`

                The type of the object. Always `programmatic_tool_calling`.

                - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

            - `Mcp`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call.

                `minItems: 0`, `maxItems: 2000`

              - `ConnectionOrigin connectionOrigin`

                Where outbound MCP HTTP connections originate.

                - `SERVICE("service")`

                - `ENVIRONMENT("environment")`

              - `Optional<String> credentialId`

                The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`

              - `RequestMetadata requestMetadata`

                Metadata included with requests to this MCP server.

              - `boolean required`

                Whether this MCP server must initialize before the first turn.

              - `String serverLabel`

                A label used to identify the MCP server in tool calls.

                `minLength: 0`

              - `McpTransport transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                - `Stdio`

                  - `List<String> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 2000`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`

                  - `List<String> envVars`

                    Environment variable names inherited from the execution environment.

                    `minItems: 0`, `maxItems: 2000`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

            - `WebSearch`

              - `Optional<List<String>> allowedDomains`

                Allowed search domains, or `null` when the search is unrestricted.

                `minItems: 0`, `maxItems: 2000`

              - `ContextSize contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results, if provided.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

          - `Optional<Compaction> compaction`

            The effective context compaction settings.

            - `boolean async`

              Whether context is compacted in the background. Defaults to true.

          - `Optional<Experimental> experimental`

            The effective experimental settings for the agent.

            - `boolean timeAwareness`

              Whether the model receives periodic current-time reminders.

        - `Optional<String> agentId`

          The saved agent reference, or null when an inline agent is configured.

          `minLength: 0`

        - `AutomationEnvironment environment`

          Configuration or references used to select the execution environment.

          - `JsonValue;`

            - `JsonValue; type "none"constant`

              The type of the object. Always `none`.

              - `NONE("none")`

          - `OpenAIHosted`

            - `Optional<List<String>> capabilityDirectories`

              Directory overrides, or null to inherit the template or creation default.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<ContainerSize> containerSize`

              The configured container size, or null to use the creation default.

              - `SMALL("small")`

              - `MEDIUM("medium")`

              - `LARGE("large")`

            - `Optional<Desktop> desktop`

              Desktop overrides, or null to inherit the template or creation default.

              - `boolean enabled`

                Whether the environment provisions a desktop and browser proxy.

            - `Optional<String> environmentId`

              An existing environment reference, or null when provisioning a new environment.

              `minLength: 0`

            - `Optional<String> environmentTemplateId`

              A template reference, or null when no template is selected.

              `minLength: 0`

            - `Optional<List<File>> files`

              File overrides, excluding contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class FileId:`

                A project-scoped Files API reference resolved separately for each session.

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 0`

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `class Inline:`

                Metadata for confidential inline file contents.

                - `String path`

                  The file's absolute path inside the environment.

                  `minLength: 0`

                - `long sizeBytes`

                  The decoded size of the inline file in bytes.

                  `format: int64`, `minimum: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network overrides, or null to inherit the template or creation default.

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

                `minItems: 0`, `maxItems: 2000`

            - `Optional<Packages> packages`

              Package overrides, or null to inherit the template or creation default.

              - `List<String> npm`

                npm packages installed globally in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> python`

                Python packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

              - `List<String> system`

                System packages installed in the environment.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPlugin>> plugins`

              Plugin overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `String description`

                The installed plugin description.

                `minLength: 0`

              - `String name`

                The installed plugin name.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<Skill>> skills`

              Skill overrides, excluding archive contents, or null to inherit.

              `minItems: 0`, `maxItems: 2000`

              - `class SkillReference:`

                A skill resolved afresh from the Skills API whenever a session starts.

                - `String skillId`

                  The referenced skill ID.

                  `minLength: 0`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The requested version selector, including `latest`.

                  `minLength: 0`

              - `class Inline:`

                Safe metadata for an inline skill archive.

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `JsonValue; type "openai_hosted"constant`

              The type of the object. Always `openai_hosted`.

              - `OPENAI_HOSTED("openai_hosted")`

          - `SelfHosted`

            - `List<String> capabilityDirectories`

              Directories that expose capabilities to the agent.

              `minItems: 0`, `maxItems: 2000`

            - `Optional<String> environmentId`

              An existing registration, or null to create a session-owned environment.

              `minLength: 0`

            - `JsonValue; type "self_hosted"constant`

              The type of the object. Always `self_hosted`.

              - `SELF_HOSTED("self_hosted")`

            - `String workspaceDirectory`

              The absolute project directory in the environment.

              `minLength: 0`

        - `List<Input> input`

          Initial input delivered to each new session.

          `minItems: 0`, `maxItems: 2000`

          - `List<InputContent> content`

            The content of the message.

            `minItems: 0`, `maxItems: 2000`

            - `InputText`

              - `String text`

                The text supplied to the agent.

                `minLength: 0`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                `minLength: 0`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `JsonValue; type "message"constant`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `Metadata metadata`

          Metadata attached to each new session.

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `List<String> vaultIds`

          Vaults made available to each new session.

          `minItems: 0`, `maxItems: 2000`

      - `ExistingSession`

        - `String instructions`

          Saved instructions delivered as an automation notification.

          `minLength: 0`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The timezone used to interpret the expression.

      `minLength: 0`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

  - `class OneTimeAutomation:`

    Fields shared by periodic and one-time automations.

    - `String id`

      The automation ID.

      `minLength: 0`

    - `long createdAt`

      The creation time as a Unix timestamp in seconds.

      `format: int64`

    - `AutomationCreatedBy createdBy`

      Service-recorded provenance; callers cannot supply this field.

    - `Metadata metadata`

      Custom string key-value pairs attached to the automation.

    - `String name`

      The automation's display name.

      `minLength: 0`

    - `JsonValue; object_ "agent.automation"constant`

      Always `agent.automation`.

      - `AGENT_AUTOMATION("agent.automation")`

    - `long runAt`

      The Unix timestamp, in seconds, of the scheduled occurrence.

      `format: int64`

    - `Status status`

      Completion means the schedule has finished, not the agent's work.

      - `ACTIVE("active")`

      - `PAUSED("paused")`

      - `COMPLETED("completed")`

    - `AutomationTarget target`

      The session configuration or existing session receiving invocations.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

### Automation Agent Config

- `class AutomationAgentConfig:`

  Inline agent configuration without a generated session-local identity.

  - `Optional<String> instructions`

    Custom instructions, or null when absent.

    `minLength: 0`

  - `String model`

    The requested model name.

    `minLength: 0`

  - `MultiAgentConfig multiAgent`

    The configuration for creating and coordinating subagents.

    - `boolean enabled`

      Whether subagent tools are enabled. Defaults to false.

    - `Optional<Long> maxConcurrentSubagents`

      Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

      `format: int64`, `minimum: 1`, `maximum: 4294967295`

  - `AgentReasoning reasoning`

    The configured reasoning policy.

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

    The configured service-tier policy.

    - `AUTO("auto")`

    - `DEFAULT("default")`

    - `FLEX("flex")`

    - `PRIORITY("priority")`

    - `FAST("fast")`

    - `ULTRAFAST("ultrafast")`

  - `AgentText text`

    The configured output format and verbosity.

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

    Configured tools, excluding confidential credentials.

    `minItems: 0`, `maxItems: 2000`

    - `Function`

      - `boolean deferLoading`

        Whether the function is deferred and discovered through tool search.

      - `String description`

        A description of what the function does.

        `minLength: 0`

      - `String name`

        The name of the function.

        `minLength: 0`

      - `Parameters parameters`

        A JSON Schema object describing the function's arguments.

      - `JsonValue; type "function"constant`

        The type of the object. Always `function`.

        - `FUNCTION("function")`

      - `Optional<Boolean> async`

        Whether the agent continues without waiting for the function result.

    - `ProgrammaticToolCalling`

      - `boolean enabled`

        Whether tools can be called from model-generated code.

      - `JsonValue; type "programmatic_tool_calling"constant`

        The type of the object. Always `programmatic_tool_calling`.

        - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

    - `Mcp`

      - `Optional<List<String>> allowedTools`

        The MCP tools the agent may call.

        `minItems: 0`, `maxItems: 2000`

      - `ConnectionOrigin connectionOrigin`

        Where outbound MCP HTTP connections originate.

        - `SERVICE("service")`

        - `ENVIRONMENT("environment")`

      - `Optional<String> credentialId`

        The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

        `minLength: 0`

      - `RequestMetadata requestMetadata`

        Metadata included with requests to this MCP server.

      - `boolean required`

        Whether this MCP server must initialize before the first turn.

      - `String serverLabel`

        A label used to identify the MCP server in tool calls.

        `minLength: 0`

      - `McpTransport transport`

        The transport used to connect to the MCP server.

        - `Http`

          - `String serverUrl`

            The URL of the MCP server.

            `minLength: 0`

          - `JsonValue; type "http"constant`

            The type of the object. Always `http`.

            - `HTTP("http")`

        - `Stdio`

          - `List<String> args`

            Arguments passed to the MCP server command.

            `minItems: 0`, `maxItems: 2000`

          - `String command`

            The command used to start the MCP server.

            `minLength: 0`

          - `String cwd`

            The working directory used to start the MCP server.

            `minLength: 0`

          - `List<String> envVars`

            Environment variable names inherited from the execution environment.

            `minItems: 0`, `maxItems: 2000`

          - `JsonValue; type "stdio"constant`

            The type of the object. Always `stdio`.

            - `STDIO("stdio")`

      - `JsonValue; type "mcp"constant`

        The type of the object. Always `mcp`.

        - `MCP("mcp")`

    - `WebSearch`

      - `Optional<List<String>> allowedDomains`

        Allowed search domains, or `null` when the search is unrestricted.

        `minItems: 0`, `maxItems: 2000`

      - `ContextSize contextSize`

        The amount of search context made available to the model. Defaults to `medium`.

        - `LOW("low")`

        - `MEDIUM("medium")`

        - `HIGH("high")`

      - `Optional<Location> location`

        Approximate location used to localize search results, if provided.

        - `Optional<String> city`

          The city name.

          `minLength: 0`

        - `Optional<String> country`

          The two-letter ISO country code, such as `US`.

          `minLength: 0`

        - `Optional<String> region`

          The region or state name.

          `minLength: 0`

        - `Optional<String> timezone`

          The IANA timezone, such as `America/Los_Angeles`.

          `minLength: 0`

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

    - `JsonValue;`

      - `JsonValue; type "automations"constant`

        The type of the object. Always `automations`.

        - `AUTOMATIONS("automations")`

  - `Optional<Compaction> compaction`

    The effective context compaction settings.

    - `boolean async`

      Whether context is compacted in the background. Defaults to true.

  - `Optional<Experimental> experimental`

    The effective experimental settings for the agent.

    - `boolean timeAwareness`

      Whether the model receives periodic current-time reminders.

### Automation Created By

- `class AutomationCreatedBy: A class that can be one of several variants.union`

  How the automation was created, independently of how an invocation started.

  - `JsonValue;`

    - `JsonValue; type "developer"constant`

      The type of the object. Always `developer`.

      - `DEVELOPER("developer")`

  - `Agent`

    - `String sessionId`

      The creator session, which is also the automation's target.

      `minLength: 0`

    - `String toolCallId`

      The tool call that created the automation.

      `minLength: 0`

    - `JsonValue; type "agent"constant`

      The type of the object. Always `agent`.

      - `AGENT("agent")`

### Automation Deleted

- `class AutomationDeleted:`

  - `String id`

    The deleted automation ID.

    `minLength: 0`

  - `boolean deleted`

    Always true.

  - `JsonValue; object_ "agent.automation.deleted"constant`

    Always `agent.automation.deleted`.

    - `AGENT_AUTOMATION_DELETED("agent.automation.deleted")`

### Automation Environment

- `class AutomationEnvironment: A class that can be one of several variants.union`

  Environment selection saved before an invocation creates its session.

  - `JsonValue;`

    - `JsonValue; type "none"constant`

      The type of the object. Always `none`.

      - `NONE("none")`

  - `OpenAIHosted`

    - `Optional<List<String>> capabilityDirectories`

      Directory overrides, or null to inherit the template or creation default.

      `minItems: 0`, `maxItems: 2000`

    - `Optional<ContainerSize> containerSize`

      The configured container size, or null to use the creation default.

      - `SMALL("small")`

      - `MEDIUM("medium")`

      - `LARGE("large")`

    - `Optional<Desktop> desktop`

      Desktop overrides, or null to inherit the template or creation default.

      - `boolean enabled`

        Whether the environment provisions a desktop and browser proxy.

    - `Optional<String> environmentId`

      An existing environment reference, or null when provisioning a new environment.

      `minLength: 0`

    - `Optional<String> environmentTemplateId`

      A template reference, or null when no template is selected.

      `minLength: 0`

    - `Optional<List<File>> files`

      File overrides, excluding contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `class FileId:`

        A project-scoped Files API reference resolved separately for each session.

        - `String fileId`

          The ID of the uploaded file.

          `minLength: 0`

        - `String path`

          The file's absolute path inside the environment.

          `minLength: 0`

        - `JsonValue; type "file_id"constant`

          The type of the object. Always `file_id`.

          - `FILE_ID("file_id")`

      - `class Inline:`

        Metadata for confidential inline file contents.

        - `String path`

          The file's absolute path inside the environment.

          `minLength: 0`

        - `long sizeBytes`

          The decoded size of the inline file in bytes.

          `format: int64`, `minimum: 0`

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `Optional<Network> network`

      Network overrides, or null to inherit the template or creation default.

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

        `minItems: 0`, `maxItems: 2000`

    - `Optional<Packages> packages`

      Package overrides, or null to inherit the template or creation default.

      - `List<String> npm`

        npm packages installed globally in the environment.

        `minItems: 0`, `maxItems: 16384`

      - `List<String> python`

        Python packages installed in the environment.

        `minItems: 0`, `maxItems: 16384`

      - `List<String> system`

        System packages installed in the environment.

        `minItems: 0`, `maxItems: 16384`

    - `Optional<List<HostedPlugin>> plugins`

      Plugin overrides, excluding archive contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `String description`

        The installed plugin description.

        `minLength: 0`

      - `String name`

        The installed plugin name.

        `minLength: 0`

      - `JsonValue; type "inline"constant`

        The type of the object. Always `inline`.

        - `INLINE("inline")`

    - `Optional<List<Skill>> skills`

      Skill overrides, excluding archive contents, or null to inherit.

      `minItems: 0`, `maxItems: 2000`

      - `class SkillReference:`

        A skill resolved afresh from the Skills API whenever a session starts.

        - `String skillId`

          The referenced skill ID.

          `minLength: 0`

        - `JsonValue; type "skill_reference"constant`

          The type of the object. Always `skill_reference`.

          - `SKILL_REFERENCE("skill_reference")`

        - `Optional<String> version`

          The requested version selector, including `latest`.

          `minLength: 0`

      - `class Inline:`

        Safe metadata for an inline skill archive.

        - `String description`

          The skill description declared in `SKILL.md`.

          `minLength: 0`

        - `String name`

          The skill name declared in `SKILL.md`.

          `minLength: 0`

        - `JsonValue; type "inline"constant`

          The type of the object. Always `inline`.

          - `INLINE("inline")`

    - `JsonValue; type "openai_hosted"constant`

      The type of the object. Always `openai_hosted`.

      - `OPENAI_HOSTED("openai_hosted")`

  - `SelfHosted`

    - `List<String> capabilityDirectories`

      Directories that expose capabilities to the agent.

      `minItems: 0`, `maxItems: 2000`

    - `Optional<String> environmentId`

      An existing registration, or null to create a session-owned environment.

      `minLength: 0`

    - `JsonValue; type "self_hosted"constant`

      The type of the object. Always `self_hosted`.

      - `SELF_HOSTED("self_hosted")`

    - `String workspaceDirectory`

      The absolute project directory in the environment.

      `minLength: 0`

### Automation Schedule Param

- `class AutomationScheduleParam: A class that can be one of several variants.union`

  Creates an automation without invoking it immediately.

  - `Periodic`

    - `String expression`

      A standard five-field cron expression defining scheduled occurrences.

      `minLength: 1`, `maxLength: 256`

    - `String name`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `AutomationTargetParam target`

      The session an automation invocation targets.

      - `NewSession`

        - `EnvironmentParam environment`

          The execution environment for each new session.

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

              `minItems: 0`, `maxItems: 16384`

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

            - `Optional<String> environmentId`

              An existing prewarmed environment. Cannot be combined with a template or inline configuration.

              `minLength: 9`, `maxLength: 256`

            - `Optional<String> environmentTemplateId`

              A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

              `minLength: 0`, `maxLength: 64`

            - `Optional<List<HostedEnvironmentFileParam>> files`

              Files available before the agent starts. Defaults to an empty list.

              `minItems: 0`, `maxItems: 50`

              - `FileId`

                - `String fileId`

                  The ID of the uploaded file.

                  `minLength: 1`, `maxLength: 256`

                - `String path`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `JsonValue; type "file_id"constant`

                  The type of the object. Always `file_id`.

                  - `FILE_ID("file_id")`

              - `Inline`

                - `String data`

                  The standard-base64-encoded file contents.

                  `minLength: 0`, `maxLength: 6990508`

                - `String path`

                  The absolute destination path inside `/workspace`.

                  `minLength: 1`, `maxLength: 4096`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

            - `Optional<Network> network`

              Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

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

                `minItems: 0`, `maxItems: 16384`

              - `Optional<List<String>> blockedDomains`

                Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

                `minItems: 0`, `maxItems: 100`

            - `Optional<Packages> packages`

              Packages to install in the environment. Defaults to empty package lists.

              - `Optional<List<String>> npm`

                npm packages to install globally. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `Optional<List<String>> python`

                Python packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

              - `Optional<List<String>> system`

                System packages to install. Defaults to an empty list.

                `minItems: 0`, `maxItems: 16384`

            - `Optional<List<HostedPluginParam>> plugins`

              Plugins provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 32`

              - `String description`

                The plugin description declared in `.codex-plugin/plugin.json`.

                `minLength: 0`, `maxLength: 1048576`

              - `String name`

                The plugin name declared in `.codex-plugin/plugin.json`.

                `minLength: 1`, `maxLength: 64`

              - `InlineCapabilitySourceParam source`

                Provides ZIP bytes encoded with standard base64.

                - `String data`

                  Standard-base64 encoded ZIP archive bytes.

                  `minLength: 1`, `maxLength: 70254592`

                - `JsonValue; mediaType "application/zip"constant`

                  The archive media type, always `application/zip`.

                  - `APPLICATION_ZIP("application/zip")`

                - `JsonValue; type "base64"constant`

                  The type of the object. Always `base64`.

                  - `BASE64("base64")`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

            - `Optional<List<SetupCommandParam>> setupCommands`

              Ordered, confidential setup commands. Command bodies are never returned.

              `minItems: 0`, `maxItems: 16`

              - `String command`

                The shell command to execute.

                `minLength: 0`, `maxLength: 65536`

              - `Optional<String> cwd`

                The absolute working directory. Defaults to `/workspace`.

                `minLength: 0`, `maxLength: 4096`

            - `Optional<List<HostedSkillParam>> skills`

              Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

              `minItems: 0`, `maxItems: 200`

              - `SkillReference`

                - `String skillId`

                  The ID of the skill created through `/v1/skills`.

                  `minLength: 1`, `maxLength: 64`

                - `JsonValue; type "skill_reference"constant`

                  The type of the object. Always `skill_reference`.

                  - `SKILL_REFERENCE("skill_reference")`

                - `Optional<String> version`

                  The skill version, a positive integer or `latest`; omission selects the default.

                  `minLength: 0`, `maxLength: 1048576`

              - `Inline`

                - `String description`

                  The skill description declared in `SKILL.md`.

                  `minLength: 0`, `maxLength: 1048576`

                - `String name`

                  The skill name declared in `SKILL.md`.

                  `minLength: 1`, `maxLength: 64`

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

              `minLength: 0`, `maxLength: 1048576`

            - `Optional<List<String>> capabilityDirectories`

              Directories that contain capabilities exposed to the agent. Defaults to an empty list.

              `minItems: 0`, `maxItems: 16384`

        - `List<AgentSessionInputMessageParam> input`

          Initial user messages submitted with each new session.

          `minItems: 0`, `maxItems: 16384`

          - `List<InputContentParam> content`

            The content of the message.

            `minItems: 0`, `maxItems: 16384`

            - `InputText`

              - `String text`

                The text sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `JsonValue; type "input_text"constant`

                The type of the object. Always `input_text`.

                - `INPUT_TEXT("input_text")`

            - `InputImage`

              - `String imageUrl`

                The URL of the image sent to the model.

                `minLength: 0`, `maxLength: 1048576`

              - `JsonValue; type "input_image"constant`

                The type of the object. Always `input_image`.

                - `INPUT_IMAGE("input_image")`

          - `JsonValue; role "user"constant`

            The role of the message author. Always `user`.

            - `USER("user")`

          - `Optional<Type> type`

            The type of the input item. Always `message`.

            - `MESSAGE("message")`

        - `JsonValue; type "new_session"constant`

          The type of the object. Always `new_session`.

          - `NEW_SESSION("new_session")`

        - `Optional<Agent> agent`

          Inline agent configuration. Provide exactly one of agent and agent_id.

          - `Optional<Compaction> compaction`

            Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

            - `Optional<Boolean> async`

              Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

          - `Optional<Experimental> experimental`

            Experimental settings to merge by key. Omitted settings keep their current values.

            - `Optional<Boolean> timeAwareness`

              Whether to give the model periodic current-time reminders. Omit to keep the current setting.

          - `Optional<String> instructions`

            Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

            `minLength: 0`, `maxLength: 1048576`

          - `Optional<String> model`

            The model to use for the agent. The requested model name is preserved.

            `minLength: 0`, `maxLength: 1048576`

          - `Optional<MultiAgentConfigParam> multiAgent`

            Configuration for creating and coordinating subagents.

            - `boolean enabled`

              Whether subagent tools are enabled.

            - `Optional<Long> maxConcurrentSubagents`

              Maximum number of subagents that may run concurrently. Defaults to 6.

              `format: int64`, `minimum: 1`, `maximum: 4294967295`

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

            Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

            `minItems: 0`, `maxItems: 16384`

            - `Function`

              - `String description`

                A description of what the function does.

                `minLength: 0`, `maxLength: 1048576`

              - `String name`

                The name of the function.

                `minLength: 0`, `maxLength: 1048576`

              - `Parameters parameters`

                A JSON Schema object describing the function's arguments.

              - `JsonValue; type "function"constant`

                The type of the object. Always `function`.

                - `FUNCTION("function")`

              - `Optional<Boolean> async`

                Whether the agent continues without waiting for the function result. Defaults to `false`.

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

                `minLength: 0`, `maxLength: 1048576`

              - `McpTransportParam transport`

                The transport used to connect to the MCP server.

                - `Http`

                  - `String serverUrl`

                    The URL of the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `JsonValue; type "http"constant`

                    The type of the object. Always `http`.

                    - `HTTP("http")`

                  - `Optional<String> authorization`

                    The authorization value sent to the MCP server, if any.

                    `minLength: 0`, `maxLength: 1048576`

                  - `Optional<Headers> headers`

                    Additional HTTP headers sent to the MCP server.

                - `Stdio`

                  - `String command`

                    The command used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `String cwd`

                    The working directory used to start the MCP server.

                    `minLength: 0`, `maxLength: 1048576`

                  - `JsonValue; type "stdio"constant`

                    The type of the object. Always `stdio`.

                    - `STDIO("stdio")`

                  - `Optional<List<String>> args`

                    Arguments passed to the MCP server command.

                    `minItems: 0`, `maxItems: 16384`

                  - `Optional<Env> env`

                    Environment variables set for the MCP server process.

                  - `Optional<List<String>> envVars`

                    Environment variable names to inherit from the selected execution environment.

                    `minItems: 0`, `maxItems: 16384`

              - `JsonValue; type "mcp"constant`

                The type of the object. Always `mcp`.

                - `MCP("mcp")`

              - `Optional<List<String>> allowedTools`

                The MCP tools the agent may call. All server tools are allowed when omitted.

                `minItems: 0`, `maxItems: 16384`

              - `Optional<ConnectionOrigin> connectionOrigin`

                Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

                - `SERVICE("service")`

                  Uses the Managed Agents service network.

                - `ENVIRONMENT("environment")`

                  Uses the session's execution environment.

              - `Optional<String> credentialId`

                The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

                `minLength: 0`, `maxLength: 1048576`

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

                `minItems: 0`, `maxItems: 16384`

              - `Optional<ContextSize> contextSize`

                The amount of search context made available to the model. Defaults to `medium`.

                - `LOW("low")`

                - `MEDIUM("medium")`

                - `HIGH("high")`

              - `Optional<Location> location`

                Approximate location used to localize search results.

                - `Optional<String> city`

                  The city name.

                  `minLength: 0`, `maxLength: 1048576`

                - `Optional<String> country`

                  The two-letter ISO country code, such as `US`.

                  `minLength: 0`, `maxLength: 1048576`

                - `Optional<String> region`

                  The region or state name.

                  `minLength: 0`, `maxLength: 1048576`

                - `Optional<String> timezone`

                  The IANA timezone, such as `America/Los_Angeles`.

                  `minLength: 0`, `maxLength: 1048576`

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

            - `JsonValue;`

              - `JsonValue; type "automations"constant`

                The type of the object. Always `automations`.

                - `AUTOMATIONS("automations")`

        - `Optional<String> agentId`

          A saved agent ID. Provide exactly one of agent and agent_id.

          `minLength: 0`, `maxLength: 64`

        - `Optional<Metadata> metadata`

          Metadata attached to each new session.

        - `Optional<List<String>> vaultIds`

          The IDs of vaults made available to each new session.

          `minItems: 0`, `maxItems: 16384`

      - `ExistingSession`

        - `String instructions`

          Instructions delivered as an automation notification.

          `minLength: 0`, `maxLength: 1048576`

        - `String sessionId`

          The session receiving each invocation.

          `minLength: 0`, `maxLength: 1048576`

        - `JsonValue; type "existing_session"constant`

          The type of the object. Always `existing_session`.

          - `EXISTING_SESSION("existing_session")`

    - `String timezone`

      The IANA timezone used to interpret the cron expression.

      `minLength: 1`, `maxLength: 128`

    - `JsonValue; type "periodic"constant`

      The type of the object. Always `periodic`.

      - `PERIODIC("periodic")`

    - `Optional<Metadata> metadata`

  - `Once`

    - `String name`

      A human-readable name for the automation.

      `minLength: 1`, `maxLength: 256`

    - `long runAt`

      A future Unix timestamp in seconds.

      `format: int64`

    - `AutomationTargetParam target`

      The session an automation invocation targets.

    - `JsonValue; type "once"constant`

      The type of the object. Always `once`.

      - `ONCE("once")`

    - `Optional<Metadata> metadata`

### Automation Target

- `class AutomationTarget: A class that can be one of several variants.union`

  Saved target configuration, excluding confidential request-only values.

  - `NewSession`

    - `Optional<AutomationAgentConfig> agent`

      The inline agent configuration, or null when agent_id is configured.

      - `Optional<String> instructions`

        Custom instructions, or null when absent.

        `minLength: 0`

      - `String model`

        The requested model name.

        `minLength: 0`

      - `MultiAgentConfig multiAgent`

        The configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled. Defaults to false.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

      - `AgentReasoning reasoning`

        The configured reasoning policy.

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

        The configured service-tier policy.

        - `AUTO("auto")`

        - `DEFAULT("default")`

        - `FLEX("flex")`

        - `PRIORITY("priority")`

        - `FAST("fast")`

        - `ULTRAFAST("ultrafast")`

      - `AgentText text`

        The configured output format and verbosity.

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

        Configured tools, excluding confidential credentials.

        `minItems: 0`, `maxItems: 2000`

        - `Function`

          - `boolean deferLoading`

            Whether the function is deferred and discovered through tool search.

          - `String description`

            A description of what the function does.

            `minLength: 0`

          - `String name`

            The name of the function.

            `minLength: 0`

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

          - `Optional<Boolean> async`

            Whether the agent continues without waiting for the function result.

        - `ProgrammaticToolCalling`

          - `boolean enabled`

            Whether tools can be called from model-generated code.

          - `JsonValue; type "programmatic_tool_calling"constant`

            The type of the object. Always `programmatic_tool_calling`.

            - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

        - `Mcp`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call.

            `minItems: 0`, `maxItems: 2000`

          - `ConnectionOrigin connectionOrigin`

            Where outbound MCP HTTP connections originate.

            - `SERVICE("service")`

            - `ENVIRONMENT("environment")`

          - `Optional<String> credentialId`

            The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`

          - `RequestMetadata requestMetadata`

            Metadata included with requests to this MCP server.

          - `boolean required`

            Whether this MCP server must initialize before the first turn.

          - `String serverLabel`

            A label used to identify the MCP server in tool calls.

            `minLength: 0`

          - `McpTransport transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

                `minLength: 0`

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

            - `Stdio`

              - `List<String> args`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 2000`

              - `String command`

                The command used to start the MCP server.

                `minLength: 0`

              - `String cwd`

                The working directory used to start the MCP server.

                `minLength: 0`

              - `List<String> envVars`

                Environment variable names inherited from the execution environment.

                `minItems: 0`, `maxItems: 2000`

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

        - `WebSearch`

          - `Optional<List<String>> allowedDomains`

            Allowed search domains, or `null` when the search is unrestricted.

            `minItems: 0`, `maxItems: 2000`

          - `ContextSize contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results, if provided.

            - `Optional<String> city`

              The city name.

              `minLength: 0`

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`

            - `Optional<String> region`

              The region or state name.

              `minLength: 0`

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`

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

        - `JsonValue;`

          - `JsonValue; type "automations"constant`

            The type of the object. Always `automations`.

            - `AUTOMATIONS("automations")`

      - `Optional<Compaction> compaction`

        The effective context compaction settings.

        - `boolean async`

          Whether context is compacted in the background. Defaults to true.

      - `Optional<Experimental> experimental`

        The effective experimental settings for the agent.

        - `boolean timeAwareness`

          Whether the model receives periodic current-time reminders.

    - `Optional<String> agentId`

      The saved agent reference, or null when an inline agent is configured.

      `minLength: 0`

    - `AutomationEnvironment environment`

      Configuration or references used to select the execution environment.

      - `JsonValue;`

        - `JsonValue; type "none"constant`

          The type of the object. Always `none`.

          - `NONE("none")`

      - `OpenAIHosted`

        - `Optional<List<String>> capabilityDirectories`

          Directory overrides, or null to inherit the template or creation default.

          `minItems: 0`, `maxItems: 2000`

        - `Optional<ContainerSize> containerSize`

          The configured container size, or null to use the creation default.

          - `SMALL("small")`

          - `MEDIUM("medium")`

          - `LARGE("large")`

        - `Optional<Desktop> desktop`

          Desktop overrides, or null to inherit the template or creation default.

          - `boolean enabled`

            Whether the environment provisions a desktop and browser proxy.

        - `Optional<String> environmentId`

          An existing environment reference, or null when provisioning a new environment.

          `minLength: 0`

        - `Optional<String> environmentTemplateId`

          A template reference, or null when no template is selected.

          `minLength: 0`

        - `Optional<List<File>> files`

          File overrides, excluding contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `class FileId:`

            A project-scoped Files API reference resolved separately for each session.

            - `String fileId`

              The ID of the uploaded file.

              `minLength: 0`

            - `String path`

              The file's absolute path inside the environment.

              `minLength: 0`

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `class Inline:`

            Metadata for confidential inline file contents.

            - `String path`

              The file's absolute path inside the environment.

              `minLength: 0`

            - `long sizeBytes`

              The decoded size of the inline file in bytes.

              `format: int64`, `minimum: 0`

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Optional<Network> network`

          Network overrides, or null to inherit the template or creation default.

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

            `minItems: 0`, `maxItems: 2000`

        - `Optional<Packages> packages`

          Package overrides, or null to inherit the template or creation default.

          - `List<String> npm`

            npm packages installed globally in the environment.

            `minItems: 0`, `maxItems: 16384`

          - `List<String> python`

            Python packages installed in the environment.

            `minItems: 0`, `maxItems: 16384`

          - `List<String> system`

            System packages installed in the environment.

            `minItems: 0`, `maxItems: 16384`

        - `Optional<List<HostedPlugin>> plugins`

          Plugin overrides, excluding archive contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `String description`

            The installed plugin description.

            `minLength: 0`

          - `String name`

            The installed plugin name.

            `minLength: 0`

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `Optional<List<Skill>> skills`

          Skill overrides, excluding archive contents, or null to inherit.

          `minItems: 0`, `maxItems: 2000`

          - `class SkillReference:`

            A skill resolved afresh from the Skills API whenever a session starts.

            - `String skillId`

              The referenced skill ID.

              `minLength: 0`

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `Optional<String> version`

              The requested version selector, including `latest`.

              `minLength: 0`

          - `class Inline:`

            Safe metadata for an inline skill archive.

            - `String description`

              The skill description declared in `SKILL.md`.

              `minLength: 0`

            - `String name`

              The skill name declared in `SKILL.md`.

              `minLength: 0`

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `JsonValue; type "openai_hosted"constant`

          The type of the object. Always `openai_hosted`.

          - `OPENAI_HOSTED("openai_hosted")`

      - `SelfHosted`

        - `List<String> capabilityDirectories`

          Directories that expose capabilities to the agent.

          `minItems: 0`, `maxItems: 2000`

        - `Optional<String> environmentId`

          An existing registration, or null to create a session-owned environment.

          `minLength: 0`

        - `JsonValue; type "self_hosted"constant`

          The type of the object. Always `self_hosted`.

          - `SELF_HOSTED("self_hosted")`

        - `String workspaceDirectory`

          The absolute project directory in the environment.

          `minLength: 0`

    - `List<Input> input`

      Initial input delivered to each new session.

      `minItems: 0`, `maxItems: 2000`

      - `List<InputContent> content`

        The content of the message.

        `minItems: 0`, `maxItems: 2000`

        - `InputText`

          - `String text`

            The text supplied to the agent.

            `minLength: 0`

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

      - `JsonValue; role "user"constant`

        The role of the message author. Always `user`.

        - `USER("user")`

      - `JsonValue; type "message"constant`

        The type of the input item. Always `message`.

        - `MESSAGE("message")`

    - `Metadata metadata`

      Metadata attached to each new session.

    - `JsonValue; type "new_session"constant`

      The type of the object. Always `new_session`.

      - `NEW_SESSION("new_session")`

    - `List<String> vaultIds`

      Vaults made available to each new session.

      `minItems: 0`, `maxItems: 2000`

  - `ExistingSession`

    - `String instructions`

      Saved instructions delivered as an automation notification.

      `minLength: 0`

    - `String sessionId`

      The session receiving each invocation.

      `minLength: 0`

    - `JsonValue; type "existing_session"constant`

      The type of the object. Always `existing_session`.

      - `EXISTING_SESSION("existing_session")`

### Automation Target Param

- `class AutomationTargetParam: A class that can be one of several variants.union`

  The session an automation invocation targets.

  - `NewSession`

    - `EnvironmentParam environment`

      The execution environment for each new session.

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

          `minItems: 0`, `maxItems: 16384`

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

        - `Optional<String> environmentId`

          An existing prewarmed environment. Cannot be combined with a template or inline configuration.

          `minLength: 9`, `maxLength: 256`

        - `Optional<String> environmentTemplateId`

          A reusable hosted template applied before inline session configuration. Omitted fields inherit the template; network overrides cannot broaden its policy.

          `minLength: 0`, `maxLength: 64`

        - `Optional<List<HostedEnvironmentFileParam>> files`

          Files available before the agent starts. Defaults to an empty list.

          `minItems: 0`, `maxItems: 50`

          - `FileId`

            - `String fileId`

              The ID of the uploaded file.

              `minLength: 1`, `maxLength: 256`

            - `String path`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `JsonValue; type "file_id"constant`

              The type of the object. Always `file_id`.

              - `FILE_ID("file_id")`

          - `Inline`

            - `String data`

              The standard-base64-encoded file contents.

              `minLength: 0`, `maxLength: 6990508`

            - `String path`

              The absolute destination path inside `/workspace`.

              `minLength: 1`, `maxLength: 4096`

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

        - `Optional<Network> network`

          Network access policy for the environment. If omitted, the API version determines whether network access is enabled or disabled.

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

            `minItems: 0`, `maxItems: 16384`

          - `Optional<List<String>> blockedDomains`

            Domains blocked for both executor and browser when access is restricted. A nonempty list requires `access: restricted` and cannot be combined with nonempty `allowed_domains`. Wildcard domains are not supported.

            `minItems: 0`, `maxItems: 100`

        - `Optional<Packages> packages`

          Packages to install in the environment. Defaults to empty package lists.

          - `Optional<List<String>> npm`

            npm packages to install globally. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `Optional<List<String>> python`

            Python packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

          - `Optional<List<String>> system`

            System packages to install. Defaults to an empty list.

            `minItems: 0`, `maxItems: 16384`

        - `Optional<List<HostedPluginParam>> plugins`

          Plugins provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 32`

          - `String description`

            The plugin description declared in `.codex-plugin/plugin.json`.

            `minLength: 0`, `maxLength: 1048576`

          - `String name`

            The plugin name declared in `.codex-plugin/plugin.json`.

            `minLength: 1`, `maxLength: 64`

          - `InlineCapabilitySourceParam source`

            Provides ZIP bytes encoded with standard base64.

            - `String data`

              Standard-base64 encoded ZIP archive bytes.

              `minLength: 1`, `maxLength: 70254592`

            - `JsonValue; mediaType "application/zip"constant`

              The archive media type, always `application/zip`.

              - `APPLICATION_ZIP("application/zip")`

            - `JsonValue; type "base64"constant`

              The type of the object. Always `base64`.

              - `BASE64("base64")`

          - `JsonValue; type "inline"constant`

            The type of the object. Always `inline`.

            - `INLINE("inline")`

        - `Optional<List<SetupCommandParam>> setupCommands`

          Ordered, confidential setup commands. Command bodies are never returned.

          `minItems: 0`, `maxItems: 16`

          - `String command`

            The shell command to execute.

            `minLength: 0`, `maxLength: 65536`

          - `Optional<String> cwd`

            The absolute working directory. Defaults to `/workspace`.

            `minLength: 0`, `maxLength: 4096`

        - `Optional<List<HostedSkillParam>> skills`

          Skills referenced by ID or provided as inline ZIP archives. Defaults to an empty list.

          `minItems: 0`, `maxItems: 200`

          - `SkillReference`

            - `String skillId`

              The ID of the skill created through `/v1/skills`.

              `minLength: 1`, `maxLength: 64`

            - `JsonValue; type "skill_reference"constant`

              The type of the object. Always `skill_reference`.

              - `SKILL_REFERENCE("skill_reference")`

            - `Optional<String> version`

              The skill version, a positive integer or `latest`; omission selects the default.

              `minLength: 0`, `maxLength: 1048576`

          - `Inline`

            - `String description`

              The skill description declared in `SKILL.md`.

              `minLength: 0`, `maxLength: 1048576`

            - `String name`

              The skill name declared in `SKILL.md`.

              `minLength: 1`, `maxLength: 64`

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

          `minLength: 0`, `maxLength: 1048576`

        - `Optional<List<String>> capabilityDirectories`

          Directories that contain capabilities exposed to the agent. Defaults to an empty list.

          `minItems: 0`, `maxItems: 16384`

    - `List<AgentSessionInputMessageParam> input`

      Initial user messages submitted with each new session.

      `minItems: 0`, `maxItems: 16384`

      - `List<InputContentParam> content`

        The content of the message.

        `minItems: 0`, `maxItems: 16384`

        - `InputText`

          - `String text`

            The text sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image sent to the model.

            `minLength: 0`, `maxLength: 1048576`

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

      - `JsonValue; role "user"constant`

        The role of the message author. Always `user`.

        - `USER("user")`

      - `Optional<Type> type`

        The type of the input item. Always `message`.

        - `MESSAGE("message")`

    - `JsonValue; type "new_session"constant`

      The type of the object. Always `new_session`.

      - `NEW_SESSION("new_session")`

    - `Optional<Agent> agent`

      Inline agent configuration. Provide exactly one of agent and agent_id.

      - `Optional<Compaction> compaction`

        Context compaction settings. Omit to keep the current settings. A supplied object replaces the settings; null or an empty object enables background compaction.

        - `Optional<Boolean> async`

          Whether to compact context in the background. Omission or null defaults to true. Set to false to use blocking compaction. Background compaction may increase token usage.

      - `Optional<Experimental> experimental`

        Experimental settings to merge by key. Omitted settings keep their current values.

        - `Optional<Boolean> timeAwareness`

          Whether to give the model periodic current-time reminders. Omit to keep the current setting.

      - `Optional<String> instructions`

        Additional instructions appended to the agent's default base instructions. Omit to leave unchanged.

        `minLength: 0`, `maxLength: 1048576`

      - `Optional<String> model`

        The model to use for the agent. The requested model name is preserved.

        `minLength: 0`, `maxLength: 1048576`

      - `Optional<MultiAgentConfigParam> multiAgent`

        Configuration for creating and coordinating subagents.

        - `boolean enabled`

          Whether subagent tools are enabled.

        - `Optional<Long> maxConcurrentSubagents`

          Maximum number of subagents that may run concurrently. Defaults to 6.

          `format: int64`, `minimum: 1`, `maximum: 4294967295`

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

        Tools available to the agent. Omit to inherit, or pass null to clear them. The resolved tool list must fit within 3 MiB (3,145,728 bytes) of compact UTF-8 JSON.

        `minItems: 0`, `maxItems: 16384`

        - `Function`

          - `String description`

            A description of what the function does.

            `minLength: 0`, `maxLength: 1048576`

          - `String name`

            The name of the function.

            `minLength: 0`, `maxLength: 1048576`

          - `Parameters parameters`

            A JSON Schema object describing the function's arguments.

          - `JsonValue; type "function"constant`

            The type of the object. Always `function`.

            - `FUNCTION("function")`

          - `Optional<Boolean> async`

            Whether the agent continues without waiting for the function result. Defaults to `false`.

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

            `minLength: 0`, `maxLength: 1048576`

          - `McpTransportParam transport`

            The transport used to connect to the MCP server.

            - `Http`

              - `String serverUrl`

                The URL of the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `JsonValue; type "http"constant`

                The type of the object. Always `http`.

                - `HTTP("http")`

              - `Optional<String> authorization`

                The authorization value sent to the MCP server, if any.

                `minLength: 0`, `maxLength: 1048576`

              - `Optional<Headers> headers`

                Additional HTTP headers sent to the MCP server.

            - `Stdio`

              - `String command`

                The command used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `String cwd`

                The working directory used to start the MCP server.

                `minLength: 0`, `maxLength: 1048576`

              - `JsonValue; type "stdio"constant`

                The type of the object. Always `stdio`.

                - `STDIO("stdio")`

              - `Optional<List<String>> args`

                Arguments passed to the MCP server command.

                `minItems: 0`, `maxItems: 16384`

              - `Optional<Env> env`

                Environment variables set for the MCP server process.

              - `Optional<List<String>> envVars`

                Environment variable names to inherit from the selected execution environment.

                `minItems: 0`, `maxItems: 16384`

          - `JsonValue; type "mcp"constant`

            The type of the object. Always `mcp`.

            - `MCP("mcp")`

          - `Optional<List<String>> allowedTools`

            The MCP tools the agent may call. All server tools are allowed when omitted.

            `minItems: 0`, `maxItems: 16384`

          - `Optional<ConnectionOrigin> connectionOrigin`

            Selects where outbound MCP HTTP connections originate. Omitted or `service` uses the Managed Agents service network; `environment` uses the session's selected environment.

            - `SERVICE("service")`

              Uses the Managed Agents service network.

            - `ENVIRONMENT("environment")`

              Uses the session's execution environment.

          - `Optional<String> credentialId`

            The attached vault credential used to authenticate this MCP server. Optional when exactly one attached credential matches the server URL.

            `minLength: 0`, `maxLength: 1048576`

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

            `minItems: 0`, `maxItems: 16384`

          - `Optional<ContextSize> contextSize`

            The amount of search context made available to the model. Defaults to `medium`.

            - `LOW("low")`

            - `MEDIUM("medium")`

            - `HIGH("high")`

          - `Optional<Location> location`

            Approximate location used to localize search results.

            - `Optional<String> city`

              The city name.

              `minLength: 0`, `maxLength: 1048576`

            - `Optional<String> country`

              The two-letter ISO country code, such as `US`.

              `minLength: 0`, `maxLength: 1048576`

            - `Optional<String> region`

              The region or state name.

              `minLength: 0`, `maxLength: 1048576`

            - `Optional<String> timezone`

              The IANA timezone, such as `America/Los_Angeles`.

              `minLength: 0`, `maxLength: 1048576`

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

        - `JsonValue;`

          - `JsonValue; type "automations"constant`

            The type of the object. Always `automations`.

            - `AUTOMATIONS("automations")`

    - `Optional<String> agentId`

      A saved agent ID. Provide exactly one of agent and agent_id.

      `minLength: 0`, `maxLength: 64`

    - `Optional<Metadata> metadata`

      Metadata attached to each new session.

    - `Optional<List<String>> vaultIds`

      The IDs of vaults made available to each new session.

      `minItems: 0`, `maxItems: 16384`

  - `ExistingSession`

    - `String instructions`

      Instructions delivered as an automation notification.

      `minLength: 0`, `maxLength: 1048576`

    - `String sessionId`

      The session receiving each invocation.

      `minLength: 0`, `maxLength: 1048576`

    - `JsonValue; type "existing_session"constant`

      The type of the object. Always `existing_session`.

      - `EXISTING_SESSION("existing_session")`

### One Time Automation

- `class OneTimeAutomation:`

  Fields shared by periodic and one-time automations.

  - `String id`

    The automation ID.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `AutomationCreatedBy createdBy`

    Service-recorded provenance; callers cannot supply this field.

    - `JsonValue;`

      - `JsonValue; type "developer"constant`

        The type of the object. Always `developer`.

        - `DEVELOPER("developer")`

    - `Agent`

      - `String sessionId`

        The creator session, which is also the automation's target.

        `minLength: 0`

      - `String toolCallId`

        The tool call that created the automation.

        `minLength: 0`

      - `JsonValue; type "agent"constant`

        The type of the object. Always `agent`.

        - `AGENT("agent")`

  - `Metadata metadata`

    Custom string key-value pairs attached to the automation.

  - `String name`

    The automation's display name.

    `minLength: 0`

  - `JsonValue; object_ "agent.automation"constant`

    Always `agent.automation`.

    - `AGENT_AUTOMATION("agent.automation")`

  - `long runAt`

    The Unix timestamp, in seconds, of the scheduled occurrence.

    `format: int64`

  - `Status status`

    Completion means the schedule has finished, not the agent's work.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

    - `COMPLETED("completed")`

  - `AutomationTarget target`

    The session configuration or existing session receiving invocations.

    - `NewSession`

      - `Optional<AutomationAgentConfig> agent`

        The inline agent configuration, or null when agent_id is configured.

        - `Optional<String> instructions`

          Custom instructions, or null when absent.

          `minLength: 0`

        - `String model`

          The requested model name.

          `minLength: 0`

        - `MultiAgentConfig multiAgent`

          The configuration for creating and coordinating subagents.

          - `boolean enabled`

            Whether subagent tools are enabled. Defaults to false.

          - `Optional<Long> maxConcurrentSubagents`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `AgentReasoning reasoning`

          The configured reasoning policy.

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

          The configured service-tier policy.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `FAST("fast")`

          - `ULTRAFAST("ultrafast")`

        - `AgentText text`

          The configured output format and verbosity.

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

          Configured tools, excluding confidential credentials.

          `minItems: 0`, `maxItems: 2000`

          - `Function`

            - `boolean deferLoading`

              Whether the function is deferred and discovered through tool search.

            - `String description`

              A description of what the function does.

              `minLength: 0`

            - `String name`

              The name of the function.

              `minLength: 0`

            - `Parameters parameters`

              A JSON Schema object describing the function's arguments.

            - `JsonValue; type "function"constant`

              The type of the object. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> async`

              Whether the agent continues without waiting for the function result.

          - `ProgrammaticToolCalling`

            - `boolean enabled`

              Whether tools can be called from model-generated code.

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the object. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `Mcp`

            - `Optional<List<String>> allowedTools`

              The MCP tools the agent may call.

              `minItems: 0`, `maxItems: 2000`

            - `ConnectionOrigin connectionOrigin`

              Where outbound MCP HTTP connections originate.

              - `SERVICE("service")`

              - `ENVIRONMENT("environment")`

            - `Optional<String> credentialId`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`

            - `RequestMetadata requestMetadata`

              Metadata included with requests to this MCP server.

            - `boolean required`

              Whether this MCP server must initialize before the first turn.

            - `String serverLabel`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`

            - `McpTransport transport`

              The transport used to connect to the MCP server.

              - `Http`

                - `String serverUrl`

                  The URL of the MCP server.

                  `minLength: 0`

                - `JsonValue; type "http"constant`

                  The type of the object. Always `http`.

                  - `HTTP("http")`

              - `Stdio`

                - `List<String> args`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 2000`

                - `String command`

                  The command used to start the MCP server.

                  `minLength: 0`

                - `String cwd`

                  The working directory used to start the MCP server.

                  `minLength: 0`

                - `List<String> envVars`

                  Environment variable names inherited from the execution environment.

                  `minItems: 0`, `maxItems: 2000`

                - `JsonValue; type "stdio"constant`

                  The type of the object. Always `stdio`.

                  - `STDIO("stdio")`

            - `JsonValue; type "mcp"constant`

              The type of the object. Always `mcp`.

              - `MCP("mcp")`

          - `WebSearch`

            - `Optional<List<String>> allowedDomains`

              Allowed search domains, or `null` when the search is unrestricted.

              `minItems: 0`, `maxItems: 2000`

            - `ContextSize contextSize`

              The amount of search context made available to the model. Defaults to `medium`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<Location> location`

              Approximate location used to localize search results, if provided.

              - `Optional<String> city`

                The city name.

                `minLength: 0`

              - `Optional<String> country`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`

              - `Optional<String> region`

                The region or state name.

                `minLength: 0`

              - `Optional<String> timezone`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`

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

          - `JsonValue;`

            - `JsonValue; type "automations"constant`

              The type of the object. Always `automations`.

              - `AUTOMATIONS("automations")`

        - `Optional<Compaction> compaction`

          The effective context compaction settings.

          - `boolean async`

            Whether context is compacted in the background. Defaults to true.

        - `Optional<Experimental> experimental`

          The effective experimental settings for the agent.

          - `boolean timeAwareness`

            Whether the model receives periodic current-time reminders.

      - `Optional<String> agentId`

        The saved agent reference, or null when an inline agent is configured.

        `minLength: 0`

      - `AutomationEnvironment environment`

        Configuration or references used to select the execution environment.

        - `JsonValue;`

          - `JsonValue; type "none"constant`

            The type of the object. Always `none`.

            - `NONE("none")`

        - `OpenAIHosted`

          - `Optional<List<String>> capabilityDirectories`

            Directory overrides, or null to inherit the template or creation default.

            `minItems: 0`, `maxItems: 2000`

          - `Optional<ContainerSize> containerSize`

            The configured container size, or null to use the creation default.

            - `SMALL("small")`

            - `MEDIUM("medium")`

            - `LARGE("large")`

          - `Optional<Desktop> desktop`

            Desktop overrides, or null to inherit the template or creation default.

            - `boolean enabled`

              Whether the environment provisions a desktop and browser proxy.

          - `Optional<String> environmentId`

            An existing environment reference, or null when provisioning a new environment.

            `minLength: 0`

          - `Optional<String> environmentTemplateId`

            A template reference, or null when no template is selected.

            `minLength: 0`

          - `Optional<List<File>> files`

            File overrides, excluding contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `class FileId:`

              A project-scoped Files API reference resolved separately for each session.

              - `String fileId`

                The ID of the uploaded file.

                `minLength: 0`

              - `String path`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `JsonValue; type "file_id"constant`

                The type of the object. Always `file_id`.

                - `FILE_ID("file_id")`

            - `class Inline:`

              Metadata for confidential inline file contents.

              - `String path`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `long sizeBytes`

                The decoded size of the inline file in bytes.

                `format: int64`, `minimum: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `Optional<Network> network`

            Network overrides, or null to inherit the template or creation default.

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

              `minItems: 0`, `maxItems: 2000`

          - `Optional<Packages> packages`

            Package overrides, or null to inherit the template or creation default.

            - `List<String> npm`

              npm packages installed globally in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `List<String> python`

              Python packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `List<String> system`

              System packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

          - `Optional<List<HostedPlugin>> plugins`

            Plugin overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `String description`

              The installed plugin description.

              `minLength: 0`

            - `String name`

              The installed plugin name.

              `minLength: 0`

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

          - `Optional<List<Skill>> skills`

            Skill overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `class SkillReference:`

              A skill resolved afresh from the Skills API whenever a session starts.

              - `String skillId`

                The referenced skill ID.

                `minLength: 0`

              - `JsonValue; type "skill_reference"constant`

                The type of the object. Always `skill_reference`.

                - `SKILL_REFERENCE("skill_reference")`

              - `Optional<String> version`

                The requested version selector, including `latest`.

                `minLength: 0`

            - `class Inline:`

              Safe metadata for an inline skill archive.

              - `String description`

                The skill description declared in `SKILL.md`.

                `minLength: 0`

              - `String name`

                The skill name declared in `SKILL.md`.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `JsonValue; type "openai_hosted"constant`

            The type of the object. Always `openai_hosted`.

            - `OPENAI_HOSTED("openai_hosted")`

        - `SelfHosted`

          - `List<String> capabilityDirectories`

            Directories that expose capabilities to the agent.

            `minItems: 0`, `maxItems: 2000`

          - `Optional<String> environmentId`

            An existing registration, or null to create a session-owned environment.

            `minLength: 0`

          - `JsonValue; type "self_hosted"constant`

            The type of the object. Always `self_hosted`.

            - `SELF_HOSTED("self_hosted")`

          - `String workspaceDirectory`

            The absolute project directory in the environment.

            `minLength: 0`

      - `List<Input> input`

        Initial input delivered to each new session.

        `minItems: 0`, `maxItems: 2000`

        - `List<InputContent> content`

          The content of the message.

          `minItems: 0`, `maxItems: 2000`

          - `InputText`

            - `String text`

              The text supplied to the agent.

              `minLength: 0`

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              `minLength: 0`

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

        - `JsonValue; role "user"constant`

          The role of the message author. Always `user`.

          - `USER("user")`

        - `JsonValue; type "message"constant`

          The type of the input item. Always `message`.

          - `MESSAGE("message")`

      - `Metadata metadata`

        Metadata attached to each new session.

      - `JsonValue; type "new_session"constant`

        The type of the object. Always `new_session`.

        - `NEW_SESSION("new_session")`

      - `List<String> vaultIds`

        Vaults made available to each new session.

        `minItems: 0`, `maxItems: 2000`

    - `ExistingSession`

      - `String instructions`

        Saved instructions delivered as an automation notification.

        `minLength: 0`

      - `String sessionId`

        The session receiving each invocation.

        `minLength: 0`

      - `JsonValue; type "existing_session"constant`

        The type of the object. Always `existing_session`.

        - `EXISTING_SESSION("existing_session")`

  - `JsonValue; type "once"constant`

    The type of the object. Always `once`.

    - `ONCE("once")`

### Periodic Automation

- `class PeriodicAutomation:`

  Fields shared by periodic and one-time automations.

  - `String id`

    The automation ID.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `AutomationCreatedBy createdBy`

    Service-recorded provenance; callers cannot supply this field.

    - `JsonValue;`

      - `JsonValue; type "developer"constant`

        The type of the object. Always `developer`.

        - `DEVELOPER("developer")`

    - `Agent`

      - `String sessionId`

        The creator session, which is also the automation's target.

        `minLength: 0`

      - `String toolCallId`

        The tool call that created the automation.

        `minLength: 0`

      - `JsonValue; type "agent"constant`

        The type of the object. Always `agent`.

        - `AGENT("agent")`

  - `String expression`

    The cron expression determining scheduled occurrences.

    `minLength: 0`

  - `Metadata metadata`

    Custom string key-value pairs attached to the automation.

  - `String name`

    The automation's display name.

    `minLength: 0`

  - `JsonValue; object_ "agent.automation"constant`

    Always `agent.automation`.

    - `AGENT_AUTOMATION("agent.automation")`

  - `Status status`

    Whether scheduled delivery is active or paused.

    - `ACTIVE("active")`

    - `PAUSED("paused")`

  - `AutomationTarget target`

    The session configuration or existing session receiving invocations.

    - `NewSession`

      - `Optional<AutomationAgentConfig> agent`

        The inline agent configuration, or null when agent_id is configured.

        - `Optional<String> instructions`

          Custom instructions, or null when absent.

          `minLength: 0`

        - `String model`

          The requested model name.

          `minLength: 0`

        - `MultiAgentConfig multiAgent`

          The configuration for creating and coordinating subagents.

          - `boolean enabled`

            Whether subagent tools are enabled. Defaults to false.

          - `Optional<Long> maxConcurrentSubagents`

            Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

            `format: int64`, `minimum: 1`, `maximum: 4294967295`

        - `AgentReasoning reasoning`

          The configured reasoning policy.

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

          The configured service-tier policy.

          - `AUTO("auto")`

          - `DEFAULT("default")`

          - `FLEX("flex")`

          - `PRIORITY("priority")`

          - `FAST("fast")`

          - `ULTRAFAST("ultrafast")`

        - `AgentText text`

          The configured output format and verbosity.

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

          Configured tools, excluding confidential credentials.

          `minItems: 0`, `maxItems: 2000`

          - `Function`

            - `boolean deferLoading`

              Whether the function is deferred and discovered through tool search.

            - `String description`

              A description of what the function does.

              `minLength: 0`

            - `String name`

              The name of the function.

              `minLength: 0`

            - `Parameters parameters`

              A JSON Schema object describing the function's arguments.

            - `JsonValue; type "function"constant`

              The type of the object. Always `function`.

              - `FUNCTION("function")`

            - `Optional<Boolean> async`

              Whether the agent continues without waiting for the function result.

          - `ProgrammaticToolCalling`

            - `boolean enabled`

              Whether tools can be called from model-generated code.

            - `JsonValue; type "programmatic_tool_calling"constant`

              The type of the object. Always `programmatic_tool_calling`.

              - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

          - `Mcp`

            - `Optional<List<String>> allowedTools`

              The MCP tools the agent may call.

              `minItems: 0`, `maxItems: 2000`

            - `ConnectionOrigin connectionOrigin`

              Where outbound MCP HTTP connections originate.

              - `SERVICE("service")`

              - `ENVIRONMENT("environment")`

            - `Optional<String> credentialId`

              The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

              `minLength: 0`

            - `RequestMetadata requestMetadata`

              Metadata included with requests to this MCP server.

            - `boolean required`

              Whether this MCP server must initialize before the first turn.

            - `String serverLabel`

              A label used to identify the MCP server in tool calls.

              `minLength: 0`

            - `McpTransport transport`

              The transport used to connect to the MCP server.

              - `Http`

                - `String serverUrl`

                  The URL of the MCP server.

                  `minLength: 0`

                - `JsonValue; type "http"constant`

                  The type of the object. Always `http`.

                  - `HTTP("http")`

              - `Stdio`

                - `List<String> args`

                  Arguments passed to the MCP server command.

                  `minItems: 0`, `maxItems: 2000`

                - `String command`

                  The command used to start the MCP server.

                  `minLength: 0`

                - `String cwd`

                  The working directory used to start the MCP server.

                  `minLength: 0`

                - `List<String> envVars`

                  Environment variable names inherited from the execution environment.

                  `minItems: 0`, `maxItems: 2000`

                - `JsonValue; type "stdio"constant`

                  The type of the object. Always `stdio`.

                  - `STDIO("stdio")`

            - `JsonValue; type "mcp"constant`

              The type of the object. Always `mcp`.

              - `MCP("mcp")`

          - `WebSearch`

            - `Optional<List<String>> allowedDomains`

              Allowed search domains, or `null` when the search is unrestricted.

              `minItems: 0`, `maxItems: 2000`

            - `ContextSize contextSize`

              The amount of search context made available to the model. Defaults to `medium`.

              - `LOW("low")`

              - `MEDIUM("medium")`

              - `HIGH("high")`

            - `Optional<Location> location`

              Approximate location used to localize search results, if provided.

              - `Optional<String> city`

                The city name.

                `minLength: 0`

              - `Optional<String> country`

                The two-letter ISO country code, such as `US`.

                `minLength: 0`

              - `Optional<String> region`

                The region or state name.

                `minLength: 0`

              - `Optional<String> timezone`

                The IANA timezone, such as `America/Los_Angeles`.

                `minLength: 0`

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

          - `JsonValue;`

            - `JsonValue; type "automations"constant`

              The type of the object. Always `automations`.

              - `AUTOMATIONS("automations")`

        - `Optional<Compaction> compaction`

          The effective context compaction settings.

          - `boolean async`

            Whether context is compacted in the background. Defaults to true.

        - `Optional<Experimental> experimental`

          The effective experimental settings for the agent.

          - `boolean timeAwareness`

            Whether the model receives periodic current-time reminders.

      - `Optional<String> agentId`

        The saved agent reference, or null when an inline agent is configured.

        `minLength: 0`

      - `AutomationEnvironment environment`

        Configuration or references used to select the execution environment.

        - `JsonValue;`

          - `JsonValue; type "none"constant`

            The type of the object. Always `none`.

            - `NONE("none")`

        - `OpenAIHosted`

          - `Optional<List<String>> capabilityDirectories`

            Directory overrides, or null to inherit the template or creation default.

            `minItems: 0`, `maxItems: 2000`

          - `Optional<ContainerSize> containerSize`

            The configured container size, or null to use the creation default.

            - `SMALL("small")`

            - `MEDIUM("medium")`

            - `LARGE("large")`

          - `Optional<Desktop> desktop`

            Desktop overrides, or null to inherit the template or creation default.

            - `boolean enabled`

              Whether the environment provisions a desktop and browser proxy.

          - `Optional<String> environmentId`

            An existing environment reference, or null when provisioning a new environment.

            `minLength: 0`

          - `Optional<String> environmentTemplateId`

            A template reference, or null when no template is selected.

            `minLength: 0`

          - `Optional<List<File>> files`

            File overrides, excluding contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `class FileId:`

              A project-scoped Files API reference resolved separately for each session.

              - `String fileId`

                The ID of the uploaded file.

                `minLength: 0`

              - `String path`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `JsonValue; type "file_id"constant`

                The type of the object. Always `file_id`.

                - `FILE_ID("file_id")`

            - `class Inline:`

              Metadata for confidential inline file contents.

              - `String path`

                The file's absolute path inside the environment.

                `minLength: 0`

              - `long sizeBytes`

                The decoded size of the inline file in bytes.

                `format: int64`, `minimum: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `Optional<Network> network`

            Network overrides, or null to inherit the template or creation default.

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

              `minItems: 0`, `maxItems: 2000`

          - `Optional<Packages> packages`

            Package overrides, or null to inherit the template or creation default.

            - `List<String> npm`

              npm packages installed globally in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `List<String> python`

              Python packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

            - `List<String> system`

              System packages installed in the environment.

              `minItems: 0`, `maxItems: 16384`

          - `Optional<List<HostedPlugin>> plugins`

            Plugin overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `String description`

              The installed plugin description.

              `minLength: 0`

            - `String name`

              The installed plugin name.

              `minLength: 0`

            - `JsonValue; type "inline"constant`

              The type of the object. Always `inline`.

              - `INLINE("inline")`

          - `Optional<List<Skill>> skills`

            Skill overrides, excluding archive contents, or null to inherit.

            `minItems: 0`, `maxItems: 2000`

            - `class SkillReference:`

              A skill resolved afresh from the Skills API whenever a session starts.

              - `String skillId`

                The referenced skill ID.

                `minLength: 0`

              - `JsonValue; type "skill_reference"constant`

                The type of the object. Always `skill_reference`.

                - `SKILL_REFERENCE("skill_reference")`

              - `Optional<String> version`

                The requested version selector, including `latest`.

                `minLength: 0`

            - `class Inline:`

              Safe metadata for an inline skill archive.

              - `String description`

                The skill description declared in `SKILL.md`.

                `minLength: 0`

              - `String name`

                The skill name declared in `SKILL.md`.

                `minLength: 0`

              - `JsonValue; type "inline"constant`

                The type of the object. Always `inline`.

                - `INLINE("inline")`

          - `JsonValue; type "openai_hosted"constant`

            The type of the object. Always `openai_hosted`.

            - `OPENAI_HOSTED("openai_hosted")`

        - `SelfHosted`

          - `List<String> capabilityDirectories`

            Directories that expose capabilities to the agent.

            `minItems: 0`, `maxItems: 2000`

          - `Optional<String> environmentId`

            An existing registration, or null to create a session-owned environment.

            `minLength: 0`

          - `JsonValue; type "self_hosted"constant`

            The type of the object. Always `self_hosted`.

            - `SELF_HOSTED("self_hosted")`

          - `String workspaceDirectory`

            The absolute project directory in the environment.

            `minLength: 0`

      - `List<Input> input`

        Initial input delivered to each new session.

        `minItems: 0`, `maxItems: 2000`

        - `List<InputContent> content`

          The content of the message.

          `minItems: 0`, `maxItems: 2000`

          - `InputText`

            - `String text`

              The text supplied to the agent.

              `minLength: 0`

            - `JsonValue; type "input_text"constant`

              The type of the object. Always `input_text`.

              - `INPUT_TEXT("input_text")`

          - `InputImage`

            - `String imageUrl`

              The URL of the image supplied to the agent, which may be a base64-encoded data URL.

              `minLength: 0`

            - `JsonValue; type "input_image"constant`

              The type of the object. Always `input_image`.

              - `INPUT_IMAGE("input_image")`

        - `JsonValue; role "user"constant`

          The role of the message author. Always `user`.

          - `USER("user")`

        - `JsonValue; type "message"constant`

          The type of the input item. Always `message`.

          - `MESSAGE("message")`

      - `Metadata metadata`

        Metadata attached to each new session.

      - `JsonValue; type "new_session"constant`

        The type of the object. Always `new_session`.

        - `NEW_SESSION("new_session")`

      - `List<String> vaultIds`

        Vaults made available to each new session.

        `minItems: 0`, `maxItems: 2000`

    - `ExistingSession`

      - `String instructions`

        Saved instructions delivered as an automation notification.

        `minLength: 0`

      - `String sessionId`

        The session receiving each invocation.

        `minLength: 0`

      - `JsonValue; type "existing_session"constant`

        The type of the object. Always `existing_session`.

        - `EXISTING_SESSION("existing_session")`

  - `String timezone`

    The timezone used to interpret the expression.

    `minLength: 0`

  - `JsonValue; type "periodic"constant`

    The type of the object. Always `periodic`.

    - `PERIODIC("periodic")`

# Invocations

## Invoke an automation

`AutomationInvocation beta().agents().automations().invocations().create(InvocationCreateParamsparams = InvocationCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/automations/{automation_id}/invocations`

Queues a manual delivery without changing the saved schedule.

### Parameters

- `InvocationCreateParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class AutomationInvocation:`

  One attempted delivery by an automation.

  - `String id`

    The invocation ID.

    `minLength: 0`

  - `String automationId`

    The automation that owns the invocation.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Optional<Error> error`

    The permanent delivery failure, or null when no failure occurred.

    - `String code`

      A machine-readable error code.

      `minLength: 0`

    - `String message`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `JsonValue; object_ "agent.automation.invocation"constant`

    Always `agent.automation.invocation`.

    - `AGENT_AUTOMATION_INVOCATION("agent.automation.invocation")`

  - `Optional<Long> scheduledAt`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `Optional<String> sessionId`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `Optional<SkipReason> skipReason`

    Why an occurrence was skipped, or null when it was not skipped.

    - `PENDING_DELIVERY("pending_delivery")`

  - `AutomationInvocationSource source`

    Whether the invocation was manual or scheduled.

    - `JsonValue;`

      - `JsonValue; type "manual"constant`

        The type of the object. Always `manual`.

        - `MANUAL("manual")`

    - `class AutomationInvocationSourceAutomation:`

      - `Automation automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

            - `JsonValue;`

              - `JsonValue; type "developer"constant`

                The type of the object. Always `developer`.

                - `DEVELOPER("developer")`

            - `Agent`

              - `String sessionId`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `String toolCallId`

                The tool call that created the automation.

                `minLength: 0`

              - `JsonValue; type "agent"constant`

                The type of the object. Always `agent`.

                - `AGENT("agent")`

          - `String expression`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `Status status`

            Whether scheduled delivery is active or paused.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

            - `NewSession`

              - `Optional<AutomationAgentConfig> agent`

                The inline agent configuration, or null when agent_id is configured.

                - `Optional<String> instructions`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `String model`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgentConfig multiAgent`

                  The configuration for creating and coordinating subagents.

                  - `boolean enabled`

                    Whether subagent tools are enabled. Defaults to false.

                  - `Optional<Long> maxConcurrentSubagents`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `AgentReasoning reasoning`

                  The configured reasoning policy.

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

                  The configured service-tier policy.

                  - `AUTO("auto")`

                  - `DEFAULT("default")`

                  - `FLEX("flex")`

                  - `PRIORITY("priority")`

                  - `FAST("fast")`

                  - `ULTRAFAST("ultrafast")`

                - `AgentText text`

                  The configured output format and verbosity.

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

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `Function`

                    - `boolean deferLoading`

                      Whether the function is deferred and discovered through tool search.

                    - `String description`

                      A description of what the function does.

                      `minLength: 0`

                    - `String name`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters parameters`

                      A JSON Schema object describing the function's arguments.

                    - `JsonValue; type "function"constant`

                      The type of the object. Always `function`.

                      - `FUNCTION("function")`

                    - `Optional<Boolean> async`

                      Whether the agent continues without waiting for the function result.

                  - `ProgrammaticToolCalling`

                    - `boolean enabled`

                      Whether tools can be called from model-generated code.

                    - `JsonValue; type "programmatic_tool_calling"constant`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

                  - `Mcp`

                    - `Optional<List<String>> allowedTools`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin connectionOrigin`

                      Where outbound MCP HTTP connections originate.

                      - `SERVICE("service")`

                      - `ENVIRONMENT("environment")`

                    - `Optional<String> credentialId`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata requestMetadata`

                      Metadata included with requests to this MCP server.

                    - `boolean required`

                      Whether this MCP server must initialize before the first turn.

                    - `String serverLabel`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `McpTransport transport`

                      The transport used to connect to the MCP server.

                      - `Http`

                        - `String serverUrl`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `JsonValue; type "http"constant`

                          The type of the object. Always `http`.

                          - `HTTP("http")`

                      - `Stdio`

                        - `List<String> args`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `String command`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `String cwd`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `List<String> envVars`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `JsonValue; type "stdio"constant`

                          The type of the object. Always `stdio`.

                          - `STDIO("stdio")`

                    - `JsonValue; type "mcp"constant`

                      The type of the object. Always `mcp`.

                      - `MCP("mcp")`

                  - `WebSearch`

                    - `Optional<List<String>> allowedDomains`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize contextSize`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `LOW("low")`

                      - `MEDIUM("medium")`

                      - `HIGH("high")`

                    - `Optional<Location> location`

                      Approximate location used to localize search results, if provided.

                      - `Optional<String> city`

                        The city name.

                        `minLength: 0`

                      - `Optional<String> country`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Optional<String> region`

                        The region or state name.

                        `minLength: 0`

                      - `Optional<String> timezone`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

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

                  - `JsonValue;`

                    - `JsonValue; type "automations"constant`

                      The type of the object. Always `automations`.

                      - `AUTOMATIONS("automations")`

                - `Optional<Compaction> compaction`

                  The effective context compaction settings.

                  - `boolean async`

                    Whether context is compacted in the background. Defaults to true.

                - `Optional<Experimental> experimental`

                  The effective experimental settings for the agent.

                  - `boolean timeAwareness`

                    Whether the model receives periodic current-time reminders.

              - `Optional<String> agentId`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `AutomationEnvironment environment`

                Configuration or references used to select the execution environment.

                - `JsonValue;`

                  - `JsonValue; type "none"constant`

                    The type of the object. Always `none`.

                    - `NONE("none")`

                - `OpenAIHosted`

                  - `Optional<List<String>> capabilityDirectories`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<ContainerSize> containerSize`

                    The configured container size, or null to use the creation default.

                    - `SMALL("small")`

                    - `MEDIUM("medium")`

                    - `LARGE("large")`

                  - `Optional<Desktop> desktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `boolean enabled`

                      Whether the environment provisions a desktop and browser proxy.

                  - `Optional<String> environmentId`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `Optional<String> environmentTemplateId`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Optional<List<File>> files`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileId:`

                      A project-scoped Files API reference resolved separately for each session.

                      - `String fileId`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `JsonValue; type "file_id"constant`

                        The type of the object. Always `file_id`.

                        - `FILE_ID("file_id")`

                    - `class Inline:`

                      Metadata for confidential inline file contents.

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `long sizeBytes`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `Optional<Network> network`

                    Network overrides, or null to inherit the template or creation default.

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

                      `minItems: 0`, `maxItems: 2000`

                  - `Optional<Packages> packages`

                    Package overrides, or null to inherit the template or creation default.

                    - `List<String> npm`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> python`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> system`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Optional<List<HostedPlugin>> plugins`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `String description`

                      The installed plugin description.

                      `minLength: 0`

                    - `String name`

                      The installed plugin name.

                      `minLength: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                  - `Optional<List<Skill>> skills`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference:`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `String skillId`

                        The referenced skill ID.

                        `minLength: 0`

                      - `JsonValue; type "skill_reference"constant`

                        The type of the object. Always `skill_reference`.

                        - `SKILL_REFERENCE("skill_reference")`

                      - `Optional<String> version`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline:`

                      Safe metadata for an inline skill archive.

                      - `String description`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `String name`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `JsonValue; type "openai_hosted"constant`

                    The type of the object. Always `openai_hosted`.

                    - `OPENAI_HOSTED("openai_hosted")`

                - `SelfHosted`

                  - `List<String> capabilityDirectories`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<String> environmentId`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `JsonValue; type "self_hosted"constant`

                    The type of the object. Always `self_hosted`.

                    - `SELF_HOSTED("self_hosted")`

                  - `String workspaceDirectory`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `List<Input> input`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `List<InputContent> content`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `InputText`

                    - `String text`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `JsonValue; type "input_text"constant`

                      The type of the object. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `JsonValue; type "input_image"constant`

                      The type of the object. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                - `JsonValue; role "user"constant`

                  The role of the message author. Always `user`.

                  - `USER("user")`

                - `JsonValue; type "message"constant`

                  The type of the input item. Always `message`.

                  - `MESSAGE("message")`

              - `Metadata metadata`

                Metadata attached to each new session.

              - `JsonValue; type "new_session"constant`

                The type of the object. Always `new_session`.

                - `NEW_SESSION("new_session")`

              - `List<String> vaultIds`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `ExistingSession`

              - `String instructions`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `String sessionId`

                The session receiving each invocation.

                `minLength: 0`

              - `JsonValue; type "existing_session"constant`

                The type of the object. Always `existing_session`.

                - `EXISTING_SESSION("existing_session")`

          - `String timezone`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `JsonValue; type "periodic"constant`

            The type of the object. Always `periodic`.

            - `PERIODIC("periodic")`

        - `class OneTimeAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `long runAt`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status status`

            Completion means the schedule has finished, not the agent's work.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

            - `COMPLETED("completed")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

          - `JsonValue; type "once"constant`

            The type of the object. Always `once`.

            - `ONCE("once")`

      - `JsonValue; type "automation"constant`

        The type of the object. Always `automation`.

        - `AUTOMATION("automation")`

  - `Status status`

    Delivery status; completed does not mean the agent's work has finished.

    - `QUEUED("queued")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `SKIPPED("skipped")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.invocations.AutomationInvocation;
import com.openai.models.beta.agents.automations.invocations.InvocationCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        AutomationInvocation automationInvocation = client.beta().agents().automations().invocations().create("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "automation_id": "automation_id",
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  },
  "object": "agent.automation.invocation",
  "scheduled_at": 0,
  "session_id": "session_id",
  "skip_reason": "pending_delivery",
  "source": {
    "type": "manual"
  },
  "status": "queued"
}
```

## List automation invocations

`InvocationListPage beta().agents().automations().invocations().list(InvocationListParamsparams = InvocationListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/automations/{automation_id}/invocations`

Lists delivery records for a project-owned automation.

### Parameters

- `InvocationListParams params`

  - `Optional<String> automationId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AutomationInvocation:`

  One attempted delivery by an automation.

  - `String id`

    The invocation ID.

    `minLength: 0`

  - `String automationId`

    The automation that owns the invocation.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Optional<Error> error`

    The permanent delivery failure, or null when no failure occurred.

    - `String code`

      A machine-readable error code.

      `minLength: 0`

    - `String message`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `JsonValue; object_ "agent.automation.invocation"constant`

    Always `agent.automation.invocation`.

    - `AGENT_AUTOMATION_INVOCATION("agent.automation.invocation")`

  - `Optional<Long> scheduledAt`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `Optional<String> sessionId`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `Optional<SkipReason> skipReason`

    Why an occurrence was skipped, or null when it was not skipped.

    - `PENDING_DELIVERY("pending_delivery")`

  - `AutomationInvocationSource source`

    Whether the invocation was manual or scheduled.

    - `JsonValue;`

      - `JsonValue; type "manual"constant`

        The type of the object. Always `manual`.

        - `MANUAL("manual")`

    - `class AutomationInvocationSourceAutomation:`

      - `Automation automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

            - `JsonValue;`

              - `JsonValue; type "developer"constant`

                The type of the object. Always `developer`.

                - `DEVELOPER("developer")`

            - `Agent`

              - `String sessionId`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `String toolCallId`

                The tool call that created the automation.

                `minLength: 0`

              - `JsonValue; type "agent"constant`

                The type of the object. Always `agent`.

                - `AGENT("agent")`

          - `String expression`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `Status status`

            Whether scheduled delivery is active or paused.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

            - `NewSession`

              - `Optional<AutomationAgentConfig> agent`

                The inline agent configuration, or null when agent_id is configured.

                - `Optional<String> instructions`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `String model`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgentConfig multiAgent`

                  The configuration for creating and coordinating subagents.

                  - `boolean enabled`

                    Whether subagent tools are enabled. Defaults to false.

                  - `Optional<Long> maxConcurrentSubagents`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `AgentReasoning reasoning`

                  The configured reasoning policy.

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

                  The configured service-tier policy.

                  - `AUTO("auto")`

                  - `DEFAULT("default")`

                  - `FLEX("flex")`

                  - `PRIORITY("priority")`

                  - `FAST("fast")`

                  - `ULTRAFAST("ultrafast")`

                - `AgentText text`

                  The configured output format and verbosity.

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

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `Function`

                    - `boolean deferLoading`

                      Whether the function is deferred and discovered through tool search.

                    - `String description`

                      A description of what the function does.

                      `minLength: 0`

                    - `String name`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters parameters`

                      A JSON Schema object describing the function's arguments.

                    - `JsonValue; type "function"constant`

                      The type of the object. Always `function`.

                      - `FUNCTION("function")`

                    - `Optional<Boolean> async`

                      Whether the agent continues without waiting for the function result.

                  - `ProgrammaticToolCalling`

                    - `boolean enabled`

                      Whether tools can be called from model-generated code.

                    - `JsonValue; type "programmatic_tool_calling"constant`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

                  - `Mcp`

                    - `Optional<List<String>> allowedTools`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin connectionOrigin`

                      Where outbound MCP HTTP connections originate.

                      - `SERVICE("service")`

                      - `ENVIRONMENT("environment")`

                    - `Optional<String> credentialId`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata requestMetadata`

                      Metadata included with requests to this MCP server.

                    - `boolean required`

                      Whether this MCP server must initialize before the first turn.

                    - `String serverLabel`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `McpTransport transport`

                      The transport used to connect to the MCP server.

                      - `Http`

                        - `String serverUrl`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `JsonValue; type "http"constant`

                          The type of the object. Always `http`.

                          - `HTTP("http")`

                      - `Stdio`

                        - `List<String> args`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `String command`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `String cwd`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `List<String> envVars`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `JsonValue; type "stdio"constant`

                          The type of the object. Always `stdio`.

                          - `STDIO("stdio")`

                    - `JsonValue; type "mcp"constant`

                      The type of the object. Always `mcp`.

                      - `MCP("mcp")`

                  - `WebSearch`

                    - `Optional<List<String>> allowedDomains`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize contextSize`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `LOW("low")`

                      - `MEDIUM("medium")`

                      - `HIGH("high")`

                    - `Optional<Location> location`

                      Approximate location used to localize search results, if provided.

                      - `Optional<String> city`

                        The city name.

                        `minLength: 0`

                      - `Optional<String> country`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Optional<String> region`

                        The region or state name.

                        `minLength: 0`

                      - `Optional<String> timezone`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

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

                  - `JsonValue;`

                    - `JsonValue; type "automations"constant`

                      The type of the object. Always `automations`.

                      - `AUTOMATIONS("automations")`

                - `Optional<Compaction> compaction`

                  The effective context compaction settings.

                  - `boolean async`

                    Whether context is compacted in the background. Defaults to true.

                - `Optional<Experimental> experimental`

                  The effective experimental settings for the agent.

                  - `boolean timeAwareness`

                    Whether the model receives periodic current-time reminders.

              - `Optional<String> agentId`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `AutomationEnvironment environment`

                Configuration or references used to select the execution environment.

                - `JsonValue;`

                  - `JsonValue; type "none"constant`

                    The type of the object. Always `none`.

                    - `NONE("none")`

                - `OpenAIHosted`

                  - `Optional<List<String>> capabilityDirectories`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<ContainerSize> containerSize`

                    The configured container size, or null to use the creation default.

                    - `SMALL("small")`

                    - `MEDIUM("medium")`

                    - `LARGE("large")`

                  - `Optional<Desktop> desktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `boolean enabled`

                      Whether the environment provisions a desktop and browser proxy.

                  - `Optional<String> environmentId`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `Optional<String> environmentTemplateId`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Optional<List<File>> files`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileId:`

                      A project-scoped Files API reference resolved separately for each session.

                      - `String fileId`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `JsonValue; type "file_id"constant`

                        The type of the object. Always `file_id`.

                        - `FILE_ID("file_id")`

                    - `class Inline:`

                      Metadata for confidential inline file contents.

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `long sizeBytes`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `Optional<Network> network`

                    Network overrides, or null to inherit the template or creation default.

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

                      `minItems: 0`, `maxItems: 2000`

                  - `Optional<Packages> packages`

                    Package overrides, or null to inherit the template or creation default.

                    - `List<String> npm`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> python`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> system`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Optional<List<HostedPlugin>> plugins`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `String description`

                      The installed plugin description.

                      `minLength: 0`

                    - `String name`

                      The installed plugin name.

                      `minLength: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                  - `Optional<List<Skill>> skills`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference:`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `String skillId`

                        The referenced skill ID.

                        `minLength: 0`

                      - `JsonValue; type "skill_reference"constant`

                        The type of the object. Always `skill_reference`.

                        - `SKILL_REFERENCE("skill_reference")`

                      - `Optional<String> version`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline:`

                      Safe metadata for an inline skill archive.

                      - `String description`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `String name`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `JsonValue; type "openai_hosted"constant`

                    The type of the object. Always `openai_hosted`.

                    - `OPENAI_HOSTED("openai_hosted")`

                - `SelfHosted`

                  - `List<String> capabilityDirectories`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<String> environmentId`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `JsonValue; type "self_hosted"constant`

                    The type of the object. Always `self_hosted`.

                    - `SELF_HOSTED("self_hosted")`

                  - `String workspaceDirectory`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `List<Input> input`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `List<InputContent> content`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `InputText`

                    - `String text`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `JsonValue; type "input_text"constant`

                      The type of the object. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `JsonValue; type "input_image"constant`

                      The type of the object. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                - `JsonValue; role "user"constant`

                  The role of the message author. Always `user`.

                  - `USER("user")`

                - `JsonValue; type "message"constant`

                  The type of the input item. Always `message`.

                  - `MESSAGE("message")`

              - `Metadata metadata`

                Metadata attached to each new session.

              - `JsonValue; type "new_session"constant`

                The type of the object. Always `new_session`.

                - `NEW_SESSION("new_session")`

              - `List<String> vaultIds`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `ExistingSession`

              - `String instructions`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `String sessionId`

                The session receiving each invocation.

                `minLength: 0`

              - `JsonValue; type "existing_session"constant`

                The type of the object. Always `existing_session`.

                - `EXISTING_SESSION("existing_session")`

          - `String timezone`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `JsonValue; type "periodic"constant`

            The type of the object. Always `periodic`.

            - `PERIODIC("periodic")`

        - `class OneTimeAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `long runAt`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status status`

            Completion means the schedule has finished, not the agent's work.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

            - `COMPLETED("completed")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

          - `JsonValue; type "once"constant`

            The type of the object. Always `once`.

            - `ONCE("once")`

      - `JsonValue; type "automation"constant`

        The type of the object. Always `automation`.

        - `AUTOMATION("automation")`

  - `Status status`

    Delivery status; completed does not mean the agent's work has finished.

    - `QUEUED("queued")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `SKIPPED("skipped")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.invocations.InvocationListPage;
import com.openai.models.beta.agents.automations.invocations.InvocationListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InvocationListPage page = client.beta().agents().automations().invocations().list("automation_id");
    }
}
```

#### 200 — Example

```json
{
  "data": [
    {
      "id": "id",
      "automation_id": "automation_id",
      "created_at": 0,
      "error": {
        "code": "code",
        "message": "message"
      },
      "object": "agent.automation.invocation",
      "scheduled_at": 0,
      "session_id": "session_id",
      "skip_reason": "pending_delivery",
      "source": {
        "type": "manual"
      },
      "status": "queued"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Get an automation invocation

`AutomationInvocation beta().agents().automations().invocations().retrieve(InvocationRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/automations/{automation_id}/invocations/{invocation_id}`

Retrieves a delivery record for a project-owned automation.

### Parameters

- `InvocationRetrieveParams params`

  - `String automationId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> invocationId`

    `minLength: 0`, `maxLength: 1048576`

### Returns

- `class AutomationInvocation:`

  One attempted delivery by an automation.

  - `String id`

    The invocation ID.

    `minLength: 0`

  - `String automationId`

    The automation that owns the invocation.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Optional<Error> error`

    The permanent delivery failure, or null when no failure occurred.

    - `String code`

      A machine-readable error code.

      `minLength: 0`

    - `String message`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `JsonValue; object_ "agent.automation.invocation"constant`

    Always `agent.automation.invocation`.

    - `AGENT_AUTOMATION_INVOCATION("agent.automation.invocation")`

  - `Optional<Long> scheduledAt`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `Optional<String> sessionId`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `Optional<SkipReason> skipReason`

    Why an occurrence was skipped, or null when it was not skipped.

    - `PENDING_DELIVERY("pending_delivery")`

  - `AutomationInvocationSource source`

    Whether the invocation was manual or scheduled.

    - `JsonValue;`

      - `JsonValue; type "manual"constant`

        The type of the object. Always `manual`.

        - `MANUAL("manual")`

    - `class AutomationInvocationSourceAutomation:`

      - `Automation automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

            - `JsonValue;`

              - `JsonValue; type "developer"constant`

                The type of the object. Always `developer`.

                - `DEVELOPER("developer")`

            - `Agent`

              - `String sessionId`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `String toolCallId`

                The tool call that created the automation.

                `minLength: 0`

              - `JsonValue; type "agent"constant`

                The type of the object. Always `agent`.

                - `AGENT("agent")`

          - `String expression`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `Status status`

            Whether scheduled delivery is active or paused.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

            - `NewSession`

              - `Optional<AutomationAgentConfig> agent`

                The inline agent configuration, or null when agent_id is configured.

                - `Optional<String> instructions`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `String model`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgentConfig multiAgent`

                  The configuration for creating and coordinating subagents.

                  - `boolean enabled`

                    Whether subagent tools are enabled. Defaults to false.

                  - `Optional<Long> maxConcurrentSubagents`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `AgentReasoning reasoning`

                  The configured reasoning policy.

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

                  The configured service-tier policy.

                  - `AUTO("auto")`

                  - `DEFAULT("default")`

                  - `FLEX("flex")`

                  - `PRIORITY("priority")`

                  - `FAST("fast")`

                  - `ULTRAFAST("ultrafast")`

                - `AgentText text`

                  The configured output format and verbosity.

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

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `Function`

                    - `boolean deferLoading`

                      Whether the function is deferred and discovered through tool search.

                    - `String description`

                      A description of what the function does.

                      `minLength: 0`

                    - `String name`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters parameters`

                      A JSON Schema object describing the function's arguments.

                    - `JsonValue; type "function"constant`

                      The type of the object. Always `function`.

                      - `FUNCTION("function")`

                    - `Optional<Boolean> async`

                      Whether the agent continues without waiting for the function result.

                  - `ProgrammaticToolCalling`

                    - `boolean enabled`

                      Whether tools can be called from model-generated code.

                    - `JsonValue; type "programmatic_tool_calling"constant`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

                  - `Mcp`

                    - `Optional<List<String>> allowedTools`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin connectionOrigin`

                      Where outbound MCP HTTP connections originate.

                      - `SERVICE("service")`

                      - `ENVIRONMENT("environment")`

                    - `Optional<String> credentialId`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata requestMetadata`

                      Metadata included with requests to this MCP server.

                    - `boolean required`

                      Whether this MCP server must initialize before the first turn.

                    - `String serverLabel`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `McpTransport transport`

                      The transport used to connect to the MCP server.

                      - `Http`

                        - `String serverUrl`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `JsonValue; type "http"constant`

                          The type of the object. Always `http`.

                          - `HTTP("http")`

                      - `Stdio`

                        - `List<String> args`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `String command`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `String cwd`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `List<String> envVars`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `JsonValue; type "stdio"constant`

                          The type of the object. Always `stdio`.

                          - `STDIO("stdio")`

                    - `JsonValue; type "mcp"constant`

                      The type of the object. Always `mcp`.

                      - `MCP("mcp")`

                  - `WebSearch`

                    - `Optional<List<String>> allowedDomains`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize contextSize`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `LOW("low")`

                      - `MEDIUM("medium")`

                      - `HIGH("high")`

                    - `Optional<Location> location`

                      Approximate location used to localize search results, if provided.

                      - `Optional<String> city`

                        The city name.

                        `minLength: 0`

                      - `Optional<String> country`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Optional<String> region`

                        The region or state name.

                        `minLength: 0`

                      - `Optional<String> timezone`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

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

                  - `JsonValue;`

                    - `JsonValue; type "automations"constant`

                      The type of the object. Always `automations`.

                      - `AUTOMATIONS("automations")`

                - `Optional<Compaction> compaction`

                  The effective context compaction settings.

                  - `boolean async`

                    Whether context is compacted in the background. Defaults to true.

                - `Optional<Experimental> experimental`

                  The effective experimental settings for the agent.

                  - `boolean timeAwareness`

                    Whether the model receives periodic current-time reminders.

              - `Optional<String> agentId`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `AutomationEnvironment environment`

                Configuration or references used to select the execution environment.

                - `JsonValue;`

                  - `JsonValue; type "none"constant`

                    The type of the object. Always `none`.

                    - `NONE("none")`

                - `OpenAIHosted`

                  - `Optional<List<String>> capabilityDirectories`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<ContainerSize> containerSize`

                    The configured container size, or null to use the creation default.

                    - `SMALL("small")`

                    - `MEDIUM("medium")`

                    - `LARGE("large")`

                  - `Optional<Desktop> desktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `boolean enabled`

                      Whether the environment provisions a desktop and browser proxy.

                  - `Optional<String> environmentId`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `Optional<String> environmentTemplateId`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Optional<List<File>> files`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileId:`

                      A project-scoped Files API reference resolved separately for each session.

                      - `String fileId`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `JsonValue; type "file_id"constant`

                        The type of the object. Always `file_id`.

                        - `FILE_ID("file_id")`

                    - `class Inline:`

                      Metadata for confidential inline file contents.

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `long sizeBytes`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `Optional<Network> network`

                    Network overrides, or null to inherit the template or creation default.

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

                      `minItems: 0`, `maxItems: 2000`

                  - `Optional<Packages> packages`

                    Package overrides, or null to inherit the template or creation default.

                    - `List<String> npm`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> python`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> system`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Optional<List<HostedPlugin>> plugins`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `String description`

                      The installed plugin description.

                      `minLength: 0`

                    - `String name`

                      The installed plugin name.

                      `minLength: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                  - `Optional<List<Skill>> skills`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference:`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `String skillId`

                        The referenced skill ID.

                        `minLength: 0`

                      - `JsonValue; type "skill_reference"constant`

                        The type of the object. Always `skill_reference`.

                        - `SKILL_REFERENCE("skill_reference")`

                      - `Optional<String> version`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline:`

                      Safe metadata for an inline skill archive.

                      - `String description`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `String name`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `JsonValue; type "openai_hosted"constant`

                    The type of the object. Always `openai_hosted`.

                    - `OPENAI_HOSTED("openai_hosted")`

                - `SelfHosted`

                  - `List<String> capabilityDirectories`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<String> environmentId`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `JsonValue; type "self_hosted"constant`

                    The type of the object. Always `self_hosted`.

                    - `SELF_HOSTED("self_hosted")`

                  - `String workspaceDirectory`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `List<Input> input`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `List<InputContent> content`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `InputText`

                    - `String text`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `JsonValue; type "input_text"constant`

                      The type of the object. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `JsonValue; type "input_image"constant`

                      The type of the object. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                - `JsonValue; role "user"constant`

                  The role of the message author. Always `user`.

                  - `USER("user")`

                - `JsonValue; type "message"constant`

                  The type of the input item. Always `message`.

                  - `MESSAGE("message")`

              - `Metadata metadata`

                Metadata attached to each new session.

              - `JsonValue; type "new_session"constant`

                The type of the object. Always `new_session`.

                - `NEW_SESSION("new_session")`

              - `List<String> vaultIds`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `ExistingSession`

              - `String instructions`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `String sessionId`

                The session receiving each invocation.

                `minLength: 0`

              - `JsonValue; type "existing_session"constant`

                The type of the object. Always `existing_session`.

                - `EXISTING_SESSION("existing_session")`

          - `String timezone`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `JsonValue; type "periodic"constant`

            The type of the object. Always `periodic`.

            - `PERIODIC("periodic")`

        - `class OneTimeAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `long runAt`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status status`

            Completion means the schedule has finished, not the agent's work.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

            - `COMPLETED("completed")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

          - `JsonValue; type "once"constant`

            The type of the object. Always `once`.

            - `ONCE("once")`

      - `JsonValue; type "automation"constant`

        The type of the object. Always `automation`.

        - `AUTOMATION("automation")`

  - `Status status`

    Delivery status; completed does not mean the agent's work has finished.

    - `QUEUED("queued")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `SKIPPED("skipped")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.automations.invocations.AutomationInvocation;
import com.openai.models.beta.agents.automations.invocations.InvocationRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        InvocationRetrieveParams params = InvocationRetrieveParams.builder()
            .automationId("automation_id")
            .invocationId("invocation_id")
            .build();
        AutomationInvocation automationInvocation = client.beta().agents().automations().invocations().retrieve(params);
    }
}
```

#### 200 — Example

```json
{
  "id": "id",
  "automation_id": "automation_id",
  "created_at": 0,
  "error": {
    "code": "code",
    "message": "message"
  },
  "object": "agent.automation.invocation",
  "scheduled_at": 0,
  "session_id": "session_id",
  "skip_reason": "pending_delivery",
  "source": {
    "type": "manual"
  },
  "status": "queued"
}
```

## Domain Types

### Automation Invocation

- `class AutomationInvocation:`

  One attempted delivery by an automation.

  - `String id`

    The invocation ID.

    `minLength: 0`

  - `String automationId`

    The automation that owns the invocation.

    `minLength: 0`

  - `long createdAt`

    The creation time as a Unix timestamp in seconds.

    `format: int64`

  - `Optional<Error> error`

    The permanent delivery failure, or null when no failure occurred.

    - `String code`

      A machine-readable error code.

      `minLength: 0`

    - `String message`

      A public explanation of the delivery failure.

      `minLength: 0`

  - `JsonValue; object_ "agent.automation.invocation"constant`

    Always `agent.automation.invocation`.

    - `AGENT_AUTOMATION_INVOCATION("agent.automation.invocation")`

  - `Optional<Long> scheduledAt`

    The intended occurrence as a Unix timestamp in seconds, or null for manual runs.

    `format: int64`

  - `Optional<String> sessionId`

    The target or newly created session ID, or null before one is available.

    `minLength: 0`

  - `Optional<SkipReason> skipReason`

    Why an occurrence was skipped, or null when it was not skipped.

    - `PENDING_DELIVERY("pending_delivery")`

  - `AutomationInvocationSource source`

    Whether the invocation was manual or scheduled.

    - `JsonValue;`

      - `JsonValue; type "manual"constant`

        The type of the object. Always `manual`.

        - `MANUAL("manual")`

    - `class AutomationInvocationSourceAutomation:`

      - `Automation automation`

        The automation snapshot for this occurrence, excluding confidential values.

        - `class PeriodicAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

            - `JsonValue;`

              - `JsonValue; type "developer"constant`

                The type of the object. Always `developer`.

                - `DEVELOPER("developer")`

            - `Agent`

              - `String sessionId`

                The creator session, which is also the automation's target.

                `minLength: 0`

              - `String toolCallId`

                The tool call that created the automation.

                `minLength: 0`

              - `JsonValue; type "agent"constant`

                The type of the object. Always `agent`.

                - `AGENT("agent")`

          - `String expression`

            The cron expression determining scheduled occurrences.

            `minLength: 0`

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `Status status`

            Whether scheduled delivery is active or paused.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

            - `NewSession`

              - `Optional<AutomationAgentConfig> agent`

                The inline agent configuration, or null when agent_id is configured.

                - `Optional<String> instructions`

                  Custom instructions, or null when absent.

                  `minLength: 0`

                - `String model`

                  The requested model name.

                  `minLength: 0`

                - `MultiAgentConfig multiAgent`

                  The configuration for creating and coordinating subagents.

                  - `boolean enabled`

                    Whether subagent tools are enabled. Defaults to false.

                  - `Optional<Long> maxConcurrentSubagents`

                    Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                    `format: int64`, `minimum: 1`, `maximum: 4294967295`

                - `AgentReasoning reasoning`

                  The configured reasoning policy.

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

                  The configured service-tier policy.

                  - `AUTO("auto")`

                  - `DEFAULT("default")`

                  - `FLEX("flex")`

                  - `PRIORITY("priority")`

                  - `FAST("fast")`

                  - `ULTRAFAST("ultrafast")`

                - `AgentText text`

                  The configured output format and verbosity.

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

                  Configured tools, excluding confidential credentials.

                  `minItems: 0`, `maxItems: 2000`

                  - `Function`

                    - `boolean deferLoading`

                      Whether the function is deferred and discovered through tool search.

                    - `String description`

                      A description of what the function does.

                      `minLength: 0`

                    - `String name`

                      The name of the function.

                      `minLength: 0`

                    - `Parameters parameters`

                      A JSON Schema object describing the function's arguments.

                    - `JsonValue; type "function"constant`

                      The type of the object. Always `function`.

                      - `FUNCTION("function")`

                    - `Optional<Boolean> async`

                      Whether the agent continues without waiting for the function result.

                  - `ProgrammaticToolCalling`

                    - `boolean enabled`

                      Whether tools can be called from model-generated code.

                    - `JsonValue; type "programmatic_tool_calling"constant`

                      The type of the object. Always `programmatic_tool_calling`.

                      - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

                  - `Mcp`

                    - `Optional<List<String>> allowedTools`

                      The MCP tools the agent may call.

                      `minItems: 0`, `maxItems: 2000`

                    - `ConnectionOrigin connectionOrigin`

                      Where outbound MCP HTTP connections originate.

                      - `SERVICE("service")`

                      - `ENVIRONMENT("environment")`

                    - `Optional<String> credentialId`

                      The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                      `minLength: 0`

                    - `RequestMetadata requestMetadata`

                      Metadata included with requests to this MCP server.

                    - `boolean required`

                      Whether this MCP server must initialize before the first turn.

                    - `String serverLabel`

                      A label used to identify the MCP server in tool calls.

                      `minLength: 0`

                    - `McpTransport transport`

                      The transport used to connect to the MCP server.

                      - `Http`

                        - `String serverUrl`

                          The URL of the MCP server.

                          `minLength: 0`

                        - `JsonValue; type "http"constant`

                          The type of the object. Always `http`.

                          - `HTTP("http")`

                      - `Stdio`

                        - `List<String> args`

                          Arguments passed to the MCP server command.

                          `minItems: 0`, `maxItems: 2000`

                        - `String command`

                          The command used to start the MCP server.

                          `minLength: 0`

                        - `String cwd`

                          The working directory used to start the MCP server.

                          `minLength: 0`

                        - `List<String> envVars`

                          Environment variable names inherited from the execution environment.

                          `minItems: 0`, `maxItems: 2000`

                        - `JsonValue; type "stdio"constant`

                          The type of the object. Always `stdio`.

                          - `STDIO("stdio")`

                    - `JsonValue; type "mcp"constant`

                      The type of the object. Always `mcp`.

                      - `MCP("mcp")`

                  - `WebSearch`

                    - `Optional<List<String>> allowedDomains`

                      Allowed search domains, or `null` when the search is unrestricted.

                      `minItems: 0`, `maxItems: 2000`

                    - `ContextSize contextSize`

                      The amount of search context made available to the model. Defaults to `medium`.

                      - `LOW("low")`

                      - `MEDIUM("medium")`

                      - `HIGH("high")`

                    - `Optional<Location> location`

                      Approximate location used to localize search results, if provided.

                      - `Optional<String> city`

                        The city name.

                        `minLength: 0`

                      - `Optional<String> country`

                        The two-letter ISO country code, such as `US`.

                        `minLength: 0`

                      - `Optional<String> region`

                        The region or state name.

                        `minLength: 0`

                      - `Optional<String> timezone`

                        The IANA timezone, such as `America/Los_Angeles`.

                        `minLength: 0`

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

                  - `JsonValue;`

                    - `JsonValue; type "automations"constant`

                      The type of the object. Always `automations`.

                      - `AUTOMATIONS("automations")`

                - `Optional<Compaction> compaction`

                  The effective context compaction settings.

                  - `boolean async`

                    Whether context is compacted in the background. Defaults to true.

                - `Optional<Experimental> experimental`

                  The effective experimental settings for the agent.

                  - `boolean timeAwareness`

                    Whether the model receives periodic current-time reminders.

              - `Optional<String> agentId`

                The saved agent reference, or null when an inline agent is configured.

                `minLength: 0`

              - `AutomationEnvironment environment`

                Configuration or references used to select the execution environment.

                - `JsonValue;`

                  - `JsonValue; type "none"constant`

                    The type of the object. Always `none`.

                    - `NONE("none")`

                - `OpenAIHosted`

                  - `Optional<List<String>> capabilityDirectories`

                    Directory overrides, or null to inherit the template or creation default.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<ContainerSize> containerSize`

                    The configured container size, or null to use the creation default.

                    - `SMALL("small")`

                    - `MEDIUM("medium")`

                    - `LARGE("large")`

                  - `Optional<Desktop> desktop`

                    Desktop overrides, or null to inherit the template or creation default.

                    - `boolean enabled`

                      Whether the environment provisions a desktop and browser proxy.

                  - `Optional<String> environmentId`

                    An existing environment reference, or null when provisioning a new environment.

                    `minLength: 0`

                  - `Optional<String> environmentTemplateId`

                    A template reference, or null when no template is selected.

                    `minLength: 0`

                  - `Optional<List<File>> files`

                    File overrides, excluding contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class FileId:`

                      A project-scoped Files API reference resolved separately for each session.

                      - `String fileId`

                        The ID of the uploaded file.

                        `minLength: 0`

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `JsonValue; type "file_id"constant`

                        The type of the object. Always `file_id`.

                        - `FILE_ID("file_id")`

                    - `class Inline:`

                      Metadata for confidential inline file contents.

                      - `String path`

                        The file's absolute path inside the environment.

                        `minLength: 0`

                      - `long sizeBytes`

                        The decoded size of the inline file in bytes.

                        `format: int64`, `minimum: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `Optional<Network> network`

                    Network overrides, or null to inherit the template or creation default.

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

                      `minItems: 0`, `maxItems: 2000`

                  - `Optional<Packages> packages`

                    Package overrides, or null to inherit the template or creation default.

                    - `List<String> npm`

                      npm packages installed globally in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> python`

                      Python packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                    - `List<String> system`

                      System packages installed in the environment.

                      `minItems: 0`, `maxItems: 16384`

                  - `Optional<List<HostedPlugin>> plugins`

                    Plugin overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `String description`

                      The installed plugin description.

                      `minLength: 0`

                    - `String name`

                      The installed plugin name.

                      `minLength: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                  - `Optional<List<Skill>> skills`

                    Skill overrides, excluding archive contents, or null to inherit.

                    `minItems: 0`, `maxItems: 2000`

                    - `class SkillReference:`

                      A skill resolved afresh from the Skills API whenever a session starts.

                      - `String skillId`

                        The referenced skill ID.

                        `minLength: 0`

                      - `JsonValue; type "skill_reference"constant`

                        The type of the object. Always `skill_reference`.

                        - `SKILL_REFERENCE("skill_reference")`

                      - `Optional<String> version`

                        The requested version selector, including `latest`.

                        `minLength: 0`

                    - `class Inline:`

                      Safe metadata for an inline skill archive.

                      - `String description`

                        The skill description declared in `SKILL.md`.

                        `minLength: 0`

                      - `String name`

                        The skill name declared in `SKILL.md`.

                        `minLength: 0`

                      - `JsonValue; type "inline"constant`

                        The type of the object. Always `inline`.

                        - `INLINE("inline")`

                  - `JsonValue; type "openai_hosted"constant`

                    The type of the object. Always `openai_hosted`.

                    - `OPENAI_HOSTED("openai_hosted")`

                - `SelfHosted`

                  - `List<String> capabilityDirectories`

                    Directories that expose capabilities to the agent.

                    `minItems: 0`, `maxItems: 2000`

                  - `Optional<String> environmentId`

                    An existing registration, or null to create a session-owned environment.

                    `minLength: 0`

                  - `JsonValue; type "self_hosted"constant`

                    The type of the object. Always `self_hosted`.

                    - `SELF_HOSTED("self_hosted")`

                  - `String workspaceDirectory`

                    The absolute project directory in the environment.

                    `minLength: 0`

              - `List<Input> input`

                Initial input delivered to each new session.

                `minItems: 0`, `maxItems: 2000`

                - `List<InputContent> content`

                  The content of the message.

                  `minItems: 0`, `maxItems: 2000`

                  - `InputText`

                    - `String text`

                      The text supplied to the agent.

                      `minLength: 0`

                    - `JsonValue; type "input_text"constant`

                      The type of the object. Always `input_text`.

                      - `INPUT_TEXT("input_text")`

                  - `InputImage`

                    - `String imageUrl`

                      The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                      `minLength: 0`

                    - `JsonValue; type "input_image"constant`

                      The type of the object. Always `input_image`.

                      - `INPUT_IMAGE("input_image")`

                - `JsonValue; role "user"constant`

                  The role of the message author. Always `user`.

                  - `USER("user")`

                - `JsonValue; type "message"constant`

                  The type of the input item. Always `message`.

                  - `MESSAGE("message")`

              - `Metadata metadata`

                Metadata attached to each new session.

              - `JsonValue; type "new_session"constant`

                The type of the object. Always `new_session`.

                - `NEW_SESSION("new_session")`

              - `List<String> vaultIds`

                Vaults made available to each new session.

                `minItems: 0`, `maxItems: 2000`

            - `ExistingSession`

              - `String instructions`

                Saved instructions delivered as an automation notification.

                `minLength: 0`

              - `String sessionId`

                The session receiving each invocation.

                `minLength: 0`

              - `JsonValue; type "existing_session"constant`

                The type of the object. Always `existing_session`.

                - `EXISTING_SESSION("existing_session")`

          - `String timezone`

            The timezone used to interpret the expression.

            `minLength: 0`

          - `JsonValue; type "periodic"constant`

            The type of the object. Always `periodic`.

            - `PERIODIC("periodic")`

        - `class OneTimeAutomation:`

          Fields shared by periodic and one-time automations.

          - `String id`

            The automation ID.

            `minLength: 0`

          - `long createdAt`

            The creation time as a Unix timestamp in seconds.

            `format: int64`

          - `AutomationCreatedBy createdBy`

            Service-recorded provenance; callers cannot supply this field.

          - `Metadata metadata`

            Custom string key-value pairs attached to the automation.

          - `String name`

            The automation's display name.

            `minLength: 0`

          - `JsonValue; object_ "agent.automation"constant`

            Always `agent.automation`.

            - `AGENT_AUTOMATION("agent.automation")`

          - `long runAt`

            The Unix timestamp, in seconds, of the scheduled occurrence.

            `format: int64`

          - `Status status`

            Completion means the schedule has finished, not the agent's work.

            - `ACTIVE("active")`

            - `PAUSED("paused")`

            - `COMPLETED("completed")`

          - `AutomationTarget target`

            The session configuration or existing session receiving invocations.

          - `JsonValue; type "once"constant`

            The type of the object. Always `once`.

            - `ONCE("once")`

      - `JsonValue; type "automation"constant`

        The type of the object. Always `automation`.

        - `AUTOMATION("automation")`

  - `Status status`

    Delivery status; completed does not mean the agent's work has finished.

    - `QUEUED("queued")`

    - `COMPLETED("completed")`

    - `FAILED("failed")`

    - `SKIPPED("skipped")`

### Automation Invocation Source

- `class AutomationInvocationSource: A class that can be one of several variants.union`

  - `JsonValue;`

    - `JsonValue; type "manual"constant`

      The type of the object. Always `manual`.

      - `MANUAL("manual")`

  - `class AutomationInvocationSourceAutomation:`

    - `Automation automation`

      The automation snapshot for this occurrence, excluding confidential values.

      - `class PeriodicAutomation:`

        Fields shared by periodic and one-time automations.

        - `String id`

          The automation ID.

          `minLength: 0`

        - `long createdAt`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `AutomationCreatedBy createdBy`

          Service-recorded provenance; callers cannot supply this field.

          - `JsonValue;`

            - `JsonValue; type "developer"constant`

              The type of the object. Always `developer`.

              - `DEVELOPER("developer")`

          - `Agent`

            - `String sessionId`

              The creator session, which is also the automation's target.

              `minLength: 0`

            - `String toolCallId`

              The tool call that created the automation.

              `minLength: 0`

            - `JsonValue; type "agent"constant`

              The type of the object. Always `agent`.

              - `AGENT("agent")`

        - `String expression`

          The cron expression determining scheduled occurrences.

          `minLength: 0`

        - `Metadata metadata`

          Custom string key-value pairs attached to the automation.

        - `String name`

          The automation's display name.

          `minLength: 0`

        - `JsonValue; object_ "agent.automation"constant`

          Always `agent.automation`.

          - `AGENT_AUTOMATION("agent.automation")`

        - `Status status`

          Whether scheduled delivery is active or paused.

          - `ACTIVE("active")`

          - `PAUSED("paused")`

        - `AutomationTarget target`

          The session configuration or existing session receiving invocations.

          - `NewSession`

            - `Optional<AutomationAgentConfig> agent`

              The inline agent configuration, or null when agent_id is configured.

              - `Optional<String> instructions`

                Custom instructions, or null when absent.

                `minLength: 0`

              - `String model`

                The requested model name.

                `minLength: 0`

              - `MultiAgentConfig multiAgent`

                The configuration for creating and coordinating subagents.

                - `boolean enabled`

                  Whether subagent tools are enabled. Defaults to false.

                - `Optional<Long> maxConcurrentSubagents`

                  Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                  `format: int64`, `minimum: 1`, `maximum: 4294967295`

              - `AgentReasoning reasoning`

                The configured reasoning policy.

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

                The configured service-tier policy.

                - `AUTO("auto")`

                - `DEFAULT("default")`

                - `FLEX("flex")`

                - `PRIORITY("priority")`

                - `FAST("fast")`

                - `ULTRAFAST("ultrafast")`

              - `AgentText text`

                The configured output format and verbosity.

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

                Configured tools, excluding confidential credentials.

                `minItems: 0`, `maxItems: 2000`

                - `Function`

                  - `boolean deferLoading`

                    Whether the function is deferred and discovered through tool search.

                  - `String description`

                    A description of what the function does.

                    `minLength: 0`

                  - `String name`

                    The name of the function.

                    `minLength: 0`

                  - `Parameters parameters`

                    A JSON Schema object describing the function's arguments.

                  - `JsonValue; type "function"constant`

                    The type of the object. Always `function`.

                    - `FUNCTION("function")`

                  - `Optional<Boolean> async`

                    Whether the agent continues without waiting for the function result.

                - `ProgrammaticToolCalling`

                  - `boolean enabled`

                    Whether tools can be called from model-generated code.

                  - `JsonValue; type "programmatic_tool_calling"constant`

                    The type of the object. Always `programmatic_tool_calling`.

                    - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

                - `Mcp`

                  - `Optional<List<String>> allowedTools`

                    The MCP tools the agent may call.

                    `minItems: 0`, `maxItems: 2000`

                  - `ConnectionOrigin connectionOrigin`

                    Where outbound MCP HTTP connections originate.

                    - `SERVICE("service")`

                    - `ENVIRONMENT("environment")`

                  - `Optional<String> credentialId`

                    The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                    `minLength: 0`

                  - `RequestMetadata requestMetadata`

                    Metadata included with requests to this MCP server.

                  - `boolean required`

                    Whether this MCP server must initialize before the first turn.

                  - `String serverLabel`

                    A label used to identify the MCP server in tool calls.

                    `minLength: 0`

                  - `McpTransport transport`

                    The transport used to connect to the MCP server.

                    - `Http`

                      - `String serverUrl`

                        The URL of the MCP server.

                        `minLength: 0`

                      - `JsonValue; type "http"constant`

                        The type of the object. Always `http`.

                        - `HTTP("http")`

                    - `Stdio`

                      - `List<String> args`

                        Arguments passed to the MCP server command.

                        `minItems: 0`, `maxItems: 2000`

                      - `String command`

                        The command used to start the MCP server.

                        `minLength: 0`

                      - `String cwd`

                        The working directory used to start the MCP server.

                        `minLength: 0`

                      - `List<String> envVars`

                        Environment variable names inherited from the execution environment.

                        `minItems: 0`, `maxItems: 2000`

                      - `JsonValue; type "stdio"constant`

                        The type of the object. Always `stdio`.

                        - `STDIO("stdio")`

                  - `JsonValue; type "mcp"constant`

                    The type of the object. Always `mcp`.

                    - `MCP("mcp")`

                - `WebSearch`

                  - `Optional<List<String>> allowedDomains`

                    Allowed search domains, or `null` when the search is unrestricted.

                    `minItems: 0`, `maxItems: 2000`

                  - `ContextSize contextSize`

                    The amount of search context made available to the model. Defaults to `medium`.

                    - `LOW("low")`

                    - `MEDIUM("medium")`

                    - `HIGH("high")`

                  - `Optional<Location> location`

                    Approximate location used to localize search results, if provided.

                    - `Optional<String> city`

                      The city name.

                      `minLength: 0`

                    - `Optional<String> country`

                      The two-letter ISO country code, such as `US`.

                      `minLength: 0`

                    - `Optional<String> region`

                      The region or state name.

                      `minLength: 0`

                    - `Optional<String> timezone`

                      The IANA timezone, such as `America/Los_Angeles`.

                      `minLength: 0`

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

                - `JsonValue;`

                  - `JsonValue; type "automations"constant`

                    The type of the object. Always `automations`.

                    - `AUTOMATIONS("automations")`

              - `Optional<Compaction> compaction`

                The effective context compaction settings.

                - `boolean async`

                  Whether context is compacted in the background. Defaults to true.

              - `Optional<Experimental> experimental`

                The effective experimental settings for the agent.

                - `boolean timeAwareness`

                  Whether the model receives periodic current-time reminders.

            - `Optional<String> agentId`

              The saved agent reference, or null when an inline agent is configured.

              `minLength: 0`

            - `AutomationEnvironment environment`

              Configuration or references used to select the execution environment.

              - `JsonValue;`

                - `JsonValue; type "none"constant`

                  The type of the object. Always `none`.

                  - `NONE("none")`

              - `OpenAIHosted`

                - `Optional<List<String>> capabilityDirectories`

                  Directory overrides, or null to inherit the template or creation default.

                  `minItems: 0`, `maxItems: 2000`

                - `Optional<ContainerSize> containerSize`

                  The configured container size, or null to use the creation default.

                  - `SMALL("small")`

                  - `MEDIUM("medium")`

                  - `LARGE("large")`

                - `Optional<Desktop> desktop`

                  Desktop overrides, or null to inherit the template or creation default.

                  - `boolean enabled`

                    Whether the environment provisions a desktop and browser proxy.

                - `Optional<String> environmentId`

                  An existing environment reference, or null when provisioning a new environment.

                  `minLength: 0`

                - `Optional<String> environmentTemplateId`

                  A template reference, or null when no template is selected.

                  `minLength: 0`

                - `Optional<List<File>> files`

                  File overrides, excluding contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `class FileId:`

                    A project-scoped Files API reference resolved separately for each session.

                    - `String fileId`

                      The ID of the uploaded file.

                      `minLength: 0`

                    - `String path`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `JsonValue; type "file_id"constant`

                      The type of the object. Always `file_id`.

                      - `FILE_ID("file_id")`

                  - `class Inline:`

                    Metadata for confidential inline file contents.

                    - `String path`

                      The file's absolute path inside the environment.

                      `minLength: 0`

                    - `long sizeBytes`

                      The decoded size of the inline file in bytes.

                      `format: int64`, `minimum: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                - `Optional<Network> network`

                  Network overrides, or null to inherit the template or creation default.

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

                    `minItems: 0`, `maxItems: 2000`

                - `Optional<Packages> packages`

                  Package overrides, or null to inherit the template or creation default.

                  - `List<String> npm`

                    npm packages installed globally in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `List<String> python`

                    Python packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                  - `List<String> system`

                    System packages installed in the environment.

                    `minItems: 0`, `maxItems: 16384`

                - `Optional<List<HostedPlugin>> plugins`

                  Plugin overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `String description`

                    The installed plugin description.

                    `minLength: 0`

                  - `String name`

                    The installed plugin name.

                    `minLength: 0`

                  - `JsonValue; type "inline"constant`

                    The type of the object. Always `inline`.

                    - `INLINE("inline")`

                - `Optional<List<Skill>> skills`

                  Skill overrides, excluding archive contents, or null to inherit.

                  `minItems: 0`, `maxItems: 2000`

                  - `class SkillReference:`

                    A skill resolved afresh from the Skills API whenever a session starts.

                    - `String skillId`

                      The referenced skill ID.

                      `minLength: 0`

                    - `JsonValue; type "skill_reference"constant`

                      The type of the object. Always `skill_reference`.

                      - `SKILL_REFERENCE("skill_reference")`

                    - `Optional<String> version`

                      The requested version selector, including `latest`.

                      `minLength: 0`

                  - `class Inline:`

                    Safe metadata for an inline skill archive.

                    - `String description`

                      The skill description declared in `SKILL.md`.

                      `minLength: 0`

                    - `String name`

                      The skill name declared in `SKILL.md`.

                      `minLength: 0`

                    - `JsonValue; type "inline"constant`

                      The type of the object. Always `inline`.

                      - `INLINE("inline")`

                - `JsonValue; type "openai_hosted"constant`

                  The type of the object. Always `openai_hosted`.

                  - `OPENAI_HOSTED("openai_hosted")`

              - `SelfHosted`

                - `List<String> capabilityDirectories`

                  Directories that expose capabilities to the agent.

                  `minItems: 0`, `maxItems: 2000`

                - `Optional<String> environmentId`

                  An existing registration, or null to create a session-owned environment.

                  `minLength: 0`

                - `JsonValue; type "self_hosted"constant`

                  The type of the object. Always `self_hosted`.

                  - `SELF_HOSTED("self_hosted")`

                - `String workspaceDirectory`

                  The absolute project directory in the environment.

                  `minLength: 0`

            - `List<Input> input`

              Initial input delivered to each new session.

              `minItems: 0`, `maxItems: 2000`

              - `List<InputContent> content`

                The content of the message.

                `minItems: 0`, `maxItems: 2000`

                - `InputText`

                  - `String text`

                    The text supplied to the agent.

                    `minLength: 0`

                  - `JsonValue; type "input_text"constant`

                    The type of the object. Always `input_text`.

                    - `INPUT_TEXT("input_text")`

                - `InputImage`

                  - `String imageUrl`

                    The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                    `minLength: 0`

                  - `JsonValue; type "input_image"constant`

                    The type of the object. Always `input_image`.

                    - `INPUT_IMAGE("input_image")`

              - `JsonValue; role "user"constant`

                The role of the message author. Always `user`.

                - `USER("user")`

              - `JsonValue; type "message"constant`

                The type of the input item. Always `message`.

                - `MESSAGE("message")`

            - `Metadata metadata`

              Metadata attached to each new session.

            - `JsonValue; type "new_session"constant`

              The type of the object. Always `new_session`.

              - `NEW_SESSION("new_session")`

            - `List<String> vaultIds`

              Vaults made available to each new session.

              `minItems: 0`, `maxItems: 2000`

          - `ExistingSession`

            - `String instructions`

              Saved instructions delivered as an automation notification.

              `minLength: 0`

            - `String sessionId`

              The session receiving each invocation.

              `minLength: 0`

            - `JsonValue; type "existing_session"constant`

              The type of the object. Always `existing_session`.

              - `EXISTING_SESSION("existing_session")`

        - `String timezone`

          The timezone used to interpret the expression.

          `minLength: 0`

        - `JsonValue; type "periodic"constant`

          The type of the object. Always `periodic`.

          - `PERIODIC("periodic")`

      - `class OneTimeAutomation:`

        Fields shared by periodic and one-time automations.

        - `String id`

          The automation ID.

          `minLength: 0`

        - `long createdAt`

          The creation time as a Unix timestamp in seconds.

          `format: int64`

        - `AutomationCreatedBy createdBy`

          Service-recorded provenance; callers cannot supply this field.

        - `Metadata metadata`

          Custom string key-value pairs attached to the automation.

        - `String name`

          The automation's display name.

          `minLength: 0`

        - `JsonValue; object_ "agent.automation"constant`

          Always `agent.automation`.

          - `AGENT_AUTOMATION("agent.automation")`

        - `long runAt`

          The Unix timestamp, in seconds, of the scheduled occurrence.

          `format: int64`

        - `Status status`

          Completion means the schedule has finished, not the agent's work.

          - `ACTIVE("active")`

          - `PAUSED("paused")`

          - `COMPLETED("completed")`

        - `AutomationTarget target`

          The session configuration or existing session receiving invocations.

        - `JsonValue; type "once"constant`

          The type of the object. Always `once`.

          - `ONCE("once")`

    - `JsonValue; type "automation"constant`

      The type of the object. Always `automation`.

      - `AUTOMATION("automation")`

### Automation Invocation Source Automation

- `class AutomationInvocationSourceAutomation:`

  - `Automation automation`

    The automation snapshot for this occurrence, excluding confidential values.

    - `class PeriodicAutomation:`

      Fields shared by periodic and one-time automations.

      - `String id`

        The automation ID.

        `minLength: 0`

      - `long createdAt`

        The creation time as a Unix timestamp in seconds.

        `format: int64`

      - `AutomationCreatedBy createdBy`

        Service-recorded provenance; callers cannot supply this field.

        - `JsonValue;`

          - `JsonValue; type "developer"constant`

            The type of the object. Always `developer`.

            - `DEVELOPER("developer")`

        - `Agent`

          - `String sessionId`

            The creator session, which is also the automation's target.

            `minLength: 0`

          - `String toolCallId`

            The tool call that created the automation.

            `minLength: 0`

          - `JsonValue; type "agent"constant`

            The type of the object. Always `agent`.

            - `AGENT("agent")`

      - `String expression`

        The cron expression determining scheduled occurrences.

        `minLength: 0`

      - `Metadata metadata`

        Custom string key-value pairs attached to the automation.

      - `String name`

        The automation's display name.

        `minLength: 0`

      - `JsonValue; object_ "agent.automation"constant`

        Always `agent.automation`.

        - `AGENT_AUTOMATION("agent.automation")`

      - `Status status`

        Whether scheduled delivery is active or paused.

        - `ACTIVE("active")`

        - `PAUSED("paused")`

      - `AutomationTarget target`

        The session configuration or existing session receiving invocations.

        - `NewSession`

          - `Optional<AutomationAgentConfig> agent`

            The inline agent configuration, or null when agent_id is configured.

            - `Optional<String> instructions`

              Custom instructions, or null when absent.

              `minLength: 0`

            - `String model`

              The requested model name.

              `minLength: 0`

            - `MultiAgentConfig multiAgent`

              The configuration for creating and coordinating subagents.

              - `boolean enabled`

                Whether subagent tools are enabled. Defaults to false.

              - `Optional<Long> maxConcurrentSubagents`

                Maximum number of subagents that may run concurrently, or null when disabled. Defaults to 6 when enabled.

                `format: int64`, `minimum: 1`, `maximum: 4294967295`

            - `AgentReasoning reasoning`

              The configured reasoning policy.

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

              The configured service-tier policy.

              - `AUTO("auto")`

              - `DEFAULT("default")`

              - `FLEX("flex")`

              - `PRIORITY("priority")`

              - `FAST("fast")`

              - `ULTRAFAST("ultrafast")`

            - `AgentText text`

              The configured output format and verbosity.

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

              Configured tools, excluding confidential credentials.

              `minItems: 0`, `maxItems: 2000`

              - `Function`

                - `boolean deferLoading`

                  Whether the function is deferred and discovered through tool search.

                - `String description`

                  A description of what the function does.

                  `minLength: 0`

                - `String name`

                  The name of the function.

                  `minLength: 0`

                - `Parameters parameters`

                  A JSON Schema object describing the function's arguments.

                - `JsonValue; type "function"constant`

                  The type of the object. Always `function`.

                  - `FUNCTION("function")`

                - `Optional<Boolean> async`

                  Whether the agent continues without waiting for the function result.

              - `ProgrammaticToolCalling`

                - `boolean enabled`

                  Whether tools can be called from model-generated code.

                - `JsonValue; type "programmatic_tool_calling"constant`

                  The type of the object. Always `programmatic_tool_calling`.

                  - `PROGRAMMATIC_TOOL_CALLING("programmatic_tool_calling")`

              - `Mcp`

                - `Optional<List<String>> allowedTools`

                  The MCP tools the agent may call.

                  `minItems: 0`, `maxItems: 2000`

                - `ConnectionOrigin connectionOrigin`

                  Where outbound MCP HTTP connections originate.

                  - `SERVICE("service")`

                  - `ENVIRONMENT("environment")`

                - `Optional<String> credentialId`

                  The attached vault credential selected for this MCP server, if any. Optional when exactly one attached credential matches the server URL.

                  `minLength: 0`

                - `RequestMetadata requestMetadata`

                  Metadata included with requests to this MCP server.

                - `boolean required`

                  Whether this MCP server must initialize before the first turn.

                - `String serverLabel`

                  A label used to identify the MCP server in tool calls.

                  `minLength: 0`

                - `McpTransport transport`

                  The transport used to connect to the MCP server.

                  - `Http`

                    - `String serverUrl`

                      The URL of the MCP server.

                      `minLength: 0`

                    - `JsonValue; type "http"constant`

                      The type of the object. Always `http`.

                      - `HTTP("http")`

                  - `Stdio`

                    - `List<String> args`

                      Arguments passed to the MCP server command.

                      `minItems: 0`, `maxItems: 2000`

                    - `String command`

                      The command used to start the MCP server.

                      `minLength: 0`

                    - `String cwd`

                      The working directory used to start the MCP server.

                      `minLength: 0`

                    - `List<String> envVars`

                      Environment variable names inherited from the execution environment.

                      `minItems: 0`, `maxItems: 2000`

                    - `JsonValue; type "stdio"constant`

                      The type of the object. Always `stdio`.

                      - `STDIO("stdio")`

                - `JsonValue; type "mcp"constant`

                  The type of the object. Always `mcp`.

                  - `MCP("mcp")`

              - `WebSearch`

                - `Optional<List<String>> allowedDomains`

                  Allowed search domains, or `null` when the search is unrestricted.

                  `minItems: 0`, `maxItems: 2000`

                - `ContextSize contextSize`

                  The amount of search context made available to the model. Defaults to `medium`.

                  - `LOW("low")`

                  - `MEDIUM("medium")`

                  - `HIGH("high")`

                - `Optional<Location> location`

                  Approximate location used to localize search results, if provided.

                  - `Optional<String> city`

                    The city name.

                    `minLength: 0`

                  - `Optional<String> country`

                    The two-letter ISO country code, such as `US`.

                    `minLength: 0`

                  - `Optional<String> region`

                    The region or state name.

                    `minLength: 0`

                  - `Optional<String> timezone`

                    The IANA timezone, such as `America/Los_Angeles`.

                    `minLength: 0`

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

              - `JsonValue;`

                - `JsonValue; type "automations"constant`

                  The type of the object. Always `automations`.

                  - `AUTOMATIONS("automations")`

            - `Optional<Compaction> compaction`

              The effective context compaction settings.

              - `boolean async`

                Whether context is compacted in the background. Defaults to true.

            - `Optional<Experimental> experimental`

              The effective experimental settings for the agent.

              - `boolean timeAwareness`

                Whether the model receives periodic current-time reminders.

          - `Optional<String> agentId`

            The saved agent reference, or null when an inline agent is configured.

            `minLength: 0`

          - `AutomationEnvironment environment`

            Configuration or references used to select the execution environment.

            - `JsonValue;`

              - `JsonValue; type "none"constant`

                The type of the object. Always `none`.

                - `NONE("none")`

            - `OpenAIHosted`

              - `Optional<List<String>> capabilityDirectories`

                Directory overrides, or null to inherit the template or creation default.

                `minItems: 0`, `maxItems: 2000`

              - `Optional<ContainerSize> containerSize`

                The configured container size, or null to use the creation default.

                - `SMALL("small")`

                - `MEDIUM("medium")`

                - `LARGE("large")`

              - `Optional<Desktop> desktop`

                Desktop overrides, or null to inherit the template or creation default.

                - `boolean enabled`

                  Whether the environment provisions a desktop and browser proxy.

              - `Optional<String> environmentId`

                An existing environment reference, or null when provisioning a new environment.

                `minLength: 0`

              - `Optional<String> environmentTemplateId`

                A template reference, or null when no template is selected.

                `minLength: 0`

              - `Optional<List<File>> files`

                File overrides, excluding contents, or null to inherit.

                `minItems: 0`, `maxItems: 2000`

                - `class FileId:`

                  A project-scoped Files API reference resolved separately for each session.

                  - `String fileId`

                    The ID of the uploaded file.

                    `minLength: 0`

                  - `String path`

                    The file's absolute path inside the environment.

                    `minLength: 0`

                  - `JsonValue; type "file_id"constant`

                    The type of the object. Always `file_id`.

                    - `FILE_ID("file_id")`

                - `class Inline:`

                  Metadata for confidential inline file contents.

                  - `String path`

                    The file's absolute path inside the environment.

                    `minLength: 0`

                  - `long sizeBytes`

                    The decoded size of the inline file in bytes.

                    `format: int64`, `minimum: 0`

                  - `JsonValue; type "inline"constant`

                    The type of the object. Always `inline`.

                    - `INLINE("inline")`

              - `Optional<Network> network`

                Network overrides, or null to inherit the template or creation default.

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

                  `minItems: 0`, `maxItems: 2000`

              - `Optional<Packages> packages`

                Package overrides, or null to inherit the template or creation default.

                - `List<String> npm`

                  npm packages installed globally in the environment.

                  `minItems: 0`, `maxItems: 16384`

                - `List<String> python`

                  Python packages installed in the environment.

                  `minItems: 0`, `maxItems: 16384`

                - `List<String> system`

                  System packages installed in the environment.

                  `minItems: 0`, `maxItems: 16384`

              - `Optional<List<HostedPlugin>> plugins`

                Plugin overrides, excluding archive contents, or null to inherit.

                `minItems: 0`, `maxItems: 2000`

                - `String description`

                  The installed plugin description.

                  `minLength: 0`

                - `String name`

                  The installed plugin name.

                  `minLength: 0`

                - `JsonValue; type "inline"constant`

                  The type of the object. Always `inline`.

                  - `INLINE("inline")`

              - `Optional<List<Skill>> skills`

                Skill overrides, excluding archive contents, or null to inherit.

                `minItems: 0`, `maxItems: 2000`

                - `class SkillReference:`

                  A skill resolved afresh from the Skills API whenever a session starts.

                  - `String skillId`

                    The referenced skill ID.

                    `minLength: 0`

                  - `JsonValue; type "skill_reference"constant`

                    The type of the object. Always `skill_reference`.

                    - `SKILL_REFERENCE("skill_reference")`

                  - `Optional<String> version`

                    The requested version selector, including `latest`.

                    `minLength: 0`

                - `class Inline:`

                  Safe metadata for an inline skill archive.

                  - `String description`

                    The skill description declared in `SKILL.md`.

                    `minLength: 0`

                  - `String name`

                    The skill name declared in `SKILL.md`.

                    `minLength: 0`

                  - `JsonValue; type "inline"constant`

                    The type of the object. Always `inline`.

                    - `INLINE("inline")`

              - `JsonValue; type "openai_hosted"constant`

                The type of the object. Always `openai_hosted`.

                - `OPENAI_HOSTED("openai_hosted")`

            - `SelfHosted`

              - `List<String> capabilityDirectories`

                Directories that expose capabilities to the agent.

                `minItems: 0`, `maxItems: 2000`

              - `Optional<String> environmentId`

                An existing registration, or null to create a session-owned environment.

                `minLength: 0`

              - `JsonValue; type "self_hosted"constant`

                The type of the object. Always `self_hosted`.

                - `SELF_HOSTED("self_hosted")`

              - `String workspaceDirectory`

                The absolute project directory in the environment.

                `minLength: 0`

          - `List<Input> input`

            Initial input delivered to each new session.

            `minItems: 0`, `maxItems: 2000`

            - `List<InputContent> content`

              The content of the message.

              `minItems: 0`, `maxItems: 2000`

              - `InputText`

                - `String text`

                  The text supplied to the agent.

                  `minLength: 0`

                - `JsonValue; type "input_text"constant`

                  The type of the object. Always `input_text`.

                  - `INPUT_TEXT("input_text")`

              - `InputImage`

                - `String imageUrl`

                  The URL of the image supplied to the agent, which may be a base64-encoded data URL.

                  `minLength: 0`

                - `JsonValue; type "input_image"constant`

                  The type of the object. Always `input_image`.

                  - `INPUT_IMAGE("input_image")`

            - `JsonValue; role "user"constant`

              The role of the message author. Always `user`.

              - `USER("user")`

            - `JsonValue; type "message"constant`

              The type of the input item. Always `message`.

              - `MESSAGE("message")`

          - `Metadata metadata`

            Metadata attached to each new session.

          - `JsonValue; type "new_session"constant`

            The type of the object. Always `new_session`.

            - `NEW_SESSION("new_session")`

          - `List<String> vaultIds`

            Vaults made available to each new session.

            `minItems: 0`, `maxItems: 2000`

        - `ExistingSession`

          - `String instructions`

            Saved instructions delivered as an automation notification.

            `minLength: 0`

          - `String sessionId`

            The session receiving each invocation.

            `minLength: 0`

          - `JsonValue; type "existing_session"constant`

            The type of the object. Always `existing_session`.

            - `EXISTING_SESSION("existing_session")`

      - `String timezone`

        The timezone used to interpret the expression.

        `minLength: 0`

      - `JsonValue; type "periodic"constant`

        The type of the object. Always `periodic`.

        - `PERIODIC("periodic")`

    - `class OneTimeAutomation:`

      Fields shared by periodic and one-time automations.

      - `String id`

        The automation ID.

        `minLength: 0`

      - `long createdAt`

        The creation time as a Unix timestamp in seconds.

        `format: int64`

      - `AutomationCreatedBy createdBy`

        Service-recorded provenance; callers cannot supply this field.

      - `Metadata metadata`

        Custom string key-value pairs attached to the automation.

      - `String name`

        The automation's display name.

        `minLength: 0`

      - `JsonValue; object_ "agent.automation"constant`

        Always `agent.automation`.

        - `AGENT_AUTOMATION("agent.automation")`

      - `long runAt`

        The Unix timestamp, in seconds, of the scheduled occurrence.

        `format: int64`

      - `Status status`

        Completion means the schedule has finished, not the agent's work.

        - `ACTIVE("active")`

        - `PAUSED("paused")`

        - `COMPLETED("completed")`

      - `AutomationTarget target`

        The session configuration or existing session receiving invocations.

      - `JsonValue; type "once"constant`

        The type of the object. Always `once`.

        - `ONCE("once")`

  - `JsonValue; type "automation"constant`

    The type of the object. Always `automation`.

    - `AUTOMATION("automation")`
