<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/assistants/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Assistants

Build Assistants that can call models and use tools.

##### [List assistants](/api/reference/java/resources/beta/subresources/assistants/methods/list)

Deprecated

AssistantListPage beta().assistants().list(AssistantListParamsparams = AssistantListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/assistants

##### [Create assistant](/api/reference/java/resources/beta/subresources/assistants/methods/create)

Deprecated

[Assistant](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) beta().assistants().create(AssistantCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/assistants

##### [Retrieve assistant](/api/reference/java/resources/beta/subresources/assistants/methods/retrieve)

Deprecated

[Assistant](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) beta().assistants().retrieve(AssistantRetrieveParamsparams = AssistantRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/assistants/{assistant\_id}

##### [Modify assistant](/api/reference/java/resources/beta/subresources/assistants/methods/update)

Deprecated

[Assistant](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) beta().assistants().update(AssistantUpdateParamsparams = AssistantUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/assistants/{assistant\_id}

##### [Delete assistant](/api/reference/java/resources/beta/subresources/assistants/methods/delete)

Deprecated

[AssistantDeleted](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_deleted%20%3E%20(schema)) beta().assistants().delete(AssistantDeleteParamsparams = AssistantDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/assistants/{assistant\_id}

##### ModelsExpand Collapse

class Assistant:

Represents an `assistant` that can call the model and use tools.

String id

The identifier, which can be referenced in API endpoints.

long createdAt

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

Optional<String> description

The description of the assistant. The maximum length is 512 characters.

maxLength512

Optional<String> instructions

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String model

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

Optional<String> name

The name of the assistant. The maximum length is 256 characters.

maxLength256

JsonValue; object\_ "assistant"constant"assistant"constant

The object type, which is always `assistant`.

List<[AssistantTool](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))> tools

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterTool:

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool being defined: `code_interpreter`

class FileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool being defined: `file_search`

Optional<FileSearch> fileSearch

Overrides for the file search tool.

Optional<Long> maxNumResults

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

Optional<RankingOptions> rankingOptions

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<Ranker> ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

class FunctionTool:

[FunctionDefinition](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) function

JsonValue; type "function"constant"function"constant

The type of tool being defined: `function`

Optional<[AssistantResponseFormatOption](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))> responseFormat

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

Optional<ToolResources> toolResources

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

Optional<CodeInterpreter> codeInterpreter

Optional<List<String>> fileIds

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

Optional<FileSearch> fileSearch

Optional<List<String>> vectorStoreIds

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

class AssistantDeleted:

String id

boolean deleted

JsonValue; object\_ "assistant.deleted"constant"assistant.deleted"constant

class AssistantStreamEvent: A class that can be one of several variants.union

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

ThreadCreated

[Thread](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) data

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

JsonValue; event "thread.created"constant"thread.created"constant

Optional<Boolean> enabled

Whether to enable input audio transcription.

ThreadRunCreated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.created"constant"thread.run.created"constant

ThreadRunQueued

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.queued"constant"thread.run.queued"constant

ThreadRunInProgress

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.in\_progress"constant"thread.run.in\_progress"constant

ThreadRunRequiresAction

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.requires\_action"constant"thread.run.requires\_action"constant

ThreadRunCompleted

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.completed"constant"thread.run.completed"constant

ThreadRunIncomplete

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.incomplete"constant"thread.run.incomplete"constant

ThreadRunFailed

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.failed"constant"thread.run.failed"constant

ThreadRunCancelling

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.cancelling"constant"thread.run.cancelling"constant

ThreadRunCancelled

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.cancelled"constant"thread.run.cancelled"constant

ThreadRunExpired

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.expired"constant"thread.run.expired"constant

ThreadRunStepCreated

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.created"constant"thread.run.step.created"constant

ThreadRunStepInProgress

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.in\_progress"constant"thread.run.step.in\_progress"constant

ThreadRunStepDelta

[RunStepDeltaEvent](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) data

Represents a run step delta i.e. any changed fields on a run step during streaming.

JsonValue; event "thread.run.step.delta"constant"thread.run.step.delta"constant

ThreadRunStepCompleted

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.completed"constant"thread.run.step.completed"constant

ThreadRunStepFailed

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.failed"constant"thread.run.step.failed"constant

ThreadRunStepCancelled

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.cancelled"constant"thread.run.step.cancelled"constant

ThreadRunStepExpired

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.expired"constant"thread.run.step.expired"constant

ThreadMessageCreated

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.created"constant"thread.message.created"constant

ThreadMessageInProgress

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.in\_progress"constant"thread.message.in\_progress"constant

ThreadMessageDelta

[MessageDeltaEvent](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) data

Represents a message delta i.e. any changed fields on a message during streaming.

JsonValue; event "thread.message.delta"constant"thread.message.delta"constant

ThreadMessageCompleted

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.completed"constant"thread.message.completed"constant

ThreadMessageIncomplete

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.incomplete"constant"thread.message.incomplete"constant

ErrorEvent

[ErrorObject](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema)) data

JsonValue; event "error"constant"error"constant

class AssistantTool: A class that can be one of several variants.union

class CodeInterpreterTool:

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool being defined: `code_interpreter`

class FileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool being defined: `file_search`

Optional<FileSearch> fileSearch

Overrides for the file search tool.

Optional<Long> maxNumResults

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

Optional<RankingOptions> rankingOptions

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<Ranker> ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

class FunctionTool:

[FunctionDefinition](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) function

JsonValue; type "function"constant"function"constant

The type of tool being defined: `function`

class CodeInterpreterTool:

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool being defined: `code_interpreter`

class FileSearchTool:

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool being defined: `file_search`

Optional<FileSearch> fileSearch

Overrides for the file search tool.

Optional<Long> maxNumResults

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

Optional<RankingOptions> rankingOptions

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<Ranker> ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

class FunctionTool:

[FunctionDefinition](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) function

JsonValue; type "function"constant"function"constant

The type of tool being defined: `function`

class MessageStreamEvent: A class that can be one of several variants.union

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

ThreadMessageCreated

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.created"constant"thread.message.created"constant

ThreadMessageInProgress

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.in\_progress"constant"thread.message.in\_progress"constant

ThreadMessageDelta

[MessageDeltaEvent](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema)) data

Represents a message delta i.e. any changed fields on a message during streaming.

JsonValue; event "thread.message.delta"constant"thread.message.delta"constant

ThreadMessageCompleted

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.completed"constant"thread.message.completed"constant

ThreadMessageIncomplete

[Message](/api/reference/java/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema)) data

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.message.incomplete"constant"thread.message.incomplete"constant

class RunStepStreamEvent: A class that can be one of several variants.union

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

ThreadRunStepCreated

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.created"constant"thread.run.step.created"constant

ThreadRunStepInProgress

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.in\_progress"constant"thread.run.step.in\_progress"constant

ThreadRunStepDelta

[RunStepDeltaEvent](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema)) data

Represents a run step delta i.e. any changed fields on a run step during streaming.

JsonValue; event "thread.run.step.delta"constant"thread.run.step.delta"constant

ThreadRunStepCompleted

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.completed"constant"thread.run.step.completed"constant

ThreadRunStepFailed

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.failed"constant"thread.run.step.failed"constant

ThreadRunStepCancelled

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.cancelled"constant"thread.run.step.cancelled"constant

ThreadRunStepExpired

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) data

Represents a step in execution of a run.

JsonValue; event "thread.run.step.expired"constant"thread.run.step.expired"constant

class RunStreamEvent: A class that can be one of several variants.union

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

ThreadRunCreated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.created"constant"thread.run.created"constant

ThreadRunQueued

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.queued"constant"thread.run.queued"constant

ThreadRunInProgress

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.in\_progress"constant"thread.run.in\_progress"constant

ThreadRunRequiresAction

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.requires\_action"constant"thread.run.requires\_action"constant

ThreadRunCompleted

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.completed"constant"thread.run.completed"constant

ThreadRunIncomplete

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.incomplete"constant"thread.run.incomplete"constant

ThreadRunFailed

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.failed"constant"thread.run.failed"constant

ThreadRunCancelling

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.cancelling"constant"thread.run.cancelling"constant

ThreadRunCancelled

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.cancelled"constant"thread.run.cancelled"constant

ThreadRunExpired

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) data

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

JsonValue; event "thread.run.expired"constant"thread.run.expired"constant

class ThreadStreamEvent:

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

[Thread](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema)) data

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

JsonValue; event "thread.created"constant"thread.created"constant

Optional<Boolean> enabled

Whether to enable input audio transcription.
