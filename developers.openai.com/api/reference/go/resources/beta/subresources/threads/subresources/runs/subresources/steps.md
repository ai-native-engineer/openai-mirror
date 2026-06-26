<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/runs/subresources/steps/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Beta](/api/reference/go/resources/beta)

[Threads](/api/reference/go/resources/beta/subresources/threads)

[Runs](/api/reference/go/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Steps

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
