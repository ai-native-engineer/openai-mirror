<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

## Create agent session input events

`beta.agents.sessions.events.create(session_id, **kwargs) -> void`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

- `session_id: String`

- `events: Array[AgentSessionInputParam]`

  The input events to submit to the session.

  - `class AgentSessionInputComputerUseApprovalRequestResult`

    Responds to a pending Computer Use approval request.

    - `request_id: String`

      The registered request ID from the required action.

    - `response: AgentBrowserAuthenticationSubmitParam | AgentBrowserAuthenticationCancelParam | AgentBrowserOriginAccessParam`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam`

        - `action: :submit`

          - `:submit`

        - `fields: Array[Field{ field_id, value}]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: String`

            The field ID from the required action.

          - `value: String`

            The value to enter into the registered control.

        - `type: :browser_authentication`

          - `:browser_authentication`

        - `selected_option: String`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class AgentBrowserOriginAccessParam`

        - `decision: :approve | :deny | :cancel`

          Whether to allow, deny, or cancel the requested origin access.

          - `:approve`

            Allow the browser to access this origin.

          - `:deny`

            Deny access to this origin.

          - `:cancel`

            Dismiss this request without approving access.

        - `type: :browser_origin_access`

          - `:browser_origin_access`

    - `type: :"agent.session.input.computer_use_approval_request_result"`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `:"agent.session.input.computer_use_approval_request_result"`

  - `class AgentSessionInputMessage`

    Adds one or more user messages and starts a turn.

    - `input: Array[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: Array[InputContentParam]`

        The content of the message.

        - `class InputText`

          Text input to the model.

          - `text: String`

            The text sent to the model.

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input to the model.

          - `image_url: String`

            The URL of the image sent to the model.

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

      - `role: :user`

        The role of the message author. Always `user`.

        - `:user`

      - `type: :message`

        The type of the input item. Always `message`.

        - `:message`

    - `type: :"agent.session.input.message"`

      The type of the object. Always `agent.session.input.message`.

      - `:"agent.session.input.message"`

  - `class AgentSessionInputCancel`

    Cancels the session's active turn.

    - `type: :"agent.session.input.cancel"`

      The type of the object. Always `agent.session.input.cancel`.

      - `:"agent.session.input.cancel"`

  - `class AgentSessionInputToolResult`

    Submits the result of a function call.

    - `call_id: String`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: String`

      The ID of the turn that requested the function call.

    - `type: :"agent.session.input.tool_result"`

      The type of the object. Always `agent.session.input.tool_result`.

      - `:"agent.session.input.tool_result"`

    - `error: String`

      The error message when the call failed.

    - `output: AgentFunctionCallOutputParam`

      The function result when the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContentParam]`

        - `class InputText`

          Text input to the model.

        - `class InputImage`

          Image input to the model.

- `idempotency_key: String`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

result = openai.beta.agents.sessions.events.create(
  "session_id",
  events: [
      request_id: "request_id",
      response: {action: "submit", fields: [{field_id: "field_id", value: "value"}], type: :browser_authentication},
      type: :"agent.session.input.computer_use_approval_request_result"
  ]

puts(result)
