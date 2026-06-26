<!-- source: https://developers.openai.com/api/reference/cli/resources/chat/subresources/completions/methods/list/ -->

[Skip to content](#_top)

[API Reference](/api/reference/cli)

[Chat](/api/reference/cli/resources/chat)

[Completions](/api/reference/cli/resources/chat/subresources/completions)

Copy Markdown

Open in **Claude**

Open in **ChatGPT**

Open in **Cursor**

---

**Copy Markdown**

**View as Markdown**

# List Chat Completions

$ openai chat:completions list

GET/chat/completions

List stored Chat Completions. Only Chat Completions that have been stored
with the `store` parameter set to `true` will be returned.

##### ParametersExpand Collapse

--after: optional string

Identifier for the last chat completion from the previous pagination request.

--limit: optional number

Number of Chat Completions to retrieve.

--metadata: optional map[string]

A list of metadata keys to filter the Chat Completions by. Example:

`metadata[key1]=value1&metadata[key2]=value2`

--model: optional string

The model used to generate the Chat Completions.

--order: optional "asc" or "desc"

Sort order for Chat Completions by timestamp. Use `asc` for ascending order or `desc` for descending order. Defaults to `asc`.

##### ReturnsExpand Collapse

ChatCompletionList: object { data, first\_id, has\_more, 2 more }

An object representing a list of Chat Completions.

data: array of [ChatCompletion](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion%20%3E%20(schema)) { id, choices, created, 6 more }

An array of chat completion objects.

id: string

A unique identifier for the chat completion.

choices: array of object { finish\_reason, index, logprobs, message }

A list of chat completion choices. Can be more than one if `n` is greater than 1.

finish\_reason: "stop" or "length" or "tool\_calls" or 2 more

The reason the model stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
`length` if the maximum number of tokens specified in the request was reached,
`content_filter` if content was omitted due to a flag from our content filters,
`tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
Read the [Model Spec](https://model-spec.openai.com/2025-12-18.html) for more.

"stop"

"length"

"tool\_calls"

"content\_filter"

"function\_call"

index: number

The index of the choice in the list of choices.

logprobs: object { content, refusal }

Log probability information for the choice.

content: array of [ChatCompletionTokenLogprob](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs }

A list of message content tokens with log probability information.

token: string

The token.

bytes: array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: array of object { token, bytes, logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: string

The token.

bytes: array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

refusal: array of [ChatCompletionTokenLogprob](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_token_logprob%20%3E%20(schema)) { token, bytes, logprob, top\_logprobs }

A list of message refusal tokens with log probability information.

token: string

The token.

bytes: array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

top\_logprobs: array of object { token, bytes, logprob }

List of the most likely tokens and their log probability, at this token position. The number of entries may be fewer than the requested `top_logprobs`.

token: string

The token.

bytes: array of number

A list of integers representing the UTF-8 bytes representation of the token. Useful in instances where characters are represented by multiple tokens and their byte representations must be combined to generate the correct text representation. Can be `null` if there is no bytes representation for the token.

logprob: number

The log probability of this token, if it is within the top 20 most likely tokens. Otherwise, the value `-9999.0` is used to signify that the token is very unlikely.

message: object { content, refusal, role, 4 more }

A chat completion message generated by the model.

content: string

The contents of the message.

refusal: string

The refusal message generated by the model.

role: "assistant"

The role of the author of this message.

annotations: optional array of object { type, url\_citation }

Annotations for the message, when applicable, as when using the
[web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

type: "url\_citation"

The type of the URL citation. Always `url_citation`.

url\_citation: object { end\_index, start\_index, title, url }

A URL citation when using web search.

end\_index: number

The index of the last character of the URL citation in the message.

start\_index: number

The index of the first character of the URL citation in the message.

title: string

The title of the web resource.

url: string

The URL of the web resource.

audio: optional object { id, data, expires\_at, transcript }

If the audio output modality is requested, this object contains data
about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

id: string

Unique identifier for this audio response.

data: string

Base64 encoded audio bytes generated by the model, in the format
specified in the request.

expires\_at: number

The Unix timestamp (in seconds) for when this audio response will
no longer be accessible on the server for use in multi-turn
conversations.

transcript: string

Transcript of the audio generated by the model.

Deprecatedfunction\_call: optional object { arguments, name }

Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

arguments: string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: string

The name of the function to call.

tool\_calls: optional array of [ChatCompletionMessageToolCall](/api/reference/cli/resources/chat#(resource)%20chat.completions%20%3E%20(model)%20chat_completion_message_tool_call%20%3E%20(schema))

The tool calls generated by the model, such as function calls.

chat\_completion\_message\_function\_tool\_call: object { id, function, type }

A call to a function tool created by the model.

id: string

The ID of the tool call.

function: object { arguments, name }

The function that the model called.

arguments: string

The arguments to call the function with, as generated by the model in JSON format. Note that the model does not always generate valid JSON, and may hallucinate parameters not defined by your function schema. Validate the arguments in your code before calling your function.

name: string

The name of the function to call.

type: "function"

The type of the tool. Currently, only `function` is supported.

chat\_completion\_message\_custom\_tool\_call: object { id, custom, type }

A call to a custom tool created by the model.

id: string

The ID of the tool call.

custom: object { input, name }

The custom tool that the model called.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool to call.

type: "custom"

The type of the tool. Always `custom`.

created: number

The Unix timestamp (in seconds) of when the chat completion was created.

model: string

The model used for the chat completion.

object: "chat.completion"

The object type, which is always `chat.completion`.

moderation: optional object { input, output }

Moderation results for the request input and generated output, if moderated
completions were requested.

input: object { model, results, type }  or object { code, message, type }

Moderation for the request input.

moderation\_results: object { model, results, type }

Successful moderation results for the request input or generated output.

model: string

The moderation model used to generate the results.

results: array of object { categories, category\_applied\_input\_types, category\_scores, 3 more }

A list of moderation results.

categories: map[boolean]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: map[array of "text" or "image"]

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: map[number]

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

type: "moderation\_results"

The object type, which is always `moderation_results`.

error: object { code, message, type }

An error produced while attempting moderation.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which is always `error`.

output: object { model, results, type }  or object { code, message, type }

Moderation for the generated output.

moderation\_results: object { model, results, type }

Successful moderation results for the request input or generated output.

model: string

The moderation model used to generate the results.

results: array of object { categories, category\_applied\_input\_types, category\_scores, 3 more }

A list of moderation results.

categories: map[boolean]

A dictionary of moderation categories to booleans, True if the input is flagged under this category.

category\_applied\_input\_types: map[array of "text" or "image"]

Which modalities of input are reflected by the score for each category.

"text"

"image"

category\_scores: map[number]

A dictionary of moderation categories to scores.

flagged: boolean

A boolean indicating whether the content was flagged by any category.

model: string

The moderation model that produced this result.

type: "moderation\_result"

The object type, which was always `moderation_result` for successful moderation results.

type: "moderation\_results"

The object type, which is always `moderation_results`.

error: object { code, message, type }

An error produced while attempting moderation.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which is always `error`.

service\_tier: optional "auto" or "default" or "flex" or 2 more

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](https://platform.openai.com/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

"auto"

"default"

"flex"

"scale"

"priority"

Deprecatedsystem\_fingerprint: optional string

This fingerprint represents the backend configuration that the model runs with.

Can be used in conjunction with the `seed` request parameter to understand when backend changes have been made that might impact determinism.

usage: optional object { completion\_tokens, prompt\_tokens, total\_tokens, 2 more }

Usage statistics for the completion request.

completion\_tokens: number

Number of tokens in the generated completion.

prompt\_tokens: number

Number of tokens in the prompt.

total\_tokens: number

Total number of tokens used in the request (prompt + completion).

completion\_tokens\_details: optional object { accepted\_prediction\_tokens, audio\_tokens, reasoning\_tokens, rejected\_prediction\_tokens }

Breakdown of tokens used in a completion.

accepted\_prediction\_tokens: optional number

When using Predicted Outputs, the number of tokens in the
prediction that appeared in the completion.

audio\_tokens: optional number

Audio input tokens generated by the model.

reasoning\_tokens: optional number

Tokens generated by the model for reasoning.

rejected\_prediction\_tokens: optional number

When using Predicted Outputs, the number of tokens in the
prediction that did not appear in the completion. However, like
reasoning tokens, these tokens are still counted in the total
completion tokens for purposes of billing, output, and context window
limits.

prompt\_tokens\_details: optional object { audio\_tokens, cached\_tokens }

Breakdown of tokens used in the prompt.

audio\_tokens: optional number

Audio input tokens present in the prompt.

cached\_tokens: optional number

Cached tokens present in the prompt.

first\_id: string

The identifier of the first chat completion in the data array.

has\_more: boolean

Indicates whether there are more Chat Completions available.

last\_id: string

The identifier of the last chat completion in the data array.

object: "list"

The type of this object. It is always set to “list”.

### List Chat Completions

CLI Tool

HTTPHTTP

HTTPHTTP

TypeScriptTypeScript

PythonPython

JavaJava

GoGo

RubyRuby

CLI ToolCLI Tool

openai chat:completions list \
  --api-key 'My API Key'

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
