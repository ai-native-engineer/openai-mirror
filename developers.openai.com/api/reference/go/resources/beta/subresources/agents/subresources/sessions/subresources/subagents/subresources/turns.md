<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/turns/ -->

# Turns

## List subagent turns

`client.Beta.Agents.Sessions.Subagents.Turns.List(ctx, sessionID, subagentID, query) (*CursorPage[Turn], error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `query BetaAgentSessionSubagentTurnListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentTurnListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentTurnListParamsOrderAsc BetaAgentSessionSubagentTurnListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentTurnListParamsOrderDesc BetaAgentSessionSubagentTurnListParamsOrder = "desc"`

      Returns resources in descending order.

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

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
  page, err := client.Beta.Agents.Sessions.Subagents.Turns.List(
    context.TODO(),
    "session_id",
    "subagent_id",
    openai.BetaAgentSessionSubagentTurnListParams{

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

`client.Beta.Agents.Sessions.Subagents.Turns.Get(ctx, sessionID, subagentID, turnID) (*Turn, error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `turnID string`

### Returns

- `type Turn struct{…}`

  The canonical public representation of a session turn.

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
  turn, err := client.Beta.Agents.Sessions.Subagents.Turns.Get(
    context.TODO(),
    "session_id",
    "subagent_id",
    "turn_id",
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", turn.ID)
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

`client.Beta.Agents.Sessions.Subagents.Turns.Items.List(ctx, sessionID, subagentID, turnID, query) (*CursorPage[AgentSessionItemUnion], error)`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `sessionID string`

- `subagentID string`

- `turnID string`

- `query BetaAgentSessionSubagentTurnItemListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionSubagentTurnItemListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionSubagentTurnItemListParamsOrderAsc BetaAgentSessionSubagentTurnItemListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionSubagentTurnItemListParamsOrderDesc BetaAgentSessionSubagentTurnItemListParamsOrder = "desc"`

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
  page, err := client.Beta.Agents.Sessions.Subagents.Turns.Items.List(
    context.TODO(),
    "session_id",
    "subagent_id",
    "turn_id",
    openai.BetaAgentSessionSubagentTurnItemListParams{

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
