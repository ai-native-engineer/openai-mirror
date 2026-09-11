<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/items/methods/list/ -->

[Sessions](/api/reference/resources/beta/subresources/agents/subresources/sessions)

[Items](/api/reference/resources/beta/subresources/agents/subresources/sessions/subresources/items)

# List agent session items

GET/agents/sessions/{session\_id}/items

Lists items produced by the session’s root agent, including its interactions with subagents. Each subagent has its own item history. See [inspecting agent output](/api/docs/guides/agents-api/observability).

session\_id: string

##### Query ParametersExpand Collapse

after: optional string

Return resources after this resource ID in the selected order.

limit: optional number

The maximum number of resources to return, between 1 and 100. Defaults to 20.

minimum1

maximum100

order: optional "asc" or "desc"

The order in which resources are returned. Defaults to `desc`.

"asc"

Returns resources in ascending order.

"desc"

Returns resources in descending order.

data: array of [AgentSessionItem](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_item%20%3E%20(schema))

The resources returned in this page, in the requested sort order.

AgentSessionMessage object { id, content, phase, 4 more }

A user or assistant message recorded in a session.

id: string or null

The ID of this item, or null for legacy user messages whose ID was not recorded.

content: array of [AgentSessionMessageContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_session_message_content%20%3E%20(schema))

The content of the message. User messages contain input text or images; assistant messages contain output text.

InputText object { text, type }

Text supplied by the user.

text: string

The text supplied by the user.

type: "input\_text"

The type of the object. Always `input_text`.

InputImage object { image\_url, type }

An image supplied by the user.

image\_url: string

The URL of the image supplied by the user, which may be a base64-encoded data URL.

type: "input\_image"

The type of the object. Always `input_image`.

OutputText object { text, type }

Text produced by the assistant.

text: string

The text produced by the assistant.

type: "output\_text"

The type of the object. Always `output_text`.

phase: "commentary" or "final\_answer" or null

The phase of an assistant message.

"commentary"

Commentary produced while the agent works.

"final\_answer"

The agent’s final answer.

role: "user" or "assistant"

The role of the message author.

"user"

"assistant"

status: [AgentOutputItemStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_output_item_status%20%3E%20(schema))

The status of the message. User messages are always `completed`.

"in\_progress"

The item is in progress.

"completed"

The item is complete.

"incomplete"

The item stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "message"

The item type. Always `message`.

AgentReasoningItem object { id, status, summary, 2 more }

A reasoning item produced by the agent.

The ID of the reasoning item.

status: [AgentOutputItemStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_output_item_status%20%3E%20(schema)) or null

The status of an agent output item.

"in\_progress"

The item is in progress.

"completed"

The item is complete.

"incomplete"

The item stopped before completing.

summary: array of [SummaryText](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20summary_text%20%3E%20(schema)) { text, type }

The reasoning summaries produced by the agent.

text: string

The reasoning summary text.

type: "summary\_text"

The content type. Always `summary_text`.

turn\_id: string

The ID of the turn that contains this item.

type: "reasoning"

The item type. Always `reasoning`.

AgentFunctionCallItem object { id, arguments, call\_id, 4 more }

A function call produced by the agent.

The ID of the function call item.

arguments: unknown

The arguments to pass to the function.

call\_id: string

The ID used to submit the function result.

The name of the function to call.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the function call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "function\_call"

The item type. Always `function_call`.

FunctionCallOutput object { id, call\_id, error, 4 more }

The result supplied for a function call.

The ID of the function call output item.

call\_id: string

The ID of the function call that produced this output.

error: string or null

The error message, if the call failed.

output: [AgentFunctionCallOutput](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_output%20%3E%20(schema)) or null

The text or model-input content supplied as a function result.

string

array of [InputContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20input_content%20%3E%20(schema))

InputText object { text, type }

Text input recorded in a session item.

text: string

The text supplied to the agent.

type: "input\_text"

The type of the object. Always `input_text`.

InputImage object { image\_url, type }

Image input recorded in a session item.

image\_url: string

The URL of the image supplied to the agent, which may be a base64-encoded data URL.

type: "input\_image"

The type of the object. Always `input_image`.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the function call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "function\_call\_output"

The item type. Always `function_call_output`.

AgentMessage object { id, content, recipient\_agent\_id, 3 more }

A message exchanged between agent threads.

The ID of the message.

content: array of [AgentContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_content%20%3E%20(schema))

The content exchanged between the agents.

OutputText object { text, type }

A text content part produced by the agent.

text: string

The text produced by the agent.

type: "output\_text"

The content type. Always `output_text`.

EncryptedContent object { encrypted\_content, type }

Encrypted content exchanged between agents.

encrypted\_content: string

The encrypted content payload.

type: "encrypted\_content"

The content type. Always `encrypted_content`.

recipient\_agent\_id: string

The ID or name of the receiving agent.

sender\_agent\_id: string

The ID or name of the sending agent.

turn\_id: string

The ID of the turn that contains this item.

type: "agent\_message"

The item type. Always `agent_message`.

AgentMcpCallItem object { id, arguments, error, 6 more }

A call to a tool on an MCP server.

The ID of the MCP call item.

arguments: unknown

The arguments passed to the MCP tool.

error: unknown

The error returned by the MCP tool, if any.

The name of the MCP tool.

output: unknown

The output returned by the MCP tool, if any.

server\_label: string

The label of the MCP server.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the MCP tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "mcp\_call"

The item type. Always `mcp_call`.

AgentWebSearchCallItem object { id, action, status, 2 more }

A web search call produced by the agent.

The ID of the web search call.

action: [WebSearchAction](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20web_search_action%20%3E%20(schema)) or null

An action performed by the web search tool.

Search object { queries, query, type }

A search query or group of search queries.

queries: array of string or null

The search queries, when multiple queries were used.

query: string or null

The search query, when a single query was used.

type: "search"

The type of the object. Always `search`.

OpenPage object { type, url }

Opens a web page.

type: "open\_page"

The type of the object. Always `open_page`.

url: string or null

The URL of the page that was opened.

FindInPage object { pattern, type, url }

Finds text within a web page.

pattern: string or null

The text pattern that was searched for.

type: "find\_in\_page"

The type of the object. Always `find_in_page`.

url: string or null

The URL of the page that was searched.

Other object { type }

Another web search action.

type: "other"

The type of the object. Always `other`.

status: [AgentOutputItemStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_output_item_status%20%3E%20(schema))

The status of the web search call.

"in\_progress"

The item is in progress.

"completed"

The item is complete.

"incomplete"

The item stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "web\_search\_call"

The item type. Always `web_search_call`.

AgentCommandExecutionItem object { id, command, cwd, 6 more }

A command execution produced by the agent.

The ID of the command execution item.

command: string

The command that was executed.

cwd: string or null

The working directory used to execute the command.

duration\_ms: number or null

The command duration in milliseconds.

exit\_code: number or null

The process exit code, if the command completed.

output: string or null

The command output, if available.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the command execution.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "command\_execution"

The item type. Always `command_execution`.

AgentCreateSubagentCallItem object { id, agent\_id, content, 5 more }

A request to spawn a subagent.

The ID of the tool call item.

agent\_id: string

The ID of the agent that requested the subagent.

content: array of [AgentContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_content%20%3E%20(schema))

The task given to the spawned agent.

OutputText object { text, type }

A text content part produced by the agent.

text: string

The text produced by the agent.

type: "output\_text"

The content type. Always `output_text`.

EncryptedContent object { encrypted\_content, type }

Encrypted content exchanged between agents.

encrypted\_content: string

The encrypted content payload.

type: "encrypted\_content"

The content type. Always `encrypted_content`.

model: string or null

The model requested for the spawned agent.

reasoning\_effort: string or null

The reasoning effort requested for the spawned agent.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "create\_subagent\_call"

The item type. Always `create_subagent_call`.

AgentSendSubagentInputCallItem object { id, content, recipient\_agent\_id, 4 more }

A request to send input to another agent.

The ID of the tool call item.

content: array of [AgentContent](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_content%20%3E%20(schema))

The input sent to the receiving agent.

OutputText object { text, type }

A text content part produced by the agent.

text: string

The text produced by the agent.

type: "output\_text"

The content type. Always `output_text`.

EncryptedContent object { encrypted\_content, type }

Encrypted content exchanged between agents.

encrypted\_content: string

The encrypted content payload.

type: "encrypted\_content"

The content type. Always `encrypted_content`.

recipient\_agent\_id: string

The ID of the agent receiving the input.

sender\_agent\_id: string

The ID of the agent sending the input.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "send\_subagent\_input\_call"

The item type. Always `send_subagent_input_call`.

AgentResumeSubagentCallItem object { id, recipient\_agent\_id, sender\_agent\_id, 3 more }

A request to resume a subagent.

The ID of the tool call item.

recipient\_agent\_id: string

The ID of the agent to resume.

sender\_agent\_id: string

The ID of the agent requesting the resume.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "resume\_subagent\_call"

The item type. Always `resume_subagent_call`.

AgentWaitForSubagentsCallItem object { id, recipient\_agent\_ids, sender\_agent\_id, 3 more }

A request to wait for one or more subagents.

The ID of the tool call item.

recipient\_agent\_ids: array of string

The IDs of the agents to wait for.

sender\_agent\_id: string

The ID of the agent waiting for results.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "wait\_for\_subagents\_call"

The item type. Always `wait_for_subagents_call`.

AgentInterruptSubagentCallItem object { id, recipient\_agent\_id, sender\_agent\_id, 3 more }

A request to interrupt a subagent’s current turn. The subagent remains available.

The ID of the tool call item.

recipient\_agent\_id: string

The ID of the agent to interrupt.

sender\_agent\_id: string

The ID of the agent requesting the interrupt.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "interrupt\_subagent\_call"

The item type. Always `interrupt_subagent_call`.

AgentCloseSubagentCallItem object { id, recipient\_agent\_id, sender\_agent\_id, 3 more }

A request to close a subagent.

The ID of the tool call item.

recipient\_agent\_id: string

The ID of the agent to close.

sender\_agent\_id: string

The ID of the agent requesting the close.

status: [AgentFunctionCallStatus](/api/reference/resources/beta#(resource)%20beta.agents%20%3E%20(model)%20agent_function_call_status%20%3E%20(schema))

The status of the tool call.

"in\_progress"

The call is in progress.

"completed"

The call completed successfully.

"failed"

The call failed.

"incomplete"

The call stopped before completing.

turn\_id: string

The ID of the turn that contains this item.

type: "close\_subagent\_call"

The item type. Always `close_subagent_call`.

first\_id: string or null

The ID of the first resource in `data`, or `null` if the page is empty.

has\_more: boolean

Whether there are more resources to retrieve after this page.

last\_id: string or null

The ID of the last resource in `data`, or `null` if the page is empty. Pass this as `after` with the same order and filters.

object: "list"

The object type, which is always `list`.

### List agent session items

curl https://api.openai.com/v1/agents/sessions/$SESSION_ID/items \

  "data": [
      "content": [
          "text": "text",
          "type": "input_text"
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"

  "data": [
      "content": [
          "text": "text",
          "type": "input_text"
      ],
      "phase": "commentary",
      "role": "user",
      "status": "in_progress",
      "turn_id": "turn_id",
      "type": "message"
  ],
  "first_id": "first_id",
  "has_more": true,
  "last_id": "last_id",
  "object": "list"
