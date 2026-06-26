<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/runs/subresources/steps/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Beta](/api/reference/java/resources/beta)

[Threads](/api/reference/java/resources/beta/subresources/threads)

[Runs](/api/reference/java/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Steps

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
