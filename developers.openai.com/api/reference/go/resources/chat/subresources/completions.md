<!-- source: https://developers.openai.com/api/reference/go/resources/chat/subresources/completions/ -->

[Skip to content](#_top)

[API Reference](/api/reference/go)

[Chat](/api/reference/go/resources/chat)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# Completions

Given a list of messages comprising a conversation, the model will return a response.

##### [Create chat completion](/api/reference/go/resources/chat/subresources/completions/methods/create)

client.Chat.Completions.New(ctx, body) (\*[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)), error)

POST/chat/completions

##### [List Chat Completions](/api/reference/go/resources/chat/subresources/completions/methods/list)

client.Chat.Completions.List(ctx, query) (\*CursorPage[[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))], error)

GET/chat/completions

##### [Get chat completion](/api/reference/go/resources/chat/subresources/completions/methods/retrieve)

client.Chat.Completions.Get(ctx, completionID) (\*[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)), error)

GET/chat/completions/{completion\_id}

##### [Update chat completion](/api/reference/go/resources/chat/subresources/completions/methods/update)

client.Chat.Completions.Update(ctx, completionID, body) (\*[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)), error)

POST/chat/completions/{completion\_id}

##### [Delete chat completion](/api/reference/go/resources/chat/subresources/completions/methods/delete)

client.Chat.Completions.Delete(ctx, completionID) (\*[ChatCompletionDeleted](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_deleted%20%3E%20(schema)), error)

DELETE/chat/completions/{completion\_id}

##### ModelsExpand Collapse

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

type ChatCompletionAllowedToolChoice struct{…}

Constrains the tools available to the model to a pre-defined set.

AllowedTools [ChatCompletionAllowedTools](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema))

Constrains the tools available to the model to a pre-defined set.

Type AllowedTools

Allowed tool configuration type. Always `allowed_tools`.

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

type ChatCompletionAudio struct{…}

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

type ChatCompletionAudioParamResp struct{…}

Parameters for audio output. Required when audio output is requested with
`modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

Format ChatCompletionAudioParamFormat

Specifies the output audio format. Must be one of `wav`, `mp3`, `flac`,
`opus`, or `pcm16`.

One of the following:

const ChatCompletionAudioParamFormatWAV ChatCompletionAudioParamFormat = "wav"

const ChatCompletionAudioParamFormatAAC ChatCompletionAudioParamFormat = "aac"

const ChatCompletionAudioParamFormatMP3 ChatCompletionAudioParamFormat = "mp3"

const ChatCompletionAudioParamFormatFLAC ChatCompletionAudioParamFormat = "flac"

const ChatCompletionAudioParamFormatOpus ChatCompletionAudioParamFormat = "opus"

const ChatCompletionAudioParamFormatPcm16 ChatCompletionAudioParamFormat = "pcm16"

Voice ChatCompletionAudioParamVoiceUnionResp

The voice the model uses to respond. Supported built-in voices are
`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`,
`sage`, `shimmer`, `marin`, and `cedar`. You may also provide a
custom voice object with an `id`, for example `{ "id": "voice_1234" }`.

One of the following:

string

string

One of the following:

const ChatCompletionAudioParamVoiceString2Alloy ChatCompletionAudioParamVoiceString2 = "alloy"

const ChatCompletionAudioParamVoiceString2Ash ChatCompletionAudioParamVoiceString2 = "ash"

const ChatCompletionAudioParamVoiceString2Ballad ChatCompletionAudioParamVoiceString2 = "ballad"

const ChatCompletionAudioParamVoiceString2Coral ChatCompletionAudioParamVoiceString2 = "coral"

const ChatCompletionAudioParamVoiceString2Echo ChatCompletionAudioParamVoiceString2 = "echo"

const ChatCompletionAudioParamVoiceString2Sage ChatCompletionAudioParamVoiceString2 = "sage"

const ChatCompletionAudioParamVoiceString2Shimmer ChatCompletionAudioParamVoiceString2 = "shimmer"

const ChatCompletionAudioParamVoiceString2Verse ChatCompletionAudioParamVoiceString2 = "verse"

const ChatCompletionAudioParamVoiceString2Marin ChatCompletionAudioParamVoiceString2 = "marin"

const ChatCompletionAudioParamVoiceString2Cedar ChatCompletionAudioParamVoiceString2 = "cedar"

ChatCompletionAudioParamVoiceIDResp

ID string

The custom voice ID, e.g. `voice_1234`.

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

type ChatCompletionContentPartUnion interface{…}

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

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

type ChatCompletionContentPartRefusal struct{…}

Refusal string

The refusal message generated by the model.

Type Refusal

The type of the content part.

type ChatCompletionContentPartText struct{…}

Learn about [text inputs](https://platform.openai.com/docs/guides/text-generation).

Text string

The text content.

Type Text

The type of the content part.

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

type ChatCompletionDeleted struct{…}

ID string

The ID of the chat completion that was deleted.

Deleted bool

Whether the chat completion was deleted.

Object ChatCompletionDeleted

The type of object being deleted.

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

type ChatCompletionFunctionCallOption struct{…}

Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.

Name string

The name of the function to call.

type ChatCompletionFunctionMessageParamResp struct{…}

Content string

The contents of the function message.

Name string

The name of the function to call.

Role Function

The role of the messages author, in this case `function`.

type ChatCompletionFunctionTool struct{…}

A function tool that can be used to generate a response.

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

Type Function

The type of the tool. Currently, only `function` is supported.

type ChatCompletionMessage struct{…}

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

type ChatCompletionMessageParamUnionResp interface{…}

Developer-provided instructions that the model should follow, regardless of
messages sent by the user. With o1 models and newer, `developer` messages
replace the previous `system` messages.

One of the following:

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

type ChatCompletionMessageToolCallUnion interface{…}

A call to a function tool created by the model.

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

type ChatCompletionModality string

One of the following:

const ChatCompletionModalityText [ChatCompletionModality](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_modality%20%3E%20(schema)) = "text"

const ChatCompletionModalityAudio [ChatCompletionModality](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_modality%20%3E%20(schema)) = "audio"

type ChatCompletionNamedToolChoice struct{…}

Specifies a tool the model should use. Use to force the model to call a specific function.

Function ChatCompletionNamedToolChoiceFunction

Name string

The name of the function to call.

Type Function

For function calling, the type is always `function`.

type ChatCompletionNamedToolChoiceCustom struct{…}

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

Custom ChatCompletionNamedToolChoiceCustomCustom

Name string

The name of the custom tool to call.

Type Custom

For custom tool calling, the type is always `custom`.

type ChatCompletionPredictionContent struct{…}

Static predicted output content, such as the content of a text file that is
being regenerated.

Content ChatCompletionPredictionContentContentUnion

The content that should be matched when generating a model response.
If generated tokens would match this content, the entire model response
can be returned much more quickly.

One of the following:

string

[][ChatCompletionContentPartText](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_content_part_text%20%3E%20(schema))

Text string

The text content.

Type Text

The type of the content part.

Type Content

The type of the predicted content you want to provide. This type is
currently always `content`.

type ChatCompletionRole string

The role of the author of a message

One of the following:

const ChatCompletionRoleDeveloper [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "developer"

const ChatCompletionRoleSystem [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "system"

const ChatCompletionRoleUser [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "user"

const ChatCompletionRoleAssistant [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "assistant"

const ChatCompletionRoleTool [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "tool"

const ChatCompletionRoleFunction [ChatCompletionRole](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_role%20%3E%20(schema)) = "function"

type ChatCompletionStoreMessage struct{…}

A chat completion message generated by the model.

ID string

The identifier of the chat message.

ContentParts []ChatCompletionStoreMessageContentPartUnionOptional

If a content parts array was provided, this is an array of `text` and `image_url` parts.
Otherwise, null.

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

type ChatCompletionStreamOptions struct{…}

Options for streaming response. Only set this when you set `stream: true`.

IncludeObfuscation boolOptional

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

IncludeUsage boolOptional

If set, an additional chunk will be streamed before the `data: [DONE]`
message. The `usage` field on this chunk shows the token usage statistics
for the entire request, and the `choices` field will always be an empty
array.

All other chunks will also include a `usage` field, but with a null
value. **NOTE:** If the stream is interrupted, you may not receive the
final usage chunk which contains the total token usage for the request.

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

type ChatCompletionTokenLogprob struct{…}

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

type ChatCompletionToolUnion interface{…}

A function tool that can be used to generate a response.

One of the following:

type ChatCompletionFunctionTool struct{…}

A function tool that can be used to generate a response.

Function [FunctionDefinition](/api/reference/go/resources/$shared#(resource)%20%24shared%20%3E%20(model)%20function_definition%20%3E%20(schema))

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

type ChatCompletionToolChoiceOptionUnion interface{…}

Controls which (if any) tool is called by the model.
`none` means the model will not call any tool and instead generates a message.
`auto` means the model can pick between generating a message or calling one or more tools.
`required` means the model must call one or more tools.
Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

`none` is the default when no tools are present. `auto` is the default if tools are present.

One of the following:

string

One of the following:

const ChatCompletionToolChoiceOptionAutoNone ChatCompletionToolChoiceOptionAuto = "none"

const ChatCompletionToolChoiceOptionAutoAuto ChatCompletionToolChoiceOptionAuto = "auto"

const ChatCompletionToolChoiceOptionAutoRequired ChatCompletionToolChoiceOptionAuto = "required"

type ChatCompletionAllowedToolChoice struct{…}

Constrains the tools available to the model to a pre-defined set.

AllowedTools [ChatCompletionAllowedTools](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20ChatCompletionAllowedTools%20%3E%20(schema))

Constrains the tools available to the model to a pre-defined set.

Type AllowedTools

Allowed tool configuration type. Always `allowed_tools`.

type ChatCompletionNamedToolChoice struct{…}

Specifies a tool the model should use. Use to force the model to call a specific function.

Function ChatCompletionNamedToolChoiceFunction

Name string

The name of the function to call.

Type Function

For function calling, the type is always `function`.

type ChatCompletionNamedToolChoiceCustom struct{…}

Specifies a tool the model should use. Use to force the model to call a specific custom tool.

Custom ChatCompletionNamedToolChoiceCustomCustom

Name string

The name of the custom tool to call.

Type Custom

For custom tool calling, the type is always `custom`.

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

type ChatCompletionAllowedTools struct{…}

Constrains the tools available to the model to a pre-defined set.

Mode ChatCompletionAllowedToolsMode

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

One of the following:

const ChatCompletionAllowedToolsModeAuto ChatCompletionAllowedToolsMode = "auto"

const ChatCompletionAllowedToolsModeRequired ChatCompletionAllowedToolsMode = "required"

Tools []map[string, any]

A list of tool definitions that the model should be allowed to call.

For the Chat Completions API, the list of tool definitions might look like:

[
  { "type": "function", "function": { "name": "get_weather" } },
  { "type": "function", "function": { "name": "get_time" } }
]

#### CompletionsMessages

Given a list of messages comprising a conversation, the model will return a response.

##### [Get chat messages](/api/reference/go/resources/chat/subresources/completions/subresources/messages/methods/list)

client.Chat.Completions.Messages.List(ctx, completionID, query) (\*CursorPage[[ChatCompletionStoreMessage](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_store_message%20%3E%20(schema))], error)

GET/chat/completions/{completion\_id}/messages
