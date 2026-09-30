<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/events/ -->

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
