<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/turns/subresources/items/ -->

# Items

## List agent session turn items

`client.beta.agents.sessions.turns.items.list(stringturnID, ItemListParamsparams, RequestOptionsoptions?): ConversationCursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/turns/{turn_id}/items`

Lists items belonging to one root-agent turn, including its interactions with subagents. See [inspecting agent output](/api/docs/guides/agents-api/observability).

### Parameters

- `turnID: string`

  `minLength: 0`, `maxLength: 1048576`

- `params: ItemListParams`

  - `session_id: string`

    Path param: The ID of the session that owns the turn.

    `minLength: 0`, `maxLength: 1048576`

  - `after?: string`

    Query param: Return items after this cursor in the selected order. Pass the previous response's last_id, which can differ from the last item's ID.

    `minLength: 0`, `maxLength: 1048576`

  - `limit?: number`

    Query param: The maximum number of resources to return, between 1 and 100. Defaults to 20.

    `format: int64`, `minimum: 1`, `maximum: 100`

  - `order?: "asc" | "desc"`

    Query param: The order in which resources are returned. Defaults to `desc`.

    - `"asc"`

      Returns resources in ascending order.

    - `"desc"`

      Returns resources in descending order.

### Returns

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: string | null`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

      `minLength: 0`

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      `minItems: 0`, `maxItems: 2000`

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

          `minLength: 0`

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

          `minLength: 0`

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

          `minLength: 0`

        - `type: "output_text"`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: "commentary" | "final_answer" | null`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: "user" | "assistant"`

      The role of the message author.

      - `"user"`

      - `"assistant"`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `"in_progress"`

        The item is in progress.

      - `"completed"`

        The item is complete.

      - `"incomplete"`

        The item stopped before completing.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

      `minLength: 0`

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      `minItems: 0`, `maxItems: 2000`

      - `text: string`

        The reasoning summary text.

        `minLength: 0`

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

      `minLength: 0`

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

      `minLength: 0`

    - `name: string`

      The name of the function to call.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `"in_progress"`

        The call is in progress.

      - `"completed"`

        The call completed successfully.

      - `"failed"`

        The call failed.

      - `"incomplete"`

        The call stopped before completing.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

      `minLength: 0`

    - `call_id: string`

      The ID of the function call that produced this output.

      `minLength: 0`

    - `error: string | null`

      The error message, if the call failed.

      `minLength: 0`

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

            `minLength: 0`

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

      `minLength: 0`

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      `minItems: 0`, `maxItems: 2000`

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

          `minLength: 0`

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

          `minLength: 0`

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

      `minLength: 0`

    - `sender_agent_id: string`

      The ID or name of the sending agent.

      `minLength: 0`

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

      `minLength: 0`

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

      `minLength: 0`

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

      `minLength: 0`

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

        `minLength: 0`

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

      `minLength: 0`

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

      `minLength: 0`

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

        `minLength: 0`

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        `minItems: 0`, `maxItems: 2000`

        - `id: string`

          The field ID to submit as field_id in a fields entry.

          `minLength: 0`

        - `label: string`

          The label to display beside the control.

          `minLength: 0`

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

          `minLength: 0`

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        `minItems: 0`, `maxItems: 2000`

        - `id: string`

          The option ID to submit as selected_option.

          `minLength: 0`

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

          `minItems: 0`, `maxItems: 2000`

        - `label: string`

          The method label to display.

          `minLength: 0`

      - `reason: string | null`

        Why the agent needs the user to sign in.

        `minLength: 0`

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

      `minLength: 0`

    - `turn_id: string`

      `minLength: 0`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

      `minLength: 0`

    - `request_id: string`

      The registered request answered by this item.

      `minLength: 0`

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

          `minLength: 0`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

      `minLength: 0`

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

          `minItems: 0`, `maxItems: 2000`

        - `query: string | null`

          The search query, when a single query was used.

          `minLength: 0`

        - `type: "search"`

          The type of the object. Always `search`.

          - `"search"`

      - `WebSearchActionResourceOpenPage`

        Opens a web page.

        - `type: "open_page"`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: string | null`

          The URL of the page that was opened.

          `minLength: 0`

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

          `minLength: 0`

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

          `minLength: 0`

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

      `minLength: 0`

    - `command: string`

      The command that was executed.

      `minLength: 0`

    - `cwd: string | null`

      The working directory used to execute the command.

      `minLength: 0`

    - `duration_ms: number | null`

      The command duration in milliseconds.

      `format: int64`

    - `exit_code: number | null`

      The process exit code, if the command completed.

      `format: int64`

    - `output: string | null`

      The command output, if available.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `agent_id: string`

      The ID of the agent that requested the subagent.

      `minLength: 0`

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      `minItems: 0`, `maxItems: 2000`

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

      `minLength: 0`

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      `minItems: 0`, `maxItems: 2000`

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

      `minLength: 0`

    - `sender_agent_id: string`

      The ID of the agent sending the input.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: string`

      The ID of the agent to resume.

      `minLength: 0`

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

      `minItems: 0`, `maxItems: 2000`

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

      `minLength: 0`

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: string`

      The ID of the agent to close.

      `minLength: 0`

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSessionItem of client.beta.agents.sessions.turns.items.list('turn_id', {
  session_id: 'session_id',
})) {
  console.log(agentSessionItem);
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
