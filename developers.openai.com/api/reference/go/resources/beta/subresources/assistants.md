<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/assistants/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/go/resources/beta/subresources/assistants/methods/list)

Deprecated

client.Beta.Assistants.List(ctx, query) (\*CursorPage[[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema))], error)

GET/assistants

##### [Create assistant](/api/reference/go/resources/beta/subresources/assistants/methods/create)

Deprecated

client.Beta.Assistants.New(ctx, body) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

POST/assistants

##### [Retrieve assistant](/api/reference/go/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

client.Beta.Assistants.Get(ctx, assistantID) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/go/resources/beta/subresources/assistants/methods/update)

Deprecated

client.Beta.Assistants.Update(ctx, assistantID, body) (\*[Assistant](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)), error)

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/go/resources/beta/subresources/assistants/methods/delete)

Deprecated

client.Beta.Assistants.Delete(ctx, assistantID) (\*[AssistantDeleted](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)), error)

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

type Assistant struct{…}

Represents an `assistant` that can call the model and use tools.

ID string

The identifier, which can be referenced in API endpoints.

CreatedAt int64

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

Description string

The description of the assistant. The maximum length is 512 characters.

maxLength512

Instructions string

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model string

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

Name string

The name of the assistant. The maximum length is 256 characters.

maxLength256

Object Assistant

The object type, which is always `assistant`.

Tools [][AssistantToolUnion](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

ResponseFormat [AssistantResponseFormatOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))Optional

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Temperature float64Optional

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

ToolResources AssistantToolResourcesOptional

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

CodeInterpreter AssistantToolResourcesCodeInterpreterOptional

FileIDs []stringOptional

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

FileSearch AssistantToolResourcesFileSearchOptional

VectorStoreIDs []stringOptional

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

TopP float64Optional

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

type AssistantDeleted struct{…}

ID string

Deleted bool

Object AssistantDeleted

type AssistantStreamEventUnion interface{…}

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

type AssistantStreamEventThreadCreated struct{…}

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

Data [Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

Event ThreadCreated

Enabled boolOptional

Whether to enable input audio transcription.

type AssistantStreamEventThreadRunCreated struct{…}

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCreated

type AssistantStreamEventThreadRunQueued struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunQueued

type AssistantStreamEventThreadRunInProgress struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunInProgress

type AssistantStreamEventThreadRunRequiresAction struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunRequiresAction

type AssistantStreamEventThreadRunCompleted struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCompleted

type AssistantStreamEventThreadRunIncomplete struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunIncomplete

type AssistantStreamEventThreadRunFailed struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunFailed

type AssistantStreamEventThreadRunCancelling struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelling

type AssistantStreamEventThreadRunCancelled struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelled

type AssistantStreamEventThreadRunExpired struct{…}

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunExpired

type AssistantStreamEventThreadRunStepCreated struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCreated

type AssistantStreamEventThreadRunStepInProgress struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepInProgress

type AssistantStreamEventThreadRunStepDelta struct{…}

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

Data [RunStepDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

Event ThreadRunStepDelta

type AssistantStreamEventThreadRunStepCompleted struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCompleted

type AssistantStreamEventThreadRunStepFailed struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepFailed

type AssistantStreamEventThreadRunStepCancelled struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCancelled

type AssistantStreamEventThreadRunStepExpired struct{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepExpired

type AssistantStreamEventThreadMessageCreated struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCreated

type AssistantStreamEventThreadMessageInProgress struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageInProgress

type AssistantStreamEventThreadMessageDelta struct{…}

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

Data [MessageDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

Event ThreadMessageDelta

type AssistantStreamEventThreadMessageCompleted struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCompleted

type AssistantStreamEventThreadMessageIncomplete struct{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageIncomplete

type AssistantStreamEventErrorEvent struct{…}

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

Data [ErrorObject](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema))

Event Error

type AssistantToolUnion interface{…}

One of the following:

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

type CodeInterpreterTool struct{…}

Type CodeInterpreter

The type of tool being defined: `code_interpreter`

type FileSearchTool struct{…}

Type FileSearch

The type of tool being defined: `file_search`

FileSearch FileSearchToolFileSearchOptional

Overrides for the file search tool.

MaxNumResults int64Optional

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

RankingOptions FileSearchToolFileSearchRankingOptionsOptional

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Ranker stringOptional

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolFileSearchRankingOptionsRankerAuto FileSearchToolFileSearchRankingOptionsRanker = "auto"

const FileSearchToolFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

type FunctionTool struct{…}

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of tool being defined: `function`

type MessageStreamEventUnion interface{…}

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

One of the following:

MessageStreamEventThreadMessageCreated

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCreated

MessageStreamEventThreadMessageInProgress

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageInProgress

MessageStreamEventThreadMessageDelta

Data [MessageDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

Event ThreadMessageDelta

MessageStreamEventThreadMessageCompleted

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageCompleted

MessageStreamEventThreadMessageIncomplete

Data [Message](/api/reference/go/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadMessageIncomplete

type RunStepStreamEventUnion interface{…}

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

One of the following:

RunStepStreamEventThreadRunStepCreated

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCreated

RunStepStreamEventThreadRunStepInProgress

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepInProgress

RunStepStreamEventThreadRunStepDelta

Data [RunStepDeltaEvent](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

Event ThreadRunStepDelta

RunStepStreamEventThreadRunStepCompleted

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCompleted

RunStepStreamEventThreadRunStepFailed

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepFailed

RunStepStreamEventThreadRunStepCancelled

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepCancelled

RunStepStreamEventThreadRunStepExpired

Data [RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

Event ThreadRunStepExpired

type RunStreamEventUnion interface{…}

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

One of the following:

RunStreamEventThreadRunCreated

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCreated

RunStreamEventThreadRunQueued

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunQueued

RunStreamEventThreadRunInProgress

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunInProgress

RunStreamEventThreadRunRequiresAction

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunRequiresAction

RunStreamEventThreadRunCompleted

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCompleted

RunStreamEventThreadRunIncomplete

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunIncomplete

RunStreamEventThreadRunFailed

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunFailed

RunStreamEventThreadRunCancelling

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelling

RunStreamEventThreadRunCancelled

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunCancelled

RunStreamEventThreadRunExpired

Data [Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

Event ThreadRunExpired

type ThreadStreamEvent struct{…}

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

Data [Thread](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

Event ThreadCreated

Enabled boolOptional

Whether to enable input audio transcription.
