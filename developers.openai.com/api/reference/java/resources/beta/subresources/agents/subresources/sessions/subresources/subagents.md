<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/ -->

# Subagents

## List session subagents

`SubagentListPage beta().agents().sessions().subagents().list(SubagentListParamsparams = SubagentListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents`

Lists subagents in a session, including nested and closed subagents. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `SubagentListParams params`

  - `Optional<String> sessionId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.SubagentListPage;
import com.openai.models.beta.agents.sessions.subagents.SubagentListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentListPage page = client.beta().agents().sessions().subagents().list("session_id");
    }
}
```

#### Response

```json
{
  "data": [
    {
      "id": "id",
      "closed_at": 0,
      "instructions": [
        {
          "text": "text",
          "type": "output_text"
        }
      ],
      "name": "name",
      "object": "agent.session.subagent",
      "opened_at": 0,
      "parent_agent_id": "parent_agent_id",
      "session_id": "session_id",
      "status": "active"
    }
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
}
```

## Retrieve a session subagent

`Subagent beta().agents().sessions().subagents().retrieve(SubagentRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}`

Retrieves a subagent belonging to this session. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `SubagentRetrieveParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

### Returns

- `class Subagent:`

  A subagent created within a session.

  - `String id`

    The ID of the subagent.

  - `Optional<Long> closedAt`

    The Unix timestamp, in seconds, when the subagent was closed. Null while active, including after resume.

  - `Optional<List<AgentContent>> instructions`

    Initial task content, or null when unavailable. Text may contain placeholders for images or audio when only a preview is available.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.Subagent;
import com.openai.models.beta.agents.sessions.subagents.SubagentRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        SubagentRetrieveParams params = SubagentRetrieveParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        Subagent subagent = client.beta().agents().sessions().subagents().retrieve(params);
    }
}
```

#### Response

```json
{
  "id": "id",
  "closed_at": 0,
  "instructions": [
    {
      "text": "text",
      "type": "output_text"
    }
  ],
  "name": "name",
  "object": "agent.session.subagent",
  "opened_at": 0,
  "parent_agent_id": "parent_agent_id",
  "session_id": "session_id",
  "status": "active"
}
```

# Items

## List subagent items

`ItemListPage beta().agents().sessions().subagents().items().list(ItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `ItemListParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.items.ItemListPage;
import com.openai.models.beta.agents.sessions.subagents.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListParams params = ItemListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        ItemListPage page = client.beta().agents().sessions().subagents().items().list(params);
    }
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

# Turns

## List subagent turns

`TurnListPage beta().agents().sessions().subagents().turns().list(TurnListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns`

Lists all turns of this subagent, including turns after a resume. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `TurnListParams params`

  - `String sessionId`

  - `Optional<String> subagentId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnListPage;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnListParams params = TurnListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .build();
        TurnListPage page = client.beta().agents().sessions().subagents().turns().list(params);
    }
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

`Turn beta().agents().sessions().subagents().turns().retrieve(TurnRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}`

Retrieves a turn belonging to this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `TurnRetrieveParams params`

  - `String sessionId`

  - `String subagentId`

  - `Optional<String> turnId`

### Returns

- `class Turn:`

  The canonical public representation of a session turn.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.TurnRetrieveParams;
import com.openai.models.beta.agents.sessions.turns.Turn;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        TurnRetrieveParams params = TurnRetrieveParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .turnId("turn_id")
            .build();
        Turn turn = client.beta().agents().sessions().subagents().turns().retrieve(params);
    }
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

`ItemListPage beta().agents().sessions().subagents().turns().items().list(ItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/turns/{turn_id}/items`

Lists items belonging to one turn of this subagent. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `ItemListParams params`

  - `String sessionId`

  - `String subagentId`

  - `Optional<String> turnId`

  - `Optional<String> after`

    Return resources after this resource ID in the selected order.

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

  - `Optional<Order> order`

    The order in which resources are returned. Defaults to `desc`.

    - `ASC("asc")`

      Returns resources in ascending order.

    - `DESC("desc")`

      Returns resources in descending order.

### Returns

- `class AgentSessionItem: A class that can be one of several variants.union`

  An item associated with a session turn.

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

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.subagents.turns.items.ItemListPage;
import com.openai.models.beta.agents.sessions.subagents.turns.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListParams params = ItemListParams.builder()
            .sessionId("session_id")
            .subagentId("subagent_id")
            .turnId("turn_id")
            .build();
        ItemListPage page = client.beta().agents().sessions().subagents().turns().items().list(params);
    }
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
