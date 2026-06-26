<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/assistants/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/python/resources/beta/subresources/assistants/methods/list)

Deprecated

beta.assistants.list(AssistantListParams\*\*kwargs)  -> SyncCursorPage[[Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))]

GET/assistants

##### [Create assistant](/api/reference/python/resources/beta/subresources/assistants/methods/create)

Deprecated

beta.assistants.create(AssistantCreateParams\*\*kwargs)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

POST/assistants

##### [Retrieve assistant](/api/reference/python/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

beta.assistants.retrieve(strassistant\_id)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/python/resources/beta/subresources/assistants/methods/update)

Deprecated

beta.assistants.update(strassistant\_id, AssistantUpdateParams\*\*kwargs)  -> [Assistant](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/python/resources/beta/subresources/assistants/methods/delete)

Deprecated

beta.assistants.delete(strassistant\_id)  -> [AssistantDeleted](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema))

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

class Assistant: …

Represents an `assistant` that can call the model and use tools.

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

description: Optional[str]

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: Optional[str]

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

name: Optional[str]

The name of the assistant. The maximum length is 256 characters.

maxLength256

object: Literal["assistant"]

The object type, which is always `assistant`.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources: Optional[ToolResources]

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[List[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[List[str]]

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

class AssistantDeleted: …

id: str

deleted: bool

object: Literal["assistant.deleted"]

[AssistantStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))

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
in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

One of the following:

class ThreadCreated: …

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: Literal["thread.created"]

enabled: Optional[bool]

Whether to enable input audio transcription.

class ThreadRunCreated: …

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.created"]

class ThreadRunQueued: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.queued"]

class ThreadRunInProgress: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.in\_progress"]

class ThreadRunRequiresAction: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.requires\_action"]

class ThreadRunCompleted: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.completed"]

class ThreadRunIncomplete: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.incomplete"]

class ThreadRunFailed: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.failed"]

class ThreadRunCancelling: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelling"]

class ThreadRunCancelled: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelled"]

class ThreadRunExpired: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.expired"]

class ThreadRunStepCreated: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.created"]

class ThreadRunStepInProgress: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.in\_progress"]

class ThreadRunStepDelta: …

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: Literal["thread.run.step.delta"]

class ThreadRunStepCompleted: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.completed"]

class ThreadRunStepFailed: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.failed"]

class ThreadRunStepCancelled: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.cancelled"]

class ThreadRunStepExpired: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.expired"]

class ThreadMessageCreated: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.created"]

class ThreadMessageInProgress: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.in\_progress"]

class ThreadMessageDelta: …

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

event: Literal["thread.message.delta"]

class ThreadMessageCompleted: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.completed"]

class ThreadMessageIncomplete: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.incomplete"]

class ErrorEvent: …

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema))

event: Literal["error"]

[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of tool being defined: `function`

[MessageStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20message_stream_event%20%3E%20(schema))

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

One of the following:

class ThreadMessageCreated: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.created"]

class ThreadMessageInProgress: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.in\_progress"]

class ThreadMessageDelta: …

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

event: Literal["thread.message.delta"]

class ThreadMessageCompleted: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.completed"]

class ThreadMessageIncomplete: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.message.incomplete"]

[RunStepStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20run_step_stream_event%20%3E%20(schema))

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

One of the following:

class ThreadRunStepCreated: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.created"]

class ThreadRunStepInProgress: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.in\_progress"]

class ThreadRunStepDelta: …

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

event: Literal["thread.run.step.delta"]

class ThreadRunStepCompleted: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.completed"]

class ThreadRunStepFailed: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.failed"]

class ThreadRunStepCancelled: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.cancelled"]

class ThreadRunStepExpired: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

event: Literal["thread.run.step.expired"]

[RunStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20run_stream_event%20%3E%20(schema))

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

One of the following:

class ThreadRunCreated: …

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.created"]

class ThreadRunQueued: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.queued"]

class ThreadRunInProgress: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.in\_progress"]

class ThreadRunRequiresAction: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.requires\_action"]

class ThreadRunCompleted: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.completed"]

class ThreadRunIncomplete: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.incomplete"]

class ThreadRunFailed: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.failed"]

class ThreadRunCancelling: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelling"]

class ThreadRunCancelled: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.cancelled"]

class ThreadRunExpired: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

event: Literal["thread.run.expired"]

class ThreadStreamEvent: …

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

event: Literal["thread.created"]

enabled: Optional[bool]

Whether to enable input audio transcription.
