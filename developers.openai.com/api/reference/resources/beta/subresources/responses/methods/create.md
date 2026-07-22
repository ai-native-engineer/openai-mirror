<!-- source: https://developers.openai.com/api/reference/resources/beta/subresources/responses/methods/create/ -->

[API Reference](/api/reference)

[Beta](/api/reference/resources/beta)

[Responses](/api/reference/resources/beta/subresources/responses)

# Create a model response

POST/responses

Creates a model response. Provide [text](/docs/guides/text) or
[image](/docs/guides/images) inputs to generate [text](/docs/guides/text)
or [JSON](/docs/guides/structured-outputs) outputs. Have the model call
your own [custom code](/docs/guides/function-calling) or use built-in
[tools](/docs/guides/tools) like [web search](/docs/guides/tools-web-search)
or [file search](/docs/guides/tools-file-search) to use your own data
as input for the model’s response.

##### Header ParametersExpand Collapse

"openai-beta": optional array of "responses\_multi\_agent=v1"

##### Body ParametersJSONExpand Collapse

background: optional boolean

Whether to run the model response in the background.
[Learn more](/docs/guides/background).

context\_management: optional array of object { type, compact\_threshold }

Context management configuration for this request.

type: string

The context management entry type. Currently only ‘compaction’ is supported.

compact\_threshold: optional number

Token threshold at which compaction should be triggered for this entry.

minimum1000

conversation: optional string or [BetaResponseConversationParam](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_conversation_param%20%3E%20(schema)) { id }

The conversation that this response belongs to. Items from this conversation are prepended to `input_items` for this response request.
Input items and output items from this response are automatically added to this conversation after this response completes.

ConversationID = string

The unique ID of the conversation.

BetaResponseConversationParam object { id }

The conversation that this response belongs to.

id: string

The unique ID of the conversation.

include: optional array of [BetaResponseIncludable](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))

Specify additional output data to include in the model response. Currently supported values are:

* `web_search_call.action.sources`: Include the sources of the web search tool call.
* `code_interpreter_call.outputs`: Includes the outputs of python code execution in code interpreter tool call items.
* `computer_call_output.output.image_url`: Include image urls from the computer call output.
* `file_search_call.results`: Include the search results of the file search tool call.
* `message.input_image.image_url`: Include image urls from the input message.
* `message.output_text.logprobs`: Include logprobs with assistant messages.
* `reasoning.encrypted_content`: Includes an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (like when the `store` parameter is set to `false`, or when an organization is enrolled in the zero data retention program).

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

input: optional string or array of [BetaEasyInputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, agent, 2 more }  or [BetaResponseOutputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  or 32 more

Text, image, or file inputs to the model, used to generate a response.

Learn more:

* [Text inputs and outputs](/docs/guides/text)
* [Image inputs](/docs/guides/images)
* [File inputs](/docs/guides/pdf-files)
* [Conversation state](/docs/guides/conversation-state)
* [Function calling](/docs/guides/function-calling)

TextInput = string

A text input to the model, equivalent to a text input with the
`user` role.

InputItemList = array of [BetaEasyInputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, agent, 2 more }  or [BetaResponseOutputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  or 32 more

A list of one or many input items to the model, containing
different content types.

BetaEasyInputMessage object { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string or [BetaResponseInputMessageContentList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

TextInput = string

BetaResponseInputMessageContentList = array of [BetaResponseInputContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: optional "commentary" or "final\_answer"

"commentary"

"final\_answer"

type: optional "message"

The type of the message input. Always `message`.

Message object { content, role, agent, 2 more }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

role: "user" or "system" or "developer"

"user"

"system"

"developer"

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: optional "message"

BetaResponseOutputMessage object { id, content, role, 4 more }

id: string

content: array of [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [BetaResponseOutputRefusal](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }

BetaResponseOutputText object { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

BetaResponseOutputRefusal object { refusal, type }

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

FileSearchCall object { id, queries, status, 3 more }

[file search guide](/docs/guides/tools-file-search) for more information.

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

string

number

boolean

file\_id: optional string

filename: optional string

score: optional number

formatfloat

text: optional string

ComputerCall object { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](/docs/guides/tools-computer-use) for more information.

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

action: optional [BetaComputerAction](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

actions: optional [BetaComputerActionList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

agent: optional object { agent\_name }

agent\_name: string

ComputerCallOutput object { call\_id, output, type, 4 more }

The output of a computer tool call.

call\_id: string

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: optional string

image\_url: optional string

type: "computer\_call\_output"

id: optional string

The ID of the computer tool call output.

acknowledged\_safety\_checks: optional array of object { id, code, message }

The safety checks reported by the API that have been acknowledged by the developer.

id: string

code: optional string

message: optional string

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

WebSearchCall object { id, action, status, 2 more }

[web search guide](/docs/guides/tools-web-search) for more information.

id: string

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

Search object { type, queries, query, sources }

type: "search"

queries: optional array of string

Deprecatedquery: optional string

sources: optional array of object { type, url }

type: "url"

url: string

OpenPage object { type, url }

type: "open\_page"

url: optional string

FindInPage object { pattern, type, url }

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

FunctionCall object { arguments, call\_id, name, 6 more }

[function calling guide](/docs/guides/function-calling) for more information.

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { call\_id, output, type, 4 more }

The output of a function tool call.

call\_id: string

maxLength64

minLength1

output: string or array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [BetaResponseInputFileContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function tool call.

string

A JSON string of the output of the function tool call.

array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [BetaResponseInputFileContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

An array of content outputs (text, image, file) for the function tool call.

BetaResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

text: string

maxLength10485760

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision)

type: "input\_image"

detail: optional "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

file\_id: optional string

image\_url: optional string

maxLength20971520

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputFileContent object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

type: "function\_call\_output"

id: optional string

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

AgentMessage object { author, content, recipient, 3 more }

A message routed between agents.

author: string

content: array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or object { encrypted\_content, type }

Plaintext, image, or encrypted content sent between agents.

BetaResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

text: string

maxLength10485760

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision)

type: "input\_image"

detail: optional "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

file\_id: optional string

image\_url: optional string

maxLength20971520

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

EncryptedContent object { encrypted\_content, type }

encrypted\_content: string

maxLength10485760

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The item type. Always `agent_message`.

id: optional string

The unique ID of this agent message item.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCall object { action, arguments, call\_id, 3 more }

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: string

The action arguments as a JSON string.

call\_id: string

maxLength64

minLength1

type: "multi\_agent\_call"

The item type. Always `multi_agent_call`.

id: optional string

The unique ID of this multi-agent call.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCallOutput object { action, call\_id, output, 3 more }

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

maxLength64

minLength1

output: array of object { text, type, annotations }

text: string

The text content.

maxLength10485760

type: "output\_text"

The content type. Always `output_text`.

annotations: optional array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }

Citations associated with the text content.

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

minimum0

type: "file\_citation"

The citation type. Always `file_citation`.

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

The index of the last character of the citation in the message.

minimum0

start\_index: number

The index of the first character of the citation in the message.

minimum0

title: string

The title of the cited resource.

type: "url\_citation"

The citation type. Always `url_citation`.

url: string

The URL of the cited resource.

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

The ID of the container.

end\_index: number

The index of the last character of the citation in the message.

minimum0

file\_id: string

filename: string

start\_index: number

The index of the first character of the citation in the message.

minimum0

type: "container\_file\_citation"

The citation type. Always `container_file_citation`.

type: "multi\_agent\_call\_output"

The item type. Always `multi_agent_call_output`.

id: optional string

The unique ID of this multi-agent call output.

agent: optional object { agent\_name }

agent\_name: string

ToolSearchCall object { arguments, type, id, 4 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id: optional string

The unique ID of this tool search call.

agent: optional object { agent\_name }

agent\_name: string

call\_id: optional string

maxLength64

minLength1

execution: optional "server" or "client"

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

ToolSearchOutput object { tools, type, id, 4 more }

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by the tool search output.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id: optional string

The unique ID of this tool search output.

agent: optional object { agent\_name }

agent\_name: string

call\_id: optional string

maxLength64

minLength1

execution: optional "server" or "client"

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools object { role, tools, type, 2 more }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

A list of additional tools made available at this item.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id: optional string

The unique ID of this additional tools item.

agent: optional object { agent\_name }

agent\_name: string

Reasoning object { id, summary, type, 4 more }

[managing context](/docs/guides/conversation-state).

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

Compaction object { encrypted\_content, type, id, agent }

A compaction item generated by the [`v1/responses/compact` API](/docs/api-reference/responses/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength10485760

type: "compaction"

id: optional string

The ID of the compaction item.

agent: optional object { agent\_name }

agent\_name: string

ImageGenerationCall object { id, result, status, 2 more }

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

CodeInterpreterCall object { id, code, container\_id, 4 more }

id: string

code: string

container\_id: string

outputs: array of object { logs, type }  or object { type, url }

Logs object { logs, type }

logs: string

type: "logs"

Image object { type, url }

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

LocalShellCall object { id, action, call\_id, 3 more }

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

LocalShellCallOutput object { id, output, type, 2 more }

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

ShellCall object { action, call\_id, type, 5 more }

A tool representing a request to execute one or more shell commands.

action: object { commands, max\_output\_length, timeout\_ms }

commands: array of string

Ordered shell commands for the execution environment to run.

max\_output\_length: optional number

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: optional number

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

maxLength64

minLength1

type: "shell\_call"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

environment: optional [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

The environment to execute the shell commands in.

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

ShellCallOutput object { call\_id, output, type, 5 more }

The streamed output items emitted by a shell tool call.

call\_id: string

maxLength64

minLength1

output: array of [BetaResponseFunctionShellCallOutputContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout }

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: object { type }  or object { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

exit\_code: number

The exit code returned by the shell process.

type: "exit"

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id: optional string

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

max\_output\_length: optional number

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall object { call\_id, operation, status, 4 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

maxLength64

minLength1

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile object { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile object { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile object { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" or "completed"

"in\_progress"

"completed"

type: "apply\_patch\_call"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

ApplyPatchCallOutput object { call\_id, status, type, 4 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

maxLength64

minLength1

status: "completed" or "failed"

"completed"

"failed"

type: "apply\_patch\_call\_output"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

output: optional string

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools object { id, server\_label, tools, 3 more }

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

McpApprovalRequest object { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent: optional object { agent\_name }

agent\_name: string

McpApprovalResponse object { approval\_request\_id, approve, type, 3 more }

A response to an MCP approval request.

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

reason: optional string

McpCall object { id, arguments, name, 7 more }

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

CustomToolCallOutput object { call\_id, output, type, 3 more }

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id: optional string

The unique ID of the custom tool call output in the OpenAI platform.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

CustomToolCall object { call\_id, input, name, 5 more }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CompactionTrigger object { type, agent }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

agent: optional object { agent\_name }

agent\_name: string

ItemReference object { id, agent, type }

An internal identifier for an item to reference.

id: string

The ID of the item to reference.

agent: optional object { agent\_name }

agent\_name: string

type: optional "item\_reference"

The type of item to reference. Always `item_reference`.

Program object { id, call\_id, code, 3 more }

id: string

The unique ID of this program item.

call\_id: string

maxLength64

minLength1

code: string

maxLength10485760

fingerprint: string

maxLength10485760

type: "program"

The item type. Always `program`.

agent: optional object { agent\_name }

agent\_name: string

ProgramOutput object { id, call\_id, result, 3 more }

id: string

The unique ID of this program output item.

call\_id: string

maxLength64

minLength1

result: string

maxLength10485760

status: "completed" or "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

agent: optional object { agent\_name }

agent\_name: string

instructions: optional string

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

max\_output\_tokens: optional number

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](/docs/guides/reasoning).

minimum16

max\_tool\_calls: optional number

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

metadata: optional map[string]

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: optional "gpt-5.6-sol" or "gpt-5.6-terra" or "gpt-5.6-luna" or 92 more or string

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](/docs/models)
to browse and compare available models.

"gpt-5.6-sol" or "gpt-5.6-terra" or "gpt-5.6-luna" or 92 more

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](/docs/models)
to browse and compare available models.

"gpt-5.6-sol"

"gpt-5.6-terra"

"gpt-5.6-luna"

"gpt-5.4"

"gpt-5.4-mini"

"gpt-5.4-nano"

"gpt-5.4-mini-2026-03-17"

"gpt-5.4-nano-2026-03-17"

"gpt-5.3-chat-latest"

"gpt-5.2"

"gpt-5.2-2025-12-11"

"gpt-5.2-chat-latest"

"gpt-5.2-pro"

"gpt-5.2-pro-2025-12-11"

"gpt-5.1"

"gpt-5.1-2025-11-13"

"gpt-5.1-codex"

"gpt-5.1-mini"

"gpt-5.1-chat-latest"

"gpt-5"

"gpt-5-mini"

"gpt-5-nano"

"gpt-5-2025-08-07"

"gpt-5-mini-2025-08-07"

"gpt-5-nano-2025-08-07"

"gpt-5-chat-latest"

"gpt-4.1"

"gpt-4.1-mini"

"gpt-4.1-nano"

"gpt-4.1-2025-04-14"

"gpt-4.1-mini-2025-04-14"

"gpt-4.1-nano-2025-04-14"

"o4-mini"

"o4-mini-2025-04-16"

"o3"

"o3-2025-04-16"

"o3-mini"

"o3-mini-2025-01-31"

"o1"

"o1-2024-12-17"

"o1-preview"

"o1-preview-2024-09-12"

"o1-mini"

"o1-mini-2024-09-12"

"gpt-4o"

"gpt-4o-2024-11-20"

"gpt-4o-2024-08-06"

"gpt-4o-2024-05-13"

"gpt-4o-audio-preview"

"gpt-4o-audio-preview-2024-10-01"

"gpt-4o-audio-preview-2024-12-17"

"gpt-4o-audio-preview-2025-06-03"

"gpt-4o-mini-audio-preview"

"gpt-4o-mini-audio-preview-2024-12-17"

"gpt-4o-search-preview"

"gpt-4o-mini-search-preview"

"gpt-4o-search-preview-2025-03-11"

"gpt-4o-mini-search-preview-2025-03-11"

"chatgpt-4o-latest"

"codex-mini-latest"

"gpt-4o-mini"

"gpt-4o-mini-2024-07-18"

"gpt-4-turbo"

"gpt-4-turbo-2024-04-09"

"gpt-4-0125-preview"

"gpt-4-turbo-preview"

"gpt-4-1106-preview"

"gpt-4-vision-preview"

"gpt-4"

"gpt-4-0314"

"gpt-4-0613"

"gpt-4-32k"

"gpt-4-32k-0314"

"gpt-4-32k-0613"

"gpt-3.5-turbo"

"gpt-3.5-turbo-16k"

"gpt-3.5-turbo-0301"

"gpt-3.5-turbo-0613"

"gpt-3.5-turbo-1106"

"gpt-3.5-turbo-0125"

"gpt-3.5-turbo-16k-0613"

"o1-pro"

"o1-pro-2025-03-19"

"o3-pro"

"o3-pro-2025-06-10"

"o3-deep-research"

"o3-deep-research-2025-06-26"

"o4-mini-deep-research"

"o4-mini-deep-research-2025-06-26"

"computer-use-preview"

"computer-use-preview-2025-03-11"

"gpt-5-codex"

"gpt-5-pro"

"gpt-5-pro-2025-10-06"

"gpt-5.1-codex-max"

string

moderation: optional object { model, policy }

Configuration for running moderation on the input and output of this response.

model: string

The moderation model to use for moderated completions, e.g. ‘omni-moderation-latest’.

policy: optional object { input, output }

The policy to apply to moderated response input and output.

input: optional object { mode }

The moderation policy for the response input.

mode: "score" or "block"

"score"

"block"

output: optional object { mode }

The moderation policy for the response output.

mode: "score" or "block"

"score"

"block"

multi\_agent: optional object { enabled, max\_concurrent\_subagents }

Configuration for server-hosted multi-agent execution.

enabled: boolean

Whether to enable server-hosted multi-agent execution for this response.

max\_concurrent\_subagents: optional number

`max_concurrent_subagents` sets the maximum number of subagents that can be active simultaneously across the entire agent tree. It includes all descendants—children, grandchildren, and deeper subagents—but excludes the root agent.
The API does not impose a fixed upper bound on this setting. The default is `3`, which is recommended for most workloads. Multi-agent runs also have no fixed limit on tree depth or the total number of subagents created during a run.

minimum1

parallel\_tool\_calls: optional boolean

Whether to allow the model to run tool calls in parallel.

previous\_response\_id: optional string

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: optional [BetaResponsePrompt](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema)) { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables: optional map[string or [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } ]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

version: optional string

Optional version of the prompt template.

prompt\_cache\_key: optional string

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](/docs/guides/prompt-caching).

prompt\_cache\_options: optional object { mode, ttl }

Options for prompt caching. Supported for `gpt-5.6` and later models. By default, OpenAI automatically chooses one implicit cache breakpoint. You can add explicit breakpoints to content blocks with `prompt_cache_breakpoint`. Each request can write up to four breakpoints. For cache matching, OpenAI considers up to the latest 80 breakpoints in the conversation, without a content-block lookback limit. Set `mode` to `explicit` to disable the implicit breakpoint. The `ttl` defaults to `30m`, which is currently the only supported value. See the [prompt caching guide](/docs/guides/prompt-caching) for current details.

mode: optional "implicit" or "explicit"

Controls whether OpenAI automatically creates an implicit cache breakpoint. Defaults to `implicit`. With `implicit`, OpenAI creates one implicit breakpoint and writes up to the latest three explicit breakpoints in the request. With `explicit`, OpenAI does not create an implicit breakpoint and writes up to the latest four explicit breakpoints. If there are no explicit breakpoints, the request does not use prompt caching.

"implicit"

"explicit"

ttl: optional "30m"

The minimum lifetime applied to every implicit and explicit cache breakpoint written by the request. Defaults to `30m`, which is currently the only supported value. The backend may retain cache entries for longer.

Deprecatedprompt\_cache\_retention: optional "in\_memory" or "24h"

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

"in\_memory"

"24h"

reasoning: optional object { context, effort, generate\_summary, 2 more }

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: optional "auto" or "current\_turn" or "all\_turns"

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: optional "none" or "minimal" or "low" or 4 more

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

"max"

Deprecatedgenerate\_summary: optional "auto" or "concise" or "detailed"

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: optional string or "standard" or "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

string

"standard" or "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: optional "auto" or "concise" or "detailed"

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: optional string

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: optional "auto" or "default" or "flex" or 2 more

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

"auto"

"default"

"flex"

"scale"

"priority"

store: optional boolean

Whether to store the generated model response for later retrieval via
API.

stream: optional boolean

If set to true, the model response data will be streamed to the client
as it is generated using [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format).
See the [Streaming section below](/docs/api-reference/responses-streaming)
for more information.

stream\_options: optional object { include\_obfuscation }

Options for streaming responses. Only set this when you set `stream: true`.

include\_obfuscation: optional boolean

When true, stream obfuscation will be enabled. Stream obfuscation adds
random characters to an `obfuscation` field on streaming delta events to
normalize payload sizes as a mitigation to certain side-channel attacks.
These obfuscation fields are included by default, but add a small amount
of overhead to the data stream. You can set `include_obfuscation` to
false to optimize for bandwidth if you trust the network links between
your application and the OpenAI API.

temperature: optional number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

text: optional [BetaResponseTextConfig](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema)) { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](/docs/guides/text)
* [Structured Outputs](/docs/guides/structured-outputs)

format: optional [BetaResponseFormatTextConfig](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Text object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

BetaResponseFormatTextJSONSchemaConfig object { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

JSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

verbosity: optional "low" or "medium" or "high"

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

"low"

"medium"

"high"

tool\_choice: optional [BetaToolChoiceOptions](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) or [BetaToolChoiceAllowed](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  or [BetaToolChoiceTypes](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  or 6 more

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

BetaToolChoiceOptions = "none" or "auto" or "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

BetaToolChoiceAllowed object { mode, tools, type }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" or "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: array of map[unknown]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

BetaToolChoiceTypes object { type }

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](/docs/guides/tools).

type: "file\_search" or "web\_search\_preview" or "computer" or 5 more

The type of hosted tool the model should to use. Learn more about
[built-in tools](/docs/guides/tools).

Allowed values are:

* `file_search`
* `web_search_preview`
* `computer`
* `computer_use_preview`
* `computer_use`
* `code_interpreter`
* `image_generation`

"file\_search"

"web\_search\_preview"

"computer"

"computer\_use\_preview"

"computer\_use"

"web\_search\_preview\_2025\_03\_11"

"image\_generation"

"code\_interpreter"

BetaToolChoiceFunction object { name, type }

Use this option to force the model to call a specific function.

name: string

type: "function"

For function calling, the type is always `function`.

BetaToolChoiceMcp object { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name: optional string

The name of the tool to call on the server.

BetaToolChoiceCustom object { name, type }

Use this option to force the model to call a specific custom tool.

name: string

The name of the custom tool to call.

type: "custom"

For custom tool calling, the type is always `custom`.

BetaSpecificProgrammaticToolCallingParam object { type }

type: "programmatic\_tool\_calling"

The tool to call. Always `programmatic_tool_calling`.

BetaToolChoiceApplyPatch object { type }

Forces the model to call the apply\_patch tool when executing a tool call.

type: "apply\_patch"

The tool to call. Always `apply_patch`.

BetaToolChoiceShell object { type }

Forces the model to call the shell tool when a tool call is required.

type: "shell"

The tool to call. Always `shell`.

tools: optional array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](/docs/guides/tools-web-search)
  or [file search](/docs/guides/tools-file-search). Learn more about
  [built-in tools](/docs/guides/tools).
* **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](/docs/guides/tools-connectors-mcp).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](/docs/guides/function-calling). You can also use
  custom tools to call your own code.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

top\_logprobs: optional number

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

top\_p: optional number

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

Deprecatedtruncation: optional "auto" or "disabled"

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

Deprecateduser: optional string

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).

##### ReturnsExpand Collapse

BetaResponse object { id, created\_at, error, 32 more }

id: string

Unique identifier for this Response.

created\_at: number

Unix timestamp (in seconds) of when this Response was created.

formatunixtime

error: [BetaResponseError](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_error%20%3E%20(schema)) { code, message }

An error object returned when the model fails to generate a Response.

code: "server\_error" or "rate\_limit\_exceeded" or "invalid\_prompt" or 16 more

The error code for the response.

"server\_error"

"rate\_limit\_exceeded"

"invalid\_prompt"

"bio\_policy"

"vector\_store\_timeout"

"invalid\_image"

"invalid\_image\_format"

"invalid\_base64\_image"

"invalid\_image\_url"

"image\_too\_large"

"image\_too\_small"

"image\_parse\_error"

"image\_content\_policy\_violation"

"invalid\_image\_mode"

"image\_file\_too\_large"

"unsupported\_image\_media\_type"

"empty\_image\_file"

"failed\_to\_download\_image"

"image\_file\_not\_found"

message: string

A human-readable description of the error.

incomplete\_details: object { reason }

Details about why the response is incomplete.

reason: optional "max\_output\_tokens" or "content\_filter"

The reason why the response is incomplete.

"max\_output\_tokens"

"content\_filter"

instructions: string or array of [BetaEasyInputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, agent, 2 more }  or [BetaResponseOutputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  or 32 more

A system (or developer) message inserted into the model’s context.

When using along with `previous_response_id`, the instructions from a previous
response will not be carried over to the next response. This makes it simple
to swap out system (or developer) messages in new responses.

string

A text input to the model, equivalent to a text input with the
`developer` role.

InputItemList = array of [BetaEasyInputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_easy_input_message%20%3E%20(schema)) { content, role, phase, type }  or object { content, role, agent, 2 more }  or [BetaResponseOutputMessage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  or 32 more

A list of one or many input items to the model, containing
different content types.

BetaEasyInputMessage object { content, role, phase, type }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role. Messages with the
`assistant` role are presumed to have been generated by the model in previous
interactions.

content: string or [BetaResponseInputMessageContentList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

Text, image, or audio input to the model, used to generate a response.
Can also contain previous assistant responses.

TextInput = string

BetaResponseInputMessageContentList = array of [BetaResponseInputContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_content%20%3E%20(schema))

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

role: "user" or "assistant" or "system" or "developer"

The role of the message input. One of `user`, `assistant`, `system`, or
`developer`.

"user"

"assistant"

"system"

"developer"

phase: optional "commentary" or "final\_answer"

"commentary"

"final\_answer"

type: optional "message"

The type of the message input. Always `message`.

Message object { content, role, agent, 2 more }

A message input to the model with a role indicating instruction following
hierarchy. Instructions given with the `developer` or `system` role take
precedence over instructions given with the `user` role.

content: [BetaResponseInputMessageContentList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

role: "user" or "system" or "developer"

"user"

"system"

"developer"

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

type: optional "message"

BetaResponseOutputMessage object { id, content, role, 4 more }

id: string

content: array of [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [BetaResponseOutputRefusal](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }

BetaResponseOutputText object { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

BetaResponseOutputRefusal object { refusal, type }

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

FileSearchCall object { id, queries, status, 3 more }

[file search guide](/docs/guides/tools-file-search) for more information.

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

string

number

boolean

file\_id: optional string

filename: optional string

score: optional number

formatfloat

text: optional string

ComputerCall object { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](/docs/guides/tools-computer-use) for more information.

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

action: optional [BetaComputerAction](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

actions: optional [BetaComputerActionList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

agent: optional object { agent\_name }

agent\_name: string

ComputerCallOutput object { call\_id, output, type, 4 more }

The output of a computer tool call.

call\_id: string

maxLength64

minLength1

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id: optional string

image\_url: optional string

type: "computer\_call\_output"

id: optional string

The ID of the computer tool call output.

acknowledged\_safety\_checks: optional array of object { id, code, message }

The safety checks reported by the API that have been acknowledged by the developer.

id: string

code: optional string

message: optional string

agent: optional object { agent\_name }

agent\_name: string

status: optional "in\_progress" or "completed" or "incomplete"

The status of the message input. One of `in_progress`, `completed`, or `incomplete`. Populated when input items are returned via API.

"in\_progress"

"completed"

"incomplete"

WebSearchCall object { id, action, status, 2 more }

[web search guide](/docs/guides/tools-web-search) for more information.

id: string

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

Search object { type, queries, query, sources }

type: "search"

queries: optional array of string

Deprecatedquery: optional string

sources: optional array of object { type, url }

type: "url"

url: string

OpenPage object { type, url }

type: "open\_page"

url: optional string

FindInPage object { pattern, type, url }

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

FunctionCall object { arguments, call\_id, name, 6 more }

[function calling guide](/docs/guides/function-calling) for more information.

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { call\_id, output, type, 4 more }

The output of a function tool call.

call\_id: string

maxLength64

minLength1

output: string or array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [BetaResponseInputFileContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function tool call.

string

A JSON string of the output of the function tool call.

array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or [BetaResponseInputFileContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file_content%20%3E%20(schema)) { type, detail, file\_data, 4 more }

An array of content outputs (text, image, file) for the function tool call.

BetaResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

text: string

maxLength10485760

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision)

type: "input\_image"

detail: optional "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

file\_id: optional string

image\_url: optional string

maxLength20971520

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputFileContent object { type, detail, file\_data, 4 more }

type: "input\_file"

detail: optional "auto" or "low" or "high"

"auto"

"low"

"high"

file\_data: optional string

The base64-encoded data of the file to be sent to the model.

maxLength73400320

file\_id: optional string

file\_url: optional string

filename: optional string

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

type: "function\_call\_output"

id: optional string

The unique ID of the function tool call output. Populated when this item is returned via API.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the item. One of `in_progress`, `completed`, or `incomplete`. Populated when items are returned via API.

"in\_progress"

"completed"

"incomplete"

AgentMessage object { author, content, recipient, 3 more }

A message routed between agents.

author: string

content: array of [BetaResponseInputTextContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text_content%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImageContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image_content%20%3E%20(schema)) { type, detail, file\_id, 2 more }  or object { encrypted\_content, type }

Plaintext, image, or encrypted content sent between agents.

BetaResponseInputTextContent object { text, type, prompt\_cache\_breakpoint }

text: string

maxLength10485760

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImageContent object { type, detail, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision)

type: "input\_image"

detail: optional "low" or "high" or "auto" or "original"

"low"

"high"

"auto"

"original"

file\_id: optional string

image\_url: optional string

maxLength20971520

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

EncryptedContent object { encrypted\_content, type }

encrypted\_content: string

maxLength10485760

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The item type. Always `agent_message`.

id: optional string

The unique ID of this agent message item.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCall object { action, arguments, call\_id, 3 more }

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

The multi-agent action that was executed.

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

arguments: string

The action arguments as a JSON string.

call\_id: string

maxLength64

minLength1

type: "multi\_agent\_call"

The item type. Always `multi_agent_call`.

id: optional string

The unique ID of this multi-agent call.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCallOutput object { action, call\_id, output, 3 more }

action: "spawn\_agent" or "interrupt\_agent" or "list\_agents" or 3 more

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

maxLength64

minLength1

output: array of object { text, type, annotations }

text: string

The text content.

maxLength10485760

type: "output\_text"

The content type. Always `output_text`.

annotations: optional array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }

Citations associated with the text content.

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

minimum0

type: "file\_citation"

The citation type. Always `file_citation`.

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

The index of the last character of the citation in the message.

minimum0

start\_index: number

The index of the first character of the citation in the message.

minimum0

title: string

The title of the cited resource.

type: "url\_citation"

The citation type. Always `url_citation`.

url: string

The URL of the cited resource.

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

The ID of the container.

end\_index: number

The index of the last character of the citation in the message.

minimum0

file\_id: string

filename: string

start\_index: number

The index of the first character of the citation in the message.

minimum0

type: "container\_file\_citation"

The citation type. Always `container_file_citation`.

type: "multi\_agent\_call\_output"

The item type. Always `multi_agent_call_output`.

id: optional string

The unique ID of this multi-agent call output.

agent: optional object { agent\_name }

agent\_name: string

ToolSearchCall object { arguments, type, id, 4 more }

arguments: unknown

The arguments supplied to the tool search call.

type: "tool\_search\_call"

The item type. Always `tool_search_call`.

id: optional string

The unique ID of this tool search call.

agent: optional object { agent\_name }

agent\_name: string

call\_id: optional string

maxLength64

minLength1

execution: optional "server" or "client"

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the tool search call.

"in\_progress"

"completed"

"incomplete"

ToolSearchOutput object { tools, type, id, 4 more }

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by the tool search output.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "tool\_search\_output"

The item type. Always `tool_search_output`.

id: optional string

The unique ID of this tool search output.

agent: optional object { agent\_name }

agent\_name: string

call\_id: optional string

maxLength64

minLength1

execution: optional "server" or "client"

"server"

"client"

status: optional "in\_progress" or "completed" or "incomplete"

The status of the tool search output.

"in\_progress"

"completed"

"incomplete"

AdditionalTools object { role, tools, type, 2 more }

role: "developer"

The role that provided the additional tools. Only `developer` is supported.

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

A list of additional tools made available at this item.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "additional\_tools"

The item type. Always `additional_tools`.

id: optional string

The unique ID of this additional tools item.

agent: optional object { agent\_name }

agent\_name: string

Reasoning object { id, summary, type, 4 more }

[managing context](/docs/guides/conversation-state).

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

Compaction object { encrypted\_content, type, id, agent }

A compaction item generated by the [`v1/responses/compact` API](/docs/api-reference/responses/compact).

encrypted\_content: string

The encrypted content of the compaction summary.

maxLength10485760

type: "compaction"

id: optional string

The ID of the compaction item.

agent: optional object { agent\_name }

agent\_name: string

ImageGenerationCall object { id, result, status, 2 more }

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

CodeInterpreterCall object { id, code, container\_id, 4 more }

id: string

code: string

container\_id: string

outputs: array of object { logs, type }  or object { type, url }

Logs object { logs, type }

logs: string

type: "logs"

Image object { type, url }

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

LocalShellCall object { id, action, call\_id, 3 more }

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

LocalShellCallOutput object { id, output, type, 2 more }

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

ShellCall object { action, call\_id, type, 5 more }

A tool representing a request to execute one or more shell commands.

action: object { commands, max\_output\_length, timeout\_ms }

commands: array of string

Ordered shell commands for the execution environment to run.

max\_output\_length: optional number

Maximum number of UTF-8 characters to capture from combined stdout and stderr output.

timeout\_ms: optional number

Maximum wall-clock time in milliseconds to allow the shell commands to run.

call\_id: string

maxLength64

minLength1

type: "shell\_call"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

environment: optional [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

The environment to execute the shell commands in.

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

ShellCallOutput object { call\_id, output, type, 5 more }

The streamed output items emitted by a shell tool call.

call\_id: string

maxLength64

minLength1

output: array of [BetaResponseFunctionShellCallOutputContent](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_shell_call_output_content%20%3E%20(schema)) { outcome, stderr, stdout }

Captured chunks of stdout and stderr output, along with their associated outcomes.

outcome: object { type }  or object { exit\_code, type }

The exit or timeout outcome associated with this shell call.

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

exit\_code: number

The exit code returned by the shell process.

type: "exit"

stderr: string

Captured stderr output for the shell call.

maxLength10485760

stdout: string

Captured stdout output for the shell call.

maxLength10485760

type: "shell\_call\_output"

The type of the item. Always `shell_call_output`.

id: optional string

The unique ID of the shell tool call output. Populated when this item is returned via API.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

max\_output\_length: optional number

The maximum number of UTF-8 characters captured for this shell call’s combined output.

status: optional "in\_progress" or "completed" or "incomplete"

The status of the shell call output.

"in\_progress"

"completed"

"incomplete"

ApplyPatchCall object { call\_id, operation, status, 4 more }

A tool call representing a request to create, delete, or update files using diff patches.

call\_id: string

maxLength64

minLength1

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

The specific create, delete, or update instruction for the apply\_patch tool call.

CreateFile object { diff, path, type }

Instruction for creating a new file via the apply\_patch tool.

diff: string

Unified diff content to apply when creating the file.

maxLength10485760

path: string

Path of the file to create relative to the workspace root.

minLength1

type: "create\_file"

The operation type. Always `create_file`.

DeleteFile object { path, type }

Instruction for deleting an existing file via the apply\_patch tool.

path: string

Path of the file to delete relative to the workspace root.

minLength1

type: "delete\_file"

The operation type. Always `delete_file`.

UpdateFile object { diff, path, type }

Instruction for updating an existing file via the apply\_patch tool.

diff: string

Unified diff content to apply to the existing file.

maxLength10485760

path: string

Path of the file to update relative to the workspace root.

minLength1

type: "update\_file"

The operation type. Always `update_file`.

status: "in\_progress" or "completed"

"in\_progress"

"completed"

type: "apply\_patch\_call"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

ApplyPatchCallOutput object { call\_id, status, type, 4 more }

The streamed output emitted by an apply patch tool call.

call\_id: string

maxLength64

minLength1

status: "completed" or "failed"

"completed"

"failed"

type: "apply\_patch\_call\_output"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

output: optional string

Optional human-readable log text from the apply patch tool (e.g., patch results or errors).

maxLength10485760

McpListTools object { id, server\_label, tools, 3 more }

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

McpApprovalRequest object { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent: optional object { agent\_name }

agent\_name: string

McpApprovalResponse object { approval\_request\_id, approve, type, 3 more }

A response to an MCP approval request.

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

id: optional string

agent: optional object { agent\_name }

agent\_name: string

reason: optional string

McpCall object { id, arguments, name, 7 more }

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

CustomToolCallOutput object { call\_id, output, type, 3 more }

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

id: optional string

The unique ID of the custom tool call output in the OpenAI platform.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

CustomToolCall object { call\_id, input, name, 5 more }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CompactionTrigger object { type, agent }

Compacts the current context. Must be the final input item.

type: "compaction\_trigger"

The type of the item. Always `compaction_trigger`.

agent: optional object { agent\_name }

agent\_name: string

ItemReference object { id, agent, type }

An internal identifier for an item to reference.

id: string

The ID of the item to reference.

agent: optional object { agent\_name }

agent\_name: string

type: optional "item\_reference"

The type of item to reference. Always `item_reference`.

Program object { id, call\_id, code, 3 more }

id: string

The unique ID of this program item.

call\_id: string

maxLength64

minLength1

code: string

maxLength10485760

fingerprint: string

maxLength10485760

type: "program"

The item type. Always `program`.

agent: optional object { agent\_name }

agent\_name: string

ProgramOutput object { id, call\_id, result, 3 more }

id: string

The unique ID of this program output item.

call\_id: string

maxLength64

minLength1

result: string

maxLength10485760

status: "completed" or "incomplete"

The terminal status of the program output.

"completed"

"incomplete"

type: "program\_output"

The item type. Always `program_output`.

agent: optional object { agent\_name }

agent\_name: string

metadata: map[string]

format, and querying for objects via API or the dashboard.

Keys are strings with a maximum length of 64 characters. Values are strings
with a maximum length of 512 characters.

model: "gpt-5.6-sol" or "gpt-5.6-terra" or "gpt-5.6-luna" or 92 more or string

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](/docs/models)
to browse and compare available models.

"gpt-5.6-sol" or "gpt-5.6-terra" or "gpt-5.6-luna" or 92 more

Model ID used to generate the response, like `gpt-4o` or `o3`. OpenAI
offers a wide range of models with different capabilities, performance
characteristics, and price points. Refer to the [model guide](/docs/models)
to browse and compare available models.

"gpt-5.6-sol"

"gpt-5.6-terra"

"gpt-5.6-luna"

"gpt-5.4"

"gpt-5.4-mini"

"gpt-5.4-nano"

"gpt-5.4-mini-2026-03-17"

"gpt-5.4-nano-2026-03-17"

"gpt-5.3-chat-latest"

"gpt-5.2"

"gpt-5.2-2025-12-11"

"gpt-5.2-chat-latest"

"gpt-5.2-pro"

"gpt-5.2-pro-2025-12-11"

"gpt-5.1"

"gpt-5.1-2025-11-13"

"gpt-5.1-codex"

"gpt-5.1-mini"

"gpt-5.1-chat-latest"

"gpt-5"

"gpt-5-mini"

"gpt-5-nano"

"gpt-5-2025-08-07"

"gpt-5-mini-2025-08-07"

"gpt-5-nano-2025-08-07"

"gpt-5-chat-latest"

"gpt-4.1"

"gpt-4.1-mini"

"gpt-4.1-nano"

"gpt-4.1-2025-04-14"

"gpt-4.1-mini-2025-04-14"

"gpt-4.1-nano-2025-04-14"

"o4-mini"

"o4-mini-2025-04-16"

"o3"

"o3-2025-04-16"

"o3-mini"

"o3-mini-2025-01-31"

"o1"

"o1-2024-12-17"

"o1-preview"

"o1-preview-2024-09-12"

"o1-mini"

"o1-mini-2024-09-12"

"gpt-4o"

"gpt-4o-2024-11-20"

"gpt-4o-2024-08-06"

"gpt-4o-2024-05-13"

"gpt-4o-audio-preview"

"gpt-4o-audio-preview-2024-10-01"

"gpt-4o-audio-preview-2024-12-17"

"gpt-4o-audio-preview-2025-06-03"

"gpt-4o-mini-audio-preview"

"gpt-4o-mini-audio-preview-2024-12-17"

"gpt-4o-search-preview"

"gpt-4o-mini-search-preview"

"gpt-4o-search-preview-2025-03-11"

"gpt-4o-mini-search-preview-2025-03-11"

"chatgpt-4o-latest"

"codex-mini-latest"

"gpt-4o-mini"

"gpt-4o-mini-2024-07-18"

"gpt-4-turbo"

"gpt-4-turbo-2024-04-09"

"gpt-4-0125-preview"

"gpt-4-turbo-preview"

"gpt-4-1106-preview"

"gpt-4-vision-preview"

"gpt-4"

"gpt-4-0314"

"gpt-4-0613"

"gpt-4-32k"

"gpt-4-32k-0314"

"gpt-4-32k-0613"

"gpt-3.5-turbo"

"gpt-3.5-turbo-16k"

"gpt-3.5-turbo-0301"

"gpt-3.5-turbo-0613"

"gpt-3.5-turbo-1106"

"gpt-3.5-turbo-0125"

"gpt-3.5-turbo-16k-0613"

"o1-pro"

"o1-pro-2025-03-19"

"o3-pro"

"o3-pro-2025-06-10"

"o3-deep-research"

"o3-deep-research-2025-06-26"

"o4-mini-deep-research"

"o4-mini-deep-research-2025-06-26"

"computer-use-preview"

"computer-use-preview-2025-03-11"

"gpt-5-codex"

"gpt-5-pro"

"gpt-5-pro-2025-10-06"

"gpt-5.1-codex-max"

string

object: "response"

The object type of this resource - always set to `response`.

output: array of [BetaResponseOutputItem](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_item%20%3E%20(schema))

An array of content items generated by the model.

* The length and order of items in the `output` array is dependent
  on the model’s response.
* Rather than accessing the first item in the `output` array and
  assuming it’s an `assistant` message with the content generated by
  the model, you might consider using the `output_text` property where
  supported in SDKs.

BetaResponseOutputMessage object { id, content, role, 4 more }

id: string

content: array of [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or [BetaResponseOutputRefusal](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type }

BetaResponseOutputText object { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

BetaResponseOutputRefusal object { refusal, type }

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

FileSearchCall object { id, queries, status, 3 more }

[file search guide](/docs/guides/tools-file-search) for more information.

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

string

number

boolean

file\_id: optional string

filename: optional string

score: optional number

formatfloat

text: optional string

FunctionCall object { arguments, call\_id, name, 6 more }

[function calling guide](/docs/guides/function-calling) for more information.

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the function to run.

status: optional "in\_progress" or "completed" or "incomplete"

"in\_progress"

"completed"

"incomplete"

FunctionCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the function call generated by your code.

StringOutput = string

A string of the output of the function call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the function call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

AgentMessage object { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

content: array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }  or object { text, type }  or 7 more

Encrypted content sent between agents.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseOutputText object { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

Text object { text, type }

A text content.

text: string

type: "text"

SummaryText object { text, type }

A summary text from the model.

text: string

type: "summary\_text"

ReasoningText object { text, type }

text: string

type: "reasoning\_text"

BetaResponseOutputRefusal object { refusal, type }

refusal: string

type: "refusal"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

ComputerScreenshot object { detail, file\_id, image\_url, 2 more }

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

EncryptedContent object { encrypted\_content, type }

encrypted\_content: string

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The type of the item. Always `agent_message`.

agent: optional object { agent\_name }

agent\_name: string

MultiAgentCall object { id, action, arguments, 3 more }

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

MultiAgentCallOutput object { id, action, call\_id, 3 more }

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

output: array of [BetaResponseOutputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, logprobs, text, type }

annotations: array of object { file\_id, filename, index, type }  or object { end\_index, start\_index, title, 2 more }  or object { container\_id, end\_index, file\_id, 3 more }  or object { file\_id, index, type }

FileCitation object { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation object { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation object { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath object { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

logprobs: array of object { token, bytes, logprob, top\_logprobs }

token: string

bytes: array of number

logprob: number

top\_logprobs: array of object { token, bytes, logprob }

token: string

bytes: array of number

logprob: number

text: string

type: "output\_text"

type: "multi\_agent\_call\_output"

The type of the multi-agent result. Always `multi_agent_call_output`.

agent: optional object { agent\_name }

agent\_name: string

WebSearchCall object { id, action, status, 2 more }

[web search guide](/docs/guides/tools-web-search) for more information.

id: string

action: object { type, queries, query, sources }  or object { type, url }  or object { pattern, type, url }

Search object { type, queries, query, sources }

type: "search"

queries: optional array of string

Deprecatedquery: optional string

sources: optional array of object { type, url }

type: "url"

url: string

OpenPage object { type, url }

type: "open\_page"

url: optional string

FindInPage object { pattern, type, url }

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

ComputerCall object { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](/docs/guides/tools-computer-use) for more information.

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

action: optional [BetaComputerAction](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

actions: optional [BetaComputerActionList](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { Click, DoubleClick, Drag, 6 more }

Click object { button, type, x, 2 more }

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

DoubleClick object { keys, type, x, y }

A double click action.

keys: array of string

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag object { path, type, keys }

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

Keypress object { keys, type }

A collection of keypresses the model would like to perform.

keys: array of string

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move object { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys: optional array of string

The keys being held while moving the mouse.

Screenshot object { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll object { scroll\_x, scroll\_y, type, 3 more }

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

Type object { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait object { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

agent: optional object { agent\_name }

agent\_name: string

ComputerCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

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

Reasoning object { id, summary, type, 4 more }

[managing context](/docs/guides/conversation-state).

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

Program object { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

code: string

fingerprint: string

type: "program"

The type of the item. Always `program`.

agent: optional object { agent\_name }

agent\_name: string

ProgramOutput object { id, call\_id, result, 3 more }

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

ToolSearchCall object { id, arguments, call\_id, 5 more }

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

ToolSearchOutput object { id, call\_id, execution, 5 more }

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

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The loaded tool definitions returned by tool search.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

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

AdditionalTools object { id, role, tools, 2 more }

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

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

The additional tool definitions made available at this item.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent: optional object { agent\_name }

agent\_name: string

Compaction object { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

agent: optional object { agent\_name }

agent\_name: string

created\_by: optional string

The identifier of the actor that created the item.

ImageGenerationCall object { id, result, status, 2 more }

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

CodeInterpreterCall object { id, code, container\_id, 4 more }

id: string

code: string

container\_id: string

outputs: array of object { logs, type }  or object { type, url }

Logs object { logs, type }

logs: string

type: "logs"

Image object { type, url }

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

LocalShellCall object { id, action, call\_id, 3 more }

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

LocalShellCallOutput object { id, output, type, 2 more }

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

ShellCall object { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

action: object { commands, max\_output\_length, timeout\_ms }

commands: array of string

max\_output\_length: number

Optional maximum number of characters to return from each command.

timeout\_ms: number

Optional timeout in milliseconds for the commands.

call\_id: string

environment: [BetaResponseLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  or [BetaResponseContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }

Represents the use of a local environment to perform shell actions.

BetaResponseLocalEnvironment object { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

BetaResponseContainerReference object { container\_id, type }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

ShellCallOutput object { id, call\_id, max\_output\_length, 6 more }

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

Timeout object { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit object { exit\_code, type }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

ApplyPatchCall object { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

call\_id: string

operation: object { diff, path, type }  or object { path, type }  or object { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

CreateFile object { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

DeleteFile object { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

UpdateFile object { diff, path, type }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call.

ApplyPatchCallOutput object { id, call\_id, status, 5 more }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

created\_by: optional string

The ID of the entity that created this tool call output.

output: optional string

Optional textual output returned by the apply patch tool.

McpCall object { id, arguments, name, 7 more }

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

McpListTools object { id, server\_label, tools, 3 more }

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

McpApprovalRequest object { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent: optional object { agent\_name }

agent\_name: string

McpApprovalResponse object { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

agent: optional object { agent\_name }

agent\_name: string

reason: optional string

CustomToolCall object { call\_id, input, name, 5 more }

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

Direct object { type }

type: "direct"

Program object { caller\_id, type }

caller\_id: string

type: "program"

namespace: optional string

The namespace of the custom tool being called.

CustomToolCallOutput object { id, call\_id, output, 5 more }

id: string

The unique ID of the custom tool call output item.

call\_id: string

The call ID, used to map this custom tool call output to a custom tool call.

output: string or array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

The output from the custom tool call generated by your code.

StringOutput = string

A string of the output of the custom tool call.

OutputContentList = array of [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more }

Text, image, or file output of the custom tool call.

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

type: "custom\_tool\_call\_output"

The type of the custom tool call output. Always `custom_tool_call_output`.

agent: optional object { agent\_name }

agent\_name: string

caller: optional object { type }  or object { caller\_id, type }

Direct object { type }

type: "direct"

The caller type. Always `direct`.

Program object { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

created\_by: optional string

The identifier of the actor that created the item.

parallel\_tool\_calls: boolean

Whether to allow the model to run tool calls in parallel.

temperature: number

What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.
We generally recommend altering this or `top_p` but not both.

minimum0

maximum2

tool\_choice: [BetaToolChoiceOptions](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_options%20%3E%20(schema)) or [BetaToolChoiceAllowed](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_allowed%20%3E%20(schema)) { mode, tools, type }  or [BetaToolChoiceTypes](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool_choice_types%20%3E%20(schema)) { type }  or 6 more

How the model should select which tool (or tools) to use when generating
a response. See the `tools` parameter to see how to specify which tools
the model can call.

BetaToolChoiceOptions = "none" or "auto" or "required"

Controls which (if any) tool is called by the model.

`none` means the model will not call any tool and instead generates a message.

`auto` means the model can pick between generating a message or calling one or
more tools.

`required` means the model must call one or more tools.

"none"

"auto"

"required"

BetaToolChoiceAllowed object { mode, tools, type }

Constrains the tools available to the model to a pre-defined set.

mode: "auto" or "required"

Constrains the tools available to the model to a pre-defined set.

`auto` allows the model to pick from among the allowed tools and generate a
message.

`required` requires the model to call one or more of the allowed tools.

"auto"

"required"

tools: array of map[unknown]

A list of tool definitions that the model should be allowed to call.

For the Responses API, the list of tool definitions might look like:

  { "type": "function", "name": "get_weather" },
  { "type": "mcp", "server_label": "deepwiki" },
  { "type": "image_generation" }

type: "allowed\_tools"

Allowed tool configuration type. Always `allowed_tools`.

BetaToolChoiceTypes object { type }

Indicates that the model should use a built-in tool to generate a response.
[Learn more about built-in tools](/docs/guides/tools).

type: "file\_search" or "web\_search\_preview" or "computer" or 5 more

The type of hosted tool the model should to use. Learn more about
[built-in tools](/docs/guides/tools).

Allowed values are:

* `file_search`
* `web_search_preview`
* `computer`
* `computer_use_preview`
* `computer_use`
* `code_interpreter`
* `image_generation`

"file\_search"

"web\_search\_preview"

"computer"

"computer\_use\_preview"

"computer\_use"

"web\_search\_preview\_2025\_03\_11"

"image\_generation"

"code\_interpreter"

BetaToolChoiceFunction object { name, type }

Use this option to force the model to call a specific function.

name: string

type: "function"

For function calling, the type is always `function`.

BetaToolChoiceMcp object { server\_label, type, name }

Use this option to force the model to call a specific tool on a remote MCP server.

server\_label: string

The label of the MCP server to use.

type: "mcp"

For MCP tools, the type is always `mcp`.

name: optional string

The name of the tool to call on the server.

BetaToolChoiceCustom object { name, type }

Use this option to force the model to call a specific custom tool.

name: string

The name of the custom tool to call.

type: "custom"

For custom tool calling, the type is always `custom`.

BetaSpecificProgrammaticToolCallingParam object { type }

type: "programmatic\_tool\_calling"

The tool to call. Always `programmatic_tool_calling`.

BetaToolChoiceApplyPatch object { type }

Forces the model to call the apply\_patch tool when executing a tool call.

type: "apply\_patch"

The tool to call. Always `apply_patch`.

BetaToolChoiceShell object { type }

Forces the model to call the shell tool when a tool call is required.

type: "shell"

The tool to call. Always `shell`.

tools: array of object { name, parameters, strict, 5 more }  or object { type, vector\_store\_ids, filters, 2 more }  or object { type }  or 13 more

An array of tools the model may call while generating a response. You
can specify which tool to use by setting the `tool_choice` parameter.

We support the following categories of tools:

* **Built-in tools**: Tools that are provided by OpenAI that extend the
  model’s capabilities, like [web search](/docs/guides/tools-web-search)
  or [file search](/docs/guides/tools-file-search). Learn more about
  [built-in tools](/docs/guides/tools).
* **MCP Tools**: Integrations with third-party systems via custom MCP servers
  or predefined connectors such as Google Drive and SharePoint. Learn more about
  [MCP Tools](/docs/guides/tools-connectors-mcp).
* **Function calls (custom tools)**: Functions that are defined by you,
  enabling the model to call your own code with strongly typed arguments
  and outputs. Learn more about
  [function calling](/docs/guides/function-calling). You can also use
  custom tools to call your own code.

Function object { name, parameters, strict, 5 more }

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

FileSearch object { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: array of string

filters: optional object { key, type, value }  or object { filters, type }

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

CompoundFilter object { filters, type }

filters: array of object { key, type, value }  or unknown

ComparisonFilter object { key, type, value }

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

string

number

boolean

array of string or number

string

number

unknown

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

Computer object { type }

type: "computer"

ComputerUsePreview object { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" or "mac" or "linux" or 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

WebSearch object { type, filters, search\_context\_size, user\_location }

[web search tool](/docs/guides/tools-web-search).

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

Mcp object { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

allowed\_tools: optional array of string or object { read\_only, tool\_names }

McpAllowedTools = array of string

A string array of allowed tool names

McpToolFilter object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

authorization: optional string

connector\_id: optional "connector\_dropbox" or "connector\_gmail" or "connector\_googlecalendar" or 5 more

about service connectors [here](/docs/guides/tools-remote-mcp#connectors).

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

McpToolApprovalFilter object { always, never }

always: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

never: optional object { read\_only, tool\_names }

read\_only: optional boolean

tool\_names: optional array of string

McpToolApprovalSetting = "always" or "never"

Specify a single approval policy for all tools. One of `always` or
`never`. When set to `always`, all tools will require approval. When
set to `never`, all tools will not require approval.

"always"

"never"

server\_description: optional string

server\_url: optional string

tunnel\_id: optional string

CodeInterpreter object { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string or object { type, file\_ids, memory\_limit, network\_policy }

string

The container ID.

CodeInterpreterToolAuto object { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

ProgrammaticToolCalling object { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration object { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action: optional "generate" or "edit" or "auto"

"generate"

"edit"

"auto"

background: optional "transparent" or "opaque" or "auto"

Background type for the generated image. One of `transparent`,
`opaque`, or `auto`. Default: `auto`.

"transparent"

"opaque"

"auto"

input\_fidelity: optional "high" or "low"

"high"

"low"

input\_image\_mask: optional object { file\_id, image\_url }

file\_id: optional string

image\_url: optional string

model: optional string or "gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

string

"gpt-image-1" or "gpt-image-1-mini" or "gpt-image-1.5"

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-1.5"

moderation: optional "auto" or "low"

"auto"

"low"

output\_compression: optional number

minimum0

maximum100

output\_format: optional "png" or "webp" or "jpeg"

"png"

"webp"

"jpeg"

partial\_images: optional number

minimum0

maximum3

quality: optional "low" or "medium" or "high" or "auto"

"low"

"medium"

"high"

"auto"

size: optional string or "1024x1024" or "1024x1536" or "1536x1024" or "auto"

string

"1024x1024" or "1024x1536" or "1536x1024" or "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell object { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

Shell object { type, allowed\_callers, environment }

type: "shell"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

environment: optional [BetaContainerAuto](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  or [BetaLocalEnvironment](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  or [BetaContainerReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }

BetaContainerAuto object { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids: optional array of string

memory\_limit: optional "1g" or "4g" or "16g" or "64g"

"1g"

"4g"

"16g"

"64g"

network\_policy: optional [BetaContainerNetworkPolicyDisabled](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  or [BetaContainerNetworkPolicyAllowlist](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled object { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist object { allowed\_domains, type, domain\_secrets }

allowed\_domains: array of string

type: "allowlist"

domain\_secrets: optional array of [BetaContainerNetworkPolicyDomainSecret](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value }

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills: optional array of [BetaSkillReference](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  or [BetaInlineSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type }

BetaSkillReference object { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version: optional string

BetaInlineSkill object { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment object { type, skills }

type: "local"

skills: optional array of [BetaLocalSkill](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path }

description: string

name: string

path: string

BetaContainerReference object { container\_id, type }

container\_id: string

type: "container\_reference"

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

Namespace object { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: array of object { name, type, allowed\_callers, 5 more }  or object { name, type, allowed\_callers, 3 more }

Function object { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

output\_schema: optional map[unknown]

parameters: optional unknown

strict: optional boolean

Custom object { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

defer\_loading: optional boolean

description: optional string

format: optional object { type }  or object { definition, syntax, type }

Text object { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar object { definition, syntax, type }

definition: string

syntax: "lark" or "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

ToolSearch object { type, description, execution, parameters }

type: "tool\_search"

description: optional string

execution: optional "server" or "client"

"server"

"client"

parameters: optional unknown

WebSearchPreview object { type, search\_content\_types, search\_context\_size, user\_location }

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

ApplyPatch object { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers: optional array of "direct" or "programmatic"

"direct"

"programmatic"

top\_p: number

An alternative to sampling with temperature, called nucleus sampling,
where the model considers the results of the tokens with top\_p probability
mass. So 0.1 means only the tokens comprising the top 10% probability mass
are considered.

We generally recommend altering this or `temperature` but not both.

minimum0

maximum1

background: optional boolean

Whether to run the model response in the background.
[Learn more](/docs/guides/background).

completed\_at: optional number

Unix timestamp (in seconds) of when this Response was completed.
Only present when the status is `completed`.

formatunixtime

conversation: optional object { id }

The conversation that this response belonged to. Input items and output items from this response were automatically added to this conversation.

id: string

The unique ID of the conversation that this response was associated with.

max\_output\_tokens: optional number

An upper bound for the number of tokens that can be generated for a response, including visible output tokens and [reasoning tokens](/docs/guides/reasoning).

max\_tool\_calls: optional number

The maximum number of total calls to built-in tools that can be processed in a response. This maximum number applies across all built-in tool calls, not per individual tool. Any further attempts to call a tool by the model will be ignored.

moderation: optional object { input, output }

Moderation results for the response input and output, if moderated completions were requested.

input: object { categories, category\_applied\_input\_types, category\_scores, 3 more }  or object { code, message, type }

Moderation for the response input.

ModerationResult object { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

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

Error object { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

output: object { categories, category\_applied\_input\_types, category\_scores, 3 more }  or object { code, message, type }

Moderation for the response output.

ModerationResult object { categories, category\_applied\_input\_types, category\_scores, 3 more }

A moderation result produced for the response input or output.

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

Error object { code, message, type }

An error produced while attempting moderation for the response input or output.

code: string

The error code.

message: string

The error message.

type: "error"

The object type, which was always `error` for moderation failures.

output\_text: optional string

SDK-only convenience property that contains the aggregated text output
from all `output_text` items in the `output` array, if any are present.
Supported in the Python and JavaScript SDKs.

previous\_response\_id: optional string

The unique ID of the previous response to the model. Use this to
create multi-turn conversations. Learn more about
[conversation state](/docs/guides/conversation-state). Cannot be used in conjunction with `conversation`.

prompt: optional [BetaResponsePrompt](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_prompt%20%3E%20(schema)) { id, variables, version }

Reference to a prompt template and its variables.
[Learn more](/docs/guides/text?api-mode=responses#reusable-prompts).

id: string

The unique identifier of the prompt template to use.

variables: optional map[string or [BetaResponseInputText](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  or [BetaResponseInputImage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  or [BetaResponseInputFile](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } ]

Optional map of values to substitute in for variables in your
prompt. The substitution values can either be strings, or other
Response input types like images or files.

string

BetaResponseInputText object { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint: optional object { mode }

mode: "explicit"

BetaResponseInputImage object { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](/docs/guides/vision).

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

BetaResponseInputFile object { type, detail, file\_data, 4 more }

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

version: optional string

Optional version of the prompt template.

prompt\_cache\_key: optional string

Used by OpenAI to cache responses for similar requests to optimize your cache hit rates. Replaces the `user` field. [Learn more](/docs/guides/prompt-caching).

prompt\_cache\_options: optional object { mode, ttl }

The prompt-caching options that were applied to the response. Supported for `gpt-5.6` and later models.

mode: "implicit" or "explicit"

Whether implicit prompt-cache breakpoints were enabled.

"implicit"

"explicit"

ttl: "30m"

The minimum lifetime applied to each cache breakpoint.

Deprecatedprompt\_cache\_retention: optional "in\_memory" or "24h"

Deprecated. Use `prompt_cache_options.ttl` instead.

The retention policy for the prompt cache. Set to `24h` to enable extended prompt caching, which keeps cached prefixes active for longer, up to a maximum of 24 hours. [Learn more](/docs/guides/prompt-caching#prompt-cache-retention).
This field expresses a maximum retention policy, while
`prompt_cache_options.ttl` expresses a minimum cache lifetime. The two
fields are independent and do not interact.
For `gpt-5.5`, `gpt-5.5-pro`, and future models, only `24h` is supported.

For older models that support both `in_memory` and `24h`, the default depends on your organization’s data retention policy:

* Organizations without ZDR enabled default to `24h`.
* Organizations with ZDR enabled default to `in_memory` when `prompt_cache_retention` is not specified.

"in\_memory"

"24h"

reasoning: optional object { context, effort, generate\_summary, 2 more }

**gpt-5 and o-series models only**

Configuration options for
[reasoning models](https://platform.openai.com/docs/guides/reasoning).

context: optional "auto" or "current\_turn" or "all\_turns"

Controls which reasoning items are rendered back to the model on later turns.
When returned on a response, this is the effective reasoning context mode
used for the response.

"auto"

"current\_turn"

"all\_turns"

effort: optional "none" or "minimal" or "low" or 4 more

Constrains effort on reasoning for reasoning models. Currently supported
values are `none`, `minimal`, `low`, `medium`, `high`, `xhigh`, and `max`.
Reducing reasoning effort can result in faster responses and fewer tokens
used on reasoning in a response. Not all reasoning models support every
value. See the
[reasoning guide](https://platform.openai.com/docs/guides/reasoning)
for model-specific support.

"none"

"minimal"

"low"

"medium"

"high"

"xhigh"

"max"

Deprecatedgenerate\_summary: optional "auto" or "concise" or "detailed"

**Deprecated:** use `summary` instead.

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

"auto"

"concise"

"detailed"

mode: optional string or "standard" or "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

string

"standard" or "pro"

Controls the reasoning execution mode for the request.

When returned on a response, this is the effective execution mode.

"standard"

"pro"

summary: optional "auto" or "concise" or "detailed"

A summary of the reasoning performed by the model. This can be
useful for debugging and understanding the model’s reasoning process.
One of `auto`, `concise`, or `detailed`.

`concise` is supported for `computer-use-preview` models and all reasoning models after `gpt-5`.

"auto"

"concise"

"detailed"

safety\_identifier: optional string

A stable identifier used to help detect users of your application that may be violating OpenAI’s usage policies.
The IDs should be a string that uniquely identifies each user, with a maximum length of 64 characters. We recommend hashing their username or email address, in order to avoid sending us any identifying information. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).

maxLength64

service\_tier: optional "auto" or "default" or "flex" or 2 more

Specifies the processing type used for serving the request.

* If set to ‘auto’, then the request will be processed with the service tier configured in the Project settings. Unless otherwise configured, the Project will use ‘default’.
* If set to ‘default’, then the request will be processed with the standard pricing and performance for the selected model.
* If set to ‘[flex](/docs/guides/flex-processing)’ or ‘[priority](https://openai.com/api-priority-processing/)’, then the request will be processed with the corresponding service tier.
* When not set, the default behavior is ‘auto’.

When the `service_tier` parameter is set, the response body will include the `service_tier` value based on the processing mode actually used to serve the request. This response value may be different from the value set in the parameter.

"auto"

"default"

"flex"

"scale"

"priority"

status: optional [BetaResponseStatus](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_status%20%3E%20(schema))

The status of the response generation. One of `completed`, `failed`,
`in_progress`, `cancelled`, `queued`, or `incomplete`.

"completed"

"failed"

"in\_progress"

"cancelled"

"queued"

"incomplete"

text: optional [BetaResponseTextConfig](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_text_config%20%3E%20(schema)) { format, verbosity }

Configuration options for a text response from the model. Can be plain
text or structured JSON data. Learn more:

* [Text inputs and outputs](/docs/guides/text)
* [Structured Outputs](/docs/guides/structured-outputs)

format: optional [BetaResponseFormatTextConfig](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_format_text_config%20%3E%20(schema))

An object specifying the format that the model must output.

Configuring `{ "type": "json_schema" }` enables Structured Outputs,
which ensures the model will match your supplied JSON schema. Learn more in the
[Structured Outputs guide](/docs/guides/structured-outputs).

The default format is `{ "type": "text" }` with no additional options.

**Not recommended for gpt-4o and newer models:**

Setting to `{ "type": "json_object" }` enables the older JSON mode, which
ensures the message the model generates is valid JSON. Using `json_schema`
is preferred for models that support it.

Text object { type }

Default response format. Used to generate text responses.

type: "text"

The type of response format being defined. Always `text`.

BetaResponseFormatTextJSONSchemaConfig object { name, schema, type, 2 more }

JSON Schema response format. Used to generate structured JSON responses.
Learn more about [Structured Outputs](/docs/guides/structured-outputs).

name: string

The name of the response format. Must be a-z, A-Z, 0-9, or contain
underscores and dashes, with a maximum length of 64.

schema: map[unknown]

The schema for the response format, described as a JSON Schema object.
Learn how to build JSON schemas [here](https://json-schema.org/).

type: "json\_schema"

The type of response format being defined. Always `json_schema`.

description: optional string

A description of what the response format is for, used by the model to
determine how to respond in the format.

strict: optional boolean

Whether to enable strict schema adherence when generating the output.
If set to true, the model will always follow the exact schema defined
in the `schema` field. Only a subset of JSON Schema is supported when
`strict` is `true`. To learn more, read the [Structured Outputs
guide](/docs/guides/structured-outputs).

JSONObject object { type }

JSON object response format. An older method of generating JSON responses.
Using `json_schema` is recommended for models that support it. Note that the
model will not generate JSON without a system or user message instructing it
to do so.

type: "json\_object"

The type of response format being defined. Always `json_object`.

verbosity: optional "low" or "medium" or "high"

Constrains the verbosity of the model’s response. Lower values will result in
more concise responses, while higher values will result in more verbose responses.
Currently supported values are `low`, `medium`, and `high`.

"low"

"medium"

"high"

top\_logprobs: optional number

An integer between 0 and 20 specifying the maximum number of most likely
tokens to return at each token position, each with an associated log
probability. In some cases, the number of returned tokens may be fewer than
requested.

minimum0

maximum20

truncation: optional "auto" or "disabled"

The truncation strategy to use for the model response.

* `auto`: If the input to this Response exceeds
  the model’s context window size, the model will truncate the
  response to fit the context window by dropping items from the beginning of the conversation.
* `disabled` (default): If the input size will exceed the context window
  size for a model, the request will fail with a 400 error.

"auto"

"disabled"

usage: optional [BetaResponseUsage](/api/reference/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_usage%20%3E%20(schema)) { input\_tokens, input\_tokens\_details, output\_tokens, 2 more }

Represents token usage details including input tokens, output tokens,
a breakdown of output tokens, and the total tokens used.

input\_tokens: number

The number of input tokens.

input\_tokens\_details: object { cache\_write\_tokens, cached\_tokens }

A detailed breakdown of the input tokens.

cache\_write\_tokens: number

The number of input tokens that were written to the cache.

cached\_tokens: number

The number of tokens that were retrieved from the cache.
[More on prompt caching](/docs/guides/prompt-caching).

output\_tokens: number

The number of output tokens.

output\_tokens\_details: object { reasoning\_tokens }

A detailed breakdown of the output tokens.

reasoning\_tokens: number

The number of reasoning tokens.

total\_tokens: number

The total number of tokens used.

Deprecateduser: optional string

This field is being replaced by `safety_identifier` and `prompt_cache_key`. Use `prompt_cache_key` instead to maintain caching optimizations.
A stable identifier for your end-users.
Used to boost cache hit rates by better bucketing similar requests and to help OpenAI detect and prevent abuse. [Learn more](/docs/guides/safety-best-practices#safety-identifiers).

Text inputImage inputFile inputWeb searchFile searchStreamingFunctionsReasoning

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "input": "Tell me a three sentence bedtime story about a unicorn."
  }'

  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "completed_at": 1741476543,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "message",
      "id": "msg_67ccd2bf17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "In a peaceful grove beneath a silver moon, a unicorn named Lumina discovered a hidden pool that reflected the stars. As she dipped her horn into the water, the pool began to shimmer, revealing a pathway to a magical realm of endless night skies. Filled with wonder, Lumina whispered a wish for all who dream to find their own hidden magic, and as she glanced back, her hoofprints sparkled like stardust.",
          "annotations": []
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 36,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 87,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 123
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "input": [
        "role": "user",
        "content": [
          {"type": "input_text", "text": "what is in this image?"},
            "type": "input_image",
            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
  }'

  "id": "resp_67ccd3a9da748190baa7f1570fe91ac604becb25c45c1d41",
  "object": "response",
  "created_at": 1741476777,
  "status": "completed",
  "completed_at": 1741476778,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "message",
      "id": "msg_67ccd3acc8d48190a77525dc6de64b4104becb25c45c1d41",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The image depicts a scenic landscape with a wooden boardwalk or pathway leading through lush, green grass under a blue sky with some clouds. The setting suggests a peaceful natural area, possibly a park or nature reserve. There are trees and shrubs in the background.",
          "annotations": []
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 328,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 52,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 380
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "input": [
        "role": "user",
        "content": [
          {"type": "input_text", "text": "what is in this file?"},
            "type": "input_file",
            "file_url": "https://www.berkshirehathaway.com/letters/2024ltr.pdf",
            "detail": "auto"
  }'

  "id": "resp_686eef60237881a2bd1180bb8b13de430e34c516d176ff86",
  "object": "response",
  "created_at": 1752100704,
  "status": "completed",
  "completed_at": 1752100705,
  "background": false,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "max_tool_calls": null,
  "model": "gpt-5.4",
  "output": [
      "id": "msg_686eef60d3e081a29283bdcbc4322fd90e34c516d176ff86",
      "type": "message",
      "status": "completed",
      "content": [
          "type": "output_text",
          "annotations": [],
          "logprobs": [],
          "text": "The file seems to contain excerpts from a letter to the shareholders of Berkshire Hathaway Inc., likely written by Warren Buffett. It covers several topics:\n\n1. **Communication Philosophy**: Buffett emphasizes the importance of transparency and candidness in reporting mistakes and successes to shareholders.\n\n2. **Mistakes and Learnings**: The letter acknowledges past mistakes in business assessments and management hires, highlighting the importance of correcting errors promptly.\n\n3. **CEO Succession**: Mention of Greg Abel stepping in as the new CEO and continuing the tradition of honest communication.\n\n4. **Pete Liegl Story**: A detailed account of acquiring Forest River and the relationship with its founder, highlighting trust and effective business decisions.\n\n5. **2024 Performance**: Overview of business performance, particularly in insurance and investment activities, with a focus on GEICO's improvement.\n\n6. **Tax Contributions**: Discussion of significant tax payments to the U.S. Treasury, credited to shareholders' reinvestments.\n\n7. **Investment Strategy**: A breakdown of Berkshire\u2019s investments in both controlled subsidiaries and marketable equities, along with a focus on long-term holding strategies.\n\n8. **American Capitalism**: Reflections on America\u2019s economic development and Berkshire\u2019s role within it.\n\n9. **Property-Casualty Insurance**: Insights into the P/C insurance business model and its challenges and benefits.\n\n10. **Japanese Investments**: Information about Berkshire\u2019s investments in Japanese companies and future plans.\n\n11. **Annual Meeting**: Details about the upcoming annual gathering in Omaha, including schedule changes and new book releases.\n\n12. **Personal Anecdotes**: Light-hearted stories about family and interactions, conveying Buffett's personable approach.\n\n13. **Financial Performance Data**: Tables comparing Berkshire\u2019s annual performance to the S&P 500, showing impressive long-term gains.\n\nOverall, the letter reinforces Berkshire Hathaway's commitment to transparency, investment in both its businesses and the wider economy, and emphasizes strong leadership and prudent financial management."
      ],
      "role": "assistant"
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "service_tier": "default",
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_logprobs": 0,
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 8438,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 398,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 8836
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "tools": [{ "type": "web_search_preview" }],
    "input": "What was a positive news story from today?"
  }'

  "id": "resp_67ccf18ef5fc8190b16dbee19bc54e5f087bb177ab789d5c",
  "object": "response",
  "created_at": 1741484430,
  "status": "completed",
  "completed_at": 1741484431,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "web_search_call",
      "id": "ws_67ccf18f64008190a39b619f4c8455ef087bb177ab789d5c",
      "status": "completed"
    },
      "type": "message",
      "id": "msg_67ccf190ca3881909d433c50b1f6357e087bb177ab789d5c",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "As of today, March 9, 2025, one notable positive news story...",
          "annotations": [
              "type": "url_citation",
              "start_index": 442,
              "end_index": 557,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
            },
              "type": "url_citation",
              "start_index": 962,
              "end_index": 1077,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
            },
              "type": "url_citation",
              "start_index": 1336,
              "end_index": 1451,
              "url": "https://.../?utm_source=chatgpt.com",
              "title": "..."
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "web_search_preview",
      "domains": [],
      "search_context_size": "medium",
      "user_location": {
        "type": "approximate",
        "city": null,
        "country": "US",
        "region": null,
        "timezone": null
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 328,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 356,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 684
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "tools": [{
      "type": "file_search",
      "vector_store_ids": ["vs_1234567890"],
      "max_num_results": 20
    }],
    "input": "What are the attributes of an ancient brown dragon?"
  }'

  "id": "resp_67ccf4c55fc48190b71bd0463ad3306d09504fb6872380d7",
  "object": "response",
  "created_at": 1741485253,
  "status": "completed",
  "completed_at": 1741485254,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "file_search_call",
      "id": "fs_67ccf4c63cd08190887ef6464ba5681609504fb6872380d7",
      "status": "completed",
      "queries": [
        "attributes of an ancient brown dragon"
      ],
      "results": null
    },
      "type": "message",
      "id": "msg_67ccf4c93e5c81909d595b369351a9d309504fb6872380d7",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The attributes of an ancient brown dragon include...",
          "annotations": [
              "type": "file_citation",
              "index": 320,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 576,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 815,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 815,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1030,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1030,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1156,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
            },
              "type": "file_citation",
              "index": 1225,
              "file_id": "file-4wDz5b167pAf72nx1h9eiN",
              "filename": "dragons.pdf"
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "file_search",
      "filters": null,
      "max_num_results": 20,
      "ranking_options": {
        "ranker": "auto",
        "score_threshold": 0.0
      },
      "vector_store_ids": [
        "vs_1234567890"
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 18307,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 348,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 18655
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "instructions": "You are a helpful assistant.",
    "input": "Hello!",
    "stream": true
  }'

event: response.created
data: {"type":"response.created","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"in_progress","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":null,"user":null,"metadata":{}}}

event: response.in_progress
data: {"type":"response.in_progress","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"in_progress","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":null,"user":null,"metadata":{}}}

event: response.output_item.added
data: {"type":"response.output_item.added","output_index":0,"item":{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"in_progress","role":"assistant","content":[]}}

event: response.content_part.added
data: {"type":"response.content_part.added","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"part":{"type":"output_text","text":"","annotations":[]}}

event: response.output_text.delta
data: {"type":"response.output_text.delta","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"delta":"Hi"}

...

event: response.output_text.done
data: {"type":"response.output_text.done","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"text":"Hi there! How can I assist you today?"}

event: response.content_part.done
data: {"type":"response.content_part.done","item_id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","output_index":0,"content_index":0,"part":{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}}

event: response.output_item.done
data: {"type":"response.output_item.done","output_index":0,"item":{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"completed","role":"assistant","content":[{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}]}}

event: response.completed
data: {"type":"response.completed","response":{"id":"resp_67c9fdcecf488190bdd9a0409de3a1ec07b8b0ad4e5eb654","object":"response","created_at":1741290958,"status":"completed","error":null,"incomplete_details":null,"instructions":"You are a helpful assistant.","max_output_tokens":null,"model":"gpt-5.4","output":[{"id":"msg_67c9fdcf37fc8190ba82116e33fb28c507b8b0ad4e5eb654","type":"message","status":"completed","role":"assistant","content":[{"type":"output_text","text":"Hi there! How can I assist you today?","annotations":[]}]}],"parallel_tool_calls":true,"previous_response_id":null,"reasoning":{"effort":null,"summary":null},"store":true,"temperature":1.0,"text":{"format":{"type":"text"}},"tool_choice":"auto","tools":[],"top_p":1.0,"truncation":"disabled","usage":{"input_tokens":37,"output_tokens":11,"output_tokens_details":{"reasoning_tokens":0},"total_tokens":48},"user":null,"metadata":{}}}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "input": "What is the weather like in Boston today?",
    "tools": [
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "The city and state, e.g. San Francisco, CA"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
          },
          "required": ["location", "unit"]
    ],
    "tool_choice": "auto"
  }'

  "id": "resp_67ca09c5efe0819096d0511c92b8c890096610f474011cc0",
  "object": "response",
  "created_at": 1741294021,
  "status": "completed",
  "completed_at": 1741294022,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.4",
  "output": [
      "type": "function_call",
      "id": "fc_67ca09c6bedc8190a7abfec07b1a1332096610f474011cc0",
      "call_id": "call_unLAR8MvFNptuiZK6K6HCy5k",
      "name": "get_current_weather",
      "arguments": "{\"location\":\"Boston, MA\",\"unit\":\"celsius\"}",
      "status": "completed"
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [
      "type": "function",
      "description": "Get the current weather in a given location",
      "name": "get_current_weather",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {
            "type": "string",
            "description": "The city and state, e.g. San Francisco, CA"
          },
          "unit": {
            "type": "string",
            "enum": [
              "celsius",
              "fahrenheit"
        },
        "required": [
          "location",
          "unit"
      },
      "strict": true
  ],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 291,
    "output_tokens": 23,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 314
  },
  "user": null,
  "metadata": {}

### Create a model response

HTTP

curl https://api.openai.com/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d '{
    "model": "o3-mini",
    "input": "How much wood would a woodchuck chuck?",
    "reasoning": {
      "effort": "high"
  }'

  "id": "resp_67ccd7eca01881908ff0b5146584e408072912b2993db808",
  "object": "response",
  "created_at": 1741477868,
  "status": "completed",
  "completed_at": 1741477869,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "o1-2024-12-17",
  "output": [
      "type": "message",
      "id": "msg_67ccd7f7b5848190a6f3e95d809f6b44072912b2993db808",
      "status": "completed",
      "role": "assistant",
      "content": [
          "type": "output_text",
          "text": "The classic tongue twister...",
          "annotations": []
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": "high",
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 81,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 1035,
    "output_tokens_details": {
      "reasoning_tokens": 832
    },
    "total_tokens": 1116
  },
  "user": null,
  "metadata": {}

200 example

  "id": "id",
  "created_at": 0,
  "error": {
    "code": "server_error",
    "message": "message"
  },
  "incomplete_details": {
    "reason": "max_output_tokens"
  },
  "instructions": "string",
  "metadata": {
    "foo": "string"
  },
  "model": "gpt-5.1",
  "object": "response",
  "output": [
      "id": "id",
      "content": [
          "annotations": [
              "file_id": "file_id",
              "filename": "filename",
              "index": 0,
              "type": "file_citation"
          ],
          "logprobs": [
              "token": "token",
              "bytes": [
                0
              ],
              "logprob": 0,
              "top_logprobs": [
                  "token": "token",
                  "bytes": [
                    0
                  ],
                  "logprob": 0
          ],
          "text": "text",
          "type": "output_text"
      ],
      "role": "assistant",
      "status": "in_progress",
      "type": "message",
      "agent": {
        "agent_name": "agent_name"
      },
      "phase": "commentary"
  ],
  "parallel_tool_calls": true,
  "temperature": 1,
  "tool_choice": "none",
  "tools": [
      "name": "name",
      "parameters": {
        "foo": "bar"
      },
      "strict": true,
      "type": "function",
      "allowed_callers": [
        "direct"
      ],
      "defer_loading": true,
      "description": "description",
      "output_schema": {
        "foo": "bar"
  ],
  "top_p": 1,
  "background": true,
  "completed_at": 0,
  "conversation": {
    "id": "id"
  },
  "max_output_tokens": 0,
  "max_tool_calls": 0,
  "moderation": {
    "input": {
      "categories": {
        "foo": true
      },
      "category_applied_input_types": {
        "foo": [
          "text"
      },
      "category_scores": {
        "foo": 0
      },
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
    },
    "output": {
      "categories": {
        "foo": true
      },
      "category_applied_input_types": {
        "foo": [
          "text"
      },
      "category_scores": {
        "foo": 0
      },
      "flagged": true,
      "model": "model",
      "type": "moderation_result"
  },
  "output_text": "output_text",
  "previous_response_id": "previous_response_id",
  "prompt": {
    "id": "id",
    "variables": {
      "foo": "string"
    },
    "version": "version"
  },
  "prompt_cache_key": "prompt-cache-key-1234",
  "prompt_cache_options": {
    "mode": "implicit",
    "ttl": "30m"
  },
  "prompt_cache_retention": "in_memory",
  "reasoning": {
    "context": "auto",
    "effort": "none",
    "generate_summary": "auto",
    "mode": "standard",
    "summary": "auto"
  },
  "safety_identifier": "safety-identifier-1234",
  "service_tier": "auto",
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "low"
  },
  "top_logprobs": 0,
  "truncation": "auto",
  "usage": {
    "input_tokens": 0,
    "input_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "output_tokens": 0,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 0
  },
  "user": "user-1234"
