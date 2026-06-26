<!-- source: https://developers.openai.com/api/reference/java/resources/chat/subresources/completions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Chat](/api/reference/java/resources/chat)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Completions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](/api/reference/java/resources/chat/subresources/completions/methods/create)

[ChatCompletion](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) chat().completions().create(ChatCompletionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/chat/completions

##### [List Chat Completions](/api/reference/java/resources/chat/subresources/completions/methods/list)

ChatCompletionListPage chat().completions().list(ChatCompletionListParamsparams = ChatCompletionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chat/completions

##### [Get chat completion](/api/reference/java/resources/chat/subresources/completions/methods/retrieve)

[ChatCompletion](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) chat().completions().retrieve(ChatCompletionRetrieveParamsparams = ChatCompletionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chat/completions/{completion\_id}

##### [Update chat completion](/api/reference/java/resources/chat/subresources/completions/methods/update)

[ChatCompletion](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) chat().completions().update(ChatCompletionUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/chat/completions/{completion\_id}

##### [Delete chat completion](/api/reference/java/resources/chat/subresources/completions/methods/delete)

[ChatCompletionDeleted](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)) chat().completions().delete(ChatCompletionDeleteParamsparams = ChatCompletionDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/chat/completions/{completion\_id}

##### ModelsExpand Collapse

class ChatCompletion:

Represents a chat completion response returned by model, based on the provided input.

String id

A unique identifier for the chat completion.

List<Choice> choices

A list of chat completion choices. Can be more than one if `n` is greater than 1.

FinishReason finishReason

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

One of the following:

STOP("stop")

LENGTH("length")

TOOL\_CALLS("tool\_calls")

CONTENT\_FILTER("content\_filter")

FUNCTION\_CALL("function\_call")

long index

The index of the choice in the list of choices.

Optional<Logprobs> logprobs

Log probability information for the choice.

Optional<List<[ChatCompletionTokenLogprob](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))>> content

A list of message content tokens with log probability information.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

List<TopLogprob> topLogprobs

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Optional<List<[ChatCompletionTokenLogprob](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))>> refusal

A list of message refusal tokens with log probability information.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

List<TopLogprob> topLogprobs

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

[ChatCompletionMessage](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema)) message

A chat completion message generated by the model.

long created

The Unix timestamp (in seconds) of when the chat completion was created.

formatunixtime

String model

The model used for the chat completion.

JsonValue; object\_ "chat.completion"constant"chat.completion"constant

The object type, which is always `chat.completion`.

Optional<Moderation> moderation

Moderation results for the request input and generated output, if moderated
completions were requested.

Input input

Moderation for the request input.

One of the following:

class ModerationResults:

Successful moderation results for the request input or generated output.

String model

The moderation model used to generate the results.

List<Result> results

A list of moderation results.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

One of the following:

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

JsonValue; type "moderation\_results"constant"moderation\_results"constant

The object type, which is always `moderation_results`.

class Error:

An error produced while attempting moderation.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which is always `error`.

Output output

Moderation for the generated output.

One of the following:

class ModerationResults:

Successful moderation results for the request input or generated output.

String model

The moderation model used to generate the results.

List<Result> results

A list of moderation results.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

One of the following:

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

JsonValue; type "moderation\_results"constant"moderation\_results"constant

The object type, which is always `moderation_results`.

class Error:

An error produced while attempting moderation.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which is always `error`.

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

DeprecatedOptional<String> systemFingerprint

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

Optional<[CompletionUsage](/api/reference/java/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema))> usage

Usage statistics for the completion request.

class ChatCompletionAllowedToolChoice:

Constrains the tools available to the model to a pre-defined set.

[ChatCompletionAllowedTools](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) allowedTools

Constrains the tools available to the model to a pre-defined set.

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class ChatCompletionAssistantMessageParam:

Messages sent by the model in response to user messages.

JsonValue; role "assistant"constant"assistant"constant

The role of the messages author, in this case `assistant`.

Optional<Audio> audio

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

String id

Unique identifier for a previous audio response from the model.

Optional<Content> content

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

String

List<ChatCompletionRequestAssistantMessageContentPart>

One of the following:

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartRefusal:

String refusal

The refusal message generated by the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the content part.

DeprecatedOptional<FunctionCall> functionCall

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

Optional<String> refusal

The refusal message by the assistant.

Optional<List<[ChatCompletionMessageToolCall](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))>> toolCalls

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall:

A call to a function tool created by the model.

String id

The ID of the tool call.

Function function

The function that the model called.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall:

A call to a custom tool created by the model.

String id

The ID of the tool call.

Custom custom

The custom tool that the model called.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

The type of the tool. Always `custom`.

class ChatCompletionAudio:

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

String id

Unique identifier for this audio response.

String data

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

long expiresAt

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

formatunixtime

String transcript

Transcript of the audio generated by the model.

class ChatCompletionAudioParam:

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

Format format

Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.

One of the following:

WAV("wav")

AAC("aac")

MP3("mp3")

FLAC("flac")

OPUS("opus")

PCM16("pcm16")

Voice voice

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
`sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

One of the following:

String

enum UnionMember1:

ALLOY("alloy")

ASH("ash")

BALLAD("ballad")

CORAL("coral")

ECHO("echo")

SAGE("sage")

SHIMMER("shimmer")

VERSE("verse")

MARIN("marin")

CEDAR("cedar")

class Id:

Custom voice reference.

String id

The custom voice ID, e.g. `voice_1234`.

class ChatCompletionChunk:

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](https://platform.openai.com/docs/guides/streaming-responses).

String id

A unique identifier for the chat completion. Each chunk has the same ID.

List<Choice> choices

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

Delta delta

A chat completion delta generated by streamed model responses.

Optional<String> content

The contents of the chunk message.

DeprecatedOptional<FunctionCall> functionCall

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

Optional<String> arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Optional<String> name

The name of the function to call.

Optional<String> refusal

The refusal message generated by the model.

Optional<Role> role

The role of the author of this message.

One of the following:

DEVELOPER("developer")

SYSTEM("system")

USER("user")

ASSISTANT("assistant")

TOOL("tool")

Optional<List<ToolCall>> toolCalls

long index

Optional<String> id

The ID of the tool call.

Optional<Function> function

Optional<String> arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Optional<String> name

The name of the function to call.

Optional<Type> type

The type of the tool. Currently, only `function` is supported.

Optional<FinishReason> finishReason

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

One of the following:

STOP("stop")

LENGTH("length")

TOOL\_CALLS("tool\_calls")

CONTENT\_FILTER("content\_filter")

FUNCTION\_CALL("function\_call")

long index

The index of the choice in the list of choices.

Optional<Logprobs> logprobs

Log probability information for the choice.

Optional<List<[ChatCompletionTokenLogprob](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))>> content

A list of message content tokens with log probability information.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

List<TopLogprob> topLogprobs

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Optional<List<[ChatCompletionTokenLogprob](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))>> refusal

A list of message refusal tokens with log probability information.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

List<TopLogprob> topLogprobs

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

long created

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

formatunixtime

String model

The model to generate the completion.

JsonValue; object\_ "chat.completion.chunk"constant"chat.completion.chunk"constant

The object type, which is always `chat.completion.chunk`.

Optional<Moderation> moderation

Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.

Input input

Moderation for the request input.

One of the following:

class ModerationResults:

Successful moderation results for the request input or generated output.

String model

The moderation model used to generate the results.

List<Result> results

A list of moderation results.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

One of the following:

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

JsonValue; type "moderation\_results"constant"moderation\_results"constant

The object type, which is always `moderation_results`.

class Error:

An error produced while attempting moderation.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which is always `error`.

Output output

Moderation for the generated output.

One of the following:

class ModerationResults:

Successful moderation results for the request input or generated output.

String model

The moderation model used to generate the results.

List<Result> results

A list of moderation results.

Categories categories

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes categoryAppliedInputTypes

Which modalities of input are reflected by the score for each category.

One of the following:

TEXT("text")

IMAGE("image")

CategoryScores categoryScores

A dictionary of moderation categories to scores.

boolean flagged

A boolean indicating whether the content was flagged by any category.

String model

The moderation model that produced this result.

JsonValue; type "moderation\_result"constant"moderation\_result"constant

The object type, which was always `moderation_result` for successful moderation results.

JsonValue; type "moderation\_results"constant"moderation\_results"constant

The object type, which is always `moderation_results`.

class Error:

An error produced while attempting moderation.

String code

The error code.

String message

The error message.

JsonValue; type "error"constant"error"constant

The object type, which is always `error`.

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

DeprecatedOptional<String> systemFingerprint

This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

Optional<[CompletionUsage](/api/reference/java/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema))> usage

An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the
token usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

class ChatCompletionContentPart: A class that can be one of several variants.union

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartImage:

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageUrl imageUrl

String url

Either a URL of the image or the base64 encoded image data.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ChatCompletionContentPartInputAudio:

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

InputAudio inputAudio

String data

Base64 encoded audio data.

Format format

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

WAV("wav")

MP3("mp3")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the content part. Always `input_audio`.

File

FileObject file

Optional<String> fileData

The base64 encoded file data, used when passing the file to the model
as a string.

Optional<String> fileId

The ID of an uploaded file to use as input.

Optional<String> filename

The name of the file, used when passing the file to the model as a
string.

JsonValue; type "file"constant"file"constant

The type of the content part. Always `file`.

class ChatCompletionContentPartImage:

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageUrl imageUrl

String url

Either a URL of the image or the base64 encoded image data.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ChatCompletionContentPartInputAudio:

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

InputAudio inputAudio

String data

Base64 encoded audio data.

Format format

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

WAV("wav")

MP3("mp3")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the content part. Always `input_audio`.

class ChatCompletionContentPartRefusal:

String refusal

The refusal message generated by the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the content part.

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionCustomTool:

A custom tool that processes input using a specified format.

Custom custom

Properties of the custom tool.

String name

The name of the custom tool, used to identify it in tool calls.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

One of the following:

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

InnerGrammar grammar

Your chosen grammar.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

class ChatCompletionDeleted:

String id

The ID of the chat completion that was deleted.

boolean deleted

Whether the chat completion was deleted.

JsonValue; object\_ "chat.completion.deleted"constant"chat.completion.deleted"constant

The type of object being deleted.

class ChatCompletionDeveloperMessageParam:

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

Content content

The contents of the developer message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "developer"constant"developer"constant

The role of the messages author, in this case `developer`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionFunctionCallOption:

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

String name

The name of the function to call.

class ChatCompletionFunctionMessageParam:

Optional<String> content

The contents of the function message.

String name

The name of the function to call.

JsonValue; role "function"constant"function"constant

The role of the messages author, in this case `function`.

class ChatCompletionFunctionTool:

A function tool that can be used to generate a response.

[FunctionDefinition](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) function

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessage:

A chat completion message generated by the model.

Optional<String> content

The contents of the message.

Optional<String> refusal

The refusal message generated by the model.

JsonValue; role "assistant"constant"assistant"constant

The role of the author of this message.

Optional<List<Annotation>> annotations

Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

JsonValue; type "url\_citation"constant"url\_citation"constant

The type of the URL citation. Always `url_citation`.

UrlCitation urlCitation

A URL citation when using web search.

long endIndex

The index of the last character of the URL citation in the message.

long startIndex

The index of the first character of the URL citation in the message.

String title

The title of the web resource.

String url

The URL of the web resource.

formaturi

Optional<[ChatCompletionAudio](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema))> audio

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

DeprecatedOptional<FunctionCall> functionCall

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

Optional<List<[ChatCompletionMessageToolCall](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))>> toolCalls

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall:

A call to a function tool created by the model.

String id

The ID of the tool call.

Function function

The function that the model called.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall:

A call to a custom tool created by the model.

String id

The ID of the tool call.

Custom custom

The custom tool that the model called.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

The type of the tool. Always `custom`.

class ChatCompletionMessageCustomToolCall:

A call to a custom tool created by the model.

String id

The ID of the tool call.

Custom custom

The custom tool that the model called.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

The type of the tool. Always `custom`.

class ChatCompletionMessageFunctionToolCall:

A call to a function tool created by the model.

String id

The ID of the tool call.

Function function

The function that the model called.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageParam: A class that can be one of several variants.union

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

class ChatCompletionDeveloperMessageParam:

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

Content content

The contents of the developer message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "developer"constant"developer"constant

The role of the messages author, in this case `developer`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionSystemMessageParam:

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

Content content

The contents of the system message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "system"constant"system"constant

The role of the messages author, in this case `system`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionUserMessageParam:

Messages sent by an end user, containing prompts or additional context
information.

Content content

The contents of the user message.

One of the following:

String

List<[ChatCompletionContentPart](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))>

One of the following:

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartImage:

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageUrl imageUrl

String url

Either a URL of the image or the base64 encoded image data.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ChatCompletionContentPartInputAudio:

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

InputAudio inputAudio

String data

Base64 encoded audio data.

Format format

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

WAV("wav")

MP3("mp3")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the content part. Always `input_audio`.

File

FileObject file

Optional<String> fileData

The base64 encoded file data, used when passing the file to the model
as a string.

Optional<String> fileId

The ID of an uploaded file to use as input.

Optional<String> filename

The name of the file, used when passing the file to the model as a
string.

JsonValue; type "file"constant"file"constant

The type of the content part. Always `file`.

JsonValue; role "user"constant"user"constant

The role of the messages author, in this case `user`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionAssistantMessageParam:

Messages sent by the model in response to user messages.

JsonValue; role "assistant"constant"assistant"constant

The role of the messages author, in this case `assistant`.

Optional<Audio> audio

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

String id

Unique identifier for a previous audio response from the model.

Optional<Content> content

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

String

List<ChatCompletionRequestAssistantMessageContentPart>

One of the following:

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartRefusal:

String refusal

The refusal message generated by the model.

JsonValue; type "refusal"constant"refusal"constant

The type of the content part.

DeprecatedOptional<FunctionCall> functionCall

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

Optional<String> refusal

The refusal message by the assistant.

Optional<List<[ChatCompletionMessageToolCall](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))>> toolCalls

The tool calls generated by the model, such as function calls.

One of the following:

class ChatCompletionMessageFunctionToolCall:

A call to a function tool created by the model.

String id

The ID of the tool call.

Function function

The function that the model called.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall:

A call to a custom tool created by the model.

String id

The ID of the tool call.

Custom custom

The custom tool that the model called.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

The type of the tool. Always `custom`.

class ChatCompletionToolMessageParam:

Content content

The contents of the tool message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "tool"constant"tool"constant

The role of the messages author, in this case `tool`.

String toolCallId

Tool call that this message is responding to.

class ChatCompletionFunctionMessageParam:

Optional<String> content

The contents of the function message.

String name

The name of the function to call.

JsonValue; role "function"constant"function"constant

The role of the messages author, in this case `function`.

class ChatCompletionMessageToolCall: A class that can be one of several variants.union

A call to a function tool created by the model.

class ChatCompletionMessageFunctionToolCall:

A call to a function tool created by the model.

String id

The ID of the tool call.

Function function

The function that the model called.

String arguments

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionMessageCustomToolCall:

A call to a custom tool created by the model.

String id

The ID of the tool call.

Custom custom

The custom tool that the model called.

String input

The input for the custom tool call generated by the model.

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

The type of the tool. Always `custom`.

enum ChatCompletionModality:

TEXT("text")

AUDIO("audio")

class ChatCompletionNamedToolChoice:

Specifies a tool the model should use. Use to force the model to call a specific function.

Function function

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class ChatCompletionNamedToolChoiceCustom:

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

Custom custom

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

class ChatCompletionPredictionContent:

Static predicted output content, such as the content of a text file that is
being regenerated.

Content content

The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; type "content"constant"content"constant

The type of the predicted content you want to provide. This type is
currently always `content`.

enum ChatCompletionRole:

The role of the author of a message

DEVELOPER("developer")

SYSTEM("system")

USER("user")

ASSISTANT("assistant")

TOOL("tool")

FUNCTION("function")

class ChatCompletionStoreMessage:

A chat completion message generated by the model.

String id

The identifier of the chat message.

Optional<List<ContentPart>> contentParts

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

One of the following:

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartImage:

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageUrl imageUrl

String url

Either a URL of the image or the base64 encoded image data.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ChatCompletionStreamOptions:

Options for streaming response. Only set this when you set `stream: true`.

Optional<Boolean> includeObfuscation

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

Optional<Boolean> includeUsage

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

class ChatCompletionSystemMessageParam:

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

Content content

The contents of the system message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "system"constant"system"constant

The role of the messages author, in this case `system`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionTokenLogprob:

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

List<TopLogprob> topLogprobs

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

String token

The token.

Optional<List<Long>> bytes

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

double logprob

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

class ChatCompletionTool: A class that can be one of several variants.union

A function tool that can be used to generate a response.

class ChatCompletionFunctionTool:

A function tool that can be used to generate a response.

[FunctionDefinition](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema)) function

JsonValue; type "function"constant"function"constant

The type of the tool. Currently, only `function` is supported.

class ChatCompletionCustomTool:

A custom tool that processes input using a specified format.

Custom custom

Properties of the custom tool.

String name

The name of the custom tool, used to identify it in tool calls.

Optional<String> description

Optional description of the custom tool, used to provide more context.

Optional<Format> format

The input format for the custom tool. Default is unconstrained text.

One of the following:

JsonValue;

JsonValue; type "text"constant"text"constant

Unconstrained text format. Always `text`.

class Grammar:

A grammar defined by the user.

InnerGrammar grammar

Your chosen grammar.

String definition

The grammar definition.

Syntax syntax

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

LARK("lark")

REGEX("regex")

JsonValue; type "grammar"constant"grammar"constant

Grammar format. Always `grammar`.

JsonValue; type "custom"constant"custom"constant

The type of the custom tool. Always `custom`.

class ChatCompletionToolChoiceOption: A class that can be one of several variants.union

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

Auto

One of the following:

NONE("none")

AUTO("auto")

REQUIRED("required")

class ChatCompletionAllowedToolChoice:

Constrains the tools available to the model to a pre-defined set.

[ChatCompletionAllowedTools](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema)) allowedTools

Constrains the tools available to the model to a pre-defined set.

JsonValue; type "allowed\_tools"constant"allowed\_tools"constant

Allowed tool configuration type. Always `allowed_tools`.

class ChatCompletionNamedToolChoice:

Specifies a tool the model should use. Use to force the model to call a specific function.

Function function

String name

The name of the function to call.

JsonValue; type "function"constant"function"constant

For function calling, the type is always `function`.

class ChatCompletionNamedToolChoiceCustom:

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

Custom custom

String name

The name of the custom tool to call.

JsonValue; type "custom"constant"custom"constant

For custom tool calling, the type is always `custom`.

class ChatCompletionToolMessageParam:

Content content

The contents of the tool message.

One of the following:

String

List<[ChatCompletionContentPartText](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))>

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

JsonValue; role "tool"constant"tool"constant

The role of the messages author, in this case `tool`.

String toolCallId

Tool call that this message is responding to.

class ChatCompletionUserMessageParam:

Messages sent by an end user, containing prompts or additional context
information.

Content content

The contents of the user message.

One of the following:

String

List<[ChatCompletionContentPart](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))>

One of the following:

class ChatCompletionContentPartText:

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

String text

The text content.

JsonValue; type "text"constant"text"constant

The type of the content part.

class ChatCompletionContentPartImage:

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageUrl imageUrl

String url

Either a URL of the image or the base64 encoded image data.

formaturi

Optional<Detail> detail

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

AUTO("auto")

LOW("low")

HIGH("high")

JsonValue; type "image\_url"constant"image\_url"constant

The type of the content part.

class ChatCompletionContentPartInputAudio:

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

InputAudio inputAudio

String data

Base64 encoded audio data.

Format format

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

WAV("wav")

MP3("mp3")

JsonValue; type "input\_audio"constant"input\_audio"constant

The type of the content part. Always `input_audio`.

File

FileObject file

Optional<String> fileData

The base64 encoded file data, used when passing the file to the model
as a string.

Optional<String> fileId

The ID of an uploaded file to use as input.

Optional<String> filename

The name of the file, used when passing the file to the model as a
string.

JsonValue; type "file"constant"file"constant

The type of the content part. Always `file`.

JsonValue; role "user"constant"user"constant

The role of the messages author, in this case `user`.

Optional<String> name

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

class ChatCompletionAllowedTools:

Constrains the tools available to the model to a pre-defined set.

Mode mode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

AUTO("auto")

REQUIRED("required")

List<Tool> tools

A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

[
  { "type": "function", "function": { "name": "get_weather" } },
  { "type": "function", "function": { "name": "get_time" } }
]

#### CompletionsMessages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/java/resources/chat/subresources/completions/subresources/messages/methods/list)

MessageListPage chat().completions().messages().list(MessageListParamsparams = MessageListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chat/completions/{completion\_id}/messages
