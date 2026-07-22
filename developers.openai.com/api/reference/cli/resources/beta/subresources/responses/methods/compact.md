<!-- source: https://developers.openai.com/api/reference/cli/resources/beta/subresources/responses/methods/compact/ -->

[API Reference](/api/reference/cli)

[Beta](/api/reference/cli/resources/beta)

[Responses](/api/reference/cli/resources/beta/subresources/responses)

# Compact a response

$ openai beta:responses compact

POST/responses/compact

Compact a conversation. Returns a compacted response object.

Learn when and how to compact long-running conversations in the [conversation state guide](https://platform.openai.com/docs/guides/conversation-state#managing-the-context-window). For ZDR-compatible compaction details, see [Compaction (advanced)](https://platform.openai.com/docs/guides/conversation-state#compaction-advanced).

##### ParametersExpand Collapse

--model: "gpt-5.6-sol" or "gpt-5.6-terra" or "gpt-5.6-luna" or 92 more or string

Body param: Model ID used to generate the response, like `gpt-5` or `o3`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points. Refer to the [model guide](https://platform.openai.com/docs/models) to browse and compare available models.

--input: optional string or array of [BetaResponseInputItem](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_item%20%3E%20(schema))

Body param: Text, image, or file inputs to the model, used to generate a response

--instructions: optional string

Body param: A system (or developer) message inserted into the model’s context.
When used along with `previous_response_id`, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

--previous-response-id: optional string

Body param: The unique ID of the previous response to the model. Use this to create multi-turn conversations. Learn more about [conversation state](https://platform.openai.com/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

--prompt-cache-key: optional string

Body param: A key to use when reading from or writing to the prompt cache.

--prompt-cache-options: optional object { mode, ttl }

Body param: Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](https://platform.openai.com/docs/guides/prompt-caching) for current details.

Deprecated--prompt-cache-retention: optional "in\_memory" or "24h"

Body param: How long to retain a prompt cache entry created by this request.

--service-tier: optional "auto" or "default" or "flex" or "priority"

Body param: The service tier to use for this request.

--beta: optional array of "responses\_multi\_agent=v1"

Header param: Optional beta features to enable for this request.

##### ReturnsExpand Collapse

beta\_compacted\_response: object { id, created\_at, object, 2 more }

id: string

The unique identifier for the compacted response.

created\_at: number

Unix timestamp (in seconds) when the compacted conversation was created.

object: "response.compaction"

The object type. Always `response.compaction`.

output: array of [BetaResponseOutputItem](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

The compacted list of output items. This is a list of all user messages, followed by a single compaction item.

beta\_response\_output\_message: object { id, content, role, 4 more }

id: string

content: array of [BetaResponseOutputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  or [BetaResponseOutputRefusal](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }

beta\_response\_output\_text: object { annotations, text, type, logprobs }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

file\_citation: object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

url\_citation: object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

container\_file\_citation: object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

file\_path: object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs: optional array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

beta\_response\_output\_refusal: object { refusal, type }

refusal: string

type: "refusal"

role: "assistant"

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "message"

agent: optional object { agent\_name }

agent\_name: string

phase: optional "commentary" or "final\_answer"

"commentary"

"final\_answer"

beta\_response\_file\_search\_tool\_call: object { id, queries, status, 3 more }

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

queries: array of string

status: "in\_progress" or "searching" or "completed" or 2 more

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

agent: optional object { agent\_name }

agent\_name: string

results: optional array of object { attributes, file\_id, filename, 2 more }

attributes: optional map[string or number or boolean]

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

file\_id: optional string

filename: optional string

score: optional number

text: optional string

beta\_response\_function\_tool\_call: object { arguments, call\_id, name, 6 more }

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

arguments: string

A JSON string of the arguments to pass to the function.

call\_id: string

name: string

The name of the function to run.

type: "function\_call"

The type of the function tool call. Always `function_call`.

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

beta\_response\_function\_tool\_call\_output\_item: object { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

output: string or array of [BetaResponseInputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the function call generated by your code.

string output: string

A string of the output of the function call.

output content list: array of [BetaResponseInputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function call.

beta\_response\_input\_text: object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

beta\_response\_input\_image: object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id: optional string

image\_url: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

beta\_response\_input\_file: object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

agent\_message: object { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

content: array of [BetaResponseInputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseOutputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  or object { text, type }  or 7 more

Encrypted content sent between agents.

beta\_response\_input\_text: object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

beta\_response\_output\_text: object { annotations, text, type, logprobs }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

file\_citation: object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

url\_citation: object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

container\_file\_citation: object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

file\_path: object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs: optional array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: object { text, type }

A text content.

text: string

type: "text"

summary\_text: object { text, type }

A summary text from the model.

text: string

type: "summary\_text"

reasoning\_text: object { text, type }

text: string

type: "reasoning\_text"

beta\_response\_output\_refusal: object { refusal, type }

refusal: string

type: "refusal"

beta\_response\_input\_image: object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id: optional string

image\_url: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

computer\_screenshot: object { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" or "high" or "auto" or "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string

image\_url: string

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

beta\_response\_input\_file: object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

encrypted\_content: object { encrypted\_content, type }

encrypted\_content: string

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The type of the item. Always `agent_message`.

agent: optional object { agent\_name }

agent\_name: string

multi\_agent\_call: object { id, action, arguments, 3 more }

id: string

The unique ID of the multi-agent call item.

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

The multi-agent action to execute.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: string

The JSON string of arguments generated for the action.

call\_id: string

type: "multi\_agent\_call"

The type of the multi-agent call. Always `multi_agent_call`.

agent: optional object { agent\_name }

agent\_name: string

multi\_agent\_call\_output: object { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

output: array of [BetaResponseOutputText](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

file\_citation: object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

url\_citation: object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

container\_file\_citation: object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

file\_path: object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs: optional array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

type: "multi\_agent\_call\_output"

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_function\_web\_search: object { id, action, status, 2 more }

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

search: object { type, queries, query, sources }

type: "search"

queries: optional array of string

Deprecatedquery: optional string

sources: optional array of object { type, url }

type: "url"

url: string

open\_page: object { type, url }

type: "open\_page"

url: optional string

find\_in\_page: object { pattern, type, url }

pattern: string

type: "find\_in\_page"

url: string

status: "in\_progress" or "searching" or "completed" or "failed"

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_computer\_tool\_call: object { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

call\_id: string

pending\_safety\_checks: array of object { id, code, message }

id: string

code: optional string

message: optional string

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

"computer\_call"

action: optional object { button, type, x, 2 more }  or object { keys, type, x, y }  or object { path, type, keys }  or 6 more

click: object { button, type, x, 2 more }

button: "left" or "right" or "wheel" or 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

"left"

"right"

"wheel"

"back"

"forward"

type: "click"

Specifies the event type. For a click action, this property is always `click`.

x: number

The x-coordinate where the click occurred.

y: number

The y-coordinate where the click occurred.

keys: optional array of string

The keys being held while clicking.

double\_click: object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

drag: object { path, type, keys }

A drag action.

path: array of object { x, y }

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: number

The x-coordinate.

y: number

The y-coordinate.

type: "drag"

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: optional array of string

The keys being held while dragging the mouse.

keypress: object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

move: object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

screenshot: object { type }

A screenshot action.

scroll: object { scroll\_x, scroll\_y, type, 3 more }

A scroll action.

scroll\_x: number

The horizontal scroll distance.

scroll\_y: number

The vertical scroll distance.

type: "scroll"

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: number

The x-coordinate where the scroll occurred.

y: number

The y-coordinate where the scroll occurred.

keys: optional array of string

The keys being held while scrolling.

type: object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

wait: object { type }

A wait action.

actions: optional array of [BetaComputerAction](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

click: object { button, type, x, 2 more }

button: "left" or "right" or "wheel" or 2 more

Indicates which mouse button was pressed during the click. One of `left`, `right`, `wheel`, `back`, or `forward`.

"left"

"right"

"wheel"

"back"

"forward"

type: "click"

Specifies the event type. For a click action, this property is always `click`.

x: number

The x-coordinate where the click occurred.

y: number

The y-coordinate where the click occurred.

keys: optional array of string

The keys being held while clicking.

double\_click: object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

drag: object { path, type, keys }

A drag action.

path: array of object { x, y }

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: number

The x-coordinate.

y: number

The y-coordinate.

type: "drag"

Specifies the event type. For a drag action, this property is always set to `drag`.

keys: optional array of string

The keys being held while dragging the mouse.

keypress: object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

move: object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

screenshot: object { type }

A screenshot action.

scroll: object { scroll\_x, scroll\_y, type, 3 more }

A scroll action.

scroll\_x: number

The horizontal scroll distance.

scroll\_y: number

The vertical scroll distance.

type: "scroll"

Specifies the event type. For a scroll action, this property is always set to `scroll`.

x: number

The x-coordinate where the scroll occurred.

y: number

The y-coordinate where the scroll occurred.

keys: optional array of string

The keys being held while scrolling.

type: object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

wait: object { type }

A wait action.

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_computer\_tool\_call\_output\_item: object { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

output: object { type, file\_id, image\_url }

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: optional string

image\_url: optional string

status: "completed" or "incomplete" or "failed" or "in\_progress"

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

acknowledged\_safety\_checks: optional array of object { id, code, message }

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

code: optional string

message: optional string

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_reasoning\_item: object { id, summary, type, 4 more }

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

summary: array of object { text, type }

text: string

type: "summary\_text"

type: "reasoning"

agent: optional object { agent\_name }

agent\_name: string

content: optional array of object { text, type }

text: string

type: "reasoning\_text"

encrypted\_content: optional string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

program: object { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

code: string

fingerprint: string

type: "program"

The type of the item. Always `program`.

agent: optional object { agent\_name }

agent\_name: string

program\_output: object { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

result: string

status: "completed" or "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_tool\_search\_call: object { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string

execution: "server" or "client"

"server"

"client"

status: "in\_progress" or "completed" or "incomplete"

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: "tool\_search\_call"

The type of the item. Always `tool_search_call`.

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_tool\_search\_output\_item: object { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string

execution: "server" or "client"

"server"

"client"

status: "in\_progress" or "completed" or "incomplete"

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: array of [BetaTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The loaded tool definitions returned by tool search.

beta\_function\_tool: object { name, parameters, strict, 5 more }

name: string

parameters: map[unknown]

strict: boolean

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

beta\_file\_search\_tool: object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

Comparison Filter: object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

Compound Filter: object { filters, type }

filters: array of object { key, type, value }  or unknown

Comparison Filter: object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_1: unknown

type: "and" or "or"

"and"

"or"

max\_num\_results: optional number

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

hybrid\_search: optional object { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker: optional "auto" or "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold: optional number

beta\_computer\_tool: object { type }

type: "computer"

beta\_computer\_use\_preview\_tool: object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

beta\_web\_search\_tool: object { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

allowed\_domains: optional array of string

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

city: optional string

country: optional string

region: optional string

timezone: optional string

type: optional "approximate"

"approximate"

mcp: object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

MCP allowed tools: array of string

A string array of allowed tool names

MCP tool filter: object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

headers: optional map[string]

require\_approval: optional object { always, never }  or "always" or "never"

MCP tool approval filter: object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

MCP tool approval setting: "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

code\_interpreter: object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

union\_member\_0: string

The container ID.

CodeInterpreterToolAuto: object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

name: string

value: string

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

programmatic\_tool\_calling: object { type }

image\_generation: object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-2" or 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

local\_shell: object { type }

A tool that allows the model to execute shell commands in a local environment.

beta\_function\_shell\_tool: object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

beta\_container\_auto: object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

name: string

value: string

skills: optional array of [BetaSkillReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

beta\_skill\_reference: object { skill\_id, type, version }

skill\_id: string

type: "skill\_reference"

version: optional string

beta\_inline\_skill: object { description, name, source, type }

description: string

name: string

source: object { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

beta\_local\_environment: object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

beta\_container\_reference: object { container\_id, type }

container\_id: string

type: "container\_reference"

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

beta\_namespace\_tool: object { description, name, tools, type }

description: string

name: string

tools: array of object { name, type, allowed\_callers, 5 more }  or [BetaCustomTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more }

function: object { name, type, allowed\_callers, 5 more }

name: string

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

beta\_tool\_search\_tool: object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

beta\_web\_search\_preview\_tool: object { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

type: "approximate"

city: optional string

country: optional string

region: optional string

timezone: optional string

beta\_apply\_patch\_tool: object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

additional\_tools: object { id, role, tools, 2 more }

id: string

The unique ID of the additional tools item.

role: "unknown" or "user" or "assistant" or 5 more

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: array of [BetaTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))

The additional tool definitions made available at this item.

beta\_function\_tool: object { name, parameters, strict, 5 more }

name: string

parameters: map[unknown]

strict: boolean

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

beta\_file\_search\_tool: object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

Comparison Filter: object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

Compound Filter: object { filters, type }

filters: array of object { key, type, value }  or unknown

Comparison Filter: object { key, type, value }

key: string

type: "eq" or "ne" or "gt" or 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string or number or boolean or array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_2: boolean

union\_member\_3: array of string or number

union\_member\_0: string

union\_member\_1: number

union\_member\_1: unknown

type: "and" or "or"

"and"

"or"

max\_num\_results: optional number

ranking\_options: optional object { hybrid\_search, ranker, score\_threshold }

hybrid\_search: optional object { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker: optional "auto" or "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold: optional number

beta\_computer\_tool: object { type }

type: "computer"

beta\_computer\_use\_preview\_tool: object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

beta\_web\_search\_tool: object { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" or "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters: optional object { allowed\_domains }

allowed\_domains: optional array of string

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { city, country, region, 2 more }

city: optional string

country: optional string

region: optional string

timezone: optional string

type: optional "approximate"

"approximate"

mcp: object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

MCP allowed tools: array of string

A string array of allowed tool names

MCP tool filter: object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading: optional boolean

headers: optional map[string]

require\_approval: optional object { always, never }  or "always" or "never"

MCP tool approval filter: object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

MCP tool approval setting: "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

code\_interpreter: object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

union\_member\_0: string

The container ID.

CodeInterpreterToolAuto: object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

name: string

value: string

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

programmatic\_tool\_calling: object { type }

image\_generation: object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Allows to set transparency for the background of the generated image(s).
This parameter is only supported for GPT image models that support
transparent backgrounds. Must be one of `transparent`, `opaque`, or
`auto` (default value). When `auto` is used, the model will
automatically determine the best background for the image.

`gpt-image-2` and `gpt-image-2-2026-04-21` do not support
transparent backgrounds. Requests with `background` set to
`transparent` will return an error for these models; use `opaque` or
`auto` instead.

If `transparent`, the output format needs to support transparency,
so it should be set to either `png` (default value) or `webp`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-2" or 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

local\_shell: object { type }

A tool that allows the model to execute shell commands in a local environment.

beta\_function\_shell\_tool: object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

beta\_container\_auto: object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

beta\_container\_network\_policy\_disabled: object { type }

type: "disabled"

beta\_container\_network\_policy\_allowlist: object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

name: string

value: string

skills: optional array of [BetaSkillReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

beta\_skill\_reference: object { skill\_id, type, version }

skill\_id: string

type: "skill\_reference"

version: optional string

beta\_inline\_skill: object { description, name, source, type }

description: string

name: string

source: object { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

beta\_local\_environment: object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

beta\_container\_reference: object { container\_id, type }

container\_id: string

type: "container\_reference"

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

beta\_namespace\_tool: object { description, name, tools, type }

description: string

name: string

tools: array of object { name, type, allowed\_callers, 5 more }  or [BetaCustomTool](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more }

function: object { name, type, allowed\_callers, 5 more }

name: string

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

beta\_custom\_tool: object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

text: object { type }

Unconstrained free-form text.

grammar: object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

beta\_tool\_search\_tool: object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

beta\_web\_search\_preview\_tool: object { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" or "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types: optional array of "text" or "image"

"text"

"image"

search\_context\_size: optional "low" or "medium" or "high"

"low"

"medium"

"high"

user\_location: optional object { type, city, country, 2 more }

type: "approximate"

city: optional string

country: optional string

region: optional string

timezone: optional string

beta\_apply\_patch\_tool: object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_compaction\_item: object { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

image\_generation\_call: object { id, result, status, 2 more }

An image generation request made by the model.

id: string

result: string

status: "in\_progress" or "completed" or "generating" or "failed"

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

agent: optional object { agent\_name }

agent\_name: string

beta\_response\_code\_interpreter\_tool\_call: object { id, code, container\_id, 4 more }

id: string

code: string

container\_id: string

outputs: array of object { logs, type }  or object { type, url }

logs: object { logs, type }

logs: string

type: "logs"

image: object { type, url }

type: "image"

url: string

status: "in\_progress" or "completed" or "incomplete" or 2 more

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

agent: optional object { agent\_name }

agent\_name: string

local\_shell\_call: object { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

action: object { command, env, type, 3 more }

command: array of string

env: map[string]

type: "exec"

timeout\_ms: optional number

user: optional string

working\_directory: optional string

call\_id: string

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

agent: optional object { agent\_name }

agent\_name: string

local\_shell\_call\_output: object { id, output, type, 2 more }

The output of a local shell tool call.

id: string

output: string

type: "local\_shell\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

beta\_response\_function\_shell\_tool\_call: object { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

action: object { commands, max\_output\_length, timeout\_ms }

commands: array of string

max\_output\_length: number

Optional maximum number of characters to return from each command.

timeout\_ms: number

Optional timeout in milliseconds for the commands.

call\_id: string

environment: [BetaResponseLocalEnvironment](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  or [BetaResponseContainerReference](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }

Represents the use of a local environment to perform shell actions.

beta\_response\_local\_environment: object { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

beta\_response\_container\_reference: object { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

beta\_response\_function\_shell\_tool\_call\_output: object { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

max\_output\_length: number

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: array of object { outcome, stderr, stdout, created\_by }

An array of shell call output contents

outcome: object { type }  or object { exit\_code, type }

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

timeout: object { type }

Indicates that the shell call exceeded its configured time limit.

exit: object { exit\_code, type }

exit\_code: number

Exit code from the shell process.

type: "exit"

stderr: string

The standard error output that was captured.

stdout: string

The standard output that was captured.

created\_by: optional string

The identifier of the actor that created the item.

status: "in\_progress" or "completed" or "incomplete"

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call\_output"

The type of the shell call output. Always `shell_call_output`.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

beta\_response\_apply\_patch\_tool\_call: object { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

call\_id: string

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

create\_file: object { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

delete\_file: object { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

update\_file: object { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to update.

type: "update\_file"

Update an existing file with the provided diff.

status: "in\_progress" or "completed"

"in\_progress"

"completed"

type: "apply\_patch\_call"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

beta\_response\_apply\_patch\_tool\_call\_output: object { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

call\_id: string

status: "completed" or "failed"

"completed"

"failed"

type: "apply\_patch\_call\_output"

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call output.

output: optional string

Optional textual output returned by the apply patch tool.

mcp\_call: object { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_call"

agent: optional object { agent\_name }

agent\_name: string

approval\_request\_id: optional string

error: optional string

output: optional string

status: optional "in\_progress" or "completed" or "incomplete" or 2 more

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

mcp\_list\_tools: object { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

server\_label: string

tools: array of object { input\_schema, name, annotations, description }

input\_schema: unknown

name: string

annotations: optional unknown

description: optional string

type: "mcp\_list\_tools"

agent: optional object { agent\_name }

agent\_name: string

error: optional string

mcp\_approval\_request: object { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent: optional object { agent\_name }

agent\_name: string

mcp\_approval\_response: object { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

agent: optional object { agent\_name }

agent\_name: string

reason: optional string

beta\_response\_custom\_tool\_call: object { call\_id, input, name, 5 more }

call\_id: string

An identifier used to map this custom tool call to a tool call output.

input: string

The input for the custom tool call generated by the model.

name: string

The name of the custom tool being called.

type: "custom\_tool\_call"

The type of the custom tool call. Always `custom_tool_call`.

id: optional string

The unique ID of the custom tool call in the OpenAI platform.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

direct: object { type }

program: object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the custom tool being called.

beta\_response\_custom\_tool\_call\_output\_item: [BetaResponseCustomToolCallOutput](/api/reference/cli/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

created\_by: optional string

The identifier of the actor that created the item.

usage: object { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Token accounting for the compaction pass, including cached, reasoning, and total tokens.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: object { cache\_write\_tokens, cached\_tokens }

A detailed breakdown of the input tokens.

cache\_write\_tokens: number

The number of input tokens that were written to the cache.

cached\_tokens: number

The number of tokens that were retrieved from the cache.
[More on prompt caching](https://platform.openai.com/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: object { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

### Compact a response

CLI Tool

openai beta:responses compact \
  --api-key 'My API Key' \
  --model gpt-5.6-sol

  "id": "resp_001",
  "object": "response.compaction",
  "created_at": 1764967971,
  "output": [
      "id": "msg_000",
      "type": "message",
      "status": "completed",
      "content": [
          "type": "input_text",
          "text": "Create a simple landing page for a dog petting cafe."
      ],
      "role": "user"
    },
      "id": "cmp_001",
      "type": "compaction",
      "encrypted_content": "gAAAAABpM0Yj-...="
  ],
  "usage": {
    "input_tokens": 139,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 438,
    "output_tokens_details": {
      "reasoning_tokens": 64
    },
    "total_tokens": 577

  "id": "resp_001",
  "object": "response.compaction",
  "created_at": 1764967971,
  "output": [
      "id": "msg_000",
      "type": "message",
      "status": "completed",
      "content": [
          "type": "input_text",
          "text": "Create a simple landing page for a dog petting cafe."
      ],
      "role": "user"
    },
      "id": "cmp_001",
      "type": "compaction",
      "encrypted_content": "gAAAAABpM0Yj-...="
  ],
  "usage": {
    "input_tokens": 139,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 438,
    "output_tokens_details": {
      "reasoning_tokens": 64
    },
    "total_tokens": 577
