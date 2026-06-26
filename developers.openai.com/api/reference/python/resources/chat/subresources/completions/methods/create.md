<!-- source: https://developers.openai.com/api/reference/python/resources/chat/subresources/completions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Chat](/api/reference/python/resources/chat)

[Completions](/api/reference/python/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create chat completion

chat.completions.create(CompletionCreateParams\*\*kwargs)  -> [ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

POST/chat/completions

**Starting a new project?** We recommend trying [Responses](https://platform.openai.com/docs/api-reference/responses)
to take advantage of the latest OpenAI platform features. Compare
[Chat Completions with Responses](https://platform.openai.com/docs/guides/responses-vs-chat-completions?api-mode=responses).

---

Creates a model response for the given chat conversation. Learn more in the
[text generation](https://platform.openai.com/docs/guides/text-generation), [vision](https://platform.openai.com/docs/guides/vision),
and [audio](https://platform.openai.com/docs/guides/audio) guides.

Parameter support can differ depending on the model used to generate the
response, particularly for newer reasoning models. Parameters that are only
supported for reasoning models are noted below. For the current state of
unsupported parameters in reasoning models,
[refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).

Returns a chat completion object, or a streamed sequence of chat completion
chunk objects if the request is streamed.

##### ParametersExpand Collapse

messages: Iterable[[ChatCompletionMessageParam](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_param%20%3E%20(schema))]

A list of messages comprising the conversation so far. Depending on the
[model](https://platform.openai.com/docs/models) you use, different message types (modalities) are
supported, like [text](https://platform.openai.com/docs/guides/text-generation),
[images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

One of the following:

class ChatCompletionDeveloperMessageParam: …

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content: Union[str, List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]]

The contents of the developer message.

One of the following:

str

The contents of the developer message.

List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]

An array of content parts with a defined type. For developer messages, only type `text` is supported.

text: str

The text content.

type: Literal["text"]

The type of the content part.

role: Literal["developer"]

The role of the messages author, in this case `developer`.

name: Optional[str]

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionSystemMessageParam: …

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content: Union[str, List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]]

The contents of the system message.

One of the following:

str

The contents of the system message.

List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]

An array of content parts with a defined type. For system messages, only type `text` is supported.

text: str

The text content.

type: Literal["text"]

The type of the content part.

role: Literal["system"]

The role of the messages author, in this case `system`.

name: Optional[str]

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionUserMessageParam: …

Messages sent by an end user, containing prompts or additional context
information.

content: Union[str, List[[ChatCompletionContentPart](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]]

The contents of the user message.

One of the following:

str

The text contents of the message.

List[[ChatCompletionContentPart](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]

An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text, image, or audio inputs.

One of the following:

class ChatCompletionContentPartText: …

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: str

The text content.

type: Literal["text"]

The type of the content part.

class ChatCompletionContentPartImage: …

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL

url: str

Either a URL of the image or the base64 encoded image data.

formaturi

detail: Optional[Literal["auto", "low", "high"]]

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

"auto"

"low"

"high"

type: Literal["image\_url"]

The type of the content part.

class ChatCompletionContentPartInputAudio: …

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

input\_audio: InputAudio

data: str

Base64 encoded audio data.

format: Literal["wav", "mp3"]

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

"wav"

"mp3"

type: Literal["input\_audio"]

The type of the content part. Always `input_audio`.

class File: …

Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.

file: FileFile

file\_data: Optional[str]

The base64 encoded file data, used when passing the file to the model
as a string.

file\_id: Optional[str]

The ID of an uploaded file to use as input.

filename: Optional[str]

The name of the file, used when passing the file to the model as a
string.

type: Literal["file"]

The type of the content part. Always `file`.

role: Literal["user"]

The role of the messages author, in this case `user`.

name: Optional[str]

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionAssistantMessageParam: …

Messages sent by the model in response to user messages.

role: Literal["assistant"]

The role of the messages author, in this case `assistant`.

audio: Optional[Audio]

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

id: str

Unique identifier for a previous audio response from the model.

content: Optional[Union[str, List[ContentArrayOfContentPart], null]]

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

str

The contents of the assistant message.

List[ContentArrayOfContentPart]

An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.

One of the following:

class ChatCompletionContentPartText: …

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: str

The text content.

type: Literal["text"]

The type of the content part.

class ChatCompletionContentPartRefusal: …

refusal: str

The refusal message generated by the model.

type: Literal["refusal"]

The type of the content part.

Deprecatedfunction\_call: Optional[FunctionCall]

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: str

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: str

The name of the function to call.

name: Optional[str]

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

refusal: Optional[str]

The refusal message by the assistant.

tool\_calls: Optional[List[[ChatCompletionMessageToolCallUnion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))]]

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall: …

A call to a function tool created by the model.

id: str

The ID of the tool call.

function: Function

The function that the model called.

arguments: str

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: str

The name of the function to call.

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall: …

A call to a custom tool created by the model.

id: str

The ID of the tool call.

custom: Custom

The custom tool that the model called.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool to call.

type: Literal["custom"]

The type of the tool. Always `custom`.

class ChatCompletionToolMessageParam: …

content: Union[str, List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]]

The contents of the tool message.

One of the following:

str

The contents of the tool message.

List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]

An array of content parts with a defined type. For tool messages, only type `text` is supported.

text: str

The text content.

type: Literal["text"]

The type of the content part.

role: Literal["tool"]

The role of the messages author, in this case `tool`.

tool\_call\_id: str

Tool call that this message is responding to.

class ChatCompletionFunctionMessageParam: …

content: Optional[str]

The contents of the function message.

name: str

The name of the function to call.

role: Literal["function"]

The role of the messages author, in this case `function`.

model: Union[str, [ChatModel](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema))]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

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

audio: Optional[ChatCompletionAudioParam]

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

format: Literal["wav", "aac", "mp3", 3 more]

Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.

One of the following:

"wav"

"aac"

"mp3"

"flac"

"opus"

"pcm16"

voice: Voice

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
`sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

One of the following:

str

Literal["alloy", "ash", "ballad", 7 more]

One of the following:

"alloy"

"ash"

"ballad"

"coral"

"echo"

"sage"

"shimmer"

"verse"

"marin"

"cedar"

class VoiceID: …

Custom voice reference.

id: str

The custom voice ID, e.g. `voice_1234`.

frequency\_penalty: Optional[float]

Number between -2.0 and 2.0. Positive values penalize new tokens based on
their existing frequency in the text so far, decreasing the model’s
likelihood to repeat the same line verbatim.

minimum-2

maximum2

Deprecatedfunction\_call: Optional[[FunctionCall](/api/reference/python/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20function_call%20%3E%20(schema))]

Deprecated in favor of `tool_choice`.

Controls which (if any) function is called by the model.

`none` means the model will not call a function and instead generates a
message.

`auto` means the model can pick between generating a message or calling a
function.

Specifying a particular function via `{"name": "my_function"}` forces the
model to call that function.

`none` is the default when no functions are present. `auto` is the default
if functions are present.

One of the following:

Literal["none", "auto"]

`none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.

One of the following:

"none"

"auto"

class ChatCompletionFunctionCallOption: …

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

name: str

The name of the function to call.

Deprecatedfunctions: Optional[Iterable[Function]]

Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

name: str

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

description: Optional[str]

A description of what the function does, used by the model to choose when and how to call the function.

parameters: Optional[[FunctionParameters](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))]

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

logit\_bias: Optional[Dict[str, int]]

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the
tokenizer) to an associated bias value from -100 to 100. Mathematically,
the bias is added to the logits generated by the model prior to sampling.
The exact effect will vary per model, but values between -1 and 1 should
decrease or increase likelihood of selection; values like -100 or 100
should result in a ban or exclusive selection of the relevant token.

logprobs: Optional[bool]

Whether to return log probabilities of the output tokens or not. If true,
returns the log probabilities of each output token returned in the
`content` of `message`.

max\_completion\_tokens: Optional[int]

An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

Deprecatedmax\_tokens: Optional[int]

The maximum number of [tokens](/tokenizer) that can be generated in the
chat completion. This value can be used to control
[costs](https://openai.com/api/pricing/) for text generated via API.

This value is now deprecated in favor of `max_completion_tokens`, and is
not compatible with [o-series models](https://platform.openai.com/docs/guides/reasoning).

metadata: Optional[Metadata]

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

modalities: Optional[List[Literal["text", "audio"]]]

Output types that you would like the model to generate.
Most models are capable of generating text, which is the default:

`["text"]`

The `gpt-4o-audio-preview` model can also be used to
[generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate
both text and audio responses, you can use:

`["text", "audio"]`

One of the following:

"text"

"audio"

moderation: Optional[[Moderation](/api/reference/python/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20moderation%20%3E%20(schema))]

Configuration for running moderation on the request input and generated output.

model: str

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

n: Optional[int]

How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

minimum1

maximum128

parallel\_tool\_calls: Optional[[bool](/api/reference/python/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20parallel_tool_calls%20%3E%20(schema))]

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

prediction: Optional[ChatCompletionPredictionContentParam]

Static predicted output content, such as the content of a text file that is
being regenerated.

content: Union[str, List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]]

The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.

One of the following:

str

The content used for a Predicted Output. This is often the
text of a file you are regenerating with minor changes.

List[[ChatCompletionContentPartText](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))]

An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text inputs.

text: str

The text content.

type: Literal["text"]

The type of the content part.

type: Literal["content"]

The type of the predicted content you want to provide. This type is
currently always `content`.

presence\_penalty: Optional[float]

Number between -2.0 and 2.0. Positive values penalize new tokens based on
whether they appear in the text so far, increasing the model’s likelihood
to talk about new topics.

minimum-2

maximum2

prompt\_cache\_key: Optional[str]

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

prompt\_cache\_retention: Optional[Literal["in\_memory", "24h"]]

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

One of the following:

"in\_memory"

"24h"

reasoning\_effort: Optional[ReasoningEffort]

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

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

response\_format: Optional[[ResponseFormat](/api/reference/python/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema))]

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

One of the following:

class ResponseFormatText: …

Default response format. Used to generate text responses.

type: Literal["text"]

The type of response format being defined. Always `text`.

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

class ResponseFormatJSONObject: …

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: Literal["json\_object"]

The type of response format being defined. Always `json_object`.

safety\_identifier: Optional[str]

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

Deprecatedseed: Optional[int]

This feature is in Beta.
If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

minimum-9223372036854776000

maximum9223372036854776000

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

"auto"

"default"

"flex"

"scale"

"priority"

stop: Optional[Union[Optional[str], Sequence[str], null]]

Not supported with latest reasoning models `o3` and `o4-mini`.

Up to 4 sequences where the API will stop generating further tokens. The
returned text will not contain the stop sequence.

One of the following:

Optional[str]

Sequence[str]

store: Optional[bool]

Whether or not to store the output of this chat completion request for
use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or
[evals](https://platform.openai.com/docs/guides/evals) products.

Supports text and image inputs. Note: image inputs over 8MB will be dropped.

stream: Optional[Literal[false]]

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](https://platform.openai.com/docs/api-reference/chat/streaming)
for more information, along with the [streaming responses](https://platform.openai.com/docs/guides/streaming-responses)
guide for more information on how to handle the streaming events.

stream\_options: Optional[ChatCompletionStreamOptionsParam]

Options for streaming response. Only set this when you set `stream: true`.

include\_obfuscation: Optional[bool]

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

include\_usage: Optional[bool]

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

temperature: Optional[float]

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: Optional[[ChatCompletionToolChoiceOptionParam](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema))]

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

One of the following:

Literal["none", "auto", "required"]

`none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools.

One of the following:

"none"

"auto"

"required"

class ChatCompletionAllowedToolChoice: …

Constrains the tools available to the model to a pre-defined set.

allowed\_tools: [ChatCompletionAllowedTools](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema))

Constrains the tools available to the model to a pre-defined set.

mode: Literal["auto", "required"]

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

"auto"

"required"

tools: List[Dict[str, object]]

A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

[
  { "type": "function", "function": { "name": "get_weather" } },
  { "type": "function", "function": { "name": "get_time" } }
]

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

class ChatCompletionNamedToolChoice: …

Specifies a tool the model should use. Use to force the model to call a specific function.

function: Function

name: str

The name of the function to call.

type: Literal["function"]

For function calling, the type is always `function`.

class ChatCompletionNamedToolChoiceCustom: …

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom: Custom

name: str

The name of the custom tool to call.

type: Literal["custom"]

For custom tool calling, the type is always `custom`.

tools: Optional[Iterable[[ChatCompletionToolUnionParam](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool%20%3E%20(schema))]]

A list of tools the model may call. You can provide either
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools) or
[function tools](https://platform.openai.com/docs/guides/function-calling).

One of the following:

class ChatCompletionFunctionTool: …

A function tool that can be used to generate a response.

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

The type of the tool. Currently, only `function` is supported.

class ChatCompletionCustomTool: …

A custom tool that processes input using a specified format.

custom: Custom

Properties of the custom tool.

name: str

The name of the custom tool, used to identify it in tool calls.

description: Optional[str]

Optional description of the custom tool, used to provide more context.

format: Optional[CustomFormat]

The input format for the custom tool. Default is unconstrained text.

One of the following:

class CustomFormatText: …

Unconstrained free-form text.

type: Literal["text"]

Unconstrained text format. Always `text`.

class CustomFormatGrammar: …

A grammar defined by the user.

grammar: CustomFormatGrammarGrammar

Your chosen grammar.

definition: str

The grammar definition.

syntax: Literal["lark", "regex"]

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

"lark"

"regex"

type: Literal["grammar"]

Grammar format. Always `grammar`.

type: Literal["custom"]

The type of the custom tool. Always `custom`.

top\_logprobs: Optional[int]

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.
`logprobs` must be set to `true` if this parameter is used.

minimum0

maximum20

top\_p: Optional[float]

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Deprecateduser: Optional[str]

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

verbosity: Optional[Literal["low", "medium", "high"]]

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

One of the following:

"low"

"medium"

"high"

web\_search\_options: Optional[[WebSearchOptions](/api/reference/python/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20web_search_options%20%3E%20(schema))]

This tool searches the web for relevant results to use in a response.
Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

search\_context\_size: Optional[Literal["low", "medium", "high"]]

High level guidance for the amount of context window space to use for the
search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

"low"

"medium"

"high"

user\_location: Optional[WebSearchOptionsUserLocation]

Approximate location parameters for the search.

approximate: WebSearchOptionsUserLocationApproximate

Approximate location parameters for the search.

city: Optional[str]

Free text input for the city of the user, e.g. `San Francisco`.

country: Optional[str]

The two-letter
[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user,
e.g. `US`.

region: Optional[str]

Free text input for the region of the user, e.g. `California`.

timezone: Optional[str]

The [IANA timezone](https://timeapi.io/documentation/iana-timezones)
of the user, e.g. `America/Los_Angeles`.

type: Literal["approximate"]

The type of location approximation. Always `approximate`.

##### ReturnsExpand Collapse

class ChatCompletion: …

Represents a chat completion response returned by model, based on the provided input.

id: str

A unique identifier for the chat completion.

choices: List[Choice]

A list of chat completion choices. Can be more than one if `n` is greater than 1.

finish\_reason: Literal["stop", "length", "tool\_calls", 2 more]

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

One of the following:

"stop"

"length"

"tool\_calls"

"content\_filter"

"function\_call"

index: int

The index of the choice in the list of choices.

logprobs: Optional[ChoiceLogprobs]

Log probability information for the choice.

content: Optional[List[[ChatCompletionTokenLogprob](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))]]

A list of message content tokens with log probability information.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: List[TopLogprob]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

refusal: Optional[List[[ChatCompletionTokenLogprob](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))]]

A list of message refusal tokens with log probability information.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: List[TopLogprob]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

message: [ChatCompletionMessage](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema))

A chat completion message generated by the model.

content: Optional[str]

The contents of the message.

refusal: Optional[str]

The refusal message generated by the model.

role: Literal["assistant"]

The role of the author of this message.

annotations: Optional[List[Annotation]]

Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

type: Literal["url\_citation"]

The type of the URL citation. Always `url_citation`.

url\_citation: AnnotationURLCitation

A URL citation when using web search.

end\_index: int

The index of the last character of the URL citation in the message.

start\_index: int

The index of the first character of the URL citation in the message.

title: str

The title of the web resource.

url: str

The URL of the web resource.

formaturi

audio: Optional[ChatCompletionAudio]

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

id: str

Unique identifier for this audio response.

data: str

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

expires\_at: int

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

formatunixtime

transcript: str

Transcript of the audio generated by the model.

Deprecatedfunction\_call: Optional[FunctionCall]

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: str

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: str

The name of the function to call.

tool\_calls: Optional[List[[ChatCompletionMessageToolCallUnion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))]]

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall: …

A call to a function tool created by the model.

id: str

The ID of the tool call.

function: Function

The function that the model called.

arguments: str

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: str

The name of the function to call.

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall: …

A call to a custom tool created by the model.

id: str

The ID of the tool call.

custom: Custom

The custom tool that the model called.

input: str

The input for the custom tool call generated by the model.

name: str

The name of the custom tool to call.

type: Literal["custom"]

The type of the tool. Always `custom`.

created: int

The Unix timestamp (in seconds) of when the chat completion was created.

formatunixtime

model: str

The model used for the chat completion.

object: Literal["chat.completion"]

The object type, which is always `chat.completion`.

moderation: Optional[Moderation]

Moderation results for the request input and generated output, if moderated
completions were requested.

input: ModerationInput

Moderation for the request input.

One of the following:

class ModerationInputModerationResults: …

Successful moderation results for the request input or generated output.

model: str

The moderation model used to generate the results.

results: List[ModerationInputModerationResultsResult]

A list of moderation results.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

type: Literal["moderation\_results"]

The object type, which is always `moderation_results`.

class ModerationInputError: …

An error produced while attempting moderation.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which is always `error`.

output: ModerationOutput

Moderation for the generated output.

One of the following:

class ModerationOutputModerationResults: …

Successful moderation results for the request input or generated output.

model: str

The moderation model used to generate the results.

results: List[ModerationOutputModerationResultsResult]

A list of moderation results.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

type: Literal["moderation\_results"]

The object type, which is always `moderation_results`.

class ModerationOutputError: …

An error produced while attempting moderation.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which is always `error`.

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

"auto"

"default"

"flex"

"scale"

"priority"

Deprecatedsystem\_fingerprint: Optional[str]

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

usage: Optional[CompletionUsage]

Usage statistics for the completion request.

completion\_tokens: int

Number of tokens in the generated completion.

prompt\_tokens: int

Number of tokens in the prompt.

total\_tokens: int

Total number of tokens used in the request (prompt + completion).

completion\_tokens\_details: Optional[CompletionTokensDetails]

Breakdown of tokens used in a completion.

accepted\_prediction\_tokens: Optional[int]

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

audio\_tokens: Optional[int]

Audio input tokens generated by the model.

reasoning\_tokens: Optional[int]

Tokens generated by the model for reasoning.

rejected\_prediction\_tokens: Optional[int]

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

prompt\_tokens\_details: Optional[PromptTokensDetails]

Breakdown of tokens used in the prompt.

audio\_tokens: Optional[int]

Audio input tokens present in the prompt.

cached\_tokens: Optional[int]

Cached tokens present in the prompt.

class ChatCompletionChunk: …

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](https://platform.openai.com/docs/guides/streaming-responses).

id: str

A unique identifier for the chat completion. Each chunk has the same ID.

choices: List[Choice]

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

delta: ChoiceDelta

A chat completion delta generated by streamed model responses.

content: Optional[str]

The contents of the chunk message.

Deprecatedfunction\_call: Optional[ChoiceDeltaFunctionCall]

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: Optional[str]

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: Optional[str]

The name of the function to call.

refusal: Optional[str]

The refusal message generated by the model.

role: Optional[Literal["developer", "system", "user", 2 more]]

The role of the author of this message.

One of the following:

"developer"

"system"

"user"

"assistant"

"tool"

tool\_calls: Optional[List[ChoiceDeltaToolCall]]

index: int

id: Optional[str]

The ID of the tool call.

function: Optional[ChoiceDeltaToolCallFunction]

arguments: Optional[str]

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: Optional[str]

The name of the function to call.

type: Optional[Literal["function"]]

The type of the tool. Currently, only `function` is supported.

finish\_reason: Optional[Literal["stop", "length", "tool\_calls", 2 more]]

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

One of the following:

"stop"

"length"

"tool\_calls"

"content\_filter"

"function\_call"

index: int

The index of the choice in the list of choices.

logprobs: Optional[ChoiceLogprobs]

Log probability information for the choice.

content: Optional[List[[ChatCompletionTokenLogprob](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))]]

A list of message content tokens with log probability information.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: List[TopLogprob]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

refusal: Optional[List[[ChatCompletionTokenLogprob](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))]]

A list of message refusal tokens with log probability information.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: List[TopLogprob]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: str

The token.

bytes: Optional[List[int]]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

created: int

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

formatunixtime

model: str

The model to generate the completion.

object: Literal["chat.completion.chunk"]

The object type, which is always `chat.completion.chunk`.

moderation: Optional[Moderation]

Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.

input: ModerationInput

Moderation for the request input.

One of the following:

class ModerationInputModerationResults: …

Successful moderation results for the request input or generated output.

model: str

The moderation model used to generate the results.

results: List[ModerationInputModerationResultsResult]

A list of moderation results.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

type: Literal["moderation\_results"]

The object type, which is always `moderation_results`.

class ModerationInputError: …

An error produced while attempting moderation.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which is always `error`.

output: ModerationOutput

Moderation for the generated output.

One of the following:

class ModerationOutputModerationResults: …

Successful moderation results for the request input or generated output.

model: str

The moderation model used to generate the results.

results: List[ModerationOutputModerationResultsResult]

A list of moderation results.

categories: Dict[str, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Dict[str, List[Literal["text", "image"]]]

Which modalities of input are reflected by the score for each category.

One of the following:

"text"

"image"

category\_scores: Dict[str, float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: str

The moderation model that produced this result.

type: Literal["moderation\_result"]

The object type, which was always `moderation_result` for successful moderation results.

type: Literal["moderation\_results"]

The object type, which is always `moderation_results`.

class ModerationOutputError: …

An error produced while attempting moderation.

code: str

The error code.

message: str

The error message.

type: Literal["error"]

The object type, which is always `error`.

service\_tier: Optional[Literal["auto", "default", "flex", 2 more]]

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

"auto"

"default"

"flex"

"scale"

"priority"

Deprecatedsystem\_fingerprint: Optional[str]

This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

usage: Optional[CompletionUsage]

An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the
token usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

completion\_tokens: int

Number of tokens in the generated completion.

prompt\_tokens: int

Number of tokens in the prompt.

total\_tokens: int

Total number of tokens used in the request (prompt + completion).

completion\_tokens\_details: Optional[CompletionTokensDetails]

Breakdown of tokens used in a completion.

accepted\_prediction\_tokens: Optional[int]

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

audio\_tokens: Optional[int]

Audio input tokens generated by the model.

reasoning\_tokens: Optional[int]

Tokens generated by the model for reasoning.

rejected\_prediction\_tokens: Optional[int]

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

prompt\_tokens\_details: Optional[PromptTokensDetails]

Breakdown of tokens used in the prompt.

audio\_tokens: Optional[int]

Audio input tokens present in the prompt.

cached\_tokens: Optional[int]

Cached tokens present in the prompt.

DefaultImage inputStreamingFunctionsLogprobs

### Create chat completion

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

completion = client.chat.completions.create(
  model="VAR_chat_model_id",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]

print(completion.choices[0].message)

  "id": "chatcmpl-B9MBs8CjcvOU2jLn4n570S5qMJKcT",
  "object": "chat.completion",
  "created": 1741569952,
  "model": "gpt-5.4",
  "choices": [
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": null,
        "annotations": []
      "logprobs": null,
      "finish_reason": "stop"
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 10,
    "total_tokens": 29,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
  "service_tier": "default"

### Create chat completion

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

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            ],
    ],
    max_tokens=300,

print(response.choices[0])

  "id": "chatcmpl-B9MHDbslfkBeAs8l4bebGdFOJ6PeG",
  "object": "chat.completion",
  "created": 1741570283,
  "model": "gpt-5.4",
  "choices": [
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The image shows a wooden boardwalk path running through a lush green field or meadow. The sky is bright blue with some scattered clouds, giving the scene a serene and peaceful atmosphere. Trees and shrubs are visible in the background.",
        "refusal": null,
        "annotations": []
      "logprobs": null,
      "finish_reason": "stop"
  ],
  "usage": {
    "prompt_tokens": 1117,
    "completion_tokens": 46,
    "total_tokens": 1163,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
  "service_tier": "default"

### Create chat completion

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

completion = client.chat.completions.create(
  model="VAR_chat_model_id",
  messages=[
    {"role": "developer", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  stream=True

for chunk in completion:
  print(chunk.choices[0].delta)

{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"role":"assistant","content":""},"logprobs":null,"finish_reason":null}]}

{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{"content":"Hello"},"logprobs":null,"finish_reason":null}]}

....

{"id":"chatcmpl-123","object":"chat.completion.chunk","created":1694268190,"model":"gpt-4o-mini", "system_fingerprint": "fp_44709d6fcb", "choices":[{"index":0,"delta":{},"logprobs":null,"finish_reason":"stop"}]}

### Create chat completion

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
messages = [{"role": "user", "content": "What's the weather like in Boston today?"}]
completion = client.chat.completions.create(
  model="VAR_chat_model_id",
  messages=messages,
  tools=tools,
  tool_choice="auto"

print(completion)

  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1699896916,
  "model": "gpt-4o-mini",
  "choices": [
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": [
            "id": "call_abc123",
            "type": "function",
            "function": {
              "name": "get_current_weather",
              "arguments": "{\n\"location\": \"Boston, MA\"\n}"
        ]
      "logprobs": null,
      "finish_reason": "tool_calls"
  ],
  "usage": {
    "prompt_tokens": 82,
    "completion_tokens": 17,
    "total_tokens": 99,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0

### Create chat completion

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

completion = client.chat.completions.create(
  model="VAR_chat_model_id",
  messages=[
    {"role": "user", "content": "Hello!"}
  ],
  logprobs=True,
  top_logprobs=2

print(completion.choices[0].message)
print(completion.choices[0].logprobs)

  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1702685778,
  "model": "gpt-4o-mini",
  "choices": [
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?"
      "logprobs": {
        "content": [
            "token": "Hello",
            "logprob": -0.31725305,
            "bytes": [72, 101, 108, 108, 111],
            "top_logprobs": [
                "token": "Hello",
                "logprob": -0.31725305,
                "bytes": [72, 101, 108, 108, 111]
                "token": "Hi",
                "logprob": -1.3190403,
                "bytes": [72, 105]
            ]
            "token": "!",
            "logprob": -0.02380986,
            "bytes": [
              33
            ],
            "top_logprobs": [
                "token": "!",
                "logprob": -0.02380986,
                "bytes": [33]
                "token": " there",
                "logprob": -3.787621,
                "bytes": [32, 116, 104, 101, 114, 101]
            ]
            "token": " How",
            "logprob": -0.000054669687,
            "bytes": [32, 72, 111, 119],
            "top_logprobs": [
                "token": " How",
                "logprob": -0.000054669687,
                "bytes": [32, 72, 111, 119]
                "token": "<|end|>",
                "logprob": -10.953937,
                "bytes": null
            ]
            "token": " can",
            "logprob": -0.015801601,
            "bytes": [32, 99, 97, 110],
            "top_logprobs": [
                "token": " can",
                "logprob": -0.015801601,
                "bytes": [32, 99, 97, 110]
                "token": " may",
                "logprob": -4.161023,
                "bytes": [32, 109, 97, 121]
            ]
            "token": " I",
            "logprob": -3.7697225e-6,
            "bytes": [
              32,
              73
            ],
            "top_logprobs": [
                "token": " I",
                "logprob": -3.7697225e-6,
                "bytes": [32, 73]
                "token": " assist",
                "logprob": -13.596657,
                "bytes": [32, 97, 115, 115, 105, 115, 116]
            ]
            "token": " assist",
            "logprob": -0.04571125,
            "bytes": [32, 97, 115, 115, 105, 115, 116],
            "top_logprobs": [
                "token": " assist",
                "logprob": -0.04571125,
                "bytes": [32, 97, 115, 115, 105, 115, 116]
                "token": " help",
                "logprob": -3.1089056,
                "bytes": [32, 104, 101, 108, 112]
            ]
            "token": " you",
            "logprob": -5.4385737e-6,
            "bytes": [32, 121, 111, 117],
            "top_logprobs": [
                "token": " you",
                "logprob": -5.4385737e-6,
                "bytes": [32, 121, 111, 117]
                "token": " today",
                "logprob": -12.807695,
                "bytes": [32, 116, 111, 100, 97, 121]
            ]
            "token": " today",
            "logprob": -0.0040071653,
            "bytes": [32, 116, 111, 100, 97, 121],
            "top_logprobs": [
                "token": " today",
                "logprob": -0.0040071653,
                "bytes": [32, 116, 111, 100, 97, 121]
                "token": "?",
                "logprob": -5.5247097,
                "bytes": [63]
            ]
            "token": "?",
            "logprob": -0.0008108172,
            "bytes": [63],
            "top_logprobs": [
                "token": "?",
                "logprob": -0.0008108172,
                "bytes": [63]
                "token": "?\n",
                "logprob": -7.184561,
                "bytes": [63, 10]
            ]
        ]
      "finish_reason": "stop"
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 9,
    "total_tokens": 18,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
  "system_fingerprint": null

##### Returns Examples

  "id": "chatcmpl-B9MBs8CjcvOU2jLn4n570S5qMJKcT",
  "object": "chat.completion",
  "created": 1741569952,
  "model": "gpt-5.4",
  "choices": [
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Hello! How can I assist you today?",
        "refusal": null,
        "annotations": []
      "logprobs": null,
      "finish_reason": "stop"
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 10,
    "total_tokens": 29,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "audio_tokens": 0
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "audio_tokens": 0,
      "accepted_prediction_tokens": 0,
      "rejected_prediction_tokens": 0
  "service_tier": "default"
