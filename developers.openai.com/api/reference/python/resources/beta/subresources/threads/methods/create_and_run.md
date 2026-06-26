<!-- source: https://developers.openai.com/api/reference/python/resources/beta/subresources/threads/methods/create_and_run/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Beta](/api/reference/python/resources/beta)

[Threads](/api/reference/python/resources/beta/subresources/threads)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create thread and run

Deprecated: The Assistants API is deprecated in favor of the Responses API

beta.threads.create\_and\_run(ThreadCreateAndRunParams\*\*kwargs)  -> [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

POST/threads/runs

Create a thread and run it in one request.

##### ParametersExpand Collapse

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

instructions: Optional[str]

Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: Optional[Union[str, [ChatModel](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)), null]]

The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

One of the following:

str

Literal["gpt-5.4", "gpt-5.4-mini", "gpt-5.4-nano", 75 more]

One of the following:

"gpt-5.4"

"gpt-5.4-mini"

"gpt-5.4-nano"

"gpt-5.4-mini-2026-03-17"

"gpt-5.4-nano-2026-03-17"

"gpt-5.3-chat-latest"

"gpt-5.2"

"gpt-5.2-2025-12-11"

"gpt-5.2-chat-latest"

"gpt-5.2-pro"

"gpt-5.2-pro-2025-12-11"

"gpt-5.1"

"gpt-5.1-2025-11-13"

"gpt-5.1-codex"

"gpt-5.1-mini"

"gpt-5.1-chat-latest"

"gpt-5"

"gpt-5-mini"

"gpt-5-nano"

"gpt-5-2025-08-07"

"gpt-5-mini-2025-08-07"

"gpt-5-nano-2025-08-07"

"gpt-5-chat-latest"

"gpt-4.1"

"gpt-4.1-mini"

"gpt-4.1-nano"

"gpt-4.1-2025-04-14"

"gpt-4.1-mini-2025-04-14"

"gpt-4.1-nano-2025-04-14"

"o4-mini"

"o4-mini-2025-04-16"

"o3"

"o3-2025-04-16"

"o3-mini"

"o3-mini-2025-01-31"

"o1"

"o1-2024-12-17"

"o1-preview"

"o1-preview-2024-09-12"

"o1-mini"

"o1-mini-2024-09-12"

"gpt-4o"

"gpt-4o-2024-11-20"

"gpt-4o-2024-08-06"

"gpt-4o-2024-05-13"

"gpt-4o-audio-preview"

"gpt-4o-audio-preview-2024-10-01"

"gpt-4o-audio-preview-2024-12-17"

"gpt-4o-audio-preview-2025-06-03"

"gpt-4o-mini-audio-preview"

"gpt-4o-mini-audio-preview-2024-12-17"

"gpt-4o-search-preview"

"gpt-4o-mini-search-preview"

"gpt-4o-search-preview-2025-03-11"

"gpt-4o-mini-search-preview-2025-03-11"

"chatgpt-4o-latest"

"codex-mini-latest"

"gpt-4o-mini"

"gpt-4o-mini-2024-07-18"

"gpt-4-turbo"

"gpt-4-turbo-2024-04-09"

"gpt-4-0125-preview"

"gpt-4-turbo-preview"

"gpt-4-1106-preview"

"gpt-4-vision-preview"

"gpt-4"

"gpt-4-0314"

"gpt-4-0613"

"gpt-4-32k"

"gpt-4-32k-0314"

"gpt-4-32k-0613"

"gpt-3.5-turbo"

"gpt-3.5-turbo-16k"

"gpt-3.5-turbo-0301"

"gpt-3.5-turbo-0613"

"gpt-3.5-turbo-1106"

"gpt-3.5-turbo-0125"

"gpt-3.5-turbo-16k-0613"

parallel\_tool\_calls: Optional[[bool](/api/reference/python/resources/beta/subresources/threads/methods/create_and_run#(resource)%20beta.threads%20%3E%20(method)%20create_and_run%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20parallel_tool_calls%20%3E%20(schema))]

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

response\_format: Optional[AssistantResponseFormatOptionParam]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

stream: Optional[Literal[false]]

If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

minimum0

maximum2

thread: Optional[[Thread](/api/reference/python/resources/beta/subresources/threads/methods/create_and_run#(resource)%20beta.threads%20%3E%20(method)%20create_and_run%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20thread%20%3E%20(schema))]

Options to create a new thread. If no thread is provided when running a
request, an empty thread will be created.

messages: Optional[Iterable[ThreadMessage]]

A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

content: Union[str, Iterable[[MessageContentPartParam](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_part_param%20%3E%20(schema))]]

The text contents of the message.

One of the following:

str

The text contents of the message.

Iterable[[MessageContentPartParam](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_part_param%20%3E%20(schema))]

An array of content parts with a defined type, each can be of type `text` or images can be passed with `image_url` or `image_file`. Image types are only supported on [Vision-compatible models](https://platform.openai.com/docs/models).

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class TextContentBlockParam: …

The text content that is part of a message.

text: str

Text content to be sent to the model

type: Literal["text"]

Always `text`.

role: Literal["user", "assistant"]

The role of the entity that is creating the message. Allowed values include:

* `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
* `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

One of the following:

"user"

"assistant"

attachments: Optional[Iterable[ThreadMessageAttachment]]

A list of files attached to the message, and the tools they should be added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[Iterable[ThreadMessageAttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class ThreadMessageAttachmentToolFileSearch: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

tool\_resources: Optional[ThreadToolResources]

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ThreadToolResourcesCodeInterpreter]

file\_ids: Optional[Sequence[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ThreadToolResourcesFileSearch]

vector\_store\_ids: Optional[Sequence[str]]

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

vector\_stores: Optional[Iterable[ThreadToolResourcesFileSearchVectorStore]]

A helper to create a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) with file\_ids and attach it to this thread. There can be a maximum of 1 vector store attached to the thread.

chunking\_strategy: Optional[ThreadToolResourcesFileSearchVectorStoreChunkingStrategy]

The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy.

One of the following:

class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyAuto: …

The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.

type: Literal["auto"]

Always `auto`.

class ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStatic: …

static: ThreadToolResourcesFileSearchVectorStoreChunkingStrategyStaticStatic

chunk\_overlap\_tokens: int

The number of tokens that overlap between chunks. The default value is `400`.

Note that the overlap must not exceed half of `max_chunk_size_tokens`.

max\_chunk\_size\_tokens: int

The maximum number of tokens in each chunk. The default value is `800`. The minimum value is `100` and the maximum value is `4096`.

minimum100

maximum4096

type: Literal["static"]

Always `static`.

file\_ids: Optional[Sequence[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs to add to the vector store. For vector stores created before Nov 2025, there can be a maximum of 10,000 files in a vector store. For vector stores created starting in Nov 2025, the limit is 100,000,000 files.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

tool\_choice: Optional[AssistantToolChoiceOptionParam]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tool\_resources: Optional[[ToolResources](/api/reference/python/resources/beta/subresources/threads/methods/create_and_run#(resource)%20beta.threads%20%3E%20(method)%20create_and_run%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20tool_resources%20%3E%20(schema))]

A set of resources that are used by the assistant’s tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[Sequence[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[Sequence[str]]

The ID of the [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this assistant. There can be a maximum of 1 vector store attached to the assistant.

tools: Optional[Iterable[[AssistantToolParam](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]]

Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top\_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.

We generally recommend altering this or temperature but not both.

minimum0

maximum1

truncation\_strategy: Optional[[TruncationStrategy](/api/reference/python/resources/beta/subresources/threads/methods/create_and_run#(resource)%20beta.threads%20%3E%20(method)%20create_and_run%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20truncation_strategy%20%3E%20(schema))]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

##### ReturnsExpand Collapse

class Run: …

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

[AssistantStreamEvent](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_stream_event%20%3E%20(schema))

Represents an event emitted when streaming a Run.

Each event in a server-sent events stream has an `event` and `data` property:

event: thread.created
data: {"id": "thread_123", "object": "thread", ...}

We emit events whenever a new object is created, transitions to a new state, or is being
streamed in parts (deltas). For example, we emit `thread.run.created` when a new run
is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses
to create a message during a run, we emit a `thread.message.created event`, a
`thread.message.in_progress` event, many `thread.message.delta` events, and finally a
`thread.message.completed` event.

We may add additional events over time, so we recommend handling unknown events gracefully
in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to
integrate the Assistants API with streaming.

One of the following:

class ThreadCreated: …

Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.

data: [Thread](/api/reference/python/resources/beta#(resource)%20beta.threads%20%3E%20(model)%20thread%20%3E%20(schema))

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

id: str

The identifier, which can be referenced in API endpoints.

created\_at: int

The Unix timestamp (in seconds) for when the thread was created.

formatunixtime

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread"]

The object type, which is always `thread`.

tool\_resources: Optional[ToolResources]

A set of resources that are made available to the assistant’s tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

code\_interpreter: Optional[ToolResourcesCodeInterpreter]

file\_ids: Optional[List[str]]

A list of [file](https://platform.openai.com/docs/api-reference/files) IDs made available to the `code_interpreter` tool. There can be a maximum of 20 files associated with the tool.

file\_search: Optional[ToolResourcesFileSearch]

vector\_store\_ids: Optional[List[str]]

The [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object) attached to this thread. There can be a maximum of 1 vector store attached to the thread.

event: Literal["thread.created"]

enabled: Optional[bool]

Whether to enable input audio transcription.

class ThreadRunCreated: …

Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.created"]

class ThreadRunQueued: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.queued"]

class ThreadRunInProgress: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.in\_progress"]

class ThreadRunRequiresAction: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.requires\_action"]

class ThreadRunCompleted: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.completed"]

class ThreadRunIncomplete: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.incomplete"]

class ThreadRunFailed: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.failed"]

class ThreadRunCancelling: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.cancelling"]

class ThreadRunCancelled: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.cancelled"]

class ThreadRunExpired: …

Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.

data: [Run](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run%20%3E%20(schema))

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for execution of this run.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run was created.

formatunixtime

expires\_at: Optional[int]

The Unix timestamp (in seconds) for when the run will expire.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run failed.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

Details on why the run is incomplete. Will be `null` if the run is not incomplete.

reason: Optional[Literal["max\_completion\_tokens", "max\_prompt\_tokens"]]

The reason why the run is incomplete. This will point to which specific token limit was reached over the course of the run.

One of the following:

"max\_completion\_tokens"

"max\_prompt\_tokens"

instructions: str

The instructions that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

last\_error: Optional[LastError]

The last error associated with this run. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded", "invalid\_prompt"]

One of `server_error`, `rate_limit_exceeded`, or `invalid_prompt`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

message: str

A human-readable description of the error.

max\_completion\_tokens: Optional[int]

The maximum number of completion tokens specified to have been used over the course of the run.

minimum256

max\_prompt\_tokens: Optional[int]

The maximum number of prompt tokens specified to have been used over the course of the run.

minimum256

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: str

The model that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

object: Literal["thread.run"]

The object type, which is always `thread.run`.

parallel\_tool\_calls: bool

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

required\_action: Optional[RequiredAction]

Details on the action required to continue the run. Will be `null` if no action is required.

submit\_tool\_outputs: RequiredActionSubmitToolOutputs

Details on the tool outputs needed for this run to continue.

tool\_calls: List[[RequiredActionFunctionToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20required_action_function_tool_call%20%3E%20(schema))]

A list of the relevant tool calls.

id: str

The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) endpoint.

function: Function

The function definition.

arguments: str

The arguments that the model expects you to pass to the function.

name: str

The name of the function.

type: Literal["function"]

The type of tool call the output is required for. For now, this is always `function`.

type: Literal["submit\_tool\_outputs"]

For now, this is always `submit_tool_outputs`.

response\_format: Optional[AssistantResponseFormatOption]

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models#gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models#gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which ensures the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables JSON mode, which ensures the message the model generates is valid JSON.

**Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly “stuck” request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

One of the following:

Literal["auto"]

`auto` is the default value

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

class ResponseFormatJSONSchema: …

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

json\_schema: JSONSchema

Structured Outputs configuration options, including a JSON Schema.

name: str

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the response format is for, used by the model to
determine how to respond in the format.

schema: Optional[Dict[str, object]]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

strict: Optional[bool]

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

type: Literal["json\_schema"]

The type of response format being defined. Always `json_schema`.

started\_at: Optional[int]

The Unix timestamp (in seconds) for when the run was started.

formatunixtime

status: [RunStatus](/api/reference/python/resources/beta#(resource)%20beta.threads.runs%20%3E%20(model)%20run_status%20%3E%20(schema))

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

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was executed on as a part of this run.

tool\_choice: Optional[AssistantToolChoiceOption]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tools and instead generates a message.
`auto` is the default value and means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools before responding to the user.
Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tools and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user.

One of the following:

"none"

"auto"

"required"

class AssistantToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific tool.

type: Literal["function", "code\_interpreter", "file\_search"]

The type of the tool. If type is `function`, the function name must be set

One of the following:

"function"

"code\_interpreter"

"file\_search"

function: Optional[AssistantToolChoiceFunction]

name: str

The name of the function to call.

tools: List[[AssistantTool](/api/reference/python/resources/beta#(resource)%20beta.assistants%20%3E%20(model)%20assistant_tool%20%3E%20(schema))]

The list of tools that the [assistant](https://platform.openai.com/docs/api-reference/assistants) used for this run.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class FileSearchTool: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

file\_search: Optional[FileSearch]

Overrides for the file search tool.

max\_num\_results: Optional[int]

The maximum number of results the file search tool should output. The default is 20 for `gpt-4*` models and 5 for `gpt-3.5-turbo`. This number should be between 1 and 50 inclusive.

Note that the file search tool may output fewer than `max_num_results` results. See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

minimum1

maximum50

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score\_threshold of 0.

See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

ranker: Optional[Literal["auto", "default\_2024\_08\_21"]]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

class FunctionTool: …

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[FunctionParameters]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

strict: Optional[bool]

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

type: Literal["function"]

The type of tool being defined: `function`

truncation\_strategy: Optional[TruncationStrategy]

Controls for how a thread will be truncated prior to the run. Use this to control the initial context window of the run.

type: Literal["auto", "last\_messages"]

The truncation strategy to use for the thread. The default is `auto`. If set to `last_messages`, the thread will be truncated to the n most recent messages in the thread. When set to `auto`, messages in the middle of the thread will be dropped to fit the context length of the model, `max_prompt_tokens`.

One of the following:

"auto"

"last\_messages"

last\_messages: Optional[int]

The number of most recent messages from the thread when constructing the context for the run.

minimum1

usage: Optional[Usage]

Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).

completion\_tokens: int

Number of completion tokens used over the course of the run.

prompt\_tokens: int

Number of prompt tokens used over the course of the run.

total\_tokens: int

Total number of tokens used (prompt + completion).

temperature: Optional[float]

The sampling temperature used for this run. If not set, defaults to 1.

top\_p: Optional[float]

The nucleus sampling value used for this run. If not set, defaults to 1.

event: Literal["thread.run.expired"]

class ThreadRunStepCreated: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.created"]

class ThreadRunStepInProgress: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.in\_progress"]

class ThreadRunStepDelta: …

Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.

data: [RunStepDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta_event%20%3E%20(schema))

Represents a run step delta i.e. any changed fields on a run step during streaming.

id: str

The identifier of the run step, which can be referenced in API endpoints.

delta: [RunStepDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step_delta%20%3E%20(schema))

The delta containing the fields that have changed on the run step.

step\_details: Optional[StepDetails]

The details of the run step.

One of the following:

class RunStepDeltaMessageDelta: …

Details of the message creation by the run step.

type: Literal["message\_creation"]

Always `message_creation`.

message\_creation: Optional[MessageCreation]

message\_id: Optional[str]

The ID of the message that was created by this run step.

class ToolCallDeltaObject: …

Details of the tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

tool\_calls: Optional[List[[ToolCallDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call_delta%20%3E%20(schema))]]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCallDelta: …

Details of the Code Interpreter tool call the run step was involved in.

index: int

The index of the tool call in the tool calls array.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

id: Optional[str]

The ID of the tool call.

code\_interpreter: Optional[CodeInterpreter]

The Code Interpreter tool call definition.

input: Optional[str]

The input to the Code Interpreter tool call.

outputs: Optional[List[CodeInterpreterOutput]]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterLogs: …

Text output from the Code Interpreter tool call as part of a run step.

index: int

The index of the output in the outputs array.

type: Literal["logs"]

Always `logs`.

logs: Optional[str]

The text output from the Code Interpreter tool call.

class CodeInterpreterOutputImage: …

index: int

The index of the output in the outputs array.

type: Literal["image"]

Always `image`.

image: Optional[Image]

file\_id: Optional[str]

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

class FileSearchToolCallDelta: …

file\_search: object

For now, this is always going to be an empty object.

index: int

The index of the tool call in the tool calls array.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

class FunctionToolCallDelta: …

index: int

The index of the tool call in the tool calls array.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

id: Optional[str]

The ID of the tool call object.

function: Optional[Function]

The definition of the function that was called.

arguments: Optional[str]

The arguments passed to the function.

name: Optional[str]

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

object: Literal["thread.run.step.delta"]

The object type, which is always `thread.run.step.delta`.

event: Literal["thread.run.step.delta"]

class ThreadRunStepCompleted: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.completed"]

class ThreadRunStepFailed: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.failed"]

class ThreadRunStepCancelled: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.cancelled"]

class ThreadRunStepExpired: …

Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.

data: [RunStep](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20run_step%20%3E%20(schema))

Represents a step in execution of a run.

id: str

The identifier of the run step, which can be referenced in API endpoints.

assistant\_id: str

The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) associated with the run step.

cancelled\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step was cancelled.

formatunixtime

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step completed.

formatunixtime

created\_at: int

The Unix timestamp (in seconds) for when the run step was created.

formatunixtime

expired\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.

formatunixtime

failed\_at: Optional[int]

The Unix timestamp (in seconds) for when the run step failed.

formatunixtime

last\_error: Optional[LastError]

The last error associated with this run step. Will be `null` if there are no errors.

code: Literal["server\_error", "rate\_limit\_exceeded"]

One of `server_error` or `rate_limit_exceeded`.

One of the following:

"server\_error"

"rate\_limit\_exceeded"

message: str

A human-readable description of the error.

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.run.step"]

The object type, which is always `thread.run.step`.

run\_id: str

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) that this run step is a part of.

status: Literal["in\_progress", "cancelled", "failed", 2 more]

The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.

One of the following:

"in\_progress"

"cancelled"

"failed"

"completed"

"expired"

step\_details: StepDetails

The details of the run step.

One of the following:

class MessageCreationStepDetails: …

Details of the message creation by the run step.

message\_creation: MessageCreation

message\_id: str

The ID of the message that was created by this run step.

type: Literal["message\_creation"]

Always `message_creation`.

class ToolCallsStepDetails: …

Details of the tool call.

tool\_calls: List[[ToolCall](/api/reference/python/resources/beta#(resource)%20beta.threads.runs.steps%20%3E%20(model)%20tool_call%20%3E%20(schema))]

An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `file_search`, or `function`.

One of the following:

class CodeInterpreterToolCall: …

Details of the Code Interpreter tool call the run step was involved in.

id: str

The ID of the tool call.

code\_interpreter: CodeInterpreter

The Code Interpreter tool call definition.

input: str

The input to the Code Interpreter tool call.

outputs: List[CodeInterpreterOutput]

The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.

One of the following:

class CodeInterpreterOutputLogs: …

Text output from the Code Interpreter tool call as part of a run step.

logs: str

The text output from the Code Interpreter tool call.

type: Literal["logs"]

Always `logs`.

class CodeInterpreterOutputImage: …

image: CodeInterpreterOutputImageImage

file\_id: str

The [file](https://platform.openai.com/docs/api-reference/files) ID of the image.

type: Literal["image"]

Always `image`.

type: Literal["code\_interpreter"]

The type of tool call. This is always going to be `code_interpreter` for this type of tool call.

class FileSearchToolCall: …

id: str

The ID of the tool call object.

file\_search: FileSearch

For now, this is always going to be an empty object.

ranking\_options: Optional[FileSearchRankingOptions]

The ranking options for the file search.

ranker: Literal["auto", "default\_2024\_08\_21"]

The ranker to use for the file search. If not specified will use the `auto` ranker.

One of the following:

"auto"

"default\_2024\_08\_21"

score\_threshold: float

The score threshold for the file search. All values must be a floating point number between 0 and 1.

minimum0

maximum1

results: Optional[List[FileSearchResult]]

The results of the file search.

file\_id: str

The ID of the file that result was found in.

file\_name: str

The name of the file that result was found in.

score: float

The score of the result. All values must be a floating point number between 0 and 1.

minimum0

maximum1

content: Optional[List[FileSearchResultContent]]

The content of the result that was found. The content is only included if requested via the include query parameter.

text: Optional[str]

The text content of the file.

type: Optional[Literal["text"]]

The type of the content.

type: Literal["file\_search"]

The type of tool call. This is always going to be `file_search` for this type of tool call.

class FunctionToolCall: …

id: str

The ID of the tool call object.

function: Function

The definition of the function that was called.

arguments: str

The arguments passed to the function.

name: str

The name of the function.

output: Optional[str]

The output of the function. This will be `null` if the outputs have not been [submitted](https://platform.openai.com/docs/api-reference/runs/submitToolOutputs) yet.

type: Literal["function"]

The type of tool call. This is always going to be `function` for this type of tool call.

type: Literal["tool\_calls"]

Always `tool_calls`.

thread\_id: str

The ID of the [thread](https://platform.openai.com/docs/api-reference/threads) that was run.

type: Literal["message\_creation", "tool\_calls"]

The type of run step, which can be either `message_creation` or `tool_calls`.

One of the following:

"message\_creation"

"tool\_calls"

usage: Optional[Usage]

Usage statistics related to the run step. This value will be `null` while the run step’s status is `in_progress`.

completion\_tokens: int

Number of completion tokens used over the course of the run step.

prompt\_tokens: int

Number of prompt tokens used over the course of the run step.

total\_tokens: int

Total number of tokens used (prompt + completion).

event: Literal["thread.run.step.expired"]

class ThreadMessageCreated: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: Optional[str]

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Optional[List[Attachment]]

A list of files attached to the message, and the tools they were added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[List[AttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class AttachmentToolAssistantToolsFileSearchTypeOnly: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: List[[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

annotations: List[[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

value: str

The data that makes up the text.

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

created\_at: int

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

On an incomplete message, details about why the message is incomplete.

reason: Literal["content\_filter", "max\_tokens", "run\_cancelled", 2 more]

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.message"]

The object type, which is always `thread.message`.

role: Literal["user", "assistant"]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: Optional[str]

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: Literal["in\_progress", "incomplete", "completed"]

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: str

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: Literal["thread.message.created"]

class ThreadMessageInProgress: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: Optional[str]

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Optional[List[Attachment]]

A list of files attached to the message, and the tools they were added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[List[AttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class AttachmentToolAssistantToolsFileSearchTypeOnly: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: List[[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

annotations: List[[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

value: str

The data that makes up the text.

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

created\_at: int

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

On an incomplete message, details about why the message is incomplete.

reason: Literal["content\_filter", "max\_tokens", "run\_cancelled", 2 more]

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.message"]

The object type, which is always `thread.message`.

role: Literal["user", "assistant"]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: Optional[str]

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: Literal["in\_progress", "incomplete", "completed"]

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: str

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: Literal["thread.message.in\_progress"]

class ThreadMessageDelta: …

Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.

data: [MessageDeltaEvent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta_event%20%3E%20(schema))

Represents a message delta i.e. any changed fields on a message during streaming.

id: str

The identifier of the message, which can be referenced in API endpoints.

delta: [MessageDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_delta%20%3E%20(schema))

The delta containing the fields that have changed on the Message.

content: Optional[List[[MessageContentDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content_delta%20%3E%20(schema))]]

The content of the message in array of text and/or images.

One of the following:

class ImageFileDeltaBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_file"]

Always `image_file`.

image\_file: Optional[ImageFileDelta]

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

file\_id: Optional[str]

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

class TextDeltaBlock: …

The text content that is part of a message.

index: int

The index of the content part in the message.

type: Literal["text"]

Always `text`.

text: Optional[TextDelta]

annotations: Optional[List[[AnnotationDelta](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation_delta%20%3E%20(schema))]]

One of the following:

class FileCitationDeltaAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

index: int

The index of the annotation in the text content part.

type: Literal["file\_citation"]

Always `file_citation`.

end\_index: Optional[int]

minimum0

file\_citation: Optional[FileCitation]

file\_id: Optional[str]

The ID of the specific File the citation is from.

quote: Optional[str]

The specific quote in the file.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

class FilePathDeltaAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

index: int

The index of the annotation in the text content part.

type: Literal["file\_path"]

Always `file_path`.

end\_index: Optional[int]

minimum0

file\_path: Optional[FilePath]

file\_id: Optional[str]

The ID of the file that was generated.

start\_index: Optional[int]

minimum0

text: Optional[str]

The text in the message content that needs to be replaced.

value: Optional[str]

The data that makes up the text.

class RefusalDeltaBlock: …

The refusal content that is part of a message.

index: int

The index of the refusal part in the message.

type: Literal["refusal"]

Always `refusal`.

refusal: Optional[str]

class ImageURLDeltaBlock: …

References an image URL in the content of a message.

index: int

The index of the content part in the message.

type: Literal["image\_url"]

Always `image_url`.

image\_url: Optional[ImageURLDelta]

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

url: Optional[str]

The URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

role: Optional[Literal["user", "assistant"]]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

object: Literal["thread.message.delta"]

The object type, which is always `thread.message.delta`.

event: Literal["thread.message.delta"]

class ThreadMessageCompleted: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: Optional[str]

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Optional[List[Attachment]]

A list of files attached to the message, and the tools they were added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[List[AttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class AttachmentToolAssistantToolsFileSearchTypeOnly: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: List[[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

annotations: List[[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

value: str

The data that makes up the text.

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

created\_at: int

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

On an incomplete message, details about why the message is incomplete.

reason: Literal["content\_filter", "max\_tokens", "run\_cancelled", 2 more]

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.message"]

The object type, which is always `thread.message`.

role: Literal["user", "assistant"]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: Optional[str]

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: Literal["in\_progress", "incomplete", "completed"]

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: str

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: Literal["thread.message.completed"]

class ThreadMessageIncomplete: …

Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.

data: [Message](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message%20%3E%20(schema))

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

id: str

The identifier, which can be referenced in API endpoints.

assistant\_id: Optional[str]

If applicable, the ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) that authored this message.

attachments: Optional[List[Attachment]]

A list of files attached to the message, and the tools they were added to.

file\_id: Optional[str]

The ID of the file to attach to the message.

tools: Optional[List[AttachmentTool]]

The tools to add this file to.

One of the following:

class CodeInterpreterTool: …

type: Literal["code\_interpreter"]

The type of tool being defined: `code_interpreter`

class AttachmentToolAssistantToolsFileSearchTypeOnly: …

type: Literal["file\_search"]

The type of tool being defined: `file_search`

completed\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was completed.

formatunixtime

content: List[[MessageContent](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20message_content%20%3E%20(schema))]

The content of the message in array of text and/or images.

One of the following:

class ImageFileContentBlock: …

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

image\_file: [ImageFile](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_file%20%3E%20(schema))

file\_id: str

The [File](https://platform.openai.com/docs/api-reference/files) ID of the image in the message content. Set `purpose="vision"` when uploading the File if you need to later display the file content.

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image if specified by the user. `low` uses fewer tokens, you can opt in to high resolution using `high`.

One of the following:

"auto"

"low"

"high"

type: Literal["image\_file"]

Always `image_file`.

class ImageURLContentBlock: …

References an image URL in the content of a message.

image\_url: [ImageURL](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20image_url%20%3E%20(schema))

url: str

The external URL of the image, must be a supported image types: jpeg, jpg, png, gif, webp.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. `low` uses fewer tokens, you can opt in to high resolution using `high`. Default value is `auto`

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class TextContentBlock: …

The text content that is part of a message.

text: [Text](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20text%20%3E%20(schema))

annotations: List[[Annotation](/api/reference/python/resources/beta#(resource)%20beta.threads.messages%20%3E%20(model)%20annotation%20%3E%20(schema))]

One of the following:

class FileCitationAnnotation: …

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the “file\_search” tool to search files.

end\_index: int

minimum0

file\_citation: FileCitation

file\_id: str

The ID of the specific File the citation is from.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_citation"]

Always `file_citation`.

class FilePathAnnotation: …

A URL for the file that’s generated when the assistant used the `code_interpreter` tool to generate a file.

end\_index: int

minimum0

file\_path: FilePath

file\_id: str

The ID of the file that was generated.

start\_index: int

minimum0

text: str

The text in the message content that needs to be replaced.

type: Literal["file\_path"]

Always `file_path`.

value: str

The data that makes up the text.

type: Literal["text"]

Always `text`.

class RefusalContentBlock: …

The refusal content generated by the assistant.

refusal: str

type: Literal["refusal"]

Always `refusal`.

created\_at: int

The Unix timestamp (in seconds) for when the message was created.

formatunixtime

incomplete\_at: Optional[int]

The Unix timestamp (in seconds) for when the message was marked as incomplete.

formatunixtime

incomplete\_details: Optional[IncompleteDetails]

On an incomplete message, details about why the message is incomplete.

reason: Literal["content\_filter", "max\_tokens", "run\_cancelled", 2 more]

The reason the message is incomplete.

One of the following:

"content\_filter"

"max\_tokens"

"run\_cancelled"

"run\_expired"

"run\_failed"

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

object: Literal["thread.message"]

The object type, which is always `thread.message`.

role: Literal["user", "assistant"]

The entity that produced the message. One of `user` or `assistant`.

One of the following:

"user"

"assistant"

run\_id: Optional[str]

The ID of the [run](https://platform.openai.com/docs/api-reference/runs) associated with the creation of this message. Value is `null` when messages are created manually using the create message or create thread endpoints.

status: Literal["in\_progress", "incomplete", "completed"]

The status of the message, which can be either `in_progress`, `incomplete`, or `completed`.

One of the following:

"in\_progress"

"incomplete"

"completed"

thread\_id: str

The [thread](https://platform.openai.com/docs/api-reference/threads) ID that this message belongs to.

event: Literal["thread.message.incomplete"]

class ErrorEvent: …

Occurs when an [error](https://platform.openai.com/docs/guides/error-codes#api-errors) occurs. This can happen due to an internal server error or a timeout.

data: [ErrorObject](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20error_object%20%3E%20(schema))

code: Optional[str]

message: str

param: Optional[str]

type: str

event: Literal["error"]

DefaultStreamingStreaming with Functions

### Create thread and run

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

run = client.beta.threads.create_and_run(
  assistant_id="asst_abc123",
  thread={
    "messages": [
      {"role": "user", "content": "Explain deep learning to a 5 year old."}
    ]

print(run)

  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076792,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": null,
  "expires_at": 1699077392,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "required_action": null,
  "last_error": null,
  "model": "gpt-4o",
  "instructions": "You are a helpful assistant.",
  "tools": [],
  "tool_resources": {},
  "metadata": {},
  "temperature": 1.0,
  "top_p": 1.0,
  "max_completion_tokens": null,
  "max_prompt_tokens": null,
  "truncation_strategy": {
    "type": "auto",
    "last_messages": null
  "incomplete_details": null,
  "usage": null,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true

### Create thread and run

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

stream = client.beta.threads.create_and_run(
  assistant_id="asst_123",
  thread={
    "messages": [
      {"role": "user", "content": "Hello"}
    ]
  stream=True

for event in stream:
  print(event)

event: thread.created
data: {"id":"thread_123","object":"thread","created_at":1710348075,"metadata":{}}

event: thread.run.created
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"tool_resources":{},"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}

event: thread.run.queued
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"tool_resources":{},"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}

event: thread.run.in_progress
data: {"id":"run_123","object":"thread.run","created_at":1710348075,"assistant_id":"asst_123","thread_id":"thread_123","status":"in_progress","started_at":null,"expires_at":1710348675,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"tool_resources":{},"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}

event: thread.run.step.created
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.run.step.in_progress
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":null}

event: thread.message.created
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[], "metadata":{}}

event: thread.message.in_progress
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"in_progress","incomplete_details":null,"incomplete_at":null,"completed_at":null,"role":"assistant","content":[], "metadata":{}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"Hello","annotations":[]}}]}}

...

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":" today"}}]}}

event: thread.message.delta
data: {"id":"msg_001","object":"thread.message.delta","delta":{"content":[{"index":0,"type":"text","text":{"value":"?"}}]}}

event: thread.message.completed
data: {"id":"msg_001","object":"thread.message","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","run_id":"run_123","status":"completed","incomplete_details":null,"incomplete_at":null,"completed_at":1710348077,"role":"assistant","content":[{"type":"text","text":{"value":"Hello! How can I assist you today?","annotations":[]}}], "metadata":{}}

event: thread.run.step.completed
data: {"id":"step_001","object":"thread.run.step","created_at":1710348076,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"message_creation","status":"completed","cancelled_at":null,"completed_at":1710348077,"expires_at":1710348675,"failed_at":null,"last_error":null,"step_details":{"type":"message_creation","message_creation":{"message_id":"msg_001"}},"usage":{"prompt_tokens":20,"completion_tokens":11,"total_tokens":31}}

event: thread.run.completed
{"id":"run_123","object":"thread.run","created_at":1710348076,"assistant_id":"asst_123","thread_id":"thread_123","status":"completed","started_at":1713226836,"expires_at":null,"cancelled_at":null,"failed_at":null,"completed_at":1713226837,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":{"prompt_tokens":345,"completion_tokens":11,"total_tokens":356},"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}

event: done
data: [DONE]

### Create thread and run

Python

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

from openai import OpenAI
client = OpenAI()

tools = [
    "type": "function",
    "function": {
      "name": "get_current_weather",
      "description": "Get the current weather in a given location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA",
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
        "required": ["location"],
]

stream = client.beta.threads.create_and_run(
  thread={
      "messages": [
        {"role": "user", "content": "What is the weather like in San Francisco?"}
      ]
  assistant_id="asst_abc123",
  tools=tools,
  stream=True

for event in stream:
  print(event)

event: thread.created
data: {"id":"thread_123","object":"thread","created_at":1710351818,"metadata":{}}

event: thread.run.created
data: {"id":"run_123","object":"thread.run","created_at":1710351818,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710352418,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"},"unit":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location"]}}}],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.queued
data: {"id":"run_123","object":"thread.run","created_at":1710351818,"assistant_id":"asst_123","thread_id":"thread_123","status":"queued","started_at":null,"expires_at":1710352418,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"},"unit":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location"]}}}],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.in_progress
data: {"id":"run_123","object":"thread.run","created_at":1710351818,"assistant_id":"asst_123","thread_id":"thread_123","status":"in_progress","started_at":1710351818,"expires_at":1710352418,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":null,"last_error":null,"model":"gpt-4o","instructions":null,"tools":[{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"},"unit":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location"]}}}],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":null,"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: thread.run.step.created
data: {"id":"step_001","object":"thread.run.step","created_at":1710351819,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"tool_calls","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710352418,"failed_at":null,"last_error":null,"step_details":{"type":"tool_calls","tool_calls":[]},"usage":null}

event: thread.run.step.in_progress
data: {"id":"step_001","object":"thread.run.step","created_at":1710351819,"run_id":"run_123","assistant_id":"asst_123","thread_id":"thread_123","type":"tool_calls","status":"in_progress","cancelled_at":null,"completed_at":null,"expires_at":1710352418,"failed_at":null,"last_error":null,"step_details":{"type":"tool_calls","tool_calls":[]},"usage":null}

event: thread.run.step.delta
data: {"id":"step_001","object":"thread.run.step.delta","delta":{"step_details":{"type":"tool_calls","tool_calls":[{"index":0,"id":"call_XXNp8YGaFrjrSjgqxtC8JJ1B","type":"function","function":{"name":"get_current_weather","arguments":"","output":null}}]}}}

event: thread.run.step.delta
data: {"id":"step_001","object":"thread.run.step.delta","delta":{"step_details":{"type":"tool_calls","tool_calls":[{"index":0,"type":"function","function":{"arguments":"{\""}}]}}}

event: thread.run.step.delta
data: {"id":"step_001","object":"thread.run.step.delta","delta":{"step_details":{"type":"tool_calls","tool_calls":[{"index":0,"type":"function","function":{"arguments":"location"}}]}}}

...

event: thread.run.step.delta
data: {"id":"step_001","object":"thread.run.step.delta","delta":{"step_details":{"type":"tool_calls","tool_calls":[{"index":0,"type":"function","function":{"arguments":"ahrenheit"}}]}}}

event: thread.run.step.delta
data: {"id":"step_001","object":"thread.run.step.delta","delta":{"step_details":{"type":"tool_calls","tool_calls":[{"index":0,"type":"function","function":{"arguments":"\"}"}}]}}}

event: thread.run.requires_action
data: {"id":"run_123","object":"thread.run","created_at":1710351818,"assistant_id":"asst_123","thread_id":"thread_123","status":"requires_action","started_at":1710351818,"expires_at":1710352418,"cancelled_at":null,"failed_at":null,"completed_at":null,"required_action":{"type":"submit_tool_outputs","submit_tool_outputs":{"tool_calls":[{"id":"call_XXNp8YGaFrjrSjgqxtC8JJ1B","type":"function","function":{"name":"get_current_weather","arguments":"{\"location\":\"San Francisco, CA\",\"unit\":\"fahrenheit\"}"}}]}},"last_error":null,"model":"gpt-4o","instructions":null,"tools":[{"type":"function","function":{"name":"get_current_weather","description":"Get the current weather in a given location","parameters":{"type":"object","properties":{"location":{"type":"string","description":"The city and state, e.g. San Francisco, CA"},"unit":{"type":"string","enum":["celsius","fahrenheit"]}},"required":["location"]}}}],"metadata":{},"temperature":1.0,"top_p":1.0,"max_completion_tokens":null,"max_prompt_tokens":null,"truncation_strategy":{"type":"auto","last_messages":null},"incomplete_details":null,"usage":{"prompt_tokens":345,"completion_tokens":11,"total_tokens":356},"response_format":"auto","tool_choice":"auto","parallel_tool_calls":true}}

event: done
data: [DONE]

##### Returns Examples

  "id": "run_abc123",
  "object": "thread.run",
  "created_at": 1699076792,
  "assistant_id": "asst_abc123",
  "thread_id": "thread_abc123",
  "status": "queued",
  "started_at": null,
  "expires_at": 1699077392,
  "cancelled_at": null,
  "failed_at": null,
  "completed_at": null,
  "required_action": null,
  "last_error": null,
  "model": "gpt-4o",
  "instructions": "You are a helpful assistant.",
  "tools": [],
  "tool_resources": {},
  "metadata": {},
  "temperature": 1.0,
  "top_p": 1.0,
  "max_completion_tokens": null,
  "max_prompt_tokens": null,
  "truncation_strategy": {
    "type": "auto",
    "last_messages": null
  "incomplete_details": null,
  "usage": null,
  "response_format": "auto",
  "tool_choice": "auto",
  "parallel_tool_calls": true
