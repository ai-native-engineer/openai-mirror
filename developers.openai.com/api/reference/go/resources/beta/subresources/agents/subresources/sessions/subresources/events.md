<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/events/ -->

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
