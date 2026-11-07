<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/agents/subresources/sessions/subresources/turns/subresources/items/ -->

# Items

## List agent session turn items

`ItemListPage beta().agents().sessions().turns().items().list(ItemListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())`

**get** `/agents/sessions/{session_id}/turns/{turn_id}/items`

Lists items belonging to one root-agent turn, including its interactions with subagents. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `ItemListParams params`

  - `String sessionId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> turnId`

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<String> after`

    Return items after this cursor in the selected order. Pass the previous response's last_id, which can differ from the last item's ID.

    `minLength: 0`, `maxLength: 1048576`

  - `Optional<Long> limit`

    The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

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

      `minLength: 0`

    - `List<AgentSessionMessageContent> content`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      `minItems: 0`, `maxItems: 2000`

      - `InputText`

        - `String text`

          The text supplied by the user.

          `minLength: 0`

        - `JsonValue; type "input_text"constant`

          The type of the object. Always `input_text`.

          - `INPUT_TEXT("input_text")`

      - `InputImage`

        - `String imageUrl`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

          `minLength: 0`

        - `JsonValue; type "input_image"constant`

          The type of the object. Always `input_image`.

          - `INPUT_IMAGE("input_image")`

      - `OutputText`

        - `String text`

          The text produced by the assistant.

          `minLength: 0`

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

      `minLength: 0`

    - `JsonValue; type "message"constant`

      The item type. Always `message`.

      - `MESSAGE("message")`

  - `class AgentReasoningItem:`

    A reasoning item produced by the agent.

    - `String id`

      The ID of the reasoning item.

      `minLength: 0`

    - `Optional<AgentOutputItemStatus> status`

      The status of the reasoning item.

    - `List<SummaryText> summary`

      The reasoning summaries produced by the agent.

      `minItems: 0`, `maxItems: 2000`

      - `String text`

        The reasoning summary text.

        `minLength: 0`

      - `JsonValue; type "summary_text"constant`

        The content type. Always `summary_text`.

        - `SUMMARY_TEXT("summary_text")`

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "reasoning"constant`

      The item type. Always `reasoning`.

      - `REASONING("reasoning")`

  - `class AgentFunctionCallItem:`

    A function call produced by the agent.

    - `String id`

      The ID of the function call item.

      `minLength: 0`

    - `JsonValue arguments`

      The arguments to pass to the function.

    - `String callId`

      The ID used to submit the function result.

      `minLength: 0`

    - `String name`

      The name of the function to call.

      `minLength: 0`

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

      `minLength: 0`

    - `JsonValue; type "function_call"constant`

      The item type. Always `function_call`.

      - `FUNCTION_CALL("function_call")`

  - `FunctionCallOutput`

    - `String id`

      The ID of the function call output item.

      `minLength: 0`

    - `String callId`

      The ID of the function call that produced this output.

      `minLength: 0`

    - `Optional<String> error`

      The error message, if the call failed.

      `minLength: 0`

    - `Optional<AgentFunctionCallOutput> output`

      The function result, if the call succeeded.

      - `String`

      - `List<InputContent>`

        - `InputText`

          - `String text`

            The text supplied to the agent.

            `minLength: 0`

          - `JsonValue; type "input_text"constant`

            The type of the object. Always `input_text`.

            - `INPUT_TEXT("input_text")`

        - `InputImage`

          - `String imageUrl`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `JsonValue; type "input_image"constant`

            The type of the object. Always `input_image`.

            - `INPUT_IMAGE("input_image")`

    - `AgentFunctionCallStatus status`

      The status of the function call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "function_call_output"constant`

      The item type. Always `function_call_output`.

      - `FUNCTION_CALL_OUTPUT("function_call_output")`

  - `AgentMessage`

    - `String id`

      The ID of the message.

      `minLength: 0`

    - `List<AgentContent> content`

      The content exchanged between the agents.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText:`

        A text content part produced by the agent.

        - `String text`

          The text produced by the agent.

          `minLength: 0`

        - `JsonValue; type "output_text"constant`

          The content type. Always `output_text`.

          - `OUTPUT_TEXT("output_text")`

      - `EncryptedContent`

        - `String encryptedContent`

          The encrypted content payload.

          `minLength: 0`

        - `JsonValue; type "encrypted_content"constant`

          The content type. Always `encrypted_content`.

          - `ENCRYPTED_CONTENT("encrypted_content")`

    - `String recipientAgentId`

      The ID or name of the receiving agent.

      `minLength: 0`

    - `String senderAgentId`

      The ID or name of the sending agent.

      `minLength: 0`

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "agent_message"constant`

      The item type. Always `agent_message`.

      - `AGENT_MESSAGE("agent_message")`

  - `class AgentMcpCallItem:`

    A call to a tool on an MCP server.

    - `String id`

      The ID of the MCP call item.

      `minLength: 0`

    - `JsonValue arguments`

      The arguments passed to the MCP tool.

    - `JsonValue error`

      The error returned by the MCP tool, if any.

    - `String name`

      The name of the MCP tool.

      `minLength: 0`

    - `JsonValue output`

      The output returned by the MCP tool, if any.

    - `String serverLabel`

      The label of the MCP server.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the MCP tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "mcp_call"constant`

      The item type. Always `mcp_call`.

      - `MCP_CALL("mcp_call")`

  - `ComputerUseCall`

    - `String id`

      The ID of the activity item.

      `minLength: 0`

    - `Optional<Output> output`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `String imageUrl`

        The complete JPEG image as a base64 data URL.

        `minLength: 0`

      - `JsonValue; type "computer_screenshot"constant`

        The content type. Always `computer_screenshot`.

        - `COMPUTER_SCREENSHOT("computer_screenshot")`

    - `AgentFunctionCallStatus status`

      The execution status of the activity.

    - `Optional<String> title`

      A model-generated description of the activity, when available.

      `minLength: 0`

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "computer_use_call"constant`

      The item type. Always `computer_use_call`.

      - `COMPUTER_USE_CALL("computer_use_call")`

  - `ComputerUseApprovalRequest`

    - `String id`

      The stable history item ID.

      `minLength: 0`

    - `Request request`

      A registered form awaiting the application's response.

      - `Optional<String> credentialOrigin`

        The registered form or frame origin where values will be entered.

        `minLength: 0`

      - `List<Field> fields`

        Controls to render. All submitted values are sensitive.

        `minItems: 0`, `maxItems: 2000`

        - `String id`

          The field ID to submit as field_id in a fields entry.

          `minLength: 0`

        - `String label`

          The label to display beside the control.

          `minLength: 0`

        - `boolean required`

          Whether this control requires a nonempty value.

        - `String type`

          The rendering type, such as email, password, or text.

          `minLength: 0`

      - `List<Option> options`

        Sign-in methods. Empty for a plain form.

        `minItems: 0`, `maxItems: 2000`

        - `String id`

          The option ID to submit as selected_option.

          `minLength: 0`

        - `List<String> fieldIds`

          IDs from the registered fields that this method accepts.

          `minItems: 0`, `maxItems: 2000`

        - `String label`

          The method label to display.

          `minLength: 0`

      - `Optional<String> reason`

        Why the agent needs the user to sign in.

        `minLength: 0`

      - `JsonValue; type "browser_authentication"constant`

        The type of the object. Always `browser_authentication`.

        - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String requestId`

      `minLength: 0`

    - `String turnId`

      `minLength: 0`

    - `JsonValue; type "computer_use_approval_request"constant`

      The item type. Always computer_use_approval_request.

      - `COMPUTER_USE_APPROVAL_REQUEST("computer_use_approval_request")`

  - `ComputerUseApprovalRequestResult`

    - `String id`

      The stable history item ID.

      `minLength: 0`

    - `String requestId`

      The registered request answered by this item.

      `minLength: 0`

    - `Response response`

      The admitted response, without submitted credential values.

      - `class Submit:`

        - `JsonValue; action "submit"constant`

          - `SUBMIT("submit")`

        - `Optional<String> selectedOption`

          The chosen sign-in method, or null when no options were offered.

          `minLength: 0`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

      - `JsonValue;`

        - `JsonValue; action "cancel"constant`

          - `CANCEL("cancel")`

        - `JsonValue; type "browser_authentication"constant`

          - `BROWSER_AUTHENTICATION("browser_authentication")`

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "computer_use_approval_request_result"constant`

      - `COMPUTER_USE_APPROVAL_REQUEST_RESULT("computer_use_approval_request_result")`

  - `class AgentWebSearchCallItem:`

    A web search call produced by the agent.

    - `String id`

      The ID of the web search call.

      `minLength: 0`

    - `Optional<WebSearchAction> action`

      The action performed by the web search tool.

      - `Search`

        - `Optional<List<String>> queries`

          The search queries, when multiple queries were used.

          `minItems: 0`, `maxItems: 2000`

        - `Optional<String> query`

          The search query, when a single query was used.

          `minLength: 0`

        - `JsonValue; type "search"constant`

          The type of the object. Always `search`.

          - `SEARCH("search")`

      - `OpenPage`

        - `JsonValue; type "open_page"constant`

          The type of the object. Always `open_page`.

          - `OPEN_PAGE("open_page")`

        - `Optional<String> url`

          The URL of the page that was opened.

          `minLength: 0`

      - `FindInPage`

        - `Optional<String> pattern`

          The text pattern that was searched for.

          `minLength: 0`

        - `JsonValue; type "find_in_page"constant`

          The type of the object. Always `find_in_page`.

          - `FIND_IN_PAGE("find_in_page")`

        - `Optional<String> url`

          The URL of the page that was searched.

          `minLength: 0`

      - `JsonValue;`

        - `JsonValue; type "other"constant`

          The type of the object. Always `other`.

          - `OTHER("other")`

    - `AgentOutputItemStatus status`

      The status of the web search call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "web_search_call"constant`

      The item type. Always `web_search_call`.

      - `WEB_SEARCH_CALL("web_search_call")`

  - `class AgentCommandExecutionItem:`

    A command execution produced by the agent.

    - `String id`

      The ID of the command execution item.

      `minLength: 0`

    - `String command`

      The command that was executed.

      `minLength: 0`

    - `Optional<String> cwd`

      The working directory used to execute the command.

      `minLength: 0`

    - `Optional<Long> durationMs`

      The command duration in milliseconds.

      `format: int64`

    - `Optional<Long> exitCode`

      The process exit code, if the command completed.

      `format: int64`

    - `Optional<String> output`

      The command output, if available.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the command execution.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "command_execution"constant`

      The item type. Always `command_execution`.

      - `COMMAND_EXECUTION("command_execution")`

  - `class AgentCreateSubagentCallItem:`

    A request to spawn a subagent.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `String agentId`

      The ID of the agent that requested the subagent.

      `minLength: 0`

    - `List<AgentContent> content`

      The task given to the spawned agent.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `Optional<String> model`

      The model requested for the spawned agent.

      `minLength: 0`

    - `Optional<String> reasoningEffort`

      The reasoning effort requested for the spawned agent.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "create_subagent_call"constant`

      The item type. Always `create_subagent_call`.

      - `CREATE_SUBAGENT_CALL("create_subagent_call")`

  - `class AgentSendSubagentInputCallItem:`

    A request to send input to another agent.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `List<AgentContent> content`

      The input sent to the receiving agent.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText:`

        A text content part produced by the agent.

      - `EncryptedContent`

    - `String recipientAgentId`

      The ID of the agent receiving the input.

      `minLength: 0`

    - `String senderAgentId`

      The ID of the agent sending the input.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "send_subagent_input_call"constant`

      The item type. Always `send_subagent_input_call`.

      - `SEND_SUBAGENT_INPUT_CALL("send_subagent_input_call")`

  - `class AgentResumeSubagentCallItem:`

    A request to resume a subagent.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `String recipientAgentId`

      The ID of the agent to resume.

      `minLength: 0`

    - `String senderAgentId`

      The ID of the agent requesting the resume.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "resume_subagent_call"constant`

      The item type. Always `resume_subagent_call`.

      - `RESUME_SUBAGENT_CALL("resume_subagent_call")`

  - `class AgentWaitForSubagentsCallItem:`

    A request to wait for one or more subagents.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `List<String> recipientAgentIds`

      The IDs of the agents to wait for.

      `minItems: 0`, `maxItems: 2000`

    - `String senderAgentId`

      The ID of the agent waiting for results.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "wait_for_subagents_call"constant`

      The item type. Always `wait_for_subagents_call`.

      - `WAIT_FOR_SUBAGENTS_CALL("wait_for_subagents_call")`

  - `class AgentInterruptSubagentCallItem:`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `String recipientAgentId`

      The ID of the agent to interrupt.

      `minLength: 0`

    - `String senderAgentId`

      The ID of the agent requesting the interrupt.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "interrupt_subagent_call"constant`

      The item type. Always `interrupt_subagent_call`.

      - `INTERRUPT_SUBAGENT_CALL("interrupt_subagent_call")`

  - `class AgentCloseSubagentCallItem:`

    A request to close a subagent.

    - `String id`

      The ID of the tool call item.

      `minLength: 0`

    - `String recipientAgentId`

      The ID of the agent to close.

      `minLength: 0`

    - `String senderAgentId`

      The ID of the agent requesting the close.

      `minLength: 0`

    - `AgentFunctionCallStatus status`

      The status of the tool call.

    - `String turnId`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `JsonValue; type "close_subagent_call"constant`

      The item type. Always `close_subagent_call`.

      - `CLOSE_SUBAGENT_CALL("close_subagent_call")`

### Example

```java
package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.agents.sessions.turns.items.ItemListPage;
import com.openai.models.beta.agents.sessions.turns.items.ItemListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ItemListParams params = ItemListParams.builder()
            .sessionId("session_id")
            .turnId("turn_id")
            .build();
        ItemListPage page = client.beta().agents().sessions().turns().items().list(params);
    }
}
```

#### 200 — Example

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
