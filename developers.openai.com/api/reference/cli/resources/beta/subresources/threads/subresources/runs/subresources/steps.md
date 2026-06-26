<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/threads/subresources/runs/subresources/steps/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Threads](/api/reference/cli/resources/beta/subresources/threads)

[Runs](/api/reference/cli/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Steps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/cli/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

$ openai beta:threads:runs:steps list

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/cli/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

$ openai beta:threads:runs:steps retrieve

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

code\_interpreter\_tool\_call: object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

logs: object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

image: object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

code\_interpreter\_tool\_call\_delta: object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

file\_search\_tool\_call: object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

"text"

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

file\_search\_tool\_call\_delta: object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

function\_tool\_call: object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

function\_tool\_call\_delta: object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

message\_creation\_step\_details: object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

run\_step: object { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run step was cancelled.

completed\_at: number

The Unix timestamp (in seconds) for when the run step completed.

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

expired\_at: number

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

failed\_at: number

The Unix timestamp (in seconds) for when the run step failed.

last\_error: object { code, message }

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: map[string]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" or "cancelled" or "failed" or 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  or [ToolCallsStepDetails](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

message\_creation\_step\_details: object { message\_creation, type }

Details of the message creation by the run step.

message\_creation: object { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

tool\_calls\_step\_details: object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [ToolCall](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

code\_interpreter\_tool\_call: object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

logs: object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

image: object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

file\_search\_tool\_call: object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

"text"

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

function\_tool\_call: object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" or "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

"message\_creation"

"tool\_calls"

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

run\_step\_delta: object { step\_details }

The delta containing the fields that have changed on the run step.

step\_details: optional [RunStepDeltaMessageDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  or [ToolCallDeltaObject](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

run\_step\_delta\_message\_delta: object { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation: optional object { message\_id }

message\_id: optional string

The ID of the message that was created by this run step.

tool\_call\_delta\_object: object { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls: optional array of [ToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

code\_interpreter\_tool\_call\_delta: object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

file\_search\_tool\_call\_delta: object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

function\_tool\_call\_delta: object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

run\_step\_delta\_event: object { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: string

The identifier of the run step, which can be referenced in API endpoints.

delta: object { step\_details }

The delta containing the fields that have changed on the run step.

step\_details: optional [RunStepDeltaMessageDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  or [ToolCallDeltaObject](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

run\_step\_delta\_message\_delta: object { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation: optional object { message\_id }

message\_id: optional string

The ID of the message that was created by this run step.

tool\_call\_delta\_object: object { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls: optional array of [ToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

code\_interpreter\_tool\_call\_delta: object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

file\_search\_tool\_call\_delta: object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

function\_tool\_call\_delta: object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

object: "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

run\_step\_delta\_message\_delta: object { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation: optional object { message\_id }

message\_id: optional string

The ID of the message that was created by this run step.

run\_step\_include: "step\_details.tool\_calls[\*].file\_search.results[\*].content"

"step\_details.tool\_calls[\*].file\_search.results[\*].content"

tool\_call: [CodeInterpreterToolCall](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  or [FileSearchToolCall](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  or [FunctionToolCall](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

Details of the Code Interpreter tool call the run step was involved in.

code\_interpreter\_tool\_call: object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

logs: object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

image: object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

file\_search\_tool\_call: object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

"text"

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

function\_tool\_call: object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

tool\_call\_delta: [CodeInterpreterToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index, type, id, code\_interpreter }  or [FileSearchToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file\_search, index, type, id }  or [FunctionToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index, type, id, function }

Details of the Code Interpreter tool call the run step was involved in.

code\_interpreter\_tool\_call\_delta: object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

file\_search\_tool\_call\_delta: object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

function\_tool\_call\_delta: object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

tool\_call\_delta\_object: object { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls: optional array of [ToolCallDelta](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

code\_interpreter\_tool\_call\_delta: object { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: optional string

The ID of the tool call.

code\_interpreter: optional object { input, outputs }

The Code Interpreter tool call definition.

input: optional string

The input to the Code Interpreter tool call.

outputs: optional array of [CodeInterpreterLogs](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  or [CodeInterpreterOutputImage](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

code\_interpreter\_logs: object { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs: optional string

The text output from the Code Interpreter tool call.

code\_interpreter\_output\_image: object { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image: optional object { file\_id }

file\_id: optional string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

file\_search\_tool\_call\_delta: object { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: optional string

The ID of the tool call object.

function\_tool\_call\_delta: object { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id: optional string

The ID of the tool call object.

function: optional object { arguments, name, output }

The definition of the function that was called.

arguments: optional string

The arguments passed to the function.

name: optional string

The name of the function.

output: optional string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

tool\_calls\_step\_details: object { tool\_calls, type }

Details of the tool call.

tool\_calls: array of [ToolCall](/api/reference/cli/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

code\_interpreter\_tool\_call: object { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: object { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: array of object { logs, type }  or object { image, type }

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

logs: object { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

image: object { image, type }

image: object { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

file\_search\_tool\_call: object { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: object { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options: optional object { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

results: optional array of object { file\_id, file\_name, score, content }

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

content: optional array of object { text, type }

The content of the result that was found. The content is only included if requested via the include query parameter.

text: optional string

The text content of the file.

type: optional "text"

The type of the content.

"text"

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

function\_tool\_call: object { id, function, type }

id: string

The ID of the tool call object.

function: object { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.
