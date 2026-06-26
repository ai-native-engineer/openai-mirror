<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/assistants/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/resources/beta/subresources/assistants/methods/list)

Deprecated

GET/assistants

##### [Create assistant](/api/reference/resources/beta/subresources/assistants/methods/create)

Deprecated

POST/assistants

##### [Retrieve assistant](/api/reference/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/resources/beta/subresources/assistants/methods/update)

Deprecated

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/resources/beta/subresources/assistants/methods/delete)

Deprecated

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

Assistant object { id, created\_at, description, 10 more }

Represents an `assistant` that can call the model and use tools.

id: string

The identifier, which can be referenced in API endpoints.

created\_at: number

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

description: string

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: string

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models) for descriptions of them.

name: string

The name of the assistant. The maximum length is 256 characters.

maxLength256

object: "assistant"

The object type, which is always `assistant`.

tools: array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterTool object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool object { function, type }

function: [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

response\_format: optional [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

temperature: optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources: optional object { code\_interpreter, file\_search }

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: optional object { file\_ids }

file\_ids: optional array of string

A list of [file](/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

file\_search: optional object { vector\_store\_ids }

vector\_store\_ids: optional array of string

The ID of the [vector store](/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

top\_p: optional number

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

AssistantDeleted object { id, deleted, object }

id: string

deleted: boolean

object: "assistant.deleted"

AssistantStreamEvent = object { data, event, enabled }  or object { data, event }  or object { data, event }  or 22 more

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

event: thread.created
data: {"id": "thread_123", "object": "thread", ...}

We emit events whenever a new object is created, transitions to a new state, or is being
streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
to create a message during a run, we emit a `thread.message.created event`, a
`thread.message.in_progress` event, many `thread.message.delta` events, and finally a
`thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully
in your code. See the [Assistants API quickstart](/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

One of the following:

object { data, event, enabled }

Occurs when a new [thread](/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

event: "thread.created"

enabled: optional boolean

Whether to enable input audio transcription.

object { data, event }

Occurs when a new [run](/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.created"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.queued"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.in\_progress"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.requires\_action"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.completed"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.incomplete"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.failed"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.cancelling"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.cancelled"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.expired"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.created"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.in\_progress"

object { data, event }

Occurs when parts of a [run step](/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: "thread.run.step.delta"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.completed"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.failed"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.cancelled"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.expired"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.created"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.in\_progress"

object { data, event }

Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

event: "thread.message.delta"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.completed"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.incomplete"

ErrorEvent object { data, event }

Occurs when an [error](/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema)) { code, message, param, type }

event: "error"

DoneEvent object { data, event }

Occurs when a stream ends.

data: "[DONE]"

event: "done"

CodeInterpreterTool object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool object { function, type }

function: [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

MessageStreamEvent = object { data, event }  or object { data, event }  or object { data, event }  or 2 more

Occurs when a [message](/docs/api-reference/messages/object) is created.

One of the following:

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.created"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.in\_progress"

object { data, event }

Occurs when parts of a [Message](/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a message delta i.e. any changed fields on a message during streaming.

event: "thread.message.delta"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.completed"

object { data, event }

Occurs when a [message](/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) { id, assistant\_id, attachments, 11 more }

Represents a message within a [thread](/docs/api-reference/threads).

event: "thread.message.incomplete"

RunStepStreamEvent = object { data, event }  or object { data, event }  or object { data, event }  or 4 more

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

One of the following:

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.created"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.in\_progress"

object { data, event }

Occurs when parts of a [run step](/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: "thread.run.step.delta"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.completed"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.failed"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.cancelled"

object { data, event }

Occurs when a [run step](/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

event: "thread.run.step.expired"

RunStreamEvent = object { data, event }  or object { data, event }  or object { data, event }  or 7 more

Occurs when a new [run](/docs/api-reference/runs/object) is created.

One of the following:

object { data, event }

Occurs when a new [run](/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.created"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.queued"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.in\_progress"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.requires\_action"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.completed"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.incomplete"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.failed"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.cancelling"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.cancelled"

object { data, event }

Occurs when a [run](/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

event: "thread.run.expired"

ThreadStreamEvent object { data, event, enabled }

Occurs when a new [thread](/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) { id, created\_at, metadata, 2 more }

Represents a thread that contains [messages](/docs/api-reference/messages).

event: "thread.created"

enabled: optional boolean

Whether to enable input audio transcription.
