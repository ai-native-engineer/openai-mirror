<!-- source: https://developers.openai.com/api/reference/ruby/resources/evals/subresources/runs/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Evals](/api/reference/ruby/resources/evals)

[Runs](/api/reference/ruby/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create eval run

evals.runs.create(eval\_id, \*\*kwargs) -> [RunCreateResponse](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20run_create_response%20%3E%20(schema)) { id, created\_at, data\_source, 11 more }

POST/evals/{eval\_id}/runs

Kicks off a new run for a given evaluation, specifying the data source, and what model configuration to use to test. The datasource will be validated against the schema specified in the config of the evaluation.

##### ParametersExpand Collapse

eval\_id: String

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | CreateEvalResponsesRunDataSource{ source, type, input\_messages, 2 more}

Details about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent{ content, type} | FileID{ id, type}

Determines what populates the `item` namespace in the data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

type: :jsonl

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent{ content, type} | FileID{ id, type} | StoredCompletions{ type, created\_after, created\_before, 3 more}

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

class StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: :stored\_completions

The type of source. Always `stored_completions`.

created\_after: Integer

An optional Unix timestamp to filter items created after this time.

created\_before: Integer

An optional Unix timestamp to filter items created before this time.

limit: Integer

An optional maximum number of items to return.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String

An optional model to filter by (e.g., ‘gpt-4o’).

type: :completions

The type of run data source. Always `completions`.

input\_messages: Template{ template, type} | ItemReference{ item\_reference, type}

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template { template, type }

template: Array[[EasyInputMessage](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem{ content, role, type}]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputMessageContentList](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

String = String

A text input to the model.

ResponseInputMessageContentList = Array[[ResponseInputContent](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

A list of one or many input items to the model, containing different content
types.

One of the following:

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: :low | :high | :auto | :original

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

:low

:high

:auto

:original

type: :input\_image

The type of the input item. Always `input_image`.

file\_id: String

The ID of the file to be sent to the model.

image\_url: String

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: :input\_file

The type of the input item. Always `input_file`.

detail: :low | :high

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

:low

:high

file\_data: String

The content of the file to be sent to the model.

file\_id: String

The ID of the file to be sent to the model.

file\_url: String

The URL of the file to be sent to the model.

formaturi

filename: String

The name of the file to be sent to the model.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

phase: :commentary | :final\_answer

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

:commentary

:final\_answer

type: :message

The type of the message input. Always `message`.

class EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputText](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText{ text, type} | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

GraderInputs = Array[[GraderInputItem](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))]

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

type: :message

The type of the message input. Always `message`.

type: :template

The type of input messages. Always `template`.

class ItemReference { item\_reference, type }

item\_reference: String

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: :item\_reference

The type of input messages. Always `item_reference`.

model: String

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: SamplingParams{ max\_completion\_tokens, reasoning\_effort, response\_format, 4 more}

max\_completion\_tokens: Integer

The maximum number of tokens in the generated output.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

response\_format: [ResponseFormatText](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema{ name, description, schema, strict}

Structured Outputs configuration options, including a JSON Schema.

name: String

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: String

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Hash[Symbol, untyped]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: bool

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: :json\_schema

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

tools: Array[[ChatCompletionFunctionTool](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } ]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: String

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: String

A description of what the function does, used by the model to choose when and how to call the function.

parameters: [FunctionParameters](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: bool

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: :function

The type of the tool. Currently, only `function` is supported.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class CreateEvalResponsesRunDataSource { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent{ content, type} | FileID{ id, type} | Responses{ type, created\_after, created\_before, 8 more}

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

class Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: :responses

The type of run data source. Always `responses`.

created\_after: Integer

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Integer

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: String

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: untyped

Metadata filter for the responses. This is a query parameter used to select responses.

model: String

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

temperature: Float

Sampling temperature. This is a query parameter used to select responses.

tools: Array[String]

List of tool names. This is a query parameter used to select responses.

top\_p: Float

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Array[String]

List of user identifiers. This is a query parameter used to select responses.

type: :responses

The type of run data source. Always `responses`.

input\_messages: Template{ template, type} | ItemReference{ item\_reference, type}

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template { template, type }

template: Array[ChatMessage{ content, role} | EvalItem{ content, role, type}]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class ChatMessage { content, role }

content: String

The content of the message.

role: String

The role of the message (e.g. “system”, “assistant”, “user”).

class EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputText](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText{ text, type} | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

GraderInputs = Array[[GraderInputItem](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))]

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

type: :message

The type of the message input. Always `message`.

type: :template

The type of input messages. Always `template`.

class ItemReference { item\_reference, type }

item\_reference: String

A reference to a variable in the `item` namespace. Ie, “item.name”

type: :item\_reference

The type of input messages. Always `item_reference`.

model: String

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: SamplingParams{ max\_completion\_tokens, reasoning\_effort, seed, 4 more}

max\_completion\_tokens: Integer

The maximum number of tokens in the generated output.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

text: Text{ format\_}

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format\_: [ResponseFormatTextConfig](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatTextJSONSchemaConfig { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: String

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Hash[Symbol, untyped]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: :json\_schema

The type of response format being defined. Always `json_schema`.

description: String

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: bool

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

tools: Array[[Tool](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]

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

class FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: String

The name of the function to call.

parameters: Hash[Symbol, untyped]

A JSON schema object describing the parameters of the function.

strict: bool

Whether to enforce strict parameter validation. Default `true`.

type: :function

The type of the function tool. Always `function`.

defer\_loading: bool

Whether this function is deferred and loaded via tool search.

description: String

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: :file\_search

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array[String]

The IDs of the vector stores to search.

filters: [ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }

A filter to apply.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

class CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array[[ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | untyped]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

UnionMember1 = untyped

type: :and | :or

Type of operation: `and` or `or`.

One of the following:

:and

:or

max\_num\_results: Integer

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: RankingOptions{ hybrid\_search, ranker, score\_threshold}

Ranking options for search.

hybrid\_search: HybridSearch{ embedding\_weight, text\_weight}

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: Float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: Float

The weight of the text in the reciprocal ranking fusion.

ranker: :auto | :"default-2024-11-15"

The ranker to use for the file search.

One of the following:

:auto

:"default-2024-11-15"

score\_threshold: Float

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: :computer

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: Integer

The height of the computer display.

display\_width: Integer

The width of the computer display.

environment: :windows | :mac | :linux | 2 more

The type of computer environment to control.

One of the following:

:windows

:mac

:linux

:ubuntu

:browser

type: :computer\_use\_preview

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search | :web\_search\_2025\_08\_26

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

:web\_search

:web\_search\_2025\_08\_26

filters: Filters{ allowed\_domains}

Filters for the search.

allowed\_domains: Array[String]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: :low | :medium | :high

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

:low

:medium

:high

user\_location: UserLocation{ city, country, region, 2 more}

The approximate location of the user.

city: String

Free text input for the city of the user, e.g. `San Francisco`.

country: String

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: String

Free text input for the region of the user, e.g. `California`.

timezone: String

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: :approximate

The type of location approximation. Always `approximate`.

class Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: String

A label for this MCP server, used to identify it in tool calls.

type: :mcp

The type of the MCP tool. Always `mcp`.

allowed\_tools: Array[String] | McpToolFilter{ read\_only, tool\_names}

List of allowed tool names or a filter object.

One of the following:

McpAllowedTools = Array[String]

A string array of allowed tool names

class McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

authorization: String

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: :connector\_dropbox | :connector\_gmail | :connector\_googlecalendar | 5 more

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

:connector\_dropbox

:connector\_gmail

:connector\_googlecalendar

:connector\_googledrive

:connector\_microsoftteams

:connector\_outlookcalendar

:connector\_outlookemail

:connector\_sharepoint

defer\_loading: bool

Whether this MCP tool is deferred and discovered via tool search.

headers: Hash[Symbol, String]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: McpToolApprovalFilter{ always, never} | :always | :never

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Always{ read\_only, tool\_names}

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

never: Never{ read\_only, tool\_names}

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

McpToolApprovalSetting = :always | :never

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

:always

:never

server\_description: String

Optional description of the MCP server, used to provide more context.

server\_url: String

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: String

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: String | CodeInterpreterToolAuto{ type, file\_ids, memory\_limit, network\_policy}

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String = String

The container ID.

class CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: :auto

Always `auto`.

file\_ids: Array[String]

An optional list of uploaded files to make available to your code.

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit for the code interpreter container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [ContainerNetworkPolicyDisabled](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled { type }

type: :disabled

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

A list of allowed domains when type is `allowlist`.

type: :allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Array[[ContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

Optional domain-scoped secrets for allowlisted domains.

domain: String

The domain associated with the secret.

minLength1

name: String

The name of the secret to inject for the domain.

minLength1

value: String

The secret value to inject for the domain.

maxLength10485760

minLength1

type: :code\_interpreter

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: :image\_generation

The type of the image generation tool. Always `image_generation`.

action: :generate | :edit | :auto

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

:generate

:edit

:auto

background: :transparent | :opaque | :auto

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

:transparent

:opaque

:auto

input\_fidelity: :high | :low

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

:high

:low

input\_image\_mask: InputImageMask{ file\_id, image\_url}

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: String

File ID for the mask image.

image\_url: String

Base64-encoded mask image.

model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

String = String

Model = :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

:"gpt-image-1"

:"gpt-image-1-mini"

:"gpt-image-2"

:"gpt-image-2-2026-04-21"

:"gpt-image-1.5"

:"chatgpt-image-latest"

moderation: :auto | :low

Moderation level for the generated image. Default: `auto`.

One of the following:

:auto

:low

output\_compression: Integer

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: :png | :webp | :jpeg

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

:png

:webp

:jpeg

partial\_images: Integer

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: :low | :medium | :high | :auto

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

:low

:medium

:high

:auto

size: String | :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

String = String

Size = :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

class LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: :local\_shell

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: :shell

The type of the shell tool. Always `shell`.

environment: [ContainerAuto](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }

One of the following:

class ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: :container\_auto

Automatically creates a container for this request

file\_ids: Array[String]

An optional list of uploaded files to make available to your code.

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit for the container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [ContainerNetworkPolicyDisabled](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled { type }

type: :disabled

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

A list of allowed domains when type is `allowlist`.

type: :allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Array[[ContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

Optional domain-scoped secrets for allowlisted domains.

domain: String

The domain associated with the secret.

minLength1

name: String

The name of the secret to inject for the domain.

minLength1

value: String

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Array[[SkillReference](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } ]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference { skill\_id, type, version }

skill\_id: String

The ID of the referenced skill.

maxLength64

minLength1

type: :skill\_reference

References a skill created with the /v1/skills endpoint.

version: String

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill { description, name, source, type }

description: String

The description of the skill.

name: String

The name of the skill.

source: [InlineSkillSource](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: String

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: :"application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: :base64

The type of the inline skill source. Must be `base64`.

type: :inline

Defines an inline skill for this request.

class LocalEnvironment { type, skills }

type: :local

Use a local computer environment.

skills: Array[[LocalSkill](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } ]

An optional list of skills.

description: String

The description of the skill.

name: String

The name of the skill.

path: String

The path to the directory containing the skill.

class ContainerReference { container\_id, type }

container\_id: String

The ID of the referenced container.

type: :container\_reference

References a container created with the /v1/containers endpoint

class CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

The name of the custom tool, used to identify it in tool calls.

type: :custom

The type of the custom tool. Always `custom`.

defer\_loading: bool

Whether this tool should be deferred and discovered via tool search.

description: String

Optional description of the custom tool, used to provide more context.

format\_: [CustomToolInputFormat](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

A grammar defined by the user.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

class NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: String

A description of the namespace shown to the model.

minLength1

name: String

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array[Function{ name, type, defer\_loading, 3 more} | [CustomTool](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } ]

The function/custom tools available inside this namespace.

One of the following:

class Function { name, type, defer\_loading, 3 more }

name: String

maxLength128

minLength1

type: :function

defer\_loading: bool

Whether this function should be deferred and discovered via tool search.

description: String

parameters: untyped

strict: bool

class CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

The name of the custom tool, used to identify it in tool calls.

type: :custom

The type of the custom tool. Always `custom`.

defer\_loading: bool

Whether this tool should be deferred and discovered via tool search.

description: String

Optional description of the custom tool, used to provide more context.

format\_: [CustomToolInputFormat](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

A grammar defined by the user.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

type: :namespace

The type of the tool. Always `namespace`.

class ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: :tool\_search

The type of the tool. Always `tool_search`.

description: String

Description shown to the model for a client-executed tool search tool.

execution: :server | :client

Whether tool search is executed by the server or by the client.

One of the following:

:server

:client

parameters: untyped

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search\_preview | :web\_search\_preview\_2025\_03\_11

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

:web\_search\_preview

:web\_search\_preview\_2025\_03\_11

search\_content\_types: Array[:text | :image]

One of the following:

:text

:image

search\_context\_size: :low | :medium | :high

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

:low

:medium

:high

user\_location: UserLocation{ type, city, country, 2 more}

The user’s location.

type: :approximate

The type of location approximation. Always `approximate`.

city: String

Free text input for the city of the user, e.g. `San Francisco`.

country: String

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: String

Free text input for the region of the user, e.g. `California`.

timezone: String

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: :apply\_patch

The type of the tool. Always `apply_patch`.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

name: String

The name of the run.

##### ReturnsExpand Collapse

class RunCreateResponse { id, created\_at, data\_source, 11 more }

A schema representing an evaluation run.

id: String

Unique identifier for the evaluation run.

created\_at: Integer

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

data\_source: [CreateEvalJSONLRunDataSource](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_jsonl_run_data_source%20%3E%20(schema)) { source, type }  | [CreateEvalCompletionsRunDataSource](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20create_eval_completions_run_data_source%20%3E%20(schema)) { source, type, input\_messages, 2 more }  | Responses{ source, type, input\_messages, 2 more}

Information about the run’s data source.

One of the following:

class CreateEvalJSONLRunDataSource { source, type }

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

source: FileContent{ content, type} | FileID{ id, type}

Determines what populates the `item` namespace in the data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

type: :jsonl

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource { source, type, input\_messages, 2 more }

A CompletionsRunDataSource object describing a model sampling configuration.

source: FileContent{ content, type} | FileID{ id, type} | StoredCompletions{ type, created\_after, created\_before, 3 more}

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

class StoredCompletions { type, created\_after, created\_before, 3 more }

A StoredCompletionsRunDataSource configuration describing a set of filters

type: :stored\_completions

The type of source. Always `stored_completions`.

created\_after: Integer

An optional Unix timestamp to filter items created after this time.

created\_before: Integer

An optional Unix timestamp to filter items created before this time.

limit: Integer

An optional maximum number of items to return.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String

An optional model to filter by (e.g., ‘gpt-4o’).

type: :completions

The type of run data source. Always `completions`.

input\_messages: Template{ template, type} | ItemReference{ item\_reference, type}

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template { template, type }

template: Array[[EasyInputMessage](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20easy_input_message%20%3E%20(schema)) { content, role, phase, type }  | EvalItem{ content, role, type}]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputMessageContentList](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

String = String

A text input to the model.

ResponseInputMessageContentList = Array[[ResponseInputContent](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))]

A list of one or many input items to the model, containing different content
types.

One of the following:

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class ResponseInputImage { detail, type, file\_id, image\_url }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: :low | :high | :auto | :original

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

:low

:high

:auto

:original

type: :input\_image

The type of the input item. Always `input_image`.

file\_id: String

The ID of the file to be sent to the model.

image\_url: String

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile { type, detail, file\_data, 3 more }

A file input to the model.

type: :input\_file

The type of the input item. Always `input_file`.

detail: :low | :high

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

:low

:high

file\_data: String

The content of the file to be sent to the model.

file\_id: String

The ID of the file to be sent to the model.

file\_url: String

The URL of the file to be sent to the model.

formaturi

filename: String

The name of the file to be sent to the model.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

phase: :commentary | :final\_answer

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

:commentary

:final\_answer

type: :message

The type of the message input. Always `message`.

class EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputText](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText{ text, type} | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

GraderInputs = Array[[GraderInputItem](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))]

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

type: :message

The type of the message input. Always `message`.

type: :template

The type of input messages. Always `template`.

class ItemReference { item\_reference, type }

item\_reference: String

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

type: :item\_reference

The type of input messages. Always `item_reference`.

model: String

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: SamplingParams{ max\_completion\_tokens, reasoning\_effort, response\_format, 4 more}

max\_completion\_tokens: Integer

The maximum number of tokens in the generated output.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

response\_format: [ResponseFormatText](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_text%20%3E%20(schema)) { type }  | [ResponseFormatJSONSchema](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_schema%20%3E%20(schema)) { json\_schema, type }  | [ResponseFormatJSONObject](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20response_format_json_object%20%3E%20(schema)) { type }

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatJSONSchema { json\_schema, type }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema{ name, description, schema, strict}

Structured Outputs configuration options, including a JSON Schema.

name: String

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: String

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Hash[Symbol, untyped]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: bool

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: :json\_schema

The type of response format being defined. Always `json_schema`.

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

tools: Array[[ChatCompletionFunctionTool](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type } ]

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

function: [FunctionDefinition](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

name: String

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: String

A description of what the function does, used by the model to choose when and how to call the function.

parameters: [FunctionParameters](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: bool

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: :function

The type of the tool. Currently, only `function` is supported.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class Responses { source, type, input\_messages, 2 more }

A ResponsesRunDataSource object describing a model sampling configuration.

source: FileContent{ content, type} | FileID{ id, type} | Responses{ type, created\_after, created\_before, 8 more}

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent { content, type }

content: Array[Content{ item, sample}]

The content of the jsonl file.

item: Hash[Symbol, untyped]

sample: Hash[Symbol, untyped]

type: :file\_content

The type of jsonl source. Always `file_content`.

class FileID { id, type }

id: String

The identifier of the file.

type: :file\_id

The type of jsonl source. Always `file_id`.

class Responses { type, created\_after, created\_before, 8 more }

A EvalResponsesSource object describing a run data source configuration.

type: :responses

The type of run data source. Always `responses`.

created\_after: Integer

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

created\_before: Integer

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

instructions\_search: String

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

metadata: untyped

Metadata filter for the responses. This is a query parameter used to select responses.

model: String

The name of the model to find responses for. This is a query parameter used to select responses.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

temperature: Float

Sampling temperature. This is a query parameter used to select responses.

tools: Array[String]

List of tool names. This is a query parameter used to select responses.

top\_p: Float

Nucleus sampling parameter. This is a query parameter used to select responses.

users: Array[String]

List of user identifiers. This is a query parameter used to select responses.

type: :responses

The type of run data source. Always `responses`.

input\_messages: Template{ template, type} | ItemReference{ item\_reference, type}

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template { template, type }

template: Array[ChatMessage{ content, role} | EvalItem{ content, role, type}]

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class ChatMessage { content, role }

content: String

The content of the message.

role: String

The role of the message (e.g. “system”, “assistant”, “user”).

class EvalItem { content, role, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: String | [ResponseInputText](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_text%20%3E%20(schema)) { text, type }  | OutputText{ text, type} | 3 more

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

GraderInputs = Array[[GraderInputItem](/api/reference/ruby/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))]

A list of inputs, each of which may be either an input text, output text, input
image, or input audio object.

One of the following:

String = String

A text input to the model.

class ResponseInputText { text, type }

A text input to the model.

text: String

The text input to the model.

type: :input\_text

The type of the input item. Always `input_text`.

class OutputText { text, type }

A text output from the model.

text: String

The text output from the model.

type: :output\_text

The type of the output text. Always `output_text`.

class InputImage { image\_url, type, detail }

An image input block used within EvalItem content arrays.

image\_url: String

The URL of the image input.

formaturi

type: :input\_image

The type of the image input. Always `input_image`.

detail: String

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio { input\_audio, type }

An audio input to the model.

input\_audio: InputAudio{ data, format\_}

data: String

Base64-encoded audio data.

format\_: :mp3 | :wav

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

:mp3

:wav

type: :input\_audio

The type of the input item. Always `input_audio`.

role: :user | :assistant | :system | :developer

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

:user

:assistant

:system

:developer

type: :message

The type of the message input. Always `message`.

type: :template

The type of input messages. Always `template`.

class ItemReference { item\_reference, type }

item\_reference: String

A reference to a variable in the `item` namespace. Ie, “item.name”

type: :item\_reference

The type of input messages. Always `item_reference`.

model: String

The name of the model to use for generating completions (e.g. “o3-mini”).

sampling\_params: SamplingParams{ max\_completion\_tokens, reasoning\_effort, seed, 4 more}

max\_completion\_tokens: Integer

The maximum number of tokens in the generated output.

reasoning\_effort: [ReasoningEffort](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

One of the following:

:none

:minimal

:low

:medium

:high

:xhigh

seed: Integer

A seed value to initialize the randomness, during sampling.

temperature: Float

A higher temperature increases randomness in the outputs.

text: Text{ format\_}

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

format\_: [ResponseFormatTextConfig](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatTextJSONSchemaConfig { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

name: String

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: Hash[Symbol, untyped]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: :json\_schema

The type of response format being defined. Always `json_schema`.

description: String

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: bool

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

tools: Array[[Tool](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))]

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

class FunctionTool { name, parameters, strict, 3 more }

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

name: String

The name of the function to call.

parameters: Hash[Symbol, untyped]

A JSON schema object describing the parameters of the function.

strict: bool

Whether to enforce strict parameter validation. Default `true`.

type: :function

The type of the function tool. Always `function`.

defer\_loading: bool

Whether this function is deferred and loaded via tool search.

description: String

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool { type, vector\_store\_ids, filters, 2 more }

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

type: :file\_search

The type of the file search tool. Always `file_search`.

vector\_store\_ids: Array[String]

The IDs of the vector stores to search.

filters: [ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | [CompoundFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20compound_filter%20%3E%20(schema)) { filters, type }

A filter to apply.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

class CompoundFilter { filters, type }

Combine multiple filters using `and` or `or`.

filters: Array[[ComparisonFilter](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20comparison_filter%20%3E%20(schema)) { key, type, value }  | untyped]

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter { key, type, value }

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

key: String

The key to compare against the value.

type: :eq | :ne | :gt | 5 more

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

:eq

:ne

:gt

:gte

:lt

:lte

:in

:nin

value: String | Float | bool | Array[String | Float]

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String = String

Float = Float

UnionMember2 = bool

UnionMember3 = Array[String | Float]

One of the following:

String = String

Float = Float

UnionMember1 = untyped

type: :and | :or

Type of operation: `and` or `or`.

One of the following:

:and

:or

max\_num\_results: Integer

The maximum number of results to return. This number should be between 1 and 50 inclusive.

ranking\_options: RankingOptions{ hybrid\_search, ranker, score\_threshold}

Ranking options for search.

hybrid\_search: HybridSearch{ embedding\_weight, text\_weight}

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

embedding\_weight: Float

The weight of the embedding in the reciprocal ranking fusion.

text\_weight: Float

The weight of the text in the reciprocal ranking fusion.

ranker: :auto | :"default-2024-11-15"

The ranker to use for the file search.

One of the following:

:auto

:"default-2024-11-15"

score\_threshold: Float

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool { type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

type: :computer

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool { display\_height, display\_width, environment, type }

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

display\_height: Integer

The height of the computer display.

display\_width: Integer

The width of the computer display.

environment: :windows | :mac | :linux | 2 more

The type of computer environment to control.

One of the following:

:windows

:mac

:linux

:ubuntu

:browser

type: :computer\_use\_preview

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool { type, filters, search\_context\_size, user\_location }

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search | :web\_search\_2025\_08\_26

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

:web\_search

:web\_search\_2025\_08\_26

filters: Filters{ allowed\_domains}

Filters for the search.

allowed\_domains: Array[String]

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

search\_context\_size: :low | :medium | :high

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

:low

:medium

:high

user\_location: UserLocation{ city, country, region, 2 more}

The approximate location of the user.

city: String

Free text input for the city of the user, e.g. `San Francisco`.

country: String

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: String

Free text input for the region of the user, e.g. `California`.

timezone: String

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

type: :approximate

The type of location approximation. Always `approximate`.

class Mcp { server\_label, type, allowed\_tools, 8 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: String

A label for this MCP server, used to identify it in tool calls.

type: :mcp

The type of the MCP tool. Always `mcp`.

allowed\_tools: Array[String] | McpToolFilter{ read\_only, tool\_names}

List of allowed tool names or a filter object.

One of the following:

McpAllowedTools = Array[String]

A string array of allowed tool names

class McpToolFilter { read\_only, tool\_names }

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

authorization: String

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

connector\_id: :connector\_dropbox | :connector\_gmail | :connector\_googlecalendar | 5 more

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

:connector\_dropbox

:connector\_gmail

:connector\_googlecalendar

:connector\_googledrive

:connector\_microsoftteams

:connector\_outlookcalendar

:connector\_outlookemail

:connector\_sharepoint

defer\_loading: bool

Whether this MCP tool is deferred and discovered via tool search.

headers: Hash[Symbol, String]

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

require\_approval: McpToolApprovalFilter{ always, never} | :always | :never

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter { always, never }

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

always: Always{ read\_only, tool\_names}

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

never: Never{ read\_only, tool\_names}

A filter object to specify which tools are allowed.

read\_only: bool

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

tool\_names: Array[String]

List of allowed tool names.

McpToolApprovalSetting = :always | :never

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

One of the following:

:always

:never

server\_description: String

Optional description of the MCP server, used to provide more context.

server\_url: String

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

tunnel\_id: String

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

class CodeInterpreter { container, type }

A tool that runs Python code to help generate a response to a prompt.

container: String | CodeInterpreterToolAuto{ type, file\_ids, memory\_limit, network\_policy}

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String = String

The container ID.

class CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

type: :auto

Always `auto`.

file\_ids: Array[String]

An optional list of uploaded files to make available to your code.

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit for the code interpreter container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [ContainerNetworkPolicyDisabled](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled { type }

type: :disabled

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

A list of allowed domains when type is `allowlist`.

type: :allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Array[[ContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

Optional domain-scoped secrets for allowlisted domains.

domain: String

The domain associated with the secret.

minLength1

name: String

The name of the secret to inject for the domain.

minLength1

value: String

The secret value to inject for the domain.

maxLength10485760

minLength1

type: :code\_interpreter

The type of the code interpreter tool. Always `code_interpreter`.

class ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: :image\_generation

The type of the image generation tool. Always `image_generation`.

action: :generate | :edit | :auto

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

:generate

:edit

:auto

background: :transparent | :opaque | :auto

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

:transparent

:opaque

:auto

input\_fidelity: :high | :low

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

:high

:low

input\_image\_mask: InputImageMask{ file\_id, image\_url}

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

file\_id: String

File ID for the mask image.

image\_url: String

Base64-encoded mask image.

model: String | :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

String = String

Model = :"gpt-image-1" | :"gpt-image-1-mini" | :"gpt-image-2" | 3 more

The image generation model to use. Default: `gpt-image-1`.

One of the following:

:"gpt-image-1"

:"gpt-image-1-mini"

:"gpt-image-2"

:"gpt-image-2-2026-04-21"

:"gpt-image-1.5"

:"chatgpt-image-latest"

moderation: :auto | :low

Moderation level for the generated image. Default: `auto`.

One of the following:

:auto

:low

output\_compression: Integer

Compression level for the output image. Default: 100.

minimum0

maximum100

output\_format: :png | :webp | :jpeg

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

:png

:webp

:jpeg

partial\_images: Integer

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

quality: :low | :medium | :high | :auto

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

:low

:medium

:high

:auto

size: String | :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

String = String

Size = :"1024x1024" | :"1024x1536" | :"1536x1024" | :auto

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

:"1024x1024"

:"1024x1536"

:"1536x1024"

:auto

class LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: :local\_shell

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool { type, environment }

A tool that allows the model to execute shell commands.

type: :shell

The type of the shell tool. Always `shell`.

environment: [ContainerAuto](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [LocalEnvironment](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20local_environment%20%3E%20(schema)) { type, skills }  | [ContainerReference](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_reference%20%3E%20(schema)) { container\_id, type }

One of the following:

class ContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: :container\_auto

Automatically creates a container for this request

file\_ids: Array[String]

An optional list of uploaded files to make available to your code.

memory\_limit: :"1g" | :"4g" | :"16g" | :"64g"

The memory limit for the container.

One of the following:

:"1g"

:"4g"

:"16g"

:"64g"

network\_policy: [ContainerNetworkPolicyDisabled](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_disabled%20%3E%20(schema)) { type }  | [ContainerNetworkPolicyAllowlist](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled { type }

type: :disabled

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array[String]

A list of allowed domains when type is `allowlist`.

type: :allowlist

Allow outbound network access only to specified domains. Always `allowlist`.

domain\_secrets: Array[[ContainerNetworkPolicyDomainSecret](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } ]

Optional domain-scoped secrets for allowlisted domains.

domain: String

The domain associated with the secret.

minLength1

name: String

The name of the secret to inject for the domain.

minLength1

value: String

The secret value to inject for the domain.

maxLength10485760

minLength1

skills: Array[[SkillReference](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [InlineSkill](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill%20%3E%20(schema)) { description, name, source, type } ]

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference { skill\_id, type, version }

skill\_id: String

The ID of the referenced skill.

maxLength64

minLength1

type: :skill\_reference

References a skill created with the /v1/skills endpoint.

version: String

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill { description, name, source, type }

description: String

The description of the skill.

name: String

The name of the skill.

source: [InlineSkillSource](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

Inline skill payload

data: String

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: :"application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: :base64

The type of the inline skill source. Must be `base64`.

type: :inline

Defines an inline skill for this request.

class LocalEnvironment { type, skills }

type: :local

Use a local computer environment.

skills: Array[[LocalSkill](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema)) { description, name, path } ]

An optional list of skills.

description: String

The description of the skill.

name: String

The name of the skill.

path: String

The path to the directory containing the skill.

class ContainerReference { container\_id, type }

container\_id: String

The ID of the referenced container.

type: :container\_reference

References a container created with the /v1/containers endpoint

class CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

The name of the custom tool, used to identify it in tool calls.

type: :custom

The type of the custom tool. Always `custom`.

defer\_loading: bool

Whether this tool should be deferred and discovered via tool search.

description: String

Optional description of the custom tool, used to provide more context.

format\_: [CustomToolInputFormat](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

A grammar defined by the user.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

class NamespaceTool { description, name, tools, type }

Groups function/custom tools under a shared namespace.

description: String

A description of the namespace shown to the model.

minLength1

name: String

The namespace name used in tool calls (for example, `crm`).

minLength1

tools: Array[Function{ name, type, defer\_loading, 3 more} | [CustomTool](/api/reference/ruby/resources/responses#(resource)%20responses%20%3E%20(model)%20custom_tool%20%3E%20(schema)) { name, type, defer\_loading, 2 more } ]

The function/custom tools available inside this namespace.

One of the following:

class Function { name, type, defer\_loading, 3 more }

name: String

maxLength128

minLength1

type: :function

defer\_loading: bool

Whether this function should be deferred and discovered via tool search.

description: String

parameters: untyped

strict: bool

class CustomTool { name, type, defer\_loading, 2 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: String

The name of the custom tool, used to identify it in tool calls.

type: :custom

The type of the custom tool. Always `custom`.

defer\_loading: bool

Whether this tool should be deferred and discovered via tool search.

description: String

Optional description of the custom tool, used to provide more context.

format\_: [CustomToolInputFormat](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { definition, syntax, type }

A grammar defined by the user.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

type: :namespace

The type of the tool. Always `namespace`.

class ToolSearchTool { type, description, execution, parameters }

Hosted or BYOT tool search configuration for deferred tools.

type: :tool\_search

The type of the tool. Always `tool_search`.

description: String

Description shown to the model for a client-executed tool search tool.

execution: :server | :client

Whether tool search is executed by the server or by the client.

One of the following:

:server

:client

parameters: untyped

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: :web\_search\_preview | :web\_search\_preview\_2025\_03\_11

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

:web\_search\_preview

:web\_search\_preview\_2025\_03\_11

search\_content\_types: Array[:text | :image]

One of the following:

:text

:image

search\_context\_size: :low | :medium | :high

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

:low

:medium

:high

user\_location: UserLocation{ type, city, country, 2 more}

The user’s location.

type: :approximate

The type of location approximation. Always `approximate`.

city: String

Free text input for the city of the user, e.g. `San Francisco`.

country: String

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

region: String

Free text input for the region of the user, e.g. `California`.

timezone: String

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool { type }

Allows the assistant to create, delete, or update files using unified diffs.

type: :apply\_patch

The type of the tool. Always `apply_patch`.

top\_p: Float

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

error: [EvalAPIError](/api/reference/ruby/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) { code, message }

An object representing an error response from the Eval API.

code: String

The error code.

message: String

The error message.

eval\_id: String

The identifier of the associated evaluation.

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String

The model that is evaluated, if applicable.

name: String

The name of the evaluation run.

object: :"eval.run"

The type of the object. Always “eval.run”.

per\_model\_usage: Array[PerModelUsage{ cached\_tokens, completion\_tokens, invocation\_count, 3 more}]

Usage statistics for each model during the evaluation run.

cached\_tokens: Integer

The number of tokens retrieved from cache.

completion\_tokens: Integer

The number of completion tokens generated.

invocation\_count: Integer

The number of invocations.

model\_name: String

The name of the model.

prompt\_tokens: Integer

The number of prompt tokens used.

total\_tokens: Integer

The total number of tokens used.

per\_testing\_criteria\_results: Array[PerTestingCriteriaResult{ failed, passed, testing\_criteria}]

Results per testing criteria applied during the evaluation run.

failed: Integer

Number of tests failed for this criteria.

passed: Integer

Number of tests passed for this criteria.

testing\_criteria: String

A description of the testing criteria.

report\_url: String

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

result\_counts: ResultCounts{ errored, failed, passed, total}

Counters summarizing the outcomes of the evaluation run.

errored: Integer

Number of output items that resulted in an error.

failed: Integer

Number of output items that failed to pass the evaluation.

passed: Integer

Number of output items that passed the evaluation.

total: Integer

Total number of executed output items.

status: String

The status of the evaluation run.

### Create eval run

Ruby

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

require "openai"

openai = OpenAI::Client.new(api_key: "My API Key")

run = openai.evals.runs.create(
  "eval_id",
  data_source: {source: {content: [{item: {foo: "bar"}}], type: :file_content}, type: :jsonl}

puts(run)

  "object": "eval.run",
  "id": "evalrun_67e57965b480819094274e3a32235e4c",
  "eval_id": "eval_67e579652b548190aaa83ada4b125f47",
  "report_url": "https://platform.openai.com/evaluations/eval_67e579652b548190aaa83ada4b125f47&run_id=evalrun_67e57965b480819094274e3a32235e4c",
  "status": "queued",
  "model": "gpt-4o-mini",
  "name": "gpt-4o-mini",
  "created_at": 1743092069,
  "result_counts": {
    "total": 0,
    "errored": 0,
    "failed": 0,
    "passed": 0
  "per_model_usage": null,
  "per_testing_criteria_results": null,
  "data_source": {
    "type": "completions",
    "source": {
      "type": "file_content",
      "content": [
          "item": {
            "input": "Tech Company Launches Advanced Artificial Intelligence Platform",
            "ground_truth": "Technology"
      ]
    "input_messages": {
      "type": "template",
      "template": [
          "type": "message",
          "role": "developer",
          "content": {
            "type": "input_text",
            "text": "Categorize a given news headline into one of the following topics: Technology, Markets, World, Business, or Sports.\n\n# Steps\n\n1. Analyze the content of the news headline to understand its primary focus.\n2. Extract the subject matter, identifying any key indicators or keywords.\n3. Use the identified indicators to determine the most suitable category out of the five options: Technology, Markets, World, Business, or Sports.\n4. Ensure only one category is selected per headline.\n\n# Output Format\n\nRespond with the chosen category as a single word. For instance: \"Technology\", \"Markets\", \"World\", \"Business\", or \"Sports\".\n\n# Examples\n\n**Input**: \"Apple Unveils New iPhone Model, Featuring Advanced AI Features\"  \n**Output**: \"Technology\"\n\n**Input**: \"Global Stocks Mixed as Investors Await Central Bank Decisions\"  \n**Output**: \"Markets\"\n\n**Input**: \"War in Ukraine: Latest Updates on Negotiation Status\"  \n**Output**: \"World\"\n\n**Input**: \"Microsoft in Talks to Acquire Gaming Company for $2 Billion\"  \n**Output**: \"Business\"\n\n**Input**: \"Manchester United Secures Win in Premier League Football Match\"  \n**Output**: \"Sports\" \n\n# Notes\n\n- If the headline appears to fit into more than one category, choose the most dominant theme.\n- Keywords or phrases such as \"stocks\", \"company acquisition\", \"match\", or technological brands can be good indicators for classification.\n"
          "type": "message",
          "role": "user",
          "content": {
            "type": "input_text",
            "text": "{{item.input}}"
      ]
    "model": "gpt-4o-mini",
    "sampling_params": {
      "seed": 42,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_completions_tokens": 2048
  "error": null,
  "metadata": {}

##### Returns Examples

  "object": "eval.run",
  "id": "evalrun_67e57965b480819094274e3a32235e4c",
  "eval_id": "eval_67e579652b548190aaa83ada4b125f47",
  "report_url": "https://platform.openai.com/evaluations/eval_67e579652b548190aaa83ada4b125f47&run_id=evalrun_67e57965b480819094274e3a32235e4c",
  "status": "queued",
  "model": "gpt-4o-mini",
  "name": "gpt-4o-mini",
  "created_at": 1743092069,
  "result_counts": {
    "total": 0,
    "errored": 0,
    "failed": 0,
    "passed": 0
  "per_model_usage": null,
  "per_testing_criteria_results": null,
  "data_source": {
    "type": "completions",
    "source": {
      "type": "file_content",
      "content": [
          "item": {
            "input": "Tech Company Launches Advanced Artificial Intelligence Platform",
            "ground_truth": "Technology"
      ]
    "input_messages": {
      "type": "template",
      "template": [
          "type": "message",
          "role": "developer",
          "content": {
            "type": "input_text",
            "text": "Categorize a given news headline into one of the following topics: Technology, Markets, World, Business, or Sports.\n\n# Steps\n\n1. Analyze the content of the news headline to understand its primary focus.\n2. Extract the subject matter, identifying any key indicators or keywords.\n3. Use the identified indicators to determine the most suitable category out of the five options: Technology, Markets, World, Business, or Sports.\n4. Ensure only one category is selected per headline.\n\n# Output Format\n\nRespond with the chosen category as a single word. For instance: \"Technology\", \"Markets\", \"World\", \"Business\", or \"Sports\".\n\n# Examples\n\n**Input**: \"Apple Unveils New iPhone Model, Featuring Advanced AI Features\"  \n**Output**: \"Technology\"\n\n**Input**: \"Global Stocks Mixed as Investors Await Central Bank Decisions\"  \n**Output**: \"Markets\"\n\n**Input**: \"War in Ukraine: Latest Updates on Negotiation Status\"  \n**Output**: \"World\"\n\n**Input**: \"Microsoft in Talks to Acquire Gaming Company for $2 Billion\"  \n**Output**: \"Business\"\n\n**Input**: \"Manchester United Secures Win in Premier League Football Match\"  \n**Output**: \"Sports\" \n\n# Notes\n\n- If the headline appears to fit into more than one category, choose the most dominant theme.\n- Keywords or phrases such as \"stocks\", \"company acquisition\", \"match\", or technological brands can be good indicators for classification.\n"
          "type": "message",
          "role": "user",
          "content": {
            "type": "input_text",
            "text": "{{item.input}}"
      ]
    "model": "gpt-4o-mini",
    "sampling_params": {
      "seed": 42,
      "temperature": 1.0,
      "top_p": 1.0,
      "max_completions_tokens": 2048
  "error": null,
  "metadata": {}
