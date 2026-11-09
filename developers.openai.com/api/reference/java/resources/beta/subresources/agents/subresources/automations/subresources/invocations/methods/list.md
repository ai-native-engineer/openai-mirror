<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/automations/subresources/invocations/methods/list/ -->

## List automation invocations

`InvocationListPage beta().agents().automations().invocations().list(InvocationListParamsparams = InvocationListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/automations/{automation_id}/invocations`

Lists delivery records for a project-owned automation.

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

  "data": [
      "automation_id": "automation_id",
      "error": {
        "code": "code",
        "message": "message"
      "object": "agent.automation.invocation",
      "scheduled_at": 0,
      "session_id": "session_id",
      "skip_reason": "pending_delivery",
      "source": {
        "type": "manual"
      "status": "queued"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
