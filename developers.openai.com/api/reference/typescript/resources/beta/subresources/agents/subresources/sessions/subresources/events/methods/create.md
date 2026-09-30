<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

## Create agent session input events

`client.beta.agents.sessions.events.create(stringsessionID, EventCreateParamsparams, RequestOptionsoptions?): void`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

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

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

await client.beta.agents.sessions.events.create('session_id', {
  events: [
      request_id: 'request_id',
      response: {
        action: 'submit',
        fields: [{ field_id: 'field_id', value: 'value' }],
        type: 'browser_authentication',
      type: 'agent.session.input.computer_use_approval_request_result',
});
