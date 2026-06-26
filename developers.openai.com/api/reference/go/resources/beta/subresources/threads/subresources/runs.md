<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/runs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Runs

Build Assistants that can call models and use tools.

##### [List runs](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list)

Deprecated

client.Beta.Threads.Runs.List(ctx, threadID, query) (\*CursorPage[[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))], error)

GET/threads/{thread\_id}/runs

##### [Create run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/create)

Deprecated

client.Beta.Threads.Runs.New(ctx, threadID, params) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs

##### [Retrieve run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/retrieve)

Deprecated

client.Beta.Threads.Runs.Get(ctx, threadID, runID) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

GET/threads/{thread\_id}/runs/{run\_id}

##### [Modify run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/update)

Deprecated

client.Beta.Threads.Runs.Update(ctx, threadID, runID, body) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}

##### [Submit tool outputs to run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/submit_tool_outputs)

Deprecated

client.Beta.Threads.Runs.SubmitToolOutputs(ctx, threadID, runID, body) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}/submit\_tool\_outputs

##### [Cancel a run](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/cancel)

Deprecated

client.Beta.Threads.Runs.Cancel(ctx, threadID, runID) (\*[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema)), error)

POST/threads/{thread\_id}/runs/{run\_id}/cancel

##### ModelsExpand Collapse

type RequiredActionFunctionToolCall struct{…}

Tool call objects

ID string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function RequiredActionFunctionToolCallFunction

The function definition.

Arguments string

The arguments that the model expects you to pass to the function.

Name string

The name of the function.

Type Function

The type of tool call the output is required for. For now, this is always `function`.

type Run struct{…}

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

ID string

The identifier, which can be referenced in API endpoints.

AssistantID string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

CancelledAt int64

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

CompletedAt int64

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

ExpiresAt int64

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

FailedAt int64

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

IncompleteDetails RunIncompleteDetails

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

Reason stringOptional

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

const RunIncompleteDetailsReasonMaxCompletionTokens RunIncompleteDetailsReason = "max\_completion\_tokens"

const RunIncompleteDetailsReasonMaxPromptTokens RunIncompleteDetailsReason = "max\_prompt\_tokens"

Instructions string

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

LastError RunLastError

The last error associated with this run. Will be `null` if there are no errors.

Code string

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

const RunLastErrorCodeServerError RunLastErrorCode = "server\_error"

const RunLastErrorCodeRateLimitExceeded RunLastErrorCode = "rate\_limit\_exceeded"

const RunLastErrorCodeInvalidPrompt RunLastErrorCode = "invalid\_prompt"

Message string

A human-readable description of the error.

MaxCompletionTokens int64

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

MaxPromptTokens int64

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Model string

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

Object ThreadRun

The object type, which is always `thread.run`.

ParallelToolCalls bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

RequiredAction RunRequiredAction

Details on the action required to continue the run. Will be `null` if no action is required.

SubmitToolOutputs RunRequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

ToolCalls [][RequiredActionFunctionToolCall](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))

A list of the relevant tool calls.

ID string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

Function RequiredActionFunctionToolCallFunction

The function definition.

Arguments string

The arguments that the model expects you to pass to the function.

Name string

The name of the function.

Type Function

The type of tool call the output is required for. For now, this is always `function`.

Type SubmitToolOutputs

For now, this is always `submit_tool_outputs`.

ResponseFormat [AssistantResponseFormatOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

StartedAt int64

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

Status [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

ThreadID string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

ToolChoice [AssistantToolChoiceOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

Tools [][AssistantToolUnion](/api/reference/go/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

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

TruncationStrategy RunTruncationStrategy

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

Type string

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

const RunTruncationStrategyTypeAuto RunTruncationStrategyType = "auto"

const RunTruncationStrategyTypeLastMessages RunTruncationStrategyType = "last\_messages"

LastMessages int64Optional

The number of most recent messages from the thread when constructing the context for the run.

minimum1

Usage RunUsage

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

CompletionTokens int64

Number of completion tokens used over the course of the run.

PromptTokens int64

Number of prompt tokens used over the course of the run.

TotalTokens int64

Total number of tokens used (prompt + completion).

Temperature float64Optional

The sampling temperature used for this run. If not set, defaults to 1.

TopP float64Optional

The nucleus sampling value used for this run. If not set, defaults to 1.

type RunStatus string

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

const RunStatusQueued [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "queued"

const RunStatusInProgress [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "in\_progress"

const RunStatusRequiresAction [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "requires\_action"

const RunStatusCancelling [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "cancelling"

const RunStatusCancelled [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "cancelled"

const RunStatusFailed [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "failed"

const RunStatusCompleted [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "completed"

const RunStatusIncomplete [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "incomplete"

const RunStatusExpired [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) = "expired"

#### RunsSteps

Build Assistants that can call models and use tools.

##### [List run steps](/api/reference/go/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/list)

Deprecated

client.Beta.Threads.Runs.Steps.List(ctx, threadID, runID, query) (\*CursorPage[[RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))], error)

GET/threads/{thread\_id}/runs/{run\_id}/steps

##### [Retrieve run step](/api/reference/go/resources/beta/subresources/threads/subresources/runs/subresources/steps/methods/retrieve)

Deprecated

client.Beta.Threads.Runs.Steps.Get(ctx, threadID, runID, stepID, query) (\*[RunStep](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema)), error)

GET/threads/{thread\_id}/runs/{run\_id}/steps/{step\_id}

##### ModelsExpand Collapse

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type MessageCreationStepDetails struct{…}

Details of the message creation by the run step.

MessageCreation MessageCreationStepDetailsMessageCreation

MessageID string

The ID of the message that was created by this run step.

Type MessageCreation

Always `message_creation`.

type RunStep struct{…}

Represents a step in execution of a run.

ID string

The identifier of the run step, which can be referenced in API endpoints.

AssistantID string

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

CancelledAt int64

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

CompletedAt int64

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

CreatedAt int64

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

ExpiredAt int64

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

FailedAt int64

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

LastError RunStepLastError

The last error associated with this run step. Will be `null` if there are no errors.

Code string

One of `server_error` or `rate_limit_exceeded`.

One of the following:

const RunStepLastErrorCodeServerError RunStepLastErrorCode = "server\_error"

const RunStepLastErrorCodeRateLimitExceeded RunStepLastErrorCode = "rate\_limit\_exceeded"

Message string

A human-readable description of the error.

Metadata [Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Object ThreadRunStep

The object type, which is always `thread.run.step`.

RunID string

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

Status RunStepStatus

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

const RunStepStatusInProgress RunStepStatus = "in\_progress"

const RunStepStatusCancelled RunStepStatus = "cancelled"

const RunStepStatusFailed RunStepStatus = "failed"

const RunStepStatusCompleted RunStepStatus = "completed"

const RunStepStatusExpired RunStepStatus = "expired"

StepDetails RunStepStepDetailsUnion

The details of the run step.

One of the following:

type MessageCreationStepDetails struct{…}

Details of the message creation by the run step.

MessageCreation MessageCreationStepDetailsMessageCreation

MessageID string

The ID of the message that was created by this run step.

Type MessageCreation

Always `message_creation`.

type ToolCallsStepDetails struct{…}

Details of the tool call.

ToolCalls [][ToolCallUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

Type ToolCalls

Always `tool_calls`.

ThreadID string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

Type RunStepType

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

const RunStepTypeMessageCreation RunStepType = "message\_creation"

const RunStepTypeToolCalls RunStepType = "tool\_calls"

Usage RunStepUsage

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

CompletionTokens int64

Number of completion tokens used over the course of the run step.

PromptTokens int64

Number of prompt tokens used over the course of the run step.

TotalTokens int64

Total number of tokens used (prompt + completion).

type RunStepDelta struct{…}

The delta containing the fields that have changed on the run step.

StepDetails RunStepDeltaStepDetailsUnionOptional

The details of the run step.

One of the following:

type RunStepDeltaMessageDelta struct{…}

Details of the message creation by the run step.

Type MessageCreation

Always `message_creation`.

MessageCreation RunStepDeltaMessageDeltaMessageCreationOptional

MessageID stringOptional

The ID of the message that was created by this run step.

type ToolCallDeltaObject struct{…}

Details of the tool call.

Type ToolCalls

Always `tool_calls`.

ToolCalls [][ToolCallDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))Optional

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type RunStepDeltaEvent struct{…}

Represents a run step delta i.e. any changed fields on a run step during streaming.

ID string

The identifier of the run step, which can be referenced in API endpoints.

Delta [RunStepDelta](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema))

The delta containing the fields that have changed on the run step.

Object ThreadRunStepDelta

The object type, which is always `thread.run.step.delta`.

type RunStepDeltaMessageDelta struct{…}

Details of the message creation by the run step.

Type MessageCreation

Always `message_creation`.

MessageCreation RunStepDeltaMessageDeltaMessageCreationOptional

MessageID stringOptional

The ID of the message that was created by this run step.

type RunStepInclude string

type ToolCallUnion interface{…}

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

type ToolCallDeltaUnion interface{…}

Details of the Code Interpreter tool call the run step was involved in.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type ToolCallDeltaObject struct{…}

Details of the tool call.

Type ToolCalls

Always `tool_calls`.

ToolCalls [][ToolCallDeltaUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))Optional

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCallDelta struct{…}

Details of the Code Interpreter tool call the run step was involved in.

Index int64

The index of the tool call in the tool calls array.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

ID stringOptional

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallDeltaCodeInterpreterOptional

The Code Interpreter tool call definition.

Input stringOptional

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallDeltaCodeInterpreterOutputUnionOptional

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Index int64

The index of the output in the outputs array.

Type Logs

Always `logs`.

Logs stringOptional

The text output from the Code Interpreter tool call.

type CodeInterpreterOutputImage struct{…}

Index int64

The index of the output in the outputs array.

Type Image

Always `image`.

Image CodeInterpreterOutputImageImageOptional

FileID stringOptional

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type FileSearchToolCallDelta struct{…}

FileSearch any

For now, this is always going to be an empty object.

Index int64

The index of the tool call in the tool calls array.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

ID stringOptional

The ID of the tool call object.

type FunctionToolCallDelta struct{…}

Index int64

The index of the tool call in the tool calls array.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

ID stringOptional

The ID of the tool call object.

Function FunctionToolCallDeltaFunctionOptional

The definition of the function that was called.

Arguments stringOptional

The arguments passed to the function.

Name stringOptional

The name of the function.

Output stringOptional

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type ToolCallsStepDetails struct{…}

Details of the tool call.

ToolCalls [][ToolCallUnion](/api/reference/go/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

type CodeInterpreterToolCall struct{…}

Details of the Code Interpreter tool call the run step was involved in.

ID string

The ID of the tool call.

CodeInterpreter CodeInterpreterToolCallCodeInterpreter

The Code Interpreter tool call definition.

Input string

The input to the Code Interpreter tool call.

Outputs []CodeInterpreterToolCallCodeInterpreterOutputUnion

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

type CodeInterpreterToolCallCodeInterpreterOutputLogs struct{…}

Text output from the Code Interpreter tool call as part of a run step.

Logs string

The text output from the Code Interpreter tool call.

Type Logs

Always `logs`.

type CodeInterpreterToolCallCodeInterpreterOutputImage struct{…}

Image CodeInterpreterToolCallCodeInterpreterOutputImageImage

FileID string

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

Type Image

Always `image`.

Type CodeInterpreter

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

type FileSearchToolCall struct{…}

ID string

The ID of the tool call object.

FileSearch FileSearchToolCallFileSearch

For now, this is always going to be an empty object.

RankingOptions FileSearchToolCallFileSearchRankingOptionsOptional

The ranking options for the file search.

Ranker string

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

const FileSearchToolCallFileSearchRankingOptionsRankerAuto FileSearchToolCallFileSearchRankingOptionsRanker = "auto"

const FileSearchToolCallFileSearchRankingOptionsRankerDefault2024\_08\_21 FileSearchToolCallFileSearchRankingOptionsRanker = "default\_2024\_08\_21"

ScoreThreshold float64

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Results []FileSearchToolCallFileSearchResultOptional

The results of the file search.

FileID string

The ID of the file that result was found in.

FileName string

The name of the file that result was found in.

Score float64

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

Content []FileSearchToolCallFileSearchResultContentOptional

The content of the result that was found. The content is only included if requested via the include query parameter.

Text stringOptional

The text content of the file.

Type stringOptional

The type of the content.

Type FileSearch

The type of tool call. This is always going to be `file_search` for this type of tool call.

type FunctionToolCall struct{…}

ID string

The ID of the tool call object.

Function FunctionToolCallFunction

The definition of the function that was called.

Arguments string

The arguments passed to the function.

Name string

The name of the function.

Output string

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

Type Function

The type of tool call. This is always going to be `function` for this type of tool call.

Type ToolCalls

Always `tool_calls`.
