<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/items/ -->

# Items

## List subagent items

`client.beta.agents.sessions.subagents.items.list(stringsubagentID, ItemListParamsparams, RequestOptionsoptions?): CursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

### Parameters

- `subagentID: string`

- `params: ItemListParams`

  - `session_id: string`

    Path param: The ID of the session.

  - `after?: string`

    Query param: Return resources after this resource ID in the selected order.

  - `limit?: number`

    Query param: The maximum number of resources to return, between 1 and 100. Defaults to 20.

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

    - `content: Array<AgentSessionMessageContent>`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `MessageContentResourceInputText`

        Text supplied by the user.

        - `text: string`

          The text supplied by the user.

        - `type: "input_text"`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `MessageContentResourceInputImage`

        An image supplied by the user.

        - `image_url: string`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: "input_image"`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `MessageContentResourceOutputText`

        Text produced by the assistant.

        - `text: string`

          The text produced by the assistant.

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

    - `type: "message"`

      The item type. Always `message`.

      - `"message"`

  - `AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: string`

      The ID of the reasoning item.

    - `status: AgentOutputItemStatus | null`

      The status of the reasoning item.

    - `summary: Array<SummaryText>`

      The reasoning summaries produced by the agent.

      - `text: string`

        The reasoning summary text.

      - `type: "summary_text"`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "reasoning"`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: string`

      The ID of the function call item.

    - `arguments: unknown`

      The arguments to pass to the function.

    - `call_id: string`

      The ID used to submit the function result.

    - `name: string`

      The name of the function to call.

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

    - `type: "function_call"`

      The item type. Always `function_call`.

      - `"function_call"`

  - `FunctionCallOutputItemResource`

    The result supplied for a function call.

    - `id: string`

      The ID of the function call output item.

    - `call_id: string`

      The ID of the function call that produced this output.

    - `error: string | null`

      The error message, if the call failed.

    - `output: AgentFunctionCallOutput | null`

      The function result, if the call succeeded.

      - `string`

      - `Array<InputContent>`

        - `InputContentResourceInputText`

          Text input recorded in a session item.

          - `text: string`

            The text supplied to the agent.

          - `type: "input_text"`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `InputContentResourceInputImage`

          Image input recorded in a session item.

          - `image_url: string`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: "input_image"`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "function_call_output"`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `AgentMessageItemResource`

    A message exchanged between agent threads.

    - `id: string`

      The ID of the message.

    - `content: Array<AgentContent>`

      The content exchanged between the agents.

      - `OutputText`

        A text content part produced by the agent.

        - `text: string`

          The text produced by the agent.

        - `type: "output_text"`

          The content type. Always `output_text`.

          - `"output_text"`

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

        - `encrypted_content: string`

          The encrypted content payload.

        - `type: "encrypted_content"`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: string`

      The ID or name of the receiving agent.

    - `sender_agent_id: string`

      The ID or name of the sending agent.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "agent_message"`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: string`

      The ID of the MCP call item.

    - `arguments: unknown`

      The arguments passed to the MCP tool.

    - `error: unknown`

      The error returned by the MCP tool, if any.

    - `name: string`

      The name of the MCP tool.

    - `output: unknown`

      The output returned by the MCP tool, if any.

    - `server_label: string`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "mcp_call"`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `ComputerUseCallItemResource`

    One execution of the platform-provided computer-use capability.

    - `id: string`

      The ID of the activity item.

    - `output: Output | null`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: string`

        The complete JPEG image as a base64 data URL.

      - `type: "computer_screenshot"`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: string | null`

      A model-generated description of the activity, when available.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_call"`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `BrowserAuthenticationRequestItemResource`

    A credential-free history record of the emitted login request.

    - `id: string`

      The stable history item ID.

    - `request: Request`

      A registered form awaiting the application's response.

      - `credential_origin: string | null`

        The registered form or frame origin where values will be entered.

      - `fields: Array<Field>`

        Controls to render. All submitted values are sensitive.

        - `id: string`

          The field ID to submit as field_id in a fields entry.

        - `label: string`

          The label to display beside the control.

        - `required: boolean`

          Whether this control requires a nonempty value.

        - `type: string`

          The rendering type, such as email, password, or text.

      - `options: Array<Option>`

        Sign-in methods. Empty for a plain form.

        - `id: string`

          The option ID to submit as selected_option.

        - `field_ids: Array<string>`

          IDs from the registered fields that this method accepts.

        - `label: string`

          The method label to display.

      - `reason: string | null`

        Why the agent needs the user to sign in.

      - `type: "browser_authentication"`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: string`

    - `turn_id: string`

    - `type: "computer_use_approval_request"`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `ComputerUseApprovalRequestResultItemResource`

    A credential-free record of an admitted response, not proof of completion.

    - `id: string`

      The stable history item ID.

    - `request_id: string`

      The registered request answered by this item.

    - `response: ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource | ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

      The admitted response, without submitted credential values.

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource`

        - `action: "submit"`

          - `"submit"`

        - `selected_option: string | null`

          The chosen sign-in method, or null when no options were offered.

        - `type: "browser_authentication"`

          - `"browser_authentication"`

      - `ComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource`

        - `action: "cancel"`

          - `"cancel"`

        - `type: "browser_authentication"`

          - `"browser_authentication"`

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "computer_use_approval_request_result"`

      - `"computer_use_approval_request_result"`

  - `AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: string`

      The ID of the web search call.

    - `action: WebSearchAction | null`

      The action performed by the web search tool.

      - `WebSearchActionResourceSearch`

        A search query or group of search queries.

        - `queries: Array<string> | null`

          The search queries, when multiple queries were used.

        - `query: string | null`

          The search query, when a single query was used.

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

      - `WebSearchActionResourceFindInPage`

        Finds text within a web page.

        - `pattern: string | null`

          The text pattern that was searched for.

        - `type: "find_in_page"`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: string | null`

          The URL of the page that was searched.

      - `WebSearchActionResourceOther`

        Another web search action.

        - `type: "other"`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "web_search_call"`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: string`

      The ID of the command execution item.

    - `command: string`

      The command that was executed.

    - `cwd: string | null`

      The working directory used to execute the command.

    - `duration_ms: number | null`

      The command duration in milliseconds.

    - `exit_code: number | null`

      The process exit code, if the command completed.

    - `output: string | null`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "command_execution"`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: string`

      The ID of the tool call item.

    - `agent_id: string`

      The ID of the agent that requested the subagent.

    - `content: Array<AgentContent>`

      The task given to the spawned agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `model: string | null`

      The model requested for the spawned agent.

    - `reasoning_effort: string | null`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "create_subagent_call"`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: string`

      The ID of the tool call item.

    - `content: Array<AgentContent>`

      The input sent to the receiving agent.

      - `OutputText`

        A text content part produced by the agent.

      - `EncryptedContentResource`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: string`

      The ID of the agent receiving the input.

    - `sender_agent_id: string`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "send_subagent_input_call"`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to resume.

    - `sender_agent_id: string`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "resume_subagent_call"`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_ids: Array<string>`

      The IDs of the agents to wait for.

    - `sender_agent_id: string`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "wait_for_subagents_call"`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to interrupt.

    - `sender_agent_id: string`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "interrupt_subagent_call"`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: string`

      The ID of the tool call item.

    - `recipient_agent_id: string`

      The ID of the agent to close.

    - `sender_agent_id: string`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: string`

      The ID of the turn that contains this item.

    - `type: "close_subagent_call"`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

### Example

```typescript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env['OPENAI_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const agentSessionItem of client.beta.agents.sessions.subagents.items.list(
  'subagent_id',
  { session_id: 'session_id' },
)) {
  console.log(agentSessionItem);
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
