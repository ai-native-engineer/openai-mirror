<!-- source: https://developers.openai.com/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list/ -->

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

# List runs

Deprecated: The Assistants API is deprecated in favor of the Responses API

client.Beta.Threads.Runs.List(ctx, threadID, query) (\*CursorPage[[Run](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))], error)

GET/threads/{thread\_id}/runs

Returns a list of runs belonging to a thread.

##### ParametersExpand Collapse

threadID string

query BetaThreadRunListParams

After param.Field[string]Optional

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Before param.Field[string]Optional

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Limit param.Field[int64]Optional

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Order param.Field[[BetaThreadRunListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list#(resource)%20beta.threads.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))]Optional

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

const BetaThreadRunListParamsOrderAsc [BetaThreadRunListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list#(resource)%20beta.threads.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "asc"

const BetaThreadRunListParamsOrderDesc [BetaThreadRunListParamsOrder](/api/reference/go/resources/beta/subresources/threads/subresources/runs/methods/list#(resource)%20beta.threads.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema)) = "desc"

##### ReturnsExpand Collapse

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

One of the following:

type Auto string

`auto` is the default value

type ResponseFormatText struct{…}

Default response format. Used to generate text responses.

Type Text

The type of response format being defined. Always `text`.

type ResponseFormatJSONObject struct{…}

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

Type JSONObject

The type of response format being defined. Always `json_object`.

type ResponseFormatJSONSchema struct{…}

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JSONSchema ResponseFormatJSONSchemaJSONSchema

Structured Outputs configuration options, including a JSON Schema.

Name string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the response format is for, used by the model to
determine how to respond in the format.

Schema map[string, any]Optional

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Strict boolOptional

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Type JSONSchema

The type of response format being defined. Always `json_schema`.

StartedAt int64

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

Status [RunStatus](/api/reference/go/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

ThreadID string

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

ToolChoice [AssistantToolChoiceOptionUnion](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

type AssistantToolChoiceOptionAuto string

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

const AssistantToolChoiceOptionAutoNone AssistantToolChoiceOptionAuto = "none"

const AssistantToolChoiceOptionAutoAuto AssistantToolChoiceOptionAuto = "auto"

const AssistantToolChoiceOptionAutoRequired AssistantToolChoiceOptionAuto = "required"

type AssistantToolChoice struct{…}

Specifies a tool the model should use. Use to force the model to call a specific tool.

Type AssistantToolChoiceType

The type of the tool. If type is `function`, the function name must be set

One of the following:

const AssistantToolChoiceTypeFunction AssistantToolChoiceType = "function"

const AssistantToolChoiceTypeCodeInterpreter AssistantToolChoiceType = "code\_interpreter"

const AssistantToolChoiceTypeFileSearch AssistantToolChoiceType = "file\_search"

Function [AssistantToolChoiceFunction](/api/reference/go/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema))Optional

Name string

The name of the function to call.

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

Name string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the function does, used by the model to choose when and how to call the function.

Parameters [FunctionParameters](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))Optional

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Strict boolOptional

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

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

### List runs

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  page, err := client.Beta.Threads.Runs.List(
    context.TODO(),
    "thread_id",
    openai.BetaThreadRunListParams{

  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", page)

  "object": "list",
  "data": [
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4o",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
          "type": "code_interpreter"
      ],
      "tool_resources": {
        "code_interpreter": {
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ]
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
      "id": "run_abc456",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-4o",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
          "type": "code_interpreter"
      ],
      "tool_resources": {
        "code_interpreter": {
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ]
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
  ],
  "first_id": "run_abc123",
  "last_id": "run_abc456",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "id": "run_abc123",
      "object": "thread.run",
      "created_at": 1699075072,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699075072,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699075073,
      "last_error": null,
      "model": "gpt-4o",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
          "type": "code_interpreter"
      ],
      "tool_resources": {
        "code_interpreter": {
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ]
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
      "id": "run_abc456",
      "object": "thread.run",
      "created_at": 1699063290,
      "assistant_id": "asst_abc123",
      "thread_id": "thread_abc123",
      "status": "completed",
      "started_at": 1699063290,
      "expires_at": null,
      "cancelled_at": null,
      "failed_at": null,
      "completed_at": 1699063291,
      "last_error": null,
      "model": "gpt-4o",
      "instructions": null,
      "incomplete_details": null,
      "tools": [
          "type": "code_interpreter"
      ],
      "tool_resources": {
        "code_interpreter": {
          "file_ids": [
            "file-abc123",
            "file-abc456"
          ]
      "metadata": {},
      "usage": {
        "prompt_tokens": 123,
        "completion_tokens": 456,
        "total_tokens": 579
      "temperature": 1.0,
      "top_p": 1.0,
      "max_prompt_tokens": 1000,
      "max_completion_tokens": 1000,
      "truncation_strategy": {
        "type": "auto",
        "last_messages": null
      "response_format": "auto",
      "tool_choice": "auto",
      "parallel_tool_calls": true
  ],
  "first_id": "run_abc123",
  "last_id": "run_abc456",
  "has_more": false
