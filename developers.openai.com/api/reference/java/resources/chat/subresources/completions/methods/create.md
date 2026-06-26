<!-- source: https://developers.openai.com/api/reference/java/resources/chat/subresources/completions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/java)

[Chat](/api/reference/java/resources/chat)

[Completions](/api/reference/java/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create chat completion

[ChatCompletion](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) chat().completions().create(ChatCompletionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

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

ChatCompletionCreateParams params

List<[ChatCompletionMessageParam](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_param%20%3E%20(schema))> messages

A list of messages comprising the conversation so far. Depending on the
[model](https://platform.openai.com/docs/models) you use, different message types (modalities) are
supported, like [text](https://platform.openai.com/docs/guides/text-generation),
[images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

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

[ChatModel](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) model

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

Optional<[ChatCompletionAudioParam](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema))> audio

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

Optional<Double> frequencyPenalty

Number between -2.0 and 2.0. Positive values penalize new tokens based on
their existing frequency in the text so far, decreasing the model’s
likelihood to repeat the same line verbatim.

minimum-2

maximum2

DeprecatedOptional<FunctionCall> functionCall

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

enum FunctionCallMode:

`none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function.

NONE("none")

AUTO("auto")

class ChatCompletionFunctionCallOption:

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

String name

The name of the function to call.

DeprecatedOptional<List<Function>> functions

Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

String name

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Optional<String> description

A description of what the function does, used by the model to choose when and how to call the function.

Optional<[FunctionParameters](/api/reference/java/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))> parameters

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Optional<LogitBias> logitBias

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the
tokenizer) to an associated bias value from -100 to 100. Mathematically,
the bias is added to the logits generated by the model prior to sampling.
The exact effect will vary per model, but values between -1 and 1 should
decrease or increase likelihood of selection; values like -100 or 100
should result in a ban or exclusive selection of the relevant token.

Optional<Boolean> logprobs

Whether to return log probabilities of the output tokens or not. If true,
returns the log probabilities of each output token returned in the
`content` of `message`.

Optional<Long> maxCompletionTokens

An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

DeprecatedOptional<Long> maxTokens

The maximum number of [tokens](/tokenizer) that can be generated in the
chat completion. This value can be used to control
[costs](https://openai.com/api/pricing/) for text generated via API.

This value is now deprecated in favor of `max_completion_tokens`, and is
not compatible with [o-series models](https://platform.openai.com/docs/guides/reasoning).

Optional<Metadata> metadata

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Optional<List<Modality>> modalities

Output types that you would like the model to generate.
Most models are capable of generating text, which is the default:

`["text"]`

The `gpt-4o-audio-preview` model can also be used to
[generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate
both text and audio responses, you can use:

`["text", "audio"]`

TEXT("text")

AUDIO("audio")

Optional<Moderation> moderation

Configuration for running moderation on the request input and generated output.

String model

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

Optional<Long> n

How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

minimum1

maximum128

Optional<Boolean> parallelToolCalls

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

Optional<[ChatCompletionPredictionContent](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema))> prediction

Static predicted output content, such as the content of a text file that is
being regenerated.

Optional<Double> presencePenalty

Number between -2.0 and 2.0. Positive values penalize new tokens based on
whether they appear in the text so far, increasing the model’s likelihood
to talk about new topics.

minimum-2

maximum2

Optional<String> promptCacheKey

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

Optional<PromptCacheRetention> promptCacheRetention

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

IN\_MEMORY("in\_memory")

\_24H("24h")

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

Optional<ResponseFormat> responseFormat

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

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

Optional<String> safetyIdentifier

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

DeprecatedOptional<Long> seed

This feature is in Beta.
If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

minimum-9223372036854776000

maximum9223372036854776000

Optional<ServiceTier> serviceTier

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

AUTO("auto")

DEFAULT("default")

FLEX("flex")

SCALE("scale")

PRIORITY("priority")

Optional<Stop> stop

Not supported with latest reasoning models `o3` and `o4-mini`.

Up to 4 sequences where the API will stop generating further tokens. The
returned text will not contain the stop sequence.

String

List<String>

Optional<Boolean> store

Whether or not to store the output of this chat completion request for
use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or
[evals](https://platform.openai.com/docs/guides/evals) products.

Supports text and image inputs. Note: image inputs over 8MB will be dropped.

Optional<[ChatCompletionStreamOptions](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema))> streamOptions

Options for streaming response. Only set this when you set `stream: true`.

Optional<Double> temperature

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

Optional<[ChatCompletionToolChoiceOption](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema))> toolChoice

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

Optional<List<[ChatCompletionTool](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool%20%3E%20(schema))>> tools

A list of tools the model may call. You can provide either
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools) or
[function tools](https://platform.openai.com/docs/guides/function-calling).

class ChatCompletionFunctionTool:

A function tool that can be used to generate a response.

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

Optional<Long> topLogprobs

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.
`logprobs` must be set to `true` if this parameter is used.

minimum0

maximum20

Optional<Double> topP

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

DeprecatedOptional<String> user

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

Optional<Verbosity> verbosity

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<WebSearchOptions> webSearchOptions

This tool searches the web for relevant results to use in a response.
Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

Optional<SearchContextSize> searchContextSize

High level guidance for the amount of context window space to use for the
search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

LOW("low")

MEDIUM("medium")

HIGH("high")

Optional<UserLocation> userLocation

Approximate location parameters for the search.

Approximate approximate

Approximate location parameters for the search.

Optional<String> city

Free text input for the city of the user, e.g. `San Francisco`.

Optional<String> country

The two-letter
[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user,
e.g. `US`.

Optional<String> region

Free text input for the region of the user, e.g. `California`.

Optional<String> timezone

The [IANA timezone](https://timeapi.io/documentation/iana-timezones)
of the user, e.g. `America/Los_Angeles`.

JsonValue; type "approximate"constant"approximate"constant

The type of location approximation. Always `approximate`.

##### ReturnsExpand Collapse

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

long completionTokens

Number of tokens in the generated completion.

long promptTokens

Number of tokens in the prompt.

long totalTokens

Total number of tokens used in the request (prompt + completion).

Optional<CompletionTokensDetails> completionTokensDetails

Breakdown of tokens used in a completion.

Optional<Long> acceptedPredictionTokens

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

Optional<Long> audioTokens

Audio input tokens generated by the model.

Optional<Long> reasoningTokens

Tokens generated by the model for reasoning.

Optional<Long> rejectedPredictionTokens

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

Optional<PromptTokensDetails> promptTokensDetails

Breakdown of tokens used in the prompt.

Optional<Long> audioTokens

Audio input tokens present in the prompt.

Optional<Long> cachedTokens

Cached tokens present in the prompt.

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

long completionTokens

Number of tokens in the generated completion.

long promptTokens

Number of tokens in the prompt.

long totalTokens

Total number of tokens used in the request (prompt + completion).

Optional<CompletionTokensDetails> completionTokensDetails

Breakdown of tokens used in a completion.

Optional<Long> acceptedPredictionTokens

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

Optional<Long> audioTokens

Audio input tokens generated by the model.

Optional<Long> reasoningTokens

Tokens generated by the model for reasoning.

Optional<Long> rejectedPredictionTokens

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

Optional<PromptTokensDetails> promptTokensDetails

Breakdown of tokens used in the prompt.

Optional<Long> audioTokens

Audio input tokens present in the prompt.

Optional<Long> cachedTokens

Cached tokens present in the prompt.

### Create chat completion

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
import com.openai.models.ChatModel;
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionCreateParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
            .addDeveloperMessage("string")
            .model(ChatModel.GPT_5_4)
            .build();
        ChatCompletion chatCompletion = client.chat().completions().create(params);

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
