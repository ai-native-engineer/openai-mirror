<!-- source: https://developers.openai.com/api/reference/typescript/resources/beta/subresources/responses/subresources/input_items/methods/list/ -->

[API Reference](/api/reference/typescript)

[Beta](/api/reference/typescript/resources/beta)

[Responses](/api/reference/typescript/resources/beta/subresources/responses)

[Input Items](/api/reference/typescript/resources/beta/subresources/responses/subresources/input_items)

# List input items

client.beta.responses.inputItems.list(stringresponseID, InputItemListParams { after, include, limit, 2 more } params?, RequestOptionsoptions?): CursorPage<[BetaResponseItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_item%20%3E%20(schema))>

GET/responses/{response\_id}/input\_items

Returns a list of input items for a given response.

##### ParametersExpand Collapse

responseID: string

params: InputItemListParams { after, include, limit, 2 more }

after?: string

Query param: An item ID to list items after, used in pagination.

include?: Array<[BetaResponseIncludable](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_includable%20%3E%20(schema))>

Query param: Additional fields to include in the response. See the `include`
parameter for Response creation above for more information.

"file\_search\_call.results"

"web\_search\_call.results"

"web\_search\_call.action.sources"

"message.input\_image.image\_url"

"computer\_call\_output.output.image\_url"

"code\_interpreter\_call.outputs"

"reasoning.encrypted\_content"

"message.output\_text.logprobs"

limit?: number

Query param: A limit on the number of objects to be returned. Limit can range between
1 and 100, and the default is 20.

order?: "asc" | "desc"

Query param: The order to return the input items in. Default is `desc`.

* `asc`: Return the input items in ascending order.
* `desc`: Return the input items in descending order.

"asc"

"desc"

betas?: Array<"responses\_multi\_agent=v1">

Header param: Optional beta features to enable for this request.

##### ReturnsExpand Collapse

BetaResponseItem = [BetaResponseInputMessageItem](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_item%20%3E%20(schema)) { id, content, role, 3 more }  | [BetaResponseOutputMessage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_message%20%3E%20(schema)) { id, content, role, 4 more }  | [BetaResponseFileSearchToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_file_search_tool_call%20%3E%20(schema)) { id, queries, status, 3 more }  | 29 more

Content item used to generate a response.

BetaResponseInputMessageItem { id, content, role, 3 more }

id: string

The unique ID of the message input.

content: [BetaResponseInputMessageContentList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_message_content_list%20%3E%20(schema)) { , ,  }

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id?: string | null

image\_url?: string | null

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseInputFile { type, detail, file\_data, 4 more }

type: "input\_file"

detail?: "auto" | "low" | "high"

"auto"

"low"

"high"

file\_data?: string

file\_id?: string | null

file\_url?: string

filename?: string

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

role: "user" | "system" | "developer"

"user"

"system"

"developer"

type: "message"

agent?: Agent | null

agent\_name: string

status?: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

BetaResponseOutputMessage { id, content, role, 4 more }

id: string

content: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | [BetaResponseOutputRefusal](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_refusal%20%3E%20(schema)) { refusal, type } >

BetaResponseOutputText { annotations, text, type, logprobs }

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

FileCitation { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

BetaResponseOutputRefusal { refusal, type }

refusal: string

type: "refusal"

role: "assistant"

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "message"

agent?: Agent | null

agent\_name: string

phase?: "commentary" | "final\_answer" | null

"commentary"

"final\_answer"

BetaResponseFileSearchToolCall { id, queries, status, 3 more }

[file search guide](https://platform.openai.com/docs/guides/tools-file-search) for more information.

id: string

queries: Array<string>

status: "in\_progress" | "searching" | "completed" | 2 more

"in\_progress"

"searching"

"completed"

"incomplete"

"failed"

type: "file\_search\_call"

agent?: Agent | null

agent\_name: string

results?: Array<Result> | null

attributes?: Record<string, string | number | boolean> | null

string

number

boolean

file\_id?: string

filename?: string

score?: number

formatfloat

text?: string

BetaResponseComputerToolCall { id, call\_id, pending\_safety\_checks, 5 more }

[computer use guide](https://platform.openai.com/docs/guides/tools-computer-use) for more information.

id: string

call\_id: string

pending\_safety\_checks: Array<PendingSafetyCheck>

id: string

code?: string | null

message?: string | null

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "computer\_call"

action?: [BetaComputerAction](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action%20%3E%20(schema))

Click { button, type, x, 2 more }

button: "left" | "right" | "wheel" | 2 more

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

keys?: Array<string> | null

The keys being held while clicking.

DoubleClick { keys, type, x, y }

A double click action.

keys: Array<string> | null

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag { path, type, keys }

A drag action.

path: Array<Path>

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: number

The x-coordinate.

y: number

The y-coordinate.

type: "drag"

Specifies the event type. For a drag action, this property is always set to `drag`.

keys?: Array<string> | null

The keys being held while dragging the mouse.

Keypress { keys, type }

A collection of keypresses the model would like to perform.

keys: Array<string>

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys?: Array<string> | null

The keys being held while moving the mouse.

Screenshot { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll { scroll\_x, scroll\_y, type, 3 more }

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

keys?: Array<string> | null

The keys being held while scrolling.

Type { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

actions?: [BetaComputerActionList](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_computer_action_list%20%3E%20(schema)) { , , , 6 more }

Click { button, type, x, 2 more }

button: "left" | "right" | "wheel" | 2 more

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

keys?: Array<string> | null

The keys being held while clicking.

DoubleClick { keys, type, x, y }

A double click action.

keys: Array<string> | null

The keys being held while double-clicking.

type: "double\_click"

Specifies the event type. For a double click action, this property is always set to `double_click`.

x: number

The x-coordinate where the double click occurred.

y: number

The y-coordinate where the double click occurred.

Drag { path, type, keys }

A drag action.

path: Array<Path>

An array of coordinates representing the path of the drag action. Coordinates will appear as an array of objects, eg

  { x: 100, y: 200 },
  { x: 200, y: 300 }

x: number

The x-coordinate.

y: number

The y-coordinate.

type: "drag"

Specifies the event type. For a drag action, this property is always set to `drag`.

keys?: Array<string> | null

The keys being held while dragging the mouse.

Keypress { keys, type }

A collection of keypresses the model would like to perform.

keys: Array<string>

The combination of keys the model is requesting to be pressed. This is an array of strings, each representing a key.

type: "keypress"

Specifies the event type. For a keypress action, this property is always set to `keypress`.

Move { type, x, y, keys }

A mouse move action.

type: "move"

Specifies the event type. For a move action, this property is always set to `move`.

x: number

The x-coordinate to move to.

y: number

The y-coordinate to move to.

keys?: Array<string> | null

The keys being held while moving the mouse.

Screenshot { type }

A screenshot action.

type: "screenshot"

Specifies the event type. For a screenshot action, this property is always set to `screenshot`.

Scroll { scroll\_x, scroll\_y, type, 3 more }

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

keys?: Array<string> | null

The keys being held while scrolling.

Type { text, type }

An action to type in text.

text: string

The text to type.

type: "type"

Specifies the event type. For a type action, this property is always set to `type`.

Wait { type }

A wait action.

type: "wait"

Specifies the event type. For a wait action, this property is always set to `wait`.

agent?: Agent | null

agent\_name: string

BetaResponseComputerToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the computer call tool output.

call\_id: string

output: [BetaResponseComputerToolCallOutputScreenshot](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_computer_tool_call_output_screenshot%20%3E%20(schema)) { type, file\_id, image\_url }

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is
always set to `computer_screenshot`.

file\_id?: string

image\_url?: string

status: "completed" | "incomplete" | "failed" | "in\_progress"

"completed"

"incomplete"

"failed"

"in\_progress"

type: "computer\_call\_output"

acknowledged\_safety\_checks?: Array<AcknowledgedSafetyCheck>

The safety checks reported by the API that have been acknowledged by the
developer.

id: string

code?: string | null

message?: string | null

agent?: Agent | null

agent\_name: string

created\_by?: string

The identifier of the actor that created the item.

BetaResponseFunctionWebSearch { id, action, status, 2 more }

[web search guide](https://platform.openai.com/docs/guides/tools-web-search) for more information.

id: string

action: Search { type, queries, query, sources }  | OpenPage { type, url }  | FindInPage { pattern, type, url }

Search { type, queries, query, sources }

type: "search"

queries?: Array<string>

Deprecatedquery?: string

sources?: Array<Source>

type: "url"

url: string

OpenPage { type, url }

type: "open\_page"

url?: string | null

FindInPage { pattern, type, url }

pattern: string

type: "find\_in\_page"

url: string

status: "in\_progress" | "searching" | "completed" | "failed"

"in\_progress"

"searching"

"completed"

"failed"

type: "web\_search\_call"

agent?: Agent | null

agent\_name: string

BetaResponseFunctionToolCallItem extends [BetaResponseFunctionToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_function_tool_call%20%3E%20(schema)) { arguments, call\_id, name, 6 more }  { id, status, created\_by }

[function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.

id: string

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseFunctionToolCallOutputItem { id, call\_id, output, 5 more }

id: string

The unique ID of the function call tool output.

call\_id: string

output: string | Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

The output from the function call generated by your code.

string

Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseInputImage](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_image%20%3E%20(schema)) { detail, type, file\_id, 2 more }  | [BetaResponseInputFile](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_file%20%3E%20(schema)) { type, detail, file\_data, 4 more } >

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id?: string | null

image\_url?: string | null

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseInputFile { type, detail, file\_data, 4 more }

type: "input\_file"

detail?: "auto" | "low" | "high"

"auto"

"low"

"high"

file\_data?: string

file\_id?: string | null

file\_url?: string

filename?: string

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "function\_call\_output"

agent?: Agent | null

agent\_name: string

caller?: Direct { type }  | Program { caller\_id, type }  | null

Direct { type }

type: "direct"

The caller type. Always `direct`.

Program { caller\_id, type }

caller\_id: string

maxLength64

minLength1

type: "program"

created\_by?: string

The identifier of the actor that created the item.

AgentMessage { id, author, content, 3 more }

id: string

The unique ID of the agent message.

author: string

content: Array<[BetaResponseInputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_input_text%20%3E%20(schema)) { text, type, prompt\_cache\_breakpoint }  | [BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs }  | Text { text, type }  | 7 more>

Encrypted content sent between agents.

BetaResponseInputText { text, type, prompt\_cache\_breakpoint }

text: string

type: "input\_text"

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseOutputText { annotations, text, type, logprobs }

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

FileCitation { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

Text { text, type }

A text content.

text: string

type: "text"

SummaryText { text, type }

A summary text from the model.

text: string

type: "summary\_text"

ReasoningText { text, type }

text: string

type: "reasoning\_text"

BetaResponseOutputRefusal { refusal, type }

refusal: string

type: "refusal"

BetaResponseInputImage { detail, type, file\_id, 2 more }

An image input to the model. Learn about [image inputs](https://platform.openai.com/docs/guides/vision).

detail: "low" | "high" | "auto" | "original"

"low"

"high"

"auto"

"original"

type: "input\_image"

file\_id?: string | null

image\_url?: string | null

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

ComputerScreenshot { detail, file\_id, image\_url, 2 more }

A screenshot of a computer.

detail: "low" | "high" | "auto" | "original"

The detail level of the screenshot image to be sent to the model. One of `high`, `low`, `auto`, or `original`. Defaults to `auto`.

"low"

"high"

"auto"

"original"

file\_id: string | null

image\_url: string | null

type: "computer\_screenshot"

Specifies the event type. For a computer screenshot, this property is always set to `computer_screenshot`.

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

BetaResponseInputFile { type, detail, file\_data, 4 more }

type: "input\_file"

detail?: "auto" | "low" | "high"

"auto"

"low"

"high"

file\_data?: string

file\_id?: string | null

file\_url?: string

filename?: string

prompt\_cache\_breakpoint?: PromptCacheBreakpoint { mode }

mode: "explicit"

EncryptedContent { encrypted\_content, type }

encrypted\_content: string

type: "encrypted\_content"

recipient: string

type: "agent\_message"

The type of the item. Always `agent_message`.

agent?: Agent { agent\_name }

agent\_name: string

MultiAgentCall { id, action, arguments, 3 more }

id: string

The unique ID of the multi-agent call item.

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

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

agent?: Agent { agent\_name }

agent\_name: string

MultiAgentCallOutput { id, action, call\_id, 3 more }

id: string

The unique ID of the multi-agent call output item.

action: "spawn\_agent" | "interrupt\_agent" | "list\_agents" | 3 more

"spawn\_agent"

"interrupt\_agent"

"list\_agents"

"send\_message"

"followup\_task"

"wait\_agent"

call\_id: string

output: Array<[BetaResponseOutputText](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_output_text%20%3E%20(schema)) { annotations, text, type, logprobs } >

annotations: Array<FileCitation { file\_id, filename, index, type }  | URLCitation { end\_index, start\_index, title, 2 more }  | ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }  | FilePath { file\_id, index, type } >

FileCitation { file\_id, filename, index, type }

file\_id: string

filename: string

index: number

type: "file\_citation"

URLCitation { end\_index, start\_index, title, 2 more }

end\_index: number

start\_index: number

title: string

type: "url\_citation"

url: string

ContainerFileCitation { container\_id, end\_index, file\_id, 3 more }

container\_id: string

end\_index: number

file\_id: string

filename: string

start\_index: number

type: "container\_file\_citation"

FilePath { file\_id, index, type }

file\_id: string

index: number

type: "file\_path"

text: string

type: "output\_text"

logprobs?: Array<Logprob>

token: string

bytes: Array<number>

logprob: number

top\_logprobs: Array<TopLogprob>

token: string

bytes: Array<number>

logprob: number

type: "multi\_agent\_call\_output"

The type of the multi-agent result. Always `multi_agent_call_output`.

agent?: Agent { agent\_name }

agent\_name: string

BetaResponseToolSearchCall { id, arguments, call\_id, 5 more }

id: string

The unique ID of the tool search call item.

arguments: unknown

Arguments used for the tool search call.

call\_id: string | null

execution: "server" | "client"

"server"

"client"

status: "in\_progress" | "completed" | "incomplete"

The status of the tool search call item that was recorded.

"in\_progress"

"completed"

"incomplete"

type: "tool\_search\_call"

The type of the item. Always `tool_search_call`.

agent?: Agent { agent\_name }

agent\_name: string

created\_by?: string

The identifier of the actor that created the item.

BetaResponseToolSearchOutputItem { id, call\_id, execution, 5 more }

id: string

The unique ID of the tool search output item.

call\_id: string | null

execution: "server" | "client"

"server"

"client"

status: "in\_progress" | "completed" | "incomplete"

The status of the tool search output item that was recorded.

"in\_progress"

"completed"

"incomplete"

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The loaded tool definitions returned by tool search.

BetaFunctionTool { name, parameters, strict, 5 more }

name: string

parameters: Record<string, unknown> | null

strict: boolean | null

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string | null

output\_schema?: Record<string, unknown> | null

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: Array<string>

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

ComparisonFilter { key, type, value }

key: string

type: "eq" | "ne" | "gt" | 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

filters: Array<ComparisonFilter { key, type, value }  | unknown>

ComparisonFilter { key, type, value }

key: string

type: "eq" | "ne" | "gt" | 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

"and"

"or"

max\_num\_results?: number

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker?: "auto" | "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold?: number

BetaComputerTool { type }

type: "computer"

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" | "mac" | "linux" | 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

allowed\_domains?: Array<string> | null

search\_context\_size?: "low" | "medium" | "high"

"low"

"medium"

"high"

user\_location?: UserLocation | null

city?: string | null

country?: string | null

region?: string | null

timezone?: string | null

type?: "approximate"

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

Array<string>

McpToolFilter { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

authorization?: string

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

headers?: Record<string, string> | null

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

McpToolApprovalFilter { always, never }

always?: Always { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

never?: Never { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

"always" | "never"

"always"

"never"

server\_description?: string

server\_url?: string

tunnel\_id?: string

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids?: Array<string>

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

type: "allowlist"

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action?: "generate" | "edit" | "auto"

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

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

input\_fidelity?: "high" | "low" | null

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

file\_id?: string

image\_url?: string

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

"auto"

"low"

output\_compression?: number

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

"png"

"webp"

"jpeg"

partial\_images?: number

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

BetaFunctionShellTool { type, allowed\_callers, environment }

type: "shell"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids?: Array<string>

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

type: "allowlist"

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

BetaSkillReference { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version?: string

BetaInlineSkill { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment { type, skills }

type: "local"

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

description: string

name: string

path: string

BetaContainerReference { container\_id, type }

container\_id: string

type: "container\_reference"

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string

format?: Text { type }  | Grammar { definition, syntax, type }

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

definition: string

syntax: "lark" | "regex"

"lark"

"regex"

type: "grammar"

BetaNamespaceTool { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string | null

output\_schema?: Record<string, unknown> | null

parameters?: unknown

strict?: boolean | null

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string

format?: Text { type }  | Grammar { definition, syntax, type }

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

definition: string

syntax: "lark" | "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

BetaToolSearchTool { type, description, execution, parameters }

type: "tool\_search"

description?: string | null

execution?: "server" | "client"

"server"

"client"

parameters?: unknown

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

"low"

"medium"

"high"

user\_location?: UserLocation | null

type: "approximate"

city?: string | null

country?: string | null

region?: string | null

timezone?: string | null

BetaApplyPatchTool { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

type: "tool\_search\_output"

The type of the item. Always `tool_search_output`.

agent?: Agent { agent\_name }

agent\_name: string

created\_by?: string

The identifier of the actor that created the item.

AdditionalTools { id, role, tools, 2 more }

id: string

The unique ID of the additional tools item.

role: "unknown" | "user" | "assistant" | 5 more

The role that provided the additional tools.

"unknown"

"user"

"assistant"

"system"

"critic"

"discriminator"

"developer"

"tool"

tools: Array<[BetaTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_tool%20%3E%20(schema))>

The additional tool definitions made available at this item.

BetaFunctionTool { name, parameters, strict, 5 more }

name: string

parameters: Record<string, unknown> | null

strict: boolean | null

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string | null

output\_schema?: Record<string, unknown> | null

BetaFileSearchTool { type, vector\_store\_ids, filters, 2 more }

type: "file\_search"

vector\_store\_ids: Array<string>

filters?: ComparisonFilter { key, type, value }  | CompoundFilter { filters, type }  | null

ComparisonFilter { key, type, value }

key: string

type: "eq" | "ne" | "gt" | 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

string

number

boolean

Array<string | number>

string

number

CompoundFilter { filters, type }

filters: Array<ComparisonFilter { key, type, value }  | unknown>

ComparisonFilter { key, type, value }

key: string

type: "eq" | "ne" | "gt" | 5 more

"eq"

"ne"

"gt"

"gte"

"lt"

"lte"

"in"

"nin"

value: string | number | boolean | Array<string | number>

string

number

boolean

Array<string | number>

string

number

unknown

type: "and" | "or"

"and"

"or"

max\_num\_results?: number

ranking\_options?: RankingOptions { hybrid\_search, ranker, score\_threshold }

hybrid\_search?: HybridSearch { embedding\_weight, text\_weight }

embedding\_weight: number

text\_weight: number

ranker?: "auto" | "default-2024-11-15"

"auto"

"default-2024-11-15"

score\_threshold?: number

BetaComputerTool { type }

type: "computer"

BetaComputerUsePreviewTool { display\_height, display\_width, environment, type }

display\_height: number

display\_width: number

environment: "windows" | "mac" | "linux" | 2 more

"windows"

"mac"

"linux"

"ubuntu"

"browser"

type: "computer\_use\_preview"

BetaWebSearchTool { type, filters, search\_context\_size, user\_location }

[web search tool](https://platform.openai.com/docs/guides/tools-web-search).

type: "web\_search" | "web\_search\_2025\_08\_26"

"web\_search"

"web\_search\_2025\_08\_26"

filters?: Filters | null

allowed\_domains?: Array<string> | null

search\_context\_size?: "low" | "medium" | "high"

"low"

"medium"

"high"

user\_location?: UserLocation | null

city?: string | null

country?: string | null

region?: string | null

timezone?: string | null

type?: "approximate"

Mcp { server\_label, type, allowed\_callers, 9 more }

Give the model access to additional tools via remote Model Context Protocol
(MCP) servers. [Learn more about MCP](https://platform.openai.com/docs/guides/tools-remote-mcp).

server\_label: string

type: "mcp"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

allowed\_tools?: Array<string> | McpToolFilter { read\_only, tool\_names }  | null

Array<string>

McpToolFilter { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

authorization?: string

connector\_id?: "connector\_dropbox" | "connector\_gmail" | "connector\_googlecalendar" | 5 more

about service connectors [here](https://platform.openai.com/docs/guides/tools-remote-mcp#connectors).

"connector\_dropbox"

"connector\_gmail"

"connector\_googlecalendar"

"connector\_googledrive"

"connector\_microsoftteams"

"connector\_outlookcalendar"

"connector\_outlookemail"

"connector\_sharepoint"

defer\_loading?: boolean

headers?: Record<string, string> | null

require\_approval?: McpToolApprovalFilter { always, never }  | "always" | "never" | null

McpToolApprovalFilter { always, never }

always?: Always { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

never?: Never { read\_only, tool\_names }

read\_only?: boolean

tool\_names?: Array<string>

"always" | "never"

"always"

"never"

server\_description?: string

server\_url?: string

tunnel\_id?: string

CodeInterpreter { container, type, allowed\_callers }

A tool that runs Python code to help generate a response to a prompt.

container: string | CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

string

CodeInterpreterToolAuto { type, file\_ids, memory\_limit, network\_policy }

type: "auto"

file\_ids?: Array<string>

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

type: "allowlist"

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

type: "code\_interpreter"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

ProgrammaticToolCalling { type }

type: "programmatic\_tool\_calling"

The type of the tool. Always `programmatic_tool_calling`.

ImageGeneration { type, action, background, 9 more }

A tool that generates images using the GPT image models.

type: "image\_generation"

action?: "generate" | "edit" | "auto"

"generate"

"edit"

"auto"

background?: "transparent" | "opaque" | "auto"

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

input\_fidelity?: "high" | "low" | null

"high"

"low"

input\_image\_mask?: InputImageMask { file\_id, image\_url }

file\_id?: string

image\_url?: string

model?: (string & {}) | "gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

(string & {})

"gpt-image-1" | "gpt-image-1-mini" | "gpt-image-2" | 3 more

"gpt-image-1"

"gpt-image-1-mini"

"gpt-image-2"

"gpt-image-2-2026-04-21"

"gpt-image-1.5"

"chatgpt-image-latest"

moderation?: "auto" | "low"

"auto"

"low"

output\_compression?: number

minimum0

maximum100

output\_format?: "png" | "webp" | "jpeg"

"png"

"webp"

"jpeg"

partial\_images?: number

minimum0

maximum3

quality?: "low" | "medium" | "high" | "auto"

"low"

"medium"

"high"

"auto"

size?: (string & {}) | "1024x1024" | "1024x1536" | "1536x1024" | "auto"

(string & {})

"1024x1024" | "1024x1536" | "1536x1024" | "auto"

"1024x1024"

"1024x1536"

"1536x1024"

"auto"

LocalShell { type }

A tool that allows the model to execute shell commands in a local environment.

type: "local\_shell"

The type of the local shell tool. Always `local_shell`.

BetaFunctionShellTool { type, allowed\_callers, environment }

type: "shell"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

environment?: [BetaContainerAuto](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_auto%20%3E%20(schema)) { type, file\_ids, memory\_limit, 2 more }  | [BetaLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_environment%20%3E%20(schema)) { type, skills }  | [BetaContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_reference%20%3E%20(schema)) { container\_id, type }  | null

BetaContainerAuto { type, file\_ids, memory\_limit, 2 more }

type: "container\_auto"

file\_ids?: Array<string>

memory\_limit?: "1g" | "4g" | "16g" | "64g" | null

"1g"

"4g"

"16g"

"64g"

network\_policy?: [BetaContainerNetworkPolicyDisabled](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_disabled%20%3E%20(schema)) { type }  | [BetaContainerNetworkPolicyAllowlist](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_allowlist%20%3E%20(schema)) { allowed\_domains, type, domain\_secrets }

BetaContainerNetworkPolicyDisabled { type }

type: "disabled"

BetaContainerNetworkPolicyAllowlist { allowed\_domains, type, domain\_secrets }

allowed\_domains: Array<string>

type: "allowlist"

domain\_secrets?: Array<[BetaContainerNetworkPolicyDomainSecret](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_container_network_policy_domain_secret%20%3E%20(schema)) { domain, name, value } >

domain: string

minLength1

name: string

minLength1

value: string

maxLength10485760

minLength1

skills?: Array<[BetaSkillReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_skill_reference%20%3E%20(schema)) { skill\_id, type, version }  | [BetaInlineSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill%20%3E%20(schema)) { description, name, source, type } >

BetaSkillReference { skill\_id, type, version }

skill\_id: string

maxLength64

minLength1

type: "skill\_reference"

version?: string

BetaInlineSkill { description, name, source, type }

description: string

name: string

source: [BetaInlineSkillSource](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_inline_skill_source%20%3E%20(schema)) { data, media\_type, type }

data: string

Base64-encoded skill zip bundle.

maxLength70254592

minLength1

media\_type: "application/zip"

The media type of the inline skill payload. Must be `application/zip`.

type: "base64"

The type of the inline skill source. Must be `base64`.

type: "inline"

BetaLocalEnvironment { type, skills }

type: "local"

skills?: Array<[BetaLocalSkill](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_local_skill%20%3E%20(schema)) { description, name, path } >

description: string

name: string

path: string

BetaContainerReference { container\_id, type }

container\_id: string

type: "container\_reference"

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string

format?: Text { type }  | Grammar { definition, syntax, type }

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

definition: string

syntax: "lark" | "regex"

"lark"

"regex"

type: "grammar"

BetaNamespaceTool { description, name, tools, type }

description: string

minLength1

name: string

minLength1

tools: Array<Function { name, type, allowed\_callers, 5 more }  | [BetaCustomTool](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_custom_tool%20%3E%20(schema)) { name, type, allowed\_callers, 3 more } >

Function { name, type, allowed\_callers, 5 more }

name: string

maxLength128

minLength1

type: "function"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string | null

output\_schema?: Record<string, unknown> | null

parameters?: unknown

strict?: boolean | null

BetaCustomTool { name, type, allowed\_callers, 3 more }

A custom tool that processes input using a specified format. Learn more about [custom tools](https://platform.openai.com/docs/guides/function-calling#custom-tools)

name: string

type: "custom"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

defer\_loading?: boolean

description?: string

format?: Text { type }  | Grammar { definition, syntax, type }

Text { type }

Unconstrained free-form text.

type: "text"

Unconstrained text format. Always `text`.

Grammar { definition, syntax, type }

definition: string

syntax: "lark" | "regex"

"lark"

"regex"

type: "grammar"

type: "namespace"

BetaToolSearchTool { type, description, execution, parameters }

type: "tool\_search"

description?: string | null

execution?: "server" | "client"

"server"

"client"

parameters?: unknown

BetaWebSearchPreviewTool { type, search\_content\_types, search\_context\_size, user\_location }

type: "web\_search\_preview" | "web\_search\_preview\_2025\_03\_11"

"web\_search\_preview"

"web\_search\_preview\_2025\_03\_11"

search\_content\_types?: Array<"text" | "image">

"text"

"image"

search\_context\_size?: "low" | "medium" | "high"

"low"

"medium"

"high"

user\_location?: UserLocation | null

type: "approximate"

city?: string | null

country?: string | null

region?: string | null

timezone?: string | null

BetaApplyPatchTool { type, allowed\_callers }

type: "apply\_patch"

allowed\_callers?: Array<"direct" | "programmatic"> | null

"direct"

"programmatic"

type: "additional\_tools"

The type of the item. Always `additional_tools`.

agent?: Agent { agent\_name }

agent\_name: string

BetaResponseReasoningItem { id, summary, type, 4 more }

[managing context](https://platform.openai.com/docs/guides/conversation-state).

id: string

summary: Array<Summary>

text: string

type: "summary\_text"

type: "reasoning"

agent?: Agent | null

agent\_name: string

content?: Array<Content>

text: string

type: "reasoning\_text"

encrypted\_content?: string | null

status?: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

Program { id, call\_id, code, 3 more }

id: string

The unique ID of the program item.

call\_id: string

code: string

fingerprint: string

type: "program"

The type of the item. Always `program`.

agent?: Agent { agent\_name }

agent\_name: string

ProgramOutput { id, call\_id, result, 3 more }

id: string

The unique ID of the program output item.

call\_id: string

result: string

status: "completed" | "incomplete"

The terminal status of the program output item.

"completed"

"incomplete"

type: "program\_output"

The type of the item. Always `program_output`.

agent?: Agent { agent\_name }

agent\_name: string

BetaResponseCompactionItem { id, encrypted\_content, type, 2 more }

A compaction item generated by the [`v1/responses/compact` API](https://platform.openai.com/docs/api-reference/responses/compact).

id: string

The unique ID of the compaction item.

encrypted\_content: string

The encrypted content that was produced by compaction.

type: "compaction"

agent?: Agent { agent\_name }

agent\_name: string

created\_by?: string

The identifier of the actor that created the item.

ImageGenerationCall { id, result, status, 2 more }

An image generation request made by the model.

id: string

result: string | null

status: "in\_progress" | "completed" | "generating" | "failed"

"in\_progress"

"completed"

"generating"

"failed"

type: "image\_generation\_call"

agent?: Agent | null

agent\_name: string

BetaResponseCodeInterpreterToolCall { id, code, container\_id, 4 more }

id: string

code: string | null

container\_id: string

outputs: Array<Logs { logs, type }  | Image { type, url } > | null

Logs { logs, type }

logs: string

type: "logs"

Image { type, url }

type: "image"

url: string

status: "in\_progress" | "completed" | "incomplete" | 2 more

"in\_progress"

"completed"

"incomplete"

"interpreting"

"failed"

type: "code\_interpreter\_call"

agent?: Agent | null

agent\_name: string

LocalShellCall { id, action, call\_id, 3 more }

A tool call to run a command on the local shell.

id: string

action: Action { command, env, type, 3 more }

command: Array<string>

env: Record<string, string>

type: "exec"

timeout\_ms?: number | null

user?: string | null

working\_directory?: string | null

call\_id: string

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "local\_shell\_call"

agent?: Agent | null

agent\_name: string

LocalShellCallOutput { id, output, type, 2 more }

The output of a local shell tool call.

id: string

output: string

type: "local\_shell\_call\_output"

agent?: Agent | null

agent\_name: string

status?: "in\_progress" | "completed" | "incomplete" | null

"in\_progress"

"completed"

"incomplete"

BetaResponseFunctionShellToolCall { id, action, call\_id, 6 more }

A tool call that executes one or more shell commands in a managed environment.

id: string

action: Action { commands, max\_output\_length, timeout\_ms }

commands: Array<string>

max\_output\_length: number | null

Optional maximum number of characters to return from each command.

timeout\_ms: number | null

Optional timeout in milliseconds for the commands.

call\_id: string

environment: [BetaResponseLocalEnvironment](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_local_environment%20%3E%20(schema)) { type }  | [BetaResponseContainerReference](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_container_reference%20%3E%20(schema)) { container\_id, type }  | null

Represents the use of a local environment to perform shell actions.

BetaResponseLocalEnvironment { type }

Represents the use of a local environment to perform shell actions.

type: "local"

The environment type. Always `local`.

BetaResponseContainerReference { container\_id, type }

Represents a container created with /v1/containers.

container\_id: string

type: "container\_reference"

The environment type. Always `container_reference`.

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

type: "shell\_call"

agent?: Agent { agent\_name }

agent\_name: string

caller?: Direct { type }  | Program { caller\_id, type }  | null

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseFunctionShellToolCallOutput { id, call\_id, max\_output\_length, 6 more }

The output of a shell tool call that was emitted.

id: string

The unique ID of the shell call output. Populated when this item is returned via API.

call\_id: string

max\_output\_length: number | null

The maximum length of the shell command output. This is generated by the model and should be passed back with the raw output.

output: Array<Output>

An array of shell call output contents

outcome: Timeout { type }  | Exit { exit\_code, type }

Represents either an exit outcome (with an exit code) or a timeout outcome for a shell call output chunk.

Timeout { type }

Indicates that the shell call exceeded its configured time limit.

type: "timeout"

The outcome type. Always `timeout`.

Exit { exit\_code, type }

exit\_code: number

Exit code from the shell process.

type: "exit"

stderr: string

The standard error output that was captured.

stdout: string

The standard output that was captured.

created\_by?: string

The identifier of the actor that created the item.

status: "in\_progress" | "completed" | "incomplete"

The status of the shell call output. One of `in_progress`, `completed`, or `incomplete`.

"in\_progress"

"completed"

"incomplete"

type: "shell\_call\_output"

The type of the shell call output. Always `shell_call_output`.

agent?: Agent { agent\_name }

agent\_name: string

caller?: Direct { type }  | Program { caller\_id, type }  | null

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

type: "program"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseApplyPatchToolCall { id, call\_id, operation, 5 more }

A tool call that applies file diffs by creating, deleting, or updating files.

id: string

call\_id: string

operation: CreateFile { diff, path, type }  | DeleteFile { path, type }  | UpdateFile { diff, path, type }

One of the create\_file, delete\_file, or update\_file operations applied via apply\_patch.

CreateFile { diff, path, type }

Instruction describing how to create a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to create.

type: "create\_file"

Create a new file with the provided diff.

DeleteFile { path, type }

Instruction describing how to delete a file via the apply\_patch tool.

path: string

Path of the file to delete.

type: "delete\_file"

Delete the specified file.

UpdateFile { diff, path, type }

Instruction describing how to update a file via the apply\_patch tool.

diff: string

Diff to apply.

path: string

Path of the file to update.

type: "update\_file"

Update an existing file with the provided diff.

status: "in\_progress" | "completed"

"in\_progress"

"completed"

type: "apply\_patch\_call"

agent?: Agent { agent\_name }

agent\_name: string

caller?: Direct { type }  | Program { caller\_id, type }  | null

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

type: "program"

created\_by?: string

The ID of the entity that created this tool call.

BetaResponseApplyPatchToolCallOutput { id, call\_id, status, 5 more }

The output emitted by an apply patch tool call.

id: string

call\_id: string

status: "completed" | "failed"

"completed"

"failed"

type: "apply\_patch\_call\_output"

agent?: Agent { agent\_name }

agent\_name: string

caller?: Direct { type }  | Program { caller\_id, type }  | null

Direct { type }

type: "direct"

Program { caller\_id, type }

caller\_id: string

type: "program"

created\_by?: string

The ID of the entity that created this tool call output.

output?: string | null

Optional textual output returned by the apply patch tool.

McpListTools { id, server\_label, tools, 3 more }

A list of tools available on an MCP server.

id: string

server\_label: string

tools: Array<Tool>

input\_schema: unknown

name: string

annotations?: unknown

description?: string | null

type: "mcp\_list\_tools"

agent?: Agent | null

agent\_name: string

error?: string | null

McpApprovalRequest { id, arguments, name, 3 more }

A request for human approval of a tool invocation.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_approval\_request"

agent?: Agent | null

agent\_name: string

McpApprovalResponse { id, approval\_request\_id, approve, 3 more }

A response to an MCP approval request.

id: string

approval\_request\_id: string

approve: boolean

type: "mcp\_approval\_response"

agent?: Agent | null

agent\_name: string

reason?: string | null

McpCall { id, arguments, name, 7 more }

An invocation of a tool on an MCP server.

id: string

arguments: string

name: string

server\_label: string

type: "mcp\_call"

agent?: Agent | null

agent\_name: string

approval\_request\_id?: string | null

error?: string | null

output?: string | null

status?: "in\_progress" | "completed" | "incomplete" | 2 more

"in\_progress"

"completed"

"incomplete"

"calling"

"failed"

BetaResponseCustomToolCallItem extends [BetaResponseCustomToolCall](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call%20%3E%20(schema)) { call\_id, input, name, 5 more }  { id, status, created\_by }

id: string

The unique ID of the custom tool call item.

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

BetaResponseCustomToolCallOutputItem extends [BetaResponseCustomToolCallOutput](/api/reference/typescript/resources/beta#(resource)%20beta.responses%20%3E%20(model)%20beta_response_custom_tool_call_output%20%3E%20(schema)) { call\_id, output, type, 3 more }  { id, status, created\_by }

id: string

The unique ID of the custom tool call output item.

status: "in\_progress" | "completed" | "incomplete"

"in\_progress"

"completed"

"incomplete"

created\_by?: string

The identifier of the actor that created the item.

### List input items

TypeScript

import OpenAI from "openai";
const client = new OpenAI();

const response = await client.responses.inputItems.list("resp_123");
console.log(response.data);

  "object": "list",
  "data": [
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
          "type": "input_text",
          "text": "Tell me a three sentence bedtime story about a unicorn."
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false

  "object": "list",
  "data": [
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
          "type": "input_text",
          "text": "Tell me a three sentence bedtime story about a unicorn."
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false
