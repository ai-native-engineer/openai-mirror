<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/runs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Runs

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

RunListPage beta().threads().runs().list(RunListParamsparams = RunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) beta().threads().runs().create(RunCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) beta().threads().runs().retrieve(RunRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) beta().threads().runs().update(RunUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) beta().threads().runs().submitToolOutputs(RunSubmitToolOutputsParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

[Run](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) beta().threads().runs().cancel(RunCancelParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

class RequiredActionFunctionToolCall:

Tool call objects

String id

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function function

The function definition.

String arguments

The arguments that the model expects you to pass to the function.

String name

The name of the function.

JsonValue; type "function"constant"function"constant

The type of tool call the output is required for. For now, this is always `function`.

class Run:

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

String id

The identifier, which can be referenced in API endpoints.

String assistantId

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

Optional<Long> cancelledAt

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

Optional<Long> completedAt

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

long createdAt

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

Optional<Long> expiresAt

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

Optional<Long> failedAt

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

Optional<IncompleteDetails> incompleteDetails

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

Optional<Reason> reason

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

MAX\_COMPLETION\_TOKENS("max\_completion\_tokens")

MAX\_PROMPT\_TOKENS("max\_prompt\_tokens")

String instructions

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

Optional<LastError> lastError

The last error associated with this run. Will be `null` if there are no errors.

Code code

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

INVALID\_PROMPT("invalid\_prompt")

String message

A human-readable description of the error.

Optional<Long> maxCompletionTokens

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

Optional<Long> maxPromptTokens

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String model

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

JsonValue; object\_ "thread.run"constant"thread.run"constant

The object type, which is always `thread.run`.

boolean parallelToolCalls

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

Optional<RequiredAction> requiredAction

Details on the action required to continue the run. Will be `null` if no action is required.

SubmitToolOutputs submitToolOutputs

Details on the tool outputs needed for this run to continue.

List<[RequiredActionFunctionToolCall](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))> toolCalls

A list of the relevant tool calls.

String id

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function function

The function definition.

String arguments

The arguments that the model expects you to pass to the function.

String name

The name of the function.

JsonValue; type "function"constant"function"constant

The type of tool call the output is required for. For now, this is always `function`.

JsonValue; type "submit\_tool\_outputs"constant"submit\_tool\_outputs"constant

For now, this is always `submit_tool_outputs`.

Optional<[AssistantResponseFormatOption](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))> responseFormat

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

Optional<Long> startedAt

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

[RunStatus](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) status

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

String threadId

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

Optional<[AssistantToolChoiceOption](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))> toolChoice

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

List<[AssistantTool](/api/reference/java/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))> tools

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

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

Optional<TruncationStrategy> truncationStrategy

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

Type type

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

AUTO("auto")

LAST\_MESSAGES("last\_messages")

Optional<Long> lastMessages

The number of most recent messages from the thread when constructing the context for the run.

minimum1

Optional<Usage> usage

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

long completionTokens

Number of completion tokens used over the course of the run.

long promptTokens

Number of prompt tokens used over the course of the run.

long totalTokens

Total number of tokens used (prompt + completion).

Optional<Double> temperature

The sampling temperature used for this run. If not set, defaults to 1.

Optional<Double> topP

The nucleus sampling value used for this run. If not set, defaults to 1.

enum RunStatus:

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

QUEUED("queued")

IN\_PROGRESS("in\_progress")

REQUIRES\_ACTION("requires\_action")

CANCELLING("cancelling")

CANCELLED("cancelled")

FAILED("failed")

COMPLETED("completed")

INCOMPLETE("incomplete")

EXPIRED("expired")

#### RunsSteps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/java/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

StepListPage beta().threads().runs().steps().list(StepListParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/java/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

[RunStep](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) beta().threads().runs().steps().retrieve(StepRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

class CodeInterpreterLogs:

Text output from the Code Interpreter tool call as part of a run step.

long index

The index of the output in the outputs array.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

Optional<String> logs

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage:

long index

The index of the output in the outputs array.

JsonValue; type "image"constant"image"constant

Always `image`.

Optional<Image> image

Optional<String> fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class CodeInterpreterToolCall:

Details of the Code Interpreter tool call the run step was involved in.

String id

The ID of the tool call.

CodeInterpreter codeInterpreter

The Code Interpreter tool call definition.

String input

The input to the Code Interpreter tool call.

List<Output> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class LogsOutput:

Text output from the Code Interpreter tool call as part of a run step.

String logs

The text output from the Code Interpreter tool call.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

class ImageOutput:

Image image

String fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

JsonValue; type "image"constant"image"constant

Always `image`.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class CodeInterpreterToolCallDelta:

Details of the Code Interpreter tool call the run step was involved in.

long index

The index of the tool call in the tool calls array.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

Optional<String> id

The ID of the tool call.

Optional<CodeInterpreter> codeInterpreter

The Code Interpreter tool call definition.

Optional<String> input

The input to the Code Interpreter tool call.

Optional<List<Output>> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs:

Text output from the Code Interpreter tool call as part of a run step.

long index

The index of the output in the outputs array.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

Optional<String> logs

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage:

long index

The index of the output in the outputs array.

JsonValue; type "image"constant"image"constant

Always `image`.

Optional<Image> image

Optional<String> fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCall:

String id

The ID of the tool call object.

FileSearch fileSearch

For now, this is always going to be an empty object.

Optional<RankingOptions> rankingOptions

The ranking options for the file search.

Ranker ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Result>> results

The results of the file search.

String fileId

The ID of the file that result was found in.

String fileName

The name of the file that result was found in.

double score

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Content>> content

The content of the result that was found. The content is only included if requested via the include query parameter.

Optional<String> text

The text content of the file.

Optional<Type> type

The type of the content.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FileSearchToolCallDelta:

JsonValue fileSearch

For now, this is always going to be an empty object.

long index

The index of the tool call in the tool calls array.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

Optional<String> id

The ID of the tool call object.

class FunctionToolCall:

String id

The ID of the tool call object.

Function function

The definition of the function that was called.

String arguments

The arguments passed to the function.

String name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

class FunctionToolCallDelta:

long index

The index of the tool call in the tool calls array.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

Optional<String> id

The ID of the tool call object.

Optional<Function> function

The definition of the function that was called.

Optional<String> arguments

The arguments passed to the function.

Optional<String> name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class MessageCreationStepDetails:

Details of the message creation by the run step.

MessageCreation messageCreation

String messageId

The ID of the message that was created by this run step.

JsonValue; type "message\_creation"constant"message\_creation"constant

Always `message_creation`.

class RunStep:

Represents a step in execution of a run.

String id

The identifier of the run step, which can be referenced in API endpoints.

String assistantId

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

Optional<Long> cancelledAt

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

Optional<Long> completedAt

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

long createdAt

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

Optional<Long> expiredAt

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

Optional<Long> failedAt

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

Optional<LastError> lastError

The last error associated with this run step. Will be `null` if there are no errors.

Code code

One of `server_error` or `rate_limit_exceeded`.

One of the following:

SERVER\_ERROR("server\_error")

RATE\_LIMIT\_EXCEEDED("rate\_limit\_exceeded")

String message

A human-readable description of the error.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

JsonValue; object\_ "thread.run.step"constant"thread.run.step"constant

The object type, which is always `thread.run.step`.

String runId

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

Status status

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

IN\_PROGRESS("in\_progress")

CANCELLED("cancelled")

FAILED("failed")

COMPLETED("completed")

EXPIRED("expired")

StepDetails stepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails:

Details of the message creation by the run step.

MessageCreation messageCreation

String messageId

The ID of the message that was created by this run step.

JsonValue; type "message\_creation"constant"message\_creation"constant

Always `message_creation`.

class ToolCallsStepDetails:

Details of the tool call.

List<[ToolCall](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))> toolCalls

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall:

Details of the Code Interpreter tool call the run step was involved in.

String id

The ID of the tool call.

CodeInterpreter codeInterpreter

The Code Interpreter tool call definition.

String input

The input to the Code Interpreter tool call.

List<Output> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class LogsOutput:

Text output from the Code Interpreter tool call as part of a run step.

String logs

The text output from the Code Interpreter tool call.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

class ImageOutput:

Image image

String fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

JsonValue; type "image"constant"image"constant

Always `image`.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall:

String id

The ID of the tool call object.

FileSearch fileSearch

For now, this is always going to be an empty object.

Optional<RankingOptions> rankingOptions

The ranking options for the file search.

Ranker ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Result>> results

The results of the file search.

String fileId

The ID of the file that result was found in.

String fileName

The name of the file that result was found in.

double score

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Content>> content

The content of the result that was found. The content is only included if requested via the include query parameter.

Optional<String> text

The text content of the file.

Optional<Type> type

The type of the content.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall:

String id

The ID of the tool call object.

Function function

The definition of the function that was called.

String arguments

The arguments passed to the function.

String name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

JsonValue; type "tool\_calls"constant"tool\_calls"constant

Always `tool_calls`.

String threadId

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

Type type

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

MESSAGE\_CREATION("message\_creation")

TOOL\_CALLS("tool\_calls")

Optional<Usage> usage

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

long completionTokens

Number of completion tokens used over the course of the run step.

long promptTokens

Number of prompt tokens used over the course of the run step.

long totalTokens

Total number of tokens used (prompt + completion).

class RunStepDelta:

The delta containing the fields that have changed on the run step.

Optional<StepDetails> stepDetails

The details of the run step.

One of the following:

class RunStepDeltaMessageDelta:

Details of the message creation by the run step.

JsonValue; type "message\_creation"constant"message\_creation"constant

Always `message_creation`.

Optional<MessageCreation> messageCreation

Optional<String> messageId

The ID of the message that was created by this run step.

class ToolCallDeltaObject:

Details of the tool call.

JsonValue; type "tool\_calls"constant"tool\_calls"constant

Always `tool_calls`.

Optional<List<[ToolCallDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>> toolCalls

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta:

Details of the Code Interpreter tool call the run step was involved in.

long index

The index of the tool call in the tool calls array.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

Optional<String> id

The ID of the tool call.

Optional<CodeInterpreter> codeInterpreter

The Code Interpreter tool call definition.

Optional<String> input

The input to the Code Interpreter tool call.

Optional<List<Output>> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs:

Text output from the Code Interpreter tool call as part of a run step.

long index

The index of the output in the outputs array.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

Optional<String> logs

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage:

long index

The index of the output in the outputs array.

JsonValue; type "image"constant"image"constant

Always `image`.

Optional<Image> image

Optional<String> fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta:

JsonValue fileSearch

For now, this is always going to be an empty object.

long index

The index of the tool call in the tool calls array.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

Optional<String> id

The ID of the tool call object.

class FunctionToolCallDelta:

long index

The index of the tool call in the tool calls array.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

Optional<String> id

The ID of the tool call object.

Optional<Function> function

The definition of the function that was called.

Optional<String> arguments

The arguments passed to the function.

Optional<String> name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class RunStepDeltaEvent:

Represents a run step delta i.e. any changed fields on a run step during streaming.

String id

The identifier of the run step, which can be referenced in API endpoints.

[RunStepDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema)) delta

The delta containing the fields that have changed on the run step.

JsonValue; object\_ "thread.run.step.delta"constant"thread.run.step.delta"constant

The object type, which is always `thread.run.step.delta`.

class RunStepDeltaMessageDelta:

Details of the message creation by the run step.

JsonValue; type "message\_creation"constant"message\_creation"constant

Always `message_creation`.

Optional<MessageCreation> messageCreation

Optional<String> messageId

The ID of the message that was created by this run step.

enum RunStepInclude:

STEP\_DETAILS\_TOOL\_CALLS\_FILE\_SEARCH\_RESULTS\_CONTENT("step\_details.tool\_calls[\*].file\_search.results[\*].content")

class ToolCall: A class that can be one of several variants.union

Details of the Code Interpreter tool call the run step was involved in.

class CodeInterpreterToolCall:

Details of the Code Interpreter tool call the run step was involved in.

String id

The ID of the tool call.

CodeInterpreter codeInterpreter

The Code Interpreter tool call definition.

String input

The input to the Code Interpreter tool call.

List<Output> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class LogsOutput:

Text output from the Code Interpreter tool call as part of a run step.

String logs

The text output from the Code Interpreter tool call.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

class ImageOutput:

Image image

String fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

JsonValue; type "image"constant"image"constant

Always `image`.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall:

String id

The ID of the tool call object.

FileSearch fileSearch

For now, this is always going to be an empty object.

Optional<RankingOptions> rankingOptions

The ranking options for the file search.

Ranker ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Result>> results

The results of the file search.

String fileId

The ID of the file that result was found in.

String fileName

The name of the file that result was found in.

double score

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Content>> content

The content of the result that was found. The content is only included if requested via the include query parameter.

Optional<String> text

The text content of the file.

Optional<Type> type

The type of the content.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall:

String id

The ID of the tool call object.

Function function

The definition of the function that was called.

String arguments

The arguments passed to the function.

String name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

class ToolCallDelta: A class that can be one of several variants.union

Details of the Code Interpreter tool call the run step was involved in.

class CodeInterpreterToolCallDelta:

Details of the Code Interpreter tool call the run step was involved in.

long index

The index of the tool call in the tool calls array.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

Optional<String> id

The ID of the tool call.

Optional<CodeInterpreter> codeInterpreter

The Code Interpreter tool call definition.

Optional<String> input

The input to the Code Interpreter tool call.

Optional<List<Output>> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs:

Text output from the Code Interpreter tool call as part of a run step.

long index

The index of the output in the outputs array.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

Optional<String> logs

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage:

long index

The index of the output in the outputs array.

JsonValue; type "image"constant"image"constant

Always `image`.

Optional<Image> image

Optional<String> fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta:

JsonValue fileSearch

For now, this is always going to be an empty object.

long index

The index of the tool call in the tool calls array.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

Optional<String> id

The ID of the tool call object.

class FunctionToolCallDelta:

long index

The index of the tool call in the tool calls array.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

Optional<String> id

The ID of the tool call object.

Optional<Function> function

The definition of the function that was called.

Optional<String> arguments

The arguments passed to the function.

Optional<String> name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallDeltaObject:

Details of the tool call.

JsonValue; type "tool\_calls"constant"tool\_calls"constant

Always `tool_calls`.

Optional<List<[ToolCallDelta](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>> toolCalls

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta:

Details of the Code Interpreter tool call the run step was involved in.

long index

The index of the tool call in the tool calls array.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

Optional<String> id

The ID of the tool call.

Optional<CodeInterpreter> codeInterpreter

The Code Interpreter tool call definition.

Optional<String> input

The input to the Code Interpreter tool call.

Optional<List<Output>> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs:

Text output from the Code Interpreter tool call as part of a run step.

long index

The index of the output in the outputs array.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

Optional<String> logs

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage:

long index

The index of the output in the outputs array.

JsonValue; type "image"constant"image"constant

Always `image`.

Optional<Image> image

Optional<String> fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta:

JsonValue fileSearch

For now, this is always going to be an empty object.

long index

The index of the tool call in the tool calls array.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

Optional<String> id

The ID of the tool call object.

class FunctionToolCallDelta:

long index

The index of the tool call in the tool calls array.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

Optional<String> id

The ID of the tool call object.

Optional<Function> function

The definition of the function that was called.

Optional<String> arguments

The arguments passed to the function.

Optional<String> name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallsStepDetails:

Details of the tool call.

List<[ToolCall](/api/reference/java/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))> toolCalls

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall:

Details of the Code Interpreter tool call the run step was involved in.

String id

The ID of the tool call.

CodeInterpreter codeInterpreter

The Code Interpreter tool call definition.

String input

The input to the Code Interpreter tool call.

List<Output> outputs

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class LogsOutput:

Text output from the Code Interpreter tool call as part of a run step.

String logs

The text output from the Code Interpreter tool call.

JsonValue; type "logs"constant"logs"constant

Always `logs`.

class ImageOutput:

Image image

String fileId

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

JsonValue; type "image"constant"image"constant

Always `image`.

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall:

String id

The ID of the tool call object.

FileSearch fileSearch

For now, this is always going to be an empty object.

Optional<RankingOptions> rankingOptions

The ranking options for the file search.

Ranker ranker

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

AUTO("auto")

DEFAULT\_2024\_08\_21("default\_2024\_08\_21")

double scoreThreshold

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Result>> results

The results of the file search.

String fileId

The ID of the file that result was found in.

String fileName

The name of the file that result was found in.

double score

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Optional<List<Content>> content

The content of the result that was found. The content is only included if requested via the include query parameter.

Optional<String> text

The text content of the file.

Optional<Type> type

The type of the content.

JsonValue; type "file\_search"constant"file\_search"constant

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall:

String id

The ID of the tool call object.

Function function

The definition of the function that was called.

String arguments

The arguments passed to the function.

String name

The name of the function.

Optional<String> output

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

JsonValue; type "function"constant"function"constant

The type of tool call. This is always going to be `function` for this type of tool call.

JsonValue; type "tool\_calls"constant"tool\_calls"constant

Always `tool_calls`.
