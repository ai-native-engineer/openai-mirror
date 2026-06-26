<!-- source: https://developers.openai.com/api/reference/go/resources/chat/subresources/completions/methods/retrieve/ -->

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

# Get chat completion

client.Chat.Completions.Get(ctx, completionID) (\*[ChatCompletion](/api/reference/go/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)), error)

GET/chat/completions/{completion\_id}

Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.

##### ParametersExpand Collapse

completionID string

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

### Get chat completion

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

func main() {
  client := openai.NewClient(
    option.WithAPIKey("My API Key"),
  chatCompletion, err := client.Chat.Completions.Get(context.TODO(), "completion_id")
  if err != nil {
    panic(err.Error())
  fmt.Printf("%+v\n", chatCompletion.ID)

  "object": "chat.completion",
  "id": "chatcmpl-abc123",
  "model": "gpt-4o-2024-08-06",
  "created": 1738960610,
  "request_id": "req_ded8ab984ec4bf840f37566c1011c417",
  "tool_choice": null,
  "usage": {
    "total_tokens": 31,
    "completion_tokens": 18,
    "prompt_tokens": 13
  "seed": 4944116822809979520,
  "top_p": 1.0,
  "temperature": 1.0,
  "presence_penalty": 0.0,
  "frequency_penalty": 0.0,
  "system_fingerprint": "fp_50cad350e4",
  "input_user": null,
  "service_tier": "default",
  "tools": null,
  "metadata": {},
  "choices": [
      "index": 0,
      "message": {
        "content": "Mind of circuits hum,  \nLearning patterns in silence—  \nFuture's quiet spark.",
        "role": "assistant",
        "tool_calls": null,
        "function_call": null
      "finish_reason": "stop",
      "logprobs": null
  ],
  "response_format": null

##### Returns Examples

  "object": "chat.completion",
  "id": "chatcmpl-abc123",
  "model": "gpt-4o-2024-08-06",
  "created": 1738960610,
  "request_id": "req_ded8ab984ec4bf840f37566c1011c417",
  "tool_choice": null,
  "usage": {
    "total_tokens": 31,
    "completion_tokens": 18,
    "prompt_tokens": 13
  "seed": 4944116822809979520,
  "top_p": 1.0,
  "temperature": 1.0,
  "presence_penalty": 0.0,
  "frequency_penalty": 0.0,
  "system_fingerprint": "fp_50cad350e4",
  "input_user": null,
  "service_tier": "default",
  "tools": null,
  "metadata": {},
  "choices": [
      "index": 0,
      "message": {
        "content": "Mind of circuits hum,  \nLearning patterns in silence—  \nFuture's quiet spark.",
        "role": "assistant",
        "tool_calls": null,
        "function_call": null
      "finish_reason": "stop",
      "logprobs": null
  ],
  "response_format": null
