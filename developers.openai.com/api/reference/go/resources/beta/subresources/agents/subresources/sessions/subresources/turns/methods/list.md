<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/turns/methods/list/ -->

## List agent session turns

`client.Beta.Agents.Sessions.Turns.List(ctx, sessionID, query) (*CursorPage[Turn], error)`

**get** `/agents/sessions/{session_id}/turns`

Lists turns by creation time and turn ID. The after cursor is exclusive in the selected order. See [session turns](/api/docs/guides/agents-api/sessions/manage#inspect-session-turns).

- `sessionID string`

- `query BetaAgentSessionTurnListParams`

  - `After param.Field[string]`

    Return resources after this resource ID in the selected order.

  - `Limit param.Field[int64]`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Order param.Field[BetaAgentSessionTurnListParamsOrder]`

    The order in which resources are returned. Defaults to `desc`.

    - `const BetaAgentSessionTurnListParamsOrderAsc BetaAgentSessionTurnListParamsOrder = "asc"`

      Returns resources in ascending order.

    - `const BetaAgentSessionTurnListParamsOrderDesc BetaAgentSessionTurnListParamsOrder = "desc"`

      Returns resources in descending order.

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

```go
package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.Beta.Agents.Sessions.Turns.List(
    context.TODO(),
    "session_id",
    openai.BetaAgentSessionTurnListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "data": [
      "agent_id": "agent_id",
      "completed_at": 0,
      "error": {
        "code": "context_length_exceeded",
        "message": "message"
      "object": "agent.session.turn",
      "session_id": "session_id",
      "started_at": 0,
      "status": "queued",
      "subagent_id": "subagent_id",
      "usage": {
        "input_tokens": 0,
        "input_tokens_details": {
          "cached_tokens": 0
        "output_tokens": 0,
        "output_tokens_details": {
          "reasoning_tokens": 0
        "total_tokens": 0
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
