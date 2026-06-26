<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/threads/subresources/runs/methods/cancel/ -->

[Skip to content](#_top)

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Threads](/api/reference/resources/beta/subresources/threads)

[Runs](/api/reference/resources/beta/subresources/threads/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Cancel a run

Deprecated: The Assistants API is deprecated in favor of the Responses API

POST/threads/{thread\_id}/runs/{run\_id}/cancel

Cancels a run that is `in_progress`.

##### Path ParametersExpand Collapse

thread\_id: string

run\_id: string

##### ReturnsExpand Collapse

Run object { id, assistant\_id, cancelled\_at, 24 more }

Represents an execution run on a [thread](/docs/api-reference/threads).

id: string

The identifier, which can be referenced in API endpoints.

assistant\_id: string

The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: number

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: number

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: number

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: number

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: number

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: object { reason }

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: optional "max\_completion\_tokens" or "max\_prompt\_tokens"

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: string

The instructions that the [assistant](/docs/api-reference/assistants) used for this run.

last\_error: object { code, message }

The last error associated with this run. Will be `null` if there are no errors.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt"

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: string

A human-readable description of the error.

max\_completion\_tokens: number

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: number

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: [Metadata](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that the [assistant](/docs/api-reference/assistants) used for this run.

object: "thread.run"

The object type, which is always `thread.run`.

parallel\_tool\_calls: boolean

Whether to enable [parallel function calling](/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: object { submit\_tool\_outputs, type }

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: object { tool\_calls }

Details on the tool outputs needed for this run to continue.

tool\_calls: array of [RequiredActionFunctionToolCall](/api/reference/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema)) { id, function, type }

A list of the relevant tool calls.

id: string

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.

function: object { arguments, name }

The function definition.

arguments: string

The arguments that the model expects you to pass to the function.

name: string

The name of the function.

type: "function"

The type of tool call the output is required for. For now, this is always `function`.

type: "submit\_tool\_outputs"

For now, this is always `submit_tool_outputs`.

response\_format: [AssistantResponseFormatOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](/docs/models#gpt-4o), [GPT-4 Turbo](/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

"auto"

`auto` is the default value

ResponseFormatText object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

ResponseFormatJSONSchema object { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

json\_schema: object { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: optional map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

started\_at: number

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: "queued" or "in\_progress" or "requires\_action" or 6 more

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

thread\_id: string

The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: [AssistantToolChoiceOption](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_option%20%3E%20(schema))

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

"none" or "auto" or "required"

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

AssistantToolChoice object { type, function }

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: "function" or "code\_interpreter" or "file\_search"

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: optional [AssistantToolChoiceFunction](/api/reference/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_tool_choice_function%20%3E%20(schema)) { name }

name: string

The name of the function to call.

tools: array of [CodeInterpreterTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20code_interpreter_tool%20%3E%20(schema)) { type }  or [FileSearchTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20file_search_tool%20%3E%20(schema)) { type, file\_search }  or [FunctionTool](/api/reference/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20function_tool%20%3E%20(schema)) { function, type }

The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.

One of the following:

CodeInterpreterTool object { type }

type: "code\_interpreter"

The type of tool being defined: `code_interpreter`

FileSearchTool object { type, file\_search }

type: "file\_search"

The type of tool being defined: `file_search`

file\_search: optional object { max\_num\_results, ranking\_options }

Overrides for the file search tool.

max\_num\_results: optional number

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: optional object { score\_threshold, ranker }

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: number

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: optional "auto" or "default\_2024\_08\_21"

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

FunctionTool object { function, type }

function: [FunctionDefinition](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: optional string

A description of what the function does, used by the model to choose when and how to call the function.

parameters: optional [FunctionParameters](/api/reference/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: optional boolean

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](/docs/guides/function-calling).

type: "function"

The type of tool being defined: `function`

truncation\_strategy: object { type, last\_messages }

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: "auto" or "last\_messages"

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: optional number

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: object { completion\_tokens, prompt\_tokens, total\_tokens }

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: number

Number of completion tokens used over the course of the run.

prompt\_tokens: number

Number of prompt tokens used over the course of the run.

total\_tokens: number

Total number of tokens used (prompt + completion).

temperature: optional number

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: optional number

The nucleus sampling value used for this run. If not set, defaults to 1.

### Cancel a run

HTTP

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

curl https://api.openai.com/v1/threads/thread_abc123/runs/run_abc123/cancel \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v2" \
  -X POST

  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076126,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "cancelling",
  "started_at": 1699076126,
  "expires_at": 1699076726,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4o",
  "instructions": "You summarize books.",
  "tools": [
      "type": "file_search"
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_123"]
  "metadata": {},
  "usage": null,
  "temperature": 1.0,
  "top_p": 1.0,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true

##### Returns Examples

  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076126,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "cancelling",
  "started_at": 1699076126,
  "expires_at": 1699076726,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "last_error": null,
  "model": "gpt-4o",
  "instructions": "You summarize books.",
  "tools": [
      "type": "file_search"
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": ["vs_123"]
  "metadata": {},
  "usage": null,
  "temperature": 1.0,
  "top_p": 1.0,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true
