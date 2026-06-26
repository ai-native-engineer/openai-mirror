<!-- source: https://developers.openai.com/api/reference/ruby/resources/chat/subresources/completions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/ruby)

[Chat](/api/reference/ruby/resources/chat)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Completions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](/api/reference/ruby/resources/chat/subresources/completions/methods/create)

chat.completions.create(\*\*kwargs) -> [ChatCompletion](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) { id, choices, created, 6 more }

POST/chat/completions

##### [List Chat Completions](/api/reference/ruby/resources/chat/subresources/completions/methods/list)

chat.completions.list(\*\*kwargs) -> CursorPage<[ChatCompletion](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) { id, choices, created, 6 more } >

GET/chat/completions

##### [Get chat completion](/api/reference/ruby/resources/chat/subresources/completions/methods/retrieve)

chat.completions.retrieve(completion\_id) -> [ChatCompletion](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) { id, choices, created, 6 more }

GET/chat/completions/{completion\_id}

##### [Update chat completion](/api/reference/ruby/resources/chat/subresources/completions/methods/update)

chat.completions.update(completion\_id, \*\*kwargs) -> [ChatCompletion](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) { id, choices, created, 6 more }

POST/chat/completions/{completion\_id}

##### [Delete chat completion](/api/reference/ruby/resources/chat/subresources/completions/methods/delete)

chat.completions.delete(completion\_id) -> [ChatCompletionDeleted](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)) { id, deleted, object }

DELETE/chat/completions/{completion\_id}

##### ModelsExpand Collapse

class ChatCompletion { id, choices, created, 6 more }

Represents a chat completion response returned by model, based on the provided input.

id: String

A unique identifier for the chat completion.

choices: Array[Choice{ finish\_reason, index, logprobs, message}]

A list of chat completion choices. Can be more than one if `n` is greater than 1.

finish\_reason: :stop | :length | :tool\_calls | 2 more

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

One of the following:

:stop

:length

:tool\_calls

:content\_filter

:function\_call

index: Integer

The index of the choice in the list of choices.

logprobs: Logprobs{ content, refusal}

Log probability information for the choice.

content: Array[[ChatCompletionTokenLogprob](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs } ]

A list of message content tokens with log probability information.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

refusal: Array[[ChatCompletionTokenLogprob](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs } ]

A list of message refusal tokens with log probability information.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

message: [ChatCompletionMessage](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)) { content, refusal, role, 4 more }

A chat completion message generated by the model.

created: Integer

The Unix timestamp (in seconds) of when the chat completion was created.

formatunixtime

model: String

The model used for the chat completion.

object: :"chat.completion"

The object type, which is always `chat.completion`.

moderation: Moderation{ input, output}

Moderation results for the request input and generated output, if moderated
completions were requested.

input: ModerationResults{ model, results, type} | Error{ code, message, type}

Moderation for the request input.

One of the following:

class ModerationResults { model, results, type }

Successful moderation results for the request input or generated output.

model: String

The moderation model used to generate the results.

results: Array[Result{ categories, category\_applied\_input\_types, category\_scores, 3 more}]

A list of moderation results.

categories: Hash[Symbol, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Hash[Symbol, Array[:text | :image]]

Which modalities of input are reflected by the score for each category.

One of the following:

:text

:image

category\_scores: Hash[Symbol, Float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: String

The moderation model that produced this result.

type: :moderation\_result

The object type, which was always `moderation_result` for successful moderation results.

type: :moderation\_results

The object type, which is always `moderation_results`.

class Error { code, message, type }

An error produced while attempting moderation.

code: String

The error code.

message: String

The error message.

type: :error

The object type, which is always `error`.

output: ModerationResults{ model, results, type} | Error{ code, message, type}

Moderation for the generated output.

One of the following:

class ModerationResults { model, results, type }

Successful moderation results for the request input or generated output.

model: String

The moderation model used to generate the results.

results: Array[Result{ categories, category\_applied\_input\_types, category\_scores, 3 more}]

A list of moderation results.

categories: Hash[Symbol, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Hash[Symbol, Array[:text | :image]]

Which modalities of input are reflected by the score for each category.

One of the following:

:text

:image

category\_scores: Hash[Symbol, Float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: String

The moderation model that produced this result.

type: :moderation\_result

The object type, which was always `moderation_result` for successful moderation results.

type: :moderation\_results

The object type, which is always `moderation_results`.

class Error { code, message, type }

An error produced while attempting moderation.

code: String

The error code.

message: String

The error message.

type: :error

The object type, which is always `error`.

service\_tier: :auto | :default | :flex | 2 more

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

:auto

:default

:flex

:scale

:priority

Deprecatedsystem\_fingerprint: String

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

usage: [CompletionUsage](/api/reference/ruby/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)) { completion\_tokens, prompt\_tokens, total\_tokens, 2 more }

Usage statistics for the completion request.

class ChatCompletionAllowedToolChoice { allowed\_tools, type }

Constrains the tools available to the model to a pre-defined set.

allowed\_tools: [ChatCompletionAllowedTools](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) { mode, tools }

Constrains the tools available to the model to a pre-defined set.

type: :allowed\_tools

Allowed tool configuration type. Always `allowed_tools`.

class ChatCompletionAssistantMessageParam { role, audio, content, 4 more }

Messages sent by the model in response to user messages.

role: :assistant

The role of the messages author, in this case `assistant`.

audio: Audio{ id}

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

id: String

Unique identifier for a previous audio response from the model.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartRefusal](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal, type } ]

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

String = String

The contents of the assistant message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartRefusal](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal, type } ]

An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartRefusal { refusal, type }

refusal: String

The refusal message generated by the model.

type: :refusal

The type of the content part.

Deprecatedfunction\_call: FunctionCall{ arguments, name}

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

refusal: String

The refusal message by the assistant.

tool\_calls: Array[[ChatCompletionMessageToolCall](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))]

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall { id, function, type }

A call to a function tool created by the model.

id: String

The ID of the tool call.

function: Function{ arguments, name}

The function that the model called.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall { id, custom, type }

A call to a custom tool created by the model.

id: String

The ID of the tool call.

custom: Custom{ input, name}

The custom tool that the model called.

input: String

The input for the custom tool call generated by the model.

name: String

The name of the custom tool to call.

type: :custom

The type of the tool. Always `custom`.

class ChatCompletionAudio { id, data, expires\_at, transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

id: String

Unique identifier for this audio response.

data: String

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

expires\_at: Integer

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

formatunixtime

transcript: String

Transcript of the audio generated by the model.

class ChatCompletionAudioParam { format\_, voice }

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

format\_: :wav | :aac | :mp3 | 3 more

Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.

One of the following:

:wav

:aac

:mp3

:flac

:opus

:pcm16

voice: String | :alloy | :ash | :ballad | 7 more | ID{ id}

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
`sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

One of the following:

String = String

Voice = :alloy | :ash | :ballad | 7 more

One of the following:

:alloy

:ash

:ballad

:coral

:echo

:sage

:shimmer

:verse

:marin

:cedar

class ID { id }

Custom voice reference.

id: String

The custom voice ID, e.g. `voice_1234`.

class ChatCompletionChunk { id, choices, created, 6 more }

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](https://platform.openai.com/docs/guides/streaming-responses).

id: String

A unique identifier for the chat completion. Each chunk has the same ID.

choices: Array[Choice{ delta, finish\_reason, index, logprobs}]

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

delta: Delta{ content, function\_call, refusal, 2 more}

A chat completion delta generated by streamed model responses.

content: String

The contents of the chunk message.

Deprecatedfunction\_call: FunctionCall{ arguments, name}

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

refusal: String

The refusal message generated by the model.

role: :developer | :system | :user | 2 more

The role of the author of this message.

One of the following:

:developer

:system

:user

:assistant

:tool

tool\_calls: Array[ToolCall{ index, id, function, type}]

index: Integer

id: String

The ID of the tool call.

function: Function{ arguments, name}

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

finish\_reason: :stop | :length | :tool\_calls | 2 more

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

One of the following:

:stop

:length

:tool\_calls

:content\_filter

:function\_call

index: Integer

The index of the choice in the list of choices.

logprobs: Logprobs{ content, refusal}

Log probability information for the choice.

content: Array[[ChatCompletionTokenLogprob](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs } ]

A list of message content tokens with log probability information.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

refusal: Array[[ChatCompletionTokenLogprob](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs } ]

A list of message refusal tokens with log probability information.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

created: Integer

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

formatunixtime

model: String

The model to generate the completion.

object: :"chat.completion.chunk"

The object type, which is always `chat.completion.chunk`.

moderation: Moderation{ input, output}

Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.

input: ModerationResults{ model, results, type} | Error{ code, message, type}

Moderation for the request input.

One of the following:

class ModerationResults { model, results, type }

Successful moderation results for the request input or generated output.

model: String

The moderation model used to generate the results.

results: Array[Result{ categories, category\_applied\_input\_types, category\_scores, 3 more}]

A list of moderation results.

categories: Hash[Symbol, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Hash[Symbol, Array[:text | :image]]

Which modalities of input are reflected by the score for each category.

One of the following:

:text

:image

category\_scores: Hash[Symbol, Float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: String

The moderation model that produced this result.

type: :moderation\_result

The object type, which was always `moderation_result` for successful moderation results.

type: :moderation\_results

The object type, which is always `moderation_results`.

class Error { code, message, type }

An error produced while attempting moderation.

code: String

The error code.

message: String

The error message.

type: :error

The object type, which is always `error`.

output: ModerationResults{ model, results, type} | Error{ code, message, type}

Moderation for the generated output.

One of the following:

class ModerationResults { model, results, type }

Successful moderation results for the request input or generated output.

model: String

The moderation model used to generate the results.

results: Array[Result{ categories, category\_applied\_input\_types, category\_scores, 3 more}]

A list of moderation results.

categories: Hash[Symbol, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: Hash[Symbol, Array[:text | :image]]

Which modalities of input are reflected by the score for each category.

One of the following:

:text

:image

category\_scores: Hash[Symbol, Float]

A dictionary of moderation categories to scores.

flagged: bool

A boolean indicating whether the content was flagged by any category.

model: String

The moderation model that produced this result.

type: :moderation\_result

The object type, which was always `moderation_result` for successful moderation results.

type: :moderation\_results

The object type, which is always `moderation_results`.

class Error { code, message, type }

An error produced while attempting moderation.

code: String

The error code.

message: String

The error message.

type: :error

The object type, which is always `error`.

service\_tier: :auto | :default | :flex | 2 more

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

:auto

:default

:flex

:scale

:priority

Deprecatedsystem\_fingerprint: String

This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

usage: [CompletionUsage](/api/reference/ruby/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema)) { completion\_tokens, prompt\_tokens, total\_tokens, 2 more }

An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the
token usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

ChatCompletionContentPart = [ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartImage](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image\_url, type }  | [ChatCompletionContentPartInputAudio](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_input_audio%20%3E%20(schema)) { input\_audio, type }  | File{ file, type}

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartImage { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL{ url, detail}

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class ChatCompletionContentPartInputAudio { input\_audio, type }

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

input\_audio: InputAudio{ data, format\_}

data: String

Base64 encoded audio data.

format\_: :wav | :mp3

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

:wav

:mp3

type: :input\_audio

The type of the content part. Always `input_audio`.

class File { file, type }

Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.

file: File{ file\_data, file\_id, filename}

file\_data: String

The base64 encoded file data, used when passing the file to the model
as a string.

file\_id: String

The ID of an uploaded file to use as input.

filename: String

The name of the file, used when passing the file to the model as a
string.

type: :file

The type of the content part. Always `file`.

class ChatCompletionContentPartImage { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL{ url, detail}

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class ChatCompletionContentPartInputAudio { input\_audio, type }

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

input\_audio: InputAudio{ data, format\_}

data: String

Base64 encoded audio data.

format\_: :wav | :mp3

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

:wav

:mp3

type: :input\_audio

The type of the content part. Always `input_audio`.

class ChatCompletionContentPartRefusal { refusal, type }

refusal: String

The refusal message generated by the model.

type: :refusal

The type of the content part.

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionCustomTool { custom, type }

A custom tool that processes input using a specified format.

custom: Custom{ name, description, format\_}

Properties of the custom tool.

name: String

The name of the custom tool, used to identify it in tool calls.

description: String

Optional description of the custom tool, used to provide more context.

format\_: Text{ type} | Grammar{ grammar, type}

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { grammar, type }

A grammar defined by the user.

grammar: Grammar{ definition, syntax}

Your chosen grammar.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

type: :custom

The type of the custom tool. Always `custom`.

class ChatCompletionDeleted { id, deleted, object }

id: String

The ID of the chat completion that was deleted.

deleted: bool

Whether the chat completion was deleted.

object: :"chat.completion.deleted"

The type of object being deleted.

class ChatCompletionDeveloperMessageParam { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the developer message.

One of the following:

String = String

The contents of the developer message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For developer messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :developer

The role of the messages author, in this case `developer`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionFunctionCallOption { name }

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

name: String

The name of the function to call.

class ChatCompletionFunctionMessageParam { content, name, role }

content: String

The contents of the function message.

name: String

The name of the function to call.

role: :function

The role of the messages author, in this case `function`.

class ChatCompletionFunctionTool { function, type }

A function tool that can be used to generate a response.

function: [FunctionDefinition](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessage { content, refusal, role, 4 more }

A chat completion message generated by the model.

content: String

The contents of the message.

refusal: String

The refusal message generated by the model.

role: :assistant

The role of the author of this message.

annotations: Array[Annotation{ type, url\_citation}]

Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

type: :url\_citation

The type of the URL citation. Always `url_citation`.

url\_citation: URLCitation{ end\_index, start\_index, title, url}

A URL citation when using web search.

end\_index: Integer

The index of the last character of the URL citation in the message.

start\_index: Integer

The index of the first character of the URL citation in the message.

title: String

The title of the web resource.

url: String

The URL of the web resource.

formaturi

audio: [ChatCompletionAudio](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema)) { id, data, expires\_at, transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

Deprecatedfunction\_call: FunctionCall{ arguments, name}

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

tool\_calls: Array[[ChatCompletionMessageToolCall](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))]

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall { id, function, type }

A call to a function tool created by the model.

id: String

The ID of the tool call.

function: Function{ arguments, name}

The function that the model called.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall { id, custom, type }

A call to a custom tool created by the model.

id: String

The ID of the tool call.

custom: Custom{ input, name}

The custom tool that the model called.

input: String

The input for the custom tool call generated by the model.

name: String

The name of the custom tool to call.

type: :custom

The type of the tool. Always `custom`.

class ChatCompletionMessageCustomToolCall { id, custom, type }

A call to a custom tool created by the model.

id: String

The ID of the tool call.

custom: Custom{ input, name}

The custom tool that the model called.

input: String

The input for the custom tool call generated by the model.

name: String

The name of the custom tool to call.

type: :custom

The type of the tool. Always `custom`.

class ChatCompletionMessageFunctionToolCall { id, function, type }

A call to a function tool created by the model.

id: String

The ID of the tool call.

function: Function{ arguments, name}

The function that the model called.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

ChatCompletionMessageParam = [ChatCompletionDeveloperMessageParam](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_developer_message_param%20%3E%20(schema)) { content, role, name }  | [ChatCompletionSystemMessageParam](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_system_message_param%20%3E%20(schema)) { content, role, name }  | [ChatCompletionUserMessageParam](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_user_message_param%20%3E%20(schema)) { content, role, name }  | 3 more

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

One of the following:

class ChatCompletionDeveloperMessageParam { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the developer message.

One of the following:

String = String

The contents of the developer message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For developer messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :developer

The role of the messages author, in this case `developer`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionSystemMessageParam { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the system message.

One of the following:

String = String

The contents of the system message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For system messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :system

The role of the messages author, in this case `system`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionUserMessageParam { content, role, name }

Messages sent by an end user, containing prompts or additional context
information.

content: String | Array[[ChatCompletionContentPart](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]

The contents of the user message.

One of the following:

String = String

The text contents of the message.

ArrayOfContentParts = Array[[ChatCompletionContentPart](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]

An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text, image, or audio inputs.

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartImage { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL{ url, detail}

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class ChatCompletionContentPartInputAudio { input\_audio, type }

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

input\_audio: InputAudio{ data, format\_}

data: String

Base64 encoded audio data.

format\_: :wav | :mp3

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

:wav

:mp3

type: :input\_audio

The type of the content part. Always `input_audio`.

class File { file, type }

Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.

file: File{ file\_data, file\_id, filename}

file\_data: String

The base64 encoded file data, used when passing the file to the model
as a string.

file\_id: String

The ID of an uploaded file to use as input.

filename: String

The name of the file, used when passing the file to the model as a
string.

type: :file

The type of the content part. Always `file`.

role: :user

The role of the messages author, in this case `user`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionAssistantMessageParam { role, audio, content, 4 more }

Messages sent by the model in response to user messages.

role: :assistant

The role of the messages author, in this case `assistant`.

audio: Audio{ id}

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

id: String

Unique identifier for a previous audio response from the model.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartRefusal](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal, type } ]

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

String = String

The contents of the assistant message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartRefusal](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_refusal%20%3E%20(schema)) { refusal, type } ]

An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartRefusal { refusal, type }

refusal: String

The refusal message generated by the model.

type: :refusal

The type of the content part.

Deprecatedfunction\_call: FunctionCall{ arguments, name}

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

refusal: String

The refusal message by the assistant.

tool\_calls: Array[[ChatCompletionMessageToolCall](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))]

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall { id, function, type }

A call to a function tool created by the model.

id: String

The ID of the tool call.

function: Function{ arguments, name}

The function that the model called.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall { id, custom, type }

A call to a custom tool created by the model.

id: String

The ID of the tool call.

custom: Custom{ input, name}

The custom tool that the model called.

input: String

The input for the custom tool call generated by the model.

name: String

The name of the custom tool to call.

type: :custom

The type of the tool. Always `custom`.

class ChatCompletionToolMessageParam { content, role, tool\_call\_id }

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the tool message.

One of the following:

String = String

The contents of the tool message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For tool messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :tool

The role of the messages author, in this case `tool`.

tool\_call\_id: String

Tool call that this message is responding to.

class ChatCompletionFunctionMessageParam { content, name, role }

content: String

The contents of the function message.

name: String

The name of the function to call.

role: :function

The role of the messages author, in this case `function`.

ChatCompletionMessageToolCall = [ChatCompletionMessageFunctionToolCall](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_function_tool_call%20%3E%20(schema)) { id, function, type }  | [ChatCompletionMessageCustomToolCall](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_custom_tool_call%20%3E%20(schema)) { id, custom, type }

A call to a function tool created by the model.

One of the following:

class ChatCompletionMessageFunctionToolCall { id, function, type }

A call to a function tool created by the model.

id: String

The ID of the tool call.

function: Function{ arguments, name}

The function that the model called.

arguments: String

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: String

The name of the function to call.

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall { id, custom, type }

A call to a custom tool created by the model.

id: String

The ID of the tool call.

custom: Custom{ input, name}

The custom tool that the model called.

input: String

The input for the custom tool call generated by the model.

name: String

The name of the custom tool to call.

type: :custom

The type of the tool. Always `custom`.

ChatCompletionModality = :text | :audio

One of the following:

:text

:audio

class ChatCompletionNamedToolChoice { function, type }

Specifies a tool the model should use. Use to force the model to call a specific function.

function: Function{ name}

name: String

The name of the function to call.

type: :function

For function calling, the type is always `function`.

class ChatCompletionNamedToolChoiceCustom { custom, type }

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom: Custom{ name}

name: String

The name of the custom tool to call.

type: :custom

For custom tool calling, the type is always `custom`.

class ChatCompletionPredictionContent { content, type }

Static predicted output content, such as the content of a text file that is
being regenerated.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.

One of the following:

String = String

The content used for a Predicted Output. This is often the
text of a file you are regenerating with minor changes.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text inputs.

text: String

The text content.

type: :text

The type of the content part.

type: :content

The type of the predicted content you want to provide. This type is
currently always `content`.

ChatCompletionRole = :developer | :system | :user | 3 more

The role of the author of a message

One of the following:

:developer

:system

:user

:assistant

:tool

:function

class ChatCompletionStoreMessage { id, content\_parts }

A chat completion message generated by the model.

id: String

The identifier of the chat message.

content\_parts: Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type }  | [ChatCompletionContentPartImage](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_image%20%3E%20(schema)) { image\_url, type } ]

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartImage { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL{ url, detail}

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class ChatCompletionStreamOptions { include\_obfuscation, include\_usage }

Options for streaming response. Only set this when you set `stream: true`.

include\_obfuscation: bool

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

include\_usage: bool

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

class ChatCompletionSystemMessageParam { content, role, name }

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the system message.

One of the following:

String = String

The contents of the system message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For system messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :system

The role of the messages author, in this case `system`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionTokenLogprob { token, bytes, logprob, top\_logprobs }

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: Array[TopLogprob{ token, bytes, logprob}]

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: String

The token.

bytes: Array[Integer]

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: Float

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

ChatCompletionTool = [ChatCompletionFunctionTool](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_function_tool%20%3E%20(schema)) { function, type }  | [ChatCompletionCustomTool](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_custom_tool%20%3E%20(schema)) { custom, type }

A function tool that can be used to generate a response.

One of the following:

class ChatCompletionFunctionTool { function, type }

A function tool that can be used to generate a response.

function: [FunctionDefinition](/api/reference/ruby/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) { name, description, parameters, strict }

type: :function

The type of the tool. Currently, only `function` is supported.

class ChatCompletionCustomTool { custom, type }

A custom tool that processes input using a specified format.

custom: Custom{ name, description, format\_}

Properties of the custom tool.

name: String

The name of the custom tool, used to identify it in tool calls.

description: String

Optional description of the custom tool, used to provide more context.

format\_: Text{ type} | Grammar{ grammar, type}

The input format for the custom tool. Default is unconstrained text.

One of the following:

class Text { type }

Unconstrained free-form text.

type: :text

Unconstrained text format. Always `text`.

class Grammar { grammar, type }

A grammar defined by the user.

grammar: Grammar{ definition, syntax}

Your chosen grammar.

definition: String

The grammar definition.

syntax: :lark | :regex

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

:lark

:regex

type: :grammar

Grammar format. Always `grammar`.

type: :custom

The type of the custom tool. Always `custom`.

ChatCompletionToolChoiceOption = :none | :auto | :required | [ChatCompletionAllowedToolChoice](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_allowed_tool_choice%20%3E%20(schema)) { allowed\_tools, type }  | [ChatCompletionNamedToolChoice](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice%20%3E%20(schema)) { function, type }  | [ChatCompletionNamedToolChoiceCustom](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_named_tool_choice_custom%20%3E%20(schema)) { custom, type }

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

One of the following:

Auto = :none | :auto | :required

`none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools.

One of the following:

:none

:auto

:required

class ChatCompletionAllowedToolChoice { allowed\_tools, type }

Constrains the tools available to the model to a pre-defined set.

allowed\_tools: [ChatCompletionAllowedTools](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) { mode, tools }

Constrains the tools available to the model to a pre-defined set.

type: :allowed\_tools

Allowed tool configuration type. Always `allowed_tools`.

class ChatCompletionNamedToolChoice { function, type }

Specifies a tool the model should use. Use to force the model to call a specific function.

function: Function{ name}

name: String

The name of the function to call.

type: :function

For function calling, the type is always `function`.

class ChatCompletionNamedToolChoiceCustom { custom, type }

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

custom: Custom{ name}

name: String

The name of the custom tool to call.

type: :custom

For custom tool calling, the type is always `custom`.

class ChatCompletionToolMessageParam { content, role, tool\_call\_id }

content: String | Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

The contents of the tool message.

One of the following:

String = String

The contents of the tool message.

ArrayOfContentParts = Array[[ChatCompletionContentPartText](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema)) { text, type } ]

An array of content parts with a defined type. For tool messages, only type `text` is supported.

text: String

The text content.

type: :text

The type of the content part.

role: :tool

The role of the messages author, in this case `tool`.

tool\_call\_id: String

Tool call that this message is responding to.

class ChatCompletionUserMessageParam { content, role, name }

Messages sent by an end user, containing prompts or additional context
information.

content: String | Array[[ChatCompletionContentPart](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]

The contents of the user message.

One of the following:

String = String

The text contents of the message.

ArrayOfContentParts = Array[[ChatCompletionContentPart](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))]

An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text, image, or audio inputs.

One of the following:

class ChatCompletionContentPartText { text, type }

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: String

The text content.

type: :text

The type of the content part.

class ChatCompletionContentPartImage { image\_url, type }

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

image\_url: ImageURL{ url, detail}

url: String

Either a URL of the image or the base64 encoded image data.

formaturi

detail: :auto | :low | :high

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

:auto

:low

:high

type: :image\_url

The type of the content part.

class ChatCompletionContentPartInputAudio { input\_audio, type }

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

input\_audio: InputAudio{ data, format\_}

data: String

Base64 encoded audio data.

format\_: :wav | :mp3

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

:wav

:mp3

type: :input\_audio

The type of the content part. Always `input_audio`.

class File { file, type }

Learn about [file inputs](https://platform.openai.com/docs/guides/text) for text generation.

file: File{ file\_data, file\_id, filename}

file\_data: String

The base64 encoded file data, used when passing the file to the model
as a string.

file\_id: String

The ID of an uploaded file to use as input.

filename: String

The name of the file, used when passing the file to the model as a
string.

type: :file

The type of the content part. Always `file`.

role: :user

The role of the messages author, in this case `user`.

name: String

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionAllowedTools { mode, tools }

Constrains the tools available to the model to a pre-defined set.

mode: :auto | :required

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

:auto

:required

tools: Array[Hash[Symbol, untyped]]

A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

[
  { "type": "function", "function": { "name": "get_weather" } },
  { "type": "function", "function": { "name": "get_time" } }
]

#### CompletionsMessages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/ruby/resources/chat/subresources/completions/subresources/messages/methods/list)

chat.completions.messages.list(completion\_id, \*\*kwargs) -> CursorPage<[ChatCompletionStoreMessage](/api/reference/ruby/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema)) { id, content\_parts } >

GET/chat/completions/{completion\_id}/messages
