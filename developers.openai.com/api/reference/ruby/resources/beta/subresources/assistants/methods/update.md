<!-- source: https://developers.openai.com/api/reference/ruby/resources/beta/subresources/assistants/methods/update/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Beta](/api/reference/ruby/resources/beta)

[Assistants](/api/reference/ruby/resources/beta/subresources/assistants)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Modify assistant

Deprecated

beta.assistants.update(assistant\_id, \*\*kwargs) -> [Assistant](/api/reference/ruby/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant%20%3E%20(schema)) { id, created\_at, description, 10 more }

POST/assistants/{assistant\_id}

Modifies an assistant.

##### ParametersExpand Collapse

assistant\_id: String

description: String

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: String

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String | :"gpt-5" | :"gpt-5-mini" | :"gpt-5-nano" | 39 more

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

One of the following:

String = String

Model = :"gpt-5" | :"gpt-5-mini" | :"gpt-5-nano" | 39 more

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

One of the following:

:"gpt-5"

:"gpt-5-mini"

:"gpt-5-nano"

:"gpt-5-2025-08-07"

:"gpt-5-mini-2025-08-07"

:"gpt-5-nano-2025-08-07"

:"gpt-4.1"

:"gpt-4.1-mini"

:"gpt-4.1-nano"

:"gpt-4.1-2025-04-14"

:"gpt-4.1-mini-2025-04-14"

:"gpt-4.1-nano-2025-04-14"

:"o3-mini"

:"o3-mini-2025-01-31"

:o1

:"o1-2024-12-17"

:"gpt-4o"

:"gpt-4o-2024-11-20"

:"gpt-4o-2024-08-06"

:"gpt-4o-2024-05-13"

:"gpt-4o-mini"

:"gpt-4o-mini-2024-07-18"

:"gpt-4.5-preview"

:"gpt-4.5-preview-2025-02-27"

:"gpt-4-turbo"

:"gpt-4-turbo-2024-04-09"

:"gpt-4-0125-preview"

:"gpt-4-turbo-preview"

:"gpt-4-1106-preview"

:"gpt-4-vision-preview"

:"gpt-4"

:"gpt-4-0314"

:"gpt-4-0613"

:"gpt-4-32k"

:"gpt-4-32k-0314"

:"gpt-4-32k-0613"

:"gpt-3.5-turbo"

:"gpt-3.5-turbo-16k"

:"gpt-3.5-turbo-0613"

:"gpt-3.5-turbo-1106"

:"gpt-3.5-turbo-0125"

:"gpt-3.5-turbo-16k-0613"

name: String

The name of the assistant. The maximum length is 256 characters.

maxLength256

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

response\_format: [AssistantResponseFormatOption](/api/reference/ruby/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

AssistantResponseFormatOption = :auto

`auto` is the default value

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

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

temperature: Float

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources: ToolResources{ code\_interpreter, file\_search}

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: CodeInterpreter{ file\_ids}

file\_ids: Array[String]

Overrides the list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: FileSearch{ vector\_store\_ids}

vector\_store\_ids: Array[String]

Overrides the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

tools: Array[[AssistantTool](/api/reference/ruby/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterTool { type }

type: :code\_interpreter

The type of tool being defined: `code_interpreter`

class FileSearchTool { type, file\_search }

type: :file\_search

The type of tool being defined: `file_search`

file\_search: FileSearch{ max\_num\_results, ranking\_options}

Overrides for the file search tool.

max\_num\_results: Integer

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: RankingOptions{ score\_threshold, ranker}

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

class FunctionTool { function, type }

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

The type of tool being defined: `function`

top\_p: Float

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

##### ReturnsExpand Collapse

class Assistant { id, created\_at, description, 10 more }

Represents an `assistant` that can call the model and use tools.

id: String

The identifier, which can be referenced in API endpoints.

created\_at: Integer

The Unix timestamp (in seconds) for when the assistant was created.

formatunixtime

description: String

The description of the assistant. The maximum length is 512 characters.

maxLength512

instructions: String

The system instructions that the assistant uses. The maximum length is 256,000 characters.

maxLength256000

metadata: [Metadata](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: String

ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models) for descriptions of them.

name: String

The name of the assistant. The maximum length is 256 characters.

maxLength256

object: :assistant

The object type, which is always `assistant`.

tools: Array[[AssistantTool](/api/reference/ruby/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterTool { type }

type: :code\_interpreter

The type of tool being defined: `code_interpreter`

class FileSearchTool { type, file\_search }

type: :file\_search

The type of tool being defined: `file_search`

file\_search: FileSearch{ max\_num\_results, ranking\_options}

Overrides for the file search tool.

max\_num\_results: Integer

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: RankingOptions{ score\_threshold, ranker}

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: Float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: :auto | :default\_2024\_08\_21

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

:auto

:default\_2024\_08\_21

class FunctionTool { function, type }

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

The type of tool being defined: `function`

response\_format: [AssistantResponseFormatOption](/api/reference/ruby/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20assistant_response_format_option%20%3E%20(schema))

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

AssistantResponseFormatOption = :auto

`auto` is the default value

class ResponseFormatText { type }

Default response format. Used to generate text responses.

type: :text

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: :json\_object

The type of response format being defined. Always `json_object`.

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

temperature: Float

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

tool\_resources: ToolResources{ code\_interpreter, file\_search}

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: CodeInterpreter{ file\_ids}

file\_ids: Array[String]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code\_interpreter“ tool. There can be a maximum of 20 files associated with the tool.

file\_search: FileSearch{ vector\_store\_ids}

vector\_store\_ids: Array[String]

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

top\_p: Float

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

### Modify assistant

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

assistant = openai.beta.assistants.update("assistant_id")

puts(assistant)

  "id": "asst_123",
  "object": "assistant",
  "created_at": 1699009709,
  "name": "HR Helper",
  "description": null,
  "model": "gpt-4o",
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
  "tools": [
      "type": "file_search"
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": []
  "metadata": {},
  "top_p": 1.0,
  "temperature": 1.0,
  "response_format": "auto"

##### Returns Examples

  "id": "asst_123",
  "object": "assistant",
  "created_at": 1699009709,
  "name": "HR Helper",
  "description": null,
  "model": "gpt-4o",
  "instructions": "You are an HR bot, and you have access to files to answer employee questions about company policies. Always response with info from either of the files.",
  "tools": [
      "type": "file_search"
  ],
  "tool_resources": {
    "file_search": {
      "vector_store_ids": []
  "metadata": {},
  "top_p": 1.0,
  "temperature": 1.0,
  "response_format": "auto"
