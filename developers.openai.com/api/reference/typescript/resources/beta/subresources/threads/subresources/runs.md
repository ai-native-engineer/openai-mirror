<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Threads](/api/reference/typescript/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Runs

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

client.beta.threads.runs.list(stringthreadID, RunListParams { after, before, limit, order } query?, RequestOptionsoptions?): CursorPage<[Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more } >

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

client.beta.threads.runs.create(stringthreadID, RunCreateParamsparams, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }  | Stream<[AssistantStreamEvent](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))>

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

client.beta.threads.runs.retrieve(stringrunID, RunRetrieveParams { thread\_id } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

client.beta.threads.runs.update(stringrunID, RunUpdateParams { thread\_id, metadata } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

client.beta.threads.runs.submitToolOutputs(stringrunID, RunSubmitToolOutputsParamsparams, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }  | Stream<[AssistantStreamEvent](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))>

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

client.beta.threads.runs.cancel(stringrunID, RunCancelParams { thread\_id } params, RequestOptionsoptions?): [Run](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 24 more }

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

RequiredActionFunctionToolCall { id, function, type }

Tool call objects

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

Run { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number | null

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: number | null

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: number | null

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: number | null

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: IncompleteDetails | null

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason?: "max\_completion\_tokens" | "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: LastError | null

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" | "rate\_limit\_exceeded" | "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number | null

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number | null

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: RequiredAction | null

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: SubmitToolOutputs { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: Array<[RequiredActionFunctionToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type } >

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema)) | null

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

started\_at: number | null

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

thread\_id: string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](/api/reference/typescript/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema)) | null

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

tools: Array<[AssistantTool](/api/reference/typescript/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))>

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

CodeInterpreterTool { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search?: FileSearch { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results?: number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options?: RankingOptions { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker?: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool { function, type }

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of tool being defined: `function`

truncation\_strategy: TruncationStrategy | null

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" | "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages?: number | null

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Usage | null

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature?: number | null

The sampling temperature used for this run. If not set, defaults to 1.

top\_p?: number | null

The nucleus sampling value used for this run. If not set, defaults to 1.

RunStatus = "queued" | "in\_progress" | "requires\_action" | 6 more

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

"queued"

"in\_progress"

"requires\_action"

"cancelling"

"cancelled"

"failed"

"completed"

"incomplete"

"expired"

#### RunsSteps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

client.beta.threads.runs.steps.list(stringrunID, StepListParams { thread\_id, after, before, 3 more } params, RequestOptionsoptions?): CursorPage<[RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more } >

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/typescript/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

client.beta.threads.runs.steps.retrieve(stringstepID, StepRetrieveParams { thread\_id, run\_id, include } params, RequestOptionsoptions?): [RunStep](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)) { id, assistant\_id, cancelled\_at, 13 more }

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

RunStep { id, assistant\_id, cancelled\_at, 13 more }

Represents a step in execution of a run.

id: string

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: number | null

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: number | null

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: number | null

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: number | null

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: LastError | null

The last error associated with this run step. Will be `null` if there are no errors.

code: "server\_error" | "rate\_limit\_exceeded"

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: string

A human-readable description of the error.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: "thread.run.step"

The object type, which is always `thread.run.step`.

run\_id: string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: "in\_progress" | "cancelled" | "failed" | 2 more

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: [MessageCreationStepDetails](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20message_creation_step_details%20%3E%20(schema)) { message\_creation, type }  | [ToolCallsStepDetails](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_calls_step_details%20%3E%20(schema)) { tool\_calls, type }

The details of the run step.

One of the following:

MessageCreationStepDetails { message\_creation, type }

Details of the message creation by the run step.

message\_creation: MessageCreation { message\_id }

message\_id: string

The ID of the message that was created by this run step.

type: "message\_creation"

Always `message_creation`.

ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array<[ToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.

thread\_id: string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: "message\_creation" | "tool\_calls"

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Usage | null

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: number

Number of completion tokens used over the course of the run step.

prompt\_tokens: number

Number of prompt tokens used over the course of the run step.

total\_tokens: number

Total number of tokens used (prompt + completion).

RunStepDelta { step\_details }

The delta containing the fields that have changed on the run step.

step\_details?: [RunStepDeltaMessageDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_message_delta%20%3E%20(schema)) { type, message\_creation }  | [ToolCallDeltaObject](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta_object%20%3E%20(schema)) { type, tool\_calls }

The details of the run step.

One of the following:

RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation?: MessageCreation { message\_id }

message\_id?: string

The ID of the message that was created by this run step.

ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls?: Array<[ToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

RunStepDeltaEvent { id, delta, object }

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: string

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema)) { step\_details }

The delta containing the fields that have changed on the run step.

object: "thread.run.step.delta"

The object type, which is always `thread.run.step.delta`.

RunStepDeltaMessageDelta { type, message\_creation }

Details of the message creation by the run step.

type: "message\_creation"

Always `message_creation`.

message\_creation?: MessageCreation { message\_id }

message\_id?: string

The ID of the message that was created by this run step.

RunStepInclude = "step\_details.tool\_calls[\*].file\_search.results[\*].content"

ToolCall = [CodeInterpreterToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call%20%3E%20(schema)) { id, code\_interpreter, type }  | [FileSearchToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call%20%3E%20(schema)) { id, file\_search, type }  | [FunctionToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call%20%3E%20(schema)) { id, function, type }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

ToolCallDelta = [CodeInterpreterToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_tool_call_delta%20%3E%20(schema)) { index, type, id, code\_interpreter }  | [FileSearchToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20file_search_tool_call_delta%20%3E%20(schema)) { file\_search, index, type, id }  | [FunctionToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20function_tool_call_delta%20%3E%20(schema)) { index, type, id, function }

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

ToolCallDeltaObject { type, tool\_calls }

Details of the tool call.

type: "tool\_calls"

Always `tool_calls`.

tool\_calls?: Array<[ToolCallDelta](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCallDelta { index, type, id, code\_interpreter }

Details of the Code Interpreter tool call the run step was involved in.

index: number

The index of the tool call in the tool calls array.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id?: string

The ID of the tool call.

code\_interpreter?: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input?: string

The input to the Code Interpreter tool call.

outputs?: Array<[CodeInterpreterLogs](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_logs%20%3E%20(schema)) { index, type, logs }  | [CodeInterpreterOutputImage](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20code_interpreter_output_image%20%3E%20(schema)) { index, type, image } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

CodeInterpreterLogs { index, type, logs }

Text output from the Code Interpreter tool call as part of a run step.

index: number

The index of the output in the outputs array.

type: "logs"

Always `logs`.

logs?: string

The text output from the Code Interpreter tool call.

CodeInterpreterOutputImage { index, type, image }

index: number

The index of the output in the outputs array.

type: "image"

Always `image`.

image?: Image { file\_id }

file\_id?: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

FileSearchToolCallDelta { file\_search, index, type, id }

file\_search: unknown

For now, this is always going to be an empty object.

index: number

The index of the tool call in the tool calls array.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

id?: string

The ID of the tool call object.

FunctionToolCallDelta { index, type, id, function }

index: number

The index of the tool call in the tool calls array.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

id?: string

The ID of the tool call object.

function?: Function { arguments, name, output }

The definition of the function that was called.

arguments?: string

The arguments passed to the function.

name?: string

The name of the function.

output?: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

ToolCallsStepDetails { tool\_calls, type }

Details of the tool call.

tool\_calls: Array<[ToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))>

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

CodeInterpreterToolCall { id, code\_interpreter, type }

Details of the Code Interpreter tool call the run step was involved in.

id: string

The ID of the tool call.

code\_interpreter: CodeInterpreter { input, outputs }

The Code Interpreter tool call definition.

input: string

The input to the Code Interpreter tool call.

outputs: Array<Logs { logs, type }  | Image { image, type } >

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

Logs { logs, type }

Text output from the Code Interpreter tool call as part of a run step.

logs: string

The text output from the Code Interpreter tool call.

type: "logs"

Always `logs`.

Image { image, type }

image: Image { file\_id }

file\_id: string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: "image"

Always `image`.

type: "code\_interpreter"

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

FileSearchToolCall { id, file\_search, type }

id: string

The ID of the tool call object.

file\_search: FileSearch { ranking\_options, results }

For now, this is always going to be an empty object.

ranking\_options?: RankingOptions { ranker, score\_threshold }

The ranking options for the file search.

ranker: "auto" | "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results?: Array<Result>

The results of the file search.

file\_id: string

The ID of the file that result was found in.

file\_name: string

The name of the file that result was found in.

score: number

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content?: Array<Content>

The content of the result that was found. The content is only included if requested via the include query parameter.

text?: string

The text content of the file.

type?: "text"

The type of the content.

type: "file\_search"

The type of tool call. This is always going to be `file_search` for this type of tool call.

FunctionToolCall { id, function, type }

id: string

The ID of the tool call object.

function: Function { arguments, name, output }

The definition of the function that was called.

arguments: string

The arguments passed to the function.

name: string

The name of the function.

output: string | null

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: "function"

The type of tool call. This is always going to be `function` for this type of tool call.

type: "tool\_calls"

Always `tool_calls`.
