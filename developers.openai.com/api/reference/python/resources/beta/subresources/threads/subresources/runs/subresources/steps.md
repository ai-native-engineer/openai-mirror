<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/subresources/runs/subresources/steps/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Threads](/api/reference/python/resources/beta/subresources/threads)

[Runs](/api/reference/python/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Steps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/python/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

beta.threads.runs.steps.list(strrun\_id, StepListParams\*\*kwargs)  -> SyncCursorPage[[RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))]

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/python/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

beta.threads.runs.steps.retrieve(strstep\_id, StepRetrieveParams\*\*kwargs)  -> [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class RunStep: …

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

class RunStepDelta: …

The delta containing the fields that have changed on the run step.

step\_details: Optional[StepDetails]

The details of the run step.

One of the following:

class RunStepDeltaMessageDelta: …

Details of the message creation by the run step.

type: Literal["message\_creation"]

Always `message_creation`.

message\_creation: Optional[MessageCreation]

message\_id: Optional[str]

The ID of the message that was created by this run step.

class ToolCallDeltaObject: …

Details of the tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

tool\_calls: Optional[List[[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class RunStepDeltaEvent: …

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: str

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema))

The delta containing the fields that have changed on the run step.

object: Literal["thread.run.step.delta"]

The object type, which is always `thread.run.step.delta`.

class RunStepDeltaMessageDelta: …

Details of the message creation by the run step.

type: Literal["message\_creation"]

Always `message_creation`.

message\_creation: Optional[MessageCreation]

message\_id: Optional[str]

The ID of the message that was created by this run step.

Literal["step\_details.tool\_calls[\*].file\_search.results[\*].content"]

[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallDeltaObject: …

Details of the tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

tool\_calls: Optional[List[[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.
