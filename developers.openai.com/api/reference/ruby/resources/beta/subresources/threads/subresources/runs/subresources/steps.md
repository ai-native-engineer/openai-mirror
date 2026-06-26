<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/threads/subresources/runs/subresources/steps/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Threads](/api/reference/ruby/resources/beta/subresources/threads)

[Runs](/api/reference/ruby/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Steps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/ruby/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

beta.threads.runs.steps.list(run\_id, \*\*kwargs) -> CursorPage<[RunStep](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more } >

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/ruby/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

beta.threads.runs.steps.retrieve(step\_id, \*\*kwargs) -> [RunStep](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

class CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: Integer

The index of the output in the outputs array.

type: :logs

Always `logs`.

logs: String

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage { index, type, image }

index: Integer

The index of the output in the outputs array.

type: :image

Always `image`.

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[Logs{ logs, type} | Image{ image, type}]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: String

The text output from the Code Interpreter tool call.

type: :logs

Always `logs`.

class Image { image, type }

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: :image

Always `image`.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: Integer

The index of the tool call in the tool calls array.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[[CodeInterpreterLogs](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } ]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: Integer

The index of the output in the outputs array.

type: :logs

Always `logs`.

logs: String

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage { index, type, image }

index: Integer

The index of the output in the outputs array.

type: :image

Always `image`.

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCall { id, file\_search, type }

id: String

The ID of the tool call object.

file\_search: FileSearch{ ranking\_options, results}

For now, this is always going to be an empty object.

ranking\_options: RankingOptions{ ranker, score\_threshold}

The ranking options for the file search.

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Array[Result{ file\_id, file\_name, score, content}]

The results of the file search.

file\_id: String

The ID of the file that result was found in.

file\_name: String

The name of the file that result was found in.

score: Float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Array[Content{ text, type}]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: String

The text content of the file.

type: :text

The type of the content.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: untyped

For now, this is always going to be an empty object.

index: Integer

The index of the tool call in the tool calls array.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: String

The ID of the tool call object.

class FunctionToolCall { id, function, type }

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

class FunctionToolCallDelta { index, type, id, function }

index: Integer

The index of the tool call in the tool calls array.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation{ message\_id}

message\_id: String

The ID of the message that was created by this run step.

type: :message\_creation

Always `message_creation`.

class RunStep { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: String

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: String

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Integer

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Integer

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: Integer

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Integer

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Integer

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: LastError{ code, message}

The last error associated with this run step. Will be `null` if there are no errors.

code: :server\_error | :rate\_limit\_exceeded

One of `server_error` or `rate_limit_exceeded`.

One of the following:

:server\_error

:rate\_limit\_exceeded

message: String

A human-readable description of the error.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: :"thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: String

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: :in\_progress | :cancelled | :failed | 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

:in\_progress

:cancelled

:failed

:completed

:expired

step\_details: [MessageCreationStepDetails](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  | [ToolCallsStepDetails](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

One of the following:

class MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation{ message\_id}

message\_id: String

The ID of the message that was created by this run step.

type: :message\_creation

Always `message_creation`.

class ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array[[ToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[Logs{ logs, type} | Image{ image, type}]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: String

The text output from the Code Interpreter tool call.

type: :logs

Always `logs`.

class Image { image, type }

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: :image

Always `image`.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall { id, file\_search, type }

id: String

The ID of the tool call object.

file\_search: FileSearch{ ranking\_options, results}

For now, this is always going to be an empty object.

ranking\_options: RankingOptions{ ranker, score\_threshold}

The ranking options for the file search.

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Array[Result{ file\_id, file\_name, score, content}]

The results of the file search.

file\_id: String

The ID of the file that result was found in.

file\_name: String

The name of the file that result was found in.

score: Float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Array[Content{ text, type}]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: String

The text content of the file.

type: :text

The type of the content.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall { id, function, type }

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

type: :tool\_calls

Always `tool_calls`.

thread\_id: String

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: :message\_creation | :tool\_calls

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

:message\_creation

:tool\_calls

usage: Usage{ completion\_tokens, prompt\_tokens, total\_tokens}

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: Integer

Number of completion tokens used over the course of the run step.

prompt\_tokens: Integer

Number of prompt tokens used over the course of the run step.

total\_tokens: Integer

Total number of tokens used (prompt + completion).

class RunStepDelta { step\_details }

The delta containing the fields that have changed on the run step.

step\_details: [RunStepDeltaMessageDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  | [ToolCallDeltaObject](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

One of the following:

class RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: :message\_creation

Always `message_creation`.

message\_creation: MessageCreation{ message\_id}

message\_id: String

The ID of the message that was created by this run step.

class ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: :tool\_calls

Always `tool_calls`.

tool\_calls: Array[[ToolCallDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: Integer

The index of the tool call in the tool calls array.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[[CodeInterpreterLogs](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } ]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: Integer

The index of the output in the outputs array.

type: :logs

Always `logs`.

logs: String

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage { index, type, image }

index: Integer

The index of the output in the outputs array.

type: :image

Always `image`.

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: untyped

For now, this is always going to be an empty object.

index: Integer

The index of the tool call in the tool calls array.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: String

The ID of the tool call object.

class FunctionToolCallDelta { index, type, id, function }

index: Integer

The index of the tool call in the tool calls array.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class RunStepDeltaEvent { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: String

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema)) { step\_details }

The delta containing the fields that have changed on the run step.

object: :"thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

class RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: :message\_creation

Always `message_creation`.

message\_creation: MessageCreation{ message\_id}

message\_id: String

The ID of the message that was created by this run step.

RunStepInclude = :"step\_details.tool\_calls[\*].file\_search.results[\*].content"

ToolCall = [CodeInterpreterToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  | [FileSearchToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  | [FunctionToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[Logs{ logs, type} | Image{ image, type}]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: String

The text output from the Code Interpreter tool call.

type: :logs

Always `logs`.

class Image { image, type }

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: :image

Always `image`.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall { id, file\_search, type }

id: String

The ID of the tool call object.

file\_search: FileSearch{ ranking\_options, results}

For now, this is always going to be an empty object.

ranking\_options: RankingOptions{ ranker, score\_threshold}

The ranking options for the file search.

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Array[Result{ file\_id, file\_name, score, content}]

The results of the file search.

file\_id: String

The ID of the file that result was found in.

file\_name: String

The name of the file that result was found in.

score: Float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Array[Content{ text, type}]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: String

The text content of the file.

type: :text

The type of the content.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall { id, function, type }

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

ToolCallDelta = [CodeInterpreterToolCallDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index, type, id, code\_interpreter }  | [FileSearchToolCallDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file\_search, index, type, id }  | [FunctionToolCallDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index, type, id, function }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: Integer

The index of the tool call in the tool calls array.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[[CodeInterpreterLogs](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } ]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: Integer

The index of the output in the outputs array.

type: :logs

Always `logs`.

logs: String

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage { index, type, image }

index: Integer

The index of the output in the outputs array.

type: :image

Always `image`.

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: untyped

For now, this is always going to be an empty object.

index: Integer

The index of the tool call in the tool calls array.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: String

The ID of the tool call object.

class FunctionToolCallDelta { index, type, id, function }

index: Integer

The index of the tool call in the tool calls array.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: :tool\_calls

Always `tool_calls`.

tool\_calls: Array[[ToolCallDelta](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: Integer

The index of the tool call in the tool calls array.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[[CodeInterpreterLogs](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } ]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: Integer

The index of the output in the outputs array.

type: :logs

Always `logs`.

logs: String

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage { index, type, image }

index: Integer

The index of the output in the outputs array.

type: :image

Always `image`.

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: untyped

For now, this is always going to be an empty object.

index: Integer

The index of the tool call in the tool calls array.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: String

The ID of the tool call object.

class FunctionToolCallDelta { index, type, id, function }

index: Integer

The index of the tool call in the tool calls array.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array[[ToolCall](/api/reference/ruby/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: String

The ID of the tool call.

code\_interpreter: CodeInterpreter{ input, outputs}

The Code Interpreter tool call definition.

input: String

The input to the Code Interpreter tool call.

outputs: Array[Logs{ logs, type} | Image{ image, type}]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: String

The text output from the Code Interpreter tool call.

type: :logs

Always `logs`.

class Image { image, type }

image: Image{ file\_id}

file\_id: String

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: :image

Always `image`.

type: :code\_interpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall { id, file\_search, type }

id: String

The ID of the tool call object.

file\_search: FileSearch{ ranking\_options, results}

For now, this is always going to be an empty object.

ranking\_options: RankingOptions{ ranker, score\_threshold}

The ranking options for the file search.

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Array[Result{ file\_id, file\_name, score, content}]

The results of the file search.

file\_id: String

The ID of the file that result was found in.

file\_name: String

The name of the file that result was found in.

score: Float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Array[Content{ text, type}]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: String

The text content of the file.

type: :text

The type of the content.

type: :file\_search

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall { id, function, type }

id: String

The ID of the tool call object.

function: Function{ arguments, name, output}

The definition of the function that was called.

arguments: String

The arguments passed to the function.

name: String

The name of the function.

output: String

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: :function

The type of tool call. This is always going to be `function` for this type of tool call.

type: :tool\_calls

Always `tool_calls`.
