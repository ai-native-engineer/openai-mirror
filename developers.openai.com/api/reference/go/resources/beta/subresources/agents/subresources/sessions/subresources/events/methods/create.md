<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

## Create agent session input events

`client.Beta.Agents.Sessions.Events.New(ctx, sessionID, params) error`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

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

```go
package main

import (
  "context"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
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
      }},
  if err != nil {
    panic(err.Error())
