<!-- source: https://developers.openai.com/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/list/ -->

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

# List runs

Deprecated: The Assistants API is deprecated in favor of the Responses API

RunListPage beta().threads().runs().list(RunListParamsparams = RunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/threads/{thread\_id}/runs

Returns a list of runs belonging to a thread.

##### ParametersExpand Collapse

RunListParams params

Optional<String> threadId

Optional<String> after

A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj\_foo, your subsequent call can include after=obj\_foo in order to fetch the next page of the list.

Optional<String> before

A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with obj\_foo, your subsequent call can include before=obj\_foo in order to fetch the previous page of the list.

Optional<Long> limit

A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

Optional<[Order](/api/reference/java/resources/beta/subresources/threads/subresources/runs/methods/list#(resource)%20beta.threads.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

ASC("asc")

DESC("desc")

##### ReturnsExpand Collapse

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

One of the following:

JsonValue;

class ResponseFormatText:

Default response format. Used to generate text responses.

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class ResponseFormatJsonObject:

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

class ResponseFormatJsonSchema:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JsonSchema jsonSchema

Structured Outputs configuration options, including a JSON Schema.

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Schema> schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<Long> startedAt

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

[RunStatus](/api/reference/java/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema)) status

The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, `incomplete`, or `expired`.

One of the following:

QUEUED("queued")

IN\_PROGRESS("in\_progress")

REQUIRES\_ACTION("requires\_action")

CANCELLING("cancelling")

CANCELLED("cancelled")

FAILED("failed")

COMPLETED("completed")

INCOMPLETE("incomplete")

EXPIRED("expired")

String threadId

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

Optional<[AssistantToolChoiceOption](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))> toolChoice

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Auto

One of the following:

NONE("none")

AUTO("auto")

REQUIRED("required")

class AssistantToolChoice:

Specifies a tool the model should use. Use to force the model to call a specific tool.

Type type

The type of the tool. If type is `function`, the function name must be set

One of the following:

FUNCTION("function")

CODE\_INTERPRETER("code\_interpreter")

FILE\_SEARCH("file\_search")

Optional<[AssistantToolChoiceFunction](/api/reference/java/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema))> function

String name

The name of the function to call.

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

String name

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Optional<String> description

A description of what the function does, used by the model to choose when and how to call the function.

Optional<[FunctionParameters](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))> parameters

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

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

### List runs

Java

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package com.openai.example;

import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.beta.threads.runs.RunListPage;
import com.openai.models.beta.threads.runs.RunListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunListPage page = client.beta().threads().runs().list("thread_id");

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
