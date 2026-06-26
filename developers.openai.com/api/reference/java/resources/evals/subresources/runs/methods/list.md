<!-- source: https://developers.openai.com/api/reference/java/resources/evals/subresources/runs/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Evals](/api/reference/java/resources/evals)

[Runs](/api/reference/java/resources/evals/subresources/runs)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Get eval runs

RunListPage evals().runs().list(RunListParamsparams = RunListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/evals/{eval\_id}/runs

Get a list of runs for an evaluation.

##### ParametersExpand Collapse

RunListParams params

Optional<String> evalId

Optional<String> after

Identifier for the last run from the previous pagination request.

Optional<Long> limit

Number of runs to retrieve.

Optional<[Order](/api/reference/java/resources/evals/subresources/runs/methods/list#(resource)%20evals.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20order%20%3E%20(schema))> order

Sort order for runs by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

ASC("asc")

DESC("desc")

Optional<[Status](/api/reference/java/resources/evals/subresources/runs/methods/list#(resource)%20evals.runs%20%3E%20(method)%20list%20%3E%20(params)%20default%20%3E%20(param)%20status%20%3E%20(schema))> status

Filter runs by status. One of `queued` | `in_progress` | `failed` | `completed` | `canceled`.

QUEUED("queued")

IN\_PROGRESS("in\_progress")

COMPLETED("completed")

CANCELED("canceled")

FAILED("failed")

##### ReturnsExpand Collapse

class RunListResponse:

A schema representing an evaluation run.

String id

Unique identifier for the evaluation run.

long createdAt

Unix timestamp (in seconds) when the evaluation run was created.

formatunixtime

DataSource dataSource

Information about the run’s data source.

One of the following:

class CreateEvalJsonlRunDataSource:

A JsonlRunDataSource object with that specifies a JSONL file that matches the eval

Source source

Determines what populates the `item` namespace in the data source.

One of the following:

class FileContent:

List<Content> content

The content of the jsonl file.

Item item

Optional<Sample> sample

JsonValue; type "file\_content"constant"file\_content"constant

The type of jsonl source. Always `file_content`.

class FileId:

String id

The identifier of the file.

JsonValue; type "file\_id"constant"file\_id"constant

The type of jsonl source. Always `file_id`.

JsonValue; type "jsonl"constant"jsonl"constant

The type of data source. Always `jsonl`.

class CreateEvalCompletionsRunDataSource:

A CompletionsRunDataSource object describing a model sampling configuration.

Source source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent:

List<Content> content

The content of the jsonl file.

Item item

Optional<Sample> sample

JsonValue; type "file\_content"constant"file\_content"constant

The type of jsonl source. Always `file_content`.

class FileId:

String id

The identifier of the file.

JsonValue; type "file\_id"constant"file\_id"constant

The type of jsonl source. Always `file_id`.

class StoredCompletions:

A StoredCompletionsRunDataSource configuration describing a set of filters

JsonValue; type "stored\_completions"constant"stored\_completions"constant

The type of source. Always `stored_completions`.

Optional<Long> createdAfter

An optional Unix timestamp to filter items created after this time.

Optional<Long> createdBefore

An optional Unix timestamp to filter items created before this time.

Optional<Long> limit

An optional maximum number of items to return.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<String> model

An optional model to filter by (e.g., ‘gpt-4o’).

Type type

The type of run data source. Always `completions`.

Optional<InputMessages> inputMessages

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template:

List<InnerTemplate> template

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class EasyInputMessage:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

One of the following:

String

List<[ResponseInputContent](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20response_input_content%20%3E%20(schema))>

One of the following:

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class ResponseInputImage:

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

Detail detail

The detail level of the image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

One of the following:

LOW("low")

HIGH("high")

AUTO("auto")

ORIGINAL("original")

JsonValue; type "input\_image"constant"input\_image"constant

The type of the input item. Always `input_image`.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> imageUrl

The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

formaturi

class ResponseInputFile:

A file input to the model.

JsonValue; type "input\_file"constant"input\_file"constant

The type of the input item. Always `input_file`.

Optional<Detail> detail

The detail level of the file to be sent to the model. Use `low` for the default rendering behavior, or `high` to render the file at higher quality. Defaults to `low`.

One of the following:

LOW("low")

HIGH("high")

Optional<String> fileData

The content of the file to be sent to the model.

Optional<String> fileId

The ID of the file to be sent to the model.

Optional<String> fileUrl

The URL of the file to be sent to the model.

formaturi

Optional<String> filename

The name of the file to be sent to the model.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Phase> phase

Labels an `assistant` message as intermediate commentary (`commentary`) or the final answer (`final_answer`).
For models like `gpt-5.3-codex` and beyond, when sending follow-up requests, preserve and resend
phase on all assistant messages — dropping it can degrade performance. Not used for user messages.

One of the following:

COMMENTARY("commentary")

FINAL\_ANSWER("final\_answer")

Optional<Type> type

The type of the message input. Always `message`.

class EvalItem:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class OutputText:

A text output from the model.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

class InputImage:

An image input block used within EvalItem content arrays.

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

List<[EvalContentItem](/api/reference/java/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))>

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

OutputText

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

InputImage

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Type> type

The type of the message input. Always `message`.

JsonValue; type "template"constant"template"constant

The type of input messages. Always `template`.

class ItemReference:

String itemReference

A reference to a variable in the `item` namespace. Ie, “item.input\_trajectory”

JsonValue; type "item\_reference"constant"item\_reference"constant

The type of input messages. Always `item_reference`.

Optional<String> model

The name of the model to use for generating completions (e.g. “o3-mini”).

Optional<SamplingParams> samplingParams

Optional<Long> maxCompletionTokens

The maximum number of tokens in the generated output.

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> reasoningEffort

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

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

Optional<ResponseFormat> responseFormat

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText:

Default response format. Used to generate text responses.

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

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

class ResponseFormatJsonObject:

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

Optional<Long> seed

A seed value to initialize the randomness, during sampling.

Optional<Double> temperature

A higher temperature increases randomness in the outputs.

Optional<List<[ChatCompletionFunctionTool](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema))>> tools

A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

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

The type of the tool. Currently, only `function` is supported.

Optional<Double> topP

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

class Responses:

A ResponsesRunDataSource object describing a model sampling configuration.

Source source

Determines what populates the `item` namespace in this run’s data source.

One of the following:

class FileContent:

List<Content> content

The content of the jsonl file.

Item item

Optional<Sample> sample

JsonValue; type "file\_content"constant"file\_content"constant

The type of jsonl source. Always `file_content`.

class FileId:

String id

The identifier of the file.

JsonValue; type "file\_id"constant"file\_id"constant

The type of jsonl source. Always `file_id`.

class InnerResponses:

A EvalResponsesSource object describing a run data source configuration.

JsonValue; type "responses"constant"responses"constant

The type of run data source. Always `responses`.

Optional<Long> createdAfter

Only include items created after this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

Optional<Long> createdBefore

Only include items created before this timestamp (inclusive). This is a query parameter used to select responses.

minimum0

Optional<String> instructionsSearch

Optional string to search the ‘instructions’ field. This is a query parameter used to select responses.

Optional<JsonValue> metadata

Metadata filter for the responses. This is a query parameter used to select responses.

Optional<String> model

The name of the model to find responses for. This is a query parameter used to select responses.

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> reasoningEffort

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

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

Optional<Double> temperature

Sampling temperature. This is a query parameter used to select responses.

Optional<List<String>> tools

List of tool names. This is a query parameter used to select responses.

Optional<Double> topP

Nucleus sampling parameter. This is a query parameter used to select responses.

Optional<List<String>> users

List of user identifiers. This is a query parameter used to select responses.

JsonValue; type "responses"constant"responses"constant

The type of run data source. Always `responses`.

Optional<InputMessages> inputMessages

Used when sampling from a model. Dictates the structure of the messages passed into the model. Can either be a reference to a prebuilt trajectory (ie, `item.input_trajectory`), or a template with variable references to the `item` namespace.

One of the following:

class Template:

List<InnerTemplate> template

A list of chat messages forming the prompt or context. May include variable references to the `item` namespace, ie {{item.name}}.

One of the following:

class ChatMessage:

String content

The content of the message.

String role

The role of the message (e.g. “system”, “assistant”, “user”).

class EvalItem:

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

Content content

Inputs to the model - can contain template strings. Supports text, output text, input images, and input audio, either as a single item or an array of items.

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

class OutputText:

A text output from the model.

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

class InputImage:

An image input block used within EvalItem content arrays.

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

List<[EvalContentItem](/api/reference/java/resources/graders#(resource)%20graders.grader_models%20%3E%20(model)%20eval_content_item%20%3E%20(schema))>

One of the following:

String

class ResponseInputText:

A text input to the model.

String text

The text input to the model.

JsonValue; type "input\_text"constant"input\_text"constant

The type of the input item. Always `input_text`.

OutputText

String text

The text output from the model.

JsonValue; type "output\_text"constant"output\_text"constant

The type of the output text. Always `output_text`.

InputImage

String imageUrl

The URL of the image input.

formaturi

JsonValue; type "input\_image"constant"input\_image"constant

The type of the image input. Always `input_image`.

Optional<String> detail

The detail level of the image to be sent to the model. One of `high`, `low`, or `auto`. Defaults to `auto`.

class ResponseInputAudio:

An audio input to the model.

InputAudio inputAudio

String data

Base64-encoded audio data.

Format format

The format of the audio data. Currently supported formats are `mp3` and
`wav`.

One of the following:

MP3("mp3")

WAV("wav")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the input item. Always `input_audio`.

Role role

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

One of the following:

USER("user")

ASSISTANT("assistant")

SYSTEM("system")

DEVELOPER("developer")

Optional<Type> type

The type of the message input. Always `message`.

JsonValue; type "template"constant"template"constant

The type of input messages. Always `template`.

class ItemReference:

String itemReference

A reference to a variable in the `item` namespace. Ie, “item.name”

JsonValue; type "item\_reference"constant"item\_reference"constant

The type of input messages. Always `item_reference`.

Optional<String> model

The name of the model to use for generating completions (e.g. “o3-mini”).

Optional<SamplingParams> samplingParams

Optional<Long> maxCompletionTokens

The maximum number of tokens in the generated output.

Optional<[ReasoningEffort](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))> reasoningEffort

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

NONE("none")

MINIMAL("minimal")

LOW("low")

MEDIUM("medium")

HIGH("high")

XHIGH("xhigh")

Optional<Long> seed

A seed value to initialize the randomness, during sampling.

Optional<Double> temperature

A higher temperature increases randomness in the outputs.

Optional<Text> text

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](https://platform.openai.com/docs/guides/text)
* [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)

Optional<[ResponseFormatTextConfig](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20response_format_text_config%20%3E%20(schema))> format

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

class ResponseFormatText:

Default response format. Used to generate text responses.

JsonValue; type "text"constant"text"constant

The type of response format being defined. Always `text`.

class ResponseFormatTextJsonSchemaConfig:

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

String name

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Schema schema

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

JsonValue; type "json\_schema"constant"json\_schema"constant

The type of response format being defined. Always `json_schema`.

Optional<String> description

A description of what the response format is for, used by the model to
determine how to respond in the format.

Optional<Boolean> strict

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

class ResponseFormatJsonObject:

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

JsonValue; type "json\_object"constant"json\_object"constant

The type of response format being defined. Always `json_object`.

Optional<List<[Tool](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20tool%20%3E%20(schema))>> tools

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

class FunctionTool:

Defines a function in your own code the model can choose to call. Learn more about [function calling](https://platform.openai.com/docs/guides/function-calling).

String name

The name of the function to call.

Optional<Parameters> parameters

A JSON schema object describing the parameters of the function.

Optional<Boolean> strict

Whether to enforce strict parameter validation. Default `true`.

JsonValue; type "function"constant"function"constant

The type of the function tool. Always `function`.

Optional<Boolean> deferLoading

Whether this function is deferred and loaded via tool search.

Optional<String> description

A description of the function. Used by the model to determine whether or not to call the function.

class FileSearchTool:

A tool that searches for relevant content from uploaded files. Learn more about the [file search tool](https://platform.openai.com/docs/guides/tools-file-search).

JsonValue; type "file\_search"constant"file\_search"constant

The type of the file search tool. Always `file_search`.

List<String> vectorStoreIds

The IDs of the vector stores to search.

Optional<Filters> filters

A filter to apply.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

class CompoundFilter:

Combine multiple filters using `and` or `or`.

List<Filter> filters

Array of filters to combine. Items can be `ComparisonFilter` or `CompoundFilter`.

One of the following:

class ComparisonFilter:

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

String key

The key to compare against the value.

Type type

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

EQ("eq")

NE("ne")

GT("gt")

GTE("gte")

LT("lt")

LTE("lte")

IN("in")

NIN("nin")

Value value

The value to compare against the attribute key; supports string, number, or boolean types.

One of the following:

String

double

boolean

List<ComparisonFilterValueItem>

One of the following:

String

double

JsonValue

Type type

Type of operation: `and` or `or`.

One of the following:

AND("and")

OR("or")

Optional<Long> maxNumResults

The maximum number of results to return. This number should be between 1 and 50 inclusive.

Optional<RankingOptions> rankingOptions

Ranking options for search.

Optional<HybridSearch> hybridSearch

Weights that control how reciprocal rank fusion balances semantic embedding matches versus sparse keyword matches when hybrid search is enabled.

double embeddingWeight

The weight of the embedding in the reciprocal ranking fusion.

double textWeight

The weight of the text in the reciprocal ranking fusion.

Optional<Ranker> ranker

The ranker to use for the file search.

One of the following:

AUTO("auto")

DEFAULT\_2024\_11\_15("default-2024-11-15")

Optional<Double> scoreThreshold

The score threshold for the file search, a number between 0 and 1. Numbers closer to 1 will attempt to return only the most relevant results, but may return fewer results.

class ComputerTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

JsonValue; type "computer"constant"computer"constant

The type of the computer tool. Always `computer`.

class ComputerUsePreviewTool:

A tool that controls a virtual computer. Learn more about the [computer tool](https://platform.openai.com/docs/guides/tools-computer-use).

long displayHeight

The height of the computer display.

long displayWidth

The width of the computer display.

Environment environment

The type of computer environment to control.

One of the following:

WINDOWS("windows")

MAC("mac")

LINUX("linux")

UBUNTU("ubuntu")

BROWSER("browser")

JsonValue; type "computer\_use\_preview"constant"computer\_use\_preview"constant

The type of the computer use tool. Always `computer_use_preview`.

class WebSearchTool:

Search the Internet for sources related to the prompt. Learn more about the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search` or `web_search_2025_08_26`.

One of the following:

WEB\_SEARCH("web\_search")

WEB\_SEARCH\_2025\_08\_26("web\_search\_2025\_08\_26")

Optional<Filters> filters

Filters for the search.

Optional<List<String>> allowedDomains

Allowed domains for the search. If not provided, all domains are allowed.
Subdomains of the provided domains are allowed as well.

Example: `["pubmed.ncbi.nlm.nih.gov"]`

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The approximate location of the user.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

Optional<Type> type

The type of location approximation. Always `approximate`.

Mcp

String serverLabel

A label for this MCP server, used to identify it in tool calls.

JsonValue; type "mcp"constant"mcp"constant

The type of the MCP tool. Always `mcp`.

Optional<AllowedTools> allowedTools

List of allowed tool names or a filter object.

One of the following:

List<String>

class McpToolFilter:

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<String> authorization

An OAuth access token that can be used with a remote MCP server, either
with a custom MCP server URL or a service connector. Your application
must handle the OAuth authorization flow and provide the token here.

Optional<ConnectorId> connectorId

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

CONNECTOR\_DROPBOX("connector\_dropbox")

CONNECTOR\_GMAIL("connector\_gmail")

CONNECTOR\_GOOGLECALENDAR("connector\_googlecalendar")

CONNECTOR\_GOOGLEDRIVE("connector\_googledrive")

CONNECTOR\_MICROSOFTTEAMS("connector\_microsoftteams")

CONNECTOR\_OUTLOOKCALENDAR("connector\_outlookcalendar")

CONNECTOR\_OUTLOOKEMAIL("connector\_outlookemail")

CONNECTOR\_SHAREPOINT("connector\_sharepoint")

Optional<Boolean> deferLoading

Whether this MCP tool is deferred and discovered via tool search.

Optional<Headers> headers

Optional HTTP headers to send to the MCP server. Use for authentication
or other purposes.

Optional<RequireApproval> requireApproval

Specify which of the MCP server’s tools require approval.

One of the following:

class McpToolApprovalFilter:

Specify which of the MCP server’s tools require approval. Can be
`always`, `never`, or a filter object associated with tools
that require approval.

Optional<Always> always

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

Optional<Never> never

A filter object to specify which tools are allowed.

Optional<Boolean> readOnly

Indicates whether or not a tool modifies data or is read-only. If an
MCP server is [annotated with `readOnlyHint`](https://modelcontextprotocol.io/specification/2025-06-18/schema#toolannotations-readonlyhint),
it will match this filter.

Optional<List<String>> toolNames

List of allowed tool names.

enum McpToolApprovalSetting:

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

ALWAYS("always")

NEVER("never")

Optional<String> serverDescription

Optional description of the MCP server, used to provide more context.

Optional<String> serverUrl

The URL for the MCP server. One of `server_url`, `connector_id`, or
`tunnel_id` must be provided.

formaturi

Optional<String> tunnelId

The Secure MCP Tunnel ID to use instead of a direct server URL. One of
`server_url`, `connector_id`, or `tunnel_id` must be provided.

CodeInterpreter

Container container

The code interpreter container. Can be a container ID or an object that
specifies uploaded file IDs to make available to your code, along with an
optional `memory_limit` setting.

One of the following:

String

class CodeInterpreterToolAuto:

Configuration for a code interpreter container. Optionally specify the IDs of the files to run the code on.

JsonValue; type "auto"constant"auto"constant

Always `auto`.

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the code interpreter container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

JsonValue; type "code\_interpreter"constant"code\_interpreter"constant

The type of the code interpreter tool. Always `code_interpreter`.

ImageGeneration

JsonValue; type "image\_generation"constant"image\_generation"constant

The type of the image generation tool. Always `image_generation`.

Optional<Action> action

Whether to generate a new image or edit an existing image. Default: `auto`.

One of the following:

GENERATE("generate")

EDIT("edit")

AUTO("auto")

Optional<Background> background

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

TRANSPARENT("transparent")

OPAQUE("opaque")

AUTO("auto")

Optional<InputFidelity> inputFidelity

Control how much effort the model will exert to match the style and features, especially facial features, of input images. This parameter is only supported for `gpt-image-1` and `gpt-image-1.5` and later models, unsupported for `gpt-image-1-mini`. Supports `high` and `low`. Defaults to `low`.

One of the following:

HIGH("high")

LOW("low")

Optional<InputImageMask> inputImageMask

Optional mask for inpainting. Contains `image_url`
(string, optional) and `file_id` (string, optional).

Optional<String> fileId

File ID for the mask image.

Optional<String> imageUrl

Base64-encoded mask image.

Optional<Model> model

The image generation model to use. Default: `gpt-image-1`.

One of the following:

GPT\_IMAGE\_1("gpt-image-1")

GPT\_IMAGE\_1\_MINI("gpt-image-1-mini")

GPT\_IMAGE\_2("gpt-image-2")

GPT\_IMAGE\_2\_2026\_04\_21("gpt-image-2-2026-04-21")

GPT\_IMAGE\_1\_5("gpt-image-1.5")

CHATGPT\_IMAGE\_LATEST("chatgpt-image-latest")

Optional<Moderation> moderation

Moderation level for the generated image. Default: `auto`.

One of the following:

AUTO("auto")

LOW("low")

Optional<Long> outputCompression

Compression level for the output image. Default: 100.

minimum0

maximum100

Optional<OutputFormat> outputFormat

The output format of the generated image. One of `png`, `webp`, or
`jpeg`. Default: `png`.

One of the following:

PNG("png")

WEBP("webp")

JPEG("jpeg")

Optional<Long> partialImages

Number of partial images to generate in streaming mode, from 0 (default value) to 3.

minimum0

maximum3

Optional<Quality> quality

The quality of the generated image. One of `low`, `medium`, `high`,
or `auto`. Default: `auto`.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

AUTO("auto")

Optional<Size> size

The size of the generated images. For `gpt-image-2` and `gpt-image-2-2026-04-21`, arbitrary resolutions are supported as `WIDTHxHEIGHT` strings, for example `1536x864`. Width and height must both be divisible by 16 and the requested aspect ratio must be between 1:3 and 3:1. Resolutions above `2560x1440` are experimental, and the maximum supported resolution is `3840x2160`. The requested size must also satisfy the model’s current pixel and edge limits. The standard sizes `1024x1024`, `1536x1024`, and `1024x1536` are supported by the GPT image models; `auto` is supported for models that allow automatic sizing. For `dall-e-2`, use one of `256x256`, `512x512`, or `1024x1024`. For `dall-e-3`, use one of `1024x1024`, `1792x1024`, or `1024x1792`.

One of the following:

\_1024X1024("1024x1024")

\_1024X1536("1024x1536")

\_1536X1024("1536x1024")

AUTO("auto")

JsonValue;

JsonValue; type "local\_shell"constant"local\_shell"constant

The type of the local shell tool. Always `local_shell`.

class FunctionShellTool:

A tool that allows the model to execute shell commands.

JsonValue; type "shell"constant"shell"constant

The type of the shell tool. Always `shell`.

Optional<Environment> environment

One of the following:

class ContainerAuto:

JsonValue; type "container\_auto"constant"container\_auto"constant

Automatically creates a container for this request

Optional<List<String>> fileIds

An optional list of uploaded files to make available to your code.

Optional<MemoryLimit> memoryLimit

The memory limit for the container.

One of the following:

\_1G("1g")

\_4G("4g")

\_16G("16g")

\_64G("64g")

Optional<NetworkPolicy> networkPolicy

Network access policy for the container.

One of the following:

class ContainerNetworkPolicyDisabled:

JsonValue; type "disabled"constant"disabled"constant

Disable outbound network access. Always `disabled`.

class ContainerNetworkPolicyAllowlist:

List<String> allowedDomains

A list of allowed domains when type is `allowlist`.

JsonValue; type "allowlist"constant"allowlist"constant

Allow outbound network access only to specified domains. Always `allowlist`.

Optional<List<[ContainerNetworkPolicyDomainSecret](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20container_network_policy_domain_secret%20%3E%20(schema))>> domainSecrets

Optional domain-scoped secrets for allowlisted domains.

String domain

The domain associated with the secret.

minLength1

String name

The name of the secret to inject for the domain.

minLength1

String value

The secret value to inject for the domain.

maxLength10485760

minLength1

Optional<List<Skill>> skills

An optional list of skills referenced by id or inline data.

One of the following:

class SkillReference:

String skillId

The ID of the referenced skill.

maxLength64

minLength1

JsonValue; type "skill\_reference"constant"skill\_reference"constant

References a skill created with the /v1/skills endpoint.

Optional<String> version

Optional skill version. Use a positive integer or ‘latest’. Omit for default.

class InlineSkill:

String description

The description of the skill.

String name

The name of the skill.

[InlineSkillSource](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20inline_skill_source%20%3E%20(schema)) source

Inline skill payload

String data

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

JsonValue; mediaType "application/zip"constant"application/zip"constant

The media type of the inline skill payload. Must be `application/zip`.

JsonValue; type "base64"constant"base64"constant

The type of the inline skill source. Must be `base64`.

JsonValue; type "inline"constant"inline"constant

Defines an inline skill for this request.

class LocalEnvironment:

JsonValue; type "local"constant"local"constant

Use a local computer environment.

Optional<List<[LocalSkill](/api/reference/java/resources/responses#(resource)%20responses%20%3E%20(model)%20local_skill%20%3E%20(schema))>> skills

An optional list of skills.

String description

The description of the skill.

String name

The name of the skill.

String path

The path to the directory containing the skill.

class ContainerReference:

String containerId

The ID of the referenced container.

JsonValue; type "container\_reference"constant"container\_reference"constant

References a container created with the /v1/containers endpoint

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

One of the following:

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

Grammar

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

class NamespaceTool:

Groups function/custom tools under a shared namespace.

String description

A description of the namespace shown to the model.

minLength1

String name

The namespace name used in tool calls (for example, `crm`).

minLength1

List<Tool> tools

The function/custom tools available inside this namespace.

One of the following:

class Function:

String name

maxLength128

minLength1

JsonValue; type "function"constant"function"constant

Optional<Boolean> deferLoading

Whether this function should be deferred and discovered via tool search.

Optional<String> description

Optional<JsonValue> parameters

Optional<Boolean> strict

class CustomTool:

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

String name

The name of the custom tool, used to identify it in tool calls.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

Optional<Boolean> deferLoading

Whether this tool should be deferred and discovered via tool search.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<[CustomToolInputFormat](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20custom_tool_input_format%20%3E%20(schema))> format

The input format for the custom tool. Default is unconstrained text.

One of the following:

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

Grammar

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "namespace"constant"namespace"constant

The type of the tool. Always `namespace`.

class ToolSearchTool:

Hosted or BYOT tool search configuration for deferred tools.

JsonValue; type "tool\_search"constant"tool\_search"constant

The type of the tool. Always `tool_search`.

Optional<String> description

Description shown to the model for a client-executed tool search tool.

Optional<Execution> execution

Whether tool search is executed by the server or by the client.

One of the following:

SERVER("server")

CLIENT("client")

Optional<JsonValue> parameters

Parameter schema for a client-executed tool search tool.

class WebSearchPreviewTool:

This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search).

Type type

The type of the web search tool. One of `web_search_preview` or `web_search_preview_2025_03_11`.

One of the following:

WEB\_SEARCH\_PREVIEW("web\_search\_preview")

WEB\_SEARCH\_PREVIEW\_2025\_03\_11("web\_search\_preview\_2025\_03\_11")

Optional<List<SearchContentType>> searchContentTypes

One of the following:

TEXT("text")

IMAGE("image")

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

The user’s location.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user, e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones) of the user, e.g. `America/Los_Angeles`.

class ApplyPatchTool:

Allows the assistant to create, delete, or update files using unified diffs.

JsonValue; type "apply\_patch"constant"apply\_patch"constant

The type of the tool. Always `apply_patch`.

Optional<Double> topP

An alternative to temperature for nucleus sampling; 1.0 includes all tokens.

[EvalApiError](/api/reference/java/resources/evals#(resource)%20evals.runs%20%3E%20(model)%20eval_api_error%20%3E%20(schema)) error

An object representing an error response from the Eval API.

String code

The error code.

String message

The error message.

String evalId

The identifier of the associated evaluation.

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

String model

The model that is evaluated, if applicable.

String name

The name of the evaluation run.

JsonValue; object\_ "eval.run"constant"eval.run"constant

The type of the object. Always “eval.run”.

List<PerModelUsage> perModelUsage

Usage statistics for each model during the evaluation run.

long cachedTokens

The number of tokens retrieved from cache.

long completionTokens

The number of completion tokens generated.

long invocationCount

The number of invocations.

String modelName

The name of the model.

long promptTokens

The number of prompt tokens used.

long totalTokens

The total number of tokens used.

List<PerTestingCriteriaResult> perTestingCriteriaResults

Results per testing criteria applied during the evaluation run.

long failed

Number of tests failed for this criteria.

long passed

Number of tests passed for this criteria.

String testingCriteria

A description of the testing criteria.

String reportUrl

The URL to the rendered evaluation run report on the UI dashboard.

formaturi

ResultCounts resultCounts

Counters summarizing the outcomes of the evaluation run.

long errored

Number of output items that resulted in an error.

long failed

Number of output items that failed to pass the evaluation.

long passed

Number of output items that passed the evaluation.

long total

Total number of executed output items.

String status

The status of the evaluation run.

### Get eval runs

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
import com.openai.models.evals.runs.RunListPage;
import com.openai.models.evals.runs.RunListParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        RunListPage page = client.evals().runs().list("eval_id");

  "object": "list",
  "data": [
      "object": "eval.run",
      "id": "evalrun_67e0c7d31560819090d60c0780591042",
      "eval_id": "eval_67e0c726d560819083f19a957c4c640b",
      "report_url": "https://platform.openai.com/evaluations/eval_67e0c726d560819083f19a957c4c640b",
      "status": "completed",
      "model": "o3-mini",
      "name": "bulk_with_negative_examples_o3-mini",
      "created_at": 1742784467,
      "result_counts": {
        "total": 1,
        "errored": 0,
        "failed": 0,
        "passed": 1
      "per_model_usage": [
          "model_name": "o3-mini",
          "invocation_count": 1,
          "prompt_tokens": 563,
          "completion_tokens": 874,
          "total_tokens": 1437,
          "cached_tokens": 0
      ],
      "per_testing_criteria_results": [
          "testing_criteria": "Push Notification Summary Grader-1808cd0b-eeec-4e0b-a519-337e79f4f5d1",
          "passed": 1,
          "failed": 0
      ],
      "data_source": {
        "type": "completions",
        "source": {
          "type": "file_content",
          "content": [
              "item": {
                "notifications": "\n- New message from Sarah: \"Can you call me later?\"\n- Your package has been delivered!\n- Flash sale: 20% off electronics for the next 2 hours!\n"
          ]
        "input_messages": {
          "type": "template",
          "template": [
              "type": "message",
              "role": "developer",
              "content": {
                "type": "input_text",
                "text": "\n\n\n\nYou are a helpful assistant that takes in an array of push notifications and returns a collapsed summary of them.\nThe push notification will be provided as follows:\n<push_notifications>\n...notificationlist...\n</push_notifications>\n\nYou should return just the summary and nothing else.\n\n\nYou should return a summary that is concise and snappy.\n\n\nHere is an example of a good summary:\n<push_notifications>\n- Traffic alert: Accident reported on Main Street.- Package out for delivery: Expected by 5 PM.- New friend suggestion: Connect with Emma.\n</push_notifications>\n<summary>\nTraffic alert, package expected by 5pm, suggestion for new friend (Emily).\n</summary>\n\n\nHere is an example of a bad summary:\n<push_notifications>\n- Traffic alert: Accident reported on Main Street.- Package out for delivery: Expected by 5 PM.- New friend suggestion: Connect with Emma.\n</push_notifications>\n<summary>\nTraffic alert reported on main street. You have a package that will arrive by 5pm, Emily is a new friend suggested for you.\n</summary>\n"
              "type": "message",
              "role": "user",
              "content": {
                "type": "input_text",
                "text": "<push_notifications>{{item.notifications}}</push_notifications>"
          ]
        "model": "o3-mini",
        "sampling_params": null
      "error": null,
      "metadata": {}
  ],
  "first_id": "evalrun_67e0c7d31560819090d60c0780591042",
  "last_id": "evalrun_67e0c7d31560819090d60c0780591042",
  "has_more": true

##### Returns Examples

  "object": "list",
  "data": [
      "object": "eval.run",
      "id": "evalrun_67e0c7d31560819090d60c0780591042",
      "eval_id": "eval_67e0c726d560819083f19a957c4c640b",
      "report_url": "https://platform.openai.com/evaluations/eval_67e0c726d560819083f19a957c4c640b",
      "status": "completed",
      "model": "o3-mini",
      "name": "bulk_with_negative_examples_o3-mini",
      "created_at": 1742784467,
      "result_counts": {
        "total": 1,
        "errored": 0,
        "failed": 0,
        "passed": 1
      "per_model_usage": [
          "model_name": "o3-mini",
          "invocation_count": 1,
          "prompt_tokens": 563,
          "completion_tokens": 874,
          "total_tokens": 1437,
          "cached_tokens": 0
      ],
      "per_testing_criteria_results": [
          "testing_criteria": "Push Notification Summary Grader-1808cd0b-eeec-4e0b-a519-337e79f4f5d1",
          "passed": 1,
          "failed": 0
      ],
      "data_source": {
        "type": "completions",
        "source": {
          "type": "file_content",
          "content": [
              "item": {
                "notifications": "\n- New message from Sarah: \"Can you call me later?\"\n- Your package has been delivered!\n- Flash sale: 20% off electronics for the next 2 hours!\n"
          ]
        "input_messages": {
          "type": "template",
          "template": [
              "type": "message",
              "role": "developer",
              "content": {
                "type": "input_text",
                "text": "\n\n\n\nYou are a helpful assistant that takes in an array of push notifications and returns a collapsed summary of them.\nThe push notification will be provided as follows:\n<push_notifications>\n...notificationlist...\n</push_notifications>\n\nYou should return just the summary and nothing else.\n\n\nYou should return a summary that is concise and snappy.\n\n\nHere is an example of a good summary:\n<push_notifications>\n- Traffic alert: Accident reported on Main Street.- Package out for delivery: Expected by 5 PM.- New friend suggestion: Connect with Emma.\n</push_notifications>\n<summary>\nTraffic alert, package expected by 5pm, suggestion for new friend (Emily).\n</summary>\n\n\nHere is an example of a bad summary:\n<push_notifications>\n- Traffic alert: Accident reported on Main Street.- Package out for delivery: Expected by 5 PM.- New friend suggestion: Connect with Emma.\n</push_notifications>\n<summary>\nTraffic alert reported on main street. You have a package that will arrive by 5pm, Emily is a new friend suggested for you.\n</summary>\n"
              "type": "message",
              "role": "user",
              "content": {
                "type": "input_text",
                "text": "<push_notifications>{{item.notifications}}</push_notifications>"
          ]
        "model": "o3-mini",
        "sampling_params": null
      "error": null,
      "metadata": {}
  ],
  "first_id": "evalrun_67e0c7d31560819090d60c0780591042",
  "last_id": "evalrun_67e0c7d31560819090d60c0780591042",
  "has_more": true
