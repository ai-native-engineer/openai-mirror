<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/agents/subresources/sessions/subresources/subagents/subresources/items/methods/list/ -->

## List subagent items

`beta.agents.sessions.subagents.items.list(strsubagent_id, ItemListParams**kwargs)  -> SyncCursorPage[AgentSessionItem]`

**get** `/agents/sessions/{session_id}/subagents/{subagent_id}/items`

Lists this subagent's own items across all of its turns. See [subagent workflows](/api/docs/guides/agents-api/multi-agent).

- `session_id: str`

- `subagent_id: str`

- `after: Optional[str]`

  Return resources after this resource ID in the selected order.

- `limit: Optional[int]`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

- `order: Optional[Literal["asc", "desc"]]`

  The order in which resources are returned. Defaults to `desc`.

  - `"asc"`

    Returns resources in ascending order.

  - `"desc"`

    Returns resources in descending order.

- `AgentSessionItem`

  An item associated with a session turn.

  - `class AgentSessionMessage: …`

    A user or assistant message recorded in a session.

    - `id: Optional[str]`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

    - `content: List[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      - `class MessageContentResourceInputText: …`

        Text supplied by the user.

        - `text: str`

          The text supplied by the user.

        - `type: Literal["input_text"]`

          The type of the object. Always `input_text`.

          - `"input_text"`

      - `class MessageContentResourceInputImage: …`

        An image supplied by the user.

        - `image_url: str`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

        - `type: Literal["input_image"]`

          The type of the object. Always `input_image`.

          - `"input_image"`

      - `class MessageContentResourceOutputText: …`

        Text produced by the assistant.

        - `text: str`

          The text produced by the assistant.

        - `type: Literal["output_text"]`

          The type of the object. Always `output_text`.

          - `"output_text"`

    - `phase: Optional[Literal["commentary", "final_answer"]]`

      The phase of an assistant message. Null for user messages.

      - `"commentary"`

        Commentary produced while the agent works.

      - `"final_answer"`

        The agent's final answer.

    - `role: Literal["user", "assistant"]`

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

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["message"]`

      The item type. Always `message`.

      - `"message"`

  - `class AgentReasoningItem: …`

    A reasoning item produced by the agent.

    - `id: str`

      The ID of the reasoning item.

    - `status: Optional[AgentOutputItemStatus]`

      The status of the reasoning item.

    - `summary: List[SummaryText]`

      The reasoning summaries produced by the agent.

      - `text: str`

        The reasoning summary text.

      - `type: Literal["summary_text"]`

        The content type. Always `summary_text`.

        - `"summary_text"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["reasoning"]`

      The item type. Always `reasoning`.

      - `"reasoning"`

  - `class AgentFunctionCallItem: …`

    A function call produced by the agent.

    - `id: str`

      The ID of the function call item.

    - `arguments: object`

      The arguments to pass to the function.

    - `call_id: str`

      The ID used to submit the function result.

    - `name: str`

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

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call"]`

      The item type. Always `function_call`.

      - `"function_call"`

  - `class FunctionCallOutputItemResource: …`

    The result supplied for a function call.

    - `id: str`

      The ID of the function call output item.

    - `call_id: str`

      The ID of the function call that produced this output.

    - `error: Optional[str]`

      The error message, if the call failed.

    - `output: Optional[AgentFunctionCallOutput]`

      The function result, if the call succeeded.

      - `str`

      - `List[InputContent]`

        - `class InputContentResourceInputText: …`

          Text input recorded in a session item.

          - `text: str`

            The text supplied to the agent.

          - `type: Literal["input_text"]`

            The type of the object. Always `input_text`.

            - `"input_text"`

        - `class InputContentResourceInputImage: …`

          Image input recorded in a session item.

          - `image_url: str`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

          - `type: Literal["input_image"]`

            The type of the object. Always `input_image`.

            - `"input_image"`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["function_call_output"]`

      The item type. Always `function_call_output`.

      - `"function_call_output"`

  - `class AgentMessageItemResource: …`

    A message exchanged between agent threads.

    - `id: str`

      The ID of the message.

    - `content: List[AgentContent]`

      The content exchanged between the agents.

      - `class OutputText: …`

        A text content part produced by the agent.

        - `text: str`

          The text produced by the agent.

        - `type: Literal["output_text"]`

          The content type. Always `output_text`.

          - `"output_text"`

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

        - `encrypted_content: str`

          The encrypted content payload.

        - `type: Literal["encrypted_content"]`

          The content type. Always `encrypted_content`.

          - `"encrypted_content"`

    - `recipient_agent_id: str`

      The ID or name of the receiving agent.

    - `sender_agent_id: str`

      The ID or name of the sending agent.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["agent_message"]`

      The item type. Always `agent_message`.

      - `"agent_message"`

  - `class AgentMcpCallItem: …`

    A call to a tool on an MCP server.

    - `id: str`

      The ID of the MCP call item.

    - `arguments: object`

      The arguments passed to the MCP tool.

    - `error: object`

      The error returned by the MCP tool, if any.

    - `name: str`

      The name of the MCP tool.

    - `output: object`

      The output returned by the MCP tool, if any.

    - `server_label: str`

      The label of the MCP server.

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["mcp_call"]`

      The item type. Always `mcp_call`.

      - `"mcp_call"`

  - `class ComputerUseCallItemResource: …`

    One execution of the platform-provided computer-use capability.

    - `id: str`

      The ID of the activity item.

    - `output: Optional[ComputerUseCallItemResourceOutput]`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: str`

        The complete JPEG image as a base64 data URL.

      - `type: Literal["computer_screenshot"]`

        The content type. Always `computer_screenshot`.

        - `"computer_screenshot"`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: Optional[str]`

      A model-generated description of the activity, when available.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_call"]`

      The item type. Always `computer_use_call`.

      - `"computer_use_call"`

  - `class BrowserAuthenticationRequestItemResource: …`

    A credential-free history record of the emitted login request.

    - `id: str`

      The stable history item ID.

    - `request: BrowserAuthenticationRequestItemResourceRequest`

      A registered form awaiting the application's response.

      - `credential_origin: Optional[str]`

        The registered form or frame origin where values will be entered.

      - `fields: List[BrowserAuthenticationRequestItemResourceRequestField]`

        Controls to render. All submitted values are sensitive.

        - `id: str`

          The field ID to submit as field_id in a fields entry.

        - `label: str`

          The label to display beside the control.

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: str`

          The rendering type, such as email, password, or text.

      - `options: List[BrowserAuthenticationRequestItemResourceRequestOption]`

        Sign-in methods. Empty for a plain form.

        - `id: str`

          The option ID to submit as selected_option.

        - `field_ids: List[str]`

          IDs from the registered fields that this method accepts.

        - `label: str`

          The method label to display.

      - `reason: Optional[str]`

        Why the agent needs the user to sign in.

      - `type: Literal["browser_authentication"]`

        The type of the object. Always `browser_authentication`.

        - `"browser_authentication"`

    - `request_id: str`

    - `turn_id: str`

    - `type: Literal["computer_use_approval_request"]`

      The item type. Always computer_use_approval_request.

      - `"computer_use_approval_request"`

  - `class ComputerUseApprovalRequestResultItemResource: …`

    A credential-free record of an admitted response, not proof of completion.

    - `id: str`

      The stable history item ID.

    - `request_id: str`

      The registered request answered by this item.

    - `response: ComputerUseApprovalRequestResultItemResourceResponse`

      The admitted response, without submitted credential values.

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationSubmitResource: …`

        - `action: Literal["submit"]`

          - `"submit"`

        - `selected_option: Optional[str]`

          The chosen sign-in method, or null when no options were offered.

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

      - `class ComputerUseApprovalRequestResultItemResourceResponseComputerUseApprovalResponseKindResourceBrowserAuthenticationCancelResource: …`

        - `action: Literal["cancel"]`

          - `"cancel"`

        - `type: Literal["browser_authentication"]`

          - `"browser_authentication"`

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["computer_use_approval_request_result"]`

      - `"computer_use_approval_request_result"`

  - `class AgentWebSearchCallItem: …`

    A web search call produced by the agent.

    - `id: str`

      The ID of the web search call.

    - `action: Optional[WebSearchAction]`

      The action performed by the web search tool.

      - `class WebSearchActionResourceSearch: …`

        A search query or group of search queries.

        - `queries: Optional[List[str]]`

          The search queries, when multiple queries were used.

        - `query: Optional[str]`

          The search query, when a single query was used.

        - `type: Literal["search"]`

          The type of the object. Always `search`.

          - `"search"`

      - `class WebSearchActionResourceOpenPage: …`

        Opens a web page.

        - `type: Literal["open_page"]`

          The type of the object. Always `open_page`.

          - `"open_page"`

        - `url: Optional[str]`

          The URL of the page that was opened.

      - `class WebSearchActionResourceFindInPage: …`

        Finds text within a web page.

        - `pattern: Optional[str]`

          The text pattern that was searched for.

        - `type: Literal["find_in_page"]`

          The type of the object. Always `find_in_page`.

          - `"find_in_page"`

        - `url: Optional[str]`

          The URL of the page that was searched.

      - `class WebSearchActionResourceOther: …`

        Another web search action.

        - `type: Literal["other"]`

          The type of the object. Always `other`.

          - `"other"`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["web_search_call"]`

      The item type. Always `web_search_call`.

      - `"web_search_call"`

  - `class AgentCommandExecutionItem: …`

    A command execution produced by the agent.

    - `id: str`

      The ID of the command execution item.

    - `command: str`

      The command that was executed.

    - `cwd: Optional[str]`

      The working directory used to execute the command.

    - `duration_ms: Optional[int]`

      The command duration in milliseconds.

    - `exit_code: Optional[int]`

      The process exit code, if the command completed.

    - `output: Optional[str]`

      The command output, if available.

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["command_execution"]`

      The item type. Always `command_execution`.

      - `"command_execution"`

  - `class AgentCreateSubagentCallItem: …`

    A request to spawn a subagent.

    - `id: str`

      The ID of the tool call item.

    - `agent_id: str`

      The ID of the agent that requested the subagent.

    - `content: List[AgentContent]`

      The task given to the spawned agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `model: Optional[str]`

      The model requested for the spawned agent.

    - `reasoning_effort: Optional[str]`

      The reasoning effort requested for the spawned agent.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["create_subagent_call"]`

      The item type. Always `create_subagent_call`.

      - `"create_subagent_call"`

        The current public item type.

  - `class AgentSendSubagentInputCallItem: …`

    A request to send input to another agent.

    - `id: str`

      The ID of the tool call item.

    - `content: List[AgentContent]`

      The input sent to the receiving agent.

      - `class OutputText: …`

        A text content part produced by the agent.

      - `class EncryptedContentResource: …`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: str`

      The ID of the agent receiving the input.

    - `sender_agent_id: str`

      The ID of the agent sending the input.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["send_subagent_input_call"]`

      The item type. Always `send_subagent_input_call`.

      - `"send_subagent_input_call"`

        The current public item type.

  - `class AgentResumeSubagentCallItem: …`

    A request to resume a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to resume.

    - `sender_agent_id: str`

      The ID of the agent requesting the resume.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["resume_subagent_call"]`

      The item type. Always `resume_subagent_call`.

      - `"resume_subagent_call"`

        The current public item type.

  - `class AgentWaitForSubagentsCallItem: …`

    A request to wait for one or more subagents.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_ids: List[str]`

      The IDs of the agents to wait for.

    - `sender_agent_id: str`

      The ID of the agent waiting for results.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["wait_for_subagents_call"]`

      The item type. Always `wait_for_subagents_call`.

      - `"wait_for_subagents_call"`

        The current public item type.

  - `class AgentInterruptSubagentCallItem: …`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to interrupt.

    - `sender_agent_id: str`

      The ID of the agent requesting the interrupt.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["interrupt_subagent_call"]`

      The item type. Always `interrupt_subagent_call`.

      - `"interrupt_subagent_call"`

        The current public item type.

  - `class AgentCloseSubagentCallItem: …`

    A request to close a subagent.

    - `id: str`

      The ID of the tool call item.

    - `recipient_agent_id: str`

      The ID of the agent to close.

    - `sender_agent_id: str`

      The ID of the agent requesting the close.

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: str`

      The ID of the turn that contains this item.

    - `type: Literal["close_subagent_call"]`

      The item type. Always `close_subagent_call`.

      - `"close_subagent_call"`

        The current public item type.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
page = client.beta.agents.sessions.subagents.items.list(
    subagent_id="subagent_id",
    session_id="session_id",
page = page.data[0]
print(page)

  "data": [
      "content": [
          "text": "text",
          "type": "input_text"
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
