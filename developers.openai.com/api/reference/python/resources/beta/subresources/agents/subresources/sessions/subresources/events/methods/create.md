<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

## Create agent session input events

`beta.agents.sessions.events.create(strsession_id, EventCreateParams**kwargs)`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

- `session_id: str`

- `events: Iterable[AgentSessionInputParam]`

  The input events to submit to the session.

  - `class SessionInputParamAgentSessionInputComputerUseApprovalRequestResult: …`

    Responds to a pending Computer Use approval request.

    - `request_id: str`

      The registered request ID from the required action.

    - `response: SessionInputParamAgentSessionInputComputerUseApprovalRequestResultResponse`

      The response for this request type.

      - `class AgentBrowserAuthenticationSubmitParam: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `fields: List[Field]`

          Values for up to six active fields in the required action. The submitted field-value mapping and selected option must fit within 120 KiB of JSON.

          - `field_id: str`

            The field ID from the required action.

          - `value: str`

            The value to enter into the registered control.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

        - `selected_option: Optional[str]`

          The chosen method. Required when the required action contains options.

      - `class AgentBrowserAuthenticationCancelParam: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class AgentBrowserOriginAccessParam: …`

        - `decision: Literal["approve", "deny", "cancel"]`

          Whether to allow, deny, or cancel the requested origin access.

          - `"approve"`

            Allow the browser to access this origin.

          - `"deny"`

            Deny access to this origin.

          - `"cancel"`

            Dismiss this request without approving access.

        - `type: Literal["browser_origin_access"]`

          - `"browser_origin_access"`

    - `type: Literal["agent.session.input.computer_use_approval_request_result"]`

      The type of the object. Always `agent.session.input.computer_use_approval_request_result`.

      - `"agent.session.input.computer_use_approval_request_result"`

  - `class SessionInputParamAgentSessionInputMessage: …`

    Adds one or more user messages and starts a turn.

    - `input: List[AgentSessionInputMessageParam]`

      The user messages to add to the session.

      - `content: List[InputContentParam]`

        The content of the message.

        - `class InputContentParamInputText: …`

          Text input to the model.

          - `text: str`

            The text sent to the model.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentParamInputImage: …`

          Image input to the model.

          - `image_url: str`

            The URL of the image sent to the model.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

      - `role: Literal["user"]`

        The role of the message author. Always `user`.

        - `"user"`

      - `type: Optional[Literal["message"]]`

        The type of the input item. Always `message`.

        - `"message"`

    - `type: Literal["agent.session.input.message"]`

      The type of the object. Always `agent.session.input.message`.

      - `"agent.session.input.message"`

  - `class SessionInputParamAgentSessionInputCancel: …`

    Cancels the session's active turn.

    - `type: Literal["agent.session.input.cancel"]`

      The type of the object. Always `agent.session.input.cancel`.

      - `"agent.session.input.cancel"`

  - `class SessionInputParamAgentSessionInputToolResult: …`

    Submits the result of a function call.

    - `call_id: str`

      The ID of the function call.

    - `success: bool`

      Whether the function call succeeded.

    - `turn_id: str`

      The ID of the turn that requested the function call.

    - `type: Literal["agent.session.input.tool_result"]`

      The type of the object. Always `agent.session.input.tool_result`.

      - `"agent.session.input.tool_result"`

    - `error: Optional[str]`

      The error message when the call failed.

    - `output: Optional[AgentFunctionCallOutputParam]`

      The function result when the call succeeded.

      - `str`

      - `List[InputContentParam]`

        - `class InputContentParamInputText: …`

          Text input to the model.

        - `class InputContentParamInputImage: …`

          Image input to the model.

- `idempotency_key: Optional[str]`

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
client.beta.agents.sessions.events.create(
    session_id="session_id",
    events=[{
        "request_id": "request_id",
        "response": {
            "action": "submit",
            "fields": [{
                "field_id": "field_id",
                "value": "value",
            }],
            "type": "browser_authentication",
        "type": "agent.session.input.computer_use_approval_request_result",
    }],
