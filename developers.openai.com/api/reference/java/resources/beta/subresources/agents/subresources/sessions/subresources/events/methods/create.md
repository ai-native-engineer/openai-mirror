<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/events/methods/create/ -->

## Create agent session input events

`beta().agents().sessions().events().create(EventCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**post** `/agents/sessions/{session_id}/events`

Submits message, cancellation, tool-result, or computer-use approval-response events to a managed agent session. Cancellation can recover a still-open turn whose backend execution has ended by marking it cancelled and abandoning unpublished outputs. Saved results, published files, and existing terminal outcomes are preserved. HTTP 202 confirms acceptance, not durable completion. See [session events](/api/docs/guides/agents-api/sessions/events).

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
