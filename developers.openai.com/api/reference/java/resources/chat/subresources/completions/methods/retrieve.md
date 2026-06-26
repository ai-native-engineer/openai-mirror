<!-- source: https://developers.openai.com/api/reference/java/resources/chat/subresources/completions/methods/retrieve/ -->

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

# Get chat completion

[ChatCompletion](/api/reference/java/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) chat().completions().retrieve(ChatCompletionRetrieveParamsparams = ChatCompletionRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/chat/completions/{completion\_id}

Get a stored chat completion. Only Chat Completions that have been created
with the `store` parameter set to `true` will be returned.

##### ParametersExpand Collapse

ChatCompletionRetrieveParams params

Optional<String> completionId

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

### Get chat completion

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
import com.openai.models.chat.completions.ChatCompletion;
import com.openai.models.chat.completions.ChatCompletionRetrieveParams;

public final class Main {
    private Main() {}

    public static void main(String[] args) {
        OpenAIClient client = OpenAIOkHttpClient.fromEnv();

        ChatCompletion chatCompletion = client.chat().completions().retrieve("completion_id");

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
