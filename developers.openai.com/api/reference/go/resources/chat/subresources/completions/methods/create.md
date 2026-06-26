<!-- source: https://developers.openai.com/api/reference/go/resources/chat/subresources/completions/methods/create/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Chat](/api/reference/go/resources/chat)

[Completions](/api/reference/go/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Create chat completion

client.Chat.Completions.New(ctx, body) (\*[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)), error)

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

body ChatCompletionNewParams

Messages param.Field[[][ChatCompletionMessageParamUnionResp](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_param%20%3E%20(schema))]

A list of messages comprising the conversation so far. Depending on the
[model](https://platform.openai.com/docs/models) you use, different message types (modalities) are
supported, like [text](https://platform.openai.com/docs/guides/text-generation),
[images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

type ChatCompletionDeveloperMessageParamResp struct{…}

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

Content ChatCompletionDeveloperMessageParamContentUnionResp

The contents of the developer message.

One of the following:

string

[][ChatCompletionContentPartText](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

Text string

The text content.

Type Text

The type of the content part.

Role Developer

The role of the messages author, in this case `developer`.

Name stringOptional

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

type ChatCompletionSystemMessageParamResp struct{…}

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, use `developer` messages
for this purpose instead.

Content ChatCompletionSystemMessageParamContentUnionResp

The contents of the system message.

One of the following:

string

[][ChatCompletionContentPartText](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

Text string

The text content.

Type Text

The type of the content part.

Role System

The role of the messages author, in this case `system`.

Name stringOptional

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

type ChatCompletionUserMessageParamResp struct{…}

Messages sent by an end user, containing prompts or additional context
information.

Content ChatCompletionUserMessageParamContentUnionResp

The contents of the user message.

One of the following:

string

[][ChatCompletionContentPartUnion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part%20%3E%20(schema))

One of the following:

type ChatCompletionContentPartText struct{…}

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

Text string

The text content.

Type Text

The type of the content part.

type ChatCompletionContentPartImage struct{…}

Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

ImageURL ChatCompletionContentPartImageImageURL

URL string

Either a URL of the image or the base64 encoded image data.

formaturi

Detail stringOptional

Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision#low-or-high-fidelity-image-understanding).

One of the following:

const ChatCompletionContentPartImageImageURLDetailAuto ChatCompletionContentPartImageImageURLDetail = "auto"

const ChatCompletionContentPartImageImageURLDetailLow ChatCompletionContentPartImageImageURLDetail = "low"

const ChatCompletionContentPartImageImageURLDetailHigh ChatCompletionContentPartImageImageURLDetail = "high"

Type ImageURL

The type of the content part.

type ChatCompletionContentPartInputAudio struct{…}

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

InputAudio ChatCompletionContentPartInputAudioInputAudio

Data string

Base64 encoded audio data.

Format string

The format of the encoded audio data. Currently supports “wav” and “mp3”.

One of the following:

const ChatCompletionContentPartInputAudioInputAudioFormatWAV ChatCompletionContentPartInputAudioInputAudioFormat = "wav"

const ChatCompletionContentPartInputAudioInputAudioFormatMP3 ChatCompletionContentPartInputAudioInputAudioFormat = "mp3"

Type InputAudio

The type of the content part. Always `input_audio`.

ChatCompletionContentPartFile

File ChatCompletionContentPartFileFile

FileData stringOptional

The base64 encoded file data, used when passing the file to the model
as a string.

FileID stringOptional

The ID of an uploaded file to use as input.

Filename stringOptional

The name of the file, used when passing the file to the model as a
string.

Type File

The type of the content part. Always `file`.

Role User

The role of the messages author, in this case `user`.

Name stringOptional

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

type ChatCompletionAssistantMessageParamResp struct{…}

Messages sent by the model in response to user messages.

Role Assistant

The role of the messages author, in this case `assistant`.

Audio ChatCompletionAssistantMessageParamAudioRespOptional

Data about a previous audio response from the model.
[Learn more](https://platform.openai.com/docs/guides/audio).

ID string

Unique identifier for a previous audio response from the model.

Content ChatCompletionAssistantMessageParamContentUnionRespOptional

The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

One of the following:

string

[]ChatCompletionAssistantMessageParamContentArrayOfContentPartUnionResp

One of the following:

type ChatCompletionContentPartText struct{…}

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

Text string

The text content.

Type Text

The type of the content part.

type ChatCompletionContentPartRefusal struct{…}

Refusal string

The refusal message generated by the model.

Type Refusal

The type of the content part.

DeprecatedFunctionCall ChatCompletionAssistantMessageParamFunctionCallRespOptional

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

Arguments string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name string

The name of the function to call.

Name stringOptional

An optional name for the participant. Provides the model information to differentiate between participants of the same role.

Refusal stringOptional

The refusal message by the assistant.

ToolCalls [][ChatCompletionMessageToolCallUnion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))Optional

The tool calls generated by the model, such as function calls.

One of the following:

type ChatCompletionMessageFunctionToolCall struct{…}

A call to a function tool created by the model.

ID string

The ID of the tool call.

Function ChatCompletionMessageFunctionToolCallFunction

The function that the model called.

Arguments string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name string

The name of the function to call.

Type Function

The type of the tool. Currently, only `function` is supported.

type ChatCompletionMessageCustomToolCall struct{…}

A call to a custom tool created by the model.

ID string

The ID of the tool call.

Custom ChatCompletionMessageCustomToolCallCustom

The custom tool that the model called.

Input string

The input for the custom tool call generated by the model.

Name string

The name of the custom tool to call.

Type Custom

The type of the tool. Always `custom`.

type ChatCompletionToolMessageParamResp struct{…}

Content ChatCompletionToolMessageParamContentUnionResp

The contents of the tool message.

One of the following:

string

[][ChatCompletionContentPartText](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

Text string

The text content.

Type Text

The type of the content part.

Role Tool

The role of the messages author, in this case `tool`.

ToolCallID string

Tool call that this message is responding to.

type ChatCompletionFunctionMessageParamResp struct{…}

Content string

The contents of the function message.

Name string

The name of the function to call.

Role Function

The role of the messages author, in this case `function`.

Model param.Field[[ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema))]

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models)
to browse and compare available models.

string

type ChatModel string

One of the following:

const ChatModelGPT5\_4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4"

const ChatModelGPT5\_4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini"

const ChatModelGPT5\_4Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano"

const ChatModelGPT5\_4Mini2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-mini-2026-03-17"

const ChatModelGPT5\_4Nano2026\_03\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.4-nano-2026-03-17"

const ChatModelGPT5\_3ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.3-chat-latest"

const ChatModelGPT5\_2 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2"

const ChatModelGPT5\_2\_2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-2025-12-11"

const ChatModelGPT5\_2ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-chat-latest"

const ChatModelGPT5\_2Pro [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro"

const ChatModelGPT5\_2Pro2025\_12\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.2-pro-2025-12-11"

const ChatModelGPT5\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1"

const ChatModelGPT5\_1\_2025\_11\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-2025-11-13"

const ChatModelGPT5\_1Codex [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-codex"

const ChatModelGPT5\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-mini"

const ChatModelGPT5\_1ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5.1-chat-latest"

const ChatModelGPT5 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5"

const ChatModelGPT5Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini"

const ChatModelGPT5Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano"

const ChatModelGPT5\_2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-2025-08-07"

const ChatModelGPT5Mini2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-mini-2025-08-07"

const ChatModelGPT5Nano2025\_08\_07 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-nano-2025-08-07"

const ChatModelGPT5ChatLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-5-chat-latest"

const ChatModelGPT4\_1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1"

const ChatModelGPT4\_1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini"

const ChatModelGPT4\_1Nano [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano"

const ChatModelGPT4\_1\_2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-2025-04-14"

const ChatModelGPT4\_1Mini2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-mini-2025-04-14"

const ChatModelGPT4\_1Nano2025\_04\_14 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4.1-nano-2025-04-14"

const ChatModelO4Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini"

const ChatModelO4Mini2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o4-mini-2025-04-16"

const ChatModelO3 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3"

const ChatModelO3\_2025\_04\_16 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-2025-04-16"

const ChatModelO3Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini"

const ChatModelO3Mini2025\_01\_31 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o3-mini-2025-01-31"

const ChatModelO1 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1"

const ChatModelO1\_2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-2024-12-17"

const ChatModelO1Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview"

const ChatModelO1Preview2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-preview-2024-09-12"

const ChatModelO1Mini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini"

const ChatModelO1Mini2024\_09\_12 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "o1-mini-2024-09-12"

const ChatModelGPT4o [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o"

const ChatModelGPT4o2024\_11\_20 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-11-20"

const ChatModelGPT4o2024\_08\_06 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-08-06"

const ChatModelGPT4o2024\_05\_13 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-2024-05-13"

const ChatModelGPT4oAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview"

const ChatModelGPT4oAudioPreview2024\_10\_01 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-10-01"

const ChatModelGPT4oAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2024-12-17"

const ChatModelGPT4oAudioPreview2025\_06\_03 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-audio-preview-2025-06-03"

const ChatModelGPT4oMiniAudioPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview"

const ChatModelGPT4oMiniAudioPreview2024\_12\_17 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-audio-preview-2024-12-17"

const ChatModelGPT4oSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview"

const ChatModelGPT4oMiniSearchPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview"

const ChatModelGPT4oSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-search-preview-2025-03-11"

const ChatModelGPT4oMiniSearchPreview2025\_03\_11 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-search-preview-2025-03-11"

const ChatModelChatgpt4oLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "chatgpt-4o-latest"

const ChatModelCodexMiniLatest [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "codex-mini-latest"

const ChatModelGPT4oMini [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini"

const ChatModelGPT4oMini2024\_07\_18 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4o-mini-2024-07-18"

const ChatModelGPT4Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo"

const ChatModelGPT4Turbo2024\_04\_09 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-2024-04-09"

const ChatModelGPT4\_0125Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0125-preview"

const ChatModelGPT4TurboPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-turbo-preview"

const ChatModelGPT4\_1106Preview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-1106-preview"

const ChatModelGPT4VisionPreview [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-vision-preview"

const ChatModelGPT4 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4"

const ChatModelGPT4\_0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0314"

const ChatModelGPT4\_0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-0613"

const ChatModelGPT4\_32k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k"

const ChatModelGPT4\_32k0314 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0314"

const ChatModelGPT4\_32k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-4-32k-0613"

const ChatModelGPT3\_5Turbo [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo"

const ChatModelGPT3\_5Turbo16k [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k"

const ChatModelGPT3\_5Turbo0301 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0301"

const ChatModelGPT3\_5Turbo0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0613"

const ChatModelGPT3\_5Turbo1106 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-1106"

const ChatModelGPT3\_5Turbo0125 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-0125"

const ChatModelGPT3\_5Turbo16k0613 [ChatModel](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20chat_model%20%3E%20(schema)) = "gpt-3.5-turbo-16k-0613"

Audio param.Field[[ChatCompletionAudioParamResp](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio_param%20%3E%20(schema))]Optional

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

FrequencyPenalty param.Field[float64]Optional

Number between -2.0 and 2.0. Positive values penalize new tokens based on
their existing frequency in the text so far, decreasing the model’s
likelihood to repeat the same line verbatim.

minimum-2

maximum2

DeprecatedFunctionCall param.Field[[ChatCompletionNewParamsFunctionCallUnion](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20function_call%20%3E%20(schema))]Optional

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

string

One of the following:

const ChatCompletionNewParamsFunctionCallFunctionCallModeNone ChatCompletionNewParamsFunctionCallFunctionCallMode = "none"

const ChatCompletionNewParamsFunctionCallFunctionCallModeAuto ChatCompletionNewParamsFunctionCallFunctionCallMode = "auto"

type ChatCompletionFunctionCallOption struct{…}

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

Name string

The name of the function to call.

DeprecatedFunctions param.Field[[]ChatCompletionNewParamsFunction]Optional

Deprecated in favor of `tools`.

A list of functions the model may generate JSON inputs for.

Name string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the function does, used by the model to choose when and how to call the function.

Parameters [FunctionParameters](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))Optional

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

LogitBias param.Field[map[string, int64]]Optional

Modify the likelihood of specified tokens appearing in the completion.

Accepts a JSON object that maps tokens (specified by their token ID in the
tokenizer) to an associated bias value from -100 to 100. Mathematically,
the bias is added to the logits generated by the model prior to sampling.
The exact effect will vary per model, but values between -1 and 1 should
decrease or increase likelihood of selection; values like -100 or 100
should result in a ban or exclusive selection of the relevant token.

Logprobs param.Field[bool]Optional

Whether to return log probabilities of the output tokens or not. If true,
returns the log probabilities of each output token returned in the
`content` of `message`.

MaxCompletionTokens param.Field[int64]Optional

An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

DeprecatedMaxTokens param.Field[int64]Optional

The maximum number of [tokens](/tokenizer) that can be generated in the
chat completion. This value can be used to control
[costs](https://openai.com/api/pricing/) for text generated via API.

This value is now deprecated in favor of `max_completion_tokens`, and is
not compatible with [o-series models](https://platform.openai.com/docs/guides/reasoning).

Metadata param.Field[[Metadata](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20metadata%20%3E%20(schema))]Optional

Set of 16 key-value pairs that can be attached to an object. This can be
useful for storing additional information about the object in a structured
format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

Modalities param.Field[[]string]Optional

Output types that you would like the model to generate.
Most models are capable of generating text, which is the default:

`["text"]`

The `gpt-4o-audio-preview` model can also be used to
[generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate
both text and audio responses, you can use:

`["text", "audio"]`

const ChatCompletionNewParamsModalityText ChatCompletionNewParamsModality = "text"

const ChatCompletionNewParamsModalityAudio ChatCompletionNewParamsModality = "audio"

Moderation param.Field[[ChatCompletionNewParamsModeration](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20moderation%20%3E%20(schema))]Optional

Configuration for running moderation on the request input and generated output.

Model string

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

N param.Field[int64]Optional

How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

minimum1

maximum128

ParallelToolCalls param.Field[bool]Optional

Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling#configuring-parallel-function-calling) during tool use.

Prediction param.Field[[ChatCompletionPredictionContent](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_prediction_content%20%3E%20(schema))]Optional

Static predicted output content, such as the content of a text file that is
being regenerated.

PresencePenalty param.Field[float64]Optional

Number between -2.0 and 2.0. Positive values penalize new tokens based on
whether they appear in the text so far, increasing the model’s likelihood
to talk about new topics.

minimum-2

maximum2

PromptCacheKey param.Field[string]Optional

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](https://platform.openai.com/docs/guides/prompt-caching).

PromptCacheRetention param.Field[[ChatCompletionNewParamsPromptCacheRetention](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema))]Optional

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](https://platform.openai.com/docs/guides/prompt-caching#prompt-cache-retention).
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

const ChatCompletionNewParamsPromptCacheRetentionInMemory [ChatCompletionNewParamsPromptCacheRetention](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "in\_memory"

const ChatCompletionNewParamsPromptCacheRetention24h [ChatCompletionNewParamsPromptCacheRetention](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)) = "24h"

ReasoningEffort param.Field[[ReasoningEffort](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20reasoning_effort%20%3E%20(schema))]Optional

Constrains effort on reasoning for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).
Currently supported values are `none`, `minimal`, `low`, `medium`, `high`, and `xhigh`. Reducing
reasoning effort can result in faster responses and fewer tokens used
on reasoning in a response.

* `gpt-5.1` defaults to `none`, which does not perform reasoning. The supported reasoning values for `gpt-5.1` are `none`, `low`, `medium`, and `high`. Tool calls are supported for all reasoning values in gpt-5.1.
* All models before `gpt-5.1` default to `medium` reasoning effort, and do not support `none`.
* The `gpt-5-pro` model defaults to (and only supports) `high` reasoning effort.
* `xhigh` is supported for all models after `gpt-5.1-codex-max`.

ResponseFormat param.Field[[ChatCompletionNewParamsResponseFormatUnion](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema))]Optional

An object specifying the format that the model must output.

Setting to `{ "type": "json_schema", "json_schema": {...} }` enables
Structured Outputs which ensures the model will match your supplied JSON
schema. Learn more in the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

type ResponseFormatText struct{…}

Default response format. Used to generate text responses.

Type Text

The type of response format being defined. Always `text`.

type ResponseFormatJSONSchema struct{…}

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).

JSONSchema ResponseFormatJSONSchemaJSONSchema

Structured Outputs configuration options, including a JSON Schema.

Name string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the response format is for, used by the model to
determine how to respond in the format.

Schema map[string, any]Optional

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

Strict boolOptional

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](https://platform.openai.com/docs/guides/structured-outputs).

Type JSONSchema

The type of response format being defined. Always `json_schema`.

type ResponseFormatJSONObject struct{…}

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

Type JSONObject

The type of response format being defined. Always `json_object`.

SafetyIdentifier param.Field[string]Optional

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

DeprecatedSeed param.Field[int64]Optional

This feature is in Beta.
If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.
Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

minimum-9223372036854776000

maximum9223372036854776000

ServiceTier param.Field[[ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema))]Optional

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

const ChatCompletionNewParamsServiceTierAuto [ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "auto"

const ChatCompletionNewParamsServiceTierDefault [ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "default"

const ChatCompletionNewParamsServiceTierFlex [ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "flex"

const ChatCompletionNewParamsServiceTierScale [ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "scale"

const ChatCompletionNewParamsServiceTierPriority [ChatCompletionNewParamsServiceTier](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)) = "priority"

Stop param.Field[[ChatCompletionNewParamsStopUnion](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema))]Optional

Not supported with latest reasoning models `o3` and `o4-mini`.

Up to 4 sequences where the API will stop generating further tokens. The
returned text will not contain the stop sequence.

string

[]string

Store param.Field[bool]Optional

Whether or not to store the output of this chat completion request for
use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or
[evals](https://platform.openai.com/docs/guides/evals) products.

Supports text and image inputs. Note: image inputs over 8MB will be dropped.

StreamOptions param.Field[[ChatCompletionStreamOptions](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_stream_options%20%3E%20(schema))]Optional

Options for streaming response. Only set this when you set `stream: true`.

Temperature param.Field[float64]Optional

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

ToolChoice param.Field[[ChatCompletionToolChoiceOptionUnion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool_choice_option%20%3E%20(schema))]Optional

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

Tools param.Field[[][ChatCompletionToolUnion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_tool%20%3E%20(schema))]Optional

A list of tools the model may call. You can provide either
[custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools) or
[function tools](https://platform.openai.com/docs/guides/function-calling).

type ChatCompletionFunctionTool struct{…}

A function tool that can be used to generate a response.

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Name string

The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

Description stringOptional

A description of what the function does, used by the model to choose when and how to call the function.

Parameters [FunctionParameters](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_parameters%20%3E%20(schema))Optional

The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.

Omitting `parameters` defines a function with an empty parameter list.

Strict boolOptional

Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

Type Function

The type of the tool. Currently, only `function` is supported.

type ChatCompletionCustomTool struct{…}

A custom tool that processes input using a specified format.

Custom ChatCompletionCustomToolCustom

Properties of the custom tool.

Name string

The name of the custom tool, used to identify it in tool calls.

Description stringOptional

Optional description of the custom tool, used to provide more context.

Format ChatCompletionCustomToolCustomFormatUnionOptional

The input format for the custom tool. Default is unconstrained text.

One of the following:

ChatCompletionCustomToolCustomFormatText

Type Text

Unconstrained text format. Always `text`.

ChatCompletionCustomToolCustomFormatGrammar

Grammar ChatCompletionCustomToolCustomFormatGrammarGrammar

Your chosen grammar.

Definition string

The grammar definition.

Syntax string

The syntax of the grammar definition. One of `lark` or `regex`.

One of the following:

const ChatCompletionCustomToolCustomFormatGrammarGrammarSyntaxLark ChatCompletionCustomToolCustomFormatGrammarGrammarSyntax = "lark"

const ChatCompletionCustomToolCustomFormatGrammarGrammarSyntaxRegex ChatCompletionCustomToolCustomFormatGrammarGrammarSyntax = "regex"

Type Grammar

Grammar format. Always `grammar`.

Type Custom

The type of the custom tool. Always `custom`.

TopLogprobs param.Field[int64]Optional

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.
`logprobs` must be set to `true` if this parameter is used.

minimum0

maximum20

TopP param.Field[float64]Optional

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

DeprecatedUser param.Field[string]Optional

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#safety-identifiers).

Verbosity param.Field[[ChatCompletionNewParamsVerbosity](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema))]Optional

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

const ChatCompletionNewParamsVerbosityLow [ChatCompletionNewParamsVerbosity](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema)) = "low"

const ChatCompletionNewParamsVerbosityMedium [ChatCompletionNewParamsVerbosity](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema)) = "medium"

const ChatCompletionNewParamsVerbosityHigh [ChatCompletionNewParamsVerbosity](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema)) = "high"

WebSearchOptions param.Field[[ChatCompletionNewParamsWebSearchOptions](/api/reference/go/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%20default.non_streaming%20%3E%20(param)%20web_search_options%20%3E%20(schema))]Optional

This tool searches the web for relevant results to use in a response.
Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

SearchContextSize stringOptional

High level guidance for the amount of context window space to use for the
search. One of `low`, `medium`, or `high`. `medium` is the default.

One of the following:

const ChatCompletionNewParamsWebSearchOptionsSearchContextSizeLow ChatCompletionNewParamsWebSearchOptionsSearchContextSize = "low"

const ChatCompletionNewParamsWebSearchOptionsSearchContextSizeMedium ChatCompletionNewParamsWebSearchOptionsSearchContextSize = "medium"

const ChatCompletionNewParamsWebSearchOptionsSearchContextSizeHigh ChatCompletionNewParamsWebSearchOptionsSearchContextSize = "high"

UserLocation ChatCompletionNewParamsWebSearchOptionsUserLocationOptional

Approximate location parameters for the search.

Approximate ChatCompletionNewParamsWebSearchOptionsUserLocationApproximate

Approximate location parameters for the search.

City stringOptional

Free text input for the city of the user, e.g. `San Francisco`.

Country stringOptional

The two-letter
[ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1) of the user,
e.g. `US`.

Region stringOptional

Free text input for the region of the user, e.g. `California`.

Timezone stringOptional

The [IANA timezone](https://timeapi.io/documentation/iana-timezones)
of the user, e.g. `America/Los_Angeles`.

Type Approximate

The type of location approximation. Always `approximate`.

##### ReturnsExpand Collapse

type ChatCompletion struct{…}

Represents a chat completion response returned by model, based on the provided input.

ID string

A unique identifier for the chat completion.

Choices []ChatCompletionChoice

A list of chat completion choices. Can be more than one if `n` is greater than 1.

FinishReason string

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

One of the following:

const ChatCompletionChoiceFinishReasonStop ChatCompletionChoiceFinishReason = "stop"

const ChatCompletionChoiceFinishReasonLength ChatCompletionChoiceFinishReason = "length"

const ChatCompletionChoiceFinishReasonToolCalls ChatCompletionChoiceFinishReason = "tool\_calls"

const ChatCompletionChoiceFinishReasonContentFilter ChatCompletionChoiceFinishReason = "content\_filter"

const ChatCompletionChoiceFinishReasonFunctionCall ChatCompletionChoiceFinishReason = "function\_call"

Index int64

The index of the choice in the list of choices.

Logprobs ChatCompletionChoiceLogprobs

Log probability information for the choice.

Content [][ChatCompletionTokenLogprob](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))

A list of message content tokens with log probability information.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

TopLogprobs []ChatCompletionTokenLogprobTopLogprob

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Refusal [][ChatCompletionTokenLogprob](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))

A list of message refusal tokens with log probability information.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

TopLogprobs []ChatCompletionTokenLogprobTopLogprob

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Message [ChatCompletionMessage](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message%20%3E%20(schema))

A chat completion message generated by the model.

Content string

The contents of the message.

Refusal string

The refusal message generated by the model.

Role Assistant

The role of the author of this message.

Annotations []ChatCompletionMessageAnnotationOptional

Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

Type URLCitation

The type of the URL citation. Always `url_citation`.

URLCitation ChatCompletionMessageAnnotationURLCitation

A URL citation when using web search.

EndIndex int64

The index of the last character of the URL citation in the message.

StartIndex int64

The index of the first character of the URL citation in the message.

Title string

The title of the web resource.

URL string

The URL of the web resource.

formaturi

Audio [ChatCompletionAudio](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_audio%20%3E%20(schema))Optional

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

ID string

Unique identifier for this audio response.

Data string

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

ExpiresAt int64

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

formatunixtime

Transcript string

Transcript of the audio generated by the model.

DeprecatedFunctionCall ChatCompletionMessageFunctionCallOptional

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

Arguments string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name string

The name of the function to call.

ToolCalls [][ChatCompletionMessageToolCallUnion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))Optional

The tool calls generated by the model, such as function calls.

One of the following:

type ChatCompletionMessageFunctionToolCall struct{…}

A call to a function tool created by the model.

ID string

The ID of the tool call.

Function ChatCompletionMessageFunctionToolCallFunction

The function that the model called.

Arguments string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name string

The name of the function to call.

Type Function

The type of the tool. Currently, only `function` is supported.

type ChatCompletionMessageCustomToolCall struct{…}

A call to a custom tool created by the model.

ID string

The ID of the tool call.

Custom ChatCompletionMessageCustomToolCallCustom

The custom tool that the model called.

Input string

The input for the custom tool call generated by the model.

Name string

The name of the custom tool to call.

Type Custom

The type of the tool. Always `custom`.

Created int64

The Unix timestamp (in seconds) of when the chat completion was created.

formatunixtime

Model string

The model used for the chat completion.

Object ChatCompletion

The object type, which is always `chat.completion`.

Moderation ChatCompletionModerationOptional

Moderation results for the request input and generated output, if moderated
completions were requested.

Input ChatCompletionModerationInputUnion

Moderation for the request input.

One of the following:

type ChatCompletionModerationInputModerationResults struct{…}

Successful moderation results for the request input or generated output.

Model string

The moderation model used to generate the results.

Results []ChatCompletionModerationInputModerationResultsResult

A list of moderation results.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ChatCompletionModerationInputModerationResultsResultCategoryAppliedInputTypeText ChatCompletionModerationInputModerationResultsResultCategoryAppliedInputType = "text"

const ChatCompletionModerationInputModerationResultsResultCategoryAppliedInputTypeImage ChatCompletionModerationInputModerationResultsResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

Type ModerationResults

The object type, which is always `moderation_results`.

type ChatCompletionModerationInputError struct{…}

An error produced while attempting moderation.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which is always `error`.

Output ChatCompletionModerationOutputUnion

Moderation for the generated output.

One of the following:

type ChatCompletionModerationOutputModerationResults struct{…}

Successful moderation results for the request input or generated output.

Model string

The moderation model used to generate the results.

Results []ChatCompletionModerationOutputModerationResultsResult

A list of moderation results.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ChatCompletionModerationOutputModerationResultsResultCategoryAppliedInputTypeText ChatCompletionModerationOutputModerationResultsResultCategoryAppliedInputType = "text"

const ChatCompletionModerationOutputModerationResultsResultCategoryAppliedInputTypeImage ChatCompletionModerationOutputModerationResultsResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

Type ModerationResults

The object type, which is always `moderation_results`.

type ChatCompletionModerationOutputError struct{…}

An error produced while attempting moderation.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which is always `error`.

ServiceTier ChatCompletionServiceTierOptional

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

const ChatCompletionServiceTierAuto ChatCompletionServiceTier = "auto"

const ChatCompletionServiceTierDefault ChatCompletionServiceTier = "default"

const ChatCompletionServiceTierFlex ChatCompletionServiceTier = "flex"

const ChatCompletionServiceTierScale ChatCompletionServiceTier = "scale"

const ChatCompletionServiceTierPriority ChatCompletionServiceTier = "priority"

DeprecatedSystemFingerprint stringOptional

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

Usage [CompletionUsage](/api/reference/go/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema))Optional

Usage statistics for the completion request.

CompletionTokens int64

Number of tokens in the generated completion.

PromptTokens int64

Number of tokens in the prompt.

TotalTokens int64

Total number of tokens used in the request (prompt + completion).

CompletionTokensDetails CompletionUsageCompletionTokensDetailsOptional

Breakdown of tokens used in a completion.

AcceptedPredictionTokens int64Optional

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

AudioTokens int64Optional

Audio input tokens generated by the model.

ReasoningTokens int64Optional

Tokens generated by the model for reasoning.

RejectedPredictionTokens int64Optional

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

PromptTokensDetails CompletionUsagePromptTokensDetailsOptional

Breakdown of tokens used in the prompt.

AudioTokens int64Optional

Audio input tokens present in the prompt.

CachedTokens int64Optional

Cached tokens present in the prompt.

type ChatCompletionChunk struct{…}

Represents a streamed chunk of a chat completion response returned
by the model, based on the provided input.
[Learn more](https://platform.openai.com/docs/guides/streaming-responses).

ID string

A unique identifier for the chat completion. Each chunk has the same ID.

Choices []ChatCompletionChunkChoice

A list of chat completion choices. Can contain more than one elements if `n` is greater than 1. Can also be empty for the
last chunk if you set `stream_options: {"include_usage": true}`.

Delta ChatCompletionChunkChoiceDelta

A chat completion delta generated by streamed model responses.

Content stringOptional

The contents of the chunk message.

DeprecatedFunctionCall ChatCompletionChunkChoiceDeltaFunctionCallOptional

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

Arguments stringOptional

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name stringOptional

The name of the function to call.

Refusal stringOptional

The refusal message generated by the model.

Role stringOptional

The role of the author of this message.

One of the following:

const ChatCompletionChunkChoiceDeltaRoleDeveloper ChatCompletionChunkChoiceDeltaRole = "developer"

const ChatCompletionChunkChoiceDeltaRoleSystem ChatCompletionChunkChoiceDeltaRole = "system"

const ChatCompletionChunkChoiceDeltaRoleUser ChatCompletionChunkChoiceDeltaRole = "user"

const ChatCompletionChunkChoiceDeltaRoleAssistant ChatCompletionChunkChoiceDeltaRole = "assistant"

const ChatCompletionChunkChoiceDeltaRoleTool ChatCompletionChunkChoiceDeltaRole = "tool"

ToolCalls []ChatCompletionChunkChoiceDeltaToolCallOptional

Index int64

ID stringOptional

The ID of the tool call.

Function ChatCompletionChunkChoiceDeltaToolCallFunctionOptional

Arguments stringOptional

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

Name stringOptional

The name of the function to call.

Type stringOptional

The type of the tool. Currently, only `function` is supported.

FinishReason string

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.

One of the following:

const ChatCompletionChunkChoiceFinishReasonStop ChatCompletionChunkChoiceFinishReason = "stop"

const ChatCompletionChunkChoiceFinishReasonLength ChatCompletionChunkChoiceFinishReason = "length"

const ChatCompletionChunkChoiceFinishReasonToolCalls ChatCompletionChunkChoiceFinishReason = "tool\_calls"

const ChatCompletionChunkChoiceFinishReasonContentFilter ChatCompletionChunkChoiceFinishReason = "content\_filter"

const ChatCompletionChunkChoiceFinishReasonFunctionCall ChatCompletionChunkChoiceFinishReason = "function\_call"

Index int64

The index of the choice in the list of choices.

Logprobs ChatCompletionChunkChoiceLogprobsOptional

Log probability information for the choice.

Content [][ChatCompletionTokenLogprob](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))

A list of message content tokens with log probability information.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

TopLogprobs []ChatCompletionTokenLogprobTopLogprob

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Refusal [][ChatCompletionTokenLogprob](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema))

A list of message refusal tokens with log probability information.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

TopLogprobs []ChatCompletionTokenLogprobTopLogprob

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

Token string

The token.

Bytes []int64

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

Logprob float64

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

Created int64

The Unix timestamp (in seconds) of when the chat completion was created. Each chunk has the same timestamp.

formatunixtime

Model string

The model to generate the completion.

Object ChatCompletionChunk

The object type, which is always `chat.completion.chunk`.

Moderation ChatCompletionChunkModerationOptional

Moderation results for the request input and generated output. Present
on the moderation chunk when moderated completions are requested.

Input ChatCompletionChunkModerationInputUnion

Moderation for the request input.

One of the following:

type ChatCompletionChunkModerationInputModerationResults struct{…}

Successful moderation results for the request input or generated output.

Model string

The moderation model used to generate the results.

Results []ChatCompletionChunkModerationInputModerationResultsResult

A list of moderation results.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ChatCompletionChunkModerationInputModerationResultsResultCategoryAppliedInputTypeText ChatCompletionChunkModerationInputModerationResultsResultCategoryAppliedInputType = "text"

const ChatCompletionChunkModerationInputModerationResultsResultCategoryAppliedInputTypeImage ChatCompletionChunkModerationInputModerationResultsResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

Type ModerationResults

The object type, which is always `moderation_results`.

type ChatCompletionChunkModerationInputError struct{…}

An error produced while attempting moderation.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which is always `error`.

Output ChatCompletionChunkModerationOutputUnion

Moderation for the generated output.

One of the following:

type ChatCompletionChunkModerationOutputModerationResults struct{…}

Successful moderation results for the request input or generated output.

Model string

The moderation model used to generate the results.

Results []ChatCompletionChunkModerationOutputModerationResultsResult

A list of moderation results.

Categories map[string, bool]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

CategoryAppliedInputTypes map[string, []string]

Which modalities of input are reflected by the score for each category.

One of the following:

const ChatCompletionChunkModerationOutputModerationResultsResultCategoryAppliedInputTypeText ChatCompletionChunkModerationOutputModerationResultsResultCategoryAppliedInputType = "text"

const ChatCompletionChunkModerationOutputModerationResultsResultCategoryAppliedInputTypeImage ChatCompletionChunkModerationOutputModerationResultsResultCategoryAppliedInputType = "image"

CategoryScores map[string, float64]

A dictionary of moderation categories to scores.

Flagged bool

A boolean indicating whether the content was flagged by any category.

Model string

The moderation model that produced this result.

Type ModerationResult

The object type, which was always `moderation_result` for successful moderation results.

Type ModerationResults

The object type, which is always `moderation_results`.

type ChatCompletionChunkModerationOutputError struct{…}

An error produced while attempting moderation.

Code string

The error code.

Message string

The error message.

Type Error

The object type, which is always `error`.

ServiceTier ChatCompletionChunkServiceTierOptional

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

One of the following:

const ChatCompletionChunkServiceTierAuto ChatCompletionChunkServiceTier = "auto"

const ChatCompletionChunkServiceTierDefault ChatCompletionChunkServiceTier = "default"

const ChatCompletionChunkServiceTierFlex ChatCompletionChunkServiceTier = "flex"

const ChatCompletionChunkServiceTierScale ChatCompletionChunkServiceTier = "scale"

const ChatCompletionChunkServiceTierPriority ChatCompletionChunkServiceTier = "priority"

DeprecatedSystemFingerprint stringOptional

This fingerprint represents the backend configuration that the model runs with.
Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

Usage [CompletionUsage](/api/reference/go/resources/completions#(resource)%20completions%20%3E%20(model)%20completion_usage%20%3E%20(schema))Optional

An optional field that will only be present when you set
`stream_options: {"include_usage": true}` in your request. When present, it
contains a null value **except for the last chunk** which contains the
token usage statistics for the entire request.

**NOTE:** If the stream is interrupted or cancelled, you may not
receive the final usage chunk which contains the total token usage for
the request.

CompletionTokens int64

Number of tokens in the generated completion.

PromptTokens int64

Number of tokens in the prompt.

TotalTokens int64

Total number of tokens used in the request (prompt + completion).

CompletionTokensDetails CompletionUsageCompletionTokensDetailsOptional

Breakdown of tokens used in a completion.

AcceptedPredictionTokens int64Optional

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

AudioTokens int64Optional

Audio input tokens generated by the model.

ReasoningTokens int64Optional

Tokens generated by the model for reasoning.

RejectedPredictionTokens int64Optional

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

PromptTokensDetails CompletionUsagePromptTokensDetailsOptional

Breakdown of tokens used in the prompt.

AudioTokens int64Optional

Audio input tokens present in the prompt.

CachedTokens int64Optional

Cached tokens present in the prompt.

### Create chat completion

Go

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

package main

import (
  "context"
  "fmt"

  "github.com/openai/openai-go"
  "github.com/openai/openai-go/option"
  "github.com/openai/openai-go/shared"

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  chatCompletion, err := client.Chat.Completions.New(context.TODO(), openai.ChatCompletionNewParams{
    Messages: []openai.ChatCompletionMessageParamUnion{openai.ChatCompletionMessageParamUnion{
      OfDeveloper: &openai.ChatCompletionDeveloperMessageParam{
        Content: openai.ChatCompletionDeveloperMessageParamContentUnion{
          OfString: openai.String("string"),
    }},
    Model: shared.ChatModelGPT5_4,
  })
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", chatCompletion)

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
