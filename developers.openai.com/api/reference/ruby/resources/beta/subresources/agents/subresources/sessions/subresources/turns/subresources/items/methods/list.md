<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/agents/subresources/sessions/subresources/turns/subresources/items/methods/list/ -->

## List agent session turn items

`beta.agents.sessions.turns.items.list(turn_id, **kwargs) -> ConversationCursorPage<AgentSessionItem>`

**get** `/agents/sessions/{session_id}/turns/{turn_id}/items`

Lists items belonging to one root-agent turn, including its interactions with subagents. See [inspecting agent output](/api/docs/guides/agents-api/observability).

- `session_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `turn_id: String`

  `minLength: 0`, `maxLength: 1048576`

- `after: String`

  Return items after this cursor in the selected order. Pass the previous response's last_id, which can differ from the last item's ID.

  `minLength: 0`, `maxLength: 1048576`

- `limit: Integer`

  The maximum number of resources to return, between 1 and 100. Defaults to 20.

  `format: int64`, `minimum: 1`, `maximum: 100`

- `order: :asc | :desc`

  The order in which resources are returned. Defaults to `desc`.

  - `:asc`

    Returns resources in ascending order.

  - `:desc`

    Returns resources in descending order.

- `AgentSessionItem = AgentSessionMessage | AgentReasoningItem | AgentFunctionCallItem | 14 more`

  An item associated with a session turn.

  - `class AgentSessionMessage`

    A user or assistant message recorded in a session.

    - `id: String`

      The ID of this item, or null for legacy user messages whose ID was not recorded.

      `minLength: 0`

    - `content: Array[AgentSessionMessageContent]`

      The content of the message. User messages contain input text or images; assistant messages contain output text.

      `minItems: 0`, `maxItems: 2000`

      - `class InputText`

        Text supplied by the user.

        - `text: String`

          The text supplied by the user.

          `minLength: 0`

        - `type: :input_text`

          The type of the object. Always `input_text`.

          - `:input_text`

      - `class InputImage`

        An image supplied by the user.

        - `image_url: String`

          The URL of the image supplied by the user, which may be a base64-encoded data URL.

          `minLength: 0`

        - `type: :input_image`

          The type of the object. Always `input_image`.

          - `:input_image`

      - `class OutputText`

        Text produced by the assistant.

        - `text: String`

          The text produced by the assistant.

          `minLength: 0`

        - `type: :output_text`

          The type of the object. Always `output_text`.

          - `:output_text`

    - `phase: :commentary | :final_answer`

      The phase of an assistant message. Null for user messages.

      - `:commentary`

        Commentary produced while the agent works.

      - `:final_answer`

        The agent's final answer.

    - `role: :user | :assistant`

      The role of the message author.

      - `:user`

      - `:assistant`

    - `status: AgentOutputItemStatus`

      The status of the message. User messages are always `completed`.

      - `:in_progress`

        The item is in progress.

      - `:completed`

        The item is complete.

      - `:incomplete`

        The item stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :message`

      The item type. Always `message`.

      - `:message`

  - `class AgentReasoningItem`

    A reasoning item produced by the agent.

    - `id: String`

      The ID of the reasoning item.

      `minLength: 0`

    - `status: AgentOutputItemStatus`

      The status of the reasoning item.

    - `summary: Array[SummaryText]`

      The reasoning summaries produced by the agent.

      `minItems: 0`, `maxItems: 2000`

      - `text: String`

        The reasoning summary text.

        `minLength: 0`

      - `type: :summary_text`

        The content type. Always `summary_text`.

        - `:summary_text`

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :reasoning`

      The item type. Always `reasoning`.

      - `:reasoning`

  - `class AgentFunctionCallItem`

    A function call produced by the agent.

    - `id: String`

      The ID of the function call item.

      `minLength: 0`

    - `arguments: untyped`

      The arguments to pass to the function.

    - `call_id: String`

      The ID used to submit the function result.

      `minLength: 0`

    - `name: String`

      The name of the function to call.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

      - `:in_progress`

        The call is in progress.

      - `:completed`

        The call completed successfully.

      - `:failed`

        The call failed.

      - `:incomplete`

        The call stopped before completing.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :function_call`

      The item type. Always `function_call`.

      - `:function_call`

  - `class FunctionCallOutput`

    The result supplied for a function call.

    - `id: String`

      The ID of the function call output item.

      `minLength: 0`

    - `call_id: String`

      The ID of the function call that produced this output.

      `minLength: 0`

    - `error: String`

      The error message, if the call failed.

      `minLength: 0`

    - `output: AgentFunctionCallOutput`

      The function result, if the call succeeded.

      - `String = String`

      - `UnionMember1 = Array[InputContent]`

        - `class InputText`

          Text input recorded in a session item.

          - `text: String`

            The text supplied to the agent.

            `minLength: 0`

          - `type: :input_text`

            The type of the object. Always `input_text`.

            - `:input_text`

        - `class InputImage`

          Image input recorded in a session item.

          - `image_url: String`

            The URL of the image supplied to the agent, which may be a base64-encoded data URL.

            `minLength: 0`

          - `type: :input_image`

            The type of the object. Always `input_image`.

            - `:input_image`

    - `status: AgentFunctionCallStatus`

      The status of the function call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :function_call_output`

      The item type. Always `function_call_output`.

      - `:function_call_output`

  - `class AgentMessage`

    A message exchanged between agent threads.

    - `id: String`

      The ID of the message.

      `minLength: 0`

    - `content: Array[AgentContent]`

      The content exchanged between the agents.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText`

        A text content part produced by the agent.

        - `text: String`

          The text produced by the agent.

          `minLength: 0`

        - `type: :output_text`

          The content type. Always `output_text`.

          - `:output_text`

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

        - `encrypted_content: String`

          The encrypted content payload.

          `minLength: 0`

        - `type: :encrypted_content`

          The content type. Always `encrypted_content`.

          - `:encrypted_content`

    - `recipient_agent_id: String`

      The ID or name of the receiving agent.

      `minLength: 0`

    - `sender_agent_id: String`

      The ID or name of the sending agent.

      `minLength: 0`

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :agent_message`

      The item type. Always `agent_message`.

      - `:agent_message`

  - `class AgentMcpCallItem`

    A call to a tool on an MCP server.

    - `id: String`

      The ID of the MCP call item.

      `minLength: 0`

    - `arguments: untyped`

      The arguments passed to the MCP tool.

    - `error: untyped`

      The error returned by the MCP tool, if any.

    - `name: String`

      The name of the MCP tool.

      `minLength: 0`

    - `output: untyped`

      The output returned by the MCP tool, if any.

    - `server_label: String`

      The label of the MCP server.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the MCP tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :mcp_call`

      The item type. Always `mcp_call`.

      - `:mcp_call`

  - `class ComputerUseCall`

    One execution of the platform-provided computer-use capability.

    - `id: String`

      The ID of the activity item.

      `minLength: 0`

    - `output: Output{ image_url, type}`

      The last screenshot emitted by the model. Null when screenshot inclusion is disabled or the call emitted no screenshot.

      - `image_url: String`

        The complete JPEG image as a base64 data URL.

        `minLength: 0`

      - `type: :computer_screenshot`

        The content type. Always `computer_screenshot`.

        - `:computer_screenshot`

    - `status: AgentFunctionCallStatus`

      The execution status of the activity.

    - `title: String`

      A model-generated description of the activity, when available.

      `minLength: 0`

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :computer_use_call`

      The item type. Always `computer_use_call`.

      - `:computer_use_call`

  - `class ComputerUseApprovalRequest`

    A credential-free history record of the emitted login request.

    - `id: String`

      The stable history item ID.

      `minLength: 0`

    - `request: Request{ credential_origin, fields, options, 2 more}`

      A registered form awaiting the application's response.

      - `credential_origin: String`

        The registered form or frame origin where values will be entered.

        `minLength: 0`

      - `fields: Array[Field{ id, label, required, type}]`

        Controls to render. All submitted values are sensitive.

        `minItems: 0`, `maxItems: 2000`

        - `id: String`

          The field ID to submit as field_id in a fields entry.

          `minLength: 0`

        - `label: String`

          The label to display beside the control.

          `minLength: 0`

        - `required: bool`

          Whether this control requires a nonempty value.

        - `type: String`

          The rendering type, such as email, password, or text.

          `minLength: 0`

      - `options: Array[Option{ id, field_ids, label}]`

        Sign-in methods. Empty for a plain form.

        `minItems: 0`, `maxItems: 2000`

        - `id: String`

          The option ID to submit as selected_option.

          `minLength: 0`

        - `field_ids: Array[String]`

          IDs from the registered fields that this method accepts.

          `minItems: 0`, `maxItems: 2000`

        - `label: String`

          The method label to display.

          `minLength: 0`

      - `reason: String`

        Why the agent needs the user to sign in.

        `minLength: 0`

      - `type: :browser_authentication`

        The type of the object. Always `browser_authentication`.

        - `:browser_authentication`

    - `request_id: String`

      `minLength: 0`

    - `turn_id: String`

      `minLength: 0`

    - `type: :computer_use_approval_request`

      The item type. Always computer_use_approval_request.

      - `:computer_use_approval_request`

  - `class ComputerUseApprovalRequestResult`

    A credential-free record of an admitted response, not proof of completion.

    - `id: String`

      The stable history item ID.

      `minLength: 0`

    - `request_id: String`

      The registered request answered by this item.

      `minLength: 0`

    - `response: Submit{ action, selected_option, type} | Cancel{ action, type}`

      The admitted response, without submitted credential values.

      - `class Submit`

        - `action: :submit`

          - `:submit`

        - `selected_option: String`

          The chosen sign-in method, or null when no options were offered.

          `minLength: 0`

        - `type: :browser_authentication`

          - `:browser_authentication`

      - `class Cancel`

        - `action: :cancel`

          - `:cancel`

        - `type: :browser_authentication`

          - `:browser_authentication`

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :computer_use_approval_request_result`

      - `:computer_use_approval_request_result`

  - `class AgentWebSearchCallItem`

    A web search call produced by the agent.

    - `id: String`

      The ID of the web search call.

      `minLength: 0`

    - `action: WebSearchAction`

      The action performed by the web search tool.

      - `class Search`

        A search query or group of search queries.

        - `queries: Array[String]`

          The search queries, when multiple queries were used.

          `minItems: 0`, `maxItems: 2000`

        - `query: String`

          The search query, when a single query was used.

          `minLength: 0`

        - `type: :search`

          The type of the object. Always `search`.

          - `:search`

      - `class OpenPage`

        Opens a web page.

        - `type: :open_page`

          The type of the object. Always `open_page`.

          - `:open_page`

        - `url: String`

          The URL of the page that was opened.

          `minLength: 0`

      - `class FindInPage`

        Finds text within a web page.

        - `pattern: String`

          The text pattern that was searched for.

          `minLength: 0`

        - `type: :find_in_page`

          The type of the object. Always `find_in_page`.

          - `:find_in_page`

        - `url: String`

          The URL of the page that was searched.

          `minLength: 0`

      - `class Other`

        Another web search action.

        - `type: :other`

          The type of the object. Always `other`.

          - `:other`

    - `status: AgentOutputItemStatus`

      The status of the web search call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :web_search_call`

      The item type. Always `web_search_call`.

      - `:web_search_call`

  - `class AgentCommandExecutionItem`

    A command execution produced by the agent.

    - `id: String`

      The ID of the command execution item.

      `minLength: 0`

    - `command: String`

      The command that was executed.

      `minLength: 0`

    - `cwd: String`

      The working directory used to execute the command.

      `minLength: 0`

    - `duration_ms: Integer`

      The command duration in milliseconds.

      `format: int64`

    - `exit_code: Integer`

      The process exit code, if the command completed.

      `format: int64`

    - `output: String`

      The command output, if available.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the command execution.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :command_execution`

      The item type. Always `command_execution`.

      - `:command_execution`

  - `class AgentCreateSubagentCallItem`

    A request to spawn a subagent.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `agent_id: String`

      The ID of the agent that requested the subagent.

      `minLength: 0`

    - `content: Array[AgentContent]`

      The task given to the spawned agent.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `model: String`

      The model requested for the spawned agent.

      `minLength: 0`

    - `reasoning_effort: String`

      The reasoning effort requested for the spawned agent.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :create_subagent_call`

      The item type. Always `create_subagent_call`.

      - `:create_subagent_call`

  - `class AgentSendSubagentInputCallItem`

    A request to send input to another agent.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `content: Array[AgentContent]`

      The input sent to the receiving agent.

      `minItems: 0`, `maxItems: 2000`

      - `class OutputText`

        A text content part produced by the agent.

      - `class EncryptedContent`

        Encrypted content exchanged between agents.

    - `recipient_agent_id: String`

      The ID of the agent receiving the input.

      `minLength: 0`

    - `sender_agent_id: String`

      The ID of the agent sending the input.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :send_subagent_input_call`

      The item type. Always `send_subagent_input_call`.

      - `:send_subagent_input_call`

  - `class AgentResumeSubagentCallItem`

    A request to resume a subagent.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: String`

      The ID of the agent to resume.

      `minLength: 0`

    - `sender_agent_id: String`

      The ID of the agent requesting the resume.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :resume_subagent_call`

      The item type. Always `resume_subagent_call`.

      - `:resume_subagent_call`

  - `class AgentWaitForSubagentsCallItem`

    A request to wait for one or more subagents.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_ids: Array[String]`

      The IDs of the agents to wait for.

      `minItems: 0`, `maxItems: 2000`

    - `sender_agent_id: String`

      The ID of the agent waiting for results.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :wait_for_subagents_call`

      The item type. Always `wait_for_subagents_call`.

      - `:wait_for_subagents_call`

  - `class AgentInterruptSubagentCallItem`

    A request to interrupt a subagent's current turn. The subagent remains available.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: String`

      The ID of the agent to interrupt.

      `minLength: 0`

    - `sender_agent_id: String`

      The ID of the agent requesting the interrupt.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :interrupt_subagent_call`

      The item type. Always `interrupt_subagent_call`.

      - `:interrupt_subagent_call`

  - `class AgentCloseSubagentCallItem`

    A request to close a subagent.

    - `id: String`

      The ID of the tool call item.

      `minLength: 0`

    - `recipient_agent_id: String`

      The ID of the agent to close.

      `minLength: 0`

    - `sender_agent_id: String`

      The ID of the agent requesting the close.

      `minLength: 0`

    - `status: AgentFunctionCallStatus`

      The status of the tool call.

    - `turn_id: String`

      The ID of the turn that contains this item.

      `minLength: 0`

    - `type: :close_subagent_call`

      The item type. Always `close_subagent_call`.

      - `:close_subagent_call`

```ruby
require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

page = openai.beta.agents.sessions.turns.items.list("turn_id", session_id: "session_id")

puts(page)

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
