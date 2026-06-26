<!-- source: https://developers.openai.com/api/reference/python/resources/chat/subresources/completions/methods/list/ -->

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

# List Chat Completions

chat.completions.list(CompletionListParams\*\*kwargs)  -> SyncCursorPage[[ChatCompletion](/api/reference/python/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema))]

GET/chat/completions

List stored Chat Completions. Only Chat Completions that have been stored
with the `store` parameter set to `true` will be returned.

##### ParametersExpand Collapse

after: Optional[str]

Identifier for the last chat completion from the previous pagination request.

limit: Optional[int]

Number of Chat Completions to retrieve.

metadata: Optional[Metadata]

A list of metadata keys to filter the Chat Completions by. Example:

`metadata[key1]=value1&metadata[key2]=value2`

model: Optional[str]

The model used to generate the Chat Completions.

order: Optional[Literal["asc", "desc"]]

Sort order for Chat Completions by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

One of the following:

"asc"

"desc"

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

### List Chat Completions

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

completions = client.chat.completions.list()
print(completions)

  "object": "list",
  "data": [
      "object": "chat.completion",
      "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
      "model": "gpt-5.4",
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
  ],
  "first_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "last_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "has_more": false

##### Returns Examples

  "object": "list",
  "data": [
      "object": "chat.completion",
      "id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
      "model": "gpt-5.4",
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
  ],
  "first_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "last_id": "chatcmpl-AyPNinnUqUDYo9SAdA52NobMflmj2",
  "has_more": false
