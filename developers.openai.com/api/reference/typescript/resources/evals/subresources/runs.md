<!-- source: https://developers.openai.com/api/reference/typescript/resources/evals/subresources/runs/ -->

[Skip to content](#_top)

[API Reference](/api/reference/typescript)

[Evals](/api/reference/typescript/resources/evals)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Runs

Manage and run evals in the OpenAI platform.

##### [Get eval runs](/api/reference/typescript/resources/evals/subresources/runs/methods/list)

client.evals.runs.list(stringevalID, RunListParams { after, limit, order, status } query?, RequestOptionsoptions?): CursorPage<[RunListResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_list_response%20%3E%20(schema)) { id, created\_at, data\_source, 11 more } >

GET/evals/{eval\_id}/runs

##### [Create eval run](/api/reference/typescript/resources/evals/subresources/runs/methods/create)

client.evals.runs.create(stringevalID, RunCreateParams { data\_source, metadata, name } body, RequestOptionsoptions?): [RunCreateResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_create_response%20%3E%20(schema)) { id, created\_at, data\_source, 11 more }

POST/evals/{eval\_id}/runs

##### [Get an eval run](/api/reference/typescript/resources/evals/subresources/runs/methods/retrieve)

client.evals.runs.retrieve(stringrunID, RunRetrieveParams { eval\_id } params, RequestOptionsoptions?): [RunRetrieveResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_retrieve_response%20%3E%20(schema)) { id, created\_at, data\_source, 11 more }

GET/evals/{eval\_id}/runs/{run\_id}

##### [Cancel eval run](/api/reference/typescript/resources/evals/subresources/runs/methods/cancel)

client.evals.runs.cancel(stringrunID, RunCancelParams { eval\_id } params, RequestOptionsoptions?): [RunCancelResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_cancel_response%20%3E%20(schema)) { id, created\_at, data\_source, 11 more }

POST/evals/{eval\_id}/runs/{run\_id}

##### [Delete eval run](/api/reference/typescript/resources/evals/subresources/runs/methods/delete)

client.evals.runs.delete(stringrunID, RunDeleteParams { eval\_id } params, RequestOptionsoptions?): [RunDeleteResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_delete_response%20%3E%20(schema)) { deleted, object, run\_id }

DELETE/evals/{eval\_id}/runs/{run\_id}

##### ModelsExpand Collapse

CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | StoredCompletions { type, created\_after, created\_before, 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: "stored\_completions"

The type of source. Always `stored_completions`.

created\_after?: number | null

An optional Unix timestamp to filter items created after this time.

created\_before?: number | null

An optional Unix timestamp to filter items created before this time.

limit?: number | null

An optional maximum number of items to return.

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string | null

An optional model to filter by (e.g., ‘gpt-4o’).

type: "completions"

The type of run data source. Always `completions`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<[EasyInputMessage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputMessageContentList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

ResponseInputMessageContentList = Array<[ResponseInputContent](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, response\_format, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format?: [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

tools?: Array<[ChatCompletionFunctionTool](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } >

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent { content, type }  | FileID { id, type }

Determines what populates the `item` namespace in the data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

type: "jsonl"

The type of data source. Always `jsonl`.

EvalAPIError { code, message }

An object representing an error response from the Eval API.

code: string

The error code.

message: string

The error message.

RunListResponse { id, created\_at, data\_source, 11 more }

A schema representing an evaluation run.

id: string

Unique identifier for the evaluation run.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | Responses { source, type, input\_messages, 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent { content, type }  | FileID { id, type }

Determines what populates the `item` namespace in the data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

type: "jsonl"

The type of data source. Always `jsonl`.

CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | StoredCompletions { type, created\_after, created\_before, 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: "stored\_completions"

The type of source. Always `stored_completions`.

created\_after?: number | null

An optional Unix timestamp to filter items created after this time.

created\_before?: number | null

An optional Unix timestamp to filter items created before this time.

limit?: number | null

An optional maximum number of items to return.

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string | null

An optional model to filter by (e.g., ‘gpt-4o’).

type: "completions"

The type of run data source. Always `completions`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<[EasyInputMessage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputMessageContentList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

ResponseInputMessageContentList = Array<[ResponseInputContent](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, response\_format, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format?: [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

tools?: Array<[ChatCompletionFunctionTool](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } >

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

Responses { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | Responses { type, created\_after, created\_before, 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: "responses"

The type of run data source. Always `responses`.

created\_after?: number | null

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before?: number | null

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search?: string | null

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata?: unknown

Metadata filter for the responses. This is a query parameter used to select responses.

model?: string | null

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature?: number | null

Sampling temperature. This is a query parameter used to select responses.

tools?: Array<string> | null

List of tool names. This is a query parameter used to select responses.

top\_p?: number | null

Nucleus sampling parameter. This is a query parameter used to select responses.

users?: Array<string> | null

List of user identifiers. This is a query parameter used to select responses.

type: "responses"

The type of run data source. Always `responses`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<ChatMessage { content, role }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage { content, role }

content: string

The content of the message.

role: string

The role of the message (e.g. “system”, “assistant”, “user”).

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.name”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, seed, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

text?: Text { format }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [ResponseFormatTextConfig](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools?: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

eval\_id: string

The identifier of the associated evaluation.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that is evaluated, if applicable.

name: string

The name of the evaluation run.

object: "eval.run"

The type of the object. Always “eval.run”.

per\_model\_usage: Array<PerModelUsage>

Usage statistics for each model during the evaluation run.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

invocation\_count: number

The number of invocations.

model\_name: string

The name of the model.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

per\_testing\_criteria\_results: Array<PerTestingCriteriaResult>

Results per testing criteria applied during the evaluation run.

failed: number

Number of tests failed for this criteria.

passed: number

Number of tests passed for this criteria.

testing\_criteria: string

A description of the testing criteria.

report\_url: string

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts { errored, failed, passed, total }

Counters summarizing the outcomes of the evaluation run.

errored: number

Number of output items that resulted in an error.

failed: number

Number of output items that failed to pass the evaluation.

passed: number

Number of output items that passed the evaluation.

total: number

Total number of executed output items.

status: string

The status of the evaluation run.

RunCreateResponse { id, created\_at, data\_source, 11 more }

A schema representing an evaluation run.

id: string

Unique identifier for the evaluation run.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | Responses { source, type, input\_messages, 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent { content, type }  | FileID { id, type }

Determines what populates the `item` namespace in the data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

type: "jsonl"

The type of data source. Always `jsonl`.

CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | StoredCompletions { type, created\_after, created\_before, 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: "stored\_completions"

The type of source. Always `stored_completions`.

created\_after?: number | null

An optional Unix timestamp to filter items created after this time.

created\_before?: number | null

An optional Unix timestamp to filter items created before this time.

limit?: number | null

An optional maximum number of items to return.

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string | null

An optional model to filter by (e.g., ‘gpt-4o’).

type: "completions"

The type of run data source. Always `completions`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<[EasyInputMessage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputMessageContentList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

ResponseInputMessageContentList = Array<[ResponseInputContent](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, response\_format, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format?: [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

tools?: Array<[ChatCompletionFunctionTool](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } >

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

Responses { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | Responses { type, created\_after, created\_before, 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: "responses"

The type of run data source. Always `responses`.

created\_after?: number | null

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before?: number | null

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search?: string | null

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata?: unknown

Metadata filter for the responses. This is a query parameter used to select responses.

model?: string | null

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature?: number | null

Sampling temperature. This is a query parameter used to select responses.

tools?: Array<string> | null

List of tool names. This is a query parameter used to select responses.

top\_p?: number | null

Nucleus sampling parameter. This is a query parameter used to select responses.

users?: Array<string> | null

List of user identifiers. This is a query parameter used to select responses.

type: "responses"

The type of run data source. Always `responses`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<ChatMessage { content, role }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage { content, role }

content: string

The content of the message.

role: string

The role of the message (e.g. “system”, “assistant”, “user”).

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.name”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, seed, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

text?: Text { format }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [ResponseFormatTextConfig](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools?: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

eval\_id: string

The identifier of the associated evaluation.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that is evaluated, if applicable.

name: string

The name of the evaluation run.

object: "eval.run"

The type of the object. Always “eval.run”.

per\_model\_usage: Array<PerModelUsage>

Usage statistics for each model during the evaluation run.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

invocation\_count: number

The number of invocations.

model\_name: string

The name of the model.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

per\_testing\_criteria\_results: Array<PerTestingCriteriaResult>

Results per testing criteria applied during the evaluation run.

failed: number

Number of tests failed for this criteria.

passed: number

Number of tests passed for this criteria.

testing\_criteria: string

A description of the testing criteria.

report\_url: string

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts { errored, failed, passed, total }

Counters summarizing the outcomes of the evaluation run.

errored: number

Number of output items that resulted in an error.

failed: number

Number of output items that failed to pass the evaluation.

passed: number

Number of output items that passed the evaluation.

total: number

Total number of executed output items.

status: string

The status of the evaluation run.

RunRetrieveResponse { id, created\_at, data\_source, 11 more }

A schema representing an evaluation run.

id: string

Unique identifier for the evaluation run.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | Responses { source, type, input\_messages, 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent { content, type }  | FileID { id, type }

Determines what populates the `item` namespace in the data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

type: "jsonl"

The type of data source. Always `jsonl`.

CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | StoredCompletions { type, created\_after, created\_before, 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: "stored\_completions"

The type of source. Always `stored_completions`.

created\_after?: number | null

An optional Unix timestamp to filter items created after this time.

created\_before?: number | null

An optional Unix timestamp to filter items created before this time.

limit?: number | null

An optional maximum number of items to return.

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string | null

An optional model to filter by (e.g., ‘gpt-4o’).

type: "completions"

The type of run data source. Always `completions`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<[EasyInputMessage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputMessageContentList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

ResponseInputMessageContentList = Array<[ResponseInputContent](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, response\_format, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format?: [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

tools?: Array<[ChatCompletionFunctionTool](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } >

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

Responses { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | Responses { type, created\_after, created\_before, 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: "responses"

The type of run data source. Always `responses`.

created\_after?: number | null

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before?: number | null

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search?: string | null

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata?: unknown

Metadata filter for the responses. This is a query parameter used to select responses.

model?: string | null

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature?: number | null

Sampling temperature. This is a query parameter used to select responses.

tools?: Array<string> | null

List of tool names. This is a query parameter used to select responses.

top\_p?: number | null

Nucleus sampling parameter. This is a query parameter used to select responses.

users?: Array<string> | null

List of user identifiers. This is a query parameter used to select responses.

type: "responses"

The type of run data source. Always `responses`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<ChatMessage { content, role }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage { content, role }

content: string

The content of the message.

role: string

The role of the message (e.g. “system”, “assistant”, “user”).

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.name”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, seed, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

text?: Text { format }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [ResponseFormatTextConfig](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools?: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

eval\_id: string

The identifier of the associated evaluation.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that is evaluated, if applicable.

name: string

The name of the evaluation run.

object: "eval.run"

The type of the object. Always “eval.run”.

per\_model\_usage: Array<PerModelUsage>

Usage statistics for each model during the evaluation run.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

invocation\_count: number

The number of invocations.

model\_name: string

The name of the model.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

per\_testing\_criteria\_results: Array<PerTestingCriteriaResult>

Results per testing criteria applied during the evaluation run.

failed: number

Number of tests failed for this criteria.

passed: number

Number of tests passed for this criteria.

testing\_criteria: string

A description of the testing criteria.

report\_url: string

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts { errored, failed, passed, total }

Counters summarizing the outcomes of the evaluation run.

errored: number

Number of output items that resulted in an error.

failed: number

Number of output items that failed to pass the evaluation.

passed: number

Number of output items that passed the evaluation.

total: number

Total number of executed output items.

status: string

The status of the evaluation run.

RunCancelResponse { id, created\_at, data\_source, 11 more }

A schema representing an evaluation run.

id: string

Unique identifier for the evaluation run.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | Responses { source, type, input\_messages, 2 more }

Information about the run’s data source.

One of the following:

CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent { content, type }  | FileID { id, type }

Determines what populates the `item` namespace in the data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

type: "jsonl"

The type of data source. Always `jsonl`.

CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | StoredCompletions { type, created\_after, created\_before, 3 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: "stored\_completions"

The type of source. Always `stored_completions`.

created\_after?: number | null

An optional Unix timestamp to filter items created after this time.

created\_before?: number | null

An optional Unix timestamp to filter items created before this time.

limit?: number | null

An optional maximum number of items to return.

metadata?: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model?: string | null

An optional model to filter by (e.g., ‘gpt-4o’).

type: "completions"

The type of run data source. Always `completions`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<[EasyInputMessage](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputMessageContentList](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

string

ResponseInputMessageContentList = Array<[ResponseInputContent](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

A list of one or many input items to the model, containing different content
types.

One of the following:

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

"low"

"high"

"auto"

"original"

type: "input\_image"

The type of the input item. Always `input_image`.

file\_id?: string | null

The ID of the file to be sent to the model.

image\_url?: string | null

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: "input\_file"

The type of the input item. Always `input_file`.

detail?: "low" | "high"

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

"low"

"high"

file\_data?: string

The content of the file to be sent to the model.

file\_id?: string | null

The ID of the file to be sent to the model.

file\_url?: string

The URL of the file to be sent to the model.

formaturi

filename?: string

The name of the file to be sent to the model.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

phase?: "commentary" | "final\_answer" | null

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

"commentary"

"final\_answer"

type?: "message"

The type of the message input. Always `message`.

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, response\_format, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

response\_format?: [ResponseFormatText](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

ResponseFormatText { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema { name, description, schema, strict }

Structured Outputs configuration options, including a JSON Schema.

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description?: string

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema?: Record<string, unknown>

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict?: boolean | null

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

tools?: Array<[ChatCompletionFunctionTool](/api/reference/typescript/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } >

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: "function"

The type of the tool. Currently, only `function` is supported.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

Responses { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent { content, type }  | FileID { id, type }  | Responses { type, created\_after, created\_before, 8 more }

Determines what populates the `item` namespace in this run’s data source.

One of the following:

FileContent { content, type }

content: Array<Content>

The content of the jsonl file.

item: Record<string, unknown>

sample?: Record<string, unknown>

type: "file\_content"

The type of jsonl source. Always `file_content`.

FileID { id, type }

id: string

The identifier of the file.

type: "file\_id"

The type of jsonl source. Always `file_id`.

Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: "responses"

The type of run data source. Always `responses`.

created\_after?: number | null

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before?: number | null

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search?: string | null

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata?: unknown

Metadata filter for the responses. This is a query parameter used to select responses.

model?: string | null

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

temperature?: number | null

Sampling temperature. This is a query parameter used to select responses.

tools?: Array<string> | null

List of tool names. This is a query parameter used to select responses.

top\_p?: number | null

Nucleus sampling parameter. This is a query parameter used to select responses.

users?: Array<string> | null

List of user identifiers. This is a query parameter used to select responses.

type: "responses"

The type of run data source. Always `responses`.

input\_messages?: Template { template, type }  | ItemReference { item\_reference, type }

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

Template { template, type }

template: Array<ChatMessage { content, role }  | EvalItem { content, role, type } >

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

ChatMessage { content, role }

content: string

The content of the message.

role: string

The role of the message (e.g. “system”, “assistant”, “user”).

EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

GraderInputs = Array<string | [ResponseInputText](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText { text, type }  | 2 more>

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

string

ResponseInputText { text, type }

A text input to the model.

text: string

The text input to the model.

type: "input\_text"

The type of the input item. Always `input_text`.

OutputText { text, type }

A text output from the model.

text: string

The text output from the model.

type: "output\_text"

The type of the output text. Always `output_text`.

InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: string

The URL of the image input.

formaturi

type: "input\_image"

The type of the image input. Always `input_image`.

detail?: string

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio { data, format }

data: string

Base64-encoded audio data.

format: "mp3" | "wav"

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

"mp3"

"wav"

type: "input\_audio"

The type of the input item. Always `input_audio`.

role: "user" | "assistant" | "system" | "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

"user"

"assistant"

"system"

"developer"

type?: "message"

The type of the message input. Always `message`.

type: "template"

The type of input messages. Always `template`.

ItemReference { item\_reference, type }

item\_reference: string

A reference to a variable in the `item` namespace. Ie, “item.name”

type: "item\_reference"

The type of input messages. Always `item_reference`.

model?: string

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params?: SamplingParams { max\_completion\_tokens, reasoning\_effort, seed, 4 more }

max\_completion\_tokens?: number

The maximum number of tokens in the generated output.

reasoning\_effort?: [ReasoningEffort](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema)) | null

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

seed?: number

A seed value to initialize the randomness, during sampling.

temperature?: number

A higher temperature increases randomness in the outputs.

text?: Text { format }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format?: [ResponseFormatTextConfig](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

tools?: Array<[Tool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

The two categories of tools you can provide the model are:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](https://platform.openai.com/docs/guides/tools-web-search)
  or [file search](https://platform.openai.com/docs/guides/tools-file-search). Learn more about
  [built-in tools](https://platform.openai.com/docs/guides/tools).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code. Learn more about
  [function calling](https://platform.openai.com/docs/guides/function-calling).

One of the following:

FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: string

The name of the function to call.

parameters: Record<string, unknown> | null

A JSON schema object describing the parameters of the function.

strict: boolean | null

Whether to enforce strict parameter validation. Default `true`.

type: "function"

The type of the function tool. Always `function`.

defer\_loading?: boolean

Whether this function is deferred and loaded via tool search.

description?: string | null

A description of the function. Used by the model to determine whether or not to call the function.

FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: "file\_search"

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array<string>

The IDs of the vector stores to search.

filters?: [ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }  | null

A filter to apply.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array<[ComparisonFilter](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | unknown>

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: string

The key to compare against the value.

type: "eq" | "ne" | "gt" | 5 more

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`, `in`, `nin`.

* `eq`: equals
* `ne`: not equal
* `gt`: greater than
* `gte`: greater than or equal
* `lt`: less than
* `lte`: less than or equal
* `in`: in
* `nin`: not in

One of the following:

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

Type of operation: `and` or `or`.

One of the following:

"and"

"or"

max\_num\_results?: number

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

Ranking options for search.

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: number

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: number

The weight of the text in the reciprocal ranking fusion.

ranker?: "auto" | "default-2024-11-15"

The ranker to use for the file search.

One of the following:

"auto"

"default-2024-11-15"

score\_threshold?: number

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: "computer"

The type of the computer tool. Always `computer`.

ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: number

The height of the computer display.

display\_width: number

The width of the computer display.

environment: "windows" | "mac" | "linux" | 2 more

The type of computer environment to control.

One of the following:

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

The type of the computer use tool. Always `computer_use_preview`.

WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

Filters for the search.

allowed\_domains?: Array<string> | null

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The approximate location of the user.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type?: "approximate"

The type of location approximation. Always `approximate`.

Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

A label for this MCP server, used to identify it in tool calls.

type: "mcp"

The type of the MCP tool. Always `mcp`.

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

List of allowed tool names or a filter object.

One of the following:

Array<string>

McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

authorization?: string

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

Identifier for service connectors, like those available in ChatGPT. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided. Learn more
about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

Currently supported `connector_id` values are:

* Dropbox: `connector_dropbox`
* Gmail: `connector_gmail`
* Google Calendar: `connector_googlecalendar`
* Google Drive: `connector_googledrive`
* Microsoft Teams: `connector_microsoftteams`
* Outlook Calendar: `connector_outlookcalendar`
* Outlook Email: `connector_outlookemail`
* SharePoint: `connector_sharepoint`

One of the following:

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

Whether this MCP tool is deferred and discovered via tool search.

headers?: Record<string, string> | null

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

Specify which of the MCP server’s tools require approval.

One of the following:

McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always?: Always { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

never?: Never { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only?: boolean

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names?: Array<string>

List of allowed tool names.

"always" | "never"

"always"

"never"

server\_description?: string

Optional description of the MCP server, used to provide more context.

server\_url?: string

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id?: string

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: "auto"

Always `auto`.

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the code interpreter container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

type: "code\_interpreter"

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

The type of the image generation tool. Always `image_generation`.

action?: "generate" | "edit" | "auto"

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

One of the following:

"transparent"

"opaque"

"auto"

input\_fidelity?: "high" | "low" | null

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id?: string

File ID for the mask image.

image\_url?: string

Base64-encoded mask image.

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

Moderation level for the generated image. Default: `auto`.

One of the following:

"auto"

"low"

output\_compression?: number

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

"png"

"webp"

"jpeg"

partial\_images?: number

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: "shell"

The type of the shell tool. Always `shell`.

environment?: [ContainerAuto](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }  | null

One of the following:

ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

Automatically creates a container for this request

file\_ids?: Array<string>

An optional list of uploaded files to make available to your code.

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

The memory limit for the container.

One of the following:

"1g"

"4g"

"16g"

"64g"

network\_policy?: [ContainerNetworkPolicyDisabled](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

ContainerNetworkPolicyDisabled { type }

type: "disabled"

Disable outbound network access. Always `disabled`.

ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

A list of allowed domains when type is `allowlist`.

type: "allowlist"

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets?: Array<[ContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

Optional domain-scoped secrets for allowlisted domains.

domain: string

The domain associated with the secret.

minLength1

name: string

The name of the secret to inject for the domain.

minLength1

value: string

The secret value to inject for the domain.

maxLength10485760

minLength1

skills?: Array<[SkillReference](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } >

An optional list of skills referenced by id or inline data.

One of the following:

SkillReference { skill\_id, type, version }

skill\_id: string

The ID of the referenced skill.

maxLength64

minLength1

type: "skill\_reference"

References a skill created with the /v1/skills endpoint.

version?: string

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

InlineSkill { description, name, source, type }

description: string

The description of the skill.

name: string

The name of the skill.

source: [InlineSkillSource](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

type: "inline"

Defines an inline skill for this request.

LocalEnvironment { type, skills }

type: "local"

Use a local computer environment.

skills?: Array<[LocalSkill](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } >

An optional list of skills.

description: string

The description of the skill.

name: string

The name of the skill.

path: string

The path to the directory containing the skill.

ContainerReference { container\_id, type }

container\_id: string

The ID of the referenced container.

type: "container\_reference"

References a container created with the /v1/containers endpoint

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: string

A description of the namespace shown to the model.

minLength1

name: string

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array<Function { name, type, defer\_loading, 3 more }  | [CustomTool](/api/reference/typescript/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } >

The function/custom tools available inside this namespace.

One of the following:

Function { name, type, defer\_loading, 3 more }

name: string

maxLength128

minLength1

type: "function"

defer\_loading?: boolean

Whether this function should be deferred and discovered via tool search.

description?: string | null

parameters?: unknown

strict?: boolean | null

CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

The name of the custom tool, used to identify it in tool calls.

type: "custom"

The type of the custom tool. Always `custom`.

defer\_loading?: boolean

Whether this tool should be deferred and discovered via tool search.

description?: string

Optional description of the custom tool, used to provide more context.

format?: [CustomToolInputFormat](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

type: "namespace"

The type of the tool. Always `namespace`.

ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: "tool\_search"

The type of the tool. Always `tool_search`.

description?: string | null

Description shown to the model for a client-executed tool search tool.

execution?: "server" | "client"

Whether tool search is executed by the server or by the client.

One of the following:

"server"

"client"

parameters?: unknown

Parameter schema for a client-executed tool search tool.

WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

One of the following:

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location?: UserLocation | null

The user’s location.

type: "approximate"

The type of location approximation. Always `approximate`.

city?: string | null

Free text input for the city of the user, e.g. `San Francisco`.

country?: string | null

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region?: string | null

Free text input for the region of the user, e.g. `California`.

timezone?: string | null

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: "apply\_patch"

The type of the tool. Always `apply_patch`.

top\_p?: number

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

eval\_id: string

The identifier of the associated evaluation.

metadata: [Metadata](/api/reference/typescript/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema)) | null

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: string

The model that is evaluated, if applicable.

name: string

The name of the evaluation run.

object: "eval.run"

The type of the object. Always “eval.run”.

per\_model\_usage: Array<PerModelUsage>

Usage statistics for each model during the evaluation run.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

invocation\_count: number

The number of invocations.

model\_name: string

The name of the model.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

per\_testing\_criteria\_results: Array<PerTestingCriteriaResult>

Results per testing criteria applied during the evaluation run.

failed: number

Number of tests failed for this criteria.

passed: number

Number of tests passed for this criteria.

testing\_criteria: string

A description of the testing criteria.

report\_url: string

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts { errored, failed, passed, total }

Counters summarizing the outcomes of the evaluation run.

errored: number

Number of output items that resulted in an error.

failed: number

Number of output items that failed to pass the evaluation.

passed: number

Number of output items that passed the evaluation.

total: number

Total number of executed output items.

status: string

The status of the evaluation run.

RunDeleteResponse { deleted, object, run\_id }

deleted?: boolean

object?: string

run\_id?: string

#### RunsOutput Items

Manage and run evals in the OpenAI platform.

##### [Get eval run output items](/api/reference/typescript/resources/evals/subresources/runs/subresources/output_items/methods/list)

client.evals.runs.outputItems.list(stringrunID, OutputItemListParams { eval\_id, after, limit, 2 more } params, RequestOptionsoptions?): CursorPage<[OutputItemListResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_list_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more } >

GET/evals/{eval\_id}/runs/{run\_id}/output\_items

##### [Get an output item of an eval run](/api/reference/typescript/resources/evals/subresources/runs/subresources/output_items/methods/retrieve)

client.evals.runs.outputItems.retrieve(stringoutputItemID, OutputItemRetrieveParams { eval\_id, run\_id } params, RequestOptionsoptions?): [OutputItemRetrieveResponse](/api/reference/typescript/resources/evals#(resource)%20evals.runs.output_items%20%3E%20(model)%20output_item_retrieve_response%20%3E%20(schema)) { id, created\_at, datasource\_item, 7 more }

GET/evals/{eval\_id}/runs/{run\_id}/output\_items/{output\_item\_id}

##### ModelsExpand Collapse

OutputItemListResponse { id, created\_at, datasource\_item, 7 more }

A schema representing an evaluation run output item.

id: string

Unique identifier for the evaluation run output item.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Record<string, unknown>

Details of the input data source item.

datasource\_item\_id: number

The identifier for the data source item.

eval\_id: string

The identifier of the evaluation group.

object: "eval.run.output\_item"

The type of the object. Always “eval.run.output\_item”.

results: Array<Result>

A list of grader results for this output item.

name: string

The name of the grader.

passed: boolean

Whether the grader considered the output a pass.

score: number

The numeric score produced by the grader.

sample?: Record<string, unknown> | null

Optional sample or intermediate data produced by the grader.

type?: string

The grader type (for example, “string-check-grader”).

run\_id: string

The identifier of the evaluation run associated with this output item.

sample: Sample { error, finish\_reason, input, 7 more }

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

finish\_reason: string

The reason why the sample generation was finished.

input: Array<Input>

An array of input messages.

content: string

The content of the message.

role: string

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: number

The maximum number of tokens allowed for completion.

model: string

The model used for generating the sample.

output: Array<Output>

An array of output messages.

content?: string

The content of the message.

role?: string

The role of the message (e.g. “system”, “assistant”, “user”).

seed: number

The seed used for generating the sample.

temperature: number

The sampling temperature used.

top\_p: number

The top\_p value used for sampling.

usage: Usage { cached\_tokens, completion\_tokens, prompt\_tokens, total\_tokens }

Token usage details for the sample.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

status: string

The status of the evaluation run.

OutputItemRetrieveResponse { id, created\_at, datasource\_item, 7 more }

A schema representing an evaluation run output item.

id: string

Unique identifier for the evaluation run output item.

created\_at: number

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

datasource\_item: Record<string, unknown>

Details of the input data source item.

datasource\_item\_id: number

The identifier for the data source item.

eval\_id: string

The identifier of the evaluation group.

object: "eval.run.output\_item"

The type of the object. Always “eval.run.output\_item”.

results: Array<Result>

A list of grader results for this output item.

name: string

The name of the grader.

passed: boolean

Whether the grader considered the output a pass.

score: number

The numeric score produced by the grader.

sample?: Record<string, unknown> | null

Optional sample or intermediate data produced by the grader.

type?: string

The grader type (for example, “string-check-grader”).

run\_id: string

The identifier of the evaluation run associated with this output item.

sample: Sample { error, finish\_reason, input, 7 more }

A sample containing the input and output of the evaluation run.

error: [EvalAPIError](/api/reference/typescript/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

finish\_reason: string

The reason why the sample generation was finished.

input: Array<Input>

An array of input messages.

content: string

The content of the message.

role: string

The role of the message sender (e.g., system, user, developer).

max\_completion\_tokens: number

The maximum number of tokens allowed for completion.

model: string

The model used for generating the sample.

output: Array<Output>

An array of output messages.

content?: string

The content of the message.

role?: string

The role of the message (e.g. “system”, “assistant”, “user”).

seed: number

The seed used for generating the sample.

temperature: number

The sampling temperature used.

top\_p: number

The top\_p value used for sampling.

usage: Usage { cached\_tokens, completion\_tokens, prompt\_tokens, total\_tokens }

Token usage details for the sample.

cached\_tokens: number

The number of tokens retrieved from cache.

completion\_tokens: number

The number of completion tokens generated.

prompt\_tokens: number

The number of prompt tokens used.

total\_tokens: number

The total number of tokens used.

status: string

The status of the evaluation run.
