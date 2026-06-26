<!-- source: https://developers.openai.com/api/reference/python/resources/chat/subresources/completions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/python)

[Chat](/api/reference/python/resources/chat)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Completions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](/api/reference/python/resources/chat/subresources/completions/methods/create)

chat.completions.create(CompletionCreateParams\*\*kwargs)  -> [ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

POST/chat/completions

##### [List Chat Completions](/api/reference/python/resources/chat/subresources/completions/methods/list)

chat.completions.list(CompletionListParams\*\*kwargs)  -> SyncCursorPage[[ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))]

GET/chat/completions

##### [Get chat completion](/api/reference/python/resources/chat/subresources/completions/methods/retrieve)

chat.completions.retrieve(strcompletion\_id)  -> [ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

GET/chat/completions/{completion\_id}

##### [Update chat completion](/api/reference/python/resources/chat/subresources/completions/methods/update)

chat.completions.update(strcompletion\_id, CompletionUpdateParams\*\*kwargs)  -> [ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))

POST/chat/completions/{completion\_id}

##### [Delete chat completion](/api/reference/python/resources/chat/subresources/completions/methods/delete)

chat.completions.delete(strcompletion\_id)  -> [ChatCompletionDeleted](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema))

DELETE/chat/completions/{completion\_id}

##### ModelsExpand Collapse

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

class ChatCompletionAllowedToolChoice: …

Constrains the tools available to the model to a pre-defined set.

allowed\_tools: [ChatCompletionAllowedTools](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema))

Constrains the tools available to the model to a pre-defined set.

type: Literal["allowed\_tools"]

Allowed tool configuration type. Always `allowed_tools`.

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

class ChatCompletionAudio: …

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

class ChatCompletionAudioParam: …

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

[ChatCompletionContentPart](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

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

class ChatCompletionContentPartRefusal: …

refusal: str

The refusal message generated by the model.

type: Literal["refusal"]

The type of the content part.

class ChatCompletionContentPartText: …

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

text: str

The text content.

type: Literal["text"]

The type of the content part.

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

class ChatCompletionDeleted: …

id: str

The ID of the chat completion that was deleted.

deleted: bool

Whether the chat completion was deleted.

object: Literal["chat.completion.deleted"]

The type of object being deleted.

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

class ChatCompletionFunctionCallOption: …

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

name: str

The name of the function to call.

class ChatCompletionFunctionMessageParam: …

content: Optional[str]

The contents of the function message.

name: str

The name of the function to call.

role: Literal["function"]

The role of the messages author, in this case `function`.

class ChatCompletionFunctionTool: …

A function tool that can be used to generate a response.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

type: Literal["function"]

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessage: …

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

[ChatCompletionMessageParam](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_param%20%3E%20(schema))

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

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

[ChatCompletionMessageToolCallUnion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

A call to a function tool created by the model.

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

Literal["text", "audio"]

One of the following:

"text"

"audio"

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

class ChatCompletionPredictionContent: …

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

Literal["developer", "system", "user", 3 more]

The role of the author of a message

One of the following:

"developer"

"system"

"user"

"assistant"

"tool"

"function"

class ChatCompletionStoreMessage: …

A chat completion message generated by the model.

id: str

The identifier of the chat message.

content\_parts: Optional[List[ChatCompletionStoreMessageContentPart]]

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

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

class ChatCompletionStreamOptions: …

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

class ChatCompletionTokenLogprob: …

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

[ChatCompletionToolUnion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool%20%3E%20(schema))

A function tool that can be used to generate a response.

One of the following:

class ChatCompletionFunctionTool: …

A function tool that can be used to generate a response.

function: [FunctionDefinition](/api/reference/python/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

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

[ChatCompletionToolChoiceOption](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema))

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

class ChatCompletionAllowedTools: …

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

#### CompletionsMessages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/python/resources/chat/subresources/completions/subresources/messages/methods/list)

chat.completions.messages.list(strcompletion\_id, MessageListParams\*\*kwargs)  -> SyncCursorPage[[ChatCompletionStoreMessage](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema))]

GET/chat/completions/{completion\_id}/messages
